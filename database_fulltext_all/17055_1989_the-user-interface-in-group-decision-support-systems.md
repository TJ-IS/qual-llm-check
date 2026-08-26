---
otero_id: 17055
otero_key: "D9W2F6J3"
title: "The user interface in group decision support systems"
authors: "Paul Gray; Lorne Olfman"
year: "1989"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(89)90002-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The User Interface in Group Decision Support Systems \*

Paul GRAY and Lorne OLFMAN

The Claremont Graduate School, Claremont, CA 91711, USA

The human interface is a critical success factor for group decision support systems (GDSS). The user interface design problem for such systems is more complex than that for individual work stations because it involves consideration of the public and private screens and their interactions, the physical environment of the facility, the response time of the network, and the cognitive style and cultural differences among users. This paper explores five interface design issues that are specific to decision support systems for groups: the design of the public screen; the interaction between the private screens and the public screen; the design of the individual's interaction with the system as a whole; the effects of varying cognitive style, and the implications of cultural differences among participants particularly in international GDSS. The design issues are illustrated by the interfaces provided in four experimental GDSS's (U. of Arizona, Claremont Graduate School, U. of Minnesota, and XEROX PARC). These systems are all of the single room type, where participants are present at the same time. The interfaces described range in approach from simple listings, to conventional microcomputer interface, to near typewriterless interfaces using touchscreens, to a highly sophisticated "what you see is what I see" (WYSIWIS).

Keywords: International Group DSS, Computer Interfaces, Decision-Making, Decision Laboratories, Electronic Meetings.

## Introduction

To the user, the system is the interface. For decision support systems, human-computer interactions can be analyzed in terms of Bennett's (1983) three questions:

1. What does the user see at the terminal?

2. What must the user know about what he sees at the terminal?

3. What can the user do with the system in order to accomplish the purpose of using the system?

These three questions, originally formulated for individual DSS design, apply equally well to group decision support system (GDSS) design. In considering GDSS design, several additional factors have to be considered:

![](/api/attachments/D9W2F6J3/fulltext/images/a565896ffe7c6b89810593dcd0be7b70a88de266ce138564a3fd39d7ee84ab76.jpg)

Paul Gray is Professor and Chairman of Information Science at The Claremont Graduate School, Claremont, CA, USA. He has been involved in decision support systems, computer based modeling, and simulation for many years in both research institutes and universities. He began work in Group Decision Support Systems in 1980. He received his Ph.D. in operations research from Stanford University and holds degrees in mathematics and electrical en-York University. The University of gineering from New York University, The University of Michigan, and Purdue University. He spent most of the 1960's at Stanford Research Institute. Since then he has been a professor at several universities, including Stanford and the University of Southern California. He was general Chairman of DSS-86, the International Conference on Decision Support Systems. He has been Secretary (1975-79) and Vice President-at-Large (1983-86) of The Institute of Management Sciences.

![](/api/attachments/D9W2F6J3/fulltext/images/f4cb13501c0da3ec7815701b1902c65f65dbd5e0f97be8fd8ee66e91a2466192.jpg)

Lorne Olfman is Assistant Professor of Information Science at The Claremont Graduate School. He has a PhD in MIS from Indiana University and also degrees in Computing Science and Economics. He held various jobs in both the public and private sectors in Canada. His current research and teaching interests include systems development methodologies, end-user computing, and group decision-making. He has co-authored a number of papers and articles on

end-user training.

1. The design of the "public screen(s)".

2. The interaction between the public screen and the individual screen.

3. The design of the individual's workstation in the group environment.

4. Cognitive style differences among participants.

5. Cultural differences among participants.

These additional considerations increase the dimensionality of the interface problem. In terms of what the user of a GDSS sees, the focus is on both private and public screens. What the user must know includes individual and cultural style differences. What the user does with the system expands to include interactions with other participants and possibly a chauffer and/or facilitator.

In this paper, we explore the issues involved in interface design. We limit the discussion to GDSS's in which all the participants are in the same room at the same time. (For a discussion of other GDSS arrangements, see DeSanctis and Gallupe, 1985). That is, systems in which the group is involved in a conference whose purpose is either cooperative work or decision making. To illustrate the design issues, we describe existing interfaces developed at the University of Arizona, The Claremont Graduate School, The University of Minnesota, and XEROX Palo Alto Research Center (XEROX PARC) in a series of exhibits.

## The Interface in a Group Decision Support System

In a GDSS used to support conferencing, the basic structure is that of a set of individual DSS terminals interconnected by communications (Huber, 1984; Bui and Jarke, 1986; Gray, 1987). What distinguishes a GDSS technically from an office automation system built around a local area network is that the participants are not only in the same room, but work together simultaneously on the same problem or decision. In so doing, the GDSS requires software that supports the group as a whole and hardware/software combinations that can cope with periods of high demand when the group is performing a joint function such as voting or ranking alternatives.

GDSS can be provided at various levels of the organization. In this paper we assume that the users are senior executives. This assumption leads to some criteria, such as “executive look and feel”

and rapid response time, that can be relaxed if the system is to be used at lower levels. We also assume a system that is multipurpose. That is, the system can be used for a wide variety of cooperative work and decision tasks. Because business dealings increasingly involve people from different cultures and countries, we consider the interface issues associated with multicultural situations.

The typical arrangement consists of a conference table or tables in which

– each participant has access to a personal computer (or a computer terminal) which serves as a private interface,

\- one or more large displays that can be seen by everyone and serve as “public screen(s)”.

The displays for individuals are networked so that information can be routed among individuals and between individuals and a file server. For access to large data bases and specific software, the network maybe connected to a mainframe. Some facilities rely on keyboard input. Others provide mouse and/or touchscreens to reduce the need for typing.

A special case is the display provided to the "chauffeur". The concept of chauffeur in GDSS is that of an individual who is skilled in using the technology. The chauffeur may be the conference leader, a conference member, or a trusted assistant. It is the chauffeur's role to facilitate the flow of information between conference members and the public screens during the meeting. Thus, the chauffeur controls not only his/her own display but those seen by the entire group.

Most facilities provide software that is specifically related to supporting the group as well as that normally available in standard or custom packages for individual support. Typical of these additional software packages are

\- software to support the chauffeur and the chairperson in running the meeting.

\- software for voting, ranking, rating, and other means for determining the group's preferences.

\- software for processing the information generated by the group. These functions include collecting, retrieving, sorting, editing, analyzing, and displaying information created by group members.

The interfaces for this GDSS-specific software are the subject of this paper.

During our discussion of the interface issues, we present exhibits that describe four example interface concepts. These examples have been chosen from four of the centers at which GDSS research is underway. The examples are not necessarily the most advanced available at these facilities. They were chosen to illustrate differences in approaches and as examples of design choices that were made. Although the systems necessarily reflect current technology, these examples should be taken to be representative of the broader underlying principles involved. Table 1 compares the characteristics of the four example systems. Arizona and Claremont have more than one system but only one is described here.

## Issues in Design

## Issue 1: The Design of the “Public Screen(s)”

The public screen is typically a display at the front of the room that is seen by everyone in the conference. Its purpose is to provide a common focus around which the discussion flows. In most current systems, only one person controls what is shown. Design decisions that have to be made involve technical, organizational, and cost issues. The distinctions are not clear cut since the technology affects what can be done organizationally, organizational imperatives can drive technical decisions, and budget limitations may be decision factors. The following is a brief discussion of the design considerations for the public screen.

## 1. One Screen or Multiple Screens

Public screens involve projection of some display device. Each screen is limited to the lesser of the underlying resolution of the display device and the projection device. For example, CGA graphics from a PC are limited to 80 characters per line and 25 lines. Projection devices on the market are related to the resolutions available in CGA, EGA, and VGA formats, with each step in increasing resolution coming at escalating cost.

In many situations, the small amount of information available on the PC screen is just not sufficient. This is particularly true for the many situations where windowing is desired to compare several alternatives simultaneously. For this reason, Arizona in its large facility (and Claremont) use multiple public screens, each of which may be windowed. Experience in multi-screen video indicates that people can absorb information from several sources simultaneously. Multiple screens can be used in various ways. For example, the screens may project long lists that require more than 25 lines; or one screen may have reference information on it (e.g., historical performance graphs), while another has currently changing information (e.g., charts belonging to the presentation being made). One screen may show the base case in a spreadsheet while the other shows the what if case.

In multinational discussions, where the same information has to be displayed in each of several languages, multiple screens become imperative unless participants can accept small windows.

## 2. Resolution

As alluded to above, the designer must choose the resolution to be displayed. Usually the intent is simply to project the same display on the public screen as on an individual Personal Computer screen, such as the chauffeur's. In this case, the resolution decision is simple. The problem becomes more complicated if the private screens are high resolution. Currently, about \$1000 buys a monochrome 19-inch screen with pixel resolution that allows two 8 1/2 by 11 inch typewritten sheets to be displayed in "what you see is what you get" mode. Such resolution is available on the very large public screen at XEROX PARC (see Exhibit 4). To achieve it, however, requires a highly expensive light valve mounted in a separate room.

High resolution is needed in systems that support complex visual decisions such as are involved in packaging or engineering design. Consider a group discussing packaging design for a new product to be produced in country A for sale in country B. By using the graphics capabilities on the public screen, people from both cultures can see how the package will appear and can alert one another about culturally sensitive issues such as symbols or colors.

Although higher resolution can increase what is seen on a single screen of given size, there are limits to the smallest lettering that the eye can discern. The desire and need for an ever increasing amount of information displayed will push people to multiple high-resolution screens.

Table 1  
Comparison of Systems.

<table><tr><td></td><td>Arizona *</td><td>Claremont *</td><td>Minnesota</td><td>Xerox</td></tr><tr><td colspan="5">Equipment</td></tr><tr><td>Manufacturer</td><td>NCR</td><td>HP</td><td>NCR</td><td>Xerox</td></tr><tr><td colspan="5">Configuration</td></tr><tr><td>Network</td><td>PC Net or Token ring</td><td>Ethernet</td><td>Hardwired</td><td>Ethernet</td></tr><tr><td>Number of Stations</td><td>16</td><td>9</td><td>5</td><td>4</td></tr><tr><td>Operating System</td><td>DOS</td><td>DOS</td><td>UNIX</td><td>XEROX</td></tr><tr><td>Software Language</td><td>PASCAL</td><td>BASIC</td><td>C</td><td>INTERLISP</td></tr><tr><td colspan="5">Public Screen</td></tr><tr><td>Vendor</td><td>BARCO</td><td>LIMELIGHT</td><td>SONY</td><td>HUGHES</td></tr><tr><td>Projection</td><td>Front 10&#x27;</td><td>Front</td><td>25-inch TV</td><td>Rear, full wall</td></tr><tr><td>Color</td><td>RGB</td><td>Green screen</td><td>Green screen</td><td>Black &amp; white</td></tr><tr><td colspan="5">Workstations</td></tr><tr><td>Type</td><td>PC</td><td>PC</td><td>Terminal</td><td>Workstation</td></tr><tr><td>Screen Size</td><td>13&#x27;&#x27;</td><td>12&#x27;&#x27;</td><td>12&#x27;&#x27;</td><td>19&#x27;&#x27;</td></tr><tr><td>Color</td><td>yes</td><td>no</td><td>no</td><td>no</td></tr><tr><td>Mapping</td><td>character</td><td>character</td><td>character</td><td>bit-mapped</td></tr><tr><td>Primary Mode of Interaction</td><td>keyboard</td><td>touch screen</td><td>keyboard</td><td>mouse, icon</td></tr><tr><td>Principal Use</td><td>Planning, Decision making</td><td>Decision making</td><td>Decision making</td><td>Cooperative design work</td></tr><tr><td></td><td>* Refers to the smaller of the two systems at Arizona</td><td>* Refers to one of three sys-tems at Clare-mont</td><td></td><td></td></tr></table>

## 3. Color vs. Monochrome

Both systems at Arizona and one at Claremont use color projection. Minnesota and XEROX use monochrome. Cost and resolution considerations both enter into this choice. Color is more expensive for a given resolution. The choice, however, is almost predefined. Public screens should match the private screens.

## 4. Speed of Response

The public screen (and private screens) should paint as quickly as possible. Thus, the underlying computer driver should have quick response. In a world in which they have 12 to 20MHz personal computers on their desks, executives will not put up with waiting for the screen to paint. If the GDSS is tied to a mainframe, high-speed communications must be provided. 1200 or 2400 baud does not do; 9600 baud or better is recommended.

## 5. Location of Screen

The public screens must be visible to everyone. The usual arrangement has been to put the screens in the front to the room. In the large Arizona system and at XEROX PARC, people are arrayed in a row and face the large screen, which is rear projected. In the small Arizona system (Exhibit 1) and at Claremont (Exhibit 2), people are in a U-shaped arrangement where they can see one another and can also see the screen. However, in the U-shape, people who are close to the screen are at an angle and people who face the screen are furthest away. If a curved screen is used to increase the sharpness of the display head-on, then the screen starts blurring for people who view it at large angles.

The U-shape allows everyone to talk directly to everyone else on a line of sight but makes public display design more difficult. Putting the public screen perpendicular to the discussion as in the Minnesota facility (Exhibit 3) forces people to choose between face-to-face discussion and the public screen. Putting people in rows makes public display design easier but reduces eye contact and results in verbal discussion flowing principally between individuals and the chairperson.

The choice of seating arrangement is also affected by the culture in which the meeting takes place. For example, the U-shaped arrangement would not be appropriate for a negotiation in Japan because people want to be physically opposite one another. Thus, choosing an inappropriate configuration can prevent shared understanding.

## 6. Controlling Public Screen Content

Controlling the public screen controls the flow of the discussions. Thus, the person who decides what is shown has power in the meeting. One approach is to give control to the conference chair or to the chair through the chauffeur. A second approach, used in the Minnesota GDSS software is to allow any individual to control the content of the public screen. A third is to have some form of Roberts Rules of Order in which the person currently speaking can display their work on the public screen. A fourth is reflected in the Arizona software shown in Figure E1-5 in Exhibit 1. Here, people make comments addressed to individuals on a panel. The software collates all the comments addressed to that individual for display on the public screen. The control problem becomes more complex with multiple public screens and/or multiple languages.

## 7. Cost

The larger the screen, the easier it is to view and the higher the resolution that can be used on the underlying driver. However, these desirable attributes come at increasing cost. Unfortunately, there are diseconomies of scale.

## Issue 2: The interaction Between the Public Screen and the Individual Screen

## 1. Relation of Private Screen to Public Screen

What is shown on the public screen should also be available on the private screens. This is particularly true when a presentation is being given. For example, someone is giving a briefing by projecting a series of charts using presentation graphics software. People should be able to look at that chart on their private screen as well on the public screen. Furthermore, they should be able to leaf through the presentation both forward and backward. In a sophisticated system such as Colab at Xerox Parc (Exhibit 4), the public screen is available on demand in a window on the private screen. As discussed in Issue 4 below, a sophisticated system allows the user to convert the format shown on the public screen (e.g., a bar graph) into their preferred format (e.g., column of figures)

Conversely, what is on the private screen should be movable to the public screen. Thus, if an individual has an idea (e.g., a favorable “what if” case) they should be able to have their private screen displayed for everyone to see. The rules of the meeting will determine whether they can do so at will or if they must go through the chauffeur or the chairman.

## 2. Editing Capability

At the next level of sophistication, individuals should be able to edit or annotate the copy of the public screen on their private screen. Such editing capability facilitates cooperative work. For example, if a contract is being negotiated, an individual may want to edit the text currently displayed and send it to the public screen. By windowing the public screen or by using multiple screens, the alternative proposal can be looked at side by side with the original.

## 3. Language Choice

For multicultural GDSS, group members should be able to work in their own language on their private screen irrespective of what language is being shown on the main public screen. For presentations, they should be able to leaf through the charts in the language of their choice. Where near-simultaneous translation is provided (see Issue 5), they should be able to show the public screen in their own language.

## Issue 3: The Design of the Individual Workstation in the Group Environment

## 1. Group Environment

The individual sits at a workstation that provides him/her with workspace, data entry device(s) and a private screen. Because a GDSS involves interpersonal interactions, the physical environment provided to group members individually and collectively is an inherent part of the human interface. The design of the work station requires attention to ergonomics. The workspace should be comfortable in seating (decision makers spend a lot of their time sitting!), lighting, and ambiance. The last implies an executive “look and feel” to the facility. Ample space should be available to lay out documents, notepads, and other personal items. Decision makers are important, well paid people who are used to having comfortable surroundings.

## 2. Input Devices

A variety of input devices can be used including keyboard, mouse, bit pad and touch screen.

A fundamental decision has to be made whether a particular piece of software will be typewriter based (e.g., Minnesota) or nearly typewriterless (e.g., Claremont). The conventional wisdom is to try to make real systems for executives as nearly typewriterless as possible. Although the younger generation was brought up on computers and is typewriter skilled, middle-aged managers often do not type or have a “typing-is-for secretaries” attitude. At Claremont, the keyboard is in a slide-out drawer under the table that allows it to be stored when not in use and increases the workspace available to the participants. In multilingual situations, the required keyboard mappings increase the complexity of using typewriter input.

The mouse, the bitpad and the touch screen are all alternatives to the keyboard. The touch screen requires the least skill and learning time. The bit pad allows people to write and draw, although the resolution is often quite poor. Furthermore, many people's handwriting is difficult to read. The mouse requires some training, but more and more people have mouse skills.

## 3. The Private Screen

By recessing the private screen in front of the participant so it is not a barrier to the line of sight, it does not interfere with discussion. People are able look at one another while talking. The arrangement at Minnesota, where the display is on a side table, reduces visual contact.

Selecting the size of the private screen involves a design tradeoff. To make screens less obtrusive, small screens are preferred. However, to increase the amount of information seen, larger screens are required. Bit mapped screens increase the amount of information that can be shown. However, reading small type is a problem for middle-aged executives.

## 4. Monochrome vs. Color

The choice of monochrome vs. color affects the private screens as well as the public screen. Color, even though it costs more for a given resolution, adds a dimension to the information displayed. However, many software designers do not understand how to use color effectively. Examples of commercial PC software with outlandish color use abound. If cost is a constraint, the tradeoff that a designer must make is between the use of color and the resolution of the display. As we move toward universal acceptance of EGA and beyond that to even better color resolution, the color issue will disappear. Software designers have to be particularly cognizant of the color blind male when choosing color combinations because the probability of one or more color blind participants becomes significant for large groups.

## 5. Number of Persons Per Screen

The Arizona and Claremont systems are set up so that two or more people can work comfortably at one workstation, whereas the Minnesota and XEROX PARC systems are basically one to one between people and screens. Multiple people per screen allow small subgroups of participants to discuss responses and reinforce one another. Such reinforcement often generates increased interaction during a meeting. A single user arrangement provides greater privacy but may result in individuals losing themselves in the screen rather than participating with the group.

## Issue 4: Cognitive Style

It is arrogant for the designer to assume that all users of a GDSS have the same cognitive style and that they come from the same cultural and language background. Working in a personal computer environment, it becomes possible to match individual cognitive style and to take cultural and language differences into account in interface design.

Cognitive style refers to the way individuals understand information most effectively. Cognitive style differences imply that a “one size fits all” approach to interface design should be avoided. For example, some people comprehend columns of figures most easily while others prefer bar graphs or pie charts or a combination of table and graph on the same screen. Although a GDSS is designed for group use, the technology permits custom tailoring the information display to individuals. A thoughtful designer will create interfaces that allow the user to select the form of presentation. Many commercial software packages allow users to set “profiles” according to their wish. Thus, a participant may create a chart as a bar graph and have it displayed as a line chart on the public screen and as a table on someone else’s private screen. (Note, however, that some of this advantage is lost if private screens are shared.)

## Issue 5: Cultural Differences Among Participants

Cultural differences also have to be accommodated in design of the interface. If a GDSS is to be used in a different culture or if it is to be used for an international conference involving, say, negotiation, then the designer has to look at additional interface issues. These issues include presenting information in different languages, translating from one language to another, and recognizing that colors and icons have different meanings in different cultures (Gray, Olfman and Park, 1988).

Group process is a set of behaviors. GDSS provide tools that help organize and formalize these behaviors. As shown in Figure 1, there are many layers that frame the group decision process. In the outermost layer, are beliefs and assumptions held by each of the participants (Wagner,

![](/api/attachments/D9W2F6J3/fulltext/images/4e048484c5e9981bd2a2c00f9b697c0b20dca9268e4da624761d8416f9086e43.jpg)  
Fig. 1. Frames in the Communications Process (from Bostrom, 1987).

1981). The group meets to focus on one or more problems (e.g., to negotiate a trade agreement). To reach the desired outcome, the group members must have rapport. "Rapport is the synergy, mutual trust and respect developed within the group" (Bostrom, 1987, p. 17). Rapport is a necessary factor in successful communications. It depends on a shared set of beliefs and assumptions about the world.

## 1. Beliefs, Assumptions, and Process

To establish rapport in a cross-cultural setting, individuals from each culture have to understand their counterparts' underlying beliefs and assumptions. The difficulty of achieving rapport is best underscored by the difficulty of understanding jokes and humor from radically different cultures. What is funny in one culture is not necessarily funny in another.

Similarly, it is important to understand how groups achieve outcomes. Each group in each culture has a set of rules and norms of behavior it follows in trying to reach closure. The computer lays an extra layer of behavior on top. People from different cultures can perceive the same graphics or images in different ways. Little is known about the implications of this phenomenon for GDSS. One helpful way of gaining insight about this problem would be, for example, for a group of Americans to observe the process of making a decision in a Korean “decision room”, and vice versa. Even if the participants do not speak the language, simply observing what users see, what they must know, and what they can do prior to undertaking a joint session should help improve the process. The old saw that you must place yourself in another person’s shoes to understand how they think and approach problems is indeed applicable.

## 2. Translation

Some method of translation must be available to display common text in different languages (and character sets). For simplicity, the following discussion assumes that only two languages are being used. Yet, the possibility of multiple working languages should not be ignored (e.g., the United Nations supports six working languages). The translation problem in a GDSS meeting involves both voice and text. That is, conversation must be translated as well as text and symbols on the screens. To gain an understanding of the translation process, we first consider voice translation.

Two types of voice-to-voice language translation systems usually provided are simultaneous and sequential. Simultaneous translation is geared toward providing “real-time” translation from one language to another. In a voice-to-voice simultaneous translation, the listener hears the words of the speaker in his/her own language just after the words are spoken. The speaker continues without interruption, and is generally only minimally aware of the translator’s presence. Simultaneous translation is not accomplished by transliteration (i.e., word-by-word), but depends on phrases and sentences to achieve the necessary context. As a result, even if the speaker is bilingual, he or she cannot tell whether the translation is accurate.

In sequential voice-to-voice translation, a spoken sentence (more likely a paragraph) is retold in another language after it has been completed. The speaker hears the translation and waits until it is finished before continuing. Like any dichotomous classification, simultaneous and sequential translation will tend to fuse together when the chunks being translated are small enough. As demonstrated by the scenarios in Exhibit 5, both forms of translation could be useful in an international GDSS.

Ideally, small, low-priced machines should be available to support highspeed, high accuracy translation between any pair of languages. Unfortunately, such translation capabilities will most likely not be available for a long time to come. Therefore, in the near term, computer generated information (text, spreadsheets, graphs) will have to be handled by skilled facilitators who translate the material and type it in. Low sophistication level translators such as on-line dictionaries, transliteration tools, and idiom translators will provide computer assistance to facilitators. Depending on the decision-making context and the methods available translation can greatly slow the group process.

The scenarios in Exhibit 5 describe how translation might be accomplished using current GDSS software. The frameworks for electronic brainstorming and issue analysis are from the University of Arizona (Exhibit 1), voting from Claremont Graduate School (Exhibit 2), and negotiation from New York University (Shakun, 1988).

The scenarios indicate that various levels of translation precision and speed are required to support international GDSS. The classification matrix in Figure 2 summarizes these variations. High speed translation capabilities and exact translations are only required in issue analysis; on the other hand, electronic brainstorming requires neither high speed nor fully accurate translations. One thing we can be sure of. Translation will not come cheap. It will require additional people in the room who have considerable technical skills, and whose skills are trusted by the participants. An advantage of existing unicultural GDSS is that people can leave the meeting having a record of exactly what happened. Considerable additional investment has to be made if this advantage is to be retained in international GDSS.

## Conclusions

The four interfaces described in the exhibits range in complexity from the simple listings of the Minnesota system to the sophistication of WYSIWIS of Colab at XEROX PARC. It is worth thinking about these interfaces in terms of Bennet's "what does the user see?, what must the user know?, what can the user do?" paradigm. Although the Minnesota system was the simplest to implement, this simplicity was obtained at the expense of the user. The user must know how to type and has to know the rules by which the system works. In the touchscreen system at Claremont, the user must only understand the implications of what happens when he or she touches the screen at a particular point. In the mouse-driven WYSIWIS system, with its emphasis on cooperative work and information sharing, the user has the most information displayed and has the greatest freedom of action. In its present configuration, it is designed for use by computer professionals. Because of its sophistication, even if the system is made available to executives, it is likely that it will require some time for novices to learn all the possibilities of what can be done.

![](/api/attachments/D9W2F6J3/fulltext/images/ced826db8d7653cbe6a27d23a02d7182d263a6d4e1ccfadb23be5dd4e4287e71.jpg)  
Fig. 2. Allowable Speed and Accuracy of Translation.

In thinking about these interfaces and how they are being used, it is clear that the combination of GDSS hardware and software provides a powerful capability for human parallel processing. In conventional meetings, where Roberts Rules of Order are followed and everyone speaks in turn, ideas are presented sequentially and the conversation jumps around from topic to topic. In GDSS arrangements, the participants all “speak” at the same time and hence a more efficient creation and recording of ideas takes place. The “piggybacking” of ideas is not lost because, as people work, they can see the input from others on the same topic and hence can add their responses to the discussion.

The interface is a critical success factor for decision support systems which is as important as the availability of appropriate software tools and proper training. For group decision support systems, the design of the human interface is more complex than that for the individual work station. It involves consideration not only of the private screen, but also of the public screen(s), the relation of the public screens and the private screens, the physical environment of the facility (e.g., lighting, executive feel), the response time of the network, the differing cognitive styles of participants, and cultural differences. In short, the interface has to be designed in a consistent manner using a systems approach.

## References

Bennett, John L. (ed.), Building Decision Support Systems, Addison-Wesley Publishing Company, Reading, MA (1983).

Bostrom, Robert P., Successful Application of Communication Techniques to Improve the Systems Development Process, Indiana University, IRMIS Working Paper # W709 (1987).

Bui, Tung X. and Jarke, Matthias, Communications Design for Co-oP: A Group Decision Support System, ACM Transactions on Office Information Systems 4 (April 1986) 81–103.

DeSanctis, Gerardine and Gallupe, Brent R., A Foundation for the Study of Group Decision Support Systems, Management Science 33 (May 1987) 589–609.

Gray, Paul, Group Decision Support Systems, Decision Support Systems Journal 3 (September 1987) 233–242.

Gray, P., Olfman, L., and Park, H., Design of the Human Interface for International GDSS, Claremont Graduate School Working Paper 88-1 (January 1988).

Gray, Paul, The User Interface in Group Decision Support Systems, DSS-88 Transactions, Providence, R.I: The Institute of Management Sciences (1988).

Huber, G.P., Issues in the Design of Group Decision Support Systems, MIS Quarterly 8 (December 1984) 195–204.

Nunamaker, J.F., Applegate, L.M., Konsynski, B.R., Facilitating Group Creativity: Experience with a Group Decision Support System, Journal of Management Information Systems, Spring 1987.

Nunamaker, J.F., Applegate, L.M., Konsynski, B.R., Computer-Aided Deliberation: Model Management and Group Decision Support, Journal of Operations Research, Nov.-Dec., 1988.

Shakun, Melvin F., Evolutionary System Design: Policy Making Under Complexity and Group Decision Support Systems, Oakland, CA, Holden-Day, Inc. (1988).

Slocum, J., A Survey of Machine Translation: Its History, Current Status, and Future, Computational Linguistics 11(1) (1985) 1–17.

Stefik, Mark, et al., Beyond the Chalkboard: Computer Support for Collaboration and Problem Solving in Meetings, Communications of the ACM 30 (Jan. 1987) 32–47.

Wagner, G.R., Decision Support systems: Computerized Mind Support for Executive Problems, Managerial Planning (Sept./Oct. 1981) 9–16.

## Exhibit 1: The Arizona Interface

The University of Arizona has two systems in operation. The smaller system (Nunamaker et al., 1987, 1988), shown in Figure E1-1, provides 16 personal computers whose screens are imbedded in a U-shaped table. A public screen can be used to show what is on the chauffeur's (facilitator's) screen. The system's program and data reside on a file server that is also used as the chauffeur's work station. The second, larger system provides 24 PS/2 Model 50 workstations and two six-foot projection screens arranged in amphitheatre style (Figure E1-2). This system, which became operational November 1987 uses the same software. Only the first system is discussed here.

The Arizona GDSS provides a large number of tools, including tools for brainstorming, issue analysis, voting, stakeholder identification, assumption surfacing, and recording what happened during a meeting. The chauffeur's station provides access to and control over the group support tools. The interfaces have been set up so the chauffeur and the user can understand the screens that appear even if they have not seen a particular screen previously. The system, written in Turbo Pascal, uses pop-up menus, cursor selection from menus, and keyboard instructions to communicate with the user. Figure E1-3 shows the first screen seen by the chauffeur. Not evident from this or subsequent figures is the use of color to help users separate input by others from information which they are creating.

In brainstorming, each participant is asked to generate an idea. The idea is then circulated at random to other participants who comment on it, using no more than 5 lines. The 5-line limit (based on experimentation with a variety of formats from a few lines to no maximum) is designed to keep the answers crisp and easy to understand. Figure E1-4 shows a brainstorming screen after a particular idea has been commented on by several people. The idea and previous comments are shown in the top window of the split screen and space is provided on the bottom for individual's comments. Once brainstorming ends, tools are provided that

![](/api/attachments/D9W2F6J3/fulltext/images/f14040c3f88e787dd6a5025747b0339b24c893110c398bdbc5e0d8b2e321baa9.jpg)  
Fig. E1-1. The University of Arizona Small GDSS Facility.

![](/api/attachments/D9W2F6J3/fulltext/images/643a25ebd80c2d25dedd69cdc60a50cde80fb81119f0199d7561323f5eb09319.jpg)  
Fig. E1-2. The University of Arizona Large GDSS Facility.

allow the group to review and edit the comments it created into a coherent whole. The process has been used many times and has proven to be quite efficient.

A particularly interesting screen, shown in Figure E1-5, is that used for sending questions to a panel or for commenting on an item in a list. The screen consists of windows which are identified by

![](/api/attachments/D9W2F6J3/fulltext/images/39d567eba15a8d921f2414b52da575ff3ee061c461997e429658835fdb16eecf.jpg)  
Fig. E1-3. First Screen Seen by Chauffeur; Arizona GDSS Interface.

![](/api/attachments/D9W2F6J3/fulltext/images/c4245429749555a553ad6bd3fd554edbb3b31c82c7254bfa6f8dcd0ae2a12f3e.jpg)  
PRESS F10 TO SUBMIT COMMENTS & CONTINUE  
Fig. E1-4. Electronic Brainstorming Screen as Seen by Participant after Several Rounds; Arizona GDSS Interface.

a short little (such as panelist name or issue number) on the top. In the panel application, one window is created for each panelist. While speakers talk, a member of the audience can send a question addressed to an individual panelist or to the panel as a whole. In an alternate application of this interface, in the larger of the two Arizona GDSS facilities, a series of proposed conclusions from a meeting were shown on the public screen. Each window corresponded to one conclusion. Participants could add comments, examples, and objections for whichever conclusions they chose. The result was that a group of about 30 people prepared a 30 page document in about 20 minutes that contained a large amount of information and which was ordered by topic. The output was reproduced and handed out to participants about 10 minutes after they finished.

## Exhibit 2: The Claremont Interface

This exhibit describes the interface built for one of three GDSS networks at Claremont Graduate School. This system obtained under a grant from Hewlett-Packard Corporation (HP) consists of nine fully configured HP-150 touchscreen microcomputers, each with two floppy disks drives, interconnected through an Ethernet. An HP-150 with a 20 Mb hard disk acts as the file server (Figure E2-1). This system was designed specifically to investigate the advantages and disadvantages of using the touchscreen as an interface. The design objective was to create as nearly typewriterless a system as possible for the meeting participants. The system uses a chauffeur who is able to type and is skilled in using both the software and the hardware.

![](/api/attachments/D9W2F6J3/fulltext/images/183f8ec7905dd62786d05bb0ea2f847078a0b93ac348ae32a88ace9fcfcddc16.jpg)  
Fig. E1-5. Participant's Screen for Sending Questions to a Panel.

![](/api/attachments/D9W2F6J3/fulltext/images/473e33ba2070c2dfedcc49daa0d8a9b23c36e0296d7c327a90e6f1aeeca89655.jpg)  
Fig. E2-1. The Claremont Graduate School GDSS Facility.

Claremont, like Arizona, provides capabilities for information sharing, creating ideas, and making choices. In what follows, we concentrate on the choice-making part of the software because it is a truly typewriterless system for the participants.

The voting software can be used to:

\- vote yes or no on an issue,

\- rank alternatives,

\- select $k$ preferred alternatives out of $n$ ,

\- rate alternatives,

\- perform preference voting.

Figure E2-2 shows the functional design of the voting system. It consists of a chauffeur's module and a participant's module. The chauffeur's module allows the chauffeur to:

\- generate the screens containing the alternatives to be voted on,

![](/api/attachments/D9W2F6J3/fulltext/images/1a437da40ebb62e03c97b3c3ba29cc773f6a0129377c4e53df98311f1faf74bb.jpg)  
Fig. E2-2. General Design of the Voting Subsystem Software.

\- create (or retrieve) the background reference information on each alternative,

\- manage and control the flow of voting by deciding when to start or complete voting and initiating the calculation and display of results,

\- participate as a voter.

The participant's module, provided at each station is more limited in scope. It allows the participant to (1) register to vote, (2) indicate readiness to vote after registering, and (3) cast ballots and transmit them for counting. The chauffeur's main screen is shown in figure E2-3. The top of the screen provides administrative, status, and time information. The rectangles in the middle of the screen are labeled touch areas. When the chauffeur touches one of these areas, a new screen comes up which allows him to perform the function indicated. Table E2-1 describes each of the functions briefly.

The voting screens seen by the participants are shown in Figure E2-4 and E2-5. In Figure E2-4a,

![](/api/attachments/D9W2F6J3/fulltext/images/de0229d426352c3b62fbaa654cc13bf86536c6ed2b560a0c217f7446c43e9ffc.jpg)  
Fig. E2-3. Chauffeur's Screen; Claremont Graduate School GDSS Voting.

![](/api/attachments/D9W2F6J3/fulltext/images/0133858111a6d70e099d29140a6edaa86c19ec82fb851c02392ca1c4175f6dd2.jpg)  
b. PARTICIPANT'S SCREEN--YES/NO VOTE  
Fig. E2-4. Participant's Initial Screens; Claremont Graduate School GDSS Voting Software.

the user typically touches the REGISTER FOR NEXT CASE line either at the number or on the text. The next screen (Figure E2-4b) then appears and he/she indicates whether they are ready to vote or not. If they are ready, they see the screen shown in Figure E2-5. Here the software automatically counts the number of alternatives and self configures the screen. That is, the user sees a screen that is aesthetic for that number of alternatives. Voters touch their preferred alternatives and, after they touch DONE, their vote is sent to the file server for processing. When the procedure is completed, the chauffeur selects GROUP RESULTS and a graphical output appears on the public screen.

![](/api/attachments/D9W2F6J3/fulltext/images/4d0cfd1ed40908a19a876413012022af30e0d69f021b292771363f343f30629b.jpg)  
Fig. E2-5. Participant's Screen for Voting; Claremont Graduate School GDSS Voting Software.

Table E2-1  
Functions Available on the Chauffeur's Screen.

<table><tr><td>Function</td><td>Description</td></tr><tr><td>Prepare Case</td><td>Used to lay out the screen. Chauffeur specifies the number of alternatives; the title of each alternative; and the rules of the vote. The system automatically generates the screen to be viewed by the participants.</td></tr><tr><td>Prepare Reference</td><td>Used to prepare reference material for each alternative to be considered. The reference material is, in effect, a help screen that allows participants to understand the alternative being voted on.</td></tr><tr><td>Begin Register</td><td>Starts case registration. The chauffeur is shown a list of existing cases and can select which one is to be voted on.</td></tr><tr><td>End Register</td><td>Terminates case registration</td></tr><tr><td>Begin Case</td><td>Allows Votes to be cast</td></tr><tr><td>End Case</td><td>Ends the voting and starts computation of results</td></tr><tr><td>Send Note</td><td>Allows the chauffeur to send a message to any or all participants</td></tr><tr><td>Participate</td><td>Allows the chauffeur to be one of the voters</td></tr><tr><td>Group Results</td><td>Displays the results of the vote</td></tr><tr><td>Group Status</td><td>Displays the voting status of the group. Shows who registered, who voted, who abstained, who asked for more time to make up their mind.</td></tr><tr><td>Cancel Case</td><td>Removes the case from the file.</td></tr><tr><td>Exit</td><td>Leave the voting system.</td></tr></table>

The main advantage of this system is its touchscreen interface. Experience with a number of groups and individuals who have been exposed to the voter end of this system shows that the touchscreen requires almost no learning time. Similarly, the chauffeur screen has proved to feel natural to people who are computer experienced.

## Exhibit 3: The Minnesota Interface

The first iteration of the University of Minnesota GDSS (DeSanctis and Gallupe, 1987) is shown in Figure E3-1. The private terminals indicated in the figure are simple terminals (not personal computers) running off an NCR Tower 32 supermicrocomputer used as a file server and computing engine. In its initial configuration, the system has 4 private terminals, although additional terminals can easily be added. The public screen is a 25-inch monitor that operates off the file server via a video out port.

![](/api/attachments/D9W2F6J3/fulltext/images/35b8216cf4d4e7698c8df4ab6fdbe4f7979ec839b29b301701fc2e99663c4bf4.jpg)  
Fig. E3-1. The University of Minnesota GDSS Facility.

As shown in Figure E3-2, the GDSS software consists of a public program to manage what appears on the individual screens and private programs for individual participants. The software is coded in C and runs under UNIX. The UNIX message exchange capabilities are used to support communications among the two programs. The public program receives all communications from the participants' private programs during the meeting and acts on them.

![](/api/attachments/D9W2F6J3/fulltext/images/298b8ced099bee5131de6f4cf78d7219a1d47f45168d9628d1cb18ef1ebf9216.jpg)  
One private program for each group member  
Fig. E3-3. Relation Between Public and Private Programs in the Minnesota GDSS Facility.

![](/api/attachments/D9W2F6J3/fulltext/images/d695a03ea4ffaa099ae3e2d690b5c5012254c0705b009f0da114d426ccb17ed1.jpg)  
Fig. E3-4. Main Menu for the Minnesota GDSS Interface.

The private program initially presents each participant with a general purpose agenda (Figure E3-3). The user selects an agenda item and receives a submenu which has the same look and feel as Figure E3-4.

![](/api/attachments/D9W2F6J3/fulltext/images/afbf9614954a7e416229469f458af43cba9245fc0a61cb59d278ea8b8b30227d.jpg)  
Fig. E3-2. Relation Between Public and Private Programs in the Minnesota GDSS Facility.

From the point of the user, the Minnesota GDSS offers a conventional, mainframe interface. All presentations are text lists. Users are assumed to be able to type their inputs, many of which are text intensive. In some situations, such as ranking or rating alternatives, the users are expected to follow relatively rigid prescriptions in entering information. Another feature of the Minnesota approach is that any participant can ask to view the current state of the decision on the public screen. That is, the system is democratic in who decides what is shown on the public screen rather than using a chauffeur to control the public screen.

The physical arrangement (see Figure E3-1) differs from that of other facilities in that the personal screens face toward the public screen rather than being built into the table so that they are in front of the user during discussions. Thus, a participant must turn sideways to view or use the terminal. In practice, this means that a participant has to separate him/herself from the meeting to use the terminal.

## Exhibit 4: The XEROX PARC Interface

Colab (Stefik, 87) is an experimental meeting room at the Xerox Palo Alto Research Center (XEROX PARC). The objective of the work in this laboratory is to explore how computers can support collaborative work in face-to-face meetings. Colab provides facilities for meetings of two to eight people who are engaged in design, rather than in decision making.

Colab consists of a relatively small room with

\- A large screen display (the electronic chalkboard or "Liveboard").

\- An automated podium (called ELECTERN).

\- Four workstations on a semicircle. These workstations have 19-inch displays and are driven by very powerful Interlisp-D machines. Workstation input is by mouse.

\- A local area network (specifically Ethernet) to connect the work stations and the Liveboard.

\- A conventional whiteboard.

The liveboard is a $4.5 \times 6$ foot glass plate with a GE projection video system behind it. The screen itself is touch sensitive. Mouse, keyboard, and touch input serve as “electronic chalk”. The Liveboard serves as the display for the Electern. The

Electern is, in effect, a high technology podium for presentations and a workstation that can be used by a group leader.

The basic philosophy of Colab is “What You See is What I See”, usually referred to as WYSIWIS. This is analogous to the word processing concept of WYSIWYG (what you see is what you get) and refers to the idea that images should be consistent among participants. Thus, it is possible to share information with all or selected participants and everyone can see the same thing. Furthermore, everyone can see where others are pointing. The basic metaphor is that of two people sitting over a sketch and discussing it.

The WYSIWIS approach does not result in the an image appearing in the same place on all displays. Colab provides private windows as well as public windows. It is the public windows which are WYSIWIS. However, public windows can appear at different locations on screens since users are able to arrange their screens to suit their own preferences. The different size and placement of windows on individual screens may make the image seem different even though the content is the same. Catering to the preferences of users makes WYSIWIS difficult to implement.

Two major software tools have been developed for the Colab environment:

COGNOTER (Cognition Noter; Knowing Together),

ARGNOTER (Argument Noter).

These tools support two phases of group meetings: idea generation and selection among alternatives. We describe COGNOTER briefly here. Both COGNOTER and ARNOTER are described in Stefik et al. (1987).

COGNOTER is a form of idea generating software. People start with a blank slate and use it for creating new concepts. COGNOTER goes through three phases: (1). Brainstorming, (2). Ordering, and (3). Evaluation. In the brainstorming phase (Figure E4-1), participants add ideas and supporting text on the screen. The ideas are put down in any order. Criticism of ideas is discouraged. In ordering (Figure E4-2), arrows are used to connect ideas in sequential order. Transitivity is maintained. If A comes before B and B before C, then A precedes C. Finally, groups of ideas are clustered and given a name. The group name (e.g., input devices) serves as a shorthand for the individual items (e.g., mouse, typewriter, touchscreen) in the cluster.

![](/api/attachments/D9W2F6J3/fulltext/images/1757e8fc31d104d449a901fad876a5e6d8db67a179e569b3bb20abd36c9006e2.jpg)  
Fig. E4-1. Brainstorming in COGNOTER.

![](/api/attachments/D9W2F6J3/fulltext/images/0538631aad766cc675e61df3bf5dafd6332dd4505453aa35f49c3d2669a5145c.jpg)  
Fig. E4-2. Assigning Relationships in COGNOTER.

COGNOTER differs from more conventional idea generating tools which use the linear thinking outlining format in that it separates the idea generation and ordering phase and in that it allows multiple linkages among concepts (a form of hypertext).

Although Colab is directed more at cooperative work than at group decision making, its basic configuration is similar to that of the other three GDSS's discussed in this paper. With its WYSISWIS approach, Colab may well be the forerunner of the next stage of interface technology in GDSS.

## Exhibit 5: Four Translation Scenarios

## 1. Electronic Brainstorming

In electronic brainstorming individuals generate ideas which they type into the computer. Ideas are then circulated randomly among individuals who add comments or new ideas. Thus, each idea creates a file to which individuals append new information. Typically, the system limits the comments to a few lines. The process is silent. All communication is through electronic text.

In international GDSS, each idea or comment on an idea would be generated in the native language of the participant. The idea is sent to the facilitator who types in the translation. Knowing the preferred language of the next individual who will see the idea and then comment on it, the computer sends the appropriate version of the file to the next participant's screen.

As simple automated translators become available, the facilitator would see the automated translation and edit it. For brainstorming, an automated translation system must be able to give the gist of what is being said but need not necessarily be 100% precise. The delays from human intervention in creating or checking the translation should be acceptable since only a few lines are being added at a time.

The facilitator would have to be discreet in maintaining anonymity during the process. Several facilitators may be required for large groups to keep pace with the rate of information generation.

## 2. Issue Analysis

Issue analysis is a follow up to electronic brainstorming in which a large set of ideas or alternatives has been created. The group then tries to aggregate those which are similar into a single statement. Typically, the current list is shown on both the public and the private screens. The process is both verbal and visual. People suggest new combinations verbally and the facilitator puts a combined statement up on the public screen. Once the aggregation is completed, the group ranks the statements in order of importance. In an international setting, the statements would be shown on the public screen in each language. To be successful, this process requires that all group members share an equivalent meaning for each item being discussed. Therefore, a highly accurate, idiomatic translation must be available. A bilingual facilitator (or facilitators) would need to review each item for “equivalent meaning.” It would be highly desirable to have simultaneous translation facilities available for the verbal part of the interaction. Issue analysis is an example of a highly interactive process among group members and represents one of the more difficult problems for international GDSS design.

## 3. Voting

Most GDSS provide voting systems that allow people to choose an alternative, select 'k' out of 'n' alternatives, rank alternatives, or rate alternatives on some scale. If voting is by secret ballot, then it involves electronic text only. Unlike brainstorming, where the translation can be fuzzy and still be used, voting requires precise translation of the alternatives to be considered. In the special case of voting on individuals by name, placement of names on the ballot can become an issue if alphabetic order varies from language to language. On the other hand, voting is often not as on-line and time sensitive a process as brainstorming. Hence, the translations needed can be prepared ahead of time, and checked out at leisure.

## 4. Negotiation

Negotiations involve two sides who are trying to find a mutually satisfactory solution to a specific

## U.S. Proposal

Last year (1986), Korea enjoyed a US\$7.3 billion trade surplus with the United States, due mainly to booming shipment of passenger cars and consumer electronic goods. U.S. government would take certain protectionist retaliation if Korea's market-opening efforts falter or fail. Therefore, U.S. requests Korea to make its domestic market more accessible to U.S. goods.

미국측 제안

1986년 한국은 미국에 대해 미화 73억 달라의 무역수지혹자들 기록하였다. 이것은 주로 승용차와 전자제품의 대폭적 수출증가에 기인한 것이다. 만약 한국정부가 한국시장개방노력을 개을리 한다면 미국정부는 보호무역주의자들이 주장하는 보복조치들을 채택할 가능성도 있다. 따라서 미국상품에 대한 대폭적인 수입개방조치를 취할 것을 한국측에 요청한다.

A:WUS2

Doc 2 Pg 1 Ln 1 Pos 10

Fig. E5-1. Example of Windowed Simultaneous Translation in a U.S.-Korea Negotiation.

problem. The problem itself may be complex. Consider, as a hypothetical example, the purchase of U.S. aircraft by, say, Korea in which some of the components and some of the assemblies are to be produced in Korea. The issues in the negotiation are which parts and assemblies are to be produced where, and the prices to be paid. The anticipated output of such a meeting is a detailed contract to be signed by both sides that spells out the agreed upon terms and conditions. Precision is particularly important. Here, sequential translation of the text stored in the computer would be acceptable. Assume that there is a facilitator who is responsible for verifying translations. If side 1 presents an offer to side 2, it could be sent to translation and then, after being verified by the facilitator, would be passed on to the group members of side 2.

Figure E5-1 shows a typical screen for a U.S.-Korean negotiation. This screen was produced by windowing two word processing files, one in each language.

As an intermediate step, prior to the development of high-speed, highly reliable computerized text translation systems, a text-to-voice-to-text translation system can be used to support negotiation. In such a system, the text is synthesized into speech for the facilitator, who would key in the translated text for the other side to see. As a variant, the speech is simultaneously voice translated as well (either by a talented facilitator or a professional simultaneous translator). The result is that side 2 first hears the proposal and then can see it on their screens.
