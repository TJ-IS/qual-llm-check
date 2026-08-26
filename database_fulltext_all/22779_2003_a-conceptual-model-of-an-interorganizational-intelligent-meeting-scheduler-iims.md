---
otero_id: 22779
otero_key: "GMYNAKKC"
title: "A conceptual model of an interorganizational intelligent meeting-scheduler (IIMS)"
authors: "Chanan Glezer"
year: "2003"
journal: "The Journal of Strategic Information Systems"
doi: "10.1016/s0963-8687(02)00034-3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/jsis

# A conceptual model of an interorganizational intelligent meeting-scheduler (IIMS)

Chanan Glezer

Department of Information Systems Engineering, Ben-Gurion University of the Negev, Beer Sheva 84105, Israel

Accepted 19 November 2002

## Abstract

This article proposes and evaluates a comprehensive agent-based architecture for an Interorganizational Intelligent Meeting-Scheduler. The article extends and generalizes the Intelligent Meeting-Scheduler conceptual model [EXPERSYS 95-Proc. Seventh Intl Conf. Artificial Intelligence Expert Syst. Appl. (1995) 279; J. Organizational Comput. Electron. Commerce, 9 (1999) 233] which focused on intraorganizational meeting scenarios.

First, the article reviews several academic meeting-scheduling prototypes and commercial software packages. Based on this review, it is demonstrated that only an integrated approach tha supports interoperability in all three dimensions of the meeting-scheduling problem (calendar, scheduling, and communication-management) can succeed in achieving interoperability among heterogeneous calendar and scheduling systems.

The next part of the article provides a specification of an agent-based system that attempts to address the interoperability challenge. The specification comprises of the following elements: environment, behaviors, symbol-level, and knowledge-level architectures [IEEE Trans. Syst., Man, Cybernet. 25 (1995) 852]. The inter-organizational meeting-scheduling process is articulated as an iterative negotiation process where knowledge and symbol level units (‘the IIMS system’) interact with the system’s end-users (‘the environment’) by exhibiting behaviors that address end-user requirements.

The IIMS conceptual model is evaluated empirically and related to relevant literature on adoption difficulties of inter-organizational systems. It is evident that the IIMS faces a plethora of technological, organizational, sociological, behavioral, and psychological challenges that hinder its successful adoption. The article proposes several implementation tactics and guidelines in order to overcome these obstacles.

q 2003 Elsevier Science B.V. All rights reserved.

Keywords: Meetings; Group-tasks; Meeting-scheduling; Interoperability; Human resource management (HRM); Calendars; Software agents; Inter-organizational systems (IOS)

## 1. Introduction

## 1.1. Background

Whenever two or more people need to communicate at the same time, a meeting needs to be scheduled. Meetings are a major liaison device for achieving mutual adjustment in organizations (Mintzberg 1979). Huber (1990) views meetings as a tool that facilitates efficiency in the exchange of information among people. Malone and Crowston (1994) view the meeting-scheduling task as an organizational coordination mechanism that handles simultaneity constraints.

Several commercial software packages (Smith and Eglowstein 1994; Grudin and Palen 1995; Palen 1999; Mosier and Tammaro 1997) as well as academic prototype systems (Beard et al., 1990; Sen and Durfee 1991, 1992, 1993a,b; 1994a,b; Sugihara et al., 1989; Glezer and Yadav 1995, 1999; Pino and Mora 1998; Greif and Sarin 1987) attempt to provide assistance during the meeting-scheduling process. Web-based products such as Lotus Notes (Florio 1999a,b), Netscape Calendar, and Yahoo Calendar provide a variety of powerful features including global access, integration with event databases, to-do lists, group calendars, and synchronization capabilities with organizer mobile devices. The main emphasis and evaluation approach of these meeting-schedulers is summarized in Table 1. The software packages and academic prototypes mentioned in Table 1 assume an intraorganizational meeting scenario scheduled in a homogeneous organizational environment.

With the adoption of the Internet as an underlying global information infrastructure, organizations need to collect and disseminate more and more information in a timely fashion in order to make effective and competitive decisions (Carstensen and Sorensen, 1996).

Developments in the area of electronic commerce and mobile telecommunication technology as well as increased traveling have created an ‘interoperability challenge where people are more than ever dislocated from relevant information sources and need to integrate information from an increasing number of heterogeneous information sources.

The ‘interoperability-challenge’ applies to the common task of meeting-scheduling because people schedule more and more meetings with people whose calendars are stored in remote locations and are represented in heterogeneous formats. The need to share and synchronize calendars creates major technological challenges with respect to both inter- and intra-organizational meetings.

## 1.2. Problem statement

Several attempts have been made to overcome the interoperability challenge in calendar and scheduling systems. As an example, the Internet Engineering Task Force (IETF) has formed a working group on calendar and scheduling<sup>1</sup>, which proposes various standards for storing and exchanging temporal data between heterogeneous calendar and scheduling systems. The OSKI standard<sup>2</sup> serves as an ‘Open Shared Kalendaring Infrastructure’ that provides calendar services for groups of people equipped with disconnected and connected devices.

Table 1 Summary of key extant meeting-schedulers

<table><tr><td>Work/authors on meeting-scheduling problem</td><td>Model/major emphasis in the work</td><td>Methodology/evaluation approach</td></tr><tr><td>Grace Pino and Mora (1998)</td><td>Latitude model based on participants&#x27; preferences</td><td>Modeling and illustration of a scheduling process using a prototype</td></tr><tr><td>Distributed meeting-scheduler (DMS) Sen and Durfee (1994a,b; 1993a,b; 1992, 1991)</td><td>Distributed multistage negotiation</td><td>Experimental verification of a mathematical negotiation model</td></tr><tr><td>Visual calendar Beard et al. (1990)</td><td>Transparency metaphor</td><td>Illustration and evaluation of a visual metaphor model using a prototype</td></tr><tr><td>Meeting-scheduler for office automation Sugihara et al. (1989)</td><td>Timetable rearrangement (TR)</td><td>Experimental verification of a mathematical optimization model</td></tr><tr><td>MPCAL Greif and Sarin (1987)</td><td>Controlled sharing of calendars using roles and proposals</td><td>Evaluation of research prototype</td></tr><tr><td>RTCAL Greif and Sarin (1987)</td><td>Real-time conferencing using blackboard</td><td>Evaluation of research prototype</td></tr><tr><td>Commercial meeting-schedulers: Microsoft schedule + , Sun calendar manager, ca up-to-date, Lotus organizer and notes R5, meeting maker 1.5 Yahoo and Netscape calendar and scheduling systems Grudin and Palen (1995), Palen (1999), Smith and Eglowstein (1994), Mosier and Tammaro (1997) and Florio (1999a,b), calendar.yahoo.com, home.netscape.com/calendar/index.html)</td><td>Boolean overlaying of calendars</td><td>Specifications of commercial meeting-schedulers and comparison of commercial meeting-schedulers (mostly using surveys and interviews)</td></tr></table>

Nevertheless, achieving effective interoperability between such systems is a very complex task that also demands exchanging knowledge about organizations’ structure and functionality. Such knowledge includes business process descriptions, portions of organizational charts, problem tables, organizational goals, and individual qualifications of employees per relevant business processes. In order to ensure effective interoperability among meeting-schedulers, the above knowledge elements, termed ‘organizational knowledge’ (Nonaka 1994; Nonaka and Takeuchi, 1995; Spender, 1996), need to be shared and used for activities such as meeting-content planning and group composition (Glezer and Yadav 1999).

Existing calendar and scheduling interoperability standards do not adequately address the organizational knowledge sharing aspect described above. In addition, providing a comprehensive solution to the ‘interoperability challenge’ is important because it is expected to resolve the ‘partial use’ problem and enable a wide adoption of calendar and scheduling systems (Grudin and Palen 1995; Mosier and Tammaro 1997). Adopting open, interoperable calendaring and scheduling systems such as Sun’s Calendar Manager creates new opportunities for social coordination because employees can make interpretations about their peers’ schedules, and potentially reduce negotiation efforts and interruptions (Palen 1999).

## 1.3. Research objectives

The objectives of this paper are as follows:

1. To review the extant work on interoperability standards and protocols in calendar and scheduling systems.

2. To propose and evaluate an agent-based conceptual model for an Interorganizational Intelligent Meeting-Scheduler (IIMS) that addresses the ‘interoperability-challenge’.

## 2. Related work on groupware and interoperability standards

Groupware systems are information systems that support collaboration and information sharing among people in organizations. In terms of operation scope, they are positioned between organizational information systems and personal computing. Groupware systems are unique in that their successful adoption in organizations involves social, political and motivational factors that extend beyond their technological quality and compatibility (Grudin, 1994).

Schmidt and Simone (1996) describe the complex interdependencies between individual activities in the modern industrial society and the difficulty in articulating these interdependencies, which poses a major challenge to groupware systems. Coordination mechanisms (Schmidt and Simone, 1996; Carstensen and Sorensen, 1996) serve as the underlying concept in designing groupware systems. Coordination mechanisms can be conventional (paper-based) or computational. Schmidt and Simone (1996) mention malleability and linkability as necessary requirements from coordination mechanisms. Malleability refers to the ability of ‘actors’ (users) of the coordination mechanism to define and modify the protocol used by the mechanism. Linkability refers to the ability of a coordination mechanism to interact with other coordination mechanisms using the idea of a general notation (Schmidt and Simone, 1996).

Group Calendaring and Scheduling (C&S) systems are a common class of groupware. They are well established for organizational use, however, in most cases are limited to the exchange of information among users of the same system within the boundaries of a single company<sup>3</sup>.

Universal standards for C&S applications have yet to be defined as current C&S applications use their own proprietary communication protocol, making it impossible for these applications to inter-operate without appropriate software-based gateways (Hanseth and Monteiro, 1998). The lack of calendaring and scheduling interoperability standards has resulted in the following interoperability problems<sup>4</sup>:

† Users are unable to choose their own calendaring and scheduling application but rather are required to conform to standards set by the organization.

† Users of one calendaring and scheduling system cannot communicate with users of a different system.

† Users cannot easily reconcile information between their personal organizers and their desktop C&S system.

The IETF Calendaring and Scheduling working group was formed in order to propose standards that will address the above problems and has recently approved a set of standards that are now being adopted by the Netscape Calendar Server system. These standards deal with storage and retrieval of temporal data (calendar management), and with connectivity among parties in a C&S system (communication management)<sup>4</sup>.

In another implementation of an interoperable C&S system, the Vcalendar standard was used to implement a Disconnected Wide-Area Group Calendar Service named OSKI<sup>2</sup> (‘Open Shared Kalendaring Infrastructure’). OSKI is a scalable, easily accessible, and fault-tolerant service that provides calendar services for groups of people.

In the area of calendar management, OSKI makes it possible to locate all copies of a user’s calendar, retrieve them, and integrate them to a single calendar based on the access privileges of the requestor. In the area of communication management, OSKI adopts the Palm OS resolution strategy for disconnected services<sup>5</sup>.

In a recent attempt to provide interoperability across wireless mobile platforms, SyncML<sup>6</sup> was developed in order to serve as a common language for synchronizing devices and applications across any network. SyncML leverages Extensible Markup Language (XML) in order to provide interoperability in the area of communication management by synchronizing back and forth any mobile device with any stationary networked application.

Based on the literature surveyed above, it is evident that previous work focuses on providing interoperability in the areas of calendar and communication management. Much less attention has been paid to providing interoperability in the area of scheduling management, namely, the sharing of relevant knowledge among participating organizations. This knowledge is required in tasks that promote the creation of a Shared Context (Pendergast and Hayne, 1995) such as meeting-content planning and effective group composition (Glezer and Yadav 1995, 1999).

The purpose of this article is to fill a gap by proposing and evaluating a balanced and adaptive agent-based architecture for an IIMS. The IIMS addresses the ‘interoperability challenge’ concurrently in three dimensions inherent to the meeting-scheduling task, namely calendar, communication and scheduling management. The IIMS adopts the IETF standards and proposes new mechanisms for sharing and mediating organizational knowledge among the organizations participating in the meeting-scheduling session. The following section provides a detailed specification of the IIMS conceptual model.

## 3. A conceptual model of an interorganizational intelligent meeting-scheduler

The IIMS model is based on the research methodology proposed by Baldwin and Yadav (1995). Following this methodology, the IIMS conceptual model is constructed to enable interoperability among heterogeneous organizational units during a meeting-scheduling process. An organizational unit is defined as a group of people sharing the same type of calendar and scheduling system. Therefore, inter-organizational meeting-scheduling refers to a scenario involving two or more heterogeneous C&S systems. Such systems may be used by different companies, divisions, departments or even virtual cross-functional teams in a single company. On the other hand, intra-organizational meeting-scheduling involves the assembly of a meeting in a homogeneous environment and was addressed by the IMS model (Glezer and Yadav, 1995, 1999).

The IIMS conceptual model is composed of symbol level and knowledge level units. It concurrently interacts with its organizational environment by producing behaviors that are derived from the host and invitee user-requirements. These user-requirements are oriented towards the environment of the IIMS, and specify the expectations of the above end-users on what the system should be capable of doing for them. The behaviors are a translation of user-requirements to a set of internal and functional clusters of activities, which are activated on demand in order to meet the user-requirements (Baldwin and Yadav, 1995).

The symbol level architecture of the IIMS is based on the notion of software-agents (Genesereth and Ketchpel, 1994). These agents are distinct and autonomous software components that interact among themselves and with the external environment by exchanging messages during a meeting-scheduling session. The knowledge level architecture of the IIMS consists of a segregated collection of knowledge units used by different IIMS functional agents.

Following is a detailed specification of the elements used to compose the IIMS conceptual model. The description emphasizes how intra- and inter-organizational meeting-scheduling differ and how they are related.

## 3.1. The inter-organizational meeting-scheduling process

Scheduling meetings in a single organization involves a sequence of interrelated steps. The meeting-scheduling task has a distributed nature, where a host assumes responsibility for collecting and disseminating the necessary information in an iterative process until mutual agreement is achieved over a meeting time-slot.

Fig. 1 depicts a general workflow-type sequence of steps of an inter-organizational meeting-scheduling process. This sequence is not meant to be a strict one. By using process-script stored in the IIMS, the system could easily customize the scheduling process in order to fit a specific meeting context. As an example, in the case of committeetype meeting, there is no need to go through the group composition stage and this step is skipped (Glezer and Yadav, 1999).

![](/api/attachments/GMYNAKKC/fulltext/images/050a889479430e703b8687ef0fb01b9d2f8037d4ed0c0a6fdf85600ae1915e37.jpg)  
V Invoke sharing of organizational knowledge with other organizations

\* Identify a pool of candidate invitees and then optimize by assembling the most effective (optimal) sub-group. Optimization is based on the fit between the planned meeting-content and the recorded qualifications of the candidates.

Fig. 1. The interorganizational meeting-scheduling process.

Capturing the inter-organizational meeting-scheduling process using workflow technology is complex because it requires a delicate balance between a ‘from-within and ‘from-without’ work process perspectives in its design (Bowers et al. 1995). The former perspective emphasizes the current work practices, while the latter emphasizes the organization demands relative to what the authors call (inter-organizational) accountability. This consideration leads to the definition of a basic requirement for technological support, namely, the capacity to take into account both perspectives and their interaction in a flexible way by providing the means for partial specification and incremental design of the work process support (Bowers et al., 1995).

The first step in the meeting-scheduling process is to select an appropriate person, named host, who is in charge of assembling the meeting. After selecting the host, the next step is to select the most suitable organizations that should be represented in the meeting and therefore participate in the meeting-scheduling process. As soon as the participating organizations are selected, the meeting-schedulers in these organizations become brokers that link the host with the invitees from these organizations. The IIMS also has to collect and store relevant organizational knowledge (Nonaka 1994; Nonaka and Takeuchi, 1995; Spender, 1996) regarding the selected participating organizations. After all this is done the host can proceed with the negotiation process which includes organizing the activities of meeting content planning, group composition, time slot searching and solution evaluation.

A major difference between the intra- and inter-organizational meeting-scheduling process is that the latter requires an autonomous inter-organizational knowledge sharing mechanism (bottom left of Fig. 1). This mechanism is part of the ongoing knowledge creation process involving ‘actors’ that perform knowledge-internalization and externalization (Nonaka, 1994). These activities transform knowledge elements from tacit to explicit formats. Organizational knowledge creation is an upward spiral process, which starts at the individual level and moves towards the creation of group, organizational and inter-organizational knowledge (Nonaka, 1994). The creation and sharing mechanisms of inter-organizational knowledge is in the focus of the IIMS model.

When evaluating a solution after a scheduling iteration, the host decides whether to invoke a concurrent knowledge sharing mechanism that selectively propagates to partner organizations some new knowledge elements received or discovered during the most recent cycle of the meeting-scheduling process. This knowledge includes organizational charts, process flows, personnel records, and goals. The organizational knowledge is transferred across the inter-organizational network to other organizations in order to facilitate interoperability among C&S systems. As a result, organizations can reveal a portion of their knowledge to their immediate ‘neighbors’ and this knowledge can be further propagated to other organizations by passing through a chain of transit organizations.

The knowledge propagation process is controlled by a set of rules where each organization has to publish the types of knowledge it is willing to ‘subscribe to’ from other organizations. For example, let us say that company A informs company B that it is interested in the organization chart of company C. Consequently, if during an interorganizational meeting-scheduling session, company B receives from company D the organization chart of company C it will pass it on to company A. This capability is expected to gradually improve the effectiveness and efficiency of the meeting-scheduling process because the selection of external invitees will be based on more concrete knowledge.

## 3.2. Environment (E)

The environment of the IIMS (Fig. 2) consists of two dimensions. The first dimension includes a set of meeting scenarios. Each scenario comprises a meeting-scheduling problem that a host has to solve with assistance from the IIMS. The scenarios can include meetings, seminar, workshops and conferences (Weirich 1992).

The second dimension, the inter-organization, includes the organizations participating in the session and their characteristics (e.g. domestic or international), and the type of relationships with the host organization and among themselves (e.g. customer-supplier). The environment can be illustrated as an interconnected network of links between the participating organizations indicating the role an organization plays in each link.

The main implication of the inter-organizational environment is the need for synchronization among the organizational knowledge bases of participating organizations. For an intra-organizational meeting scenario we assume that knowledge in the system is maintained by in-house transaction processing systems and that it is easily accessible to employees within the organization. In an inter-organizational meeting, however, we need a mechanism that enables participating organizations to share calendars and other organizational knowledge units among themselves based on predefined rules. It is possible that a relationship among participating organizations will be permanent and independent from a certain meeting-scheduling scenario.

Environment:

![](/api/attachments/GMYNAKKC/fulltext/images/2d699c9388f86775cc1952dc63b48f86368528a46dd662a6333002e134579de8.jpg)  
Fig. 2. Components of the IIMS environment.

## 3.3. Behaviors (B)

Based on the inter-organizational meeting-scheduling process described above, five clusters of behaviors (functions) are synthesized for the IIMS. These clusters are responsible for providing control management, temporal data management, scheduling management, internal, and external communication management. The organizational knowledge is captured and maintained by the scheduling management cluster. In order to handle inter-organizational meeting scenarios, the IIMS provides capabilities that expand communication links to partner organizations, exchange knowledge units with such organizations and reconcile conflicts between various organizational schemas. Table 2 depicts a detailed list of IIMS behaviors.

## 3.4. Knowledge level architecture (K)

This section describes the knowledge needed by the IIMS to handle the interaction with external organizations. Fig. 3 depicts the knowledge units clustered according to the IIMS functions. The description emphasizes (see bold face) the inter-organizational aspects of the knowledge architecture. In order to support the inter-organizational behaviors presented in Table 2, we need knowledge that support the calendar, communication, and scheduling interoperability.

For calendar interoperability, the standards developed by IETF are adopted in order to exchange invitations and replies, drag-and-drop calendar objects, and synchronize handheld calendar copies.

For communication interoperability, we need to maintain a description of the environment as a list of potential partner organizations recognized by the IIMS. This list includes a brief description of the organizational profile of each partner and its location in the underlying communication network. This directory-based service can be implemented using a system such as the Open Lightweight Directory Access Protocol (www.openldap.org).

For scheduling interoperability we need mainly an inter-organizational knowledge management mechanism (IOKM) which includes the following characteristics:

† A mechanism for creating and storing a unified schema between the host organization and other organizations using mediating keywords (schema integration/reconciliation).

† A mechanism for sharing and propagating organizational knowledge among participating organizations (knowledge sharing/propagation).

The unified schema integrates a portion of the organizational databases of the host organization with the database of one (or more) other participating organizations using standardized keywords. As an example, if a host specifies a meeting to deal with preparing a mutual marketing plan for an alliance between two airlines then the unified schema includes organizational charts for the marketing divisions of the airlines, as well as relevant work processes, problems, goals and records of suitable employees. The unified schema (see Fig. 4) is constructed using mediating keywords that ‘bypass’ organizational boundaries and enable the IIMS to reconcile differences between the organizational databases of participating organizations.

Table 2 Functions and related behaviors of the IIMS

<table><tr><td>Function</td><td>Behaviors (B)</td></tr><tr><td>Control management</td><td>1: Request services for handling temporal data2: Request services for scheduling a meeting3: Request services for maintenance and tuning</td></tr><tr><td>Temporal data management</td><td>1: Maintain calendars for people, equipment and groups2: Manage temporal constraints for people, equipment and groups3: Provide add-on services (e.g. ‘to do lists’, automatic reminders)4: Support distributed calendar management</td></tr><tr><td>Scheduling management</td><td>1: Select host organization and individual2: Select participating organizations3: Plan meeting-content using organizational knowledge4: Identify potential invitees for a given meeting-content5: Rank potential invitees for a given meeting-content6: Form most effective group with the highest expected effectiveness, or lowest expected conflict for a given meeting-content7: Search for a feasible meeting time-slot using search strategies8: Consult with invitees to evaluate a time-slot9: Evaluate responses of invitees10: Invoke inter-organizational knowledge sharing process11: Commit calendars to a time-slot12: Maintain group-composition matrices</td></tr><tr><td>Intra-organizational communication management</td><td>1: Deliver a message or knowledge unit within the organization2: Maintain the intra-organizational communication network</td></tr><tr><td>Inter-organizational communication management</td><td>1: Identify and choose candidate organizations for a scheduling session2: Construct a unified schema for a scheduling session3: Deliver a message or knowledge unit to an external invitee4: Propagate an organizational knowledge unit to another organization5: Publish own rules about knowledge interests to other organizations</td></tr></table>

The IIMS is therefore capable of planning a meeting’s content and selecting invitees who match that content from more than one organization. The selection of employees for a given inter-organizational meeting-content is performed in the following two modes:

† ‘Distinct’: Participating organizations are treated as separate entities. The host has access to a list of knowledge units retrieved for each organization based on common keywords provided at the beginning of the scheduling session. The selection of invitees is separate for each organization (see Fig. 4).

† ‘Pooled’: Participating organizations are treated as a virtual unified entity for certain organizational knowledge units. As an example, the host or the IIMS can introduce hierarchy into the unified schema by defining the goals ‘market share’ of airline 1 and ‘profit/quarter’ of airline 2 to be equivalent. Consequently, if there is a calendar conflict \*\* The Calendar knowledge base includes calendars of external invitees.

![](/api/attachments/GMYNAKKC/fulltext/images/52ea20e494faf6ec8b6bcd66e01716c01904cf16ca7a531fb23cd2c085c635be.jpg)  
\* For a detailed description of the calendar, scheduling and internal communication knowledge bases please refer to (Glezer and Yadav, 1999)

Fig. 3. Knowledge Level architecture of the IIMS .

for invitees in the most effective group, a ‘blocking invitee’ may be replaced by another invitee even if he or she is from a different organization.

In order to construct and use a common schema, we need to maintain an index of keywords that maps the organizational database of each IIMS. The index will point to related knowledge units within an organizational database. The index should be updated to ensure quality of the group composition process.

The need for a schema integration/reconciliation mechanism is supported by findings from a case study in which a CAD system was used by a textile supply chain (Holland,

![](/api/attachments/GMYNAKKC/fulltext/images/4a47f9e0890a29ce2dcf72b9c8bf4516985d8e752f0bb40134f7ba322b069b89.jpg)  
Fig. 4. Example of a unified schema created by the IIMS.

1995). The study showed that standards of the CAD technology and shared access to the CAD system expedited sharing of new designs for clothes between the mill, the textile stores, and the chain stores, which formed an integrated supply chain.

The knowledge sharing/propagation mechanism is a very effective tool for expediting the meeting-scheduling process. This mechanism consists of two complementary processes:

† Propagation (Push): This specifies the frequency and types of knowledge to be shared with other organizations. After each scheduling iteration (see Fig. 1), every IIMS looks at new knowledge units it received and decides based on knowledge sharing rules (see Fig. 3) whether peer organizations might be interested in this knowledge. Based on this decision, the knowledge is propagated to these organizations.

† Subscription (Pull): Each IIMS has to transfer to other IIMSs the types of knowledge it wishes to be updated on and the frequency of the updates. The most appropriate types of organizational knowledge to be shared among partner organizations are marketing and operations management processes, organizational charts, and culture attributes (such as expected punctuality in meetings). Both propagation and subscription rules are stored in element d. of the Interorganizational Interoperability Knowledge in Fig. 3.

A major challenge in implementing the knowledge sharing mechanism is to determine the proprietary knowledge that should be propagated among participating organizations who may actually be competitors.

## 3.5. Symbol level architecture (S)

The architecture of the IIMS at the symbol level is based on the notion of Software-Agents (Genesereth and Ketchpel 1994). In this section the notation of S.x is used to denote a software-agent and L.x to denote a link that is used to transmit information (data and messages) between agents.

Fig. 5 depicts the symbol level IIMS architecture. We see that the system actually operates in a hierarchical mode. The Control-Manager (S.1) serves as the underlying coordinator that handles the interaction with the host. It is in charge of coordinating and activating its two subordinate functional agents: the Calendar-Manager (S.2) and the Scheduling-Manager (S.3).

At a lower layer, the Intra-organizational Communication-Manager (S.4) and Interorganizational Communication-Manager (S.5) serve as supporting agents for both the Scheduling and Calendar Managers. The Intra Communication-Manager is mainly responsible for providing connectivity within the boundaries of an organizational network (e.g. transmitting calendars, announcing meetings and collecting responses). The Inter Communication-Manager is in charge of external connectivity, which crosses the boundaries of an organization. It stores and disseminates relevant knowledge units among different organizations and operates the knowledge sharing mechanism.

Each of the four functional agents has a supporting knowledge base, which is maintained by a corresponding knowledge base management agent. To simplify the illustration, the knowledge base management agents are represented by the lines connecting the knowledge bases with their functional owner agents. All agents interact via messages that travel through communication links. A chain of several communication links is called a communication path. Each agent has an internal working area, an input queue for entering messages, and an output queue which is used to activate other agents or submit responses to a calling agent. The inter-organizational links include L.5, and L.8–L.10.

L.5 is used to transmit and receive calendars for employees in external organizations. These calendars are stored in a special area designated for external employees within the calendar knowledge base. L.8 is used by the Scheduling-Manager to access the unified schema stored under S.5 and to interact with external employees during the scheduling session (e.g. to announce a meeting and collect responses). L.9 is used to convert messages from the inter-organizational communication network to the intra-organizational network and vice versa. Finally, L.10 is used to interact with other IIMSs.

## 4. Evaluation of the IIMS model

In order to gain insight about the practical value of the proposed IIMS model, an interview was conducted with a former senior manager of Merger and Acquisitions in a major American global investment bank. The area of Merger and Acquisitions is appropriate for testing the IIMS model because it involves many interorganizational meeting scenarios in a dynamic, heterogeneous and very competitive environment.

![](/api/attachments/GMYNAKKC/fulltext/images/eff13ba9309447059fe0606f0dd7cbdd3f16a38738c9507c2039dfb1c23a3672.jpg)  
KBMS=Knowledge Base Management System  
\* Running on desktop or handheld device

Fig. 5. Symbol level architecture of the IIMS.

First, the IIMS model was presented in detail to the manager, followed by a set of questions regarding the validity of the following elements in the model: interorganizational meeting-scheduling process (Fig. 1); inter-organizational knowledge elements (right branch in Fig. 3); knowledge sharing/propagation mechanism; and schema integration/reconciliation mechanism (e.g. Fig. 4).

The answers from the interview reveal the following findings:

† The Inter-organizational meeting-scheduling process diagram provides a good representation of the actual process in the real business world. The interviewee added that identification of potential partner organizations for merger and acquisition deals is usually conducted using external data sources provided by economic consulting agencies, lawyers, and accountants.

† Implementing the knowledge propagation/sharing mechanism is problematic especially in competitive sectors such as banking, finance, marketing, etc. where organizations can harm themselves by sharing valuable organizational knowledge with competitors. The interviewee commented that the IIMS is more suitable to either, largescale consortiums of cooperative companies, government, and military organizations where competition is not prevalent.

† Implementing the schema integration/reconciliation mechanism is very important and challenging for the success of the IIMS, however, practically, most organizations do not represent their knowledge in a standardized computerized format. According to the interviewee, the need for a common glossary that will enable partner organizations to integrate knowledge schemes is the biggest challenge in adopting the IIMS.

Recent developments in the area of interoperability schemes such as web services<sup>7</sup> the Universal Description Discovery and Integration (UDDI) project<sup>8</sup>, and the Open Grid Services Architecture for Distributed System Integration (OGSA)<sup>9</sup> provide encouraging indications that achieving practical interoperability over heterogenous software and hardware platforms is in fact possible in the upcoming years.

Nevertheless, the above findings provide only a preliminary feedback regarding the feasibility and value of the IIMS model. The following section frames these preliminary case-based findings in a wider technological, human and organizational context, by relating them to several other factors mentioned in the literature, which hinder the successful adoption of the model.

## 5. Discussion of the IIMS model

This section discusses the IIMS model from both a technological and a nontechnological perspective. The discussion is divided into the following two stages:

First, relevant work, from the organizational behavior and information systems literature is reviewed in order to shed some light on the limitations of the proposed model and its practical feasibility (Section 5.1). Next, several practical guidelines are proposed in order to facilitate easier adoption of the IIMS and to overcome the limitations mentioned above (Section 5.2).

## 5.1. Limitations of the IIMS model

This section reviews the relevant literature regarding both the non-technological and technological limitations of the IIMS model. Non-technological limitations refer to organizational, psychological, sociological and behavioral limitations. Such limitations focus on the way people react to and interact with the new technology. Technological limitations, on the other hand, stem from the internal features and capabilities of the technology itself and are usually caused by the selection and combination of specific implementation tools and constructs (e.g. software agents, knowledge bases, information retrieval versus information filtering).

## 5.1.1. Non-technological limitations

Under the technological rationality for adopting innovation (a structuralist perspective [Swan et al., 1997]), if the proposed IIMS model is sufficiently good in terms of technological criteria, then end-users will automatically adopt it and it will gradually diffuse to become an organization-wide solution (Rogers, 1983). There is, however, substantial practical and theoretical evidence that this is not the case and there are many obstacles to a successful adoption of new technologies in organizations (Grudin, 1989, 1994). These obstacles extend beyond merely providing a sophisticated technological solution. Following is a review of several important literature sources to support this claim.

The literature on innovation has been extremely broad, extending from traditional structuralist approaches to more process-oriented approaches (Swan et al., 1997). From the structuralist perspective, networks are treated as cognitive structures through which information and knowledge can be smoothly transferred from suppliers to users so that the new ‘thing’ can be adopted within the user firm (Swan et al., 1997). Structuralist perspectives have been criticized for under-emphasizing the dependency of innovation within a social and organizational context (Scarbrough and Corbett, 1992). In contrast, process perspectives argue that innovation should be seen as a complex, time phased, and politically-charged design and decision process often involving multiple social groups within organizations. Process perspectives on innovation, extend structuralist perspectives by examining more dynamic, cognitive, social and political processes through which new ideas are developed, communicated, transferred, and implemented over time within particular organizational contexts (‘community networks’), and identifying ways of facilitating these processes. The difference between these perspectives is demonstrated in the cases of E-bank and Brightco (Swan et al., 1997).

The Information Infrastructure (II) evolution theory (Hanseth et al., 1996; Hanseth and Monteiro 1998; Monteiro 1998) provides an alternative explanation of the way innovations are diffused into organizations. This theory is based on the need to balance between standardization and flexibility in order for a network infrastructure to survive innovations. For example, in the case of the Internet expansion (next generation IP) there is a need to balance the momentum achieved via standardizing protocols (e.g. TCP/IP) with the need for flexibility on the other (Hanseth et al., 1996; Monteiro, 1998). If the expansion momentum results in irreversibility of the network, then the information infrastructure might collapse or be perceived as ‘everybody’s enemy in the organization (Hanseth and Braa, 1998) such as in the case of the SAP installation at Norsk Hydro.

In another case study which evaluated the adoption of an Electronic Patient Record (EPR) system (Hanseth and Monteiro, 1998), the patient’s record is part of a large, complex and irreversible ‘actor’ networks. In order to fit the new EPR system to the existing network into the organization, two generic strategies were recommended. The first strategy involves gateways that translate information back and forth between two co-existing networks such as electronic and paper-based patient record systems. If the translation is too complex for a gateway to handle, then the second strategy of polyvalent networks is recommended. The authors claimed that polyvalent networks can be implemented for security reasons when terminals transferring sensitive patient information are separated from terminals used for global Internet access and e-mail correspondence.

Groupware technology such as the IIMS may be avoided if it interferes with the subtle and complex social dynamics that are common to groups. Groupware adoption often requires additional work from individuals who do not perceive a direct benefit from its use (Grudin, 1994). In order to overcome these barriers, adoption of groupware technology may be achieved either by mandated use from senior management or by attracting a critical mass of users and diffusion via social peer pressure (Grudin and Palen, 1995).

Groupware Calendaring System (GCS) create new opportunities for social coordination but at the same time also introduce opportunities for conflict by challenging the notion of personal privacy and control over information and time. By using groupware systems, employees are able to infer the quality of time allocation of their peers, which creates social pressure against adoption (Palen, 1999). This problem is brought out in the situation when a R&D headquarters of a global pharmaceutical firm introduced a groupware tool to facilitate sharing of early experimental results among researchers as part of a major effort to reduce R&D cycle time (Ciborra and Patriotta, 1996). The goal was to enable researchers to capitalize quickly on successful breakthroughs and to avoid repeating their peers’ failed trials. However, the groupware was rarely used because researchers had no incentive to put new findings into a shared database where others might use them to get it right first, nor did they have any incentive to disclose their failures. To stimulate use of the groupware, management announced a policy of taking contributions to the shared knowledge base into account in performance reviews. The result was a sharp increase in usage, but for the most part the contributions were neither timely nor valuable.

In a case study of three groups using Lotus Notes (Kartsen, 1995), variations of how a single application is interpreted within its user group were traced to the individually constructed meanings of each user. As an individual agent, each user forms her or his conceptions based on interactions with the application. Groupware applications are not ‘ready’ when they are installed on the users’ workstations, but are constantly constructed and reconstructed. How the application is understood and discussed guides its use and evolution; and how the application is used and further developed guides how it is understood (Kartsen, 1995).

## 5.1.2. Technological limitations

There are several technological-oriented limitations in adopting the IIMS which stem from the symbol-level constructs (Baldwin and Yadav, 1995) and user modeling approach used by the IIMS model. The model is based on agent-based intelligence that provides semi-automatic scheduling capabilities, which rely on explicit and implicit user-modeling. The following explains the relevant technological difficulties based on the symbol level constructs used in the model.

The use of software agents for automation of tasks for end-users is considered problematic because they interfere with the human need for understanding and control (Schneiderman and Maes, 1997). Software agents can therefore only be a complementary technique to well designed interfaces comprised of direct manipulation and visualization techniques. End-users must always be able to specify the amount of control they would like over the agent’s behavior, possibly even bypassing the agent. In addition, end-users must understand and fully trust the agent’s behavior (Schneiderman and Maes, 1997).

User models were found to be valuable for general categories but problematic when using fine-grained topics (Allen, 1990). In a state of the art survey of social and contentbased techniques for text filtering, Oard (1997) proposed a graphical, two-dimension classification for the complementary information detection tasks: information retrieval and information filtering.

The first dimension is the rate of information source change, and the second is the rate of information needs change. The former deals with the stability of the dataset, whereas the latter deals with dynamism of queries over a period of time. Information retrieval is low on information source change rate and high on information needs change rate, contrary to information filtering where information source change rate is high and information needs change rate is low. Although there are a number of existing applications that provide ample support for standard information filtering and information retrieval tasks, a combination both highly dynamic queries with highly dynamic datasets remains a ‘grand challenge’ (Oard, 1997).

Content-based, automated filtering techniques, based on matching the frequency of keywords in the documents with an individual user model (profile), are limited in finding novelty but can effectively manage information overload. A combined approach that also pays attention to peer judgments and collaborative annotation is likely to be more effective than the pure content-based approaches (Oard, 1997).

As demonstrated in Section 3.4, a major technological challenge is the integration and reconciliation of heterogeneous knowledge schemas belonging to different organizations. Creating an integrated organizational knowledge schema and adopting the most suitable knowledge sharing mechanisms are not easy tasks. These tasks become even more challenging whenever the organizations use remote domains of knowledge, and in severe cases can hinder the widespread adoption the IIMS model. Evidence supporting this claim was obtained in a preliminary interview with a former manager of Mergers and Acquisitions (M&A) who was presented the model. The interview suggests that the IIMS model is very useful, subject to providing ample support for the selection of participating organizations as well as integration and sharing of heterogeneous organizational knowledge.

All in all, there is a substantial body of literature providing evidence that a plethora of technological, psychological, cultural, organizational and sociological factors determine the success in adopting the proposed IIMS model. Among the most critical factors are the size of the installed base of users; the strengths of the human and non-human network agents supporting the technology as well as the fit among them; and the number of quality gateways that enable the technology to create a foothold despite of other strong contenders. The purpose of the following subsection is to propose some guidelines and remedies in order to overcome these limitations.

## 5.2. Addressing the IIMS model limitations

This section proposes several implementation tactics and guidelines for the IIMS in an attempt to overcome the limitations just mentioned. Future empirical research is needed, however, in order to acknowledge the value of these guidelines in real-life interorganizational meeting-scheduling scenarios.

## 5.2.1. Addressing the non-technological limitations

The following studies provide guidelines and suggestions on how to overcome the cultural, sociological, organizational, and psychological limitations in adopting collaborative and inter-organizational applications.

Grudin (1994) draws the following guidelines:

† Adopting the system incrementally by gradually adding meeting-scheduling features to existing single-user applications and workflow systems that proved to be a success in the target organizations.

† Adopting the new system in a pilot department which has experience with groupware systems, and expanding the system from there.

† Providing tangible incentives to employees and managers that maintain their calendars up-to-date.

† Balance calendar maintenance work among employees and managers as much as possible.

† Tailoring the application to the specific needs of the adopting organization. In the case of the IIMS this requires using process scripts and meeting-content templates that provide flexibility during the scheduling process (Glezer and Yadav, 1999) (see also scheduling knowledge elements in Fig. 3).

In a recent study, Gebauer and Buxmann (2000) developed an economic model to evaluate inter-organizational business transaction systems. The model considered the following parameters: the system’s one-time setup costs; current costs for system administration and application development; and saving of information costs and process time. Gebauer and Buxmann (2000) evaluated their model in the area of supply chain management using the Zephyr transaction system developed at the Lawrence Livermore National Lab (LLNL) in order to connect LLNL with its suppliers.

Based on the LLNL case, it is clear that low setup costs are critical for the successful diffusion of new inter-organizational applications and their underlying technologies. The reason for this is that convincing new partner organizations to use the new system is not easy if even its preliminary testing involves high setup costs.

In order to overcome this difficulty, Gebauer and Buxmann (2000) recommend developing what they call an ‘80%-solution’, using open, standard, and Internetcompatible technologies instead of striving for the optimal technical solution from an internal standpoint (‘100%-solution’), which can turn out to be sub-optimal from an overall standpoint of the firm.

## 5.2.2. Addressing the technological limitations

The most critical technological limitation in adopting the IIMS is the mechanism of schema integration and knowledge sharing among the partner organizations. The dynamic nature of both the knowledge bases and the queries, place the adoption of the IIMS in the zone of the ‘grand challenge’ (Oard, 1997).

In order to cope with this challenge, the IIMS should be viewed as an application that can operate only after participating organizations have already established a basic technological platform with a reasonable level of inter-organizational cooperation. This means that an IIMS installation and adoption should be deferred to a later stage, after teams from the partner organizations have already met, discussed and created a common technological infrastructure and some degree of common terminology. The common infrastructure and terminology can then gradually facilitate collaboration at the application level (e.g. IIMS).

After basic inter-organizational transaction processing capabilities have been created, including common anthologies, the chances for success in adopting an application such as the IIMS are higher. This claim is supported by evidence from the adoption of the Zephyr system at LLNL (Gebauer and Buxmann, 2000). After Zephyr is up and running, other inter-organizational applications are more likely to succeed because they are not pioneer IOS anymore. In addition, using a standard and widespread underlying platform such as the Internet can reduce hurdles and expedite the adoption process.

Gebauer and Buxmann (2000) also mention the following technological challenges in future adoption of similar IOS: alignment and integration of business processes; a dynamic group of business partners that collaborate over an IOS network; and reduced search costs for business partners which increases the level of competition. The latter two are highly influenced by the intensive growth of Internet usage for business purposes (e.g. Extranets/ Internet-based Electronic Data Interchange (EDI), and Internet-based Supply Chain Management).

The keys to overcoming the technological challenges in adopting the IIMS are congruent with the general guidelines for successful development and adoption of information systems, namely, using standard technologies such as the Internet and open standards; ensuring tight involvement of stakeholders (e.g. end-users, mid- and strategic-level managers) during all stages of the IIMS life cycle; and finally, deferring adoption of the IIMS in order that partner organizations have more opportunities to align their business processes.

## 6. Conclusions

This article reviews the prevailing literature on interoperability standards for calendar and scheduling systems. It then proposes and evaluates comprehensive agent-based architecture for an IIMS that incorporates interoperability standards and mechanisms in all three aspects inherent to the meeting-scheduling process: calendar-, scheduling- and communication- management.

The article claims that a plethora of technological, psychological, cultural, organizational and sociological factors may hinder the successful adoption of the proposed model. A number of implementation tactics and guidelines are proposed in an attempt to overcome these obstacles. As an example: using standard technologies such as the internet and open standards as much as possible; ensuring tight involvement of stakeholders such as end-users, mid- and strategic-level managers during all stages of the IIMS life cycle; and finally; deferring adoption of the IIMS to later stages in order that business partners have ample opportunities to align their business processes.

Beyond the above preliminary evaluation, more research is needed in order to construct a full-scale IIMS and evaluate its performance and benefits in the real business world.

## References

Allen, R.B., 1990. User models: theory, method, and practice. International Journal of Man– Machine Studies 32 (5), 511–543.

Baldwin, D., Yadav, S.B., 1995. The process of research investigation in artificial intelligence—an unified view. IEEE Transactions on Systems, Man, and Cybernetics 25 (5), 852–861.

Beard, D., Palanlappan, M., Humm, A., Banks, D., Nair, A., Shan, Y., 1990. A visual calendar for scheduling group meeting. CSCW Proceedings of the Conference on Computer Supported Cooperative Work, 279–290.

Bowers, J., Button, G., Sharrock, W., 1995. Workflow from within and without: technology for cooperative work on the print industry shop floor. Proceedings of the Fourth European Conference on Computer-Supported Cooperative Work, 51–66.

Carstensen, P., Sorensen, C., 1996. From social to systematic: mechanisms supporting coordination in design, computer supported cooperative work. Journal of Collaborative Computing 5 (4), 387–413.

Ciborra, C., Patriotta, P., 1996. Groupware and teamwork in new product development: the case of a consumer goods multinational. In: Ciborra, C., (Ed.), Groupware and Teamwork, Wiley, New York, pp. 121–142.

Florio, S., 1996a. Notes R5 Calendar & Scheduling, Available from Notes R5 featured articles section at http://www.notes.net/today.nsf.

Florio, S., 1996b. This Iris later view Ryan Jansen: Calendar Keeping, Available from Notes R5 interviews section at http://www.notes.net/today.nsf.

Gebauer, J., Buxmann, P., 2000. Assessing the value of inter organizational systems to support business transactions. International Journal of Electronic Commerce 4 (4), 61–82.

Genesereth, M.R., Ketchpel, S.P., 1994. Software agents. Communications of the ACM 37 (7), 48–53.

Glezer, C., Yadav, S.B., 1995. A conceptual model and a prototype for an intelligent meetingscheduler (IMS). EXPERSYS 95-Proceedings of the seventh International Conference on Artificial Intwelligence and Expert Systems Applications, 279–285.

Glezer, C., Yadav, S.B., 1999. A conceptual model of an intelligent meeting-scheduler (IMS). Journal of Organizational Computing and Electronic Commerce 9 (4), 233–251.

Greif, I., Sarin, S., 1987. Data sharing in group work. ACM Transactions on Office Information Systems (2), 187–211.

Grudin, J., 1989. Why groupware applications fail: problems in design and evaluation. Office: Technology and People 4 (3), 245–264.

Grudin, J., 1994. Groupware and social dynamics: eight challenges for developers. Communications of the ACM 37 (1), 93–105.

Grudin, J., Palen, L., 1995. Why groupware succeeds: discretion or mandate? Proceedings of European CSCW Conference (ECSCW’95), 263–278.

Hanseth, O., Braa, K., 1998. Technology as a traitor: emergent SAP infrastructure in a global organization. Proceedings of the Nineteenth International Conference on Information Systems (ICIS), 188–196.

Hanseth, O., Monteiro, E., 1998. Changing irreversible networks. Proceedings of the European Conference on Information Systems (ECIS 1998) 3, 1123–1139.

Hanseth, O., Monteiro, E., Hatling, M., 1996. Information infrastructure development. Science Technology and Human Values 21 (4), 407–426.

Holland, C.P., 1995. Cooperative supply chain management: the impact of interorganizationa systems. Journal of Strategic Information Systems 4 (2), 117–133.

Huber, G.P., 1990. A theory of the effects of advanced information technologies on organizational design, intelligence and decision making. Academy of Management Review 15 (1), 47–71.

Kartsen, H., 1995. It’s like everyone working around the same desk: organizational reading of Lotus notes. Scandinavian Journal of Information Systems 7 (1), 3–32.

Malone, T.W., Crowston, C., 1994. The interdisciplinary study of coordination. ACM Computer Surveys 26 (1), 86–119.

Mintzberg, H., 1979. The Structuring of Organizations, Prentice-Hall, Englewood Cliffs.

Monteiro, E., 1998. Scaling information infrastructure: the case of the next generation IP in internet. The Information Society 14 (3), 229–245.

Mosier, J.N., Tammaro, S.G., 1997. When are group scheduling tools useful. Computer Supported Cooperative Work: The Journal of Collaborative Computing 6, 53–70.

Nonaka, I., 1994. A dynamic theory of organizational knowledge creation. Organization Science 5 (1), 14–37.

Nonaka, I., Takeuchi, H., 1995. The knowledge-creating company, How Japanese Companies Create the Dynamics of innovation, Oxford University Press, New York.

Oard, D.W., 1997. The state of the art in text filtering. User Modeling and User Adapted Interaction: An International Journal 7 (3), 141–178.

Palen, L., 1999. Social, individual&technological issues for groupware calendar systems. Proceedings of the ACM CHI’99 Conference.

Pino, J.A., Mora, H.A., 1998. Scheduling meetings using participants’ preferences. Information Technology and People 11 (2), 140–151.

Pendergast, M., Hayne, S.C., 1995. Alleviating convergence problems in group support systems. Computer Supported Cooperative Work: The Journal of Collaborative Computing 3, 1–28.

Rogers, E.M., 1983. Diffusion of Innovations, The Free Press, New York.

Scarbrough, H., Corbett, M., 1992. Technology and Organization: Power, Meaning and Design, Routledge, London.

Schmidt, K., Simone, C., 1996. Coordination mechanisms: an approach to CSCW systems design. Computer Supported Cooperative Work: Journal of Collaborative Computing 5 (2–3), 155–200.

Schneiderman, B., Maes, P., 1997. Direct manipulation versus software agents: excerpts from debates at IUI 97 and CHI 97. Interactions, November–December, 42–61.

Sen, S., Durfee, E.H., 1991. A formal study of distributed meeting scheduling: preliminary results. Proceedings of the ACM Conference on Organizational Computing Systems, 55–68.

Sen, S., Durfee, E.H., 1992. A formal analysis of communication and commitment in distributed meeting scheduling. Working Papers of the Eleventh International Workshop on Distributed Artificial Intelligence, 334–344.

Sen, S., Durfee, E.H., 1993a. The effects of search bias on flexibility in distributed scheduling. Working Papers of the Twelfth International Workshop on Distributed Artificial Intelligence 12, 321–334.

Sen, S., Durfee, E.H., 1993b. Using temporal abstractions and cancellations for efficiency in automated meeting scheduling. Proceedings of the International Conference on Intelligent and Cooperative Information Systems for Efficiency, 163–172.

Sen, S., Durfee, E.H., 1994a. On the design of an adaptive meeting scheduler. Proceedings of the Tenth IEEE Conference on AI Applications, 40–46.

Sen, S., Durfee, E.H., 1994b. The role of commitment in cooperative negotiation. International Journal of Intelligent and Cooperative Information Systems 3 (1), 67–81.

Smith, B., Eglowstein, H., 1994. Scheduling across the enterprise. BYTE 19 (6), 216–222.

Spender, J., 1996. Organizational knowledge, learning and memory: three concepts in search of a theory. Journal of Organizational Change 9 (1), 63–78.

Sugihara, K., Kikunu, T., Yoshida, N.A., 1989. Meeting scheduler for office automation. IEEE Transactions on Software Engineering 15 (10), 1141–1146.

Swan, J., Newell, S., Scarbrough, H., Hislop, D., 1997. Knowledge management and innovation: networks and networking. Journal of Knowledge Management 3 (30), 262–275.

Weirich, M.L., 1992. Meetings and Conventions Management, Delmar Publishers Inc, New York.
