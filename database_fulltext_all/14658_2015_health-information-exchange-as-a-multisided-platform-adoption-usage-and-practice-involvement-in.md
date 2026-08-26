---
otero_id: 14658
otero_key: "GBBH6E26"
title: "Health Information Exchange as a Multisided Platform: Adoption, Usage, and Practice Involvement in Service Co-Production"
authors: "Niam Yaraghi; Anna Ye Du; Raj Sharman; Ram D. Gopal; Ram Ramesh"
year: "2015"
journal: "Information Systems Research"
doi: "10.1287/isre.2014.0547"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## 6SR

![](/api/attachments/GBBH6E26/fulltext/images/eacbad498cfd9f2c0e9004d161e45cc8f0417fc0677f4abae38b334d04399a7f.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Health Information Exchange as a Multisided Platform: Adoption, Usage, and Practice Involvement in Service Co-Production

Niam Yaraghi, Anna Ye Du, Raj Sharman, Ram D. Gopal, Ram Ramesh

To cite this article:

Niam Yaraghi, Anna Ye Du, Raj Sharman, Ram D. Gopal, Ram Ramesh (2015) Health Information Exchange as a Multisided Platform: Adoption, Usage, and Practice Involvement in Service Co-Production. Information Systems Research 26(1):1-18. http://dx.doi.org/10.1287/isre.2014.0547

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2015, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/GBBH6E26/fulltext/images/db8ffc366e946f9521bf9bb0e798c0be2ab140617ff004068e9d9e393bd03623.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

http://dx.doi.org/10.1287/isre.2014.0547 © 2015 INFORMS

# Health Information Exchange as a Multisided Platform: Adoption, Usage, and Practice Involvement in Service Co-Production

Niam Yaraghi

Center for Technology Innovation, Governance Studies, The Brookings Institution, Washington, DC 20036, nyaraghi@brookings.edu

Anna Ye Du, Raj Sharman

Management Science and Systems Department, State University of New York at Buffalo, Buffalo, New York 14260 {yedu@buffalo.edu, rsharman@buffalo.edu}

Ram D. Gopal

Department of Operations and Information Management, University of Connecticut, Storrs, Connecticut 06269, ram.gopal@business.uconn.edu

Ram Ramesh Ram Ramesh

Management Science and Systems Department, State University of New York at Buffalo, Buffalo, New York 14260, rramesh@buffalo.edu

ealth Information Exchanges (HIE) are becoming integral parts of the national healthcare reform efforts, chiefly because of their potential impact on cost reduction and quality enhancement in healthcare services. However, the potential of an HIE platform can only be realized when its multiple constituent users actively participate in using its variety of services. In this research, we model HIE systems as multisided platforms that incorporate self-service technologies whose value to the users depends on both user-specific and networkspecific factors. We develop a model of adoption, use, and involvement of clinical practices in the coproduction of the HIE services. This model is grounded in social network theory, service operations theory, and institutional isomorphism theory. A longitudinal study of actual adoption and use behaviors of 2,054 physicians within 430 community medical practices in Western New York over a three-year period has been carried out to evaluate the proposed model. This study has been supported by HEALTHeLINK, the Regional Health Information Organization of Western New York, which has an extensive database comprising over half a million transactions on patient records by the HIE users. We extracted panel data on adoption, use, and service coproduction behaviors from this database and carried out a detailed analysis using metrics derived from the foundational theories. Positioning practices within two distinct but interrelated networks of patients and practitioners, we show that adoption, use, and service coproduction behaviors are influenced by the topographies of the two networks, isomorphic effects of large practices on the smaller ones, and practice labor inputs in HIE use. Our findings provide a comprehensive view of the drivers of HIE adoption and use at the level of medical practices. These results have implications for marketing and revenue management of HIE platforms, as well as public health and national/regional healthcare policy making.

Keywords: health information exchange; multisided platforms; network externalities

## 1. Introduction

Healthcare expenditures constitute a major part of the structural deficit in the U.S. federal budget (Chernew et al. 2010). The United States spent 17.9% of its GDP on healthcare in 2010, more than any other country in the world (Baicker and Skinner 2010, Martin et al. 2012). Despite the \$2.6 trillion of expenditure, the quality and efficiency of the U.S. healthcare system ranked last when compared to Britain, Canada, Germany, the Netherlands, Australia, and

New Zealand (Davis et al. 2010). As a result, a concerted national effort to reform healthcare using information technologies with a focus on reducing costs and increasing quality of service is well under way (Menon et al. 2000, Casalino et al. 2003, Aron et al. 2011, Buntin et al. 2011). The recently enacted Health Information Technology for Economic and Clinical Health Act (HITECH) requires all medical records to be in standardized digital forms by 2014 (Blumenthal and Tavenner 2010). One of the principal objectives of this act is to set up Health Information Exchange (HIE) platforms through which providers can access medical data in a timely and cost-effective manner (Sipkoff 2010). HIE is a potential solution to persisting problems in the U.S. healthcare system including cost (Overhage et al. 2002, Walker et al. 2005), safety (Bloom 2002), and efficiency (Corrigan et al. 2002).

Despite significant initial promise, the nationwide growth in HIE services is far from meeting the expectations (Adler-Milstein et al. 2011). Previous research reveals different barriers to HIE expansion. These barriers include financial factors (Fontaine et al. 2010), competition between healthcare providers (Grossman et al. 2006), lack of stakeholder buy-in (Malepati et al. 2007), distrust in other HIE members (Ross et al. 2010), and security concerns (Edwards et al. 2010).

Although these studies shed light on our understanding of HIE diffusion, significant lacunae exist in this body of literature. First, most of them focus on individual practitioners rather than practices as their unit of analysis. The decision to adopt HIE is typically made at the practice level as a group rather than at the physician level as an individual. Consequently, important practice-level considerations such as Information Technology (IT) capital and labor inputs, the value derived from HIE by a practice as a whole, and the involvement of a practice in the coproduction of healthcare services that could significantly affect both HIE adoption and use cannot be adequately captured unless they are studied at the group level. Second, most studies investigate adoption decisions at a single point in time using survey data. However, adoption and use of HIE the systems are dynamic, time-variant processes that require analyses of panel data captured from actual behaviors. The snapshot data does not capture these temporal dimensions of adoption including diffusion of awareness and participation at different levels in e-healthcare over time. Furthermore, the conclusions of studies based only on survey data may be limited to outcomes that are only directly perceived by community members, thus necessitating the need for longitudinal observations of actual behaviors. Third, and most important, to our knowledge the current literature fails to consider HIE as a multisided platform (MSP). An HIE typically encompasses multiple unique but interdependent sides, i.e., public hospital systems, private healthcare practices, support services such as laboratories, pharmacies, and radiology units, and even insurance providers in some instances. Accordingly, the value derived by each side from an HIE is unique, yet depends on the participation and engagement of the HIE by the other sides. A consideration of HIE as an MSP would lead to a characterization of network externalities in each side of the platform and the cross-externalities among the multiple sides. Determining these externalities requires analyses of actual longitudinal behaviors of the different sides of the platform, which cannot be done with survey-based snapshot data of community perceptions. Finally, a multisided HIE platform operates within the larger contexts of two broad social networks, i.e., network of patients and network of service providers. Hence, analysis of these social networks in addition to practice-level characteristics becomes essential in understanding the externality effects of HIE adoption and use.

Motivated by the importance and contemporary prominence of HIE platforms at all levels of healthcare policy and public health, and shortfalls in the extant literature in this area, we undertook a longitudinal study of adoption and use behaviors by community practices in collaboration with HEALTHeLINK Inc.,<sup>1</sup> a regional HIE serving the Western New York area. HEALTHeLINK provided extensive panel data sets on adoption and use behaviors of community practices over a three-year period since its inception. Using this unique data set, we modeled the HIE as a multisided platform and investigated its different network externalities using (a) social network characterizations of the underlying contexts, (b) modeling the service coproduction process by the practices in conjunction with the HIE, and (c) modeling of adoption and use behaviors over time as driven by the attributes of practices, social networks, and processes involved. The theoretical contributions of this paper, summarized below, are four-fold.

First, we consider HIE as a multisided platform in which the potential value of HIE for each practice depends on the other practices with which it shares patients. We show that the practice position in a network of patients is an important determinant of HIE adoption and use. Second, we use social network analysis to capture the diffusion of information about HIE benefits among practices through the common practitioners who are affiliated with multiple practices. We show the significant role of physicians in diffusing the information about the benefits of HIE and how to use it among practices with which they are affiliated. Third, we study the use of HIE at the practice level and develop an analytical model to capture the latent practice efficiency in coproduction of HIE services, which otherwise would not be possible to measure directly. Finally, we study the effects of institutional isomorphism of HIE adoption by capturing the dependency of smaller practices on larger practices as the ratio of both patients and physicians that they share with larger practices and show that the smaller practices with a higher level of dependency on larger practices tend to follow the lead of larger practices and adopt HIE sooner than their peers.

The paper is organized as follows: §2 presents the HIE background. It also reviews the literature on the barriers and drivers of HIE adoption, explores the most recent studies that address adoption of Information Systems (IS) through social network analysis, and examines the literature on the role of customer efficiency as an active element of the coproduction process of services. Section 3 introduces the empirical context and discusses how HEALTHeLINK collects the medical data from the data providers and distributes it among its members. The model of HIE adoption, use, and efficiency in service coproduction is presented in §4. Section 5 presents the results of the empirical analysis and §6 is a discussion of results and conclusions. The associated online supplement (available as supplemental material at http://dx.doi.org/10.1287/isre.2014.0547) is organized as follows: Section A provides a multisided characterization of the HIE platform along with the associated network externality effects. Section B presents the structure of the HEALTHeLINK platform using this HIE model. Section C presents the structure of the HEALTHeLINK database and discusses the details of operationalization of model variables. A graphical illustration of our research model is presented in Section D.

## 2. Related Literature

## 2.1. HIE Background

Community Healthcare Management Information Systems (CHMIS) were created in 1990 through several grants from the John A. Hartford Foundation.<sup>2</sup> These systems were designed as a central repository of patients’ medical and demographic data and were mainly used to study and evaluate the healthcare services and facilitate the billing procedure as a means of cost reduction (Stark et al. 1996, Rubin 2003). Technical problems, expensive infrastructure, privacy and legal concerns, and the lack of a sustainable business model were the main causes of their failure (Gardner and Warner 1994, Starr 1977, Vest and Gamm 2010).

Community Health Information Networks (CHIN) emerged over the second half of the 1990s. These commercial platforms had a decentralized architecture and were focused on reducing the costs of medical data transmission between healthcare providers (U.S. Congress: Office of Technology Assessment 1995, Lassila et al. 1997). Although with the advances in computer network technology, these platforms did not have many of the technical problems faced by their ancestors, they did not survive because they could not effectively manage the relationship between their stakeholders. This led to intense competition among both healthcare providers and technology vendors and hindered the potential performance of CHINs (Paul 1995, Payton and Ginzberg 2001, Briggs 2003, Lorenzi 2003, Rubin 2003, Vest and Gamm 2010). Moreover, these networks were unable to achieve significant value and were criticized for not being cost effective (U.S. Congress: Office of Technology Assessment 1995, Lewis and Wakerly 1995).

Unlike the two former approaches, Regional Health Information Organizations (RHIO) were initiated with unprecedented political and governmental support (Solomon 2007, Squazzo 2007). The payment policies are shifting rapidly to reward the quality rather than the volume of healthcare services through different approaches such as Accountable Care Organizations (ACO), bundled payments, and medical home initiatives. This motivates the healthcare providers to adopt HIE solutions to increase the quality of their services (Bates and Bitton 2010, McClellan et al. 2010). On the other hand, by including the exchange of health information between different providers as an important criteria for financial incentives awarded through the HITECH act, the Office of the National Coordinator (ONC) for Health Information Technology actively supports HIE (Williams et al. 2012).

RHIOs act as neutral organizations that promote and facilitate the exchange of medical information among the providers within a geographical region. The collaborative nature of RHIOs and their limited focus on providers within a geographical region intensifies the sensitivity of proprietary medical information and raises the question of data ownership (Amatayakul 2008, Grossman et al. 2008). Moreover, the most persistent obstacle to growth of RHIOs remains financial sustainability (Mcllwain and Lassetter 2009, Scalise 2006, Terry 2006). In addition to RHIOs, as building blocks of a Nationwide Health Information Network (NwHIN), ONC recognizes other solutions to promote HIE and no longer provides direct financial support to RHIOs (Lenert et al. 2012). While RHIOs serve as a query based exchange in which the medical records of each patient can be retrieved at any time by an authorized member, the DIRECT<sup>3</sup> initiative offers an Internet-like point to point exchange between different providers. The other solution, suggested by the Markle Foundation,<sup>4</sup> was a consumer-mediated exchange in which patients have control over their records and manage the aggregation and distribution of their own medical information among the healthcare providers (Vest and

Gamm 2010, Williams et al. 2012). Although neither of these two additional solutions provide all of the capabilities of RHIOs, they provided new opportunities for private HIE vendors to increase their presence in the market. These private vendors recruit members based on economic incentives, generating profits without having to meet the requirements for undertaking the truly difficult tasks in health information exchange and critical services necessary for a community health system or even universal connectivity for the region. As a result the private vendors can grow at a much higher rate than RHIOs (Lenert et al. 2012). The decrease in governmental support and the intense competition that RHIOs face with the advent of private HIE vendors warrants a careful investigation of the drivers of both HIE adoption and use. To our knowledge, this research is among the first to consider HIE as a multisided platform and to investigate the complex and interrelated relationships between practices, physicians, and patients to provide a comprehensive view of the drivers of HIE adoption and use.

## 2.2. Health IT Adoption

Financial factors are important barriers to Health IT adoption. Adler-Milstein et al. (2011) study the level of participation of U.S. hospitals in promoting HIE and report that nonprofit hospitals and those with larger market shares are more likely to promote HIE growth. The results of a survey from 155 officials of childrens’ hospitals show the lack of financial resources as a major barrier to Health IT use (Nakamura et al. 2010).

A major part of IS literature focuses on Health IT outcomes. The use of HIE is shown to prevent redundant tests and avoid hospitalizations (Johnson et al. 2011). Through empirical examinations of two large Asian hospitals, Aron et al. (2011) show that automation of control systems significantly reduces both procedural and interpretative error rates by medical staff. Kane and Labianca (2011) investigate the effects of users’ post-adoption resistance to healthcare IS on patient safety at the individual, shared group, and group configuration levels. They show that the location of healthcare providers in the groups’ workflow is a determinant of IS avoidance. By surveying approximately 600 individuals in 40 healthcare groups, Kane and Alavi (2008) find that IS centrality within the network is positively associated with both efficiency and quality of healthcare.

## 2.3. Social Structure

The importance of social networks in the diffusion of innovation was first revealed by seminal studies of Rogers (1962) and Coleman et al. (1966). Focusing on IS literature, next we briefly review recent studies on the role of social networks in IS diffusion and user performance.

Sasidharan et al. (2012) reveal that the status of individuals within a network highly influences their performance and the quality of information they receive from the system. Chellappa and Saraf (2010) study performance of firms in Enterprise Systems Software markets and show that the status of firms in their networks of alliances positively influences their performance. By analyzing the use of video telephone systems over 18 months, Kraut et al. (1998) show how increased use of the system by others changes both the normative environments and potential values derived from the system. Social structure of digital networks has also been investigated as a predictor of diffusion of viral messages (Bampo et al. 2008).

2.4. Customer Efficiency in Service Coproduction IS are widely used to increase the efficiency and quality of customer service by engaging the customers in producing their own required services. Early studies on service management consider the interaction between users and service providers in the process of providing services (Fuchs 1968). Time, control, effort, dependence, efficiency, and human contact are among the factors that affect customers’ decisions to use automatic service channels (Kelley et al. 1990). The customers’ capabilities in using the IS that are designed to facilitate the services affects their levels of use and satisfaction with the self-service channels. Xue and Harker (2002) first conceptualized the notion of customer efficiency to capture the differences between customers’ involvement in coproduction of services. Xue et al. (2007) consider customer efficiency as a latent variable and propose a method to measure it based on the users’ choices of different service channels. In the context of Internet banking, Xue et al. (2011) further investigate the role of customer involvement in service coproduction in customers’ adoption of online banking systems.

## 3. Context

## 3.1. HIE as a Multisided Platform

HIE simply defined is the act of sharing medical information on patients among different healthcare providers. HIE platforms facilitate this exchange by collecting, organizing, and storing the medical data from various providers on a centralized or decentralized database. Access to this database is enabled through a portal that is commonly shared by the participating members of the exchange. When a participating member wishes to view a specific record, the access request is first verified and validated, and then the record is retrieved from the database.

In general, four major types of users are connected to an HIE. Each type constitutes a side of the multisided HIE platform. The first and most important side is comprised of the Patients whose records are stored in the exchange. The second type of users are the major Medical Data Providers. This group consists of labs, radiology centers, and major hospitals in a community. Although private practices and other ancillary healthcare services could also upload medical data on their patients to an HIE database, the volume of data generated by them is usually small compared to the data uploaded by the major providers. The major providers generally push data in large volumes into an HIE while the other users tend to push and pull data mostly in smaller volumes. Because the HIE services needed by users are different, it is important to distinguish between these two types of providers in describing the HIE user base. The third group of users consists of independent physicians, private practices, and other medical/paramedical services that could use an HIE. For ease of exposition, we denote this group as Healthcare Providers. Unlike the second group, Healthcare Providers are geographically widespread, much larger in number but much smaller in size than the major providers, and more likely to be push/pull users of the exchange. Healthcare Providers are the direct beneficiaries of data provided by labs, radiology centers, and major hospitals. The practices could use the data accessed through an HIE to improve the quality of their healthcare services and simultaneously reduce costs. The last group of users consists of Payers of medical services such as insurance companies, and state and federal governments. Their connection to an HIE is through the patient medical and health records that may be available through the exchange. An HIE would offer a smoother process of claims processing, better control over payments to healthcare providers, and enhanced quality of care. The interaction of these four sides on an HIE platform is discussed in Section A of the online supplement.

## 3.2. Patient Consent

When practices request medical records (lab, radiology, or hospital reports), the results will automatically be pushed to the HIE data center by the medical data providers regardless of the membership status of the ordering provider. Patient consent is essential before any member of the HIE can access the patient’s medical records from the platform. Although medical records are pushed into the HIE system by data providers, records will not be accessible without patient consent. Thus, there are two prerequisites for access to HIE data: (i) membership, and (ii) patient consent. A member practice would advise its patients to provide consent so that the practice can access their records from the HIE. The consent forms are distributed by HEALTHeLINK to its members only. Nonmembers cannot obtain patient consent. As a result, data ordered by a member practice will not be available to a nonmember. Similarly, the data ordered by a nonmember practice will not be accessible to a member practice although such data is pushed into the system; a nonmember would not ask the patient to consent. Furthermore, as practices join the system, they actively solicit consent from their patients. This will result in an increased volume of accessible data on the HIE platform for other members.

## 3.3. Networks of Common Patients and Common Physicians

We recognize two separate networks of common patients and common physicians in the HIE market. In both networks, practices are the nodes. In the network of common patients, the nodes are linked by common patients. The weight of each link is proportionate to the number of shared patients. In this network, degree centrality of a node is characterized as the total number of practices that are directly linked to it. The practices that share patients with a large number of other practices will have a high degree of centrality while the peripheral practices that do not share patients with many other practices will have a lower degree of centrality. We also construct a network termed Network of Common Practitioners where each node represents a practice and a link exists between a pair of nodes if they share common medical practitioners. Each link is weighted by the number of common practitioners between two associated practice nodes.

## 3.4. HIE Service Channels

HEALTHeLINK allows practices to receive lab reports, radiology reports, and hospital transcriptions via two different channels: (1) directly through their interoperable Electronic Medical Record (EMR) systems which do not require user involvement, and (2) through manual search and download of medical data from a designated Web portal. The first channel is considered full service, i.e., the practice involvement in the coproduction process is minimal. The second channel is considered self-service, i.e., practices have to search and download their required medical information from the Web portal.

## 3.5. Practice Efficiency in Coproduction of HIE Services

The coproduction concept in the service industry was first introduced by Whitaker (1980, p. 240). He introduces the concept with some examples:

In “delivering” services, the agent helps the person being served to make the desired sorts of changes. Whether it is learning new ideas or new skills, acquiring healthier habits, or changing one’s outlook on family or society, only the individual served can accomplish the change. He or she is a vital “coproducer”

of any personal transformation that occurs. The agent can supply encouragements, suggest options, illustrate techniques, and provide guidance and advice, but the agent alone cannot bring about the change. Rather than an agent presenting a “finished product” to the citizen, agent and citizen together produce the desired transformation.

Based on this definition, Xue and Harker (2002) introduce consumer efficiency: An efficient customer is simply a customer who uses less time while accomplishing more transactions. In other words, an efficient customer uses less time to complete the same or even more transactions as compared to inefficient customers.

Following this definition, Xue et al. (2007) provide an analytical model to measure the customer efficiency in the online banking context based on the customer’s use behavior via two channels, i.e., self-service (ATM, website) and full service (Bank Tellers). We use the exact terminology in the HIE context. Coproduction does not mean helping to create more medical documents. In fact, HIE does not create any medical documents; it facilitates access to the documents that are already created by data providers and would have otherwise been accessed via other channels (such as fax, mail, etc.). In this context, the successful realization of HIE services (i.e., online delivery of the medical records) requires practices’ involvement or participation. The practices have different levels of participation. Some of them are very active, while others are not. According to Fuchs (1968), customers are always either passively or actively involved in the service production process. We apply the approach used by Xue et al. (2007) to measure the practices’ efficiency in coproduction of HIE services based on their participation behavior via two self-service and full-service channels. We define “practice efficiency”<sup>5</sup> as a practice’s ability to share as many medical records as possible with minimum labor and investment. HIE member practices typically invest in their own IT infrastructure as well as human resources to use the HIE services and access their patients’ medical information. When direct measurements of input and output may not be possible, efficiency can be observed as a latent variable through actual HIE customer use behaviors. Holding all other factors constant, the more efficient customers will use the system more than the customers with less efficiency (Xue et al. 2007). In the appendix we propose an analytical model to measure the unobservable practice efficiency in using HIE. Note that the efficiency pertains to the practice of accessing the documents via the HIE system. It is not the efficiency of producing the necessary documents representing the entire demand to a practice, nor does it capture the possible higher performance that a practice may reach in providing better healthcare services with lower costs as a result of HIE adoption and use.

## 4. Theory and Hypotheses

## 4.1. Degree Centrality

Following our discussion about the role of the member providers in obtaining the consent of patients and increasing the volume of accessible data on HIE platforms, we argue that the potential value of an HIE as a multisided platform for a given practice depends on how many other practices have joined the system and how many patients the given practice is sharing with them. The common patients who visit multiple practices create an opportunity for practices to realize this potential. If a patient only visits a single practice, then his or her documents will already be available in the EMR systems or traditional paper based medical archives in that particular practice and there is no need to access HIE for further information. Yaraghi et al. (2013, 2014) studies on the growth of HIE platforms confirm that the flow of patients among different providers has a significant impact on their propensity to adopt the HIE system. Because degree centrality captures the extent to which a practice is sharing patients with others, we argue that the value of HIE for practices with higher in-degree centralities in the network of common patients will be higher and thus they will adopt HIE sooner and use it more than others.

<sup>Hypothesis</sup> <sup>H1-1.</sup> Practices with higher in-degree centrality in the network of common patients adopt HIE sooner than others.

<sup>Hypothesis</sup> <sup>H1-2.</sup> Practices with higher in-degree centrality in the network of common patients use HIE more than others.

The availability of alternative channels highly affects the potential value of HIE to practices. If users could receive the benefits of an HIE through other channels, the HIE would be of less value to them, and thus they would have less incentive to adopt HIE (Boyer et al. 2002, Xue et al. 2011). Proximity to main data providers offers easier and faster access to medical records for practices in dense urban areas compared to those in rural areas. On the other hand, practices in rural areas may have the health records of their entire set of patients. If they do not share patients with other practices, they would not need to use HIE to download any more records. Thus the potential value of HIE for practices in rural areas will be capitalized if they share a considerable number of patients with others. Basically we hypothesize that for a rural area practice shared patients becomes even more important in their decision to adopt HIE because it is harder for them to receive paper records via other channels. This implies that, ceteris paribus, the practices in rural areas will adopt HIE sooner and use it more if they share patients with other practices.

<sup>Hypothesis</sup> <sup>H1-3.</sup> Rural location positively moderates the relationship between in-degree centrality and HIE adoption time.

<sup>Hypothesis</sup> <sup>H1-4.</sup> Rural location positively moderates the relationship between in-degree centrality and HIE use.

## 4.2. Betweenness Centrality

According to social networks theory, nodes with high betweenness centrality will observe the perspectives and behaviors of other nodes due to their vantage locations in the network and are in a better position to innovate and learn through experiments (Mehra et al. 2001, Sasidharan et al. 2012). In the context of this study, the quality of HIE information and the velocity with which it is received and transmitted by a practice node through common practitioners is proportionate to its betweenness centrality. The practices with high betweenness centrality are most likely to receive information about HIE benefits and to gain knowledge from HIE use through the practitioners who are also affiliated with other practices. Accordingly, we use betweenness centrality in the network of common practitioners as a representative metric for the recognition of the potential value of an HIE by a practice. Consistent with prior research on diffusion of innovation through social networks (Davis 1991, Grewal et al. 2006, Tucker 2008), we argue that the practices with high betweenness centrality in the network of common members, are more likely to know about HIE benefits and hence, be influenced by the adoption behaviors of other practices. As a result they adopt HIE sooner than others.

In the healthcare context, a large portion of learning happens through peers rather than conventional training and marketing procedures (Venkatesh et al. 2011). Because practices with higher betweenness centrality in the network of common practitioners have better opportunities to learn how to use HIE more effectively than others, they are expected to have a higher level of HIE use as well.

<sup>Hypothesis</sup> <sup>H2-1.</sup> Practices with higher betweenness centrality in the network of common physicians adopt HIE sooner than others.

<sup>Hypothesis</sup> <sup>H2-2.</sup> Practices with higher betweenness centrality in the network of common physicians use HIE more than others.

Learning about HIE through common physicians improves as the experience of practices with HIE systems increases. The longer the experience with HIE, the higher the chance for a practice to learn more about it not only through the common physicians but also through its own experience. As practices learn more about HIE, their level of HIE use would also increase. We expect the tenure of a practice with HIE to positively moderate the relationship between betweenness centrality and HIE use.

<sup>Hypothesis</sup> <sup>H2-3.</sup> Tenure positively moderates the relationship between betweenness centrality and HIE use.

Training with IS improves the users’ skills and thus their efficiency in using the system (Gur ˇau 2002, Wang et al. 2003). In the health-care context, familiarity with IS happens through the network of peers over a relatively longer period of time. During the post-adoption period, users learn how to use the HIE through self-experience and through their peers. This will increase their efficiency in HIE service coproduction. Experience with HIE not only helps practices to learn how to use HIE more efficiently on their own but also provides them with more opportunities to learn about it through the physicians that they share.

<sup>Hypothesis</sup> <sup>H2-4.</sup> Betweenness centrality in the network of common physicians positively affects the practice efficiency in coproduction of HIE services.

<sup>Hypothesis</sup> <sup>H2-5.</sup> Tenure positively moderates the relationship between betweenness centrality and the practice efficiency in coproduction of HIE services.

## 4.3. Institutional Isomorphism

Institutional theory describes the notion of isomorphism as the tendency of an organization to follow other organizations especially when faced with new and uncertain phenomena with high levels of risk (DiMaggio and Powell 1983, DiMaggio 1988, Hall and Quinn 1984). DiMaggio and Powell (1983, p. 157) state: “When organizational technologies are poorly understood and when goals are ambiguous, or when the environment creates symbolic uncertainty, organizations tend to model themselves after similar organizations in their field that they perceive to be more legitimate or successful.”

Organizations affect each other either through explicit interactions or by implicitly becoming external change agents. Certain large practices and especially the major hospital systems can be regarded as influential change agents over other comparatively smaller community practices. The adoption of innovations by opinion leaders can have a significant effect on other peers in the network (Rogers and Kincaid 1981). The significant influence of opinion leaders on adoption of new innovations has also been confirmed in IS literature (Gurbaxani 1990, Kwon 1990, McLeod Jr. and Fuerst 1982). Loh and Venkatraman (1992) studied the trends in IT outsourcing and showed that the largescale IBM-Kodak contract became a flag bearer for numerous subsequent contracts in the industry and coined the term Kodak Effect. Similarly, adoption by large and well known practices and major hospital systems would signal a recognition of the potential value of an HIE to other practices in a community. Davis (1991) studies the diffusion of similar corporate strategies among Fortune 500 firms and shows the significant effect of interlocks among firms on their adoption of similar strategies.

HEALTHeLINK was created as a consortium of payers and major practices in Western New York. These large practices were among the strong supporters and the first to adopt HIE. Following the same logic, the high ratio of common physicians between smaller and larger practices will lead smaller practices to follow the similar decisions made by larger practices. The high ratio of common patients, on the other hand, reflects the degree of financial dependency of smaller practices on larger practices. When a small practice receives most of its patients, as the sources of revenue, from a larger practice, it tends to follow the strategies of the larger practice. Assuming that large practices adopt HIE first, these observations lead to the following two hypotheses.

<sup>Hypothesis</sup> <sup>H3-1.</sup> Practices with higher patientcentric isomorphic quotients adopt HIE sooner.

<sup>Hypothesis</sup> <sup>H3-2.</sup> Practices with higher practitionercentric isomorphic quotients adopt HIE sooner.

The graphical representation of the above hypotheses is presented in Section D of the online supplement.

## 5. Empirical Analysis

## 5.1. Data

In this research, we used a database consisting of the medical records of 30,626 unique patients provided by HEALTHeLINK. Medical records refers to lab, radiology, or hospital transcription reports. The medical records of these patients were ordered by the healthcare providers in Western New York and created by the data providers at the exchange between August 2008 and July 2011. Conditional on patient consent, the practices can use HIE to access these records. Note that a patient could have multiple records and a record could be accessed by multiple physicians, while a physician could also access multiple records. The access logs consisted of 463,146 record accesses through full service channels and $^ { 4 2 , 0 5 7 }$ accesses through self-service channels. Our analysis used six specific data sets. The first two were comprised of the access logs pertaining to the full- and self-service channels, respectively. This represents the number of times that a particular practice has used either of the two channels to view the medical records that were ordered by itself or by other practices for a particular patient. In cases where a large provider has several affiliated practices, the subordinate practices are treated as independent entities and the adoption and HIE use by each of the affiliated practices are analyzed independently; the subordinate practices do not necessarily adopt the HIE at the same time and their use of HIE is also independent of their affiliated practices.

Because all of the major data providers (labs, radiology centers, and hospitals) have already adopted HIE, every medical document that is created by these data providers is automatically pushed to the HEALTHeLINK data center. This data will only be accessible to HIE members if the patient has previously provided consent to sharing of their medical records. We collected the data on type, creation date, and ordering doctor of these medical reports regardless of the HIE membership of the ordering doctor. The physicians in each practice need unique, practice-specific usernames and passwords to access the HIE services. Hence, if a physician is affiliated with multiple practices and hospitals, he would need different usernames and passwords for each affiliation. The fourth data set contains the affiliation data of all of the members of HEALTHeLINK. This data set, in conjunction with the third data set is used to identify the common physicians and patients between different practices in each month. The fifth data set contains the membership date and location of each practice. The last data set consists of the data that we collected on the populations of the cities in which each practice is located. We merged that data with the location and membership data set for further analysis. The complete description of data processing and analysis procedure is provided in Section C of the online supplement.

Our analysis consists of three stages. First, we analyze the use patterns of practices in self-service and full-service channels and test the hypotheses as to the covariates of HIE use. Second, we estimate the latent practice efficiency as described in the appendix and investigate the hypotheses as to the covariates of practice efficiency. Third, we perform a survival analysis to test the hypotheses as to the covariates of HIE adoption.

## 5.2. Variables

5.2.1. Dependent Variables. Access measures the level of HIE use by each practice and represents the logarithm of the total number of times that HIE was used by a particular practice to download any of the three different types of medical documents (lab reports, radiology reports, and hospital transcriptions) in each month via the full- or self-service channel. The TimeToAdopt is measured in months and represents the time that it took for each practice to adopt HIE. PracticeEfficiency measures the latent efficiency of each practice in each month in producing HIE services. Refer to the appendix for a detailed discussion on efficiency measurement.

5.2.2. Independent Variables. The DegreeCentrality and BetweennessCentrality of each practice is calculated according to the common patients’ and common physicians’ networks, respectively. DegreeCentrality is calculated per month and shows the number of participating practices with which a focal practice is sharing patients. This represents the network externality effect. As the number of participating practices that share patients with a focal practice grows, the volume of accessible data also increases and thus HIE becomes more valuable for the focal practice. The patient and physician isomorphic quotients are calculated based on the ratio of shared patients and physicians of smaller practices with top large practices, respectively.

5.2.3. Control Variables. The availability of alternative options affects the potential value of the new innovation for consumers (Boyer et al. 2002, Xue et al. 2011). To control for the effects of proximity and ease of access to medical data providers, we control for the location of the practices via a binary variable, Rural, which is equal to one if the practice is in a rural area and far from the main data providers. The literature highlights the effects of competition on the practices’ tendency to join and use HIE systems (Melnick and Keeler 2007, Vest and Gamm 2010). We control for the effect of competition by including the MarketShare in the models. The value of each of the three document types provided by HEALTHeLINK (lab reports, radiology reports, and hospital transcripts) is different among practices depending on their specialties and patient demographics. For a primary care practice, lab reports may be more essential while for a specialty practice, such as orthopedics, radiology reports may be most important. In every time period, we consider each practice’s total number of accesses through both channels (self- and full-service) to each of these three different documents as proxies for the Value of each service in the next time period. To consider the effects of learning through experience and its possible impact on user efficiency (Jensen and Aanestad 2006, Venkatesh et al. 2011), we control for Tenure, which measures the number of months since a practice adopted HIE. The literature also suggests that the time saving benefits of electronic health records (EHR) are realized more by nurses rather than physicians (Poissant et al. 2005). Thus, nurses tend to have more positive attitudes toward the HIE systems (Venkatesh et al. 2011). We control for these effects by NurseRatio which measures the ratio of nurses to physicians in a practice. A more detailed description of the variables in our analysis and the correlations between the variables are reported in Section C of the online supplement. Descriptive statistics are presented in Table 1.

## 5.3. Results

We regress the logarithm of HIE access times through both self- and full-service channels on correlates of practice efficiency, cost of practice effort, and service value and alternative channels. Note that the network centrality metrics are calculated per month and are considered dynamic constructs in the model. Moreover, to address the collinearity between tenure and its squared term, we have centralized tenure around its mean. Formally, we estimate the following model:

Table 1 Variable Definition and Summary Statistics (Reports the Statistics Only for the HIE Members)

<table><tr><td>Variable</td><td>Definition</td><td>Average</td><td>Std. dev.</td></tr><tr><td>logLAB</td><td>Logarithm of the number of lab reports accessed by each practice through both channels in each month</td><td>1.6901630</td><td>1.6062388</td></tr><tr><td>logRADIO</td><td>Logarithm of the number of radiology reports accessed by each practice through both channels in each month</td><td>1.4980636</td><td>1.1516464</td></tr><tr><td>logTRANS</td><td>Logarithm of the number of hospital transcriptions accessed by each practice through both channels in each month</td><td>1.1716654</td><td>0.8560032</td></tr><tr><td>Tenure</td><td>Number of months since membership until August 2011</td><td>11.2937727</td><td>7.7366104</td></tr><tr><td rowspan="2">Rural</td><td>= 1 if the population of the city in which the practice is located in is less than 17,000</td><td>10.15119%</td><td>N/A</td></tr><tr><td>= 0 if the population of the city in which the practice is located in is more than 17,000</td><td></td><td></td></tr><tr><td>logMarketShare</td><td>Logarithm of the number of potential patients that a practice with size m located in a city with population of N and healthcare provider population of M = m × N/M.</td><td>9.0726367</td><td>1.6123149</td></tr><tr><td>NurseRatio</td><td>Ratio of nonphysician employees to physician employees in each practice</td><td>0.2763163</td><td>0.2391473</td></tr><tr><td>In-degreeCentrality</td><td>Normalized in-degree centrality in the network of common patients. The network nodes in each month consist of only the member practices.</td><td>0.0125542</td><td>0.0447516</td></tr><tr><td>Out-degreeCentrality</td><td>Normalized out-degree centrality in the network of common patients. The network nodes in each month consist of only the member practices.</td><td>0.0125542</td><td>0.0342362</td></tr><tr><td>BetweennessCentrality</td><td>Normalized betweenness centrality in the network of common physicians. The network nodes in each month consist of only the member practices.</td><td>0.0160172</td><td>0.0536078</td></tr><tr><td>PracticeEfficiency</td><td>Practice efficiency in HIE service co-production</td><td>0.2845370</td><td>0.090142</td></tr><tr><td>CommonPatientsWithLargePractices</td><td>Ratio of patients shared with major practices</td><td>0.1243217</td><td>0.0438938</td></tr><tr><td>CommonPhysiciansWithLargePractices</td><td>Ratio of physicians shared with major practices</td><td>0.3084354</td><td>0.1207375</td></tr></table>

Table 2 Estimation Results of Full-Service Channel Use

<table><tr><td>Variable</td><td>Coefficient</td><td>Estimate</td><td>Standard error</td><td>t value</td><td>Pr &gt; |t|</td><td>VIF</td></tr><tr><td>Intercept</td><td> $\beta_0$ </td><td>1.216743</td><td>0.8390</td><td>1.45</td><td>0.1473</td><td>0</td></tr><tr><td>LabServiceValue</td><td> $\beta_1$ </td><td>0.067806</td><td>0.0240</td><td>2.83</td><td>0.0048</td><td>2.04982</td></tr><tr><td>RadiologyServiceValue</td><td> $\beta_2$ </td><td>0.168508</td><td>0.0363</td><td>4.65</td><td>&lt;0.0001</td><td>2.89912</td></tr><tr><td>TranscriptionServiceValue</td><td> $\beta_3$ </td><td>0.178945</td><td>0.0413</td><td>4.34</td><td>&lt;0.0001</td><td>2.30513</td></tr><tr><td>Tenure</td><td> $\beta_4$ </td><td>0.03747</td><td>0.00911</td><td>4.11</td><td>&lt;0.0001</td><td>3.38458</td></tr><tr><td>Tenure $^2$ </td><td> $\beta_5$ </td><td>-0.002637</td><td>0.000582</td><td>-4.53</td><td>&lt;0.0001</td><td>1.77921</td></tr><tr><td>Rural</td><td> $\beta_6$ </td><td>-0.01144</td><td>0.4707</td><td>-0.02</td><td>0.9806</td><td>1.17519</td></tr><tr><td>MarketShare</td><td> $\beta_7$ </td><td>-0.06465</td><td>0.0942</td><td>-0.69</td><td>0.4928</td><td>1.10615</td></tr><tr><td>NurseRatio</td><td> $\beta_8$ </td><td>0.896784</td><td>0.6279</td><td>1.43</td><td>0.1535</td><td>1.10414</td></tr><tr><td>BetweennessCentrality</td><td> $\beta_9$ </td><td>4.430611</td><td>1.4428</td><td>3.07</td><td>0.0022</td><td>5.53823</td></tr><tr><td>In-degreeCentrality</td><td> $\beta_{10}$ </td><td>0.000119</td><td>0.000043</td><td>2.78</td><td>0.0055</td><td>6.71493</td></tr><tr><td>Out-degreeCentrality</td><td> $\beta_{11}$ </td><td>0.000041</td><td>0.000032</td><td>1.29</td><td>0.1970</td><td>5.91706</td></tr><tr><td>Tenure × NurseRatio</td><td> $\beta_{12}$ </td><td>0.17617</td><td>0.0232</td><td>7.58</td><td>&lt;0.0001</td><td>2.60558</td></tr><tr><td>Tenure × BetweennessCentrality</td><td> $\beta_{13}$ </td><td>0.04219</td><td>0.0593</td><td>0.71</td><td>0.4768</td><td>5.13269</td></tr><tr><td>RuralLocation × In-degreeCentrality</td><td> $\beta_{14}$ </td><td>0.002382</td><td>0.000325</td><td>7.33</td><td>&lt;0.0001</td><td>1.18172</td></tr><tr><td colspan="4"></td><td colspan="3">Adjusted R-square = 0.8327</td></tr></table>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$Access_{itc}$ $=\beta_{0}+\beta_{1}\log Lab_{i,t-1}+\beta_{2}\log Radio_{i,t-1}$ $+\beta_{3}\log Trans_{i,t-1}+\beta_{4}\text{Tenure}_{i,t}+\beta_{5}\text{Tenure}_{i,t}^{2}$ $+\beta_{6}\text{Rural}_{i}+\beta_{7}\text{logMarketShare}_{i}+\beta_{8}\text{NurseRatio}_{i}$ $+\beta_{9}\text{BetweennessCentrality}_{i,t}$ $+\beta_{10}\text{In-degreeCentrality}_{i,t}$ $+\beta_{11}\text{Out-degreeCentrality}_{i,t}$ $+\beta_{12}\text{Tenure}_{i,t}\times\text{NurseRatio}_{i}$ $+\beta_{13}\text{Tenure}_{i,t}\times\text{BetweennessCentrality}_{i,t}$ $+\beta_{14}\text{Rural}_{i}\times\text{In-degreeCentrality}_{i,t}+\varepsilon_{i,t}.$ (1)
</div>

Table 3 Estimation Results of Self-Service Channel Use

<table><tr><td>Variable</td><td>Coefficient</td><td>Estimate</td><td>Standard error</td><td>t value</td><td>Pr &gt; |t|</td><td>VIF</td></tr><tr><td>Intercept</td><td> $\beta_0$ </td><td>0.418433</td><td>0.6310</td><td>0.66</td><td>0.5073</td><td>0</td></tr><tr><td>LabServiceValue</td><td> $\beta_1$ </td><td>0.067369</td><td>0.0212</td><td>3.18</td><td>0.0015</td><td>2.04982</td></tr><tr><td>RadiologyServiceValue</td><td> $\beta_2$ </td><td>-0.0172</td><td>0.0321</td><td>-0.54</td><td>0.5921</td><td>2.89912</td></tr><tr><td>TranscriptionServiceValue</td><td> $\beta_3$ </td><td>0.020329</td><td>0.0365</td><td>0.56</td><td>0.5773</td><td>2.30513</td></tr><tr><td>Tenure</td><td> $\beta_4$ </td><td>0.014754</td><td>0.00804</td><td>1.84</td><td>0.0667</td><td>3.38458</td></tr><tr><td>Tenure $^2$ </td><td> $\beta_5$ </td><td>-0.00233</td><td>0.000517</td><td>-4.50</td><td>&lt;0.0001</td><td>1.77921</td></tr><tr><td>Rural</td><td> $\beta_6$ </td><td>-0.1461</td><td>0.3544</td><td>-0.41</td><td>0.6802</td><td>1.17519</td></tr><tr><td>MarketShare</td><td> $\beta_7$ </td><td>0.154933</td><td>0.0708</td><td>2.19</td><td>0.0288</td><td>1.10615</td></tr><tr><td>NurseRatio</td><td> $\beta_8$ </td><td>-0.66495</td><td>0.4718</td><td>-1.41</td><td>0.1590</td><td>1.10414</td></tr><tr><td>BetweennessCentrality</td><td> $\beta_9$ </td><td>2.156079</td><td>1.2824</td><td>1.68</td><td>0.0930</td><td>5.53823</td></tr><tr><td>In-degreeCentrality</td><td> $\beta_{10}$ </td><td>-0.00003</td><td>0.000038</td><td>-0.84</td><td>0.4010</td><td>6.71493</td></tr><tr><td>Out-degreeCentrality</td><td> $\beta_{11}$ </td><td>0.000012</td><td>0.000029</td><td>0.43</td><td>0.6678</td><td>5.91706</td></tr><tr><td>Tenure × NurseRatio</td><td> $\beta_{12}$ </td><td>0.091821</td><td>0.0205</td><td>4.48</td><td>&lt;0.0001</td><td>2.60558</td></tr><tr><td>Tenure × BetweennessCentrality</td><td> $\beta_{13}$ </td><td>0.14293</td><td>0.0666</td><td>2.14</td><td>0.0322</td><td>5.13269</td></tr><tr><td>Rural location × In-degreeCentrality</td><td> $\beta_{14}$ </td><td>0.00099</td><td>0.000288</td><td>3.43</td><td>0.0006</td><td>1.18172</td></tr><tr><td colspan="7">Adjusted R-square 0.6271</td></tr></table>

To choose between random or fixed effects estimation methods, we rely on the Hausman (1978) specification test. For both channels, the null hypothesis that individual effects are uncorrelated with the other independent variables in the model is not rejected $( p = 0 . 1 4 3$ and 0.148 respectively) and thus random effect method produces unbiased, consistent, and efficient estimates. Tables 2 and 3 present the random effects estimation results of Equation (1) for full- and self-service channels, respectively.

Note that because the set of independent variables in Tables 2 and 3 are both the same, the variance inflation factor (VIF) in the two models is also identical.

In-degree centrality captures the extent to which each practice receives patients from other practices who have already adopted HIE in each month. Outdegree centrality, on the other hand, reflects the extent to which each practice refers its patients to other practices. The business value of HIE for practices is realized when they receive, rather than refer, patients.

This is confirmed by the positive effects of in-degree centrality on the use of HIE through full-service channels. Thus, Hypothesis H1-2 is partially supported.

Betweenness centrality in the network of common physicians positively affects HIE use in the self-service channel; thus, Hypothesis H2-2 is also partially supported. However, we show in Table 4 that this measure is significant in increasing the efficiency of practices in coproduction of HIE services. In other words, although betweenness centrality does not directly affect the level of use through the selfservice channel, it increases the efficiency of practices in using the HIE system.

The interaction of tenure and betweenness centrality is positive and significant only in self-service channel use. The insignificance of the interaction in full-service channel use may be due to the minimal need for user involvement in HIE services. The positive effect of tenure on the relationship between betweenness centrality and HIE use is evident in the self-service channel. This partially supports Hypothesis H2-3. To better use the self-service channel, practices need to have enough time to learn from each other, however this may not be as critical in the fullservice channel. Location makes no difference in HIE use for the self-service or full-service channel. However, the interaction of rural location and in-degree centrality is positive and significant in both channels. This confirms that for rural practices that share patients with others, the use of HIE is even more significant. Thus, Hypothesis H1-4 is supported.

Different types of HIE services (lab reports, radiology reports, and hospital transcriptions) are of different value for different medical practices based on various factors including specialty, patient demographics, and physician preferences. The value of each of these three services is captured by the total number of transactions in two channels in previous months. The values of the three services are significant and positively affect the level of HIE use in both channels except the value of radiology reports and hospital transcriptions in using HIE through the selfservice channel. The other finding in the results is that while the ratio of nurses to physicians does not directly increase HIE use, the interaction of tenure and nurse ratio is positive and significant in both channels. This implies that the higher nurse ratio increases the effect of tenure on HIE use. Note also that the tenure of a practice with HIE positively affects its HIE use. This effect is statistically significant in the fullservice channel and partially significant in the selfservice channel.

Table 4 Analysis of Covariates of Practice Efficiency

<table><tr><td>Variable</td><td>Coefficient</td><td>Estimate</td><td>Std. dev.</td><td>t value</td><td>Pr &gt; |t|</td></tr><tr><td>Intercept</td><td> $\beta_0$ </td><td>0.41121</td><td>0.0515</td><td>7.99</td><td>&lt;0.0001</td></tr><tr><td>Tenure</td><td> $\beta_1$ </td><td>0.186897</td><td>0.0479</td><td>3.90</td><td>0.0001</td></tr><tr><td>Tenure $^{2}$ </td><td> $\beta_2$ </td><td>0.247343</td><td>0.0933</td><td>2.65</td><td>0.0081</td></tr><tr><td>BetweennessCentrality</td><td> $\beta_3$ </td><td>0.695872</td><td>0.8073</td><td>0.86</td><td>0.3889</td></tr><tr><td>BetweennessCentrality × Tenure</td><td> $\beta_4$ </td><td>0.819843</td><td>0.1752</td><td>4.68</td><td>&lt;0.0001</td></tr></table>

Adjusted R-square = 001004

Following the method described in the appendix, we construct measures of practice efficiency or in HIE service coproduction. We first regress channel use on all covariates in Equation (1) except those associated with customer efficiency. We use the standardized residuals from this regression to construct efficiency measures as described in Equations (15) and (16) in the appendix. To verify the effects of tenure and betweenness centrality on the computed practice efficiency, we regress the practice efficiency on Tenure, Tenure<sup>2</sup>, and BetweennessCentrality, and their interaction in model (2). In reality, the efficiency of practices increases by tenure until it reaches its maximum and then remains constant. If we had included the squared term of tenure in a linear model, after a certain point, the pure effects of tenure would turn out to be negative on practice efficiency. To address this issue, we design a nonlinear model that allows the effects of tenure to diminish gradually.<sup>6</sup>

$$
\begin{array}{l} \log (\text {PracticeEfficiency} _ {i t}) \\ = \log \left[ \beta_ {0} + \frac {\beta_ {1} \text {Tenure} _ {i t}}{\sqrt {1 + \beta_ {2} \text {Tenure} _ {i t} ^ {2}}} + \beta_ {3} \text {BetweennessCentrality} _ {i t} \right. \\ \left. + \beta_ {4} (\text {BetweennessCentrality} _ {i t} \times \text {Tenure} _ {i t}) + a _ {i} \right] \\ + u _ {i, t}. \end{array} \tag {2}
$$

We use a fixed effects model to control for unobserved variables that affect efficiency and change by practice but are constant over time. The validity of the fixed effects model is confirmed by performing the F -test on the hypothesis that there are no fixed effects. The null hypothesis of poolability is rejected (F -value = 42.51, p-value < 000001) and thus confirms that there are group effects, or time effects, or both. The results of estimating Equation (2) are presented in Table 4.

The significant effects of tenure and betweenness centrality on the level of practice efficiency in using HIE validate our analytical approach in measuring the latent practice efficiency by confirming the positive association between the measured efficiency and the variables that we logically expected to affect it. Note that in this formulation, the coefficient of $T e n u r e ^ { 2 }$ must be positive to ensure the nonnegativity of the term under the square root. This implies that the practices efficiency in coproducing HIE services will increase

Number of observations with right censored adoption time: 308 as they continue to learn how to use the system. When efficiency reaches a maximum level of involvement, it does not change thereafter. As hypothesized in Hypothesis H2-4, the positive effect of learning through informal interactions in the network of physicians on increasing the practice efficiency in using HIE is confirmed in the results of Table 4. Hypothesis H2-5 on the moderating effect of tenure on the relationship between betweenness centrality and efficiency is also supported.

We use a survival analysis method to test the hypotheses as to HIE adoption time. Two general approaches to survival analysis exist. The first deals with an event time and is known as the Accelerated Failure Time (AFT) model. The second deals with hazard rates and is known as the Proportionate Hazard model. AFT models use parametric estimation methods and allow us to test certain hypotheses about the shape of a hazard function. The proportionate hazard models use semiparametric methods to estimate the survival function whose interpretation may not be straightforward. Results indicate that AFT models have a significant advantage if the shape of the survival distribution is known as they provide more efficient estimates with smaller standard error. Finally, with AFT models it is much easier to predict event times with any specific set of covariates. We use the LIFEREG procedure in SAS software to estimate Equation (3). For a detailed description of the procedure see (Allison 2010).

log4TimeToAdopt<sub>i</sub>5

$$
= \beta_ {0} + \beta_ {1} \text { BetweennessCentrality } _ {i}
$$

$$
+ \beta_ {2} \text { In - degreeCentrality } _ {i} + \beta_ {3} \text { Out - degreeCentrality } _ {i}
$$

$$
+ \beta_ {4} R u r a l _ {i} + \beta_ {5} M a r k e t S h a r e _ {i}
$$

$$
+ \beta_ {6} \text { CommonPatientsWithLargePractices }
$$

$$
+ \beta_ {7} \text { CommonPhysiciansWithLargePractices }
$$

$$
+ \beta_ {8} I n - d e g r e e C e n t r a l i t y _ {i} \times R u r a l _ {i} + \varepsilon_ {i}.\tag{3}
$$

Because the practices were observed from the initiation of HEALTHeLINK, there is no left truncation in the data. In other words, there is no practice that has adopted HIE before the start date of our data collection. The right truncation exists because some practices had not adopted until the finish date of our study. Because all of the data providers have adopted HIE, the medical records ordered by every physician in the study population will be electronically sent to HIE servers. However, these records will only be accessible if the ordering doctor is a member of the HIE and the patient has provided consent. This allows us to operationalize all of the covariates in Equation (3). We calculate the network centralities based on all of the practices that a focal practice has ever shared patients with. This reflects the perceived benefits of HIE for a practice. Some practices may have not adopted HIE yet and thus joining will not result in immediate benefits for their peers. Other practices evaluate the potential benefits of HIE based on the assumption that all of the practices will eventually join under the pressure of state and federal regulations. Table 5 presents the results. The negative coefficients show a positive impact of model variables on reducing the time taken by a practice to adopt HIE.

According to the results of the survival analysis shown in Table 5, it takes less time for practices with higher betweenness centrality to adopt the system; thus, Hypothesis H2-1 is supported. The negative coefficient of in-degree centrality in the network of common patients shows that practices sharing more patients with others would adopt the HIE sooner than those that share less. This supports Hypothesis H1-1. Neither the rural location by itself nor its integration with in-degree centrality is significant; thus, Hypothesis H1-3 is not supported. The influence through common patients is not significant; thus, Hypothesis H3-1 is not supported. The coefficient of the ratio of common physicians with large practices to the total number of physicians is negative. Hence, the practices that are influenced by opinion leaders through common physicians adopt the HIE sooner than others. This confirms Hypothesis H3-2.

Table 5 Survival Analysis of Practice Adoption Time

<table><tr><td>Variable</td><td>Coefficient</td><td>Estimate</td><td>Standard error</td><td> $\chi^2$ </td><td>Pr &lt;  $\chi^2$ </td><td>VIF</td></tr><tr><td>Intercept</td><td> $\beta_0$ </td><td>7.6076</td><td>0.1981</td><td>1,474.59</td><td>&lt;0.0001</td><td>0</td></tr><tr><td>BetweennessCentrality</td><td> $\beta_1$ </td><td>-11.1848</td><td>3.4603</td><td>10.45</td><td>0.0012</td><td>1.02545</td></tr><tr><td>In-degreeCentrality</td><td> $\beta_2$ </td><td>-1.1340</td><td>0.5963</td><td>3.62</td><td>0.0572</td><td>1.09555</td></tr><tr><td>Out-degreeCentrality</td><td> $\beta_3$ </td><td>-0.0030</td><td>0.0127</td><td>0.05</td><td>0.8153</td><td>2.58271</td></tr><tr><td>RuralLocation</td><td> $\beta_4$ </td><td>0.0371</td><td>0.1758</td><td>0.04</td><td>0.8330</td><td>4.66247</td></tr><tr><td>MarketShare</td><td> $\beta_5$ </td><td>-0.0406</td><td>0.0271</td><td>2.24</td><td>0.1344</td><td>1.02262</td></tr><tr><td>CommonPatientsWithLargePractices</td><td> $\beta_6$ </td><td>-0.1772</td><td>0.2680</td><td>0.44</td><td>0.5085</td><td>1.05053</td></tr><tr><td>CommonPhysiciansWithLargePractices</td><td> $\beta_7$ </td><td>-0.0001</td><td>0.0000</td><td>17.68</td><td>&lt;0.0001</td><td>1.00552</td></tr><tr><td>In-degreeCentrality × RuralLocation</td><td> $\beta_8$ </td><td>0.2405</td><td>3.7780</td><td>0.00</td><td>0.9492</td><td>4.61348</td></tr></table>

## 6. Discussion and Conclusion

Health information technology in general, and HIE in particular, is an inevitable part of reforms currently under way in the national healthcare system. An HIE will provide unique opportunities to increase the quality of healthcare services and, at the same time, significantly reduce healthcare costs. Healthcare payers including state and federal governments as well as private insurance companies have realized the benefits and potentials of HIE systems and are now vigorously advocating them.

Despite the proven advantages of HIE, the nationwide adoption rate is still not promising. Medical information is of high business value for practices. Sharing such information with competitors is considered a risk to strategic market advantage. Practices may also be reluctant to use the HIE because they do not see any direct financial benefit. These and other attitudes negatively affect the level of HIE use among physicians. Technology savvy physicians may be more willing to accept the new technology than their nonsavvy peers. Finally, HIE provides a transparent management and control tool for insurance companies. This is not necessarily encouraging for many physicians who enjoy the independence that their high position in the medical hierarchy provides.

The main goal of HIE platforms is to connect healthcare providers to each other and enable them to share medical records in a timely and cost-effective manner. Therefore, network externalities are crucial in realizing the potential of HIE platforms. Emerging forms of healthcare organizations such as Accountable Care Organizations (ACOs) and Managed Care Organizations (MCOs) can use the findings of this study to efficiently monitor, control, and reduce the costs of their operations. Next we discuss the practical implications of our work.

## 6.1. Practical Implications

We have empirically shown that the practices with a higher number of shared patients, larger market share, and higher dependency on major practices will adopt HIE faster than others. Moreover, we show the effects of learning through experience and peers on enhancing the involvement of practices in HIE service coproduction. These two findings provide grounds for creating strategies to not only increase HIE adoption but also to enhance the actual use of HIE services by practices. Although there is an abundance of studies in the literature on the effects of social networks on adoption and use of new innovations, we have taken a new approach using degree centrality to capture the network externality and its effect on enhancing the potential value of HIE for members. The paper also provides new insights on the importance of peer influence and the role of learning from other physicians in the HIE market. To our knowledge, this is the first rigorous study of the effects of large practices on driving HIE adoption. Considering the fact that HIE platforms in the nation have not been successful in growing their membership base and increasing their use, this paper will be of interest to practitioners who would like to promote these platforms. The paper provides clear recommendations on identifying the practices that can create the highest externality in the network, impact the others’ decision to join, and diffuse the knowledge about HIE to the others.

HEALTHeLINK does not have a unique data architecture or an exclusive operational model to distinguish it from the majority of publicly sponsored RHIOs. In fact, its success in attracting new members and increasing its use among the providers in Western New York supports the credibility of the suggestions provided here as tested strategies for success. The main contribution of this research is highlighting the effects of degree and betweenness centralities in the networks of common patients and physicians on increasing the adoption and use of HIE. This study calls for attention to the multisided nature of HIE and reveals the importance of members in increasing value and diffusing knowledge about HIE. Although HEALTHeLINK only allows sharing of a limited set of medical documents, we still show the prominent influence of these factors on its adoption and use by medical providers.

HEALTHeLINK has recently implemented new technologies that enable practices to share Continuity of Care Documents (CCD) among themselves. Over the time period of our study, this feature was not yet fully functional and the participation of practices in this type of exchange was minimal. With enough participating practices in the near future, consideration of the level of shared CCDs in the use model can add more insights to the analysis results. As the number of HIE functionalities grows, we do not see any reason for these externalities to weaken or fade. Degree centrality will still be important because the value of full functioning HIEs will increase for those practices who share patients with others. In fact, the advanced feature of practice-to-practice sharing of medical records increases the importance of degree centrality in driving the value of HIE for practices. For advanced HIEs, betweenness centrality also becomes more important because learning about all of the advanced functionalities will logically be more challenging. Given the unsatisfactory state of the HIE platforms through the

United States, the results of this study will be of interest to the HIEs that struggle with the long-term question of “value.” Regardless of the type of medical documents, reinforcement of network externality will lead to more available data on the HIE platforms and thus increases their value to potential members.

## 6.2. Future Research

Interoperability of EHR systems is one of the main obstacles of HIE growth. Healthcare providers will be unable to use HIE to its full extent unless they have fully functional and interoperable EHR systems that can smoothly connect to HIE to share medical documents. The practices in Western New York use 15 different types of EMR systems of which a dozen can easily operate with the HEALTHeLINK system and directly import medical data from HIE systems into their internal database. In other words, although interoperability may be an issue in the overall growth of HIE, it is not a major obstacle in the case that we have studied. Moreover, for practices that do not have an interoperable EMR or even do not have an EMR, HEALTHeLINK provides its services through a Web portal called Virtual Health Record (VHR) in which participating practices can view and download patient records regardless of their EMR systems. In our paper, we refer to this system as a self-service channel. Although it takes more time to find and download the patient records through this channel, it solves the interoperability issue to a large extent. In our study, the existence of a VHR system that allows access to HIE without requiring an interoperable EHR system resolves the issue of interoperability. However, in many cases, HIEs do not provide this alternative channel and thus their value for providers depends on the interoperability of their EHR systems with HIEs. This will naturally affect their decision to adopt HIE and their level of HIE use and thus should be considered an important construct in the diffusion models. Investigating the magnitude of the effects of EHR interoperability on HIE adoption and use is an interesting area of research. RHIOs can provide interoperable EHR systems to their members as a complementary product to motivate the adoption and increase the use of their services. The analysis of the costs and benefits of implementing these policies can be a subsequent study.

The policies of payers such as Medicare, Medicaid, and other health insurance companies may largely affect the adoption and use of HIE. With the advent of new payment plans, such as pay for performance, and the appearance of new types of healthcare organizations such as ACOs, providers face a greater need to increase the quality and decrease the cost of their services by adoption and use of HIE. This study does not focus on the relationship between payers and providers and its effect of HIE adoption and use; over the period in which the data was collected, these policies were not in effect. Moreover, the specific details of payment policies and agreements between payers and providers are generally confidential. Access to this data will allow further research on the effects of these policies on HIE adoption, use, and subsequent effects on the quality and costs of healthcare services.

Some of the important areas of future research include measurement and assessment of the effectiveness of HIE platforms in yielding better care for the patients, lower costs of healthcare delivery, and improved coverage of the services. HEALTHeLINK, like many other public RHIOs, is currently supported by funds from the government, state, and its stakeholders. It does not charge its members for the services it provides. To be financially sustainable, HIE platforms have to design viable charging fees for their services. Analyzing adoption and use trends in networks, such as SureScript<sup>®</sup>, which already has a sustainable and successful business plan and which generates revenue by charging their members, is a promising area of future research to provide insights for HIE platforms and help them in designing similar business plans. In healthcare research, the severity of patients’ conditions is generally controlled by the Charlson (1987) comorbidity index, which is available through claims data sets filed by payers. Studying the effects of patients’ conditions on HIE use by practices can add more insights to this area of research. These avenues of research are rooted in analytical modeling and empirical investigations of revenue, and yield management strategies for an HIE. We are currently pursuing some of these research directions.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2014.0547.

## Acknowledgments

The results presented in this article rely on the data collected at HEALTHeLINK. The authors thank Daniel Porreca for his support.

## Appendix

## Measurement of Practice Efficiency in HIE Service Coproduction

Following Xue et al. (2007), we develop an analytical model based on the Cobb-Douglas production function which considers HIE use as a function not only of firm inputs but also customer inputs and characteristics. We show how this model can be applied to measure the efficiencies of practices in using an HIE system as a latent variable that otherwise cannot be measured directly. Our model is distinguished from Xue et al. (2007) in two major dimensions. First, our unit of analysis is a practice rather than an individual, and thus results in an entirely different operationalization of model variables. Second, we model efficiency as a time dependent variable. By applying panel data, we let the efficiencies of practices in using different HIE services vary over time. We model efficiency as a dynamic variable that is different from the fixed and static characterization in the literature and is a generalization of this concept. This approach will capture time dependent factors such as learning and field experiences that may affect long-term efficiency. Our principal empirical task is to construct suitable surrogates for each practice so that we can: (a) isolate practice efficiency from other factors that affect channel choice, and (b) provide support to the claim that our definition of practice efficiency is measuring what we expect by demonstrating that it is correlated with factors that are plausibly associated with efficiency. In this analysis, we denote each of the two channels of access (full- and self-service) by $C _ { c }$ in which $c \in \{ 1 , 2 \}$ . We consider each of the three medical reports (lab reports, radiology reports, and hospital transcriptions) as a service and denote them by $j \in \{ 1 , 2 , 3 \}$ . The cost of labor for a practice is w (e.g., time opportunity cost) per unit of input labor $( { L _ { c j } } )$ and the value of the service is v per unit of output $( O _ { c j } )$ . Service value is independent of the channel through which the service is acquired but differs by service (e.g., lab reports may be more important to a set of specific practices, as compared to hospital transcripts). We also allow service value and labor cost to change over time. Thus, a practice’s utility of using channel c at time t to receive $O _ { c j }$ of type j medical records is

$$
U _ {c j, t} = v _ {j, t} O _ {c j, t} - w _ {t} L _ {c j, t}.\tag{4}
$$

In Equation (4) we denote the utility of each service through each channel to be a time dependent variable. The total utility for each practice at each period of time is the sum of the utility of receiving each of the medical records through all of the channels. Thus

$$
U _ {t} = \sum_ {c} \sum_ {j} U _ {c j, t}.\tag{5}
$$

Let the production inputs for channel and service type be indicated as practice-invested capital (R), practice labor (L), HIE platform invested capital (K), and HIE platform employee labor (H), respectively. Assuming that the effects of practice inputs and HIE platform inputs are in multiplicative form, this yields an overall production function for service of type j in channel c at time t (or output $O _ { c j , t } )$ of the form

$$
O _ {c j, t} = g _ {c} (R _ {c, t}, L _ {c j, t}) f _ {c} (K _ {c, t}, H _ {c, t}).\tag{6}
$$

Where $f _ { c } ( K _ { c , t } , H _ { c , t } )$ is a function of labor and capital by the HIE platform which are likely to be slow changing and is quasifixed for every practice in our analysis. We model the practice portion of the production function using a Cobb-Douglas format as follows:

$$
g _ {c} (R _ {c, t}, L _ {c, t}) = R _ {c, t} ^ {\alpha_ {c}} (A _ {c, t} L _ {c j, t}) ^ {\beta_ {c}},\tag{7}
$$

where $\alpha _ { c }$ and $\beta _ { c }$ are the output elasticity of practice capital and practice labor, respectively, and $A _ { c , t }$ is a time varying practice-specific factor that affects the practice’s productivity of labor when using channel c at time t. At each time period a practice chooses an effort level and a capital level for each channel that maximizes its overall utility, thus

$$
\max _ {L _ {c, t}} U _ {c, t} = \max _ {L _ {c j, t}} \sum_ {j = 1} ^ {J} \bigl (v _ {j, t} O _ {c j, t} - w _ {t} L _ {c j, t} \bigr).\tag{8}
$$

This leads to a set of first order equations such that optimum level of $L _ { c j , t }$ is computed as

$$
L _ {c j, t} ^ {*} = \left(L _ {c j, t} \Big | \frac {\partial O _ {c j , t}}{\partial L _ {c j , t}} = \frac {w _ {t}}{v _ {j , t}}\right).\tag{9}
$$

Now if we differentiate $O _ { c j , t }$ with respect to $L _ { c j , t }$ and substituting the ${ L _ { c j , t } } ^ { * }$ in that we will have

$$
\begin{array}{r} \frac {\partial O _ {c j}}{\partial L _ {c j , t}} = \frac {\partial R _ {c , t} ^ {\alpha_ {c}} (A _ {c , t} L _ {c j , t}) ^ {\beta_ {c}} f _ {c} (K _ {c , t} , H _ {c , t})}{\partial L _ {c j , t}} \\ = \beta_ {c} R _ {c, t} ^ {\alpha_ {c}} A _ {c, t} ^ {\beta_ {c}} L _ {c j, t} ^ {\beta_ {c} - 1} f _ {c} (K _ {c, t}, H _ {c, t}) = \frac {w _ {t}}{v _ {j , t}}, \end{array}\tag{10}
$$

$$
L _ {c j, t} ^ {*} = \left[ \beta_ {c} R _ {c, t} ^ {\alpha_ {c}} A _ {c, t} ^ {\beta_ {c}} f _ {c} (K _ {c, t}, H _ {c, t}) \frac {v _ {j , t}}{w _ {t}} \right] ^ {1 / (1 - \beta_ {c})}.\tag{11}
$$

In the above formula, ${ L _ { c j , t } } ^ { * }$ implies the optimal labor choice for channel c at time t. Substituting this back into the original production function yields:

$$
\begin{array}{l} O _ {c j, t} = g _ {c} (R _ {c, t}, L _ {c j, t}) f _ {c} (K _ {c, t}, H _ {c, t}) \\ \quad = R _ {c, t} ^ {\alpha_ {c} / (1 - \beta_ {c})} A _ {c, t} ^ {\beta_ {c} / (1 - \beta_ {c})} \beta_ {c} ^ {\beta_ {c} / (1 - \beta_ {c})} f _ {c} (K _ {c, t}, H _ {c, t}) ^ {1 / (1 - \beta_ {c})} \\ \cdot w _ {t} ^ {\beta_ {c} / (\beta_ {c} - 1)} v _ {j, t} ^ {\beta_ {c} / (1 - \beta_ {c})}. \end{array}\tag{12}
$$

Since $\begin{array} { r } { { O _ { c , t } } ^ { * } = \sum _ { j } O _ { c j , t } } \end{array}$ then

$$
\begin{array}{l} O _ {c, t} ^ {*} = R _ {c, t} ^ {\alpha_ {c} / (1 - \beta_ {c})} A _ {c, t} ^ {\beta_ {c} / (1 - \beta_ {c})} \beta_ {c} ^ {\beta_ {c} / (1 - \beta_ {c})} f _ {c} (K _ {c, t}, H _ {c, t}) ^ {1 / (1 - \beta_ {c})} \\ \cdot w _ {t} ^ {\beta_ {c} / (\beta_ {c} - 1)} \sum_ {j} v _ {j, t} ^ {\beta_ {c} / (1 - \beta_ {c})}. \end{array}\tag{13}
$$

In the logarithmic format we will have

$$
\begin{array}{l} \log O _ {c, t} ^ {*} = \frac {\alpha_ {c}}{1 - \beta_ {c}} \log R _ {c, t} + \frac {\beta_ {c}}{1 - \beta_ {c}} \log A _ {c, t} + \frac {\beta_ {c}}{1 - \beta_ {c}} \log \beta_ {c} \\ \quad + \frac {1}{1 - \beta_ {c}} \log f _ {c} (K _ {c, t}, H _ {c, t}) + \frac {\beta_ {c}}{\beta_ {c} - 1} \log w _ {t} \\ \quad + \log \sum v _ {j, t} ^ {\beta_ {c} / (1 - \beta_ {c})}. \end{array} \tag {14}
$$

Thus at every time period t each practice will use each channel (full- and self-service) to receive a number of medical documents $O _ { c } { ^ * }$ . The number of such documents is a function of capital $\boldsymbol { R } _ { c } ,$ efficiency $A _ { c } ,$ , HIE platform inputs in channels $f _ { c } ( \bar { K _ { c } } , H _ { c } )$ , unit cost of customer labor w, and the value of each type of medical records $v _ { j }$

The number of medical records received by each practice can be regressed on the measures of practice capital $R _ { c } ,$ practice effort costs w, and medical record value $v _ { j } .$ . The efficiency measures can then be obtained as the residual of the resulting regression equation. This approach to measuring efficiency has been previously used by well-known economists such as Griliches (1994) to measure the economical productivity of agents in different micro- and macroeconomic contexts.

$$
\begin{array}{l} \log O _ {c, t} ^ {*} = \frac {\alpha_ {c}}{1 - \beta_ {c}} \log R _ {c, t} + \frac {\beta_ {c}}{1 - \beta_ {c}} \log \beta_ {c} \\ \qquad + \frac {1}{1 - \beta_ {c}} \log f _ {c} (K _ {c, t}, H _ {c, t}) + \frac {\beta_ {c}}{\beta_ {c} - 1} \log w _ {t} \\ \qquad + \log \sum v _ {j, t} ^ {\beta_ {c} / (1 - \beta_ {c})} + \varepsilon_ {t}. \end{array}\tag{15}
$$

In the regression equation above, $\pmb { \varepsilon } _ { t } = [ \beta _ { c } / ( 1 - \beta _ { c } ) ] \log { A _ { c , t } }$ and thus $\overset { \cdot } { A _ { c , t } } = \varepsilon _ { t } ^ { ( 1 - ^ { \bullet } \beta _ { c } ) / \beta _ { c } }$

Three issues arise from directly using the residuals as a measure of practice efficiency. (1) The regression equation is derived for each channel separately; greater precession may be obtained if we aggregate the residuals from all of the channels. (2) The unobservable practice characteristics may affect its choice of channel and thus the observed residual may include an error term s that can be practice-specific fixed or random effect. Thus we will have $\varepsilon _ { t } ^ { \prime } = [ \beta _ { c } / ( 1 - \beta _ { c } ) ] \log A _ { c , t } + s _ { t } .$ . (3) The production function applies to all channels, though the level and extent of a practice’s participation can vary substantially. As explained earlier, we expect the amount of practice labor input in a full-service channel to be smaller than that in a self-service channel to access a type of medical record. This implies a low elasticity of labor input in a full-service channel and, therefore, minimal variation in full service channel use due to the direct effect of efficiency. However, the full-service channel use may be helpful in estimating individual effects so they can be usefully incorporated into a composite efficiency measure as shown in Equation (16).

To address the above three issues, we construct a customer efficiency measure for each practice at every time period as the difference between efficiency in using selfservice channel $C ^ { \prime \prime }$ and full-service channel $C ^ { \prime }$

$$
C E _ {t} = \theta_ {C ^ {\prime \prime}} \varepsilon_ {t, C ^ {\prime \prime}} - \theta_ {C ^ {\prime}} \varepsilon_ {t, C ^ {\prime}}.\tag{16}
$$

The optimal weights are theoretically related to the variance of each residual and are proportional to the marginal product of labor in each type of channel through $\beta _ { c } / ( 1 - \beta _ { c } )$ 5.

## References

Adler-Milstein J, Bates DW, Jha AK (2011) A survey of health information exchange organizations in the United States: Implications for meaningful use. Ann. Internal Medicine 154(10): 666–671.

Adler-Milstein J, DesRoches CM, Jha AK (2011) Health information exchange among U.S. hospitals. Amer. J. Managed Care 17(11):761–768.

Allison PD (2010) Survival Analysis Using SAS: A Practical Guide (SAS Inst, Cary, NC).

Amatayakul M (2008) Think a privacy breach couldn’t happen at your facility? Think again. Healthcare Financial Management: J. Healthcare Financial Management Assoc. 62(5):100–101.

Aron R, Dutta S, Janakiraman R, Pathak PA (2011) The impact of automation of systems on medical errors: Evidence from field research. Inform. Systems Res. 22(3):429–446.

Baicker K, Skinner JS (2010) Tax Policy and Economy, Vol. 25 (University of Chicago Press, Chicago).

Bampo M, Ewing MT, Mather DR, Stewart D, Wallace M (2008) The effects of the social structure of digital networks on viral marketing performance. Inform. Systems Res. 19(3):273–290.

Bates DW, Bitton A (2010) The future of health information technology in the patient-centered medical home. Health Affairs 29(4):614–621.

Bloom BS (2002) Crossing the quality chasm: A new health system for the 21st century. JAMA: J. Amer. Medical Assoc. 287(5): 646–647.

Blumenthal D, Tavenner M (2010) The “meaningful use” regulation for electronic health records. New England J. Medicine 363(6): 501–504.

Boyer KK, Hallowell R, Roth AV (2002) E-services: Operating strategy—a case study and a method for analyzing operational benefits. J. Oper. Management 20(2):175–188.

Briggs B (2003) The history of networks in health care. Health Data Management 11(3):36.

Buntin MB, Burke MF, Hoaglin MC, Blumenthal D (2011) The benefits of health information technology: a review of the recent literature shows predominantly positive results. Health Affairs 30(3):464–471.

Casalino L, Gillies RR, Shortell SM, Schmittdiel JA, Bodenheimer T, Robinson JC, Rundall T, Oswald N, Schauffler H, Wang MC (2003) External incentives, information technology, and organized processes to improve health care quality for patients with chronic diseases. JAMA: J. Amer. Medical Assoc. 289(4):434–441.

Charlson ME, Pompei P, Ales KL, MacKenzie CR (1987) A new method of classifying prognostic comorbidity in longitudinal studies: Development and validation. J. Chronic Diseases 40(5):373–383.

Chellappa RK, Saraf N (2010) Alliances, rivalry, and firm performance in enterprise systems software markets: A social network approach. Inform. Systems Res. 21(4):849–871.

Chernew ME, Baicker K, Hsu J (2010) The specter of financial armageddon health care and federal debt in the United States. New England J. Medicine 362(13):1166–1168.

Coleman JS, Katz E, Menzel H (1966) Medical Innovation: A Diffusion Study (Bobbs-Merrill, New York).

Corrigan JM, Greiner A, Erickson SM (2002) Fostering Rapid Advances in Health Care: Learning from System Demonstrations (National Academies Press, Washington, DC).

Davis GF (1991) Agents without principles? The spread of the poison pill through the intercorporate network. Admin. Sci. Quart. 36(4):583–613.

Davis K, Schoen C, Stremikis K, Fund C (2010) Mirror, mirror on the wall: How the performance of the U.S. health care system compares internationally: 2010 update, Commonwealth Fund. http://www.commonwealthfund.org/publications/fund -reports/2010/jun/mirror-mirror-update.

DiMaggio PJ (1988) Interest and agency in institutional theory. Zucker LG, ed. Research in Institutional Patterns Environment and Culture (Ballinger, Cambridge, MA), 3–22.

DiMaggio PJ, Powell WW (1983) The iron cage revisited: Institutional isomorphism and collective rationality in organizational fields. Amer. Sociol. Rev. 48(2):147–160.

Edwards A, Hollin I, Barry J, Kachnowski S (2010) Barriers to cross– institutional health information exchange: A literature review. J. Healthcare Inform. Management: JHIM 24(3):22–34.

Fontaine P, Zink T, Boyle RG, Kralewski J (2010) Health information exchange: Participation by Minnesota primary care practices. Arch. Intern Medicine 170(7):622–629.

Fuchs VR (1968) The Service Economy (National Bureau of Economic Research, Cambridge, MA).

Gardner BD, Warner JE (1994) Two steps forward-one step back. Choices 9(1):5–9.

Grewal R, Lilien GL, Mallapragada G (2006) Location, location, location: How network embeddedness affects project success in open source systems. Management Sci. 52(7):1043–1056.

Griliches Z (1994) Productivity, R&D, and the data constraint. Amer. Econom. Rev. 84(1):1–23.

Grossman JM, Bodenheimer TS, McKenzie K (2006) Hospitalphysician portals: The role of competition in driving clinical data exchange. Health Affairs 25(6):1629–1636.

Grossman JM, Kushner KL, November EA, LTHPOLICY PC (2008) Creating Sustainable Local Health Information Exchanges: Can Barriers to Stakeholder Participation Be Overcome? (Center for Studying Health System Change, Washington, DC).

Gurˇau C (2002) E-banking in transition economies: The case of Romania. J. Financial Services Marketing 6(4):362–378.

Gurbaxani V (1990) Diffusion in computing networks: The case of BITNET. Comm. ACM 33(12):65–75.

Hall RH, Quinn RE (1984) State expansion and organizational fields. Organ. Theory Public Policy 147–161.

Hausman JA (1978) Specification tests in econometrics. Econometrica: J. Econometric Society 46(6):1251–1271.

Jensen TB, Aanestad M (2006) How healthcare professionals “make sense” of an electronic patient record adoption. Inform. Systems Management 24(1):29–42.

Johnson KB, Unertl KM, Chen Q, Lorenzi NM, Nian H, Bailey J, Frisse M (2011) Health information exchange usage in emergency departments and clinics: The who, what, and why. J. Amer. Medical Informatics Assoc. 18(5):690–697.

Kane GC, Alavi M (2008) Casting the net: A multimodal network perspective on user-system interactions. Inform. Systems Res. 19(3):253–272.

Kane GC, Labianca GJ (2011) IS avoidance in health-care groups: A multilevel investigation. Inform. Systems Res. 22(3):504–522.

Kelley SW, Donnelly JH, Skinner SJ (1990) Customer participation in service production and delivery. J. Retailing 66(3):315–335.

Kraut RE, Rice RE, Cool C, Fish RS (1998) Varieties of social influence: The role of utility and norms in the success of a new communication medium. Organ. Sci. 9(4):437–453.

Kwon TH (1990) A diffusion of innovation approach to MIS infusion: Conceptualization, methodology, and management strategies. Proc. Eleventh Internat. Conf. Inform. Systems (Association for Computing Machinery, New York), 139–147.

Lassila KS, Pemble KR, DuPont LA, Cheng RH (1997) Assessing the impact of community health information networks: A multisite field study of the Wisconsin health information network. Topics Health Inform. Management 18(2):64–76.

Lenert L, Sundwall D, Lenert ME (2012) Shifts in the architecture of the nationwide health information network. J. Amer. Medical Informatics Assoc. 19(4):498–502.

Lewis WR, Wakerly RT (1995) CHINs (community health information networks): Fad or destiny? Healthcare Inform. Management: J. Healthcare Inform. Management Systems Society Amer. Hospital Assoc. 9(2):5–7.

Loh L, Venkatraman N (1992) Diffusion of information technology outsourcing: Influence sources and the Kodak effect. Inform. Systems Res. 3(4):334–358.

Lorenzi NM (2003) Strategies for Creating Successful Local Health Information Infrastructure Initiatives (Vanderbilt University, Nashville, TN).

Malepati S, Kushner K, Lee JS (2007) RHIOs and the value proposition: Value is in the eye of the beholder. J. AHIMA 78(3):24–29.

Martin AB, Lassman D, Washington B, Catlin A (2012) Growth in U.S. health spending remained slow in 2010; Health share of gross domestic product was unchanged from 2009. Health Affairs 31(1):208–219.

McClellan M, McKethan AN, Lewis JL, Roski J, Fisher ES (2010) A national strategy to put accountable care into practice. Health Affairs 29(5):982–990.

McLeod R Jr, Fuerst WL (1982) Marketing the MIS during times of resource scarcity. MIS Quart. 6(3):45–54.

Mcllwain K, Lassetter JS (2009) Building sustainable hies. Health Management Tech. 30(2):8–11.

Mehra A, Kilduff M, Brass DJ (2001) The social networks of high and low self-monitors: Implications for workplace performance. Admin. Sci. Quart. 46(1):121–146.

Melnick G, Keeler E (2007) The effects of multi-hospital systems on hospital prices. J. Health Econom. 26(2):400–413.

Menon NM, Lee B, Eldenburg L (2000) Productivity of information systems in the healthcare industry. Inform. Systems Res. 11(1): 83–92.

Nakamura MM, Ferris TG, DesRoches CM, Jha AK (2010) Electronic health record adoption by children’s hospitals in the United States. Arch. Pediatrics Adolescent Medicine 164(12):1145–1151.

Overhage JM, Dexter PR, Perkins SM, Cordell WH, McGoff J, McGrath R, McDonald CJ (2002) A randomized, controlled trial of clinical information shared from another institution. Ann. Emergency Medicine 39(1):14–23.

Paul LS (1995) IDS vs. CHIN: The great debate. Infocare (May):42,44.

Payton FC, Ginzberg MJ (2001) Interorganizational health care systems implementations: An exploratory study of early electronic commerce initiatives. Health Care Management Rev. 26(2):20–32.

Poissant L, Pereira J, Tamblyn R, Kawasumi Y (2005) The impact of electronic health records on time efficiency of physicians and nurses: A systematic review. J. Amer. Medical Informatics Assoc. 12(5):505–516.

Rogers EM (1962) Diffusion of Innovations (Free Press, New York).

Rogers EM, Kincaid DL (1981) Communication Networks: Toward a New Paradigm for Research (Free Press, New York).

Ross SE, Schilling LM, Fernald DH, Davidson AJ, West DR (2010) Health information exchange in small-to-medium sized family medicine practices: Motivators, barriers, and potential facilitators of adoption. Internat. J. Medical Informatics 79(2):123–129.

Rubin RD (2003) The community health information movement: Where it’s been, where it’s going. Public Health Informatics Inform. Systems 31(1):595–616.

Sasidharan S, Santhanam R, Brass DJ, Sambamurthy V (2012) The effects of social network structure on enterprise systems success: A longitudinal multilevel analysis. Inform. Systems Res. 23(3-Part-1):658–678.

Scalise DA (2006) Primer for building RHIOs. Hospitals Health Networks 80:49–53.

Sipkoff M (2010) HIEs are slow going but critical part of HIT. Managed Care 19(March):30–34.

Solomon MR (2007) Regional health information organizations: A vehicle for transforming health care delivery? J. Medical Systems 31(1):35–47.

Squazzo JD (2007) The state of regional health information organizations: Health data exchange on the rise. Healthcare Executive 22(5):8–10.

Stark MJ, Gregan SL, Allen PW (1996) The Iowa CHMIS: Work in progress. J. Ambulatory Care Management 19(1):98–104.

Starr P (1997) Smart technology, stunted policy: Developing health information networks. Health Affairs 16(3):91–105.

Terry K (2006) The rocky road to RHIOs. Medical Econom. 83(4): TCP8–TCP10.

Tucker C (2008) Identifying formal and informal influence in technology adoption with network externalities. Management Sci. 54(12):2024–2038.

U.S. Congress: Office of Technology Assessment (1995) Bringing healthcare online: The role of information technologies.

Venkatesh V, Zhang X, Sykes TA (2011) “Doctors do too little technology”: A longitudinal field study of an electronic healthcare system implementation. Inform. Systems Res. 22(3):523–546.

Vest JR, Gamm LD (2010) Health information exchange: Persistent challenges and new strategies. J. Amer. Medical Informatics Assoc. 17(3):288–294.

Walker J, Pan E, Johnston D, Adler-Milstein J, Bates DW, Middleton B (2005) The value of health care information exchange and interoperability. Health Affairs Jan–Jun(suppl):W5-10–W5-18.

Wang YS, Wang YM, Lin HH, Tang TI (2003) Determinants of user acceptance of Internet banking: An empirical study. Internat. J. Service Indust. Management 14(5):501–519.

Whitaker GP (1980) Coproduction: Citizen participation in service delivery. Public Administration Rev. 40(3):240–246.

Williams C, Mostashari F, Mertz K, Hogin E, Atwal P (2012) From the office of the national coordinator: The strategy for advancing the exchange of health information. Health Affairs 31(3):527–536.

Xue M, Harker PT (2002) Customer efficiency concept and its impact on e-business management. J. Service Res. 4(4):253–267.

Xue M, Hitt LM, Chen P (2011) Determinants and outcomes of Internet banking adoption. Management Sci. 57(2):291–307.

Xue M, Hitt LM, Harker PT (2007) Customer efficiency, channel usage, and firm performance in retail banking. Manufacturing Service Oper. Management 9(4):535–558.

Yaraghi N, Du AY, Sharman R, Gopal RD, Ramesh R (2013) Network effects in health information exchange growth. ACM Trans. Management Inform. Systems (TMIS) 4(1):1–26.

Yaraghi N, Du AY, Sharman R, Gopal RD, Ramesh R, Singh R, Singh G (2014) Professional and geographical network effects on healthcare information exchange growth: Does proximity really matter? J. Amer. Medical Informatics Assoc. 21(4):671–678.
