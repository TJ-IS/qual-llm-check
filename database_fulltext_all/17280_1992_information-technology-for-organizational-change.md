---
otero_id: 17280
otero_key: "PRDFM3BQ"
title: "Information technology for organizational change"
authors: "Joey F. George; J.F. Nunamaker; Joseph S. Valacich"
year: "1992"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(92)90052-q"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## ODSS

# Information technology for organizational change

Joey F. George and J.F. Nunamaker, Jr.
University of Arizona, Tucson, AZ 85721, USA

Joseph S. Valacich

Indiana University, Bloomington, IN 47405, USA

The interrelationships between organization structure and information systems have attracted the attention of researchers since the 1950s. We propose three different architectures for organizational decision support systems (ODSS), each of which is tailored to an emerging change in organization structures: Downsizing; a focus on teams; and outsourcing. We argue that no single ODSS architecture can adequately meet the challenges of each structural change. Rather, each proposed architecture relies to a lesser or greater degree on five types of information technology: Communication; coordination; filtering; decision making; and monitoring technologies.

Keywords: Organizational decision support system, Downsizing, Teams, Outsourcing.

![](/api/attachments/PRDFM3BQ/fulltext/images/52590776e8462c314f185c5bab96e89566903cfdfcbc7460c09b83878d4fbadd.jpg)

Joey F. George is an Assistant Professor of MIS at the University of Arizona. He earned his A.B. degree from Stanford University in 1979 and his Ph.D. in Management at the University of California at Irvine in 1986. His research interests focus on how information systems affect work. Specific topics include the effects of group decision support system (GDSS) use on various group work processes and their outcomes, GDSS use in non-American cultures, the effects of computing on decision authority in organizations, computer training and support in organizations, and the effects of extensive computerization in work groups.

Correspondence to: Dr. Joey F. George, Department of Management Information Systems, University of Arizona, Tucson, AZ 85721, USA.

## 1. Introduction

Information technology (IT) and organizational structure have been intertwined since the publication of Leavitt and Whisler's “Management in the 1980's” in 1958 [16]. In that seminal paper, the authors predicted that there would be dramatic changes in organizational structure due to the influence of IT (Leavitt and Whisler were in fact the first to coin the term ‘information technology’ in their 1958 article). Specifically, they predicted that IT would enable the following changes:

(1) The boundary between planning and performance would move upward in the organization;

![](/api/attachments/PRDFM3BQ/fulltext/images/22a878122f94ed4d0a68ee3a6706bdb9d18efbdb95bcacbe3ea71d5e7869e950.jpg)

Jay F. Nunamaker is a Professor of Management Information Systems (MIS) and Computer Science and Head of the Department of Management Information Systems at the University of Arizona. He received a PhD from Case Institute of Technology in systems engineering and operations research. He was an Associate Professor of Computer Science and Industrial Administration at Purdue University. Dr. Nunamaker joined the faculty at the University of Arizona in

1974. He has authored numerous papers on group decision support systems, the automation of software construction, performance evaluation of computer systems and decision support systems for systems analysis and design.

![](/api/attachments/PRDFM3BQ/fulltext/images/cc9de25034823a6af1fd7047038800e34f82872f5d7f3e8d8768c22767ae3a65.jpg)

Joseph S. Valacich is an assistant professor of Decision and Information Systems at Indiana University. He received a bachelors degree in computer science and M.B.A. from the University of Montana, and a Ph.D. from the University of Arizona. Dr. Valacich worked for several years in the information systems field as a programmer, analyst and product manager. His current research interests include the design and investigation of communication and decision technologies to support collaborative group work. His recent research has been published in Management Science, IEEE Journal on System, Man, and Cybernetics, and the International Journal of Man-Machine Studies.

(2) Middle management jobs would become highly structured;

(3) Large industrial organizations would recentralize;

(4) Some middle management levels would move upward in the organizational hierarchy, while others would move downward;

(5) The line separating middle from higher levels of the organizational hierarchy would become clear and impenetrable.

There is no question that the typical organizational structure has changed since 1958 [1]. The days of the rigid hierarchical pyramid have passed, giving way to more flexible organizational forms. Perhaps the most notable changes have been in the ranks of middle management. Some of Leavitt and Whisler's predictions have come true: Middle management jobs are more structured; some middle management jobs have moved up in the organization while others have moved downward. But most noticeably, there are fewer middle managers now. Leavitt and Whisler did not foresee the other major change that has accompanied the reduction in the number of middle managers, the reduction in hierarchical levels. The extent to which these changes have been the result of IT use in organizations is an open question, but there is no doubt that organizations are using IT as a vital means to cope with the structural changes [9].

Academics continue to predict structural change in organizations and the role of IT in enabling these changes $[1,10,12,14]$ . For example, Applegate and her colleagues describe ‘cluster’ organizations, where hierarchies have been replaced with formal and informal communication networks and with project-oriented work groups. IT will allow the widespread sharing of information, shorten the time and distances between workers, identify who in the organization has the needed expertise, provide immediate access to information for managers, and free up workers at all levels for creative work. Drucker $[10]$ describes organizations that resemble orchestras or hospitals, where there are no intervening levels of management. There are more specialists at operational levels but smaller staffs at headquarters. Most of the work will be done by temporary task forces, whose members can be physically and temporally dispersed, but still work together through IT.

The information systems that will be needed to make these new types of organizational forms function are currently being developed in bits and pieces. For example, since communication via computer network becomes essential in such organizations, the development of flexible electronic mail and computer conferencing systems is crucial. Much of the work in these new organizations will be done by physically and temporally dispersed work groups. In these dispersed conditions, groups will need to receive the same level of support they can get today in same-place, same-time electronic meeting rooms. And all of these systems must be integrated, into organizational decision support systems (ODSS).

While the organizational forms described previously are not yet here, certain aspects of them are becoming evident. Three recent trends, documented in current business periodicals, which are bringing us closer to the organizational forms described above are: (1) downsizing; (2) an emphasis on teams; (3) the outsourcing of functions formally performed by the organization itself. How each of these trends can be supported by IT provides some insight into how ODSS can be designed and developed. In this paper, we will describe these three trends and how IT is currently being used to enable and support them. Then we will describe how ODSS might be designed to provide more and better support, emphasizing the particular IT needed for the necessary ODSS.

## 2. Current trends in organizations

Of all the structural changes currently taking place in organizations, the most widely publicized is downsizing. Downsizing describes the practice of reducing both the overall size of the workforce and of the number of hierarchical levels in the organization $[18,24]$ . Announcements of downsizing have become relatively common. In a four day period, The Wall Street Journal reported on announced downsizing plans at Unisys (cuts of 7% to 8% of its workforce of 88000, or 6000 to 7000 people) and Kodak (cuts of 3% of its workforce, or 4500 people) $[24]$ . Discussion of past downsizing also appears frequently in business periodicals. (Another article in The Wall Street Journal (Aug. 29, 1989) reported that Campeau Corporation had cut 8000 employees in the past 18 months, and that SmartCard International had halved its staff.) The personnel most likely to be removed in downsizing are in middle management, especially in staff positions.

For years, middle managers have served as intermediaries between top management and first line supervisors. They have acted as amplifiers for top management, broadcasting down to the levels below them the broad directives of the top. Conversely, they have acted as the filters from the bottom, reviewing massive amounts of information and deciding what got passed up to top management. For middle managers in a staff role, part of the job also consisted of taking raw data and transforming it through analysis into a few pieces of information top management needed to perform their jobs. A second major role of middle management was to maintain span of control at the low levels set at the turn of the century by Fayol and others. Each manager could manage only so many subordinates effectively.

Yet another key role of middle managers was integration among their own organizational units and other units in order to achieve organizational goals. According to Lawrence and Lorsch [15], the degree of integration needed is similar across many types of organizations, but the actual nature of the integration varies. Middle managers are the ones who must work with managers of other organizational units to achieve the proper level and type of integration.

With middle managers disappearing from the organization, there is no longer a need for many of the intermediary levels of hierarchy they formerly occupied. The organization becomes flatter. Fewer middle managers and fewer hierarchical levels mean fewer nodes in the organizational communication network, leading to more direct communication among nodes and more traffic along the remaining network channels. Similarly, spans of control necessarily increase. More personnel answer to each remaining manager. Despite the demands these changes make on the remaining managers, someone still has to integrate each unit's work with that of other organizational units. But since the overall workload has not decreased (it has probably increased), the organization must find a way to deal with its new structure.

A second trend that has received attention during the past few years is the movement towards teamwork [6]. The team concept has primarily been applied to manufacturing. Here the organization of work is changed so that what was formerly done by individuals working alone is now done by a group of workers working together. As such, they work as a team. For example, instead of the well-known assembly line model, where an individual worker is responsible only for installing a car's front windshield, the team concept envisions a group of workers given responsibility for putting together the entire automobile. The team model is taken from Japanese and Swedish automobile assembly practices, where generally self-managing teams work together to produce complete products.

The teamwork concept has not yet been widely applied to the service sector in the U.S., where 70% of the workforce is employed. There have been some attempts (e.g., [6]), but they tend to follow the manufacturing model very closely. For example, instead of a clerk in an insurance claims office being responsible for opening mail and then deciding how to distribute it, a team of clerks is given responsibility for processing the claim from the time it comes in until it is settled. If the types of organizational forms described by Applegate, et al., [1] and Drucker [10] come to be, however, most all work at the managerial level and in the service sector will be done by teams.

Finally, the third trend we are investigating is outsourcing functions formerly handled by the organization itself. To some extent, this has been going on for some time, but it is gaining in popularity. Recent examples include IBM's trial contract with Pitney Bowes to run their mailrooms, and Eastman Kodak's decision to hire IBM to run their data processing center and Businessland to run their personal computer information centers [7]. In a way, outsourcing can be seen as another form of downsizing. It reduces the size of the company because all of the personnel who were working in that area no longer work for the organization (they are often hired by the company that assumes responsibility for the function).

Outsourcing allows organizations to focus on what they do best, in Kodak's case, to be in the photographic-products business, not in the computer business [7]. However, it does create new interdependencies between organizations that did not exist before. Outsourcing may require even more coordination than was required before, and it may be more complex, as it is coordination between organizations, rather than between different individuals within the same organization.

## 3. The current role of IT

Of the three trends in organizations that we have discussed, the one most dependent on IT for support has been downsizing. Perhaps this is because downsizing is not a recent trend, but one that has been progressing over the past decade. As was mentioned above, if there are fewer middle managers, but the same amount of work, some means must be developed to deal with that work. Organizations have increasingly turned to IT as that means, for the amplifier/filter, span of control, and integration functions of the middle manager.

The amplifier/filter role deals primarily with communication. As an amplifier, a middle manager must figure out a way to communicate the wishes and views of top management to the lower levels of the organization. As a filter, the middle manager must screen incoming messages and pass on only those that are deemed important to top management. In the past decade, these functions have been performed to some extent via electronic mail. In fact, as electronic mail has gained in popularity, and as some executives and managers have found themselves becoming inundated with messages, some have suggested that electronic mail be merged with artificial intelligence so that information overload is avoided [19].

The span of control function can be handled in part with electronic mail, as it involves elements of communication too. Managers can issue requests and monitor responses to those requests using electronic mail. They can call meetings, make announcements, send memos, and ask for comments, all via electronic mail. However, trying to achieve the coordination necessary for effective work between a manager and dozens of employees can easily lead to hundreds of messages, even over trivial matters. Consider how difficult it can be to call meetings which everyone involved can attend and how much communication that calls for.

To better deal with span of control tasks and the coordination they call for, managers have turned to electronic calendars and what some have called groupware $[9,14]$ . Electronic calendars enable all concerned to see calendars for coworkers and, for facilities, making it easier to schedule meetings for groups in specific rooms. Groupware also enables coordination among group members, but on a more sophisticated level. Coordinator, an example of groupware, sets up a framework of offers and commitments, and reminds workers of promises they have made and deadlines that are approaching. Some people, however, find systems like Coordinator to be too rigid and intrusive.

The communication and coordination functions of electronic mail and groupware also provide support for the integration role of middle managers. The technologies provide much the same type of support, but the nature of it differs across roles. Whereas a manager with an expanded span of control needs support for communication and coordination within his/her work group, s/he needs support for the same functions between work groups in the role of integrator.

As downsizing takes place, managers not only have to manage more people, they also have to manage more information, and information at a lower level of abstraction. These circumstances have led some managers to demand the development of executive information systems (EIS), which allow them to handle the increased levels of information they now must face $[21]$ .

The other two trends we discussed earlier, work group teams and outsourcing, do not at this point appear to be supported very well by IT. In the case of teams, the lack of IT support may be due to some of the following. First, most teams so far are in manufacturing. Traditional use of IT in manufacturing has been more inclined to replace workers than to support them. Second, the teams are all in the same place at the same time working on the same task. The communication feature of IT does not add much to the process in such a situation, at least not enough to justify the cost. Third, the emphasis on teams in the American workplace is still very new. We may not yet know how to design systems that can effectively support such processes in their current manifestations. However, as the emphasis shifts to teams in the service sector, and as the manufacturing-like assembly line model is abandoned in service organizations, there may be more possibilities to explore for IT.

Outsourcing is an even more recent phenomenon. It seems clear, however, that coordination will become very important here, but as was pointed out above, it will be coordination between organizations, not within them. The communication role of IT becomes important here, and it is not clear whether electronic mail would suffice. Just how IT in the form of ODSS could be used to support outsourcing and teamwork, in addition to providing more advanced support for downsizing, is discussed later in the paper. First, however, we will look at specific information technologies, which would be components of an ODSS.

## 4. ODSS technologies

There are many information technologies that could act as key components of an ODSS. Some of these technologies and their roles in supporting different organizational objectives have been mentioned previously. Some technologies are more appropriate than others in supporting organizational objectives. Downsizing might require technologies that facilitate intraorganizational communication, information filtering, and operational monitoring. Teams also require IT to support communication, but with a focus on intra-group communication, as well as technologies to support coordination and decision making. Organizations opting to outsource activities will require technologies to support interorganizational communication and coordination. Thus different organizational objectives require different IT and dissimilar implementations of that technology. There are many specific technologies that can be applied to foster different organizational objectives. This section describes many specific technologies as they apply to general ODSS objectives such as communication, coordination, filtering, decision making and monitoring.

Communication technologies refer to IT designed to foster team, organizational or interorganizational communication. Common technologies of this class include electronic mail, computer conferencing and video conferencing. Electronic mail refers to systems that allow information to be sent via a communication network from one individual, group or organization to another. Electronic mail can be seen as a general purpose communication method and is often used as a replacement for paper memos or telephone calls. The focus of computer conferencing refers to computer-based systems that allow individuals, distributed in both time and space, to communicate and coordinate activities, typically focusing on specific issues or ‘conferences.’ Computer conferencing is distinguished from electronic mail by its focus on specific issues or conferences. Computer conferencing can be thought of as a special purpose communication environment where conference members are often analogous to group members involved in an ongoing project. Video conferencing refers to technologies that allow physically distributed individuals to meet simultaneously in an environment where group members can see and hear one another as in a face-to-face meeting. Future implementations of video technologies may be used in conjunction with other meeting technologies such as an electronic meeting system (described below).

Coordination technologies refer to IT used to coordinate resources, facilities and projects. Groupware [9,14] refers to information system environments designed to coordinate and support work teams. Although groupware technologies may span many technological classifications (e.g., communication and decision making), its special strength is for coordination. In this light, coordination technologies refer to IT used to coordinate resources (e.g., equipment and people), facilities (e.g., rooms), and projects (e.g., automatic reminders and scheduling systems).

Filtering technologies refer to intelligent agents used to filter and summarize information. For example, future implementations of coordination technologies such as electronic mail and computer conferencing can integrate artificial intelligence technologies to sort, prioritize and automatically respond to an increased volume of electronic messages [19]. Receivers can determine what messages they receive by specifying what their interests are, and message priority filters can be established by senders as well as receivers [3,4]. The net result is that a manager will receive less overall information, but what is received will be more relevant.

Decision making technologies are those designed to improve the effectiveness and efficiency of individual and group decision making. An electronic meeting system (EMS) refers to computer-based technologies designed to make meetings more productive. Although an EMS can encompass video and computer conferencing, in this context an EMS refers to IT designed to enhance face-to-face group meetings. Decision support systems are individual support environments for the solution of structured and semi-structured problems $[23]$ .

Monitoring technologies refer to such IT as executive information systems (EIS), described as computer-based technologies used to monitor the status of organizational operations, industry trends, competitors and other relevant information. The goal of an EIS is to summarize and integrate key information required by senior decision makers to more effectively communicate, plan and control their organization [22].

Each of these ODSS technologies are designed to perform general types of activities. However, the application and consequence of each technology may be different depending upon the situation. For example, teams using an electronic mail system will generally use it to communicate and coordinate activities between specific team members on a project. The electronic mail technology used by the team may reside on a large corporate system, or on a local team network. Thus the relative scope for the application of communication technologies for teams may be quite narrow (e.g., one electronic mail system residing on a local system). Yet, for an organization that has outsourced an organizational function to another organization, electronic mail communication may be much more complicated, as multiple systems may need to be bridged for effective, timely and secure interorganizational electronic communication. The matrix in fig. 1 relates the ODSS technologies to the organizational design issues described previously. The relationship is somewhat arbitrary, yet represents what technologies we feel most strongly support various organizational objectives. Each of the ODSS configurations implied in Fig. 1, and the organizational objective each configuration is intended to support, is discussed in more detail in the remainder of the paper.

![](/api/attachments/PRDFM3BQ/fulltext/images/b37ed5cb275e3a35cce461dfba0eea75e84229bde1a74849a490b6ddb18fec97.jpg)  
Fig. 1. ODSS technology vs organizational objective.

## 5. Future role of IT

The application of IT to support various organizational objectives requires that the ODSS be applied in an explicit manner. The objective of this section is to describe how similar technologies can be applied differently to achieve distinct organizational designs. This is not to suggest that multiple organizational objectives cannot be simultaneously achieved. It does suggest, however, that each objective may best be met by specific technological capabilities.

## 5.1. ODSS support for downsizing

As noted above and displayed in the matrix, organizational downsizing can take advantage of most of the ODSS technologies described here. The downsizing of an organization increases the number of information sources (and possibly the amount of information) upper-level members must interact with. Key elements of an ODSS for organizational downsizing appear to be communication, filtering and monitoring technologies.

Downsizing may leave some organizational sites without local experts for certain problems, requiring them to communicate with remote experts from time to time. Eveland and Bickson [11] found that computer-mediated communication (e.g., electronic mail) requires less effort for individuals than traditional communication methods (e.g., telephone), resulting in lower relative costs. The low cost will enable such sites to connect to distributed experts, allowing them to quickly solve problems and make decisions. Applegate, et al., [1] propose that these distributed communication technologies will eventually form the organizational infrastructure and change the role of formal reporting procedures, as individuals in large, widely dispersed and complex corporations will be able to communicate with any other individual; just as if s/he worked in a small company.

Communication technologies also foster a deluge of electronic messages. Current research in this area applies expert system technology to filter and process messages automatically. Expert system mail systems can apply user defined rules as to which messages to read and respond to immediately, which to discard, and which to save for later (prioritization). Malone and his colleagues [19] have been investigating the effects of intelligent mail systems to ease the burden of processing larger volumes of electronic messages. Their approach has been to design information filters (i.e., cognitive, social and economic filters) that can be applied to a variety of textual documents (electronic mail, bulletin boards or the table of contents of journals) to more effectively decide what to respond to, what to download and what to read.

An alternative approach has been followed by Brookes and associates $[3,4]$ in the OFFICE EXPRESS system. In this system, messages are delivered based on their content rather than by specific user address, according to key word lists kept by users. In addition, message authors can prioritize the messages they send, so that messages are filtered for recipients according to their priority ratings. An added feature is the creation of dynamic conferences through the automatic linking of related messages in an organization's message database.

Just as expert systems can filter electronic messages, executive information systems will be a pervasive monitoring technology, facilitating expanded spans of control. For example, a manager will be able to ‘manage by exception’ by having her EIS look for data out of normal operating boundaries. Thus, operational anomalies can be identified by the system so that they can be addressed as soon as possible.

An ODSS architecture for supporting the downsizing of an organization is presented in fig. 2. The key elements of this ODSS are systems and tools that facilitate effective organizational communication, information filtering and operational monitoring. These ODSS subsystems may reside ‘above’ or be part of existing organizational information systems. The key elements must be configured so that upper-management is effectively supported with functions previously supplied by middle managers.

![](/api/attachments/PRDFM3BQ/fulltext/images/61a8b58d8825808a954f7263f9d59297d49de8e3b5ef9ae69dedabd7decf038a.jpg)  
Fig. 2. ODSS for downsizing.

## 5.2. ODSS support for teams

As shown in the matrix in fig. 1, the primary ODSS technologies required to support organizational teams include intragroup communication, team member coordination and decision making technologies. Team communication may be facilitated, in most cases, by using a small team network or existing organizational information system communication facilities (e.g., electronic mail and conferencing systems). However, organizational downsizing may, on occasion, leave remote organizational sites without key team members. In these cases, remote teams will need to link to experts at other organizational locations. This linking will be easy if all distributed offices share IT resources and systems. Yet if remote offices have their own local computing facilities, then linking to remote offices may be somewhat difficult. In any event, intragroup communication will be a key ODSS requirement for work group teams.

The coordination of meetings, resources and team members can be a large undertaking. An ODSS that can access facility, equipment and team member calendars can be used to find, for example, the earliest time available for a one hour meeting using a specified room and equipment. Once found, the system can schedule the room, equipment and team members by updating the personal electronic calendar of each team member, room and equipment. Other ODSS technologies to facilitate coordination might include systems, such as Coordinator (briefly described above), that can remind team members of commitments and approaching deadlines.

![](/api/attachments/PRDFM3BQ/fulltext/images/89f3cf62687fa1f966229ab29c72f550e81e07df04b0bc615c4c6ad27f230acc.jpg)  
Fig. 3. ODSS for teams.

Team decision making technologies include electronic meeting environments. These environments are designed to improve group productivity for a variety of group tasks (e.g., planning, idea generation, problem solving, issue discussion, negotiation, conflict resolution, decision making, etc.—see also [20]) by reducing the group process losses common in nonsupported group interaction (see [8] for a detailed discussion of these systems). An ODSS architecture to support teams is presented in fig. 3. The key components of this architecture are the local team systems for communication, coordination and decision making, and communication linkages to larger organizational systems.

## 5.3. ODSS support for outsourcing

The key technology required to support the outsourcing of organizational activities are ODSS systems for interorganizational communication. Barrett and Konsynski [2] described interorganizational systems as those that involve resources shared between two or more organizations. Typical resources include hardware, software, communication and transmission facilities, rules and procedures, data and databases, and expertise. As suggested by fig. 4, the relationships between organizations can be multifaceted (i.e., as contractors for services, as suppliers of resources, or purchasers of products). As we have already seen, Businessland and IBM's relationship with Kodak is that of contractors. They are performing activities for Kodak that were previously performed internally.

The relationships between American Hospital Supply (AHS) and their customers is a classic example of an interorganizational ODSS. AHS leverages its ODSS for interorganizational communication to become a primary supplier to hospitals and clinics. The incentives for establishing interorganizational ODSS are numerous. Firms that stick to their core business are generally much more competitive than firms that get out of their core activities [5]. Thus when Kodak got out of the business of supporting its internal personal computers, the organization could more easily focus on its primary business.

The ODSS technology matrix suggests that the key ODSS feature for interorganizational systems is communications. However, the coordination and timing of services and the delivery of products and resources will also be important. The coordination may be facilitated by monitoring systems (e.g., inventory, quality of service, etc.). Nonetheless, the key requirement will be the initial communication linkages, as with any other interorganizational ODSS technology.

![](/api/attachments/PRDFM3BQ/fulltext/images/77ae38541a8c09ecca283ba1d5d2363bb1f8b3d0b0e270f4f00895faea3cc457.jpg)  
Fig. 4. ODSS for outsourcing.

## 6. Conclusion

In this paper, we have focused on what we believe are the three most promising current trends in organizations from an IS perspective: downsizing, teams, and outsourcing. These changes are important in and of themselves, because they are happening now and because organizations need to understand how to successfully apply IT to them. The changes are also interesting because they foreshadow the changes described in the Applegate, et al. [1] and Drucker [10] papers. If we are to move to a world of organizations such as those described in these papers, we are likely to first encounter such changes.

Each type of change brings with it its own requirements for information technology support. While it may be possible for a single ODSS architecture to satisfy the support requirements for many types of organizational change, it is probably more effective for an ODSS to be designed to meet the requirements of a specific situation. We have suggested that ODSS be tailored to specific situations rather than be designed as general purpose organizational systems. If we can successfully develop ODSS to support organizations engaged in downsizing, team development, and outsourcing, then we will be better prepared to develop ODSS to support the next set of new organizational forms.

## References

[1] L.M. Applegate, J.I. Cash, Jr. and D.Q. Mills, Information Technology and Tomorrow's Manager, Harvard Business Review, 128–136 (1988).

[2] S. Barrett, and B. Konsynski, Inter-Organization Information Sharing, Systems, MIS Quarterly Special Issue, 93–105 (1982).

[3] C.H.P. Brookes, A Corporate Intelligence System for Soft Information Exchange, in: L.B. Methlie and R.H.

Sprague, ed., Knowledge Representation for Decision Support Systems, 161–166 (Elsevier Science Publishers, B.V., Amsterdam, 1985).

[4] C.H.P. Brookes and M. O'Connor, Supporting the Process of Group Decision Making, Working Paper, Pacific Research Institute for Information Systems and Management, 1988.

[5] E.S. Buffa, Meeting the Competitive Challenge, (Dow Jones-Irwin, Homewood, IL, 1984).

[6] Business Week, The Payoff from Teamwork, 56–62 (July 10, 1989).

[7] P.B. Carroll, and J.R. Wilke, Computer Firms Find Service is What Sells, Not Fancier Hardware. The Wall Street Journal, A1 and A9 (Aug. 15, 1989).

[8] A.R. Dennis, J.F. George, L.M. Jessup, J.F. Nunamaker Jr. and D.R. Vogel, Information Technology to Support Electronic Meetings, MIS Quarterly 12, Nr. 4, 591–624 (December 1988).

[9] J. Dreyfuss, Catching the Computer Wave, Fortune, 78–79, 82 (Sept. 26, 1988).

[10] P.F. Drucker, The Coming of the New Organization, Harvard Business Review, 45–53 (Jan.-Feb. 1988).

[11] J.D. Eveland, and T.K. Bickson, Work Group Structures and Computer Support: A Field Experiment, Proceedings of the Conference on Computer-Supported Cooperative Work, Portland, OR, 324–343 (1988).

[12] G.P. Huber, Effects of Decision and Communication Technologies on Organizational Decision Processes and Structures, in: R.M. Lee, A. McCosh, and R. Migliarese, ed., Organizational Decision Support Systems, (North-Holland, Amsterdam, 1988).

[13] G.P. Huber, The Nature and Design of Post-Industrial Organizations, Management Science 30, Nr. 8, 928–951 (1984).

[14] R. Johansen, Groupware, (The Free Press, New York, 1988).

[15] P.R. Lawrence and J.W. Lorsch, Organization and Environment, (Richard D. Irwin, Inc., Homewood, IL, 1969).

[16] H.J. Leavitt and T.L. Whisler, Management in the 1980's, Harvard Business Review, 41–48 (Nov.-Dec. 1958).

[17] R.M. Lee, A.M. McCosh, and P. Migliarese, ed., Organizational Decision Support Systems, (North-Holland, Amsterdam, 1988).

[18] J. Main, The Winning Organization, Fortune, 50–52, 56, 60 (Sept. 26, 1988).

[19] T.W. Malone, K.R. Grant, F.A. Turbak, S.A. Brobst, and M.D. Cohen, Intelligent Information-Sharing Systems, Communications of the ACM 30, Nr. 5, 390–402 (1987).

[20] J.E. McGrath, Groups: Interaction and Performance, (Prentice-Hall, Englewood Cliffs, NJ, 1984).

[21] PC Week, Phasing Out of Middle Managers May Increase Dependence on EIS, 71, 78 (August 21, 1989).

[22] J.F. Rockart, and D.W. DeLong. Executive Support Systems: The Emergence of Top Management Computer Use. (Dow Jones-Irwin, Homewood, IL, 1988).

[23] R.H. Sprague, A Framework for the Development of Decision Support Systems, MIS Quarterly 4, Nr. 4, 1–26 (1980).

[24] The Wall Street Journal, (August 21, August 24, and August 29, 1989).
