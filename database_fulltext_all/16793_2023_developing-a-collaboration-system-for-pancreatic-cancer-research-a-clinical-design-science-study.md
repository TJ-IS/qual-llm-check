---
otero_id: 16793
otero_key: "GMCF8AW5"
title: "Developing a collaboration system for pancreatic cancer research: a clinical design science study"
authors: "David Rueckel; Barbara Krumay; Ewald Dannerer"
year: "2023"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2022.2088417"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Developing a collaboration system for pancreatic cancer research: a clinical design science study

David Rueckel, Barbara Krumay & Ewald Dannerer

To cite this article: David Rueckel, Barbara Krumay & Ewald Dannerer (2022): Developing a collaboration system for pancreatic cancer research: a clinical design science study, European Journal of Information Systems, DOI: 10.1080/0960085X.2022.2088417

To link to this article: https://doi.org/10.1080/0960085X.2022.2088417

CO © 2022 The Author(s). Published by Informa UK Limited, trading as Taylor & Francis Group.

![](/api/attachments/GMCF8AW5/fulltext/images/dde6209d7274c622e83833ea00ad1b6a03c2b1a3a88bf0399700371988d4abdc.jpg)

Published online: 16 Jun 2022.

![](/api/attachments/GMCF8AW5/fulltext/images/ec1162e0bc3713b9c379284e288192d5ab7760f26448e5277524525fe57acb0d.jpg)

Submit your article to this journal

![](/api/attachments/GMCF8AW5/fulltext/images/39c0f8f57947b69f40ed8a6dbf74d87a5187c5f98c4c95b9bc89fbf0d61015d8.jpg)

Article views: 467

![](/api/attachments/GMCF8AW5/fulltext/images/a976ff021004b7759ff06c5bc890b2c7d780f810c515318c3eba073d0a60bd58.jpg)

View related articles

![](/api/attachments/GMCF8AW5/fulltext/images/fd3b8038957b54cd0a04023be3ac569bb250855a70326a67e97b3b592bca16f5.jpg)

View Crossmark data

RESEARCH ARTICLE

∂ OPEN ACCESS

Check for updates

# Developing a collaboration system for pancreatic cancer research: a clinical design science study

David Rueckel <sup>a,b</sup>, Barbara Krumay <sup>a</sup> and Ewald Dannerer<sup>c</sup>

<sup>a</sup>Department of Business Informatics– Information Engineering, Johannes Kepler University, Linz, Austria; <sup>b</sup>Department of Compute Science, University of Applied Sciences Technikum Wien, Vienna, Austria; <sup>c</sup>Ordensklinikum Linz GmbH, Linz, Austria

## ABSTRACT

Great potential exists for the use of information systems (IS) in medical research, as they already form the backbone of several long-term medical research projects. IS can potentially support practitioner-researchers (practitioners who conduct research in their areas of practice) by enabling collaboration, particularly when the number of cases is low and the treatment strategy is centralised. However, practitioner-researchers and academic researchers difer in their research approaches. In this clinical IS research efort, we designed an IS, together with a local hospital, for supporting research on pancreatic cancer by applying a design science research (DSR) approach. We also observed how DSR is accepted and used by practitionerresearchers in this context. Consequently, we not only developed an IS but also gained insights into the benefits of DSR in projects with heterogeneous participants, namely those from various fields with diferent experiences and requirements. The results show that DSR contributes to mutual understanding, transparency in the design process and long-term benefits for all parties involved, which was further confirmed by post-hoc interviews.

ARTICLE HISTORY Received 1 March 2021 Accepted 1 June 2022

KEYWORDS Clinical IS research; practitioner-researcher; design science; cancer research; collaboration

## 1. Introduction

Research on and the use of information systems (IS) have become indispensable in healthcare in general and in medical research (i.e., research regarding human health) in particular (Fichman et al., 2011; Romanow et al., 2012). In addition to medical and organisational hospital IS (Kuhn & Giuse, 2001), national and international eHealth platforms (Fan et al., 2018), electronic health records (Austin et al., 2021; Mishra et al., 2012) and medical research projects and initiatives are supported by IS (Giannoulis et al., 2017). As the COVID-19 pandemic has shown, worldwide healthcare collaboration is vital. Although distributed medical research activities are challenged by distance, time constraints and scarce resources, IS have the potential to address these challenges. For example, medical cancer researchers rely on cancer case data (e.g., for diagnosis, treatment, complication rates and mortality). Medical research institutions may provide access to their data, but the IS at hand rarely support distributed, worldwide collaboration, and this support is particularly lacking for rare diseases. Research on rare diseases (i.e., those with low case numbers) depends even more on collaboration among researchers and access to a case base. Furthermore, legal and compliance regulations, such as those around sensitive patient data, may hinder collaboration among the institutions and practitionerresearchers involved. In this clinical IS research project, two types of practitioner-researchers are involved: IS practitioner-researcher and medical practitioner-researchers. It has become necessary for both IS and medical practitioner-researchers to join forces in developing IS that facilitate collaboration.

This study focused on a pancreatic cancer research setting, which is complex and distributed and, therefore, requires collaboration among practitionerresearchers and academic researchers. Practitionerresearchers are “practitioners who are involved in doing research into areas of their practice” (Reed & Procter, 1995, p. 3). The aim of the current clinical IS research project was to develop a prototype of an IS to enable distributed collaboration for documenting the states and course – or aetiopathology – of a rather rare disease considering the special needs of practitionerresearchers. Pancreatic cancer is infrequent (representing 2.5% of all cancers in 2018), often lethal (24% survival rate 1 year after diagnosis) and usually treated in specialised hospitals (Rawla et al., 2019).

Medical practitioner-researchers (10) from a specific hospital (hereafter referred to as the case institution), representatives (2) of the IS department at the case institution (one IS practitioner-researcher, one technician), academic IS researchers (2) and research coordinators (2) from an associated university were involved at diferent levels of this study. The needs of other stakeholders (e.g., administrative staf) were considered when necessary, and software developers were involved in developing the prototype. The remainder of this paper is structured as follows: First, we briefly present the state of the field and how design science research (DSR) was applied in the current project. We subsequently describe the development of the pancreatic cancer IS prototype and its evaluation. Next, we explain how this study contributes to solving a relevant problem (i.e., using an artefact) and how it contributes to the discussion of the role of DSR in knowledge generation. Finally, we conclude the work and present its limitations and possibilities for further research.

## 2. Background information

This background section introduces the concepts of practitioner-researchers in general and clinical IS research in particular.

## 2.1. Practitioner-researchers

Practitioner-researchers are diferentiated from purely academic researchers by their practical experience and expertise in the field in which they conduct research, which is frequently related to their practice (Fraser, 1997; Reed & Procter, 1995). Furthermore, a gap has been noted between academic and practitioner research (Anderson et al., 2001). Research projects involving practitioner-researchers gain complexity via the interplay of high levels of practitioner knowledge (Meerabeau, 1995) and the associated possibility of bias, as practitioner knowledge and identity may afect data collection (Reed, 1995). The risks associated with such project settings are well documented in various disciplines, including IS research, clinical IS research, and medical research (Burton et al., 2020; Heiskanen & Newman, 1997; Mathiassen & Sandberg, 2013). The concepts of practitioner research and action research overlap (Avison et al., 2018; Davison et al., 2004) and, depending on the abstraction level of the scientific discipline, may be used synonymously (e.g., Kemmis, 2009) or hierarchically (e.g., action research as a form of practitioner research). We deliberately avoided focusing this discussion on methodological diferentiation; rather, we examine support for both IS and medical practitioner-researchers performing research in a pancreatic research setting regarding their need to collaborate worldwide. Enabling structured data collection and collaboration using a specialised IS may help to overcome the abovementioned biases and challenges resulting from practitioner-researchers conducting research in their work environments (i.e., pancreatic cancer research). The collaboration of practitioner-researchers is even more crucial in distributed clinical IS research projects across organisational and geographic boundaries, especially when distributed data collection and analysis are inevitable due to low case numbers worldwide, as in pancreatic cancer research (Rawla et al., 2019).

## 2.2. IS for medical research

Considerable academic literature exists on collaboration in medical research using IS, with focuses ranging from the collection of patient data to the development of IS that support medical research. However, research on patient data (Alagiakrishnan et al., 2016) and the anonymised exchange of sensitive information (e.g., diseases, treatments and cures) remains limited. This may be because the leaking of highly sensitive data to the public (e.g., due to unintended sharing or hacking) can lead to severe legal issues for the responsible organisation (Wooten et al., 2012). In this context, we reviewed three streams of the existing literature: IS support of (distributed) research projects in general (Franklin et al., 2011; Zheng et al., 2017); design and use of IS in cancer prevention, early detection or registration (Abuzaghleh et al., 2013; Hart et al., 2012; Kincaid et al., 2003); and IS in cancer collaboration projects (Giannoulis et al., 2017; Quo et al., 2005; Xing et al., 2007). Concerning the use of standard, “of-the-shelf” software products for collaboration, Franklin et al. (2011) evaluated electronic data capture systems by comparing two open-source projects and one commercial product. They found that existing software tools integrated many useful functionalities (e.g., data sharing, content management, team spaces, survey-based data collection, secure data manage ment, diferent data export mechanisms and identity and role management) but lacked either a focus on medical research and, therefore, special medical functionalities or the capability to integrate historical case data. In contrast, the literature has reported cases of successful custom developments of IS (Bjørn et al., 2009; Giannoulis et al., 2017; Xing et al., 2007; Zheng et al., 2017) for comparable purposes. Consequently, we derived insights from those cases; for instance, from a cloud-based mobile IS to document and research alcohol consumption in a distributed manner, as central registration was required to participate in the interest of security and transparency (Zheng et al., 2017). Another collaborative IS was successfully used for knowledge management in cancer research by adding support for learning from certain cases of cancer treatment (Giannoulis et al., 2017). An architecture for cancer collaboration projects was imple mented within one hospital and ofered additional support (e.g., idea exchange and resource management) alongside classical medical cooperation and collaboration functions (Xing et al., 2007). Although the existing literature is promising regarding the sup port of collaborative medical research projects, certain cases lack pragmatic distributed (worldwide) data collection. Specifically, a need exists for practitionerresearcher involvement in the development of user interfaces, consideration of privacy and security issues due to the collection of sensitive data and structured data management in future solutions (Bjørn et al., 2009). As has been widely discussed (Davis, 1989; Johnson et al., 2005; Tang & Patel, 1994), user interface design ‒ its usability in particular ‒ and early user involvement are critical success factors for the acceptance of IS, not only in healthcare but for other applications as well (Abras et al., 2004; Shneiderman et al., 2017; Venkatesh et al., 2011).

## 3. Methodological approach

The research design of this study relies on the DSR approach (Gregor & Hevner, 2013; Hevner et al., 2004; Pefers et al., 2007), which, in the field of IS, generally refers to the work of Hevner et al. (2004), who discussed how IS research based on expert activities “creates and evaluates IT artifacts intended to solve identified organisational problems” (p. 77). According to Hevner et al. (2004), the resulting guideline defines the principles for research-led artefact development (i.e., the artefact should impact business goals as well as people and the social context). Hevner (2007) established three essential cycles of the development process (i.e., design, relevance and rigour), highlighting the iterative nature of DSR. The design cycle central to DSR “iterates between the core activities of building and evaluating the design artefacts and processes of the research” (Hevner, 2007, p. 88). The relevance cycle integrates the environment, ensuring that the designed artefact is useful and will be accepted by future users. In this study, we specifically addressed acceptance of the artefact by directly involving a research group to gain deeper insights and evaluate the artefact. We also focused on the specific environment for which the artefact was built (i.e., pancreatic cancer research involving practitionerresearchers not being software developers), a consideration that has been suggested in particular for designing IS (Bodenbenner et al., 2013). The rigour cycle integrates the knowledge base, allowing researchers to draw from a rich pool of knowledge and apply their skills to artefact development. We used several sources (e.g., literature), rigorously followed methodological rules and documented all steps accordingly. We followed the process model provided by Pefers et al. (2007) as an overarching guideline.

In the first step, “problem identification and motivation” (Pefers et al., 2007), we reviewed the existing literature and assessed the current status of cancer case documentation at the case institution, allowing us to determine the current situation and related problems. We conducted a structured literature review (Webster & Watson, 2002) of studies from the Senior Scholars

Basket of Journals, widely used scientific databases, such as IEEE Explore, ACM Digital Library and Springer and search engines, such as Google Scholar. We were able to identify 57 studies (including 20 from the IS discipline) as the basis for the problem definition step, but also for defining the objectives and developing and designing the artefact. Summarising the literature review, we identified two main starting points for the artefact building process. On one hand literature shows that sharing sensitive patient data is one major issue (Wooten et al., 2012). On the other, needs of stakeholders vary, influencing requirements, interface design and usability eforts (Johnson et al., 2005; Tang & Patel, 1994), making an early involvement of all stakeholders a precondition to acceptance and use of the IS (Abras et al., 2004; Venkatesh et al., 2011).

In addition to insights from the academic literature, we assessed the current status of case documentation in a pancreatic cancer research setting as a basis for problem definition. We observed medical practitioner-researchers in their daily routines and analysed documents provided by the case institution (in particular, anonymised patient records, instructions for treatments, existing policies and guidelines for the documentation of cancer cases). From this, we concluded that the current problem at the case institution related to data collection methods, problems with sensitive data storage and the importing of previously collected data.

Next, we began to “define the objectives for a solution” (Pefers et al., 2007). The documents were analysed in greater detail, relying on wellestablished content analysis procedures (i.e., coding). Two academic IS researchers conducted interviews with both IS and medical practitioner-researchers at the case institution. The IS practitioner-researcher, therefore, had a special role by providing insights into organisational aspects based on his practitioner knowledge and yet focusing on the aim of the research project. The interviews were audiotaped, transcribed and analysed. We identified requirements for specific data (e.g., survival curve, 30 – and 90-day mortality, rate of complications), the distributed research environment, access control, identity management, anonymisation and standardisation of data export (for importing data from existing sources). We compared these requirements to the capabilities of existing software (e.g., Franklin et al., 2011; Zheng et al., 2017), showing that the identified requirements had been insuficiently addressed. We then iteratively conducted two focus groups to identify the core process, the requirements for the user interface and a role concept (e.g., diferentiation between research administrators and researchers) for the artefact. Considering the gathered information, we formulated the following objective of the artefact: to develop a prototype that enables collaboration in the documentation of pancreatic cancer considering the needs of diferent stakeholders (based on a role concept).

In the third step, we applied well-established, standardised modelling approaches to design and develop an artefact that could fulfil the identified needs and requirements. According to Pefers et al. (2007), iterations are a vital characteristic of DSR based on demonstration and evaluation. Thus, we ran three main iterations: user interface design (It1), data model and management design (It2) and prototype development (It3). Within each of these main iterations were feedback loops.

In It1, we designed a draft of the user interface and exposed it to both IS and medical practitionerresearchers individually, aiming at clarifying its “look and feel” and usability. We used their feedback to inform the redesign of the user interface. It1, therefore, included the design of the initial interface, followed by two redesigns based on the feedback.

In It2, we conducted a focus group consisting of the whole research group to identify the data required for the artefact. This step was critical for the project, as it provided important information regarding the data to be stored in the database and led to the final design, featuring a combination of relational and non-relational database management systems. Finally, we added the required functionality (e.g., data import) to the artefact, exposed it to the focus group again and conducted two additional interviews with a medical practitionerresearcher and the IS practitioner-researcher to further improve the artefact before evaluation.

In It3, we implemented the artefact prototype by installing it at the case institution for evaluation. We invited all involved parties to use the prototype as they would in natural situations. We followed the suggestions of Gregor and Hevner (2013) for evaluation, focusing on validity, utility, quality and eficacy. Medical staf (two nurses and two medical technical assistants) who were not part of the research group and two medical practitioner-researchers from the research group gave extensive structured feedback according to the proposed evaluation criteria and centred on the medical core process.

After conducting unstructured unit tests during development, 11 structured test cases were applied by both IS and medical practitioner-researchers. They applied black-box tests (e.g., input–output tests without knowing the programme code) to determine whether the formal software engineering requirements were met. This evaluation prompted minor changes to the final implementation (e.g., the colours of the interface). The artefact appears to be a useful and valid tool for improving research on the disease and represents a considerable improvement in collaboration among cancer researchers. After the project, the case institution hired a professional software development company to implement a full version of the artefact, which was recently launched. See, Figure 1 below for an illustration of the data sources used for the current application of DSR.

In addition to developing the artefact, we observed the DSR process in general to gain insights into the process itself as well as its applicability in this complex research situation, integrating people from various scientific backgrounds. We recorded field notes and conducted short interviews during and after the project with the involved parties. Post-hoc interviews and observations were conducted 6 and 12 months after the implementation of the artefact at the case institution. The field notes and interviews were then discussed among the academic IS researchers involved in the project and were used not only to assess the long-term utility and eficacy of the artefact but also to understand the development process and its applicability for projects involving both IS and medical practitioner-researchers.

## 4. Artefact description

This section presents the artefact and its development at six levels of abstraction: (1) the medical core process (clinical pathway), (2) special requirements resulting from the core process, (3) used case diagram representing the requirements, (4) flowchart visualising the structure and sequence, (5) description of the database model and (6) description of the user interface.

![](/api/attachments/GMCF8AW5/fulltext/images/d54818542171fae80ec56c3cf83db22be02cf38d013790f1c49f32a589b37955.jpg)  
Figure 1. Data sources used for the current application of design science research.

## 4.1. Core process

The core process, or abstract clinical pathway, to be supported by the prototype (Figure 2) begins with the initial diagnosis (pancreatic carcinoma) and progresses to the collection of both basic patient data and comprehensive preoperative data. Once these data are gathered, physicians and surgeons initiate therapy and subsequently collect postoperative data. The patient’s health condition is monitored in periodic follow-up examinations, and in the event of recurring cancer, therapy is adapted (administer therapy) and repeated. The case is closed at the patient’s natural or cancer-caused death (life-long monitoring).

## 4.2. Special requirements

Table 1 shows the requirements determined from experience with the medical core process and common practices in cancer research.

## 4.3. Use case diagram

To support medical practitioner-researchers in documenting, sharing and analysing cancer case data using an IS, administrator and researcher roles were defined. Administrators are responsible for creating (and deleting) research entities (e.g., hospitals) and researchers (e.g., physicians and surgeons involved in pancreatic cancer research) from the data. Administrators associate researchers with research entities and import and export existing case data from external sources (CSVs). Researchers create, look up, edit and close cases. Administrators are usually medical practitionerresearchers (senior or associate) or medical administrative staf (Figure 3).

## 4.4. Structure and sequence (flowchart)

The use case diagram was then transferred into a flowchart diagram (Figure 4). Following a successful login, users in both roles (administrators and researchers) can utilise the following functions: (a) searching and editing existing case data, (b) collecting new case data or using the import/export function and (c) editing researchers and research entities.

## 4.5. Database model

A combined database approach was chosen for the prototype such that case data were stored in a NoSQL database (MongoDB) and all other data were stored in a relational database (MS SQL Server). The aim of this model was twofold: (a) separate identity management from research data management to facilitate its future integration into a broader identity management system and (b) relocate import and export functions to a separate database to facilitate load balancing. Figure 5 shows an excerpt from the entity relationship model of the databases. The relational database houses the case institution, users, roles and patients, and the non-relational part holds all information related to diagnosis and treatment. We refrained from providing a full description of the database here and instead focus on the implementation of the non-relational part. In the prototype, the non-relational part was used to hold only four fields – date of diagnosis (DateFirstDiag), pre-surgery information (PreSurgInfo), pre-surgery pictures (PreSurgPictures) and surgery indications (SurgIndic) – to assess feasibility. For the sake of clarity, the principle of these fields is explained based on PreSurgPictures (pictures captured via X-ray, computer tomography, medical ultrasonics etc.). This field allows for the entry of related pictures, which means there is at least one picture available; however, there is no limit to the number of diferent pictures for each case. Each picture consists of a file in a specific format (digital or analogue) and may also have a textual description (diagnosis). Since this increases the complexity of database relations, a non-relational design was chosen for the cases. Based on these considerations, cases were documented in MongoDB.

## 4.6. User interface

A key factor for the acceptance and usage of IS is the user interface, which influences how it is perceived by diferent user groups (Abras et al., 2004; Johnson et al., 2005; Tang & Patel, 1994). The logical flow of the system is strongly related to the core process as described above, with the addition of a login. Regarding usability, ISO standards and relevant insights from the literature (e.g., Shneiderman et al., 2017) were applied. Given the difering researcher and administrator roles, the user interface has two diferent instantiations. The interface for researchers provides functionality, such as search and the ability to enter new patients/cases. The administrator interface has the additional functionality of adding users and institutions and assigning roles. The logic and process of the user interface are shown in Figures 3 and 4.

## 5. Discussion

With this study, we aimed at developing a prototype of an IS to enable distributed collaboration in documenting the states and aetiopathology of a rather rare disease by considering the unique needs of practitionerresearchers. Based on our definition of practitionerresearchers (Fraser, 1997; Reed & Procter, 1995), we further considered the gap between academic research and practitioner research (Anderson et al., 2001). As DSR provides “both practical relevance (via its

![](/api/attachments/GMCF8AW5/fulltext/images/713be4ee599119df8c767fd4bb932c4da15fced4dc41a23785e37d028d9bc59f.jpg)  
Figure 2. Core process activity diagram.

emphasis on useful artefacts) and scientific rigour (via the formulation of design theories)” as pointed out by Baskerville et al. (2018), our contribution is twofold. First, we developed an IS that enables collaboration among the pancreatic cancer research community. Second, we focused on the role of DSR in developing an artefact with both IS and medical practitionerresearchers and the process of doing so.

Table 1. Special requirements.

<table><tr><td>Requirement</td><td>Description</td></tr><tr><td>Distributed Research Environment</td><td>Case data must be collected on a distributed basis. Therefore, it is crucial to support researchers independently in their use of the IS from their locality. This requirement led to the application of client–server architecture and appropriate web technologies.</td></tr><tr><td>Access Control and Identity Management</td><td>Due to the sensitivity of the collected data and the use of networks to support independent local research, access control is essential. Furthermore, for transparency reasons, the identity of the researcher and research entity must be clarified.</td></tr><tr><td>Anonymisation</td><td>The proposed medical core process results in the collection of both medical research and personal data, which, in the case of European countries, is regulated by the General Data Protection Regulation.</td></tr><tr><td>Standardisation of Comma-Separated Values (CSV) Files(Import/Export)</td><td>Data collection occurred prior to this clinical IS research project, and researchers mainly used spreadsheets to structure the data. Such data can easily be processed (imported or exported) using CSV files. As there is no common or official standard for CSV files, syntax rules must be defined. Data must also be processed using statistical software.</td></tr></table>

The developed artefact is an IS that enables the collaboration of both IS and medical practitionerresearchers who conduct pancreatic cancer research. We directly followed the DSR paradigm, aiming at designing a solution to an existing, relevant problem in a rigorous manner (Gregor & Hevner, 2013; Hevner, 2007). We follow the idea that a novel and useful artefact “contributes to design knowledge” (Baskerville et al., 2018, p. 359). By integrating the needs of various stakeholders from the very beginning, we developed an artefact that considers their varying perspectives and fulfils their requirements. We used DSR as a research paradigm to design the prototype, which was later implemented at the case institution. We evaluated the artefact for validity, utility, quality and eficacy (Gregor & Hevner, 2013) and found that it fulfilled these qualities. From prior research, we know that perceived usefulness and ease of use (Davis, 1989) influence both the attitudes towards usage and the actual use of a system. Other factors, such as performance and efort expectancy, influence behavioural intention, moderated, for example, by experience (Venkatesh et al., 2003). Similarly, user-centred design (Abras et al., 2004) calls for the early and constant involvement of users and for products to be designed according to their needs. The acceptance and further usage of the IS by medical staf largely depend on the appropriate design of the interface to fit users’ needs (Johnson et al., 2005; Venkatesh et al., 2003). DSR was a helpful framework not only for structuring the development process but also for ensuring the full involvement of future users and bridging the gap between their needs and the technical knowledge of IT specialists. Hence, medical research and pancreatic cancer research benefit from the artefact itself and clinical IS research gains insights from the development of artefacts. In the post-hoc interviews, the participants expressed that they had gained a broader acceptance of IS and that they would participate in future clinical IS research projects.

We have further added to the discussion of how DSR contributes to design knowledge (Baskerville et al., 2018; Gregor & Hevner, 2013). In particular, this study advances design knowledge via design principles (Baskerville et al., 2018) – specifically, methodological design principles regarding the involvement of heterogeneous groups (i.e., academic and practitionerresearchers both from the fields of IS and medicine as well as other stakeholders). We conclude that the early involvement of all stakeholders in DSR is beneficial for the artefact no matter the participants’ prior design knowledge (e.g., software development skills).

![](/api/attachments/GMCF8AW5/fulltext/images/338bffd0a3f57d6988ecf4808c3cdcce0cf15c4e5351eb58ad9b3cf00c0e48a6.jpg)  
Figure 3. Use case IS.

![](/api/attachments/GMCF8AW5/fulltext/images/27fdad15d7468d05a32539ac578a29f2e2dd58044256a26fc68a40c29c70ca54.jpg)  
Figure 4. Flowchart.

Moreover, the insights gained in the project show that the involvement of stakeholders requires clear guidance through the design process, which is supported by Pefers et al. (2007). This leads to the high utility and eficacy of the artefact as well as improved design knowledge among all participants. Although stakeholder involvement in the development of IS has been widely discussed (Abras et al., 2004; Davis, 1989; Venkatesh et al., 2011), the heterogeneous groups that comprise these stakeholders have rarely been investigated. To the best of our knowledge, our study is the first to focus on the application of DSR in heterogenous research groups consisting of academic and practitioner-researchers both from the fields of IS and medicine as well as other stakeholders. According to the literature, practitioner-researchers frequently begin their research based on their experience to investigate relevant research objectives (Anderson et al., 2001; Reed & Procter, 1995). This relates directly to the relevance cycle (Hevner, 2007), an integral part of DSR (Reed & Procter, 1995). The DSR process suggested by Pefers et al. (2007) and adopted in this study allowed for the continuous involvement of practitioner-researchers, who consistently contributed to the development of the artefact (Pefers et al., 2007). Furthermore, the six steps of the DSR process of Pefers et al. (2007) helped define small and understandable parts to be achieved within the development process. Medical practitioner-researchers struggle to understand classic software engineering process models, such as the waterfall model or agile development using scrum (see, e.g., Mahalakshmi & Sundararajan, 2013), as they are unfamiliar with software development. By contrast, the artefact design and development process became understandable and transparent due to the defined steps (Pefers et al., 2007). Nevertheless, certain steps in the process posed challenges. In general, the more abstract steps at the beginning required greater involvement and support from the IS researchers. In particular, both IS and medical practitionerresearchers struggled during the problem identification stage (Pefers et al., 2007), which is considered crucial for such projects. They were certain that they knew what the problem was, but they could not easily express or explain it. The same was true for the second step (definition of objectives). Both IS and medical practitioner-researchers and stakeholders were asked to express their demands and wishes in a structured and transparent manner. The outcome of this step demonstrated varying results depending on each individual’s perspective. The definition of the required data fields and the description of processes was a particularly challenging task. In contrast, the design and development stage (Pefers et al., 2007) was rather easy for them to understand but remained unclear to other stakeholders due to a lack of understanding. By adjusting the prototype based on iterations and feedback, transparency and mutual understanding were established. In the evaluation phase, the participants explained that they realised both the benefits of the IS and the importance of a structured approach (i.e., DSR). In the post-hoc interviews 6 and 12 months after the implementation of the IS, the interviewed participants described their experiences with the design process as well as the longterm use of the artefact. Both IS and medical practitioner-researchers noted the value of such a structured design process, as they stated they specifically valued the knowledge that they gained from the project and the IS that was built. They also mentioned that for future research projects in their respective fields, a structured process might contribute to a deeper understanding and more concise results. The participants further expressed their satisfaction with the utility and eficacy of the developed system.

![](/api/attachments/GMCF8AW5/fulltext/images/d90bfd3340f9df80ee92ae763b1b64267c95b39c68ddfff9fc1b1b8a3e6f5482.jpg)  
Figure 5. Entity relationship model (excerpt) including the non-relational part (using unified modelling language notation).

## 6. Conclusion, limitations and future research

In this study, we presented the design and development process of IS that aimed at supporting IS and medical practitioner-researchers in a pancreatic cancer research setting. By applying DSR, the process was made transparent and comprehensible for all stakeholders. Based on our observations of the development process and the DSR process of Pefers et al.

(2007), we concluded that DSR has several benefits for both IS and medical practitioner-researchers. As Baskerville et al. (2018) noted, design principles make key contributions to design knowledge by presenting an opportunity to develop a fully formulated design theory that considers relevant stakeholders. However, this is a single case and, to the best of our knowledge, the first attempt to investigate the benefits of DSR for research projects involving practitioner-researchers. Future research should focus on research projects that may serve as breeding grounds for additional insights into the role of DSR in the support of IS practitioner-researchers not only in clinical IS research but in IS research in general. Especially due to the ongoing digitalisation and transformational phenomena, IS practitioner-researchers will be intensively facing the challenge of dealing with multidisciplinary research settings involving both academic and practitioner-researchers. Thus, academic IS research is called to further investigate the important role of IS practitioner-researchers. Furthermore, future studies should examine how developing a fully formulated design theory can appropriately consider the involvement of both academic researchers and practitioner-researchers.

## Disclosure statement

No potential conflict of interest was reported by the author(s).

## ORCID

David Rueckel http://orcid.org/0000-0001-5672-6466 Barbara Krumay http://orcid.org/0000-0001-5313-3833

## References

Abras, C., Maloney-Krichmar, D., & Preece, J. (2004). Usercentered design. In W. S. Brainbridge (Ed.), Berkshire encyclopedia of human-computer interaction (Vol. 2, pp. 763–768). Sage Publications, Thousand Oaks, CA.

Abuzaghleh, O., Faezipour, M., & Barkana, B. D. (2013). Skinaid: A virtual reality system to aid in the skin cancer prevention and pain treatment. 2013 IEEE Long Island Systems, Applications And Technology conference (LISAT), 1–6. https://doi.org/10.1109/LISAT.2013.6578220

Alagiakrishnan, K., Wilson, P., Sadowski, C. A., Rolfson, D., Ballermann, M., Ausford, A., Vermeer, K., Mohindra, K., Romney, J., & Hayward, R. S. (2016). Physicians’ use of computerized clinical decision supports to improve medication management in the elderly – The seniors medication alert and review technology intervention. Clinical Interventions in Aging, 11(1), 73–81. https://doi.org/10. 2147/CIA.S94126

Anderson, N., Herriot, P., & Hodgkinson, G. P. (2001). The practitioner-researcher divide in industrial, work and organizational (IWO) psychology: Where are we now, and where do we go from here? Journal of Occupational and Organizational Psychology, 74(4), 391–411. https:// doi.org/10.1348/096317901167451

Austin, E. J., LeRouge, C., Lee, J. R., Segal, C., Sangameswaran, S., Heim, J., Lober, W. B., Hartzler, A. L., & Lavallee, D. C. (2021). A learning health systems approach to integrating electronic patientreported outcomes across the health care organization. Learning Health Systems, 5(4), e10263. https://doi.org/10. 1002/lrh2.10263

Avison, D. E., Davison, R. M., & Malaurent, J. (2018). Information systems action research: Debunking myths and overcoming barriers. Information & Management, 55 (2), 177–187. https://doi.org/10.1016/j.im.2017.05.004

Baskerville, R. L., Baiyere, A., Gregor, S., Hevner, A. R., & Rossi, M. (2018). Design science research contributions: Finding a balance between artifact and theory. Journal of the Association for Information Systems, 19(5), 3. https:/ doi.org/10.17705/1jais.00495

Bjørn, P., Burgoyne, S., Crompton, V., MacDonald, T., Pickering, B., & Munro, S. (2009). Boundary factors and contextual contingencies: Configuring electronic templates for healthcare professionals. European Journal of Information Systems, 18(5), 428–441. https://doi.org/10. 1057/ejis.2009.34

Bodenbenner, P., Feuerriegel, S., & Neumann, D. (2013). Design science in practice: Designing an electricity demand response system. In J. Vom Brocke, R. Hekkala, S. Ram, & M. Rossi (Eds.), Design science at the

intersection of physical and virtual design (Vol. 7939, pp. 293–307). Springer. https://doi.org/10.1007/978-3-642- 38827-9\_20

Burton, J., Gruber, T., & Gustafsson, A. (2020). Fostering collaborative research for customer experience Connecting academic and practitioner worlds. Journal of Business Research, 116(August), 351–355. https://doi. org/10.1016/j.jbusres.2020.04.058

Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Quarterly, 13(3), 319. https://doi.org/10.2307/249008

Davison, R. M., Martinsons, M. G., & Kock, N. (2004). Principles of canonical action research. Information Systems Journal, 14(1), 65–86. https://doi.org/10.1111/j. 1365-2575.2004.00162.x

Fan, H., Lederman, R., Rowe, F., & Matook, S. (2018). Online health communities: How do community members build the trust required to adopt information and form close relationships? European Journal of Information Systems, 27(1), 62–89. https://doi.org/10. 1080/0960085X.2017.1390187

Fichman, R. G., Kohli, R., Krishnan, R., Fichman, R. G., Kohli, R., & Krishnan, R. (2011). Editorial Overview — The role of information systems in healthcare: Current research and future trends. Information Systems Research, 22(3), 419–428. https://doi.org/10.1287/isre.1110.0382

Franklin, J. D., Guidry, A., & Brinkley, J. F. (2011). A partnership approach for electronic data capture in small-scale clinical trials. Journal of Biomedical Informatics, 44(1), S103–S108. https://doi.org/10.1016/j. jbi.2011.05.008

Fraser, D. M. (1997). Ethical dilemmas and practical problems for the practitioner researcher. Educational Action Research, 5(1), 161–171. https://doi.org/10.1080/ 09650799700200014

Giannoulis, M., Marakakis, E., & Kondylakis, H. (2017). Developing a collaborative knowledge system for cancer diseases. 2017 IEEE 30th international symposium on Computer-Based Medical Systems (CBMS), 767–768. https://doi.org/10.1109/CBMS.2017.66

Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science research for maximum impact. MIS Quarterly, 37(2), 337–A6. https://doi.org/10.25300/ MISQ/2013/37.2.01

Hart, A. F., Verma, R., Mattmann, C. A., Crichton, D. J., Kelly, S., Kincaid, H., Hughes, S., Ramirez, P., Goodale, C., Anton, K., Colbert, M., Downs, R. R., Patriotis, C., & Srivastava, S. (2012). Developing an open source, reusable platform for distributed collaborative information management in the early detection research network. 2012 IEEE 13th international conference on Information Reuse & Integration (IRI), 263–270. https://doi.org/10.1109/IRI.2012.6303019

Heiskanen, A., & Newman, M. (1997). Bridging the gap between information systems research and practice: The reflective practitioner as a researcher. Scopus.

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. MIS Quarterly, 28(1), 75–105. https://doi.org/10.2307/ 25148625

Hevner, A. R. (2007). The three cycle view of design science. Scandinavian Journal of Information Systems, 19(2), 4. https://aisel.aisnet.org/sjis/vol19/iss2/4

Johnson, C. M., Johnson, T. R., & Zhang, J. (2005). A user-centered framework for redesigning health care interfaces. Journal of Biomedical Informatics, 38(1), 75–87. https://doi.org/10.1016/j.jbi.2004.11.005

Kemmis, S. (2009). Action research as a practice-based practice. Educational Action Research, 17(3), 463–474. https://doi.org/10.1080/09650790903093284

Kincaid, H., Crichton, D., Winget, M., Kelly, S., Johnsey, D., Srivastava, S., & Thornquist, M. (2003). A national virtual specimen database for early cancer detection. 16th IEEE symposium computer-based medical systems, 2003. Proceedings, 117–123. https://doi.org/10.1109/CBMS. 2003.1212776

Kuhn, K. A., & Giuse, D. A. (2001). From hospital information systems to health information systems: Problems, challenges, perspectives. Methods of Information in Medicine, 40(4), 275–287. https://doi.org/10.1055 s-0038-1634170

Mahalakshmi, M., & Sundararajan, M. (2013). Traditional SDLC vs scrum methodology - a comparative study. International Journal of Emerging Technology and Advanced Engineering, 3(6), 192–196. http://citeseerx.ist. psu.edu/viewdoc/download?doi=10.1.1.413.2992&rep= rep1&type=pdf

Mathiassen, L., & Sandberg, A. (2013). How a professionally qualified doctoral student bridged the practice-research gap: A confessional account of collaborative practice research. European Journal of Information Systems, 22 (4), 475–492. Scopus. https://doi.org/10.1057/ejis.2012.35

Meerabeau, L. (1995). The nature of practitioner knowledge. In J. Reed & S. Procter (Eds.), Practitioner research in health care (pp. 32–45). Springer US. https://doi.org/10. 1007/978-1-4899-6627-8\_2

Mishra, A. N., Anderson, C., Angst, C. M., & Agarwal, R. (2012). Electronic health records assimilation and physician identity evolution: An identity theory perspective. Information Systems Research, 23(3–part–1), 738–760. https://doi.org/10.1287/isre.1110.0407

Pefers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. Journal of Management Information Systems, 24(3), 45–77. https:/ doi.org/10.2753/MIS0742-1222240302

Quo, C. F., Wu, B., & Wang, M. D. (2005). Development of a laboratory information system for cancer collaboration projects. 2005 IEEE engineering in medicine and biology 27th annual conference, 2859–2862. https://doi.org/10. 1109/IEMBS.2005.1617070

Rawla, P., Sunkara, T., & Gaduputi, V. (2019). Epidemiology of pancreatic cancer: Global trends, etiology and risk factors. World Journal of Oncology, 10(1), 10–27. https:// doi.org/10.14740/wjon1166

Reed, J. (1995). Practitioner knowledge in practitioner research. In J. Reed & S. Procter (Eds.), Practitioner research in health care (pp. 46–61). Springer US. https:// doi.org/10.1007/978-1-4899-6627-8\_3

Reed, J., & Procter, S. (1995). Practitioner research in context. In J. Reed & S. Procter (Eds.), Practitioner research in health care (pp. 3–31). Springer US. https://doi.org/10. 1007/978-1-4899-6627-8\_1

Romanow, D., Cho, S., & Straub, D. (2012). Editor’s comments: Riding the wave: Past trends and future directions for health IT research. MIS Quarterly, 36(3), iii–x. https:// doi.org/10.2307/41703474

Shneiderman, B., Plaisant, C., Cohen, M., Jacobs, S. M., & Elmqvist, N. (2017). Designing the user interface: Strategies for efective human-computer interaction (6th ed.). Pearson.

Tang, P. C., & Patel, V. L. (1994). Major issues in user interface design for health professional workstations: Summary and recommendations. International Journal of Bio-Medical Computing, 34(1–4), 139–148. https:// doi.org/10.1016/0020-7101(94)90017-5

Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: Toward a unified view. MIS Quarterly, 27(3), 425. https://doi.org/10.2307/30036540

Venkatesh, V., Sykes, T. A., & Zhang, X. (2011). “just what the doctor ordered”: A revised UTAUT for EMR system adoption and use by doctors. 2011 44th Hawaii international conference on system sciences, 1–10. https://doi.org/ 10.1109/HICSS.2011.1

Webster, J., & Watson, R. T. (2002). Analyzing the past to prepare for the future: Writing a literature review. MIS Quarterly, 26(2), xiii–xxiii. https://doi.org/10.2307/ 4132319

Wooten, R., Klink, R., Sinek, F., Bai, Y., & Sharma, M. (2012). Design and implementation of a secure healthcare social cloud system. 2012 12th IEEE/ACM international symposium on Cluster, Cloud and Grid computing (ccgrid 2012), 805–810. https://doi.org/10.1109/CCGrid.2012.131

Xing, J., Li, Z., Chen, L., Ni, J., & Ye, J. (2007). The architecture of hospital information system for cancer collaboration projects. 2007 IEEE/ICME International Conference on Complex Medical Engineering, 1832–1835. https://doi.org/10.1109/ICCME.2007.4382064

Zheng, Z., Bruns, L., Li, J., & Sinnott, R. O. (2017). A mobile application and cloud platform supporting research into alcohol consumption. Proceedings of the 1st international conference on medical and health informatics 2017, 48–55. https://doi.org/10.1145/3107514.3107519
