---
otero_id: 21033
otero_key: "YPWZC2F2"
title: "A comprehensive agent-based architecture for intelligent information retrieval in a distributed heterogeneous environment"
authors: "Neal G. Shaw; Ahmad Mian; Surya B. Yadav"
year: "2002"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(01)00128-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A comprehensive agent-based architecture for intelligent information retrieval in a distributed heterogeneous environment

Neal G. Shaw <sup>a,</sup>\*, Ahmad Mian <sup>b</sup>, Surya B. Yadav <sup>c,1</sup>

<sup>a</sup>Department of Information Systems and Management Sciences, College of Business Administration, University of Texas at Arlington, Box 19437, Arlington, TX 76019-0437, USA <sup>b</sup>FILECONTROL.COM, Houston, TX, USA

<sup>c</sup>Area of ISQS, College of Business Administration, Texas Tech University, Lubbock, TX 79409-2101, USA

Received 1 June 1998; received in revised form 1 April 2001; accepted 1 June 2001

## Abstract

The Internet has become the global infrastructure supporting information acquisition and retrieval from many heterogeneous data sources containing high-speed text and rich multimedia images, audio, and video. AgentRAIDER is an ongoing research project at Texas Tech University designed to develop a comprehensive architecture for an intelligent information retrieval system with distributed heterogeneous data sources. The system is designed to support intelligent retrieval and integration of information from the Internet. Current systems of this nature focus only on specific aspects of the distributed heterogeneous problem such as database queries or information filtering. Consequently, these concepts and others have never been successfully integrated into a unified, cohesive architecture. This paper discusses the design and implementation of the AgentRAIDER system and identifies areas for applications of the system in various domains. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Intelligent agents; Information retrieval; Heterogeneous data sources; Distributed decision-making

## 1. Introduction

## 1.1. Background

The Internet has become the global infrastructure supporting information acquisition and retrieval from many heterogeneous data sources containing highspeed text and rich multimedia images, audio, and video. Users attempting to extract valuable information from such a complex environment largely fail, often either because not enough information is available or because of information overload [18]. The amount of information available via the Internet has become too large to be managed by an individual user. System developers must develop information retrieval systems that can assist users in accessing and managing the information base that is the Internet.

When developing such a system, however, many non-trivial issues arise for a system developer. For example:

 How can one system access data from multiple data sources, all of which are different in nature?

 How can a user cope with the tremendous amount of information available?

 Can information agents be used effectively to enhance the user interface, and consequently, user productivity?

Previously, studies have examined various aspects of the information retrieval problem: heterogeneous databases [9,24], information filtering [6,17], information agents [2 – 4,8,14,32,35], distributed systems [1,24], etc. These studies adequately address these issues in an isolated context. Unfortunately, these studies fail to consider two key points: (1) the integration of multiple aspects of the retrieval problem, and (2) the practical application of their solutions. Some researchers have attempted to integrate one or more of these perspectives [13]; however, these integrated approaches have not yet been successfully implemented.

## 1.2. Problem statement

With the wealth of information that is globally distributed via the Internet, a need has arisen for computerized information systems that can retrieve and integrate large amounts of information; however, diverging streams of research in various fields have precluded a truly comprehensive information retrieval system from being developed. Those that have been proposed have been conceptualized with little or no thought to actual development and implementation feasibility, and as a result, no comprehensive system has been actually implemented. These shortcomings, along with the exponential growth of the Internet, indicate the need for a realistic, practical comprehen sive architecture for information retrieval in a distributed heterogeneous environment.

## 1.3. Research objectives

The goal of this research is to develop, design, and implement a comprehensive, integrated intelligent information retrieval system for distributed heterogeneous data sources. The system combines theories and applications from various fields to first develop a comprehensive architecture and then to develop the AgentRAIDER prototype, an implementation of the architecture. The research presented in this paper extends current knowledge in many fields to produce two major contributions to heterogeneous information retrieval:

 the development of a comprehensive architecture for an intelligent information retrieval system for heterogeneous data sources

 the design and implementation of a working prototype of an intelligent retrieval system for heterogeneous data sources.

The paper is organized as follows: Section 2 presents a review of the relevant literature describing previous work in the area of information agents and distributed heterogeneous data sources. Section 3 presents the authors’ comprehensive architecture and some illustrations of its use in various domains. Section 4 describes the AgentRAIDER project, an implementation of the architecture, and shows how it illustrates the development and usefulness of the comprehensive architecture. Section 5 contains a summary of the paper and some directions for future research.

## 2. Current work

## 2.1. Decision support systems

As with most areas of information technology, researchers in decision support systems have recently focused on incorporating the Internet into DSS design [3]; however, the Internet presents problems for DSS design due to the extensive amount of information available from sources which are quite different in nature. Consequently, a number of DSS researchers have independently developed many concepts and components that are necessary for successful integration of decision support systems and the Internet. For example, recent developments include methods for information retrieval [9], Internet searching [12], customized information [26], information filtering [6,17,27], feedback [31], and architectures based upon mediators and facilitators such as intelligent agents [3,10,20].

Each of these recent evolutions in DSS has added to a growing body of knowledge associated with the use of DSS in a distributed, heterogeneous environment such as the Internet. Unfortunately, a comprehensive architecture to integrate these DSS design trends has not yet been presented. Thus, the architecture presented in this paper fills a gap in existing DSS literature by presenting a mediated architecture using intelligent agents that provides support for information retrieval, information filtering, intelligent user feedback and profiling, as well as more traditional components of DSS design. In addition, Agent-RAIDER extends related works in DSS [11,21] by integrating multiple aspects of advanced DSS technology.

## 2.2. Intelligent information agents

The trend in computing is gradually moving toward the notion of agents [2 – 4,8,11,12,14,16,18,21 – 23,28,30,32,34,35], software assistants that help users achieve productivity. Agents have the potential to be extremely useful, especially when they are given ‘‘intelligence.’’ That is, agents can be given the ability to learn user actions and preferences and respond appropriately the next time the user performs a similar action or needs specific preferences. In other words, software agents can have the capability to learn by example [16,28].

Recently, the agency concept has been applied in the area of information retrieval. For example, Yahoo’s MyAgentk and Microsoft’s Agentk have publicized agent-based information retrieval facilities. The drawback to these commercial agents and those proposed in the literature is that they do not integrate the agency concept with other technologies which are needed by the user. Consider a user who wants to retrieve information from a distributed heterogeneous environment such as the Internet. Previously proposed agents can only retrieve the information. They do not have the capability to filter, analyze, or synthesize the information. The agency concept is well-supported both in industry and in academia. The concept simply needs to be extended beyond its traditional boundaries.

## 2.3. Distributed heterogeneous data sources

Distributed heterogeneous data sources are the most complex sources of information. The distributed nature of the data must be addressed with the development of retrieval systems that can access data at multiple locations, and the heterogeneity of the data must be addressed with a system that can access multiple types of data [9]. This complexity has only grown stronger with the growth of the Internet and the resulting global, instantaneous access to text and multimedia data sources.

The concept of distributed heterogeneous information retrieval from databases has been well studied [9,24,29]. The Internet, however, not only consists of multiple databases, but also consists of text, video, audio, images, etc. No comprehensive model for information retrieval under such conditions has been developed. Many companies and researchers have solved individuals parts of the distributed heterogeneous retrieval problem; however, the individual pieces of the solution have never been combined to form an integrated, comprehensive solution.

## 2.4. Digital libraries

As an example of the heterogeneous information problem, consider the case of digital libraries. Digital libraries are heterogeneous public information repositories with a wide variety of internal multimedia information [1]. In addition, these libraries typically contain electronic documents as well as structured and semi-structured databases; however, as Kalakota and Whinston [15] note, the most complex problem associated with digital libraries is a question of how to integrate and assimilate information so that is it easily accessible and relevant to the user. Similarly, Paepcke et al. [25] discuss the difficulty associated with creating interoperable digital libraries. The AgentRAIDER architecture developed in this paper is a possible solution to some of these problems since the intelligent agent concept is well-integrated with existing knowledge of heterogeneous databases, thus creating an architecture that is capable of handling some of the problems presented by digital libraries. Further, AgentRAIDER enhances work investigating methods for locating heterogeneous information in digital libraries [5] by incorporating the use of intelligent user profiling to restrict searches and matching with user requirements. (In the interest of brevity, we have not provided a comprehensive review of digital libraries. For a review of some of the major digital library projects, see Ref. [25]).

3. A comprehensive architecture for an intelligent information retrieval system with distributed heterogeneous data sources

## 3.1. The comprehensive architecture

Since the previous works in the field of information retrieval, information agents, and distributed heterogeneous data sources have never been successfully integrated, we have proposed a comprehensive architecture for the design of an intelligent information retrieval and filtering system (see Fig. 1). The architecture is composed of five agents, data sources, and a user profile base, all of which we shall briefly discuss.

(a) Intelligent User Information Agent (IUIA)—the component of the system that serves as the communication interface between the user and the system.

(b) Query Enhancing Agent (QA)—the component of the system that enhances the user’s query based on the user profile.

![](/api/attachments/YPWZC2F2/fulltext/images/4f25f64dbcefcd09fd290313cfc856686bf8c80a86068001c154e3b6d824c145.jpg)  
Fig. 1. General architecture for an intelligent retrieval system with distributed heterogeneous data sources.

(c) Searching and Routing Agent (SRA)—the component of the system that sends and retrieves information from distributed heterogeneous data sources.

(d) Filtering Agent (FA)—the component of the system that filters the raw data from the Searching and Routing Agent based on the user profile.

(e) Analysis and Synthesis Agent (ASA)—the component of the system that uses the filtered information to enhance decision-making using data mining techniques and the user profile to analyze and synthesize the information retrieved.

(f) User Profile Base (UPB)—a knowledge base of holistic user profiles for all the users of a system; this conceptual profile base can either be distributed across the system or stored in a central location—the holistic user profile consists of a personal profile, a functional area profile, a current project profile, an organizational environment profile, and a client-type profile [27].

(g) Team Members—the IUIA also provides for communication among team members (user nodes); each team member may be equipped with the entire comprehensive system or with only the IUIA.

(h) Structured and Semi-Structured Databases— databases that have some type of structure that can be stored by our system to enhance speed and efficiency of information retrieval from these databases; can be on local or remote nodes.

(i) Unstructured data—represents data that is not in a structured format; typical examples of unstructured data include data from the Internet, i.e. text files, image files, etc.; can be located on local or remote nodes.

Also important to note is the feedback that follows the opposite path as the flow of information. The feedback helps populate the knowledge bases of the system to enhance the learning capabilities of the system.

A more detailed exposition of each agent and its assigned tasks is given in Appendix A. To demonstrate the completeness of our architecture, we have mapped the agent tasks listed in the Intelligent Integration of Information Reference Architecture [13] developed by the Advanced Research Project Agency of the government. This mapping can be found in Appendix B. Only nine tasks remain unassigned to agents in our architecture. At the time of this writing, no other practical architecture has succeeded in addressing such a large number of the ideal reference tasks. Thus, the mapping shows that the proposed architecture is indeed more complete than other projects such as InfoSleuth [22] and TSIMMIS [7].

## 3.2. Sample applications

The following are two sample scenarios for which users might want to make use of the retrieval system. The first scenario is a military application and the second is a typical corporate setting. For each scenario, the flow of information is traced through the various agents in the comprehensive architecture. Note for Scenario 2 that the results would be vastly different depending upon the knowledge bases available to the agents. For a manager in a manufacturing industry, the results would be very different than a user, for example, in the military because the organizational and user knowledge bases would be different. The agents thus have the ability to adapt based upon the context in which they are used. Notice also that the tasks listed to handle the scenarios are designed to follow the conceptual model. In a physical design, each agent would likely spawn multiple smaller agents to accomplish each task.

(1) The user is a military commander who is preparing the logistics for a battle that is likely to be fought near the Black Sea. He needs a detailed account of all battles fought in the area so he can avoid past mistakes and take advantage of past successes. In summary, the user wants a detailed history of all naval battles fought in the Black Sea.

 User tells IUIA ‘‘I want to find all naval battles fought in the Black Sea’’

 IUIA interprets request in the warfare context based upon user profile

 IUIA searches information base for previously gathered information

 IUIA forwards the request to QEA

 QEA finds keywords ‘‘Black Sea,’’ naval, battles

 QEA adds related keywords Navy, history, ships, etc.

 QEA adds keywords based on user profile

 QEA sends keywords to SRA

 SRA searches known databases (military databases, libraries, etc.)

 SRA searches the Internet (text files, WWW, Gopher, etc.)

 SRA notifies QEA if there is insufficient data and QEA revises query

 SRA sends aggregate search results to FA

 FA removes irrelevant data based on user profile, i.e. battles not fought in the Black Sea, non-naval battles fought in the Black Sea, etc.

 FA notifies SRA if insufficient data remains

 FA forwards filtered data to ASA

 ASA analyzes data and reports, for example, statistics on battles in the Black Sea, trends, etc.

 ASA gives feedback to FA

 ASA sends all information to IUIA

 IUIA stores information in information base

 IUIA reports information to the user

 IUIA asks user for feedback

 IUIA reports to ASA on the usefulness of the information

 All agents update local knowledge bases and user profile based upon the usefulness of the information to the user.

(2) The user is a purchasing manager. An actual inventory of items on hand shows substantially different amounts of several items than computer records suggest. The manager wants to search all available databases for all transactions involving the missing items. Once the transactions have been traced, he wants to order items from vendors to replace the missing items. In addition, he would like comparative data from other companies in his industry.

 User asks IUIA to ‘‘find inventory, prices, etc. for widgets, plugs, and grinders’’

 IUIA interprets request in purchasing context

 IUIA searches information base for previously gathered information

 IUIA forwards the request to QEA

 QEA finds keywords ‘‘inventory,’’ ‘‘prices,’’ ‘‘widgets,’’ ‘‘plugs,’’ ‘‘grinders’’

 QEA adds related keywords ‘‘amount,’’ ‘‘items,’’ etc.

 QEA adds keywords based on user profile

 QEA adds keywords for competitor information based on organizational knowledge

 QEA sends keywords to SRA

 SRA searches known databases (inventory databases, libraries, etc.)

 SRA searches the Internet (text files, WWW, Gopher, etc.)

 SRA notifies QEA if there is insufficient data and QEA revises query

 SRA sends aggregate search results to FA

 FA removes irrelevant data based on user profile

 FA notifies SRA if insufficient data remains

 FA forwards filtered data to ASA

 ASA analyzes data and reports, for example, comparisons with other companies in the industry, trends, etc.

 ASA gives feedback to FA

 ASA sends all information to IUIA

 User rates information on timeliness, accuracy, usefulness, etc.

 IUIA reports to ASA on the usefulness of the information

 All agents update local knowledge bases and user profile based upon the usefulness of the information to the user.

## 3.3. A model of the intelligent user information agent

With the exception of the Intelligent User Interface Agent, the majority of the functionality needed for the proposed architecture has already been developed either by academia or by industry. In consequence, our design efforts have concentrated on the intelligent user information agent (IUIA) of the comprehensive architecture that we have proposed. The following paragraphs explain the functions of the IUIA so that designers and programmers may independently develop customized IUIAs or other modules that will interface with an IUIA. This agent will serve as the interface between the user and the information retrieval subsystem. The IUIA will serve three primary functions:

 to provide an interface for communication between the user and other team members

 to interact with the Query Enhancing Agent and the Analysis and Synthesis Agent to support users in various functions throughout the system

 to provide a means for the user to give feedback in order for the system to learn and enhance the capabilities of the system.

The IUIA should be designed to have an intuitive, easy to use graphical interface. Functionality will be included that allows the user to communicate directly with a team member while the agent is simultaneously sending and receiving requests for vital information. A general architecture of the IUIA follows in Fig. 2. The IUIA consists of eight parts, as can be seen in the figure.

 User Interface Subsystem—subsystem responsible for interfacing with the user, specifically, handling user input and providing output to the user

 Feedback Subsystem—subsystem for processing user feedback in order to learn and enhance the knowledge bases of the system

 Information Processing Subsystem—subsystem designed to process the information coming in from the Analysis and Synthesis Agent

 Query Processing Subsystem—subsystem responsible for directing user queries to the Query Enhancing Agent

 User Communication Subsystem—subsystem responsible for the communication between the user and other team members

 User Profile Base—the holistic user profile base defined in the comprehensive architecture above

 User Knowledge—a knowledge base about the user’s personal interface preferences

 Organizational Knowledge—a knowledge base about the organization, i.e. structure, organizational chart, etc.

## 4. AgentRAIDER

Agent for Retrieval and Analysis of Information in Distributed Environments (AgentRAIDER) is the result of an ongoing research investigation at Texas Tech University into the intelligent retrieval of information from distributed heterogeneous environments. Agent-RAIDER is a prototype system based on the comprehensive architecture proposed in this paper. Agent-RAIDER is an implementation of the Intelligent User Information Agent (IUIA). Together with commercially available implementations of the other components, it demonstrates the feasibility of the architecture for organizations to use as a solution to information retrieval problems. The following sections discuss the design and implementation of AgentRAIDER.

## 4.1. Design issues

When the authors began to develop an actual system design for the comprehensive architecture, the first decision that had to be made was the classic decision of ‘‘build vs. buy’’ [33] in information systems. After analyzing the offerings by various companies, it was decided that the only component of the architecture that would need to be built was the Intelligent User Information Agent (IUIA). The commercial components require slight alteration for interface purposes, but by and large, the technologies are available. For example, IBM offers data mining solutions, and Internet search services have developed query augmenters. Multiple companies and researchers have developed searching and routing mechanisms, and information filtering tools are available both commercially and without charge on the Internet. In contrast, the IUIA is a unique component which has never before been implemented. So the final decision was made to implement only the IUIA. This significantly enhances the potential of the architecture because any company (or any person) can easily develop a customized implementation of the architecture by customizing or developing an IUIA.

![](/api/attachments/YPWZC2F2/fulltext/images/4985a66e5eff857b33aa5672d4234e18819115bebcac13f3fc4641b0b40cf11a.jpg)  
Fig. 2. Architecture of an Intelligent User Information Agent (IUIA).

![](/api/attachments/YPWZC2F2/fulltext/images/a6e527e10db2019e0f8396b0fd1acac196433f629f433088ed3990f7abfc4150.jpg)  
Fig. 3. AgentRAIDER system architecture.

![](/api/attachments/YPWZC2F2/fulltext/images/7c37eb701b5934f92adc27efc04c4c34d448fe12e1a16e341ba1f02eeed6fbaf.jpg)  
Fig. 4. AgentRAIDER main screen

We designed our version of the IUIA with two high level design goals:

Modularity—the IUIA should be independent of all other modules in the architecture and should have a well-defined communication interface (the KQML agent communication language).

 Scalability—the system should allow for incremental or major upgrades as technology and throughput change.

## 4.2. Novel aspects of the design

The primary contribution of the AgentRAIDER project is the conceptual development of an architecture for the intelligent retrieval of distributed heterogeneous information; however, the design of the AgentRAIDER prototype also presents some novel techniques, which are of interest to the DSS design community. Specifically, the following characteristics of the design are features of AgentRAIDER, which present new and/or improved aspects of the design:

![](/api/attachments/YPWZC2F2/fulltext/images/975672afee230f775f0099d70e3299c53c8b6685c2eaa62a24936746d8070769.jpg)  
Fig. 5. AgentRAIDER main screen menu options.

![](/api/attachments/YPWZC2F2/fulltext/images/30abf3f18155409cf7de43f13ddd0bda9854a254e23ef0618b1089187171b6d5.jpg)  
Fig. 6. Sample AgentRAIDER retrieval screen.

 Intelligent user profiling—AgentRAIDER develops user profiles based upon an intelligent feedback system [27]. This design is more advanced than systems which rely on profiles constructed solely based upon an initial user input. Although the basic approach of adaptable agents based upon profiling has been used previously, the AgentRAIDER prototype accepts feedback throughout multiple stages of the information retrieval process to simulate a continuous feedback system instead of accepting feedback only at a few discrete intervals. Further, the system is able to adapt its behavior based upon the user feedback received at multiple points, and thus, the prototype is able to adapt to future user queries based upon the contents of a dynamically updated profile.

 Standardized agent-based communication—The AgentRAIDER prototype uses standardized agent communication based upon the KQML agent communication language. The application and use of this language in a mediated architecture allows for external interfaces which allow easy adaptation and modification of the proposed system. Architectures emphasizing proprietary communication languages and interfaces limit the utility and expandability of agentbased communication systems, but AgentRAIDER is not subject to those limitations. Although other agentbased systems have used the KQML language, the AgentRAIDER prototype is unique in its use of KQML because in addition to the feedback loop described above, it allows for the connection of unknown external agents as well as third-party search tools, which can incorporate the KQML language.

![](/api/attachments/YPWZC2F2/fulltext/images/31d4802c1f7df74cd1c32a8ff003388255411e770645e400503796f3c88ff7cf.jpg)  
Fig. 7. Sample AgentRAIDER feedback screen.

 Incorporation of existing technology—AgentRAIDER was designed to allow for the inclusion of readily available technology such as Internet search engines, query augmenters, and data mining tools. The prototype is designed specifically to support reuse of these and other technologies to ease implementation and support of AgentRAIDER systems.

 Facilitation of heterogeneous data access—The design of AgentRAIDER provides for interfaces with multiple types of information systems, including webbased search engines, text-based databases, data warehouses, etc. Thus, based upon user entries, as well as its internal knowledge bases, AgentRAIDER can access multiple heterogeneous data sources. This characteristic is a particularly important one in the areas of information systems and decision support systems given the relative absence of research in the area [19].

## 4.3. The AgentRAIDER prototype

The agent implementations and the knowledge base representations are the most critical components of the prototype since those components are the implementations of the key characteristics that distinguish the AgentRAIDER architecture from other projects. The remainder of the prototype development is a fairly standard implementation using the Java programming language for network communications and using a number of Visual Basic components to develop the user interface. Fig. 3 shows the system architecture of the AgentRAIDER prototype. Notice that the main program driver is indeed the IUIA, as discussed previously in this paper. The various IUIA subsystems are shown as functions that can be called as needed. First, the user is presented with a screen in which a request can be entered. This initial screen is shown in Fig. 4, and the menu options available on this screen are shown in Fig. 5. As the query is processed, and information is retrieved, the user is presented with a concept/URL screen showing some of the raw information retrieved from the Internet, in this case. Fig. 6 shows an example of such a screen. Finally, Fig. 7 shows one user feedback screen which can be used to rate information on its relevance to the user’s query.

There are a number of additional screens for feedback, results, etc., that are not presented here.

## 5. Conclusions and future research

## 5.1. Summary

This paper has presented a comprehensive architecture for intelligent information retrieval in a distributed heterogeneous environment. Theories and methods have been borrowed from multiple disciplines to produce a cohesive, integrated architecture. The architecture represents a significant contribution to knowledge in many fields such as information retrieval and information systems because it represents the first information retrieval architecture from which actual systems can be built.

To illustrate the feasibility of implementing a system based upon the architecture, we have profiled the AgentRAIDER project at Texas Tech University. AgentRAIDER demonstrates that the architecture is modular, flexible, and scaleable. The major technologies needed to implement AgentRAIDER are available either commercially or via the Internet. Thus, organizations and end users all have the capability to assemble an information retrieval system based upon the comprehensive architecture proposed by the authors. The architecture is truly universal.

## 5.2. Future research

The comprehensive architecture represents a significant advancement in the field of information retrieval. Also, as the Internet continues to grow, developers and researchers alike can make use of the architecture to design and evaluate systems. Still, much work remains to be done in this area. Three areas of research that we intend to pursue to extend the architecture are the following:

 to demonstrate the feasibility of the system in a collaborative decision-making environment

 to perform benchmark tests of the system using the Internet

 to complete the functionality of the prototype system using the latest developments in methodology and technology.

## Appendix A. List of agent tasks

Intelligent User Information Agent (IUIA)

 act as the user interface (I/O)

 apply knowledge from essential knowledge base and local knowledge base

 interpret context of user requests

A. ask user for confirmation

B. update knowledge base and user profile

 compare request with information base (Information Management Agent)

 forward user requests to the Query Enhancing Agent

 present a graphical user interface

 accept user input in structured or unstructured format

 receive data from Analysis and Synthesis Agent

 return data in an organized, useable format specified by user profile

 accept user feedback on usefulness, timeliness, etc. of information

 send feedback to the Analysis and Synthesis Agent

A. feedback should reflect the usefulness, timeliness, etc. of the information

B. suggest methods of improvement to ASA

 update local knowledge base, if necessary

 conform to standards of ARPA Knowledge Sharing Effort.

## Query Enhancing Agent (QEA)

 accept user request from IUIA

 parse user request for keywords

 apply knowledge from essential knowledge base and local knowledge base

 add or replace keywords using user profile

 forward refined query to Searching and Routing Agent

 accept feedback and add or replace keywords as necessary

 send feedback to IUIA

A. did IUIA send enough information? B. was a viable query formed?

 update local knowledge base, if necessary

 conform to standards of ARPA Knowledge Sharing Effort.

## Searching and Routing Agent (SRA)

 accept refined query from QEA

 connect to local and remote knowledge bases

 apply knowledge from essential knowledge base and local knowledge base

 search structured databases based on the knowledge bases

 search unstructured data, i.e. the Internet, using existing search tools

 forward all data to the Filtering Agent

 accept feedback and repeat search using different sources, etc. if necessary

 send feedback to QEA about effectiveness of query

A. how much information was returned?

B. was it relevant?

 update local knowledge base, if necessary

 conform to standards of ARPA Knowledge Sharing Effort.

## Filtering Agent (FA)

 accept raw data stream from SRA

 remove data that is irrelevant based on the user profile

 apply knowledge from essential knowledge base and local knowledge base

 forward useful data to the Analysis and Synthesis Agent

 accept feedback and permit more/less data to pass if necessary

 send feedback to SRA about data sent

A. was data relevant?

B. is more information needed?

C. does the information fit the user profile?

 update local knowledge base, if necessary  conform to standards of ARPA Knowledge Sharing Effort.

Analysis and Synthesis Agent (ASA)

 accept filtered data stream from FA

 analyze the data stream (data mining etc.) based on user profile

 apply knowledge from essential knowledge base and local knowledge base

 supplement raw data with any useful information from the analysis

 forward information to IUIA

 accept feedback from IUIA (user) about quality of information

 send feedback to FA about the effectiveness of the filter

A. was information useful?

B. could useful information be synthesized?

C. were any critical parts missing?

 update local knowledge base, if necessary.

 S.1.a: Ontology and Vocabulary Transformation Services.

## SRA

 C.5: Resource Discovery Services

 C.6.b: Tool and Information Source Selection

 S.4: Physical Integration Support Services

 S.5: Component Programming Services

 S.3.f: Heterogeneous Transactions

 S.1.d: Information Source Library.

## FA

## ASA

 S.2.a: Data Restructuring

 S.2.d: Context Transformation

 S.3.b: Result Integration

 S.2.b: Abstraction and Aggregation

 F.2: Inference Services.

User Profile

## Appendix B. Comparison of tasks with $\mathbf { I } ^ { 3 }$ reference architecture [13]

## IUIA

 C.1: Dynamic Tool Selection and Invocation

 C.2: Dynamic Configuration Construction

 C.3: Static Configuration Construction

 C.4: Ad Hoc Configuration Construction

 C.6.a: Service Selection

 C.6.c: Template Construction

 C.6.d: Process Control

 C.7.b: Process Scheduling

 C.7.c: Data and process Management

 S.3.c: Collaboration

 S.3.e: Consistency Management

 S.1.c: View Integration

 S.1.b: View Transformation.

## QEA

 C.7.a: Parsing

 S.3.a: Query Decomposition

. S.3.g: Behavioral Import.

## Unmatched

 W: Wrapping Services

 S.2.c: Object Correspondence

 S.2.e: Standards Development and Support Services

 S.3.d: Distributed Update Generation

 F.1: Active Services

 F.3: Multistate Services

 F.4: Temporal Services

 F.5: Object-Orientation Services

 F.6: Persistence Services.

## References

[1] P.A. Bernstein, A model for distributed system services, Communications of the ACM 39 (2) (Feb. 1996) 86–98.

[2] H.K. Bhargava, W.C.J. Branley, Simulating belief systems of autonomous agents, Decision Support Systems 14 (1995) 329– 348.

[3] T. Bui, J. Lee, An agent-based framework for building decision support systems, Decision Support Systems 25 (1999) 225– 237.

[4] D.G. Conway, G.J. Koehler, Interface agents: caveat mercator in electronic commerce, Decision Support Systems 27 (2000) 355– 366.

[5] R. Dolin, D. Agrawal, A. El Abbadi, L. Dillon, Pharos: a scalable distributed architecture for locating heterogenous information sources, Proc. Conference on Information and Knowledge Management (CIKM), Las Vegas, NV, 1997.

[6] P.W. Foltz, S.T. Dumais, Personalized information delivery: an analysis of information filtering methods, Communications of the ACM 35 (12) (Dec. 1992) 51– 60.

[7] H. Garcia-Molina, J. Hammer, K. Ireland, Y. Papakonstantinou, J. Ullman, J. Widom, Integrating and accessing heterogeneous information sources in TSIMMIS, Proceedings of the AAAI Symposium on Information Gathering, Stanford, CA, AAAI Press/MIT Press, Menlo Park, CA, USA, 1995, pp. 61– 64.

[8] M.R. Genesereth, S.P. Ketchpel, Software agents, Communications of the ACM 37 (7) (July 1994) 48 – 53.

[9] R. Giladi, P. Shoval, An architecture of an intelligent system for routing user requests in a network of heterogeneous databases, Journal of Intelligent Information Systems 3 (1994) 205– 219.

[10] M. Goul, A. Philippakis, M.Y. Kiang, D. Fernandes, R. Otondo, Requirements for the design of a protocol suite to automate DSS deployment on the World Wide Web: a client/server approach, Decision Support Systems 19 (1997) 151–170.

[11] T.J. Hess, L.P. Rees, T.R. Rakes, Using autonomous software agents to create the next generation of decision support systems, Decision Sciences 31 (1) (Winter 2000) 1 – 31.

[12] C. Hsinchun, C. Yi-Ming, M. Ramsey, C.C. Yang, An intelligent personal spider (agent) for dynamic Internet/Intranet searching, Decision Support Systems 23 (1998) 41– 58.

[13] R. Hull, R. King, Y. Arens, M. Siegel, H. Garcia-Molina, M. Genesereth, A. Goldschmidt, L. Kerschberg, N. Singh, C. Thompson. Reference Architecture for the Intelligent Integration of Information, Program on Intelligent Integration of Information (I<sup>3</sup>)—Advanced Research Projects Agency, May 19, 1995.

[14] A. Joshi, M.P. Singh, Multiagent systems on the net, Communications of the ACM 42 (3) (March 1999) 39– 40.

[15] R. Kalakota, A.B. Whinston, Frontiers of Electronic Commerce, Addison-Wesley, New York, 1996.

[16] H. Lieberman, D. Maulsby, Instructible agents: software that just keeps getting better, IBM Systems Journal 35 (3/4) (1996) 539– 556.

[17] S. Loeb, D. Terry, Information filtering, Communications of the ACM 35 (12) (Dec. 1992) 26– 28.

[18] P. Maes, Agents that reduce work and information overload, Communications of the ACM 37 (7) (July 1994) 31 – 40.

[19] S. March, A. Hevner, S. Ram, Research commentary: an agenda for information technology research in heterogeneous and distributed environments, Information Systems Research 11 (4) (December 2000) 327– 341.

[20] F.P. Maturana, D.H. Norrie, Distributed decision-making using the contract net within a mediator architecture, Decision Support Systems 20 (1997) 53–64.

[21] A. Montazemi, K. Gupta, On the effectiveness of cognitive

feedback from an interface agent, Omega 25 (6) (1997) 643– 658.

[22] M.P. Singh, A. Rao, M.J. Wooldridge, M. Nodine, A. Unruh, Facilitating open communication in agent systems: the Info-Sleuth infrastructure, Intelligent Agents IV—Agent Theories, Architectures, and Languages: Proceedings of the Fourth International Workshop (ATAL ’97, Providence, RI), Springer-Verlag, Berlin, Germany, 1997, pp. 281 – 295.

[23] T.A. Ottaway, J.R. Burns, Adaptive, agile approaches to organizational architecture using agent technology, Decision Sciences 28 (3) (Summer 1997) 483–511.

[24] M.T. Ozsu, P. Valduriez, Principles of Distributed Database Systems, Prentice-Hall, Paris, 1991.

[25] A. Paepcke, C.-C.K. Chang, H. Garcia-Molina, T. Winograd, Interoperability for digital libraries worldwide, Communications of the ACM 41 (4) (April 1998) 33– 42.

[26] A. Palma-dos-Reis, F.M. Zahedi, Designing personalized intelligent financial decision support systems, Decision Support Systems 26 (1999) 31–47.

[27] K. Parker, A Holistic Profile for Information Filtering Systems, Texas Tech University, 1995, unpublished Ph.d dissertation, Texas Tech. University, Lubbock, TX.

[28] T. Selker, Coach: a teaching agent that learns, Communications of the ACM 37 (7) (July 1994) 92 – 99.

[29] M.-C. Shan, R. Ahmed, J. Davis, W. Du, W. Kent, Pegasus: a heterogeneous information management system, in: W. Kim (Ed.), Modern Database Systems: The Object Model, Interoperability, and Beyond, ACM Press, New York, 1995, pp. 664– 682.

[30] Singapore Information Technology Institute, iAgent: Technical Descriptions, 1997.

[31] R. Vahidov, R. Elrod, Incorporating critique and argumentation in DSS, Decision Support Systems 26 (1999) 249– 258.

[32] N. Vulkan, Economic implications of agent technology and Ecommerce, The Economic Journal 109 (February 1999) F67 – F90.

[33] J.L. Whitten, L.D. Bentley, V.M. Barlow, Systems Analysis and Design Methods, 3rd edn., IRWIN, Boston, MA, 1994.

[34] S.B. Yadav, N.G. Shaw. A white paper on an intelligent agent for information retrieval from distributed heterogeneous data sources. Texas Tech University, 1997.

[35] C.C. Yang, J. Yen, H. Chen, Intelligent Internet searching agent based on hybrid simulated annealing, Decision Support Systems 28 (2000) 269 – 277.

Neal G. Shaw is currently an assistant professor in the Department of Information Systems and Operations Management in the College of Business Administration at the University of Texas at Arlington, where he has been since receiving his doctoral degree in information systems from Texas Tech University. Dr. Shaw has received research grants from NASA and published his findings in major national and international conferences along with such journals as IEEE Transactions on Software Engineering. His current research interests include IT implementation and the use of IT in supply chain management.

Ahmad Mian is the founder, President and Chief Technology Officer of FileControl, based in Houston, TX. Previously, he was the Vice President and CTO at Underwriters Indemnity Group. Mr. Mian has developed enterprise-wide technology solutions for Fortune 500 companies such as NewYork Life, Exxon, and Shell. He holds degrees in Electrical Engineering, Physics and Mathematics and an MBA from Texas Tech University. Additionally, Mr. Mian has attained advanced executive education from the Massachusetts Institute of Technology—Sloan School of Management.

Dr. Surya B. Yadav is the James and Elizabeth Sowell Professor of Telecom Technology and the head of the ISQS department. He has over 16 years of teaching, research, and systems development experience in the area of information systems. He received his B.S.E.E. degree in electrical engineering from Banaras University, M.Tech. Degree in computer science from I.I.T. Kanpur, India, Masters of Business Information Systems, and PhD degree in business information systems from Georgia State University. His research interests include research methodology, adaptive systems, and electronic commerce. He has published in several journals including Communications of the ACM, IEEE Trans. on Software Engineering, IEEE Trans. on Systems, Man, and Cybernetics, Decision Support Systems, and Journal Management Information Systems.
