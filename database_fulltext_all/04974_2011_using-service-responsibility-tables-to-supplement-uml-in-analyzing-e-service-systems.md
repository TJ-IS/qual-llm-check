---
otero_id: 4974
otero_key: "8ADAXHUQ"
title: "Using service responsibility tables to supplement UML in analyzing e-service systems"
authors: "Xin Tan; Steven Alter; Keng Siau"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.01.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using service responsibility tables to supplement UML in analyzing e-service systems Xin Tan <sup>a,1</sup>, Steven Alter <sup>b,2</sup>, Keng Siau <sup>c,</sup>⁎

<sup>a</sup> Fairleigh Dickinson University, 1000 River Road, H-DH2-06, Teaneck, NJ 07666, United States

<sup>b</sup> University of San Francisco, 2130 Fulton Street, MH-314, San Francisco, CA 94117-1045, United States

<sup>c</sup> University of Nebraska-Lincoln, 209 CBA, Department of Management, Lincoln, NE 68588-0491, United States

## a r t i c l e i n f o

Article history: Received 10 May 2009 Received in revised form 16 January 2011 Accepted 16 January 2011 Available online 21 January 2011

Keywords: Systems analysis and design Work system method Service responsibility table Uni<sup>fi</sup>ed modeling language

## a b s t r a c t

This paper proposes using Service Responsibility Tables (SRTs) as a tool in analyzing e-service systems. First it discusses dif<sup>fi</sup>culties and de<sup>fi</sup>ciencies of using formal modeling languages such as UML in analyzing e-service systems. It proposes using SRTs as an informal language and lightweight analytical tool to be used by business professionals in analyzing e-service systems. SRTs are based on a service value chain framework but do not rely on abstract concepts and constructs, and therefore can be used by business professionals to supplement UML. We suggest a set of heuristics for transforming SRTs into two key UML diagrams, thereby illustrating how SRTs can be used as a bridge from relatively informal modeling by business professionals to formal modeling techniques for systems design and implementation by IT professionals

© 2011 Elsevier B.V. All rights reserved

## 1. Introduction

The advent of the Internet and other modern information and communication technologies (ICTs) has led businesses worldwide to embrace e-commerce and e-service. E-commerce has been widely accepted as a viable business model for buying and selling products/ services over the Web, leading to a new paradigm known as e-service, or electronic service, de<sup>fi</sup>ned as the provision of service over electronic networks [42]. Common examples of such e-service include online package tracking, email noti<sup>fi</sup>cation of order status, and more recently mobile banking. The advantages of providing customers with e-service include reducing operating expenses, allowing for personalization, and improving customer satisfaction [8,40]. Through eservice, enhanced service experience and higher levels of customer satisfaction tend to increase revenues and pro<sup>fi</sup>tability [42]. For customers, the bene<sup>fi</sup>ts of e-service include addressing new business needs, saving money and time in traveling, and avoiding awkward interpersonal encounters [32].

Whereas e-service systems may offer many bene<sup>fi</sup>ts to businesses and their customers, developing e-service systems is challenging [56]. E-service is predominately self-service [40]. In other words, customer use of e-service systems implies coproduction of service, frequently requiring customers to engage in new behaviors [33]. There is a general agreement on the importance of user involvement during systems analysis and design [10,55].

The self-service nature of e-service poses several dif<sup>fi</sup>culties in effectively involving users' participation in systems analysis and design stages. First, ordinary customers, i.e. the intended users of e-service systems, often have dif<sup>fi</sup>culty identifying and describing the capabilities and features they want [33]. Even if the system totally re<sup>fl</sup>ects what they requested, it often omits important capabilities that the users failed to request [34].

Second, formal requirements modeling methods, such as Uni<sup>fi</sup>ed Modeling Language (UML), are frequently used to create requirements representations that need users' review and approval [22]. Such formal notations are dif<sup>fi</sup>cult to understand for people with little or no technology background [25]. Users have dif<sup>fi</sup>culty verifying the accuracy and completeness of requirements models that are presented in formalisms that are unfamiliar to them at best, and sometimes seem impenetrable to typical business professionals.

This paper proposes Service Responsibility Tables (SRTs) as tools that business professionals and service customers can use in the analysis stage of e-service system development. The idea of SRTs came from service-related extensions of work system research [2,4], which has focused for over a decade on developing lightweight systems analysis tools for business professionals. The form of SRTs is based on the structure of the service value chain framework [4,6,7]. Tan, Alter, and Siau [57] propose that the use of SRTs might alleviate dif<sup>fi</sup>culties in analyzing e-service systems by helping users and analysts summarize and discuss important elements and processes involved in service provision. In comparison with formal modeling methods, SRTs are easier to use by business professionals who typically have little or no knowledge of the heavyweight analytical tools. SRTs can help them devote their cognitive effort to eliciting and identifying requirements in e-service systems, instead of making sense of the syntax and grammar of formal modeling languages.

We are not proposing that SRTs should replace UML, which is the de facto modeling standard of the software development community [21]. Instead, we propose to use SRTs as a lightweight analytical tool for business professionals. The resulting SRTs can be transformed to rigorous UML diagrams by analysts who are able to <sup>fi</sup>ll in missing details needed to produce syntactically and substantively correct UML diagrams. We suggest using a set of heuristics to facilitate the transformation from SRTs to UML diagrams.

The rest of the paper is organized as follows. The <sup>fi</sup>rst section introduces common cognitive problems that can affect requirements modeling, and explains why some of these problems are heightened in e-service systems analysis. The objective is to clarify the dif<sup>fi</sup>culties of applying formal modeling methods in the analysis stage. The second section provides background on a <sup>fl</sup>exible class of analysis tools called SRTs, and explains how they can be used as lightweight analysis tools for business professionals and analysts. The third section summarizes initial heuristics for transforming SRTs into UML diagrams for documenting requirements. The usefulness of the heuristics is illustrated through a case. The conclusion section discusses the implications of the present study for research and practice, and highlights the directions for future research.

## 2. Related literature

Eliciting and documenting users' requirements for the system being built are crucial activities in system development projects. Despite the general agreement on the importance of user involvement during systems analysis and design, the level and quality of user involvement are often inadequate [30,31]. This section reviews related literature to summarize common problems in eliciting and documenting users' requirements. It also surveys the literature related to e-service to reveal the additional problems in using formal modeling methods in e-service systems analysis. It concludes with the features of a novice-friendly analytical tool to supplement UML for e-service systems analysis.

## 2.1. Common problems in requirements determination

One of the key objectives of systems analysis and design is to determine users' information requirements. Being able to understand users' information requirements is vital in any software project and a key factor in any successful software implementation [11–13,17]. Information requirements determination is a set of activities performed by systems analysts to assess the functionality required in a proposed system. According to Pohl [38], requirements determination involves four tasks that are often performed iteratively in practice:

i. Requirements speci<sup>fi</sup>cation: to understand the organizational situation that the system under consideration aims to improve and describe the needs and constraints of the system under development.

ii. Requirements negotiation: to establish an agreement on the requirements of the system among the various stakeholders involved in the process.

iii. Requirements representation: to develop a mapping of realworld needs onto a requirements model.

iv. Requirements validation: to ensure that the derived speci<sup>fi</sup>cation corresponds to the original stakeholder needs and conforms to the internal and/or external constraints set by the enterprise and its environment.

Requirements determination for information systems is a highly communicative, iterative, and creative activity. Holtzblatt and Beyer [28] claim that the success of information requirements determination depends on how well people communicate and understand each other. Davis [16] summarizes four sources of dif<sup>fi</sup>culties in information requirements determination: (1) the constraints on humans as information processors and problem solvers, (2) the variety and complexity of information requirements, (3) the complex patterns of interaction among users and analysts in de<sup>fi</sup>ning requirements, and (4) the unwillingness of users to provide requirements. Valusek and Fryback [59] label these dif<sup>fi</sup>culties as communication obstacles “within” individual users, “among” users, and “between” users and analysts. More recently, Siau and Tan [48,49] elaborate further on the cognitive underpinnings of such communication problems in the context of conceptual modeling and requirements determination.

Frames of reference held by organization members are implicit guidelines that serve to organize and shape their interpretation of events and organizational phenomena, as well as to give meaning to it [62]. Inconsistent frames of reference among stakeholders may lead to communication problems in systems analysis and design. Cognitive inef<sup>fi</sup>cacy during systems analysis also may lead to inaccurate or incomplete requirements. In relation to systems development and use, Orlikowski and Gash [35] label such frames of reference as technological frames that are vital in understanding of the variety and complexity of user needs. For instance, analysts must manage the subjective nature of language to disseminate technology to users in a non-technical way. On the other hand, analysts often organize, classify, describe, and explain complex processes and concepts in a highly technical manner.

## 2.2. Nature of e-service systems

Businesses and non-pro<sup>fi</sup>t organizations have started embracing e-service to deliver service to their customers through electronic networks, although there is a lack of agreement on the de<sup>fi</sup>nition of e-service [40]. In this research, we de<sup>fi</sup>ne e-service as:

Acts or performances that are delivered through electronic devices and networks to help people complete tasks, solve problems, or conduct transactions.

A review of e-service literature [40] identi<sup>fi</sup>es two inherent characteristics of e-service: information service and self-service. Information service refers to the assumption that information is the primary value exchanged between the two parties in an e-service relationship. Further, an e-service experience is a self-service experience [40], or customer coproduction of service [33]. Some researchers claim that “selling tangible goods online is itself an e-service that substitutes for physical retailing” [27].

These characteristics lead to challenges in developing and implementing e-service systems. First, the self-service nature of e-service has a high demand for customer engagement and learning [33,40]. Second, because e-service is typically conceptualized as information service, the dimensions of information quality, as well as non-technological features such as trust, reliability, and risk, should be considered as part of comprehensive requirements for e-service systems.

## 2.3. Why UML by itself is not sufficient for e-service systems analysis

With the dominance of object-oriented paradigm in information systems development, object-oriented modeling is expected to play an increasingly important role in requirements engineering. Consistent with this trend, UML has emerged as a de facto standard for object-oriented modeling language [21,22,29]. UML is a graphical modeling language for modeling system requirements, describing design artifacts, and specifying implementation details. The current UML speci<sup>fi</sup>cation (version 2.2) de<sup>fi</sup>nes thirteen types of diagrams, which can be applied for specifying, visualizing, and documenting models of software systems in various development phases. Some of the diagrams, such as class diagrams, use case diagrams, and activity diagrams, are used for capturing and analyzing an application's requirements [9,41].

Object-oriented requirements engineering is a relatively new area in object-oriented information systems development. Relatively few empirical studies have investigated how practitioners use UML for requirements engineering in organizational contexts. Dawson and Swatman [18] investigate how object-oriented modeling methods are used by practicing professionals in requirements engineering. Based on a case study, Glinz [25] identi<sup>fi</sup>es several de<sup>fi</sup>ciencies of UML as a language for requirements speci<sup>fi</sup>cation. In other research, Siau and Lee [45] investigate the possible synergetic values and relationships between the use case and class diagrams in the context of requirements analysis. Dobing and Parsons [21] survey the use of UML diagrams by practitioners.

A literature survey revealed several critical insuf<sup>fi</sup>ciencies of UML for requirements determination.

i. Although UML is a language with rigorous grammar and syntax, it is not a development methodology [21]. Guidelines for applying UML are inconsistent across different development settings [20,23]. Without a sound methodology as the frame of reference, the communication obstacles identi<sup>fi</sup>ed above tend to have a negative impact on the accuracy and comprehensiveness of requirements determination.

ii. UML is a complex modeling language [44,51]. It is easy for novice developers and analysts to be overwhelmed by the various graphical notations and associated object-oriented concepts [1,46]. Business professionals and ordinary users typically <sup>fi</sup>nd the formal models much too complex, both conceptually and technically [18]. These language problems pose dif<sup>fi</sup>culties in various parts of requirements negotiation and requirements validation.

iii. The recommended diagrams for modeling requirements suffer from de<sup>fi</sup>ciencies related to accurate representation of requirements [50], especially non-functional requirements [25]. Such semantic de<sup>fi</sup>ciencies may lead to incomplete representation of functional and non-functional requirements [23].

Table 1 summarizes speci<sup>fi</sup>c problems caused by solely using UML for requirements determination for e-service systems.

In view of the de<sup>fi</sup>ciencies of UML, we propose that additional analytical tools should be adopted in requirements determination for e-service systems analysis and design. For better analysis outcomes, such tools should supplement UML by meeting the following needs:

First, the analytical tools should be embedded in a sound framework in e-service contexts. Such a framework would provide a frame of reference that helps service providers, customers, managers, and analysts explore different elements and processes of service provision, and generate comprehensive requirements.

Second, the analytical tools should alleviate learning dif<sup>fi</sup>culties for business professionals and customers by providing an informal speci<sup>fi</sup>cation language. Such lightweight analytical tools should be easy to learn and should make sense to people who are familiar with service contexts but not necessarily technical and modeling concepts. This approach is consistent with recommendations from many practitioners and researchers [11,18,49].

Third, the analytical tools should be <sup>fl</sup>exible enough to capture non-functional requirements related to the dimensions of information quality and other factors such as trust and security. In this way, the analytical tools can supplement UML to generate a comprehensive summary of users' functional or non-functional requirements.

Table 1  
Problems in solely using UML for requirements determination for e-service systems

<table><tr><td rowspan="2">Requirements determination task</td><td colspan="2">Characteristics of e-service systems</td></tr><tr><td>Self-service/customer coproduction</td><td>Information service and non-functional concerns</td></tr><tr><td>Requirements specification</td><td>As a modeling language, UML does not provide a sound frame of reference for service providers and customers to identify requirements in e-service context.</td><td>As a modeling language, UML does not provide sufficient semantics to specify different dimensions of information quality, as well as certain non-functional requirements in an e-service context.</td></tr><tr><td>Requirements negotiation</td><td>UML models are too complex for service providers and customers to understand, therefore causing difficulty in requirements negotiation.</td><td>Insufficient semantics may cause difficulties in negotiating non-functional requirements.</td></tr><tr><td>Requirements representation</td><td>The complexity of UML makes it difficult for service providers and customers to participate effectively in requirements representation.</td><td>Insufficient semantics may cause difficulties representing complete requirements and/or the omission of non-functional requirements.</td></tr><tr><td>Requirements validation</td><td>UML models are too complex for service providers and customers to understand, therefore causing difficulty in validating requirements by e-service users</td><td>Insufficiency in representation semantics may make it difficult for users to validate the requirements.</td></tr></table>

In summary, the suggested supplementary tools should facilitate lightweight analysis by users. These tools should help them think through their own views of IT-reliant work systems, and should help them understand the business situation and potential implications of any proposed change regarding process <sup>fl</sup>ow, information usage, and aspects of software and hardware that are visible to users and their colleagues. These tools should help users conduct lightweight analysis with or without the help of IT professionals. These tools should generate an understanding that supports heavyweight analysis and design performed by systems analysts and other IT professionals while building software. The lightweight analysis should complement and supplement heavyweight techniques that are used for formal documentation of requirements and for designing and implementing IT-based solutions.

We believe that Service Responsibility Tables (SRTs) are a good example of an analytical tool that business professionals can use in lightweight analysis of e-service systems. The following section provides background about SRTs as an analytical tool.

## 3. Service value chain and Service Responsibility Tables

The general goal of supporting lightweight analysis by business professionals motivated development of the work system approach for understanding and analyzing IT-reliant systems in organizations. Its basic assumption is that most systems in organizations can be viewed and analyzed as work systems rather than as business processes, computer systems, or tools that are used by individuals. Additional information about work system framework and work system method can be found in Appendix A. In this section, we focus on the theoretical foundation of our proposed analytical tool.

The evolution of the work system method has generated a number of concepts, frameworks, and tools including the work system framework, work system life cycle model, work system snapshot, and work system principles, all of which have been described in prior literature [2,3,5–7]. More recently, widespread interest and concern about services and the service economy led to extensions of the work system approach to incorporate issues and characteristics related to services. The main products to date of those efforts are the service value chain framework and Service Responsibility Tables [4,6].

## 3.1. Service value chain framework

Noting the increasing importance of services in the economy in general and for technology companies in particular, IBM joined with other technology companies in a major initiative to develop university courses of study related to service and to develop “service science” [15,54]. Motivations for this initiative included the long term need to hire employees who can succeed in a service economy and the belief that many practical and theoretical ideas related to service are not yet well developed.

The effort to develop service science motivated an effort to introduce service concepts into the work system method in a more direct way. In an attempt to incorporate service concepts more completely, recent extensions of the work system approach incorporated additional issues and characteristics related to services. The service value chain framework (Fig. 1) depicts generic activities and responsibilities of both service providers and customers. These activities and responsibilities may occur before, during, and after delivery of a speci<sup>fi</sup>c service to a speci<sup>fi</sup>c customer. The form of the service value chain framework is based on the common observation that services tend to be co-produced by service providers and service consumers [60,61]. The service value chain framework includes a large number of concepts related to services, such as coproduction of value, value capture, service interactions, differentiation between back stage and front stage during the production and consumption of services, negotiations leading to service level agreements, provider and consumer preparation prior to instances of service delivery, negotiation of requests during speci<sup>fi</sup>c instances of service provision, service ful<sup>fi</sup>llment, and service follow-up [4,6,7].

## 3.2. Service Responsibility Tables

The work system approach was developed speci<sup>fi</sup>cally to help business professionals understand, evaluate, and analyze systems in organizations at any level of detail appropriate for their particular situation, regardless of whether IT plays a central role. Typically they would obtain help from IT professionals if changes in hardware and software might be needed. We believe that a practical, easily learned form of lightweight analysis for business professionals would be a good compromise between 1) assuming that they are incapable of analyzing anything in an organized manner and 2) assuming that the only legitimate form of analysis is precise, rigorous analysis needed to produce testable computer programs and IT systems.

![](/api/attachments/8ADAXHUQ/fulltext/images/b36c20fc54b0107f81e295d91687f3bba5686f91b5682ff4ba9f67e884e2433a.jpg)  
Fig. 1. Service value chain framework [6] slightly updated.

The two-sided format of the service value chain framework translates directly into a useful and <sup>fl</sup>exible analysis tool called a Service Responsibility Table (SRT). SRTs strip out the terminology about steps in services per se, and emphasize coproduction by identifying the (active or passive) responsibilities of both service providers and service consumers throughout a service process. Table 2 is an SRT corresponding to a loan application and underwriting system.

As shown in the <sup>fi</sup>rst two columns of Table 2, the simplest form of SRT resembles a two-column swimlane diagram, with one column for providers and one for customers, and with speci<sup>fi</sup>c provider and customer roles indicated clearly. The entries in the <sup>fi</sup>rst two columns of Table 2 are all activities, although some SRT entries can be responsibilities, such as a patient's responsibilities during a physical exam or a traveler's responsibilities during an airplane <sup>fl</sup>ight. It is easy

A Service Responsibility Table (SRT) example.

to extend a two-column SRT into a three-column SRT that adds a new column for any of a number of topics that might be important for analyzing a particular system. The third column in Table 2 identi<sup>fi</sup>es information used or generated at each step. Many other examples of topics for the third column are listed in Table 3.

An SRT (see Table 2) overlaps somewhat with a work system snapshot, a central tool in the work system method that consists of a one page summary of a work system based on six central elements of the work system framework (see Appendix). The preferred sequence in applying these tools is to use the work system snapshot to create agreement about the scope and outputs of the work system being studied, and then to use a sequence of SRTs to create a stronger customer focus and to introduce a series of topics such as information used or generated (as shown in Table 2), business rules at each step, important exceptions at each step, and so on.

The format of an SRT facilitates easy reuse as the analysis proceeds. For example, it is easy to generate a set of three-column SRTs by reusing the <sup>fi</sup>rst two columns and including in each additional SRT a new column for any of a number of topics that might be important for analyzing a particular system (see Table 2). Initial empirical evidence from classroom usage by MBA and EMBA students suggests that SRTs are potentially useful tools [4].

## 3.3. Advantages of Service Responsibility Tables

Use of an SRT early in an e-service system analysis has several advantages over using formal speci<sup>fi</sup>cation languages such as UML.

<table><tr><td>Provider activity or responsibility</td><td>Customer activity or responsibility</td><td>Information used or generated</td><td colspan="3">advantages over using formal specification languages such as UML.</td></tr><tr><td>Loan officer identifies businesses that might need a commercial loan.</td><td></td><td>Uses a company&#x27;s financial profile</td><td colspan="3">Table 3List of typical topics (by Step) for additional columns of an SRT.</td></tr><tr><td>Loan officer contacts potential loan applicant.</td><td>Potential loan applicant agrees to discuss the possibility of receiving a loan</td><td>Uses contact information of potential applicants</td><td>Topics related to problems or issues (by step)</td><td>Topics related to the system&#x27;s structure and requirements (by step)</td><td>Topics related to performance metrics (by step)</td></tr><tr><td>Loan officer discusses loan applicant&#x27;s financing needs and possible terms of the proposed loan.</td><td>Potential loan applicant discusses financing needs.</td><td>Generates initial loan application with financial terms such as amount, terms, interest rate, collaterals, etc.</td><td rowspan="8">Issues and problems participant or interpersonal issuesInformation issuesTechnology issuesConfusion or training issuesPoints of frictionReasons for delays, errors, reworkCommunication issuesConflicts with culture or policiesLegal or regulatory issuesExternal dependenciesConflicts with other systems</td><td rowspan="8">Goals and requirementsPre-conditionsTriggersBusiness rulesBusiness or legal constraintsPost-conditionsSpecial casesSignificant exceptionsAlternative paths or methodsKnowledge or skill requirements for participantsParticipant incentivesInformation usedInformation generatedTechnology usedProducts and services produced (and used in other systems by customers or provider organizations)Possibilities for changeThings that cannot changeBenefits provided to customers</td><td rowspan="8">Activity rateDuration (cycle time)Delay between stepsDefect rateRework rateDowntimeProvider costCustomer costCustomer complaintsInformation accuracyInformation timelinessInformation availabilityInformation securityTechnology performanceKey performance gaps for important steps (Gap = desired vs. current value of an important metric.)</td></tr><tr><td>Loan officer helps loan applicant compile a loan application</td><td>Loan applicant compiles loan application.</td><td>Generates formal loan application with financial termsUses loan application</td></tr><tr><td>Loan officer and senior credit officer meet to verify that the loan application has no glaring flaws.</td><td></td><td></td></tr><tr><td>Credit analyst prepares a “loan write-up” summarizing the client&#x27;s financial history, providing projections of sources of funds for loan payments, etc.</td><td></td><td>Generates loan write-up with details</td></tr><tr><td>Loan officer presents the loan write-up to a senior credit officer or loan committee.</td><td></td><td>Uses loan write-up</td></tr><tr><td>Senior credit officer or loan committee makes approval decision.</td><td></td><td>Uses loan write-up and loan application</td></tr><tr><td>Loan officer informs loan applicant of the decision</td><td>Loan applicant accepts or declines an approved loan.</td><td>Uses loan application</td></tr><tr><td>Loan administration clerk produces loan documents for an approved loan that the client accepts</td><td></td><td>Generates loan documents</td></tr></table>

i. It clari<sup>fi</sup>es scope and context of the process without requiring mastery of details that will be clari<sup>fi</sup>ed later in the analysis by using detailed representations of work<sup>fl</sup>ow and logic.

ii. It focuses attention on activities and responsibilities rather than on details of technology and information.

iii. It identi<sup>fi</sup>es the job roles that are involved.

iv. It brings customer responsibilities into the analysis.

v. It identi<sup>fi</sup>es service interactions (rows with both provider and customer responsibilities) and other steps that are not visible to customers.

The tabular structure of SRTs is also conducive to creation of various standard versions that can be de<sup>fi</sup>ned and used through database or spreadsheet software. For example, at the beginning of its systems analysis efforts, a particular <sup>fi</sup>rm might establish the common practice of using SRTs with the following third columns: problems, opportunities, and issues; key errors and exceptions; constraints; and recommended changes (if any) for each step. People in that <sup>fi</sup>rm would become accustomed to discussing a two-column SRT to de<sup>fi</sup>ne the scope of the system to be analyzed, and then using the additional SRTs as a starting point for exploring additional topics and issues.

Many additional variations are consistent with an SRT's basic structure. For example, if it is important to remember that certain groups of steps occur in parallel, it is possible to number the activities and use simple numerical conventions to indicate activities that occur in parallel. If it is important to record non-sequential precedence relationships in an SRT (rather than in other documentation), it is possible to add two numeric columns, one that numbers each activity and another that identi<sup>fi</sup>es one or more direct predecessors of each activity.

These features make SRTs potentially useful analytical tools to supplement UML in e-service systems analysis and design. SRTs satisfy the three previously mentioned criteria for an ideal lightweight analytical tool:

First, SRTs are derived from a sound theoretical foundation that combines work system ideas and the service value chain framework. In other words, SRTs are not just a speci<sup>fi</sup>cation language. Instead, SRTs are embedded in an analytical method that can be used to guide the comprehensive analysis of e-service system.

Second, SRTs potentially alleviate learning dif<sup>fi</sup>culties for business professionals and customers by providing an informal speci<sup>fi</sup>cation language without abstract symbols and obscure terminology. Business professionals and customers who are familiar with a particular service context can easily learn and apply the rules for constructing and understanding SRTs.

Third, SRTs are <sup>fl</sup>exible enough to capture non-functional requirements related to the dimensions of information quality and other factors such as trust and security. The mechanism is simply to add columns related to these topics, as shown in Table 2.

In summary, dif<sup>fi</sup>culties in using UML in e-service systems analysis and design can be alleviated by using SRTs as lightweight analytical tools for business professionals. To do that, however, it is necessary to bridge the gap between lightweight analysis and heavyweight analysis. The transformation of SRTs into UML diagrams is discussed next.

## 4. Transforming SRTs to UML diagrams

We propose using SRTs to supplement UML in e-service systems analysis, with SRTs supporting lightweight analysis by business professionals and UML continuing in its role as the de facto standard language for modeling in object-oriented development. Most objectoriented development methodologies, such as the Uni<sup>fi</sup>ed Process (UP), stipulate that UML diagrams constructed in systems analysis phase should be used later in the design and construction phases [19,43]. Using SRTs to supplement UML requires a way to transform

SRTs from lightweight analysis into key UML diagrams such as class diagrams and use case diagrams that are critical for the design and construction efforts.

The transformation from SRTs into UML diagrams builds upon prior studies that tried to bridge the gap between informal and formal representation languages [24]. We assume that the transformation will be accomplished by systems analysts guided by heuristics for creating initial transformations and then <sup>fi</sup>lling in missing details that might not have been articulated in the initial, lightweight analysis. To demonstrate this approach, we present two sets of heuristics. One transforms SRTs into use case diagrams. The other is used to create class diagrams.

## 4.1. Transforming an SRT into a use case diagram

System analysts employ use case diagrams to model information requirements. Each use-case describes an element of the functionality of a software system that generates value for users. The sum of these use-cases de<sup>fi</sup>nes the total functionality of the software system. Usecase diagrams are the cornerstones in the UML-based development. For example, UP is use-case centric. The following heuristics can be used to transform an SRT into a use case diagram for further analysis:

i. Identify the various types of service providers and customers in an SRT and consider them as actors in a use case diagram.

ii. Identify the various activities and responsibilities associated with each type of service provider and customer. These activities and responsibilities can be regarded as candidates for use cases in a use case diagram.

iii. Based on the expected functionalities, decide which use cases should be included in the use case diagram.

iv. Link actors with corresponding use cases; show “extends” or “includes” relationships among use cases based on the SRT.

Following these heuristics, the SRT (as shown in Table 2) can be used to generate a use case diagram. In particular, the transformation followed these steps:

i. Loan of<sup>fi</sup>cer, loan applicant, credit analyst, senior loan of<sup>fi</sup>cer, and loan administration clerk are identi<sup>fi</sup>ed in the SRT (Table 2) and these can be regarded as actors in the use case diagram.

ii. Primary activities and responsibilities in the SRT are summarized into

a. identify potential loan applicants,

b. contact potential loan applicants,

c. discuss <sup>fi</sup>nancing needs,

d. compile loan application,

e. verify loan application,

f. prepare loan write-up,

g. make approval decision, and

h. produce loan documents.

These will be treated as candidates of use cases in the use case diagram.

iii. Considering the expected functionalities of the software system supporting loan approval, “identify potential loan applicants” and “contact potential loan applicants” are excluded from the list of use cases. These activities are considered to be outside the scope of the software system for loan approval. As a result, six use cases are identi<sup>fi</sup>ed from the SRT.

iv. Link the identi<sup>fi</sup>ed use cases with corresponding actors based on the descriptions in the SRT. The use case “Produce loan documents” can be carried out only when “Make approval decision” is completed. Thus, there is an “extends” stereotype between the two use cases.

The resulting use case diagram is shown in Fig. 2.

![](/api/attachments/8ADAXHUQ/fulltext/images/3ddb0be24a419ef5d30be4ca237f5d6328b24a660e84f83420ac3b7ee44007c9.jpg)  
Fig. 2. A use case diagram transformed from the SRT for a loan approval system.

## 4.2. Transforming an SRT into a class diagram

A domain model describes the important things and concepts associated with a system. In UML, these things and concepts are represented as classes and the various kinds of relationships among them. The UML class diagram is used for capturing the contents of the domain model [43]. If we extend the SRT to contain a third column titled “information used or generated”, that third column can be translated into a UML class diagram by using the following heuristics:

i. Identify all the objects mentioned in the three columns of SRT and determine the objects about which the software system will track or maintain information. These will be considered as classes.

ii. Decide the names of classes and the relationships among them.

iii. Identify the attributes for each class using the contents in the third column of the SRT.

iv. Fill in missing classes, attributes, and relationships by further analysis.

Following the above heuristics, the sample SRT (as shown in Table 2) can be used to generate a UML class diagram through several steps:

i. Among all the objects mentioned in the SRT, client company, loan applicant, loan application, loan write-up, loan of<sup>fi</sup>cer, loan analyst, and senior loan of<sup>fi</sup>cer are the objects about which the software system will record information. They are the candidates for classes.

ii. Using the descriptions in the SRT, the individual classes will be connected through associations. For instance, “loan of<sup>fi</sup>cer” will be associated with “loan application,” while “loan applicant” (as a person) is a part of “client company,” thus an aggregation relationship.

iii. For each class, the attributes will be identi<sup>fi</sup>ed using the contents in the third column in the SRT. For instance, “loan application” has attributes consisting of <sup>fi</sup>nancial terms such as amount, terms, interest rate, and collateral.

iv. All classes that are a type of person will be a subclass of the “person” class. The relationships between person and its subclasses are generalization.

The class diagram in Fig. 3 was produced from the SRT in Table 1 by using the above heuristics.

## 5. Implications for research

To address some of the dif<sup>fi</sup>culties of using UML in e-service systems analysis, we propose the use of SRTs as a lightweight analytical tool that is understandable and usable by business professionals. The use of SRTs can supplement the use of UML by helping business professionals interpret a problem domain and identify signi<sup>fi</sup>cant issues. The diagnostic qualities of the SRTs generate advantages that warrant future study.

![](/api/attachments/8ADAXHUQ/fulltext/images/bfc97e27f843500cbd53f3323b357f44fda90ce898fa2a65f71d78a5825e8cca.jpg)  
Fig. 3. A class diagram transformed from the SRT for a loan approval system.

i. SRTs help in focusing attention on signi<sup>fi</sup>cant issues.

The quality and ef<sup>fi</sup>ciency of systems analysis and information requirements determination is often reduced by the cognitive limitations of people as information processors and problem solvers. For instance, representativeness bias refers to an individual's tendency to generalize from samples that are too small for population. Similarly, availability bias leads people to estimate the frequency of events based on the ease with which instances are recalled from memory [10,59]. By focusing attention on signi<sup>fi</sup>cant issues, SRTs can help in counteracting cognitive limitations and biases of individual business professionals.

ii. SRTs can help trigger memory and encourage deep re<sup>fl</sup>ection. Tendencies toward satis<sup>fi</sup>cing and automaticity are additional limitations of people as information processors and problem solvers. In satis<sup>fi</sup>cing, people tend to be satis<sup>fi</sup>ed with a problem solution that is “good enough” and do not aim for an optimal solution [52]. Automaticity refers to the dif<sup>fi</sup>culty experienced by some domain experts when they attempt to describe the detailed steps in completing a task that is so familiar to them that they do it almost automatically [53]. SRTs encourage users to deeply re<sup>fl</sup>ect on their routines, triggering memory and therefore mitigating the impact of satis<sup>fi</sup>cing and automaticity.

iii. SRTs use vocabulary and syntax that are familiar to their intended users.

Topi and Ramesh [58] suggest that conceptual models used as communication tools between analysts and users should not be as formal and restrictive as tools for communicating between analysts and developers. Siau and Tan [47] propose the use of cognitive mapping techniques such as semantic mapping and causal mapping as potentially effective communication tools between analysts and end-users. The use of business oriented vocabulary and syntax in SRTs helps business professionals understand, evaluate, and analyze systems in organizations at whatever level of detail is appropriate for their particular situation, regardless of whether IT plays a central role. Accordingly, this analytical tool is appropriate for the lightweight analysis conducted by business professionals.

It should be noted that the goal of this research is not to make SRTs as complex or as precise as the UML diagrams. SRTs should be as easy to use and as informal as possible. They should remain a lightweight analysis tool that can be used easily and understood by business professionals with little or no training. IT specialists would still be required, however. Either they would develop SRTs with the business professionals or they would examine the SRTs produced by business professionals, identify areas of imprecision, and perform the translation to the related UML diagrams. Our attempt to develop this approach further will strive to balance simplicity of use and completeness of information.

## 6. Conclusions

This paper reviewed the dif<sup>fi</sup>culties of using a formal modeling language such as UML in e-service systems analysis and proposed using SRTs as an informal language and lightweight analytical tool to supplement UML. This tool is based on the service value chain framework and does not require technical concepts or obscure terminology. Therefore it can be adopted easily by business professionals to analyze e-service systems. The paper also presents a set of heuristics to transform SRTs to two key UML diagrams, which are used as formal modeling techniques for systems design and implementation by IT professionals.

Our research on the use of SRTs addresses the following goals:

i. Understand the bene<sup>fi</sup>ts and practical limitations of lightweight analysis such as the approach based on SRTs.

ii. Develop heuristics that can be used to transform SRTs into UML diagrams that can be used for more precise documentation and analysis that is needed for the development of testable software.

iii. Develop ways to complement and supplement UML diagram creation by using SRTs to capture ideas, issues, and requirements that are outside of UML's scope.

There are a number of directions for future study in this line of research. First, empirical studies can assess the ef<sup>fi</sup>cacy of using the service value chain framework and the associated SRT technique in analyzing e-service systems. Case study or action research might be appropriate research methods for this purpose. The proposed SRT technique may also be applied in educational and training settings to educate systems analysis and design students. Second, the proposed heuristics can be tested in practice and developed further. New heuristics can be developed to guide the transformation of SRTs into other UML diagrams, such as activity diagrams and sequence diagrams. Third, follow-on research might assess the semantic equivalence of SRTs and UML diagrams. Finally, SRTs might be used in other systems analysis and design contexts, such as knowledge management systems and enterprise systems integration. In all areas, the overarching goal is to supplement formal, high precision analysis and design tools with lightweight tools that are more useable and understandable by typical business professionals. Such tools could help business professionals understand e-service systems in greater depth and could help them communicate with IT professionals about functional and nonfunctional requirements for software development.

## Appendix A. Work system framework and work system method

A work system is a system in which human participants and/or machines perform work (processes and activities) using information, technology, and other resources to produce speci<sup>fi</sup>c products and/or services for speci<sup>fi</sup>c internal or external customers. Typical business organizations contain work systems that procure materials from suppliers, produce products, deliver products to customers, <sup>fi</sup>nd customers, create <sup>fi</sup>nancial reports, hire employees, coordinate work across departments, and perform many other functions.

Information systems, supply chains, and projects are all special cases of work systems. An information system is a work system whose processes and activities are devoted to processing information, i.e., capturing, transmitting, storing, retrieving, manipulating, and displaying information. A supply chain is an interorganizational work system devoted to procuring materials and other inputs required to produce a <sup>fi</sup>rm's economic products and services. The <sup>fi</sup>rm and speci<sup>fi</sup>c suppliers are participants in processes and activities that use speci<sup>fi</sup>c information and technology to create, monitor, and ful<sup>fi</sup>ll orders. A project is a work system that is designed to produce a particular set of products and services and then go out of existence.

The fact that a work system uses IT extensively does not imply that it is an information system. The following are examples of work systems that use IT extensively but are not information systems: ful<sup>fi</sup>llment systems for physical goods, package delivery systems, highly automated manufacturing systems, medical systems that include physical examination or treatment of patients, and transportation systems that use IT extensively. In such cases, an information system may produce intermediate products and services that are meaningful and useful primarily in the context of a larger work system that involves activities beyond processing information. Alternatively, the processing of information may be so intertwined with the work system that it is barely meaningful to speak of the information system as a separate system.

## A.1. Work system framework

Figure A-1 is the work system framework, which identi<sup>fi</sup>es nine elements that are part of even a rudimentary understanding of a work system. Four of these elements (processes and activities, participants, information, and technologies) constitute the work system. The other <sup>fi</sup>ve elements <sup>fi</sup>ll out a basic understanding of the situation. For example, no analysis of a work system is complete without some understanding of the customer's view of whatever the system produces. The double-headed arrows in the work system framework express the need for alignment between the elements. The arrows also convey the path through which a change in one element might affect another element. In particular, the arrows linking processes and activities to participants, information, and technologies say that a change in the processes and activities might call for a change in any of those elements, and vice versa.

The work system framework is designed to emphasize business rather than IT concerns. In contrast to inwardly facing analysis models that overemphasize producer concerns and underemphasize customer concerns, the work system framework places the customer at the top because a work system's primary goal is to produce products and services for customers. The work system framework does not preclude the possibility that customers will perform self-service steps, however, because a customer can also be a participant.

As explained in [3,5], the terms included in the work system framework re<sup>fl</sup>ect a number of distinctions that are sometimes overlooked. For example, the work system framework uses processes and activities instead of business process, which is often interpreted as a highly structured set of steps. Processes and activities covers a full range of situations that might involve highly structured work<sup>fl</sup>ows and/or “artful processes” whose sequence and content “depend on the skills, experience, and judgment of the primary actors” [26]. The term participants (not users) is included because important roles in a work system may be played by people who are not direct users of IT. The information in the system might include computerized databases, documents, shared knowledge, or even unrecorded discussions and commitments. Technologies (not IT) is used because multiple technologies may be relevant to the analysis. The analysis of a work system is incomplete if it does not consider the products and services provided for its customers. The customers include the direct bene<sup>fi</sup>ciaries of whatever a work system produces, plus other customers whose interest and involvement are less direct. The environment includes organizational culture and relevant regulations, policies and procedures, competitive issues, organizational history, and technical developments. Strategies of the <sup>fi</sup>rm, organization, and work system should be aligned, although in many situations they may not be articulated clearly.

## A.2. Work system method

The work system method is a method that business professionals (and/or IT professionals) can use for understanding and analyzing a work system at whatever level of depth is appropriate for their particular concerns. It has evolved iteratively starting in around 1997. At each stage, the then current version was tested by evaluating the areas of success and the dif<sup>fi</sup>culties experienced by MBA and EMBA students trying to use it for a practical purpose. A version called “workcentered analysis” that was presented in the 1990s in a textbook was used by a number of universities as part of the basic explanation of systems in organizations, thereby helping students focus on business issues and helping student teams communicate. Ramiller [39] reports on using a version of the work system framework within a method for “animating” the idea of business process within an undergraduate class. In a research setting, Petrie [37] uses the work system framework as a basic analytical tool in a Ph.D. thesis examining 13 e-commerce web sites. Petkov and Petkova [36] demonstrate the usefulness of the work system framework by comparing grades of students who did and did not learn about the framework before trying to interpret the same ERP case study.

Results from analyses of real world systems by typical employed MBA and EMBA students indicate that a systems analysis method for business professionals must be much more prescriptive than soft system methodology [14]. While not a straitjacket, it must be at least somewhat procedural and must provide vocabulary and analysis concepts while at the same time encouraging the user to perform the analysis at whatever level of detail appropriate for the task at hand. The latest version of the work system method is organized around a general problem-solving outline that includes:

![](/api/attachments/8ADAXHUQ/fulltext/images/e488a6340aa60c4088ac2cbf75a3ca7c88e6523284af85946c732d62934edc2b.jpg)  
Figure A-1. The work system framework, slightly updated [3,5].

i. Identify the problem or opportunity.

ii. Identify the work system that has that problem or opportunity (plus relevant constraints and other considerations).

iii. Use the work system framework to summarize the work system.

iv. Gather relevant data.

v. Analyze using design characteristics, measures of performance, and work system principles.

vi. Identify possibilities for improvement.

vii. Decide what to recommend.

viii. Justify the recommendation using relevant metrics and work system principles.

In contrast to systems analysis and design methods for IT professionals who need to produce a rigorous, totally consistent de<sup>fi</sup>nition of a computerized system, the work system method:

i. Encourages the user to decide how deep to go.

ii. Makes explicit use of the work system framework and work system life cycle model.

iii. Makes explicit use of work system principles.

iv. Makes explicit use of characteristics and metrics for the work system and its elements.

v. Views work system participants as part of the system (not just users of the software).

vi. Includes codi<sup>fi</sup>ed and non-codi<sup>fi</sup>ed information.

vii. Includes IT and non-IT technologies.

viii. Suggests that recommendations include work system improvements that rely on IS changes, plus other work system changes that don't rely on IS changes.

## References

[1] R. Agarwal, A.P. Sinha, Object-oriented modeling with UML: a study of developers perceptions. Communications of the ACM 46 (9)(2003) 248–256.

[2] S. Alter, 18 reasons why IT-reliant Work systems should replace the IT artifact as the core subject matter of the is <sup>fi</sup>eld, Communications of the AIS 12 (23) (2003) 365–394.

[3] S. Alter, The Work System Method: Connecting People, Processes, and IT for Business Results, The Work System Press, Larkspur, CA, 2006.

[4] S. Alter, Service Responsibility Tables: A New Tool for Analyzing and Designing Systems, Thirteenth Americas Conference on Information Systems, Association for Information Systems, Keystone, CO, 2007.

[5] S. Alter, De<sup>fi</sup>ning information systems as work systems: implications for the IS <sup>fi</sup>eld, European Journal of Information Systems 17 (5) (2008) 448–469.

[6] S. Alter, Service system fundamentals: work system, value chain, and life cycle IBM Systems Journal 47 (1) (2008) 71–85.

[7] S. Alter, Viewing systems as services: a fresh approach in the IS <sup>fi</sup>eld Communications of the AIS 26 (11) (2010) 195–224.

[8] M.J. Bitner, A.L. Ostrom, M.L. Meuter, Implementing successful self-service technologies, Academy of Management Executive 16 (4) (2002) 96–108.

[9] G. Booch, J. Rumbaugh, I. Jacobson, The Uni<sup>fi</sup>ed Modeling Language User Guide Addison-Wesley, Reading, Mass., 1999.

[10] G.J. Browne, V. Ramesh, Improving information requirements determination: a cognitive perspective, Information Management 39 (8) (2002) 625–645.

[11] G.J. Browne, M.B. Rogich, An empirical investigation of user requirements elicitation: comparing the effectiveness of prompting techniques, Journal of Management Information Systems 17 (4) (2001) 223–249.

[12] J. Bubenko, Challenges in requirements engineering, in: second IEEE international symposium on requirements engineering, York, England, 1995.

[13] T.A. Byrd, K.L. Cossick, R.W. Zmud, A synthesis of research on requirements analysis and knowledge acquisition techniques, MIS Quarterly 16 (1) (1992) 117–138.

[14] P. Checkland, Systems Thinking, Systems Practice (includes a 30-year retrospective), John Wiley & Sons, Chichester, UK, 1999.

[15] H. Chesbrough, J. Spohrer, A research manifesto for services science, Communications of the ACM 49 (7) (2006) 35–40.

[16] G.B. Davis, Strategies for information requirements determination, IBM Systems Journal 21 (1) (1982) 4–30.

[17] A.M. Davis, P. Hsia, Giving voice to requirements engineering, IEEE Software 11 (2) (1994) 12–16.

[18] L. Dawson, P. Swatman, The use of object-oriented models in requirements engineering: a <sup>fi</sup>eld study, Twentieth International Conference on Information Systems, Association for Information Systems, Charlotte, NC, 1999, pp. 260–273

[19] A. Dennis, B.H. Wixom, D. Tegarden, Systems Analysis and Design : An Objectoriented Approach with UML, Wiley, New York, 2001.

[20] B. Dobing, J. Parsons, Understanding the role of use cases in UML: a review and research agenda, Journal of Database Management 11 (4) (2000) 28–36

[21] B. Dobing, J. Parsons, How UML is used, Communications of the ACM 49 (5) (2006) 109–113.

[22] B. Dobing, J. Parsons, Dimensions of UML diagram use: a survey of practitioners, Journal of Database Management 19 (1) (2008) 1–18.

[23] J. Erickson, A decade and more of UML: an overview of uml semantic and structural issues and UML <sup>fi</sup>eld use, Journal of Database Management 19 (3) (2008) i–vii.

[24] M.D. Fraser, K. Kumar, V.K. Vasihnavi, Informal and formal requirements speci<sup>fi</sup>cation languages: bridging the gap, IEEE Transactions on Software Engineering 17 (5) (1991) 454–466.

[25] M. Glinz, Problems and de<sup>fi</sup>ciencies of UML as a requirements speci<sup>fi</sup>cation language, 10th International Workshop on Software Speci<sup>fi</sup>cation and Design (IWSSD-10), Association for Information Systems, San Diego, 2000, pp. 11–22.

[26] C. Hill, R. Yates, C. Jones, S.L. Kogan, Beyond predictable work<sup>fl</sup>ows: enhancing productivity in artful business processes, IBM Systems Journal 45 (4) (2006) 663–682.

[27] C.F. Hofacker, R.E. Goldsmith, E. Bridges, E. Swilley, E-Services: a synthesis and research agenda, Journal of Value Chain Management 1 (1/2) (2007) 13–44.

[28] K. Holtzblatt, H.R. Beyer, Requirements gathering: the human factor, Commu nications of the ACM 38 (5) (1995) 30–32.

[29] C.Kobryn,UML 2001: a standardization odyssey,Communicationsof the ACM 42 (10) (1999) 29–37.

[30] S. Kujala, User involvement: a review of the bene<sup>fi</sup>ts and challenges, Behaviour & Information Technology 22 (1) (2003) 1–16.

[31] M.L. Markus, J. Mao, Participation in development and implementation—updating an old,tired concept for today's IS contexts, Journal of the Association for Information Systems 5 (11) (2004) 514–544.

[32] M.L. Meuter, A.L. Ostrom, R.I. Roundtree, M.J. Bitner, Self-service technologies: understanding customer satisfaction with technoiogy-based service encounters, Journal of Marketing 64 (2000) 50–64.

[33] M.L. Meuter, M.J. Bitner, A.L. Ostrom, S.W. Brown, Choosing among alternative service delivery modes: an investigation of customer trial of self-service technologies, Journal of Marketing 69 (2005) 61–83.

[34] C.J. Neill, P.A. Laplante, Requirements engineering: the state of the practice, IEEE Software 20 (6) (2003) 40–45.

[35] W.J. Orlikowski, D.C. Gash, Technological frames: making sense of information technology in organizations, ACM Transactions on Information Systems 12 (2) (1994) 174–207.

[36] D. Petkov, O. Petkova, The work system model as a tool for understanding the problem in an introductory IS proiect 23rd Information Systems Education Conference (ISECON 2006). Association for Information Systems, Dallas, TX, 2006.

[37] D.E. Petrie, Understanding the Impact of Technological Discontinuities on Information Systems Management: The Case of Business-to-Business Electronic Commerce, Claremont Graduate University, 2004

[38] K. Pohl, Process-Centered Requirements Engineering, John Wiley & Sons, New York, 1996.

[39] N. Ramiller, Animating the concept of business process in the core course in information systems, Journal of Informatics Education and Research 3 (2) (2002) 53–71.

[40] J. Rowley, An analysis of the e-service literature: towards a research agenda, Internet Research 16 (3) (2006) 339–359.

[41] J. Rumbaugh, I. Jacobson, G. Booch, The Uni<sup>fi</sup>ed Modeling Language Reference Manual, Addison-Wesley, Reading, Mass., 199

[42] R. Rust, P. Kannan, E-service: a new paradigm for business in the electronic environment, Communications of the ACM 46 (6) (2003) 36–42.

[43] K. Scott, The Uni<sup>fi</sup>ed Process Explained, Addison-Wesley, Boston, MA, 2002.

[44] K. Siau, Q. Cao, Uni<sup>fi</sup>ed modeling language — a complexity analysis, Journal of Database Management 12 (1) (2001) 26–34.

[45] K. Siau, L. Lee, Are use case and class diagrams complementary in requirements analysis? An experimental study on use case and class diagrams in UML, Requirements Engineering 9 (4) (2004) 229–237.

[46] K. Siau, P. Loo, Identifying the Learning Dif<sup>fi</sup>culties with Uni<sup>fi</sup>ed Modeling Language (UML), Information Systems Management 23 (3) (2006).

[47] K. Siau, X. Tan, Information systems requirements determination and analysis: a mental modeling approach, Ninth Americas Conference on Information Systems (AMCIS'03). Association for Information Systems Tampa FL. 2003 pp 1370–1379

[48] K. Siau, X. Tan, Improving the quality of conceptual modeling using cognitive mapping techniques, Data & Knowledge Engineering 55 (3) (2005) 343–365.

[49] K. Siau, X. Tan, Using cognitive mapping techniques to supplement UML and UP in information requirements determination, Journal of Computer Information Systems 47 (2006) 59–66

[50] K. Siau, Y. Tian, A semiotics analysis of UML graphical notations, Requirements Engineering 14 (1) (2009) 15–26.

[51] K. Siau, J. Erickson, L. Lee, Theoretical versus practical complexity: the case of UML, Journal of Database Management 16 (3) (2005) 40–57.

[52] H.A. Simon, Behavioral Models of Rational Choice, in: Models of Man, Wiley, New York, 1957.

[53] H.A. Simon, Information processing models of cognition, Annual Review of Psychology 30 (1979) 363–396

[54] J. Spohrer, P.P. Maglio, J. Bailey, D. Gruhl, Steps toward a science of service systems, Computer 40 (1) (2007) 71–77.

[55] Standish, Extreme CHAOS, The Standish Group International, 2001, p. 12.

[56] S. Swamynathan, A. Kannan, T.V. Geetha, Composite event monitoring in XML repositories using generic rule framework for providing reactive e-services, Decision Support Systems 42 (1) (2006) 79–88.

[57] X. Tan, S. Alter, K. Siau, Integrating lightweight systems analysis into the uni<sup>fi</sup>ed process by using service responsibility tables, Fourteenth Americas Conference on Information Systems, Association for Information Systems, Toronto, Canada, 2008.

[58] H. Topi, V. Ramesh, Human factors research on data modeling: a review of prior research, an extended framework and future research directions, Journal of Database Management 13 (2) (2002) 3–19.

[59] J.R. Valusek, D.G. Fryback, Information requirements determination: obstacles within, among, and between participants, in: R. Galliers (Ed.), Information Analysis: Selected Readings, Addison Wesley, Reading, MA, 1987, pp. 139–151.

[60] S.L. Vargo, R.F. Lusch, Evolving to a new dominant logic for marketing, Journal of Marketing 68 (2004) 1–17.

[61] S.L. Vargo, R.F. Lusch, Service-dominant logic: reactions, re<sup>fl</sup>ections and re<sup>fi</sup>nements, Marketing Theory 6 (3) (2006) 281–288.

[62] K.E. Weick, Sensemaking in Organizations, Sage Publications, Thousand Oaks, CA, 1995.

Xin Tan is currently an assistant professor in Department of Information Systems and Decision Sciences at Fairleigh Dickinson University. He obtained a Ph.D. from the University of Nebraska-Lincoln, and an MBA from Miami University. His current research interests include information systems development, and user acceptance of advanced information technology and information systems. He has published papers in Communications of the ACM, Data & Knowledge Engineering, IEEE Transactions on Professional Communication, Information Resource Management Journal, and Journal of Computer Information Systems.

Steven Alter is a Professor of Information Systems at the University of San Francisco. He holds a B.S. in mathematics and Ph.D. in management science from MIT. He extended his 1975 Ph.D. thesis into one of the <sup>fi</sup>rst books on decision support systems. After teaching at the University of Southern California he served for eight vears as cofounder and Vice President of Consilium, a manufacturing software <sup>fi</sup>rm that went public in 1989 and was acquired by Applied Materials in 1998. His many roles at Consilium included starting departments for customer service, training, documentation, technical support, and product management. Upon returning to academia, he wrote an information systems textbook whose fourth edition was published in August 2001 with a new title, Information Systems: Foundation of E-business. His articles have appeared in Harvard Business Review, Sloan Management Review, MIS Quarterly, Interfaces, Communications of the ACM, Communications of the AIS, Futures, The Futurist, and many conference transactions.

Keng Siau is the E. J. Faulkner Professor at the University of Nebraska, Lincoln (UNL). He is the Director of the UNL-IBM Global Innovation Hub, Editor-in-Chief of the Journal of Database Management, and North America Regional Editor of the Requirements Engineering journal. He received his Ph.D. degree from the University of British Columbia (UBC). His master and bachelor degrees are in Computer and Information Sciences from the National University of Singapore. Professor Siau has over 250 academic publications. He has published more than 100 refereed journal articles, and these articles have appeared (or are forthcoming) in journals such as Management Information Systems Quarterly, Journal of the Association for Information Systems, Communications of the ACM, IEEE Computer, Information Systems Journal, Journal of Strategic Information Systems, Information Systems, ACM SIGMIS's Database, IEEE Transactions on Systems, Man, and Cybernetics, IEEE Transactions on Professional Communication, IEEE Transactions on Information Technology in Biomedicine, IEICE Transactions on Information and Systems, Data and Knowledge Engineering, Journal of Information Technology, and International Journal of Human-Computer Studies. He is Co-Editor of the AMIS volume titled “Systems Analysis and Design: Techniques, Methodologies, Approaches, and Architectures.” He served as Organizing and Program Chairs of the International Conference on Evaluation of Modeling Methods in Systems Analysis and Design (EMMSAD) (1996–2005). He also served on the organizing committees of AMCIS 2005, ER 2006, AMCIS 2007, EuroSIGSAND 2007, EuroSIGSAND 2008, and ICMB 2009. He received the International Federation for Information Processing (IFIP) Outstanding Service Award in 2006. He is also a recipient of the IBM Faculty Award in 2006, 2008, and 2010.
