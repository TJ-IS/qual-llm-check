---
otero_id: 3708
otero_key: "KXXEJ5SN"
title: "Knowledge management-centric help desk: specification and performance evaluation"
authors: "Luz Minerva González; Ronald E. Giachetti; Guillermo Ramirez"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.04.013"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Knowledge management-centric help desk: specification and performance evaluation

Luz Minerva Gonza´lez, Ronald E. Giachetti\*, Guillermo Ramirez

Department of Industrial and Systems Engineering, Florida International University, 10555 W. Flagler Street, Miami, FL 33199, USA

Received 21 February 2003; received in revised form 20 April 2004; accepted 21 April 2004 Available online 1 June 2004

## Abstract

The technology help desk function has grown in importance as information technology has proliferated throughout the organization. The primary objective of the help desk is to resolve problems related to IT in the organization. As such, the agents in the help desk must be very knowledgeable of the information systems, applications, and technologies supported. Most efforts at improving help desk performance have been to make the current system more efficient through application of information technologies. In this paper we propose a new approach, called a knowledge management-centric help desk. The proposed knowledge management system draws upon diverse knowledge sources in the organization including databases, files, experts, knowledge bases, and group chats. The knowledge management system is designed to be incorporated into the daily operation of the help desk in order to ensure high utilization and maintenance of the knowledge stores. The benefits of the knowledge management-centric help desk are evaluated using a simulation study with actual data from a help desk. The experimental results indicate the knowledge management-centric approach would significantly reduce the time to resolve problems and improve the throughput of the help desk. <sup>D</sup> 2004 Elsevier B.V. All rights reserved

Keywords: Help desk system; Knowledge management system; Knowledge-based system; Expert systems; Simulation evaluation

## 1. Introduction

Help desks serve an important role of the information technology department by providing the primary point of contact for clients to contact analysts to help them resolve problems with information technology including hardware, software, and networks. To resolve the information technology problems reported by callers, the help desk analysts must possess knowledge of the information technologies supported by the help desk. Knowledge has been defined as, ‘‘a justified personal belief that increases an individual’s capacity to take effective action’’ [2,30]. The product of the help desk is this knowledge. Acquiring and maintaining the knowledge to support these information technologies is becoming increasingly difficult. According to a study conducted by the Gartner Group, the average number of information technologies supported by help desks has increased from 25 to 2000 in the past 5 years [34]. One reason for the increase is the proliferation and distribution of information technology such as different personal computers, software applications, printers, and servers throughout the organization. Moreover, Sharer [24,36] finds that the more distributed the information technology, the more support the end users require. As a result, help desks have experienced both an increase in the number of information technologies they must support and an increase in workload.

There are two types of help desks depending on whether the clients served are internal or external to the organization [17,40]. Internal help desks are usually organized as part of the IT Department. It has been observed that the internal help desk has a great impact on the productivity of the organization since the help desk is resolving problems that may stop, delay, or otherwise impact the completion of daily business activities [18]. As an example, in the company we studied a problem with a network router prevented employees from accessing an important server. Such a problem has significant deleterious effect on the productivity of the affected employees since they could not perform their primary job function. The faster the help desk can troubleshoot and resolve the problem the better [20,24]. External help desks are for paying clients of the company who have service agreements for technical support. In the case of the external help desk, it is an important value-added service provided to the client. The speed and quality of the solutions provided influence customer satisfaction and therefore the business’s image [12,17].

In the traditional help desk, the agent is responsible for handling a call and solving the problem by resorting to various information and knowledge sources [24]. We call this an agent-centric help desk. There are at least two problems with the agent-centric approach. The first problem is of recognizing repeat problems as such. Help desk personnel report about 60 – 70% of their time is spent on solving repeat problems [34,37]. However, when the help desk receives a problem call, it may be assigned to an agent who has not previously resolved that type of problem. The agent-centric help desk does not capture an agent’s knowledge about resolving a particular situation in a way that it can be searched, reviewed, disseminated, and updated by others. Consequently, the benefits of learning are not fully realized because the structure of the agent-centric help desk does not facilitate sharing knowledge. The second problem is that in today’s business environment employee turnover is high, especially for technical employees [11]. In the help desk this is a problem because the help desk performance is heavily dependent on the knowledge, skills, and ability of the help desk agents to quickly resolve problems. Help desk agents are stores of significant knowledge concerning the systems, business processes, and technologies and if they leave their knowledge often goes with them [27,32]. These two problems reduce both the efficiency and effectiveness of the help desk.

The two problems identified with an agent-centric help desk are both related to the ability of the help desk to acquire, maintain, and disseminate the knowledge of all the agents. In this paper we present a knowledgecentric help desk system that addresses these two problems by improving how knowledge is managed by the help desk. Knowledge management is a discipline that provides strategy, process, and technology to share and leverage information and expertise that will increase our level of understanding to more effectively solve problems and make decisions [35].

In the next section we review help desk operations and trends. Then we examine knowledge management practices and technologies. A knowledge management-centric help desk system is defined. To evaluate the benefits of the proposed system we perform experiments to compare the agent-centric to the knowledge-centric system. Actual data from an internal IT help desk was collected and used to create a simulation model. A three factor two level experiment was conducted. The results are presented and conclusions are drawn in the last section. Our contributions are first the specification of a knowledge-based centric help desk and second the performance evaluation of the system using actual industry data.

## 2. Help desk operations and technologies

An agent resolves a problem by accessing many different information and knowledge sources as shown in Fig. 1. These sources range from files on the agent’s computer, access to the database, communication with other agents, and access to the Internet. We call this the agent-centric approach since the onus of finding and collecting the requisite information and knowledge to solve a problem is the responsibility of the agent.

![](/api/attachments/KXXEJ5SN/fulltext/images/2249b39b2591669606fd34cde61b8d316d4fce7b9475d3250d90e8cfe85be434.jpg)  
Fig. 1. Typical help desk with agent-centric collection of data, information, and knowledge.

In automating the agent-centric help desk, many have focused on computer– telephony integration (CTI). The basis of CTI is to integrate computers and telephones so they can work together seamlessly and intelligently [10]. The major hardware technologies are as follows: Automatic call distributor (ACD); voice response unit (VRU), Interactive voice response unit (IVR), predictive dialing, headsets, and reader bounds [3,4]. These technologies are used to make the existing process more efficient by minimizing the agent’s idle time and evenly loading the agents in the help desk. These technologies do not address the problem of knowledge loss when agents leave nor do they provide information to the agent in helping to resolve problems.

Several authors have investigated the application of case-based reasoning systems to improve the performance of help desks [7,8,14,37]. Case-based reasoning captures, stores, and adapts solutions to old problems to use them to solve ether recurrence of the old problem or a new problem [21]. The storage of knowledge is in the form of cases in which each case describes a problem that may occur and a solution to that problem. The cases are organized according to a taxonomy. For example, Go¨ker and Roth-Berghofer [14] use a failure description that comprises the topic, subject, and behavior of the failure. Using the classifications, the help desk agents can search for cases that match the current problem they are handling. To develop a case-based system the knowledge must be captured and represented in the form of these cases. The knowledge acquisition process reported by Chan et al. [7] was through interviewing the more experienced help desk agents. An issue for case-based systems is continuing the acquisition of knowledge in the form of new cases after the initial development of the system. Go¨ker and Roth-Berghofer [14] found that the acquisition process and the maintenance process are as important as the technology installed. In their approach they recommend a separate case author who is in charge of system maintenance and incorporating new cases into the system.

A related approach is instead of finding related cases the system can store information on experts and their expertise so that the agent can be guided to the appropriate expert for solving a problem. These types of systems are called people finders or expert finders and several exist such as the one at HP and the SAGE system developed for the Florida State University Systems [6].

The research shows that case-based reasoning is an appropriate technology for help desk applications. However, there are four outstanding issues concerning the application of case-based systems for help desks that should be addressed. The first issue is the cases are the only source of knowledge in the system and often ignore available information and knowledge sources outside of the case-based system. Taylor et al. [39] found that help desk agents access a wide variety of knowledge sources. One of the more important knowledge sources is not embedded in physical systems but in the employees themselves [23,39]. Secondly, cases are intended for helping resolve recurring problem types and provide little support for resolving new problem types. Consequently, a case-based system alone is insufficient for the help desk environment. A third issue is updating and maintaining the knowledge in the system is perceived as difficult [22]. The provisions for continued knowledge acquisition are weak since new knowledge must be formulated in the structure of a case. Often, a systems expert knowledgeable in the support system and programming language is responsible for system maintenance and generation of new cases. These systems run the risk of becoming outdated since generation of cases is often not a continuous process. IT help desks that support dynamic and rapidly changing technical products need continuous knowledge acquisition; otherwise, the knowledge base would quickly become obsolete. The fourth issue is overemphasis on the technology solution withou reengineering the supported business process often fails. Nissen et al. [29] assert that information technology must be integrated with the design of the process it supports. In the domain of knowledge systems they find the literature provides little discussion of incorporating knowledge-based systems into the process. Likewise, Weber et al. [41] found that many knowledge management systems are not incorporated into the processes the systems support. The repercussion is the systems are underutilized and as a result do not achieve their goal of knowledge-sharing.

While case-based reasoning systems enable help desks to store and share knowledge in the form of cases, there is room in improvement by addressing the aforementioned issues. The strategy taken in this article is that instead of relying on a single technology such as case-based reasoning, the coordination of several technologies and their integration into the business process could improve the productivity and effectiveness of the help desk. Knowledge management is used as the framework for integrating the technologies, people, and process for improved help desk performance.

## 3. Knowledge management

Knowledge management is about acquisition and storage of employees’ knowledge and making the knowledge accessible to other employees within the organization [1,26,27,35]. Nonaka and Takeuchi [31] have extensively studied knowledge in the organization and developed a model that describes knowledge as existing in two forms. Tacit knowledge is defined as personal, context-specific knowledge that is difficult to formalize and communicate. Explicit knowledge is factual and easily codified so that it can be formally documented and transmitted. Through knowledge management a company changes individual’s knowledge into organizational knowledge [38]. Organizational knowledge is knowledge held by the organization. The organization maintains the organizational knowledge in organizational knowledge resources which are operated on by human or computer processes that manipulate the knowledge to create value for the organization [19].

Nonaka and Takeuchi [31] define organizational learning as, ‘‘a process that amplifies the knowledge created by individuals and crystallizes it as part of the knowledge network of the organization.’’ In a help desk environment, much of the knowledge is from experiential learning [24,39]. A challenge is how to transfer the knowledge gained by individuals into organizational knowledge.

Many authors have described processes for knowledge management [13,26,33,35]. Nissen et al. [29] review several knowledge management process models and propose an amalgamated process that involves the following steps: (1) collecting knowledge, (2) organize knowledge, (3) storing knowledge, (4) making knowledge available, (5) using the knowledge, and (6) knowledge evolution. Technology is available to support each one of these knowledge management process steps [29]. Knowledge management systems (KMS) are systems that gather, organize, and disseminate an organization’s knowledge as opposed to information or data [1].

For the help desk, the relevant knowledge management approach is of problem solving. Gray [16] presents a framework that categorizes knowledge management according to a problem-solving perspective. The framework defines four cells according to the type of problem and the process supported. Along the horizontal axis they define two classes of problems as new problems and previously solved problems. Along the vertical axis they define two processes of problem recognition and problem solving. The primary function of the help desk is problem solving of both new and previously solved problems. When solving new problems, Gray [16] calls this knowledge creation. Solving previously solved problems is called knowledge acquisition.

Several characteristics can be defined that would make a KMS successful in the help desk. The KMS must be able to gather knowledge from humans and other sources. In a help desk environment, the information and knowledge resides in many disparate forms such as databases, files, people, electronic documents, and procedures. Part of the knowledge management task is the coding and classification of the stored information and knowledge so that it can be put to use by help desk agents in resolving problems.

## 4. A knowledge management system for a help desk

The knowledge management-centric approach to a help desk is shown in Fig. 2. In this approach the knowledge management system (KMS) serves as an intermediary between the help desk agent and all data, information, and knowledge sources. The strength of this approach is twofold; first by becoming the intermediary all information passes through the system and thus should facilitate the knowledge acquisition function. Knowledge acquisition is often an obstacle [22], since busy knowledge-workers may overlook the capturing of knowledge into the system and thus the KMS would stagnate. A second advantage of the knowledge management-centric system is it specifies a single uniform interface for the help desk agent to access various knowledge sources. It is recognized that the help desk agent must access a multitude of knowledge sources with different file formats, at remote locations, and often organized differently. Except for the knowledge base, the knowledge from the other sources are not organized since the knowledge sources are external to the system. Rather the interface for searching for the knowledge is organized. The knowledge management system points to the location where the knowledge can be found. For example, if the knowledge resides in a document on a file server, the knowledge management system contains an entry for the knowledge source and a pointer to link the location to the entry.

![](/api/attachments/KXXEJ5SN/fulltext/images/c25eac38c730f90a3cd922c060fe9e35236a81d56a2c7512e835af0d02161473.jpg)  
Fig. 2. Knowledge management-centric help desk.

The knowledge management system is designed to support both tacit and explicit knowledge as classified by Nonaka and Takeuchi [31]. To accomplish this goal the proposed knowledge management system integrates several technologies including group-ware, information retrieval, and document management. The group-ware element is the ability to collaborate on a problem with other help desk agents and to access them through the system. The group-ware aspect addresses tacit knowledge, which is personal and context-specific making it difficult to formalize. The information retrieval element is evident in the ability to access remote information whether in a database, on the Internet (such as a FAQ from a vendor), or document files. Document management is evident in the storage and indexing of documents on file servers. The later two technologies address explicit knowledge, which can be codified.

An important element of the knowledge management system is organizing access to the knowledge so that it can be retrieved as needed. Knowledge is organized according to a taxonomy of problem scope, product, and feature. The taxonomy is context-specific to the help desk and how the help desk agents perceive the problem domain. Problem scope describes the general type of problem such as software, hardware,

![](/api/attachments/KXXEJ5SN/fulltext/images/6c43d9061f2017fca5e46f2872cf9c2f1f29ed79dce68f2e5988ff06b3aa4f6e.jpg)  
Fig. 3. Prototype input screen for search.

or network. The product is the specific product the problem is being experienced with. The feature is an identification of the feature in that product causing the problem. The knowledge management system interface is shown in Fig. 3 to illustrate how the taxonomy is used to access various knowledge sources. On the left-hand side are the search criteria for the problem. On the right-hand side there are knowledge sources including experts for the identified problem, documents that match the problem, associated files, and knowledge bases. Experts in the system are selfclassified according to the taxonomy described above. Some of the identified sources such as the documents that match the problem may or may not help the agent in resolving the call. The knowledge bases are cases as used in the case-based reasoning approach. These cases would be directly relevant to the problem and can be adapted to solve the current problem.

Implementation of the knowledge management system changes the problem resolution process followed by the help desk and the new process is shown in Fig. 4. A short examination of the process flow shows several potential performance enhancers. First, it is possible that the help desk clerk, usually a lower skill job classification than a support agent, can with the aid of the KMS resolve the problem. This is possible when the client’s problem matches a case in the system. Then both the time to resolve a problem will be improved and at a lower wage rate than if utilizing a support agent. The second potential performance improvement is that through the knowledge management system the help desk agent can leverage the organization’s knowledge and solve the problem faster than if working without the knowledge management system.

![](/api/attachments/KXXEJ5SN/fulltext/images/379c0296925072b8ee40e4a701054d0cf4b8dbc636001cfe35f195d920da7c3d.jpg)  
Fig. 4. Knowledge management-centric help desk resolution process flow.

The knowledge management-centric system helps achieve organizational learning. When a problem is resolved by any agent then the solution becomes part of the organizational memory and is available to all other agents. The knowledge management system is incorporated into the processes of the help desk. Acquisition of new knowledge and maintenance of the knowledge is not a separate process. Consequently, we address the concerns raised by Weber et al. [41] that show low system utilization when the system is not incorporated into the business process.

## 5. Performance evaluation of the knowledge management-centric help desk

The research objective is to analyze the performance of the knowledge management-centric help desk system. The research hypothesis is the knowledge management-centric system will have a shorter problem resolution time. A shorter problem resolution time will occur because the knowledge management system will facilitate organizational learning and will enable agents to access knowledge sources acquired by the entire group which will enable them to resolve the problem faster. A second reason the knowledge management-centric system will reduce the problem resolution time is many calls that would have been elevated can be solved at a lower level, which would greatly reduce the time to resolve that problem. A consequence of a shorter resolution time should be a higher throughput and a decrease in the average queue size for problems. Formally, the hypothesis is:

Hypothesis 1. The time in system for all problem calls except for critical severity calls will be lower in the knowledge management-centric system than the agent-centric system.

The hypothesis excludes a class of calls termed critical severity because these are typically handled specially. More on the call classification is discussed in a later section. To test the hypothesis a simulation model is developed that describes the current agentcentric help desk and the knowledge managementcentric help desk. Several authors have studied help desks and/or help desks using simulation techniques. Simulation enables help desks to perform analysis that captures the entire interrelationship between callers, agents, skills, and technology [5,9,28]. For example, Chin and Sprecher [9] analyzed the impact of staffing levels on a goal of meeting a service level agreement of 95% calls answer rate. In this case, the simulation model research approach is adopted so that we can conduct experiments to evaluate the knowledge management system without disrupting the help desk’s daily operations. The simulation enables an evaluation of the performance of the knowledge management system prior to full-scale implementation in the help desk. The simulation model will help to analyze the benefits or advantages that can be obtained with the implementation of the knowledge management system.

## 6. Description of current agent-centric help desk

Here we describe a particular information technology (IT) help desk of a fortune 500 company in the hospitality industry. IT is a component of the firm’s strategy. The mission of IT is to assist the business units in achieving their strategies and to recommend technology applications to accomplish greater operating efficiency, improved client experience and increased revenues. One of the main areas of interested of IT is the Problem Management Process owned by the help desk that is the process of detecting, correcting, and reporting problems impacting services committed by the business and supported by IT. Incidents such as hardware, software, applications, operations, and facilities failures cause these problems. The goal of problem management is to provide a process to resolve problems caused by these failures in the most expeditious and cost-effective manner, and to ensure that the analysis is done on a regular basis to fix recurring problems.

When the help desk was first formed, it was composed of a single person that attended to the phone calls and wrote down on a paper form the problems to be solved. Oftentimes, to resolve a simple problem, like connections to printers, took as much time as a week. This process was very inefficient; many calls were abandoned due to the phone line being busy. The problem reporter had to leave a message in the voice mail and if this was full, the problem reporter did not have another way to communicate with the help desk agent. The calls waited in the voice mail queue until the single agent had time to check it and either resolve or assign the problem to someone else.

Two years ago, the company has changed to a multi-person and multi-tier help desk. Now, the help desk is composed of four support levels. The first level includes the agents who answer the telephone calls. The second level is called senior support and consists of the senior help desk agents. The third level includes specialists who do not directly work for the help desk but are called when a problem occurs in their specialty. The fourth level includes the technicians who will travel to the business unit to make any necessary repairs and resolve the problem. Also, now a computer telephony integrated software package, called Remedyk, is used to track calls and their resolution. Remedyk features ensure that a case is entered quickly and tracked through its life cycle and thus provide a better service.

According to Marcella [24], many help desks are organized in a similar fashion to the one described above. Marcella [24] found that most help desks have several support levels, they utilize technology for tracking calls and performance, their organizational focus is limited to problem resolution, the use of AI/knowledge bases is limited, and they rely primarily on staff expertise. The majority of help desks came into being by ‘‘evolutionary’’ means, i.e. developed in reaction to demand. Consequently, the one described here is not unlike many other help desks.

Fig. 5 shows the possible flow of problems through the current help desk as modeled in the simulation. A calling population of calls arrives to the agents at the first level. When an agent of the help desk answers a call, they check if the problem has been previously reported in order to update it and inform the problem reporter about the status of the ticket or generate a new ticket, where the ticket is a mechanism for tracking problems. If the problem has never been reported the agent (first level) attempts to solve it. If the problem is solved in the first level and there are no other problems, the call is finished and the agent completes the ticket form and closes it. If the problem cannot be solved at the first level, the operator appends additional information and assigns a priority to the problem. The priority is assigned according the following criteria:

![](/api/attachments/KXXEJ5SN/fulltext/images/e304914e0793110c910922096e775f26de28812c71215fccfd42a893aaee6f8e.jpg)  
Fig. 5. Conceptual model of help desk operations.

Critical severity: A system or a major system component is down or unavailable to a substantial portion of the user community, or the user cannot conduct critical business operations that will result in a significant loss of revenue, profit, or productivity.

High severity: A problem that causes a partial or potential system or application outage.

Medium severity: A problem that must be resolved but does not impact the service level commitments of the information technology organization. The problem does not severely impede the user’s ability to conduct business and/or it can be circumvented. Low severity: A low impact problem that does not require immediately resolution, as it does not directly affect the user’s productivity or system or application availability.

Similar prioritization is implemented in most help desks. According to the priority, the problem is assigned to an agent or technician who is responsible for resolving the problem.

The system represents an agent-centric help desk as previously described. This means that an agent determines a solution for the problem and this information is stored in personal files or database that the agent in the future can use to resolve similar problems. However, this information is not shared among the rest of the agents. Then, if a similar problem arrives to a second agent, that agent has to start researching the problem without any base and will spend approximately the same amount of time that was spent by the first agent.

## 7. Data collection

Prior to data collection unstructured interviews were held with the management and help desk agents. The purpose of the interviews was to learn the help desk operating procedures, the key performance indicators (KPI), demand levels, and to obtain insight from the agents working in the help desk. The KPIs are management performance tools to help determine the help desk performance in meeting objectives and established service level agreements. Among the KPIs identified the relevant ones to our study were: (1) number of calls received versus number of calls abandoned; (2) number of calls resolved at first contact; and (3) average time to resolve a problem at each level. Based on these KPIs, the data requirements were identified in order to build a simulation model.

Data was collected from the Remedyk CTI system for four separate weeks randomly selected from a 6- month period starting in January to June. The data collected was for a total of 4965 calls and consisted of the time between arrivals, number of resources, types of calls, and service times. Sample data is provided in Appendix A. It is noted that some problems do not have a recorded resolve time. The interviews with the help desk agents indicate that these calls are handled at first contact and resolved within less than 2 min. The Remedy system cannot provide data of abandoned calls. The interviews with the help desk agents suggest that this was generally not a problem for the help desk. An analysis of staffing levels and arrival patterns confirm that abandoned calls were not an issue.

The arrival rate determines the demand load of the help desk. The arrival rate depends on the day of the week. For each day of the week a statistical analysis was performed on the data to fit a probability distribution to the data. It was observed that Mondays have the highest average arrival rate of 27 calls/h and Sunday has the lowest average arrival rate at 2 calls/h.

Table 1  
Frequency of each category

<table><tr><td>Problem category</td><td>Percentage of frequency</td></tr><tr><td>Phone Call</td><td>25.40</td></tr><tr><td>Network</td><td>22.98</td></tr><tr><td>Software</td><td>22.88</td></tr><tr><td>AS400</td><td>12.79</td></tr><tr><td>Hardware</td><td>5.32</td></tr><tr><td>Software Ship</td><td>3.95</td></tr><tr><td>Telecom</td><td>1.35</td></tr><tr><td>Remote Access-DSM</td><td>1.03</td></tr><tr><td>Database System</td><td>1.01</td></tr><tr><td>Procurement</td><td>0.95</td></tr><tr><td>Remote Access-General</td><td>0.77</td></tr><tr><td>Remedy</td><td>0.62</td></tr><tr><td>Support SVC Calls</td><td>0.32</td></tr><tr><td>Communications</td><td>0.28</td></tr><tr><td>Data Transmission</td><td>0.28</td></tr><tr><td>Backups Ships</td><td>0.08</td></tr></table>

Table 2  
Classification of calls by priority

<table><tr><td>Priority</td><td>No. of calls</td><td>%</td></tr><tr><td>Low</td><td>4488</td><td>90.39</td></tr><tr><td>Medium</td><td>256</td><td>5.16</td></tr><tr><td>High</td><td>200</td><td>4.03</td></tr><tr><td>Critical</td><td>21</td><td>0.42</td></tr><tr><td>Totals</td><td>4965</td><td>100.00</td></tr></table>

The problems are classified into 16 categories as shown in Table 1 with their frequency of occurrence. A Pareto phenomenon is observed whereby the top seven problem categories account for 94.67% of the total types of calls received. The frequency of each priority is shown in Table 2.

The service times for each problem category were analyzed and determined. The service time is the time between logging a problem call and the time the problem is resolved. The service time is correlated to the problem category and assigned level. For each problem category a probability distribution was fitted to the data collected to arrive at a function for service time to be used in the simulation model.

## 8. The simulation model

The agent-centric and knowledge managementcentric help desks were modeled in the simulation package Arenak. Arenak is a commercial discreteevent simulation package. A full exposition of the simulation model is available in [15]. The simulation model was verified to make sure that it works properly in terms of Arenak functionalities and the entities (problem calls) follow the same path as described in the conceptual model. The verification was done using the Trace function. The Trace was run for one replication for 4 weeks of operation time. The Trace output allows following the sequence of an entity as it flows through the system, from entity creation until entity disposal. The knowledge management-centric help desk simulation model was also verified using the Trace function. The logic and entity process flow was determined to agree with the intended design. In addition to verifying the Trace output, the model was run with different replication numbers to verify that it works under different conditions.

After verifying operation of the simulation model it was validated. Four replications were conducted with different random number streams on the simulation model. A t-test with a 95% confidence level was conducted to compare the results of the simulation model with the results recorded for the actual system based on the data collected from Remedyk. For each variable the null hypothesis of no difference between the systems was rejected with a 95% confidence level which indicates the simulation model adequately represents the actual system’s behavior.

## 9. Experimental design and analysis

The purpose of the experimental design is to identify the effects of three different factors on five dependent variables. The factors are:

Factor A: Time to type problem information and search the knowledge management system for relevant knowledge sources (minutes).

Factor B: Time to resolve a problem using the knowledge management system (minutes).

Factor C: Time to add new information into the knowledge management system (minutes).

The dependent output variables are:

O1: Throughput (Total number of calls resolved in time period)

O2: Time in the system of critical priority problems (minutes)

O3: Time in the system of high priority problems (minutes).

O4: Time in the system of medium priority problems (minutes).

O5: Time in the system of low priority problems (minutes).

O6: Number of problem calls in technicians’ queue.

O7: Number of problem calls in second level queue.

O8: Number of problem calls in third level queue.

The dependent variables are performance variables tracked by the help desk and according to Anton and Gusting [4] these are common performance measures. A different output variable is needed for each problem priority since they follow different paths through the help desk.

The factors are analyzed with two levels (low and high). The values for low and high were determined by expert opinion obtained during the interviews and by observing the help desk operations. Table 3 shows the factors and their respective levels.

The experimental design is a full factorial of two levels and three factors $\bar { 2 } ^ { 3 }$ , giving a total of eighttreatment combination. Table 4 shows the combination of these factors and their levels (1 = low and $2 = \mathrm { { h i g h } ) }$ for each experiment, which is a cell in the table. Six replications of each of the eight experiments were run in a random order and the results were recorded for further statistical analysis. Each simulation experiment was for 1 week (17,640 min). The same random number seed was used for the agent-centric and the knowledge management-centric models. The summarized results are shown in Table 5.

The analysis of variance (ANOVA) for full factorial design is done to test that the main effects or interaction parameters are equal to zero. In statistical analysis, the factors with a P value lower than 0.05 $( P { < } 0 . 0 5 )$ are considered as important factors that significantly influence the results. The ANOVA analysis shows that only the dependent variable throughput (O1) is significantly influenced by Factor A, time to type and search the knowledge-base, and Factor B, time to resolve a problem using the knowledge management system. Time to add new information into the knowledge management system is marginally significant because the P value is equal to 0.05. The other dependent variables do not have any factors that affect them significantly (i.e. in all cases P>0.05).

Table 3  
Factors and their levels

<table><tr><td>Factor</td><td>Low (best case)</td><td>High (worst case)</td></tr><tr><td>A</td><td>3 min</td><td>6 min</td></tr><tr><td>B</td><td>Triangular (2, 5, 7 min) $^a$ </td><td>Triangular (4, 7, 10 min)</td></tr><tr><td>C</td><td>2 min</td><td>5 min</td></tr></table>

<sup>a</sup> Indicates a triangular distribution with these endpoints for min, mid, and max.

Table 4  
Eight-treatment combinations, $2 ^ { 3 }$ factorial experiments

<table><tr><td rowspan="4">Factor C</td><td colspan="4">Factor A</td></tr><tr><td colspan="2">FA Level 1</td><td colspan="2">FA Level 2</td></tr><tr><td colspan="2">Factor B</td><td colspan="2">Factor B</td></tr><tr><td>FB Level 1</td><td>FB Level 2</td><td>FB Level 1</td><td>FB Level 2</td></tr><tr><td>FC Level 1</td><td> $A_{1}B_{1}C_{1}$ </td><td> $A_{1}B_{2}C_{1}$ </td><td> $A_{2}B_{1}C_{1}$ </td><td> $A_{2}B_{2}C_{1}$ </td></tr><tr><td>FC Level 2</td><td> $A_{1}B_{1}C_{2}$ </td><td> $A_{1}B_{2}C_{2}$ </td><td> $A_{2}B_{1}C_{2}$ </td><td> $A_{2}B_{2}C_{2}$ </td></tr></table>

Table 6 shows the values of the t-statistic and the value of the t-critical two-tail (t-table) for each dependent variable. From Table 6, it can be noticed that in almost all the cases the p-value is lower than the t-statistic; this means that $H _ { 0 }$ is rejected. In other words, the means are not equal. This is the case for Throughput, Time in the System High Priority Calls, Time in the System Medium Priority Calls, Time in the System Low Priority Calls, Number of Problem in Technicians’ queue, and Number of Problem in Second Level’ queue. On the other hand, for Time in the System Critical Calls, and Number of Problem in Third Level’ queue can be seen that the $p \mathrm { - }$ value is higher than the t-statistic, then $H _ { 0 }$ is not rejected, then it is concluded that its means are equal.

Table 5  
Summary output for the agent-centric versus knowledge management-centric help desk

<table><tr><td>Variables</td><td>Agent-centric system (average)</td><td>Knowledge management-centric system (average)</td></tr><tr><td>O1: Throughput (calls/time period)</td><td>2733</td><td>3371</td></tr><tr><td>O2: Time in system critical calls (minutes)</td><td>416.73</td><td>329.74</td></tr><tr><td>O3: Time in system high priority calls (minutes)</td><td>503.07</td><td>240.54</td></tr><tr><td>O4: Time in system medium priority calls (minutes)</td><td>547.07</td><td>193.99</td></tr><tr><td>O5: Time in system low priority calls (minutes)</td><td>360.94</td><td>152.06</td></tr><tr><td>O6: Number of problem calls in technicians&#x27; queue</td><td>88</td><td>6</td></tr><tr><td>O7: Number of problem calls in second level&#x27; queue</td><td>103</td><td>25</td></tr><tr><td>O8: Number of problem calls in third level&#x27; queue</td><td>83</td><td>88</td></tr></table>

t-test for comparison of agent-centric system versus knowledgecentric system

<table><tr><td>Variables</td><td>t-statistics</td><td>t-critical two-tail</td></tr><tr><td>Throughput</td><td>29.488</td><td>2.571</td></tr><tr><td>Time System Critical Calls</td><td>0.653</td><td>2.571</td></tr><tr><td>Time System High Priority Calls</td><td>3.661</td><td>2.571</td></tr><tr><td>Time System Medium Priority Calls</td><td>3.737</td><td>2.571</td></tr><tr><td>Time System Low Priority Calls</td><td>6.939</td><td>2.571</td></tr><tr><td>Number of Problem in Technicians&#x27; queue</td><td>25.599</td><td>2.571</td></tr><tr><td>Number of Problem in Second Level&#x27; queue</td><td>13.354</td><td>2.571</td></tr><tr><td>Number of Problem in Third Level&#x27; queue</td><td>-1.527</td><td>2.571</td></tr></table>

## 10. Discussion of results

The intention of the hypothesis was to prove that applying a knowledge management system would decrease the time in the system of high, medium, and low priority calls. Table 5 shows the results for each priority level. At the low, medium, and high priorities, the knowledge management-centric system outperforms the agent-centric system significantly. The time in system for low priority calls was improved by 57.9%, for medium priority by 64.5%, and for high priority by 52.2%. At the critical priority level the t-test failed and no statistically significant difference can be concluded with confidence for critical priority problems. However, it was expected that there would be no significant improvement in resolving critical calls. Critical calls are nonrecurring problems that stop a system or have a significant detrimental impact on a business process. Critical calls are few in number (0.42%) and often require a specialist to make modifications to the effected application. The knowledge management system is not designed to support these types of calls.

The simulation output shows the knowledge management-centric system will have almost 19% higher throughput than the agent-centric system. This is a significant improvement. The knowledge management-centric system could lower the load for a stable level of calls thus releasing agents to perform other tasks. Or, the knowledge management-centric system could accommodate greater increases in calls from company growth without requiring additional support staff.

The knowledge management-centric system had 92.5% fewer calls in queue at the technician level. The reason for the large decrease can be attributed to more problems being resolved at the first level due to the knowledge provided by the system. Likewise, a 75.3% decrease in the number in queue at the second level was observed for the same reason.

The experiments show that the number in queue at the Third Level is the same for both the agentcentric and knowledge management-centric systems. The reason is the knowledge management system does not typically include this specialized knowledge for infrequent problems. The problems that are elevated to the Third Level often require the specialist to make modifications to the application in question in order to resolve the problem. The knowledge management system is not designed to support this activity.

The experiments indicate the potential cost benefits of the knowledge management-centric approach. Cost savings can be realized for several reasons. First, the knowledge management-centric approach enables the resolution of problems at lower levels. Typically, the agents at lower levels are also at lower salary levels. Second, the knowledge management-centric system resolves problems in a shorter time. If the problem was causing downtime to a business unit, this means the unit can resume normal operations faster. The decreased downtime is a cost savings. Furthermore, since the problems are resolved in a shorter amount of time, reductions in staffing requirements may occur. This staff can be used to improve the knowledge base or be assigned to other tasks within the organization.

The experiments were based on a comparison of two models, the agent-centric help desk and the proposed knowledge management-centric help desk. Extensive data for the former is available and was used to validate the model. The knowledge management system is in the prototype stage and has not been implemented in the help desk. Consequently, there is no actual data. The validity of the simulation model of the knowledge management system depends on the accuracy of the data used in Table 3 for the three input factors. If following implementation it was found that the values deviate far from the values used, then this would invalidate the results of the experiments.

Other issues in the knowledge management system still require further investigation. First, the identification of experts is currently by self-identification but a potential enhancement is to classify experts based on the problems they solve. This can be accomplished so that an agent who resolves a high number of problems associated with technology X would become an expert in technology X. The system could also incorporate keystroke logging and similar technologies to facilitate the creation of new cases. A further enhancement would be an indication of the usefulness or relevance of the source based on how many times it has been previously used such as done with Internet search engines.

## 11. Conclusion

The article makes two contributions. The first contribution is the specification of a knowledge-centric system for a help desk. The knowledge-centric system incorporates aspects of case-based reasoning systems, expert people finders, and group-ware systems, and indexes them for easy retrieval by help desk agents. The integration of several disparate knowledge sources enables the knowledge-centric system to support resolution of both repeat problems as well as new problems. The knowledge-centric system is centralized and integrated into the help desk process to better ensure its use while making maintenance and evolution a part of the everyday business activities. Thus, the knowledge management-centric system avoids the problems associated with systems that require specialized personnel to periodically update the knowledge contained in the system. Because all problems and problem solutions pass through the knowledge management system this information and knowledge becomes available to all help desk agents. Thus, the knowledge is captured by the organization as well as by the individual and promotes organizational learning.

The research hypothesis was that the use of several knowledge sources and the incorporation of the knowledge management system as the centralized component of the help desk would lead to performance improvements. The second contribution was to conduct a discrete-event computer simulation to quantitatively compare the agent-centric and knowledge management-centric help desk. The simulation study showed a greater than 50% decrease in average time to resolve a problem and a 19% increase in throughput. These improvements are significant and provide justification for implementing the knowledge management system. The advantage of simulation is to conduct a study without disrupting the operations of the actual help desk. Moreover, we are able to evaluate the proposed system prior to installation.

There are several issues related to the adoption of a knowledge management system into the help desk organization that are not addressed. The experiments were conducted with the assumption that cases existed for the top 20% of the problems, which account for almost 80% of the calls. Consequently, the experimental results are only valid with the preexistence of a knowledge base. As Ref. [14] recommend, new installations of knowledge management systems should have sufficient cases to cover at least some of the problems likely to be encountered. If the knowledge management system were installed with no cases in its knowledge base, then there would probably be no performance improvement. However, it is noted the system also is an expert-finder and group-ware system, so these components of the system could aid problem resolution. The centralized architecture of the system was designed so that it would not hinder the problem resolution process even when no cases are found. The power of simulation is that different assumptions, such as no knowledge base, could be quickly evaluated. A second issue not addressed is the cultural barriers to acceptance and adoption of the system. Adoption of technology and unwillingness to share knowledge are well-documented [25]. Computer simulation experiments are not the best way to examine cultural issues or human acceptance of a system.

## Acknowledgements

Luz Minerva Gonza´lez would like to acknowledge the financial support of Royal Caribbean Cruise Lines during the completion of this project.

Appendix A. Sample data collected from Remedy CTI System

<table><tr><td>Ticket number</td><td>Arrived date</td><td>Arrival time</td><td>Resolved date</td><td>Resolved  $time^a$ </td><td>Priority</td><td>Group+</td><td>Category</td><td>Description</td></tr><tr><td>MIA-000506-0001</td><td>05/06/00</td><td>7:58</td><td></td><td></td><td>Low</td><td>Customer Care</td><td>NETWORK</td><td>NETWORK SECURITY PASSWORD</td></tr><tr><td>MIA-000506-0002</td><td>05/06/00</td><td>8:41</td><td>5/6/00</td><td>8:41</td><td>Low</td><td>Customer Care</td><td>SOFTWARE</td><td>Error performance operation when updating the virus definitions.</td></tr><tr><td>MIA-000506-0003</td><td>05/06/00</td><td>8:43</td><td></td><td></td><td>Low</td><td>Customer Care</td><td>NETWORK</td><td>NETWORK SECURITY LOCKED OUT</td></tr><tr><td>SVS-000506-0001</td><td>05/06/00</td><td>9:01</td><td>5/12/00</td><td>16:58</td><td>Medium</td><td>Customer Care Level-2</td><td>SOFTWARE (SHIP)</td><td>There appears to be some problem with the cross mounted drive permissions. Users are having trouble running programs which previously worked; these programs work under the administrative logins (ss1/ss2) but not under ttyxxx logins. This appears to be independent of the Encore login. The programs known to be affected so far are: Prepaid Gratuities Crew APIS reports Crew Resolution Reports We need to find a solution to these issues. They can be run the Systems Manager at this time, but this is only a temporary solution.</td></tr><tr><td>MIA-000506-0004</td><td>05/06/00</td><td>9:13</td><td></td><td></td><td>Low</td><td>Customer Care</td><td>NETWORK</td><td>NETWORK SECURITY LOCKED OUT</td></tr><tr><td>MIA-000506-0005</td><td>05/06/00</td><td>9:16</td><td></td><td>3.56</td><td>Low</td><td>Customer Care</td><td>NETWORK</td><td>NETWORK SECURITY PASSWORD</td></tr><tr><td>MIA-000506-0006</td><td>05/06/00</td><td>9:49</td><td></td><td>2.42</td><td>Low</td><td>Customer Care</td><td>AS400</td><td>AS400 COLONIAL PASSWORD ENABLE</td></tr><tr><td>MIA-000506-0007</td><td>05/06/00</td><td>10:16</td><td></td><td>2.20</td><td>Low</td><td>Customer Care</td><td>AS400</td><td>AS400 COLONIAL PASSWORD ENABLE</td></tr><tr><td>MIA-000506-0008</td><td>05/06/00</td><td>10:23</td><td>5/8/00</td><td>15:38</td><td>Low</td><td>Technicians</td><td>HARDWARE</td><td>Printer jam \\mia-fps-03\mia-prn-ic-01 giving error printer jam after user as open an check unit hp iisi (13.1 internal jam)</td></tr></table>

<sup>a</sup> When resolved time is missing it is assumed to be under 5 min per interview with help desk agents.

## References

[1] M. Alavi, D. Leidner, Knowledge management systems: emerging views and practices from the field, Proceedings of the 32nd Hawaii Conference on System Sciences, Los Altimos, CA, IEEE Computer Society, Maui, HI, USA, 1999, pp. 239.

[2] M. Alavi, D. Leidner, Knowledge management systems: issues, challenges, and benefits, Communications of the Association for Information Systems 1 (7) 1 – 37.

[3] J. Anton, The past, present, and future of customer access

centers, International Journal of Service Industry Management 11 (2) (2000) 120– 130.

[4] J. Anton, D. Gusting, Call Center Benchmarking: How Good Is Good Enough, Purdue Univ. Press, Indiana, 2000.

[5] V. Bapat, E. Pruitte, Using simulation in call centers, Winter Simulation Conference Proceedings, IEEE, Washington, DC, 1998, pp. 1390–1395.

[6] I. Becerra-Fernandez, The role of artificial intelligence technologies in the implementation of people-finder knowledge management systems, Knowledge-Based Systems 13 (2000) 315 – 320.

[7] C.W. Chan, L.L. Chen, L. Geng, Knowledge engineering for an intelligent case-based system for help desk operations, Expert Systems with Applications 18 (2000) 125– 132.

[8] K.H. Chang, P. Raman, W.H. Carlisle, J.H. Cross, A selfimproving helpdesk service system using case-based reasoning techniques, Computers in Industry 30 (2) (1996) 113– 125.

[9] V. Chin, S.C. Sprecher, Using a manufacturing based simulation package to model a customer service center, Winter Simulation Conference Proceedings, IEEE, New Orleans, LA, USA, 1990, pp. 904– 907.

[10] B. Cleveland, J. Mayben, Call Center Management on Fast Forward, Call Center Press, Maryland, 1997.

[11] K. Dawson, The Complete Guide to Starting, Running, and Improving Your Call Center, CMP Books, New York, 1999.

[12] R.A. Feinberg, I.S. Kim, L. Hokama, K. de Ruyter, C. Keen, Operational determinants of caller satisfaction in the call cen ter, International Journal of Service Industry Management 11 (2) (2000) 131 – 141.

[13] G. Fischer, J. Ostwald, Knowledge management: problems, promises, realities, and challenges, IEEE Intelligent Systems, (2001) 60– 72.

[14] M.H. Go¨ker, T. Roth-Berghofer, The development and utilization of the case-based help-desk support system homer, Engineering Applications of Artificial Intelligence 12 (1999) 665– 680.

[15] L.M. Gonza´lez, Analysis of applying knowledge management to an information technology help desk, Thesis, Industrial and Systems Engineering, FIU (2002).

[16] P.H. Gray, A problem-solving perspective on knowledge management processes, Decision Support Systems 31 2001, pp. 87–102.

[17] R. Heckman, A. Guskey, Sources of customer satisfaction and dissatisfaction with information technology help desks, Journal of Market Focused Management 3 (1998) 59– 89.

[18] G. Held, Network Management: Techniques, Tools, and Systems, Wiley, Chichester, UK, 1992.

[19] C.W. Holsapple, K.D. Joshi, Organizational knowledge resources, Decision Support Systems 31 (2001) 39 – 54.

[20] A. Lazarov, P. Shoval, A rule-based system for automatic assignment of technicians to service faults, Decision Support Systems 32 (2002) 343 – 360.

[21] D. Leake, Case-Based Reasoning: Experiences, Lessons, and Future Directions, AAAI Press, Menlo Park, CA, 1996.

[22] S. Lee, R.M.O. Keefe, The effect of knowledge representation schemes on maintainability of knowledge-based systems, IEEE Transactions on Knowledge Data Engineering 8 (1996) 173– 178.

[23] D. Leonard-Barton, Wellsprings of Knowledge, Harvard Business School Press, Boston, 1995.

[24] R. Marcella, I. Middleton, The role of the help desk in the strategic management of information systems, OCLC Systems and Services 12 (4) (1996) 4 – 19.

[25] R. McDermott, C. O’Dell, Overcoming cultural barriers to sharing knowledge, Journal of Knowledge Management 5 (1) (2001) 76 – 85.

[26] K. Mertins, P. Heisig, J. Vorbeck, Knowledge Management: Best Practices in Europe, Springer-Verlag, Berlin, 2001.

[27] P. Meso, R. Smith, A resource-based view of organizational knowledge management systems, Journal of Knowledge Management 4 (3) (2000) 224– 234.

[28] K. Miller, V. Bapat, Case study: simulation of the call center environment for comparing competing call routing technologies for business case Roi projection, Winter Simulation Conference Proceedings, IEEE, Washington DC, USA, 1999, pp. 1694– 1700.

[29] M. Nissen, M. Kamel, K. Sengupta, Integrated analysis and design of knowledge systems and processes, Information Resources Management Journal, 2000, pp. 24 – 43.

[30] I. Nonaka, A dynamic theory or organizational knowledge creation, Organization Science 5 (1) (1994) 14 – 37.

[31] I. Nonaka, H. Takeuchi, The Knowledge-Creating Company, Oxford Press, New York, 1995.

[32] S.E.A. Piggott, Internet commerce and knowledge management—the next megatrends, Business Information Review 14 (4) (1997) 169–172.

[33] B. Rubenstein-Montano, J. Liebowitz, J. Buchwalter, D. McCaw, B. Newman, K. Rebeck, A systems thinking framework for knowledge management, Decision Support Systems 31 (2001) 5 –16.

[34] S. Sandborn, Structuring the service desk, Information World 23 (52) (2001) 28.

[35] A. Satyadas, U. Harigopal, Knowledge management tutorial: an editorial overview, IEEE Transactions on Systems, Man, and Cybernetics—Part C: Applications and Reviews 31 (4) (2001) 429– 437.

[36] R.J. Sharer, Applying policy management to reduce support costs for remote and mobile computing, International Journal of Network Management 8 (1998) 211 – 218.

[37] E. Simoudis, Using case-based retrieval for customer technical support, IEEE Expert 7 (5).

[38] K.E. Sveiby, The New Organizational Wealth. Managing and Measuring Knowledge-Based Assets, Berrett Koehler Publisher, San Francisco, 1997.

[39] M.J. Taylor, D. Gresty, R. Askwith, Knowledge for network support, Information and Software Technology 43 (2001) 469–475.

[40] A.H. Thomas, The Virtual Help Desk, Thomson Computer Press, New York, 1996.

[41] R. Weber, D.W. Aha, I. Becerra-Fernandez, Intelligent lessons learned systems, Expert Systems with Applications 17 (2001) 17 – 34.

Luz Minerva Gonza´lez was born in Nicaragua where she completed her BS in Industrial Engineering. She earned an MS in Industrial Engineering at Florida International University in Miami, FL. While earning her degree, she worked at Royal Caribbean Cruise Lines. She is now in the Management of Information Systems Department at Americatel in Miami, FL.

![](/api/attachments/KXXEJ5SN/fulltext/images/743ed58f7859023e94ac82688ff78241cbb92a0a1120d02ed688accfae92a7c9.jpg)

Ronald E. Giachetti is Associate Professor of Industrial & Systems Engineering at Florida International University. He is also the director of the Masters Program, Information Systems Track. Dr. Giachetti conducts research in enterprise systems, systems integration, design methodologies, and application of operations research. He has managed research projects which total over \$1 million with funding from NSF, NASA Ames Research Center, US Army,

and industry. He has published over 25 refereed articles in journals, including International Journal of Production Research, International Journal of Production Economics, European Journal of Operations Research, and the Journal of Robotics and Computer Integrated Manufacturing. He received his Ph.D. in Industrial Engineering from North Carolina State University.

Guillermo Ramirez earned his MS in Engineering Management from Florida International University in Miami, FL. While earning his degree, he worked in the technical call center for Vodophone.
