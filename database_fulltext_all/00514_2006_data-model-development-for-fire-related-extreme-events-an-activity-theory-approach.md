---
otero_id: 514
otero_key: "EMFX93WF"
title: "Data Model Development for Fire Related Extreme Events:  An Activity Theory Approach"
authors: "Rui Chen; Raj Sharman; Raghav Rao; and Shambhu J. Upadhyaya"
year: "2006"
journal: "MIS Quarterly"
doi: "10.25300/misq/2013/37.1.06"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# DATA MODEL DEVELOPMENT FOR FIRE RELATED EXTREME EVENTS: AN ACTIVITY THEORY APPROACH<sup>1</sup>

Rui Chen Information Systems and Operations Management, Miller College of Business, Ball State University, Muncie, IN 47306 U.S.A. {rchen3@bsu.edu}

Raj Sharman Management Science and Systems, School of Management, State University of New York at Buffalo, Jacobs Management Center, Buffalo, NY 14260 U.S.A. {rsharman@buffalo.edu}

H. Raghav Rao Management Science and Systems, School of Management, State University of New York at Buffalo, Jacobs Management Center, Buffalo, NY 14260 U.S.A. and Department of GSM, Sogang University, Seoul, SOUTH KOREA {mgmtrao@buffalo.edu}

Shambhu J. Upadhyaya Computer Science and Engineering, School of Engineering and Applied Sciences, State University of New York at Buffalo, 201 Bell Hall, Buffalo, NY 14260 U.S.A. {shambhu@buffalo.edu}

Post-analyses of major extreme events reveal that information sharing is critical for effective emergency response. The lack of consistent data standards for current emergency management practice, however, hinders efficient critical information flow among incident responders. In this paper, we adopt a third-generation activity theory guided approach to develop a data model that can be used in the response to fire-related extreme events. This data model prescribes the core data standards to reduce information interoperability barriers. The model is validated through a three-step approach including a request for comment (RFC) process, case application, and prototype system test. This study contributes to the literature in the area of interoperability and data modeling; it also informs practice in emergency response system design.

Keywords: Data model, extreme events, design science, activity theory

## Introduction

Communication interoperability is crucial to interorganizational communications among various response agencies (e.g., local, state, and federal) (Townsend 2006). The U.S. Department of Homeland Security (DHS) has pointed out that response agencies typically use systems that are heterogeneous and independently operated and managed (DHS 2004). When these systems are not interoperable, response agencies cannot share task-critical information in a timely manner. To date, there is a lack of data standards adequately designed to address interagency communication for day-today extreme incidents such as fire (Chen et al. 2008c).

![](/api/attachments/EMFX93WF/fulltext/images/fd46632af5a075439218231511191ae9341058a555a41a847f43d668dc3d6777.jpg)  
Figure 1. Responses in the Baltimore Tunnel Fire

In the United States, fire is one of the most common emergency incident types (Karter 2008). A typical response to fire incidents involves multiple agencies. Thus sharing of taskcritical information is imperative to enable coordination and collaboration among the participating agencies. For example, on July 18, 2001, a CSX Transportation train caused a tunnel fire in Baltimore, Maryland. During the two-day response period, a total of 17 engines, 8 trucks, 3 battalions, and 150 firefighters responded, along with police and emergency medical services (EMS) (see Figure 1a). Further, the remote management team at the emergency operations center (EOC) had to support collaboration with more than 10 agencies at city, state, and federal levels (see Figure 1b). To manage this kind of incident, it is vital to share task-critical information on precise locations within the scene, information on hazardous conditions, injury and casualty data, and response tactics and progress among responders, as scene related information unfolds, to enable informed decision making and collaboration.

![](/api/attachments/EMFX93WF/fulltext/images/17181789ea9e70061792bbdd85554c74fb44202989cd53a3fdb60dd2b10922e5.jpg)  
Figure 2. Example Document Used for Fire Incidence Response

An examination of response documents (see Figure 2) that are typically used in fire incidents including the Baltimore tunnel fire reveals that much of the task-critical information is not yet supported by existing emergency data standards, such as the National Information Exchange Model (NIEM). Most of the existing standards support information sharing within the boundaries of individual occupational communities (e.g., public health); none of them supports the day-to-day response operations in fire incidents. The lack of emergency data standards introduces communication barriers and hampers information exchange among responders (Chen et al. 2008a; Rao et al. 1995; Sanchez-Ruiz et al. 2008).

This paper makes two contributions. First, it presents an improved data model development methodology that is based on an extension of activity theory. Constructs such as timeline, environment, and transition were created as additions to activity theory in order to better explain information sharing in the context of a fire incident response. An analysis of multiple activity systems (i.e., on-site response and EOC response) was used to elicit requirements and capture activities with the temporal sequence of development, multi-stage transitions, and two levels of reinforcing feedback (i.e., within-stage and between-stage feedback). Second, this paper develops and validates an object-oriented data model that supports real-time response-information exchange during a fire incident response. The data model has been cultivated with support and collaboration from the emergency community, and has been presented to target users whose feedback has been incorporated. Based on the data model, our study also develops a prototype system that allows a responder to provide scene-based information using handheld devices. It includes suggestions for dealing with specific fire related issues that can be communicated to other responders including the incident commander. The prototype also includes the capability to communicate live scene feeds from responders, making the task of understanding the scene much easier. The innovations that are developed in the current study therefore extend responders’ capabilities in task critical information sharing.

To summarize, we follow the design science research guidelines proposed by Hevner et al. (2004) and others (Peffers et al. 2008; Purao et al. 2008):

(1) Develop a data model that standardizes task-critical information for fire-related incident management.

(2) Incorporate an extended activity theory approach that improves emergency management practice with a validated data standard

(3) Carry out a research evaluation using a three-step approach:

• initiate a request for comment (RFC) process

employ a case study to show the value of the data model

develop a prototype system and demonstrate it to fire chiefs and other first responders

In the remainder of this paper, we first examine the existing literature on emergency data interoperability and activity theory. We then present the new data model development methodology. Next, we explore example elements of this fire response data model. We further highlight the data model’s quality and validation. Finally, we discuss the paper’s implications and limitations, and suggest directions for future research.

## Background and Theoretical Framework

In this section, we present the theoretical framework that directs the data model development. We first explore the interoperability issues in emergency communication and identify existing research gaps. Subsequently we introduce third-generation activity theory and discuss its potential in eliciting and understanding the requirements in the data model development process.

## Emergency Interoperability

The existing response information systems of emergency response organizations are somewhat fragmented, localized, and technologically disconnected (Frale 2005; NIEM 2007). The heterogeneity of these systems typically causes communication non-interoperability and interrupts information flow. Even among similar organizations such as fire companies, the way that information is shared and managed may differ from county to county (Chen et al. 2007).

The foundation for communication interoperability is datalevel interoperability, which establishes a common semantic understanding among participating organizations and ensures that data are structured in a semantically consistent manner. A number of emergency-related data standards have been developed by the public and private sectors (DHS/DOJ 2006; DOJ 2005; E9-1-1 2006; EIC 2005; HL7 2006; NEMSIS 2007; OASIS 2006; PHIN 2005). Among these data standards, maximum progress toward promulgation of an emergency data standard has been achieved through the National Information Exchange Model (NIEM). NIEM was developed by the U.S. Department of Justice (DOJ) and the DHS and is designed to “facilitate timely, secure information sharing across the whole of the justice, public safety, emergency and disaster management, intelligence, and homeland security enterprise” (DHS/DOJ 2006). An increasing body of literature has examined NIEM for its impacts and management issues (Gil-Garcia et al. 2009; Hayes-Roth et al. 2008).

A collection of data standards, NIEM contains 828 data types and 4,090 data properties that seek to standardize information pertaining to justice, intelligence, immigration, emergency management, international trade, and infrastructure protection (DHS/DOJ 2006). NIEM standards are organized in an object-oriented structure, which is represented using an XML schema for the purpose of consistent definition and seamless transmission of information.

The existing NIEM standards on emergency management are narrowly defined around alarm events, resources, and message distribution. With regard to the complexity of emergency management, a great amount of information is missing for day-to-day emergency operations and large-scale, multiple-hazard incidents. Based on public documents available in the Baltimore tunnel fire, it is clear that, for example, key data elements on fire spread, structure damage, and response operations are all missing from NIEM standards. In this paper, we develop a data model that standardizes the core data shared and exchanged during a fire incident response.

## Activity Theory

The development of a data model requires systematic approaches to elicit and analyze the internal elements, structures, and relationships of the data elements (Zowghi and Coulin 2005). In this paper, we use activity theory to guide the requirements gathering process (Engeström 1987, 1999). Activity theory provides a lens to analyze the computersupported activity of a group or organization and to study the design of artifacts for individuals and organizations.

Activity theory suggests that human activity is directed toward an object, mediated by artifacts or instruments, and socially constituted within the surrounding environment (Bertelsen and Bodker 2003; Vygotsky 1978). Activity can be understood as a structure with various sub-activities that are collated or extended away from the core activities (Bertelsen and Bodker 2003). The subject is the active element of the process; it can be either an individual or a group. The object transformed by the activity can be either an ideal or material object (Fuentes et al. 2003). The transformation process is enabled and supported by various instruments, either physical or logical. Each instrument provides the subject with the experience historically collected by his or her community (Fuentes et al. 2003). During the interaction, subjects internalize and/or externalize their cognitive schemes and their understanding of the relationship between themselves and the external objects, instruments, surroundings, and other factors.

First-generation activity theory focused on individual action and studied the concepts of subject, mediating artifact (i.e., instrument), and object (Vygotsky 1978). Second-generation activity theory focused on collective activity and studied a single-activity system, including the concepts of subject, instrument, object, rules, community, and division of labor (Leont’ev 1978). The most recent version of this theory, third-generation activity theory, suggests the use of multiple interacting activity systems to investigate complex social activities (Engeström 1987). In doing so, it provides a more refined and detailed account of the embedded issues of the research topic (Chaudhury 2001; Shankar et al. 2011). In this study, we apply third-generation activity theory to understand the requirements for data model development in fire-related emergency communication.

![](/api/attachments/EMFX93WF/fulltext/images/d7dff9220b1ef2a59984f65b1d9102dcecec7293d5824b0bf5f20c459f00ba9f.jpg)

Emergency response is a complex phenomenon that develops as the incident response and mitigation efforts unfold. The principal components (e.g., subject) of emergency mitigation change depending on the circumstances, and the response operations are influenced jointly by both social (e.g., community) and technical (e.g., instrument) factors whose relationships undergo frequent restructuration. By applying activity theory, we may investigate emergency response along dimensions of subject, activity, instrument, community, rule, and division of labor. In our study, we capture all of these key data elements in our data model and standardize them to ensure higher data interoperability.

## Data Model Development

To support communication during a response to a fire incident, we sought to develop a data model that standardizes the key information to be shared and exchanged. A data model is a precise and unambiguous representation of organizational information requirements (Hull and King 1987; Peckham and Maryanski 1988). In this section, we apply the discussion introduced in the preceding section to facilitate the data model development process. The development methodology is outlined in Figure 3. To gain an initial understanding of fire response and its communication needs, we collected more than 40 documents and notes from fire response organizations in the western New York area. These included fire incident response technical data forms, fire incident response dispatch forms, field notes and chronological logs, fire incident messaging systems (e.g., National Fire Incident Reporting System-NFIRS; DOS/DOJ 2006), and fire response plans. We then contacted eight first responders with expertise and experience in responding to fire-related emergencies. Through semi-structured interviews, we solicited typical response and information-sharing practices that occur during a fire response from practitioners. The involved response organizations and experts were identified mainly through a top-down internal referring approach starting with the Deputy Chief, Department of Emergency Services of Erie County, New York. These sources provided a systematic foundation for the data model development.

We then extracted the response task-critical data from the above sources using third-generation activity theory as a guideline to understand fire response phenomenon. We first identified the major emergency activity systems that exist in a typical fire response. Based on the inputs collected from both the local response community and the existing literature of emergency management (Chen et al. 2008b), it became clear that incident response may consist of both on-site and EOC (remote) operations.

On-site response is reactive in nature, as responders identify and mitigate the immediate threats. Such responders operate within a very limited time window and work with the local picture stemming from the confined scene. Meanwhile, the overall incident response may be supervised by a remote structure such as EOC. EOC deals with strategic issues and works with a global picture, leveraging external resources to assist with the on-site response. The EOC-guided actions are based on a more reflective and proactive posture, and EOC commanders typically operate with a large time window. The on-site response and EOC response focus on distinct response tasks, constraints, and outcome quality. Specifically, the onsite response addresses immediate mitigation needs, while the EOC response oversees and supports the former—for instance, with resources and information.

Through the lens of third-generation activity theory, we examined these two activity systems to capture task-critical data along the multiple dimensions informed by activity theory. At the EOC level, supervisors and officials in the affected area initiate fire response through information exchange (e.g., dispatch systems) and provision of supportive response equipment. The actions undertaken are influenced by the existing rules (e.g., mutual aid agreements between municipalities), the nature of the community (e.g., government, profit, and nonprofit organizations), and the division of labor (e.g., resource acquisition, transit, and distribution tasks). Meanwhile, at the on-site level, first responders work to put out the fire. On-site responders’ efforts are facilitated by communication (e.g., field notes and command sheets) and equipment on hand, and their operations are influenced by rules (e.g., standard operating procedures in firefighting), the nature of the community (e.g., fire, police, and EMS), and division of labor (e.g., command, planning, and operation). Both EOC and on-site response activities are closely centered on the fire and the two groups of responders make direct contributions to mitigating the fire. As a result, the two systems of response activities share the same object (fire) and the outcome (i.e., the mitigated fire) as well.

Third-generation activity theory also incorporates contradiction analysis. Contradictions are important for system design, in that they indicate emergent opportunities for activity development and can be used as sources of improvement (Kuutti 1991). Contradictions may take place either inside the key constructs (e.g., subject) or between them (Engeström 1999). In the context of fire incident response, there exist a number of contradictions among the on-site and remote response activities. For example, on-site response agencies often compete to fill the incident commander position when they arrive on scene. Most of the time, the resolution of this contradiction is determined by the incident type. If there is a criminal aspect to an incident, law enforcement agencies are in charge of the scene; otherwise, a fire chief is in charge. To resolve such possible contradictions and support efficient incident response, we identified incident category as a relevant data element and added it to the data model. Similar contradictions also exist in EOC response activities.

We illustrate the application of third-generation activity theory to fire incident response in Figure 4. As depicted in the figure, the fire response consists of two activity systems that interact with each other. Each activity system may be analyzed in terms of the dimensions of subject, instrument, object, rule, community, and division of labor.

Table 1 presents an illustrative set of data model elements that were derived from the application of third-generation activity theory.

While it successfully captures multiple pertinent issues, activity theory fails to recognize other imperative matters that are integral to emergency response. In order to capture taskcritical data that are not recognized by activity theory, we extended this theoretical framework in a number of ways. The extension was informed by a conjunction of (1) recognition of the existing limitations of activity theory and (2) key characteristics of the research phenomenon under investigation. Since its inception, activity theory has invited critiques for its limited presentation of social activities and researchers have made calls to extend this theoretical framework (Davydov 1999; Lektorsky 1999). Several issues stand out in the area of emergency management research: natural and social environment (Jaegar et al. 2007; Lorincz et al. 2004), activity timeliness (Chen et al. 2008b; Turoff et al. 2004), and transitions inside and between activity systems (Fischer 1998; Wallace and De Blogh 1985). These issues were noted in our interviews with the first responders as well. Expansion of activity theory along these dimensions enables the depiction of a complete picture of emergency response and therefore makes the extension from both a theoretical and practical perspective. These extensions are also applicable to other social activities and environments.

We started by broadening the traditional formalisms of activity theory (Engeström 1987) to consider environment as an important construct. Environment, either natural or social, may influence how an activity unfolds and affect the outcome that follows. Unlike subject, community, or rule, which are defined in the traditional formalisms of activity theory as being closely tied to a given activity, environmental influences are not activity specific. The same environment setting may affect multiple concurrent activities that take place within its vicinity. For example, the concern for social environment may affect different subjects simultaneously and direct their operations. The concerns of the social environment (e.g., public safety) may affect the EOC response, while the concerns of the natural environment (e.g., rain and wind speed) may shape on-site response. The various environment factors were included in the data model so that task-critical data could be communicated among the involved agencies.

![](/api/attachments/EMFX93WF/fulltext/images/212a092171b338b50b27087a94f5b28d42e1016507d6c6e437cbf1bb4791dc5e.jpg)  
Figure 4. Application of Third-Generation Activity Theory on Emergency Communication (On-Site and EOC)

In addition, we extended activity theory to include timeline as a relevant construct. While it views social activities as developing systems with a long history, activity theory does not explicitly consider timeline, or temporal sequence, as an integral component in the analyses of social activities. In our study, we extended the traditional formalisms of activity theory to include timeline in a considerably different manner from the prior literature (Iivari and Linger 1999; Kofod-Petersen and Cassens 2006). We argue that temporal sequence is inherent to all social activities and affects other major constructs in activity theory. In a given activity system, the timeline records the progress of the activities and reveals the pattern of the development. In a fire-related incident, emergency response activities take place throughout the course of incident development. As the incident unfolds, responders react accordingly, changing their tactics and operations as necessary to reflect changing threats and response priorities. By following the timeline concept, we were able to break down the emergency response activities and understand them with high granularity.

Table 2 illustrates the concepts of environment and timeline in data model development.

Table 1. Examples of Data Model Elements Informed by Activity Theory

<table><tr><td colspan="2">Activity Theory Concept</td><td>On-Site Response</td><td>EOC Response</td></tr><tr><td rowspan="3">Subject</td><td>Definition</td><td>Individual on-site responders who provide immediate mitigation to the fire incident.</td><td>Individual response organization principals, supportive agent representatives, and emergency managers.</td></tr><tr><td>Design implication</td><td>The subjects involved in mitigation need to be identified so as to learn their individual experiences and viewpoints that are operation-oriented.</td><td>The subjects involved in supervision need to be identified so as to learn their individual experiences and viewpoints that are management-oriented.</td></tr><tr><td>Derived data elements</td><td>Response personnel's expertise and training.</td><td>Response personnel's organizational affiliation—title and position.</td></tr><tr><td rowspan="3">Object</td><td>Definition</td><td>Fire.</td><td>Fire.</td></tr><tr><td>Design implication</td><td>The data standard should capture the details of an ongoing fire and its immediate threats.</td><td>The data standard should recognize the impacts that the ongoing fire poses to the community.</td></tr><tr><td>Derived data elements</td><td>Fire spread, rate of spread, and fuel.</td><td>Affected area and affected size.</td></tr><tr><td rowspan="3">Community</td><td>Definition</td><td>Core emergency services such as fire and rescue, law enforcement, emergency medical personnel, and hazardous materials teams.</td><td>Supportive emergency agencies (regional, state, and federal) and organizations (private and public).</td></tr><tr><td>Design implication</td><td>The data standard should consider the different perspectives (e.g., daily routine) each subcommunity brings. Also consider the perspective differences within the subcommunity (e.g., among different fire companies).</td><td>Requirements should be elicited from multiple municipalities and across local, state, and federal hierarchy. Also consider the differences in information artifacts those organizations have currently adopted.</td></tr><tr><td>Derived data elements</td><td>Response organization's name, ID, and contact.</td><td>Response organization's category (government/private/non-profit organization).</td></tr><tr><td rowspan="3">Instrument</td><td>Definition</td><td>Field note, tactical command sheet, and equipments (e.g., fire engines).</td><td>Interagency dispatch system, fire incident messaging systems, and mitigation equipments.</td></tr><tr><td>Design implication</td><td>Existing forms and documents used by first responders should be studied to identify the core data elements; response resources should be captured.</td><td>Existing paper-based files and digital archives of the participating agencies and organizations should be examined; response resources should be captured.</td></tr><tr><td>Derived data elements</td><td>Regulation document title, author, and version; resource name, ID, description.</td><td>Generalized; same as rule elements of on-site response.</td></tr><tr><td rowspan="3">Rule</td><td>Definition</td><td>Standard operating procedures, training manuals, operation guidelines, codes, chain of command.</td><td>Emergency management mutual-aid agreements, public safety initiatives, reporting policies.</td></tr><tr><td>Design implication</td><td>The data standard should study the operational rules, especially those set by the incident command system (ICS) prescribed by Department of Homeland Security. The ICS imposes protocols on emergency operation.</td><td>The repository of response-related policies should be studied to design the data standard. Also examine the typical EOC procedures, including those pertaining to information storage, transmit, and access control.</td></tr><tr><td>Derived data elements</td><td>IMS unit category, established date, and sub-unit.</td><td>Last updated date, last verified date, quality comment, reliability numeric.</td></tr><tr><td rowspan="3">Division of Labor</td><td>Definition</td><td>Standard on-site response tasks and job assignments.</td><td>Collaborative participation of general stakeholders.</td></tr><tr><td>Design implication</td><td>On-site emergency response assignments and action plans to generate data labels for the patterns in on-site mitigation should be examined.</td><td>The inter-agency collaboration processes should be studied to generate data labels that support the strategic response supervision dynamics.</td></tr><tr><td>Derived data elements</td><td>Response activity—ID, category, description.</td><td>Resource distribution schedule—estimated departure date, committed date, and arrival date.</td></tr><tr><td rowspan="3">Contradiction</td><td>Definition</td><td>Tensions within and between local responders onsite.</td><td>Tensions within and between remote management and support teams.</td></tr><tr><td>Design implication</td><td>The data model should explore the standard operating procedures to identify likely conflicts in the on-site mitigation process.</td><td>The emergent collaboration and coordination among affiliated teams and management centers may be reviewed for potentially problematic issues.</td></tr><tr><td>Derived data elements</td><td>Incident category, location district.</td><td>Information sensitivity level response, personnel security clearance level.</td></tr><tr><td colspan="3">Theoretical Construct</td><td>Informed Data Model Elements</td></tr><tr><td colspan="2"></td><td>On-Site Response</td><td>EOC Response</td></tr><tr><td rowspan="3">Environment</td><td>Definition</td><td>Natural setting (e.g., temperature, barometer, wind direction)</td><td>Social and economic threats, long-term threats to property and life</td></tr><tr><td>Design implication</td><td>Natural environmental elements need to be captured and labels generated to specify their properties</td><td>Social environmental elements need to be captured and labels generated to specify their properties.</td></tr><tr><td>Data elements</td><td>Weather temperature, barometer, and wind speed</td><td>Environment fate and toxicity, population density</td></tr><tr><td rowspan="3">Timelines</td><td>Definition</td><td>Temporal sequences of the on-site incident mitigation operations</td><td>Temporal sequences of the managerial control and oversight operations</td></tr><tr><td>Design implication</td><td>Major transitions of the on-site fire response should be captured to reflect the chain of operations and the nature of mutual communications</td><td>EOC activation sequence and operation stages should be recorded to understand the nature of communications in and out of the management center</td></tr><tr><td>Data elements</td><td>Alarm date and time, overhaul date and time</td><td>Response facility activated date and time</td></tr></table>

Additionally, we extended activity theory to consider transition as an important perspective. Our analyses of activity system transitions allowed us to observe the development of emergency response activities and to capture important data elements into the data model. Boer et al. (2002) studied temporal interconnectedness among multiple heterogeneous activity systems. Our work suggests that any single-activity system may also experience transitions, and that this system may expand or shrink during its course of development.

Management of incidents in general involves three stages: preplanning, response, and recovery (DHS 2008). Emergency activities flow throughout all of these stages, with the activity system first growing and then collapsing along the course of the timeline. While the components (e.g., subjects, objects, and rules) of the activity system sharply differ, operations at the varying stages are correlated. Specifically, they share portions of task-critical data that can be incorporated into data model development.

Recognition of these transitions has major implications for the fire incident data model. The study described here focused on the fire response stage. From the preplanning stage to the response stage, task-critical data is generated and passed on. In preplanning, for example, the local emergency management agency assesses the jurisdiction and identifies the vulnerabilities in terms of fire incidents. The agency may inspect building structures and collect data on floor maps, water sources (e.g., fire hydrants), and clean agents (e.g., automatic extinguishing systems). Further, the agency may examine the primary use of the specific property (e.g., restaurant, school, hospital, etc.). Should an incident then occur, such data can assist the responders at the response stage in developing an appropriate intervention strategy, be it passive or active. We therefore captured and standardized these data in the data model, because they can be communicated among the stakeholders during the fire response stage.

Likewise, the incident response may generate and pass to the recovery stage the data on fire liability, equipment usage and damage, and estimate of loss. Such data facilitate the auditing, reimbursement, and renovation processes. We therefore incorporated and standardized the data in the data model so that they may be captured and made ready for use later. Through transition analyses, we enhanced the data model so that it supports fire response and mitigation and maximizes its support to the overall emergency management effort.

We also suggest that reinforcing feedback may exist both within and between the transition stages of an activity system. Feedback is an implied part of activity theory (Bardram 1998; Engeström et al. 1997; Foorthuis et al. 2008). Feedback can influence and improve—directly or indirectly—the development of an emergency management system (Zhang and Bai 2005). During a fire incident, responders provide feedback to one another, thereby reinforcing the best practices of fire response. For example, response performance data (e.g., the evaluation of a response operation plan and the result of a response activity) may become available in real time during the incident response, allowing decision makers to incorporate those data into their oversight of ongoing operations. If an ongoing operation fails to meet its objective, responders search for and execute corrective actions in an attempt to increase the operational effectiveness and efficiency. Responders may also provide feedback on the emergency management strategies as they brief the incoming response team on the response progress, allowing the latter to properly interpret the operations undertaken and to modify them if necessary.

![](/api/attachments/EMFX93WF/fulltext/images/bd4465ae743309bd60265215170c2e280107a631ccc5632c8ebc3d92eafadcff.jpg)  
Figure 3. Application of Transition and Feedback Perspectives in Emergency Response

In addition, feedback may be given during the transitions in the emergency management life cycle. For example, in the aftermath of an incident, the performance data on response and mitigation may be passed on to emergency professionals at the recovery stage, who then analyze the data to generate after-action reports and recommend changes for improvements in the future (e.g., using four fire engines instead of three for the response to a fire incident of similar size). Once retrieved and circulated among agencies in the next preplanning stage, these reports and recommendations enable the local community to implement the proposed changes and revise their existing plans. In this way, while originating from the current-incident response, the feedback-related data ultimately benefit the next-incident response. We therefore incorporated and standardized the feedback data elements in the data model so that they could be preserved and used to reinforce improvements in incident response during and after an incident.

The concepts of transition and feedback are illustrated in Figure 5. Figure 5 also provides example data elements (i.e., data types and properties) that draw on the concept of transition and feedback ideas. Once the fire response was analyzed and data elements captured, we continued to define data elements with formal definitions. We also organized data elements into either data properties or data types. A data type is a structure that carries values associated with a real-world entity, whereas a data property is a characteristic of a thing.

The creation of new data types benefits directly from the NIEM data standard following the object-oriented principle. For example, the NIEM standard contains a PersonType with built-in properties (e.g., person name, date of birth, gender). To create a ResponsePersonnelType, we established that ResponsePersonnelType that inherited its base properties from PersonType and then added new properties (e.g., expertise, training, and security clearance level) to Response PersonnelType that are unique to responders. Through inheritance, existing properties in NIEM PersonType are automatically inherited into ResponsePersonnelType, thereby avoiding the overhead in redeclaring and redefining these properties in the new data model.

![](/api/attachments/EMFX93WF/fulltext/images/2bd314d9b73843313104bcc5706628dfe2a465253a610889e73091d1c95bf218.jpg)

Furthermore, we added a set of important metadata to the data model, where the metadata was inspired by the considerations discussed earlier in this paper. Metadata for all the emergency communication messages may include the message sender, message recipient, expiration date, expiration time, language, reliability numeric (i.e., accuracy of the content), and sensitivity level, among other things. These items are important to ensure data accountability, confidentiality, and reliability in the emergency response (Rice et al. 2004).

We also developed a number of symbolic icons to facilitate the information processing of data model elements based on ANSI Z535.2 (www.ansi.org) and ISO3864-2002 (www. iso.org) code and symbol standards. Emergency responders must process information under extreme time constraints. The use of symbols in data communications helps the sender to prioritize the message contents (e.g., safety-related issues) and facilitates the receivers in attending to and interpreting the content efficiently. Symbolic icons may serve a number of purposes: (1) to alert persons of an existing or potential hazard, (2) to identify the hazard, (3) to describe the consequences of exposure to the hazard, and (4) to instruct persons about the appropriate measures needed to avoid the hazard. An example symbolic icon is provided in Table 3. The symbols use graphics—visual signs—to provide a universal nonverbal recognition of the hazard. The color of each symbol establishes the connection between the symbol with the underlying facts (e.g., red implies danger). Additionally, the symbols use brief text messages to convey supplementary information. Such text is important for responders who are color blind and, therefore, unable to recognize the symbol colors.

We used XML to specify and record the fire response data model. Where the response agents are concerned, XMLbased dictionary specification allows the platforminterdependent utilization of data standards and the development of automated information processing tools (DOJ 2005; March et al. 2000; Mendling and Nuttgens 2006; W3C 2008). In the rest of this section, we present the data model developed for fire response communication.

## Data Model Components

Response data may be classified into two major categories: threat assessment and incident command (Chen et al. 2008a). Threat assessment concerns the facts of fire incident occurrence as well as its consequences, including data related to the incident setting, fire hazard, and threat. Incident command addresses the response management structure and response operation details. In this section, we introduce the data model along these dimensions.

## Threat Assessment

Threat assessment is an important response task in which response agents analyze the incident situation to make informed decisions and determine the nature of the strategic response.

Incident setting data. Timely sharing and exchange of incident setting data provide responders with a quick overview of the incident. Examples of incident setting data include the basic information on fire incidents such as the incident ID, description, fire category, both the date and time of the incident start, alarm sounded, incident under control, overhaul, and end. To this end, we developed a data type, Incident Specifics Type, to group these properties. As some incident specific properties are defined in the NIEM u:activityType, we established an inheritance relationship between the two data types. Following a NIEM-like Object-Oriented design, the proposed Incident Specifics Type is designed to inherit from u:activityType. This allows the new data type to inherit and reuse all the data properties in the NIEM-specified data type without inventing and redefining them. New properties (e.g., alarm date, alarm time, and reporter) that are missing from u:activityType are added into the Incident Specifics Type to support the fire response. Other important data types include Incident Location, Weather, Building Structure, Fire Detector, On-site Material, Automatic Extinguishing System, and Fire Hydrant data types.

Fire hazard data. During the response to a fire incident, the sharing of information on fire hazards allows the responders to comprehend the potential hazards that may emerge. To this end, we developed two data types: Fire Behavior Type and Hazard Factor Type.

Fire Behavior Type describes the real-time fire development and trend of progress. Its key properties include fire fuel, fire heat, and fire oxygen—the three ingredients required to start and sustain a fire, also referred to as the “fire triangle” (NIFC 2006). In addition, Fire Behavior Type includes properties such as fire spread, rate of spread, and flame length. It is important for the responders to comprehend these pieces of information before an effective fire intervention plan can be conceived and operational safety ensured.

Hazard Factor Type is designed to capture the set of fire hazards that are present. These hazards may directly or indirectly contribute to the fire escalation. Fire hazards may include factors such as building construction (e.g., wall collapse), an act or omission (e.g., fire door blocked), and onsite materials (e.g., explosive hazard materials). A close monitoring of the hazard factors should be implemented to detect and predict any emerging hazards.

Fire threat data. Information on threats reveals the immediate consequences caused by the fire. Fire incidents may cause consequences such as personal injury and casualty, chemical release and environmental contamination, property damage, and public safety impacts. A number of data types were developed to address these issues, including Casualty Type, Civilian Casualty Type, Fire Service Casualty Type, Property Damage Type, Environment Damage Type, and Public Safety Type.

## Incident Command

The data components for incident command capture the response management design and response operations. During the course of response, it is important to immediately publish information on the incident management system (e.g., on-site ICS and off-site EOC) in place, as it provides situational awareness of the collective response, clarifies the task assignment and resource allocation, and enforces the command and control structure.

Response management data. Guidelines provided by the national incident management system (NIMS) to identify major data components such as Response Facility Type, Incident Management System (IMS) Type, Response Organization Type, Response Personnel Type, and Response Resources Type were followed. The NIMS defines response personnel as one type of resource in general; in our data model, however, we differentiated response personnel from other resources (e.g., fire engines): The former are complex entities that may assume management roles and harness the other resources to carry out response tasks. Because NIEM had already created Response Resource Type, we did not reinvent this data type.

During a fire incident, the associations among response personnel, response organization, and IMS may vary. For example, the same individual may be mobilized to work for different IMS units during a fire response. We developed association data types (e.g., Responder IMS Association Type) that capture the dynamic involvements that are possible. A generic Regulation Document Type was also created to capture the variety of manuals, standard operating procedures, and rules followed in fire response.

Response operation data. Data types for the response operation were also developed. Creation of a standard for such information facilitates the monitoring, tracking, and analysis of response progress, ensuring that the mitigation develops as designed. An example data type here is Response Operation Plan Type, which describes the details of a response operation plan. Incident response operating plans are developed by the Planning unit of the ICS; they lay out the tactics and strategies to be used in the response processes. The Response Operation Plan Type includes plan title, ID, objective, approved date, approved time, evaluation, and corrective actions. Other response operation data types are Response Activity Type, Resource Schedule Type, Activity Involved Response Personnel Association Type, and Activity Involved Resource Association Type.

Table 4 provides a sample list of data model elements derived from the activity theory informed data modeling approach. It illustrates how the design implications shown in Figures 4 and 5 and Tables 1, 2, and 3 contribute to the data model development. Figure 6 presents a snapshot of the fire response data that illustrates the major data dimensions and components. The improved data model includes more than 50 data types, more than 200 data properties, and more than 70 codes. Snippets of the data model specification spreadsheet and data schema are available in Appendices A and B, respectively. The data model is important to construct the incident reports, dispatch forms, assessment reports, response plans, situation reports, request forms, comments, and response summaries, among other uses.

<table><tr><td colspan="3">Table 4. Activity Approach Informed Data Model Components</td></tr><tr><td colspan="2">Theoretical Construct</td><td>Example Data Elements</td></tr><tr><td rowspan="7">Onsite response (Figure 4)</td><td>Subject</td><td>Response personnel expertise and training</td></tr><tr><td>Object</td><td>Fire spread, rate of spread, and fuel</td></tr><tr><td>Community</td><td>Responses organization name, ID, and contact</td></tr><tr><td>Rule</td><td>Regulation document title, author, and version</td></tr><tr><td>Division of Labor</td><td>IMS unit category, established date, and sub unit</td></tr><tr><td>Environment</td><td>Weather temperature, barometer, and wind speed</td></tr><tr><td>Timeline</td><td>Alarm date and time, overhaul date and time</td></tr><tr><td rowspan="7">EOC Response (offsite) (Figure 4)</td><td>Subject</td><td>Response personnel organization affiliation—title and position</td></tr><tr><td>Object</td><td>Affected area and affected size of fire</td></tr><tr><td>Community</td><td>Response organization category (government/private/NPO)</td></tr><tr><td>Rule</td><td>Generalized; same as rule elements of onsite response</td></tr><tr><td>Division of Labor</td><td>Resource schedule—estimated departure and arrival date</td></tr><tr><td>Environment</td><td>Environment fate and toxicity and population density</td></tr><tr><td>Timeline</td><td>Response facility activated date and time</td></tr><tr><td colspan="2">Contradiction</td><td>Location district, sensitivity level, and parameter safety</td></tr><tr><td colspan="2">Stage Transition</td><td>Fire hydrant water main size, water flow, and pressure</td></tr><tr><td colspan="2">Reinforcing Feedback</td><td>Response activity result, plan evaluation, and corrective action</td></tr><tr><td colspan="2">Symbolic Icon</td><td>Parameter safety, structure safety, and injury severity</td></tr></table>

## Data Model Validation

To validate the fire response data model, we followed a threepart approach. This approach benefitted from an RFC procedure, a case application, and a prototype development and system test. The validation results attest to the quality of the new data model developed.

## Step 1: Initial Validation

Our data model was first validated by a panel of domain experts, who evaluated the model and provided feedback (Boudreau and Straub 2001). The validation process included 10 evaluators with an average of 15+ years of experience in fire response. The evaluators were experienced with fire incident response and its related information-sharing practices. The evaluators were individually contacted for their review feedback.

To facilitate validation, we developed a RFC-style document to introduce the evaluators to the research project. This RFC document outlined the research objective, development process, and proposed data model. We conducted on-site visits or made email contact with the evaluators to distribute the RFC and collect their feedback. The responders were asked to evaluate all aspects of the data model. The evaluation generated comments relating to coverage, depth, logic, organization, and naming. For instance, regarding data model additions, the evaluators suggested three data elements to be added. These were (1) disposition in Casualty data type; (2) EOC indicator in IMSUnit data type; and (3) surrounding risk assessment in Incident Location data type. The data model was subsequently modified to incorporate the feedback and sent back to the evaluators for comments again. The second round of evaluation was conducted in a similar manner with the evaluators. Consensus building was achieved through the RFC approach. This step ensured that the revisions from the step did not generate fresh reactions and we had consensus on the final model.

<table><tr><td colspan="9">Fire Incident Response</td></tr><tr><td colspan="7">Threat Assessment</td><td colspan="2">Incident Command</td></tr><tr><td colspan="2">Incident Setting</td><td colspan="2">Fire Hazard</td><td colspan="2">Threat</td><td colspan="2">Response Management</td><td>Response Operation</td></tr><tr><td>Incident SpecificsIncident ID, Incident Description, Category, Alert Level, Incident Date, Incident Time, Reporter, Alarm Date, Alarm Time, Alarm Method, Situation Found, Overhaul Date, Overhaul Time, Incident End Date, Incident End Time, Incident Result Text</td><td>WeatherSky, Temperature, Barometer, Wind Speed, Wind Direction, Dew Point, Precipitation, Humidity, Inversion</td><td>IgnitionCause of Ignition, Fire Liability, Fire Origin, Heat Source, Item First Ignited, Type of Material First Ignited, Human Factor Category, Non Human Factor Category, Equipment Involved, Exposure</td><td>Fire BehaviorFuel, Heat, Oxygen, Fire Spread, Rate of Spread, Flame length, Location, Measure Date, Measure Time</td><td>CasualtyCasualty Number, Injury Date, Injury time, Severity, Apparent Symptom, Body Injury, Cause of Injury, Activity Reference, Disposition, Injury Location, HumanFactor TOnjury, NonHumanfactor TOnjury</td><td>Property DamageFlame Damage, Smoke Damage, Water Damage, Number of Buildings Burned, No-Mobile Property Damage Value, Mobile Property Damage Value, Content Damage Value</td><td>IMS UnitName, ID, Unit Category, EOC Indicator, Established Date, Established Time, Termination Date, Termination Time, Sub Unit, Parent Unit</td><td>Response OrganizationName, ID, Category, Response District, Contact, Response Organization Sub Unit</td><td>Operation PlanTitle, ID, Objective, Creator, Recipient, Description, Approve Date, Approve Time, Evaluation, Corrective Action</td></tr><tr><td>StructureProperty Use,Category, Status, Safety, Height, Floor Map, Floor Size, Resident, Owner, Fire Detector, Automatic Extinguishing System, On Site Material, Fire Hydrant</td><td>EquipmentCategory, Brand, Model, Serial Number, Year, Power Source, Portability</td><td>Hazard FactorBuilding Construction, Act Omission, On site Material, Delay, Protective Equipment, Egress Exit, Natural Condition</td><td>Civilian CausualtyCivilian Reference, Affiliation Description</td><td>Public SafetyAffected Area, Affected Area Size, Evacuation Area, Evacuation Area Size</td><td>Response FacilityName, ID, Contact, Description, Activated Date, Activated Time, Deactivated Date, Deactivated Time, Structure Location</td><td>Response PersonnelName, Birth Date, Gender, Expertise, Training, Status, Security Clearance Level</td><td>Response PersonnelName, ID, Description, Certification, Kind, Location, Time of Usage</td><td>Response ActivityID, Category, Description, Date, Time, End Date, End Time, Result, Corrective Action</td></tr><tr><td>Fire DetectorCategory, Power Supply, Operation, Effectiveness, Failure Reason</td><td>On Site MaterialCategory, Description, Fire Load, Storage Use, Quantity</td><td>Fire Service CasualtyFirefighter Reference, Prior Physical Condition, Object Involved, Specification Location, Protective Equipment, Protective Equipment Failure</td><td>Environment DamageEnvironment Fate, Environment Toxicity</td><td>Response OrganizationIMS AssociationResponse Organization Reference, IMS Unit Reference, Description, Is Primary Organization Indicator</td><td>Personnel IMS AssociationPersonnel Reference, IMS Unit Reference, Position, Description</td><td>Personnel IMS AssociationPersonnel Reference, IIMS Unit Reference, Position, Description</td><td>ResourceName, ID, Description, Certification, Kind, Location, Time of Usage</td><td>Resource ScheduleAvailable Date, Committed Date, Estimated Departure Date, Anticipated Return Date</td></tr><tr><td>Automatic Extinguishing SystemCategory, Operation, Sprinkler Heads Number, Failure Reason</td><td>Fire HydrantWater Main Size, Water Flow, Pressure, Location</td><td>MetadataDistribution, Effective Date, Expiration Date, Language, Last Updated Date, Last Verified Date, Probability Numeric, Quality Comment, Reliability Numeric, Sensitivity, Release Date, Publisher name</td><td>Regulation DocumentTitle, Author, Keyword, Category, Summary, Content, Version, Classification Level</td><td>Regulation DocumentTitle, Author, Keyword, Category, Summary, Content, Version, Classification Level</td><td>Regulation DocumentTitle, Author, Keyword, Category, Summary, Content, Version, Classification Level</td><td>Regulation DocumentTitle, Author, Keyword, Category, Summary, Content, Version, Classification Level</td><td>Regulation DocumentTitle, Author, Keyword, Category, Summary, Content, Version, Classification Level</td><td>Regulation DocumentTitle, Author, Keyword, Category, Summary, Content, Version, ClassificationLevel</td></tr></table>

# North Bailey Fire Co.

# 966 Sweet Home Road, Amherst, N. Y. 14226

## FIRE REPORT

Incident #3201

AddressSam < Address 0

City Zip City Zip

4

Type of Action TakenExtinguishment RescuenvestigateRemove Hazard

Stand-by□Cancelled en Route□Other:

Equipment Involved In Ignition:ELeCTR:CAL C

Type Of Material Ignited: a

Building Story(s)6 Smoke Detectors YesNo

Construction Type:B.ck

Detector Operable YesNo

Hazardous Material: Battery or A/C:B0+

Amount of Material: Estimated Loss:Building:5,

polntotorigin: BDroon /uNder Rug

Extended To:Aρt/29 Cause olFire:WorN Electrice1 Cor0

Remarks: BOUlevar.O TOWER APARTMENtS

DRIVERS: VEHICLE FIRES:

Color

Engine 2Richter, T Year

Engine 3 wh, tc, Tii Make

Rescue5 BLAzczy<k N.ik Model

Ladder 6 Coarus / Geih Plate # State

Rescue7Hum mcr ALbc\~ t V.I.N.#

Mutual Ald Given To:

Officer In ChargeRich ter

## Figure 7. Fire Report Form

Transition elements informed by the extended activity theory approach

Property Use: Floor Map:

Water Main Size: Water Flow: Pressure:

Automatic Extinguishing System

Category: Operation: Sprinkler Head #:

System Failure Reason (if any):

Feedback elements informed by the extended activity theory approach

Operation Plan

Title: Id: Objective:

Description:

Approve Date: Approve Time: Recipient:

Response Activity

ID: Category: Description:

Start Date: Start Time: End Date: End Time:

Result: Corrective Action:

Injuries Severity:

![](/api/attachments/EMFX93WF/fulltext/images/8cac5e8b340db21aa2a9df8006a5633edd18f420a26b2f2898a10cb48735ef1b.jpg)

Figure 8. Examples of Activity Theory Informed Additions

## Step 2: Case Application

Next, we employed an empirical case to show the utility of the data model in improving the existing interagency response information sharing practice. As shown in Figure 7, we studied a document entitled Fire Report Form. This form was collected at a later stage of the data model development process and, therefore, was not used in the model development.

The North Bailey Fire Company in Amherst, New York, uses this form to record and report the fire incidents that take place in its district. This form serves as the sole document detailing the incident response that North Bailey Fire Company is in charge of and may be requested by supportive agencies (e.g., EMS, Environment Protection Agency) during a fire response.

We solicited comments from a panel of five domain experts who represented fire-related domains such as fire, police, and hazardous materials. One panelist was affiliated with North Bailey Fire Company. The panelists all had senior management roles in their respective fields, with an average of 15+ years of fire response experience; they were all aware of the NIEM standard. We contacted each panelist individually through on-site visits, during which we presented the Fire Report Form along with a set of new data elements that were informed by our extended Activity Theory approach. By interviewing the panel members (verbal communication), we collected their feedback as to whether our proposed theorydriven data elements related to the Fire Report Form and whether they could improve the existing data communication practice. The panelists shared their individual thoughts and discussed and reached consensus. The panel pointed out that the existing Fire Report Form lacked important response data, which might result in task-critical data elements not being shared and exchanged during an incident response. The panelists found the data model useful as it was guided by activity theory and provided a comprehensive set of fire response data, which could be used to expand the Fire Report Form. Examples of new data elements that were approved by the panel members are shown in Figure 8. Additional insights were also generated from the panel study; a standardized electronic Fire Report Form would provide excellent accommodation for these additional document fields. As part of an electronic response document, the data on “floor map,” for example, can be retrieved directly from internal databases and immediately become available to the responders. In western New York, such data are unfortunately not available to the local responders at the present time. All of the information is kept in paper archives at varying office locations, leaving the responders with no clue about how to develop the most appropriate fire intervention strategies when they are most needed. Representatives from the fire department also expressed interest in incorporating the proposed changes into their fire report design.

## Step 3: Prototype System Test

Finally, we built a prototype system<sup>2</sup> to examine the proposed data model’s real support for core response activities in fire incident management. This prototype utilized the fire response data model to standardize fire response communication (Valecha et al. 2010). It enabled first responders to enter pertinent information that dealt with situation assessment, resource application, and collaboration, etc. The system development and testing team consisted of eight graduate students; these students had all worked in software industries, with titles such as system engineer or project manager, before joining the graduate program. The development followed the standard software development life cycle (SDLC) methodology and took five months to complete.

As a prototype, this system utilized only a portion of the standards in the fire response data model. These elements covered key response data such as incident specifics, fire specifics, and casualty. The prototype system contained 16 modules, including resource, weather, map, and communication. In this prototype system, a total of 33 forms were generated to store information on user privilege for form users, fire hydrant locations, and responder injuries. Figure 9 provides a snapshot of the prototype system. The systems diagram in Figure 9 explains the front-end functionality of the built system. The response data was stored in the Internet cloud and could be accessed by any handheld device or a computer with Internet access. Only authenticated personal with proper user name and password could access the system. All departments (i.e., fire, police, EMS, and dispatch) had their own forms with relevant information required for that department. The system was accessible via connected wireless and wired networks and also via wireless smart phones (e.g., Android). The initiation of the system starts with the dispatcher’s trigger of reporting an incident. An alert is sent to the fire chief, police, and EMS after the incident is reported by the dispatcher. The on-duty fire chief accepts the call and responds to the emergency. Next, the incident commander enters the incident information and the fire chief enters the response data on the centralized system. This information is, in turn, used by all other personnel, such as police and EMS. The system is also used to retrieve maps and blueprints, and allows responders to use chat and video feed as a way of effective communication. Finally, an incident report is generated, which is both stored for future reference and reported to the state agency.

Through the prototype, the data model was evaluated by user acceptance testing to assess its quality and level of support in fire response communication. The user acceptance test consisted of both scripted based and tabletop exercises which are typical methods for emergency response exercises (FEMA 2003). This test ensures that the prototype developed based on the model was indeed useful in the mitigation of a fire incident. The user acceptance testing thus serves as a proof of concept. Highlights of the user acceptance test are presented in Table 5.

## Discussion and Conclusion

Our paper contributes to research in that it presents a novel approach in developing data models. The extended activity theory approach offers a number of unique benefits. Published literature identifies a number of methods for data model development (Zowghi and Coulin 2005): goal-oriented (Mylopoulos et al. 1999; Zhang et al. 2007), function-based (Chandrasekaran and Kaindl 1996), and viewpoint-oriented (Finkelstein et al. 1991; Kotonya 1999). A comparison suggests that the approach informed by extended activity theory provides a more comprehensive framework for data modeling.

Take the viewpoint-oriented approach, for example. A viewpoint is a collection of information about a system or related problem that is gathered from a particular perspective (Finkelstein et al. 1991). While viewpoint approaches model the domain from multiple perspectives to form a complete picture of the target system, they are typically criticized for not being able to take into account nonfunctional requirements that may be embedded in the community and social environment (Nuseibeh et al. 1996; Sommerville et al. 1998). They do not consider contradictions and conflicts that are part of collaborative systems. Prior research suggests that such conventional approaches are typically limited in the scope of analysis that they can offer (Simsion and Witt 2001; West 2011).

![](/api/attachments/EMFX93WF/fulltext/images/bc141306ec230506446bbdc6608c40eca53cef60e84f47b0753d79ba2691e014.jpg)  
Figure 9. Snapshot of Prototype System Screen

Based on existing literature (Chen et al. 2008a), Table 6 offers a comparative summary of potential approaches to data model development.

This data model contains data types that are common to other incident types. Data types related to incident setting (incident specifics, incident location, weather), threat (casualty, civilian casualty, fire service casualty, property damage, public safety, environment damage), response management (IMS unit, response facility, response organization, response personnel, resource, response organization IMS association, personnel IMS association, personnel response organization association, regulation document), response operation (operation plan, response activity, resource schedule, activity-involved responder association, activity-involved response organization association), and all metadata are applicable to other incident scenarios such as floods and earthquakes. In contrast, data types such as incident setting (structure, fire detector, on-site material, automatic extinguishing system, fire hydrant, ignition, equipment) and fire hazards (fire behavior and hazard factor) are specific to fire response scenarios. To develop a data model for other incidents such as earthquakes, common data types may be reused while earthquake-specific data types (e.g., magnitude, number of seismic stations that reported Pand S-wave arrival times for the earthquake, and the rootmean-square travel time residual) must replace fire-specific data types.

Our study has certain limitations that should be noted. First, the data model may not comprehensively address all aspects of the communication requirements during a fire incident response. The current scope of the data model covers the core response operations in a fire incident response. Future research might expand the data model to include other data elements that are supportive of the fire response. For example, we might capture the details of typical response resources (e.g., fire engine, hose, and ladder) and standardize them in the data model. Second, the data model development relies primarily on the expertise of the emergency response community of western New York. While state and national response practices of fire response are considered in the data model, the model might be enriched and validated by practitioners from other regions of the country.

<table><tr><td colspan="2">Table 5. User Acceptance Test Results</td></tr><tr><td>Participators</td><td>Six participants from dispatch, fire, police, and EMS</td></tr><tr><td>Qualifications</td><td>An average of 15+ years of incident management experience</td></tr><tr><td colspan="2">Phase 1. Test Script-Based Evaluation</td></tr><tr><td>Evaluation procedures</td><td>1. A mock emergency scenario was created.2. Evaluators assumed response roles such as fire, police, and EMS.3. Evaluators received test scripts that prescribed role-specific response actions.4. Evaluators completed the response by executing the test scripts.</td></tr><tr><td>Conclusion</td><td>Through the prototype system, six evaluators were able to assume individual response roles and complete fire response tasks in a collaborative manner. In this mock fire test, evaluators successfully completed around 80 response management steps with everybody sharing task information with the others. The evaluators were satisfied with the communication support from the prototype system. Quote: “Using the prototype system is a good experience for all of us.”</td></tr><tr><td colspan="2">Phase 2. Table-Top Exercise-Based Evaluation</td></tr><tr><td>Evaluation procedures</td><td>1. A mock emergency scenario was created:We asked a fire chief not participating in the validation of the system to develop a scenario for a multi-story apartment complex on fire. The scenario included additional scene information provided from time to time—for example: the group participating in the software validation process learned that there were three victims trapped in apartment 353 and two in apartment 401. The responding team was informed 10 minutes into the mitigation exercise that some handicapped elderly gentleman was trapped on the fifth floor and would need wheel chair assistance, etc. The scenes and information were adopted from scenarios that are typical of fire related incidents in apartment complexes.2. Evaluators assumed response roles such as first alarm, second alarm, police on scene, Fire Company, and EMS.3. No script was offered; role players acted following their professional training.4. Evaluators completed the incident response through collaboration.</td></tr><tr><td>Support covered</td><td>1. The prototype system was associated with a high level of satisfaction in communication support as the data model allowed timely sharing of critical fire response information.2. New values were suggested for the data property of incident victim health condition. This suggestion was not endorsed by the majority of the responders and was ultimately dropped.3. Evaluators expressed strong interest in adopting the prototype system for implementation at local fire stations.</td></tr></table>

Table 6. Comparison of Approaches of Data Model Development

<table><tr><td>Dimension</td><td>Focus</td><td>Goal Oriented</td><td>Function Based</td><td>Viewpoint Oriented</td><td>Extended Activity Theory Approach</td></tr><tr><td rowspan="2">People</td><td>Individual</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>Community</td><td></td><td></td><td></td><td>×</td></tr><tr><td rowspan="4">Process</td><td>Task structure</td><td></td><td>×</td><td></td><td></td></tr><tr><td>Division of labor</td><td></td><td>×</td><td>×</td><td>×</td></tr><tr><td>Temporal sequence</td><td></td><td></td><td></td><td>×</td></tr><tr><td>Object hierarchy</td><td>×</td><td></td><td>×</td><td></td></tr><tr><td rowspan="4">Technology</td><td>Instrument</td><td></td><td></td><td>×</td><td>×</td></tr><tr><td>Symbolic language</td><td></td><td></td><td></td><td>×</td></tr><tr><td>Social issues</td><td></td><td></td><td>×</td><td>×</td></tr><tr><td>Environment issues</td><td></td><td></td><td></td><td>×</td></tr><tr><td rowspan="2">Interaction</td><td>Contradictions</td><td>×</td><td></td><td>×</td><td>×</td></tr><tr><td>Transition and feedback</td><td></td><td></td><td></td><td>×</td></tr></table>

In addition, other researchers might develop response performance metrics on the basis of threat assessment and incident command information. It would be beneficial to develop an emergency index (e.g., Bayesian algorithms) on the basis of the individual symbolic codes of emergency facts. For example, a red code might be generated to indicate an escalating incident when a combination of response symptoms is present; multiple agencies should be brought into the incident response in this scenario. Otherwise, the code goes to green; the supportive agencies can be released to address other fires and not tie up resources.

In this study, activity theory is primarily used to identify data elements. The utilization of activity theory ensures the conformance of data values to business requirements and acceptance criteria. Yet future study may further support the research by considering quality aspects of data modeling, requirements analysis, and emergency processes.

In conclusion, the lack of consistent communication data standards for emergency management represents an impediment to efficient information sharing and exchange in the context of emergency response systems that cater to specific emergencies such as fires, floods, and severe snowstorms (Chou et al. 2011). Using fire incidents as an example, we have developed a systematic data model to capture and standardize response-critical information for fire incident management. The paper provides a detailed data model along with a data dictionary and an object-oriented structure. This project is guided by an extension to the activity theory approach to ensure the research rigor. This project represents one of the first attempts in the response community to propose solutions that would contribute to the creation of a widely accepted set of emergency data standards. The fire incident data model improves collaboration and information sharing among response organizations and agencies.

## Acknowledgments

Our research was supported by NSF under grants 0802062 and 0809186; the usual disclaimer applies. The research of the third (corresponding) author has been funded in part by NSF under grant 0916612 and by Sogang Business School’s World Class University Project (R31-20002) funded by Korea Research Foundation and by the Sogang University Research Foundation. The usual disclaimer applies. We would like to thank Dean Messing (Deputy Commissioner of Disaster Preparedness, Erie County Emergency Services, New York), Dan Neaverth (Deputy Commissioner of Emergency Medical Service, Erie County Emergency Services, New York; Chief of Orchard Park Fire District, New York), James Zymanek (Town of Amherst Disaster Coordinator, New York; past Chief of Williamsville Fire Department, New York), Dave Humbert (Chief of North Bailey Fire Department, Amherst, New York), James Guy (past Fire Chief and now Chief of Environmental Affairs, University at Buffalo), Steve McGonagle (Captain/Chief of Amherst Police Department), Tom Maxim (CEO of Twin City Ambulance), Steve Piotrowski (Officer, Amherst Police Department), Craig Johnson (Officer, Amherst Police Department), John Buttino (Eggertsville Fire Company), Brian Brauner (Twin City Ambulance), Thomas Fitzpatrick (Captain of Buffalo Fire Department, New York), Dominic Creamer (Emergency Services and Safety Coordinator, Amherst Emergency Services, New York), Brian Benstead (New York State Office of Fire Prevention and Control), Tiger Schmittendorf (New York State Office of Fire Prevention and Control), Dennis Carson (Police Emergency Services Coordinator, Town of Tonawanda, New York), Greg Blossat (Captain, Buffalo Police Department, New York), Mike Wood (Chief of Manassas Fire Department, Manassas, Virginia), Michael Parker (Chief of Ellicott Creek Volunteer Fire Company, New York), Michael Lotocki (Chief of Scranton Fire Company, New York), and Brian Horwood (Chief of Hamburg Fire Department, New York) for their great help in this research project.

## Notes

The most recent version NIEM 2.1 is backward compatible, with all previous intergovernmental information exchange models, “including GJXDM, NIEM 1.0, and NIEM 2.0 and continues to support existing exchanges,” as specified in Richards (2009). It may be noted that the suggestions made in this paper also apply to the current version as well. Icons in Figure 1 remain the property of Icons-Land (http://www.icons-land.com).

## References

Bardram, J. 1998. “Designing for the Dynamics of Cooperative Work Activities,” in Proceedings of the 1998 ACM Conference on Computer Supported Cooperative Work, S. Poltrock and J. Grudin (eds.), Seattle, WA, November 14-18, pp. 89-98.

Bertelsen, O. W., and Bodker, S. 2003. “Activity Theory,” in HCI Models Theories, and Frameworks: Toward A Multidisciplinary Science, J. M. Caroll (ed.), San Francisco: Morgan Kaufmann, pp. 291-324.

Boer, N. I., van Baalen, P. J., and Kumar, K. 2002. “An Activity Theory Approach for Studying the Situatedness of Knowledge

Sharing,” in Proceedings of the 35<sup>th</sup> Hawaii International Conference on System Sciences, Los Alamitos, CA: IEEE Computer Society Press.

Boudreau, G., and Straub, D 2001. “Validation in IS Research: A State-of-the-Art Assessment,” MIS Quarterly (25:1), pp. 1-16.

Chandrasekaran, B., and Kaindl, H. 1996. “Representing Functional Requirements and User-System Interactions,” in Proceedings of the AAAI-96 Workshop on Modeling and Reasoning about Function, Portland, OR, August.

Chaudhury, A., Mallick, D. N., and Rao, H. R. 2001. “Web Channels in E-Commerce,” Communications of the ACM (44:1), pp. 99-104.

Chen, R., Sharman, R., Chakravarti, N., Rao, H. R., and Upadhyaya, S. 2008a. “Emergency Response Information System Interoperability: Development of Chemical Incident Response Data Model,” Journal of the Association for Information Systems (9:3), pp. 203-232.

Chen, R., Sharman, R., Rao, H. R., and Upadhyaya, S. 2007. “Response Information Interoperability: A Development of Data Standards in the Fire Incident Context,” paper presented at the Sixth Pre-ICIS International Workshop on E-Business, Montreal, Canada, December 9.

Chen, R., Sharman, R., Rao, H. R., and Upadhyaya, S. 2008b. “Coordination in Emergency Response Management,” Communications of the ACM (51:5), pp. 66-73.

Chen, R., Sharman, R., Rao, H .R., and Upadhyaya, S. 2008c. “Data Model Development For Fire Related Extreme Events: An Activity Theory and Semiotics Approach,” in Proceedings of the 29<sup>th</sup> International Conference on Information Systems, Paris, France, December 14-17.

Chou, C. H., Zahedi, F. M., and Zhao, H. 2011. “Ontology for Developing Web Sites for Natural Disaster Management: Methodology and Implementation,” IEEE Transactions on Systems, Man, and Cybernetics—Part A (41:1), pp. 50-62.

Davydov, V. V. 1999. “The Content and Unsolved Problems of Activity Theory,” in Perspectives on Activity Theory, Y. Engeström, R. Miettinen and R.-L. Punamäki (eds.), New York: Cambridge University Press, pp. 39-52.

DHS. 2004. “National Incident Management System,” Department of Homeland Security (available at http://www.fema.gov/ emergency/nims).

DHS. 2008. “Fact Sheet: Achieving First Responder Communications Interoperability,” in Multi Agency Unified Command and Control Infrastructure, J. Mederos and Alan Lewis, U.S. Department of Homeland Security Federal Protective Services and Stonecutter Group, LLC, pp. 67-71 (http://www. stonecuttergroup.com/incubation/projects/infrastructure/Multi %20Agency%20Unified%20Command%20and%20Control%2 0Proposal.pdf).

DHS/DOJ. 2006. “National Information Exchange Model,” Washington, DC (www.niem.gov).

DOJ. 2005. “Building Exchange Content Using the Global Justice XML Data Model,” Department of Justice, Washington, DC (www.it.ojp.gov/documents/GJXDMUserGuide.pdf).

E9-1-1. 2006. “NENA Data Standards for Local Exchange Carriers, ALI Service Providers & 9-1-1 Jurisdictions,” National

Emergency Number Association (http://www.nena.org/resource/ collection/6366E817-C855-4776-AF3A-F9F715D1AF12/NEN A\_02-011-v6\_9-1-1\_Data\_Management.pdf

EIC. 2005. “Common Alerting Protocol,” Emergency Interoperability Consortium (https://www.oasis-open.org/committees/ download.php/15135/emergency-CAPv1.1-Corrected\_DOM.pdf)

Engeström, Y. 1987. Learning by Expanding: An Activity-Theoretical Approach to Developmental Research, Helsinki: Orienta-Konsultit Oy..

Engeström, Y. 1999. “Activity Theory and Individual and Social Transformation,” in Perspectives on Activity Theory, Y. Engeström, R. Miettinen, and R-L. Punamäki (eds.), Cambridge, UK: Cambridge University Press, pp. 19-38.

Engeström, Y., Brown, K., Christopher, L. C., and Gregory, J. 1997. Coordination, Cooperation, and Communication in the Courts: Expansive Transitions in Legal Work, Cambridge, UK: Cambridge University Press.

FEMA. 2003. “IS-139 Exercise Design,” FEMA Emergency Management Institute, Emmitsburg, MD (http://training.fema.gov/ EMIWeb/IS/is139.asp).

Finkelstein, A., Goedicke, M., Kramer, J., and Niskier, C. 1991. “Viewpoint Oriented Software Development: Methods and Viewpoints in Requirements Engineering,” in Algebraic Methods II: Theory, Tools and Applications, New York: Springer-Verlag, pp. 29-54.

Fischer, H. W. 1998. “The Role of the New Information Technologies in Emergency Mitigation, Planning, Response and Recovery,” Disaster Prevention and Management (7:1), pp 28-37.

Foorthuis, R., Brinkkemper, S., and Bos, R. 2008. An Artifact Model for Projects Conforming to Enterprise Architecture, New York: Springer.

Frale, D. 2005. “Emergency Interoperability Consortium Announces Agreement with Department of Homeland Security to Promote Data Sharing During Emergencies,” E Team, Inc. (http://www.globenewswire.com/newsroom/news.html?d= 70859).

Fuentes, R., Gomez-Sanz, J. J., and Pavon, J. 2003. “Social Analysis of Multi-Agent Systems with Activity Theory,” in Current Topics in Artificial Intelligence: 10<sup>th</sup> Conference of the Spanish Association for Artificial Intelligence, San Sebastian, Spain, November 12-14.

Gil-Garcia, J. R., Chun, S. A., and Janssen, M. 2009. “Government Information Sharing and Integration: Combining the Social and the Technical,” Information Policy (14:1-2), pp. 1-10.

Hayes-Roth, R., Blais, C., Pullen, J. M., and Brutzman, D. 2008. “How to Implement National Information Sharing Strategy: Detailed Elements of the Evolutionary Management Approach Required,” paper presented at the FCEA–GMU C41 Center Symposium, Critical Issues in C41. Fairfax, VA, May 21.

Hevner, A., March, S. T., Park, J., and Ram, S. 2004. “Design Science Research in Information Systems,” MIS Quarterly (28:1), pp. 75-105.

HL7. 2006. “HL7 Messaging Protocol,” Health Level Seven International (http://www.hl7.org/).

Hull, R., and King, R. 1987. “Semantic Database Modeling: Survey, Applications, and Research Issues,” ACM Computer Survey (19:3), pp. 201-260.

Iivari, J., and Linger, H. 1999. “Knowledge Work as Collaborative Work: A Situated Activity Theory View,” in Proceedings of the 32<sup>nd</sup> Hawaii International Conference on System Sciences, Los Alamitos, CA: IEEE Compute r Society Press.

Jaegar, P. T., Shneiderman, B., Fleischmann, K. R., Preece, J., Qu, Y., and Wu, F. 2007. “Community Response Grids: E-Government, Social Networks, and Effective Emergency,” Telecommunications Policy (31:1), pp. 10-11.

Karter, M. J. 2008. “Fire Loss in the United States 2007,” National Fire Protection Association, Quincy, MA (http://www. maine.gov/dps/fmo/research/documents/FireLossintheUS07 long.pdf)

Kofod-Petersen, A., and Cassens, J. 2006. “Using Activity to Model Context Awareness,” paper presented at the Modeling and Retrieval of Context: Second International Workshop, Edinburgh, Scotland.

Kotonya, G. 1999. “Practical Experience with Viewpoint-Oriented Requirements Specification,” Requirements Engineering (4:3), pp. 115-133.

Kuutti, K. 1991. “Activity Theory and its Applications to Information Systems Research and Development,” in Information Systems Research: Contemporary Approaches and Emergent Traditions, H-E. Nissen, H. K. Klein, and R. H. Hirschheim (eds.), Amsterdam: Elsevier, pp. 529-549.

Lektorsky, V. A. 1999. “Activity Theory in a New Era,” in Perspectives on Activity Theory, Y. Engeström, R. Miettinen and R.-L. Punamäki (eds.), Cambridge, United Kingdom: Cambridge University Press, pp. 65-69.

Leont’ev, A. N. 1978. Activity, Consciousness and Personality, Englewood Cliffs, NJ: Prentice-Hall.

Lorincz, K., Malan, D., Fulford-Jones, T. R. F., Nawoj, A., Clavel, A., Shnyder, V., Mainland, G., Welsh, M., and Moulton, S. 2004. “Sensor Networks for Emergency Response: Challenges and Opportunities,” Pervasive (3:4), pp 16-23.

March, S. T., Hevner, A., and Ram, S. 2000. “Research Commentary: An Agenda for Information Technology Research in Heterogeneous and Distributed Environments,” Information Systems Research (11:4), pp. 327-341.

Mendling, J., and Nuttgens, M. 2006. “XML Interchange Formats for Business Process Management,” Information Systems and E-Business Management (4:3), pp. 217-220.

Mylopoulos, J., Chung, L., and Yu, E. 1999. “From Object-Oriented to Goal-Oriented Requirements Analysis,” Communications of the ACM (42:1), pp. 31-37.

NEMSIS. 2007. “EMS Data Dictionary,” National Emergency Medical Services Information System Technical Assistance C e n t e r ( h t t p : / / w w w . n e m s i s . o r g / v 2 / d o w n l o a d s / datasetDictionaries.html).

NIEM. 2007. “National Information Exchange Model Concept of Operations,” NIEM Program Management Office, Washington, DC (http://reference.niem.gov/niem/guidance/concept-ofoperations/0.5/concept-of-operations.pdf).

NIFC. 2006. “This Thing Called Fire,” National Interagency Fire Center, Boise, ID (http://www.nifc.gov/pres\_visit/ whatisfire.html).

Nuseibeh, B., Finkelstein, A., and Kramer, J. 1996. “Method Engineering for Multi-Perspective Software Development,” Information and Software Technology (38:4), pp. 267-274.

OASIS. 2006. “Emergency Data Exchange Language,” OASIS Emergency Management Technical Committee (https://www. oasis-open.org/committees/download.php/17227/EDXL-DE\_ Spec\_v1.0.html).

Peckham, J., and Maryanski, F. 1988. “Semantic Data Models,” ACM Computer Survey (20:3), pp. 153-189.

Peffers, K., Uunanen, T., Rothenberger, M. A., and Chatterjee, S. 2008. “A Design Science Research Methodology for Information Systems Research,” Journal of Management Information Systems (24:3), pp. 45-77.

PHIN. 2005. “PHIN Vocabulary Standards and Specifications,” Centers for Disease Control and Prevention, Atlanta, GA (http://www.cdc.gov/phin/activities/vocabulary.html).

Purao, S., Baldwin, C. Y., Hevner, A., Storey, V. C., Pries-Heje, J., Smith, B., and Zhu, Y. 2008. “The Sciences of Design: Observations on an Emerging Field,” Communications of the AIS (23:1), pp. 523-546.

Rao, H. R., Chaudhury, A., and Chakka, M. 1995. “Modeling Team Processes: Issues and a Specific Example,” Information Systems Research (16:3), pp. 255-285.

Rice, D., Garfinkel, R., and Gopal, R. 2004. “Security, Privacy, and a Trusted Information Intermediary,” in Proceedings of the 10<sup>th</sup> Americas Conference on Information Systems, New York, pp. 1403-1411.

Richards, R. C. 2009. “NIEM 2.1 to Be Released in Late Summer 2009,” Legal Informatics Blog, State College, PA (http:// legalinformatics.wordpress.com/?s=NIEM+2.1)

Sanchez-Ruiz, A. J., Umapathy, K., Beckham, J., and Welsh, P. 2008. “The Data Interoperability Problem as an Exemplary Case Study in the Development of Software Collaboration Environments,” paper presented at the International Workshop on Collaboration and Cognition in Next Generation Networks, Orlando, FL.

Shankar, D., Agrawal, M., and Rao, H. R. 2011. “Emergency Response to Mumbai Terror Attacks: An Activity Theory Analysis,” in Cyber Security, Cyber Crime and Cyber Forensics: Applications and Perspectives, R. Santanam, M. Sethumadhavan, and M. Virendra, (eds), Hershey, PA: IGI Global, pp. 46-58.

Simsion, G. C., and Witt, G. C. 2001. Data Modeling Essentials, Scottsdale, AZ: The Coriolis Group.

Sommerville, I., Sawyer, P., and Viller, S. 1998. “Viewpoints for Requirements Elicitation: A Practical Approach,” paper presented at the IEEE International Conference on Requirement Engineering, Colorado Springs, CO.

Townsend, F. F. 2006. “The Federal Response to Hurricane Katrina Lessons Learned,” The White House, Washington, DC.

Turoff, M., Chumer, M., Van de Walle, B., and Yao, X. 2004. “The Design of A Dynamic Emergency Response Management Information System (DERMIS),” Journal of Information Technology Theory and Application (5:4), pp. 1-35.

Valecha, R., Sharman, R., Monteiro, J., Rao, H. R., Upadhyaya, S., Keerthana, B., Patel, M., Singh, A., Sharma, K., and Chen, R. 2010. “A Prototype of a Fire-Related Extreme Eventz System (FREEZ),” paper presented at the Workshop on Information Technologies and Systems, St. Louis, MO.

Vygotsky, L. S. 1978. Mind and Society, Cambridge, MA: Harvard University Press.

W3C. 2008. Extensible Markup Language (XML) 1.0 (5<sup>th</sup> ed.), W3C (http://www.w3.org/TR/REC-xml).

Wallace, W. A., and De Balogh, F. 1985. “Decision Support Systems for Disaster Management,” Public Administration Review (45:Special Issue), pp. 134-146.

West, M. 2011. Developing High Quality Data Models, San Francisco: Morgan Kaufmann.

Zhang, H., Kishore, R., Sharman, R., and Ramesh, R. 2007. “Agile Integration Modeling Language (AIML): A Conceptual Modeling Grammar for Agile Integrative Business Information Systems,” Decision Support Systems (44:1), pp. 266-284.

Zhang, P., and Bai, G. 2005. “An Activity Systems Theory Approach to Agent Technology,” International Journal of Knowledge and Systems Sciences (2:1), pp. 60-65.

Zowghi, D., and Coulin, C. 2005. “Requirement Elicitation: A Survey of Techniques, Approaches, and Tools,” in Engineering and Managing Software Requirements, A. Aurum and C. Wohlin (eds.), Berlin: Springer, pp. 19-46.

## About the Authors

Rui Chen is an assistant professor of Information Systems and Operations Management in the Miller College of Business at Ball State University. He holds a Bachelor’s and a Master’s degree in computer science and a Ph.D. in management science and systems from State University of New York at Buffalo. His research focuses on information assurance, emergency management, emerging media, IT capability, and IT outsourcing. He has published a number of research articles in renowned journals, conferences, and books. He has also served many journals, conferences, and books in various capacities such as editor, editorial advisory board member, editorial review board member, program committee member, session chair, and discussant. He received the Advanced Certificate in Information Assurance from State University of New York at Buffalo and the National Security Agency, and is also a Microsoft Certified Database Administrator and Microsoft Certified Systems Engineer.

Raj Sharman is an associate professor in the Management Science and Systems Department of the State University of New York at Buffalo. He received his B.Tech and M.Tech degrees from IIT Bombay, India, and his M.S. degree in Industrial Engineering and Ph.D. in Computer Science from Louisiana State University. His research streams include information assurance, disaster preparedness and response management, patient safety and health care systems, business value of information technology investments, and imaging systems. He has published in national and international journals and is the recipient of several grants from university and external agencies, including the National Science Foundation. He serves as an associate editor for Communications of the Association of Information Systems and Journal of Information Systems Security, and as a coordinating guest editor for Information Systems Frontiers.

H. R. Rao is a SUNY Distinguished Service Professor at SUNY Buffalo and WCU Visiting Professor at Sogang University, South Korea. He has published more than 150 archival papers and has received several best paper or best paper runner up awards at several conferences such as the Americas Conference on Information Systems and the International Conference on Information Systems. He has edited several books, two of which are on information assurance, security, and privacy services. He has been a Fulbright scholar and his research is funded by the National Science Foundation, Department of Defense, and others. He is co-editor-inchief of Information Systems Frontiers and is (or has been) an associate editor or guest senior editor at journals including MIS Quarterly, Information Systems Research, Decision Support Systems, IEEE Transactions on SMC, ACM Transactions on MIS, and Communications of the ACM. He has a Ph.D. from Purdue University, an MBA from Delhi University, and a B.Tech from IIT Kanpur.

Shambhu J. Upadhyaya is a professor of Computer Science and Engineering at the State University of New York at Buffalo where he directs the Center of Excellence in Information Systems Assurance Research and Education (CEISARE), designated by the National Security Agency. Prior to July 1998, he was a faculty member at the Electrical and Computer Engineering Department. His research interests are information assurance, computer security, fault diagnosis, fault tolerant computing, and VLSI testing. He has authored or coauthored more than 150 articles in refereed journals and conferences in these areas. His current projects involve insider threat modeling, intrusion detection, security in wireless networks, and protection against Internet attacks. His research has been supported by the National Science Foundation, Rome Laboratory, the U.S. Air Force Office of Scientific Research, National Security Agency, IBM, and Cisco.

# DATA MODEL DEVELOPMENT FOR FIRE RELATED EXTREMEEVENTS: AN ACTIVITY THEORY APPROACH

## Rui Chen

Department of Information Systems and Operations Management, Miller College of Business, Ball State university Muncie, IN 47306 U.S.A. {rchen3@bsu.edu}

Raj Sharman Management Science and Systems, School of Management, State University of New York at Buffalo, Jacobs Management Center, Buffalo, NY 14260 U.S.A. {rsharman@buffalo.edu}

## H. Raghav Rao

Management Science and Systems, School of Management, State University of New York at Buffalo, Jacobs Management Center, Buffalo, NY 14260 U.S.A. and Department of GSM, Sogang University, Seoul, SOUTH KOREA {mgmtrao@buffalo.edu}

Shambhu J. Upadhyaya Computer Science and Engineering, School of Engineering and Applied Sciences, State University of New York at Buffalo, 201 Bell Hall, Buffalo, NY 14260 U.S.A. {shambhu@buffalo.edu}

## Appendix A

## Data Model Specification Spreadsheet

<table><tr><td>Type/Sub-Property</td><td>Type</td><td>Definition</td></tr><tr><td>IncidentSpecificsType</td><td>extends u:ActivityType</td><td>A structure that describes the specific characteristics of the incident</td></tr><tr><td>IncidentCategory</td><td>nfirs:FireIncidentCodeSimpleType</td><td>A code identifying the fire incident type such as "structure fire"</td></tr><tr><td>AlarmDate</td><td>u:DateType</td><td>A code identifying the date when fire is first reported</td></tr><tr><td>AlarmTime</td><td>niem-xsd:time</td><td>A code identifying the time when fire is first reported</td></tr><tr><td>AlarmMethod</td><td>AlarmMethodCodeSimpleType</td><td>A code identifying how the alarm is received from the public. E.g., telephone, municipal alarm system, private alarm system.</td></tr><tr><td colspan="3">Table A.1 A Snippet of Data Types (Continued)</td></tr><tr><td>Type/Sub-Property</td><td>Type</td><td>Definition</td></tr><tr><td>SituationFound</td><td>SituationFoundCodeSimpleType</td><td>A code identifying the incident situation found upon arrival</td></tr><tr><td>AlertLevel</td><td>u:ImageType</td><td>A code identifying the safety alert level raised</td></tr><tr><td>Reporter</td><td>u:PersonType</td><td>A reference to the incident reporter</td></tr><tr><td>UnderControlDate</td><td>u:DateType</td><td>A code identifying the date when fire is under control</td></tr><tr><td>UnderControlTime</td><td>niem-xsd:time</td><td>A code identifying the time when fire is under control</td></tr><tr><td>OverhaulDate</td><td>u:DateType</td><td>A code identifying the date when fire overhaul is conducted</td></tr><tr><td>OverhaulTime</td><td>niem-xsd:time</td><td>A code identifying the time when fire overhaul is conducted</td></tr><tr><td>IncidentLocationType</td><td>extends em:LocationType</td><td>A structure that describes details about the incident location</td></tr><tr><td>ParameterSafety</td><td>u:ImageType</td><td>A code identifying the level of parameter security</td></tr><tr><td>District</td><td>u:TextType</td><td>A description of the response district</td></tr><tr><td>PopulationDensity</td><td>PopulationDensityMeasureType</td><td>A description of the neighboring area population density</td></tr><tr><td>SurroundingRiskAssessment</td><td>u:TextType</td><td>A description of the risks and vulnerabilities that are present at the local area</td></tr><tr><td>Terrain</td><td>u:TextType</td><td>A description of the terrain of the incident spot</td></tr><tr><td>PopulationDensityMeasureType</td><td>extends u:MeasureType</td><td>A structure that describes details about the population density</td></tr><tr><td>@populationDensityUnitCode</td><td>PopulationDensityUnitCodeSimpleType</td><td>A code identifying the units associated with the population density reading</td></tr><tr><td>WeatherType</td><td>extends u:SuperType</td><td>A structure that describes details about the weather condition</td></tr><tr><td>Sky</td><td>u:TextType</td><td>A description of sky condition</td></tr><tr><td>Temperature</td><td>TemperatureMeasureType</td><td>A description of temperature</td></tr><tr><td>Barometer</td><td>PressureMeasureType</td><td>A description of barometer</td></tr><tr><td>WindSpeed</td><td>WindSpeedMeasureType</td><td>A description of wind speed</td></tr><tr><td>WindDirection</td><td>WindDirectionCodeSimpleType</td><td>A description of wind direction</td></tr><tr><td>DewPoint</td><td>TemperatureMeasureType</td><td>A description of dew point of the day</td></tr><tr><td>Precipitation</td><td>PrecipitationMeasureType</td><td>A description of precipitation</td></tr><tr><td>Humidity</td><td>u:PercentageType</td><td>A description of humidity</td></tr><tr><td>InterventionIndicator</td><td>niem-xsd:boolean</td><td>Indicator of intervention occurrence</td></tr><tr><td>TemperatureMeasureType</td><td>extends u:MeasureType</td><td>A structure that describes details about the temperature measurement</td></tr><tr><td>@temperatureUnitCode</td><td>TemperatureUnitCodeSimpleType</td><td>A code identifying the units associated with the temperature reading</td></tr><tr><td>TemperatureDescription</td><td>u:TextType</td><td>A description or narrative of the temperature</td></tr></table>

<table><tr><td colspan="2">Table A.2 A Snippet of Code Lists</td></tr><tr><td>CodeSimpleType</td><td>Code List</td></tr><tr><td>WindDirectionCodeSimpleType</td><td>base xsd:string</td></tr><tr><td>N</td><td>North</td></tr><tr><td>S</td><td>South</td></tr><tr><td>W</td><td>West</td></tr><tr><td>E</td><td>East</td></tr><tr><td>NW</td><td>Northwestern</td></tr><tr><td>NE</td><td>Northeastern</td></tr><tr><td>SW</td><td>Southwestern</td></tr><tr><td>SE</td><td>Southeastern</td></tr><tr><td>TemperatureUnitCodeSimpleType</td><td>base xsd:string</td></tr><tr><td>C</td><td>Celsius Scale</td></tr><tr><td>F</td><td>Fahrenheit Scale</td></tr><tr><td>PressureUnitCodeSimpleType</td><td>base xsd:string</td></tr><tr><td>PSI</td><td>Pound per square inch</td></tr><tr><td>GPSC</td><td>Gram per square centimeter</td></tr><tr><td>MMHG</td><td>Millimeter of mercury</td></tr><tr><td>INHG</td><td>Inch of mercury</td></tr><tr><td>MB</td><td>Millibar</td></tr><tr><td>PA</td><td>Pascal</td></tr><tr><td>KPA</td><td>Kilopascal</td></tr><tr><td>MPA</td><td>Megapascal</td></tr><tr><td>T/IN2</td><td>Ton per square inch</td></tr><tr><td>PopulationDensityUnitCodeSimpleType</td><td>base xsd:string</td></tr><tr><td>URB</td><td>Urban center, densely populated</td></tr><tr><td>SUB</td><td>Suburban, predominantly single-family residential</td></tr><tr><td>RUR</td><td>Rural, scattered small communities and farms</td></tr><tr><td>PrecipitationUnitCodeSimpleType</td><td>base xsd:string</td></tr><tr><td>MM</td><td>Millimeter</td></tr><tr><td>IN</td><td>Inch</td></tr><tr><td>WaterFlowUnitCodeSimpleType</td><td>base xsd:string</td></tr><tr><td>GPM</td><td>Gallon per minute</td></tr><tr><td>LPM</td><td>Litter per minute</td></tr><tr><td>DamageExtentSimpleType</td><td>base xsd:string</td></tr><tr><td>COO</td><td>Confined to the object of origin</td></tr><tr><td>CPR</td><td>Confined to part of room or area of origin</td></tr><tr><td>CRO</td><td>Confined to room of origin</td></tr><tr><td>CFC</td><td>Confined to fire-rated comp of origin</td></tr><tr><td>CFO</td><td>Confined to floor of origin</td></tr><tr><td>CSO</td><td>Confined to structure of origin</td></tr><tr><td>EBS</td><td>Extended beyond structure of origin</td></tr><tr><td>NDM</td><td>No damage of this type</td></tr></table>

<table><tr><td colspan="3">Table A.3 A Snippet of Symbol Collection</td></tr><tr><td>Emergency Symbol</td><td></td><td>Definition</td></tr><tr><td>ParameterSafetySimpleType</td><td>base u:ImageType</td><td>A structure that describes the scene parameter security level</td></tr><tr><td><img src="/api/attachments/EMFX93WF/fulltext/images/9dfd295393ed4ea0014aad9cad22c01f8b1d7d25d287ac7f0fd2ddebe7deccef.jpg"/></td><td>ParameterSafetyLow</td><td>Low level of parameter safety</td></tr><tr><td><img src="/api/attachments/EMFX93WF/fulltext/images/ce345407f3e5428a7645fbce7069eade9e05e368a6ba6fb8d8b491ae67e4bf07.jpg"/></td><td>ParameterSafetyMid</td><td>Mid level of parameter safety</td></tr><tr><td><img src="/api/attachments/EMFX93WF/fulltext/images/18fbf8e73ed4997e9196f54e9636f604b7239795352015751cf2c9b355f44c4d.jpg"/></td><td>ParameterSafetyHigh</td><td>High level of parameter safety</td></tr><tr><td>FireLoadCodeSimpleType</td><td>base u:ImageType</td><td>A structure that describes the fire load of onsite materials</td></tr><tr><td><img src="/api/attachments/EMFX93WF/fulltext/images/c8b8bbb3e15b1455f1c8eb132a4b40cbd03a145f7c7490aad083a7d01bb9fbce.jpg"/></td><td>FireLoadHigh</td><td>High level of fire load</td></tr><tr><td><img src="/api/attachments/EMFX93WF/fulltext/images/14d2996bb718272c8c622c0eb36c5194122cbd1c2f44e3f4ec815ba264ef23f2.jpg"/></td><td>FireLoadMid</td><td>Mid level of fire load</td></tr><tr><td><img src="/api/attachments/EMFX93WF/fulltext/images/5abe134189aa806638e2147c16e08dd879a2be2ca16a56014f1e282d5126e5a1.jpg"/></td><td>FireLoadLow</td><td>Low level of fire load</td></tr><tr><td>Emergency Symbol</td><td></td><td>Definition</td></tr><tr><td>InjuritySeveritySimpleType</td><td>base u:ImageType</td><td>A structure that describes the injury level of victims</td></tr><tr><td><img src="/api/attachments/EMFX93WF/fulltext/images/3da7bbb4b7f3332469e3512f9727f60529e321f89d6ed3728003552b4f4cedab.jpg"/></td><td>InjurySeverityDead</td><td>Death</td></tr><tr><td><img src="/api/attachments/EMFX93WF/fulltext/images/88e567e6aae21d9e3391943a32fd12c3f7acbb4dd4b5c17cd39e5058860095f4.jpg"/></td><td>InjurySeverityHigh</td><td>High level of injury severity</td></tr><tr><td><img src="/api/attachments/EMFX93WF/fulltext/images/0c71197c0985b446770813af11f38e424a4172f67d3c368a9028e7fa98492953.jpg"/></td><td>InjurySeverityMid</td><td>Mid level of injury severity</td></tr><tr><td><img src="/api/attachments/EMFX93WF/fulltext/images/8b913273b08e5dcd1321023434824fae17ab18c0dfa11cb2ba3d6e4d8886b4a7.jpg"/></td><td>InjurySeverityLow</td><td>Low level of injury severity</td></tr></table>

## Appendix B

## Snippets of Data Model XML Schema

## Table B1. Snippet of the Data Type Schema

```xml
<!--Define Types-->
<xsd:complexType name='IncidentSpecificType'>
<xsd:complexContent>
    <xsd:extension base='u:ActivityType'>
    <xsd:sequence>
    <xsd:attribute ref='IncidentCategory' use='optional"/>
    <xsd:element ref='AlarmDate' minOccurs='0' maxOccurs='unbounded' />
    <xsd:element ref='AlarmTime' minOccurs='0' maxOccurs='unbounded' />
    <xsd:element ref='AlarmMethod' minOccurs='0' maxOccurs='unbounded' />
    <xsd:element ref='SituationFound' minOccurs='0' maxOccurs='unbounded' >
    <xsd:element ref='AlertLevel' minOccurs='0' maxOccurs='unbounded' />
    <xsd:element ref='Reporter' minOccurs='0' maxOccurs='unbounded' />
    <xsd:element ref='UnderControlDate' minOccurs='0' maxOccurs='unbounded' />
    <xsd:element ref='UnderControlTime' minOccurs='0' maxOccurs='unbounded' />
    <xsd:element ref='OverhaulDate' minOccurs='0' maxOccurs='unbounded' />
    <xsd:element ref='OverhaulTime' minOccurs='0' maxOccurs='unbounded' />
    </xsd:sequence>
</xsd:extension>
</xsd:complexContent>
</xsd:complexContent>
<xsd:complexType name='IncidentLocationType'>
<xsd:complexContent>
    <xsd:extension base='em:LocationType'>
    <xsd:sequence>
    <xsd:element ref='ParameterSafety' minOccurs='0' maxOccurs='unbounded' />
    <xsd:element ref='District' minOccurs='0' maxOccurs='unbounded' />
    <xsd:element ref='PopulationDensity' minOccurs='0' maxOccurs='unbounded' />
    <xsd:element ref='SurroundingRiskAssessment' minOccurs='0' maxOccurs='unbounded' />
    <xsd:element ref='Terrain' minOccurs='0' maxOccurs='unbounded' />
    </xsd:sequence>
</xsd:extension>
</xsd:complexContent>
</xsd:complexContent>
<xsd:complexType name='WeatherType'>
<xsd:complexContent>
    <xsd:extension base='u:SuperType'>
    <xsd:sequence>
    <xsd:element ref='DewPoint' minOccurs='0' maxOccurs='unbounded' />
    <xsd:element ref='WindSpeed' minOccurs='0' maxOccurs='unbounded' />
    <xsd:element ref='Humidity' minOccurs='0' maxOccurs='unbounded' />
    <xsd:element ref='Barometer' minOccurs='0' maxOccurs='unbounded' />
    <xsd:element ref='Temperature' minOccurs='0' maxOccurs='unbounded' />
    <xsd:element ref='Precipitation' minOccurs='0' maxOccurs='unbounded' />
    <xsd:element ref='Sky' minOccurs='0' maxOccurs='unbounded' />
    <xsd:element ref='InterventionIndicator' minOccurs='0' maxOccurs='unbounded' />
    <xsd:element ref='WindDirection' minOccurs='0' maxOccurs='unbounded' />
    </xsd:sequence>
</xsd:extension>
</xsd:complexContent>
</xsd:complexContent>
```

```asp
<xsd:complexType name='TemperatureMeasureType'>
<xsd:complexContent>
    <xsd:extension base='u:MeasureType'>
    <xsd:sequence>
    <xsd:element ref='TemperatureDescription' minOccurs='0' maxOccurs='unbounded' />
    <xsd:element ref=' @temperatureUnitCode' minOccurs='0' maxOccurs='unbounded' />
    </xsd:sequence>
    </xsd:extension>
</xsd:complexContent>
</xsd:complexType>
<xsd:complexType name='PressureMeasureType'>
<xsd:complexContent>
    <xsd:extension base='u:MeasureType'>
    <xsd:sequence>
    <xsd:element ref=' @pressureUnitCode' minOccurs='0' maxOccurs='unbounded' />
    <xsd:element ref='AtTemperature' minOccurs='0' maxOccurs='unbounded' />
    </xsd:sequence>
</xsd:extension>
</xsd:complexContent>
</xsd:complexType>
```

## Table B.2 Snippet of Property Schema

## <!--Define Properties-->

```xml
<xsd:attribute name='PopulationDensityUnitCodeSimpleType' type='xsd:string' />
<xsd:element name='TemperatureDescription' type='u:TextType' />
<xsd:element name=' @temperatureUnitCode' type='TemperatureUnitCodeSimpleType' />
<xsd:attribute name='SpecificInjuryLocation' type='nfirs:AreaOfFireOriginCodeSimpleType' />
<xsd:attribute name='ProtectiveEquipmentFailure' type='nfirs:ProtectiveEquipmentProblemCodeSimpleType' />
<xsd:attribute name='ProtectiveEquipment' type='nfirs:ProtectiveEquipmentCodeSimpleType' />
<xsd:attribute name='ObjectInvolved' type='nfirs:ObjectInvolvedInInjuryCodeSimpleType' />
<xsd:attribute name='PriorPhysicalCondition' type='nfirs:PhysicalConditionPriorToInjuryCodeSimpleType' />
<xsd:element name='FirefighterReference' type='ResponsePersonnelType' />
<xsd:element name='WindSpeedDescription' type='u:TextType' />
<xsd:element name='ResponsePersonnelReference' type='ResponsePersonnelType' />
<xsd:element name='ActivityReference' type='u:ActivityType' />
<xsd:attribute name='NonHumanFactoryToInjury' type='nfirs:FactorToInjuryCodeSimpleType' />
<xsd:element name='InjuryDate' type='u:DateType' />
<xsd:element name='CasualtyNumber' type='u:TextType' />
<xsd:attribute name='Disposition' type='nfirs:TakenToCodeSimpleType' />
<xsd:attribute name='HumanFactorToInjury' type='nfirs:HumanFactorToInjuryCodeSimpleType' />
<xsd:element name='ActivityReference' type='u:ActivityType' />
<xsd:element name='InjuryTime' type='niem-xsd:time' />
<xsd:attribute name='InjuryLocation' type='nfirs:InjuryLocationCodeSimpleType' />
<xsd:attribute name='ApparentSymptom' type='nfirs:PrimaryApparentSymptomCodeSimpleType' />
<xsd:element name='AlarmMethod' type='AlarmMethodCodeSimpleType' />
```
