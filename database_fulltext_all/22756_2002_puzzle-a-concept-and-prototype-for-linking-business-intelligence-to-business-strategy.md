---
otero_id: 22756
otero_key: "C5S66WSQ"
title: "PUZZLE: a concept and prototype for linking business intelligence to business strategy"
authors: "Kamel Rouibah; Samia Ould-ali"
year: "2002"
journal: "The Journal of Strategic Information Systems"
doi: "10.1016/s0963-8687(02)00005-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# PUZZLE: a concept and prototype for linking business intelligence to business strategy

Kamel Rouibah $^{*}$ , Samia Ould-ali

Department of Quantitative Methods and Information Systems, College of Business Administration, P.O. Box 5486 Safat 13055, Kuwait

Received 29 November 1999; revised paper accepted 18 March 2002

## Abstract

Business intelligence (BI) is a strategic approach for systematically targeting, tracking, communicating and transforming relevant weak signs $^{1}$ into actionable information on which strategic decision-making is based. Despite the increasing importance of BI, there is little underlying theoretical work, which directly can guide the interpretation of ambiguous weak signs. This paper gives an insight into the issue through a new strategic business intelligence system called PUZZLE. We describe this system and validate it by designing a prototype, test the system using in-depth interviews, and hold learning sessions in order to further knowledge about BI. The main results from tests show that: interpreting weak signs is potentially important for senior managers, consultants, and researchers; interpretation can be achieved gradually by bringing the weak signs together using a tracking form based upon the concept of actor/theme/weak signs/enrichment /links; interpreting weak signs is a complex process of establishing links between the weak signs. Final results show that the individual cognitive process appears heuristic when interpreting weak signs. Implications for strategic management practice and research are addressed. © 2002 Elsevier Science B.V. All rights reserved.

Keywords: Business intelligence; Weak signs; Interpreting weak signs; Fast response management; Strategic information system; Strategic business intelligence system; Creativity; Ill-structured problem; Research engineering; Exploratory research; Prototyping

## 1. From business intelligence to interpreting weak signs

Companies are evolving in turbulent and equivocal environments (Drucker, 1993; Kelly, 1998; Grove, 1999). This requires companies to be alert and watchful for the detection of weak signals (Ansoff, 1975) and discontinuities about emerging threats and opportunities and to initiate further probing based on such detection (Walls and Widmeyer, 1992. In such environments, business intelligence (BI) is surfacing to deal with the large volume of information available but which are often misleading, inaccurate and untimely (Martinsons, 1994; Futures Group, 1997; Attaway, 1998; Herring, 1998; Freeman, 1999; Groom and David, 2001). The main crucial question raised by companies in such environments is how to exploit these information elements to grasp opportunities, and avoid surprises when discontinuities occur (Grove, 1999; Moore and McKenna, 1999). This is the reason that companies need to have a well analysed, designed, and developed strategic business intelligence system (SBIS) (Martinsons, 1994). The emphasis here is on information systems that enhance strategic decision-making and that support the competitive strategy of an organisation (Wiseman, 1988). Much has been written on environmental scanning systems since Aguilar, Ansoff and Porter (e.g. Beal, 2000). However, it seems that the growing uncertainty of business environments still raises the need for an efficient SBIS to support scanning and interpreting information so that valuable intelligence may be delivered to senior managers. This paper develops a new SBIS and its implementation as a computer system. It is oriented to improve the BI and to ensure success of the business strategy. The meaning of BI emphasised in this paper, termed in French as veille stratégique, is considered as a systematic approach by which a company keeps itself vigilant and aware of developments and early warning signs in its external environment in order to anticipate business opportunities or threats. The external environment includes all factors and events outside the company that can affect its performance. Designing a successful SBIS requires an understanding of the relationship between the BI process and weak signs. There are several similar variants of BI processes (Martinsons, 1994; Attaway, 1998; Nolan, 1999). Our intent is not to describe in detail those approaches but only to show the link to weak signs. The description of these similar processes is beyond the scope of this paper. Among these, one is certified ISO 9001 and is mainly oriented toward weak signs management. This process is explained below.

## 1.1. Focus of this research

We consider the BI process as cyclical, involving five phases (Fig. 1, adapted from Lesca, 1994).

The first phase ‘targeting’ consists of bounding the surveillance of the company’s environment to set tracking priorities. The second phase consists of organising tracking and selecting the crucial weak signs. The third phase consists of routing the weak signs collected from outside to inside the organisation. The fourth phase ‘interpreting’ consists of transforming the collected information into actionable intelligence. If interpretation is significant, actions can be taken in phase 5. Otherwise, information search has to be refined in a more specific way (return to phase 2) if information is imprecise or; (2) the boundary (target) has to be redefined (return to phase 1) if it is too large. Of these five phases, the fourth—interpreting—is the most important and most difficult (Rouibah, 1998; Attaway, 1998; Subramanian and IsHak, 1998). Inadequate transformation leads to failures in using BI (Martinsons, 1994; Lesca and Caron, 1995).

![](/api/attachments/C5S66WSQ/fulltext/images/badc9d9d6e2ca96ceeee7d593adc88879ddacde4da21d2fbfd5ac673cef4fb23.jpg)  
Fig. 1. Phases of business intelligence.

Much has been written about the characteristics associated with events as threats or opportunities, their consequences and people's reactions (Thomas and McDaniel, 1990; Schneider and Meyer, 1991; Wagner and Gooding, 1997). However, researchers have not directly examined how people interpret weak signs in order to identify whether they turn into opportunities or threats even though interpreting weak signs is recognised as an important research topic for strategic decision-making (El Sawy and Pauchant, 1988; Thomas and McDaniel, 1990; Ansoff and McDonnell, 1990; Martinsons, 1994; Freeman, 1999). In addition, despite the need for strategic intelligence delivery being widely recognised (Attaway, 1998; Herring, 1998; Nolan, 1999; Freeman, 1999; Groom and David, 2001), the problem of interpreting weak signs has not received much attention in the academic world.

While providing insight into the problem was an operational objective of this study, there were also important theoretical and practical questions that had to be asked:

1. How to interpret weak signs in order to create meaningful maps of environmental changes useful to managers?

2. In what format should weak signs be presented?

3. How can such maps be created?

From a practical perspective, answers were sought to discover what difficulties and operational questions are associated with the interpretation of weak signs.

Hopefully, this paper provides some insight into those issues. The remaining segments of the paper are organised as follows. In the next segment difficulties of interpreting weak signs and research methodology are discussed. In the third segment, relevant and current literature on the subject of this paper is reviewed. In the fourth segment of the paper, a new prescriptive approach to deal with weak sign and the specification of the computer tool's functionality will be introduced. The fifth segment presents prototype capabilities and limitation. The sixth segment of the paper deals with lessons learned from validation of the approach. The concluding segment of the paper offers the implications of our findings for both academics and practitioners.

## 2. Work context and research methodology

Before describing the research methodology used, Sections 2.1–2.3 discuss the context of weak signs and the concept of strategic information systems (SIS).

Two reasons explain the difficulty in interpreting weak signs: the position of such information in strategic decision-making, and the nature of the information involved.

## 2.1. The position of weak signs in decision making

Two generic modes of scanning can be acknowledged: reactive and proactive. In the reactive mode of scanning (Cyert and March, 1963) search is stimulated by a problem and directed towards supporting strategic decisions. Its benefits are readily apparent to managers because the information collected could be directly integrated into strategic decision-making. However, the proactive mode of scanning or surveillance is exploratory and not directed to any predefined problem (Aguilar, 1967). In the latter case, the required information cannot be defined in advance. Its benefits are less easily measured. Therefore, monitoring activities are not fully integrated into the decision-making process (Lesca and Caron, 1995), senior managers continue to make poor decisions (Martinsons, 1994), and weak signs are ignored (Rouibah, 1998). Weak signs associated with the proactive mode may lead to a change in business strategy and therefore will require transformation into actionable intelligence before the information becomes usable. The proactive mode is the main concern of this paper.

## 2.2. The nature of information involved

The particular characteristics of weak signs make them very difficult to manage. According to El Sawy (1985) and Rouibah et al. (1997), a weak sign is:

\- anticipatory: it informs about changes when they begin to occur,

\- uncertain: it concerns events that have not yet been realised,

\- ambiguous: its content is usually uncertain or could be deliberately contaminated or distorted (for example by a competitor),

\- fragmentary: each information element taken alone is insignificant; however, significance increases gradually when combined with other weak signs,

• dynamic: it evolves over time,

\- cyclical: it has a complex life cycle from growing to declining that varies in its duration and significance (Ansoff, 1975; McCann and Gomez-Meija, 1992),

\- qualitative: in most cases, numbers are not involved and information may be available in other forms such as written, verbal, or visual images.

Weak signs are thus subject to perception and interpretation, and multiple meanings are possible. In order to avoid any confusion in the use of the word signal, we prefer to call such information a weak sign. Here, we define weak signs as uncertain and fragmented information about developments and trends. These have not been completely realised, or they have potential consequences, or are perceived to have a significant impact on organisational performance, either as threats or opportunities.

Taking into account the previous explanation, it is clear that quantitative and archival information available in on-line computerised databases (OCDBs) (McCann and Gomez-Meija, 1992) are out of the scope of this paper. They can help to track changes in world markets and to decrease the time needed to discover trends. OCDBs rely on information that can be codified and entered textually or numerically. They are used in combination with well-known scientometrics and bibliometric techniques (e.g. see Courtial, 1994). These are more concerned with how often archived information is consulted, and are very often used to perform trend analysis in research (e.g. assessment of laboratory results, comparison between laboratories). Nevertheless, these tools are inappropriate to assess unwritten information, which come from personal sources as some weak signs may.

Based on the previous difficulties, it can be assumed that a manager's attitude towards BI would be more effective if a SBIS were developed to assist with a better handling of weak signs. Section 2.3 explains what we mean by a SBIS.

## 2.3. Strategic information systems for business intelligence (SBIS)

Strategic information systems (SIS) are systems which contribute significantly to an organisation's performance and, consequently, to play a major role in its competitive strategy. A SIS is defined as a system having a profound effect on business success by influencing or shaping a company's strategy or by playing a direct role in the implementation of that strategy (Sabherwal and King, 1995; Galliers, 1991). An alternative interpretation of SIS suggests that it is not necessarily a particular information system, but rather a combination of those parts of an organisation's cluster of information systems, which feed its strategy planning processes (Clarke, 1994). Among factors that influence the SIS application, external factors (such as environmental competition, uncertainty and external needs) are driving forces for any SIS application (Choe et al., 1998). A SIS-oriented toward external changes helps an organisation to remain competitive and proactive.

As a result, all components of information systems, which support all or part of BI phases (Fig. 1) are considered to be SIS. If the above is agreed, then we consider a SBIS as SIS oriented to support company's BI activities.

## 2.4. Research methodology

Interpreting weak signs is a real problem encountered by many managers in different organisations that is closely related to the strategic decision-making process. This process is recognised as ill-structured and not adequately understood (Walls and Widmeyer, 1992; Schneider and Meyer, 1991; Channel et al., 1997). While the current situation is known (difficulty of the interpreting weak signs), the target or ideal situation that informs managers about potential threats or opportunities is unknown. Surveys (collecting large amounts of data followed by testing hypotheses) are not appropriate for helping managers in this situation. Therefore, the chosen methodology used to perform this research has been called ‘engineering research’ (Channel et al., 1997). It is an on-site methodology useful for expanding knowledge about complex and ill-structured processes, such as interpreting weak signs, and helping managers to progress.

Characteristics of this research methodology are as follows:

1. Engineering activities: the researcher is not an observer, but is a part of the problem solving process. He acts as an engineer who develops a conceptual model, builds a prototype, acts as a facilitator and evaluates his construction on site in the organisation.

2. Exploratory research: due to the lack of structure underlying the problem addressed, it can only be approached by exploratory research based on trial and error, in modelling, building, testing and evaluating.

3. Creation of procedural knowledge: it refers to the knowledge that helps to act and to reason (the knowledge of what to do next). This takes the form of a method, a guideline or a prototype.

The main results expected from this methodology fall into the following:

1. Ability to stimulate interest. Most senior managers or executives needing to be interviewed are not always able to express clearly either their difficulties or their requirements. Therefore, it is useful to support them with ‘something’ in the form of a prototype in order to attract them and motivate their meeting with researchers.

2. Prototype. This can be used as a support for training and learning of users who will learn faster by doing rather than by talking. We improve the prototype using users' suggestions.

3. Creation of new information. Testing the prototype enables the collection of users' reactions and relevant observations, which would be out of reach without the prototype or when traditional methods such as surveys are used.

4. Open new research directions. Negative users' reactions during tests become new research directions and new concepts to develop. The feedback (data collected during tests with the end users) can be re-used to improve the interpreting process in order to support managers' needs and contribute to more theoretical knowledge in the field of BI.

5. Refinement of concepts. Based upon users' reactions and suggestions, we go back to the concepts (artefact) we developed in order to further knowledge and propose enhancement and refinement.

Section 3 specifies the appropriate literature with regard to advantages and limitations to the model developed.

## 3. Literature review

Several researchers admit that the information collected must be transformed into actionable intelligence before it becomes usable (Martinsons, 1994; Lesca and Caron,

1995; Herring, 1998; Koneig, 1996; Attaway, 1998). Moreover, to achieve such an objective, authors propose to integrate unrelated pieces of information in order to create a holistic picture (Valette, 1993; Martinsons, 1994; Lesca and Caron, 1995; Koneig, 1996; Attaway, 1998; Subramanian and IsHak, 1998; Freeman, 1999).

However this transformation has received little attention. Only two methods 3T (El Sawy and Pauchant, 1988) and PUZZLE (Valette, 1993), to our knowledge, have addressed the problem. According to those authors, interpreting weak signs can be done based on a tracking form composed of ‘actor/theme $^{2}$ /information’. Pieces of information, related to a theme and a specific actor (e.g. a competitor), can be pieced together to get a mental map ‘puzzle’. The term ‘puzzle’ has been used by several researchers to create an analogy between interpreting weak signs and reconstruction of a puzzle (see Gilad and Gilad, 1986; Valette, 1993; Lesca and Caron, 1995; Attaway, 1998; Hall, 2001). Valette suggests using PUZZLE to detect significant environmental changes and to orient the scanning. El Sawy and Pauchant found collective interpretation produces more value than when individuals work alone. They also found that a shift in the interpretation is generated through the perception of new weak signs or the occurrence of new learning and ideas. Moreover, a change in a cognitive map takes place through cognitive functions, which are invariant (content independent), and thus, can be applied to a variety of tasks and situations. However, these cognitive functions have not been studied and implemented as a guideline. We propose to reuse the idea of integrating bits of information together in the form of puzzles and to build a new method—accompanied by a prototype—in line with the two previous ones, which we continue to refer to as PUZZLE. In order to complete the understanding of weak signs and the cognitive functions that occur during the interpretation we turn to creativity and learning.

According to several authors output and process are key concepts in creativity (e.g. Couger et al., 1993; MacCrimmon and Wagner, 1994; Bostrom and Nagasundaram, 1998). The output is built up gradually by successive alteration (Plsek, 1996). One process that is common to many theoretical contributions is making connections or associations (see Stenberg, 1988; Kanter, 1988; MacCrimmon and Wagner, 1994). This process is one of the main focus of this paper; it refers to the creation of new ideas through relationships between existing ideas. In our model, such connections can be triggered by linking pieces of information together in order to infer new information from adjacent ones; and to generate hypotheses that must be validated quickly. This idea is derived from the kaleidoscopic thinking of Kanter (1988). It allows the creation of arrangements by connecting fragmentary information elements until new patterns and actions can be generated. Such idea is also in line with Herring's view of intelligence as a process in which information is subject to systematic examination and determination of significant relationships (Herring, 1998). Weak signs are not all alike since they probably come from different sources. Thus, they can support or contradict each other, or one weak sign may be the cause, the consequence, or the result of another weak sign. The process of making connections was implemented by connecting weak signs through a typology of links: causality, confirmation, and contradiction.

The limited rationality theory (Simon, 1960) gives insight on the human interpretation of issues. According to this theory, the human brain has limited capacities for interpreting information and it is influenced by the nature of the information. Miller (1956) showed that the maximum number of chunks (weak signs in our model) that could be remembered and dealt with at one time in short-term memory, is $7 \pm 2$ . Based on Miller's findings, Simon proposed a reasoning mode that is heuristic. This requires a manager to build partial environmental maps. These help him to act even though they are incomplete. In addition, according to research in cognitive theory, individuals treat information better and faster when it is presented visually (Meyer, 1991). Therefore, we have chosen to represent the interpreted information as a graphical map, that we continue to refer to as puzzle. Puzzles are composed of weak signs and their links. During the creation of a cognitive puzzle, different modifications can reflect what has been learned. Piaget (1996) and Norman (1982) identified the following modes of learning: assimilation where new information is assimilated into an old cognitive map; accommodation where old cognitive maps are modified when new information does not fit the old cognitive map; and structuring when new cognitive maps are formed. Then, it can be inferred that elements of a puzzle will be subject to addition, deletion, and mergers.

Based on that previous observations it should now be clear that there is a very intimate and dynamic relationship between interpretation of weak signs and creativity.

The following method was developed from the previous observations.

## 4. Proposed method

We define the interpretation of weak signs as both a process and product:

\- a process by which an individual or group of individuals transform weak signs into meaningful maps, even partial, about how a company's present and future business environment may be impacted,

\- an end product, that is the output of that process.

Fig. 2 shows the conceptual model for the interpretation.

## 4.1. Phases of the method

We propose a method based upon a creative process of seven steps.

## 4.1.1. Step 1—input to the method

One way to establish boundaries of the environment is to limit the surveillance effort to (a) the specific targets (actors $^{3}$ /theme) and; (b) to key strategic information sources. Weak signs collected according to targets are input to the method. These information elements are in their early stage and have been collected according to surveillance mode. Interpreters are non-experts.

![](/api/attachments/C5S66WSQ/fulltext/images/1801f0a8920c2f4b2ab99205f73cead3cdeb9d772176a3d0e982d4de382363b3.jpg)  
Fig. 2. Framework of weak signs interpretation.

## 4.1.2. Step 2—enrichment of the weak signs

All employees of a company could be a potential source of valuable intelligence. A single information element may lead to significantly different interpretations based on its context. One might enrich an element in different ways: assess its content using certain criteria (surprise, validity, relevance, timeliness, completeness, accuracy), provide continuations or contradictions to the existing information, and to complete missing information. The value of a weak sign is enhanced when all the views are integrated.

## 4.1.3. Step 3—categorisation of weak signs

Once the content of a weak sign has been evaluated, it can be categorised and classified according to themes. These can be identified during a learning session and bounded by an initial definition. A theme is a subject of interest that informs about an external actor for example the R&D policy of a competitor.

## 4.1.4. Step 4—creation of puzzles

This step consists of selecting certain information elements from the themes in order to elaborate puzzles. The construction of a puzzle is a real act of creativity because it consists of linking weak signs together in such a manner that fragmentary elements become an intelligible map, even if incomplete. A puzzle is a visual map, focused on a specific actor, where its nodes are small sentences (phrases) corresponding to weak signs; and edges are reasoning links (confirmation, contradiction, causality) which connect different nodes. Puzzles are useful to perceive a change when they are compared at different times.

## 4.1.5. Step 5—perception of modification

Different transformations may occur when examining a initial puzzle called $G_{0}$ :

1. delete information in $G_{0}$ , if it is obsolete;

2. subdivide rich information of $G_{0}$ ;

3. merge two information elements of $\mathrm{G}_0$ into one element when they are identical or one of them is redundant;

4. add a link between two information elements of $G_{0}$ i.e. one has been identified as a new link such as a continuation;

5. delete a link between two information elements of $G_{0}$

## 4.1.6. Step 6—refinement of puzzles

Each puzzle must be flexible, and continually restructured as new weak signs are collected. Examination of a puzzle based upon new information could challenge the existing information in contradiction, confirmation, or continuation. Thus, other supplementary transformations can take place in the puzzle $G_{0}$ , other than the five above: modification of an information content; substitution of information (new information replaces existing).

## 4.1.7. Step 7—proposal of actions

Going from atomised pieces of information to a refined puzzle helps users to reason. Arguments and questions are required to conduct such reasoning process:

\- Infer new information from the related and adjacent elements that needs immediate validation.

\- Provide progressive verification of the coherence between information elements.

\- Orient the scanning and tracking of new and missing information.

## 4.2. Functions needed for implementation

According to our model, creation of puzzles requires an appropriate computer tool that is composed of a database and an ideas mapping tool to support cognitive mapping. While the database will store, and retrieve information, and capture users' knowledge during enrichment activities (pull for enrichment and push for discussion); the drawing graph will support the creation and analysis of puzzles. Co-ordination and communication are also necessary functions for collective interpretation.

A form will record the following for each information element:

\- a title, this is a short anticipatory information about actions of an actor,

\- a tracker that collects the information,

\- a theme, to which information elements are related,

\- an information source that generates information,

• each information element is enriched,

\- each information element is evaluated in terms of importance/reliability so that different representations can be generated according to their importance and reliability.

\- each information has an editing date, an expired date and a date for the expected event,

\- an end user in the organisation who needs the information.

To ensure the security and confidentiality of the system, each user should have identification and privileges in storage, enrichment, extraction of information, and access to a puzzle summary.

## 5. Prototype capabilities and limitations

The prototype developed, called PUZZLE, comprises Lotus Notes (LN) and Decision Explorer (DE) (from Banxia). DE was chosen because it can be easily customised to generate puzzle maps. On the other hand, LN was chosen for three main reasons.

\- LN, as a technology platform, is able to create many applications. It contains various sophisticated tools and an integrated macro language, which allows further development and customisation of the applications.

\- LN, as groupware, allows several users to work simultaneously on the same application. Through its shared databases and e-mail services, LN supports collaborative work, co-ordination of activities, and communication between different users, pursuing common goals.

\- LN, as an Intranet, is a central knowledge database with highly controlled security access. It guarantees the security and confidentiality of communication.

An application was developed within LN (for storage, enrichment and extraction) and customised DE (puzzle creation and refinement) in order to support the puzzle approach. The resulting prototype supports the method presented here and has the following capabilities.

1. PUZZLE allows a company to keep all employees informed of crucial events on a frequent basis. It provides rapid storage and easy access to timely information, thereby reducing the search time.

2. PUZZLE allows capture of users' knowledge from every branch of the organisation during supply, enrichment of weak signs, or creation of puzzles. Users can access all information and interpret it from different views. The prototype visualises information elements and their enrichment in order to keep track of all persons who have enriched weak signs. Therefore, it can be seen as a knowledge management system.

3. During the creation of puzzles, the prototype provides an environment to create multiple arrangement of puzzles. Information mobility, link affectation, colours to differentiate ideas, and a zoom function to focus on particular information elements are available.

4. During analysis of a puzzle, the prototype allows comments to be made and the author's name and puzzle creation date to be stored in order to be able to compare different puzzles created over a period of time.

5. Finally, PUZZLE can be used as a working agenda for discussions when interpreting weak signs. The output of such discussions is a puzzle map that is relevant, timely and contains actionable intelligence that the decision makers may create.

When a manager from enterprise X (us) raises a question about a specific actor Y (i.e. a competitor), information elements related to Y will be activated on the computer screen according to criteria used to store data (see Section 4.2). The manager connects the information elements by looking at their enrichment. In case some difficulties occur, accessing the help of the prototype provides definitions of links and examples. The manager then creates a first puzzle about Y. If it stimulates his reasoning, it can be printed and individually used. Otherwise, it can support collective discussions to derive other actions. Alternatively, the puzzle can be cancelled and a new puzzle generated using another idea. This procedure can be iterated as many times as necessary. Fig. 3 illustrates an example of a puzzle concentrated on Y and the theme the policy of Y toward R and D.

Link affectation is made by the authors using the prototype.

![](/api/attachments/C5S66WSQ/fulltext/images/c5492dbee049bbcc112b33bef09f373773eb9a8be97f93f8a49be5dc090414de.jpg)  
Fig. 3. Example of a Puzzle.

This puzzle could have been created by company X who puts Y under surveillance. The elements of such a puzzle are connected by different links based on reasoning and assessment of X. With the same information elements, it is possible to create several puzzles until the most meaningful one is produced, or it suggests more interrogations and hypotheses. This puzzle is dynamic since it can be modified according to addition of new weak signs. The analysis of that puzzle can lead to the following:

The expected event to be realised is Y may become a threat for X. Therefore, based upon the sixth and seventh elements, the following hypothesis can be inferred: Y is becoming a competitor of enterprise X. Taking this hypothesis into consideration, the following actions should be undertaken by X:

\- keep Y under surveillance and track it in order to discover why it is becoming a competitor. What are its future strategies?

\- define the information sources for collecting more information about Y's actions and assign persons to track the information,

\- check the accuracy of: X is looking for an alliance with competitor Z, and evaluate the impact of such an alliance on X,

\- cross check the first and second elements because they are in opposition.

In addition to its capabilities, the prototype suffers from some limitations. Its composition of two systems can be constraint. Weak signs are stored and enriched in LN before they are exported to DE where puzzles are created and analysed. In addition, the prototype does not automatically perform all these previous tasks. Information push for enrichment and discussion, and puzzle creation through link affectation, are manual tasks. For instance after a user accesses information, he can enrich it before sending it to other users. Once, a user has completed the enrichment, the prototype integrates the views of all others users which become visible to all. Actually PUZZLE allows collective enrichment, but it does not support collective creation of puzzles. Finally, the prototype requires the assistance of a facilitator.

## 6. Testing and results

This prototype is already operational and has been validated using several tests. Three difficulties have been highlighted (McCusker, 1992): disagreement over what to measure, benefit not easy to perceive, and benefit not easy to quantify. Because of these issues, the validation was based on two criteria:

1. usefulness of PUZZLE; this criteria refers to how PUZZLE (as a method and prototype) enhances and supports the process of BI and the interpretation of weak signs.

2. ease of use of the prototype; this criteria refers to how practical and easy to comprehend the concepts in PUZZLE are.

## 6.1. Subject and testing procedures

These tests were performed between 1997 and 2000 in France and the Netherlands, using four methods.

First, in-depth interviews were held during several demonstrations of the prototype (in France and the Netherlands). This validation has involved many participants from companies who had been introduced to PUZZLE through the use of examples during a three day exhibition. Interviews lasted between a half and one hour.

Second, the prototype was demonstrated during several initiation days, to eight professors (three in the Netherlands and five in France) with two consultants in France and with six senior managers from French companies (four from an electronics company and two from an insurance company). After being introduced to BI and PUZZLE, a demonstration and interviews lasted 1/2 day.

Third, learning sessions were held with four senior managers from a Small and Medium Sized Enterprise that develops electrical components. PUZZLE had been in use for two months. With this third method, data collection followed a collective learning process of four stages (Davis and Olson, 1985): basic understanding, individual learning, recommendations, and tests.

Fourth, several tests were carried out with twenty MBA students from two Dutch universities who were given a half a day introduction to PUZZLE. The tests were not part of any course curriculum, nor did students receive academic credits for their participation and no students had studied BI. After being introduced to PUZZLE, each student was asked to create a puzzle (30 min) assisted by comments and advice from a facilitator. Then, they were asked to create a puzzle collectively (30 min).

## 6.2. Data collection

To decrease researcher generated bias during the tests, two researchers were present, one to operate PUZZLE and the other to collect data from direct observations. These included the appropriateness of concepts (e.g. weak signs and links), assessment of PUZZLE (identification of strengths and weaknesses, adequacy of the conceptual model compared with the empirical situation, perceived activity of puzzle creation). In addition, participants who tested the prototype were surveyed in order to determine their reactions.

The four tests demonstrated advantages and disadvantages of PUZZLE and opened new perspectives.

## 6.3. Do users perceive PUZZLE as useful?

Among favourable reactions recorded were the following:

First, PUZZLE is seen as a structuring method that formalises heuristic reasoning, clarifies BI and helps to perform it. All participants agreed that “it is important for managers to understand how to perform BI based upon weak signs which is completely different from illegal, unethical economic espionage”. Also, all agreed that interpreting weak signs in order to transform them into intelligence is both important and necessary before becoming actionable information.

Second, PUZZLE allows better understanding of the concept ‘weak signs’ and orients the environmental scanning. It shows where BI bottlenecks are in order to propose improvements “currently, a number of departments across the company collect competitive information on an ad-hoc basis, and very little of it is ever turned into useful intelligence. Rather than anticipating what our competitors are going to do, we found ourselves reading photocopied snippets of what they have already done", commented another participant.

Third, PUZZLE is an organisational tool to support the co-ordination of scanning, helps selecting weak signs and interpreting activities. As a consequence, the informal activities of scanning currently operating within companies could be reduced. “PUZZLE avoids overloading managers and executives by selecting only crucial pieces of information”, commented one participant.

Fourth, the cognitive process of individuals is heuristic. Throughout the observations, it seems that test participants of PUZZLE follow heuristic reasoning and not algorithmic: an idea emerges, that launches others, then other information elements are searched, and the process is iterated during creation of puzzles, hypotheses and commentaries. As individuals scan the external environment, the new information and interpretation they acquire influence their perception of environmental changes, which in turn affects what they will perceive in their environment and how they will scan it. That finding suggests that BI is a feedback process and that interpretation activities are close to that of the targeting and selecting of weak signs.

Fifth, Puzzle stimulates interest and helps the interpretation of weak signs based solely upon cognition “You give experts a tool to go further in reaction and in reflection. With PUZZLE we are concentrated more on the cognition of experts. This is a very original work which is different from most published work or existing tools like Datamining, for example” commented a participant. This suggests that interpreting weak signs is much concerned with human activity and as with technology.

Based on the positive reactions, we can assume that test participants perceive PUZZLE as being useful for interpreting weak signs and for improving BI.

## 6.4. Do users perceive puzzle as easy to use?

In addition to the previous favourable reactions, participants also perceive PUZZLE as a helpful tool that encourages communication and discussion. They also agreed that learning BI skills could contribute to enhancing and improving career opportunities, students' creativity, and could help students to learn real-world skills.

Despite the positive above reaction, PUZZLE shows some weaknesses. Even though participants recognised the value of connecting weak signs to generate working hypotheses, they perceived this activity to be difficult. They especially perceived this activity more difficult when puzzles are created individually than collectively. According to other test participants, puzzles are not suitable when many different information elements have to be interpreted.

In addition, it was suggested that improving the collective method could give richer weak signs, define a typology of weak signs to facilitate the puzzles creation, and develop a library of puzzles in order to facilitate their management. Finally, other test participants thought that PUZZLE requires creative persons for interpreting weak signs.

Based upon the above reactions, we can infer that PUZZLE is an easy to use educational tool and the proposed concepts seemed to be understandable. However the proposed concepts need further improvement and refinements (Table 1).

Table 1
Summary of findings

<table><tr><td>Criteria</td><td>Expected contribution</td><td>Findings</td></tr><tr><td rowspan="2">Perceived value of PUZZLE to BI and interpreting weak signs</td><td>BI process</td><td>- PUZZLE clarifies the content of BI- PUZZLE fully supports the BI process (targeting, tracking, and interpretation of weak signs)- BI is a feedback process- Puzzle is method to initiate performing BI activities- PUZZLE helps selecting of weak signs</td></tr><tr><td>Interpreting weak signs</td><td>- PUZZLE is seen as a structuring method that formalises heuristic reasoning- Transforming weak signs into intelligence is important and necessary before becoming actionable information- PUZZLE allows better understanding the concept of ‘weak signs’ and orients environmental scanning- The cognitive process of individuals during weak sign interpretation appears heuristic- PUZZLE stimulates interest and helps the interpretation of weak signs based solely upon cognition- Interpretation activities are close to that of targeting and selecting of weak signs- PUZZLE is an organisational tool to support the co-ordination of scanning and interpreting activities</td></tr><tr><td rowspan="2">Ease of use of PUZZLE</td><td>Puzzle in operation</td><td>- PUZZLE is a helpful tool for training and for quick learning of BI and the interpretation of weak signs- PUZZLE contributes to improving users’ and students’ BI skills, their creativity, and their career opportunities- PUZZLE helps students to learn real-world skills- PUZZLE facilitates communication and discussion</td></tr><tr><td>Weakness of PUZZLE</td><td>- Connecting weak signs is a difficult individual task but less so when collectively undertaken- Puzzles are not suitable when many information elements have to be interpreted.- PUZZLE requires creative persons for interpreting weak signs</td></tr></table>

## 7. Discussion and conclusions

This paper has presented a SBIS, based on exploratory research, to support managers in practice to better handling weak signs and to ensure success of the business strategy. This is an elusive issue related to knowledge management that has received little academic attention.

This paper brings three main contributions: conceptual contribution in the form of a creative method to support interpreting weak signs, design contribution in the form of computer tool to support this method, and empirical contribution for understanding the process of interpreting weak signs.

These findings have implications for both research and practice. From a practical perspective, our findings encourage the use of PUZZLE by managers to perform the process of BI. The use of a tracking form, based on ‘actor/theme/weak sign/personnel enrichment/link, transformations’, continuous discussion and creation of puzzles, are all suitable for company’s use. That form constitutes a shared language for understanding BI and that will facilitate its use in companies. PUZZLE can also be a viable training method for managers who want to learn BI process quickly and effectively.

From a research perspective this paper supports previous researches and adds new findings. This paper suggests interpreting weak signs as both a process and a product. The process requires the transformation of seemingly unrelated information elements into useful puzzles (product) using links in order to produce hypotheses about potential opportunities and threats. We found that collective interpretation produces more value than when individuals work alone. Convergence of individual interpretations following discussions seems to be fast and easy. These findings support the previous results of El Sawy and Pauchant (1988). Moreover, this study suggests interpreting weak signs and BI as complex processes in which individuals follow a heuristic cognitive process. The discovery of managers' difficulties in connecting weak signs was totally unexpected because it had never been highlighted before and brings new findings to strategic management literature. This finding also contradicts most statements of previous researches (Daft and Weick, 1984; Martinsons, 1994; Attaway, 1998; Subramanian and IsHak, 1998; Freeman, 1999).

In addition, this research encourages the use of the engineering research methodology proposed by Channel et al. (1997). This could be very helpful for researchers who want to understand the application of SIS in an area where little underlying theory exists, or for ill-structured problems. This methodology is very useful because of its ability to stimulate interest, create new information, open new research directions, and to propose refinement of concepts.

Results of this study should be examined in light of its limitations. First, we do not claim that this research is other than exploratory since the sample size was small, which limits the ability to generalise the result beyond this sample. Second, we obtained data from a single informant and that may introduce respondent bias and limit the generalisibility of the results. However, as companies compete in a turbulent environment, the results and their implications are not industry-specific. Third, limits of this research should also be examined with the reliability of its results. This is concerned with the extent to which our results are reproducible and consistent with those produced by other approaches. This is a difficult question to answer in any research study, particularly one as exploratory as ours. Our intent was to explore whether the PUZZLE approach could provide insights into the important research question posed above, and not to engage in a rigorous comparison of alternative BI processes and software.

Future research can take several directions. First this research suggests to continue testing PUZZLE, through replication under different conditions and in other organisations, in order to learn more about weak signs interpretation including: what are the frequency of using and updating puzzles? For which enterprises the PUZZLE approach is more suitable? What are the characteristics of those enterprises (size, activities, etc.)? Does the use of the prototype result in more creative ideas and better interpretation of weak signs? Also there is a need to apply PUZZLE to a specific case study such as an emerging technology, like the web telephone.

Second, findings about the difficulty to connect weak signs to each other suggests new research directions toward understanding the adequacy of organisational memory models with PUZZLE. One model that is well-known and respected in this field is that of Horst Rittel's Issue Based Information Systems (IBIS) (Rittel and Kunz, 1970). The IBIS model focuses on the articulation of key issues in the design problem. Each issue can have many positions. A position is a statement or assertion that resolves the issue. Each of an issue's positions, in turn, may involve one or more arguments that either support that position or object to it. Thus each separate issue is the root of a (possibly empty) tree, with the children of the issues being positions, and the children of the positions being arguments. In addition, new issues raised during discussion may be posted at any time and linked into the most appropriate nodes. Those postings serve as an organisational memory that not only captures the final decisions when trees are ‘closed,’ but also shows the history of the alternatives explored (Conklin and Begeman, 1988). This paper encourages future research to apply this model with puzzle by creating a graphical web based IBIS that allows all members of a company to read and post an issue (weak sign), positions (enrichments and questions), and arguments (links) at any time using their web connections. Those suggestions will help to build a complete and coherent theory around PUZZLE for BI.

## Acknowledgements

Without the support of the Centre des Etudes et de Recherches Appliquées à la Gestion, Ecole Supérieure des Affaires, Université Pierre Mendès (France) and the Information and Technology department at the Eindhoven Faculteit Technology Management (The Netherlands), this study would not have been possible. The authors gratefully acknowledge the contributions made by these organizations, professors Omar El Sawy and Humbert Lesca, the Editor-in-chief and anonymous reviewers.

## References

Aguilar, F., 1967. Scanning the business environment. Macmillan, New York.

Ansoff, I., McDonnell, E., 1990. Implanting strategic management. 2nd ed. Prentice-Hall, Englewood Cliffs, NI.

Ansoff, H.I., 1975. Managing strategic surprise by response to weak signals. California Management Review. XXVIII (2), 21–33.

Attaway, M.C., 1998. A Review of issues related to gathering and assessing competitive intelligence. American Business Review 16 (1), 125–135.

Beal, R.M., 2000. Competing effectively: Environmental scanning, competitive strategy, and organisational performance in small manufacturing firms. Journal of Small Business Management 38, 27–47.

Bostrom, R.P., Nagasundaram, M., 1998. Research in Creativity and GSS. Proceedings of the Thirty-First Hawaii International Conference on System Sciences, January 6–9. vol. 6. IEEE Computer Society, Piscataway, NJ ISBN 0-(8186)-8248-5, Best paper in minitrack, pp. 391–505

Channel, V., Lesca, H., Martinet, A.C., 1997. Vers une ingénierie de la recherche en science de gestion. Revue Française de gestion, november–december, 41–51.

Choe, J-M., Lee, Y-H., Park, K.-C., 1998. The relationship model between the influence factors and the strategic applications of information systems. European Journal of Information Systems 7, 137–149.

Clarke, R., 1994. The path of development of Strategic Information Systems Theory. Available from http://www.anu.edu.au/people/Roger.Clarke/SOS/StratISTh.html.

Conklin, J., Begeman, M., 1988. gIBIS: A Hypertext tool for Exploratory Policy Discussion. ACM Transactions on Office Information Systems 6, 4 October.

Couger, J.D., Higgins, L.F., McIntyre, S.C., 1993. (Un)structured creativity in information systems organizations. MIS Quarterly December, 375–397.

Courtial, J.P., 1994. A coword analysis of scientometrics. Scientometrics 31, 251–260.

Cyert, R., March, J., 1963. A behavioral theory of the firm. Prentice-Hall, Englewood Cliffs, NJ.

Daft, R., Weick, K.E., 1984. Toward a model of organisation as interpretation systems. Academy of Management Review 9, 284–296.

Davis, G.B., Olson, M., 1985. Management information systems: foundations, structure and development. McGraw-Hill, New York.

Drucker, P.F., 1993. Managing in Turbulent Times. Reprint edition. Harper Collins Publishers, ISBN: 0887306160.

El Sawy, O., 1985. Personal information systems for strategic scanning in turbulent environments: can the CEO go on-line? MIS Quarterly March, 53–60.

El Sawy, O.A., Pauchant, T., 1988. Triggers, templates and twitches in the tracking of emerging strategic issues. Strategic Management Journal 9, 455–473.

Freeman, O., 1999. Competitor intelligence: information or intelligence. Business Information Review 16 (2), 71–77.

Futures Group, 1997. Ostriches and eagles 1997, Futures Group Inc. (August) available from http://www.tfg.com/pubs/docs/0\_Elll-97.html.

Galliers, R.D., 1991. Strategic Information Systems planning: myths reality and guidelines for successful implementation. European Journal of Information Systems 1 (1), 55–64.

Gilad, T., Gilad, B., 1986. Business intelligence. The quiet revolution. Sloan Management Review 27, 53–62.

Groom, J.R., David, F.R., 2001. Competitive intelligence activity among small firms. SAM Advanced Management Journal winter, 12–20.

Grove, A., 1999. Only the paranoid survive: How to Exploit the Crisis Points that Challenge Every Company. 1st current edition, Bantam Books.

Hall, C., 2001. The intelligent puzzle. Competitive Intelligence Review 12 (4), 3–14.

Herring, J.P., 1998. What is intelligence analyst? Competitive intelligence Magazine 1 (2), 13–16.

Kanter, R.M., 1988. Change-Master Skills: What it takes to be creative. In: Kuhn, R.L. (Ed.). Handbook for Creative and Innovative General Managers. McGraw-Hill, New York, NY, pp. 91–99.

Kelly, K., 1998. New rules for the new economy: ten ways the network economy is changing everything. Fourth Estate, London.

Koneig, G., 1996. Management stratégique, paradoxes, interactions et apprentissages. Nathan, Paris.

Lesca, H., Caron, M.L., 1995. Veille stratégique: créer une intelligence collective au sein de l'entreprise. Revue Française de Gestion septembre–octobre, 58–68.

Lesca, H., 1994. Veille strategique pour le management strategique état de la question et axes de recherche. Economies et sociétés, série Science de Gestion 5 (20), 31–50.

Maccrimmon, K.R., Wagner, C., 1994. Stimulating ideas through creativity software. Management Science 40(11), 1514–1532.

Martinsons, M.G., 1994. A strategic vision for managing business intelligence. Information Strategy Spring, 17–33.

McCann, J., Gomez-Meija, L., 1992. Going on-line in the environmental scanning process. IEEE Transaction on Engineering Management 39 (4), 394–399.

McCusker, I.C., 1992. IT effectiveness—What does management need to know? The EDP Auditor Journal 3, 25–29.

Meyer, A.D., 1991. Visual data in organizational research. Organisation Science 2 (2), 218–236.

Miller, G.A., 1956. The magical number seven, plus or minus two: some limits on our capacity for processing information. Psychological Review 63 (2), 81–97.

Moore, G., McKenna, R., 1999. Crossing the chasm: marketing and selling high-tech products to mainstream customers. Rev ed. Perennial (Harper Collins) publisher, ISBN: 0066620023.

Nolan, J.A., 1999. It is the third millennium: do you know where your competitor is? Journal of Business Strategy November/December, 11–15.

Norman, 1982. Learning and Memory. W.H. Freeman, San Francisco, CA.

Piaget, J., 1996. Epistémologie génétique. Press Universitaire de France.

Plsek, P.E., 1996. Working paper: models for the creative process. available from http://www.directedCreativity.com/pages/WPModels.html.

Rittel, H., Kunz, W., 1970. Working paper. Issues as Elements of Information Systems. 131. Institute of Urban and Regional Development, University of California, Berkeley, CA.

Rouibah, K., 1998. Puzzle: a business intelligence tool for the interpretation of anticipatory and fragmentary weak signs. PhD Dissertation, Ecole Supérieure des Affaires, Université Pierre Mendès France, Grenoble, France.

Rouibah, K., Lesca, H., Malek, S., 1997. Business intelligence. A processing heuristic for weak signal. 15th Annual International Conference of AoM/IAoM, Montreal, Québec, Canada, 6–9 août 15 (1), 97–106.

Sabherwal, R., King, W., 1995. An empirical taxonomy of the decision-making process concerning strategic applications of information systems. Journal of Management Information Systems 11 (4), 177–214.

Schneider, S.C., Meyer, A.D., 1991. Interpreting and responding to strategic issues: the impact of national culture. Strategic Management Journal (12), 307–320.

Simon, H., 1960. The new science of management decision. Prentice-Hall, Englewood Cliffs.

Stenberg, R.J., 1988. The nature of creativity. Cambridge University Press, New York.

Subramanian, R., IsHak, S., 1998. Competitor analysis practices of US companies: an empirical investigation. MIR Management International Review 3, 7–23.

Thomas, J.B., McDaniel, B.R., 1990. Interpreting strategic issues: effects of strategy and the information-processing structure of top management teams. Academy of Management Journal 33 (2), 286–306.

Valette, F., 1993. Le concept de Puzzle: coeur du processus d'écoute prospective de l'environnement de l'entreprise. ThDoc ESA, France.

Wagner, J.A., Gooding, R.Z., 1997. Equivocal information and attribution: an investigation of patterns of managerial sense making. Strategic Management Journal 18 (4), 275–286.

Walls, J.G., Widmeyer, G.R., El Sawy, O.A., 1992. Building an information system design theory for vigilant EIS. Information System Research 3 (1), 36–59.

Wiseman, C., 1988. Strategic Information Systems. Irwin, Home-Wood, IL.
