---
otero_id: 14250
otero_key: "GN4TN32J"
title: "Knowledge networking to support medical new product development"
authors: "Kannan Mohan; Radhika Jain; Balasubramaniam Ramesh"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.02.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Knowledge networking to support medical new product development

Kannan Mohan <sup>a,⁎</sup>, Radhika Jain <sup>b</sup>, Balasubramaniam Ramesh <sup>c</sup>

<sup>a</sup> Department of Computer Information Systems, Zicklin School of Business, Baruch College, United States

<sup>b</sup> Department of Management Information Systems, Fogelman College of Business and Economics, University of Memphis, United States

<sup>c</sup> Department of Computer Information Systems, J. Mack Robinson College of Business, Georgia State University, United States

Available online 20 March 2006

## Abstract

New product development (NPD) in the pharmaceutical industry is very knowledge intensive. Knowledge generated and used during medical NPD processes is fragmented and distributed across various phases and artifacts. Many challenges in medical NPD can be addressed by the integration of this fragmented knowledge. We propose the creation and use of knowledge networks to address these challenges. Based on a case study conducted in a leading pharmaceutical company, we have developed a knowledge framework that represents knowledge fragments that need to be integrated to support medical NPD. We have also developed a prototype system that supports knowledge integration using knowledge networks. We illustrate the capabilities of the system through scenarios drawn from the case study. Qualitative validation of our approach is also presented.

© 2006 Elsevier B.V. All rights reserved.

Keywords: Knowledge integration; Knowledge networks; New product development; Pharmaceutical knowledge management; Healthcar

## 1. Introduction

The pharmaceutical industry occupies an important position in developed economies both due to the tremendous impact it has on the daily life as well as its extremely capital intensive nature. In the USA, Food and Drug Administration (FDA) alone regulates over \$1 trillion worth of medical devices, drugs, biologics, and food products [35]. According to Association of the British Pharmaceutical Industry (ABPI), pharmaceuticals are one of Britain's leading manufacturing sectors, bringing in a trade surplus of £3.6 billion with exports valued at £11.9 billion [8].

As it represents a significant component of the developed economies, any improvements in the management of critical processes in this industry are likely to have enormous economic impact.

Pharmaceutical firms depend heavily upon their ability to rapidly develop and introduce new products into the market. In fact, product development speed directly impacts their financial bottom-line as well as their ability to satisfy unmet medical needs of patients. However, development of new medical products is complex and time-consuming. It takes anywhere between 7 and 17 years and several millions to billions of dollars to launch new medical products [16]. Some of the factors contributing to the length, cost, and uncertainty of this process include:

• The stringent regulatory requirements of governmental entities like the FDA requiring the maintenance of design history for every medical product to show that the products were developed as per the approved plan and with extensive clinical trials,

• Medical products are used to treat human beings whose well-being and safety are of utmost importance. Failure of the product can have serious consequences.

• Increasing possibilities for therapeutic intervention brought about by newer technologies, and

• Enormous investments required in research and development, and testing.

The regulatory load faced by pharmaceutical new product development (NPD) organizations is increasing to the point of overload. More records of increasing complexity will be under the scrutiny of a number of authorities as emerging markets develop [15]. For example, manufacturers have to satisfy different sets of requirements for the products marketed in the European Union which may be significantly different from those of the FDA. Furthermore, this industry faces very low success rate in NPD; vast majority of investigational products that enter clinical trials fail [16]. As a result of these challenges, medical NPD teams are constantly seeking novel ways to improve development processes, while at the same time ensuring the safety of the products under development. Effective knowledge management offers potential for such improvements in this knowledge intensive industry which draws on a variety of knowledge sources [32]. As the knowledge capital acquired by the firms during the development process is the primary source of competitiveness in this industry, it is critical to capture, communicate, and reuse this knowledge gained from various sources [29]. However, long development time-frames and the distributed nature of the research and development process across organizational and geographical boundaries exacerbate the fragmentation of knowledge generated and used across the different phases of the NPD life cycle [34]. Currently, pharmaceutical product development organizations use commercial document management systems to record NPD design history [9]. These systems place significant restrictions on the type and granularity of knowledge that can be recorded. Also, these systems do not provide adequate support to integrate knowledge that is scattered throughout the various phases and artifacts of the NPD process [9].

Our research is based on the premise that, in order to effectively manage knowledge in the medical NPD process, techniques to integrate fragmented knowledge chunks are essential. A critical problem in facilitating the integration of knowledge to support NPD is that there has been little attention focused on providing specific guidelines to medical product developers on how to effectively integrate essential knowledge elements so that they are useful throughout the product life cycle [33]. In this research, we address this issue by developing an approach to seamlessly integrate fragmented knowledge using knowledge networks. Semantic knowledge networks provide the ability to describe and follow the life of a physical or conceptual artifact. These have been used as effective solutions to support knowledge integration in knowledge intensive processes in multiple domains [25]. Motivated by their effectiveness in supporting knowledge intensive processes, we propose the creation and use of knowledge networks to facilitate integration of knowledge fragments that are generated and used in medical NPD. The development of a knowledge network should be guided by the unique characteristics of the medical NPD domain. Based on this premise, we address the following key research questions:

(1) What are the elements of a knowledge network that can facilitate knowledge integration in medical NPD? and

(2) What functionalities should be provided in a system that supports the creation and use of knowledge networks to facilitate knowledge integration in medical NPD?

The paper is organized as follows: Section 2 provides the background on the process of medical NPD, along with unique issues in this area. We draw from the literature on knowledge integration for supporting medical NPD. We then present knowledge networking as an approach for knowledge integration to support NPD in this domain. This is followed by the description of a case study in Section 3. Based on our case study and literature review, we draw the requirements that must be satisfied by the proposed approach. We then present our knowledge integration framework. Section 4 presents our prototype system. In Section 5, we present the preliminary qualitative evaluation of the usefulness of our approach. Section 6 presents the contributions of our approach and concludes with limitations and future research.

## 2. Background

2.1. New product development in pharmaceutical industry

Medical NPD typically involves the following phases: (1) Discovery, (2) Feasibility, (3) Optimization, (4) Demonstration, (5) Production, and (6) Launch and follow-through [27]. Across these phases, extensive knowledge is generated and consumed. For instance during idea generation, large chunks of knowledge associated with specific products are generated. These ideas are scrutinized during evaluation and screening. When ideas are discarded, specific reasons behind the rejections should be documented so that the same ideas are not revisited. In medical NPD, creating designs for manufacturability (DFM) [6], which is critical for success, is achieved by the use of simple designs with a small number of parts, and standardization of parts and material used. Documenting design decisions made in conformance with these principles is very helpful in justifying additional costs incurred during manufacturing. FDA has proposed Good Manufacturing Practices (GMP) [23] that can help in meeting quality requirements. GMP requires that the outputs of the mandated reviews and critical decisions made during development be recorded. This is especially important during the design phase because quality problems not addressed at this stage can have adverse impact throughout the life cycle, especially during the manufacturing phase.

In summary, the NPD process in the pharmaceutical industry may be characterized as follows:

• Cross-functional involvement: Experts in areas like marketing, manufacturing, product design, clinical trials, quality assurance, evaluation, and regulatory constraints need to effectively collaborate during the process of NPD.

• Creation and use of fragmented knowledge at various phases: Knowledge is spread across different stakeholders across various aforementioned functional areas and across various phases and tasks.

• Significant documentation of processes, product life cycle, and design history required by regulations: Failure to comply with regulations that mandate extensive documentation of the design process can result in not only hefty fines, but also potentially expensive litigation if any problems develop even after the product launch.

• Need for shared understanding: Complex dependencies across functional areas necessitate a shared understanding among stakeholders who play critical roles in these areas.

The above discussion highlights the importance of integrating fragmented and distributed knowledge in medical NPD. In the following section, we review the specific challenges in managing this knowledge for medical NPD.

## 2.2. Challenges in managing knowledge in medical NPD process

A major portion of the development costs in the pharmaceutical industry is attributed to insufficient and ineffective knowledge sharing [14]. Before a drug is manufactured and is made available to the public, it follows primarily a non-physical supply chain in which access to intellectual capital is considered critical for success. Exchanging knowledge among participants in the NPD activities during discovery and development of a drug concept can be very costly. The Research & Development (R&D) of a drug is initiated by generating hypotheses for new compounds using both proprietary and public domain information. Lack of knowledge sharing across the stakeholders involved in R&D processes results in duplication of effort, failure to recognize problems early, and loss of knowledge due to turnover [29]. For example, using knowledge from idea conception and hypotheses development to prioritizing targets and compounds in later development stages can lead to faster drug development. Typically, this type of knowledge gets shared across projects or development team members on an informal basis or through a committee appointed for the purpose. At times, fragments of it may be documented to satisfy an immediate need. This knowledge may be lost along with the context in which it was generated and used, and can only be retrieved if there are mechanisms for identifying and locating the author and/or consumer of the knowledge [18].

With the increasing number of mergers (such as the recent merger of Warner-Lambert and Pfizer in 2000) [1], the advent of high-throughput technologies of unparalleled speed and scope (such as genomics and proteomics), and staff turnover [29], it is becoming harder for pharmaceutical organizations to keep track of this knowledge. In addition, long development cycles and the distributed nature of the development process make face-to-face knowledge sharing and transfer very difficult, if not impossible. As a result, the need to acquire such knowledge to bring the development and clinical data back into the research process is becoming increasingly important. This need is highlighted in the case of the recent recall of Merck's Vioxx on Sept. 30, 2004. The potential litigations and corporate liability of taking this drug off the market is huge, especially because there are over 20 million consumers of this product. In fact, the ability of Merck to sufficiently justify the critical decisions made during product development is expected to be a major factor in determining the potential financial implications of the recall. The ability to acquire existing knowledge and generate new knowledge is critical to acquire patents and develop new drugs that are converted into marketable products, clearly defining the competitive advantage for pharmaceutical organizations. Of specific interest in our research is the ability of these organizations to integrate fragmented and distributed knowledge. Issues in achieving this integration in medical NPD process are discussed in the next section.

## 2.3. Knowledge integration

An important component of knowledge integration is the pooling and recombination of individuals' tacit knowledge to create group level knowledge [7]. It can be seen as the synthesis of specialized knowledge that is distributed across various phases and artifacts in th NPD process, into situation-specific systemic knowledge to create organizational value and increase effectiveness of knowledge application [2,12]. While there has been significant focus on knowledge integration in various industries, pharmaceutical industry is now becoming increasingly cognizant of the ways in which knowledge integration can be achieved. For example, Abbott's [1] classification of hard and soft, and routine and ad-hoc information sources, is useful in achieving knowledge integration across various phases from discovery and development to the marketing of medical products. During the late phases of the development process, the need to integrate knowledge obtained through a variety of sources such as clinical trials, clinical pharmacology, case-studies, medical research reports, as well as knowledge from the develop ment of other related drugs, is central to adequately substantiate the side effects of medical products and to support internal decision-making [19]. Neumann and Thomas [22] report a similar phenomena in life sciences informatics and state that making informed decisions requires synthesis of knowledge over a wide variety of domains. They highlight the current archaic nature of development practices and assert that mechanisms are needed to integrate and use diverse knowledge sources to achieve maximum value realization In the absence of such a capability, scientists fail to spot potentially critical details and unwittingly settle for less-than optimal outcomes. Furthermore, knowledge of actual customer needs that marketing departments possess, should b made available in a timely and usable manner when a new product development is initiated to ensure its commercial success and viability [30].

Problems in knowledge integration are also partly attributed to novelty, dependence, and specialization of each functional unit involved in the NPD process [4]. If the knowledge generated from early phases of the NPD is shared with the entire team, functional units that participate in the later stages of NPD can begin their work in parallel rather than waiting for the completion of the entire design or R&D phase. As medical NPD increasingly involves virtual teamwork, the following challenges identified by prior research [2] in integrating diverse, fragmented, and distributed knowledge in these teams also require careful examination:

• Constraints on transactive memory: Transactive memory facilitates pooling of stakeholders' tacit knowledge to support the performance of collective tasks.

• Insufficient mutual understanding: Mutual understanding is referred to as the common ground between those involved in the development process. Mutual understanding enhances comprehension and interpretation of the knowledge that is communicated.

• Failure to share and retain contextual knowledge: This leads to misunderstanding and misinterpretation among stakeholders. Communication among team members usually focuses on commonly held knowledge and tends to overlook uniquely held knowledge [31]. This uniquely held knowledge fails to draw attention and is lost during the process. Also, knowledge may not get reused because it is difficult to access and is highly interdisciplinary in nature.

• Organizational ties become essential between the various teams involved in the development process.

Various knowledge integration mechanisms to address the above problems have been proposed by past research [2,12]. Operational manuals and directives that embody diverse knowledge created by various experts are commonly used for knowledge integration. Organizational routines are considered effective in integrating tacit knowledge. For complex and non-routine tasks, using self-managed teams results in effective knowledge integration [2]. Although these generic guidelines are valuable, there has been a paucity of research that addresses the unique knowledge integration challenges in medical NPD. In the following section, we summarize past knowledge integration initiatives in the medical NPD literature.

## 2.4. Knowledge integration initiatives in medical NPD process

While pharmaceutical industry has been slow to implement knowledge management initiatives, there is an increasing awareness in the industry about this issue as is evident from the creation of R&D alliances and knowledge management initiatives in pharmaceutical organizations worldwide. For example, Roche has a network of over 30 R&D alliances worldwide with companies such as deCODE genetics (Reykjavik, Iceland) and Partners Health-Care System (Boston, USA), which have strengthened Roche's access to innovations [26]. Industry leaders such as Pfizer, Merck, and Glaxo-Wellcome are increasingly recognizing the benefits of similar initiatives [20]. The need for knowledge sharing and transfer across organizational boundaries and the lack of tools that can help with these processes in complex and dynamic environments has been highlighted by past studies at AstraZeneca, a pharmaceutical organization [28]. The NDA (New Drug Application) expertise system, developed at Roche, represents early efforts towards knowledge capture and the development of a knowledge model [18]. At the core of this system is a sixvolume paper-based document that serves as a repository for synthesized worldwide regulatory requirements from the agencies that must approve new drug applications and continuously monitor a drug's use. A primary limitation of this manual approach is that it is difficult to search, locate, and update relevant pieces of knowledge. Although several IT systems are being used in drug discovery and development, most of these are standalone systems and rarely communicate with each other, which can lead to significant duplication of effort [18].

Projects Management Workbench, a knowledgebased tool developed in-house to accelerate drug development at Eli Lilly, primarily focuses on serving as an electronic repository for various documents and reports in addition to providing access to several glossaries, templates, directories, planning, and financial tools. It manages knowledge at the level of documents or files, making it too coarse for easy access and update. Although past research has attempted to identify high-level frameworks for clinical application integration infrastructure [3], research on knowledge integration in medical NPD has been very limited. The knowledge discovery tool (KDT) [21] allows the integration of fifteen publicly available sources of disconnected biomedical information. Whereas this research seeks to mine hidden linkages from data sources, it does not support the integration of contextual knowledge fragments.

Motivated by the dearth of research that adequately addresses knowledge integration challenges in medical NPD, we propose the use of knowledge networks as a knowledge integration mechanism.

## 2.5. Knowledge networks for knowledge integration

The discussion in the earlier sections highlights that medical NPD process is very knowledge intensive and requires pooling and integrating knowledge from a large number of sources. We propose that such knowledge integration can be achieved by establishing a knowledge network. A knowledge network can be defined as a network in which nodes represent different fragmented and distributed knowledge components that are critical for medical product development and are integrated through links of different types. These are networks of people and information systems associated with collaborative, knowledge-intensive tasks such as those involved in medical NPD. It includes links to the stakeholders who are involved in the creation, maintenance, and use of knowledge fragments, as well as the sources in which knowledge fragments are stored. A knowledge network may be used to link the knowledge fragments that are generated and used at different phases in the NPD process. Such a knowledge network plays a critical role in supporting the exploration and justification of design decisions and solutions. Further, understanding the context in which key design decisions are made will help in monitoring the repercussions of changes in the underlying context. For example, the history of designs and underlying assumptions associated with alternatives considered during specific development activities can help provide a dynamic validation of the decisions under varied contexts.

To understand the notion of knowledge networking in the medical NPD domain, let us consider the phases involved in the NPD process and the artifacts developed. Fig. 1 shows that various artifacts and knowledge fragments embedded in them (denoted as small, filled ellipses) that are generated at various phases of the NPD may be linked to form a knowledge network. Examples of these artifacts include documents on trial protocols, applications for approvals, etc., and examples of knowledge fragments include initial ideas for drug development, reasons why some ideas were screened out, decisions made during prototype design, aspects of clinical trial design and clinical results, and documents that are created to comply with FDA regulations.

The knowledge network provides links between artifacts and knowledge fragments generated within a particular phase or between artifacts generated across different phases. It also includes rationale behind critical decisions and links to relevant elements of knowledge. Links to stakeholders who are involved in creation and use of these knowledge elements are also part of the knowledge network. An example of such a knowledge network for medical NPD is shown in Fig. 2. Various artifacts act as ‘sources’ of knowledge. These artifacts are managed in different ‘tools and environments’ like document management systems and collaboration environments. Different ‘tasks’ performed by various ‘stakeholders’ during various ‘phases’ of the medical NPD necessitate the generation and use of these knowledge elements.

![](/api/attachments/GN4TN32J/fulltext/images/55c5bae3eddb03329f0303a2998e860cc56bd095eb2124a2c14c8e0d9c1dd7f7.jpg)  
Fig. 1. Integrating knowledge by establishing a knowledge network.

Our approach to developing a knowledge network that integrates fragmented and distributed knowledge in medical NPD involves the following steps. These steps also address the two research questions discussed in Section 1:

• Development of a framework for knowledge networking (addresses research question 1): This framework will represent the knowledge elements that are to be acquired and linked.

• Development of a prototype knowledge networking system (addresses research question 2): This system is capable of creating a knowledge network by establishing links across different knowledge elements that are identified in the framework.

• Examination of the usefulness of our approach to knowledge integration in medical NPD: Validation will involve demonstrating our approach to stakeholders involved in the NPD process and obtaining qualitative feedback from them about the usefulness of our approach.

The following sections describe these three steps involved in our approach to developing a knowledge integration solution for medical NPD using knowledge networks.

## 3. Framework for knowledge networking to support NPD in pharmaceutical industry

The first step in our approach (addressing research question 1: What are the elements of a knowledge network that can facilitate knowledge integration in medical NPD?) is the development of a framework to identify the fragmented knowledge elements that must be integrated to support NPD and the specification of requirements to effectively integrate these knowledge fragments. This framework constitutes a common vocabulary that can be used by the stakeholders involved in NPD. It identifies knowledge elements that are likely to be valuable during NPD. To develop this knowledge framework, we conducted a case study in a leading pharmaceutical organization. We describe the details of case study in the following section.

![](/api/attachments/GN4TN32J/fulltext/images/c4891951663e8d7b563a00b3aaaf79921b5998d19a542bdcb31b5914dc8265d3.jpg)  
Fig. 2. Components of a knowledge network in medical NPD.

## 3.1. Case study

The case study method has been suggested as the best suited method to understand interactions among information technology innovations and organizational context [36]. A single case study is appropriate when it is a revelatory or a critical case that helps investigate a phenomenon in depth and provides rich understanding [36]. Though single case studies might result in detailed and particularistic findings, more general insights can be obtained from such studies through ‘analytic generalization’ [36]. The organization (hereafter referred to by the pseudonym Pharmco) in which we conducted our case study develops pharmaceutical products and medical devices. The purpose of the case study was to understand the process of NPD in the medical domain, specifically focusing on the need for and challenges to achieve knowledge integration. The selection of the organization as the site for our case study was based on purposive sampling and was driven by the following reasons:

(1) This organization is one of the leading pharmaceutical product development organizations in the world, with numerous products under development at various stages in different business units,

(2) It follows significantly mature processes for medical NPD and document management, and

(3) Despite the considerable process maturity, initial discussion with stakeholders in the organization revealed that they face challenges in managing knowledge in medical NPD.

Qualitative data was collected through semi-structured interviews with stakeholders playing different roles in the NPD process. Scientists involved in conceiving new ideas for NPD and focusing on their development, business process analysts focusing specifically on studying the processes followed for NPD and identifying solutions for managing documents generated throughout this process, and developers who customize and configure these solutions to suit to this organization were identified as key informants for our study. Whenever possible interviews were recorded and transcribed. In some situations, detailed notes were taken during interviews. Each interview lasted at least 1.5h and each informant was interviewed multiple times. Analysis of this data yielded important insights into the role of knowledge integration in the process of developing new products in medical domain. Due to lack of significant literature focusing specifically on knowledge networking for pharmaceutical NPD, no a priori coding scheme was developed. Data analysis followed open, axial, and selective coding techniques, commonly used as part of the grounded theory method. Segments of data were labeled initially with codes. These codes were then categorized and relationships between categories were created, resulting in the knowledge networking framework.<sup>1</sup>

The focus of the study was on understanding the needs to capture design history when developing new medical products. Data from the case study emphasized the importance of documenting the design history from the time the idea is conceived till the product goes into production and is launched in the market. (“Main motive behind design history is for any pharma medical device company whatever you manufacture, you manufacture a tablet or a medical device, you need to maintain a history of how you did that. You have to keep record of from when you thought you can make to the actual product you launched into the market.”) Further, FDA requires that experiments conducted as a part of clinical tests are documented in detail. For many products, over 100 different types of documents with more than 1000 pages each are used to document the complete development process. Throughout the process of NPD, documents go through a life cycle consisting of the following successive phases: Open, Initiate, Authenticate, Review, Approve, and Complete. The process of managing the document life cycle is significantly complex and time-consuming. In some cases, just the approval phase may take more than six months as this requires review and validation of various fragments of relevant knowledge that are spread across the organization. In this highly regulated industry with stringent demands on quality, a product cannot be launched until the design history is documented adequately. (“The rule is, until you complete your design history file and you get your design history file approved totally, you can't sell the product. That's what FDA requires. So if you are spending 6–7 months within a company trying to get some approval, you are basically delaying the product in the market by 6–7 months. That is losing a lot of money for the company”) Significant benefits can be realized if the approval phase for the documents can be shortened. The capability to manage design history documents is key to successful and rapid development of medical products.

When different versions of documents are created to address different uses of a medical product, each version needs to go through the approval process independently. Similarly, revisions to documents also require approval. Each revision must be justified with detailed rationale. The process of managing different versions of approved deliverables, acquiring documentation about the latest approved version, and monitoring the reasons behind changes to them is very tedious. (“In the manual process, the problem the company had was [that] the paper document should be approved and it was revised. What if instead of getting the revised document approved I got the same document which I got approved this morning?”) Any mistakes committed in the process can result in heavy fines imposed by the FDA. Even simple tasks, considered routine administrative tasks in most domains, such as the removal of a file from the system, require justifications. Pharmco uses a change control system to manage deliverables. Though this system can help track changes to files, the ability to manage knowledge fragments at a lower level of granularity can help avoid a lot of rework. (“Each deliverable refers to [many] other deliverables. They are referred to at the document level. In some cases, these are paper copies, and in some, there are electronic copies.”)

Design history files are maintained to comply with Good Manufacturing Practices (GMP). The ability to manage dependencies across different documents and deliverables is very critical in the efficient management of design history. (“I have to first get my requirements approved to write the design specifications. I have to get the design specification approved. The end product/ system that you design has to meet all the requirements. If the end system doesn't meet all the requirements you have to do something called hazard analysis. Basically hazard analysis is: what is the impact if you don't meet a requirement?”) Each design history file may be made up of several deliverables and each of these deliverables may have complex dependencies among them. For example, a file containing results from a clinical trial from a healthcare facility needs to be linked to a file summarizing the results from several related clinical trials. Pharmco tracks dependencies for each document or file. However, this coarse level of granularity for managing dependencies leads to a lot of unnecessary rework. For example, when a document containing the results from a clinical trial is updated based on changes submitted from the corresponding healthcare facility, all documents that depend on it need to be reevaluated. Commercial product life cycle and document management systems are used by this organization to manage design history documents. As these systems do not provide the ability to maintain dependencies at a finer level of detail, say across relevant sections of documents, this recurrent activity generates enormous amount of unnecessary workload in the approval process. In addition, the retrieval and reuse of knowledge is also constrained by this approach. For example, when different versions of a product go through the FDA approval process, the design history documents for each of these are maintained independently in spite of an overwhelming amount of overlap among them. Due to such fragmentation, the organization is forced to repeatedly engage in a costly process of acquiring and presenting similar or same information to satisfy very similar FDA requests or mandates. In fact, this process may be repeated multiple times as the approval process for other countries and regions such as the European Union are initiated, resulting not only enormous amounts of avoidable work, but also long delays that may have significant economic impact on the organization. (“There was a project team of like 50 people trying to manufacture some instrument. They had people working on team from US, England, and Brazil... Project leader will be getting approvals on all individual documents [that she gets from all these places] And after that she has to also get the approval from individuals on the entire file. It's like 12 or 15 binders she has to get approval and on all of them from a few people.”)

Another difficulty faced by the NPD teams in the organization is the inability to seamlessly access and reuse knowledge fragments that are distributed among collaborating team members, often in systems using different formats and tools. Though the standardization or centralization of these knowledge sources is impossible and even undesirable, the inability to quickly determine where and how relevant knowledge components are located was among the chief concerns of the NPD teams. (“We don't know what the old system does, I mean we are getting the product out, but when it breaks down we don't know how to fix it. FDA mandates that you have to know your systems. If you don't know your system you don't know how safe it is, you cannot use it on human beings”).

The need to address these issues faced by the various stakeholders in the NPD process forms the basis of our research.

## 3.2. Requirements and solutions

As a part of the case study, we also reviewed various regulatory guidelines and documentation practices mandated by FDA that were used by Pharmco. Based on interview data, a thorough analysis of the guidelines and documentation practices, and a review of relevant literature, we identified the following requirements to support knowledge integration in medical NPD. In Table 1, these requirements are mapped to a set of characteristics of a potential solution that satisfies them. The table also categorizes the requirements based on the knowledge integration challenges discussed in Section 2.

## 3.3. Knowledge networking framework

Based on the findings of our case study and the requirements identified above to address the various knowledge integration issues, we developed a framework for knowledge networking that facilitates integration of knowledge. Drawing from prior literature on knowledge integration [17], we use a multi-layered framework for supporting process, control, and information layers in medical NPD. Different layers in the knowledge network are necessary to preserve the situated nature of knowledge that is acquired and used throughout the medical NPD process. Different applications of the knowledge network may require the use of knowledge across these levels. For example, a knowledge network to support Good Manufacturing Practices [23], Good Clinical Practices [10], Good Laboratory Practices [11], etc., may require the use of knowledge at all the three levels.

The implementation of the proposed framework requires the following capabilities:

• Abstraction mechanisms that allow the variation of granularity and sophistication in knowledge networking: This refers to the capability to customize the level at which knowledge is acquired and linked in the knowledge network.

• Inference services supporting the semantics of the different types of links in the knowledge network: Depending on the nature of the links, changes in some pieces of knowledge should be propagated to dependent knowledge elements.

• Maintenance of thick descriptions of traces, say using multimedia, in case the initially chosen level of traces needs to be reassessed later.

• Mechanisms that allow stakeholders in the process to define and enact a model-driven knowledge networking process accompanying the NPD process: Knowledge network frameworks drive the process of acquiring, linking, and using knowledge chunks that improve the effectiveness of the NPD process.

Table 1  
Table 1 (continued)

<table><tr><td colspan="3">Requirements for knowledge integration (KI) in medical NPD and solutions needed</td><td>KI challenge</td><td>Requirements for KI in medical NPD</td><td>Solution needed</td></tr><tr><td>KI challenge</td><td>Requirements for KI in medical NPD</td><td>Solution needed</td><td>6.</td><td>Knowledge Contextualization {KC}: Use development history documents at the conclusion or termination of a project for organizational learning [29]: Stakeholders should be able to understand the context in which certain decisions were taken that led to the conclusion or termination of projects.</td><td>Provide specific primitives to represent knowledge about history of the project, capturing the successes and failures of critical decisions, along with their rationale.Support a variety of models to represent rationale.</td></tr><tr><td>1. Constraints on transactive memory</td><td>Knowledge Assembly {KA}: Participants must be able to control the assembly of knowledge – the process of bringing together knowledge required for a specific situation – relevant to them [22].</td><td>Provide facilities to integrate knowledge fragments at the level of detail or granularity desired by project participants.Provide facilities to link knowledge sources that may be distributed across different layers in the NPD process.</td><td rowspan="2">7.</td><td rowspan="2">Knowledge Evolution {KE}: Recognition that activities conducted and information needs change over a period of time [18].</td><td rowspan="2">Provide facilities to manage the repercussions of changes to contextual information on decisions and related knowledge fragments and artifacts.</td></tr><tr><td>2.</td><td>Knowledge description {KD}: Knowledge must carry its pedigree -so that it can be evaluated based on its source [22] and life cycle [18].</td><td>Every artifact developed in the NPD process is linked to its source and the task that generated it.</td></tr><tr><td>3.</td><td>Knowledge Sources {KS}: Knowledge sources should include not only structured databases but also unstructured sources such as extant literature and document management systems [18,19].</td><td>Provide facilities for integrating knowledge stored in structured as well as unstructured knowledge sources.For example, facilitate integration of knowledge stored in tools like MS Word, MS Outlook, and NetMeeting.</td><td>8. Inflexibility of organizational ties</td><td>Cross-functional Integration {CFI}: Stronger ties between the various practice areas in medical NPD: Although FDA provides guidelines for various areas (GMP, GCP, etc.), lack of ties between these practice areas limits the extent to which knowledge can be shared and understood across these areas.</td><td>Networking knowledge chunks across boundaries of practice areas: Knowledge that is fragmented across these areas should be linked in meaningful ways so that it facilitates increased ties and sharing across these practice areas.</td></tr><tr><td>4.</td><td>Knowledge Organization {KO}: Assembled knowledge must be organized such that it can be reasoned upon [22].</td><td>Provide primitives necessary to represent both informal and formal knowledge components. Provide facilities to create a network of knowledge components.</td><td rowspan="2">9. Insufficient mutual understanding</td><td rowspan="2">Knowledge Interpretation {KI}: Scientists may not interpret or adapt the same information the way it was intended as the knowledge has its own local interpretation [32]: This is due to the lack of common vocabulary and understanding.Knowledge that is acquired is not based on a common understanding across the various stakeholders.</td><td rowspan="2">Capture and store the context of knowledge fragment along with the knowledge element itself.</td></tr><tr><td>5. Failure in sharing and retaining contextual knowledge</td><td>Change Management {CM}: It should ensure that correct versions of documents are sent through the approval process, and changes done to these documents should be documented. All stakeholders should be sharing appropriate versions of the right documents.</td><td>Establish links between process and product related knowledge elements at different levels of granularity. Integrate this with existing tools for configuration management.</td></tr></table>

Fig. 3 shows a high-level, three-layered framework for knowledge networking [17]. It also shows some knowledge fragments such as knowledge base of potential and validated targets, toxicology information base, animal models, etc., that are consumed and generated during various phases of NPD. In this framework, knowledge elements in each layer can be linked to those in other layers. Knowledge elements in each layer can be customized for the product under development. Also, specific knowledge elements in each layer focus on specific practice areas such as Good Laboratory Practices (GLPs) and Good Clinical Practices (GCPs) put forward by the FDA.

Knowledge networks for GMP, GCP, GLP, etc., (in general GxP) can encompass elements from all the three layers. Fig. 4 shows a framework with some specialized primitives in each layer pertaining to knowledge network for Good Manufacturing Practices (GMP) for a generic medical device. The primitives shown are only illustrative and are not exhaustive. Each layer shown in the Fig. 4 is described below:

Process layer: This layer represents different aspects of the NPD process (in Fig. 4, it refers to manufacturing process). Production operations, the sequence in which these operations are performed, the production items generated out of these operations, and the sources of these items are shown in this layer. For Good Laboratory

Practices (GLPs), the process layer will represent aspects about chemical procedures used to test specimens and the knowledge generated during these processes.

Control layer: This layer represents quality systems that are required to regulate the various operations shown in the process layer. Certain aspects of design, characteristics of product items that are based on visible or invisible properties of items, and critical parts of production are controlled by quality constraints that originate from FDA regulations. In many cases, while it may be easy to assess conformance using visible properties, it may not always be possible to do the same with invisible properties (for example, the way cattle has been fed or the way meat has been cut) [17]. Therefore, it is important to distinguish between these properties and to represent relevant knowledge about both.

Information layer: This layer represents all the information required by the other two layers. When a production or design decision is taken, this decision is elaborated with its rationale, production or design issue addressed, and the impact it has on the other two layers. This layer may include models like gIBIS (Graphical Issue-Based Information System) and ReMaP (Representation and Maintenance and Process Knowledge) that have been used to represent decision rationale in a wide variety of contexts [5,24]. These models help

![](/api/attachments/GN4TN32J/fulltext/images/903472393b56011db2e5af9dc1f7c9c21a6a54404c60948d2796604b3e746c8c.jpg)  
Fig. 3. Three-layered framework supporting different practice areas.

![](/api/attachments/GN4TN32J/fulltext/images/d20ef34aa313f9fb63abd2fda65511d5c4f403b9b012fbb69689b948dd5ca417.jpg)  
Fig. 4. An example of knowledge network for Good Manufacturing Practice (GMP).

document the decision making process in terms of the issues considered during decision making, the alternatives that can resolve the issues, and arguments that support or oppose the issues and the decisions that resolve the issues. Decision rationale is linked to decisions taken and artifacts and processes that are impacted by them.

In summary, the framework presented above addresses research question 1 (What are the elements of a knowledge network that can facilitate knowledge integration in medical NPD?). The framework identifies the different layers and knowledge elements that are part of a knowledge network. In the next section, we describe a prototype system that has been developed to instantiate the framework. Several features of the prototype are demonstrated through an example drawn from our case study.

## 4. Prototype system

To address the research question 2 identified in Section 1 (What functionalities should be provided in a system that supports the creation and use of knowledge networks to facilitate knowledge integration in medical NPD?), we developed a prototype system for knowledge networking (hereafter referred to as HLK—HeaLthcare Knowledge Integration System). This system is designed to address key issues in integrating knowledge to provide effective support for medical NPD. The prototype system has been developed based on the requirements derived from our case study (shown in Section 3.2) and the literature on medical NPD.

HLK comprises of three layers: The user interface layer, the tool services layer, and the storage layer. The user interface provides multiple layers to support the management of multiple knowledge networks simultaneously. The tool services layer maintains consistency between knowledge elements in the network. When the state of one knowledge element is changed by a stakeholder, the services layer alerts the user about the impact on other dependent knowledge elements in the network. The tool services layer also has components that communicate with external work process tools that are used during NPD. The storage layer supports the storage of knowledge network schemas and knowledge networks that are created based on the schemas. Microsoft Visual Basic was used to develop user interface for HLK. A relational database supports instantiations of the knowledge network. HLK provides a multi-user knowledge integration environment with limited authentication capabilities.

The various functionalities of the prototype map to different requirements listed in Table 1. In the following sections, we illustrate the capabilities of HLK through a scenario drawn from our case study. This illustration also explains the process followed by NPD teams for creating, modifying, and using a knowledge network.

4.1. Defining and instantiating the knowledge network $( \mathit { 4 K A } \mathit { 3 } , \mathit { \Omega } ^ { \prime } \mathit { K O } \mathit { \bar { 3 } } , \mathit { \Omega } ^ { \prime } \mathit { K I } \mathit { 3 } ) ^ { 2 }$

Stakeholders involved in the NPD process can log into HLK to create/modify/access the knowledge networks. It can support frameworks such as the ones discussed in

Section 3.3. For instance, Fig. 5 illustrates how the knowledge framework for Good Manufacturing Practices (GMP) shown in Fig. 4 can be instantiated in HLK. Specifically, all the elements and links between them identified in Fig. 4 can be defined in HLK using a schema editor. The schema editor is used to define the node types and the relationships between the node types that are part of the network. These node types appear in the toolbar palette. The toolbar buttons can then be used to instantiate and link knowledge fragments in a knowledge network. HLK automatically checks if the nodes can be legally linked before actually creating a link. Fig. 5 shows knowledge network instantiated by the project participants during clinical testing of a new medical product. To perform clinical trials for a new drug, a trial design (which follows trial design and protocol development controls put forward by FDA's Good Clinical Practices (GCPs)) is developed. A protocol is generated from the trial design process. This protocol is used to execute the actual trial operations. The trial operations depend on FDA's safety and efficacy assessment criteria. Analysis of the results from statistical techniques is documented. Such documentation depends on requirements stated in the GCP for statistical method selection and documentation. Due to unknown effects produced by the treatment in the trials, a decision is taken to stop the trials. Such a decision is backed by appropriate rationale. The knowledge network also depicts the various dependencies among the knowledge elements. For example, the selection of a statistical method (an instance of ‘clinical trial operation’) depends on treatment 1 phase 1 for Dx (an instance of ‘clinical trial operation’), which in turn uses Dx trial protocol (an artifact). NPD team members may create such networks by identifying knowledge fragments and their links to other knowledge fragments. For each node, information on the stakeholders who created it, the documents or fragments of artifacts that contain them, and their status, etc., can be tracked. These knowledge element types can be linked to specific documents (or paragraphs in text documents or cells in a spreadsheet or records in a database) that may contain additional knowledge. This facilitates knowledge assembly (discussed in Table 1) required by various stakeholders involved in the process of NPD.

## 4.2. Integrating knowledge across different practice areas ({CFI}, {KI})

Knowledge across different practice areas in medical NPD can also be linked within HLK. For instance, knowledge created in clinical practice can be linked to knowledge created in manufacturing practice. Networking knowledge chunks across boundaries of practice

![](/api/attachments/GN4TN32J/fulltext/images/04c882d826140cc70acd1630a68649fb19ed2ff42efaa7a4a519ca00236bab4f.jpg)  
Fig. 5. A knowledge network in HLK.

areas is facilitated by the ability to create crosscutting links between knowledge elements in different layers in the knowledge network. These crosscutting links document the relationships between knowledge that is associated with various good practices suggested by FDA (Good Manufacturing Practices, Good Clinical Practices, Good Laboratory Practices, etc.). Fig. 6 shows how knowledge fragments across various practice areas can be linked to each other. In this scenario, knowledge that guides Good Clinical Practices is linked to that associated with Good Manufacturing Practices. When modifying details about a node, a project participant can open views of other NPD projects (shown as a tree-like structure in Fig. 6) and select elements that need to be linked to those in current project. Stakeholders from different areas can gain an improved understanding of how decisions taken in other practice areas can impact their decisions. For example, a knowledge element documented as part of GLP can refer to a difficulty in designing a required component for a medical device. This element impacts the assembly line of that component which is documented by several knowledge elements as part of GMP.

## 4.3. Linking knowledge fragments to sources ({KD}, {CM})

Each knowledge element can be described by associated nodes of knowledge and through links to artifacts that document their ‘life’. To facilitate such linking, HLK is integrated with MS Word, and MS Outlook, that are used to create, modify and exchange documents. For example, the knowledge element ‘Dx trial phase 1 results’ (shown in Fig. 5), an instantiation of ‘Artifact description’ that is part of the GCP knowledge network can be linked to a MS Word document that details the results of the trial. The link can be established as a property of the knowledge node. Specifically, an additional property is created for the knowledge element ‘Dx trial phase 1 results’. This property can be used to document the link between this knowledge element and the Word document that provides details on the test results. This will be valuable when decisions are documented in detail in different documents. Instead of recreating this knowledge within HLK, stakeholders can simply create a link to the sources that document this knowledge.

![](/api/attachments/GN4TN32J/fulltext/images/b49da437fbccf6be31f3b645d1d69dd00cb41d9321e4c2bf60a8b5de2eb6e36c.jpg)  
Fig. 6. Integrating knowledge from different practice areas.

## 4.4. Variety and types of knowledge sources ({KS})

Unstructured knowledge documented in various artifacts developed during the NPD process can be linked to structured knowledge. Knowledge elements used to document the history of an NPD project can be linked to additional artifacts (such as structured design models, unstructured documents and instant messages between stakeholders, items in a project plan, etc.) that document history. Discussions between various scientists and reviews done in specific contexts can be linked to specific knowledge elements. To facilitate this, HLK is integrated with Groove, a peer to peer tool that can be used for collaborative management of documents and other artifacts. Different stakeholders using diverse set of work process and collaboration tools can facilitate integration of knowledge fragments that are stored in these diverse work environments.

## 4.5. Managing dependencies and changes ({KO}, {CM})

The knowledge elements in the knowledge network have properties that can be propagated from one node to another. For example, the status of a trial can be changed if the rationale justifying a decision about the trial becomes invalidated. Such change propagation can be visually shown in HLK with a change in the color of the affected nodes. To manage knowledge about changes done to artifacts in the NPD process, HLK is integrated with MS Visual Source Safe, a configuration management system. Configuration management systems can manage versions of any artifact and bring together different versions of artifacts as a configuration. In HLK, knowledge elements in any layer can be linked to specific versions of any artifact managed in the configuration management system.

## 4.6. Integrating contextual knowledge ({KC})

The knowledge framework acts as a common vocabulary used across different stakeholders involved in the NPD process. Various elements in the framework also facilitate capture of the context in which specific knowledge and artifacts are created. For example, knowledge about trial results for one drug may become useful in the conception and development of a different product. Knowledge created in these two contexts and documented in two different knowledge networks can be linked to one another.

## 4.7. Managing knowledge evolution ({KE})

As steps in the NPD process and the information used for these steps evolve over time, the knowledge framework can be tailored to suit to the new needs. HLK is built to be flexible so that it can support customizations to the knowledge framework used. Depending on how each practice area evolves over time, the knowledge network can be customized to include any new and relevant primitives using the schema editor. HLK facilitates the evolution of elements in the knowledge network. New primitives can be linked to existing knowledge elements in the network.

Table 2 provides a mapping of the requirements in NPD to integrate knowledge and the capabilities of our knowledge networking approach that address these requirements.

Our approach presented in the previous sections demonstrates how major concerns in knowledge integration in medical NPD can be addressed using the knowledge framework and the prototype system. For example, constraints on transactive memory, insufficient mutual understanding, failure in sharing and retaining contextual knowledge, and inflexibility of organizational ties [2] are some of the critical challenges addressed by the use of a knowledge networking framework and the HLK system. In summary, these challenges are addressed in our approach as follows:

Mapping the requirements for KI in NPD and the capabilities of our approach

<table><tr><td>Capability of our approach (drawn from set of points discussed above)</td><td>Requirement addressed (drawn from)</td></tr><tr><td>Defining and instantiating the knowledge network</td><td>{KA}, {KO}, {KI}</td></tr><tr><td>Integrating knowledge across different practice areas</td><td>{CFI}, {KI}</td></tr><tr><td>Describing the life of knowledge fragments</td><td>{KD}, {CM}</td></tr><tr><td>Variety and types of knowledge sources</td><td>{KS}</td></tr><tr><td>Managing dependencies and changes</td><td>{KO}, {CM}</td></tr><tr><td>Integrating contextual knowledge</td><td>{KC}</td></tr><tr><td>Managing knowledge evolution</td><td>{KE}</td></tr></table>

• Transactive memory helps stakeholders to pool in their tacit knowledge to perform collective tasks. A knowledge network brings together explicitly coded knowledge by providing links to their locations, and tacit knowledge by providing links to the stakeholders who were involved in the NPD process.

• By providing a framework that can be used in the acquisition and use of knowledge, a common vocabulary is established thereby enhancing mutual understanding across the various stakeholders.

• Knowledge networks establish the links between knowledge chunks that are embedded in various contexts at varied levels of granularity to facilitate sharing of contextual knowledge.

• Links established between various stakeholders from various cross-functional areas involved in the process also improve organizational ties by enabling them to share knowledge that would have otherwise resided in islands fragmented from one another.

## 5. Preliminary evaluation of the knowledge framework and the prototype

A comprehensive evaluation of new technologies is very challenging, especially in mission-critical domains such as medical NPD. Since medical NPD processes typically span several years, it is very difficult to conduct field evaluations of the usefulness of the knowledge framework and the prototype system. Also, due to the low tolerance for disruptions in this domain, deployment of a new approach to knowledge integration requires approvals from very senior levels of management. Since a longitudinal study spanning several years is beyond the scope of the current study, we conducted a preliminary qualitative evaluation of our approach. The objective of the evaluation was to seek feedback from the participants in the medical NPD process on the potential usefulness of our approach and issues that should be considered before the implementation of our approach.

The knowledge networking framework and the prototype were presented to the stakeholders involved in NPD process to perform a qualitative evaluation of our approach. The participants in this exercise were the same as those who participated in the case study. The presentation included a demonstration of how requirements and features in Tables 1 and 2 addressed issues in medical NPD. We solicited comments from the participants on the utility of the framework and the prototype system. Data was collected in the form of qualitative comments. The following points summarize the qualitative feedback received from the stakeholders:

1. Usefulness of knowledge integration: All the stakeholders indicated that the ability of the system to integrate knowledge across different functional areas to capture various knowledge fragments spread throughout the temporal and spatial dimensions of the NPD will be useful in improving the NPD process. They found the ability to integrate contextual knowledge about several decisions made by NPD teams very valuable as it will allow them to follow the evolution of knowledge fragments across the various stages in the NPD process.

2. Usefulness of dependency management: The ability to manage revisions made to the several project documents and dependencies in the knowledge fragments embedded in these documents was identified as a very important feature. Further, the ability to document this knowledge at a much lower level of granularity than supported by the tools currently used in the organization was also considered by the participants to offer great potential to access relevant knowledge when needed.

3. Impact of knowledge integration on process improvement: One of the important areas where the framework and tool offer promise is in enhancing Pharmco's ability to speed up the approval process and easily find evidence when responding to or providing information to the FDA and other regulators. All the stakeholders concurred that segregating different types of knowledge fragments by their focus (i.e. process, control, and information layer) was a useful means of separating concerns.

Overall, the participants indicated that they are very likely to consider using the tool and framework. A pilot study is being planned to further assess the feasibility of our approach. However, the participants also raised some important concerns that could impede the immediate deployment of our approach on a broader scale:

1. Issues in organizational adoption: Stakeholders raised concerns about factors that impact the acceptance of a new approach to manage knowledge.

Further empirical studies are necessary to understand the impact of behavioral and normative beliefs about adopting our approach. Since this would significantly change the current knowledge processes followed in the organization, development of appropriate incentive schemes is critical to the successful adoption of the new approach.

2. Scalability, robustness, and security concerns: Since our tool is a research prototype, issues related to scalability, robustness, and security need to be carefully evaluated before it can be deployed in a production environment. The study of these issues is a subject of ongoing research.

3. Value of intellectual property: Since the knowledge capital involved in this domain is unique and critical to competitive advantage, the knowledge processes used are closely guarded making it difficult to conduct evaluations. An objective of the pilot study is the development a governance mechanism within the organization to help address this issue.

## 6. Discussion and conclusions

## 6.1. Contributions

Our approach to knowledge integration contributes to the current research and practice in the following ways:

1. It proposes a novel approach to knowledge integration in the medical NPD process

2. It presents the HLK as a ‘proof of concept’ to support knowledge integration in medical NPD

3. It provides preliminary evaluation of the usefulness of our approach in improving medical NPD.

This study is among the first to examine knowledge integration in detail in this domain. Knowledge integration is one of the major challenges in pharmaceutical industry because of the tremendous impact it has on NPD process. Our knowledge integration framework provides support for a wide range of NPD processes to accommodate regulatory standards and guidelines specified for various phases. Also, it allows customization to accommodate the needs of individual scientists and designers interested in different aspect of the medical NPD process. Further, it provides a mechanism for integrating various sources of knowledge generated and used throughout the medical NPD process. This knowledge is captured along with the wide range of contextual factors and rationale which allows for contextual interpretation of information enhancing re-usability of the knowledge. The layered approach proposed here provides an excellent mechanism to abstract out the details while simultaneously providing the capability to customize the framework for situated knowledge capture and use.

With access to integrated knowledge networks, project participants can get a comprehensive crosscutting view of the entire medical NPD process which can enhance their ability to see how their decisions affect wide range of other decisions and artifacts. It is likely to help in the early identification and mitigation of the risks that threaten the product development. By capturing FDA guidelines in the knowledge framework, recordkeeping of various decisions is made more manageable. This can allow for rapid review and approval process by regulatory agencies for ensuring new product efficacy and safety. Furthermore, reuse of knowledge can speed up the development process by reducing time-to-market, a critical factor that underlies the financial bottom-line of pharmaceutical organizations. The knowledge framework facilitated by our prototype provides an excellent mechanism to fully integrate knowledge fragmented across the large array of diverse information technologies to address diverse information needs of stakeholders involved in the process.

## 6.2. Limitations and future research

Organizational issues such as the development of an organizational climate that promotes knowledge sharing and the role of incentives in this process have not been addressed in our research. Though overhead involved in managing and integrating vast amounts of knowledge is significant, since NPD in this domain is regulated and the cost of errors is extremely high, this poses a much lesser concern when compared to NPD in other domains. However, the examination of the impact of overhead involved in documenting knowledge during NPD is the focus of future research. The identification of technical, organizational, and environmental factors that facilitate and impede the development of knowledge networks is a topic for future research. Furthermore, issues around security, administrative processes, data ownership, access, responsibility and control need to be addressed [3]. When operating in heavily regulated environment, one needs to find the right balance between information transparency and intellectual property rights, confidentiality, and legal concerns.

We are currently planning a detailed empirical evaluation of the effectiveness of the framework and prototype in improving the process of NPD. Future field research will also focus on investigating the impact of similarity in shared knowledge content and length of communications paths [13] on knowledge integration using knowledge networks.

## References

[1] R. Abbott, An overview of knowledge integration for innovation in healthcare and pharmaceuticals, Drug Information Journal 32 (1998) 905–915.

[2] M. Alavi, A. Tiwana, Knowledge integration in virtual teams: the potential role of KMS, Journal of the American Society for Information Science and Technology 53 (2002) 1029–1037.

[3] T. Bloom, G. Bunn, Clinical information platforms: infrastructure for clinical development, Drug Information Journal 35 (2001) 781–789.

[4] P. Carlile, E. Rebentisch, Into the black box: the knowledge transformation cycle, Management Science 49 (2003) 1180–1195.

[5] E.J. Conklin, M. Begeman, GIBIS: a hypertext tool for exploratory policy discussion, Presented at the ACM Conference on Computer-Supported Cooperative Work, Portland, Oregon, United States, 1988.

[6] K. Crow, Design for Manufacturability, 2001.

[7] M. De Boer, V. d. Bosch, F. A.J, Managing organizational knowledge integration in the emerging multimedia complex, Journal of Management Studies 36 (1999) 120–123.

[8] Facts and statistics from the pharmaceutical industry, The Association of the British Pharmaceutical Industry, 2004.

[9] J.M.W. Glen, M. Lord, New product development processes within the UK medical device industry, Medical Engineering and Physics 18 (1996) 670–676.

[10] Good Clinical Practice in FDA-regulated clinical trials, http:// www.fda.gov/oc/gcp/default.htm, 2004.

[11] Good Laboratory Practices, http://www.fda.gov/ora/compliance\_ ref/bimo/glp/default.htm, 2004.

[12] R. Grant, Prospering in dynamically-competitive environments: organizational capability as knowledge integration, Organization Science 7 (1996) 375–387.

[13] M. Hansen, Knowledge networks: explaining effective knowledge sharing in multiunit companies, Organization Science 13 (2002) 232–248.

[14] C. Hodgman, An information-flow model of the pharmaceutical industry, Drug Discovery Today 6 (2001) 1256–1258.

[15] D. Hughes, Dizzying but scary: looking towards R&D in 2005, Drug Discovery Today 4 (1999) 393–395.

[16] Innovation or Stagnation: Challenges and opportunities on the critical path to new medical product," U.S. Department of Food and Health Services, Food and Drug Administration (FDA), 2004.

[17] M.H. Jansen-Vullers, C.A. van Dorp, A.J.M. Beulens, Managing traceability information in manufacture, International Journal of Information Management 23 (2003) 395–413.

[18] S. Koretz, G. Lee, Knowledge management and drug development, Journal of Knowledge Management 2 (1998) 53–58.

[19] J. Kubler, T. Weihrauch, Integrated summaries and meta-analyses in clinical drug development, Drug Information Journal 36 (2002) 127–133.

[20] J. Liebowitz, Knowledge management receptivity at a major pharmaceutical company, Journal of Knowledge Management 4 (2000) 252–258.

[21] E. Liongosari, Accelerating Drug Discovery Process through Model-Based Knowledge Integration, Presented at KMWorld and Intranets, Santa Clara, CA, 2002.

[22] E. Neumann, J. Thomas, Knowledge assembly for the life sciences, Drug Discovery Today 7 (2002) s160–s162.

[23] Pharmaceutical cGMPs for the 21st century – a risk-based approach, Department of Health and Human Services, U.S. Food and Drug Administration, 2004.

[24] B. Ramesh, V. Dhar, Representing and maintaining process knowledge for large-scale systems development, IEEE Expert 9 (1994) 54–59.

[25] B. Ramesh, M. Jarke, Towards reference models for requirements traceability, IEEE Transactions on Software Engineering 27 (2001) 58–93.

[26] “Roche-Corporate Media News,” 2002.

[27] L. Rochford, W. Rudelius, New product development process: stages and successes in the medical products industry, Industrial Marketing Management 26 (1997) 67–84.

[28] J. Roth, Enabling knowledge creation: learning from an R&D organisation, Journal of Knowledge Management 7 (2003) 32–48, doi:10.1108/13673270310463608.

[29] A. Sapienza, J. Lombardino, Recognizing, appreciating, and capturing the tacit knowledge of R&D scientists, Drug Development Research 57 (2002) 51–57.

[30] C. Spiguel, The pharmaceutical industry in the 21st century: surviving in the e-business environment, Drug Information Journal 34 (2000) 709–723.

[31] G. Stasser, S. Vaughan, D. Stewart, Pooling unshared information: the benefits of knowing how access to information is distributed among group members, Organizational Behavior and Human Decision Processes 82 (2000) 102–116.

[32] A. Styhre, A. Ingelgård, J. Roth, A nonreductionist view of knowledge: product development in the pharmaceutical industry, Emergence 2 (2000) 51–67.

[33] A. Tiwana, B. Ramesh, Integrating knowledge on the web, IEEE Internet Computing (2001 May/June) 32–39.

[34] K.V. d. Voorde, K. Reygaert, System audit of a megatrial, Drug Information Journal 35 (2001) 469–473.

[35] E. Whitmore, Product Development Planning for Health Care Products Regulated by the FDA, ASQC Quality Press, Milwaukee, Wisconsin, 1997.

[36] R.K. Yin, Case Study Research: Design and Methods, Sage Publications, Beverly Hills, CA, 1989.

![](/api/attachments/GN4TN32J/fulltext/images/d41eb0a3ca383282b0b10e888fcbf7d21be6fc4c9688668c1a36764f5302fc69.jpg)  
Kannan Mohan is an Assistant Professor of Computer Information Systems at Baruch College. Dr. Mohan received his Ph.D. degree in Computer Information Systems from Georgia State University. His research interests include managing software product family development, providing traceability support for systems development, knowledge integration, and agile development methodologies. His research work has appeared in several conferences and journals including Communications of the AIS, Communications of the ACM, and Decision Support Systems.

![](/api/attachments/GN4TN32J/fulltext/images/8c79b377fdd6d9bece2d3b09a0e5d395dd4100b5d4ff6d63039c0e5975c7e9a4.jpg)

![](/api/attachments/GN4TN32J/fulltext/images/3cc4c89f536ba978c9f2b0e61c72f74e65082ac94abf616c9b0e5f09e232c086.jpg)

Radhika Jain is finishing up her doctoral work at J Mack Robinson College of Business at Georgia State University. In August 2006, she begins her appointment as an Assistant Professor at Fogelman College of Business and Economics at the University of Memphis. Her research interests include managing contextual process knowledge in different domains, business process integration, knowledge management in healthcare, and ubiquitous computing. Her work has appeared in the Requirements Engineering Journal, IEEE Computer, Journal of International Information Management, and International Journal of Mobile Computing as well as in several leading conferences.

Balasubramaniam Ramesh is a Professor of Computer Information Systems at Georgia State University. Dr. Ramesh received his PhD degree in Information Systems from New York University. His research work has appeared in several leading conferences and journals including the IEEE Transactions on Software Engineering, MIS Quarterly, Communications of the ACM, JAIS, IEEE Expert, IEEE Computer, IEEE Intelligent Systems, IEEE Internet Computing, Annals of Software Engineering, Annals of Operations Research, and Decision Support Systems among others. His research interests include supporting complex organizational processes in areas such as requirements engineering and traceability in systems development, concurrent engineering, NPD, knowledge management, and business process management.
