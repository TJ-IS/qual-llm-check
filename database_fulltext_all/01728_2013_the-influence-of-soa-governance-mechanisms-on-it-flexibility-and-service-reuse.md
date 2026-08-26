---
otero_id: 1728
otero_key: "QEESVCME"
title: "The influence of SOA governance mechanisms on IT flexibility and service reuse"
authors: "Nils Joachim; Daniel Beimborn; Tim Weitzel"
year: "2013"
journal: "The Journal of Strategic Information Systems"
doi: "10.1016/j.jsis.2012.10.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The influence of SOA governance mechanisms on IT flexibility and service reuse ☆

Nils Joachim ⇑, Daniel Beimborn, Tim Weitzel

Department of Information Systems and Services, University of Bamberg, An der Weberei 5, 96047 Bamberg, Germany

## a r t i c l e i n f o

Article history: Available online 3 January 2013

Keywords: Service-oriented architecture (SOA) SOA governance IT governance Flexibility Modularity Reuse Survey

## a b s t r a c t

While many firms have introduced SOA, only one in five have achieved anticipated benefits such as increased IT flexibility or reuse. Industry analysts assume that a lack of SOA governance is the main reason why SOA projects fail. Addressing the substantial research gap on SOA governance this paper theoretically and empirically investigates which SOA governance mechanisms are needed to achieve the benefits of SOA, such as increasing IT flexibility and reusing services. The proposed theoretical SOA governance model is evaluated using data from 81 SOA-using organizations.

Overall, the results confirm the relevance of a variety of SOA governance mechanisms (structures, processes, and employees/relations), but at the same time, that IT infrastructure flexibility and service reuse are influenced by different mechanisms. Key governance mechanisms that show a strong effect on infrastructure flexibility are using standards, service management processes, educating employees, and IT/business communication while reuse can only be increased through service management, standards and qualification. Contrary to expectations, implementing new, dedicated decision-making bodies for SOA hampers organizations in achieving higher degrees of IT flexibility and reuse, and a firm is better off using existing IT decision-making bodies.

\- 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Many firms report that their SOA projects have failed to realize the expected benefits from servitization. Industry analysts propose that the ‘‘main reason SOA projects fail is because there is a lack of governance’’ (Saran, 2006). As the maturing academic literature on development and implementation of service-oriented architectures (SOAs) has so far mostly investigated important technical aspects of SOA, there is a dearth of research on SOA governance and its mechanisms. A recent literature review reveals that ‘‘organization and governance’’ is addressed in only 4 out of 175 SOA research articles and calls for future research on ‘‘how organizations should apply the SOA concept’’ (Viering et al., 2009, p. 46). The importance of SOA governance also comes up in a Forrester Research study, which finds that only 20% of surveyed organizations achieve all anticipated SOA benefits, while 50% achieve less or struggle to reap the expected benefits (Heffner, 2009). Thus, a relevant question for researchers and practitioners alike is how to achieve the benefits expected from adopting SOA

While the potential benefits are well understood and include increasing IT infrastructure flexibility (e.g., Kumar et al., 2007; Yoon and Carter, 2007) and services reuse to achieve cost decreases and increasing enterprise agility (e.g., Baskerville et al., 2005; Yoon and Carter, 2007), extending a firm’s IT governance to utilize SOA is not trivial. The SOA concept comprises the idea of a component-oriented coupling of business processes and their implementation using a new service layer (Siedersleben, 2007). Hence, introducing SOA necessitates managing this new service layer between the existing business processes and application systems. SOA governance therefore requires finding ways to establish structures and processes and develop employees to handle the new relationship between IT and process architecture. Our research question thus is:

Which SOA governance mechanisms are important to implement an effective SOA that increases IT flexibility and leads to service reuse?

Our research model shows how SOA governance affects IT flexibility and reuse. An empirical evaluation based on data from 81 firms using SOA reveals the differential impact of various SOA governance mechanisms (structures, processes, and employees/relations). The study contributes (a) to existing research by offering the first empirically substantiated analysis of the importance of SOA governance and a comparison of the influence of different SOA governance mechanisms, and (b) to practitioners by providing evidence-based answers to the question, which governance mechanisms are most important for achieving IT flexibility and reuse.

We first delineate conceptual foundations regarding SOA – modular systems theory, IT flexibility, and SOA governance – and then develop the research model and hypotheses. Afterwards, we explain our approach and data before testing the model. Finally, results, limitations, and areas for future research are discussed.

## 2. Concepts and related research

This section first briefly discusses why, from a theoretical perspective, SOA needs governance, to then draw on existing literature for developing the core concepts of our research model.

## 2.1. Conceptualization of SOA

SOA has attracted attention for its promise of new ways to cope with old IT architecture challenges. The literature, while focusing primarily on technical aspects, includes important research areas (Ren and Lyytinen, 2008) such as security, reliability, service composition (Curbera et al., 2003), the selection and management of services (Yu et al., 2007), and orchestrating services (Peltz, 2003). Some research also addresses the question of the benefits that result from SOA adoption (Joachim et al., 2011; Kumar et al., 2007).

Based on a review of the SOA literature, Joachim (2011) categorizes frequently mentioned characteristics of SOA as either technologies often used for implementing SOA, service-oriented design principles applied at the IS architecture level, or principles for establishing a service-oriented enterprise (SOE). However, beyond these common characteristics, ‘‘it seems that there is little agreement among practitioners and researchers alike as to a standard definition of SOA’’ (Erickson and Siau, 2008, p. 43). Erickson and Siau identified nine different formal definitions of SOA, which range from ‘‘modularizing a firm’s business activities into functional services" to “using web services for distributed computing". In our work, we draw on Bieberstein et al., who define SOA as a holistic concept comprising IT and business aspects: ‘‘A service-oriented architecture is a framework for integrating business processes and supporting IT infrastructure as secure, standardized components – services – that can be reused and combined to address changing business priorities’’ (2005a, p. 5).

Yoon and Carter (2007) investigate the benefits that drive an organization’s interest in adopting SOA. Their case studies reveal that SOA can facilitate integration of systems, improve data flow and customer service as well as reduce IT cost. Also, SOA can lead to quicker IT responses to market change or customer demand and to reuse of already existing implemented functionality. Baskerville et al. (2005) emphasize the theoretically high potential of reuse in an SOA, even though they could only partly show positive effects of reuse (such as lower development costs or responding quicker to changing customer demands) in their two case studies, as existing services needed to be adapted to reuse existing functionality. Another benefit of SOA is a higher level of flexibility, as previously developed modular services can be reused or locally extended if business needs change or new needs arise (Yoon and Carter, 2007). Gartner summarizes the role of achieving reuse in an SOA: ‘‘Reuse is not a benefit of SOA but a hurdle that needs to be overcome in order to improve business agility and lower software maintenance’’ (Saran, 2006). This important role of reuse is supported further by Bieberstein et al. (2005b, pp. 692–693), who state that ‘‘reuse promotes company-wide consistency of key business operations and processes, while reducing costs.’

Synthesizing prior efforts, Becker et al. (2009) did an extensive literature analysis and thus identified agility, and reuse as the most important benefits of SOA with which we concur. Thus, we will draw on those as our endogenous variables when developing our model.

## 2.2. Applying modular systems theory to the SOA paradigm

While modularity is a key concept in various scientific disciplines, such as biology, mathematics, and psychology, a thorough theoretical consideration of modularity as a key constituent in services metaphors in general, and for SOA in particular, is lacking. Schilling (2000, p. 312) defines: ‘‘Modularity is a general systems concept: it is a continuum describing the degree to which a system’s components can be separated and recombined, and it refers both to the tightness of the coupling between components and the degree to which the ‘rules’ of the system architecture enable (or prohibit) the mixing and matching of components.’’ Essentially, almost all biological, technical and other systems can be interpreted as hierarchically nested modular systems (Simon, 1962) that ‘‘are intentionally designed to require low levels of coordination so that they can be carried out by an organizational structure of quasi-independent divisions functioning as loosely coupled subsystems" (San: chez and Mahoney, 1996, p. 64). In this vein, business processes and supporting applications can be modularized into services by adopting SOA (Papazoglou and Heuvel, 2007). As is the case for each modular system, the components or services of an SOA represent other subsystems that can again be viewed as a modular system consisting of finer, loose services (Simon, 1962). However, ‘‘loose does not mean lax; loosely coupled systems operate to very stringent performance requirements’ (Hagel and Brown, 2005, p. 85). For example, a modular, loosely coupled product design enables a decentralized production process in cases where well-defined standard interfaces exist. This allows employees to work on separate components while still ensuring that the resulting components can interact effectively (Schilling, 2000). In the context of SOA, dedicated governance and management mechanisms define the necessary standards for locally developed, modularized services to facil itate the reuse of services in other processes. From a business-oriented perspective on services management, there is a substantial gap between, for example, SOA potential resulting from modularity, and realized SOA benefits resulting from reuse. SOA faces the challenge – and opportunity – that service construction needs to be directed towards business goals. SOA governance thus directs how services are constructed and how they are used and reused

## 2.3. IT flexibility

Achieving flexible IT is an important IT strategic goal (Kumar, 2004) and a major reason to adopt SOA. Byrd and Turner (2000) have conceptualized the flexibility of IT infrastructure as the combination of both the human and technical IT infrastructure. Since our research addresses the SOA domain, which is mainly an architectural and technical concept, we restrict our research to the technical part of IT infrastructure flexibility, which we hereafter refer to simply as IT flexibility, defined as the ‘‘degree to which its [the IT infrastructure’s] resources are sharable and reusable’’ (Duncan, 1995, p. 42).

Based on the degree of shareability and reusability of the resources within an IT infrastructure, Duncan proposes three criteria for IT flexibility: (1) connectivity, that is, enabling components to connect to each other; (2) compatibility, that is, allowing connected components to interact and share information (Chung et al., 2003); and (3) modularity, that is, ‘‘isolating and standardizing as many business and systems processes as possible’’ (Duncan, 1995, p. 48) and covering applications and data. Byrd and Turner define modularity as ‘‘the ability to add, modify, and remove any software, hardware, or data components of the infrastructure with ease and with no major overall effect’’ (2000, p. 171). However, an empirical evaluation of Duncan’s three dimensions by Byrd and Turner found a lack of discriminant validity between connectivity and compatibility; therefore, they were merged to the new concept of integration (2000).

Chanopas et al. (2006) extended these works and identified another dimension, scalability, to be an important part of IT flexibility<sup>1</sup>. Scalability – ‘‘the degree to which hardware/software can be scaled and upgraded on existing infrastructure’’ (Chanopas et al., 2006, p. 645) – can be seen as an important outcome of SOA. SOA is generally expected to exhibit higher scalability than point-to-point connections because an enterprise service bus (ESB) is applied for application integration. This solves the major problem of rapidly increasing complexity with a rising number of systems to be integrated in case of pointto-point connections (Papazoglou and Heuvel, 2007). A scalable IT infrastructure allows for easier handling of increasing numbers of users, workload or transaction volume (Chanopas et al., 2006: Kumar. 2004). For example, in an SOA multiple instances of resource intensive services can be deployed across (e.g., virtualized) computing nodes and accessed using dynamic routing to avoid bottlenecks (resulting from increasing transaction volume) (Papazoglou and Heuvel, 2007).

Based on those previous works, we conceptualize technical IT flexibility by the three dimensions of modularity, integration, and scalability.

## 2.4. SOA governance

SOA governance is frequently proposed as the means to an effective SOA (Varadan et al., 2008; Walker, 2007). The basic idea is that SOA governance should support the firm in handling any challenges arising from SOA implementation.

Research regarding SOA governance has focused mainly on developing methods for designing and implementing single services or entire service-oriented solutions (Arsanjani et al., 2008). Other works investigate selected SOA governance aspects, such as methods for: service identification of single services (Esswein et al., 2009); service integration testing (Bertolino and Polini, 2009); describing models and tools for supporting SOA governance activities at the technical level (Derler and Weinreich, 2007); developing an SOA governance approach based on the lifecycle of single services (Schepers et al., 2008); or proposing new organizational structures for SOA (Bieberstein et al., 2005b). There is also broader research that takes a more comprehensive approach to SOA governance. For example, Leusse et al. (2009) propose a special SOA governance model for handling nonfunctional requirements in a dynamic way. Strnadl (2007) formulates a specific semantic meta model that captures the combined requirements of business process management and SOA governance, while Niemann et al. (2008) suggest a generic SOA governance model emphasizing the control cycle and Varadan et al. (2008) develop an SOA governance framework based on IBM’s client experiences.

Although many SOA governance and management mechanisms have been proposed in the academic and practitioner literature, to the best of our knowledge none of the concepts has been evaluated by quantitative studies to examine their contribution to a successful SOA implementation. To select the SOA governance mechanisms to be included in our study, we first selected two established governance models to identify important governance mechanism categories. The generic IT governance model of De Haes and Van Grembergen (2009) distinguishes between structures, processes, and relational mechanisms, while the conceptual SOA governance model suggested by Kohnke et al. (2008) draws on structures, processes, and employees/ relations. As both models draw on three comparable pillars, we decided to focus on these three categories and harmonize the labels from both governance models.

In a second step, we conducted a review of the research literature on SOA (Joachim, 2011), to identify different SOA governance mechanisms that have been proposed often for each of the three categories. We identified 33 papers<sup>2</sup> with statements regarding SOA governance. However, as very general propositions like ‘‘SOA governance is important for an effective SOA’’ do not mention particular SOA governance mechanisms, we excluded those papers that did not investigate SOA governance in detail. In total, we investigated 10 papers, each offering detailed insights into different SOA governance mechanisms. Table 1 lists the SOA governance mechanisms and shows the relative frequency they were mentioned in the investigated papers.

The model development, which follows in the next section, includes those governance mechanisms that were mentioned as being important by the majority of the papers.

## 3. Research model

We next develop our research model (visualized in Fig. 1), theorizing the influence of the three categories of SOA governance (i.e., structures, processes, and employees/relations) on (a) the three dimensions of technical IT flexibility (i.e., modularity, integration, and scalability) as identified in the previous literature, and (b) reuse to trace separately the effects of different SOA governance/management mechanisms in more detail.

## 3.1. Structures

Structures are the first of the three categories of SOA governance proposed by Kohnke et al. (2008). Within this category, we look explicitly at two aspects: establishing new decision-making bodies and using standards. One example of implementing such a new decision-making body for SOA governance could be the SOA Center of Excellence (CoE) (Walker, 2007). However, it depends on whether the CoE is restricted to identifying problems and making recommendations or whether it also has authority to make decisions (Schepers et al., 2008). The CoE is a board or committee comprising business domain owners as well as IT and, in particular SOA experts (Keen et al., 2008). The CoE consolidates the SOA-related knowledge of the organization and performs the company-wide planning of all SOA-related tasks (Mitra, 2005). While existing decision-making bodies can accomplish the first SOA pilot projects, specific decision-making bodies, such as a CoE or an SOA board, are usually implemented when SOA is adopted more broadly. For example, Walker describes how existing internal enterprise architecture governance mechanisms were leveraged to steer the SOA-related activities rather than ‘‘defining a completely new and independent governance structure’’ (2007, p. 660). However, for handling a firm-wide introduction of SOA, it is often suggested that a new governance body is put into place to achieve the desired goals, such as increasing flexibility and reuse (Varadan et al., 2008, p. 480).

Hypothesis (H1a). Introducing a new decision-making body (e.g., SOA Center of Excellence) increases IT flexibility in terms of modularity, integration, and scalability.

Hypothesis (H1b). Introducing a new decision-making body (e.g., SOA Center of Excellence) increases reuse.

Establishing and using standards is a further SOA governance mechanism beyond establishing new decision-making bodies. Such standards range from criteria to guide whether functionality should be implemented as services (e.g., expected frequency of service use) through to design standards for system interfaces (Bieberstein et al., 2005b; Lee et al., 2010). The former can help to identify the appropriate level of modularity and granularity of services, which facilitates reuse, while the latter can enhance flexibility to integrate functionality freely as needed or replace existing functionality with a new service, or if decisions are based on open reference models (Bieberstein et al., 2005b).

Table 1  
Frequently mentioned SOA governance mechanisms (bold = used in our study)

<table><tr><td>Governance category</td><td>SOA governance mechanism</td><td>Description</td><td>Source</td><td>Frequency (out of 10)</td></tr><tr><td rowspan="3">Structure</td><td>New decision-making body</td><td>Establishing a new, SOA-specific decision-making body (e.g., SOA Center of Excellence (CoE) or an SOA board) which has the decision rights regarding company-wide planning of all SOA-related tasks and is not limited only to making recommendations.</td><td>1, 2, 4–9</td><td>8</td></tr><tr><td>Standards</td><td>Defining internal, SOA-related technology standards to which all projects must adhere.</td><td>1, 2, 4–9</td><td>8</td></tr><tr><td>Roles and responsibilities</td><td>Establishing new roles (e.g., SOA leads, service owner) and supporting the collaboration and coordination of SOA activities when new services need to be developed or existing ones need to be adapted for reuse in another domain.</td><td>2–4, 8, 9</td><td>5</td></tr><tr><td rowspan="3">Processes</td><td>Service management</td><td>Implementing service management processes is important to support the service operation. Service management covers the entire service portfolio, which needs to be prioritized and coordinated during its lifecycle.</td><td>1, 2, 4–10</td><td>9</td></tr><tr><td>Service development</td><td>Adhering to obligatory design guidelines to develop coherent services across the firm and reduce service redundancy.</td><td>1, 4–10</td><td>8</td></tr><tr><td>Performance measurement</td><td>Using aligned metrics to monitor the services (should be jointly selected with the business units) to align the SOA implementation with business goals (e.g., higher flexibility, reduced business process costs).</td><td>2, 4–6, 8</td><td>5</td></tr><tr><td rowspan="4">Employees/relations</td><td>Qualifications</td><td>SOA can be successful only when IT personnel understand service-oriented thinking and the SOA paradigm. If not available, appropriate trainings have to be established.</td><td>2–5, 7–10</td><td>8</td></tr><tr><td>IT/business communication</td><td>For implementing effective services, good communication between IT and business units is important to facilitate knowledge exchange and thus align IT with business requirements.</td><td>1–5, 8–10</td><td>8</td></tr><tr><td>Collaborative work of business units</td><td>SOA governance has to promote collaborative work of business units to support the identification of synergies and define requirements across different business processes.</td><td>2–4, 6–9</td><td>7</td></tr><tr><td>Incentives</td><td>Using incentives (e.g., annual bonuses) to increase the commitment of the employees to the changes that result from implementing SOA (e.g., rewarding developers or business units for identify service reuse potentials).</td><td>2–4, 9, 10</td><td>5</td></tr></table>

1: Becker et al. (2009), 2: Bieberstein et al. (2005b), 3: Kavianpour (2007), 4: Kohnke et al. (2008), 5: Lee et al. (2010), 6: Schepers et al. (2008), 7:Tewary et al. (2009), 8: Varadan et al. (2008), 9: Walker (2007), 10: Yoon and Carter (2007).

Hypothesis (H2a). Applying common standards increases IT flexibility in terms of modularity, integration, and scalability.

Hypothesis (H2b). Applying common standards increases reuse.

## 3.2. Processes

In the SOA governance processes category, we distinguish between processes that support service management and those related to service development. Service management processes provide a centralized overview of existing services and their control during the entire service lifecycle (Walker, 2007). Moreover, good service management includes policies and agreements for charging service use. This allows for compensation to the business units which first demands a service and then bears the additional costs required to develop a generic service that is reusable by other business units, as opposed to implementation of a service specific to the needs of a single business unit, which would cost less (Walker, 2007). Tasks related to managing the availability of services, application management, and service support are also part of the service management process (Kohnke et al., 2008: Schepers et al., 2008), In addition, Varadan states that “the realization of SLAs between providers and consumers" is important (2008, p. 481). A central perspective on all existing services guides the development of new services and the adap tation of existing services to create a flexible IT infrastructure. Thus, it allows for increased reuse of existing services.

Hypothesis (H3a). Implementing service management processes increases IT flexibility in terms of modularity, integration, and scalability.

Hypothesis (H3b). Implementing service management processes increases reuse.

Analysis of existing services can raise the need to refine existing services or to develop new ones. To ensure that newer versions of existing services or new services are still compatible with other existing services, clear service development processes are needed. This ensures further that services are designed to be sufficiently modular to support their flexible integration and later reuse (Lee et al., 2010). Service development processes should also ensure that, whenever possible, existing functionality is reused and not developed anew. The development of reusable services is seen as considerable effort (Becker et al., 2009) that needs additional guidance by established processes. As services should not be defined separately for each project, there is a need ‘‘to evangelize solutions across projects and processes’’ (Hirschheim et al., 2010, p. 44)

![](/api/attachments/QEESVCME/fulltext/images/053691d1154e145b71d94957b7000ea2263088e544d66c098023cf98a1b447c3.jpg)  
Fig. 1. Research model.

Hypothesis (H4a). Establishing service development processes increases IT flexibility in terms of modularity, integration, and scalability.

Hypothesis (H4b). Establishing service development processes increases reuse.

## 3.3. Employees/relations

The third and final category of SOA governance mechanisms comprises actions related to the involved employees/relations. We distinguish between the qualifications of involved IT emplovees. IT/business communication, and the collaborative work of different business units when developing services. The existing knowledge and skills of employees regarding the implementation and management of SOA are important. SOA also require new skills that, in turn, may require training (Kohnke et al., 2008). Thus, organizations often educate their employees with respect to building, reusing, and deploying services (Yoon and Carter, 2007). Further, ‘‘new skills in technology, architecture, development, and infrastructure design’’ are often required to implement an ESB and registry (Varadan et al. 2008). Without sufficient knowledge regarding SOA and the concept of service orientation, it is unlikely that services will be designed in such a way that they create the expected flexible IT infrastructure or are sufficiently modular to be reused.

Hypothesis (H5a). Better SOA-qualified employees will allow for higher IT flexibility in terms of modularity, integration, and scalability.

Hypothesis (H5b). Better SOA-qualified employees will allow for higher reuse.

Tiwana et al. (2003) already revealed that better knowledge exchange between business and IT increases flexibility in IT projects. Correspondingly, Sabherwal and Chan found that better IT/business alignment increases (business and IT) flexibility (2001). According to Chen (2008), alignment via communication is one of three important means to achieve IT/business alignment, in addition to alignment via architecture and governance in an SOA. Chen highlights further that, in particular, ‘‘efforts are made to narrow ‘culture gaps’ between business and IT people, which has been a major cause for system development failure’’ (2008, p. 3). Consequently, when there is good communication between IT and business employees, the resulting SOA is more likely to fulfill business demands regarding flexibility and reuse, because there will be fewer problems and misunderstandings.

Hypothesis (H6a). Good communication between IT and business units increases IT flexibility in terms of modularity, integration, and scalability

Hypothesis (H6b). Good communication between IT and business units increases reuse.

As services in an SOA should support business needs (Bieberstein et al., 2005a), it is important that the business units work collaboratively on the specifications of services and that they are able to communicate their specific needs (Yoon and Carter, 2007). Krafzig et al. (2005) highlight that ‘‘being able to talk about the specific nature of different services at an abstract level will enable the different stakeholders in an SOA project [. . .] to communicate their ideas and concerns more effectively.’’ Therefore, a common understanding of services and communication among business units to identify synergies between business processes is important to promote an effective IT infrastructure that should not only serve the minority of single business units appropriately but also fulfill the needs of the majority. Thus, SOA governance should create ‘‘an effective collaboration environment across multiple business units with a diverse set of business goals’’ (Walker, 2007, p. 652) to deploy ‘‘shareable and reusable services such that they can be used across lines of business and across processes in a manner dictated by the business’’ (Varadan et al., 2008, p. 473).

Hypothesis (H7a). The collaborative work of different business units increases IT flexibility in terms of modularity, integration, and scalability.

Hypothesis (H7b). The collaborative work of different business units increases reuse.

## 3.4. Modularity as mediator

While integration and scalability, as part of IT infrastructure flexibility, provide benefits for the adopting organization, modularity as a third aspect of IT flexibility does not per se constitute any value for the organization. The reasoning behind modularity is that the functionality encapsulated in the service can be reused in other business activities (Yoon and Carter, 2007). Thus, functionality is not encapsulated as modular services for its own sake, but is worth the additional effort only if the services are actually reused. According to modular systems theory, services that are modular and loosely coupled can be separated and recombined easily, enabling different combinations and reuse of services (Schilling, 2000).

Hypothesis (H8). A higher degree of modularity will increase the reuse of services in an SOA.

The higher the degree of modularity, the more likely a service can be reused in another context (Baskerville et al., 2005). Yet, managerial complexity and communication overhead increase when the same functionality is split into loosely coupled services rather than implementing it into just one tightly coupled, aggregated service. A service with a rather low degree of modularity, though, is hardly reusable in other contexts, as it is tightly coupled with other services and difficult to separate from its context. This makes the use of just one part or the entire service in other contexts difficult or even impossible. Thus, modularity is expected to be a key enabler of reusing functionality. We therefore propose that SOA governance and management mechanisms not only directly increase reuse, but are (partially) mediated by modularity as key facilitator of reuse.

Hypothesis (H9). Modularity mediates the influence of SOA governance/management mechanisms on reuse of functionality.

## 4. Methodology and results

This section begins by explaining the data collection and methodology, followed by a test of the data quality as well as of the validity and reliability of the measurement model. Finally, the research model is evaluated.

## 4.1. Approach

## 4.1.1. Data collection

We applied a quantitative approach and conducted a survey in the German service industry, comprising logistics, trade, financial services, energy, and so on (US SIC codes 4000–8999). We chose the service industry because of its comparatively higher reliance of its business processes on IT compared to other industries in which the role and importance of physica assets and materials may be significant contingencies.

We contacted the firms individually by phone to identify the manager in charge of the IT architecture and to request participation in the survey. This led to appropriate persons being identified in 1743 firms. Next, we mailed out a paper-based questionnaire. After two reminders (via postal mail and phone), we eventually received 247 questionnaires (i.e., a response rate of 14.2%). To test our hypotheses, we selected only those responding organizations that had already adopted SOA and show a sufficient degree of SOA supporting their business processes to offer valid insights into SOA governance/management mechanisms. Thus, we eliminated 124 of the 247 responding organizations that had not yet adopted SOA.

## 4.1.2. Measurement

All but one construct are based on (reflective) multi-item measures and were derived from the literature where possible (i.e., in the case of modularity, integration, and scalability); these are shown in Appendix A. Establishing a ‘‘new decisionmaking body’’ was the only construct operationalized by a single item, as it does not comprise or is formed by two or more components (Bergkvist and Rossiter, 2007)<sup>3</sup>. We used a single item that asked for rating the degree to which new decisionmaking bodies have been established for SOA directly. The other constructs measuring the SOA governance mechanisms were newly developed for this study, as we are not aware of a prior quantitative study that has investigated SOA governance/management mechanisms.

Before designing the survey, we reviewed the literature on SOA governance and conducted a series of case studies in 9 large German services firms. One part of the case study interviews examined the SOA governance/management mechanisms applied in the particular firm. Thus, we had the opportunity to learn SOA lingo from experts, receive feedback about our model and items, and gain insights into different SOA governance approaches and their importance for effective SOA implementation.

Next, we discussed the operationalizations of the new constructs with a group of seven researchers experienced in the field of SOA to avoid unclear or ambiguous formulations. Moreover, we asked an industry expert panel consisting of consultants active in the SOA domain to assess the items and their content. We followed their suggestions and refined our measurement instruments accordingly. As no additional items were proposed, their responses also suggested that our items adequately cover the content domain (Lewis et al., 1995).

Then, we evaluated content validity involving ten consultants from several consulting firms and experienced in SOA following the procedure applied by Lewis et al. (1995). This approach requests each panelist to rate the relevance of each item on a three-point scale in order to calculate the content validity ratio (CVR). All except two items showed a CVR equal to or higher than .80 and thus fulfill the requested threshold of .62 (Lawshe, 1975) meaning that the overwhelming majority of panelists feel that the developed items are important for SOA governance, which is significant at the 5% level. The two remaining items are rated at .60 (IBC2) and .40 (SMM2), thus, IBC2 is only marginally below the threshold. Using card sorting (Moore and Benbasat, 1991), both items were consistently assigned to their intended constructs (IBC2 in 90% of the cases to IT/business communication and SMM2 in 80% of the cases to service management) by the same ten consultants. Assessing Fleiss’ Kappa<sup>4</sup>, the 10 panelists showed a high inter-rater reliability of .76. As both items are part of reflective multi-item measurement models each consisting of three items and as reflective constructs are in general more robust than formative constructs (Petter et al., 2007), we decided to keep these two items within the model.

As control variables we added organizational size (measured by total number of emplovees from secondary data sources). industry type (dummy variables for logistics&trade, financial services, and ICT), and usage of general IT governance mechanisms (ITIL and COBIT). Including the latter in the analysis allows for examining whether IT flexibility is predicted by the investigated SOA governance mechanisms or rather by the use of ITIL or COBIT, which are not SOA-specific

## 4.1.3. Analysis

We used Partial Least Squares (PLS) (SmartPLS, Ringle et al., 2007) and SPSS to analyze the data. For testing the hypotheses, we implemented two different models:

\- Flexibility model: First, we tested the hypotheses between the different SOA governance/management mechanisms and technical IT flexibility (consisting of modularity, integration, and scalability).

Direct and full reuse model: Second, we estimated a pair of models comprising the influence of the different SOA governance/management mechanisms on reuse as well as the mediating role of modularity. The direct reuse model links the different SOA governance/management mechanisms to reuse while the full reuse model adds modularity as mediator in between. Comparing the results of both models allows for testing the mediation effect.

Analyzing the results from the flexibility and reuse models allows for an integrated picture of the effects of SOA governance/management mechanisms on IT flexibility as well as on reuse.

Our data set comprised several missing values. Since SOA adoption is infrequent and since the usable data set is comparably small, we followed the suggestions of Kristensen and Eskildsen (2010) to apply missing value treatment. Kristensen and Eskildsen simulated the effects of applying different missing value handling strategies and found that replacing the missing values using the expectation–maximization (EM) algorithm leads to more valid and more reliable estimation results, compared to pairwise deletion or simple treatments such as mean value substitution. However, we applied a very conservative approach and used the EM algorithm only for those items, which had at most 3 missing responses (i.e., 3.7% missing values at most) while eliminating data from the other questionnaires from the data set. This led eventually to 81 responses used in the following calculations.

## 4.2. Quality of data and measurement model

Before evaluating our research model, we tested our data for normality using the Kolmogorov–Smirnov test and assessed skewness and kurtosis, which showed that some of our items are not normally distributed. This and the limited sample size were the reasons why we chose PLS instead of covariance-based SEM for testing our research model.

Further, we examined the data regarding non-response bias. Therefore, we compared the answers given by the early respondents to those respondents who answered only after several reminders. The basic assumption of this approach is that the latter group shares similarities with those receivers of the questionnaire that have not answered at all, and thus can serve as a proxy, as argued in Armstrong and Overton (1977). As no indicator showed a significant difference according to the Kolmogorov–Smirnov test, we can assume that non-response bias is not a major problem in our data. Similarly, no differences were shown in the answers not included in the analysis because of missing values in single items.

Next, we took several measures for making sure that common method bias had not affected our results, such as using dif ferent questionnaire versions and applying the marker variables approach. The details are reported in Appendix D.

After analyzing the quality of our data, we tested the reliability and validity of the PLS measurement model. All but one indicator loading (SMM3 .699) where above .707 (cf. Appendix A). Appendix B shows that construct reliability, convergent and discriminant validity are satisfied in both model estimations, too<sup>5</sup>.

## 4.3. Analyzing the influence of SOA governance on IT flexibility (flexibility model)

Table 2 shows the path coefficients from testing the flexibility model (paths from all governance constructs to the three IT flexibility dimensions). Notably, establishing new decision-making bodies has a significantly negative relationship with modularity and integration but no influence on scalability. Standards show strong relationships with all three dimensions of technical IT infrastructure flexibility. Further, service management processes have a weakly significant influence on modularity and integration but none on scalability. With respect to employees/relations, the results show that their qualifications as well as IT/business communication positively affect all three dimensions of IT flexibility. Finally, the service development process and the collaboration of different business units are only related to modularity. The remainder of the hypothesized relationships are not significant. Also, COBIT shows no significant influence while ITIL contributes weakly to integration.<sup>6</sup>

Table 3 presents the $\mathsf { R } ^ { 2 }$ of the dependent variables (modularity, integration, and scalability). The different SOA governance/management mechanisms predict a significant part of the variance in modularity (45.8%) and integration (37.8%), while the explanation of scalability (18.3%) is weak.

Correspondingly, Table 4 provides the single effect sizes $( f ^ { 2 } ) .$ . We find that, according to Chin (1998), all SOA governance mechanisms have small to medium effects on modularity and that all except service development processes and the collaborative work of business units also have a similar effect on integration. However, only standards, the qualification of employees, and IT/business communication have a small effect on scalability.

## 4.4. Analyzing the mediation effects between SOA governance, modularity, and reuse (reuse model)

Table 5 presents the results of testing the reuse model with and without modularity (i.e., full vs. direct reuse model); comparing the results uncovers the mediation effect of modularity (Baron and Kenny, 1986). First, the results exhibit clearly that modularity is positively related with reuse of functionality (cf. Table 5, full reuse model). Further, analogous to the flexibility model estimation, establishing new decision-making bodies for SOA governance is negatively related with reuse. Using standards enhances reuse, and having clear service management processes seems by far to be the single most important SOA governance factor for driving reuse. By contrast, it is interesting that implementing service development processes, better IT/business communication, and collaboration among business units show no positive relationship with reuse. The collaboration of different business units seems to even dampen the effect of modularity on reuse (no relationship in the direct reuse model, but a significant negative relationship in the full reuse model). The negative relationship is caused by a statistical sup pressor effect; it can be interpreted such that collaboration of business units increases modularity but not reuse. In addition, the direct reuse model without modularity as mediator, shows that better qualification of employees with SOA skills does indeed increase reuse.

Table 2  
Flexibility model test results (b and significance levels).

<table><tr><td colspan="3">Impact of SOA governance mechanism...</td><td colspan="3">on...</td></tr><tr><td></td><td>Hyp.</td><td>Mechanism</td><td>Modularity</td><td>Integration</td><td>Scalability</td></tr><tr><td rowspan="2">Structures</td><td>H1a</td><td>New decision-making body</td><td>-.256*</td><td>-.339**</td><td>-.008</td></tr><tr><td>H2a</td><td>Standards</td><td>.334**</td><td>.307**</td><td>.246*</td></tr><tr><td rowspan="2">Processes</td><td>H3a</td><td>Service management</td><td>.156+</td><td>.162+</td><td>-.059</td></tr><tr><td>H4a</td><td>Service development</td><td>.138+</td><td>.102</td><td>-.092</td></tr><tr><td rowspan="3">Employees/relations</td><td>H5a</td><td>Qualification</td><td>.135+</td><td>.216*</td><td>.223*</td></tr><tr><td>H6a</td><td>IT/business communication</td><td>.159*</td><td>.147+</td><td>.261*</td></tr><tr><td>H7a</td><td>Collaborative work of business units</td><td>.214*</td><td>.094</td><td>-.062</td></tr><tr><td rowspan="7">Controls</td><td></td><td>Organizational size</td><td>-.207*</td><td>-.224*</td><td>-.017</td></tr><tr><td></td><td>ITIL</td><td>.105</td><td>.133+</td><td>.014</td></tr><tr><td></td><td>COBIT</td><td>-.069</td><td>.069</td><td>.013</td></tr><tr><td></td><td>Industry type:</td><td></td><td></td><td></td></tr><tr><td></td><td>Logistics and trade</td><td>.127+</td><td>-.108</td><td>.016</td></tr><tr><td></td><td>Financial services</td><td>.053</td><td>.091+</td><td>.106+</td></tr><tr><td></td><td>IT and communication</td><td>-.238**</td><td>-.013</td><td>-.035</td></tr></table>

<sup>+</sup> p <sup>6</sup> .1 (Because of the small sample size we chose to also consider $p \leqslant . 1$ as threshold for (weakly) significant relationships as is done in other studies using SEM (Worren et al., 2002; Zhu and Kraemer, 2002). In this way, we can avoid severe type-II errors which might just arise from the small sample. However, relationships that do not meet the traditional 05 significance level but only the 1 level will be particularly carefully discussed). ${ \bf \Phi } ^ { * } p \leqslant . 0 5 .$

$$
p \leqslant . 0 1.
$$

Table 3  
R-squares (flexibility model).

<table><tr><td>R-squares</td><td>Modularity</td><td>Integration</td><td>Scalability</td></tr><tr><td>Flexibility model</td><td>.458</td><td>.378</td><td>.183</td></tr><tr><td>Controls only</td><td>.218</td><td>.114</td><td>.023</td></tr></table>

Table 4  
Single effect sizes $( f ^ { 2 } ) .$

<table><tr><td rowspan="2">SOA governance mechanism</td><td colspan="3">Effect size of SOA governance mechanism on...</td></tr><tr><td>Modularity</td><td>Integration</td><td>Scalability</td></tr><tr><td>Structures</td><td></td><td></td><td></td></tr><tr><td>New decision-making body</td><td> $.06^b$ </td><td> $.10^b$ </td><td>.00</td></tr><tr><td>Standards</td><td> $.19^a$ </td><td> $.14^a$ </td><td> $.06^b$ </td></tr><tr><td>Processes</td><td></td><td></td><td></td></tr><tr><td>Service management</td><td> $.02^b$ </td><td> $.02^b$ </td><td>.00</td></tr><tr><td>Service development</td><td> $.02^b$ </td><td>.01</td><td>.01</td></tr><tr><td>Employees/relations</td><td></td><td></td><td></td></tr><tr><td>Qualification</td><td> $.03^b$ </td><td> $.06^b$ </td><td> $.05^b$ </td></tr><tr><td>IT/business communication</td><td> $.03^b$ </td><td> $.02^b$ </td><td> $.05^b$ </td></tr><tr><td>Collaborative work of business units</td><td> $.06^b$ </td><td>.01</td><td>.00</td></tr></table>

<sup>a</sup> Medium.  
<sup>b</sup> Small.

The $R ^ { 2 }$ show that the SOA governance/management mechanisms account for 48.7% of the variance of reuse, while the controls alone account for only 6% of reuse (not reported in tables). Thus, SOA governance is an important determinant for the degree of reuse in an SOA.

Looking at the single effect sizes $( f ^ { 2 } )$ clarifies that reuse is predicted largely by modularity and it also demonstrates the importance of service management processes for facilitating reuse.

Hypothesis 9 proposes that modularity mediates the influence of SOA governance/management mechanisms on reuse of functionality. First evidence is provided by the fact that the inclusion of modularity as a mediator goes hand in hand with most of the path coefficients (from SOA governance/management mechanisms to reuse) becoming weaker (Baron and Kenny, 1986), such as for new decision making body, standards, qualification of employees, or, less strongly, for service management (cf. Table 5, comparing paths of direct with full reuse model). To test for the existence of partial or even full mediation effects, we re-estimated the direct reuse model using the approach suggested by Preacher and Hayes (2004), which was also adopted in other recent IS studies (e.g., by Coltman et al. (2011) and Al-Natour et al. (2011)). Following this procedure, we bootstrapped the sampling distributions using 2000 bootstrap samples. The right columns of Table 5 show the point estimates as well as the lower and upper bounds of the 95% or 99% confidence intervals belonging to the mediation effect of modularity on the relationship between the different governance mechanisms and reuse. The results show that all mediation tests are statistically significant. However, according to Baron and Kenny (1986) a mediation effect requires that there is a significant direct relationship between the exogenous variable and the endogenous variable if the mediator is absent. By contrast, Shrout and Bolger (2002) argue that this requirement is not a necessity in the presence of rather low statistical power, which is likely in case of smaller sample size. According to these arguments, the statistically significant mediation effect of service development is likely to be an actual mediation effect, while in case of IT/business communication and collaborative work of business units we should not argue mediation to be existent since the basic relationship between them and reuse in the direct model is very close to zero.

Table 5  
Influence of SOA governance mechanisms on reuse (b and f<sup>2</sup>).

<table><tr><td rowspan="2"></td><td rowspan="2">Hyp.</td><td rowspan="2">Determinant</td><td colspan="2">Direct reuse model (without modularity)</td><td colspan="2">Full reuse model (with modularity)</td><td colspan="3">Mediation analysis (for full reuse model)</td></tr><tr><td>Path ( $\beta$ ) on reuse</td><td>Single effect ( $f^{2}$ ) on reuse</td><td>Path ( $\beta$ ) on reuse</td><td>Single effect ( $f^{2}$ ) on reuse</td><td>Lower bound</td><td>Upper bound</td><td>Point estimate</td></tr><tr><td rowspan="3">Structures</td><td>H8</td><td>Modularity</td><td>n/a</td><td>n/a</td><td> $.459^{**}$ </td><td> $.22^a$ </td><td></td><td></td><td></td></tr><tr><td>H1b</td><td>New decision-making body</td><td> $-.380^{**}$ </td><td> $.13^b$ </td><td> $-.268^{**}$ </td><td> $.12^b$ </td><td> $-.338^{**}$ </td><td> $-.004^{**}$ </td><td>-.126</td></tr><tr><td>H2b</td><td>Standards</td><td> $.271^{**}$ </td><td> $.11^b$ </td><td> $.113^+$ </td><td> $.02^b$ </td><td> $.017^{**}$ </td><td> $.355^{**}$ </td><td>.163</td></tr><tr><td rowspan="2">Processes</td><td>H3b</td><td>Service management</td><td> $.482^{**}$ </td><td> $.20^a$ </td><td> $.423^{**}$ </td><td> $.17^a$ </td><td> $.004^*$ </td><td> $.209^*$ </td><td>.080</td></tr><tr><td>H4b</td><td>Service development</td><td>.119</td><td>.01</td><td>.064</td><td>.00</td><td> $.003^*$ </td><td> $.189^*$ </td><td>.072</td></tr><tr><td rowspan="3">Employees/relations</td><td>H5b</td><td>Qualification</td><td> $.152^*$ </td><td> $.03^b$ </td><td>.086</td><td>.01</td><td> $.005^*$ </td><td> $.178^*$ </td><td>.070</td></tr><tr><td>H6b</td><td>IT/business communication</td><td>.010</td><td>.00</td><td>-.083</td><td>.01</td><td> $.004^*$ </td><td> $.186^*$ </td><td>.074</td></tr><tr><td>H7b</td><td>Collaborative work of business units</td><td>-.031</td><td>.00</td><td> $-.125^+$ </td><td> $.02^b$ </td><td> $.007^*$ </td><td> $.227^*$ </td><td>.096</td></tr><tr><td rowspan="7">Controls</td><td></td><td>Organizational size</td><td> $-.190^*$ </td><td></td><td>-.093</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>ITIL</td><td>-.063</td><td></td><td> $-.118^+$ </td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>COBIT</td><td>-.001</td><td></td><td>.030</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Industry type:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Logistics and trade</td><td>-.078</td><td></td><td> $-.136^+$ </td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Financial services</td><td>.105</td><td></td><td>.080</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>IT and communication</td><td>-.018</td><td></td><td> $.093^+$ </td><td></td><td></td><td></td><td></td></tr></table>

Note: significance levels of b, classification of effect sizes (f<sup>2</sup>).  
$p \leqslant . 0 5 .$  
$p \leqslant . 0 1 .$  
<sup>a</sup> Medium.  
<sup>b</sup> Small.  
Table 6  
Summary of all results (shaded cells represent confirmed propositions).

<table><tr><td colspan="2">Corresponding model :</td><td colspan="3">Flexibility model</td><td>Direct reuse model</td><td>Full vs. direct reuse model</td><td></td></tr><tr><td colspan="2">SOA governance mechanism:</td><td>Influence on modularity</td><td>Influence on integration</td><td>Influence on scalability</td><td>Influence on reuse (H1-7b)</td><td>Mediation by modularity (H9)</td><td>Test of Hypotheses (H1-H7)</td></tr><tr><td rowspan="2">Structures</td><td>New decision-making body</td><td>-</td><td>-</td><td></td><td>-</td><td></td><td>H1a+b rejected</td></tr><tr><td>Standards</td><td>++</td><td>++</td><td>+</td><td>+</td><td>✓</td><td>H2a+b confirmed</td></tr><tr><td rowspan="2">Processes</td><td>Service management</td><td>+</td><td>+</td><td></td><td>++</td><td>✓</td><td>H3a largely confirmed H3b confirmed</td></tr><tr><td>Service development</td><td>+</td><td></td><td></td><td></td><td>(✓) $^{a}$ </td><td>H4a+b rejected</td></tr><tr><td rowspan="3">Employees /relations</td><td>Qualification</td><td>+</td><td>+</td><td>+</td><td>+</td><td>✓</td><td>H5a+b confirmed</td></tr><tr><td>IT/business communication</td><td>+</td><td>+</td><td>+</td><td></td><td></td><td>H6a confirmed H6b rejected</td></tr><tr><td>Collaborative work of business units</td><td>+</td><td></td><td></td><td></td><td></td><td>H7a+b rejected</td></tr><tr><td colspan="5">Influence of modularity on reuse:</td><td colspan="3">++ (H8 confirmed)</td></tr><tr><td colspan="5">Modularity acts as mediator:</td><td colspan="3">H9 confirmed (for those governance mechanisms positively related with reuse)</td></tr><tr><td colspan="8">Note: shaded cells represent confirmed propositions; ++: significant positive relationship with medium effect size; +: significant positive relationship with small effect size; -: significant negative relationship with medium effect size; -: significant negative relationship with small effect size; ✓: significant mediation;</td></tr></table>

Thus, we can summarize that all statistically significant relationships between governance mechanisms and reuse are partly mediated by modularity and that the strongest and most significant mediation effect can be identified for standards. Table 6 summarizes all empirical results with respect to the importance of the different SOA governance/management mechanisms.

## 5. Discussion of results, implications, and limitations

While previous research proposes that SOA governance in general is important, our results (Table 6) offer the first empirically substantiated analysis of the importance of SOA governance and a comparison of the influence of different SOA governance mechanisms. Compared to previous conceptual works, our empirical results draw a more differentiated picture that highlights the importance of organizational aspects in addition to the well-known architectural ones. Also, our results open opportunities for discussing new insights into the differential importance and effects of SOA governance mechanisms for achieving SOA’s benefits based on evidence. The main findings are discussed in the following:

Implementing new, dedicated decision-making bodies for SOA hampers organizations in achieving higher degrees of IT flexibility and reuse:

One explanation for this contradictory result is that often existing IT governance decision-making bodies that have already existed before are also used for governing SOA (Walker, 2007). Thus, this result first supports the argument that establishing new decision-making bodies specifically for SOA is not a necessity in earlier phases of SOA implementations (Kohnke et al., 2008). An additional post hoc analysis comparing early (beginning of SOA implementation) and experienced (five or more years SOA) users<sup>7</sup> shows no significant difference in the distribution of implemented decision-making bodies<sup>8</sup>. This shows that both groups (firms experienced with SOA and SOA novices) alike often limit the degree of implementing new decision-making bodies but continue to use existing ones. We have seen similar phenomena in our nine case studies. For example, one of the studied firms defined its SOA governance as a ‘‘lean approach.’’ Rather than implementing new decision-making bodies, the organization has relied completely on existing structures that are known to perform well. The interviewees argued that new decision-making bodies would require considerable efforts without providing better results in terms of IT flexibility and reuse. Thus, using the existing structures might be at least more efficient – if not effective – for achieving the desired goals.

Moreover, the negative statistical relationship implies that adding more governance might even reduce reuse effectiveness. Firms might implement new decision-making bodies for SOA in addition to the already existing IT governance mechanisms giving both the decision rights to jointly govern the SOA activities. This increases the complexity of decision making processes as coordination among more governance units requires more effort, takes longer and eventually hampers IT flexibility and reuse – this was a negative phenomenon that we could observe when studying the SOA undertakings at a large Swiss bank. As an additional effect, departments might start to work around over-governed SOAs and try to hide their local SOA initiatives to avoid the involvement of unwanted additional and centralized decision-making bodies that (from the department’s perspective) simply add delays and confusion without contributing anything positive. Obviously, this workaround behavior strongly reduces the opportunity to gain synergies and to reuse already developed services. Future research should investigate different ways of implementing SOA-related decision-making bodies. Such analyses should scrutinize different scopes and degrees of power or rights associated with these decision-making bodies to reveal which structures are useful for which purposes and why, as well as which tradeoffs may arise. Altogether, establishing new decision-making bodies such as SOA centers of excellence turns out to be of no utility. Rather, a successful SOA introduction relies more on the efficient use of any functioning decision-making body that may already have existed before SOA. As a consequence, the success factor of establishing new roles and organizational structures often mentioned in expert interviews shows, in fact to hamper IT flexibility and service reuse.

Comparing the effects of SOA governance on the different dimensions of IT flexibility shows that scalability is less affected than modularity or integration:

Only three of the investigated SOA governance mechanisms (usage of standards, employee qualifications, and better IT/ business communication) are positively related with scalability. As argued earlier, increasing scalability by adopting SOA is realized mainly on the technical layer and less from using SOA governance processes. For example, in an SOA multiple instances of resource intensive services can be deployed across (e.g., virtualized) computing nodes and are accessed using dynamic routing to avoid bottlenecks (resulting from increasing transaction volume) (Papazoglou and Heuvel, 2007). Thus, most of the investigated SOA governance processes are too far away from actually influencing scalability, which is achieved on the technical layer. However, using standards is, of course, still beneficial as this mechanism addresses the technical layer. In addition, better communication between IT and business helps to identify the possible areas of services where scalability is needed and consequently allows implementing the services accordingly at the technical layer.

Besides the three mechanisms that are important for scalability, the integration facet of flexibility is supported by a fourth one: establishing service management processes. These processes support organizations in maintaining a consistent overview about the services and service versions deployed and used. However, the single most important SOA governance mechanism for facilitating integration is the consistent use of standards, which ensures efficient integration of different services even in the long term.

In comparison to scalability and integration, modularity is enhanced by all SOA governance mechanisms except implementing new decision-making bodies. This is not surprising as modularity is one of SOA’s core aspects and therefore everything is directed towards enhancing modularity.

Reuse is only driven by using standards, service management processes and qualifications:

While modularity per se does not create value but is driven by nearly all SOA governance mechanisms, reuse – as one of the core benefits of modularity – is only supported by standards, service management processes, and high employee qualification. Organizations face two problems when trying to reuse services. First, developing services for reuse increases development time (Schelp and Aier, 2009). Second, in the majority of cases the developed services still have to be adapted to specific needs when reused (Baskerville et al., 2005). To overcome these problems organizations need to establish organization-wide standards which allow easier reuse of developed services and train employees to increase their qualifications. Also, employees need to be trained on how to reuse services (Yoon and Carter, 2007). In addition, service management processes allow for a central overview about the existing services and increase the chance of identifying suitable existing services when needed by the business. Technically this can be supported by organization-wide registries and/or repositories (Yoon and Carter, 2007).

According to our hypotheses, service development processes, collaborative work of different business units as well as IT/ business communication should also be important factors for achieving reuse of the same functionality across multiple business units and processes. However, in our data this is not the case. Even though the establishment of service development processes is a necessary precondition for developing potentially reusable services, there is still a missing link to actual reuse.

Facilitating conditions to increase the reuse of services could be the collaborative work of different business units or IT/ business communication. But, fostering collaborative work between business units can also have a downside. Increased col laboration will also raise complexity and thus make it more difficult to reuse services without the additional support of ade quate processes. Even though clear development processes are in place, it could be that the processes are valid only for specific departments and are not overarching for the entire enterprise. Consequently, services are developed only for each project, which cannot lead to reuse without further solutions across the projects (Hirschheim et al., 2010). This argument is supported by the current state of most SOA implementations in action nowadays, since in most firms SOA is implemented not across the entire organization but only in specific areas. In our survey and in our case studies, the majority of participants stated that SOA is used primarily in single business areas For example in financial service companies, one often observes that the starting point for using SOA is in multi-channel customer interaction. Thus, reuse of existing services takes place between the different channels, but is limited to the particular business domain of retail banking and does not spill over to the rest of the bank. Thus, even though services could theoretically be reused in other areas of the organization, a wider reuse across different business units cannot take place at this particular stage of SOA implementation in practice (Schelp and Aier, 2009). Accordingly, better communication between IT and business or between multiple business units at this limited state of SOA adoption does not increase the reuse of services.

Using standards, establishing service management processes, increasing qualifications of employees, and facilitating IT/ business communication show to be the most important SOA governance mechanisms:

Overall, our results show that of the seven investigated SOA governance mechanisms these four are the ones that are consistently positively related with the flexibility dimensions and reuse (significant relationships with at least three of the four outcome variables). The importance of these four mechanisms might be rooted in their role as forming a solid base for the remaining (and maybe later implemented) mechanisms. Particularly, highly qualified employees and organization-wide standards will also play important roles for other governance processes and for effective collaboration. Thus, these two build the foundation to develop a flexible IT as well as reusable services. Based on the foundation sown through the two previously mentioned governance mechanisms, service management processes are of particular importance to actually reuse the potentially reusable services and thus to leverage the theoretical potential of service orientation. Better IT/business communication will then guide how an organization’s SOA will further develop in the future according to business needs, e.g, in terms of where integration and scalability are actually needed and where not. Thus, organizations should put strong emphasis on implementing these four mechanisms that in turn will support the entire SOA development process as they contribute to overall SOA implementation in terms of IT flexibility and reuse.

Our research has some limitations. First, the results regarding the effectiveness of SOA governance mechanisms for increasing reuse might be affected by the circumstance that the current state of SOA adoption is, in most firms, limited to a few business areas; thus, the often high potential of reusing services across the entire organization today is limited by the current state of low adoption in practice. Second, the tests performed to assess CMB (cf. Appendix D) indicate that the evaluation of our hypotheses may be conservative and – in combination with our comparably small data set – could have led to type-II-errors. Thus, ‘‘weakly confirmed’’ hypotheses, such as the relationship between service management and inte gration, may show to be significant in future studies. Third, for interpreting the importance of the different SOA governance mechanisms, one should keep in mind that we limited our research to the role of those mechanisms for achieving technical IT infrastructure flexibility and reuse. Thus, the importance of the investigated SOA governance/management mechanisms may vary for other benefits associated with SOA, such as increasing data quality or process quality or facilitating outsourcing opportunities (Beimborn et al., 2012). Fourth, most SOA governance mechanisms had only been implemented to a low to moderate degree in the surveyed firms. In some years, a repetition of the study may show more and stronger effects on IT flexibility. Finally, the existing literature on SOA governance/management mechanisms has largely neglected theory building. Thus, we were unable to apply a well-established theoretical foundation for our research model that would allow us to extend existing theory. However, by connecting the concepts of IT governance and IT flexibility, our work contributes to developing an IS servitization theory.

## 6. Conclusion

Overall, we can summarize that the majority of the investigated SOA governance/management mechanisms are confirmed to be relevant determinants for achieving IT flexibility from SOA. The most important SOA governance mechanisms are: using standards, establishing clear service management processes, increasing the qualification of employees, and facilitating IT/business communication. Our results offer a number of useful insights to services science and particularly services governance from an IS perspective. As this, to the best of our knowledge, is the first quantitative evaluation of SOA governance/management mechanisms, our results offer an evidence-based contribution to the discussion of the role of SOA governance when bringing together managerial and technical perspectives regarding service orientation. These can help future research advance the theoretical and business foundations of the SOA concept and disclose relations between technical and organizational goals and how both can be achieved. Particularly, when studying the business value impact of SOA, governance mechanisms are important organizational complements to be considered.

For managers, the results are helpful in implementing and developing SOA. Some 88% of our survey participants see the implementation of SOA as a challenging task, and almost as many expect organizational and governance changes to be necessary. As we have modeled both SOA governance and IT flexibility in a multifaceted way, the analyses reveal the differentia influence of SOA governance/management mechanisms on IT flexibility dimensions and reuse. Organizations striving for higher IT flexibility or reuse as a substantial goal of an SOA initiative can use the results to single out the most relevant management mechanisms.

We can conclude that SOA governance is crucial to reap the fruits sown through service orientation. Our analyses have shown the importance of SOA governance for SOA’s ability to improve IT flexibility and services reuse. These findings complement the predominantly technical literature on SOA and also specify which governance mechanisms are needed to achieve increased integration, scalability, modularity, and reuse.

## Acknowledgments

This work was supported by the E-Finance Lab at Goethe University in Frankfurt, Germany. The authors gratefully acknowledge the financial support during the data collection of the industry partners.

## Supplementary material

Supplementary data associated with this article can be found, in the online version, at http://dx.doi.org/10.1016/ j.jsis.2012.10.003.

## References

Al-Natour, S., Benbasat, I., Cenfetelli, R., 2011. The adoption of online shopping assistants: perceived similarity as an antecedent to evaluative beliefs. Journa of the Association for Information Systems 12 (5), 347–374.

Armstrong, J.S., Overton, T.S., 1977. Estimating nonresponse bias in mail surveys. Journal of Marketing Research 14 (3), 396–402.

Arsanjani, A., Ghosh, S., Allam, A., Abdollah, T., Ganapathy, S., Holley, K., 2008. SOMA: A method for developing service-oriented solutions. IBM Systems Journal 47 (3), 377–396.

Baron, R.M., Kenny, D.A., 1986. The moderator-mediator variable distinction in social psychological research: conceptual, strategic, and statistical considerations. Journal of Personality and Social Psychology 51 (6), 1173–1182.

Baskerville, R., Cavallari, M., Hjort-Madsen, K., Pries-Heje, J., Sorrentino, M., Virili, F. 2005. Extensible architectures: the strategic value of service-oriented architecture in banking. In: Proceedings of the 13th European Conference on Information Systems (ECIS). Regensburg, Germany.

Becker, A., Buxmann, P., Widjaja, T., 2009. Value potential and challenges of service-oriented architectures – a user and vendor perspective. In: Proceedings of the 17th European Conference on Information Systems (ECIS). Verona, Italy.

Beimborn, D., Joachim, N., Weitzel, T., 2012. Do service-oriented IT architectures facilitate business process outsourcing? A study in the German service industry. Zeitschrift für Betriebswirtschaft (ZfB). Journal of Business Economics 82 (Special Issue 4) 77–108.

Bergkvist, L., Rossiter, J.R., 2007. The predictive validity of multiple-item versus single-item measures of the same constructs. Journal of Marketing Research 44 (2), 175–184.

Bertolino, A., Polini, A., 2009. SOA Test Governance: enabling service integration testing across organization and technology borders. In: Proceedings of the International Conference on Software Testing, Verification and Validation Workshops. Denver, CO, USA, pp. 277–286.

Bieberstein, N., Bose, S., Fiammante, M., Jones, K., Shah, R., 2005a. Service-oriented architecture (SOA) compass: business value, planning, and enterprise Roadmap. IBM Press, Upper Saddle River, NJ.

Bieberstein, N., Bose, S., Walker, L., Lynch, A., 2005b. Impact of service-oriented architecture on enterprise systems, organizational structures, and individuals. IBM Systems Journal 44 (4), 691–708.

Byrd, T.A., Turner, D.E., 2000. Measuring the flexibility of information technology infrastructure: exploratory analysis of a construct. Journal of Management Information Systems 17 (1), 167–208.

Chanopas, A., Krairit, D., Khang, D.B., 2006. Managing information technology infrastructure: a new flexibility framework. Management Research News 29 (10), 632–651.

Chen, H.-M., 2008. Towards service engineering: service orientation and business-IT alignment. In: Proceedings of the 41st Hawaii International Conference on System Sciences (HICSS). Waikoloa, Big Island, HI, USA: IEEE Computer Society.

Chin, W.W., 1998. The partial least square approach to structural equation modeling. In: Marcoulides, G.A. (Ed.), Modern Methods for Business Research. Lawrence Erlbaum Associates, Mahwah, NJ, USA, pp. 295–336.

Chung, S.H., Rainer, R.K., Lewis, B.R., 2003. The impact of information technology infrastructure flexibility on strategic alignment and applications implementation. Communications of the Association for Information Systems 11 (1), 191–206.

Coltman, T., Devinney, T.M., Midgley, D.F., 2011. Customer relationship management and firm performance. Journal of Information Technology 26 (3), 205– 219.

Curbera, F., Khalaf, R., Mukhi, N., Tai, S., Weerawarana, S., 2003. The next step in web services. Communications of the ACM 46 (10), 29–34.

de Haes, S., van Grembergen, W., 2009. An exploratory study into IT governance implementations and its impact on business/IT alignment. Information Systems Management 26 (2), 123–137.

Derler. P., and Weinreich. R. 2007, Models and tools for SOA governance, In: Draheim, D.. Weber, G. (Eds.). Trends in Enterprise Application Architecture. Berlin: Springer, pp. 112–126.

Duncan, N.B., 1995. Capturing flexibility of information technology infrastructure: a study of resource characteristics and their measure. Journal of Management Information Systems 12 (2), 37–57.

Erickson, J., Siau, K., 2008. Web services, service-oriented computing, and service-oriented architecture: separating hype from reality. Journal of Database Management 19 (3), 42–54.

Esswein, W., Weller, J., Starke, J., Juhrisch, M., 2009. Identifikation von Services aus Geschäftsprozessmodellen durch automatisierte Modellanalyse. In: Proceedings of the 9th International Conference on Business Informatics. Vienna, Austria, pp. 513–522.

Gefen, D., Straub, D.W., Boudreau, M.-C., 2000. Structural equation modeling and regression: guidelines for research practice. Communications of the Association for Information Systems 4 (1).

Hagel, J., Brown, J.S., 2005. The Only Sustainable Edge: Why Business Strategy Depends on Productive Friction and Dynamic Specialization. Harvard Business School Press, Boston, Mass.

Heffner, R., 2009. Insights For CIOs: SOA And Beyond. Forrester Research.

Hirschheim, R., Welke, R., Schwarz, A., 2010. Service-oriented architecture: myths, realities, and a maturity model. MIS Quarterly Executive 9 (1), 37–48

Joachim, N., 2011. A literature review of research on service-oriented architectures (SOA): characteristics, adoption determinants, governance mechanisms, and business impact. In: Proceedings of the 17th Americas Conference on Information Systems (AMCIS). Detroit, MI, USA.

Joachim, N., Beimborn, D., Schlosser, F., Weitzel, T., 2011. Does SOA create or require IT/business collaboration? Investigating SOA’s potential to reduce the gap between IT and business. In: Proceedings of the 32nd International Conference on Information Systems (ICIS). Shanghai, China.

Kavianpour, M., 2007. SOA and large scale and complex enterprise transformation. In: Proceedings of the 5th International Conference on Service-Oriented Computing (ICSOC). Vienna, Austria, pp. 530–545.

Keen, M., Allison, A., Dan, A., Falkl, J., Hately, A., Peng, D., Richter, J. 2008. Case Study: SOA Governance Scenario. IBM Corporation.

Klein, R., Rai, A., 2009. Interfirm strategic information flows in logistics supply chain relationships. MIS Quarterly 33 (4), 735–762.

Kohnke, O., Scheffler, T., Hock, C., 2008. SOA-Governance – an approach to management of service oriented architecture. Wirtschaftsinformatik 50 (5), 408– 412.

Krafzig, D., Banke, K., Slama, D., 2005. Enterprise SOA: Service-oriented Architecture Best Practices. Prentice Hall, Upper Saddle River, NJ.

Kristensen, K., Eskildsen, I., 2010, Design of PLS-Based Satisfaction Studies, In: Vinzi. V.E., Chin, W.W., Henseler. L.. Wang, H. (Eds.). Handbook of Partial Least Squares: Concepts, Methods and Applications. Springer, Heidelberg, pp. 247–277.

Kumar. R.L., 2004. A framework for assessing the business value of information technology infrastructures, Journal of Management Information Systems 2 (2), 11–32.

Kumar, S., Dakshinamoorthy, V., Krishnan, M.S. 2007. SOA and information sharing in supply Chain: ‘‘How’’ Information is Shared Matters!. In: Proceedings of the 28th International Conference on Information Systems (ICIS). Montreal, QC, Canada.

Lawshe, C.H., 1975. A quantitative approach to content validity. Personnel Psychology 28 (4), 563–575.

Lee, J.H., Shim, H.-J., Kim, K.K., 2010. Critical Success Factors in SOA implementation: an exploratory study. Information Systems Management 27 (2), 123– 145.

Leusse, P., Dimitrakos, T., Brossard, D., 2009. A governance model for SOA. In: Proceedings of the IEEE International Conference on Web Services (ICWS). Los Angeles, CA, USA, pp. 1020–1027.

Lewis, B.R., Snyder, C.A., Rainer, R.K., 1995. An empirical assessment of the information resource management construct. Journal of Management Information Systems 12 (1), 199–223.

Liang, H., Saraf, N., Hu, Q., Xue, Y., 2007. Assimilation of enterprise systems: the effect of institutional pressures and the mediating role of top management. MIS Quarterly 31 (1), 59–87.

Lowry, P.B., Romans, D., Curtis, A., 2004. Global journal prestige and supporting disciplines: a scientometric study of information systems journals. Journal of the Association for Information Systems 5 (2), 29–77.

Mitra, T., 2005. A Case for SOA Governance. <http://www.ibm.com/developerworks/webservices/library/ws-soa-govern/> (retrieved 08.20.10).

Moore, G.C., Benbasat, I., 1991. Development of an instrument to measure the perceptions of adopting an information technology innovation. Information Systems Research 2 (3), 192–222.

Niemann, M., Eckert, J., Repp, N., Steinmetz, R., 2008. Towards a generic governance model for service-oriented architectures. In: Proceedings of the 14th Americas Conference on Information Systems (AMCIS). Toronto, ON, Canada, pp. 1–10.

Nunnally, J.C., 1978. Psychometric Theory, second ed. McGraw-Hill, New York, NY.

Papazoglou, M.P., Heuvel, W.-J., 2007. Service oriented architectures: approaches, technologies and research issues. The VLDB Journal 16 (3), 389–415.

Peltz, C., 2003. Web services orchestration and choreography. Computer 36 (10), 46–52.

Petter, S., Straub, D., Rai, A., 2007. Specifying formative constructs in information systems research. MIS Quarterly 31 (4), 623–656

Preacher, K.J., Hayes, A.F., 2004. SPSS and SAS procedures for estimating indirect effects in simple mediation models. Behavior Research Methods 36 (4), 717–731.

Ren, M., Lyytinen, K.J., 2008. Building enterprise architecture agility and sustenance with SOA. Communications of the Association for Information Systems 22 (1), 75–86.

Ringle, C.M., Wende, S., Will, A., 2007. SmartPLS 2.0 (M3) Beta. Hamburg, <http://www.smartpls.dc>.

Sabherwal, R., Chan, Y.E., 2001. Alignment between business and IS strategies: a study of prospectors, analyzers, and defenders. Information Systems Research 12 (1), 11–33.

Sanchez, R., Mahoney, J.T., 1996. Modularity, flexibility, and knowledge management in product and organization design. Strategic Management Journal 17 (Winter Special Issue), 63–76.

Saran, C., 2006. SOA Will Fail Without Governance Warns Gartner. <http://www.computerweekly.com/Articles/2006/09/07/218322/soa-will-fail-withoutgovernance-warns-gartner.htm> (retrieved 08.11.10).

Schelp, J., Aier, S., 2009. SOA and EA – sustainable contributions for increasing corporate agility. In: Proceedings of the 42nd Hawaii International Conference on System Sciences (HICSS). Waikoloa, Big Island, HI, USA.

Schepers, T.G.J., Iacob, M.E., van Eck, P.A.T., 2008. A lifecycle approach to SOA governance. In: Proceedings of the 2008 ACM Symposium on Applied computing. Fortaleza, Ceara, Brazil: ACM, pp. 1055–1061.

Schilling, M.A., 2000. Toward a general modular systems theory and its application to interfirm product modularity. Academy of Management Review 25 (2), 312–334.

Sedera, D., Gable, G.G., 2010. Knowledge management competence for enterprise system success. Journal of Strategic Information Systems 19 (4), 296–306.

Shrout, P., Bolger, N., 2002. Mediation in experimental and nonexperimental studies: new procedures and recommendations. Psychological Methods 7 (4), 422–445.

Siedersleben, J., 2007. SOA revisited: component orientation in system landscapes. Wirtschaftsinformatik 49 (Special Issue), 110–117.

Simon, H.A., 1962. The architecture of complexity: american philosophical society. Proceedings of the American Philosophical Society 106 (6), 467–482

Strnadl, C.F., 2007. Bridging architectural boundaries design and implementation of a semantic BPM and SOA governance tool. In: Proceedings of the 5th International Conference on Service-Oriented Computing (ICSOC). Vienna, Austria, pp. 518–529.

Tewary, A.K., Kosalge, P., Motwani, J., 2009. Piloting service oriented architecture—a case study in the oil industry. In: Proceedings of the 15th Americas Conference on Information Systems (AMCIS). San Francisco, CA, USA, pp. 1–12.

Tiwana, A., Bharadwaj, A., Sambamurthy, V., 2003. The Antecedents of information systems development capability in firms: a knowledge integration perspective. Proceedings of the 24th International Conference in Information Systems Seattle, USA pp. 246–258.

Varadan, R., Channabasavaiah, K., Simpson, S., Holley, K., Allam, A., 2008, Increasing business flexibility and SOA adoption through effective SOA governance. IBM Systems Journal 47 (3), 473–488.

Viering, G., Legner, C., Ahlemann, F., 2009. The (lacking) business perspective on SOA – critical themes in SOA research. In: Proceedings of the 9th International Conference on Business Informatics. Vienna, Austria, pp. 45–54.

Walker, L., 2007. IBM business transformation enabled by service-oriented architecture. IBM Systems Journal 46 (4), 651–667.

Worren, N., Moore, K., Cardona, P., 2002. Modularity, strategic flexibility and firm performance: a study of the home appliance industry. Strategic Management Journal 23 (12), 1123.

Yoon, T., Carter, P.E., 2007. Investigating the antecedents and benefits of SOA implementation: a multi-case study approach. In: Proceedings of the 13th Americas Conference on Information Systems (AMCIS). Keystone, CO, USA, pp. 1–11.

Zhu, K., Kraemer, K.L., 2002. E-Commerce metrics for net-enhanced organizations: assessing the value of e-commerce to firm performance in the manufacturing sector. Information Systems Research 13 (3), 275–295.

Yu, T., Zhang, Y., Lin, K.-J., 2007. Efficient algorithms for web services selection with end-to-end QoS constraints. ACM Transactions on the Web 1 (1), 1–26.
