---
otero_id: 24944
otero_key: "DWA5D3JJ"
title: "Project Memory: Information Management for Project Teams"
authors: "Mark Weiser; Joline Morrison"
year: "1998"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1998.11518189"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Project Memory: Information Management for Project Teams

Mark Weiser & Joline Morrison

To cite this article: Mark Weiser & Joline Morrison (1998) Project Memory: Information Management for Project Teams, Journal of Management Information Systems, 14:4, 149-166, DOI: 10.1080/07421222.1998.11518189

To link to this article: http://dx.doi.org/10.1080/07421222.1998.11518189

![](/api/attachments/DWA5D3JJ/fulltext/images/e1282d4198b0ade222539bd21821d9b5751bee51d576ae6b6bf69c46695e0931.jpg)

Published online: 08 Dec 2015.

![](/api/attachments/DWA5D3JJ/fulltext/images/26654d6e89d4572086e2dccbd3982e463619357ba8a36e46e4363c045b50d92b.jpg)

Submit your article to this journal ↗

![](/api/attachments/DWA5D3JJ/fulltext/images/b747ce355ca8a85d14236ae0ada8ec8adf57bb46fce67070b2cd7e083f08fc14.jpg)

Article views: 8

![](/api/attachments/DWA5D3JJ/fulltext/images/e0778db5fd6b130a99cf0a0792b9e8f8361c2ba9de654d05c31678e2e6d2d1ab.jpg)

View related articles ↗

![](/api/attachments/DWA5D3JJ/fulltext/images/d49192fd37f79fd4d69b84ca860fd12ad223c1297c79c9285b27bb1112423270.jpg)

Citing articles: 33 View citing articles ↗

# Project Memory: Information Management for Project Teams

MARK WEISER AND JOLINE MORRISON

MARK WEISER is an Assistant Professor of Management Information Systems at Oklahoma State University. He received his Ph.D. in MIS from the University of Iowa and a B.S. in MIS from Pennsylvania State University. His research interests include organizational memory systems and telecommunications. Dr. Weiser has developed and delivered multiple graduate courses in telecommunications management and the impact of technology on business.

JOLINE MORRISON is an Assistant Professor in the Management Information Systems department at the University of Wisconsin at Eau Claire. She received her Ph.D. in MIS from the University of Arizona in 1992. Her current research interests include group and organization collaboration systems and database and client/server systems. Dr. Morrison is active in promoting organizational memory as an information systems research area.

ABSTRACT: Modern organizations are successfully using project teams to address complex tasks. Yet these teams often use approaches for project data management that may not capture project processes, contexts, rationales, or artifacts in a way that enables new project members to familiarize themselves quickly with the project history. Project information is rarely captured, retained, or indexed so that people external to the project can retrieve and apply it to future tasks. To address the issue of capturing a comprehensive project history that can subsequently be retrieved and applied to current problems, a generalizable object-oriented data model is developed. It decomposes project information into five discrete classes: projects, users, events, meetings, and documents. Through inheritance and domain references, the model describes the people, temporal events (such as meetings or single agenda items within a meeting), and archival documents that are created within a project or support some aspect of the project. These project items can be retrieved based on either contextual information (such as the dates they were created or last revised, who created them, or the projects they pertain to) or user-supplied descriptive keywords. Hypertext-like links can also be created to associate related items. Based on this model, a prototype system, Project Memory, has been developed to validate the model structure and system requirements.

KEY WORDS AND PHRASES: knowledge management, organizational learning, organizational memory, team memory.

MODERN ORGANIZATIONS ARE SUCCESSFULLY USING PROJECT TEAMS to address today's complex business challenges. One drawback of the team approach is that its inherent combination of employee empowerment and information decentralization often results in organizational knowledge fragmentation and a loss of organizational learning [11]. Formal project documentation such as project reports, meeting minutes, and correspondence usually exists as disjointed documents stored in file folders. Informal items like electronic mail messages and personal notes are often not retained at all. Project contexts, $^{1}$ underlying idea progressions, and rationales behind key decisions are effectively lost as an organizational resource when project team members leave for new assignments and human memories fade.

Existing group support systems primarily support teams working in face-to-face environments on single tasks or collections of related tasks $[10]$ . These systems generally allow users to retrieve only limited classes of support documents and rarely capture context, rationale, or process information. Current project management software applications typically focus on document retrieval, workflow integration, and scheduling. Some systems capture limited project context information such as the people involved and the duration of the project but do not explicitly address elements such as how the project evolved or the rationale behind key decisions.

This research addresses the problem of capturing, retaining, indexing, and retrieving project contexts, processes, rationales, and artifacts by developing a generalizable data model and associated information system for: (1) capturing and retaining project context information such as goals, agendas, and players involved; (2) acquiring and retaining details about a project's processes, decision rationales, and ultimate results either transparently by gathering information during project activities, or explicitly through user inputs; (3) capturing and retaining all project source and output documents, as well as their revision histories; (4) enabling users to search and retrieve project information including documents, events, people, and related projects using a variety of search parameters; and (5) linking related projects and their attached data items together to create a delimited search space. Since team members are generally more concerned with completing current project tasks rather than archiving information that may or may not prove useful at a later time, all of this must be accomplished with a minimal amount of extra user effort and in a manner that motivates its use.

## Related Work

THE FOLLOWING PARAGRAPHS DESCRIBE CURRENT PROJECT MANAGEMENT system applications and “organizational memory” concepts and systems. The final section relates our research agenda to these areas.

## Project Management Systems

Current systems address project management primarily through scheduling/resource management, document management, and collaboration support. Project scheduling and resource management systems emphasize developing project task timetables and assigning and balancing resources such as equipment and personnel. Popular applications use models such as Gantt and PERT charts and enable managers to develop baseline schedules and evolving status reports, including costing information. In the past these products have not been integrated with other project applications; however, vendors are striving to develop database integration and data import/export features [10].

Document-oriented project data integration is usually accomplished by systems that create indexes to document files or store linked references to documents or document data. Documents may be stored either as graphic images or in their native application formats (e.g., word processor, spreadsheet). Users can index or link related documents or phrases and subsequently retrieve them using key words, link navigation, or text string searches $[3]$ .

Existing collaboration support systems have been categorized according to their primary goals $[7]$ . Group decision support systems (GDSS) provide communication support to help remove common communication barriers and reduce uncertainty and “noise” from group decision processes $[8]$ . Computer-supported cooperative work (CSCW) systems emphasize data sharing among participants for specific group tasks (e.g., $[7, 9]$ ). To our knowledge, no systems in either of these categories have focused on capturing project contexts, processes, rationales, or external artifacts, or providing a means for retaining and indexing project information for later retrieval.

Some innovative systems provide insight into some of these tasks, however. For example, NoteCards $[22, 23]$ is a hypertext-based idea-structuring system that records and documents group ideas and keeps a historical record of group activities. gIBIS $[6]$ is a hypertext-based tool designed to capture the rationale behind a design process in terms of decisions, rejected options, and tradeoff analysis. gIBIS stores all data in a relational DBMS; users may link and retrieve external data using embedded links to application and data files.

The Claremont GS Environment $[13, 19]$ supports both group collaboration and longitudinal data access at a meeting level, and allows users to access data generated and associated with previous meetings. It provides limited search and retrieval capabilities across projects. Chen et al. $[4]$ have developed a series of algorithms to automatically identify and index ideas from the output of a GDSS “electronic brainstorming” session to allow future users to retrieve meeting outputs through topic or key word searches.

Lotus Notes [18] is a popular development environment for creating applications to support workgroup document management and collaboration. Notes applications enable team members to share database data, documents, electronic mail messages, and ongoing online discussions using a distributed database that keeps copies of all data items at geographically distributed sites. The environment has recently been updated so that applications can be accessed using a World Wide Web browser. It should be noted that Notes applications require the development of an underlying data model or structure such as we are proposing.

## Organizational Memory

Researchers characterize organizational memory as a device for integrating organizational knowledge and providing information from the past that can potentially aid present activities $[20, 24]$ . A series of studies cited by Walsh and Ungson $[24]$ suggest that organizational memory may be stored and processed by: (1) individuals within the organization; (2) coalitions or upper echelons within the organization; or (3) the organization itself. We propose that “project memory” is a subset of organizational memory that incorporates the memory of coalitions (i.e., project teams), as well as the memories of the individuals involved. It attempts to capture, retain, and integrate “hard” project data (such as database records, documents, and standard operating procedures) with “soft” items (such as stories, recollections of critical incidents, and details about decision processes).

An example of an existing system with organizational and project memory characteristics is AI-STARS, an online integrated data system in use at Digital Equipment Corporation that integrates data types such as electronic mail messages, bulletin board postings, interdepartmental memos, product release statements, and service manuals using an object-oriented data model $[2]$ . Users can create specific fields to describe these objects (e.g., reviewer\_name, modification\_date). Along with query capabilities that use specific field values, users may also perform full-text searches. The system supports creation of “views,” or specific subsets of the database, both for security and to reduce the potential search space for a given subject area.

Answer Garden [1] is another relevant organizational memory system that has been used experimentally at information system help desks to enable users to find solutions by answering a series of multiple-choice questions. Users may go through a series of questions, effectively working through the nodes of a tree, until the desired answer is found. If an answer is not found, the user instructs the system to send the question to a knowledgeable expert. The expert receives the question through electronic mail and answers it by inserting the answer into the database. Thus, the organizational memory “grows” as users ask new questions.

## Summary

Current approaches to project and document management and collaboration-support satisfactorily address specific aspects of project information management and provide insight into methods for capturing project contexts, processes, rationales, and artifacts. Similarly, existing organizational memory systems suggest retention, indexing, and retrieval strategies that are applicable to ongoing project information. This research integrates knowledge from both of these areas to develop the semantic data model and prototype information system we now describe.

## Data Model Development

THE TEAM PROCESS LITERATURE WAS REVIEWED AND ARCHIVAL DATA from four ongoing project teams was analyzed [15, 25] in an attempt to identify and describe organizational processes in general enough terms to support a wide variety of environments and tasks. Information-affecting project processes were identified as items obtained (1) during group meetings, (2) through individual efforts on group projects between meetings, and (3) from external sources and other projects. Records of items in the first two categories are typically found in project records or file folders. Related data items from external sources and other projects are retained only if a project member recognizes them as relevant and explicitly has copies made and retained. References to the original sources, however, may be misplaced. Also, the reasons why the document was relevant to the project may be lost, thus undermining the ability later to understand the underlying processes or rationales.

From the three general categories of project processes identified in the previous paragraph, a set of logical components was developed. Figure 1 illustrates that a Current Process is based on Pending Events, Past Events, people (Users), and “Other” Support Items, which include any organizational artifacts (including information from other organizational information systems) that could have an impact on the current process. It is within this context that the current process proceeds. These relationships are critical to identifying truly similar activities in the future that might be affected by knowledge of the current process.

An Event is the culmination of a process. It may be a project team meeting, a major project milestone, or the record of a final decision. An Event is supported by other Items such as Users, To-Do Tasks, other Events, and Support Items. Support Items are objects such as text documents, spreadsheets, graphics, multimedia objects, and database and transaction system data that have an impact on a given process. Users are the individuals associated with a given process or related support item. To-Do Tasks are planned future events that must be carried out to complete a process.

Team process characteristics are well suited to an object model description. Projects represent groups of organizational resources and artifacts that are related and may be further specialized into subprojects; this suggest the presence of container objects, domain references, and inheritance. Thus, a Project container class groups ongoing team processes and their related components. Documents, users, and events are also represented as discrete object classes. The progression of ideas during the creation and revision of documents implies versioning, which is an important element within the object model.

The Team Process Semantic Data Model (figure 2) captures team process components using six object classes that exploit common features of the object model. All Items must have an associated Owner (i.e., creator), and can optionally have Abstracts, Rationales, and associated Key Words. Inheritance, shown by the heavier lines, flows from superclass to subclass (e.g., a Project instance has all of the attributes of the Item class plus the specialized attributes of the Project class). Attributes may be primitive (such as a string value used to record an Item's name) or may include domain references (shown by the thin arrows that imply an attribute of one class is one or more instances of another class). These relationships reflect the context in which class instances are created. For example, each Participant in an Event instance is also an instance of the User class. The Agenda of either an Event or Project is an Item, probably of the class Document. Project instances may be subprojects of other Project instances, and Documents may be revisions of other Documents. A Meeting is a specialized instance of the Event class, with additional attributes of End Time and Location.

![](/api/attachments/DWA5D3JJ/fulltext/images/901b4761fedc8dde3063e64a4a31dc64a7435289a3ad686dcc9ceb565f59c4d1.jpg)  
Figure 1. Components of a Project Process

An important feature of this model is the concept of versioning as described by Kim [17]. It enables users to track the progression of ideas and events over time and within a single document. Most file systems overwrite old versions of files unless revisions are explicitly renamed. Under the object-oriented philosophy, the new and old versions may share the same name, attribute values, and references, but maintain unique identities within the system. This is illustrated in the model whereby a Document instance may be a RevisionOf a parent document instance. Versioning is important in a system that claims to represent the “memory” of a project because an action may be based on ideas that are subsequently edited out of a document.

## Prototype Implementation

## System Requirements

Based on the proposed data model and an informal evaluation of a prototype interface by team project participants and facilitators [14], the following list of system requirements and features was developed:

1. Familiar application environments and transparent item creation. To motivate system use, users should be able to work in familiar application environments when creating documents, and documents should automatically be stored and maintained with no special user intervention.

![](/api/attachments/DWA5D3JJ/fulltext/images/1e32d19f194a2c6c4d853b0f844d9bc6916371064c4cfcedcfbc6439d52c0a05.jpg)  
Figure 2. Team Process Semantic Data Model

2. Standardized user-supplied key words. Whenever a user needs to supply keywords to a newly created document, a list of current system key words is provided to help minimize syntactic differences that may adversely affect subsequent queries.

3. Proprietary storage. To ensure data integrity, all user application data files are stored wholly within the database rather than in the user's file system.

4. Security classifications. To encourage users to submit work-in-progress and potentially sensitive information that they may not wish to release for public viewing, the current design provides security levels of personal, group, and all for all items. The need for finer-grained security in an implementation of an organization-wide system is recognized but not yet implemented.

5. Multiple but contained access paths. To enhance information retrieval relevance and precision for information seekers who potentially do not know exactly what they are looking for, each item may be retrieved based on a variety of search parameters. For example, a document may be retrieved by referencing its creator, the project in which it was created, another project that it supports, or through a search of creation/revision dates or relevant keywords. This allows a single item to be referenced in support of multiple other items to clarify its content and context.

6. Document granularity. The advantage of this approach is that it is less likely for an individual data "unit" to be retrieved and then interpreted out of context because of the contextual clues that exist in the document as a whole. The disadvantage is that subsequent users can determine whether an item is relevant to a current task only by reviewing its entire content.

![](/api/attachments/DWA5D3JJ/fulltext/images/8ffe87eef495c469041fab940285e5c37efde325a6548238eccdd6124e5f4371.jpg)  
Figure 3. Extended Relational Model

## Logical Database Structure

To provide the necessary implementation flexibility for planned evaluation studies, as well as the required characteristics of the proposed object data model, Microsoft Access was selected as the database development platform. It supports the binary data type required for storing document files and easily interfaces with a variety of other applications. Figure 3 shows the transformation of the object model into an extension of the entity relationship model using a variation of Chen's notation [5, 21], with the addition of dashed lines to imply the object-oriented notion of inheritance. Also, rather than using the characters 0, 1, M, and N, and O on connecting lines to represent relationship connectivities, all relationships are explicitly stated from the view of each entity. For example, each Item may be the result of from 0 to 1 Projects, but each Project instance results in between 0 and many Items. Attributes of the table fields are shown beside each corresponding entity and relationship, with primary key fields underlined.

Although the object model inherently supports versions of any class instance, this model shows only versioning of Documents through the unary relationship “is revision of.” The Document entity encompasses all traditional project documentation such as meeting minutes, reports, and financial spreadsheets, and also includes links or pointers to external documents that may be modified over time. This model effectively

![](/api/attachments/DWA5D3JJ/fulltext/images/94530b9fc7a25e361b55553c2c80d4bca651c87108c837e7c683b05bedbf1499.jpg)  
Figure 4. Elements within a Project Folder  
supports the notion of multiple versions created by different users through its link to the User entity.

## Interface Description

Project team members are presented file-folder icons representing their individual projects on the main system screen (figure 4). Double-clicking on a project folder displays the project's elements ("People," "Events," etc.). From this screen, users may create new projects and then specify an abstract, known agenda items, and relevant keywords (figure 5). Users also may designate access rights to the new project by specifying "Project," "Group," or "All." When a project is newly created, the team consists of only the project creator, who may then select new team members from the list of organizational members or add external members. Adding or removing team members is considered to be an event in the project's process, and is automatically captured as a project Event.

Users may also explicitly create events corresponding to important project occurrences such as deadlines or decisions. Event context and rationale information may be entered, and key words may be attached to assist in future searches either by picking from a list of previously entered key words for the project or by entering a new key word that is then added to the project key word list. Any system object (i.e., documents, users, projects, comments, or other events) may be attached to an event, thus creating a web of relationships and access points.

The Meeting creation and information screen is shown in figure 6. As previously indicated, a Meeting is a specialized type of Event with unique object properties. The information provided by the Events screen may be especially useful for bringing new project team members “up to speed” on the process and status of an ongoing project.

![](/api/attachments/DWA5D3JJ/fulltext/images/63b22948cc10b3daaf3b8bcf786659976ed54964b9f2731d68cd8f0aeee1853d.jpg)  
Figure 5. Project Creation

The other project elements represented by icons in figure 4 can be manipulated in similar ways. The “People” icon allows team members to review and/or edit information about project team members. “Documents” allows users to examine all project-related documents, as well as enter new documents. Users may create or import documents created in any Windows application; application files are automatically stored in their native binary formats within the database, thus satisfying our transparent item creation and proprietary storage requirements. “Status” provides managerial information about project progress and anticipated completion dates. “Meeting” shows event information (figure 6) for past or pending meetings. Users may also create text “Comments” about the project in general, or associated with any project item. All items may have associated key words for subsequent searches. The process of creating or changing any object is transparently recorded as a project Event.

An important feature of the system is its search facility. Project Memory users may specify the following search parameters: (1) the type(s) of items to be returned by the search; (2) the projects to search from; (3) people who created, or are otherwise related to, the search targets; (4) date ranges specifying when the item was created or last edited; and (5) item key words. This flexible search strategy satisfies our requirement for multiple search paths within a contained search space.

![](/api/attachments/DWA5D3JJ/fulltext/images/d1445a11b4a8f440d326c0eb96f1a897252cd60c0142fcd23be026c113237abf.jpg)  
Figure 6. Project Meeting Information

## System Evaluation

A FIELD STUDY WAS USED TO EVALUATE SYSTEM USABILITY and user motivation while gathering project information within a live team project. A laboratory study served to evaluate the effectiveness of the system's retrieval functions for enabling new team members to become familiar with past project processes.

## Field Study

A project team of administrative managers and technical support staff members at a large public university who were investigating electronic transmissions of standard documents for university administration agreed to use the Project Memory system to record project information. Since the system and data model were changing throughout the study, our collected data were qualitative rather quantitative; data collection methods included unstructured interviews, observed system use, examination of memory base contents, and analysis of usage statistics.

With our assistance, the team leader created the project and entered context data such as team member names and the project goal, description, and timetable. Initially, system use was limited: Team members did not see where the system added any value to their team process. To rectify this problem, the team leader (who was a strong supporter of the system) offered to use the system as the principal means of group communication. Since a primary communication item was meeting scheduling, we were prompted to create the Meeting subclass within the data model. As a result, team members had to interact with the system to receive notifications about meeting details.

This increased system use substantially.

Team members also suggested that another feature that would stimulate system use would be the ability to notify team members automatically by electronic mail when meetings were scheduled or new items were added to the project so they would not be forced to log into the system every day. Code added to the system for this purpose employed Simple Mail Transfer Protocol (SMTP) syntax and used an IBM RS6000 as a globally accessible SMTP server. Messages were sent to each user's preferred e-mail address (maintained as an attribute in the user data table). The object model (figure 2) shows this change through the addition of a “notify” method in the Meeting and Document classes. This feature was received very positively.

As the project proceeded, it appeared that explicit context and process items were primarily entered by the team leader, while team members used the system as a communications medium and document-sharing device. Attributes specifically praised by team members were the system's ability to access all project information from a single icon and its ability to associate a single document with several related projects. Transparently incorporating personal projects and other items into the system was also noted as especially useful because it allowed the system to be used for projects other than the specific group project. Trace data of system interaction showed that users had created two additional projects with memberships other than the original project team, and both contained project event and process information. Users also created documents within the Electronic Documents project that had “personal” rights, allowing only the items’ creators to view them. Multiple versions of several documents were also noted. Although the additional projects were not within the scope of the study, their unprompted establishment and the use of nondefault security classifications reflect the perceived value of these features.

A prime area of concern was the time required to load binary documents to remote locations, where delays could be two to five times the typical duration to load a document off a local server. Distributed and replicated storage methods are being investigated to improve system performance. Other areas for potential improvements included (1) adding a context-sensitive help system, (2) adding a menu system covering all system functions in addition to the icons, and (3) adding a simple mail utility to enable free-form writing of notes to be sent to any user within the system, rather than only incorporating the prefabricated notification messages now in use. Overall, the field study indicated that our system could successfully be used by team members for recording project context, process, and document information provided the team leader is motivated to enter process and context information.

## Laboratory Study

After making the modifications suggested by the field study, Project Memory was used in a controlled environment to determine if the system aided a search and retrieval task involving historical information. (A detailed description of this study is presented in [17]). An actual strategic planning project's documentation was used to populate the system. The experimental model, presented in figure 7 and based on CSCW-based experimental research, explores the impact of two different organizational memory (OM) technologies (paper-based archives and Project Memory) on the OM process and the user, OM, and task outcomes.

![](/api/attachments/DWA5D3JJ/fulltext/images/298da8429ee48542b0834472f4e7f89a1be55e8f1cad12f0b3526ecb8ffebfb7.jpg)  
Figure 7. Experimental Model

Our experimental subjects were twenty-four upper-level undergraduate business (primarily MIS and accounting) students. After being separated into randomly assigned treatment (Project Memory) and control (paper archive) groups, subjects were taken to separate sites and told they had been chosen to assume leadership of an ongoing project committee charged with creating a strategic plan for the university's business college. They were instructed to use their given OM system individually to answer a series of five questions ranging from details of historical events in the project to open-ended questions asking for recommendations for bringing the project to a smooth conclusion. Treatment-group members were given a brief training session in the use of the Project Memory system and then shown how to access the project's electronic file folder. Control subjects were given the paper documents, arranged chronologically in a series of labeled file folders. Following collection of the completed answer sets, a post-test questionnaire (provided in the appendix) was distributed to the participants to elicit overall outcome and process satisfaction as well perceived completeness, organization, and indexing quality of the documents and satisfaction with the amount of data available to answer the questions.

Table 1 presents means and standard deviations for all independent variables for all subjects as well as results sorted by treatment groups. Multiple regression analysis, summarized in Table 2, indicated that the Project Memory–supported subjects were superior at finding specific answers to the structured questions with distinctly “right” answers, while the paper-archive users appeared to perform better on the less-structured questions. The paper-based users found it easier to reorganize and synthesize the information because they could reorganize information visually and spatially by sorting paper documents into different piles.

Table 1. Means and Standard Deviations

<table><tr><td rowspan="2">Variable</td><td colspan="2">Overall (N = 24)</td><td colspan="2">OMIS (N = 13)</td><td colspan="2">Paper archives (N = 11)</td></tr><tr><td>Mean</td><td>S.D.</td><td>Mean</td><td>S.D.</td><td>Mean</td><td>S.D.</td></tr><tr><td>Age</td><td>21.38</td><td>1.93</td><td>21.46</td><td>2.40</td><td>21.27</td><td>1.27</td></tr><tr><td>Gender (1 = M; 2 = F)</td><td>1.25</td><td>0.44</td><td>1.23</td><td>0.44</td><td>1.27</td><td>0.47</td></tr><tr><td>Major (1 - MIS; 2 = other)</td><td>1.71</td><td>0.46</td><td>1.77</td><td>0.44</td><td>1.64</td><td>0.50</td></tr><tr><td>GPA</td><td>3.33</td><td>0.39</td><td>3.36</td><td>0.43</td><td>3.29</td><td>0.34</td></tr><tr><td>General computer experiencea</td><td>2.00</td><td>0.53</td><td>2.18</td><td>0.36</td><td>1.79</td><td>0.63</td></tr><tr><td>General computer attitudesb</td><td>2.26</td><td>0.61</td><td>2.19</td><td>0.61</td><td>2.33</td><td>0.63</td></tr><tr><td>Overall no. of documents retrieved</td><td>23.00</td><td>21.57</td><td>13.62</td><td>8.03</td><td>34.09</td><td>27.26</td></tr><tr><td>Overall no. of relevant documents retrieved</td><td>6.25</td><td>4.90</td><td>4.46</td><td>2.15</td><td>8.36</td><td>6.38</td></tr><tr><td>Overall precision</td><td>0.36</td><td>0.21</td><td>0.42</td><td>0.25</td><td>0.30</td><td>0.14</td></tr><tr><td>Overall recall</td><td>0.15</td><td>0.11</td><td>0.10</td><td>0.05</td><td>0.19</td><td>0.15</td></tr><tr><td>Overall answer qualityc</td><td>5.62</td><td>1.66</td><td>5.47</td><td>1.87</td><td>5.79</td><td>1.45</td></tr><tr><td>Overall process satisfactiond</td><td>2.79</td><td>0.72</td><td>3.08</td><td>0.76</td><td>2.45</td><td>0.52</td></tr><tr><td>Overall outcome satisfactiond</td><td>2.83</td><td>1.05</td><td>2.92</td><td>1.26</td><td>2.73</td><td>0.79</td></tr><tr><td>Overall time (max. = 75 min.)</td><td>69.04</td><td>7.82</td><td>71.77</td><td>6.41</td><td>65.82</td><td>8.39</td></tr><tr><td>Satisfaction with info. completenesse</td><td>3.67</td><td>0.98</td><td>3.29</td><td>0.76</td><td>4.00</td><td>1.07</td></tr><tr><td>Satisfaction with info. organizationf</td><td>2.73</td><td>1.10</td><td>3.14</td><td>0.90</td><td>2.38</td><td>1.19</td></tr><tr><td>Satisfaction with info. indexingg</td><td>2.93</td><td>1.28</td><td>3.19</td><td>1.25</td><td>2.63</td><td>1.30</td></tr><tr><td>Satisfaction with info. quantityh</td><td>4.86</td><td>2.07</td><td>3.86</td><td>1.77</td><td>5.86</td><td>1.95</td></tr></table>

$^{a}$ 0 = none; 6 = very high. $^{b}$ 1 = very negative; 6 = very positive. $^{c}$ 1 = poorest answer group; 6 = best answer group (see text); $^{d}$ 1 = very unsatisfied; 6 = very satisfied. $^{e}$ 1 = very incomplete; 6 = very complete. $^{f}$ 1 = very poorly organized; 6 = very well organized. $^{g}$ 1 = very poorly indexed; 6 = very well indexed. $^{h}$ 1 = not enough; 4 = just right; 7 = too much.

The Project Memory users were consistently more satisfied with all aspects of the task process. The experimental memory base contained only thirty documents, which was a small fraction of the actual project archives. Still, most of the paper subjects were frustrated with the process and felt that too much information was provided. The system and underlying data model, however, provided a viable means for locating and retrieving project-based information in a delimited search space, with the caveat that, once relevant information is located, users will probably print out hard copies for subsequent analysis and synthesis.

Table 2. Summary of Multiple Regression Results (All Variables)

<table><tr><td rowspan="2">Variables</td><td colspan="12">Regression coefficients</td></tr><tr><td>Time</td><td>No. docs. retr.</td><td>No. relevant docs. retr.</td><td>Over-all pre-cision</td><td>Over-all re-call</td><td>Overall answer qual.</td><td>Proc. satis.</td><td>Outcome satis.</td><td>Satis. with info. completeness</td><td>Satis. with info.org.</td><td>Satis. with indexing</td><td>Satis. with quantity</td></tr><tr><td>Age</td><td>1.23</td><td>-2.52</td><td>-0.46</td><td>0.01*</td><td>-0.01</td><td>-0.08</td><td>0.21</td><td>-0.01</td><td>0.09</td><td>0.29**</td><td>-0.28</td><td></td></tr><tr><td>Gender</td><td>5.22</td><td>-14.28</td><td>-3.91</td><td>0.04</td><td>-0.09</td><td>0.76</td><td>0.66</td><td>0.57</td><td>0.43</td><td>-0.34</td><td>0.35</td><td>0.59</td></tr><tr><td>Major</td><td>2.44</td><td>-22.02</td><td>-2.33</td><td>0.03</td><td>-0.05</td><td>-0.39</td><td>0.60</td><td>0.24</td><td>-1.41</td><td>0.36</td><td>-0.35</td><td>-9.18**</td></tr><tr><td>GPA</td><td>-10.81**</td><td>17.40</td><td>3.10</td><td>-0.02</td><td>0.07</td><td>1.16</td><td>-0.58</td><td>-0.37</td><td>-0.32</td><td>-1.55*</td><td>-1.23</td><td>1.05</td></tr><tr><td>Group</td><td>2.54</td><td>-8.83</td><td>-1.95</td><td>0.25***</td><td>-0.05</td><td>0.10</td><td>0.40</td><td>0.30</td><td>0.23</td><td>1.53**</td><td>1.24**</td><td>2.42</td></tr><tr><td>Gen. comp. exp.</td><td>13.97***</td><td>35.26**</td><td>-7.74*</td><td>0.01</td><td>-0.18*</td><td>-1.22</td><td>0.48</td><td>-0.52</td><td>-2.66*</td><td>-2.20**</td><td>-2.48**</td><td>-7.60**</td></tr><tr><td>Gen. comp. att.</td><td>5.14</td><td>1.08</td><td>-3.31</td><td>0.00</td><td>-0.08</td><td>-0.11</td><td>-0.22</td><td>0.07</td><td>-1.66*</td><td>-1.59**</td><td>-2.23***</td><td>-2.64</td></tr><tr><td> $R^2$ </td><td>0.55*</td><td>0.48</td><td>0.36</td><td>0.96***</td><td>0.36</td><td>0.25</td><td>0.35</td><td>0.25</td><td>0.62</td><td>0.85**</td><td>0.90**</td><td>0.79</td></tr></table>

$*p \leq 0.1; **p \leq 0.05; ***p \leq 0.01; ****p \leq 0.001$ .

## Discussion

THE FIELD STUDY SUGGESTED THAT THE PROPOSED DATA MODEL and Project Memory system are useful to team members actively working on a project primarily because they provide a central repository and access point for project communications and documents. The communication aspect proved to be critical; without a reason to use the system actively, team members saw no added value over their present approaches to project data management. It is likely that if team members used the system over time, it would become increasingly mission-critical, and users would ultimately recognize the value of being able to retrieve both their own and others' project information.

Little process or rationale information was captured other than the information explicitly entered by the project team leader or gained as trace data from team member operations such as viewing or changing documents. One strategy to overcome this problem would be for managers to require team members to enter such information as a project deliverable. Context information such as ownership and other data is already captured within the data model.

The laboratory experiment illustrated that the system supported structured search and retrieval operations very well, and with a much higher satisfaction level than use of paper-based archives. The system did not support the unstructured tasks as well. This may have been because it is easier to keep a sense of context with piles of paper, or it may have been because the experimental subjects were more familiar with the paper-based approach; with additional system experience, the computer system users may have performed equally well. We feel that these differences would be even more pronounced within a larger, more realistic project memory base.

A limitation of this research to date has been the absence of a longitudinal evaluation where working project team members insert and index project information that is subsequently retrieved and used by the same team members or other users. Such a study is necessary to ascertain whether the data model and prototype system can successfully capture and retain “soft” knowledge components such as imprecise project processes or decision rationales, and whether the system can successfully scale up to meet the potentially massive data retention requirements of a large team working on a complex project.

## Conclusions and Future Research Directions

THIS STUDY DESCRIBES DEVELOPMENT OF AN OBJECT-ORIENTED DATA MODEL and prototype system to support ongoing project teams. The evolving model and prototype system have been enhanced by knowledge gained through a field study with a working project team that highlighted motivational and technical considerations and confirmed the utility of the design in terms of providing a support environment that could be used to capture and retain project context, process, and document information. The laboratory experiment provided insight into indexing and retrieving project information within the system, and confirmed that the Project Memory environment was preferable to the associated paper document archives in terms of usability for a series of search and retrieval tasks.

Along with performing these types of longitudinal studies, future research also needs to investigate ways to enable geographically dispersed team members to collaborate successfully using the system. Major issues having an impact on such research involve ways to use the World Wide Web for information distribution while maintaining the ease of use proven in Project Memory's current graphical, icon-based format. Partial replication and distribution of the database at remote sites is being investigated to minimize the delays inherent in transfer of large binary files using common file transfer protocols.

All of these investigations will have an impact on the model structure and are being carefully evaluated in terms of the success of the current system features and other research in this area. Overall, this approach shows great promise for enhancing how teams retain project information.

## NOTE

1. For the purposes of this research, we define “context” as those items addressing the questions who, what, where, when, and why. “Process” considers how.

## REFERENCES

1. Ackerman, M.S. and Malone, T.W. Answer garden: a tool for growing organizational memory. Proceedings of the ACM Conference on Office Information Systems, Cambridge, MA, April 25–27, 1990, pp. 31–39.

2. Anick, P.G.; Flynn, R.A.; and Hanssen, D.R. Addressing the requirements of a dynamic corporate textual information base. SIGIR '91 (Proceedings of the 1991 ACM/SIGIR Conference on Research and Development in Info. Retrieval), pp. 163–172.

3. Berline, G., and Grunin, L. Document management: the painful transition. PC Magazine, 12, 12 (June 29, 1993), 171–216.

4. Chen, H.; Hsu, P.; Orwig, R.; Hoopes, L.; and Nunamaker, J. Automatic concept classification of text from electronic meetings. Communications of the ACM, 37, 10 (October 1994), 56–73.

5. Chen, P. The entity relationship model—toward a unified view of data. ACM Transactions on Database Systems, 1 (March 1976), 9–36.

6. Conklin, J., and Begeman, M.L. gIBIS: a hypertext tool for exploratory policy discussion. ACM Transactions on Office Information Systems 6, 4 (October 1988), 303–331.

7. Dennis, A.R.; George, J.F.; Jessup, L.M.; Nunamaker, J.F., Jr.; and Vogel, D.R. Information technology to support electronic meetings. MIS Quarterly, 12, 4 (December 1988), 591–624.

8. DeSanctis, G., and Gallupe, R.B. A foundation for the study of group decision support systems. Management Science, 33, 5 (May 1987), 589–609.

9. Greif, I., and Sarin, S. Data sharing in group work. ACM Transactions on Office Information Systems, 5, 2 (April 1987), 187–211.

10. Higgs, S. Reviews: project management for windows. BYTE (April 1995) (CD-ROM).

11. Jarvenpaa, S.L., and Ives, B. The global network organization of the future: information management opportunities and challenges. Journal of Management Information Systems, 10, 4 (Spring 1994), 25.-57.

12. Kim, Won. Introduction to Object-Oriented Databases. Cambridge, MA: MIT Press, 1990.

13. Mandviwalla, M.; Gray, P.; Olfman, L.; and Satzinger, J. The Claremont GDSS support environment. Proceedings of the Twenty-Fourth Annual Hawaii International Conference on System Sciences, vol. 3, Kauai, January 1991, pp. 600–607.

14. Morrison, J. Development and evaluation of a system to support group and organizational memory. Ph.D dissertation, University of Arizona, 1992.

15. Morrison, J. Team memory: information management for business teams. Proceedings of the Twenty-Sixth Annual Hawaii International Conference on System Sciences, vol. 4, January 1993, pp. 122–131.

16. Morrison, J. Organizational memory information systems: characteristics and development strategies. Proceedings of the Thirtieth Annual Hawaii International Conference on System Sciences, vol. 3, January 1997.

17. Morrison, J., and Weiser M. A research framework for empirical studies in organizational memory. Proceedings of the Twenty-Ninth Annual Hawaii International Conference on System Sciences, vol. 3, January 1996, pp. 178–187.

18. NotesOnWeb http://www.lotus.com/ntsdoc96 Notes. Web site accessed August 2, 1996.

19. Sandoe, K.; Olfman, L.; and Mandviwalla, M. Meeting in time: recording the workgroup conversation. Proceedings of the 12th International Conference on Information Systems, December 1991, pp. 261–271.

20. Stein, E.W., and Zwass, V. Actualizing organizational memory with information systems. Information Systems Research, 6, 2 (June 1995), 85–117.

21. Teorey, T.J.; Yang, D.; and Fry, J.P. A logical design methodology using the extended entity-relationship model. Computing Surveys, 18 (June 1986), 197–222.

22. Trigg, R.H. Guided tours and tabletops: tools for communicating in a hypertext environment. ACM Trans. on Office Information Systems, 6, 4 (October 1988), 398–414.

23. Trigg, R.H.; Suchman, L.A.; and Halasz, F.G. Supporting collaboration in NoteCards. Proceedings of the 1986 Conference on Computer-Supported Collaborative Work, Austin, December 1986, pp. 153–162.

24. Walsh, J.P., and Ungson, G.R. Organizational memory. Academy of Management Review, 16, 1 (January 1991), 57–91.

25. Weiser, M. Development of an object model and system implementation to explore the organizational memory requirements of project teams. Ph.D thesis, University of Iowa, 1995.

## APPENDIX: Postexperiment Questionnaire

1. Overall, how complete waste information that you were given to answer the questions? (1 = very incomplete, 6 = very complete)

2. Overall, how well organized was the information that you were given to answer the questions? (1 = very poorly organized, 6 = very well organized)

3. Overall, how well indexed was the information that you were given to answer the questions? (1 = very poorly indexed, 6 = very well indexed)

4. Overall, the amount of information available to answer the questions was: (1 = not enough, 4 = just right, 7 = too much)

5. Overall, how satisfied were you with the process of searching the project materials to find the required information? (1 = very unsatisfied, 6 = very satisfied)

6. Overall, how satisfied are you with your responses to the given questions? (1 = very unsatisfied, 6 = very satisfied)
