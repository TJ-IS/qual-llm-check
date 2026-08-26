---
otero_id: 11382
otero_key: "NDBRCD66"
title: "Evaluating the Adoption of Enterprise Application Integration in Health-Care Organizations"
authors: "KHALIL KHOUMBATI; MARINOS THEMISTOCLEOUS; ZAHIR IRANI"
year: "2006"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222220404"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/NDBRCD66/fulltext/images/9fb6a42acaca4cbce38b175cc4775e37d2c52910a5080e7c2720f278033bcc59.jpg)

# Journal of Management Information Systems

Publication details, including instructions for authors and subscription information: http://www.tandfonline.com/loi/mmis20

# Evaluating the Adoption of Enterprise Application Integration in Health-Care Organizations

KHALIL KHOUMBATI <sup>a</sup> , MARINOS THEMISTOCLEOUS <sup>a</sup> & ZAHIR IRANI <sup>a</sup>

a Brunel University Published online: 08 Dec 2014.

To cite this article: KHALIL KHOUMBATI , MARINOS THEMISTOCLEOUS & ZAHIR IRANI (2006) Evaluating the Adoption of Enterprise Application Integration in Health-Care Organizations, Journal of Management Information Systems, 22:4, 69-108

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222220404

## PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the “Content”) contained in the publications on our platform. However, Taylor & Francis, our agents, and our licensors make no representations or warranties whatsoever as to the accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views expressed in this publication are the opinions and views of the authors, and are not the views of or endorsed by Taylor & Francis. The accuracy of the Content should not be relied upon and should be independently verified with primary sources of information. Taylor and Francis shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses, damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden. Terms & Conditions of access and use can be found at http:// www.tandfonline.com/page/terms-and-conditions

# Evaluating the Adoption of Enterprise Application Integration in Health-Care Organizations

KHALIL KHOUMBATI, MARINOS THEMISTOCLEOUS, AND ZAHIR IRANI

KHALIL KHOUMBATI is a Researcher in the Department of Information Systems and Computing at Brunel University. He holds an M.Sc. in Information Technology and a B.S. in Electronics, both from the Institute of Information Technology, University of Sindh. His current research focus is on the adoption of enterprise application integration in health-care organizations. He has published several research papers in internationally refereed journals and international conferences such as the Hawaii International Conference on System Sciences (HICSS), Americas Conference on Information Systems (AMCIS), European Conference on Information System (ECIS), and European and Mediterranean Conference on Information Systems (EMCIS).

MARINOS THEMISTOCLEOUS is a Lecturer in the Department of Information Systems and Computing at Brunel University. He holds a Ph.D. from Brunel University. He also holds an M.Sc. on Information Systems Management and a B.S. in Computer Sciences, both from Athens University of Economics and Business. Dr. Themistocleous has worked as a consultant for the Greek Ministry of Finance (on e-government adoption), Greek Standardization body (EDI expert), Greek Federation of SMEs (e-business expert), ORACLE Greece (ERP systems), and ORACLE UK (on CRM integration in e-government). He has coauthored three textbooks on electronic commerce and distance learning, published more than 20 internationally refereed journal papers, and received citations of excellence. Some of his articles have been published in journals such as the European Journal of Operational Research, Journal of Information and Management, Information Systems Journal, and European Journal of Information Systems. He has also published more than 50 research papers in international conferences. During the past five years, he has co-organized minitracks at conferences such as Hawaii International Conference on System Sciences (HICSS) and Americas Conference on Information Systems (AMCIS). Dr. Themistocleous serves as the Managing Editor for the European Journal of Information Systems. He acts as an international reviewer for research proposals submitted to the European Union.

ZAHIR IRANI is the Head of Information Systems and Computing and a member of Senate at Brunel University. Having worked for several years as a project engineer in the manufacturing sector, Professor Irani retains close links with industry and has served as a nonexecutive director for several years. He consults for the Office of the Deputy Prime Minister (ODPM) in the United Kingdom as well as international organizations such as Hong Kong and Shanghai Banking Corporation (HSBC), Royal

Dutch Shell Petroleum, Defence Evaluation Research Agency (DERA), BMW, and Adidas. Professor Irani leads a multidisciplinary group of international Ph.D. students who research information systems evaluation and application integration. He has been recognized as the Hooker Distinguished Professor at McMaster University (Canada) as well as being a Visiting Professor at the Arab Academy of Science and Technology (Egypt) and at Ahlia University (Bahrain). He is the Editor-in-Chief of the Journal of Enterprise Information Management and European Editor of the Business Process Management Journal. Professor Irani is on the editorial board of several journals, as well as cochair and minitrack chair to international conferences. He has edited special issue journals, and his scholarly work has been published in leading journals, including IEEE Transactions on Engineering Management, Information & Management, Information Systems Journal, Journal of Management Information Systems, and European Journal of Information Systems.

ABSTRACT: The integration of heterogeneous information systems has always been problematic in health-care organizations, as it is associated with the delivery of key services and has high operational costs. Therefore, health-care organizations are looking for new means to increase their functional capabilities and reduce integration cost. In addressing this need, enterprise application integration (EAI) technology has emerged to facilitate systems integration, enhance the quality of services, and reduce integration costs. Despite the application of EAI in other sectors, its adoption in health care is slow. In seeking to build on the limited normative research surrounding EAI, the authors of this paper focus on the evaluation of factors that influence EAI adoption in the health-care sector. In doing so, using fuzzy cognitive mapping as a technique to identify causal interrelationships among the EAI adoption factors. This approach will enhance the quality of the evaluation process and emphasizes the importance of each factor and its interrelationship with other factors. The outcomes shown in this paper will support health-care organizations’ decision makers in exploring the implications surrounding EAI adoption.

KEY WORDS AND PHRASES: enterprise application integration, health-care organization, information system adoption, information system evaluation.

HEALTH-CARE ORGANIZATIONS ARE EXPLOITING the use of information technology (IT) to automate and improve their clinical and business processes [12, 51]. Decisions regarding IT implementations are often made at the departmental level, with each department developing information systems (IS) based on its needs, beliefs, practices, and expertise [12, 24]. As a result, IT infrastructures in health-care organizations often consist of a number of autonomous and heterogeneous systems [7, 48]. The nonintegrated nature of health-care IS is strongly associated with both a reduction in the outcome of care as well as the many medical errors that occur; for instance, (1) hard copy films are constantly lost/unavailable or (2) information needed for diagnosing or prescribing is often missing. These examples delay the decision-making process (with an adverse impact on patient care outcomes) or they may result in a wrong medical decision (medical error). According to the National Patient Safety

Agency (NPSA), there are up to 850,000 medical errors per year in National Health Services (NHS), which result in the loss of 64 patients per day in the United Kingdom (23,360 per annum) [22]. Similarly Kohn [26] reported that 98,000 patients die every year in the United States.

The integration of these systems is therefore among the most urgent priorities for health-care organizations to meet the increasing clinical, organizational, and managerial needs. In attempting to address this, several integration standards, systems, and projects such as Health Level 7 (HL7), Digital Imaging and Communication in Medicine (DICOM), CEN/TC251, Synergy Extranet (SynEx), and Synapses have been developed and used in health-care organizations to support the integration of their systems. Despite the benefits that these approaches have provided, there are still many human, organizational, and technological problems associated with their adoption. Neither HL7 nor DICOM claim to be a panacea in solving all integration problems, with HL7 being suitable for the description of clinical signs and DICOM being applicable for the integration of radiology images [3, 35]. These integration approaches have focused on the technological aspects, solving the connection problems between different devices and the exchange of information between computer applications [3, 36].

To this end, enterprise application integration (EAI) has emerged to overcome integration problems at all levels (e.g., data and process) [33, 34, 38]. EAI aims at integrating individual applications into a seamless whole, enabling business process and data to speak to one another across applications [29, 38, 44, 45]. Furthermore, it incorporates functionality from a diversity of systems and results in the development of flexible and maintainable integrated IT infrastructure [46]. EAI supports the rapid connections and interface of information between intraorganizational and interorganizational applications [1, 9, 20]. Its benefits are very important to health-care organizations, as these are associated with a dramatic reduction of medical errors. It also offers a rapid return on investment (ROI), as it provides a flexible, manageable, and maintainable IT infrastructure that supports a changing business and technical requirement. This, in turn, has led the health-care sector to move toward EAI, which can be used to integrate health-care services, processes, and IT infrastructures in a flexible and maintainable way. Therefore, such solutions will significantly reduce the number of medical errors that occur.

Nonetheless, there remains limited research reported on the evaluation and the adoption of EAI in the health-care sector. There is also much confusion regarding the factors influencing the EAI adoption decision-making process. In exploring this further, the paper focuses on understanding the interrelationships among the key factors that affect the decision-making process for EAI adoption. In particular, the authors have attempted to evaluate EAI adoption factors and their causal interrelationships when set against a backdrop of evaluating EAI in health care. The factors influencing EAI adoption in health-care organizations are identified and then discussed. Thereafter, a case study is presented to extrapolate the factors that influence EAI adoption. Fuzzy cognitive mapping (FCM) is then used to demonstrate the interrelationships that exist among the factors that influence the adoption of EAI in health-care organizations.

## Health Care Information Systems

THIS SECTION PRESENTS AN OVERVIEW of the literature to identify the factors influencing for the adoption of EAI in health-care organizations. The description of these factors is discussed below.

## Factors Influencing the EAI Adoption in

## Health-Care Organizations

Many studies on the adoption of innovations [39] and the adoption of integration technologies [14, 46, 49] indicate that different factors influence the take-up of ITbased innovations. In the area of EAI, Themistocleous [46] developed a framework to explain the factors that influence the adoption of EAI in the context of multinational organizations. In this paper, the authors use Themistocleous’s [46] framework as the basis for this research for the following reasons:

• The health-care sector is one of the few sectors where the adoption rate of IT was very slow compared to other industries due to poor IT budget [11]. Therefore, health-care industry expenditure on IT was about 2 percent of its total budget as compare to 10 percent by other industries [31]. As a result, there is limited research reported on IT-based innovations adoption in the health-care sector.

• As a new emerging technology, EAI has not been widely studied. To the best of the authors’ knowledge, the framework proposed by Themistocleous [46] is the only available source of reference in this area. The framework is based on factors such as benefits, barriers, and costs that affect the decision-making process for EAI adoption. These factors have been empirically tested and validated through various case studies in private organizations as well as in the public sector.

• The literature review in the area of health care indicates limited research on IT adoption and, in particular, on EAI. Based on Rogers’s model [39], the healthcare organizations can be classified as laggards [39] regarding the adoption of EAI (illustrated in Figure 1). Thus, relevant research frameworks, such as that proposed by Themistocleous [46], should be used to study this area.

• The authors reviewed the literature on the adoption of other integration technologies such as electronic data interchange (EDI) and Web services and identified six common factors: (1) benefits, (2) IT infrastructure, (3) costs, (4) external pressures, (5) internal pressures, and (6) IT sophistication. These factors are also reported by Themistocleous [46], which indicates that his framework has taken into consideration the most important factors.

• As a result, Themistocleous’s [46] framework has been considered appropriate to study the adoption of EAI in health-care organizations due to (1) the absence of a health-care–specific framework on EAI adoption and (2) the framework is validated and widely used in other sectors. This gives sufficient justification to the authors to consider the Themistocleous [46] framework as a basis for this research.

![](/api/attachments/NDBRCD66/fulltext/images/23c9462ab24fa14decec9236194e1f74cc703301880a6c6f314aca7636f7edc8.jpg)  
Figure 1. EAI Adopters

Moreover, the authors have done some minor additions to the aforementioned framework since there are literature references reporting factors that are health-care specific. For instance, Kim and Michelman [23] have identified several factors for the development of hospital IS. These factors include (1) the relationships among administrators and physicians, (2) political barriers, and (3) customers/patients satisfaction. In addition, Kimberly and Evanisko [25] reported organizations’ size as an important factor for the adoption of technological and administrative innovations in health-care organizations. The description of all these factors is presented, with Figure 2 illustrating the framework for EAI adoption in health-care organizations.

## Benefits of EAI Adoption

Benefits refer to the level of recognition of the advantages that integration technologies could provide to organizations. Iacovou et al. [14], in their model of EDI adoption, classified perceived benefits into direct and indirect. In the context of EAI adoption in multinational and public organizations, Themistocleous [46] categorized the benefits as: (1) operational, (2) technical, (3) strategic, (4) managerial, and (5) organizational. In the context of health-care organizations, it is not clear whether the same benefits or the same categories of benefits exist. This leads to the need for the identification, classification, and better understanding of EAI benefits. Despite this fact, the EAI benefits should be considered as an important factor that influence the decision-making process for its adoption as the majority of organizations seek to understand and evaluate them in advance.

## Costs of EAI Adoption

Many organizations conduct a cost–benefit analysis before adopting a new technology [40]. Thus, several authors, such as Iacovou et al. [14] and Wu [49], have identified cost as a factor for the adoption of technologies, which facilitates the organization to evaluate these costs prior to adoption. Themistocleous [46] evaluated EAI costs and classified them using the costs classification proposed by Irani et al. [16]. As a result, EAI costs are classified into direct and indirect (e.g., human and organization).

![](/api/attachments/NDBRCD66/fulltext/images/0acd14b23ec6aca1cacf539b430b90fe7c4162a78749b5c559147e370da9b7ad.jpg)  
Figure 2. Framework for the Adoption of EAI Health-Care Organizations

## IT Infrastructure

The nonintegrated nature of IT infrastructure causes numerous problems to organizations. Several authors have reported the IT infrastructure as a factor in their integration technologies adoption models. Grimson et al. [11] reported nonintegrated IT infrastructures in health-care organizations as a key obstacle in providing better healthcare services. Therefore, the nonintegrated IT infrastructure is a factor that affects the introduction of EAI in health-care organizations.

## IT Sophistication

IT sophistication is reported as a factor in integration technologies adoption models such as EDI and EAI. According to Chwelos et al. [5] and Iacovou et al. [14], organizations with sophisticated IT resources will likely be adopters of EDI technology. In the context of EAI adoption, Themistocleous [46] reported IT sophistication to be related to the technical expertise in the organizations. It is associated with the level of understanding in addressing technical problems at an enterprise and cross-enterprise level.

## Internal Pressures

According to Themistocleous [46], organizations turned to EAI adoption for many reasons, including technical, managerial, financial, and strategic. Therefore, these reasons present internal pressures for the adoption of EAI. As a result, Themistocleous [46] considered this as a factor for EAI adoption. Health-care organizations have various motivations, such as the provision of better health-care services, prevention of medical errors, and inclusion of data security and privacy, which motivate the adoption of EAI in health-care organizations.

## External Pressures

Organizations have responded to several external pressures, such as competitors, suppliers, and customers, for the adoption of EAI [46]. Therefore, organizations are looking for new practices to better coordinate cross-enterprise business processes, which translate into a factor that influences the adoption of EAI. In the context of health-care organizations, there are several stakeholders, such as patients, suppliers, and government bodies, collaborating with the organization. Thus, the authors have considered the external pressures as a factor for the adoption of EAI in health-care organizations.

## Barriers of EAI Adoption

The practice has shown that there are many barriers related to the application of EAI, with organizations needing to consider these barriers before proceeding to EAI adoption. Kim and Michelman [23] have also reported several barriers such as political issues and consider it as a factor for the integration of health-care IS. Thus, it is important for health-care organizations to understand these barriers before deciding for the adoption of EAI technology. This can help them to reduce the risks that are associated with its adoption.

## EAI Evaluation Frameworks

There appears to be a market confusion surrounding the adoption of EAI technologies and packages, due to the diversity of EAI products and technologies available. In addressing this issue, Themistocleous [46] developed two different types of frameworks for: (1) integration technologies and (2) integration packages when set against the business objectives. These frameworks highlight possible combinations of integration technologies and packages that can be used to integrate an IT infrastructure. Therefore, these evaluation frameworks facilitate organizations to overcome the confusion regarding the selection of EAI technologies and packages. As a result, these evaluation frameworks are considered as a factor for the adoption of EAI technology.

## IT Support

IT support is related to vendor support, consultant support, and management support. Themistocleous [46] has reported support as a factor for the adoption of new technologies (e.g., EAI). This is for several reasons, such as organizations have limited knowledge of EAI adoption or lack of employees with EAI skill. Therefore, organizations seek outside support from vendors or external consultants to overcome this problem.

## Compatibility

Compatibility has been considered a factor during the technology adoption process. Rogers [39] defines compatibility as the degree to which an innovation is perceived as consistent with the existing values, past experience, and needs of potential adopters. Similar views are shared by other researchers, such as Wu [49], who study the area of integration technologies and Web services. Therefore, the authors considered compatibility as a factor to evaluate EAI adoption in health-care organizations.

## Patient Satisfaction

Patient satisfaction has a significant impact on the performance of health-care organizations. The adoption of IT in health-care organizations is viewed as improving the quality of health-care services and achieving patients satisfaction [53]. However, the nonintegrated IT infrastructure in health-care organizations has caused problems in providing high-quality medical care and achieving higher patient satisfaction [23]. Kim and Michelman [23] reported customer/patient’s satisfaction as a factor for the strategic use of IT in health-care organizations. Furthermore, they reported that the integration of health-care IS can enhance patients’ satisfaction.

## Organization Size

Several characteristics such as the volume of services and the number of employees are being represented to reflect the size of the organization. In the context of hospitals, several other measures are also used to represent the size, such as the number of beds, total assets, and number of personnel. The dominant measure that is being used in hospital research is the number of beds as the operational definition of size that influences the adoption of technological innovations [25]. In addition, Minder [37] has also reported organizational size as an important factor in the context of Web services adoption. Thus, the authors consider organization size as a factor for the adoption of EAI in health care.

## Physician and Administrator Relationship

The integration of IS changes the balance of power among units within the organizations [23]. In the health-care industry, the relationship between administrators and physicians is particularly important because of the autonomous role of physicians. In addressing this, Malvey [35] reported that the development of integrated health-care IS is a problem, particularly due to the conflicts between the clinicians and administrators. Therefore, in many situations, these conflicts have negative effects on the relationships between physicians and administrators, resulting in a political barrier during the integration of health-care IS [23]. Therefore, physicians and administrators relationships represent an important factor during the adoption of integration technologies in health-care organizations.

# ENTERPRISE APPLICATION INTEGRATION IN HEALTH-CARE ORGANIZATIONS

## Telemedicine

Traditionally, telemedicine systems have been designed to improve the care process by allowing physicians to consult a specialist about a case without sending the patient to another location, which may be difficult or time-consuming to reach [4]. However, the existing infrastructure of telemedicine is based on dedicated private networks. These networks cost relatively high amounts to develop and maintain. The developments in the technology such as the wide availability of Internet connectivity, client and server software, and videoconferencing have made low-cost telemedicine applications more feasible [4, 13]. However, the nonintegrated nature of the infrastructure of many health-care organizations does not allow for the widest possible usage and the reaping of the advantages attached to telemedicine.

## Research Methodology

THE SCOPE OF THIS PAPER IS TO INCREASE the understanding of the evaluation of EAI within the health-care industry. Key factors associated with the take-up of EAI have been identified, which, through a robust evaluation approach, will seek to explain why the adoption of EAI in health care has been slow. However, before any propagation is offered through lessons learned, suitable analysis and synthesis must first take place. A number of conditions affecting the research process now need to be addressed, with their justification for inclusion within the proposed research methodology forming the basis of this section.

To describe the core adoption factors associated with EAI in health care, the authors followed the research methodology proposed in Figure 3, which outlines the research design, approaches to data generation, and the way the data are analyzed and synthesized.

The authors evaluated a variety of research strategies as proposed by Yin [52] and, in doing so, allowed the research focus to dictate their choice of a case study. This research strategy was adopted to test and validate the factors proposed in the previous section. Because the authors cannot generalize the data derived from a single case study, they suggest that the research findings will allow others to relate their experiences to those reported herein. This study can act as a frame of reference that will allow others in this and associated areas of research to ground their understanding within the presented context. Hence, this paper offers a broader understanding of the phenomenon of EAI evaluation in health-care organizations.

## Data Collection

The research design has been operationalized into a protocol that served as a mechanism to generate appropriate data [10]. A research protocol is an instrument that acts as an operationalized “action plan” for an empirical inquiry [52]. A case study protocol presents the investigator with a formal document that sets out the proposed rules and procedures to be followed when carrying out fieldwork research. The empirical data presented were collected using the variety of data collection sources such as interviews, observations, and documentation (e.g., project reports and other publications that form part of the case study organization’s history), allowing the researchers to cross-check the veracity of all data generated. To manage the data bias that is considered to be a research challenge when conducting interpretivist research of this nature, three approaches to triangulation were employed: (1) data, (2) methodological, and (3) interdisciplinary triangulation [16, 19, 52].

![](/api/attachments/NDBRCD66/fulltext/images/3f21811086e7f73c0c6baf577100f40e28cc0e262ee020db2f16dd05f1b375b3.jpg)  
Figure 3. Research Methodology

## Interviews

In terms of data collection, interviews were conducted with different people in the hospital—that is, director of IT services, project manager, director of health-care business development, and several other members of the project team and IT department. The interviews lasted from 40 to 60 minutes and were on a one-to-one basis. Taking notes during the interviews merely decreased the interview time and increased the risk of data bias; therefore, the authors considered tape recording as a more effective approach to eliciting the data. Every interview was tape-recorded and later transcribed, so that a full record of the conversation was obtained. Telephone and e-mail were also used to clarify issues.

## Data Analysis: Fuzzy Cognitive Mapping

FCM is a technique that can be used to obtain causal maps that represent individuals’ opinions on the relationships among the factors that influence the adoption of EAI [17]. The analysis of data involves examining the meaning of people’s words as actions. In this research, ATLAS/ti software was used to assist in data analysis and the ATLAS/ti program assists the researcher in completing the coding process visually in an efficient way. There are several modeling techniques such as FCM, systems dynamics modeling, and soft systems methodology that are being widely used in the organizational domain to explore the interrelationship between factors/concepts. Therefore, the authors provide the description of these modeling techniques with their strengths and weakness in Table 1. Based on these descriptions, the authors found FCM especially useful in solving problems where many decision factors are causally interrelated with each other.

To explore the interrelationships and dependence between the various factors associated with EAI adoption, a fuzzy cognitive map, which acts as an extension of a cognitive map, was considered appropriate. Thus, FCM can help decision makers to analyze hidden casual relationships, which might contribute to more relevant and meaningful solutions [27].

FCM-based models are collections of factors that present causal relationships that exist between these factors [50]. The causal relationships between nodes are represented using signs to indicate positive or negative causality. These signs are not numerical operators like addition or subtraction, but, in the concept of modeling, they mean have “greater effect on” and “lesser effect on,” respectively. In addition, Kosko [27] describes causal relationships between the nodes as being fuzzified, and instead of only using signs to indicate positive or negative causality between the factors, a number is associated with the relationship to express the degree of relationship between two factors.

The advantages of using FCM within this study fall into two categories. One is concerned with the technique, which offers structure through symbolic and graphical representation rather than linear layout. The second is concerned with the use of results, which offers an understanding of appraisal decisions, information is obtained clearly communicable, and insight can be gained into the structure of information [18, 27]. The reasons below support the justification to employ FCM to model EAI factors for health-care organizations:

<sub>trengths</sub> <sub>and</sub> <sub>Weaknes</sub>s <sup>of</sup> <sup>the</sup> <sup>Modeling</sup>

<table><tr><td>Modeling techniques</td><td>Strengths</td><td>Weakness</td><td>References</td></tr><tr><td>Fuzzy cognitive mapping (FCM):A fuzzy cognitive map is an extension of a cognitive map. The term fuzzy was introduced by Kosko [27] using a well-established artificial intelligence technique, which incorporates ideas from neural networks and fuzzy logic. FCM is a method to graphically represent state variables within a dynamical system by links that signify cause and effect relationships, being augmented with fuzzy or multivalent weights, quantified via numbers, or words. Visually, FCM is essentially a nonhierarchical diagram from which changes to each statement, hence fuzzy concept (i.e., node), is governed by a series of causal increases or decreases in fuzzy weight values (i.e., links between nodes).Systems dynamic modeling (SDM):Systems dynamic modeling is a technique of studying the structure and behavior of social economic and ecological systems in which the components interact with one another. System dynamics is based on information-feedback theory, which provides symbols for mapping business systems in terms of diagrams and equations, and a programming language for making computer simulation. In its simplest form, system dynamics focuses on the flow of feedback (information that is transmitted and returned) that occurs throughout the parts of a system and the system behaviors that result from those flows.</td><td>Structure thought through symbolic representation.Graphical rather than linear layout.Quick insight into the structure of information.Manage large amount of qualitative informationCapture individual knowledge and experience.Needs less skill and training.Represents the evolving states with time.Graphical representation.Enables various pieces of incomplete information to be put together.Diagram and simulation makes for easy and effective communication with the client and sponsor of work.Has no fixed form to design.</td><td>Exerts undue influence on mapping process.Large maps become complex to administer.Stress and uncomfortable feeling of respondent.Potential convergence to undesired steady states.At the higher level, it is difficult to design.Requires special skills to model.Requires assumption of established problem or issue.Lack of sociopolitical theory.Requires more skills and training.</td><td>[18, 27, 32, 42][2, 8, 21, 28, 30]</td></tr></table>

<table><tr><td>Soft system methodology (SSM):Soft systems methodology was developed through action research, by which ideas are tested in the client organization. It has been used in practice with a wide range of organizations, both public and private. SSM recognizes that many problems in organizations are affected by less tangible factors, including culture, informal interactions, and attitudes. Thus, SSM intends to investigate, understand, and identify a problem. Its investigation may reveal a number of problems to address, rather than presuppose a single root cause of difficulties. It views the problem domain in a holistic rather than a reductionism way, recognizing that the component parts are interconnected, so that a change to one part will affect the other parts.</td><td>Process is iterative.Supports different viewpoints through rich pictures.Takes social, political, and power distribution issues into consideration through the application of cultural stream analysis.Gives better understanding of problem situation.Allows for new and imaginative solutions to be discovered.</td><td>The technique is not appropriate for all situations.SSM is used for soft problems predominantly.SSM is used to solve some ill parts of the system, but it does not build a whole system.Time-consuming process.The power-handling part seems fancy and the managers always have the upper hand.</td><td>[2, 21, 28, 30]</td></tr></table>

• models are easy to build, no expert knowledge in modeling or high-level mathematics is needed,

• models are easy to run and implement,

• easy execution of models,

• all operations are based on matrices multiplications, and

• easy modeling at low cost.

One further justification is the flexibility of FCM to create (through normalizing results) a new FCM that can represent the views of a number of experts in a unified manner [27]. In this way, valuable knowledge can be obtained from the different experts in the domain, which might contribute to more relevant and meaningful solutions for the adoption of EAI in health-care organizations. Thus, the FCM-based model is a powerful representation technique and is more flexible than other modeling techniques. To design the FCM and to assign a value to its nodes, the experts give qualitative estimates of the strengths associated between the factors. These estimates are translated into numeric values in the range of –1 to 1 in increments of 0.25. The experts were asked to assign these numerical values. The outcome of this exercise is a diagrammatic representation that displays causality in the form of a FCM. This graphic display clearly shows the factors’ interrelationships and their degree the influence. Thus, the research findings of this study are derived from empirical data with empirical evidences being used to draw conclusions.

## Empirical Study: Case Evaluation

THE HOSPITAL WHERE THIS STUDY WAS CONDUCTED serves a population of approximately 360,000 persons and is located in northwestern England. The main hospital is located at three sites, including 65 primary health-care services providers. NWE-HOSPITAL has approximately 4,500 staff, with 1,300 beds across the three sites. Annually, NWE-HOSPITAL provides for approximately 90,000 inpatient episodes, 300,000 outpatient episodes, 80,000 accident and emergency (A&E) visits, 3,180 births, 10 million laboratory tests, and 200,000 X-rays. Clearly, this represents significant data to manage the entire process that needs to be integrated.

## Information Technology Context

NWE-HOSPITAL developed its IT strategy in 1988–89, with a pilot site for resource management. During that time, IBM mainframe-based system implementation was providing comprehensive ward ordering and reporting facilities. When originally implemented, the systems were one of the most advanced in the NHS. During 1999, the hospital started working largely on the need to test a wide range of critical-care systems to ensure year 2000 (Y2K) compliance. As a result, NWE-HOSPITAL made a significant investment during that time to address Y2K compliance. The systems that were deployed at the primary and the secondary health-care services providers provide important services and support to health-care professional within their own areas.

## Need for Integration

The NWE-HOSPITAL is the host of legacy IS such as patient administration system, laboratory reporting, pharmacy, radiology, maternity, and pediatric IS. Thus, the existing IT infrastructure of NWE-HOSPITAL, along with the other hospitals and general practitioners (GPs), was heterogeneous and consisted of several incompatible systems that had evolved over time and were based on different technologies. As a result, NWE-HOSPITAL faced significant integration problems while working with other hospital sites, GPs, suppliers, insurance agents, and other government bodies. It proved difficult for NWE-HOSPITAL to adopt “best of breed” integration strategy. In addition, there was a redundancy of data and functionality, as many applications stored similar data or ran systems that overlapped in functionality.

According to the director of IT services, there was an increasing demand for the foundation of a single, shared repository of patients’ data to be accessed and managed by appropriate health-care professionals in the region. The nonavailability of the required data at the appropriate time was causing the occurrence of medical errors. For instance, patients were given inappropriate medication or doctors could not make accurate diagnoses, as important information could not be logged. Moreover, the existing IT infrastructure did not allow clinical staff in hospital environments to view and search electronic patient records, medication profiles, clinical documents, images, and medical alerts and warnings. In addition, there was a need to create orders for tests and investigations, online prescriptions, electronic discharge summaries, and to access online knowledge bases in support of the clinicians daily work practices.

NWE-HOSPITAL was facing the challenge of providing secure, accurate, and upto-date electronic records that would be available and improve clinical governance, in order to promote high-quality care and support in reducing medical errors. In addition, it was observed that NWE-HOSPITAL was facing pressures internally from physicians and externally from the other stakeholders, such as GPs, patients, and government bodies, to improve health-care processes and services.

## Strategy for the Adoption of EAI

The NHS developed an information strategy to ensure that patients and their healthcare providers have all the information necessary to make decisions about their own treatment and care. They established a vision to provide the right information at the right place and time, under the right safeguards and conditions.

NWE-HOSPITAL has made significant steps toward this, according to the director of IT:

If we are to move to more integrated and supportive care services, we need to move to more integrated information services and systems that can truly be considered patient-centered. We stop thinking about systems that occupy specific organisational boundaries and start to think about integrated service for the whole community.

The current strategy across the NHS was largely based on organizations with a consideration of the community as a whole. As a result, the concept of an integrated electronic health record was introduced as a means of sharing a summary of patients records for the benefit of clinicians, partner organizations, and patients. Therefore, in late 2001, NWE-HOSPITAL started to work with a health-care software company on a pilot project to demonstrate the capability of a first-generation integrated electronic health record (EHR) within the council, as represented in Figure 4.

To achieve the underlying vision of an EHR that could provide detailed access to the patients’ records and transcripts, it was also decided to extend the view to the patients’ records beyond hospital-based events. Eventually, the system should provide patients’ records from birth to death within a specific community as a geographical region. The project was focused to deliver the core infrastructure needed for the EHR and includes the following objectives:

• a patient master index facility of an estimated population of 350,000;

• a central database, through which NWE-HOSPITAL can receive and manage patients’ information from multiple sources being fed mainly to the enterprise data repository system;

• an integration tool for managing the interface transactions;

• a Web-based system infrastructure for delivery of applications, data, and processes to end users;

• an integral security and navigation model appropriate for use in an EHR;

• information for patients and coverage of consent issues; and

• enabling the gathering of detailed clinical cancer information that can be viewed through the integration.

To achieve these objectives, an integration group was formed to support the integration requirements for the modern IT infrastructure and to integrate a number of organizational, clinical, and financial processes. The project implementation strategy of the hospital consisted of several phases. The first phase lasted from March 2002 through September 2002.

The objective was to establish a best-practice methodology for integration, which was considered critical for realizing the better utilizations of existing IT investments. During the pilot project implementation, one of the recurring themes was the type of system that is needed to deliver the integration solution. In conjunction with its team of external experts, the team chose an EAI technology for its integration problem.

The project manager of the NWE-HOSPITAL reported that the during the implementation process, health-care process design was considered carefully. As hospital processes are very complex, involving clinical and administrative tasks, large volumes of data, and a large number of people, patients, and personnel.

![](/api/attachments/NDBRCD66/fulltext/images/4f2f49df83da9ee0991b0d1cbe978c52f3c5281630885031801cde9da334346c.jpg)  
Figure 4. EAI Architecture

According to the director of IT services, the integration of telemedicine was an important element in the modernization and restructuring process in the NHS hospitals. To take full advantage of telemedicine applications, they needed to integrate the hospital’s health-care IS. However, to date, telemedicine applications were isolated solutions with very little connection to existing IS. The existing integration approach of NWE-HOSPITAL used the standard HL7 to exchange documents with IS to generate and administer documents. Future telemedicine applications are planned to be integrated at all levels with the health-care IS.

## Empirical Study: Data Analysis and Findings

IT WAS APPARENT FROM THE EMPIRICAL DATA that several factors influenced EAI adoption. The main findings drawn from the evaluation of EAI in the hospital are summarized below.

The existing IT infrastructure of the NWE-HOSPITAL including with 65 primary care providers and a social services department were heterogeneous and consisted of several incompatible systems. Consequently, NWE-HOSPITAL faced significant integration problems while working with other hospitals, primary care providers, and other government bodies. Thus, it was difficult for NWE-HOSPITAL to integrate all the applications that ran on the mainframe and the nonmainframe platforms. In addition, there was a redundancy of data and functionality as many applications stored similar data or ran systems overlapping in their functionality. As a result, the hospital could not take advantage of IT and support closer collaboration with its various stakeholders. Thus, the exiting IT infrastructure represents an influencing factor for the adoption of EAI in NWE-HOSPITAL.

There was marketplace confusion due to a variety of EAI products available in the market. Therefore, NWE-HOSPITAL decided to study the available EAI products in the market. To study these EAI products, the hospital did not go through the development of any specific framework that can support them in assessing the integration technologies. However, the NWE-HOSPITAL IT services department and external consultant formulated several specific criteria that met the requirements of their integration needs. When the interviewees were asked to describe these criteria, they only described main criteria such as security, real-time integration, support health-care process integration, security and confidentiality, customization, and flexibility.

When the NWE-HOSPITAL manager for IT services was asked to comment on the framework proposed by Themistocleous et al. [47] for the evaluation of integration technologies and packages, he was initially surprised to learn of the existence of such a framework for the evaluation of integration technologies and packages. After a thorough discussion, he commented that

the framework covers broad categories of the evaluation criteria and provides support as a decision-making tool for the evaluation of EAI technologies and packages.

According to the external consultant, this framework deals with overcoming the real integration problem, as in the market, there are varieties of integration tools; nevertheless, none of them can solve the entire integration problem. Therefore, this framework provides the facility to overcome the problem of selection and assessment of integration technologies and packages. Furthermore, the interviewees explained that this framework covers the broader categories of the various criteria, and represents a tool while selecting the integration technologies. Therefore, these evaluation frameworks improve the level of IT sophistication. Thus, it appears that the framework proposed by Themistocleous et al. [47] for the evaluation of EAI technologies and packages has a significant role in selecting EAI software. From the empirical evidence, it appears that NWE-HOSPITAL considered the existence of the frameworks for the assessment of EAI technologies and packages as an influencing factor for EAI adoption.

## Benefits of EAI Adoption

The interviewees were asked to identify the benefits of EAI that the hospital has experienced due to the implementation of EAI. They agreed that EAI implementation has provided a significant benefit to the hospital. All these benefits have been classified based on the classification model developed by Shang and Seddon [41] for the adoption of enterprise systems. These benefits are grouped as operational, managerial, strategic, IT infrastructure, and organizational, and are briefly described below.

• The operational dimension includes benefits such as cost savings, efficient standard-based management of essential connections, and systems flexibility. Due to the adoption of EAI, the quality of connections has improved along with systems performance and reliability. Furthermore, interviewees realized that the EAI solution has secured the existing IT investments.

• The managerial dimension is achieved through care process advances from better adherence to clinical protocols and improvements in clinical decision making. Other benefits identified include enabling GPs to receive X-rays and laboratory test results within 24 hours instead of eight days. A&E staff are able to check at the click of a mouse whether a patient, who might be unconscious, is taking prescribed medications or has any allergies. Thus, this enables the staff to handle emergencies more quickly and improve the quality of patient outcomes through real-time alerts and reduction of medical errors.

• The strategic dimension includes improvements in the discharge reporting process, which, in the past, took between six to ten weeks. Now, with availability of all the required information, the reports are issued within three to seven days of patient discharge. The time saving represents approximately tenfold improvement. This has also resulted in better collaboration with stakeholders.

• The organizational dimensions includes patients’ satisfaction with improved access to health-care medical records, a decrease in the appointments waiting time, and an increasing positive perception of improved quality of care. Thus, this has enhanced patient understanding and satisfaction.

• The IT infrastructure dimension includes the reduction of number of interfaces and maintenance time. These findings demonstrate that the use of EAI technologies (such as XML, COM, DCOM, JDBC, and .Net) have reduced the complexity of the interfaces. In addition, the use of EAI has resulted in the integration of the customs, packages, and e-business applications in a more flexible and manageable way.

According to the interviewees, all these benefits were achieved during the first phase of EAI adoption in NWE-HOSPITAL. The benefits further motivated NWE-HOSPI-TAL to continue its EAI implementation strategy for the remaining phases. The findings are in accordance with those of Themistocleous [46], who suggests benefits as a factor for the adoption of EAI.

## Barriers to EAI Adoption

NWE-HOSPITAL experienced several barriers during the adoption of EAI technology. All these barriers are classified based on those developed by Shang and Seddon [41] and are discussed below.

• The operational dimension indicates that the most commonly cited barrier within the case study to the adoption of EAI implementation is the relatively high cost associated with its implementation and training. Because of this, initially, the NWE-HOSPITAL IT department faced problems in justifying the investment.

The managerial dimension represents the fact that the key barriers to adoption of EAI include clinicians’ and GPs’ willingness regarding the adoption of technology. It is not possible to adopt integration technologies without the support of clinicians and especially GPs. According to the interviews, there are several concerns regarding the adoption of the new system, such as improvements in the repeat prescription process leading to a concern about loss of contact with patients. Further concerns came from security and confidentiality concerns about the patients’ clinical and demographic data. As a result, initially, three-quarters of the local GP practices were included in the project. Another barrier experienced by the hospital was reported to be the difficulty in finding the suppliers; this was due to a lack of communication between the NHS and suppliers, and about their plans and capabilities.

• The strategic dimension has been described as a political issue: resistance of change from the clinical staff. The role of the nursing staff toward the adoption of this technology was not positive. There was a resistance to change from the staff. They had several fears, such as thinking that it would be difficult for them to use this technology, which may require a lot of skills and training. Therefore, if they were not able to interact with this technology, they might lose their jobs. As most of the nurses were from other parts of the world, they were already facing technological problems. However, the continuous technology training supports them in overcoming this problem, although this takes more time to motivate and educate them about the benefits of integration technology.

• NWE-HOSPITAL experienced several IT infrastructure barriers such as a lack of skilled technical staff with expertise in integration technology in general, and EAI technology in particular. Thus, they faced a problem selecting particular EAI technologies and packages. Therefore, they employed the services of an external consultant to help them in this process.

The organizational dimension includes, among others things, the lack of understanding of EAI benefits. Moreover, patients feared that their electronic record may be easily accessible by inappropriate parties as compared to paper records. Therefore, to overcome this problem, NWE-HOSPITAL launched an awareness campaign throughout the council; briefing leaflets were distributed to every household, and posters were displayed in libraries, pharmacies, hospitals, clinics, and opticians’ practices. Moreover, interviews about the project on local radio stations and advertisements in the area’s newspapers explained the objectives of the project. The project manager reported that only 13 percent out of 330,000 people refused to opt for the EHR. Furthermore, patients were given the option at what level they wanted to permit the processing of their medical records (under the Public Interest Disclosure Act 1998). Thus, some patients did not prefer online access to their medical records; therefore, almost 10 percent of the patients refused to allow the online access of their records. Hospital management realized that security and confidentiality of patient data are important issues. Thus, apart from the technical measures, they took several other steps as well, including

– access to the system is controlled through a user’s sign-in code and password;

– only those health-care professionals who have a specific role relevant to the type of data being accessed will be able to view the personal data;

– only those clinicians who possess a direct care relationship with the patient will be able to access the patients record;

– patients will be able, in due time, to seal those parts of their records upon which they wish to place special access controls under the Data Protection Act 1998.

– a record will be kept of everyone who accesses a patient’s records, and alerts will be raised if anyone tries to access a record against the rules; and

– all staff work to a code of conduct for handling personal identifiable information and are bound by a common law duty of confidence to ensure patient information is not disclosed inappropriately.

## Costs of EAI Adoption

The costs dimensions reported by Irani and Love [15] are the most common dimensions that are being used for the evaluation of IT adoption costs. Therefore, taking into consideration Irani and Love’s [15] classification, interviewees were initially asked to identify the costs of EAI adoption. They answered that the initial EAI implementation cost was relatively high, but for confidentially reasons, they did not disclose the actual amount. All the interviewees identified software, hardware, communication, and consultancy costs as major direct costs for EAI adoption in healthcare organizations. The most significant indirect costs identified are the education and training costs of the IT staff, clinicians, and GPs. In addition, management time, project team time, and the external consultant incurred significant indirect costs. Invariably, time is spent on the planning and implementation of new systems into current work practices.

## Patient Satisfaction

When the health-care manager of NWE-HOSPITAL was asked to report on improvements in patient satisfaction, he replied that during the adoption of EAI technology, it had been observed that patient’s satisfaction had improved for several reasons. First, the availability of patient information wherever, at any time, has brought improvement in the interaction between the physician and the patients. Thus, significant time is being directed to the patients rather than searching through paper records. Moreover, the trust board receives regular information on complaints from the patients. The hospital has undertaken satisfaction surveys of complainants in order to improve complaint handling. In addition, the perceived competence of the physicians has brought improvement in patient’s satisfaction. Therefore, patient satisfaction represents an important influencing factor for the adoption of EAI.

## Physicians and Administrators Relationship

The relationship between administrators and physicians is being considered as most beneficial in achieving long-term goals and objectives in hospital development. The interviewees shared their views that it is very important that health professionals should have an important role in the development of such projects and that physicians and doctors have ownership of the project from the start. Thus, it appears that the relationship between the administrators and the physicians represents an important factor for the adoption of EAI technology.

## Data Analysis: Applying Fuzzy Cognitive Mapping

THE FCM DATA ANALYSIS WILL DEMONSTRATE the interrelationships of the influencing factors for the adoption of EAI. This will provide a better understanding of these interdependencies and support the investigation of the EAI adoption in health-care organizations. To design the FCM and to assign a value to its nodes, EAI adoption factors were described to the interviewees for a better understanding. The following description was followed to support the robust identification of causal relationships, where all the factors identified from the literature that influence the adoption of EAI in health-care organizations are denoted by F1 to F14, as shown in Table 2. Thereafter, by using the conventions proposed by Kosko [27], the interconnection strength between two factors, such as Fi and Fj, was used for the identification of causal relationships among these factors.

• The total effect is “+” if the causal relationship that exists between one factor and another has a greater effect.

• The total effect is “–” if the causal relationship that exists from one factor to another factor has a lesser effect.

• The total effect is unknown, “0,” if the causal relationship that exists from one factor to another has no effect.

An operational FCM has a numerical value weight associated with each causal link. Therefore, to obtain causal link strength, the interviewees were asked to express the degree of causal influences by using the fuzzy linguistic expressions such as very strong, strong, moderate, weak, and none (see Table 3).

Three stakeholders—project manager, director of IT services, and health-care services manager—were interviewed. Following the above description to identify the causal relationship of the factors, each interviewee was asked to identify the relationship between the influencing factors. The matrices corresponding to the problem domain, with 14 factors, are presented in Tables 4, 5, and 6.

The FCM matrices from the three interviewees were combined, as proposed by Kosko [27]. Where a number of experts are available, a combined FCM connection matrix can be obtained by adding augmented FCM matrices $E _ { 1 } , . . . , E _ { k }$ . Each FCM matrix $E _ { i }$ has n rows and n columns. The combined matrix $E _ { c }$ is obtained by adding elements Eij from the connection matrices obtained from the three interviewees. The combined FCM is finally obtained by normalizing each element by the number of experts (see Equation (1)):

Table 2. Fuzzy Nodes of EAI Adoption Factors

<table><tr><td>Nodes</td><td>EAI adoption factors</td></tr><tr><td>F1</td><td>Benefits</td></tr><tr><td>F2</td><td>Barriers</td></tr><tr><td>F3</td><td>Costs</td></tr><tr><td>F4</td><td>Compatibility</td></tr><tr><td>F5</td><td>Internal pressures</td></tr><tr><td>F6</td><td>External pressures</td></tr><tr><td>F7</td><td>IT infrastructure</td></tr><tr><td>F8</td><td>IT support</td></tr><tr><td>F9</td><td>IT sophistication</td></tr><tr><td>F10</td><td>Evaluation framework</td></tr><tr><td>F11</td><td>Telemedicine</td></tr><tr><td>F12</td><td>Organization size</td></tr><tr><td>F13</td><td>Patient satisfaction</td></tr><tr><td>F14</td><td>Physician and administrator relationships</td></tr></table>

Table 3. Fuzzy Causal Weight

<table><tr><td>Causal weight</td><td>Weight</td></tr><tr><td>Very strong</td><td>1.000</td></tr><tr><td>Strong</td><td>0.750</td></tr><tr><td>Moderate</td><td>0.500</td></tr><tr><td>Weak</td><td>0.250</td></tr><tr><td>None</td><td>0.000</td></tr></table>

$$
E _ {c} = 1 / k \sum_ {i = 1} ^ {K} E _ {i},\tag{1}
$$

where $E _ { c }$ is the combined FCM connection matrix, k represents number of the interviewees, and $E _ { i }$ stands for the elements of the matrices. The combined connection matrices are represented in Table 7, and Figure 5 shows the FCM.

The combined FCM, as presented in Figure 5, shows that there is a higher level of interaction between the factors that are obtained from the individual interviewees. It appears that the factor benefits bears a strong interrelationship with EAI evaluation frameworks. This relationship shows that the EAI evaluation frameworks provide the benefit to overcome marketplace confusion regarding the selection of a particular EAI technology. The benefits show a moderate interrelationship with costs and IT infrastructure. On the other hand, internal pressures, patient satisfaction, and telemedicine represent a weak interrelationship with benefits. The findings suggest that the existing IT infrastructure of NWE-HOSPITAL was not integrated, creating the problems faced by this hospital. However, the adoption of EAI provided the support to overcome these problems and, thus, resulted in an increase in patient satisfaction. The interrelationship of benefits with internal pressures shows that there were pressures from the physicians regarding the availability of patients’ information at the right place and right time. EAI adoption has overcome this problem.

<sub>merical</sub> <sub>Fuzzy</sub> W<sup>eight</sup> <sup>of</sup> <sup>Factors</sup> <sup>by</sup> <sup>Director</sup> <sup>of</sup>

<table><tr><td>Factors</td><td>F1</td><td>F2</td><td>F3</td><td>F4</td><td>F5</td><td>F6</td><td>F7</td><td>F8</td><td>F9</td><td>F10</td><td>F11</td><td>F12</td><td>F13</td><td>F14</td></tr><tr><td>F1</td><td>0.000</td><td>0.000</td><td>0.500</td><td>-0.250</td><td>0.500</td><td>0.250</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.750</td><td>0.500</td><td>-0.250</td><td>0.500</td><td>0.000</td></tr><tr><td>F2</td><td>0.000</td><td>0.000</td><td>0.250</td><td>0.000</td><td>0.500</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.500</td></tr><tr><td>F3</td><td>0.750</td><td>0.750</td><td>0.000</td><td>0.000</td><td>0.500</td><td>0.000</td><td>0.750</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F4</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F5</td><td>0.000</td><td>0.000</td><td>-0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F6</td><td>0.000</td><td>0.000</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F7</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.500</td><td>0.250</td><td>-0.250</td><td>0.000</td><td>0.000</td><td>0.500</td><td>0.750</td><td>0.000</td><td>0.250</td><td>0.000</td><td>0.000</td></tr><tr><td>F8</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.250</td><td>0.000</td><td>0.500</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F9</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.250</td><td>0.500</td><td>0.000</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F10</td><td>0.750</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>1.000</td><td>1.000</td><td>1.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F11</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.500</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.250</td><td>0.000</td></tr><tr><td>F12</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F13</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F14</td><td>-0.500</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr></table>

<sub>merical</sub> <sub>Fuzzy</sub> W<sup>eight</sup> <sup>of</sup> <sup>the</sup> <sup>Factors</sup> <sup>by</sup> <sup>Projec</sup>

<table><tr><td>Factors</td><td>F1</td><td>F2</td><td>F3</td><td>F4</td><td>F5</td><td>F6</td><td>F7</td><td>F8</td><td>F9</td><td>F10</td><td>F11</td><td>F12</td><td>F13</td><td>F14</td></tr><tr><td>F1</td><td>0.000</td><td>0.000</td><td>0.750</td><td>0.250</td><td>0.500</td><td>0.250</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.750</td><td>0.500</td><td>0.000</td><td>0.500</td><td>0.250</td></tr><tr><td>F2</td><td>0.000</td><td>0.000</td><td>0.500</td><td>0.000</td><td>0.250</td><td>-0.500</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.500</td></tr><tr><td>F3</td><td>0.750</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.250</td><td>0.000</td><td>0.250</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F4</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F5</td><td>0.000</td><td>0.000</td><td>-0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F6</td><td>0.000</td><td>0.000</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F7</td><td>0.250</td><td>0.000</td><td>0.250</td><td>0.500</td><td>0.500</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.500</td><td>0.500</td><td>0.000</td><td>0.250</td><td>0.000</td><td>0.000</td></tr><tr><td>F8</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.500</td><td>0.000</td><td>0.500</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F9</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.500</td><td>0.500</td><td>0.000</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F10</td><td>0.750</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.750</td><td>0.750</td><td>0.750</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F11</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.250</td><td>0.000</td></tr><tr><td>F12</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F13</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F14</td><td>0.250</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td colspan="15">Table 6. Numerical Fuzzy Weight of Factors by Health-Care Services Manager</td></tr><tr><td>Factors</td><td>F1</td><td>F2</td><td>F3</td><td>F4</td><td>F5</td><td>F6</td><td>F7</td><td>F8</td><td>F9</td><td>F10</td><td>F11</td><td>F12</td><td>F13</td><td>F14</td></tr><tr><td>F1</td><td>0.000</td><td>0.000</td><td>1.000</td><td>-0.500</td><td>0.250</td><td>0.250</td><td>0.250</td><td>0.000</td><td>0.000</td><td>1.000</td><td>0.500</td><td>-0.250</td><td>0.250</td><td>0.250</td></tr><tr><td>F2</td><td>0.000</td><td>0.000</td><td>0.500</td><td>0.000</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.250</td></tr><tr><td>F3</td><td>0.250</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.250</td><td>0.000</td><td>0.500</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F4</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F5</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F6</td><td>0.000</td><td>0.000</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F7</td><td>0.750</td><td>0.000</td><td>0.500</td><td>0.500</td><td>0.000</td><td>-0.500</td><td>0.000</td><td>0.000</td><td>0.500</td><td>0.500</td><td>0.000</td><td>0.000</td><td>-0.500</td><td>0.000</td></tr><tr><td>F8</td><td>-0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.500</td><td>0.000</td><td>0.250</td><td>0.750</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F9</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.750</td><td>0.250</td><td>0.000</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F10</td><td>0.500</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.500</td><td>0.500</td><td>0.750</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F11</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F12</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F13</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F14</td><td>0.000</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr></table>

<sub>mbined</sub> <sub>and</sub> <sub>Normalized</sub> <sub>Fuzzy</sub> W<sup>eight</sup> <sup>of</sup> <sup>E</sup>

<table><tr><td>Factors</td><td>F1</td><td>F2</td><td>F3</td><td>F4</td><td>F5</td><td>F6</td><td>F7</td><td>F8</td><td>F9</td><td>F10</td><td>F11</td><td>F12</td><td>F13</td><td>F14</td></tr><tr><td>F1</td><td>0.000</td><td>0.000</td><td>0.750</td><td>-0.250</td><td>0.500</td><td>0.250</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.750</td><td>0.500</td><td>-0.250</td><td>0.500</td><td>0.250</td></tr><tr><td>F2</td><td>0.000</td><td>0.000</td><td>0.500</td><td>0.000</td><td>0.250</td><td>-0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.500</td></tr><tr><td>F3</td><td>0.500</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.250</td><td>0.000</td><td>0.500</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F4</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F5</td><td>0.000</td><td>0.000</td><td>-0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F6</td><td>0.000</td><td>0.000</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F7</td><td>0.500</td><td>0.000</td><td>0.250</td><td>0.500</td><td>0.250</td><td>0.250</td><td>0.000</td><td>0.500</td><td>0.500</td><td>0.500</td><td>0.000</td><td>0.250</td><td>-0.250</td><td>0.000</td></tr><tr><td>F8</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.250</td><td>0.000</td><td>0.500</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F9</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.500</td><td>0.500</td><td>0.000</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F10</td><td>0.750</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.750</td><td>0.750</td><td>0.750</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F11</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.250</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.250</td><td>0.000</td></tr><tr><td>F12</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F13</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.500</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>F14</td><td>-0.250</td><td>0.250</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr></table>

![](/api/attachments/NDBRCD66/fulltext/images/525c4d843e530d8fd120ba7e1519ec6ca871fcb21337d6166d28471baf3f4afd.jpg)  
Figure 5. The Combined FCM

Barriers show a moderate relationship with costs, a weak relationship with evaluation frameworks, and physician and administrator relationships. These relationships are in line with the findings of previous literature that suggests EAI technology represents an important barrier due to the variety of EAI technologies in the market; thus, organizations spent a lot of resources and time to evaluate EAI technologies [47].

Costs, as shown in Figure 5, appear to have a strong interrelationship with benefits. This is a result of NWE-HOSPITAL conducting a cost–benefit analysis before the adoption of EAI technology. Therefore, the analysis of the expected benefits supported the investment of such an amount. However, a moderate relationship of costs is also represented in Figure 5 with barriers and IT infrastructure, and a weak relationship with external pressures.

The factor compatibility shows a moderate relationship with IT infrastructure. This is due to NWE-HOSPITAL finding that EAI is consistent with their past values and practices, as the hospital clinical staff had been using IT in their work at different levels.

The combined map in Figure 5 depicts that internal pressures has moderate relationships with benefits and IT infrastructure. It appears that the internal pressure from the various stakeholders of NWE-HOSPITAL was one of the factors that initiated the adoption of EAI in the hospital. Most of the pressures were for the better utilization of the existing IT infrastructure and getting the maximum benefits of IT for the provision of better health-care services. Internal pressures also has a weak interrelationship with barriers, costs, IT infrastructure, and telemedicine.

External pressures has a moderate interrelationship with factors such as telemedicine and weak relationships with benefits, costs, and IT infrastructure. The moderate interrelationship of external pressures with telemedicine demonstrates that the integration of telemedicine applications with the rest of the hospital’s departments was one of the motivations that initiated the adoption of EAI in NWE-HOSPITAL. Moreover, the external pressures from the patients and government organizations regarding the provision of better health-care facilities initiated the adoption of EAI in NEW-HOSPITAL.

Based on Figure 5, it appears that the factor IT infrastructure has a strong interrelationship with evaluation frameworks, a moderate interrelationship with benefits, costs, and IT sophistication, and a weak interrelationship with IT support. The strong relationship of IT infrastructure with evaluation framework shows that there is no single product that covers all integration requirements for its IT infrastructure. Thus, it is difficult to decide which EAI product is suitable for the proposed IT infrastructure. Therefore, there is a need for a tool that can support organizations to select a particular technology based on the requirements of their IT infrastructure.

IT support has a strong interrelationship with the evaluation frameworks, a moderate relationship with IT infrastructure, and a weak relationship with benefits, barriers, and costs. The strong relationship with evaluation frameworks shows that NEW-HOS-PITAL lacked the EAI experts that could access and select the particular EAI technology and packages. Therefore, the hospital employed the services of external consultants to provide them the support for the selection of a particular EAI solution.

The combined FCM in Figure 5 depicts IT sophistication as having an interrelationship with factors such as IT infrastructure, IT support, and EAI evaluation frameworks. The strong interrelationship of IT sophistication with evaluation frameworks shows that NWE-HOSPITAL lacked the required level of knowledge of EAI skills to decide on a particular technology. Therefore, the interviewees believe that EAI evaluation frameworks support the overcoming of this problem.

Figure 5 illustrates a strong relationship between evaluation frameworks and benefits. This finding is in accordance with the literature that suggests that EAI evaluation frameworks contribute toward the elimination of the marketplace confusion regarding the selection of a particular package or technology. The evaluation frameworks show a moderate relationship with barriers, IT infrastructure, and IT support, and a weak relationship with IT sophistication.

In Figure 5, telemedicine shows a moderate interrelationship with benefits and patient satisfaction. The finding shows that the integration of telemedicine applications with the rest of the applications of NWE-HOSPITAL will provide increased access to services for remotely located patients. As a result of such facilities, the patient’s satisfaction has increased.

The factor organization size has a weak interrelationship with benefits, costs, and IT infrastructure. From the organization size point of view, NWE-HOSPITAL is split on three sites including 65 primary health-care service providers, has approximately 4,500 staff, and 1,300 beds set across the three sites. All are using different IT hardware and software applications. Thus, the larger organization size combined with a large number of different types of IT applications results in a nonintegrated IT infrastructure. This finding is in accordance with the literature findings that suggest that larger-sized health-care organizations will likely implement IT innovations.

Patients’ satisfaction is represented in the map with a moderate interrelationship with benefits, a less weak interrelationship with IT infrastructure, and a weak interrelationship with telemedicine. It appears that the adoption of EAI at NWE-HOSPITAL results in providing patients with several facilities, such as (1) online appointing booking, (2) selecting a particular GP online, (3) changing the GP online, and (4) viewing the medical record online. Also, it provides many other benefits at the secondary care level, such as (1) the availability of laboratory results at the proper time has supported physicians and (2) reducing medical errors has enhanced patient satisfaction.

The factor physician and administrator relationship shows a moderate interrelationship with barriers and a weaker interrelationship with benefits. The interrelationship with barriers shows that, due to the integration of health-care IS, the political barriers between administrators and physicians is particularly important.

## Research Synthesis

A NUMBER OF FACTORS IDENTIFIED FROM THE LITERATURE were validated in the previous section. These factors are presented in Table 8, where their contribution is identified and confirmed with literature findings.

## IT Infrastructure

Evidences from the empirical data suggest that, for many years, IT implementation decisions in the hospital has gone through several phases and resulted in a nonintegrated IT infrastructure. Consequently, the hospital has faced significant integration problems while working with stakeholders. Nevertheless, the limitations of the existing IT infrastructure motivated the hospital to adopt EAI. These findings are in accordance with the literature, which suggests that the existing IT infrastructure of an organization represents a factor that influences the adoption process [14, 46, 49].

## Benefits of EAI Adoption

The normative literature indicates that benefits is a factor for the adoption of various integration technologies such as EDI, EAI, and Web services [14, 46, 49]. The empirical data from the case hospital validated this as the benefits derived from the pilot project motivated the hospital to expand the scope of EAI implementation.

## External Pressures

Empirical evidence confirms the findings in the literature that external pressures are a factor for the adoption of integration technologies [5, 14, 46]. In particular, the findings show that external pressures from government organizations (NHS) and from partners (e.g., hospitals and GPs) represent an influencing factor for the adoption of EAI in the case hospital. The pressures from citizens, patients, and local health authority members, such as primary care and social services providers, also represent external pressures. All of these external pressures represented a decisive influential factor for EAI adoption.

<sub>nthesis</sub> <sub>of</sub> <sub>EAI</sub> <sub>Adoption</sub> <sub>Factor</sub> <sub>for</sub> <sub>N</sub>W<sup>E-H</sup>

<table><tr><td rowspan="2">Factors</td><td rowspan="2">Conclusions for NWE-HOSPITAL</td><td colspan="3">Integration technologies</td><td colspan="2">Health informatics</td></tr><tr><td>Iacovou et al. [14]</td><td>Themistocleous [46]</td><td>Wu [49]</td><td>Kim and Michelman [23]</td><td>Kimberly and Evanisko [25]</td></tr><tr><td>Benefits</td><td>The hospital achieved several benefits with the availability of the right information at the right time and right place.</td><td>√</td><td>√</td><td>√</td><td></td><td></td></tr><tr><td>Barriers</td><td>The hospital experienced several barriers during the EAI pilot implementation.</td><td></td><td>√</td><td></td><td>√</td><td></td></tr><tr><td>Costs</td><td>Several direct and indirect costs identified with EAI adoption.</td><td>√</td><td>√</td><td>√</td><td></td><td></td></tr><tr><td>Compatibility</td><td>Increased use of IT by clinical staff makes for accepting EAI technology, as the technology is consistent with existing values.</td><td></td><td></td><td>√</td><td></td><td></td></tr><tr><td>Internal pressures</td><td>These pressures were for the better utilization of the existing IT infrastructure for the provision of better health-care services.</td><td></td><td>√</td><td></td><td></td><td></td></tr><tr><td>External pressures</td><td>Pressures from the NHS, patients&#x27; other hospitals, GPs, and social services for better health-care services and close collaboration.</td><td>√</td><td>√</td><td></td><td></td><td></td></tr><tr><td>IT infrastructure</td><td>IT infrastructure was nonintegrated at the primary and secondary service providers. This motivated the case hospital for the adoption of EAI.</td><td>√</td><td>√</td><td>√</td><td></td><td></td></tr></table>

<table><tr><td rowspan="2">Factors</td><td rowspan="2">Conclusions for NWE-HOSPITAL</td><td colspan="3">Integration technologies</td><td colspan="2">Health informatics</td></tr><tr><td>Iacovou et al. [14]</td><td>Themistocleous [46]</td><td>Wu [49]</td><td>Kim and Michelman [23]</td><td>Kimberly and Evanisko [25]</td></tr><tr><td>IT support</td><td>External consultant provided the support for the assessment of EAI tools.</td><td></td><td>√</td><td></td><td></td><td></td></tr><tr><td>IT sophistication</td><td>The IT department was lacking the required level of knowledge of EAI skills.</td><td></td><td>√</td><td>√</td><td></td><td></td></tr><tr><td>Evaluation frameworks</td><td>Evaluated integration technologies with the support of external consultant and solution provider vendor.</td><td></td><td>√</td><td></td><td></td><td></td></tr><tr><td>Telemedicine</td><td>Integration of telemedicine was an important element in the modernization process.</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Organization size</td><td>The hospital has greater volume of transactions and is geographically dispersed at three sites, including 65 GPs and other departments.</td><td></td><td></td><td></td><td></td><td>√</td></tr><tr><td>Patient satisfaction</td><td>The perceived competence of the physicians has brought improvement in patients&#x27; satisfaction.</td><td></td><td></td><td></td><td>√</td><td></td></tr><tr><td>Physician and administrator relationships</td><td>Positive role of the physicians played an important role during the adoption.</td><td></td><td></td><td></td><td>√</td><td></td></tr></table>

<sub>le</sub> <sub>8.</sub> C<sup>ontinu</sup>

## Barriers of EAI Adoption

Empirical evidence gathered from the case hospital indicates that the hospital has experienced several barriers during the implementation of EAI. This supports the literature findings, which suggest that the introduction of new technologies often presents several barriers that organization needs to address [5, 6, 46]. The case study data analysis supported this perspective and confirmed that the barriers are among the most significant factors during the EAI implementation process.

## Internal Pressures

From the case study findings, it appears that internal pressures, such as pressure from the physicians, influenced the adoption of EAI in NWE-HOSPITAL. The physicians’ pressure arose from problems in providing better decision making as a result of the nonavailability of required timely clinical information such as laboratory and radiology results. Literature findings also confirm that internal pressures are an influential factor during the adoption of EAI [46].

## Patients’ Satisfaction

The findings from the case study indicate that patient satisfaction is an important influential factor too. The integrated IT infrastructure has resulted in improvements in physician and staff working, such as the availability of the patient’s medical record, pathology results, and radiology results at the click of a mouse aids in reducing medical errors by providing the appropriate medication, which results in better care services. These findings are in accordance with the literature findings, which suggest that IT can help improve the patient satisfaction [53]. The more integrated systems will result higher patients’ satisfaction.

## Evaluation Frameworks

Another interesting finding extrapolated from the case study shows that the evaluation frameworks for the assessment of integration technologies and packages represent an influencing factor for the adoption of EAI. The case study data indicates that the case hospital went through several criteria for the assessment of EAI technologies and packages. Furthermore, with the help of the external consultant, they identified different technologies that support their integration needs. Findings reported in the case of NWE-HOSPITAL agree with the literature that several criteria need to be identified during the selection of EAI technologies, [46].

## Organizational Size

Based on the organizational size characteristics, such as capacity of beds, provision of health-care services, number of primary health-care providers, and number of employees, empirical data collected from the case hospital indicate that NWE-HOSPI-TAL, geographically dispersed over the three different sites, including 65 GPs and a social services department. Therefore, this has validated that the organization size factor in the process of EAI implementation has an important role. This confirms the literature findings that suggest that a larger size of organization structure results in a need for integrating the distributed IT infrastructure [25].

## IT Sophistication

The case study data show that there was a lack of skilled employees to understand integration problems or technologies. As a result, the hospital hired an external consultant to improve the IT sophistication. Thus, IT sophistication comprises an influential factor for the adoption of EAI. These findings confirm the previous literature findings of Chwelos et al. [5], Themistocleous [46], and Wu [49].

## IT Support

In the literature, several authors, such as Themistocleous [46], identified support as a factor during the adoption of various integration technologies such as EAI. The case study data shows that the NWE-HOSPITAL IT department was lacking skilled staff with knowledge of EAI. Thus, NWE-HOSPITAL hired the services of an external consultant to support them in the selection of a particular technology suitable for their integration problem. Therefore, these findings confirm the literature findings of Themistocleous [46], which suggest that during the EAI adoption process, organizations get outside support such as consultant and vendor support for the selection of the right integration solutions suitable for their integration problem.

## Costs of EAI Adoption

In agreement with the literature, costs appear to be a significant factor that influences the decision-making process for the adoption of EAI technology [31]. In addition, the hospital has followed the costs taxonomy proposed by Irani and Love [15] to classify the costs into direct, indirect human, and indirect organizational.

## Telemedicine

From the findings, it appears that the integration of telemedicine applications with other clinical IS represents an important factor during the adoption process of EAI.

Therefore, this has validated including telemedicine as a factor in the process of EAI implementation in health-care organizations.

## Administrators and Physicians Relationships

The data show that the relationship between the administrators and the physicians has an important role. During the EAI implementation process, the physicians were actively consulted in the systems evaluation and selection process. These findings are correlated with Kim and Michelman’s [23] findings suggesting that during the integration process, the role of the physicians is very important. Thus, it is suggested that physicians should be involved during the integration process.

## Key Empirical Findings

THE ANALYSIS OF THE EMPIRICAL DATA DERIVED from the case hospital revealed many lessons that will be helpful to health-care organizations seeking to adopt EAI. These lessons are summarized below.

The work carried out by the case organization focused on highlighting the importance of an integrated Web-based virtual patient record system. Such an IS provides a complete, real-time dynamic electronic patient record that clinicians can access from anywhere. It utilizes existing infrastructure; therefore, existing operational systems are brought into play rather than having to be replaced. This emphasizes that healthcare organizations do not have to replace their applications with new ones, but, rather, EAI produces an environment to integrate disparate IS—saving money, time, and reducing the risk of failure of new implementations.

Empirical data has suggested that security and confidentiality comprise factors that affect the adoption of EAI. This finding extends the body of knowledge in the area of EAI adoption in health care, as security and confidentiality were not reported as influential factors in the literature. The analysis of the case study shows that security and confidentiality were considered an issue. The reason for this is that patients and GPs have the same degree of concern for security, such as access to patient care information. Patients and clinical professionals were worried that making personal health information more widely available may endanger its confidentiality and increase the organizations exposure to risk. Therefore, interviewees agreed on ways of enforcing security by ensuring rigorous methods of encryption and signature authentication. Thus, apart from technical measures, the security policy needs guidance from a national (federal) perspective. This means that further work should be done in this area as these two issues are critical for the success of the integrated IS. Therefore, security and confidentiality are shown to be important factors for consideration during the EAI adoption process.

Analysis of the empirical data indicated that the case hospital identified the need of education of their staff and patients during the EAI implementation process. NWE-HOSPITAL launched an awareness campaign to increase exposure to the EAI adoption process; briefing leaflets were distributed to every household and posters were displayed in libraries, pharmacies, hospitals, clinics, and opticians’ practices. Moreover, interviews about the project on local radio stations and advertisements in the area’s newspapers explained the project objectives. These efforts made it possible for the hospital to get the “buy-in” of its employees. Thus, these case findings support education as a factor for the adoption of EAI in health-care organizations.

The external pressures from government, partners, and patients for the provision of better health-care services represent an important driver for the adoption of EAI. It appears that external pressures is a key factor that brings changes in health-care organizations because these organizations traditionally lack resources and expertise, and are usually laggards in the IT innovation adoptions.

Another important finding from the case study is that there was generally a lack of national guidance to seek the consent of patients, while this proves a major hurdle during the EAI implementation. Therefore, considerable effort was put into publicity campaigns (such as advertisements, leaflets, and posters) to increase public awareness and to ensure that implied consent was informed. Therefore, it is suggested that all stakeholders involved in or affected by the adoption process should be aware of the changes that the system will bring. This usually reduces the resistance to change, which is often a barrier to EAI adoption.

The case organization has traditionally relied on vendor support, which indicates that the level of IT sophistication was low. This is a high-risk strategy, and, as reported in the literature, it should be avoided. To address this issue, the organizations should consider employing practitioners with EAI skills or at least train their IT staff before they start the project.

Marketplace confusion regarding EAI technologies was a problem during the implementation of EAI. Therefore, with the support of vendors and external consultants, the hospitals evaluated their EAI packages and technologies and established which would suit their integration need. The interviewees reported that the use of evaluation frameworks for the assessment of EAI technologies and packages is of high importance. It is for that reason that it is not always appropriate to rely on vendor support because, in many cases, the vendor chooses their own EAI products and not necessarily the best EAI solution available.

The results of the pilot project motivated the hospital to further implement EAI for the remaining phases. This motivation was based on the analysis of EAI adoption benefits, barriers, enhanced patient satisfaction, integration of existing IT infrastructure, and costs. Since most EAI projects require a high level of investment, it is suggested that organizations should run pilot projects before making any decisions on broad EAI implementations [43].

## Conclusions

THIS PAPER HAS EXPLORED EAI ADOPTION within a health-care organization. EAI has emerged to provide significant benefits to organizations in support of their overcoming integration problems, with a particular motivation of reducing the overall integration cost that is achieved through the reduction of integration time and maintenance cost.

Through critically reviewing the normative literature, the authors identified several factors considered during the adoption of EAI. The key factors extrapolated include benefits, barriers, costs, evaluation frameworks, IT infrastructure, IT sophistications, IT support, internal pressures, external pressures, organization size, compatibility, telemedicine, patient satisfaction, and physicians and administrators relationships. These factors can provide others with a detailed understanding of issues that need due consideration and can act as a frame of reference associated with EAI adoption in health-care organizations.

To explore these factors empirically, an interpretive case study research strategy was adopted. The findings from the case study confirmed and validated the proposed factors when grounded within the health-care industry. In doing so, this paper offered an in-depth understanding of the phenomenon surrounding the evaluation of EAI in the context of the health-care sector. It therefore provides improved support to decision makers associated with the evaluation and adoption of EAI in health care.

The application of FCM demonstrates the interrelationship of the influencing factors for the adoption of EAI in the case hospital. This shows how decision maps are constructed and how numeric values are assigned to represent the interrelationship of each factor. The use of an FCM approach has enhanced the quality of the evaluation process, and shows the importance of each factor and its interrelationship with other factors. This has provided insights to a better understanding of interdependencies of the factors that influence EAI adoption. This approach may support the quality of decision making in health-care organizations when considering the adoption of EAI. Further, it can support the researchers to analyze and understand the adoption process of EAI.

## Limitations of the Research Conducted

The most important difficulty the authors faced was the restricted access of information such as the hospital’s documents, which was due to confidentiality issues. In some cases, the interviewees as well were not able to provide the related information. Moreover, despite several attempts, the researcher failed to get appointments with top executives of the hospital and the NHS IT department and, therefore, changed the interviewee level from executive management to middle and lower management. The discussion in the Research Methodology section focused on the use of a qualitative method for collecting the data for this research. The reason for this is that the qualitative method facilitates generalization of soft, rich contextual data, which is associated with human and organizational issues. However, despite the advantages the qualitative research provides, this method does have disadvantages as well, such as being time-consuming, in that the authors spent lot of time in the process of data collection and analysis. The amount of data collected was more contextual, which made the interpretation difficult and hard to achieve without some degree of bias.

The empirical data collected are confined to the limited context of a public-sector organization of the United Kingdom. Moreover, the organizational structure of the health-care organization for provision of health-care services varies from country to country. Therefore, it is difficult to generalize the results to other parts of the world.

## REFERENCES

1. Al-Naeem, T.; Rabhi, F.A.; Benatallah, B.; and Ray, P.K. Systematic approaches for designing B2B applications. International Journal of Electronic Commerce, 9, 2 (Winter 2004–2005), 41–70.

2. Avison, D., and Fitzgerald, G. Information Systems Development: Methodologies, Techniques and Tools. London: McGraw-Hill, 2003.

3. Carr, C., and Moore, S. IHE: A model for driving adoption of standards. Computerized Medical Imaging and Graphics, 27, 2–3 (2003), 137–146.

4. Chau, P.Y.K., and Hu, P.J. Examining a model of information technology acceptance by individual professionals: an exploratory study. Journal of Management Information Systems, 18, 4 (Spring 2002), 191–229.

5. Chwelos, P.; Benbasat, I.; and Dexter, A. Research report: Empirical test of an EDI adoption model. Information Systems Research, 12, 3 (2001), 304–321.

6. Davenport, T.H. Putting the enterprise into the enterprise system. Harvard Business Review (July–August 1998), 121–131.

7. Devaraj, S., and Kohli, R. Information technology payoff in the health-care industry: A longitudinal study. Journal of Management Information Systems, 16, 4 (Spring 2000), 41–67.

8. Dutta, A., and Roy, R. The mechanics of Internet growth: A developing-country perspective. International Journal of Electronic Commerce, 9, 2 (Winter 2004–2005), 143–166.

9. Erasala, N.; Yen, D.; and Rajkumar, T. Enterprise application integration in the electronic commerce world. Computer Standards & Interfaces, 25, 2 (2001), 69–82.

10. Friedman, G.D. Primer of Epidemiology. New York: McGraw-Hill, 1994.

11. Grimson, J.; Grimson, W.; and Hasselbring, W. The SI challenge in healthcare. Communications of the ACM, 43, 6 (2000), 49–55.

12. Harkee, V.; Alessi, D.; and Collan, M. IT and institutional constraints: Effects of legal and administrative constraints use IT in production of health care services. In R.H. Sprague Jr. (ed.), Proceedings of the Thirty-Sixth Annual Hawaii International Conference on System Sciences. Los Alamitos, CA: IEEE Computer Society Press, 2003 (available at csdl2.computer.org/ comp/proceedings/hicss/2003/1874/06/187460164b.pdf).

13. Hu, P.J.; Chau, P.Y.K.; Sheng, O.R.L.; and Tam, K.Y. Examining the technology acceptance model using physician acceptance of telemedicine technology. Journal of Management Information Systems, 16, 2 (Fall 1999), 91–112.

14. Iacovou, C.L.; Benbasat, I.; and Dexter, A. Electronic data interchange and small organizations: Adoption and impact of technology. MIS Quarterly, 19, 4 (1995), 465–485.

15. Irani, Z., and Love, P.E.D. The propagation of technology taxonomies for evaluating investments in information systems. Journal of Management Information Systems, 17, 3 (Winter 2000–2001), 161–177.

16. Irani, Z.; Ezingeard, J.N.; and Grieve, R.J. Integrating the costs of an IT/IS infrastructure into the investment decision making process. International Journal of Technological Innovation, Entrepreneurship and Technology Management, 17, 11–12 (1997), 695–706.

17. Irani, Z.; Themistocleous, M.; and Love, P.E.D. The impact of enterprise application integration on information systems lifecycles. Information & Management, 41, 2 (2003), 117–187.

18. Irani, Z.; Sharif, A.; Love, P.E.D.; and Kahraman, C. Applying concepts of fuzzy cognitive mapping to model: The IT/IS investment evaluation process. International Journal of Production Economics, 75, 1–2 (2002), 199–211.

19. Janesick, V. The choreography of qualitative research design. In N.K. Denzin and Y.S. Lincoln (eds.), Handbook of Qualitative Research. Thousand Oaks, CA: Sage, 2000, pp. 379–399.

20. Johannesson, P., and Perjons, E. Design principles for process modelling in enterprise application integration. Information Systems, 26, 3 (2001), 165–184.

21. Kasimin, H., and Yusoff, M. The use of a soft systems approach in developing information systems for development planning: An exploration in regional planning. Computers Environment and Urban Systems, 20, 3 (1996), 165–180.

22. Khoumbati, K.; Themistocleous, M.; and Irani, Z. Evaluating integration approaches benefits adopted by healthcare organizations. In T. Leino, T. Saarinen, and S. Klien (eds.), Proceedings of the Twelfth European Conference on Information Systems. Turku, Finland: Turku School of Economics and Business Administration, 2004 (available at aisel.isworld.org/ pdf.asp?Vpath=ECIS/2004&PDFpath=20040083.pdf).

23. Kim, K.K, and Michelman, J. An examination of factors for the strategic use of information systems in the healthcare industry. MIS Quarterly, 14, 2 (1990), 201–215.

24. Kim, K.K., and Umanath, N. An empirical investigation of electronic integration in a supply chain relationship. In P. De and J.I. DeGross (eds.), Proceedings of the Twentieth International Conference on Information Systems. Atlanta: Association for Information Systems, 1999, pp. 546–551.

25. Kimberly, J., and Evanisko, M. Organisational innovation: The influence of individual, organisational, and contextual factors on hospital adoption of technological and administrative innovations. Academy of Management Journal, 24, 4 (1981), 689–713.

26. Kohn, L. To Err Is Human: Building a Safer Health System. New York: National Academy Press, 2000.

27. Kosko, B. Neural Networks and Fuzzy Systems. Englewood Cliffs, NJ: Prentice Hall, 1992.

28. Lai, C.L.; Lee, W.B.; and Ip, W.H. A study of system dynamics in just-in-time logistics. Journal of Materials Processing Technology, 138, 1–3 (2003), 265–269.

29. Lam, W. Investigating success factors in enterprise application integration: A case driven analysis. European Journal of Information Systems, 14, 2 (2005), 175–187.

30. Lane, D.C., and Oliva, R. The greater whole: Towards a synthesis of system dynamics and soft systems methodology. European Journal of Operational Research, 107, 1 (1998), 214–235.

31. Lang, R. ROI and IT: Strategic alignment and selection objectivity. Journal of Healthcare Information Management, 17, 4 (2003), 2–3.

32. Lee, S.; Kim, B.G.; and Lee, K. Fuzzy cognitive map–based approach to evaluate EDI performance: A test of causal model. Expert Systems with Applications, 27, 2 (2004), 287–299.

33. Linthicum, D. Enterprise Application Integration. Reading, MA: Addison-Wesley, 1999.

34. Linthicum, D. B2B Application Integration. Reading, MA: Addison-Wesley, 2000.

35. Malvey, M. Simple Systems, Complex Environment. Beverly Hills, CA: Sage, 1981.

36. Michio, K.; Kazuhiko, O.; Hiroyuki, Y.; Yutaka, A.; Fumiaki, K.; Hiroyuki, F.; Shingo, H.; Takaya, S.; Shigeki, T.; and Mansaori, A. Merit-9: A patient information exchange guideline using MML, ML7 and DICOM. International Journal of Medical Informatics, 51, 1 (1998), 59–68.

37. Minder, C. Factors affecting the adoption and diffusion of XML and Web services standards for e-business systems. International Journal of Human–Computer Studies, 58, 3 (2003), 259–279.

38. Puschmann, T., and Alt, R. Enterprise application integration—The case of the Robert Bosch group. Journal of Enterprise Information Management, 17, 1 (2004), 105–116.

39. Rogers, M. Diffusion of Innovations. New York: Free Press, 1983.

40. Ryan, S.D., and Harrison, D.H. Considering social subsystem costs and benefits in information technology investment decisions: A view from the field on anticipated payoffs. Journal of Management Information Systems, 16, 4 (Spring 2000), 11–40.

41. Shang, S., and Seddon, P. Assessing and managing the benefits of enterprise systems: The business manager’s perspective. Information Systems Journal, 20, 12 (2002), 271–299.

42. Sharif, A., and Irani, Z. Research note: Theoretical optimisation on IT/IS investments. Logistics Information Management, 27, 2 (1999), 287–299.

43. Skoumpopoulou, D., and O’Kane, J. EAI implementation: Case studies of five multinational companies. In Z. Irani, S. Alshawi, and O. Sarikas (eds.), Proceedings of the First European and Mediterranean Conference on Information Systems. London: Brunel University Press, 2004 (available at uxisweb1.brunel.ac.uk/iseingsites/EMCIS/EMCIS2004/subsite/ default.htm).

44. Stal, M. Web services: Beyond component-based computing. Communications of the ACM, 45, 10 (2002), 71–76.

45. Sutherland, J., and Heuvel, W. Enterprise application integration and complex adaptive systems. Communications of ACM, 45, 10 (2002), 59–64.

46. Themistocleous, M. Justifying the decision for EAI implementations: A validated proposition of influential factors. Journal of Enterprise Information Management, 17, 2 (2004), 85–104.

47. Themistocleous, M.; Irani, Z.; and Love, P.E.D. Evaluating the integration of supply chain information systems: A case study. European Journal of Operational Research, 159, 2 (2004), 393–405.

48. Toussaint, P.; Bakker, A.; and Groenewegen, L. Integration of information systems: Assessing its quality. Computer Methods and Programs in Biomedicine, 64, 1 (1992), 9–35.

49. Wu, C. A readiness model for adopting Web services. Journal of Enterprise Information Management, 17, 5 (2004), 363–371.

50. Xirogiannis, G., and Glykas, M. Fuzzy cognitive maps in business analysis and performance-driven change. IEEE Transactions on Engineering Management, 51, 3, (2004), 334–351.

51. Xu, Y.; Sauquet, E.; Zapletal, D.L.; and Degoulet, P. Integration of medical applications: The mediator service of the synex platform. International Journal of Medical Informatics, 58– 59, 1 (2000), 157–166.

52. Yin, R.K. Case Study Research Design and Methods. Thousand Oaks, CA: Sage, 2003.

53. Zabada, C.; Singh, S.; and Munchus, G. The role of information technology in enhancing patient satisfaction. British Journal of Clinical Governance, 6, 1 (2001), 9–16.
