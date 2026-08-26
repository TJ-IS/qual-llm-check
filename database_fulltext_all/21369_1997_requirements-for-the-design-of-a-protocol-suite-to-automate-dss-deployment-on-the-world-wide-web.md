---
otero_id: 21369
otero_key: "A7V5A2XH"
title: "Requirements for the design of a protocol suite to automate DSS deployment on the World Wide Web: A client/ server approach"
authors: "M. Goul; A. Philippakis; M.Y. Kiang; D. Fernandes; R. Otondo"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)00054-1"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Requirements for the design of a protocol suite to automate DSS deployment on the World Wide Web: A client/server approach

M. Goul $^{*}$ , A. Philippakis, M.Y. Kiang, D. Fernandes, R. Otondo

Computer Information Systems Area, School of Accountancy, College of Business, Arizona State University, Tempe, AZ 85287-3606, USA

Received 1 December 1995; revised 3 April 1996; accepted 15 August 1996

## Abstract

The purpose of this paper is to propose and justify requirements for the design of a protocol suite for deploying and sharing Specific DSSs both within and across organizations by utilizing the World Wide Web (WWW) infrastructure and a client/server decomposition model. At the heart of the model proposed for the protocol suite is an approach for inter-agent communication as adapted from the distributed artificial intelligence literature. A modularized layered approach to protocol specification, and three sample client interfaces derived from the protocol are presented. Our approach is contrasted to alternative schemes for decision model access across wide area networks.

Keywords: Decision support system; Internet protocol; Distributed artificial intelligence

## 1. Introduction

Modern organizations are undergoing significant transformations leading to major restructuring initiatives resulting in the elimination of entire middle management layers $[18,19]$ . The elimination of middle management layers has a direct bearing on DSS research conducted under the rubric of traditional DSS assumptions emphasizing the differences between DSS research and EDP/MIS research. For example, many organizations' Business Process Reengineering (BPR) efforts have been designed to 'empower' line personnel decision making $[17,19]$ , but line personnel have not typically been the traditional end-user audience for many of the research-oriented Specific DSSs (the term 'Specific DSS' is adapted from the compendium [38]). Today's line personnel do not have the budgets to devote to specialized and customized DSS design and development, nor do they have the level of training traditionally assumed in Specific DSSs equipped with sophisticated statistical and/or optimization solvers and associated end-user interfaces. For example, a recent Wall Street Journal article on BPR describes an emerging and ongoing problem:

“Managers and newly ‘empowered’ employees may feel crushed by constant pressure to work faster... [at Gillette’s Designs Labs] in early installations of new machines to produce redesigned razors, engineers found that they had ratcheted up the level of technology so much that the operators needed more training. When the sophisticated machines provided reports on quality and production rates, the operators didn't understand the implications and adjust the equipment. Now, Gillette is running remedial education in advance of bringing in the equipment" [37].

Information Systems (IS) departments in modern organizations are also undergoing significant change. Some IS departments are being distributed into functional areas, and many face increasing outsourcing competition from a growing sector of global consulting firms, including the development of Specific DSSs. The DSS research community can serve either as inhibitors or facilitators of DSS outsourcing. Our view is that the DSS research community should be among the leaders in facilitating outsourcing. For this reason and others, we argue for a new perspective to DSS deployment.

Additional trends suggestive of the need for a new perspective to DSS deployment include technological advancements in the reference disciplines of DSS research including: End-User-Interfaces (EUI), Database Management Systems (DBMS), Model Management Systems (MMS), and Artificial Intelligence (AI). The availability of high-level Graphical User Interface (GUI) development tools has made organizations accustomed to rapid application development, e.g., what is referred to as 'middle-out design' in the traditional DSS literature [24]. In addition, World Wide Web's (WWW) hypertext orientation has enabled a standardized 'look and feel' to interfaces for navigating the Internet. The use of the WWW as a distribution system is further facilitated by the fact that Web browsers are available for all the major computing platforms and installation of Web browsers at client sites is relatively easy [13]. The resulting dramatic growth of the WWW offers a global infrastructure for DSS service and product distribution. Advancements in the DBMS area have provided new insights for incorporating complex objects, including multimedia, into distributed object-oriented database systems that are naturally integrated with near-horizon distributed object-oriented operating systems (e.g., [32]).

These technological advancements imply that traditional DSS research perspectives, specifically those with respect to linkages between the DBMS and MMS components of a DSS, need to be expanded (e.g., [10]). Finally, with respect to AI, the DSS research community has recently formalized an organizational perspective [16]. As AI becomes more integrated into the reference disciplines of DSS, the impact of AI on DSS will be more pervasive. Additionally, recent work in distributed AI, particularly in the area of intelligent agents, is now attracting more research activity across many computer-related research streams [26,30,41].

Given the environment described above, today's DSS research community is somewhat fragmented. Such differentiation of effort can only serve to reduce the impact of the DSS research community. Modern technology-based industries have been forged by organizations that have been willing to adopt industry-wide, open systems protocol suites in order to advance the competitive positions of all organizations within an industry. We believe DSS researchers whose interests lie in Specific DSS research streams should similarly consider their respective research interests in order to imitate this type of collective industry-level strategy in the form of an Open-DSS protocol suite.

The purpose of this paper is to offer a starting point for developing an agreed-upon protocol suite for an Open-DSS deployment strategy that relies on the emerging World Wide Web inter-networking infrastructure. This paper is organized as follows. First, we define DSS deployment, and we argue for a particular Open-DSS perspective as based on changing the historical perspective to DSS deployment. Next, we discuss related work in the areas of intelligent network search, client/server computing, distributed artificial intelligence, object-oriented modeling, and model management systems, all under the auspices of forging a new Open-DSS deployment strategy. In the context of this discussion, we develop requirements and suggest specifications for a DSS deployment protocol suite. We conclude with a discussion of the limitations and benefits of the requirements proposed.

## 2. DSS deployment: Towards a new perspective

In this section, we state a working definition of DSS deployment, and we discuss relevant DSS research in order to lay the foundation for specifying a set of requirements for an Open-DSS deployment protocol suite. We begin with a working definition abstracted from traditional DSS literature (e.g., [2,6,8,20,28,36]), and as presented from an end-user's perspective.

DSS deployment involves:

(1) The discovery of opportunities for utilizing new Specific DSS applications intended to improve decision making and problem solving by individuals, groups, and organizations;

(2) The design, development, and validation of relevant, customized DSSs;

(3) The delivery of relevant and customized DSSs to individuals, groups, or organizations targeted in (1), above;

(4) The training of individuals, groups, and organizations for relevant and customized DSSs delivered as per (3), above;

(5) Discretionary utilization by individuals, groups, and organizations of DSSs delivered in (3), above, with training as provided in (4), above; and

(6) The collection of DSS outcome measures to be used as feedback for continuously improving each Specific DSS.

This working definition includes a discovery phase, a construction phase, a delivery phase, a training phase, a utilization phase, and a continuous improvement feedback loop. The concept of an Open-DSS deployment strategy can be examined from the standpoint of designing new improvement-oriented interventions for individual phases, for groups of phases, or for the ordering of phases. By defining a plausible intervention strategy relevant to this DSS deployment definition, we lay the foundation for defining a set of requirements for an Open-DSS protocol suite.

## 2.1. Intervention strategy

In the discovery phase of DSS deployment, traditional DSS literature often presumes that an organization's IS department's DSS group is charged with the responsibility for searching the organizational environment for opportunities to deploy high-impact DSSs. In reality, DSS deployment has been championed by high-level functional area managers who had the authority and budgets to bring about the creation of DSSs to reinforce the historical control points of their functional areas in organizations. Modern organizational practices such as BPR, have significant implications for the discovery phase of DSS deployment. The new end-users of DSSs are empowered line personnel who are charged to focus on continuous improvement to fundamental business processes. In order to deploy DSSs to empowered line personnel, those employees need new infrastructure support to discover and begin utilizing DSSs in a manner independent of a centralized IS department. Empowered line employees represent the target audience for a new DSS deployment philosophy. For instance, they are rewarded through team-oriented incentive programs and they do not have the skills and knowledge associated with traditional middle level managers. For the most part, empowered line personnel have experience with computers, but do not possess the same training as middle level managers who were the target audience for traditional DSS research.

Given that the majority of the DSS end-user audience in organizations is shifting to empowered line personnel aligned around fundamental business processes, there is a need for an alternative DSS deployment model that can be addressed by an Open-DSS protocol suite. Our approach is to suggest modifications to the deployment model discussed above as follows (note: this model is again stated from an end-user's perspective).

DSS deployment involves:

(0) The design, development, and validation of Open-DSS protocol suite compliant Specific DSSs by commercial and academic entities whereby those Specific DSSs are accessible to end-users through the WWW;

(1) The discovery of Specific DSSs on the WWW through end-user supported search in order that Specific DSSs can be utilized to improve decision making, problem solving, and end-user learning for individuals, groups, and organizations;

(2) The delivery of relevant DSSs to individuals, groups, or organizations who choose Specific DSSs discovered in (1), above;

(3) The training of individuals, groups, and organizations for relevant and customizable DSSs delivered as per (2), above;

(4) Discretionary utilization by individuals, groups, and organizations of Specific DSSs delivered in (2), above, with training as provided in (3), above; (5) The collection of DSS outcome measures to be used as feedback for continuously improving each application of a Specific DSS as matched to an individual's, group's, or organization's needs; and (6) The ongoing development of standards for Specific DSSs accessible through the WWW.

## 2.2. Implications of the intervention strategy and the new model of DSS deployment

This new definition of DSS deployment suggests DSSs will be developed on the WWW in the initial step of DSS development processes, and this is drastically different than the approach taken in traditional DSS development processes. In many ways this step is already occurring, but it is occurring as the first wave of organizations are creating WWW home pages describing their products and services. It is only a matter of time before vendors of Specific DSSs utilize the WWW on a wider scale. For example, J.P. Morgan and Co. already has WWW pages, both text-based and hypertext, that describe Specific DSSs under a product category called RiskMetrics™ [22]. RiskMetrics™ includes daily market data, a methodology for analyzing the data, and associated documentation (we assume this documentation includes training materials). The WWW pages describing RiskMetrics™ include protocols on “Structure of the RiskMetrics™ data files”, assume Netscape as the typical end-user WWW browser, and discuss data file downloading for a variety of hardware/software platform configurations. It is important to note that J.P. Morgan and Co.’s RiskMetrics™ product suite is based on a methodology that is used by the company, but differs from the in-house systems used by the company. This is apparent in the disclosure statement included in their WWW pages [22].

Already, users of Internet browsers can discover Specific DSSs, such as RiskMetrics™, that address their individual needs, the needs of their team, and/or the needs of their organization. However, current Internet browsers do not have the ability to conduct intelligent searches for Specific DSSs in isolation of an end-user who is busy with line responsibilities. This inability exists because there is no common framework for intelligent Specific DSS search, or what we have referred to as an Open-DSS protocol suite. With an agreed-upon Open-DSS protocol suite, there is opportunity to develop the types of browsers end-users need in order to be led to Specific DSSs. In addition, the realization of an Open-DSS protocol suite can help to bring about standards. Such standards will be important for guaranteeing the integrity of Specific DSSs and would also help to realize a high level of service.

## 2.3. Distributed artificial intelligence as a foundation for an Open-DSS protocol suite

The relevant metaphor for our approach to the definition of requirements for an Open-DSS protocol suite is derived from the distributed artificial intelligence (DAI) literature base. At the heart of most DAI paradigms, “agents” are computer-based abstractions for the processes that communicate and coordinate in the solving of problems. This agent-based paradigm is the natural extension of centralized to distributed computing. In addition, agents, in a DSS research context, represent the mechanism for both deploying and discovering Specific DSSs. Coordination and communication between agents is an area where multiple research ideas have been investigated. The objective of agent coordination is to ensure that an agent reasons about its own actions and those of other agents in the system in a manner that ensures the agents in the system act in a coherent and efficient manner. More specifically, there are three reasons why actions of agents in the DAI context need to be coordinated [21]:

1. There are dependencies between the agents' actions in the system.

2. There are global system constraints to be achieved.

3. No single agent has sufficient competence, resources, or information to solve the system.

Two different approaches have been explored in relation to agent communication paradigms. These are direct agent communication, in which the agents handle their own coordination, and assisted agent communication, in which agents use special system programs to achieve coordination. The advantage of direct communication is that it is independent of features or biases of any other programs. Two widely used architectures for direct communication are the contract-net approach and the specification sharing approach.

In the contract net approach [33], agents in need of services distribute requests for proposals to other agents. The recipients of these messages evaluate those requests and submit bids to the originating agents. The originators use these bids to decide which agents to assign tasks and then award contracts to those agents. A five stage snap-shot view of the contract net approach over the Web, resulting in the establishment of a contract, is outlined in Fig. 1. The communication intensive nature of the contract net approach is highlighted by Fig. 1.

In the specification sharing approach to coordination, agents supply other agents with information about their capabilities and needs. This information is used by the agents to coordinate their activities.

The specification sharing approach is often more efficient than the contract net approach because it decreases the amount of communication that must take place.

As long as the number of agents in either the contract net approach or the specification sharing approach is small, communication cost is not an important factor. But in an environment like the Internet, with millions of programs, the cost of broadcasting bids or specifications and the consequential processing of those messages is prohibitive.

An alternative to direct communication is to organize agents into what is called a federated system $[15]$ . In a federated system, agents do not communicate directly with each other. Instead, the agents communicate only with system programs called facilitators or mediators $[38–40]$ . This communication consists of the agents' needs, abilities, application level information, and various requests [15]. The facilitators use this information to transform application level messages and route them to an appropriate agent. Facilitators thus form a meta-level of communication. A simple case of a federated system architecture is shown in Fig. 2 which illustrates that communication over the Web is done by the facilitators only.

![](/api/attachments/A7V5A2XH/fulltext/images/9f09dd91ff519ef61c9189b9c3213cce628184f3613c2f4d7854657ca3284e30.jpg)  
Fig. 1. A snap-shot view of the contract-net process over the Web (adapted from [34]).

From the federated system paradigm, the role and functionality of facilitators is what requires specification in the context of developing an Open-DSS protocol suite. In the next section, requirements are set forth that operationalize the nature of facilitation in our perspective of future DSS deployment.

## 3. Requirements for an Open-DSS protocol suite

Our suggested approach to Open-DSS draws from the DAI metaphor as discussed in the earlier section, and the model of recent WWW Robots, Wanderers, and Spiders [25]. Robots, Wanderers, and Spiders are all names for programs that automatically and recursively search the WWW in order to identify addresses and/or retrieve documents/pages under a set of end-user stipulated search parameters. For example, the Repository Based Software Engineering Spider “creates an Oracle database of the Web graph, traversing links to a specifiable depth beginning at a URL passed as an argument” [12]. Another example is Lycos, “a Robot that uses a finite memory model of the web to guide intelligent, directed searches for specific information needs” [27]. Emerging commercial products similar in scope to those above include Apple Computer, Inc.’s AppleSearch (we reviewed a trial version on CD ROM) [1]. AppleSearch provides an end-user with an easy-to-use interface to guide searches for text-based documents given keywords stipulated by an end-user. AppleSearch also allows end-users to specify the number of responses to be returned in a keywordbased search conducted by a limited-intelligence computer-based agent.

![](/api/attachments/A7V5A2XH/fulltext/images/c27ba3b9493eafa8edcea06187f9790882e149e13b1e0b5e70f9a3f18c2d2f8b.jpg)  
Fig. 2. A federated system (adapted from [15]).

Consistent with the ideas of the systems and product described above, under an Open-DSS protocol suite we propose to aid end-user DSS discovery by pursuing a strategy whereby DSS builders are required to supply information about their Specific DSS that defines the purpose, the computing environment required, the data inputs required, the data outputs produced, and other information. This information would be added at the time of the DSS's creation by the DSS builder. In addition, we propose a standardized DSS search tool and interface for an end-user. That tool would elicit search parameters including the availability of data to the end-user, keywords describing the needed purpose for a DSS, and the desired outputs of a DSS. As akin to the systems and product discussed above, this approach to DSS deployment in an Open-DSS environment would facilitate the following type of scenario:

Employees working on the line of a billing operations center for a large credit card services provider have been challenged by management to reduce costs. Those employees know there are three types of costs critical to the bottom line: mailing costs, float costs, and operational overhead costs. Mailing costs and operational overhead costs are well understood by the employees, but approaches to reducing float costs are not well understood. First, those employees utilize an interactive DSS search tool to attempt to discover available relevant Specific DSSs. Discovery of relevant Specific DSSs from both within and outside of the organization can serve several purposes. Next, the Specific DSSs discovered in such a search can be studied and analyzed in order to provide a foundation for increased employee learning of finance-based models related to float costs. Third, these candidate DSSs are considered in terms of hardware/software, data, and other resource requirements. Fourth, some of the DSSs discovered in such a search might be amenable to immediate deployment, in which case issues such as availability, price, and licensing are addressed. The DSSs discovered in such a search can provide employees with insight and tools to make effective cost-reduction decisions leading to a direct impact on bottom line productivity in the billing operations center...

This scenario presumes the existence of an Open-

DSS protocol suite. In addition it serves as an exemplar of what we refer to as a General Foundations requirement for an Open-DSS deployment protocol suite, stated as follows.

## 3.1. Requirement 1: General foundations

Automated, intelligent WWW DSS search agents should provide end-users with improved discovery of existing Specific DSSs pertaining to a particular decision making or problem solving situation as defined by end-users and as matched to available Open-DSS protocol suite compliant Specific DSSs.

We use the phrase “automated, intelligent WWW DSS search agents” for several reasons. First, the intelligent search agents are consistent with the federated system concept of a facilitator. Second, WWW search agents (i.e., Robots, Spiders, and Wanderers) are in a nascent stage of development, but their potential to change the way individuals utilize the resources of a vast and growing information systems infrastructure portends significant changes to the manner by which people conduct work and make decisions. Third, while existing systems and products are based solely on text-based keyword searches, we suggest that more intelligent search agents will better serve end-users. Further, we suggest that the automation of those intelligent search agents implies that an end-user’s examination of information infrastructure resources can be conducted in parallel to an end-user’s regular job duties. Fourth, the General Foundations requirement for an Open-DSS protocol suite will enable the DSS research community to develop Open-DSS protocol suite compliant Specific DSSs that can be ‘discovered’ by empowered line personnel. This capability represents a radical departure from traditional DSS deployment whereby managers have traditionally been the ones to devote budgets to the design, development, and implementation of DSSs.

The General Foundations requirement stated above doesn't precisely address how to begin formalizing an Open-DSS deployment protocol suite amenable to implementation in today's inter-networking computing environment. We propose a client/server decomposition model for purposes of elucidating roles for a standard end-user interface, a standard DSS builder interface, and a standard role for automated intelligent WWW DSS search agents. This decomposition is consistent with prevailing definitions for the terms 'client' and 'server' (e.g., [9]). A client is an application that initiates peer-to-peer communication; in the case of our General Foundations requirement, there are two clients: an end-user client and a DSS builder client. A server is a daemon process that waits for incoming communication requests from a client, i.e., a server receives a client's request, performs the necessary computations, and returns the result to the client. A client/server model that decomposes the roles of Specific DSS Builders and Specific DSS end-users is consistent with the following requirement for an Open-DSS protocol suite.

## 3.2. Requirement 2: Client / server decomposition

The decomposition of Open-DSS standards should be along the lines of the client/server computing model, and they should be consistent with prevailing notions of directed network search. Two clients are required, one for the DSS end-user community, and one for DSS builders. A server process is required to act on behalf of an end-user client process to discover relevant Specific DSSs for a particular decision making or problem solving situation.

In addition to a client/server architectural perspective to an Open-DSS protocol suite, there is a need for non-technical requirements that serve to guide Open-DSS protocol suite compliant DSS builders with regard to accountability. For example, compliant DSSs should be built in accordance with considerations regarding the network resources that could be consumed if the purpose of the Specific DSS does not fulfill its promised intent. Further, DSS builders will need to conduct their own searches in order to determine if other Specific DSSs exist that subsume the Specific DSS they plan to add to the global database of Specific DSSs. In addition to DSS builder accountability, end-users also need to be accountable. End-users need to consider the issue of whether they really need a DSS. Also, novice end-users should limit the number of identified DSSs returned that are relevant to their decision making or problem solving situations, then review those DSSs returned with an eye towards how to more precisely specify future search parameters to discover even more relevant DSSs. With respect to incorporating an Open-DSS protocol suite into the genre of Robots, Spiders, and Wanderers now operating on the Internet, the DSS research community will need to be accountable for adhering to the emerging de facto standard “Guidelines for Robot Writers” [14]. Along these lines, an emerging, and latest version of a de facto standard for Robot exclusion can be found at http://web.nexor.co.uk/mak/doc/robots/norobots.html. This emerging Robot exclusion standard will enable the exclusion of specified Open-DSS compliant Specific DSSs from consideration by server agents. This exclusion standard is significant because it facilitates DSS builder security, organizational DSS security, etc. Considered as whole, the above discussion of the non-technical requirements for an Open-DSS deployment protocol suite implies the following requirement.

## 3.3. Requirement 3: Accountability and security

The realization of an Open-DSS protocol suite must go beyond technical architectural considerations in order to address human behaviors. Accountability guidelines for both DSS builders and end-users are required. In addition, an exclusion capability is necessary in order to ensure a high level of security for both organizations and DSS builders. To the extent possible, the Open-DSS protocol suite must adhere to emerging de facto standards for WWW Robots, Spiders, and Wanderers.

The above three requirements have addressed general foundations for a new approach to DSS deployment, the applicability of a client/server decomposition model, and the need for non-technical aspects in a robust protocol suite that is linked to current and emerging research in the area of Robots, Spiders, and Wanderers. At this point, it is advantageous to consider a dynamic model that embodies these requirements. Fig. 3 illustrates a framework for the creation of Open-DSS compliant Specific DSSs by DSS builders and end-user searches as conducted by automated, intelligent WWW DSS search agents. In Fig. 3, numbers assigned to arcs and the associated footnotes are intended to clarify what we describe as roles for an Open-DSS deployment protocol suite based on a client/server decomposition.

![](/api/attachments/A7V5A2XH/fulltext/images/93b7ab8c0de170a02c0f7fb597136d1767cdb1b498141473650b770cff0fbffe.jpg)  
Fig. 3. A dynamic model based on Requirements 1–3.

## Legend:

1. A DSS builder constructs a DSS Deployment Protocol Suite Compliant Specific DSS in conjunction with a DSS Builder Client.

2. The DSS Builder Client enables the construction of a Compliant Specific DSS that is open to retrieval by End-User requests.

3. A specific DSS is now open to End-User searches as conducted by WWW search agents.

4. An End-User constructs a DSS search agent via interaction with the end-user client.

5. The end-user client generates an automated intelligent WWW DSS search agent.

6. A Server Daemon (known as a Robot, Wanderer, or Spider) initiates recursive searches through Netscape Pages in order to discover Specific DSSs matching end-user's needs.

7. Single Specific DSSs and/or integrated Specific DSSs are identified as meeting the criteria of the End-User's search agent.
8. The End-User's search agent returns complete Specific DSSs that address the End-User's decision making or problem solving situation.

9. The End-User's client software supports the utilization of Specific DSSs discovered in the network search.

10. There is an implicit feedback loop between Specific DSS End-Users and DSS Builders. This feedback is intended to enable continuous improvements to Specific DSSs.

The framework of Fig. 3 also includes a feedback loop from end-users to DSS builders. That loop is included in order to facilitate a continuous improvement orientation to the inclusion of Specific DSSs into a global database of Specific DSSs. An additional tenet of DSS deployment is end-user training, although training is not clearly demonstrated in the dynamic model of Fig. 3. The feedback loop and the training aspect need to be included in the requirements for an Open-DSS protocol suite as per stages 4, 5, and 6 of the DSS deployment model described above. These issues are addressed in the following requirement.

## 3.4. Requirement 4: End-user training and DSS builder feedback

Specific DSSs built to be shared both within and across organizations will require the inclusion of computer-based training materials constructed by the builders of DSSs in accordance with new Open-DSS protocol suite standards. At present, the two World-Wide Web Consortium (W3C) protocols – HyperText Transfer Protocol (HTTP), and HyperText Markup Language (HTML) – dominate the Web. Current alternatives to the basic Web protocols include Hyper-G and Java [3]. Specific DSS builders also need end-user feedback in order to improve Specific DSSs and to guide future DSS research. To enable feedback, we propose to incorporate a suitable interface designed to ask the user for permission to set up a feedback relationship, based, for example on the end-user's e-mail address. In this way, DSS builders will have a mechanism for assessing the relevance of their Specific DSSs to organizational needs, and they will have the opportunity to direct their communications to individuals, groups, and organizations where their Specific DSS has been deemed relevant in a particular decision making/problem solving situation.

Requirement 4 addresses end-user training and the automated establishment of linkages between DSS builders and Specific DSS end-users in a way that has heretofore been under-addressed. The basic idea is that a market driven approach to DSS deployment means that end-user decision making/problem solving activities should serve as the stimuli for building Specific DSSs that have relevance to what organizations, specifically empowered line personnel, need in order to improve bottom-line productivity. At a higher level of abstraction, it may be that a Specific DSS, discovered in an end-user search, only addresses a portion of the complete model needed by end-users. Obviously there is a need for devising a search strategy that would enable end-users to express their needs, then an automated, intelligent WWW DSS search agent should be artificially intelligent enough to integrate multiple Specific DSSs into a single, coherent Specific DSS (e.g., [11]). The nature of this integration feature is expressed in the following requirement.

## 3.5. Requirement 5: Model integration

The matching process of the General Foundation requirement suggests that automated, intelligent WWW DSS search agents have the ability to discover a Specific DSS germane to an end-user's decision making or problem solving situation. Research in model integration suggests an exciting potential for adding the necessary intelligence to automated, intelligent WWW DSS search agents to enable an agent to construct a Specific DSS from a collection of component Specific DSSs. Thus, a model integration requirement for the Open-DSS protocol suite is necessary, however implementation details will require additional research.

Requirement 5 is an example of where an emerging area of promising research needs to be included in an agreed-upon Open-DSS protocol suite, but further research is needed to finalize implementation details. While this issue is not specific to DSS deployment on the WWW, this type of situation can be dealt with, for example, by including an additional, and final requirement as follows.

## 3.6. Requirement 6: Incremental refinement of the Open-DSS deployment protocol suite

Emerging research in the DSS area will undoubtedly require the addition of implementation details that add more intelligence to automated WWW DSS search agents. In such cases, there should be “not yet defined” portions of protocol suite details, and those portions should serve as stimuli for needed research in DSS.

## 4. A proposed set of preliminary specifications

The requirements addressed in the previous section are operationalized here in a proposed set of protocol specifications. We suggest a specification that emphasizes a modularized, layered approach. In order to provide details in a layered approach to the protocol suite, there are several assumptions that need to be made. These assumptions relate to issues surrounding the way compliant Specific DSSs are to be built and maintained. In addition, they address the model integration needs which are stated in our Requirement 5. We mention these assumptions for completeness:

1. DSSs decomposability: the degree to which a design method assists in decomposing the DSSs into subordinate DSSs.

2. DSS composability: the degree to which a design method assists in integrating pre-existing DSSs into compound DSSs.

3. DSS understandability: there is a high degree of DSS understandability if each DSS can be understood by AI agents.

4. DSS continuity: the DSS design method should be such that a small change in the specification should only necessitate a very limited number of DSS components to be modified. It should above all not demand any change in the overall organization of the DSS community and the results that exist therein.

5. DSS protection: the design method would support DSS protection if given unforeseen circumstances confine their effects to the DSS or DSS component in which they occurred. These effects will not propagate to other DSSs.

Concomitant with the above assumptions, a layered approach is used to operationalize the abstractions required to implement the requirements for the design of the protocol suite. Layers enable Specific DSSs to form an object that resides at a node which can be searched by the search agent. The four proposed layers are drawn from Newell and Simon's premises about problem definition:

"To have a problem implies (at least) that certain information is given to the problem solver: information about what is desired, under what conditions, by means of what tools and operations, starting with what initial information, and with what access to what resources. The problem solver has an interpretation of this information – exactly that interpretation which lets us label some part of it as goal, another part as side conditions, and so on. Consequently, if we provide a representation for this information (in symbol structures), and assume that the interpretation of these structures is implicit in the program of the problem solving IPS (Information Processing Systems), then we have defined a problem" ([29], p. 73).

An advantage for adopting this approach in delineating the layers is that the functionality of each layer has been addressed in previous well defined research streams in the DSS research community. This approach also surfaces a problem in deploying DSSs on the WWW: although access to the WWW can be viewed as a resource, it cannot be viewed as a complete tool. This is because access to the WWW can be seen as a generator of a set of possible DSS solutions, but it cannot be seen as an effective generator of a set of actual DSS solutions. We propose that an Open-DSS protocol suite constitutes one method of actual solution set generation in the nascent research area of interorganizational DSS search over the WWW [4,5].

The generation of solution sets depends on interpretations of the meaning of provided information. In turn, these interpretations are dependent on proper representation of the problem space. It is through proper representation and symbol manipulation that incoming information is linked to problem solutions. Two general sets of representations are appropriate: set representations, which represent the subset of actual solutions contained in the superset of possible solutions, and search representations, which represent the problem of locating actual solutions [29]. Of these two, the search representation is the more convenient characterization of the Open-DSS protocol suite.

Search representations must conform to the object of the search. Such objects can be described via a state language containing symbols designating expressions and their components, and a process language containing symbols designating the transformational operators of such expressions. These languages specify the problem space: incoming information is specified in the state language, and operations and actions are specified in the process language. Problem solving is thus the transformation of incoming information into appropriate responses. The Open-DSS protocol suite would develop widely accepted search representations for the problem space of Specific DSS discovery. This objective would be implemented by combining the aforementioned problem solving model [29] with the layered approach common to many distributed architectures (e.g., ISO/OSI model, DARPANET, IBM's SNA, and Digital Equipment's DECNET).

Development of the Open-DSS protocol suite can now be grounded in the above theory. First, a state language based on a model of incoming information to the problem solver (e.g., tools and operations, resources) would be developed. The symbol set of the state language used by the Specific DSS would be specified in model form in the Functionality layer. Tools, operations, and other resources to be provided by the problem solver (or the problem solver's organization) would be specified in the Resource layer. Interpretations of the program would be surfaced and represented through a human-language based interface in the Semantic layer. Finally, the set of possible solutions would be contained in the Specific DSS layer. The process language would act upon the Resource, Functionality, and Semantic layers to generate a set of actual solutions from the set of possible solutions available through the Specific DSS layer.

An important aspect of this problem space, its formulation, and its problem solving process involves the order in which a search strategy accesses the layers of the Open-DSS protocol suite. In devising a search strategy, it is often useful to differentiate the search strategy from information generated during the search. Information generated during the search may vary in its ability to predict the location of an element in the actual solution set. It may also vary in its “density” (i.e., predictive power per unit of memory storage). The more predictive and the more “dense” the information is in identifying an element of the set of actual solutions, the more valuable that information is in increasing the effectiveness and efficiency of heuristic searches. Therefore, information of a higher predictive nature and higher density should be placed at the entry levels of the Open-DSS protocol suite.

Although the problem solving paradigm from $[29]$ is useful for abstracting layers for the Open-DSS protocol suite, it is less helpful in ordering them for a heuristic search. Consequently, another problem solving process which is more closely related to the DSS search problem space must be employed. The design and development of Specific DSS implementations is one such process. Research from this area [23,24] offers ordered guidelines that can serve as a model of ordering information in the Open-DSS protocol suite. The ordered DSS design guidelines are mapped to the corresponding premises from the problem solving paradigm and listed in the first, second, and third columns of Fig. 4, respectively. These guidelines and premises are then extended to order the layers of the Open-DSS protocol suite. The DSS design literature [23,24] thus suggests that a heuristic search would access the layers of the Open-DSS protocol suite in the following order: Semantic/Interface, Functionality, Resource, and Product/Specific DSS. This ordering of the layers, as well as an explanation for each protocol layer, is displayed in the fourth and fifth columns of Fig. 4, respectively.

The resulting protocol suite thus provides a general yet practical model for initiating future research and development in the selective discovery of Specific DSS implementations on the WWW. Its contribution to research lies in the provision of a standardized platform for hypothesis testing and empirical validation. This platform would be useful for such research areas as model integration. However, because model integration is at an early stage of development, to address the topic of setting standards for this area is premature. Accordingly, we envision the future need for a fifth layer to address model integration needs. The practical contribution of the Open-DSS protocol suite lies in its ability to generate inexpensively a set of actual solutions from a set of widely dispersed possible solutions. The four-layer model also offers a minimal structure to incorporate traditional ideas of DSS design with DAI strategies.

The uniqueness of the Open-DSS protocol suite can be demonstrated through a comparison to DSS search engines. One such search engine, DecisionNet [4,5], can serve as an example in this comparison. The two are similar in several respects. Both utilize the WWW infrastructure and are based on the client/server model. Both are motivated by technological advancements in such DSS reference disciplines as EUI, DBMS, and AI. However, DecisionNet and the Open-DSS protocol suite differ in a number of ways. Such differences concern motivation for development, mediators employed, and contribution to research and practice. These and other differences can be found in Fig. 5 which contrasts the DecisionNet approach to the Open-DSS protocol suite.

<table><tr><td>Ordered Steps from Keen &amp; Scott Morton (1978)</td><td>Ordered Steps from Keen &amp; Gambino (1983)</td><td>Mapped to Newell &amp; Simon&#x27;s (1972) Problem Solving Paradigm</td><td>Ordered Open-DSS Deployment Layers</td><td>Open-DSS Protocol</td></tr><tr><td rowspan="4">Define key problemDesign the DSSData managementEvolutionary design, mgmt. learning</td><td rowspan="4">Sketch user-system dialogSolicit user reactionBuild a DSS product</td><td>Interpretations of initial information given to problem solver (e.g., goals, conditions, and resource constraints and availability) and symbol structures contained within information processing program.</td><td>Semantic/Interface</td><td>Text explanation of DSS and its key area of application. May include a copy of end-user and DSS builder interfaces. Stored in web directory (e.g., searchable through Lycos).</td></tr><tr><td>State language containing symbols designating expressions and their components; process language containing symbols designating transformation operators of such expressions.</td><td>Functionality</td><td>Brief explanation of the underlying models behind the DSS. May include assumptions, mathematical formulae, demo, etc.</td></tr><tr><td>Tools, operations, information, and other resources given to problem solver.</td><td>Resource</td><td>Hardware, software, and other resources needed by the user. Can include personal skill requirements for the user</td></tr><tr><td>Set of possible solutions.</td><td>Product/Specific DSS</td><td>The products and services received from the DSS provider, as well a legal and other requirements requested of the user.</td></tr></table>

Fig. 4. An ordering for Open-DSS deployment layers based on ordered DSS design methodologies.

The similarities between the Open-DSS protocol suite and the DecisionNet approach demonstrate that the two approaches are not mutually exclusive. In the Open-DSS protocol suite, for example, DSS technologies can be delivered as services as well as products.

The relationship between DSS design concepts [23,24], DAI strategies [31], and the Open-DSS protocol layers is displayed in Fig. 6. This relationship is represented as a horizontal correspondence between the layers of these three domains. As a bridge between DSS design and DAI strategies, the Open-DSS protocol suite retains traditional ideas of DSS design while integrating newer concepts from DAI. This union of DAI and traditional DSS concepts provides a richer foundation for integrating DSS users and providers over the WWW.

This union is demonstrated in preliminary specifi-

<table><tr><td></td><td>DecisionNet Approach</td><td>Open-DSS Protocol Suite</td></tr><tr><td>Motivation</td><td>Need for real-time and interactively specified, mathematical processing of data while imposing minimum technology requirements on its users (both consumers and providers).</td><td>Need for a new perspective to DSS deployment due to changing environment--organizational restructuring, information systems development outsourcing, etc.</td></tr><tr><td>Mediator</td><td>Broker: a designated node(s) that possesses expertise and capacity needed to search, access, and use the decision technologies.</td><td>Facilitator: a less structured network that allows any node to serve as a facilitator.</td></tr><tr><td>Participants</td><td>Registered customers and providers.</td><td>Virtually everyone who has access to the WWW.</td></tr><tr><td>Search Control</td><td>Exclusively by the broker on registered providers.</td><td>Diffused to both the end-users and the DSS builders. The end-users have more open and flexible control in the search process through the information supplied by the DSS builder at each layer.</td></tr><tr><td>Search Strategy</td><td>The broker(s) acts similarly to the role of a traditional consulting firm which provides solutions to the customers based on their requests. The broker has full control of the selection process.</td><td>More detailed specifications are needed to accelerate the search process, which means the DSS builder needs to better inform and educate the end-users via the layered specifications. The end-user makes the final selection decision.</td></tr><tr><td>Market Structure</td><td>A brokerage monopolized market.</td><td>A free market environment that is consistent with the way the Web is evolving.</td></tr><tr><td>Major Contributions</td><td>Proposed a new way to deliver technologies to users--as services rather than as products. Determined the transactions and functionality requirements of the DecisionNet. Developed a prototype.</td><td>Identified the needs for new infrastructure support to discover and utilize DSSs. Proposed a modularized, layered approach to the design of the protocol suite. Suggested a set of preliminary specifications of the layers to help operationalize the requirements for the design of the protocol suite.</td></tr><tr><td>Steps in Traditional DSS Design</td><td>Open-DSS Deployment Layers</td><td>Strategic Considerations of DAI (Shaw &amp; Fox, 1993)</td></tr><tr><td rowspan="2">Define key problem (Keen &amp; Scott Morton, 1978); Sketch user-system dialog (Keen &amp; Gambino, 1983)</td><td rowspan="2">Semantic/ Interface</td><td>Goal Identification &amp; Task Assignment</td></tr><tr><td rowspan="2">Distribution of Knowledge, Learning Schemes</td></tr><tr><td rowspan="2">Design the DSS (Keen &amp; Scott Morton, 1978); Solicit user reaction (Keen &amp; Gambino, 1983)</td><td rowspan="2">Functionality</td></tr><tr><td rowspan="2">Organization of Agents</td></tr><tr><td>Data management (Keen &amp; Scott Morton, 1978)</td><td rowspan="2">Resource</td></tr><tr><td rowspan="3">Evolutionary design, management learning (Keen &amp; Scott Morton, 1978); Build a system product (Keen &amp; Gambino, 1983)</td><td rowspan="2">Coordination Mechanisms</td></tr><tr><td rowspan="2">Product/ Specific DSS</td></tr><tr><td>Distribution of Knowledge, Learning Schemes</td></tr></table>

Fig. 5. A comparison between DecisionNet and the Open-DSS protocol suite.

Fig. 6. A comparison of traditional DSS Design, Open-DSS deployment, and a DAI framework.

<table><tr><td colspan="2">Semantic/Interface Layer Specifications</td></tr><tr><td colspan="2">Keywords Relating to:</td></tr><tr><td>Key problem description</td><td>Message/information type</td></tr><tr><td>Functional area</td><td>Input and output variables</td></tr><tr><td>Industrial area</td><td>Coordination strategies to link DSSs</td></tr><tr><td>Cross-functionality</td><td>Individual, group, or organizational DSS</td></tr><tr><td>Generality/depth of model</td><td>Task &amp; resource allocation</td></tr><tr><td colspan="2">Text Explanation:</td></tr><tr><td>Written language (e.g., English)</td><td>Keyword format/WWW addressing</td></tr><tr><td>Programming language for hypertext (e.g., HTML)</td><td>Graphics format (e.g., gif)Length</td></tr></table>

Fig. 7. Examples of proposed specifications for the Semantic layer.

![](/api/attachments/A7V5A2XH/fulltext/images/ba38c73ae2b71707a16dc88bfcc531d9381cac0fba3df52ccf11899113126bf4.jpg)  
Fig. 8. Examples of proposed specifications for the Functionality layer.

![](/api/attachments/A7V5A2XH/fulltext/images/cded5ea3bf9a5adc99e13c0049d7639dd586833ef3833b42a0a9e7640cc2ff02.jpg)  
Fig. 9. Examples of proposed specifications for the Resource layer.

cations of the layers displayed in Figs. 7–10. Traditional DSS ideas and their operationalizations are portrayed in the following examples: key problem (key problem description in the Semantic/Interface layer); user reaction (provider e-mail addresses in the Resource layer); data management (data dictionary in the Resource layer); and evolutionary design (shared learning in Product/Specific DSS layer). DAI strategies and their operationalizations are portrayed in these examples: task assignment (task and resource allocation in the Semantic/Interface layer);

distribution of knowledge (e-mail addresses of other users in the Resource layer); organization of agents (agent organization and coordination schemes in the Resource layer); coordination mechanisms (message/information type in the Semantic layer); and learning schemes (algorithms and heuristics in the Functionality layer). By integrating emerging DAI technologies with traditional DSS technologies, the Open-DSS protocol suite supports a growing number of WWW implementations of DSS technology (e.g., [7]). The final three figures display examples of

![](/api/attachments/A7V5A2XH/fulltext/images/d5d910816f1148ad4b8c78bd8eb3250ece1e20ac86f9f006050fa78b4915ab2d.jpg)  
Fig. 10. Examples of proposed specifications for the Specific DSS layer.

![](/api/attachments/A7V5A2XH/fulltext/images/12c7c167063c55604d0ba7f19e999ad3a585c87a04f3c60f734ac07f51a7a6df.jpg)  
Fig. 11. Example of a data entry form to commence a search for candidate DSSs.

WWW interfaces which conform to the Open-DSS protocol suite. These examples provide a flavor of future implementations.

Fig. 11 describes a data entry form to browse the WWW. Partial completion of the data entry form would be acceptable. Depending on the implementation, users may enter their own input (e.g., as in

Keywords) or they may choose from preselected entries (e.g., Representation). Such data entry would be converted by the browser to standards within the protocol suite. A search would begin when the user selects the “Begin Search” command button.

Figs. 12 and 13 describe the examples of documents returned to the requester after a search has been initiated. Fig. 12 demonstrates breadth-first search in a list of “hits”. This information is largely derived from the Semantic layer of the protocol suite, although some items may be added. For instance, the third hit in Fig. 12 contains two such features. First, a graphic icon has been added to allow the user to see a demo of the Specific DSS. Second, access to the Specific DSS is controlled through the use of firewalls and passwords. The user must first notify the DSS provider in order to obtain permission to access the Specific DSS. Permission is operationalized in a one-time password to access the Specific DSS files contained in the directory “protected.documentss”. The user can then access the file site, enter the password, and obtain the desired files. An example of the screen from this protected directory is displayed in Fig. 13.

![](/api/attachments/A7V5A2XH/fulltext/images/b3d6b16fa3cfccd68082ce1056696f998ff35abb6a0a44e3b9e6cab526aef72a.jpg)  
Fig. 12. Example of a list of discovered Specific DSSs.

![](/api/attachments/A7V5A2XH/fulltext/images/d534e10fd56f611dbde7204599bb5d3f415dd7d2b4adcedf0dcd63918e9b53cc.jpg)  
Fig. 13. Example of a DSS search return form.

Fig. 13 displays specific information on this DSS. Pages for other Specific DSSs might include mathematical formulae, related WWW sites, and other information contained in Figs. 7–10. At this point it is advantageous to consider the four layers and the relevance to the scenario depicted in Section 3 above.

To implement the first step in the scenario, the employees would express their problem area and initiate a search using a suitable (text/graphics) representation. After receiving information regarding candidate DSSs, the Functionality layer would provide facilities for analyzing the suitability of each model to the billing operations problem area. The Resource layer would assist the employees in determining which of those DSSs can run on the computing platforms available. If some of the discovered DSSs are amenable for immediate deployment, further information regarding availability, price, and licensing can be accessed through the Product/Specific DSS layer.

## 5. Limitations and benefits of the requirements proposed

The main limitation to the proposed Open-DSS requirements may prove, over the long run, to be one of the major benefits. Overall, we have taken a market-driven approach to the definitions of requirements by including only a minimal number of the requirements we felt were necessary in order to begin moving towards protocol suite implementation details in future work. For example, there are no restrictions embedded in the requirements regarding the definition of exactly what a “Specific DSS” is. This implies a lack of control – from the protocol level – over what might be put on the Internet that is portrayed as a Specific DSS. In addition, this implies that a keyword orientation to the categorization of a new Specific DSS by its builder is not specified by the requirements we propose. We contemplated an object-oriented structure for specifying a set of parameters for characterizing a new Specific DSS, e.g., finance model, distribution model, queuing model, math programming model, statistical model, etc. On closer inspection, we felt that the DSS builder would be better able to establish descriptions of a Specific DSS from the perspectives of end-users being targeted by the Specific DSS. Again, this is consistent with the market-driven approach we subscribed to.

One important advantage to the proposed Open-DSS protocol suite requirements is that they are mapped to emerging standards for Robots, Wanderers, and Spiders that already exist on the WWW. Through this mapping, we have suggested adoption of the protocol suite that already exists and has been evolved through early experience with this type of intelligent search agent on the WWW. The benefit of this mapping is that any approach the DSS community takes for implementing the requirements, the Open-DSS protocol suite will be upwardly compatible with protocol suites for those generalized search agents already operating on the WWW. Last, and most importantly, what we have proposed is a first step for altering traditional assumptions and approaches to DSS deployment in a deployment strategy that realistically targets the new majority audience of DSS end-users: empowered line personnel aligned in teams around fundamental business processes.

## Acknowledgements

The authors gratefully acknowledge Professor Bui and the anonymous referees for their insightful and constructive comments on earlier drafts of this paper. Commercial DSS builders and DSS researchers around the world, regardless of the traditional DSS research niche they have ascribed to and have historically worked in, are hereby invited to become involved in research projects related to the issues our DSS research group at Arizona State University have been dealing with. At stake is the ability of existing DSS research streams to maintain growth and relevance as the pace of technological change, most recently in the areas of inter-networking and client/server computing, challenges the very assumptions of virtually all traditional information systems research streams. There are fundamental changes taking place in today's modern organization, and the traditional assumptions about DSS deployment are now less relevant. We would appreciate any comments or insights you have: please forward them to mgoul@imap1.asu.edu. Your comments and insights will be used to guide us as we work to define implementation details for the Open-DSS protocol suite requirements we have proposed in this paper.

## References

[1] AppleSearch Trial Software™, Client/Server Software for Text Search and Retrieval, Apple Computer, Inc. (1993).

[2] J.L. Bennett, User-Oriented Graphics Systems for Decision Support in Unstructured Tasks, in: S. Treu, Ed., User-Oriented Design of Interactive Graphics Systems, Association for Computing Machinery, New York, NY (1977).

[3] H. Berghel, HTML Compliance and the Return of the Test Pattern, Communications of the ACM 39, No. 2 (1996) 19–22.

[4] H.K. Bhargava, A.S. King and D.S. McQuay, DecisionNet: An Architecture for Modeling and Decision Support over the World Wide Web, in: T.X. Bui, Ed., Proceedings of the Third International Conference on Decision Support Systems, ISDSS '95, Hong Kong (June 22–23, 1995) 499–506.

[5] H.K. Bhargava, R. Krishnan and D. Kaplan, On Generalized Access to a WWW-based Network of Decision Support Services, in: T.X. Bui, Ed., Proceedings of the Third International Conference on Decision Support Systems, ISDSS '95, Hong Kong (June 22–23, 1995) 507–516.

[6] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Foundations of Decision Support Systems (Academic Press, Orlando, FL, 1981).

[7] A.B. Bordetsky and P.J. Levy, Collaborative Computing for Decision Support in Cardiovascular Consulting, Journal of Organizational Computing 5 (1995) 401–416.

[8] W.C. Burkan, Making EIS Work, DSS '88 Transactions, The Institute of Management Sciences, Providence, RI (1988) 121–136.

[9] D. Comer and D.L. Stevens, Inter-Networking with TCP/IP, Volume III, Client – Server Programming and Applications (BSD Socket Version) (Prentice-Hall, Englewood Cliffs, NJ, 1993).

[10] R.W. Blanning, C.W. Holsapple and A.B. Whinston, Eds., Decision Support Systems 9, No. 1, Special Issue on Model Management Systems (January, 1993).

[11] D.R. Dolk and J.E. Kottemann, Model Integration and a Theory of Models, in: R.W. Blanning, C.W. Holsapple and A.B. Whinston, Eds., Decision Support Systems 9, No. 1, Special Issue on Model Management Systems (January, 1993) 51–63.

[12] D. Eichmann, Repository Based Software Engineering Project Spider, in: M. Kostner, Ed., World Wide Web Robots, Wanderers, and Spiders (downloaded from the Internet on December 29, 1994), WWW pages provided as a Public Service by Nexor, Inc.

[13] J.W. Erkes, K.B. Kenny, J.W. Lewis, B.D. Sarachan, M.W. Sobolewski and R.N. Sum, Implementing Shared Manufacturing Services on the World-Wide Web, Communications of the ACM 39, No. 2 (1966) 34–45.

[14] J. Fletcher and L. McLoughlin, Guidelines for Robot Writers, in: M. Kostner, Ed., World Wide Web Robots, Wanderers, and Spiders (downloaded from the Internet on December 29, 1994), WWW pages provided as a Public Service by Nexor, Inc.

[15] M.R. Genesereth, N.P. Singh and M.A. Syed, A Distributed and Anonymous Knowledge Sharing Approach to Software Interoperation (available as http://logic.stanford.edu/sharing/papers/fgcs.ps, November 15, 1994).

[16] M. Goul, J.C. Henderson and F.M. Tonge, The Emergence of Artificial Intelligence as a Reference Discipline for Decision Support Systems Research, Decision Sciences, Special Issue on Knowledge-Based DSS 23, No. 6 (1992) 1263–1276.

[17] G. Hall, J. Rosenthal and J. Wade, How to Make Reengineering Really Work, Harvard Business Review 71, No. 6 (November/December 1993) 119–131.

[18] M. Hammer, Reengineering Work: Don't Automate, Obliterate, Harvard Business Review 68, No. 4 (July/August 1990) 104–112.

[19] M. Hammer, Re-Engineering, Retail Business Review 61, No. 3 (March/April 1993) 10–19.

[20] E.G. Hurst, D.N. Ness and T.J. Gambino, Growing DSS: A Flexible, Evolutionary Approach, in: J.L. Bennett, Ed., Building Decision Support Systems (Addison-Wesley, Reading, MA, 1983) 111–132.

[21] N.R. Jennings, Coordination Techniques for Distributed Artificial Intelligence, in: G.M. O'Hare and N.R. Jennings, Eds., Foundations of Distributed Artificial Intelligence (J. Wiley and Sons, Chichester, UK, 1995).

[22] J.P. Morgan WWW Pages, RiskMetrics™, Copyright 1994 by J.P. Morgan and Co. (downloaded from the Internet on January 15, 1995).

[23] P.G.W. Keen and M.S. Scott Morton, Decision Support Systems: An Organizational Perspective (Addison-Wesley, Reading, MA, 1978).

[24] P.G.W. Keen and T.J. Gambino, Building a Decision Support System: The Mythical Man-Month Revisited, in: J.L. Bennett, Ed., Building Decision Support Systems (Addison-Wesley, Reading, MA, 1983) 133–172.

[25] M. Koster, World Wide Web Robots, Wanderers and Spiders (downloaded from the Internet on December 29, 1994), WWW pages provided as a Public Service by Nexor, Inc.

[26] P. Maes, Agents that Reduce Work and Information Overload, Communications of the ACM 37, No. 7 (1994) 31–40.

[27] M.L. Mauldin, Lycos, in: M. Kostner, Ed., World Wide Web Robots, Wanderers, and Spiders (downloaded from the Internet on December 29, 1994), WWW pages provided as a Public Service by Nexor, Inc.

[28] J.H. Moore and M.G. Chang, Meta-Design Considerations in Building DSS, in: J.L. Bennett, Ed., Building Decision Support Systems (Addison-Wesley, Reading, MA, 1983) 173–204.

[29] A. Newell and H.A. Simon, Human Problem Solving (Prentice-Hall, Englewood Cliffs, NJ, 1972).

[30] PACT: An Experiment in Integrating Concurrent Engineering Systems (available as http://www.eit.com/papers/pact/pact.html#Krstan).

[31] M.J. Shaw and M.S. Fox, Distributed Artificial Intelligence for Group Decision Support, Decision Support Systems 9 (1993) 349–367.

[32] A. Silberschatz, J. Peterson and P. Galvin, Operating System Concepts (Addison-Wesley, Reading, MA, 1991) 597–627.

[33] R.G. Smith, The Contract Net Protocol: High Level Communication and Control in a Distributed Problem Solver, IEEE Transactions on Computing C-29 (1980) 1104–1113.

[34] R.G. Smith and D. Randall, Frameworks for Cooperation in Distributed Problem Solving, in: A.H. Bond and L. Glasser, Eds., Readings in Distributed Artificial Intelligence (Morgan Kaufman, San Mateo, CA, 1982) 61–70.

[35] R.H. Sprague, Jr., A Framework for the Development of Decision Support Systems, MIS Quarterly 4, No. 4 (December, 1980) 1–26.

[36] R. Sprague and H.J. Watson, Eds., Decision Support Systems (Prentice-Hall, Englewood Cliffs, NJ, 1993).

[37] Wall Street Journal, On The Pressure to Work Faster (December 23, 1994), p. 1.

[38] G. Wiederhold, Mediation in the Architecture of Future Information Systems, IEEE Computer Magazine (March 1992) 38–49.

[39] G. Wiederhold, P. Wegner and S. Ceri, Towards Metaprogramming, Communications of the ACM (November 1992) 88–99.

[40] G. Wiederhold, Interoperation, Mediation, and Ontologies, Proceedings, International Symposium on Fifth Generation Computer Systems (FGCS94), Workshop on Heterogeneous Cooperative Knowledge-Bases W3, ICOT, Tokyo (December 1994) 33–48.

[41] M. Woolridge and N.R. Jennings, Intelligent Agents - Theories, Architectures, and Languages (Springer-Verlag, Berlin, 1995).

![](/api/attachments/A7V5A2XH/fulltext/images/5bf548bf30fb703a39ee448816cf3a08af6c283133d50a5eb2e9c414fda0ed63.jpg)

Michael Goul is an Associate Professor of Computer Information Systems at Arizona State University. His research has been published in a wide range of academic and practitioner journals, and his recent research interests integrate the disciplines of decision support, distributed artificial intelligence, and Web search agents. Dr. Goul has published papers in Decision Sciences, Organizational Computing, IEEE Expert, Journal of Management Information Sys-

![](/api/attachments/A7V5A2XH/fulltext/images/be719a6f06f6ab9f32f953a656405c70f2034339dfb2c1b7992956f6a95fdb0d.jpg)

Danny Fernandes is a doctoral student at Arizona State University, College of Business. He received his B.Sc. in Mechanical Engineering (1979) and an M.B.A. (1986) from the University of Nairobi (Kenya). He is on the faculty of the Department of Management Science, University of Nairobi, and has done consulting work in the information systems area. His research interests include AI applications to Decision Support. He is a member of INFORS, DSI, and ACM.

tems, Organizational Computing, and other journals. He has also co-edited a special issue of Decision Sciences on decision support and artificial intelligence, and served as Program Co-Chair for the Association for Information Systems Second Annual Americas Conference.

![](/api/attachments/A7V5A2XH/fulltext/images/4ca936663685aadd81bc560006cb529df24b32d9b7b5e013ce405b76ba1389d2.jpg)

Andrew Philippakis is Professor of Information Systems at Arizona State University and Director in Information Technology for the College of Business. His research interests include decision support systems and organizational impact of technology. He has published in such journals as Decision Sciences, Decision Support Systems, and Organizational Computing.

![](/api/attachments/A7V5A2XH/fulltext/images/240255ece8889b28ba8d64ac38e7123f33430d6d538f22fee7cc9af02d4bcb56.jpg)

![](/api/attachments/A7V5A2XH/fulltext/images/0771cf2af41e8e1ebada5bf76956a31c47ad1f28a07d6b98c8b26c72842e6d7c.jpg)  
Robert F. Otondo is a doctoral student in Computer Information Systems at Arizona State University. He received his M.S. in Computer Information Systems from Arizona State University in 1993 and his M.B.A. from California State University, Sacramento in 1983. His research interests include the application of organizational learning to the analysis and design of decision support systems. He is a member of AIS, DSI, TIMS, and ACM.

Melody Y. Kiang is an Associate Professor of Computer Information Systems at Arizona State University. She received her M.S. from the University of Wisconsin, Madison, and her Ph.D. in Management Science and Information Systems from the University of Texas, Austin. Her research emphasizes the development and application of artificial intelligence techniques to a variety of management problems. Dr. Kiang has published papers in Management Sci-

ence, IEEE Transactions on SMC, Decision Support Systems, The Journal of Management Information Systems, The European Journal of Operations Research, The Journal of the Operational Research Society, and other professional journals. She is an associate editor of Decision Support Systems and is a guest editor of a special issue of that journal on Qualitative Reasoning in Business, Finance, and Economics. She is a member of TIMS, AIS, and IEEE.
