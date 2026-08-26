---
otero_id: 24740
otero_key: "RKS22AU2"
title: "Expert Systems and Multimedia: Examining the Potential for Integration"
authors: "William L. Fuerst; James M. Ragusa; Efraim Turban"
year: "1994"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1994.11518054"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Expert Systems and Multimedia: Examining the Potential for Integration

William L. Fuerst, James M. Ragusa & Efraim Turban

To cite this article: William L. Fuerst, James M. Ragusa & Efraim Turban (1994) Expert Systems and Multimedia: Examining the Potential for Integration, Journal of Management Information Systems, 11:3, 155-179, DOI: 10.1080/07421222.1994.11518054

To link to this article: http://dx.doi.org/10.1080/07421222.1994.11518054

![](/api/attachments/RKS22AU2/fulltext/images/bff0c29f723935ac9a00a82bffa2edbd3f2841ce04d57394498bcc7de2581860.jpg)

Published online: 14 Dec 2015.

![](/api/attachments/RKS22AU2/fulltext/images/460d739be1b53dafcaed1acda54bd7d45662da94d6a7536ad70802bcdbd020b0.jpg)

Submit your article to this journal ↗

![](/api/attachments/RKS22AU2/fulltext/images/225f15d2cc7b5405b3afa01f05a5f9425eee45346af78ac13757e3e1e409a8d7.jpg)

View related articles ↗

# Expert Systems and Multimedia: Examining the Potential for Integration

WILLIAM L. FUERST, JAMES M. RAGUSA, AND EFRAIM TURBAN

WILLIAM L. FUERST is an Associate Professor of MIS at Texas A&M University in the College of Business Administration and Graduate School of Business. He is the Director of the Center for the Management of Information Systems and the InfoTech Lab, which specializes in the analysis and innovative use of emerging information technologies. The primary area of focus in InfoTech is multimedia technologies. Dr. Fuerst has published in the MIS Quarterly, Decision Sciences, and the Journal of Information Systems, among other journals. His research interests focus on emerging information technologies, systems development strategies, and MIS planning.

JAMES M. RAGUSA is an Associate Professor of Industrial Engineering in the College of Engineering, University of Central Florida. He is Director of the Intelligent Multimedia Applications Laboratory. Dr. Ragusa's primary research interests are in expert systems, multimedia, and the integration of these technologies. He has held a wide range of government, technical, and managerial positions, and has published in journals such as Heuristics, Expert Systems with Applications, and the Journal of Computer Information Systems.

EFRAIM TURBAN is a Professor of Information Systems in the College of Business at California State University, Long Beach, and is currently a Visiting Professor in the School of Accountancy and Business, Nanyang Technological University, Singapore. Dr. Turban has written fourteen books in information systems, expert systems, and management sciences. He has published extensively in numerous national and international journals, including Journal of Management Information Systems, MIS Quarterly, and Management Science. Dr. Turban's research interests include information technology (with emphasis on the integration of expert systems with other technologies), neural networks, and the management of information systems.

ABSTRACT: Expert systems and multimedia are being incorporated into organizations at increasing rates because, while being independently developed, they possess capabilities appropriate for integration with each other. This paper examines the potential for such integration, providing support to users beyond the capabilities of each independently used technology. An integrated system, essential to the city of Los Angeles during the 1992 riots and the 1994 earthquake, is examined to demonstrate the usefulness and benefits of expert systems and multimedia integration. The potential for this integration is further explored by examining issues related to an integration framework where the two technologies support each other. Three integrated prototype systems are reviewed to promote the legitimacy of expert systems and multimedia integration. Preliminary findings conclude that this integration will offer benefits to various applications.

KEY WORDS AND PHRASES: expert systems, hypermedia, hypertext, information systems applications, multimedia.

THE EMERGING FIELDS OF COMPUTERIZED MULTIMEDIA (MM) and expert systems (ES) are entering their early stages of commercial application. Interesting applications have been developed in each field in the late 1980s and early 1990s. Each offers new opportunities for rethinking operations established in the past. Unfortunately, neither technology has had the expected impact yet. Some businesses have experimented with expert systems but have not totally endorsed the technology, perhaps in part because of the text-based approach of most expert systems. Multimedia is newer, so businesses are just starting to look at the functions that might be supported by this emerging technology. Without some type of built-in decision assistance, however, multimedia applications will probably have a more narrow scope than if such assistance were available. While businesses face the problem of trying to reengineer operations to take advantage of each technology, opportunities for integrating the two systems into a single environment may be overlooked. Such an integrated environment would provide the visual, audio, and graphics support of the multimedia component combined with the advice-rendering and decision-making support in the form of rules and a knowledge base from the expert system component.

Consequently, our purpose here is to explore the potential for the integration of these two technologies. We begin by presenting an actual case of the integrated multimedia and expert system developed for computer problem diagnosis in the city of Los Angeles, no small task for a city of that size with its inherent organizational complexities. The 1992 riots and the 1994 earthquake brought national attention to that city, and the amount of information needed by all public offices during those nightmares was tremendous. The integrated ES/MM system, although not central to supporting riot and earthquake relief efforts, was an important part of the city's infrastructure for assisting those who were attempting to obtain critical information during that time. This example is presented at the beginning of the paper to highlight the potential for integrating expert systems and multimedia, as it provides readers with a point of reference for the subsequent discussion.

After the LA example, we present an ES/MM integration framework that depicts the interaction of these technologies with an application environment. This framework illustrates the potential for ES/MM integration, leading to an environment where these technologies together will support users more fully than either technology can independently. Using the integration framework, the next section presents three prototypes that have integrated expert systems and multimedia technologies and also lists potential application areas. In presenting these prototypes, we focus on the integration aspects, not on the individual technologies. The paper concludes with a discussion of the value provided by ES/MM integration and a statement of future research needs.

An Intelligent Multimedia System for Computer Problem Diagnosis, City of Los Angeles

MOST OF THE LOS ANGELES CITY GOVERNMENT WORKED to its limit in reaction to the May 1992 riot and the major earthquake in January 1994. Thanks to the city's sophisticated computing environment, very few problems were encountered while the huge workload was being managed during those times. This complex, varied environment had been purchased from dozens of vendors and accommodated more than 12,000 workstations [10]. The tremendous demand for computer resources was kept in check by a help-desk where an ES/MM system continued to operate during the riot and the earthquake.

Although this help-desk system does not include the 911 emergency services, it does support many round-the-clock users. The major user groups include the LA Police Department, the LA Fire Department, the city council and the mayor, all PC and AS/400 users in dozens of departments, and those who access the city mainframe. With increased computerization and user sophistication, the city depends on this computing environment. When hardware and software problems arise, the city relies on a complex set of client support groups. Local help-desk units handle minor problems (approximately 10 to 15 percent of the 1,200 monthly requests) for each major user's group. A centralized group, Service Level Management (SLAM), provides diagnostic and resolution support for more complex problems. SLAM handles more than 1,000 requests per month. Problems unresolved by SLAM are referred to vendors or to specialists.

## The Problem

Increasing demand for services, rotation of personnel, and a tight budget had created serious problems for the SLAM staff. In order to provide timely, efficient services to its customers, it had become apparent that increased productivity was the only solution. Expert system technology had been an innovative solution that had proven itself in similar situations $[2, 15]$ . However, initial examination of the expert system solution showed that while ES implementation would alleviate the problem by providing faster problem diagnosis, it would not completely resolve the lack of timely and efficient response to the increased demand. As a result, a 1990 feasibility study indicated that the existing procedures needed to be reengineered to take advantage of an integrated ES/MM system to resolve the SLAM work overload problems.

## The Solution

The integrated system called AWESOME (Automated Workstation Expert System of Maintained Equipment) was developed during 1991 and 1992. As illustrated in figure 1, it combined an expert system with support information, in the form of hypertext, and still video imaging. AWESOME is a PC-based system that aids in all aspects of problem diagnostics, including:

![](/api/attachments/RKS22AU2/fulltext/images/fbc19dcc855b5f405342cf324c2374dbc912f982809f5d71bb0c7188be4eab76.jpg)

## Figure 1.

\- Problem diagnostic advice. Help-desk staff respond to client requests for assistance in determining, for example, why a particular function failed.

\- Access to support information via hypertext capability. Help-desk staff access phone numbers, client departments, and supporting documentation by using the hypertext capability.

\- Help information for computer-related problems. Based on the symptoms provided by the client, the explanation facility of the expert system and the hypertext capability provide “help” screens to assist help-desk staff.

\- Video images and device-specific information for all supported devices. Helpdesk staff are able to access, for example, video image techniques for connecting equipment.

AWESOME makes extensive use of still video images for problem diagnosis, including images of all supported devices, control panels, keyboards, and cable configurations. For example, figure 2 presents a user interface screen, in this case one used for exploring printer problems, where selected icons will provide still video images to address specific problems.

## Benefits and Impact of the System

The single most beneficial aspect of AWESOME has been its diagnostic ability: the average diagnostic time was reduced almost 50 percent, from 15.42 minutes to 8.82

## PRINTER PROBLEM CATEGORIES

![](/api/attachments/RKS22AU2/fulltext/images/8dad198147492f69bed3f9d6cf727b306a4db6052b1b686957231f0c0a83f3cb.jpg)  
Figure 2.

minutes [10]. Another benefit is the significant reduction of time-consuming mistakes. The introduction of this integrated system for computer problem diagnosis has increased the productivity of employees and has greatly improved the manner of troubleshooting. The ability of the SLAM personnel to refer to images in AWESOME has allowed technical specialists quickly and accurately to communicate specific solutions to the variety of client requests. For example, if a client requests assistance with a cabling problem, the SLAM technician accesses images of the cabling connection and describes these images to the client with more speed and accuracy than a technical support manual could provide.

It is likely that a significant organizational change will occur when the help-desk merges with the centralized troubleshooting facility. A more significant change may occur when online clients, with the help of supportive multimedia, perform automated initial diagnosis, thereby eliminating the need for a help-desk and reducing demands for diagnostic services.

## Expert System/Multimedia Integration

THE EXAMPLE PRESENTED ABOVE ILLUSTRATES THE VALUE of integrating multimedia and expert systems, even though each technology is still evolving individually. To examine the value of such integration, this study uses an integration framework for presenting three prototype ES/MM systems to answer an underlying research question: Does the potential exist for integrating expert systems and multimedia technologies where such integration provides more support than a nonintegrated environment? The answer provides insight about the integration of these technologies and their ability to transform or reengineer existing processes into new, innovative, and beneficial processes.

Because the primary focus of this study is on the integration of expert system and multimedia technologies, each should be defined. An expert system is a computer program that replicates the decisions of an expert through the use of heuristics (rules of thumb) and the manipulation of data provided by the user. Multimedia is defined here as the use of multiple media types—audio, video, still images, animation, text, and graphics—all under computer control. In the broadest sense, multimedia allows the delivery of distinct media information in multisensory ways through computer control in a single presentation [37]. Because the intent of this study is to integrate these technologies, not their individual capabilities, no further discussion of individual, specific features and characteristics is presented. Thus, the remainder of this section focuses on examples, benefits, and a framework of ES/MM integration.

## Examples and Benefits of ES/MM Integration

The potential benefits of integrating expert systems and multimedia have been recognized only recently in the literature. Since multimedia is a subset of hypermedia, there are many concepts of hypermedia that also apply to multimedia. Hypermedia is a term to describe multimedia augmented with hypertext functionality—that is, multimedia information linked by association $[4, 6, 17, 23, 30]$ . Coyne $[11]$ believes the ultimate success of hypermedia may be dependent upon expert system technology. He contends that the labor-intensive manual associative linking required by active hypermedia could be performed automatically by an expert system tailored to a specific application domain.

Kimbrough, Pritchett, Bieber, and Bhargava [24] described a system where calculations were linked to expert system-generated explanations for explaining how calculations were performed. Bieber and Kimbrough [7] proposed a generalized hypertext concept where nodes and linkages need not be represented explicitly in the system but, rather, could be inferred or computed at run time from user inputs, attached documents, and declarations describing an application's commands and knowledge structure. Applying this notion to multimedia, an integrated approach can support users through an expert system that provides run-time inferences in the linking of multimedia information.

The merger of expert systems and multimedia, according to others $[8, 32, 43]$ , is valuable for the presentation of expertise. Other researchers $[22, 38]$ have reported that as the number of media presented increases, so does the rate of audience interest, attention, and retention. When multimedia is supported by or combined with an intelligent system, hypothetically the advantages will be even greater. Users might not only be captured by the different media capabilities of such a system, but they might also make more effective use of the information.

According to Sipior and Garrity [39], integrated systems offer an advantage to traditional expert systems users who must translate diagrams of problem attributes and characteristics into text form and then convert again to diagrams when interpreting recommendations. Interactive multimedia designs took away that burden. Ragusa [34] indicated that expert systems become more functional for some applications by incorporating multimedia capabilities.

Research laboratories at Texas Instruments, Rand Corporation, Bell Labs, XEROX Research Center, IBM Research Center, and a few universities have been pursuing the idea of making multimedia more intelligent (that is, integrating multimedia and expert systems), as the following examples illustrate. Burger and Marshall [9] described a prototype that reasons in detail about the meaning of user input before intelligently choosing among the media alternatives for the appropriate presentation. An expert system combined with a natural language processor supporting multimedia presentations has been developed by Wahlster, Graf, and Rist [44], where graphics and text are guided by an embedded expert system knowledge base. MacNeil [29] developed a case-based reasoning system to capture and reuse knowledge about the design of multimedia presentations. Thompson [40] described a hypothetical claims processing system in which a workflow process could be modified using knowledge-based rules to classify and route a scanned transaction, seeking a more balanced and efficient workflow.

Navigating a linked multimedia system may not be efficient, especially since users normally do not have any systematic procedure for navigation $[42]$ . By merging expert systems and multimedia, navigation can be guided so that an effective and efficient use of the system is achieved. Options can be evaluated by the expert system, allowing a navigational approach that will intelligently support the user's requests. This support assures the access of all critical knowledge. For example, Bieber $[6]$ described a system where an expert system provides a hypermedia-style interface for navigating among decision support models, data, and reports.

From the examples and benefits above, it appears the potential for expert systems and multimedia integration is significant. To explore that potential, an integration framework was developed.

## ES/MM Integration Framework

Figure 3 presents the ES/MM integration framework utilized in this study. This framework includes three different environments: technical, application, and integrated. The technical environment consists of various expert system and multimedia components, while the application environment consists of the domain-specific problems and tasks. The focus of the framework is the environment where the value of the integration is manifested, that is, where the integration has the potential to provide more value than could have been attained through existing means or through individual use of either technology. With this focus on integration, the factors included in the framework are limited to those relating to both expert systems and multimedia. $^{1}$ The remainder of this section is devoted to discussing those factors pertinent to the environments—technical, application, and integrated—shown in figure 3.

The basis for the expert system component in the technical environment was derived from Turban's [41] structure of an expert system. Four components of an expert system—source of knowledge, knowledge base, user interface, and explanation facility—were selected from the Turban structure where multimedia can enhance the capability of the expert system.

Technical Environment  
![](/api/attachments/RKS22AU2/fulltext/images/ab285e5303d2e9b84bae82f84c711b33ecc533512a2c729d3e2db59b7ec2f9a9.jpg)  
Figure 3.

The primary sources of knowledge for an expert system are people and existing documentation, including CD-ROM [12], still images, real-time video, voice, and text. Also, multimedia has been used to support knowledge acquisition through the use of multimedia tools to train in knowledge acquisition (for example, KRATT [27]) and to explore documented knowledge. Other attempts [16, 26] have been made to support knowledge acquisition where multimedia either provides rich knowledge sources or facilitates the acquisition process.

Traditionally, acquired knowledge is represented in expert systems as rules or facts in a knowledge base. However, with new ES/MM integrated systems, various media types are also used to represent knowledge, allowing the multisensory capability to enhance the communication of this knowledge [37]. For example, Hillman [18] described knowledge diagramming where the knowledge is represented by a top-down graphical description.

In most expert systems, the user interface is accomplished via a keyboard, with the system asking questions or presenting menus and the user providing answers. Multimedia can enhance this dialogue. Especially when complex tasks are involved, communication can be greatly enhanced if the expert system is supported by video, pictures, diagrams, or animation. For example, Abu-Hakima [3] presented a system, used primarily for equipment diagnostics, where the user interface included template-based text, graphics, and icons. A similar system is being prototyped by the U.S. Post Office where employees of new, complex letter-sorting equipment use an expert system supported by a linked multimedia interface as a guide for the operation and maintenance of the equipment. In the future, as voice recognition systems become more effective and economical, audio capabilities will become even more prevalent.

Multimedia also supports the explanation facilities of expert systems by providing improved explanations that may include video or audio presentations of underlying expert system logic, supporting graphs (trend lines), display of pictures (still and motion), or graphical comparisons of alternatives. For example, Mao, Dhaliwal, and Benbasat [28] presented a system, called Hyper-FINALYZER, which allows reasoning traces and deep explanations using graphical browsers to represent relationships between the analysis and the structure of the domain knowledge.

The multimedia element in the technical environment consists of four major components: media types, sources of content material, user interface, and linkages among the stored material and the interfacing component $[7, 37, 45]$ . Notice that user interface is common to both the expert system and the multimedia technologies. The media types, also referred to as media forms or data types, consist of audio, video, text, graphics, still images, and animation. Content material sources (similar to expert knowledge sources) take the form of existing material such as videotape and still images, or they may be originally created for use in the multimedia application. Linkages between the actual stored media and the user interface component normally take the form of indexes or hypertext, allowing for nonlinear $^{2}$ access and presentation.

A factor relevant to both the expert system and the multimedia environments is whether the tools in those environments support integration with the other. At this time, capabilities in both environments need further development for such integration. Authoring systems used in multimedia development do not easily allow expert systems to be included. Even in those authoring systems that allow scripting, integration with expert systems is difficult. The expert system environment does a better job of allowing for integration with multimedia, probably because of the command level of instruction utilized in expert system shells. This is still a limited capability, however, and these limitations are addressed again in the concluding section.

The application environment has two major components (problem/opportunity and task characteristics) that are important considerations in the development of ES/MM. Along with multimedia, an ES/MM integrated system contains a knowledge base as a component of the expert system. Because the knowledge is domain-specific, the expert system's ability to represent the application is dependent upon the characteristics of the task to be accomplished within that domain. Research has been conducted to determine the type of task characteristics appropriate for individual expert systems [1, 25] and for individual multimedia systems [31]. Focusing on task definition and bounding, Laufman et al. [25] stated that tasks suitable as candidates for expert system development are those that are unambiguous, well bounded, narrowly defined, independent from other tasks, and decomposable within a domain. Isakowitz [20] included the task perspective as a critical component for developing organizational hypermedia systems, which would also apply to multimedia systems. Since this component of the application environment is critical when deciding whether an integrated system is appropriate, the specific task characteristics of the prototypes are addressed in the following section.

All of these various components from the multimedia, expert systems, and application environments come together in the integrated environment. This final component of the integration framework (figure 3) is one where the expert system and multimedia technologies provide more support than either technology alone. The factors included in the integrated environment in figure 3 evaluate whether such integration is appropriate in a given situation, and they are presented in the following discussion.

## Appropriateness Factors

As stated above, the characteristics of the task are of major importance. However, there are additional factors that must be considered in determining whether an integrated system is appropriate, including the need for multisensory approaches and realism, the variety of presentation modes, the goal of the communication, the amount of change in the problem domain, and a range of practical issues.

Regarding the multisensory nature of an integrated ES/MM environment, two important concepts need to be considered: cognitive and affective domains. These concepts relate to communication that either is text-based or uses a multisensory approach. An integrated ES/MM may be overkill if text-based communication invokes the desired cognitive result. In other cases, however, a multisensory approach may be necessary to affect a desired outcome (for example, learning).

Realism is an important factor when trying to determine the appropriateness of an integrated environment. Two examples illustrate this point. First, as a training tool for hostage negotiations, multiple data types such as video and audio provide more realistic scenarios than a text-based approach. Second, additional data types provide an environment for training employees to use particular types of equipment, which might range from assembly-line machines to jet airplanes.

Research on presentation modes has been conducted in recent years $[13, 21, 33]$ . A common research approach compares text-based presentations with alternative formats such as graphics and video. The findings support the value of a nontext-based approach, and suggest that there is value in the use of additional data types.

Establishing the goal(s) of the communication is necessary to determine the appropriateness of an integrated system. These goals include the system's ability to persuade, instruct, grab attention, or solve problems. For instance, if the goal of a communication is simply to provide an answer to a quantitatively expressed problem, the cost of developing an integrated system may not be justified; but if the goal is to persuade or to grab attention, such integration may be appropriate.

Another factor is the degree of change in the problem domain. If the rules for an expert system change often, or if the various data types in the multimedia component frequently become outdated, then an integrated approach may not be appropriate due to the regular maintenance required to update the rules or data. Therefore, the stability of the problem domain must be considered in order to determine the appropriateness of an ES/MM integrated system.

There are several practical issues $^{3}$ relating to the appropriateness of an integrated environment. First, should the system be developed from scratch or merely enhanced from an existing system? The answer depends upon the original development of the system. Developed either as an expert system or as a multimedia system, it could probably be enhanced to include the other technology. Yet, if bringing in the other technology results in a considerably different system, is it considered enhancement or new development? The answer is really a matter of degree.

Another issue concerns the most appropriate types of information systems to be enhanced to the level of an integrated ES/MM environment. Generally, a system currently using expert system or multimedia capabilities would be a likely candidate. Taking a system with one of these technologies and incorporating the other is not as big a step as taking a system totally unrelated to either technology and trying to incorporate both ES and MM. In that sense, traditional types of management information systems and transaction processing systems are probably not good candidates for ES/MM integration at this time, although they provide data that certain types of ES/MM systems could use. Since the direction of the computer industry in general is toward more multiple media capabilities, it is quite possible that components of management information systems will involve ES/MM integration, at least at the level of the user interface. Decision support systems and executive information systems are more likely candidates for the inclusion of ES/MM capabilities at this time.

## Costs of Integration

On the surface, the cost of developing an integrated ES/MM system would seem to exceed the cost of developing a one-technology system. That would be true in most cases, unless developers take steps to limit the technologies of an integrated system as compared with a one-technology system. Obviously, looking only at the cost is incomplete because a careful evaluation of the benefits is necessary to determine if the integrated system is cost-effective, with anticipated benefits exceeding anticipated costs. This evaluation may seem straightforward, but because both technologies are fairly new, there is little history to help estimate the expense of developing an integrated system. Similarly, the benefits in some cases are determined in a straightforward manner (for example, the savings that would result from using a kiosk instead of hiring additional staff for a public display), while in other cases this would be more difficult (determining the revenue produced from the kiosk). It is obvious that these cost considerations must be addressed before determining the appropriateness of an integrated system.

## Performance Results

Developers will have to look at the expected performance results to determine the benefits of integrated systems. As in most cases where developing systems must be justified, these performance results are classified as tangible and intangible benefits. Quantifying the benefits of an integrated system should provide a better picture of whether to undertake the development; however, intangible benefits may round out the argument for such development. Examples of performance results include reduced time for troubleshooting problems, increased sales rates, better utilization of personnel (for example, selling), as well as greater accuracy and more effective communication in the response to user requests for information.

## Organizational Impact

The organizational impact of an integrated system is related to potential benefits. Los Angeles' AWESOME system provides examples of these benefits. First, fewer support staff are needed to service requests because the integrated system is a more efficient troubleshooting device. Second, the future organizational structure of the computer support group will be affected if the integrated system provides automated support. Staff reduction and functional reorganization are types of impact created by an integrated system and must be considered when determining the appropriateness of the integrated environment.

All of the factors presented above are included in the integration framework and are used in the analysis of the three prototypes discussed below.

## Integrated ES/MM Applications

AS THE PREVIOUS SECTION DEMONSTRATED, THERE IS CONSIDERABLE POTENTIAL for integrating expert systems and multimedia. Although such integration is still in its infancy, some prototypes today exemplify the available potential when these technologies are combined. This section presents three such prototypes that provide integration of expert systems and multimedia.

Because the potential for integration has been realized only recently, a strictly controlled experimental analysis was not feasible. For that reason, a qualitative methodology was chosen in order to explore that potential and to present these emerging technologies in operation, to show the impact that integration might have on the host organizations. This approach is consistent with an idiographic procedure $[14]$ where a phenomenon is studied in its context. The means for collecting the data were personal observation and experience with the systems, interviews with key personnel, and review of existing documentation. The use of multiple means for data collection provided a richer approach than would have been provided by a single data-collection method $[5]$ .

The prototypes presented in this analysis are (1) an intelligent visual database management system for NASA, (2) a marketing sales system for the Convention/Civic

Center located in Orange County, Florida, and (3) a property appraisal and resale support system. These systems were selected because the researchers worked with the development of some aspect of the system or because information was available through personal contact. In addition to these systems, this section provides a listing of other applications with potential for future development.

All these prototypes have task characteristics that make them appropriate candidates for integrated systems. The characteristics are lack of ambiguity, including ability to deal with specific, well-bounded, narrowly defined problem domains; independence from other tasks; decomposability into identifiable modules, which will facilitate development and delivery; and problem domains where visualization is important. These prototypes represent appropriate applications for systems utilizing both expert systems and multimedia capabilities.

Table 1 summarizes these prototypes as well as the Los Angeles computer problem diagnostic system, all based on the ES/MM integration framework. The review of each prototype describes the environment prior to integration. By taking advantage of the integrated system, the reengineered application will provide benefits not available in the existing environment. The discussion illustrates the variety of applications, media, users, results, and organizational impacts possible with ES/MM integration.

## Intelligent Visual Database Management System for NASA

The thrust of the intelligent visual database management system for NASA [35, 36] is directed toward the feasibility of intelligent and direct interfacing between an expert system and a large, high-resolution color image database. The target application was an integrated system for the collection, classification, storage, retrieval, and transmission of NASA Space Shuttle Program close-out photography (more than 150,000 images). These pictures, “shuttle close-out photographs,” document all significant flight-preparation processing and modification activities for quality control and assurance. Key elements of the space shuttle included the orbiter, external tank, and solid rocket boosters.

The present system combines expert system development software (LEVEL5 OBJECT), compressed digital imagery, and a point-and-click, object-oriented user interface. While presently designed for still image and alpha-numeric data, the prototype system could be expanded to include hypertext and digital video technology for storing motion video.

The role of the expert system is to provide knowledge-based classification and retrieval assistance for image management and to interface with image records and the mass storage device. The expert system provides support for the heuristics for image classification and retrieval tasks that have been developed by specialists over the years but that are not commonly known or documented. Experienced classification specialists have learned to recognize which objects in technically oriented space shuttle subsystem images are important and which are not. Experienced retrieval specialists also have developed an understanding of the logical sequence that systems engineers and quality technicians use to locate required images. This knowledge is

Downloaded by [University of Pennsylvania] at 16:40 18 April 2016

<table><tr><td></td><td>LA&#x27;s Computer Support and Diagnostic System</td><td>NASA&#x27;s Intelligent Visual Data Base System</td><td>Orange Co. Convention Center Marketing System</td><td>Property Appraisal and Resale Support System</td></tr><tr><td colspan="5">ES environment</td></tr><tr><td>Expert knowledge source</td><td>Computer and functional specialists; documentation</td><td>Classification and retrieval specialists</td><td>Convention center specialists; documentation</td><td>Commercial real estate and financial specialists</td></tr><tr><td>Knowledge base</td><td>ES rules concerning computer specifications</td><td>ES rules concerning classification and retrieval</td><td>ES production rules concerning resources of facility</td><td>ES knowledge base of physical characteristics of properties</td></tr><tr><td>User interface</td><td>Graphical user interface</td><td>Object-oriented interface</td><td>Graphical user interface</td><td>Graphical user interface</td></tr><tr><td>Explanation facility</td><td>Text and photos of computer equipment</td><td>Text identifying photos retrieved</td><td>Text, illustrations, and image displays of facilities</td><td>Text and graphics explaining classification of properties</td></tr><tr><td colspan="5">MM environment</td></tr><tr><td>Media types</td><td>Still video images and text</td><td>Still images and text</td><td>Still images; text, graphics</td><td>Still images, video; graphics; text</td></tr><tr><td>Content sources</td><td>Photography obtained from vendors</td><td>Photography taken during space shuttle processing</td><td>Photography of facilities; graphics created for system</td><td>Photography of properties; text/graphics created for system</td></tr><tr><td>Linkages</td><td>Hypertext</td><td>Hypertext</td><td>Hypertext</td><td>Indexes</td></tr></table>

Table 1 Attributes of Selected Systems

Downloaded by [University of Pennsylvania] at 16:40 18 April 2016  
Application environment

<table><tr><td>Problem/opportunity</td><td>Inefficiencies in trouble-shooting over 1,000 calls/month</td><td>Inefficiencies in handling large image database</td><td>Inefficiencies in selling effort; better way to sell space</td><td>Inefficiencies in classifying; better way of selling properties</td></tr><tr><td>Task characteristics</td><td>Labor-intensive and often frustrating communication between technicians and users</td><td>Labor-intensive searching for and retrieval of specific images</td><td>Labor-intensive selling and configuring of convention center facilities</td><td>Labor-intensive selling effort and classification of repossessed properties</td></tr><tr><td></td><td colspan="4">ES/MM integration</td></tr><tr><td>System description</td><td>Computer problem diagnosis</td><td>Classification and retrieval of space shuttle images</td><td>Marketing of convention center facilities</td><td>Classification and resale of repossessed real estate</td></tr><tr><td>Development tool</td><td>1st Class HT</td><td>LEVEL5 OBJECT</td><td>VP-Export and C++</td><td>EXSYS and Authorware</td></tr><tr><td>User community</td><td>Computer help-desk technicians</td><td>Launch processing, engineering, and quality specialists</td><td>Sales agents; customers</td><td>Sales agents; customers</td></tr><tr><td>Performance measures</td><td>Troubleshooting time; accuracy of diagnosis</td><td>Access to images related to input requests</td><td>Sales rates; utilization rates of facilities</td><td>Sales rates; property turnover; accuracy of appraisals</td></tr><tr><td>Performance results</td><td>Reduction of average time per call from 15.42 to 8.82 minutes; greater accuracy</td><td>Drastic reduction in time for display of images requested and in system costs</td><td>Increased sales and faster turnover due to visualization and financing/appraising support</td><td>Increased sales and faster turnover due to visualization and financing/appraising support</td></tr><tr><td>Organizational impact</td><td>Reduction in help desk staff, with potential for elimination of help desk</td><td>Reduction in staff for retrieval tasks; more time available for analysis tasks</td><td>More specialized selling efforts; better customer service</td><td>Direct access by customers; focused selling efforts</td></tr></table>

![](/api/attachments/RKS22AU2/fulltext/images/bf88b9f95887085268e71cb3597643d09bf6199b250ceec9a345822791cd0475.jpg)  
Figure 4.

not possessed by less experienced or newly hired classifiers or retrievers, and can be provided by the expert system. Figure 4 presents a diagram of the various levels of screen detail used by the expert system in classifying and retrieving images.

The manual retrieval of specific images is lengthy (about 3,000 images per launch with more than 61 launches). When the Challenger exploded shortly after launch, the analysis of the problem took several months. This was partly because of the manual search time required to collect images of the suspected, and later confirmed, faulty O-rings. Reengineering the system to incorporate an integrated ES/MM environment will provide value in terms of more efficient and effective performance. The ES/MM system will allow huge time savings, guide users to certain potential problem areas because of classification and retrieval support (expert systems), and allow easy access to visual supporting evidence (multimedia). Such value could not have been obtained without the integration of expert system and multimedia technologies. In addition, the ES/MM system may have other organizational impact because time reductions and easy access may allow NASA to redistribute some workforce effort to analyze functions rather than engage in search and retrieval activities.

## A Convention Center Marketing Expert System

The Orange County Convention/Civic Center Marketing Expert System (MES) prototype has demonstrated the advantages of combining expert systems and multimedia technologies for a marketing and sales application [19]. The convention center's sales staff has been limited to personal contact and printed material; however, reengineering their approach to include an integrated system has the potential to improve staff productivity at trade shows and sales blitzes. One purpose of the system is to get the client's attention long enough to distinguish their product from the competition. The stimulus of an expert system linked to a multimedia platform creates that attraction.

The expert system provides a front-end user interface to a knowledge-base of 125 production rules (heuristics about facility resources and optimum uses) and multimedia (text and images) for determining the best mix of facilities and services for prospective convention center clients. The expert system gathers general client information, including mailing address and phone number, as well as specific information concerning the prospective event, including possible dates and anticipated needs related to space, catering, electrical power, seating arrangements, breakout rooms, and setup services. From this input, the system accesses images to display the facilities of the convention center and to illustrate some different layout alternatives based on the user requirements. These images are accessed from a laser disk, which stores color images of overall views of the center (outside and inside), exhibit halls, meeting rooms, and banquet areas (actual views and layout drawings).

This marketing prototype uses an expert system development tool (VP-Expert) for the inference engine, relational database software for data storage, and a C++ software interface to a Write Once, Read Many (WORM) optical laser disk system. In the future, the expert system, user-intelligent query and advisement front end will be expanded to include an increased set of multimedia, which will encompass computer-generated graphics (exhibit setup and layout possibilities), video and audio (a greeting by the convention center director and events in progress), and additional text (contract provisions, food service menus, electrical service capabilities, and loading/unloading/shipping instructions). Advantages of this system include ease of use, better match of resources and client needs, interesting visual displays, and improved performance of less experienced convention center staff.

The applicable performance measures are the impact on sales and the responsiveness of the system to client requests. The value of the ES/MM integrated system lies in its ability to provide better levels of service by guiding clients through the presentation with suggestions of alternative facility and service configurations. The integration of

ES/MM technologies seems to be an ideal mechanism for reaching clients in this situation. The organizational impact is that sales staff will be able to provide a higher level of service through specialized selling approaches, as well as changing the way in which the staff will interact with clients in promoting the facilities of the convention center.

## A Property Appraisal and Resale Support System

Public agencies such as the Federal Depositor's Insurance Company (FDIC) and Resolution Trust Company (RTC), as well as private mortgage and lending companies, provide an appropriate application environment for integrating expert systems and multimedia. The prototype PARESS (Property Appraisal and Resale Support System) provides sales support for commercial real estate agents. This prototype, developed in EXSYS and Authorware software, was developed as a reengineered approach to the traditional real estate sales method of relying on printed descriptions to interest clients before scheduling on-site visits. With the large dollar amounts typically involved in commercial real estate sales, the integrated system is economically feasible and makes sales efforts more effective and efficient. Figure 5 presents a gray-scale representation (the system uses color screens) of a screen used to request information in multimedia formats about a property that possesses the preferred user specifications as classified by the expert system. This classification is explained below.

The expert system area of PARESS is a knowledge-based facility for supporting the property sales function. Input parameters from clients include the desired location, square footage, access to traffic patterns, number of rentable units, state of repair, construction materials (like roofing, facades, and interior walls), and infrastructure technology (like telecommunications cabling and electrical power supplies). Each of these input items is evaluated against a stored knowledge base to receive a rating that contributes to the overall classification of a selected property's ability to meet the client's needs. Future enhancements to the system will include another expert system capability that will assist agents with financing details and appraisals of available properties.

The multimedia area of PARESS combines still images, video, and textual material to present the property to clients. By using multimedia, more vivid views of the property are available through multiple views of the exterior and the interior. Still images provide detailed observations where users initiate “hot points” on the image and receive specific textual descriptions.

Performance measures for this system include response times, sales and turnover rates, and accuracy of appraisals. Increased sales are the ultimate goal. Over time, the system could be available to clients either directly on site and, to a limited extent, through remote access. Some of the technological constraints with telecommunications will have to be resolved before large multimedia files, particularly real-time videos, can be effectively sent to remote locations; however, progress that is underway with ISDN and other telecommunications facilities indicate that remote access of systems such as PARESS will be feasible.

Downloaded by [University of Pennsylvania] at 16:40 18 April 2016

![](/api/attachments/RKS22AU2/fulltext/images/7f5acf40f68263dc1d3d500c29ba10116f792128ba9f616c0f98e11e4d05876c.jpg)

The value of this integrated system is its unique combination of the expert system and the multimedia capabilities. Video showing real estate properties in a multiple-listing service has already been prototyped, but expert system features have not been included. In PARESS, support is provided beyond the presentation of video or the still images of real estate properties because the system classifies properties based on the user's needs and specifications, providing for a more efficient and effective search of properties.

## Promising Application Areas

Other interesting applications are under development in many organizations. Several companies (Electric Power Research Institute, Competitive Solutions, Inc., and Texas Instruments) are undertaking projects to incorporate expert systems and multimedia technologies. Proprietary in nature, these systems are still in the developmental stage and public information is limited. However, available information indicates these applications integrate expert systems and multimedia in order to provide targeted users with support not available in the current environment. Also, additional application areas are ripe for developing integrated ES/MM systems. Table 2, adapted from [36], presents a representative list of these areas.

## Conclusions

DOES THE POTENTIAL EXIST FOR INTEGRATED EXPERT SYSTEMS and multimedia technologies to provide users with a higher level of support than either technology could provide individually? From the presentation above, the answer is clearly yes. Implemented systems such as Los Angeles' AWESOME illustrate the value of this integration. This presentation of application areas where expert systems and multimedia technologies are able to support each other also demonstrates the potential for integration and the power of such a system; moreover, these prototypes confirm this potential. The performance results of these prototypes could motivate organizations to review opportunities for creating ES/MM integrated solutions.

As organizations evaluate their current operations, they may find it appropriate to reengineer selected processes to include integrated expert systems and multimedia technologies. The integrated environment component of figure 3 presented several factors that must be assessed in order to determine the appropriateness of an integrated system. These included the task characteristics, the need for multisensory capabilities, the ability to incorporate multiple media types and expert systems knowledge, the need for realism, the persuasive, instructive, and attention-grabbing nature of the communication, the amount of change in the media types and the knowledge rules, and several practical issues.

The value that ES/MM integration is able to provide to organizations has also been illustrated. This value consists of a new level of support that could not have been obtained by using traditional information system approaches or by using either technology alone. The three prototypes illustrated the value of integration in terms of effectiveness and efficiencies obtained as a result of improved communication, reduction or redistribution of work force, improved response times, and greater accuracy.

Table 2 Representative Potential Integrated Applications (adapted from [36])

<table><tr><td colspan="2">Consumer services</td></tr><tr><td>Senior center adviser</td><td>Real estate adviser</td></tr><tr><td>Car buying visual adviser</td><td>Video games</td></tr><tr><td>Home/car self repair</td><td>Plant care adviser</td></tr><tr><td>Banking service adviser</td><td>Interior design adviser</td></tr><tr><td colspan="2">Travel, tourism, and recreation</td></tr><tr><td>Vacation selection</td><td>Hotel/restaurant selector</td></tr><tr><td>Recreation/camping adviser</td><td>Map/route guide</td></tr><tr><td>Entertainment/attraction adviser</td><td>Golf course selector</td></tr><tr><td colspan="2">Law enforcement</td></tr><tr><td>Mug shot identification</td><td>Vehicle identification</td></tr><tr><td>Accident/crime presentation</td><td>Crime site/victim records</td></tr><tr><td>Prison inmate education</td><td>Evidence inventory</td></tr><tr><td colspan="2">Human resources</td></tr><tr><td>Employee orientation</td><td>Skills training</td></tr><tr><td>Loss prevention training</td><td>Management development</td></tr><tr><td>Company orientation</td><td>Customer orientation</td></tr><tr><td colspan="2">Marketing</td></tr><tr><td>Product identification</td><td>Electronic catalogs</td></tr><tr><td>Customer/dealer information</td><td>Sales presentations</td></tr><tr><td>Convention center selection</td><td>Distribution adviser</td></tr><tr><td colspan="2">Education and training</td></tr><tr><td>Intelligent computer-aided instruction</td><td>Teacher preparation/certification</td></tr><tr><td>AIDS/sex education</td><td>Science/math education</td></tr><tr><td>Art/literature education</td><td>Adult literacy education</td></tr><tr><td>Medical/paramedic training</td><td>Language training</td></tr><tr><td>Simulator training</td><td>Customer service training</td></tr><tr><td colspan="2">Other</td></tr><tr><td>Document/visuals storage and retrieval</td><td>Architectural/landscape design assistance</td></tr><tr><td>Accounting reference storage and retrieval</td><td>Engineering/scientific system displays</td></tr><tr><td>Urban planning</td><td>Real estate selection</td></tr></table>

As companies evaluate existing application environments, inefficiencies will be uncovered that will prompt the reengineering of certain operations. Some specific examples of these inefficiencies include an overloaded sales staff using the traditional, printed brochures for selling, a text-based training program, a high turnover of skilled personnel in training or troubleshooting functions, an individual who is the source of expertise and who is often unavailable, or a collection of numerous images that must be accessed often and quickly. These examples are a few of the types of inefficiencies that will drive organizations to reevaluate their tasks. If these inefficiencies are costly, reengineering the operations for an integrated ES/MM may be beneficial. Since the development of such systems will be costly, however, the inefficiencies must be significant enough to warrant the expense of ES/MM system development.

The integration of these technologies results in benefits beyond those provided by either one of the technologies used individually. As businesses think about reengineering, numerous organizational applications will become candidates for ES/MM integration. Companies may be pushed to a point where they need to repair some inherent operational deficiency, or they may be pulled by these technologies to the point where the ES/MM integration provides a better way of doing business.

Yet, a considerable hurdle remains. Better tools are needed to develop the linkages between the technologies. At this time, expert system shells and multimedia authoring systems are not readily able to be integrated, thereby requiring highly skilled developers to accomplish the integration. When considering which of these technologies could more readily incorporate the other, expert systems software probably is closer to the development of such potential. ES shells have been around longer and many have already gone through enough major revisions to refine specific capabilities. Because the nature of the shells is more command-language-oriented, the links to MM may more likely be the next major release capability. That is not to say that expert system shells have to be all-inclusive by providing the software to perform all the functions of the expert system and the multimedia. Even multimedia authoring systems do not provide all the capabilities of entering and editing the data types. For instance, Adobe's Photoshop provides input and edit capabilities for images while the access to these images is accomplished by an authoring system such as Macromedia's Authorware or Asymetrix's Toolbox. The key element is the ability to link to an external resource (such as images and video) in a seamless manner. Until these capabilities are available, the developer will be spending considerable time completing that task.

The integration of expert systems and multimedia has the potential to produce innovative applications with great appeal. With the increased sophistication, complexity, and number of data types (motion and still imagery, graphics, text, audio, and animation), organizations will seek efficient and flexible ways to incorporate this technology into specific environments. Intelligent multimedia systems will be developed to enable efficient, effective interaction with varying types of complex applications, gaining support from the knowledge-based reasoning capabilities of expert systems as well as visual and audio support from multimedia.

Hand in hand with potential, though, comes the need for further research about the application of these integrated systems. As these technologies continue to develop individually, their integration must also be developed in terms of effective ways to apply the integration within organizational settings. Among the issues to be studied are several that seem fruitful for continued research, including an investigation of the modes of integration (tight versus loose), the development of an appropriate cost/benefit analysis framework for justification of such systems, an investigation of the effect of intelligent multimedia systems on factors such as decision quality, user receptivity, retention rates, and usability features, an analysis of the personnel skills required to develop systems in this integrated environment, and the determination of appropriate architectures for typical intelligent multimedia applications. Further research is needed to identify situational factors in the application environment to determine if there are specific cause-effect relationships leading to the successful development and use of ES/MM integrated systems.

When more is known about these and related research topics, and with the projected increased capabilities and reduced costs of both multimedia and expert systems, it is reasonable to expect that integrated ES/MM systems will be appropriate for many practical applications.

## NOTES

1. Technical issues such as data compression/decompression, storage mechanisms, and image transmission systems are not included in the framework because they support the individual technologies, not their integration. Clearly, these technical issues are important for the further development of each technology even though their consideration is beyond the scope of this study.

2. Nonlinear refers to the linking of components in the system in a nonsequential fashion, allowing users to control the navigational flow to any component that has been previously indexed.

3. Some of these practical issues relate to technical details that change rapidly as newer technologies emerge. Since they are ever-changing, they are not included in detail in this paper.

## REFERENCES

1. Abdolmohammadi, M.J., and Bazaz, M.S. Identification of tasks for expert systems development in auditing. Expert Systems with Applications, 3 (1991), 99–107.

2. Abraham, D.M.; Spangler, W.E.; and May, J.H. Expertech: issues in the design and development of an intelligent help desk system. Expert Systems with Applications, 2, 4 (1991), 305–319.

3. Abu-Hakima, S. Generating hypermedia explanations. Proceedings of the Ninth National Conference on Artificial Intelligence (AAAI-91): Workshop Notes on Intelligent Multimedia Interfaces. Anaheim, CA, July 15, 1991, pp. 63–68.

4. Akscyn, R.M.; McCracken, D.L.; and Yoder, E.A. KMS: a distributed hypermedia system for managing knowledge in organizations. Communications of the ACM, 31, 7 (July 1988), 820–835.

5. Benbasat, I.; Goldstein, D.; and Mead, M. The case research strategy in studies of information systems. MIS Quarterly, 11, 3 (September 1987), 369–386.

6. Bieber, M. Automating hypermedia for decision support. Hypermedia, 4, 2 (1992), 83–110.

7. Bieber, M., and Kimbrough, S. On generalizing the concept of hypertext. MIS Quarterly, 16, 1 (March 1992), 77–93.

8. Bielawski, L., and Lewand, R. Intelligent Systems Design: Integrating Expert Systems, Hypermedia, and Database Technologies. New York: Wiley, 1991.

9. Burger, J.D., and Marshall, R.J. Aimi: an intelligent multimedia interface. Proceedings of the Ninth National Conference on Artificial Intelligence (AAAI-91): Workshop Notes on Intelligent Multimedia Interfaces. Anaheim, CA, July 15, 1991, pp. 23–28.

10. Clarke, D.E.; Turban, E.; and Wang, P. An integrated expert system/multimedia for troubleshooting of computer hardware at the city of Los Angeles. Expert Systems with Applications, 7, 3 (1994), 441–449.

11. Coyne, J. The importance of expert systems in a hypermedia environment. Proceedings of the IEEE Conference on Managing Expert System Programs and Projects. Bethesda, MD, September 1990, pp. 205–208.

12. Dean, R.P. SPECSystem: a knowledge-based system on CD-ROM. PC AI, 6, 6 (November–December 1992), 36–38.

13. DeSanctis, G. Computer graphics as decision aids: direction for research. Decision Sciences, 5 (1984), 463–487.

14. Franz, C.R., and Robey, D. An investigation of user-led system design: rational and political perspectives. Communications of the ACM, 27 (1984), 1202–1209.

15. Ford, B. An expert diagnostic system using multimedia. Expert Systems: Planning, Implementation, Integration, 2, 3 (Fall 1990), 19–24.

16. Gaines, B.R., and Linster, M. Integrating a knowledge acquisition tool, expert system shell, and a hypermedia system. International Journal of Expert Systems, 3, 2 (1990), 105–129.

17. Haan, B.J.; Kahn, P.; Riley, V.A.; Coombs, J.H.; and Meyrowitz, N.K. IRIS hypermedia services. Communications of the ACM, 35, 1 (January 1992), 36–51.

18. Hillman, D. Bridging acquisition and representation. AI Expert, 3, 4 (November 1988), 38–46.

19. Hofferd, T.; Roulston, M.; McGuire, B.; and Shoemaker, K. Orange County Convention/Civic Center Marketing Expert System (M.E.S.). Working paper, University of Central Florida, Intelligent Multimedia Applications Laboratory, Orlando, 1993.

20. Isakowitz, T. Hypermedia, information systems, and organizations: a research agenda. Proceedings of the Twenty-Sixth Annual Hawaii International Conference on Systems Sciences, January 1993, pp. 361–369.

21. Jarvenpaa, S.L. The effect of task demands and graphical format on information systems. Management Science, 35, 3 (1989), 285–303.

22. Johnson, V. Picture-perfect presentations. Training and Development Journal, 43, 5 (May 1989), 45–47.

23. Karr, R.A. The executive information application-intermedia goes to work. PC AI, 6, 6 (November–December 1992), 34–35.

24. Kimbrough, S.O.; Pritchett, C.; Bieber, M.; and Bhargava, H. The Coast Guard's KSS project. Interfaces, 20, 6 (1990), 5–16.

25. Laufman, S.C.; DeVaney, D.M.; and Whiting, M.A. A methodology for evaluating KBS applications. IEEE Expert (December 1990), 43–61.

26. Lee, J.K.; Lee, I.K.; Choi, H.R.; and Ahn, S.M. Automatic rule generation by the transformation of expert's diagram: LIFT. International Journal of Man–Machine Studies (1990), 275–292.

27. Liebowitz, J., and Bland, K. KARTT: a multimedia tool that builds knowledge acquisition skills. PC AI, 6, 6 (November–December 1992), 28–30.

28. Mao, J.; Dhaliwal, J.S.; and Benbasat, I. The use of hypertext to provide explanations in knowledge-based systems: a conceptual model and implementation. Proceedings of the 27th Hawaii International Conference on Systems Sciences, vol. 4, Kauai, January 1994, pp. 210–223.

29. MacNeil, R. Generating multimedia presentations automatically using TYRO, the constraint, case-based designer's apprentice. IEEE (August 1991), 74–79.

30. McQuillan, J. Multimedia networking: an applications portfolio. Data Communications, 21, 12 (September 1992), 85–94.

31. Ottinger, L.L., and Paradice, D.B. Approaches to research in multimedia processing. Proceedings of the National Decision Sciences Institute, November 1991, pp. 944–946.

32. Parsaye, K.; Chignell, M.; Khoshafian, S.; and Wong, H. Intelligent Databases: Object-Oriented, Deductive Hypermedia Technologies. New York: Wiley, 1989.

33. Pracht, W.E. A graphical interactive structural modeling aid for decision support systems. IEEE Transactions on Systems, Man, and Cybernetics, 16, 2 (1986), 265–270.

34. Ragusa, J.M. Models and applications of multimedia, hypermedia, and intellimedia integration with expert systems. Expert Systems with Applications, 7, 1 (1994), 7–13.

35. Ragusa, J.M.; Dologite, D.G.; Orwig, G.W.; and Mockler, R.J. Adding knowledge-assistance to PC-base photographic image database management systems. Information Resource Management Journal, 6, 2 (1993), 27–36.

36. Ragusa, J.M., and Orwig, G.W. Attacking the information access problem with expert systems. Expert Systems: Planning, Implementation, Integration, 2, 4 (Winter 1991), 26–32.

37. Raskin, R., Multimedia: the next frontier for business. PC Magazine, 9, 13 (July 1990), 151–192.

38. Saettler, P. The Evolution of American Educational Technology. Englewood, CO: Laboratories Unlimited, 1990.

39. Sipior, J.C., and Garrity, E.J. Merging expert systems with multimedia technology. Data Base, 21, 4 (Winter 1992), 45–49.

40. Thompson, D. Imaging meets expert systems. AI Expert, 6, 11 (November 1991), 24–32.

41. Turban, E. Decision Support and Expert Systems, 2d ed. New York: Macmillan, 1993.

42. Tuthill, G.S. Knowledge Engineering. Blue Ridge Summit, PA: TAB, 1990.

43. Veljkov, M.D., Managing multimedia. Byte, 15, 8 (August 1990), 227–232.

44. Wahlster, W.; Andre, E.; Graf, W.; and Rist, T. Designing illustrated texts: how language production is influenced by graphics generation. Proceedings of the Ninth National Conference on Artificial Intelligence (AAAI-91): Workshop Notes on Intelligent Multimedia Interfaces, Anaheim, CA, July 15, 1991, pp. 9–20.

45. Wanninger, L.A., Jr. The Minnesota imaging project research application for understanding an emerging technology. Proceedings of the 25th Hawaii International Conference on Systems Sciences, vol. 4, Kauai, January 7–10, 1992, pp. 410–419.
