---
otero_id: 24942
otero_key: "F9BBGCE8"
title: "Lessons from the Early Adopters of Web Groupware"
authors: "Alan R. Dennis; Sridar K. Pootheri; Vijaya L. Natarajan"
year: "1998"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1998.11518186"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Lessons from the Early Adopters of Web Groupware

Alan R. Dennis, Sridar K. Potheri & Vijaya L. Natarajan

To cite this article: Alan R. Dennis, Sridar K. Potheri & Vijaya L. Natarajan (1998) Lessons from the Early Adopters of Web Groupware, Journal of Management Information Systems, 14:4, 65-86, DOI: 10.1080/07421222.1998.11518186

To link to this article: http://dx.doi.org/10.1080/07421222.1998.11518186

![](/api/attachments/F9BBGCE8/fulltext/images/257b49535d069c0c6c6a132a7c9b9ad9a5722f454fce40302c6d30c4eac175bc.jpg)

Published online: 08 Dec 2015.

![](/api/attachments/F9BBGCE8/fulltext/images/04979451a737f7d2d0a559e714319f6d0f81b296e1b259e8de91b87eb3577779.jpg)

Submit your article to this journal ↗

![](/api/attachments/F9BBGCE8/fulltext/images/884d63b7257d88866a95ecd78f89046a51c75b3f57cca736f2da77544106e8f2.jpg)

Article views: 2

![](/api/attachments/F9BBGCE8/fulltext/images/64a2eacd9c2f0fa597a92964cb6b3a49bce94b7ef26d78f0f553a31fc57f04eb.jpg)

View related articles ↗

![](/api/attachments/F9BBGCE8/fulltext/images/c23476266d1fab0350a87067b54e62a5f2d8dfca95c66d6cd8a48198b52a8d13.jpg)

Citing articles: 15 View citing articles ↗

# Lessons from the Early Adopters of Web Groupware

ALAN R. DENNIS, SRIDAR K. POOTHERI, AND VIJAYA L. NATARAJAN

ALAN R. DENNIS is an Associate Professor of Management in the Terry College of Business at the University of Georgia. He received a Bachelor of Computer Science from Acadia University, an M.B.A. from Queens University, and a Ph.D. in management information systems from the University of Arizona. His current research interests include group brainstorming and decision making, and the design of web-based technologies to support collaborative work. His past research has appeared in journals such as Academy of Management Journal, MIS Quarterly, Information Systems Research, Management Science, Communications of the ACM, Organizational Behavior and Human Decision Processes, and Journal of Applied Psychology. His most recent book is Business Data Communications and Networking, coauthored with Jerry FitzGerald.

SRIDAR POOTHERI is a doctoral candidate in mathematics and a master's candidate in computer science at the University of Georgia. He received a Bachelor of Mathematics degree from the Vivekananda College at the University of Madras, and a Master of Mathematics degree from the Ramanjuan Institute of Advanced Study in Mathematics at the University of Madras, India. His current research interests include graph theory and combinatorics and the design of web-based technologies to support collaborative work.

VIJAYA NATARAJAN is an M.S. candidate in computer science at the University of Georgia. She received a Bachelor of Mathematics degree from the Vaishnava College at the University of Madras, and a Master's of Mathematics from the Ramanjuan Institute of Advanced Study in Mathematics at the University of Madras, India. Her current research interests include distributed computing, design of Web-based technologies to support collaborative work, including fungal genome resources.

ABSTRACT: The Internet and World Wide Web hold many possibilities for virtual communities. In this paper we describe the development of a first-generation Web-groupware system called TCBWorks that enables anyone with a Web browser to use groupware. We discuss the design strategy, the overall design, and the technical architecture, and contrast it with other forms of groupware. We then discuss the results of a series of interviews with users in four organizations and a survey of sixty-nine organizations to better understand how organizations are using Web groupware and the advantages and disadvantages they encountered.

KEY WORDS AND PHRASES: adoption of information technology, groupware, Web groupware.

THE INTERNET AND WORLD WIDE WEB HOLD MANY POSSIBILITIES for virtual communities—people with shared interests or goals for whom electronic communication is a primary form of interaction. The Internet and the Web enable individuals to exchange e-mail, participate in newsgroup or listserv discussions, and publish information electronically. The Web also enables innovative applications of groupware $[5, 7, 16]$ . Traditional groupware has been focused primarily on private, often LAN-based, internal corporate networks. Many groupware tools such as the document databases and workflow systems of Lotus Notes or the brainstorming and decision-oriented systems of GroupSystems or VisionQuest required proprietary—and often expensive—software. Such systems are awkward for building electronic communities, which often reach far beyond one proprietary local or wide area network.

The Web is changing this: Dozens of Web-based systems now bring the power of groupware to any desktop equipped with a Web browser $[1, 3, 20]$ . The question, of course, is what are the advantages and disadvantages Web-based groupware systems compared with the more traditional Internet systems available to electronic communities (e.g., e-mail, listservs, usenet newsgroups)?

In this paper we describe the development and use of a first-generation Web-based groupware system called TCBWorks. Our goal is to identify a number of fundamental issues facing groupware developers and users in order to help them design and implement improved groupware environments. We begin by examining the current technologies available for collaboration. We then discuss the basic design strategy and specific features of our Web-based groupware system, which is in use at more than 200 installations worldwide. Next, we report the results of a survey of sixty-nine organizations that are early adopters of the system to better understand how they are using it, and the benefits and problems they have experienced. While some of the issues raised are probably specific only to the immediate future of Web groupware, many are fundamental issues critical to its long-term success.

## Groupware and the Internet

ELECTRONIC COMMUNITIES HAVE EXISTED IN SOME FORM FOR ALMOST as long as there has been reliable electronic communication, at least since the mid-1970s [8, 9, 19]. Many of these communities existed through proprietary conferencing systems (e.g., EEIS, developed at the New Jersey Institute of Technology [10]). As the Internet and internal networks became commonplace, e-mail, listservs, and usenet newsgroups soon followed. One of the key advantages of e-mail, listservs, and newsgroups over the proprietary conferencing systems was their universality; because of standards, users on a variety of different systems could now communicate freely with each other.

Conferencing systems, e-mail, listservs, and newsgroups generally can be categorized as different forms of groupware. In general, groupware is a set of hardware and software designed to help groups work together, whether in the same room at the same time, or at different times and places $[15]$ . Vendors, consultants, users, and university researchers all have used the term groupware to denote many different types of software, each of which supports very different types of group work.

E-mail and, by extension, listservs enable individuals to send electronic messages to others or to entire groups of other users. Communication is sequential and generally unstructured. Messages on different topics can follow each other and become intertwined, making communication much like watching many different television channels simultaneously. E-mail and listservs are “push” technologies, in that the sender of the message determines who receives it, not the receiver(s). This can create problems with information overload because users cannot easily filter or summarize messages without processing them $[11]$ .

Listservs also impose a heavy message load on the network and supporting computers. If there are 1,000 members of a listserv, then every message is duplicated 1,000 times. If users choose to save messages, those messages are duplicated and stored in 1,000 different places.

Usenet newsgroups solve some of these problems by imposing some minimal structure to messages. Messages can be organized and threaded so that responses can be linked to the original messages and other responses by threads that enable readers to follow related discussions. Newsgroups are “pull” technologies, in that users select which messages to read. This ability to select messages and the limited structure offer some improvement in the reduction of information overload; however, editing and organizing messages is difficult. Security is also an issue because, unlike e-mail and listservs, it is more difficult to restrict access to newsgroups so that only selected users can participate.

Newsgroups reduce network traffic and storage because only one copy of each message is stored on each newsgroup server. Nonetheless, since not all newsgroup servers are updated simultaneously, there are some inconsistencies in the message structures among different newsgroup servers. Messages and replies to messages may be available to some users before others.

Proprietary conferencing systems and groupware systems are pull technologies too but they offer the ability to select participants and define their privileges. They provide two key functions beyond those of e-mail and newsgroups. First, they enable participants to generate, read, and organize information in an archived, structured form. Participants can edit, move, and structure the information in many different formats, so that the structure can add meaning to the comments and reduce the effects of information overload $[11, 15]$ . Filtering is possible as participants can use headings and position in the structure to choose what they wish to read $[11]$ . The archival nature of these systems also means that participants can use them as a group or organizational memory $[15]$ . Many systems also enable anonymous comments, possibly encouraging more open discussion $[11, 15]$ .

The second key function of this form of groupware is the ability for group members to vote on, or otherwise quantitatively analyze, the relative merits of alternatives $[11, 15]$ . Most groupware systems' users can vote by ranking or rating alternatives. Some support more formal methods such as Delphi or multicriteria decision making, so that all members can evaluate alternatives on a series of criteria (e.g., rating cars on gas mileage, trunk space, acceleration). Others support more elaborate decision analysis processes. In any case, each participant enters his or her ratings, analyses, or votes, which are then combined with those of all other participants and presented to the whole group for further discussion.

While these proprietary conferencing and groupware systems offer several benefits over e-mail, listservs, and newsgroups, they historically used software and architectures running over local area networks or proprietary wide area networks, architectures that severely restrict the systems' widespread use. Using them to support distributed meetings over long distances required expensive special-purpose hardware and software. They do not have the same low cost, technical simplicity, and "reach" of Internet-based tools.

Thanks to the recent explosion of the Web, however, we can now build systems and architectures that take advantage of widely adopted open standards that are available to most potential groupware users. Many existing proprietary groupware products are embracing the Web (e.g., Notes). Today, more than seventy-five Web groupware systems are available, virtually all of which have debuted since 1996 [20].

## TCBWorks: A Web Groupware System

WE NOW DISCUSS ONE WEB GROUPWARE SYSTEM and contrast it with other forms of groupware. The first version of TCBWorks (version 1.0) was released on October 10, 1995. The second version (1.1) was released on April 1, 1996. TCBWorks, which takes its name from the initials of the Terry College of Business at the University of Georgia, can be accessed using a Web browser at http://tcbworks.cba.uga.edu.

## Design Strategy

Most current groupware tools take either a data-centered or a process-centered view in their design. Lotus Notes, for example, is data-centered; it provides an excellent repository for storing data in a highly structured database format. Although there are many different types of data that can be defined and many ways to view them, the types of group processes Notes supports is extremely limited; it is difficult to analyze, assign priorities, and vote on the information without writing special-purpose external procedures.

Other groupware tools, such as GroupSystems or VisionQuest, are process-centered. They provide many different tools to support different group processes, such as idea generation, information organizing, and voting. Integrating data among different processes, however, can be difficult because each process is supported by a separate tool that treats its data separately from the data in other tools (e.g., one tool for generating ideas, another for voting). This approach has two major drawbacks. First, data often must be moved from one tool to another (sometimes losing structure and information in the process). Second, to accomplish most tasks, the user must master a set of tools, each of which has a different interface.

We took an object-oriented view to the system design. The system was designed as a set of objects, each with a common set of data and processes. All data are available to all processes, eliminating the need to move them among separate tools. Most processes share some common objects (e.g., add, delete), meaning that separate processes share the same program code and interface.

The system is also flexible, but restrictive, as defined by Silver [18]. Its flexibility comes from the wide range of functions that participants can use in a variety of ways. Users can add, delete, modify, move, and combine different parts of the discussion. Each comment can be anonymous, or it can identified with the name of its author. Users can add, delete, and change the importance of different criteria when voting.

However, such flexibility can create chaos if not managed properly. Imagine the impact on productivity and group cohesiveness if some users regularly deleted comments that opposed their viewpoints, or changed the criteria and their relative importance after others had finished voting.

The system is restrictive in that one person, the leader or organizer of a project, defines what participants can and cannot do. No function is available unless the organizer makes it available. For example, the organizer normally does not permit participants to delete others' comments or to change voting criteria. Usually, only the organizer deletes comments or changes criteria. To provide flexibility and restrictiveness, we created the ability for the organizer to enable or disable every function in the program at the individual button level. No button is available unless the organizer permits participants to use it. To implement this, we created four categories of users, each with different access rights.

\- Administrators can perform any function, including creating and deleting users.

\- Organizers can create new projects and perform any function on the projects they create, including granting access to other users, deleting the project, moving it, and so on.

\- Participants can only access those projects to which they have been granted access by an organizer, and can only perform those functions permitted by the organizer.

\- Observers have read-only access to the projects specified by an organizer.

Restrictiveness provides a more powerful intervention so that groups are more likely to use the system as the organizer intended. Used properly, it promotes the use of more effective techniques and prevents less effective ones, fosters learning, promotes consistency, and provides coordination $[18]$ . When used improperly, however, it can also constrain creativity and exploration, limit system applicability, promote user dissatisfaction, and be seen as manipulative, thus resulting in non-use of the system $[18]$ .

## System Design

The principal organizing object in the TCBWorks is the project, which contains all the data and processes needed to perform most group tasks. Projects are organized in a hierarchy, so projects can contain sub-projects, sub-sub-projects, and so on. All projects can be added, deleted, modified, and moved. The Project Screen (figure 1)

displays all projects to which the user has access. The action buttons displayed on the left of the screen change according to the type of user. Figure 1 is the project screen seen by the system administrator, showing all possible buttons. A project organizer would have all of the buttons except the Controls button, which is used to control access to the database (e.g., create new users). A participant has no ability to create or change a project, so a participant's project screen only shows the Open and View buttons (as well as help, refresh, and exit). An observer's project screen just shows the View button (as well as help, refresh, and exit).

Each project in turn contains a set of topics, which contain many of the same properties as projects. They also are organized hierarchically and can be added, deleted, modified, and moved. The Topic Screen (see figure 2) displays all the topics that exist for a project and enables the user to discuss topics and add new ones. Once again, which buttons are displayed depends upon the type of user and the rights granted by the project organizer. Administrator(s), the project organizer, and any user to whom the organizer has granted organizer rights can perform any function. Participants have only those buttons the organizer has selected. The buttons available to participants can be changed at any point by the organizer. For example, the organizer may begin a session by permitting participants to add new topics but not to vote. Once the list of topics has been developed, the organizer may remove the add button and activate the vote button. Figure 2 shows the organizer's view of the topics with all buttons.

Topics in turn contain comments (short paragraphs of text) that can be added, deleted, and modified. The Comment screen (figure 3) displays all the comments entered under a topic and provides an input box for participants to enter their comments. Typically, there are many comments from different participants under the same topic. Comments are normally displayed in the order in which they are entered, but participants also have the option to insert their comments after a specific one, simply by changing the number in the comment number box (see figure 3). The organizer can specify whether participants can Insert, Delete, or Replace comments, as well as specifying whether comments will be anonymous or identified by the name of the contributor.

Comments can contain html tags, enabling participants to specify formatting (e.g., bold, italics, bullet lists), as well as taking advantage of all the other benefits of the Web. It becomes simple to embed a graphic in a comment (provided that you know the html syntax and the Web address of the graphic). It is also simple to insert a link to other Web documents.

Each topic can be rated (voted on) using a set of criteria defined by the organizer. There are a maximum of ten criteria, each with separate user-defined ranges (minimum and maximum values). Each participant enters a rating for each topic for each criterion, and the system provides the mean value of the group's ratings (see figure 4). Votes can be easily changed at any time, and participants can shift between the screen in which they enter their votes and the screen that displays the average of all participants' votes (assuming that the organizer grants this access). The results are sorted to display in ascending or descending order by the average across all criteria, or any one criterion.

![](/api/attachments/F9BBGCE8/fulltext/images/73442590c864eca8455f40438ef2c6da4d946d9c2e8e7e8d465224b2b6fa52ee.jpg)  
Figure 1. Project Screen

## Technical Design

TCBWorks uses a client-server architecture that requires Netscape or a compatible browser. The system itself is composed of twenty-eight C programs (about 25,000 lines of code) residing on a UNIX or Linux Web server that work in conjunction with a database (we use the MiniSQL database [12, 13]). The programs generate the html forms that are used to capture the user's commands and present information in response. The user enters information via a Web browser and clicks on a button, sending the form to the Web server. Based on the form's information, the server calls the appropriate C program and passes the information to it via the CGI interface. Then the program processes the form information, interacts with the MiniSQL database via SQL statements to retrieve information from or update the database, generates an html form, and sends it to the Web server, which sends it to the browser for display.

Each transaction is a separate request. The Web server does not remember the previous steps it took to reach any given screen. Because the user can get to any screen (by using the “back” key) and exit at any state, the html form that is returned with each request must contain sufficient information to tell the system all choices made by the user in the previous screen, in addition to the current request. For example, to add a new topic, the html form must also contain information on the current project, because the system cannot determine the project in which the user is working. This information is passed along from program to form and form to program as a hidden value; thus, each form contains the information needed to process the current request and the system's memory of who the user is and how the user has reached the current screen.

![](/api/attachments/F9BBGCE8/fulltext/images/763a1e7cd78d55ab30a1a679e2fd42386766950db27f165bd514bf0dc7e9fdd2.jpg)  
Figure 2. Topic Screen

The decision to take an object-oriented design approach allowed many of the software modules to be reused. For example, the code to add, delete, modify, and move topics is virtually identical to the code for projects. Once the program modules for the projects were complete, it was easy to reuse most of it for the topics.

## TCBWorks Compared with Other Systems

When we began developing TCBWorks, virtually no other Web groupware systems were available. Today there are more than seventy-five, and new ones are being added every week. David Woolley's continually updated Web page on Web conferencing [20] is the most comprehensive list of systems. Collaborative Strategies [1] and Groupware Central [3] also are good sources of information.

Since new systems are being added and existing systems are being updated very rapidly, any direct comparison of TCBWorks with other systems would become quickly outdated. In general, as we write this in early 1998, most other Web groupware systems could be classified as Web conferencing systems. These differ significantly from the TCBWorks type of groupware in three major ways.

![](/api/attachments/F9BBGCE8/fulltext/images/5bbc1b14ef8daee5cf835374f1b4ad1ef856f072c34ed6ed08cf6219a676d439.jpg)  
Figure 3. Comment Discussion Screen

First, Web conferencing systems typically organize each comment as a separate entity within the overall structure of the discussion. Each comment has a title and lists the author's name; anonymity is rare. Each comment that replies to another comment is usually indented below the original comment. This tends to emphasize the unique focus of each separate comment, rather than the structure of the overall discussion. Structure follows the comments, rather than comments following the structure. Discussions with many replies often present a visually complicated display with many indented comments.

In contrast, TCBWorks' comments are subordinate to the overall structure. The structure changes only when the organizer or participants explicitly choose to modify it. All comments about the same topic in the structure flow together, with related comments flowing like paragraphs. Comments can be anonymous if the organizer so chooses. The disadvantage of this approach is that individual comments can get buried within the structure and are not as highlighted as they are in the conferencing approach.

Figure 4. Voting Screen  
![](/api/attachments/F9BBGCE8/fulltext/images/55934b34bdc297c45226d9cfcc2c630986a78a198c4901eccf3e4fce82df624d.jpg)

A second major difference is the ability to organize comments and selectively allow or restrict participants' ability to perform different functions. Few Web conferencing systems enable users to combine, move, edit, or delete comments and topics. The few that do usually restrict these capabilities to the system administrator and provide little capability for selectively sharing them with users. This again fits the intent of the two types of systems. Web conferencing systems often are intended to share information to be read once, much like e-mail, whereas systems such as TCBWorks are designed to enable groups to build and edit pools of information.

Finally, TCBWorks enables users to vote and make decisions. Most Web conferencing systems do not, simply because this is not their intended application. Voting is not useful for all groups or tasks. In some cases, groups can reach decisions solely through discussion. In other cases, voting allows the group to quickly identify the true opinions of each member and focus discussion on the areas of disagreement, rather than spending time discussing issues on which the members agree. Voting also helps bring closure and clearly indicates the support or lack thereof for some positions by forcing the silent majority to express their opinions. Without voting, dominant individuals may force the group to spend many hours discussing lost causes or issues on which the group already agrees.

## User Experiences with TCBWorks

MORE THAN 200 ORGANIZATIONS HAVE USED TCBWorks, with at least one installation on every continent except Antarctica. A commercial version is now available (called Consensus @nyWare) at www.softbicycle.com.

At present, we know very little about how Web groupware systems such as TCBWorks are being used. Although TCBWorks and other Web systems are designed to support discussion and collaboration across space and time, users often adapt tools in ways not intended by their designers $[6]$ . Thus, one fundamental question is: How are Web groupware tools being used?

We argued previously that Web-based groupware systems offer the same ubiquitous reach as e-mail and listservs (in contrast to today's proprietary conferencing and groupware systems), but offered benefits such as more structured discussions. A second fundamental question is: What are the advantages and disadvantages reported by Web groupware users?

## Research Design

We decided that the best way to answer these questions was through a combined interview and survey approach. The interviews would provide an in-depth understanding of how TCBWorks was used, while the survey would provide more breadth.

We conducted interviews with up to three members of four organizations that had used our software. Two organizations were still using the software, but two had stopped. Conducted over the telephone or via e-mail, the interviews began with two principal questions (which follow), but flowed differently for each interviewee. Individual responses to these questions were pursued and took each interview in a slightly different direction.

1. Please describe how you are using Web groupware. A few scenarios would be useful.

2. What do you see as the biggest advantages and disadvantages of Web-based tools?

The survey also focused on these questions. Given the rather immature state of the field, we chose to use open-ended, qualitative survey questions to determine how organizations used Web groupware and what benefits and problems they experienced. Surveys were e-mailed to 237 potential respondents, with a second “mailing” sent one month later. None of the organizations or respondents had any affiliation with the developers or the University of Georgia. We received responses from seventy-nine organizations (a response rate of 33 percent). Of these, ten were not usable. In two cases, our contacts forwarded the survey to others within their organization and asked them to respond too. In two other cases, faculty teaching groupware courses sent reports from their students who had used Web groupware. Including the multiple responses from these organizations, we received a total of 105 useable responses for analysis.

We performed three analyses on the survey responses. First, we identified the types of applications for which the Web groupware was being used (we examined the entire response, not just that specifically pertaining to that question). Once we had identified the specific applications, we organized and grouped them into general themes (e.g., quality teams and business process redesign teams were grouped under a general heading of project teams). Second, we examined the entire response to identify the advantages and disadvantages of Web groupware reported by the respondent. Once again, specific advantages and disadvantages were grouped and organized into higher-level themes. Finally, we examined the responses for “interesting” observations and insights that did not fall into any of the given categories, paying particular attention to the most successful adopters (or at least the most enthusiastic) and least successful (the discarders).

## Applications

The first analysis attempted to understand the ways in which Web groupware was being used (or had been used, in the case of the discarders). Figure 5 summarizes the results, based on our sample of sixty-nine organizations. Several organizations reported two major ways in which they were using Web groupware, so the numbers in figure 5 sum to more than 100 percent.

One major application was to support the work of project teams. Five organizations reported using Web groupware for project teams who met in decision rooms. Here, it was used to support face-to-face decision making in the same way as traditional proprietary group support systems such as GroupSystems or VisionQuest. The goal was to improve group performance and reduce the time spent in face-to-face meetings.

Fifteen organizations (20 percent of those in our sample) reported using it to support colocated teams—teams that worked in the same location (e.g., the same building) but who used it to support different time and place meetings. Most organizations in this category reported using it to supplement regular face-to-face non-groupware team meetings. In most cases, it was used as part of meeting preparation. For example:

\- For “meeting scheduling, mostly. An agenda and topics can be set up beforehand, and voting/polling questions can be set up as well to avoid spending lots of time on ‘tangents.’”

\- For “discussion groups of key subjects pertaining to problems that are to be discussed in upcoming meetings. Hopefully, this would shorten the meetings by allowing the participants to complete all but the final discussion and decision of any given project, thereby freeing the participants for more productive tasks.”

Interestingly, no organization reported using the software to continue discussions started in meetings. Face-to-face meetings were seen as sources of closure, not for initiation of new items to be discussed asynchronously.

![](/api/attachments/F9BBGCE8/fulltext/images/c5e607d0c9d5952f8afc51a76869c22147a4977c98777a7ccfc0046b27c66c71.jpg)  
Figure 5. How TCBWorks Is Used

The most common use of the software was to support project teams located in different cities or different countries for whom communicating between meetings was difficult. Web groupware was seen as a “complementary form to conventional face-to-face, one time, one location meetings.” Team members used the software to “examine and perhaps vote on issues through the Internet, at the location and time of their convenience (including if the Professor is on a trip out of town, which frequently occurs) eventually responding [to] requests without delay as soon as they are received independently of conventional meeting dates.” Once again, the software was primarily used to supplement (not replace) existing face-to-face meetings (held outside of decision rooms) and to improve communication between these meetings. A comment by one organization was typical: “We have no plans of using EMS [electronic meeting system] within the same location and timing although that it is not out of question; it could perfectly well later take that option into consideration.”

One major unexpected use of the software was for educational purposes, primarily at universities. The first—and in hindsight most obvious—educational application was its use in teaching groupware. Due to the ease of accessing the system over the Web, and the fact that virtually all university computing labs have Web access, using the system to teach groupware concepts was quite natural.

Two other education applications were to supplement or replace the face-to-face teaching of a course. In the colocated category, instructors used the software to extend class discussions outside of class in addition to traditional teaching. In the distributed category, the software was used to teach courses that did not have face-to-face class meetings. For most of these organizations, the software supplemented other media, such as phone or traditional mail correspondence courses. For some users, the software replaced other media.

For example, the University of Pittsburgh used TCBWorks to run an entire course on competitive intelligence over the Internet. Class discussion was conducted in a structured manner. First, students reviewed the session outline, objectives, key concepts, readings, and topics for discussion. Second, the professor initiated the discussion by summarizing the session topic and raising points for deliberation. Third, students continued the online discussion, initiating ideas and following up on comments in the manner of a normal discussion.

The third major category of applications was a catchall. The most common “other” application was to support special interest groups—that is, to replace listservs. One example is the Electronic Technology Group of the African Studies Association, a group of information technology researchers with interests in Africa. Their goal is to share information about research resources on Africa among universities in the United States and Kenya, South Africa, Zambia, and Uganda. Similarly, a variety of student groups at the University of Georgia and elsewhere are using the software within their campus (i.e., an intranet) to discuss students’ issues. Job hunting and course evaluations were typical applications. The key benefit here—and in the African example—is the ability to hold formal and informal discussions and to share information and opinions among groups of individuals with common interests in a more structured form than a newsgroup, listserv, or mailing list provides.

## Advantages

The most frequently mentioned advantage of Web groupware was its ability to enable any-place/any-time interaction (see figure 6). The reach of Web-based software truly meant that people could interact whether they were in the same building or anywhere around the world. Many respondents drew a sharp distinction between this ubiquitous access and the constraints of proprietary or LAN-based systems. This unlimited reach was often related to the next two most commonly mentioned advantages: the use of a client that was both (1) commonly available and (2) platform-independent. Several users commented on the advantages of providing the same tool to users of Windows and Macintosh computers—a telling observation about the importance of a common client (a Web browser) rather than a proprietary client that operated over the Internet. One user noted that he “was going to install RoundTable, but when the MIS manager learned that it required a two megabyte proprietary client installed on each desktop, [the MIS manager] said no.” For this organization, the added network management complexity introduced by installing additional software on each desktop greatly outweighed the benefits.

The remaining advantages focused mostly on the benefits to those using the software. The ability to provide very structured, anonymous discussions and an organizational memory capable of storing many different formats (e.g., gif, jpeg, html) at a low cost were mentioned by several organizations, although these advantages also are true of other forms of groupware to some extent.

![](/api/attachments/F9BBGCE8/fulltext/images/802a21a42213b2b562b8bc444e9da975c44fdc16b018c0cc68d0911ae5315168.jpg)  
Figure 6. Major Advantages Reported

## Disadvantages

In general, the disadvantages reported fall into three areas, the first and most prominent of which dealt with network technologies (see figure 7). Users were concerned about slow and unreliable networks and network security. Six percent of the responding organizations reported that the lack of Web access by some users was a distinct disadvantage. While some of these issues may improve as network technologies improve, they are likely to remain fundamental challenges facing Web groupware developers.

The second group of disadvantages centered on the current version of our software. The limitations of systems using Web browsers and html as the interface, systems administration problems, the lack of features, and too much structure were mentioned by a small but significant number of users. In our opinion, these issues are transitory, pertaining only to our current system; better-designed commercial systems that use Java are likely to overcome them.

The third group of disadvantages centered on two issues that were mentioned by only a few organizations: integration with other tools, and training and facilitation. Nonetheless, these fundamental issues will become more important over time. Our software was not integrated with any other tools; sending e-mail messages or creating graphics, for example, meant that the users had to use a separate tool. Embedding graphics (or other files) in messages required the user to FTP the files to a Web server first and then link to them in the software. While our software provided some editing and formatting capabilities, it lacked the full power of a word processor, so users preparing long documents preferred to write them in a word processor before cutting and pasting into our software.

![](/api/attachments/F9BBGCE8/fulltext/images/3d2be5ffd5054d39f52394e93269394c2f2371ac45532cf54f981eaaf85b589f.jpg)  
Figure 7. Major Disadvantages Reported

Taken separately, each of these activities is a minor inconvenience. After all, who would expect to create graphics using groupware software? Taken together, however, they present an interesting pattern. In order to work in groups, participants must perform an array of diverse activities. Users must master a set of rather diverse tools, each with slightly different interfaces and possibly incompatible data formats. This lack of integration among desktop tools and between desktop and groupware tools is a fundamental issue. Until it is simple both to create and to share text, graphics, and video with other group members through an integrated set of tools, collaboration will continue to be cumbersome.

Likewise, we believe that training users who are scattered in space and time and who rarely meet face-to-face is a crucial issue that will be faced in some degree by every organization that adopts Web groupware. While many users commented on how easy the system was to use (many more than reported problematic training as a disadvantage), few organizations had a formal training program. Most had users experiment with the system and learn it by themselves. The following comment was typical: “[It was] very simple. After a few false starts, I got the hang of things and have had no problems.”

Three organizations reported that the ability to restrict what participants could and could not do was important for training. When participants first began to use the system, it was important not to overwhelm them with the system's capabilities. One manager felt that “two buttons is one too many.” Once participants became familiar with the system, organizers allowed them to access more functions (i.e., buttons) such as deleting, moving, and combining comments and topics.

## Conclusions from Successes and Failures

In the foregoing analyses, we discussed the interview and survey data together. Here we examine the four organizations that we interviewed more closely. Two were successful in implementing Web groupware, but two were unsuccessful. The successes were a university distance learning program (not the University of Georgia's) that used TCBWorks to offer undergraduate courses across the United States over the Web, and a multinational technology firm that used it to extend the reach of its existing groupware room. The two unsuccessful organizations were an academic organization that used it to coordinate discussion and policy decisions, and a medium-sized newspaper that employed it in a groupware room and beyond.

Three general themes emerged from these four cases that are potential explanations for the differences between success and failure. The first was the reason for implementing the system. In the two successful cases, the organizations had a project with a specific need. The university wanted to test the use of the Web to support an existing distance education course taught by e-mail, while the multinational had a dispersed project team to support. The reasons for implementation were more general for the less successful organizations. Several members of the newspaper staff had participated in two face-to-face groupware sessions at a hotel, and when they learned that the hotel was closing its groupware room, they purchased the hardware to establish their own room. The academic organization decided to experiment with Web groupware after a spontaneous conversation between the organization's leader and the system developers.

The second theme involved the way in which the system was introduced to the potential users. In both successful cases, all users received training (a minimum of thirty minutes, sometimes as long as two hours) through a series of group classes or one-on-one sessions either in actual meetings or over the telephone. None of the members of the academic organization received training, and only the facilitators at the newspaper did.

The third theme had to do with critical mass $[14]$ . In both successful organizations, there were compelling reasons to use the system to communicate and to meet deadlines. In contrast, both discarding organizations explicitly cited a lack of interaction as one major reason for discarding it; that is, no one participated—there was no critical mass. There were no deadlines for the initial projects undertaken, so one major source of frustration was that users would connect to the system only to find that no one had entered any comments. After several tries, participants no longer made the effort to connect to the system. Perhaps these organizations had members who did not need to discuss issues as much as originally believed, or for whom the broadcast or “push” approach of e-mail and listservs was more appropriate than the “pull” approach of the Web groupware system.

The students in the distance learning class also felt this lack of a critical mass. They complained about the “lack of immediate feedback from colleagues” when they entered comments. In response, the instructor altered the course so that instead of permitting any-time interaction, all students had to participate in a one-hour discussion session scheduled every week at a specific time. This approach was more restrictive but better enabled the group to use the software. Almost all students considered this an improvement, although one student commented that this same-time interaction put slow typists at a disadvantage.

## Lessons Learned

## Technical Issues

WE HAVE LEARNED MANY LESSONS FROM DEVELOPING AND USING TCBWorks, both technical and user-based. The first major technical lesson is that, thanks to a Web browser, it is possible to develop a major application system on the Web. The use of a Web browser such as Netscape as the client environment offers distinct advantages and disadvantages over traditional system development.

First, because a Web browser provides many built-in functions, development proceeds much faster than it would in a traditional environment. Traditionally, 60 to 80 percent of any system is the user interface. With Web-based development, much of the interface is automatically provided by the browser; you only need to specify what functions to use. Interface coding is reduced to about 40 percent of the application, saving a significant amount of programming time. The disadvantage is that one is limited to the browser's capabilities.

A second technical lesson was security. If security is important, a secure Web server that encrypts packets can be used. Most servers also can restrict access to only certain Internet addresses (e.g., within one company or set of companies). The problem occurs if users regularly use CompuServe or other commercial access providers, because one must grant access to all users of those services—not a very satisfactory solution.

Our system has a moderate level of security in addition to that of the Web server itself. Each time a user logs in with a correct userid and password, the user is assigned a randomly generated authentication code that is valid until the user logs out or until twelve hours have elapsed, whichever comes first. This code is the user's access into the database; without it, access is denied. It also prevents someone from placing a bookmark in the middle of the system to bypass the login process, or “stealing” a packet and using its information to gain access. You can still bookmark a screen or steal a packet, but the authentication code granting access will be useless after logout or after twelve hours.

A third issue was the importance of testing the system on many computers and browsers. Netscape, for example, produces slightly different displays for the same html form when running on a UNIX machine, a Macintosh, or in Windows. The type of display (14-inch versus 17-inch) can also make enormous differences in the readability of graphics, particularly background graphics. Many users with low-resolution monitors complained that they could not read the text on the screen because of the background gifs we used in the first version of the software. After several trials, we found some simple background gif files that add color but do not detract from the actual material.

A final technical issue is the rapid evolution in de-facto standards. Most de-facto standards begin as one vendor's extensions to the existing standard. Initially, these extensions are proprietary but are rapidly incorporated by other vendors. But not all extensions become de-facto standards. For example, while most of the extensions to html proposed by Netscape and Microsoft have been quickly copied by the other's web browser, the same is not true for their APIs offered as improvements to CGI; Netscape Server API (NSAPI) and Microsoft's Internet Server API (ISAPI) are not compatible.

Identifying such shifts in de-facto standards early enough to incorporate the benefits they offer quickly is difficult. Even more challenging than addressing these evolutionary changes is facing the dramatic changes a technology revolution imposes. For example, the adoption of Java renders much existing program code irrelevant. Rewriting software to use these new standards places an immense strain on resources and programmer learning, whether the application is for research, internal use, or commercial application.

## Individual, Group, and Organizational Issues

We also learned several important lessons about users' needs and expectations. Learning about the software, and making an informed decision about its fit with a specific organization's needs is simplified by using the Web. Since it is Web-based, anyone with a Web browser can experiment with it. About twenty organizations have established databases on our server as a trial before deciding to install it on their own servers.

Most users have been quite enthusiastic about the software. Those who are less enthusiastic see it as a regular desktop application and hold it to the same standards. They expect to use all the standard interface concepts such as double-clicking to open topics, dragging-and-dropping to move, and using pull-down menus with multiple windows. These simple operations are beyond the capabilities of systems built with today's Web browsers. Until the next generation of browsers and Web groupware systems with Java become more common, we will not be able to satisfy those users.

Another issue concerns response time. In general, every request issued by the user results in a request sent to the Web server. Response times vary depending on network traffic. Most intranet users have reported response times of 1–2 seconds, or less. Response time across the Internet varies tremendously. While some North American and Asian users have reported response times that are also 1–2 seconds (even Japanese users accessing our U.S. server), most response times are considerably longer. Even moderately longer response times (3–4 seconds) can prove extremely frustrating, because they occur after every command (i.e., button click). Several users have discontinued use of the software because the response times proved too frustrating.

Java also offers opportunities to overcome this problem to some extent. Java is multithreaded, which means it is possible to separate transactions from the network. For example, when a new item is added, or an existing one deleted or changed, Java can display the results on the client immediately and then start a new thread, which operates in the background to send the update to the server. The user need not wait until the transaction is complete before continuing. Obviously, an action that requires the server to provide information will still introduce delay, but the decoupling of input from its processing will help immensely.

One interesting observation is that the use of structure was cited both as an advantage (by 9 percent) and as a disadvantage (4 percent). On the plus side, the ability to impose a structure on discussions to focus them and a structure that remained stable as participants entered replies to comments were benefits; however, the use of structure to develop many discussion topics tended to fragment the discussions into too many pieces. This had practical consequences; for example: “There were too many topics, and you have to keep checking to see if someone has posted a comment in every topic.” It also had cognitive consequences: “It is comparable to being at a party and trying to involve yourself in three semi-related discussions. You are not able to fully integrate yourself in any one of the discussions plus you run the risk of annoying the people you are talking with since your attention is divided.”

We believe that the issue of structure is fundamental. Identifying the “right” number of topics for discussion is difficult. A recent study suggests that imposing structure on discussions by dividing them into several topics can significantly improve their depth and quality $[5]$ . As noted here, however, more topics means more discussion areas that participants must follow. There must be a balance so that the number of topics does not become unwieldy. Several organizations reported that three to five topics seemed to work well for their discussions (three were used in the prior study $[5]$ ), but additional research is needed before we attempt to choose an “ideal” number of topics.

One major advantage cited by participants was the ability to work any place and any time. But this definite plus probably played a role in the system's failure in several organizations because participants would connect to the groupware system only to find that no one had entered any comments. After several such experiences, participants no longer tried. There was not a sufficient critical mass [14]. (Of course, there may have been other factors leading to failures, such as the quality of the system and the type of tasks for which the system was used.)

We believe that the critical mass issue is fundamental. Web groupware is a pull technology that requires users to deliberately access the system, unlike e-mail, which is a push technology. If users find discussion scant, they are likely to abandon it. This issue has been well studied in the context of e-mail $[14]$ , but we are aware of little research in the groupware area. Some implications for managers are clear. When implementing Web groupware, ensure that there is a critical mass of users that can benefit from regular discussion. Otherwise, the investment is not likely to succeed. During the initial implementation, strategies such as promoting same-time/different-place discussions for certain groups may be beneficial in building the necessary critical mass.

Most of the installations and users of the software were new to groupware, and a significant proportion were also new to the Internet. We had erroneously believed that many of the initial users of our Web groupware system would be users of existing groupware interested in expanding its reach—which was, in fact, true only of the instructors teaching groupware courses. The significant proportion of installations and users new to groupware suggests that we may soon see an explosive growth in the acceptance of groupware in “mainstream” computing, making it into more of a standard application.

This also has implications for the way systems are introduced to users. Training was a key difference between the successful and the unsuccessful organizations; the successful organizations trained users, the unsuccessful ones did not. It is also interesting to see the type of training provided. The two successful organizations we interviewed (and several others in the survey) provided training on both the technology (e.g., which keys did what) and the new work structures and behavior norms. For example, several organizations provided rules of etiquette (e.g., “no flaming”), gave examples of use and process guidelines (e.g., idea generation, then idea consolidation, and then voting), stressed the importance of “meeting planning,” and discussed the structuring of work using the outlining capability embedded in the software. While we have no direct evidence, we believe that this training, both in using the technology and perhaps more importantly on the new work processes required, was an important factor in successful adoption. We recommend that managers plan for training (both technology-specific and work process requirements) when implementing Web groupware, especially in cases where group members are geographically dispersed. While this may seem obvious, we failed to provide adequate training when we assisted the two ultimately unsuccessful organizations.

In the cases of distributed teams, distributed classes, and special interest groups, many of the participants were also new to each other. Even the relatively “lean” media provided by the Web groupware system (see $[2, 17]$ ) enabled members to build relationships. Some typical comments included: “Some of the members feel like friends” and “I have a perception of them as [to what] they think and where they are coming from.”

## Conclusions

Web-based groupware can encourage more organizations to consider using groupware to improve communication and can help build virtual communities where members work together and share a sense of each other and of being part of the organization, even if they do not meet in person. However, technology alone cannot create virtual communities. Two organizations in our interviews and several from the survey installed the software but no one came to use it. Without a compelling need or desire to interact, participants in these organizations did not build a virtual community.

We believe that we are on the edge of a revolution. Within a year, most organizations will realize that the Web is not only a means of electronic publishing but a way to build and maintain virtual organizations and communities. Web groupware will play a key role in building these communities. Even systems designed solely for internal use (that do not access the Internet) will allow individuals with similar interests and needs to form virtual communities. Of course, the Web will need to mature, and the need for traditional groupware applications will remain, but more and more groupware applications will use the Web instead of proprietary operating systems and networks. Those who get to the Web first, learn its intricacies, and push its limits will have a distinct advantage.

## REFERENCES

1. Collaborative Strategies. Clearinghouse for Information on Collaboration Technologies, Tools and Methods. http://www.collaborate.com, 1996.

2. Daft, R.L., and Lengel, R.H. Organizational information requirements, media richness and structural design. Management Science, 32 (1986), 554-571.

3. Dennis, A.R., ed. Groupware Central. http://www.cba.uga.edu/groupware/groupware.html, 1996.

4. Dennis, A.R.; Quek F.; and Potheri, S.K. Using the Internet to implement support for distributed decision making. In P. Humphreys, L. Bannon, A. McCosh, P. Migliarese, and J. Pomeroi (eds.), Implementing Systems for Supporting Management Decisions: Concepts, Methods, and Experiences. London: Chapman and Hall, 1996, pp. 139–159.

5. Dennis, A.R.; Valacich, J.S.; Connolly, T.; and Wynne, B. Process structuring in group brainstorming. Information Systems Research, 7 (1996), 268–277.

6. DeSanctis, G., and Poole, M.S. Capturing the complexity in advanced technology use: adaptive structuration theory. Organization Science, 5 (1994), 121–147.

7. Fellers, J.W.; Clifton, A.; and Handley, H. Using the Internet to provide support for distributed interactions. Proceedings of the Twenty-Eighth Annual Hawaii International Conference on System Sciences, Maui, 1995, pp. 52–60.

8. Hiltz, S.R. Online Communities: A Case Study of the Office of the Future. Norwood, NJ: Ablex, 1984.

9. Hiltz, S.R., and Turoff, M. The Network Nation: Human Communication via the Computer. Reading, MA: Addison-Wesley, 1978.

10. Hiltz, S.R., and Turoff, M. The evolution of user behavior in computerized conferencing systems. Communications of the ACM, 24 (1981), 739–751.

11. Hiltz, S.R., and Turoff, M. Structuring computer-mediated communication systems to avoid information overload. Communications of the ACM, 28 (1985), 690–699.

12. Hughes, J. MiniSQL Product Information. http://hughes.com.au/product/msql, 1996.
13. Hughes, J. MiniSQL—A Lightweight Mini SQL Database Engine [source code] ftp://bond.edu.au/pub/Minerva/msql, 1996.

14. Markus, M. Toward a critical mass theory of interactive media: universal access, interdependence and diffusion. Communication Research, 14 (1987), 491–511.

15. Nunamaker, J.F.; Dennis, A.R.; Valacich, J.S.; Vogel, D.R.; and George, J.F. Electronic meeting systems to support group work. Communications of the ACM, 34, 7 (1991), 40–61.

16. Quek, F., and Tarr, I. An example of the use of the WWW as a tool and environment for research collaboration. IFIP Working Group 8.4 Conference Proceedings, Tucson, 1996.

17. Rice, R.E. Task analyzability, use of new media, and effectiveness: a multi-site exploration of media richness. Organization Science, 3 (1992), 475-500.

18. Silver, M.S. Decision support systems: directed and non-directed change. Information Systems Research, 1 (1990), 47–70.

19. Vallee, J.; Johanson, R.; Randolph, R.; and Hastings, A. Group Communication through Computers, Social, Managerial and Economic Issues, vol. 4. Menlo Park, CA: Institute for the Future, 1978.

20. Woolley, D.R. Conferencing on the Web. http://freenet.msp.mn.us/people/drwool/webconf.html, 1996.
