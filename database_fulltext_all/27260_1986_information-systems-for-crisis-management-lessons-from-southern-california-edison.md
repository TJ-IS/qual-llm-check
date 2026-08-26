---
otero_id: 27260
otero_key: "975NJFJ5"
title: "Information Systems for Crisis Management: Lessons from Southern California Edison"
authors: "Thomas J. Housel; Omar A. El Sawy; Paul F. Donovan"
year: "1986"
journal: "MIS Quarterly"
doi: "10.2307/249195"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Information Systems for Crisis Management: Lessons from Southern California Edison
Author(s): Thomas J. Housel, Omar A. El Sawy and Paul F. Donovan
Source: MIS Quarterly, Vol. 10, No. 4 (Dec., 1986), pp. 389-400
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/249195

Accessed: 09/05/2014 10:07

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Information Systems for Crisis Management: Lessons from Southern California Edison

By: Thomas J. Housel
Department of Business
Communication
Graduate School of Business
Administration
University of Southern California
Los Angeles, California

By: Omar A. El Sawy
Center for Futures Research
Graduate School of Business
Administration
University of Southern California
Los Angeles, California

By: Paul F. Donovan
Corporate Communications
Southern California Edison Company
2244 Walnut Grove Avenue
Rosemead, California

## Abstract

This article describes the design, implementation, and evaluation of an integrated voice-data-video information system for crisis management at Southern California Edison (SCE). It was developed for top managers to help prevent and control problems that might arise with their nuclear power generating station at San Onofre, California. The article describes some of the system's unique design features, and the lessons that SCE learned from implementation. It concludes by providing a generic set of prescriptions for the design and implementation of information systems for crisis management.

Keywords: Crisis management, information systems design, information systems implementation, information systems evaluation, group decision support systems

ACM Categories: C.2.1, C.4, H.1, H.4.2, H.4.3, J.1, K.6.1

# Understanding Organizational Crises

No organization is immune from the possibility of a crisis. While no single, all-encompassing approach exists to plan for a crisis, organizations can set up crisis management systems that help prevent a crisis from becoming a disaster.

In the complex, fast-paced business environment, a crisis management plan is only as good as the information system that supports it. Managers need quick, reliable, and clear information to prevent and control crises. It is the design, implementation, and evaluation of systems to provide such information that is the focus of this study.

Companies that have crisis management procedures in place recover 2.5 times faster after a crisis than companies that do not [4]. However, a recent survey of CEOs found that only 50% of them had a plan in place for managing one, though 89% believed that “a crisis is as certain as death and taxes,” [17]. As the business environment becomes more complex and the frequency of crises increases, crisis management systems will become a central part of strategic management.

A crisis is characterized by extreme threats to important values, intense time pressures, high stress, and the need for rapid, yet careful decision making [1]. Business crises are defined broadly as turning points in which a situation of impending danger to the organization runs the risk of escalating in intensity, interfering with the normal operations of the business, jeopardizing the organization's public image, and damaging the organization's bottom line [4, 9, 11].

One way to classify organizational crises is through their precipitating events [9]. There are technological crises caused by the failure of technology, with examples ranging from industrial accidents (e.g., toxic gas leaks), to computer failures (e.g., in online transaction processings systems). There are confrontation crises precipitated by social action groups or labor unions as a way of pressuring for their demands, with examples such as product boycotts and labor strikes being most common.

There are malevolence crises which are precipitated through hateful or criminal intent and include such incidents as product tampering, terrorism, and sabotage, whose crisis consequences can range from product recalls to loss of human life. There are management failure crises which are seemingly precipitated by management's ineptitude (e.g., hostile takeovers or bad financial press coverage), by management's negligence (e.g., inattention to high risk transactions or potential strategic market shifts) or management's misconduct (e.g., embezzlement and tax law violations). There are also crises that contain elements of more than one of these types, such as unwanted or unplanned product defects which result in massive product recalls.

## Southern California Edison: The Context of the Crisis Study

The Southern California Edison Company (SCE) is the largest electrical power utility in California, the second largest in revenues in the nation (over \$5 billion in 1985), and has over 17,000 employees. It has been providing electrical power for 100 years, and currently provides about 66% of the electricity for Southern California through its 61 generating stations, including the San Onofre Nuclear Generating Station (SONGS). The crisis information system created to prevent and control accidents at SONGS provided the context for this study.

The potentially devastating effects of nuclear accidents have prompted nuclear power companies across the country to take all possible measures to prevent such accidents. Incidents such as the Three Mile Island accident in Harrisburg, Pennsylvania [8] and the Chernobyl disaster in the U.S.S.R. [16] have demonstrated the extreme importance of having an effective information system during such crises, to activate and coordinate a timely response.

SCE identified the need to develop an information system for crisis management that would provide immediate, reliable, high clarity information to aid top management decision making in the event that an accident or emergency occurred. In a crisis, decision making would take place under stress and there would be a greater chance of miscommunication. To provide the best possible infrastructure, SCE management examined all new information technologies and management methods that might leverage decision making during crises.

Over its many years of service, SCE has successfully resolved crises of power interruptions caused by such events as natural disasters, equipment breakdowns, and air vehicles colliding with power lines. However, none of these crises had information system requirements as demanding as the SONGS situation. The information system had to operate reliably over a prolonged period in a variety of adverse conditions and because of the complexity and potential severity of a nuclear accident, an information system would have to enable very rapid communications among a large number of parties (e.g., civil agencies, the media, non-technical support staff). Since the interacting parties did not necessarily share the same background knowledge or expertise, the need for clear information was greater because of the greater potential for miscommunication.

A key aspect of SCE's crisis management plan was the creation of the Emergency Support Organization headed by the Vice President for Nuclear Engineering, Safety, and Licensing. This organization was responsible for developing detailed plans, procedures, and infrastructures to provide managerial, technical, and logistical support for crises (see Figure 1). Managers and representatives from the Information Services Department were part of this organization, and Information Services was responsible for providing the information technology infrastructure.

The Emergency Operations Facility (EOF) is the decision making focal point and coordinates the activities of all the other SCE crisis teams, the outside agencies, and SONGS technical support personnel. SONGS technical support personnel keep the EOF team informed of events at the reactors and receive instructions from EOF management. The Emergency News Center coordinates all activities with the press and draws its input for press releases and conferences from the EOF. Headquarters personnel service a support function and perform the "pick and shovel" work (e.g., access past host computer records of maintenance or repair work on reactors) requested by the EOF. The EOF management personnel also confer with the Executive VP at headquarters on major decisions and keep him informed of events at SONGS.

Figure 1. Southern California Edison's Emergency Support Organization  
![](/api/attachments/975NJFJ5/fulltext/images/373123cc596aade4afa006eb6ba748fe7f58d962d4fb5f84bd16df5e01c9f22e.jpg)

The activities of the outside crisis teams are also coordinated through the EOF. These include the Nuclear Regulatory Commission (NRC), the State Office of Emergency Services, and other civil agencies. These outside agencies were made part of the Emergency Support Organization because of the vital support roles they play in providing expert support, medical treatment, population evacuation, and control.

## Design Issues

The design features of SCE's crisis information system focus on the need for immediate, reliable, and high clarity information by the crisis teams. The crisis information network also makes use of the company's existing information system capabilities.

## Basic Network Design

The crisis information transmission network is represented in Figure 2, and shows the various types of links that connect them. The network topology is a wheel design with the EOF as the hub for decision making, information reception, and information dissemination. The remote sensing, voice, data, and video information links serve as spokes to the other crisis teams. Some of these links are dedicated so that they are available for use immediately at all times. Others are dial-up or switched links which go through the public network or SCE's private branch exchanges.

Dedicated remote sensing links: These links transmit technical measurement information from the instrument readings at SONGS to the EOF.

Voice and data links: The voice and data links from the EOF to the civil agencies make immediate communication from the EOF possible in oral and written modes, vital to the swift mobilization of resources.

Dedicated and integrated voice-data links: The dedicated voice and data links to the State Office of Emergency Services improve the clarity of technical information exchanges with the EOF. This integrated link is also used to conduct crisis training between the two locations during drills.

Figure 2. Information System Links for the Emergency Support Organization  
![](/api/attachments/975NJFJ5/fulltext/images/c4096f40dcb8735b25960dbe4c52f28c4d281e7b5451c777894d1fd7e1b95f77.jpg)

Dedicated and Integrated voice-data-video link: The video link between the EOF and headquarters makes it possible for headquarter support personnel to more rapidly understand and respond to EOF team members requests, and for top management to understand the severity of the situation.

## Immediate Information

Both the human communication procedures espoused for information exchange between crisis teams, and the underlying network topology (hub and spokes), are designed to help fulfill the requirement for timely information. The teams have, in the EOF, one primary point of contact for information access, exchange, and decision-making. The information technology, both hardware and software, was selected to support and enhance these rapid information exchange procedures.

The use of dedicated telecommunication lines between the crisis team locations allows immediate access to desired crisis personnel with no chance for a busy signal. Another feature of many of the dedicated voice lines is the special conferencing feature which allows an EOF team member to interact with members at more than one location simultaneously, greatly simplifying the decision maker's coordination tasks.

The dedicated data lines also have a broadcast feature which make it possible to immediately send the same text message to many locations at once. The broadcast feature is particularly useful in providing information to the press and outside civil agencies without the need to orally communicate the message. This avoids the potential problems of tying up decision makers in prolonged dialog with outside agencies over routine information.

The video conferencing system allows immediate, high clarity communication between top level and support personnel at headquarters and the EOF through the use of visual aids (e.g., maps, status boards, sketches) and the ability to see each others' nonverbal cues. Because of the advantages of this information channel in increasing the speed of understanding of technical data and reducing the potential for translation errors, there is a proposal to establish new video conferencing links between the EOF and the Emergency News Center, and the EOF and SONGS. The video link to SONGS would be used to "see" the problem while discussing it. The possibility of mobile robots with video cameras has also been considered. A video link is also under consideration for a future connection between the EOF and the NRC.

## Reliable Transmission of Information

SCE developed a private information network throughout their 60,000 square mile service area because they were not satisfied with the service reliability of the public switched network. The current information transmission network runs over their existing power lines and is maintained by SCE's telecommunications function which allows them to set and control their own service reliability levels.

In addition to their private network, SCE uses the public switched transmission network operated by the local telephone company and long distance telephone companies. The public transmission network is primarily used for routine operations and serves as a redundant, back-up system during crises.

## High Clarity Information

During a crisis, information needs go up tremendously, while at the same time putting the participants under increased stress and time pressure, thus greatly increasing the chances of information overload and miscommunication. It becomes vital for effective management of a crisis to minimize message ambiguity, information filtering and distortion, and conflicting instructions. There is also a need to maximize the clarity of the vital information exchanged between the crisis teams. The information exchange procedures and supporting network configuration were designed and the information technology selected to fulfill these requirements for high clarity information.

The centralized topology and the structured communication channels, with the EOF as the hub, serve to reduce the information overload and conflicting information. In addition, integrated (i.e., combinations of voice, data, and video) information links between the EOF and the other crisis teams bolster information clarity. SCE installed integrated voice-data links between the EOF team and most of the crisis teams, and a voice-data-video link between the EOF and headquarters. These links are especially useful when the different teams are called upon to interactively interpret data.

Video capabilities enable the use of visual aids for explanation, and the use of full-motion video added important non-verbal cues. The proposed enhancements of the video conferencing system could allow for mobile access to plant operations so that “real time” motion pictures could be available to the EOF and the other supporting teams.

The Executive Vice President of Operations saw the advantage of having the interactive video conferencing capability between headquarters and the EOF in promoting immediate, high clarity communications. His justification for the full motion interactive video conferencing capability was that it would reduce the potential for misunderstanding caused by voice-only communications between interactants who did not share the same background understanding of technical issues. He reasoned that it would be much easier to understand a complex problem if it could be seen as well as described. In addition, the non-verbal cues or "body language" of the interactants would provide additional information that would help them understand one another.

## Implementation Issues

The implementation of the SCE crisis information system was very closely intertwined with the design process, and had an iterative nature. Drills and simulation exercises were a key part of the implementation process, for both the vital training they provided and the design insights that they generated. However, they also generated further insights for the implementation process itself. It was as if the information systems implementation was what was being prototyped, rather than the information systems design.

All the while, the Emergency Support Organization procedures were being documented, and procedures for continuously updating them were being refined. The resulting manual included clear information about procedures, duties and responsibilities; team compositions, with contact information and alternative personnel; methods of notification; information services and how to use them; and responses in the different types of emergencies.

All the SCE crisis teams and the outside agencies included in the Emergency Support Organization were involved in this implementation process. This included parties not customarily included in information systems implementation, such as the press. This inclusion also contributed to the training of those personnel to interface effectively with the SCE crisis information system.

## Drills

During the drills, team leaders talk through procedures with team members and “turn-up the system” to make sure it is operating properly. These drills give team members a chance to think through and discuss their responsibilities and actions without the time pressures present during exercises or actual incidents, and also to discuss improvements to the information system. In this way the drills serve as training sessions and give the participants a chance to receive immediate feedback on their suggestions and performance. The drills are held regularly, and are always announced beforehand.

## Exercises

Exercises involve all SCE crisis teams and outside agencies and require full activation of the crisis information system, simulating a real crisis. The exercises are graded by observers from the NRC and SCE, thus creating some of the pressures on personnel that might occur during a real incident. The exercises are held periodically, but are sometimes unannounced. The nature of the emergency can vary along the whole spectrum from an “Alert” to a “General Emergency.”

The crisis information system is tested during the exercises for information immediacy, reliability, and clarity over the time period (often several days) of a real emergency, and how that contributes to decision response. The exercises prove useful in pointing out possible information bottlenecks, equipment or network failures, procedural difficulties, or human communication errors caused by team members. This valuable feedback is translated into changes and enhancements to the system design and user procedures.

During the exercises, Information Services Department personnel must ensure that crisis team members have priority access to the host computer to gather needed data (e.g., maintenance and repair records, work orders for the reactor, health information). They are also responsible for ensuring the reliability of the computer equipment and must be ready to respond immediately to any breakdowns. Telecommunications department personnel are responsible for ensuring the reliability of the information transmission network (both public and private), and the voice and video equipment.

## Evaluating the Impact at SCE

SCE's crisis information system performance has not been evaluated in an actual emergency; fortunately, none have occurred. Therefore, all evaluation of the information system's effectiveness has been conducted through graded exercises. This evaluation process has the limitation of not creating the emotional strain on the crisis teams that would happen during a real emergency.

Under evaluation constraints, SCE management thought it vital to attach special significance to the exercises so that crisis team members would be motivated to perform well. In their efforts to create an objective assessment of the crisis organization's effectiveness, SCE management often conducts unannounced exercises. One unannounced exercise required use of the recently installed video conferencing link between the EOF and headquarters. In this manner, management sought to create a unique crisis scenario which would require team members to use the new technology.

The scenarios created for the exercises involve tests of the information system, as well as simulations of different kinds of plant failures. For example, one scenario involved the loss of a primary information link (i.e., the dedicated voice network) and required the use of a back-up radio network. A significant part of the evaluation process focuses on the crisis team's use of the information system.

The NRC is involved with the graded exercises and serves as an objective source for performance evaluation. SCE management is extremely motivated to be objective in their evaluations of the exercises and tend to be more critical than the NRC representatives.

There is also a psychological effect on crisis team members of having an effective crisis information system that could help them save lives. It gives team members confidence that they have access to the appropriate information whenever they may need it, and that they will be able to handle an emergency. This increased confidence was translated into better performance on the graded exercises.

The implementation of the crisis information system also had serendipitous positive impacts on SCE's employees use of the system for their daily work, and their acceptance of new information tools. Because the crisis information system requires constant testing, SCE employees are asked to use it for their daily work as much as possible. This encouragement to use the system, and the justification of keeping the system "well oiled,"

seems to put less pressure on employees to use the system to improve their productivity. With the mental burden of having to become more productive to justify management's purchase of new information system tools relieved, employees feel more at ease in trying the system and use those aspects of the system that help them perform their work. Those features of the system that do not help them are used just as often as deemed necessary to test their reliability.

The pride that crisis team members have in their information system also makes it easier for them to accept new information tools as they are added. For example, when the video conferencing system was added to the information system, crisis team members were much quicker to accept this new tool than is usually the case when it is introduced in other companies. Video conferencing can be threatening to those users who perceive that they must be “movie stars” to use the system effectively. This was not the case at SCE because the crisis team members immediately saw the potential of this information tool to improve vital communications links.

## Justification

The justification for the cost of implementing SCE's crisis information system was based on the very low probability of the occurrence of an event (a nuclear accident) that might lead to potentially very high negative impacts. It was obviously not a direct ROI justification. Because of the overwhelming public safety consideration, and given the situation that occurred at Three Mile Island and Chernobyl, it would seem that there would be no resistance to such a justification.

However, the nuclear industry, like other industries that face the remote possibility of a catastrophic accident, is very reticent to even admit that the possibility for an accident exists. Like any other company with stockholders, SCE has to justify expenditures. Being a regulated utility, SCE also has the added problem of being required to justify any expenditures that might result in a rate hike. Therefore, they had to clearly demonstrate the benefit of their crisis information system, especially with respect to added information technology enhancements such as video conferencing. Improved crisis response and control through immediate, reliable, and clear information easily provide this justification.

However, organizations in other industries where a crisis would not have such severe consequences (loss of human life) may find the justification more difficult, unless top management support is very strong. Organizations implementing crisis information systems have the problem of implementing an information system that cannot be justified based on its potential ROI, competitive advantage, or contribution to the company's bottom line. Rather, it is based on some vague insurance value. Such an investment has to be evaluated in terms of how much it minimizes management regret. Justification based on the prevention of negatives is much more difficult to sell.

## Enhancements

SCE's overriding concern for the safety of its nuclear plant, and the recent negative events in the industry, have motivated them to continually test and enhance their system. The recent addition of integrated voice and data links between the EOF and the Emergency News Center, and the EOF and the state Office of Emergency Services, are two examples of recent refinements.

The scheduled enhancement of the data transmission network from its current slow speed (9.6 kilobits per second to 19.2 kilobits per second) to a much higher speed (1.5 megabits per second) will require significant changes in the existing network. This faster transmission speed will permit the use of high speed printers, faster data transfer, and easier expansion of the video conferencing system.

The addition of an interactive video conferencing link between the EOF and headquarters has been in place for approximately six months. This system refinement required a special transmission network because of the large bandwidth requirements (i.e., 1.5 megabits, duplex) of compressed video conferencing. This addition also required more justification than the integrated voice and data links because of the significant cost involved (i.e., \$155,000 per site for the equipment, and approximately \$100,000 for the changes in the existing microwave transmission network).

## Generic Prescriptions for the Design and Implementation of Information Systems for Crisis Management

The SCE crisis context is one of the most severe, complex, and intense situations that any organization needs to plan for, and yet shares the same generic characteristics of all crises. It, therefore, illuminates a wide variety of options for the design and implementation of information systems for any crisis context.

The general prescriptions that we present below are based on three sets of inputs. First, and most influential, are the lessons that we have learned from the SCE experience. Second, we have attempted to integrate what practitioners of crisis management have reported and suggested. Third, we have incorporated what we know in general about designing and implementing information systems. We have synthesized these three sets of inputs to produce a generic set of prescriptions for designing and implementing information systems for crisis management in the following seven steps (see Figure 3).

1. Acknowledge Inevitability of Crises: The biggest and most difficult step that an organization must take towards effective crisis management is acknowledging and accepting the inevitability of crises. Organizations must include the “unthinkable” as an integral part of top management strategic planning. Thinking about potential crises ahead of time helps diffuse emotional reactions to them [9].

2. Identify Critical Areas of Vulnerability: This step can be likened to an inverted Critical Success Factors (CSF) method, where critical areas of company operations that are vulnerable to possible crises are identified. It could also be combined with the CSF method, and points of vulnerability for each CSF determined.

Figure 3. Procedure for Designing and Implementing Information Systems for Crisis Management  
![](/api/attachments/975NJFJ5/fulltext/images/1bbb0576b46188e6565450004c28660abf966df6e180e6b23f83e8b9c08b335a.jpg)

3. Identify and Classify Potential Types of Crises: For each critical area of vulnerability, identify whether there are any technological, confrontational, malevolence, or management failure potential crises. Classify each type of crisis according to its potential severity. Top management must decide the priority level of each type of crisis in terms of allocating resources to crisis management planning.

4. Develop Crisis Management Contingency Plans: Once the priority levels are set, contingency planning can begin. This includes:

\- Assembling crisis management teams — identifying the crisis decision making team, the front-line crisis team, the emergency news center team, the headquarters support team, the external experts, critical stakeholders, and outside support agencies (see Figure 4).

\- Prescribing key decisions on the “mechanical” portions of the crisis.

\- Creating scenarios for the less predictable aspects of the crisis.

Figure 4. Generic Crisis Support Organization  
![](/api/attachments/975NJFJ5/fulltext/images/7e0c0b10cc0c44ccfe1cd20ff42efa1bed6cbbabdf92f1aea022ac9167ab70d8.jpg)

5. Develop Information Systems for Crisis Management: It is only after the previous four steps are completed that developing a crisis information system can be effectively accomplished.

\- Perform a human communication network analysis to determine communication nodes and sources, potential communication bottlenecks, and how much information is required (i.e., voice, data, and/or video) to prevent miscommunication.

\- Perform a communication network analysis to determine what kinds of links are required for crisis peak loads (e.g., voice-only, data-only, integrated voice-data, integrated voice-data-video; dedicated or dial-up; private or public connection).

\- Develop a quick and easy updating method for frequent changes in the information system based on tests, changes in crisis priorities, changes in personnel, and improvements in technology.

\- Select/design hardware and software for preset procedures.

\- Select/design hardware and software for less predictable events.

\- Develop early warning information systems that will trigger alerts and preset responses.

6. Conduct Crisis Drills and Exercises: Drills and exercises are necessary to simulate real crises, and provide valuable feedback about the strengths and weaknesses of a company's crisis management system [5]. They are particularly useful in providing constant tests of the ability of a company's information system to provide immediate, reliable, and clear information during different types of crises.

\- Drills give crisis team members the opportunity to think through their tasks without the pressure of being graded.

\- Exercises should occasionally be unannounced to more closely simulate the pressures of a real crisis.

\- Exercises should be graded to show team members how well they have performed.

\- Records of exercise performance should be kept for comparison and learning.

7. Use Crisis Information Technologies for Day-to-Day Situations: One of the best ways to maintain the reliability of a crisis information system is to have personnel use its components for day to day operations whenever possible. This will also help crisis team members maintain confidence in the system, as well as become accustomed to new information technologies which are introduced into the system.

## Conclusions

There is ample evidence that crises are inevitable in the business environment. Similarly, there is evidence that the potentially negative effects of business crises can be mitigated by advance crisis management planning. However, this has not spurred top management to pay sufficient strategic attention to crisis management and its accompanying information system requirements.

There is a need for information systems that can leverage the management decision making process during crises. As organizations and their MIS functions have risen to meet the challenge of using information systems for competitive advantage and for creating strategic opportunities, so must they now respond to the challenge of using information systems to meet oncoming crises. Information systems for crisis management are too vital to be left to chance.

## Acknowledgement:

We would like to extend our thanks to the management of the Southern California Edison Company for their support in making the writing of this paper possible, especially: David J. Fogarty, Executive Vice President; Edward J. Faeder, Manager of Environmental Operations; and Lewis M. Phelps, Manager of Corporate Communications.

## References

[1] Billings, R.S., Milburn, T.W., and Schaalman, M.L. "A Model of Crisis Perception: A Theoretical and Empirical Analysis," Administrative Science Quarterly, Volume 25, Number 2, June 1980, pp. 300-316.

[2] Business Week "How Companies are Learning to Prepare for the Worst," December 23, 1985, pp. 74-76.

[3] El Sawy, O.A., and Evans, J.S. "Becoming Proactive Surprise Managers," The President, American Management Association, New York, New York, November 1985.

[4] Fink, S. Crisis Management: Planning for the Inevitable, American Management Association, New York, New York, 1986.

[5] Gray, P. and Borovits, I. "Gaming and Group DSS," in J. Fedorowicz, (ed.), DSS-86 Transactions, The Institute of Management Sciences, Providence, Rhode Island, 1986, pp. 165-175.

[6] Holsti, O. "Limitations of Cognitive Abilities in the Face of Crises," in Studies on Crisis Management, C.F. Smart and W.T. Stanbury (eds.), Institute for Research on Public Policy, Butterworth, Toronto, Canada, 1978, pp. 35-52.

[7] Housel, T.J., Schornstein, H., and Donovan, P.F. "Video Teleconferencing in the Power Industry," Public Utilities Fortnightly, Volume 117, Number 10, 1986, pp. 53-57.

[8] Kwong, B. and Housel, T.J. "Three Mile Island: A Communications and Telecommunications Analysis," Working Paper, University of Southern California, Los Angeles, California, 1986.

[9] Lerbinger, O. Managing Corporate Crises: Strategies for Executives, Barrington Press, Boston, Massachusetts, 1986.

[10] Minoli, D. "Protecting Communications from Disaster," Infosystems, Volume 33, Number 2, February 1986, pp. 38-40.

[11] Mitroff, I. and Kilmann, R. Corporate Tragedies: Product Tamperings, Sabotage, and Other Catastrophes, Praeger Publishing, New York, New York, 1984.

[12] Phelps, N.L., "Setting up a Crisis Recovery Plan," Journal of Business Strategy, Volume 6, Number 4, Spring 1986, pp. 5-10.

[13] Pincus, T.H. "A Crisis Parachute: Helping Stock Prices Have a Soft Landing," Jour-

nal of Business Strategy, Volume 6, Number 4, Spring 1986, pp. 32-38.

[14] Rogers, E.M. and Rogers, R.A. Communication in Organizations, The Free Press, New York, New York, 1976.

[15] Spiller, R. and Housel, T.J. "Using Video Teleconferencing," Sloan Management Review, Volume 26, Number 4, Fall 1985, pp. 67-89.

[16] Time Magazine, “Anatomy of a Catastrophe: Moscow Biames ‘Gross’ Human Error for Chernobyl Accident,” September 1, 1986, pp. 26-29.

[17] Time Magazine, “Coping with Catastrophes: Crisis Management Becomes the New Corporate Discipline,” February 24, 1986, p. 53.

## About the Authors

Thomas J. Housel is an Assistant Professor of Business Communication at the University of Southern California School of Business. He received his Ph.D. from the University of Utah. He has served as a consultant for IBM, Hughes Aircraft, Southern California Edison and other companies. His research on telecommunications and organizational communication problems appears in such journal as the Sloan Management Review, Telematics and Informatics, and the Journal of Business Communication. He is the author of the forthcoming book, Introduction to Telecommunication: The Business Perspective due to be published by South-Western Publishing in 1987.

Omar A. El Sawy is an Assistant Professor at the Center for Futures Research, Graduate School of Business Administration, University of Southern California. He holds a BSEE from Cairo University, an MBA from the American University in Cairo, and a Ph.D. from the Graduate School of Business, Stanford University. Omar has been active in the computer field since 1968, including seven years with NCR Corporation, and four years as manager of computer services at the Hoover Institution, Stanford University. His research and teaching interests straddle the information systems and the strategy area. He is the author of two previous M/S Quarterly articles.

Paul F. Donovan is the Supervisor of Video Services at the Southern California Edison Company and has been with SCE for 14 years in the Corporate Communications function. His responsibilities include management of the video conferencing facilities. He holds an MA in Communications from the Annenberg School of Communications, University of Southern California. He has won numerous awards for his industrial videotapes and films produced for Southern California Edison. His most recent publication appears in Public Utilities Fortnightly.
