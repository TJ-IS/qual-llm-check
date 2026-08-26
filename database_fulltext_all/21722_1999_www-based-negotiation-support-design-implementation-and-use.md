---
otero_id: 21722
otero_key: "WE9KWB2S"
title: "WWW-based negotiation support: design, implementation, and use"
authors: "Gregory E. Kersten; Sunil J. Noronha"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00012-3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# WWW-based negotiation support: design, implementation, and use

Gregory E. Kersten <sup>a,b,)</sup>, Sunil J. Noronha <sup>c,1</sup>

Decision Analysis and Support Project, International Institute for Applied Systems Analysis, Laxenburg, Austria Centre for Computer Assisted Management, Carleton UniÕersity, Ottawa, Ontario, Canada K1S 5B6 <sup>c</sup> T.J. Watson Research Center, IBM, Yorktown Heights, USA

Accepted 19 January 1999

## Abstract

Support for international negotiations requires integration of decision-theoretic approaches with communication facilities, and different visualization modes. In addition, negotiation support systems NSS should also be tailored to different culturalŽ . and educational backgrounds of their users. While there have been studies on cross-cultural negotiations involving simple game or economic models, there have been no experiments with NSS in international and cross-cultural contexts. At the same time the emergence and quickly spreading use of the World Wide Web WWW and electronic commerce indicates theŽ . potential of NSS supporting commercial transactions across borders. This paper presents INSPIRE, the first Web-based NSS that has been tested and used in teaching and training in several countries. Developed in the context of a cross-cultural study of decision making and negotiation, it has been primarily used to conduct and study negotiation via WWW as well as in teaching and training. The architecture of INSPIRE, which relies heavily on the net-centric computing paradigm and object oriented design, is also discussed. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Negotiation analysis; Web-based support systems; Negotiation support systems, bilateral negotiations; Preference modeling; Conjoint analysis, object-oriented design; Cross-cultural negotiation; Net-centric computing

## 1. Introduction

Negotiations have been studied from many perspectives including psychology, sociology, political science, economics, applied mathematics, engineering, computer science and artificial intelligence <sup>w</sup> <sup>x</sup> 1,12,17,21,23,27,32,33,39,41,50,52 . These perspectives have also been incorporated in negotiation teaching and training. Simulation is an often used vehicle to study and teach negotiation 2,6,13,18, <sup>w</sup> 36,51 . Traditionally, the focus has been on complex <sup>x</sup> and difficult negotiation problems and on training negotiation experts. New computing and communication technologies allow small- and medium-size firms to enter the global market place and therefore, to negotiate deals on international markets. These technologies expand the meaning of the phrase ‘international negotiations’ which are now becoming commonplace.

One of the dimensions adding to the difficulty and complexity of studying and conducting international negotiations is the fact that they involve people from different cultures and with different social and educational backgrounds. Studies of cross-cultural negotiations include analysis of cases involving two or more parties from different countries 15,35 and<sup>w</sup> <sup>x</sup> interviews with, and written experiences of, experts and negotiators who participated in international negotiations 16 . The results of these and other studies<sup>w</sup> <sup>x</sup> have been of little significance to most managers who conduct negotiations with their foreign partners. This is because the negotiations studied involved very large corporations and governments, and highly trained professional negotiators and experts.

Negotiation simulations allow for focused research and for analysis and verification of specific behaviors and interactions. However, simulations are usually conducted in laboratories, in unicultural environments. To obtain results pertinent to international and cross-cultural negotiation, experiments have been conducted in several countries in a manner that allows comparison of results see, e.g., Refs.Ž <sup>w</sup> <sup>x</sup> 2,11,18,43 . These experiments often involve bar-. gaining records enriched with questionnaires and reports from large samples and many countries 9,24<sup>w</sup> <sup>x</sup> but rarely involve negotiations between people from different cultures. There has been little comparative research, especially research involving inter-cultural negotiations. There has been no research on 1 theŽ . use of computers and other sophisticated communication media in negotiation in terms of their relative effectiveness across users from different cultural backgrounds, and 2 as the impact of differentŽ . culture specific decision making styles on the design of electronic aids to negotiation. Yet, these are the characteristics of the increasing number of business negotiations.

The objective of the InterNeg project is to fill this void and develop an environment that supports remote negotiations over simple or complex problems, including real-life situations. This will be achieved through the development of a site on the World Wide Web WWW that includes electronic Ž . bargaining facilities, analytical tools, quantitative and qualitative models, summaries, abstracts, annotated bibliographies, research results, surveys, and other forms of expertise. InterNeg will allow negotiations in multiple locations by many people at the same time and with no additional cost to negotiators. By its very nature, InterNeg has the potential to become accessible to everyone—lay people and experts alike —and provide them enabling tools and information to interact more directly and to bring negotiation expertise to lower levels in social and organizational hierarchies.

The InterNeg site provides systems and information that can be used at any place that has an Internet connection. The site and INSPIRE InterNeg SupportŽ Program for Intercultural REsearch , a prototype of. one of its Web-based negotiation support systems Ž . NSS , have been operational since July 1996. In the first year, over 500 people from India, Canada, Finland, Portugal, US, Hong Kong, and Korea have negotiated via INSPIRE. Because the system is Web-based, inter-cultural negotiations are carried out as easily as intra-cultural negotiations. The negotiations include all main activities, such as preference assessment, analysis of the alternative offers, offer exchanges together with messages, counter-offer evaluation, and the assessment of the compromise efficiency Pareto-optimality . Participants mayŽ . choose to conduct negotiations anonymously, not knowing their counterpart’s country or background. There are facilities that help the user evaluate ‘the goodness’ of an offer, review the history of a negotiation, and determine whether an agreement can be improved in a way that satisfies both sides.

This paper describes the development of the InterNeg site and its current and future services, the architecture of the INSPIRE NSS and the initial experiences with INSPIRE. It sets a basis for future research on the impact of computer and communication technologies on negotiations and international communication within and between cultures. It also aims at providing directions for the development of Web-based negotiation support tools for real-life negotiation with and between human and artificial agents.

## 2. Negotiation support via the Web

InterNeg is a computer-based environment that builds upon two emerging technologies: net-centric computing and NSS. Together, these technologies are integrated into a suite of resources that facilitate negotiation, training and research.

## 2.1. World Wide Web: technologies and serÕices

Recent developments in computer and communication technologies have contributed to two trends that are critical to this research project:

1. Widespread use of networked computer systems —especially systems based upon the Internet— growing at a phenomenal pace, and

2. Flexible system-independent technologies and multimedia interfaces allowing for the use of the systems by anyone and on any computer platform.

The principal feature of the WWW is that it allows people from different locations and time zones to communicate and to use previously inaccessible computational resources. While currently the Web’s greatest use is for dissemination of information and software, it is increasingly being used as a means for remote execution and control of complete software systems, thus adding another dimension to the value it delivers see, e.g., Refs. 4,7,8,44 .Ž <sup>w</sup> <sup>x</sup>.

The Web permeates research and education. Its services include access to techniques and tools that are used in research e.g., statistical packages andŽ mathematical programming software , access to data. and information for processing and analysis, and generation of massive amounts of data. In education, the ability to access and run remote programs and databases allows its users to extend classroom and laboratory boundaries across geographical and time zones. It allows instructors and students to retrieve and use resources from remote sites. However, to our knowledge, the Web is not used in studying and teaching negotiations. Extensive search of Web resources showed that there is a very small number of sites devoted to negotiation a list of these sites isŽ maintained at http://interneg.carleton. ca/interneg/links and its associated Web pages . None of these sites use the Web for research. or training activities that are accessible to students, researchers and practitioners.

## 2.2. Negotiation support systems

NSS are computer-based software tools typically used for training and research in a laboratory environment 5,10,14,25,28,29,42 . In teaching and train- <sup>w</sup> <sup>x</sup> ing NSS are used to:

<sup>Ø</sup> present and illustrate a particular problem solving technique,

<sup>Ø</sup> teach the analytical approach to problem solving,

<sup>Ø</sup> teach negotiation analysis and other decision analytic methods,

<sup>Ø</sup> teach different presentation techniques for problem structuring, analysis and solution,

<sup>Ø</sup> expand a student tool set for communication, conflict identification and resolution, and

<sup>Ø</sup> show the underlying assumptions and limitations of NSS and the analytical methods.

While there is a large and growing number of NSSs, they are rarely used in real negotiations <sup>w</sup> <sup>x</sup> 30,38,47 . Moreover, systems that have actually been used in real negotiations are not of the NSS type. Rather, they are traditional model-based decision support systems allowing for what-if and sensitivity analyses, and simulation of potential effects of the contemplated compromises.

Two current trends that may potentially lead to widespread use of NSS in real negotiations are:

1. the maturity of formal methods for decision and negotiation analysis, and

2. expansion of the use of Web-based systems in business and other transactions.

Zartman 53 argues that decision analytic meth- <sup>w</sup> <sup>x</sup> ods based on multi-attribute theory, simulation modeling, statistical analysis, and cognitive mapping have shown their usefulness. Kersten and Szapiro 31 and<sup>w</sup> <sup>x</sup> Holsapple et al. 26 provide a negotiation support <sup>w</sup> <sup>x</sup> framework that is based on a formal negotiation theory. The INSPIRE system implements many of these postulates; it uses decision theory, supports construction of utility functions and offer assessment, and facilitates communication and process evaluation.

The growth of Web-based commerce systems may be illustrated by the recently created virtual corporations which provide businesses and other organizations with the electronic market and tools for exchanging information, and structuring and recording negotiations see, for example, Ž http:// www.jango.com and http:// www. personalogic.com.. Its result is the rapidly increasing electronic communication between representatives of companies in different countries and time zones. It is safe to assume that a significant part of the communication involves negotiation.

## 3. InterNeg: resources and services

The InterNeg project began in 1996 with the development of a simple Web-based NSS prototype. The software, called INSPIRE, has been tested and enhanced since the Summer of 1996. In July 1996, the system became fully operational. The host InterNeg site also offers other services. It is the home site of two journals, International Negotiation and Group Decision and Negotiation where basic information such as the table of contents, abstracts, and calls for papers are maintained. Beginners’ handouts, information on how INSPIRE can be used in different university courses, and examples of student assignments are available as well as several articles, an extensive bibliography and information about programs and organizations involved in negotiation.

The InterNeg site is a source and repository of negotiation-related resources and its home page is at http://interneg.carleton.ca/. The site is organized into five departments in addition to general information about the site, its history, users and developers. An overview of the site is presented in Fig. 1.

Each department has a different focus:

Reference desk: An archive of reference material on negotiation and negotiation support, including answers to frequently asked questions, bibliographies, software catalogues, glossaries and computing dictionaries.

<sup>Ø</sup> Research and studies: Research output from the InterNeg group, our world-wide collaborators and other researchers.

Support tools and aids: Software that is usable on the Web. This includes software produced as part of the InterNeg project, e.g., INSPIRE and INSS Ž . the InterNeg Support System , and tools contributed by other researchers.

Learning and training: Negotiation learning and teaching resources, e.g., tutorials, essays on and guidelines for negotiation strategies, course information, university programs and other training aids.

![](/api/attachments/WE9KWB2S/fulltext/images/c261ac3105394e0f0bb90655ce725134857ec6d4ae617582666265fdf2f80f61.jpg)  
Fig. 1. The basic structure of the InterNeg site http: Ž . <sup>rr</sup>interneg.carleton.ca<sup>r</sup>interneg<sup>r</sup>overview<sup>r</sup>site\_chart.html .

External links: Links to negotiation-related sites other than InterNeg, and to resources in other negotiation-related disciplines such as software agents, e-commerce, computer-supported cooperative work, etc.

## 4. The INSPIRE process model

## 4.1. Negotiations phases

INSPIRE is the first system designed to conduct negotiations on the Web. It is based on the phasemodel of negotiation proposed by many researchers and practitioners, into which most negotiation processes fall see, e.g., Refs. 12,18,21,40 . It is used Ž <sup>w</sup> <sup>x</sup>. in negotiation teaching and training as well as in the design of NSS. The system is based on analytical models rooted in decision and negotiation analysis <sup>w</sup> <sup>x</sup> 3,29,31,34,42,45 . Developed in the context of a cross-cultural study of decision making and negotiation, it has been primarily used to conduct and study negotiation via the WWW as well as in the teaching of information systems, management science, international business, and English as a second language.

INSPIRE views a negotiation as a process occurring in a particular context. Following Refs. <sup>w</sup> <sup>x</sup> 6,18,34,45 , the process involves a series of activities beginning with pre-negotiation, conduct of negotiations, and post-settlement Žalso called postagreement ..

The pre-negotiation phase involves preparation for negotiation, proceeding through the actual conduct of the negotiation during which messages, arguments, offers and concessions are exchanged and evaluated by the parties until an agreement is reached, and finally, implementation of the agreement. It is usually inappropriate to assume that reaching an agreement is the goal of the negotiation, as is often assumed in low-context societies 12,24 such as the <sup>w</sup> <sup>x</sup> American. Indeed, in many high-context cultures such as the Japanese, an agreement is viewed as merely the beginning. Revision of the contract and re-negotiation are activities of the post-settlement phase and they constitute an integral aspects of the negotiation process 17,41,48 .<sup>w</sup> <sup>x</sup>

INSPIRE currently addresses the following activities of the preparation, conduct and post-settlement phases of the whole process, i.e.,

1. preparation involves understanding the negotiation problem, issues and options, and preference elicitation via hybrid conjoint analysis leading to the construction of a utility function;

2. the conduct of negotiation involves support for offer construction and counter-offer evaluation by means of ratings based on the utility function, and graphical representation of the negotiation’s dynamics; and

3. post-settlement involves computation of possible offers that dominate the most recent compromise and re-negotiation.

These three negotiation phases correspond to three main support functions. In addition to these functions, there is a range of smaller support features, including the maintenance of the history of offers and messages, protected access to the user’s files, and tracking the progress of the negotiation process. Also, during the offer exchange, the user may reevaluate issues and options and modify his or her utility function.

In this section and the next sections, we present the negotiation model and the system. In Section 6, the use of INSPIRE is discussed with a detailed example. To illustrate the implementation of the specific aspects of the model and the system in these two sections, we make references to figures given in Section 6.

## 4.2. Preparation

During the preparation phase each user individually performs activities that enable him or her to comprehend the problem, the main negotiable issues and options, the possible offers and criteria. This phase also involves specification of preferences leading to the construction of the user’s utility function. In order to do so, the user has to compare packages which are possible offers in which all issues are stated i.e., in each package there is one option for Ž each issue . The preparation activities that are imple-. mented in INSPIRE are depicted in Fig. 2. While users may communicate with their partners, the communication at this stage is limited to unstructured messages.

![](/api/attachments/WE9KWB2S/fulltext/images/8899d6595734adf3d46d8f1c8ea3c7e27f06a8e478ad0b18c471c9b45e60d505.jpg)  
Fig. 2. INSPIRE’s preparation phase.

The currently implemented technique for construction of utility functions is based on hybrid conjoint analysis 3,19,20,42 . In this, the initial utility<sup>w</sup> <sup>x</sup> values are composed from the user’s partial assessments and then they are verified and updated with the user’s evaluation of the complete packages. The evaluation of the complete packages allows for the revision of the partial utilities i.e., part-worths ofŽ . each option and for each issue.

In INSPIRE the hybrid conjoint analysis has been implemented in the following three steps in which the user provides concrete preference information: Ž . 1 The user evaluates the relative importance of the issues to be negotiated. The rating assigned to each issue is viewed as a component of the total utility of a package. The utility component of each issue is assumed to be independent of the other issues, i.e., any possible interactions are assumed to be insignificant. Therefore, the utility components are simply added together to form the total utility function and this is called composition. 2 The user evaluates theŽ . relative importance of each issue’s options. The rating of each option constitutes the utility component of an issue when that particular option is the one that is present in a package. This activity is illustrated in Fig. 9. 3 The user makes a comparative evaluation Ž . of several complete packages selected by INSPIRE, viewing each package as a whole. This is the decompositional step. The total utility of a package is decomposed into constituent option utilities using an additive model:

$$
U \left(p _ {k}\right) = \text { constant } + \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n _ {i}} u _ {i j} x _ {i j k} + \varepsilon_ {k},
$$

where: $U ( p _ { k } )$ is the total utility of a package $p _ { k } \mathrm { : }$ $( k = 1 , \dots N ) ; u _ { i j }$ is the utility associated with issue i and option $j , ( i = 1 , \ldots m ; j = 1 , \ldots n _ { i } ) ;$ and $x _ { i j k }$ is a binary variable indicating whether the option i of issue j is present in the package k; and $\varepsilon _ { k }$ is an error. $( k = 1 , \ldots N )$ .

Steps one and two are simple and they have been embedded in other Web-based systems in which users’ utility are constructed 44 . Step three has<sup>w</sup> <sup>x</sup> been added to allow users a holistic assessment of packages, re-evaluate utility values determined in the previous steps, and take into account non-linear utilities.

The number of packages that could be presented is equal to $\begin{array} { r } { N = \prod _ { i = 1 } ^ { m } n _ { i } , } \end{array}$ , where m is the number of issues and $n _ { i }$ is the number of options in issue i. Typically, N is a very large number and we need some way of selectively presenting just a few packages for the user to rate, yet obtain reliable utility values. This is a problem in the design of fractional factorial experiments and one of the most compact and effective designs is the orthogonal design 37 . <sup>w</sup> <sup>x</sup>

All packages can be represented with a matrix X with N column and n rows, where $\begin{array} { r } { n = \prod _ { i = 1 } ^ { m } n _ { i } . } \end{array}$ Rows represent all options for all the issues and a column represents one package. In orthogonal design, n columns i.e., packages ofŽ . X are selected so that the matrix X) is orthogonal. The selected set of orthogonal packages and their initial utility values computed after the second step are presented to the user for the package-rating step. Given the ratings for these packages, the weights $u _ { i j }$ are computed that minimize the error terms using linear regression.

Since the utility of every possible option is considered explicitly, the utility function for a given issue can be non-linear. This is an advantage since people usually do not have linear utilities as they traverse a given range of values.

By default, issues are assumed to have ‘discrete options, i.e., only a small number of explicitly listed options are considered to be meaningful as outcomes of the issue. These are also called salient options and they are used in the process of utility construction. However, some issues can also be ‘continuous in the sense that any intermediate value can be meaningful. This is typical of quantitative issues such as the price of some commodity. In such cases, the utility function within an issue is assumed to be piece-wise linear, i.e., linear interpolation or extrap- Ž olation is used to compute the utility of intermediate. points between the salient options.

## 4.3. The conduct of negotiations

The conduct of negotiations is divided into four standard stages, namely, climate-setting, presenting, mid-point bargaining, and closing. These four stages are not clearly distinguished in INSPIRE. However, the system’s two modes of communication, that is structured offers and free-text messages allow the users to perform activities corresponding to all the stages.

Offers have a pre-defined format; they contain names of the issues and options issue values . WhileŽ . constructing or analyzing an offer, users automatically obtain its utility value. An offer may be accompanied with a message, which allows for argumentation and backing see Fig. 10 for an example . UsersŽ . may also send separate messages in order, for example, to set the climate, request explanations, or press their counterpart for a reply. These and other activities that can be performed during the conduct phase are listed in Fig. 3.

To support users in reviewing the negotiation and its dynamics, the system groups together all the past messages and offers, including utility values. In addition, a graph displaying negotiation dynamics is also available. It depicts all the offers made by both parties over time and the user’s rating scale see Fig. Ž 11 for an example ..

During negotiation, users may review and revise their ratings, effectively updating their utilities, as shown in Fig. 3. We have observed that the graphical facility and offer scores become a focal point with some users and they tend to revise their preferences frequently, apparently with the objective of getting a satisfactory graph with high final scores. We speculate that this kind of preference migration may reflect the users’ cultural background.

![](/api/attachments/WE9KWB2S/fulltext/images/cf73ec96ecdbfad515abe90f23f26f949c0ddc2f77fec7db0f80202ed0133ba0.jpg)  
Fig. 3. The conduct of negotiation through INSPIRE.

## 4.4. Post-settlement re-negotiation

Once a compromise has been achieved during the conduct phase, INSPIRE checks it for efficiency Ž . Pareto-optimality . This is the stage when the system acts as a mediator and takes into consideration the utilities of the two parties. Negotiation ends if the compromise is efficient. Otherwise the system computes efficient packages and displays several of them to both users. The displayed packages include those that increase one party’s utility alone, as well as the mid-point solutions.

The list of the post-settlement phase activities is similar to that of the conduct of the negotiation phase and is displayed in Fig. 4. The system’s additional activity is the computation, selection, and display of efficient offers. A notable distinction is that in the post-settlement phase, users cannot revise their preferences. This is because in this phase, the system uses the preference information to determine and display efficient packages. If either party changes their utility structure, the current efficient solutions may become inefficient; in particular, the last-reached inefficient compromise may turn efficient, effectively terminating the negotiation in a way that would be considered unexpected by the counterpart. Apart from confusion, unilateral transformation of the efficient set under consideration can undercut the acceptability of the mediation process.

Apart from utility modification, users can perform the same actions during the post-settlement stage as during the conduct of the negotiation phase.

## 5. INSPIRE’s architecture

## 5.1. Client<sup>r</sup>serÕer decomposition

The traditional view of a negotiation or group Ž . support system is that of a desktop application: each user has one copy of the software on their personal computer, which communicates with the other users’ copies over a network typically a LAN , usually inŽ . synchronous mode i.e., with both parties simultane- Ž ously logged on . Fig. 5 depicts how INSPIRE’s . process model, conceptualized as a NSS, has been translated into its implementation structure as a Web application. The system uses the client<sup>r</sup>server model of distributed systems to partition the main components.

The connection between the two negotiating sides can be either direct or through a common server program. Conceptually, there is no reason to require the server program unless the concept of a third-party conflict resolution service or facilitatorŽ <sup>r</sup>mediator<sup>r</sup> arbitrator is intrinsic to the group support methodol-. ogy provided by the system. All services not involving a third party, e.g., preference elicitation, offer analysis and construction support, etc., can be implemented locally within each user’s desktop application and indeed it is desirable to implement such Ž features locally for privacy and security reasons—the user’s preference information, for example, should not be accessible to anybody else . Only the objects. explicitly exchanged during communication e.g., of- Ž fers and messages and information required by the . third-party facilitator e.g., preferences for Pareto-op-Ž timal analysis during post-settlement need be trans-. mitted outside the desktop. However, this neat conceptual partitioning based upon functionality which Ž is useful for presentation to a lay user disappears . when translated into the physical implementation of INSPIRE; it is replaced by a two-component: frontend and engine model see Fig. 5 , that moreŽ . closely reflects the realities of current net-centric computing technology 22,49 .

![](/api/attachments/WE9KWB2S/fulltext/images/8a389bd8d6f5ef865c6193cf69951ec48199de63615e792c09ed20c4af992f3e.jpg)  
Fig. 4. INSPIRE’s support of post-settlement activities.

![](/api/attachments/WE9KWB2S/fulltext/images/62f38bfae0178d376a892f2f38c1979bde6c545ee66b4d8a76ccba22884cca2d.jpg)  
Fig. 5. The INSPIRE client<sup>r</sup>server architecture.

Three major factors affect the design of INSPIRE: Ž . 1 We wish to enable users with nothing more than a Web browser and an Internet connection to avail of INSPIRE’s services. This implies a tremendous degree of portability and gives the researchers access to users in remote countries with minimal computing resources. 2 Current trends in net-centric comput-Ž . ing are towards pay-per-use software: programs reside at their developers’ home sites and are automatically downloaded and executed whenever the user needs a particular piece of functionality. This induces a tendency towards an architecture in which the server INSPIRE’s home site plays a central Ž . role, regardless of the structure of communication needs. 3 Since one of INSPIRE’s primary goals isŽ . to observe and log user activities as completely as possible for the cross-cultural study, and since it is difficult to monitor actions on the user’s host machine, it is desirable that all non-trivial activities be conducted through the INSPIRE site.

Another factor that significantly influenced the design is the fact that the negotiations supported are asynchronous: since the two parties negotiating with each other typically reside in far away countries with different time zones, it is rare for both sides to be simultaneously logged on. Therefore, INSPIRE is designed to interact independently with each user, saving the state resulting from each user’s actions in a form that can be retrieved when the counterpart logs on some time later.

Returning to Fig. 5, we see that while the functionality of the facilitator is implemented entirely in applications on the Web server side as expectedŽ from the conceptual organization , the functionality . of a desktop NSS has been distributed between the browser on the user’s desktop and the application programs on the INSPIRE server. However, examining the system’s design in terms of the ‘browser side’ and ‘Web server side application’ implementation components is too fine-grained to convey its modular structure. The appropriate higher-level abstraction is a division of the system into ‘frontend and ‘computational engine’ components.

## 5.2. The frontend and the engine

The distinction between INSPIRE’s frontend and the engine corresponds roughly to the distinction between a traditional knowledge based system’s visible user interface and invisible internal model base and reasoning engine. The frontend comprises dozens of HTML<sup>r</sup>JavaScript pages as well as Java applets. They reside on the INSPIRE site but are displayed or executed on demand on the user’s host machine. The engine is a collection of programs in C<sup>qq</sup>. These programs also reside on the INSPIRE site, but they are executed on the INSPIRE host itself and invoked via the Web server and the CGI protocol. The basic underlying mechanism that connects the two segments is the CGI protocol, but since this protocol is too primitive to directly handle negotiation-related objects, a new high-level tag-style mechanism has been provided on top of CGI, as explained in Section 5.3.

One of the major goals that this architectural division addresses is that of supporting collaborative group development of INSPIRE by people with varying levels of familiarity with Web document presentation languages HTML, JavaScript and pro- Ž . gramming languages and protocols CŽ <sup>qq</sup>, Java and CGI . One of the most important reasons for the . explosive success of the WWW is the ease with which anyone can develop Web pages. INSPIRE’s frontend, though sophisticated in organization and content, is amenable to design intervention by anyone with basic word processing skills and this has enabled people with wide ranging skills including behavioral scientists and decision analysts to directly modify and contribute to the design. This is possible because the frontend’s interface to the engine resembles an extended set of HTML tags. The engine on the other hand comprises several thousand lines of C<sup>qq</sup>, and along with the Java applets is accessible for development only by relatively experienced programmers.

All of INSPIRE’s implementation is object-oriented, and each piece of functionality listed within the two major components in Fig. 6 is provided by a group of object classes that is loosely coupled with the rest of the system. Therefore, each of them has been implemented fairly independently of the others. At the heart of the system lies one segment, labeled ‘methodologies’ on which we focus here and in Section 5.4.

In this context, ‘methodologies’ is an umbrella term for the sequence of activities performed by the users in conjunction with the system. This is the part of INSPIRE’s architecture where it looks at the state of the negotiation and dispatches a page from the frontend to the user’s browser or performs a short sequence of computational activities and typically displays their results. This is obviously an important part of the system and implicitly controls the invocation of much of the other functionality of the system.

In general, users always need to know ‘What can I do next?’ and the answer depends on the context and any rules provided by the system’s designers. In other words, we have to deal with states and contexts.

Based on the state of a negotiation, differing sets of activities are proposed to the user. Web pages are very good at representing and presenting context. Therefore, methodologies can be implemented by a dispatching system that determines which page to display based on a given situation. One of the principles learned from the INSPIRE implementation is that a rule-based structure works surprisingly well for implementing methodologies. In fact, the whole section comprises a series of if–then–else statements in C<sup>qq</sup> and stands out from the otherwise characteristically object-oriented code in the system. An example of the rule-based structure of the ‘methodologies’ component is given in Table 1. The fragment of the C<sup>qq</sup> code represents the rule that is invoked if the parties are in the conduct negotiations phase and did not achieve a compromise. The statement "pipe\_fileŽPAGE\_DIR <sup>q</sup> "<sup>r</sup>offer\_first.html", substitutions." and a similar statement that follows it are used to create dynamic Web pages which are described in more detail in Section 5.3. If there was no offer exchange, a dynamic Web page is generated for the user to formulate an offer and a message anŽ example of such a page is given in Fig. 10 . If one or.

![](/api/attachments/WE9KWB2S/fulltext/images/c432dd79a8fba091314fee8878fa7f3c6c9aa03a1fc34dfbf4a5ec0870691c26.jpg)  
Fig. 6. INSPIRE’s main components.

more offers were exchanged, the Web page also contains the most recent offer of the counterpart.

This part of the architecture can be summarized as follows: pages in the frontend represent contexts; states are represented by mostly Boolean expres-Ž . sions in the engine. While the latter is obvious, it helps in understanding the former to observe that each page displays text and images describing part Ž of the current situation and gives the user options . Ž . clickable links, prompts and other widgets to perform only those activities that are relevant to the given context.

Table 1 Example of the rule-based ‘methodologies’ component

<table><tr><td>C + + code</td><td>Comments</td></tr><tr><td>if (! session.agreement_reached())</td><td rowspan="3">If the parties are in the offer exchange mode but no agreement has been reached and if no offers were made by any user then</td></tr><tr><td>{ if (session.active_user.history.number_of_offers() == 0)</td></tr><tr><td>if (session.other_user.history.number_of_offers() == 0)</td></tr><tr><td>{ pipe_file (PAGE_DIR + &quot;/offer_first.html&quot;,substitutions);}</td><td rowspan="2">display any message from the counterpart and prompt the active user for the first offer</td></tr><tr><td>else</td></tr><tr><td>{ pipe_file (PAGE_DIR + &quot;/offer_compare.html&quot;, substitutions);}</td><td rowspan="2">otherwise display any message from the counterpart, compare with the last counter-offer, and prompt for an offer</td></tr><tr><td>}</td></tr><tr><td>}</td><td rowspan="2">otherwise...</td></tr><tr><td>else</td></tr></table>

## 5.3. The coupling mechanism

The Web pages that comprise the user interface are generic in the sense that they can be re-used for arbitrary negotiation cases. However, an unchanging Web page cannot reflect the dynamics of a negotiation. The dynamics inherent in the process manifests itself in two ways: 1 different Web pages must beŽ . displayed to the user in response to different actions, and 2 the contents of a given Web page itself must Ž . adapt to the latest situation. For example, a page displaying the issues under negotiation cannot have the issue names hard-coded since they differ from negotiation to negotiation; the names must be generated on the fly.

In short, Web pages have to be constructed on the fly by the programs in the engine to display dynamic or adaptive responses. However, hard-coding the contents of Web pages into the software would be a very poor approach to system development as it requires program recompilation for the slightest change, suffers loss of readability and maintainability, and prevents non-programmers from directly working on the contents of the pages.

It is clear that a means must be found to generate only those parts of a Web page that absolutely have to be computed by the engine e.g., information thatŽ is specific to the users or the negotiation, utility values, etc. and retain the rest as a proper Web. page. The solution we found is to support new HTML-like tags in the Web pages that are understood by the INSPIRE programs. These special tags begin with <sup>-</sup>INEG<sup>)</sup> and end with ${ \mathit { \Sigma } } < / { \mathrm { I N E G } } > ;$ for example <sup>-</sup>INEG<sup>)</sup>user\_id<sup>-r</sup>INEG<sup>)</sup> denotes the name of the user accessing the INSPIRE system. A Web page containing such <sup>-</sup>INEG<sup>)</sup> tags is called a dynamic page because it adapts to the situation as Ž explained in a moment , whereas a page without . these tags is called a static or normal HTML<sup>r</sup> JavaScript page. Dynamic pages are not meant to be directly accessed on the Web via their URLs; rather, dynamic pages are meant to be processed by the INSPIRE engine before being displayed to the user. When any program in the INSPIRE engine pipes out a dynamic page, it substitutes each <sup>-</sup>INEG<sup>)</sup> tag by something appropriate in the above example, theŽ user’s name . This simple ‘macro substitution. mechanism enormously simplifies the interface between Web page developers and program developers. All that is required to keep the user interface and the engine fully synchronized with each other is a welldesigned catalogue of <sup>-</sup>INEG<sup>)</sup> tags and their semantics.

There are four categories of $< \mathrm { I N E G } >  { \mathrm { \ t a g s { \Omega } } }$ in INSPIRE: identification, version management, history state recapitulation, and negotiation object em-Ž . bedding e.g., offers, messages, rating tables . ForŽ . example, <sup>-</sup> INEG <sup>)</sup> issue\_rating <sup>-r</sup>INEG <sup>)</sup> generates the HTML table used during the preparation stage to rate the issues; $< \mathrm { \Delta I N E G } > \mathrm { \ o f f e r } _ { - }$ construction\_box ${ < / \mathrm { I N E G } > }$ generates a table containing menu selections for each of the issues by which the user can construct an offer; and <sup>-</sup>INEG<sup>)</sup> engine\_url ${ < / \mathrm { I N E G } > }$ identifies the location URLŽ path to the engine programs on the INSPIRE site . enabling them to be freely moved around.

## 5.4. The main components

The DSS architecture has traditionally been neatly divided into three components: Dialog, Data and Model, i.e., the ‘DDM paradigm’, with clearly defined roles for each component 46 . We found this<sup>w</sup> <sup>x</sup> architecture restrictive and inflexible. The DDM concept does not sufficiently address the need for flexible use of multiple-complementary as well as competitive-analytical methods. The traditional DSS architecture limits communication between the system’s components and also the components’ communication with external systems in ways independent of any pre-specified control mechanism. In the development of INSPIRE, an effort was made to construct software objects that can be used and reused in different conditions and in different configurations. Moreover, we aimed at a system which in the future can be expanded with new and additional components. Thus, we were looking for a system which allows for:

1. the situation-dependent use of different decision, negotiation, and data analysis and visualization support methodologies defined by available data Ž or meeting specified constraints or is specified by the user ,.

2. management and visualization of a potentially very large set of solutions,

3. private and content rich communication between the users, other systems and Web sites as well as the ability to communicate with users through e-mail,

4. use of specialized models for dialog, solution and communication components, in addition to those used in the Model component,

5. expandability in directions not necessarily envisaged by the developers and the ability to use external services provided by other Web sites.

The main component of the INSPIRE system that is instrumental in obtaining the above characteristics is the Methodologies and control Ž . M&C component.

Figs. 7 and 8 depict the INSPIRE architecture in two main modes: the support of a single party in the negotiation individual support mode and the mode Ž . in which the system determines and presents efficient solutions joint support or mediation mode . AtŽ . a general level, as discussed in Section 5.2, the architecture comprises the engine and the frontend. Currently, the frontend functions as a Dialog component with limited computational capabilities. However, with the introduction of Java applets and coupling with local client applications, the frontend functions will encompass some of the functionality of the Model and Data components.

The Model component is represented by several separate objects used for preference elicitation, utility and history construction, and also other objects which are activated by the M&C component at different stages of the negotiation process. The M&C component of INSPIRE decides on the system’s behavior; it takes information from the frontend Di-Ž alog component..

The negotiation process supported by INSPIRE can take several different forms. Negotiations can be sequential, that is, parties discuss about one issue at the time, parallel, and mixed. They also can be conducted with or without messages. Other options, which are not yet implemented, include the addition and<sup>r</sup>or deletion of issues and options, addition of separate objects e.g., price lists, pictures to the Ž . messages, voice and video, etc.

A major problem with the DDM is that it does not have a plug-and-play philosophy. The system should be viewed and implemented as a collection of loosely-associated smart objects the DSS as toolkitŽ metaphor . DSS and NSS design . must always be open-ended-amenable to change, but most DSSs are weak in providing a methodology for change. We view system change as an upgrade in the attributes or behaviors of indiÕidual objects occasionally,Ž modules , independently of other objects or modules,.

![](/api/attachments/WE9KWB2S/fulltext/images/5fe02835b89bd054786b173811970c12de565435a07ed5ceb634bd014d495feb.jpg)  
Fig. 7. INSPIRE’s architecture: Individual support mode.

![](/api/attachments/WE9KWB2S/fulltext/images/b3e36fe77450759c0cf2d570022c4c7657352009f17237c9fb00a921dbe3fd30.jpg)  
Fig. 8. INSPIRE’s architecture: Mediation mode.

rather than one synchronized change across the whole system.

As an example, consider the problem of making INSPIRE qualitative-information-capable, i.e., able to handle missing information such as incomplete preference ratings. This can be implemented by a series of independent changes: upgrade the PreferenceStructure object classes which deal with storage and retrieval of preferences to accept holes in the data; then upgrade the UtilityFunction objects to interpolate for missing preferences instead of asking for additional information; then upgrade post-settlement algorithmic classes to deal with interval ranges; then experiment with alternative preference elicitation strategies that optimally use qualitative information. A good sufficiently general and abstract set ofŽ . object interfaces and loose coupling between components are critical to achieving this kind of open-endedness.

One of the main characteristics of the INSPIRE system is its expandability. Fig. 7 illustrates the loosely coupled architecture of INSPIRE. This is also depicted in Fig. 8, where some objects are introduced and others removed due to the change of the system’s mode of operation from individualŽ support to mediation ..

It may appear that Figs. 7 and 8 depict two different though similar systems. This is of courseŽ . not the case, but reflects the ability to use the same components to perform similar functions but for different users, or the use of the system’s other components which previously were not available. For example, the same engine can be used by each user separately in the individual mode to rankŽ . offers or it can be used in the mediation mode and order offers using both utility functions.

In the mediation mode, the system can be viewed as comprising three engine and two frontend entities. This mode is entered only when the users have achieved a compromise. The components involved in these activities are depicted in Fig. 8. Note, however, that the smaller and larger components with the same names are ‘clones’ of the same program but used for different users or different other components. At this stage, the system verifies the efficiency of the compromise using—for the first time—the utilities of both simultaneously. If the compromise is non-efficient, the system asks users whether they want it to search for efficient solutions. Upon obtaining a positive answer from both users, the system determines efficient solutions and selects and displays five solutions for each party.

Once the negotiation is concluded, INSPIRE informs the users and asks them if they agree to provide their counterparts with their negotiation dynamics graphs and other graphs that describe the negotiation dance 41 . The graphs are displayed<sup>w</sup> <sup>x</sup> only if both parties agree.

## 6. An example from a real negotiation

The illustrations in this section are intended to provide the flavor of an INSPIRE session. An example of one of the user activities during the prenegotiation stage is given in Fig. 9. Having read a description of the case—which specifies the four negotiated issues the purchase price of the bicycle Ž parts under negotiation, the delivery and payment schedules, and the return policy for defective parts. and the options available for each issue—the user is requested to compare each of these options against the others and specify their relative importance. The ratings supplied by the user during this and subsequent steps are used to construct a utility function.

During the conduct negotiation phase users construct offers, analyze counter-offers, send and receive messages, and review the negotiation dynamics. Fig. 10 is a snapshot of the offer construction screen; it illustrates how the users can communicate either by plain messages or structured offers, and how the score attached to an offer helps select a good offer.

![](/api/attachments/WE9KWB2S/fulltext/images/c90afa6b5bc935b888c4ded03af121ed6f946abf1a32b5dea686c4173f89bc01.jpg)  
Fig. 9. Rating the options of each issue.

Fig. 11 is a graph of the dynamics of the negotiation process; such graphs are generated on the fly throughout the negotiation, and the one in the figure was generated at the very end of the negotiation. The user names displayed on the graph Ž . misty and ldias are pseudonyms adopted as INSPIRE login names by the users in order to protect their anonymity. The small numbered triangles denote offers; the X-axis shows the time at which each event occurred and the Y-axis represents the score associated with an offer. Note that though the offers of both parties are shown, only a single utility function Ž . misty’s has been used to evaluate all of them. For two reasons: eachŽ party’s preference information is private and unavailable to the other side; nor is it meaningful to make interpersonal utility comparisons ..

Note that while misty makes concessions right until her fourth offer, ldias makes concessions until his third offer; then he appears to make a reverse concession between his third and fourth offer. This worries misty into thinking that ldias has hardened his position, and she quickly accepts his fourth offer. In truth, ldias did not make a reverse concession; his graph not shown indicates that his fourth offer was Ž . indeed worse for himself than his third—from his point of Õiew! In other words, when he thought he was giving away value to misty in order to reach a

![](/api/attachments/WE9KWB2S/fulltext/images/9d92ae0e6c897d69b9e26b6b1945ed6add16fa60654f5cb967bdf85367ea751b.jpg)  
Fig. 10. Offer formulation

![](/api/attachments/WE9KWB2S/fulltext/images/5c0e7695aa45674f5f061f4be2b600d706952c7bdd772f3b24097fe3f0947a4a.jpg)  
Fig. 11. Graph of negotiation dynamics.

compromise, he actually appeared to her to have grasped value and taken a tougher stance. This pattern is quite common in the negotiations observed via INSPIRE and underscores natural misunderstandings as a cause of negotiation failure.

As a consequence of misty accepting ldias’ fourth offer which was worse for both of them than his third, INSPIRE automatically enters the post-settlement phase and recommends several better compromises. The system’s recommendations are given in Fig. 12; three packages dominate the accepted compromise. Note that one of these packages yields the same utility value rating Ž . <sup>s</sup> 50 , to one user. However, this package increases the utility to the other user and therefore it is also displayed.

In the post-settlement phase, ldias and misty continue negotiating, each making their fifth offer, and finally, an optimal compromise as shown in Fig. 11 is reached.

## 7. Future work

The INSPIRE system has been developed as a tool for research and also used for training. Because of the cross-cultural research function we do not plan to change the system; its specification has been frozen so that we can compare the conduct of negotiations by different users, and at different times. However, our experience with this system, both in terms of the research output from analyzing international negotiations conducted through INSPIRE, and the experience gained from building and deploying a NSS, as well as the feedback from our users, motivate and inform the design of a new system, INSS, which is currently under development. INSS will have all the features of INSPIRE and many more.

By using Java applets, users will be able to add new values options to the negotiation issues. If, for Ž . example, a user begins with five salient values for the price, she may add new price values during negotiation. New values will require re-calculation of the utilities for both parties and we will use a simple approximation of piece-wise linear utilities. However, both the user and her counterpart will be able to modify their preferences, if they wish to do so. Further, we plan to introduce an option to add values for the discrete issues. In this case, both users will have to specify the relative preference for the new value.

Issues themselves may be introduced or removed dynamically during the course of the negotiation.

![](/api/attachments/WE9KWB2S/fulltext/images/ac5da8e8f0ddd06fc9d9a2a58b22943e191bb1d87438066be35917fc1af146bf.jpg)  
Fig. 12. Pareto-optimal offers that dominate the compromise.

Allowing the two negotiators to dynamically define the set of negotiable issues at the beginning requires Ž . 1 value focused analysis to be performed as a pre-negotiation step by the individual negotiators, and 2 a new initial protocol during which the issuesŽ . are proposed and negotiated by all the parties.

We also plan to enhance the pre-negotiation phase with support for specification of reservation levels and the best alternative to a negotiated agreement Ž . BATNA . Once these two constructs have been elicited from the user, the system will flag any offer or counter-offer that violates either the BATNA or any of the reservation levels. Further planned enhancements include context-sensitive advice; users will be able to obtain information explaining their opponent’s behavior, assistance in interpreting offers, suggestions regarding available strategies, etc.

An important factor that we have observed as influencing the negotiation process in INSPIRE is the availability of means for exchanging different kinds of structured objects during communication between the negotiators e.g., formally specified of-Ž fers vs. free-text messages . INSS will be enhanced. with facilities to transfer price lists, balance sheets and other multimedia documents such as pictures and video clips.

## Acknowledgements

We wish to acknowledge the contributions of John Bowen, David Cray, Anantha Mahadevan, Kumudini Ponnudurai and Ravi Ramsaran, the co-developers of the InterNeg site. The authors also thank the anonymous reviewers for their valuable comments and suggestions. This work has been supported by the Social Science and Humanities Research Council of Canada, the Natural Sciences and Engineering Research Council of Canada, and the International Institute for Applied System Analysis.

## References

<sup>w</sup> <sup>x</sup> 1 N.J. Adler, Cross-cultural management research: the ostrich and the trend, Academy of Management Review 8 4 1983Ž . Ž . 226–232.

<sup>w</sup> <sup>x</sup>2 N.J. Adler, J.L. Graham, Cross-cultural interaction: The international comparison fallacy? Journal of International Business Studies, 1989 515–537.Ž .

<sup>w</sup> <sup>x</sup> 3 M.G. Angur, V. Lotfi, J. Sarkis, A hybrid conjoint measurement and bi-criteria model for a two group negotiation problem, Socio-Economic Planning Sciences 30 3 1996Ž . Ž . 195–206.

<sup>w</sup> <sup>x</sup> 4 S. Ba, R. Kalakota, A. Whinston, Using client–broker architecture for intranet decision support, Decision Support Systems 19 1997 171–192.Ž .

<sup>w</sup> <sup>x</sup> 5 P. Balakrishnan, J. Eliashberg, An analytical process model of two-party negotiations, Management Science 41 2 1995Ž . Ž . 226–243.

<sup>w</sup> <sup>x</sup> 6 M.A. Bazerman, M.A. Neale, Negotiator rationality and negotiator cognition: the interactive roles of prescriptive and prescriptive research, in: H.P. Young Ed. , NegotiationŽ . Analysis, The University of Michigan Press, 1991, pp. 109– 130.

<sup>w</sup> <sup>x</sup> 7 I. Ben-Shaul, S. Ifergan, WebRule: An Event-based Framework for Active Collaboration Among Web Server, Hyper Proceedings of the Sixth International World Wide Web Conference, http:<sup>rr</sup>www6.nttlabs.com<sup>r</sup>HyperNews<sup>r</sup>get<sup>r</sup> PA-PER45.html downloaded August 10, 1997 , 1996.Ž .

<sup>w</sup> <sup>x</sup> 8 H.K. Bhargava, R. Krishnana, R. Miller, Decision support on

demand: emerging electronic markets for decision technologies, Decision Support Systems 19 1997 193–214. Ž .

<sup>w</sup> <sup>x</sup> 9 M.H. Bond, Chinese values and the search for culture-free dimensions of culture: The chinese culture connection, Journal of Cross-Cultural Psychology, 1987.

<sup>w</sup> <sup>x</sup> 10 T.X. Bui, Negotiation processes, evolutionary systems-design, and negotiator, Group Decision and Negotiation 5 Ž . Ž .4–6 1996 339–353.

<sup>w</sup> <sup>x</sup> 11 P.J. Carnevale, Property, culture, and negotiation, in: R.M. Kramer, D.M. Messick Eds. , Negotiation as a Social Pro-Ž . cess, Sage, 1995, pp. 309–323.

<sup>w</sup> <sup>x</sup> 12 R. Cohen, Negotiating Across Cultures, Communication Obstacles on International Diplomacy, Washington, DC, United States Institute of Peace Press, 1991.

<sup>w</sup> <sup>x</sup> 13 T.A. Darling, J.L. Mumpower, Simulating process and outcome for two-party contract negotiations, Control and Cybernetics 21 1 1992 151–184.Ž . Ž .

<sup>w</sup> <sup>x</sup> 14 L. Fang, K.W. Hipel, D.M. Kilgour, Interactive decision making, The Graph Model for Conflict Resolution, New York, Wiley, 1993.

<sup>w</sup> <sup>x</sup> 15 G.O. Faure, Negotiation concepts across cultures—implementing nonverbal tools, Negotiation Journal 9 4 1993Ž . Ž . 355–359.

<sup>w</sup> <sup>x</sup> 16 G. Fisher, International Negotiation. A Cross-Cultural Perspective, Intercultural Press, Yarmouth, MA, 1980.

<sup>w</sup> <sup>x</sup> 17 R. Fisher, W. Ury, Getting to Yes Negotiating Agreement Without Giving In, Penguin Books, New York, 1983.

<sup>w</sup> <sup>x</sup> 18 J.L. Graham, A.T. Mintu, W. Rogers, Explorations of negotiation behaviors in ten foreign cultures using a model developed in the United States, Management Science 40 1Ž . Ž . 1994 72–95.

<sup>w</sup> <sup>x</sup> 19 P.E. Green, On the design of choice experiments involving multifactor alternatives, Journal of Consumer Research 1 Ž . 1974 61–68.

<sup>w</sup> <sup>x</sup> 20 P.E. Green, Y. Wind, Multiattribute Decisions in Marketing: A Measurement Approach, The Dryden Press, Hinsdale, IL, 1973.

<sup>w</sup> <sup>x</sup> 21 P.H. Gulliver, Disputes and Negotiations: A Cross-Cultural Perspective, Academic Press, Orlando, FL, 1979.

<sup>w</sup> <sup>x</sup> 22 M.A. Hamilton, Java and the shift to net-centric computing, IEEE Computer 29 8 1996 31–39.Ž . Ž .

<sup>w</sup> <sup>x</sup> 23 K.W. Hipel, N.M. Fraser, Cooperation in conflict analysis, Applied Mathematics and Computation 43 1991 181–206.Ž .

<sup>w</sup> <sup>x</sup> 24 G. Hofstede, Cultural predictors of negotiation styles, in: F. Mautner-Markhof Ed. , Process of International Negotia-Ž . tions, Westview Press, 1989, pp. 193–201.

<sup>w</sup> <sup>x</sup> 25 C.W. Holsapple, H. Lai, A.B. Whinston, Analysis of negotiation support system research, Journal of Computer Information Systems 35 3 1995 2–11.Ž . Ž .

<sup>w</sup> <sup>x</sup> 26 C.W. Holsapple, H. Lai, A.B. Whinston, Implications of negotiation theory for research and development of negotiation support systems, Group Decision and Negotiation 6 3Ž . Ž .1997 255–274.

<sup>w</sup> <sup>x</sup> 27 F.C. Ikle, N. Leites, Political negotiation as a process of modifying utilities, Conflict Resolution 6 1 1962 19–28.Ž . Ž .

<sup>w</sup> <sup>x</sup> 28 M.T. Jelassi, B.H. Jones, Getting to yes with NSS: how computers can support negotiation, in: A.M.M.R.M. Lee, P.

Migliarese Eds. , Organizational Decision Support Systems, Ž . North-Holland, 1988, pp. 75–85.

<sup>w</sup> <sup>x</sup> 29 G.E. Kersten, NEGO—group decision support system, Information and Management 8 5 1985 237–246.Ž . Ž .

<sup>w</sup> <sup>x</sup> 30 G.E. Kersten, Support for group decisions and negotiations. An overview, in: J. Climaco Ed. , Multicriteria Analysis,Ž . Springer-Verlag, 1997, pp. 332–346.

<sup>w</sup> <sup>x</sup> 31 G.E. Kersten, T. Szapiro, Generalized approach to modeling negotiations, European Journal of Operational Research 26 Ž . Ž . 1 1986 142–149.

<sup>w</sup> <sup>x</sup> 32 G.E. Kersten, W. Michalowski, S. Szpakowicz et al., Restructurable representations of negotiation, Management Science 37 10 1991 1269–1290.Ž . Ž .

<sup>w</sup> <sup>x</sup> 33 V.A. Kremenuk Ed. , International Negotiations, Analysis,Ž . Approaches, Issues, Jossey-Bass, San Francisco, CA, 1991.

<sup>w</sup> <sup>x</sup> 34 D.A. Lax, J. Sebenius, The Manager as Negotiator, The Free Press, New York, 1986.

<sup>w</sup> <sup>x</sup> 35 C. Lockhart, Bargaining in International Conflicts, Columbia Univ. Press, New York, NY, 1979.

<sup>w</sup> <sup>x</sup> 36 W. Michalowski, G.E. Kersten, Z. Koperczak, et al., Negotiation with a terrorist: can an expert system help? in: M.G. Singh, K.S. Hindi, D. Salasa Eds. , Managerial Decision Ž . Support Systems, North-Holland, 1988, pp. 193–200.

<sup>w</sup> <sup>x</sup> 37 D.C. Montgomery, Design and Analysis of Experiments, Wiley, New York, 1997.

<sup>w</sup> <sup>x</sup> 38 J.D. Nyhart, D.K. Samarasan, The Elements of Negotiation Management, International System Dynamics Conference, 1990.

<sup>w</sup> <sup>x</sup> 39 D.G. Pruitt, Negotiation Behavior, Academic Press, New York, 1981.

<sup>w</sup> <sup>x</sup> 40 D.G. Pruitt, Process and outcome in community mediation, Negotiation Journal 11 4 1995 365–377. Ž . Ž .

<sup>w</sup> <sup>x</sup> 41 H. Raiffa, The Art and Science of Negotiation, Harvard Univ. Press, Cambridge, MA, 1982.

<sup>w</sup> <sup>x</sup> 42 A. Rangaswamy, G.R. Shell, Using computers to realize joint gains in negotiations: toward an ‘Electronic Bargaining Table’, Management Science 43 8 1997 1147–1163.Ž . Ž .

<sup>w</sup> <sup>x</sup> 43 A.E. Roth, V. Prasnikar, M. Okuno-Fujiwara et al., Bargaining and market behaviour in Jerusalem, Ljubljana, Pittsburgh, and Tokyo: an experimental study, The American Economic Review 81 5 1991 1068–1095.Ž . Ž .

<sup>w</sup> <sup>x</sup> 44 H. Sakagami, T. Kamba, Learning Personal Preferences on Online Newspaper Articles from User Behavior, Hyper Proceedings of the Sixth International World Wide Web Conference, http:<sup>rr</sup>www6.nttlabs.com<sup>r</sup>Hy-perNews<sup>r</sup>get<sup>r</sup>PA-PER142.html downloaded August 10, 1997 , 1996.Ž .

<sup>w</sup> <sup>x</sup> 45 J.K. Sebenius, Negotiation analysis: a characterization and review, Management Science 38 1 1992 18–38.Ž . Ž .

<sup>w</sup> <sup>x</sup> 46 R.H. Sprague, H.J. Watson, Decision Support for Management, Upper Saddle River, Prentice-Hall, NJ, 1997.

<sup>w</sup> <sup>x</sup> 47 J.E. Teich, H. Wallenius, J. Wallenius, Advances in negotia-

tion science, Transactions in Operational Research 6 1994 Ž . 55–94.

<sup>w</sup> <sup>x</sup> 48 W. Ury, Getting Past No. Negotiating your Way from Confrontation to Cooperation, Bantam Books, New York, 1993.

<sup>w</sup> <sup>x</sup> 49 T.L. Watson, Network-centric computing, Software SQ. IBM Corporation 31 1 1996 http: Ž . Ž . <sup>rr</sup>www<sup>r</sup>software.ibm.com<sup>r</sup> sq<sup>r</sup>enu<sup>r</sup>issues<sup>r</sup>vol31<sup>r</sup>ncc.html.

<sup>w</sup> <sup>x</sup> 50 A.P. Wierzbicki, The role of multiobjective optimization in negotiation and mediation support, Theory and Decision 34 Ž . Ž . 3 1993 201–214.

<sup>w</sup> <sup>x</sup> 51 G.R. Winham, Simulation for teaching and analysis, in: V. Kremenuk Ed. , International Negotiations, Analysis, Ap- Ž . proaches, Issues, Jossey-Bass, 1991, pp. 409–423.

<sup>w</sup> <sup>x</sup> 52 H.P. Young Ed. , Negotiation Analysis, Ann Arbor, TheŽ . University of Michigan Press, 1991.

<sup>w</sup> <sup>x</sup> 53 I.W. Zartman, Decision-support and negotiation research—a researchers perspective, Theory and Decision 34 3 1993Ž . Ž . 345–351.

![](/api/attachments/WE9KWB2S/fulltext/images/4f22e345217c9c8dc7199bec82d0cca97863ed22a719191103fdc82d4ecf5fb0.jpg)

Gregory E. Kersten is a professor of decision sciences and information systems at the School of Business and the Director of the Centre for Computer Assisted Management at Carleton. In 1997–1998, he was a senior research scholar at the International Institute for Applied Systems Analysis in Austria. He is a Vice-Chairperson of the IN-FORMS Group Decision and Negotiation College, a departmental editor of the Group Decision and Negotiation

Journal and member of the editorial boards of Decision Systems, INFOR, and Control and Cybernetic. His research interests include decision-making, negotiations, artificial intelligence, and decision support. He has written over 80 refereed papers. He is the principal investigator of the InterNeg project with objectives to build web-based decision and NSS and to study their use in training and e-commerce.

Sunil J. Noronha received his B.Tech in Electrical Engineering from the Indian Institute of Technology, Madras, in 1987 and his PhD from the Computer Science and Automation Department of the Indian Institute of Science, Bangalore, in 1993. In 1994 he joined Carleton University’s School of Business as a postdoctoral fellow and worked on the Negoplan and InterNeg projects on negotiation support. Since June 1997 he is a Research Staff Member at IBM’s T.J. Watson Research Center, Yorktown Heights, New York. His research interests include topics in artificial intelligence, decision support systems, data mining and electronic commerce. Dr. Noronha is a member of the IEEE, ACM and INFORMS.
