---
otero_id: 216
otero_key: "4D75TN6J"
title: "The turnaround of the London Ambulance Service Computer-Aided Despatch system (LASCAD)"
authors: "Guy Fitzgerald; Nancy L Russo"
year: "2005"
journal: "European Journal of Information Systems"
doi: "10.1057/palgrave.ejis.3000541"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The turnaround of the London Ambulance Service Computer-Aided Despatch system (LASCAD)

Guy Fitzgerald<sup>1</sup> and Nancy L. Russo<sup>2</sup>

<sup>1</sup>Department of Information Systems and Computing, Brunel University, Uxbridge, Middlesex, U.K.; <sup>2</sup>Department of Operations Management & Information Systems, Northern Illinois University, DeKalb, IL, U.S.A.

Correspondence: Guy Fitzgerald, Department of Information Systems and Computing, Brunel University, Uxbridge, Middlesex UB8 3PH, U.K. Tel: þ 44 1895 266018; Fax: þ 44 1895 251686; E-mail: guy.fitzgerald@brunel.ac.uk

## Abstract

The implementation of the Computer-Aided Despatch system at the London Ambulance Service has been one of the most notorious cases of failure within the information systems (IS) literature. What is less well known is that there followed, some time later, a much more successful implementation, described as a turnaround. This paper, based on a case study approach, describes the context and detail of that implementation. A framework from the literature, used in an analysis of the initial failure, is used to analyse and compare the similarities and differences in the development of the two systems. The framework provides four interacting elements and relationships for analysis. These elements are Supporters, Project Organisation, Information System, and the Environment in which they operate. The turnaround system was found to address directly almost all the issues identified as problematic in the failure. These included the approach taken by management to understand the needs of users, including issues unrelated to the system itself, their involvement in the development process, an improvement in the availability of resources (brought about in some part because of the previous failure), the ability to follow a relaxed timeline driven by users’ acceptance levels, the preparation of infrastructure projects to develop confidence, participation and prototyping, thorough testing, phased and simple implementation, and trust building. Certain environmental factors could not be so directly addressed but nevertheless were overcome by attention to detail and internal needs. Conclusions indicate that the factors addressed are not new and are to be found in the success literature. What is unusual is that they were implemented in this case in such unlikely circumstances.

European Journal of Information Systems (2005) 14, 244–257.

doi:10.1057/palgrave.ejis.3000541

Keywords: London Ambulance Service; Computer-Aided Despatch; information system; implementation; systems; success factors; failure; case study

## Introduction

The London Ambulance Service (LAS) Computer-Aided Despatch (CAD) system (LASCAD) has become widely known as a prime example of an information systems (IS) failure (see, e.g., Beynon-Davies, 1995; Finkelstein & Dowell, 1996; Collins, 1997). The LASCAD ‘crash’ happened in 1992 hitting the newspaper headlines with suggestions that 20–30 people had died as a result, leading to the resignation of the Chief Executive (CE) (The Guardian, 1992; The Independent, 1992). Questions were asked in the Parliament and a Public Inquiry instigated. This was followed by intense media interest and further government enquiries. Subsequently, however, the LAS disaster and its aftermath faded from prominence with little media coverage and few front-page stories. In 1996, a new LAS CAD system was implemented, with relatively little fanfare, which was very successful, enabling LAS to improve its performance substantially and to win the BCS (British Computer Society) award for Excellence in IS Management in 1997. Given the magnitude of the failure of the 1992 system, this was a significant turnaround and this paper examines how such a transformation was achieved and what lessons might be learnt. The next section examines some of the issues of failure and success in the IS literature.

## Information systems failure and success

Failure, including time and budget overruns, is an ongoing theme in the IS literature. For example, according to a Standish Group survey (Jiang & Klein, 1999) only 16% of IS projects are completed on time and within budget. Of the remainder, approximately 53% are over budget in terms of both time and money, and 31% of all projects are cancelled. Despite the fact that much has been written about IS success and failure over the years, there is no generally agreed definition of these terms. Lyytinen & Hirschheim (1987), for example, identify four types of failure: correspondence failure, process failure, interaction failure, and expectation failure. Correspondence failure refers to the failure to meet the objectives originally specified for the system. Process failure is when the system is not developed within time and budget constraints, or when the system is never implemented. Interaction failure refers to poor usage of a system, where the system meets technical specifications but fails to meet the needs of the users and is either not used in part or not used in its entirety. Expectation failure encompasses the others and refers to the ‘inability of an IS to meet a specific stakeholder group’s expectations’. Sauer (1993), however, criticises this definition of failure for being too broad. Expectation failure could be applied to unreasonable expectations, and does not take into account expectations that could not be known when the system was created. Under this category, a system could at one time be viewed as a success by one group of stakeholders and as a failure by other groups; indeed, Wilson & Howcroft (2002) argue that it is not even necessary for a technology to actually change for it to be perceived differently over time. For them success or failure is a ‘social accomplishment’ dependent on the perspective of the subject and how legitimacy is ascribed to different voices. Sauer (1993) defines failure as having finally and irreversibly occurred when the level of dissatisfaction with a system is such that there is no longer enough support to sustain it. Similar to this is the definition used by Markus & Keil (1994) that takes failure to mean an unused system, not simply a system that does not live up to expectations.

There are also various definitions of success. For some this relates to the benefits provided, and results obtained, through the use of the system. Ein Dor & Segev (1978)

identified success definitions such as profitability, application to major problems, quality of decisions/performance, user satisfaction, and widespread use. Ives et al. (1983) identified several aspects of success, including system quality (decision-making performance, perceived quality), system acceptance, use or change in attitudes or behaviour. For others the success of an IS refers to qualities of the system itself, such as the timeliness, accuracy, and reliability of output (DeLone & McLean, 1992, 2003; Li, 1997), or to the users’ satisfaction with the system (Bailey & Pearson, 1983; DeLone & McLean, 1992).

Beyond the various definitions are debates about the causes of such success and failure. These fall broadly into two categories. The first relates to factors that are inadequately addressed, known as ‘risk factors’, or, at least in some sense, their opposite, that is, ‘success factors’. Jiang & Klein (1999), for example, suggest that lack of system success can be related to risks inherent in the development process, including non-existent or unwilling users, multiple users, personnel turnover, inability to specify purpose, lack of management support, lack of user experience, and technical complexity. Sarkis & Sundarraj (2003), in the context of their study of a successful IS implementation at Texas Instruments, identify important lessons (or factors) that relate to strategic planning. These are: aligning IT with the business, top management support, addressing change management issues, rationalising business processes, identifying the importance of intangible issues, and focusing on metrics. These factors are frequently mentioned and are specifically identified by Sarkis and Sundarraj as having ‘strong literature support’. Nevertheless, they suggest that they are often ignored in practice in the ‘rush’ to implement. Further factors identified include issues related to information characteristics and physical software design (Kirs et al., 2001), scope creep, lack of communication, and isolation of IT (Al-Mashari & Al-Mudimigh, 2003). A particular sub-set of the factors category is the importance of involving the users in the systems development process, which is frequently identified as predisposing IS projects to a greater chance of success (from the early work of Olsen & Ives (1981) through to more recent studies, for example, Iivari & Igbaria (1997), which takes a broader view of users, including organisational levels of users, task variety, and computing experience). Other factors that might particularly relate to the success of a system include the relationship between the IS staff and the users (Li, 1997), users confidence (Li, 1997), service quality and conflict resolution, organisation size, structure, time frame, organisational resources, maturity, project climate of organisation, responsible executive, and the existence of a steering committee (Ein Dor & Segev, 1978).

The second category relates to the effects of broader, organisational, social, and political elements and interactions. These effects are beyond individual success or failure factors, and in particular beyond purely technological factors. Markus (1983), for example, illustrated that the user resistance to a new system was motivated by political interests rather than technological deficiencies. Sauer (1993) views the causes of failure as occurring in the inter-relationship between the system itself, the supporters, and the project organisation. As do Kanellis et al. (1999), who view success as ‘a perspective that emerges from the social and technical interplay within an organisation’. In other words, success is not a onedimensional concept, but instead is reflected in ‘multiple perceptions influenced by context’.

A number of attempts have been made to analyse the LAS failure. For example, Flowers (1997) utilises Critical Failure Factors, Collins (1997) identifies ‘10 steps’ to failure, and Finkelstein & Dowell (1996) adopt a ‘false assumptions’ approach. These studies essentially adopt analysis frameworks that utilise various failure factors. Introna (1996) uses Actor Network Theory and identifies ‘Episodic Circuits of Power’, Beynon-Davies (1995) adopts Sauer’s (1993) Exchange framework, and Wastell & Newman (1996) use a multi-perspective psychophysiology methodology. These three studies go far beyond the simple concept of technical failure and relate to the wider context of organisational, social, and/or political elements for their explanations and interpretations. Such approaches seem highly appropriate for the complex LAS case. Therefore, to structure the comparison of the LAS failure with the subsequent turnaround and reduce potential bias, the authors chose the Exchange Framework (Sauer, 1993), utilised by Beynon-Davies (1995), in his analysis of the 1992 LAS failure, to underpin the analysis of the case. Beynon-Davies’ analysis adheres closely to the findings of the Public Inquiry (Page et al., 1993), which is also beneficial as it is the major source for most analyses of the LAS crash. The framework itself is relatively comprehensive, well known, and well referenced. Further, it encompasses some of the broader social, political, and organisational perspectives, characteristic of the second category of the literature identified above.

The Exchange Framework (Figure 1) describes the development of an IS as dependent upon interactions between the project organisation, the IS, and the supporters, all within a particular environment. This forms a ‘triangle of dependencies’ where the IS depends on the project organisation, the project organisation depends on its supporters, and the supporters depend on the IS. If there are problems (‘flaws’ in Sauer’s terms) in any of the factors or relationships, then that is likely to have a detrimental effect on the IS development project, leading possibly to failure or termination. The triangle is not a closed system, as each relationship is also influenced by external and environmental factors.

## Research methodology

The research methodology followed in this study is that of a case study in which the authors investigated the situation and environment of the LAS and its new CAD system primarily via a series of interviews with key players. The benefits of the case study approach are the degree of breadth and detail that can be obtained in complex real-world situations (Galliers, 1992; Darke et al., 1998). Avison (1993) suggests that ‘the strength of the case isy in its use for examining natural situations and in the opportunity it provides for deep and comprehensive analysis’.

![](/api/attachments/4D75TN6J/fulltext/images/ff62f6d5c04991a1bd630f653355accea41ee07aa330df57a4445fb9e8b6ed7e.jpg)  
Figure 1 Sauer’s exchange framework (Sauer, 1993).

Interviews and visits were conducted over a period of 6 months, with some subsequent follow-ups to check queries and issues. The formal interviews were conducted using a semi-structured questionnaire designed to collect common information but allowing the interviewee the freedom to tell their own story, in their own words, and reflect on what had happened and on what they regarded as important. Formal interviews were conducted with five key players: Martin Gorham (CE), Avril Hardy (Training Manager), Ian Tighe (IT Director), Quentin Armitage (Systems Developer) and John Jennings (Sector Controller), and some were interviewed more than once. These people were chosen based on the objectives of the study and the key roles that they played in the development of the new LAS system. Of these, Gorham, Tighe, and Armitage were appointed after the 1992 crash, whereas Hardy and Jennings experienced both the old and the new system. All formal interviews were recorded and transcribed to ensure accuracy. Additional informal discussions were held with other people in LAS, in particular despatch staff on various shifts. Observation of the operations and control room was also undertaken. Despatch staff and sector controllers are the immediate users of the system with the ambulance teams being the resources that the CAD system despatches.

Weaknesses of the case study approach are acknowledged. Common criticisms relate to the possibility of either researchers or interviewees, or both, biasing or unduly influencing the results. Interviewees who have played a key role in a development may wish for it to be seen in the best and most successful light. The authors were aware of this and attempted to cross-check data and perceptions wherever possible. Other criticisms relate to researchers having preconceived notions that result in them ‘finding what they were looking for’. To minimize these potential problems, the authors interviewed the variety of people mentioned above, representing a range of managerial, operational, and user perspectives. Some interviewees reviewed versions of the case description in order to assure that the data had been credibly interpreted from their perspective. Despite attempts to minimise these potential issues, the case nevertheless reflects the biases of the participants and the authors.

## The CAD system

This section begins with a brief description of the 1992 crash and its aftermath. This is followed by a description of the development of the new system, introduced in 1996.

## The crash of the 1992 LASCAD system

The LAS is the largest ambulance service in the world and covers an area of 620 square miles with responsibility for the seven million people who live in the area plus the many who commute or visit. The LAS comprises 70 ambulance stations, 700 vehicles (around 400 ambulances, plus helicopter, motorcycles, and other patient transfer vehicles), and over 3000 staff (including 670 paramedics and 300 control staff). On average, the Service responds to around 2500 calls per day (1500 of which are 999 emergency calls). The demand for emergency services has increased steadily over the years with an annual growth rate of around 15%.

A new CAD system was introduced on the night of 26th October 1992 to replace the previous manual despatching system. According to Beynon-Davies (1999), ‘a flood of 999 calls apparently swamped operators’ screens. It was also claimed that many recorded calls were being wiped off screens. This in turn caused a mass of automatic alerts to be generated indicating that calls to ambulances had not been acknowledged’. Operators were unable to clear the queues that developed and ambulances that had completed a job were not always cleared and made available, with the result that the system had fewer and fewer resources to allocate. Finally, at 1400 hours on the 27th October 1992 the system was unable to cope and LAS decided to terminate the system and revert to semimanual operation. Calls continued to be taken via the system but the incident details were printed out and allocation was done manually, followed by mobilisation of ambulances via the system again. This improved the situation and LAS was at least able to respond to emergency calls and continue to despatch ambulances. This failure became known in the U.K. media as the ‘crash of the London Ambulance system’. In the context of the definition of failure discussion above, the 1992 CAD system did not crash completely, although according to the Public Inquiry the problems ‘cumulatively led to all the symptoms of systems failure’ (Page et al., 1993).

As a result the CE of LAS, who had championed the 1992 system, resigned. The next day a new CE, Martin Gorham, was appointed. He had been in the NHS (National Health Service) for about 25 years, mainly in hospital management, and had been director of corporate planning for a large health authority. Despite the change of CE it was not long before further problems emerged. On 4th November 1992, the semi-manual system failed to print out calls and LAS was forced to revert to a fully manual, paper-based system, with voice or telephone ambulance mobilisation. The Times (London) of 5 November 1992 reported a 25 min delay in despatching an ambulance and senior management were forced to ‘concede that the system could not cope with its task’. In operational terms LAS was now back where it was prior to the 1992 system.

A Public Inquiry was set up by the government and its findings were published in February 1993. The Report (Page et al., 1993) was highly critical of the management of LAS. In relation to the programme of change including the implementation of the CAD system, the report stated that ‘ythe speed and depth of the change was simply too aggressive for the circumstances. Management clearly underestimated the difficulties involved in changing the deeply ingrained culture of LAS and misjudged the industrial relations climate so that staff were alienated to the changes rather than brought on board’. The report made a series of conclusions and recommendations for the future of LAS. Despite the significant problems experienced, LAS was recommended to continue to seek a computer solution for ambulance despatch but that ‘it must be developed and introduced in a time scale which, whilst recognising the need for earliest introduction, must allow fully for consultation, quality assurance, testing, and training’ (Page et al., 1993). In relation to the management of LAS, a restructuring was recommended together with a range of new appointments. It was acknowledged that such recommendations had resource implications and the South West Thames RHA (Regional Health Authority), now responsible for LAS, was encouraged to devise a financial strategy to achieve this.

Gorham agreed that the LAS needed restructuring. He says, ‘The simple fact was that the current structure was a complete obstacle to making progress. We didn’t have the level of management resources that were needed. I think that’s one of the reasons why my predecessor wasn’t able to deliver what he set out to do. He just never had the amount of high level management resources you need to turn around a big high-profile, complex organisation, which had drifted 10–15 years behind the time.’ Gorham implemented a four divisional structure and created an executive board, consisting of the CE, Finance Director, Director of Personnel, Operations Director, four Divisional Directors, and a Deputy who also managed the Control Room. Gorham also created a planning and an IT function with Ian Tighe appointed from the West Midlands Police as IT Director. Tighe in turn appointed Quentin Armitage as an IT developer.

Meanwhile, the manual despatch system continued to operate, but problems were still being experienced highlighted by the case of Nasima Begum in June 1994. The 11 year old had a liver condition, for which she was receiving regular treatment, but unfortunately her condition worsened and despite four emergency calls she had to wait 53 min for an ambulance, only to die of renal failure. The tragedy was compounded by the fact that she lived only two minutes from a hospital and that the only available ambulance was sent elsewhere, to someone who did not really require emergency service. Again very bad publicity resulted, with the media attributing the death to the delay in despatching an ambulance (Collins, 1997).

The Nasima Begum case resulted in another review of the Service, this time by William Wells, South West Thames RHA Chairman, on behalf of the Secretary of State. This review underlined the Page Report recommendations and introduced more initiatives. Further, in the first part of 1995 the House of Commons, through their Select Committee on Health, carried out a further inquiry into the Service and suggested ‘that lives may well have been lost’.

## The new CAD system (1996)

Gorham and the new LAS management team were under severe pressure to introduce a new computerised CAD system, but they felt that to do this quickly was likely to lead to at least some of the same problems that afflicted the 1992 system. They recognised that a manual system was not viable in the long-term and that a computerised solution would be necessary at some point, due partly to the increasing volumes of calls but also to meet new challenging performance targets required by the government for ambulance despatch.

Thus, the approach adopted was one of continuing operation of the manual system, despite its problems, to buy time. Additional resources and extra staff were allocated to help the system function more efficiently. Meanwhile, Gorham attempted to build bridges with the LAS workforce together with a series of infrastructure improvements (known as warm-up projects), long deemed necessary, but also calculated to help build confidence and trust prior to publicly thinking about any new computerised system. These projects included replacing the electrical system, a new control room, a digital phone system, and upgrading of the ambulance fleet, with new vehicles and improvements to make conditions better for the crews. However, to the outside world this was perceived as inaction, as Ian Tighe, the new IT Director, reflected ‘Most observers were certain that change should come far quicker than it was, and at times it was very hard to resist the pressurey’.

However, the successful implementation of the warmup projects eventually enabled the LAS to conclude that the time was right to begin addressing the design of a new CAD system. It was decided to develop the system in-house and although a package-based solution was considered and evaluated it was rejected. A participative approach utilising prototyping was adopted to help involve the users and instil ownership and acceptance of the system. A very slow and deliberate approach was adopted that provided time for participation and iteration. A great deal of attention was paid to testing and training and the system was only implemented when it was felt to be ready, not just in a technical sense but when the users were convinced about its capabilities. Indeed the implementation date for the new system was delayed at one point as a result.

In relation to technology, a new hardware platform was chosen, as the old system was essentially a PC architecture, which was not thought to be adequate for a command and control system. The new system was UNIX based with an Informix database supporting around 60 workstations. Two systems were implemented, each with mirror disks and data replication between the two, with the second system capable of running the entire system. According to Tighe, ‘We took the safe solution, this has worked for 20 years in other emergency services, and we know it works’.

The new system went live on 17th January 1996. After about a week of successful running the operation moved into the new control room. The initial system was a very basic system enabling the operators to receive a call and enter the details of an incident directly into the system. The computerised Gazetteer, using a Postal Address File, looked up the location and provided a map reference within one second. The system provided the controller with information on which of the 150 or so deployment points around London was the nearest to the incident and the controller would then dispatch an appropriate ambulance. The system additionally provided the location of the nearest hospital for the controller to pass to the ambulance crew. The new CAD system was implemented with few problems and it provided immediate benefits.

After a short period further enhancements were introduced with the most significant being in September 1996 when ‘early call viewing’ was introduced. Once the call-takers had established the address of the incident that information was immediately made available to the controllers to begin the despatch process, that is, before the call had finished. For the first time an element of re-engineering of the original manual process had been implemented and the benefits of a computerised system demonstrated. According to Armitage, in the hour before this new phase was implemented 38% of the calls were despatched within 3 min, in the next hour it was 50%, and in the following hour 60%. Next an AVLS (Automatic Vehicle Location System) was implemented, providing real-time information about what resources were available, where the ambulances were, their status, etc.

The result was that the annual performance rates improved significantly, as shown in Table 1.

Table 1 Ambulance activation rates

<table><tr><td>Year</td><td>3 min Activation (%)</td><td>8 min Response (%)</td><td>14 min Response (%)</td></tr><tr><td>1993/94</td><td>35</td><td>12</td><td>62</td></tr><tr><td>1994/95</td><td>36</td><td>13</td><td>68</td></tr><tr><td>1995/96</td><td>44</td><td>17</td><td>76</td></tr><tr><td>1996/97</td><td>80</td><td>35</td><td>90</td></tr><tr><td>1997/98</td><td>85</td><td>37</td><td>91</td></tr><tr><td>1998/99</td><td>89</td><td>39</td><td>87</td></tr></table>

These improvements also need to be viewed in the light of increasing demand for the service, for example, in 1996/97 emergency 999 calls increased by 16% on the previous year. 1

The impact in other terms was also impressive. As Armitage says, ‘although there were one or two people who were still sceptical, I think the majority had confidence. They wanted a computer system, to move away from their antiquated procedures. Now they are desperate for morey it’s very rewarding’. John Jenkins, one of the sector controllers, says, ‘there is no doubt about it, things really changed for the better. Gorham made a big impact on this Service andy improved it dramatically.’ Hardy agrees, stating that now people have ‘trust in the system, it very rarely goes wrong. It does what you want it to do and it’s very simple to use’.

Other indicators also suggest success. The number of complaints from the public dropped quickly after the implementation of the system, from 100 per month to about 25 and below, over the following few months. The House of Commons Health Committee Report of December 1996 stated that they ‘were struck not only by the technological improvements but also by the orderly and efficient atmosphere in the Central Ambulance Control. This contrasted strongly with the impression we had gained on our previous visity which was of a Central Ambulance Control that was ‘‘not a pleasant environment in which to work, being noisy, overcrowded and claustrophobic’’’. They went on to say ‘We warmly welcome the improvements in response times that the management and staff of the LAS have achievedy and the effective way in which new technology appears to have been introduced. We wish to congratulate both management and staff for their efforts in turning around an organisation whichy was on ‘the brink of collapse’ only four years ago’.

## Analysis and comparison of the 1992 and 1996 systems

The above briefly outlines the 1992 LAS crash and the development of the new, more successful, system in 1996. This now forms the basis for analysis and comparison of the two systems and in this section they are analysed using Sauer’s Exchange Framework as utilised by Beynon-Davies (1995) in his analysis of the 1992 LAS failure. The four main elements of the framework are: environment, project organisation, IS, and supporters. Table 2 lists these elements and the factors within these elements and summarises the findings from the analysis in 1992 and 1996. The dates of 1992 and 1996 are used to denote which of the two systems is being discussed, although these are just the implementation years and of course much of the development of each system was in fact prior to these dates.

## Project organisation

The first element in the framework is Project Organisation and Beynon-Davis identifies seven factors that contributed to the failure in this context. These are the inexperience of the developers, a history of failure, an over-ambitious project timetable, contractor problems, poor project management, incomplete software, and poor training. These are now examined in turn.

Beynon-Davies (1995) and the Page Report comment that the 1992 developers had ‘no previous experience of building despatch systems for ambulance services’. This resulted in insufficient attention being paid to the critical nature of the project with the specification being ‘poor and leaving many areas undefined’ (Beynon-Davies, 1995) and the system being implemented without having undergone proper testing. This issue was directly addressed in the 1996 system with experienced developers appointed from the West Midlands Police with knowledge of building command and control systems. This appears to be a significant difference between the two developments and an important factor in the turnaround. This experience led the developers to address the 1996 project in a significantly different way and to have opted for a more robust technical infrastructure.

The second factor is the ‘history of failure’ in LAS. Prior to 1992, there had been an earlier attempt to computerise the despatch system that was abandoned as an expensive failure. This may well have been an important factor contributing to the 1992 failure. However, in 1996 the history of failure was even greater, because of the traumatic 1992 crash. Thus, this presents a problem for the analysis because in 1992 it was seen as a flaw or problem, leading to failure and yet in 1996 it was seen as an important driver for success. The explanation is probably to do with the degree of failure. The pre-1992 abandonment was only an internal LAS issue, whereas the 1992 system was a national disaster and was at the forefront of everyone’s mind and acted as a catalyst for not letting the same thing happen again, that is, the greater the disaster the more it pushes the developers to adopt the opposite approach to that taken previously. However, this may be difficult to identify in other studies of failure/success due to the unusually high level of visibility of this failure, and the resulting attention and resources devoted to its solution.

The third factor is the ‘over-ambitious project timetable’ identified as a problem in 1992. In 1996, despite the enormous political pressures on Gorham and LAS to move quickly, they resisted, and a very cautious approach was adopted before publicly considering a new computer system. The developers of the new system recognised this problem with the 1992 development and went to the other extreme with a relatively relaxed timetable that was even further delayed at one stage.

The fourth factor is the contractor problems that were identified in 1992. It was felt that there had been some misleading of LAS management over their developers experience and confusion over the role of the prime contractor and subsidiaries in the project. No such problems were encountered in 1996 as the development was undertaken in-house by LAS itself. This was a deliberate decision based on the problems experienced previously and it ensured that there were very clear responsibility lines. It also meant that LAS could control the project themselves and as Tighe states, ‘We wanted to control the pace of change, we didn’t want to be in the position that to carry out a simple function you had to know about ten others, because that would have changed the pace. We needed to dictate the agenda’. (This was also one of the reasons for rejecting a package solution.) Given the history, the system had to be acceptable to the staff and according to Tighe, ‘the only thing they would find acceptable is the thing that they invent’.

The next factor was poor project management in 1992. It had originally been specified that PRINCE (Projects in Controlled Environments), a project management method, should be used but the contractors appointed did not know PRINCE and therefore it was not followed. Exception reports were never raised because of the fear of delivering bad news. In 1996, PRINCE was used as the method to drive the project, but on its own it would not have helped much, rather the culture needed to be changed to make it work. Tighe says, ‘we had to convince people that if they saw a problem that they must not feel ashamed and feel that they have made a mistake and want to hide it. We had to instil the understanding that problems had to be aired, that it could be put right. This could only be achieved in relation to the development of the system if the culture of the whole organisation was also changing. The project management method was used throughout, so everyone understood it, the reports required, the project assurance team, the significance of it, etc. It began with the warm-up projects and thus people knew about it long before the computer system was developed’.

The next factor was the ‘incomplete software’ and indeed the 1992 system had serious flaws in both the delivered system and the software development process.

The most serious problem was the lack of adequate testing and the system failed, in part, because it could not handle the volume of calls required. In the 1996 system, testing was extensive including system testing, stress testing, and usability and organisational testing. The testing process was seen as critical in a command and control environment, but it was also recognised to be necessary for gaining the confidence of some, still sceptical, users. Users were involved throughout the process and their input was used to make modifications even at this relatively late stage. Armitage states, ‘We did a lot of stress related testing on the systemy we loaded the system up with 3000 jobs in an hour and at that time the busiest days were about 3000 jobs in the whole day. We let the users see this happen and they took heart, they saw the system working much much harder than it would ever need to, and surviving’.

The final factor in relation to project organisation was the poor training of users in 1992. Although some training had taken place, it was deemed to have been too early and by the time the system had been implemented the skills had been forgotten (Page et al., 1993). In developing the 1996 system a great deal of effort was devoted to training, not just in relation to the computer system but training on all procedures. Hardy headed the training responsibility and she comments that ‘it was a very strange experiencey to be asked the question ‘how long do you need to train people?’, it was an absolute luxury compared to the time before when it was what can we cram into the short time that we’ve got left’. Indeed the need for full training was one reason why implementation was delayed at one point. Tighe adds, ‘We weren’t prepared to go live earlyy until we were all happy that the programs were fully tested, the system tested, integration tested and the users had tested and accepted and that we’d performance tested.’

Thus, the factors relating to the element of Project Organisation in 1996 were quite different from those in 1992. Development was done in-house, with experienced developers following a well-established project management method. The developers were able to align the development activities with the specific needs and history of the LAS, with an appropriate timeline, an incremental process, and substantial user involvement.

## Information system

The next element of the framework relates to the IS itself and Beynon-Davies (1995) identifies three factors of significance in 1992; the complexity of the system, communication and response time problems, and the frustration of the ambulance crews.

The 1992 system had been seen as a way to automate the entire process with relatively little manual/user intervention. It was indeed complex, and substantially different from the previous way of working, with many new and different functions. Communication was also identified as problematic in the 1992 system, such as ambulance crews pressing the wrong buttons, or ambulances being in radio black-spots (Beynon-Davies, 1995), and this meant that incorrect information was sometimes used in allocation decisions. The misdirection of ambulances, the large queue of exception messages, and frustrated patients calling in multiple times all contributed to a ‘vicious circle’ leading to unacceptable response times. The 1996 system was in contrast deliberately straightforward. The initial system was a simple calltaking one, which was then built upon in stages, as each stage was understood and accepted.

A second principle adopted for the new 1996 system was that it should be as close as possible to the functioning of the manual system. This was thought to be the best way to obtain buy-in and acceptance from the staff. As Hardy states, ‘We wanted everything to be the same, the screen format was to follow as closely as possible the printouts on paper and the printed version of the call should also be the same format that would be used if you were hand-writing the form’. The past was influential here, with the 1992 crash system having had a very different look and feel to the manual system, which was thought to have caused unnecessary problems. It seems clear that these policies of simplicity, implementing in phases, and reflecting the manual system with which people were familiar enhanced the chances of success in this context. Further the system was tested thoroughly at each stage and was supported by a full back-up system that could take over immediately if any problem arose with the primary system. As a result, no response time problems were reported with the 1996 system and the performance was significantly improved.

The final factor in this dimension relates to ‘crew frustration’ with the system. Beynon-Davies (1995) states that there was a belief that ‘this may have led to an increased number of instances where crews failed to press the right buttons, or took a different vehicle to an incident than that suggested by the system’. The ambulance crews were very negative about the system in 1992, they felt that they had not been involved in its development, that they had not been listened to, and were very frustrated with its ineffectiveness in use. In 1996 as has already been indicated, these frustration problems were addressed in various ways, including the ‘warm-up’ projects, one of which not only upgraded the ambulance fleet but also included features to make the crews’ job more comfortable, for example, air conditioning in the ambulances, an internal door, and portable radios. The crews, although some were still somewhat reluctant, were generally more amenable to the 1996 system than they had been in 1992.

Thus, the element of IS in 1996 was also quite different to 1992. The system was very simple and straightforward, it reflected the manual way of working, and its development involved the users to overcome the previous resistance and frustrations. The result was a system that not only worked well from a technical perspective but also one that integrated well with the operators and users and with which they felt comfortable.

## Supporters

The third element of the framework is that of Supporters of the system (Sauer, 1993). Although Beynon-Davies (1995) states that he prefers the term Stakeholders rather than Supporters, to indicate that some of those with interests in the system may be negative rather than supporters, and he identifies the staff of LAS to be in this category. He identifies four factors in relation to the 1992 staff/stakeholders as follows: mistrust of management, low morale, lack of ownership of the system, and an anticomputer bias.

In 1992, the then CE wanted to push through automation as quickly as possible, and in one go. The rank and file of the organisation were not behind him in his attempt to impose what was seen as a technological solution to a wider set of organisational problems and there was a good deal of mistrust. The background of mistrust of management was partly the result of previous history and in particular an earlier pay dispute in which the London branch had held out against a national agreement with relations between the staff and management being extremely poor. Also the CAD system, with its automation of manual tasks, was seen as a threat to jobs. Further, Beynon-Davies (1995) quotes suppliers talking about their perceptions of LAS as exhibiting ‘disorganisation, low staff morale, friction between management and the workforce, and an atmosphere of hostility towards computing systems’. Gorham concurs with this and says that some of the war stories he came across in his discussions with staff were ‘frightening – this was nasty stuff’ and ‘it was an organisation that didn’t respect individuals and that was a core problem’.

There was clearly a very deep underlying mistrust of management in LAS and this had to be changed prior to any attempt to introduce a new computer system in 1996. As has been shown, Gorham attempted to build bridges with the workforce and demonstrate good faith. One important element of this was the warm-up or infrastructure projects, already discussed. These projects were undertaken with a great deal of care and effort was devoted to involving the staff in their development. For Tighe it was about asking, ‘Why didn’t this work before? The technological aspects had always spelt trouble but if we ignore that side, why did people reject it? How do we generate a different reaction? Can we create a different environment where people are actually more willing to accept that change is positive and that there might be something in it for them, as well as for everybody else’? One project reflecting this was the provision of portable radios for the ambulance crews so that they could be in communication with each other and the control room when away from their vehicles. This saved time but also was designed to improve staff security, with the addition of an emergency button, which gave something of benefit directly to the crews. Changing such a culture was a slow and laborious process, involving high levels of consultation and persuasion, but little by little perceptions changed and as each project was successfully implemented and seen to be delivering benefits the mood began to change. As Tighe states, ‘people began to gain confidence in us, they saw that we actually did know a little bit about technology and implementation’.

The participative approach adopted for the new CAD system was also important in re-establishing trust. One of the techniques employed initially was to have open forum sessions that anyone could attend. As Tighe recalls ‘We constantly sat down with team and non-team members in open sessions where we pledged to answer any question as honestly as we could. We stood out at the front, as Directors, and they gave us hell, but we shared as much as we could of what was going on and our understandings. People wanted to know what was happening, what the view was on any topic, they wanted to know what would happen if you did this in this way, and that went on a lot’. There were a good number of these forum sessions but in the end they became quite poorly attended, whereas initially the meetings would attract 30–40 people in the end only two or three were turning up. This was interpreted by Tighe as the staff showing confidence and being happy to leave others to get on with it.

The participative approach adopted included prototyping. The users would be presented with designs for comment and reactions. They were not expected to come up with formal specifications, they could just react to prototypes. The idea was to bring the users on board and give them confidence in the idea of computerisation and using the system. Initially, it was decided that the first part to be tackled would be the management of the resources, that is, the ambulances, their location, and deployment. This seemed sensible as it would deliver important benefits. Armitage, the project leader, and also the main programmer of the system recalls, ‘I went away and produced the first prototype, not talking to users at all but having observed how the control room worked’. Although it might seem strange not to talk to the users, to begin with it was felt that a computer system was still such a contentious issue that it would be best to start with a prototype that people could see rather than asking them to provide a specification. The resources prototype was demonstrated to users and they said ‘actually we’d like the computer to do the call-taking first, we’re not so concerned about the resources. That can come later’. With some reluctance this was agreed and Armitage thinks that it was an important decision, ‘I think to some extent it helped that we had gone down the wrong route (as the staff perceived it) and they said no, we want you to do something else, and we did. They saw that they could have considerable influence over the way things were done and that they weren’t frightened to say ‘oh we don’t like it like that, we want it changed’ and although it took time to build up the relationships it worked very well’.

Hardy recalls group meetings to have a first attempt at designing the new screens layouts. ‘A big group of us all sat there with the systems people who made a first attempty and we would say that we’d like it to look somewhat different and they would make some changes, there and then, so that we could actually see it. This was one of those exercises where we went full-circle, loads of times. We’d all sit round the table with all the stakeholders therey Gradually we worked through it all until we were happy with the end result and this went an awfully long way to convincing people that things were going to be different this time’. Thus, people who wanted to be involved would participate in the working groups, while those who did not want to be directly involved could attend the Forums to hear what was happening and why.

The degree of flexibility and response to users’ comments and requests was significant, particularly in the early stages. Clearly, the system could have been developed much faster without striving for this consensus, but it was deemed to be the over-riding consideration. Hardy suggests that this was very painful at times, ‘we would go around and around because you’d be presented with something and share it with the users. The users would mull it over and come up with all sorts of suggestions and then you’d come back again and review ity and it would just go on and on and on like that. You would often come full circle and be back where you started. But unless you go through that process you don’t feel like you’ve been involved’.

This participation, especially in the early period where the focus was on the call-taking, involved about 300 people, primarily the Control Room staff, rather than absolutely everybody. This ‘Golden Circle’, as it became known, has been criticised by McGrath (2002) for not involving the ambulance crews adequately and she suggests that some parties were deliberately kept out of this process, as they ‘might challenge the legitimacy of the project’. Tighe confirms that at this point, the ambulance crews were not involved in the design of the call-taking system. He says that it was felt unnecessary to involve those who were not directly affected, and secondly, not everybody could be involved from a purely practical perspective. Further he suggests that it was importantly about empowering those whose views had been particularly ignored in the 1992 system, that is, the Controllers.

Thus, the element relating to Supporters in 1996 was also quite different to 1992. We have seen the impact of the activities undertaken by the new LAS management and the development team to address the identified stakeholder problems, that is, mistrust of management, low morale, lack of ownership of the system, and an anticomputer bias. In 1996, they involved a broad set of users in many different ways, ranging from communication with management via the open forums or directly with the CE as he participated in the operations of the organisation or through participation and prototypes.

This helped contribute to the feeling of ownership and buy-in of users, and the increasing level of trust helped reduce the anti-computer bias of 1992.

## Environment

The final element in the framework is the environment. Beynon-Davis identifies eight environment factors that contributed to the failure in 1992. These are the poor NHS and labour relations background, the lack of a strategic vision for the organisation, the aggressive pace of change, the lack of investment in LAS, a ‘fear of failure’ on the part of management, and the assumption that changes in working practices could automatically be achieved by the use of information technology.

The NHS reforms were clearly an important contextual factor in the 1992 development. Beynon-Davies states that ‘A great deal of the shape of the LASCAD project was determined by the internal tensions within the NHS’. The government of the time was attempting to reform the NHS to make it more ‘efficient and effective’ with the establishment of NHS Trusts and the introduction of more market-oriented purchaser/provider relationships. These changes were highly contentious and seen by some as a threat to the very existence of the NHS. The NHS unions actively resisted these changes and it had a detrimental effect in terms of morale within LAS, resulting in a lack of support for the CAD project and an antipathy towards management.

The 1996 development also took place in this environment, with the NHS still being ‘reformed’ with opposition and bad feeling within the NHS an ongoing factor. However, after the crash Gorham, the CE, had the reports of the various public inquiries into the crash to help in the argument for the provision of additional time and money. The inquiry reports also helped set a different agenda for LAS. Gorham’s goal was to improve LAS, in terms of management, personnel, infrastructure, and efficient use of resources and the new CAD system was an important, but just a small part of that. Additionally, the 1992 failure meant that the government did not want another set of bad publicity, which could and would be used by its political enemies. This was of some considerable benefit to the 1996 development.

The poor industrial relations of the 1992 development were, at least initially, still very bad in 1996. When Gorham took over he found himself immediately facing the staff union representatives who came into his office demanding that the computer system be switched off. Gorham admits he did not really know what to do. He had the unions on one side saying it must be shut down, and what was left of his management team telling him that to shut down would be the final management abdication. Gorham says ‘there I was sat in the middle and didn’t really understand what they were talking about anyway but I managed to buy some time being new in post’.

Gorham used this time to talk to the union representatives and try and establish some kind of relationship and dialogue. He saw their role as crucial and needed them to be, ‘if not completely supportive, at least not too antagonistic’. He tried to appeal to the trade unions by stressing that it was about the future of LAS rather than just the system. He felt that getting them to work together with him was not impossible because the unions were apparently somewhat shocked and a little surprised at the turn of events, particularly the resignation of the CE. They had seen him as the problem and now found themselves having ‘won’ that battle but not quite knowing what to do next. Gorham describes this as the unions ‘no longer having this frame of reference, which was quite useful’.

The fact that there was no overall IT responsibility in the NHS in 1992 has been highlighted as a factor by Beynon-Davies, and possibly if there had been such a function there might have been some IT strategy, standards, or controls in place that might have helped the 1992 development for the better. However, such an overall IT responsibility in the NHS was still not in place by 1996 and the new system was developed without the benefits that such a responsibility might have provided. This seems to indicate that while an overall NHS IT responsibility might have been helpful it was not a necessary condition.

The next factor identified by Beynon-Davies as problematic was the ‘lack of a strategic vision’ in 1992. It is not clear whether Beynon-Davies meant an NHS vision or an LAS vision. Certainly there was no specific NHS vision, as has been discussed above, but the 1992 CE did have a strong vision for the LAS and the CAD system, and here we disagree with Beynon-Davies; there was a vision, it was just that it might be considered somewhat inappropriate. In 1996, there was also a strong strategic vision for LAS, on the part of the CE, but it was somewhat different and to be achieved in very different ways.

In 1992, management’s fear of failure was argued to be the reason that the CE drove forward with the system in the face of evidence, even prior to implementation, that the system was inadequate. The fear of being seen to fail was perhaps the reason that the implementation was not delayed when problems came to light. Ironically the failure was actually much more public and disastrous than any loss of face that would have occurred if the system had been delayed, or even abandoned, prior to implementation. In 1996, there was still a fear of failure and a desire not to be seen to lose face. The commitment to a new computerised system was contentious with the staff, and the management needed to make sure it was successful, but this time losing face was not about backing down in the face of staff and unions but about bringing those people on board.

Beynon-Davies identified as an additional environmental factor in 1992 the desire of the CE to use IT as the driver for ‘changing working practices’. It was thought that the automation of the process would be to a level where the staff and operators would not really be required to make any decisions and thus did not need to be much involved. IT was seen as a battering ram for process change, which resulted in fears for their jobs by the staff. In 1996, there was also a desire to see changes in working practices in order to improve performance, but IT was used very gently rather than as the mechanism for pushing major change, it was not a threat to jobs, but it was part of a larger change process.

Thus, it can be seen that when comparing the element of environment of the 1992 crash and the 1996 system, some important aspects were the same or at least quite similar (in the comparison of the previous elements significant differences were observed). Similarities can be seen in relation to the context of the NHS, which was still exhibiting internal tensions and continuing to be politically charged, with the government demanding modernisation of the NHS and LAS. Labour relations were also poor, at least initially in the 1996 development. However, there were some significant environment differences. The aggressive pace of change of 1992 was substituted with the very gentle, deliberate pace of 1996. The 1992 use of IT to drive changes in what were seen as restrictive working practices were replaced by the use of IT to more gently enable change with the system closely reflecting the manual system, at least initially. In relation to investment in LAS, the impact of the 1992 crash was such that the government was prepared to temper its demands of LAS somewhat and to provide significant extra funding to make sure that such a disaster did not occur again. The Public Inquiry reports were also undoubtedly helpful to the 1996 development in terms of putting pressure on the government to address certain key issues. Thus, a mix of similarities and differences are found in relation to the element of environment.

## Summary

The above analysis is summarised in Table 2, with the 1992 factors, identified by Beynon-Davies (1995), compared with the development of the 1996 turnaround system. In the next section, some implications of this analysis are discussed.

## Discussion

The analysis shows that almost all the problem factors of 1992 were directly addressed in 1996, mainly by adopting exactly the opposite or inverse approach. For example, the problems of complexity of the 1992 system were addressed by developing, at least initially, a very simple system, reflecting the structure and outputs of the existing manual system, and implementing in a staged manner. The factors that were not addressed or changed were typically those outside the direct control of LAS management, for example, the history of failure, the context of the NHS reforms, and the lack of an overall NHS IT responsibility. It is interesting that none of these factors that remained similar were sufficient to undermine or derail the success of the new system. Although, as has been noted, the history of failure, resulting in the media interest and the Page Report, probably contributed significantly to the obtaining of improved funding that enabled the ‘warm-up’ projects and the system itself.

Overall the following general factors emerge from the analysis as of key importance: good project management; realistic (relatively relaxed) project timescales; use of experienced developers; a participative approach; prototyping; good training; extensively tested software; staged development and implementation; ownership by users and line management; strategic vision and buy-in from senior management; establishment of trust between staff and management; adequate investment for the project in hand; and a combined IT and wider organisational focus of the project. None of these are particularly surprising or indeed original, as many have been identified in previous studies (e.g., Iivari & Igbaria, 1997; Jiang & Klein, 1999; Kirs et al., 2001; Sarkis & Sundarraj, 2003); nevertheless, the case provides further evidence of their importance in relation to successful IS.

This study set out explicitly to compare the 1992 and 1996 development environments based on Beynon-Davies’ analysis (1995), utilising Sauer’s Exchange Framework, of the 1992 failure, and therefore for consistency our analysis followed this framework. This framework enabled an interesting comparison that particularly highlights the way in which the new development effectively addressed the identified problems of the old. It shows how flawed the 1992 development was, which is well known, and also how it was possible to overcome such flaws, which in 1992 seemed unlikely. It shows the importance of the four elements of the framework and their interaction. None of the factors discussed within each element can be said to stand alone, but instead relate to, and are influenced by, other factors in other elements. It also, in our view, shows the importance of the environment factors in framing the two developments and contributing to understanding the effect of these factors and thus how to address them.

There are, however, some limitations to this approach. The framework, or at least Beynon-Davies’ use of it, seems to focus more on factors than processes, although the authors have tried to consider both in this analysis. Also the authors do not always concur with Beynon-Davies’ categorisations of factors within Sauer’s four elements; nevertheless, his categorisations have been followed. This framework also prevents the case being presented chronologically, as the four elements have to be addressed separately, and it is hoped that this has not prevented the story of the 1996 development emerging in its own right.

## Conclusion

Given the high cost of IS failure, the importance of determining failure and success factors cannot be ignored. This paper addresses issues of failure and success in IS by outlining the 1992 LASCAD crash and then describing and analysing the development of the 1996 turnaround system utilising a framework from the literature (Sauer, 1993, as used by Beynon-Davies, 1995)

Table 2 Comparison of the 1992 and 1996 development contexts

<table><tr><td>1992 Failure</td><td>1996 Turnaround</td></tr></table>

## Project Organisation

\- External developers had no previous experience of building despatch systems for ambulance services.

\- History of failure: earlier attempt at computerisation abandoned as an expensive failure.

\- Over-ambitious project timetable.

\- Contractor problems.

\- Poor Project Management: PRINCE prescribed but not used.

\- Incomplete software put into use; thorough testing not done.

\- Training too early. Training inadequate and could not keep up with frequent changes to software.

## Information System

\- Complex system that automated call-taking, allocation, and despatch with little manual/user intervention. Different from previous way of working, with new and different functionality.

\- Response time problems due to numerous communication problems such as a large queue of exception messages, repeat calls by patients, and ambulance crews pressing the wrong buttons.

\- Ambulance crews were very negative about the system. Bad feeling about previous labour disputes. Crews felt that system was forced on them, without their input. Resistance.

## Supporters

\- System was brainchild of CE who refused to delay implementation even after problems arose. Rank and file not in support. Mistrust of management.

\- Morale was not high prior to implementation of system, and sunk to new lows after the ‘crash’.

\- Little computer experience beyond earlier failure. Anti-computer bias in staff and crews.

\- Staff and crews were not consulted and felt that system was imposed upon them. Lack of ‘ownership’.

## Environment

\- NHS reforms to be more efficient and effective possibly pushed CE to seek quick improvements through technology.

\- Poor labour relations due in part to earlier pay dispute and general attitude towards management.

\- NHS – no overall IT responsibility so no standards or controls in place.

\- No strategic vision (according to Beynon-Davies’ assessment). In our view, there was a strategic vision held by the CE, albeit a flawed one.

\- Pace of change too aggressive.

\- Lack of investment – went for the cheapest option.

\- Management fear of failure led to ‘full steam ahead’ approach, in spite of evidence that system was inadequate.

\- CE wished to change working practices, using IT as the driver.

\- In-house developers with experience developing command and control systems for Police services.

\- Even greater history of failure, which served as catalyst for avoiding failure again.

\- Very relaxed project timetable.

\- No contractors: in-house development.

\- Good Project Management: PRINCE used, realistic view of project, ‘no blame’ culture.

\- System developed in smaller increments; thorough testing undertaken; and users involved throughout.

\- Training good, timely, and accurate. Training manager assigned. User participation aided understanding.

\- Initial system very simple, built in stages. First implemented simple call-taking system as users requested. Initial system closely followed manual way of working.

\- No response time, or other problems, with implementation. The system had full back-up system that could take over if problems arose with the primary system.

\- CE made peace with labour unions and spent time with ambulance crews. Ambulance fleet was upgraded. Staff and crews more receptive to the system

CE worked hard to develop trust in the workforce. IT staff also established good relationship with control staff by soliciting end user input and allowing development to be directed by it.

\- Morale improved. CE stressed internally and externally that staff were not to blame for 1992 failure.

\- Still anti-computer at outset, but difficulty in achieving im provements without computerisation began to change the attitude towards computerisation.

\- Widened ownership by involving users in the development process. Users felt they had been listened to and the new system reflected their wishes. (Ambulance crews not so involved)

\- Still upheaval/change in NHS and pressure to reform. However, 1992 outcome resulted in more time and money allocated in effort to avoid a repeat.

\- Still difficult (although some positive change). Unions had succeeded in getting prior CE to resign.

\- Still no NHS overall IT responsibility. However, LAS did create internal IT staff.

Initially, the only strategic vision held by the CE was ‘how to get out of the hole’. CE did evolve a strong strategic vision after gaining perspective on LAS.

\- Change but at very gentle pace.

\- Significant investment not only in the system itself but also in ‘warm-up’ projects. Finance made available as a result of the crash.

\- Still fear of failure but implementation delayed until system and users were ready.

\- Still desire to change but not using IT as a battering ram for process change.

to compare the two cases in relation to factors that were identified as significant in the 1992 failure. The findings indicate that the failure factors identified in relation to the 1992 crash were, in the main, addressed successfully in the 1996 system. From this some specific and generic issues relating to successful systems development are suggested.

The most important differences between the two processes relate to the IS, the project organisation, and to the supporters. Fewer of the environmental factors were different at the time the 1996 system was introduced. When the changes are examined, it becomes apparent that leadership and the understanding of the needs of staff, as opposed to the forcing through of change without consensus, were important. In general, there were a number of key people who were able to act in a way that reflected the overall ethos of the approach. Their presence was critical, as was the availability of resources and the ability to learn from previous mistakes. The analysis highlights the need for thorough testing and training and a sensible implementation deadline. It also shows the importance of taking into account the broader context, including the human element (supporters in Sauer’s terms), into which an IS will be introduced.

## About the authors

Guy Fitzgerald is Professor of Information Systems at Brunel University and is Director of Research in the School of Information Systems, Computing, and Maths. Prior to this, he was at Birkbeck College, University of London, Templeton College, Oxford University and Warwick University. He has also worked in the computer industry with companies such as British Telecom, Mitsubishi, and CACI Inc., International. His research interests are concerned with the effective management and development of information systems and he has published widely in these areas, including articles in European Journal of Information Systems, Journal of Strategic Information Systems, International Journal of Information Management, Communications of the ACM, and Journal of Information Technology. He is co-author, with David Avison, of the text Information Systems Development: Methodologies, Techniques,

## References

AL-MASHARI M and AL-MUDIMIGH A (2003) ERP implementation: lessons from a case study. Information Technology & People 16(1), 21–33.

AVISON DE (1993) Human, Organizational and Social Dimensions of Information Systems Development. North-Holland, Amsterdam, 496pp.

BAILEY JE and PEARSON SW (1983) Development of a tool for measuring and analyzing computer user satisfaction. Management Science 29(5), 530–545.

It is hoped that this study is interesting in its own right but also contributes to our understanding of IS success and failure. The study is one of a very small number of longitudinal examinations of a turnaround process. The application of this framework to other cases of IS development and indeed turnarounds would contribute further to our understanding of long-term success and failure of IS implementations.

Whereas a single case study cannot be viewed as directly generalisable, the results do contain outcomes that are supported by various other studies and provide some implications for practice. The experience of LAS provides managers with a number of strategies for achieving successful IS implementation. Foremost is the recognition that turnaround is a gradual process, requiring an understanding of the context, including the system, the project organisation, the stakeholders, and the environment in which they interact.

## Acknowledgements

We thank all those who participated in the case for all their time and effort, especially Ian Tighe who also helped facilitate the research.

and Tools, and is co-editor of the Information Systems Journal (ISJ), an international journal, from Blackwell Publishing.

Professor Nancy L. Russo is Chair of the Department of Operations Management and Information Systems at Northern Illinois University. She received her Ph.D. in Management Information Systems from Georgia State University in 1993. In addition to studies of the use and customisation of system development methods in evolving contexts, her research has addressed web application development, the impact of enterprise-wide software adoption on the IS function, IT innovation, research methods, and IS education issues. Her work has appeared in Information Systems Journal, Communications of the ACM, Journal of Information Technology, Information Technology & People, and other journals, books, and conference proceedings.

BEYNON-DAVIES P (1995) Information systems ‘Failure’: the case of the London Ambulance Service’s Computer Aided Despatch Project. European Journal of Information Systems 4, 171–184.

BEYNON-DAVIES P (1999) Human error and information systems failure: the case of the London Ambulance Service Computer-Aided Despatch system project. Interacting with Computers 11, 699–720.

COLLINS T (1997) (with BICKNELL, D.) Crash: Ten Easy Ways to Avoid a Computer Disaster. Simon and Schuster, London.

IIVARI J and IGBARIA M (1997) Determinants of user participation: a Finnish survey. Behaviour and Information Technology 16(2), 111–121.

DARKE P, SHANKS G and BROADBENT M (1998) Successfully completing case study research: combining rigour, relevance and pragmatism. Information Systems Journal 8(4), 273–289.

DELONE WH and MCLEAN ER (1992) Information systems success: the quest for the dependent variable. Information Systems Research 3(1), 60–95.

DELONE WH and MCLEAN ER (2003) The DeLone and McLean model of information systems success: a ten-year update. Journal of Management Information Systems 19(4), 9–30.

EIN DOR P and SEGEV E (1978) Organizational context and the success of management information systems. Management Science 24(10), 1064–1077.

FINKELSTEIN A and DOWELL J (1996) A comedy of errors: the London Ambulance Service case study. In Proceedings Eighth International Workshop on Software Specification & Design IWSSD-8, pp 2–4, IEEE CS Press: Washington, DC, USA.

FLOWERS S (1997) Information systems failure: identifying the critical failure factors. Failure and Lessons Learned in Information Technology Management 1, 19–29.

GALLIERS RD (1992) Choosing information systems research approaches. In Information Systems Research: Issues, Methods and Practical Guidelines (GALLIERS RD, Ed.), pp 144–162, Blackwell Scientific, Oxford.

THE GUARDIAN (1992) Ambulance Chief Resigns, 29th November, pp 1–2.

THE INDEPENDENT (1992) Software Failure May be Behind Ambulance Crisis by Susan Watts and Ian McKinnon, 30th October 1992, p 2.

INTRONA L (1996) Management. Information and Power, Macmillan.

IVES B, OLSEN M and BAROUDI JJ (1983) The measurement of user information satisfaction. Communications of the ACM 26(10), 785–793.

JIANG JJ and KLEIN G (1999) Risks to different aspects of system success. Information and Management 36, 263–272.

KANELLIS P, LYCETT M and PAUL RJ (1999) Evaluating business information systems fit: from concept to practical application. European Journal of Information Systems 8, 65–76.

KIRS JP, PFLUGHOEFT K and KROECK G (2001) A process model cognitive biasing effects in information systems development and usage. Information and Management 38, 153–165.

LI Y (1997) Perceived importance and information system success factors: a meta analysis of group differences. Information and Management 32, 15–28.

LYYTINEN K and HIRSCHHEIM R (1987) Information systems failures – a survey and classification of the empirical literature. Oxford Surveys in Information Technology 4, 257–309.

MARKUS L (1983) Power, politics and MIS implementation. Communications of the ACM 26, 430–444.

MARKUS ML and KEIL M (1994) If We Build It, They Will Come: Designing Information Systems That People Want to Use. Sloan Management Review 35(4), 11–25.

MCGRATH K (2002) The Golden Circle: a way of arguing and acting about technology in the London Ambulance Service. European Journal of Information Systems 11, 251–256.

OLSEN MH and IVES B (1981) User involvement in systems design: an empirical test of alternative approaches. Information & Management 4, 183–195.

PAGE D, WILLIAMS P and BOYD D (1993) Report of the Public Inquiry into the London Ambulance Service. HMSO, London (referred to as the Page Report).

SARKIS J and SUNDARRAJ RP (2003) Managing large-scale global enterprise resource planning systems: a case study at Texas Instruments. International Journal of Information Management 23(5), 431–442.

SAUER C (1993) Why Information Systems Fail: A Case Study Approach. Alfred Waller, Henley-On-Thames, Oxfordshire.

THE TIMES (1992) New Failings Force 999 Staff to Ditch Computers’ by Tim Jones, 11th May 1992, p 6.

WASTELL D and NEWMAN M (1996) Information systems design, stress and organisational change in the Ambulance Services, A Tale of Two Cities. Accounting, Management & Information Technology 6(4), 283–299.

WILSON M and HOWCROFT D (2002) Re-conceptualising failure: social shaping meets IS research. European Journal of Information Systems 11, 236–250.
