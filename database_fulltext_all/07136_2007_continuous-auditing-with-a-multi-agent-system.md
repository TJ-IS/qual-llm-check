---
otero_id: 7136
otero_key: "SEAJ8DRU"
title: "Continuous auditing with a multi-agent system"
authors: "Charles Ling-yu Chou; Timon Du; Vincent S. Lai"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.08.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Continuous auditing with a multi-agent system

Charles Ling-yu Chou, Timon Du, Vincent S. Lai <sup>⁎</sup>

Faculty of Business Administration, The Chinese University of Hong Kong, Shatin, N.T. Hong Kong

Received 15 March 2005; received in revised form 15 April 2006; accepted 9 August 2006 Available online 4 October 2006

## Abstract

Information technology has dramatically changed the way businesses and business information are managed. In electronic business, much of the information is in electronic format, and the resulting change in the auditing environment has forced audit professionals to audit electronic evidence. Moreover, the emergence of real time accounting reports has put increasing pressure on audit professionals to provide real-time auditing services, or continuous auditing, in which the time between the occurrence of events and the provision of an auditor's opinion is minimized to an acceptable level. This paper proposes an agent-based system for continuous auditing called the agent-based continuous audit model (ABCAM). The system can be implemented independently of the client's information system, is able to undertake automatic auditing in real time, and can easily adapt to changes in auditing requirements and information systems. Five scenarios are developed to illustrate the model. © 2006 Elsevier B.V. All rights reserved.

Keywords: Financial auditing; Continuous auditing; Multi-agent system; Mobile agent

## 1. Introduction

As accounting information systems are popularly used to generate, compute, authenticate, store, and sort transactional data, it has become common for companies to employ electronic data processing (EDP) and other automation systems. Data that is generated in electronic format has had an enormous impact on audit professionals in two main ways [26]. The first relates to the change in the subject of audits, as more manual operations are being replaced by automatic processes and many internal controls can now be implemented by the information system itself. The second relates to the pressure that is being exerted on audit professionals to offer a fuller service, as companies, such as Wal-Mart, J. C. Penney, and Dollar General, begin to provide timely financial or non-financial reports to the public on a weekly basis [7].

Although some companies now publish corporate information almost in real time – Cisco Systems, for example, is able to close its books in hours [12] – decision makers often question the reliability and relevance of such material [7]. To alleviate such concerns, audit results now need to be released alongside such corporate information, or should at least not lag significantly behind. As a result of this new demand, audit professionals are being forced to adopt new strategies to implement auditing practices in a continuous time frame [7,26]. With this new arrangement, audit professionals take a proactive role to assure the quality of the data, which means that instead of initiating a backward inspection by testing the accuracy of the reported figures, auditors carry out continuous auditing.

In this study, we propose a continuous auditing model – the agent-based continuous audit model (ABCAM) – that uses a multi-agent system. The system uses mobile agents to help human auditors to perform auditing work that is tedious, trivial, or complicated. The system allows continuous auditing without having to interface with the client's enterprise system, particularly in the design phase, and permits human auditors to audit many clients concurrently while accessing data from different applications or different collaborative relationships, such as supply chain partnerships.

In the following sections, we first present a review of computer-based auditing. Section 3 introduces the new system. The demonstration and discussions are presented in Sections 4 and 5, respectively.

## 2. Computer-based auditing

Auditing is a process that estimates the degree to which the assertions of a corporation correspond with certain established criteria, such as specific corporate rules, policies and constraints, or generally accepted accounting principles (GAAP) that are established by the Financial Accounting Standards Board (FASB) and other authoritative bodies.

The auditing process is organized and executed under the constraints of labor and cost. As it is not realistic for auditors to monitor every single business transaction to assure the relevance and correctness of business information, they rely on supporting evidence, which is known as audit evidence, to test the trustworthiness of the information.

Generally speaking, audit evidence can be classified into seven broad categories [3,7]: the physical examination of the assets that are represented in the accounts; confirmation by authenticated documents that are prepared either outside or inside the organization (a typical example is to request the confirmation of an annual purchase from a selected customer); documentation, in which auditors test the interrelationships between the data in various documents; observation; inquiries, which include the formal and informal statements of the management and employees of the organization or unit; re-performance of the calculation or the flow of the process; and analytical procedures.

In the last two decades, research on accounting and auditing has explored diverse ways of achieving effective and efficient gains through the adoption of information technology [1]. The ideas that have been proposed are generally classified into two major approaches. The first approach aims to develop useful computer-assisted auditing tools as decision aids for the process of audit planning and the evaluation of the internal controls in an operational system. The second approach seeks a convincing methodology for the implementation of the concept of continuous auditing.

## 2.1. Computer-assisted auditing tools

Since the 1980s, researchers and major accounting firms have developed various computerized audit aids. In addition to the simple automation of selected audit processes, decision support systems (DSS) and knowledgebased expert systems (KES) are two of the more general approaches [1]. The automation of auditing processes simply provides reliable and high-speed functions that take over part of the job of the auditors, in particular tasks that are normally routine and are prone to error if auditors lose concentration. Typical tasks of this type are footing, recalculation, and crosschecking between accounts [21]. In practice, the automation of auditing processes is packaged as generalized auditing software, which is provided by software vendors and delivers comprehensive and user-friendly services for auditing.

Decision support systems (DSS) assist in making semi-structured or unstructured decisions by providing analytical models, transparent connection tools to databases, and user-friendly presentation interfaces [2]. Some typical uses of DSS for auditing process are the decision statistical sampling method and analytical review procedures.

Knowledge-based expert systems (KES) emulate the reasoning process of audit professionals to solve problems that require judgmental decision making [2]. Auditing knowledge, which generally takes the format of if-then rules, is elicited from experienced audit professionals and is stored in a knowledge base. Auditors then collect facts about the problem that they want to solve and use inference engines to come to a conclusion about the problem. Such conclusions are deduced by the engines through the analysis of the relationship between facts and rules. Tasks such as risk analysis, internal control evaluation, audit program planning, and technical advice are problems that are suitable for solving with KES [5,30].

## 2.2. Continuous auditing models

Research on continuous auditing models has blossomed in the last two decades [8,15,18,29]. Most of the approaches monitor or analyze transaction data by establishing a set of rules that are pre-defined for a specific auditing purpose. Once any violations of the predefined rules are altered within a transaction lifecycle or immediately after the completion of a transaction, alarms or “red flags” can then be raised to attract the auditor's attention [6]. Based on the collected evidence, auditors can both enhance weak internal controls and suggest improvements. Generally speaking, continuous auditing can be classified into two approaches: embedded audit modules and audit data marts.

## 2.2.1. Embedded audit modules (EAM)

Embedded audit modules (EAM) attempt to supervise all of the audit-related data that resides in operational databases. Small modules (codes) are built into the information system in the design phase as subroutine functions of the system [6]. The modules are triggered by events, and initiate various kinds of actions on the audit-related information [28]. These actions include utilization of simple tools to capture information and generate reports on the violation of constraints [8,15] and that of more sophisticated tools to simulate processing functions [18].

However, the feasibility of implementing EAM is a problem, because EAM require auditors to engage intensively with the system developers in the design phase of a system. In practice, the contractual relationship between a corporation and an auditing firm is normally reviewed on an annual or quarterly basis, and the information system itself normally exists before the auditing firm is invited to provide its services, which means that auditors are rarely involved in system design. Moreover, an intensive collaboration between audit professionals and system developers to build an embedded auditing module would contradict the expected independence and impartiality of auditing practice [24].

## 2.2.2. Audit data marts (ADM)

Audit data marts are small data warehouses into which audit-related information is extracted for further inspection [26]. The idea is to obtain the required information from the data mart to minimize interference to the operational system. As the audit data is automatically and periodically downloaded from the client's database, the auditing is claimed to be continuous. Unfortunately, little evidence can be evaluated using this approach, and only procedures that use historical data such as documentary evidence can be carried out [7]. Moreover, auditors have the extra burden of managing the audit data mart for each client. The large volume of data that has to be transported from the client's system to the data mart is another obstacle to the adoption of this approach.

## 3. An agent-based continuous audit model (ABCAM)

This study proposes a continuous auditing model – the ABCAM – that uses multiple mobile software agents to support auditing processes. A software agent is a software object that achieves a goal by performing actions and reacting to events with prearranged activities in a dynamic environment [10,14]. Typically, a software agent is programmed to have mobility and intelligence. Mobility implies that the agent is able to travel from one platform to another, and intelligence refers to the deployment of different degrees of artificial intelligence. An intelligent mobile agent should therefore be able to provide sophisticated computation or behavioral models for working on remote data resources. Intelligent mobile agents are generally applied to (and benefit) applications such as electronic commerce, secure brokering, distributed information retrieval, parallel processing, monitoring and notification, telecommunication networks services, and workflow applications and groupware [19,32]. Some examples of these applications include the supply chain SMART project (http://smart.npo.org), brokering services in electronic markets [10], virtual enterprises [17], information retrieval and internet-auction houses [27], and distributed network management [9].

The basic concept that underlies the ABCAM is that the activities that are traditionally undertaken by human auditors in the audit procedures to collect competent audit evidence can ultimately be executed by various kinds of software agents. With the ABCAM, each mobile agent represents a specific audit procedure and acts on behalf of a human auditor to access and inspect the audit-related information that resides in distributed information sources. As a whole, the numerous agents behave aggregately as an audit agency system.

The implementation of ABCAM is based on two important assumptions. First, the system is supposed to be implemented in the corporations with a high level of automation in their business operations. In such organizations, business information is stored and maintained in electronic format, and the business policies and internal controls are fully reflected by the process definitions that are maintained in the enterprise information system. The second assumption is that the audit evidence that is collected by software agents is able to provide competent support to the auditor to edit audit opinions. We assert that, at this stage, five out of the seven types of audit evidence can be directly collected by intelligent mobile agents. These include asset examination, documentation, confirmation, re-performance, and analytical procedures. The remaining two types of evidence – inquiry and observation – that cannot be handled by such agents are generally considered to be less relevant to the generation of a reliable audit opinion [23]. However, as the intelligence of the mobile agents improves as the artificial intelligence technology advances, future agents may eventually be able to simulate the collection of these two types of audit evidence.

## 3.1. Ways of handling audit evidence with ABCAM

## 3.1.1. Documentation, re-performance, and analytical procedures

In the ABCAM, different mobile agents handle the collection of these three types of audit evidence in the same way. The agents all compare accounting data (such as data in ledgers and journals) with supporting data sources to validate the integrity of the information in the financial reports. For example, documentation compares accounting data with informative documents (such as checks, invoices, and POs); analytical procedures compare accounting data with a referenced industrial benchmark index; and re-performance compares accounting data with the re-performance results of the corresponding operations. Thus, any document that has errors or is potentially fraudulent can be located. During implementation, a mobile agent may access many distributed information resources to collect the information that is needed to invoke certain analytic procedures associated with the agent behaviors, or may stay in the Enterprise Resource Planning (ERP) system and complete its analysis of the documents that are hosted by the ERP.

## 3.1.2. Confirmation

The mobile agent retrieves the audit information and confirms its veracity with external entities (e.g., customers, vendors, or banks). In this design, the agent is programmed to communicate with the automatic online services provided by the parties being inspected. To facilitate message exchanges for the confirmation of financial statement, the engaged agents and computing services should adopt a common communicating protocol (such as the Agent Communication Language or Simple Agent Communication Protocol) and vocabulary for supporting the semantics of the financial data.

## 3.1.3. Asset examination

The mobile agents are commissioned to validate the actual existence of the assets that have been recorded in the accounting information system. In doing so, the commissioned agents retrieve relevant information on business operations in real time and carry this information to other applications for further confirmation. For effective communication between the mobile agents and the participating applications, they need to agree on common agent communication language and common vocabulary. An example of this audit evidence is the examination of actual stock availability through the communication with the inventory management system for real time inventory maintenance.

## 3.2. The agent platform in ABCAM

In this study, we adapted a platform from IBM's Tokyo laboratory (www.trl.ibm.com/aglets/) to develop our audit agency system. The referenced platform has a set of abstract classes and application programming interfaces (API) with which users can build their own multiple agent platform. Of these abstract classes, Aglet, AgletProxy, and AgletContext are the three main components that drive agent activities such as creation, cloning, dispatch, messaging, and disposal.

An Aglet is an abstract Java object that implements all of the basic agent activities. A system developer can model its own mobile agent behavior by extending the class definitions.

An AgletProxy is an Aglet representative. In implementation, intra-Aglet messaging and communication between the Aglets and the environment go through the interface of an AgletProxy, rather than through the Aglets directly. This design serves two purposes: it acts as a shield to protect the Aglets from malicious access and provides location transparency.

A context is the workplace of the Aglets. Every active Aglet must be hosted by an AgletContext, which serves as a stationary object that provides a means of maintaining and managing the running Aglets. The functions of the AgletContext can be used by the Aglets to obtain information about other active Aglets and the environment. Basically, one computer can run many Aglet servers (engines), one server can host many AgletContexts, and one AgletContext can host many Aglets.

Based on the functions of the Aglets, AgletProxy, and AgletContext, the architecture of the ABCAM Agency Services Server was developed and implemented. The functions of the Agency Services Server, which are shown in Fig. 1, involve three modules: the Interface Module, the procedures module, and the agent invocation and execution module. This server interprets commands from auditors and mobilizes the necessary mobile agents to complete assignments.

The Interface Module, which manages the interface between the Agency Services Server and the human auditors, is in charge of two functions: the capture of information for the identification of specific audit procedures from the audit requesters and the presentation of the results of the audit procedures to the audit requesters.

The Procedures Module is responsible for mapping the audit requests that are identified by the Interface

![](/api/attachments/SEAJ8DRU/fulltext/images/34265f54d08095c093d11c2c32bf240f96e208995129d5ea60e92a2c825ec148.jpg)  
Fig. 1. Audit agency system.

Module into a detailed plan of activities for collecting the audit evidence. In this plan, much information is required, such as the evidence that needs to be collected, the mobile agent that needs to be dispatched, and the configuration of the mobile agents. The information that is specified in the configuration of the mobile agent includes the itinerary for the agent, the information sources that the mobile agent will access, and the computation procedure for the specified assignment. The Procedures Module is supported by an audit procedures database that generates a suitable activity plan. This database must be maintained by an auditing firm and adapted to suit changes in auditing requirements and different client operational systems.

The Agent Invocation and Execution Module is responsible for initiating the activities of the mobile agents and administrating their performance of the required assignments. The agents are initiated by a Java class code that is compiled by an Aglet. Various kinds of abstract audit classes are pooled in the agent pools, and are accessed by a Universal Resource Identifier from the Internet. The pooling of the Aglet classes can be maintained in three ways: through a local file directory, an Aglets server, or an http server. However, the configuration of the agents is formatted as a file that is accessed by the agents as an input. When the mobile agent completes its assignment outside the Agency Services Server, it comes back to the

Server and transfers the assignment result to the Interface Module. The Interface Module then consolidates and formats the audit results for return to the audit requester.

## 4. Demonstrations and implementation

## 4.1. System development

For demonstration purposes, we developed an audit agency system, a database system to support the data management, and several datasets for the simulation of auditing operations. The audit agency system is an agent platform that serves the Agent Service System and the collaborating mobile agents. The Aglets Software Development Kit v.2.0.2 (ASDK) is utilized to build the platform, and the mobile agent is developed in Java (J2SE, v. 1.4.2).

An open-source database server, MySQL, is used to build the database management system. Typically, SQL queries are sent to the MySQL server by a text-based MySQL client program, a composite GUI MySQL control center, or a Java program through the JDBC driver (MySQL Connector/J). The JDBC technology is an API (which is provided with the J2SE v. 1.4.2 installation pack) that provides connectivity to a wide range of SQL databases. By interfacing with database-specific drivers, a Java program can establish a connection to the database, access data, send SQL statements, and process the results that are returned from the SQL query. Using JDBC technology, programmers can give mobile agents the ability to autonomously access and process data in any SQL-based database.

To simulate the audit procedures, several datasets are prepared and stored in various formats. For demonstration purposes, a database is built and hosted by the MySQL server. The database is loaded with a set of test data, which is extracted from a sample workbook from the 30-day evaluation version of ActiveData for Excel (commercial software for auditing and fraud detection from Information Active Inc., www.informationactive. com). The test data is contained in four tables, and represents 5000 invoices, 1000 customer records, 77 product status records in the inventory, and 27 basic records from sales people. As this test data was prepared to demonstrate the data analysis ability of ActiveData for Excel, which is only one part of the auditing capability of our proposed system, we need to revise the original test data to fit the purposes of our study. The revision includes changes to the invoice table and the addition of a supplemental accounts receivable table. The revised tables and their relationships are shown in Fig. 2.

In addition to the preparation of the test data, we also generate two more individual business documents according to the scenario requirements for demonstration purposes. The first document is a workflow process definition that is formatted in XML Processing Description Language (XPDL). XPDL is a specification for process definition language that was proposed by the Workflow Management Coalition (WfMC). The specification provides a common meta-model to describe the process definition and XML schema that specifies the definition that is defined in XPDL. Business processes that are defined in XPDL are guaranteed to be able to be imported and implemented by workflow management systems or enterprise information systems that support the XPDL specification (www.wfmc.org). In our demonstration, the sample workflow that is provided by the WfMC (www.wfmc.org/standards/docs. htm) is adopted and modified for our demonstration scenario. A selected part of the sample workflow definition is shown in Fig. 3.

![](/api/attachments/SEAJ8DRU/fulltext/images/1c989b368f7957e09a25520f17cf782e618b3f4d3c62be537f492a2d7b46c818.jpg)  
Fig. 2. Table relationships diagram of the test data.

The second document is a business policy that specifies the rules for invoicing authorization. In this document, we establish a three level management hierarchy in the sales department, and then specify the information that is required for the approval authority of each management level. The business policy is formatted in XML and can be read by the software agents, which are the criteria for the validation of the conformance level of the audit evidence. Fig. 4 shows the authorization rules in detail.

## 4.2. Development of the agent server

As we have mentioned in previous sections, the Agency Services Server is composed of three modules: the Interface Module, Procedures Module, and Agent Invocation and Execution Module. Any available thirdgeneration or fourth-generation programming language, such as Java or C++, can be used to program the functions of the first two modules. However, the Agent Invocation and Execution Module is an agent server that initiates and administrates the mobile agents, and thus at least one AgletContext must be created to host the agents. Moreover, every resource that plans to interact with the mobile agents locally must also have a mobile agent server installed. The individual agent servers are identified with the universal resource identifier (URI), and at least one local agent will be activated to accept

![](/api/attachments/SEAJ8DRU/fulltext/images/1560188a65df2e97fdc56a8c52cf3bbf8295b2e8e6a0b81d2951a9e7c48deb20.jpg)  
Fig. 3. Selected portion of the XPDL workflow definition.

![](/api/attachments/SEAJ8DRU/fulltext/images/732abd791d0ceea225846dd9a9e2b5a218d90f87bea22fa3ec61fbe884bd46b8.jpg)  
Fig. 4. An authorization hierarchical chart in XML format.

message exchange requests from the incoming mobile agents. The Aglets Software Development Kit provides a simple Aglets server – Tahiti – for preliminary use, and programmers can use this server to review, monitor, and supervise the Aglets.

## 4.3. Implementing the audit procedures

To demonstrate the operation of the ABCAM, a scenario, as depicted in Fig. 5, is proposed for illustration in which an audit firm is engaged in the continuous financial auditing of a client. In doing so, the ABCAM system will dispatch mobile agents to access the client's ERP and inventory management system for an audit trail of the transactional data. In addition, the audit firm also needs to consult a third party to validate the integrity of the record saved in the client's ERP system.

To illustrate the actions of the mobile agents in the collection of five types of audit evidence, the following five scenarios are proposed. For a better understanding of the agent behavior and their collaboration pattern, information on state chart and flow chart diagrams is provided in the Appendix.

4.3.1. Demonstration of documentation — assuring the continuance of the business process definition

Generally, the relationships between the documents in the auditing process are revealed in the workflow definition of all business processes. Traditionally, auditors utilize expert systems to help them investigate the workflow definition to identify any control weaknesses by examining the design of the operation processes. In the continuous auditing model, the mobile agents help to assure that the workflow definitions that are validated by the auditors are identical to those that are actually running the accounting information system.

In this scenario, auditors extract the workflow definition from the workflow management system before the commencement of the audit practice and compare it with the workflow that is acknowledged to be the authorized process. Any discrepancy that is found is identified as an unexpected change. Unexpected changes may be caused by authorized or unauthorized operations, both of which can have a significant impact on the relevancy of the audit result. Therefore, it is an important inspection task to assure the effectiveness of the audit plan at every point in the implementation of continuous auditing.

![](/api/attachments/SEAJ8DRU/fulltext/images/527835e5ddeaf783bcac2fc61d6828fc22ae934d3fb629f4f0a4c25eea380a1b.jpg)  
Fig. 5. Demonstration scenarios for the collection of five types of audit evidence.

To deal with such scenario, our system programs a mobile agent (Agent 1 as depicted in Fig. 5) to perform the following activities.

(a) Agent 1 is initiated by the Agency Services Server, and is then dispatched to agent server 2.

(b) On arrival at agent server 2, the mobile agent encounters a local agent and asks the local agent for the definition of the process workflow.

(c) After getting a response from the local agent, the mobile agent takes the definition and moves to agent server 3 to undertake further activities.

(d) Based on the assignment, the mobile agent acquires the authorized process workflow from the workflow management system (which is simulated by agent server 4) and compares it with the definition that was retrieved from agent server 2.

(e) Finally, the agent brings any discrepancies back to the Agency Services Server. The inspection results will then be transferred to, and ultimately consolidated by, the Interface Module.

## 4.3.2. Demonstration of re-performance — assuring the effectiveness of the implementation of business rules

In practice, corporations define various business rules and then code them into their business information systems. Business rules are the definitions, directions, or constraints that guide business behavior in actual operations [4]. Although these rules should be adaptable, they must be enforced immediately in the business information system. To assure the effectiveness of the defined business rules, auditors will inspect the transaction documents of the corresponding records to determine whether a transaction has been processed according to the constraints of the business rules. The itinerary for the mobile agent for this purpose is specified as follows.

(a) A mobile agent (Agent 2 in Fig. 5) is initiated by the Agency Services Server and is sent to the client site, which is simulated by agent server 3 to acquire the business rule that covers authorization policy, which is formatted in XML.

(b) After fetching the rule, the mobile agent moves to the client's ERP system in agent server 4 and interacts with the server's local agent, which subsequently queries its database for the results that have been requested by the mobile agent. In this scenario, SQL queries are used to identify any exceptional records that contradict the business rules for the authorization policy. An example of an SQL query to identify exceptional approval for amounts that are larger than 10,000 in the invoice tables (which contravenes the authorization policy) is as follows.

Select InvoiceNo, Amount

From Invoices

Where Amount N10,000

AND Authorizer bN1.

## 4.3.3. Demonstration of analytical procedures

Auditors normally use analytical procedures to identify the suspected error-prone and fraudulent pieces of business information. In this scenario, we demonstrate the inspection of the consistency of invoices and accounts receivable records. As the existence of any records in accounts receivable depends solely on the existence of invoices, every record in the accounts receivable must be supported by an invoice. Moreover, as one invoice can only generate one accounts receivable record, the auditor must prevent the same invoice from being generated multiple times or from non-existent invoices. The following itinerary for a mobile agent carries out this procedure.

(a) A mobile agent (Agent 3) is initiated and sent to the client's ERP at agent server 4.

(b) The mobile agent queries the server's local agent, using SQL, for the necessary information. For illustration purpose, two examples of SQL queries are listed below. The first SQL query is implemented to identify any occurrence of duplicate accounts receivables that have been generated from the same vendor invoices: Select Invoices.InvoiceNo, count(Invoices.InvoiceNo) as existence From Invoices, Account\_Receivables Where Invoices.InvoiceNo = Account\_Receivables.InvoiceNo AND existence N1 Group by InvoiceNo. The second SQL query is for identifying accounts receivables with inexistent invoices: Select AccountReceivables.AccountReceivableNo, AccountReceivables.InvoiceNo, Invoices.InvoiceNo From AccountReceivables Left JOIN Invoices On AccountReceivables.InvoiceNo = Invoices. InvoiceNo Where Invoices.InvoiceNo is NULL.

## 4.3.4. Demonstration of confirmation — confirming the information with a third party

As business documents must be authenticated and confirmed, an auditor sometimes needs to confirm specific information with a third party for validation purposes. For example, to audit the delivery of a product, the auditor needs to confirm with the customer that the consolidated amount in the delivery or billing statement is correct. In an electronic business context, these tasks can be implemented by the interaction of collaborating software agents, and the confirmation process can be carried out frequently at the individual transaction level to achieve continuous auditing. The following is an example of the implementation of such a procedure.

(a) A mobile agent (Agent 4) is initiated by the Agency Services Server and is dispatched to the customer's ERP, where a local agent server 4 is installed.

(b) The local agent responds to the data request of the mobile agent, and then accesses all delivery transactions in the ERP for the queried records.

(c) The mobile agent transports the records to agent server 5 at the customer's site for confirmation.

(d) The local agent in agent server 5 accepts the tabular records, compares them with its own records, and delivers any discrepant records to the mobile agent. The mobile agent then goes back to the Agency Services Server to report the audit result.

4.3.5. Demonstration of asset examination — physical inspection

The last scenario simulates the activity of examining fixed assets in a warehouse. Traditionally, auditors need to go to the company's warehouse and physically count the stock to confirm the accuracy of the inventory that is recorded in the accounting information system. In modern warehouse management, advanced technologies, such as RFID, can be adopted to improve the efficiency of inventory checking procedures. With the use of these technologies, auditors can confirm the physical inventory with the inventory management system to assure the correctness of the asset value of the warehouse in real time. The implementation of the audit procedure to deal with asset examination, which is shown in Fig. 5, is as follows.

(a) A mobile agent (Agent 5) is initiated to acquire information on stock availability from the ERP system at agent server 4.

(b) To attest the reliability of the inventory information in the client's ERP system, stock availability information is also acquired from the inventory management system at agent server 6 for comparison and validation.

(c) The mobile agent will compare the information that is maintained in the client's ERP system with the information in the inventory management system for any discrepancies.

(d) Consequently, the mobile agent responds with any discrepancies in the asset account to the Agency Services Server through the Interface Module.

## 5. Benefits and Drawbacks of ABCAM

## 5.1. Benefits

In addition to the general benefits that can be obtained with an intelligent agent-based system [19], the ABCAM can overcome problems that are associated with the implementation of an EAM or an audit data mart, and assures that audit procedures to be implemented in a continuous way. The basic features and benefits provided by the ABCAM are elaborated as follows.

Continuous inspection. The mobile agents act as inspectors of audit-related information, rather than being embedded as sub-routines in an information system.

Therefore, the mobile agents can be scheduled to execute pre-defined audit procedures periodically or randomly. Through a periodic inspection of audit-related information, the audit agency system provides timely information, such as daily or weekly reports, to human auditors, on a more frequent basis.

Independence. Another feature of the ABCAM is that its development is independent of the development of the information system of the client. As the mobile agent is not an embedded program in the information system, audit professionals can develop an audit agent system without having to intensively involve the client's legacy system, particularly in the design stage. Thus, only an authorized secure interface with read-only access to the audit-related information is needed.

Flexibility. The software agent is flexible and can access various kinds of information, and the audit agent system can adapt easily to changes in the audit environment. In the ABCAM, a mobile agent is dispatched to interact with local agents to acquire information. The local agent is a program that is programmed, generated, and housed in the local system to assist the mobile agent, which allows the mobile agent to work independently of the local system while the local agent adapts to any environmental changes, such as changes in the audit criteria, operation system, and information system.

Intelligence. The mobile agent is able to employ a certain degree of intelligence and automation when implementing audit procedures. For example, the inspection of a mobile agent is not limited to the historical records in an accounting information system. Rather, the agent can compare consistency in various ways, such as carrying information to a third party system for confirmation and consulting inventory databases for the most updated stock level.

## 5.2. Drawbacks

Although ABCAM offers unique benefits for continuous auditing, the system has some limitations in its application. Of all these limitations, the following two are of particular concern.

Concerns in System Performance. In ABCAM, mobile agents need to have frequent interactions with internal and external applications and systems for audit evidence, which subsequently will adversely impact the overall performance of the system. In our auditing demonstration as depicted in Fig. 5, the implementation of audit procedures by mobile agents consumes significant computing resources, which include the server hosting the agent interactions and the database administrator replying queries for data access. These resource requirements could significantly scale up when multiple audit agents are triggered for actions simultaneously [27,31]. Consequently, the costs associated with the computer upgrades may become a prohibiting factor for the adoption and implementation of ABCAM.

Concerns in security and system integrity. The adoption of ABCAM system to support continuous auditing implies that all information systems in the client's site would become accessible to the audit agents. This access of agents, if unrestricted, will violate the doctrine of Information Technology (IT) systems in safeguarding the enterprise information against malicious, unauthorized access, including both internally and externally. Hence, ABCAM will have appropriate security mechanism established for granting the auditing agents with required access rights and privileges. Furthermore, with the promulgation of the Sarbanes-Oxley Act in 2002, it becomes crucial for auditors to assure the integrity of internal financial controls in enterprise to gain public confidence on the audit results. Though IT professionals and users are still confused of the roles of IT in Sarbanes-Oxley Act [16], it is of utmost importance to explore different alternatives IT could comply to the Act.

Our ABCAM could base the security design on IBM's Tokyo laboratory platform. Unfortunately, the platform's security policy only has mechanisms to differentiate data access by external or local mobile agents. In other words, the platform has a limitation in specifying and enforcing the roles of mobile agents and their access privileges. In our future study, we plan to design digital certificates into ABCAM to identify external audit agents and assign their corresponding access rights. This security measure may have technical difficulties in its implementation. However, our initial exploration suggested that it is feasible for consideration.

## 6. Conclusion and future work

This study proposes an ABCAM that adopts mobile agent technology to undertake the continuous execution of audit procedures. The model is designed to provide a method for the implementation of continuous auditing that overcomes the problems of implementing both an embedded audit module and an audit data mart in an audit-related database. The ABCAM gives auditors the independence to develop and install an audit agency system while the client's system is running, and even while it is being upgraded. A demonstration is provided to show the interaction patterns among mobile agents while they are commissioned to collect five types of audit evidence.

This paper is a fundamental exploration of the application of mobile agent technology in a continuous auditing model. Several other studies could be pursued as an extension to this study, such as a study on setting a high degree of agent intelligence for the execution of audit procedures. Here, we present only simple behavior, such as synchronous communication between the local agents and the database to retrieve the data that is required for operations. The addition of a higher degree of intelligence for mobile agents could explore more sophisticated evidence-collecting activities [20]. For example, an agent with reasoning ability could be used to identify a potential control weakness in the process definition, and an agent with the ability to acquire the semantics of documentation and business policies could automatically generate audit procedures for specific audit objectives [25]. An agent that could learn from previous experience would have the ability to adjust to a better sampling method and sampling rate to execute audit procedures. Moreover, an agent with built-in intelligence would be able to decide the best time to execute audit activities.

A study on the building of an infrastructure for collaboration between agent systems would also be of merit. To facilitate automatic collaboration between agents, several functions could be provided, such as directory services, automatic matching services, ontological development, and consolidation and conciliation [31]. Other functions that are normally transparent to agent operations, such as security controls and persistent preservation management, might also be important.

This paper does not provide an evaluation of the actual implementation of the proposed system using real or simulated corporate data. It is understood that such evaluation could contribute to the understanding of the audit effectiveness, efficiency and consistency [13,22] of AB CAM. However, the foci of our current investigation are to explore the technical feasibility of continuous auditing and to demonstrate possible applications of continuous auditing. However, in our future study, we plan to emphasize the evaluation and benchmarking of ABCAM performance, which can be achieved by using either surveys or experiments.

Future research could also look at the security mechanisms of automatic audit practices. Although auditors need to be allowed to read corporate data, an advanced access control mechanism for auditors is necessary when they are auditing companies that collaborate closely with other partners in electronic business [11], because auditors are able to access information that is shared by various combinations of partners, most of which is confidential.

A study of audit risk models, eternal sampling methods, and sampling rates could also prove useful. Current audit risk models have been developed for auditing practices that are implemented over a long period (say, quarterly), and only limited resources can be used to audit large amounts of business transactions. However, the emergence of continuous auditing requires a new approach in deciding the frequency and scale of auditing.

## Appendix A. Appendix

For a better understanding of the agent behaviors and their collaboration patterns, two different diagrams – state chart and flow chart – are elaborated here. In the state chart diagram, events and state changes of each agent are provided to illustrate the reaction patterns of each participating agent in action. In the flow chart diagram, control information of the execution of an audit procedure is depicted to illustrate the control flow among agents. This diagram provides a better understanding of the choreography patterns among collaborating agents in an audit procedure.

## A.1. State chart diagram

When an audit event is triggered, multiple audit agents will be activated. For illustration purpose, we have selected three general types of agents – the Audit Procedure Execution (APE) Agent, Local Registration (LR) Agent, and the Local Service (LS) Agent – to demonstrate their state changes in the State Charts. These agents collaborate to accomplish specific inspection tasks, as part of an audit procedure, that have been

![](/api/attachments/SEAJ8DRU/fulltext/images/1b4842ebb74e96e96551b02217adc92f92e780b6ae5f973def05a8d04a32c18a.jpg)  
Fig. A1. State chart diagram: audit procedure execution agent.

![](/api/attachments/SEAJ8DRU/fulltext/images/0118079d311daafda901f709e880938043648bf6b72c7add433a58650e49dd88.jpg)  
Fig. A2. State chart diagram: local registration agent.

committed for execution in a local virtual hosting machine (the AgletContext).

The APE agent is an instance of a set of agent classes, with each agent class specializing in one distinct audit procedure. In other words, different APE agents are commissioned to serve for different audit objectives in different audit procedures. However, these APE agents have fundamental patterns in mobility and interaction that can be generalized in Fig. A1. As for a LR Agent, it provides registration and status maintenance services for all active and inactive LS agents in the hosting machines. An inactive LS agent suggests that the agent is temporarily removed from the working space and stored in a secondary storage. When the inactive agent is triggered for action, the LR agent is responsible for activating the agent from the storage. The state changes of a LR agent in serving the aforementioned roles can be generalized as in Fig. A2. Similarly, the behavior patterns common to all LS agents are depicted in Fig. A3. The registration information of all available LS agents in a hosting machine is maintained in a registration table. If any of these services is triggered, the LR agent is responsible for the activation of the corresponding LS agent. Subsequently, the LS agent becomes ready to interact with visiting agents. Upon the completion of interaction and task, the LS agent will doze off and turn into inactive mode to conserve the computing resources.

In this appendix, we shall only elaborate the APE agents in Fig. A1 in greater depth. In general, the life cycle of APE agents can be classified into three different stages — OnCreation Operation, Inspection Operation, and After Inspection Operation. In the first stage, an APE agent is created by the agent administration center (it is a special LR agent dwelling in the main auditing agency system maintained by the auditing firm). During the creation process, the specification for the inspection procedure, including the itinerary for the agents and the data set to be inquired, will be inputed from the Interface Module.

![](/api/attachments/SEAJ8DRU/fulltext/images/d3a7bfbd5d0cf43a7c05b46a7e357c1e1ec86d2ca734a62b3fb16237e9f512d7.jpg)  
Fig. A3. State chart diagram: local service agent.

In the Inspection Operation stage, the APE agent navigates among various virtual hosting machines (AgeletContext) and interacts with the local service agents. Before being dispatched, the APE agent first queries the machine to be visited for its status and availability. If the machine is inactive or unready, the APE agent will then be put in a short idle state or deactivated to a sleep mode. When the APE agent has successfully been dispatched to the visited machine, it will report its status to the monitoring manager of the home hosting machine — the agent administration center. At the same time, the APE agent will also request the activation of the required local service agent and interact with them for tasks completion. The same processes are repeated for each remaining hosting machines until all the site addresses listed in the itinerary have been visited.

The After Inspection Operation stage begins when the APE agent completes all its tasks as specified in the itinerary and returns to the agent administration center. If no exceptional event is raised in the inspection operation stage, the after inspection operation stage would consolidate all analyzed data into reports for submission to the Interface Module. Otherwise, the exception event will be reported instead.

## A.2. Flow chart diagram

In the following sections, several flow chart diagrams are presented to illustrate the control flow among participators, including auditors, Interface Module, and software agents. In general, an audit procedure, either implemented in a traditional way by an auditor or with the assistance of a computer technology, would require consultation to multiple resources, documentation, or even individuals and corporations. The completion of an audit inspection hence requires multiple agents and their collaboration. In designing an agency system, a single process executed by an auditor may have to be split into several atomic operations so that these operations could be coded into various agents for better reusability, management, and maintenance.

![](/api/attachments/SEAJ8DRU/fulltext/images/10d4d19c51d10bc0112a4116bd81051b24f4c399b0740566af4b7f13452c1853.jpg)  
Fig. A4. Flow chart for agents collaboration in high level.

Basically the flow chart diagrams is illustrated in an audit scenario, which auditors are going to assure the effectiveness of the implementation of certain business rules. This audit process involves multiple agent collaboration which can be organized in three levels. Fig. A4 portrays the highest level of collaboration among auditors, Interface Module, audit procedure execution agent, and local service agents. The second level of collaboration is depicted in Fig. A5. At the lowest level, Fig. A6 is used to illustrate individual requested services in various contexts, whereas Fig. A6 is used to demonstrate the post-inspection operation done in the administration center. The same figures can also be generalized to most of the other audit procedures.

Fig. A6 together demonstrate the scenarios of business rules inspection in the context of the ERP and the administration center. Initially, the audit agent

![](/api/attachments/SEAJ8DRU/fulltext/images/20d702795d3b7c11cb2649532ea7b1341538644adde34aea385ef888c9f3c1e5.jpg)  
Fig. A5. Flow chart for general inspection operation.

![](/api/attachments/SEAJ8DRU/fulltext/images/4219d3e936cf9e18c1b53608bd97c7a86669f0a1a5632166f750e7004c167dcd.jpg)  
Fig. A6. Differentiated flow chart for scenario — business rules inspection.

needs to query the local agent at the ERP system for relevant workflow definition, in which the business rules and constraints of business transactions would be extracted. With the retrieval of this workflow definition, the APE agent goes back to the administration center context to consult a special function support agent and generate the required queries on specific data schema to identify frauds or errors in transactions or events. The queries will be used by the APE agent to retrieve information relevant to audit inspection in the ERP context. After all these queries have been executed, the APE agent returns to the Administration Center context to finalize its inspection analysis. An inspection report will subsequently be forwarded to the Interface Module.

## References

[1] M. Abdolmohammadi, C. Usoff, A longitudinal study of applicable decision aids for detailed tasks in a financial audit, International Journal of Intelligent Systems in Accounting, Finance & Management 10 (3) (2001) 139–154.

[2] T. Amer, J. Andrew, D. Bailey, P. De, A review of the computer information systems research related to accounting and auditing, Journal of Information Systems 2 (1) (1987) 3–28.

[3] A.A. Arens, R.J. Elder, M.S. Beasley, Essentials of Auditing and Assurance Services: an Integrated Approach, Prentice Hall, New Jersey, 2003.

[4] Business Semantics of Business Rules Request for Proposal, Object Management Group (2003).

[5] C.E. Brown, D.S. Murphy, The use of auditing expert systems in public accounting, Journal of Information Systems 4 (3) (1990) 63–72.

![](/api/attachments/SEAJ8DRU/fulltext/images/b0150000ab354d248168e81a05a8e6d723ed005e1a5f429f38cdb0b205f3adeb.jpg)  
Fig. A6 (continued).

[6] Y. Chen, Continuous auditing using a strategic-systems approach, Internal Auditing 19 (3) (2004) 31–36.

[7] R.J. Daigle, J.C. Lampe, Continuous online assurance: expanding internal audit's scope, Internal Auditing 17 (5) (2002) 8–17.

[8] R. Debreceny, G.L. Gray, W.-L. Tham, K.-Y. Goh, P.-L. Tang, The development of embedded audit modules to support continuous monitoring in the electronic commerce environment, International Journal of Auditing 7 (2) (2003) 169–185.

[9] T.C. Du, E.Y. Li, A.-P. Chang, Mobile agents in distributed network management, Communications of the ACM 46 (7) (2003) 127–132.

[10] T.C. Du, E.Y. Li, E. Wei, Mobile agents for a brokering service in the electronic marketplace, Decision Support Systems 39 (3) (2005) 371–383.

[11] R.K. Elliott, Confronting the future: choices for the attest function, Accounting Horizons 8 (3) (1994) 106–124.

[12] R.K. Elliott, Twenty-first century assurance, Auditing: a Journal of Practice and Theory 21 (1) (2002) 139–146.

[13] Michael J. Fischer, “Realizing” the benefits of new technologies as a source of audit evidence: an interpretive field study, Accounting, Organizations and Society 21 (2/3) (1996) 219–242.

[14] A. Fuggetta, G.P. Picco, G. Vigna, Understanding code mobility, IEEE Transactions on Software Engineering 24 (5) (1998) 342–361.

[15] S.M. Groomer, U.S. Murthy, Continuous auditing of database applications: an embedded audit module approach, Journal of Information Systems 3 (2) (1989) 53–69.

[16] T. Hoffman, IT role in Sarb-Ox problems is unclear: users find multiple compliance hurdles, Computer World 39 (4) (2005 Feb 7) 14.

[17] A.K. Jain, M. Aparicio IV, M.P. Singh, Agents for process coherence in virtual enterprises, Communications of the ACM 42 (3) (1999) 62–69.

[18] H.S. Koch, Online computer auditing through continuous and intermittent simulation, MIS Quarterly 5 (1) (1981) 29–41.

[19] D.B. Lange, M. Oshima, Programming and Deploying Java Mobile Agents with Aglets, Addison-Wesley, Massachusetts, 1998.

[20] R. Lanza, Building intelligence into audit interrogation software, IT Audit Forum 2 (1999).

[21] L.M. Lovata, Audit technology and the use of computer assisted audit techniques, Journal of Information Systems 4 (2) (1990) 60–68.

[22] L.S. McDaniel, The effects of time pressure and audit program structure on audit performance, Journal of Accounting Research 28 (2) (1990) 267–285.

[23] W.F. Messier, Auditing and Assurance Services: a Systematic Approach, 2nd ed. McGraw-Hill Higher Education, 2000.

[24] N.H. Minsky, Independent On-line Monitoring of Evolving Systems, presented at the 18th International Conference on Software Engineering, Berlin, Germany, 1996.

[25] K.M. Nelson, A. Kogan, R.P. Srivastava, M.A. Vasarhelyi, Virtual Auditing Agents: the Edgar Agent Example, Thirty-first Hawaii International Conference on System Science, Kohala Coast, HI USA, 1998.

[26] Z. Rezaee, A. Sharbatoghlie, R. Elam, P.L. McMickle, Continuous auditing: building automated auditing capability, Auditing: a Journal of Practice and Theory 21 (1) (2002) 147–163.

[27] S.G. Robert, K. David, A.P. Ronald, B. Joyce, C. Daria, G. Peter, H. Martin. B. Jeffrey, B. Maggie. J. Renia. S. Niranian. Mobile-agent versus client/server performance: scalability in an information-

retrieval task, Lecture Notes - Computer Science 2240 (2001) 229–243.

[28] B.A. Schroeder, On-line monitoring: a tutorial, IEEE Computer 28 (6) (1995) 72–78.

[29] M.A. Vasarhelyi, F.B. Halper, The continuous audit of online systems, Auditing: a Journal of Practice and Theory 10 (1) (1991) 110–125.

[30] R. Weber, Information Systems Control and Audit, Prentice-Hall, Inc., New Jersey, 1999.

[31] N.J.E. Wijngaards, B.J. Overeinder, M. van Steen, F.M.T. Brazier, Supporting internet-scale multi-agent systems, Data and Knowledge Engineering 41 (2–3) (2002) 229–245.

[32] J. Woodroof, D. Searcy, Continuous audit model development and implementation within a debt covenant compliance domain, International Journal of Accounting Information Systems 2 (2001) 169–191.

![](/api/attachments/SEAJ8DRU/fulltext/images/8c532ea1767a5cd99d20e839dc0dbd93f096c971577802235584bf8312d2c895.jpg)  
Charles Ling-yu Chou is currently a Ph.D. student in the Department of Decision Sciences and Managerial Economics at the Chinese University of Hong Kong. He received both his BS and MSc degrees from the National Taiwan University. His research interests include computer assisted auditing model, e-commerce, product data management, web services, and semantic web technologies.

![](/api/attachments/SEAJ8DRU/fulltext/images/68bc5b90710c5c99ea1b968686b991300b10066c5e8510d622d64d258cc502a7.jpg)

![](/api/attachments/SEAJ8DRU/fulltext/images/bb34934f8e08c2ae83eddd70409452962489627a6537dd20fba57a75d312c0fc.jpg)

Timon C. Du received his BS degree in Mechanical Engineering from the National Chung-Hsing University, Taiwan, in 1989. He obtained his Master's and PhD degrees in Industrial Engineering from the Arizona State University. Currently, Dr. Du is a Professor at The Chinese University of Hong Kong, Hong Kong, and director of EMBA (Asia Pacific) Program of Faculty of Business Administration. His research interests are in e-business, data mining, collaborative commerce, and semantics webs.

Vincent S. Lai is a professor of MIS at the Chinese University of Hong Kong. He received his BSS from the Chinese University of Hong Kong, MSc in MIS from the University of Arizona, and PhD in MIS from the University of Texas at Arlington. His research focuses on electronic commerce, IS adoption and diffusion, and global IS strategy.
