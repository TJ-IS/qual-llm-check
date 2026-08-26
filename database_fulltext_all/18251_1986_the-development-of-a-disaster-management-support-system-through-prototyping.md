---
otero_id: 18251
otero_key: "9D5PRNVX"
title: "The development of a disaster management support system through prototyping"
authors: "Salvatore Belardo; Kirk R. Karwan"
year: "1986"
journal: "Information & Management"
doi: "10.1016/0378-7206(86)90051-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Development of a Disaster Management Support System Through Prototyping

Salvatore Belardo

School of Business Administration, State University of New York at Albany, BA 310 Albany, NY 12222, USA

and

Kirk R. Karwan

Fuqua School of Business, Duke University, Durham, NC 27706, USA

The authors discuss the development of a disaster management decision support system through the use of a prototyping strategy. The system was designed to aid a Regional Emergency Medical Organization in establishing an effective means of dealing with multiple casualty emergencies. Prototyping proved to be an appropriate development approach, promoting a high level of user involvement and interest in a setting where tasks were somewhat ill-structured and the problem and associated decision rules not well understood. The authors conjecture that their approach will work well in the development of similar systems for other crisis on disaster managers. The limitations of the study are also discussed.

Keywords: Prototyping, disaster management, emergency management, information requirements, system development, heuristic development, microcomputers

![](/api/attachments/9D5PRNVX/fulltext/images/401671a342cf3a322e8389fffbcc4731490fe90c119cfab9f65adb4c76055640.jpg)

Salvatore Belardo is Associate Professor and Chairman of the Management Science and Information Systems Department at the State University of New York at Albany. Dr. Belardo received his BSME from Rochester Institute of Technology, his MBA from SUNY-Albany and an M.S. and Ph.D. from Rensselaer Polytechnic Institute. He is the director of the university's Center for Disaster Management and a consultant to industry and government. He is currently working with

developing nations to provide industry and commerce with computer applications and programs.

## 1. Introduction

We have learned to cope with natural and man-made disasters in a variety of ways. Yet the development of sophisticated systems to support disaster management decisions is a relatively recent interest of public and private groups. This newly found concern can be attributed to a number of factors, the most prominent of these being; (1) a greater public awareness of disasters created by media coverage, (2) the widening use of computer systems in public management and (3) the recent and continuing developments in information and communications technology.

In developing computerized support systems for disaster management, it is apparent that much of the earlier work in areas such as police and fire protection can offer some guidelines (e.g. [8,12]). On the other hand, since floods, nuclear power plant accidents, chemical explosions, etc. are so much more rare than the “routine” events that require public service, some gaps do exist in our knowledge regarding how best to support disaster management decisions. Furthermore, since these events are so unusual, there has been little incentive to develop sophisticated and potentially expensive control mechanisms.

![](/api/attachments/9D5PRNVX/fulltext/images/558e6fea990c386802a92a4ee391cdfee902ecdcf0dcf415afd2afff7d067898.jpg)

Kirk Karwan is an Assistant Professor in the Fuqua School of Business at Duke University. He received his B.E.S. and M.S.E. degrees from the Johns Hopkins University and his Ph.D. from the Carnegie-Mellon School of Urban & Public Affairs. He previously taught at Tulane University and worked as a Systems Analyst for the U.S. Coast Guard. His current research involves the design and implementation of computerized information and decision support systems in the areas of crisis management and production planning and control.

In light of this, it is not surprising that some of the difficulties in developing disaster management support systems are uncharacteristic of more common decision environments. For example, the determination of information requirements is an extremely difficult task even though disaster management procedures appear to be fairly well defined. Also, although prototyping has proven to be a sensible approach to system development in this type of setting [4], rapid prototyping seems to be neither viable nor desirable. Finally, the eventual definition of most disaster management support systems will no doubt have to await some future developments or changes in hardware, software and communications technology.

In this paper, we will demonstrate the validity of these assertions in regard to the development of one particular disaster (or emergency management) decision support system. The system that will be described has been developed over a two year period for a regional emergency medical organization in upstate New York. Though some of our experiences with this system are no doubt unique to the chosen environment, we are confident that many of them are also generalizable to most disaster management situations. In fact, as will be discussed in section 5, most of the major differences in our experience with developing this system appear to be the result of environmental differences, i.e., since disaster management problems themselves are relatively rare (by definition) and are subject to considerable public scrutiny.

## 2. Multiple Casualty Response

In most medical emergency situations (i.e., heart attack, auto accident, etc.) individual ambulance and/or fire department emergency service provider agencies can respond quickly and effectively. However, in the event of a large fire, an explosion, a plane crash or a train derailment, the capabilities of any one agency are typically inadequate. In such situations, the activities of various provider agencies need to be coordinated.

In responding to this need in the Albany, New York area, the Regional Emergency Medical Organization (REMO) has been engaged in an ongoing effort to develop procedures to address problems brought about by multiple casualty situations. The region serviced by REMO consists of six counties (Albany, Columbia, Greene, Rensselaer, Saratoga, and Schenectady) covering 3,500 square miles (5631 km $^{2}$ ) and with a population of over 860,000 people. Service is provided by 135 emergency medical service (EMS) agencies. The equipment located at each agency site varies in number and type as well as communications capabilities. Some sites have only one Basic Life Support ambulance available while others may have a combination of Basic Life and Advanced Life Support ambulance with voice and telemetry transmission capabilities. The majority of the more than 78,000 calls for emergency medical assistance that are received each year can be adequately handled by the individual EMS provider agencies or by several agencies working together. It is during a multiple casualty emergency situation, however, that a system for deploying resources and providing backup ambulances to those agencies stripped of their resources is needed.

## 3. The Prototyping Approach

A number of systems design techniques were considered for developing a multiple casualty response system. After some deliberation with New York State Office of Emergency Preparedness and REMO officials, a strategy was selected that would enable dispatchers to evaluate a series of working decision aids. This design strategy, known as prototyping, has proven to be useful across a wide range of information systems' applications. In general, prototypes have been shown to:

(1) improve the likelihood of developing systems actually desired by users,

(2) shorten the overall development period,

(3) reduce management risk.

(4) serve as specifications for further (later) system development.

See, for example, [2,7,9], for more detail.

In our opinion, the first of the above points was perhaps the most important advantage of the approach. As Davis [10] notes, prototyping makes sense when there is substantial uncertainty in information requirements due to a lack of user experience or understanding of the system being designed. In such circumstances, prototyping can help to prevent early (often costly) specification errors in systems development [5,16]. Much of this is due not only to increased involvement by users in detail development but also to the fact that prototypes can help to stimulate users' interest and managerial dedication to the system. Maintaining user interest and involvement was paramount in the development of our system since skepticism was evident among dispatchers who drew heavily on their experience in making decisions during emergencies.

## 4. System Development

## 4.1. The Basic Approach

The Multiple Casualty Computer Aided Dispatch System (MCCADS) was developed over a two year period using a micro-computer based prototyping strategy for information assessment. The MCCADS prototyping strategy that we will describe mirrors the approach of Naumann and Jenkins (1982). Figure 1, adapted from their work, depicts the general iterative approach that was used. In particular, an initial prototype system (version 0) was developed based upon a fairly limited knowledge of the system's requirements. After testing this prototype to determine requirements more precisely, a second working prototype (version 1) was established. The remaining steps involved further refinements to working versions of the system.

Observe that, in our approach, we did not seek to establish a working system during initial definition and design. At the outset, it was apparent that too little was known about information and system requirements to adequately define a working prototype. For this reason, it was intended that the initial prototype be employed for the purpose of refining system requirements and to pique interest in the entire project.

![](/api/attachments/9D5PRNVX/fulltext/images/980435b0114812832e07aa03732d954c4756e5226901f65ed1450410bf1b738b.jpg)  
Fig. 1. MCCADS Prototyping Strategy (adapted from [18]).

## 4.2. The First Prototype: Definition Phase

In our initial attempts to develop a system, we held discussions with REMO officials and representatives of the local (Albany) disaster management community to ascertain the procedures used to make decisions concerning the deployment of resources. We then designed a prototype system to determine if we understood the problem and whether the system components contained in the prototype adequately fulfilled the managers needs. This “Version 0” prototype, which we also entitled EMDSS (Emergency Medical Decision Support System), was then evaluated in a field setting by ten individuals of the REMO control center and training facility in Colonie, New York.

The results of the field experiment (discussed in greater detail in [3] provided several specific insights into the decision process employed by REMO dispatchers. Tests administered to assess opinions about the various components and features of a DSS for multiple casualty response (both before and after the experiment) showed that data retrieval was considered to be the single most important feature. This was an expected result. On the other hand, despite the fact that emergency dispatchers typically employ standard road maps as tools, the participants indicated that enhanced graphics were not particularly important in their decision processes. In the experiment we observed that their decisions did not involve interacting with supplemental computer generated graphics displays but rather almost exclusively with street maps that were also supplied. The primary reason for this seemed to be the relative lack of sophisticated graphics capabilities available to the participants, i.e., we suspected that interactive graphics capabilities developed subsequent to the field test would probably be better received.

An initial model component of the Version 0 prototype consisted primarily of a bi-objective algorithm that evaluated both total transportation time as well as the maximum time from dispatch to arrival on-scene. The field examination of the prototype showed that those with the model-based component did significantly better in assigning resources than those using traditional manual procedures. Not only were their assignments feasible (i.e., all ambulances assigned, no ambulances used twice) but, later, when all the participants were asked to carefully deliberate and select what they considered to be the most appropriate assignment of resources for each of three scenarios presented, they overwhelmingly chose solutions presented by the computer based bi-objective algorithm.

![](/api/attachments/9D5PRNVX/fulltext/images/e007538c99ec2751b877836b8bf3e85f2d8b125fe7ac5b56d0f47bddee09e68a.jpg)  
Fig. 2. Multiple Casualty Computer-Aided Dispatch System.

Despite this “success” with an algorithmic approach, the tests also revealed that the straightforward use of such a model did not allow for adequate solutions to the problem of deploying resources in response to multiple casualty events. (This will be discussed in more detail in the following subsection.) On the other hand, the use of the normative technique did help the users to focus their attention more directly on the design of the system. Once the dispatchers had seen that they could more adequately respond to emergency situations with the benefit of a computer-based system, they then began to participate in the definition stage to an extent that they had not before. It was only after the field test that they began to describe the decision rules that they employed and the heuristics that they incorporated in their decision processes. As an example, each dispatcher knew that each agency and/or ambulance was capable of different response rates. These rates had never actually been estimated or recorded. In building a system to help them choose ambulances to respond to a multiple casualty incident, it became readily apparent that these “handicaps” would have to be made more explicit.

## 4.3. The Second Iteration: A Working Prototype

REMO headquarters in Colonie is the location of the Regional Emergency Alerting Center (REMAC). This center is staffed by professional dispatchers provided by the town of Colonie Police Department and serves as the central Advanced Life Support frequency monitoring and coordinating center for the entire REMO area. The center was the obvious choice of location for further tests of a centralized computer-based dispatch system.

With the aid of REMAC personnel, a second prototype (Version 1) was developed over a several month period. This system, entitled MCCADS, (Multiple Casualty Computer Aided Dispatch System) is a simple to use, menu driven aid which allows dispatchers to make complicated decisions about areas of the region they do not routinely dispatch for without the assistance of maps.

In developing this prototype several key assumptions and decisions were made. For example, the Universal Transverse Mercator (UTM) grid system was chosen due to the availability of maps for the entire state of New York (which are all on the same scale of 1:2400) and the fact that each is large enough to plot agency base coordinates reasonably accurately. Furthermore, it was decided that during a medical emergency, the agencies contacted initially should be dispatched directly to the incident and that the decision concerning the total number of required ambulances would be made by the commander on the scene (based, for example, on patient condition). Rather than using a preplan set up for say 10, 20, 30 or more patients, it was decided that MCCADS should automatically locate $1\frac{1}{2}$ times the number of ambulances requested by the dispatcher. These ambulances are those closest to the incident (i.e., either by town or village designation or UTM coordinates). A list of the agencies, the number of ambulances available and so forth is provided by the system to the dispatcher who communicates with the various agencies. Once an ambulance is dispatched, the system removes it from the available list until such time as it returns to its base. Those areas which are left without coverage will then be covered by back up units (suggested by MCCADS) which move progressively closer to the incident in case additional units are needed on the scene. This relocation is done by actually sending the cover agency's ambulance(s) directly to the base of the agency it is now covering.

The concept of a handicap was also built into the computer's calculation of distance away from the incident as it ranks the agency bases from nearest to farthest for a particular incident/coordinate location. The handicap represents the average time from receipt of a call until time enroute (i.e., ramp time) plus average transport time.

## 4.4. Data Collection

In addition to the data obtained through the field experiments, data necessary to the development of MCCADS was obtained from various provider agencies. A survey form was designed and sent to all 135 emergency medical service provider agencies throughout REMO's region. The following information was obtained:

1. Agency name.

2. Agency Code Number - 4 digit number assigned by REMO.

3. Street location on a map of each base station - this information was converted to the UTM coordinates on the REMO large maps.

4. Average time off the ramp - used to develop handicap.

5. Number of bases, number of vehicles and type (transport/nontransport) at each base.

6. Agency emergency phone number - although there are a few central county-wide dispatch centers, there still exist a few “Mom and Pop” dispatchers and answering services in the region.

7. Agencies “own choice” of 5 backup ambulances in order to cover their base if they were unavailable. This, of course, takes into consideration previous mutual aid agreements and parochialism, which has developed over time.

The next group of data obtained was the centroid locations for the municipalities throughout the region as a beginning of the location file. This information was provided by the Local Accident Surveillance Project Group of the New York State Department of Transportation, which helped save many hours of plotting coordinates on the over 80 maps of the region.

The software for MCCADS was developed on an Apple IIe micro-computer with two $5_{4}^{1}$ inch floppy disks. One disk contains all of the programs and the other disk contains the permanent agency file (maximum number of agencies is currently 250), the temporary agency file which is copied from the permanent file and manipulated during the execution of the emergency program and the location file (maximum 2,000).

## 4.4. Current Procedure for Using MCCADS

A schematic of the MCCADS system is shown in Figure 2. The dispatcher simply inserts the 2 disks, turns on the computer and is given a menu which includes editing functions, file building functions, copying functions and a “run” emergency program. When the emergency program is selected, the computer automatically copies the permanent agency file into the temporary agency file and the dispatcher is asked the incident location. Any one of the locations in the file may be typed in by name, or the word “coordinates” can be typed and the dispatcher will be prompted for the actual UTM coordinates, which he can obtain from available maps. When the number of ambulances requested is then typed in, an ordered list of agencies with their number of ambulances and first responder vehicles and phone number is provided on both the screen and printer. In the next phase, the screen goes directly down the list giving the dispatcher the opportunity to assign each agency as his phone or radio message to them would determine availability to respond. After the required number of ambulances have been sent to the scene, or a control command is depressed to exit this phase, the next phase is begun. Here, the computer goes down the list of ambulances assigned, giving the dispatcher the pre-plan on who is supposed to be used to cover the vacant districts. Every new list takes into consideration units which were assigned or put off service so that they will not be listed as available again until the dispatcher puts them back in service or the incident is over. The emergency program can be run over again using the same location or any other one should additional ambulances be necessary. When the incident is over, the dispatcher simply “clears all assignments” by erasing the temporary file.

## 4.5. Review and Test of the Second Prototype

The second prototype was tested at REMAC using a number of fairly simple scenarios. The most complex test involved a (fictitious) situation where a university fieldhouse in the area partially collapsed. In this scenario, the local fire department that was initially contacted set up a command post near the fieldhouse and requested 20 ambulances from REMAC. During the test, the REMAC dispatchers employed MCCADS to generate a list of ambulances and actually telephoned each of 10 agencies suggested by the microcomputer system. (Each agency contacted was informed at the outset of the conversation that "THIS IS ONLY A TEST. NO UNITS SHOULD BE DISPATCHED AT THIS TIME.") In this particular situation, a total list of 25 ambulances was required in order to dispatch 20 of them since three of the 25 were already on call, there was no answer at one of the agencies that had only one ambulance and one ambulance in the data set was being dispatched by two different agencies(!)

The four REMO employees who routinely worked as dispatchers were involved in this particular test. Their evaluation and comments were helpful in assessing the need for further improvements in MCCADS. In particular, on a scale of 1 to 10, the four dispatchers rated the prototype system on four attributes as given in Table 1.

These numeric assessments are clearly not overwhelming endorsements of the system. On the other hand, many of the dispatchers' detailed comments were enlightening in explaining the problems remaining with the second prototype. Specifically it was felt that:

1. The system should have the ability to review input data at any time (coordinates and location of incident, whether or not ambulance has already been dispatched, etc.)

2. Greater flexibility is required in assigning backup ambulances to uncovered areas. The system needs to be dynamic in this regard in that it should consider all current assignments before recommending backups. Furthermore, no area should be totally stripped of ambulances when backups are arranged.

3. The data on handicaps are not totally believable. These figures should be reviewed by REMO experts. Some agencies appear to have reported extremely optimistic ramp times.

4. The required phone calling would almost be prohibitive during busy hours of the day. (Actually much of this would be done by radio but interference due to time of the day and other radio traffic generated by an emergency would still cause problems.) An automatic dialing system would be helpful for calls made by phone.

5. Since the second prototype is primarily a stand-alone micro system, it is difficult for two or more dispatchers to work together. A small network of terminals would allow all involved dispatchers to coordinate calls to the agencies.

Table 1

<table><tr><td>Attribute</td><td>Average Rating</td></tr><tr><td>Speed</td><td>7</td></tr><tr><td>Accuracy</td><td>7</td></tr><tr><td>Usefulness</td><td>8</td></tr><tr><td>Ease of Use</td><td>8</td></tr></table>

6. The system should prompt dispatchers to call other appropriate emergency agencies, e.g., to put hospitals on standby and to arrange for local aviation support.

Most of these difficulties can be solved in a straightforward manner in the development of the third prototype. Items 4 and 5, on the other hand, deal also with the issue of emerging technology and will most likely merit further technical evaluation.

## 4.6. The Next Step

The second prototype is currently available for use by dispatchers at REMAC. A third prototype that incorporates most of the straightforward suggestions described above is being designed to replace it. This system will allow for a less confusing display of the current status, an improved ability to provide backup ambulances for “uncovered” agencies (using more expert-like decision rules) and will provide phone numbers (and possibly recommendations) for contacting other related emergency personnel and facilities.

It is also hoped that REMO officials will examine in detail the handicap times collected from the provider agencies. Dispatchers have indicated that they would be much more trustful of MCCADS if “accurate” numbers are incorporated. A procedure for arriving at these figures needs to be agreed upon.

## 5. Discussion

## 5.1. Summary and Future

It now appears that there will be at least 4 stages involved in the prototyping of MCCADS:

Stage 1. As described in section 4, the Version 0 prototype was designed primarily to test the feasibility of employing a microcomputer based system to aid dispatchers. The prototype was model based and a crude representation of what was really needed.

Stage 2. As discussed above, this working version of MCCADS (the Version 1 prototype) incorporated most of the real requirements of the users.

Tests of this prototype (involving simulation scenarios) revealed that the second version was an excellent model for a “final” system. Currently it is being used by REMO.

Stage 3. As indicated, this prototype has been designed and will be tested in the near future. It is an enhanced version that provides more effective information and greater detail than the stage 2 prototype. It is intended to be an “expert system” [13] in that it will capture the decision rules employed by dispatchers.

Stage 4. This prototype has proven easy to envision but difficult to deliver upon for a number of reasons. It is really the “ideal” system (Lucas, 1976) that designers often specify in the early stages of typical systems development projects. That is, the ideal dispatching system would have up to date information on the location of all ambulances and personnel, as well as a (close to) instantaneous ability to notify the appropriate agencies to act. With today’s technology, such a system is certainly a technologically feasible one. Microcomputer based computer and telecommunications networks have become a reality [6] and are well suited for this type of application. Unfortunately, economic infeasibility will likely prevent an agency such as REMO from implementing such a system in the near future. At this point, it is more likely that a technologically improved system will consist of 2 or 3 microcomputers in a network that has automatic telephone dialing capabilities. This would allow several dispatchers to work simultaneously in locating, contacting and allocating a large number of resources.

The major practical problems that remain are typical of disaster management environments $[3,4]$ . Since actual events occur so seldom, it is difficult to base investment decisions on a cost-benefit justification that looks primarily at actual system use in operation. Since most of the time spent by managers and dispatchers at an organization such as REMO is devoted to training (and not emergency response), it is important that decision support tools such as MCCADS can also serve as training devices. In this regard, MCCADS has received favorable reviews since it is being used to train new dispatchers as well as to keep experienced personnel thinking about improvements in decision rules that have been developed exclusively using past experience.

Another practical problem that plagues all emergency management systems involves the ability to keep information accurate and relevant. REMO is no exception. It is extremely difficult to justify that data should be up to date at all times, especially to the point where the precise location of resources is always known. This aspect would require both resources and considerable cooperation from all involved agencies. It currently appears to be a low priority item at REMO and similar agencies that have only recently organized and are continuing to formulate procedures.

## 5.2. Reasons for Success

An important factor in measuring the success of prototyping is that the procedure be an effective or “superior” one. According to Young [20], effective prototyping is characterized by design improvements at each stage and by quick recognition of deficiencies in definition. In the case of MCCADS, design improvements have been dramatic at each iteration of the process and straightforward unobtrusive tests (as we have described) have allowed for efficient observation of design problems that have remained at each stage.

Many observers advocate that all systems development projects should borrow as much as possible from prototyping and heuristic development. (See, e.g. the discussion in [18] or [17]. Our reasons for using a prototyping design strategy in an environment such as described here are compelling. Since computers have been used so little in disaster management, it was important that we demonstrate early in our interactions with REMO how these tools could be employed to improve the decision process. Prototyping also proved to be invaluable since the multiple casualty problem is a poorly understood one where appropriate (dispatching) decision rules are still being formulated.

In particular, the approach that we employed (recall Figure 1) effectively engaged REMO personnel in the definition, development and implementation cycles. Just as observed in numerous other settings (e.g., [1]), a very simple first prototype served to generate great interest on the part of potential users and managers. This interest then led to a high level of cooperation by dispatchers in designing the second and third prototypes. Continued involvement appeared to move users quickly down the learning curve and had a significant impact on attitude toward actual use of the system. Furthermore, since dispatchers and managers were unable to articulate their needs at the beginning of the project, we have sincere doubts that the system could have progressed very far without employing an iterative approach involving prototypes. As Davis and Olsen [11] have noted, “people can express what they like or do not like about an existing application system more easily than they can express what they think they would like in an imagined future system”.

Although some observers go so far as to suggest that “rapid prototyping” should be the universally preferred development strategy since user feedback is maximized, our application has not permitted such development. The reasons for a planned and deliberate development of MCCADS include; (1) such a system is not a high priority item due to the limited amount of time that it is used in actual operational settings, (2) the fact that there is no room for error since the system will be used as an aid in life and death situations, and (3) since cost justification is extremely difficult and cost quickly becomes a prohibitive factor. Furthermore, in this and many other environments (Keen, 1985), the required data was not readily available and the data collection process needed to go hand in hand with the development of the appropriate DSS.

## 5.3. Limitations and Generalizability

While prototyping is an appropriate strategy for the decision setting discussed in this paper, the conclusions that are drawn from the study must be weighed carefully. In fact, whenever an adaptive design approach such as prototyping is employed, there will always be questions concerning the transportability of what is learned while moving from prototypes to the “production system”. For example, concerns about generalizability may typically arise in situations where;

(1) prototypes are developed for a small representation of an actual problem,

(2) a prototype is developed using a software package and the production system is/will be implemented using a procedural language, or

(3) a prototype is developed on a certain piece of hardware and the production system on another.

The limitations of this particular study stem primarily from two factors; (1) the technology employed and (2) the specific application area. In our case, the prototypes were developed on a microcomputer, the very same system that the production system was to be implemented on (due to budgetary limitations). While this made our task more manageable, it also limits our ability to comment on future analogous prototyping efforts. As indicated above, newer and more advanced technology that includes distributed data processing, telecommunications and automated dialing features would allow for a more ambitious design and provide greater insight into the use of prototyping in other settings.

The fact that the decision setting involved a low frequency, high consequence emergency task also suggests that generalization to other settings must be made carefully. On the other hand, our findings in this setting generally support the wisdom that prototyping is an appropriate strategy when tasks are ill-structured and the decision setting is not well understood.

## 6. Concluding Remarks

In this paper we have described our work in developing a microcomputer based response system for a disaster management situation. The prototyping strategy that has recently proliferated in the MIS/DSS systems design literature was found to be an appropriate one, yielding what appears to be impressive improvements at each succeeding stage. It is our belief that the prototyping approach lends itself nicely to the development of emergency medical response situations, and, in fact, that its use will speed up the development of other decision support systems in environments that deal with rare, potentially catastrophic, events.

## References

[1] Alavi, M. and H.A. Napier, "An Experiment in Applying the Adaptive Design Approach to DSS Development," Information Management 7, 1984, 21–28.

[2] Bally, L., J. Brittan and H.H. Wagner, "A Prototype Approach to Information Systems Design and Development," Information Management 1, No. 1, November 1977, 21–26.

[3] Belardo, S., K.R. Karwan and W.A. Wallace, "DSS Component Design Through Field Experimentation: An Application to Emergency Management," Proceedings of the Third International Conference on Information Systems, Ann Arbor, MI. 1982, 93–106.

[4] Belardo, S., K.R. Karwan and W.A. Wallace, “Managing the Response to Disasters Using Microcomputers,” Interfaces 14, No. 2 (March-April 1984), 29–39.

[5] Berrisford, T.R. and J.C. Wetherbe, "Heuristic Development: A Redesign of Systems Design," MIS Quarterly 3, No. 1, March 1979, 11–19.

[6] Brennan, J.J. and M.K. Malloy, "Microcomputers", Interfaces 13, No. 1, February 1983, 28–39.

[7] Carey, T.T. and R.E.A. Mason, “Information Systems Prototyping: Techniques, Tools and Methodology,” INFOR, 1985.

[8] Carlson, E.D., B.F. Grace and J.A. Sutton, “Case Studies of End User Requirements for Interactive Problem Solving,” MIS Quaterly 1, No. 1 (March 1977), 51–63.

[9] Cohen, Claude. “Prototyping Techniques for Decision Support Systems Development,” paper presented at TIMS/ORSA Joint National Meeting, April 1983, Chicago.

[10] Davis, G.B., “Strategies for Information Requirements Determination,” IBM Systems Journal 21, No. 1 (1982), 4–30.

[11] Davis, G.B. and M.H. Olson, Management Information Systems: Conceptual Foundations, Structure and Development, McGraw-Hill, New York, 1985.

[12] Halpern, J., E. Sarisamlis and Y. Wand, "An Activity Network Approach for the Analysis of Manning Policies

in Firefighting Operations," Management Science 28, No. 10 (October 1982), 1121–1136.

[13] Hayes-Roth, F., D.A. Waterman and D.B. Lenat, Building Expert Systems, Addison-Wesley, 1983.

[14] Keen, P., "A Walk Through Decision Support," Computerworld XIX, No. 2 (January 14, 1985). INDEPTH 3–16.

[15] Lucas, H.C., Jr., The Analysis Design and Implementation of Information Systems, McGraw-Hill, New York, 1976.

[16] Mason, R.E.A. and T.T. Carey, "An Approach to Prototyping Interactive Information Systems," Communications of the ACM, 26, No. 5 (May 1983), 347–354.

[17] McNurlin, B.C., “Developing Systems by Prototyping,” EDP Analyzer 19, No. 9 (September 1981), 1–14.

[18] Naumann, J.D. and A.M. Jenkins, “Prototyping: The New Paradigm for Systems Development,” MIS Quarterly 6, No. 3 (September 1982), 29–44.

[19] Naumann, J.D., G.B. Davis and J.D. McKeen," Determining Information Requirements: A Contingency Method for Selection of a Requirements Assurance Strategy," Journal of Systems and Software 1, No. 4. Elsevier North Holland, 1980, 273–281.

[20] Young, T.R., “Superior Prototypes,” Datamation 30, No. 7, May 1984, 152–158.
