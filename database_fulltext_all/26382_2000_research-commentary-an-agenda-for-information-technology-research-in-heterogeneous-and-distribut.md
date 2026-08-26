---
otero_id: 26382
otero_key: "TWPKCNEM"
title: "Research Commentary: An Agenda for Information Technology Research in Heterogeneous and Distributed Environments"
authors: "Salvatore March; Alan Hevner; Sudha Ram"
year: "2000"
journal: "Information Systems Research"
doi: "10.1287/isre.11.4.327.11873"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/TWPKCNEM/fulltext/images/bb1f7c4d52549b7ccb488a530f5d03abb6111210d6b9325e5227c082a441287f.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Research Commentary: An Agenda for Information Technology Research in Heterogeneous and Distributed Environments

Salvatore March, Alan Hevner, Sudha Ram,

To cite this article:

Salvatore March, Alan Hevner, Sudha Ram, (2000) Research Commentary: An Agenda for Information Technology Research in Heterogeneous and Distributed Environments. Information Systems Research 11(4):327-341. http://dx.doi.org/10.1287/ isre.11.4.327.11873

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2000 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/TWPKCNEM/fulltext/images/42b0f2a65eef8e68ca156a1915aed80c0195ebbcab0f3e1c9ff9aa6bf2b646c3.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Research Commentary: An Agenda for Information Technology Research in Heterogeneous and Distributed Environments

Salvatore March • Alan Hevner • Sudha Ram

Owen Graduate School of Management, Vanderbilt University, Nashville, Tennessee 37203 College of Business Administration, University of South Florida, Tampa, Florida 33620 Eller College of Business and Public Administration, University of Arizona, Tucson, Arizona 85721 sal.march@owen.vanderbilt.edu • ahevner@coba.usf.edu • ram@bpa.arizona.edu

pplication-driven, technology-intensive research is critically needed to meet the challenges of globalization, interactivity, high productivity, and rapid adaptation faced by business organizations. Information systems researchers are uniquely positioned to conduct such research, combining computer science, mathematical modeling, systems thinking, management science, cognitive science, and knowledge of organizations and their functions. We present an agenda for addressing these challenges as they affect organizations in heterogeneous and distributed environments. We focus on three major capabilities enabled by such environments: Mobile Computing, Intelligent Agents, and Net-Centric Computing. We identify and define important unresolved problems in each of these areas and propose research strategies to address them.

(Heterogeneous and Distributed Systems; Interoperability; Mobile Computing; Intelligent Agents; Net-Centric Computing)

## 1. Introduction

In a recent survey of key issues in information management (Brancheau et al. 1996) four of the top five issues relate directly to heterogeneous and distributed environments; they are (#1) building a responsive IT infrastructure, (#3) developing and managing distributed systems, (#4) developing and implementing an information architecture, and (#5) planning and managing communication networks. A responsive IT infrastructure must provide “the processor power, network connectivity, and application development framework required to support core business activities and unknown future ventures” (Brancheau et al. 1996 p. 229).

Distributed and heterogeneous computing has taken on even more significance with the rapidly expanding use of the Internet and the World Wide Web. These have literally transformed the business environment and demand both technological and managerial innovations. Organizations rely on their information processing capabilities to create and manage virtual organizations, dynamic business partnerships, and integrated supply chains, and to participate in the emerging global electronic markets. As core business activities shift from an internal / operations focus to a customer / partnership focus, an organization’s IT infrastructure must support interoperability with those of its customers and partners (Madnick 1992).

Innovative distributed and heterogeneous computing relies upon a foundation of research and development that spans a number of related fields. Each contains many exciting areas of research opportunity. Figure 1 presents a layered architecture of distributed system foundations. Each layer relies upon the technologies and capabilities of the underlying layers. The Technology Kernel provides the infrastructure of hardware, systems software, and telecommunications that comprises the physical presence of the system (Kleinrock 1985, Hevner and Berndt 2000). Welldocumented and rigorous standards and protocols enable the integration of these technologies. Research challenges in this layer, although beyond the scope of this paper, include the development of faster, smaller, and more intelligent processors, improved hardware architectures, and enhanced data transmission capabilities (Kavi et al. 1999).

The Distributed Systems Architecture, Control, and Optimization layer provides the processes, methods, algorithms, and tools to analyze, design, build, test, and deploy distributed systems. At the most controlled level of organizational and interorganizational management, distributed systems are developed using the same hardware and operating system platforms, the same languages and tools, and syntactically and semantically consistent data and processing definitions. In such an environment, distributed systems can be efficiently developed to optimize performance measures such as cost, response time, flexibility, maintainability, security, scalability, and reliability. This is essentially the “distributed system design” task—what an organization would do if it could develop its information processing capability “from scratch.” Research issues in this area are discussed in §2.

Rarely do organizations have this luxury. Numerous legacy systems often exist. These typically exhibit some level of heterogeneity. They are implemented using different hardware, operating systems, languages, DBMSs, and data and processing definitions. They have different levels of data and processing security, integrity, and validation requirements. They are often mission critical and too expensive to replace or integrate or, for organizational, managerial, or logistical reasons, require a significant level of autonomy—they must control their own definitions. This is the realm of the Heterogeneous Interoperability layer. Research needed to achieve high levels of heterogeneous interoperability is discussed in §3.

![](/api/attachments/TWPKCNEM/fulltext/images/7d081fd155eacbae23a9b7c4aba0d0e1f63890ed2f404d6afc890bf5f8094d73.jpg)

Distributed and heterogeneous interoperability technologies enable the development of capabilities with which organizations can address core information processing problems and opportunities. We discuss research issues underlying three such capabilities, Mobile Computing, Intelligent Agents, and Net-Centric Computing, in §§4, 5, and 6, respectively. Mobile Computing integrates wireless communication and hand-held computing technologies to yield “anytime, anywhere” computing and connectivity. Intelligent Agents integrate artificial intelligence, database, information retrieval, and decision support technologies to yield software systems that can act “as an agent of” a person or organization in tasks such as searching for information, identifying suitable trading partners or customers, monitoring or negotiating prices, and making purchase, sale, or production decisions. Net-Centric Computing integrates the Internet and the World Wide Web with the information processing capabilities of organizations to yield a “global, digital economy” in which global partnerships and virtual organizations can be instantly formed and managed.

These have significant potential for becoming major innovations (Tsichritzis 1999), though each has significant technical, organizational, and behavioral challenges that must be addressed when organizations make commitments to electronic commerce and web systems. These include, for example, concerns over security, integrity, performance, standardization, cost, usability, manageability, and acceptance. In this paper we focus on the technical challenges and research issues in heterogeneous and distributed environments. Section 7 summarizes and places them in the context of an overall research agenda.

## 2. Distributed Systems Architecture, Control, and Optimization

The transformation of physically networked computers into an effective and efficient distributed system requires methods and techniques for building a systems architecture, establishing rigorous controls, and optimizing the system performance. In this section we highlight important research topics in these areas.

## 2.1. Architecture

Distributed system architectures define the allocation of hardware, networking, application software, and data in a distributed environment. Strategies are designed for the movement of data and control information (e.g., synchronization) throughout the system (Andrews 1991). While client-server architectures (Adler 1995) have proven to be a popular choice for distributed systems, event-driven architectures are emerging, as requirements for real-time, on-demand behaviors become more prevalent (Fidge et al. 1997). Based on the architectural infrastructure, distributed software development methods are used to build application systems. Current trends in distributed software engineering include a move toward componentbased development (Brown and Wallnau 1998), widespread use of middleware products (e.g., CORBA, DCOM, and EJB), and the development of integrated tool environments (Rover et al. 1998).

## 2.2. Control

Processing in a distributed system that supports parallel activities is likely to involve asynchronous and, often, nondeterministic behaviors. Control issues are paramount in order to maintain system correctness and reliability. Architectural decisions and control methods are tightly interwoven. For example, data replication will increase system availability in the presence of failures but also will require sophisticated control algorithms for maintaining integrity and consistency across all copies (Anderson et al. 1998). Research and development are very active in the following areas:

• Transaction Management. A transaction is a bounded collection of actions that constitutes a meaningful client interaction with the system. A transaction must satisfy four critical properties: Atomicity, Consistency, Isolation, and Durability (ACID). Achieving these when transactions are geographically distributed and long-lived (e.g., days to weeks) remains a challenging research problem (Bernstein and Newcomer 1997).

• Fault-Tolerance and Survivability. The demand for dependable distributed systems drives research on methods for detecting and correcting faults during execution (Gartner 1999). The goal is to produce robust systems that can survive in the presence of faults and continue to perform correctly (Ellison et al. 1999). A particularly interesting line of research is the development of control methods that support system survivability when the network is partitioned (Melliar-Smith and Moser 1998).

• Security and Privacy. In the Internet age, society is rightly concerned over security and privacy issues. The high level of interconnectivity among distributed systems raises control requirements for trust levels, encryption, intrusion detection, malicious code (e.g., virus) protection, and enforceable security policies (Pfleeger and Cooper 1997).

• Data Quality. The quality of data in a system can be described in four dimensions: intrinsic, accessible, context, and representation (Wang and Strong 1996). A distributed system must support the verification, maintenance, and presentation of quality data in its processing.

• Maintenance and Evolution. Effective distributed systems provide means for continuous maintenance and evolution. Control issues include scalability for the addition/deletion of resources (e.g., new sites), portability to new platforms, and configuration management (e.g., version control).

## 2.3. Optimization

The efficiency of a distributed system is predicated on the optimization of its processing performance. The two classes of optimization algorithms are static and dynamic. Static optimization focuses on long-term design decisions such as the selection of site locations, hardware configurations, data and software allocations, and network topology and line bandwidths. During system execution, dynamic optimization algorithms monitor the actual, real-time system state and make decisions on query/update strategies, replication of data copies to additional sites to increase availability, and when to change control authorities in the presence of system faults. The ability to monitor and measure performance properties (e.g., resource utilization, transaction response time) in the global distributed state is key to dynamic optimization (Jakiela 1995, Garg 1997).

## 3. Heterogeneous Interoperability

Modern organizations use a wide variety of distributed information systems to conduct their day-to-day business. These access a variety of databases, they operate on different hardware platforms (e.g., mainframes, database servers, personal computers, workstations), use different operating systems (e.g., Windows, UNIX, and Macintosh) and DBMSs (e.g., Oracle, DB2, Informix), and have different database structures (e.g., relational, object-oriented) with varying semantics (e.g., units of measurement, scales, naming, meaning of data).

While research has successfully addressed many hardware, operating system, DBMS, and structural heterogeneities, semantic heterogeneities continue to pose enormous challenges. Briefly stated, a semantic heterogeneity exists when data is defined differently in different databases. Differences can be as simple as different naming conventions (e.g., l\_name in one database and last\_name in another) or measures (e.g., dollars in one database and lira in another). They can be as complicated as different rating scales (e.g., 1–10 for credit rating in one database vs. A, B, C in another) or different meanings for the same data item (e.g., a field value “Land Type” having a value of “suitable” to indicate “suitable for road construction” in one database vs. “suitable for sewage disposal” in another). Such differences must be resolved if systems are to interoperate. This is termed the semantic interoperability problem. If managed centrally, database definitions can simply be changed to conform to a single semantic.

The challenge is to make diverse information systems interoperate at the semantic level, in the face of organizational or economic constraints that require them to remain autonomous, i.e., retain their differences. Important challenges in addressing semantic interoperability include: schema integration, schema evolution, and query processing.

## 3.1. Schema and Data Conflict Resolution

In the late-1980s to mid-1990s, many research efforts examined the semantic interoperability issue. Most of these addressed differences in structured data sources, i.e., those managed by DBMSs and file systems. Two distinct approaches emerged, the Global Schema Approach and the Federated Schema Approach. These were extensions of earlier view integration techniques (Batini et al. 1986), i.e., techniques for generating a single integrated schema from multiple user views.

The Global Schema Approach generates a single “integration schema” or enterprise wide schema from those of the participating databases (Ram and Ramesh 1999). This approach is not practical if multiple and autonomous groups or organizations are interested in sharing data. Hence the Federated Schema Approach evolved as an alternate solution (Sheth and Larson 1990). This approach offers a compromise between complete integration (as in the Global Schema Approach) and no integration at all. However, it may not be able to deal with all of the semantic heterogeneities that exist in the participating databases.

In today’s environment, a third approach, the Data Warehousing Approach, has emerged (Chaudhuri and Dayal 1997). In this approach, data is extracted from multiple operational databases, cleaned to eliminate errors and missing data, transformed into a common format by resolving any syntactic, structural, or semantic conflicts, and then loaded into a data warehouse.

Several efforts are addressing the problem of data cleaning and the semantic conflict detection and resolution process. Comprehensive taxonomies are being developed to define various types of semantic conflicts found in traditional business databases (Kashyap and Sheth 1996, Kim and Seo 1991). Recently, this work has been extended to cover conflicts found in geographic and temporal databases (Ram et al. 1999c). Such frameworks form the basis for automatic conflict identification. Incorporating techniques from the data mining and information retrieval (IR) communities can also facilitate detection and resolution of conflicts.

## 3.2. Versioning and Schema Evolution

In a distributed environment the number and variety of data sources can change frequently. Furthermore, the content and structure of existing data sources can change. Thus it is not sufficient to map from a federated schema to a static underlying export schema of a local data source. Changes to local schemas must be dynamically tracked to determine their effects on the federated schema. Changes to the schema of one local database may require a cascading set of changes to other local database schemas. Manually tracking and understanding the implications of such changes is a very complex problem.

The schema evolution problem has been extensively addressed in the context of a single database (e.g., Ra and Rudensteiner, 1997). Schema evolution in such an environment is defined as the process of incorporating changes into the database schema without loss of existing data and with minimal modification to applications. Prevalent approaches include coercion (Peters and Ozsu 1997) and versioning (Liu et al. 1997).

In coercion, existing data are changed to conform to the changed schema immediately and a new database schema is created. When versioning is used, changes are not made to the data; a new version of the schema is created for every change and only changed schema objects are associated with the new schema version. Some “relaxed” (i.e., noncoercion and nonversioning) techniques based on graph-theoretic modeling have been proposed that can be extended to the problem of schema evolution in a heterogeneous environment (Ram and Shankar 2000). These techniques use a welldefined semantic model graph to identify the types of schema changes that could occur and the actions that need to be taken for each type of change. Using a graph-theoretic model assists in defining a set of operations that are proven to be correct and complete in tracking all possible schema changes. The graphtheoretic approach needs to be explored further as a way of automating the schema evolution and management process. This is especially important given the variety of heterogeneous web information sources.

## 3.3. Query Processing in Heterogeneous Database Systems

The issue of processing queries in a heterogeneous environment has also been addressed extensively (Sheth and Larson 1990). A global query language is used to query multiple databases via a global or federated schema. The global query is first decomposed into subqueries, each of which can be sent to one more underlying local databases. Each subquery is translated into a form that the local database can process. Results are gathered back from each local database and assembled before being presented to the end user. Much of the research has focused on developing query languages for a global schema, efficient query decomposition procedures, and techniques for translating between different query languages. This work needs to be extended to deal with multiple heterogeneous web resources. These do not have structured schemas so structured query languages are therefore insufficient.

The above foundational research in distributed systems and heterogeneous interoperability has enabled a number of exciting information processing capabilities. In the next three sections we focus on three of them, Mobile Computing, Intelligent Agents, and Net-Centric Systems.

## 4. Mobile Computing

Anytime, anywhere (i.e., ubiquitous) computing is the goal of research and development on mobile computing. Mobile computing applications are increasingly viable because of recent advances in portable information devices and high-speed wireless communications. Computing and information resources can be linked from anywhere to anywhere in the world at any time of the day via the Internet or direct network connections. A mobile user will be provided with a fully functional view of the desired distributed system environment. It is not too far-fetched to predict that mobile computing will become the dominant paradigm for future computing applications.

A mobile computing environment can be recognized as a special case of a general distributed heterogeneous computing environment. Mobile users are simply clients for more powerful servers. The following distinctive conditions apply in mobile environments (Satyanarayanan 1996):

• Mobility. Users carry portable computers from place to place while connected to or disconnected from system resources. The location of a user is a critical factor in providing effective system service. For example, queries may depend on mobile client locations—“Retrieve all clients who are within five miles of Client A.”

• Resource Constraints. Portable client devices have limitations on computing speed, memory/disk size, battery power, screen size/resolution, and reception range.

• Frequent Disconnection. The unreliable nature of wireless communication, as well as the nature of mobile applications implies frequent client connection and disconnection.

• Variable, Slow, and Asymmetric Communication Links. The quality of wireless connections varies widely in terms of bandwidth and reliability depending on distance between sender/receiver and atmospheric conditions, among other considerations. At best the speed of wireless data transmission is two to three orders of magnitude slower than wired transmissions. Because of the limited power resources of the client, the bandwidth from client to server is typically much smaller than the bandwidth from server to client on the communications link.

• Risks. The physical security and the electronic security of small, mobile client devices (e.g., laptops, PDAs) transmitting over open air are very difficult to ensure.

The intriguing and seemingly unlimited potential of mobile applications and the inherent constraints of mobile systems make mobile computing a rich arena for research and development. Because of the need for equipment intensive experimental environments, a significant amount of this research features collaborative efforts between industry and academia. Experimental mobile computing systems include Bayou (Xerox PARC), Coda and Odyssey (Carnegie-Mellon University), and Rover (MIT) (Jing et al. 1999). We discuss three important areas relevant to MIS researchers—system agility, location management, and data management.

## 4.1. System Agility

Mobile systems must be extremely agile to respond effectively to changing environmental conditions while maintaining acceptable levels of user service. System agility combines requirements for awareness, adaptability, and control (Satyanarayanan 1996). The decentralized nature of mobile systems places a great burden on individual clients and servers to estimate the global state of the overall system. Environmental awareness is critical for mobile applications to achieve quality of service goals. Server resources (e.g., bandwidth, data) should only be allocated to client requests when there is a good chance of eventual application success. Some initial research on building environmentally aware mobile architectures is underway (Welling and Badrinath 1998). A key issue of awareness is the location management of mobile clients as discussed below.

Mobile applications rely on the adaptability of the system to meet dynamic resource needs. Policies for resource allocation, deallocation, and reallocation must exist under some form of centralized or decentralized control. Rapid system adaptability to the needs of mobile applications must be balanced with the need to maintain overall system stability. This is an area rich in research opportunity. The problem is how to optimize the use of system resources to achieve overall system goals of performance, reliability, and stability. Research from the areas of transaction management and control theory should provide insights to solution techniques.

## 4.2. Location Management

Wireless communication technology and protocols support the mobile client (MC). An MC moves from cell to cell of wireless subnets. Handoffs between cells are handled by sophisticated wireless communications protocols. However, if the MC is participating in a mobile computing application, the mobile system must be aware of the hand-off. Thus, the location and address of the MC will potentially change during calls and upon each new connection to the system. Location management must provide two important functions: (1) continual updating of an MC’s location and (2)

on-demand searching for a specific MC in the mobile system. Effective location management strategies must be scalable to a very large number of MCs, efficient so as to minimize network overhead and MC battery drain, and timely so that accurate location information is available with little delay.

Numerous strategies have been proposed for mobile location management (Badrinath and Imielinski 1996). However, no one strategy has been shown to be superior for scalability, efficiency, and timeliness based on theoretical or experimental analyses. Potential research directions in mobile location management include the use of intelligent network agents to manage MC locations, the use of location information to balance processing loads among servers (Krishnamurthi et al. 1998), and the application of research in directory management to better understand issues of number and location of directory copies (e.g., query vs. update costs) containing location information.

## 4.3. Data Management

Challenging research issues abound in the area of data management in mobile computing systems (Barbara 1999, Jing et al. 1999). The movement of data is severely constrained by limited capacity and power of the mobile client and the relatively slow speed of wireless communications.<sup>1</sup> Thus, most data management strategies emphasize server broadcasts of data (i.e., server push) into the mobile system environment. This strategy is also termed a “broadcast disk” where the server continuously and repeatedly transmits data packets in an optimized pattern. For example, the most frequently accessed data, so-called hot spots (e.g., stock prices, sports scores, airline schedules), are transmitted more often. The mobile client, when connected, can “tune in” to the desired data on the broadcast. To minimize client search and connect times, efficient indexing structures are provided on the broadcast disk (Imielinski et al. 1997). As clients connect and disconnect from the system, the broadcast disk is always available for access.

Specific data requests from the mobile client are typically handled on a separate, lower bandwidth channel. Such “client pull” requests are directed to a selected server based on client locations and server loads. Strategies for handling directed data requests are optimized to minimize energy expenditure by the client by moving most processing into the server (Datta et al. 1999). Since web browsing is anticipated to be a prevalent activity in mobile systems, optimal fetching schemes for web pages is an interesting research direction (Jiang and Kleinrock 1998).

Well-known database research problems, such as distributed query optimization, data allocation/replication, concurrency control, and rollback/recovery, take on new and interesting dimensions in a mobile computing environment. The applications of existing solutions for these problems to mobile environments are not obvious. New insights based on a thorough understanding of mobile environments and applications are required.

## 5. Intelligent Agents

The emergence of the Internet and the World Wide Web has significantly increased the scope and scale of data distribution and heterogeneity. This increasingly pervasive and global information infrastructure enables the concept of an Infocosm (Sheth 1997), “a society where information is available anytime, anywhere, and in many forms enabling knowledgeintensive and cooperative activities. These support effective decision making, higher organizational efficiency and enterprise integration, and more personal effectiveness and fun.”

Achieving such a vision, however, requires new approaches to semantic interoperability. We must deal not only with a broad variety of digital data such as text, numbers, audio, video and images, but also with algorithms and processes that operate on these data and models that interpret and transform this data into information and knowledge.

Exacerbating this problem is the magnitude and volatility of the available data. The scale has changed from a few databases managed within a single organization to millions of information sources, many of which are virtually unmanaged. Moreover, new sources are continuously being introduced as others change or disappear. Search engines that involve only representational or structural components of data are insufficient. Their lack of precision leads to increasing information overload and frustration. Intelligent agents are emerging as a way to deal with the staggering variety and volume of data in distributed and heterogeneous environments.

An intelligent agent is a piece of software that acts “intelligently” and “in the place of” a human to perform a given task. Some desirable properties of an intelligent agent are autonomy, adaptability, mobility, and communication ability. To deal with the size and complexity of information on the Web, it is desirable to have different types of agents, each specializing in different tasks, but collaborating to solve a problem. A Virtual Enterprise Architecture (VEA) defines an organization of three types of agents, demand agents interact with end users to understand their needs, supply agents know about and interact with information sources, and broker agents act as intermediaries in matching users’ needs with available resources (Brown et al. 1995). Given the number of sources of information on the Web, such a network of collaborating agents can ease the task of information discovery and retrieval and appears to be a promising research direction. This section describes the research issues that arise in the context of developing such collaborating intelligent agent systems.

## 5.1. Information Overload

Currently there are more than 800 million pages on the Web; this number is expected to grow exponentially. While there are many different search engines available to help people find relevant pages, most yield a large number of “hits,” often sacrificing precision for recall. The enormous burden of sifting through the search results rests squarely on the end user. Services are needed that go beyond the capabilities of current search engines and automatically gather, manipulate, integrate, and interpret data from multiple information sources. These should understand the context of a user’s information need and provide context-sensitive information processing. A challenging problem is to define the context for each user and develop ways to capture and use context to limit information overload. This may be accomplished by personalized intelligent agents that interact with the user to formulate more precise queries and filter and transform the resulting information. The design of such learning and filtering agents is an important open research issue. These need to be domain independent and easily generalizable across a number of different application areas (Ram et al. 1999a, Ram et al. 1999b). Further, they must access and interpret diverse types of data including images, tables, and arrays of data, along with unstructured text.

## 5.2. Unstructured Heterogeneous Web Sources

Earlier work addressed ways to integrate structured data sources using a global or federated schema. The environment on the Web today is very different. It includes many sources of unstructured data. Most web sources are designed primarily for human browsing rather than for use by a program. Automatically extracting their content typically is very difficult. Further, given the rapid growth of the WWW, it is not always possible to anticipate the exact set of data sources that will be used to assemble information for any given need. This means that it is not always possible to know in advance exactly what kinds of semantic conflicts will occur.

Hence we must go beyond the concepts of schema integration and global query processing typical of past approaches. The concept of a “mediator” (Wiederhold 1992) has been proposed to deal with the dynamic semantic interoperability common to such environments. A mediator is an intelligent agent that acts as a broker between a set of information sources and a set of applications. A mediator exploits knowledge about specific data sources and applications to access relevant data from multiple heterogeneous sources, dynamically identify semantic conflicts, and collaborate with other mediators to resolve them.

The effective construction of such mediation services requires a common representation of the underlying semantics of the data resources and applications accessing them. Such a representation is termed an ontology (Uschold 1996). For semantic interoperability, an ontology should be general enough to identify and enable the resolution of a wide range of conflicts that can occur in a given environment, including those that exist in images, video, and other multimedia data sources. The development and testing of such ontologies and embedding them within intelligent agents are important and difficult research tasks.

## 5.3. Support for Dynamic Evolution

Web information sources are constantly changing— new sources are continuously being added as old ones are updated or deleted. Information sources often change location, content, or appearance, or simply get outdated. Schema evolution techniques described in §3.2 are impractical because of the overwhelming need for autonomy. Given this continuous evolution, it is important to develop techniques to track changes so that appropriate information sources are used. Intelligent agents can keep a memory of users’ web sessions and notify them when relevant websites change, are deleted, or become outdated. New semantic information processing techniques are needed to develop such agents. Such techniques may exploit metadata, or the description of a resource (perhaps encoded in XML), to determine if it is worth visiting a website.

## 5.4. Knowledge Management

Effective knowledge management is among the most significant challenges facing modern business organizations. If business teams and individuals could always locate accurate, timely, and relevant information, along with the insights of experts on how to proceed, they would be more effective at identifying opportunities and solving problems (Dixon 2000). Intelligent agents can electronically capture and make such knowledge available within an organization. Successful knowledge management treats knowledge as a resource, utilizing intelligent agents to exercise selectivity, impose order on information resources, add structure to ill-structured information to increase its value, and proactively capture information that may be useful in the future. The insights, understanding, and intuition of experts also can be codified into more structured forms, such as rules for solving specific business problems, and even be embedded into automated workflow. However, because of the diversity and unpredictability of real-world opportunities, it is often difficult to codify knowledge to this extent. Research in OLAP (Chaudhuri and Dayal 1997) and data mining techniques (Fayyad and Uthurusamy 1996) offer promise in capturing derived knowledge in a reusable form.

## 5.5. Measurement and Metrics

Considerable resources are being invested in developing intelligent agents for heterogeneous and distributed environments. It is important to quantify and measure their benefits. Metrics must be developed that are robust, parsimonious, and easy to measure. Their application should result in an easy and unambiguous interpretation. However, calculating the return on investment can be a challenging undertaking given the uncertainty of benefits, many of which are intangible. Typical benefits of an agent-based system are time savings, more and better information, better decisions, improved business processes, and support to accomplishing strategic business objectives. Specific case studies are needed to facilitate the development, evaluation, and utilization of generalizable measures to evaluate large-scale agent-based efforts. Such studies should provide insights into the agent-based system development process and facilitate the development of future systems.

## 6. Net-Centric Systems

A recent DARPA funded study defined Netcentricity as “the power of digital networks to distribute information instantly and on a global scale.” It concluded that a national research agenda is needed to address “the strategic, managerial, technical, and behavioral factors that accelerate or hinder” its diffusion (DARPA 1999). Distributed and heterogeneous interoperability technologies are foundational for the development of Net-Centric systems, the systems that enable this concept.

Theoretically any system having access to the Internet can be considered to be “Net-Centric.” That is, given access to the Internet, any system can request information from and provide information to any other such system. However, there are a number of technical issues that must be addressed before the necessary levels of security, accessibility, and interoperability required to support the concept of Netcentricity are achieved.

## 6.1. The Electronic Marketplace

The business needs underlying Netcentricity are not new. Electronic Data Interchange (EDI) is among the earliest attempts to utilize technology to meet them (Sullivan 1998). Central to EDI is the definition and standardization of terms needed to conduct various business transactions. These enable partners in the transaction to communicate with each other electronically without modifying their internal application systems. They do so by establishing a vocabulary and grammar for communication. Often an intermediary provides document transmittal services including security, validation, tracking, and reliability.

Utilizing the EDI standards for Purchase Order (850), Ship Notice (856), and Remittance Advice (820), for example, organizations can easily establish electronic trading partner relationships. The buyer sends an 850 to the seller. The seller ships the order and responds with an 856. Upon receipt, the buyer pays for the order and confirms payment with an 820. Internal systems at the buyer and seller sites produce and interpret these documents.

Such arrangements are sufficient for simple trading relationships where particulars such as product identification, units-of-sale, pricing, payment terms, delivery method and timeframe, and backorder policies are established in advance and remain fixed for a period of time, typically by contract. However, they do not support the rich interactions, dynamic relationships, and negotiations that characterize the current business environment. EDI is fundamentally a syntactic, tagbased language and is thus insufficient for collaborations and exchanges that require semantic understanding. EDI documents, for example, define where the unit-of-sale and payment terms must go, but not what they mean. While issues of price and delivery timeframe can be “negotiated” using EDI standards such as Purchase Order Acknowledgement (855) and Purchase Order Change (860) documents, it is more like sending a “message in a bottle” then engaging in a business exchange.

Electronic markets are emerging as a viable replacement for EDI-based trading partnerships. These are typically accessible through the World Wide Web, either directly from buyers or sellers or through an intermediary (such as eBay, GE’s Trading Partner Network, CommerceOne, or Ariba). They use web documents to post products or services. These must be interpreted by potential trading partners. Lack of standards in document formatting and terminology make electronic interpretation a daunting task. Hence, although utilizing an “electronic” media to post items, other processes such as search, negotiation, ordering, and payment are still typically done manually.

XML (eXtensible Markup Language) is a promising technology to address some of these problems (St. Laurent and Cerami 1999). Current work in developing XML standards, however, suffers from the same limitations as EDI standards. XML tags enable the interpretation of data posted on web pages by specifying the type of data, e.g., a product number, product description, or price, however, they do not address the semantics of the data, e.g., what the product is, how it is used, the meaning of price. Hence, as with EDI, XML is developing as a syntactic, tag-based language. Significant efforts are being expended to integrate EDI and XML. We argue that such efforts are a beginning, not an end. Since XML is extensible and since the standardization effort is in its early stages, it has the potential to overcome some of these limitations. These efforts must be integrated with work in ontologies, data quality (Wang and Strong 1996), and common sense reasoning (Goldstein and Storey 1991, Storey et al. 1997) to develop semantic as well as syntactic standards.

The interpretation of a data item specified as “Price,” for example, depends on a number of factors such as payment currency (exchange rates), unit-of-sale (e.g., per gallon or per pound), number of units purchased (price break quantities), and terms-of-sale (e.g., billed or advanced payment). Significant research efforts are needed to identify and define those factors that are necessary to enable the interpretation of such data items if processes such as purchase negotiations are to be supported.

A research agenda in this area must focus on the identification and semantic modeling of tasks that must be supported in various domains. Electronic trading is simply one example. Others include distributed decision-making and problem solving, intelligence gathering, problem and opportunity identification, inter-organizational collaboration, and joint ventures. Furthermore, since these are relatively uncharted waters, prototype systems should be developed and tested in specific trading domains to enable the identification of problems and opportunities for additional research efforts.

## 6.2. Developing Net-Centric Systems

Net-Centric systems are based on a fundamental client-server model of computing. Client-side and server-side applications may themselves use an ntiered architecture and what is the “client” in one interaction may be the “server” in another. The interactions may be simple, such as a Web Server (server-side) servicing Hyper-Text Transfer Protocol (HTTP) requests from a Web Browser (client-side).

However, they can be considerably more complex. A user on the “client-side” may, for example, interact with the organization’s sales order system, itself an ntiered application, through a web browser. The user enters an order into the browser. As a result, the web server interacts with an application server supporting the sales order system. This application server interacts with a database server hosting the sales, purchases and inventory database. As a result the inventory level for a product may drop below its reorder point. A trigger in the sales, purchases and inventory database causes this database server to interact with an application server supporting the purchase order system, which determines that a replenishment order should be placed, decides on the quantity to order, and from which vendor. All of this happens on the “client-side,” possibly on different machines, possibly in different geographic locations.

The purchase order system on the “client-side” must interact with the vendor’s sales order system on the “server-side.” Of course, the vendor’s sales order system may also be n-tiered. The interaction may utilize a web server on the “server-side” or it may use the Internet to send messages directly to a Distributed Object on the “server-side.” To accept the order the vendor may need to request additional information, such as authorization to accept a price or delivery change. For that interaction, “client” and “server” roles are reversed.

Distributed objects can be used to directly support client-server interactions. A distributed object is a named information processing capability (an object) that is registered on some machine. As with any object, a distributed object has a well-defined interface (messages to which it can respond). Messages may be sent to it from any machine that is connected to the network. These evoke the information processing capabilities of the object, which can include sending messages to other (distributed) objects and accessing application and database servers.

There are a number of mechanisms through which a distributed object can be realized, including Enterprise Java Beans (EJB), Common Object Request Broker Architecture (CORBA), Java Remote Method Invocation (RMI), Distributed Common Object Model (DCOM), and even direct communication (Socket) programs. To make matters more confusing, a web server can be considered to be a “distributed object.” It is named by the IP address of the machine on which it is implemented. It has a well-defined interface—requests to use a specified protocol to “serve” named files. It takes specific actions based on the type of file to be served, e.g., returning HTML files but executing Active Server Page (ASP) or Cold Fusion Method (CFM) files and returning the execution results. Furthermore, an application server may itself be a collection of interrelated distributed and local objects that form a “wrapper” around legacy applications (e.g., Object Oriented Middleware products).

Distributed objects open new opportunities and challenges for developing Net-Centric systems and for addressing the semantic problems raised above. As envisioned by the Object Management Group (OMG), Common Business Classes provide informationprocessing capabilities common to a variety of organizations (Chandra et al. 2000, Guttman and Matthew 1995, March et al. 1999). They are organized into components such that the classes within a component operate together to provide a coherent set of capabilities for specific functional areas such as sales order processing, procurement, finance, or human resources. They can be shared across organizations and effectively define a standard vocabulary for implementing applications that use these capabilities. Furthermore, as with any object technology, these classes are extensible, thus enabling significant customization within an organization without sacrificing the basic functions that make them sharable and allow cross-application integration and interoperability.

Hence, defining a standard set of common business classes can both reduce development time and effort and enable interoperability of the developed systems. Basic research in this area must address the feasibility of developing, managing, and sharing such classes and their instantiations across specific organizations. IBM’s San Francisco project (Arnold et al. 1997, Bohrer et al. 1998) is an attempt to define the infrastructure needed to support such a concept. Of particular concern is managing objects—instances of these classes. Conceptually, an object represents one “thing” in the world. That “thing” in the world should correspond to exactly one instance in the information system. That instance must be persistent, that is, have existence independent of the application using it. Thus it must be globally identified and there must be mechanisms through which messages can be sent to it from any application, anywhere on the network, independent of platforms, operating systems, and implementation languages.

There should, for example, be a single object within the information system corresponding to the single business organization IBM. That business organization can play the role of customer, vendor, consultant, partner, competitor, all at the same time. It is, however, the same “thing” in the world. Furthermore it is likely that this same “thing” in the world is represented in multiple organizations’ information systems—IBM is likely a customer, vendor, consultant, partner, competitor for many organizations. This fact must somehow be recognized when partnerships are formed and these systems are required to interoperate.

If common business classes are to have significant impact on the development of Net-Centric systems, additional research must resolve the problems of object persistence and object identification across multiple organizational information systems. Object Oriented Database Management Systems (OODBMS) are an approach to this problem; however, they typically address object identification only within the database, leaving a significant disconnect between the OODBMS and the network environment in which these objects must behave.

## 6.3. Performance and Scalability

Given the scope and complexities inherent in Net-Centric systems, performance and scalability are issues demanding significant research (Christ et al. 2000). While there are a number of performance issues that must be addressed; speed, cost, security, and reliability are among the most significant. These become even more problematic as the number of interacting Net-Centric systems grows. Performance bottlenecks must be identified and solutions developed for them. Recent experiences with denial of service attacks against “store-front” websites (Harrison 2000) highlight the fact that it is a simple matter to overload a web server. Net-Centric systems, by their very nature, are exposed to such threats. Even if unauthorized access is thwarted by a robust security mechanism, there can be a significant cost to implementing that security mechanism. In the face of a well-orchestrated assault, the detection effort may degrade performance to the point that authorized access becomes untimely, even if the server machine is able to withstand the load.

## 7. Summary and Conclusions

Application-driven, technology-intensive research is critically needed to meet the challenges of globalization, interactivity, high productivity, and rapid adaptation faced by business organizations (Madnick 1992). Business organizations are demanding information processing capabilities that enable and facilitate the management of distributed operations, virtual organizations, dynamic business partnerships, integrated supply chains, and enable them to engage in global electronic markets. These business environments are increasingly distributed and heterogeneous.

We focus on three capabilities enabled in such environments, Mobile Computing, Intelligent Agents, and Net-Centric Computing. These define areas for fruitful research, connected by a number of prevailing themes; technology push, scalability, pervasive heterogeneity, performance, domain independence, and production experience. Each is briefly summarized below.

• Technology Push. Research must track the steady advances in the underlying technology kernel and their implications for developing and managing information capabilities within organizations. The emergence of a highly reliable, high-speed network capability in the Internet, for example, has significantly changed the way in which businesses can organize and business be conducted. It was simply not feasible to create and manage virtual organizations in real time without this capability. Similarly, the significant increase in communications bandwidth has dramatically changed the fundamental assumptions in distributed database design. Rules-of-thumb, assumptions, and constraints are predicated on state-of-the-art technologies. They become rapidly outdated with changes in the underlying technology.

• Scalability. Any effective solution must be scalable to thousands and perhaps millions of users. Research prototypes are extremely valuable in assessing the feasibility of concepts and ideas. Solutions should continue to be built and tested in research laboratories. However, researchers must address the fundamental problems encountered in real-world environments.

• Pervasive Heterogeneity. The diversity of information formats and content is a salient factor in nearly all distributed systems. Research must focus on the semantic issues involved in such systems. Ontologies and standardization are approaches to dealing with textual and numeric data; however, these must be extended to the effective handling of multimedia content. There is currently no conceptual basis for representing the underlying semantics of a video or even of complex images.

• Performance. Efficiency cannot be overlooked in the pursuit of distributed system solutions. Optimization approaches that minimize user response times or maximize system resource utilization are important research contributions. Intimately related to scalability and technology push, performance is concerned with defining evaluation criteria and the effects of design decisions on those criteria. Performance studies can help identify bottlenecks caused by technology limitations and predict the effects of system scale and technology advances.

• Domain Independence. Effective distributed system solutions must be generalizable across multiple domains. While preliminary efforts in such areas as ontology and standards will, of necessity, focus on specific domains, the ultimate goal is to develop concepts and constructs that are largely independent of the application domain. Projects such as the “common sense reasoner” (Goldstein and Storey 1991) are a start in this direction.

• Production Experience. Research in heterogeneous, distributed systems must be aligned with real-world production experience. Closely related to scalability and performance, this works in two ways. Results from industrial experience should be available for feedback and analysis by research groups. Proposed new solutions must be amenable to experimental design and implementation in production systems. Collaborative industrial/academic research projects are called for in order to maximize productivity and accelerate solution acceptance into production-grade distributed systems.

## References

Adler, R. 1995. Distributed coordination models for client/server computing. IEEE Comput. 28(4) 14–22.

Anderson, T., Y. Breitbart, H. Korth, A. Wool. 1998. Replication, consistency, and practicality: Are these mutually exclusive? Proc. SIGMOD Conf., Seattle, WA, 484–495.

Andrews, G. 1991. Paradigms for process interaction in distributed programs. ACM Comput. Surveys 23(1) 49–90.

Arnold, V., R. Bosch, E. Dumstorff, P. Helfrich, T. Hung, V. Johnson, R. Persik, P. Whidden. 1997. IBM business frameworks: San Francisco project technical overview. IBM Systems J. 36(3), 437– 445.

Badrinath, B., T. Imielinski. 1996. Location management for networks with mobile users. T. Imielinski and H. Korth, eds. Mobile Computing. Kluwer Academic Publishers, 29–152.

Barbara, D. 1999. Mobile computing and databases—A survey. IEEE Trans. Knowledge Data Engnrg. 11(1) 108–117.

Batini, C., M. Lenzirini, S. Navathe. 1986. A comparative analysis of methodologies for database schema integration. ACM Comput. Surveys 18(4) 323–364.

Bernstein, P., E. Newcomer. 1997. Principles of Transaction Processing for the Systems Professional. Morgan Kaufmann Publishers, Inc.

Bohrer, K., V. Johnson, A. Nilsson, B. Rubin. 1998. Business process components for distributed object applications. Comm. ACM 41(6) 43–48.

Brancheau, J., B. Janz, J. Wetherbe. 1996. Key issues in information systems management: 1994–95 SIM Delphi results. MIS Quart. 20(2) 225–42.

Brown, A., K. Wallnau. 1998. The current state of CBSE. IEEE Software 15(5) 37–46.

Brown, C., L. Gasser, D. O’Leary, A. Sangster. 1995. AI on the WWW: Supply and demand agents. IEEE Expert 10(4) 50–55.

Chandra, J., S. March, S. Mukherjee, W. Pape, R. Ramesh, R. Rao, R. Waddoups. 2000. Information systems frontiers. Comm. ACM 43(1) 71–79.

Chaudhuri, S., U. Dayal. 1997. An overview of data warehousing and OLAP technology. ACM SIGMOD Record 26(1) 65–74.

Christ, R., S. Halter, K. Lynne, S. Meizer, S. Munroe, M. Pasch. 2000. San Francisco performance: A case study in performance for large-scale java applications. IBM System J. 39(1) 4–20.

DARPA. 1999. Harnessing the Power of Netcentricity: A National Research Agenda. Robert H. Smith School of Business, University of Maryland, College Park, MD.

Datta, A., D. Vandermeer, A. Celik, V. Kumar. 1999. Broadcast protocols to support efficient retrieval from databases by mobile users. ACM Trans. Database Systems 24(1) 1–79.

Dixon, N. M. 2000. Common Knowledge: How Companies Thrive by Shar ing What They Know. Harvard Business School Press, Boston, MA.

Ellison, R., R. Linger, T. Longstaff, N. Mead. 1999. Survivable net work system analysis: A case study. IEEE Software 16(4) 70–77.

Fayyad, U., R. Uthurusamy. 1996. Data mining and knowledge discovery in databases. Comm. ACM 39(11) 24–26.

Fidge, C., P. Kearney, M. Utting. 1997. A formal method for building concurrent, real-time software. IEEE Software 14(2) 99–106.

Garg, V. 1997. Methods for observing global properties in distributed systems. IEEE Concurrency 5(4) 69–77.

Gartner, F. 1999. Fundamentals of fault-tolerant distributed computing in asynchronous environments. ACM Comput. Surveys 31(1) 1–26.

Goldstein, R., V. Storey. 1991. The commonsense business reasoner. Proc. 2nd Internat. Conf. Database and Expert Systems Appl. (DEXA). Berlin, Germany, 124–129.

Guttman, M., J. Matthews. 1995. The Object Technology Revolution. John Wiley & Sons, Inc., New York.

Harrison, A. 2000. University computer used in Web attacks. Com puterworld Computerworld, Inc. (February 14).

Hevner, A., D. Berndt. 2000. Eras of business computing. M. Zelkowitz, ed. Advances in Computers, Vol. 52. Academic Press, Ltd.

Imielinski, T., S. Viswanathan, B. Badrinath. 1997. Data on air: Organization and access. IEEE Trans. Knowledge Data Engrg. 9(3) 353–372.

Jakiela, H. 1995. Performance visualization of a distributed system: A case study. IEEE Comput. 28(11) 30–36.

Jiang, Z., L. Kleinrock. 1998. Web prefetching in a mobile environment. IEEE Personal Comm. (October) 25–34.

Jing, J., A. Helal, A. Elmagarmid. 1999. Client-server computing in mobile environments. ACM Comput. Surveys 31(2) 117–157.

Kashyap, V., A. Sheth. 1996. Semantic and schematic similarities between database objects: A context-based approach. VLDB J. 5(4) 276–304.

Kavi, K., J. Browne, A. Tripathi. 1999. Computer systems research: The pressure is on. IEEE Comput. 32(1) 30–39.

Kim, W., J. Seo. 1991. Classifying schematic and data heterogeniety in multidatabase systems. IEEE Comput. 24(12) 12–18.

Kleinrock, L. 1985. Distributed systems. Comm. ACM. 28(11) 1200– 1213.

Krishnamurthi, G., M. Azizoglu, A. Somani. 1998. Optimal location management algorithms for mobile networks. Proc. MOBICOM ’98. Dallas, TX, 223–232.

Liu, L., R. Zicari, W. Hursch, K. Lierberherr. 1997. The role of polymorphic reuse mechanisms in schema evolution in objectoriented databases. IEEE Trans. Knowledge and Data Engrg. 9(1) 50–67.

Madnick, S. 1992. The challenge: To be part of the solution instead of being the problem. Proc. Workshop on Inform. Tech. Systems. Dallas, TX.

March, S., C. Wood, G. Allen. 1999. Research frontiers in object technology. Inform. Systems Frontiers 1(1) 75–94.

Melliar-Smith, P., L. Moser. 1998. Surviving network partitioning. IEEE Comput. 31(3) 62–68.

Peters, R., T. Ozsu. 1997. An axiomatic model for dynamic schema evolution in objectbase systems. ACM Trans. Database Systems. 22(1) 75–114.

Pfleeger, C., D. Cooper. 1997. Security and privacy: Promising ad vances. IEEE Software 14(5) 27–32.

Ra, Y., E. Rudensteiner. 1997. A transparent schema evolution system based on object oriented view technology. IEEE Trans. Data and Knowledge Engrg. 9(4) 600–623.

Ram, S., J. Park, D. Lee. 1999a. Digital libraries in the next millennium: State of the art and research directions. Inform. Systems Frontiers 1(1) 75–94.

———, G. Ball. 1999b. Semantic model support for geographic information systems. IEEE Comput. 32(5) 74–81.

—, K. Kim, Y. Hwang. 1999c. A comprehensive framework for classifying data and schema level semantic conflicts in geographic and non-geographic databases. Proc. Ninth Workshop on Inform. Tech. Systems. 185–190.

, V. Ramesh. 1999. Schema integration: Past, present and future. A. Elmagarmid, M. Rusinkiewicz, and A. Sheth, eds. Management of Heterogeneous and Autonomous Database Systems. Morgan Kaufman, 119–155.

, G. Shankar. 2000. Automating dynamic schema evolution in a heterogeneous database environment: Possibility or a pipe dream? Working paper, Department of MIS, College of BPA, University of Arizona, Tucson, AZ.

Rover, D., A. Waheed, M. Mutka, A. Bakic. 1998. Software tools for complex distributed systems: Toward integrated tool environments. IEEE Concurrency 6(2) 40–54.

Satyanarayanan, M. 1996. Fundamental challenges in mobile com puting. Proc. ACM Sympos. Principles of Distributed Comput. Philadelphia, PA, 1–7.

Sheth, A. 1997. Semantic interoperability in infocosm: Beyond infrastructural and data interoperability in federated information systems. Keynote talk, Internat. Conf. Interoperating Geographic Systems (Interop ’97). Santa Barbara, CA.

—, J. Larson. 1990. Federated database systems for managing distributed, heterogeneous, and autonomous databases. ACM Comput. Surveys 22(3) 184–236.

St. Laurent, S., E. Cerami. 1999. Building XML Applications. McGraw Hill.

Storey, V., R. Goldstein, R. Chiang, D. Dey, S. Sundaresan. 1997. Database design with common sense business reasoning and learning. ACM Trans. Database Systems 22(4) 471–512.

Sullivan, R. L. 1999. Electronic Commerce with EDI. Twain, Inc.

Tsichritzis, D. 1999. Reengineering the university. Comm. ACM 42(6).

Uschold, M. 1996. Ontologies: Principles, methods and applications. Knowledge Engrg. Rev. 11(2) 93–136.

Wang, R., D. Strong. 1996. Beyond accuracy: What data quality means to data consumers. J. Management Inform. Systems (Spring) 5–34.

Weiderhold, G. 1992. Mediators in the architecture of future information systems. IEEE Comput. 25(3) 38–49.

Welling, G., B. Badrinath. 1998. An architecture for exporting environment awareness to mobile computing applications. IEEE Trans. Software Engrg. 24(5) 391–400.

Izak Benbasat, Associate Editor. This paper was received on March 28, 2000, and was with the authors 2 weeks for 1 revision.
