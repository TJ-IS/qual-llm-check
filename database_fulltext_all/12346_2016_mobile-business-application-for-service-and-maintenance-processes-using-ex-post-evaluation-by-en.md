---
otero_id: 12346
otero_key: "GBJU6T52"
title: "Mobile business application for service and maintenance processes: Using ex post evaluation by end-users as input for iterative design"
authors: "Christine Legner; Nils Urbach; Christoph Nolte"
year: "2016"
journal: "Information & Management"
doi: "10.1016/j.im.2016.03.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: Mobile Business Application for Service and Maintenance Processes: Using Ex Post Evaluation by End-Users as Input for Iterative Design

Authors: Christine Legner Prof. Dr. Nils Urbach Prof. Dr. Christoph Nolte Dipl.Ing., MBA

![](/api/attachments/GBJU6T52/fulltext/images/44bb6ef8c57b3089ddcf198ad8e903669c13401d4e958d6105e50f9384f73b73.jpg)

PII: S0378-7206(16)30015-5

DOI: http://dx.doi.org/doi:10.1016/j.im.2016.03.001

Reference: INFMAN 2889

To appear in: INFMAN

Received date: 3-7-2014

Revised date: 8-2-2016

Accepted date: 6-3-2016

Please cite this article as: C. Legner, N. Urbach, C. Nolte, Mobile Business Application for Service and Maintenance Processes: Using Ex Post Evaluation by End-Users as Input for Iterative Design, Information and Management (2016), http://dx.doi.org/10.1016/j.im.2016.03.001

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Mobile Business Application for Service and Maintenance Processes: Using Ex Post Evaluation by End-Users as Input for Iterative Design

## Authors:

Prof. Dr. Christine Legner

Faculty of Business and Economics (HEC)

Department of Information Systems

University of Lausanne

CH-1015 Lausanne

Tel +41 21 692 3432christine.legner@unil.chhttp://hec.unil.ch/people/clegner

Prof. Dr. Nils Urbach (Corresponding author)

Faculty of Law, Business and Economics Chair of Information Systems and Strategic IT Management University of Bayreuth

Wittelsbacherring 10 95447 Bayreuth, Germany

Tel. +49 921 55-4712 nils.urbach@uni-bayreuth.de http://www.sim.uni-bayreuth.de

Dipl.Ing. Christoph Nolte, MBA

DEKRA Automobil GmbH

Abt.: AP4 Entwicklung Technik / Fahrzeugprüfwesen

Handwerkstr. 15

HV-0370 Stuttgart

D-70565 Stuttgart

Tel.: +49 711/78612494

christoph.nolte@dekra.com

http://www.dekra.com

Mobile Business Application for Service and Maintenance Processes: Using Ex Post Evaluation by End Users as Input for Iterative Design

## Abstract

Although mobile technologies are increasingly used for business purposes, many companies have found it difficult to successfully implement them. Not only do the rapid technological changes increase the risks of companies’ investments into mobile technologies, but many such applications have also failed to gain user acceptance. In contrast to the consumer domain, there are very few empirical studies of mobile applications’ effectiveness from the perspectives of professional end users. Furthermore, designing mobile business applications has become an increasingly iterative and incremental activity, and ex post evaluations by actual users can provide crucial feedback to an iterative design process. In this study, we seek to contribute to establishing a design cycle that closely links the building and the evaluation of mobile business applications. Our objectives are to (1) gain a better understanding of mobile business applications’ success by means of ex post evaluations from end users, and to (2) leverage these empirical insights to inform the design of mobile business applications. We conducted the study in collaboration with DEKRA Automotive, which offers expert services in the automotive sector with experience in mobile business applications. Our primary contribution is a systematic approach to using ex post evaluation as input for the iterative design of mobile business applications. We suggest an adapted version of the D&M information system (IS) Success Model, which has process quality as an additional construct, as a basis for ex post evaluations of a mobile business application by its end users. Furthermore, we illustrate how a performance-based analysis of the empirical results enables one to derive priorities and recommendations for future design iterations. Our results reveal that system quality and process quality are the main determinants of individual benefits of

using mobile business applications. Our findings thus contradict other studies that identify information quality as a significant motivator of (consumer-oriented) mobile data services. We conclude that a mobile business application’s design should focus on process quality, emphasizing functional support for operational tasks in a specific work context while ensuring system quality, which is largely affected by technology platform choices.

Keywords: Automotive industry, mobile business applications, IS adoption, IS success, mobile services, service and maintenance processes

## 1

## Introduction

Mobile devices such as personal digital assistants (PDAs), tablet computers, and smartphones have become widespread and provide users with real-time access to information and services from anywhere and at any time. With the increasing proliferation of mobile technologies, the traditional application areas of computing have broadened to encompass a variety of scenarios, such as m-commerce, mobile banking, and entertainment services (Bouwman et al., 2009). Companies see great potential in utilizing mobile technologies to help business users to perform their tasks more quickly and with higher quality while they are away from their stationary office (Gebauer et al., 2010; Nah et al., 2005). However, in practice, companies’ adoption of mobile business applications has long lagged behind expectations. On the one hand, investments in mobile business applications are risky, owing to rapid technological changes. In their early phases, emerging mobile platforms and devices target individual users and often do not fulfill the requirements of corporate information technology (IT). On the other hand, many companies have found it difficult to successfully implement mobile applications and to gain user acceptance. In contrast to the consumer domain, there is a dearth of empirical insights into the adoption of mobile business applications and their effectiveness from the perspectives of business users. To date, “the debate has largely failed to embed

glowing accounts for technological potential in a sound discussion of organizational realities” (Sørensen et al., 2008, p. 243).

This gap in the research motivates our study. Building on design science research and the current discourse on design evaluation (Helfert, 2012; Hevner et al., 2004; Peffers et al., 2008), we argue that mobile business applications, as innovative IT artifacts, should be evaluated using utility as a primary criterion for end users. Since designing mobile business applications has become an increasingly iterative and incremental activity, ex post evaluations of mobile business applications can provide crucial feedback to an iterative design process. Thus, our primary objective is to assess mobile business applications’ success in the organizational context based on empirical data from actual users. Our secondary objective is to demonstrate how these empirical insights might inform mobile business applications’ design. We thereby contribute to establishing a design cycle that closely links artifact building and artifact evaluation. We collaborated with DEKRA Automotive, a subsidiary of the German-based company DEKRA AG that offers expert services in the automotive sector with extensive experience of mobile business applications in service and maintenance processes. Our contribution is a systematic approach for leveraging ex post evaluations from the perspective of end users for the iterative design of mobile business applications: we propose to evaluate mobile business applications based on an adapted version of DeLone and McLean’s IS success model, which has process quality as additional construct. Although the IS success model is an established theoretical framework that has been used to explain the success of various IS types (Urbach et al., 2009), to our knowledge, it has not yet been used to analyze the success of mobile business applications. The empirical analysis of the resulting performance–effect matrix allows us to derive priorities for improving the design of the mobile solutions.

#

This paper – a significantly revised and extended version of a conference paper (Legner et al., 2011) – is structured as follows: in the next section, we review previous research on mobile applications’ design and adoption, highlighting the research gap we intend to address. We then introduce DEKRA AG’s research context and its approach to mobile business applications’ design and implementation. We then explain our evaluation framework. In the following sections, we present the three-step approach we took: model development, ex post evaluation, and the performance-based model analysis as input for iterative design. We conclude by summarizing our findings and implications as well as presenting an outlook on future research opportunities.

## 2 Mobile Applications’ Design, Success, and Adoption[A1]

## 2.1 Design of Mobile Applications

Mobile computing comprises all activities, processes, and applications that are conducted via wireless and mobile communication networks. Mobile technologies have not only broadened computing’s traditional application areas but also made application design and development processes more complex and demanding than in the past (Tarasewich, 2003). Although all applications need usable interfaces, good interface design of mobile applications is particularly challenging. This is not only due to the size of the mobile front-ends in general and the diversity of the segment of mobile devices, which comprises smartphones, PDAs, and tablets with differing hardware capabilities, operating systems, and/or software platforms (Wasserman, 2010). It is also due to restrictions of the various environments in which mobile applications are executed (Table 1), as opposed to traditional applications, which are executed on relatively stable desktop PCs. Thus, researchers have introduced contextuality (Benou and Vassilakis, 2010; Kakihara and Sørensen, 2002; Tarasewich, 2003) to describe

#

the various circumstances in which mobile devices are used and to emphasize the situatedness of human interactions that involve mobile devices.

One dimension of context is a computing environment’s characteristics, which include (a) the networking infrastructure’s properties (latency, bandwidth, disconnections, and cost), (b) the individual devices’ properties (memory capacity, battery lifetime, processing power, input/output, and communication capabilities), and (c) the properties of the operating systems (user interface, security, and program execution). A computing context’s characteristics and restrictions should be considered while designing mobile applications. For instance, limited input capabilities dictate the need for less typing on the keyboard. Besides the computing context, user mobility demands that the operational environment’s properties are considered when designing mobile applications. On the one hand, the outside environment (noise levels, brightness, and temperature) imposes restrictions when using mobile applications. On the other hand, the parameters that comprise an application’s operational environment (e.g., the location) may enhance the mobile application with information that might benefit users. As a third domain, the user context influences a mobile application’s design in terms of user interface, functionality, and content. Users of mobile business applications vary vastly regarding qualities, such as computer literacy, preferences, and skills, which must be taken into account. Finally, user activities and interactions drive the need for mobile support and interaction modalities.

<table><tr><td colspan="3">Computing domain</td><td>Environment domain</td><td colspan="2">User domain</td></tr><tr><td>Communication network</td><td>Mobile device</td><td>Operating system</td><td>Operational environment</td><td>User skills and preferences</td><td>User activities</td></tr><tr><td>WLAN</td><td>Smartphone</td><td>Windows</td><td>Brightness</td><td>Age</td><td>Tasks and</td></tr><tr><td>UMTS</td><td>Personal</td><td>Mobile</td><td>Noise levels</td><td>Gender</td><td>goals of</td></tr><tr><td>Bluetooth</td><td>digital</td><td>Windows 7</td><td>Temperature</td><td>Computer</td><td>mobile users</td></tr><tr><td rowspan="4">Mobile ad hoc network ...</td><td>assistant (PDA)</td><td>Phone</td><td>Wet conditions</td><td>literacy</td><td>Information requirements</td></tr><tr><td>Mobile Internet device (MID)</td><td>Android iOS ...</td><td>Vibrations ...</td><td>User preferences ...</td><td>Work processes</td></tr><tr><td>Ultra-mobile PC (UMPC)</td><td></td><td></td><td></td><td>Events ...</td></tr><tr><td>Tablet PC ...</td><td></td><td></td><td></td><td></td></tr></table>

## 2.2 Empirical Studies on Mobile Service Adoption and Success[A2]

For users, mobile computing is associated with unique value factors such as ubiquity, instant connectivity, personalization, and timeliness (Lee et al., 2010). Exploring and evaluating mobile computing’s use and requirements from the perspectives of end users has thus attracted much interest from researchers. Table 2 presents selected empirical studies and illustrates that their majority investigates consumer-oriented mobile services, notably mobile phone and data services (Lee et al., 2010), m-commerce (Benou and Vassilakis, 2010; Lee et al., 2007; Lee and Benbasat, 2003; Tarasewich, 2003), m-payment (Pousttchi, 2008), and mobile banking (Al-Jabri and Sohail, 2012; Koo et al., 2013; Luarn and Lin, 2005). They focus on services that were introduced relatively early on and therefore have established traditions. From multiple surveys, Bouwman et al. (2009) observe a move from talk-based services toward content-based services. They classify mobile services into three categories:

#

content (or information) services, messaging (or communication) services, and a broad set of advanced mobile services that enable transactions or specific applications and that are provided via high-capacity networks. Given the many types and facets of mobile services, Bouwman et al. (2009) argue that mobility in itself requires further conceptualization; we also need a deeper understanding of the differences between the various types of services and applications, and the kinds of value they offer.

Although the adoption of consumer-oriented mobile services by end users has been studied extensively via qualitative and quantitative-empirical surveys, their results cannot be directly applied to mobile business applications (Gebauer et al., 2010): consumers decide whether or not to use mobile services based on their individual preferences and motivations, while businesses implement mobile technologies to automate and streamline business processes and to increase the productivity of their remotely distributed employees.

<table><tr><td>Reference</td><td>Focus</td><td>Application area</td><td>Theoretical foundations</td></tr><tr><td>Benou and Vassilakis (2010)</td><td>Consumers</td><td>Mobile commerce</td><td>Not explicated</td></tr><tr><td>Bouwman et al. (2009)</td><td>Consumers</td><td>Mobile services</td><td>Diffusion of innovations (Rogers, 1983)</td></tr><tr><td>Chatterjee et al. (2009)</td><td>Business</td><td>Mobile work in health care</td><td>Information systems success (DeLone and McLean, 1992; DeLone and McLean, 2003)</td></tr><tr><td>Gebauer et al. (2010), Gebauer (2008)</td><td>Business</td><td>Mobile business applications</td><td>Task–technology fit (Goodhue and Thompson, 1995), technology acceptance model (Davis, 1989)</td></tr><tr><td>Al-Jabri and Sohail(2012)</td><td>Consumers</td><td>Mobile banking</td><td>Diffusion of innovations(Rogers, 1983)</td></tr><tr><td>Koo et al. (2013)</td><td>Consumers</td><td>Mobile banking</td><td>Information systems success (DeLone and McLean, 1992; DeLone and McLean, 2003)</td></tr><tr><td>Lee et al. (2007)</td><td>Consumer</td><td>Mobile commerce</td><td>Task–technology fit (Goodhue and Thompson, 1995)</td></tr><tr><td>Lee et al. (2010)</td><td>Consumer</td><td>Mobile data services</td><td>Two-factor theory (Herzberg et al., 1959)</td></tr><tr><td>Lee and Benbasat (2003)</td><td>Consumer</td><td>Mobile commerce</td><td>Not explicated</td></tr><tr><td>Luarn and Lin (2005)</td><td>Consumer</td><td>Mobile banking</td><td>Technology acceptance model (Davis, 1989), theory of planned behavior (Ajzen, 1991)</td></tr><tr><td>Mallat (2007)</td><td>Consumer</td><td>Mobile payment</td><td>Diffusion of innovations (Rogers, 1983)</td></tr><tr><td>Nah et al. (2005)</td><td>Business</td><td>Mobile business applications</td><td>Not explicated</td></tr><tr><td>Pousttchi (2008)</td><td>Consumer</td><td>Mobile payment</td><td>Not explicated</td></tr><tr><td>Sørenson et al. (2008)</td><td>Business</td><td>Mobile business applications</td><td>Not explicated</td></tr><tr><td>Tarasewich (2003)</td><td>Consumers</td><td>Mobile commerce</td><td>Not explicated</td></tr></table>

Table 2. Selected Empirical Studies on Mobile Services’ Adoption and Success

The few studies dedicated to mobile business applications include those of Gebauer et al. (2010) and Gebauer (2008), who combined the concept of task–technology fit and the technology acceptance model (TAM) to explain the adoption and use of mobile technologies in business settings. Nah et al. (2005) demonstrated the impact of mobile business applications and value in improving the business users’ productivity, as well as increasing process efficiency and effectiveness in a utility company. Based on 11 in-depth qualitative studies, Sørenson et al. (2008) synthesize organizational implications specifically related to the applications of mobile IT. They identified a number of trade-offs, for instance, between mediated versus situated interactions, management control versus discretion, individual versus collective collaboration, or ubiquitous versus opaque technologies.

## 2.3 Research Gap

We have identified and reviewed two research streams related to mobile applications: the first (Section 2.1) investigates mobile applications’ architectural design and emphasizes contextual factors in mobile application development. This research stream can be associated with mobile applications’ building or development phase. The second research stream (Section 2.2) studies the success and adoption of mobile applications via empirical investigations. It relies on data from actual or potential users to evaluate mobile services and applications. Neither research stream has fully embraced the specificities of mobile business applications: they propose either generic guidelines or architectures for mobile applications’ design, or focus mostly on consumer-oriented mobile services and their adoption. Furthermore, we have not seen any approaches that establish a design cycle that closely links the building and evaluation phases and thereby leverages empirical evaluation to improve a mobile business application’s design.

## 3 Research Setting

## 3.1 Motivation for Studying Mobile Business Applications in the Context of Service and Maintenance

#

Our research setting is technical customer service and maintenance – one of the most promising areas for mobile business applications (Fellmann et al., 2011; Thun, 2008). This has been confirmed by in-depth case studies (Legner and Thiesse, 2006; Nah et al., 2005; Thomas et al., 2007): first, these processes are highly information-intensive and generate tremendous amounts of paper for documenting maintenance and inspection results. Second, documents must be archived for years, to allow for traceability and/or to comply with safety regulations. Digital data management can eventually significantly reduce administrative costs. Mobile technologies also impose specific work processes, thereby ensuring that technicians complete their work accurately and according to predefined instructions

## 3.2 Mobile Business Applications at DEKRA Automotive

We collaborated with DEKRA Automotive, a subsidiary of the global German company DEKRA AG. One of its core business areas is periodical technical vehicle inspection (PTI) in Europe, a state-prescribed regular roadworthiness service for road vehicles. German legislation prescribes that each vehicle be checked for electronically regulated safety systems such as airbags, electronic stability control (ESC), and antilock braking system (ABS); therefore, specific information needs to be available during vehicle testing. To cover these legislative demands, inspections had to change fundamentally, requiring comprehensive access to information and applicable procedures. Accordingly, the rapid development of mobile technology opens opportunities for both the automotive service industry, particularly for inspection services.

DEKRA Automotive has been evaluating mobile solutions that can improve work processes during inspections since 2004. During the initial 2-year project, hardware and software were chosen and evaluated. The design and development phase of the mobile application followed: first, existing work processes were analyzed to identify the main tasks performed by employees. These tasks were subsequently transformed into support tasks for use on ultra-

#

mobile devices. When DEKRA was faced with implementing the directive for PTI’s update in Germany, it recognized the need to use vehicle-specific information in inspections. So, DEKRA IT developers added the associated information requirements to the scope of their ongoing mobile development project. The implementation of the final solution had to consider hardware and software restrictions. After a 4-year development phase, hardware from the consumer market and proprietary PTI software fit together well. The first set of mobile devices, called DEKRA Pocket Computers (DPCs), was rolled out to DEKRA inspection engineers in the middle of 2008.

At the end of 2008, > 2,000 DEKRA employees involved in vehicle testing and related services were equipped with the DPC. After the establishment phase (about 1 year), DEKRA decided to have its users evaluate the DPC. At the time, the DPC’s use was still not mandatory for all users. The evaluation sought to validate the implementation success and utility of DPCs from the perspectives of end users and to gain insights related to future mobile business application designs. The empirical findings would allow DEKRA developers to align their defined key demands for further development with end-user expectations. In light of rapid technological changes, a technology agnostic evaluation was perceived as valuable to understand important design factors from the perspectives of end users. As DEKRA could not avoid the migration to a new platform, for technological reasons, the empirical insights were intended to inform the mobile application group and to help them define requirements toward designing a new platform, once a migration became necessary.

## 3.3 The DEKRA Desktop Pocket PC (DPC)

With the development and introduction of its DPC, DEKRA sought to support its employees with the most effective mobile solution possible. From the very outset, DEKRA was aware that the DPC’s success was dependent on this mobile solution’s design and its acceptance by end users. Thus, DEKRA invested much time and effort into designing this mobile business application’s foundations, emphasizing three primary aspects as follows:

Mobile platform choice: it prioritized usability and operation of the device in its dayto-day working environment.

Mobile application development: it sought to design the application structure and functionalities to be as intuitive as possible, so as to effectively support primary tasks and to allow for easy data input during car inspections.

Mobile application support: use of the mobile application had to be self-explanatory, requiring as little support as possible.

Concerning the mobile platform choice, for a hardware platform, DEKRA decided to use the HP IPAQ 214, which met its predefined requirements relating to size, costs, readability, and battery life. DEKRA realized its DPC as a single-hand operation application. This would allow employees to use it in parallel with a mobile phone. Furthermore, a pen-operating mode was used to give users the most flexible and individual operating options.

In terms of mobile application development, DEKRA’s mobile business application was structured to comprise three main functional areas: the order overview, the fault documentation tree, and the data collection pages. At the start of each application, the order overview displays the most relevant vehicle identification parameters, and provides filter functions for selecting further functionality. From this page, the system settings are also accessible, and can be individually set by every user.

The fault documentation, which represents the DPC’s core, is realized by a tree structure. Its design was very similar to the stationary PC application, in order to make utilization easier for employees (recognition effect). To effectively support fault documentation, the application was used with a minimum of interactions and/or clicks and a very intuitive navigation via either the navigation key or pen control.

For the data collecting pages, DEKRA realized various input features, which support users with the easiest and most effective handling during their technical work:

Swift input method for dates in a segmented order via the use of the navigation key

Shortcuts to main areas

User-specific suggestions for alphanumeric input

Prediction of expected parameters or figures, such as brake force values referring to vehicle weight.

Concerning end-user support for the mobile application, DEKRA sought to provide a lowsupport application. In case of problems, users could follow a simple procedure to initialize the device.

## 4 Framework for Evaluating Mobile Business Applications as Input for an Iterative Design Cycle

Many companies have found it difficult to gain user acceptance when introducing mobile business applications. Adoption issues force them to consider and integrate user feedback more carefully into the design cycle. Because mobile application design is becoming an increasingly iterative and incremental activity, an ex post evaluation of the design outcomes (i.e., the artifact in use) can provide crucial feedback to an iterative design process (Fig. 1). If design evaluation is based on end-user surveys, it delivers empirical evidence that the designed artifact achieves the purposes for which it was designed (Peffers et al., 2008). In design science research (Pries-Heje et al., 2008), the assessment of an innovative IT artifact based on the subjective opinions of the artifact’s de facto users is considered to be an ex post evaluation strategy. It is critical to realize a complete design cycle that connects the building phase with the evaluation phase in real-world settings (Helfert, 2012; Peffers et al., 2008).

![](/api/attachments/GBJU6T52/fulltext/images/157c64b4740f42c22308f6841720ba828305b18f5b53677c0fcc08c4d417ea41.jpg)  
Figure 1. Iterative Design Cycle for Mobile Business Applications

Although previous studies have suggested several evaluation criteria for IT artifacts, such as functionality, completeness, performance, or usability (Hevner et al., 2004), the ultimate goal is to assess their value or utility. In their recent review of evaluation criteria, Helfert et al. (2012) suggested differentiating between (1) quality, as a function of the artifact assessed against a specification (independent of users), and (2) utility, to assess whether the output fits its purpose and meets users’ subjective needs (dependent on users). Our approach can be associated with the second alternative, and uses user-dependent evaluation criteria. Building on this rationale, we suggest using user-dependent evaluation criteria. We propose a three-stage approach to evaluate mobile business applications’ utility for end users and to derive priorities for their subsequent incremental development (building phase): (1) first, we develop an evaluation model on the basis of the D&M IS Success Model (DeLone and McLean, 2003) considering existing studies on mobile applications and related fields. (2) By using the adapted D&M IS Success Model, we carry out an ex post evaluation, collecting survey data from mobile service users, and conduct an empirical validation applying a path modeling approach. Finally, (3) we conduct a performance-based analysis to interpret the empirical results from the previous stage, and to derive priorities for improving the mobile

solution’s design. We will present each of the three stages in the following sections. Although we present an exemplary iteration of the design cycle, our vision is that the evaluation and building phases alternate (e.g., annually).

## 5 Model Development

## 5.1 The D&M IS Success Model

As there is no established model for evaluating mobile business applications’ utility from the perspectives of end users, our research process comprised reviewing the literature to find a suitable theoretical foundation for our research endeavor. We identified the D&M IS Success Model (DeLone and McLean, 2003) as a comprehensive evaluation framework to provide a sound basis for our study. In contrast to other models, such as the TAM (Davis, 1989), the D&M IS Success Model offers a relatively broad and comprehensive evaluation approach, and is also fairly parsimonious. Most importantly, its success dimensions are quality and use of constructs, which reflect the two aforementioned evaluation criteria types, that is, quality and utility. Furthermore, its proposed associations have been validated by a large number of empirical studies, and many validated measures exist that can be reused to assess the proposed success dimension. Several success models for evaluating specific IS types – for instance, knowledge management systems (Kulkarni et al., 2007) or enterprise systems (Gable et al., 2003), but also mobile technologies in health care (Chatterjee et al., 2009) or banking (Koo et al., 2013) – have been developed from this theory. As the D&M IS Success Model does not rely on technology features, but on quality dimensions from the perspectives of end users, it allows one to compare success factors for different types of applications and technologies. A comprehensive presentation and discussion of the D&M IS Success Model and its application in previous research can be found in the review articles provided by

#

Urbach et al. (2009), Urbach and Müller (2011), and Petter et al. (Petter et al., 2008; Petter et al., 2012).

## 5.2 Constructs

To adapt the D&M IS Success Model to mobile business applications, we reviewed existing studies on consumer-oriented mobile applications that identify system quality and information quality as two key dimensions with high impacts on the usage of mobile data services (Lee et al., 2010). We also considered some of the extensions to the model related to business applications, and specifically employee portals (Urbach et al., 2010), because mobile applications share many commonalities with web portals such as front-end integration of information, communication, and applications. Based on this literature, we introduced process quality as an additional construct. This construct complements information and system quality, by measuring how the system, together with the presented information, supports the user’s work routines. We argue that process quality is particularly relevant to reflect unique value factors of mobile business applications, such as ubiquitous use, instant connectivity, and assistance in completing complex tasks. Table 3 includes a complete list of the seven constructs we used for the development of the evaluation model. To control for support concerning the mobile business application that its users receive from their management, which is considered a primary factor in IS use and adoption in organizational contexts, we defined management support as a control variable.

<table><tr><td>Construct</td><td>Description</td></tr><tr><td>System quality</td><td>Can be regarded as the extent to which the mobile business application is easy to use to accomplish tasks. For mobile business applications, system quality relates among others to system performance and interface design and navigation.</td></tr></table>

#

<table><tr><td>Information quality</td><td>Focuses on the quality of the information the mobile application provides for its users. Information quality has been shown to be a prominent success factor when investigating IS success (McKinney et al., 2002). For mobile business applications, we considered the aspects of usefulness, understandability, and timeliness.</td></tr><tr><td>Process quality</td><td>Summarizes the measures that capture the quality of the mobile business application's support of the users' work routines. It is an additional construct that has been added, in line with the studies by Urbach et al. (2010) and Chen et al. (2013). Specifically, it comprises measures related to the efficiency, reliability, comprehensibility, and traceability of the supported processes.</td></tr><tr><td>Service quality</td><td>Includes overall support measures relating to the mobile business application that are delivered by the service provider. It considers the measures of responsiveness, empathy, reliability, and competence of the responsible support personnel.</td></tr><tr><td>Use</td><td>Measures the mobile business application's perceived de facto use by the employees. It will be assessed by the extent to which the main functionalities provided by the mobile business application are used.</td></tr><tr><td>User satisfaction</td><td>An employee's affective attitude to the mobile business application when he or she interacts directly with it. The proposed success dimension evaluates adequacy, efficiency, effectiveness, and overall satisfaction with the mobile business application.</td></tr><tr><td>Individual benefits</td><td>Subsume perceived individual benefits measures that the employees gain by using the mobile business application. These benefits cover the aspects of willingness to use, helpfulness, and usefulness.</td></tr><tr><td>Management support (control variable)</td><td>Relates to the support that the user receives by his or her management on the mobile business application. It evaluates the leadership team’s active encouragement of and support for the mobile application’s usage.</td></tr></table>

Table 3. Constructs of the Adapted D&M IS Success Model

## 5.3 Hypotheses

Based on the findings of DeLone and McLean (1992; 2003) and Urbach et al. (2010), as well as other related studies, we propose a model that assumes that system quality, information quality, process quality, and service quality are linked to user satisfaction and the mobile business application’s use, and that these – in turn – influence the individual benefits of using the application. To keep the model parsimonious, we omitted the feedback about individual benefits to user satisfaction and use, as proposed in the original model. In the following, we derive the hypotheses we tested in our study.

Previous studies suggest a positive relationship between an IS’s system quality and its use (e.g., DeLone and McLean, 1992; DeLone and McLean, 2003; Iivari, 2005). In addition, in the context of mobile business applications, it is likely that an unreliable system and/or one with poor interface design and navigation will be used less often (Koo et al., 2013). Thus, we hypothesize as follows:

H1a: System quality positively influences the use of a mobile business application. Similarly, several previous studies suggest a positive relationship between an IS’s system quality and its users’ satisfaction (e.g., Iivari, 2005; Kulkarni et al., 2007; Urbach et al., 2010). Again, it is likely that a poorly performing mobile business application and/or one with poor interface design and navigation will lead to lower user satisfaction than a high-quality system (Koo et al., 2013). Thus, we hypothesize as follows:

H1b: System quality positively influences user satisfaction with a mobile business application.

The D&M IS Success Model (1992; 2003) assumes that a higher information quality level leads to higher usage, which is also supported by related empirical studies (e.g., Hsieh and Wang, 2007; Rai et al., 2002). A mobile business application’s purpose is to provide users with useful, understandable, and timely information needed to perform tasks (e.g., Gebauer, 2008; Gebauer et al., 2010; Koo et al., 2013). If low-quality information is provided, users will likely use a system less often. Thus, we hypothesize as follows:

H2a: Information quality positively influences the use of a mobile business application.

Similarly, previous research suggests a positive relationship between information quality and user satisfaction (e.g., Iivari, 2005; Kulkarni et al., 2007). Moreover, in the context of mobile business applications, it is unlikely that a system that provides low-quality information will lead to satisfied users. Thus, we hypothesize as follows:

H2b: Information quality positively influences user satisfaction with a mobile business application.

A primary purpose of a mobile business application is to support and simplify organizational work processes. In line with the work of Urbach et al. (2010) and Chen et al. (2013), we suggest that process support quality is positively associated with the use of a mobile business application. Accordingly, a mobile business application that better supports work routines is likely to be used often. Thus, we hypothesize as follows:

H3a: Process quality positively influences the use of a mobile business application. Similarly, Urbach et al.’s (2010) results indicate a positive relationship between process support and user satisfaction. Again, we assume that a mobile business application that better supports work processes will lead to higher user satisfaction. Thus, we hypothesize the following:

H3b: Process quality positively influences user satisfaction with a mobile business application.

The updated D&M IS Success Model (2003) assumes a positive relationship between service quality and use, which is also supported by related empirical studies (Petter et al., 2008). In a business context, users are dependent on the mobile application for their daily work, and technical support in case of system problems or breakdowns is critical to its deployment (Chatterjee et al., 2009). Thus, we hypothesize as follows:

H4a: Service quality positively influences the use of a mobile business application. Similarly, previous research suggests a positive relationship between service quality and user satisfaction (e.g., Halawi et al., 2007). In addition, in the context of mobile business applications, it is likely that a more responsive and more competent service will lead to higher user satisfaction. Thus, we hypothesize as follows:

H4b: Service quality positively influences user satisfaction with a mobile business application.

Previous studies assume a positive impact of use on user satisfaction (e.g., DeLone and McLean, 2003; Iivari, 2005; Urbach et al., 2010). Accordingly, in the context of mobile business applications, we suggest that increasingly better usage experience involving a successively deeper embedding of the system into users’ work routines will lead to higher user satisfaction. Thus, we hypothesize the following:

H5a: Use positively influences user satisfaction with a mobile business application. Similarly, previous work also suggests an impact of user satisfaction on use (e.g., DeLone and McLean, 2003; Iivari, 2005; Urbach et al., 2010). Also, in the context of mobile business applications, users with high user satisfaction will use the system more often than users who do not like to use it. Thus, we hypothesize the following:

H5b: User satisfaction positively influences use of a mobile business application. The updated D&M IS Success Model (2003) suggests a positive influence of use on the net benefits of using an IS, which is also supported by related empirical studies (Petter et al.,

2008). In our context, the rationale behind introducing mobile business applications is to support users in accomplishing their tasks and, thus, to achieve their professional goals. With our focus on the benefits achieved by individual users, we assume that higher usage leads to a higher goal attainment. Thus, we hypothesize as follows: H6: Use positively influences the individual benefits from using a mobile business application.

Similarly, previous research suggests a positive relationship between user satisfaction and individual benefits (DeLone and McLean, 1992; Iivari, 2005; Urbach et al., 2010). We assume that employees with high-user satisfaction will more likely benefit from using the system than users who do not like to use the mobile application. Thus, we hypothesize as follows:

H7: User satisfaction positively influences the individual benefits from using a mobile business application.

The resulting adapted D&M IS Success Model is displayed in Fig. 2. Each arrow represents a hypothesized positive relationship between two success dimensions we will test. Since we were interested in understanding end users’ satisfaction and their acceptance of mobile business applications, we focus on individual performance impacts rather than organizational performance impacts as the final dependent variable of interest. Measuring the organizational impacts of individual IS initiatives has proven difficult (e.g., Gelderman, 1998; Goodhue and Thompson, 1995). Thus, we do not include organizational impact in our model, although in our view this impact is generally an important part of a comprehensive analysis.

![](/api/attachments/GBJU6T52/fulltext/images/0c1048dfd9d8c59eed8dbd731c4d4f7f0ff1217d14c27c59120c73f58a1dcdbc.jpg)  
Figure 2. Adapted D&M IS Success Model

## 5.4 Construct Operationalization

Following various authors’ recommendations (e.g., Bharati and Chaudhury, 2004; DeLone and McLean, 2003; Kankanhalli et al., 2005), we used tested and proven measures, where available, for the operationalization of the success model’s constructs. Thus, we adapted items identified in previous studies and modified them for use in the mobile application context where required. To operationalize the individual benefit construct, we developed our items on the basis of the perceived usefulness measure proposed by Davis (1989) – one of the most common impact measures at the individual level (Petter et al., 2008). From the resulting pool of items, we had to select a limited number of items for our study, because the case organization did not want its employees to spend too much time on the questionnaire. Table 4 shows the items we finally used and measured on a seven-point Likert-type scale (1 = strongly disagree and 7 = strongly agree). We pretested after combining the items in a draft survey instrument. To ensure questionnaire design quality and presentation quality, we discussed the draft within our research team and modified it according to their feedback. Finally, we put the draft questionnaire through a trial run with a group of eight experts in

mobile service and maintenance processes. Based on their feedback, we finalized the questionnaire’s appearance and instructions (Appendix A).

<table><tr><td>Construct</td><td>Items</td><td>No. of items</td><td>References</td></tr><tr><td>System quality</td><td>Navigation, searchability, structure, usability, and functionality</td><td>5</td><td>Items adapted from Ahn et al. (2004), Lee et al. (2010), McKinney et al. (2002)</td></tr><tr><td>Information quality</td><td>Information usefulness, understandability, and timeliness</td><td>3</td><td>Items adapted from Lee et al. (2010), Lin and Lee (2006), McKinney et al. (2002), Yang et al. (2005)</td></tr><tr><td>Process quality</td><td>Efficiency, reliability, comprehensibility, and traceability</td><td>4</td><td>New items derived from Puschmann and Alt (2005), Martini et al. (2009)</td></tr><tr><td>Service quality</td><td>Responsiveness, empathy, reliability, and competence</td><td>4</td><td>Items adapted from Chang and King (2005), Pitt et al. (1995), Urbach et al. (2010)</td></tr><tr><td>Use</td><td>Extent of using different features</td><td>8</td><td>New items derived from Almutairi and Subramanian (2005), Chatterjee et al. (2009)</td></tr><tr><td>User satisfaction</td><td>Adequacy, efficiency, effectiveness, and overall satisfaction</td><td>4</td><td>Items adapted from Chatterjee et al. (2009), Seddon and Kiew (1994)</td></tr><tr><td>Individual benefits</td><td>Helpfulness, importance, and overall usefulness</td><td>3</td><td>New items derived from Davis (1989)</td></tr><tr><td>Management support</td><td>Encouragement and leadership support</td><td>2</td><td>Items adapted from Urbach et al. (2010)</td></tr></table>

Table 4. Construct Operationalizations

## 6 Ex Post Evaluation

## 6.1 Data Collection

The questionnaire was distributed to 900 DEKRA employees who had used the mobile application at least once during the last month. The participants were invited by e-mail and directed to the online survey (in December 2009). To ensure independent and reliable results, no incentives were offered for participation. After a 17-day survey period, we closed the online survey. In total, 374 DPC users completed the online survey, a response rate of 41.6%, which is considerably above the minimum of 20% recommended by Malhotra and Grover (1998). The average time participants took to work through the 42 questions (including eight demographic questions) was 15 min – the same as the time suggested in our invitation e-mail. After eliminating 57 incomplete responses, 317 fully completed survey responses remained for data analysis. The respondents’ demographic characteristics are shown in Appendix B. Given the perceptual assessment of both dependent and independent variables in our model, common method bias might have potentially affected our results’ validity. To control for this bias, we used Harman’s single-factor test, which is considered the most widespread approach (Malhotra et al., 2006). Thus, all the items we used to operationalize our constructs were subject to an exploratory factor analysis. We examined the unrotated factor solution to determine the number of factors necessary to account for the variance in the items. The factor analysis revealed 14 factors with an eigenvalue >1.0 that account for 64.8% of the total variance. Further, because the first factor accounts for only 26.7% of the variance, we concluded that neither “(1) a single factor emerges from unrotated factor solutions” nor “(2) a first factor explains the majority of the variance in the variables” (Malhotra et al., 2006, p. 1867). Thus, we concluded that common method bias did not significantly affect our results.

## 6.2 Analysis and Results

For the empirical analysis, we used the partial least square (PLS) approach (Chin, 1998; Wold, 1985) using the data from the survey. Compared with covariance-based approaches, PLS is advantageous when the research model is relatively complex with a large number of indicators, the measures are not well established, and/or the relationships between the indicators and latent variables must be modeled in different modes, that is, formative and reflective measures (Chin and Newsted, 1999; Fornell and Bookstein, 1982). Furthermore, the PLS approach is best suited for management-oriented problems with decision relevance that focus on prediction (Fornell and Bookstein, 1982; Huber et al., 2007). We used the software package SmartPLS (Ringle et al., 2005) for the statistical calculations.

## 6.2.1 Assessment of Measurement Models

We mainly used reflective indicators for the operationalization of the model’s constructs. Only use was measured formatively. Following the validation guidelines of Straub et al. (2004) and Lewis et al. (2005), we tested the reflective measurement models for internal consistency reliability, indicator reliability, convergent validity, and discriminant validity by applying standard decision rules. We assessed internal consistency reliability with Cronbach’s alpha (CA; Cronbach, 1951) and composite reliability (CR; Werts et al., 1974). The CA and CR values of most constructs in our model are (Table 5) above the generally recommended minimum of .700 (Nunnally and Bernstein, 1994). Only the CA value of management support is slightly below this threshold. However, as CR is recommended as the preferred measure (Chin, 1998), we kept the construct in our model and did not alter its operationalization. According to Straub et al. (2004, p. 401), values > .950 “are more suspect than those in the middle alpha ranges,” thus indicating potential common method bias. For our model, all values are below this threshold.

We determined indicator reliability, using a confirmatory factor analysis (CFA) within PLS. Items with a loading < .700 are usually considered unreliable (Chin, 1998). In our model, all loadings are above this threshold with significance at the .001 level. We further tested for convergent validity, with the average variance extracted (AVE), a commonly applied criterion proposed by Fornell and Larcker (1981). As indicated in Table 5, all the reflective constructs in our model have AVE indicators > .500, demonstrating that all constructs possess adequate reliability (Segars, 1997).

<table><tr><td>Construct</td><td>CA</td><td>CR</td><td>AVE</td></tr><tr><td>System quality</td><td>.894</td><td>.919</td><td>.654</td></tr><tr><td>Information quality</td><td>.849</td><td>.909</td><td>.771</td></tr><tr><td>Process quality</td><td>.806</td><td>.871</td><td>.628</td></tr><tr><td>Service quality</td><td>.866</td><td>.909</td><td>.714</td></tr><tr><td>Management support</td><td>.650</td><td>.851</td><td>.740</td></tr><tr><td>User satisfaction</td><td>.892</td><td>.926</td><td>.758</td></tr><tr><td>Individual benefits</td><td>.851</td><td>.910</td><td>.771</td></tr></table>

Table 5. Internal Consistency and Convergent Validity

To assess the constructs’ discriminant validity, we compared the items’ cross-loadings (Appendix C). Each indicator’s loading is higher for its construct than for any of the others. Furthermore, each of the constructs loads highest with its assigned items. Thus, we infer that the different constructs’ indicators are not interchangeable (Chin, 1998). Furthermore, the square root of each construct’s AVE is greater than their interconstruct correlations (Table 6). This result provides more evidence of all the constructs being sufficiently dissimilar (Fornell and Larcker, 1981). Finally, we calculated the variance inflation factors (VIFs) for all latent variables to get an indication of how much of a latent variable’s variance is explained by the other models’ variables. Since all VIF values are fairly low (< 3.300), we assumed that multicollinearity among the independent variables is not an issue.

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>1. Management support</td><td>.860</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. Individual benefits</td><td>.078</td><td>.878</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3. Information quality</td><td>.164</td><td>.416</td><td>.878</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4. Process quality</td><td>.041</td><td>.677</td><td>.536</td><td>.792</td><td></td><td></td><td></td><td></td></tr><tr><td>5. Service quality</td><td>.156</td><td>.264</td><td>.276</td><td>.331</td><td>.845</td><td></td><td></td><td></td></tr><tr><td>6. System quality</td><td>.056</td><td>.614</td><td>.464</td><td>.721</td><td>.245</td><td>.809</td><td></td><td></td></tr><tr><td>7. Use</td><td>.082</td><td>.694</td><td>.376</td><td>.658</td><td>.275</td><td>.548</td><td>for m.</td><td></td></tr><tr><td>8. User Satisfaction</td><td>.081</td><td>.813</td><td>.414</td><td>.743</td><td>.278</td><td>.686</td><td>.741</td><td>.870</td></tr><tr><td colspan="9">Note: diagonal elements represent the square root of the AVE.</td></tr></table>

Table 6. Interconstruct Correlations

We measured the construct use with a formative measurement model. All items show weights higher than .100, with significance at the .050 level, which demonstrates a sufficient reliability level (Lohmöller, 1989). We also checked the measurement model for multicollinearity by means of VIFs. As the value is below the threshold of 10 (Diamantopoulos and Siguaw, 2006; Gujarati, 2003), we conclude that multicollinearity among the items is not an issue in our study. Finally, we followed the suggestion by MacKenzie et al. (2005) to also test discriminant validity for the formative constructs. In our study, correlations between use and all other constructs of < .700 (Table 6) indicate good discriminant validity (Bruhn et al., 2008).

## 6.2.2 Assessment of the Structural Model

Once we had validated the measurement model, we analyzed the structural model and tested the hypothesized relationships between the constructs (Fig. 3). Becuase our success model includes a mutual influence between use and user satisfaction that cannot be simultaneously tested, we tested two different models, as proposed by Iivari (2005). Model 1 assumes that the influence is from use to user satisfaction, while model 2 works from user satisfaction to use. We used bootstrapping with 1000 resamples to determine the paths’ significance within the structural models.

![](/api/attachments/GBJU6T52/fulltext/images/db003f82434637faca9cd3eeb714de5e7a4293c0867b098a73b89e142ea042f1.jpg)

Notes: <sup>\*</sup>significant at \*\* \*\*\* $p < . 0 5 0 ;$ <sup>\*</sup>significant at $p < . 0 1 0 ;$ significant at $p < . 0 0 1$

## Figure 3. Results of the Structural Analysis

The structural models’ quality was evaluated on squared multiple correlations $( R ^ { 2 } )$ and crossvalidated redundancy measures $( Q ^ { 2 } )$ . Overall, both models explain a considerable portion of the latent variables’ variance. More than half of the variance of the endogenous dependent variables user satisfaction $( R ^ { 2 } = . 6 9 4$ in model 1 and $R ^ { 2 } = . 6 0 2$ in model 2) and individual benefits $( R ^ { 2 } = . 6 8 0$ in both models) is explained, which can be considered substantial. The use variable’s variance $( R ^ { 2 } = . 4 5 2$ in model 1 and $R ^ { 2 } = . 5 7 8$ in model 2) is explained to a slightly lesser extent, but is still at a moderate level (Chin, 1998). We tested the model’s predictive relevance with a nonparametric Stone–Geisser test (Geisser, 1975; Stone, 1974). According to this test, positive $Q ^ { 2 }$ values confirm the model’s predictive relevance with respect to particular construct. Furthermore, the better the tested model’s predictive relevance, the greater $Q ^ { 2 }$ value becomes (Fornell and Cha, 1994). The test results show positive values for all endogenous latent variables.

Having established the measurement’s validity and having confirmed that the structural model’s quality is acceptable, we evaluated the structural paths to test the hypothesized links. These are considered to be supported by the data, since the corresponding path coefficients had the predicted sign and were significant at least at a p-value <.050 (Table 7).

<table><tr><td colspan="2">Hypothesized relationship</td><td> $\beta (model 1)$ </td><td>Support</td><td> $\beta (model 2)$ </td><td>Support</td></tr><tr><td>H1a</td><td>System quality  $\rightarrow$  Use</td><td>.151**</td><td>Yes</td><td>-.029</td><td>No</td></tr><tr><td>H1b</td><td>System quality  $\rightarrow$  User satisfaction</td><td>.252***</td><td>Yes</td><td>.314***</td><td>Yes</td></tr><tr><td>H2a</td><td>Information quality  $\rightarrow$  Use</td><td>-.002</td><td>No</td><td>.014</td><td>No</td></tr><tr><td>H2b</td><td>Information quality  $\rightarrow$  User satisfaction</td><td>-.025</td><td>No</td><td>-.026</td><td>No</td></tr><tr><td>H3a</td><td>Process quality  $\rightarrow$  Use</td><td>.533***</td><td>Yes</td><td>.237***</td><td>Yes</td></tr><tr><td>H3b</td><td>Process quality  $\rightarrow$  User satisfaction</td><td>.300***</td><td>Yes</td><td>.518***</td><td>Yes</td></tr><tr><td>H4a</td><td>Service quality  $\rightarrow$  Use</td><td>.053</td><td>No</td><td>.039</td><td>No</td></tr><tr><td>H4b</td><td>Service quality  $\rightarrow$  User satisfaction</td><td>.009</td><td>No</td><td>.030</td><td>No</td></tr><tr><td>H5a</td><td>Use  $\rightarrow$  User satisfaction</td><td>.409***</td><td>Yes</td><td>n/a</td><td>n/a</td></tr><tr><td>H5b</td><td>User satisfaction  $\rightarrow$  Use</td><td>n/a</td><td>n/a</td><td>.567***</td><td>Yes</td></tr><tr><td>H6</td><td>Use → Individual benefits</td><td>.201***</td><td>Yes</td><td>.203***</td><td>Yes</td></tr><tr><td>H7</td><td>User satisfaction → Individual benefits</td><td>.665***</td><td>Yes</td><td>.663***</td><td>Yes</td></tr><tr><td colspan="6">Path-β: * significant at p&lt;.050; ** significant at p&lt;.010; *** significant at p&lt;.001.</td></tr></table>

Table 7. Results of Hypotheses Tests

The empirical results of our study revealed mixed support for the previously formulated hypotheses. The paths from system quality to use and user satisfaction, from process quality to use and user satisfaction, from use to user satisfaction, and from use and user satisfaction to individual benefits emerged as hypothesized. However, the links from information quality to use and user satisfaction, and from service quality to use and user satisfaction, are not supported. The control variable management support had no significant influence on our results, either as an additional antecedent or as a mediator or moderator. Thus, we concluded that the leadership team’s encouragement of and support for the mobile application’s usage played no intervening role in our study.

To find out whether the independent latent variables in our models have a substantial impact on the dependent variables, we calculated their effect sizes on both use and user satisfaction by means of Cohen’s $f ^ { 2 }$ (Cohen, 1988; Table 8). Consistent with the hypotheses test results, the effect sizes indicate that process quality and, to a lesser extent, system quality show a substantial effect, while the effect sizes of service quality and information quality are negligible.

<table><tr><td></td><td colspan="2">Effect $^{1}$  ( $f^{2}$ ) on use</td><td colspan="2">Effect $^{1}$  ( $f^{2}$ ) on user satisfaction</td></tr><tr><td>Construct</td><td>Model 1</td><td>Model 2</td><td>Model 1</td><td>Model 2</td></tr><tr><td>System quality</td><td>.020</td><td>.002</td><td>.098</td><td>.118</td></tr><tr><td>Service quality</td><td>.004</td><td>.002</td><td>.000</td><td>.003</td></tr><tr><td>Process quality</td><td>.210</td><td>.043</td><td>.105</td><td>.279</td></tr><tr><td>Information quality</td><td>.000</td><td>.000</td><td>.003</td><td>.003</td></tr></table>

<sup>1</sup>Values for f<sup>2</sup> between .020 and .150, .150 and .350, and exceeding .350 indicate that the exogenous variable has a small, medium, or large effect, respectively, on an endogenous latent variable (Chin, 1998).

Table 8. Effect Sizes

## 7 Implications for Iterative Mobile Business Application Design

## 7.1 Performance-based Model Analysis

By means of performance-based model analysis, we were able to analyze the impacts of the model’s independent variables and thereby derive the priorities for mobile application design. For this purpose, we contrasted the corresponding latent variables’ index values with their total effects on the model’s final dependent variable, that is, individual benefits (Table 9). This approach has already been used by other authors (e.g., Fornell et al., 1996; Martensen and Gronholdt, 2003; Urbach et al., 2011) to improve the interpretability of path modeling results. We estimated the latent variables’ index values by means of the weighted average of point scale. Thus, they can be considered as performance measures for the respective constructs. The total effects are the independent latent variable’s direct and indirect effects on the dependent latent variable.

<table><tr><td>Construct</td><td>Index values</td><td>Standard deviation</td><td>Total effects on individual benefits2</td></tr><tr><td>Information quality</td><td>77.840</td><td>17.290</td><td>- / -</td></tr><tr><td>Process quality</td><td>60.111</td><td>17.901</td><td>.451 / .451</td></tr><tr><td>Service quality</td><td>75.592</td><td>14.917</td><td>- / -</td></tr><tr><td>System quality</td><td>60.327</td><td>20.433</td><td>.239 / .239</td></tr></table>

<sup>2</sup> Total effects were calculated for both model 1 and model 2.

## Table 9. Index Values and Total Effects

This performance-based model analysis demonstrates that process quality had a relatively high and system quality a moderate total effect on the individual benefit construct. At the same time, both constructs had significant lower index values compared with the remaining two latent constructs, that is, information and service quality, which did not significantly influence the dependent variables.

To derive specific recommendations for the design of mobile business applications, we combined the estimated total effects and the performance indexes of the dependent variables into an effect–performance matrix. Since such a data presentation is appealing from a management perspective and can be useful in priority setting and strategy development, it is also called a priority map (Martensen and Gronholdt, 2003). Figure 4 shows the priority map for the construct individual benefits. The lines separating the cells represent the average total effects and index values. Of the four resulting cells, the lower-right one is the area with the greatest opportunity. Although these constructs’ effects are relatively strong, there is sufficient room for performance improvement. Accordingly, we conclude that future design improvements should address both process quality and system quality in order to efficiently increase the individual benefits for the mobile application users.

Performance

![](/api/attachments/GBJU6T52/fulltext/images/35076d30d8ab42eea57ac2655a571ce24286308ea68eb3eeeed8c9195c2032d6.jpg)  
Figure 4. Priority Map for Individual Benefits

## 7.2 Interpretation and Recommendations for Mobile Application Design

First, the empirical results confirm that the mobile business application can generally be considered successful from the perspectives of end users, while leaving some room for improvement (index value of individual impact: 64,955). They also underpin that some of the initial design goals were met by the DEKRA Pocket PC. DEKRA’s emphasis on providing an easy-to-use and low-support application (Section 3.3) has been found to be successful, as confirmed by the high index values for service quality and the non-significant impact of service quality. In case of problems, users follow a simple procedure to initialize the device, which results in a very low number of service incidents. At the same time, users are fairly satisfied with the resolution of the remaining problems by the DPC support team, as indicated by the high index values for service quality.

Concerning mobile application design, the empirical data underpins system quality’s relevance from the perspectives of end users and points at potential for improvement concerning the DPC’s navigation and usability. DEKRA finds that system quality is largely influenced by its initial mobile technology platform choice. A particularity of mobile

#

applications is that the hardware platform defines the operating system and imposes significant constraints on the application design and its ease of use, particularly concerning navigation, searchability, or usability.

Interestingly, process quality was very relevant to DEKRA employees, while information quality had non-significant impacts on use and user satisfaction. Our interpretation is as follows: in service and maintenance processes, mobile business applications’ use is mostly embedded in the operational business processes. Thus, the productivity and quality improvements that technicians realize in their daily work routines by using the mobile device are the main drivers of use and user satisfaction. The quality of vehicle-specific information without reference to the process plays only a minor role. PTI inspectors do not seem to access vehicle information on a mobile device during vehicle inspection, but rather from their stationary work environments. However, when the necessary information is provided in the right context, it is appreciated by users, as indicated by the fairly high index value for information quality.

Table 10 summarizes DEKRA’s interpretation of the empirical findings, along with the implications for mobile application design. The performance-based analysis suggests that future mobile application design should address both process quality and system quality, while service quality and information quality will have little or no effect on individual benefits. When using these empirical findings as input for incremental development (the building phase), DEKRA realized that it needed to address them in two different ways and at different development speeds. Process quality was addressed in typical release cycles by extending the functionality of existing applications or adding further applications, while system quality could only be improved when migrating to a new mobile platform. This implies decomposing the incremental development and the iterative development of mobile business applications (Section 4) into two streams:

Mobile application development (functional extensions): in the next releases, DEKRA prioritized improving process quality by extending functionality. It also added further applications, as well as information and control functions for test equipment. Today, > 4000 employees are equipped with the DEKRA DPC.

Migration to a new mobile platform: significant improvements in system quality are only possible with the migration to the next technology generation, comprising Android or iOS-based mobile touch devices, which are not only easier to use but also provide more options for visualization and larger screens. DEKRA – like many companies – has faced fundamental changes of mobile devices and their operating systems in the market. As production was ceased on the HP IPAQ 214 and Microsoft took its mobile operating system Windows Mobile 6.5 off the market, DEKRA selected Samsung Galaxy S5, an Androidbased mobile touch device as mobile platform for the DEKRA Pocket PC Version 2.

<table><tr><td>Construct</td><td>Interpretation for DEKRA</td><td>Implications for iterative mobile application development (artifact building)</td></tr><tr><td>System quality</td><td>Moderate total effect on individual benefits: potential for improving the DPC's navigation and usability.The current mobile technology platform constrains mobile application design;improvements can only be addressed when migrating to the new platform.</td><td>Largely influenced by the mobile technology platform choice (device, hardware platform, and operating system).Significant improvements in system quality require migration to a new technology platform; system quality should be considered as evaluation criterion when selecting mobile platforms.</td></tr><tr><td>Information quality</td><td>High index value, but no effect on individual benefits.Employees do not seem to access information without reference to the process on a mobile device, but rather from a stationary work environment.</td><td>When setting priorities for mobile application development, pure information access and data viewing applications should be deprioritized.</td></tr><tr><td>Process quality</td><td>High total effect on individual benefits.Process-supporting functionalities are most important for employees, since mobile business applications use is embedded in work routines.</td><td>When setting priorities for mobile application development, the focus should be on extending process support within existing applications or adding further applications that support employees in their daily operations.Future releases should focus on extending process support in de facto work environments: mobile application design needs to consider contextuality and situatedness in the work routine.</td></tr><tr><td>Service quality</td><td>High index value, but no effect on individual benefits.Confirms that the DPC is already an easy-to-use application resulting in very few technical service incidents.</td><td>Mobile applications are fairly easy to use and users are experienced in their use.Service provided by support personnel is only required in emergency situations.The focus should be on low-support applications.</td></tr></table>

Table 10. Interpretation and Design Recommendations

## 7.3 Discussion and Generalization

The empirical results are aligned with the existing literature on mobile business applications (Gebauer et al., 2010) that emphasizes system quality’s relevance for mobile applications success. System quality has a direct positive influence on user satisfaction, but only an indirect influence on use. A key finding from our analysis is that process support positively influences use and user satisfaction; thus, it is the most important determinant of the

#

individual benefits of using mobile applications in service and maintenance scenarios, while information quality has no significant impact. By identifying process support as the most important determinant of individual benefits, our findings emphasize the mobile business application’s unique value factors, such as ubiquitous use, instant connectivity, and assistance in completing complex tasks. The empirical results underpin the importance of contextuality in mobile applications’ design (Section 2.1) to deal with the situatedness in work routines and de facto work environments. With its emphasis on process quality and the nonsignificant impact of information quality, our study reveals specific characteristics of mobile business applications compared with other mobile service types. Our findings contradict many studies that use the D&M IS Success Model (Petter et al., 2008) and show a strong correlation between information quality and user satisfaction, including the study by Lee et al. (2010), which identifies information quality as a significant motivator of (consumer-oriented) mobile data services. Similar to the studies on employee portal success by Urbach et al. (2010), service quality – which comprises the responsiveness, reliability, and competence of end user support – has a positive influence on neither use nor user satisfaction. This may be explained by the fact that contemporary Internet and mobile applications are fairly easy to use and that users are experienced in their use.

Based on the study findings, we can derive recommendations for the design of mobile business applications (Table 10). The design should primarily focus on system quality and specific process support. To improve system quality, companies should concentrate on aspects such as accessibility, interface design, navigation, and usability, which are highly dependent on the mobile platform choice (the device, its hardware platform, and its operating system). Concerning the functionality provided by mobile business applications, the results suggest that development efforts should target process quality and should provide specific functionalities that support employees in performing their daily tasks in their work

environments. Information quality and service quality have less influence on the individual benefits of an application’s use. Service quality can be deprioritized, since the latest generations of mobile devices are intuitive to use and allow one to build low-support applications.

## 8 Summary and Conclusion

To summarize, our study results comprise a systematic approach to leverage ex post evaluations from the perspectives of end users for the iterative design of mobile business applications, including (1) a theoretically grounded evaluation model based on the adapted D&M IS Success Model, (2) an empirical study as ex post evaluation of a mobile business application from the perspectives of actual users, and (3) a performance-based analysis of the empirical results to derive priorities and recommendations for future design iterations. By considering mobile business applications, our research complements existing empirical studies, which mostly focus on consumer-oriented mobile services’ success and adoption, and reveals specific success factors from the perspectives of professional end users. Our results go beyond the existing body of research, in that we consider mobile business applications as innovative IT artifacts that should be improved in iterative design cycles. With the ex post evaluation of their utility for end users and the performance-based analysis, we suggest theoretically grounded techniques to better link the building and evaluation phases in the iterative design of mobile business applications.

We contribute to both theory and practice. From a practical perspective, our framework and empirical study has helped DEKRA to analyze end-user satisfaction with the DPC and to improve its mobile business application design. Furthermore, the empirical results reveal that system quality and process quality are the most important levers of this mobile business application’s success, and thereby provide guidance for the mobile application’s future

#

development. Although the results of the performance-based model analysis provide specific advice to our case company, the structural analysis results provide generalizable indications concerning the factors that contribute to successful mobile business application design, which might well also be relevant for other companies.

Our contribution to theory is the development and empirical testing of a modified version of the D&M IS Success Model for mobile business applications and performance-based analysis. Although the IS success model is an established theoretical framework that has already been used to explain the success of various IS types, our study is among the very first to empirically validate a comprehensive success model for mobile business applications. Thus, we address the various authors’ recommendations (e.g., DeLone and McLean, 2003; Iivari, 2005) to extend and further empirically test the IS success model in different settings and system contexts than in previous studies. Compared with the updated D&M IS Success Model, our extensions and empirical results underpin process quality’s impacts on individual benefits in the context of mobile business applications, emphasize the unique characteristics of mobile business applications, and identify their situatedness in the business process as a particular form of contextuality (Table 1) as an important success factor in their design. Our empirical results thereby draw the attention of researchers to the embedding of mobile applications in work routines. They confirm that recent studies’ insights are related to mobile technology-mediated work emphasizing the congruency between mobile applications and activity systems (Karaniasos and Allen, 2014) and the affordances that mobile applications bring to individual routines (Boillat et al. 2015).

Our study further contributes to the existing body of research by proposing a novel approach to support the iterative design of mobile applications (Fig. 1) that relies on a rigorous ex post evaluation of the design outcomes (i.e., the artifact in use). The suggested theoretically grounded techniques build on the D&M IS Success Model and allowed us to better link the

#

building and evaluation phases in the iterative design of mobile business applications<sup>.</sup> By integrating the D&M IS Success Model in the ex post evaluation of an IT artifact, we also contributed to linking two allegedly separate paradigms, design science, and behavioral science. Thus, we sought to answer the call by Hevner and March (2003, p. 111) to “combine the creativity and precision of design science with the empiricism and discipline of behavioral science.” Thus, we encourage researchers to follow this path and to investigate the complementary of the design-oriented and behavioristic research paradigms (e.g., Buhl et al., 2012; Junglas et al., 2011) in research on mobile business applications.

Our study is limited in that the assessment is based on individual perceptions of business users. To improve future research, we suggest integrating additional factual data to avoid subjective estimation variance. The use construct is especially appropriate for measurement by automatically collecting data, for instance, relating to the frequencies of use and intensities of use of mobile business applications. A further limitation relates to individual benefits, which we intentionally chose as the final dependent variable. Although individual impacts are an important indicator of the application’s success, particularly for mobile business applications, future research might also incorporate organizational impacts for broader insight into the net benefits related to the use of mobile business applications. Finally, we used Harman’s single-factor test only to control for the common method bias, which is considered a limited approach (Podsakoff et al., 2003). As more advanced tests require the collection of a marker variable, which we did not include in our survey, we cannot completely rule out that a common method bias affected our findings’ validity.

From a practical perspective, mobile business application design strongly depends on the available mobile technology platforms, and the fundamental changes introduced by Android and iOS-based mobile touch devices have forced many companies to migrate their mobile applications. The understanding of a mobile business application’s utility and success factors from end users’ perspectives is particularly useful for coping with ongoing innovations in mobile technology and for justifying application development priorities as well as migration paths to new technology platforms. Although we were only able to show a single iteration of annually) as input for the release and migration planning of mobile business applications.

## Appendix A

All items were measured using a seven-point Likert-type scale (1 = very low and 7 = very high). The reliability indicator Cronbach’s alpha is reported for each of the constructs that were operationalized reflectively.

## A.1 System quality (Cronbach’s alpha = .894)

Please assess the system quality of the DEKRA Pocket Computer (DPC) for the general inspection (GI). SYS\_QUAL1: My DPC allows me to easily navigate through the GI application. SYS\_QUAL2: My DPC enables me to easily find the information needed for the GI. SYS\_QUAL3: The GI application on my DPC is well structured. SYS\_QUAL4: The GI application on my DPC is easy to use. SYS\_QUAL5: The GI application on my DPC offers the functionalities needed for the GI.

## A.2 Information quality (Cronbach’s alpha = .849)

Please assess the quality of the information provided by the DEKRA Pocket Computer (DPC) for the general inspection (GI).

INF\_QUAL1: The information provided by my DPC is useful.

INF\_QUAL2: The information provided by my DPC is understandable. INF\_QUAL3: The information provided by my DPC is up to date.

## A.3 Process quality (Cronbach’s alpha = .806)

Please assess the quality of the process support provided by the DEKRA Pocket Computer (DPC) for the general inspection (GI).

PRO\_QUAL1: My DPC efficiently supports the GI processes.

PRO\_QUAL2: My DPC reliably supports the GI processes.

PRO\_QUAL3: My DPC supports the GI processes in a way that allows one to understand them.

PRO\_QUAL4: My DPC supports the GI processes in a way that allows one to trace them.

## A.4 Service quality (Cronbach’s alpha = .866)

Please assess the service quality of the personnel responsible for supporting your DEKRA Pocket Computer (DPC).

SER\_QUAL1: The service personnel are always highly willing to help whenever I need support with the DPC.

SER\_QUAL2: The service personnel provide personal attention when I experience problems with the DPC.

SER\_QUAL3: The service personnel provide services related to the DPC at the promised time.

SER\_QUAL4: The service personnel have sufficient knowledge to answer my questions concerning the DPC.

A.5 Use

Please indicate the extent to which you use the DEKRA Pocket Computer (DPC) to perform the following tasks.

USE1: Using the DPC for the general inspection (GI) in general.

USE2: Using the DPC for the GI of vehicle that obligatory need vehicle-specific information (VSI).

USE3: Using the DPC to capture defects in the GI.

USE4: Using the DPC for the GI without setting up a vehicle at the mobile engineer terminal (MET) before.

USE5: Using the DPC at the stationary engineer terminal (SET).

USE6: Using the DPC at the MIT.

USE7: Using the DPC for vehicle identification number (VIN).

USE8: Using the DPC for the inspection-specific notices of the system data application.

## A.6 User satisfaction (Cronbach’s alpha = .892)

Please indicate your satisfaction with your DEKRA Pocket Computer (DPC).

USE\_SAT1: How adequately does the DPC support your tasks related to the GI.

USE\_SAT2: How efficient is your work with the DPC?

USE\_SAT3: How effective is your work with the DPC?

USE\_SAT4: How satisfied are you with the DPC on the whole?

## A.7 Individual benefits (Cronbach’s alpha = .851)

Please assess the individual benefits derived from using your DPC.

IND\_BEN1: The DPC is helpful to accomplish my tasks.

IND\_BEN2: The DPC is useful for my job.

IND\_BEN3: I would not want to discontinue my DPC use.

## A.8 Management support (Cronbach’s alpha = .650)

Please assess the organizational culture concerning using the DPC.

MAN\_SUP1: My supervisor actively encourages me to use the DPC.

MAN\_SUP2: My organization’s leadership explicitly supports the DPC’s use.

Appendix B

<table><tr><td colspan="2">Age (years)</td><td colspan="2">Gender</td><td colspan="2">Computer skills</td></tr><tr><td>0–25</td><td>2 (0.6%)</td><td>Male</td><td>317 (100%)</td><td>Very good</td><td>46 (14.5%)</td></tr><tr><td>25–30</td><td>39 (12.3%)</td><td>Female</td><td>0 (0.0%)</td><td>Good</td><td>142 (44.8%)</td></tr><tr><td>30–35</td><td>40 (12.6%)</td><td></td><td></td><td>Sufficient</td><td>91 (28.7%)</td></tr><tr><td>35–40</td><td>48 (15.1%)</td><td></td><td></td><td>Medium</td><td>33 (10.4%)</td></tr><tr><td>40–45</td><td>71 (22.4%)</td><td></td><td></td><td>Insufficient</td><td>4 (1.3%)</td></tr><tr><td>45–50</td><td>65 (20.5%)</td><td></td><td></td><td>Poor</td><td>1 (0.3%)</td></tr><tr><td>50–55</td><td>28 (8.8%)</td><td></td><td></td><td>Very poor</td><td>0 (0.0%)</td></tr><tr><td>55–60</td><td>22 (6.9%)</td><td></td><td></td><td></td><td></td></tr><tr><td>60–65</td><td>2 (0.6%)</td><td></td><td></td><td></td><td></td></tr></table>

Table 11. Respondents’ Demographic Characteristics

Appendix C

<table><tr><td>Items</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>MAN_SUP1</td><td>.869</td><td>.042</td><td>.162</td><td>.054</td><td>.160</td><td>.031</td><td>.069</td></tr><tr><td>MAN_SUP2</td><td>.852</td><td>.095</td><td>.119</td><td>.014</td><td>.108</td><td>.067</td><td>.071</td></tr><tr><td>IND_BEN1</td><td>.046</td><td>.908</td><td>.399</td><td>.636</td><td>.235</td><td>.586</td><td>.777</td></tr><tr><td>IND_BEN2</td><td>.117</td><td>.850</td><td>.328</td><td>.564</td><td>.214</td><td>.502</td><td>.653</td></tr><tr><td>IND_BEN3</td><td>.050</td><td>.875</td><td>.364</td><td>.578</td><td>.246</td><td>.524</td><td>.704</td></tr><tr><td>INF_QUAL1</td><td>.132</td><td>.404</td><td>.775</td><td>.461</td><td>.222</td><td>.446</td><td>.382</td></tr><tr><td>INF_QUAL2</td><td>.149</td><td>.336</td><td>.925</td><td>.469</td><td>.250</td><td>.377</td><td>.346</td></tr><tr><td>INF_QUAL3</td><td>.149</td><td>.336</td><td>.925</td><td>.469</td><td>.250</td><td>.377</td><td>.346</td></tr><tr><td>PRO_QUAL1</td><td>.066</td><td>.401</td><td>.506</td><td>.755</td><td>.319</td><td>.519</td><td>.433</td></tr><tr><td>PRO_QUAL2</td><td>-.015</td><td>.654</td><td>.317</td><td>.803</td><td>.226</td><td>.615</td><td>.718</td></tr><tr><td>PRO_QUAL3</td><td>.004</td><td>.563</td><td>.386</td><td>.805</td><td>.308</td><td>.516</td><td>.592</td></tr><tr><td>PRO_QUAL4</td><td>.096</td><td>.470</td><td>.546</td><td>.804</td><td>.221</td><td>.618</td><td>.548</td></tr><tr><td>SER_QUAL1</td><td>.188</td><td>.268</td><td>.292</td><td>.329</td><td>.907</td><td>.234</td><td>.265</td></tr><tr><td>SER_QUAL2</td><td>.060</td><td>.265</td><td>.208</td><td>.274</td><td>.829</td><td>.191</td><td>.263</td></tr><tr><td>SER_QUAL3</td><td>.136</td><td>.106</td><td>.164</td><td>.225</td><td>.744</td><td>.154</td><td>.161</td></tr><tr><td>SER_QUAL4</td><td>.140</td><td>.219</td><td>.245</td><td>.275</td><td>.891</td><td>.237</td><td>.233</td></tr><tr><td>SYS_QUAL1</td><td>.035</td><td>.492</td><td>.426</td><td>.627</td><td>.253</td><td>.810</td><td>.556</td></tr><tr><td>SYS_QUAL2</td><td>.030</td><td>.539</td><td>.429</td><td>.562</td><td>.203</td><td>.820</td><td>.584</td></tr><tr><td>SYS_QUAL3</td><td>.077</td><td>.458</td><td>.308</td><td>.565</td><td>.142</td><td>.773</td><td>.545</td></tr><tr><td>SYS_QUAL4</td><td>.093</td><td>.413</td><td>.334</td><td>.536</td><td>.159</td><td>.790</td><td>.477</td></tr><tr><td>SYS_QUAL5</td><td>.020</td><td>.525</td><td>.317</td><td>.639</td><td>.220</td><td>.836</td><td>.570</td></tr><tr><td>USE_SAT1</td><td>-.002</td><td>.718</td><td>.336</td><td>.673</td><td>.216</td><td>.633</td><td>.909</td></tr><tr><td>USE_SAT2</td><td>.086</td><td>.756</td><td>.403</td><td>.679</td><td>.238</td><td>.594</td><td>.896</td></tr><tr><td>USE_SAT3</td><td>.063</td><td>.752</td><td>.415</td><td>.668</td><td>.258</td><td>.625</td><td>.877</td></tr><tr><td>USE_SAT4</td><td>.148</td><td>.593</td><td>.275</td><td>.557</td><td>.261</td><td>.531</td><td>.794</td></tr></table>

Table 12. Cross-loadings of Reflectively Measured Constructs

## References

Ahn, T., Ryu, S. and Han, I. (2004). The Impact of the Online and Offline Features on the User Acceptance of Internet Shopping Malls. Electronic Commerce Research and Applications, 3, 405-420.

Ajzen, I. (1991). The Theory of Planned Behavior. Organizational Behavior and Human Decision Processes, 50 (2), 179-211.

Al-Jabri, I.M. and Sohail, M.S. (2012). Mobile Banking Adoption: Application of Diffusion of Innovation Theory. Journal of Electronic Commerce Research, 13 (4), 379-391.

Almutairi, H. and Subramanian, G.H. (2005). An Empirical Application of the Delone and Mclean Model in the Kuwaiti Private Sector. Journal of Computer Information Systems, 45 (3), 113-122.

Benou, P. and Vassilakis, C. (2010). The Conceptual Model of Context for Mobile Commerce Applications. Electronic Commerce Research, 10 (2), 139-165.

Bharati, P. and Chaudhury, A. (2004). An Empirical Investigation of Decision-Making Satisfaction in Web-Based Decision Support Systems. Decision Support Systems, 37 (2), 187- 197.

Boillat, T., Lienhard, K., Legner, C. (2015). Entering the World of Individual Routines: The Affordances of Mobile Applications. In Proceedings of the Thirty-Sixth International Conference on Information Systems (ICIS 2015), Fort Worth, USA.

Bouwman, H., Carlsson, C., Walden, P. and Molina-Castillo, F.J. (2009). Reconsidering the Actual and Future Use of Mobile Services. Information Systems & e-Business Management, (7), 301–317.

Bruhn, M., Georgi, D. and Hadwich, K. (2008). Customer Equity Management as Formative Second-Order Construct. Journal of Business Research, 61 (12), 1292-1301.

Buhl, H.U., Fridgen, G., Röglinger, M. and Müller, G. (2012). On Dinosaurs, Measurement Ideologists, Separatists, and Happy Souls Proposing and Justifying a Way to Make the Global Is/Bise Community Happy. Business & Information Systems Engineering, 4 (6), 307-315.

Chang, J.C.-J. and King, W.R. (2005). Measuring the Performance of Information Systems: A Functional Scorecard. Journal of Management Information Systems, 22 (1), 85-115.

Chatterjee, S., Chakraborty, S., Sarker, S., Sarker, S. and Lau, F.Y. (2009). Examining the Success Factors for Mobile Work in Healthcare: A Deductive Study. Decision Support Systems, 46, 620–633.

Chen, J.V., Chen, Y.-W. and Capistrano, E.P.S. (2013). Process Quality and Collaboration Quality on B2B E-Commerce. Industrial Management & Data Systems, 113 (6).

Chin, W.W. (1998). The Partial Least Squares Approach to Structural Equation Modeling, in: Modern Methods for Business Research, (G.A. Marcoulides ed.), Mahwah: Lawrence Erlbaum Associates, pp. 295-336.

Chin, W.W. and Newsted, P.R. (1999). Structural Equation Modeling Analysis with Small Samples Using Partial Least Squares, in: Statistical Strategies for Small Sample Research, (R. Hoyle ed.), Thousand Oaks, CA: Sage Publications, pp. 307-341.

Cohen, J. (1988). Statistical Power Analysis for the Behavioral Sciences. 2nd ed. Lawrence Erlbaum, Hillsdale, NJ.

Cronbach, L.J. (1951). Coefficient Alpha and the Internal Structure of Tests. Psychometrika, 16 (3), 297-334.

Davis, F.D. (1989). Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology. MIS Quarterly, 13 (3), 318-340.

DeLone, W.H. and McLean, E.R. (1992). Information Systems Success: The Quest for the Dependent Variable. Information Systems Research, 3 (1), 60-95.

DeLone, W.H. and McLean, E.R. (2003). The Delone and Mclean Model of Information Systems Success: A Ten-Year Update. Journal of Management Information Systems, 19 (4), 9-30.

Diamantopoulos, A. and Siguaw, J.A. (2006). Formative Versus Reflective Indicators in Organizational Measure Development: A Comparison and Empirical Illustration. British Journal of Management, 17 (4), 263-282.

Fellmann, M., Hucke, S., Breitschwerdt, R., Thomas, O., Blinn, N. and Schlicker, M. (2011). Informationssystemarchitekturen Zur Unterstützung Technischer Kundendienstleistungen, In Proceedings of the 10. Internationale Tagung Wirtschaftsinformatik, Zürich, Switzerland.

Fornell, C. and Bookstein, F.L. (1982). Two Structural Equation Models: Lisrel and Pls Applied to Consumer Exit-Voice Theory. Journal of Marketing Research, 19, 440-452.

Fornell, C. and Cha, J. (1994). Partial Least Squares, in: Advanced Methods of Marketing Research, (R.P. Bagozzi ed.), Cambridge: Blackwell, 52-78.

Fornell, C., Johnson, M.D., Anderson, E.W., Jaesung, C. and Bryant, B.E. (1996). The American Customer Satisfaction Index: Nature, Purpose, and Findings. Journal of Marketing, 60 (4), 7-18.

Fornell, C. and Larcker, D.F. (1981). Evaluating Structural Equation Models with Unobservable Variables and Measurement Error. Journal of Marketing Research, 18, 39-50. Gable, G., Sedera, D. and Chan, T. (2003). Enterprise Systems Success: A Measurement Model, In Proceedings of the 24th International Conference on Information Systems (ICIS 03), Seattle, Washington.

Gebauer, J. (2008). User Requirements of Mobile Technology: A Summary of Research Results. Information Knowledge Systems Management, 7 (1/2), 101-119.

Gebauer, J., Shaw, M.J. and Gribbins, M.L. (2010). Task-Technology Fit for Mobile Information Systems. Journal of Information Technology, 25 (3), 259-272.

Geisser, S. (1975). The Predictive Sample Reuse Method with Applications. Journal of the American Statistical Association, 70, 320-328.

Gelderman, M. (1998). The Relation between User Satisfaction, Usage of Information Systems and Performance. Information & Management, 34 (1), 11-18.

Goodhue, D.L. and Thompson, R.L. (1995). Task-Technology Fit and Individual Performance. MIS Quarterly, 19 (2), 213.

Gujarati, D.N. (2003). Basic Econometrics. McGraw-Hill, New York, NY.

Halawi, L.A., McCarthy, R.V. and Aronson, J.E. (2007). An Empirical Investigation of Knowledge Management Systems' Success. Journal of Computer Information Systems, 48 (2), 121-135.

Helfert, M.D., Brian; Ostrowski, Lukasz. (2012). The Case for Design Science Utility and Quality - Evaluation of Design Science Artifact with the Sustainable Ict Capability Maturity Framework. Systems, Signs & Actions, 6 (1), 46-66.

Herzberg, F., Mausner, B. and Snyderman, B. (1959). The Motivation to Work. Wiley, New York.

Hevner, A.R. and March, S.T. (2003). The Information Systems Research Cycle. Computer, 36 (1), 111-113.

Hevner, A.R., March, S.T., Park, J. and Ram, S. (2004). Design Science in Information Systems Research. MIS Quarterly, 28 (1), 75-105.

Hsieh, J.J.P.-A. and Wang, W. (2007). Explaining Employees' Extended Use of Complex Information Systems. European Journal of Information Systems 16 (3), 216-227.

Huber, F., Herrmann, A., Frederik, M., Vogel, J. and Vollhardt, K. (2007). Kausalmodellierung Mit Partial Least Squares - Eine Anwendungsorientierte Einführung. Gabler, Wiesbaden.

Iivari, J. (2005). An Empirical Test of the Delone-Mclean Model of Information System Success. The DATA BASE for Advances in Information Systems, 26 (2), 8-27.

Junglas, I., Niehaves, B., Spiekermann, S., Stahl, B.C., Weitzel, T., Winter, R. and Baserville, R. (2011). The Inflation of Academic Intellectual Capital: The Case for Design Science Research in Europe. European Journal of Information Systems 20 (1), 1-6.

Kakihara, M. and Sørensen, C. (2002). Mobility: An Extended Perspective, In Proceedings of the 35th Hawaii International Conference on System Sciences), pp. 1756-1766.

Kankanhalli, A., Tan, B.C.Y. and Wei, K.-K. (2005). Contributing Knowledge to Electronic Knowledge Repositories: An Empirical Investigation. MIS Quarterly, 29 (1), 113-143.

Karanasios, S. and Allen, D. (2014). Mobile Technology in Mobile Work: Contradictions and Congruencies in Activity Systems. European Journal of Information Systems, 23 (5), 529- 542.

Koo, C., Wati, Y. and Chung, N. (2013). A Study of Mobile and Internet Banking Service: Applying for Is Success Model. Asia Pacific Journal of Information Systems, 23 (1), 65-86. Kulkarni, U.R., Ravindran, S. and Freeze, R. (2007). A Knowledge Management Success Model: Theoretical Development and Empirical Validation. Journal of Management Information Systems, 23 (3), 309-347.

Lee, C.-C., Cheng, H.K. and Cheng, H.-H. (2007). An Empirical Study of Mobile Commerce in Insurance Industry: Task–Technology Fit and Individual Differences. Decision Support Systems, 43, 95–110.

Lee, S., Shin, B. and Lee, H.G. (2010). Understanding Post-Adoption Usage of Mobile Data Services: The Role of Supplier-Side Variables. Journal of the Association for Information Systems, 10 (12), 860-888.

Lee, Y.E. and Benbasat, I. (2003). Interface Design for Mobile Commerce. Communications of the ACM, 46 (12), 49-42.

Legner, C., Nolte, C. and Urbach, N. (2011). Evaluating Mobile Business Applications in Service and Maintenance Processes: Results of a Quantitative-Empirical Study, In Proceedings of the 9th European Conference on Information Systems (ECIS 2011), Helsinki, Finland.

Legner, C. and Thiesse, F. (2006). RFID-Based Maintenance at Frankfurt Airport. IEEE Pervasive Computing, 5 (1), 34-39.

Lewis, B.R., Templeton, G.F. and Byrd, T.A. (2005). A Methodology for Construct Development in Mis Research. European Journal of Information Systems, 14 (4), 388-400.

Lin, H.-F. and Lee, G.-G. (2006). Determinants of Success for Online Communities: An Empirical Study. Behaviour & Information Technology, 25 (6), 479-488.

Lohmöller, J.-B. (1989). Latent Variable Path Modeling with Partial Least Squares. Physica-Verlag, Heidelberg.

Luarn, P. and Lin, H.-H. (2005). Toward an Understanding of the Behavioral Intention to Use Mobile Banking. Computers in Human Behavior, 25, 873-891.

MacKenzie, S.B., Podsakoff, P.M. and Jarvis, C.B. (2005). The Problem of Measurement Model Misspecification in Behavioral and Organizational Research and Some Recommended Solutions. Journal of Applied Psychology, 90 (4), 710-730.

Malhotra, M.K. and Grover, V. (1998). An Assessment of Survey Research in Pom: From Constructs to Theory. Journal of Operations Management, 16 (4), 407-425.

Malhotra, N.K., Kim, S.S. and Patil, A. (2006). Common Method Variance in Is Research: A Comparison of Alternative Approaches and a Reanalysis of Past Research. Management Science, 52 (12), 1865-1883.

Martensen, A. and Gronholdt, L. (2003). Improving Library Users’ Perceived Quality, Satisfaction and Loyalty: An Integrated Measurement and Management System. The Journal of Academic Librarianship, 29 (3), 140-147.

Martini, A., Corsob, M. and Pellegrini, L. (2009). An Empirical Roadmap for Intranet Evolution. International Journal of Information Management, 29, 295-308.

McKinney, V., Kanghyun, Y. and Zahedi, F.M. (2002). The Measurement of Web-Customer Satisfaction: An Expectation and Disconfirmation Approach. Information Systems Research, 13 (3), 296-315.

Nah, F.F.-H., Siau, K. and Sheng, H. (2005). The Value of Mobile Applications: a Utility Company Study. Communications of the ACM, 48 (2), 85-90.

Nunnally, J. and Bernstein, I. (1994). Psychometric Theory. 3rd ed. McGraw Hill, New York.

Peffers, K., Tuunanen, T., Rothenberger, M.A. and Chatterjee, S. (2008). A Design Science Research Methodology for Information Systems Research. Journal of Management Information Systems, 24 (3), 45-77.

Petter, S., DeLone, W. and McLean, E.R. (2008). Measuring Information Systems Success: Models, Dimensions, Measures, and Interrelationships. European Journal of Information Systems, 17 (3), 236-263.

Petter, S., DeLone, W. and McLean, E.R. (2012). The Past, Present, and Future of "Is Success". Journal of the Association for Information Systems, 13 (Special Issue), 341-362.

Pitt, L.F., Watson, R.T. and Kavan, C.B. (1995). Service Quality: A Measure of Information Systems Effectiveness. MIS Quarterly, 19 (2), 173-187.

Podsakoff, P.M., MacKenzie, S.B., Jeong-Yeon, L. and Podsakoff, N.P. (2003). Common Method Biases in Behavioral Research: A Critical Review of the Literature and Recommended Remedies. Journal of Applied Psychology, 88 (5), 879.

Pousttchi, K. (2008). A Modeling Approach and Reference Models for the Analysis of Mobile Payment Use Cases. Electronic Commerce Research and Applications, 7 (2), 182-201.

Pries-Heje, J., Baskerville, R. and Venable, J.R. 2008. Strategies for Design Science Research Evaluation. In Proceedings of the 16th European Conference on Information Systems (ECIS 2008), Galway, Ireland.

Puschmann, T. and Alt, R. (2005). Developing an Integration Architecture for Process Portals. European Journal of Information Systems, 14 (2), 121-134.

Rai, A., Lang, S.S. and Welker, R.B. (2002). Assessing the Validity of Is Success Models: An Empirical Test and Theoretical Analysis. Information Systems Research, 13 (1), 50-69.

Ringle, C.M., Wende, S. and Will, A. 2005. "Smartpls 2.0 (M3) Beta." Hamburg, Germany: University of Hamburg.

Rogers, E.M. (1983). Diffusion of Innovations. Free Press, New York.

Seddon, P.B. and Kiew, M.-Y. (1994). A Partial Test and Development of the Delone and Mclean Model of Is Success, In Proceedings of the 15th International Conference on Information Systems (ICIS 94), pp. 99-110, Vancouver, Canada.

Segars, A.H. (1997). Assessing the Unidimensionality of Measurement: A Paradigm and Illustration within the Context of Information Systems Research. Omega, 25 (1), 107-121.

Sørensen, C., Al-Taitoona, A., Kietzmann, J., Picaa, D., Wireduc, G., Elaluf-Calderwooda, S., Boatenga, K., Kakiharad, M. and Gibsone, D. (2008). Exploring Enterprise Mobility: Lessons from the Field. Information Knowledge Systems Management, (7), 243-271.

Stone, M. (1974). Cross-Validatory Choice and Assessment of Statistical Predictions. Journal of the Royal Statistical Society, 36 (2), 111-133.

Straub, D., Boudreau, M.-C. and Gefen, D. (2004). Validation Guidelines for IS Positivist Research Communications of the AIS, 13, 380-427.

Tarasewich, P. (2003). Designing Mobile Commerce Applications. Communications of the ACM, 46 (12), 57-60.

Thomas, O., Walter, P., Loos, P., Nuttgens, M. and Schlicker, M. (2007). Mobile Technologies for Efficient Service Processes: A Case Study in the German Machine and Plant Construction Industry, In Proceedings of the 13th Americas Conference on Information Systems (AMCIS 2007), Keystone, Colorado, USA.

Thun, J.-H. (2008). Supporting Total Productive Maintenance by Mobile Devices. Production Planning & Control, 19 (4), 430-434.

Urbach, N. and Müller, B. (2011). The Updated Delone and Mclean Model of Information Systems Success, in: Information Systems Theory - Explaining and Predicting Our Digital Society, (Y.K. Dwivedi, M.R. Wade and S.L. Schneberger eds.), New York: Springer, pp. 1- 18.

Urbach, N., Smolnik, S. and Riempp, G. (2009). The State of Research on Information Systems Success. Business & Information Systems Engineering, 1 (4), 315-325.

Urbach, N., Smolnik, S. and Riempp, G. (2010). An Empirical Investigation of Employee Portal Success. The Journal of Strategic Information Systems, 19 (3), 184–206.

Urbach, N., Smolnik, S. and Riempp, G. (2011). Determining the Improvement Potentials of Employee Portals Using a Performance-Based Analysis. Business Process Management Journal, 17 (5), 829-845.

Wasserman, A.I. (2010). Software Engineering Issues for Mobile Application Development, In Proceedings of the 2010 FSE/SDP Workshop on the Future of Software Engineering Research, 397-400, Santa Fe, Nex Mexico, USA.

Werts, C.E., Linn, R.L. and Jöreskog, K.G. (1974). Intraclass Reliability Estimates: Testing Structural Assumptions. Educational and Psychological Measurement, 34.

Wold, H. (1985). Partial Least Squares. Encyclopedia of Statistical Sciences, 6, 581-591.

Yang, Z., Cai, S., Zhou, Z. and Zhou, N. (2005). Development and Validation of an Instrument to Measure User Perceived Service Quality of Information Presenting Web Portals. Information & Management, 42 (4), 575-589.

Dr. Christine Legner is Professor of Information Systems at HEC Lausanne, the Faculty of Business and Economics of the University of Lausanne (Switzerland). Prior to joining HEC Lausanne, she has been full professor at EBS Business School in Wiesbaden (Germany) and senior researcher at the University of St. Gallen (Switzerland). She has received a doctoral degree from University of St. Gallen and Masters degrees from University of Karlsruhe and from University of Paris-Dauphine (France). Prof. Legner’s research interests relate to business information systems, enterprise architecture management and digital business innovation in enterprises and across their entire value chain. Her work has appeared in a number of leading IS journals, including the Journal of Management Information Systems, Journal of the AIS and Journal of Strategic Information Systems. She also regularly presents her work at the leading international IS conferences.

Dr. Nils Urbach is Professor of Information Systems and Strategic IT Management at the University of Bayreuth. Furthermore, he is Deputy Director of the Finance & Information Management (FIM) Research Center and the Project Group Business & Information Systems Engineering of Fraunhofer FIT. Before, he was Assistant Professor at EBS Business School in Wiesbaden. He also received his doctorate from EBS. Furthermore, he holds a diploma in information systems from the University of Paderborn. He gathered international experience during his research stays at the University of Pittsburgh and at Université de Lausanne. Complementary to his academic work, he was Consultant with Horváth & Partners and Accenture. His work has been published in several international journals such as the Journal of Information Technology, Journal of Strategic Information Systems, Information & Management, and IEEE Transactions on Engineering Management as well as in the proceedings of key international conferences.

Christoph Nolte, MBA, is Head of Quality Management and Deputy Technical Director at DEKRA Automotive in Stuttgart, Germany, as well as Deputy Chairman of the Regional Advisory Group Europe at CITA, the International Motor Vehicle Inspection Committee. He has done strategic alignment at DEKRA Automotive since 2005 and introduced a number of mobile solutions in DEKRA. Furthermore, he holds a diploma in engineering from Technische Hochschule Mittelhessen. He is an expert in technology and materials.

# Mobile Business Application for Service and Maintenance Processes: Using Ex Post Evaluation by End-Users as Input for Iterative Design

## Highlights:

• We recommend linking the building of mobile business apps to their evaluation in productive use.

We suggest a model for ex post evaluation of mobile business apps’ utility for endusers.

• A performance-based analysis supports deriving priorities for future design iterations.

Mobile business apps’ design should focus on process quality while ensuring system quality.

The main contribution is an approach to use ex post evaluation as input for iterative design.
