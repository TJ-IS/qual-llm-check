---
otero_id: 24272
otero_key: "GV8G9GUP"
title: "Organizational requirements and the introduction of information technology in courtrooms: a case study"
authors: "David Poulson; Neil Waddell"
year: "1996"
journal: "Journal of Information Technology"
doi: "10.1080/026839696345441"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Organizational requirements and the introduction of information technology in courtrooms: a case study

DAVID POULSON and NEIL WADDELL

HUSAT Research Institute, Loughborough University of Technology, UK

Traditional methods of systems design have tended to concentrate on capturing functional requirements and from them develop a system that will provide users with a technical solution to a problem they may have. However, there is a growing understanding, with historical origins in sociotechnical systems theory, that technical solutions alone, regardless of how well designed, may not succeed fully unless there is a concomitant understanding of the organization into which the technical solution is to be introduced. Organizational requirements, therefore, should become considerations of equal importance to systems designers. The ESPRIT Project ORDIT (organizational requirements definition for information technology) has developed a methodology which identifies and operationalizes organizational requirements for IT systems. This paper presents a case study in which the ORDIT concepts are applied to the process of introducing an IT system into a courtroom.

## Introduction

The successful design and implementation of software-based systems is dependent on two interrelated factors. The first of these is to do with creating appropriate technical solutions which meet the needs of users, whilst the second is to do with creating appropriate social and organizational features which will endow the new system with coherence and relevance in the context of the organization receiving it (Eason, 1988). It is now something of a truism that technical systems often fail for non-technical reasons. This is because the latter of these two factors has been ignored. This paper will address the importance of, and ways of representing, social and organizational aspects of systems design. For the historical origins of sociotechnical systems theory, the reader is directed to Emery and Trist (1969); Rice (1958); and Trist et al. (1962).

Organizational requirements may be defined as those requirements that come out of a system being placed in a social context rather than those that derive from the functions to be performed or the task to be assisted. One of the difficulties in identifying organizational requirements is that the various structures, policies and objectives which make up the organization, and hence give rise to these requirements, are embedded within it and often, 'not open to direct observation or easy articulation' (Harker et al., 1993). What is needed, therefore, is an approach to systems design which ensures that communication between designers and users is supported to a degree hitherto not achieved. In order to achieve this, it is recognized that the methodology must provide both the framework and language needed to capture and convey these features.

An important point to note is that different types of innovation exert different types of pressure for change within the organization. Innovation may come about as a result of technological change or as a result of structural or organizational change. Each has its own particular characteristics and each must be addressed accordingly. The case study reported in this paper examines the effects of technological change, specifically the introduction of an evidence storage and retrieval system for use in a courtroom during a serious fraud trial.

## The ORDIT approach

Enterprise modelling (Dobson and McDermid, 1989) is the framework adopted by the ORDIT project. It can be used at a number of different levels of abstraction, and allows the analyst to reason about the human as well as the technical implications of developments. The concepts at each level of abstraction comprise three basic entities and the relationships between them. In each model the three entities are: an 'agent' type of entity, that is a primary manipulator of the state or structure of the system; an 'action' type of entity, that is an operation that changes the state of the system; and a 'resource' type of entity which enables the agent to perform the action. The generic concepts in an ORDIT enterprise model are depicted in Figure 1.

Within this framework it is argued that agent entities have functional relationships to the action entities, since the agent performs or monitors the actions. In addition the agent has an access relationship to the resources (e.g. information) used in actions. The agent may, for example, have rights to read that information or to modify it. Because ORDIT is particularly interested in organizational structure the relationships between agent entities is also included. These we term structural relationships, and this is one of the central concepts in ORDIT. Relationships between resources (resource models) and between actions (activity models) are of less interest to ORDIT and are covered in detail in more conventional systems design.

![](/api/attachments/GV8G9GUP/fulltext/images/5fdc087195b3d77c432178bafa7b5c164bea3ca17640213a07d271e28c0515c3.jpg)  
Figure 1 The generic concepts in an ORDIT enterprise model

## The basic modelling framework

ORDIT models are based on the underlying principle that one can reason about sociotechnical systems by using three basic building blocks: agents, actions and resources. It has been found useful to consider three levels of abstraction to talk about these elements, which have been labelled the activity level, the role level and the responsibility level (see Figure 2). These three levels of abstraction are of value to the ORDIT analyst as they allow the analyst to describe and reason about sociotechnical systems at different levels of detail.

The distinction between responsibilities, obligations and activities, and the relationship of activities to responsibilities through obligations, is the central tenet of the ORDIT modelling framework. This is based on the assumption that workers execute activities in order to discharge the obligations imposed on them by virtue of the responsibilities they hold. These obligations effectively describe a 'job' or, in ORDIT terminology a 'role', and are the link between responsibilities and the activities executed.

The distinction between responsibilities and obligations is apparent from the words we use: a responsibility is for something (a state of affairs) whereas an obligation is to do (or not to do) something that will change or maintain that state of affairs. Thus a set of obligations must be discharged in order to fulfil a responsibility. As such, obligations define in what way the responsibility holder is responsible, and how the responsibilities can be fulfilled. For example barristers have responsibility for the representation of their clients. To fulfil this responsibility they must discharge obligations that would entail, for example, planning and presenting a defence for a client.

![](/api/attachments/GV8G9GUP/fulltext/images/5fd76d07304e99ca9df3a7bbec4be9650d46312603389464e0ff51e8fb3ad7da.jpg)  
Figure 2 The three levels of abstraction of the ORDIT Model

The distinction between obligations and activities is essentially one of the level of specification. We regard obligations as a description of what needs to be done rather than how it is to be achieved. Activities are defined as specific operations that change the state of the system. The role holder may have a wide choice of activities that discharge the obligation held.

## Responsibility level

At a responsibility level of modelling the analyst is reasoning at a very high level of abstraction. The basic building blocks for thinking about organizations at this level are considerations of the responsibilities that various parties have to each other for states of affairs and the rights they have to any information that needs to be used. Often at this level of representation one is considering the responsibility that organizations may possess as a whole, and the relationships between organizations and outside parties. To give an example, one might consider the crown as an abstract embodiment of the law and various agents (e.g., judges, barristers, solicitors and the police) are responsible to the crown to constitute, organize and administrate the law.

## Obligation level

At a lower level of abstraction we can also reason about the states of affairs that have been associated with particular role holders. We can say that particular roles within an organization have sets of obligations that come about as a result of responsibilities. Thus as a result of a responsibility to provide a client with legal representation, a barrister may have obligations to plan and present a defence. From this perspective obligations can be considered as the duties that must be discharged as a consequence of holding responsibilities. At this level of representation the analyst is concerned with what needs to be done rather than how it is achieved. At this level of abstraction resources are likely to be dealt with in a fairly abstract way, that is, by referring to the logical type of information rather than how it is manifest in the real world. Thus in the legal context ‘evidence’ can be thought of as an abstract concept which does not specify the form that it takes in practice. By focusing on obligations at the role level rather than activities at the execution level, ORDIT avoids the trap of working from the system as it is instantiated at present.

## Activity level

At the lowest level of abstraction we can reason about the activities that need to be performed in order to discharge obligations. In many cases a single obligation might lead to a number of possible activities. At this level of abstraction the agents involved can also be described in specific terms, for example the activities associated with a particular barrister rather than the role of 'barrister'. Likewise the resource aspects may also be described in specific rather than abstract terms, for example allegedly fraudulent documents rather than 'evidence'.

## The case study

The case study was based on an evaluation of a pilot system in a courtroom used for the storage, retrieval and presentation of evidence in a serious fraud trial. The aim of the case study was to assess how well ORDIT principles could be applied in this rather unique setting. As the case study was a retrospective investigation, all information was obtained from HUSAT's report to the client and discussions with the HUSAT consultant who had prepared this report. This was therefore a role-played exercise with the 'client' being represented by the HUSAT consultant.

The first phase of the analysis was to identify the nature of the problem to be solved and to identify what the client wanted from the ORDIT team. This activity involved the client describing the world in which they were operating, the parties concerned and their roles in making the system operate. The result of this discussion was a focusing of the context for the ORDIT investigation. In this case it was agreed with the client that the focus of interest was the presentation of evidence in fraud cases and that the analysis should look at the current state of affairs, the experiences of introducing a pilot IT system, and some possibilities for future IT systems.

Having agreed the general scope of the investigation, it was decided to identify in more detail the boundary to the problem by identifying those stakeholders or agencies within the system of interest, and also those outside the system who impinged on it. The result was two high level diagrams. The first lists the stakeholders having some relationship to the 'black box' fraud trial (see Figure 3), and the second lists those roles within the fraud trial boundary (see Figure 4).

This distinction was considered important, as in subsequent modelling only those agencies within the immediate boundary of the problem would be looked at in detail.

## Responsibility modelling

The responsibilities of the different roles within the fraud trial are listed to illustrate the process (see Figure 5).

At this level of representation, it is possible to reason about the high level responsibilities associated with the case, and consider the implication of major changes to the organizational structure concerned. Thus if one of the scenarios for the future was the elimination of a particular role (for example the jury), then the responsibility for providing a verdict would have to be reallocated to another agent. The point to be made here is that high level responsibilities and their resultant obligations are likely to be enduring aspects of sociotechnical systems.

![](/api/attachments/GV8G9GUP/fulltext/images/3c58ba312e14902158489a9b26ab43173ed18dcd733deba5549791a41127d229.jpg)  
Figure 3 External agencies influencing the fraud trial

## Obligation modelling

Once some understanding of the current system had been obtained at the responsibility level it was decided to describe the system at a lower level of abstraction, namely that of the obligations associated with responsibilities (see Figure 6). One example of this process was a discussion that centred around the role of the prosecution counsel and the obligations that made up their duties.

Prosecution counsel have a responsibility to the crown for prosecution, and thus the associated high level obligation is to manage this prosecution. In this example this obligation can be broken down into subobligations which are involved with planning the presentation of evidence and the actual presentation itself. Planning involves the collating of evidence and preparation of questions for witnesses. Presentation involves obligations to show the evidence to the court, and to examine and cross examine witnesses.

At an obligation level of representation one can reason about the duties that agents have as a consequence of their responsibilities, and can examine what it is that role holders need to do rather than how it is achieved. Thus it can be seen that an IT system which is used in the presentation and planning of evidence will impinge directly on the role of prosecution counsel.

![](/api/attachments/GV8G9GUP/fulltext/images/daf2d661e640993d32a6486d652b95b531cb296ecb3269a610b8664b1ce0cf74.jpg)  
Figure 4 Roles within the fraud trial

## Activity modelling

Moving down to an even lower level of representation one can talk about the activities that may be associated with the discharging of these obligations. From the example given, it can be seen that prosecution counsel engage in the activities listed in Figure 7 below.

At this level of representation the analyst is interested in the activities that the agent has to perform in order to discharge obligations. The distinction is an important one to make, as the activity list covers the full range of activities that may be engaged in in order to discharge responsibilities rather than specifying what must happen in each trial.

## Considering the implications of introducing technology

When considering the implications of introducing technology for work roles, one possible starting point is to look at the changes that introducing technology would have on work roles, assuming those roles remained

Judge Responsible to the Crown to ensure correct legal procedures are followed
Jury Responsible to the Crown for providing a verdict based on the evidence given
Defendant Responsible to the Crown to be available for trial
Prosecution Responsible to the Crown to manage prosecution
Defence Responsible to the Crown to manage defence
Witnesses Responsible to the Crown to provide evidence
Ancillary staff Responsible to the Crown for conducting courtroom duties

Figure 5 High level responsibilities

## Manage prosecution

Plan evidence to present:

\- Collate evidence

• Prepare questions for witnesses

Present evidence:

• Show evidence

\- Examine witnesses

• Cross examine witnesses

## Figure 6 Obligation modelling

essentially the same, that is, involved the same responsibilities and obligations. When this is carried out for the introduction of technology in the presentation of evidence it is clear that prosecution counsel would have additional activities to perform relating to operating the technology:

(1) Presenting evidence on the display screen;

(2) Organizing data capture onto the system;

(3) Scanning documents;

(4) Preparing files for presentation;

(5) Searching the system;

(6) Retrieving documents;

(7) Linking documents into presentation files; and

(8) Coordinating the presentation with the system operator.

If these additional tasks are to be performed by the prosecution counsel, then there are implications for the skills they might require, that is, training in the use of the system. If it is considered appropriate that other agents take on responsibilities for these tasks then new

## Plan evidence to present

\- Look at documents

• Collate evidence within documents

• Make notes to prepare speech

\- Write down questions to ask

## Present evidence

\- Address the court

\- Introduce evidence in speech

\- Direct jury to read evidence in courtroom binders

\- Present argument using documents as evidence

\- Argue points of law with judge and defence

\- Draw witness's attention to documents

\- Ask witnesses questions

\- Summarize witnesses replies verbally

\- Argue with witnesses

\- Summarize case

\- Summarize evidence at end of trial

\- Direct jury to re-read evidence

\- Request jury to reach a prosecution verdict

## Figure 7 Activity modelling

work roles may need to be created. Thus it can be seen that the introduction of technology might lead to organizational change being considered, as new roles are created or new obligations and responsibilities are associated with existing roles.

In the pilot development for the courtroom a new role was introduced to perform these activities, namely that of a system operator. The system operator was given responsibility for operating the system on behalf of both the prosecution and defence counsel. However, prosecution counsel was still responsible for the planning and presentation of the vast bulk of the evidence, and so what happened was that prosecution counsel had an additional responsibility to the operator to direct the storage and retrieval of information, and the operator was given a responsibility by the prosecution counsel to operate the system on their behalf. Thus the operator has been given a responsibility along with some of the prosecuting counsels' obligations, whilst counsel have retained their original responsibilities but passed some of their obligations on.

In practice this reallocation caused difficulties. Creating this new role meant that counsel had to brief the operator prior to each court session. Owing to this, and to limitations in the technology, once a plan of action had been decided it was difficult for counsel to change the direction of their presentation of evidence. It may not have been possible for counsel to be as flexible in the presentation of evidence as they had been in the past.

Discussions with the client centred around the possibility of removing the system operator role, and whether it would have been better for counsel to operate the equipment for themselves. Further discussion took place regarding the degree of support that the IT system should provide and whether support could be given to other roles within the organization. In particular it was questioned whether IT support would be more effective in the collating and evaluating of evidence prior to the trial, rather than providing simple storage and retrieval as was currently the case in the pilot study.

These discussions provided feedback to the analyst as to whether they understood the problem domain adequately, but also acted as a focus for subsequent explorations of possible future scenarios. Part of this discussion explored the constraints that operated within the system, whether it would be possible to add/modify/remove roles, whether responsibilities could be grouped in different ways, and where IT support could be best applied.

Discussion with the client revealed that the most likely scenario for usage was that of an impartial courtroom operator. It had been noted that having a system operator who was a police officer might create a perception of bias in the case towards the prosecution, and therefore an independent operator was desirable. It was thought that having counsel provide their own operators would be inefficient, and likewise it was thought to be overly complicated for counsel to use their own expert intermediaries. It was argued that counsel would be required to learn to interact with courtroom operators as part of their training. This would require specialist skills on the part of counsel but this was seen as acceptable by the client.

## Conclusions

In such a short paper it has not been possible to describe the ORDIT methodology in any great detail (but see also Chudge and Blyth, 1993; Olphert and Harker, 1994). This paper has instead concentrated on describing some of the concepts central to ORDIT, and in showing how some of these concepts were applied to a case study. It is argued that these concepts are of considerable value in the analysis of problems concerning the introduction of technology, as the analysis focuses on the responsibilities associated with satisfying the primary purpose of the organization, rather than on the way that these are currently executed. In addition the analysis places emphasis on considering the human aspects of socio-technical systems, that is, human roles and obligations, rather than focusing on technical issues and the activities that need to be supported by technology.

As mentioned earlier, it is necessary to consider that different types of innovation may exert different types of pressure for change within the organization (see Figure 8). In the present example we have considered the impact of introducing an IT system. This, we feel, will tend to exert a bottom-up influence since change will tend to be associated with a new range of physical activities associated with operating the system (scanning documents, creating files, creating indexes, retrieval procedures, presentation procedures, etc). These in turn create new obligations and responsibilities which then become the focus of the ORDIT analysis and modelling procedures.

![](/api/attachments/GV8G9GUP/fulltext/images/0e36b170015651b206d79889f5de39493124eb573649da0085c9c697e412c1c5.jpg)  
Figure 8 Illustration of different changes exerting different influences

An alternative form of innovation can be envisaged that would create a more direct and immediate influence on considerations of responsibility. The introduction of non-jury trials for particularly complex and lengthy criminal proceedings, namely serious fraud, is something that has been considered in recent years. This, we feel, would exert a more top-down influence since a central role, that of the jury, in the legal structure is being removed. Moreover this innovation is essentially organizational and not dependent on technology. It would therefore be a matter of assessing the impact of this change on responsibilities within the legal process and redistributing these responsibilities to appropriate new role holders. Details of associated obligations and activities would tend to follow this procedure rather than precede it as in the first example discussed above.

A final point to remember is that regardless of the nature of the change being introduced, whether it be technological or organizational, the focus of ORDIT is the same. All forms of innovation affect organizations and, more importantly, the people who make up those organizations.

## Acknowledgement

The authors are very much indebted to Mr Jarnail Chudge for contributions to the work upon which this paper is based and to the Crown Prosecution Service for valuable comments on earlier drafts.

## References

Chudge, J. and Blyth, A. (1993) ORDIT: A New Methodology to assist in the process of eliciting and modelling organisational requirements in S. Kaplan (ed) Organisational Computing Systems, Milpitas, California, ACM press.

Dobson, J. and McDermid, J.A. (1989) Security models and enterprise models, in Database Security: Status and Prospects II, Landwehr C.E. (ed) (Elsevier Science Publishers, Amsterdam).

Emery, F.E. and Trist, E.L. (1969) Socio-technical systems, in Systems Thinking, Emery F.E. (ed) (Penguin, London).

Eason, K.D. (1988) Information Technology and Organisational Change (Taylor & Francis, London).

Harker, S.D.P., Eason, K.D. and Dobson, J.E. (1993) The change and evolution of requirements as a challenge to the practice of software engineering, in IEEE International Symposium on Requirements Engineering 4–6 January, San

Diego. IEEE Computer Society Press, Los Alamitos, Ca, pp. 266–72.

Olphert, C.W. and Harker, S.D.P. (1994) The ORDIT methodology for organisational requirements definition, in Human Factors in Organizational Design and Management-IV, Bradley G.E. and Hendrick H.W. (eds) pp. 421–6.

Trist, E.L., Higgin, G.W., Murray, H. and Pollack, A.B. (1962) Organisational Choice (Tavistock, London).

## Biographical notes

Dr David Poulson has been at HUSAT for the past twelve years. In that time he has been involved in a large number of research and development projects covering a wide range of design topics. These have included practical design work, as well as studies of the design process for IT products. David also provided a technical input to the development of a design framework and tools for organizational analysis. Other interests include user requirement analysis and evaluation. Recent research work has also included investigations into the design of rehabilitation technology products and the development of design tools to improve the usability of such products. David has published in the areas of design ergonomics, and rehabilitation/assistive technology.

Dr Neil Waddell has been at HUSAT for the past nine years. In that time he has undertaken research and consultancy for the CEC, government departments, major banks, the judiciary and a number of commercial organizations. His interests have included the areas of organizational and user requirements elicitation and specification. Recent research work has included the area of logistics as related to supply chain management, support needs for people with physical and complex disabilities and the social impact of video telephony on people with special needs. Neil has published in the areas of psychology, information technology and computer integrated manufacturing.

Address for correspondence: David Poulson, HUSAT Research Institute, The Elms, Elms Grove, Loughborough, Leicestershire LE11 1RG.
