---
otero_id: 23830
otero_key: "EU3VXVG9"
title: "Decision-Variable Partitioning: an alternative modelling approach in Soft Systems Methodology"
authors: "J Ledington; P W J Ledington"
year: "1999"
journal: "European Journal of Information Systems"
doi: "10.1057/palgrave.ejis.3000311"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision-Variable Partitioning: an alternative modelling approach in Soft Systems Methodology

J Ledington and PWJ Ledington

School of Information Systems and Management Science, Griffith University, Nathan, Q 4111, Australia

Creating human activity system models is an essential feature of Soft Systems Methodology. It is an area of the methodology that has received very little research attention and has remained static for the past fifteen years. This paper argues the need for further development of the modelling approach involved in Soft Systems Methodology, demonstrates that conventional models are based upon functional decomposition, and presents an alternative modelling approach called Decision-Variable Partitioning.

## Introduction and background

The emergence and development of Soft Systems Methodology (SSM) (Checkland, 1981; Checkland & Scholes, 1990) and its integration into the information systems field has produced a continuing strand of research activity (see for example: Wilson, 1984; Wood-Harper et al, 1985; Avison & Wood-Harper, 1990; Davies & Ledington, 1991; Lewis, 1994; Stowell, 1995). The research reported in this paper contributes to this stream of research by focusing on issues arising in the modelling process applied within SSM. The paper presents a new approach to this aspect of SSM.

The application of Soft Systems thinking to the development of formal information systems has highlighted the problem of deciding which information systems, of the many possible information systems that could be developed in any situation, to actually develop. This can be termed the problem of strategic requirements analysis. The SSM approach to this problem (Checkland & Scholes, 1990) is to argue that any formal information system is only meaningful to the extent that it supports and facilitates some organised human activity (often more colloquially termed, organizational activities, business activities, or business processes). The question then emerges as to which of the many possible perceptions, or meanings, given to the actions in a situation should be used as the basis for defining the business activity concerned. For example, is a university department about teaching, research, scholarship, learning, or managing the interaction of all of these.

SSM provides a structured approach to making explicit the various meanings associated with a situation through the development and use of human activity system models. Creating such models allows the meanings and the implications of taking those meanings seriously within the situation to be discussed and debated by those involved in, and responsible for, the situation. The aim is to establish a stable definition of the activity supported by these stakeholders in the form of a human activity system model, which may then be used as a framework for determining the information systems required to support the activity concerned.

In principle, the Soft Systems approach to the requirements problem appears sound but in practice it is plagued by a range of issues which limit its usefulness. First, there can be difficulties in producing defensible activity models. Boyle (1995), for example, found that different modellers produced quite different activity models representing different world-views from the one root definition. Ledington and Donaldson (1997) found that many who claimed to be SSM users did not use the conceptual modelling process. As the model is central to the SSM approach, any uncertainty or lack of confidence in the model reduces the level of confidence in the overall analysis. Second, it is often difficult to express nuances of meaning within conceptual models, especially for inexperienced users. Third, conceptual models often seem simplistic when compared to the actual situation, a situation that often necessitates the use of multiple models. Fourth, the information aspects of human activity models are not strongly defined and this leads to uncertainty about the information systems identified using the approach. When, in the extreme, these problems combine, users can be faced by a large modelling and comparison effort that creates ambiguous and uncertain results that, in turn, can lead to the rejection of the overall approach. It appears, therefore, that there are problems with the expression of activity systems models in SSM that may limit its acceptance and effectiveness in practical situations. Hirschheim et al (1995, p 127) support this view by suggesting that “SSM needs better modelling methods and support tools. Its conceptual modelling method is too simplistic even when compared to standard structured process modelling (i.e. levelled data flow diagramming), let alone when compared to object-oriented organizational modelling”.

The research theme that this paper begins to explore arises from these issues identified above. The theme can be focused around two questions:

How can an SSM conceptual model be structured and expressed other than in the conventional form reported in the research literature?

What are the implications of using such an alternative modelling approach?

The rest of this paper reports some initial research that has begun to explore these questions. The paper proceeds as follows. Section 2 critiques the modelling approach used in SSM. Section 3 describes an alternate decomposition strategy named Decision-Variable Partitioning (DVP) and Section 4 provides an example of the use of DVP in a real-world SSM project. Section 5 concludes with a discussion on directions for future research.

## A critique of the modelling approach used in SSM

SSM embodies a cycle of activities whereby a definition is chosen, formalised into a root definition, a conceptual model is developed from the root definition, the model and situation are compared, and the comparison is used to structure a debate about change amongst the stakeholders of the situation. The term ‘conceptual model differs from the normal connotation of the term ‘model’ as a formal description of some phenomenon. In SSM, a conceptual model is a logically derived framework for interpretation. The model expresses a logical statement of a particular definition thought to be meaningful in the context of a situation by a participant in that situation.

The conventional approach to constructing a conceptual model from a root definition is to identify the activities implied by the root definition and then to structure them according to their logical dependence upon each other. The aim is to produce a model that represents the minimum but necessary set of interconnected activities to be the system specified in the root definition. Essentially the modelling process is to partition the overall system as represented by the root definition into the minimal set of subsystems and relationships (activities and logical dependencies). The approach to model development in SSM, therefore, is consistent with the concept of functional decomposition (DeMarco, 1978). SSM provides only limited and informal guidelines for creating the decomposition, i.e. comparing the model with the root definition and limiting the number of activities to around ten at any one level. The only partitioning enforced for the model is the separation of the operative transformation process from the control subsystem that operates upon the transformation process. SSM provides no guidelines for partitioning the transformation process of the system or for determining whether a minimally partitioned set of activities has been established.

Three difficulties can be recognised in the conceptual modelling process. First, real-world problem solving can involve more than one transformation or focus. Often, multiple focuses need to be considered and prioritised yet the process involved in SSM considers each focus separately as only one transformation is modelled. The methodology of SSM involves a number of iterations through the enquiry cycle of construct, compare, and debate using one transformation statement for each iteration. The conceptual models do not provide for multiple transformations to be represented. For example, a university is often considered to be about teaching and research, but there is a lot of discussion and debate in our university about whether the priority or focus should be on research first and teaching second, or whether teaching should be considered as the first priority. There is also a concern on how the two can be linked together to form a coherent whole. The present strategy of singletransformation modelling in SSM does not allow these issues to be readily addressed.

Second, root definitions often contain secondary transformations. The focus of the secondary transformation is then lost in the conceptual modelling process using the functional decomposition approach because only the primary transformation is functionally decomposed.

For example, the root definition: ‘. . . to provide courses to increase technical skills and knowledge for suitably qualified and interested parties, that will be of value to the industry, whilst meeting BTEC approval in a manner that is both efficient and financially viable (Wood-Harper et al, 1985, p 57); contains the transformation of unprovided courses to provided courses and the transformation of interested parties (students) with less skills and knowledge to students with more skills and knowledge. In the model that is subsequently produced from this definition, Wood-Harper et al only focus on, and functionally decompose, the transformation relating to courses. The focus on students is lost in their decomposition by being spread over a number of subsystems. Furthermore, it is not clear from the root definition which of the transformations is the primary focus. The prioritising or ordering of the transformations affects the world-view. For example, if students are the primary focus then courses can be tailored to meet students needs or options other than courses can be considered to increase students’ skills and knowledge. Whereas, if courses are the primary focus and students the secondary focus then students would have to take prearranged courses.

Third, SSM has an underlying assumption that humans socially construct their reality and the power of SSM lies in its ability to make explicit the different views in a situation and to facilitate and record the debate about change. Experience suggests that debate is not always about the primary transformation or focus in a situation but rather about the rules or constraints that govern each transformation. Recently, our daughter was suspended from school for two weeks because she had coloured her hair. The school she attends has very strict dress rules and it will only provide lessons to students if they are suitably attired. This rule has been socially constructed and is often hotly debated amongst the students, parents, and teachers. The rule also distinguishes the school from many others in the area that have changed over time to a less strict dress code. Rules such as these are socially constructed yet they are not given an explicit focus in an enquiry using SSM as they are not made explicit in the models and are, therefore, not available for debate. Some consideration is given to rules in the environmental constraints but environmental constraints are defined in the methodology as constraints that are taken as imposed and not open to debate. In the root definition given above, three constraints are placed on the transformation of the provision of courses; the courses must be valuable, efficient and viable, and BTEC approved. Similarly, two constraints are placed on students; they must be suitably qualified and they must be interested. The constraints are related to the transformation statement because they qualify the transformation. The transformation on courses, ‘unprovided courses provided courses’ could be rewritten as ‘unprovided, valuable, BTEC approved, efficient and viable courses provided courses’. The constraints affect the worldview, therefore if they are not made explicit in the model, an appreciation of the view expressed is limited. For example, the major football codes in Australia (Rugby League, Rugby Union, Australian Rules, and Soccer) are distinguishable by their rules which change over time. The rules affect aspects of the game such as how fast the game is, how safe it is for players, how large the scores are, and how skilful the game. Therefore, it is important to discuss constraints in relation to what is trying to be achieved (transformation).

Discussing and debating these constraints in isolation to the transformation or purpose or discussing and debating the purpose in isolation to the constraints does not necessarily lead to a coherent whole. Mills and Murgatroyd (1991) argue that rules are social creations; they distinguish one organization from another; and they can provide a way of appreciating a situation as they can be seen as a root metaphor that is not as removed from organizational life as the metaphors of ‘machine’ and ‘organism’ used by Morgan (1986). Yet, the functional decomposition strategy used in SSM does not allow a focus on constraints in the model. An underlying concern of our work is that, in using SSM to enquire about organizations, there is a need to explore the relationship between purpose (transformation) and constraints (often expressed in terms of rules). The contemporary modelling process used in SSM, however, does not allow analysts to make explicit the interaction of the two elements through the structure of the model. It is this concern that has led to the formulation of Decision-Variable Partitioning (DVP).

## Decision-Variable Partitioning (DVP)

DVP (Ledington & Ledington, 1997) is an approach to manage complex situations using a systems framework. It facilitates the partitioning of systems into subsystems in such a way that it allows a focus on a part of the problem in relative isolation to other parts while maintaining a focus on the whole (each transformation).

The argument presented in this paper is that decision variables have meaning and can provide a basis for conceptualising activities required to carry out transformations. An interation (looping) decision variable has meaning because it represents a transformation. In the root definition given above, ‘for each unprovided course <sub>→</sub> provided course’ is a looping decision variable representing the transformation. The selection decision variable has meaning because it represents a constraint governing a transformation. Again, using the root definition given above, ‘if BTEC approved’ is a constraint upon the transformation of courses. Courses will only be provided if BTEC approved. The process of producing models using DVP results in a decision tree.

Figure 1 shows a systems model using DVP that is developed from the root definition given above with the primary transformation assumed to be the provision of courses. The rectangular boxes represent a subsystem to handle all activities (to transform the focus) in response to the state of the decision variable. That is, all responses (to achieve the transformation) to each state of a selection or iteration variable are kept in one subsystem. The ellipses represent the activities that are placed at the end of each branch of the tree. At each level in the decomposition, a subsystem is added that contains at least one activity to determine the state of the decision variable on that level. For example, the activity ‘determine if approved’ determines the state of the decision variable on that level. The subsystem containing this activity represents all activities in response to the state of the previous decision variable, ‘for each unprovided course’ prior to going into the state of the next decision variable, ‘if viable’, therefore, this subsystem may contain other activities that are needed that do not depend on viability. The ‘determine’ activities correspond to the ‘appreciate activities of an SSM conceptual model. Once the decomposition is derived, the decision tree can be used as the basis for determining activities and these activities, represented by ellipses, can be added at the bottom of each node of the decision tree. For example, all activities that are necessary to transform each student from less skills and knowledge to more skills and knowledge (if qualified and interested) through the provision of courses would be placed at the end of the tree in the subsystem ‘if interested’. Because students is plural in the root definition, a question arises ‘does the transformation from less skills and knowledge to more skills and knowledge relate to each student (as indicated in the DVP model) or group of students?’ That is, should there be another iteration level in the decomposition for each group of students between the primary and secondary transformation? This question would have to be clarified as they mean different things.

![](/api/attachments/EU3VXVG9/fulltext/images/64befbba1878baf9f61649e3c0ca288ebc858e17c5282bd55f7b8818774ed9dd.jpg)  
Figure 1 Decision-variable partitioning example based on root definition (Wood-Harper et al, 1985, p 57).

From this model, it can be seen that prioritising the transformations is important. In this example, students can only be transformed to more skills and knowledge through the pre-arranged courses because all activities are limited to converting the primary transformation of unprovided courses to provided courses. Changing the world-view underlying this particular representation to a focus on students (switching the transformations) would allow more flexibility in how students could be transformed from less skills and knowledge to more skills and knowledge, with courses being only one possible method for achieving this end. The model clearly highlights the prioritisation of transformations embedded in this worldview and the constraints under which the transformations would be carried out and can suggest and lead to a consideration of alternate world-views.

The constraints on a transformation can be of two forms; exclusive or discriminatory. Exclusive constraints state the conditions under which the transformation will be carried out or abandoned. In the above example, all the constraints appear to be exclusive. Courses will only be provided if BTEC approved or student knowledge will only be increased if students are qualified. These constraints dictate whether the activities to transform the focus will be carried out or not.

Discriminatory constraints determine which activities will be carried out depending on the state of the constraint. An example would be if different types of students were treated differently. One might wish to distinguish between, and create different activities for, parttime and full-time students, for example. Discriminatory constraints would not determine whether the transformation would be carried out or not but rather would distinguish the activities to carry out the transformation.

A DVP model can be developed by using the following process:

1. Identify the transformations deemed relevant.

2. Prioritise the transformations.

3. Determine the constraints for each transformation.

4. Construct the initial structure showing each transformation as an interation variable in order of priority and each constraint as a selection variable.

5. Add a subsystem at each level of the structure to contain at least one activity to determine the state of the decision variable on that level and the activities specified in the root definition.

6. To the end of each branch of the tree, add the operational activities.

While the process of developing the model is portrayed as a linear process, it is more likely to be iterative. The process of building and modifying the model is essentially a social process of formalising a conceptualisation and will involve discussion and debate. Once the transformations have been specified and prioritised and the constraints determined for a particular worldview, the drawing of the structure of the model could be automated. The structure can then be used to facilitate adding the activities.

A recent study by Ledington and Donaldson (1997) found that many people who claimed to be SSM users did not use the core activities of SSM; that is, the construction of the models and the comparison with the situation. Furthermore, we have often encountered students who have difficulty drawing the conceptual models. Automating the process of drawing the structure of the models from a list of prioritised transformations and constraints may alleviate some of the difficulties. While the DVP model shown in Figure 1 reflects systems notations in that it contains system/subsystem representations, initial work with students indicates that they still find this model difficult to understand. An alternative model that is showing some promise is shown in Figure 2 which is more like a decision tree than a system representation. Work is continuing in this area to refine the model.

This section has presented an alternative systems decomposition strategy to functional decomposition and argued that DVP allows more information to be included in the model by making explicit the transformations and constraints upon the transformations as well as the activities. SSM activity models that use functional decomposition do not allow for multiple transformations to be made explicit and focused upon, nor do they allow for the constraints upon each transformation to be considered. Yet, it has been argued that both the prioritising of transformations and the rules governing the transformations are social constructions and should be made explicit to enable debate. Another distinguishing feature of the DVP model is that the control structure (the decision states) is built into the activity model rather than being shown as a separate subsystem as in the conventional model.

Many accounts of successful SSM studies can be found in the literature, (see for example: Checkland & Scholes, 1990; Davies & Ledington, 1991). Therefore, the question raised in this study is ‘can the process be improved by the use of an alternate systems representation?’ The next section explores this question by comparing the DVP models with SSM conceptual models produced in an SSM action research project conducted by a master’s student in a large government department.

## A comparison of modelling approaches

In this section of the paper, the results of using both the conventional functional modelling approach and the DVP modelling approach are presented. The approach adopted in this study is to compare a conventionallyproduced and a DVP-based model derived from the same root definition, as well as collecting and comparing the insights gained from the modelling processes involved. The study was conducted in conjunction with a live SSM project that is concerned with problems associated with the provision of information technology support services within a large public service organization.

The root definition and conceptual model illustrated in Figure 3 was produced by an experienced SSM modeller (the supervisor) as part of the main case study. The SSM modeller has fifteen years experience teaching SSM and using SSM in action-based research. The modeller was asked to provide a record of any insights gained from the modelling process. A DVP model, Figure 4, was produced independently by a different modeller without knowing the insights produced by the first modeller, and again the insights produced in the DVP-based modelling process were recorded. The models produced and the insights recorded are compared in order to assess the similarities and differences between the two approaches.

## DVP modeller’s reflections

The DVP model was produced by working through each step of the process (as defined in the previous section)

## 1. Identify the transformations deemed relevant

Some difficulty arose in trying to determine the primary focus. Is the primary focus on client, problem, or resolution? An initial reading of the root definition seemed to indicate that client was the focus because client is mentioned a number of times in the definition but, in fact, there is no transformation as such on client. Two possible transformations emerged:

![](/api/attachments/EU3VXVG9/fulltext/images/5d2ea7995d0cdf9c89466b1de477fe3494fa05b16fe39c0c3713291cb6425635.jpg)  
Figure 2 Decision-variable partitioning—decision tree example based on the root definition (Wood-Harper et al, 1985, p 57).

Unresolved client IT problems  Resolved client IT problems

Less beneficial client IT resolutions More beneficial client IT resolution

The attempt to find the focus leads to a number of issues and reflections.

• The transformation of less beneficial client IT resolutions to more beneficial client IT resolutions cannot be correct because there is nothing in the root definition to suggest that there are activities to improve resolutions. Is there a transformation on resolution? There must be one if a number of resolutions for each problem are considered because this would create the looping structure. Reflecting on the root definition, there could be two interpretations. One interpretation is that more than one resolution is considered for each problem. In this case, the resolutions would have to be prioritised and ‘beneficial’ would become a constraint on resolutions. This would lead to the transformation:

## Unprioritised resolution Prioritised resolution

The second interpretation would be to assume that only one resolution is considered, acted upon, and then if the resolution is not found to be beneficial, the problem would be considered unresolved and would go round the cycle again. This interpretation would be a ‘learn by doing’ system and ‘beneficial’ would be assessed after a resolution is enacted rather than being assessed prior to taking action as in the first interpretation.

The root definition contains ambiguities that make the SSM modelling process less rigorous.

• As there is no focus on client but rather on a client’s problem, the system can only respond to problems and cannot include, for example, any measures to prevent problems arising. This conceptual model reflects a reactive rather than proactive system. This observation did not jump out from the conceptual model but occurred when searching for the primary focus for the DVP model and searching for the transformation on client.

This insight suggests that another relevant system could be to explore a proactive system with the focus on client.

• While discussing the root definition for this relevant system, a question was raised about whether the transformation was on clients’ problems or a client’s problem. The master’s student responded that it did not really

Root Definition:

A Group Manager-owned system, manned by IT knowledgeable and customer focussed personnel which recognises, diagnoses, and takes rationally planned action to resolve IT related problems which affect end-user (clients) such that the client finds the resolution beneficial. The system operates under the constraints of resource availability, rapid technological change, and the limitations of the existing infrastructure.

![](/api/attachments/EU3VXVG9/fulltext/images/76d2b75ca3db49a5789b1dcaa14ea231cf897e93af2dadce8c8f53d842ae47b1.jpg)  
Figure 3 Root definition and SSM conceptual model used in the case study.

matter as they both meant the same thing. This is not the case; however, if a DVP model is constructed treating problems as a group ‘for each group of problems’ rather than ‘for each problem’. The DVP modeller would be forced to think about activities for each group of problems and could include activities such as the allocation of resources to solve the various problems. Being forced to specifically represent the focus using DVP and trying to attach activities to transform this focus forces the modeller to think about the implications of the stated transformation.

An experienced analyst may see the subtleties contained in the relevant systems; however, if more rigour can be attached to the modelling process then perhaps inexperi enced analysts may also benefit.

## 2. Prioritise the transformations

If it is assumed that there exists a transformation on resolutions then, logically, the primary focus would be on a problem, because problems would have to be identified before resolutions found.

3. Determine the constraints for each transformation The constraints described in this root definition are resource availability, rapid technological change, and the limitations of existing infrastructure. The following difficulties emerged while trying to attach the constraints to each transformation:

• Considering resource availability, the question arises as to whether this constraint attaches to the transformation on problems or the transformation on resolutions. Do resources constrain whether problems will be tackled or do they constrain whether a resolution will be considered or both? The answer to this question is not clear from the root definition.

DVP appears to be forcing more effort to understanding the meaning embedded in the root definition.

![](/api/attachments/EU3VXVG9/fulltext/images/32530e2dedc86aa0bf78882cba6dde85770cd1a9698121162b19c5f4e7d8970f.jpg)  
Figure 4 Decision-variable partitioning example based on the root definition shown in Figure 3.

• The constraints of rapid technological change, and limitations of existing infrastructure are even more difficult to understand and to model. How do you incorporate ‘if rapid technological change’ into a transformation on unresolved problems to resolved problems or the transformation on unprioritised resolutions to prioritised resolutions? It does not make sense to say that problems will be resolved if rapid technological change occurs or that solutions will be prioritised if rapid technological change occurs. This constraint cannot be incorporated into the DVP model because, as it is worded, it cannot relate to either transformation. The issue therefore, raised by this problem is whether the DVP model is limiting or whether the SSM conceptual model which contains a reference to this constraint is not logical. In the conceptual model, ‘know about changes in technology’ affects knowing possible actions and their consequences. Therefore, it appears to be an activity necessary to determine possible resolutions rather than a constraint on the transformations.

The third constraint is also difficult to model because the meaning is not clear. The DVP model cannot contain a constraint ‘if infrastructure’. The meaning of this constraint would have to be clarified. If an assumption is made that it means ‘if fit with existing infrastructure then again it is difficult to determine whether this constraint acts on problems to be considered or on the resolutions.

Either the constraints are not clearly thought about in relation to the transformations in the root definition or the meaning embedded in the root definition is ambiguous.

• As discriminatory constraints are usually not considered in SSM, there are no such constraints mentioned in the root definition. Are different types of client problems considered and treated differently? From personal past experience with IT support services, these discriminatory constraints can create problems. For example, should the managing director’s IT problem be given priority over an IT problem in the sales department which may cause the loss of sales?

Using DVP modelling would force the analyst to try to gain an understanding of the discriminatory constraints that may be relevant in a worldview.

## 4. and 5. Construct the initial structure and add the activities

The DVP model shown in Figure 4 assumes the two transformations on a problem and a resolution and assumes that the constraint ‘if resources available relates to the primary transformation on problem and the constraint ‘if fit with existing infrastructure’ relates to resolution. The rapid technological constraint could not be included.

## Conventional SSM modeller’s reflections

A number of points arose in the modelling and subsequent reflection.

• The model is client focused. It is the client who recognises that there is a problem initially and defines that the problem has been resolved eventually.

• I did not use measures of performance in the model (as I do not think they are usefully incorporated into the model). However, I was reflecting on the model and realised that it had no way of improving its performance (I then incorporated two dotted feedback relationships into the model but feel that these are inadequate). Such a system is faced by problems that it has to understand and resolve. It cannot leave a client with a problem. In one sense it should only be solving problems it has not met before, otherwise it has not really resolved the problem. This is a different definition of problem resolution, i.e., a client may be happy that a problem has been resolved but if the problem recurs, perhaps to someone else, then it surely has not been adequately resolved. Such a system has to learn at a sophisticated level and now I feel that there should be explicit activities to account for this. One view is that the management subsystem would fulfil this role, but I am not convinced by this argument which leaves the notion that two learning activities must occur—one to develop the operational capacity to solve complex problems and the other to learn to manage the system. (This again is an interesting thought that needs further attention!)

• I missed incorporating activities concerned with ensure an adequate supply of ‘IT knowledgeable and customer focused personnel’. This seems to be a blind spot with me!

• On reflection I think that the term ‘problem’ is constraining. It is too sanitised. The user faces a situation in which their normal business activity is disrupted (and which presumably they cannot resolve without technical assistance). It could be no more than a minor irritation, but it could amount to a crisis, or even a disaster. Perhaps models based upon a view of IT support as a form of ‘workflow’ crisis management might be worth exploring, e.g., pre-crisis activity, crisis resolution activity, and post-crisis activity, then some form of ‘workflow crisis management system’ might be relevant.

## Comparison of using the two approaches

The systematic application of the DVP process raised consideration of a number of ambiguities and inconsistencies in the root definition. These problems are not reflected in the conventional modelling process and either have not been noticed or have been resolved implicitly by the modeller. The issue of what is meant by a ‘resolution’ and how the system generates better resolutions emerges explicitly from the DVP process and is also part of the concerns of the conventional modeller, although in this latter case this seems to emerge from the modeller’s experience rather than as a consequence of the requirements of the modelling process. The conventional modeller fails to recognise the issues concerning the incorporation of constraints into the model. The DVP process provides a level of rigour in modelling, and of critical analysis of the root definition and model that transcends the experience of the other modeller. In this sense, the use of DVP out-performs the conventional approach.

The activities incorporated into both of the models are consistent with each other, but the DVP model incorporates two classes of model element that the conventional model does not. The DVP model explicitly incorporates the activities that are needed when a condition is not met and forces consideration about the meaning of the constraint; that is, is it a discriminatory or exclusive constraint? The model explicitly requires that the core decision activities themselves are represented. The DVP model creates a two-level representation of the human activity system involving primarily a decision structure that represents a particular world-view; that is, the structure is meaningful and within this structure are embedded activity clusters. By comparison, the conventional model is presented as a single activity cluster. The DVP model therefore offers a richer framework for use in the comparison process of SSM. It may well be that in a particular real world context problems may arise because of weaknesses in handling the non-positive areas of activity. The DVP model provides the potential to identify such weaknesses in a situation whereas the conventional model does not.

## Conclusion

In this paper, we have argued the need for alternative modelling approaches within SSM, have presented an approach called Decision-Variable Partitioning, and have provided a comparative example of SSM modelling using this approach.

A model within SSM is of value only to the extent that it provides a mechanism for focusing attention upon aspects of the situation. It is only in the context of a particular situation at a particular time that one model may be regarded as more useful, valuable, or insightful than another. It is always open to analysts using SSM to choose other definitions and models. In the same sense, there is no intrinsic value attached to constructing a model in one way or another. There is no answer to the question of whether a DVP-based model is intrinsically better than a functional decomposition model. However, we have demonstrated that alternative modelling approaches, such as DVP, are possible within SSM and that their use creates different emphases and different areas of attention and insight. Users of SSM may now choose different modelling approaches and, in this sense, this research establishes a significant new direction for the development of SSM.

Having begun to establish that a choice of systems modelling approaches is possible within SSM, the research challenge is to make that choice an informed one. The SSM literature provides a range of broad strategies for applying the model and compare cycle within problem situations such as the distinction between primary task and issue-based models (Checkland, 1981), the system to use SSM (Checkland & Scholes, 1990), and different modes of use (Checkland & Scholes, 1990). These broad strategies, that have been developed from practical experience of applying SSM, provide users with informed choices for using SSM. Similarly, guidelines for choosing a modelling approach are required. To develop such guidelines requires more experience of applying DVP-based models and a greater understanding of the strengths and weaknesses of both DVP and conventionally-based models. Further, it provides new directions for considering the issues involved in training potential users of SSM and in considering the development of support tools. Work is also continuing on relating a DVP model to information systems requirements. Logically, the minimum but necessary data required to support the world-view depicted in a particular model must be to know the states of the decision variables. Which branch of the tree to follow must be known in order to know which activities to carry out.

Finally, one unexpected insight that has emerged during this research is the importance of the reflective learning process during model building. The rigour of the DVP formalism seemed to force a greater attention upon the terms used in the model giving them sharper definitions. In so doing, it forced the creation of previously unrecognised distinctions. In this process, the comparison is not between the model and the situation but rather between the meaning expressed in the root definition and the meaning expressed in the model. As the process unfolds and the meanings are sharpened, new possibilities for other meanings are generated.

While these are still early days for this new stream of research associated with SSM, the potential of DVP to provide a richer modelling environment has clearly been demonstrated.

## References

Avison DE and Wood-Harper AT (1990) Multiview: An Exploration in Information Systems Development. Blackwell, Oxford.

Boyle S (1995) An Investigation of Heuristics used in the Construction of Conceptual Models from Root Definitions in the Soft Systems Methodology. Masters Dissertation, Department of Computing, Swinburne University.

Checkland PB (1981) Systems Thinking, Systems Practice. Wiley, Chichester.

Checkland PB and Scholes J (1990) Soft Systems Methodology in Action. Wiley, Chichester.

Davies LJ and Ledington PWJ (1991) Information in Action: Soft Systems Methodology. Macmillan, Basingstoke.

DeMarco T (1978) Structured Analysis and System Specification. Yourdon Inc, New York.

Hirschheim R, Klein HK and Lyytinen K (1995) Information Systems Development and Data Modelling: Conceptual and Philosophi cal Foundations. Cambridge University Press, Cambridge.

Ledington J and Ledington PWJ (1997) Decision-Variable Par

titioning: A Strategy for Decomposing Complex Problems. In: Linking People, Nature, Business and Technology (Wollin A and Rickert K, Eds), University of Queensland, Gatton.

Ledington PWJ and Donaldson J (1997) Soft OR and Management Practice: A study of the adoption and use of Soft Systems Methodology. Journal of the Operational Research Society 48, 229–240.

Lewis PJ (1994) Information Systems Development. Pitman, London.

Mills AJ and Murgatroyd SJ (1991) Organizational Rules: A framework for understanding organizational action. Open University Press, Milton Keynes.

Morgan G (1986) Images of Organization. Sage, Newbury Park.

Stowell FA (1995) Information Systems Provision: The Contribution of Soft Systems Methodology. McGraw-Hill, London.

Wilson B (1984) Systems, Concepts, Methodologies and Applications. Wiley, Chichester.

Wood-Harper AT, Antill L and Avison DE (1985) Information Systems Definition: The Multiview Approach. Blackwell, Oxford.

## About the authors

Jeannie Ledington (previously Jeannie Donaldson) B.Econ., B.Com., MFM (University of Queensland) is completing doctoral studies on alternative modelling approaches in Soft Systems Methodology. She has held academic posts in information systems at the University of Queensland, Queensland University of Technology, and Griffith University.

Paul Ledington B.A., M.A., PhD (Lancaster) has been actively researching in the area of Soft Systems Methodology and its application in information systems inquiry for many years. He has held academic posts at the Royal Military College of Science (Cranfield), Lancaster University, the University of Queensland, and is Associate Professor and Head of School at Griffith University.
