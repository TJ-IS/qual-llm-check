---
otero_id: 21781
otero_key: "DD5DH4AM"
title: "Collaborative Object Workspaces (COWS): exploring the integration of collaboration technology"
authors: "Munir Mandviwalla; Shariq Khan"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00049-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Collaborative Object Workspaces COWS : exploring the ž / integration of collaboration technology

Munir Mandviwalla <sup>)</sup>, Shariq Khan

Temple UniÕersity, Computer and Information Sciences, Room 303, Wachman Hall 038-24, 1805 N. Broad Street, Philadelphia, PA 19122, USA

## Abstract

The integration of multiple computer-based tools and technologies presents new design and usage challenges. This paper reports on a project focusing on integrating well-known collaborative features into a single usable tool. The results of the project are a set of design and behavioral propositions suitable for future research. The project also introduces the use of a research methodology that integrates the process of prototyping with the process of building theory. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Collaboration; Computer-Supported Cooperative Work CSCW ; Group support systems; Any-time, any-place; Integration; Ž . Convergence; Theory; Research methodology

## 1. Introduction

Organizational computing is evolving from centralized processing to inter- and intraconnected systems. For example, to the user, the distinction between local area networks and wide area networks is no longer very relevant. The act of word processing is no longer separate and distinct from, say, writing an e-mail message. Web browsers now include shared whiteboards, chat, and voice interaction, and can access both local and wide area documents. Convergence is the underlying concept influencing a wide range of technologies. Convergence suggests the need to think formally about integration. In many of the above examples, the key element is integration, i.e., combining existing tools and techniques to solve problems. Integration represents new design issues and challenges.

Integration is an old idea; the integrated desktop has been a dream for computer visionaries for a long time. However, integration is difficult to research and accomplish. The tools are not quite there. There is very little prior systematic research on the topic. Most efforts have focused on envisioning or designing highly integrated systems 3 . It is surprising that <sup>w</sup> <sup>x</sup> so little research has followed the pioneering work of Engelbart and other visionaries.

We think that research on collaborative systems is at an important cross-road with respect to integration and the evolution of organizational computing. Researchers and software developers have invented many important collaborative support features e.g.,Ž WYSIWIS, concurrency control, anonymous brainstorming, and organizational memory . There is now. a need to start thinking about how to integrate existing features. This is important because, for example, it does not seem reasonable to expect a team to use a separate system whenever they need to share different types of information e.g., text, documents,Ž sketches in different settings e.g., face-to-face, dis- . Ž tributed and asynchronous . The problem is that . since most systems are self-contained, sharing data is inconvenient, log-on procedures vary, and users have to experience the additional cognitive load of moving back and forth between disparate systems.

From the design perspective, we know very little about building integrated systems and from the organizational perspective, we know even less about how, and if, users will apply new integrated technologies. For example, how do you start a design process following an ‘‘integrated’’ perspective? What are strategies for integration? Will integrated features be appropriated in the manner envisioned by the designers or will users simply use the technologies as stand-alone distinct tools? How well will users understand the highly integrated capabilities of these tools? These and other questions will determine the success and adoption of integrated technologies.

To summarize, the research goals of this paper are to explore the following questions in the context of collaborative work:

<sup>Ø</sup> What is integration?

<sup>Ø</sup> How do you build integrated systems?

<sup>Ø</sup> Are integrated systems useful?

In this paper, we take a step toward answering some of the questions above by a outlining a Ž . preliminary definition and presenting generic strategies for integration; b applying our ideas in a Ž . prototype development project; and c suggesting Ž . theory, design, and usage issues within the context of an exploratory study.

The context for the above work is collaboration. We ignore issues involving the integration of single user tasks such as word processing and spreadsheeting. These tasks are only considered when they have a collaborative context such as collaborative authoring. Collaboration is a natural fit for integration research given the large number of tasks and features relevant to group work. Several researchers have already explored the benefits of an integrated approach to collaboration technology e.g., Ref. 12 .<sup>w</sup> <sup>w</sup> <sup>xx</sup> We are more interested in integrating existing andŽ often proven collaboration features. As a result, the. main contribution of our work is in exploring strategies for integrating well-known collaborative support features. <sup>3</sup>

## 2. Research approach and methodology

The goal of research is to apply rigorous and appropriate methodologies to interesting problems; e.g., applying a behavioral theory to understand the use of integrated features, conducting an laboratory experiment to test a hypothesis related to integration, or studying how organizations use integrated features in a field experiment. We decided that it was premature to apply the above research strategies. As discussed earlier, we know very little about integration in collaborative systems; what it is, what are the fundamental components and characteristics, how it should or could be used, and so on. In addition, it is unclear as to what behavioral theory is relevant to the problem, what the useful hypotheses are, and how an organization should be studied. There is a need for fundamental theoretical principles to guide research. Moreover, there are very few examples of integrated collaborative systems. Using existing technology as a basis for exploring the topic will likely lead to irrelevant questions, whereas looking at exciting new examples of integration in the commercial world may result in focusing on new technology that will never take hold, again producing irrelevant questions. Our approach is to use prototype systems development as a research methodology to address the question of integration and collaborative work. The approach is based on inducing design and behavioral propositions that will contribute to theory development.

According to Webster 1985 , a theory is ‘‘theŽ . general or abstract principles of a body of fact, a science, or an art.’’ According to Dubin 2 , a theory<sup>w</sup> <sup>x</sup> is an attempt to model some aspects of the empirical world. Walls et al. 15 argue that Dubin’s character-<sup>w</sup> <sup>x</sup> ization of ‘‘theory’’ only takes into account the predictive and explanatory character of the social and natural sciences. The problem is that in Dubin’s and other social scientists’ conceptualizations of theory, the object of interest is assumed to already exist in nature or society. When we consider integration, the ‘‘objects’’ have not been fully invented yet, suggesting the need to think about invention and the invention process. This brings us to what is now a classical paradox of Information Systems IS re-Ž . search in which we are faced with researching objects<sup>r</sup>issues that do not exist or still need work using methodologies that assume that the object<sup>r</sup>issue is relatively fixed in nature or society. Traditionally, this has meant choosing between an acceptable methodology such as conducting a laboratory experiment with irrelevant technology or spending the large amount of time and resources needed to create the technology with little to show for the research other than a system. Moreover, one of the key problems of systems development type of research is the tendency to work in a theoretical vacuum, producing systems that can only be evaluated for their intrinsic design qualities rather than empirically testable theories, hypotheses, experimental design, and data analysis 16 .<sup>w</sup> <sup>x</sup>

Walls et al. 15 provide researchers with a struc-<sup>w</sup> <sup>x</sup> tured process for creating theoretically motivated and empirically testable system designs. Walls et al. define the components of a design product theory to include meta-requirements — goals to which the theory applies, meta-design — artifacts hypothesized to meet meta-requirements, kernel theories — theories from reference disciplines that govern the design requirements, and testable design product hypothesis — that tests whether the meta-design satisfies the meta-requirements. Mandviwalla et al. <sup>w</sup> <sup>x</sup> 9 applied the Walls et al. approach to explore new structures for the design of group support systems. However, the Walls et al. approach does not help the researcher identify applicable kernel theories or suggest strategies for generating testable design product hypothesis. There are no obvious kernel theories related to integration; it may be a topic that is more ‘‘internal’’ to the field of IS rather than ‘‘external’’ <sup>w</sup> <sup>x</sup> <sup>4</sup> 16 . In effect, the Walls et al. approach presupposes the existence of a paradigm; they assume ‘‘normal science’’ in which theories and methodologies are readily available 6 . Paradigms are impor- <sup>w</sup> <sup>x</sup> tant because they provide scientists with a map and provide some of the directions essential for mapmaking 6 . Unless the researcher has some idea where to go, they will not be able to produce ‘‘parsimonious’’ research based on ‘‘strategic’’ hypothesis Ref. 16 , p. 2 . Given the large number of <sup>w</sup> <sup>w x</sup> <sup>x</sup> system options and behavioral options in IS research, it is very important that we focus on ‘‘strategic’’ questions.

Weber 16 argues that IS research should focus<sup>w</sup> <sup>x</sup> on internally oriented paradigms as opposed to paradigms and kernel theories from related fields. Weber proposes an approach that focuses on ‘‘discrete artifacts’’ — objects in the internal environment that take on discrete states particularly the data and instructions that make up a system. The discrete artifacts are researched by a study of statics identifying the basic structural properties of the artifact, study of comparatiÕe statics — how the structural properties relate to each other and how to rearrange them to attain increase levels of performance, and study of dynamics — the changes that occur when an artifact moves from one equilibrium position to another. For example, in the context of integration research, a study of statics could mean understanding the properties of integration and a study of comparative statics could mean understanding which combination of integration methods yields the best performance. It is through performance that Weber envisions a link to the external environment Že.g., including user satisfaction as a variable of interest . However, Weber maintains that the connec-. tion should not be based on theories of the external environment such as behavioral theories but on establishing the conditions for success across a class of systems based on the internal structural propertiesŽ . of the system. Weber rejects the notion of studying interactions between the external environment and the internal environment because the process will inevitably lead to a focus on the objects in the external environment given that the variability of humans is much more than the variability of artifacts.

We believe that it is possible to balance the interaction between the internal and external environments. The concepts of strategic hypothesis and parsimony can help the researcher remain focused on both technical and behavioral issues. Moreover, Weber’s internal focus may lead to technology determinism 10 . A deterministic approach may lead to <sup>w</sup> <sup>x</sup> systems and paradigms that will never be used. Finally, many of us are attracted to IS research because of the potential to impact design and behavior. One way to balance design and behavior is to make them interdependent through concepts of practicality Žcurrent design can only support some behaviors and . Ž releÕance current behavior will only use some design artifacts . However, even if we could. balance behavior and design using concepts of practically and relevance, how can we identify the strategic issues that should be balanced? As Weber 16<sup>w</sup> <sup>x</sup> points out, the number of possibilities for human behavior and for constructing artifacts is very large.

Kuhn 6 outlines the process of scientific revolu-<sup>w</sup> <sup>x</sup> tion which is also the process through which theo-Ž ries and paradigms are created as being sparked by. the perception of an anomaly. Normal science plays a critical role in this process because working with standard tests and procedures leads to a detail of information and to a precision that prepares the researcher to know what to expect — this person is best equipped to know when something has gone wrong and to identify true and interesting anomalies. In IS, it is increasingly hard to see relevant anomalies because due to various environmental, logistical, and structural factors, we often limit empirical research to apparatus read: technology that is rootedŽ . in design paradigms that are no longer relevant e.g.,Ž researching the ease of use of Windows 3.1 when Windows ’95 changed the design paradigm ..

We believe that prototyping — the process of developing, testing, and refining artifacts — affords information scientists the opportunity to jumpstart the sparks needed to perceive anomalies. Given the large number of design options and larger number of behavioral options, the speed and process of prototyping allow the researcher to consider and discard many combinations of behavior and design. Fig. 1 presents the process used for our research on integration and collaborative work. The process binds behavior to implementable artifacts and binds system design to behaviorally relevant options that allow the IS researcher to converge on the strategic hypotheses that are the key to development of theory. The process affords the best chance of perceiving the anomalies that Kuhn writes about. Moreover, if one accepts Kuhn’s view of science, then prototyping is the best mirror of how science is conducted. The remainder of this paper applies the methodology outlined in this section.

![](/api/attachments/DD5DH4AM/fulltext/images/b156692355c9bac8d89fd1adaa6699f4c3e529368ee9493b38f10ec2a289ae54.jpg)  
Fig. 1. Prototyping as a research method.

## 3. Conceptualizing the problem

## 3.1. Issues of integration

This section presents a preliminary definition of integration. We first present generic ideas for identifying, defining, and implementing integration. These ideas are applied to collaboration and our specific project in Section 4.

First, integration does not mean ‘‘throwing everything into the pot.’’ Only proven features that show real value are candidates for integration. The goal is to increase the value of these features by making them more accessible and powerful. Integration also provides opportunities for new features that were previously not possible. All technological domains can be broken up into smaller components. For example, word processing consists of many components such as spell checking, WYSIWYG, and outlining. Often, these features can be abstracted or grouped together as factors based on some key underlying factors. In the collaborative context, concepts of mode, medium, and structure provide a powerful lens for thinking about Computer-Supported Cooperative Work CSCW, also see Ref. 8Ž <sup>w</sup> <sup>x</sup> and explained further below . There are other legiti- . mate grouping schemes. For this research, we are less interested in identifying the perfect grouping; only in that the scheme should provide a powerful lens for thinking about the selected technological domain.

A technology is integrated in the technological domain of interest if it combines support for more than one of the identified key factors. For example, a collaborative technology is integrated if it combines support for more than one mode, medium, and structure.

Borrowing concepts from marketing, the integration may take a vertical direction where, e.g., several different modes of working are integrated e.g.,Ž same-time, same-place with different-time, different-place . The integration may also take a. vertical–horizontal focus where, e.g., several different modes are integrated with several different structures. <sup>5</sup> Integration is accomplished at the presentation Ž . interface and<sup>r</sup>or data level. Consider the Netscape browser. The application supports several different media — hyperdocuments, text, graphics, sound, and video. The integration is at the presentation level. The underlying data points to different files.

## 3.2. Collaboration and integration

This section further details the key collaborative integration factors identified above mode, medium,Ž structure , the direction of integration vertical. Ž and<sup>r</sup>or horizontal , and how integration is imple- . mented data andŽ . <sup>r</sup>or presentation .

Mode pertains to different ways of working. For example, some systems support face-to-face work Ž . same-time, same-place , while others focus on distributed work different-time, different-place . AnŽ . integrated application will support more than one mode of work. Important attributes of mode include location and time and issues dependent on combinations of location and time e.g., awareness of others,Ž public or private work .. Medium is the media that the application provides for interaction. For example, some systems provide desktop video; others combine video with a shared whiteboard. Still others focus on text only. An integrated application will combine support for at least two different media. Important attributes of medium include the types of media Ž . e.g., text, graphic, video, 3D, etc. and issues that arise from the intrinsic properties of each medium Ž . e.g., richness . Structure is the structure provided by the application to support group development and productive outcomes. For example, some systems support cognitive mapping structures. Others focus on anonymity and consensus building through voting and commenting. An integrated application will combine support for at least two distinct structures. Important attributes of structure include the behavior that the structure focuses on such as consensus building and reduction of process losses.

All the factors are interrelated. For example, integrating support for multiple modes may also involve integrating support for multiple media; integrating a shared whiteboard with a bulletin board includes integrating two media — graphics for the shared whiteboard and text in the bulletin board — and may also involve two modes — synchronous for the whiteboard and asynchronous for the bulletin board. Integration is accomplished at the presentation Žinterface and . <sup>r</sup>or data level. In the previous example, a presentation level integration would imply that bulletin board and whiteboard are somehow represented together in one screen. A data level integration would imply that the bulletin board and whiteboard share data. The focus above has been on setting up a preliminary working definition of integration.

Table 1  
Basic attributes of COWS

<table><tr><td>Collaboration factor</td><td>COWS attributes</td></tr><tr><td>Mode</td><td></td></tr><tr><td>Same-time, same-place</td><td>quick entry, organize (object folders and relationships), object template</td></tr><tr><td>Same-time, different-place</td><td>WYSIWIS, review missed events (log finder), public/private</td></tr><tr><td>Different-time, different-place</td><td>organize information (object folders), group memory (log player and finder)</td></tr><tr><td>Medium</td><td>sketch, list, and table views</td></tr><tr><td>Structure</td><td></td></tr><tr><td>Setting up a project/session</td><td>usage controls, representation model (object template)</td></tr><tr><td>During a project/session</td><td>‘look here’, select view, WYSIWIS, object locking, timed refresh, organize (object folders and relationships)</td></tr></table>

## 4. COWS research prototype

To investigate further our ideas of integration, we prototyped a collaborative system called Collaborative Object Workspaces COWS . The goal of the Ž . COWS project is to create an architecture and representation metaphor that can provide integrated support for most, if not all, the collaborative work activities of teams. Research has only recently started looking at the issues involved in creating all-purpose designs 12 . Previous efforts tended to limit their focus to specific tasks e.g., shared drawing or deci- Ž sion-making meetings or specific time–place quad- . rants e.g., same-time, different-place .Ž .

COWS is a 32-bit client server Windows-based information sharing tool that supports controlled and free-form sentential-, sketch-, and table-based interaction on shared and private objects. COWS operates on local and wide area networks using TCP<sup>r</sup>IP sockets. COWS is currently in use in a pilot project and has been demonstrated at several conferences <sup>w</sup> <sup>x</sup> 5,7 . The software was designed in Microsoft Visual Basic version 4.0<sup>r</sup>5.0e. TCP<sup>r</sup>IP connectivity and low-level drawing features are provided by thirdparty components. Many of the individual ‘‘features’’ are based on old e.g., the shared whiteboard andŽ . new e.g., recordable memory ideas in CSCW re-Ž . search. The most basic element in COWS is the object. Objects have properties e.g., title, sentences,Ž graphics, and links to external documents and meth-. ods e.g., add, edit, group, sort, merge, and vote . Ž . Users work in the same object-based environment from beginning to end. Table 1 shows the basic attributes of COWS based on mode, medium, and structure. Table 2 describes the individual features.

A session is established when the session initiator creates it. Any user can start, save, and reload a session. When a user starts a session, it automatically takes on the server role for others the server code isŽ integrated into all the clients . This means that teams. can choose a centralized server strategy or follow a more flexible distributed approach in which any team member starts a session. Figs. 2 and 3 show the current set of object containers e.g., shared objects,Ž participants, log book; see the left side of the win-. <sup>6</sup> dow . Containers of objects are further grouped in folders see Fig. 2; shared objects . Objects areŽ . manipulated in Õiews. A view is opened in the right-hand pane of Fig. 2 by clicking on the appropriate toolbar button figure shows a list view .Ž . COWS currently supports three views: Sketch Ž . layered object-based drawings , List, and Table Ž . organized lists . All the views are WYSIWIS ‘‘live’’ in that data are updated in real time or by a refreshŽ command . All the views reference the same data. Ž . data integration . The views are also accessible simultaneously by opening multiple workspace windows a limited form of presentation integration . Ž .

Table 2  
COWS feature description in order of appearance in Table 1 Ž .

<table><tr><td>COWS features</td><td>Description</td></tr><tr><td>Quick entry</td><td>enters small text fragments quickly</td></tr><tr><td>Object folders</td><td>labeled containers for multiple objects</td></tr><tr><td>Object relationships</td><td>named association among objects (depicted by arrows in sketch view)</td></tr><tr><td>Representation model (object template)</td><td>selects or creates an object template so individual objects can be categorized (e.g., rectangles represent questions, circles represent options)</td></tr><tr><td>WYSIWIS</td><td>“what you see is what I see” updating of data</td></tr><tr><td>Log finder</td><td>a standard database type of list of all previous events in a session</td></tr><tr><td>Public/private</td><td>objects can be placed in public or private workspaces</td></tr><tr><td>Log player</td><td>allows play back of events in the past; the user can step back and forth through the events of the selected session</td></tr><tr><td>Sketch view</td><td>layered object-based drawing</td></tr><tr><td>List view</td><td>simple lists</td></tr><tr><td>Table view</td><td>organized lists</td></tr><tr><td>Usage controls</td><td>allow object add, edit, move, open, restrict available view</td></tr><tr><td>“Look here”</td><td>selects an object and invites some or all users to “look” at an object;a new window containing a flashing object appears on the screen of targeted users</td></tr><tr><td>Object locking</td><td>if a particular object is in use, then the object is locked and color coded</td></tr><tr><td>Timed refresh</td><td>sets the frequency with which the public window is updated</td></tr></table>

Fig. 3 shows an open workspace with shared objects in the Sketch view.

To summarize, COWS supports face-to-face work by providing a convenient and quick ‘‘verbal’’ interaction environment through a list view that has quick entry features. Distributed asynchronous work is supported because all activities are automatically recorded and available through a log player and log book described further below . Distributed syn-Ž . chronous work is supported through the high-awareness drawing environment of a WYSIWIS sketch view and a ‘‘look here’’ command. The transition between ‘‘modes’’ is seamless. Content structure is supported through a template feature that allows data to be categorized and also through the availability of multiple work surface layers. Process structure is supported by controls to restrict functionality. The remainder of this paper discusses COWS in the context of design and behavioral propositions.

![](/api/attachments/DD5DH4AM/fulltext/images/b60549053d72cfa6eb52a200714da45f6d54f513a344a3ab206bb72d87b26b77.jpg)  
Fig. 2. List view.

![](/api/attachments/DD5DH4AM/fulltext/images/27710e4bfc58fe0432ddda0b330832320a42973c00bb5c0720bbcf33005e5285.jpg)  
Fig. 3. Sketch view.

## 5. Design propositions

The design propositions were created as part of the prototyping process depicted in Fig. 1. These propositions are strategic in that through the prototyping process, we have eliminated other technical approaches to the problem. The propositions outlined below passed our practicality and releÕance tests. In other words, they are not only doable but that the initial evidence suggests that the propositions may also reflect artifacts that will prove useful.

## 5.1. An integrated system will combine multiple modes of work

We were able to formulate this proposition by creating support in COWS for the following scenarios: same-time, same-place; same-time, differentplace; and different-time, different-place. The ‘‘combining’’ was accomplished as follows.

<sup>Ø</sup> When a user logs on, new and changed objects are highlighted. This means that users can work across modes without worrying about losing touch with key events.

<sup>Ø</sup> If other users are on-line, then their presence is indicated and their work updated in real time on the shared public object folder. This means that coordi-Ž . nation and update problems of working in different modes are avoided.

<sup>Ø</sup> The WYSIWIS updating of data in real time also increases awareness. In the same-time, different-place situation, there is a need to coordinate work with others since none of the common face-toface physical cues is available. When an object is moved in the sketch, it is also moved on the screens of all the other participants. The WYSIWIS is there when needed; it does not place any special demand on other modes.

<sup>Ø</sup> A quick-entry dialog box allows participants to quickly enter small fragments of text. In a same-time, same-place or different-place situation, participants Ž . may generate a large quantity of discrete small-size data e.g., ideas in a brainstorming session . ForŽ . example, Dennis et al. 1 report that participants in a <sup>w</sup> <sup>x</sup> meeting type in as much as one comment with anŽ average length of 22.7 words every 1.75 min. The.

quick-entry dialog box can be called when needed and allows us to integrate the unique needs of faceto-face interaction with the rest of the system.

<sup>Ø</sup> Different-time, different-place users may need to catch up with what has transpired so far. The log book see Fig. 4a is used to look for specific events,Ž . the Log player see Fig. 4b will play back in realŽ . time all the past events in the session using a VCR metaphor.

<sup>Ø</sup> During same-time, same-place situations, the log book may be useful to locate specific items of interest or the log player to catch up when somebody walks in late. Participants who happen to miss an event because they were distracted for a few seconds can quickly review events in the log book see Fig.Ž 4a ..

<sup>Ø</sup> Participants working out of sync with one another may need very organized ways with which to share information. Text is organized by categorizing through object templates see Fig. 5 , by group-Ž . ing objects in folders, and by forming relationships among objects.

<sup>Ø</sup> The WYISIWIS, quick-entry, log book, log player features are not tied to particular modes. They

![](/api/attachments/DD5DH4AM/fulltext/images/cbed6dcb2bac3254eff5166ead6c864c8a6f0159d8a5ab04080e0ce98dad12f8.jpg)  
Fig. 4. a Log book. b Log player. Ž . Ž .

![](/api/attachments/DD5DH4AM/fulltext/images/ab070c63bb641ecd4511576efdf4e477d54996ebed86b1051b245c810a4a640a.jpg)  
Fig. 5. Adding a new object type into the object template.

are always there, further producing the sense for the user that they are in a seamless environment with respect to mode of use.

## 5.2. An integrated system will combine multiple media

The representation of collaborative work remains an open question. Early systems experimented with drawing surfaces 13 and sentential text 11 . Sev-<sup>w x</sup> <sup>w x</sup> eral modern systems focus on hypermedia 14 or<sup>w</sup> <sup>x</sup> documents 4 as the underlying metaphor. However,<sup>w</sup> <sup>x</sup> it is natural for people to exchange information using all the above schemes — as sketches, small sentence fragments, lists, tables, links, and documents. Clearly, there is a need to integrate the media. We were able to formulate this proposition by presenting information in integrated sketch, list, and table views. The ‘‘integration’’ was accomplished as follows.

<sup>Ø</sup> The views provide different representations of the objects. The underlying data are the same dataŽ integration ..

<sup>Ø</sup> The sketch is the richest view; complex relationships are represented by connecting lines or by groupings object. Lists are better suited for working with large quantities of data. Tables are the most restrictive and work well for certain types of organized lists. This means that users can use each view for its distinctive properties without having to import or rekey data.

<sup>Ø</sup> Since the underlying data are integrated, the user can switch back and forth among appropriate views. For example, one task may require a list view; the same task at a later stage in time may need a sketch view. This means that users get the sense that their data are always there wherever they happen to be in the system.

## 5.3. An integrated system will combine multiple structuring techniques

Structures support group development and productive outcomes. For example, some systems support cognitive-mapping structures. Others focus on anonymity and consensus building through voting and commenting. An integrated application will combine support for at least two distinct structures. We were able to formulate this proposition by integrating process structures such as access control and concurrency control with content structures such as categorization. The ‘‘integration’’ was accomplished as follows.

<sup>Ø</sup> Project leaders restrict the use of the software by limiting the ability of users to add, move, edit objects, and so on see Fig. 6 . The restriction is Ž . integrated into all the available views and all the modes of work. These settings can be changed at any point during a session.

<sup>Ø</sup> The project leader can select a representation model for the objects. For example, decide that only two types of objects will be available to users e.g.,Ž idea and comment . These object categories apply. across all the available views. For example, in the sketch, the categories will appear as different shapes Ž . e.g., all ideas as circles, all comments as rectangles .

![](/api/attachments/DD5DH4AM/fulltext/images/a97b8d01f1cbd068c5a564c7854e1932728a394dee793aab2ca225c75b4c6c32.jpg)  
Fig. 6. Setting usage controls.

The object template can be modified at any time. Fig. 5 shows an example of manipulating an object template.

<sup>Ø</sup> During a session, if an object is in use, then it is locked and color-coded. We integrated the locking across the available views and it works independently of the mode in which other users are operating. If there is no one else on-line, no action is taken. If there are other users on-line, the selected object is locked. If another attempt is made to edit the object immediately, then a message is sent to the user holding the lock indicating that somebody else wants the object. At that point, the lock can be given up or the two users in question can initiate a ‘‘chat’’ session with the chat utility.

![](/api/attachments/DD5DH4AM/fulltext/images/3a6cb51f4c35604434ad9427bc71b1093116a162d67186507db178cdb2bb62bc.jpg)  
Fig. 7. ‘‘Look here’’ command.

<sup>Ø</sup> When more focused collaboration is desired, awareness of others is increased by changing the available views and operations on objects. For example, lists offer a more restricted view of information than a sketch view.

<sup>Ø</sup> At the object level, each user can select an object and issue a queued ‘‘look here’’ to invite some or all users to ‘‘look’’ at the selected object Ž . see Fig. 7 . A new window containing a flashing object appears on the side of the screen of targeted users. The window disappears if the user does not click the window in a few seconds. We were also able to integrate this feature across all modes of work. If only one other user is on-line, then only that user gets the look here message.

## 6. Behavioral propositions <sup>7</sup>

The general theory underlying our behavioral propositions is that complex collaborative work will benefit more from integrated systems than the equivalent sum of features offered in non-integrated applications. Initially, users will find it harder to use and understand integration. Integration will also lead to new behavioral patterns that we might call ‘‘integrated behavior.’’ We generated the behavioral propositions by using successive versions of our prototype. The propositions listed below pass our tests of practicality and releÕance. The usage was informal and consisted of a usage by the develop-Ž . ment team the authors of this paper ; b observa-Ž . Ž . tion of people in our work environment that would come in to see our work and try out the prototype; Ž .c observation during public demonstrations in which users would be able to ‘‘drive’’ the application; dŽ . use in an advanced graduate class in which students had to use the software in distributed mode; and eŽ . through an exploratory study involving 12 students in an introductory graduate course. The software was demonstrated to the group and then each student was assigned a mini-task involving the use of the software. At the end, a questionnaire was administered and the subjects were interviewed. The propositions are listed and elaborated further below.

<sup>Ø</sup> Users will prefer integrated collaboratiÕe features when compared to the equiÕalent set of features offered in non-integrated applications.

Users in our exploratory study were asked to indicate their preference for either the sketch or list view as being the only available view. One selected the list view, two others selected the sketch, the rest Ž . nine users indicated that they would prefer to use both. The results suggest that users will take advantage of the capabilities provided in integrated software. Given that we had already constructed this feature, the proposition passes our practicality test. The relevance test was passed because each user had a preference as opposed to selecting the ‘‘do notŽ care’’ choice on the questionnaire . Computing liter-. ature on graphs vs. tables and interface consistency may prove useful in further exploring this proposition. Economic and marketing theory on packaging may also provide additional insight in explaining the reasons for the preference for integration.

<sup>Ø</sup> An integrated collaboratiÕe application is harder to use for simple tasks than the equiÕalent set of features offered in non-integrated applications.

<sup>Ø</sup> An integrated collaboratiÕe application is easier to use for complex tasks than the equiÕalent set of features offered in non-integrated applications.

<sup>Ø</sup> An integrated collaboratiÕe application is harder to initially understand than the equiÕalent set of features offered in non-integrated applications.

We developed these propositions primarily in response to watching our informal users and from their feedback. Most users had trouble operating the software when they were first introduced to it. We would typically introduce the software using simple tasks such as brainstorming or flowcharting. Several users remarked, after we had walked them through some of the high-end features, that they would find them useful for complex tasks. In our exploratory study, we probed this issue further by asking participants whether they thought the individual views were better suited to certain tasks. A little more than half 58% agreed, while the rest were unsure, only aŽ . small percentage disagreed. Our assumption was that people who could map tasks to views would reflect a good understanding of the software and how to use it. Given that a large percentage of the subjects was unsure all subjects were expert computer users , weŽ . decided that we needed to think carefully about relevance. We then developed a more complex scenario a human resources hiring task and starting Ž . using that in our demonstrations. Changing the task changed the tone of the feedback and usage. Although the upfront time to explain the task was longer than for the simple tasks, we found that users would have less trouble understanding how to operate the software and were more appreciative of the features. To summarize, the propositions pass the practicality test because the software can support complex tasks. One of the key features in this context is the use of folders to hold and organize larger quantities of information. The folders are available in all the integrated modes, media, and structures. The propositions pass the relevance test as they are generated in response to user feedback. End-user computing theory on ease of use and software training can be used to further test the above propositions.

<sup>Ø</sup> Integrated collaboratiÕe applications will result in ‘‘integrated’’ behaÕioral patterns.

This was an unexpected proposition in that we had conceptualized our work as primarily impacting range of capabilities and ease of use. However, after using the software for a while, we began to observe what one could call integrated behavior. For example, distributed students log-in to the system and expect to work asynchronously, they happen to find other users on-line and start working with them in a synchronous manner. Later, these users ‘‘disband’’ and work for a while asynchronously and then spontaneously ‘‘meet’’ again in a few minutes for synchronous work. We had originally imagined that the integrated features would be used in a more timeand work-delimited manner. This proposition meets the practicality test in that it is feasible to do the above, though if we had more confidence on the relevance, there would have been ways to modify the software to further facilitate such behavioral integration. However, we are not convinced that the proposition has passed the relevance test. Perhaps the behavior we observed was simply exploration on the part of students. Moreover, we are also unclear on the theoretical basis for such behavior, though structuration theories may help explain the appropriation of features for other than their intended use.

## 7. Discussion and conclusion

The next step in our research is to start envisioning an empirical study that will allow us to study integration. However, we believe that the results of our prototyping research process in the form of design and behavioral propositions represent a complete unit of research that stands on it own. The ‘‘usage’’ component of our prototyping research process has allowed us to consider the type of future study that would prove most value. A laboratory experiment, for example, does not seem appropriate. A laboratory experiment would, by default, involve simple tasks and little opportunity for new behaviors to emerge. An observational method holds more promise. It is also important to note that there are uncountable design and behavioral propositions that we discarded on our way to the list of propositions presented in this work. For example, conducting an experiment around the hypothesis, that integration increases usability, seems now to be clearly the wrong question.

This paper represents a first attempt to define and understand the issues surrounding the integration of collaborative technologies in which we used prototyping as a research methodology to identify strategic design and behavioral propositions. The main contribution of this paper is in presenting a working definition of integration along with a research prototype that integrates collaborative features in the dimensions of mode quadrants of the time–place ma- Ž trix , medium text and sketches , and structure con-. Ž . Ž tent and process . We also believe that our methodol-. ogy will prove useful to researchers who are interested in working on questions that are relevant and practical.

## References

<sup>w</sup> <sup>x</sup> 1 A. Dennis, J. Nunamaker, D. Vogel, GDSS laboratory experiments and field studies: closing the gap, Proceedings of the Hawaii International Conference on System Sciences Ž . HICSS , 1989, pp. 300–309.

<sup>w</sup> <sup>x</sup> 2 R. Dubin, Theory building in applied areas, in: M.D. Dunnett Ž . Ed. , Handbook of Industrial and Organizational Psychology, Rand-McNally, Chicago, IL, 1976.

<sup>w</sup> <sup>x</sup> 3 D.C. Engelbart, W.K. English, A research center for augmenting human intellect, Reprinted in: I. Greif Ed. , Com- Ž . puter-Supported Cooperative Work: A Book of Readings, Morgan Kaufman Publishers, CA, 1988.

<sup>w</sup> <sup>x</sup> 4 J. Fowler, D. Baker, R. Darghi, V. Kouramajian, H. Gilson, K. Long, C. Petermann, G.A. Gorry, Experience with the virtual notebook system: abstraction in hypertext, Proceedings of the Conference on Computer-Supported Cooperative Work CSCW , 1994, pp. 133–143.Ž .

<sup>w</sup> <sup>x</sup> 5 S. Khan, M. Mandviwalla, Collaborative Object Workspace Ž . COWS . Software Demonstration, ACM Computer-Supported Cooperative Work Conference CSCW , Boston,Ž . November 16–20, 1996.

<sup>w</sup> <sup>x</sup> 6 T. Kuhn, The Structure of Scientific Revolutions, 2nd edn., University of Chicago Press, Chicago, IL, 1970, Enlarged.

<sup>w</sup> <sup>x</sup> 7 M. Mandviwalla, S. Khan, Studying the integration of technology with Collaborative Object Workspaces COWS , Pro-Ž . ceedings of the ACM Computer Personnel Research Conference, 1997, pp. 181–186.

<sup>w</sup> <sup>x</sup> 8 M. Mandviwalla, L. Olfman, What do groups need? A proposed set of generic groupware requirements, ACM Transactions on Computer–Human Interaction 1 3 1994Ž . Ž . 245–268.

<sup>w</sup> <sup>x</sup> 9 M. Mandviwalla, P. Gray, L. Olfman, The meta environment: a new group support system structure, Journal of Organizational Computing and Electronic Commerce 7 1Ž . Ž . 1997 35–55.

<sup>w</sup> <sup>x</sup> 10 M.L. Markus, D. Robey, Information technology and organizational change: causal structure in theory and research, Management Science 34 1988 583–597.Ž .

<sup>w</sup> <sup>x</sup> 11 J.F. Nunamaker, A. Dennis, J.S. Valacich, D.R. Vogel, J. George, Electronic meeting systems to support group work, Communications of the ACM 34 7 1991 40–61.Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 M. Sohlenkamp, G. Chwelos, Integrating communication, cooperation, and awareness: the DIVA virtual office environ-

ment, Proceedings of the Conference on Computer-Supported Cooperative Work CSCW , 1994, pp. 331–343. Ž .

<sup>w</sup> <sup>x</sup> 13 M. Stefik, G. Foster, D. Bobrow, K. Kahn, S. Lanning, L. Suchman, Beyond the chalkboard: computer support for collaboration and problem solving in meetings, Communications of the ACM 30 1 1987 32–47.Ž . Ž .

<sup>w</sup> <sup>x</sup> 14 N.A. Streitz, J. Geibler, J.M. Haake, J. Hol, DOLPHIN: integrated meeting support across local and remote desktop environments and liveboards, Proceedings of the Conference on Computer Supported Cooperative Work CSCW , 1994,Ž . pp. 345–357.

<sup>w</sup> <sup>x</sup> 15 J. Walls, G. Widmeyer, O. El Sawy, Building an information system design theory for vigilant EIS, Information Systems Research 3 1 1992 36–59.Ž . Ž .

<sup>w</sup> <sup>x</sup> 16 R. Weber, Toward a theory of artifacts: a paradigmatic base for information systems research, Journal of Information Systems Spring 1987 3–19.Ž .

Munir Mandviwalla is Associate Professor of Computer and Information Sciences at Temple University. His current research interests include the requirements, design, and use of collaborative systems and communication technologies, the role of technology in large-scale professional conferences, and the process of scholarship. Dr. Mandviwalla has published more than 35 articles in scholarly journals and international conferences including MIS Quarterly, ACM Transactions on Computer–Human Interaction, Information Systems Journal, Journal of Organizational Computing and Electronic Commerce, and Information Technology and People. His work has been supported by grants from the National Science Foundation NSF , Bell Atlantic, Microsoft, CIGNA,Ž . Lotus Development, and Lilly Endowment.

Shariq Khan is the Lead Systems Developer at Proscape Technologies, a Philadelphia-based software development company that specializes in Sales Force Automation software. He is the leading the architecture and development team of Proscape Salesgode and Salesgod Server for NT. Salesgod Server is a multithreaded data-synchronization server that allows different systems of Salesgod to transparently exchange data and information over wide and local area networks. Shariq also designed and developed the Salesgod Continuous-Learning and Presentation Systems with DataTrackinge that allows organizations to present and track multimedia presentations on a desktop or over the web using a standard browser. He also took part in the development of COWS, a software that enables users to collaborate in real time using an object metaphor over standard TCP<sup>r</sup>IP. He has been a co-author in several publications relating to this project and won an ‘‘Outstanding Project and Student’’ award in the ACM Computer Science Conference, Philadelphia, 1996.
