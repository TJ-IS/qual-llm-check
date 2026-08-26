---
otero_id: 26950
otero_key: "XBU9FWQC"
title: "Issues in the Design of Group Decision Support Sytems"
authors: "George P. Huber"
year: "1984"
journal: "MIS Quarterly"
doi: "10.2307/248666"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Issues in the Design of Group Decision Support Systems
Author(s): George P. Huber
Source: MIS Quarterly, Vol. 8, No. 3 (Sep., 1984), pp. 195-204
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/248666
Accessed: 18-01-2016 19:56 UTC

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Issues in the Design of Group Decision Support Sytems

By: George P. Huber
Department of Management
University of Texas at Austin
Graduate School of Business
Austin, Texas 78712

## Abstract

This paper deals with a number of issues pertinent to the design of group decision support systems. It notes that the need for such systems, whether designed by users or vendors, is a consequence of the clash of two important forces: (1) the environmentally-imposed demand for more information sharing in organizations, and (2) the resistance to allocating more managerial and professional time to attending meetings. The paper focuses on three major issues in the design of these systems: 1) system capabilities, 2) system delivery modes, and 3) system design strategies, and discusses the relationship of these issues to system use and survival. The relevance of numeric information, textual information, and relational information in a decision-group context are examined, and various system capabilities for displaying and using such information are noted.

Keywords: Decision support systems, meetings
ACM Categories: C.3, H.1.2, H.4.2, H.4.3

## Introduction

Managers, and other professionals, spend a good deal of their time in decision-related meetings; meetings where people possessing different facts, expertise, and points of view share and use information in order to select their individual or collective courses of action. It appears that the current and increasing complexity and turbulence of organizational environments can only heighten demands for such information exchange and use $[12, 16]$ . On the other hand, increases in the time spent in meetings require decreases in the time spent in other managerial or professional activities, and as a consequence will be resisted in many instances.

An outcome of this perceived imbalance in the distribution of time is the development and implementation of approaches for making meetings more effective and efficient. One such approach has been the use of structured group management techniques such as the Nominal Group Technique and the Delphi Technique $[2, 20]$ . Another has been the use of teleconferencing and video-conferencing $[14]$ . The most recent approach, and the one dealt with in this article, is the use of group decision support systems (GDSS). As will be seen, a GDSS consists of a set of software, hardware, and language components and procedures that support a group of people engaged in a decision-related meeting.

GDSS' are only infrequently encountered today, and published descriptions [5, 6, 15, 19] are scarce. A typical GDSS consists of a meeting room with a conference table. Each seating position has a small CRT terminal. Input at these terminals is by keyboard, touchscreen, mouse, or some combination of these devices. The meeting's participants are able to create displays on their CRT's (e.g., their subjective probability histograms for various levels of sales or their lists of suggestions for reducing costs), and to select any portion or all of their "personal" display for forwarding to a computer. The computer software is operated by a chauffeur who, at the group's direction, creates on a large public display screen the desired output, such as the group's average histogram or a cumulative list of all suggestions.

Observation of GDSS in action indicates that the extent of rich verbal interaction among meeting participants is not significantly different from that in meetings not supported with GDSS. The nature of the interaction changes, however, from communications concerning what members' views are (e.g., the shape of their subjective histograms of sales or their preference orderings of capital expenditures), as this information is already available on the public display screen, to communications concerning the information that different members possess and that causes them to hold the different views that they do. I note this type of information sharing not so much to argue that it results in better discussions (although some research suggests that it does [7]), but to distinguish it from computer-aided delphi meetings [9], where verbal interaction is typically minimal, and from teleconferencing [14], where real-time computer-aided aggregation and display of information is uncommon.

The idea of GDSS is not new. A number of academic research groups and private-sector corporations have worked on the development or implementation of GDSS. Among these are C.A.C.I. Inc., Cleveland State University, Decisions and Designs Inc., EXECUCOM Systems Corporation, Georgia Institute of Technology, K.R. Hammond Associates, Perceptive Decisions (Perceptronics), SUNY-Albany, Southern Methodist University, and Wilson Learning Corporation. A review of these systems shows that they vary considerably; there is strikingly little overlap in the group tasks that they support. It also shows that individual systems tend to support only a very small set of group tasks. For example, one system provides the capability for a group to construct and employ a decision tree, and that is about all it does. Another provides the capability for a group to identify and analyze the multi-attribute utility functions of its members. Yet another provides the capability for a group to obtain its members' strengths of feeling about the importance of different organizational goals and the performance of organizational units with regard to these goals and to use the resulting values in an organizational analysis algorithm.

Each of these systems seems useful for supporting a group in carrying out the particular task for which the GDSS was designed, and some of the systems support a marginally wider variety of tasks than do those mentioned above. Nevertheless, it appears that either the entrepreneur-uring organizations behind these systems have already segmented the GDSS market (I find this highly unlikely), or that individual GDSS designers approached their design task with a decision-aiding technique in mind that followed more from their disciplinary backgrounds than from a careful review of the tasks faced by decision groups. If the latter is the case, and the narrowness of focus of these systems suggests as much, it seems to fly in the face of the first principle of systems design; that designers should begin by examining user needs, and then determine the nature of the system best suited to fulfill those needs.

Just as the purpose of decision support systems is to increase the effectiveness of individual decision makers by facilitating the interactive exchange and use of information between the individual and the computer, the purpose of group decision support systems is to increase the effectiveness of decision groups by facilitating the interactive sharing and use of information among group members and also between the group and the computer. (By decision groups we mean groups engaged in decision-related tasks, e.g., creating a short list of alternatives for a decision maker. A decision group may or may not have the authority to make the final decision.) The useful domain and overall effectiveness of these systems are yet to be determined, but what evidence exists suggest that even today's GDSS' contribute to decision group effectiveness [6, 15, 19]. Further, it seems reasonable to believe that there would be an increase in effectiveness even if the systems were used in conjunction with proven group management techniques [11].

Finally, just as experience and development have led to increases in the effectiveness of DSS for individual use, we can expect that future GDSS will be markedly superior to today's relatively rudimentary forms.

Not surprisingly, and as will be seen, familiar concepts such as DSS generators and specific DSS [17] are just as integral to the design of GDSS as they are to the design of DSS. The additional requirement imposed on a GDSS, the requirement that it facilitate information sharing among group members, introduces the need for additional system capabilities, which in turn suggests that GDSS design strategies might include additional considerations or processes beyond those included in today's DSS design strategies. Further, the fact that GDSS' have, as their most conspicuous feature, the capability to support information sharing among group members, suggests that GDSS users and the organizational tasks for which GDSS' are used would be different from typical DSS user and tasks. This in turn suggests that GDSS system delivery modes (e.g., rent versus buy) might be different from DSS delivery modes, even in the same customer organization.

GDSS' are a relatively new technology. They serve in environments that seem relatively more complex that those of DSS, perhaps in terms of user tasks and certainly in terms of user (group) processes. As a consequence, approaches for addressing the issues of system capabilities, system delivery modes, and system design strategies are not well understood. The purpose of this article is to examine these issues in light of what experience we have and drawing upon knowledge from other fields, and in this way either advance the development of GDSS or prompt others to undertake and report superior examinations.

## System Capabilities and System Delivery Modes

Individual GDSS currently tend to support only a very small set of group tasks. This section examines some of the consequences of narrowly focused GDSS designs. It will be useful first, however, to define what is meant by a group decision support system.

Sprague's distinction between DSS generators and specific DSS is useful in this regard [17]. Sprague defines DSS generators as the tools (e.g., software, hardware, and languages) from which specific DSS are constructed, and defines specific DSS as the particular programs, commands, databases, and so forth that support a particular user in a particular task environment. Although generally discussed as a dichotomy, DSS generators and specific DSS are actually end-points on a continuum. For example, a given DSS vendor's product contains a particular subset of all DSS generators. Such a product is useful for constructing specific DSS that deal with a certain set of decision tasks, e.g., budget planning tasks or production scheduling tasks. At the DSS generator end of the continuum, these products look a bit like specific DSS'; they each support a type or subset of the potentially supportable decision tasks. At the specific DSS end of the continuum, many vendor products look like DSS generators; they look like tool kits that allow users to build specific DSS to match their particular decision situations. With these remarks in mind, we will consider a GDSS as a set of software components, hardware components, language components, and procedures that support a group of people engaged in a decision-related meeting. It may be more or less "specific," (i.e. it may be more or less specialized).

## Relationship between system capabilities and system use and survival

In any given organization, the frequency of a GDSS' use depends largely on how well its capabilities match the tasks encountered by the organization's decision groups. When evaluating proposed capabilities on this frequency-of-use criterion, two types of errors can occur. One is to provide capabilities whose use or availability is not cost-effective. The other is not to provide needed or desired capabilities. In addition to the obvious effects, errors of this latter type also have less obvious effects that deserve some elaboration.

Studies of organizational information systems have found that if a source or channel is used for one purpose it tends to become used for other purposes as well. The likelihood that a particular information source or channel will be used in a given instance is often more closely related to the frequency of its prior use than to its technical appropriateness [10]. These findings suggest that, all else equal, the greater the range of group tasks supported by the GDSS, the more frequently the GDSS will be used, and the more a GDSS is used in general, the more likely it will be used in any given instance. Of course, if the system's capabilities are well chosen, the range of tasks supported will increase with increases in the number of capabilities. Thus, there is an eventual synergistic effect on the frequency of GDSS use that follows from the inclusion of capabilities that widen the range of supported tasks. These arguments are summarized in Figure 1.

This matter of frequency of use is a more important consideration in GDSS than it is in DSS. Fre-

![](/api/attachments/XBU9FWQC/fulltext/images/a1e2901090b680b882d028cdf3b3e0bd9314ebad31d8613f96d160b256018cc5.jpg)

quency of use is an important determinant of user skill in either case; when users only infrequently employ either DSS or GDSS they become slower and more error-prone. The cost of user inefficiency is, however, much greater in the case of GDSS. If a DSS user “gets stuck,” he or she can take a few moments or an hour or so of his or her own time to refer to a manual, or to receive help from the vendor’s hotline service without any great cost to the organization. In contrast, if the group “facilitator” or the system “chauffeur” of a GDSS gets stuck, experience shows that the group participants quickly become disgruntled, critical of the system, and disinclined to use it in the future. $^{1}$ Worse still, of course, is the case where the facilitator or chauffeur gets so stuck that the meeting (whose agenda is sometimes quite dependent upon the GDSS) must be adjourned. Because such events are very public and costly in both an organizational sense and in an image sense, it is much easier for GDSS to fall into disrepute and disuse. It is for these reasons that the user's skill level, and hence the system's frequency of use, is more critical in the case of GDSS.

Three other effects of the range or number of system capabilities should also be highlighted. The first follows from the previous idea; because user skills (i.e., facilitator skills, chauffeur skills, and participant skills) decline if they are not utilized, there may be a critical frequency of GDSS use that must be attained in order for the system to survive in any given organizational environment. (It is worth noting that this critical number or set may be different from the number or set that is critical to the GDSS' marketability.) The second effect is that, since frequency of a GDSS' use is partly a function of the number of group tasks it supports, there may be a critical number or set of group tasks that the GDSS must support in order for it to survive in a particular organizational environment. Finally, since the number of group tasks that a GDSS supports is partly a function of the number and nature of the GDSS' capabilities, there may be a critical number or set of capabilities that the GDSS must possess in order for it to survive in a particular organizational environment.

In summary, the above reasoning suggests that one consequence of designing GDSS that support only a very small set of decision group tasks is that the resulting highly specialized GDSS will not survive. This, in turn, suggests that, although cost or technological considerations will undoubtedly preclude inclusion of certain features, GDSS designers should be cautious in making design decisions that narrow the range of group tasks that the GDSS supports. How can these thoughts be reconciled with the fact that a number of the narrowly-focused, specialized GDSS referred to earlier have existed for some time and seem to be used as frequently now as they ever were? The answer to this question introduces the subject of GDSS delivery modes and the relationships between delivery modes and the range of tasks that must be supported.

## Delivery modes and the range of tasks supported

There are at least three modes in which GDSS can be made available to users. Perhaps the most familiar of these is for the GDSS to be permanently installed at the user's or customer's site, as are most DSS. $^{2}$ From a GDSS vendor's point of view, a problem with this mode is that the system may not be used properly and therefore may fall into local disrepute and go unused. The problem of system misuse is much more critical with GDSS than with DSS since experience with GDSS makes clear that good group management skills are critical to the effective use of GDSS.

Another delivery mode is for the vendor to rent the system on an on-call basis (i.e., to have the system be as portable as the vendor's staff whose temporary services are included in the rental fee). This is the mode used by K.R. Hammond Associates and by Wilson Learning Corporation. Although system reliability can be adversely affected by the required portaging, recognizing this problem can lead to its near elimination. My observations of GDSS of this nature have convinced me that the group management skills and GDSS experience possessed by vendor staff are important resources and are critical components of these systems.

The third delivery mode is as a vendor-site installation where the software, hardware, support staff, and so forth are all provided for a fee, and to which the customer brings the decision group. This mode is used by Decisions and Designs, Incorporated and by SUNY-Albany. Unless the installation is heavily used, there is a high overhead cost incurred here but system reliability is high. Here again, observation of these systems in use shows that group management skills and experience with decision tasks, and with GDSS-supported decision making in particular, are important components of these systems.

What is the relationship between these three GDSS delivery modes and the variety of tasks that the GDSS must support? The reasoning presented earlier suggested that in any given user organization GDSS that support only a small set of decision-group tasks will not survive. However, if the GDSS took one of the latter two forms (i.e., if it were rented rather than purchased) the reasoning might not apply, since the rental cost might be low relative to the payoff from use and since the availability of vendor support staff reduces the likelihood of system malfunction or misuse. Thus we find that rentable, portable systems and “decision room” systems support only a small set of decision group tasks and yet survive in the market place.

Close scrutiny of the four systems just mentioned (and most of the other GDSS noted earlier) makes clear that they support only a small set of decision-group tasks and yet survive as rental systems. Could they survive as customer-site installations? The reasoning presented earlier and the observable lack of implementation as customer-site installations suggests that the answer is negative; that they are, in general, too specialized to generate the frequency of use required for survival. Although there may be organizations that will frequently use a highly specialized GDSS, these would seem to be uncommon. (This is in contrast to DSS where frequent use of specialized DSS, such as accounting or production scheduling packages, is not uncommon.)

To summarize, the discussion of this section suggested that specialized GDSS are far more likely to survive as either portable or vendor-site rental systems than as customer-site purchased systems. It also highlighted the fact that an important component of a GDSS, or at least a major factor in a GDSS' success, is the capability of the user group or vendor staff to manage the decision group and to draw appropriately upon the GDSS technology. These two “system capabilities” are more likely to be present in a rental system, as vendor staffs are more likely to possess the required skills and experience than are most user groups. Of course there are advantages to user-owned systems as well, but for the above-mentioned skills to be maintained in a user environment, the system would have to be used frequently. This thought brings us full circle to the matter of system design.

## Alternative GDSS Design Strategies

An obvious alternative to the technique-driven design strategy just discussed is to examine user tasks and then determine the nature of the system best suited to support these tasks. How do we implement this task-driven design strategy in the context of GDSS design? The logical first step is to examine the tasks of decision groups.

Decision groups can have a wide variety of tasks. On one dimension they may be involved in any step of the problem-solving process: problem sensing, problem exploration, problem definition, criterion and constraint identification, proposal generation, proposal evaluation, choice, implementation, and performance evaluation. On another dimension, decision groups may serve as “reactors” to descriptions of decisions tentatively made, as information generators, as recommendation generators, or as autonomous decision units.

When the numerous combinations from these two dimension (and possibly others) are overlaid on the variety of problem types and contexts faced by private and public sector organizations, it is clear that the possible decision-group tasks are beyond enumeration. This fact makes it difficult to employ a design strategy that derives the necessary system features from an examination of user tasks. There seem to be two approaches to retaining a focus on the user's tasks. One is to design a specialized GDSS, proclaim its market as being those groups with the type of task that this GDSS is designed for, and then rent the GDSS to customers in this market. Although such a GDSS is not likely to be used frequently by any one customer, it is likely to be used frequently enough by all customers together that it will survive as a rented product.

What if, rather than a specialized GDSS, a general GDSS is desired, (i.e. a GDSS with a large enough set of capabilities that it can support a wide range of decision-group tasks and therefore survive and prosper in a customer-site installation)? Given the innumerable decision-group tasks that an organization might generate, how can we use a design strategy that derives system capabilities from a knowledge of user tasks? There does not seem to be a good answer to this latter question.

Fortunately, an alternative approach exists. It is to focus on group activities rather than on group tasks, and to derive the necessary system capabilities from a review of these activities and a consideration of how computing and communications (C²) technology might be used to carry them out. In other words, it is to use an activity-driven design strategy.

A review of the literature on group decision making $[3, 4, 13]$ and on structured group management techniques $[2, 20]$ makes clear that whatever tasks a group may engage in, its members will be found to be carrying out one or more of the following activities: information retrieval (or generation), information sharing, or information use. This discussion will focus on information sharing and use.

## Information sharing and use

Information sharing is the most typical of the activities in which groups engage and it is one of the two activities most obviously supported by technology, the other being information use. Of course vendors and technologies, including traditional technologies such as slide projectors, are already serving the information sharing market very well. General GDSS, however, may possess several useful capabilities that are far beyond those provided by traditional information sharing technologies. For example, the group can decide during the meeting that it wants to see data contained in the organization's database and can, in real time, have it's chauffer retrieve and display the data on the public screen so that the facts can be collectively known. Personal entry terminals and appropriate software will enable the group, and each participant in the group, to create and modify the group's information displays. "What-if" and other analytic software will enable the group to use information, even ad hoc information entries brought forth during the meeting, as input to interrogations made and responded to in real time. In this way new information can be generated that may be critical to carrying out the immediate task.

Capabilities such as these are clearly beyond traditional information sharing technologies, and possession of them will give GDSS' a significant competitive advantage over traditional technologies. A second competitive advantage follows from the fact that these features are not limited to dealing with hard data. General GDSS can also enable groups to elicit, share, modify, and use professional judgements and opinions in at least as many ways as they do hard data. It appears that this capability can considerably enhance the contribution of decision groups to the organizational decision-making process.

## Numeric information

The sharing and use of numeric information is a common and important activity in the decision-group meetings of corporations and public agencies. This fact suggests that GDSS should provide a high level of support for numeric information sharing. This is already the case; today's specialized GDSS' enable chauffeurs and participants to enter, change, and publicly display numeric information from their personal terminals. Since quantification and sharing of judgements and opinions is generally thought to lead to higher quality decisions $[2, 11]$ , we can expect the necessary capabilities to appear in general GDSS'. In addition to facilitating information sharing, a GDSS can draw upon its computational capabilities to use numeric information to produce new information, as when it draws upon the participants' quantified, but subjective probability estimates to compute expected value or consensus forecasts.

The usefulness of this information-production capability is dramatically apparent in DSS, where real-time “what-if” and “goal-seeking” analyses generate information that leads users toward more informed choices. The what-if capability is especially helpful in the decision-group context as it reduces the frequency with which differences of opinion lead either to temporary adjournments or to unconvinced participants. For example, without GDSS support, a decision group in disagreement about the effects of different pricing strategies on cash flows would have to either adjourn so that alternative analyses could be prepared for a future meeting, or proceed to a decision with some members still believing that the decision was based on unsound reasoning. In contrast, with GDSS support that group could develop a cash flow model and run what-if analyses, just as with a DSS, and could then more likely proceed on a consensus basis.

Graphical portrayal of numeric information is at least as desirable in GDSS as in DSS, since group discussion of such displays lead to a wider understanding and to a higher level of satisfaction [15, 19].

## Textual information

Today's DSS are largely concerned with the retrieval and use of numeric information [1, 18]. In contrast, the environment of most meetings in corporations or public agencies is highly verbal. Thoughts are primarily shared and modified, not numbers. To the extent that the thoughts need to be recorded, they are put into text form. To the extent that the number of words verbally exchanged becomes an overload, the words are condensed and put into text form. To the extent that sentences and paragraphs dealing with complex matters are not totally clear, they are put into text form for closer scrutiny.

Meetings are extremely verbal environments, and the most important of the thoughts with which they deal are put into text form. A GDSS that does not reflect these facts will serve only a fraction of group tasks. For this reason it is important to consider how GDSS can support decision groups by aiding in the sharing of textual information.

Most meeting-related, text-conveyed information (e.g., meeting minutes, sub-committee reports) is distributed prior to the meeting. There are at least two situations, however, where the performance of groups can be improved with text-processing technology. One of these is the situation where real-time text editing is done by an interacting group. Examples include final contract editing and subcommittee report editing. Although such situations may not occur frequently, the availability of distributed forms of GDSS may cause distributed groups to engage in this activity much more frequently in the future. (At present distributed groups generally deal with such tasks by using low or intermediate level communication technologies, such as postal mail or teleconferencing, where each member tries to “keep up” by marking on a hard copy of the document.)

Much more important is the common situation where the decision group's participants are to share qualitative variables, such as problems, causes, or proposed solutions. This variable identification task occurs in many forms. In brainstorming the task is often to generate and share creative “solutions” to a problem. In problem analysis, one task is to identify and list possible causes of the problem. In planning, a common task is to identify and record activities that need to be carried out. Even if the lists of such variables are prepared in advance of the meeting, most groups will want to add or delete certain items. Clearly, sharing information about the existence of such qualitative variables is a common and important group task, and it seems to be one that can be usefully facilitated by appropriately designed GDSS.

A textual information-sharing GDSS should allow each participant to create variable lists or other texts at their personal input devices, and then to transfer these items to the public display screen. Such participant-controlled text-entering and transfer capability is highly desirable, as it maintains the feeling that participants control the GDSS, rather than vice versa. Further, each participant should be able to designate any portion of his or her text for public display, for instance his or her “best” ideas. Verbally directing a chauffeur to transfer items from a personal display to the public display screen is feasible, but is not as desirable as direct participant control because it reduces spontaneity. The key point here is that the GDSS should not interfere with the group’s communications.

To summarize these thoughts and capabilities, a general GDSS should have, as a component, a text writer whose work space contents can be displayed and can be created from multiple participant-controlled terminals. It would also be desirable to have a friendly and flexible text editing capability, in which case we would essentially be speaking of a multi-station word processor. A closely allied pair of features — the ability to display simultaneously both the text in memory and the text in the work space, and split-screen terminals with a double public screen — would enable the GDSS to support an even wider variety of group tasks. These capabilities would be especially attractive in a distributed environment.

## Relational information

Many meetings involve relational information. Often the information is portrayed in the form of a network or tree. One example is a PERT or CPM network for helping the group envision the activities and activity relationships inherent in enacting a plan. While a tentative version of a plan can sometimes be prepared ahead of time, experience shows that changes are often suggested and agreed upon during a meeting, and occasionally there is an unanticipated need to develop a network from scratch. Similarly, a decision tree, with its alternative action branches and its possible outcome branches, is a powerful tool for helping group members share their views about how a particular decision should be made.

The usefulness of sharing information with relational displays should not be underestimated. As suggested by the executive quoted in the Harvard Business Review, “We argued for 45 minutes about what we should do right now and what it would cost to postpone a decision, but it wasn’t until we put a decision tree on the board that people began to realize that we had all been talking about different problems!” [8].

Other relational displays frequently discussed in meetings are organization charts and distribution diagrams. Of course, such displays can be prepared ahead of time using traditional technologies if the task is simply one of presentation. But if the task is one where improvements are sought, as in a planning meeting, appropriately designed GDSS can be extremely useful. This is especially true if the relational displays are used as a basis for GDSS-supported what-if interrogations. Thus, the PERT network and computational algorithm could be used during the meeting to identify the new critical path, the time-to-project-completion, or the slack times as the planning group considers reallocation of resources in order to reduce key activity times. Such GDSS-derived values could be important inputs to the continuation of the meeting. Similarly, a decision tree could be used to identify the best of the immediately available alternatives and consequently allow the group to proceed to other agenda items. Finally, the GDSS should have printing capabilities in order to make hard copies of the agreed upon network or tree for the participants to take with them when they leave the meeting.

Whether the development and alteration of relational information should be facilitated with a freehand device such as magnetic stylus and tablet, or with a more structured display mechanism such as a set of menus, or with an in-between device like a mouse, would seem to be very context-dependent and is a subject for further research.

## Summary

This article has dealt with several issues in the design of group decision support systems (GDSS) It began by noting that the need for such systems, whether designed by the user or by a vendor, is a consequence of the clash of two important forces — the environmentally-imposed demand for more information sharing in organizations and the resistance to still more meetings.

A subsequent analysis of systems capabilities and delivery modes led to the conclusion that the low frequency of use associated with highly specialized GDSS' will cause them to have difficulty surviving as a customer-site installation. On the other hand, specialized GDSS' may be well received as either portable or vendor-site rental systems, or as components of a GDSS with a broader range of capabilities.

It was also noted that major factors in GDSS success are the capabilities of the users and their aides in managing a decision group and drawing appropriately on the GDSS technology. This fact supported the belief that vendor support may be critical to GDSS success in the great majority of applications.

A discussion of GDSS design strategies led to the conclusion that an activity-driven design strategy was superior to either a technique-driven or task-driven strategy. The subsequent analysis of group activities made clear that textual and relational information are relatively more important for GDSS than they are for DSS, most of which deal largely with numeric information.

As noted earlier, we can expect future GDSS to be markedly superior to today's relatively rudimentary forms. It will be interesting to observe the nature of the general GDSS' that eventually appear, and to see whether they emerge as "full-blown" systems or as expansions of specialized systems. The eventual state may be the same — general GDSS' that have a number of specialized GDSS' as optional modules, e.g. a PERT module or a financial planning module.

## References

[1] Bennett, J. (ed.), Building Decision Support Systems, Addison-Wesley, Reading, Massachusetts, 1983.

[2] Delbecq, A.L., Van de Ven, A.H., and Gustafson, D.H. Group Techniques for Program Planning: A Guide to Nominal Group and Delphi Processes, Scott-Foresman & Company, Glenview, Illinois, 1975.

[3] Fisher, B.A. Small Group Decision Making, McGraw-Hill, New York, New York, 1974.

[4] Gouran, D.S. Making Decisions in Groups, Scott, Foresman and Company, Glenview Illinois, 1982.

[5] Gray, P. "The SMU Decision Room Project," Transactions of the First International Conference on Decision Support Systems, Atlanta, Georgia, June 1981.

[6] Gray, P. "Initial Observations from the Decision Room Project," Transactions of the Third International Conference on Decision Support Systems, Boston, Massachusetts, June 1983.

[7] Hall, J., and Watson, W.H. "The Effects of a Normative Intervention on Group Decision-Making Performance," Human Relations, Volume 23, Number 4, August 1970, pp. 299-317.

[8] Hayes, R.H. “Qualitative Insights from Quantitative Methods,” Harvard Business Review, Volume 47, Number 4, July-August 1969, pp. 108-117.

[9] Hiltz, S. and Turoff, M. The Network Nation: Human Communication Via Computer, Addison-Wesley, Reading, Massachusetts, 1979.

[10] Huber, G.P. “Organizational Information Systems: Determinants of Their Performance and Behavior,” Management Science, Volume 28, Number 6, February 1982, pp. 138-155.

[11] Huber, G.P. “Group Decision Support Systems as Aids in the Use of Structured Group Management Techniques,” Transactions of the Second International Conference on Decision Support Systems, San Francisco, California, June 1982.

[12] Huber, G.P. “The Nature and Design of Post-Industrial Organizations,” Management Science, Volume 30, Number 8, August 1984.

[13] Kowitz, A.C., and Knutson, T.J. Decision

Making in Small Groups, Boston, Allyn, and Bacon, Boston, Massachusetts, 1980.

[14] Johansen, R., Vallee, J., and Spangler, K. Electronic Meetings, Addison-Wesley, Reading, Massachusetts, 1979.

[15] Kull, D.J. "Group Decisions: Can Computers Help?" Computer Decisions, Volume 14, Number 5, May 1982, pp. 70-82, 160.

[16] Simon, H.A. “Applying Information Technology to Organization Design,” Public Administration Review, “Volume 33, Number 3, May/June 1973, pp. 268-278.

[17] Sprague, R.H., Jr. "A Framework for Research on Decision Support Systems," MIS Quarterly, Volume 4, Number 4, December 1980, pp. 1-26.

[18] Sprague, R.H., Jr., and Carlson, E.D. Building Effective Decision Support Systems, Prentice-Hall, New York, New York, 1982.

[19] Steeb, R., and Johnston, S.C. “A Computer-Based Interactive System for Group Decision Making,” IEEE Transactions on Systems, Man, and Cybernetics, Volume SMC-11, Number 8, August 1981, pp. 544-552.

[20] Van Gundy, A.B. Techniques of Structured Problem Solving, Von Nostrand Reinhold Company, New York, New York, 1981.

## About the Author

Dr. George P. Huber is Eddy Clark Scurlock Professor of Management at the University of Texas at Austin. His research focuses on decision support systems, information systems, decision making, and organization design, and he has published two books and over fifty articles on these topics. He is currently vice chairman of the TIMS College on Information Systems, a member of the board of directors of the Institute for the Advancement of Decision Support Systems, and a member of the Council of the Institute of Management Sciences. Dr. Huber has held positions with three major corporations and the U.S. Department of Labor and consulted extensively for both private and public sector organizations.
