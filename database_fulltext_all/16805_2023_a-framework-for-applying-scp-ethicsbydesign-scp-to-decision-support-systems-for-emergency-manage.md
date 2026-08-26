---
otero_id: 16805
otero_key: "7FHT3S44"
title: "A framework for applying <scp>ethics‐by‐design</scp> to decision support systems for emergency management"
authors: "Alexander Nussbaumer; Andrew Pope; Karen Neville"
year: "2023"
journal: "Information Systems Journal"
doi: "10.1111/isj.12350"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
S P E C I A L I S S U E P A P E R

WILEY

# A framework for applying ethics-by-design to decision support systems for emergency management

Alexander Nussbaumer<sup>1</sup> | Andrew Pope<sup>2</sup> | Karen Neville<sup>2</sup>

<sup>1</sup>Institute of Interactive Systems and Data Science (ISDS), Graz University of Technology, Graz, Austria

<sup>2</sup>Business Information Systems, University College Cork, Cork, Ireland

Correspondence Andrew Pope, Business Information Systems, University College Cork, Cork, Ireland. Email: a.pope@ucc.ie

## Abstract

The development and utilisation of new information and communication technologies presents opportunities and risks, which bring ethical issues to the forefront. Any attempt to minimise the potential negative consequences to individuals, organisations and society resulting from the use of these technologies is challenging. In order to address these challenges, this paper presents an ethics-by-design approach that has been developed and implemented in the context of Decision Supports Systems for Emergency Management. Such systems help manage large and cross-border disasters by supporting decision makers to respond on emergencies in a reasonable way by taking follow-up actions into account. The approach taken in this paper specifically provides means to support the ethical dimensions of these decisions. Actions taken during disasters can have ramifications that persist long after a disaster has passed. The ethics-by-design approach presented here not only informs the design of systems, but also considers the role and training of the decision makers in the design process. The paper builds on the literature on ethics in information systems and makes a contribution to theory by providing a framework to ensure ethical considerations are embedded into the design of systems.

K E Y W O R D S

computer ethics, decision support, decision support systems,

emergency management, ethics, ethics-by-design

## 1 | INTRODUCTION

Although the design and application of novel technologies introduce opportunities, such activities bring ethica issues to the fore. Consequently, some researchers have warned of the negative and unintended consequences of technology use (Tarafdar et al., 2015). Advances in artificial intelligence (AI) and automation, along with th pervasive use of social media, underscore the need to consider the ethical implications of technology (cf. Jobin et al., 2019).

Quantifying the potential cost to individuals, organisations and society, resulting from technology use, repre sents a significant challenge (Héder, 2017; Stahl et al., 2016). Nonetheless, the exploration of ethical issues associ ated with technology is essential for the advancement of information systems (IS) research and practic (cf. Davison, 2000; Davison et al., 2001; Mingers & Walsham, 2010; Walsham, 2012). Guidelines, (Rogerso et al., 2000) codes of conduct (Oz, 1992), and principles (cf. Myers & Venable, 2014; Walsham, 1996) have bee used to guide researchers to “do no harm.”

Emerging technologies may place a huge burden on users regarding their ethical use. Even those who are fully aware of the importance of ethics can encounter challenges because of cognitive limitations in decision-making (Gigerenzer, 2010). For example, the use of a new technology could lead to consequences that are not fully under stood and foreseen by the user (cf. Tarafdar et al., 2015). As a result, there is a need to embed ethical aspects, and guidance for ethical use, inside the technology rather than placing sole responsibility on the users. This pape addresses the problem of how to integrate ethics in the design process of technology that inherently raise important ethical questions. The key aim of the paper is to create a framework that embeds ethics within the design of a new technology. In particular, it supports the creation of an ethics-by-design approach that addresses the context and lifecycle of a research and development project and includes the user in the design.

System designers bear responsibility to ensure ethical purpose (respecting fundamental rights, principles and values) as well as technical robustness in the design, development and deployment of new systems (cf. Friedman et al., 2008). However, there remains few holistic guidelines for researchers who wish to incorporate ethical consid erations into artefact design (cf. Chatterjee et al., 2009). This paper proposes, theory engrained, practical guideline that can be used by IS designers and researchers to proactively minimise the negative consequences of IS design and use.

Building on the literature in IS and computer ethics, the ethics-by-design approach was developed and implemented in the context of a three-year funded security capability research project incorporating the develop ment of a decision support system (DSS) for emergency management (EM). The goal of this system was to support decision-makers to make “good” decisions that consider the consequences of follow-up actions. The design of systems to help manage large and cross-border disasters present unique challenges. The allocation of life-savin resources, for example, may result in ethical dilemmas, which present decision makers with equally undesirable out comes (Geale, 2012). Actions taken during disasters can have ramifications that persist long after a disaster has passed. Concepts of ethics and behaviour in EM decision-making have societal implications which may advanc scholarship and practice in analogous settings where the allocation of, and application of, life-saving resources ma present ethical dilemmas which often include equally undesirable outcomes (Geale, 2012). This paper builds on previ ous research which argues that ethical considerations should be incorporated into IS design (Friedman et al., 2008; Stahl et al., 2014). Furthermore, the authors propose that research focusing on the ethical obligations inherent in EM research may provide useful insights for IS researchers.

This paper contributes to the literature both in addressing the call to embed ethics into system's design and pro viding a practical approach to evaluating the ethical dimensions of technology artefacts. Although this work look specifically at DSS for EM, the design could be adopted by other types of IS that have societal impact, especially in connection with new technologies.

This paper is organised as follows. Section 2 explores the discipline of EM and describes the challenges, and inherent difficulties, associated with multi-agency EM. Next, the use of technology for EM is discussed and the S HELP system is introduced. Following this, ethical issues associated with technology design and usage are discussed Section 3 presents a framework for integrating an ethics-by-design approach into a DSS for EM. The framewor engages with the academic literature on computer ethics and ethical assessment. The framework provides guidanc in the application of ethics-by-design in information systems development. A practical example of this is presente in Section 4 through the design, development and evaluation on S-HELP. Finally, Section 5 discusses the contribu tion of our research on ethics research and computer ethics, as well as information systems development.

## 2 | BACKGROUND

## 2.1 | Emergency management

Natural and manmade disasters have the potential to cause widespread loss of life and long-lasting economic damage (Farazmand, 2014). Cascading disasters can also result in amplification and subsidiary events, which can devastate critical infrastructure (Pescaroli & Alexander, 2016). Due to the multifaceted nature of disaste types and durations, planning and responding to such events requires a multidisciplinary approach (Noran, 2014). In addition to widespread loss of life, large-scale disasters can place a significant burden on decision-making (Zhou et al., 2018) and the global supply chain (Laugé et al., 2015). Collaboration and coordina tion represent significant challenges in EM (Carlson et al., 2017). Each agency often has its own control struc ture, objectives, standard operating procedures (SOPs), terminology and even organisational culture (Kapucu et al., 2010; Salmon et al., 2011). Yet despite these differences, agencies must often work together towards a common shared goal. A coordinated response often requires agencies, who have not collaborated before, to collaborate despite fundamentally different remits (cf. Weick & Sutcliffe, 2007). The COVID-19 pandemic dem onstrates the need for a coordinated global response requiring expertise from a myriad of disciplines operating in unfamiliar territory (ECDC, 2020; Pisano et al., 2020).

EM refers to the coordinated activities, which seek to control and reduce the impact of disasters. The formalisation of the discipline first took shape in 1950s America due to the threat of nuclear war (Haddow et al., 2017). Since then, the discipline has moved from top-down hierarchical control structures towards more flexi ble collaborative models (Waugh Jr & Streib, 2006). In such arrangements, interoperability and coordination are key Coordination and control represent real challenges when multiple agencies, including civilian organisations, must col laborate in unfamiliar territory with new control structures (cf, Bharosa et al 2010: Lanzara, 1983: McMaster 8 Baber, 2012; Quarantelli, 1988; Salmon et al., 2011).

## 2.2 | Technology for EM

Effective interorganizational and cross disciplinary communication are pertinent both to the domain of IS and EM (Beydoun et al., 2018). According to Chen et al., (2008, p. 202) an effective information supply chain is crucial to facilitate inter-organisational and intra-organisational cooperation that is the hallmark of EM. Indeed, sensitivity to the initial conditions of a disaster and relationships with other organisations, including community groups, can hav more of an impact than leadership in EM (Koehler et al., 2014). Though information systems (IS) can play an important role in this regard, IS often play only a tangential role in the EM literature (Leidner et al., 2009). Nonethe less, the promise of technology-enhanced EM has been a feature of the EM literature since the 1970s (cf. Quarantelli, 1978). Since then, many ICT tools have been used to support the human activities of EM (Hu & Kapucu, 2016). Examples include two-way radios, global positioning systems (GPS) enabled devices, internet of things (IoT) devices and sensors (Ray et al., 2017) and satellite phones. Dedicated standalone information system for EM have also emerged. Sahana EDEN, for example, is a server-based disaster management information system (DMIS) that was introduced in the aftermath of the 2004 Indian Ocean tsunami (Rafi et al., 2018). Perhaps accounting for the unique signature of each disaster type, numerous discrete information systems to support EM have also emerged. These include: DSS (Van de Walle & Turoff, 2008; Wallace & de Balogh, 1985), knowledge management systems (KMS) for EM (Dorasamy et al., 2013), EM information systems (EMIS) (Carver & Turoff, 2007), geographic information systems (GIS) (Cova, 1999), hazard analysis and modelling systems (Zerger & Wealands, 2004) and resource management systems (cf. Özdamar & Ertem, 2015; Sangiamkul & Van Hillegersberg, 2011). Social media and crowdsourcing tools have also been used successfully in EM (McCormick, 2016; Reuter et al., 2012; Tim et al., 2017) though their use is not without drawbacks (cf. Alexander, 2014). The IS literature often views EM through the lens of information sharing and interoperability (Allen et al., 2014) both in terms of information qualit and the architectures and tools which facilitate it (Bharosa et al., 2009). However, there remains a gap regarding how ethics can be embedded in IS to support interoperability and multi-agency collaboration. The following section provides a description of a development project, which incorporated an ethics-by-design approach.

## 2.3 | The S-HELP approach

S-HELP is a DSS designed to be used by strategic decision-makers during large-scale disasters. The DSS provide access to features and functionality via modules. It was designed and developed using open-source tools and frameworks. A key feature of the DSS is a situation management console (Figure 1), which provides users with the ability to create, modify, and delete situations (disaster events). The underlying database management system (DBMS stores data about the incident type (e.g., flood, epidemic, explosion), location and severity. Depending on the situa tion type and location, the system will provide disaster-specific information and decision support. For example, flooding event will require a different approach to COVID-19. S-HELP manages “live” disasters and allows users to review historical disasters for training and debriefs to leverage expertise and knowledge from past situations. The DSS also provides users with dynamic information management (IM) boards

These boards (Figure 2) visualise and display incident-related information and guide the decision-making process during response. The boards provide a common operational picture, which can be used by different stakeholders. The use of boards (often whiteboards) is common in EM. Digital boards allow for multiple partici pants, irrespective of location, to concurrently update the operational picture. Roles and permissions can b modified to assign observer-only access for community groups or enable active participation during th disaster.

Although the boards are actively managed by a trained information manager, the situation log contains an immu table, timestamped copy of all data collected. It provides auditing capabilities, post-disaster, to review decisions an the data used. Information gathered on the IM boards can be used to identify the strategic aims, priorities and ke issues to assign tasks. For example, a strategic aim might be to protect the health of the public, while a key priorit could include lowering the surge of hospital admissions. A key issue might focus on preventing the spread of infec tions. Table 1 provides a description of each module.

The next section discusses the importance of ethics-by-design for the design and development of DSS solutions for EM.

<table><tr><td>Name</td><td>Description</td><td>Primary Type</td><td>Created By</td><td>No. Incidents</td></tr><tr><td>Flood</td><td>Flooding in</td><td>Flood</td><td>Admin</td><td>1</td></tr><tr><td>Flooding Event</td><td>Main street and surrounding roads impassible</td><td>Flood</td><td>User 1</td><td>3</td></tr><tr><td>Chemical Cloud</td><td>Toxic cloud of unknown content</td><td>Chemical</td><td>User 1</td><td>1</td></tr><tr><td>Airport Crash</td><td>Light aircraft crash landing</td><td>Aviation Disaster</td><td></td><td>2</td></tr></table>

Incidents for: Chemical cloud  
![](/api/attachments/7FHT3S44/fulltext/images/eede385c49187e32d77b994f4d12e08fe2e8f80a67ff4d89e5c5d066c4aec705.jpg)  
F I G U R E 1 Situation console/module where users can register and manage disaster events [Colour figure can be viewed at wileyonlinelibrary.com]

![](/api/attachments/7FHT3S44/fulltext/images/de435fd8fee39c29eaed99cb60ee70750e45fdf14fa30467f58f46d31aa10eed.jpg)  
F I G U R E 2 Information management boards (data deliberately obscured) [Colour figure can be viewed at wileyonlinelibrary.com]

T A B L E 1 Overview of S-HELP modules and functionality

<table><tr><td>Module</td><td>Functionality</td></tr><tr><td>Situation module</td><td>Creates new situations and utilises live and historical situations</td></tr><tr><td>Situation log</td><td>Records all disaster data, provides real-time updates to the mgt boards</td></tr><tr><td>Information management boards (RCS)</td><td>Provides information management and visualisation capabilities of the DSS to build the common operational picture or recognised current situation (RCS). The boards deliver situational awareness to strategic level decision-makers. Boards can be shared, edited and remotely by multiple participating agencies.</td></tr><tr><td>Aims &amp; key issues</td><td>Enables the creation, presentation and prioritisation of strategic aims</td></tr><tr><td>Casualty module</td><td>Efficient tracking of casualty-related data using customizable reporting.</td></tr><tr><td>Action module</td><td>Creates and assigns time-sensitive actions leveraging the DSS taxonomy to enable cross border and inter-agency coordination and collaboration.</td></tr><tr><td>KM module</td><td>The knowledge management (KM) module stores, shares and surfaces knowledge assets utilising the type and geographic location of the disaster</td></tr><tr><td>LMS module</td><td>The learning management system (LMS) module trains, evaluates and tracks users decision-making knowledge and donning and doffing of personal protective equipment (PPE) procedures.</td></tr><tr><td>Resource allocation (DSS)</td><td>Built on a taxonomy incorporating emergency phases and tasks, the DSS allocates personnel, resources and tasks depending on the emergency management phase and disaster type.</td></tr><tr><td>Crisis Communications tool</td><td>Used to quickly create and disseminate information and alerts to the public and community groups via e-mail and social media channels.</td></tr><tr><td>GIS module</td><td>This geographic information system (GIS) module utilises a spatial database for planning. The module is equipped with relevant datasets to plot capabilities and disaster specific models (for e.g., plumes and floods).</td></tr><tr><td>Social Module</td><td>Monitors social feeds for disaster-related content in real time. Trending issues are clustered and illustrated on the GIS. Provides a mechanism to manage and display content from verified users and reputable sources.</td></tr><tr><td>Weather module</td><td>Provides real-time weather reports utilising the location of the event, incorporating temperature, wind direction and air pressure.</td></tr><tr><td>Reporting generator</td><td>Rapidly converts and exports Information Management data for policymakers, the public and invested stakeholders.</td></tr></table>

## 2.4 | Ethics in EM and information systems

The practice of EM and the use of technology therein prompt fundamental ethical dilemmas. However, the consideration of ethical issues may improve the likelihood of successful outcomes (Geale, 2012). One of the paradoxes of technology is that as our dependence increases so too does our vulnerability (Héder, 2017; Zack, 2010). Equally problematic, and controversial, is the allocation of resources during a crisis (cf. Hardin, 1996). We are seeing this sce nario unfold in the COVID-19 crisis where personal protective equipment (PPEs) is in short supply (cf. Wallac et al., 2020). We may see a similar dilemma with respect to allocation of vaccine stocks. This scenario could be exacerbated by IS that utilise algorithms for decision-making, or predefined models for resource allocation. Decision making algorithms have been used successfully in emergency medicine (cf. Widgren & Jourak, 2011). However, the variability of disasters types and severity levels in EM present challenges (Pescaroli et al., 2018)

It can be observed that many ethical frameworks exist both within and outside the domain of healthcare an EM (Geale. 2012). In general. these frameworks explicitly state ethical values and articulate different processes and methods to assess technology in light of these values. In particular, ethical impact assessment framework provide means to assess the ethical soundness of new technologies (e.g., Wright, 2011). These approaches facilitate ethical assessments before, during and after the development of a technology, as well as influencing designs for new technologies (Reijers et al., 2018).

The approach described in this paper incorporates elements of the aforementioned frameworks but extends each of them. Bélanger and Crossler (2011) have criticised the contribution of information privacy research in the IS literature, and advocate approaches that incorporate design and action. In contrast to general ethical frameworks and those represented in the domain of healthcare/EM, our framework presents more detail on how ethical value influence the design process. This is similar to privacy-by-design approaches, but takes into account general ethica values, not only privacy. Ethical frameworks in the context of autonomous decision-making focus on the ethics of decisions solely made by software and how to assess them. However, our approach focuses on ethical decisionmaking as a combination of human and technical dimensions. This positioning is a unique characteristic of our ethica framework, as it presents details on the software design, and how general ethical values and considerations ar reflected in a way that supports ethical decision-making in DSS

## 3 | FRAMEWORK FOR CREATING AN ETHICS-BY-DESIGN APPROACH

This section presents a framework for creating an ethics-by-design approach for computer applications in the context of EM and DSS. Such an approach addresses the ethical considerations and concerns of new computer applica tions in a holistic way. This is important, because traditional ethical rules are often ill suited to new technica solutions, which can lead to a policy vacuum (Moor, 1985). Addressing this shortcoming, Gotterbarn (1999) propose the creation of a dedicated ethics role so that ethical considerations are embedded in software development. These considerations lead to an ethics-by-design approach, where ethical policies as well as the innovation policy, or approach, are part of the developed software

In addition to classical computer ethics, which deals with the ethical use of computers, the ethics-by-design approach deals with design principles and guidelines so that the software itself follows ethical rules or support humans to follow ethical rules (Gotterbarn et al., 1997). While Gotterbarn (1999) addresses the topic of integrating ethical considerations with computer applications, our approach incorporates the research and development (R&D) process that leads to the development of new applications. To achieve this, a framework has been elaborated that captures ethical aspects, relevant to EM, and provides guidelines on how to apply and verify an ethics-by-design approach throughout the R&D process.

The key components of this framework are (a) a research and development process that provides anchors to integrate ethical design decisions, (b) the definition of the scope where ethical considerations are to be applied (c) the methods to identify ethical requirements and values, (d) the elaboration of design principles that guide th research and development, and (e) a methodology for how to perform ethical assessments. Figure 3 presents and overviews of ethics by design framework.

This framework has been elaborated and applied in the specific context of EM and DSS. However, the overal concept can be transferred and applied to other domains, as discussed in Section 5. In particular, it serves as a guid for how to develop, apply and assess ethics-by-design in any other domain.

## 3.1 | Research and development process

The first part of the framework consists of the integration of ethical design decisions into the research and develop ment (R&D) process. Overall, the ethics-by-design approach consists of a process that integrates EM R&D with ethi cal aspects relevant in this domain. These include the ethical values and ethical impact assessment, as used in existing ethical frameworks. Reijers et al. (2018) describe three types of methods for ethical impact assessment based on ethical values. These are ex-ante methods dealing with emerging technologies (e.g., anticipatory ethics of emerging technologies [Brey, 2012]), ex-post methods dealing with existing technologies and intra methods dealing with technology design.

![](/api/attachments/7FHT3S44/fulltext/images/940613c91357ae4f3f4b734f531dd05553ae7f9f9531b84bf415c4f014c8775d.jpg)  
F I G U R E 3 The diagram gives an overview of the ethical framework with its five key components

Our framework takes up these three types of methods for impact assessment and aligns them closely with agile software development (cf. Agile Alliance, 2001). The approach aims to elicit requirements and develop solutions through the collaborative effort of the development teams in cooperation with end-users and stakeholder (cf. Cockburn & Highsmith, 2001; Ramesh et al., 2010). In contrast to big upfront deliverables, an adaptive and flexi ble approach is established which considers changing and evolving requirements throughout the development life cycle (cf. Nerur & Balijepally, 2007). It employs an adaptive and iterative approach with an emphasis on frequent delivery of working software (Lee & Xia, 2010). Like the agile stage-gate hybrid model of software development (Cooper & Sommer, 2016), our approach uses checkpoints, or ethical stage-gates, to progress and adhere to ethica considerations.

The ethical stage-gates are implemented periodically during the research and development process and incorpo rate a combination of three activities. First, ethical requirements are identified and translated to ethical values. Sec ond, ethical design principles are elaborated so that they can be integrated in the software application and training Third, an assessment is performed that reveals the ethical impact on society. Which activities are performed depend on the temporal placement of the ESGs in the R&D lifecycle (beginning, during, and the end of the R&D process)

Initially, ethical requirements elicitation is the prevalent activity, which progresses into the formulation of ethica values later on. Ethical impact assessment is conducted with ex-ante methods to anticipate the impact at the begin ning and applies ex-post assessment methods at the end. The elaboration of ethical design principles is prevalent during the R&D process, as they influence the implementation.

It is important to mention that the three activities conducted at an ESG have a strong interplay. For example, an ethical impact assessment delivers ethical requirements that are used for creating design principles. In the initial plan ning phase of an R&D project, it should be specified how many ESGs are needed and when they occur. An overview of this framework with all these components is depicted in Figure 3. The following subsections provide further details on the individual components of the framework

## 3.2 | Scope and application domain

The second component of the ethical framework targets the identification of the scope and application context, where ethical considerations are to be applied. In our case, the application domain includes EM supported by DSS Thus, the scope of ethical considerations includes the system to be developed, the training methodology, end-users and stakeholders affected by the system. The identification of scope and application context can be achieved wit the help of scenarios tailored to the application domain. While traditional technology assessment focuses on policy makers, Constructive Technology Assessment (CTA) follows a co-evaluative approach with a socially embedded research process that includes all stakeholders in activities (Konrad et al., 2017). Like CTA, Social Impact Analysi (SIA) involves the key actors in the assessment, tries to prevent or repair negative consequences and considers socia impacts in the design (Becker, 2001). SIA applies a process that involves stakeholders in each step including, scenario design, impact analysis, mitigation of negative impacts, and reporting. Like CTA and SIA, our framework proposes th identification and integration of the main stakeholders. Our approach also proposes the creation of real-life scenarios. Following Konrad et al. (2017), the development starts with simple scenarios and then expands to explore differ ent directions, situations and actors. Including well-defined scenarios and stakeholders will demonstrate how th software application is used. Scenarios facilitate the elicitation of ethical requirements, the creation of ethical design principles, and ethical impact assessment

In contrast to other ethical frameworks, our approach includes both technical and human dimensions, as well a the interaction between them. While Moor (1985) raises concerns about a policy vacuum in respect of how com puters are used, Wright (2011) presents a framework for ethical impact assessment that seeks to address the prob lem. Though Wright's framework contains a broad overview of ethical values and assessment methods, it stil focuses on the use of the technology. In our case, human decision-making is a central aspect of the applicatio domain, which must be taken into account regarding the ethical design. Consequently, training activities that improve human decision-making skills are used. In EM, there are ethical implications associated with making soun decisions to avoid harm and making ethical decisions that consider the wider impact on society

Another aspect of current ethics-by-design approaches is ethical decision-making in artificial intelligence (AI). AI enables software to make autonomous decisions in a variety of situations such as autonomous vehicles (Hevelke & Nida-Rümelin, 2015), personal digital assistants (Maedche et al., 2019), or healthcare robots (Van Wynsberghe, 2016). Bak (2020) cautions that computer models and simulations are rarely morally neutral and highlights the importance of collaborating with stakeholders to incorporate ethical considerations “by design.” Dignum et al. (2018) outline a framework for ethical decision-making that focuses on accountability, transpar ency and understandability. They highlight the difference between human and machine-based decision-making by stating that decisions taken by machines must be justified, transparent, and explainable. Though our frame work relies on human decision-making with the help of information systems, these aspects of autonomou decision-making should be taken into account, if the developed system contains smart or autonomous decision-making.

## 3.3 | Ethical requirements and values

The third component consists of the ethical requirements analysis, which progresses to ethical value definition. Thi process starts at the first ESG as a collection of ethical requirements. During subsequent refinement activities, at later ESGs, these requirements will be categorised and translated into a small set of ethical values. This proces should be accompanied by a literature review of existing ethical frameworks that list ethical values relevant to th application domain (e.g., Wright, 2011).

Another important aspect of this step is its connection with the ethical impact assessments at the same ESGs The outcome of the impact assessment is taken up as ethical requirements for the software and training design which are then translated into functional or non-functional software requirements. These requirements inform th creation of the ethical design principles (see next subsection). This clearly demonstrates the interplay between ethi cal impact assessment, requirements analysis and design principles that is the output of an ESG activity, performed during the R&D process, informs subsequent activities

The following ethical values were identified as relevant in the context of EM and decision-making. They resulte from both a literature review and focus groups with relevant stakeholders during the application of the ethics-by design approach (see Section 4). Though this set of values fits to the application domain of EM and DSS, it might b different in other application domains. The relevance of ethical values is articulated and summarised as follows:

• Transparency. The justification and ethical considerations for decisions made in response to a disaster must b transparent and comprehensible (Landesman, 2012). The justification includes information on the circumstances and why and how the decisions have been made. Furthermore, all stakeholders should be included in th decision-making process, in order to make them aware of the reasons and potential risks of decision (Upshur, 2002). Decisions taken should be available post-incident for debriefing and formal auditing. This is even more critical when decisions are made, or enabled, by algorithms. Though there is a perception that machines ar infallible. Zarsky (2016) states that such a view is misguided. Rather, greater automation demands greater trans parency (ibid). The importance of transparency is reiterated by Turilli and Floridi (2009) who state that transpar ency is a pro-ethical condition that can impair, or enable, other ethical practices and principles. Childress and Gaare Bernheim (2008) relate honest and truthful communication with the transparency principle

• Responsiveness. The speed of access to information in EM is vital to minimise harm arising from a lack of resources. Responsiveness, as well as the adjunct values timeliness and rigour are most relevant for ensuring effective and high-quality EM (Hunt et al., 2016). Decisions should be reviewed and revised if required. Respon siveness is particularly relevant to system design as optimal performance in situational awareness is vital. Deci sions made quickly can minimise harm, while delayed decisions might lead to increased harm in the time when no response to emergency is provided. A DSS should easily access the current operational picture/situation throug a well-designed user interface.

• Reasonableness. Responders should base their decisions on science, empirical data, best practice, principles and experiential knowledge to ensure decisions are proportionate and appropriate (Geale, 2012; Landesman, 2012) However, in a pluralist society, people might disagree on what is reasonable, which can lead to a prioritisation problem (Daniels, 2000). In the case of Personal Injury Evaluation Systems (PIES) and Judicial Support System (JSDSS), for example, there is evidence that judgements are being made by less well-trained assessor (Person, 2000). Providing decision-makers with adequate training can help to address this.

• Data protection and privacy. The technical framework and security measures should be designed to guarante that all personal data are safe from unforeseen, unintended or malevolent use (European Commission, 2013). Pri vacy and confidentiality should be protected carefully in healthcare (Childress & Gaare Bernheim, 2008). Privac concerns several aspects of a person, including information about the anonymity, the communication, and th body of a person (Wright, 2011). This is relevant for end-user participation, as it outlines how data are processed and ensures that end-user privacy is respected. It relates to the training approach as trainee data need to b secured. The system design phase must incorporate steps and controls to assure confidentiality. The integrity and availability of the data created by, and pertaining to, decision makers must be secured

• Justice and fairness. Justice incorporates equality and non-discriminatory principles. All stakeholders shoul receive equal access to healthcare and risks should be managed carefully, irrespective of race, age, gender and nationality. Scarce resources should be fairly distributed amongst victims (European Commission, 2013 Landesman, 2012). Benefits and burdens should be distributed equitably (Childress & Gaare Bernheim, 2008) and limited resources should be distributed fairly (Geale, 2012). This value relates to the system design and facilitates fair and blind EM. For example, a resource management tool should not allow decision-makers to prioritise a spe cific cohort.

• Precaution. Precaution must be taken in order to understand and assess risks in the emergency mitigation and planning phases. Precaution strongly relates to avoiding, preventing and removing harm (Childress & Gaar Bernheim, 2008). Upshur (2002) argues that reducing public harm justifies interventions. However, such interventions should be taken with caution and must be justifiable. Limiting harm is also an ethical rule in disaster situa tions with limited resources (Geale, 2012). An impact assessment of the risk of different disaster types should be performed in advance (European Commission, 2013). This value relates to the training approach for developin decision-making competencies. Trainees should learn to assess the ramifications of decisions that are taken.

Though listed as individual values, many of the values are interrelated. Daniels (2000), for example, argues that fair process will involve transparency about the grounds for decisions. While there are good reasons for all these principles, the application of public health intervention guided by these principles might conflict with the genera value of liberty. Childress and Gaare Bernheim (2008) name five justificatory conditions for such interventions: effec tiveness, necessity, least infringement, proportionality and impartiality

Legal issues are often considered in conjunction with ethical issues. Though transparency and data protection are ethical values, many countries have legal regulations pertaining to the transparency of decision-making and th protection of personal data. While legal aspects vary from country to country, ethical values are more general and often include legal aspects. Thus, the focus must be the ethical aspects. However, referring to legal aspects provides a valuable source of consideration.

Humanitarian principles are closely tied to ethical aspects. The United Nations (UN) General Assembly Resolu tion 46/182 declares that humanitarian assistance must be provided with respect to principles of humanity, neutral ity, impartiality and independence. By adhering to these principles, practitioners can achieve a measure of accountability from the wider humanitarian community. As per the legal issues discussed above, humanitarian princi ples provide a source of identifying relevant ethical values.

## 3.4 | Ethical design principles

The fourth component deals with the translation of ethical requirements and values into concrete design principles that inform and guide the software development and training activities. This translation is most relevant as it inherently enriches software and training components with ethics that influences the human behaviour an usage of these components. However, the translation can be difficult and time consuming. While some ethica requirements can take the form of functional software requirements that are easy to implement, others can take th form of non-functional requirements that do not provide clear instruction for implementation. Thus, a collaboratio between the technical and ethical team members is needed for the formulation of ethical requirements a implementable design guidelines

This procedure is similar to the value-sensitive design (VSD), which aims to influence the technological design by explicitly identifying human values to be considered and integrated throughout the design proces (Cummings, 2006; Friedman et al., 2013). The formalised VSD methodology consists of a three-part iterativ approach, which includes the investigation of conceptual, empirical and technical issues specific to a particula design. The conceptual investigation consists of an analysis informed by the philosophy of those value constructs rel evant to the design in question. The technical investigation aims to assess how the technology supports particula values and how values identified in the conceptual investigation could be supported by different design possibilities The empirical investigation focuses on human interaction with the technology.

Another example that pursues a similar approach to our framework is privacy-by-design, which seeks to inte grate regulations and ethical rules in software design (cf. Cavoukian, 2009; Cavoukian et al., 2010). It advocates an approach whereby systems should be designed and built with an emphasis on avoiding, or limiting, the amount of personal data that is processed (Schaar, 2010). This approach was reinforced by the general data protection regula tions (GDPR) that became enforceable in 2018 in the EU and became a model for many national laws outside th EU. GDPR includes several principles on the use of private and personal data, such as granting rights to the data sub ject (e.g., right to erase personal data) and ethical processing of personal data (e.g., anonymization, data minimization). Adopting these principles in phased software design and development leads to privacy-by-design approache that integrate privacy principles in software design. In contrast to privacy-by-design that focuses on one specific value, our framework is open to other ethical values and promotes the identification of relevant ethical values

## 3.5 | Ethical impact assessment

The fifth component of the framework is the ethical impact assessment. Typically, an ethical impact assessment investigates how the use of a product might negatively affect society (Wright & Friedewald, 2013). In our framework, the ethical impact assessment has two distinct objectives. First, it should deliver ethical requirement that can be translated to design principles for the software and training as described in Sections 3.3 and 3.4. Second it should verify the ethical soundness of the final product. While the first goal is primarily achieved with impact assessments at an early stage of the R&D process, the latter goal is achieved with impact assessments at a late phase of the R&D process.

In general, ethical impact assessment can be defined as a process during which an organisation, together with stakeholders, considers the ethical issues or impacts posed by a new project, technology, service, program, legisla tion, or other initiative, to identify risks and solutions (Wright & Friedewald, 2013). An ethical impact assessmen framework is presented by Wright (2011) that advocates the use of ethical impact assessments and provides a struc ture for undertaking such assessments. It consists of a collection of ethical principles (values) that should be consid ered and provides questions to assess whether these principles have been adhered to. The second part of th structure is a set of tools that can be used by decision-makers to engage stakeholders in considering the principles values and issues. Examples are expert workshops, checklists of questions, ethical matrix, or citizen panels and real world disaster scenarios for EM preparation, response, debriefs and training.

Our framework involves stakeholders in the aforementioned exercises to perform impact assessment. However. while existing ethical frameworks and methods focus on either ex-ante or ex-post methods (Reijers et al., 2018), ou approach includes the whole spectrum of ethical assessments. This has the advantage of applying ethical aspects throughout the development lifecycle. Ex-ante methods are employed at an earlier R&D phase and are characterised by conducting workshops or focus groups that involve a small number of stakeholders, which are more effective in discussing and creating new ideas. Ex-post methods are conducted at a later R&D phase and involve larger stake holder groups with stakeholders from different areas and of different types. This ensures a sound and complete ethi cal verification. Ex-ante methods inform the formulation of requirements and values, and the design of the product Ex-post methods verify the ethical soundness of the final product.

The framework proposes the use of task and scenario-based methodologies in both focus groups and studies Task-based exercises reguire more precise and in-depth work from the participants. because they have to delive results. Through the use of realistic scenarios, the tasks are not abstract, and stakeholders can do the assessment from their viewpoint (different for each stakeholder group) related to a concrete situation. A scenario consists of five basic elements: (1) the nature of the disaster for example, what, where, when and who? (2) ground rules and logistica factors (3) participant roles and stakeholders (4) scenario objectives; and (5) complicating factors or setback (Alexander, 2000). Although this study used scenarios for ethical evaluation, the use of scenarios for IS development is well established (Sutcliffe, 2003). Furthermore, the use of mock-ups, draft screenshots, pencil-and-paper approaches allows an assessment before the implementation (Beynon-Davies et al., 1999; Camburn et al., 2017). In particular, the requirements analysis and creation of design principles are undertaken before an implementation

## 4 | APPLYING ETHICS-BY-DESIGN IN THE S-HELP APPROACH FOR MANAGING EMERGENCIES

This section describes the practical application of the ethical framework and its integration with the R&D of the S-HELP project. This project aimed to develop a DSS and methodology for multi-agency decision-making during largescale emergencies to support rapid and effective DM across all stages of EM (Neville et al., 2016). Beside the devel opment of a system consisting of various tools for supporting the whole decision-making process in emergency situ ations, research has been undertaken to train decision-makers in the use of the system. This section describes th overall approach and details of how the ethical framework has been applied. In doing so, it provides a means throug which researchers, creating applications in different domains, can adapt the framework to implement their ow adapted ethics-by-design approach.

The first step consisted of the identification of the relevant stakeholders. In the S-HELP project, the stake holders comprised researchers and practitioners in the field of public health, EM and decision-making. Additionally as potential victims of a disaster, the public and local population were deemed to constitute a stakeholder group that is affected by the outcomes of the project.

The R&D process was planned with three ethical stage gates (ESGs), one at the beginning of the project, one in the middle and one at the end. At the first ESG, an initial ethical requirement elicitation and ex-ante impact assess ment was conducted by the project members and relevant stakeholders. This resulted in the formulation of an initia set of ethical requirements and design principles:

• User participation needs to be regulated by privacy and data protection practices, such as the use of informed consent forms, as well as respect of anonymity in user studies, workshops and training sessions

• User interfaces should be designed in a way that end-users can quickly and easily access EM information, especially in stress conditions.

• The proper and effective use of the DSS in EM situations needs trained end-users (decision-makers in EM).

• The effect of the use of the DSS in EM should avoid harm to society or at least minimise and balance non avoidable harm.

At the second ESG, and after the initial development phase, a focus group workshop was conducted to under take the first ethical review including a further ethical impact assessment, ethical requirements elicitation, and an exercise for elaborating design principles. The workshop included experts in the field of decision-making, ethics, EM and public health. The group was presented with the system user interface (UI) wireframes along with scenarios detailing how the system could be used. Participants were then asked to analyse the existing and planned feature regarding their ethical impact on society, to identify relevant ethical values and to elaborate design recommendations (listed in Table 2). The recommendations were summarised and categorised according to six ethical values (se Table 2). These ethical values were first identified on the basis of a literature review and subsequently approved b the focus group participants.

T A B L E 2 Overview of how ethical values are applied in different fields

<table><tr><td>Ethical value</td><td>System design</td><td>Training approach</td></tr><tr><td>Transparency</td><td>The system provides a mechanism to record what decisions have been made to facilitate subsequent justification of unpopular decisions.The Situation Log Module records this information.</td><td>Trainees are made aware that their decisions and activities are recorded by the system for later review</td></tr><tr><td>Responsiveness</td><td>The user interface facilitates convenient and quick access to critical information.Notifications on the RCS module (information management boards) alert participants to changes and updates. Quick and timely access to information is especially important during emergencies.</td><td>A training module allows users to practice accessing critical information, to familiarise themselves with the systems capabilities of providing quick access to emergency information.</td></tr><tr><td>Reasonableness</td><td>The system provides relevant information on the current emergency situation in order to get a full picture of an emergency. The knowledge management (KM) module provides decision-makers with access to relevant standard operation procedures and emergency plans. This helps decision-makers to make decisions in a reasonable way.</td><td>Stakeholders who are responsible for making decisions are trained to make appropriate decisions. A decision-making training program has been set up for this purpose.</td></tr><tr><td>Data protection and privacy</td><td>Data gathered from victims and decision-makers are protected. For example, casualty data are decoupled from patient data and data from decision-makers is only available to their supervisors.</td><td>The training includes information about the privacy rights of victims. Furthermore, information relating to trainees and their training progress is visible only to trainees.</td></tr><tr><td>Justice and fairness</td><td>The system facilitates access to all relevant emergency information (e.g., human, health and first responder resources, situation overview, geographic information), which is a prerequisite for fair decisions. Several modules support this access including, the Weather Module, the Geographic Information System and the Situation Module.</td><td>The training emphasises that a core goal of EM is to avoid harm and that a good overview of the current situation supports balanced decisions. The decision-making training helps understand decision alternatives and the consequences of such decisions on society. Furthermore, trainees are trained to take all available emergency information into account.</td></tr><tr><td>Precaution</td><td>The knowledge management module surfaces related past incidents so that decision-makers can leverage past experience on current incidents. The use of modelling, such as flood and chemical plume models, help decision-makers assess the impact of decision alternatives before actually making decisions.</td><td>End-users tasked with decision-making are trained in decision-making to enhance the understanding of decision alternatives and consequences, which ensures decisions are made with care whilst considering the ramifications of such decisions.</td></tr></table>

The recommendations from the focus group and literature review were categorised on the basis of the values identified in the literature review. To facilitate transparency, the focus group recommended that all decisions taken during an incident should be recorded. To ensure responsiveness, the focus group recommend the creation of an accurate informational picture that would be customised depending on the incident type and user role. Reasonable ness was considered both in terms of access to relevant knowledge and ensuring adequate training for decision makers. In order to ensure data protection and privacy, the focus group recommended securing the storage of, an access to, personal data. Furthermore, it was recommended that only data from trustworthy sources should b considered for decision-making. The latter was to be considered when displaying live data from social channels for example, Twitter. To uphold justice and fairness, the focus group recommended providing decision-makers wit access to relevant data on environmental conditions, local infrastructure and vulnerable members of the community It was recommended that decision-makers should also be trained to evaluate the consequences of decision alterna tives. Finally, the system should ensure that all decisions avoid, or minimise, inflicting harm on affected people and victims.

![](/api/attachments/7FHT3S44/fulltext/images/27fe115ba24759da5aa3a59028aebfe9b4b9ec0c018e751728b27c3ea61a41a7.jpg)  
F I G U R E 4 The ethics-by-design approach as demonstrated in the S-HELP project

Based on the recommendations, design principles have been elaborated that inform the system and training design. An overview of the most relevant principles is presented in Table 2.

The final ethical stage-gate incorporated an evaluation to determine if the ethical values, previously outlined, were appropriately and sufficiently incorporated in the system. This evaluation was conducted over the course of three scenario evaluations (biological scenario, flood scenario, chemical scenario) with experts from EM and healthcare. Tremblay et al. (2010) recommend adapting focus groups for design research incorporating exploratory focus groups and confirmatory focus groups. Although an exploratory focus group was conducted in this study, a confirmatory focus group was not possible. The ethical soundness and especially the adherence to the elaborated ethical values represented only one component of the multiple evaluations that were being conducted across the three scenarios. A survey approach was chosen because it could be conducted after the system technical evaluation had taken place. As such, it was complimentary to the scenario evaluations. The use of a survey, on conclusion of th technical evaluation, fulfilled some of the benefits gained through confirmatory focus groups. It facilitated the evalu ation of design decisions, tested the system in realistic scenarios and leveraged the expertise of practitioners an those familiar with the application environment. A limitation of this approach is that this evaluation could not be compared with a control group, because a setting with A/B testing would have required a second system that ha not integrated the ethics-by-design approach.

This section presented an example of how the ethics-by-design framework has been applied in the S-HELP pro ject. It serves as an example of the flexibility in instantiating the framework. Instead of following the framework' process sequentially, the actual implementation diverged in certain aspect. Figure 4 illustrates the outcome of th ethics-by-design approach on the S-HELP project

## 5 | CONCLUSIONS

This paper discussed a framework for applying an ethics-by-design approach that has been developed and implemented in the context of a 3-year funded research project on DSS for EM. Systems to manage large-scale cross-border disasters presents profound ethical challenges. The creation of systems to meet such needs requires sensitivity to ethical issues whilst ensuring decision-makers can be empowered to make decisions quickly. Given that EM is a multi-phase longitudinal process, decision support must ensure that good decisions are considered, whilst taking follow-up actions into account. In simple terms, decisions that are enabled by such systems can have profound, and often unintended, societal consequences. It is beholden on the designers of such systems to embed ethi cal principles in the design, and consider the ethical implications surfaced in training and the use of such systems Access, or lack thereof, to digital technologies can contribute to second-order disasters that can further exacerbat the precarity of already disadvantaged citizens (Madianou, 2015). An approach to ISD that incorporates ethics-by design could help mitigate such outcomes.

The holistic framework presented in this paper provides a pragmatic way to address ethical concerns. The framework provides a process, applied in the EM and DSS domain, to operationalise an ethics-by-design approach for arte fact creation. Its application in the S-HELP project demonstrates its usefulness and applicability, while th summative evaluation demonstrates its validity. The key concepts of the framework are built on existing concepts in the field of ethical frameworks and ethical impact assessment.

This paper makes multiple contributions. The articulation of an ethics-by-design approach shifts the IS discourse on design towards a more practical, ethics-based footing. In doing so, it builds on the growing body of literature pertaining to ethics and technology design and use. Second, the ethics-by-design approach can be applied to other contexts. The approach guides the selection of ethical values and demonstrates replicable strategies for evaluatin ethical design that considers the perspective of multiple stakeholders. Such an approach would be particularly pru dent for designers of systems that incorporate algorithms, or artificial intelligence, for decision-making irrespective of application domain. The paper contributes to theory by elaborating on Gotteborn's ethics-by-design approac through its practical application in a large-scale R&D project. Furthermore, the paper contributes to the DSS litera ture through design guidelines for systems design and decision-making training

The framework approach builds on an agile software development process and its key components. While th agile software development process influences the ethics-by-design approach, there is also a reciprocal effect. Incor porating the ethics-by-design approach in the agile software development methodology advances the quality an feature of the agile approach. Since the agile methodology is already widely adopted and used in software develop ment projects, it could serve as a method to make the ethics-by-design approach tangible for many projects dealing with societal aspects. Considering that ethics-by-design has rarely been applied in practice, there is significant scope for impact of our approach.

This paper contributes to literature on ethical frameworks and ethical impact analysis. While existing ethica frameworks focus rather solely on ex-ante, intra, or ex-post methods for ethical impact analysis (Reijers et al., 2018)

our approach includes the whole spectrum of ethical assessments. Ex-ante methods dealing with emerging technologies (“anticipatory ethics of emerging technologies”) focus on the assessment of technology that has not been devel oped so far (cf. Brey, 2012). In our approach, this is performed at the first ethical stage-gate, in order to obtai ethical requirements for the technology to be developed. Intra methods, such as value sensitive design are used to influence the technical design based on human and ethical values. These are applied once, or multiple times, during the research and development process. Ex-post methods dealing with the assessment of existing technology ar applied through the summative ethical evaluation at the last ethical stage-gate. Together with the use of scenario and integration of all relevant stakeholders, these methods constitute a holistic framework

Though the framework incorporates several methods and concepts previously discussed in the ethics literature, it enriches the existing literature with two distinct features. First, it combines these methods into a holis tic framework and applies meaningful sequencing. In this way, the individual methods benefit from each other, which brings additional value to the whole framework. Furthermore, the framework provides structure and guidance on how to apply these methods to achieve an ethics-by-design approach. Such an approach should prove especially useful for designers and developers who are not experienced in applying ethics whilst assuring end-users on the provision of ethical solutions. The second distinct feature is the role of stakeholders in the ethics-by-design approach. Traditional ethical frameworks focus on the ethical use of a technology and how technology can be designed such that it can be used in an ethical way. However, well-designed technology can still be used in a harmful way by untrained users. To mitigate this, our approach demonstrates how stake holders, including technology users, can be included in the ethics-by-design approach. This extended focus rep resents a more complete ethical design.

The outcome of this paper, the framework for creating an ethics-by-design approach and its practical applica tion, have the potential to be used in different contexts and application domains that deserve ethical attention. First future R&D projects in the field of EM and DSS can adopt much of the process described in the framework. Eve the identified ethical values could be reused. However, caution is required as a further refinement or differences in the application domain might lead to slight deviations in the resulting ethical values. Second, R&D projects in othe fields can take up the overall process and adapt it to their needs. Since many of the framework components are wel understood (e.g., agile development process, requirements elicitation, focus groups, evaluations), they can be adapte to meet the project's characteristics, in order to integrate ethics-by-design

Although digital technology has the potential to transform our everyday lives, and society at large, such technol ogy brings ethical issues to the fore. Royakkers et al. (2018), analysed the scientific literature on six dominant technologies: Internet of Things, robotics, biometrics, persuasive technology, virtual & augmented reality, and digita platforms. The analysis revealed many of these technologies were problematic in respect of ethical and societa values. The analysis demonstrates that it is necessary to address such concerns. Since computer models and simula tions are rarely morally neutral, there is an even greater need to collaborate with stakeholders to incorporate ethica considerations “by design” (Bak, 2020). Moreover, due to cognitive limitations of ethical behaviour (Gigerenzer, 2010), humans need to be supported for the ethical use of a technology. Beyond merely promoting awareness for these challenges, technology makers need tools and methodologies to tackle ethical concerns in a practical way without unnecessarily limiting functionality and economic value. The framework presented in this paper provides a means to address this challenge, as it offers a practical and flexible method that can be adapted in different contexts.

However, the sheer variety and reach of emerging technologies also introduces one of the limitations of our approach. In contrast to EM and DSS where a small number of decision-makers can be trained, the users of mass technologies are ordinary consumers that cannot be reached for explicit training. However, there is still the potentia for software to offer user training, which could be elaborated in a careful design. Another limitation concerns the human aspect of decision-making. Decision-making in autonomous systems and robots is often based on artificia intelligence technology. Even though the role of the user controlling these devices is limited, an even greater need for a careful ethics-by-design is necessary. A final limitation lies in the acceptance of applying ethics in the design in general. Commercial producers of technology might be reluctant to address ethics if a reduction in the number of features leads to a potential decrease in economic value.

The findings of this paper can be used by other research-driven software projects, outside of the context of EM to integrate ethical considerations. Though EM has specific ethical requirements that lead to the set of identified ethical values, the same process would lead to other ethical values relevant in other domains and their integration in the technology design. The benefits of exploring analogous settings as a source of inspiration and innovation hav been widely discussed (cf. Franke et al., 2014; Poetz & Prügl, 2010). One could draw comparisons between th extreme needs of EM practitioners and the lead user concept (cf. Von Hippel, 1986). As such, EM represents a fertil research domain both for IS, in general, and the application of novel approaches to ethics research specifically

This project [S-HELP] has received funding from the European Union’s Seventh Framework Programme for research, technological development and demonstration under grant agreement no (607865)

## DATA AVAILABILITY STATEMENT

The data that support the findings of this study are available on request from the corresponding author. The data ar not publicly available due to privacy or ethical restrictions.

## ORCID

Alexander Nussbaumer https://orcid.org/0000-0002-4692-5741

Andrew Pope https://orcid.org/0000-0003-0685-5061

Karen Neville https://orcid.org/0000-0002-8751-6290

## REFERENCES

Agile Alliance. (2001). Manifesto for Agile Software Development. Retrieved from http://www.agilemanifesto.org

Alexander, D. (2000). Scenario methodology for teaching principles of emergency management. Disaster Prevention and Management, 9(2), 89–97.

Alexander, D. E. (2014). Social media in disaster risk reduction and crisis management. Science and Engineering Ethics, 20(3), 717–733.

Allen, D. K., Karanasios, S., & Norman, A. (2014). Information sharing and interoperability: The case of major incident management. European Journal of Information Systems, 23(4), 418–432

Bak Marieke A R (2020). Computing Fairness: Ethics of Modeling and Simulation in Public Health. SIMULATION, 003754972093265.http://dx.doi.org/10.1177/0037549720932656

Becker, H. A. (2001). Social impact assessment. European Journal of Operational Research, 128(2), 311–321. https://doi.org 10.1016/S0377-2217(00)00074-6

Bélanger, F., & Crossler, R. (2011). Privacy in the digital age: A review of information privacy research in information systems. MIS Quarterly, 35(4), 1017–1041. https://doi.org/10.2307/41409971

Beydoun, G., Dascalu, S., Dominey-Howes, D., & Sheehan, A. (2018). Disaster management and information systems: Insights to emerging challenges. Information Systems Frontiers, 20(4), 649–652

Beynon-Davies, P., Tudhope, D., & Mackay, H. (1999). Information systems prototyping in practice. Journal of Information Technology, 14(1), 107–120.

Bharosa, N., Appelman, J. A., Van Zanten, B., & Zuurmond, A. (2009). Identifying and confirming information and system quality requirements for multi-agency disaster management. Paper presented at: ISCRAM 2009: Proceedings of the 6th international conference on information Systems for Crisis Response and Management, Gothenborg, Sweden, 10–1 May 2009. ISCRAM.

Bharosa, N., Lee, J., & Janssen, M. (2010). Challenges and obstacles in sharing and coordinating information during multi agency disaster response: Propositions from field exercises. Information Systems Frontiers, 12(1), 49–65.

Brey, P. A. (2012). Anticipatory ethics for emerging technologies. NanoEthics, 6(1), 1–13.

Camburn, B., Viswanathan, V., Linsey, J., Anderson, D., Jensen, D., Crawford, R., & Wood, K. (2017). Design prototyping methods: State of the art in strategies, techniques, and guidelines. Design Science, 3(13), 1–33.

Carlson, E. J., Poole, M. S., Lambert, N. J., & Lammers, J. C. (2017). A study of organizational reponses to dilemmas in inter organizational emergency management. Communication Research, 44(2), 287–315.

Carver, L., & Turoff, M. (2007). Human-computer interaction: The human and computer as a team in emergency management information systems. Communications of the ACM, 50(3), 33–38

Cavoukian, A. (2009). Privacy by design: The 7 foundational principles. Information and Privacy Commissioner of Ontario Canada. 5.

Cavoukian, A., Taylor, S., & Abrams, M. E. (2010). Privacy by design: Essential for organizational accountability and strong business practices. IDIS, 3, 405–413. https://doi.org/10.1007/s12394-010-0053-z

Chatterjee, S., Sarker, S., & Fuller, M. (2009). Ethical information systems development: A Baumanian postmodernist perspective. Journal of the Association for Information Systems, 10(11), 3

Chen, R., Sharman, R., Chakravarti, N., Rao, H. R., & Upadhyaya, S. J. (2008). Emergency response information system interoperability: Development of chemical incident response data model. Journal of the Association for Information Systems, (3), 200–232.

Childress, J. F., & Gaare Bernheim, R. (2008). Public health ethics. Bundesgesundheitsblatt, Gesundheitsforschung, Gesundheitsschutz, 51(2), 158–163. https://doi.org/10.1007/s00103-008-0444-6

Cockburn, A., & Highsmith, J. (2001). Agile software development, the people factor. Computer, 34(11), 131–133.

Cooper, R. G., & Sommer, A. F. (2016). The agile–stage-gate hybrid model: A promising new approach and a new research opportunity. Journal of Product Innovation Management, 33(5), 513–526.

Cova, T. J. (1999). GIS in emergency management. Geographical Information Systems, 2(12), 845–858.

Cummings, M. L. (2006). Integrating ethics in design through the value-sensitive design approach. Science and Engineering Ethics, 12, 701–715.

Daniels, N. (2000). Accountability for reasonableness: Establishing a fair process for priority setting is easier than agreein on principles. BMJ [British Medical Journal], 321(7272), 1300–1301. https://doi.org/10.1136/bmj.321.7272

Davison, R. M. (2000). Professional ethics in information systems: A personal perspective. Communications of the Associatio for Information Systems, 3(1), 8.

Davison, R. M., Kock, N., Loch, K. D., & Clarke, R. (2001). Research ethics in information systems: Would a code of practic help? Communications of the Association for Information Systems, 7(1), 4.

Dignum, V., Baldoni, M., Baroglio, C., Caon, M., & Chatila, R. (2018). Ethics by Design: Necessity or Curse? Paper presented at: Proceedings of the 2018 AAAI/ACM Conference on AI, Ethics, and Society (AIES'18), 60–66. doi:https://doi.org/10 1145/3278721.3278745

Dorasamy, M., Raman, M., & Kaliannan, M. (2013). Knowledge management systems in support of disasters management: A two decade review. Technological Forecasting and Social Change, 80(9), 1834–1853.

ECDC. (2020). COVID-19 Situation Update Worldwide, as of Week 50 2020. Retrieved from https://www.ecdc.europa.eu en/geographical-distribution-2019-ncov-cases

European Commission. (2013). Ethics for researchers: Facilitating Research Excellence in FP7. Retrieved from http://cordis europa.eu/fp7/ethics\_en.html

Farazmand, A. (2014). Crisis and emergency management. In Crisis and emergency management: Theory and practice, 1. Routledge.

Franke, N., Poetz, M., & Schreier, M. (2014). Integrating problem solvers from analogous markets in new product ideation Management Science, 60(4), 1063–1081 Retrieved December 21, 2020 from http://www.jstor.org/stable/42919585

Friedman, B., Kahn, P. H., & Borning, A. (2008). Value sensitive design and information systems. In K. E. Himma & H. T. Tavani (Eds.), The handbook of information and computer ethics (pp. 69–101). John Wiley & Sons

Friedman, B., Kahn, P. H., Borning, A., & Huldtgren, A. (2013). Value sensitive design and information systems. In N. Doorn D. Schuurbiers. I. van de Poel. & M. Gorman (Eds.). Early engagement and new technologies: Opening up the laboratory. Phi losophy of engineering and technology (Vol. 16). Springer. https://doi.org/10.1007/978-94-007-7844-3\_4

Geale, S. K. (2012). The ethics of disaster management. Disaster Prevention and Management, 22(4), 445–462

Gigerenzer, G. (2010). Moral satisficing: Rethinking moral behavior as bounded rationality. Topics in Cognitive Science, 2 528-554.https://doi.org/10.1111/i.1756-8765.2010.01094.x

Gotterbarn, D. (1999). How the new software engineering code of ethics affects you. Software, 16(6), 58–64. https://doi org/10.1109/52.805474

Gotterbarn, D., Miller, K., & Rogerson, S. (1997). Software engineering code of ethics. Communications of the ACM, 40(11) 110–118. https://doi.org/10.1145/265684.265699

Haddow, G., Bullock, J., & Coppola, D. P. (2017). Introduction to emergency management (6th ed.). Butterworth-Heinemann.

Hardin, G. (1996). Lifeboat ethics: The case against helping the poor. In W. Aiken & H. LaFollette (Eds.), World hunger and morality. Prentice Hall.

Héder, M. (2017). From NASA to EU: The evolution of the TRL scale in public sector Innovation. The Innovation Journal: The Public Sector Innovation Journal.22(2).1-23

Hevelke, A., & Nida-Rümelin, J. (2015). Responsibility for crashes of autonomous vehicles: An ethical analysis. Science and Engineering Ethics, 21(3), 619–630.

Hu, Q., & Kapucu, N. (2016). Information communication technology utilization for effective emergency management net works. Public Management Review, 18(3), 323–348.

Hunt, M., Tansey, C. M., Anderson, J., Boulanger, R. F., Eckenwiler, L., Pringle, J., & Schwartz, L. (2016). The challenge of timely, responsive and rigorous ethics review of disaster research: Views of research ethics committee members. PLoS One, 11(6), e0157142. https://doi.org/10.1371/journal.pone.0157142

Jobin, A., Ienca, M., & Vayena, E. (2019). The global landscape of AI ethics guidelines. Nature Machine Intelligence, 1(9), 389–399.

Kapucu, N., Arslan, T., & Demiroz, F. (2010). Collaborative emergency management and national emergency management network. Disaster Prevention and Management, 19(4), 452–468.

Koehler, G. A., Kress, G. G., & Miller, R. L. (2014). What disaster response management can learn from chaos theory. In A. Farazmand (Ed.), Crisis and emergency management: Theory and practice (pp. 111–134) Routledge.

Konrad, K., Rip, A., & Greiving, V. S. (2017). Constructive technology assessment – STS for and with technology actors EASST Review, 36(3) Retrieved from https://easst.net/article/constructive-technology-assessment-sts-for-and-with technology-actors/

Landesman, L. Y. (2012). Public health management of disasters: The practice guide. American Public Health Association.

Lanzara, G. F. (1983). Ephemeral organizations in extreme environments: Emergence, strategy, extinction. Journal of Management Studies, 20(1), 71–95.

Laugé, A., Hernantes, J., & Sarriegi, J. M. (2015). Critical infrastructure dependencies: A holistic, dynamic and quantitativ approach. International Journal of Critical Infrastructure Protection, 8, 16–23.

Lee, G., & Xia, W. (2010). Toward agile: An integrated analysis of quantitative and qualitative field data on software develop ment agility. MIS Quarterly, 34(1), 87–114.

Leidner, D. E., Pan, G., & Pan, S. L. (2009). The role of IT in crisis response: Lessons from the SARS and Asian tsunami disas ters. The Journal of Strategic Information Systems, 18(2), 80–99.

Madianou, M. (2015). Digital inequality and second-order disasters: Social media in the typhoon Haiyan recovery. Socia Media Society, 1(2), 1–11 2056305115603386.

Maedche, A., Legner, C., Benlian, A., Berger, B., Gimpel, H., Hess, T., & Söllner, M. (2019). AI-based digital assistants. Busi ness & Information Systems Engineering, 61(4), 535–544

McCormick, S. (2016). New tools for emergency managers: An assessment of obstacles to use and implementation. Disasters, 40(2), 207–225.

McMaster, R., & Baber, C. (2012). Multi-agency operations: Cooperation during flooding. Applied Ergonomics, 43(1), 38–47.

Mingers, J., & Walsham, G. (2010). Toward ethical information systems: The contribution of discourse ethics. MIS Quarterly 34(4), 833–854.

Moor, J. H. (1985). What is computer ethics? Metaphilosophy, 16(4), 266–275. https://doi.org/10.1111/j.1467-9973.1985 tb00173.x

Myers, M. D., & Venable, J. R. (2014). A set of ethical principles for design science research in information systems. Informa tion Management, 51(6), 801–809.

Nerur, S., & Balijepally, V. (2007). Theoretical reflections on agile development methodologies. Communications of the ACM, 50(3), 79–83

Noran, O. (2014). Collaborative disaster management: An interdisciplinary approach. Computers in Industry, 65(6), 1032– 1040.

Neville. K., O'Riordan. S.. Pope. A.. Rauner. M.. Rochford. M.. Madden. M.. Sweeney. J.. Nussbaumer. A.. McCarthy. N. O'Brien, C. (2016). Towards the development of a decision support system for multi-agency decision-making during cross-border emergencies. Journal of Decision Systems, 25(sup1), 381–396.

Oz, E. (1992). Ethical standards for information systems professionals: A case for a unified code. MIS Quarterly, 16(4), 423–433.

Özdamar, L., & Ertem, M. A. (2015). Models, solutions and enabling technologies in humanitarian logistics. European Journal of Operational Research, 244(1), 55–65

Person, D. (2000). DSS in insurance claims departments: Personal injury evaluation systems. International Review of Law Computers & Technology, 14(3), 371–383

Pescaroli, G., & Alexander, D. (2016). Critical infrastructure, panarchies and the vulnerability paths of cascading disasters. Natural Hazards, 82(1), 175–192.

Pescaroli, G., Nones, M., Galbusera, L., & Alexander, D. (2018). Understanding and mitigating cascading crises in the globa interconnected system. International Journal of Disaster Risk Reduction. 30. 159–163. https://doi,org/10.1016/i.jidrr 2018.07.004

Pisano, G. P., Raffaela, S., & Zanini, M. (2020). Lessons from Italy's response to coronavirus, Harvard business review online Retrieved from https://hbr org/2020/03/lessons-from-italys-response-to-coronavirus

Poetz. M. K., & Prügl. R. (2010). Crossing domain-specific boundaries in search of innovation: Exploring the potential of pyramiding. Journal of Product Innovation Management, 27(6), 897–914.

Quarantelli, E. L. (1978). Disasters: Theory and research. Sage Publications.

Quarantelli, E. L. (1988). Disaster crisis management: A summary of research findings. Journal of Management Studies, 25(4), 373–385.

Rafi, M. M., Aziz, T., & Lodi, S. H. (2018). A comparative study of disaster management information systems. Online Informa tion Review, 42(6), 971–988.

Ramesh, B., Cao, L., & Baskerville, R. (2010). Agile requirements engineering practices and challenges: An empirical study Information Systems Journal, 20(5), 449–480.

Ray, P. P., Mukherjee, M., & Shu, L. (2017). Internet of things for disaster management: State-of-the-art and prospects. IEEE Access. 5.18818-18835

Reijers, W., Wright, D., Brey, P., Weber, K., Rodrigues, R., O'Sullivan, D., & Gordijn, B. (2018). Methods for practising ethics in research and innovation: A literature review, critical analysis and recommendations. Science and Engineering Ethics, 24, 1437-1481. https://doi.org/10.1007/s11948-017-9961-8

Reuter, C., Marx, A., & Pipek, V. (2012). Crisis management 2.0: Towards a systematization of social software use in crisis sit uations. International Journal of Information Systems for Crisis Response and Management (IJISCRAM), 4(1), 1–16

Rogerson, S., Weckert, J., & Simpson, C. (2000). An ethical review of information systems development: The Australian com puter society's code of ethics and SSADM. Information Technology & People, 13(2), 121–136.

Royakkers, L., Timmer, J., & Kool, L. (2018). Societal and ethical issues of digitization. Ethics and Information Technology, 20 127–142. https://doi.org/10.1007/s10676-018-9452-x

Salmon, P., Stanton, N., Jenkins, D., & Walker, G. (2011). Coordination during multi-agency emergency response: Issues an solutions. Disaster Prevention and Management, 20(2), 140–158.

Sangiamkul, E., & Van Hillegersberg, J. (2011). Research directions in information systems for humanitarian logistics. Paper presented at: Proceedings of the 8th international ISCRAM conference (pp. 1-10), Lisbon, Portuga

Schaar, P. (2010). Privacy by design. Identity in the Information Society, 3, 267–274. https://doi.org/10.1007/s12394-010- 0055-x

Stahl, B. C., Eden, G., Jirotka, M., & Coeckelbergh, M. (2014). From computer ethics to responsible research and innovation in ICT: The transition of reference discourses informing ethics-related research in information systems. Information Man agement, 51(6), 810–818.

Stahl, B. C., Timmermans, J., & Mittelstadt, B. D. (2016). The ethics of computing: A survey of the computing-oriented litera ture. ACM Computing Surveys (CSUR), 48(4), 1–38

Sutcliffe, A. (2003). Scenario-based requirements engineering. Paper presented at: Proceedings 11th IEEE internationa requirements engineering conference, 2003: IEEE, pp. 320-329.

Tarafdar, M., Gupta, A., & Turel, O. (2015). Special issue on the ‘dark side of information technology use’: An Introductio and a framework for research. Information Systems Journal, 25(3), 161–170.

Tim, Y., Pan, S. L., Ractham, P., & Kaewkitipong, L. (2017). Digitally enabled disaster response: The emergence of socia media as boundary objects in a flooding disaster. Information Systems Journal, 27(2), 197–232

Tremblay, M. C., Hevner, A. R., & Berndt, D. J. (2010). Focus groups for artifact refinement and evaluation in design research. Communications of the AIS, 26(27), 599–618

Turilli, M., & Floridi, L. (2009). The ethics of information transparency. Ethics and Information Technology, 11(2), 105–112

Upshur, R. E. G. (2002). Principles for the justification of public health intervention. Canadian Journal of Public Health, 93(2) 101–103. https://doi.org/10.1007/BF03404547

Van de Walle, B., & Turoff, M. (2008). Decision support for emergency situations. In Handbook on decision support systems 2 (pp. 39–63). Springer.

Van Wynsberghe, A. (2016). Healthcare robots: Ethics, design and implementation. Routledge

Von Hippel, E. (1986). Lead users: A source of novel product concepts. Management Science, 32(7), 791–805.

Wallace, D., Burleson, S., Heimann, M., Crosby, J., Swanson, J., Gibson, C., & Greene, C. (2020). An adapted emergency department triage algorithm for the COVID-19 pandemic. Journal of the American College of Emergency Physicians, 1(6) 1374–1379. https://doi.org/10.1002/emp2.12210

Wallace, W. A., & De Balogh, F. (1985). Decision support systems for disaster management. Public Administration Review, 45, 134–146.

Walsham, G. (1996). Ethical theory, codes of ethics and IS practice. Information Systems Journal, 6(1), 69–81.

Walsham, G. (2012). Are we making a better world with ICTs? Reflections on a future agenda for the IS field. Journal of Information Technology. 27(2). 87–93

Waugh, W. L., Jr., & Streib, G. (2006). Collaboration and leadership for effective emergency management. Public Administra tion Review, 66, 131–140.

Weick, K. E., & Sutcliffe, K. M. (2007). Managing the unexpected: Resilient performance in an age of uncertainty (2nd ed.). John Wiley & Sons.

Widgren, B. R., & Jourak, M. (2011). Medical emergency triage and treatment system (METTS): A new protocol in primary triage and secondary priority decision in emergency medicine. The Journal of Emergency Medicine, 40(6), 623–628

Wright, D. (2011). A framework for the ethical impact assessment of information technology. Ethics and Information Technol ogy, 13, 199–126.

Wright, D., & Friedewald, M. (2013). Integrating privacy and ethical impact assessments. Science and Public Policy, 40, 755– 766. https://doi.org/10.1093/scipol/sct083

Zack, N. (2010). Ethics for disaster. Rowman & Littlefield Publishers.

Zarsky, T. (2016). The trouble with algorithmic decisions: An analytic road map to examine efficiency and fairness in auto mated and opaque decision making. Science, Technology & Human Values, 41(1), 118–132.

Zerger, A., & Wealands, S. (2004). Beyond modelling: Linking models with GIS for flood risk management. Natural Hazards 33(2), 191–208.

Zhou, L., Wu, X., Xu, Z., & Fujita, H. (2018). Emergency decision making for natural disasters: An overview. International Jour nal of Disaster Risk Reduction, 27, 567–576.

## AUTHOR BIOGRAPHIES

Alexander Nussbaumer is a post-doctoral researcher at the Institute of Interactive Systems and Data Science (ISDS) at the Graz University of Technology (TU Graz), Austria. He holds a PhD in computer science from the same university. He has 15 years research experience, starting at the Cognitive Science Section of the Depart ment of Psychology at the University of Graz and then joining the Cognitive and Digital Science (CoDiS) Lab of the ISDS at TU Graz. In the context of these affiliations, he has participated in many international research projects on digital learning, secure society research, decision support, cultural heritage, and smart city research. His research focuses on the intersection between computer science and cognitive psychology, but also includes general topics on human factors and societal aspects related to computer applications.

Andrew Pope is a Senior Lecturer in the Department of Business Information Systems at University College Cork (UCC), Ireland. He has more than 15 years' experience with industry-funded R&D projects in the areas of knowledge management, DSS, IS security, and innovation practice. He is a course Director for the Master of Design and Development of Digital Business program at Cork University Business School and a Director at the Centre for Resilience and Business Continuity (CRBC). He is a member of the EITIC research group which espouses responsible IS research and teaching with the aim of anticipating future negative impacts of IT usage and effecting positive change. His work has been presented at many international conferences and published in peer-reviewed journals including the Journal of Strategic Information Systems.

Dr Karen Neville is a Senior Lecturer in the Department of Business Information Systems (BIS), Cork University Business School (CUBS), at University College Cork (UCC), Ireland. She is the founder and Managing Director of UCC's Centre for Resilience and Business Continuity (CRBC) and has generated over €14 million in income for UCC. Karen is a leading expert in Decision Support Systems (DSS) and approaches for Emergency Management. She has formed and lead international consortiums and is active in Horizon Europe Research, developing Technology Readiness Level (TRL) 8 and 9 solutions which have changed regional and national policies. Karen holds a PhD in Information Systems Security and is a Teaching and Learning Fellow in UCC. She is the Director of the BIS PhD Programme. She has presented at top IS conferences and published in international journals such as Journal of Information Technology (JIT). Her research is focussed on EM, Cybersecurity, Business Continuity and Resilience Solutions, DSS and Decision-making Under Stress Training

How to cite this article: Nussbaumer, A., Pope, A., & Neville, K. (2021). A framework for applying ethics-by-design to decision support systems for emergency management. Information Systems Journal, 1–22. https://doi.org/10.1111/isj.12350
