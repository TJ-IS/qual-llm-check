---
otero_id: 1406
otero_key: "S695SMGU"
title: "Transportation security decision support system for emergency response: A training prototype"
authors: "S.W. Yoon; J.D. Velasquez; B.K. Partridge; S.Y. Nof"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.06.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Transportation security decision support system for emergency response: A training prototype

S.W. Yoon <sup>a</sup>, J.D. Velasquez <sup>a,</sup>⁎, B.K. Partridge <sup>b</sup>, S.Y. Nof <sup>a</sup>

<sup>a</sup> PRISM Center, School of Industrial Engineering Purdue University, 315 N. Grant Street, West Lafayette, IN 47907, USA

<sup>b</sup> PRISM Center, INDOT Research Division, P.O. Box 2279 West Lafayette IN 47906, USA

## a r t i c l e i n f o

Article history: Received 30 August 2007 Received in revised form 29 May 2008 Accepted 15 June 2008 Available online 21 June 2008

Keywords: Computer-based training Mock drills Organizational learning

## a b s t r a c t

During emergencies, decision making is a challenging task requiring immediate and effective action from responders under the pressures of incomplete and erroneous information. Identi<sup>fi</sup>cation of appropriate resources and personnel, proper lines of communication, and timely accessibility to relevant procedures can minimize after effects. To achieve emergency response and recovery effectiveness, responders need to be prepared and trained for various emergency situations and decision support systems. To address some of the decision making needs experienced by responders, a low-cost computer computer-based training prototype with a decision support system tool was developed. The emergency training prototype was designed for the Indiana Department of Transportation. Emergency responders' capabilities, collaboration with other agencies, deployment of resources and personnel, implementation of response plans, and use of the chain of command were evaluated. The usefulness of prototype and potential decision making systems for the transportation agency are validated based on several mock drills.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Recent terrorist attacks and natural disasters have brought substantial attention to the role that governmental agencies must play in maintaining national security. Transportation systems are particularly vulnerable to those events due to the system's open and accessible nature; and critical because they serve large numbers of people in extensive networks. Due to the vulnerability and criticality of transportation systems, agencies in the transportation network are in great need to identify their preparedness for all types of emergency situations. Agencies are more than ever being required to examine their preparedness and abilities to respond and recover from such events in a timely manner. Emergencies can radically affect transportation operations; and consequently, public safety, national security, and the economy. Situational awareness, alertness to suspicious activities, and the preparedness of transportation agents as <sup>fi</sup>rst responders are critical to mitigate the often negative effects of emergencies.

During emergencies, transportation agents need to assess the emergency and provide immediate response such as public broadcasting messages, road closures, alternative detours, debris removal, etc. Decision making under such circumstances is dif<sup>fi</sup>cult to structure and implementation of existing plans is usually not adequate for the emergency. Furthermore, the vast amount of incident information received and the vast number of emergency resources and personnel needed complicates the decision making process even further. In the work by Mendonca, the author provides a set of requirements for computer-based systems to support decision making and improvisation in response to extreme events, similar to the types of events simulated in this work, and using as reference the events of September 11 [14]. Transportation agents need to become familiar with the dynamic nature of the emergency scenario including: emergency response plans, situation assessment, resource deployment, emergency cooperation, and inter-agency collaboration.

A decision support system for emergency response was developed to assess the state of preparation of a transportation agency to respond to emergencies, enable the development of new Standard Operating Procedures (SOPs), and to better train and empower employees in the decision making process. The system was developed by the Production, Robotics, and Integration Software for Manufacturing and Management Systems (PRISM) Center at Purdue University in cooperation with the Operations and Research Departments of the Indiana Department of Transportation (INDOT), the Indiana State Police (ISP), and the Indiana Department of Homeland Security (IDHS). Furthermore, the usefulness of a decision support system as a training tool to identify the strengths and weaknesses of the emergency responses and the transportation operations is also examined in this research.

The remainder of this article is organized as follows. Section 2 provides background on transportation security and training for emergency response. In Section 3, the decision support system for emergency response is described in more detail. Section 4 discusses the implementation of the prototype in a mock drill environment. In Section 5, evaluations by mock drill participants are summarized.

## 2. Background

The ever-changing nature of today's world has switched the focus of responding to events, “new realities are now making strategy itself appear obsolete, turning businesses into adaptive systems that remain alert to shifting paradigms and play-out different scenarios in a sense-and-respond mode” [13]. From 1998 through 2000 more than 65,000 emergency responders were trained, meanwhile in 2004 alone over 386,000 responders were trained with support from the Homeland Security Department spending over \$200 million on their training. The training guarantees that employees are able to respond to changing environments and assuring that they are able to stay alert to new threats [7]. However, the majority of training time focuses on acquiring skills and information through lectures and demonstrations, with the least amount of training time devoted to validating the skills sets in live environments [17]. The literature indicates that computer-based virtual environments can help trainees gain familiarity with the decision making process and acquire skills interactively.

The Defense Advanced Research Projects Agency (DARPA) had, after the events of September 11, the “goal of empowering users within the foreign intelligence and counterterrorism communities with IT so they could anticipate and ultimately preempt terrorist attacks by allowing them to <sup>fi</sup>nd and share information faster, collaborate across multiple agencies in a more agile manner, connect the dots better, conduct quicker and better analyses, and enable better decision making” [18]. An experiment conducted using information technology tools developed by DARPA showed the value of incorporating such tools in order to invert the trend by which most time in the decision making process is spent doing research and producing reports and documents, rather than on analyzing the information available (i.e., time spent in research was reduced from 330 h to 76) [18].

The timely availability of information guarantees that the decisions made by responders effectively meet the requirements of the event while reducing waste, duplication, errors and con<sup>fl</sup>icts. Access to a decision support system provides a decision maker with the ability to (1) identify, secure and deploy the correct number and types of resources in realtime; (2) determine the current inventory of available resources, personnel and their location; (3) review historical records of similar or related events; (4) store on-time decisions for further review and the creation of organizational memory system. In a highly distributed organization such as a state department of transportation, a decision support system functions as a data warehouse to serve all the functions discussed previously. Furthermore, it also enables all members of the distributed network to access in a timely manner the information anytime and at any location in the state.

The value of real-time and supported decision making depends on the ability of organizations to quickly respond to emergencies and adapt to changes such as technological advances, growing and changing customer demands, changes in the labor force, environmental and political concerns, societal impacts, security concerns and many others [1]. Modeling and simulation of emergency response has been identi<sup>fi</sup>ed as critical for organizations for many years [9]. However, it has not been until recently that the focus has shifted from purely modeling the emergency event to a more holistic approach of examining all aspects of emergency response from awareness to response evaluation and decision making. A recent report by the Committee on Science and Technology for Countering Terrorism of the National Research Council identi<sup>fi</sup>ed “systems analysis, modeling and simulation” as the <sup>fi</sup>rst of seven crosscutting challenges to be addressed in countering terrorism [16].

There are several on-going projects that focus on simulation for studying disasters as well as their effects and they include: emergency response planning, emergency response training, identi<sup>fi</sup>cation and detection, among others. In emergency response planning, tools have allowed for the evaluation of strategies to respond to a disaster event, for example, map analysis software that can be used to plan responses to events such as a forest <sup>fi</sup>re. In emergency response training, Sandia National Laboratories for instance has developed a program called Weapons of Mass Destruction Decision Analysis Center, to simulate war-room environments in the event of a terrorist attack, to train public of<sup>fi</sup>cials [20]. Another simulation system developed for emergency response training, a virtual reality application, immerses <sup>fi</sup>rst responders in a computer-simulated setting in which a biological warfare agent has been dispersed through a terrorist bomb [19].

A comprehensive framework has been recommended to integrate modeling, simulation and visualization tools for emergency response by including planning, vulnerability analysis, identi<sup>fi</sup>cation and detection, training and real-time response support [8]. An example of one such system is CICERO, a computer-based incident management system using the Internet and networks to communicate and coordinate across the organization [11].

## 3. Decision support system for emergency response

Decision support systems (DSS) are designed to assist decision makers with a particular complex problem in a computer-based environment. Initially, decision support systems were conceived as a storage database for relevant decision information [21]. Nowadays, decision support systems help decision makers' access and understand data and its signi<sup>fi</sup>cance, as well as the implications of their judgments regarding that data, in an effort to assist them in making more educated decisions with the information given [4]. A decision support system for emergency response and management however, must be tailored to affect the decision making and behavior of the organization and it is often the case that it needs to support operational, tactical, and strategic decision making [5]. Decision support systems can be used to reduce the time to make critical decisions among them task assignment and resource allocation but also to guide long-term decisions, training and the command and control capabilities of the organization [22].

A decision support system-of-systems has been developed for transportation agents to be trained in various transportation emergency situations and assess their response readiness by simulating, preparing and responding to simulated realtime events. The decision support system enables decision makers' access to data distributed throughout the network and spanning many departments within the agency. A similar system but for a different context, “FALCON” has been designed to assist emergency organizations with environmental management decisions by integrating chemical inventories information, security, health readiness and population demographics into one information system and allow for assessment of response readiness, training and security [6]. The design of a decision support system for resource intervention in real-time emergency management due to the importance of transport infrastructure and its role in emergency resource intervention and population evacuation has been provided by Mincardi et al. [15].

The decision support system (DSS) developed was divided into several information areas for each of the available districts, containing information that was relevant to the respective district and also incorporating both a bottom-up approach (information related to the actual state of events communicated by <sup>fi</sup>rst responders) and a top-down view to the decision making process (information regarding policies by the decision makers). The decision support content areas integrated were: resources, communication contacts, maps, ITS/weather, and plans and procedures. The system developed functions similarly to the group decision support system (GDSS) for con<sup>fl</sup>ict decisions de<sup>fi</sup>ned by Zhuge [23] as it requires continuous decisions, cognitive cooperation from the participants and has to support dynamic scenarios.

## 3.1. Resource information support

During emergencies, decision makers face the challenge of identifying, securing and procuring the right type and number of resources to respond to an event. The resource function allows decision makers to access in real-time, information stored in the resource database to address equipment demands. Among the information included in the database are a comprehensive inventory of vehicles, machines, and equipment organized according to the purpose categories to which they belong. Once the user is faced with a resource procurement decision regarding the on-going emergency event, it must select the district, category, number and the type of equipment to deploy. The resource information decision support system in-turn provides the user with the number of resources available in each sub-district that matches the criteria selected. A user can select and request the deployment of the resources needed and identify the contact information, at the sub-district, district and central of<sup>fi</sup>ce levels to request it from. The resource information is provided to the user to guarantee an expedited process in securing and procuring the resources needed to handle speci<sup>fi</sup>c emergency scenarios. The user can also request resources to be transferred or moved from one sub-district to another by identifying the type, number, district and subdistrict. Finally, a log of all requested resources is kept to better track the number and type of resources requested, resources already assigned, resources released, or resources being transferred in order to minimize resource waste, duplication, errors and con<sup>fl</sup>icts (Fig. 1).

![](/api/attachments/S695SMGU/fulltext/images/6f7c9d93ec107dd8f6ea6e79084b68a3526a749fa75efef2e3e03cfbecb56708.jpg)  
Fig. 1. Resource information support.

## 3.2. Communication information support

Identi<sup>fi</sup>cation of organizational contacts with whom to collaborate during an emergency poses a signi<sup>fi</sup>cant challenge to decision makers due to their availability, and organizationally de<sup>fi</sup>ned roles and responsibilities. The communication decision support function enables the user to access contact information for all employees at the district/subdistrict levels as well as the central of<sup>fi</sup>ce in order to coordinate emergency response efforts and follow the proper lines of emergency communication. The information provided includes an individual's position in the organization and his/ her contact phone-numbers, email and availability during the day. The system enables the user to search three levels deep into the organizational tree to <sup>fi</sup>nd backup personnel inside the organization to communicate with in case other decision makers are unavailable at the time of the emergency (Fig. 2). By having real-time access to the contact information of all employees, a decision maker is able to reduce the time to identify emergency contacts and guarantee that the required organizational lines of communication are followed.

## 3.3. Map information support

Emergency events for transportation organizations usually require the closure of roads, identi<sup>fi</sup>cation of alternative traf<sup>fi</sup>c routes, and deployment of heavy duty machinery among many others. This decision support function enables decision makers to access all state, districts, and sub-district maps (to the mile-marker level) and make an informed decision regarding the best roads and routes for traf<sup>fi</sup>c and emergency personnel during an event. The maps are of signi<sup>fi</sup>cant importance in the case that traf<sup>fi</sup>c needs to be re-routed (e.g., <sup>fl</sup>ooding, bridge collapse) or resources need to be reallocated within districts or sub-districts. Furthermore, the

![](/api/attachments/S695SMGU/fulltext/images/ea6c18deddecb9075b22f0cb2dcce09fe2c31cebf79ebfc2aa3e7ac970f94325.jpg)  
Fig. 2. Communication information support.

![](/api/attachments/S695SMGU/fulltext/images/7e581f27695c659be07872fc22c2502b7a6a04629531d9d10146ed4531a0dae5.jpg)  
Fig. 3. Map information support.

maps also help a decision maker better identify the correct location of the events in order to better determine access roads to get to the location, help identify communities that might be affected by the events and notify other governmental agencies and sub-districts that need to be informed (Fig. 3).

## 3.4. ITS/weather information support

Current weather conditions and traf<sup>fi</sup>c at the location of an emergency event can positively or negatively affect the resource deployment, personnel availability, road closures and/or traf<sup>fi</sup>c re-direction decisions. Weather information allows users to identify the conditions in the area to be able to determine the operability of the roads in order to assess the safest way to direct traf<sup>fi</sup>c or schedule operations such as rerouting of vehicles, snow removal, or closure of roads. In addition, Intelligent Transportation Systems (ITS) information, in the form of video footage from different locations throughout the state and dynamic message signs, is incorporated to provide decision makers with real-time feed and the ability to better inform communities of current emergency conditions at those speci<sup>fi</sup>c locations via dynamic message signs (Fig. 4). The ITS/weather information decision support system empowers a decision maker with critical transportation infrastructure information to ensure that decisions regarding equipment and personnel deployment, road closures, traf<sup>fi</sup>c re-direction and others are not hindered by external forces outside of the decision makers control such as weather or traf<sup>fi</sup>c congestion.

![](/api/attachments/S695SMGU/fulltext/images/d45b8cfd4a0add342dd8084cbdc701e67222708ee61c7a83b61419f4bae95070.jpg)  
Fig. 4. ITS/weather information support.

![](/api/attachments/S695SMGU/fulltext/images/7afbc8eeee6d97b8f3eabb388b7cd982ae0d817f5e8df4c398a33c1bc5f1c3d8.jpg)  
Fig. 5. Plans and procedures information support.

## 3.5. Plans and procedures information support

To safeguard the safety and security of all stakeholders during an emergency, it is necessary for an organization to follow established policies and procedures, if they have been developed. Sometimes the documents that need to be accessed are distributed throughout the network and therefore access to it is limited; unless they are centrally located and in a format that is accessible by all members of the network, at any time and from any place, their applicability is limited. Having timely access to the different sets of organizational procedures for emergency response enables decision makers to validate if the actions taken are in accordance with de<sup>fi</sup>ned organizational response guidelines. This function enables users' electronic access to regularly accessed procedural documents used by members of the organization. Furthermore, having access to the set of plans and procedures enables individuals that may have not been trained on emergency response but that are being required to act as if they were, the necessary information to make informed decisions and reduce their potential for errors. Among the documents included in this prototype were: a comprehensive emergency management plan, emergency operations plans, an incident command system plan, district speci<sup>fi</sup>c emergency operations plans, HAZMAT operations procedures and alert bulletins (Fig. 5).

The overall system architecture is depicted in Fig. 6.

## 4. Implementation of transportation security decision support system: a case study

To assess the effectiveness of the decision support system as a training tool and a valuable decision making tool to be implemented by the organization, a total of four transportation security mock drills have been conducted in a time span of two years with participation and cooperation from the Indiana Department of Transportation (INDOT), the Indiana Department of Homeland Security (IDHS), the Indiana State Police (ISP), and the Department of Natural Resources (DNR). Each mock drill included participation from different Indiana districts, with a total participation of 114 transportation agents throughout the four mock drills. By applying preplanned response strategies and action plans, pre-implemented functions and databases, maps and visuals, communication, facilities and equipment for emergency plans, participants selected or elaborated their best actions to deal with the emergency scenario.

A series of concurrent and sometimes interrelated emergency events were distributed to the participating teams and stored in a central database. The emergency scenarios were a combination of daily traf<sup>fi</sup>c occurrences (i.e., road constructions, automobile collisions), extraordinary incidents (i.e., terrorist threats and natural disasters), and simultaneous occurrences of different types of emergency events<sup>1</sup>. Not all events required a decision or action by the teams; rather it was dictated by the location and proximity of the district (team) to the unfolding events. Once the transportation security exercise started, the database released the series of emergency events to the distributed teams, based on a preprogrammed sequence and time interval. The computer screen was divided into two regions: (1) the left region provided the teams with all the relevant information regarding the events, hints that had been previously determined by users as possible actions, and an interface for the team to type their actions and the means by which they were to communicate with others, and (2) the right region which provided access to all the different decision support systems previously de<sup>fi</sup>ned. During the speci<sup>fi</sup>ed time periods for making a decision, each team analyzed the given incident, discussed their response plans, accessed any/all the different decision support systems available to them and determined their actions to prepare, mitigate or respond to the emergency. Once a decision had been reached by the members of a team, if the event affected them, a designated team member would enter the decision or series of decisions into the computer. Once a decision had been entered by a team, it was shared to all other teams simultaneously for them to react. Simultaneously, and in a different computer or tv screen a team was able to view all the decisions that other involved districts were making.

![](/api/attachments/S695SMGU/fulltext/images/17a91e18072c8119cdb8447f6412f4ffde8d30d4d9de89579fc7de39c7659de2.jpg)  
Fig. 6. Architecture of transportation security training for emergency response.

The mock drill teams included representatives from participating transportation districts, and representatives from ISP, IDHS, DNR and the Counter-Terrorism task force, invited to serve in the evaluation process. An evaluation teamwas formed to oversee the entire training drill with representatives from all the agencies included. Emergency events unfolded at speci<sup>fi</sup>c times to guarantee that teams had enough time to discuss and agree on the decision to activate or deploy resources. At any given time, drill participants had access to the decision support systems in order to make decisions about emergency personnel availability, equipment inventory, weather and traf<sup>fi</sup>c conditions and existing plans and procedures.

The entire drill was monitored closely and assessed by the evaluation team. Team decisions and actions during the drills were stored in an outcome database for further review, discussion, feedback and recommendations during the postanalysis. Failure to record information for subsequent use or post-incident analysis has been identi<sup>fi</sup>ed as a critical problem in emergency responses [11].

## 4.1. Critical objectives of transportation emergency operations

The objectives of the transportation security mock drills were to enable the Indiana Department of Transportation become better prepared for large-scale emergencies. Gaps and shortcomings in the current preparedness of INDOT for preparing, managing, mitigating and responding to critical security emergencies were identi<sup>fi</sup>ed. The critical objectives regarding emergency operations preparedness identi<sup>fi</sup>ed by INDOT and the research team included:

1) Enhance inter-agency communication,

2) Enable collaboration with other state agencies

3) Better management of resources and personnel deployment,

![](/api/attachments/S695SMGU/fulltext/images/dfaae209243dd529af756d09e1e6b36e702a9580333fc63f01c94bf961ba809f.jpg)  
Fig. 7. Decision/action-level performance evaluation about MDI objectives.

4) Assessment of standard emergency procedure implementation (e.g., standard operations procedures (SOP), response plans (RP)),

5) Enhance quality of agency chain of command/team building,

6) Better public communication.

In order to assess INDOT's performance regarding the six objectives, a checklist was provided to the evaluation team for all the events. Each evaluator was required to complete the checklist for each event based on his/her observation of the decision making process during the drill. Most of the evaluation questions required the responder to answer “Positive” or “Negative” due to the time constraints and in order for the evaluators to scrutinize participants' performance intensively.

## 4.2. Analysis of emergency response performance

A total of 192 evaluation checklists were collected from the two most recent mock drills. In order to systematically analyze INDOT's emergency response performance, evaluation questions were further classi<sup>fi</sup>ed according to the six critical objectives of emergency operation and the overall assessment was as follows.

Fig. 7 summarizes the decision/action-level performance evaluation for the six critical objectives and the overall assessment of the drill. Speci<sup>fi</sup>cally for emergency operation objective 3, better management of resources and personnel deployment, 90% positive responses indicate that drill participants deployed necessary resources and personnel appropriately and effectively from the evaluators' point of view. The lowest positive responses were obtained by objectives 1, enhance inter-agency communication and 6, better public communication, which indicates that those two areas need to be enhanced.

## 5. Opportunities of transportation security improvements

To ful<sup>fi</sup>ll the transportation security training objectives, opportunities for emergency operation improvements have been identi<sup>fi</sup>ed along with critical emergency operation aspects to be included based on post-analysis and evaluation processes.

1) Inter-agency communication: each agency needs to clarify their responsibilities, communication <sup>fl</sup>ow structure, and information sharing and veri<sup>fi</sup>cation procedure with interagencies.

2) Collaboration with other state agencies: more structures/ procedures at local and state levels for contacts and responsibilities need to be designed.

3) Resources and personnel deployment: consistency on equipment identi<sup>fi</sup>cation for agencies, and resources and personnel sharing procedures need to be improved.

4) Standard emergency procedure implementation: actions/ decisions made by training teams were not based on the existing plans/operating procedures. More de<sup>fi</sup>ned SOPs, checklists, continuity of operations plans, standard tracking charts, and reporting forms need to be included in the decision making process.

5) Agency chain of command/team building: a clear chain of command needs to be built. The roles and responsibilities of teams and incident commanders need to be considered when an emergency unfolds.

6) Public communication: early activation of public communication is the key to mitigate emergency effects.

## Table 1

Overall evaluation of transportation security training with TSTP

<table><tr><td>Assessment factor</td><td>Average ratinga</td></tr><tr><td>a. The drill was well structured and organized</td><td>3.93</td></tr><tr><td>b. The amount of time for the drill was appropriate</td><td>3.48</td></tr><tr><td>c. The drill scenario was plausible and realistic</td><td>3.73</td></tr><tr><td>d. The decision support system was a valuable tool to support the drill</td><td>3.56</td></tr><tr><td>e. Hints for actions/decisions were valuable</td><td>3.32</td></tr><tr><td>f. Participation in this drill was appropriate for someone in my position</td><td>4.36</td></tr><tr><td>g. The participants included the right people in terms of level and mix of disciplines</td><td>4.02</td></tr><tr><td>h. The drill provided a good opportunity to enhance my performance during emergencies</td><td>4.02</td></tr></table>

<sup>a</sup> Rating of satisfaction was scaled from 1 (strongly disagree) to 5 (strongly agree).

The mock drills were found to be educational and valuable by the training participants and highlighted the need for continuous training to better meet the requirements of employees to make more educated decisions under emergency pressures. Training participants considered that their inclusion in the mock drills was adequate and that the mix of decision makers was a good re<sup>fl</sup>ection of real life emergency scenarios. Participants considered that transportation security training mock drills provided a good opportunity for them to enhance their decision making performance and be better prepared to deal with emergencies (Table 1). The majority of participants recommended that similar mock drills should be conducted at least once a year (85% of respondents) with 62% of responders suggesting that at least two mock drills be conducted in a given year.

## 6. Conclusions

The transportation security decision support system was designed as a low-cost, useful opportunity to verify a transportation agency's capabilities, procedures, and preparedness to handle a simulated emergency situation, involving a combination of terrorist attacks, natural hazards (snow), and severe traf<sup>fi</sup>c accidents. It also enabled observation and self-examination of strengths and weaknesses in managing, preparing and responding to a series of security emergency scenarios. It is anticipated that the tool will be employed again by other organizations after additional changes are made based on input from all users. Some of the changes to be implemented will include an optimization interface to provide users with information on how to minimize costs and transportation time from and to event locations, and expanding the DSS capabilities to include other agencies' resource constraints. Also being considered is the deployment of the training tool using the Web similarly to the TeamSpirit group decision support system (GDSS) tool developed by Chen et al. [2]. The DSS tool originally was developed for DOT use, but with <sup>fi</sup>nite resources and some agency overlap in responding to an emergency, extending the DSS to encompass multiple agencies is a logical extension. The use of the tailored training tool enables the DOT to better train its employees and be able to meet the speci<sup>fi</sup>c requirements of the agency at the same time: this level of customization leads to better decision outcomes and decision processes as identi<sup>fi</sup>ed by Limayem et al. [12]. A similar yet limited optimization extension, a decision support system that integrates mathematical models, rules and algorithms in a user-friendly format to minimize incident response time has been developed and successfully implemented for response to roadway network incidents [24]. In other work with similar DSS goals, an integrated DSS and expert system (ES) for service network planning was built and implemented for a major air-express courier [3].

Based on the feedback provided by all participants, the decision support tool was shown to have improved the communication within the organization when responding to emergency events by better identifying with whom to communicate, the most appropriate resources and methods to secure effective communication, the best actions to be followed and the procedures and plans to follow in order to mitigate emergency events. By identifying the appropriate people with whom to communicate inside the organization, the correct information to share, and the ways by which to share it, an organization can create lines and backups of communication and command to better serve the mission of the organization and guarantee that errors and con<sup>fl</sup>icts are avoided. For further validation of the decision support system presented in this work, an assessment instrument will need to be developed for the next iterations of the mock drill that takes into consideration the work by Kim et al. [10] and their eight constructs for critical incident management systems.

## Acknowledgments

Research reported in this article has been supported in part by JTRP/INDOT funds and by the PRISM Center at Purdue University. The authors also wish to thank several colleagues who have participated in this research: J. Poturalski and T. Shield from INDOT; K. Woodall from IDHS; X. Chen, H.S. Ko, and W. Jeong from the PRISM Center at Purdue University.

## References

[1] D. Bhatt, J. Zaveri, The enabling role of decision support systems in organizational learning, Decision Support Systems 32 (3) (2002).

[2] M. Chen, Y. Liou, C.-W. Wang, Y.-W. Fan, Y.-P.J. Chi, TeamSpirit: design, implementation, and evaluation of a web-based group decision support system, Decision Support Systems 43 (4) (2007).

[3] W. Cheung, L.C. Leung, P.C.F. Tam, An intelligent decision support system for service network planning, Decision Support Systems 39 (3) (2005).

[4] S. French, Decision Analysis and Decision Support, John Wiley and Sons, 2004.

[5] S. French, M. Turoff, Decision support systems, Communications of the ACM 50 (3) (2007).

[6] S. Frysinger, M.L. Deaton, A.G. Gonzalo, A.M. VanHorn, M.A. Kirk, The FALCON decision support system: preparing communities for weapons of opportunity, Environmental Modeling and Software 22 (4) (2007).

[7] M. Hall, War on Terror Takes on a Thankful Town, USA Today, 2005.

[8] S. Jain, C. McLean, A framework for modeling and simulation for emergency response, Proceedings of the 2003 Winter Simulation Conference, 2003.

[9] T. Kanno, K. Furuta, Modeling and simulation of inter-and intraorganizational communication and coordination in emergency response International Journal of Emergency Management 3 (2–3) (2006).

[10] J.K. Kim, R. Sharman, H.R. Rao, S. Upadhyaya, Ef<sup>fi</sup>ciency of critical incident management systems: instrument development and valida tion, Decision Support Systems 44 (1) (2007).

[11] C. Ledger, B. Turner, Computer assistance to communication and coordination during emergencies Proceedings JEEE 35th Annual 2001 International Carnahan Conference on Security Technology, vol. 42–44, 2001.

[12] M. Limayem, P. Banerjee, L. Ma, Impact of GDSS: opening the black box, Decision Support Systems 42 (2) (2006).

[13] G.Y. Lin, R.E. Luby Jr., K.Y. Wang, New model for military operations, ORMS 31 (6) (2004).

[14] D. Mendonca, Decision support for improvisation in response to extreme events: learning from the response to the 2001 World Trade Center attack, Decision Support Systems 43 (3) (2007).

[15] R. Minciardi, R. Sacile, E. Trasforini, A decision support system for resource intervention in real-time emergency management, International Journal of Emergency Management 4 (1) (2007).

[16] National Research Council, Making the Nation Safer: the Role of Science and Technology in Countering Terrorism, National Academies Press Washington DC, 2002.

[17] K. Ozbay, New frontiers in emergency and incident management training, TR News 238 (2005).

[18] R. Popp, T. Armour, T. Senator, K. Numrych, Countering terrorism through information technology, Communications of the ACM 47 (3) (2004).

[19] Sandia National Laboratories, Virtual Reality Training Tool Pits Rescue Teams Against Computerized Attack, 1999.

[20] San Francisco Chronicle, Software Simulated Terror Hit — Sandia Develops Program as Tool for Public Of<sup>fi</sup>cials, , 2002.

[21] M. Silver, Systems that Support Decision Makers, John Wiley and Sons, 1991.

[22] S. Thompson, N. Altay, W.G. Green III, J. Lepetina, Improving disaster response efforts with decision support systems, International Journal of Emergency Management 3(4) (2006).

[23] H. Zhuge, Con<sup>fl</sup>ict decision training through multi-space cooperation, Decision Support Systems 29 (2) (2000).

[24] K.G. Zografos, K.N. Androutsopoulos, G.M. Vasilakis, A real-time decision support system for roadway network incident response logistics, Transportation Research. Part C 10 (2002).

Juan Diego Velasquez received his B.S. degree in 1998, his M.S. degree in 2003 and is completing his Ph.D. degree all in the Department of Industrial Engineering at Purdue University, West Lafayette, IN. He has been working at the Production, Robotics, and Integration Software for Manufacturing and Management (PRISM) Center since he started his Ph.D. in 2003. His research interests include protocol de<sup>fi</sup>nition for organizational activities, scheduling algorithms, decision support systems and organizational learning methods.

Sangwon Yoon is a Ph.D. candidate in the school of Industrial Engineering at Purdue University. He is a member of the Production, Robotics, and Integration Software for Mfg. Management Center (PRISM). His research interests are in the areas of enterprise collaboration, production and operations management, information system integration, and decision support systems. He has worked on several industry projects regarding total quality management, enterprise resource planning, enterprise information management, and transportation safety and security.

Barry K. Partridge is the Director of the Indiana Department of Transporta tion Research and Development Of<sup>fi</sup>ce and a licensed Professional Engineer. Dr. Partridge received his Ph.D. in Civil Engineering from Purdue University specializing in Environmental Engineering and has thirty years experience in the transportation <sup>fi</sup>eld and twenty-four years experience in transportation research. Dr. Partridge has served on various national committees including the AASHTO Research Advisory Committee and the Transportation Research Board and is the author/co-author of numerous articles related to transportation environmental issues, bene<sup>fi</sup>cial reuse of waste materials and transportation security issues.

Shimon Y. Nof is a Professor of Industrial Engineering at Purdue University, has held visiting positions at MIT and universities in Chile, EU, Hong Kong, Israel, Japan, and Mexico. Director of the NSF-industry-supported PRISM Center for Production, Robotics and Integration Software for Manufacturing and Management; he is a Fellow of IIE, Secretary General of IFPR, and current Chair of IFAC CC — Manufacturing and Logistics Systems. He has published over 250 articles on production engineering and information/robotics engineering and management, and is the author/editor of nine books in these areas. In 1999 he was elected to the Purdue Book of Great Teachers, and in 2002 he was awarded the Engelberger Medal for Robotics Education. Professor Nof has also had over eight years of experience in industry positions.
