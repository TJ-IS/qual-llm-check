---
otero_id: 21766
otero_key: "U662VTP6"
title: "Managing process knowledge for decision support"
authors: "P Balasubramanian; Kumar Nochur; John C Henderson; M.Millie Kwan"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00041-x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Managing process knowledge for decision support

P. Balasubramanian <sup>a,)</sup>, Kumar Nochur <sup>b,1</sup>, John C. Henderson <sup>a</sup>, M. Millie Kwan <sup>a</sup>

<sup>a</sup> Information Systems Department, School of Management, Boston UniÕersity, 595 Commonwealth AÕe a641A, Boston, MA 02215, USA b RiÕerside Technology Center, Vidya Technologies, 840 Memorial DriÕe, Cambridge, MA 02139, USA

## Abstract

In this paper we describe a technique for modeling and implementing process knowledge within an organization. We begin by presenting a framework Knowledge Mill for describing the knowledge management process. Later, we elaborateŽ . on one aspect of the process — classification. In particular, we describe a goal-oriented modeling schema for capturing and organizing knowledge during the decision-making process. A patented tool ThoughtFlow Ž . e that supports the application of the goal-oriented schema is also described. In addition, a case study of using the framework and tool in a strategy deployment process, within the IT organization of a large company, is presented. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Decision support; Knowledge management; Strategy

## 1. Introduction

The existing literature on knowledge management deals mostly with the strategic aspects of this emerging discipline. However, having understood the importance of this field, managers are looking for guidelines and help to implement computerized application systems that can support knowledge management. Our focus in this paper is to provide a general framework, called the Knowledge Mill, that covers all aspects of the knowledge management process, and then to present a specific goal-oriented schema for modeling and leveraging knowledge elements in the specific context of decision-making Ž . Section 3 . A software tool, ThoughtFlowe, that implements the goal-oriented schema and facilitates the development of knowledge management solutions is also described Section 4 . Finally, we pre-Ž . sent a case study that illustrates how the Knowledge Mill framework and the ThoughtFlowe tool can be applied in a real-life engagement Section 5 .Ž .

By now, most organizations have realized that knowledge management is not a product that one can buy, but a capability that needs to be built over time. We define Knowledge Management as an organizational capability that allows people in organizations, working as individuals knowledge workers , or inŽ . teams, projects, or other such communities of interest, to create, capture, share, and leverage their collective knowledge to improve performance.

There are several elements in the definition that need additional elaboration. First, we explain what we mean by capability. A capability is a distinctive attribute of a business unit that creates value for its customers. Capabilities are measured by the value they generate for the organization. Thus, capabilities differentiate an organization from others and directly affect its performance 26 .<sup>w</sup> <sup>x</sup>

In order to deliver a capability, organizations have to identify the constituent operating drivers, such as technology, organization and processes, that build a capability. Two firms may obtain the same capability, such as knowledge management, by investing in different kinds of operating drivers, which include not only tangible infrastructure, but also process and organizational components 26 . <sup>w</sup> <sup>x</sup>

The effectiveness of a technology investment in knowledge management systems depends on how work is organized around that investment. Furthermore, the structure of the organization, including outsourcing relationships and alliances, must be aligned with the technology and the work processes that are in place 50 . For the purposes of this article, <sup>w</sup> <sup>x</sup> we will assume that the technology component of a business capability is knowledge management systems, including infrastructure investments. In the process component, we include procedures, workflows, management controls, and human resource practices. Organizational elements include relationships with other firms in the value chain, the culture of the firm as well as internal management structure.

Our definition of knowledge management rests on the ability to capture and store collective knowledge in the form of knowledge objects. A knowledge object is a module<sup>r</sup>packet of value-added information that is self-contained and that preserves the content and context from its original business setting for reuse in other settings. The challenge is in determining the key aspects of a process that will result in delivering high performance. Our first contribution is the goal-oriented modeling schema which is centered around decision-making, and which enables an organization to carefully define its knowledge objects and to seek out and organize the information that needs to be captured, stored, transferred and reused in other settings. A knowledge object could be a discrete, granular entity that is explicitly labeled as such, or it could be a composite entity that includes multiple and diverse knowledge elements and the network of cause–effect relationships between them. Teams within organizations can use these knowledge objects to obtain efficient access to the lessons learned from previous experiences, and to the process know-how that drives the enterprise.

The second contribution of this work is the Knowledge Mill, our framework for describing the key aspects of knowledge management see Fig. 1 . Ž . This framework describes the activities that are performed during the conceptualization, design, development and use of a knowledge management application.

In this framework, the process begins with the senior management of the organization knowledgeŽ steering committee clearly identifying the goals of . the application system. For example, the application system could be designed to reduce employee turnover in the IT organization that has several consultants with marketable skills SAP, C Ž <sup>q q</sup>, project management, etc. Based on such a high level goal, . we derive critical success factors CSF , that if suc- Ž . cessfully managed, will ensure competitive performance 39 . Some examples of CSF for the stated<sup>w</sup> <sup>x</sup> goal are: facilitating a vibrant knowledge community, creating knowledge repositories, etc.

After identifying the set of CSFs, the process of designing the application system begins. We divide the process of design into two components: user interface design and content<sup>r</sup>knowledge-base design. The content design itself can be accomplished by using six processes that we have identified under the Knowledge Mill framework. These processes, that need not occur sequentially, are: capture, transform, classify, maintain, discoÕer and disseminate. The capture process brings the data about events of interest into the system by capturing information Ž . experience, lessons learned from company projects and by collecting and interpreting information from sources inside and outside the organization. This can be pulled into the system before, during or after the event has occurred. Recent advances, like the use of workflow management systems, enable organizations to collect information about events during the very process of doing work.

During the transformation process, the information is attributed to its source, given context and validated, thereby making it easier to access, interpret and use. In order to perform this process, roles such as knowledge stewards 13 have been identi-<sup>w</sup> <sup>x</sup> fied. These stewards screen the content, make sure that the requisite approvals are provided by the subject matter experts, and identify and acknowledge the sources. As a result of this process, a package of material is produced that has been certified as important, and that includes the best ideas from the group as well as the perspective of the firm’s top experts.

![](/api/attachments/U662VTP6/fulltext/images/94d194427d78432e46d599ec6af7a5430eab587491926441640588871cf2421c.jpg)  
Fig. 1. The Knowledge Mill.

The classification process includes activities such as chunking, indexing, filtering and linking. As a result of this process, a classification scheme is developed and the new information is integrated and linked with the existing content. A major challenge during classification is in deciding how to divide the inputs into meaningful categories of knowledge objects. Each object should cover the context that will make it reusable in other settings while, at the same time, maintaining compactness for easy understandability. Our approach to this classification is driven by the fact that decisions are made to accomplish some kind of purpose, i.e., to achieve a goal. We, therefore, propose a goal-oriented classification schema that captures, in the form of objects in the programming sense, all the key variables that are relevant for effective decision-making. This schema is described in Section 3. Using this schema, a knowledge-base to capture content, as well as the relevant context, can be designed. As time goes by, the size of the knowledge-base required to maintain the content and support the various stakeholders can become quite large. So, using conversion rules, we can specify the logic to construct a hypertext node- Ž link model interface to navigate the knowledge-base..

Avoiding obsolescence is a major concern with knowledge-bases. Hence, a critical task is to add and delete materials and maintain freshness and currency. A knowledge-base without maintenance is worth nothing 13 , and hence we identify this as a critical process in our Knowledge Mill framework. Knowledge stewards similar to those used in the transfor-Ž mation process can be used to decide when and. where knowledge-bases need updating.

The discoÕery process identifies information from the knowledge-base to make recommendations to different stakeholders in the organization. In addition to helping knowledge-base owners discover new relationships between the knowledge objects, this is particularly useful when functional units within organizations have independently developed their own knowledge-bases. Techniques such as intelligent query answering 1,19 , data mining 12 and recom-<sup>w</sup> <sup>x</sup> <sup>w x</sup> mender 25,38 can prove to be very helpful here. <sup>w</sup> <sup>x</sup>

The dissemination process determines how people gain access to the content. The objective is to make it easy for people to find what they are looking for. Information from the knowledge-base can be used in two ways: push and pull. The early uses of the knowledge-base might be described as a pull use that is, information is pulled from the knowledge-base. This assumes that users know what they want and will get it using detailed searches. Another technique is to push the information to the users. However, this could result in information overload. The next level of dissemination might be to push releÕant content out onto the network using techniques such as collaborative filtering 14,45 .<sup>w</sup> <sup>x</sup>

The knowledge management processes that we described are a set of primary activities that need to be performed for all applications. In addition to this, there is a set of support activities that need to be performed. On of the most important activities from this set is architecture design. The benefits of a good architecture design are: reduced time-to-market for knowledge management applications, greater productivity of the development and maintenance group, improved usability and accuracy of applications and leverage of infrastructure investments.

The architecture that is chosen should be relatively stable and it should allow the integration of other best-in-class products such as discussion tools, databases, search engines, etc. This may require the architecture group to choose standards and tools that are well supported and highly integrated through clearly defined interfaces.

The choice of open system architectures provides the freedom to select components from multiple vendors and prevent over-dependence on any one source. Additionally, there would be an available talent pool, trained to use the open architectures, from which to draw additional resources.

## 2. Literature review

In a recent paper, Hansen et al. 16 described two<sup>w</sup> <sup>x</sup> approaches to knowledge management. In the first approach, called the codification approach, organizations attempt to capture knowledge in the form of objects and store them in repositories. In the second approach, called the personalization approach, organizations believe that knowledge is closely associated with the person who developed it and is shared mainly through person-to-person contacts. To support this type of knowledge sharing, they provide technologies to enable communication between knowledge workers and thereby facilitate knowledge transfer. We will use this framework for our literature review. For other perspectives, such as knowledge strategies and knowledge management systems in organizations, readers are referred to Refs. <sup>w</sup> <sup>x</sup> 5,7,10,15,34,36,37,40,48 .

Under the codification approach, one can use generic workflow management tools that let users model any decision making process or the tool can support specific decision making process models. In this paper, we provide a particular decision making process model, the goal-oriented model, to codify knowledge around decision making. This model provides the context and rationale to enable knowledge workers to understand and use the relevant knowledge objects. Other approaches to provide context can be provided using available workflow modeling tools.

The research literature refers to several workflow modeling techniques that can support the codification approach. Some of them support specific process models for specific decision making. For example, one such model is provided by the system called Project Memory 51 . This system provides a com- <sup>w</sup> <sup>x</sup> prehensive object-oriented framework, comprising of projects, users, events, meeting and documents, etc., for capturing project history. Similarly, the Process Handbook project 31 provides templates represent-<sup>w</sup> <sup>x</sup> ing organizational processes from different perspectives. These templates can be used to capture and archive organizational process knowledge. Another example of a model for capturing knowledge for design projects is gIBIS 6 . gIBIS provides a data<sup>w</sup> <sup>x</sup> structure that is based on argumentation theory to capture design rationale.

The Action Workflow approach is based on a theory of work structure as language in action. Action Workflow defines a workflow as an atomic ‘loop’ of action between a customer and a performer. The loop consists of four phases: proposal, agreement, performance and satisfaction 8,32 . The main<sup>w</sup> <sup>x</sup> purpose of this technique is to identify incompletions in coordination within processes. Another technique called the Trigger modeling technique has three central concepts: activity, actor and trigger. A trigger model is a graphic representation of the activities in a process, arranged under the role that performs it and linked by triggers that lead from one activity to the next. The analysis method provides guidelines for checking the completeness of a model 24 . <sup>w</sup> <sup>x</sup>

The Role Interaction Net RIN technique sup- Ž . ports process enactment. Based on organization role theory, RIN describes processes as a collection of role types and interactions between them. An interaction represents a process step as a bi-directional coincident state change mechanism that addresses both the communication and computational aspects among parties involved in it 46 . Another process <sup>w</sup> <sup>x</sup> model, called Regatta, is a network of task assignments, reflecting organizational authority and responsibility for performing tasks. It provides constructs for prototypical communications 49 .<sup>w</sup> <sup>x</sup>

WooRKS is an object-oriented workflow system designed to assist organizations in defining, executing, coordinating and monitoring workflows. WooRKS incorporates an organizational model for specifying actors, informational module for defining information to be handled, a time model for controlling when actions must be executed, an operator model for executing operations and a procedure model for combining these various components 2 .<sup>w</sup> <sup>x</sup> Mobile is a workflow model defined in terms of abstract data types. It includes detailed models from five major perspectives: functional, behavioral, organizational, informational and operational, as well as brief descriptions of some optional perspectives 22 . <sup>w</sup> <sup>x</sup>

InConcert is an object-oriented client-server workflow management system. The InConcert object model consists of tasks, roles and references to data objects. It also provides an event and trigger model <sup>w</sup> <sup>x</sup> 43 . The Dynamic Workflow management framework DWM provides a meta-model that acts as a Ž . template to guide analysts in identifying the role of objects and relationships in the application domain. DWM defines the basic elements of a business process and provides an integrated view from four distinct perspectives: functional, informational, behavioral and organizational 27,28 .

In addition to these special purpose systems, there are several generic techniques that exist in the process modeling literature. For example, work break down structures recursively breakdown a process into atomic tasks. Instances of this, such as PERT charts, are used in scheduling applications. PERT charts graphically depict tasks, their ordering interrelationships, and the scheduled start and stop times as well as duration of each task. Another technique is the Data Flow diagramming DFD technique. AŽ . DFD progressively in layers shows the variousŽ . components of a system such as inputs, processes and outputs. Flowcharts show the sequencing of tasks in an algorithmic fashion, and may include representations of inputs, outputs, devices and task types.

Another popular technique for recording empirical observations about a process is IDEF3. The process schematic is similar to a PERT chart but has more expressive power in defining the order of process elements, and start–stops and durations are not recorded. The object schematic is a state transition diagram for objects in the process. Elaborations provide detailed characteristics of each entity in the schematics, including a textual description and a listing of object types and instances, facts and constraints 20 . For a survey of knowledge management<sup>w</sup> <sup>x</sup> tools that support the codification approach, see Emery 11 and Ruggles 40 Table 1 .<sup>w x</sup> <sup>w x</sup> Ž .

The literature described so far relates to the codification approach. The personalization approach is essentially supported by knowledge transfer tools. These tools allow knowledge workers to ask each other questions, solve problems and trade best practice ideas. Ruggles 40 provides a list of tools that<sup>w</sup> <sup>x</sup> are available. In addition, several companies have services that allow customers to tap into their expertise using communication technologies. For example, Giga Information Group has a worldwide network called ExperNet. <sup>2</sup> This network has over 1000 IT professionals and consultants who provide answers to customer queries. This service is provided over the Internet for subscribers to the service. Another service provided by Ernst & Young, called Ernie, allows customers to start a dialogue with an Ernst & Young professional on any business issues and get back opinions, solutions and responses, delivered online. This service is also provided on a subscription basis Table 2 .Ž .

Table 1  
List of codification tools from Refs. 11,40 <sup>w</sup> <sup>x</sup>

<table><tr><td>Tool</td><td>Company</td></tr><tr><td>KnowledgeX</td><td>IBM, www.knowledgex.com</td></tr><tr><td>RetrievalWare,</td><td>Excalibur Technologies,</td></tr><tr><td>Visual RetrievalWare</td><td>www.excalib.com</td></tr><tr><td>Knowledge Organizer</td><td>Verity, www.verity.com</td></tr><tr><td>Knowledge Server/Update/Builder</td><td>Autonomy,www.autonomy.com</td></tr><tr><td>TeleSim</td><td>Thinking Tools,www.thinkingtools.com</td></tr></table>

Table 2  
List of personalization tools from Refs. 11,40 <sup>w</sup> <sup>x</sup>

<table><tr><td>Tool</td><td>Company</td></tr><tr><td>Notes</td><td>Lotus Development, www.lotus.com</td></tr><tr><td>NetMeeting</td><td>Microsoft, www.microsoft.com</td></tr><tr><td>Knowledge Server</td><td>Intraspect, www.intraspect.com</td></tr><tr><td>GrapeVINE</td><td>GrapeVINE Technologies, www.grapevine.com</td></tr></table>

Although we have described several techniques for approaching knowledge management, in this research we support the codification approach and focus on abstracting and storing knowledge specifically in the context of decision-making. We do so using the classification primitives discussed in Section 3.

## 3. Goal oriented decision-making: the process and its cognitive elements

Decision-making may be broadly construed as the process of selecting from a set of options the alternative s that are most likely to lead to desired out- Ž . comes. The process entails various steps and stages that decision-makers engage in, either explicitly or implicitly. A key knowledge management challenge in the context of decision-making is to surface tacit elements that are often not apparent, but which are crucial for improving decisions and their resultant outcomes 37 . An additional need in organizations is<sup>w</sup> <sup>x</sup> to document the thought process behind decisions in a format that can be easily reviewed by those who wish to contribute to an ongoing decision or to understand the guiding rationale behind choices already made 35 . The mandate of a learning organi- <sup>w</sup> <sup>x</sup> zation 44 requires that such shared representations<sup>w</sup> <sup>x</sup> be available to facilitate collaboration and to improve the quality of decisions. In addition, shared frameworks are also needed to enable double-loop learning 3 for improving the quality of the decision-making process itself. Researchers have also pointed out the need to provide context information along with content knowledge relating to decision events so that later users can assess the relevance of the knowledge to their situational needs.

Based on these considerations, we identify the following steps that comprise the decision-making process, and delineate the issues that are typically relevant during each step 17,30 . We also identify<sup>w</sup> <sup>x</sup> the cognitive and enactment elements involved so that we can model them in the context of managing knowledge to improve the decision-making process. The elements, italicized in the steps described below, are the basic objects or primitives of our goaloriented schema for modeling decision-making.

## 3.1. Step 1: Define the context and purpose of the decision

What is the situational background within which the decision is to be made? Is there a sense of context or ‘big picture’ that provides the perspective needed for effective decision-making? Results, events, outcomes, information and such other elements impinge on our awareness and create a need for changing or improving a situation. It is important that a sense of context be provided within which the details of the decision-making process can be understood, both during the process and as a frame of reference for those who review it later. As an example, if an investor, on hearing about a 600-point drop in the Dow Jones average, is contemplating what to do with her stock investments, the context for her decision could be stated as: 10% single-day drop in the Dow Jones average.

Every decision is framed by an implicit or explicit sense of purpose 35 . A decision is typically made<sup>w</sup> <sup>x</sup> to achieve a goal, to solve a problem, or to implement a plan. We can generalize across these instances to say that a decision is driven by a goal focus. For instance, our investor might define her goal as: maintain at least 70% of the value of my stock-market portfolio in the near term.

The outputs of this step are a specification of the context and a statement of goals or objectiÕes. Goals and objectives are often defined in a hierarchy, in terms of multiple objectives contributing towards a parent goal. Note that a decision can be framed by multiple, and often conflicting, goals. If the purpose behind making a decision is not clear, the process is seriously handicapped by a lack of direction and focus.

## 3.2. Step 2: Identify or generate the options to be considered

Decision-making implies a choice from among two or more options. In many situations, the choice of doing nothing, i.e., sustaining the status quo, is also a relevant alternative vis a vis the opportunity to do something new or different. The crux of decision-making entails the selection of option sŽ . that will best help to achieve goals. While some options may be obvious in a given situation, the generation of non-obvious or creative options is often neglected, due to time pressures and other reasons, leading to sub-optimal decisions 41 . In the example of our investor, she may identify options such as: sell all stocks, sell some selected stocks, do nothing, buy stocks at a lower price, etc.

## 3.3. Step 3: Specify factors, assumptions, reasons and other releÕant information to be considered

A decision is typically made in the context of various factors or conditions that must be satisfied to varying degrees. Some of these must be satisfied by the decision, and are often referred to as constraints. Others are less mandatory and are used as criteria to screen options and to guide the selection of the most suitable alternatives. Without the specification of factors, there can be no anchors or reference points to select among various options. For instance, our investor might have a binding constraint, based on her adherence to some portfolio balance theory, that she must maintain at least 50% of her investments in the form of shares in NYSE listed companies. A relevant criterion or factor might be that her investments should yield at least a 20% annualized return.

Consideration of risks and uncertainties is also a critical part of real-world decision-making. It is often helpful to consider various hypotheses or predictions in order to identify options and to assess how they might play out under various scenarios. Personal opinions, intuition, hunches and other such subjective elements are also important ingredients of the decision process. All these elements that are not objectively grounded facts, and which entail some degree of uncertainty or subjectivity, can be viewed as different kinds of assumptions that are relevant for decision-making. As an example, our investor could make an assumption that the Federal Reserve would reduce the prime rate to stabilize the stock market.

The analysis of options against factors, and under various assumptions, entails the surfacing of reasons, i.e., the rationale supporting a particular entity in the decision calculus. Reasons can be adduced to justify goals or to support specific options, factors or assumptions. For instance, our investor’s reason for justifying her assumption that the Fed would drop Ž the prime rate might be statements made by the. Federal Reserve Chairman that imply an imminent rate cut.

While it is common practice to view goals, options, factors, assumptions and reasons as different kinds of information elements, greater conceptual clarity and cognitive power can be gained by labeling these primary constructs, or primitives, into their own schematic categories, as done above, and then creating a separate information category to refer to data and other factual elements that cannot be classified, as yet, into one of those more specific categories. Facts or data can be placed in the ‘generic information category at the entry level. They could continue to exist in this category, or they can be upgraded, as and when appropriate, into more specific, higher level categories.

As an example of such transformation, consider the following for our investor’s decision situation:

she gets a newsfeed update via the Internet that Meta Logic, one of the companies in her portfolio, has entered into merger negotiations with Omega Magic. While this fact initially enters her awareness as an information element, she adds value to it by thinking of it as a reason to include Alpha Logic in her list of stocks that are not to be sold in the short term.

3.4. Step 4: Assess options against releÕant factors, assumptions and other Õariables to make the decision

This step pertains to the actual making of a decision, the other steps so far being preludes to this act. The decision-maker selects one or more options that will best contribute, singly or in combination, to the goals or objectives that define the purpose of the decision, and which are compatible with relevant factors, assumptions, reasons and other variables. The output of this step is a selection, i.e., the decision, that will contribute most optimally to the goal sŽ . made explicit in Step 1. In the example of our investor, she may decide, after considering all the variables, that she will hold on to her blue-chip stocks and sell the rest of her portfolio.

The choice of the best option s in a given situa- Ž . tion assumes that the decision-makers have some requisite content or domain knowledge that will help them evaluate all the variables of interest and arrive at a conclusion, i.e., a decision. Such domain knowledge typically resides in the minds of decisionmakers, or is sought from external sources as needed. It includes principles, concepts, theories, commonsense understanding and cause–effect relationships that apply between relevant variables. In the case of our investor, she may have known the relationships between prime rates and the valuation of specific shares in her portfolio. Or, she may have sought expert advice from an investment advisor regarding market performance under the prevailing conditions.

While content knowledge seems to be the main focus of knowledge management initiatives today, it is very important to recognize that there is yet another type of knowledge that is critical for effective performance, i.e., process knowledge. In the context of decision-making, process knowledge or know-how entails knowing how to analyze and synthesize the variables of interest, and the attendant content knowledge, in a way that leads to high quality decisions. Process know-how encompasses knowledge of the tools, frameworks or methodologies that can aid the decision-maker in a specific situation, and further knowing when and how to use them. It also includes knowledge of more general protocols, such as how to poll stakeholders, surface assumptions, resolve conflicts, arrive at a consensus, etc. For example, our investor may have used a rating system, i.e., an analytical tool for classifying different kinds of shares based on their P<sup>r</sup>E ratios.

## 3.5. Step 5: Enact the decision and reÕiew results

While the making of a decision marks the cognitive end-point of the decision process, it is useful to add one more step, decision enactment and review, that focuses attention on the effects of the decision. Enactment refers to the implementation of a decision by defining plans and deploying actions, tasks, and other such work elements that translate them into practice. Reviewing the results of an enacted decision, vis a vis the original goal s , constitutes theŽ . closing of the feedback loop and enables evaluation of the effectiveness of the decision, as well as of the decision-making process itself. If a gap is identified between the results of a decision and the original goals driving its enactment, the next iteration of the decision-making process would address how this gap could be reduced. In the example of our investor, enactment would mean placing an order with her broker to sell specific shares. Review would refer to monitoring the performance of her revised portfolio, to see if it is on target to meet her goal.

A few points should be noted about the steps described above. Many variations of these steps are possible. For example, the steps may be applied in a different sequence or in a non-linear or iterative fashion, depending on the needs of the situation. The beginning and end points could be different from what is shown above, and all the steps may not be necessary in some situations. In many real-world situations some of these steps may not even be defined explicitly, and the distinctions we have made about the steps and the elements they entail may not be very clear-cut. However, the twelve classes of elements that we have identified above, i.e., goals, decisions, problems, plans, actions, results, options, factors, reasons, assumptions, information and knowledge constitute the primary objects, or primitives, that are necessary to model the decision-making process adequately. The first six are considered primary classes and the second six are auxiliary or supporting classes. We maintain flexibility in this schema to have additional terms that are synonymous, or to introduce new terms that are tailored to a user’s environment. For instance, since goals and objectives are similar in the sense of being desired outcomes, they are both considered as belonging to the goal class, which describes a high-level taxonomy element, within which the objectiÕe label is applied as a sub-class descriptor. Similarly, the labels criterion and constraint, being similar to the label factor, are subsumed within the class defined by the factor label.

In this schema, knowledge could be a discrete, granular object that is explicitly labeled as such, or it could be a composite entity that includes multiple elements from various classes and the network of cause–effect relationships between them.

The goal-oriented decision making model described in this section subscribes to the rational model of decision making more about this in Sec-Ž tion 6 . While there are many versions of the rational. model of decision-making, they generally consist of some variation of the following steps or stages 47 :<sup>w</sup> <sup>x</sup> identify the decision or problem to be addressed; clarify and prioritize relevant goals and objectives; generate options; evaluate options with regard to their consequences and contributions towards goals; select the option s that will generate outcomes thatŽ . match the goals most closely. The elements of our schema are based on this composite view of the decision-making process.

Furthermore, Janis 23 has described a process<sup>w</sup> <sup>x</sup> called vigilant problem solving, which he states is ‘‘a realistic descriptive model of what most executives demonstrate by their actions that they are capable of doing when they try to do the best job of decisionmaking. The hallmark of high-quality decision-making is that by the time the policymakers arrive at their final choice and move towards closure, they have carried out the essential steps of vigilant problem solving.’’ The steps and underlying schema of our decision-making framework map very closely the steps and cognitive elements that comprise Janis vigilant problem-solving process: 1 Formulate the Ž . problem; 2 Use informational resources; 3 Ana-Ž . Ž . lyze and reformulate; 4 Evaluate and select.Ž .

In Section 4, we describe the architecture of a knowledge modeling tool called ThoughtFlowe, which embodies the twelve cognitive and enactment elements of this goal-oriented schema to represent, share and leverage knowledge during decision-making. In Section 5, we present a case study to illustrate how ThoughtFlowe can be applied to a strategic planning and decision-making process in the IT organization of a large company.

## 4. ThoughtFlowe architecture

Our goal-oriented schema for decision making is supported by a software tool called ThoughtFlowe Ž . Fig. 2 . In this section, we describe the architecture of the system.

There are two possible modes for interaction with the system. In the authoring mode, users define workflows, build templates, design data entry forms, specify presentation views, etc., using the primitives of ThoughtFlowe. Users instantiate specific applications of the object model by entering data into the forms or templates that have been defined based on a workflow model.

![](/api/attachments/U662VTP6/fulltext/images/e817d442658c41cdf713af08b4f404d25c80b0e42d8778572e2e1b2e426c0cbf.jpg)  
Fig. 2. The ThoughtFlow architecture.

In the browse mode, users navigate, query and view the information contained in the database using predefined views. These views could be visual treeŽ or network diagrams of the objects , or in the form. of reports, tables, etc. It should be noted that the same user could operate in both modes.

The users’ interaction with the system is primarily via the GUI layer. This layer has two components: the workflow module and the query module. Using the workflow module, the end-user can enter data into various forms and templates. This data is piped into the database via the Object Manager.

At the outset, authors have to define relationships between pre-defined objects and also define custom objects, if needed, to suit their individual needs. This definition, done through the Object Manager layer, guides both data collection and navigation through the model. The workflow logic, as described above, can be stored under this layer using the Thought-Flowe system. Under the same layer, authors can specify the business rules that govern their particular domain. For example, a bank processing a loan application may have a rule which states that applicants must have equity in their homes as collateral. This rule can be used to pre-process a loan request based on the value of the equity attribute.

Coupled to the Object Manager are various processing tools. These tools enable the user to build applications that enforce constraints between the decision elements represented by the data. For example, in a choice situation, such as buying a car, a decision matrix is constructed based on weights assigned to various factors such as cost, reliability,Ž styling, and so on and the ratings of the options on. each factor, leading to the determination of the best option. Furthermore, using this module, users could define triggers that get activated based on new infor mation entering the system.

The third layer, the database layer, stores all the data, rules, relationships and integrity constraints. The database could be relational, object oriented or some hybrid of these forms. This is accomplished by loosely coupling, using drivers such as ODBC, the Object Manager with the database management system.

In some instances, users would like to import or export data between ThoughtFlowe and other applications. For example, a user may want to export data from ThoughtFlowe to conduct AHP 42 analysis <sup>w</sup> <sup>x</sup> through Expert Choice. This is facilitated through a Data Exchange module which provides export<sup>r</sup>import protocols, such as APIs, to move data between various applications and data bases.

In the current implementation of ThoughtFlowe, the GUI layer has been programmed using Java 1.1 with Borland’s now Inprise JBuilder developmentŽ . kit. The middle layer is implemented in the form of JavaBeans objects. The back-end, MSAccess, is coupled to the Object Manager layer using ODBC drivers. The workflow capability is still under development.

## 5. Case study

The case presented here is adapted from a study of the strategic planning and implementation process at the IT organization of a large company, Alpha. Strategy management is a process that encompasses high level goal-setting, problem-solving and decision-making. Therefore, it is a good example to demonstrate our knowledge management framework for decision support. The specifics of the strategies in the case have been masked to protect the confidentiality of the data. In the following, we describe first the context and overview of the process and then show how the Knowledge Mill framework and the ThoughtFlowe framework for decision support can be applied to model it.

The leadership of Alpha IT observed that the organization is too reactive, operating in a mode where customers give the requirements and the IT organization puts a team together to build the system. They felt that IT needs to understand where the business is going, to leverage IT to effect those capabilities that will differentiate Alpha in the marketplace. Consequently, they embarked on a strategy process to establish clear priorities to guide its development plan, rationalize IT investments and focus the activities of its employees. In addition, strategic objectives were defined to assess Alpha IT’s performance.

Alpha IT’s leadership team employed a strategic planning process that is adapted from Hax and Majluf’s methodology 18 . Based on Alpha’s Vision, <sup>w</sup> <sup>x</sup> Mission and Values, its financial objectives, and the principles of a key corporate initiative called G2000, they derived a set of business driÕers which represent the demands of Alpha on the IT organization. A small number of strategic thrusts were then created that would map to these business drivers. High level executives were assigned to be owners and champions of these thrusts. They were held responsible for forming strategic thrust teams which would then deploy the thrusts by creating action programs, operational plans for these programs and measures to gauge the success in achieving the strategic intent of the thrusts. In addition, a strategic management system will be built leveraging the intranet infrastructure to promote lateral communication between employees, especially in the form of knowledge and expertise sharing, as well as upward communication in the form of grassroots participation in corporate affairs. By creating a strategic management framework and making it visible to the whole organization, the leadership team hoped that employees at all levels would be able to see where and how their work fits within the framework and contribute to the accomplishment of the strategic thrusts.

In the following, we illustrate how Knowledge Mill and ThoughtFlowe’s modeling language can be applied to the strategy management process at Alpha IT. Note that the Knowledge Mill framework suggests multiple methods of implementing each process. In a real-life situation, one or more of these methods may be employed. Sections 5.1, 5.2, 5.3, 5.4 and 5.5 maps the actual activities performed at Alpha IT into each of the processes from Capture through Dissemination of the Knowledge Mill framework. In addition, we illustrate how Classify, Maintain and Disseminate processes can be supported by the ThoughtFlowe tool. This tool is designed to provide a rational perspective into a decision making process such as strategic management. Other perspectives such as a political perspective or an emergent perspective are also useful for knowledge management purposes, but are not yet available in the ThoughtFlowe tool.

## 5.1. Capture

The strategic planning exercise was carried out by the leadership team through a process that included bi-weekly meetings and electronic discussions and document exchanges via e-mail. The strategist who coordinated the process collected these documents and e-mails as they were generated during the process. Once the strategic management system is implemented, the work products and work-in-progress of the team will be captured by the system, rather than manually.

## 5.2. Transform

The strategist selected from the collection a set of materials that captured the essence of the process, including a map of the strategic planning process, slides presented at meetings, working documents such as issues lists, team exercises and voting results, action items, summaries of team member feedback and validation by external reviewers, references such as the Hax and Majluf methodology and the G2000 program initiative, as well as the final strategic plan document. Thus, the strategist served as the ‘knowledge steward’.

## 5.3. Classify

The strategist went over the selected materials with us and explained the context of the strategic planning process — what brought about the process, who the key players were, their positions and responsibilities, and what they hoped to achieve, — as well as details of the process itself. In the classify step, we employed ThoughtFlowe’s goal-oriented schema to express the strategic planning and deployment variables at Alpha. First, we created a case for Alpha and then created the IT strategic planning process as an issue Ž . see Fig. 3A . The context was extracted from the strategic planning process document and entered as background information under the issue.

The purpose of the decisions in this issue is described by the Õision established by the leadership team. To achieve this vision, the leadership team came up with five strategic thrusts which we show in Fig. 3A as goals contributing to the vision. Note Ž that the elliptical shape of goal class elements is used in the ThoughtFlowe tree representation for elements that are labeled strategic thrusts. This is based on customizing the goal class sub-labels to include strategic thrust as a kind of goal, to reflect

usage in the IT organization. Similarly, note that the object labeled as Õision also has the ellipse icon of the goal class, to reflect the fact that a vision is a high-level goal. At the other end, an objectiÕe or target being lower level goals, they would also be classified within the goal class and represented with its identifying icon . Each strategic thrust contributes. to one or more business driÕers which were derived from three key inputs at the corporate level: a corporate initiative called G2000, the Four Equations, which embody the financial goals of Alpha, and finally, Alpha’s Vision, Mission and Values. For example, the ‘Develop human resources’ thrust aims to achieve the business driver ‘Create a high performing work environment,’ which in turn is derived from the G2000 initiative and Alpha’s Mission and Values see Fig. 3B .Ž .

Each thrust defines its own strategic intent goalŽ . and rationale. Fig. 3B shows the strategic intent of the ‘Develop human resources’ thrust, which is ‘Create a diverse environment that enables our people to be the most respected and valuable in the industry.’ The rationale that brought about this intent was based on observations of the current situation at Alpha IT. Given this intent, the thrust team designed a number of action programs planŽ . to achieve it. Fig. 3B shows one such action program ‘Form knowledge communities’. An action program may have subprograms. A subprogram for ‘Form knowledge communities’ is ‘Establish IT leadership devel-

![](/api/attachments/U662VTP6/fulltext/images/0335df2946e5eb9f563674284fc2c8bd9c5fc43087f90dad35674417b3d58831.jpg)  
Fig. 3. A Breakdown of vision into strategic thrusts. The left pane shows the primitives of the goal-oriented schema for organizing processŽ . information. The lower pane displays the roles of people who are responsible for deploying the ‘Develop human resources’ thrust. The file tabs show the various categories of information that can be stored within each item in the tree. Note that the labels of our goal-oriented schema have been customized to suit Alpha IT’s usage context. For instance, since IT personnel prefer to call their goals as thrusts, ThoughtFlow has been tailored to reflect their use of terminology. The iconic shape of the objects, as matched on the left pane palette , Ž . establishes the correspondence between the schema primitives and their customized application. B The intent, rationale and actionŽ . programs of the ‘Develop human resources’ thrust, described using ThoughtFlow. C The decision to recommend LDPs shows the factors Ž . and options considered.

![](/api/attachments/U662VTP6/fulltext/images/cb85dd834999698b73f0faa81601155a39f534e27c622b12fc92f56ee6e59473.jpg)  
Fig. 3 continued .Ž .

opment program LDP as a knowledge community’.Ž . The leader of this program defined its mission as follows: ‘Attract, retain and groom future leaders of IT by offering a best-in-class in the industry global leadership development program.’ To do so, a decision had to be made about how to develop or select such LDPs and actions had to be taken to carry out the decision.

Fig. 3C shows the decision for ‘Recommend LDPs’. The team considered two sets of factors: ‘Industry standards’ such as hands-on experiential learning, and ‘Program attributes’ such as the ability to grow and improve the program. They considered three options: Alpha leadership programs, executive programs at universities and executive programs at leading companies. Examples of the ‘Alpha programs’ option were listed. Based on the factors and the options, the team made the decisions as shown. Plans of action were made to implement these decisions. For example, to implement the decision ‘Seed IT into Business Partner programs’, one action would be to ‘strengthen business partner relationships’. Later on, the results of these actions would be reviewed and compared to the objectives of the strategic thrust.

Once knowledge of the strategic management process is classified within ThoughtFlowe objects, we can then fill in the details of the objects. This could include attaching external source documents to the appropriate objects, defining measures for goals and roles for activities, and other such details of planning and implementation. For example, the lower pane in Fig. 3B shows the roles defined for the ‘Develop human resources’ thrust.

## 5.4. Maintain

Strategic planning is a continuously evolving process. Therefore, the goal-oriented schema we have applied to describe decisions in a strategic management context will need to be updated and maintained as the process progresses. Given that the vision of the strategic management system is to promote lateral communication and general participation in strategy and planning, the schema should be maintained by all who participate in the process. The strategic management system is intended to provide secured access, based on roles, via the company’s intranet. By bringing all strategic planning activities under the same framework and system, participants can clearly see who is doing what, understand and justify the value of their work by tracing to the strategic thrusts, as well as learn from each other’s work and methods.

![](/api/attachments/U662VTP6/fulltext/images/f5771286d6ed4f0774fc643f85d04f3b5fad16ef7cca594428170dba82750bb3.jpg)  
Fig. 3 continued .Ž .

## 5.5. Disseminate and discoÕer

The strategic framework established in Thought-Flowe organizes work performed in Alpha IT so that workers can use this information to support their work. We consider three levels of questions that could be asked of this system: operational, tactical and strategic. At the operational level, a supervisor may ask, ‘‘Who should I assign to the role of analyst in the ‘Develop Human Resources’ thrust?’’ The supervisor may wish to find from the system the people who are involved in the action programs of that thrust and assign one of them to be the analyst to leverage their knowledge of the thrust. He would find that John Doe is already an analyst of the action program ‘Form knowledge communities’ and that 20% of his time has been allocated to it. Jane Smith is a manager of the program ‘Leverage workforce diversity’ and 10% of her time has been allocated to it. He may then decide to allocate an extra 10% of Jane Smith’s time to the analyst role for the thrust.

At the tactical level, a member of the strategic team may be interested in monitoring the progress of the thrust implementations. A relevant question in this context could be: What percentage of the action programs have been completed and how much have they contributed to the success of the thrust? The answer to this question can be found by selecting the completed action programs of each thrust, and then calculating the total score of the programs based on the measures defined for each thrust.

Alternatively, a manager who has been assigned to ‘strengthen business partner relationships’ may wish to see how this assignment contributes to the vision of the organization. She can find the answer by tracing the path up the tree from the activity ‘strengthen business partner relationship’ toward the strategic goals. Fig. 3C shows the rationale as follows: the activity is based on a decision to ‘seed IT into the business partner programs’ in order to leverage business partner programs as LDPs to groom future leaders. Going up the tree Fig. 3B , ‘Recom- Ž . mending LDPs’ is part of an action program to develop an IT LDP as a knowledge community. The action program is part of the ‘Form knowledge communities’ action program under the ‘Develop human resources’ strategic thrust. This thrust was justified because 1 People and their knowledge andŽ . skills are our source of competitive advantage, 2Ž . employee satisfaction is low and 3 there is anŽ . alarming growth in contractors without coordinated skills transfer. The thrust also satisfies the business driver ‘Create a high performing work environment’.

At the strategic level, a question may need to be analyzed, broken down into many questions which are then answered, and the answers are integrated to provide a single response to the original question. For example, one may ask ‘What are we doing with regard to managing culture change?’ Each of the thrust deployment program managers may find themselves involved in managing culture change in different ways. To answer this question, more sophisticated or intelligent querying techniques might need to be employed.

These examples demonstrate the ‘pull’ approach to dissemination. In the ‘push’ approach, the system may automatically send information of interest to a user. Some examples would be a notification for a pending activity, an announcement of accomplished objectives, or a monthly progress report.

We have illustrated how Knowledge Mill and ThoughtFlowe can be applied to a strategic planning and deployment process. The resulting process schema is a composite knowledge object, at the level of a ThoughtFlowe map or a tree diagram, that represents and links the relevant goals, assumptions, factors, decisions, options, rationale, actions and results. In addition, smaller, or more granular knowledge objects, such as the ‘recommend which LDPs decision, can also be defined within this process schema. These objects can potentially be reused in similar contexts.

## 6. Conclusions

In this paper we have described a framework Ž . Knowledge Mill for building knowledge management systems. In particular, we presented a goaloriented schema for capturing and organizing knowledge around decision making. We have also described the architecture and functionality of a tool Ž . ThoughtFlowe that supports the schema.

In addition, we applied this framework and the goal-oriented model to a case study. The case study showed how this methodology can be applied to the strategic planning and deployment process within the IT organization of Alpha. As a next step, we would like to introduce this prototype to the team members involved in the strategic planning exercise. Later, a preliminary evaluation of the prototype will be conducted through interviews with users. Qualitative data will be collected through interviews with stakeholders and process records to capture the key lessons from the development process. These lessons will be incorporated into the methodology for designing knowledge management systems.

As we mentioned in Section 3, the planning process described in this paper is based on the rational decision-making model. The extent to which actual organizational decision-making processes reflect a rational model has been questioned for decades. At the most extreme front is the view that organizations ‘‘muddle through’’ the decision making process, making small, incremental decisions because it is just too difficult to reach consensus on decisions which deviate substantially from the status quo. Therefore, it has been claimed that analysis, particularly of means–ends relationships found in rational models, is significantly limited 29 . However, it<sup>w</sup> <sup>x</sup> turns out that even these very unstructured decision processes can be modeled using core phases and routines fairly consistent with the rational model <sup>w</sup> <sup>x</sup> 33 . The key is including dynamic factors such as speed-ups and delays, while allowing for multiple cycles of phases or routines.

As it is now evident that decision processes deviate from a strict interpretation of the rational model, the question is how much deviation is desirable? While there is no absolute answer, evidence suggests that a higher degree of rationality is related to higher decision effectiveness 21 . Furthermore, the rational<sup>w</sup> <sup>x</sup> approach provides a clear basis for reasoned choices and does not preclude deviation from the model via the inclusion of experiential learning, the practicalities of implementation and the involvement of intuition, reflection and the interaction between thought and action 15 . Political posturing, hidden agendas, <sup>w</sup> <sup>x</sup> power plays, pet projects and such other ‘arational’ issues are often critical elements in the calculus of decision-making. A purely rational approach that ignores these subjective, personal or organizational dimensions is doomed to fail in terms of getting decisions accepted or implemented. A rational framework for decision support should accommodate and operate within the realities defined by such elements. A rational model can even be used to identify the arational elements in a way that gives better understanding or leverage in dealing with them. For this reason, we designed our system around the rational model, yet we were careful to design it with flexibility, so that it can be adapted to fit the decision-making process at hand. For example, the steps may be applied in different sequence or in a non-linear or iterative fashion, depending upon the needs of the situation.

In addition to the strategic planning process, we plan to apply the Knowledge Mill framework to several other project-based processes at Alpha, including repetitive processes such as real estate authorization, SAP implementations, and establishing<sup>r</sup> maintaining enterprise architecture standards, as well as ad hoc processes such as a project to modernize real estate facilities across Alpha. The generalizability of the framework will increase as we apply it to more processes. We are also applying this framework to processes in other organizations, including a major healthcare service provider. This will increase the generalizability of the framework across organizations.

A major impediment to knowledge management has been the lack of systematic capture of information by organizations 9 . Traditionally, organizations <sup>w</sup> <sup>x</sup> are not good at dealing with historical information about decision making. Histories are recorded only for actions that have been taken and not for ones that have been considered. This results in knowledge repositories that offer only a sampling of alternatives that were considered. Having a richer set of alternatives, as encouraged by our goal-oriented schema, can reduce the search costs involved in exploring other alternatives. In most cases, since the exploration costs can be prohibitive, there is a systematic bias against estimation. In effect, there is a bias towards Type I errors the selection of bad alterna-Ž tives . We believe that the model we are proposing . can help reduce this bias.

The current version of the ThoughtFlowe tool works in the traditional client-server environment for Windows 3.11<sup>r</sup>NT<sup>r</sup>95 in both single-user and client<sup>r</sup>server based groupware versions. A webbased cross-platform version for intranets is under development. We have begun work in implementing a Java-based version of the tool. Such a tool would help teams share the knowledge objects over a corporate intranet. Similarly, the current version of the tool only supports standard database search and retrieval. In order to support some of the advanced dissemination techniques, such as push technologies, we are exploring advanced retrieval techniques such as agent-based technologies 4 , recommender sys-<sup>w</sup> <sup>x</sup> tems 25,38 and collaborative filtering 14,45 .<sup>w x</sup> <sup>w x</sup>

## Acknowledgements

We would like to thank W. Thomas Boehm, Director of IT Strategy, Planning and Architecture at Lucent Technologies, for providing us with the context for the case study.

## References

<sup>w</sup> <sup>x</sup> 1 S. Abiteboul, D. Quass, J. McHugh, J. Widom, J. Wiener, The Lorel Query Language for semistructured data, Journal on Digital Libraries 1 1996 9.Ž .

<sup>w</sup> <sup>x</sup> 2 M. Ader, G. Lu, P. Pons, J. Monguio, L. Lopez, G.D. Michelis, M.A. Grasso, G. Vlondakis, WooRKS, An Object Oriented Workflow System for Offices, Universita di Mi-´ lano, http:<sup>rr</sup>cuiwww.unige.ch<sup>r</sup>osg<sup>r</sup>publications<sup>r</sup>ooarticles<sup>r</sup>ithaca<sup>r</sup>woorks<sup>r</sup>woorks.ps, 1994.

<sup>w</sup> <sup>x</sup> 3 C. Argyris, Teaching smart people to learn, in: C. Argyris Ž . Ed. , On Organizational Learning, Blackwell, Cambridge, 1992, pp. 84–100.

<sup>w</sup> <sup>x</sup> 4 J.M. Bradshaw, Software Agents, AAAI Press<sup>r</sup>MIT Press, Cambridge, 1997, p. 480.

5 R.E. Cole, Special issue on knowledge and the firm, California Management Review 40 1998 1–292.Ž .

<sup>w</sup> <sup>x</sup> 6 J. Conklin, M. Begeman, gIBIS: a hypertext tool for exploratory policy and discussion, ACM Transaction on Office Information Systems 6 1988 303–331.Ž .

<sup>w</sup> <sup>x</sup> 7 T.H. Davenport, L. Prusak, Working Knowledge: How Organizations Manage What they Know, 1st edn., Harvard Business School Press, Boston, 1998.

<sup>w</sup> <sup>x</sup> 8 P.J. Denning, R. Medina-Mora, Completing the loops, Interfaces 25 1995 42–57.Ž .

<sup>w</sup> <sup>x</sup> 9 V. Dhar, Associate Professor, Leonard N. Stern School of Business, New York University, The Role of Machine Learning in Organizational Learning, personal communications, 1998.

<sup>w</sup> <sup>x</sup> 10 L. Edvinsson, M. Malone, Intellectual Capital: Realizing Your Company’s True Value by Finding Its Hidden Brainpower, Harper Collins Publishers, NY, 1997.

<sup>w</sup> <sup>x</sup> 11 P. Emery, Understand knowledge management, e-Business Advisor 17 1999 14–21.Ž .

<sup>w</sup> <sup>x</sup> 12 U.M. Fayyad, G. Piatetsky-Shapiro, P. Smyth, R. Uthurusamy, Advances in Knowledge Discovery and Data Mining, AAAI Press<sup>r</sup>The MIT Press, Cambridge, 1996, p. 611.

<sup>w</sup> <sup>x</sup> 13 D.A. Garvin, A note on knowledge management, Note 9- 398-031, Harvard Business School, Boston, November 26, 1997.

<sup>w</sup> <sup>x</sup> 14 D. Goldberg, D. Nichols, B. Oki, D. Terry, Using collaborative filtering to weave an information tapestry, Communications of the ACM 35 1992 61–70.Ž .

<sup>w</sup> <sup>x</sup> 15 R. Grant, Contemporary Strategy Analysis, 3rd edn., Blackwell, Malden, 1998.

<sup>w</sup> <sup>x</sup> 16 M.T. Hansen, N. Nohria, T. Tierney, What’s your strategy for managing knowledge? Harvard Business Review, 1999, 106–116.

<sup>w</sup> <sup>x</sup> 17 E.F. Harrison, The Managerial Decision-Making Process, Houghton Mifflin, Boston, 1981.

<sup>w</sup> <sup>x</sup> 18 A.C. Hax, N.S. Majluf, The Strategy Concept and Process: A Pragmatic Approach, 2nd edn., Prentice-Hall, Upper Saddle River, 1996.

<sup>w</sup> <sup>x</sup> 19 T. Imielinski, Intelligent query answering in rule based systems, The Journal of Logic Programming 1987 229–257.Ž .

<sup>w</sup> <sup>x</sup> 20 K.B.S., IDEF3 Process Description Capture Method, Knowledge Based Systems, College Station, TX, 1995.

<sup>w</sup> <sup>x</sup> 21 J.J. Dean, M. Sharfman, Does decision process matter? A study of strategic decision-making effectiveness, Academy of Management Journal 39 1996 368–396.Ž .

<sup>w</sup> <sup>x</sup> 22 S. Jablonski, C. Bussler, Workflow Management: Modeling concepts, Architecture and Implementation, International Thomson Computer Press, 1996.

<sup>w</sup> <sup>x</sup> 23 I. Janis, Crucial Decisions: Leadership in Policymaking and Crisis Management, Free Press, 1989.

<sup>w</sup> <sup>x</sup> 24 S. Joosten, Trigger modelling for workflow analysis, Proceedings of the CON ‘94: Workflow Management, Challenges, Paradigms and Products, Oldenbourg, Vienna, 1994.

<sup>w</sup> <sup>x</sup> 25 H. Kautz, Recommender systems, Papers from the 1998 Workshop, Menlo Park, AAAI Press, California, 1998, p. 129.

<sup>w</sup> <sup>x</sup> 26 N. Kulatilaka, P. Balasubramanian, J. Storck, Managing in-

formation technology investments: a capability-based real options approach, Working Paper a96-35, Boston University, Boston, June 1996.

<sup>w</sup> <sup>x</sup> 27 M.M. Kwan, P.R. Balasubramanian, Dynamic workflow management: a framework for modeling workflows, Proceedings of the Hawaiian International Conference on System Sciences HICSS-30 , HI, 1997.Ž .

<sup>w</sup> <sup>x</sup> 28 M.M. Kwan, P.R. Balasubramanian, Adding workflow analysis techniques to the IS development toolkit, Proceedings of the Hawaiian International Conference on System Sciences Ž . HICSS-31 , HI, 1998.

<sup>w</sup> <sup>x</sup> 29 C. Lindblom, The science of muddling through, Public Administration Review 19 1959 79–88.Ž .

<sup>w</sup> <sup>x</sup> 30 R.I. Lyles, Practical Management Problem Solving and Decision Making, Van Nostrand-Reinhold, New York, 1982.

<sup>w</sup> <sup>x</sup>31 T. Malone, K. Crowston, J. Lee, B. Pentland, Tools for inventing organizations: toward a handbook of organizational processes, Proceedings of the 2nd IEEE Workshop on Enabling Technologies Infrastructure for Collaborative Enterprises, Morgantown, WV, 1993.

<sup>w</sup> <sup>x</sup>32 R. Medina-Mora, T. Winograd, R. Flores, F. Flores, The action workflow approach to workflow management technology, Proceedings of the CSCW, 1992.

<sup>w</sup> <sup>x</sup>33 H. Mintzberg, D. Raisinghani, A. Theoret, The structure of´ ˆ unstructured decision processes, Administrative Science Quarterly 21 1976 246–275.Ž .

<sup>w</sup> <sup>x</sup> 34 P. Myers, Knowledge Management and Organizational Design, Butterworth-Heinemann, Newton, 1996, p. 261.

<sup>w</sup> <sup>x</sup> 35 K.S. Nochur, From workflow to thoughtflow, Proceedings of the Groupware ‘94, San Jose, 1994.

<sup>w</sup> <sup>x</sup> 36 I. Nonaka, H. Takeuchi, The Knowledge-Creating, Oxford Univ. Press, New York, 1995.

<sup>w</sup> <sup>x</sup> 37 L. Prusak, Knowledge In Organizations, Butterworth-Heinemann, Newton, 1997, p. 261.

<sup>w</sup> <sup>x</sup> 38 P. Resnick, H. Varian, Special section: recommender systems, Communications of the ACM 40 1997 56–89.Ž .

<sup>w</sup> <sup>x</sup> 39 J.F. Rockart, Chief executives define their own data needs, Harvard Business Review 1979 81–92.Ž .

40 R. Ruggles, Knowledge Management Tools, 1st edn., Butterworth-Heinemann, Newton, 1997, p. 303.

<sup>w</sup> <sup>x</sup> 41 J.E. Russo, P.J.H. Schoemaker, Decision Traps, Doubleday<sup>r</sup>Currency, New York, 1989.

<sup>w</sup> <sup>x</sup> 42 T.L. Saaty, The Analytical Hierarchy Process, McGraw-Hill, New York, 1980.

<sup>w</sup> <sup>x</sup> 43 S. Sarin, K. Abbot, D. McCarthy, A process model and system for supporting collaborative work, Proceedings of the ACM SIGIOS Conference on Organizational Computing Systems, Atlanta, GA, 1991.

<sup>w</sup> <sup>x</sup> 44 P. Senge, The Fifth Discipline: The Art and Practice of the Learning Organization, Doubleday<sup>r</sup>Currency, New York, 1990.

<sup>w</sup> <sup>x</sup>45 U. Shardanand, P. Maes, Social information filtering: algorithms for automating ‘word of mouth’, Proceedings of the Conference on Human Factors in Computing Systems — CHI ‘95, Denver, CO, 1995.

<sup>w</sup> <sup>x</sup> 46 B. Singh, G.L. Rein, Role interaction nets RINs : a process Ž . description formalism, Technical Report CT-083-92, Micro-

electronics and Computer Technology, Austin, TX, July 22, 1992.

47 T. Stephenson, Management: A Political Activity, Macmillan, London, 1995.

<sup>w</sup> <sup>x</sup> 48 T.A. Stewart, Intellectual Capital, Doubleday<sup>r</sup>Currency, New York, 1997.

<sup>w</sup> <sup>x</sup> 49 K.D. Swenson, Visual support for reengineering work processes, Proceedings of the COOCS ‘93, 1993.

<sup>w</sup> <sup>x</sup> 50 N. Venkatraman, J.C. Henderson, Real strategies for virtual organizing, Sloan Management Review, 1998.

<sup>w</sup> <sup>x</sup> 51 M. Weiser, J. Morrison, Project memory: information management for project teams, Journal of Management Information Systems 14 1998 149–166.Ž .

![](/api/attachments/U662VTP6/fulltext/images/3b8843f14202e7db5245f0ec92cc1459da1578c0580fb5f09ebfa5eadae4cb66.jpg)

P. Balasubramanian is an assistant professor of Management Information Systems in the department of information systems, Boston University. Professor Balasubramanian received his PhD from New York University with a minor in computer science. His current research interests include designing knowledge management systems using concepts from systems design, hypertext design and workflow management, exploring the role of IT architectures in delivering

business capabilities, querying complex dynamic systems, hypermedia design and development, and model management systems. He has published papers in the Communications of the ACM, Decision Support Systems, Annals of Operations Research and in several proceeding of the Hawaii International Conference of Systems Sciences.

![](/api/attachments/U662VTP6/fulltext/images/c6083f0fe21af604db5c27bbd4d6f98724a65d94bc17db86e4392c8e93210972.jpg)

Dr. Kumar S. Nochur is the founder and chief knowledge architect of Vidya Technologies, a Cambridge, MA based company that delivers consulting, training and software services to help organizations achieve superior results in Innovation, New Product Development, Strategic Planning, Decision-Making, and R&D<sup>r</sup>Technology Management. He is the inventor of ThoughtFlowe, a patented software framework for structuring information, managing knowl-

edge, and aligning actions with goals and plans to increase effectiveness. He has taught Business Strategy at Boston University’s Graduate School of Management, and Technology Management at the University of Melbourne. As a management consultant and educator, he has worked with 3M, Amoco, AT&T BellŽ Labs , Bose, CNA, Exxon, General Electric, Gillette, Johnson and. Johnson, Lockheed, and other companies and government agencies. He has BS and MBA degrees from the University of Bombay and a PhD in Management of Technological Innovation from the Sloan School of Management at MIT.

![](/api/attachments/U662VTP6/fulltext/images/96d64723447c6dec57ce0ce46b416dabd1b8168508833163519b40d85c167cac.jpg)

Professor John C. Henderson is Chair of the Management Information Systems Department and Director of the Systems Research Center at Boston University’s School of Management. He received his PhD from the University of Texas at Austin. He is a noted researcher, consultant and executive educator with published papers appearing in journals such as Management Science, Sloan Management ReÕiew, MIS Quarterly, IBM Systems Journal, European Manage-

ment Journal, and many others. Presently his research focuses on three main areas: managing strategic partnerships, aligning business and IT strategies, and knowledge management. Prior to joining Boston University, he was a faculty member at the MIT Sloan School of Management.

![](/api/attachments/U662VTP6/fulltext/images/5a9384082ae23c8bee4c2d0c972454d4a02e61a8ed1f4a4f1dffe3f4f6e0720d.jpg)

M. Millie Kwan is a doctoral candidate in the department of information systems, Boston University. Ms. Kwan received her MS in computer science from Washington University in St. Louis and a M.L.S. in Library and Information Science from the University of Maryland. Her current research interests are in designing knowledge management systems, information systems design, workflow modeling and analysis, and IT strategy. She has published papers in the

proceedings of the Hawaii International Conference of Systems Sciences and in the proceeding of the Workshop on Information Technologies and Systems.
