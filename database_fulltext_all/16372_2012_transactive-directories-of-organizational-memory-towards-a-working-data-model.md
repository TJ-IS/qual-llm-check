---
otero_id: 16372
otero_key: "6TBHRFAM"
title: "Transactive directories of organizational memory: Towards a working data model"
authors: "Paul Jackson"
year: "2012"
journal: "Information & Management"
doi: "10.1016/j.im.2012.01.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Transactive directories of organizational memory: Towards a working data model

Paul Jackson

School of Management, Edith Cowan University, 100 Joondalup Drive, Joondalup 6026, Western Australia, Australia

A R T I C L E I N F O

Article history: Received 4 February 2007 Received in revised form 9 November 2011 Accepted 31 December 2011 Available online 1 February 2012

Keywords: Transactive memory systems Organizational memory Organizational learning Knowledge mapping Knowledge sharing

## A B S T R A C T

Transactive memory system is a term from group psychology that describes a system that helps small groups maintain and use personal directories to allocate and retrieve knowledge. Such systems have been observed at the level of whole organizations, suggesting that they provide a means for conceptualizing the exploitation of organizational memory. In this paper, I describe a longitudinal investigation of a global engineering consulting firm in which I used inductive analysis of interview data to map and then develop a conceptual entity-relationship model of organizational memory. This model formed the basis for a transactive directory to facilitate knowledge retrieval and allocation in the firm. - 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

What organizations know and apply to routine tasks, problem solving, and decision making has been described as their organizational memory (OM) or knowledge [16]. It exists in a variety of forms and repositories, such as: documents, databases, employees’ brains, and group rituals. However, the persistent challenge of using the OM effectively is one of enhancing the scope and availability of the stocks of knowledge within the organization [9]. In my study, I used case study data to identify descriptive entities, relationships, and attributes that employees generally use in order to populate their personal directories for their subsequent information storage and retrieval. I then compared this to an existing transactive model of organizational memory and extended it to accommodate the new metadata.

My exploratory, longitudinal study was conducted within a single organization, allowing OM and the associated transactive systems to be explored in depth over the life of several business projects. My research built on the entity-relationship (ER) model and attempted to develop the basis for the design of a practicable IS to manage OM metadata. The resulting ER model can then be used as a general schema for designing and building organizational transactive directories that might be maintained manually by personnel (e.g., using workflow software to record knowledge required or acquired), by implicit software functions embedded in software (e.g., linked tags and author information recorded in

Wikis), or through automated machine intelligence programs ‘‘crawling’’ through documents and filling the database. The resulting data model should be able to answer the descriptive (retrieval) and normative (allocative) questions demanded of a transactive memory directory, such as:

\- Where is the knowledge needed to perform this process?

\- Who is responsible for this knowledge?

\- What knowledge does this activity produce?

\- Who needs to be informed of this new knowledge? and

\- Where should we save this new knowledge?

## 2. Organizational memory

## 2.1. Background

Knowledge resides in memory traces in individuals; it is what they know. We can state what we know, transcribe it, put it in databases, but we always know more than we can tell. Organizations are social groups who absorb and develop systems of knowledge to serve their purposes. Organizations can be seen as information processing systems within which collective interpretations of the knowledge exist and from which it emerges. Thus organizations have a particular memory: the knowledge of how to do things, how to approach problems and issues, and how to deal with one another [1].

The instrumental view of organizational memory is that it is knowledge which is useful in successfully accomplishing present activities; it might result in higher or lower levels of organizational effectiveness. Although the aim of organizational memory is clearly to refine and improve performance through the adoption of superior routines, some memories may inhibit higher performance (e.g., the ‘‘not invented here’’ syndrome). The sense-making view of organizational memory is that it involves knowledge that gives structure and meaning to events and allows shared interpretation to develop in the organization. OM is therefore also the set of mental models available to the organization; they determine cognitive, regulative, and normative judgments about the world.

There are organizational, social and personal routines that store knowledge in and retrieve it from this memory. This is one critical, function of organizational learning – being able to draw upon the experience of others in the organization. The processes which contribute to it involve acquisition, retention, search and retrieval (e.g., [6]). Several business activities have organizational learning as a by-product; learning on the job, learning how to work effectively in a team, or discussions in post-project review [3]. Such learning processes can be facilitated by giving personnel capabilities (technology, training, time, and space) and motivation (recognition, self-fulfilment, rewards) to contribute knowledge to the organization as a whole [14].

OM is stored in several places and the knowledge is intended to help the firm improve its competitiveness and effectiveness [18]. Typically memories include individual’s brains, IT storage devices, managerial know-how, rules and policies, workplace ecology and roles and structures. Positive correlations have been found between strong OM in these categories and organizational performance, organizational learning, improvisation and speed of decision making. OM can improve productivity by improving routine work, developing better control over production, logistics and service delivery, and identifying the best skills for a job.

Nonetheless, a major challenge facing the development of systems to support OM is the modelling of its memory. A system that unifies the organizational knowledge can be used to gain insight into how information might best be stored in the organization’s memory, thereby opening the possibility for systematic and deliberate improvement. The goal of a transactive memory system (TMS) approach is to create a unified OM: a directory structure which provides a unified mental model of the firm and which matches the information needs of business with its appropriate content to improve performance. In this research I wished to continue to develop a sound way to model an organization’s memory in its diverse forms and manifestations.

A TMS contains the processes used to maintain and use the knowledge of groups. When knowledge is sent to a group it is allocated to a responsible member. In the process, it is encoded by the group members into their personal directory structure to tell them that this person has charge of that piece of knowledge, and they can retrieve it from the expert when they need it, using their own directories, possibly in combination with other people’s directories or external aids, such as diaries. The concept of TMS has thus been extended to describe knowledge storage and retrieval in organizations. Thus organizations can be seen as collections of personal and technological directories which, when current and accurate, provide access to OM when and where it is required.

There are four classes of meta-knowledge about the entities: conceptual (their meanings), descriptive (the general attributes), cognitive (the meta-memory of capabilities), and persuasive (the nature of the retainer). The schema accommodates the instrumental and the sense-making view of the OM, so that practical, cultural, and explanatory knowledge can be stated in the predicate entity, whilst the conceptual entity contains the underlying mental models that exist in the organizational reality of invoices, orders and schedules, punctuality, or quality.

It was the schema that I hoped to extend in the course of my research. Furthermore, I pursued the approach of others by viewing the OM metadata schema as providing TMS directories to any form of information, hard or soft, and noting that the processes by which this metadata is maintained consisted of a complex set of routine and ad hoc, formal and informal, technological and social interactions [10]. My focus in modelling OM was the storage, sharing, and retrieving of the cognitive, regulative, and normative contents of the OM through a TMS: I did not try to cover other dimensions such as generality and specificity of knowledge, or the epistemology of OM, etc.

I combined the OM literature from management science, TMS research from group psychology, and data modelling techniques, in an attempt to develop a general purpose data model of an organization’s group-level TMS directory. Because TMS research in psychology and management science has focussed on how to measure a TMS [11], the performance benefits of a well-developed TMS [20] and the antecedents of TMS development [2,15], focussing my work on the structure of the group TMS directory seemed a logical next step. OM and group memory research in IS has tended to focus on the capture of the memory provided by databases and Intranets. This does not address the fact that OM is stored in many different containers that vary by task or project type, and that most of an organization’s knowledge is tacit and will remain so.

TMS seems most beneficial in reducing task time in large groups solving a dynamic task with volatile knowledge needs [17]. The better the group transactive directories, the better the group performance and the greater the amount of knowledge exchange [19]. The degree of sharing of mental models, combined with strong transactive memory (ease of finding the knowledge), the better the group performance [4]. A positive correlation exists between strength of TMS and knowledge worker team performance [12]. TMS is positively correlated with group capability for many reasons: its facility to store and utilize more knowledge than a single individual, better knowledge exploitation, appropriate matching of problems to expertise, better anticipation of performance and appropriate allocation of tasks, better decision making through expertise evaluation, and cognitive load reduction permitting more specialization.

## 2.2. Research on organizational memory

Exploring the structure, content, and processes of organizational memory requires access to rich data in a natural setting. Therefore an in-depth case study is suitable. OM and organizational learning concepts provide powerful metaphors for openended, exploratory interview questions and allowed me to extract wide-ranging information about an organization’s needs and to determine how it goes about using its memory effectively. As the patterns and structure of OM are not known a priori, factors that constrain or facilitate the performance of OM help in identifying its salient descriptive or structural features. I used a research technique based upon a method proposed by Walsh and Ungson<sup>1</sup>: 1. Determine the constitution of the memory of the organization through detailed data collection, induction and mapping.

2. Determine how people find and use the memory components, analysing any issues to see if there are patterns in them which inhibit or facilitate their access.

3. Create a schema that describes the OM, considering design solutions that provide functions to maintain the metadata and facilitate access to the OM in whatever form or location it is stored.

Although this approach mirrors classic analysis used for the preparation of a conceptual database design, my purpose was not to develop a model of a particular organization’s memory: I was seeking the attributes which determine how people store, find, retrieve, and use information. In contrast to a business IS, the resulting data schema will be a general purpose model of metadata about OM.

## 3. The investigation

## 3.1. Methodology

I applied a qualitative and interpretive research approach to a single organization which I observed as part of a team, using a case study technique over a period of 18 months. I gained detailed insight into the OM processes and content over several business project lifecycles and from multiple personal, role-based and hierarchical perspectives. The organization was a large, globalized, engineering consulting firm based in Northern Europe and we studied a single Division that delivered projects and consulting expertise to clients in developing countries. The projects involved road building, bridge construction, water management and softer activities, such as institution building and behavioural change. I began the case study by reading the organization’s annual and regular management reports, viewing the corporate intranet and Internet portals, and conducting interviews with the management team; the division employs project managers, engineers and social scientists, mostly located throughout the world. The management framework was a matrix, and work was one-of-a-kind. Consultant reports and engineering or institution building projects were specific to the needs of the client and thus the work, whilst thematically consistent, was driven by distinct problems that required novel approaches and solutions. It was this that made the study particularly interesting: the company’s ability to manage and reuse tacit and explicit knowledge across physical distance was critical to its success.

## 4. Data collection

I collected data through conducting interviews, organizing workshops, reading operational documents, and assessing protocols. A total of 2 workshops and 47 interviews were conducted with 23 different staff members at six-monthly intervals over a period of 18 months, with participants varying according to their availability (see Appendix A). All managerial positions (managers, administrators, specialists and project managers) were represented and participants from head office, overseas, and different sub-areas were interviewed. This allowed me to cover all staff perspectives on OM, conduct cross-checks on the characteristics given by different participants, confirm that the model was correct and gain insight into all phases of the business cycle.

Following the OM research programme, the first interview was used to gain an understanding of the work and draw out the content and structure of the organizational memory (see Appendix B). An OM schema was developed and annotated with the issues pertaining to the use of that memory for operational purposes and learning. This and the associated issues were shared with the organization in presentations and four interim reports. Three subsequent sets of interviews over the next 18 months confirmed the structure of the memory and used follow-up questions to confirm changes or improvements in use or storage of the OM.

## 4.1. Data analysis

Data analysis was performed in two steps. The first analysed the interview data and arrived at a schema of the OM of the organization. All interviews were transcribed and the OM domains and key entities within them were identified. These domains and entities were formed inductively and named according to the nature of the knowledge (sales, project management, etc.). Statements and constructs were grouped with other like-statements and domains were formed, the interview data was reviewed to see if my abstractions matched those of the participants, and generalization was then performed until the distinctions became trivial (when combining two into one domain blurred important distinctions between them). Another similar pass over the data then identified entities which belonged to the domains. I tried to consider alternative options and the model was verified by participants in the interviews and workshops.

The second step in data analysis uncovered the OM characteristics of the new data model and it was entered into the software product ‘‘MindManager’’ as a concept map. Statements regarding access to the elements of the memory were linked to domains, entities, or the learning processes which stored information in or retrieve information from memory. These comments were then analysed for common threads and consistent responses. Difficulties in accessing OM were of particular use, as they highlighted access paths that would otherwise not be noticed if they were available and thus not salient or obvious.

The outcome was a concept map of the properties of OM which influenced the organizational learning processes. For example, water management experience was difficult to determine as it was unrecorded (in peoples’ minds) and they were relatively unavailable (often working in the field). Thus the form in which memory was stored and its location influenced its retrieval: such properties were the metadata for a working OM data model.

## 5. Results

Fig. 1 is the high level schema of the Division’s OM using UML modelling notation. Each element is a ‘‘domain’’ of expertise in the company, though elements of the model may be typical of engineering consulting firms in general. My purpose here was not to generalise on the content, but to use it to discover what might be its generally applicable OM characteristics.

For each domain I noted items that might represent the general structural characteristics of OM (although the domain descriptions were not comprehensive). In identifying typical attributes of OM metadata I asked: does this attribute influence a person’s capability or motivation to store, retrieve, or use knowledge in the OM?

Strategic management combines the experiential knowledge of senior managers, market experts, and technologists with explicit, published vision and mission statements, organization plans and performance data. Decisions are legitimized by their formal codification in the planning process, but the ‘‘memory’’ input is diffuse and based upon experience, belief, and conviction. The general area of operational management on the other hand covers sub-domains of routine staff planning and development, creating staff work plans, project logistics as codified in the organizational handbook (but not in the English language) as well as everyday problem resolution. This is non-formalised and based upon the memories of managers, whose role identified them as hubs and gatekeepers who locate knowledge for others. The division is sub-divided into groups responsible for market areas such as water and environmental management. Knowledge within these areas is deep but tacit and includes solution design, client needs, and the policies that were relevant to a particular market area. Customer knowledge includes relationships and prior interactions with customers, knowledge of their characteristics, policies and requirements, previous history of cultural and political specifics of the environment, upcoming marketing opportunities etc. This knowledge is acquired personally and directly, through engagement with the customer and includes their idiosyncrasies, preferences and intentions. Ethical dealings with customers are documented in the organizational handbook and enacted in the organizational culture. Proposal knowledge is used to formulate responses to RFPs and includes proposal preparation (templates, previous proposals, winning formulas), knowledge of people who could work in the project and their skills, project management, and technical knowledge. Technology is used to store templates, text standards, and previous bids but there is effective management of the required tacit knowledge: groups of experienced consultants are involved in discussion and review. Project management knowledge is mainly explicit. Their control systems stipulate budget management, scheduling, reporting etc., and are specific, mandated and public. Experienced personnel are routinely asked to review projects; a very effective use of tacit memory. Technical expertise is available in engineering, construction, hydrology and water management, and also social science, languages, and dialects. It is gained through education and work experience and it is not possible to codify this knowledge. Consultants increase their knowledge on-the-job and by interaction with colleagues as needed. Knowledge is found through the online CV system, personal contacts, or by asking a manager. There is a database of independent contractors who constitute an external memory. Project specific knowledge is knowledge uniquely relevant to an individual project, which can be explicit (the terms of reference, contracts, the project plan, change management and quality records and documents, billing and budget, etc.) stored in formal documentation which provides high control and monitoring material. This is always accessible. Nevertheless, details are retained in the project manager and participant’s heads.

![](/api/attachments/6TBHRFAM/fulltext/images/d75ae31ed3d631ca65f34118ba4f8f84cfa28ca3356801633376a8bf302c7184.jpg)  
Fig. 1. UML high level conceptual data schema of the division.

Organizational awareness involves sensing metadata, which supports both the retrieval of memory from known sources and its transfer to relevant targets. The absence of organizational awareness leads to staff capabilities being underused. Finally, cultural knowledge, the shared meanings and norms, existed explicitly in management guidelines and implicitly in company values. The company is seen as having high ethical standards – but remote employees are frustrated at not feeling that they belong to the firm and its ideals. The company spirit appears to deteriorate when a consultant is abroad for some time.

## 6. Discussion

The interview data allowed me to develop a schema of the OM. From this case I identified and abstracted the entities and attributes that facilitate or inhibit access to the OM. Some general characteristics of OM emerged in the case study.

OM can be divided into domains of expertise (the body of knowledge expressed in knowledge predicates combining concepts or action), that are important in retrieval and for which there are clear responsibilities. A body of knowledge can be kept in several retainers and a retainer can store the expertise of several domains. Several retainers may have to be used simultaneously to complete a work process. There are different retainer types. When we consider the salient characteristics of the entities, we see the nature of work to be done as one determinant of the most appropriate retainer. For example a quality review requires tacit, responsive knowledge where boilerplate and templates for proposal preparation is highly explicit. The mode of use of memory is interactive and context-specific, suggesting that a person is the most appropriate retainer type. How the memory is acquired is also an attribute that may determine the appropriate retainer: if acquisition is embodied and personal, then storage is probably tacit, making transfer to any other retainer problematic. Under some circumstances, storage is a natural part of the work process, but in others it is a significant effort and consequently not done. The social level of knowledge acquisition plays a role in deciding where it is most convenient and cost-effective to store. For example, if acquisition occurs at a group level through teamwork, then storage will be a function of social knowledge and probably learned from the group through socialization.

There are different costs associated with different retainers. For example, whilst an IS may be the most appropriate or desirable repository for outside staff, there may not be a budget for this. The type of repository may also be determined by institutionalized organizational preferences: e.g., face-to-face knowledge retrieval. People in an organization can use their personal knowledge directories, other people’s knowledge, technologies and maps about OM storage to retrieve it when required. This transactive OM metadata requires its own particular set of processes for keeping up to date and being useful. Thus the transactive directories are part of the OM itself and transform personal or group instrumental knowledge into organizational knowledge.

Organizational awareness of the existence, capabilities, and needs of the rest of the organization or remote staff seemed to be a vacuum in the Division’s OM. For example, the knowledge, intelligence, and on-the-ground expertise of outside staff have been excluded from OM because they are out of the loop. As a consequence, outside personnel feel unappreciated.

Whilst OM suggests a monolithic structure, the existence of conflicting, contradictory and non-intersecting memories imply the opposite. A single domain of expertise can be distributed across different types of retainers and the allocation may be fluid and organic. There are different groups with different perceptions bound together by the organization. Thus there are multiple, contradictory interpretive systems which reflect the preferences of various domains (engineering, human resources, world view, etc.) and histories. But there is a strong sense of conceptual unity in the domain model of the Division’s OM and the variations show it to be a permanent work in progress: indeed the variations exist only because of the overall coherence of mental models, routines, concepts, and norms.

The fragmentation of OM in the Division might be explained by the lack of an institutionalized organizational learning process. There is no program to build a coherent ‘‘organizational memory’’, although it does occur when there is a specific need. The mental maps of managers are kept up to date, but the informal and conversational method of building personal OM directories is confined to co-workers and excludes, for example, remote or travelling staff. As such, the nature of managing knowledge in this Division can be described as cartographic and behavioural [8]: the appropriate method to facilitate this sort of organizational learning is to develop personal transactive directories which generate connections between people rather than codify their expertise and experience.

![](/api/attachments/6TBHRFAM/fulltext/images/26ec3fe0eb889fe355ae6bcfab86b69e508b4af9152fb1d21ca032a2d83cc8b4.jpg)  
Fig. 2. UML conceptual data schema for OM.

## 6.1. The emergent structure of OM

The information schema in Fig. 2 is an entity-relationship model which originally contained three entities: retainers, concepts, and knowledge predicates (marked \*) [21]. The creation of the schema is a design process, and therefore a black art and includes intuition, tacit knowledge, and background beliefs. The entities, relationships and attributes emerged from the extensive interview data as candidates for the OM model.

## 6.2. Entities

The entities were:

\- Retainers – where a specific memory can be stored; a retainer is the storage dimension of OM, such as SAP, a networked drive, or a manager.

\- Concepts/instances – the referents (‘‘Project 4711’’) and concepts (‘‘The Project’’) of knowledge which reflect the socially constructed mental models in the workplace. These can be related to form an ontology.

\- Knowledge predicates – the combination of concepts into memories/propositions stating theories, norms, or facts about the organizational world. For example, a project must have a contract, a schedule and a budget but Project 4711 had a complicated contract, with unusual deliverables.

## The entities which emerged in the study were:

\- Retainer type – the type of bin (technology, person‘s head, procedure, etc.) where it is stored. For example, knowledge predicates for retrieval during a quality assurance process are stored in a person.

\- Domain of expertise – the area of expertise built from the knowledge predicates. It is usually a major signpost within organizations when searching for a particular memory or possible retainer. They (for example, road construction or water supply) are key signposts for accessing the knowledge predicates about such disciplines.

\- Work process – the productive organizational activity performed by people in certain roles, or part of the value chain: it results in a desired outcome that often has learning as a by-product.

\- Learning process–a reference list of the organizational learning processes, which create, store, retrieve, and use knowledge predicates into and from OM during a business process.

\- Synonyms – other expressions for concepts. Although uniform, unequivocal concept use is usually desirable, it is not always possible in large or distributed organizations and a synonym can capture nuances.

\- Process–Knowledge–OL–Retainer – This is a quaternary link entity which rather than being an object, expresses a crucial relationship between four other entities: a work process, a knowledge predicate, a learning process, and a retainer. It supports the proposal of Brandon and Hollingshead [5] for a taskexpertise-person construct to aid transactive memory development. This entity can instantiate relationships derived from business activity statements such as ‘‘During tender preparation the project manager must locate, use, and update all boilerplate information about the organization from the computer IS’’. This entity consists at a minimum of pointers to these four entities. It can itself also have attributes, such as the ‘‘relevance’’ or ‘‘value’’ of knowledge to a work process, or an indication of the retainer most appropriate to an organizational learning process during a particular work process.

## 6.3. Relationships

The concepts and instances which are our mental model of the world may have synonyms. Concepts can be related to each other to create knowledge predicates, expressing facts, and theories about work and life in the organization. A knowledge predicate can be part of one or more domains of expertise, which consists of a set of work processes that may be sub-processes of work processes. A knowledge predicate may be required by a particular work process. A learning process is a part of a work process executed during an activity required by that work process. The knowledge predicates that are input to a work process are best held in one or more retainers for future use. Here a retainer can only be of one type.

## 6.4. Attributes

Many attributes are obvious, but some have a normative dimension: the interview data contained many comments like: ‘‘This person should know that. . .’’ Certain breakdowns or successes in accessing the OM indicated that there was an appropriate place or medium to store it which might be different from where it is normally stored. This confirms Chang and Cho’s [7] finding that OM should be activated according to the task’s project or task characteristics. Confusion in communication between divisional subgroups indicated that language was not used consistently in the firm and that divergences in memory had to be understood if the memory was to be improved. This normative knowledge is itself part of the OM and its metadata.

For the retainer entity type ‘‘person’’, likeability, competence, and historical connection to others were important attributes: though they would probably never be included in a firm-wide OM directory [13]. But firms with a congenial culture or a matrixproject system with dynamic teams may find that the firm’s transactive memory would be improved by the maintenance of individual transactive directories. Matrix structures form linkages between people from diverse organizational units, who access each other’s knowledge long after their projects have been completed.

An attribute map/content was included in the knowledge predicate entity to indicate parts of an OM that are maps and those that are its content. Often personnel have to work through a chain of pointers to retrieve content, so a directory of transactive memory must contain predicates and meta predicates. When this directory information is part of the OM, its storage, update and retrieval is facilitated and the underlying content is made visible.

The knowledge predicate entity should be able to accommodate as attributes any form of knowledge. Tacit knowledge can be described but not captured and its retainer identified: for example, that Fred has a strong feeling for Ugandan protocols. Cultural knowledge can be expressed as propositions, for example, that the firm does not deal with corrupt governments. The value, legitimacy and mindfulness of the knowledge need to be known to improve its management (for example to secure or not over manage it) and to increase its visibility.

The organizational learning process entity emerged as a significant actual and normative determinant of where memory should reside and be accessed. The attributes of this entity not only qualify the appropriate retainer but they can be used to develop useful heuristics, such as:

\- Where knowledge acquisition is a team process, OM resides in groups;

\- Where knowledge acquisition is on the job, knowledge subsequently resides in persons’ heads;

\- Where knowledge storage is explicit and standardised (such as proposal preparation), much of the input memory is explicit, e.g., templates, boilerplate and document chunks and best stored in technology;

\- Where the knowledge retrieval is interactive and contextual, the organizational memory is best found in a qualified person;

\- If the retrieval and use is distributed or remote or has wide scope, technology based retainers are appropriate.

The data suggests that there are multiple interpretive systems and often diverging or conflicting definitions and understandings of what constitutes knowledge in an organization. An explicit schema of OM can be used to manage these towards greater convergence.

## 7. Conclusions

My paper discussed OM using a transactive memory approach. I mapped the memory of a large engineering consulting organization and identified entities, relationships, and attributes that constitute useful OM metadata. It has the limitation of being only one instance of an OM from which to derive general characteristics, but its data were rich and deep. I found that using mapping techniques was an effective way of identifying specific items of memory. The hindrances to the learning processes that exploit that memory revealed the characteristics of storage and access pathways. I observed that OM has attributes such as needs to know and most appropriate retainer, some of which have a normative component that gives members of the organization a sense of how to plan or manage their OM.

## Appendix A

See Tables A1 and A2.

Table A1  
Interview participants.

<table><tr><td>#</td><td>Location</td><td>Role</td><td>Nr interviews</td></tr><tr><td>1</td><td>HO based</td><td>Head Office Resource Manager</td><td>4</td></tr><tr><td>2</td><td>OS based</td><td>Project Manager</td><td>4</td></tr><tr><td>3</td><td>HO based</td><td>Head Office Project Assistant</td><td>2</td></tr><tr><td>4</td><td>HO based</td><td>Market Area Manager</td><td>4</td></tr><tr><td>5</td><td>HO based</td><td>Project Coordinator</td><td>1</td></tr><tr><td>6</td><td>OS based</td><td>Project Manager</td><td>2</td></tr><tr><td>7</td><td>HO based</td><td>Project Specialist/Consultant</td><td>4</td></tr><tr><td>8</td><td>HO based</td><td>Project Specialist/Consultant</td><td>1</td></tr><tr><td>9</td><td>HO based</td><td>Market Area Manager</td><td>4</td></tr><tr><td>10</td><td>HO based</td><td>Head Office Knowledge Manager</td><td>4</td></tr><tr><td>11</td><td>HO based</td><td>Director</td><td>4</td></tr><tr><td>12</td><td>OS based</td><td>Branch Manager</td><td>1</td></tr><tr><td>13</td><td>OS based</td><td>Branch Manager</td><td>1</td></tr><tr><td>14</td><td>HO based</td><td>Corporate Knowledge Manager</td><td>1</td></tr><tr><td>15</td><td>OS based</td><td>Project Specialist/Consultant</td><td>1</td></tr><tr><td>16</td><td>OS based</td><td>Project Specialist/Consultant</td><td>2</td></tr><tr><td>17</td><td>OS based</td><td>Branch Manager</td><td>1</td></tr><tr><td>18</td><td>OS based</td><td>Project Specialist/Consultant</td><td>1</td></tr><tr><td>19</td><td>HO based</td><td>Project Specialist</td><td>1</td></tr><tr><td>20</td><td>OS based</td><td>Branch Manager</td><td>1</td></tr><tr><td>21</td><td>OS based</td><td>Market Area Manager</td><td>1</td></tr><tr><td>22</td><td>HO based</td><td>Portal administrator</td><td>1</td></tr><tr><td>23</td><td>HO based</td><td>Project Assistant to MA Manager</td><td>1</td></tr><tr><td colspan="2"></td><td>Total</td><td>47</td></tr></table>

Table A2 Interview distribution.

<table><tr><td></td><td>Interviews</td><td>Workshops &amp; (presentations)</td></tr><tr><td>0 months</td><td>13</td><td>2</td></tr><tr><td>6 months</td><td>11</td><td>(1)</td></tr><tr><td>12 months</td><td>10</td><td>(1)</td></tr><tr><td>18 months</td><td>13</td><td>(1)</td></tr><tr><td>Total</td><td>47</td><td>5</td></tr><tr><td>Total different staff</td><td>23</td><td></td></tr></table>

## Appendix B. Two-interview questions

## B.1. Organizational memory

Organizational (or corporate) memory is the means by which knowledge from the past is brought to bear on present activities. It can also be seen as corporate knowledge which gives structure and meaning to events and allows shared interpretation to emerge.

Content of organizational memory

\- What do you think constitutes the information and knowledge which makes your Department effective or even special?

Sharedness of organizational memory and characteristics hindering this.

\- Do you think the staff in your Department has a strong common and shared understanding of this knowledge?

\- What factors do you think might influence this?

Location of organizational memory – retainers

\- Where is information and knowledge regarding roles, procedures and work-related advice usually kept (technology, paper, and people’s heads)?

\- How is this information and knowledge usually found?

\- Are there any issues in accessing this information and knowledge?

## B.2. Organizational learning processes

Knowledge processes are the processes which support the sharing, learning and creation of knowledge in your organization.

Distribution/externalisation

\- Are there any things in your work environment which you feel influence your capability or motivation to express your knowledge to others?

Acquire/internalisation

\- Are there any things in your work environment which you feel influence your capability or motivation to absorb new knowledge?

Interpretation/objectivation

\- Do you think the organization learns from your experiences?

\- Describe the processes of how the organization learns from the experiences of the staff.

\- How does it make this available to others who might need it?

Organizational learning processes

\- What are the processes for developing and approving new and improved processes? Do they work well?

## References

[1] M.S. Ackerman, C. Halverson, Organizational memory as objects, processes and trajectories: an examination of organizational memory in use, Computer Sup ported Cooperative Work 13 (2), 2004, pp. 155–189.

[2] A.E. Akgun, J. Byrne, H. Keskin, G.S. Lynn, S.Z. Imamoglu, Knowledge networks in new product development projects: a transactive memory perspective, Information & Management 42 (8), 2005, p. 1105.

[3] L. Argote, E. Miron-Spektor, Organizational learning: from experience to knowledge, Organization Science 22 (5), 2011, p. 1123.

[4] J.R. Austin, Transactive memory in organizational groups: the effects of content, consensus, specialization, and accuracy on group performance, Journal of Applied Psychology 88 (5), 2003, p. 866.

[5] D. Brandon, A.B. Hollingshead, Transactive memory systems in organizations: matching tasks, expertise and people, Organization Science 15 (6), 2004, p. 633.

[6] H.S. Cha, D.E. Pingry, M.E. Thatcher, Managing the knowledge supply chain: an organizational learning model of information technology offshore outsourcing, MIS Quarterly 32 (281), 2008.

[7] D.R. Chang, H. Cho, Organizational memory influences new product success, Journal of Business Research 61, 2008, pp. 13–23.

[8] M. Earl, Knowledge management strategies: towards a taxonomy, Journal of Management Information Systems 18 (1), 2001, pp. 215–233.

[9] R.M. Henrya, G.E. McCrayb, R.L. Purvisc, T.L. Robertsd, Exploiting organizational knowledge in developing IS project cost and schedule estimates: an empirical study, Information & Management 44 (6), 2007, pp. 598–612.

[10] P. Jackson, J. Klobas, Transactive memory systems in organizations: implications for knowledge directories, Decision Support Systems 44 (2), 2008, pp. 409–424.

[11] K. Lewis, Measuring transactive memory systems in the field: scale development and validation, Journal of Applied Psychology 88 (4), 2003, pp. 587–604.

[12] K. Lewis, Knowledge and performance in knowledge-worker teams: a longitudi nal study of transactive memory systems, Management Science 50 (11), 2004, pp. 1519–1533.

[13] L. Lu, Y.C. Yuan, Shall I Google it or ask the competent villain down the hall?. The moderating role of information need in information source selection Journal of the American Society for Information Science and Technology 62 (1), 2011, pp 133–145.

[14] M.L. Markus, Toward a theory of knowledge reuse: types of knowledge reuse situations and factors in reuse success, Journal of Management Information Systems 18 (1), 2001, pp. 57–93.

[15] I. Oshri, P. Van Fenema, J. Kotlarsky, Knowledge transfer in globally distributed teams: the role of transactive memory, Information Systems Journal 18 (6). 2008 pp. 593–616.

[16] D. Randall, J. Hughes, J. O’Brien, M. Rouncefield, P. Tolmie, ‘Memories are made of this’: explicating organisational knowledge and memory, European Journal of Information Systems 10, 2001, pp. 113–121.

[17] Y. Ren, K.M. Carley, L. Argote, The contingent effects of transactive memory: when is it more beneficial to know what others know, Management Science 52 (5), 2006, pp. 671–682.

[18] H. Weinberger, D. Te‘eni, A.J. Frank, Ontology-based evaluation of organizationa memory, Journal of the American Society for Information Science and Technology 59 (9), 2008, pp. 1454–1468.

[19] Y. Yuan, J. Fulk, P. Monge, N. Contractor, Expertise Directory Development, Shared Task Interdependence and Strength of Communication Network Ties as Multilev el Predictors of Expertise Exchange in Transactive Memory Work Groups, Com munication Research 37 (1), 2010, p. 20.

[20] Z. Zhang, P. Hempel, Y. Han, D. Tjosvold, Transactive memory system links work team characteristics and performance, Journal of, Applied Psychology 92 (6), 2007, p. 1722.

[21] D. Nevo, Y. Wand, Organizational memory information systems: a transactive memory approach, Decision Support Systems 39 (4), 2005, pp. 549–562.

![](/api/attachments/6TBHRFAM/fulltext/images/f63e703bfb8665d23b8fb1a354169744d8361e8f6c88d3d0b1e9351bf8fef9c3.jpg)

Paul Jackson has been an IT industry practitioner for over twenty vears. He has managed development of large software systems in diverse areas from ERP to public housing and network management in Australia and Germany. He has consulted to industry and public service organizations in strategic IS planning, ISbusiness alignment and systems development. He joined Edith Cowan University in June 2002 as a lecturer in the School of MIS. He has a PhD in information systems development and his particula research interest is investigating knowledge and information management in projects from philosophi

cal, social and cognitive perspectives to improve outcomes. He has published in a variety of journals including Decision Support Systems, Information Technology & People and the International Journal of Project Management.
