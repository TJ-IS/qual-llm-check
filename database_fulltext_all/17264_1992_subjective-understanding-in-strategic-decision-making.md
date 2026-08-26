---
otero_id: 17264
otero_key: "9NUX52JT"
title: "Subjective understanding in strategic decision making"
authors: "Surya B. Yadav; Deepak Khazanchi"
year: "1992"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(92)90037-p"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Subjective understanding in strategic decision making

# An information systems perspective

Surya B. Yadav and Deepak Khazanchi

Area of Information Systems and Quantitative Sciences, College of Business Administration, Texas Tech University, Lubbock, TX79409-2101, USA

Decision makers and people in general, are constantly involved with understanding, formulating, and solving problems. Many of the problems faced by decision makers fall into the ill-structured/ill-defined category – as contrasted with well-structured/well-defined problems. This is especially true of problems faced by strategic decision makers. These problems routinely challenge the cognitive capacities of managers. Managers meet these challenges with limited information-processing capabilities. Decision makers perform various activities that help them understand ill-structured problems. These activities to a large extent are “cognitive” in nature. It is argued that IS support provided to managers “through” their “cognitive orientations” might facilitate understanding of ill-structured problems. A new concept called the called the “cognitive lens” is used to describe these cognitive orientations from an IS perspective. In conjunction with this notion, a classification of IS support in terms of a continuum of inquiry modes is proposed. These inquiry modes – introspective, dialectic, and eclectic inquiry – operate on cognitive lenses stored and maintained in a “cognitive lens support system.” The system architecture and the functional support required to facilitate the different inquiry modes are also described.

Keywords: Cognitive lens, Cognitive lens support system, Cognitive model, Ill-structured problem, Understanding-activities, Strategic planning process, Inquiry mode, Problem understanding.

![](/api/attachments/9NUX52JT/fulltext/images/b82399f18f0ce468bcf738862bcbd1fabe0a6907512a9cd0bac63dffb911520d.jpg)

Surya B. Yadav is Associate Professor of Information Systems at Texas Tech University. He received his Ph.D. in Business Information Systems from Georgia State University in 1981. He has a M.Tech. in Computer Science from the Indian Institute of Technology, Kanpur, and a B.S. in Electrical Engineering from Banaras Hindu University. Professor Yadav has published in several journals, including Communications of the ACM, JMIS, Journal of Systems and Software, and Deci sion Support Systems. His research interests include expert systems for information requirements determination, adaptive knowledge-based systems, and software engineering.

## 1. Introduction

The ability of an executive to have a subjective understanding of his own decision process for a given problem domain has often been emphasized, but rarely practiced in developing information systems. When an executive faces an ill-structured problem situation he generally makes an “intuitive” or “seat of the pants” decision. For example, it is argued that actual planning in the manager’s workday world may become planning via intuition. Such planning is highly dependent on the person or persons involved. ‘Hunch’, ‘judgment’, ‘synthesis’, and ‘intuition’ are the key words involved in determining success or failure of the planning effort $[10,28,36]$ . These concepts relate to the individual’s belief system and that of the other members of the organization. In fact, some researchers report that “beliefs are … a powerful constraint on the options the executive will consider and the decisions they make … these beliefs can be so powerful a constraint that top management may miss opportunities presented by actual or potential changes in the objective constraints” $[11, p. 10]$ .

Thus, at the outset, it seems reasonable to believe that an attempt to aid decision-makers in a

![](/api/attachments/9NUX52JT/fulltext/images/c688f7968a0be14c509bfdf6c112026c426240fdb55b3d58ce516a7d83b2ed01.jpg)

include IS support for ill-structured problem solving, cognitive aspects of human-computer interaction, strategic impact and use of IT, intelligent systems, and evaluation of systems.

form that facilitates understanding of problems, should be included as one of the primary objectives of providing information systems support. This achievement of understanding, especially with regard to ill-structured problems, should result in higher decision quality, and a greater degree of decision confidence.

The field of information system is presently undergoing a “paradigm shift” [23] – a radical change in the field’s approach to its subject matter, its methods and its interpretation of findings. This change seems to be a movement from a behavioristic orientation to a cognitive orientation. In other words, the emphasis on information systems (IS) support for the behavioral aspects of decision making is shifting towards providing support for the cognitive orientations of decision-makers. Researchers seem to look for ways to provide IS support for the subjective understanding of ill-structured problems such as strategic decision making. The move towards supporting the cognitive orientations is a result of the fact that there now exists some ability to capture a decision-maker’s a priori experiences, perceptions, values, and beliefs and represent them in a form that can be readily manipulated and refined [2,17,31]. This representation may be in a form that is amenable to a computer system that allows the explicit specification of decision-makers’ cognitive orientations. The system would be an aid for enhancing the decision-makers’ understanding of their own decision processes and cognitive structures [6,13,32,41].

## 1.1. Problem definition

A manager makes decisions based upon his “view” of the world. This is especially true of decisions that are strategic in nature $[1,27,39]$ . The process of strategy making, as any other organizational process, is much dependent on the individual cognition of the world by the organizational members $[10,11]$ . The solution to such ill-structured problems rests mainly on the “cognitive” efforts of the decision-makers $[20,24]$ . Managers make decisions like whether to react to, ignore, try to influence, or anticipate the opportunities or threats in the environment. Thus managers “perceptions” may be different from the environment’s objective condition. In effect, diagnosis is an opinion $[15,27]$ . This opinion of the environment is based on the decision-maker's implicit cognitive orientation.

Although the issues of understanding and representing this subjective aspect of decision making have been addressed in a number of referent IS disciplines such as artificial intelligence, cognitive science, and management science; IS literature seems to have largely ignored this problem. There appears to be a lacuna in the IS literature about some formal basis of systematically investigating the nature and type of information system support that can be provided to decision-makers involved in making such subjective decisions. (This point will be further reinforced in the literature review section). Consequently, it can be stated that there appears to be a need for a conceptual model that incorporates a cognitive perspective of information system support for ill-structured problem domains. This need appears to be especially critical for the improvement of a decision-maker's understanding of the problem.

## 1.2. Objectives

The primary objective of this paper is to conceptually develop and validate a cognitive perspective of information systems support for ill-structured problem domains. In particular, this paper has the following objectives.

1. To develop and detail a new notion called the cognitive lens, and illustrate its use in an ill-structured problem domain, such as strategic decision making. Specifically, the notion is applied to the strategic planning process.

2a. To derive a set of activities that facilitate understanding of ill-structured problems. Henceforth, these activities will be referred to as understanding-activities.

2b. To develop a set of IS functions using the notion of cognitive lens, to support the understanding-activities. These functions are proposed as an integral part of a general classification of information system support for the cognitive lens.

2c. To propose a supporting architecture for a cognitive lens support system based on the understanding-activities and the classification of IS support.

3. To provide initial validation for the conceptual development in this paper. The validation of the concepts is achieved through the means of both illustrative and tautological evidence.

## 1.3. Review of relevant literature

Cognition is the act or process of knowing including awareness and judgment. Every decision-maker – whether it be a person making decisions about their own life or an executive making corporate decisions, uses this ability of “cognition” to capture information to “understand” and produce alternative solutions about a problem domain. Keen and Scott Morton [20], assert that such information is not an objective commodity but a personalized response to one’s environment. They further argue that the implications for decision support systems are obvious – the system should mesh with the cognitive structures of its users. Gorry and Scott Morton [16], in discussing their framework for information systems indicate that the missing ingredient (associated with IS activities in most organizations) apart from basic awareness of the problem, is the skill to elicit from the management, it’s view of the organization and it’s environment, and to formalize models of this view.

Donaldson & Lorsch [11, p. 279–80], in a study of top executive decision making in a dozen leading corporations concluded that among the corporate managers in each of the companies investigated, there existed a distinctive system of “beliefs.” They reported that, “… these system of interrelated beliefs act as a filter, through which management perceives the realities facing the firm.” Thus, it appears that top decision-makers tend to rely heavily on support from their view of the world around them in handling ill-structured problems.

Ford and Hegarty [14], in an exploratory study of decision-maker's beliefs concluded that “... contemporary organizations face turbulent environments that require frequent adaptive decisions in order to survive. These decisions must be made, in part, on the cause/effect maps that the decision-makers use as a basis for evaluating various options they have available. A better understanding of what these maps are, how they are developed, and how they are used will further the understanding of both individual and organizational behavior” [p. 290]. This further reinforces our assertion in the previous section about the need of a cognitive approach to providing IS support to decision-makers.

It is argued that IS support for the belief systems of decision makers would be most useful for the initial stages of decision making – problem comprehension or problem understanding, and problem formulation (decision recognition and diagnosis routines of Mintzberg [27] or the intelligence phase of Simon [39]). The next section explores this issue, and delineates the information support needs of a decision-maker involved in achieving some degree of understanding of an ill-structured problem.

## 2. Understanding ill-structured problems

Most researchers agree that while there is a best way to carry out structured tasks, ill-structured tasks require each decision-maker to make a situational value judgment from their personal frame of reference $[16]$ . A very common example of a structured task is the inventory control problem. This problem has a definite structure, is not too complex, and the problem of estimating the inventory reorder level is easily understood in terms of its various constituent constructs (variables such as demand, order costs, etc.) and their functional relationships. On the other hand, consider the strategic planning problem of capital structure financing (debt versus equity) for an organization. This problem is definitely complex, ill-structured, occurs infrequently, and is not very well understood by decision-makers $[33]$ . In fact the capital structure problem has been mathematically modeled and analyzed by numerous researchers, and it appears that the solution lies in understanding why capital structure decisions matter rather than whether they matter $[30, 33]$ . Furthermore, managers making capital structure decisions tend to bring into the decision a number of external constructs and relationships that may have little similarity with a normative perspective of the problem $[33,38]$ . This ill-structuredness, and the accompanying lack of understanding on the part of the decision-maker seems to be symptomatic of most strategic problems $[14,27,34]$ .

As discussed in the previous section and illustrated by the capital structure example, decision-makers tend to understand ill-structured problems on the basis of their cognitive orientations. In confirming this conclusion, Pounds [34, p. 5] argues that “... because a manager’s world is complex .... The problem of understanding problem finding is ... eventually reduced to the problem of understanding the models which managers use.” He further adds that “... problem definition cannot precede model construction. It is impossible to know, for example, that a cost is too high unless one’s own experience has some basis which suggests it might be lower. This basis might be one’s own experience, the experience of the competitor, or the output of a scientific model” [p. 17].

Thus, it appears that a decision-maker develops an understanding of an ill-structured problem in two basic ways: First, from the quantitative data that he can objectively analyze – thus in the capital structure problem, though the level of debt may have been directly available as a quantified entity, the decision-maker implicitly represents it as the belief about the level of debt rather than the dollar value of the debt itself; Second the decision-maker uses his “judgment” to make the final diagnosis based on his “view” of the world (problem domain).

Decision-makers implicitly have complex belief systems about a problem domain, but rarely analyze the whole system when formulating ill-structured problems $[2,11]$ . This is attributed to “bounded rationality” on account of limited information processing capabilities of decision-makers $[39]$ . It results in the utilization of only a condensed portion (a system of simplified higher level constructs) of their implicit cognitive orientations.

The above discussion provides some insight into the nature of ill-structured problems and the process of understanding and formulating them. It appears that there are numerous information needs that should be embodied in any computer system that provides support to decision-makers for understanding and formulating ill-structured problems. In discussing system support for problem solving, Coombs and Alty [9, p. 23] assert that, “... the system would be explicitly concerned with supporting the conceptual aspect’s of a decision-maker’s effort at problem solving; providing an environment in which the user may achieve a better understanding of his problem, and in so doing be equipped to solve it.”

This assertion reinforces the arguments detailed in the previous discussions about the nature of support needed for understanding ill-structured problems. The promotion of problem understanding is achieved by activities that [9,11,20]:

1. provide some degree of structure to the contextual information based on the decision-maker's cognitive orientation; in other words providing an opportunity to obtain an insight into their own thinking;

2. focus attention on the important aspects (for example, the centrality of constructs) of the structure of their cognitive orientations; and

3. help to analyze their view of the problem, compare with other's view, study a synthesized view, and predict the outcomes of given processing circumstances on the whole cognitive structure and/or its constituent components.

These needs dictate the type of “activities” that would have to be supported by an information system designed to aid decision-makers in the understanding and formulation of ill-structured problems. The first need suggests understanding-activities such as modeling, simplification, and comprehension, that provide the decision-maker the ability to look at their own cognitive orientation and allow them to understand its inherent organization. Evaluation, inquiry, and testing are examples of the activities that derive from the second need described in the previous paragraph. The third set of understanding-activities involve analysis, comparison, and synthesis.

These understanding-activities, when provided in a support system, will help promote understanding of ill-structured problems. These activities are further explicated in the following paragraphs.

1. Simplification. Involves answering the question, 'can the system help organize the ill-structured problem in terms of constructs and relationships derived from my (the decision-maker's) view?' In other words, this is an attempt to translate the overwhelming complexity of the problem into familiar and comprehensible terms.

2. Comprehension and clarity. The decision-maker is able to look at his own view of the problem in terms that are familiar to him. The decision-maker uses the system to look at the inherent structure of his own belief system.

3. Analysis. Involves the ability to examine critically the structure of the decision-maker's belief system. For example, in the capital structure problem the decision-maker is able to examine the impact and importance of individual constructs, for example, “level of debt” compared to others like “fear of bankruptcy.” Analysis provides an opportunity to simplify complex belief systems into a manageable and critical set of constructs and relationships between constructs.

4. Inquiry. An ability to systematically investigate one's own thinking about the problem. This implies an ability to query and understand one's own cognitive structure, and that of one's organizational peers (or experts), competitors, and others working in the same environment.

5. Comparison. This is achieved through inquiry and direct comparisons. It involves answering questions such as – does my view of the problem differ from my peers, competitors, or from other normative models? Coupled with inquiry and analysis, this becomes a powerful activity. It provides an opportunity to confirm (or disconfirm) often entrenched beliefs, perceptions and values about a problem. By being able to look at one's own view, and that of others, an opportunity is provided for checking the feasibility and validity of some of the constructs and their linkages. In effect the very foundations of the decision-maker's system of beliefs can be tested.

6. Evaluation. Involves an ability to measure the worth of one's own belief system through querying and analysis. Furthermore, this implies an ability to test and evaluate alternative cognitive structures by modifying, deleting, adding constructs and/or relationships, and then determining the impact of these changes.

7. Synthesis and Condensation. These understanding-activities in combination with analysis, inquiry and testing allow the decision-maker to synthesize and/or aggregate two or more views of the same problem. Particularly, condensation allows the opportunity to group or combine constructs/relationships into meta-level views, and consequently increase problem understanding.

8. Projection and Prediction. An ability to predict and project the possible decision impact of an individual or groups view of the problem. This is achieved through seeing the problem from other's frame of reference. In addition, this allows the possibility of temporal projection of individual or group views and the enhancement of knowledge – which are nothing but well-grounded, true beliefs.

The above activities aid in the subjective understanding of ill-structured problems. An information (support) system must have the requisite functional capabilities to help perform these activities. Furthermore, the activities must be achieved “through” the cognitive orientations of the decision-makers. This suggests that a support system would have to be capable of representing and manipulating the cognitive orientations of decision-makers. This point will be further elaborated in subsequent sections.

## 3. Cognitive lens

A decision-maker perceives only that information relevant to him in order to achieve a specific goal within the problem space under consideration. In reviewing the literature, it was observed that a number of researchers have shown $[2,11,13,14]$ that the determination of this “relevant information” appears to depend upon the cause-maps (mental models) that decision-makers carry in their minds. These models serve as “interpretive lenses” which help decision-makers select certain aspects of an issue as important for diagnosis $[15,37]$ .

A model is a simplified representation of reality. It is created for a specific point of view. This “viewpoint” or “cognitive orientation” or “thinking” (so to say) assists the decision-maker to understand and formulate an ill-structured problem. The fundamental theme here seems to be that every decision-maker looks at his environment, both internal and external to the company, through his tinted glass, i.e., some type of an “innate model” or a “cognitive lens.” Once the information is received by the decision-maker, it is interpreted on the basis of this “cognitive lens” (see fig. 1) which represents all his a priori knowledge, beliefs, values, and perceptions about the problem domain. This information is then used to understand, formulate and/or make a diagnosis of the problem. In other words, the decision-maker’s cognitive orientation – made explicit by the “cognitive lens,” is used to achieve a semblance of understanding (and order) of an ill-structured problem.

Thus, the notion of cognitive lens attempts to capture a decision-maker's “encapsulation” of information in the form of “constructs” and “relationships” that are in reality a complete representation of the decision-makers viewpoint (see fig. 1). The cognitive lens is an attempt to model reality, but from a cognitive (or “individual’s”) frame of reference. A cognitive lens converts filtered information into a set of constructs and their interrelationships of the real world. The cognitive lens is at a level beyond the idea of filtration – that is, it is at a higher level of abstraction. It is not static like a filter. A cognitive lens is dynamic and adaptive in the sense that it is modifiable and can be refined based upon new environmental information perceived by a decision-maker. A cognitive lens casts perspective on information. The same information may be looked at from different perspectives – due to the cognitive lens. It should be noted that the cognitive lens presupposes the possibility of an objective cognitive orientation and does not imply a relativistic viewpoint. The linkages between constructs within the cognitive lens, are not taken to be causal in any precise way [12]. In fact, these interrelationships between the constructs could be causal, correlational, or based on judgmental probabilities. These linkages can be described as causal positive, causal negative, correlational positive, and correlational negative relationships. Each of these can be further assigned judgmental probabilities.

![](/api/attachments/9NUX52JT/fulltext/images/924818c57aeb550280aa295ce8c358e44f4377c1eb83a451caa645e467ffacf3.jpg)  
Fig. 1. Decision maker's cognitive lens.

In order for understanding to occur the decision-maker must interact with the environment affecting the problem. (In most cases this environment is the problem domain). This interaction of the decision-maker's cognition – described by his cognitive lens, with the problem domain, then, must be aided for understanding to be effective. There is no single cognitive lens that can be applied to every problem domain. A decision-maker will use different cognitive lenses for different problem-domains. Although the issues of formation and stimulation of the cognitive lens are not the subject of this paper, there are two important points that need to be emphasized. First, an external stimulus (or cue) would be needed to initiate the use of a latent (or an active) cognitive lens. This stimulus may be a desired goal or policy or utility. These would exist as inherent constructs in the decision-maker's cognitive lens. Second, the formation and the level of sophistication of a cognitive lens would be greatly dependent (in a temporal sense) on an individual's a priori experiences, beliefs, values, and perceptions relating to the problem domain.

To further illustrate the notion of cognitive lens, consider the various aspects of the strategic planning process (see fig. 2). The strategic planning process consists of a set of ill-structured situations [1,15]. The strategic planner's actions are driven by his cognitive lens and its interaction with the ill-structured problems associated with the strategic planning process.

Fig. 2 shows in the outer ring all the higher level concepts, called “superconstructs,” that are concerned with strategic planning. These superconstructs consist of a number of lower-level (in

![](/api/attachments/9NUX52JT/fulltext/images/70294683497aa4eb287b0122806e2921c35f027558963c442cce725ce03b5794.jpg)  
Fig. 2. Cognitive perspective of the strategic planning process from the viewpoint of the strategic planner.

terms of abstraction) constructs. For example, corporate mission and long range plan could both be superconstructs. Furthermore, corporate mission and long range planning subsume a number of lower-level constructs, which are developed by the strategic manager depending on his cognitive lens. Consider the statement of an executive who takes the available information about his company's strategic plan, and molds it according to his view [11]: "Our shareholders are looking for income and staying whole with inflation. We've got to keep them happy by diversifying the portfolio." The executive's constructs based on his cognitive lens are: "shareholders want a stable income," "effect of inflation," "we (the company) should keep the shareholders happy," and "the company should diversify their portfolio." Each of these constructs is linked together by relationships deducible from the executive's statement.

The capturing of the structure of the cognitive lens of a decision-maker, and the encompassing interaction with the problem domain, can allow him to see how he understands problems and makes decisions. In effect this would also allow him to have a conversation with his own thinking $[2,37]$ . In addition, the ability to introspect, discuss, and query their own cognitive lens should allow decision-makers to map large and complex information. This will not only increase the efficiency and effectiveness of the strategic planning process, but also allow the decision-maker to be more creative in finding solutions $[19]$ .

![](/api/attachments/9NUX52JT/fulltext/images/2a4490922029a6d8d64d0e30d3696d77b9f720c2b45b82a4110df3c0cc85ddd2.jpg)  
Fig. 3. Realms of IS support.

Consequent to the previous discussions, a system that provides decision-makers (such as strategic planners) an ability to inquire in various modes would furnish them with a basis to understand, evaluate and analyze their environment effectively and continuously $[19,26,29]$ . Not only could this be done in terms of their own cognitive lens, but also in terms of the cognitive lens of their peers, and competitive decision-makers. Thus, in order to provide IS support to a decision-maker involved with ill-structured problems, an information system has to provide the requisite capabilities to assist the understanding-activities “through” the cognitive lens. This statement is further explicated in the next section.

## 4. IS support for cognitive lens

It was argued at the beginning of this paper that the field of information systems is going through a “paradigm shift.” This shift in emphasis is reflected in the view of IS support shown in fig. 3.

The traditional realm has considered IS support for problem solving efforts (including problem understanding and formulation) to be as depicted in the left half of fig. 3. In this realm, the understanding-activities to be supported for a problem domain are derived for the problem, and aided by a system that incorporates requisite IS functions. No real emphasis is placed on the importance of the cognitive realm of the decision-maker (see fig. 3). This approach is adequate for well-structured problems. However, in the case of an ill-structured problem, the cognitive orientations of decision-makers play an important role in gaining understanding. These orientations form the basis for the understanding of ill-structured problems. Therefore, these understanding-activities must be performed “through” the cognitive orientations (described by a decision-maker’s cognitive lens) of the decision-makers. In other words, the activities to be supported, should accommodate the cognitive lens of the individual. In order for such a support to be tenable, it is proposed to treat the cognitive lens as a frame-based object. The support of the required understanding-activities through the cognitive lens is realized in terms of the interaction between the problem domain and the cognitive lens of the individual. Functions to be supported by an information (support) system help manipulate the cognitive lens and in turn also perform these activities. When support is provided in this fashion, the IS functions allow the decision-maker to “operate” on his cognitive lens for that problem domain.

An executive's use of the cognitive lens also depends on the type of inquiry he wants to make. For a given problem domain, executives may want to look at their own cognitive lens, or converse with other's cognitive lens, or develop a consensual lens for the problem. Any one of these modes of inquiry will promote problem understanding and consequently lead to a clear problem definition. In turn, a better understanding of the problem would lead to a greater decision confidence and higher decision quality.

A system adopting the idea of a cognitive lens does not provide the manager with a final solution for the problem. But, the use of a “cognitive lens support system,” allows the manager to inquire, in a Churchmaninan sense, not only of his own “weltanschauung,” but that of the world. The idea of a system with support for the cognitive lens is well grounded in the ideas of inquiring systems discussed by Churchman [7]. The notion of cognitive lens provides a vehicle to facilitate different inquiry modes. These modes allow one to get a better insight into the kind of IS support that is appropriate for improving problem understanding. The IS support perspective of the cognitive lens in terms of a classification based upon different inquiring modes is further detailed in fig. 4. A list of IS support functions that can be utilized within the different modes of an inquiry continuum are also listed and will be further described in the next section. The inquiring modes are introspective, dialectic and eclectic and are explained in fig. 4.

In order to further develop, at the implementation level, the functional requirements for IS support, it is useful to classify them into four general functional categories $[20,43]$ – Building, Retrieving, Inferencing, and Evaluating functions. Building functions incorporate construction, modification, and deletion. Retrieval functions allow the user to access information from the system database. Inferencing functions incorporate the ability to query, synthesis, condensing, projecting and predicting. This may involve changing the nature of the relationship or understanding an unknown relationship between constructs or predicting/ projecting the effect of a change in a relationship. Evaluating functions incorporate analysis, comparison, testing, and other similar modules. These functional categories can be utilized to generate a set of implementation modules along with an accompanying architecture for a cognitive lens support system.

<table><tr><td>Inquiry Mode</td><td>IS Support(in terms of functionality)</td><td>Result</td></tr><tr><td>IntrospectiveTo reflect orexamine the belief system for a problem domain. View ofdecision-maker&#x27;s perceptions in terms of their belief systems.Deduce the impact on specific oral strategic constructs through what-if, goal seeking, etc.analysis. This leads to not only an understanding of the decision-making process, but also provides an ability to predict using pre-existing constructs.</td><td>Introspective Inquiry- Examine Lens- Analyze Lens- Project Lens- Query Lens</td><td>Increased problem understanding, clarity and concretization of own belief system. Increased self-assurance, and improved decision confidence.</td></tr><tr><td>DialecticDiscussion &amp; reasoning as method of intellectual investigation. An Hegelian inquiry plus a predictive ability.Understand how &quot;others&quot; view their problem domain (environment) through their stated values &amp; beliefs; an argumentative (Hegelian) approach by conversing with/analyzing others&#x27; belief systems. Other&#x27;s here may be &quot;experts&quot;, &quot;competitors&quot;, or &quot;peers&quot;. Predicting others&#x27; constructs rather than the concepts of the person who is doing the predicting.</td><td>Dialectic Inquiry- Compare Lenses- Examine Lenses- Query Lenses- Project Lenses- Analyze Lenses</td><td>Highly increased problem clarity, understanding and concretization of own belief system. Highly increased decision confidence &amp; decision quality. Leads to more efficient and effective decisions both in the long and short run. This also provides flexibility in terms of decision choices and could be considered as a contingent outcome.</td></tr><tr><td>EclecticComposed of elements drawn from various sources. To some extent, provides a synergistic view. Similar to the dialectic mode, except that this mode involves synthesizing or aggregating belief systems of one or more decision-maker, competitive policy maker, expert, group, etc.. May involve development of collective maps in the form of group&#x27;s lens for diagnosis &amp; evaluation of environment and/or strategy alternatives. This leads to a map that will include the most valuable or important constructs and relationships of the group members for that problem domain.</td><td>Eclectic Inquiry- Describe Consensus Lens- Compare Lenses- Synthesize Lenses- Query Lenses</td><td>Leads to a consensus decision. Should result in a group decision that is most acceptable and clearly optimum in the group&#x27;s perception. Also, results in all the outcomes of the above two inquiry modes.</td></tr></table>

Fig. 4. Classification of IS support for cognitive lens.

## 5. Cognitive lens support system

Based upon synthesis of the existing literature on problem understanding and problem formulation, and the previous discussions, this section proposes a set of functions for each type of inquiry mode. The cognitive lens support system will allow the manager to use all of the inquiring modes detailed in the classification of IS support for the cognitive lens (see fig. 4).

## 5.1. Functional support

The functions specific to each inquiry mode are listed in fig. 4. This figure also describes the probable outcomes of each inquiry mode in terms of problem understanding, decision quality, and decision confidence. The functions are at the highest level of abstraction. A module that is common to all the inquiry modes is the “build domain-specific lens” module.

## 1. Build Domain-Specific Cognitive Lens

1.1 Construct Cognitive Lens

1.2 Modify Cognitive Lens

1.3 Delete Cognitive Lens

This module is not listed in the IS support function column in fig. 4. It falls into the “building functions” category. The module allows the creation of cognitive lens(es) and sets up the constructs and relationships. These are stored in the form of frames [25]. After eliciting constructs and related linkages (relationships), and the strength of the relationships (weights or probabilities) this function allows the creation of one or more cognitive lenses.

The three inquiry modes utilize modules that fall into one or more of the functional categories described earlier. Thus, “describe consensus lens” falls into the category of a “building function;” examine lens, analyze lens, and compare lens are modules belonging to the “evaluating functions” category; and query lens, synthesize lens, project lens are “inferencing functions.” The individual inquiry modes and their constituent functions are described below.

## 2. Introspective Inquiry

2.1 Examine Lens

2.2 Analyze Lens

2.3 Project Lens

2.4 Query Lens

This module provides the user an opportunity to perform the gamut of operations from sensitivity analysis of utility constructs, centrality of constructs, etc., to projecting and predicting using the cognitive lens of the manager. An introspective approach to inquiry allows the manager to reflect or examine their belief systems for a specific problem domain. Also this mode allows the manager to have a conversation with their own thinking.

3. Dialectic Inquiry

3.1 Compare Lenses

3.2 Examine Lenses

3.3 Query Lenses

3.4 Project Lenses

This module provides the user an opportunity to perform a dialectic inquiry by allowing comparisons between their cognitive lens and that of others. It also allows the manager to converse with the positions that are counter to their own thinking about a specific problem domain. In other words, it allows a dialectic examination of the problem. An ability to project the impact of a change in the relationship between one or more constructs is provided through the “project lenses” option.

4. Eclectic Inquiry

4.1 Describe Consensus Lens

4.2 Compare Lenses

4.3 Synthesize Lenses

4.4 Query Lenses

The eclectic inquiry module provides the manager a means of drawing on the belief systems of more than one source. This could also be used in group decision situations. It provides the option of the development of “views” of the world i.e. aggregation of cognitive lenses, and their synthesis – optimum or otherwise, for specific problem domains.

## 5.2. System architecture

The generic form of the cognitive lens support system architecture is detailed in fig. 5. The system consists of a “user-interface,” a “cognitive lens (CL) control system,” which in turn communicates with the “cognitive lens (CL) inquiry system,” and the “cognitive lens (CL) maintenance system.” It also includes a “cognitive lens database” which consists of cognitive lenses. These structures are stored and maintained in the system as frames. Each component of the cognitive lens support system is discussed in detail in the following paragraphs.

## 5.2.1. User-interface

This system provides a user-friendly interface for the decision-maker. For the novice user the system provides a interactive mode for developing and analyzing cognitive lenses. All inquiries will be guided through a system based query and reply operation. The system supports the manager in a form that is intuitive and easy to utilize. The user-interface is the only part of the system transparent to the user. The inputs for building a lens are in the form of constructs and relationships – mainly in a graphical form. Operational commands are intuitive and are based on the classification discussed earlier. The system allows the user to display the cognitive lens in the form of digraphs.

## 5.2.2. CL control system

The CL control system accepts information from the user-interface module and transfers control to the next module to be executed. For example, if the user is interested in building a cognitive lens, the control system module will direct the query to the maintenance system. This module is the hub of the system.

![](/api/attachments/9NUX52JT/fulltext/images/2f23ac2e86a772f7126f2a87c939eb4a02c1b418c17b12b2dde1488457d67475.jpg)  
Fig. 5. Cognitive lens support system architecture.

## 5.2.3. CL maintenance system

The CL maintenance system takes commands that deal with building and maintenance of the cognitive lenses. This module is used to elicit constructs, relationships, signs of the relationships, and weights of the relationships. After elicitation, the information is stored in the CL database as frames. The CL maintenance system, then, connects to the module handling the cognitive lens database.

## 5.2.4. CL inquiry system

The CL inquiry system makes operational all the inquiry modes discussed in previous sections of this paper. It provides the user the opportunity to analyze and evaluate their cognitive lens and others using the introspective, dialectic or eclectic inquiry mode. These inquiries are transmitted to the cognitive lens database.

## 5.2.5. Cognitive lens database

The cognitive lens database consists of cognitive structures stored and represented in the form of “frame-based objects” (see fig. 6). The frames are of standard form containing attribute slots and sub-frame slots [25]. The attribute slots do not point to other frames. The sub-frames are slots that point to other frames. These frame structures are dynamic in nature. The representation of the cognitive lens involves the use of four basic frames. The root-frame has slots for name, problem-domain and sub-frame slots. The sub-frame slots – superconstruct-slots, construct-slots and relationship-slots – in turn, point to three frames. The superconstruct frame defines a subset of the cognitive lens. It may subsume constructs and relationships and therefore in reality is a miniature version of the cognitive lens. A construct frame stores information about the concepts or constructs in the cognitive lens structure. The relationship frame is used to store information about the relationships between constructs. The cognitive lens database stores cognitive lens frames in terms of superconstruct(s), construct(s) and relationship(s) frames, and are normally built or modified by operations performed from the maintenance system. The CL database also provides access to this information through calls from the CL inquiry system.

![](/api/attachments/9NUX52JT/fulltext/images/e4213e81d93a3acd006e4c64cee0cc804927320636db965033e53bf8dec16b46.jpg)  
Fig. 6. Frame representation of cognitive lens.

## 6. Validation

The validity of the notions developed in this paper can be deduced from the literature referenced, and the research done in the areas of strategy and international policy making, cognitive science, and management science. This section reiterates some of the previous work that supports the concepts – cognitive lens, cognitive lens support system, and the continuum of inquiring modes for the cognitive lens, developed in this paper. In addition, the latter half of this section provides a hypothetical illustration of these concepts.

Many researchers [2,4,5,12,13,14,31,32], have used the approach of cognitive mapping (based on digraph theory) to provide empirical evidence for the idea that the belief systems of decision-makers could provide a basis for understanding, and generating and/or predicting solutions for ill-structured problems. Most of this work has been done in the area of international policy making. Bougon et al. have demonstrated the development of an aggregate view of the beliefs of the members of an organization [5]. Axelrod and his colleagues [2,3], have successfully documented research of their investigation of the individual and group belief systems of foreign policy makers using the idea of cognitive mapping. They have also shown that these representations of belief systems are not only stable over time, but are also predictive.

![](/api/attachments/9NUX52JT/fulltext/images/37fb016206fae4ce887e576f6da063dc359c9d6b65aaa58c4d5a169ef05c8ba6.jpg)  
Fig. 7. Hypothetical illustration (based on references [2] & [5]).

The cognitive lens, in effect is a higher level concept that subsumes the ideas of cognitive mapping and cognitive structures. The cognitive lens support system and the accompanying inquiring modes proposed in this paper are well grounded in the research discussed above. Furthermore, the works of Churchman [7] on inquiring systems, and that of Mason [26] and Mitroff [29] on dialectic inquiring systems provide strong support for the concepts of dialectic/eclectic/introspective modes of inquiry, proposed as a part of the classification of IS support for the cognitive lens.

## 6.1. Illustration of IS support

Some aspects of the notion of cognitive lens and the accompanying cognitive lens support system with its different inquiry modes is illustrated with the help of a hypothetical problem shown in fig. 7. Because this illustration is being used to validate the concepts developed in this paper, prosaic explanations are used in lieu of mathematical rigor. To provide some corroboration for the framework of inquiry modes and the related concepts, it is sufficient to show that many sophisticated conclusions can be deductively drawn. It is important to reiterate that the constructs and their associated relationships represented in the CL system are beliefs and should not be construed as variables with functional relationships. Consequently when a construct is labeled “profit” for example, it implies the belief of “profit” in the mind of the decision-maker, rather than the quantity of profit in the balance sheet. The construct cannot be quantified – it is just the persuasion or conviction about the notion of “profit” in the decision-maker’s thinking. Signed digraphs [2,18,35,40] are used to display and represent the cognitive lens in visual form. As observed earlier, these visual representations of cognitive structures are not limited to this technique. The following section presents a brief review of the notations and their meaning as utilized in the signed digraphs [2,18,35].

## 6.2. A brief digression: notations and their meanings

The digraphs in fig. 7 show the cognitive lens as a set of constructs and their relationships. Relationships or associations between constructs are represented by straight lines with an arrow indicating the direction of the association. A positive (+) sign on a path implies that the constructs on each end of the path have a direct association. In other words an increase in one construct, for example, “A” will result in an increase in the construct “B” available to the company. Similarly a decrease in “A” will result in a reduction in “B”. Thus a positive association means that changes occur in the same direction, but not necessarily positively [2], and vice versa. Relationships between constructs can be negative (−), implying that any change in one construct will result in an opposite change in the other construct (the construct at the end of the arrow head). For example, in the view of the first manager (see fig. 7a) a change in construct “A” results in a change in construct “B” in the same direction.

## 6.3. Analysis through inquiry

Some of the major conclusions that can be gleaned from each mode of inquiry in the cognitive lens support system can now be detailed.

## Introspective inquiry mode

In this mode the manager(s) are able to externalize and analyze their own thinking about the problem. Fig. 7a shows the cognitive lens of three managers for a hypothetical ill-structured problem. At the outset it is easy to recognize the effect of a construct, and the effect on any given construct. Some important construct(s) or constructs that have “cognitive centrality” [2] in the cognitive lenses can be identified by simply looking at the number of constructs directly effecting any given construct and at the number of constructs effected by the construct under consideration. Table 1 summarizes this result and indicates that the construct B is the most central in the first manager's cognitive lens.

Table 1

<table><tr><td>Construct</td><td>Effected by construct</td><td>Effects construct</td><td>Total effect</td></tr><tr><td>B</td><td>A</td><td>C</td><td>2</td></tr><tr><td>A</td><td>none</td><td>B</td><td>1</td></tr><tr><td>C</td><td>B</td><td>none</td><td>1</td></tr></table>

Table 1 also suggests that the first manager believes that “A” and “C” are of equal importance. The figure (manager 1, fig. 7a) also shows that an increase in “A” causes an increase in “B”, which in turn results in an increase in “C”. Thus, the net effect of “A” on “C” is positive and can be visualized as a single equivalent positive relationship between constructs “A” and “C”.

A similar analysis of the cognitive lenses of the other two managers (manager 2 and 3 in fig. 7a) indicates that the central or important construct for manager 2 is “C” and that for manager 3 is “A”. Also, the construct “B” has a net positive effect on “A” for manager 2 and “C” has a net positive effect on “B”. It can also be deduced from all the three lenses introspectively that each manager considers a different construct to be their utility and policy constructs [2,5] – a utility construct has no arrows going out from it, and a policy or goal construct has no arrows coming into it.

## Dialectic inquiry mode

In this mode the manager can compare his own lens with an opposing view. This opposing view could be a normative or expert view, or could be the view(s) of other managers. This dialectic inquiry can be the result of differences in the relationship(s) between one or more constructs. For this illustration, consider a dialectic of the first manager's cognitive lens with the other two lenses. Prima facie it appears that the manager 1 has the same constructs as the other managers. A deeper analysis of the cognitive lenses of manager 1 and manager 2 suggests that there is a different set of relationships between the three constructs. Since, this is a simplistic example this distinction can be easily made. In most realistic ill-structured problems, the belief systems of the managers are very complex [2] and it would be the cognitive lens system that would provide this comparative analysis. This dialectic also indicates whether some constructs and/or relationships are absent (or present) in the cognitive lens of the first manager. Furthermore for manager 1, it appears that the effect of a change in construct “A” results in an corresponding change in “C” in the same direction. This is not true in the case of manager 2. This comparison could provide the first manager with insight into the possible intricacy of the problem under consideration.

## Eclectic inquiry mode

This inquiry mode is useful for problem understanding in that it provides an eclectic insight of the problem (fig. 7b). This notion draws from research in group problem solving. It has been empirically demonstrated that groups tend to perform better (i.e., are more effective) in problem solving activities, compared to the “best” member’s contribution to the effort [8, 22]. These results suggest that team performance in problem solving tasks provides synergistic advantages. Drawing on this evidence, an eclectic inquiry on the cognitive lenses of the managers is used to analyze some combination of the cognitive lenses. Such an inquiry generally uses cognitive lenses in combinations of three or more – since a pairwise comparison can be easily obtained from the dialectic inquiry mode. This combination could be a median, average, mode, condensation [5,18] or some other form of aggregation. In the example being analyzed here the consensus lens (shown in fig. 7b) has been obtained by combining the cognitive lenses of the three managers. It can be visually seen that the “consensual lens” provides some additional information about the problem. Firstly, it suggests that each manager’s conceptualization is only a part of the whole problem. Secondly, it also appears that all the constructs are in fact connected to each other by relationships that are positive. [Note: This conclusion could have been drawn from the pairwise comparison of cognitive lenses in the dialectic inquiry mode, but the resulting interpretation is not as dramatic].

Lastly, the consensual lens also suggests that the nature of the relationships between the three constructs is really cyclic in nature. Thus, a change in “A” results in a change in “B” in the same direction, and which produces a change in “C” in the same direction, which in consequence changes “A”, and so on. This conclusion is important to the understanding of the problem, and also provides each manager with some additional insight.

## 7. Concluding remarks

It is relevant to mention here that there are extant systems for developing and analyzing cognitive maps, for example, COPE [12,13]. The proposed cognitive lens support system (CLSS) differs from such systems both in terms of its scope and objectives. Since it is not the objective of this paper to indicate the system's relative efficacy, a brief list of some of it's distinguishing features are listed below.

1. It (CLSS) allows more functionality and an ability to manipulate the cognitive lens. This functionality is not dependent on any specific tool (e.g., cognitive mapping);

2. It provides a higher level of functionality to look at belief systems, which are closer to the natural cognitive processes and decision structures of managers;

3. It allows decision-makers to inquire in dialectic and eclectic modes in addition to introspective mode;

4. The notion of “cognitive lens” incorporated in the system provides a means of systematically investigating strategic decision-makers’ perspectives of their own “views” (and that of others) about a problem; and

5. The fundamental objective of this system is to facilitate problem understanding “through” the cognitive lens. In doing this, the system would assist decision-maker’s involved with handling ill-structured problems, such as strategic planning, to enhance their understanding of the problem.

It is becoming apparent that an understanding of the cognitive processes and structures of decision-makers is an issue of great importance to the information systems (IS) field. This paper introduces a new concept called the “cognitive lens.” The “cognitive lens” provides a way of looking at a decision-maker’s perspective of their own “view” (and that of others) of an ill-structured problem. An investigation of activities that promote problem understanding suggests some functional capabilities for a support system. This support system facilitates problem understanding “through” the cognitive lens. A classification of inquiry modes and IS support in terms of requisite functionality relevant to the concept of the cognitive lens have also been developed. The cognitive lens support system stores and maintains cognitive lenses as dynamic frames. Visual representation and some mathematical analysis are achieved through the use of signed digraphs – which derive their rigor from graph theory in the field of mathematics. The notion of cognitive lens and the classification of inquiry modes for the cognitive lens systems are corroborated using both tautologous and illustrative evidence.

In general, the cognitive lens support system provides an opportunity to decision-makers associated with solving ill-structured problems, such as those in the strategic planning process, to enhance their understanding of their own “cognitive structure,” and that of their competitors. This should provide executive’s with the opportunity to gain a competitive advantage not only in a business sense, but also in terms of the higher level of certainty and understanding that accrues from being able to view their cognitive lenses and that of their competition.

## References

[1] R.N. Anthony, Planning & Control Systems-A Framework for Analysis (Harvard University Press, Boston, 1965).

[2] R.M. Axelrod (Editor), Structure of Decision-The Cognitive Maps of Political Elites (Princeton University Press, Princeton, 1976).

[3] R.M. Axelrod, Framework for a General Theory of Cognition & Choice (Institute of International Studies, University of California, Berkeley, 1972).

[4] M.G. Bougon, Uncovering Cognitive Maps, in: G. Morgan, Ed., Beyond Method-Strategies for Social Research (Sage Publishers, Beverly Hills, 1983).

[5] M.G. Bougon, K. Weick and D. Binkhorst, Cognition in Organizations: An Analysis of the Utrecht Jazz Orchestra, Administrative Science Quarterly 22 (Dec., 1977) 606–639.

[5] J.G. Carbonell, Subjective Understanding: Computer Models of Belief Systems (UMI Research Press, Ann Arbor, 1981).

[7] C.W. Churchman, The Design of Inquiring Systems, Part I (Basic Books, New York, 1971).

[8] R. Cooke and J. Kernaghan, Estimating the Difference Between Group Versus Individual Performance on Problem-Solving Tasks, Group Organizational Studies 12, Nr. 3 (1987) 319–342.

[9] M. Coombs and J. Alty, Expert Systems: an alternative

paradigm, International Journal of Man-Machine Studies 20 (1984) 21–43.

[10] T.K. Das, The Subjective Side of Strategy Making-Future Orientations and Perceptions of Executives (Praeger Publishers, New York, 1986).

[11] G. Donaldson and J.W. Lorsch, Decision Making At The Top: The Shaping of Strategic Direction (Basic Books, New York, 1983).

[12] C. Eden, Cognitive Mapping, European Journal of Operational Research 36 (1988) 1–13.

[13] C. Eden, S. Jones and D. Sims, Thinking in Organizations (The Macmillan Press, London, 1979).

[14] J.D. Ford and W.H. Hegarty, Decision Maker's Beliefs About the Causes & Effects of Structure: An Exploratory Study, Academy of Management Journal 27, Nr. 3 (1984) 271–291.

[15] W.F. Glueck and L.R. Jauch, Strategic Management and Business Policy (McGraw-Hill Book Comp., New York, 1984).

[16] G.A. Gorry and M.S. Scott Morton, A Framework for Management Information Systems, Sloan Management Review, (Fall 1971) 27–42.

[17] G. Grudnitski, Eliciting Decision-Maker's Information Requirements-Application of The Rep Test Methodology, Journal of Management Information Systems 1, Nr. 1 (Summer 1984) 11–32.

[18] F. Harary, R.Z. Norman and D. Cartright, Structural Models: An Introduction to the Theory of Directed Graphs (John Wiley & Sons, New York, 1965).

[19] S. Jones and D. Sims, Mapping as an Aid to Creativity, Journal of Management Development 4, Nr. 1 (1985) 47–60.

[20] P.G.W. Keen and M.S. Scott Morton, DSS-An Organizational Perspective (Addison-Wesley Pub. Comp., Reading, 1978).

[21] G.A. Kelly, The Psychology of Personal Constructs, Volume One (W.W. Norton & Comp., New York, 1955).

[22] J.A. Kernaghan, Group Versus "Best" Member Contributions To Effective Decision Making By Work Teams, Midwest Division Academy of Management Conference Proceedings, Milwaukee, Wisconsin, April 18–21 (1990) 109–114.

[23] T.S. Kuhn, The Structure of Scientific Revolutions (University of Chicago Press, Chicago, 1962).

[24] H. Lucas, Jr., Computer Based Information Systems in Organizations (SRA, Chicago, 1986).

[25] G.F. Luger and W.A. Stubblefield, Artificial Intelligence and the Design of Expert Systems (The Benjamin/Cummings Publ. Comp., Redwood City, 1989).

[26] R.O. Mason, A Dialectical Approach To Strategic Planning, Management Science 15, Nr. 8 (April, 1969) B403-B414.

[27] H. Mintzberg, D. Raisinghani and A. Théorêt, The Structure of “Unstructured” Decision Process, Administrative Science Quarterly 21, Nr. 2 (June, 1976) 746–755.

[28] H. Mintzberg, Planning on the Left side & Managing on the Right, Harvard Business Review 54, Nr. 4 (July-August, 1976) 49–58.

[29] I.I. Mitroff, A Communication Model of Dialectical Inquiring Systems-A Strategy for Strategic Planning, Management Science 19, Nr. 10 (June, 1971) B634-B648.

[30] F. Modigliani and H. Miller, The Cost of Capital, Corporation Finance, and the Theory of Investment, American Economic Review (June, 1958) 261–297.

[31] A.R. Montazemi and D.W. Conrath, The Use of Cognitive Mapping for Information Requirements Analysis, MIS Quarterly 10 (March, 1986) 45–55.

[32] A.R. Montazemi, D.W. Conrath and C.A. Higgins, An Exception Reporting Information System for Ill-Structured Decision Problems, IEEE Transactions on Systems, Man, and Cybernetics SML-17, Nr. 5 (September/October, 1987) 771–779.

[33] J.M. Pinegar and L. Wilbricht, What Manager's Think of Capital Structure Theory: A Survey, Financial Management (Winter 1989) 82–91.

[34] W.F. Pounds, The Process of Problem Finding, Industrial Management Review 11, Nr. 1 (Fall 1969) 1–19.

[35] A.P. Sage, Methodology For Large-Scale Systems (McGraw-Hill Book Comp., New York, 1977).

[36] J. Schermerhorn, Jr., Management For Productivity (John Wiley & Sons, New York, 1986).

[37] C.R. Schwenk, The Cognitive Perspective of Strategic Decision Making, Journal of Management Studies 25, Nr. 1 (January, 1988) 41–58.

[38] D.F. Scott, Jr. and D.J. Johnson, Financing Policies and Practices in Large Corporations, Financial Management (Summer 1982) 51–59.

[39] H. Simon, The New Science of Management Decision (Harper, New York, 1960).

[40] J.N. Warfield, Societal Systems-Planning, Policy And Complexity (John Wiley & Sons, New York, 1976).

[41] C. Wegman, Conceptual Representation of Belief Systems, Journal for the Theory of Social Behavior 11, Nr. 3 (1981) 279–305.

[42] K.E. Weick, Cognitive Processes in Organizations, in: B.M. Staw, Ed., Research in Organizational Behavior, Volume I (JAI Press, Greenwich, 1979).

[43] L.F. Young, Computer Support For Creative Decision Making: Right Brained DSS, in: H.G. Sol, Ed., Processes and Tools for Decision Support (North-Holland Pub. Comp., Amsterdam, 1983).
