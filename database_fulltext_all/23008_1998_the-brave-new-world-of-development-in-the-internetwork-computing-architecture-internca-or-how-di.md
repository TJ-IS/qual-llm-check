---
otero_id: 23008
otero_key: "SUGK4YES"
title: "The Brave New World of development in the internetwork computing architecture (InterNCA): or how distributed computing platforms will change systems development"
authors: "Kalle Lyytinen; Gregory Rose; Richard Welke"
year: "1998"
journal: "Information Systems Journal"
doi: "10.1046/j.1365-2575.1998.00037.x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Brave New World of development in the internetwork computing architecture (InterNCA): or how distributed computing platforms will change systems development

Kalle Lyytinen, Gregory Rose\* & Richard Welke\*

University of Jyväskylä, Department of Computer Science and Information Systems, FIN-40 351 Jyväskylä, Finland, email kalle@cs.jyu.fi, and \*College of Business Administration, Computer Information Systems Department, Georgia State University, University Plaza, Atlanta, GA 30303-4012, USA

Abstract. This essay is a speculation of the impact of the next generation technological platform — the internetwork computing architecture (InterNCA) — on systems development. The impact will be deep and pervasive and more substantial than when computing migrated from closed computer rooms to ubiquitous personal computers and flexible client-server solutions. Initially, by drawing upon the notion of a technological frame, the InterNCA, and how it differs from earlier technological frames, is examined. Thereafter, a number of hypotheses are postulated with regard to how the architecture will affect systems development content, scope, organization and processes. Finally, some suggestions for where the information systems research community should focus its efforts (if the call for relevance is not to be taken lightly) are proposed.

Keywords: Computing platforms, network computing architecture, systems development, systems development methods, World-Wide Web

## INTRODUCTION

We have entered the dawning of the Brave New World of development in the internetwork computing architecture (InterNCA). In this essay, we use the 'neutral' term of InterNCA to loosely denote all technological components and associated standards that organize internet-based data transfer and computing, as well as the increasingly dense resulting digital interconnectivity between individuals and organizations. The concept is thus broader than just the http protocols and associated browser services with hyperlinks. As recently as 1994, business use of the InterNCA was essentially unheard of. As of 1998, it is evident that InterNCA use will be commonplace. The goal of this research essay is to examine the functionality and architecture of the InterNCA and to estimate and speculate about its impact on developing and managing information system (IS)-based services. We argue that in order to increase the relevance of IS research, i.e. our need as a research field to look at practice, to work with practitioners and to improve the work that they do through our research, researchers should become more cognizant of the InterNCA phenomenon. In particular, we should ask what challenges the InterNCA will have on IS development, and on how development services will be organized and delivered in the future.

The fundamental premise of our exploration is the following claim: the InterNCA will drastically change IS services, their delivery and their associated organizational processes. We use the term service throughout this article in contrast to ‘application’ because we think the latter term provides a wrong image and ‘granularity’ at which we should view design and management of computing tasks. The InterNCA will result in an unprecedented speed of change and discontinuity in service alternatives, use new software-based mechanisms, lead to ubiquity of services and coalesce software development with media design. These changes will profoundly shape the way we should think, develop and use IS.

These changes are far more drastic than any we have seen so far using the World-Wide Web (WWW) as a passive communication tool (Cox, 1997). Yet, even these relatively minor uses of the InterNCA have resulted in an explosion of electronic marketing and placed Internet and Intranets the top priority in many IS departments. In contrast to the current beliefs, the InterNCA is not about how to develop cute web pages and manage company-wide WWW sites. The importance goes much further and deals with how organizations will or can use, manage and organize a radically different computing platform in the future.

This essay is organized as follows. First, the new IS service delivery platform (ISD platform) is identified. Second the implications of this platform for systems development is then discussed. Finally, research challenges that will drive our research in this area in the future are identified.

## THE TECHNOLOGICAL FRAME OF INTERNCA

Frame proposition F1: the InterNCA exhibits a new, revolutionary, ‘technological frame’ (Bijker, 1987) of computing, i.e. a new aggregate of concepts and techniques used by a community of IT service providers in its problem solving

The InterNCA technological frame portrays a radical break from old technological frames built on mainframes, personal computers or client-server computing. This discontinuity is a result of such elements as goals of use, theories, problem-solving strategies and development practices. It embodies the oft-heard phrase, ‘the computer is the network’.

The technological frame of the InterNCA platform has already been established through standards, designs, successful applications and development practices. Remaining technological bottlenecks are being rapidly resolved (such as interface integration, new media-related services, service standardization) and the alignment of different goals of diverse stakeholder groups including software vendors, hardware suppliers, telecommunication operators and media business is taking place. Consequently, strategists and utopists are beginning to seriously consider the possible uses of the InterNCA. In addition, a user base of over 150 million users is there to foster its rapid diffusion and learning.

## Frame proposition F2: our view of IS services will be redefined by the InterNCA technological frame

In the near future, IS services will be conditioned by the InterNCA in the same manner as earlier generations of IS services were conditioned by mainframe or PC architectures. Fundamentally, the new platform will result in four major changes in IS services:

\- The first change will be in the ubiquity of services: services available at any time and at any place.

\- Second, the speed of change in available services will be unprecedented. The pace at which new modes of delivery have been invented within the InterNCA — including web-frames, push technologies, component-based solutions, XML, etc. — and subsequently have been adopted is unheard of even in the fast-paced world of computing. Services can be developed and maintained an order of magnitude faster than with earlier platforms. This results in a situation in which past best practices and gradually learned ways to use previous technological ‘frames’ do not work anymore. As a result, many technologies and related skills will become obsolete overnight. Just one example is the need (or even memory of the use) of gopher for the distribution of information.

\- Third, new software-enabled mechanism services will change, as will the ways organizations develop and use software. The InterNCA platform is founded on the use of component architectures that will help the creation of software component markets and the delivery of software through the network.

\- Fourth, IS service delivery will coalesce around problems of media design: IS services will become foremost media based and media oriented in contrast to computation orientations of the past.

## Frame proposition F3: changes in IS services imply changes in future functional architectures

Based on Zachman's work on information architecture frameworks (Sowa & Zachman, 1992), we can characterize the future system architecture using the following six components: data, function, network, people, time and motivation (Zachman, 1987). These components correspond to six interrogatives of what, how, where, who, when and why, that one must ask while thinking of any IS service. Table 1 summarizes major characteristics of InterNCA's architecture and how they relate to Zachman's six components. (URLs of some appropriate technical references for many of these technologies are provided at the end of this paper.) These are further divided into two major categories: user-related features and technology features. The former relates to the ways in which any type of IS service is seen or delivered to the would-be user. The latter describes new and novel technological aspects in the InterNCA platform that make it radically different from the previous platforms.

Table 1. Features of the InterNCA

<table><tr><td>Information system architecture changes</td><td>Unique architectural features</td><td>ISD area impacted</td></tr><tr><td colspan="3">User related</td></tr><tr><td>What, how</td><td>Unified user interface with multimedia services</td><td>A, S</td></tr><tr><td>Where, what, why, who, when, how</td><td>Similar access to all clients</td><td>T, A, B, S</td></tr><tr><td>Why, what, who, when, how</td><td>Reflective applications</td><td>B, S</td></tr><tr><td>Why, what, who, when, how</td><td>Workflow and group-level services</td><td>B, S</td></tr><tr><td colspan="3">Technology related</td></tr><tr><td>Where, how</td><td>New telecommunication services</td><td>T, S</td></tr><tr><td>Where, what, why, who, when, how</td><td>Component-based capability</td><td>T, B, S</td></tr><tr><td>Where, how</td><td>Multimedia databases</td><td>T, S</td></tr><tr><td>What, how</td><td>Integration of both structured and unstructured data</td><td>A, S</td></tr><tr><td>What, how</td><td>Separation of user interface and application rules</td><td>A, S</td></tr></table>

The first column in Table 1 refers to which components of the architecture are being impacted by the InterNCA platform. Novel features of the InterNCA in contrast to earlier generations of computing are presented in the second column. The third column shows how these features will impact development skills (these will be discussed below in delivery proposition D5). Overall, Table 1 offers a flavour of emerging technologies, interfaces and standards that will make up the technological frame of InterNCA. It illustrates how substantial changes are taking place within computing ‘frames’, as each interrogative is impacted numerous times by items in this list. Below each of these unique features are described in more detail.

## Unified user interface with multimedia services

In the InterNCA platform, the user interface will be unified through the concept of browsers. A unified interface forms a stark contrast to traditional, specialized environments where a dedicated and specialized interface existed for each application family and platform. Currently, browsers are available for all technical environments and can form the standard interface to all computing tasks. In addition, they will unify representation of aspects of their heterogeneous clients and new standards can add novel functionality to the interfaces such as VRML offers for 3D graphics. Moreover, multimedia and interactive functionality can be presented via platform-independent applets (Java), scripts (Java Script) or components (Java Beans).

## Similar access to all clients

The InterNCA allows design of applications that can be executed entirely on the client, entirely on the server or any of their combinations. Again, this is in stark contrast to relatively rigid demands for specific execution environments in current applications. Applications need not have persistence on the client side, and they can be streamed to the client from the server. As none of these solutions requires persistent client software beyond a browser (in this case, Java enabled and compliant with the appropriate protocols such as IIOP, TCP/IP, HTTP, etc.), thin network computers and portable clients can be used as primary execution platforms. Yet, thin clients can potentially have the same functionality, look and feel as traditional more robust clients.

## Reflective applications

In contrast to previous platforms, the InterNCA-based browsers provide users with the details of application metadata. There is no difference between how system data and how system documentation need be handled. For example, view document information and view document source functions provide a window to the inner workings of the InterNCA applications. In addition, readable scripts can be incorporated into HTML (or in addition powered with XML) pages and used in lieu of compiled code. This fosters user learning and sharing of information, which is necessary with short application lifespans.

## Workflow and group-level services

A new layer of software has emerged with the InterNCA that is often referred to as ‘glueware’ or ‘middleware’. These software components enable task integration and task co-ordination from the user point of view. They are also called workflow systems because they manage the flow of information objects through applications. Thus, the InterNCA, in contrast to older platforms, can provide these services seamlessly at the user interface. This is because dynamic task monitors and higher level co-ordination protocols can be integrated to the network-based interface.

In addition, uniform service interfaces can be expanded to all types of applications including personal tools, group-level tools and traditional applications. The integration of personal tools with group-level, multimedia tools will make a drastic difference. Whiteboards, video conferencing and newsgroup applications are seamlessly integrated and the InterNCA will thus create an environment in which end-user computing and group-level computing take place within the same client.

## New telecommunication services

The InterNCA takes advantage of rapidly expanding telecommunication standards and solutions. These standards and solutions were not available with previous platforms. Highly functional telecommunication services will become commonplace as telecommunication costs decrease and bandwidths soar. For example, currently projected speeds with twisted pair lines are 6 Mbps by the end of the century (Heim & World, March, 1997).

In addition, high bandwidth wireless connections up to 2 Mbps will be possible from any car or pocket using the new third-generation wireless solutions that will be available by the turn of the millennium [Universal Mobile Telephone Services (UMTS)]. A bleak reflection of the expected functionality of these technologies can be found from the current multifunctional wireless personal digital assistants (PDAs), such as Nokia's Communicator 9000. In contrast to old applications, some clients will be mobile and use several telecommunication protocols and standards.

## Component-based capability

Object-oriented technologies are currently evolving to distributed object-based systems that use object request brokers (ORBs). These systems provide standardized object based services (such as Active X, Java Beans and CORBA). The ORBs allow the creation and use of software that is more granular, configurable and 'market driven' in contrast to the current situation.

Distributed systems managed by ORBs will change the delivery and production mechanisms related to software production. This will in turn create software production that is more individualized and market based (Cox, 1996). Future services will become quickly and easily configurable using even the most remote computing services and using replaceable components. Moreover, each component in the system will be able to execute on several platforms and across networks. In addition, legacy systems will be transformed and encapsulated through interfaces. The result is that existing systems will be available for use as distributed components.

## Multimedia databases

In the InterNCA, data of any kind can reside anywhere on the network. All machines that are enabled as servers can store multimedia data. Business databases can be accessed via CGIs (common gateway interfaces), and their output can be posted dynamically as needed to a browser. With hyperlinks and search engines, data can be found across the network and treated as if it resides on one machine. Databases will become key components in media management systems.

## Integration of both structured and unstructured data

Borderlines between structured databases and document management will become blurred both at the application interface and at the database operation level. The InterNCA standards can embed both structured data and unstructured data as objects in HTML code. Moreover, search engines and hyperlinks provide structure to less structured data within documents. Further, component capability allows data to be directly available as output to the browser or indirectly as input to component containers. This input to components allows applications to use structured and unstructured data simultaneously.

## Separation of user interface and application rules

Traditionally application programs mingled code that dealt with application rules and the user interface. The former component encoded the procedural knowledge in application domains. The InterNCA allows these two components to be separated into distinct component capabilities and services. As a result, application rules will be managed as an organizational asset and maintained as part of the organization's component base. Much of this application logic is available commercially and can form part of existing business reference component frameworks (such as SAP/R3).

## IMPLICATIONS FOR IS SERVICE DELIVERY

## Delivery proposition D1: telecommunications skills become critical in developing applications in the InterNCA

Telecommunications skills are rarely considered as part of everyday development skills. Before the InterNCA, telecommunication services had been considered static and given during system development. Telecommunications now must be considered part of the system developers domain. This can be likened to the situation in the late 1970s when database design was tenuously added to the list of needed development skills.

As the InterNCA becomes the dominating platform, the increasing degrees of freedom from dynamically changing telecommunication functionality will make such knowledge mandatory. For example, the next generation of intelligent switches and routers make (non-standard) protocols, tailored to a particular application, possible. Likewise the development of third-generation wireless telecommunication services (such as UMTS) will integrate mobile computing as one aspect of any application design. Therefore, developers will need a much deeper understanding of telecommunication capabilities in order to develop services that meet a rich variety of demands for applications across an array of fixed and mobile intelligent devices deployed (or roaming) throughout the world.

## Delivery proposition D2: user interface design skills must be broadened in InterNCA

The InterNCA is an information-rich kaleidoscope of multimedia content that will further tax the cognitive capability of many. This taxing has a medical name ‘information fatigue syndrome’, which, according to one study reported in the Investor’s Business Daily, over 50% of senior management already suffer from. The current technical skills of forms layout and data design are insufficient to usefully master the emerging ‘network user interface’ (NUI). Multimedia functionality delivered via a common interface co-mingles the issues of content and form. Both artistic and content skills, as well as information organization (e.g. using hypertext linking), become a necessity. Without a significant change, technically focused people will continue to perform content-related tasks with predictably poor results.

## Delivery proposition D3: broad organizational design and change management skills are necessary in the InterNCA development

Today, BPR skills, and the issues they address, have become an important expansion of the scope of effect considered in IS development. The InterNCA will further push the frontiers of change, both in speed of technological change and in the scope of organizational impact it enables and embraces. The problems brought on by nearly continuous change are formidable; the intervals between ‘freezing’ and ‘unfreezing’ are becoming indiscernible. The learning organization must either learn more quickly or fall to those organizations that can sustain such change. In addition, the emergence of ‘virtual’ or ‘relational’ networks as a viable organizational form, enabled by the InterNCA, place even greater demands on the designers of such systems. Thus, IS design will become a broad area of mission critical business change that must comprehend, and develop systems for, emergent organizational arrangements. Importantly, it must do so in a manner that can be quickly assimilated and understood.

## Delivery proposition D4: software development changes radically in InterNCA

The complexity of the InterNCA is, at present, at least an order of magnitude greater than its predecessor, the client–server model. Yet, many organizations have had considerable difficulty implementing distributed applications using even that model. At the same time, once distinct application types (e.g. workflow, decision support systems (DSS), imaging, transaction processing, collaboration) are blending into a set of 'features' that may or may not be possessed by a particular application.

At the same time, the distinctions between ‘internal’ and ‘external’ applications have greyed. The impact of this greying is both the altering and the broadening of design considerations such as availability, security, support and access for all applications. In response to these issues, new mechanisms and methods of application assembly are emerging. Among some of these mechanisms and methods are visual scripting of components at the client side and component-server sides, distributed component architectures with multiple layers for presentation, enterprise-wide component-based application generation, security, messaging, management and communication. These are a far cry from the application-oriented, data-flow diagramming, functional design and bespoke application days of yore. Against these changes, the role of the software developer necessarily changes. Some will manufacture components; the majority will facilitate their adaptation, choice, understanding and use.

## Delivery proposition D5: IS development skills have to be broadened

The InterNCA-induced changes will profoundly transform system development. Not only will development tasks change in content, but they will also have a new scope. The scope of knowledge needed to develop IS services will grow so large that no individual will be able to become an expert in all areas. Tasks will have to be divided and experts will need to co-operate more than ever before in multiskilled teams. Consequently, roles in teams will go beyond ‘old’ dichotomies between users and designers.

Necessary skill components in delivering services will be Telecommunications, Artistic/content, Business Process Design and Change Management and Software skills (TABS). Telecommunications skills will be needed because of the ubiquity and variety of telecommunication services in applications. BPR/CM skills will be needed because of the speed of organizational change induced and discontinuity in organizational designs. Artistic/content skills will be needed because of the coalescence of systems with the media design. Finally, new software skills are needed because of the novel software based mechanisms used to deliver new services.

Collectively, we call the new system development skill profile the TABS Model. The four components of TABS break out in a similar fashion to the architecture framework of Zachman. Essentially, the scope and scale of development in the new InterNCA requires a specialization along individual architectural components. Table 2 summarizes how Zachman's components relate to the four TABS areas.

A list of how these four development skills are necessitated by features of the InterNCA are shown in column 3 of Table 1. Note how all features impact software development. Also, note how each change impacts at least two skill areas in column 1. This demonstrates that the scope of knowledge needed to develop services on the InterNCA is necessarily broad. Although each development initiative cannot be expected to cover in depth all skill areas, IS managers and project managers must understand each of the four areas and integrate them into high-quality designs. Finally, all services available within the platform will need to be viewed holistically because of their ubiquity and fast delivery capability. Developers should be seen responsible for providing and managing a set of integrated services rather than developing singular ‘applications’. Some of these services are developed in-house, some of them are developed by users, and many more are obtained from outside. Because of this ‘incremental’ Lego-like nature of services, the InterNCA will offer tremendous room for creativity and variation in service delivery.

The TABS skills areas are already broadly used in new software development initiatives. From the start, many new software houses have built their business by fully integrating the four TABS components. (We have solicited these examples from the development practices of a Finnish software company called Yomi Media. It develops NCA-based solutions that integrate information systems design and media solutions. These have been developed for many major corporations in Finland.) From its start the company has hired personnel in the fields of telecommunication design, art and content production, software development and lately also BPR personnel. In such an environment, a typical development project involves a diagnostic phase, in which the values of the organization, its desired image and other cultural factors are considered from the media design viewpoint. Based on this diagnosis, a generic application interface — viewed as an open media space — is created for the company’s IS solutions. Using this generic interface, basic look-and-feel guidelines for all corporate WWW-based user interfaces can then be produced.

The generic user interface is then consistently ‘copied’ into each application, although the subsequent design trajectory and options may vary radically in each case. Although specifying the application logic and functionality, ‘traditional’ software skills are needed to design data structures, configure components and develop class structures, etc. Telecommunication skills are simultaneously needed to determine the requirements for the network infrastructure. In many cases the user is not certain how the application will improve her business or whether the organization has to be reorganized to fully use the InterNCA applications. Therefore, broad BPR skills are needed to identify organizational strengths and weaknesses of the user organization.

Table 2. Zachman components and associated TABS skills areas

<table><tr><td>Zachman components</td><td>TABS skills area</td></tr><tr><td>Where or network</td><td>Telecommunications</td></tr><tr><td>What or data</td><td>Artistic/content</td></tr><tr><td>Why, who and when or motivations, people and time</td><td>BPR</td></tr><tr><td>How or function</td><td>Software skills</td></tr></table>

Consider the following real example in which all the TABS skills were integrated This concerns the development of an intranet for the Ministry of Education (MoE) in Finland. Initially a survey was carried out to create a ‘desired’ organizational image for MoE, to find out the organizational values to be reflected in this image, to determine major communication flows inside and outside the organization, and to understand its organizational culture. An artist then designed the look and feel of the generic user interface. Simultaneously, a software engineer started to work on a personnel application using several prototypes to test the desired functionality. All this functionality was then implemented ‘behind’ the designed look and feel. At the same time, a telecommunication expert consulted with the ministry regarding its network solutions and authentication so that these applications could be operated within the ministry. This was often done without taking into account any time or place constraints. The ministry was later advised to organize its intranet operations and how it would obtain radical improvements in its internal information flow.

## THE RESEARCH CHALLENGES IN SYSTEMS DEVELOPMENT

As claimed above, the InterNCA sets a huge challenge for IS research. Never before in the history of computing have we observed a technological change so deep and intense as this. Further, never before has the demand for useful knowledge been so high. As a consequence, current research practices need to be critically evaluated as to what extent they meet the knowledge demands of the InterNCA.

Research proposition R1: to increase their relevance, IS researchers must critically assess their current research methods and standards so that they can scale up with InterNCA development.

We must ask ourselves what types of research methods and standards are appropriate to address the relevant research topics during the InterNCA era. Currently, individually centred, tenure-driven research practices are the norm. However, it seems that these practices are ill-suited to meet the research needs of the future. Traditional research standards that regard ‘researchable’ any topic that can be attacked during a 2-year (PhD) study will come up short. Such research practices do not help us much if we want to improve theories and methods of how large-scale, reusable, distributed, object-based systems can and should evolve. Instead we need to cherish research practices that are based on cumulative, multidisciplinary and longitudinal research designs.

Proposition R2: IS researchers should drop research approaches and topics that do not meet the needs of the InterNCA platform

It is uncertain to what extent all past research topics are relevant and to what extent our current research approaches will be applicable in investigation of the InterNCA phenomenon. As critical devil's advocates we assume that not all are. To assume otherwise is to face the risk of losing the credibility among our patronage — IS professionals — and face a relegation to antiquity.

Research proposition R3: information system researchers must emphasize the long-term evolution of information technology and its infrastructural nature in their research

A pressing topic in years to come will be the management, evolution and assessment of the technologies that make the InterNCA phenomenon possible. This technological complex has many times been coined as the information technology infrastructure. The concept of infrastructure emphasizes longevity, persistence, pervasiveness and criticality of a large array of technological components. Although IS research in the past has focused on some elements of the infrastructure such as networks, the new research challenge is to understand how to manage, transform and transcend the infrastructure to deliver required services with a long-term perspective. Issues that will transpire will deal with technology choices, technology integration, migration, technology planning and implementation. An example of a critical infrastructure topic is the study of standards. Standards govern the integration and evolution of the infrastructure and in turn affect what and how information is passed between services. To date, little research on standards has been performed in the IS academic community. Just ask yourself how many articles you have read about standardization over the last 2–3 years. How many of these articles have been published in top-tier academic journals? In the same vein, IS researchers must take a keen look at how large-scale and dramatic changes take place in infrastructure and how they impact development forms. For example, studies of the impact of new protocols of object migration on legacy system maintenance alone would be worthy in any top-tier journal and would add greatly our relevance.

## Research proposition R7: information systems researchers must address emerging technological needs to develop IS services and seek to provide practical guidelines for doing so effectively

In the area of IS development many topics will parallel with the traditional IS development subjects including: models, methodologies and tools, and implementation guidelines. But as our TABS models suggests, all these have to be rethought. The era of media-oriented and component-driven design will fundamentally change the rules of the game. For example, IS developers should not limit their understanding to the functional requirements and their change. In addition, their design guidelines must integrate media-related requirements and non-functional requirements dealing with security, mobility and so forth.

In addition to rethinking existing topics, radically new topics will emerge. For example, we need to increase our understanding of how to specify and design component-based, multimedia applications that have heavily distributed data and computations. In addition, we need to understand how to manage multiskilled teams. Further, we need to understand how to organize development activities that emphasize reuse. Also, issues such as management of networked development organizations, skill distribution or fast learning by individuals and organizations wait for solutions.

Overall, it is likely that traditional value-chain delivery of IS services will be radically transformed. We speculate that systems development will become more like film production and less like a traditional engineering activity. Such forms of intellectual work as film development combine high levels of both technical and artistic skills within short development spans. In addition, as with film development, it is likely that InterNCA systems development will occur through the use of dynamic and effectively networked organizational forms.

## ACKNOWLEDGEMENT

We are indebted to Olli Väätäinen and Vesa-Matti Paananon for providing details of the development of an intranet for the MoE in Finland.

## REFERENCES

Bijker, W. (1987) The social construction of bakelite: toward a theory of invention. In: The Social Construction of Technological Systems, Bijker, W., Hughes, T. and Pinch, T. (eds), pp. 159–190, MIT Press, Cambridge MA.

Cox, B. (1996) Superdistribution-Objects as Property on the Electronic Frontier. Addison-Wesley Reading, MA.

Cox, J. (1997) The OMG's view of the web. Network World, 14, (2) 22.

Heim, J. (1997) Save that webpage. PCWorld, March, 266–268.

Sowa, J.F. & Zachman, J.A. Extending and formalizing the framework for information systems architecture'. IBM Systems Journal, 31, 590–615.

Zachman, J.A. (1987) A framework for information systems architecture. IBM Systems Journal, 26, 276–292.

## Technical references

VRML information. http://www.ncsa.uiuc.edu/general/vrml
Java information. http://java.sun.com/
Javascript information. http://home.netscape.com/
comprod/products/tools/visual\_js.html
CORBA, IDL and IIOP information. http://www.omg.org
CGI information. http://hoohoo.ncsa.uiuc.edu/cgi/overview

## Biographies

Kalle Lyytinen is a full professor in Information Systems at the University of Jyväskylä, Finland. During 1997 he served as a G.E. Smith Visiting Professor at Georgia State University. His earlier positions include London School of Economics, Hong Kong University of Science and Technology, and Copenhagen Business School. He is the past chairman of IFIP 8.2 and currently serves on the editorial board of Information Systems Journal, European Journal of Information Systems, Accounting, Management and Information Technology, Information Systems Research, Information Technology & People, Requirements Engineering Journal and Journal of Strategic Information Systems. Since 1997, he has been a senior editor of MIS Quarterly. He has published over 70 articles and edited or written six books. His research interests include information system theories, system design methods and tools, system failures and risk assessment, computer-supported cooperative work, and diffusion of complex standardized technologies.

Gregory Rose is a doctoral candidate at Georgia State University. He received an MBA from Binghamton University and a BS in business administration from the University of Vermont. He worked as a systems integrator prior to entering the Georgia State doctoral programme. He is currently working on projects involving implementation strategies, WWW development, and electronic commerce, and has published in the Journal of Global Information Management.

Richard Welke is a full professor at Georgia State University and the head of department of Computer Information Systems. He is the past chairman of IFIP 8. He is widely published and consulted in the areas of method management and engineering management and internet technologies.
