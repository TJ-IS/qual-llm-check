---
otero_id: 20997
otero_key: "DJ5Z6S9M"
title: "Meeting others—supporting situation awareness on the WWW"
authors: "Yu You; Samuli Pekkola"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(01)00101-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com<sup>r</sup>locate<sup>r</sup>dsw

# Meeting others—supporting situation awareness on the WWW

Yu You<sup>)</sup>, Samuli Pekkola

Department of Computer Science and Information Systems, UniÕersity of JyÕaskyla, P.O. Box 35, 40351 Jy ¨ ¨ ¨ ¨Õaskyla, Finland

## Abstract

World Wide Web WWW techniques provide a simple interface, which is accessible almost everywhere. The WWWŽ . supports document sharing and information retrieval, but has no tools for direct user interaction, simply because the mechanisms to support user awareness are missing. The aim of this paper is twofold. First, we present general concepts of situation awareness, which concerns the user interaction on the WWW platform, and a theoretical framework, which is used in examining existing awareness support systems. Second, we provide an analysis of PeopleAwarenessEngine, which supports situation awareness and enables user communication and collaboration on the WWW. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: WWW; Situation awareness; User interaction; CSCW

## 1. Introduction

Perceiving, recognizing, and understanding the activities of others are the basic requirements for group work and more generally for human communication and interaction. Adequate human behaviour in group work requires that the group members are aware of the overall situation, people and objects involved. In real life, group members can see each other and the actions occurring within a group, as well as actions performed around the group at all times, i.e. the participants are aware of several activities which may, or may not, be related to the group or its tasks. Also, the members of the group can easily share documents and other artefacts needed in a session.

Unfortunately, the situation is not the same for technical platforms such as those on the World Wide Web WWW . Since the WWW is rooted strongly inŽ . information sharing and not in group work or its supporting functions, many problems exist when using the WWW as a group communication environment. For example, an individual WWW surfer cannot participate to a session where people negotiate and share documents online, simply because people are not presented. WWW protocols, e.g. HTTP 3 ,<sup>w</sup> <sup>x</sup> hide the complexity of the distributed and heterogeneous environment but simultaneously this encapsulation generates difficulties in representing people on the WWW.

Lately, collaborative tools and services such as email, mailing lists, newsgroups, and electronic libraries have been either adapted to the Internet, or developed as a new medium. This has motivated many researchers to carry out some studies to discover the essential features for effective group work on the WWW 4,5,8,9,15 . In principle, these studies <sup>w</sup> <sup>x</sup> show that the WWW is lacking many features to support human communication, and consequently, group work. The reasons for this kind of failure are clear: the co-operating groups on the WWW are large, transient and unstable, their membership is non-determinable, and self-evident participants are physically distributed. All are concepts noted by Schmidt and Bannon 35 while writing about groups<sup>w</sup> <sup>x</sup> in other contexts. From the discussions above, we highlight one very specific and important area: awareness—awareness of people, awareness of group memberships and further members’ identities, and the awareness of activities taking place within and around the group.

Awareness of others, and multiple communication modes with relevant others, have a crucial role in ordinary work processes. For example, Heath et al.’s <sup>w</sup> <sup>x</sup> 18 study of London Underground’s control rooms introduced the idea of ‘peripheral’ or ‘out of the corner of the eye’ awareness visual or audio , which,Ž . as they claimed, is essential for any co-ordinated activity. Other researchers in different work situations have reported similar results, e.g. 17,25,31,36 .<sup>w</sup> <sup>x</sup> All these examples point out the same requirement: the ability to be aware of other people, firstly, when co-operating with them, but, secondly, also when accomplishing individual work, because others’ activities may also affect the person’s own work.

In this paper, we will first present a framework in which the awareness of others is studied from several viewpoints. In the sequel, this framework is used to analyse existing applications. Finally, we will present and analyse our own system, PeopleAware-<sup>1</sup> nessEngine PAW , which allows users to be aware Ž . of other users in the same page or WWW site.

## 2. Co-operation on the WWW

Suitable network infrastructure and document-intensive features of the WWW enable its use as a basis for co-operation. Basic support for co-operative work on the WWW, such as support for document handling and management, have already been implemented in several systems e.g. Refs. 2,20 whichŽ <sup>w</sup> <sup>x</sup>. provide rudimentary functions, e.g. brainstorming, workflow and document management. These are all document-centric tasks and as such, are ideal for the WWW platform. Another prominent feature of these applications is their support for asynchronous work rather than synchronous work.

Some systems have further extended asynchronous work towards synchronicity by adapting tools for online communication on the WWW. For example, MetaWeb expands BSCW 2 by running an awareness and communication application in parallel 39 . Also, CBE system 28 embeds an applet <sup>w x</sup> <sup>w x</sup> into a WWW page and provides a shared workspace, which is similar to Internet Relay Chat IRC sys- Ž . tems where users must enter a specific site for communication. In addition to these, some text-based and audio communication systems over ordinary WWW pages have been developed e.g. Refs. Ž <sup>w</sup> <sup>x</sup> 40,41 ..

These different applications address the importance of AWeb-basedB communication by presenting different solutions. Therefore, they are a step in the right direction, but they suffer from one or more of the following limitations:

<sup>Ø</sup> requirement to enter a specified online AplaceB to be able to meet others and communicate with them,

<sup>Ø</sup> lack of sufficient context to aid users in their communication attempts i.e. the users are im-Ž properly presented, so the awareness of others as well as the ability and accessibility to communicate with others are not made explicit ,.

<sup>Ø</sup> requirement of specific software to be installed on a client machine.

These limitations are noted by Isaacs et al. 23 as<sup>w</sup> <sup>x</sup> well. They also noted that unintended interaction should be supported among distributed communities; this, however, is not implemented in most systems. Very often, naturally occurring informal contacts and communication attempts provide an opportunity for collaborators to learn about each other, and serve as a framework within collaborative tasks 27 .<sup>w</sup> <sup>x</sup>

## 3. Maintaining awareness on the WWW

The importance of awareness of other people and their actions has been pointed out in many situations, e.g. in the London Underground control rooms 18 ,<sup>w</sup> <sup>x</sup> in formulating planes 13 , and in a stock exchange<sup>w</sup> <sup>x</sup> dealing room 19 . In this section, we will take the lessons learned and place them in the context of the WWW and develop a framework to aid system analysis.

The major issue of WWW-based co-operation we address in our paper is the maintenance of situation awareness between remote partners, when changes taking place in one location affect the activities in another. This kind of situation awareness is illustrated in Fig. 1. It shows a workspace, which is located in a server, and through which two message flows are passing by. These flows are actually series of actions and state changes human actions and data Ž changes which are usually considered to take place. in the server side.

In Fig. 1, all other communication channels between location A and location B are deliberately ignored due to the structure of the WWW. Direct communication without passing the messages through the WWW server is possible, but the difficulties of management, the inability to transmit the message to all other potential receivers in the same online community, and security issues prevent its usage. This premise of the awareness study requires that changes in any of the states are perceptible to the system itself. Otherwise, they would be ignored and unreachable.

## 3.1. Situation awareness

Situation awareness SA has long been recog-Ž . nised as a phenomenon that refers to the degree of accuracy by which observers’ perceptions of their current environment mirror reality 1,12 . SA can be<sup>w</sup> <sup>x</sup> organised into two categories: workspace awareness ( ) ( ) WA and user awareness UA . Both can be seen as subsets of situation awareness and are used together to support co-operative work. In general, awareness information represents the maintenance of group consciousness by keeping everyone adequately informed.

![](/api/attachments/DJ5Z6S9M/fulltext/images/1c144dc2354cd2dcaf93bd9d9c8732850e7f9f4f2527e54054dcb4ffe895f3ee.jpg)  
Fig. 1. Maintaining flows of changes between two users in dispersed places.

Workspace awareness means the understanding of other people’s interactions within a shared workspace <sup>w</sup> <sup>x</sup> 16 . This involves knowledge about the tasks and activities of those people. In reference to group work on the WWW, the WWW pages can be treated as a user interface. Here, the user interface is not to be understood as a normal user-side surface for interaction, but as a set of technical restrictions or rulesŽ . that guide the users’ actions in that space. Besides the user interface, typically there are work tasks to be performed, writing electronic documents, ordering some goods, or communicating with others, for instance.

Users get feedback through understanding the changes in artefacts documents . This is an addi-Ž . tional channel for human communication, i.e. the message is also transmitted through the artefacts themselves as stated in Robinson’s 33Ž <sup>w</sup> <sup>x</sup> ADouble-Level LanguageB about the presence of two layers of actions in group work; upon documents and simultaneously using spoken language to point out the issues in that document . In real life, when co-operat-. ing using physical objects, this communication through artefacts is often as important as direct communication 8 , or more important in a special <sup>w</sup> <sup>x</sup> situation in which opportunities for direct communication are not offered.

Awareness information provides knowledge not only about the changes in the artefacts, but also about the users’ actions upon those artefacts. In the situation awareness context, user awareness represents direct actions occurring in the workspace i.e. Ž web page or site ; that is, the information about who. is around, whether they are available, and what they are doing. This includes conversational awareness <sup>w</sup> <sup>x</sup> 6 , by which we refer to questions like Adid they hear, understand, and believe me?B In general, the maintenance of user awareness on the WWW provides functions like user action notifications and user conversations.

The notification of users’ actions includes the awareness information about each user’s personal status such as their WWW page entering and leav-Ž ing times as well as a contact indicator, which. facilitates their ability and willingness to establish contacts with others. For example, ICQ 22 provides<sup>w</sup> <sup>x</sup> some pre-formulated text-messages, e.g. AAvailableB, AAwayB, AExtended AwayB, ADo not disturbB, and APrivacyB, to indicate the users’ awareness status and their eagerness to communicate with other users, and other systems support informal user conversations on the WWW by integrating text-chat programs.

## 3.2. Information flows

Different implementations of situation awareness address different mechanisms to support co-operative work on account of technical considerations and the nature of collaborative work. Based on the perspectives of different requirements, different modalities of awareness information are described below.

v User interaction: The two basic modes are synchronous and asynchronous interactions. Synchronous interaction enables users to be aware of each other and other people’s activities on a relatively high level. Meanwhile, real-time contact facilities can be adopted to enable users to establish communication channels with each other on the basis of mutual consciousness. Asynchronous interaction keeps awareness information on a lower level, which builds on a sequential information-exchanging mode like email.

v User attention: There are two general ways to identify user attentions: direct and indirect. Direct attention provides direct understanding of activities of other people, e.g. mainly mediated by video conferencing or avatars in a 3D virtual reality environment. Indirect attention means attention is focused towards artefacts. Information required, or focused on, relates to the activities, which change the states of the artefacts, rather than about the person who performs the actions. Often, this happens in asynchronous systems, for example, in workflow systems and ordinary WWW sites.

v Information transmission: There are two types of information transmission: active push style andŽ .

passive delivery pull style . In active transmission, Ž . of which usage is restricted to synchronous systems, awareness information is explicitly generated and dispatched directly to participants subscribers . Con-Ž . versely, in passive mode, often used in asynchronous systems, awareness information is perceived by an implicit pull or through artefacts. That is, the artefact is the information carrier. There are no immediate cues of awareness information for users.

## 3.3. Technical issues

According to Norman 29 and Chen 5 , a need<sup>w</sup> <sup>x</sup> <sup>w x</sup> for face-to-face communication in order to perform co-operative tasks becomes less necessary, if the mechanisms to support situational awareness have been well established among group members whose roles are well defined. Although ordinary WWW users do not have explicit roles for collaboration, they have implicit roles set by the technology, i.e. specific applications operating on the WWW.

v Persistence: Information is stored on the server side to ensure the consistency and persistence of data. If any changes in the data occur, the users are notified in different ways depending on the situation, e.g. direct messaging is used while browsing online, or a reminder is sent when the user is off-line byŽ using email for example ..

v Authorisation: In order to be able to identify users e.g. so that the email reminder can be sent ,Ž . some user authorisation is needed. However, there are1 cases in which users are not willing to reveal their identity to every one c.f. Ref. 26 .Ž <sup>w</sup> <sup>x</sup>.

Table 1  
Awareness analysis framework

<table><tr><td>Situation awareness</td><td>workspace awarenessuser awareness</td></tr><tr><td>User interaction</td><td>synchronousasynchronous</td></tr><tr><td>User attention</td><td>directindirect</td></tr><tr><td>Information transmission</td><td>activepassive</td></tr><tr><td>Persistence</td><td></td></tr><tr><td>Authorisation</td><td></td></tr><tr><td>Operating platform</td><td>WWWstand-alone application</td></tr></table>

v Operating platform: Users may adopt the WWW browser as a tool for co-operation. However, even though the WWW browser provides a simple and uniform interface, a browser cannot be used in every situation due to its technical inadequacies in supporting complex co-operative tasks. This makes the use of stand-alone applications essential.

We have presented several issues with regard to maintaining the awareness of other people and their actions on the WWW. From those issues above, a framework for analysing awareness in terms of several systems, including those on the WWW, is summarised in Table 1.

## 4. Related studies of awareness support systems

Few systems provide awareness mechanisms to support user interaction. We will use the framework discussed to analyse several off-the-shelf applications and well-known prototypes. This brief survey covers systems from desktop to WWW applications, and from educational experiments to commercial products on different operating platforms. Our sample is based on computer-supported distributed group systems. We won’t present every known application but provide a set of applications instead, which support basic characteristics of group work and awareness.

v ICQ 22 is an Internet tool, which informs the<sup>w</sup> <sup>x</sup> user about other users who are online<sup>2</sup> at any time. Functions include public chat, private messages via ICQ, email, URL and file transfers. ICQ is a standalone application rather than a WWW-based usertracking system. However, ICQ includes a tool, which adds a small status bar about user’s presence in the ICQ application e.g.Ž AOnlineB and AOfflineB messages into a WWW page, but in principle, ICQ can . be regarded as an online reminder and communication tool.

v Elvin 11 is a synchronous notification applica- <sup>w</sup> <sup>x</sup> tion comprised of two stand-alone tools: Tickertape and CoffeeBiff. Tickertape displays text messages

Ž . events scrolling across a single-line window. Text messages are sent by the system or by other users. CoffeeBiff is an awareness tool, which shows users interest in going to the kitchen for a cup of coffee. At the moment, there is no linkage to the WWW, but the developers intend to include support for situation awareness, e.g. different event sources like WWW news, email delivery, and information stories.

v Cobrow 7 reveals users on the same WWW<sup>w</sup> <sup>x</sup> site and provides a tool for text chat communication. However, its major weakness is the lack of a counter-like-awareness tool i.e. users are forced toŽ use heavy user interface every time and platform . dependency on the server side due to the programming languages and implementation used.

v Gooey 14 enables users in the same WWW<sup>w</sup> <sup>x</sup> site to communicate with others, and to be aware of each other by getting a constantly updated list of others on the site. However, Gooey is not a pure WWW-based application, but a stand-alone i.e. itŽ requires installation system with a very tight con- . nection with WWW browsers. In addition to communication and basic awareness, Gooey enables content annotations or discussion launching on any web page, if the specific client software Gooey tool is in-Ž . stalled in the user’s computer.

v HumanClick 21 is a WWW communication<sup>w</sup> <sup>x</sup> tool designed for site operators, for example, for vendors in EC. HumanClick enables users Ž . customers to make a chat invitation to the site operator, and vice versa, operators can send chat requests to customers on their site. Awareness information about users on the page is only provided to operators, users are kept isolated from each other.

v WAP system 30 provides an awareness proto-<sup>w</sup> <sup>x</sup> type that gives the number of online users on the same site. The paper also touches on other issues such as user profiles and connectivity with other applications, but those have not been implemented or tested.

v Nessie 32 is an awareness environment, which<sup>w</sup> <sup>x</sup> supports event transmission. Situation awareness is oriented in two different ways: task or social relationship, and presented by sensors and indicators to symbolise particular awareness information. Nessie presents an open protocol and quite detailed descriptions on information presentation for event notifications, but it lacks studies on different awareness models, and consequently, the adaptation of these models to different events. However, Nessie provides a set of tools so that some features can be integrated with the WWW via common gateway Ž interfaces while other more advanced features re-. quire users to install external applications on their machine.

Several common shortfalls are distinguished.

v Software and platform-dependency: Most systems mentioned are stand-alone systems requiring installation on the client side. It is unlikely that users will, or are even able to download and install programs on their computer, therefore pure WWW applications are ideal, and often the only choice for them. On the server side, platform dependency is not as crucial as on the client side, but due to different programming languages and techniques, server side solutions are often platform- and operating systemdependent, thus the issue of portability is valid.

v Unclear awareness representation: Displaying awareness information should be considered with user interface design. For example, in Cobrow, it is difficult to find out who is in the same page from the user list. This can be regarded as one of the key aspects for mutual awareness, since users need to know about the other people’s interests before they may be willing to interact with them especially in EC. For example, in an EC site where cars are being sold, it is obviously essential to know which car orŽ car brand the person is interested in. .

A summary of the systems described is illustrated in Table 2 by using the framework presented earlier.

All these systems provide a certain level of awareness, since user awareness is supported in each system. However, workspace awareness is seldom supported, even though it is often seen as an essential feature of group work, because changes in the artefacts or their states need to be represented.Ž . Other dominant features are synchronous awareness updating, indirect user attention, and active information transmission. Also, it is remarkable that applications which are running only on the WWW have fewer features for co-operation—simply because the common WWW technology i.e. HTTP does notŽ . support continuous communication. However, future versions of Java Media Framework and WWW browsers will alter the situation.

In the next section, we will present our own system, PeopleAwarenessEngine http: Ž <sup>rr</sup>www. crackatit.com<sup>r</sup>., which takes the lessons learned from the various studies and puts them into practice.

## 5. PeopleAwarenessEngine

PeopleAwarenessEngine PAW builds up a gen- Ž . eral infrastructure and a set of functions to support situation awareness and user communication on the WWW. When using PAW, users are considered to be located AnearbyB in the sense that they are connected together when they are 1 looking at theŽ . same page place , or 2 sharing the same siteŽ . Ž . Ž . space . PAW addresses the major concerns associated with group working the following way: PAW is integrated into the WWW pages, therefore users do not need to launch an external application, go to a specific chat place, or install a browser plug-in, to be able to interact with others.

Table 2  
Comparison of awareness support systems

<table><tr><td></td><td></td><td>ICQ</td><td>Elvin</td><td>Cobrow</td><td>Gooey</td><td>Human Click</td><td>WAP</td><td>Nessie</td></tr><tr><td>Situation Awareness</td><td>workplace user</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td></tr><tr><td>User Interaction</td><td>synchronous asynchronous</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td></td></tr><tr><td>User Attention</td><td>direct indirect</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr><tr><td>Information Transmission</td><td>active passive</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td>√</td></tr><tr><td>Persistence Authorization</td><td></td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td></tr><tr><td>Platform</td><td>WWW stand-alone</td><td>√</td><td>√</td><td></td><td>√</td><td></td><td>√</td><td></td></tr></table>

Awareness information of people is embedded in the WWW pages, or alternatively in an additional window, which is launched from these pages. The WWW page provides a shared context of interest, which in turn, provides reasons to interact with others. The design makes it easy for users to initiate interactions once they are aware of, or perhaps even AseeB, each other where they are located. For example, when using PAW with an electronic commerce Ž . EC site, customers could ask questions in real time from the vendor while shopping there, or vice versa, the vendor might offer online help for the customers. Currently such a feature is not supported in EC applications. Asking questions or obtaining help through a help desk requires the user to send an email to the vendor, but there is no way of knowing the other side’s presence, availability, or willingness to interact. PAW is therefore used to create social proximity over the WWW pages, where the creation of a good customer relationship is supported seeŽ also Ref. 24 .<sup>w</sup> <sup>x</sup>.

PAW consists of four components, which are drawn from the theory of situation awareness. They are the following.

v Counter Ž . workspace awareness , which enables users to be aware of others in the same page and in the same site, allowing the user to contact others who are virtually nearby.<sup>3</sup>

v User list Ž .user awareness for users to obtain information about others, or contact anyone in the community.

v Page list Ž . workspace awareness , which is similar to the user list, but which is generated according to the users’ dynamic actions like browsing movements or the static structure of sites, for example, the product list in shop sites. Workspace awareness can be triggered and generated from traditional groupware and conveyed to web users via PAW Server Ž . the Server API component in Fig. 2 . For example, the status, ownership, timestamps of documents group users are working on can be presented remotely to mobile workers via PAW tool.

v Communication component user awareness( ) enables users to communicate by using text chat, or more advanced audio and video tools which how-Ž ever, are not yet supported due to technical inadequacies. Java Media Framework V2.0 38 supports <sup>w</sup> <sup>x</sup> audio capture and transmission, but has not been integrated to PAW or commonly used WWW browsers yet ..

Fig. 2 illustrates the structure of PAW architecture. The PAW server is operating in parallel, but independently of an ordinary web server, as a Java Servlet 37 . The CRACK! applet code is embedded<sup>w</sup> <sup>x</sup> in the web page. Once a browser downloads a page from the HTTP server, the applet is launched as Ž usual and a connection to the CRACK! server is. established by the applet. The client sends regular heartbeat signals to allow the server to detect, for example, network crashes, and reciprocally receives update messages. The heart of the client side is the Center, which contains user and page list components. It also provides a gateway to open a chat window.

PAW architecture is a typical Client–Server architecture with some additional servers and services Ž . see Fig. 2 . The advantage of PAW is the combination of means and reasons to co-operate i.e. HTMLŽ pages and awareness widgets e.g. PAW counter ,. Ž . so that modifications are required on the server side but additional installations are not needed on the client side. Embedding a Java applet pushes the need for support onto the webmasters who have to install the PAW link into each page. A beneficial solution is to modify a proxy server, so that it inserts the code automatically into every page passing by.

![](/api/attachments/DJ5Z6S9M/fulltext/images/c4e4383418dd45cf8d7e667983984c58399730ce96144252ce2457e474a1d32a.jpg)  
Fig. 2. People awareness engine architecture.

![](/api/attachments/DJ5Z6S9M/fulltext/images/e979fd1298b50f8d7aa9ce722a909154f8e057393d9dc9c5c12d60edd686160b.jpg)  
Fig. 3. Counter showing the number of users online.

## 5.1. PAW functions

The counter, illustrated in Fig. 3, is a Java applet installed in every web page. It provides background awareness of others nearby. For example, when users enter any page, they see a rotating number represent ing the number of people in the same page or areaŽ depending on the configurations . The counter num- . ber changes with a sound when users browse theŽ . site. This sound provides peripheral awareness of actions i.e. users’ entry and leave occurring in theŽ . environment, and does not interrupt users’ other ongoing activities. Hence, users are adequately informed of others presence, even if they scroll the web page and hide the counter, or open another application.

Although the counter is not prominent, it provides basic awareness information and hides people’s identity behind raw numbers.<sup>4</sup> It also prevents users from undesirable communication attempts, since it is possible to communicate with others or receive communication requests only when the Center is open and active. For example, let’s consider a case where a customer is viewing a list of goods and is aware of another person’s arrival by seeing the spinning Ž counter or hearing the sound, i.e. getting peripheral awareness information . If the customer needs more. information or just wants to chat with another, she opens the Center and accesses a communication tool. To be able to communicate, both participants must have the Center open; if one wants personal privacy, she keeps her Center closed. This simple mechanism —a deliberate action needed to open the Center— serves as an indicator illustrating one’s status to the other—Afree for chatB or Ado not disturb me.B It is possible to maintain privacy, even with the opening of the Center by changing between these user statuses.

In addition to the counter, which allows low-level awareness of others, PAW provides components for maintaining higher levels of awareness user andŽ page views and mechanisms for human communica-. tion. Much like other similar awareness systems, the Center illustrated in Fig. 4 remains next to theŽ . WWW pages, providing constant awareness of others and the ability to communicate with them.

v Online status in Fig. 4 shows a person’s Ž . visibility and willingness to interact with other people. The Afree for chatB mode allows all communication attempts to proceed unhindered. ANo disturbB reveals that all incoming messages are ignored by the system but the user is visible to others, while AprivateB hides and denies everything the user is notŽ presented in the user list ..

v User and page views represent a higher Ž . level of awareness compared to the counter. The user view shows all people online while the page view shows their corresponding location.

![](/api/attachments/DJ5Z6S9M/fulltext/images/fa2c50491df263aff077156b269f47d14983e07082b540842c670c19bdd1c77b.jpg)  
Fig. 4. The PAW Center.

Table 3 PAW functions

<table><tr><td colspan="2">Awareness framework</td><td>PAW function</td></tr><tr><td rowspan="2">Situation awareness</td><td>workplace</td><td>The feedback, for example, “what’s new” page, “to-do” list, or change logs, is generated by other software (groupware or web server) which operates in parallel with PAW. PAW depicts the feedback to all users.</td></tr><tr><td>user</td><td>PAW tracks users’ transitions between WWW pages and their conversation.</td></tr><tr><td rowspan="2">User interaction</td><td>synchronous</td><td>Direct actions and instant feedback are supported.</td></tr><tr><td>asynchronous</td><td>Not directly supported by PAW, but because PAW can be integrated with other software, asynchronous interaction is supported indirectly.</td></tr><tr><td rowspan="2">User attention</td><td>direct</td><td>PAW supports a 3D presentation of the site structure and the live numbers of users in each page. A VRML-supported browser is needed.</td></tr><tr><td>indirect</td><td>Icons, sound and text are used.</td></tr><tr><td rowspan="2">Information transmission</td><td>active</td><td>PAW is a real-time system.</td></tr><tr><td>passive</td><td>Not supported, but similar to asynchronous interaction, a third party application can be integrated.</td></tr><tr><td>Persistence</td><td></td><td>PAW stores all events into a log-file, which can be analysed and used later.</td></tr><tr><td>Authorisation</td><td></td><td>Standard version does not support authorisation. However, the PAW server APIs external applications, which do support authorisation, can be combined with PAW.</td></tr><tr><td>Operating platform</td><td>WWW-based</td><td>PAW is completely platform-independent.</td></tr></table>

v Detailed information about people is presented in area .

v Once the communication media is selected ,Ž text chat, audio, and videoconferencing , the chat. window will appear to allow people to, for example, compose and read text messages.

The list above includes a short description of implemented features. Using the framework presented earlier, it can be claimed that PAW supports workspace and user awareness, synchronous user interactions, both direct and indirect user attention, and active information transmission on the WWW Ž .see Table 3 .

One can question whether the counter is needed at all, because the Center provides more accurate information about users. However, the answer is in the positive because the use of a small counter reduces the intervention of users’ normal page browsing or reading, while the big Center window may disturb people’s normal browsing. As Ref. 10 have noted: <sup>w</sup> <sup>x</sup> AIf awareness is a passive and background notion, then the interfaces must be particularly lightweight. At the same time, if the awareness is a basis for more interactive exchanges, then the interface must provide those capabilities.B

The PAW Center appears if and only if the user makes a specific AopenB action to start it up to investigate further awareness information of others and, the possibility of communicating with them.

## 6. Discussions and future work

Systems supporting situation awareness must satisfy general requirements for supporting awareness in different situations, and provide mechanisms for easy and flexible awareness information provision. Our awareness engine, PAW, however, is designed specifically for the WWW so that it can be used as a component which is integrated with other group work supporting systems e.g. BSCW 2 through itsŽ <sup>w</sup> <sup>x</sup>. programming interface.

Currently most WWW-based systems do not support all aspects of awareness, since there are only a few theoretical studies which they could relate to. One of them is Dix’s 9 work on defining general<sup>w</sup> <sup>x</sup> requirements for WWW applications, where he lists essential features such as information structures, notification of actions workspace awareness andŽ . awareness of users in addition to more applicationdependent issues. However, in the future it is important that we set awareness standards on the WWW, where applications differ significantly from traditional stand-alone ones.

In contrast to other systems see Tables 2 and 3 ,Ž . PAW can be seen as a kind of generic Ameta-applicationB in which the theory about situation awareness is used. As mentioned before, PAW does not force users to enter a specific place to be able to observe others, or even interact or communicate with them, since PAW is embedded in each page. Software and platform independence formed the base, which we have used when designing the first versions of awareness protocol and further connectivity with other applications. Whenever the protocol is fixed, there is no need to modify anything except the awareness representation and the user interface, which are both task- and domain-specified settings. A general, complete awareness protocol is not the topic of this paper, so it is excluded.

We believe that PAW will be widely used. It can be assumed that people spending long time at a site are interested in the topic, thus they are sharing a common point of interest. Natural follow-up for this is to create connections between the users. As said, PAW allows this by letting them to be aware of others at the same page or somewhere nearby. If users want to discuss with others, simply they can open the Center, otherwise, they are kept non-disturbed. Both the practical benefit of users to choose their level of presence, and of WWW administrators to configure the system around the common point of interest, will make the PAW to be widely used. For example, most sites, which will benefit the PAW, are databases e.g. case history for doctors , help desks Ž . Ž . Ž for ordinary people , and e-commerce for customers and sales persons sites. In the future, we . plan to integrate PAW with some EC sites with different contexts, users and tasks, so that empirical evaluations of our system and its usage will be achieved.

In the future, we will insert PAW into several WWW sites to perform detailed user evaluations. The basic question of this study is to examine whether awareness information of other users’ location and activity in the context of group work will help the completion of tasks. Our initial results parallel with theoretical foundations.

## 7. Summary

In this paper we have presented an awareness framework, which we have used to analyse some common applications. In particular, we examined the need for awareness on the WWW, and the ways users are aware of each other. Finally, we have presented our ongoing project, PeopleAwarenessEngine, through which situation awareness has been implemented into WWW pages.

Studying situation awareness on the WWW, especially workspace awareness, has a particular set of requirements. Awareness information is domainspecified and dependant on the user’s needs, therefore, technical support for different kinds of awareness information is needed. The WWW is designed for global access, so potentially hundreds or thousands of users could be located on one site at the same time, e.g. viewing the statistics in an Olympic games site, or visiting Amazon.com just before Christmas. Therefore, systems running on the WWW must be able to scale upwards by providing alternative possibilities for representing other people. Nowadays, however, most systems target small audiences or groups where intentions for using theŽ . system vary less depending on the time and task.

Furthermore, co-operative work on the WWW is normally seen as a universal access to information rather than a universal interface towards other users. If the WWW pages are treated as a user interface, there is no implicit connection between the workspace and artefacts inside that space. The awareness information is simply a set of changes, which have taken place there. The awareness is not about changes in the data itself, since the work is completed in users’ local physical places. Workspace awareness is needed when creating seamless links between the physical work place and online environment.

## References

<sup>w</sup> <sup>x</sup> 1 M. Adams, Y. Tenney, R. Pew, Situation awareness and the cognitive management of complex systems. Human Factors 37 1 1995 85–104.Ž . Ž .

<sup>w</sup> <sup>x</sup> 2 R. Bentley et al., Basic support for cooperative work on the World Wide Web special issue on innovative applications of Ž the World Wide Web . International Journal of Human–. Computer Studies 46 6 1997 824–846.Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 T. Berners-Lee et al., The World Wide Web. Communications of the ACM 37 8 1994 76–83.Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 C. Brown, S. Benford, Tracking WWW users: experience from the design of HyperVisVR. Proceedings of WebNet’96, San Francisco, 1996.

<sup>w</sup> <sup>x</sup> 5 L.L.-J. Chen, B.R. Gaines, Methodological issues in studying and supporting awareness on the World Wide Web. Proceedings of WebNet96, San Francisco, USA, 1996.

<sup>w</sup> <sup>x</sup> 6 H.H. Clark, S.E. Brennan, Grounding in communication. in: R.M. Baecker Ed. , Readings in Groupware and ComputerŽ . Supported Cooperative Work: Assisting Human–Huam Collaboration. Morgan-Kaufmann Publisher, CA, 1991, pp. 222–233.

<sup>w</sup> <sup>x</sup> 7 Cobrow, Cobrow tool, 1999, URL: http:<sup>rr</sup>www.cobrow. com<sup>r</sup>pages<sup>r</sup>.

<sup>w</sup> <sup>x</sup>8 A. Dix, Challenges and perspectives for cooperative work on the web. Proceedings of the ERCIM workshop on CSCW and the Web, Sankt Augustin, Germany, 1996.

<sup>w</sup> <sup>x</sup> 9 A. Dix, Challenges for cooperative work on the web: an analytic approach. Computer Supported Cooperative Work: the Journal of Collaborative Computing: Special Issue on CSCW and the Web 6 2–3 1997 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 10 P. Dourish, S. Bly, Portholes: supporting awareness in a distributed work group. Proceedings of the Conference on Human Factors In Computer Systems CHI’92 , ACM, Mon- Ž . terey, CA, 1992.

<sup>w</sup> <sup>x</sup> 11 G. Fitzpatrick et al., Augmenting the workaday world with Elvin. Proceedings of the Sixth European Conference On Computer Supported Cooperative Work ECSCW’99 ,Ž . Kluwer Academic Publishers, Copenhagen, Denmark, 1999.

<sup>w</sup> <sup>x</sup> 12 R.D. Gilson, Introduction to the special issues of situation awareness. Human Factors 37 1 1995 3–4.Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 C. Goodwin, M. Goodwin, Formulating planes: seeing as a situated activity. Cognition and Communication at Work. Cambridge Univ. Press, NY, 1996.

<sup>w</sup> <sup>x</sup> 14 Gooey, Gooey, 2000, Hypernix, http:<sup>rr</sup>www.getgooey. com<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 15 S. Greenberg, Collaborative interfaces for the web. Human Factors and Web Development 18 1997 241–254.Ž .

<sup>w</sup> <sup>x</sup> 16 C. Gutwin, S. Greenberg, Workspace awareness. Position Paper for the ACM CHI’97 Workshop on Awareness In Collaborative Systems, Atlanta, Georgia, 1997.

<sup>w</sup> <sup>x</sup> 17 R. Harper, Inside the IMF: an ethnography of documents, technology, and organisational action. in: B.R.G.A.A. Monk Ž . Ed. , Computers and People. Academic Press, San Diego, 1998.

<sup>w</sup> <sup>x</sup>18 C. Heath, P. Luff, Collaborative activity and technologica design: task coordination in London underground control rooms. Proceedings of the Second European Conference on Computer-Supported Cooperative Work ECSCW ’91 ,Ž . Kluwer Academic Publishers, Amsterdam, Netherlands, 1991.

<sup>w</sup> <sup>x</sup> 19 C. Heath, M. Jirotka et al., Unpacking collaboration: the interactional organisation of trading in a city dealing room. Proceedings of the Third European Conference on Computer Supported Cooperative Work-ECSCW’93, Kluwer Academic Publishers, Milan, Italy, 1993.

<sup>w</sup> <sup>x</sup> 20 T.A.B.R. Horstmann, Distributed authoring on the web with the BSCW shared workspace system. ACM Standards View 5 1 1997 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 21 HumanClick, HumanClick, 2000, http:<sup>rr</sup>www.humanclick. com<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 22 ICQ, ICQ, 2000, ICQ. http:<sup>rr</sup>web.icq.com<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 23 E.A. Isaacs, J.C. Tang, T. Morris, Piazza: a desktop environment supporting impromptu and planned interactions. Proceedings of CSCW’96, ACM, Boston, MA, 1996.

<sup>w</sup> <sup>x</sup> 24 T. Jackson, Chat finds a new life in e-commerce. Financial Times 2000 .Ž .

<sup>w</sup> <sup>x</sup> 25 C. Kasbi, M.D. Montmollin, Activity without decision and responsibility: the case of nuclear power plants. Distributed Decision Making: Cognitive Models for Cooperative Work. Wiley, Chichester, 1991, pp. 275–283.

<sup>w</sup> <sup>x</sup> 26 K. Kauppinen et al., Producing identity in collaborative virtual environments. Proceedings of VRST’98, Taipei, Taiwan, 1998.

<sup>w</sup> <sup>x</sup>27 R.E. Kraut, C. Egido, J. Galegher, Patterns of contact and communication in scientific research collaboration. in: J. Galegher, R.E. Kraut, C. Egido Eds. , Intellectural Team-Ž . work: Social and Technological Foundations of Cooperative Work. Lawrence Erlbaum, Hillsdale, NJ, 1990, pp. 149–171.

<sup>w</sup> <sup>x</sup> 28 J.H. Lee et al., Supporting multi-user, multi-applet workspaces in CBE. CSCW’96, ACM, Boston, MA, 1996.

<sup>w</sup> <sup>x</sup> 29 D.A. Norman, Cognitive artifacts. in: J.M. Carroll Ed. , Ž . Designing Interaction: Psychology at the Human–Computer Interface. Cambridge Univ. Press, Cambridge, UK, 1991, pp. 17–38.

<sup>w</sup> <sup>x</sup> 30 K. Palfreyman, T. Rodden, A Protocol for user awareness on the World Wide Web. Proceedings of CSCW’96, Boston, MA, USA, 1996.

<sup>w</sup> <sup>x</sup> 31 J.F. Patterson, M. Day, J. Kucan, Notification servers for synchronous groupware. CSCW’06, ACM, Boston, MA, 1996.

<sup>w</sup> <sup>x</sup> 32 W. Prinz, Nessie: an awareness environment for cooperative settings. Proceedings of ECSCW’99, Kluwer Academic Publishers, Copenhagen, Danmark, 1999.

<sup>w</sup> <sup>x</sup> 33 M. Robinson, Double-level languages and co-operative work. AI and Society 5 1991 34–60.Ž .

<sup>w</sup> <sup>x</sup> 34 M. Robinson, S. Pekkola, User communication and monitoring system for computer networks, Patent pending, 1999.

<sup>w</sup> <sup>x</sup> 35 K. Schmidt, L. Bannon, Taking CSCW seriously—supporting articulation work. Computer Supported Cooperative Work Ž . CSCW . 1992, pp. 7–40.

<sup>w</sup> <sup>x</sup> 36 L.A. Suchman, R.H. Trigg, Understanding practice: video as a medium for reflection and design. in: E.J. Greenbaum, M. Kyng Eds. , Design at Work. Lawrence Erlbaum, London, Ž . 1991, pp. 65–89.

<sup>w</sup> <sup>x</sup> 37 Sun, Java Servlet, 1999, Sun Microsystem.

<sup>w</sup> <sup>x</sup> 38 Sun, JavaTM Media Framework, 1999, Sun Microsystem.

<sup>w</sup> <sup>x</sup> 39 J. Trevor, T. Koch, G. Woetzel, MetaWeb: bringing synchronous groupware to the World Wide Web. Proceedings of the ECSCW’97 European Conference on Computer Sup- Ž ported Cooperative Work , Lancaster, 1997. .

<sup>w</sup> <sup>x</sup> 40 M. Walther, Supporting development of synchronous collab-

oration tools on the web with GroCo. Proceedings of the ERCIM Workshop on CSCW and the Web, Sankt Augustin, Germany, 1996.

<sup>w</sup> <sup>x</sup> 41 M.V. Welie, A. Eliens, Chatting on the web. Proceedings of ¨ the ERCIM Workshop on CSCW and the Web, Sankt Augustin, Germany, February 7–9, 1996.

![](/api/attachments/DJ5Z6S9M/fulltext/images/24a216d5767b38eb41ef4ed67488b720c59180f9847f0716b32db4f3777b415f.jpg)  
Yu You received his Master’s degree from the University of Jyvaskyla in¨ ¨ 1997. Currently, he is a doctoral student in the Graduate School in Computing and Mathematical Sciences COMAS ,Ž . University of Jyvaskyla. He has been¨ ¨ working in the field of CSCW and HCI for several years. His current research interests include awareness supports in group environments and effective Internet advertising methods and management.

![](/api/attachments/DJ5Z6S9M/fulltext/images/424512053b25bea29bf09cedda5fe4631257b9c99bfc9216b25dff97ea04cc7c.jpg)  
Samuli Pekkola, MSc, is an Assistant Professor in the Group Technologies Programme in the Department of Computer Science and Information Systems at the University of Jyvaskyla, Finland.¨ ¨ He has been working on virtual reality for a couple of years, and has published several scientific articles. He is a project manager for the VIVA project, examining the support of office and group work in VR and through the WWW. His main research interests include CVE, CSCW, WWW, networking and multimedia.
