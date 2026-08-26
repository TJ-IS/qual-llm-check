---
otero_id: 17230
otero_key: "SU72RNAF"
title: "A video conferencing system for the United States Army"
authors: "Myron Hatcher"
year: "1992"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(92)90008-d"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A video conferencing system for the United States Army

# Group decision making in a geographically distributed environment

Myron Hatcher \*

Department of Information Systems and Decision Sciences, School of Business and Administrative Sciences, California State University, Fresno, CA 93740, USA

The purpose of this article is to review the physical design, software requirements, organizational culture and management issues in a video conferencing system. The audience for the paper is researchers and future users of GDSS from both academia, government and business. The author's approach will be to discuss software, hardware features, and management improvements potential. Though this system is within the U.S. Army's culture, business organizations are exploring distributed GDSS. Organizational computing and organizational information for all organizations will hinge on GDSS. Since the author could approach this writing from the academic role. Major in the U.S. Army Reserves or GDSS researcher looking to secure research or grant fund, it is best to chose one role and write accordingly. The author chooses GDSS researcher and will try, without bias, to cover this exciting example of distributed GDSS. The Army's difficulty in using this system is that after building it, the usage was not as expected. Their purpose is to improve utilization. Initially, the physical system is described. The software support, which doesn't currently exist, for users (Tool Kit) is defined for various levels of implementation. For constant improvement of the GDSS, evaluation procedures are outlined. Since this effort is viewed as developmental, future research directions are suggested. The Army's cost justification for the system is the travel cost savings. Cost savings are important to business and government organizations alike; however, the author feels effectiveness will become the driving force in the future. For example, timeliness will gain in value. Currently, the decision process forces a decision when required. This process will change to require a certain level of information and evaluation within the time-frame. These information analyses will be made possible by the distributed GDSS.

Keywords: Video conferencing, Geographically distributed decision environment, Military, Group decision support tools.

## 1. Introduction

The conceptual basis for the paper is literature reviews, prior experience and systematic analyses. This field goes by many names such as electronic conferencing, meeting support systems, etc. It may not be obvious that video teleconferencing is a subset of GDSS. However, this fact will become apparent to the readers after they have considered and reflected on the material presented. GDSS also shares a strength with DSS that is the ability to utilize information in its raw form. The decision maker may take the raw data and extract its value.

The Army's problem is how to integrate the technology of video teleconferencing into daily business activities. First, we need a few definitions and descriptions. The video teleconferencing studios are located in eight sites in the United States. One or more decision makers go to a studio and, by prearrangement, have a meeting

![](/api/attachments/SU72RNAF/fulltext/images/ae2db44fce47f5c90c65b21075ec5268ee306287450f6ae72088e0fa153841ae.jpg)

search interests are GDSS tools, user interface, uncertainty in GDSS, and public health applications.

with person(s) at other studio(s). The major advantages are face to face communication with the ability to share videos and slides. The stated motivation for expending the funds for the studios is reduction in travel cost.

Currently, the facilities are not being used to the expected level, and this is considered a problem. Understanding the reason that a person(s) would use a video teleconferencing system will help us in understanding the utilization problem. A person would use a Geographically Distributed Group Decision Support System (GDSS) voluntarily because it improves their work. This improvement normally means efficiency and effectiveness. Efficiency means that less can be spent in the decision process to arrive at an equally good result. Effectiveness means that the decision maker tries to make a better decision.

There are many intangibles involved that may be more important than any definition of effectiveness and efficiency, and these intangibles must be considered. The fact that decision makers must go to a studio to use the system is a major hurdle. In the Army culture, their absence from the office is not standard practice. Thus, the cultural expectations must change to allow the general approach that video conferencing represents to become successful.

An explanation about travel is in order. A purpose of Army travel is clarification of issues. For example, assignment officers, in the U.S. Total Army Personnel Command, will travel to review proposed assignments with the solders assigned to them for management. Since each assignment officer manages a narrow assignment classification, each trip is for a limited number of soldiers. Given the belief that each assignment is critical in the career progression, promotion, status, and retirement income, the assignment process is taken seriously. In many situations, the video conferencing system can offer almost the same ambiance as face to face conversations at a lower operating cost.

In the future, this network will include the Air Force and Navy sub-systems. Currently, inter-operability standards are being developed for the Department of Defense. This integration will allow a new set of problems to be addressed by video conferencing systems. Additionally, the new requirements for joint assignments for career progression at the higher levels make the integration of video systems important for personnel assignments. Geographically distributed GDSS will become more common in Government and Business as software packages and hardware equipment become available. Nunamaker et al. [24] presents results of their GDSS application in an IBM facility. Wagner et al. [30] has developed a different GDSS that focuses more on process. These are two commercially available systems that are paving the way for future GDSS.

Most application research reporting is threatened by the objectivity of the reporter/author. An author has various roles that can be assumed in the writing of the results. As mentioned, the author assumes the GDSS researcher role. It is true the author is an academic, and this complements the role chosen. The author's Army experience and current activities in the U.S. Army Reserves provided the opportunity to understand the Army culture. This specific application of GDSS is highly dependent upon the Army culture and care will be taken to explain ideas in sufficient detail for generalization of these ideas to other organizations. Funded research is always a desire in research, and care will be taken to report the research findings to the full extent.

The next section will review the literature of GDSS with a focus on video conferencing. Based upon the literature review, and the author's other experiences and sources of information, a strategy is outlined for improved management control, the design and development of a software tool kit, and a composition of a model base. Evaluation procedures are recommended for the continuous improvement of the system. A future research direction extends the proposed concepts and integrates with new ideas in the design of a general GDSS.

## 2. Literature Review

The field of GDSS has grown out of Decision Support Systems (DSS) and, equally, the field of psychology. It is made possible by the technological advances in computer technology, most specifically within micro computers. The main idea behind DSS was the integration of the decision maker with the computer in closed systems so that more effective and efficient decisions could be made and semi-structured problems attacked. The decision maker's value systems must be considered in the solution process. These values were present in the decision maker during the decision process and they do not need quantification in the computer software. The computer provided rapid analysis, data storage and report generation ability. The literature shows that the impact upon operational and tactical problems has been greater with strategic problem solutions waiting for future efforts. For clarification, impact is a conceptual idea when measured by the low number of working applications.

Originally, Decision Support Systems were more concerned with financial problems and were defined with procedure statements that led to answers. The classic “What If” question allowed the investigator to easily test alternatives and evaluate parameters. Other procedures include sensitivity analysis that carry out a preset process of impact evaluation upon an outcome variable through changes in an independent variable. The analyze function depicts the variables that relate to the outcome measure(s). Many other built in procedures have evolved in the DSS field. A recent procedure is the “why” function in which an artificial intelligence module provides the decision maker with an explanation of why the result occurred. These procedures are called DSS tool set by the author.

Group Decision Support Systems (GDSS) is the latest development in DSS and addresses the fact that most decisions involve several decision makers $[20]$ . The multiple decision maker aspect of GDSS raises many new questions in research and application areas. These questions include issues such as integration of decision makers' subjective and objective opinions, space and time concerns, and how to establish the cooperation/rules agenda. The GDSS tool set contains the procedures to handle several decision makers. In DSS the value system(s) was not always expressed. In GDSS, a portion of the individual values must be expressed for information sharing. Tools for individual voting and aggregation across decision makers are also included.

The location of decision makers is an important factor in GDSS systems, and the video conferencing system has geographically distributed decision makers. This is in contrast to co-located decision makers. DeSanctis and Gallupe [14] discuss geographically distributed Group Decision Support Systems as “scenario 4.” When a decision is made by geographically distributed individuals, it is commonly assumed that there is no personal interaction or knowledge about the other decision makers. This is far from the truth. Most of the decision makers in the Army know each other from prior assignments and their current assignment. These relationships must be fully utilized in the GDSS voting schemes and other GDSS tools. The system must be designed to allow maximum use of knowledge about fellow decision makers even when they are geographically distributed.

Distributed GDSS are now possible because of advances in long distance communication systems and satellite transmissions. As all levels of the Army obtain access to these resources their utilization in decision making will increase. The Army culture is primarily one of group processes with staffs at various levels giving advice to their commanders. However, the communication system must be reliable under all conditions for full integration of hardware technology into real time decision making. This includes not only combat scenarios but administrative and managerial functions. If local area networks (LAN) that support administrative and managerial functions are not operationally reliable, they will not be trusted and used. Operational reliability includes the LAN operating a large percentage of the time (99%), and given it fails, it is only for a small length of time (one hour).

The problem areas that could be served with a GDSS system include staff taskers, tactical decision support, and strategic planning. Staff taskers cover a broad range of activities, and the framework of distributed GDSS must include the ability to structure these problems for success. Tactical decision support covers real time tracking for combat direction with improved timeliness and decision quality $[28]$ . This is particularly true in the war gaming aspect of mission evaluation $[3]$ . A good understanding of critical factors and the information needed to support decisions will be gained in the design of the distributed GDSS applications $[23]$ . Strategic decision support entails special projects and require the distributed GDSS to access large databases and forecast models. The integration of multiple decision criteria will be especially important $[5]$ at the strategic level and less important at the tactical and operational levels.

The Army decision process considers uncertainty in both short and long time frames and data validity. Uncertainty in career paths is important in personnel management staff taskers $[15]$ . The concerns are the future needs of the Army over the next 20 years and the career path that is best for a given individual. Tactical combat decision making considers most likely to least likely enemy responses and selects the best responses. Uncertainly in tactical combat decision making deals with short time horizons and accuracy of data. A recommended approach is to use Monte Carlo simulation of possible scenarios so the decision makers can understand and measure the uncertainty. This information assists in reaching a decision $[1,2,9,29]$ . Uncertainty can be presented in terms of probabilities or fuzzy possibilities $[21]$ . The simulation system and models are part of GDSS. Individuals use these models via the DSS tool kit and the group utilizes them via the GDSS tool kit.

Decision makers have various criteria and performance measures either stated or unstated that they bring to a decision process. Most military decisions involve several decision makers with conflicting agendas and responsibility for different segments of the mission. This is the main reason that the development of the theory of Group Decision Support Systems, which advances the concepts of Decision Support Systems, is so important to military decision making $[7]$ . These criteria and performance measures representing different decision makers must be integrated into distributed GDSS $[12,31]$ . The author's recommended approach is the Analytical Hierarchical Process $[13,25]$ . Both objective and subjective data can be incorporated in a ratio scale with the Analytical Hierarchy Process (AHP). Ratio scales enhance the precision of the decision process and thus the decision quality.

Relationships between Army decision makers are part of the decision process and should be included in the GDSS' system. Knowing the owner of statements and data is one way of including relationships. A sensitivity analysis of shifting weights among decision makers is another way to include relationships. Personal relationships that go back to assignments at the start of an Army career can and will enhance the decision quality. Unfortunately, other approaches discussed in the literature try to discard these relationships. In non-military companies this may be the correct approach. In the Army, where the mission guides the process, both individual and shared experiences need to be incorporated in the geographically distributed GDSS. The Army's method and culture are one of staff consultation and cooperative efforts. In combat situations, many resource decisions involve key players who may come from different branches of the military. They must work together in a real time group decision process for the mission to be accomplished. What, then, is the significance of a geographically distributed GDSS? It will effect the way the Army does business by being a natural extension of its culture. A stronger statement is that GDSS must bear the culture for the system to be successful.

GDSS in business and government organizations will be useful when initially the culture is part of the system. During GDSS' evolution the organization will change to make decisions differently that best use the advantages of GDSS. Cognitive styles of decision makers are different and must be considered by the distributed GDSS [19]. These aspects would be in any Artificial Intelligence (AI) interfaces that link each decision maker through their profile with the DSS and GDSS tool kits and communication procedures [10]. The AI component that is incorporated in the decision process considers cognitive style and other psychologically oriented concepts [1]. Any artificial intelligence components should allow the system to learn with experience and adapt to the unique and changing characteristics of each decision maker. It should be mentioned that this idea has been around for many years and has not been successful in application.

The importance of GDSS is discussed by Henderson [18], who reviews the ability of DSS to support group decision making activities. Huber [20] focuses directly on GDSS and the issues that accompany a group process. How will information be shared? What are the rules of discussion and priority? What information is shared and what is not? This is important for Army efforts since “need to know” is a requirement for accessing certain information. The question of what information may not go into the network must be addressed. It needs to be remembered that any electronic telecommunication network can be compromised.

Wagner [30] focuses on the face-to-face meeting process in one location. Rules of the game are the focus of their research. Who has what priority and when? What pre and post meeting activities should be designed into the system? Even though this research concerns face-to-face meetings in one location, these efforts are important to the distributed environment. The level of prior experience among the Army decision makers indicates a need for pre/post meeting activities to be included in our thinking and any decisions.

Malone [22] has been concerned with interaction of people without face-to-face communication, with information sharing by electronic mail systems and local area networks. Decision making is also defined in a less strict sense to include many decision activities in which a precise decision is not necessarily reached. Decision activities are important in the Army's culture where recommendations are given to the Commander for the final decision. In theory, all decisions are made by the Commander. The Army's decision process or way of doing business such as pro/con analysis and other decision activities must not be lost in computerization.

Other issues in GDSS concern experimental investigation. Gallupe and DeSanctis [14] present a research agenda and specific hypotheses that need to be answered concerning decision quality, number of possible alternatives generated, decision confidence, and satisfaction with the decision making process. Experimental research efforts should include these hypotheses for investigation and the information gained can be used to improve GDSS design. Any effort that adds insight into how groups make decisions when using video conferencing hardware and software will be of interest and value [12,24,26].

The actual design of a GDSS is discussed by DeSanctis, Sambamurthy, and Watson [8]. Issues such as set up programs, public and private programs and data files, session parameters are explored and valuable in video conferencing research. Ghiaseddin [16] proposes a higher level development system for improving the efficiency of developing applications, and Farwell [11] emphasizes the importance of flexibility. These and many other concepts will be considered in developing distributed GDSS systems and immediate approaches for improved participation in video conferencing.

Research on distributed GDSS and video conferencing will be significant to all Army decision making activities, but initially the research will benefit staff with personnel decisions. In the future, the tactical combat mission and war gaming process could use similar systems and benefit from these concepts. Eventually, the real time management of combat with decision makers geographically dispersed will be possible under distributed GDSS $[9,29]$ . The ability to accomplish the Army mission will be greatly enhanced with the use and integration of distributed GDSS. The system with databases, multiple geographically distributed decision makers, and decision making tools and models will lead to a better decision.

## 3. Video Conferencing System Description

There are eight video conferencing studios in the United States. These are:

<table><tr><td>Facility</td><td>Location</td></tr><tr><td>Headquarters, Department of the Army</td><td>The Pentagon</td></tr><tr><td>TRADOC</td><td>Ft. Monroe, Virginia</td></tr><tr><td>FORSCOM</td><td>FT McPherson, Georgia</td></tr><tr><td>Health Services Command</td><td>Ft. Sam Houston, Texas</td></tr><tr><td>Information Systems Command</td><td>Ft. Huarhuca, Arizona</td></tr><tr><td>Army War College</td><td>Carlisle Bks, Pennsylvania</td></tr><tr><td>Command and General Staff College</td><td>Ft. Leavenworth, Kansas</td></tr><tr><td>US ARMY Material Command</td><td>Alexandria, Va.</td></tr></table>

The system allows both verbal and visual conferences in a geographically distributed area through a system of audio and video links in specially equipped studios in the above locations. Each studio has five audio microphones and two full-color video monitors. The incoming monitor gives you the image from a remote location. The display monitor presents what is being sent out.

You can do most things as in face to face conversation such as taking advantage of visual and oral cues. The voice activated camera facilitates the conversation by shifting to the person talking and this image is projected to the monitoring screen.

Various images can be shared by the system. A light box is mounted on the conference table that allows printed documents, transparencies, and three dimensional objects to be shared. Each conference is equipped with an easel for flip chart presentations or individual charts and these displays are picked up by the camera. A 35-MM slide projector can be operated from the studio control panel and information similarly shared. Video recording equipment is another media for information sharing.

Individuals can use the video record for documenting the entire meeting. A hard copy machine is also available for black and white copies of any image on the incoming monitor that includes pictures of the participants.

The security level capability is secret and all transmissions can be encrypted up to this level. The top secret level is not available on the system at this point. At each location, a conference facilitator is responsible for scheduling and arranging meetings, answering technical questions, giving guidance on how best to use the equipment, and operating the equipment if desired. If more than two locations are involved in the conference a multipoint option is used. One of the studios moderates the meeting and the image on the incoming monitors in each studio. All studios can speak to and hear from the other studios. One monitor at each location displays the image from the studio that is moderating the meeting. The other monitor at each location displays the image from the studio transmitting. While a conference is in progress a participant signals the moderator that a studio wants to transmit via video. Individuals from outside locations can participate by telephone with an audio add-on option. This option has no security feature and can be used at unclassified conferences only.

## 4. Management Procedures for Scheduling a Conference

Each organization will have to consider the problems of scheduling the use of the GDSS. Appendix A outlines a specific approach that the

U.S. Army uses for their video conferencing system.

Management control was mentioned as a purpose for this paper. The author's intention was management issues for the GDSS and not the organization using the system. There is limited control in the prototype systems. Once the conference begins it is basically a free exchange. The tradeoff for control in the system should be features in the software that lead to better decisions. The integration of Artificial Intelligence (AI) in GDSS is such a feature. The more control given to the AI software, the less freedom the decision makers will have.

## 5. Design and Development of a Tool Kit and Model Base for the Video Conferencing System

It must be made clear that the current system does not have a tool kit or set of models. The purpose of the tool kit is to enhance and improve the decision process of the system. This is accomplished with software that carries out predefined functions at the decision makers' request. For discussion purposes the tool kit should be divided into Decision Support Systems (DSS) Tools and Group Decision Support Systems (GDSS) Tools. The model base contains the models that are used by the DSS and GDSS tools. Examples are simulation models, linear programming models, nonlinear programming models, Analytical Hierarchical Process models, and so forth. The tools allow the models to be applied as part of the decision process to problems.

As mentioned in the literature review, tools such as “What If,” “Goal Seeking,” “Analysis,” etc. are common in DSS. These tools apply to a spreadsheet format that are financial DSS. However, the Army’s video conferencing system is designed for a wider class of problems. Since it was financed to offset travel cost, the type of problem that would require travel must be considered. These problems tend to be qualitative and require information gathering.

The GDSS tools are the most important for these problems. It should be clarified that GDSS tools can be used by one person, but their design is for multiple decision makers. The GDSS tools include idea generation, idea organization, voting and issue exploration, as discussed by Nunamaker et al. [24], which occur during the session. Pre-meeting planning and post-meeting analysis are equally important. Following is a brief explanation of the GDSS tools. A star indicates the tools recommended for immediate implementation. Two stars indicate second priority for implementation after tools with one star.

1. \* Idea generation allows the participants to open or anonymously explore an idea simultaneously. Preferably, the comments should be in writing but could be verbally given with the voices being masked and the video camera not identifying the speaker. A Delphi or Nominal Group Process model from the model base could be used in this process.

2.\* Idea organization software assists the participants in focusing on key issues and providing various organizational schemes. After the issues are identified, the software assists in mission or policy statements formation.

3.\* Voting provides a variety of methods to determine priorities such as rating methods or ranking methods. The private votes are analyzed and results displayed. Alternatives evaluation and analysis, under different weighing criteria, provide tradeoffs.

4. Issue Exploration supports idea solicitation, stakeholder identification, assumption analysis and more. The analysis focuses on who is involved and who has what to gain or lose.

5.\*\* Problem-specific analysis applications support a certain type of evaluation. An assignment application assists an officer and the assignment officer in selecting or ordering the potential assignments. The software assists the officer in listing the criteria. Then a model from the model base, such as an Analytical Hierarchical Process (AHP) model, would be used. The model would attach weights to the criteria and relate them to potential assignments. Databases would be accessed for historical information on promotion percentages given other situations.

6.\* The pre-meeting analysis is the clarification of the topics to be discussed, the gathering of related information, and the dispersement to the participants via a computer network. Each participant could disseminate information.

7.\* The post meeting analysis is the production of a written summary or group history of the session with supporting documentation. Since a paper medium is not used, it is important to document specific decisions or actions.

The DSS and GDSS tools need to be programmed for the system. There are GDSS on the market that may meet the Army's standards; however, prototyping and implementing the systems internally would be the best approach. This would allow continuous changes in the area where the traditional systems design approach would be difficult. The Army culture is so unique that it is questionable if an off-the-shelf package would meet its needs.

The model base would be accessed by DSS tools and GDSS tools. The models are software programs that accomplish a specific analysis and may or may not have an optimization function. Examples of models are Monte Carlo simulation, linear programming, non-linear programming, queuing, decision, stackholder, analytical hierarchical process, weighing of criteria, rating of criteria, etc. Most models are software packages that can be purchased separately and are used by the GDSS software and tools.

## 6. Evaluation of the Tool Kit/GDSS System in the Video Conferencing System

The implementation of the tool kit and model base will encourage usage of the video conferencing system and the system's evaluation will provide the information needed for improvement of the DSS and GDSS tools. Each tool must be evaluated for user acceptance. After each session, each user will state their opinion on the tools that were used. The questions should concern result and process acceptance. For example, if participants indicate a desire for other voting criteria, they could be added.

The questionnaire method preferred by the author is the distribution of 100 points among attributes of a concept. For example, the concept of idea generation could be evaluated by questions or scenarios.

A. Allocate 100 points among the following idea generation attributes that you experienced in the video conference.

\_\_\_\_ 1. Provided anonymous participation

\_\_\_\_ 2. Provided access for participation

3. Values of the Delphi process

\_\_\_\_4. Values of the Nominal Group Process

5. Idea documentation

6. Process contributed to the solution

7. Process contributed to identification of the problem

Similar questions could be used to identify attributes desired but not present.

## 7. Future Directions

After the above implementation, a general GDSS should be developed. The following is a brief outline of one proposed system with five modules/objectives. The prior concepts are incorporated in the design.

A. Objective (1): Effective representation of subjective and objective opinions from decision makers through the analytical hierarchy process for use in the consolidation of judgement models in a geographically distributed GDSS.

This step includes a detailed literature search into decision making and various methods for representation of opinions. The army decision making process also will be reviewed in depth through written documents and personal interviews. This process will provide the technical basis for representation of information in the geographically distributed GDSS. Extensive use of the Defense Systems Management College (DSMC) library and access to DSMC staff and their recommended resources will be performed as a first task. This process will input into developing the consolidation of judgement models using the analytical hierarchy process. The AI decision makers' interface and AI decision process modules will use results of this first step. An annotated notebook will be delivered as supporting documentation for the development of the geographically distributed GDSS.

B. Objective (2): Development of a knowledge base and inference engine design for the AI decision makers' interface.

Each decision maker has a different military history, cognitive and psychological profile, and approach to decision tasks. Thus the interface must tailor the communication between the system and decision maker for the best decision quality. Temporal concerns will be addressed and communication tailored for different time constraints. The models from objective A that consolidate inputs from the various decision makers into a ratio scale that represent consensus are part of the AI interface.

C. Objective (3): Determination of the preferred parameters for the decision process and translating these into an inference engine design with the appropriate knowledge base design for the AI decision Process.

The decision process that binds the decision makers together must be structured for each classification of decision. This is similar to determining the rules of the game. What information will be shared, how will it be presented, and so forth? The construction of the decision process will be driven by the AI decision process module that will be dynamic and learn with experience. Thus the configuration will improve itself over time.

D. Objective (4): Select the DSS and GDSS tools and models that are needed in the distributed GDSS. These include simulation, optimization, etc.

Because of the number of problems that are resource constrained, optimization must be available for the decision makers. This will include sensitivity analysis, etc. Simulation is needed for quantifying of uncertainty in the environment through probability distributions or fuzzy possibilities.

E. Objective (5): Development of a programmable system shell for geographically distributed group decision making that provides application and user interface flexibility.

The system shell will be set up for each class of problems and tailored for each group of decision makers. Default profiles will eventually evolve for classifications of problems. This is the module where decisions regarding private versus public data, information sharing style, timing of decision process, what is a session, pre-/postsession requirements and so forth will be made.

F. Objective (6): Assessment of the feasibility of implementing the geographically distributed GDSS based upon the designs of the components and pilot testing of these selected components.

This step will provide a high level assessment of the feasibility of implementing the geographically distributed GDSS. Running models will be used for demonstration and evaluation with close cooperation with and feedback from the Army. Issues of size, complexity, realism, and quality will all be considered.

## Appendix A: Management Procedures for Scheduling a Conference

The normal hours for the system are 9:00 AM to 2:00 PM EST with a two hour time limit. Additional time outside the normal hours may be scheduled. Conferences are scheduled on a first come first served basis and a time slot reserved up to 3 days while the conference time is being confirmed. At the time of the conference the set up time is 45 minutes for a multi-point conference and 30 minutes for a point to point conference. Recurring conferences may be scheduled up to 3 months in advance through the HQDA Reservation Office. The reservation office may request any user to change the schedule for optimum use of the system.

The steps in the scheduling process are:

1. The requester of the conference or user initiates the request with the local studio's facilitator. The preferred date, time and length of conference is given to the facilitator.

2. After the date and time are secured with the local studio, the user checks the points of contact at the conference locations for date and time available.

3. The user then makes the official request to the local facilitator. The user must provide the following request data: date, time, length of conference, requester's location, points of contact, coordinator conference room, chairperson conference room, conference subject, key speakers, conferees, visual information materials to be used, whether the conference is to be recorded, and security level of conference.

4. The facilitator places the request with the HQDA Reservation Office (Pentagon).

5. If the requester has a justified request for a conference on a particular date both a time slot in the normal hours and a time slot outside the normal hours are considered.

6. The reservation office will notify the participating facilitators after confirming the conference.

7. The local facilitator notifies the requestor once the conference has been approved and assigns a control number.

8. The requestor will contact all conferees and inform them of the date, time and duration.

9. The conferees will contact the facilitator at their locations to confirm the information each participating facilitator received from the reservation office and to provide security information.

10. The requester must provide security information to the local room facilitator on clearance of the personnel who will attend the local studio when a secure conference is to be conducted.

11. The requester must provide a list of conferees to each studio when a secure conference is to be conducted.

12. Each facilitator will check the planned list of participants with attenders for proper access to the studio.

## References

[1] L. Adelman, Distributed Tactical Decision Making: Conceptual Framework And Empirical Results, Report no. M86-005, DTIC no. AD-A170 302 (May 1986).

[2] A. Basu and A. Dutta, Computer Based Support of Reasoning in the Presence of Fuzziness, Decision Support Systems 2, No. 3 (1986).

[3] R.P. Bonasso, What AI Can Do for Battle Management: A Report of the First AAAI Workshop on AI Applications to Battle Management, AI Magazine (Fall 1988).

[4] P.R. Capps and M.J. Tolson, Airland Battlefield Environment (ALBE) Tactical Decision Aid (TDA) Demonstration Program, Report no. ETL-R127, DTIC no. ADA189 712 (Nov. 1987).

[5] S. Christos, CO OP2.0 Distributed Decision Support System for Strategic Planning, DTIC no. AD-A168 443 (March 1986).

[6] G. DeSanctis and B. Gallupe, Group Decision Support Systems: A New Frontier, in: Sprague and Watson, Eds., Decision Support Systems: Putting Theory into Practice (Prentice-Hall, Englewood Cliffs, NJ, 1986).

[7] G. DeSanctis and R.B. Gallupe, A Foundation for the Study of Group Decision Support systems, Management Science 33, No. 5 (1987).

[8] G. Desanctis, V. Sambamurthy and R.T. Watson, Building a Software Environment for GDSS Research, Eighth International Conference On Decision Support Systems (Boston, MA, 1988).

[9] A. Dutta and A. Basu, Computer Based Support of Reasoning in the Presence of Fuzziness and Uncertainty, Decision Support Systems 2, No. 4 (1986).

[10] J.J. Elam and B. Konsynski, Using Artificial Intelligence Techniques to Enhance the Capabilities of Model Management Systems, Decision Sciences 18, No. 3 (1987).

[11] D.C. Farwell, A Model Based Approach to Decision Support System Flexibility, Interfaces 12, No. 5 (1982).

[12] Y. Fijol and M.A. Woodbury, Group DSS (Decision Support Systems) and Decision Outcome Measures: A Comparative Study in Distributed versus Non-Distributed Settings, DTIC no. AD-A180 949 (March 1987).

[13] E.H. Forman, T.L. Saaty, M.A. Selly and R. Waldron, Expert Choice (Decision Support Software, McClean, 1985).

[14] R.B. Gallupe and G. DeSanctis, Computer-Based Support for Group Problem-Finding: An Experimental Investigation, MIS Quarterly 12, No. 2 (1988).

[15] S.L. Gass, R.W. Collins, C.W. Meinhardt, D.M. Lemon and M.D. Gillette, The Army Manpower Long-Range Planning System, Operations Research 36, No. 1 (1988).

[16] N. Ghiaseddin, An Environment for Development of Decision Support Systems, Decision Support Systems 2, No. 3 (1986).

[17] M.E. Hatcher, Simulation and Uncertainty Within a Decision Support System Model, Proceedings: IFPS Users Association, 1985 National Meeting (Austin, TX, June 1985).

[18] J.C. Henderson, Finding Synergy between Decision Support Systems and Expert Systems Research, Decision Sciences 18 (1987).

[19] G.P. Huber, Cognitive Style as a Basis for MIS and DSS Designs: Much Ado about Nothing?, Management Science 29, No. 5 (1983).

[20] G.P. Huber, Issues in the Design of Group Decision Support Systems, MIS Quarterly 8, No. 3 (1984).

[21] Kacprzyk, J., Group Decision Making with a Fuzzy Linguistic Majority, Fuzzy Sets and Systems, 18, No. 2 (1986).

[22] T.W. Malone, K.R. Grant, F.A. Turbak, S.A. Brobst and M.D. Cohen, Intelligent Information-Sharing Systems, Communications of the ACM 30, No. 5 (1987).

[23] R.J. McTeigue, A.K. Toh and P.K. Luster, Program of Basic Research in Distributed Tactical Decision Making, Report no. PGSC-87-37, DTIC no. AD-A189 125 (Aug. 1987).

[24] J.F. Nunamaker, D. Vogel and B. Konsynski, Interaction of Task and Technology to Support Large Groups, Decision Support Systems 5, No. 2 (1989).

[25] T.L. Saaty, Multicriteria Decision Making: The Analytic Hierarchy Process (Planning, Priority Setting, Resource Allocation) (University of Pittsburgh, Pittsburgh, PA, 1988).

[26] R. Sharda, S.H. Barr and J.C. McDonnell, Decision Support System Effectiveness: A Review and an Empirical Test, Management Science 34, No. 2 (1988).

[27] D.L. Small, Distributed Tactical Decision Support, DTIC no. AD-A191 739 (Nov. 1987).

[28] H.B. Teates, The Role of Decision Support Systems in Command and Control, Signal (Sept. 1982).

[29] A.L. Vassiliou, ARES: A System for Real-Time Operational and Tactical Decision Support, DTIC no. AD-A178 565 (Dec. 1986).

[30] G.R. Wagner and M. Nagasundaram, Meeting Process Augmentation: The Real Substance of GDSS, University of Texas at Austin Publication Series (Austin, TX, 1988).

[31] R.P. Wiley and R.R. Tenney, Calculating Time-Related Performance Measures of a Distributed Tactical Decisionmaking Organization Using Stochastic Timed Petri Nets, Report no. LIDS-P-1510, DTIC no. AD-A162 463 (Oct. 1985)
