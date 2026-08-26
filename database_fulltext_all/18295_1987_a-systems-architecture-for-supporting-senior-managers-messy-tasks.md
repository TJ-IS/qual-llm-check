---
otero_id: 18295
otero_key: "PME4XAHD"
title: "A systems architecture for supporting senior managers' messy tasks"
authors: "Lawrence F. Young"
year: "1987"
journal: "Information & Management"
doi: "10.1016/0378-7206(87)90013-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Systems Architecture for Supporting Senior Managers' Messy Tasks

Lawrence F. Young

Quantitative Analysis/Information Systems Department, College of Business Administration, University of Cincinnati, Cincinnati, Ohio 45221, USA

Researchers have repeatedly observed that senior managers' work generally does not conform to formal problem-solving or decision-making models. Instead, SMS are primarily involved with intuitively directing a dynamically changing agenda or network of "concerns". This paper explores the potential for carrying the DSS approach into a new frontier of the SM's world. A general architecture for a Messy Management Support System (MMSS) is formulated, including previously defined creativity support (Idea Processing) systems. The MMSS would be linked to quantitative DSS, MIS reporting systems, telecommunications, and text processing systems. Currently feasible MMSS tasks are distinguished from those dependent on technological advances.

Keywords: Senior manager support, Executive support systems, Executive support systems architecture, Supporting executive thinking styles, Mess management support systems, Unstructured thinking support, Dynamic network support, Idea processing executive support, Creativity support for executives, Open database systems.

![](/api/attachments/PME4XAHD/fulltext/images/2b9b681933ac8265f707c359496d21fe6c6f60895a15b6b7b1692a7e9bb3bc37.jpg)

Dr. Young is Director of Information Systems Programs at the College of Business Administration, University of Cincinnati. He previously was Drexel University's MIS Coordinator, Senior Lecturer at the Technion-Israel Institute of Technology, and taught at Tel Aviv University, Baruch College-CUNY, University of Connecticut, Temple University, and as Visiting Scholar to China's Northeast University of Technology. He has consulted for corporations and government in the U.S., Israel, China, and Europe.

Dr. Young was editor, Journal of Information Systems Management, is Editorial Advisor for Information Strategy and Journal of Information Systems Management, and reviewer for the MIS Quarterly. He has authored several papers on DSS, MIS and MS/OR topics and a book entitled “Decision Support and Idea Processing Systems”, being published by Wm. C. Brown early in 1988.

1. The Issue: How Can Messy Senior Management Tasks Be Supported?

Senior managers (SMS) apparently work in a different way than assumed in the formal management science models of problem-solving or decision-making. It has been claimed $[7]$ that the very notion that top executives usually “solve problems” or “make decisions” in the formal sense is an inappropriate and misleading characterization. More appropriately, according to several observers $[1,8,10,11]$ , SMS can be said to be involved with defining and intuitively directing a dynamically changing agenda or network of “concerns”. Ackoff $[1]$ called this “managing a mess”. This sporadic “mess management” process typically uses very small amounts of hard information. It operates incrementally, forms tentative conclusions subject to rapid revision, and jumps opportunistically from item to item, cutting across several issues rather than completing discrete unitary decision problems one at a time.

In contrast to this general description of SM's tasks, decision analysis methods, computer-supported or not, are based on a unitary view of discrete decision problems. This view has itself changed as many management scientists gained wider experience in working with real managers. The Decision Support System (DSS) approach has developed in response to the recognition that one set of assumptions of decision theorists were mismatched with certain real processes. For some types of problems, described as “semi-structured”, DSS abandon the prior optimization-oriented dictum of Operations Research to attempt to:

1. render explicit an outcome objective, variables affecting the objective, and relationships among all problem elements, and

2. select or develop a standardized computational procedure to "find" the best values of the controllable (decision) variables.

Instead, DSS practitioners recognizing that many managerial problems do not lend themselves to this “structured” approach, attempt to provide an interactive user-controlled set of capabilities for exploring problems, learning about relationships and the effects of varying assumptions. Instead of seeking the one best model for a static situation, it tries to facilitate continual modification of a developing view of the problem.

In establishing this new approach, DSS has had to break through an attitudinal mind-set barrier in order to re-orient the major thrust of many management scientists. The view of such “converts” turned away from a theoretical normative picture of abstract problems in a bloodless, relatively orderly, and unreal world, and looked more directly at real people coping with messy problems. But this newer DSS view is still incomplete in that it continues to focus upon unitary decision problems as its central organizing principle. While such support systems have proven to be very useful in some situations, they have not directly addressed the non-unitary messier tasks. It is not clear whether it is feasible or desirable, given current technology, to develop computer-based management support for what William James referred to as “unstructured states of confusion” that characterize the real world. Isenberg [7] tentatively concluded that only a few limited forms of support currently appear to be feasible. Zmud [17] more extensively surveyed the literature and summarized some promising design and research directions for developing support systems for senior executives.

This paper attempts to build upon prior work in further exploring the potential for carrying DSS into the new frontier. First, a closer look at the problem of managing a dynamic network of concerns is taken in proposing a general architecture for a Messy Management Support System (MMSS). The proposed architecture groups and interrelates major new functions, including qualitative thinking support functions previously described as Idea Processing $[15,16]$ . It also provides for linkages to other systems components, such as DSS and MIS. The architecture is then examined to distinguish MMSS tasks that are currently feasible from those requiring advances in technology.

## 2. Characteristics of Mess Management Processing and Information

Webster's [12] dictionary defines a “concern” as a “matter for consideration”, or, alternatively as “an uneasy state of blended interest, uncertainty, and apprehension”. Much of managerial mess management seems to center around attempts to better understand and deal with continually changing perceived interconnections between a set of such concerns. Isenberg [7] postulates that such an inferred interconnected network of concerns and strategic agenda items in the mind of the senior manager could explain many of the observed characteristics of the SM’s apparently fractionated and ad hoc activities. In other words, while complex and dynamic, there is likely to be some sense and order in the apparent mess. A highly simplified illustration of changing connections between people, concerns, and strategic agenda items is shown in Fig. 1. The basic mess management activities and thinking processes SMS use in formulating, dealing with, and reformulating their network of concerns and strategic agendas can be characterized as:

## 1. Apparently fractionated and opportunistic but strategically linked.

More than one concern may be moved forward as a person is met, or during a phone call, or as any particular opportunity occurs. Apparently unrelated concerns (to a casual observer) are actually linked to a strategic mental agenda.

## 2. Highly inferential and intuitive.

Small amounts of hard data are taken a long way in inferring conclusions, along with the use of soft data, such as hearsay, gossip, personal opinions and interpretations of others, and the intuition borne of subconsciously perceiving patterns in a highly complex matrix of personal experiences. However, conclusions are often only tentative and subject to complete reversal given further information or experience.

## 3. Highly interpersonal.

Much thinking and thought-related action is carried out during and by means of meetings and conversations with other people.

## 4. Using action as experimental probes to aid understanding.

Directives to other people and creation of new organizational units and missions are often

## Dynamically Changing Relationships Between a Strategic Agenda, People, and Concerns :

A very partial picture.
Monday, 9 am  
![](/api/attachments/PME4XAHD/fulltext/images/057dd8b9678e571a92b54d4402b9074f0d104a940fa35b91031f8b5eece72034.jpg)

![](/api/attachments/PME4XAHD/fulltext/images/b979de159db451748380cae2aea9dd3c3c63424c098129d1fe10d145bd55da5a.jpg)

Fig. 1.

used as means of gathering more information or testing out tentative notions in the absence of more conclusive information.

Quoted from an advertisement [1986] appearing in the British publication THE ECONOMIST -

FOREIGN REPORT
a service of The Economist

Intelligence agencies, government ministers, and astute businessmen need to know about conditions that cause events before they happen.

This kind of information is of a more private and speculative nature than conventional news. It includes fact, speculation, even serious inside gossip, provides a vital background for political forecasting and business decision-making.

Fig. 2.

5. "Off-line" idea generation.

More reflective forms of thinking and idea generation commonly occur while carrying on unrelated leisure activities out of the fast cycle of direct interpersonal thinking-acting concern-juggling business activities.

In keeping with the above modes of thinking and acting, some special information characteristics are:

1. News-valued and highly temporal.

Much of the relevant information is temporal and quickly outdated. Its value depends largely on dimensions of newsworthiness, e.g. it reports a new and significant development in an item of concern.

2. Informed-speculation and interpretation.

The educated guesses and speculative thinking of “those in the know” are valued pieces of information that “explain” other “news” or help to interpret the meaning of some hard data items. (see Fig. 2).

## 3. Organized in smaller “chunks” than typical data files.

Although background text documents may be large, the document size of most complete verbal or written messages passed between concern-juggling managers (measured in words or characters or bytes) is typically much less than that of typical multi-record data processing files.

## 4. Source-dependent.

The impact or assessed value of mess-processing related information is often highly dependent on its source.

## 5. Partial and externally ambiguous.

Mess-processing related information is often unintelligible to an outsider, because it is partial and contains a form of keyword coding that only becomes meaningful when combined with other knowledge in the mind of the user. The complete message or meaning thus consists of both extra-somatically stored data (the written or spoken information) and somatically stored data (human memory and internal states of knowledge).

## 6. Natural language formatted.

Mess-processing related information is mainly text and thus is not field-formatted into fixed lengths or data-types. It may, at the most, conform to general rules of grammar.

The last three characteristics were identified by Brookes [2] as being typical of text data in general, in contrast to standard numerical or “factual” data processing files. In all of the above respects, the characteristics of information relevant for mess management processes can be seen to differ significantly from those of traditional MIS reporting systems.

## 3. Interface Characteristics and Functions of an MMSS

Given the above characteristics of mess management and the information associated with it, certain interface characteristics and operational functions suggest themselves. Isenberg [7] identified several general system characteristics he considered “musts’ and Zmud [17] repeated these, stating that they all concerned the need for a highly flexible system-user interface. Zmud also emphasized the importance of simplicity in exercising control over the selection and manipulation of system functions. Some of the previously noted interface-related characteristics include:

a. Portability, due to the executive style of peri-patetic interpersonal interaction.

b. Multi-media input provision, including voice recognition, notebook and scratchpad entries, due to the executive style of using verbal text messages as well as symbols, jotted “doodles”, and numeric data.

c. Natural language recognition, for the same reasons.

d. Ease of control and use, to avoid barriers to usage by busy executives who probably would not stop their normal activities (perhaps even momentarily) in order to figure out how to use the support system.

It has often been pointed out [9,16,17], that the features of the interface determine ease of use, and therefore the interface becomes a critical determinant of acceptance and use of a support system. But the interface is still only a means to an end. System functions (operations) need to be identified first in order to assess their utility and the value of expending development or user efforts to overcome any related interface barriers. In this regard, Zmud may have inadvertently mis-classified three of Isenberg's suggested characteristics that do not so much concern the interface as they do the nature of certain key system functions. We re-phrase these function-related characteristics as:

1. Distillation of information, the need to present only very boiled down, numerical representations drawn from larger arrays of data.

2. Facilitation of interconnectivity; due to the importance of the executive's dynamic mental network of issues, concerns, and people, the system must facilitate the creation and recall of these connections.

3. Provision for the integration of judgement and creative synthesis; that both avoids inhibiting the executive's intuition, judgement, and creativity, and actively provides support for these special capabilities.

With respect to the latter, Isenberg limited his concern to what might be considered a negative functional characteristic, that of preventing the system from substituting “the hard and trivial” and “driving out the soft and intuitive”. We have modified this point to include system functionality aimed at positively supporting “soft and intuitive” creative abilities.

Given the above reformulated and reclassified characteristics as a starting point, we can attempt to extend and collect functional features of an MMSS into the components of a general system architecture. After identifying functional components, interface characteristics can be reconsidered with the question: How critically are each of these needed for a particular system function? This should facilitate an assessment of whether interface features that may be economically or technically infeasible are really immediate “musts” for a prototype.

## 4. Functional Systems Components of an MMSS

Main functional components of an MMSS architecture are shown in Fig. 3 in the form of a systems hierarchy diagram. Linkages between components and other computer-based systems are shown in the Data Flow Diagram of Fig. 4. The major components would perform functions generally described as follows:

## 4.1 Concern Network Support (CNS)

This would enhance the user's ability to retain a complete, up to date, and consistent picture (both mentally and literally) of relevant networks of concerns, people, and strategic issues, similar to that illustrated in Fig. 1. These system functions would have to be highly dynamic and would prob-

![](/api/attachments/PME4XAHD/fulltext/images/9bb7fae30efb7ca42b95be37fc850405b57b958e76d01a277ef06434fde4dcf6.jpg)  
Fig. 3.

![](/api/attachments/PME4XAHD/fulltext/images/fadcef1927c44ce7880770796d24a311a4139c110cb55e396ccff61289dcd377.jpg)  
Fig. 4.

ably have to operate in real time (as events and interpersonal contacts occur) in order to guide the manager and to provide benefits over personal memory, etc.

The Concern Linkage Management component would be sufficiently powerful to record linkages provided by the user, and also derive and display second and higher order indirect linkages. Whenever new elements are added, deleted, or modified through use of the Concern Status

Management component, all effected network linkages would also need to be modified by the Concern Linkage Management component. Linkages would be displayed according to user-supplied criteria, upon request. But the system should also have sufficient built-in intelligence, through inference rules, to enable it to warn and prompt the user to consider important connections to pending concerns that the user might overlook in direct queries.

The Concern Status Management component would continually update concern networks by adding new elements (concerns, people, strategic agenda items), or deleting or changing existing elements. In addition, this component would perform the function of facilitating the transformation and migration of individual or groups of concerns into new concerns or into ideas or decision problems. Ideas, for our purposes, are defined as elemental and incomplete mental representations that may be potentially useful for attaining some end or interest (see Chapter 8 in Young [14]). They stand in contrast to concerns, because concerns are more concrete, being existing issues or action items already in the executive's normal processing stream of activities, whereas ideas are initially less defined or assessed or less clearly linked to an existing agenda. Thus, the generation of by-product ideas for subsequent off-line processing, while dealing with on-line concerns, can be characterized as moving into a less structured mode of thinking. This can, in turn, be supported by another subsystem of the MMSS, that of Idea Processing Support.

As noted above, the recognition of unitary decision-problems can also arise as a by-product of dealing with a network of concerns. The Concern Status Management component should therefore also facilitate the identification and transmission of newly recognized decision-problems to a more traditional analytical DSS for subsequent problem analysis.

The Concern Probe Tracking component would facilitate the executive's ability to follow the results or apparent results of recent past action-linked communications related to the same concerns. Similar to the need to use standard summary reports to aid in the control of regular on-going operational processes, this component provides control information on the more discrete executive probe actions, directives, action instigating messages, etc., used by executives in managing a network of concerns. It will be necessary to juxtapose and display past actions with the status of selected groups of concerns. In order to aid in assessing cause and effect, it will also have to associate, condense, and display related interpretative information derived from external systems such as the regular summary reporting components of the administrative MIS, text processing, and telecommunications network systems.

## 4.2 Open Information Support (OIS)

This subsystem would facilitate the user's ability to gather, filter, condense, retain, retrieve, assess, and associate “soft” commentary, news, interpretations, and informed opinions related to the active network of concerns.

The News / Soft Information Access component would be linked to the telecommunications (electronic mail) and word (text) processing systems. It would provide functions previously described by Brookes [2-4], including intelligence functions to sift, condense, or alert managers to recent soft information and news directly related to active concerns. In this, it is like an information retrieval system with “current awareness” capabilities. Their level of reliability and completeness may vary from relatively rudimentary forms of keyword pre-coding of electronic mail messages and stored text documents to sophisticated AI operations that would scan and analyze unformatted text and messages to discern topics relevant to active concerns.

In addition to providing access to soft information from internal organizational sources, this component would also provide access to external sources of news and soft information through an Open Information Database, which would filter and store items, abstracts, or reference to items obtained from external sources, such as consultants' reports, news wire services, etc. The contents of this Database would be relatively volatile, containing only those recent items deemed specially relevant to important active concerns. It would function more as an information buffer than as a historical repository.

The Source Evaluation Support component would maintain, access, and assess track records of sources of soft information. The Open Information Database would therefore also contain this source track record data categorically linked to currently active concerns, with assessments of source reliability for the relevant topic. These probably should include previously defined semantic designations or “fuzzy set” categories (e.g. “AA” or “highly reliable”, “A” or “reliable”. etc.) that could be updated.

The MIS Hard Information Association component would provide linkage and access to information produced and stored by the administrative MIS on ongoing business processes such as sales, production, and financial status reporting. In a manner similar to that of the News/Soft Information Access component, it would link information from the administrative MIS and associated corporate databases to active concerns. Hard information would be sifted, highly condensed, or merely have its existence noted in order to alert the user of its availability. This might be most easily accomplished by using an indexing and abstracting function.

## 4.3 Idea Processing Support (IPS)

This subsystem supports the idea generation and reflective, creative forms of executive activities, that are considered outside the daily process of managing concerns. Idea Processing can be described as the incubation and refinement of new ideas. These, in turn, may lead to new concerns or approaches to managing existing concerns. Thus, while temporally separate from concern management and employing very different functions, Idea Processing is linked to concern management and should be part of a comprehensive MMSS. Based on a review of non-computerized methods to enhance creativity, Young [13,15,16] identified particular functions that could be included to provide Idea Processing Support. These generally include the following main functional components:

\- Divergent Search seeks to aid in the generation of new alternatives. It centers on the classification of ideas and arranging and generating combinations of ideas.

\- Problem Redefinition focuses on conceptual boundary redefinition by classifying and arranging ideas into logical hierarchies.

\- Idea Manipulation facilitates a series of idea transformation operations (such as magnify, minify, reverse, etc.) that enable initial ideas to be converted into new ideas.

\- Metaphorical Association facilitates the user's ability to see familiar entities in new ways through metaphorical thinking. Unusual associations between entities are discovered and subsequently assessed for their utility.

\- Scenario Building / Analysis facilitates the building and assessment of scenarios, which can be considered to be qualitative models of key events or situational elements in a historical sequence. The building and subsequent assessing of alternative scenarios may aid in understanding to guiding subsequent action and policy formulation.

Idea Processing Support may be used in a stand-alone mode, or it may be linked with an analytical DSS so that as ideas may develop, attain greater definition, and become more quantifiable, they can be migrated into a different form of support. Idea processing can give rise to newly defined concerns, so that an IPS should be able to transform and transmit its selected outputs into inputs for the CNS subsystem.

## 5. Interface Dependencies of an MMSS

It will be seen that Concern Network Support places the greatest demands upon the user-system interface. It must operate in real time, while processing highly dynamic active concerns in a manner that is unobtrusive to the user's normal activities. This subsystem must obtain inputs from live communications and process them, being present as users go about their daily wanderings, fractionated conversations, lunch meetings, etc. For these reasons, this interface must be portable, include voice recognition, and be capable of natural language processing: the three interface characteristics that are most difficult to provide on a cost-effective basis. The interface might be simplified by providing a human aide (a system bearer-chauffeur) to follow the user around while carrying the system (microcomputer, stored programs and Concerns Database) and perhaps even silently entering short-hand style specially coded keyboard inputs. This, however, is a doubtful alternative on grounds of user acceptance, among other considerations.

In addition to the needs identified for the user–system interface, the Concern Network Support subsystem requires three additional interfaces of a different nature to function within a fully-integrated MMSS. One is needed with Open Information Support, one with Idea Processing Support, and at least one joint interface with the regular internal processing systems including MIS, electronic mail, and wordprocessing. These interfaces also require a portable component to maintain continuous on-line contact, and may require natural language processing for linkage with text and electronic mail messages, although this may also be eased through a keyword approach.

The Open Information Support subsystem presents a different picture with respect to the highly demanding interface features. If it is to operate in a completely integrated manner with Concern Network Support presenting soft information online to users, then it is dependent on the interface features of portability, voice recognition, etc. However, the benefits provided by the Open Information Support subsystem may be acceptably diminished if it is not fully integrated in real-time operation with Concern Network Support. The user could obtain off-line support from the soft information, news, assessments, and hard MIS associated information. An office terminal could be used on demand. It would remain for the user to remember, record, or otherwise retrieve this information when it is associated with other concerns. However, this is precisely what is done in practice today. The computer-based Open Information Support system would add sifting, associating, assessing, condensing, retrieving on demand, and displaying this valuable information.

The third subsystem, Idea Processing Support, does not require real-time linkage. Senior managers' natural model of engaging in reflective, creative generation and development of ideas is off-line. It can be provided as a completely independent stand-alone system without any computer links. Its main utility, is as a means of leveraging the user's own creativity. While linkage with other parts is not critical, it may be useful. For this reason, Idea Processing Support (IPS) is included here as a major subsystem.

If executives will only engage in this mode of thinking while simultaneously performing unrelated leisure activities, then such a support system not only must be portable, but it must provide novel new modes of input and output. However, though an idea may occur at any time, the utility of an IPS is based on its ability to support the development of the idea and the deliberate effort to generate new ideas.

## 6. Prospects for Realization of an MMSS

Given the above assessment of interface dependencies, it would appear that useful, although incomplete, MMSS functions can be developed in software currently, without awaiting further technical developments.

Limited capabilities dealing with soft information (some of the functions of an Open Information Support subsystem) have been implemented by Brookes [3]. Some Idea Processing functions have appeared in commercial microcomputer software packages, e.g. ThinkTank (Living Videotext, Inc., The Consultant, ODS, Inc.).

It would appear that both Open Information Support and Idea Processing Support functions will be further developed and evolve higher levels of integration with other information systems components.

Development of a Concern Network Support system, however, is likely to have to await the lowering of current interface barriers. On the other hand, experimental or limited versions of such a system could and should be developed in order to begin to assess their value.

Thus, we can conclude that from a technical point of view, some of the functions of an MMSS can be developed as stand-alone systems, while it is clear that a full-function integrated MMSS is currently infeasible. In contrast, previous examinations of the question of whether messy management styles could be computer supported take a more “all or nothing” viewpoint as well as a less comprehensive one.

The question of implementing an integrated MMSS would appear to depend on more than the previously identified technical issues. Completely integrating computer applications into total systems has never been accomplished even in traditional MIS. (Does anyone have a totally integrated corporate database?) While the trend in DSS software is toward more multi-function packages, even the newest packages represent less than fully integrated functionality. Part of this problem seems to be a matter of both the human resources available as well as the complexity of integrating such systems. It does not seem likely that an integrated MMSS will take managerial priority in assigning development resources, especially in the absence of demonstrated acceptance of the separate parts of such a system. Thus, incremental development of components along with slow partial integration is a more reasonable expectation.

While no one can predict how soon, if ever, an integrated MMSS may become an actuality, it is useful to develop and assess the concept. Stretching the frontier of computer support may require a top-down comprehensive vision as well as a bottom-up “one new application at a time” approach.

The limits of the DSS concept have not yet been determined, not only because of technical constraints, but mainly because of the need to understand the human processes employed by managers and to identify and assess potential modes of support for them.

## References

[1] Ackoff, R.L.: “The Systems Revolution”, Long Range Planning, Vol. 7, No. 6, pp 2–20, 1974.

[2] Brookes, C.H.P.: “Text Processing as a Tool for DSS Design”, in Processes and Tools for Decision Support, Sol, H.G. (editor), North-Holland Publishing Company, Amsterdam, New York, 1983, pp 131–138.

[3] Brookes, C.H.P.: “A Corporate Intelligence System for Soft Information Exchange”, Working Paper, University of New South Wales, Australia, 1984.

[4] Brookes, C.H.P.: “Requirements Elicitation for Knowledge-Based Decision Support Systems”, in Decision Support Systems: A Decade in Perspective, North-Holland Publishing Company, Amsterdam, New York, pp 129–144, 1986.

[5] Dreyfus, S.A.: “Formal Models vs. Human Situational Understanding; Inherent Limitations on the Modeling of Business Expertise”, ORC 81-3, University of California, Berkeley, February, 1981.

[6] The Economist: “Why Successful Businessmen Prefer Informed Speculation to Hard News Stories”, (advertisement for Foreign Report: A Private Intelligence Report on World Affairs), p. 73, 28 June-4 July, 1986.

[7] Isenberg, D.J.: “Research On How Senior Managers Think: Implications for Designing Executive Support Sys-

tems", DSS-85 Proceedings, San Francisco, CA, pp 64–66, April, 1985.

[8] Isenberg, D.J.: “Field Research on Managerial Thinking: Seven Findings, Seven Puzzles”, Working Paper 9-785-040, Division of Research, Harvard Business School, August 1984.

[9] Keene, P.G.W.: “Decision Support Systems and the Marginal Economics of Effort”, CISR Working Paper, Sloan School of Management, MIT, 1979.

[10] Kotter, J.P.: “What Effective General Managers Really Do”, Harvard Business Review, Vol. 60, No. 6, pp 156–167, 1982.

[11] Mintzberg, H.: “Planning On the Left Side and Managing On the Right”, Harvard Business Review, July–August 1976.

[12] Webster's New Collegiate Dictionary: G.&C. Merriam Company, Springfield, Mass., 1981.

[13] Young, L.F.: “Computer Support for Creative Decision-Making: Right-Brained DSS”, in Processes and Tools for Decision Support, Sol, H.G. (editor), North-Holland Publishing Company, Amsterdam, New York, 1983.

[14] Young, L.F.: “Information Representation and Assessment in Right-Brained (Qualitative) Decision Support Systems”, WPS 83-3, Working Paper Series, College of Business and Administration, Drexel University, Philadelphia, PA 19104, July 1983.

[15] Young, L.F.: “Idea Processing Systems: Definitions, Concepts, and Initial Applications”, DSS 85 Proceedings, San Francisco, pp 160–165, April 1985.

[16] Young, L.F.: “Decision Support and Idea Processing Systems”, Wm. C. Brown, Dubuque, Iowa, to be published.

[17] Zmud, R.W.: "Supporting Senior Executives Through Decision Support Technologies: A Review and Directions for Future Research", Decision Support Systems: A Decade in Perspective, (E.R. McLean, H.G. Sol editors), North-Holland, (IFIP WG8.3 Working Conference on DSS), June, 1986.
