---
otero_id: 25535
otero_key: "T92XA3VN"
title: "Design principles for learning analytics information systems in higher education"
authors: "Andy Nguyen; Tuure Tuunanen; Lesley Gardner; Don Sheridan"
year: "2021"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2020.1816144"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Design principles for learning analytics information systems in higher education

Andy Nguyen , Tuure Tuunanen , Lesley Gardner & Don Sheridan

To cite this article: Andy Nguyen , Tuure Tuunanen , Lesley Gardner & Don Sheridan (2020): Design principles for learning analytics information systems in higher education, European Journal of Information Systems, DOI: 10.1080/0960085X.2020.1816144

To link to this article: https://doi.org/10.1080/0960085X.2020.1816144

CO © 2020 The Author(s). Published by Informa UK Limited, trading as Taylor & Francis Group.

![](/api/attachments/T92XA3VN/fulltext/images/c611d1ea6076e177da526a46457bd7f4b418b339ca187e0fe41a36dced044c56.jpg)

Published online: 18 Oct 2020.

![](/api/attachments/T92XA3VN/fulltext/images/7b0bff280fbe7d7857434e36c5eda3ba0019cda018994798f0791dd233b0d832.jpg)

Submit your article to this journal

![](/api/attachments/T92XA3VN/fulltext/images/a4738a7dfb7736add8c8955f832b2d66780f500331f8059ca32937d2b4f510b7.jpg)

Article views: 347

![](/api/attachments/T92XA3VN/fulltext/images/f3d5f561e923b6a24993b3f5abc53f7ab7d0ad65f2c9e6bea258ed4e543f58b9.jpg)

View related articles

![](/api/attachments/T92XA3VN/fulltext/images/f88254bf99ea3761affc0f9af3253a85aec6dfec73a63d6eb5773c0164ca9b94.jpg)

View Crossmark data

EMPIRICAL RESEARCH

∂ OPEN ACCESS

Check for updates

# Design principles for learning analytics information systems in higher education

Andy Nguyen<sup>a</sup>, Tuure Tuunanen <sup>b</sup>, Lesley Gardner<sup>c</sup> and Don Sheridan<sup>c</sup>

<sup>a</sup>Department of Information Systems and Operations Management (ISOM), The University of Auckland, Auckland, New Zealand University of Oulu, Learning & Educational Technology Research Unit (LET), Oulu, Finland; <sup>b</sup>Faculty of Infornation Technology, University of Jyväskylä, Jyväskylä, Finland; <sup>c</sup>Department of Information Systems and Operations Management (ISOM), The University of Auckland, Auckland, New Zealand

## ABSTRACT

This paper reports a design science research (DSR) study that develops, demonstrates and evaluates a set of design principles for information systems (IS) that utilise learning analytics to support learning and teaching in higher education. The initial set of design principles is created from theory-inspired conceptualisation based on the literature, and they are evaluated and revised through a DSR process of demonstration and evaluation. We evaluated the developed artefact in four courses with a total enrolment of 1,173 students. The developed design principles for learning analytics information systems (LAIS) to establish a foundation for further development and implementation of learning analytics to support learning and teaching in higher education.

ARTICLE HISTORY Received 4 April 2019 Accepted 21 August 2020

ACCEPTING EDITOR Dr Pär Ågerfalk

ASSOCIATE EDITOR Dr Jonny Holmstrom

KEYWORDS Design Science Research; learning Analytics; information Systems; higher Education

## 1. Introduction

Advances in educational technologies and the digitalisation of education have generated increased interest in utilising learner behaviour data to provide processoriented information to enhance learning and teaching (NGUYEN et al., 2017; NOROOZI et al., 2019). Researchers and educators have noted the potential use of big data and data analytics in higher education (CHAURASIA et al., 2018; DANIEL, 2015; PICCIANO, 2012). HATHAWAY (1985) suggested that “the main barrier to efective instructional practice is lack of information”. By applying data analytics, we can now obtain useful information about the learner and learning process to aid instructional practice. For instance, WISE and JUNG (2019) reported the university instructors’ use of a LA dashboard to inform their teaching. A model of instructor analytics was constructed based on the findings to propose useful categories of activities for future study and support.

Although previous studies have recognised diferent practical implications of learning analytics (hereafter LA) related to user behaviour and engagement modelling, predictive analysis, personalisation and adaptive learning (KRUMM et al., 2014; NGUYEN et al., 2017), the design and implementation of data analytics in education involve complex processes, and the widespread adoption of LA will require sustained eforts (CHATTI et al., 2014; DANIEL, 2015). The development and implementation of LA in higher education are often ad-hoc and lacking the replication and improvement capabilities (NGUYEN et al., 2020). In this paper, we argue that depicting LA information systems (hereafter LAIS) as a class of information systems and conceptualising its design theories would establish a fundamental infrastructure to promote the development and implementation of LA.

For decades, information systems (IS) have been a powerful tool supporting and transforming education to meet the increasing demands of society (LEIDNER & JARVENPAA, 1995). Institutions have applied IS to assist diferent educational stakeholders, such as students, teachers, and institutional administrators, in learning and teaching activities, administrative tasks, and decision-making (GOLDSTEIN & KATZ, 2005; LEIDNER & JARVENPAA, 1995). IS have also become an inseparable part of modern education. The application of educational IS has continuously improved the efectiveness of learning and teaching (DAHLSTROM et al., 2014; LEIDNER & JARVENPAA, 1995). In the context of higher education, IS enhance learning and teaching by allowing for distance and self-paced learning, data-driven instruction, and automation of pedagogic activities. The use of IS in education led to novel research domains, theories, and principles that sought to address challenges facing education. As such, research in educational IS has addressed the demands for more efective tools regarding both administration, education and research required for increased masses of students (BECKER et al., 2017; HENDERSON et al., 2017; LACITY et al., 2018; PUCCIARELLI & KAPLAN, 2016). We argue that the theorisation of LAIS would open new opportunities for the educational IS research agenda to respond to the increasing demands from a widespread digitalisation in education.

The balance of both technology and learning aspects is crucial for the realisation of LA (DANIEL, 2017; DAWSON et al., 2015; REIMANN, 2016; ZHANG et al., 2018). Previous studies often examined ad-hoc or one-of applications of LA and there is a lack of standardised design knowledge to guide LA development. Recently, a few attempts have been made by connecting LA and IS research through the role of design science and design-based research (NGUYEN et al., 2020; REIMANN, 2016). The recognition of LAIS as a class of IS would bring together the forces of IS and learning sciences researchers to ofer efective LA solutions.

In this paper, we also respond to recent calls to consider how LA should be applied to support learning and teaching activities in higher education (DANIEL, 2017; ZHANG et al., 2018). This study seeks to establish a set of design principles that guide the development and implementation of LAIS. The research question for this study is as follows: How to design underlying information systems that support LA in higher education?

To address the research question, this study employed a design science research methodology (hereafter DSRM) (PEFFERS et al., 2007) to develop and evaluate a set of design principles for LAIS as a type of IS applied in the field of education. DSRM focuses on the development of a research artefact that would likely be a system or an object intended to support system development. DSRM is also well suited for DSR, which’s objective is to form design principles to support systems development (TUUNANEN & PEFFERS, 2018). The design principles are prescriptive statements that constitute the basis of design actions (BASKERVILLE & PRIES-HEJE, 2010; CHATTERJEE et al., 2017). In this study, we conceptualised an initial set of design principles grounded in the literature and then revised these via demonstration and evaluation of an operational prototype. The conceptualisation of our design principles was both action and materiality oriented (CHANDRA et al., 2015). We sought to prescribe what an artefact should allow users to do and what it should comprise. Furthermore, we developed and demonstrated a fully functioning prototype as a design instantiation of LAIS that illustrates the established design principles. Prior research has recognised the role of an instantiation of an IS design theory as an expository or representational tool that is embodied within it (GREGOR & JONES, 2007). Accordingly, we revised the principles through the development process of the system instance, its demonstration, and evaluation. Design science researchers can match our design principles with a particular application scenario and translate them into specific design requirements for LAIS (Chandra Kruse et al., 2016).

The following section reviews the literature on LA and the design, development, and implementation of LAIS in higher education. Then, we conceptualise and formulate the initial design principles. The design principles were applied to a technological architecture for LAIS. Thereafter, we demonstrate the proposed design principles through an operational LAIS prototype. Later, for evaluation, we used the artefact in four undergraduate courses with a total of 1,173 students. In the evaluation, we initially inspected server log data to assess the utility and eficacy of the artefact. We also conducted lecturer interviews and a student survey for further evaluation. After presenting the DSR process, we discuss the implications of our study, and we conclude by discussing its limitations and future research directions.

## 2. Theoretical foundations

## 2.1. Learning analytics: opportunities and challenges

Over the past decade, rapid developments in the field of big data and analytics have ofered opportunities to discover useful insights from massive volumes of educational data (BAKER & INVENTADO, 2014; IFENTHALER et al., 2018). Some research has reviewed and analysed the features and applicability of data analytics to support learning and teaching (ARNOLD & PISTILLI, 2012; NGUYEN et al., 2017, 2018; NISTOR & HERNÁNDEZ-GARCÍAC, 2018). As noted, these attempts to apply data analytics in education have emerged as a new discipline called LA. In general, LA refers to the application of data analytics methods and techniques in learning and teaching. The widely adopted definition of LA is “the measurement, collection, analysis, and reporting of data about learners and their contexts, for purposes of understanding and optimising learning and the environments in which it occurs” (SIEMENS & LONG, 2011, p. 32). In other words, the aim of LA is to process educational data to ofer meaningful information related to learner profiles, learning materials, and the learning context. It can perform descriptive modelling and predict learning constructs on a scheduled or real-time basis.

LA ofers remarkable benefits to diferent educational stakeholders, including lecturers and students. For instance, it can provide updated information about learning activities and student engagement, which could be used to construct a model of successful student behaviours (NISTOR & HERNÁNDEZ-GARCÍAC, 2018; SIEMENS & LONG, 2011). Instructors could use this model to revise learning activities and remove those that are unrelated to the course objectives. For example, BROWN (2020) reported the use of LA dashboard to monitor student learning at scale in large lecture courses. Although the teachers recognised the eficiencies that the LA dashboard facilitated, they are frustrated with how the displayed data undermined their existing pedagogical strategies. They faced dificulties in sensemaking about the reported data. Likewise, VIEIRA et al. (2018)’s systematic review of visual LA of educational data noted that far too little attention has been paid to how to deliver LA information to users in classroom settings. Moreover, while LA research mainly focusses on the analytics and learning facets, there are only a few studies that investigate LA from an IS perspective to promote its practical applications to support learning and teaching in higher education.

Although the literature has shown that LA has a promising impact on learning and teaching, the implementation of LA in practice has faced several challenges (DANIEL, 2015; PEÑA-AYALA, 2018). For instance, most of the data generated and stored in institutional IS are interoperable, but it is dificult to integrate data from disparate sources without data loss (DANIEL, 2015, 2017). Moreover, as LA is an interdisciplinary area of research, there is still a divide between those who understand the methods and techniques of data analytics and those who know how data analytics can be used to produce useful outcomes (DANIEL, 2015). Furthermore, the systematic implementation approach of LA in higher education is still lacking. The importance and originality of this study are that it explores LAIS as a class of IS and ofers insights into its design.

## 2.2. Development and implementation of learning analytics information systems

A considerable amount of literature has been published on the use of LA as a method to gain insights into learners and their learning (GRELLER & DRACHSLER, 2012; PEÑA-AYALA, 2018; SAARELA & KÄRKKÄINEN, 2017). Although these studies have extended the understanding in the domain of education, ad-hoc analyses were most common, and they were usually conducted to answer a specific research question, not gain information that could be used for widespread application.

Other studies have proposed a variety of LAIS for practical implementation (BODILY et al., 2018; LEONY et al., 2012; RUIZ et al., 2014; SIEMENS et al., 2014). For instance, LEONY et al. (2012) presented a web-based visualisation platform called GLASS (Gradient’s Learning Analytics System). This system ofers a simple workflow to visually present information related to students and their learning process in the form of widgets on a canvas on a visualisation dashboard. Another example is GAVRIUSHENKO et al. (2017)’s system architecture towards the development of an automated system for the academic advising process. This system architecture allows for determining the study profiles and recommending the proper study path to the learners.

While some prior studies propose that LAIS are an extension of existing educational IS (RUIPÉREZ-VALIENTE et al., 2015), other research describes them as distinct, standalone systems (BODILY et al., 2018; DYCKHOFF et al., 2012; SIEMENS et al., 2014). We argue that standalone LAIS with less dependency better address the challenges related to data integration. As such, LAIS can benefit from the flexibility of connecting to data from diferent sources to ofer useful insights (JÄRVELÄ et al., 2019; NOROOZI et al., 2019) and from the scalability. Accordingly, this indicates the need to investigate the underlying characteristics of LAIS as a new class of IS.

Most studies in the field of LA have developed and implemented LA for a specific application (BODILY et al., 2018; NGUYEN et al., 2020). For instance, RUBIO-FERNÁNDEZ et al. (2019) proposed a LA tool designed and implemented specifically for recommending actions to be performed to enhance a specific type of flipped classroom. Although previous research has made sustainability contributions in exploring the development and use of LA, they often neglected to present the general design principles and implementation of LAIS for further developments in the field. To our knowledge, there is only a limited account of research on LA from IS perspectives and no studies have synthesised and conceptualised design principles for LAIS. This study seeks to fill this gap in the literature. To do so, the research process involves iterations of three research activities: 1) formulation of design principles, 2) design and development and 3) demonstration and evaluation.

## 3. Design science research approach

The main goal of this study is to develop a set of empirically and theoretically grounded design principles for systems that support LA in higher education. This set of design principles is an information technology (IT) meta-artefact which establishes a general solution by depicting a class of technologies and can be instantiated into concrete IT artefacts (J IIVARI, 2015, 2017).

We adopted PEFFERS et al. (2007)’s iterative research process that allowed for the development of both design principles and system artefact. The system artefact, as an information technology with certain material properties, is utilised to demonstrate and evaluate the proposed design principles. Our study began with the identification and formulation of the problem and objectives (Phase 1) then went through three iterative phases: 2) Conceptualisation of Design Principles; 3) Design and Development; and 4) Demonstration and Evaluation.

In the identification and formulation of the problem and objectives (Phase 1), the problem of lacking guidance in the design and development of systems supporting LA is identified through the literature review and practical experience. Digitalisation has influenced and changed how education functions and is administered. While a massive amount of educational data is generated every minute, most institutions have not gathered and utilised the data efectively. Although LA has demonstrated potential benefits to educational stakeholders (NGUYEN et al., 2017; PEÑA-AYALA, 2018), there are several challenges facing the implementation of LA in higher education (CHATTI et al., 2014; DANIEL, 2015; DAWSON et al., 2014). As an interdisciplinary field, LA involves diferent expertise from diferent disciplines such as IS, computer sciences, and education (DAWSON et al., 2014). Consequently, the development and implementation of an efective LAIS in institutions require extensive resources, skills, and indepth knowledge. Even though diferent sets of challenges have been conceptualised by previous studies (DANIEL, 2015; SLADE & PRINSLOO, 2013), there remains a paucity of guidance on the development and implementation of LAIS in higher education. As a result, this study aims to construct a set of design principles that describe a class of systems that are a means to the purpose of supporting LA in learning and teaching.

In the conceptual development phase (Phase 2), we formulated the design principles based on a processoriented view of LA, using intervention theory as kernel theories. Drawing on the principles of intervention theory, we identified the prominent afordances required in the LA process and material properties to provide those afordances.

In the design and development phase (Phase 3), the design principles were translated into technical architecture and an operational prototype, that established the base for the subsequent phase of demonstrating and evaluating the artefact. The system prototype and its architecture acted as an expository or representational tool and was designed with the design principles embodied. It was a theory-ingrained artefact (SEIN et al., 2011) and embedded the research contribution in its design (PEFFERS et al., 2007). The system prototype was developed with state-of-the-art web application frameworks and technologies and hosted on Amazon Web Services (AWS) for operating in production.

In demonstration and evaluation (Phase 4), we validate the utility and eficacy of the proposed design with the prototypical implementation. The operational prototype of a LAIS was implemented to support learning and teaching at a university. We conducted two rounds of demonstration and evaluation of the artefact. The design principles and prototype were revised after each round. In the first round, we conducted a pilot study to demonstrate the prototype to the users and gathers their feedback for potential improvement. In the second round, we used three data sources including usage data (server logs), survey data from the students, and interviews with the lecturers, to formally evaluate the design principles and its artefact by adopting the evaluation criteria suggested by VENABLE et al. (2012). The analysis of usage data and survey data allowed us to observe whether afordances were indeed enacted and thus justify the utility and eficacy of the artefact. The teacher interview reveals potential side efects and undesirable consequences of using the artefacts for the improvement of the design principles.

## 4. Design principles for learning analytics information systems

The conceptualisation of design principles was informed by the literature on learning analytics (LA) (GRELLER & DRACHSLER, 2012; NGUYEN et al., 2017) and LA processes (IFENTHALER & WIDANAPATHIRANA, 2014; SIEMENS, 2013), and based on kernel theory provided by prior theory (GREGOR & JONES, 2007). The conceptualisation focuses on the activities that the system should aford for the LA process including measuring, collecting, analysing and reporting of data. In line with the fundamentals of design science research methodology (HEVNER et al., 2004; SEIN et al., 2011; WALLS et al., 1992), the requirements derived from kernel theories were used as the foundation for articulating the design principles. Particularly, the intervention theory (ARGYRIS, 1970) was used as a kernel theory to formulate the design principles for guiding the development of LAIS.

Prior research implies that the main applications of LA centre around providing insights to support decision making, aid or perform necessary interventions in learning and teaching (DYCKHOFF et al., 2012; NGUYEN et al., 2017). Beyond collecting and analysing educational data to ofer useful insights, LA should consider the learning and teaching intervention to efectively support the learning and learning design process (IFENTHALER et al., 2018; XING et al., 2015). In conjunction with this point, we argue that LAIS is only efective by empowering teachers and students as key users. Accordingly, the intervention theory is the best fit for this purpose, because of its emphasis on allowing the user, the receiver of the intervention, to be autonomous. ARGYRIS (1970)’s

Intervention Theory and Method suggest that “an intervenor, in this view, assists a system to become more efective in problem-solving, decision making and decision implementation in such a way that the system can continue to be increasingly efective in these activities and have a decreasing need for the intervenor” (ARGYRIS, 1970, p. 15). As a result, we derive the constraints from the design of interventions to establish LAIS design principles.

According to the intervention theory (ARGYRIS, 1970), there are three fundamental principles guiding the design of interventions: leveraging valid and useful information, allowing free informed choice by the user, and fostering internal commitment. The first principle emphasises on the use of valid and useful information. Valid information is “that which can be verified and has been shown to afect the phenomena the intervenor is seeking to influence” (PICCOLI et al., 2019, p. 3) whereas useful information allows the users to “control their destiny” (ARGYRIS, 1970). To support efective interventions, LAIS should ofer both valid and useful information to the users. In consonance with this requirement, the literature on LA also highlights the central role of actionable insights in LA applications (DAWSON et al., 2015; RL & GYNTHER, 2018; SIEMENS & LONG, 2011). The actionable insights refer to valid and useful information that can be concerned with the potential for practical action and influence user behaviour. We argue that LAIS must be able to report actionable insights for the users to perform and evaluate necessary interventions to the process of learning and teaching:

DP1. Principle of actionable information: LAIS should have features that allow for the reporting of actionable information about learners and their learning.

The first principle reflects the main purpose of LAIS: to provide insightful information that can support users in decision-making associated with learning and teaching activities (IFENTHALER et al., 2018; MANGAROSKA & GIANNAKOS, 2017). To perform scheduled or real-time modelling and predict learning, LAIS collects static and dynamic data about learner profiles, learning content, and the learning context (GRELLER & DRACHSLER, 2012; NGUYEN et al., 2018). In this way, LAIS can provide useful metrics that provide teachers insight into learners and their learning behaviour. In addition, LAIS facilitates the evaluation of learning design with real-time and predicted information (BAKHARIA et al., 2016; PERSICO & POZZI, 2015). The metrics may have diferent levels of aggregation specified to the needs of the users to help them plan learning interventions accordingly. For instance, a LAIS may digest the learning behaviour data and historical records to ofer predictive information on the student performance in a short-term (e.g., semester results) or long-term (e.g., degree completion) so that teachers can conduct early interventions and provide additional support. This principle also reflects the usefulness of LAIS.

Beyond providing insightful information, timing can influence the validity and usefulness of the information and afect the potential interventions (BUTLER et al., 2007; SHIMADA et al., 2018; TE’ENI, 1991). Up-to-date information is needed for appropriate decision-making in dynamic contexts in which data change over time and information needs to be frequently updated (IFENTHALER et al., 2018). Nevertheless, real-time reporting of information is not always efective. For instance, BUTLER et al. (2007) reported that tactically delayed feedback with the right timing led to improved final test performance relative to immediate feedback. As a result, we argued that LAIS should deliver reports in a timely manner to efectively support end-users:

## DP2. Principle of information timeliness: LAIS should generate reports in a timely matter.

Information timeliness refers to the ability to provide information at the appropriate time for its maximum impact. Apart from the technical constraints, the time latency between the data collection and reporting should be designed based on findings from the learning sciences and decision sciences. The second and third principles guiding the design of intervention refers to free informed choice by the users and fostering their internal commitment subsequently (ARGYRIS, 1970). Once the users are provided with valid and useful information, LAIS should enable users to take control of the information and interventions. Furthermore, we argued that the least required eforts would best motivate the system usage for efective interventions. The ease of use would encourage positive attitudes towards technology and promote its usage. As a result, we initially posited that LAIS should allow for availability and interoperability.

LAIS should be available and accessible to both data clients and data subjects at any time, as server shutdowns may discourage users from using the system and afect their tasks. LAIS should also respond to users when they request expanded exploration of the data in real-time or almost real-time (IFENTHALER et al., 2018; NGUYEN et al., 2017).

Moreover, it is important for LAIS to connect with the existing information systems in the institutions. Continuous data integration enables one to capture and load data with diferent schemas from multiple sources to generate meaningful information. As a result, LAIS should have a mechanism to collect and integrate data from diferent system environments (CHATTI et al., 2014; SIEMENS, 2013):

DP3: Principle of availability and interoperability: LAIS should be available and accessible to both data clients and data subjects at any time and be able to interoperate with any learning and teaching system, including virtual learning environments (VLEs), and allow the integration of diferent data sources.

This principle addresses the challenge of data integration when developing and implementing LAIS (CHATTI et al., 2012; DANIEL, 2015). Institutions in higher education do often have several nonintegrated information systems that store diferent educational data including student profile, learning and teaching resources, institutional finance, etc. The design and development of LAIS should concern multiple data sources to establish an integrated data pipeline that can ofer a comprehensive picture of the learners and the learning process. The next section proposes a LAIS architecture encapsulating the initial conceptualised design principles, that guides the development and demonstration of an operational system.

## 5. Learning analytics information systems architecture

Based on the design principles, a LAIS architecture was designed using service-oriented architecture (SOA) approach, which is popular in system design because of its high flexibility and extensibility (TM NGUYEN et al., 2005). An SOA system consists of multiple discrete components with a set of defined functionalities, and each unit can operate and be updated independently. This makes the SOA approach best suited for the purpose of actionable reporting and information timelines as diferent services can be designed for specific interventions and groups of users. Furthermore, this approach allows for high availability and interoperability.

We designed a LAIS architecture as an overall infrastructure for a group of LA services that support learning and teaching activities. Each LA service was designed and developed based on learning theories related to specific pedagogic activities (see DP1 and DP2). The SOA approach allows for parallel or even collaborative operation of diferent LA services to support diferent phases of learning and teaching processes. The actionable insights can be generated and provided to the users for diferent intervention scenarios without many dependencies. In addition, it features rapid extensibility and reusability.

Figure 1 proposes a LAIS architecture that allows for real-time interactions between learning and teaching systems and LA services.

Learning and teaching systems support authoring, content delivery, learning design, and learning processes. A typical example is a learning management system, which is intended for course delivery and administration. However, learning and teaching systems can also include authoring systems, communication systems, and LD tools. Both static and dynamic data are collected for analytical processes. A batch extract-transform-load (ETL) module collects and transforms static data that do not change over time, such as data from the enrolment system concerning learners’ backgrounds and course information from the learning management system.

The event transformation service module uses dynamic events from logging services and event trackers via event adapters as inputs. It normalises events from multiple sources and records them in an intermediate database. A real-time data cache can be retrieved by LA services for further analytics processing (see DP2). The outcomes of LA are delivered to end-users by reporting and response services. The user can also directly query LA data from the databases via a data application programming interface (API) such as the Experience API (xAPI). APIs are a set of subroutine definitions and communication protocols, and the xAPI is a new specification for learning technology that enables the collection of data about a wide range of experiences a learner has within online and ofline learning environments. Only authorised parties have access to this data and the UI supports interactions between the end-users and the system.

![](/api/attachments/T92XA3VN/fulltext/images/d4245e4131a8da8e54ce3e0b5d8002a23c2b926122e722b989a5cbeee7e0a7f6.jpg)  
Figure 1. Learning analytics information system (LAIS) architecture

The LAIS architecture allows for parallel development and simultaneous implementation of diferent LA while maintaining comprehensive interoperability between services and diferent educational IS (see DP3). The independence between the services allows for minimum downtime during new development and implementation thus maximise the availability of the system and its services. In addition, it allows for independent connections between specific services and existing educational IS. This would be also extremely useful in the scenario that institutions may have a number of diferent IS that may or may not contain usable interfaces for integration. Educational data from diferent systems would be extracted and put through a data pipeline that transforms and loads raw data into an integrated schema. This LAIS architecture does not only address the interoperability with the existing systems but also enables accelerated LA development informed by the needs of learning and teaching. Furthermore, evaluation of LA services based on pedagogic outcomes provides useful feedback for the development and implementation of future LA services.

We defined the main LA services and their functionalities based on learning management questions (WIGGINS & MCTIGHE, 2005) and the main applications of LA (IFENTHALER & WIDANAPATHIRANA, 2014; NGUYEN et al., 2017, 2018). Table 1 shows these services in relation to the questions. Each LA service interacts with other systems or services via four groups of parameters: events, metrics, situations, and actions. Figure 2 shows an abstraction of these interactions.

## 6. Demonstration and evaluation of the design principles of learning analytics information systems

Next, we demonstrate how we applied the design principles described above to develop a LAIS prototype in the context of higher education. Furthermore, we present a formal evaluation of the proposed design principles, and we discuss how this evaluation validates the use of the design principles and facilitates revision of them.

Evaluation of the DSR methodology (DSRM) comprises two main sub-activities: demonstration and evaluation (PEFFERS et al., 2007; TUUNANEN & PEFFERS, 2018). Demonstration indicates the ability of the artefacts to solve the identified research problems (VENABLE et al., 2012). In other words, it is a proof-ofconcept evaluation that seeks to demonstrate that artefact is viable for fulfiling its design purpose in a particular context. The evaluation aims to formally validate the efectiveness of the research artefacts for addressing the problem (PEFFERS et al., 2007).

![](/api/attachments/T92XA3VN/fulltext/images/d6562688a611f245b266cf8cb3741fe3ee1b36bc4b3c4bc14d8f217e9cb050e6.jpg)  
Figure 2. Key learning analytics (LA) services

Table 1. The functionality of learning analytics (LA) services.

<table><tr><td>LD Phase</td><td>Learning Management Question</td><td>LA Service</td></tr><tr><td>1. Profiling</td><td>What does the learner already know?Where does the learner need and want to be?How does learner best learn?</td><td>Learner Profiling:·Prior knowledge sets·Personal aspirations·Preferred learning stylesPrediction:·Performance</td></tr><tr><td>2. Strategising and Delivery</td><td>What resources do I have at my disposal?What will constitute the learning journey, and therefore, what is the best context for learning?Who will do what?</td><td>Decision Making:·Appropriate instructional resources and/or strategiesPrediction:·Scenario planning</td></tr><tr><td>3. Ascertainment and Reporting</td><td>How will I check whether the learner has achieved the learning outcomes?How will I inform the learner and others about the learner&#x27;s progress?</td><td>Situation Detection:·Notification of at-risk situationsEvaluation:·Information on learning engagementDecision Making:·Recommended interventions</td></tr></table>

In this study, we demonstrate and validate the utility of LAIS design principles through operational LAIS prototyping (BASILI et al., 2005; DAVIS, 1992). The principles were then evaluated by qualitative assessment involving observation, participant feedback, and semi-structured interviews (TREMBLAY et al., 2010; TUUNANEN & PEFFERS, 2018). We adopt the evaluation criteria suggested by VENABLE et al. (2012):

• Evaluate the artefact to establish its utility and eficacy for achieving its stated purpose.

• Evaluate the artefact to identify weaknesses and areas of improvement.

• Evaluate the artefact to identify side efects or undesirable consequences of its use.

## 6.1. Demonstration of an operational learning analytics information system prototype

The demonstration phase of the study was conducted at a large university in New Zealand in the first semester of 2016. The semester started at the beginning of March and ended in early July. The phase involved three operations management courses: two stage-II undergraduate courses (79 and 58 students) and one postgraduate course (14 students). Among the undergraduate students, 24 were taking both courses. In total, there were 127 potential data subjects. The courses ran for twelve weeks, and the final exam period occurred after the twelfth week. All the courses applied a blended learning approach, combining online teaching and learning materials with traditional classroom methods (i.e. face-to-face lectures were incorporated with computer-mediated activities for content delivery) (PORTER et al., 2014). In this case, a lecture theatre recording (LTR) service was used in the courses to allow students to take control over the time, place, path, and pace of their learning.

We applied the operational prototyping approach to demonstrate the use of LAIS design principles in the context of higher education. Operational prototyping (DAVIS, 1992; TUUNANEN et al., 2008) has been a popular approach to demonstrate the use of system design in the process of IS development (DAVIS et al., 2006; FLINK, 2014). A prototype is a partial implementation of an IS intended to validate its utility as a solution to the identified problem as well as learn about potential issues with the design. The creation of prototypes has been standard practice in IS development for many decades (BEYNON-DAVIES, 1998; DAVIS, 1992; DAVIS et al., 2006).

Operational prototyping integrates the two traditional approaches: throwaway prototyping and evolutionary prototyping (DAVIS, 1992). A throwaway prototype is built as fast as possible to verify poorly understood requirements and then is discarded, whereas an evolutionary prototype is constructed with well-understood parts to discover unknown requirements and then evolve the design. Throwaway prototyping is inefective due to the lack of understanding about critical requirements, and evolutionary prototyping is inefective as it does not produce information about the poorly understood requirements (DAVIS, 1992; DAVIS et al., 2006). Operational prototyping balances these limitations and enables comprehensive demonstration by building throwaway prototypes on top of evaluation prototypes.

## 6.1.1. An operational prototype of a learning analytics information system

We sought to develop and demonstrate an operational LAIS prototype based on the set of design principles described above. During a departmental meeting at University A, we conducted a presentation on how LA can be applied to support teachers in learning and teaching and introduced our research project. Some lecturers expressed interest in testing the prototype. With these lecturers, we discussed constructing a theory-based objective for LAIS prototyping.

As a proof of concept, the LAIS architecture and design principles were implemented to support teachers in evaluating students’ engagement with LTR, an expected service in blended classes using a lecturebased instructional approach. This information allows lecturers to evaluate in-class activities and ensure that their design engages not only the students that were present at the lecture but also the students who use the recordings. Since recent studies recognised the increasing use of lecture LTR as a substitution for attending classes (WIELING & HOFMAN, 2010; WILLIAMS et al., 2012), the consideration of LTR usage would inform lecturers about student engagement with learning.

Previous research suggests that students’ engagement with learning has a significant impact on their performance (CARINI et al., 2006; KAHU, 2013). By frequently monitoring student engagement with a course, a lecturer could perform necessary interventions and provide additional support to certain students in a timely manner. This could moderate and improve student engagement and, in turn, improve learning and achievement (KLEM & CONNELL, 2004). There is evidence showing that using LTR as a supplement when developing a knowledge base significantly improves learning performance (BOS et al., 2016). Using observations of in-class attendance as a complement to information about students’ interactions with LTR would provide lecturers a more complete picture of students’ engagement with lectures. Accordingly, we identified relevant events, metrics, and the potential use of LTR for operational prototyping (Table 2).

An operational prototype was built based on the Open edX platform (“Open edX,” 2017). Among several LA platforms, Open edX was selected because it appeared to meet our requirements. The prototype captures defined events and metrics to provide analytical reports of students’ engagement with LTR.

To ensure that they include actionable information about learners and their learning (see DP1), the reports were designed to take into account potential pedagogical actions. A report was sent to the lecturers each week via email (see DP2). The report included multiple graph visualisations with a user-friendly design. Figure 3 shows an example of the graphs.

The graphs show the total number of views on a video and the points on the video timeline to which the views correspond (light blue area). Thus, they show which parts students skipped most frequently. For instance, most students skipped through the first minute of the video represented in Figure 3 after viewing a few seconds. This result could be explained by the fact that viewers usually ignore the introduction slide and jump to the main content. It is interesting to note that the number of views slightly decreased near the end of the video. This indicates that a proportion of students gave up on learning from the LTR while viewing it. These results can be used to objectively determine the optimum length of lectures and determine the interest in a particular lecture.

The reports also provide information about segments that were replayed (dark blue area). This information may indicate potential cognitive dificulties concerning a specific part of the LTR, such as the peaks at the fifth and seventh minutes shown in Figure 3. Furthermore, several replayed segments in a lecture might suggest that students found the lecture to be dificult to understand, and the instructor might need to revise the content in later lectures or provide additional resources to improve students’ understanding.

Table 2. Design of the learning analytics information system prototype.

<table><tr><td>Data Captured</td><td>Reported Information</td></tr><tr><td>Events:load_videoplay_videopause_videoseek_videospeed_change_videostop_video.Metrics:Course informationVideo metadata (e.g., title, length.)</td><td>Metrics:Number of active students in each weekAverage video views each weekNumber of students who watched a particular video (unique viewers)Number of replays at any point in the video (replayed segments)Potential Use:To identify the parts that students most frequently skip or replay→ Adjustment of potentially problematic parts of the learning materialsTo monitor students&#x27; engagement with learning→ Early interventions if there is a lack of engagement→ Evaluation of the effectiveness of learning design improvements on subsequent student engagement</td></tr></table>

![](/api/attachments/T92XA3VN/fulltext/images/29b492e9c037fe9874490cf1c9710df5c6a7d419278e081c68ba7421753add9a.jpg)  
Figure 3. An example of a graph reported to lecturers

The LTR system is available for the students (data subjects) and teachers (data clients) to access at any time (see DP3). The information reported to lecturers is generated by analysing the data collected and integrated from several sources (see DP3). The system prototype tracks student inputs posted to the server and records them to the tracking logs. In particular, the system captures emitted events regarding students interactions with the video player while watching a recording. It also gathers static data from multiple databases. Course information is retrieved from the MongoDB database, and user details are collected from the MySQL database in the learning management system. Then, the application passes all events and state data to the analytics pipeline for data analysis.

## 6.1.2. Learnings from the demonstration of the prototype: utility and eficacy of the artefact

The objective of the demonstration phase of the study was to evaluate the implementation of the LAIS to establish its utility and eficacy for achieving its stated purpose (VENABLE et al., 2012). Next, we present how lecturers could use the LAIS prototype to support their teaching. By inspecting the parts that students most frequently skipped or replayed, the lecturers can identify potentially problematic parts of the learning materials and make appropriate adjustments, including revision of dificult content and inclusion of missing knowledge in the following lecture. Parts that were most commonly problematic featured poor audio quality and unclear explanations of concepts. In addition, the inspection of the most frequently skipped parts indicated that some content was counterproductive and should be eliminated. To optimise the blended learning settings, the lecturers attempted to edit the original LTR to remove inefectual fragments, reorganise the recordings into shorter videos and classify them into themes for better navigation and reduced cognitive workload. Prior studies suggested that these interventions would be able to promote learning and teaching by leveraging student engagement with learning materials (LAWLESS & BROWN, 1997; MAYER, 2008). For example, a well-designed navigation tool can leverage student engagement with learning content and promote learning performance (MERTENS et al., 2004).

By regularly monitoring students’ engagement with learning, the lecturers can perform necessary interventions to counteract a lack of engagement in a timely manner. For instance, learning procrastination often occurs in the early weeks of the semester that does not include any assessments. Although this behaviour can be expected, evidence can encourage lecturers to perform early interventions. Attempting to engage students in constant learning could improve students performance and enhance learning outcomes (CARINI et al., 2006; KAHU, 2013). Figure 4 illustrates an example of the LAIS reporting dashboard that indicates a lack of engagement with LTR.

The lecturers attempted to encourage students to engage with the lecture content early in the semester whenever they observed low engagements with recent recordings. Two lecturers introduced quizzes at the beginning of the following lecture to assess students knowledge and recall.

The lecturers observed a high level of student engagement with activity-based learning (ABL) exercises, as shown in Figure 5. This finding aligns with previous education science literature findings that ABL exercises engage students better than other types of exercises and hence promote active learning and improve academic performance (OIGARA et al., 2014; ROEHL et al., 2013). Consequently, the lecturers adjusted their syllabi to include ABL exercises.

## 6.1.3. Learnings from the demonstration of the

prototype: weaknesses and areas of improvement The lessons learned while developing and implementing an educational application provide insights and guidelines regarding the current understanding of specific educational technologies. Continuous evaluation and adaptation are important in software development to deliver better value to the end-users. In order to learn about possible weaknesses and areas of improvement (VENABLE et al., 2012), we performed qualitative assessments through observation and user feedback (BOUDREAU et al., 2001; TREMBLAY et al., 2010). We constantly communicated with two lecturers using the LAIS prototype throughout the semester. Students gave feedback via email regarding any operational issues or failures. Furthermore, the field notes taken by the researchers were examined to identify observed problems and potential improvements.

![](/api/attachments/T92XA3VN/fulltext/images/1d6c0b8ccd6fc2818153166d0550fbd683b91ce62674c22496b0b10eb0e19af4.jpg)  
Figure 4. The learning analytics information system’s dashboard indicates a lack of engagement in a timely manner

![](/api/attachments/T92XA3VN/fulltext/images/e6d25cbc97340c14fa5866f826c25fa5352f8b4ecf929dfe5f309cd03477a007.jpg)

![](/api/attachments/T92XA3VN/fulltext/images/9f928fe43640e17d5be5c14a365804fcd72f02930c60a2efd34710034bf0475c.jpg)

Lecture 1 Forecasting Methods  
![](/api/attachments/T92XA3VN/fulltext/images/a8587ab99dcee5a0b692246b7c54ab65c171d19583ffe17364123228e03ee325.jpg)  
Figure 5. The learning analytics information system’s dashboard shows the most engaging activities

During the demonstration phase of the study, the two lecturers expressed interest in receiving information about students’ engagement with LTR via an analytics dashboard that they could access when needed. Also, issues regarding multiple logins were observed, and students asked for the opportunity to sign on to the learning platform, which was isolated from the university learning management system, a single time. Many students demanded improvements in the ease of accessing the system. These results indicate the need for a single sign-on service (SSO) to eliminate the need to manage two diferent accounts.

We revised the design principles to address the issues experienced in the demonstration phase of the study. We found that, together with system availability, users found the availability of reporting information useful. As a result, it is important to store LA reports on the system so that the data clients (i.e. teachers) can access it when needed. Moreover, a dashboard with visualisations can be applied to display LA reporting information. LA reports can be practically supported by visualisations to deliver more meaningful information to the users (DUVAL, 2011; LEONY et al., 2012; NGUYEN et al., 2017). The benefit of visualisations is to better communicate large amounts of complex data to identify trends, patterns, correlations, and key issues. Furthermore, we observed that integration of the LAIS into the existing IS infrastructure at the university may lead to issues or complications. When developing the LAIS, we should consider and address these issues to optimise the utility of the system. Accordingly, we revised DP2 and DP3 as Principle of information delivery and Principle of interoperability to include these properties. We also saw a need to form a new DP4, Principle of information availability, based on the original DP3 and our findings from the demonstration phase. The design principles are defined as:

DP2. Principle of information delivery: Should generate responses and information that visualise learning and teaching behaviour and performance.

DP3: Principle of interoperability: Should interoperate with any LA and/or educational IS, including VLEs, and enable integration with diferent data sources without resulting in any discernible issues or complications.).

DP4. Principle of information availability: LAIS should be available and accessible to both data subjects and data clients at any time. LA reports should be stored on the system and accessible to the data clients at their convenience.

The system prototype was revised and updated to embrace the new design principles. The analytics dashboard module was updated so that the lecturers could access the reported information at any time (DP4). Moreover, an SSO was developed and implemented to allow for seamless integration with the existing learning management system (DP3).

## 6.2. Evaluation of the learning analytics information system

To formally evaluate the developed artefact, we adopted a subsequent case-study approach. This allowed us to examine the use of LAIS in the context of higher education, evaluate the artefact’s utility and eficacy for achieving its stated purpose, and investigate possible side efects or undesirable consequences of its use (VENABLE et al., 2012). The case-study approach to evaluation has been widely used in design science research on IS (BOUDREAU et al., 2001; HEVNER et al., 2004; PEFFERS et al., 2007). In this case study, we evaluated LAIS design principles and their implementation in a system via server log data, student surveys, and semi-structured interviews with the lecturers.

At University A, the developed LAIS prototype was examined in four undergraduate courses with a total enrolment of 1,173 students. These courses included one large first-year course (n = 966), and three secondyear courses (n = 207). The large first-year course is compulsory for all students aiming to obtain a Bachelor of Commerce (an undergraduate degree in business administration) from the university. The course introduces students to the field of IS and explores how IS and operations management help organisations to innovate, optimise, and deliver value. Two of the second-year courses are mandatory for operations management majors, and one is an optional course on data management.

## 6.2.1. Analysing server log data and student surveys: Utility and eficacy of the artefact

We used server log data to evaluate the utility and eficacy of the LAIS for achieving its stated purpose. As the artefact was designed to provide actionable information that the lecturers could use to monitor students’ engagement and perform necessary interventions, we looked at students’ engagement with each LTR over time. Figure 6 illustrates the total number of interaction events performed by students for each LTR (marked with diferent colours) in the first half of the semester.

The analysis shows the efect of interventions on students’ engagement with a particular video. Since students mainly use LTR as an alternative to attending lectures in person (WILLIAMS et al., 2012), students engagement with an LTR is usually expected to peak on the day it is released or the following day. Nevertheless, learning procrastination often delays student engagement, making it necessary for the lecturer to intervene. By monitoring student engagement, the lecturer can perform any necessary interventions to increase student engagement early in the semester to reduce the efect of procrastination and enhance student learning. A drill-down analysis of LTRs that involved lecturer intervention validated the impact of the lecturer’s actions using the artefact.

Figure 7 illustrates the change in the total number of interaction events with a particular LTR (LTR.A) over time since the day of its release. The students only performed 153 interaction events with LTR.A on the day of release. The number of events increased to 606 in the following two days before decreasing after that. The lecturer intervened to increase students engagement with LTR.A, increasing the total number of interaction events to 1,987. The more than 300% increase in the total number of interaction events demonstrates the efect of the lecturer’s pedagogic actions on engagement with this particular LTR. This observation analysis of server log data demonstrates the use of the LAIS to support teaching and enhance students’ engagement with learning. Hence, the system design was validated to match the purpose. Rather than directly performing an action, the LAIS allowed for free and informed choice with valid and useful information. Accordingly, the design reflects the principles of intervention theory (ARGYRIS, 1970).To further evaluate the artefact, we conducted a student survey. The survey was sent to students using the LAIS. The seven-point Likert scale (see Appendix 1) was designed to collect information about the extent to which they support teachers’ use of LA (see DP1, 2 and 4), their perceptions of the system’s quality to clarify the interoperability without resulting in any discernible issues or complications (see DP3) as well as potential ethical issues and concerns they identified (see DP4).

![](/api/attachments/T92XA3VN/fulltext/images/1bb9636c4c70badb5efed372fedde06bc4593a1ca02a3b45587dd4f4779f1c2f.jpg)  
Figure 6. Total number of interaction events for each video in the large first-year course over time

![](/api/attachments/T92XA3VN/fulltext/images/3018e6d3d13cc7864b9a24da44f6465f21911019f74aad0ae4f46ea6400748a7.jpg)  
Figure 7. An example of the efect of the lecturer’s intervention on student engagement

The results support teachers’ use of LA. The students agreed that the educational IS should inform lecturers about students that are at risk of failing (87.3% of respondents), learning content that students appear to find dificult to understand (96.0%), the learning progress of each individual (81.0%) and the whole class (90.5%) and visualisation of individuals (78.6%) and the whole class’s (85.7%) learning activities. Previous research has proposed diferent LAIS designs to address these applications of LA. For instance, ARNOLD and PISTILLI (2012) demonstrated the Course Signal system that provided prediction on students’ performance thus informed about students that are at risk of failing. Furthermore, prior research showed the use of LA dashboard to monitor the learning progress and keep track of learning activities (ARNOLD & PISTILLI, 2012; BODILY et al., 2018; VERBERT et al., 2013). The results did not show any significant conflicts of interest regarding the principle of actionable reporting (DP1). They revealed that, from the students’ perspective, educational IS should have LA capabilities to support learning and teaching. Previous studies also reported positive student attitudes towards the use of LA in higher education (Pontual Falcão et al., 2019; ROBERTS et al., 2016).

The survey reported positive results regarding students’ perception of system quality of the artefact. Most students found the system consistent (84.5%) and the response time reasonable (84.5%). This validated that the artefact had improved since the demonstration phase of the study and was seamlessly integrated into the current learning management system without causing significant dificulties to the students (see DP3 and 4). In fact, recent research suggests that, from the students’ perspective, LA should not cause any dificulties in using learning management systems but improving its usage (Pontual Falcão et al., 2019). This result indicates that our design principles are beneficial for designing LAIS and can satisfy the requirements of both lecturers and students.

Last, a majority of students (78.1%) expressed concern about ethical issues regarding how the lecturers would use the information provided by LA. They were also concerned about the transparency of the process (82.5%), data security (73.7%), and data storage (82.5%). The findings not only validate the principle of information availability (DP4) but also provide evidence supporting concepts concerning students perspectives on ethical issues suggested in the literature (PARDO & SIEMENS, 2014; SLADE & PRINSLOO, 2013).

## 6.2.2. Interviews with the lecturers: Identifying side efects or undesirable consequences of using the artefact

Semi-structured interviews were conducted with the four lecturers who used the system in their courses. The interview questions were developed based on the guidelines by WEISS (1995) and included questions related to the usage of the reporting dashboard, perceived usefulness, dificulties, and concerns. In accordance with the definition of semi-structured interviews, the interviewer asked open-ended questions and then followed the participants’ lead with follow-up questions so that they were given the opportunity to clarify or elaborate upon their answers until no additional information was discovered. During the interview, the interviewee was able to interact with the LA dashboard to demonstrate the usage of the IS or illustrate their statements. The interviews were recorded on digital files and transcribed by the researchers. Each interview lasted between 25 and 60 minutes, and the total length of the transcript was 37 pages. To analyse the data, we used thematic analysis, as described by BRAUN and CLARKE (2006) (see Appendix 2). For confidentiality, pseudonyms were used, and identifying details were altered in the transcripts. In addition, some parts of the answers were omitted as they were unrelated or extraneous. These omissions are denoted by ellipses in brackets. Our findings reveal two main themes within the interview data: perceived usability and usefulness and subjective interpretation of the reported information.

The interviews explored the lecturers’ use of the LAIS and its perceived usefulness. All the lecturers reported that the LAIS was beneficial and supported them in monitoring students’ engagement with learning through the semester:

“It is useful to see how many students watched the lecture recordings” (Lecturer 4).

“I was able to be alerted that a particular recording at a particular time has a lot of replays” (Lecturer 3).

“So, it’s actually quite helpful to see at which moment when the peaks occurred. [. . .], well, for short videos it’s very useful because I can just check a few peaks” (Lecturer 2).

The LA information helped the lecturers identify potentially problematic parts of the lecture content. For instance, if students experienced dificulties due to poor sound quality and missed a piece of essential information, this would produce unusual activity at that point in the video, indicating to the lecturer that there is a problem. The lecturer could then revisit that piece of information in the following lecture.

The lecturers also reported that being allowed to observe the content that is most often replayed by the students was useful:

“[I]t’s potentially very useful. I think, for me, the usefulness is being in reinforcing that doing activities in class is worthwhile” (Lecturer 1).

They commented that this insight would help their decision-making when designing the course for the following semester. In particular, the lecturers observed that students spent more time performing fill-in-the-blank exercises, in which students have to fill in missing words in a text, than engaging with the rest of the LTR. As a result, the lecturers aim to use these kinds of exercises to emphasise important knowledge in future courses.

Overall, the LAIS allowed lecturers to evaluate and analyse lecture content online via LTRs. The artefact provided the lecturers with information about the impact of the current lecture design, which will be useful for creating lecture content in the future. However, although the lecturers perceived the LA to be useful, they did report a lack of granularity regarding the visualisations of the aggregated analytics; the total number of replayed segments or completed viewing might not represent students’ actual engagement. For example, it is common for students to skip the title and copyright slides, which leads to a lower completion rate, even if students watch all of the body of the LTR. This negatively influenced the perceived usability and usefulness of the artefact:

“I think maybe the problem is the granularity. To be honest, I found that the diference between completed and not completed is misleading because students are never going to finish, actually complete the video, because there’s a gap on the end, right? In the beginning, there’s a copyright warning, and at the end, there’s a dead space. And I was, generally speaking, too lazy to edit the videos, to make them fully complete” (Lecturer 1).

“[. . .] the diferent graph there would be harder to analyse.” (Lecturer 2).

Despite the challenge of providing suficient information without causing information overload (EDMUNDS & MORRIS, 2000; WARE, 2012), the findings indicate that both aggregated information and highly granular information improve the usefulness of reports for lecturers’ decision-making. LAIS should support customised ad-hoc analyses of learning with diferent units of analysis (e.g., individual learners or a whole class) and time frames (e.g., information aggregated by the day, week, month, or year). Correspondingly, LAIS should report information with a flexible granularity that can deliver satisfying usability and eficacy:

DP1. Principle of actionable information: Should provide reports of actionable information about learners and their learning with flexible granularity in reporting.

The interview also indicated that lecturers could have these biases that afect their behaviour in lots of different ways. Therefore, the finding highlights the need for anonymity in the set of ethical principles for LA (PARDO & SIEMENS, 2014; SLADE & PRINSLOO, 2013). If the anonymity is secured, it may prevent the following scenario reported by the lecturer:

“[. . .] might get quite angry about students not doing things, and not necessarily deliberately penalise them but indirectly, they might think “Well, they didn’t watch that, I’m going to make my whole exam about that” (Lecturer 1)

In addition to anonymity, transparency of the process and data security are the main aspects of ethical principles for LA (PARDO & SIEMENS, 2014; SLADE & PRINSLOO, 2013). The data privacy was identified as the key challenge for the implementation of LA at institutions of higher education (DANIEL, 2015). Concerns have been raised about recording student activities on the system and profiling student learning. GREGOR and JONES (2007) suggest that institutional executive ofices are likely to be concerned about privacy and security issues when the system is up and running. We noticed that the third principle was quite generic and not reflected the nature of data sensitivity in using LA. According to these findings, the principle of information availability (DP4) is revised to address data anonymity, transparency, and security:

DP4. Principle of information anonymity and protection: LAIS Should provide anonymity for personal and protect data against accidental or unlawfu destruction or accidental loss, alteration, unauthorised disclosure or access.

## 6.3. The final set of design principles for learning analytics information systems

The proposed set of design principles for LAIS was developed through the DSR process of theory-inspired development, demonstration with operational prototyping, and case-study based evaluation. Table 3 provides an overview of the final set of design principles for LAIS that support learning and teaching in higher education.

Table 3. LAIS design principles.

<table><tr><td>#</td><td>Design principle</td><td>Design principle specification</td></tr><tr><td>DP1</td><td>Principle of actionable information</td><td>Should provide reports of actionable information about learners and their learning with flexible granularity in reporting.</td></tr><tr><td>DP2</td><td>Principle of information delivery</td><td>Should generate responses and information that visualise learning and teaching behaviour and performance.</td></tr><tr><td>DP3</td><td>Principle of information interoperability</td><td>Should interoperate with any LA and/or educational IS, including VLEs, and enable integration with different data sources without resulting in any discernible issues or complications.</td></tr><tr><td>DP4</td><td>Principle of information anonymity and protection</td><td>Should provide anonymity for personal and protect data against accidental or unlawful destruction or accidental loss, alteration, unauthorised disclosure or access.</td></tr></table>

## 7. Discussion and implications for research and practice

In the following, we discuss our contributions and implications in light of the literature on LA and educational IS as well as the practice of teaching with IS.

As an emerging field of research, LA has been defined as a process of measuring, collecting, analysing and reporting education data (SIEMENS, 2013). We demonstrated how LAIS could automate the LA process, so it has a greater impact on higher education. Although the literature has recognised the potential of LA for supporting and transforming institutional activities, such as educational decision-making, knowledge creation and enhancement of the learning experience (NGUYEN et al., 2017; NISTOR & HERNÁNDEZ-GARCÍAC, 2018), little attention has been paid to the design and development of IS with LA capabilities. This work links previous system designs for LA (BODILY et al., 2018; RUIPÉREZ-VALIENTE et al., 2015; SIEMENS et al., 2014) to provide comprehensive guidelines for developing and implementing LAIS in higher education. Efective design and implementation of LAIS would ofer great values to higher education institutions that are operating in an increasingly complex and competitive environment (DANIEL, 2015).

Our study introduces LAIS as a new class of educational IS. Although such systems may be considered part of other types of educational IS, such as learning management IS (DANIEL, 2015; RUIPÉREZ-VALIENTE et al., 2015), the purpose of their design is diferent from and independent of existing systems. Furthermore, the theories regarding LA have indicated a need to examine LAIS as a new genre of educational IS to maximise its impact in diferent educational settings. Thus, we created a set of design principles for developing and implementing LAIS. Intervention theory (ARGYRIS, 1970) as kernel theories governed our design requirements for LAIS. Through demonstration and evaluation, we show the feasibility of realising this type of IS in the context of higher education.

The theorisation of LAIS as a new class of IS can encourage educational IS researchers to join the force with the research communities in learning sciences to push the LA agenda forward. Furthermore, the conceptualisation of underlying design principles for LAIS would establish the essential foundations for further development and implementation of such systems. There is a significant body of IS literature pertinent to information systems design theory (BASKERVILLE & PRIES-HEJE, 2010; WALLS et al., 1992). IS design principles as design theories ofer simple and elegant functional explanations for generalised solution components of a specific class of IS by the related generalised requirements (BASKERVILLE & PRIES-HEJE, 2010; GREGOR & JONES, 2007).

The goal of LA is to understand and optimise learning and teaching (NISTOR & HERNÁNDEZ-GARCÍAC, 2018; SIEMENS, 2013). The proposed design principles are consistent with this view and our study demonstrates how information systems can deliver certain material properties that allow for the realisation of LA in higher education. Previous research suggested that the success of LA rests on its capability to provide actionable insights from educational data (CLOW, 2013; DAWSON et al., 2015; RL & GYNTHER, 2018). The computational aspects of LA must be well integrated with learning sciences to make a sustainable impact on the research and practice of learning and teaching (DAWSON et al., 2015). Accordingly, the proposed design principles emphasise on generating actionable responses and information that visualise learning and teaching behaviour and performance with flexible granularity in reporting. The actionable insights could be appraised by their ability to encourage users to take necessary actions to improve learning and teaching. For instance, LA dashboard may report at-risk situations from students’ learning activities for lecturers to perform early interventions to improve student retention (DIETZ-UHLER & HURN, 2013; WOLFF et al., 2013). Accordingly, the purpose of LAIS as a new class of IS was described by our design principles as to provide reports of actionable information about learners and their learning with flexible granularity in reporting. This sets out a clear goal for the design and development of LAIS to enhance learning and teaching.

Although the development and implementation of LA may show promising to automate several measurements and predictions about learning and teaching, the singular concentration on learning outcomes and performance, as the principal target of LA, without consideration of learning and teaching processes can have unfavourable consequences (DAWSON et al., 2015; VAN Leeuwen, 2019). Our study shows an example of how LA dashboard can assist lecturers in monitoring student engagement with learning materials to improve teaching and learning. Furthermore, we report empirical evidence supporting that LA should consider flexible granularity in reporting for maximising its efectiveness. (GAŠEVIĆ et al., 2016; SCHUMACHER & IFENTHALER, 2018; SIEMENS et al., 2014). A lack of attention to instructional conditions can lead to inefective use or exploitation of LA (GAŠEVIĆ et al., 2016). The flexible granularity in reporting can allow the LA users for inspecting and adopting actionable insights in accordance with instructional conditions. Correspondingly, the proposed set of design principles highlights the importance of information granularity in the LAIS development.

With regards to the confidential nature of the personal data used by LA, our study shows that for successful LA implementation it is necessary to provide anonymity for personal and protect data against accidental or unlawful destruction or accidental loss, alteration, unauthorised disclosure or access. For instance, the use of personal data and LA process can only be undertaken once they are approved by ethical committees and with consents from the data subjects. As the analysis of data relating to students and their activities is the foundation of LA process, the collection and use of these data face several ethical issues and dilemmas (SLADE & PRINSLOO, 2013). Our study reports that lecturers could have behavioural biases as the outcomes of using LA information. Prior studies indicated a need to contemplate how these ethical issues must be addressed from the early stages of the LA deployment (PARDO & SIEMENS, 2014). Our focus on information anonymity and protection is consistent with the ethical and privacy principles for LA (GRELLER & DRACHSLER, 2012; PARDO & SIEMENS, 2014). The adoption of information anonymity and protection would promote trust and accountability to use LAIS.

With regard to the fragmented nature of educational data and information systems, our study indicates that it is essential for LAIS to incorporate with any educational IS and enable integration with diferent data sources without resulting in any discernible issues or complications. As it is challenging to gather and combine unstructured data from several sources (e.g., learning materials, financial information, etc.) in a single data model (DANIEL, 2015), we propose a service-oriented architecture of LAIS that allows for flexible parallel connections with diferent sources. The proposed design would reduce the dependencies (ARSANJANI, 2004) between distinct LA services and lessen the risks of systematic errors and disruptions in the operation. Furthermore, our empirical data show that, for successful LAIS implementation, the integration with existing IS should not result in any discernible issues or complications.

All design principles proposed in this paper imply material properties that are expected to be embraced for the realisation of LAIS in higher education. Although our proposed design principles are either comprehensive or objectively superior to any other viable meta-requirement, they serve as the basis for LAIS implementation and evaluation. Moreover, following the iterative process of DSR, the set of design principles is grounded by both theories and empirical evidence that reflects the genuine user requirements.

The diversity of DSR has progressively developed over the past decade in diferent facets such as purpose, methodology, philosophical grounding, and mental models (NGUYEN et al., 2019). PEFFERS et al. (2018) document five DSR genres in IS research:

DSRM, IS Design theory (ISDT), Design-oriented IS research (DOIS), Explanatory design theory (EDT), and Action design research (ADR). J IIVARI (2015) suggests two strategies for IS design science research: 1) designing an IT meta-artefact as a solution to a general class of problems and 2) solving a specific problem for a certain group of users and generalising a bundled solution generalised that addresses a class of problems. While ADR approach proposed by SEIN et al. (2011) is more appropriate for the second strategy, DOIS and DSRM share more mutual elements with the first strategy focusing on the design of an IT meta-artefact as a solution to address a general class of problems. Nevertheless, ÖSTERLE et al. (2011) note that DOIS “is not a nonjudgemental scientific discipline; rather it is normative, in the sense that the construction of artefacts is guided by the desire to yield a specific benefit and to satisfy certain objectives” as this approach does not recognise theory building as a DSR activity but as “valid cause-efect relations” that provide “foundations for choosing desirable ends, i.e., normative actions” (WINTER, 2008). Among the five DSR genres, DSRM (PEFFERS et al., 2007) is the best fit to our study as it emphasises on the design and development of applicable artefacts which could have contributions to both theory and practice. IS research artefacts include but do not limit to systems, applications, frameworks, design theories and methods (GREGOR & HEVNER, 2013; HEVNER et al., 2004; TUUNANEN & PEFFERS, 2018).

PEFFERS et al. (2018) further argue that the DSR genres must define “their standards, values, and beliefs flexibly to accommodate innovation and evolution” and “if authors describe and justify their objectives, methods, and results with good, appropriate rationale, their arguments should be given due consideration, even though they do not fit prior patterns” (PEFFERS et al., 2018, p. 136). DSRM artefacts imply generalisability in practice, yet the concept of design theory is not frequently found in the DSRM articles (PEFFERS et al., 2018). Our study intends to go further towards presenting design theories (GREGOR & HEVNER, 2013) than DSRM studies that focus on building an IS. Building on PEFFERS et al. (2007)’s DSRM we contend that the design, implementation, and evaluation of the set of design principles and its instantiation are substantial research contributions (BASKERVILLE et al., 2018).

Design artefacts and design theories have been the two dominant types of DSR contributions (GREGOR & HEVNER, 2013). The literature highlights the importance of coexisting artefact and theory contributions in DSR but also recognises challenges to achieve both (GREGOR & JONES, 2007; HEVNER et al., 2004). Recently, BASKERVILLE et al. (2018) clarify the importance of balancing the technical and scientific contributions of a DSR project. Accordingly, our DSRM approach to the study attempts to accomplish both these two types of contributions. To do so, we first conceptualised the initial set of DP using the principles of intervention theory as kernel theories then instantiated it into the technical architecture and system prototype for demonstration and evaluation (GREGOR & JONES, 2007). Through the implementation and evaluation of the prototype, the proposed DPs were revised with the insights drawing from the authentic environment and end-users. As such, we both theoretically contribute a set of design principles and practically deliver the system architecture and prototype.

Our theory-inspired and practically applicable design principles attempt to address the problem of the lack of guidance in the design and development of LAIS. The development of DPs is rationalised with references to the findings of prior studies in LA and based on the IS kernel theories while the implementation and evaluation of the instantiated system in a real context enhances the practicability of the set of DPs since it is refined with empirical evidence. The design principles are recognised as contributions in the form of nascent design theory (GREGOR & HEVNER, 2013; GREGOR & JONES, 2007).

J IIVARI (2020) criticised that kernel theories borrowed from reference disciplines often lack technological substance and substantive technological theories should be design-oriented. However, we argue that merely technological theories may not lead to an efective and optimal solution for the problem in the domain of reference. We suggest that a balance of both substantive technological theories and situated knowledge drawn from the reference domain is needed for producing useful design and evolving design knowledge. Likewise, BROCKE Vom et al. (2020) suggest that it is essential to engage DSR in the problem and solution spaces to maximise its impact. Our study attempted to demonstrate a DSRM approach incorporating both designoriented substance and kernel theories from the reference domain to ofer useful solutions to the identified problem. Our DSRM approach supports the study to provide both design knowledge and artefacts situated in both problem and solution spaces of LA in higher education. As a result, our study also delivers the technical architecture which can be adopted for developing LAIS that embraces the proposed design principles. Furthermore, previous discussions surrounding DSR indicate that a situated implementation of an artefact can be considered as a suficient knowledge contribution (BASKERVILLE et al., 2018; GREGOR & HEVNER, 2013). Our case study ofers insights into the realisation of LA in the context of higher education.

Higher education has been subject to a series of major challenges in the past decade (DANIEL, 2015; PUCCIARELLI & KAPLAN, 2016). The institutions are required to improve their capabilities for the three main missions: teaching, research, and public service. Previous research showed the huge potential of utilising educational data to support institutional activities (NGUYEN et al., 2017; WAGNER & ICE, 2012). Nevertheless, a systematic understanding of how to apply LA is still lacking. It is also hoped that this work will generate fresh insight into LAIS as a new class of educational IS and contribute to a deeper understanding of underlying design theories for LAIS. Consequently, this study seeks to support higher education institutions to design, develop, and implement LAIS as means to improve their capabilities in teaching, research, and public services.

DAWSON et al. (2015) suggested that the design and development of LA should be “better integrated into existing educational research and note the implications for LA research and practice” (p. 65). Our DP1 and DP2 clearly supported this point by calling for afordances to provide theory-inspired actionable insights with the timing that can maximise the efectiveness of reported information. The actionable insights can allow a corrective procedure, or feedback loop, to be established for a set of pedagogic actions (RL & GYNTHER, 2018). LAIS guided by our DPs would improve learning and teaching by ofering these actionable insights to the end-users. For instance, the actionable insights enabling feedback loop would trigger the self-regulated hence enhance learning performance (YAMADA et al., 2017).

Our findings also contribute to the literature on educational technology, which has recognised LA as a promising technology in education transformations (PEÑA-AYALA, 2018). The study demonstrates that to successfully use LA, it is necessary to consider the conflicts of interest between diferent groups of education stakeholders. Information granularity benefits data clients, but it causes ethical concerns for the data subjects. Our study provides empirical evidence confirming the conceptualised sets of ethical issues proposed by PARDO and SIEMENS (2014) and SLADE and PRINSLOO (2013).

From the lecturers’ perspective, the findings indicate that the design and development of LAIS should consider the importance of the end-user experience (i.e. the ease of use and access as well as the appropriateness and flexibility of the delivered information). The DSR paradigm and literature encourage scholars to report successes and failures when planning future research (LOBATO et al., 2015). Perhaps DSR researchers, as practitioners of teaching in higher education and as scholars, should consider their successes and failures to avoid failures and leverage successes in their future endeavours to apply LA in higher education and, especially, develop LAIS.

The ability to report insightful information has been identified as a salient feature of LA. While this element is conceptualised in our principle of actionable reporting (DP1), we ofer a more detailed description of the main afordances of LAIS and explicit guidance for designing such IS, which are essential to support the development and implementation of LAIS and utilise LA in higher education.

## 8. Concluding remarks

This study proposed LAIS as a class of educational information systems and aimed to establish its design principles. We developed and implemented a fully functioning prototype as an instance of such systems to illustrate the proposed design principles. Through the DSR process of developing and evaluating a set of design principles for LAIS, this study makes both practical and theoretical contributions to the fields of educational technology, IS, and DSR. As e-learning has become a fundamental part of the learning experience in higher education, LAIS presented great opportunities for learning and teaching. The development and implementation of an operational LAIS prototype and the case-study based evaluation show that the proposed LAIS design has the potential to provide teachers with useful LA information. With timely and accurate information about learning and teaching in their classes, lecturers can adjust their pedagogical activities and make appropriate decisions. The LAIS design principles were evaluated and improved from both the lecturer and student perspectives to avoid potential conflicts of interest. Thus, the proposed LAIS design can serve as a guideline for further development and implementation of LA to support learning and teaching. Also, this study provides useful information about the LA services and functionalities that lecturers appreciate to commercial stakeholders, IS developers, and engineers.

This study has some limitations. First, rather than focusing on the fundamental purpose of LA and the requirements from the stakeholders, the design principles of LAIS could be conceptualised diferently. Second, although we demonstrated and evaluated our set of design principles, additional rounds of demonstration and evaluation could be conducted in a diferent context to revise the design principles to ensure their generalisability. Third, we believe that, given a year’s experience with LA, the lecturers will ask for new features and services beyond those that automatically inform them about student engagement. Finally, further research could examine LAIS design principles in the context of diferent LA modules in higher education.

## Disclosure statement

No potential conflict of interest was reported by the authors.

## ORCID

Tuure Tuunanen http://orcid.org/0000-0001-7119-1412

## References

ARGYRIS, C. (1970). Intervention theory and method: A behavioral science view. Addison-Wesley.

ARNOLD, K., & PISTILLI, M. D. (2012) Course signals: using learning analytics to increase student success. In Proceedings of the 2nd International Conference on Learning Analytics and Knowledge pp 267–270, ACM, Vancouver, Canada.

ARSANJANI, A. (2004). Service-oriented modeling and architecture: How to identify, specify, and realize services for your SOA. In IBM developer works (pp. 1–15), IBM.

BAKER, R., & INVENTADO, P. S. (2014). Educational data mining and learning analytics. In J. A. Larusson & B. White (Eds.), Learning Analytics: From Research to Practice (pp. 61–75). Springer.

BAKHARIA, A., CORRIN, L., DE Barba, P., KENNEDY, G., GAŠEVIĆ, D., MULDER, R., WILLIAMS, D., DAWSON, S., & LOCKYER, L. (2016) A conceptual framework linking learning design with learning analytics. In Proceedings of the 6th International Conference on Learning Analytics and Knowledge pp 329–338, ACM Press, New York, USA. Available at: http://dl.acm.org/citation.cfm? doid=2883851.2883944.

BASILI, V. R., BOEHM, B. W., ROMBACH, H. D., & ZELKOWITZ, M. V. (2005). Foundations of empirical software engineering. (B. Boehm, H. D. Rombach, & M. V. Zelkowitz, Eds). Springer.

BASKERVILLE, R. ;., BAIYERE, A. ;., GREGOR, S. ;., HEVNER, A. ;., ROSSI, M., BASKERVILLE, R., BAIYERE, A., GREGOR, S., & HEVNER, A. (2018). Design science research contributions: finding a balance between artifact and theory. Journal of the Association for Information Systems, 19(5), 358–376. Available at: https:// aisel.aisnet.org/jais/vol19/iss5/3/

BASKERVILLE, R., & PRIES-HEJE, J. (2010). Explanatory design theory. Business & Information Systems Engineering, 2(5), 271–282. Available at http://link. springer.com/10.1007/s12599-010-0118-4

BECKER, S. A., BECKER, S. A., CUMMINS, M., DAVIS, A., FREEMAN, A., HALL, C. G., & ANANTHANARAYANAN, V. (2017). NMC Horizon Report: 2017 Higher Education Edition. The New Media Consortium.

BEYNON-DAVIES, P. (1998). Information systems development: An Introduction to Information Systems Engineering. Macmillan International Higher Education.

BODILY, R., IKAHIHIFO, T. K., MACKLEY, B., & GRAHAM, C. R. (2018). The design, development, and implementation of student-facing learning analytics dashboards. Journal of Computing in Higher Education, 30(3), 572–598. Available at http://link.springer.com/10. 1007/s12528-018-9186-0

BOS, N., GROENEVELD, C., VAN Bruggen, J., & BRAND-GRUWEL, S. (2016). The use of recorded lectures in

education and the impact on lecture attendance and exam performance. British Journal of Educational Technology, 47(5), 906–917. Available at: https://doi.org/10.1111/bjet. 12300

BOUDREAU, M.-C., GEFEN, D., & STRAUB, D. W. (2001). Validation in information systems research: a state-of-the -art assessment. MIS Quarterly, 25(1), 1. Available at https://www.jstor.org/stable/3250956?origin=crossref

BRAUN, V., & CLARKE, V. (2006). Using thematic analysis in psychology. Qualitative Research in Psychology, 3(2), 77–101. Available at: http://www.tandfonline.com/doi/ abs/10.1191/1478088706qp063oa

BROCKE Vom, J., WINTER, R., HEVNER, A., & MAEDCHE, A. (2020). Special issue editorial – Accumulation and evolution of design knowledge in design science research: A journey through time and space. Journal of the Association for Information Systems, 21(3), 520–544. Available at: https://aisel.aisnet. org/jais/vol21/iss3/9

BROWN, M. (2020). Seeing students at scale: How faculty in large lecture courses act upon learning analytics dashboard data. Teaching in Higher Education, 25(4), 384–400. https://doi.org/10.1080/13562517.2019.1698540

BUTLER, A. C., KARPICKE, J. D., & ROEDIGER, H. L. (2007). The efect of type and timing of feedback on learning from multiple-choice tests. Journal of Experimental Psychology. Applied, 13(4), 273–281. https://doi.org/10.1037/1076-898X.13.4.273

CARINI, R., KUH, G., & KLEIN, S. (2006). Student engagement and student learning: testing the linkages. Research in Higher Education, 47(1), 1–32. Available at: http://www.springerlink.com/index B8M6T51V83732308.pdf

Chandra Kruse, L., SEIDEL, S., & PURAO, S. (2016). Making use of design principles. J. Parsons, T. Tuunanen, B. Venable, J. Donnellan, M. Helfert, & J. Kenneally. Eds., Tackling Society’s Grand Challenges with Design Science. DESRIST 2016 37–51. Springer, Cham. Available at http://link.springer.com/10.1007 978-3-319-39294-3\_3

CHANDRA, L., SEIDEL, S., & GREGOR, S. (2015) Prescriptive knowledge in IS research: conceptualizing design principles in terms of materiality, action, and boundary conditions. In 2015 48th Hawaii International Conference on System Sciences pp 4039–4048, IEEE, HI, USA. Available at: http://ieeexplore.ieee.org/document 7070304/.

CHATTERJEE, S., XIAO, X., ELBANNA, A., & SARKER, S. (2017) The information systems artifact: a conceptualization based on general systems theory. In Proceedings of the 50th Hawaii International Conference on System Sciences, HI, USA.

CHATTI, M. A., DYCKHOFF, A. L., SCHROEDER, U., & THÜS, H. (2012). A reference model for learning analytics. International Journal of Technology Enhanced Learning, 4(5/6), 318–331. Available at: http://www. inderscienceonline.com/doi/abs/10.1504/IJTEL.2012. 051815

CHATTI, M. A., LUKAROV, V., THÜS, H., MUSLIM, A., YOUSEF, A. M. F., WAHID, U., GREVEN, C., CHAKRABARTI, A., & SCHROEDER, U. (2014). Learning analytics: challenges and future research directions. Eleed, Iss. 10. Available at https://eleed.cam pussource.de/archive/10/4035

CHAURASIA, S. S., KODWANI, D., LACHHWANI, H., & KETKAR, M. A. (2018). Big data academic and learning analytics. International Journal of Educational Management,

32(6), 1099–1117. Available at https://www.emeraldinsight. com/doi/10.1108/IJEM-08-2017-0199

CLOW, D. (2013). An overview of learning analytics. Teaching in Higher Education, 18(6), 683–695. Available at: http://srhe.tandfonline.com/doi/abs/10.1080/ 13562517.2013.827653

DAHLSTROM, E., BROOKS, D. C., & BICHSEL, J. (2014) The current ecosystem of learning management systems in higher education: Student, faculty, and IT perspectives. EDUCAUSE Review. Available at: http://www.educause. edu/ecar.2014

DANIEL, B. (2015). Big data and analytics in higher education: opportunities and challenges. British Journal of Educational Technology, 46(5), 904–920. Available at: http://onlinelibrary.wiley.com/doi/10.1111/bjet.12230/ full

DANIEL, B. (2017). Big Data and data science: A critica review of issues for educational research. British Journal of Educational Technology, 50(1), 101–113. Available at https://doi.org/http://doi.wiley.com/10.1111/bjet.12595

DAVIS, A. M. (1992). Operational prototyping: a new development approach. IEEE Software, 9(5), 70–78. Available at http://ieeexplore.ieee.org/document/156899/

DAVIS, A. M., DIESTE, O., HICKEY, A., JURISTO, N., & MORENO, A. M. (2006) Efectiveness of requirements elicitation techniques: Empirical results derived from a systematic review. In 14th IEEE International Requirements Engineering Conference (RE’06) pp 179–188, IEEE, MN, USA. Available at: http://ieeex plore.ieee.org/document/1704061/.

DAWSON, S., GAŠEVIĆ, D., & SIEMENS, G. (2014) Current state and future trends: A citation network analysis of the learning analytics field. Proceedings of the 4th International Conference on Learning Analytics And Knowledge, IN, USA. Available at: http://dl.acm.org/cita tion.cfm?id=2567585 .

DAWSON, S., GAŠEVIĆ, D., & SIEMENS, G. (2015). Let’s not forget: learning analytics are about learning. TechTrends, 59(1), 64–71. Available at http://link. springer.com/article/10.1007/s11528-014-0822-x

DIETZ-UHLER, B., & HURN, J. E. (2013). Using learning analytics to predict (and improve) student success: a faculty perspective. Journal of Interactive Online Learning, 12(1), 17–26. Available at: https://eric.ed.gov/? id=EJ1032978

DUVAL, E. (2011) Attention please!: learning analytics for visualization and recommendation. In Proceedings of the 1st International Conference on Learning Analytics and Knowledge pp 9–17, ACM, Banf, Canada.

DYCKHOFF, A. L., ZIELKE, D., BÜLTMANN, M., CHATTI, M. A., & SCHROEDER, U. (2012). Design and implementation of a learning analytics toolkit for teachers. Journal of Educational Technology & Society, 15(3), 58–76. Available at https://www.jstor.org/stable/ pdf/jeductechsoci.15.3.58.pdf

EDMUNDS, A., & MORRIS, A. (2000). The problem of information overload in business organisations: a review of the literature. International Journal of Information Management, 20(1), 17–28. https://doi.org/10.1016/ S0268-4012(99)00051-1

FLINK, R. (2014). Operational prototyping a tool for delivering value. Healthcare Financial Management : Journal of the Healthcare Financial Management Association, 68 (6), 116–123. Available at https://www.ncbi.nlm.nih.gov/ pubmed/24968635

GAŠEVIĆ, D., DAWSON, S., ROGERS, T., & GAŠEVIĆ, D. (2016). Learning analytics should not promote one size

fits all: the efects of instructional conditions in predicting academic success. The Internet and Higher Education, 28, 68–84. https://doi.org/10.1016/j.iheduc.2015.10.002

GAVRIUSHENKO, M., SAARELA, M., & KÄRKKÄINEN, T. (2017) Towards evidence-based academic advising using learning analytics. In International Conference on Computer Supported Education pp 44–65, Springer, Cham, Porto, Portugal. Available at: https://link. springer.com/chapter/10.1007/978-3-319-94640-5\_3.

GOLDSTEIN, P. J., & KATZ, R. N. (2005). Academic analytics: the uses of management information and technology in higher education. EDUCAUSE, 8(1), 1–12. Available at https://library.educause.edu/resources/2005 12/academic-analytics-the-uses-of-managementinformation-and-technology-in-higher-education

GREGOR, S., & HEVNER, A. R. (2013). Positioning and presenting design science research for maximum impact. MIS Quarterly, 37(2), 337–355. https://doi.org/10.25300 MISQ/2013/37.2.01

GREGOR, S., & JONES, D. (2007). The anatomy of a design theory. Journal of the Association for Information Systems, 8(5), 312–355. Available at http://aisel.aisnet.org/jais vol8/iss5/19

GRELLER, W., & DRACHSLER, H. (2012). Translating learning into numbers: a generic framework for learning analytics. Educational Technology & Society, 15(3), 42–57. Available at: https://www.jstor.org/stable/pdf/jeductech soci.15.3.42.pdf

HATHAWAY, W. E. (1985). Hopes and Possibilities for Educational Information Systems. Paper presented at the invitational conference Information Systems and School Improvement: Inventing the Future, UCLA Centerfor the Study of Evaluation, Los Angeles. Available at: https://eric.ed.gov/?id=ED253560.

HENDERSON, M., SELWYN, N., & ASTON, R. (2017). What works and why? Student perceptions of ‘useful digital technology in university teaching and learning. Studies in Higher Education, 42(8), 1567–1579. https:/ doi.org/10.1080/03075079.2015.1007946

HEVNER, A. R., MARCH, S. T., PARK, J., & RAM, S. (2004). Design science in information systems research. MIS Quarterly, 28(1), 75–105. https://doi.org/10.2307 25148625

IFENTHALER, D., GIBSON, D., & DOBOZY, E. (2018). Informing learning design through analytics: applying network graph analysis. Australasian Journal of Educational Technology, 34(2), 117–132, Available at https://www.ajet. org.au/index.php/AJET/article/view/3767.

IFENTHALER, D., & WIDANAPATHIRANA, C. (2014). Development and validation of a learning analytics framework: two case studies using support vector machines. Technology, Knowledge and Learning, 19(1–2), 221–240. Available at http://link.springer.com/10.1007/s10758-014- 9226-4

IIVARI, J. (2015). Distinguishing and contrasting two strategies for design science research. European Journal of Information Systems, 24(1), 107–115. Available at https:/ www.tandfonline.com/doi/full/10.1057/ejis.2013.35

IIVARI, J. Information system artefact or information system application: that is the question. (2017). Information Systems Journal, 27(6), 753–774. Available at https://doi. org/10.1111/isj.12121

IIVARI, J. (2020). editorial: A critical look at theories in design science research. Journal of the Association for Information Systems, 21(3), 502–519. Available at https://aisel.aisnet.org/jais/vol21/iss3/10

JÄRVELÄ, S., MALMBERG, J., HAATAJA, E., SOBOCINSKI, M., & KIRSCHNER, P. A. (2019). What multimodal data can tell us about the students’ regulation of their learning process? Learning and Instruction. Available at: https://doi.org/10.1016/j.learninstruc.2019.04.004

KAHU, E. (2013). Framing student engagement in higher education. Studies in Higher Education, 38(5), 758–773. Available at: http://srhe.tandfonline.com/doi/abs/10. 1080/03075079.2011.598505

KLEM, A., & CONNELL, J. (2004). Relationships matter: linking teacher support to student engagement and achievement. Journal of School Health, 74(7), 262–273. Available at: http://onlinelibrary.wiley.com/doi/10.1111/ j.1746-1561.2004.tb08283.x/full

KRUMM, A. E., WADDINGTON, R. J., TEASLEY, S. D., & LONN, S. (2014). Learning analytics. The SAGE Encyclopedia of Educational Technology. Springer. Available at: http://link.springer.com/10.1007/978- 1-4614-3305-7

LACITY, M. C., SCHEEPERS, R., & WILLCOCKS, L. P. (2018). Cognitive automation as part of Deakin university’s digital strategy. MIS Quarterly Executive, 17 (2), 89–107. Available at https://aisel.aisnet.org/misqe/ vol17/iss2/4

LAWLESS, K., & BROWN, S. (1997). Multimedia learning environments: issues of learner control and navigation. Instructional Science, 25(2), 117–131. Available at: http:/ www.springerlink.com/index/U736J42W0226648X.pdf

LEIDNER, D. E., & JARVENPAA, S. L. (1995). The use of information technology to enhance management school education: a theoretical view. MIS Quarterly, 19(3), 265. Available at https://www.jstor.org/stable/249596?origin= crossref

LEONY, D., PARDO, A., DE LA Fuente Valentín, L., DE Castro, D. S., & KLOOS, C. D. (2012) GLASS: a learning analytics visualization tool. In Proceedings of the 2nd International Conference on Learning Analytics and Knowledge pp 162–163, ACM, Vancouver, Canada.

LOBATO, J., WALTERS, C., HOHENSEE, C., & GRUVER, J. (2015) Leveraging failure in design research. ZDM Mathematics Education 47(6), 963–979, Springer. Available at: http://link.springer.com/article/10. 1007/s11858-015-0695-2 .

Lwoga, E. (2014). Critical success factors for adoption of web-based learning management systems in Tanzania. International Journal of Education and Development using ICT, 10(1).Chicago. Available at: https://www.learn techlib.org/p/147447/

MANGAROSKA, K., & GIANNAKOS, M. (2017). Learning analytics for learning design: towards evidence-driven decisions to enhance learning. In European conference on technology enhanced learning (pp. 428–433), Springer, Tallinn, Estonia. Available at: http://link. springer.com/10.1007/978-3-319-66610-5\_38.

MAYER, R. E. (2008). Applying the science of learning: evidence-based principles for the design of multimedia instruction. American Psychologist, 63(8), 760–769. https://doi.org/10.1037/0003-066X.63.8.760

MERTENS, R., SCHNEIDER, H., & MÜLLER, O. (2004) Hypermedia navigation concepts for lecture recordings. In E-Learn: World Conference on E-Learning in Corporate, Government, Healthcare, and Higher Education (pp. 2840–2847). Association for the Advancement of Computing in Education (AACE), Washington DC, USA. Available at: http://www2.inf.uos. de/papers\_pdf/2004\_02.pdf

NGUYEN, A., GARDNER, L., & SHERIDAN, D. (2017) A multi-layered taxonomy of learning analytics applications. In Pacific Asia Conference on Information Systems (PACIS) 2017 Proceedings, Langkawi, Malaysia. Available at: http://aisel.aisnet.org/pacis2017/54/.

NGUYEN, A., GARDNER, L., & SHERIDAN, D. (2018) Building an ontology of learning analytics. In Pacific Asia Conference on Information Systems (PACIS) 2018 Proceedings Yokohama, Japan.

NGUYEN, A., GARDNER, L., & SHERIDAN, D. (2019) Towards ontology-based design science research for knowledge accumulation and evolution. In Hawaii International Conference on System Sciences (HICSS), HI, USA.

NGUYEN, A., GARDNER, L., & SHERIDAN, D. (2020) A design methodology for learning analytics information systems: informing learning analytics development with learning design. In Hawaii International Conference on System Sciences (HICSS), HI, USA.

NGUYEN, T. M., SCHIEFER, J., & TJOA, A. M. (2005) Sense & response service architecture (SARESA). In Proceedings of the 8th ACM international workshop on Data warehousing and OLAP - DOLAP p 77, ACM Press, New York, USA. Available at: http://portal.acm.org/cita tion.cfm?doid=1097002.1097015.

NISTOR, N., & HERNÁNDEZ-GARCÍAC, Á. (2018). What types of data are used in learning analytics? An overview of six cases. Computers in Human Behavior, 89(1), 335–338. Available at https://doi.org/10.1016/j.chb.2018.07.038

NOROOZI, O., ALIKHANI, I., JÄRVELÄ, S., KIRSCHNER, P. A., JUUSO, I., & SEPPÄNEN, T. (2019). Multimodal data to design visual learning analytics for understanding regulation of learning. Computers in Human Behavior, 100(1), 298–304. https://doi.org/10. 1016/j.chb.2018.12.019

OIGARA, J. N., ONCHWARI, G., KEENGWE, J., & GLOBAL, I. G. I. (2014). Promoting active learning through the flipped classroom model. IGI Global, Hershey, Pennsylvania.

ÖSTERLE, H., BECKER, J., FRANK, U., HESS, T., KARAGIANNIS, D., KRCMAR, H., LOOS, P., MERTENS, P., OBERWEIS, A., & SINZ, E. J. (2011). Memorandum on design-oriented information systems research. European Journal of Information Systems, 20 (1), 7–10. Available at https://www.tandfonline.com/doi full/10.1057/ejis.2010.55

PARDO, A., & SIEMENS, G. (2014). Ethical and privacy principles for learning analytics. British Journal of Educational Technology, 45(3), 438–450. https://doi.org 10.1111/bjet.12152

PEFFERS, K., TUUNANEN, T., & NIEHAVES, B. (2018). Design science research genres: Introduction to the special issue on exemplars and criteria for applicable design science research. European Journal of Information Systems, 27(2), 129–139. Available at https://www.tand fonline.com/doi/full/10.1080/0960085X.2018.1458066

PEFFERS, K., TUUNANEN, T., & ROTHENBERGER, M. A. (2007) A design science research methodology for information systems research. Journal of Management Information System, 24(3), 45–77. Available at: http://www.tandfonline. com/doi/abs/10.2753/MIS0742-1222240302 .

PEÑA-AYALA, A. (2018). Learning analytics: A glance of evolution, status, and trends according to a proposed taxonomy. Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 8(3), e1243. Available at https://doi.org/http://doi.wiley.com/10.1002/widm.1243

PERSICO, D., & POZZI, F. (2015). Informing learning design with learning analytics to improve teacher

inquiry. British Journal of Educational Technology, 46 (2), 230–248. https://doi.org/10.1111/bjet.12207

PICCIANO, A. (2012). The evolution of big data and learning analytics in American higher education. Journal of Asynchronous Learning Networks, 16(3), 9–20. Available at https://eric.ed.gov/?id=EJ982669

PICCOLI, G., BARTOSIAK, M. Ł., PALESE, B., & RODRIGUEZ, J. (2019). Designing scalability in required in-class introductory college courses. Information & Management, 103263. Available at: https://linkinghub. elsevier.com/retrieve/pii/S0378720619300394

Pontual Falcão, T., FERREIRA, R., Lins Rodrigues, R., DINIZ, J., & GAŠEVIĆ, D. (2019) Students’ perceptions about learning analytics in a brazilian higher education institution. In Proceedings - IEEE 19th International Conference on Advanced Learning Technologies, ICALT 2019 pp 204–206, Institute of Electrical and Electronics Engineers Inc, Maceió, Brazil.

PORTER, W. W., GRAHAM, C. R., SPRING, K. A., & WELCH, K. R. (2014). Blended learning in higher education: institutional adoption and implementation. Computers & Education, 75(1), 185. https://doi.org/10. 1016/j.compedu.2014.02.011

PUCCIARELLI, F., & KAPLAN, A. (2016). Competition and strategy in higher education: managing complexity and uncertainty. Business Horizons, 59(3), 311–320. https://doi.org/10.1016/j.bushor.2016.01.003

REIMANN, P. (2016). Connecting learning analytics with learning research: the role of design-based research. Learning: Research and Practice, 2(2), 130–142. Available at: https://doi.org/10.1080/23735082.2016.1210198

RL, J. Ø. R. N. Ø., & GYNTHER, K. (2018). What constitutes an “actionable insight” in learning analytics? Journa of Learning Analytics, 5(3), 198–221. https://doi.org/10. 18608/jla.2018.53.13

ROBERTS, L. D., HOWELL, J. A., SEAMAN, K., & GIBSON, D. C. (2016). Student attitudes toward learning analytics in higher education: “the fitbit version of the learning world”. Frontiers in Psychology, 7(1), 1–11. Available at: http://journal.frontiersin.org/article/10. 3389/fpsyg.2016.01959/full

ROEHL, A., REDDY, S. L., & SHANNON, G. J. (2013). The Flipped Classroom: An Opportunity To Engage Millennial Students Through Active Learning Strategies. Journal of Family and Consumer Sciences, 105(2), 44. https://doi.org/10.14307/JFCS105.2.12

RUBIO-FERNÁNDEZ, A., MUÑOZ-MERINO, P. J., & Delgado KLOOS, C. (2019). A learning analytics tool for the support of the flipped classroom. Computer Applications in Engineering Education, 27(5), 1168–1185. Available at: https://onlinelibrary.wiley.com/ doi/abs/10.1002/cae.22144

RUIPÉREZ-VALIENTE, J. A., MUÑOZ-MERINO, P. J., LEONY, D., & KLOOS, C. D. (2015). ALAS-KA: A learning analytics extension for better understanding the learning process in the Khan Academy platform. Computers in Human Behavior, 47(1), 139–148. https:// doi.org/10.1016/j.chb.2014.07.002

RUIZ, J., DÍAZ, H., & RUIPÉREZ-VALIENTE, J. (2014) Towards the development of a learning analytics extension in open edX. In Proceedings of the Second International Conference on Technological Ecosystems for Enhancing Multiculturality (pp. 299–306), Salamanca, Spain. Available at: http://dl.acm.org/citation.cfm?id=2669914

SAARELA, M., & KÄRKKÄINEN, T. (2017). Knowledge discovery from the programme for international student assessment. In Peña-Ayala, A. (Ed.), Learning Analytics:

Fundaments, Applications, and Trends (pp. 229–267). Springer, Cham. Available at http://link.springer.com 10.1007/978-3-319-52977-6\_8

SCHUMACHER, C., & IFENTHALER, D. (2018). Features students really expect from learning analytics. Computers in Human Behavior, 78(1), 397–407. https://doi.org/10. 1016/j.chb.2017.06.030

SEIN, M. K., HENFRIDSSON, O., PURAO, S., ROSSI, M., & LINDGREN, R. (2011). Action design research. MIS Quarterly: Management Information Systems, 35(1), 37–56. https://doi.org/10.2307/23043488

SHIMADA, A., KONOMI, S., & OGATA, H. (2018). Realtime learning analytics system for improvement of on-site lectures. Interactive Technology and Smart Education, 15 (4), 314–331. Available at https://www.emeraldinsight. com/doi/10.1108/ITSE-05-2018-0026

SIEMENS, G. (2013). Learning analytics: The emergence of a discipline. American Behavioral Scientist, 57(10), 1380–1400. Available at: https://doi.org/10.1177%2F0002764213498851

SIEMENS, G., GAŠEVIĆ, D., HAYTHORNTHWAITE, C., DAWSON, S., SHUM, S. B., FERGUSON, R., DUVAL, E., VERBERT, K., & BAKER, R. S. J. D. (2014) Open Learning Analytics: An integrated & modularized platform. Available at: https://solaresearch.org/core open-learning-analytics-an-integrated-modularizedplatform/.

SIEMENS, G., & LONG, P. (2011). Penetrating the fog: Analytics in learning and education. EDUCAUSE Review, 46(5), 30.Available at: https://www.learntechlib.org/p 183382/

SLADE, S., & PRINSLOO, P. (2013). Learning analytics ethical issues and dilemmas. American Behavioral Scientist, 57(10), 1510–1529. Available at: https://doi. org/10.1177/0002764213479366

TE’ENI, D. (1991). Feedback in DSS as a source of control: Experiments with the timing of feedback. Decision Sciences, 22(3), 644–655. Available at: https://doi.org/10. 1111/j.1540-5915.1991.tb01287.x

TREMBLAY, M., HEVNER, A., & BERNDT, D. (2010). Focus groups for artifact refinement and evaluation in design research. Communications of the Association for Information Systems, 26(1), 559–618. Available at https:/ aisel.aisnet.org/cais/vol26/iss1/27.

TUUNANEN, T., & PEFFERS, K. (2018). Population targeted requirements acquisition. European Journal of Information Systems, 27(6), 686-711. Available at https://www.tandfonline.com/doi/full/10.1080/ 0960085X.2018.1476015

TUUNANEN, T., PEFFERS, K., & GENGLER, C. (2008) Wide audience requirements engineering (WARE): A practical method and case study. All Sprouts Content. Helsinki School of Economics. Available at: https://aisel. aisnet.org/sprouts\_all/83.

VAN Leeuwen, A. (2019). Teachers’ perceptions of the usability of learning analytics reports in a flipped university course: When and how does information become actionable knowledge? Educational Technology Research and Development, 67(5), 1043–1064. https://doi.org/10. 1007/s11423-018-09639-y

VENABLE, J., PRIES-HEJE, J., & BASKERVILLE, R. (2012). A comprehensive framework for evaluation in design science research (423–438). Springer, Berlin. Available athttp://link.springer.com/10.1007/978-3-642-29863-9\_ 31

VERBERT, K., DUVAL, E., KLERKX, J., GOVAERTS, S., & SANTOS, J. L. (2013). Learning analytics dashboard

applications (pp. 0002764213479363). American Behavioral Scientist.

VIEIRA, C., PARSONS, P., & BYRD, V. (2018). Visua learning analytics of educational data: A systematic literature review and research agenda. Computers and Education, 122(1), 119–135. https://doi.org/10.1016/j. compedu.2018.03.018

WAGNER, E., & ICE, P. (2012). Data changes everything: delivering on the promise of learning analytics in higher education. Educause Review, 47(4), 32. Available at: https://eric.ed.gov/?id=EJ981214

WALLS, J. G., WIDMEYER, G. R., & El Sawy, O. A. (1992). Building an information system design theory for vigilant EIS. Information Systems Research, 3(1), 36–59. https:// doi.org/10.1287/isre.3.1.36

WARE, C. (2012). Information visualization: Perception for design. Morgan Kaufmann.

WEISS, R. S. (1995). Learning from strangers : The art and method of qualitative interview studies. Simon and Schuster.

WIELING, M., & HOFMAN, W. (2010). The impact of online video lecture recordings and automated feedback on student performance. Computers & Education, 54(4), 992–998. Available at: http://www.sciencedirect.com science/article/pii/S0360131509002784

WIGGINS, G. P., & MCTIGHE, J. (2005). Understanding by design (2nd ed.). Association for Supervision and Curriculum Development(ASCD).

WILLIAMS, A., BIRCH, E., & HANCOCK, P. (2012). The impact of online lecture recordings on student performance. Australasian Journal of Educational Technology, 28(2), 199–213. Available at: http://ascilite. org.au/ajet/submission/index.php/AJET/article/view/869

WINTER, R. (2008). Design science research in Europe. European Journal of Information Systems, 17(5), 470–475. Available at https://www.tandfonline.com/doi/ full/10.1057/ejis.2008.44

WISE, A. F., & JUNG, Y. (2019). Teaching with analytics: Towards a situated model of instructional decision-making. Journal of Learning Analytics, 6(2), 53–69. Available at: https://epress.lib.uts.edu.au/journals/ index.php/JLA/article/view/6357

WOLFF, A., ZDRAHAL, Z., NIKOLOV, A., & PANTUCEK, M. (2013) Improving retention: Predicting at-risk students by analysing clicking behaviour in a virtual learning environment. In Proceedings of the 3rd International Conference on Learning Analytics and Knowledge pp 145–149, ACM, Leuven, Belgium.

XING, W., GUO, R., PETAKOVIC, E., & GOGGINS, S. (2015). Participation-based student final performance prediction model through interpretable Genetic Programming: Integrating learning analytics, educationa data mining and theory. Computers in Human Behavior, 47(1), 168–181. https://doi.org/10.1016/j.chb.2014.09.034

YAMADA, M., SHIMADA, A., OKUBO, F., OI, M., KOJIMA, K., & OGATA, H. (2017). Learning analytics of the relationships among self-regulated learning, learning behaviors, and learning performance. Research and Practice in Technology Enhanced Learning, 12(1), 13. Available at: http://telrp.springeropen.com/articles/10. 1186/s41039-017-0053-9

ZHANG, J., ZHANG, X., JIANG, S., Ordóñez DE Pablos, P., & SUN, Y. (2018). Mapping the study of learning analytics in higher education. Behaviour & Information Technology, 37(10–11), 1142–1155. Available at https:// www.tandfonline.com/doi/full/10.1080/0144929X.2018. 1529198

Appendix 1. Student Survey Questions and Results

<table><tr><td>Constructs</td><td>Based on</td><td>Code</td><td>Question</td></tr><tr><td rowspan="7">Use of learning analytics by lecturers/teachers (UT)</td><td colspan="3">Would you agree that the learning system (e.g., Canvas) should provide lecturers the following information?</td></tr><tr><td></td><td>UT01</td><td>Early alerts of students that are at risk of failing.</td></tr><tr><td>NGUYEN et al. (2017)</td><td>UT02</td><td>Notifications about learning content that students appear to find difficult to understand.</td></tr><tr><td></td><td>UT03</td><td>A summary of individuals&#x27; learning progress, including when and how a particular student learned.</td></tr><tr><td></td><td>UT04</td><td>A summary of the overall learning progress of the class, including when and how the class learned.</td></tr><tr><td></td><td>UT05</td><td>A visualisation of individuals&#x27; learning activities over time.</td></tr><tr><td></td><td>UT06</td><td>A visualisation of the entire class&#x27;s learning activities over time.</td></tr><tr><td rowspan="7">Ethical concerns (EC)</td><td colspan="3">Are you concerned about ethical issues regarding the use of learning data to improve learning and teaching?</td></tr><tr><td rowspan="2">PARDO and SIEMENS (2014)</td><td>EC01</td><td>I am concerned about data anonymity in my courses.</td></tr><tr><td>EC02</td><td>I am concerned about data privacy in general.</td></tr><tr><td rowspan="2">Ifenthaler &amp; Mauriello (2016)</td><td>EC03</td><td>I am concerned about data security.</td></tr><tr><td>EC04</td><td>I am concerned about the transparency of the process.</td></tr><tr><td>SLADE and PRINSLOO (2013)</td><td>EC05</td><td>I am concerned about the period of time for which data and outcomes will be stored.</td></tr><tr><td></td><td>EC06</td><td>I am concerned about how the staff could use the information provided by learning analytics.</td></tr><tr><td rowspan="4">System quality (SQ)</td><td colspan="3">Regarding the system for lecture recordings, do you think</td></tr><tr><td>Lwoga (2014)</td><td>SQ01</td><td>The response time of the system is consistent.</td></tr><tr><td></td><td>SQ02</td><td>The response time of the system is reasonable.</td></tr><tr><td></td><td>SQ03</td><td>The speed of the Internet connection is acceptable.</td></tr></table>

UT01. Would you agree that the learning system (e.g., Canvas) should provide lecturers the following information? Early alerts of students at risk of failing.

<table><tr><td colspan="2"></td><td>Frequency</td><td>Percent</td><td>Valid Percent</td><td>Cumulative Percent</td></tr><tr><td rowspan="8">Valid</td><td>Strongly disagree</td><td>1</td><td>.7</td><td>.8</td><td>.8</td></tr><tr><td>Disagree</td><td>2</td><td>1.4</td><td>1.6</td><td>2.4</td></tr><tr><td>Somewhat disagree</td><td>1</td><td>.7</td><td>.8</td><td>3.2</td></tr><tr><td>Neither agree nor disagree</td><td>12</td><td>8.5</td><td>9.5</td><td>12.7</td></tr><tr><td>Somewhat agree</td><td>21</td><td>14.8</td><td>16.7</td><td>29.4</td></tr><tr><td>Agree</td><td>45</td><td>31.7</td><td>35.7</td><td>65.1</td></tr><tr><td>Strongly agree</td><td>44</td><td>31.0</td><td>34.9</td><td>100.0</td></tr><tr><td>Total</td><td>126</td><td>88.7</td><td>100.0</td><td></td></tr><tr><td>Missing</td><td>System</td><td>16</td><td>11.3</td><td></td><td></td></tr><tr><td>Total</td><td></td><td>142</td><td>100.0</td><td></td><td></td></tr></table>

UT02. Would you agree that the learning system (e.g., Canvas) should provide lecturers the following information? Notification about learning content that students appear to find dificult to understand.

<table><tr><td colspan="2"></td><td>Frequency</td><td>Percent</td><td>Valid Percent</td><td>Cumulative Percent</td></tr><tr><td rowspan="5">Valid</td><td>Neither agree nor disagree</td><td>5</td><td>3.5</td><td>4.0</td><td>4.0</td></tr><tr><td>Somewhat agree</td><td>9</td><td>6.3</td><td>7.1</td><td>11.1</td></tr><tr><td>Agree</td><td>49</td><td>34.5</td><td>38.9</td><td>50.0</td></tr><tr><td>Strongly agree</td><td>63</td><td>44.4</td><td>50.0</td><td>100.0</td></tr><tr><td>Total</td><td>126</td><td>88.7</td><td>100.0</td><td></td></tr><tr><td>Missing</td><td>System</td><td>16</td><td>11.3</td><td></td><td></td></tr><tr><td>Total</td><td></td><td>142</td><td>100.0</td><td></td><td></td></tr></table>

UT03. Would you agree that the learning system (e.g., Canvas) should provide lecturers the following information? A summary of individuals’ learning progress, including when and how a particular student learned.

<table><tr><td colspan="2"></td><td>Frequency</td><td>Percent</td><td>Valid Percent</td><td>Cumulative Percent</td></tr><tr><td rowspan="5">Valid</td><td>Neither agree nor disagree</td><td>4</td><td>2.8</td><td>3.2</td><td>3.2</td></tr><tr><td>Somewhat agree</td><td>2</td><td>1.4</td><td>1.6</td><td>4.8</td></tr><tr><td>Agree</td><td>5</td><td>3.5</td><td>4.0</td><td>8.7</td></tr><tr><td>Strongly agree</td><td>13</td><td>9.2</td><td>10.3</td><td>19.0</td></tr><tr><td>Total</td><td>25</td><td>17.6</td><td>19.8</td><td>38.9</td></tr><tr><td>Missing</td><td>System</td><td>41</td><td>28.9</td><td>32.5</td><td>71.4</td></tr><tr><td>Total</td><td></td><td>142</td><td>36</td><td>25.4</td><td>28.6</td></tr></table>

UT04. Would you agree that the learning system (e.g., Canvas) should provide lecturers the following information? A summary of the class’s learning progress, including when and how the class learned.

<table><tr><td colspan="2"></td><td>Frequency</td><td>Percent</td><td>Valid Percent</td><td>Cumulative Percent</td></tr><tr><td rowspan="7">Valid</td><td>Disagree</td><td>1</td><td>.7</td><td>.8</td><td>.8</td></tr><tr><td>Somewhat disagree</td><td>1</td><td>.7</td><td>.8</td><td>1.6</td></tr><tr><td>Neither agree nor disagree</td><td>10</td><td>7.0</td><td>7.9</td><td>9.5</td></tr><tr><td>Somewhat agree</td><td>25</td><td>17.6</td><td>19.8</td><td>29.4</td></tr><tr><td>Agree</td><td>45</td><td>31.7</td><td>35.7</td><td>65.1</td></tr><tr><td>Strongly agree</td><td>44</td><td>31.0</td><td>34.9</td><td>100.0</td></tr><tr><td>Total</td><td>126</td><td>88.7</td><td>100.0</td><td></td></tr><tr><td>Missing</td><td>System</td><td>16</td><td>11.3</td><td></td><td></td></tr><tr><td>Total</td><td></td><td>142</td><td>100.0</td><td></td><td></td></tr></table>

## UT05. Would you agree that the learning system (e.g., Canvas) should provide lecturers the following information? A visualisation of individuals’ learning activities over time.

<table><tr><td colspan="2"></td><td>Frequency</td><td>Percent</td><td>Valid Percent</td><td>Cumulative Percent</td></tr><tr><td rowspan="8">Valid</td><td>Strongly disagree</td><td>2</td><td>1.4</td><td>1.6</td><td>1.6</td></tr><tr><td>Disagree</td><td>4</td><td>2.8</td><td>3.2</td><td>4.8</td></tr><tr><td>Somewhat disagree</td><td>5</td><td>3.5</td><td>4.0</td><td>8.7</td></tr><tr><td>Neither agree nor disagree</td><td>16</td><td>11.3</td><td>12.7</td><td>21.4</td></tr><tr><td>Somewhat agree</td><td>25</td><td>17.6</td><td>19.8</td><td>41.3</td></tr><tr><td>Agree</td><td>35</td><td>24.6</td><td>27.8</td><td>69.0</td></tr><tr><td>Strongly agree</td><td>39</td><td>27.5</td><td>31.0</td><td>100.0</td></tr><tr><td>Total</td><td>126</td><td>88.7</td><td>100.0</td><td></td></tr><tr><td>Missing</td><td>System</td><td>16</td><td>11.3</td><td></td><td></td></tr><tr><td>Total</td><td></td><td>142</td><td>100.0</td><td></td><td></td></tr></table>

## UT06. Would you agree that the learning system (e.g., Canvas) should provide lecturers the following information? A visualisation of the entire class’s learning activities over time.

<table><tr><td colspan="2"></td><td>Frequency</td><td>Percent</td><td>Valid Percent</td><td>Cumulative Percent</td></tr><tr><td rowspan="8">Valid</td><td>Strongly disagree</td><td>2</td><td>1.4</td><td>1.6</td><td>1.6</td></tr><tr><td>Disagree</td><td>2</td><td>1.4</td><td>1.6</td><td>3.2</td></tr><tr><td>Somewhat disagree</td><td>1</td><td>.7</td><td>.8</td><td>4.0</td></tr><tr><td>Neither agree nor disagree</td><td>13</td><td>9.2</td><td>10.3</td><td>14.3</td></tr><tr><td>Somewhat agree</td><td>27</td><td>19.0</td><td>21.4</td><td>35.7</td></tr><tr><td>Agree</td><td>38</td><td>26.8</td><td>30.2</td><td>65.9</td></tr><tr><td>Strongly agree</td><td>43</td><td>30.3</td><td>34.1</td><td>100.0</td></tr><tr><td>Total</td><td>126</td><td>88.7</td><td>100.0</td><td></td></tr><tr><td>Missing</td><td>System</td><td>16</td><td>11.3</td><td></td><td></td></tr><tr><td>Total</td><td></td><td>142</td><td>100.0</td><td></td><td></td></tr></table>

EC01. Are you concerned about ethical issues regarding the use of learning data to improve learning and teaching? I am concerned about data anonymity in my courses.

<table><tr><td colspan="2"></td><td>Frequency</td><td>Percent</td><td>Valid Percent</td><td>Cumulative Percent</td></tr><tr><td rowspan="7">Valid</td><td>Disagree</td><td>2</td><td>1.4</td><td>1.8</td><td>1.8</td></tr><tr><td>Somewhat disagree</td><td>2</td><td>1.4</td><td>1.8</td><td>3.5</td></tr><tr><td>Neither agree nor disagree</td><td>19</td><td>13.4</td><td>16.7</td><td>20.2</td></tr><tr><td>Somewhat agree</td><td>24</td><td>16.9</td><td>21.1</td><td>41.2</td></tr><tr><td>Agree</td><td>28</td><td>19.7</td><td>24.6</td><td>65.8</td></tr><tr><td>Strongly agree</td><td>39</td><td>27.5</td><td>34.2</td><td>100.0</td></tr><tr><td>Total</td><td>114</td><td>80.3</td><td>100.0</td><td></td></tr><tr><td>Missing</td><td>System</td><td>28</td><td>19.7</td><td></td><td></td></tr><tr><td>Total</td><td></td><td>142</td><td>100.0</td><td></td><td></td></tr></table>

EC02. Are you concerned about ethical issues regarding the use of learning data to improve learning and teaching? I am concerned about data privacy in general.

<table><tr><td colspan="2"></td><td>Frequency</td><td>Percent</td><td>Valid Percent</td><td>Cumulative Percent</td></tr><tr><td rowspan="7">Valid</td><td>Disagree</td><td>2</td><td>1.4</td><td>1.8</td><td>1.8</td></tr><tr><td>Somewhat disagree</td><td>1</td><td>.7</td><td>.9</td><td>2.6</td></tr><tr><td>Neither agree nor disagree</td><td>14</td><td>9.9</td><td>12.3</td><td>14.9</td></tr><tr><td>Somewhat agree</td><td>24</td><td>16.9</td><td>21.1</td><td>36.0</td></tr><tr><td>Agree</td><td>29</td><td>20.4</td><td>25.4</td><td>61.4</td></tr><tr><td>Strongly agree</td><td>44</td><td>31.0</td><td>38.6</td><td>100.0</td></tr><tr><td>Total</td><td>114</td><td>80.3</td><td>100.0</td><td></td></tr><tr><td>Missing</td><td>System</td><td>28</td><td>19.7</td><td></td><td></td></tr><tr><td>Total</td><td></td><td>142</td><td>100.0</td><td></td><td></td></tr></table>

SQ01. Regarding the system for lecture recordings, do you think . . .  
EC03. Are you concerned about ethical issues regarding the use of learning data to improve learning and teaching? I am concerned about data security.

<table><tr><td colspan="2"></td><td>Frequency</td><td>Percent</td><td>Valid Percent</td><td>Cumulative Percent</td></tr><tr><td rowspan="7">Valid</td><td>Disagree</td><td>4</td><td>2.8</td><td>3.5</td><td>3.5</td></tr><tr><td>Somewhat disagree</td><td>3</td><td>2.1</td><td>2.6</td><td>6.1</td></tr><tr><td>Neither agree nor disagree</td><td>13</td><td>9.2</td><td>11.4</td><td>17.5</td></tr><tr><td>Somewhat agree</td><td>19</td><td>13.4</td><td>16.7</td><td>34.2</td></tr><tr><td>Agree</td><td>34</td><td>23.9</td><td>29.8</td><td>64.0</td></tr><tr><td>Strongly agree</td><td>41</td><td>28.9</td><td>36.0</td><td>100.0</td></tr><tr><td>Total</td><td>114</td><td>80.3</td><td>100.0</td><td></td></tr><tr><td>Missing</td><td>System</td><td>28</td><td>19.7</td><td></td><td></td></tr><tr><td>Total</td><td></td><td>142</td><td>100.0</td><td></td><td></td></tr></table>

EC04. Are you concerned about ethical issues regarding the use of learning data to improve learning and teaching? I am concerned about the transparency of the process.

<table><tr><td colspan="2"></td><td>Frequency</td><td>Percent</td><td>Valid Percent</td><td>Cumulative Percent</td></tr><tr><td rowspan="7">Valid</td><td>Disagree</td><td>3</td><td>2.1</td><td>2.6</td><td>2.6</td></tr><tr><td>Somewhat disagree</td><td>2</td><td>1.4</td><td>1.8</td><td>4.4</td></tr><tr><td>Neither agree nor disagree</td><td>18</td><td>12.7</td><td>15.8</td><td>20.2</td></tr><tr><td>Somewhat agree</td><td>22</td><td>15.5</td><td>19.3</td><td>39.5</td></tr><tr><td>Agree</td><td>31</td><td>21.8</td><td>27.2</td><td>66.7</td></tr><tr><td>Strongly agree</td><td>38</td><td>26.8</td><td>33.3</td><td>100.0</td></tr><tr><td>Total</td><td>114</td><td>80.3</td><td>100.0</td><td></td></tr><tr><td>Missing</td><td>System</td><td>28</td><td>19.7</td><td></td><td></td></tr><tr><td>Total</td><td></td><td>142</td><td>100.0</td><td></td><td></td></tr></table>

EC05. Are you concerned about ethical issues regarding the use of learning data to improve learning and teaching? I am concerned about the period of time for which data and outcomes will be stored.

<table><tr><td colspan="2"></td><td>Frequency</td><td>Percent</td><td>Valid Percent</td><td>Cumulative Percent</td></tr><tr><td rowspan="8">Valid</td><td>Strongly disagree</td><td>2</td><td>1.4</td><td>1.8</td><td>1.8</td></tr><tr><td>Disagree</td><td>6</td><td>4.2</td><td>5.3</td><td>7.0</td></tr><tr><td>Somewhat disagree</td><td>7</td><td>4.9</td><td>6.1</td><td>13.2</td></tr><tr><td>Neither agree nor disagree</td><td>15</td><td>10.6</td><td>13.2</td><td>26.3</td></tr><tr><td>Somewhat agree</td><td>23</td><td>16.2</td><td>20.2</td><td>46.5</td></tr><tr><td>Agree</td><td>28</td><td>19.7</td><td>24.6</td><td>71.1</td></tr><tr><td>Strongly agree</td><td>33</td><td>23.2</td><td>28.9</td><td>100.0</td></tr><tr><td>Total</td><td>114</td><td>80.3</td><td>100.0</td><td></td></tr><tr><td>Missing</td><td>System</td><td>28</td><td>19.7</td><td></td><td></td></tr><tr><td>Total</td><td></td><td>142</td><td>100.0</td><td></td><td></td></tr></table>

EC06. Are you concerned about ethical issues regarding the use of learning data to improve learning and teaching? I am concerned about how the staf could use the information provided by learning analytics.

<table><tr><td colspan="2"></td><td>Frequency</td><td>Percent</td><td>Valid Percent</td><td>Cumulative Percent</td></tr><tr><td rowspan="7">Valid</td><td>Disagree</td><td>3</td><td>2.1</td><td>2.6</td><td>2.6</td></tr><tr><td>Somewhat disagree</td><td>4</td><td>2.8</td><td>3.5</td><td>6.1</td></tr><tr><td>Neither agree nor disagree</td><td>18</td><td>12.7</td><td>15.8</td><td>21.9</td></tr><tr><td>Somewhat agree</td><td>22</td><td>15.5</td><td>19.3</td><td>41.2</td></tr><tr><td>Agree</td><td>35</td><td>24.6</td><td>30.7</td><td>71.9</td></tr><tr><td>Strongly agree</td><td>32</td><td>22.5</td><td>28.1</td><td>100.0</td></tr><tr><td>Total</td><td>114</td><td>80.3</td><td>100.0</td><td></td></tr><tr><td>Missing</td><td>System</td><td>28</td><td>19.7</td><td></td><td></td></tr><tr><td>Total</td><td></td><td>142</td><td>100.0</td><td></td><td></td></tr></table>

<table><tr><td colspan="2"></td><td>Frequency</td><td>Percent</td><td>Valid Percent</td><td>Cumulative Percent</td></tr><tr><td rowspan="8">Valid</td><td>Strongly disagree</td><td>2</td><td>1.4</td><td>1.7</td><td>1.7</td></tr><tr><td>Disagree</td><td>3</td><td>2.1</td><td>2.5</td><td>4.2</td></tr><tr><td>Somewhat disagree</td><td>3</td><td>2.1</td><td>2.5</td><td>6.7</td></tr><tr><td>Neither agree nor disagree</td><td>18</td><td>12.7</td><td>15.0</td><td>21.7</td></tr><tr><td>Somewhat agree</td><td>23</td><td>16.2</td><td>19.2</td><td>40.8</td></tr><tr><td>Agree</td><td>41</td><td>28.9</td><td>34.2</td><td>75.0</td></tr><tr><td>Strongly agree</td><td>30</td><td>21.1</td><td>25.0</td><td>100.0</td></tr><tr><td>Total</td><td>120</td><td>84.5</td><td>100.0</td><td></td></tr><tr><td>Missing</td><td>System</td><td>22</td><td>15.5</td><td></td><td></td></tr><tr><td>Total</td><td></td><td>142</td><td>100.0</td><td></td><td></td></tr></table>

SQ03. Regarding the system for lecture recordings, do you think . . .  
SQ02. Regarding the system for lecture recordings, do you think . . .

<table><tr><td colspan="2"></td><td>Frequency</td><td>Percent</td><td>Valid Percent</td><td>Cumulative Percent</td></tr><tr><td rowspan="7">Valid</td><td>Strongly disagree</td><td>2</td><td>1.4</td><td>1.7</td><td>1.7</td></tr><tr><td>Somewhat disagree</td><td>2</td><td>1.4</td><td>1.7</td><td>3.3</td></tr><tr><td>Neither agree nor disagree</td><td>15</td><td>10.6</td><td>12.5</td><td>15.8</td></tr><tr><td>Somewhat agree</td><td>22</td><td>15.5</td><td>18.3</td><td>34.2</td></tr><tr><td>Agree</td><td>49</td><td>34.5</td><td>40.8</td><td>75.0</td></tr><tr><td>Strongly agree</td><td>30</td><td>21.1</td><td>25.0</td><td>100.0</td></tr><tr><td>Total</td><td>120</td><td>84.5</td><td>100.0</td><td></td></tr><tr><td>Missing</td><td>System</td><td>22</td><td>15.5</td><td></td><td></td></tr><tr><td>Total</td><td></td><td>142</td><td>100.0</td><td></td><td></td></tr></table>

<table><tr><td colspan="2"></td><td>Frequency</td><td>Percent</td><td>Valid Percent</td><td>Cumulative Percent</td></tr><tr><td rowspan="8">Valid</td><td>Strongly disagree</td><td>1</td><td>.7</td><td>.8</td><td>.8</td></tr><tr><td>Disagree</td><td>1</td><td>.7</td><td>.8</td><td>1.7</td></tr><tr><td>Somewhat disagree</td><td>7</td><td>4.9</td><td>5.8</td><td>7.5</td></tr><tr><td>Neither agree nor disagree</td><td>10</td><td>7.0</td><td>8.3</td><td>15.8</td></tr><tr><td>Somewhat agree</td><td>22</td><td>15.5</td><td>18.3</td><td>34.2</td></tr><tr><td>Agree</td><td>50</td><td>35.2</td><td>41.7</td><td>75.8</td></tr><tr><td>Strongly agree</td><td>29</td><td>20.4</td><td>24.2</td><td>100.0</td></tr><tr><td>Total</td><td>120</td><td>84.5</td><td>100.0</td><td></td></tr><tr><td>Missing</td><td>System</td><td>22</td><td>15.5</td><td></td><td></td></tr><tr><td>Total</td><td></td><td>142</td><td>100.0</td><td></td><td></td></tr></table>

## Appendix 2. Process for Thematic Analysis of Interviews with the Lecturers

As the main objective of the interviews was to evaluate the use of LAIS and explore any side efects or undesirable consequences, the thematic analysis is constructionist in that it explores how a certain reality is created by the data. We analyse the interview using a recursive process consisting of six steps:

![](/api/attachments/T92XA3VN/fulltext/images/2f56d13731b5a94957d90f82fdccdd19b00c22b10410b7d49c4514caae3d9981.jpg)  
Figure 8. Thematic analysis process for interviews with the lecturers

## Step 1: Familiarisation with the research data

The initial step of the analysis involved repeatedly reading of the interview transcripts in an active manner to become immersed in and intimately familiar with the data. While reading and re-reading the manuscripts, we actively looked for potential key patterns and meanings in the interviews.

## Step 2: Coding

After becoming familiar with each interview, the transcripts were coded line-by-line for specific themes. In accordance with the objective of the interview, we used a deductive approach to develop the coding and themes, and this process was initially directed by existing notions about the two initial themes at the highest level:

(1) The perceived usability and usefulness; and

(2) Dificulties and concerns related to the use of LAIS.

## Step 3: Searching for themes

We inspected the codes and collated data to check for patterns of variability and consistency across all transcripts. Furthermore, significant broad patterns of meaning were used to identify any additional potential themes. We also identified more specific subthemes for each candidate theme.

## Step 4: Reviewing themes

We examined and refined the candidate themes against the dataset to determine whether they present underlying meanings of the data and address the objective of the interviews. We also reviewed the themes to ensure that the coded extracts of participants’ accounts formed a coherent pattern.

## Step 5: Defining and naming themes

We analysed the revised themes in detail and determined the scope and focus of each theme to explore the story of each one. In this step, we developed an informative name for each theme:

• Perceived usability and usefulness and

• Subjective interpretation of reported information.

## Step 6: Writing up

We created the analytic narrative and themes and then contextualised the analysis in relation to relevant literature. The results were written and reported in this research paper.
