---
otero_id: 15028
otero_key: "GCSE3ND8"
title: "GIST: A MODEL FOR DESIGN AND MANAGEMENT OF CONTENT AND INTERACTIVITY OF CUSTOMER-CENTRIC WEB SITES"
authors: "Terri C. Albert; Paulo B. Goes; Alok Gupta"
year: "2004"
journal: "MIS Quarterly"
doi: "10.2307/25148632"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# GIST: A MODEL FOR DESIGN AND MANAGEMENT OF CONTENT AND INTERACTIVITY OF CUSTOMER-CENTRIC WEB SITES<sup>1</sup>

By: Terri C. Albert School of Business University of Hartford 2000 Bloomfield Avenue West Hartford, CT 06117 U.S.A. talbert@hartford.edu

Paulo B. Goes Operations & Information Management School of Business University of Connecticut 2100 Hillside Road, Unit 1041-OPIM Storrs, CT 06269 U.S.A. paulo.goes@business.uconn.edu

Alok Gupta Information and Decision Sciences Carlson School of Management University of Minnesota Minneapolis, MN 55455 U.S.A. agupta@csom.umn.edu

## Abstract

Customer-centric Web-based systems, such as ecommerce Web sites, or sites that support customer relationship management (CRM) activities, are themselves information systems, but their design and maintenance need to follow vastly different approaches from the traditional systems lifecycle approach. Based on marketing frameworks that are applicable to the online world, and following design science principles, we develop a model to guide the design and the continuous management of such sites. The model makes extensive use of current technologies for tracking the customers and their behaviors, and combines elements of data mining and statistical analyses. A case study based on a financial services Web site is used to provide a preliminary validation and design evaluation of our approach. The case study showed considerable measured improvement in the effectiveness of the companyís Web site. In addition, it also highlighted an important benefit of the our approach: the identification of previously unknown or unexpected segments of visitors. This finding can lead to promising new business opportunities.

Keywords: Web site analysis and design, customer segmentation, personalization

## Introduction

Understanding the end users and their requirements has been the cornerstone of information systems analysis and design. Understanding the factors that lead to user acceptance has received abundant attention by the information systems research community (see for example, Barki and Hartwick 1994; Davis 1989). Most of the time, end users are a well-defined category, either comprising a specific segment of internal constituents (sales force, human resource, etc.) or well-known segments of the extended enterprise of suppliers and customers. User participation, before and during the implementation of information systems, and training are fundamental in facilitating acceptance and increasing the utilization of the systems (Green and Hughes 1986; Lee et al. 1995; McKeen et al. 1994).

Another characteristic of the more traditiona system development lifecycle of information systems is system maintenance. Aside from corrections and debugging that might take place after the system is released, major upgrades or new versions are released very infrequently. In other words, the cycle for incorporating major changes is relatively long. Gaps that are identified between the end usersí objectives and motives toward the system and the functionalities that the system actually delivers can only be addressed at very infrequent intervals.

Customer-centric Web-based systems, such as ecommerce Web sites, or sites that support customer relationship management (CRM) activities, are themselves complex, multicomponent, multitier information systems, but their design and maintenance need to follow vastly different approaches from the traditional systems lifecycle. While some of the end-users may be either current customers or potential customers, many of them are non-transactional visitors, often anonymous, that are part of the Internet user population at large. These users may display a wide variety of preferences and motives toward the site, which are very difficult to capture.

The Internet environment is a marketing channel for which Hoffman and Novak (1996) articulated a need to understand both the transaction and nontransaction activity. Non-transaction activities entail experiential components, whereas transaction (shopping, online banking, etc.) activities are more goal-oriented. Hoffman et al. (1996) classified sites into online storefronts, Internet presence sites, content sites, malls, incentive sites, and search agents. An early analysis of these categories indicated that only 18 percent of the sites were online storefronts while the remaining 82 percent were informational or Internet presence sites (Kaul 1995). The prevalence of the experiential, non-transactional activities conducted on non-transaction site types in the early commercialization years of the Internet continues to be the pattern, as recently demonstrated by Greenspan (2002): while 59 percent of online visitors conduct transactions, their primary activities continue to be information and communication based.

The design and administration of Web sites visited by the non-transactional user remain a challenge due to the difficulty in obtaining design requirements from these potential visitors. Their direct involvement during requirements definition and their training as end-users are usually not viable options. One can only successfully listen to the ìvoice of the customerî when there are well-understood site audiences, as demonstrated by an interesting study conducted by El Sawy et al (1999).

The Web environment is implicitly highly dynamic, defying customary geographic and temporal information systems design assumptions. In addition, a Web site is, in essence, competing with various other web sites trying to attract and capture the visitors, which introduces new market dynamics. It is critical to conduct continuous assessment of potential gaps between intentions of users and the delivered experience by the site to maintain its utility. This implies continuous management and updates of content and interaction, as opposed to the sporadic version release paradigm of traditional software development environments.

We consider Web site design and its continuous redesign as a complex product design and product update problem. We see the product itself as a multidimensional set of possible visitor experiences that the firm wants to enable. Each such experience might have been determined by very different motives expressed by very different individuals. On top of all of this, we consider the requirement of real time assessment of gaps between the visitorsí intentions and motives and the site offerings. This may lead to constant site redesign and updates. The framework and methodology we propose are intended to address this very complex product design problem when the users of the product are not well understood in advance.

In this paper, our goal is to propose an operationa framework for continuous redesign, especially for non-transactional sites. While much of what we propose can be used for transactional sites, our approach also works for non-transactional sites, an area of research that has not attracted much research. Our basic research premise is that the design and maintenance of customer-centric Web sites need to be based on a customer-focused approach. Therefore, we propose a Marketing centric approach to design and maintenance of such Web sites using a framework that we refer to as GIST: GatherñInferñSegmentñTrack. In devising and evaluating the proposed framework, we follow the principles of design science and follow the seven guidelines of design science research as suggested by Hevner et al. (2004).

The collaboration between the Information Systems and Marketing disciplines is not new; however, it has become more tightly coupled as role of the Internet is increasingly examined in applied and scholarly research. As Hong et al. (2002) state, e-commerce systems are both an information system and a marketing channel. Each discipline views the electronic environment through its own theoretical frameworks or lens. Further, Stafford (2003) sees the marketing view as more product-oriented and the information systems or technology view as more of a development concept. These multiple perspectives have led each discipline to claim different aspects of the e-commerce paradigm.

The marketing disciplineís contribution to the IS new concept development lens is its identification of ìand meeting human and social needsÖ profitablyî (Kotler 2003, p. 3). More specifically, marketing requires understanding the customerís (either a consumer or business) expectations from the firm and delivering products or services that meet or exceed these expectations. This, coupled with the IS lens for understanding the end usersí requirements (the cornerstone of information systems analysis and design), creates a powerful approach to understanding and designing customer-centric Web sites. However, surprisingly very little research has focused on integration of the two lenses.

To the best of our knowledge, GIST is the first practical methodology that combines marketing research findings for the online context that identifies determinants of customer satisfaction, loyalty, and retention with the development cycle principles from information systems. We incorporate several appropriate marketing frameworks into the GIST design. Our focus is on transforming existing marketing models for the online environment by leveraging the real-time and offline behavior of visitors, identify gaps in their expectations, and redesign the site to minimize or eliminate these gaps.

In the next section, we overview how the design science framework outlined in Hevner et al. was used to guide the development of our research artifacts that constitute the proposed framework. The following sections introduce the specific constructs and conceptual approaches that led to the GIST methodologyís development and the information architecture that is available to implement the methodology. We follow with detailed descriptions of each of the stages of GIST: GatherñInferñSegmentñTrack. We conclude with a case study of a Fortune 50 company that provides proof-of-concept for GIST.

## A Design Science Approach

In their recent article, Hevner et al. (2004) provide a general framework to guide IS researchers and practitioners on how to conduct, evaluate, and present design science research. We believe the work presented in this paper exemplifies the approach and evaluation criteria presented in their work. Below we present an outline of how various components of GIST relate to the guidelines presented in Hevner et al.

Design as an Artifact. The methodology we develop is itself the artifact that is created to address the important problem of designing and redesigning customer-centric Web sites in the presence of non-transactional visitors. The methodology consists of multiple steps: GatherñInferñSegmentñTrack, for which specific artifacts were developed. The combined artifact of these steps is a dynamic Web site design for a non-transactional Web site, described in the case study.

Problem Relevance: As stated in the Introduction, the problem of designing and redesigning customer-centric Web sites is extremely relevant. This is a problem that very significantly highlights the interplay among business strategy, IT strategy, organizational infrastructure, and IS infrastructure. The case study we present to evaluate our methodology further illustrates all of these aspects.

Research Rigor: We combine rigorous elements of multidisciplinary fields in constructing our solution methodology: marketing, data mining, and systems design. We draw from the knowledge base in each of these areas and extend the ideas in the area of consumer segmentation, its identification and validation, and the use of consumer segmentation in business strategy.

Design as a Search Process: Our methodology is iterative by nature. At each step we search for gaps between design objectives for the Web site and observed metrics. GIST internalizes the feedback loop in the continuous evaluation process and redesign.

Design Evaluation: As suggested in Hevner et al., we use an observational evaluation method to evaluate the design. Specifically, we observe whether the redesign of the Web site in the business organization resulted in identification of business leads and in identification and mapping of new customer segments.

Research Contributions: Our main contribution is the GIST methodology, which is unique in a number of ways, combines the marketing and IT disciplines to continuously address Web site design requirements for both transactional and non-transactional visitors. We create and describe the design methodologyóGIST, design artifactóthe Web site and its information gathering components, and describe the implementation strategies for a marketing research foundation to enable GIST.

Research Communication: GIST is based on the underlying disciplines and follows a rigorous step-by-step approach. At the same time, the resulting artifact is of extremely high relevance to practitioners, as demonstrated through the successful implementation in a Fortune 50 company. As suggested by Hevner et al., we present the technical foundation for successful implementation for design science researchers and the case study to communicate the relevance and importance of this research for a management-oriented audience.

## The GIST of IT: Of Nanosegments, Nanoflows, and Gap Analyses

In this section, we present our basic design approach, GIST. In terms of design science guidelines, this section partially addresses the issues of research contribution, research rigor, and design as a search process. We discuss the design aspects and requirements, theoretical and practitioner foundations, and innovative methodologies that enable GIST. We create a new knowledge artifact by defining the concept of the nanosegment and its relative positioning in the traditional consumer segmentation approaches. We also present the idea of gap analysis to internalize the design of a feedback loop for continual evaluation of the managerial artifact, the Web site, to identify and process redesign needs via gap analysis.

We propose the following steps to solve the customer-centric site designñredesign problem faced by companies:

Understand visitorsí needs and motives. Visitors are generally of two types

Transactional visitors, for which detailed information and motives might be available to the firm.

Non-transactional visitors, whose attributes remain anonymous but whose online behavior information might be captured to some degree.

Given information about visitors, their intentions and motives, design an array of possible experiences to maximize visitorsí utility and/or the firmsí profit.

Offer the appropriate experience to specific visitor groups.

Continuously assess gaps between visitors and their experiences.

Redesign and reposition experiences accordingly.

Our methodology to address the designñredesign problem hinges on two main, related building blocks that are based on extant marketing literature. These are constructs that capture the users on one hand and the desired products the Web site offers on the other. The methodology also uses marketing work done on gap analysis for e-services.

## Nanosegments

First we introduce the concept of nanosegments, which extends Peltier and Schribrowskyís (1997) microsegmentation framework that primarily focuses on the reasons for purchase decisions. Peltier and Schribrowskyís conceptual framework for developing microsegments considers needsbased buying motives and benefits. The segmentation process identifies why a purchase is made and puts less emphasis on the who. Microsegments of consumers are, therefore, identified based on their evaluative behaviors toward purchasing a product or service. Conceptually, microsegmentation yields more value to the marketing effort as the underlying motives of the customer/visitor are defined by their behaviors and complemented by their characteristics. Peltier and Schribrowsky noted that this approach provided marketers with a deeper understanding of their customers, which in turn can be translated into a more satisfying interaction and experience for the consumer.

The limitations of the Peltier and Schribrowskyís model in the online environment are that it is only applicable to buying or purchasing behaviors. In addition, this model focused on self-reported buying motives and behaviors.

We extend microsegments, for use in online environments, by using both purchase (transaction, goal-oriented) and non-purchase (nontransactional, experiential) behavior (Hoffman and Novak 1996), and define the concept of nanosegments. Nanosegments are derived based on inferring customersí individual characteristics (demographics or firmographics in business-tobusiness applications) and observing their real behavior on the Web site. Nanosegments are at a finer granularity (therefore nano) because they incorporate both detailed Web site visit behavior and customersí attributes (such as demographics or firmographics) to the extent they are available. Technological advances play a key role in defining nanosegments since advanced tracking and data mining technologies, used in conjunction with a host of internal and external information sources, are necessary to operationalize the concept.

![](/api/attachments/GCSE3ND8/fulltext/images/eae9b0c4434a85063d1a3285527821e82eb0dbe8b99f6277b6d519086c812f3c.jpg)  
Figure 1. Nanosegments vs. Personalization and Microsegments

The concept of nanosegments also draws from Peppers and Rogersí (1996) one-to-one marketing. One-to-one marketing relies on a company knowing its customers through their exchanges. The exchanges may be transaction or singular in nature or a more involved series of exchanges that includes interactive dialogue (post-sale follow up; resolving service problems or issues; building loyalty). By assimilating the information from these exchanges, a company knows how its individual customers would like to be treated. This is further enhanced through personalization or customization of products or services based upon individual customerís preferences (Peppers and Rogers 1997). It is important to note that one-to-one marketing remains primarily seller driven because the seller has to acquire an in-depth understanding of the customerís needs to provide a more meaningfu interaction. Further, existence of transactions is a must and, usually, the personalization techniques perform better as the number of transactions with a given customer increase.

Figure 1 illustrates the granularity of nanosegments as it relates to both the degree of personalization indicated on the horizontal axis and the technology requirements represented on the vertical axis. When no technology is used to enable differentiation of the visitor base, we have a generic Web site working with a broad audience. When demographic information of customers and transactional data containing purchasing patterns and intentions are available, one can target microsegments as defined by Peltier and Schribrowsky. This information is typically stored in internal databases. If, in addition to these, one is able to track online behavior of both transactional and non-transactional visitors, nanosegments can be defined by the extensive use of data mining and enhanced statistical analyses. Finally, with additional individual information, one can achieve one-to-one personalization levels. Due to the anonymous nature of the non-transactional visitors, nanosegments do not necessarily go all the way to the one-to-one marketing concept of Peppers and Rogers.

The use of nanosegments alleviates many of the inherent privacy concerns and allows the marketing efforts to capitalize on segments built on behaviors that indicate the online visitorsí collective preferences, segmented at appropriate levels. One of the primary benefits of nanosegments is its inference with respect to non-transacting visitors. Since very little ìmarketingî information is obtained from non-transacting customers, personalization strategies and micro-segments cannot be designed for them in an offline environment. However, by capturing online behavior from visits and analyzing collective patterns, new potential customer segments can be identified that perhaps didnít transact because the site wasnít appropriately designed for them. We provide a concrete example of such discovery in our case study.

## Nanoflows

The second building block relates to the online experiences the site should be equipped to offer, given the array of nanosegments that are likely to visit. We model these targeted experiences after the work of Hoffman and Novak (1996) and term them nanoflows. Hoffman and Novak expanded Csikszentmihalyiís (1977) concept of flow into the online environment. Their model proposes that flow is an integral part of the online visitorís network navigation in the computer-mediated environment. The model uses filtered-out irrelevant thoughts and perceived skill set match (regarding navigation skills) as antecedents while positive online experience with a perceived sense of control are considered consequences.

For our designñredesign purposes, each nanoflow consists of a site navigation sequence in terms of content and interactivity. These nanoflows are specifically designed to address the needs and motives of an identified nanosegment. We then identify shortcomings in design by observing the patterns of usage versus intended usage to perform gap analysis as described in the next subsection.

## Gap Analysis

Gap analysis is at the core of our methodology. Gap analysis identifies the difference between identified needs of a given nanosegment as described by nanoflows and actual user behavior.

Our approach is motivated by Zeithaml et al. (2000), who identify four gaps (information, design, communication, and fulfillment) that have to be bridged to create a positive online experience based on their e-service quality metrics. Of these, fulfillment relates to the actual delivery of goods and services, and does not directly apply to the context of this paper.

Essentially, we propose a continuous loop methodology that identifies nanosegments, provides input to nanoflow design, and continuously assesses gaps of the nanosegmentñnanoflow provided by the site. The gap analysis can result in discovery of new nanosegments as well as in the design of new nanoflows. In the next section, we discuss the information requirement and overview the technological architecture to enable the application of the GIST.

## The Information Intelligence Infrastructure

In this section, we present the infrastructure requirements to enable GIST. This can be viewed as looking at design as an artifact in Hevner et al.ís (2004) terminology. We present the technical requirements and concepts required to gather information for the gather and infer phases of GIST.

In the off-line world, CRM initiatives and marketing microsegmentation have relied on two main sources of data: individual (demographics for individual consumers or firmographics for business customers) and transactional data. The Web environment provides an extraordinary means to collect data on how customers behave when engaging in an interaction with a company. This is specifically pertinent for non-transactiona visitors where, in the offline world, there is virtually no availability of data. What is very difficult to assess in the offline world is now almost trivial in the Web world. Imagine the impossible task of interviewing or surveying each store customer to learn which stores she had to been before, and how long ago. Consider the prohibitive costs (and the privacy issues) associated with videotaping or visually monitoring what each customer does and how she behaves in a store. One can conduct periodic sampling to better design layouts and merchandise displays, but one cannot capture each individual set of actions and behaviors every time the customer comes through the door.

![](/api/attachments/GCSE3ND8/fulltext/images/a6c6580b26703fdc17074e58f4945463859f49743dc3b670c36926fbd7fa244b.jpg)  
Figure 2. GIST Information Architecture

However, important information about existing customers is often present in offline databases that can help group customers according to some common characteristics. We believe that such information could effectively be used to define nanosegments and nanoflows.

In Figure 2, we use a stylized entityñrelationship diagram to depict the information architecture of the underlying data sources that can potentially be used by GIST both from offline sources and online sources.

Individual customer information can be obtained from customer files kept by the company in their CRM systems. Customers who have registered on the Web site will have their information kept in the registered customers database. Typically, this information is not as detailed as the CRM information, and may not even contain personal information beyond e-mail addresses and some limited demographics. Information captured by third parties, such as Equifax, can also be available for purchase in third party consumer databases. Transaction information can be obtained from both offline and online transactions.

Information about online behavior may come from several sources. First, information about every click or Web site request is stored in a record of the Web log file. By analyzing the IP address and the date/time fields, information about the entire visit to the site by each customer emerges. If the site uses cookies, the Web log files will indicate that, and more can be known about the visitor. Second, when the site uses dynamic page generation, the Web server coordinates with an application server (AS) that stores business rules for the page generation. To construct the required Web page, the AS may interact with a database server (DS) to retrieve the necessary content. Hence the click stream information of the Web log files can be enriched by the AS log files and the DB log files to obtain the entire picture of the visit. Finally, third party cookie-generated information can be purchased from specialized companies to gain knowledge of access behavior to other sites.

The data analysis and mining would be better conducted if the data elements of Figure 2 were integrated through a data warehousing solution (see, for example, Inmon 2002). However, this is not always the case, and the challenge typically faced by companies is how to integrate data from disparate sources. In the next section, we bring the fundamental concepts and information architecture proposed in previous sections and propose an operational framework to enable continuous improvements in a Web site design.

## GIST: An Operational Framework

In this section, we provide further support to the design science guidelines of research rigor and design as a search process by describing each stage of GIST and the role of conceptual and technological artifacts in these stages.

GIST is a framework to continuously identify user groups at the nanosegment level, and to allow for the design and evaluation of targeted flows or user experiences for these segments. As discussed earlier, we call these experience-driven designs nanoflows. As seen in Figure 3, GIST consists of a prologue and four stages, which are continuously applied through the lifetime of the Web site.

As Parsons et al. (1998) noted, consumeroriented Web sites were originally designed and constructed using traditional marketing methods. That is, the first Web site for a firm was constructed based on the firmís offline information sources and was often considered ìuninspiringî (Albert and Sanders 2003). These information sources included internal customer databases (surveys, focus groups, purchase patterns, and purchase/transaction activities), external secondary research (syndicated studies), and competitive benchmarking or best practices analyses. A firm would identify or project the expectations of the online customer/visitor using this information and often define target audiences for the site. In the context of GIST, we refer to the initial stage of setting up a new site or working with the legacy Web site of the company as the prologue.

In the prologue, a preliminary definition of the target visitor segments and desired navigation flows should be in place. The segments at this point are not nanosegments because they do not incorporate any site behavior observations. They can be derived by looking at the intended audience of the site. In the prologue, the question related to who should be coming to the site (target population) can be answered through the application of segmentation techniques that identify market profiles. Data for these analyses are available from internal as well as external customer databases. There is extensive research proposing different methods to attain customer segmentation for database marketing (Weinstein 1993). These methods are generally classified into judgmentally based methods and decision trees (Levin and Zahavi 2001). A variety of traditional statistical, multivariate methods, such as k-means clustering and discriminant analysis, can also be used for classification purposes, as well as methods based on neural networks and genetic algorithms (Holland 1986).

![](/api/attachments/GCSE3ND8/fulltext/images/222abe95d09812f1018cda40ba082f86609d9da5b76e44e3f60417bf97722c82.jpg)  
Figure 3. The GIST Cycle

We illustrate the initial target segmentation of the prologue in the case study we cover later in this paper. The target navigation flows for each target segment are also established here. The next four stages of the cycle are described below.

Gather: In this phase one needs to explore all available data sources as depicted in Figure 2. The objective is to obtain as much relevant and feasible information about visitorsí characteristics and their online behavior, which may have an impact on Web site design and effectiveness, as possible.

Infer: In this phase we utilize data mining technologies and statistical analyses to build knowledge regarding the visitors (known and anonymous) in both transactional and nontransactional environments. In addition, click stream analysis is conducted to explore questions such as where the customers come from. The basic objective of infer is to verify if the current (nano)segments and (nano)flows are still valid. We utilize gap analyses to assess the effectiveness of current segmentation. If the existing gaps are substantial, we proceed to the segment phase.

Segment: This phase identifies new relevant nanosegments and validates nanosegments via additional marketing research. The new nanosegments and marketing analyses are used as an input in the design of nanoflows to match the companyís objectives with the visitorsí motives.

Track: In this phase we perform usability studies associated with each nanoflow. This phase also involves gap analysis and measurent of e-service metrics, which results in refined nanosegments and nanoflows.

We now present more details of the Inferñ SegmentñTrack phases. A complete real-world example of the implementation of GIST illustrating all of the phases will be presented later in the form of a case study.

## Infer Phase

The inputs to the infer phase are the target nanosegments of the previous GIST cycle, or the segments defined in the prologue in case this is the first iteration of the cycle. The focus of this phase is an in-depth data analysis that will lead to validating these (nano)segments and the associated (nano)flows through a structured gap analysis.

First, we precisely contrast who should be coming to the site by design with who is actually coming to the site; which nanoflows of the site (paths and components) are being visited, and more importantly by whom.

Data collected from Web site registration and information volunteered by users through online forms, if available, can be used to generate segmentation on who is actually coming to the site. Web log files contain data to capture information on non-transactional and even anonymous visitors, such as the referring URL (where the visitor is coming from) and the time of the visit. In general, IP addresses captured in these log files provide very limited information on the identity of the visitors. Since ISPs typically assign dynamic addresses to session users, the most one can obtain from resolving IP addresses is the identification of the ISP (e.g., AOL, ATT, etc.). One can get some general information about the geographic location of the visitorís computer. Also, by using cookies, one can at least determine if a visitor is a repeat visitor or not. All of this wil provide input to the first gap analysis: segments of who is actually coming to the site versus segments of who is the intended audience by design, as determined in the previous GIST cycle or prologue.

Augmented log files (Web server, application server, and database server) provide rich information to analyze the paths (sequence of interactions between the users and the site) and validate the nanoflows of the previous cycle. Identification of most frequent paths, most frequent exit pages, and site funnels are possible from the information contained in these log files.

Data mining for association rules (Agrawal et al. 1993), similar to the well-studied market basket problem, can play an important role in this second phase of inferring. Finding out which pages are often visited in the same session or which database queries are correlated with which visit event are important pieces of information to understand how the actual nanoflows emerge. In validating the designed nanoflows against the observed ones, we attempt to answer the following question: Is the design of the site and its components consistent with what the visitors are doing on the site? In case gaps are determined that require redesign of nanosegments and nanoflows, the segment phase of GIST is invoked. If not, continue on to track.

## Segment Phase

At this stage, sufficient data from online behavior, activities, and registration has been collected to develop profiles from both transacting and nontransacting visitors. Segmentation models can now be developed for either type of visitor by using data mining and statistical techniques on the combined data.

We propose the use of traditional marketing research to validate the nanosegments and further understand their motives. This can be done through online surveys, phone interviews, etc.

The next step within the segment stage is to design the nanoflows associated with each nanosegment. Obviously, more than one nanoflow can be associated with each nanosegment, and the same nanoflow can be shared by more than one nanosegment.

Personalization technology (for example, by BroadVisionósee www.broadvision.com) can be used to provide real time interactivity components to recognized nanosegments. In the online world, the concept of a segment having only one individual indicates the need for a very adaptable marketing environment. The Internet and its supporting technologies provide the ability to adapt or configure the firmís electronic storefront. The

GIST model provides the input into this reconfiguration whether the segment contains 1 or 500 individuals.

The site customization that GIST offers is consistent with the findings by Xue et al. (2003). In their study, a customer orientation design strategy is presented. It requires coproduction between the site/firm and the customer/visitor. Powerful navigation is often necessary to execute this strategy but too much navigation and support can be overwhelming. GISTís ability to provide the data for dynamically configured sites would address this variation in preferences. While the necessary tools for the dynamic configuration may be costly in some scenarios, the trade-off of costs versus efficiency and effectiveness may be merited in the business-to-business environment.

## Track Phase

In essence, the track phase is the evaluation and feedback stage of the loop. The key activities in the track phase deal with evaluating the gaps identified by Zeithaml et al. (2000) regarding eservice quality. These are defined (by both offline and online service quality) as the difference between the customersí (visitorsí) expectations of the experience with the firm and their actua encounter with the firm. These gaps are information gap (content design), design gap (features in page design, site design, usability, etc.), and communication gap (interactivity features).

The gap analyses are also related to the broad usability topic as presented in Nielsen (2000) and Donoghue (2002). To assess detailed gaps, focused usability studies are conducted for each nanosegmentñnanoflow pairing. The segments will guide the customized interaction with the firmís Web site by specifying the visitorís objectives upon their arrival. Continual monitoring of the visitorís online behaviors provides feedback on the interaction. The segments are evaluated based on the siteís unique communication with the visitors or members of the segment. Results of these communications are fed back into the Gather phase for the next cycle of GIST. Evaluation metrics provide feedback into the further refining of the segments and the firmís Web presence, as we adapted the concept of experience engineering as a model for understanding eservices and tracking it (Rust and Kannan 2002).

## Proof of Concept: A Case Study

In this section, we present a case study demonstrating GIST as an application of academic concepts and metrics with the tools that practitioners employ. The case study satisfies the design science guidelines (Hevner et al. 2004) of problem relevance, design evaluation, and managerial communication of research. We provide the company background and a detailed explanation of the prologue, gather, infer, segment, and track stages. For the readerís reference, each stage is also summarized in Table 1.

The company specializes in non-traditional, commercial financial services. It is a strategic business unit (SBU) of a Fortune 50 firm. Until 2001, almost all of the commercial finance business of the company was conducted offline. It entered the prologue phase in 2000 because of a companywide initiative to increase the overall Web presence of all business units. To systematically determine the target segments for the initial site, we conducted a k-means cluster analysis that examined all of the companyís closed deals over the last two years using the offline CRM data from an existing Siebel database. The variables used included measures of industry type, revenue size, financing needs, collaterals, and years in business. This analysis identified the companyís offline customers as manufacturers and retailers whose financing needs revolved around refinancing and acquisition. They have impressive assets, collaterals, and tend to be mature in their industry

The commercial finance Web site was created to promote its services to these segments. It was not thought of as a strategic tool because of its potentially low volume traffic and the complexity

<table><tr><td colspan="3">Table 1. GIST Case Study Reference</td></tr><tr><td>GIST Stage</td><td>GIST General Activities</td><td>GIST in Case Study</td></tr><tr><td>Prologue</td><td>Determine target segments.Identify objectives of site.Identify initial flows.</td><td>Used k-means clustering on offline CRM data in existing Siebel database; used industry type, revenue size, financing needs, collateral, years in business in classification technique.Objective of site: lead generation.Identified flows: generic menu tabs with paths to generic information, aiming at “Contact Us” form.No customization or induced segmentation of visitors.</td></tr><tr><td>Gather</td><td>Use information from all available sources: online, off-line, internal, external.</td><td>Data sources used:Web server log filesBroadVision log filesDigimine reportsDatabase containing information captured from on-line formsSiebel database of off-line customers</td></tr><tr><td>Infer</td><td>Data mining and statistical analysis to infer actual nano-segments.Conduct gap analyses.</td><td>Used k-means clustering on information collected from on-line forms and potential leads generated by site.Used data mining techniques available in Digimine, including association rules mining, to analyze current flows.</td></tr><tr><td>Segment</td><td>Identify new nanosegments.Use supporting marketing research to validate nano-segments.Design new nanoflows, using personalization where appropriate.</td><td>Enhanced cluster analysis with number of repeat visits variable from cookies information on click stream.Identified new nanosegments, including unexpected intermediaries nanosegment.Used phone interviews and surveys with nanosegments.Designed nanoflows.</td></tr><tr><td>Track</td><td>Detailed gap analyses at nanosegment level to assess e-service metrics.Usability studies on nanoflows.Refinement of nanoflows.</td><td>Assessed important metrics: number of leads, surveys at nanosegments.Conducted extensive usability study on intermediary nanoflows.Refined nanoflows.</td></tr></table>

and nuances of commercial finance. The siteís primary objective was to generate leads that would be pursued through one of two types of referrals: a prequalifier contacts the visitor via telephone (the next business day) or another strategic business unit within the corporation receives an electronic referral for follow up. If referred to the prequalifier, the visitor or customer transitions into the companyís offline loanoriginations department. At this point, the Web site has achieved its primary objective (to generate qualified leads). Any lead generated by the site is monitored for its progress through the loan funding process and provided a database in the gather phase. Since the siteís objective was to generate leads without specific customization, the nanoflows consisted of a generic menu with paths to generic information. The only interactive portion of the Web site was a ìContact Usî form.

In the gather phase of GIST, multiple online and offline data sources were used. After a thorough evaluation of needs, potential benefits, and costs, the company decided to use BroadVision as the platform for its Web presence. BroadVision was chosen for its ability to create Web sites with a high level of personalization technology. In addition, the company purchased the services of Digimine<sup>2</sup> to analyze the Web logs. Digimine services have the ability to merge data from a variety of sources and have the ability to quickly and dynamically respond to new queries; in addition, data from external third parties can be obtained and merged with the companyís own data. Overall, we suggested that the following data sources be used for the gather phase of GIST:

ï Web server log files

ï BroadVision application server log files

ï Digimine reports ad hoc query capabilities

Database containing information collected from the online forms submitted by the visitors

Proprietary database of potential leads (eleads) generated by the site

Offline Siebel<sup>3</sup> database containing information about the leads, prospects and converted customers, used by the offline loan origination process

The last data element in the gather phase was a traditional marketing research survey assessing the visitorís experiences with the site.

The second step of GIST, infer, aims at performing the two broad but critical gap analyses.

The first is designed to validate the question: Are the site visitors consistent with the intended audience of the site? To systematically study this question, we conducted a second k-means cluster analyses using data collected from the visitors of the Web site who filled out the contact us form and those that became potential leads. Similar firmographic variables were used in order to compare these results with the offline clustering (industry type, revenue size, financing needs, collaterals, and years in business). We identified several differences between the two environments.

(1) The online channel attracted more serviceoriented companies along with retailers and manufacturers, while the sweet spot of offline deals consisted primarily of manufacturers and retailers.

(2) The online visitors were looking primarily for working capital, while the offline companiesí needs revolved around refinancing and acquisition.

(3) The online companies tended to be less mature with fewer years in business and smaller asset and collateral sizes as compared to their offline counterparts.

A major benefit from this analysis was the realization that the initial design goal of creating a Web site to cater to the needs of the same type of customers as the offline customers is not an optimal choice. The company was already participating in promotional programs (affiliates with link reciprocation and special placements with popular search engines) aimed at attracting these similar profiles of customers; thus it was now understandable why its effectiveness was low.

As a result of these findings, within the first quarter of implementing the GIST-based approach the company was able to

start focusing its efforts to better target the appropriate type of customers

provide better and more aligned content on the Web site

![](/api/attachments/GCSE3ND8/fulltext/images/d83374dada8674b670d0e9c0142fa82f26b673508f55d3aa3f0b45d32803f99f.jpg)

<table><tr><td>Funnel</td><td>Event</td><td>Total Users</td><td>Funnel Users</td><td>% of Level 1</td><td>% of Prev. Level</td><td>Drop Off</td></tr><tr><td>Level 1</td><td>Total Users</td><td>2,535</td><td>2,535</td><td>100.00%</td><td>--</td><td>--</td></tr><tr><td>Level 2</td><td>Contact Us</td><td>202</td><td>202</td><td>7.97%</td><td>7.97%</td><td>92.03%</td></tr><tr><td>Level 3</td><td>Inquire About A Product or Service</td><td>134</td><td>85</td><td>3.35%</td><td>42.08%</td><td>57.92%</td></tr><tr><td>Level 4</td><td>Submit Inquiry</td><td>4</td><td>2</td><td>0.08%</td><td>2.35%</td><td>97.65%</td></tr><tr><td>Level 5</td><td>Thank You</td><td>9</td><td>1</td><td>0.04%</td><td>50.00%</td><td>50.00%</td></tr></table>

Figure 4. Example of a Funnel/Nanoflow

• analyze current nanoflows and develop more customized ones

ï identify new customer segments or nanosegments

realign the work force to better suit the need for an appropriate loan approval process

The second gap analysis of the infer step measures the effectiveness of a given site; for instance, is it accomplishing its general objective, in this case, lead generation? The log file analysis and the Digimine reports provided a means to answer this question through a ìfunnelî analysis, where one can monitor any intended (or expected) navigation pattern (see Figure 4 as an example). The intended patterns or nanoflows were developed in conjunction with the site content design and are modified whenever site design is modified. Any nanoflow (i.e., any sequence of pages) can be defined as a path and analyzed through Digimineís funnel analysis. For example, by examining the number of visitors who visit the site and, ultimately, complete the inquiry form, a measure of the siteís objectives could be made.

When we conducted this funnel analysis, we obtained some unexpected results: 98 percent of the visitors did not submit a loan query form. The high decay rate led to questions regarding efficacy of the design strategies toward the ultimate goal of attracting leads. One of the questions that we examined due to this finding was whether the promotional vehicles were driving intended traffic to the site and did these vehicles reach the ìrightî online audience? We conducted this analysis by examining the referring URL, the traffic that was generated from search engines, reciprocal links, and affiliates of the corporation. It was noted that those who did not submit the form did spend time gathering information on the site. We concluded that this was consistent with the online customersí profile being different from that of offline customers as identified earlier and that their nanoflows would, subsequently, be different. We also concluded that repositioning the site for more appropriate clusters or nanosegments should increase the hit rate.

While the identification of the reasons and the resolution to the problem was swift and uninteresting from the business perspective, we were also able to present the company with the trends via click-stream patterns that their ìlegitimateî visitors adopted and suggested some design improvements primarily through nanoflows. This resulted in a tremendous improvement in identifying and directing customers to appropriate pages and increased the usage of ìContact Usî forms in a few weeks after the design changes were implemented.

Because there are identified gaps between the design and visitorsí goals and behaviors, the third step of GIST, segment, was employed. A primary activity is to combine the usersí characteristics and behaviors, thus identifying new nanosegments of the visitor population. We also develop new nanoflows.

As mentioned previously, a considerable decay rate (98 percent of the visitors did not complete the online form) was measured. Of the 2 percent customers that submitted the contact form, 29 percent were considered qualified leads that continued through the offline loan origination process. Their online behaviors indicated that, in addition to the form, they also spent time learning about the types of lending available through the company. It should be noted that to receive the incrementa lending information the visitor does register on the site, thus providing additional visitor characteristics, and a cookie is placed on their hard drive. This gives the company an ability to contact the visitor and begin to build a relationship with them even if they do not pursue a loan in the short-term. The Web site also starts providing customized information to customers to encourage repeat visits to the site based on the borrowersí long-term or future needs. Using this information, nanoflows can now be customized to their individual needs.

To analyze the online behaviors of the visitors and categorize them in detail, a log analysis tool provided by Digimine is used. For example, one of the classifications was based on the page content and the number of repeat visits (1 to 3; 4 to 6; 7 and more). These implicit behaviors led to the categorization of potential borrowers into the following:

(1) Need a loan now: customers with very specific objectives displayed during the visits.

(2) Need a loan in 2 to 6 months: customers who spend much of their time doing research on different aspects of the process and often came back several times throughout a long period of time.

(3) Intermediaries: an interesting and unanticipated category of visitors that were acting on behalf of multiple clients.

The identification of the intermediaries nanosegment was a major discovery for the company, since the site was not originally designed for such visitors. They were identified because they were anonymous visitors with very high repeat visits, visited a very broad range of different contents, and never submitted a ìcontact usî form. The discovery led to creation of new content, tools, and services that were targeted for this nanosegment. The companyís Web site has now implemented this content with a high success rate.

The direct borrowers (need loan now) who became qualified leads right away (those filling out the inquiry form and moving into the qualified prospect stage) make on average 1.17 visits to the Web site. These visitors view an average of 4.9 pages and spend 18.7 minutes per visit. Their primary path includes general lending information with brand image/credibility as the second most frequent path.

On the other extreme, intermediaries are less likely to complete the online query form, as they will refer their client directly to the qualifier (intermediaries tend to be repeat customers with existing relationships with the lender). Thus, it is more difficult to track their online behaviors and characteristics at this point. Therefore, to understand this segment, we conducted a primary research study. In-depth interviews were employed in the exploratory phase. Then, a descriptive survey was developed based on the interview results with the purpose of ascertaining the segmentís design and content preferences leading to more customized nanoflows.

Overlaying the cluster analysis results based on the revealed firmographics of the visitors with the behavioral analysis categorization described above led to the seven nanosegments as depicted in Figure 5.

![](/api/attachments/GCSE3ND8/fulltext/images/ca182fc97da8b81742271c440caeb4aa13ab7bc842b330c4788b5cc12225d951.jpg)  
Figure 5. Nanosegments of Financial Services Site

After the nanosegments were identified, customized content was identified for each one of them. For example, from surveys and targeted interviews, we found out that the loan now groups desire a contact name and phone number from the site. In its original configuration, the site did not efficiently provide this. Thus, for these segments, it was important for the company to provide the appropriate content (lessening frustration with the potential for the urgent borrower to go elsewhere). As the result of these analyses, specific nanoflows were designed and implemented, as shown in Figure 6. In addition, specific content for each of the groups (manufacturing, retail, and service) was further developed within these paths.

For the loan in 2 to 6 months category, the primary goal is seeking information. For them, the site fulfills their primary objective by providing content regarding the company and the process of financing. Specific content that is important for each nanosegment, such as type of loan, type of collateral, or specialized loan originator, is now being developed to be presented with the help of personalization technologies provided by BroadVision.

The most interesting situation arises with the nanosegment of intermediaries. As mentioned earlier, the site wasnít originally designed with these users in mind. Although the site now attempts to identify this segment of users, their past online behaviors indicate that this segment is reluctant to identify themselves. However, we believe that this identification, leading to customization specific to their needs, can be encouraged by implementing the content preferences articulated in the interviews and quantified by the survey: online resource center, borrower requirements, and loan parameters. In addition, we have proposed a secured extranet for checking loan status and filing loan documentation on their clientsí behalf. This customized content and nanoflows would encourage the indirect borrower (intermediary) to self-identify and create the opportunity to understand their segment further. However, even without individual identification,

![](/api/attachments/GCSE3ND8/fulltext/images/9faedf8c5a35d5562e1c6d942ad3cf9eca52b6d2666bbd1f9e194ff05eabb476.jpg)  
Figure 6. Redesigned Nanoflows for Loan Now Segments

BroadVision can use the behaviors and characteristics of the identified indirect borrowers and research results to predict if the visitor is an intermediary. The current identification process for the intermediary nanosegment is outlined in Figure 7.

The final GIST component, track, involves the application of usability studies and measuring the efficacy of providing more customized content based on the characteristics, behaviors, and preferences of nanosegments. It is critical to measure the effectiveness of the customized content and nanoflows through a rigorous tracking process since change in market characteristics could occur due to external factors such as regulatory changes or interest rate changes. Within this case study, ongoing analysis of clickstream behaviors and visitor characteristics (online query form) is being conducted. Metrics, such as the number of qualified leads by segment and number of unique visits by segment, are used as indicators of the GIST effectiveness. Overall, after the first round of changes derived from the GIST analysis were implemented, the number of closed deals whose leads were generated by the Web site increased by 350 percent. Considering the deal sizes (minimum of \$2 million), the company considers its new Web site investment and application of GIST a huge success.

## Implications and Conclusion

The electronic storefronts of the Web environment present information systems and marketing challenges which, if overcome, can create competitive advantages. One of the primary advantages is the ability to have a customer-centric siteóone that understands and adapts to customers objectives for the visit.

Within the traditional lifecycle approach as well as the existing marketing literature, an existing conceptual model for designing these customerfocused sites did not exist. A review of applicable marketing frameworks on building and solidifying the online customer relationship through customerization (Wind and Rangaswamy 2001), loyalty, segmentation,and retention provide a body of knowledge that has not effectively been translated into Web design or ongoing site maintenance that is focused on the customersí needs. It is through these models, applicable to the e-world, that we developed a methodology for the design and maintenance of customer-centric sites.

![](/api/attachments/GCSE3ND8/fulltext/images/4d7535f67903e21dce337f07f0ec93284d8564f3628f2c200e8e30d3f1099003.jpg)  
Figure 7. Intermediary Nanosegment Identification Process

We present a methodology following the design science principles of Hevner et al. (2004) to provide an operational approach for non-transactional Web sites such that they can play a critical role in driving business objectives. The key to our approach is the identification of nanosegments and nanoflows, the specific gap analyses for these groups of visitors, their preferred paths, and the consequent actionable findings that are derived from the process. The nanosegments are generated by extensive use of statistical analyses and data mining tools on the combination of online and offline data. The concept of nanosegments vis-‡-vis personalization and microsegments was presented in Figure 1. As demonstrated in Figure 1, the nanosegment approach understands the why (online behavior through rigorous analysis) and the who (understanding from similar behavioral patterns) while minimizing the privacy concerns that are voiced in a pure one-to-one dialogue.

We also present a business-to-business application, in a large company, as an illustration of how GIST translates the academic research into the practice of developing and maintaining a customer-centric Web site. The proof of concept also serves as a model validation. One of the crucial outcomes from this model validation was if the nanosegment, so defined, is the right unit of analysis for the design and maintenance activities, given the availability of information technologies that are adequate for analyzing the vast amounts of data. Consequently, important design and content factors were identified in the first application of GIST such as

ï incomplete preliminary targeting

inadequate descriptions of the type of loans sought by the Internet customers

the discovery of a new segment, intermediaries, which redefined the role of the Web site as well as pointed toward the requirement of infrastructure enhancements

As a result of applying the GIST model, the company experienced a significant increase in their ìhit rate,î justifying the expense in new Web site design.

We also briefly relate our approach to the popular usability studies of Web sites (see, for example, Nielsen [2000] and the Web site www.useit.com). Usability studies are an essential part of GISTís track phase when they are used in conjunction with assessing e-services metrics. After we identify and uncover the relevant nanosegments, usability studies provide additional insights in the redesign and repositioning of the nanoflows that are necessary to align the goals and objectives of each nanosegment with the site. The GIST methodology is much broader in the sense that it discovers the nanosegments and continuously evaluates the designed nanoflows. Usability studies are part of one of the four stages of GIST.

A natural research follow-up of this work is to evaluate the applicability of the several available statistical and data mining techniques that can be used for the nanosegmentation step of GIST. Because the available data is collected in various ways by different systems, the information architecture necessary for GIST may be at different levels of implementation. For example, in business-to-consumer environments, due to the much richer set of observations about customer profiles and their behavior, different classification techniques might be more appropriate than kmeans cluster analysis.

Another interesting research question is related to the optimal number of nanosegments to satisfy. Depending on the objective function of the company, which may include costs to generate dynamic Web pages, emphasis may be given to better meet the requirements of some and not al identified nanosegments. Also, some nanosegments may not be clearly identified in every cycle of GIST. Knowledge of the underlying business will help better identification of these in the next cycle of the continuous methodology.

Finally, we emphasize the importance of establishing precise metrics for the continuous evaluation that takes place within the individual nanosegment gap analyses, as well as the overall aggregate performance metrics. This will be pursued through future testing and applications validating the GIST model. These tests are designed to yield a taxonomy or classification structure based on a firmís online information architecture and their e-business marketing strategies. Firms may employ this taxonomy to design their content and ongoing maintenance schedules maximizing their customer-centric sites as an integral component of their competitive arsenal.

## Acknowledgments

This research was supported in part by TECI (the Treibick Electronic Commerce Initiative), part of the Department of Operations and Information Management, School of Business, University of Connecticut. The authors are also thankful for the comments received from OPIM workshop participants at the University of Connecticut and the participants of MIS Research Center seminar participants at the University of Minnesota.

## References

Agrawal, R., Imielinski, T., and Swami, A. ìMining Association Rules Between Sets of Items in Large Databases," in Proceedings of the 1993 ACM SIGMOD International Conference Management of Data, P. Buneman and S. Jajodia (Eds.), ACM Press, New York, 1993, pp. 207-216.

Albert, T., and Sanders, W. B. E-Business Marketing, Prentice-Hall, Upper Saddle River, NJ:, 2003.

Barki, H., and Hartwick, J. ìMeasuring User Participation, User Involvement, and User Attitude," MIS Quarterly (18:1), June 1994, pp. 59-82.

Csikszentmihalyi, M. Beyond Boredom and Anxiety, Jossey-Bass, San Francisco, 1977.

Davis, F. ìPerceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology," MIS Quarterly (13:3), September 1989, pp. 319-340.

Donoghue, K. Built for Use: Driving Profitability Through the User Experience, McGraw-Hill, New York, 2002.

El Sawy, O., Malhotra, A., Gosain, S. and Young, K. ìIT-Intensive Value Innovation in the Electronic Economy: Insights from Marshall Industries,î MIS Quarterly (23:3), September 1999, pp. 305-335.

Green, G. I., and Hughes, C. ìEffects of Decision Support Training and Cognitive Style on Decision Process Attributes," Journal of Management Information Systems (3:2), Fall 1986, pp. 81-93.

Greenspan, R. ìAmerican Surfers Keep It Simple,î Internetnews.com, September 19, 2002 (available online at http://www.internetnews. com/stats/article.php/1466661).

Hevner, A. R., March, S. T., Park, J., and Ram, S. ìDesign Science in Information Systems Research,î MIS Quarterly (28:1), 2004, pp. 75- 105.

Hoffman, D. L., and Novak, T. ìMarketing in Hypermedia Computer-Mediated Environments: Conceptual Foundations,î Journal of Marketing (60:3), 1996, pp. 50-69.

Hoffman, D. L., Novak, T., and Chatterjee, P. ìCommercial Scenarios for the Web: Opportunities and Challenges,î Journal of Computer-Mediated Communication, Special Issue on Electronic Commerce (1:3), 1995 (available online at http://www.ascusc.org/jcmc/vol1/issue3/ hoffman.html).

Holland, J. H. ìA Mathematical Framework for Studying Learning in Classifier Systems,î Physica (22D:1-3), 1986, pp. 307-317.

Hong, W., Tam, K., and Yim, C. ìE-Service Environment: Impacts of Web Interface Characteristics on Consumersí On-line Shopping Behaviorî in E-Service: New Directions in Theory and Practice, R. Rust and P. Kannan (Eds), M. E. Sharpe, Armonk, NY, 2002, pp. 108-130.

Inmon, W. H. Building the Data Warehouse (3<sup>rd</sup> ed.), Wiley and Sons, New York, 2002.

Kaul, A. Personal e-mail communication, University of Tasmania, April 27,1995.

Kotler, P. Marketing Management (11<sup>th</sup> ed.), Prentice-Hall, Upper Saddle River, NJ, 2003.

Lee, S. M., Kim, Y. and Lee, J. ìAn Empirical Study of the Relationships Among End-User

Information Systems Acceptance, Training, and Effectiveness," Journal of Management Information Systems (12:2), Fall 1995, pp. 189-202.

Levin, N., and Zahavi, J. ìPredictive Modeling Using Segmentation,î Journal of Interactive Marketing (15:2), Spring 2001, pp. 2-22.

McKeen, J. D., Guimaraes, T., and Wetherbe, J. C. ìThe Relationship Between User Participation and User Satisfaction: An Investigation of Four Contingency Factors," MIS Quarterly (18:4), December 1994, pp. 427-451.

Nielsen, J. Designing Web Usability, New Riders Publishing, Indianapolis, IN, 2000.

Parsons, A., Zeisser, M., and Waitman, R. ìOrganizing Today for the Digital Marketing of Tomorrow,î Journal of Interactive Marketing (12:1), Winter 1998, pp. 31-46.

Peltier, J., and Schribrowsky, J. ìThe Use of Need-Based Segmentation for Developing Segment-Specific Direct Marketing Strategies, Journal of Direct Marketing (11:4), Fall 1997, pp. 53-62.

Peppers, D., and Rogers, M. Enterprise One to One, Doubleday/Currency, New York, 1997.

Peppers, D., and Rogers, M. The One-to-One Future, Doubleday/Currency, New York, 1996.

Rust, R. T., and Kannan, P. T. ìThe Era of e-Serviceî in E-Service: New Directions in Theory and Practice, R. Rust and P. Kannan (Eds.), M.E. Sharpe, Armonk, NY, 2002, pp. 3-24.

Stafford, T. ìE-Services,î Communications of the ACM (46:6), 2003, pp. 26-28.

Weinstein, A. Market Segmentation , McGraw-Hill Professional, New York, 1993.

Wind, J., and Rangaswamy, A. ìCustomerization: The Next Revolution in Mass Customization, Journal of Interactive Marketing (15:1), 2001, pp.13-32.

Xue, M., Harker, P., and Heim, G. ìIncorporating the Dual Customer Roles in e-Service Design, working paper, Wharton Financial Institutions Center, University of Pennsylvania, 2003.

Zeithamal, V., Parasuraman, A., and Malhotra, A. A Conceptual Framework for Understanding e-Service Quality: Implications for Future Research and Managerial Practices, Report 00- 115, Marketing Science Institute (MSI), Cambridge, MA, 2000.

## About the Authors

Terri Albertís research and teaching focus is ebusiness marketing. She has multiple conference papers and publications in the application of technology in marketing. Dr. Albert has been teaching Digital Marketing for seven years and has developed and conducted several Internet conferences for the business and academic communities. Technology and its implications for marketing, legal, and information management were the focus of the conferences. Additionally, she cofounded an e-business outreach program with the purpose of customizing e-business strategies for business partners. This has enhanced her knowledge of the technology impact on companiesí marketing strategies as well as provided an intellectual foundation for scholarly works. One of the partnerships led to her involvement with the General Electric e-business think tank (edgelab) of which she is the marketing faculty representative.

Paulo B. Goes is the Gladstein Professor of Information Management & Innovation, an endowed position at the Department of Operations and Information Management at the University of Connecticut. He is also codirector of the Treibick Electronic Commerce Initiative (TECI) and associate director of CITI (Connecticut Information Technology Institute). He was involved in the conceptualization and implementation of edgelab, an e-business think tank partnership with Genera Electric. He received his M.S. and Ph.D. degrees in Computers and Information Systems from the University of Rochester. His research interests are in the areas of Internet technologies and electronic commerce, design and evaluation of models for e-business, on-line auctions, database recovery and security, computer networking and technology. His publications have appeared in

MIS Quarterly, Management Science, Information Systems Research, Operations Research, Decision Sciences, Communications of the ACM, IEEE Transactions on Communications, IEEE Transactions on Computers, INFORMS Journal on Computing, and Decision Support Systems, among others. He is currently associate editor of Information Systems Research and INFORMS Journal of Computing. He has served as associate editor of the e-business special issue of Management Science and is on the editorial board of Journal of Database Management and POMS.

Alok Gupta is an associate professor of Information Systems in the Carlson School of Management, University of Minnesota. He received his Ph.D. in Management Science and Information Systems from The University of Texas at Austin. Before joining Carlson, he was involved in the conceptualization and implementation of edgelab, an e-business think tank partnership with General Electric and University of Connecticut. His research has been published in various information systems, economics, and computer science journals such as Management Science, Information Systems Research, Communications of the ACM, Journal of MIS, Decision Sciences, Journal of Economic Dynamics and Control, Computational Economics, DSS, IEEE Internet Computing, International Journal of Flexible Manufacturing Systems, and Journal of Organizational Computing and Electronic Commerce, among others. He received prestigious NSF Career award for his research in On-line Auctions in 2001. His current research and teaching interests are in the area of economic modeling and analysis of electronic commerce. He serves on the editorial boards of Information Systems Research, Decision Support Systems, and Brazilian Electronic Journal of Economics.
