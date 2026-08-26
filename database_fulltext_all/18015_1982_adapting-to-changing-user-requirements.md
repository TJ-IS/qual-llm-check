---
otero_id: 18015
otero_key: "ABFZZFB9"
title: "Adapting to changing user requirements"
authors: "Frank Land"
year: "1982"
journal: "Information & Management"
doi: "10.1016/0378-7206(82)90039-8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Adapting to Changing User Requirements \*

Frank Land

London School of Economics, Houghton Street, London WC2A 2AE, UK

Systems which have the capability of adapting to changing user requirements must be founded on accurate and perceptive models of the organisation in which they have to function. Design methods based on active user participation and the use of experimental and prototyping methods help to ensure accurate models. But because systems are expected to survive even when circumstances change, the designers have to have a view of what the future world will look like. A technique which helps to provide such a view is called "future analysis". However, even designs based on the best prediction technique cannot guarantee a fit between the currently designed system and future needs. Hence it is important to design systems with built-in flexibility. A number of methods have been developed which reduce the disruption caused by the amendment or even replacement of a system or system's component.

Keywords: Changing User Requirements, Technological Change, Forecasting Horizon, Planning Horizon, Participation, Prototypes, Real World Models, Future Analysis, Creeping Commitment, Formal Systems, Informal Systems.

## 1. Introduction

Information Systems have to operate in a turbulent, dynamic world. Despite the common view about people – that they are conservative, that they dislike innovation, and react adversely to the prospect of change – people as processors of information have a very high capacity to adapt to changing circumstances. Information systems based on manual processing have shown themselves to have a considerable degree of flexibility, and, where it has proved necessary, have adjusted rapidly to changing needs. Manual systems have also shown the capacity to evolve through time, but without the kind of disruption and high and costly use of resources observed when computer systems have been subjected to unforeseen changes.

Computer based systems are inherently less flexible. It follows from the way computers have to be programmed that any change which involves a change to the program requires an elaborate sequence of steps to be taken which can be time consuming, costly, and disruptive. Indeed some changes, even changes which appear trivial to the non-expert user, cannot be incorporated in the system without a substantial redesign of the computerised parts of the system. Hence, the standard model of a computer application postulates a systems or application life cycle.

![](/api/attachments/ABFZZFB9/fulltext/images/9e6d003d4083762a594c3be089e87ab2834cf88d3972012e34c5ee83151f11f5.jpg)

A project is conceived, requirements are analysed, feasibility is established, a series of design are conceived and embodied in specifications, hardware is selected, the system is constructed and tested and finally implemented. The new system operates until it no longer effectively meets the needs of the organisation, either because new technological opportunities have made the existing technology obsolete, or changing user requirements cannot be satisfied by the existing design. At that point a new system is required, a new system is conceived, and a new life cycle gets under way. Because the life cycle process is costly and disruptive, users and computer professionals have looked for methods:

1. of increasing the life of the system by building flexible, changeable software.

2. of replacing the life cycle approach of systems implementation by an evolutionary approach more akin to that applicable to manual systems.

3. which make the construction of systems less dependent on particular hardware, and which make it possible to transfer systems developed on one type of hardware to a different hardware.

4. of improving the designers model of the world in which the system will have to operate, by making it a more accurate representation of the real world.

5. which provide a systems planning strategy which enables the implemented system to more closely fit the real requirements as revealed when the system begins to be implemented.

6. of design and construction which so reduce the cost of these processes, that a system which no longer meets the needs of the organisation can be discarded and rapidly replaced by a new system. The life cycle model is changed to a model based on the concept of expendable, replaceable systems.

In this paper some observations are made on each of the above methods, but the main concentration will be on methods of improving the designers model of the world in which the system will have to operate. However before dealing with the various methods some observations are made on the life cycle model.

## 2. Time and the Life Cycle Model

The time taken to design, construct and implement a system will depend on the scale of the planned application and the resources available to implement the system. Even quite small systems require substantial time and resources, whilst the implementation of major systems may require a period measured in years. Time cycles ranging from eighteen months to five years are quite common for the period between the start of an information systems project and bringing it into operational use. Large scale systems, such as those found in public administration, or defence may take much longer that that, and implementation times exceeding ten years are not unknown.

The life cycle is illustrated by fig. 1 [19].

A major system may take 3 years to design, program, test and implement. After a further 5 years of systems operation it becomes apparent that the system no longer effectively meets the needs of the organisation, despite the fact that a great deal of resources have been devoted to maintain the system in an attempt to keep it viable. However it takes a further 2 years to develop a new system to replace the first system. The system which was conceived at time A therefore has to meet the requirements of the organisation not only as far as time B-3 years after the project was initiated-but also at time C-8 years after initiation-and at time D-10 years later. In other words, those who design the system must be capable of either foreseeing the needs of the organisation 10 years later, or of designing the system so flexibly that it can meet unforeseen needs for an operational life of 7 years (B→D).

![](/api/attachments/ABFZZFB9/fulltext/images/30451d5da2bbb0d1c8fa6b0c0ef1f3f5f605eafde1e549dfdcf8853a98ee7b5b.jpg)  
Fig. 1. Application life cycle.

A computer based system, unlike a manual system, is normally planned on the basis of an expected life span. The systems designers estimate the resources and time needed to develop and implement the application. Often the expected operational life of the system is determined by economic (or accounting) considerations rather than by technical or organisational factors. To recover the cost of development and to cover the costs of operating the system while providing an adequate return on the capital employed, the system has normally to have an operational life of several years. If it is expected to cost \$x to develop the system, and \$y per year to operate it, and the expected net annual return is \$z-\$y, then the life of the system has to be t years to return r, the required earning on capital invested, taking account of the cost of money and the rate of inflation.

If, as frequently happens, the development costs turn out higher than expected, and the tangible net benefit turns out to be somewhat below expectations, the hoped for life of the system is, without regard to technical or organisational factors, raised. For example, a well known large scale application had its life extended to seventeen years in order to provide reasonable looking annual returns to capital employed! In practice, there is little chance of the system in question surviving for anything like that time.

Because it is inherently impossible to build a completely flexible, completely portable system capable of coping with any change, the systems' planners have to define in some way the extent of change it is possible to accommodate. The further the planners look into the future, the more they are faced with uncertainty regarding the changes, and their potential impact on the system. At some time in the future, the uncertainty becomes so great that the systems designers cannot conceive of any design that can cope with the possible range of requirements at a permissible cost. This is the forecasting horizon.

In practice, the forecasting horizon will vary from organisation to organisation, and will be different for different applications. Some will be less affected by changes whether they stem from circumstances outside the organisation, or from changes within. The forecasting horizon may vary in different time periods or epochs. At times of rapid technological change, such as the current period with the widespread availability of micro-computers and computer communications technology, the forecasting horizon is closer to the present than at times of greater technological stability. A similar effect is noted in times of economic or political turbulence.

One determinant of the forecasting horizon is the expectation of changed requirements of the system together with uncertainty regarding these changes. The other important determinant is the extent to which the designer can build in flexibility At any time, the designer has only a certain number of techniques and tools available at reasonable cost. It is generally cheaper to build a dedicated, highly specific system than a generalised, flexible one.

It is however worth noting that a more general purchased application package may be cheaper for an individual user than a dedicated tailor-made system. The higher costs of producing the generalised package is spread over a number of purchasers.

Because of limitations in the tools and techniques, it is not possible to design systems which provide infinite flexibility. This is illustrated in Fig. 2.

Here line AB represents the technical possibilities of building flexibility into a system. Above the line it is not possible to provide further flexibility, at least at reasonable cost. The line is shown as rising because it can be expected that such techniques will be improved, or be reduced in cost even for systems designed at an earlier time.

![](/api/attachments/ABFZZFB9/fulltext/images/f051335d5c591d5271d8e36af0e5aff290ff21befeb7276a2ecf28cac4aca985.jpg)  
Fig. 2. Planned life span of the system in years.

The line CD represents the extent to which flexibility has to be built into a particular system to meet unforeseen changes in requirements. The system is one which exists in a changeable, uncertain environment. Given the available technical/cost possibilities, the system runs out of flexibility options in just under 3 years. For this application, the forecasting horizon is less than three years beyond the present.

The line EF represents the amount of flexibility needed to achieve different life spans for an application existing in a much more stable, predictable environment. The forecasting horizon for the system lies beyond 7 years, and is therefore not an important factor in determining the planning horizon for the system.

For all applications, the systems designers have to decide on the life span targeted for, and the extent to which the system should have flexibility. As a general rule, the planning horizon should fall within the forecasting horizon.

## 3. The Designers Model of the Real World

A systems designer designing a computer based information system, has to provide the systems' constructors—the programmers—with a model of the system they must implement. The model is embodied in the systems specifications which depict the systems designers understanding of the functional activities, data structures, information flows, and decision processes. By implication, it also mirrors the analysts conception of how the users behave and will behave given the new system. To enable the programmers and those responsible for the planning of the manual procedures to develop an efficient system, the model is supported with a range of statistical information-activity rates, volumes, distributions of peaks and troughs, seasonal trends, response requirements etc. The model then is made up of assumptions about behaviour, statistical facts, and information about the organisation derived from the process of systems analysis.

If the analysis process yields accurate data, (i.e., data which portrays the state of the real world with precision), the designer has a good chance of constructing a realistic model of the organisation and its requirements—at least, as it is at the time the analysis was carried out. But even the best model based on an analysis of the state of the organisation as it is now and incorporating the view of the future as seen by the management at this point of time, loses precision when it has to predict the state of the organisation in two or three years and even more so when the model is expected to provide the basis for the construction of a system which has to survive for many years.

The first task is to adopt better methods for modelling the present set of user requirements. The standard methods for creating the model are based on four common techniques of analysis:

i) Interviewing members of the user community to establish the requirements of the new system, and the "facts" about the existing system.

ii) Carrying out surveys by questionnaire to establish the same information as by interview.

iii) Observing the system in operation to find out how it works and to measure specific attributes of the system, such as the size and duration of queues at peak times.

iv) studying documentation and procedure manuals relating to the system in order to discover the formal rules which govern the operations of the system.

Using these techniques, the analyst/designer builds up a picture of the system in present use, and defines the requirements for the operation of the future system. Most systems analysts recognise that at least some members of the user community are not totally neutral with regard to replacement of the existing system with a new one-some may be expected to resist change, whilst others may desire change simply because it may increase their own power or status. Whatever bias they have is bound to colour their responses to the analysis process. Hence good analysts attempt to validate their model by cross checking, for example, by interviewing more members of the user community and using observation as a check on responses to surveys or interviews.

But a major hidden assumption of the conventional analysis process is that the analyst is neutral. Studies by Hedberg in Sweden and Mumford in the U.K. [14] have shown that this is not so. They found that many professional D.P. people have beliefs and values which significantly affect the way they set about the analysis process, which distort their model of what the real world is like, and which influences the designs they prefer. The studies show that systems analysts tend to think of organisations and of information systems in terms of scientific rationality, and in terms of engineering principles. They tend to describe an information system as an information providing machine (see for example the extensive literature on MIS), and think therefore that improvements to the machine can best be achieved by the application of further technology. As a result they tend to neglect the social and behavioural factors which in practice are often most important in distinguishing between effective and less effective organisations or systems.

Checkland [6] defines such systems as "Human Activity Systems", and has developed a methodology of analysis and design based on the recognition that the different participants working within or in association with the system each view the system from a different perspective and as a result have a different understanding of the system and different expectations and objectives. Sir Geoffrey Vickers [31] vividly describes the different perspectives when he describes a school as a system for educating children as viewed from the perspective of a teacher, but as a system for generating sewage when viewed from the perspective of a sanitary engineer.

Dew and Gee [10] showed in a study of the way managers described existing management information systems that there was a very wide divergence between different managers of the same organisation as to the purpose of the system. Middle managers tended to believe that a budgetary control systems designed to give them information on budget variances in order for them to take action had been designed to give more senior management control over them. Senior management tended to assume that the function of the system was to help middle management take action. Even amongst managers of the same level there were wide divergences in ranking the most important attributes of the system.

Argyris and Schon [1] in the course of comparing managers' statements relating to their activities, with observed behaviour of the same managers, found wide discrepancies. Managers may say that they take action on the basis of an 'espoused' decision process with the help of specified information. In practice, they take decisions in a very different way, using perhaps different information. The implications for systems analyst are far reaching. To the extent that the analyst's model of real behaviour and real requirements is based on what the user tells, the research of Argyris demonstrates that the basis is inadequate and can be very misleading. Unfortunately, the analyst is not helped a great deal by his back-up technique of observation because it has been shown—the 'Hawthorn effect'—that where the respondent is aware of being observed, normal behaviour is modified for the period of observation.

The analyst faces a further difficulty, revealed by recent research. All organisations function on the basis of a mixture of formalised systems, with defined relationships and roles, specified rules and regulations, clear boundaries and clearly demarcated responsibilities, systematised predictable information sources, and informal systems, with loose relationships and structures, varied often unexpected information sources, informal groupings and alliances and ad hoc processes. The rational scientific ideology, prevalent amongst systems analysts, tends to drive them to reject the informal system in favour of the formal and this attitude is strengthened by the fact that the technology, which is their stock-in-trade, can only cope with systems based on rules. As a result systems designed for computers tend to strip away the informal element in systems and retain only the formalisable, programmable aspects.

Earl and Hopwood [11] and Mintzberg [21] report on research findings which suggest that organisations which rely on a significant level of informal systems, out-perform organisations which have attempted to replace the informal by formal. These findings are supported by studies carried out by Burke and George [5] on a large sample of Canadian managers, which indicated that where managers have the possibility of using a computer-based MIS, they tended to prefer to use one of their subordinates as their information source. Any model of user requirements has to take into account the need to preserve the informal element in information systems.

The single, most widely noted problem area identified by surveys which have attempted to find out the extent to which computer-based information systems are regarded as successful by users and DP personnel, is the problem of communication between the user and the DP specialist. An example of such a study is one carried out by the British Computer Society in 1978 [3]. There are many reasons for communication difficulties [18] and some have been referred to above. The most important reasons are:

1) The different ideologies and perspectives of the different interests involved in a systems study. This problem is made worse by the different languages which different professions have developed for communication amongst themselves. This can cause wide variations in interpretations and ultimately distorted models.

2) The uncertainty, on the part of the user, regarding the way the designer operates, and hence what information the designer will need. Often this results in misplaced emphasis and omission of details which are important to the designer but irrelevant or trivial for the user.

3) Uncertainty on the part of the users of the impact the final system will have on their individual roles in the organisation and on them personally. They may doubt their ability to cope with the new system, or fear redundancy, or that their jobs may be deskilled or routinised. These fears can attack managers as well as lower level employees. This can result in a defensive attitude and a deliberate withholding of information from the analyst. Users develop a range of counter-implementation strategies designed to preserve the status quo. Keen [16], outlines the 'games' users play in their attempt to inhibit (or subvert) change. But the most widespread strategy for protecting the user from having to cope with the unknown new system, is the development of unofficial, informal systems.

4) The observation that the user operates with informal systems and that the formal procedure of the existing systems have been overtaken by less formal (but often more effective) unauthorised procedures. Many users will be reluctant to tell enquiring analysts the way they actually work because the analyst is regarded as a representative of authority. The difference between espoused systems and systems in action have also been noted above.

5) The fact that those who are involved in the analysis process-DP specialists and users-are often not aware of strategic decisions made by senior management which could have an important bearing on the workability of the system. Corporate planning is often separated from information systems planning and senior management themselves are not necessarily aware that their corporate decisions are relevant to the design of the information processing system, and for reasons of security and confidentiality, do not make even senior subordinate managers privy to all decisions.

6) The problem facing both users and analyst/designers that new systems almost certainly include innovations, for example, with respect to management reports, and neither can predict the managers response to the new style of report. In any case, different managers may respond very differently to the same report, and whilst one manager can become more effective, another manager equally effective with the old system, will find the new system less useful. Conjectures about peoples' behaviour are no substitute for knowledge and in the case of innovating systems such knowledge is not ordinarily available.

## 4. Improving the Designer's Model of the Real World

The best DP practitioners are aware of the above problems referred to above, and have developed their own methods of analysis to ensure their designs are based on better models of the real world. But many systems fail to yield expected benefits or may even have to be abandoned long before the end of their expected life span because the designer's model was unrealistic and the communication barrier's made it difficult for users and DP professionals to recognise the defects in the model. The fact that the designer has produced a comprehensive specification and that the user has 'signed off' the specification after due study, is not a guarantee that the designer has understood the user's needs, or the user, the designer's specification. There is a need therefore for new approaches to systems analysis and design which enable the designer to create more accurate, more perceptive models of the real world as it is at the time the analysis is performed, and which permit the designer to more reliably model the future.

One such approach is that of Peter Checkland, working in the Lancaster University Systems Department [6]. In the methodology, developed by Checkland, the analyst first searches for alternative 'root' definitions of the system subjected to analysis. The alternative definitions are derived from the different viewpoints of those who have an interest in the system. On the basis of the root definition conceptual models are created which define the activities necessary for each view of the system to work. The analyst compares the models with each other and with an analysis of what actually exists. Finally, the analyst confronts the different interest groups with their different models and the implication of the differences, and from the resulting debate, attempts to get an agreed, or at least clarified analysis of the situation, and the beginnings of a specification of desirable and feasible changes.

Checkland, his colleagues, and students have applied the methodology in a number of situations, and progress of the work is reported in the Journal of Applied Systems Analysis (Vol. 3, No. 2, pages 87–117, 137–148, Vol. 4, No. 1, pages

40–51, Vol. 5, No. 1, pages 75–83, Vol. 6, pages 51–68, Vol. 7, pages 123–130, Vol. 8, pages 101–114). Particular attention is focussed in this paper on the socio-technical approach and associated with it, with participative methods. Like the Checkland method described above, the socio-technical method explicitly recognises the importance of the different interest groups concerned with one system, and the method seeks to discover the social, technical, economic and organisational objectives as perceived by the different groups.

However the socio-technical approach applied as part of the conventional process of analysis and design carried out by professional specialists cannot overcome some of the major communication problems, vis-a-vis the user, described earlier. These problems can be eliminated or at least reduced, if, in association with the socio-technical approach, members of the user community at all levels are involved in the analysis, design, evaluation, and implementation of the computer based system, and if they are allowed to take the main responsibility for the system.

Participation in, and responsibility for design and implementation can result in the elimination or reduction of the problems listed above:

1) By setting up a design team which contains representatives of all the major interest groups, it becomes possible for the different ideologies and perspectives of the participants to be made explicit, and for the different members of the group to learn from each others different viewpoints. The whole process is enriched by the interaction of the group, and results in a far more sensitive and perceptive model of the world.

2) In order to participate in the design process the user has to learn and become familiar with design methods. As a result the user is no longer uncertain. The users who are not members of the design team, (and it is rare for more than a small proportion of users to be directly concerned with design) must be given the opportunity to learn how the process is carried out from their peers on the design team.

3) The user is concerned with the setting of objectives for the system, and is involved in the detailed design work, and the planned redesign of jobs, and work organisation called for by the new system. As a result, the uncertainty as to the impact of the system on the user is reduced, as are the defensive strategies thought up by users to thwart the conventional systems designer. Once again the users who participate in the design team have the responsibility to communicate with their colleagues outside the design team. In the conventional design process the designer concentrates his attention on the computer part of the system, and though the new design may change the tasks users have to perform, little attempt is made to change the way the work is organised. With the participation of users in the design team, more attention is paid to work organisation, in an effort to achieve both the efficiency and social goals set for the system.

4) If the users are directly responsible for the design of their own system, they will be less concerned with covering up the use of non-standard procedures and unauthorised short cuts.

5) The problem of senior management security is more difficult to solve. One technique is to involve senior management in a steering group for the new project (the steering group has particular responsibility for setting the global objectives of the system and defines the resources available for the project) and the constraints to which the design team have to work. A further role of the group is to act as umpire in the case of conflicts or unresolvable problems in the design team. If senior management are prepared to involve themselves in this way, they become more aware of the possible impact on the system of their strategic decisions.

6) The problem of predicting future behaviour in the context of an innovative information system can only be reduced if the systems design process is seen as experimental. But the users can play an important part in designing and participating in the experiments. The socio-technical approach was first developed at the Tavistock Institute for Human Relations which saw that a new technology could only be effectively introduced into industry if the designer attempted to integrate the social requirements of those who have to work with the new technology with the economic and technical requirements of the management.

The ideas at the Tavistock in the 1950's have been adopted in many parts of the world, and more recently have begun to be used for the design and implementation of DP systems. The socio-technical method has been applied to as number of computer systems projects in the USA, for example, by Taylor [30], in Italy by De Maio [9] and his team at the Polytechnico of Milan, in the U.K. by Mumford and her colleagues [22], and in Germany by the BIFOA organisation [17].

The importance of the socio-technical method is that it includes the analysis of social requirements in the process of understanding an organisation and its requirements, thus ensuring that the analyst's model has a better chance of reflecting the real needs of the organisation. At the same time it provides techniques for carrying out the analysis of social requirements, thus giving the designer the opportunity of building a system which addresses itself to meeting social as well as efficiency and economic objectives. Systems which result from such an analysis are likely to be more robust.

Participation techniques are being employed more frequently in the design of computer based systems, and a number of interesting cases have been reported, [2,17,22,28], from many parts of the world. All these examples encourage the belief that despite problems and difficulties the socio-technical approach combined with extensive user participation plays an important role in the design and implementation of better systems. Nevertheless the approach can only produce satisfactory results if the right tools are available. Such tools and their development are described in several papers, such as [7,9,19].

The approaches discussed above provide a sound starting point for the design of systems capable of a long and effective life. The kind of model of an organisation's requirements derived from these approaches is likely to yield a design which incorporates more real knowledge of all needs, including the elusive social needs, and as a result has a better chance of receiving approval and support from all members of the user community, than systems based on the more conventional methods of systems development. But to design systems capable of meeting a wide variety of changing user needs, the designer has to employ other techniques.

## 5. Changing User Requirements

All planning activities face the problem that that which is being planned lies in the future, and hence is subject to uncertainty. How can the planner produce a design which is not made irrelevant or obsolete by unforeseen changes in circumstances?

One approach is for the planner to attempt to predict the changes which could occur over the expected life of the system, and which could have an impact on the system in question. Such ‘future analysis’ is discussed in more detail in the appendix. In this analysis the design team, aided by coopted ‘experts’, and using a variety of techniques ranging from ‘Delphi’ methods and ‘brainstorming’, to statistical analysis and simulation modelling, identity the main areas in which change is possible.

One important feature of the analysis is that it tests what the impact of a conceivable change in requirements could have on the system. The designer then has the choice of modifying the design to enable the system to cope with such a change, perhaps by allowing spare file space or by parameterising the relevant algorithm, or if the nature of possible changes is so inprecise that no design strategy can be envisaged which would enable the program to adapt, the designer may decide that the life span for which the program was originally designed has to be reduced.

"The extent of the future analysis would depend on the kind of system under consideration. If the system is central to the organisation's existence, and a failure could imperil the whole enterprise, the future analysis must be very detailed. In such projects as the Apollo moon shot, the analysis of all possible contingencies was very elaborate indeed" [18].

The principal outcome of the analysis is a list of systems features which are vulnerable to possible changes. This list gives the designer valuable information as to which aspects of the system have to be protected by making use of the many techniques now available for achieving flexibility. Such tools include modular construction, structured design, parameterisation, providing spare capacity, data dictionaries, data base management techniques, and table-look up methods. The problem of where flexibility is needed is illustrated by the following real example.

Two major airlines merged. Each had, at the time of the merger, comprehensive airline reservation systems, and in each system the flight number was used as the principal key for accessing the data base. The management of both airlines had stated categorically that a 3 digit flight number would be adequate for identifying all services for the foreseeable future. As a result the systems designer's had implemented a large suite of programs at each airline in which the 3 digit flight number was a major means of access to the files. Indeed one of the airlines used a 4 digit number in place of the flight number as an indicator that some special action was required. When the airlines merged, it became necessary to go to a 4 digit flight number. The change from a three digit flight number is conceptually trivial, and would have required only a little clerical effort to implement before the systems came onto the computer. However, the change to a four digit number with the computer system took a great deal of programming effort and time. The incident gave rise to considerable disruption, high costs, and consequent loss of confidence which might have been avoided in the kind of structured analysis set out in the appendix had been used.

But the designer has to be aware that building flexibility into systems can also be expensive, both in terms of design effort and operational performance. The designer is involved in a trade-off between the extra development and operational costs of designing a system which is adaptable and flexible—a very general system—or of designing a very specific system dedicated to the needs existing at the time of implementation, but which may be incapable of modification, and may have to be replaced if requirements change.

Podger [25] suggests a way in which the designer can be helped to determine where to build flexibility into the system. He points out, that any application area or system can be analysed, to discover in terms of those who are associated with the system, which features of the system tend to be deep rooted and invariant or subject only to slow change, and which features are less permanent and more likely to change. He uses an accounting system as an example. To the professional accountant the content and method of construction of the basic accounting reports—the balance sheet, the profit and loss account, the fundamental method of double entry book-keeping are invariant. On the other hand, he can readily envisage repeated changes in the layout and to some extent the content of the various transactions which give rise to the accounts. Podger suggests the construction of a map of the system showing the interconnections between the many activities of the system. He notes that those aspects of the system which are deep rooted in the structure of the application, tend to be highly connected but to have a low volume of activity, whilst those features which are less dependent on the principles which govern the organisation of the application area, and hence are more readily subject to change, are less connected but tend to have much higher activity rates. From this analysis he postelates that any system can be divided into:

1. An inner zone of basic values and principles, which it would take a revolution to change

2. An intermediate zone of general procedures which are subject to change but where the lead time between the change being formulated and required is quite long.

3. An outer zone of specific procedures, subject to more rapid and frequent change.

The convention model of the systems life cycle assumes that an analysis and feasibility stage precedes the detailed design stage and that this will be followed by a specification and agreement of the specification for the system. At that point the design of the system is often frozen. For a typical information system the stages preceding the design freeze take between 20% and 35% of the total time required for the development of the system. For between 65% and 80% of this time the design of the system is not to be modified, even though the "work" is changing all the time. In practice, even a frozen design gets modified if the system is seen to be becoming irrelevant to real requirements. Further, inconsistencies in design are discovered during the construction phase as a result of 'systems queries' (which as Waters [32] shows are often due to poor specification methods.)

An alternative to the conventional approach is one which seeks to defer design decisions up to the point at which further deferment would hazard the completion date for the system. Instead of having a single freeze date for the system, often quite early in the life cycle, some aspects of the system would remain open for re-design in the light of further information, almost up to the implementation data. Whilst this approach makes project control more difficult, it enables the system to be tailored more nearly to the requirements as they are at the time of implementation. Gosden [12], after many years of responsibility for implementing information systems, argues very strongly for a design philosophy based on “creeping commitment”, and of keeping design options open for as long as possible. One consequence of this approach is that throughout the development phase of a system the designer can continuously refine the model of the real world. In other words, creeping commitment implies an ongoing process of analysis and evaluation which is carried out in parallel with design and construction. In this way, the whole process of development is accompanied by a reduction in the designer’s uncertainty, and as the implementation date is reached, the level of uncertainty becomes very low.

Rosenhead [26,27] observed that many planning processes are based on an assumption of a particular and specified future. The designers rely on a single model of requirements for the future. At the same time, they design the system so it will operate at maximum efficiency with those requirements as a basis. If the future should turn out to be different, the system which has been tuned for one set of circumstances, may operate in a degraded manner with another set of circumstances. Rosenhead suggests that in order to build systems which are robust-systems which are not degraded by changing circumstances-the designer has to consider alternative futures. At each stage of the design process, the design chosen should be the one which can cope with the largest number of possible futures. He perceives a sequential design process through time, and as the project advances towards the implementation date, and knowledge increases, it becomes possible to reduce the number of futures the system has to be prepared for.

The approach recommended by Rosenhead sacrifices an optimising design (based on a single model of the future) for a design which can cope at a satisfactory level of performance with alternative models of the future. He defines the robustness of a design in terms of the number of alternative futures the design can cope with.

Uncertainty as to the effectiveness or relevance of the system being designed may be the result of the turbulent, dynamic environment into which the system must fit. It may also be due to the difficulty of predicting how those who will use or work with the system will behave when they are confronted with a system in action, rather than the system in words—the system as described in the specification. The only way the designer has of reducing the uncertainty regarding the users response to the system is to choose an experimental approach to systems design.

Brittan [4] describes a development strategy which replaces the conventional sequential development process by one of successively refined prototypes. The function of each prototype design is to test the assumptions on which a design is based in real world conditions. Brittan suggests that it is cheaper to build one or more prototypes of a system, which pays little regard to performance, than to build a finely tuned system which turns out to be unusable or only usable at a low level of effectiveness. The prototype development process, suggested Brittan, has the following phases:

1. Project proposal

2. Preliminary study

3. Full study

4. Systems specification

5. Systems construction

6. Implementation impact

7. Implementation

8. Monitor, review, evaluate

9. Project closure

The prototype approach is, however, only one of many possible experimental design strategies the designer can use. These include building simulation models of the system. For example, the LEGOL project of Stamper [8,15] can be used to simulate the operations of alternative designs of administrative or legislative rules, prior to the implementation of such rules. In this way inconsistencies and unforeseen consequences of the application of the rules can be identified. Simulation models can also be used as part of a strategy exploring behaviour by means of management type games. Hawgood and colleagues [13] describe the construction of a game COMSI-COMSA which models, for example, the existing inventory control system, and a proposed inventory control system. The game is played by the stock control management team using the two models and the results of each game are compared against criteria for efficient inventory control. This enables the designer to choose the inventory control system which produces the best results in the game.

Other experimental techniques, useful for the designer, include field experiments with new systems components or prototypes of such components, as for example, simulated exception reports, and attitude surveys by questionnaire. It is possible to test the effect of new systems on job satisfaction by the use of survey techniques supplemented by interviews, as described by Mumford and Weir [24].

The assumption underlying the life cycle model of an information system, is that (once implemented) the system adapts to changing user requirements by successive modifications until such time as the cost of maintenance and modification becomes so high that it is cheaper to replace the system. The model reflects the way systems were managed in the era when to take advantage of the economy of scale (Grosch's law), systems tended to be large, complex, integrated and centralised structures. Modern technology, with mini and micro computers and communication networks, favour distributed systems or systems using small dedicated processors. It is possible to identify two types of application which are supported by the trend in technology.

1. Application with a high content of generalised but unchanging processes. A good example of such an application is word processing. It is possible to specify a set of generalised word processing functions which are not likely to change significantly in the foreseeable future. The Podger model [25] helps to identify the generalisable invariant aspects of systems. Because such applications do not change a great deal, the problem of adapting to changing requirements is not severe. More and more of this kind of application will be implemented in the form of application packages.

2. Highly specific applications, subject to change. The cheap new micro computer technology suggests a possible change in approach to such systems. Instead of large, complex, integrated systems this type of application may be split into separate functions, corresponding to separate organisational units, with each function processed on a dedicated micro computer. The size of programs would be relatively small, corresponding to a few modules of a large modularised integrated system. Systems will adapt to changes in requirements not only by modification but also by replacement. Because each system is dedicated, the process of replacement will have a relatively small disruptive effect on the organisation as a whole, and because the systems are small, the replacement system will be relatively cheap. Even today it has been found that it is cheaper to replace programs written in a very high level language like APL than to modify them [20]. Newer developments using application generators such as NOMAD [29] enable prototypes to be generated quickly and cheaply. It becomes possible to discard parts of systems and replace them with new versions without causing great disruption to the system as a whole.

## 6. Conclusion

One of the vital problems facing the designer of computer-based information systems is that of ensuring that the system continues to meet the changing need of the user, and at the same time taking advantage of the opportunities offered by the rapid developments in the technology.

The analysis of the problem given above suggests a few guidelines for the designer:

1. Base the system on as accurate model of the real world as possible. To do this is becomes necessary to adopt methods of analysis, design and evaluation which involve a far higher degree of user participation than is customary in conventional systems analysis and design methods.

2. Use design methods which permit experimentation or prototyping in order to check how an innovative system might operate.

3. Attempt to identify those aspects of a system which are deeply embedded and hence change only slowly, and those aspects which are volatile and subject to frequent change.

4. Avoid commitment to a particular design too early. Practice as far as possible 'creeping commitment'.

5. Design systems which can cope at adequate level with a range of possible requirements scenarios, rather than choosing a design which optimises on the basis of a single (perhaps most probable) vision of the future.

6. Attempt to second guess the future by engaging in a systematic future analysis.

7. Build flexibility into the system through well known construction techniques which enable the system to be modified without major disruption.

8. Take advantage of trends in technology—both hardware and software—which enable the designer to develop small, dedicated replaceable systems.

These guidelines are not applicable to all situations. The designer has to choose those which are most relevant to the current application and fit with the organisational environment. Nevertheless, the use of the guidelines should help the designer to overcome the problem of adapting to changing user requirements.

## References

[1] C. Argyris and D. Schon, Theory in Practice: Increasing Professional Effectiveness (Jossey-Bon, San Francisco, 1974).

[2] P. Blokdijk, A Participative Approach to Systems Design, in: H. Lucas, F. Land, T. Lincoln, K. Supper, eds., The Information Systems Environment (North Holland Publ. Comp., Amsterdam, 1980).

[3] British Computer Society, User Requirements in Data Processing (Hayden & Son, London 1979).

[4] J. Brittan, Design for a Changing Environment, The Computer Journal, Vol. 31, No. 3, (Feb. 1980).

[5] F.E. Burke and R.E. George, How Top Executives Per-

ceive their Choices Among Information Sources for Decision, IFIP WG 8.2 Working Conference, The Information Systems Environment (June 1979).

[6] P. Checkland, Systems Thinking, Systems Practice (John Wiley, 1981).

[7] H. Clausen, Concepts and Experiences with Participative Design, in: N. Szyperski and E. Groschla, eds. Implementation of Computer-Based Information Systems (Sijthoff & Noordhoff, 1979).

[8] S. Cook and R.K. Stamper, LEGOL as a Tool for the Study of Bureaucracy, in: H. Lucas, F. Land, T. Lincoln, K. Supper, eds., The Information Systems Environment (North Holland Publ. Comp., Amsterdam, 1980).

[9] A. De Maio, Socio-Technical Methods for Information Systems Design, in: H. Lucas, F. Land, T. Lincoln, K. Supper, eds., The Information Systems Environment (North Holland Publ. Comp., Amsterdam, 1980).

[10] R.B. Dew and K.P. Gee, Management Control and Information (Macmillan, New York, 1973).

[11] M. Earl and A. Hopwood, From Management to Information Management, in: H. Lucas, F. Land, T. Lincoln, K. Supper, eds., The Information Systems Environment (North Holland Publ. Comp., Amsterdam, 1980).

[12] J.A. Gosden, Some Cautions in Large Scale Systems Design and Implementation, Information and Management, Vol. 2, No. 1, (Feb. 1979).

[13] J. Hawgood, F. Land, E. Mumford, C.M. Reddington, Evaluation and Management of Computer Based Systems: An Interdisciplinary Approach, in: Information Processing '71 (North Holland Publ. Comp., Amsterdam 1972).

[14] B. Hedberg and E. Mumford, The Design of Computer Based Systems: Man's Vision of Man as an Integral Part of the Systems Design Process, in: E. Mumford and H. Sackman, eds., Human Choice and Computers (North Holland Publ. Comp., Amsterdam, 1975.

[15] S. Jones and P. Mason, Programming the Law, in: H. Lucas, F. Land, T. Lincoln, K. Supper, eds., The Information Systems Environment, (North Holland Publ. Comp., Amsterdam, 1980).

[16] P.G.W. Keen, Information Systems and Organisational Change, Communications of the ACM, Vol. 24, No. 1, (Jan 1981).

[17] F. Kolf and H.J. Oppeland, A Design-Oriented Approach to Implementation Research: The Project PORG1, in: N. Szyperski and E. Groschla, eds., Design and Implementation of Computer-Based Information Systems (Sijthoff & Noordhoff, 1979).

[18] F. Land, User Requirements and Involvement in: User Friendly Systems, INFOTECH State of the Art Conference, (March 1979).

[19] F. Land, J. Hawgood, E. Mumford, Training the Systems Analyst of the 1980's: Four New Design Tools to Assist the Design Process in: H. Lucas, F. Land, T. Lincoln, K. Supper, eds., The Information Systems Environment (North Holland Publ. Comp., Amsterdam, 1980).

[20] E.R. McLean, The Use of APL for Production Applications: The Concept of Throwaway Code, in APL 76: Conference Proceedings (ACM 1976).

[21] M. Mintzberg, The Structure of Organisations (Prentice Hall, 1979).

[22] E. Mumford and D. Henshall, A Participative Approach to the Design of Computer Systems (Associated Business Press, 1978).

[23] E. Mumford, F. Land and J. Hawgood, A Participative Approach to the Design of Computer Systems, Impact of Science on Society, Vol. 28, No. 3 (1978).

[24] E. Mumford and M. Weir, Computer Systems in Work Design: The ETHICS Method, (Associated Business Press 1979).

[25] D.N. Podger, High Level Languages - A Basis for Participative Systems Design, in: N. Szyperski and E. Groschla, eds., Design and Implementation of Computer-Based Information Systems (Sijthoff & Noordhoff, 1979).

[26] J. Rosenhead, Planning under Uncertainty: 1. The Inflexibility of Methodologies, OR, The Journal of the Operational Research Society, Vol. 31, No. 3, (March 1980).

[27] J. Rosenhead, Planning under Uncertainty: 2. A Methodology for Robustness Analysis, OR, The Journal of the Operational Research Society, Vol. 31, No. 4, (April 1980).

[28] M. Saaksjarvi, Framework for Participative Systems Long-Range Planning, in: H. Lucas, F. Land, T. Lincoln, K. Supper, eds., The Information Systems Environment (North Holland Publ. Comp., Amsterdam, 1980).

[29] J. Sharkey, Systems Prototyping, Proceedings Management Conference, (Butler-Cox Foundation, Dec. 1981).

[30] J.C. Taylor, The Socio-Technical Approach to Work Design, in: K. Legge and E. Mumford, eds., Designing Organisations for Satisfaction and Efficiency (Gower Press, 1978),

[31] G. Vickers, Education in Systems Thinking. Journal of Applied Systems Analysis, Vol. 7, (April 1980).

[32] S.J. Waters, Towards Comprehensive Specifications, The Computer Journal, Vol. 22, No. 3, (Aug. 1979).

## Appendix

## Future Analysis

The analysis can be carried out in four stages. The first stage is concerned with an attempt to discover the kinds of change which may have an impact on the system under consideration. There are two broad classes of change the design team has to consider:

● Change which may affect the logic of the system

\- Changes in the 'traffic' the system has to cope with-changes in volumes, in frequencies, e.g., peaks, numbers of elements etc.

Changes also need to be classified as:

● Transient or short-lived

● Permanent or long-lived. Note should be taken of how frequently the changes occur over the lifetime of the system. Changes can be classified into a number of major categories, and the design team has to consider the system in relation to each of these categories. The major categories are:

## Changes in available technology

The technology referred to may be information-processing technology such as computers or communication equipment, or it may be technology which is embedded in the object system itself, such as, machine tools, production processors and so forth. Changes in technology can have a number of important effects on systems:

\- They may make the chosen technology obsolete – manufacturers will no longer provide maintenance or spares

● They may provide similar capabilities at very much lower costs

● They may make it possible to achieve systems goals which, with the chosen technology were out of reach.

In general, in times of very rapid technological change, the planning horizon for a system would shorten, and the technology chosen should, as far as possible, be modular and replaceable

## Changes in legal requirements:

Many aspects of company law, tax law, industrial relations law and now privacy laws, can have a profound effect on systems. A feature of changes required to meet new legislation is that the changes are mandatory and have to be implemented to a strict externally determined timetable. If the changes are not implemented in time, the organisation concerned may be subjected to legal sanctions. Changes in legal requirements can arise from domestic legislation, from international regulations such as those promulgated by the EEC, and from changes in administrative practice permitted under enabling legislation.

## Changes in economic and other environmental factors

Changes in the economic environment have an impact on the rate of growth or decline of organisations, and on their competitive place in the market. At the most trivial level such change can have a large effect on the level of activity and hence movement of messages through a system, and on the peak traffic the system may have to provide. At a more profound level it can lead to major changes in organisations, affecting the product range, the method of distribution, the policy on stockholding, wages policy and questions relating to the ownership of the enterprise itself. Some of the most profound effects on systems are seen when companies are taken over or merged.

Some systems are almost immune to the kind of change brought about by changing economic circumstances, e.g., the certain system in the U.K. But even such systems may have to be protected against some of the consequence of changing economic circumstances, such as strikes and other forms of industrial action.

Change in attitude, expectations, tastes, or in climates of opinion

Attitudes towards technology, and in particular to computer-based systems, have changed over the past decade and will continue to evolve. Attitudes towards the role of government, towards industrial democracy, towards devolution and many other features of life are constantly undergoing change. Some of these changes are short lived, others remain dominant for long periods. Some are localised, affecting only a particular group in a factory or a particular district in a country, others are competely general. Changes in expectations of what kind of work is rewarding or satisfactory can have an important impact on the effectiveness or even workability of a computer system.

Most of the change categories discussed so far concern themselves with changes over which the organisation has no control. Changes are triggered by events outside the organisation, and the organisation and the systems within it must respond at bet they can. But other categories are concerned with changes originating within the organisation itself and therefore to some extent controllable by the organisation.

## Changes within the organisation

All commercial and administrative organisations have a tendency to change their structure and style of management. It is sometimes suggested that these changes are cyclical from centralisation to decentralisation and back again, from authoritarian to democratic and back again. In reality organisations evolve under the pressure of external changes, and some of these will lead to an apparent cyclical effect. Thus the development of large mainframe computers coincided with movements towards centralised management; whilst the advent of the new mini- and micro-technology is paralleled by organisational philosophies of distributed responsibility. There is no doubt that changes in managerial personnel, in management techniques, in management style, in the control system and procedures, and in organisational structure can have large impacts on information systems. The effects are twofold:

● They may give rise to requests for systems changes to conform to the new pattern of requirements

\- They may affect the extent to which systems are perceived as successful: a system may be seen to be successful by the manager who was instrumental in having it implemented, but may be seen as a failure by the succeeding manager
The first task of the design team is to consider which category of change could be relevant to the systems under consideration.

The second task is to identify the people most likely to contribute knowledgeably to a discussion of future trends in each relevant category. For an evaluation of technical change the discussions with the design team could involve:

● Suppliers of computer equipment and software

\- Members of the computer or management service staff

Members of the organisation's research or R and D department

● Outside consultants

For consideration of the second category, legal changes, the important authorities to consult would include:

● The company secretary

● The chief accountant

● The personnel manager or industrial relations manager

● Officials of trade unions

\- The organisation's legal advisers

The third category, changes in the economic environment, is perhaps broadest, and in many ways, most difficult. Since many of the issues resulting from changes in economic circumstances are matters of highly confidential policy, for example, issues related to mergers or takeovers, it may be impossible to obtain information even where such information exists.

Those who should be involved in discussions may include:

● Top management representatives

● Corporate planners (if they exist)

● The chief accountant

● Marketing management

● Management services

● Outside consultancies

If the third category presents most difficulty, the fourth category changes, in attitudes and expectations, gives rise to the greatest uncertainty on the impact of such changes on the system itself. Those who may help to resolve the uncertainty include:

● Representatives of user departments

● The personnel or industrial relations manager

● Members of the management service staff

● Shop stewards and union officials

● Outside consultants.

The fifth category, changes within the organisation, involves a great variety of different change types. Discussion on such changes could therefore be structured by levels in the organisation. Strategic and control systems changes could involve:

● Top management representatives

● Heads of major departments

● Management services

● Senior trade-union officials

Consultants

Changes in unit operations should be discussed by:

● Departmental managers

\- Section heads

● Member of unit operation staff

● The personnel manager

● Shop stewards or union representatives

● Management services staff

It should be noted that the change categories are not independent. A change in one category can trigger changes in other categories. A change in the attitude of the population at large to industrial democracy can trigger legislation which will lead to organisational change and a consequent change in the expectations of the people working in the organisation. Hence the groups of people identified to help in forecasting the future should always be organised in such a way that such triggering effects could be traced

The third task is to select appropriate tools to help in the future analysis. Job satisfaction analysis can help to give indications of attitude and expectation changes. These can be supplemented by other surveys designed to elicit attitudinal data. The identification of unit operations help to define the areas where organisational changes may arise. Further techniques include statistical forecasting methods for extrapolating rates of growth or decline, changes in volumes, changes in frequencies: economic modelling of the economy and the organisation itself to identify economic trends, and simulation methods to test the effect of various changes on the performance of the organisation.

To summarise: stage one categorises the types of change which could have an impact on the system under consideration, identifies those who can help in discussing future trends, and select tools and techniques which can be used as an aid to forecasting.

In stage two, the design team has to try to assess the kind of future which the system under consideration will have to face. With respect to each change category, the team, with the aid of the selected discussants and the use of the available tools, has to attempt to answer the following questions:

1. What future changes are conceivable at the present time, and when may they occur?

2. What impact might such changes have on the system?

3. Can the probability of such changes occurring be estimated? If so, what are the probabilities?

Take the case of a coronary heart unit for which a new system is under consideration. In category one the team might consider changes in medical technology which could affect the system, and changes in computer technology. With regard to medical technology it may be regarded as conceivable that a drug will be perfected which enables coronary cases to be stabilised without hospitalisation. Such a drug may be available within the next ten years. Its impact on the system in question may be profound but the team regard the probability of such a drug being developed as quite low. Nevertheless, it suggests to the team that the planning horizon for the system should be limited in the first instance to no more than five years. In practice the team will have to explore a large range of possibilities. Of these only a few will be assessed as having an impact on the system, and therefore as affecting the design of the system.

In category three, economic and other environmental changes, the team may note that medical statistics indicate a constant rise in the rate of heart disease. This suggests that the system needs to be designed to cope with increasing loads, and in particular peak loads. On the other hand, the team may be aware of the possibility of future economic recession and cuts in public expenditure. How would the system cope with an increased demar for its services, but a reduced budget? If the team assesses the probability of such cuts being enforced in the future as high, is a design of the system possible which is less sensitive to cuts in expenditure?

In category five, the team discovers that a plan to merge two health authorities has been discussed and could be implemented within the next three years. Since both health authorities have systems for coping with coronary emergencies the team may decide that a new design objective has to be set up – ensuring as far as possible the systems of the two authorities remain compatible.

The chief methods employed in stage two are open-ended discussions between the design team and the people identified as capable of contributing to the discussion, using 'brain-storming' techniques, DELPHI methods, surveys, and a variety of forecasting and diagnostic tools. The extent of the future analysis would depend on the kind of system under consideration. If the system is central to the organisation's existence and a failure of the system could imperil the whole enterprise, the future analysis must be very detailed. In such projects as the Apollo moon shot, the analysis of all possible contingencies was very elaborate indeed.

The outcome of stage 2 is:

1. A target life-span for the system.

2. A revised list of design objectives.

3. A list of systems features which may need to have flexibility built into them.

4. A number of scenarios of the future which any design would have to cope with.

Up to this point the design team has concentrated on the kinds of change the system may face in the future. However, there is no way in which a team can make precise predictions about the future, and even with the best possible future analysis, unexpected events will test the system. If the system is to be robust, a further diagnostic procedure needs to be invoked. In stage 3 the design team has to systematically test the system under consideration to establish those systems features which are sensitive to any change in requirements, either in terms of the logic or the traffic. The team has to ask itself two questions:

1. What features of the system is sensitive to changed requirements or changes in traffic?

2. What will be the impact on the viability of the system as a whole if such changes occur?

The team has to consider the whole system—the computer sub-system and the manual sub-system.

The process of analysis has to be structured in such a way that all aspects of the system are covered and reviewed. To examine the computer sub-system the team has to analyse each facet of the proposed system and test its sensitivity to change. The process of examination is in some way analogous to a structured walkthrough of a program design. A method proposed for such an examination analyses the following facets for each system.

## List all identifiers

Check what would happen to the system if:

I. The range of identifiers were increased (or reduced)

2. An identifier changed its characteristics-for example, the identifier code changed from 6 to 7 digits, or the identifier had a check digit added to it.

If the proposed design can accommodate such changes with minimum delay or limited use of resources, there is no further problem. If the change cannot be accommodated the team has to check the consequences of delayed implementation and possible costs. If these prove to be unacceptably high, the proposed design may have to be modified to allow changes to be introduced. Note that the analysis is carried out independently of any assessment of the probabilities of such changes occurring.

Modification of the design usually involves the deployment of one of the many techniques which provide for flexibility in the system. In the case of changes of identifiers, these would include the possibility of leaving a redundant space for extending the identifier range or format, and the use of data dictionaries and indexes.

## List all input and output messages

Check what would happen to the system if:

1. The content of messages were to change.

2. The types of message were changed.

3. The frequency volume or expected response time of messages changed.

The analysis is carried out as for identifiers. Tools which may help to provide flexibility include the use of a modular design approach.

## List all algorithms or procedural rules

Check what would happen to the system if:

1. The logic of the rules were altered.

2. The rules were invoked more or less frequently.

3. The values (constants) used within the rules were changed.

The analysis is carried out as for identifiers. Flexibility can be enhanced by techniques such as modular design, use of look-up tables and parameterisation.

## List all files (or the database)

Check what would happen to the system if:

1. Access path to files were altered.

2. Content of files were altered.

3. Frequences of access to file or part of files were altered.

4. Distribution of variable elements in the file were changed.

The analysis is carried out as for identifiers. More flexibility may be provided by use of database management systems, the provision of redundant space, and the use of data dictionaries.

## List all identifier relationships

Check what would happen if:

1. New dependencies or relationships were required.

Data analysis techniques are used to see what the effect of such changes would be. Database management systems could help to provide more flexibility.

The design team has to carry out a similar analysis of the manual system. For each manual activity the team has to list each task and role and consider the effect of changes in the carrying out of the task, or changes in roles. In addition to changes in logic and 'traffic', the team has to consider the effects of changes in behavioural variables, such as attitudes and motivation, and external factors, such as the availability of alternative employment.

The design team has to see the extent to which the proposed system could be modified to make it less vulnerable if changes were to occur, however unexpected.

As a result of the stage 1 analysis the design team can list those elements of the proposed system which are most sensitive to change, and those elements where such changes would have the greatest impact on the organisation. A particular element in the system may be very difficult to change in response to a revised need, but the effect of not accommodating the need may be trivial as far as the organisation is concerned. It may, for example, be possible for a manual procedure to be set up to cope with a new requirement which cannot be implemented on the computer system. The important list is the one which identifies the elements which could have important consequences on the organisation if they cannot be amended quickly (or cheaply).

In stage 4 the design team considers the output from stages 2 and 3 in order to make recommendations regarding the system's planned life-cycle and to decide how much flexibility to build into the system, and which scenarios have to be coped with. To do this the team has to assess the possible damage to the organisation from failure to adapt to changes and compare this with the cost of building in flexibility. To a large extent, the tradeoff has to rely on the judgement of the design team, since it is difficult to quantify precisely the cost of building in flexibility or of evaluating the damage from failure to adapt.

One further point needs to be noted. The extent to which a system responds to changes is not only a function of the way the system is constructed but also the type of organisation in which the system operates. Some forms of organisation are inherently more capable of responding to change than others. This applies to the organisation responsible for the design implementation and operation of the information system and the organisation of the enterprise itself. In considering the question of life-span and flexibility, the design team has to be aware of any constraints imposed by the style of management and the structure of the organisation.
