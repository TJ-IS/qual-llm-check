---
otero_id: 15412
otero_key: "7CSEJYAC"
title: "Traceability-based knowledge integration in group decision and negotiation activities"
authors: "Kannan Mohan; Balasubramaniam Ramesh"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.05.026"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Traceability-based knowledge integration in group decision and negotiation activities

Kannan Mohan <sup>a,\*</sup>, Balasubramaniam Ramesh <sup>b</sup>

<sup>a</sup>Department of Computer Information Systems, Zicklin School of Business, Baruch College, Box B11-220, One Bernard Baruch Way New York, NY 10010, United State

<sup>b</sup>Department of Computer Information Systems, J. Mack Robinson College of Business, Georgia State University, United States

Available online 28 June 2005

## Abstract

Group decision and negotiation (GDN) in distributed collaborative environments involves the acquisition and use of extensive knowledge. Knowledge elements that play a critical role in guiding GDN activities are distributed across different work environments that are not seamlessly integrated with each other. We argue that integrating fragmented knowledge will improve the process of GDN in software development. In this paper, we present an approach to knowledge integration using traceability. Our approach comprises of: (a) a traceability framework that identifies the key knowledge elements that are to be integrated, and (b) a prototype system that supports the acquisition, integration, and use of knowledge elements represented by the traceability framework. We illustrate the usefulness of our approach with a case study in a software development organization. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Knowledge integration; Traceability; Collaborative software development; Decision making; Group decision and negotiation; Work processes

## 1. Introduction

Group decision and negotiation (GDN) in knowledge-intensive domains such as large-scale, distributed software development is considered to be one of the most critical success factors. Boehm et al. [5,6] highlight the key role played by negotiation in achieving win–win solutions in software development. GDN in large-scale software development involves the integration of knowledge from a variety of sources, often embedded in different tools and environments. In complex GDN activities, the participants access and use knowledge about the problem and solution domains, which is stored in a variety of organizational memory sources such as spreadsheets, meeting minutes, design documents, etc. Seamlessly linking such knowledge fragments spread across organizational work processes and tools will be very helpful in supporting GDN activities. The development of knowledge networks, which are networks of people and information systems associated with such collaborative, knowledge-intensive tasks, is a step towards mitigating this problem [43]. Creation of such networks by seamless integration has been attempted by many tools handling explicit, codifiable content (e.g., workflow tools, project management systems, collaborative systems, intranets, and data warehouses) and those that enable sharing and distribution of contextualized knowledge content (e.g., digital whiteboards, case-based reasoning tools, multimedia channels, annotation tools, and concept mapping systems). A variety of mechanisms for achieving such integration have also been investigated in the past. These include the use of wrappers to integrate legacy data and systems, message broker-based middleware, and knowledge servers [60]. Prior research in this area recognizes that achieving integration of fragmented knowledge may be very complex or even impossible in most cases, but achieving interoperability is a viable approach [55]. One of the common problems in facilitating integration of knowledge to support collaborative software development is that the stakeholders involved do not have adequate guidance on what kind of knowledge elements should be integrated, and how the integration should be structured and used. Traceability, defined as the ability to describe and follow the life of a physical or conceptual artifact, addresses these challenges by providing semantic and structural guidance to knowledge integration. Our research is based on the premise that an important step towards achieving knowledge integration is providing traceability across various knowledge fragments that are used in GDN activities.

To provide traceability across distributed knowledge fragments, we will have to address the following question: What are the components of knowledge that need to be integrated to support GDN activities in complex problem-solving situations? Consider, for example, the process of designing a complex software system. It is a knowledge-intensive activity that requires collaboration among various stakeholders involved in the process. The complexity of large-scale software projects demands effective coordination among numerous designers or design teams to effectively manage the product development effort. As the stakeholders come from varied backgrounds with different viewpoints and expertise, effective group communication is essential for the success of a project. Prior research has suggested various frameworks for capturing knowledge about the process of decision making that could form the basis for GDN support [8,36]. Several stand-alone tools have been developed to support such knowledge capture and use [52]. Among them are approaches and tools that provide structural and collaborative guidance [4,5,7,8,11, 24,50], and synchronous and asynchronous communication, coordination, and collaboration [13,33,42, 47,48] among participants to support GDN. Further, team members use work productivity tools such as project management and document management tools as well as task-specific tools such as computer-aided software engineering (CASE) tools (e.g., Rational Rose) while engaged in GDN activities in software development. The objective of our research is to develop an approach to integrate knowledge fragments stored in such diverse environments to support GDN activities in software development. We argue that integrating knowledge fragments used by various stakeholders by providing traceability among them will increase the effectiveness of GDN activities performed during the software development process. We define knowledge traceability as the ability to follow the life of a knowledge component from its origins to its use [51]. Formally stated, a knowledge traceability network can be defined as a semantic network in which nodes represent different knowledge compo nents among which traceability is established through links of different types. This includes links to the stakeholders who are involved in the creation, maintenance, and use of these knowledge fragments, as well as the sources in which such fragments are <sup>d</sup>stored.<sup>T</sup> Such a network facilitates the understanding and communication of the context in which group decisions and negotiations are carried out. This ability is essential, for example, in exploring and justifying the selection of potential solutions from various alternatives. Further, understanding the context in which a group decision was made will help in monitoring the repercussions of changes in the underlying context. For example, capturing the history of decision making and linking underlying assumptions with the alternatives considered during a GDN activity can provide a dynamic validation of the decisions under varied contexts established by invalidated and new assumptions. Traceability has been used in the past to support knowledge-intensive processes [28,29,51]. Motivated by the effectiveness of traceability in supporting knowledge-intensive processes, we develop a traceability-based approach to integrate knowledge to provide group decision and negotiation support for software development.

In Section 2, we summarize the past research on group decision and negotiation, highlighting the lack of adequate support for integrating knowledge fragments used in GDN activities in software development. In Section 3, we present details on a case study in collaborative software development and highlight the need for knowledge integration to support GDN activities in this domain. In Section 4, we discuss the use of traceability as an effective solution to address challenges in knowledge integration. In Section 5, we present our knowledge traceability-based approach to supporting GDN in collaborative software development. We also illustrate how our approach can effectively facilitate knowledge integration through examples drawn from our case study. Section 6 discusses related research, while Section 7 provides some concluding remarks, limitations of this research, and directions for future research.

## 2. Supporting group decision and negotiation

## 2.1. Group decision and negotiation activities

The primary objective of group decision and negotiation (GDN) processes is to make a choice among alternatives that can be accepted by multiple stakeholders within a reasonable period of time. Participants often have competing viewpoints and interests during GDN. In general, GDN involves the following activities:

1. Identify and state goals and goal agreement among stakeholders [54]

2. Identify problems/issues, alternatives, and ideas through brainstorming [20]

3. Ensure that all the arguments are consistent with one another or explicitly recognize inconsistencies [8]

4. Compare alternatives and identify criteria for selection among alternatives [35]

5. Decide on a course of action after thorough consideration of all the alternatives, past decisions made, and their rationale; this may be done by communicating with stakeholders involved, or by consulting a repository documenting this knowledge [48]

6. Record decisions made, impacts of these decisions, alternatives considered, arguments and assumptions based on which decisions were made, agreements and disagreements expressed by the stakeholders, and information about stakeholders who are responsible for these; this facilitates knowledge sharing and helps decision makers understand and reevaluate their decisions [11]

7. Seek approval of group’s decision for the chosen course of action

8. As a part of the decision-making process, communicate synchronously and asynchronously with other stakeholders, and coordinate the activities of all the stakeholders involved in the process [42].

## 2.2. Supporting group decision and negotiation activities

A Group Decision and Negotiation Support System (GDNSS) is defined as an interactive computer-based system that facilitates the solution of unstructured problems by a set of decision makers working together as a group [21]. GDNSS varies widely in supporting the tasks identified in the previous subsection. A recent study comparing popular GDN systems like Lotus Notes, Assistant for Cooperative Work (ASCW), Graphical Issue Based Information Systems (gIBIS), etc., identifies several common capabilities offered by GDN tools [49]: synchronous and asynchronous communication, group collaboration through data and application sharing, collaborative editing, electronic meeting, and argumentation.

E-mail exemplifies tools that facilitate asynchronous communication. Although e-mail supports exchange of information, often it is done in the form of attachments to e-mail messages. Here the focus is on delivery rather than sharing. Often, the contents of critical exchanges between collaborating group members are lost within individual e-mail accounts. Fragmentation of knowledge resulting from this approach leads to a variety of problems. For example, during software development, a designer may make certain design decisions based on advice from an architect about the characteristics of the architecture that will impact the design. When a similar scenario is revisited in the future, retracing the reasons behind the past decisions becomes difficult, since this knowledge is buried in e-mail messages. The ability to link knowledge components stored within e-mail messages will be very helpful to mitigate such problems.

Some group collaboration tools support synchronous communication. NetMeeting is an example of a collaboration tool that supports online interactive communication and information exchange. Besides providing whiteboard and chat features for exchanges, the system also facilitates both file sharing and application sharing. Similar collaborative tools have become popular for conducting virtual interactive meetings. As these tools are intended to support informal/unstructured exchanges, the reuse of much of the knowledge contained within them (say, NetMeeting session archives) becomes difficult. Further, the conversations that occur within these tools may rely on knowledge fragments stored in other sources such as documents and e-mail messages.

Groove is an example of a peer-to-peer (P2P) collaborative system that allows groups of people to collaborate in a secure virtual workspace. Besides providing interactive communication and file/application sharing features, Groove also allows its users to browse the Internet together. Project JXTA is an effort by Sun Microsystems to provide a peer-to-peer solution for sharing applications and services [22]. These peer-to-peer systems focus primarily on communication and service sharing. These tools do not provide adequate support to integrate knowledge that is distributed across different peers in the P2P network.

Argumentation tools that support asynchronous communication take the view that group decision and negotiation can be helped by facilitating the process of identifying, communicating, and elaborating the alternatives and decision criteria, in contrast to analytical tools that concentrate on the automation of the algorithms that help aggregate preferences of group members. Most systems that attempt to provide analytical decision support to groups (such as those that employ decision theoretic models) assume that the alternative solutions to the decision problem of interest are well understood and the effects or consequences of choosing among these are well known. Systems such as gIBIS [11] and IBE [39] take a different view and focus on structuring the problem and solutions spaces. gIBIS, for example, provides a hypertext interface to the IBIS (a popular argumentation model) to facilitate the documentation of rationale behind decisions. This knowledge has been found to be useful in supporting the activities of various stakeholders involved in decision making, exemplified by tools such as REMAP (Representation and Mainte nance of Process Knowledge) [51] and SIBYL [40]. For example, SIBYL provides mechanisms to facilitate the capture and use of process knowledge. This approach recognizes that evolutionary restructuring and reformulation of the problem and solution spaces are important steps in the management of conflicts. Further, this approach is distinct in its recognition of the need to support the process of information exchange and assumption surfacing to complement the use of analytical techniques in managing conflicts. In similar spirit, recognizing the need for supporting different models of communication and argumentation, Conversation Builder [33] was developed to provide a customizable environment to support different communication protocols. A major shortcoming of these argumentation and conversation support tools is that these conversations are conducted in stand-alone environments, leading to the fragmentation of knowledge used in activities supported by these tools.

In summary, most tools that support GDN activities create islands of fragmented knowledge that are difficult to integrate. Knowledge that is essential for decision making is distributed across these environments. In the next section, we illustrate this knowledge fragmentation using a case study in distributed software development. Our work is based on the premise that the utility of GDN tools can be enhanced by the capability to integrate knowledge elements that reside fragmented in different environments. This approach seeks to minimize the overhead for the decision makers and facilitate knowledge exchange across various tools. The following section discusses the research methodology and focuses on highlighting how software development is a knowledge-intensive group decision and negotiation process.

## 3. Distributed software development: a case study

## 3.1. Research methodology

We have conducted a case study in an organization that specializes in the development of embedded telecommunication systems. We conducted structured and semi-structured interviews with various stakeholders such as developers and project managers to understand the kind of group decision and negotiation activities that they are involved in during the process of software development. This study also focused on understanding the stakeholders’ requirements for a GDN support system, as well as the capabilities of the collaborative system that they currently use. We present a brief description of the GDN activities and GDN tools used in the organization.

The organization is involved in developing HospCom, an embedded system used in hospitals. The system takes care of billing the patients for telephone and television usage. Every patient room is equipped with a telephone and a television. The patient operates the television by dialing preset codes from his/her phone. Their requests are routed to the HospCom server through a private automatic branch exchange. Services running on the HospCom would evaluate the patients’ request by checking their privileges and account balances. Authorized requests are sent to a TV controller connected to the television sets. Pay channels are restricted to patients who have adequate balance in their hospital account. The hospital staff has the capability to print reports on patients’ usage, balances, and privileges. Our case study was specifically focused on the design of the television operation module of the system. This module would receive a request from a patient, process the request in order to interpret the type of request, check the patient privilege and account balance, and service the request.

The development of HospCom is done offshore and therefore the stakeholders use collaborative tools extensively. MS Outlook and NetMeeting are primarily used for supporting unstructured discussions. Although these discussions are archived, they are not linked to the project-related artifacts that might be affected by them. This commonly resulted in repetitive discussions of issues and poor understanding of repercussions of design decisions taken during discussions. The requirements and design specifications are stored as MS Word documents. The design team uses MS Outlook as the e-mail client for communication and information delivery. They use Rational Rose to develop design specifications.

HospCom uses a variant of the Rational Unified Process (RUPR), a software engineering process and a disciplined approach to assigning tasks and responsibilities within a development organization (http://www-306.ibm.com/software/awdtools/rup/). RUP is comprised of various phases and disciplines. Each RUP discipline involves numerous GDN activities that are good examples of the activities listed in Section 2.1.

## 3.2. Knowledge fragmentation in collaborative software development

Developing large-scale, complex software has been widely recognized as a knowledge-intensive activity. Each phase in development of complex, large-scale software involves numerous group decision and negotiation activities. Knowledge elements that are needed for shaping crucial design decisions exist as fragments scattered in various development environments. Integration of such distributed knowledge elements is considered as key to successful software development [62]. Knowledge integration becomes especially challenging when software teams are geographically distributed. Distributed software teams need collaborative technologies that allow design collaboration to go beyond simple coordination of individualistic work to joint activity aimed at coconstruction of <sup>d</sup>collective work products<sup>T</sup> [27,34]. Also, software development often involves negotiations across various stakeholders [14]. Empirical research on collaborative software design suggests that critical decision-making activities in this domain can be represented as a process of argumentation [27].

In this section, we provide examples of various GDN activities involved in collaborative software development and establish the need for knowledge integration to support these activities. Table 1 focuses on a particular discipline in RUP, viz., the analysis and design discipline, as an exemplar. For each of the GDN activities enumerated in Section 2.1, examples encountered at HospCom are listed.

The activities listed above are intended to be illustrative of the GDN activities involved in the distributed software development process, rather than to be exhaustive. These GDN activities pervade throughout every discipline and phase in the software development process. Such pervasiveness and intensity of GDN activities in software development highlight the need to support the various stakeholders.

The GDN activities discussed above generate and use knowledge from different sources. In the context of large-scale, collaborative software development, multiple work practices of the stakeholders involved, performed in various work environments, generate information and knowledge that are distributed across these work environments, producing islands of knowledge. Use of this knowledge in decision making involves bringing together knowledge from multiple sources. In organizations that use multiple work systems to support various work practices [2], this capability is especially important.

Table 1 Examples of GDN activities in the analysis and design discipline of RUP at HospCom

<table><tr><td>GDN activity</td><td>Example from HospCom</td></tr><tr><td>(1) Identify and state architectural goals, and agreement among stakeholders on various architectural needs and decisions</td><td>The architecture should facilitate control of patient television operation by hospital staff through any system distributed throughout the hospital. It should facilitate use of a common device for telephone and television operation by the patients. These operations are to be separated from the hospital bill processing.</td></tr><tr><td>(2) Identify alternative architectural designs</td><td>N-tier client server architecture with multiple servers to support hardware control for television and telephone operation, and billing support, with considerably thin web-based clients. An alternative architecture of having heavy client processing and moderate server processing was also proposed.</td></tr><tr><td>(3) Ensure that all arguments that support/oppose architectural decisions are consistent with one another</td><td>Architects made some architectural decisions based on the assumption that only one type of device will be used for television control. Arguments and related assumptions that surfaced from meetings among analysts, designers, and the architects made it clear that some hospitals may use devices that are already available, thereby necessitating support for multiple types of devices.</td></tr><tr><td>(4) Compare alternative architectural designs, and identify and use criteria to select an appropriate architecture</td><td>N-tier architecture with thin web-based clients was preferred. Portability and interoperability for the client side, and performance were some of the criteria that were discussed to select this architecture.</td></tr><tr><td>(5) Identify past architectural decisions and apply them in current situation</td><td>While designing the architecture for HospCom, architects consult the architectural documents of other embedded system projects developed within the same organization and use patterns from a similar approach used in an earlier project.</td></tr><tr><td>(6) Seek approval or group decision by subjecting the architecture to reviews and creating baselines</td><td>Architecture documents are reviewed and studied for feasibility. Architecture reviewers consult with other stakeholders involved in the project.</td></tr><tr><td>(7) Record crucial architectural decisions—such documentation of architectural decisions will help in the implementation and maintenance stages</td><td>Decisions made to use certain architectural patterns to support different types of devices are recorded so that, during later stages, these patterns can be fully recognized and utilized.</td></tr><tr><td>(8) Communicate, collaborate, and coordinate with software architects, architecture reviewers, designers, design reviewers, implementers, integrators, and database designers</td><td>Software architects consult with designers, implementers, and integrators to study the feasibility of this candidate architecture. They collaborate in the definition of appropriate interfaces to facilitate smooth communication among the various subsystems.</td></tr></table>

Let us consider a scenario from our case study to illustrate such knowledge fragmentation. When software architects make crucial architectural decisions, they have to consider a variety of constraints that impact these decisions (depicted in Fig. 1). They refer to the requirements specifications, created by an analyst, to recognize the impact of any functional or non-functional requirement that is architecturally significant. They discuss the feasibility of a particular architectural alternative with the implementers. During this process, they refer to business process documents generated by analysts and current business process execution environments to identify possible impact on architecture. This necessitates communication with analysts, designers, implementers, architecture reviewers, and business process analysts to acquire knowledge that is relevant to the current decision-making scenario. Fig. 1 shows the different stakeholders with whom the architect communicates, and the different chunks of knowledge that the architect may refer to and use in during this activity. Knowledge elements required by the architect are distributed across different sources: stakeholders, documents, and models, thereby impeding their use by the stakeholders who need them.

![](/api/attachments/7CSEJYAC/fulltext/images/3b2209242bf32ae182650617ea3cc902c1af5c4132aa88c2c13c5304befb788f.jpg)  
Fig. 1. Example scenario—architect integrating knowledge to make an architectural decision.

Integration of distributed knowledge becomes essential to facilitate effective decision making in knowledge-intensive and collaborative software development environments. Past research has highlighted the importance of knowledge integration in the context of design collaboration [27]. Although current GDN support systems provide useful capabilities, they result in the creation of islands of knowledge that are isolated from one another, thereby restricting the stakeholders from gaining a holistic understanding of the situation at hand. For instance, in the above scenario, the architect refers to text documents that are created using MS Word (critical architectural factors to consider, which might have been sent to him/her as an e-mail note from a codesigner) and clarifications on business processes that might be stored as transcripts of a chat session between the architect and a business analyst. These knowledge chunks are fragmented and distributed across diverse work environments, thereby providing only a restricted understanding of the scenario to the architect. We argue that integrating these islands of knowledge will facilitate better decision making.

In summary, we argue that collaborative software development involves complex GDN activities. These GDN activities can be performed effectively by integrating knowledge that is distributed. Current GDN support tools provide considerable support for the various GDN activities discussed in Section 2.1 at different levels and focus. We argue that the process of GDN in collaborative software development can be improved by augmenting current GDN systems with capabilities to support knowledge integration.

## 4. Knowledge integration using traceability

## 4.1. Knowledge integration

Knowledge integration is defined as the synthesis of individuals’ specialized knowledge into situationspecific systemic knowledge [1]. Prior research on knowledge integration has primarily focused on organizational knowledge integration. Knowledge integra tion is referred to as the integration of individuals specialized knowledge to create organizational value [30]. It is also referred to as the pooling and recombination of individuals’ tacit knowledge to create group level knowledge [17]. Here, we define knowledge integration as the synthesis of specialized knowledge that is distributed across different artifacts and phases of software development life cycle, into systemic knowledge. We argue that such a synthesis of specialized knowledge will facilitate effective decision making during software development.

Various knowledge integration mechanisms have been proposed by past research [1,19,30]. Using operational manuals with formalized procedures and directives that embody the knowledge of a number of specialists is one of the common mechanisms used for knowledge integration. Organizational routines become essential when we are considering integration of tacit knowledge. For complex and non-routine tasks, having self-managed teams is considered to be an effective knowledge integration mechanism.

Past research has recognized several challenges faced in knowledge integration. Alavi and Tiwana [1] discuss these challenges in the context of virtual teams. Constraints on transactive memory, insufficient mutual understanding, failure in sharing and retaining contextual knowledge, and inflexibility of organizational ties are identified as some of the common challenges faced in integrating knowledge [1]:

<sup>!</sup> Transactive memory helps stakeholders to pool in their tacit knowledge to perform collective tasks [1]. Yellow pages and searchable libraries of codified knowledge are the suggested solutions to reduce the constraints on transactive memory [15].

<sup>!</sup> Mutual understanding is referred to as the common ground between the team members who communicate and collaborate. Mutual understanding enhances comprehension and interpretation of the knowledge that is communicated [37].

<sup>!</sup> Prior literature warns that failure to share and retain contextual knowledge leads to misunderstanding and misinterpretation among stakeholders [1]. Prior research, while highlighting the importance of uniquely held knowledge, argues that communication among team members usually focuses on commonly held knowledge and tends to overlook uniquely held knowledge [57]. Due to such a focus, uniquely held knowledge fails to draw attention and is often not retained [12].

<sup>!</sup> Organizational ties become essential between the various teams involved in the development process [1].

## 4.2. Traceability as a knowledge integration mechanism

We propose knowledge traceability as an effective approach to integrate knowledge to support GDN in collaborative software development. Knowledge traceability is defined as the ability to follow the life of physical or conceptual artifacts that represent knowledge fragments, from its origins to its deployment and use [28]. Traceability has been considered as an important quality attribute, and many standards require the establishment of traceability documents [51]. Traceability is intended to ensure alignment between stakeholder requirements and the various outputs of the system development process.

In general, establishing traceability involves the development of a traceability model and a prototype system that supports the model. We argue that the traceability model along with the traceability support system will serve as an effective knowledge integration approach. The following aspects of traceability make it an effective knowledge integration mechanism for GDN activities in the context of collaborative software development:

1. The traceability model acts as a common vocabulary across the stakeholders involved in the software development process. This model also serves as a directive in that it guides stakeholders in the acquisition and use of knowledge in GDN activities. Using a model as a guide solves the problem of lack of structure and knowledge on what kind of knowledge elements to capture and at what level of granularity during GDN processes. For example, during the design stage, the designer might not know what kind of rationale should be captured to document the reasons underlying key design decisions, and how to link them to different artifacts. Having a traceability model directs the designer in identifying the knowledge elements that will be most valuable during later stages of development.

2. The traceability tool acts as a platform that links the various knowledge chunks that are distributed across different stakeholders and their systems. One of the common problems in integrating knowledge that is distributed is that these pieces of knowledge exist in a wide variety of environments, like e-mail accounts of stakeholders, MS Word documents, Rational Rose models, and possibly in transcripts of chat sessions. Having a tool that seamlessly integrates knowledge from each of these environments without forcing the user to switch environments will be very useful in reduc ing the overhead in integrating knowledge.

3. Traceability models, in conjunction with appropriate traceability tools, mitigate some of the common challenges in knowledge integration. Past research has highlighted several challenges faced in integrating distributed knowledge [1]. Constraints on transactive memory, insufficient mutual understanding, failure in sharing and retaining contextual knowledge, and inflexibility of organizational ties are some of the critical challenges that could be addressed by an appropriate combination of a traceability model and tool [1]. The traceability model constitutes a common vocabulary, thereby providing a common ground among the various stakeholders involved.

A traceability approach that integrates knowledge that is distributed and fragmented across different artifacts, stakeholders, and phases of the software development life cycle addresses key challenges in knowledge integration.

## 4.3. Requirements for supporting knowledge integration for group decision and negotiation

To provide effective knowledge integration support for group decision and negotiation activities involved in collaborative software development, we have identified the following capabilities as essential:

A traceability framework for the specification of knowledge elements that are to be integrated: This will serve as a directive for codifying fragmented knowledge, thereby reducing constraints on transactive memory. This will serve as a common vocabulary among the stakeholders, thereby enhancing mutual understanding among them. A prototype system that can support the acquisition, integration, and use of various knowledge elements: This system should have the following capabilities:

1. Common vocabulary to support knowledge sharing: This provides a common understanding among the different stakeholders involved in the software development process as to what kind of knowledge is to be acquired and used.

2. Facility to share knowledge instances: Any stakeholder involved in the process should be able to access elements of knowledge acquired by any other stakeholder. This will facilitate sharing of contextual knowledge to provide a systemic view.

3. Surfacing assumptions and constraints: Assumptions and constraints that are discussed using various communication tools and those that are represented in work process tools should be surfaced so as to provide a holistic view of the scenario. This will also ensure that all alternatives have adequate support.

4. Ensuring consistency: Fragmented islands of knowledge that are distributed across different stakeholder environments and different contexts need to be checked for consistency. Integrating the distributed knowledge chunks will help surface such inconsistencies.

5. Integrating work process environments: This refers to seamless integration with work process and productivity environments in which GDN activities are performed. Such integration will motivate integration and use of knowledge that may play a crucial role in shaping design decisions.

## 5. Our approach

Our approach to developing an effective traceability-based solution involves the following:

1. Development of a traceability model: The traceability model will define what knowledge is to be captured and how different knowledge elements are to be related to each other. It may be tailored to suit different kinds of projects.

2. Development of a prototype system that supports the traceability model in the current project environment.

3. Examining the usefulness of the traceability model and the prototype system in practical scenarios.

These are discussed in the subsections below. Further, we also illustrate the use of our approach by highlighting the use of our prototype system in the context of the case study discussed in Section 3.

## 5.1. Traceability framework

We have developed a traceability framework (shown in Fig. 2) for representing traceability among various knowledge fragments produced during the various phases of software development. This framework provides primitives to represent the agents, inputs, and outputs of the system development process, as well as the linkages among them. The framework is based on reference models for traceability developed in the context of complex system engineering activities [51]. The reference models have been applied in a variety of domains including new product development, concurrent engineering, and software development.

Here, the primary focus is on managing traceability across the various knowledge fragments that are created during GDN activities that occur in the context of software development. Examples of knowledge fragments include design artifacts, process knowledge fragments such as rationale, and project management artifacts such as a project plan. These knowledge fragments may be documented in a variety of tools and environments used in software development. These include asynchronous and synchronous communication tools, argumentation tools, peer-to-peer communication tools, work productivity tools, computer-aided software engineering tools, etc. These knowledge fragments are created, modified, and used by a variety of stakeholders involved in software engineering activities, including project managers, designers, and maintainers.

Our framework is intended to represent knowledge fragments in the following dimensions:

<sup>!</sup> What knowledge is represented? This represents the semantics of captured knowledge with metadata and salient attributes. The knowledge fragments shown in the figure may be specialized to represent what knowledge is to be acquired and used. Some examples of knowledge fragments are design decisions, rationale behind these decisions, requirements, constraints on requirements, design elements, etc. Depending on project characteristics, project managers can use specific primitives from argumentation and design rationale models to represent this dimension.

![](/api/attachments/7CSEJYAC/fulltext/images/28be7504042f7578724067e0fc8e36fa2ac48a1d36a0f4174850fcb6dfca91c3.jpg)  
Fig. 2. Knowledge traceability framework.

<sup>!</sup> Who are the stakeholders playing different roles in the creation, maintenance, and use of various knowledge components so as to provide pointers to the sources of tacit knowledge where the limits of codification are reached? Here, the stakeholder node shown in the figure may be specialized as project managers, designers, software architects, implementers, testers, customers, etc.

<sup>!</sup> Where is the knowledge located within the knowledge network, in terms of sources that <sup>b</sup>document<sup>Q</sup> the knowledge chunks so that it can be accessed through the use of mediators based on the understanding of the capabilities of the sources? The source node indicates the physical location of the knowledge fragment. Knowledge fragments may be distributed across different systems used by various stakeholders. Knowledge could be embedded into various work process, productivity, communication, and collaboration tools used by the stakeholders. For instance, they could be embedded in e-mail messages, chat transcripts, specification and design documents created using word processors, project plans, and elements within group collaboration tools like Groove, etc.

<sup>!</sup> How is this knowledge represented both by formal and informal means and how does it relate to other knowledge components? Instead of representing knowledge traceability in text or matrix form, we argue that representing it as a visual, semantic network will facilitate better acquisition and use. Depending on project constraints, the level of formality may vary. Our traceability approach is semi-formal in that analytical representations of constructs are not forced, and the stakeholders define the concepts in the network, thereby restricting the type of knowledge to be represented.

<sup>!</sup> Why was a certain knowledge component created, modified, or evolved? This is a special type of knowledge fragment, viz., the design rationale behind decisions taken during the various activities in software development.

<sup>!</sup> When was the knowledge component captured, modified, or evolved? Each node in the traceability framework may have its own set of properties. Some examples of properties for these nodes would be date/time the node was created and belief status of the node.

## 5.2. Prototype system to support knowledge integration in GDN activities

We have developed Process Knowledge Tracer (PKTracer), a prototype traceability system that supports the framework shown in Fig. 2. This system supports knowledge networking among distributed collaborative development team members by establishing a semantic net representing the association among various knowledge components drawn from different tools. Satisfying the requirements identified in Section 4.3, this tool provides a variety of services to support group decision and negotiation activities. Table 2 demonstrates mapping between the requirements stated in Section 4.3 and the capabilities of our prototype system:

## 5.2.1. Knowledge integration in PKTracer

We have developed three approaches for integrating knowledge fragments that are located in different tools and environments:

1. Knowledge access strategy, which we term as level 1, involves loose integrations of tools in which a tool may be invoked from another tool using a predefined interface, but the knowledge fragments are managed only from within respective tools. For example, our system provides an interface that can be readily invoked from within any system that provides a facility to invoke a web browser. Although this strategy is the most convenient and requires almost no customization, the integration achieved is very limited. A major drawback is that this strategy keeps the knowledge in the tools in their native environments and does not allow knowledge sharing among tools.

2. A second strategy (level 2 or knowledge sharing strategy) involves the ability to manage knowledge fragments contained in one tool from another. This provides the ability to add, modify, and delete contents of the knowledge base maintained in one tool from another. This second strategy is intended to provide the ability to share knowledge between tools seamlessly. A convenient approach to such integration is to invoke components of knowledge held in a tool directly rather than through its graphical interface. The user can stay within their work context and transfer knowledge components to other tools seamlessly. Such knowledge can then be accessed within our environment for further elaboration and discussion.

Table 2  
Mapping requirements for knowledge integration to capabilities of PKTracer

<table><tr><td>Requirement for knowledge integration support</td><td>Capability of PKTracer</td></tr><tr><td>(1) Common vocabulary to support knowledge sharing</td><td>Support for a traceability framework as the one shown in Fig. 2. This framework can be tailored to suit to different kinds of projects.</td></tr><tr><td>(2) Facility to share knowledge instances</td><td>Facilitation of multi-user support, thereby enabling knowledge sharing across multiple stakeholders.</td></tr><tr><td>(3) Surfacing of assumptions and constraints</td><td>Maintenance of assumptions and constraints on the associations. For example, if an assumption is surfaced in a NetMeeting session that justifies a design object (e.g., a class definition) within Rational Rose, the integrated environment can alert the decision maker that the design object needs to be revised. Forward and backward traceability of decisions to assumptions, constraints, and alternatives ensures the verification of completeness of the problem and solution specifications. For example, before a negotiation proceeds, the system can ensure that all the alternatives have valid support.</td></tr><tr><td>(4) Ensuring of consistency</td><td>Maintenance of consistency of the knowledge components specified in different tools. For example, if a discussion between two designers within their e-mail exchanges makes an assumption that is contradicted by discussions within the NetMeeting session, having the ability to surface them and link them to appropriate objects is likely to result in the identification of the inconsistency. This can be supported at different levels of automation, depending on the formality with which these objects and links are specified in the system.</td></tr><tr><td>(5) Integration of work process environments</td><td>Maintenance of dependency information among knowledge fragments that exist in developers&#x27; work environment; Many work process tools that store this knowledge do not support such dependency management.</td></tr></table>

3. Level 3 or knowledge-mapping strategy involves maintaining a knowledge map that represents the various knowledge fragments and their respective sources within various tools; the ability to access this knowledge will largely depend on the facilities of knowledge integration provided by the respective tools. This strategy calls for the development of traceability across artifacts maintained within different tools. Unlike typical traceability tools that require duplication of information within their repositories, this approach calls for the maintenance of only a semantic map of information contained in various tools. By creating a network of traceability links between different sources of information, the user can <sup>d</sup>traverse<sup>T</sup> across various tools to invoke their respective functionalities. However, providing such a high level integration requires the creation of a metamodel representing the <sup>b</sup>schema<sup>Q</sup> of knowledge contained in various tools.

Each of the strategies places different requirements on the integrated tools, ranging from providing access to the data contained within its repositories to sharing their <sup>b</sup>schema,<sup>Q</sup> which can be incorporated within a knowledge traceability tool. PKTracer supports the three strategies discussed above.

This system provides facilities to specify and instantiate a framework such as the one shown in Fig. 2. For example, a model such as the REMAP or IBIS can be instantiated within this tool to support asynchronous deliberations among members of a design team. PKTracer has an interface that can be readily invoked from other tools, thereby illustrating level 1 integration. Level 2 integration strategy is supported with a selected set of collaboration tools like Microsoft Outlook, Word, NetMeeting, Project, and

Rational Rose. PKTracer provides macros or scripts for these tools, with which knowledge fragments from these tools can be extracted and exported to PKTracer knowledge base. This strategy is especially useful in tools that do not support structured knowledge representation. The knowledge extracted from these tools, say as fragments of conversations conducted within NetMeeting or in e-mail exchanges within Microsoft Outlook, can be stored within the structured knowledge base of PKTracer.

In this paper, we focus on level 3 integration involving the creation of knowledge maps. Whereas level 1 strategy is too restricted (to just tool invocation), level 2 strategy has the potential to lead to problems of synchronization of copies of knowledge fragments in different tools. Level 3 strategy, in contrast, is more generic and avoids problems of redundancy. This strategy is supported with a knowledge traceability network for structuring and capturing knowledge exchanged during collaborative activities, where feasible. One of the common problems is that the tools that need to be integrated do not publish their knowledge schemas; tool-specific code needs to be developed to represent the knowledge maps to access knowledge fragments in these tools. PKTracer provides such an integration with Rational Rose, Microsoft Project, and Groove. These approaches to knowledge integration within PKTracer are illustrated in the following section with scenarios drawn from a case study.

The architecture for our prototype has been designed in such a manner that it facilitates the three strategies outlined above. Fig. 3 depicts the architecture of our prototype system.

## 5.3. Supporting GDN activities using PKTracer

To illustrate our approach to knowledge integration using PKTracer, we first present scenarios on the use of PKTracer and tools used by software developers in our case study. Then we discuss how the three integration strategies are supported with PKTracer.

Before the commencement of the project, the project manager has to define the traceability model in PKTracer to guide the other project stakeholders in deciding what knowledge to capture and how. After defining the underlying traceability model, the project stakeholders are free to instantiate this model for various scenarios during the entire development life cycle. Such instances are to be captured in PKTracer and should be linked to appropriate artifacts that are developed during the development process.

![](/api/attachments/7CSEJYAC/fulltext/images/4e79aaf7afbec7297e80625b9f3cdab3ba7d102b2f82757ab411155b6fba8a1b.jpg)  
Fig. 3. Architecture of PKTracer.

Let us consider a scenario in analysis discipline of the Rational Unified Process used by HospCom. Here, the project manager defines the data types for the various knowledge elements to be represented in PKTracer based on the REMAP model. These knowl edge elements are shown as tool bar items (Fig. 4). Such a definition of traceability model illustrates the capability that satisfies the requirement to provide a <sup>d</sup>common vocabulary to provide knowledge sharing (requirement (1) in Table 2). One of the analysts raises a concern about modeling a particular requirement. As part of the TV management functionality, patients can use their telephones to send <sup>d</sup>switch<sup>T</sup> and <sup>d</sup>channel change<sup>T</sup> requests to the television in their rooms. Such requests are transmitted from the telephone to the private automatic branch exchange and then to the HospCom server through a serial port. The HospCom server recognizes this message, interprets it, and then sends appropriate messages to the corresponding TV controller to perform what is requested by the patient. The requirement that the patient can request for a <sup>d</sup>TV switch-on<sup>T</sup> raises an issue about the requestor. Is the patient the requestor, or is the serial communication component that is sending the actual request to the HospCom server the requestor? This issue is documented in PKTracer by instantiating the <sup>b</sup>issue<sup>Q</sup> node from the toolbar (refer to Fig. 4). A couple of alternatives are proposed by design team members. One suggests that the patient is the requestor, and the other suggests that the serial communication component is the requestor. These alternatives are captured as instances of the <sup>b</sup>alternative<sup>Q</sup> node. The assumption that the patient is the originator for the request and that the serial communication component is not external to the system supports the former argument. The assumption that the serial communication port is external to the system supports the latter argument. These assumptions are surfaced by explicitly representing them in PKTracer. Support for multiple stakeholders to suggest alternatives, explicate assumptions, and view others’ alternatives and assumptions demonstrates the capability of PKTracer to satisfy requirements (2) and (3) in Table 2 (<sup>d</sup>facilitating the sharing of knowledge element instances<sup>T</sup> and <sup>d</sup>surfacing assumptions and constraints<sup>T</sup>). Based on the validity of the assumptions that support the former argument, the decision that the patient will be the actor is taken. If the decision had been otherwise, the actor represented in the use case diagram will change accordingly. Fig. 4 shows the complete traceability that is captured within PKTracer.

![](/api/attachments/7CSEJYAC/fulltext/images/7e8384c0338fe25b8bd8717907b431f06c774f278b8f372823531fdf98bfa84e.jpg)  
Fig. 4. Acquiring design knowledge using PKTracer.

The above scenario also illustrates the need for collaboration among the various stakeholders to arrive at a consensus and a decision. The team uses Microsoft Outlook as the e-mail client for offline communication and NetMeeting as a conferencing and application-sharing tool. Fragments of e-mail discussion between two designers conducted with Microsoft Outlook and an online chat conducted with Net Meeting have been used to generate the knowledge fragments that are integrated (illustrating level 2 strategy). Such integration of knowledge fragments from diverse work environments facilitates support for <sup>d</sup>ensuring consistency<sup>T</sup> across the various assumptions and arguments put forward by various stakeholders, thus indicating support to requirement (4) in Table 2.

Creation of a knowledge map linking knowledge components shown in Fig. 4 with knowledge fragments in other tools using level 3 integration will be much more complex if these tools do not publish the schemas of their knowledge bases. Consider, for instance, the integration of PKTracer with Rational Rose, a commonly used CASE tool (shown in Fig. 5). PKTracer has the capability to access the various knowledge elements that reside within Rose models through the interfaces exposed by Rose. We have a developed a tree view showing all the elements in the Rose model selected by the user. Any element from this tree view can then be related to a particular node in PKTracer. After a connection is established from Rose to the PKTracer knowledge base, Rose objects can be selected and linked to any other component within PKTracer knowledge base. In our case study, changes in the use case diagram affect other diagrams like sequence diagrams representing several scenarios.

![](/api/attachments/7CSEJYAC/fulltext/images/737421aef7890a1affe140d4210df369e325ecaa5842ee18aa231485a20a387b.jpg)  
Fig. 5. Integration with Rational Rose.

Although Rose does not provide a mechanism to maintain dependencies between these two diagrams developed within itself, a knowledge map created within PKTracer can do so. This knowledge map can be used to raise alerts to the designer about affected dependencies if one of the artifacts within the model has been changed. Also, maintenance of such a dependency network will enable the designers to eliminate inconsistencies in the design. A semantic mapping of object dependencies is captured in the PKTracer database. This could be extended to various artifacts generated at different stages of the project life cycle, establishing effective traceability of artifacts across the project’s life cycle. This reinforces the support provided by PKTracer for requirements (3) and (4) stated in Table 2.

Also, some of the knowledge fragments shown in Fig. 4 are associated with specific phases or tasks in the project plan for the HospCom project. After installing PKTracer plug-ins, PKTracer’s user interface can be invoked from within MS Project, a project-planning tool. Then, any element within MS Project’s plan can be represented as a node in a knowledge map within PKTracer and linked to any other knowledge fragment within PKTracer. Knowledge fragments so represented in knowledge maps within PKTracer can readily be accessed (within their native environments) from within PKTracer. Finally, a similar strategy is used for integration of PKTracer with Groove, a peer-to-peer collaborative support system, which exposes interfaces that provide access to data that reside within Groove. Using these interfaces, we have developed connections from PKTracer to Groove. Any knowledge fragment represented in Fig. 4 can be linked to knowledge chunks that reside in Groove.

Here, we have illustrated our approach to integrating information content from a variety of sources such as synchronous collaboration tools (NetMeeting), asynchronous collaboration tools (e-mail), and work process and productivity tools (Rational Rose, MS Office Suite). The user is not only able to seamlessly access the various tools to take advantage of their unique capabilities, he/she is also able to bring together fragments of knowledge that may be scattered in these different environments, related to GDN activities. Further, we illustrate the importance of embedding these GDN environments within the context of everyday work. The ability to invoke these capabilities within the work context (say, while using Rational Rose during a design task) significantly reduces the overhead involved in their use. Further, by providing an infrastructure for level 3 integration, knowledge fragments that reside within these tools are also linked to knowledge captured from various GDSS environments. In this approach, we establish traceability among the various knowledge fragments and project artifacts. A particular discussion captured in PKTracer can also be mapped to knowledge fragments from other discussions associated with different projects. This capability facilitates the establishment of a <sup>d</sup>networked<sup>T</sup> traceability among the various knowledge fragments even across different projects.

The above illustration of integrating multiple work process and productivity tools with PKTracer demonstrates the support for seamless integration of knowledge fragments that reside across these multiple environments. This demonstrates how PKTracer satisfies the requirement to <sup>d</sup>integrate multiple work process environments<sup>T</sup> indicated in Table 2 (as requirement (5)).

In summary, our approach provides the support required to adequately address the knowledge integration challenges. Our approach maps directly to the requirements for effectively addressing the knowledge integration challenges that are discussed in Section 4.1. The traceability framework constitutes a specification of what knowledge elements are to be integrated. Our prototype system supports knowledge sharing, flexible definition of knowledge schema, acquisition and integration of knowledge in a visual network form, consistency maintenance, and seamless integration with commonly used work process and productivity tools like MS

Word, MS Outlook, MS Project, MS NetMeeting, Rational Rose, and Groove.

## 6. Related work

In this section, we review related work on knowledge integration. The emergence of the web has led to structural, media, and multilingual interoperability problems that must be systematically addressed if the resulting information glut is to be turned into knowledge [10]. The National Science Foundation’s knowledge networking (KN) initiative calls for new levels of interactivity and increases in semantic bandwidth and cultural bandwidth among people, organizations, and communities to achieve this. Knowledge management needs an approach that integrates, rather than separates, technology-focused research and process-focused social sciences.

## 6.1. Traceability

Software development organizations use different kinds of approaches to establish traceability. One of the most common means of establishing traceability is through traceability matrices, which capture the link between different artifacts of the software development process in a tabular format [16]. Prior research also documents the usefulness of a modeloriented approach to traceability. Several traceability models have been developed based on theoretical and empirical considerations [8,11,28,50,51]. It is also emphasized that traceability approaches have to be tailored to suit specific project environments [23].

A variety of traceability tools have also been developed in the past. Gotel and Finkelstein [28] compare the use of general-purpose tools, special-purpose tools, and workbenches for requirements traceability. General-purpose tools include word processors, spreadsheets, database management systems, and hypertext editors that can be configured for traceability purposes [28]. Special-purpose tools include those that focus on well-defined activities in requirements engineering. Some examples of such tools include KJ Editor [59], which traces ideas to requirements; PORC [38], which provides traceability between interview transcripts and requirements; and T tool [56], which traces requirements to test cases. When a collection of such tools is used in concert to provide less restricted traceability, they are called as workbenches [28]. The International Council on Systems Engineering (INCOSE) provides a summary of their vendor survey of requirement management tools including the leading traceability tools [32]. Domges and Pohl [23] observe that most of the traceability tools do not provide support for projectspecific adaptation of traceability. Most of the current traceability tools provide either a predefined set of data types from which the project managers can select a subset appropriate for a project, or support for users to create new data types by copying available ones [23].

In summary, it is observed that while there are a variety of approaches and tools that strive to provide traceability support, they do not easily facilitate project-specific adaptation by supporting different models and semantics. In contrast, we focus on developing a traceability approach to support group decision and negotiation activities in collaborative software development.

## 6.2. Group decision and negotiation in software development

Negotiation techniques have been recognized as critical to the success of software development projects [6]. Several approaches have been developed in the past to guide negotiation and collaborative decision making. One of the prominent negotiation-based approaches to support software development comprises of Boehm et al.’s Theory W, the WinWin spiral model, in conjunction with a groupware tool. Several studies have been conducted in the past to investigate the negotiation patterns in software development and to assess the repeatability of the same in requirements negotiation [4–7]. Since our ap proach to knowledge integration does not impose any constraint on which phase of software development it can be used, or on the kind of negotiation model that can be used, software development teams can exploit the complementarities between our approach and the WinWin approach by appropriately tailoring the underlying model in our approach. Several other approaches to structuring negotiation and argumentation have been developed in the past [11,40,50]. These approaches can provide inputs on how to practically structure the underlying model for our approach to integrate knowledge during different phases.

## 6.3. Intelligent information integration

Increasing the value of information accessed from multiple sources is very important for achieving knowledge integration. Intelligent integration of knowledge needs to go beyond the integration of databases. Recent efforts have resulted in the development of systems that act as intelligent intermediaries between the users of information and heterogeneous sources. These include [64]:

<sup>!</sup> Tools that search for potential resources of information and facilitate access to them

<sup>!</sup> Mediator systems that access, combine, and summarize information from a variety of sources

<sup>!</sup> Smart query processors that reformulate user requests to improve the prospects of accessing relevant information

<sup>!</sup> Data mining systems that discover interesting patterns of knowledge buried in data.

Since complete automation of the mediation task is not always feasible, mediator systems typically require human intervention when changes to resources, user requirements, or mediating knowledge occur [65]. Whereas the focus of this stream of research is on establishing physical integration of knowledge sources, our work is focused on establishing logical links even across sources where such physical linking may be impossible to achieve.

## 6.4. Mediator architectures

Using a mediator architecture [63], The Stanford-IBM Manager of Multiple Information Sources (TSIMMIS) system [26] provides an integrated view of data drawn from multiple and often heterogeneous sources. The heterogeneity may occur at various levels, ranging from the type of data source, to the type and units in which data are expressed, to the structure or schema used. In contrast to other mediator systems that are focused on the information content of the sources and their relationships to the integrated view desired by the users, TSIMMIS relies on understanding the capabilities of the sources so that only queries that can have a valid answer are generated.

The Garlic project [9] focuses on the integration of multimedia information systems (which include application-specific data such as CAD drawings, medical objects, maps, etc.) from a variety of database and non-database sources. The use of an object-oriented data model of data from such media-specific data repositories and an object-oriented dialect of SQL distinguish this effort. A middleware layer is used for efficient query processing and data access. In contrast, HERMES [58] project develops a general declarative language for defining a mediator. Here, heterogeneous information sources are treated as domains capable of executing certain functions with pre-specified input and output parameters.

Mediator architectures are also concerned with physical integration of data stored in heterogeneous sources. Our approach to establishing a semantic network of traceability relationships is complementary to such approaches as it helps represent the logical relationships among the varied knowledge repositories.

## 6.5. XML/RDF in integration

Inspired by the explosive growth of the Internet, efforts such as MIX [3] (Mediation of Information using XML) focus on integrating information that is distributed across many sources. This project views the web as a distributed database and XML (or its modifications or extensions) as its data model. With the expectation that many web sources will be exporting an XML view of their data, the semantic descriptions of their content, and interface descriptions (as XML queries), this project has developed the XMAS query language to integrate information from these sources. When data repositories are not converted to XML, this approach provides wrapping technologies for translating XMAS queries or commands that are understood by the underlying systems. The On2broker [25] also provides brokering services to access semistructured information in the web based on content descriptions in HTML, XML, and RDF, relying on ontologies to make the semantics of the web documents explicit and uses semantic information for answering queries. Decker et al. [18] discuss the role of XML and RDF in creating a <sup>b</sup>semantic web<sup>Q</sup> in which the knowledge can be in a machine-processable form.

XML/RDF-based integration approaches offer an alternative way of implementing the concepts discussed in our traceability approach. We are currently investigating this strategy so that we may obtain interoperability with a wide variety of tools that support these technologies.

## 6.6. Collaborating agents

The InfoSleuth project [46] exemplifies efforts to using collaborating agents to facilitate knowledge integration by gathering knowledge from a changing set of databases and semi-structured text repositories distributed across the Internet. User requests made against a domain ontology are processed by broker agents to find other agents that can satisfy them. Resource agents support the mapping between the user queries and the information resources. Intelligent agents are another interesting technology that has the potential to augment our approach. Dependency management among elements in our knowledge network is, in fact, done using intelligent agents. We are currently investigating the use of agents to offer other services such as data aggregation, event detection, decomposition, and distribution of queries.

## 6.7. Organizational memory systems

The STARS project [41] develops a KM system that aims at capturing organizational knowledge in its most complete form to facilitate knowledge integration. This system provides facilities for representing the different perspectives of design team members, and supports conflict management and knowledge integration. While STARS takes a more formal approach to knowledge representation and conflict management, our approach facilitates the representation of semi-formal knowledge, and the detection and resolution of conflicts using a reason maintenance system.

## 6.8. Summary

Intelligent Integration of Information $( \boldsymbol { \mathrm { I } } ^ { 3 } )$ and mediated architectures are aimed at developing and demonstrating technologies that integrate information from heterogeneous sources. Specifically, the $\mathrm { I } ^ { 3 }$ initiatives focus on rapid information retrieval techniques for accessing information from large, dynamically changing databases, as well as the development of tools that will reduce the time needed to develop, maintain, and evolve large-scale integrated data systems. These research efforts are therefore complementary to the efforts on knowledge integration in that they facilitate access to distributed information sources. However, knowledge integration requires tools and techniques that go beyond distributed information access and needs capabilities for interactive knowledge creation and use. Interactivity and integra tion are essential for successful knowledge networks to increase the <sup>b</sup>semantic, knowledge, activity and cultural bandwidths among people, organizations, and communities.<sup>Q</sup> While the XML/RDF and collaborating agents are also focused on increasing the semantic bandwidth to facilitate knowledge networks with a technical focus, work on organizational memory systems focuses on the social and cultural bandwidths among people and organizations.

## 7. Discussion

Although we have successfully implemented integration with some popular tools, achieving level 3 integration with tools that have complex semantic content will require considerable effort. We are currently investigating the use of autonomous agents that will facilitate coordination among various tools by allowing exchange of content as well as presentation of information. Facilitating knowledge integration among tools has been a major concern in a variety of domains. For example, in the case of computer-aided software engineering (CASE) tools, integration is attempted typically at the presentation layer or the repository layer. Further, standard formats for data interchange (e.g., CDIF) have been proposed. Knowledge integration is receiving considerable attention in the knowledge management community as well. The development of schemes for knowledge interchange in standard formats such as KIF can be beneficial. However, as a first step, the primitive knowledge components represented in each tool must first be identified and associated with components in other tools. As our work is focused on linking unstructured content from sources such as e-mail and online discussions, the development of task-neutral ontology is likely to be challenging. We are also investigating the use of XMI (XML Metadata Interchange) as a means to share metadata information among various tools, thereby facilitating a generic integration. Finally, we are conducting empirical studies to investigate the effectiveness of the approach proposed here. A detailed analysis of costs and benefits of achieving various levels of integration is the focus of this work.

In spite of the recent advances in the capabilities to acquire, process, and exchange large volumes of information, effective knowledge integration requires addressing both human and technological dimensions. Recent technical advances have focused on managing, exchanging, and integrating explicit knowledge. However, efforts to integrate both tacit and explicit knowledge simultaneously have been very limited [53,66]. Recent research in knowledge management identifies the social, cognitive, managerial [61], and technical [31,44,45] dimensions that are critical for successful knowledge integration.

## Acknowledgements

This research was supported, in part, by a grant from the National Science Foundation, DAU External Acquisition Research Program, and Air Force Research Laboratory.

## References

[1] M. Alavi, A. Tiwana, Knowledge integration in virtual teams: the potential role of KMS, Journal of American Society for Information Science and Technology 53 (12) (2002).

[2] S. Alter, 18 Reasons why IT-reliant work systems should replace the <sup>b</sup>IT Artifact<sup>Q</sup> as the core subject matter of the IS field, Communications of the Association for Information Systems 12 (2003).

[3] C. Baru, A. Gupta, B. Ludaescher, R. Marciano, Y. Papakonstantinou, P. Velikhov, XML-based information mediation with MIX, Proceedings of Exhibitions Program of ACM SIG-MOD, 1999.

[4] B. Boehm, A. Egyed, WinWin requirements negotiation processes: a multi-project analysis, Proceedings of the 5th International Conference on Software Processes, Lisle, IL, 1998.

[5] B. Boehm, P. Bose, E. Horowitz, M.-J. Lee, Software requirements as negotiated Win conditions, Proceedings of the First International Conference on Requirements Engineering

(ICRE94), Colorado Springs, Colorado, IEEE Computer Society, 1994.

[6] B. Boehm, A. Egyed, J. Kwan, D. Port, A. Shah, R. Madachy, Using WinWin spiral model: a case study, IEEE Computer 31 (7) (1998).

[7] R. Briggs, P. Gru¨ nbacher, EasyWinWin: managing complexity in requirements negotiation with GSS, Proceedings of the Hawaii International Conference on System Sciences (HICSS), IEEE Computer Society, 2002.

[8] T. Bui, F. Bodart, P. Ma, ARBAS: a formal language to support argumentation in network-based organizations, Journal of Management Information Systems 14 (3) (1997).

[9] M.J. Carey, E. Al, Towards heterogenous multimedia information systems: the Garlic approach, Proceedings of the Fifth International Workshop on Research Issues in Data Engineering (RIDE): Distributed Object Management, Taiwan, 1995.

[10] C. Chen, J. Davies, Integrating spatial, semantic, and social structures for knowledge management, Proceedings of the Hawaii International Conference on System Sciences, Los Alamitos, CA, USA, IEEE Comp Soc, 1999.

[11] J. Conklin, M. Begeman, gIBIS: a hypertext tool for explor atory policy discussion, ACM Transactions on Office Infor mation Systems 6 (1988).

[12] C. Cramton, The mutual knowledge problem and its consequences for dispersed collaboration, Organization Science 12 (3) (2001).

[13] K. Crowston, Towards a coordination cookbook: recipes for multi-agent action, Doctoral Dissertation, MIT Sloan School of Management (1991).

[14] B. Curtis, H. Krasner, N. Iscoe, A field study of the software design process for large systems, Communications of the ACM 31 (11) (1988).

[15] T.H. Davenport, L. Prusak, Working Knowledge, Harvard Business School Press, Cambridge, MA, 1997.

[16] A.M. Davis, Software Requirements: Analysis and Specifica tion, Prentice-Hall, Inc., 1990.

[17] M. De Boer, F.A.J. van den Bosch, H.W. Volberda, Managing organizational knowledge integration in the emerging multimedia complex, Journal of Management Studies 36 (3) (1999).

[18] S. Decker, S. Melnik, F.V. Harmelen, D. Fensel, M. Klein, J. Broekstra, M. Erdmann, I. Horrocks, The semantic web: the roles of XML and RDF, IEEE Internet Computing (Septem ber–October 2000), 2000.

[19] H. Demsetz, The theory of the firm revisited, in: O.E. William son, S. Winter (Eds.), The Nature of the Firm, Oxford University Press, New York, 1991.

[20] A.R. Dennis, C. Tyran, D.R. Vogel, J.F. Nunamaker, Group support systems for strategic planning, Journal of Management Information Systems 14 (1) (1997).

[21] G. DeSanctis, R.B. Gallupe, Group decision support systems: a new frontier, Data Base 16 (2) (1985) 3 – 10.

[22] M. Doernhoefer, Surfing the net for software engineering notes, ACM SIGSOFT Software Engineering Notes 26 (4) (2001).

[23] R. Domges, K. Pohl, Adapting traceability environments to project-specific needs, Communications of the ACM 41 (12) (1998).

[24] A. Egyed, B. Boehm, Analysis of system requirement negotiation behavior patterns, Proceedings of the 7th International Conferences of Systems Engineering (INCOSE), Los Angeles, CA, 1997.

[25] D. Fensel, J. Angele, S. Decker, M. Erdmann, H.-P. Schnurr, S. Staab, R. Studer, A. Witt, On2broker: semantic-based access to information sources at the WWW, Proceedings of the World Conference on the WWW and Internet (WebNet 99), Honolulu, Hawaii, USA, 1999.

[26] H. Garcia-Molina, Y. Papakonstantinou, D. Quass, A. Rajaraman, Y. Sagiv, J. Ullman, V. Vassalos, J. Widom, The TSIM-MIS approach to mediation: data models and languages, Journal of Intelligent Information Systems 8 (2) (1997).

[27] C. Geisler, E.H. Rogers, Technological mediation for design collaboration, Proceedings of the IEEE International Professional Communication Conference, 2000.

[28] O.C.Z. Gotel, A.C.W. Finkelstein, An analysis of requirements traceability problem, Proceedings of the IEEE International Conference on Requirements Engineering, Colorado Springs, 1994.

[29] O. Gotel, A. Finkelstein, Contribution structures, Proceedings of the Second International Symposium on Requirements Engineering, 1995.

[30] R. Grant, Prospering in dynamically-competitive environments: organizational capability as knowledge integration, Organization Science 7 (4) (1996).

[31] C. Holsapple, K. Joshi, Descriptions and analysis of existing knowledge management frameworks, Proceedings of the 32nd Hawaii International Conference on System Sciences, Hawaii, 1999.

[32] INCOSE, Tools Survey: Requirements Management Tools, International Council on Systems Engineering, 2002.

[33] S.M. Kaplan, A.M. Carroll, K.J. MacGregor, Supporting collaborative process with Conversation Builder, Conference Proceedings on Organizational Computing Systems, ACM SIGOIS bulletin, vol. 12, No. 2–3, 1991.

[34] J.R. Katzenbach, D.K. Smith, The discipline of teams, Harvard Business Review 71 (2) (1993).

[35] K.L. Kraemer, J.L. King, Computer-based systems for cooperative work and group decision making, ACM Computing Surveys 20 (2) (1988).

[36] S. Kraus, M. Nirkhe, K. Sycara, Reaching agreements through argumentation: a logical model, Proceedings of the Workshop on Computational Models of Conflict Management for Cooperative Problem Solving, IJCAI ’93, Chambery, France, 1993.

[37] R. Krauss, S. Fussell, Mutual knowledge and communicative effectiveness, in: J. Galagher, R. Kraut, C. Egdio (Eds.), Intellectual Teamwork: Social and Technological Foundations of Cooperative Work, Lawrence Erlbaum, Hillsdale, NJ, 1990.

[38] D. Langford, PORC 0.41: outline description of enhancements and changes, BT Internal Report (1991).

[39] M. Lease, M. Lively, J. Leggett, Using an issue-based hypertext system to capture the software life-cycle process, Hypermedia 2 (1990).

[40] J. Lee, SIBYL: A Qualitative Decision Management System, MIT Press, Cambridge, MA, 1990.

[41] S.C.-Y. Lu, J. Cai, STARS: a socio-technical framework for integrating design knowledge over the internet, IEEE Internet Computing (September–October), 2000.

[42] T.W. Malone, K. Crowston, The interdisciplinary theory of coordination, ACM Computing Surveys 26 (1) (1994).

[43] F. Maurer, W. Regli, Weaving the web of reason, IEEE Internet Computing (September–October), 2000.

[44] D.W. McDavid, A standard for business architecture description, IBM Systems Journal 38 (1) (1999).

[45] E. Motta, K. O’Hara, N. Shadbolt, A. Stutt, Z. Zdrahal, Solving VT in VITAL: a study in model construction and knowledge reuse, International Journal of Human–Computer Studies 44 (3–4) (1996).

[46] M. Nodine, B. Perry, A. Unruh, Experience with the Info-Sleuth agent architecture, Proceedings of the AAAI-98 Workshop on Software Tools for Developing Agents, 1998.

[47] J.P. Nunamaker, A.R. Dennis, J.S. Valacich, D.R. Vogel, J. George, Electronic meeting systems to support group work, Communications Of The ACM 34 (7) (1991).

[48] J.F. Nunamaker, N.C. Romano, R.O. Briggs, A framework for collaboration and knowledge management, Proceedings of the 34th Annual Hawaii International Conference on System Sciences (HICSS-34), Maui, Hawaii, 2001.

[49] U. Patel, M.J. D’Cruz, C. Holtham, Collaborative design for virtual team collaboration: a case study of Jostling on the web, Proceedings of the Conference on Designing Interactive Systems: Processes, Practices, Methods, and Techniques, Amsterdam, The Netherlands, 1997.

[50] B. Ramesh, V. Dhar, Representing and maintaining process knowledge for large-scale systems development, IEEE Expert 9 (4) (1994 (April)).

[51] B. Ramesh, M. Jarke, Toward reference models for requirements traceability, IEEE Transactions on Software Engineering 27 (1) (2001).

[52] B. Ramesh, K. Sengupta, Multimedia in a design rationale decision support system, Decision Support Systems 15 (1995).

[53] P.N. Robillard, The role of knowledge in software development, Communications of the ACM 42 (1) (1991).

[54] W.N. Robinson, V. Volkov, Supporting the negotiation life cycle, Communication of the ACM 41 (5) (1998).

[55] M.P. Singh, Engineering Interoperation, IEEE Internet Computing (MayJune 2000), 2000.

[56] J. Sodhi, Software Engineering: Methods, Management, and CASE Tools, McGraw-Hill, 1991.

[57] G. Stasser, S. Vaughan, D. Stewart, Pooling unshared information: the benefits of knowing how access to information is distributed among group members, Organizational Behavior and Human Decision Processes 82 (1) (2000).

[58] V.S. Subrahmanian, S. Adali, A. Brink, R. Emery, J. Lu, A. Rajput, T. Rogers, R. Ross, C. Ward, HERMES: heterogenous reasoning and mediator system, Technical Report, University of Maryland, 1995.

[59] N. Takeda, A. Shiomi, K. Kawai, H. Ohiwa, Requirements analysis by the KJ Editor, Proceedings of the IEEE International Symposium on Requirements Engineering, San Diego, California, 1993.

[60] A. Tiwana, B. Ramesh, Integrating Knowledge on the Web, IEEE Internet Computing (May/June 2001), 2001.

[61] R. Van Der Spek, A. Spijkervet, Knowledge Management: Dealing Intelligently with Knowledge. Knowledge Management and Its Integrative elements, CRC Press, Boca Raton, 1997.

[62] D.B. Walz, J.J. Elam, B. Curtis, Inside a software design team: knowledge acquisition, sharing, and integration, Communica tions of the ACM 36 (10) (1993).

[63] G. Widerhold, Mediators in the architecture of future information systems, IEEE Computer 25 (1992).

[64] G. Widerhold, Intelligent Integration of Information: forward, Journal of Intelligent Information Systems 5 (1996).

[65] G. Widerhold, M. Genesereth, The conceptual basis for mediation services, IEEE Expert/Intelligent Systems and Their Applications 12 (5) (1997 (September/October)).

[66] M. Zack, Managing codified knowledge, Sloan Management Review 40 (4) (1999).

![](/api/attachments/7CSEJYAC/fulltext/images/b26f2cbdd335ea14172ec7804082ab023c0e180a8fd0ed9aea325681fdb2770f.jpg)

Kannan Mohan is an Assistant Professor of Computer Information Systems at Baruch College. Dr. Mohan received his PhD degree in Computer Information Systems from Georgia State University. His research interests include managing software product family development, providing traceability support for systems development, knowledge integration, and agile development methodologies.

![](/api/attachments/7CSEJYAC/fulltext/images/ca8ff1252194ea0d3d5e98b3f024f99f51fea25ccc94ca795344e1048a876a14.jpg)

Balasubramaniam Ramesh is a Professor of Computer Information Systems at Georgia State University. Dr. Ramesh received his PhD degree in Information Systems from New York University. His research works have appeared in several leading conferences and journals including the IEEE Transactions on Software Engineering, IEEE Expert, Annals of Software Engineering, Annals of Operations Research, Communications of the ACM, Journal of AIS,

Decision Support Systems, IEEE Computer, and IEEE Software. His research interests include supporting collaborative work with artificial intelligence, decision support and multimedia technologies in the areas of requirements engineering and traceability in systems development, concurrent engineering, NPD, knowledge management, and business process redesign.
