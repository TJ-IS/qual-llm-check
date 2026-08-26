---
otero_id: 26383
otero_key: "4THK5GTJ"
title: "Memory-Based Feedback Controls to Support Groupware Coordination"
authors: "Alex Bordetsky; Gloria Mark"
year: "2000"
journal: "Information Systems Research"
doi: "10.1287/isre.11.4.366.11871"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## 6SR

![](/api/attachments/4THK5GTJ/fulltext/images/934478a5c7f4bb93e8e88725332cd28cffdf79d5321a86939918affb25a149c0.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Memory-Based Feedback Controls to Support Groupware Coordination

Alex Bordetsky, Gloria Mark,

To cite this article:

Alex Bordetsky, Gloria Mark, (2000) Memory-Based Feedback Controls to Support Groupware Coordination. Information Systems Research 11(4):366-385. http://dx.doi.org/10.1287/isre.11.4.366.11871

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2000 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/4THK5GTJ/fulltext/images/83e6902c5ee9d16350073053c460daf564234eab1c5764cbbec19495efcd4dfb.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Memory-Based Feedback Controls to Support Groupware Coordination

Alex Bordetsky • Gloria Mark

Information Systems, Naval Postgraduate School, Monterey, California 93943

Department of Information and Computer Science, University of California, Irvine, Irvine, California 92717 abordets@nps.navy.mil • gmark@ics.uci.edu

n this paper we first present an empirical study of groupware use illustrating problems that users faced with restricted feedback about others’ activities. Awareness can aid users in learning interdependencies, and in forming conventions to regulate system use and information-sharing. As a solution to providing awareness, we integrate the framework of organizational memory with intelligent agent technology to provide a coordination mechanism that enables the structuring of awareness events and gives information about the users feedback control. In the proposed model, feedback control relationships are captured into a multilayered model of organizational memory and transferred to users by agents-facilitators. The approach is based on a system dynamics approach to organizational learning.

(Groupware; Awareness; Conventions; Feedback Control; Coordination; Intelligent Agents; Case-Based Reasoning; Organizational Memory; Collaborative Technology)

## 1. Introduction

As we gain user experiences with groupware systems, we are also learning more about the problems of working in distributed environments with limited information about others. Awareness in shared work serves many purposes. It can be used to selectively inform others, to clarify interdependencies among group members, and to form and maintain conventions. Yet, despite such advantages of awareness information, we need to balance the tradeoff of informing others with maintaining privacy.

Awareness mechanisms, designed to alleviate the problems of limited information with groupware use, face significant challenges. There has been much discussion in the field of Computer-Supported Cooperative Work (CSCW) of balancing the tradeoff of costs and benefits of awareness in electronic work. Costs consist of privacy and work disruptions (Pedersen and Sokoler 1997, Gaver et al. 1992, Hudson and Smith 1996), the intrusion of remote ambient noise levels (Mantei et al. 1991), processing incoming information, and grouping asynchronous events to make sense of them (Mark and Bordetsky 1998). Benefits of awareness information include having access to relevant information to support collaborative work, such as knowing when someone else is available, when work has been completed, or which task another group member is currently working on (e.g., Dourish and Belloti 1992).

Hudson and Smith (1996) characterize this two-way street. The more output information that we provide to others, the less privacy we have. On the other hand, when we intentionally notify others, it is overhead. The more input information we get about others, the more informed we are, but more overhead is added to our work. In contrast, in collocated work, we can guard privacy; we control what information we disclose to others. We can selectively focus on information with little effort. Awareness is reciprocated through gestures, facial expressions, and back-channel responses.

Awareness mechanisms are also quite limited in the information they can supply about work. In shared office environments, much of our knowledge about our co-workers is derived not only from observing their current activities, but from a larger base of experience that we develop simply by working alongside them. This includes knowing their educational and work backgrounds, work interests, media preferences, schedules, personalities, and so on. We take such information into account in everyday work, for example, by knowing who to ask about a task (e.g. based on expertise), or by knowing whether colleagues prefer to be asked a question by email or verbally (depending on how busy they look, or how urgent we need an answer). Face-to-face work is continually carried out by integrating our knowledge of background information with current events. Therefore, in designing awareness mechanisms, we need to consider carefully how event information can be enriched, so as to provide a meaningful context for users.

The goal of this paper is to describe the benefits and limitations of awareness in electronic distributed work. This discussion is based on a user study of groupware in an actual work setting. We propose a solution for presenting feedback to the group during system use, and integrate this feedback with users’ background profiles. This paper is organized as follows. In §2, we discuss the problem of awareness as a feature of shared work, contrasting collocated and distributed work. In §3, we discuss information sharing problems and how they exist in groupware use. In §4, we introduce technical issues to be considered in designing awareness mechanisms. In §5, we present a model in which feedback control relationships are captured into an organizational memory and then transferred to users by agent-facilitators.

## 1.1. Approaches to Providing Task-Based Awareness

Some awareness systems have focused on supporting informal interaction (Whittaker et al. 1997, Gale 1994, Abel 1990, Gaver et al. 1992, Fish et al. 1990, Heath and Luff 1991, Mantei et al. 1991). Although the distinction between formal and informal awareness support in distributed work is not yet crystallized (Heath et al. 1995), this paper focuses on the issue of providing taskbased awareness information. This includes not only providing current information about activities but also incorporating it with the necessary background information needed to provide a more complete context for the information.

Awareness systems have been designed to aid synchronous and asynchronous groupware use. Early examples with synchronous work include providing a “metastructure” for coordination and information sharing processes through mechanisms such as hypermedia structures and integrated e-mail (Leland et al., 1988) or through a shared reference (Tatar et al. 1991). In asynchronous work, role assignment and explicit annotation were used in the PREP system (Neuwirth et al. 1990), and simple feedback was used with ShrEdit (Olson et al. 1992).

In addition to these task-oriented approaches, person awareness was achieved by updating video images of remote partners (Dourish and Bly 1992). More recently, attention has been given to the dual role that group members have in performing both individual and group work through the use of activity indicators (Gutwin et al. 1996). The provision of different group and individual workspace views supports users in navigating, handling artifacts, and representation (Gutwin and Greenberg 1998). The importance of both present and past awareness information (Sohlenkamp et al. 1997), as well as users’ interests (Fuchs 1999), has also been considered in the design of awareness systems. However, despite the variety of approaches, we are still a long way from providing awareness information for a wide range of collaborative activities, such as decision-making, communication, handling of shared objects, and general coordination support.

## 1.2. Research Setting and Methodology

In the next sections, we contrast our discussion of awareness in collocated work with empirical observations illustrating the role of awareness in distributed electronic work. The results are from a study of groupware system use in a German government ministry, the PoliTeam project (see Klo¨ckner et al. 1995 for a detailed description of PoliTeam). The goal of PoliTeam is to supplement paper work processes with electronic processes as the German government moves from Bonn to Berlin. The analysis is based on observations over 3 years of 12 users in the Federal Ministry of Family Affairs, Senior Citizens, Women, and Youth in Bonn and in a corresponding ministry department in Berlin. The data are from observations made in workshops, site visits, discussions between designers and users, and three sets of user interviews.

The shared workspace of PoliTeam is used by two cooperating groups: typists in a central typing pool and members of a ministry unit. The typists and most of the ministry unit members are located on different floors of the same building in Bonn and met face-toface occasionally. Two ministry unit members are in Berlin and met face-to-face with the Bonn employees about once every 6 months. The two heterogeneous user groups can be distinguished by differences in jobs, tasks, education levels, career path orientations, salaries, and computer experience.

The shared workspace has two purposes. First, it provides access to documents for all the members of the writing office (typing pool) and the ministry unit. Unit members send handwritten text or recordings to the writing office to produce a text document. Later, unit members and typists exchange the document for modifications, and the typists eventually produce a final copy. The second purpose is that it provides access for unit members to all documents within the ministry unit. Unit members co-author documents, people store ministry information, and the unit leader needs to have access to the work produced in his unit.

## 2. Awareness as a Feature of Shared Work

In this section, we describe in more detail the role of awareness in shared work and contrast it with the role of awareness in distributed electronic work.

## 2.1. Awareness Contexts

Interaction is affected by what we know of the other. Cooperative work is affected by the information that is shared by the group. People may choose to disclose information or not to the group. In a shared office environment, people generally assume that publicly visible objects are known to all, i.e., there is open awareness for the state of these objects. A closed awareness context occurs when information is withheld from others, e.g., papers are locked in drawers or meetings exclude people. In the case that someone steps unexpectedly into another office and reads a private document on the computer screen that is embarrassing, then it could result in a mutual pretense: Each person pretends that the other does not know. Still another case is when a closed awareness context is not intentional, e.g., when because of an oversight, a person is not informed of an important piece of information, such as a memo about a potential merger.

Various types of knowledge states such as these are described by Glaser and Strauss (1965) as awareness contexts, i.e., what each person knows about the other and the reciprocal knowledge that the other is aware of about him or her. The state of awareness in a group has substantial impact on interaction. Furthermore, awareness contexts can change, as people gain or withhold new information, which in turn affects interaction. Glaser and Strauss maintain that people strategically control their awareness contexts. In collocated work, people lay only that information on their desk that they want others to see. Only final drafts of papers may be distributed, while work-in-progress is not. This type of closed awareness is consistent with Goffman’s (1959) description of how people control the information that they reveal to others to maintain a desired impression.

## 2.2. Awareness Contexts in Distributed Electronic Work

Different awareness contexts have arisen among the PoliTeam users. A closed awareness context developed since the users wanted to maintain a distinction between public and private work. In the system requirements analysis, users requested that they have a personal workspace in the system to store their private documents.<sup>1</sup> For example, the unit leader has connections to another German Bundesland ministry, which is headed by a Social Democrat. He did not want all his shared work with this ministry to be seen by his own department head, who is in the other party in the coalition. In general, the users are very careful as to which documents they put in the shared folder, knowing that all will have access to it. The users maintain privacy during their working process, storing, for example, early drafts in private workspaces.

Awareness contexts are also formed by the different employees’ requirements for information, which are tied closely to their work roles. For the typists, it is a benefit that notification is automatically sent to unit members when they place a completed document in their shared folder. For the unit members, receiving notifications is a benefit, e.g., when new documents are placed in their shared folders. For the unit leader, who has distinct management functions, he receives benefits by learning who has made changes to, and who possesses an alias, for a shared document. This is more information than either the unit members or typists need. Some people would like to have information about general events and activities that occur in the shared workspace cabinet (PoliTeam uses office metaphors for containers); for others it as an information overload. Thus, awareness serves different purposes for different workspace members, depending on their task and perspective. Problems in interaction arise when users believe that others have the same awareness information as themselves, e.g., believing that another user will receive notification when they place a document in the workspace, when the user has in fact constructed an awareness profile that only reports very general events. Thus, the degree of awareness is not the same for all, and users behave as though it is.

Closed awareness contexts have also arisen among the PoliTeam users due to the overhead involved in notifying others. For example, one shared cabinet has been established for users to store relevant group information, e.g., changes in law, government policies, address lists, etc. All unit members and typists have access rights to this information. However, it requires overhead for someone to inform the others that relevant information has been added to shared cabinets. Users do not have the time to constantly check the new documents and keep themselves up-to-date on new information that is continually being added. Moreover, the users do not invest the time to organize the shared cabinet. As a result, information that is highly relevant for writing speeches or answering citizen queries, e.g., a new tax law, may be missed.

## 2.3. Learning Interdependencies

Coordination mechanisms to make interdependencies visible in collocated work exist in various forms. For example, project plans are commonly posted in public areas, often as explanations for visitors, and show clearly roles and responsibilities. Timelines indicating schedules are often of a less public nature, and are more available within a work group than outside of it. Joint schedules, at the work group or even department level, show who, when, and why (e.g., vacation or travel) office members will be absent. The value of these devices is that they provide information about others’ activities that is readily visible, and people know which others are informed because of the public or semipublic nature of these devices. Such coordination mechanisms illustrate clearly interdependencies among work group members.

A good example of the value of face-to-face settings in aiding coordination of work is found from observations of group members working in a control room in the London Underground. One of the most important coordination mechanisms for the members was provided by a common information display. By monitoring other members’ changes to it, the workers gained awareness of the state of others’ work (Heath and Luff 1992). Another example is found in Rogers (1993), who reports on the use of a centrally located whiteboard for managing files, which served to make each person’s activities visible to the group. This mediating mechanism enabled each group member to adjust his/her own work practice as they became aware of others’ actions. Rogers’ example illustrates explicit dissemination of awareness information, whereas the study by Heath and Luff shows that awareness may also be gained through peripheral observation.

## 2.4. Learning Interdependencies in Distributed Electronic Work

The means to show interdependencies in electronic work are available, such as a Web visibility page or electronic calendar that publicize people’s roles and schedules. The problem is that it must be updated continually, and many examples of groupware use have shown that users do not always do this extra work (Grudin 1988).

In contrast to collocated work, users often did not understand that documents stored in a shared workspace are affected by other members’ actions. In one case, a typist called the user hot line (resulting in a site visit) to report that a document had disappeared from a workspace, when actually another workspace member had removed it. The typist received no information that another person had accessed the document. Another example concerns changing access rights of shared folders, which affects all shared files inside the folder. Users sometimes mistakenly changed access rights. When a document becomes private, then it does not appear visually on the desktop to people who do not have the access rights. Yet, members received no feedback that access rights were changed, resulting in confusion.

## 2.5. Conventions

Conventions arise organically in a group that is collocated. Observing others’ actions enables behavior to be modeled or discrepant actions to be resolved (Lewis 1969). Becker (1982) points out that conventions govern decisions about how a group should conduct their work and, as a result, they make coordination efficient. A group need not reinvent new approaches but can instead draw on earlier experiences. Conventions in work can function to regulate relations between workers, styles of writing, filing systems, how meetings are conducted, use of equipment, etc. Shared knowledge of conventions make it possible for a group to easily cooperate.

However, problems in forming conventions arise when cooperating partners are heterogeneous. A shared object provides actors with common information. In an organizational work arrangement, the same shared object is handled according to different functions, purposes, perspectives, and interests of the cooperating actors involved. Members of the same work team, as part of the development of the group, generally develop similar interpretations for shared objects. Yet, often cooperation occurs between actors who belong to heterogeneous work groups. As a result of different work experiences, educational backgrounds, and expertise, such heterogeneous members develop diverse views on the shared objects. Yet, it is precisely because boundary objects are subject to different interpretations and handling that the task of managing transactions with them becomes complex (Star and Griesemer 1989).

Managing boundary objects is a good example of the need for cooperating partners to mesh their different perspectives, i.e., to engage in articulation work (Gerson and Star 1986). Not only must the interdependencies in the cooperative work itself be articulated but also, in principle, the procedure for arriving at an established arrangement may itself be an articulation process (Schmidt and Simone 1996). In any case, articulation is aided by physical collocation; identifying discrepancies in actions or in the handling of objects and communicating to resolve them are easier to do when face-to-face then whan actors are distributed.

## 2.6. Conventions in Distributed Electronic Work

When cooperating actors are no longer physically collocated but are remote, the management of interdependencies in groupware use becomes an even more challenging problem. We define conventions in electronic work as agreements established in the group common to all members for carrying out the following transactions, found through our investigation of the PoliTeam system: communication transactions, e.g., who to inform about document changes; data processing transactions, e.g., times when a document should be created and distributed as an alias or as a copy; and decision-making transactions, e.g., who is responsible for a document or for maintaining the order of a workspace. Convention requirements were defined by the users and include: storing (and defining) old and current documents, shared task conventions, clarifying borders between public and private work, and forming modus vivendi when workspace members are absent.

What makes it difficult for groups to use shared workspaces (and other groupware that are not strict workflow systems) without conventions is that they are open systems (Hewitt 1985) because of their evolving nature, the insufficient internal information of actors, the decentralized decision-making involved, and their use by those having different perspectives and conflicting beliefs. Users are thus conducting work in an atmosphere with information in an incomplete context that is highly dynamic. Furthermore, shared workspace design generally does not prescribe a set order or method for using its features; user actions are constrained only by the features available, e.g., a workspace may not have synchronous application-sharing.

Whereas conventions may arise naturally in a collocated group, a distributed group needs to formally establish agreements for procedures. A work team with a long history may be able to apply previous conventions to a new electronic work situation but, as with the PoliTeam users, who are heterogeneous, they must agree upon and form new procedures. Conventions in electronic work serve several purposes. They can help to avoid redundancy and process losses. They can regulate transactions with shared objects, which is especially important in heterogeneous groups. They can help make electronic work processes more transparent by enabling people to keep track of events, such as when new documents versions are completed. Finally, conventions can enable new group members or substitutes to smoothly adapt to work or members to resume work after an absence.

However, although the PoliTeam users agreed formally on procedures in common workshops, it was discovered that these agreements were often violated. For example, the typists required that they retain access to the latest electronic version of a shared document, so that they can incorporate changes into it. Yet, unit members violated this agreement and removed shared folders from the workspace so that the documents were not accessible to the typists. Almost all users did not use a required ministry file code when they created documents (moving the burden on to other users). A third violation is that users entered addresses into personal lists instead of an agreed-upon shared address list (Mark et al. 1997).

From the users’ perspective, they found it was difficult to form and define conventions with limited feedback. As one unit member reported:

We must think over, depending on the information that we have, which shared work areas would be sufficient. But I’m not in the situation where I can see that, i.e., where I get information other than that for my own folders.

This was especially true with emerging work processes, such as those made possible by establishing a shared workspace between the Bonn and Berlin departments. However, because the fast transaction of information is a new experience for both locations, it is not clear yet what role the shared workspace will have. As one unit member explained:

When we use more information together with Berlin, then we must really think what (shared work areas) would be useful.

For example, should we have things where we pack five things inside, or something else? It also depends on what it is, i.e., what kind of information. I think that in certain folders, it must be this way. It is necessary. Otherwise we have chaos. Or someone has chaos for themselves.

## 2.7. Maintaining Privacy and Regulating System Use

We have discussed so far the role of privacy and the value of receiving information in shared electronic work. We have described how distinct awareness contexts arise naturally in collocated work but also in electronic work. Importantly, we should not assume that shared work operates within an environment of open awareness. We have discovered that groupware users want products to be kept private until they are willing to disclose them. However, certain aspects of the work process can be revealed. Moreover, different users have different information requirements for others’ work processes. Feedback can operate selectively and be catered to individual needs, for example, by informing about key events in a work process while withholding specific information about content.

Awareness information could benefit users in learning interdependencies by informing each other of the consequences of their actions. For example, in the case of learning about the interdependencies of access rights and shared folders, feedback could help users understand processes that are currently not visible on the screen. In this way they learn that access rights have changed for others.

We propose that learning of the day-to-day actions of the group’s use of the shared workspace is beneficial for defining conventions. As the users expressed, without knowing others’ (or the group’s) information needs, it is difficult to organize a shared workspace, e.g., knowing which documents are considered current or outdated by others. Feedback information would also inform users when they violate conventions. For example, the writing office requires that it retain access to the latest electronic version of the document for future changes. However, this agreement is often violated, as unit members (e.g., a co-author) often removed the electronic version of the document and forgot to inform others.

Feedback conforms to the users’ wishes; most users report that they do not want to be controlled to follow conventions. Nor does the unit leader want to be an “enforcer.” He argues for the users to inform each other of violations in “subtle and sensible” ways. Thus, feedback that makes activities more transparent in electronic work could help users maintain current conventions, change them, and define new ones.

## 3. Awareness and Information Sharing

## 3.1. The Problem of Information Sharing

Individual differences in the naming, organization, and retrieval of information have been a problem of concern for some time (e.g. Allen 1991; Saracevic and Kantor 1988a, 1988b). Known as the vocabulary problem, different people rarely use the same words to refer to the same information (Furnas et al. 1987, Furnas 1982). Different naming and sorting conventions should be expected to arise naturally for groups with different expertise and specializations. Many scientific subdomains use different classification and nomenclature schemes for the same concepts, e.g., engineers (Trigg et al. 1999), biologists (Chen et al. 1997a) and zoologists (Star and Griesemer 1989). Perhaps there is no better example of this problem occurring on a wide scale than the Human Genome Project, which will be faced with offering a comprehensive body of data to biological research communities who use distinct vocabularies and databases (Chen et al. 1997a).

## 3.2. Awareness and Information Sharing

To date, little attention has focused on the problem of how groupware users name, retrieve, and classify information. We can extend these findings from scientific communities to the more mundane domain of everyday work. The PoliTeam user groups were also heterogeneous and had their own distinct vocabularies and means of operation, developed through their work roles (typists and civil servants), education, and experience.

We found that each PoliTeam user group developed their own conventions for naming, structuring, and accessing their shared information. The writing office, who typed documents for the unit members, created one shared folder for each unit member. These workspaces were contained in another folder, resulting in a two-level hierarchy. The typists worked electronically before PoliTeam was introduced and had established a convention for naming documents, using the DOS restriction of 8 characters, which specified the class of document, the name of the unit member, and the date. The typists sorted documents by the name of the unit member and date of creation.

In contrast, the unit members organized their documents by creating a shared folder for each work topic. This resulted in a deep multilevel structure for most of the unit members. Their sorting criteria for documents was based on the content of a document, e.g., a speech on a senior citizen initiative. Documents created by the typists, with their naming scheme, were difficult for unit members to access and sort. In particular, dates were of little value for accessing information, because unit members worked on multiple documents in parallel, cycling through different drafts. On the other hand, unit member documents named by content were difficult, if not impossible, for typists to access and sort.

Most PoliTeam users use a location-based finding strategy for documents (Wulf 1997). Unit members reported that they could not find documents among the vast array of information in the shared workspace because the system supported only the typists’ (two-level hierarchy) view. In addition, all users reported that they do not always know the current information stored in this shared workspace. Furthermore, the method that was used in exchanging intergroup documents was basically ad hoc. Each user had to specify in which directory the finished document should be placed. The solution worked fine for individuals who were careful about specifying locations but broke down when this information was not provided to the typists. It is an overhead for both typists and unit members to communicate about which subdirectory the finished document must be placed into.

In a workshop 6 months after the system was introduced, a convention was set for all PoliTeam users to use the typists’ system of person names and dates for naming shared documents. Because these names had no meaning for the Unit members and because their preference was to name documents according to subject, they began using the subject area within the document to write out terms in more detail. Although this helped individuals retrieve information, it hindered collaboration by leading to even more distinct classifications. One unit member used what others termed “fantasy names,” which had personal meanings for him but had no relation to the document content.

What further compounds this problem is that users have a choice of displaying information by lists or by icons. However, when icons are used, document names are cut off, and only a cryptic name is visible. As a result, the users began to add their own personal keywords to understand the content of the document. They referred to the documents according to these new keywords. Thus, different requirements led the two user groups, unit members and typists, to reference the same documents using different semantics. This became especially problematic when the users referred to documents in discussion.

In sum, the users structured their information using different methods, which correspond to their work roles, i.e., whether they type documents or write content. Multiple perspectives are intrinsic in many work situations and call for articulation. However, the process of reconciling different perspectives for the typists and unit members is difficult, because their individual perspectives are logical for their work roles and tasks.

## 3.3. The Benefits of Feedback for Information Sharing

It might be argued that there are more effective solutions than awareness information to aid groupware users in naming, retrieving, and classifying information. Why not use a solution such as a translation mechanism (Dourish et al. 1999) so that the users can retain their own naming and classifying conventions? Other approaches to overcoming the vocabulary and classification problems have included using a latent semantic structure (Dumais et al. 1988), increasing the number of names per object (Gomez et al. 1990), or using automatically generated thesauri (Chen et al. 1995), existing thesauri (e.g. Chamis 1991) or multiple thesauri for different domains (Chen and Ng 1995).

Although many of these approaches have demonstrated improvement for users in managing information, they are designed for users who remain in their separate communities. In other words, these solutions work fine for users who do not collaborate. The

PoliTeam users and other users of groupware are not just storing and retrieving the shared information in isolation but are interacting with it, engaging in collaborative processes such as problem-solving and document writing and production. Multiple separate views work fine for individual retrieval and classification, but supporting communication about the documents requires establishing a common ground among the users. Especially in asynchronous work, individual indexing strategies will not work to help users develop a common reference for their collaborative products.

We assume that feedback can help collaborating partners develop a common ground for their products. By understanding what is contained in the documents, they can better refer information to each other that might be beneficial to work, for example, to help solve the complaint that users have of not knowing what information is contained in the shared closet or to find information relevant for co-authoring documents. We assume that in the long term, it can help users produce better collective knowledge bases, as face-to-face discussion has shown (Whittaker et al. 1994). As Ehrlich and Cash (1994) note, “on-line information is only part of the whole picture associated with the creation and dissemination of corporate knowledge.”

We expect that feedback could also help users maintain agreed-upon categories for shared information. In the TeamInfo project (Berlin et al. 1993), group members agreed on a core set of classifications for shared knowledge in a group memory but found it difficult to follow them, as did the PoliTeam users. Feedback can help a group reinforce agreements by informing the group when classifications are violated. In this way, the group can either enforce the classification or refine it to more adequately

## 4. Implementing a Computerized Model of Organizational Memory

Thus far, we have described the role of awareness in shared work, both in physically collocated and distributed electronic settings. Through an empirical study, we have illustrated that different states of awareness can result in different contexts of work and that awareness can aid users in learning interdependencies and forming conventions for system and information use. In this section, we now discuss the technical aspects of awareness, as an introduction to the model.

## 4.1. Feedback Relationships of Events

Designing an effective system of computerized organizational memory is associated with the known challenge of integrating informal and documented knowledge (Chen et al. 1997). We address this issue by structuring organizational memory based on the feedback relationships of events in a shared workspace. It is known that feedback relationships and causal loops play a critical role in the human understanding of organizational system dynamics (Senge and Sterman 1990, Sterman 1989). The coordination of cooperative activities should be based on revealing interdependencies involved in the usage of shared objects (Malone and Crowston 1994). Whereas feedback itself refers to an input-output relationship, feedback control refers to real-time action in the feedback loop. We consider feedback control interdependencies between the (cooperative) process output, state, and input controls to be most critical for coordinating asynchronous and synchronous work via a groupware system. We provide a model for capturing such feedback relationships into computerized organizational memory and conveying it to cooperating partners by using a case-based reasoning technique. According to this model, the feedback controls are communicated to other users via a set of agent-facilitators (Genesereth and Ketchpel 1994, Bordetsky and Bourakov 1998).

## 4.2. Event History for Associating Actions and Effects

Earlier in the paper we described the overhead that is introduced when an awareness mechanism introduces asynchronous events; the user must try to make sense of these different pieces of incoming information. A requirement for an awareness mechanism of a shared workspace, therefore, is to facilitate for users the learning of relationships between actions and effects. In a synchronous shared workspace environment, the effects of users’ actions can be immediately seen. For example, ShrEdit, a multi-user text editor, enables users to see the views of others, or to “find” other users in the shared document (Olson et al. 1992). Additionally, one has access to activity information; users can see who is tracking whom. This provides information on other users’ actions but not their effects. In a study of ShrEdit use, the users asked each other about effects of actions, such as who had written certain parts, or they cautioned each other about the consequences of their actions.

The relationship between action and effect is easier to learn in a synchronous, as opposed to an asynchronous environment, because actions and effects are contiguous in time (e.g., Moeller 1954). However, an asynchronous shared workspace inhibits learning the relationships of actions to effects because of the numerous events that occur over time. For this reason, we have chosen to use an event history, which records the actions and effects and which we believe can be useful to aid users in pairing together the relationships.

## 4.3. Memory-Based Coordination

Earlier we also presented the problems that users face in trying to form conventions for groupware use. Are there any known examples of successful software mechanisms for convention support? Surprisingly, one of the best-known examples of convention support could be found in the area of telecommunications management. It is well-known that one of the most successful solutions that provides interconnectivity of heterogeneous networks (i.e., it establishes the conventions for LANs “talking” different protocols) is a TCP/ IP control mechanism. Why is it easy for heterogeneous nodes to communicate via the TCP/IP protocol? Because it breaks down the communication relationships to one that is basic and simple: The nodes exchange the packets that are enveloped by all necessary address attributes to reach the destination independently. The routing table (a version of memory) advises where to direct the packet first (the method is connectionless). The control (the feedback) on packet transmission is almost immediate; the packet with an unresolved address or error detection immediately gets sent back.

In the interactive environment of PoliTeam, the activities are diverse and driven by individual and group task-related differences. The role of simple basic relationships that could be understood by PoliTeam users with different backgrounds and different views on the process becomes especially important. We propose to use feedback control relationships that could be easily understood by the PoliTeam users with different backgrounds and views on the cooperative process. The next question is how to capture and adopt such relationships? We propose to use a dedicated model of organizational memory that would enable cooperating users to learn emerging feedback relationships and adopt them to coordinate their work in the groupware system environment.

The body of organizational memory (OM) literature is growing rapidly. The definitions of OM vary, but many of them clearly put knowledge management, i.e., knowledge capturing, and knowledge transfer in the center of an organizational memory framework (Ackerman 1993, Chen et al. 1997, Conklin 1996, Morrison 1993, Sandoe and Olfman 1992, Stein 1996, Stein and Zwass 1995, Walsh and Ungson 1991). For example, according to Stein and Zwass (1995), through organizational memory, past knowledge is used for current activities to increase the effectiveness of an organization. In a groupware environment, in which information technology naturally complements the organizational process, the resources for knowledge management include individuals, teams, procedures and policies, software, hardware, and telecommunication resources. Because this paper addresses the issues of computer models for organizational memory, we look first to previous models.

According to Stein and Zwass (1995), the different computerized models of organizational memory could be structured relative to the application tasks as was done in Table 1.

It is easy to see that none of these memory models addresses directly the application targets for the PoliTeam memory that are necessary to carry out activities such as document production, annotation, retrieval, and exchange. These examples also do not provide solutions for constructing explicit representations of the described feedback structure for collaboration.

The model presented in the next section proposes to provide a representation of events occurring in the shared workspace that can be viewed easily by users through the feedback control structure. However, to better illustrate the value of the model, we need to provide some more background on the PoliTeam system usage. Tasks performed in the shared workspace, such as collaborative writing, often involve multiple users and multiple operations. A typical collaborative writing task may involve, for example, two ministry employees composing the speech, exchanging versions with each other and with the Unit leader, who gives his comments, which are then incorporated into the speech. Tasks done by the Unit employees are also generally conducted in parallel. Additionally, because of the asynchronous nature of the shared workspace, events concerning the same task are spread out over time. The events might include a new document version reintroduced into the workspace and then the writer notifying the relevant group members. However, documents concerning different tasks are continually being placed into the workspace, such as new speech versions, answers to citizen’s queries, or new ministry information. Thus, a simple event history list would require much overhead by the users to sort through the events to piece together relationships and reconstruct a cohesive event history surrounding one particular task, such as collaborating on a speech. The model we propose involves compressing the representation of a task or of components of a task by relating the events through the feedback control structure. Such a compressed representation is easier for users to learn, because it requires less load on the memory to associate the events (e.g., Conklin 1996).

Table 1 Organizational Memory Types and Corresponding Applications

<table><tr><td>Memory Type</td><td>Nature of Support</td></tr><tr><td>Group/team memory</td><td>Small business team support across time and project</td></tr><tr><td>Design rationale/discussion memory</td><td>Preserves the evolutionary order of product design</td></tr><tr><td>Project memory</td><td>Support of a large project, usually with distributed participants</td></tr><tr><td>Meeting memory</td><td>Provides continuity to a series of meetings</td></tr><tr><td>Topical memory</td><td>Accumulates answers on a targeted range of topics</td></tr><tr><td>Document memory</td><td>Provide access to a targeted set of documents</td></tr><tr><td>Environmental memory</td><td>Assists in interacting with the organizational environment</td></tr></table>

Based on the above considerations, we provide a model for capturing feedback relationships, storing feedback structure in a computerized organizational memory, and revealing it to cooperating partners by using a case-based reasoning technique. In the proposed model the feedback controls are communicated to the groupware users via a set of agent-facilitators (Genesereth and Ketchpel 1994, Bordetsky and Bourakov 1998).

By screening the feedback relationships in case memory, the agents allow users to view the state of the task, expected output, and available input controls. By transferring task descriptions and adopted solutions into the case memory, the agents facilitate case-based reasoning learning of evolving group task processing relationships. Knowledge of captured relationships and their dynamics correspondingly improves user awareness of the teamwork process.

## 5. Structuring OM for Representing Feedback Relationships

Definition 1. Let P(t)-{X(t), U(t), I(t)} describe the PoliTeam supported collaborative task process at any given moment of time t. X(t) is a set of collaborative process state variables. Examples include:

—responsiveness variables (asynchronous, synchronous),

—reach variables (communications log),

—range variables (sharing pattern (broadcasting, multicasting, routing), membership).

U(t) is a set of user input controls. Examples include: —selecting a different circulation path,

—sending a new document to the shared workspace, —invoking a desktop video conferencing call.

I(t) describes the environmental impact to the group process. Examples include:

—organizational changes,

—deadline changes,

—introduction of new information and communication technology.

P(t) denotes the group process (task) outputs. Examples include:

—document,

—transaction,

—decision(s).

Based on this model we can identify the PoliTeam Event list as a representation for the following list of structures:

$$
\begin{array}{r l} & \text { PoliTeam\_Event } (t) \\ & = \{U (t), X (t), P (t), I (t) \}, t = 1, 2, \dots . \end{array}\tag{1}
$$

At any given moment t of group task processing the structure (1) enables one to associate the group output P(t) with the observed state of group communication X(t), individual inputs U(t), and potential environmental impacts I(t). In terms of the described model, the instances of PoliTeam events could be mapped as follows:

• user profile attributes, e.g., user’s role, scheduling preferences, expertise, map into U(t) elements;

• document profile attributes, e.g., date of production, subject area, state of completion, map into X(t) elements;

• folder profile attributes, e.g., documents that it contains, links to other folders, members involved, timeline, map into X(t) elements;

• path profile object, e.g., circulation path, shared workspace, desktop conferencing call, map into U(t) elements;

• privacy profile, events that the user wants to withhold, e.g., early versions of shared documents, map into I(t) elements.

The feedback model frame initially maps the relationships for communication transactions. We define conventions as rules that extend further up to the data processing and decision-making transactions. Correspondingly, we need to generalize the input, output, state, and environmental categories of the feedback model to be applicable to data processing and decision-making transactions. For example, one document is an input to the others. One user has a certain folder to take, and the other must sign it. It is also the case that these multiple relationships cannot be defined prior to system deployment. They could be captured and upgraded only during the run-time sessions with the groupware. It means that we need to add the features for capturing and transferring feedback-based knowledge from the past.

Computer-aided organizational memory presents one of the most powerful solutions for delivering the features of the structured awareness mechanism to support groupware convention-making. In the following sections we describe the concept of organizational memory. To tie the concept of organizational memory to the specific features of a feedback structure for the PoliTeam awareness information, we suggest the following definition.

Definition 2. The function of a computerized organizational memory (M) is to facilitate awareness of groupware activities by capturing the feedback relationships:

$$
M: \{\text { PoliTeam\_Event } (t), \text { PoliTeam\_Event } (t - 1),
$$

$$
\ldots , \text { PoliTeam\_Event } (t - k) \} \rightarrow \{U (t + 1) \}\tag{2}
$$

that enable compressed representations for awareness events.

From the user perspective, quick access at any time to compressed representations of awareness data improves the groupware users’ ability to achieve:

• reduction of transaction time,

• reduction of task processing time,

• increase of the task concurrency,

• learning (increase of complementary knowledge) We expect that these gains would also facilitate users in forming conventions. The memory process (2) facilitates the convention-forming process by capturing the structure for:

$$
\text { PoliTeam\_Event } (t) = \{U (t), X (t), P (t), I (t) \}\tag{3}
$$

and providing the cross-references between U(t), X(t), and P(t), for each t (or short interval), which would be the function for communication support of short-term memory, or across the history log:

$$
\begin{array}{l} \{\text { PoliTeam\_Event } (t), \text { PoliTeam\_Event } (t - 1), \\ \quad \dots \text { PoliTeam\_Event } (t - k) \}. \end{array}\tag{4}
$$

For learning, the simplest level of memory that we denote as M1 could be used to manage the relationships

$$
\{P (t), \text {   User   View   (PoliTeam\_Event } (t)) \}\tag{5}
$$

This definition fits the metaphor of computerized organizational memory design (Conklin 1996). According to this metaphor, organizational memory should provide short-term memory that supports and enhances both individual and workgroup processes, and provides the index for linking to long-term memory.

According to Chen et al. (1997) the efficient computer-supported knowledge management mechanism of organizational memory should use a combination of semantic-based indexing, environmental scanning, and knowledge retrieval.

In our model, the proposed feedback control structure of PoliTeam events is shown by the relationship {P(t),U(t), X(t), I(t)}, which is a representation for semantic-based indexing. Environmental scanning is represented through the I(t) component in the collaborative process output P(t)-{X(t), U(t), I(t)}. The index is structured to the categories of P(t), U(t), X(t) that populate different layers of case memory. Correspondingly the knowledge retrieval model is a hierarchy of memory layers (Figure 1), in which each next layer (from the bottom up) is an association based on the underlined feedback structure.

## 5.1. Implementing Case Memory: Using Case-Based Reasoning for Learning the Feedback Relationships

Case memory facilitates the learning of feedback relationships and different user views by using a casebased reasoning technique (Sycara 1993) for indexing, capturing, and retrieving the PoliTeam collaborative objects. In this architecture, objects such as individual profiles of collaborators, PoliTeam awareness events, and problem-solving task profiles are different segments (layers) of case frame representation. Some of the segments are populated in real time, such as desktop conferencing and PoliTeam awareness events, for example. The other segments, like task profiles, are mainly populated during the adjustment interactions with agent-facilitators (Figure 1)

Figure 1 Layers of OM Structured According to Feedback Control Relationships  
![](/api/attachments/4THK5GTJ/fulltext/images/eee70eeba92fe2058f63f56f91e63b1aad646257ef2dd1dbe2e8ab6236c24261.jpg)

In this hierarchy Expert profile, Document profile, and a PoliTeam awareness events profile are captured by an agent-facilitator and transferred to the case frame via the database. The other profiles (segments) are populated during the collaborative session interactively (Figure 1).

They are reflected in the PoliTeam feedback model PoliTeam\_Event(t)-{U(t), X(t), P(t), I(t)} as follows:

X(t) - {reach, range, responsiveness},

U(t) - {Expert profile, document profile, PoliTeam events profile},

P(t) - {Task profile (different user views on the task), transaction profile, decision profile}.

The case memory provides the following support for forming conventions via the feedback process. Distributed experts provide the initial knowledge base for likely cases by populating (in natural language) an appropriate set of frames. The resulting case-base provides a comparison between the current design situation and a set of known candidate solutions. Previous solutions are stored as a case memory. When a search fails to locate a similar case, the search itself becomes the basis for creating a new case.

## 5.2. Providing Feedback Controls: Agents-Facilitators

The PoliTeam user could access case memory via the agent-facilitators, which enable collaborators to communicate at different levels of bridges, routers, and gateways, depending on which segments of case memory are involved (Figure 2). In structuring the agents as agent-facilitators with bridging, routing, and gateway functionality, we follow the evolving KQML concept of agent communication models (Genesereth and Ketchpel 1994). We expand the bridging, routing, and gateway functionality into agent integration with case memory. That enables agent-facilitators to integrate profile based filtering and notification functionality (which is typical for intranet agents) with case-based reasoning search for collaboration support resources.

In the bridge state, the functionality of the agent’s communication is limited to broadcasting (or multicasting) to local agents of the team members. Normally this would apply to the members of the same organizational unit, or the team assigned to several consecutive phases of the acquisition process. The format, access rights, and other features of the shared document (model) are not customized by the bridge according to the preferences of individual group members. Everybody gets the same message or the same document.

Figure 2 Types of Agents-Facilitators  
![](/api/attachments/4THK5GTJ/fulltext/images/278bda272cedb932abab0d3f4150dfaef82aad2a70508ecf19c42c8167f13fe0.jpg)

In the router state, the communication capabilities of the agent are more advanced. The router is capable of generating individual user packets that are customized according to individual preferences and rights. It may then send the packets directly to the team member using his or her direct Internet and/or ISDN address. The router state makes use of multiple control tables to issue the packet and incorporates the bridge functions. The router state would be useful in managing collaborative sessions with representatives of different organizational units that have temporary or unique duties associated with the task at hand.

In the gateway state, the routing functionality is extended by the capability to communicate with agents who manage different dimensions. For example, the electronic meeting gateway would access the interface bridge to share a portion of the commenting process with other organizations. The functionality of the gateway is the most complex among the three states and requires multiple associative structures.

Based on the described considerations, we developed the prototype of lower level case memory and an agent-facilitator that provides routing functionality for the PoliTeam members’ communication. This prototype could be used by the PoliTeam groupware users for receiving awareness information about the different users and their views of the same task. According to the proposed feedback structure for the simplest level of PoliTeam memory, as described by expression (5), this prototype represents the M1 level memory. The concept of layered memory model is based on the different levels of feedback relationships. The function of M1 level case memory is illustrated in Figure 1. We designed the memory prototype in the development environment of the ART\*Enterprise system for coding distributed case-based reasoning architectures. In this example, case-memory is a collection of interrelated objects (segments) that are monitored on the basis of an index hierarchy represented by feedback relationships:

$$
\text { PoliTeam\_Event } (t) = \{U (t), X (t), P (t), I (t) \}.
$$

Figures 3 and 4 illustrate the routing agent-facilitator that provides groupware users access to the case memory and populates the case memory by user profile and awareness events from the system log. In the menu bar at the bottom (Figure 4), “Case profile” opens up the link to the case memory. The “Preferences” menu provides the capturing of user communication preferences and individual profiles. The upper segment of case memory keeps group communication state attributes X(t) of the awareness model. The next segment describes the user’s view of the task P(t). The lower portion of the case structure describes the feedback controls U(t) associated with user and document profiles.

## 5.3. A PoliTeam User Scenario for Coordination

In this section we present a user scenario to illustrate the implementation of the model. As described earlier, a typical task for PoliTeam users is to collaboratively write a speech for the Minister. In this scenario, several workspace members are involved in writing the speech, and they regularly show drafts to their Unit leader for his comments.

Specifically, the task is to collaboratively write a speech on how proposed new high-speed transportation affects environmental policy in the Rhine River industrial centers. The speech is to be presented to a particular environmental group P, and must be completed within a tight time deadline (I(t)).

• The Unit Leader (UL) needs to confer with the workspace members (WM) to issue the new task. The UL consults with the workgroup memory via the agent-facilitator. The UL checks recent cases of “environmental group P” as well as “transportation” by looking up the past cases in case memory. Through the agent-facilitator, the UL identifies that WM3 and WM4 have been previously involved with writing speech topics that concern this environmental group P and transportation issues, respectively. He also finds that WM4 prefers desktop video conferencing, and WM3 prefers shared application work. Then, on behalf of the UL, the agent-facilitator issues the video call to WM4 based on her conferencing preferences captured in the case-memory (X(t)) (Figure 4). A decision is reached: WM3 will write an introduction geared to the noise pollution policy, and WM4 will write the body of the speech, which discusses the cost implications. Reviewing the output (P(t)) (Figure 3) segments for both— introduction and text body cases—the agent-facilitator recognizes financial information relevance and prompts the UL to contact W3 to write about finances. Subsequent events appear as follows: Workspace members include: WM3, WM4, and UL.

• On behalf of UL, agent-facilitator UL posts in the case memory a new case (task description) into the expected output (P(t)) segment (Figure 3).

• A notification is sent to WM4 and WM3 that UL has placed the document (U(t)).

• WM4 joins the group and places the “Cost Models” document into the shared workspace. The UL and WM3 are able to view the change via the output segment (P(t)) (Figure 3).

• On behalf of the UL request the agent-facilitator searches for similar tasks (cases) underway. Among them is transportation policy analysis. By sharing and viewing the X(t) segment for the transportation policy case (similar to Figure 4) they find that they can use WM3 results for high-speed transport impact in order to evaluate the cost implications for the Rhine River industrial centers.

• WM3 transfers the document to the case memory that reveals in P(t) changes to the other members. The agent-facilitator on his behalf requests a video conference with WM4 and UL to discuss which information should be included in the speech (U(t)) (Figures 5 and 6).

Figure 3 Viewing P(t): WM4 Places a New Document Version into the Shared Workspace P(t)  
![](/api/attachments/4THK5GTJ/fulltext/images/530739d1c9216ea7eaa596fd91dd9f7b05bff670649d2b30315ae6d4273e1365.jpg)

The described state of collaborative process is captured and represented in the X(t) segment of the case memory feedback control structure {P(t), X(t), U(t)} for the Rhine River industrial centers environmental policy task.

Thus, we see in this simple scenario that the agentfacilitator can help expedite a task of speech writing by informing users of information relevant to their particular task. The unit leader receives information to see what previous speech topics the employees have had experience with and uses this memory to divide up the labor and assign new tasks for the current speech.

It is sometimes, if not often, the case in real work that one user will have information relevant to someone else’s task but is not aware that it is needed. This corresponds to a closed awareness context described earlier. The agent facilitator provides this awareness information, in the case of informing the employee that new financial information has been introduced into the workspace which may be relevant for his or her task. Although we have presented a simplistic scenario to make the role of case memory clear, we should mention that real work in a ministry is generally much more complex, and user actions and tasks are less welldefined. Considering this complexity, we feel that the awareness information that case memory would provide would prove beneficial for managing interdependencies in a shared workspace environment.

## 5.4. Enabling Privacy and Reducing Event Monitoring Overhead

The implementation of case-based reasoning in the groupware feedback controls contributes naturally to the need for collaborating workspace members to maintain privacy (see the earlier discussion on privacy and awareness contexts). Suppose that a part of the U(t) segment is information that could be used to match the user profiles identified by the privacy tools. If the application profile X(t) contains a pattern, containing part of the expert’s personal data that should be released, then U(t) to agent-router would be not to initiate the control attribute, i.e. video call, user local program initiation, or local data file sharing, that would violate the user’s privacy. The agent-facilitator configured for a privacy search would detect what application events should be given out in a way similar to the application profile capturing represented in Figure 4: reviewing the prototype U(t) segment in case memory and excluding privacy violating controls from the current U(t).

Figure 4 Mapping X(t) to U(t), Feedback Control Summary  
![](/api/attachments/4THK5GTJ/fulltext/images/106c3d668fca49e018285290e711f4a36bdd6a81aa12ba03e3ec76f6ecb4b85e.jpg)

Case-based reasoning in the groupware feedback controls also contributes to reducing overhead in monitoring incoming events. Over time, the patterns of U(t), X(t), P(t), and I(t) in the case-based reasoning memory will link together asynchronous and synchronous events that correspond to user and application profiles. Users would not need to associate the connection management and certain task processing events, resulting in significantly less event monitoring overhead.

## 6. Conclusions

In cooperative electronic work, awareness is an elusive concept. We have tried in this paper to attain a more precise notion of awareness by describing the role that such information plays in shared work. We presented examples showing how actual users working in a shared workspace face a variety of problems by having restricted activity and feedback information from their cooperating partners. In both collocated and electronic work, awareness may not be evenly distributed among group members, resulting in the formation of different knowledge contexts. In any form of cooperative work, users need to learn the interdependencies that exist to find methods to manage them, such as forming conventions. Conventions are especially needed for groupware use, ranging from regulating actions with the system to the naming, retrieving, and classification of shared information.

Although PoliTeam had more users than described in this study, we need to issue a caveat about our experiences with a limited number of users. Not only is

Information Systems Research Vol. 11, No. 4, December 2000

Figure 5 Example of U(t): Notifying and Calling a Meeting with UL and WM3  
![](/api/attachments/4THK5GTJ/fulltext/images/a42e8bf8f1aa49e6c3526a41fbcdfdc0608a8cd0012a35a21b2aa6369f3871cc.jpg)

the count of users small but also their work domain is very specific, namely, a government organization. Workers in a government organization have different organizational policies, tasks, and degrees of work flexibility, compared to what we might expect in other environments, such as industry. Thus, although the user requirements that we elicited as a result of the specific system use might be relevant for future users in this ministry, it is not clear to what extent our results can generalize. We present our results as a case study, and we hope that they can spark further work in this area. However, we would expect that the general problems that users encounter processing awareness information in a collaborative environment could generalize to other domains to some extent.

We have presented as a solution a computerized organizational memory feature for capturing the feedback relationship of events in a shared workspace. The awareness mechanism structures the events to provide feedback in the broad classes of transactions: communication transactions, data processing transactions, and decision-making transactions. Because it is difficult to define the multiplicity and complexity of relationships a priori to system use, we added the features for indexing, capturing, and retrieving collaborative objects.

For example, the PoliTeam users search documents in the shared workspace using a location-based strategy (Wulf 1997). The unit members’ search strategy was found to be different from that of the typists, and the documents were organized according to the typists’ scheme. Thus, the storage scheme affected whether documents could be found. Awareness notification, as presented in the model, could overcome the reliance on such schemes, even the strategic placement of documents, because notification is independent of location, i.e., it is specified by other criteria.

We began this paper by describing the tradeoff in awareness information: Benefits of awareness can be offset by extra overhead and privacy costs. In the model we have tried to alleviate these costs. By compressing the representation of a task, or components of a task, and relating events through a feedback control structure, asynchronous events are linked together for the user. The model incorporates a privacy profile, individual to the user, that enables the user to disallow certain events to be publicly available.

Figure 6 Example of Agent-Router Work for Scheduling Input Controls U(t)  
![](/api/attachments/4THK5GTJ/fulltext/images/bd979952b1f0c0ca31e6588f16bbec18546b0cb419e08072b1361b1a6b51d2d2.jpg)

Our next step is to implement the model in a real work context and observe the effect that feedback has on the groupware users. When conventions are not followed, a feedback mechanism can inform users to reinforce the correct usage of the system. For specific convention knowledge, such as storing old and current documents, case memory provides support. A groupware environment such as a shared workspace is dynamic; new work operations emerge, membership can change, and activities can be fluid. Feedback and activity information are necessary components of a groupware environment to support such dynamics in group work.

## References

Abel, M. J. 1990. Experiences in an exploratory distributed organization. R. E. Kraut, J. Galegher, C. Egido, eds. Intellectual Teamwork: The Social and Technological Foundations of Cooperative Work. Lawrence Erlbaum Associates, Hillsdale, NJ.

Ackerman, M. S. 1993. Definitional and contextual issues in organizational and group memories. UC Irvine ICS Technical Report. University of California, Irvine, CA, 93–42.

Allen, B. L. 1991. Cognitive research in information science: Implications for design. Ann. Rev. Inform. Sci. Techn. (ARIST) 26.

Becker, H. S. 1982. Art Worlds. University of California Press, Berkeley, CA.

Berlin, L. M., R., Jeffries, V. L. O’Day, A. Paepcke, C. Wharton. 1993. Where did you put it? Issues in the design and use of a group memory. Proc. Conf. Human Factors and Comput. Systems (IN-TERCHI’93). ACM Press, New York, pp. 23–30.

Bordetsky, A. 1996. Study of the Design Requirements for Integration of Organizational Memory into the PoliTeam Awareness Mechanism. GMD-FIT, German National Center for Research in Information Technology, Sankt-Augustin, Germany.

——, E. Bourakov. 1998. Agents-facilitators for adaptive management of collaborative environments. Proc. 3rd INFORMS Conf. Inform. Systems Tech. Montreal, Canada, 82–96.

Chamis, A. Y. 1991. Vocabulary Control and Search Strategies in On-Line Searching. Greenwood Press, New York.

Chen, H., W. K. McHenry, K. J. Lynch, S. E. Goodman. 1997a. A Textual Database/Knowledge-Base Coupling Approach to Creating Computer-Supported Organizational Memory, University of Arizona, Tucson, AZ.

, D. T. Ng. 1995. An algorithmic approach to concept exploration in a large knowledge network (automatic thesaurus consultation): Symbolic branch-and-bound vs. connectionist Hopfield net activation. J. Amer. Soc. Inform. Sci. 46(5) 348–369.

——, D. T. Ng, J. Martinez, B. R. Schatz. 1997. A Concept space approach to addressing the vocabulary problem in scientific information retrieval: An experiment on the worm community system, J. Amer. Soc. Inform. Sci., 48(1) 17–31.

——, B. R. Schatz, T. Yim, D. Fye. 1995. Automatic thesaurus generation for an electronic community system. J. Amer. Soc. Inform. Sci. 46(3) 175–193.

Conklin, J. E. 1996. Designing Organizational Memory: Preserving Intellectual Assets in a Knowledge Economy. Corporate Memory Systems, Inc., Austin, TX.

Dourish, P., V. Bellotti. 1992. Awareness and coordination in shared workspaces. Proc. CSCW ’92, 107–114.

, S. Bly. 1992. Portholes: Supporting awareness in a distributed work group. Proc. CHI’92. ACM/SIGCHI, New York, 541–547.

——, J. Lamping, T. Rodden. 1999. Building bridges: Customisation and mutual intelligibility in shared category management. Proc. GROUP’99. Phoenix, AZ.

Dumais, S., G. W. Furnas, T. K. Landauer, S. Deerwester, R. Harshman. 1988. Using Latent semantic analysis to improve access to textual information. Conf. Proc. Human Factors in Computing Systems. Washington, D.C., 281–286.

Ehrlich, K., D. Cash. 1994. Turning information into knowledge: In formation finding as a collaborative activity. Digital Libraries’94. College Station, TX.

Fish, R. S., R. E. Kraut, B. L. Chalfonte. 1990. The VideoWindow system in informal communications. Proc. CSCW’90. ACM Press, New York, 1–11.

Fuchs, L. 1999. AREA: A cross-application notification service for groupware. Proc. Sixth Euro. Conf. Computer-Supported Cooperative Work. Kluwer Academic Publishers, Dordrecht, The Netherlands, pp. 61–80.

Furnas, G. W. 1982. Statistical semantics: How can a computer use what people name things to guess what things people mean when they name things. Proc. Human Factors in Comput. Systems Conf. Gaithersburg, MD, 251–253.

——, T. K. Landauer, L. M. Gomez, S. T. Dumais. 1987. The vocabulary problem in human-system communication. Comm. ACM 30(11) 964–971.

Gale, S. 1994. Desktop video conferencing: Technical advances and evaluation issues, S. A. R. Scrivener, ed., Computer-Supported Cooperative Work: The multimedia and networking paradigm. Avebury Technical, Aldershot, UK, 81–104.

Gaver, W., T. Moran, A. MacLean, L. Lo¨vstrand, P. Dourish, K. Carter, W. Buxton. 1992. Realizing a video environment: Europarc’s RAVE system. Proc. CHI’92. ACM/SIGCHI, New York, 27–35.

Genesereth, M. R., S. P. Ketchpel. 1994. Software Agents. Comm. ACM 37(7) 48–53.

Gerson, E. M., S. L. Star. 1986. Analyzing due process in the work place. ACM Trans. Office Inform. Systems 4(3) 257–270.

Glaser, B. G., A. L. Strauss. 1965. Awareness of Dying. Aldine Publishing Co., Chicago, IL.

Goffman, E. 1959. The Presentation of Self in Everyday Life. Doubleday & Co., Inc., New York.

Gomez, L. M., C. C. Lochbaum, T. K. Landauer. 1990. All the right words: Finding what you want as a function of richness of indexing vocabulary. J. Amer. Soc. Inform. Sci. 41(8) 547–559.

Greenberg, S., C. Gutwin, A. Cockburn. 1996. Using Distortion-Oriented Displays to Support Workspace Awareness. Dept. of Computer Science, University of Calgary, Calgary, Canada.

Grudin, J. 1988. Why CSCW applications fail: Problems in the design and evaluation of organizational interfaces, Proc. CSCW ’88. Portland, OR, 85–93.

Gutwin, C., S. Greenberg. 1998. Design for individuals, design for groups: Tradeoffs between power and workspace awareness. Proc. CSCW ’98. ACM Press, New York.

——, M. Roseman, S. Greenberg. 1996. A Usability Study of Aware ness Widgets in a Shared Workspace Groupware System. Proc. CSCW’96. ACM Press, Cambridge, MA, 258–267.

Heath, C., P. Luff. 1991. Disembodied conduct: Communication through video in a multi-media office environment. Proc. CHI’91. ACM Press, New York, 99–103.

, ——. 1992. Collaboration and control: Crisis management and multimedia technology in London underground line control rooms, Comput. Supported Cooperative Work (CSCW), An Internat. J. 1 69–94.

——, A. Sellen. 1995. Reconsidering the virtual workplace: Flexible support for collaborative activity. Proc. Fourth Euro. Conf. Computer-Supported Cooperative Work (ECSCW’95). Kluwer Academic Publishers, Dordrecht, The Netherlands, 83–99.

Hewitt, C. 1985. The challenge of open systems, BYTE 10(4) 223–242.

Hudson, S. E., I. Smith. 1996. Techniques for addressing fundamental privacy and disruption tradeoffs in awareness support systems. Proc. CSCW’96. ACM Press, New York, 248–257.

Klo¨ckner, K., P. Mambrey, M. Sohlenkamp, W. Prinz, L. Fuchs, S. Kolvenbach, U. Pankoke-Babatz, A. Syri. 1995. PoliTeam: Bridging the gap between Bonn and Berlin for and with the users. Proc. Fourth Euro. Conf. Computer-Supported Cooperative Work (ECSCW’95). Kluwer Academic, Dordrecht, The Netherlands, 17–31.

Leland, M. D. P., R. S. Fish, R. E. Kraut. 1988. Collaborative document production using Quilt. Proc. CSCW’88, Portland, OR. ACM Press, New York, 206–215.

Lewis, D. K. 1969. Convention: A Philosophical Study. Harvard University Press, Cambridge, MA.

Malone, T., K. Crowston. 1994. The Interdisciplinary Study of Co ordination. ACM Comp. Surveys 6(1) 87–119.

Mambrey, P., G. Mark, U. Pankoke-Babatz. 1998. User advocacy in participatory design: Designers’ experiences with a new communication channel. Comp. Supported Cooperative Work: J. Collaborative Comp. 7 291–313.

Mantei, M. M., R. M. Baecker, A. J. Sellen, W. A. S. Buxton, T. Milligan, B. Wellman. 1991. Experiences in the use of a media space. Proc. CHI’91. ACM Press, New York, 203–208.

Mark, G., A. Bordetsky. 1998. Structuring feedback for groupware use: Memory-based awareness. J. F. Nunamaker, ed. HICCS 31, 31st Hawaii Internat. Conf. System Sci. Vol. I: Collaboration Systems and Tech. 184–193.

Leigh Star, Associate Editor. This paper was received on February 5, 1999, and was with the authors 3 months for 1 revision.

——, L. Fuchs, M. Sohlenkamp. 1997. Supporting groupware conventions through contextual awareness. W. Prinz, T. Rodden, J. Hughes, K. Schmidt, eds. Proc. ECSCW’97. Kluwer Academic Pub., Dordrecht, The Netherlands. 253–268.

Moeller, G. 1954. The CS-UCS interval in GSR conditioning. J. Experiment. Psych. 48 162–66.

Morrison, J. 1993. Team Memory: Information Support for Business Teams. Proc. Twenty-Sixth Hawaii Internat. Conf. System Sci. 4 122–131.

Neuwirth, C. M., D. S. Kaufer, R. Chandhok, J. H. Morris. 1990. Issues in the Design of Computer Support for Co-authoring and Commenting. Proc. CSCW’90. Los Angeles, CA. 183–195.

Olson, J. S., G. M. Olson, M. Storrosten, M. Carter. 1992. How a Group-Editor Changes the Character of a Design Meeting as well as its Outcome. Proc. CSCW’92. Toronto, Canada, 91–98.

Pederson, E. R., T. Sokolor. 1997. AROMA: Abstract representation of presence supporting mutual awareness. Proc. CHI’97. 51–58.

Rogers, Yvonne. 1993. Coordinating Computer-Mediated Work, Computer Supported Cooperative Work (CSCW), Internat. J. 1 295– 315.

Sandoe, K., L. Olfman. 1992. Anticipating the Mnemonic shift: Organizational remembering and forgetting in 2001. Proc. Thirteenth Internat. Conf. Inform. Systems. Dallas, TX. 127–137.

Saracevic, T., P. Kantor. 1988a. A study of information seeking and retrieving. Part II: Users, questions, and effectiveness. J. Amer. Soc. Inform. Sci. 39(3) 177–196.

, ——. 1988b. A study of information seeking and retrieving. Part III. Searchers, Searches and Overlap. J. Amer. Soc. Inform. Sci. 39(3) 197–216.

Schmidt, K., C. Simone. 1996. Coordination mechanisms: Towards a conceptual foundation of CSCW system design. CSCW: J. Collaborative Comput. 5(2–3) 155–200.

Senge, P., J. Sterman. 1990. Systems thinking and organizational learning: Acting locally and thinking globally in organization of the future. Euro. J. Oper. Res. 59 137–150.

Sohlenkamp, M., L. Fuchs, A. Genau. 1997. Awareness and Cooperative Work: The PoliTeam Approach. Proc. HICSS 30. Wailea, HI., 549–558.

Star, S. L., J. R. Griesemer. 1989. Institutional ecology, “translations” and boundary objects: Amateurs and professionals in Berkeley’s Museum of Vertebrate Zoology, 1907–39. Soc. Stud. Sci. 19 387–420.

Stein, E. 1996. Organizational memory: Review of concepts and recommendations for management. Internat. J. Inform. Management 5(2).

Stein, E. W., V. Zwass. 1995. Actualizing organizational memory with information systems. Inform. Systems Res. 6(2).

Sterman, J. D. 1989. Modeling managerial behavior: Misperceptions of feedback in dynamic decision making experiment. Management Sci. 35 321–329

Sykara, K. 1993. Machine learning for intelligent support of conflict resolution. Decision Support Systems. 10 121–136.

Tatar, D. G., G. Foster, D. G. Bobrow. 1991. Design for conversation: Lessons from Cognoter. Internat. J. Man-Machine Stud. 34 185– 209.

Trigg, R. H., J. Blomberg, L. Suchman. 1999. Moving document collections online: The evolution of a shared repository. Proc. Sixth Euro. Conf. Computer-Supported Cooperative Work, Copenhagen, Denmark, 331–350.

Walsh, J. P., G. R. Ungson. 1991. Organizational memory. Acad. Management J. 16(1) 57–91.

Whittaker, S., D. Frohlich, O. Daly-Jones. 1994. Informal workplace communication: What is it like and how might we support it. Proc. CHI’94. ACM Press, New York, 208–218.

——, J. Swanson, J. Kucan, C. Sidner. 1997. Tele-notes: Managing lightweight interactions in the desktop, ACM Trans. Computer-Human Interaction 4(2) 137–168.

Wulf, V. 1997. Storing and retrieving documents in a shared workspace: Experiences from the political administration. S. Howard, J. Hammond, G. Lindgaard, eds. Human Computer Interaction: INTERACT 97. Chapman & Hall, U.K., 469–476.
