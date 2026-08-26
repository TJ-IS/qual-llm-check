---
otero_id: 16178
otero_key: "R4P3UBKY"
title: "TeamSpirit: Design, implementation, and evaluation of a Web-based group decision support system"
authors: "Minder Chen; Yiching Liou; Ching-Wen Wang; Yi-Wen Fan; Yan-Ping Jeffery Chi"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.07.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# TeamSpirit: Design, implementation, and evaluation of a Web-based group decision support system

Minder Chen <sup>a,\*</sup>, Yiching Liou <sup>b</sup>, Ching-Wen Wang <sup>c</sup>, Yi-Wen Fan <sup>d</sup>, Yan-Ping Jeffery Chi <sup>e</sup>

<sup>a</sup> MSN-5F4, School of Management, George Mason University, Fairfax, VA 22030, USA <sup>b</sup> Department of Information Management, The National Chin-Yi Institute of Technology, Taichung, Taiwan, ROC <sup>c</sup> Graduate Institute of Business Administration, National Chung-Hsing University, Taichung, Taiwan, ROC <sup>d</sup> Department of Information Management, National Central University, Jhongli City, Taiwan, ROC <sup>e</sup> Department of Management Information System, National Chengchi University, Taipei, Taiwan, ROC

Available online 8 September 2005

## Abstract

Distributed teams can carry out critical tasks with appropriate decision support technologies. The architecture and detailed design of a Web-based GDSS, called TeamSpirit, are discussed to address the challenges of building a Web-based GDSS. A series of empirical studies are reported to assess the effectiveness of TeamSpirit in supporting distributed group problem solving when in-person facilitation is not possible. Results indicate that giving creative problem solving training to TeamSpiri participants had positive impacts on team performance. Users who received brief TeamSpirit training were able to design and facilitate virtual meetings by themselves and achieved better team performance than control groups. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Virtual team; Distributed team; Group decision support systems; Creative problem solving; Web-based GDSS

## 1. Introduction

Companies are going global and this is especially true for companies participating in the global supply chain. To become agile enterprises, these companies are deploying virtual teams to carry out short- and long-term projects [37,38]. Virtual teams are geographically dispersed groups of people sharing a common goal to carry out interdependent tasks while working at different locations. They employ computer and communication technologies to communicate ideas and information, coordinate activities, as well as make decisions [10,34]. For virtual teams to work effectively, it is critical they use collaboration technologies to overcome the barriers of time and space [22,34].

As reviewed in Section 2, we found there are few Web-based group decision support systems (GDSS) tools that are designed specifically to support group decision making and alternative evaluations. Therefore, we have developed a Web-based GDSS, called

TeamSpirit, with the specific goal of supporting virtual teams’ decision-making processes. The browserbased interface allows team members to use Team-Spirit at any place and any time. The stateless HTTP protocol and the very limited local processing capability make the development of Web-based GDSS a major challenge. In Section 3 of this paper, we discuss the architecture and design of TeamSpirit to address these challenges. Section 4 presents detailed functionalities of a set of group tools in TeamSpirit.

Research that studied group decision support systems in the existing literature used mainly face-to-face facilitated GDSS developed using client–server technology running on local area networks; therefore, some of its results may not apply to distributed teams [52]. Tools that support distributed teams which have been empirically tested are mainly asynchronous computer conferencing systems (i.e., discussion forum software); these systems do not have explicit support for decision-making processes and often do not provide tools for alternative evaluation. When virtual teams use TeamSpirit without the physical presence of a facilitator, it is a challenge to ensure the system is used effectively. We have conducted a series of empirical studies to identify issues involved in using TeamSpirit in laboratory and field settings. Section 5 presents the results of these empirical studies. This paper concludes with a discussion of future research directions for enhancing TeamSpirit and for further studying its usage empirically.

## 2. Review of collaboration technologies, Web-based DSS, and Web-based GDSS

Within organizations, teams use technology to support their tasks. These tasks are often performed within a context of group problem-solving processes. Outside organizations, emerging collaboration technologies, global outsourcing trends, an overspecialized workforce, and the growing complexity and competition in the business world are major drivers for increasing the popularity and formation of virtual teams.

## 2.1. Collaboration technology

<sup>b</sup>Collaboration<sup>Q</sup> was defined as activities that involve people engaged in various business processes (e.g., marketing, engineering, research, and development) working together by sharing information and making decisions [32]. For example, to support better supply chain integration and customer services, it is important to involve not only employees but also suppliers and customers in certain decision-making processes. The group activities performed by teams while working together include communicating ideas, exchanging and sharing information, coordinating activities, discussing issues, and making decisions. Collaboration technologies have evolved from various origins; therefore, people use various terms to describe these technologies, such as groupware [30], inter-personal computing [8], group decision support systems (GDSS) [16,28], computer-supported cooperative work (CSCW) [23], computer-mediated communication systems (CMCS), and team technologies [2]. Each term has a specific focus; for example, GDSS has a strong decision-making orientation.

We can use a space/time grid (including same-time and same-place or different-time and different-place scenarios) to classify various collaboration technologies. Most studies conducted on technology support for teamwork examine technologies that use a synchronous mode of communication [20,52]. GDSS products, such as GroupSystems [13], are LANbased client–server applications often supporting same-time and same-place groups working in faceto-face settings. These products often require the use of facilitators to design and control the decision-making process. GDSS products focus on offering tools to support a group’s communication and decision-making activities. An audio/video conference system is a major example of a collaboration technology that supports groups working at the same time but at different places. This category of tools focuses on enhancing the virtual presence of meeting participants. The support for group processes and decision making are mostly missing from products in this category.

Asynchronous technologies, such as e-mail and discussion forums, are commonly used in the business world by distributed teams [31]. Asynchronous technologies tend to focus on supporting group information exchange and sharing [52]. However, these tools do not have strong support for group decision-making processes comparing to traditional GDSS. Many Webbased tools recently developed to support distributed teams try to bring structure to those group works by providing additional project management features [17,21,29,40,52]. eRoom is an example of products in this category. It has a project-oriented and document-centric approach to collaboration. Although eRoom includes a polling tool, it does not seem to be fully integrated with the other tools. The lack of integrated decision-making tools to support the decision-making process disqualifies such tools as Webbased GDSS.

## 2.2. Web-based GDSS

A Web-based Decision Support System (DSS) is a DSS built with Web technologies so that the DSS users access it with Web browsers via an Internet connection [6,46]. Web-based DSS applications developed by companies may be deployed on corporate intranets to support internal business processes or they can be integrated into public corporate Web sites to enhance services to trading partners [46]. These applications are very application-specific and support more structured tasks of certain business processes. Currently, Web-based DSS are mostly individual DSS systems [5,18]. Web-based GDSS products, on the other hand, provide a more generic approach to solving complex problems that are less structured.

Many first-generation GDSS products, such as GroupSystems, are client–server-based and only support group decision making over local area networks. The Web is a natural medium that supports collaboration, decision making, and communication among distributed teams. However, few Web-based GDSS products are available due to the difficulty in building user-friendly Web-based applications. One of the firstgeneration Web-based GDSS systems called TCBWorks was initially developed by Alan Dennis et al. while at the University of George in the mid-1990s [14]. TCBWorks was designed to allow team members to interact, discuss issues, and make decisions. It was developed in C language using CGI (Common Gateway Interface) and a database (i.e., MiniSQL). CGI is a standard for invoking server-side programs on a Web server. TCBWorks used the first-generation Web technologies for building Web-based GDSS. TCBWorks combined structured discussion and multicriteria decision making into one tool and did not explicitly support group decision-making processes. Development of

TCBWorks was discontinued in 1997 when it was licensed to Soft Bicycle Corporation and the product was renamed @nyWARE. However, Soft Bicycle Corporation no longer exists.

GroupSystems is a LAN-based client–server application for online collaboration [24]. An add-on product called GroupIntelligence is a Web reporting tool for GroupSystems products. Therefore, GroupSystems has been used exclusively in face-to-face decision room environments with networks of PCs running Windows. After many years in the making, a new Web-based GDSS product from Ventana called Cognito was developed and released in the fourth quarter of 2003. The Cognito platform comprises three components: (1) Cognito Task Server: a server application that runs on a MicrosoftR Windows 2000 server; (2) Cognito Portal: a Web interface for users to login to Cognito and launch the Cognito client to join a task; and (3) Cognito End User Client: a Java application that needs to be installed on a client-side machine to enable a user to participate in a group task. Cognito chooses to use a client application via HTTP/ HTTPS protocols because a Java client allows more flexible drag-and-drop for moving or copying information items [7]. However, such implementation may cause configuration management complexity related to software upgrades. This is why many Web-based DSS/GDSS systems use only Web browsers on the client side.

There are several commercially available Webbased GDSS products that contain decision-making tools. For example, Facilitate.com 8.0 provides support to the group decision-making process with tools such as Brainstorming, Categorizing, Voting, Action Planning, Surveying, and Online Chat Rooms [19]. It comes with its own server. WebIQ is a similar Webbased system [53]. It has an option to allow users to participate via email and also uses email to send out reminders to participants. WebIQ does not have a tool to support multicriteria decision making yet. There is a simple tool to transfer ideas from one activity to another. The product was build with Java servlet technology and DBC/ODBC compatible databases such as Oracle. The client can be an Internet Explorer or Netscape browser.

We are facing the challenges of supporting distributed teams because it is difficult for such teams to arrange face-to-face meetings or to meet at the same time virtually. Collaborative tools need to support both synchronous and asynchronous modes of communication. Therefore, Web technologies are used to build these tools rather than using client–server technologies. The need for group decision support for distributed teams and the lack of affordable Webbased GDSS systems have motivated us in developing our Web-based GDSS system so that we can conduct research on the decision and collaboration behaviors of geographically dispersed teams.

We believe that imposing appropriate structures on the processes and information content for asynchronous group activities is a critical factor in their effectiveness. Based on our experiences and research in GDSS and CPS (Creative Problem Solving) [33,50,52], TeamSpirit was developed as a Webbased group decision-making and problem-solving support system for distributed teams. The architecture and design of TeamSpirit is presented in the next section.

## 3. TeamSpirit: the architecture and design of a Web-based group problem-solving system

The World Wide Web has become an important medium for supporting the collaboration of distributed teams. Support for group communications in existing Web-based collaboration technologies is limited to discussion forums, e-mail, instant messaging, and Web-based audio/video conferencing tools. Team-Spirit is a Web-based GDSS designed to support group problem solving and decision making with generic problem-solving tools to be used by teams working anytime and anywhere. It is intended to be used by any team members to create their own online meetings supporting group problem-solving processes so that no professionally trained facilitators are required.

This research is grounded in design science [4,25,35] which integrated systems development efforts with empirical studies such as case studies, laboratory experiments, and field studies to justify and evaluate a newly developed system. It is also influenced by the <sup>b</sup>system development methodology<sup>Q</sup> which places systems development at the heart of a multi-methodological approach to IS research [39]. The design of a Web-based GDSS called TeamSpirit has been guided by CPS theories [41], prior GDSS research and development [13,15,16,20], and collaboration technologies in the marketplace. The emergence of virtual teams in the global outsourcing environment and the omnipresence of Internet and Web infrastructures are driving the development of Web-based GDSS [49,52]. Team-Spirit’s architecture design closely followed the CPS processes and tools commonly used in general problem solving and decision making developed over time.

This section presents the architecture design, the data model of the meeting repository, and the implementation environments of TeamSpirit. Later, Section 5 discusses a set of group tools available in Team-Spirit in terms of their functionality and user interface design.

## 3.1. The architecture design of TeamSpirit

The architecture of TeamSpirit is shown in Fig. 1. The design and structuring of group decision processes have been shown to be an important element if teams, particularly distributed ones, are to succeed. Therefore, an online <sup>b</sup>meeting<sup>Q</sup> is used metaphorically to represent a group problem-solving process for the specific problem at hand in TeamSpirit.

A meeting consists of a roster and an agenda. A roster contains a list of users who are invited by the facilitator to participate in the meeting. Every registered user can be a facilitator who can create meetings. The facilitator can assign the facilitator’s role to other users although it is not recommended that more than one facilitator is facilitating the same meeting at the same time. A meeting agenda consists of a list of agenda items representing group activities. Each group activity is supported by one of the group tools built into TeamSpirit. The agenda in TeamSpirit is not static, but is an executable agenda that meeting participants can use to invoke the appropriate participation version of a group tool. The facilitator needs to design a group decision-making or problem-solving process according to the problem or issue at hand and set up a meeting agenda accordingly.

TeamSpirit is designed to support the Creative Problem Solving (CPS) process. Meeting users are classified into two different roles: participants and facilitators. Any user can create a new meeting and become a facilitator of a meeting. A meeting facilitator can invite existing users who are registered with a TeamSpirit site to join a meeting as participants. A facilitator can also change the role of a user from a participant to a facilitator. If a meeting has more than one facilitator, they must coordinate their efforts so that they do not try to set up a meeting activity at the same time. While one TeamSpirit design objective is that any user can facilitate meetings, the skills required to be an effective facilitator take time to develop.

![](/api/attachments/R4P3UBKY/fulltext/images/345f04db75dc3e08068fe181062f8be70ccd3888d3b5a57094a349229d9ce574.jpg)  
Fig. 1. The architecture of TeamSpirit.

The major components of the TeamSpirit architecture are the following:

(1) User authentication and registration function: This function checks a user’s username and password to determine the meetings that the user can participate in or facilitate. It also allows new users to register themselves online, or they can be registered by a meeting facilitator.

(2) A group problem-solving process manager: This subsystem has two major functions: (a) Join meetings function: Meeting participants can use this function to view a list of meetings in which they are invited to participate. From a list of meetings, the user can choose a meeting to view its agenda as shown in Fig. 2. From the meeting agenda, the participant can click on an agenda item, to run the agenda execution program to invoke the participant version of a group tool that supports a group activity. The sequence of the agenda items is determined by the beginning time of each activity in the agenda. (b) Manage meetings function: A facilitator can use this function to set up a meeting. Meeting setup involves the following tasks: (1) Create a meeting agenda which consists of agenda items. (2) Invite existing users or create new users to participate in the meeting.

(3) Group toolkit: A set of tools was developed to support group activities that can be classified into three major categories: idea generation, idea consolidation, and idea evaluation tools. Each group tool has two versions (i.e., programs): (a) participation version: it is used by a meeting participant engaging in a meeting activity (i.e., an agenda item) supported by the tool; (b) facilitation version: it is used by a meeting facilitator to set up parameters or data items associated with a meeting activity.

(4) Meeting repository: A relational database is used to implement the meeting repository storing all the meeting related information including meeting setup information as well as ideas generated and evaluated by various group tools.

Join Meetings ... [ Meetings | Agenda | Roster | Log Off] Meeting Agenda Excution Tool Meeting Name: Strategic Planning and Improvement Meeting Description: Create and evaluate ideas that improve our standing among our competititors

<table><tr><td>Number</td><td>Agenda Name</td><td>Activity Type</td><td>Starting Time</td><td>Ending Time</td></tr><tr><td>1</td><td>Background information</td><td>Share information</td><td>2003/03/10 07:08</td><td>2003/12/12 07:08</td></tr><tr><td>2</td><td>SWOT Analysis</td><td>Multi-aspect brainstorming</td><td>2003/04/18 09:30</td><td>2003/12/18 10:30</td></tr><tr><td>3</td><td>Generate ideas to improve our competitiveness?</td><td>Brainstorm ideas</td><td>2003/04/18 10:27</td><td>2003/10/18 10:27</td></tr><tr><td>4</td><td>Rate these ideas</td><td>Rate alternatives</td><td>2003/04/18 10:29</td><td>2003/12/30 10:29</td></tr><tr><td>5</td><td>Evaluate ideas based on several criteria</td><td>Multicriteria evaluation</td><td>2003/04/18 10:32</td><td>2003/12/18 10:32</td></tr></table>

Fig. 2. A sample TeamSpirit meeting agenda.

3.2. The data model of the TeamSpirit meeting repository

The group tools that support participant interaction rely on the Meeting Repository for information sharing. The Meeting Repository is implemented in a relational database to store meeting-related information including meeting agendas, rosters, ideas generated, shared documents, and evaluations associated with alternatives submitted by meeting participants.

A partial data model of the Meeting Repository represented as an entity relationship diagram is depicted in Fig. 3. The Activity entity (i.e., table) stores information about agenda items; the group tool that supports an activity is specified via the relationship between Activity entity and ActivityType entity. ActivityType is the entity that stores information about all group tools as well as default settings for group activities supported by these tools. A new tool can be easily integrated into TeamSpirit without modifying the program coding by adding a new entry to the ActivityType entity.

![](/api/attachments/R4P3UBKY/fulltext/images/0727fc8544282c297524d5bcb650e5c40f13ef09271f38e06421c8e1d1d5eb37.jpg)  
Fig. 3. Partial data model of the TeamSpirit’s meeting repository.

Ideas or opinions created by meeting participants in several idea generation tools are stored as instances of the Item entity. Alternatives for idea evaluation activities are also stored as instances of the Item entity so that we can share common tools or software components for the facilitation version of several group tools. New tools can be developed in about 40 manhours on average because of the common data model shared by these group tools. Additional settings of an activity can be stored in the IssueType entity (e.g., criteria for a multicriteria evaluation activity or aspects of a multi-aspect brainstorming activity).

Evaluations by participants using various idea evaluation tools are stored in the Vote entity that uses item ID and user name combined together as its primary key. Evaluation results of the Multicriteria Evaluation tool are stored in a separate MCDMVote entity (not shown in the data model) using item ID, user name, and criteria ID combined as its primary key.

## 3.3. The development framework for TeamSpirit

The traditional DSS development framework proposed by Sprague includes user interface, database, and model base [47]. The development of TeamSpirit is consistent with the traditional DSS development framework. Special design considerations for Team-Spirit development based on the framework are discussed in the following:

(1) User Interface: The Web-based GDSS user interface consists of UI elements (i.e., Web pages) for end users, facilitators, and system administrators. In TeamSpirit, the traditional notion of a <sup>b</sup>public screen<sup>Q</sup> concept is implemented via <sup>b</sup>group view<sup>Q</sup> to allow users to easily switch from an individual workspace to a group view to examine ongoing group results. We use pop-up new browser windows to keep the active browser window open to simulate dialog boxes in the traditional Windows environment. HTML Frame is used in the Information Sharing tool for a similar purpose. A context-sensitive online help Web page is available to guide the user in using TeamSpirit.

(2) Database: A relational database is used to implement the Meeting Repository for Team-Spirit. Data contributed by individual users is created and stored with a user ID associated with it so that it is possible to recreate the private screen for the individual user and generate a group view based on the meeting roster. Meeting participants’ ideas and evaluations are all stored in the database so that they can be shared among participants. DBMS software provides the concurrency control of data accessed by facilitators and participants.

(3) Model Base: In TeamSpirit, various idea generation and evaluation tools can be viewed as general decision models. When selecting these tools for agenda items, facilitators need to set up additional information for different tools such as brainstorming triggering questions, evaluation alternatives, evaluating criteria, or aspects for multi-aspect brainstorming.

TeamSpirit is a Web-based GDSS that we have designed and implemented as an integrated, communications-driven DSS with various subsystems to enhance its functionalities [44,45]. It has communication-driven DSS features because it supports decisionmaking activities by connecting decision makers who might be separated in space or time via a set of group tools to share ideas and opinions in an integrated environment.

## 3.4. Implementation of TeamSpirit

TeamSpirit is developed in ASP.NET using Visual Basic.NET as the implementation language. The TeamSpirit system can be deployed on a computer running Microsoft Windows 2003 Server with Internet Information Server (IIS) and Microsoft.NET Framework SDK installed. Facilitators and participants only need to use Web browsers to manage meetings or participate in meetings. Limited client-side JavaScript code is used in the implementation of TeamSpirit to provide local data validation to reduce the unnecessary interaction between the Web client and the Team-Spirit programs running on the server.

Since we are conducting experiments for virtual teams with members from different nations, Team-Spirit was implemented as an internationalized software product sharing the same code base. All the string literals of various tools pages, including error messages, were externalized and stored in resource files. Currently, an English version and a <sup>b</sup>traditional Chinese<sup>Q</sup> version of TeamSpirit were built. The users responses to the Chinese version of the software seemed to be more positive than to the English version when we tested both versions in Taiwan.

Security may be a major concern of organizations that are considering adopting a Web-based GDSS such as TeamSpirit. If sensitive information is disclosed inappropriately, the disclosure could result in damage to employees and to organizations using TeamSpirit. Another concern is the International Traffic in Arms Regulation (ITAR). As an example, some government RFPs suggest that an ITAR license may be required before discussing a proposed project with foreign collaborators [1]. In TeamSpirit, we can build an extended user profile with up-to-date security clearance data and classify meetings according to various security levels so that a facilitator cannot add participants who do not have proper security clearance to a meeting. There are several ways to improve Web application security to secure TeamSpirit [36]. From the IT infrastructure perspective, one needs to secure the network operating system (i.e., Windows Server), the Web server (i.e., IIS), and the database that implemented the repository. The corporate network where TeamSpirit is deployed should have proper firewall systems installed. For applications requiring a secure environment, one can use Secure Sockets Layer (SSL) protocol to encrypt data transmitted over the network, particularly login information. From the application level security perspective, TeamSpirit uses a formbased authentication supported by the ASP.NET programming environment.

## 4. Group Toolkit: Group tools support group problem-solving activities

Currently, there are several group tools supporting various group techniques. These group tools are classified into three categories for creative problem-solving techniques that are often used in tandem: idea generation, idea consolidation, and idea evaluation [43]. A general CPS process includes the following six steps [48,50]: (1) exploring potential problems, (2) defining the underlying problem, (3) producing alternative solutions, (4) evaluating solutions, (5) planning the implementation of solutions, and (6) selling the solutions.

Idea generation techniques are used in steps 1, 3, and 5, while idea organization and evaluation techniques are applied in steps 2, 4, and 6. Each group tool has two versions: a participation version and a facilitation version. The participation version is used by meeting participants to enter or evaluate ideas. The facilitation version is used by facilitators to enter basic information about an activity, determine various options or parameters, import data from other activities, and organize data generated by the participants. A group problem solving process can be conceptualized as a sequence of group activities. Group problem-solving techniques such as brainstorming and various evaluation techniques are implemented as group tools to support these group activities.

A common set of navigation links is placed on top of each Web page or tool in TeamSpirit so that users can easily switch to the current meeting agenda, to a list of meetings in which they have been invited to participate, or to the current meeting roster. From the meeting roster tool, any participant can send email to an individual participant or all participants to encourage participation in an ongoing meeting.

## 4.1. Idea generation tools

There are several tools that allow participants to input and share their ideas, opinions, or information. These tools support divergent thinking in the creative problem solving process.

Currently, TeamSpirit implements four tools in this category:

(1) Brainstorming tool: A brainstorming activity can be set up by the meeting facilitator in three modes of anonymity: (1) Complete anonymity: The participant’s user name is not associated with the idea that was created by him. (2) Semi-anonymous: Only a meeting facilitator can view the name of the participant who created the idea. (3) No anonymity: All participants can see the user name of the creator of an idea. Newly generated ideas by a participant or others are highlighted to encourage the participants to pay attention to them.

(2) Multi-Aspect Brainstorming tool: This tool encourages lateral thinking, a creative thinking principle proposed by de Bono, who argues that problems should be studied from different perspectives before one tries to solve them [11]. The meeting facilitator needs to establish a set of categories beforehand. As shown in Fig. 4, a participant needs to select a category to be associated with an idea before the idea is submitted.

(3) Discussion Forum tool: A discussion forum encourages a conversational-style dialog among participants. Any participants can post a new topic and all participants can post messages to existing topics. Participants can use the Discussion Forum as a group writing tool to collect their thoughts to be used in drafting a report.

(4) Information Sharing tool: Users can upload local documents or URLs of Web pages to share information with team members and build mutual knowledge to help distributed teams work together effectively [10].

## 4.2. Idea consolidation tools

Using idea generation tools such as the Brainstorming tool, a group can generate many ideas in a short period of time. These ideas may contain similar or duplicated items that need to be merged. A search function is implemented so that ideas containing the same keywords can be retrieved for the facilitator to review, and then they can be merged or deleted. Some irrelevant items need to be removed, while some new last-minute items can be added. Idea consolidation in a distributed environment is mainly the facilitator’s responsibility. It can be a very challenging task for the facilitator. Currently, there is only one consolidation tool that the facilitator can use to import data from other activities. This tool allows meeting participants to view a list of items and to email their consolidation suggestions to the facilitator.

When the involvement of all meeting participants is desirable during the consolidation process in a distributed environment, the use of the consolidation tool is recommended to support the convergent thinking process. A meeting facilitator can easily import data from one activity to another activity within the same meeting or across meetings. All the idea evaluation tools in TeamSpirit have an idea organization function embedded in them so that facilitators may not need to set up an explicit idea consolidation activity in the group decision-making process.

![](/api/attachments/R4P3UBKY/fulltext/images/dca1ce86a530f21c56686ff8fd58da3aaeb27270ba5af21fdd4d5f94f53471f7.jpg)  
Fig. 4. TeamSpirit multi-aspect brainstorming tool.

## 4.3. Idea evaluation tools

There are currently four evaluation tools that have been developed in TeamSpirit, including: Rating, Ranking, Selection, and Multicriteria Evaluation tools. Participants can submit their evaluations or votes. They can also view group results that include group averages and standard deviations. A large standard deviation may indicate a lack of consensus on an alternative or issue. The facilitator can bring issues with large standard deviations to participants’ attention for further discussions. The participants can recast their votes to see whether the team can come to a consensus.

(1) Rating tool: The rating tool allows participants to evaluate a set of alternatives based on a 1 to X scale, with the default value for X being 10. The rating tool can be used to evaluate quickly a long list of alternatives and cut them down to a small set of alternatives. Group evaluation results, shown in Fig. 5, contain group average and standard deviation that can be viewed by participants.

(2) Ranking tool: The ranking tool allows participants to evaluate a set of alternatives by rank ordering these items. Participants can select an alternative and move it up or down in a list of alternatives to change its ranking. Rank ordering can be used to prevent potential manipulation of voting results.

(3) Selection tool: The selection tool allows participants to evaluate a set of alternatives by voting

Yes/No on each alternative. The greater the number of <sup>b</sup>Yes<sup>Q</sup> votes on an alternative means the alternative is more favorable.

(4) Multicriteria Evaluation tool: The multicriteria evaluation tool allows participants to use a set of weighted criteria to evaluate a set of alternatives. The criteria names should imply the direction of preference. For example, instead of <sup>b</sup>cost<sup>Q</sup>, <sup>b</sup>lower cost<sup>Q</sup> should be used; instead of <sup>b</sup>impact<sup>Q</sup>, <sup>b</sup>high impact<sup>Q</sup> is better.

In a group decision-making process, outputs from a group activity are often used as inputs to another group activity. TeamSpirit has a powerful, flexible, and easy-to-use import and export utility that allows the facilitator to transfer information items generated among various meeting activities, thereby supporting continuity in information sharing and usage. Meeting facilitators can transfer data easily from one activity to another activity of the same meeting without explicitly exporting and importing data. A facilitator can export data from an activity so that they can be imported into another activity in a different meeting. The facilitator can export all items association with an activity by selecting a set of items to export manually, or by using a context-sensitive export filter to export a subset of existing items of an activity. An import filter can be defined to import a selected set of items from another activity in the same meeting. A set of criteria based on the activity type of the activity from which the associated data were generated can be set via a context-sensitive import filter. For instance, you can easily import items generated from a brainstorming activity to a rating activity. After the rating activity, one can import the top-rated items (alternatives) with

## Rating Tool: Group Rating Result

<table><tr><td colspan="3">26 participants in total. 20 have voted!View Detailed Result Close this Window</td></tr><tr><td>Group Average</td><td>Standard Deviation</td><td>Alternative</td></tr><tr><td>6.60</td><td>3.72</td><td>Need $ from business community to fuel growth.</td></tr><tr><td>5.95</td><td>3.98</td><td>Increase number of Som faculty authored articles in quality journals</td></tr><tr><td>5.90</td><td>3.48</td><td>More alliance of high-tech companies.</td></tr><tr><td>5.10</td><td>3.19</td><td>Have Ph.D. program.</td></tr><tr><td>5.00</td><td>3.78</td><td>Increase research productivity</td></tr></table>

Fig. 5. View group result statistics.

a group rating average that is greater or equal to a specific number (e.g., 6) into a multicriteria evaluation activity. The multicriteria evaluation activity can import and reuse the criteria from another multicriteria evaluation activity.

A meeting’s agenda can also be exported as an XML-formatted file so that it can be used later as a meeting template to create a new meeting with a similar problem solving process. The facilitator can import a meeting template XML file to set up a new meeting quickly. The template preserves a welldesigned problem-solving process created by an experienced facilitator and it can be used by less experienced facilitators to share facilitation knowledge in an organization. These import and export facilities in TeamSpirit improve the productivity of a facilitator who needs to manage many meetings.

## 5. Empirical studies of TeamSpirit

Dennis et al. [15] conducted a meta-analysis of GSS-related research and proposed a Fit-Appropriation Model to explain the contradictory of the research findings about GDSS effectiveness. The Fit-Appropriation Model argues that GDSS performance is affected by two factors. The first factor is the fit between the task and the GDSS structures and the second factor is the appropriation support such as the training and facilitation that the group receives. Another research study found that with proper support of synchronous collaboration technologies, distributed teams can be at least as productive as groups who work in face-to-face meetings [3]. We have conducted a series of empirical studies to evaluate TeamSpirit usage in different scenarios to gain insights into how the system can be used effectively. Special attention has been paid to factors such as training and task-type identified in the Fit-Appropriation Model. Since TeamSpirit is a Web-based system, the separation by time and space of virtual teams presented a major challenge to the effective use of the system. We were interested in studying factors affecting team performance under different time and place configurations when TeamSpirit is used. This is an important aspect of Web-based GDSS which is not incorporated in the Fit-Appropriation Model. Four clusters of empirical studies are reported in this section.

## 5.1. Empirical study: Idea generation task

One of the most critical steps in the creative problem-solving process is the idea generation activity either in identifying problems or in generating creative solutions [50]. TeamSpirit was used in various field studies and laboratory experiments to study the effects of system usage and CPS training on the creative thinking ability of the users as well as on the group decision process and outcomes.

The Torrance Test which takes two forms was adapted in this study: verbal and figural. The figural test requires that students respond by incorporating simple shapes, like circles or abstract line drawings, into more complete pictures. Two alternative figural forms for creativity measurement, the circle test and the line test, are used for pre-test and post-test [48]. The test is taken by the subjects individually and is graded individually as well. Subjects’ responses can be evaluated by four criteria [50,51]. (1) Originality: This is measured by the uniqueness of an idea compared to past responses. (2) Fluency: This is determined by the quantity of ideas generated in a certain period of time. (3) Flexibility: This is measured by the number of conceptual categories into which the generated ideas can be classified. (4) Elaboration: This is the level of detail that the subject goes into when describing an idea. Elaboration is not used in our measurement of creativity in this study. Since creativity is considered to be the most important factor affecting the quality of the problem-solving process, this study focused on the effect of using TeamSpirit on group creativity as well as the effects of training on individual creativity.

The experimental design consisted of two experimental groups: Group A and B. Students were grouped in teams of four for all the group tasks in the experiment. Both groups were given CPS training. Only Group A was given basic training on how to use TeamSpirit as a participant. Teams in Group A were asked to work on a problem in 1 week using Team-Spirit at different times and in different places. Teams in Group B were asked to work on a problem in 1 week using traditional paper and pencil. The control group was not given any CPS training and was not asked to work on the week-long exercise. All three groups were given a pre-test and a post-test (1 week after the pre-test) using Torrance Tests. Torrance’s line test was used for the pre-test and the circle test was used for the post-test.

Table 1  
Creativity measures for experimental groups and the control group

<table><tr><td rowspan="2">Group</td><td rowspan="2">Score</td><td colspan="2">Pre-test</td><td colspan="2">Post-test</td><td rowspan="2">t-test</td><td rowspan="2">df</td></tr><tr><td> $\bar{X}$ </td><td>S.D.</td><td> $\bar{X}$ </td><td>S.D.</td></tr><tr><td rowspan="4">Experimental group A</td><td>Fluency</td><td>13.31</td><td>5.03</td><td>17.31</td><td>6.76</td><td>-3.93***</td><td>38</td></tr><tr><td>Flexibility</td><td>7.9</td><td>2.41</td><td>10.92</td><td>3.59</td><td>-6.73***</td><td>38</td></tr><tr><td>Originality</td><td>5.51</td><td>3.55</td><td>7.67</td><td>4.01</td><td>-3.17**</td><td>38</td></tr><tr><td>Total creativity</td><td>25.90</td><td>9.84</td><td>35.90</td><td>13.49</td><td>-5.73***</td><td>38</td></tr><tr><td rowspan="4">Experimental group B</td><td>Fluency</td><td>15.27</td><td>5.30</td><td>15.42</td><td>4.97</td><td>-0.18</td><td>25</td></tr><tr><td>Flexibility</td><td>8.88</td><td>3.19</td><td>10.35</td><td>3.03</td><td>-2.61*</td><td>25</td></tr><tr><td>Originality</td><td>6.81</td><td>4.25</td><td>6.23</td><td>3.78</td><td>0.86</td><td>25</td></tr><tr><td>Total creativity</td><td>30.96</td><td>12.11</td><td>32</td><td>10.83</td><td>-0.59</td><td>25</td></tr><tr><td rowspan="4">Control group</td><td>Fluency</td><td>15.39</td><td>5.58</td><td>14.51</td><td>4.71</td><td>1.26</td><td>40</td></tr><tr><td>Flexibility</td><td>9.15</td><td>3.15</td><td>9.80</td><td>2.99</td><td>-1.75</td><td>40</td></tr><tr><td>Originality</td><td>6.02</td><td>3.09</td><td>5.44</td><td>3.05</td><td>1.47</td><td>40</td></tr><tr><td>Total creativity</td><td>31.54</td><td>11.29</td><td>30.05</td><td>10.18</td><td>1.12</td><td>40</td></tr></table>

Based on an analysis of the test results listed in Table 1, one can make the following observations. One week after the training, the fluency, flexibility, and originality of Group A increased significantly; in Group B, only fluency and flexibility increased while originality decreased a little. The control group’s fluency increased an insignificant amount, while originality and flexibility decreased an insignificant quantity. The total creativity score increased significantly for both Groups A and B who had received CPS training, while the control group’s total score remained relatively unchanged.

The team creativity performance measured by the fluency (i.e., the average number of ideas generated by team members) for Groups A and B are listed in Table 2. Only fluency is used in measuring creativity due to the difficulties in judging group results regarding originality and flexibility in training exercises and the group task used in experiments. There was not a significant difference for Groups A and B during the brainstorming exercise and CPS exercise. After the training, a problem-solving task is given to both groups. Teams in Group A used TeamSpirit’s brainstorming tool to generate ideas while teams in Group B (traditional) used paper and pencils.

There was no significant difference in terms of the amount of ideas generated by Group A (5.75) and Group B (5.05), measured by the average number of ideas generated by individual subjects within a group. Subjects were asked to continue working on the same task for 1 week. Group A’s teams still used TeamSpirit at different times and places while Group B’s teams used pencil and paper and worked independently. The score for Group A was 12.67 and for Group B was 5.92. There was a significant increase in the average amount of ideas generated by individuals in Group A.

Many prior research studies found that distributed teams performed less effectively than groups meeting face to face [26,27,52]. However, many of these recent studies are limited in two important aspects. First, they used ad hoc groups or did not give their groups sufficient time to adapt to one another or the communication medium. Recent evidence suggests that when virtual teams are given sufficient time to develop strong intra-group relationships and to adapt to the communication medium, they may communicate as effectively as face-to-face groups [9]. A second limitation is that the predominance of studies used synchronous (same time) rather than asynchronous (different time) technologies. Asynchronous technologies, which include e-mails and discussion forums, are probably more common in the business world than synchronous technologies [31].

Table 2  
Creativity performance comparison

<table><tr><td rowspan="2"></td><td colspan="2">Brainstorming training</td><td colspan="2">CPS training (human cloning)</td><td colspan="3">Traditional and TeamSpirit group works ideas generated</td></tr><tr><td>Naming a coffee shop</td><td>Paper clipper usage</td><td>Identify sub-problems</td><td>Generate solutions</td><td>Face-to-face (10 min)</td><td>Average individual ideas generated</td><td>Number of ideas increased</td></tr><tr><td>A (TeamSpirit)</td><td>2.42</td><td>3.69</td><td>5.06</td><td>2.04</td><td> $5.75^a$ </td><td> $12.67^a$ </td><td>△6.92</td></tr><tr><td>B (traditional)</td><td>2.84</td><td>4.74</td><td>4.21</td><td>1.42</td><td>5.05</td><td>5.92</td><td>△0.87</td></tr></table>

## 5.2. Empirical studies: creating business plans

The second category includes a laboratory experiment and a field study involving undergraduate students. In the lab experiment at the first stage, the CPS training had significant impact on team performance whether teams used TeamSpirit or not. Teams that received CPS training and had access to Team-Spirit performed slightly better than teams that only received CPS training. In the field study at the second stage, we compared two groups; both received CPS training and each group had 10 teams. Each team was asked to write a business plan in 1 month for a start-up company, covering topics such as company name, products to be sold, and the market niche. The experimental group was given a 1-h training program in using the meeting management function in TeamSpirit to set up new meetings. The group was encouraged to use Team-Spirit; however, using TeamSpirit was not required. In the experimental group, 7 out of 10 teams used TeamSpirit in supporting their business plan creation tasks. Teams that used TeamSpirit set up one to six meetings, and many meetings involved a brainstorming activity followed by a rating activity. Only one team in the experimental group failed to submit its final report, while 7 of the 10 teams in the control group did not submit their report. Based on the reports submitted, the overall quality of the experimental group’s reports as judged by four expert coders was better than those produced by the control group. Within the experimental group, teams that used TeamSpirit for more than one meeting and had more than 50% member participation received better final grades for their projects. The increase in performance may be due to the opportunities to use additional channels to engage team members in discussions. Teams within the experimental group also used face-to-face meetings, particularly in the final stage of their projects when they needed to put their reports together.

Preliminary result shows that even ad hoc distributed teams can be effective if proper collaborative technologies such as TeamSpirit were used. The effect of creativity training has statistical significance in improving individual creativity that, in turn, may improve the effectiveness of using TeamSpirit. The importance of CPS training to the effective use of collaboration technologies is consistent with earlier results from ongoing field studies.

## 5.3. Empirical study: implementation of TeamSpirit in two companies

This field study was based on implementations of TeamSpirit in two small- to medium-sized enterprises (SME). Both firms had 20–30 employees who went through a 2-h training program in using TeamSpirit. The difference between the two firms was that only employees from Firm A received a 6-h CPS training program prior to TeamSpirit training while Firm B’s employees did not receive any CPS training. The result based on data gathered from these two firms indicated that in the initial face-toface TeamSpirit training, in which both an exercise and a real problem were used for online meetings, both firms’ teams performed well. This is probably because these meetings were all facilitated by a professional facilitator in a face-to-face setting. After initial technical training on TeamSpirit, virtual meetings conducted by Firm A’s teams generated more and better ideas than meetings conducted by teams from Firm B. Participants from Firm B often used the electronic brainstorming tool in TeamSpirit as a chat room and strayed from the topic under discussion or injected emotional statements in their discussions; therefore, the ideas that were generated were less useful. The effect of CPS training is more significant in virtual meetings when in-person facilitation is not possible.

This field study of TeamSpirit implementation in two companies provides a better idea of how Webbased GDSS should be introduced into organizations. Based on this study, when companies plan to implement Web-based GDSS, they should provide employees with creativity and problem-solving training which has been shown to have a positive long-term effect on virtual meetings. Support from top management and proper incentives for employees to contribute fully via these online collaboration tools are two major factors affecting the implementation success of Web-based GDSS. Some preliminary evidence indicates that trust among team members may be another major factor that affects the performance of virtual teams. Paul and McDaniel [42], in their study of virtual teams from 10 operational telemedicine projects using health care delivery systems, found that there was a positive association between integrated interpersonal trust and virtual collaborative relationship performance. Therefore, overcoming the lack of in-person facilitation support to virtual teams is a major challenge for using online collaboration tools [12].

## 5.4. Empirical study: supporting long-term projects and complicated tasks

TeamSpirit has been used for a semester-long project between students of two MBA courses from two universities, one in Taiwan and one in the United States. There were nine teams in total, averaging six students per team, two from the U.S. and four from Taiwan. Participation in a joint project to create a global outsourcing plan was a course requirement. Hands-on sessions were given to students so they could learn how to use TeamSpirit as participants. The online meeting was designed and geared towards completion of the final report on a global outsourcing initiative. Each online meeting had eight agenda items and five different types of group tools (i.e., Information Sharing, Discussion Forum, Brainstorming, Rating, and Multicriteria Evaluation) were used. All nine teams had the identical meeting agenda. These meetings were facilitated by an expert to ensure consistency among teams.

Participants used TeamSpirit in this study over a longer period of time (about 10 weeks). They all followed the same meeting agenda. The meeting agenda from this outsourcing project involved eight activities and is a good example of how TeamSpirit can be used to support complex virtual team tasks. Early analysis of data collected from subjects indicated that they found TeamSpirit to be an effective tool compared to email and telephone in group problem solving and decision making. From a survey conducted after project completion, students tended to agree that using TeamSpirit was very helpful in improving the group problem-solving process and in completing their joint projects.

## 6. Conclusions

So far, TeamSpirit has been used for more than 100 online meetings with group size between 3 and 40. Several empirical studies were conducted to validate the system’s usefulness. These studies provided valuable feedback in improving system functionality and user-interface design. The development of TeamSpirit allows us to collect research data and to add features quickly to support a new line of inquiry. Systems development research is an evolving process. The TeamSpirit architecture, with its shared repository as well as reusable components implemented in User Controls in ASP.NET, makes the development of new group tools relatively easy. Therefore, group tools can be easily integrated into the TeamSpirit environment. One enhancement to TeamSpirit is to allow users to add comments to their ideas and to provide rationales behind their votes. Another new feature will be to allow a facilitator to incorporate graphics as part of a brainstorming triggering question, thereby allowing TeamSpirit to be used in collaborative design.

There is a limited amount of research about collaboration technologies and the group decision-making processes of virtual teams [20]. This article briefly reports a series of empirical studies to validate Team-Spirit’s functionality according to the design science research paradigm. The studies reported here showed some significant improvement of group decision outcomes when TeamSpirit was used and when CPS training was provided. It confirmed the belief that this process-oriented approach based on CPS is an effective way to support virtual teams. A Web-based GDSS such as TeamSpirit can be useful. However, more research needs to be conducted to study how additional factors, such as audio/video conferencing, multimedia contents, and facilitation styles, may affect the use of Web-based GDSS on virtual team performance.

## Acknowledgement

This research was supported and sponsored in part by National Sciences Council, Taiwan, ROC, Grant NSC92-2416-H-005-020.

## References

[1] AAU, ITAR Issue Background Information, Association of American Universities, 2002 (March), http://www.aau.edu sheets/ITAR.html.

[2] M. Alavi, P.G.W. Keen, Business teams in an information age, The Information Society 6 (4) (1989) 179– 195.

[3] G. Baker, The effects of synchronous collaborative technologies on decision making; A study of virtual teams, Information Resources Management Journal 15 (4) (2002) 79–94.

[4] N.L. Ballt/Design science II: the impact of design science on e-commerce research, Communications of the AIS 7 (Article 2) (2001).

[5] P. Bharati, A. Chaudhury, An empirical investigation of decision-making satisfaction in Web-based decision support systems, Decision Support Systems 37 (2) (2004 (May)) 187–197.

[6] H. Bhargava, D.J. Power, Decision support systems and Web technologies: a status report, Proceedings of the 2001 Americas Conference on Information Systems, Boston, MA, 2001 (August 3–5), pp. 229 – 235 (http://dssresources.com/papers/ dsstrackoverview.pdf).

[7] R.O. Briggs, Built for speed: introducing GroupSystems Cognito, Collaboration 2003: A Conference on Collaborative Technology Processes and Tools, Annapolis, MD2003 (Oct. 20–12).

[8] Byte, After the Revolution: A Sampling of Forecasts, 1990 (February, 30).

[9] L. Chidambaram, Relational development in computer-supported groups, MIS Quarterly 20 (2) (1996) 143–163.

[10] C.D. Cramton, The mutual knowledge problem and its consequences for dispersed collaboration, Organization Science 12 (3) (2001) 346–371.

[11] E. De Bono, Lateral Thinking for Management, McGraw-Hill, New York, NY, 1971.

[12] A.R. Dennis, B.A. Reinicke, BETA versus VHS and the acceptance of electronic brainstorming technology, MIS Quarterly 28 (1) (2004) 1 – 20.

[13] A.R. Dennis, J.F. George, L.M. Jessup, J.F. Nunamaker, D.R. Vogel, Information technology to support electronic meetings, MIS Quarterly 12 (4) (1988) 591– 624.

[14] A.R. Dennis, F. Quek, S.K. Pootheri, Using the Internet to implement support for distributed decision making, in: P. Humphreys, L. Bannon, A. McCosh, P. Migliarese, J-C. Pomerol (Eds.), Implementing Systems for Supporting Management Decisions: Concepts, Methods and Experiences, Chapman & Hall, London, 1996, pp. 139– 159.

[15] A.R. Dennis, B.H. Wixom, R.J. Vandenberg, Understanding fit and appropriation effects in group support systems via meta analysis, MIS Quarterly 25 (2) (2001) 167–193.

[16] G. DeSanctis, B. Gallupe, A foundation for the study of group decision support systems, Management Science 33 (5) (1987) 589 – 609.

[17] Documentum, eRoom Collaboration, http://www.documentum. com/solutions/collaboration/index.htm.

[18] J. Dong, H.S. Du, S. Wang, K. Chen, X. Deng, A framework of Web-based decision support systems for portfolio selection with OLAP and PVM, Decision Support Systems 37 (3) (2004 (June)) 367– 376.

[19] Facilitator.Com, Introduction to Facilitate.Com 8.0, (2004 July 1) http://www.facilitate.com/introduction.html.

[20] J. Fjermestad, S.T. Hiltz, An assessment of group support systems experimental research: methodology and results, Journal of Management Information Systems 15 (3) (1998) 7 – 148.

[21] GMD FIT, What is BSCW?, http://bscw.gmd.de/.

[22] S.L. Goldman, R.N. Nagel, K. Preiss, Agile Competitors and Virtual Organizations Strategies for Enriching the Customer, Van Nostrand Reinhold, New York, NY, 1995.

[23] I. Greif, Overview, in: I. Greif (Ed.), Computer-Supported Cooperative Work: A Book of Reading, Morgan Kaufmann Publishers, Inc., San Mateo, CA, 1988, pp. 5 –12.

[24] GroupSystems.Com, GroupSystems products, (2004 July 1) http://www.groupsystems.com/products/index.htm.

[25] A.R. Hevner, S.T. March, J. Park, S. Ram, Design science in IS research, MIS Quarterly 28 (1) (2004 (March)) 75 – 106.

[26] R.T. Hightower, L. Sayeed, The impact of computer mediated communication systems on biased group discussion, Computers in Human Behavior 11 (1) (1995) 33– 44.

[27] R.T. Hightower, L. Sayeed, Effects of communication mode and pre-discussion information distribution characteristics on information exchange in groups, Information System Research 7 (4) (1996) 451– 465.

[28] G. Huber, Issues in the design of group decision support systems, MIS Quarterly 8 (3) (1984) 195– 204.

[29] C.Y. Jang, C. Steinfield, B. Pfaff, Supporting awareness among virtual teams in a web-based collaborative system: the teamSCOPE system, ACM SIGGROUP Bulletin 21 (3) (2000 (December)) 28–34.

[30] R. Johansen, Groupware: Computer Support for Business Teams, The Free Press, New York, NY, 1988.

[31] S.T. Kinney, R.R. Panko, Project teams: profiles and member perceptions-implications for group support system research and products, Proceedings of the Twenty-Ninth Hawaii International Conference on System Sciences, 1996, pp. 128– 137.

[32] M. Levitt, R.P. Mahowald, There should be more to collaboration than email, IDC White Paper, IDC, 2002.

[33] I. Liou, M. Chen, Using group support systems and joint application development for requirements specification, Journal of Management Information Systems 10 (3) (1993–1994 (Winter)) 25 – 41.

[34] H.C. Lucas, J. Baroudi, The role of information technology in organization design, Journal of Management Information Systems 10 (4) (1994) 9– 23.

[35] S.T. March, G.F. Smith, Design and natural science research on information technology, Decision Support System 15 (4) (1995) 251–266.

[36] J.D. Meier, et al., Improving Web Application Security: Threats and Countermeasures, Microsoft Press, Redmond, WA, 2003.

[37] S.A. Morris, Impact of user satisfaction and trust on virtual team member, Information Resources Management Journal 15 (2) (2002) 22– 31.

[38] A. Mowshowitz, Virtual organization, Communications of the ACM 40 (9) (1997) 30– 37.

[39] J.F. Nunamaker, M. Chen, T.D. Purdin, Systems development in information systems research, Journal of Management Information Systems 7 (3) (1991) 89– 106.

[40] R. Ocker, J. Fjermestad, S.R. Hiltz, K. Johnson, Effects of four modes of group communication on the outcomes of software requirements determination, Journal of Management Information Systems 15 (1) (1998) 99–118.

[41] S.J. Parnes, The Creative studies project, in: S.G. Isaksen (Ed.), Frontiers of Creativity Research: Beyond the Basics, Bearly Limited, Buffalo, NY, 1987, pp. 156– 188.

[42] D.L. Paul, R.R. McDaniel, Effect of interpersonal trust on virtual collaborative relationship performance, MIS Quarterly 28 (2) (2004) 183– 227.

[43] P.E. Plsek, Models for the creative process, Working Paper, 2004 (June 1), http://www.directedcreativity.com/pages/ WPModels.html.

[44] D.J. Power, Decision Support Systems: Concepts and Resources for Managers, Quorum Books, Westport, CT, 2002.

[45] D.J. Power, Specifying an expanded framework for classifying and describing decision support systems, Communications of AIS 13 (Article 13) (2004 (February)).

[46] D.J. Power, S. Kaparthi, Building Web-based decision support systems, Studies in Informatics and Control 11 (4) (2002) 291– 302.

[47] R.H. Sprague, A framework for the development of decision support systems, MIS Quarterly 4 (4) (1980 (December)) 1 – 26.

[48] E.P. Torrance, The Torrance Tests of Creative Thinking, Scholastic Testing Press, Bensenville, IL, 1974.

[49] D.R. Vogel, R.M. Davison, R.H. Shroff, Sociocultural learning: A perspective on global education, Communications of AIS 7 (Article 9) (2001 (August)).

[50] C.W. Wang, R.Y. Horng, The effects of creative problem solving training on creativity, cognitive type and R&D performance, R&D Management 32 (1) (2002 (January)) 35–45.

[51] C.W. Wang, J.J. Wu, R.Y. Horng, Creative thinking ability, cognitive and R&D performance, R&D Management 29 (3) (1999) 247–254.

[52] M.E. Warkentin, L. Sayeed, R. Hightower, Virtual teams versus face-to-face teams: an exploratory study of a webbased conference system, Decision Sciences 28 (4) (1997) 975– 996.

[53] WebIQ LLC., WebIQ 2.0: Session Leader’s Guide, WebIQ LLC, Silver Spring, MD, 2003.

![](/api/attachments/R4P3UBKY/fulltext/images/bab54dcaa0c5006ccdc353250a93dc3ed2feae28128faa0a1913eaf989c22be2.jpg)

Minder Chen is an Associate Professor of Management Information Systems and Decision Science in the School of Management at George Mason University and was the Director of Technology Program. He received a BS in Electrical Engineering from National Taiwan University in 1979, an MBA from National Chiao Tung University in 1983, and a PhD in Management Information Systems from the University of Arizona in 1988. His primary research

interests are Web services, electronic commerce, knowledge management, collaboration technologies, and virtual teams. He has published papers in International Journal of E-Business, Journal of Management Information Systems, Database, Journal of Organizational Computing, Expert Systems with Applications, IEEE Transactions on Knowledge and Data Engineering, International Journal of Human Computer Studies, Journal of Electronic Commerce Research, Journal of Computer Information Systems, IEEE Transactions on Systems, Man, and Cybernetics, Journal of Small Group Research, and IEEE Software. He was the program co-chair of the Third Workshop of E-Business, December 2004.

![](/api/attachments/R4P3UBKY/fulltext/images/35862bfd62801bf485bf86f4dcce860ddc6208b5230776fa94c520bc75ad9602.jpg)  
Yiching Liou is currently a PhD candidate in the Information Management Department of National Central University. She received a Master’s Degree in Management Information Systems from the University of Arizona in 1988. Her research interests include electronic commerce, collaboration technologies and virtual teams, and business reengineering.

![](/api/attachments/R4P3UBKY/fulltext/images/e1accae4b4e5bc58afae13051a028f520ac8af4454471728564257e4a7f47db3.jpg)

Ching-Wen Wang is a Professor of Business Management in the National Chung Shing University. She received an MBA from National Chiao Tung University in 1983 and a PhD from National Chiao Tung University in 1992. Her research interests are creativity and organization behavior. She has published papers in R&D Management about R&D performance and creativity.

![](/api/attachments/R4P3UBKY/fulltext/images/bf8773e1284673ffedc962b749faf8d63948a4ac30b1bb350d620e13be0a2be8.jpg)

Yi-Wen Fan is an associate professor in the Information Management department of National Central University. She received her PhD in Management Information Systems from the University of Iowa in 1991. Her research interests include management and application of information systems, ecommerce applications, and decision support systems.

![](/api/attachments/R4P3UBKY/fulltext/images/8b2ac4ce6d6efdc53ee19ca809c3faf0f4a86d2cf0d7e7a0c722d77ebdda8d8f.jpg)  
Jeffery Y. Chi is an associate professor in the MIS department of National Cheng-Chi University. He received his PhD in Management Information Systems from the University of Maryland in 1990. His research interests include business process reengineering, management information systems, enterprise resource planning, data base, and e-marketing.
