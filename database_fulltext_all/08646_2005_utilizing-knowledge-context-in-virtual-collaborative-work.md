---
otero_id: 8646
otero_key: "FWBYPPTU"
title: "Utilizing knowledge context in virtual collaborative work"
authors: "Hyung Jun Ahn; Hong Joo Lee; Kyehyun Cho; Sung Joo Park"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.03.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Utilizing knowledge context in virtual collaborative work

Hyung Jun Ahn<sup>a,</sup>\*, Hong Joo Lee<sup>a</sup>, Kyehyun Cho<sup>b</sup>, Sung Joo Park<sup>a</sup>

<sup>a</sup> Graduate School of Management, Korea Advanced Institute of Science and Technology (KAIST), Cheongryangri, Dongdaemungu, Seoul 130-722, South Korea <sup>b</sup>NeoWiz Corporation, Seoul 135-090, South Korea

Available online 7 May 2004

## Abstract

The understanding of knowledge can be impaired if it is isolated from the proper context. Despite the importance of contextual information, there has been limited support for utilizing context in current knowledge management and collaborative systems. This paper presents a knowledge context model, called KC-V, which facilitates the use of contextual information in virtual collaborative work. Four benefits of using KC-V are suggested: evolutionary accumulation of knowledge aligned with collaborative activities, supporting the virtual team lifecycle, improved understanding by rich navigation paths, and searching for knowledge with similar context. A web-based collaboration system called VWSS is developed using KC-V. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Collaborative system; Virtual workspace; Knowledge context; Knowledge management; Virtual teams

## 1. Introduction

Along with the wide acceptance of the knowledge management (KM) paradigm in organizational information systems, the importance of contextual information is becoming broadly recognized. Contextual information is a crucial component for fully understanding knowledge [13,15,27,31,35]. Without proper contextual information, knowledge can be isolated from other relevant knowledge resulting in limited or distorted understanding [9,30,35]. Despite the importance of contextual information, research so far on knowledge management systems have focused mainly on facilitating full-text search, building knowledge maps of organizations, or the externalization and codification of knowledge [5,16,21,23,37,48,58]. Thus, one of the key issues in current KM research is how to facilitate the use of contextual information in KM systems.

In virtual collaboration environments, the utilization of contextual information is even more significant for several reasons. First, since virtual teams are usually organized for temporal objectives, contextual information can be easily lost between the dynamic changes [34,52]. Second, virtual teams are composed of distributed groups of people where the communication is mainly restricted to Internet-based methods, which is a narrower channel for accumulating context compared to face-to-face collaboration [20,57]. Third, the tasks of virtual teams are usually non-routine and knowledgeintensive, which require a high level of understanding along with contextual information [51,57].

Although the importance of context in virtual collaborative work is obvious, existing research on virtual collaboration and knowledge management is deficient in the utilization of contextual information. The purpose of this paper is to suggest a knowledge context model for virtual collaborative work (KC-V) to facilitate the creation, management, and utilization of knowledge. A web-based collaboration system called Virtual Workgroup Support System (VWSS) is designed and implemented based on KC-V. The benefits of using KC-V and VWSS are illustrated with examples.

This paper is organized as follows: Section 2 presents the background of the research by reviewing related studies on contextual information and virtual collaborative work. Section 3 describes how KC-V is modeled and what benefits KC-V can bring to virtual collaborative work. In Section 4, VWSS is described along with examples that show how the benefits of KC-V are realized. Section 5 presents a discussion, the summary, and the conclusion.

## 2. Background of research

## 2.1. Context and knowledge management

Context has been recognized by many KM researchers as being a crucial component to improve the understanding of knowledge. Knowledge is created in various contexts and cannot be perfectly understood when isolated from contexts [9,30,31,35]. However, it is observed that most current KM systems are limited primarily to conventional Database Management Systems (DBMS), Electronic Document Management (EDM), data warehouses and data mining tools, and intranet and extranet knowledge portals, while being deficient in supporting contextual information [16,30,37,48].

Existing research on knowledge context can be classified into two broad categories: context-based proactive delivery of knowledge, and the capture and utilization of contextual knowledge. The first type of research tries to deliver knowledge to users based on context, e.g. activities, organizational role, and work outputs. Maus [41], Abecker et al. [1,2], and Elst et al. [25] presented workflow management systems that recommend relevant knowledge to users based on the process context. Fischer and Ye [28] showed how relevant software components can be brought to software engineers depending on design contexts. In Agostini et al. [3], organizational context is modeled to provide awareness of other users’ activities in a shared workspace. The Watson system by Budzik and Hammond [11] provides users with related documents based on users’ job contents such as word-processing and Web browsing.

In the second type of research, the knowledge context itself is captured and reused rather than being used as a tool for knowledge delivery or discovery [30,35,46,50]. For example, Mittal and Paris [46] showed how contextual knowledge can be used for augmenting explanations in expert systems. In Klemke [35], it is suggested that context should be utilized as an important knowledge asset in organizational memories. Goldkuhl and Braf [30] presented a context model based on action situations to help people reuse situational contexts to solve problems. They presented an example from the home care service where home care assistants use contextual knowledge to help clients in various service situations.

The existing studies provide implications for modeling context. They show various components of context models such as activity, organization, and person. However, because they are oriented toward different goals such as workflow management systems, organizational memory, or problem solving, it is necessary to find out unique characteristics of virtual collaborative work and to derive a context model to effectively utilize contextual knowledge in such environments.

## 2.2. The knowledge context in virtual collaborative work environment

A virtual team can be described as a group of people who interact through interdependent tasks guided by common purpose working across space, time, and organizational boundaries using various communication technologies [38,44,57]. Virtual teams are project-focused; they are formed when a project arises, and disbanded when the project is completed [34,52,57]. Tasks of virtual teams are usually nonroutine and knowledge-intensive [20,38,52,57]. With the advancement of information technology and electronic business, the importance of virtual collaborative work has been increasing [36,44].

Table 1  
Characteristics of virtual teams

<table><tr><td>Characteristics</td><td>Description</td><td>Key implications</td></tr><tr><td>Project-based organizations</td><td>Project or task focused [52]Low team history [57]Temporary and transient team [34,52]Greater switching of tasks, roles or work assignments [20]</td><td>Possible loss of context information due to dynamic changes of organizations</td></tr><tr><td>Distributed and heterogeneous teaming</td><td>Physically distributed members [57]Heterogeneity in their cultural and organizational background [57]Across space, time, and organizational boundaries [38,40,44]Functionally distributed [20]Ad hoc collection of individuals [52]</td><td>Limited sharing of context; loss of context from inefficiency of communication</td></tr><tr><td>Non-routine, knowledge-intensive tasks</td><td>Novel and non-routine tasks [51,57]Interdependent tasks [38]</td><td>Needs for more thorough understanding of knowledge</td></tr></table>

For non-routine and knowledge-intensive work in virtual teams, the value of the knowledge context is clear. The unique characteristics of virtual collaborative work for the design of the knowledge context model are shown in Table 1.

## 2.2.1. Project-based organization

Since virtual teams are project or task focused, they are transient; they are often disbanded or significantly modified once the teams’ goals are completed [34,52,57]. Also, there are greater changes of tasks, roles, or work assignments in virtual teams [20]. Consequently, context information of knowledge items and skills developed during the collaboration processes might be lost after the projects are finished, limiting the understanding of knowledge created by the virtual teams.

## 2.2.2. Distributed and heterogeneous teaming

Virtual teams are often comprised of physically distributed and heterogeneous members. For example, in a virtual team for an automobile development project in a global company, there can be a product planning team, an engineering team, a design team, a manufacturing team, and part suppliers from different regions and culture [42]. The distributed and heterogeneous team structure limits the understanding and accumulation of shared knowledge, since contextual information can be easily lost and harder to accumulate because of the limited communication channel and inefficiency of interaction, compared to face-to-face collaboration.

## 2.2.3. Non-routine, knowledge-intensive tasks

Many tasks and responsibilities undertaken by virtual teams tend to be non-routine and knowledge-intensive [57]. This is because virtual teams are mainly organized for specific and temporal goals that require a high level of expertise from heterogeneous groups of people [20,51]. Thus, the knowledge generated from work can be diverse, heterogeneous, and novel. Utilizing knowledge context in such an environment is more crucial for successful understanding of shared knowledge.

It is obvious that the utilization of the knowledge context is essential for knowledge management in virtual collaborative work environments. Therefore, the knowledge context model of this paper can be a useful tool for knowledge management in terms of bridging the gap between virtual collaborative work and the knowledge repository by enabling rich creation, accumulation, and efficient utilization of knowledge (Fig. 1).

![](/api/attachments/FWBYPPTU/fulltext/images/57892202dcc9fff33244e4b11195174b0f966f08ad5a4fcd5c1e68406e2f14df.jpg)  
Fig. 1. Bridging virtual collaborative work and the knowledge repository with the knowledge context.

## 3. The knowledge context model

## 3.1. Design of the knowledge context model for virtual collaborative work (KC-V)

Since the goal of this paper is to facilitate the use of the knowledge context in the creation, accumulation, and utilization of knowledge in virtual collaborative work, an operational model of the knowledge context should be designed. In this paper, the target of the model is restricted to supporting project-based and knowledge-intensive virtual teams.

As shown in Section 2, many studies exist on context modeling. The components of context models can be classified into the four categories shown in Fig. 2 [54]. Among the four categories, three components—organization, person, and activity—can be regarded as being critical in virtual collaboration environments, while the physical circumstance component is less significant. Since virtual collaboration usually accompanies unique forms of organization and activity, the ‘organizational perspective’ and ‘activity perspective’ are added as requirements from the virtual collaborative work perspective.

## A. Organizational perspective

There are two distinctive requirements regarding the organizational perspective of virtual teams. First, virtual teams have a unique life cycle: (1) the organization of teams for temporal goals, (2) collaboration until the goals are achieved, and (3) disbanding teams after the goals are satisfied [34,57]. Thus, knowledge context should facilitate the creation of virtual teams and the accumulation of collaboration outputs along with the life cycle of virtual teams. Second, project-based roles of virtual team members such as project manager, activity manager, or ordinary members should be considered [7] since users can have different roles in different projects with varying levels of authority and responsibility in creating and utilizing knowledge.

## B. Activity perspective

Activity is used as a key component of context models in many research studies [1,2,32,41]. However, an important requirement that is missing in existing research is that the creation of knowledge should be naturally aligned with collaborative activities. That is, planning projects and sub-activities, coordinating distributed members, and gathering activity outputs should be integrated with knowledge creation work, and on the other hand, creation of knowledge should contribute to the management and coordination of activities. Otherwise, knowledge can be isolated from activity contexts and users may have to put additional efforts in accumulating knowl edge. For example, in many knowledge management systems, storing and retrieving documents is based on folder-based structures [58], and also, many collaborative systems provide task management functions that are separated from document management functions [5,24]. The alignment is especially important in virtual teams where the management and coordination of activities are performed mainly by computer-based communication technologies and most of the knowledge context should be created in virtual workspaces.

![](/api/attachments/FWBYPPTU/fulltext/images/48ded144882c2e71f1ea91ad5fa3878d4c2245ea4c6b561cdfa7cde728b74191.jpg)  
Fig. 2. Derivation of the knowledge context model based on extant research and requirements from the virtual team perspective.

KC-V was designed as shown in Fig. 3. Table 2 presents the description and the key attributes of the entities in KC-V. The main features of KC-V are explained in the following.

A. Activity and project. The activity entity plays a central role in KC-V as in many other context models. Since one of the major considerations of designing KC-V is that it should integrate the ‘management and coordination of activities’ with ‘knowledge creation’, the entities such as document, milestone, discussion, and coordination are associated with the activity entity.

In order to effectively support the management of activities, a project can have hierarchically organized activities with due dates and progress attributes. The project entity also has the lifecycle status of a virtual team as its attribute. The status is active when a virtual team is operating and inactive after the team is disbanded. After the completion of a project, the whole set of knowledge items and the hierarchy of activities in the project can be stored as a part of the project memory along with the knowledge context for reuse in the future.

B. Coordination and milestone associated with activity. In virtual collaborative environments, automated coordination mechanisms are frequently used for managing and adjusting dependencies and possible conflicts between collaborative entities, because communication among actors depends primarily on Internet-based communication technologies [38,40,44,52,53]. During coordination processes, knowledge assets are created and the status of an associated activity is changed. The

![](/api/attachments/FWBYPPTU/fulltext/images/c9da166526d4e187c3132f46006d9d6b3ddd8c4b1c64ed4c7f012bdcb4a9df69.jpg)  
Fig. 3. The knowledge context model.

Table 2  
Description of each entity in KC-V

<table><tr><td>Entity</td><td>Description</td><td>Key attributes</td></tr><tr><td rowspan="3">Activity</td><td rowspan="3">All the activities that are performed within a project lifecycle. Activities can have relationship with each other in a hierarchical way.</td><td>*</td></tr><tr><td>*</td></tr><tr><td>due date progress</td></tr><tr><td>Actor</td><td>Users responsible for carrying out activities of a project with different roles. For example, there can be roles for members such as project manager, activity manager, activity member, and guest.</td><td>*roleuser_id</td></tr><tr><td>Document</td><td>Various types of documents that contain explicit and formal knowledge ranging from word-processed documents to multi-media files.</td><td>physical_document</td></tr><tr><td>Milestone</td><td>Important points of time in an activity. A milestone can be associated with documents so that creation of a document for a milestone can automatically influence the progress of an associated activity.</td><td>progress</td></tr><tr><td>Discussion</td><td>Accumulation of informal and tacit knowledge generated by discussions among actors.</td><td>*discussion_content</td></tr><tr><td>Domain</td><td>Domain of knowledge category an activity or an actor belongs to.</td><td>namedescription</td></tr><tr><td>Project</td><td>A set of coherent activities and actors for a project. If a project reaches the end of its lifecycle status, it can be stored as project memory.</td><td>*durationlifecycle_status</td></tr><tr><td>Coordination</td><td>An abstraction of the automated coordination mechanisms that are frequently used in virtual collaboration environment. The output of coordination can generate knowledge items that can be associated with activities.</td><td>*message*</td></tr></table>

< entity> denotes an entity used as an attribute. < entity>\* denotes multiple occurrence of an entity.

coordination entity in KC-V is an abstraction of such coordination processes. KC-V associates the coordination entity with activity and knowledge item entities so that the knowledge created during coordination processes can be associated with activities.

The milestone entity denotes important points of time in activities. The milestone entity was devised to link the progress information of activities with knowledge creation, as shown in the links with the activity and document entities in KC-V. Thus, the milestone entity also enables natural alignment of knowledge creation with activity management.

C. Two types of knowledge items: document and discussion. The design of the knowledge items in KC-V is based on the widely accepted descriptions of knowledge such as in Nonaka and Takeuchi [47] and Davenport and Prusak [16], where knowledge is differentiated from data and information, and further categorized into explicit knowledge and tacit knowledge. In organizations, explicit knowledge is usually delivered in the form of books or documents, whereas tacit knowledge is transferred by communication among persons such as conversations or apprenticeships [16,59].

KC-V supports the two types of knowledge with the document and discussion entities, respectively. The document entity may represent output documents, interim or final reports of an activity, or manuals that have formal and explicit form. The discussion entity, on the other hand, represents informal and tacit knowledge generated by various forms of communication between actors.

D. Domains. Activities and actors are associated with domain entities each of which represents a specific knowledge category. Domain entities can be used for finding knowledge items created under a similar context or searching for experts in a specific expertise domain.

## 3.2. Benefits of using KC-V in virtual collaborative work

Utilizing KC-V in virtual collaborative work can bring four representative advantages: (1) Evolutionary accumulation of knowledge in natural alignment with collaborative activities, (2) supporting the virtual team lifecycle, (3) improved understanding by rich navigation paths, and (4) searching for knowledge with similar context. The four advantages are described below with illustrations using the entities and relationships in KC-V.

## 3.2.1. Evolutionary accumulation of knowledge in natural alignment with collaborative activities

KC-V can be used for evolutionary knowledge accumulation in natural alignment with collaborative activities. There are several implications: First, when a vast amount and various types of knowledge are created during a long period of a project, KC-V can provide an underlying structure with which the accumulated knowledge is organized. Thus, as shown in (i) of Fig. 4, knowledge items can be placed along with the hierarchy of activities in a project, which is advantageous over the approaches where knowledge is stored in separate folders independent of activities. This structure is beneficial both for creating project memory and retrieving knowledge from past projects. Second, ‘creating knowledge items’ can automatically update the status of activities as shown in (ii) of Fig. 4. In the figure, milestones are associated with specific progress points of activities and output knowledge items. Thus, creating and uploading a document for a milestone can trigger the update of the progress of the associated activity. Third, ‘coordination of activities’ can result in the accumulation of knowledge. As shown in (iii) of Fig. 4, a coordination cycle with structured messages can create output documents and discussions, which will be placed in the context of the associated activity (for details of coordination by structured messages, see Refs. [17,22,33,56]). In the example, a coordination cycle for Request Activity Reports is illustrated where an actor requests activity reports to another actor. While having conversations, knowledge items including the reports and conversations are created in the associated activity.

## 3.2.2. Supporting the virtual team lifecycle

KC-V can support the virtual team lifecycle as shown in Fig. 5. In the ‘creation of virtual teams’ phase, the knowledge context can be used to search for a similar project from the past in the knowledge repository and create the skeleton of a current project. In the operation phase, KC-V is used for retrieving and navigating through relevant knowledge and for accumulating knowledge in an evolutionary way. After the project is finished, the set of knowledge items can be stored as project memory in the knowledge repository along with the knowledge context for later use.

![](/api/attachments/FWBYPPTU/fulltext/images/647d2a46a09c098744efac693eb8f47fafd25e6282ee777d859515c93e7492b9.jpg)  
Fig. 4. The knowledge context is used for naturally aligning knowledge creation with collaborative activities.

![](/api/attachments/FWBYPPTU/fulltext/images/59a4c91ffc3680156428970ac9fdf4989e474cf12307fb0660548b679d408508.jpg)  
Fig. 5. The knowledge context facilitates utilization and creation of knowledge along with the lifecycle of virtual teams.

## 3.2.3. Improved understanding by rich navigation paths

KC-V provides rich navigation paths to users so that a knowledge item can be comprehensively understood in relationship with relevant knowledge items and the knowledge context. As in Fig. 6, a knowledge item can be retrieved by a user’s query. Then, using the knowledge context of the knowledge item, the user can expand the navigation to documents, projects, activities, projects, and discussions, which again can be used for further navigation. This way, the knowledge context makes it much easier to navigate through the collection of related knowledge, rescuing the knowledge item from isolation and improving its understanding.

## 3.2.4. Searching for knowledge with a similar context

The knowledge context can be used to find projects and activities with similar characteristics. As shown in Fig. 7, from a project or an activity, users can find similar projects and activities based on the knowledge context. This approach can be applied to a wide variety of business activities where non-routine and unstructured knowledge incorporated in past projects can be reused for current projects. For example, in software engineering projects, the importance of reusing past software processes and domain knowledge has been widely recognized [8,12]. The attributes such as domain, duration, and participating actors can be used to find similar projects and activities.

## 4. The Virtual Workgroup Support System

## 4.1. Virtual workspace model

In order to develop the web-based collaborative system called VWSS, a virtual workspace model

![](/api/attachments/FWBYPPTU/fulltext/images/71b65baa7570d9d95e8ba6538ea1fafb37edfb91b090e262018a4505209bda1f.jpg)  
Fig. 6. The knowledge context enables users to browse through a large set of relevant knowledge items.

![](/api/attachments/FWBYPPTU/fulltext/images/d5b8c4ec00506e22a7642869b9b2eecb5e874c4bf9c2a48516e4b79f8ed3c5ad.jpg)  
Fig. 7. Unstructured and tacit knowledge in past projects and activities can be reused for current activities.

was designed by extending KC-V (Fig. 8). The concept of the workspace was introduced to provide a place for coherent activities performed in a project. Thus, workspaces are created for projects and activities are performed within the boundaries of workspaces. Users can create workspaces for projects and can participate in one or more workspaces having roles in the projects and activities. Although the main focus of VWSS is on projectbased collaboration, routine or ad hoc activities are also supported. Routine activities are created for simple and repetitive creation of knowledge, such as periodical updating of documents. Ad hoc activities can be created for non-project activities.

Two types of discussion are supported in VWSS. The first one is threaded exchange of opinions on electronic bulletin boards denoted as Issue. Issues can be created in activities or annotated to documents so that informal knowledge from communication can be associated with them. The second one is voting activity that is denoted as Decision. Decision sessions can be open within activities when needed.

![](/api/attachments/FWBYPPTU/fulltext/images/8a91feb69e6de1ea4269b0ecfb470f080844d3c6bbcf4c5d944de87cb3731132.jpg)  
Fig. 8. The workspace model.

The structure of past projects and activities can be stored as templates (Workspace template and Activity template). The templates can be reused to build the skeleton of a similar project or activity.

## 4.2. Architecture of VWSS

As seen in Fig. 9, VWSS is basically composed of two supporting systems, the workspace management system and the coordination system. The workspace management system provides functions to manage contents in virtual workspaces including creation, copying, moving, and access control of activities and knowledge items. Structures of projects and activities can be stored as templates in the template repository so that users can reuse them in the creation phase of new virtual teams. All projects are stored in project memory when finished. The coordination system enables managers of workspaces and activities to coordinate the collaborative work of users based on structured and automated messages. VWSS currently supports the following types of coordination: Request Activity Reports, Request Activity Execution, Request Activity Due-date Change, Workspace Subscription Request, and Request Delegation of an Activity. VWSS also allows new coordination types to be defined and added to the system.

## 4.3. Introduction of the features of VWSS

## 4.3.1. Activity management

The basic building block of a virtual workspace is the activity folder: integration of ‘knowledge management’ and ‘management and coordination of activities’ (‘activity folder’ comes from this integration.). Thus, activity folders not only allow users to store and retrieve knowledge items, but also enable the management and coordination of activities. For example, users can upload documents and create discussions in an activity folder, while automatically updating the progress of the activity folder as knowledge items are accumulated. The milestone and coordination features introduced in Section 3.2 are also realized in the activity folder.

In order to facilitate easy manipulation of activity folders and knowledge items, VWSS provides functions such as copying, cutting, and pasting items in activity folders. There is also a special type of activity folder named Recycle that stores deleted items until they are permanently erased by the explicit request by users.

Fig. 10 shows an example screen of an activity folder that contains progress information, due date, sub activity folders, and authorized members. There is also a discussion issue ‘Implications of Analysis’, and a milestone ‘Final Analysis Results’. Normal folders without activity features can also be created for purely document-oriented purposes as the ‘Survey Data’ folder.

![](/api/attachments/FWBYPPTU/fulltext/images/e6c28bb8e1ccd614417c35dae8074a5a67adaa976b8dbacb185c036459ad0b9d.jpg)  
Fig. 9. Architecture of the Virtual Workgroup Support System.

![](/api/attachments/FWBYPPTU/fulltext/images/71c627de9e0c6fd21e40ad79aacf9a3bfa0ca8951469f136056004a90d21029f.jpg)  
Fig. 10. Activity folder view.

## 4.3.2. Document management

Documents in activity folders can be MIME type documents or URLs, such as word-processed documents, spreadsheets, graphic images, multi-media files, or links to HTML pages. Some helpful functions are provided for document management including version management, locking and unlocking of documents, and annotation of individual documents. With the version management function, users can upload documents and update version information while preserving older versions of documents. Older versions are not displayed when browsing the folders, but can be accessed through the links provided in the latest versions. With the locking and unlocking functions, users can set or release locks on documents, which prevent others from reading, updating, or modifying the documents. Users can create annotation boards using the issue feature for individual documents where comments and ideas on documents can be shared. For users’ convenience, the whole collection of annotations to a specific document can be transformed to a new document.

## 4.3.3. Issues and decisions

On-line discussions (issues) and voting sessions (decisions) can be associated with activity folders and documents. Issues are organized in a threaded way. When posting a reply to an article in an issue, users can declare their position as positive, negative, or neutral. These position types are displayed so that users may monitor the overall status of the issue thread. Users can also open voting sessions for issues related with a specific activity. Voting sessions can be one of the three types: selection from alternatives, five-scale evaluation of alternatives, and giving scores to alternatives between 0 and 100. VWSS allows users to define new voting sessions by writing questions and alternatives. The result of discussions and voting sessions can be stored as text documents when finished.

## 4.3.4. Multiple views of workspaces

Fig. 11 shows a screen view of VWSS that displays an overview of a selected workspace. Including this overview mode, there are six modes associated with the tabs on top of the screen that show different views of a workspace: the activity display view, document browsing view, discussion listing view, member management view, and calendar view. The activity display view enables users to browse the hierarchical activity structure, check due dates and progress of activities, and create or view knowledge items associated with the activities. The document browsing view allows users to see VWSS as an Electronic Document Management (EDM) system by showing only document-related information in hierarchical folders. The discussion listing view displays the whole list of discussions in a workspace, including all the issues and decisions. The member management view shows all the members of a workspace with their activities and roles. Finally, the calendar view enables users to see all the milestones, events, and activity schedules in their workspaces. Users can restrict the scope of the items in the calendar view by choosing a specific workspace.

![](/api/attachments/FWBYPPTU/fulltext/images/a1d57afe60e9e8dd9929ecaa07cf8020c392c564688a3fd9dbab0ba4c24e25f2.jpg)  
Fig. 11. Overview screen of VWSS.

## 4.4. Examples: utilization of the knowledge context in VWSS

The following provides examples that show the benefits of the knowledge context realized in VWSS.

## 4.4.1. Rich navigation paths and improved understanding of knowledge

The first example in Fig. 12 shows a search result that lists a set of knowledge items in the knowledge context of a document called ‘Blueprint of Train ticketing System.doc’. In ordinary knowledge management systems, it is difficult to find an extensive set of relevant knowledge as a result of a query. However, a search result of a document can show various items such as actors, activities, activity constraints, and other related documents in VWSS. From these knowledge items and the context, users can expand their navigation through the system to retrieve more knowledge items. Users may expand their exploration starting from the related activities or actors of the activity, or retrieve discussion results created during the activity. Consequently, users can improve their understanding by easily accessing various knowledge items relevant to target knowledge.

## 4.4.2. Knowledge context as a skeleton of project memory: the finishing phase of the virtual team lifecycle

Figs. 11 and 12 also show how knowledge and its context are organized along with activities. Because activity folders can represent the hierarchical structure of projects allowing creation of knowledge items, the structure of activity folders can be directly used as a skeleton of project memory, which is beneficial for users. Consequently, various attributes of projects such as due dates and participants and the extensive set of knowledge items such as output documents and discussions can be organized in a way that effectively supports the reuse of the memory later when similar projects are performed.

![](/api/attachments/FWBYPPTU/fulltext/images/1dbeedac6ddf4424f57e430db31e39581c4cb751015946147fefc72986f462ca.jpg)  
Fig. 12. Example knowledge context for a document.

4.4.3. Creation of workspaces using the structures of past projects: the creation phase of the virtual team lifecycle

Fig. 13 shows an example of workspace creation. In this example, a new workspace for the ‘Knowledge Management Survey Project in Government Sponsored Research Centers’ is being created. At the bottom of the screen, there is a list of eight workspaces whose domain attributes are either ‘knowledge management’ or ‘survey research’. Then, the user can choose the ‘Research Survey on Groupware Technology Acceptance’ workspace as a framework for organizing the project at hand. This will copy the structure of the activities in the template automatically into the current project. Before choosing a specific template, users can click the links of the templates to see the overview of the templates, as shown in Fig. 14.

## 4.4.4. Alignment of knowledge creation with activities

Fig. 15 shows how responding to a coordination message can contribute to creation of a knowledge item in an activity. In this example, a user replies to a message in a ‘Request Activity Reports’ coordination cycle with an attached document that will be placed in the associated activity. In this way, exchanging coordination messages for adjusting dependencies and conflicts in activities are naturally accompanied by knowledge creation in the relevant place along with the knowledge context.

Fig. 16 shows an example of uploading a document to a milestone. Once the document is uploaded and the milestone is marked finished, the progress of the activity is increased to 20%: the progress contribution of the milestone. Hence, as knowledge items are accumulated in an activity, the progress status of the activity can also be updated accordingly.

## 4.4.5. Finding knowledge items with similar contexts

Fig. 17 is a search result that shows a list of workspaces and activities whose domain coincides with a given activity and a workspace. In this case, the given activity belongs to the ‘Requirement Analysis’ domain and the containing workspace belongs to the ‘System Development’ domain. Based on the search result, users can further explore the activities and workspaces to retrieve other documents with similar characteristics, and find persons with experiences for similar subjects.

![](/api/attachments/FWBYPPTU/fulltext/images/7a7d1fe321ea80a991a7d535029133330ddc6b66d1f046a24d69db922b76a867.jpg)  
Fig. 13. Creation of a workspace using the structure of a past project.

## 5. Discussion and conclusion

## 5.1. Discussion

The significance of this paper can be summarized as follows: First, it has shown why utilizing knowledge context is crucial in virtual collaborative work by reviewing related research on both context and virtual collaboration. Second, a knowledge context model named KC-V was designed to facilitate the use of knowledge context in virtual collaborative work. The model was derived from context model components and requirements from virtual team characteristics. Third, a web-based collaborative system VWSS was implemented based on the knowledge context model. The benefits of using KC-V were illustrated with example usages of VWSS.

For the evaluation of KC-V and VWSS, Table 3 shows a comparison of VWSS with representative collaboration support systems, commercial workgroup environments, and context-aware collaboration systems. The comparison was based on the following three perspectives: knowledge manage-

![](/api/attachments/FWBYPPTU/fulltext/images/1f888a2b9ecf47faf8daeb97009e1a63c0dc136d0e023c1a4edf731d32c4d64f.jpg)  
Fig. 14. Preview of a template structure.

ment, activity management and coordination, and context support. In the knowledge management perspective, VWSS enables accumulation of knowledge in an activity-driven way compared with folder-based approaches in many other systems. It also enables the reuse of past project structures in current projects as a skeleton of knowledge accumulation. From the activity management and coor-

![](/api/attachments/FWBYPPTU/fulltext/images/6883c041e40cb0a4db37c03de0a428df83416da15faac433b1873464edcfc199.jpg)  
Fig. 15. Answering a coordination message.

![](/api/attachments/FWBYPPTU/fulltext/images/6c862c60cde920d25d58a53f884e5cf3b39cac63a89f93c4e4303c446725d6d1.jpg)  
Fig. 16. Uploading a document to a milestone.

dination perspective, VWSS is advantageous over other systems in that it supports the natural alignment of management and coordination of activities with knowledge creation. From the context support perspective, the table shows that VWSS enables context-based searches and rich navigation paths for knowledge items, while other systems are deficient in providing the knowledge context, resulting in potential isolation of knowledge.

There are clear implications of KC-V and VWSS for e-business, because the distributed collaboration of virtual teams is becoming essential for global companies [38,40,44]. This is especially true for non-routine and knowledge-intensive work, such as distributed new product development (NPD) or R&D [14,19,24,42,43,51]. For example, May and Carter [42] presented a case study of a European automotive industry where the importance of virtual collaboration among engineers distributed along an automotive supply chain is emphasized [43]. Since the knowledge context can be easily lost and harder to manage in virtual collaboration, the approach of this paper for the use of knowledge context is meaningful in such e-business environments.

![](/api/attachments/FWBYPPTU/fulltext/images/cfe4abb9388a162297b0b4d8f4346e38bb4812f90b927167057fb0744a5fc356.jpg)  
Fig. 17. Searching with context similarity.

T<sub>a</sub>bl<sub>e</sub> 3 C<sub>ompar</sub>i<sub>son</sub> <sub>w</sub>ith <sub>o</sub>th<sub>er</sub> <sub>sys</sub>t<sub>ems</sub>

<table><tr><td rowspan="3" colspan="2">Dimensions</td><td colspan="10">Systems</td></tr><tr><td colspan="4">Collaboration Support System</td><td colspan="2">Commercial Workgroup Environment</td><td>Context Aware</td><td colspan="2">Work Environment</td><td>VWSS</td></tr><tr><td>BSCW [5,6,10]</td><td>eRoom [4,5,26,29]</td><td>QuickPlace [5,29,49]</td><td>TeamSCOPE [32]</td><td>Microsoft Outlook [45]</td><td>Lotus Notes [39]</td><td>TOSCA &amp; GroupDesk [3]</td><td>Virtual Office [1,2,25,41]</td><td>Watson [11]</td><td></td></tr><tr><td rowspan="4">Knowledge management</td><td>Knowledge accumulation structure</td><td>Folder-driven</td><td>Folder-driven</td><td>Folder-driven</td><td>Folder-driven</td><td>Folder-driven</td><td>Folder-driven</td><td>Folder-driven (GroupDesk)</td><td>Workflow-driven</td><td>-</td><td>Context-driven</td></tr><tr><td>Keyword search</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>-</td><td>-</td><td>-</td><td>○</td></tr><tr><td>Knowledge annotation and history management</td><td>○</td><td>○</td><td>-</td><td>○</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>○</td></tr><tr><td>Utilizing past team and project structure</td><td>-</td><td>Predefined template</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>Reuse of past project and team structure</td></tr><tr><td rowspan="4">Activity management and coordination</td><td>Activity monitoring</td><td>Gantt Chart and Milestones</td><td>Progress tracker, and milestones</td><td>Task status, due date and milestones</td><td>Activity status and summary</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>Activity progress, due date, and milestones</td></tr><tr><td>To-do list</td><td>-</td><td>○ Generated by system</td><td>○ Generated by system</td><td>-</td><td>○ Written by user</td><td>○ Written by user</td><td>-</td><td>-</td><td>-</td><td>○ Generated by system</td></tr><tr><td>Team Schedule</td><td>○</td><td>○</td><td>○</td><td>○ (Availability of other members)</td><td>○</td><td>○</td><td>-</td><td>-</td><td>-</td><td>○ (Milestone, team calendar)</td></tr><tr><td>Coordination of activities</td><td>Structured Message</td><td>-</td><td>-</td><td>-</td><td>-</td><td>Simple task assigning message</td><td>-</td><td>-</td><td>-</td><td>Structured message</td></tr><tr><td rowspan="3">Context support</td><td>Explicit context model</td><td>-</td><td>-</td><td>-</td><td>Team member awareness</td><td>-</td><td>-</td><td>Organizational context</td><td>Workflow context</td><td>Task context</td><td>Knowledge context (KC-V)</td></tr><tr><td>Context-based knowledge searching</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>Organization context</td><td>Workflow context</td><td>Task model and content model</td><td>Knowledge context (KC-V)</td></tr><tr><td>Navigation based on context</td><td>User, folder, date, and MIME type</td><td>User, folder and date</td><td>User, folder and date</td><td>User, folder and date</td><td>User, folder and date</td><td>User, folder and date</td><td>-</td><td>-</td><td>-</td><td>Knowledge context (KC-V)</td></tr></table>

Limitations and further research issues remain. First, the search function for finding projects and activities with similar context is determined by only domain values and attributes of activities and projects. Further research on developing more effective search methods by context similarity is required, such as applying the Case-Based Reasoning (CBR) technique [18,55]. Second, empirical evaluation of KC-V and VWSS is needed to validate further the practical usefulness of the approach.

## 5.2. Conclusion

In this paper, a model of knowledge context, KC-V, was suggested as a tool for facilitating the accumulation and utilization of knowledge in virtual collaborative work. KC-V was designed based on existing context models and requirements from the characteristics of virtual collaborative work. Four benefits of utilizing knowledge context were identified: (1) evolutionary accumulation of knowledge in natural alignment with collaborative activities, (2) supporting the virtual team lifecycle, (3) improved understanding by rich navigation paths, and (4) searching for knowledge with similar contexts. In order to realize the benefits of KC-V, a web-based collaboration system called VWSS was developed based on a virtual workspace model that extends KC-V.

VWSS has been successfully used for virtual projects and classroom collaboration at a university. Although further research issues remain for refinement, it is expected that the approach of KC-V and VWSS can be beneficial for virtual collaboration in ebusiness environments with non-routine and knowledge-intensive work.

## Acknowledgements

The authors acknowledge the help from Jeesun Kim, an alumna of KAIST, who participated in the development of VWSS. We also acknowledge the constructive comments from anonymous reviewers that helped us greatly to restructure and improve this paper.

## References

[1] A. Abecker, A. Bernardi, K. Hinkelmann, O. Ku¨hn, M. Sintek, Context-aware, proactive delivery of task-specific information: the knowmore project, Information Systems Frontiers 2 (3/4) (2000) 253– 276.

[2] A. Abecker, A. Bernardi, H. Maus, M. Sintek, C. Wenzel, Information supply for business processes: coupling workflow with document analysis and information retrieval, Knowledge-Based Systems 13 (2000) 271– 284.

[3] A. Agostini, G. De Michelis, M.A. Grasso, W. Prinz, A. Syri, Contexts, work processes and workspaces, Proceedings of the International Workshop on the Design of Cooperative Systems (COOP’95), INRIA, Antibes, France, 1995, pp. 219 – 238.

[4] G. Alwang, Easy enterprise collaboration, PC Magazine 21 (9) Available at: http://www.pcmag.com/article2/ 0,4149,14052,00.asp, 2002.

[5] G. Bafoutsou, G. Mentzas, Review and functional classification of collaborative systems, International Journal of Information Management 22 (4) (2002) 281– 305.

[6] R. Bentley, W. Appelt, U. Busbach, E. Hinrichs, D. Kerr, K. Sikkel, J. Trevor, G. Woetzel, Basic support for cooperative work on the world wide web, International Journal of Human Computer Studies 46 (1997) 827–846.

[7] R. Biuk-Aghai, I.T. Hawryszkiewycz, Analysis of virtual workspaces, Proceedings of International Symposium on Database Application in Non-Traditional Environments (DANTE’99), IEEE Computer Society Press, New York, 1999, pp. 325 – 332.

[8] F. Bomarius, K.D. Althoff, W. Muller, Knowledge management for learning software organizations, Software Process Improvement and Practice 4 (2) (1998) 89 – 93.

[9] P. Brezillion, J. Pomerol, Contextual knowledge sharing and cooperation in intelligent assistant systems, Le Travail Humain 62 (3) (1999) 223 – 246.

[10] BSCW, http://bscw.gmd.de/, 2003.

[11] J. Budzik, K. Hammond, Watson: anticipating and contextualizing information needs, Proceedings of the Sixty-Second Annual Meeting of the American Society for Information Science, 1999.

[12] G. Bux, G. Marzano, Library of predefined software process models as support for software factory design: the SFINX proposal, Proceedings of the Fifth International Workshop on Computer Aided Software Engineering, Montreal, Canada, IEEE Computer Society Press, New York, 1995, pp. 176–178.

[13] CAP Ventures, The role of shared context in a knowledgeenabled environment, White paper, http://www.capv.com/bin/ pdf/divine.pdf, 2002.

[14] C.U. Ciborra, G. Patriotta, Groupware and teamwork in R&D: limits to learning and innovation, R & D Management 28 (1) (1998) 43– 52.

[15] J.H. Cook, XML sets stage for efficient knowledge management, IT Professionals 2 (3) (2000 May – June) 55 – 57.

[16] T.H. Davenport, L. Prusak, Working Knowledge: How Organizations Manage What They Know, Harvard Business School Press, Boston, 1998.

[17] G. De Michelis, M.A. Grasso, Situating conversations within the language/action perspective: the Milan Conversation Model, Proceedings of the 5th Conference on Computer Supported Cooperative Work (CSCW’94) ACM, New York, 1994, pp. 89 – 100.

[18] P. Deng, Using case-based reasoning approach to the support of ill-structured decisions, European Journal of Operational Research 93 (1996) 511 –521.

[19] R.M. Dennis, P. Flavin, G.J. Davies, Online R&D management: the way forward, R & D Management 28 (1) (1998) 27– 35.

[20] G. DeSanctis, P. Monge, Introduction to the special issue: communication process for virtual organizations, Organization Science 10 (6) (1999) 693–703.

[21] R. Dieng, Methods and tools for corporate knowledge management, Proceedings of KAW’98, Banff, Canada, 1998.

[22] J. Dietz, Business modeling for business redesign, Proceedings of the 27th Hawaii International Conference on System Sciences, IEEE Computer Society Press, New York, 1994, pp. 723– 732.

[23] M. Dzbor, J. Paralic, M. Paralic, Knowledge management in a distributed organisation, in: L.M. Camarinha-Matos, H. Afsarmanesh, H.H. Erbe (Eds.), Advances in Networked Enterprises, Virtual organizations, Balanced Automation, and System Integration, Kluwer Academic Publishing, Dordrecht, Holland, 2000, pp. 339 – 348.

[24] E. Eloranta, A. Hameri, M. Lahti, Improved project management through improved document management, Computers in Industry 45 (2001) 231 – 243.

[25] L. Elst, A. Abecker, H. Maus, Exploiting user and process context for knowledge management systems, Proceedings of Workshop on User Modeling for Context-Aware Applications, UM’01, 2001.

[26] eRoom, http://www.eroom.com/, 2003.

[27] D. Fensel, Ontologies: A Silver Bullet for Knowledge Management and Electronic Commerce, Springer Verlag, New York, 2001.

[28] G. Fischer, Y. Ye, Exploiting context to make delivered information relevant to tasks and users, Proceedings of the Workshop on User Modeling for Context-Aware Applications, UM’01, 2001.

[29] S. Gillmor, J. Angus, Teamware comes of age, Information-Week, (1999 September 20) 69–78.

[30] G. Goldkuhl, E. Braf, Contextual knowledge analysis—understanding knowledge and its relations to action and communication, Proceedings of 2nd European Conference on

Knowledge Management, IEDC-Bled School of Management, Slovenia, 2001.

[31] J. Gundry, G. Metes, Team knowledge management: a computer-mediated approach, Available at: http://www.knowab. co.uk/wbwteam.html, 1996.

[32] C. Jang, C. Steinfield, B. Pfaff, Virtual team awareness and groupware support: an evaluation of the TeamSCOPE system, International Journal of Human-Computer Studies 56 (2002) 109 – 126.

[33] M.A. Janson, C.C. Woo, Comparing IS development tools and methods: using the speech act theory, Information and Management 28 (1995) 1 – 12.

[34] S.L. Jarvenpaa, D.E. Leidner, Communication and trust in global virtual teams, Organization Science 10 (6) (1999) 791 – 815.

[35] R. Klemke, Context framework—an open approach to enhance organisational memory systems with context modelling techniques, Proceedings of PAKM2000: Third International Conference on Practical Aspects of Knowledge Management, Basel, Switzerland, 2000.

[36] K.R.T. Larsen, C.R. McInerney, Preparing to work in the virtual organization, Information and Management 39 (2002) 445 – 456.

[37] S. Liao, Knowledge management technologies and applications: literature review from 1995 to 2002, Expert Systems with Applications 25 (2) (2003) 155– 164.

[38] J. Lipnack, J. Stamps, Virtual Teams: Reaching Across Space, Time and Organizations with Technology, Wiley, New York, 1997.

[39] Lotus Notes, http://www.lotus.com/notes, 2003.

[40] J.S. Lurey, M.S. Raisinghani, An empirical study of best practices in virtual teams, Information and Management 38 (2001) 523– 544.

[41] H. Maus, Workflow context as a means for intelligent information support, in: V. Akman, et al. (Eds.), CONTEXT 2001, LNAI, vol. 2116, 2001, pp. 261 – 274.

[42] A. May, C. Carter, A case study of virtual team working in the European automotive industry, International Journal of Industrial Ergonomics 27 (2001) 171– 186.

[43] A. May, C. Carter, S. Joyner, Virtual team working in the European automotive industry: user requirements and a case study approach, Human Factors and Ergonomics in Manufacturing 10 (3) (2000) 273 – 289.

[44] M.L. Maznevski, K.M. Chudoba, Bridging space over time: global virtual team dynamics and effectiveness, Organization Science 11 (5) (2000) 473– 492.

[45] Microsoft Outlook, http://www.microsoft.com/office/outlook/, 2003.

[46] V.O. Mittal, C.L. Paris, Generating explanations in context: the system perspective, Expert Systems With Applications 8 (4) (1995) 491– 503.

[47] I. Nonaka, H. Takeuchi, The Knowledge-Creating Company: How Japanese Companies Create the Dynamics of Innovation, Oxford Univ. Press, New York, 1995.

[48] D. O’Leary, Enterprise knowledge management, Computer 31 (3) (1998) 54 – 61.

[49] QuickPlace, http://www.lotus.com/products/qplace.nsf/ homepage/first, 2003.

[50] B. Ramesh, K. Sengupta, Multimedia in a design rationale decision system, Decision Support Systems 15 (1995) 181 – 196.

[51] B. Ramesh, A. Tiwana, Supporting collaborative process knowledge management in new product development teams, Decision Support Systems 27 (1999) 213 – 235.

[52] J. Suchan, G. Hayzak, The communication characteristics of virtual teams: a case study, IEEE Transactions on Professional Communication 44 (3) (2001) 174 – 186.

[53] A.M. Townsend, A.R. Hendrickson, S.M. DeMarie, Meeting the virtual work imperative, Communications of the ACM 45 (1) (2002) 23 – 26.

[54] S. Voida, E.D. Mynatt, B. MacIntyre, G.M. Corso, Integrating virtual and physical context to support knowledge workers, IEEE Pervasive Computing 1 (3) (2002) 73 – 79.

[55] I. Watson, Applying Case-Based Reasoning: Techniques for Enterprise Systems, Morgan Kaufmann, San Francisco, 1997.

[56] T. Winograd, A language/action perspective on the design of cooperative work, Human-Computer Interaction 3 (1) (1987 – 1988) 3 – 30.

[57] S. Wong, R.M. Burton, Virtual teams: what are their characteristics, and impact on team performance? Computational and Mathematical Organization Theory 6 (2000) 339–360.

[58] E. Woods, M. Sheina, Knowledge Management: Building the Collaborative Enterprise, Ovum Report, Ovum Ltd, London, 1999.

[59] M.H. Zack, Managing codified knowledge, Sloan Management Review 40 (4) (1999 Summer) 45– 58.

![](/api/attachments/FWBYPPTU/fulltext/images/e503e7c52a2d9a694dad17b831821b03bffd07ea9105b337d1ea259ba5145931.jpg)

Hyung Jun Ahn is a PhD candidate in the Korea Advanced Institute of Science and Technology (KAIST) majoring in Information Systems. His research interest includes knowledge management systems, virtual collaboration, and multiagent systems for business problems. He is currently focusing on the collaboration problems in supply chain management. He has previously published articles in the International Journal of Software En-

gineering and Knowledge Engineering and the Expert Systems with Applications.

![](/api/attachments/FWBYPPTU/fulltext/images/3b4353fa86d005c6f59d4239bd78b2a6ac6e8650ddc99e1eec236852c98d2277.jpg)

Hong Joo Lee is currently a doctoral student in the Graduate School of Management at KAIST. His research interests include knowledge management, new product development, and Computer Supported Collaborative Work (CSCW). He is currently focusing on knowledge representation and reusing in Engineering Change Management and knowledge management in collaborative product development.

![](/api/attachments/FWBYPPTU/fulltext/images/ab445fbf20f611374cc09df84e429c12472768921d2949abf617fe598a89c700.jpg)

Kyehyun Cho is a director of Sayclub.- com, which provides virtual community services or Social Web services to more than 8.5 million people in South Korea through broadband networks. SayClub.- com is renowned for its various types of creative services that include virtual partying, sharing music, and online games. He received MS in Management Engineering from KAIST in 1994. His current research interest includes virtual commu-

nity and teams, virtual identities, knowledge context, and contextaware computing.

![](/api/attachments/FWBYPPTU/fulltext/images/a9a9a1ab0e1fab93af5ce315329952b8cc14d71b95e57dd32ca3cdd0b7dff02f.jpg)

Sung Joo Park is a Professor of Information Systems and Dean at the KAIST Graduate School of Management in Seoul, Korea. He holds a BS degree in Industrial Engineering from the Seoul National University, an MS in Industrial Engineering from the Korea Advanced Institute of Science, and PhD in Systems Science from the Michigan State University. He has been a senior researcher at the Software Development Center, KIST, and

a professor at the KAIST since 1980. His areas of research interests include intelligent information systems and the application of agent technology to management decision-making.
