---
otero_id: 1592
otero_key: "XDHBR6DW"
title: "Supporting dynamic group decision and negotiation processes: A traceability augmented peer-to-peer network approach"
authors: "Kannan Mohan; Peng Xu; Balasubramaniam Ramesh"
year: "2006"
journal: "Information & Management"
doi: "10.1016/j.im.2006.04.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Supporting dynamic group decision and negotiation processes: A traceability augmented peer-to-peer network approach

Kannan Mohan <sup>a,\*</sup>, Peng Xu <sup>b</sup>, Balasubramaniam Ramesh <sup>c</sup>

<sup>b</sup> Department of Management Science and Information Systems, College of Management, University of Massachusetts Boston, MA, United States

Received 13 June 2005; received in revised form 3 February 2006; accepted 8 April 2006 Available online 30 May 2006

## Abstract

Peer-to-peer (P2P) networks are gaining popularity in supporting group decision and negotiation (GDN) activities in which ad hoc, transient groups participate. In these, multiple stakeholders create and use knowledge that is fragmented and distributed across different locations. While P2P networks help establish physical links across participants, they lack the capability to integrate knowledge fragments embedded in documents and artifacts distributed across peers. We augmented the P2P architecture with traceability to provide a way of integrating distributed knowledge. We implemented this approach in a prototype system that used a P2P networking tool. Using a case study of software development outsourcing, we showed how our approach supported critical GDN activities. Qualitative evaluation of our approach in supporting GDN was also demonstrated. <sup>#</sup> 2006 Elsevier B.V. All rights reserved.

Keywords: Group decision and negotiation; Peer-to-peer networks; Traceability; Knowledge integration

## 1. Introduction

Group decision and negotiation (GDN) activities are important in organizational decision-making. During the process, different parties describe their goals, concerns, and constraints, discuss alternative solutions, make compromises, and achieve agreements. GDN support systems (GDNSS) facilitate communication and help organize, execute, and preserve various aspects of the process [5,9,16,18]. GDN activities are increasingly carried out by teams engaged in virtual collaboration. Such a team comprises of individuals brought together for a specific purpose, for example, the design of a product. These teams are usually cross-disciplinary in that the members come from different functions or specialties [26]. The membership of dynamic teams is often inter-institutional, representing suppliers and clients [10]. They are transient [1]; they are usually disbanded (or radically restructured) after the assignment is completed [34] and have been used extensively in product design [23], software development [21,31], management consulting [38], and health care [39].

GDNSS provide an environment where participants can meet virtually, share ideas, discuss solutions, and reach agreement. However, current GDNSS using a centralized architecture are not designed to support multiple ad hoc teams with distributed knowledge sharing among their members. As these teams are commonplace, solutions to meet their needs in a more decentralized fashion is valuable. Our research was motivated by this need to support knowledge intensive GDN processes.

A peer-to-peer (P2P) network is a promising solution to supporting the needs, since it aids the formation of ad hoc teams and can be used for knowledge sharing among them. Microsoft’s Groove<sup>1</sup>, a popular P2P networking tool, and the distinction that Kazaa<sup>1</sup> has achieved show that P2P networks are becoming mainstream collaboration technologies.

To be effective, participants in GDN processes require significant contextual and systemic knowledge about the issues under discussion. Though P2P technology provides a flexible infrastructure for collaboration, it lacks the ability to integrate components of knowledge fragmented among its participants. For example, ideas proposed during GDN and arguments that support and oppose these ideas are often known only to some participants and are embedded in several documents. Recent research on domains such as complex software development has suggested that sharing and integrating this knowledge is essential for improving GDN [28]. Consider a scenario where a supplier and a buyer are negotiating an outsourcing contract. Managers, developers and other stakeholders from different locations may participate using GDNSS. During the discussion, managers make offers and counter offers and refer to relevant information held in various documents to support their positions. They share only non-proprietary knowledge with their counterparts during the negotiation and thus the creation of semantic links among ideas, concepts, and other knowledge fragments will help participants organize and integrate the knowledge, thereby improving the GDN process [8,32]. Though P2P networks help in sharing documents amongst the participants, they do not link the knowledge fragments.

We thus constructed our research question: ‘‘how can P2P networks be augmented to integrate knowledge generated and be used during complex GDN processes?’’

We propose traceability as a solution to aid in providing semantic links across distributed knowledge fragments. Traceability, defined as the ability to describe and follow the life of a conceptual or physical artifact, has been used to support knowledge integration [27]. It is used in software development to ensure consistency across different artifacts and completeness of the system by linking the software components. This could be valuable in GDN activities.

In summary, we suggest that peer-to-peer networks augmented with traceability will provide effective support for GDN processes and discuss two components:

a. a P2P network as a way of forming ad hoc groups and b. traceability as the means of integrating fragmented knowledge components.

## 2. Group decision and negotiation

The main objective of GDN processes is to choose among alternatives championed by multiple parties within a reasonable period of time. Participants often have competing viewpoints and interests. GDNSS help them organize discussions, structure the negotiation, and evaluate alternatives.

## 2.1. Tools that support group decision and negotiation

GDNSS provide an integrated set of tools for generating and exchanging ideas, classifying and prioritizing alternatives, and performing other support functions. They have been successfully applied in fields such as software quality inspections [17], strategic planning [15], public policy planning [36], etc.

Early GDNSS provided basic functions such as synchronous meeting and voting facilities. Discussions conducted typically contained large amounts of unstructured knowledge. Participants often found it difficult to retrieve specific fragments of knowledge acquired from these discussions. This motivated the development of GDNSS that helped organize knowledge using argumentation models, concept mapping, and graphic representation of the history of discussions [7,37]. Nunamaker et al. [25] developed systems that could organize ideas so that they could be synthesized and consolidated. These also provided an analyzer that allowed the content to be viewed in the form of tables and networks. Conklin [12] described an argumentation-based GDNSS, QuestMap, which supported a structured approach. It adopted the issue based information system (IBIS) model [13] to index unstructured information and thus helped capture key issues and ideas during a discussion, displaying them graphically. Becker and Bacelo [4] and Karacapilidis et al. [19] also illustrated the adoption of the IBIS model to structure negotiations. Though these systems supported documentation based on argumentation models, they were limited in their support for ad hoc team formation and integration of knowledge fragments buried in distributed sources.

## 2.2. Need to augment the capabilities of GDNSS

Four core capabilities required for collaboration are process support, process structure, task support, and task structure [14]. Process support involves the provision of electronic communication channels within which participants interact. Process structure involves process techniques or rules that direct timing and content of participant communication. Task support makes it possible to access and integrate available information. Task structure is the use of analytical techniques, quantitative analyses or qualitative structuring techniques, to improve managerial analysis and decision-making.

Our research primarily focused on providing better process and task support, since process and task structure have been well-investigated by past research and are supported by traditional tools.

An important component of task support is providing access to knowledge about prior, related tasks. In collaborative activities, a variety of stakeholders bring together their often-unique viewpoints, objectives, priorities, and expertise: from top management to middle managers and to lower level workers. Complex GDN activities are often carried out with incomplete and even inaccurate knowledge. Interdependent knowledge fragments are generated and stored in isolated documents. A history of the decisions and the analysis of changes would be helpful in improving task support [6]. With the objective of providing such a capability, many GDNSS (such as GroupSystems and Vision-Quest) supported the capture of informal knowledge exchanged during group discussions. Systems such as Constellations [29] have facilitated access to informal knowledge by chunking multimedia information. However, the capability to integrate knowledge fragments generated and used, especially of finegrained knowledge fragments, has received very little attention.

In summary, GDN requires:

1. formation of ad hoc groups of individuals participating in GDN and

2. integration of knowledge that is distributed and fragmented across different stakeholder locations.

Here, we present our approach to providing these capabilities, centered on the concept of traceability.

## 3. Traceability-augmented P2P support for GDN

## 3.1. Peer-to-peer networks for GDN support

P2P networks were developed to deliver seamless and comprehensive environments for group collaboration, discussion, and negotiation. They support spontaneous and secure group formation, messaging, presence management, and data synchronization [35] for mutual ‘‘exchange of information and service directly between peers to achieve purposeful results’’ [24]. P2P applications are ‘‘a class of applications that takes advantage of resources – storage, cycles, content, and human presence – available at the edges of the Internet’’ [33].

Differing markedly from client–server architecture, P2P networks consider each participating computer or node as equally important in providing information and service [3,22]. Instead of searching for information in a centralizedrepository, peers search across membernodes.

The characteristics of peer-to-peer networks that make them suitable for supporting GDNSS are:

 Flexibility and user control: They make it easy for users to create and use workspaces and tools that match their interaction styles and needs without the involvement of an administrator [11].

 Increased mobility: Participants are not bound to clients at fixed locations. The synchronization services ensure that changes made by participants will be propagated automatically to all members.

 Enhanced reliability: P2P applications replicate information at multiple nodes, providing redundancy and thus fault tolerance.

 Multi-level connections: It allows users to connect to only specific participants.

 Seamless and selective connectivity: Participants in negotiations can have easy access to others spread across the Internet.

Thus, P2P networks can effectively support several critical tasks. However, while they provide the physical links between nodes and facilitate sharing of documents, they provide only limited support for integrating knowledge fragments.

## 3.2. GDN models and traceability

We refer to traceability as the ability to represent various knowledge fragments and links among them. It facilitates the linking of discussions and negotiations to related knowledge fragments that are distributed in various peer nodes at a fine-grained level.

An important step was therefore the development of a GDN model that identified the knowledge fragments that needed to be integrated for GDN processes. We considered ARBAS, IBIS or their extensions and used ARBAS to illustrate how knowledge integration could be achieved in GDN.

The ARBAS primitives include actor, problem, argument, and proposition. Stakeholders can express their views on actions representing sentiment, opinion, belief, conviction, and persuasion. These are related to actions for which justifications (relating views to goals, constraints, facts, or assumptions) may be provided. ARBAS can be used to represent the history of negotiations through a chain of activities. The interactions between initial goals and alternative solutions result from communications between group members.

## 3.3. Supporting GDN requirements

We developed a prototype system (P2PTrac) whose functionalities have been mapped to logical and physical components in a P2P network, as shown in Fig. 1. Our prototype system augmented the support provided by current P2P networks and GDNSS with traceability.

## 3.4. P2PTrac architecture

Fig. 2 shows the architecture of our system. In this, a central or distributed repository can be used to store components of deliberations. Stakeholders from any peer node can access this through a client user interface. The stakeholders may link parts of their deliberations to associated knowledge elements that reside in their peer nodes. In essence, the P2P architecture provides the physical link between peers while our prototype system provides the logical knowledge network.

One of the peers hosts the tool services and the repository layers, which stores elements (for example, ARBAS) and knowledge fragments about deliberations represented as instances of the model. The tool services layer implements the algorithms that propagate changes across knowledge fragments and provides the protocols to communicate with other work productivity tools, such as Microsoft’s Outlook<sup>1</sup> and Word<sup>1</sup>. Finegrained linking of knowledge fragments is possible

![](/api/attachments/XDHBR6DW/fulltext/images/f071ef4d6a99f27020a8b7e6a1132f93d336c209aa1af33018e24b4bb014c09d.jpg)  
Fig. 1. Requirements for supporting GDN.

![](/api/attachments/XDHBR6DW/fulltext/images/8db9c965648afa3a6267a43a830799008d417600632a51b2e17e21fa56d19ae7.jpg)  
Fig. 2. Prototype architecture.

through the use of application programming interfaces (API) that are exposed by work process and productivity tools; this helps in linking knowledge fragments residing in parts of a document or an email message. The user interface layer provides a graphical interface for recording deliberations. The user interface of P2PTrac is installed in each peer node. The tool services and repository layer may also be present in multiple peers. The clients of a peer-to-peer tool (e.g., Groove ) are also installed in each peer to provide capabilities such as file sharing, document co-editing, instant messaging, calendar, scheduling meetings, conavigating the web, etc. P2PTrac uses APIs to access knowledge that resides within the various tools.

Table 1 shows how our system supports the various requirements by mapping them to the capabilities.

## 4. Supporting dynamic GDN with P2PTrac

## 4.1. A case study

The scenario represents an organization involved in outsourcing software development projects to offshore locations. The discussions involved four senior executives who have over 60 years of combined experience in GDN activities: two represented the client side and the others were from leading software development organizations, representing the vendor side.

Six teams, three representing each side participated in the process. Fig. 3 shows the scenario including interactions between peers and critical knowledge fragments that reside in different nodes. The arrows (from participants to documents) represent access to artifacts.

P2PTrac helped the process by:

1. Formation of ad hoc groups of individuals participating in GDN: Each of the teams formed a node in a P2P network. For simplicity, each was represented as a single node. However, multiple nodes could easily be constructed.

2. Integration of contextual knowledge that is distributed and fragmented across different stakeholder locations: We made it possible to link knowledge elements distributed across the peer nodes and allowed linking of finer fragments (a paragraph in a document, a cell in a spreadsheet, etc.) by creating links.

Table 1  
Mapping capabilities of our approach to GDN requirements

<table><tr><td colspan="2">GDN needs</td><td></td><td>Requirements for GDN</td><td colspan="3">Capabilities of P2PTrac</td></tr><tr><td rowspan="3">Formation of ad-hoc groups of individuals participating in GDN</td><td rowspan="3">Infrastructural Needs</td><td rowspan="3">Communication and collaboration</td><td>Communicating synchronously</td><td>Instant messaging, co-web navigation</td><td rowspan="3" colspan="2">Peer-to-peer networking</td></tr><tr><td>Communicating asynchronously</td><td>Offline messaging, asynchronous file sharing</td></tr><tr><td>Collaboratively creating and editing documents</td><td>File management, shared to-do lists</td></tr><tr><td rowspan="8">Integration of contextual knowledge fragments that are distributed and fragmented across different stakeholder locations</td><td rowspan="8">Logical Needs</td><td rowspan="2">Storage and Retrieval</td><td>Providing group memory</td><td>Shared repository of model element instances</td><td rowspan="2">Creation and use of knowledge repository</td><td rowspan="8">Traceability and Argumentation Support</td></tr><tr><td>Providing facility for retrieving past discussions</td><td>Discussion lookup</td></tr><tr><td rowspan="5">Traceability</td><td>Tracing among GDN model elements</td><td>Definition of links among argumentation model elements at a fine-grained level</td><td rowspan="5">Traceability support</td></tr><tr><td>Establishing consistency among arguments and reasoning</td><td>Maintenance of consistency across argumentation models and knowledge fragments</td></tr><tr><td>Tracing among knowledge fragments residing in distributed physical sources</td><td>Integration with work process tools: MS Word, Outlook, Project® Integration with P2P tool--Groove®</td></tr><tr><td>Tracing argumentation model elements to supporting GDN</td><td>Linking elements (ideas, concepts, etc) across multiple discussion</td></tr><tr><td>Replaying past negotiation</td><td>Retrieval and replay of relevant past knowledge</td></tr><tr><td>Structuring and Argumentation</td><td>Generating ideas and alternatives Classifying, prioritizing problems, constraints, and alternatives Explicating assumptions Evaluating options</td><td>Argumentation model definition Visual instantiation of arguments</td><td>Model support</td></tr></table>

## 4.2. A scenario of usage from the case study

Let us consider a specific negotiation scenario between the two parties involved in drafting an outsourcing contract. In this scenario, the vendor puts forward an offer backed by several estimates and plans as documented in a proposal. The ensuing discussion is captured in P2PTrac. The negotiation is focused on finalizing the contract after resolving conflicts in the project delivery schedule. The client initially may not agree with the proposed project schedule. To resolve this problem, the parties negotiate and consult with their inhouse teams. The client talks with its internal IT department to understand the rationale behind the estimates, to verify whether they are reasonable, and to decide whether the vendor’s development processes are sufficiently mature to ensure quality. The vendor talks to their development team to develop revised estimates. Finally, legal counsels from both parties work to produce a contract.

![](/api/attachments/XDHBR6DW/fulltext/images/d8dd184e9f78ee50b936037ca5cbce228c53ccff47fa1d80be8d72930cd1870b.jpg)  
Fig. 3. Selective sharing of knowledge across the parties involved in GDN.

## 4.3. Peer-to-peer networking

Communication and collaboration is handled primarily by the P2P network. The parties involved in the contract negotiation use P2PTrac to set up a virtual workplace where they can discuss their offers and share documents. Each participant has a Groove<sup>1</sup> client installed on his or her computer. Through the Groove<sup>1</sup> tools, the participants communicate synchronously or asynchronously and also co-edit proposal and contract documents.

## 4.4. Traceability and argumentation support

## 4.4.1. Argumentation model definition and visual instantiation of arguments

GDN model elements (in this case, ARBAS nodes and links) can be defined by using the GDN model editor (shown in Fig. 4). The participants can define additional primitives that are appropriate in their process. For example, in this scenario, ‘‘Agreement’’, ‘‘Assumption’’, ‘‘Contract’’, ‘‘Offer’’, and ‘‘Document’’ are user-defined primitives.

![](/api/attachments/XDHBR6DW/fulltext/images/437c370f7b7a21dd1b8c44d5bb99ba0c63a011abc5403f9ed133b27e8606041c.jpg)  
Fig. 4. GDN Model Editor used to define ARBAS primitives.

Fig. 5 shows the discussion using ARBAS. The top panel shows the primitives that may be used; below this is a session which illustrates a negotiation between the client and vendor on the delivery schedule. Knowledge fragments generated are created as nodes in P2PTrac using the toolbar buttons. The actors involved in the process and the documents generated and used by them are shown. The complete discussion is structured as a network of concepts which are linked. The offers and proposals made by the vendor and the client are clearly identified. Alternative solutions proposed and evaluated by the participants are also shown.

## 4.4.2. Definition of links among argumentation model elements

Fig. 6 shows an example of how links are established. The ‘preliminary project plan’ node is linked to a section of a document that details the features under discussion. When the relevant document is selected, P2PTrac parses it and shows its sections in the ‘‘Read Document’’ window. Any section can thus be selected and linked to a specific knowledge element.

## 4.4.3. Maintenance of consistency across

## argumentation models and knowledge elements

Often the repercussions of changes in critical assumptions made during GDN are not well understood, leading to very costly mistakes and rework. For example, if an argument was made that the quality assurance processes of the vendor needed longer development time, the client would need to decide whether this mattered, more than its effect on the time-to-market.

When a knowledge element depends on others, P2PTrac rules propagate the effects of changes in one element on them. Thus a decision on whether to increase the project duration or to accept the vendor terms and conditions could be affected by the quality policy of the client organization. The QA department is consulted to ascertain whether outsourced development is evaluated using the same quality requirements as internal processes and the discussion could lead to a careful evaluation of the processes to be followed by the vendor. The vendor might agree to tailor parts of their processes to meet the client’s requirements and this requires a longer project duration to meet the quality requirements.

![](/api/attachments/XDHBR6DW/fulltext/images/44ccdeb44a2af4af2d3326eef39ec82cf8e40181e9ed0e575705300d5142895b.jpg)  
Fig. 5. Documenting the deliberations of the GDN scenario with P2PTrac.

The dependencies in the network of issues that are discussed, the various alternative solutions considered, and their justifications are captured and maintained by autonomous agents with different levels of formality. In the simple case, the system warns the user about changes in relevant negotiation elements that affect the decision. At the other extreme, changes to decisions may be automatically propagated.

## 4.4.4. Integration with work process and P2P tools

Fig. 7 demonstrates how a node in the GDN discussion is linked to a specific item in a Groove<sup>1</sup> tool.

Here, the problem related to the delivery schedule conflict has been linked to a meeting schedule in the calendar tool. Depending on the workspace, the user can link selected documents to any node in the model. For example, the quality assurance report from the client’s internal quality department may only be shared within the client’s peers, and not with the vendor’s negotiation team. But the legal counsel’s contractual details can be shared through the P2P network to the vendor’s legal counsel. The nodes in the GDN model may also be linked to emails that the client may have received from the vendor.

## 4.4.5. Linking elements across multiple discussions

Peers can create their own traceability networks. Each participant may create a private traceability network that is not shared with other parties but is linked to specific knowledge elements that are represented in the shared traceability network. A multi-level traceability approach can be used to support selective knowledge integration and sharing.

![](/api/attachments/XDHBR6DW/fulltext/images/9b3fd7b32570e3f37a27fb61eed1043132856b4e90a4f49f15eb12a322618802.jpg)

Fig. 6. Linking knowledge fragments to parts of an MS Word document.  
![](/api/attachments/XDHBR6DW/fulltext/images/4aaf45b237fde458fab6dad161e1af9d71a3c3806dd2fa818bddbea514428c97.jpg)  
Fig. 7. Integration of P2PTrac with Groove<sup>1</sup>.

## 4.4.6. Retrieval and replay of relevant past knowledge

Group memory that seamlessly integrates knowledge fragments is a valuable knowledge asset. In P2PTrac, users can retrieve discussion history on specific topics and replay relevant parts of the negotiation. For example, if the client or vendor wants to examine how a decision was reached, he or she can retrieve the arguments.

## 5. Qualitative evaluation of the prototype system

We conducted qualitative evaluation of our approach and tool by seeking feedback from the four senior executives who participated in the case study. The objective of this evaluation was to assess the usefulness of our approach. While this was a first step, more rigorous evaluation is ongoing.

P2PTrac was presented to the participants in the qualitative evaluation. Two executives were senior managers in three development centers located in three different countries. Two were senior executives from two of the largest software development firms in the world. All routinely participated in GDN activities using state-of-the-art information and communication technologies, including a P2P tool. The presentation included a demonstration of the various functionalities of P2PTrac. We solicited comments on the utility of the approach and the prototype system. Data were collected as qualitative comments. The following points summarize the feedback received:

1. Reducing overheads in collaboration: The usefulness of their current tools was constrained as they facilitated only sharing of files and applications rather than individual knowledge fragments. The participants thought that the P2PTrac, by providing finer levels of visibility and access could reduce the overhead of preparing multiple versions of documents.

2. Integration of contextual knowledge that is distributed and fragmented across different stakeholder locations: All participants thought that this would be useful in improving GDN activities and that integration of contextual knowledge about several decisions would be valuable: it would allow them to follow the evolution of the negotiation process and revisit or reevaluate critical decisions. The ability to manage the evolution of documents was identified as a very important feature. Further, documentation of knowledge at a finer level of granularity was also considered to offer great potential in accessing relevant knowledge as needed.

Overall, the participants indicated that they were likely to consider using our approach. However, they also identified some important concerns:

1. Scalability and robustness: Since our tool was a research prototype, the participants suggested that issues of scalability and robustness needed to be evaluated before it could be adopted in their projects.

2. Security and privacy: The participants also felt that successful negotiators valued the knowledge that provided them leverage over their counterparts; thus, security and privacy of the information was of utmost importance. However, P2P tools are beginning to incorporate security features and there is increased user confidence in the technology [30]. One of the participants suggested that P2PTrac may be readily used in his organization within the ‘‘client’’ side to support outsourcing projects.

3. Issues in organizational adoption: Study participants raised concerns about some of the common factors that are known to impact the adoption, acceptance, and continued use of a new approach to manage knowledge [20]. Since the proposed approach will significantly change the current knowledge processes, development of appropriate incentive schemes would be critical to successful adoption of the new approach. The current use of P2P tools is likely to increase user confidence in the technology and provide valuable lessons.

## 6. Discussion and conclusions

## 6.1. Contributions

We have presented an approach to augment current P2P tools with traceability to support GDN processes, emphasizing the importance of maintaining traceability among the various elements and knowledge fragments that reside in peer nodes. We described P2PTrac, our prototype system. It can be used to document GDN deliberations and establish traceability among elements and knowledge distributed in the peer-to-peer network.

In summary:

 We mapped the requirements for a GDN support system into specific functionalities necessary to support GDN activities, recognizing the ability to integrate fragmented knowledge as key to effective GDN.

 We utilized a traceability-augmented P2P system as a solution, developing a prototype system to meet these requirements and demonstrate its implementation.

 We demonstrated the use of our approach with scenarios drawn from a case study and conducted a qualitative evaluation of the usefulness of approach.

## 6.2. Implications

Our knowledge integration approach can aid in the development of important constructs related to knowledge practices that reduce the cognitive effort of participating in GDN effectively.

Practitioners involved in collaboration in domains such as large-scale software development outsourcing should consider the use of P2P network infrastructure. Though the overhead involved in documenting and integrating knowledge is a concern, our work demonstrated the potential of a new approach. It also has important implications for developers of collaboration support tools. Microsoft’s proposed incorporation of P2P into its operating system and work productivity tools like the MS Office Suite<sup>1</sup> may also be complemented by knowledge integration capabilities incorporated in P2PTrac.

## 6.3. Limitations

Generalization of our results must be made with caution. Security concerns are a significant barrier to the adoption of the P2P infrastructure. Also, individual participants may circumvent enterprise security measures (firewalls, access controls, etc.). However, establishing appropriate corporate security policies and providing necessary training can help avoid security accidents [2]. The loss of control of the corporate network is another source of concern, since individuals might set up direct connections with peers outside the corporation without the help and knowledge of administrators. Therefore, organizations need to adopt strict control policies regarding the deployment of P2P technology.

## Acknowledgement

This research was supported, in part, by a research grant from the Robinson College of Business, Georgia State University.

## References

[1] H.J. Ahn, H.J. Lee, K. Cho, S.J. Park, Utilizing knowledge context in virtual collaborative work, Decision Support Systems 39(4), 2005, pp. 563–582.

[2] J.E. Bailes, G.F. Templeton, Technical opinion: managing p2p security, Communication of the ACM 47(9), 2004, pp. 95–98.

[3] H. Balakrishnan, F. Kaashoek, D. Karger, R. Morris, I. Stoica, Looking up data in p2p systems, Communications of the ACM 46(2), 2003, pp. 43–48.

[4] K. Becker, A.P.T. Bacelo, The evaluation of GRADD: a GDSS supporting asynchronous and distributed meetings, The Sixth International Workshop on Groupware, 2000.

[5] A. Bharat, J. Stern, The effect of task complexity and conflict handling styles on computer-supported negotiations, Information & Management 37(4), 2000, pp. 161–168.

[6] H. Bhargava, R. Krishnan, A. Whinston, On integrating collaboration and decision technologies, Journal of Organisationa Computing 3, 1994, pp. 297–317.

[7] T.X. Bui, F. Bodart, P.-C. Ma, ARBAS: a formal language to support argumentation in network-based organizations, Journal of Management Information Systems 14(3), 1998, pp. 223–237.

[8] A.-M. Chang, T.-D. Han, Design of an argumentation-based negotiation support system, 28th Annual Hawaii International Conference on System Sciences, IEEE Computer Society, 1995.

[9] H.W. Chesbrough, D.J. Teece, When is virtual virtuous: organizing for innovation, Harvard Business Review 1996, pp. 66–73.

[10] V. Chiesa, G. Toletti, Network of collaborations for innovation: the case of biotechnology, Technology Analysis & Strategic Management 16(1), 2004, pp. 73–96.

[11] K.J. Chun, H.K. Park, Examining the conflicting results of GDSS research, Information & Management 33(6), 1998, pp. 313–325.

[12] J. Conklin, Designing organizational memory: preserving intellectual assets in a knowledge economy, 2001, last accessed on 4/ 17/2006, at: http://cognexus.org/dom.pdf.

[13] J. Conklin, M. Begeman, gIBIS: a tool for all reasons, Journal of the American Society for Information Science 40, 1989, pp. 200–214.

[14] A.R. Dennis, C. Tyran, D.R. Vogel, J.F. Nunamaker, Group support systems for strategic planning, Journal of Management Information Systems 14(1), 1997, pp. 155–184.

[15] A.R. Dennis, C. Tyran, D.R. Vogel, J.F. Nunamaker, Group support systems for strategic planning, Journal of Management Information Systems 14(1), 1997, pp. 155–184.

[16] J. Fulk, G. DeSanctis, Electronic communications and changing organizational forms, Organization Science 6, 1995, pp. 337– 349.

[17] M.v. Genuchten, C.v. Dijk, H. Scholten, D. Vogel, Using group support systems for software inspections, IEEE Software, May/ June, 2001.

[18] W.D. Haseman, D.L. Nazareth, S. Paul, Implementation of a group decision support system utilizing collective memory, Information & Management 42(4), 2005, pp. 591–605.

[19] N. Karacapilidis, D. Papadias, C. Pappis, Computer-mediated collaborative decision making: theoretical and implementation issues, 32nd Hawaii International Conference on System Sciences, 1999.

[20] E. Karahanna, D.W. Straub, N.L. Chervany, Information technology adoption across time: a cross-sectional comparison of pre-adoption and post-adoption beliefs, MIS Quarterly 23(2), 1999, pp. 183–213.

[21] J. Kotlarsky, H. Oshri, Social ties, knowledge sharing and successful collaboration in globally distributed system development projects, European Journal of Information Systems 14(1), 2005, pp. 37–48.

[22] J. Kubiatowicz, Extracting guarantees from chaos, Communications of the ACM 46(2), 2003, pp. 33–38.

[23] E.F. McDonough III, K.B. Kahn, G. Barczak, An investigation of the use of global, virtual, and colocated new product develop-

ment teams, Journal of Product Innovation Management 18(2), 2001, pp. 110–120.

[24] D. Moore, J. Hebeler, in: F.j. Kelly (Ed.), Peer-to-Peer: Building Secure, Scalable, and Manageable Network, McGraw-Hill/ Osborne, Berkeley, 2002.

[25] J.P. Nunamaker, A.R. Dennis, J.S. Valacich, D.R. Vogel, J.R. George, Electronic meeting systems to support group work, Communications of the ACM 34(7), 1991, pp. 40–61.

[26] G. Piccoli, B. Ives, Virtual teams: managerial behavior control’s impact on team effectiveness, International Conference on Information Systems, Brisbane, Australia, 2000.

[27] B. Ramesh, M. Jarke, Towards reference models for requirements traceability, IEEE Transactions on Software Engineering 27(1), 2001, pp. 58–93.

[28] B. Ramesh, A. Tiwana, Supporting collaborative process knowledge management in new product development teams, Decision Support Systems 27(1–2), 1999, pp. 213–235.

[29] V.S. Rao, R. Goldman-Segall, Capturing stories in organisational memory systems: the role of multimedia, 28th Annual Hawaii International Conference on System Sciences, 1995.

[30] A. Ricadela, Microsoft’s groove move, Information Week, 2005.

[31] S. Sarker, S. Sarker, D.B. Nicholson, K.D. Joshi, Knowledge transfer in virtual systems development teams: an exploratory study of four key enablers, IEEE Transactions on Professiona Communication 48(2), 2005, pp. 201–218

[32] M. Schoop, A. Jertila, T. List, Negoisst: a negotiation support system for electronic business-to-business negotiations in ecommerce, Data & Knowledge Engineering 47, 2003, pp. 371–401.

[33] C. Shirky, What is p2p? And what isn’t?, 2001, last accessed on, at: http://www.openp2p.com/pub/a/p2p/2000/11/24/shirky1- whatisp2p.html.

[34] J. Suchan, G. Hayzak, The communication characteristics of virtual teams: a case study, IEEE Transactions on Professional Communication 44(3), 2001, pp. 174–186.

[35] J. Udell, Uniting under groove, Infoworld, February 2003.

[36] W.J.H. Van Groenendaal, Group decision support for public policy planning, Information & Management 40(5), 2003, pp. 371–380.

[37] K.R. Walsh, M.H. Dickey, Structured modeling group support systems: a product design theory, Information & Managemen 41(5), 2004, pp. 655–667.

[38] D. Windsor, International virtual teams: opportunities and issues, Advances in Interdisciplinary Studies of Work Teams 8, 2001, pp. 1–39.

[39] Y. Xiao, Artifacts and collaborative work in healthcare: methodological, theoretical, and technological implications of the tangible, Journal of Biomedical Informatics 38(1), 2005, pp. 26– 33.

![](/api/attachments/XDHBR6DW/fulltext/images/00937f0e9d6f70be906604a94f2113bde15d15cfbe20a84b058c2c16d3d0d629.jpg)

Kannan Mohan is an assistant professor of Computer Information Systems at Baruch College. Dr. Mohan received his PhD degree in Computer Information Systems from Georgia State University. His research interests include managing software product family development, providing traceability support for systems development, knowledge integration, and agile development methodologies.

![](/api/attachments/XDHBR6DW/fulltext/images/27e832d61f5c992cac1bd36bf1c5b5df8b28031b15f54cdcaa96a6bc5bc9ddc9.jpg)

Peng Xu is an assistant professor at the Department of Management Science and Information Systems of the University of Massachusetts Boston. She received her PhD in Computer Information Systems from Georgia State University in 2004. Her work has appeared in several conferences and journals including the Requirements Engineering Journal, Communications of the ACM, WITS, and HICSS. Her research areas

are software process, project management, software engineering, and knowledge management

![](/api/attachments/XDHBR6DW/fulltext/images/589ca31860e38d4b8162265862326c3027141c12411a4afcb1a070c7e7319487.jpg)

Balasubramaniam Ramesh is a professor of Computer Information Systems at Georgia State University. Dr. Ramesh received his PhD degree in Information Systems from New York University. His research work has appeared in several leading conferences and journals including the IEEE Transactions on Software Engineering, MIS Quarterly, Communications of the ACM, JAIS, IEEE Expert, IEEE Computer, IEEE Intel-

ligent Systems, IEEE Internet Computing, Annals of Software Engineering, Annals of Operations Research, and Decision Support Systems among others. His research interests include supporting complex organizational processes in areas such as requirements engineering and traceability in systems development, concurrent engineering, NPD, knowledge management, and business process redesign.
