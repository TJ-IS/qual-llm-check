---
otero_id: 17536
otero_key: "TE5UJZDF"
title: "Facilitating space-time differences, group heterogeneity and multi-sensory task work through a multimedia supported group decision system"
authors: "Christian Wagner"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00061-v"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Facilitating space-time differences, group heterogeneity and multi-sensory task work through a multimedia supported group decision system

Christian Wagner \*

Department for Information and Operations Management, School of Business Administration, University of Southern California, Los Angeles, CA 90089-1421, USA

## Abstract

Group work outside of the decision laboratory exhibits several interesting characteristics. Communication is frequently off-line, particularly if individuals are geographically separated. Group members have different backgrounds (e.g., in focus groups, mixed customer and company groups) and do not necessarily share the same information or values. Tasks can have significant visual and auditory components, as for instance in product development. While these characteristics are by no means exclusive, they represent important factors which now can be addressed by multimedia supported group decision systems.

The article discusses these and related aspects of group decision making and explains design alternatives to handle them. Proposed technology solutions include a multimedia group communication and e-mail facility, a visualization tool (“virtual tour guide”), a multimedia directory, and a problem structuring tool. The software tools have been recently developed. Some initial experiences with the technology are also presented.

Keywords: Multimedia; Group decision support; Teleconferencing; Problem solving

## 1. Background and overview

## 1.1. Group decision support and multimedia

A recent article by Bly et al. [1] describes experiences with a media space, a virtual room that connects individuals at two different sites through an on-line low bandwidth videolink. The purpose of this setup was, aside from exploring the technology, to see whether group unity could be maintained. The most common use of the media space was found to be the playful monitoring of events in the other site's common area ([1], p. 34). Thus, while without immediate business purpose, the application illustrates one powerful use of multimedia for groups, the removal of distance barriers. The media space almost completely eliminated the distance barrier as it operated via a dedicated line, sending data not "on command" but continuously. Of course, the basic technology used at the site is not new (TV broadcasting has existed for decades). New is the ubiquity of sending devices, receiving devices and communication links which permits peer-to-peer transmission of multimedia data at almost any time and from several points within the organization, thus changing the nature of group communication. Still, this is not group decision support, since its focus is not on aiding the group in a problem solving task and since it does not provide task support in form of problem structuring and idea processing techniques.

A natural extension to this form of teleconferencing is, therefore, the use of multimedia within the computing environment, as part of multimedia supported group decision systems. The current generation of group decision support systems still separates between the use of computers for textual data and the use of other devices (e.g., VCR, overhead projector) for multimedia data. Requirements and implementation considerations for multimedia supported software are therefore going to be topic of this article.

## 1.2. Essence of multimedia supported group decision systems

Most present group decision support systems contain two technologies which create important capabilities: telecommunications and database. The telecommunications function results in any-place capability. Distances are becoming irrelevant, allowing users to share the same electronic workspace, whether in a face-to-face meeting or physically distant from each other. The database adds any-time capability. It permits users to work in different-time mode (asynchronous) as well as in same-time mode, and in addition establishes an organizational memory.

The use of multimedia in group decision systems adds another important dimension, namely the ability to generate virtual (work) environments. With multimedia, the stored or transmitted message preserves so many characteristics of the object which it represents, that the receiving user perceives the image as a “virtual reality”. Thus, while for instance electronic mail bridges a distance gap, multimedia electronic mail creates a virtual-same-place appearance.

Any-place, any-time, and virtual environment are capabilities that need to be discussed in detail. To this end, the article is organized as follows. The remainder of this section is dedicated to an explanation of the group decision support framework underlying the research. The next section describes several group decision support needs, the majority of which is not addressed by current technology or existing frameworks (e.g., [2], Fig. 1, [3], Fig. 1). These needs were identified in problem solving sessions and through discussion with problem owners, focusing on tasks such as product development and continuous product/process improvement. A subsequent section discusses implementation characteristics which satisfy these needs. Finally, some early experiences with the software are outlined, followed by conclusions.

![](/api/attachments/TE5UJZDF/fulltext/images/c91dd5e38970ab640faaf072c37d210389bb6fa946fff8aebb7113889252deaf.jpg)  
Fig. 1. Group decision support framework.

## 1.3. GDSS framework

Driving this research was the goal to develop technology which overcomes difficulties associated with collaborative work. The research is based on a model of group decision support which recognizes the impact of the task, the group, the individuals who make up the group, the context of the meeting, structural factors influencing the meeting, facilitation, and technology. The model, which draws on and shares significant characteristics with Refs. [2], [4] and [5], is depicted as a block diagram in Fig. 1. The figure exemplifies each component through several important characteristics.

Four components of the framework are of particular relevance for this research. First, the visual or auditory nature of tasks is addressed within task characteristics. Second, differences in group member knowledge and values are subsumed under individual characteristics. Third, space and time disparities are recognized as meeting structure related factors. Decision making hindrances created by these factors are to be compensated through advances in the fourth factor, technology.

## 2. Tasks, task requirements, solutions

## 2.1. The nature of group work: Is it text based?

Previous research on group decision support has described a large variety of tasks which were successfully carried out in text based environments (e.g., [4]). In these tasks, individuals expressed their ideas on how to solve a problem verbally. Yet verbal descriptions are not always adequate. For instance the development of new products incorporates large amounts of originally non-textual information. Product features need to be expressed and compared, packaging analyzed, advertisements need to be assessed. Much of this effort is visual, some affects other senses (food odor and consistency, or car engine sounds are just two examples). Representation of this information through verbal means can be lengthy (“1000 words”) and awkward. Although we can do little at this time to represent odors (smell, taste) and consistency (touch) in computer environments, sound and visual images are easily managed. Yet in text based group decision support systems, only text sharing is decentralized and “democratic”, while multimedia information is handled centrally through non-computerized devices (VCR, overhead, sound equipment). Thus, sharing of opinions through non-textual data can only take place with difficulty. The incorporation of multimedia into group decision support software overcomes this limitation. Group members can consequently support alternate opinions through sound and visual impressions. This democratization of multimedia communication is not entirely problem-free however, since the broadcasting of media clips by individuals may disturb the group process. If “flaming” is a problem with text based group technology, “multimedia terror” can be a problem in multimedia environments. Disgruntled individuals could for instance “pollute” the environment by repeatedly broadcasting sound clips. Thus, controlled sharing of multimedia images will have to be a design goal for the technology.

## 2.2. Heterogeneous groups

Group work may bring together individuals from various backgrounds. For example, product developers will meet with lead users of their product to brainstorm for new ideas. Alternatively, members from different organizations will meet to work on a joint project. The heterogeneity in these groups is not an undesirable side-effect of collaborative work. On the contrary, it is important for successful group work that individuals with non-identical views ([6], [7]) and complementary sets of knowledge ([8]) are assembled. A different viewpoint represents additional information which the group has to incorporate into its decision. A broad knowledge base distributed among the group membership lessens a group's reliance on the best member. However, an assembly of individuals is not a group, and output of such a quasi-group is rarely superior to the results produced by the best group member (e.g., see [9]). Furthermore, the lower the group cohesiveness, the higher is the variance in productivity within the group [10]. To assure that the individuals assembled for the problem solving task behave like a group, they either have to have a history as a group or have to go through a development process (e.g., [11]), part of which is the identification of shared values and goals.

To support heterogeneous groups, one will therefore need to provide task related factual information, e.g., about the product, the organization, as well as information to facilitate group cohesiveness building. Both needs can be supported through multimedia. Examples include the provision of factual information through sound, picture, or video clips, as well as the communication of values through joint experiences in a virtual world (e.g., joint participation in computer/video entertainment). For example, the Group Decision Program ([12]) contains an interactive narrator video sequence, stored on videodisc. The narrator explains the problem solving process. Such a system could be extended to contain also video information concerning the task environment and the task itself.

## 2.3. Overcoming space and time differences

Group problem solving is practiced almost everywhere, yet most organizations do not have computer equipped group decision rooms. Many smaller firms perceive they do not have the resources to bring all key employees to a remote decision room for a day or so. Larger firms which possess the resources are often geographically so dispersed that a common meeting place is difficult to arrange.

A problem arises when a key employee is unable to attend a group meeting and later is unwilling to accept decisions made at the meeting due to a lack of perceived ownership of the decisions. This situation was encountered when a key employee of a European car manufacturer was unwilling to “buy into” a decision regarding the development of a new product, only because he had not been able to voice his opinions at an off-site brainstorming session. In such a case, forms of remote on-line communication (e.g., teleconferencing) may be possible, but become difficult for instance if individuals do not have immediate access to a communication facility or if they are located in different time zones. For example, the US Army’s teleconferencing facilities were used below expectation, since users had to go to a studio and thus leave their offices which is contrary to Army culture ([13]). Time barriers become especially significant when intercontinental communication is desired. Unless located at America’s west coast, decision makers need to significantly extend their workday forward or backward to communicate with other economic centers in Europe and south-east Asia. Thus, the MIRROR room’s vision ([14], Fig. 1) of simultaneous on-line communication with Japan, Paris, and London will likely be an exception.

An alternative solution is the use of off-line communication, where individuals leave messages for the rest of the group in asynchronous mode (as in e-mail or voice mail). To do this effectively, the absent group member has to know how the group process will unfold. Otherwise it will be very difficult for that individual to make appropriate suggestions. While those present at the meeting will be able to rely on instant feedback to shape new ideas, absent individuals can only rely on feedforward information. But how can feedforward information be provided when none of the group participants knows in advance the direction the group discussion will take? One successful approach is the use of formal problem solving process tools. All problem solvers have to agree on solving the problem by using the same steps and the same documentation. Examples of this technique are the Kepner-Tregoe method ([15]) which formalizes problem analysis methods (e.g., “problem analysis”, “potential problem analysis”) or Xerox’s “Leadership through Quality” and “Competitive Benchmarking” method ([16]), also with formal techniques and documentation. Xerox executives have to use these techniques for planning processes through the company’s executive support system ([17]). Once the decision makers agree on a common problem solving process structure, results, whether generated on-line and off-line, will be shared more easily. If the process is implemented in software, adhering to it will require only little effort.

Despite the above comments on off-line communication, there is no doubt that on-line communication will play a major role in group decision support. Several current developments demonstrate the importance of this form of communication (e.g., [13], [18], [19]). Off-line communication will be an alternative, when on-line communication is impossible or undesirable (similar to voice mail as an important substitute to direct phone conversations). Several authors explain the value of both types of communication (e.g., [20], [21]). Morrison points out that group problem solving can be a lengthy process which incorporates phases of face-to-face communication and phases in which individuals access the organizational memory in asynchronous mode.

## 2.4. Summary

The section has illustrated several requirements for group decision support outside of the decision laboratory. One priority need is improved multimedia communication for non-textual problem solving tasks. This change in the communication structure has to be realized without a complete loss of central control. Another key need is group development in heterogeneous groups, which in part can be facilitated through the sharing of knowledge and values. A third important need is the ability to purposefully communicate off-line, realization of which requires feedforward information on the structure of the problem solving process. All of these requirements will be addressed by implementation characteristics discussed in the next section.

## 3. Implementation

This section describes specific multimedia technology solutions to key group decision support needs. The technology solutions include a multimedia communication facility, visualization tools, and a problem structuring tool. Table 1 outlines the relationship between needs and implementation features.

## 3.1. Multimedia group communication and Email facility

Overall structure. A key element of the software is the multimedia communication facility. Similar to traditional group decision support software, it permits sending messages peer-to-peer and in broadcast mode to a shared large screen. Messages in the multimedia environment are objects consisting of a text component, together with optional sound, still picture, and video components. The text component consists of the sender's address, the receiver's address, a message title, and a message text body. The sender's address is optional to permit anonymity. Message titling is made available to let the receiver overview all messages before reading them individually. This is particularly important in off-line communication where multiple messages will be waiting to be read.

Table 1  
Group support requirements and technology solutions

<table><tr><td>Requirements</td><td>Requirements detail</td><td>Technology solutions</td></tr><tr><td rowspan="2">Off-line communication</td><td>Ability to store and forward off-line messages</td><td>Multimedia communication and Email</td></tr><tr><td>Synchronization of on-line and off-line work</td><td>Problem solving structuring facility</td></tr><tr><td rowspan="2">Multisensory communication</td><td>Peer-to-peer/broadcast multimedia communication</td><td>Multimedia communication and Email</td></tr><tr><td>Avoidance of “multimedia terror”</td><td>Receiver controlled play-back of multimedia</td></tr><tr><td rowspan="2">Group development</td><td>Development of a common core of information</td><td>Multimedia directory</td></tr><tr><td>Development of shared values</td><td>Visualization tool</td></tr></table>

![](/api/attachments/TE5UJZDF/fulltext/images/3e2c903ed2b8511bf7bd90ccf676b00e53c89a427ffe8d9c1b8de028c7280f73.jpg)  
Fig. 2. Communication control panel.

Components. The communication components are shown in Figs. 2–5. Fig. 2 depicts the communication control panel which alerts the user to new messages and launches send and receive modules. The module in the figure indicates one message waiting to be read. To read the message, the user would have to activate the receive module. Unless activated, the send and receive modules are hidden. The control panel is kept small, so that it occupies only a small screen area. Fig. 3 depicts the receive module with sender area, title area, text area and control buttons. The message displayed in the figure is on the topic of “product development cycles”. A button with an “ear” icon alerts the user to an enclosed sound file. Fig. 4 shows the send module with text input area, address selection area, multimedia selection button (Attach button) and various other control buttons. To create a multimedia object, the user attaches a sound, picture, or video file to the text component. Messages can be sent to a large shared display (Master), to individual users (address list), or to a special mailbox (Support) from which they are later forwarded to the master display. Fig. 5 shows the shared master display with sender area, broadcast text area and control buttons. The “eye” icon/button indicates that a graphic image is part of the message. The individual who controls the master display unit can then decide whether to show or discard the image. The rationale behind this feature is the avoidance of “media terror”. Any time a multimedia object is received, only the text portion appears immediately on screen. The presence of graphics, sound, or video is identified by a corresponding icon/button. Both the receive and the master module contain these multimedia player buttons.

![](/api/attachments/TE5UJZDF/fulltext/images/0f285135703f04e46d469af07d9b80264eca2ae41fc88d03546091486fb5f8ed.jpg)  
Fig. 3. Multimedia communication receive module.

![](/api/attachments/TE5UJZDF/fulltext/images/cc2f7fed021c99401c478fda79afe7addbb918bea6077671e67d1e10a8c32788.jpg)  
Fig. 4. Multimedia communication send module.

Message handling. To create message objects, senders can access the whole range of multimedia files available on the network system. Any file selected to become part of a message is duplicated and attached to the message. The receiver can later decide to keep a message with all its components, or to destroy it. The duplication protocol was chosen despite the possibility of an explosion of data volume and redundant copies, in order to give both sender and receiver ownership of their personal copy of the multimedia components. Should large groups need to be supported over extended periods of time, the protocol may ultimately have to be changed to one that is more efficient in terms of memory, i.e., a pointer representation.

Message titling and message forwarding. To facilitate purposeful off-line communication, messages contain user definable titles. Thus, a group member who is unable to attend a meeting can leave several messages for the group, organized by topic. When the group discusses a certain topic, the absent member's message can be broadcast to the other group members. Since usually any message sent to the shared screen is displayed immediately, the absent member will send messages to a support unit which later forwards them to the broadcast unit at the appropriate moments (see Fig. 6). The figure shows a message on the topic “performance –basic engine” with text and graphic component. It also lists the topics of three other messages (e.g., “small convertible”), each of which can be forwarded to the shared master display at the appropriate time.

Dynamic redesign of groups. In most cases, all group members using the same facility will work on the same problem. Yet there may be situations in which different sub-groups (“break-out groups”) work on different problems. To facilitate sub-group work, the system contains a re-definable address list for each station. Address lists can be modified such that a group member may only send messages to members of his or her sub-group. Alternatively, the feature allows for asymmetric communication links, e.g., one may receive messages from one individual but be unable to send to that individual, thus permitting interesting communication structures (chain, tree, sub-groups with only group leaders broadcasting results, and so on).

![](/api/attachments/TE5UJZDF/fulltext/images/bfe624ec378d06711809976367c0298cbd005bd50a81af46d4803fdcd3757cff.jpg)  
Fig. 5. Shared communication screen (“master display”).

![](/api/attachments/TE5UJZDF/fulltext/images/08551e2184cd67379b6c2d4ef9539985fd80c0ba15f2e540638f63c723d122f9.jpg)  
Fig. 6. Message forwarding facility.

Voting and recording of results. To facilitate choice aspects of group decision making, the software includes also a voting component. Results of all phases of the decision making process are recorded through a logging facility. Neither of these two features contains any multimedia components and is consequently omitted from the discussion here.

## 3.2. Visualization tool (“virtual tour guide”) and multimedia directory

Visualization tool. The creation of a common core of shared information and beliefs is supported in part by the system's visualization tool. The metaphor underlying the visualization tool is that of a tour. An example of a tour would be a company visit. The visitor can access different departments, see their physical location, communicate with members of the department, or read relevant documents. Each stop on the tour is represented by a screen image. Each screen can be part of multiple tours. Also, tours can be part of other, larger tours. The user can navigate forward and backward through each tour, can skip to the end of a tour, or “go home” to the beginning.

![](/api/attachments/TE5UJZDF/fulltext/images/87594f9336e5bbb15b2038d06ffe530fdb432f51134b05794c6dd03cf68a00ec.jpg)  
Fig. 7. Visualization tool (virtual tour guide).

Each screen is an object consisting of optional text, graphic, sound, and video elements (see Fig. 7). In addition, a screen may contain a dialog area. The dialog feature contributes most to the software's interactivity. It is similar to a database query facility with pre-defined queries. It typically contains a list of several questions. The user selects a question to which the system responds with the retrieval of multimedia data. The screen in Fig. 7 shows the production facilities of fictitious “ACME Motors”. The figure depicts a dialog area with two pre-defined queries on ACME's employment and environmental impact. Responses to the queries are multimedia components, e.g., a spoken answer.

The visualization tool has several advantages over comparable media such as taped video. It is a random access medium and is highly interactive. Due to the interactivity and random access capability, information can be hidden and made available only on request. Information can also be made available, as is here, in hyper-linked sequences. The visualization tool can be used at the individual or the group level.

Visualization helps to share information, such as “where is the marketing department located?”. It also helps to share values. For example, a video may display the CEO communicating the firm’s mission to the other employees.

Multimedia directory. The software user may simply want to retrieve data in the form “show me a Mazda Miata”, rather than retrieve data thematically with the visualization tool. For multimedia access of this kind, we use a multimedia directory (see Fig. 8). The user specifies a keyword, to which the system responds by retrieving all corresponding data entries. This may include multiple pictures, sounds, or videos. This feature is particularly useful in tasks such as product development where developers look at or listen to competitor products, before brainstorming about own new designs.

There are two forms of data access to the multimedia directory. First, “what you ask is what you get” for concrete objects, such as “Mazda Miata”. Second, for abstract concepts, such as “friendship” or “serenity”, the directory retrieves images that most closely resemble the concept.

![](/api/attachments/TE5UJZDF/fulltext/images/d9f9879d4f7ceacbb090e2b1213065e32d91d45a7cf2787af3d2fc194ad47676.jpg)  
Fig. 8. Multimedia directory.

![](/api/attachments/TE5UJZDF/fulltext/images/a485736a23d42a64fb775b93d13e6b1da9d15d4a490fa9620a438690f50fd90c.jpg)  
Fig. 9. Problem solving structure tool: Overview.

![](/api/attachments/TE5UJZDF/fulltext/images/014b30ce6844b205ac61c319fbfab1b663c6ba42204b6f04900e894b6855ed97.jpg)  
Fig. 10. Problem solving structure tool: Instruction screen.

The second form of retrieval was added, recognizing that multimedia data is significantly richer than text data and that it can have meaning to users far beyond its direct interpretation. This feature may be used for instance by marketing professionals to deliberate alternative methods of generating moods within an advertisement.

## 3.3. Process related problem structuring

Unless individuals at the group meeting and those who communicate off-line agree on the same problem solving process, data generated by the outsiders cannot be easily introduced into the group meeting. In other words, a common process is needed to help synchronize on-line and off-line group problem solving activities. There are several ways to achieve this. For example, all individuals may be trained in the same problem solving techniques (e.g., car manufacturers' continuous improvement procedures, or the Kepner-Tregoe problem analysis). The purpose of these methods is to formalize the process, to make all important data and assumptions explicit, and to help in the development of a problem model.

The structuring tool for this group support software is designed following continuous improvement concepts. The tool prescribes a problem solving process to the user. Figs. 9–11 contain an example. The first image (Fig. 9) shows all process steps. For each process step there exists a description screen (Fig. 10), and a worksheet screen (Fig. 11). The overall process structure includes steps such as “Monitor Problem and Environment” (Fig. 9, detailed in Fig. 10). Completion of each of these steps will require data input by the user, for instance concerning the current business environment (Fig. 11). All textual data is recorded in a database and can be later shown in different formats, including a single page summary screen. Although the process structuring tool has itself no intelligence, its method of asking users the “right” questions and recording answers makes it possible to easily share information. An individual can work off-line using the tool and then forward his or her comments to each of the process steps via the communication facility. With each message carrying a meaningful title, these comments can be made available at appropriate times during the group meeting.

![](/api/attachments/TE5UJZDF/fulltext/images/554541cd4414b84740d7e7fc663de92b6da7e26eb45d752997735c9ea58e5dd0.jpg)  
Fig. 11. Problem solving structure tool: Worksheet.

The process structure shown in Fig. 9 is by no means the only way to address a continuous improvement problem, let alone other problems. While one can observe common process steps and solution finding strategies in expert problem solving, there are many ways to address each problem at this general level. The key benefit of any reasonable structuring method will be its ability to elicit relevant problem information from the problem solvers and its ability to make potential solutions more obvious.

## 3.4. Technology requirements

The software has been written in Microsoft Visual Basic and Asymmetrix Toolbook, to operate in a Microsoft Windows 3.1 environment on a local area network. Windows provides all the basic multimedia capabilities needed for the implementation. The network (in our environment a Novell network) serves as a shared repository for all message files. The system does not require any database management system. All information is stored either in flat files, or in data structures which are part of the software. The most important technology requirement is multimedia standard compliance (graphics adapter, sound adapter, processor speed) by the connected machines.

One of the main advantages of a windowed implementation is the possible coexistence of multiple applications (compare $[22]$ for the value of windowing in group support). During a session, group members should have the ability to work individually on an application and at the same time launch messages to share ideas and findings. Yet in order to realize this goal, the standard screen size with a resolution of 640 by 480 pixels is barely sufficient. Another requirement is network speed (e.g., fast Ethernet), so that the transfer of multi-megabyte files does not result in unacceptable response time. Fortunately, all this equipment (including also video capture cards and cameras for PCs) is now available as off-theshelf technology, thus permitting the creation of low-end solutions for ubiquitous, collaborative multimedia computing.

## 4. Experiences

All the described software components have become available only during the last several months. Thus, no empirical results of their usefulness are available. Some early experiences are reported here in anecdotal form.

## 4.1. Problem structuring tool

The problem structuring component, by itself, was tried by members of a Japanese electronics company subsidiary in the U.S. The tool received positive reviews. The structure it provided together with the ability to look at all the compiled (textual) data in a single summary screen were viewed as key benefits. Some users indicated that they would not want to use the formal problem solving procedure suggested by the system for day-to-day problems, only for difficult non-routine situations.

4.2. Communication facility and problem structuring tool

The communication facility and structuring tool were used in another trial at the author's organization. Again, group member acknowledged the usefulness of the software, but it became obvious that the Windows environment was not completely intuitive. Due to the small size of the desktop, users were not able to view multiple applications simultaneously. Instead of just switching between applications, they exited one before entering another, thus slowing down the interaction significantly.

## 4.3. Visualization tool and multimedia directory

The visualization tool was demonstrated and tested at the author's as well other organizations, and was found helpful and easy to use. Several individuals commented on its potential additional value as a marketing tool to represent the organization or to build virtual shopping centers in which companies could occupy virtual real estate to advertise their goods and complete business transactions. The multimedia directory was applied in group product development session to retrieve data concerning existing products as the basis for discussion.

## 5. Conclusions and outlook

Advances in the basic technologies are making it possible to create low-end multimedia group decision software, affordable to most organizations. The richness of multimedia, compared with purely textual communication, will result in less need for physical face-to-face communication. Consequently, group decision making is likely to become more prevalent, even if decision makers are separated by time and distance barriers, or by different value sets and knowledge bases. Thus, group decision support may become an “any time”, “any place” process for most organizations. This can ultimately result in better decisions, since decisions of well working groups are superior to those of even the best individual group members. It can also result in a more broad ownership of decisions, as more individuals can help shape them, including individuals who would have been unable to attend a face-to-face meeting.

Nevertheless, the existence of the technology alone will not result in better group decision making. Group decision making with one vote for each individual and the ability to broadcast ideas anonymously is not the organizational routine. Thus, new forms of group decision making have to be found which can handle the potentially significant information load generated in group problem solving, and which can incorporate inputs of many organizational stakeholders while maintaining decision autonomy of key stakeholders together with organizational harmony. This will require for instance organization-wide training in problem solving procedures, so that all members of the organization become problem solvers, rather than simply problem messengers.

The existence of group technology will also be insufficient to change the nature of organizational problem solving if individuals are unwilling to participate in the process. Specifically, if they view this form of communication as a fad or as “not ready yet”, they will not make the investment in learning and using the technology. However, like electronic mail, this technology needs participation. And like electronic mail, it will also need to spread and mature, before it is going to used routinely. [1] give some indications of the nature of group communication in such an environment, where the technology is effortlessly available at any time and in many places, and where it is used in ways not foreseen by the developers.

## Acknowledgements

The research assistance of Chharlie Chau and Karen Phillips in implementing parts of the software is hereby thankfully acknowledged. David Flores of Mesa Research has been a collaborator on the process structuring software. The research has been supported in part by a grant from the National Science Foundation (SES-9016305).

The software discussed in this article is not a commercial product, but a research tool. None of the implementation descriptions in the article are meant to be advertisements. The software will be made available, upon request, to other researchers for further joint development and testing. Please contact the author for details.

## References

[1] S.A. Bly, S.R. Harrison, and S. Irwin, Media spaces: Bringing people together in a video, audio, and computing environment, Communications of the ACM, 36(1), pp. 28–47 (1993).

[2] J.F. Nunamaker, A.R. Dennis, J.S. Valacich, and J.F. George, Electronic meeting systems to support group work, Communications of the ACM, 34(7), pp. 40–61 (1993).

[3] G. DeSanctis, and R.B. Gallupe, A foundation for the study of group decision support systems, Management Science, 33(5), pp. 589–609 (1987).

[4] A.R. Dennis, J.F. George, L.M. Jessup, J.F. Nunamaker, and D.R. Vogel, Information technology to support electronic meetings, MIS Quarterly, 12(4), pp. 591–624 (1988).

[5] B.E. Mennecke, J.A. Hoffer, and B.E. Wynne, Group development and history in GDSS research: A new research perspective, Proceedings: 25th Hawaii International Conference on Systems Sciences, IV, pp. 113–124 (1992).

[6] L.R. Hoffman, Homogeneity of member personality and its effect on group problem-solving, Journal of Abnormal and Social Psychology, 58, pp. 27–32 (1959).

[7] L.R. Hoffman, and N.R.F. Maier, Quality and acceptance of problem solutions by members of homogeneous and heterogeneous groups, Journal of Abnormal and Social Psychology, 60, pp. 401–407 (1961).

[8] W. Watson, L.K. Michaelsen, and W. Sharp, W., Member competence, group interaction, and group decision making: A longitudinal study, Journal of Applied Psychology, 71(6), pp. 803–809 (1991).

[9] P.W. Yetton, and P.C. Bottger, P.C., Individual versus group problem solving: An empirical test of the best member strategy, Organizational Behavior and Human Performance, 29, pp. 307–321 (1982).

[10] A. Zaleznik, and D. Moment, The Dynamics of Interpersonal Behavior (New York, Wiley, 1964).

[11] B.W. Tuckman, Developmental sequence in small groups, Psychological Bulletin, 63(6), pp. 384–399 (1965).

[12] S. Reisman, T.W. Johnson, and B.T. Mayes, Group decision program, Decision Support Systems, 8, pp. 169–180 (1992).

[13] M. Hatcher, A video conferencing system for the United States army, Decision Support Systems, 8, pp. 181–190 (1992).

[14] D. Chappell, D.R. Vogel, and E.E. Roberts, The MIRROR Project: A virtual meeting place, Proceedings: 25th Hawaii International Conference on Systems Sciences, IV, pp. 23–33 (1992).

[15] C.H. Kepner, and B.B. Tregoe, The Rational Manager (New York, McGraw-Hill, 1965).

[16] D.T. Kearns, D.T., Changing a corporate culture: Leadership through quality, In R.L. Kuhn (Ed.), Handbook for Creative and Innovative Managers (New York, McGraw-Hill, 1988).

[17] G.K. Guiden, and D.E. Ewers, The keys to executive support systems, Indications, 5(5) (1988).

[18] J.A. Adam, Interactive multi-media, IEEE Spectrum, pp. 22–39 (1993).

[19] E. Francik, S.E. Rudman, D. Cooper, and S. Levine, Putting innovation to work: Adoption strategies for multimedia communication systems, Communications of the ACM, 34(12), pp. 53–63 (1991).

[20] R. Johansen, Groupware: Computer Support for Business Teams (New York, The Free Press, 1988).

[21] J. Morrison, Team memory: Information management for business teams, Proceedings: 26th Hawaii International Conference on Systems Sciences, IV, pp. 122–131 (1993).

[22] P. Gray, and L. Olfman, The user interface in group decision support systems, Decision Support Systems, 5, pp. 119–137 (1989).

![](/api/attachments/TE5UJZDF/fulltext/images/80e29b8dfd2314241ad97dc64c8b0cb4c1a489cbbc5e450e0b5e6c4d5e5820fb.jpg)

Christian Wagner is assistant professor of information systems at the University of Southern California's School of Business Administration. He holds a PhD in management information systems from the University of British Columbia. Wagner's research is directed at improving decision maker performance through information technology. Results of his research have appeared in information systems, management and marketing

journals in the U.S., Europe, and Japan. Wagner has been the recipient of a NSF grant to investigate the application of computer software in creative problem solving. He is listed in Marquis Who's Who in the World and other professional registers.
