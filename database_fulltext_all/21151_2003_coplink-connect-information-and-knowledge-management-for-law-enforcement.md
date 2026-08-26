---
otero_id: 21151
otero_key: "JEDZZQUB"
title: "COPLINK Connect: information and knowledge management for law enforcement"
authors: "Hsinchun Chen; Jenny Schroeder; Roslin V. Hauck; Linda Ridgeway; Homa Atabakhsh; Harsh Gupta; Chris Boarman; Kevin Rasmussen; Andy W. Clements"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00121-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# COPLINK Connect: information and knowledge management for law enforcement

Hsinchun Chen <sup>a,</sup>\*, Jenny Schroeder <sup>b,1</sup>, Roslin V. Hauck <sup>a</sup>, Linda Ridgeway b,1 • Homa Atabakhsh <sup>a</sup>, Harsh Gupta <sup>a</sup>, Chris Boarman <sup>a</sup>, Kevin Rasmussen <sup>a</sup>, Andy W. Clements

<sup>a</sup>Artificial Intelligence Lab, Management Information Systems Department, University of Arizona, McClelland Hall, 1130 E. Helen, Rm. 430, Tucson, AZ 85721, USA <sup>b</sup>Tucson Police Department, 270 S. Stone Ave., Tucson AZ, USA

## Abstract

Information and knowledge management in a knowledge-intensive and time-critical environment presents a challenge to information technology professionals. In law enforcement, multiple data sources are used, each having different user interfaces. COPLINK Connect addresses these problems by providing one easy-to-use interface that integrates different data sources such as incident records, mug shots and gang information, and allows diverse police departments to share data easily. User evaluations of the application allowed us to study the impact of COPLINK on law-enforcement personnel as well as to identify requirements for improving the system. COPLINK Connect is currently being deployed at Tucson Police Department (TPD). <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Artificial intelligence; Knowledge management; Information sharing; Law enforcement

## 1. Introduction

## 1.1. Law-enforcement information sharing

Successful law enforcement depends upon information availability. A police officer on the beat wants to know if the person being interviewed has been involved in the previous incidents or is associated with a gang. A detective wants to know if there is a verifiable crime trend in a neighborhood or whether a vehicle involved in one incident is linked to other incidents, but it is often difficult to obtain even such basic information promptly.

The problem is not necessarily that the information has not been captured—any officer who fills out up to seven forms per incident can attest to that. The problem is one of access. Typically, law-enforcement agencies have captured data only on paper or have fed it into a database or crime information system. If the agency involved has more than one databases (that are possibly incompatible), information retrieval can be difficult or time-consuming.

A number of government programs are trying to address these issues. The Office of Justice Programs (OJP) Integrated Justice Information Technology Initiative is using the resources of five bureaus including the National Institute for Justice (NIJ) in an effort to improve the effectiveness of the justice information systems through better information sharing. The NIJ information sharing initiative is the AGILE program, which falls under the NIJ Office of Science and Technology (OS&T) and primarily addresses interoperability issues (for more information on justice initiatives, visit http://www.ojp.usdoj.gov).

In order to better explain the situation, here is an example scenario.

A crime has occurred at a given address in Tucson. One of the suspects is a person known by the alias ‘‘baby gangster.’’ The responding police officer would like to know more about this person including his real name, previous involvement with other crimes, whether he is a member of a gang, and if possible, see a picture of him. At the Tucson Police Department, information such as a person’s mug shot (picture) and involvement in a gang are each stored in separate databases, which in turn are stored separately from incident records. The police officer will have to know how to search information in these separate databases using different user interfaces. The problem can be further complicated if this suspect runs away to the Phoenix area. The police officer would have to call the Phoenix Police Department and ask to search for this suspect in their databases. As will be discussed in this paper, COPLINK Connect addresses these difficulties by providing easy access to various databases and providing an infrastructure for information sharing among various law-enforcement agencies (a distributed version of COPLINK is being developed but is beyond the scope of this paper).

## 1.2. Research test bed and case study: the Tucson Police Department

The Tucson Police Department (TPD) has encountered all the problems described in the previous section. Its information sources have included at least three distinct systems as shown in Table 1.

The records management system (RMS) contains approximately 1.5 million incident record sets. The criminal information computer (CIC) tracks the approximately 1200 individuals the department considers responsible for a majority of major crimes. Each of these systems has a different user interface, so accessing related information from any two or all three has been difficult, cumbersome, and time-consuming.

Table 1 TPD information sources

<table><tr><td>TPD system</td><td>Contents</td><td>Database platform</td></tr><tr><td>RMS</td><td>Incident reports</td><td>Oracle 8</td></tr><tr><td>Mug shots</td><td>Photos taken at time of arrest, Mugshot related information</td><td>ImageWare Software Sybase</td></tr><tr><td>Criminal information computer</td><td>Gang information</td><td>MS Access</td></tr></table>

As an NIJ-funded multi-year project, the major goals for the COPLINK project for TPD $\mathrm { a r e } ^ { 2 }$ the following.

First, to develop an integrated system to allow TPD officers easy access to all the information contained in all three systems.

Second, and perhaps more importantly, to design a prototype system for use in developing similar systems at other police departments.

Finally, with the first two goals in mind, to offer a model for allowing different police departments to share information easily.

## 2. Literature review: information sharing and knowledge management in law enforcement

Database technology plays an important role in the management of information for a police department. Previous research has described organization of information in a database system that can be easily searched by officers and other police-department staff [13,15,18,19,22,25]. The use of relational database systems for crime-specific cases such as gang-related incidents, and serious crimes such as homicide, aggravated assault, and sexual crimes, has been proven highly effective [10,20]. Deliberately targeting these criminal areas allows a manageable amount of information to be entered into a database and, in addition, combines information that exists in neighboring police districts. Although law-enforcement information is stored in these efficient databases, various kinds of data sources usually reside in separate databases. COPLINK addresses this issue by providing one easy-to-use user interface, through which various databases can be accessed (e.g. for TPD: incidents records, mug shots and gang information).

Automated record-management databases rapidly are replacing paper records of crime and police-report information. Most mid- and large-sized police agencies have made such systems available to their own personnel but lack resources that allow efficient transmission of information to other agencies. Criminals disregard jurisdictional boundaries and, in fact, take advantage of the lack of communication across jurisdictions. Federal standards initiatives such as the National Incident Based Reporting System (NIBRS) [24] are aimed at providing reporting standards that will facilitate future reporting and information sharing among police agencies as electronic reporting systems proliferate. The current TPD RMS system is not NIBRS compliant, but both the TPD and PPD are moving towards NIBRS compliant systems. If COPLINK’s underlying database system is NIBRS compliant, COPLINK will be as well.

As the number of agencies that take advantage of various existing law-enforcement information technologies expands, the development of useful artificial intelligence tools continues to progress. Although the many potential uses of databases, intelligence analysis and other technologies have yet to be fully explored [5,6,12], a number of systems currently serve as information management or intelligence analysis tools for law enforcement. The following highlights some of these systems.

. The Timeline Analysis System (TAS) uses visualization and time analysis to examine information and help analysts visually examine large amounts of information by illustrating cause-and-effect relationships. This system graphically depicts relationships found in data, revealing trends or patterns [20].

. Use of expert systems in law enforcement, includes systems such as those described in Ref. [2] and AICAMS [3].These systems attempt to aid in information retrieval by drawing upon human heuristics or rules and procedures to investigate tasks. The AICAMS project is a collaboration between the Chi nese University of Hong Kong (CUHK) and the Hong Kong Police Force (HKPF). At present, the AICAMS knowledge-based system still lacks the required precision for identifying suspects, due to incomplete data and rule base. AICAMS also includes a component to fulfill the needs for a simple but effective facial identification procedure based on a library of facial components from the HKPF. The system provides a capability for assembling an infinite number of possible facial composites by varying the position and size of the components. AICAMS also provides a geomapping component by incorporating a map-based user interface. For more information, refer to AICAMS, http://www.se.cuhk.edu.hk/ f aicams.

. INFOTECH International, a Tampa, FL-based company focusing on developing public safety solutions to improve information sharing between lawenforcement agencies, is hardware-platform independent and Windows-based. The goal is to utilize web-browser and security technology to enable secure data transmission, mainly through the use of a public key infrastructure. For more information, refer to Infotech [14], http://www.sierrawireless.com/ PartnersResellers/mobiletec.html.

. Future Alert Contact Network (FALCON) is a community policing-based system developed at Charlotte, NC. FALCON receives a request, monitors all incoming records relevant to the request and then notifies the officer by email or pager when the request is met. The goal of FALCON is to make the problem identification function in community policing more proactive by providing early notification of crime events based on user requests. FALCON allows officers to submit simple requests (e.g. notify when three or more rapes occur), as well as highly complex requests (notify when an armed robbery occurs at a liquor store by a white male with a 357 magnum). The system shifts the data analysis burden away from the officer, eliminating the need to conduct time-consuming searches of existing databases [9].

. Consolidated Criminal History Reporting System (CCHRS) was developed at Sierra Systems for Los Angeles County [23]. The criminal justice system and the supporting information systems in Los Angeles County had a case-oriented focus, in which information was organized by arrests, court cases, jail bookings, probation cases, etc. Frequently, access to an individual’s complete criminal history was required for setting bail, determining charges, releasing prisoners or making sentencing decisions. The information systems available in Los Angeles did not readily support this required, consolidated view of an individual’s criminal history. Sierra Systems developed a strategy to retrieve and display consolidated information to key criminal justice users without the need to replace the county’s existing information systems.

Each of the above systems has its own drawbacks. The systems based on expert systems, for example, encounter the problem of not having a complete knowledge base. The other systems mentioned usually implement only a certain aspect of knowledge management for law enforcement. For example, the Timeline system provides a visual aid and time analysis component, AICAMS provides geo-mapping and composes an infinite number of possible facial composites, Infotech’s goal is to enable secure data transmission, Falcon provides early notification of crime events to officers, based on the requests received, and CCHRS retrieves and displays consolidated information to officers.

The goal of COPLINK Connect is to provide an integrated solution to law enforcement by allowing access to multiple databases through one user interface as well as through information sharing between various agencies. These aspects will be discussed in the rest of this paper. Also, work is underway on the integration of other functions into COPLINK. These include crime analysis [11,12], geo-mapping, visualization of relationships, text analysis [1], agent-based collaboration [4] and distributed COPLINK. These latter aspects are, however, out of the scope of this paper.

## 3. Design criteria

The target users of COPLINK are not experienced IT users, but have pressing, critical information needs. The design of COPLINK Connect was closely guided by user requirements acquired through brainstorming sessions, system demos, structured questionnaires and interviews.

The main design criteria considered for the COPLINK project included the following:

 Platform independence: Because not all police departments utilize the same hardware or software, platform independence was critical.

 Stability and scalability: The system also had to offer room for system growth and expansion.

 Intuitive and ease of use: The front-end user interface should be intuitive and easy to use, yet flexible to meet the demanding investigative needs of detectives and officers.

Typical law-enforcement applications usually are legacy systems having out-dated performance and capability. For example, TPD’s RMS took 30 s to answer simple requests and up to 30 min for more complex queries. Improved response time was critical to restoring departmental efficiency. To ensure application speed, issues of data and network communication, disk access and system I/O needed to be addressed. This also meant carefully distributing logic where it could be most quickly and efficiently executed, i.e. all user-input error checking should be done in the front end, and all database access logic achieved through pre-compiled stored PL/SQL procedures in the database.

## 3.1. Data organization and access

Another critical issue, especially in designing a system that could be deployed across multiple lawenforcement agencies, was acknowledging that no two agencies would store their incident data in exactly the same way. Therefore, it was important to come up with a data organization design that was flexible enough to be applied to any underlying data set. The database team designed a series of standardized ‘‘views’’ that fitted typical information search and presentation situations. For example, most of the data in the TPD systems were related to ‘‘Person,’’ ‘‘Location,’’ ‘‘Vehicle,’’ or ‘‘Incident’’ information. A set of views was developed for each of these areas of interest, with the underlying data sets mapped to those standard views, making the system more portable to other law-enforcement agencies.

Current law-enforcement data are scattered over distributed information sources. To find relevant information, officers need to know which data sources contain the information needed, and how to access them. They have to manually integrate retrieved data, and they have to know how to use all the different data sources.

COPLINK provides two levels of data integration:

 data integration within the same agency. For example, at TPD: the RMS system (incident records), mug shots, and gang data sources (see Table 1),

 data integration between different agencies: a distributed version of COPLINK is being developed. It will operate initially between Tucson and Phoenix.

COPLINK provides direct access to various data sources through one graphical user interface. The mug shots and gang information, for example, each resides in a different database (each being separated from RMS that contains the incidents records). COPLINK, however, provides integrated access to these separate databases. This integration is very critical for lawenforcement investigation. Police officers are too busy and time is usually critical for their investigations. With the data integration provided in COPLINK, the officers do not need to access many different systems.

## 3.2. Search functionality

In designing COPLINK Connect, we made the decision to limit the scope of searches the system can perform, to better suit the needs of the officers. Four types of searches are made available to the user: person, vehicle, incident, and location (see Fig. 1 in the appendix). These categories correspond to the manner in which police officers perform their search. These four search forms provided in COPLINK present an analysis template for the police officers tasks. Also, police officers prefer to have independent searches (independent search forms rather than a combination).

We found through our user studies that officers often prefer to sort the return results of a search for a person, by the date of birth since, for example, a witness can usually guess an approximate age for the suspect. This feature is provided in COPLINK Connect (see Fig. 3 in the appendix). Alternatively, COPLINK Connect allows the results to be sorted by crime type. This is useful when, for example, the officer is especially interested in a particular crime type such as stolen vehicles. In this case, sorting by type of crime allows the information to be found more easily (see Fig. 5 in the appendix). These design decisions were made after extensive user requirements acquisition effort, and the corresponding functionalities are provided in COPLINK.

## 3.3. User interface

The user interface was also designed by conforming to the police officers’ expressed needs. Police officers often conduct searches based on incomplete information (e.g. partial license plate number, partial name). Support for this partial matching is built into COPLINK Connect.

Police officers often need to document the manner in which they have drawn a conclusion. This document is used in legal proceedings to justify subsequent actions. The search history window is designed to address this need (see left-most panel in the screen shots given in Figs. 2–6. The search history can be printed and presented in court. The search history also allows an efficient way for officers to review their own search scenarios. In addition, the search logs can be used as training cases for new police officers.

## 3.4. System architecture

Ease of installation, maintenance, system extensibility and cost effectiveness are important issues for law enforcement. Law-enforcement IT departments are usually under staffed and do not have time to update the application. Its user interface has to require minimum training (point and click). The current system architecture was designed for low maintenance, ease of installation and extensibility while keeping the cost low.

## 4. Graphical user interface for COPLINK Connect: an example

The graphical user interface (GUI) for the COPLINK Connect Application is shown in Figs. 2 – 6. The actual information has been altered to maintain data confidentiality. The Java front-end consists of two major parts, the input and display of data and the processing of information. Working closely with TPD officers, the COPLINK team first made low-fidelity, paper prototypes of the screens used to obtain feedback on the display and organization of the information. These were used to modify the design and functionality of the interface. Display of results was important to the front-end. We learned that a user’s idea of what constitutes a manageable and intuitive display varied with the query type and sometimes required formatting in a different way. We responded by creating a dynamic text table, using the Java API to make the interface more flexible. The figures given in the appendix (Figs. 2–6) illustrate a sample scenario in which an officer used the COPLINK Connect to search for information.

## 5. User evaluation for COPLINK Connect

## 5.1. Study design and results

A usability evaluation was conducted to assess the achievement of a number of the goals that guided the design and development of the COPLINK Connect. The series of items that comprised the usability questionnaire were based upon a number of widely used measures [7,8,16,17,21]. Items on the questionnaire used to assess and compare the COPLINK and RMS systems were based upon user perceptions of such widely used measures of usability as: effectiveness (impact of system on job performance, productivity, effectiveness of information, and information accuracy), ease of use (measures of effort required to complete a task, ease of learning how to use the application, ability to navigate easily through the different screens, and satisfaction with the interaction), and efficiency (speed of completing tasks, organization of the information on the screens, ability to find information and the interface design itself). Individual items and reliabilities for each variable are provided in Appendix A.

Benchmark levels from TPD’s current RMS system for all three usability factors were established and compared with those from COPLINK Connect. In addition to written questionnaires, observation of the data collection methods and structured interviews were used both to supplement findings and to provide feedback for further development efforts. In the structured interviews, participants were asked about ways in which they thought RMS was better than COPLINK, ways in which COPLINK was better than RMS, how they would use COPLINK in their jobs. They also were asked to report changes or additions that they would make to COPLINK as well as any suggestions regarding the visual aspect of COPLINK.

A group of 52 law-enforcement personnel was recruited to participate in this study. Participants represented a number of different job classifications and backgrounds (e.g. time at TPD, comfort level with computers, etc.). The data collection sequence was as follows. Initially, all subjects were asked to complete a pre-interaction questionnaire, establishing demographic background and prior level of computer experience (in general and with the current RMS system). Participants were then given a questionnaire that targeted the perceived usability of the current RMS system. After a brief introduction to the COPLINK Connect application, subjects were asked to complete at least two search tasks (stating the goal of each task) using COPLINK Connect. As participants accomplished these tasks, asking them to think aloud allowed us to collect process data. After a usability questionnaire on COPLINK Connect had been completed, a brief interview on the COPLINK Connect experience concluded the study.

Both interview data and survey-data analyses support a conclusion that use of COPLINK Connect provided improved performance over use of the current RMS system. For all three measures, participants rated COPLINK significantly higher than they rated RMS. Table 2 presents the mean differences in COPLINK and RMS usability ratings.

In addition to statistical data, these findings are supported by qualitative data collected from participant interviews. Comments collected from interviews indicate that COPLINK Connect was rated higher than RMS in terms of interface design and performance as well as functionality. The general themes that emerged from the interviews also can be categorized into factors of speed, ease of use, interface, and information quality.

Participants indicated that the quality and quantity of information from COPLINK Connect surpassed those of RMS. In a review of current RMS practices, a number of detectives and officers were actually unable to use RMS but were able to use COPLINK Connect to conduct searches. It is evident from this research study that COPLINK Connect allowed a population of TPD personnel to access information that would have been quite difficult for them to have acquired using the RMS system. From both the questionnaire and the interview data collected from this evaluation, it is evident that many participants rated the information found in COPLINK more useful than the information in RMS. This finding is very interesting, because most of the information contained in COPLINK have been taken from RMS.

Table 2  
Mean differences for COPLINK and RMS usability ratings

<table><tr><td rowspan="2">Variables</td><td>COPLINK</td><td>RMS</td><td rowspan="2">F (1,45)</td></tr><tr><td>M (SD)</td><td>M (SD)</td></tr><tr><td>Effectiveness</td><td>4.1 (0.5)</td><td>3.6 (0.6)</td><td>24.4*</td></tr><tr><td>Ease of use</td><td>4.1 (0.4)</td><td>3.5 (0.7)</td><td>43.1*</td></tr><tr><td>Interface design</td><td>4.1 (0.4)</td><td>3.1 (0.7)</td><td>70.1*</td></tr></table>

\* p < 0.001.

COPLINK’s ability to allow the user to structure his/her query results by selecting from a number of fields is an important strength of the system. Being able to sort query areas allows users to organize the results meaningfully in the context of a specific search task. Cases are organized in RMS by date. COPLINK Connect, on the other hand, allows users not only to organize by date but also to sort by crime type or even team and beat. Patrol officers who participated in the study indicated that the availability of COPLINK Connect at substations (within their individual areas) or in patrol cars would greatly improve on-the-street access to information that currently is unavailable there. In particular, they stressed the importance of being able to use mug shots to determine identity quickly. One patrol officer related an incident in which he apprehended a suspect he believed to be wanted for prior criminal activity. Using RMS, the only way the officer could verify the identity of the suspect was to take the person physically to downtown headquarters and have the identification office check his fingerprints. The patrol officer indicated that had he had COPLINK Connect, either in the patrol car or at one of the local substations, he could quickly and easily have verified the person’s identity by checking mug shots on file as well as current case information on the ‘wanted’ person.

Users participating in a follow-on study received a journal to document their search queries and comments for system improvement. Included on the journal sheets were seven measures. We received 23 journal sheets for analysis. Analysis of the specific goals for each response indicates a number of interesting issues regarding the users’ perceptions of the COPLINK system.

A number of journal entries were affected by machine performance of participants using lower end machines, resulting in problems in interface performance (i.e. performance issue with JAVA). A number of searches were rated lower because participants were searching for functionalities or information not included in COPLINK.

Another important issue that affected the effectiveness and efficiency of COPLINK is training and familiarity with COPLINK. Some participants indicated having problems with partial searching as well as understanding the information returned from the system. These issues could have been dealt with by proper training.

These analyses indicate a number of important issues for future development as well as implementation and deployment. We need to revisit the additional functionalities and information that users have requested. In the deployment and implementation of COPLINK, we need to focus on establishing minimum system requirements so that we can identify which low end machines will have problems running COPLINK. Finally, we need to establish formal training mechanisms and support for user training.

## 5.2. Sample cases and user feedback

During the time of user evaluation, use of COPLINK Connect had led to the investigation of cases that would otherwise not been picked up, and contributions to making multiple arrests. During interviews and in journals, users shared with us stories and examples of real cases they investigated using COPLINK Connect. We are continuing to follow up on a number of cases pending further investigation. The following are four examples of such cases.

The Case: A detective in the auto theft division was trying to find information on a suspect who stole a vehicle from his employer. The detective had searched for the name (‘‘O’Kene \* ’’) on the Records Management System and got no return.

Using COPLINK Connect: After entering the same name in COPLINK and getting no return, the detective conducted a COPLINK Connect partial search by entering (‘‘Ok’’). He found an individual with the name ‘‘O’Kane’’ who had the same date of birth as his suspect. After looking in the person’s details, the detective realized that the officer who wrote the case report misspelled the suspect’s last name O’Kene instead of O’Kane. In addition, he found information on the suspect’s girlfriend, including an address and phone number.

Current case status: The suspect is being sought for arrest.

User comments: With COPLINK Connect, you can enter partial info and get returns you cannot get without perfectly complete information in RMS. If I had not had COPLINK Connect, investigating this case would have been quite difficult and most likely would have been dropped.

The Case: An officer in the Surveillance Division was working on a residential burglary. The officer had limited information on a suspect (first name, last name, and an approximate DOB).

Using COPLINK Connect: After conducting a name search in COPLINK Connect, in seconds, the officer had the suspect’s current address, and was able to see the suspect’s prior offences for larceny in Tucson.

Current case status: The individual was put under surveillance and arrested while committing another burglary.

User comments: The speed of the COPLINK Connect search was extremely vital in this case due to time constraints. Cases such as this one, where such information is gathered ‘‘on the fly’’, comprise about 90% of the cases that I work on, so being able to get information quickly is really important.

The Case: An auto theft case in which an associate (boyfriend) stole a woman’s car.

Using COPLINK Connect: A sergeant in auto theft conducted a name search with COPLINK Connect on the associate. This individual’s name came back with prior offenses involving shootings and auto theft, as well as gang affiliation.

Current case status: The case was assigned to a detective for further investigation.

User comments: Normally, due to the high level of auto theft cases, and the relatively low number of available detectives, if a case does not stand out as being able to be solved easily or has another element that makes it attractive to investigate, the case will be dropped. If I had not used COPLINK (Connect), I would have literally thrown away this case due to its very nature.

The Case: A highway robbery case where three males robbed two girls.

Using COPLINK Connect: A crime analyst assigned to the case used COPLINK Connect to find suspects’ prior offenses, addresses, and associates.

Current case status: Two males have been arrested, another is still a suspect.

User comments: The ability to search quickly makes it easier to find information. In general, I use RMS as a supplement to COPLINK for purposes of TPD related research. I find COPLINK to be more user friendly. The fact that there are mug shots helps immensely. Without those, I need to go physically to another terminal in another room to run that person for a photo. Also, when I need a photo for a bulletin or other document, I simply save the ‘person’ screen and crop the image. I then insert that image into the document I am working on. This still results in a time-savings over going to another computer. I like the fact that you can sort entries in any of the tables. I find the data retrieved, while identical to RMS, easier to read and decipher.

## 5.3. Current status

Since our initial user study in 1999, the COPLINK Connect application has gone through a few iterations based on feedback from our users. In Spring 2001, COPLINK Connect was formally deployed at TPD. Currently, there are about 500 COPLINK Connect users in TPD, covering almost all TPD job classification and ranks. The user receptivity has been overwhelmingly positive.

A distributed COPLINK Connect application for TPD and 15+ other law-enforcement agencies in the Phoenix area is under development. Using a similar three-tier web-based architecture, we are anticipating an Arizona-wide solution in Fall 2002.

## 6. Areas for improvement

In spite of all the advantages COPLINK Connect offers (as discussed in the previous sections), we still see some areas for improvement.

. COPLINK Connect was designed and developed mainly for use by police officers. Other users such as detectives and crime analysts have needs that go beyond what Connect offers. For example, there is a need to perform sophisticated searches and to find links (relationships) between various entities (e.g. different suspects or victims, a stolen vehicle, etc.). This has motivated the development of COPLINK Detect [12]. The target users of Detect are detectives and crime analysts. Crime analysis is based on creating associations and linkage between various entities involved in a crime. Using Detect, investigators can find links between known entities (e.g. victim or suspect) and other objects (e.g. stolen vehicle, suspect from a different incident, etc.). Detect allows for entry of multiple criteria for a search (e.g. combination of people, vehicles, etc. and their linkages). Connect was intentionally designed to be simple in use by police officers. Detect was designed to be more powerful for use by detectives and crime analysts. These decisions were based on extensive user studies.

. Selecting an appropriate system architecture can be difficult. Issues such as stability and maturity of the emerging open-standard technologies and protocols need to be carefully examined.

. Police officers spend a lot of time on the streets investigating crimes. To accommodate this mobility, wireless access is important. We are currently studying wireless access to COPLINK.

. Geographical locations play a central role in law enforcement. It would be of value to the police officers if the results of COPLINK Connect could be displayed on a map. Work is under way to develop a geo-mapping component for COPLINK [1].

. Our user requirements studies have also shown that officers and detectives would like to share information search experience with other team members. We are currently working closely with law-enforcement personnel to develop a collaboration component for COPLINK [4].

## 7. Future directions for COPLINK

Large collections of unstructured text as well as structured case-report information exist in police records systems. These textual sources contain rich information for investigators that are often not captured in the structured fields. We have recently started to explore the development of textual mining approaches that support knowledge retrieval from such sources for law enforcement [1]. In order to perform a fine-grained analysis for law-enforcement content, we will be investigating the development of linguistic analysis and textual mining techniques that make intelligent use of large textual collections in police databases.

Several Internet research projects have shown the power of a new ‘‘agent’’-based search paradigm. In addition to supporting conventional searches performed by users, search agents allow users automatically to establish search profiles (or create profiles for users) and extract, summarize, and present timely information content. We believe such a proactive search agent is well suited to use by investigative personnel in law-enforcement agencies. Search agents for law enforcement can support conventional searching techniques, and be profiled for specific investigations. We plan to develop a personalized lawenforcement search agent that will support wide expansion in connectivity and information sharing between police agencies.

## Acknowledgements

This project has primarily been funded by the following grants: NSF, Digital Government Program, ‘‘COPLINK Center: Information and Knowledge Management for Law Enforcement,’’ #9983304, July 2000–June 2003.

National Institute of Justice, ‘‘COPLINK: Database Integration and Access for a Law Enforcement Intranet,’’ July 1997 – January 2000.

We would also like to thank the Digital Equipment Corporation External Technology Grants Program, agreement #US-1998004, for its award of an equipment grant of a DEC Alpha Server for the COPLINK Project.

We would like to thank the following people for their support and assistance during the entire project development and evaluation process: Andy Moosmann, Ann Lally, Kevin Lynch, and other members at the University of Arizona Artificial Intelligence Lab, Detective Tim Petersen, Dan Casey and other personnel from the Tucson Police Department, and Joe Hindman and other personnel from the Phoenix Police Department.

Appendix A. Scale items and Cronbach alpha reliabilities of usability measures (1=strongly disagree, 5=strongly agree)

<table><tr><td>Measures and items</td><td>Reliability (α)</td></tr><tr><td colspan="2">Effectiveness</td></tr><tr><td>RMS</td><td>0.89</td></tr><tr><td>COPLINK</td><td>0.90</td></tr><tr><td>(1) The information provided by the system is effective in helping me complete my task.</td><td></td></tr><tr><td>(2) Using this system improves my job performance.</td><td></td></tr><tr><td>(3) Using this system in my job increases my productivity.</td><td></td></tr><tr><td>(4) Using this system enhances my effectiveness on the job.</td><td></td></tr><tr><td>(5) I am satisfied with the accuracy of this system.</td><td></td></tr><tr><td colspan="2">Ease</td></tr><tr><td>RMS</td><td>0.90</td></tr><tr><td>COPLINK</td><td>0.85</td></tr><tr><td>(1) Overall, I&#x27;m satisfied with how easy it is to use this system.</td><td></td></tr></table>

Appendix A (continued)

<table><tr><td>Measures and items</td><td>Reliability (α)</td></tr><tr><td>(2) This system is NOT simple to use. (reverse coded)</td><td></td></tr><tr><td>(3) Learning to operate this system was easy for me.</td><td></td></tr><tr><td>(4) My interaction with this system is clear and understandable.</td><td></td></tr><tr><td>(5) It is easy to learn to use this system.</td><td></td></tr><tr><td>Interface</td><td></td></tr><tr><td>RMS</td><td>0.92</td></tr><tr><td>COPLINK</td><td>0.90</td></tr><tr><td>(1) The interface of the system is pleasant to look at.</td><td></td></tr><tr><td>(2) I like using the interface of the system.</td><td></td></tr><tr><td>(3) Navigation through the system screens and menus is easy and intuitive.</td><td></td></tr><tr><td>(4) The organization of information on the system screen is clear.</td><td></td></tr><tr><td>(5) The sequence of the system screens is confusing to me. (reverse coded)</td><td></td></tr><tr><td>(6) It is easy to find information I need on the system screen.</td><td></td></tr></table>

Appendix B. Figures  
![](/api/attachments/JEDZZQUB/fulltext/images/83e1afdd97feb19c5201114c4d3bbf4742f84271ed0b54a084da8501792931f0.jpg)

An officer wanting to know more about a particular incident or person can enter a query in the search form, query further through the summary table to see details about a person, or select an incident from the incident summary table to view on the case details summary screen. In previous screens, information could be displayed in formatted rows, but a more dynamic display was needed. For example, mug shots needed to be displayed both as person details and on the case-details screen. To accommodate this feature, screens have been laid out in clusters, grouping information for easier understanding. This in turn required manipulating the data retrieved and capturing pictures from the database, a problem solved by constructing a cyclical procedure that would loop through the data and build a hierarchical tree. We could then apply display patterns to the nodes of the tree, navigate the tree and place the information on the screen.

Fig. 1. Screen flowchart.

Figs. 2– 6: Sample scenario: An officer is trying to identify a suspect involved in an automobile theft. A confidential informant has reported that the suspect goes by the street name ‘‘Baby Gangster’’, is about 20 (probably born in 1979), and is around $5 ^ { \prime } 3 ^ { \prime \prime }$ tall.  
![](/api/attachments/JEDZZQUB/fulltext/images/d40d678f76940a3c58d3d6d6b836b528aee3833c13929e801ce8025f1afa883e.jpg)

Fig. 2. COPLINK Connect Search Screen. The officer can choose one of the four types of information upon which to search: Person, Location, Incident, or Vehicle. The officer selects the Person search screen and enters ‘‘baby $\mathbf { g } '$ in the COPLINK Connect system. Note the left panel history screen, which keeps track of the user’s searches.  
![](/api/attachments/JEDZZQUB/fulltext/images/2123f8651831a3a4e3130263c3f62c48a852639a4e479113ed4f47990deaf758.jpg)  
Fig. 3. Person Summary Screen. The system returns 58 listings referring to ‘‘baby $\mathbf { g } ; \mathbf { \Sigma } ^ { \ast }$ (all of the returns include the name ‘‘baby g).’’ The system permits sorting by any of the column headings in the table. The officer chooses to sort by date of birth and finds an entry for ‘‘baby gangster,’’ born in 1979, whose height is $5 ^ { \prime } 2 ^ { \prime \prime }$ . The officer then clicks on the ‘‘See Details’’ button to find out more about this particular ‘‘Baby Gangster’’.

![](/api/attachments/JEDZZQUB/fulltext/images/d06771ab0f35dfdb0ee35f2230ce6b3cd0997698702099391b791e93dc6e7622.jpg)

Fig. 4. Person Details Screen. This screen contains personal information about the selected person, including real name, latest description information, latest home address, other identifiers that the person may use, and a mug shot, if available. The officer now has a real name of a person who matches the description of the possible suspect he was given. The officer then decides to go to the incident summary screen to get an idea of the cases in which this person has been involved.

## References

[1] H. Atabakhsh, J. Schroeder, H. Chen, M. Chau, J. Xu, J. Zhang, H. Bi, COPLINK knowledge management for law enforcement: text analysis, visualization and collaboration, Proceedings of the National Conference on Digital Government Research, Digital Government Research Center, LA, Los Angeles, (May 2001).

[2] J.E. Bowen, An expert system for police investigators of economic crimes, Expert Systems with Applications 7 (2) (1994) 235–248.

[3] J.W. Brahan, K.P. Lam, H. Chan, W. Leung, AICAMS: artificial intelligence crime analysis and management system, Knowledge-Based Systems 11 (1998) 335 – 361.

[4] M. Chau, H. Atabakhsh, D. Zeng, H. Chen, Building an infrastructure for law enforcement information sharing and collaboration: design issues and challenges, Proceedings of the National Conference on Digital Government Research, Digital Government Research Center, LA, Los Angeles, (May 2001).

[5] H. Chen, Machine learning for information retrieval: neural networks, symbolic learning, and genetic algorithms, Journal of the American Society for Information Science 46 (3) (1995) 194– 216.

[6] H. Chen, T. Ng, An algorithmic approach to concept exploration in a large knowledge network (automatic thesaurus consultation): symbolic branch-and-bound search vs. connectionist Hopfield net activation, Journal of the American Society for Information Science 46 (5) (1995) 348 – 369.

[7] J.P. Chin, V.A. Diehl, K.I. Norman, Development of an instrument measuring user satisfaction of the human – computer interface, ACM Chi’88 Proceedings, 1988, pp. 213– 218.

[8] F.D. Davis, Perceived usefulness, perceived ease of use, and user acceptance of information technology, MIS Quarterly 13 (3) (1989) 319 – 340.

[9] Falcon, Future Alert Contact Network: Reducing Crime Via Early Notification, University of North Carolina at Charlotte (UNCC); Charlotte-Mecklenburg Police Department (CMPD); City of Charlotte, North Carolina (1998). http://pti.nw.dc.us/ solutions/solutions98/public<sup>\_</sup>safety/charlotte.html.

<table><tr><td colspan="8">Incidents Summary Table
Number of Hits - 19</td></tr><tr><td></td><td>Case #</td><td>Address</td><td>Crime_type</td><td>Team</td><td>Beat</td><td>GANG</td><td>Role</td></tr><tr><td rowspan="2">Person</td><td>9711210514</td><td>S FIESTA.AV</td><td>0301</td><td>1</td><td>55</td><td></td><td>SUSPECT</td></tr><tr><td>9711260139</td><td>E ALVORD RD</td><td>0301</td><td>1</td><td>54</td><td></td><td>ARREST</td></tr><tr><td rowspan="2">Location</td><td>9711260135</td><td>6100 S RANDALL BL</td><td>0301</td><td>1</td><td>54</td><td></td><td>ARREST</td></tr><tr><td>9711260129</td><td>S 4 AV</td><td>0301</td><td>1</td><td>56</td><td></td><td>ARREST</td></tr><tr><td rowspan="2">Incident</td><td>9607240525</td><td>6300 S MISSIONDALE RD</td><td>0301</td><td>1</td><td>55</td><td></td><td>VICTIM</td></tr><tr><td>9709160628</td><td>4500 N VIA ENTRADA 94</td><td>0701</td><td>3</td><td>11</td><td></td><td>ARREST</td></tr><tr><td rowspan="13">Vehicle</td><td>9606110383</td><td>1300 E FORT LOWELL RD</td><td>0701</td><td>3</td><td>10</td><td></td><td>ARREST</td></tr><tr><td>9711250126</td><td>6300 S SANTA CLARA.AV</td><td>0701</td><td>1</td><td>55</td><td></td><td>ARREST</td></tr><tr><td>9605190263</td><td>6700 E CARONDELET DR 300</td><td>0701</td><td>4</td><td>09</td><td></td><td>ARREST</td></tr><tr><td>9607100390</td><td>700 E IRVINGTON RD 400</td><td>0701</td><td>1</td><td>51</td><td></td><td>ARREST</td></tr><tr><td>9701160758</td><td>W CALLE ANTONE</td><td>0704</td><td>1</td><td>55</td><td></td><td>ARREST</td></tr><tr><td>9405018004</td><td>3600 E BROADWAY BL</td><td>0901</td><td>3</td><td>52</td><td></td><td>SUSPECT</td></tr><tr><td>9101110090</td><td>6300 S SANTA CRUZ</td><td>1401</td><td>1</td><td>6</td><td></td><td>ARREST</td></tr><tr><td>9703040753</td><td>100 W CALLE ANTONE</td><td>2604</td><td>1</td><td>55</td><td></td><td>SUSPECT</td></tr><tr><td>9703040752</td><td>100 W CALLE ANTONE</td><td>2604</td><td>1</td><td>55</td><td></td><td>OTHER</td></tr><tr><td>9506210060</td><td>300 W CALLE ANTONE</td><td>2605</td><td>1</td><td>55</td><td></td><td>ARREST</td></tr><tr><td>9711260432</td><td>4400 S PARK AV</td><td>2701</td><td>1</td><td>08</td><td></td><td>ARREST</td></tr><tr><td>9607180830</td><td>100 W CALLE ANTONE</td><td>2901</td><td>1</td><td>55</td><td></td><td>ARREST</td></tr><tr><td>9612310866</td><td>100 W CALLE ANTONE</td><td>2901</td><td>1</td><td>55</td><td></td><td>ARREST</td></tr></table>

Fig. 5. Incident Summary Screen. This screen displays all the incidents in which the selected person has been involved. The officer sorts by crime type, looking for cases of stolen vehicles (0701) and finds the suspect has been involved in four such incidents, either as a suspect or as an arrestee. The officer selects Case #9711250126 to look at the actual case information.

[10] B. Fazlollahi, J.S. Gordon, CATCH: computer assisted tracking of criminal histories system, Interfaces 23 (2) (1993) 51 – 62.

[11] R.V Hauck, H. Chen, COPLINK: a case of intelligent analysis and knowledge management, Proceedings of the 20th Annual International Conference on Information Systems, ’99, Association of Information Systems, Atlanta, 1999, pp. 15– 28.

[12] R.V. Hauck, H. Atabakhsh, P. Ongvasith, H. Gupta, H. Chen, COPLINK concept space: an application for criminal intelligence analysis, IEEE Computer Digital Government Special Issue 35 (3) (2002) 30–37.

[13] M.J. Hoogeveen, K. Van der Meer, Integration of information retrieval and database management in support of multimedia police work, Journal of Information Science 20 (2) (1994) 79–87.

[14] Infotech, http://www.sierrawireless.com/PartnersResellers/ mobiletec.html.

[15] C. Lewis, Police information technology, GEC Review 9 (1) (1993) 51 – 58.

[16] J.R. Lewis, IBM computer usability satisfaction questionnaires: psychometric evaluation and instructions for use, International Journal of Human – Computer Interaction 7 (1) (1995) 57 – 78.

[17] H.X. Lin, Y.Y. Choong, G. Salvendy, A proposed index of a

usability method for comparing the relative usability of different software systems, Behaviour and Information Technology 16 (4/5) (1997) 267 – 278.

[18] J. Lingerfelt, Technology as a force multiplier, Proceedings of the Conference in Technology Community Policing, National Law Enforcement and Corrections Technology Center. Available: http://www.nlectc.org/txtfiles/confrpt.txt (1997).

[19] B. Miller, Searchable databases help Missouri solve crime, Government Technology 9 (8) (1996) 18 – 19.

[20] L. Pliant, High-technology solutions, The Police Chief 5 (38) (1996) 38– 51.

[21] B. Rocheleau, Evaluating public sector information systems: satisfaction versus impact, Evaluation and Program Planning 16 (1993) 119 – 129.

[22] K. Schellenberg, Police information systems, information practices and individual privacy, Canadian Public Policy— Analyse de Politiques 23 (1) (1997) 23 – 39.

[23] Sierra, Consolidated Criminal History Reporting System, http://www.sierrasys.com/client/success/cchrs.asp (1997).

[24] United States Department of Justice, Uniform Crime Reporting: National Incident-Based Reporting System, Data Collection Guidelines, vol. 1 (1998).

[25] J. Wilcox, IT-armed officers fight gangs, Government Computer News, State and Local 3 (12) (1997) 19 – 20.

![](/api/attachments/JEDZZQUB/fulltext/images/5fa1321c28661c88799405aa67933fda13e73df4eac92d3d14977951fb7c6436.jpg)  
Fig. 6. Case Details. The case details screen provides information regarding the specific case, including location of the crime, the primary officer on the case, details about each person involved in the incident and their arresting information if applicable, and vehicles involved. The officer concludes that this person is indeed a suspect in his case and should be located for interrogation. Using the History Screen on the left panel (far left hand side of the screen shot) and clicking on the Person Details to return to that page, the officer asks for a printout of the home address and a mug shot. Before finishing, the officer saves the history file, providing a log of the automobile theft case search that was conducted during this session.

![](/api/attachments/JEDZZQUB/fulltext/images/888d2b78db1e2b4978779058975fa52c4098ea7d031b28aa0336ee7ff0071b01.jpg)

Dr. Hsinchun Chen is McClelland Professor of Management Information Systems and head of Artificial Intelligence Lab at the Management Information Systems (MIS) Department at the University of Arizona. He received his PhD degree in Information Systems from New York University in 1989. He is author of more than 70 articles covering semantic retrieval, search algorithms, knowledge discovery,

and collaborative computing in leading information technology publications. He serves on the editorial board of Journal of the American Society for Information Science and Decision Support Systems. He is an expert in digital library and knowledge manage ment research whose work has been featured in various scientific and information technologies publications including Science, the New York Times, NCSA Access Magazine, WEBster, and HPCWire. He can be reached at hchen@bpa.arizona.edu.

![](/api/attachments/JEDZZQUB/fulltext/images/e265873c904169fc42eead37e9d0fd0b1b26bbbc1ac8236b1ecf5b2b78516288.jpg)

Lieutenant Jennifer Schroeder has been a member of the Tucson Police Department for 15 1/2 years. She has extensive experience in patrol and tactical assignments as a member of the Service Dog Unit (6 years) and the SWAT team (7 years). She earned her Bachelor of Science in Business Information Systems at the University of Phoenix in 1997, and became a member of the Tucson Police Department’s technology

team while completing her coursework. She is currently pursuing her MS in Management Information Systems at the University of Arizona. Jennifer was the primary author on the COPLINK grant proposal in 1996, and subsequently returned to patrol as a supervisor after her promotion to sergeant in 1997. She became the Project Manager of COPLINK for the Tucson Police Department in February of 1999 and was promoted to the rank of lieutenant in 2001. She is currently a project manager in the Information Services Division at the Tucson Police Department. She can be reached at Jschroe1@ci.tucson.az.us.

![](/api/attachments/JEDZZQUB/fulltext/images/194aa51cd785372121f404c40ff4230577f87343a6dbfe677b95126f7f9569ce.jpg)

Roslin V. Hauck is currently pursuing her doctorate in Management Information Systems at the University of Arizona and has been affiliated with the department since 1997. She received her BS in Communication Studies from Northwestern University (1995) and her Masters in Communication at the University of Arizona (1997). Her research interests include technology adop-

tion, organizational behavior, knowledge management, human – computer interaction, and usability. She can be reached at rrv@bpa.arizona.edu.

Officer Linda Ridgeway entered the Police Academy in 1990 and graduated in December of that year. Officer Ridgeway was a patrol officer for Operations Division Midtown until 1996. She then took a position with the Headquarters Desk. She was instrumental in helping to create a new computer system to track incoming phone calls, reports, and other activity performed by officers in this position. In 1997, she was asked to take a position with the COPLINK project underway within the department. She assisted in the initial design and development of COPLINK. Once Version I was created, she helped in presenting the program to Command Staff of the Tucson Police Department as well as other agencies throughout the state. In July 2000, Officer Ridgeway left the COPLINK project and moved to a position with the City of Tucson Public Safety Academy as an Advanced Officer Training Coordinator. She can be reached at Lridgew1@ci.tucson.az.us.

![](/api/attachments/JEDZZQUB/fulltext/images/59fe45b371cc137401bb62b769286d76d64ed2f9ddc2f5378cc5f84e88c5280b.jpg)

Dr. Homa Atabakhsh is Principal Research Specialist at the University of Arizona MIS department and is Associate Director for the COPLINK Center. She received her BSc, MSc (1984), and PhD (December 1987) degrees in Computer Science from the University of Toulouse in France. She was a Research Scientist at the National Research Council of Canada from 1989 to 1996. She can be reached at homa@bpa.arizona.edu.

Harsh Gupta earned his MS in Management Information Systems from the University of Arizona in 2000, specializing in integrated large database systems, data warehousing and data mining. A former member of the AI Lab, he served as a systems engineer for the COPLINK Project. His research focuses on data migration issues and techniques for large data warehouses. He is currently working as Database Administrator at Microsoft Corp, Redmond WA. He can be reached at gupta<sup>\_</sup>harsh@hotmail.com.

Chris Boarman earned his Masters of Science degree in Management Information Systems in 2000 from the University of Arizona specializing in distributed systems. He is also a former member of the AI Lab serving as a systems engineer for the Coplink Project. His research focused on interoperability solutions for heterogeneous multidatabase systems. He currently is working for Lockheed Martin as a Systems Integrator implementing air traffic control systems. He can be reached at christopherboarman@mail.com.

Kevin Rasmussen completed a Masters of Science degree in Management Information Systems in May, 1999 at the University of Arizona where he was part of the COPLINK development team. He currently works as a Senior Programmer Analyst in the ebusiness group at Intel Corporation (http://www.intel.com) of Santa Clara CA. He can be reached at kevin.rasmussen@intel.com.

Andy W. Clements graduated from the University of Arizona with a Master of Science in Management Information Systems in May 1999. While pursuing his graduate degree, he worked in the UA/ MIS Artificial Intelligence Lab concentrating on Data Warehousing, Internet Agents for Information Retrieval, and Geographic Information Systems. He continues to work on COPLINK (http:// www.coplinkconnect.com) as Senior Software Engineer at Knowledge Computing Corporation (http://www.knowledgecc.com). He can be reached at awclemen@knowledgecc.com.
