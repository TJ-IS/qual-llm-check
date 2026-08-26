---
otero_id: 2746
otero_key: "N6MG2TY7"
title: "Development and evaluation of a software-mediated process assessment method for IT service management"
authors: "Anup Shrestha; Aileen Cater-Steel; Mark Toleman; Suren Behari; Mohammad Mehdi Rajaeian"
year: "2020"
journal: "Information & Management"
doi: "10.1016/j.im.2019.103213"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Development and evaluation of a software-mediated process assessment method for IT service management

Anup Shrestha<sup>⁎</sup>, Aileen Cater-Steel, Mark Toleman, Suren Behari, Rajaeian Mohammad Mehdi<sup>1</sup>

University of Southern Queensland, West Street, Toowoomba, Queensland, 4350, Australia

## A R T I C L E I N F O

Keywords: Process assessment IT service management Decision support system Design science research Task technology fit Staged maturity model

## A B S T R A C T

IT service improvements can add immense value to organisations. To improve IT service management (ITSM) processes, a software-mediated process assessment method is proposed with four phases: process identification, process assessment, process capability measurement and process improvement. The international standard for process assessment was applied to measure process capability. This method was trialled at two Australian organisations and positively evaluated in a US foreign exchange trading business. Our empirical evidence challenges the underlying assumption that higher levels of process capability depend on the achievement of lower level process attributes. We conclude that this method can be applied to transparently self-assess processes.

## 1. Introduction

The impact of IT services as a source of competitive advantage for organisations of all sizes is widely accepted by practitioners, governments and academics. To realise this competitive advantage, it is vital to understand both the IT service philosophy as a whole, and the pro cesses to manage IT services. These issues are of increasing importance as the reliance of companies on IT services and the complexity of process management for IT services grow.

A process approach is widely adopted in many management areas including IT management. Much of the efort since the 1980s, in the area of IT management, has been directed towards strategic issues and business-IT alignment [1]—i.e., how to integrate IT strategies with other corporate strategies. Existing work on IT service strategy has looked into the service marketing literature and focused on adapting the SERVQUAL instrument [2] to the context of IT services. Efective implementation of an IT service strategy requires improvement of processes at the operational level; ‘A strategy is only of value if mechanisms for its implementation and renewal are in place’ [3].

Research has shown that IT services account for 60–90 percent of the total cost of IT ownership [4]. The discipline of IT Service Management (ITSM) uses service-oriented thinking and a process approach to IT management. It has been argued that it is important for organisations to understand the benefits of efective ITSM processes [5]. The expanding number of studies is an indication of the increase in research interest of academics in the area of ITSM. For example, Iden and Eikebrokk [6] provided a systematic review of ITSM research and highlighted that existing research is concentrated in the areas of critical success factors, implementation and benefits of ITSM implementation. Apart from academic papers, a large number of practitioners’ reference books have been published, which provide greater access to ITSM resources for businesses. The catalyst for widespread adoption of ITSM initiatives was the publication of the IT Infrastructure Library (ITIL®) framework that was initially created by the UK government in the late 1980s [7].

The ITIL framework is currently the most widely recognised framework to enable ITSM in an organisation [8]. The ITIL framework led to the creation of the international standard for ITSM: ISO/IEC 20000 [9]. The increasing role of ITSM to provide better IT services promotes continual improvement of the ITSM processes [10]. In the ITIL 2011 framework, Continual Service Improvement (CSI) has been proposed as a critical phase with emphasis on continuing efort to identify opportunities for process improvement [11]. The CSI concept further stresses that ‘continual assessment’ is important to identify improvement opportunities for the processes involved in IT services [12]. The recent ITIL4 framework extends the focus beyond IT service delivery to the wider perspective of the service value system, co-creation of value for customers and integration with other technologies and methods [89].

In performing service improvement activities, many organisations have adopted assessment techniques that employ systematic measurement of processes using a staged maturity model such as the Capability Maturity Model Integration (CMMI) [13]. The measurement results are then used to determine the quality level of each process, thereby helping organisations to monitor process improvement initiatives through progressive quality levels. Process assessment, how ever, needs to be diferentiated from quality audit; while audits are conducted to check conformance (for example ISO 9001 quality audit) [14], process assessment goes one step beyond conformance checks and determines the process quality of staged levels for improvement [15].

Organisations would normally engage consulting firms to conduct process assessments and determine the process areas requiring improvement [10]. Process assessments are conducted by third-party assessors and consultants, by gathering a variety of evidence such as document reviews and interviews with process stakeholders [16]. However, qualified ITSM consultants with assessment skills are scarce and expensive. Research, dating back to 1990s, confirms the scarcity and exorbitant costs of IT consulting [17]. In addition, despite the popularity of IT consulting, the performance and service quality of the large global consulting companies may be debatable [18]. Consequently, smaller organisations may refrain from hiring consultants in spite of government incentives [19]. Consulting in the area of IT process improvement is challenging because comprehensive assessment methods are expensive [20]. Moreover, outcomes from a process as sessment project imply that actions are required to change processes, leading to further impositions on budgets and time [21], which is particularly substantial for small IT service providers [22]. The high costs of process assessments are accepted as a serious challenge in the ITSM community [12,23]. An alternative to reliance on costly assessments and consultants is self-assessment, where the organisation can conduct a survey-based process assessment in-house. Past service re search has confirmed that the method of asking assessment questions directly in a survey is more eficient compared to assessment interviews [24].

Although self-assessments may encourage parsimony and can therefore promote regular assessments, the absence of a third-party authority, which has expertise in assessments and consulting, means that the transparency of the assessment and acceptance of its findings are more likely to be contentious [25]. The lack of transparency in the way processes are self-assessed has been reported in the ITSM industry [12]. Self-assessment can be efective if it facilitates a comprehensive and regular appraisal of an organisation’s processes against a standard reference model [25]. In this context, the standard reference model does not have to be used for strict adherence, but more as a useful guide to demonstrate transparency in the way assessments are conducted [26]. However, to date there is limited reported evidence of the use of a standard reference model to facilitate self-assessments in ITSM.

Current ITSM process assessment methods have not promoted self assessment. Instead, widely accepted ITSM process assessment frame works such as Tudor IT Process Assessment (TIPA) for ITIL [10], CMMI for Services [13] and ITIL Maturity Model [27] use proprietary assessment models and assessment methods. Consequently, assessment outcomes are often dictated by methods and tools employed by thirdparty assessors [11]. The research problem that we address in this paper is the lack of transparency and high costs of conducting third-party ITSM process assessments in IT organisations. To address this problem, we develop and evaluate an automated self-assessment method that determines process capability in ITSM. We call our method the Soft ware-mediated Process Assessment (SMPA) method. The SMPA method is a standards-driven process assessment exercise by which organisations can cost-efectively self-assess their ITSM processes using a Decision Support System (DSS) tool to determine the process capability for service improvement. To lend transparency to the SMPA method, its activities are based on the international standard for process assessment: ISO/IEC 15504 that is being transitioned to ISO/IEC 330xx standard series [28]. A DSS tool collects and analyses data for process assessments, and recommends process improvements.

A recent review of software tools for ITSM process assessments [28] confirms that these assessment tools are primarily used to support thirdparty assessment activities and build historical assessment data [20]. All of the assessment tools discussed in [28] are designed to assist thirdparty assessors without any support for a standards-driven self-assessment exercise. Eficiency and transparency are key requirements for successful capability assessments [29]. A standards-driven self-assessment exercise has the potential to address these requirements but we have not found any standards-based solutions being ofered in research and practice. Consequently, we propose the SMPA method as a costefective and transparent self-assessment method for ITSM process im provement.

This paper describes the design, development and evaluation of the SMPA method. The method supports assessment of the existing ITSM processes for process improvement in an organisation. After describing the design and development of the SMPA method, we report two trials at the Australian Public Sector IT service providers. Furthermore, an evaluation of the method at an IT service provider in the US is provided. Then we discuss the three major issues that emerged from our research during ITSM process assessments: the use of staged maturity models for improvement; challenges of automating assessments and the limited transparency in the assessment report. Finally, we present our conclusion with research limitations and future research considerations. The next section provides a review of the background literature related to ITSM process assessment.

## 2. ITSM process assessment

## 2.1. IT service quality

The literature associated with process assessment for IT services is grounded in the concepts of service and quality. Research on IT service quality has largely focused on outcome-oriented metrics such as user satisfaction and service gap, whereas there is limited research related to process-oriented assessment of IT service quality [30].

It is widely agreed that service quality is ultimately determined by the outcomes perceived by the customer. IT service quality has been measured using process quality metrics along with other metrics, such as information systems quality, customer satisfaction, service value and service behaviour [30]. Indicators of process quality such as process efectiveness and eficiency have been incorporated into the design of an evaluation framework in ITSM [5]. At the same time, to improve customer satisfaction, service providers should also strive to improve their business processes [31]. Organisations can conduct customer surveys to assess the outcome of their service provision. As these surveys typically focus on the outcomes, they may not assist service providers to guide their process improvement initiatives [32]. To improve IT service quality [33], IT organisations need to assess their processes [30]. Process capability is recognised as one of the indicators of process quality. Our study contributes to the literature regarding guidance on how to assess process capability.

A few process assessment methods are commercially available and promoted as ‘best practices’ in the ITSM industry. These methods are often closely related to each other but promote their proprietary assessment approaches [34]. These assessment approaches can be considered as a black-box measurement system because the rationale and the assessment activities are not fully disclosed. Furthermore, due to their proprietary nature, the results of process assessments may be inconsistent and hinder comparisons and benchmarking in the ITSM industry [6]. As ITIL gained worldwide popularity, several conglomerates of IT consultants promoted their proprietary assessment mechanisms for ITIL process assessments, including an ITIL Maturity Model [27] by AXELOS—a joint-venture company created in the UK to manage ITIL and other global best practices. Several non-ITIL methods such as CMMI for Services [13] and eSCM for service providers [35] also provide ITSM process assessment models and methods. Nevertheless, a standard and universally accepted framework for assessing ITSM processes is lacking [30]. Moreover, none of the current process assessment methods sup port automated self-assessments for process improvement in ITSM.

## 2.2. Staged maturity models

Tully, Kuvaja and Messnarz [36] traced the history of staged maturity models from Plato’s four-stage ascent of the mind, through Marx’s four stages of society development and Rostow’s five stages of economic growth and concluded that ‘staged models, whether of philosophers, economists, quality gurus or software engineers, can be seen as occupying a respectable place in that utopian tradition’ [36, p. 56]. Staged maturity models became popular after Crosby [37] produced the quality management maturity grid following on from the work of Total Quality Management (TQM) pioneers, Deming [38] and Juran [39]. Earlier, Likert [40] had defined four distinct stages of organisational maturity, which he referred to as systems of organisation. His research, conducted with the use of the now popular Likert-type questionnaires, found that System 4 organisations were the most efective and suc cessful, whereas System 1 organisations faced many problems.

After Crosby’s work was used by Humphrey [41] to develop Capability Maturity Models (CMM), maturity models have gained popu larity and have been proposed for a range of activities including quality management, software development, supplier relationships, research and development efectiveness, product development, innovation and product design [42]. These maturity models ‘consist of multiple archetypal levels that together represent the evolution of a certain do main’ [43].

The use of a staged maturity model to perform repeatable and objective assessments of IT service quality has been reported [14]. As shown in Fig. 1, the international standard for process assessment [16] comprises two dimensions: a process dimension and a capability dimension. The process dimension, represented in a process reference model [44], is based on the ITSM standard and includes base practices for the first capability level (CL1). The capability dimension, represented in a process assessment model [45], consists of nine process attributes (PA1.1-PA5.2) arranged across five capability levels (CLs). The process assessment model includes generic practices for capability levels, CL2-CL5. The process attributes comprise base and generic practices as standard assessment indicators for the measurement framework [16]. Assessment indicators are used to determine if stipulated requirements are met during an objective assessment exercise.

The ITSM Process Assessment Framework illustrated in Fig. 1 uses non-proprietary models from two international standards to enable transparent ITSM process assessments. In this framework, consistent with the principles of staged maturity models, an IT service provider must fully achieve CL1 to be considered for CL2 and so forth. Using this framework, we developed our SMPA method for demonstration and evaluation. The overall research methodology that encompasses the development and evaluation of the SMPA method is described in the next section.

## 3. Research methodology

Many scholars have argued that IT artefacts should form the core of the IS discipline [e.g. [46,47]]. For creation and evaluation of novel IT artefacts, Design Science Research (DSR) has become a well-established IS research paradigm and has been recommended as a legitimate approach, alongside other IS research methods that are used to explore or confirm hypotheses [48,49]. The DSR research design is particularly suitable for IS research because ‘the [information systems] field should not only try to understand how the world is, but also how to change it’ [50, p. 109]. DSR eforts should focus on developing practical IS as an outcome [51], which is supported in the research methodology of this study.

Using behavioural IS research design, ITSM studies have investigated various IT service process quality constructs and their relationships have been hypothesised leading to the development of statistically tested instruments to examine these relationships. For example, Lepmets, Cater-Steel, Gacenga and Ras [30] followed this research design in the area of IT service quality measures. By contrast, the DSR approach focuses on building the artefacts and evaluating their utility [49,52]. The artefacts represent knowledge production and contribution to the body of literature [53].

DSR artefacts can be categorised as constructs, models, methods and instantiations [54]. In this research, the SMPA approach is proposed as a novel method for ITSM process assessment. According to Kuechler and Vaishnavi [55], methods as research artefacts are goal-directed approaches to develop novel solutions. To demonstrate the design of the SMPA approach, a DSS as an IT artefact, which represents the SMPA approach is also constructed and evaluated. For these reasons, DSR was chosen as the preferred research design for this study.

The development of the SMPA method in this research followed DSR guidelines, as set out by Pefers et al. [56]. DSR provides a methodology whereby a research problem can be investigated by introduction of a novel artefact that is evaluated to determine its efectiveness to address the identified problem. DSR methodology is outcome-oriented and provides guidelines for development and evaluation of research artefacts that contribute to specific bodies of knowledge. The artefact, referred to as the SMPA method in this paper, enables assessments based on ITSM process assessment framework (Fig. 1) and encompasses a DSS tool.

The six DSR activities [56] were followed in the research: problem identification and motivation, defining objectives of a solution, design and development, demonstration, evaluation and communication. The DSR stages in our research were iterative with subsequent rounds of experiment and improvement. During the design and development stage, the SMPA method was revised and changes were incorporated based on the experience obtained during trial demonstrations. During the evaluation stage, the SMPA method was applied twice within a strategic process improvement project in an organisation. In this research, the impact of the SMPA method was identified from the analysis of longitudinal data collected from the repeated use of the SMPA

![](/api/attachments/N6MG2TY7/fulltext/images/f1f98471bb850e483d9d10018f68c9ba9721d6838d9952348f72f5a8b57e7b40.jpg)  
Fig. 1. ITSM Process Assessment Framework (Adapted from ISO/IEC 33020 [86]).

method.

The SMPA method presents a guided approach to systematically enquire about the existing processes, measure their capability and determine process improvement recommendations. The DSR methodology was used to ensure such guidance is relevant, robust and well-tested. On the basis of the DSR methodology, we conducted demonstration trials at two organisations and an evaluation with two rounds of assessments within a third organisation. The evaluation of the SMPA method has enabled us to help organisations improve their processes and to report our lessons learnt to assist other organisations facing similar challenges. However, the SMPA method is challenging from a research point of view, because it is dificult to establish a ‘baseline’, i.e., to conduct repeated assessments under a constant organisational setting, or to determine the explicit impact of each assessment result towards process improvements. We evaluated the SMPA method based on the following performance measures by conducting focus groups with the relevant assessment participants:

• Usability: How usable was the SMPA method within the organisa tion? (during demonstration trials in two organisations);

Impact: How well did the SMPA method meet process improvement goals? (during evaluation over a 15-month timeframe in one orga nisation).

In DSR projects, researchers are advised to use established kernel theories to inform and justify the research work [57]. Next, the design principles that underpin the SMPA method are discussed.

## 4. Design principles of the SMPA method

Task-technology fit (TTF) theory [58] is used as the kernel theory to articulate the design principles on how the process assessment as a task, and a DSS tool as the technology, would fit together for the SMPA method. TTF theory informs the match between user task needs and available technology features to determine user performance [59]. The original TTF theory by Goodhue and Thompson [60] was associated with the technology fit for individual performance. The TTF theory from Zigurs and Buckland [58] applied the technology fit for group perfor mance in the context of group support systems. Our research problem is targeted towards processes performed by the internal IT team and the SMPA method is used for self-assessment of processes executed by the IT group within an organisation. Therefore, the group-level TTF by Zigurs and Buckland [58] was adopted in this research. The DSS tool used in the SMPA method shares similar group support technology dimensions as proposed in the theory: (a) communication support – SMPA uses an online survey for assessment data collection; (b) process structure – SMPA applies the structure of a standards-based assessment model and (c) information processing – SMPA stores a database of assessment questions, participant responses and knowledge items to compute assessment results and report recommendations.

The challenges of lack of transparency and high costs of process assessment, which have been discussed in the Introduction section, are addressed by following the design principles derived from the TTF theory. The TTF theory can be applied to determine the extent to which a technology provides features and fits the requirements of the task [61]. According to the TTF theory, to deal with the challenges of a decision task (i.e., determination of process capability and process improvements in our case) technology dimensions must focus on process structure and information processing dimensions of technology to enhance performance [58]. Using these technology dimensions from the TTF theory, we propose two design principles to exemplify the fit and to provide theoretical support for the development of the SMPA method. The meaning of ‘fit’ followed in our research is represented as ‘profile deviation’ to ascertain the level of alignment to a specific profile [52], which is represented as design principles in Table 1. To articulate the design principles as a fit profile, we mapped the identified proces assessment challenges (i.e., the task complexity dimension from the TTF theory) to the group technology dimensions from the TTF theory. The two design principles for the SMPA method are (a) Apply the Standardsbased Assessment Model, and (b) Automate Assessment Activities (see Table 1). These design principles provide sets of guidelines that reflect the accumulated knowledge needed to create a new self-assessment method to solve the problems of lack of transparency and high costs in process assessments.

## 4.1. Apply standards-based assessment model

The first design principle leads to using the international standard for process assessment to overcome the challenge of lack of transparency. Using the international standard facilitates a consistent assessment structure. A thorough review of the process reference model [44] and the process assessment model for ITSM [45] was conducted to develop the SMPA method. The process reference model defines a process in terms of its purpose and outcomes [44]. Attainment of the process purpose by meeting these outcomes demonstrates the achievement of CL1 (process performance) during the assessment. The goals for higher CLs are specified in the process attributes provided in the process assessment model of the standard.

This design principle guides the use of the Goal-Question-Metric (GQM) approach [62], which was applied to define the assessment structure in the SMPA method. A goal-oriented approach to ITSM process assessment helps to ensure that the measurement follows transparent assessment activities. The concept of GQM defines a process measurement model on three levels: goal (conceptual level), question (operational level) and metric (quantitative level) [62].

To apply the standards-based assessment model, the assessment indicators from international standards were used to develop a set of questions for all 26 processes from the ITSM standard [9]. One of the important aspects of the first design principle is the formulation of the survey questions from the assessment model. These survey questions can then be answered directly by the process stakeholders. A total of 198 specific questions for all processes at the first CL (PA1.1 in the standard) and 127 general questions at the higher CLs up to level 5 (PA2.1 to PA5.2) were derived based on 179 assessment indicators from the international standard process assessment model [45].

Every assessment question starts with the phrase: ‘Do you know if …?’ The questions seek to determine an understanding of the respondents’ knowledge regarding the operations, management, standardisation or improvement aspects of a process. The responses are measured using the scale: ‘Not’ (N), ‘Partially’ (P), ‘Largely’ (L), ‘Fully’ (F) and ‘Not Applicable’ (NA) consistent with the NPLF scale in the international standard [16].

## 4.2. Automate assessment activities

The design principle of automating assessment activities was applied by building a DSS tool to collect and analyse assessment data and provide decision support for process improvements. The high costs of the existing process assessment methods are due to time and resource requirements needed to organise process assessments. The costs are particularly high during information processing as the existing process assessment methods involve extensive one-on-one interviews with process stakeholders to collect assessment data, and manual inter pretation of such data by subject matter experts and assessors before presenting the results. The SMPA method has the potential to address this challenge because the use of a DSS tool can automate all phases of assessment activities: data collection, analysis and reporting for process improvement.

The DSS tool in the SMPA method can allocate assessment questions to the survey participants based on three process roles: process performers, process managers and external process stakeholders. The three process roles encapsulate a complete management and operational view for any ITSM process [10]. All responses from the survey questions are stored in the DSS to calculate process capability scores. The online survey collects and measures feedback from the process stakeholders using their direct responses to the questions.

Table 1  
Design Principles applied to the SMPA method (based on TTF [58]).

<table><tr><td>Task Complexity (Process Assessment Challenges)</td><td>Technology dimensions (from TTF [58])</td><td>Fit Profile (Design Principles)</td></tr><tr><td>Lack of Transparency</td><td>Process Structure</td><td>Apply Standards-based Assessment Model</td></tr><tr><td>High Costs</td><td>Information Processing</td><td>Automate Assessment Activities</td></tr></table>

The DSS tool determines a score for each process by calculating the mean value of all the responses for every process attribute. The coefficient of variation (CoV) is also computed to analyse the trustworthi ness of the process attribute score based on data dispersion among the respondents. Presentation of the reliability statistics (CoV) as part of the assessment report may assist in validation of the assessment results. It may also provide an input to prioritising and planning process im provements. In practice, the CoV in ITSM process assessments can also be useful to demonstrate inconsistent communication/skills among process teams.

On the basis of two design principles, the SMPA method is proposed next and is explained in detail later in sections 6 and 7.

## 5. A proposal for the software-mediated process assessment method

The SMPA method was developed following the design principles discussed in section 4. The method provides a structured procedure for a goal-oriented self-assessment of processes followed by an IT service provider. The SMPA method comprises four phases: process identification, process assessment, process capability measurement and process improvement. A DSS tool is used to execute the SMPA phases for selfassessments. Although we applied the concept of fit from the TTF theory [58] to develop the design principles, using the concept of fit for technology evaluation can be problematic for repeated use of the technology [63]. Therefore, the four phases are synchronised to the Plan-Do-Check-Act (PDCA) cycle [64] of the continuous improvement philosophy popularised by Deming [65]. We considered other process improvement frameworks such as business process re-engineering by Hammer and Champy [66], process innovation by Davenport [67] and Business Process Management principles by Rosemann and vom Brocke [68]. However, these frameworks are primarily developed for process improvement rather than process assessment and they do not ofer guidelines for self-assessments. The PDCA cycle, on the other hand, can define a self-assessment cycle – planning and executing the assessment, checking the results and taking action towards process improvement, which is the core principle of the widely accepted quality management systems in ISO 9001 [69]. The PDCA cycle is also highly relevant to the functioning of the SMPA method. The PDCA cycle is applied in the relevant artefacts of the SMPA method, viz. the service management system of ISO/IEC 20000 [9] and the principles of continual service improvement in ITIL [12].

Table 2 shows how the PDCA activities map to the SMPA phases and to the DSS functions that correspond to each of the phases. Diferent assessment routes are possible when using the four SMPA phases. For this reason, careful planning is required at each phase to select appropriate areas for further assessment and analysis.

The SMPA comprises four phases:

• Process Identification, where the business unit to be assessed is reviewed to identify the processes for assessment. The impact of the current business objectives and the perceptions of the relevant stakeholders are studied to determine the relative importance of the processes, enabling appropriate processes to be identified for further assessment.

• Process Assessment, where the current activities within the selected processes are assessed based on the testimony provided by the three stakeholder groups: performers, management and external stakeholders for each process. These activities are based on the assessment indicators provided by the international standard for process assessment. Assessment data are captured directly from the stake holders for further analysis.

• Process Capability Measurement, where the captured assessment data is objectively measured, based on the guidelines from the process assessment standard. A universal ‘one-size-fits-all’ process capability measurement model is adopted, with the emphasis on the consistency of the measurement approach. The determination of process capability enables identification of potential strengths and weak nesses in specific process areas.

• Process Improvement, where specific process areas are evaluated in detail, to identify areas of good practice, together with barriers and problems, and areas for possible improvements that are reported back to relevant stakeholders for action.

Based on the design principles of the SMPA method discussed in section 4 and the four SMPA phases, we next explain the components of the DSS functions that operationalise the SMPA method.

## 6. Development of the DSS functions

## 6.1. Process selection method

The process assessment standard [70] defines four key scoping dimensions to consider before the commencement of any process assessment: (a) organisation context for assessment, (b) organisation unit to be assessed, (c) highest capability level to assess and (d) processes to assess. As the first three dimensions depend on the specific organisational situation, contextual information is collected for analysis and presentation. For the fourth dimension, we developed a general method to select processes to assess and improve. The method to select critical ITSM processes follows four steps as illustrated in Table 3 and explained afterwards.

The first step in the process selection method is to determine an initial list of ITSM processes under consideration for improvement. This represents the input to the process selection method. All processes should be well established and implemented in an organisation before being considered for ongoing improvement. Diferent IT organisations may have diferent processes under consideration for improvement.

Table 2  
PDCA cycle mapped to SMPA phases and DSS functions.

<table><tr><td>PDCA Item</td><td>Plan</td><td>Do</td><td>Check</td><td>Act</td></tr><tr><td>SMPA Phase</td><td>Process Identification</td><td>Process Assessment</td><td>Process Capability Measurement</td><td>Process Improvement</td></tr><tr><td>DSS function</td><td>Process Selection Method</td><td>Online Assessment Survey</td><td>Process Attribute Rating</td><td>Assessment Report</td></tr></table>

Table 3 Process Selection Method.

<table><tr><td>Step</td><td>Activity</td></tr><tr><td>1 Determine the initial list of ITSM processes2 Select critical business drivers</td><td>Input: List all processes that are implemented in the organisation with clearly defined purposes and expected outcomes.Business value of process: Using the Balanced Scorecard [71] for the organisation, select a subset of key business drivers. Business drivers are linked to ITSM processes with a score based on their alignment. This step determines the importance of processes based on an organisation&#x27;s business objectives.</td></tr><tr><td>3 Categorise processes based on service gap perception</td><td>Perceived importance of process: Conduct a service gap perception survey of concerned stakeholders based on the SERVQUAL model [2] and present the survey findings to facilitate discussions about service gaps. Following these discussions, process stakeholders agree on categorising ITSM processes based on their need for improvement.</td></tr><tr><td>4 Produce a process selection matrix</td><td>Output: According to process scores from steps (2) and (3), a process selection matrix is presented to service managers to facilitate decision making to select processes for assessment.</td></tr></table>

Useful information for initial consideration of processes can be obtained from the process reference model for service management of the ISO/ IEC PDTS 33054 standard [44].

In the second step, the critical business drivers are determined according to the dimensions of the Balanced Scorecard [62]. The Balanced Scorecard analyses KPIs for an organisation at a strategic level from four perspectives: financial, customer, internal business and in novation and growth [62]. Critical business drivers are chosen rather than the processes directly because most managers struggle to understand their business in terms of processes [72]. Using the Balanced Scorecard ensures realisation of the intended goal-oriented approach using processes.

In the third step, perceptions of service gaps in IT service delivery across all process stakeholders are identified and presented to understand the need for improvement. To query process stakeholders in regards to their perceptions of quality service, a service gap perception instrument based on the SERVQUAL model proposed by [2] is used.

Finally, the last step presents the recommendations for processes to be selected for improvement. The choice of processes for improvement is based on their potential to meet business objectives and to address IT service gaps. This step provides organisations with evidence-based decision-making support to select important ITSM processes to assess and improve; thereby enabling them to demonstrate that a rigorous method is followed for such a selection. A detailed account of the process se lection method has previously been reported [90].

## 6.2. Online assessment survey

As shown in Fig. 1, the process assessment model for ITSM [45] provides a set of base practices to fulfil the process outcomes (CL1) and a set of generic practices for process management (CL2), standardisation (CL3), quantitative measurement (CL4) and innovation (CL5). The online survey questionnaire was designed with specific questions for each process for CL1 because this level relates to specific base practices (process dimension). There are common questions for all the processes from CL2 to CL5 because these levels relate to generic practices (capability dimension).

In a formal assessment exercise, the process attributes are rated based on the relevant assessment indicators to determine process capability. Existing ITSM process assessment frameworks were designed for assessors to use when conducting assessment interviews. The assessment indicators were not designed for direct information gathering. In the context of the SMPA method, the emphasis is to provide recommendations that can drive improvement of ITSM processes. Therefore, the assessment indicators were translated into assessment questions, which mapped one-to-one with each of the assessment indicators listed in the standard. The questions were then allocated to the three process stakeholder groups according to the relevance of each question to each process role. The procedure and design of the survey were chosen to be online as it is low cost, easily accessible, provides a fast response and data collected would be available in electronic format [73].

The use of the international standard of process assessment and its associated process models has been investigated [74] and subsequently reported in the software engineering community [75]. The previously validated process assessment model from the international standard [45] was used to develop a questionnaire for the SMPA online assessment survey. The assessment survey is supported by the process assessment model that was released as an ISO/IEC technical standard [45] and is compliant with the updated requirements for process assessment models provided by ISO/IEC 33004 [70].

Every assessment question from the survey was directly derived from the assessment indicator in the process assessment model. For example, an assessor’s question for the problem management process based on the standard base practice ‘RES.3.1 Identify problems’ could be ‘Can you tell me about recording of the problems?’ The corresponding online survey question is developed in a closed-ended format: ‘Do you know if identified problems are recorded?’ Use of a closed ended format is required for the DSS to analyse survey responses objectively. However, there is an option to provide comments in the DSS tool. A screenshot of the DSS tool is illustrated in Fig. 2.

## 6.3. Process attribute rating

The assessment questions are responded to using uniform answer options based on the NPLF scale adapted from the process assessment standard [16]. The ratings provide a metric of the knowledge of ITSM process stakeholders regarding the process capability. Besides the fourpoint NPLF rating scale, every question also has a ‘Don’t Know’ (DnK) option and a ‘Don’t understand the question’ (DnQ) option. The DnK option suggests that the survey participant understands the question but is unaware of the practice in question. The DnQ option is a metric to prompt the assessment facilitator to have a discussion about the question for clarity of the concepts. Every question also features a free text comment box to capture qualitative contextual data. Such textual information may be analysed by an assessor to validate responses. Assessors may also add specific recommendations based on comments data in the final assessment report.

Table 4 provides the rating scale defined by the process assessment standard along with the mean value of the scale percentage that was used for score calculation. Each response is transformed from the NPLF scale to a number (score). For example, if an answer option is ‘Yes, most of the time’, it corresponds to the ‘Largely’ rating score, i.e., the mean score value of 67.5. The individual response scores are averaged and transformed back to the NPLF scale for each process attribute of each process. The resultant final score is reported as the process attribute rating.

In this step, the DSS tool transforms a qualitative ordinal rating into a set of interval values using one dimensional aggregation based on arithmetic mean to obtain the process attribute rating. While a single response is based on a qualitative choice, multiple responses are aggregated following the process attribute rating method (clause 5.4) from the international standard on process measurement framework for the assessment of process capability ISO/IEC 33020 [76]. The DSS computes the mean of the ratings of interval values before rounding the result to the nearest integer, and then converting the result back to the corresponding ordinal rating. This is an accepted rating method as endorsed in ISO/IEC 33020 (see Clause 5.5.1.1 [76]).

![](/api/attachments/N6MG2TY7/fulltext/images/8bdfc24abb39fc1a42aac1ec8a8f33247f67c549ff52f1d06ae3a7d94d547d97.jpg)  
Fig. 2. A Screenshot of the DSS tool for online survey.

Table 4  
The NPLF rating scale adapted from the process assessment standard [16].

<table><tr><td>Answer Options</td><td>Rating score</td><td>Scale %</td><td>Mean score value (x)</td></tr><tr><td>No, never</td><td>N</td><td>0 - 15</td><td>7.5</td></tr><tr><td>Yes, but only sometimes</td><td>P</td><td>&gt;15 - 50</td><td>32.5</td></tr><tr><td>Yes, most of the time</td><td>L</td><td>&gt;50 - 85</td><td>67.5</td></tr><tr><td>Yes, always</td><td>F</td><td>&gt;85 - 100</td><td>92.5</td></tr></table>

The coeficient of variation (CoV) of all the responses is also com puted to determine the reliability of the process attribute score: $\mathit { C o V } _ { x } { = } \delta _ { x } / x$ where $C o V _ { x }$ is the coeficient of variation, $\delta _ { x }$ is the standard deviation and x is the mean value of x responses for all questions related to a particular process attribute. The mean and the CoV are simple statistical measures that are not explicitly suggested in the in ternational standards. These metrics are incorporated in the SMPA method to provide a general view of what the assessment participants know about the processes being assessed.

The assessment process profile includes all process attribute scores and their reliability scores. The following rule was used to determine the reliability score: CoV value of less than 30 percent as a ‘High’ reliability score, CoV value of over 50 percent as a ‘Poor’ reliability score and anything in between as a ‘Medium’ reliability score. The need to provide an explanation of the logic of process capability measurement is paramount, as one of the critical success factors for assessors and process managers was openness and transparency of how the process capability scores are derived. Lack of transparency can be a barrier to process improvement in the ITSM discipline. Assessors and process managers must be able to justify the assessment and process improvement eforts by explaining the calculations on which the process cap ability results were based. An explanation of sound logic of the process measurement is expected to lead to increased satisfaction and trust in the SMPA method. The provision of reliability scores provides confidence towards acceptance of the assessment results. The consistency and simplicity of the process measurement ensures that the SMPA method is flexible and easy to change in the event of alterations to the questions, standard measurement framework and/or measurement logic. This consideration is important in view of the recent change of the process assessment standard to the ISO/IEC 330xx series [77].

## 6.4. Assessment report

Every assessment question has a corresponding process improvement knowledge item stored in the DSS knowledge base. Each knowledge item consists of two components: observation and recommendation. The observation component stores the current state of the process in question. The recommendation component highlights process im provement guidelines from the ITIL framework that were contextualised to the question. To illustrate the development of a knowledge item, a scenario can be considered, for example if a question asks ‘Do you know if incidents are escalated as needed?’, the associated knowledge item consists of two components: Observation—‘Incident escalation is not performed as needed’; and Recommendation—‘According to ITIL, incidents must be escalated when needed as per the agreed service levels and customers should be notified to deliver responsive services’.

The DSS extracts relevant knowledge items from the knowledge base depending on the process assessment results when the normalized mean of all responses to a process attribute demonstrates risks (i.e., a final process attribute rating of Not or Partially Achieved). The corresponding knowledge items are compiled to provide process improvement guidelines. At PA1.1, the knowledge is specific to the process being assessed. From PA2.1 onwards, the knowledge comprises general guidelines that may apply to any process. However, specific examples are provided where applicable. All relevant knowledge items are compiled together in an assessment report that recommends actions for process improvement. Having explained the development of the SMPA method, next we discuss how the method is operationalised in the case organisations.

## 7. Operation of the SMPA method

When an organisation uses the SMPA method, the process assessment is executed by the DSS using four functions: process selection, online survey, process capability measurement and assessment report.

![](/api/attachments/N6MG2TY7/fulltext/images/bd2096dd807dd84b5dfb8d40886dfe9ee6041eec8ca37bb225eb8186a63780c6.jpg)  
Fig. 3. Operational Model of the SMPA method.

The operational model of the SMPA method, as illustrated in Fig. 3, demonstrates a typical application of the SMPA method using the DSS functions. The operational model is illustrated using Business Process Model and Notation (BPMN) v2.0, and a brief discussion of the model follows.

The key actors during the operation of the SMPA method are as sessment facilitator, survey participant and process manager. Activities of all three actors are supported by the DSS tool, which provides the underlying SMPA functionality and stores data associated with the assessment, survey questions, responses and knowledge items. The assessment facilitator initiates a typical SMPA workflow by inputting the organisation context and then the details of the assessment participants. Once the surveys are allocated by the facilitator to the participants, the participants can login to respond to survey questions. After assessment data collection, the facilitator sends the assessment report to the process managers to help them implement process improvements. The operation of the four DSS functions of the SMPA method is discussed in the next section.

## 7.1. Selection of processes for assessment

The assessment facilitator enters information in the DSS tool about the organisation unit to be assessed along with relevant contextual information regarding assessment. To select processes to assess, the steps illustrated in Table 3 are followed. The DSS tool provides evidencebased decision support for the managers to help them select the most relevant processes for assessment.

## 7.2. Survey of assessment questions

After determining the scope of the assessment in terms of processes and capability levels, the facilitator inputs information about the assessment participants and their process roles. The DSS tool sends an email to each participant with a link to an online questionnaire. Each questionnaire is customised to include the relevant questions for the process roles. The DSS tool collects responses to the questions that represent the stakeholder perceptions of achievement of process attributes at each CL as defined in the standard.

The assessment facilitator can monitor the completion of survey responses of all the participants and alert late respondents to encourage completion of the survey.

## 7.3. Rating of process attributes

Once all assessment data are collected, the DSS uses the standard measurement framework to rate process attributes and then calculate process attribute scores, and the reliability of the scores. These calculations are presented in the form of a process assessment profile from which the capability of each process can be determined.

## 7.4. Reporting of assessment results

A report is generated by the DSS comprising assessment results and process improvement guidelines. The report includes an assessment profile for each process. Recommendations for improvement are generated from the DSS knowledge base for every ‘at risk’ attribute, i.e., where there is partial or no achievement of process attributes. Survey comments from respondents are provided, followed by a list of names of the assessment participants. The assessment report is provided to the relevant process managers to help them decide on process and service improvement actions.

## 8. Evaluation of SMPA method

On the basis of the advice from Pefers et al. [56], two steps were followed for rigorous DSR evaluation: (1) demonstration of usability of artefact; and (2) evaluation of how well the artefact meets its goals. During the development phase the SMPA method was trialled (demonstrated) within two organisations. Several changes were made in response to these trial outcomes. The SMPA method was then subsequently applied (and evaluated) in an organisation with two rounds of assessment over a 15-month period.

An acceptable DSR evaluation strategy should consider the ‘what, how and when’ aspects of evaluation design [78]. Evaluation of the SMPA method was organised based on the widely cited DSR evaluation framework advocated by Venable et al. [78] that provides extensive evaluation design options for a DSR researcher to follow.

The SMPA method was pilot tested by five ITSM managers at a university before conducting two trial assessments and a final evaluation involving two rounds of self-assessment. In response to feedback, the survey questions were modified for clarity. Process-related examples were added to contextualize the questions while maintaining the traceability of the question to the related standard assessment in dicator.

To evaluate if the SMPA method is acceptable in an organisation, we demonstrated the usability of the SMPA method. The concept of usability as defined in the ISO/IEC 25010 software quality in use model [79] was applied to evaluate three quality characteristics of the SMPA method: efectiveness, eficiency and satisfaction. The standard’s terms were applied for the evaluation of the SMPA method as shown in Table 5. The design principles are evaluated by the first two usability characteristics: efectiveness and eficiency as listed in Table 5. The third usability characteristic of satisfaction is composed of the three sub-characteristics included in the standard [79] represented by usefulness, trust and comfort. Evaluation results are discussed in the next section.

## 8.1. Trial/Demonstration of SMPA method

The SMPA method was trialled at two Australian Public Sector IT service departments. Trial A was conducted at an internal IT department comprising 55 IT staf in a Queensland local government authority. Trial B was hosted by an external IT service provider based in Brisbane with over 1000 IT staf and customers across Australia. The DSS tool enabled assessment data collection at both sites in late 2013 Three ITSM processes were assessed at Trial A: Change Management, Problem Management, and Configuration Management. At Trial B, the three processes selected for assessment were Service Level Management, Problem Management and Configuration Management.

In Trial A, Problem Management achieved CL1 owing to its rating score of ‘Largely’ (L) at PA1.1. The other two processes were ‘Partially’ (P) at PA1.1 indicating CL0. The majority of the rating scores for all processes demonstrated weak reliability (six ‘Poor’, 18 ‘Medium’ and only three ‘High’ reliability scores). This meant that survey respondents were not consistent in their answers and responses were varied. Moreover, most of the rating scores were ‘Partially’ (P). There were two ‘Largely’ (L), only a single ‘Not’ (N) and none of the rating scores achieved ‘Fully’ (F) for any of the process attributes. The Trial A process assessment profile is provided as Table A1 in Appendix A.

In Trial B, all assessed processes achieved process attribute scores of ‘Largely’ (L) at PA1.1, resulting in CL1. Almost all of the rating scores for all processes in Trial B demonstrated strong reliability (18 ‘High’, two ‘Medium’ and only one ‘Poor’ reliability score). This means that survey respondents were consistent in their answers. Moreover, most of the rating scores were ‘Largely (L)’. There were two ‘Partially’ (P) and only a single ‘Fully’ (F) rating score. The results demonstrate consistently superior process capability for Trial B in comparison with Tria A. The Trial B process assessment profile is provided as Table A2 in Appendix A.

We organised focus groups for Trial A (9 participants) and Trial B (11 participants) to evaluate the usability of the SMPA method. The participants of each focus group represented the three process roles: managers, performers and external process stakeholders. The focus group facilitator encouraged all participants to discuss the positive and negative aspects of the SMPA method across each usability characteristic. The participant discussions surrounding their experience of the SMPA method were recorded and later transcribed to enable qualitative data analysis. The evaluation data were analysed by reviewing focus group discussion transcripts for supporting and opposing comments related to the three usability characteristics presented in Table 5.

A summary of the evaluation results from qualitative analysis of focus group discussions is provided as Table 6.

Considering the usability characteristics for the SMPA method, the majority of participants found the online survey easy to use and trustworthy, and largely agreed that a self-assessment experience answering direct questions made the exercise more transparent and less costly to implement than a manual assessment. However, concerns were raised about the usefulness of the process assessment questions in terms of representation and relevance.

During both trials, the facilitator solicited ideal solutions that could address the negative comments on the usability characteristics, particularly the concerns on the usefulness of the SMPA method. A consensus was reached where a tiered method was recommended, wherein the SMPA method could be used initially to obtain an overall understanding of process capabilities. Afterwards, to engage in process improvement, human judgment was considered necessary for assessment validation and process improvement recommendations. A fully automated process assessment, which is strictly standards-driven was considered to be of less value. Further clarification of the survey questions with relevant examples were suggested by participants to make the SMPA method more useful.

## 8.2. Application of SMPA method

This section describes the first real-world use of the SMPA method. During IT adoption, companies face challenges that are not only related to technology but are organisational in nature [80]. Therefore, we evaluated the SMPA method in a real-world organisational setting, that is, within the IT services group of a global financial services company, referred to as Company X. After the initial assessments using the SMPA method, the process improvement recommendations were incorporated within the ITSM improvement plans, and such plans were executed for one year before undertaking a second round of assessment. A comprehensive evaluation of the SMPA method requires an assessment of the overall impact of the improved processes. In the past, assessments of process improvement from organisational change have been conducted based on process metrics such as resource utilisation, cycle time, cost reduction and process bottlenecks [31]. Similarly, the impact of SMPA

## Table 5

Usability characteristics for artefact evaluation (based on ISO/IEC 25010 [79]).

<table><tr><td>Design Principle</td><td>Usability Characteristic</td><td>Definition from International Standard (ISO/IEC 25010)</td></tr><tr><td>Apply Standards-based Assessment Model</td><td>Effectiveness</td><td>Accuracy and completeness with which users achieve specified goals.</td></tr><tr><td>Automate Assessment Activities</td><td>Efficiency</td><td>Resources expended in relation to the accuracy and completeness with which users achieve goals.</td></tr><tr><td>N/A</td><td>Satisfaction</td><td>Degree to which user needs are satisfied when a product or system is used in a specified context of use. (Note: sub-characteristics of satisfaction used in this research are: usefulness, trust and comfort)</td></tr></table>

Table 6  
Summary of evaluation results at Trial A & B.

<table><tr><td rowspan="2">Usability characteristic</td><td colspan="2">No. of key comments</td><td rowspan="2">Selected representative comments</td></tr><tr><td>Trial A</td><td>Trial B</td></tr><tr><td rowspan="8">Effectiveness</td><td>☑ x 14</td><td>☑ x 19</td><td>☑</td></tr><tr><td>☒ x 4</td><td>☒ x 13</td><td>• ‘bigger data set – more reliable data’</td></tr><tr><td>◎ x 2</td><td>◎ x 2</td><td>• ‘more consistent and you were answering a series of questions accurately’</td></tr><tr><td></td><td></td><td>• ‘better understanding of views from various areas of the business’</td></tr><tr><td></td><td></td><td>• ‘more democratic and transparent’</td></tr><tr><td></td><td></td><td>☒</td></tr><tr><td></td><td></td><td>• ‘some of those examples were slightly irrelevant’</td></tr><tr><td></td><td></td><td>• ‘probably not a depth that we go to’</td></tr><tr><td rowspan="4">Efficiency</td><td>☑ x 6</td><td>☑ x 5</td><td>☑</td></tr><tr><td></td><td>☒ x 1</td><td>• ‘the advantage of giving you a really wide data set’</td></tr><tr><td></td><td></td><td>• ‘faster and accurate approach’</td></tr><tr><td></td><td></td><td>• ‘you don’t have to have them in a room’</td></tr><tr><td rowspan="9">Satisfaction</td><td>☒ x 16</td><td>☒ x 31</td><td>☒</td></tr><tr><td>☑ x 13</td><td>☑ x 23</td><td>• ‘some of the questions are quite confusing and ambiguous’</td></tr><tr><td>◎ x 1</td><td></td><td>• ‘meant different things, to different people’</td></tr><tr><td></td><td></td><td>• ‘too repetitive and asking the same question in many different ways’</td></tr><tr><td></td><td></td><td>☑</td></tr><tr><td></td><td></td><td>• ‘the questions are structured well’</td></tr><tr><td></td><td></td><td>• ‘The logic seems valid and reliable’</td></tr><tr><td></td><td></td><td>• ‘easy enough to use’</td></tr><tr><td></td><td></td><td>• ‘you could do it when you wanted’</td></tr></table>

☑ indicates that the usability characteristic was strongly supported in a comment.  
indicates that the usability characteristic was not clear or a neutral position was taken.  
☒ indicates that the usability characteristic was strongly opposed in a comment.

method, i.e., process improvement, was evaluated in our research based on the trend analysis of the process activities over a one-year timeline at Company X. The timing of the assessment was an important factor contributing to the success of the assessment within Company X, which was at that time undertaking a major process improvement initiative supported by the senior management. The culture in Company X was conducive to this type of survey-based assessment and an internal assessment ‘champion’ provided support.

## 8.2.1. Assessment scope

The four key scoping areas were considered by Company X before the process assessment commenced: (a) organisation context for assessment, (b) organisation unit to be assessed, (c) highest capability level to assess and (d) processes to assess.

a) Organisational context for assessment: Company X has over 200 employees, headquartered in North America, with ofices in various global locations. Company X is a managed service provider of online trading and liquidity aggregation systems to the foreign exchange market. Company X's on-demand cloud-based solutions aim to provide financial institutions with operational eficiencies and the ability to flexibly enter new markets quickly and to scale eficiently without owning and operating any IT infrastructure of their own. Company X ofers an array of IT services to over 1000 financial institutions that operate 24 h per day for 5 days per week. Company X is a representative case of an IT service provider with a desire to improve and enhance its IT services based on the ITIL framework.

b) Organisational unit to be assessed: Company X has about 70 IT staf who attend to incidents, problems and changes on a daily basis. The IT staf spans five organisational units: business support, opera tions, engineering, execution services, and trading solutions. The target groups were purposefully sampled as they cover the business and IT function at Company X and are involved in all ITSM processes.

c) Highest capability level to assess: Company X had recently implemented formal ITSM processes and it decided to assess up to capability level 3 (CL3) and considered assessment of higher process capability would be irrelevant.

d) Processes selected for assessment: Company X selected incident management, problem management and change management as processes to assess, as these processes are directly linked to their business goals.

## 8.2.2. Baseline assessment

The first process capability assessment using the SMPA method was performed in late 2015. A total of 67 key employees were identified by the process managers at Company X as participants for the assessment.

All three processes achieved CL1 owing to their attribute rating scores of ‘Largely’ (L) at PA1.1. Incident and change management process attributes were largely achieved at CL2 and CL3 as well. In contrast, problem management process attributes were only partially achieved at CL2 and CL3. Survey respondents predominantly agreed on their ratings as the majority of the rating scores demonstrated strong reliability (13 ‘High’; one ‘Medium’ and one ‘Poor’). Company X’s baseline process assessment profile is provided as Table A3 in Appendix A. Across the three processes, a total of 57 process improvement recommendations were generated by the DSS tool where process risks were determined, i.e. where process attribute rating scores are ‘partially’ or ‘poor’.

## 8.2.3. Process improvement

Using the assessment report generated by the SMPA method from the baseline assessment, Company X developed an annual process improvement plan that was scheduled for progressive execution during 2016. A major ITSM improvement project was executed to implement process improvements using ITIL guidelines and was based on the recommendations provided by the baseline assessment report.

## 8.2.4. Checkpoint assessment

The second process capability assessment using the SMPA method was performed in late 2016 with 64 participants from the same five business units as in the baseline assessment (about 90% of survey respondents were the same as the first assessment). All three processes remained at CL1. The problem management process showed improvement and largely achieved all five attributes. The reliability of responses also increased marginally (14 ‘High’; one ‘Poor’ reliability score). Company X’s checkpoint process assessment profile is provided as Table A4 in Appendix A. Across the three processes, a total of 11 process improvement recommendations were generated by the DSS tool where process risks were determined, i.e., where process attribute rating scores are ‘partially’ or ‘poor’.

Table 7  
Summary of evaluation results at Company X.

<table><tr><td>Usability characteristic</td><td>No. of key comments</td><td>Selected representative comments</td></tr><tr><td rowspan="3">Effectiveness</td><td>☑ x 13</td><td>☑</td></tr><tr><td rowspan="2">☒ x 1</td><td>• ‘the survey covered a wide range of business areas’</td></tr><tr><td>• ‘interviewer biases were avoided’</td></tr><tr><td rowspan="3">Efficiency</td><td rowspan="3">☑ x 14</td><td>☑</td></tr><tr><td>• ‘most of the questions were very explanatory’</td></tr><tr><td>• ‘single choice questions made life easier for us’</td></tr><tr><td rowspan="11">Satisfaction</td><td>☑ x 39</td><td>☑</td></tr><tr><td>☒ x 2</td><td>• ‘speed of response’</td></tr><tr><td rowspan="9">☒ x 1</td><td>• ‘the examples were relevant and useful’</td></tr><tr><td>• ‘the results seem trustworthy as the computer calculated the results’</td></tr><tr><td>• ‘interviewer biases were avoided’</td></tr><tr><td>• ‘it saved the progress and whenever you came back you could continue from where you left off’</td></tr><tr><td>• ‘I could even answer some of the questions from home’</td></tr><tr><td>☒</td></tr><tr><td>• ‘although the structure of the questions was well organised, I felt that there was repetition’</td></tr><tr><td>☒</td></tr><tr><td>• ‘for levels 2 and 3, the report does not show us the areas we are doing well in’</td></tr></table>

☑ indicates that the usability characteristic was strongly supported in a comment.  
◉ indicates that the usability characteristic was not clear or a neutral position was taken.  
☒ indicates that the usability characteristic was strongly opposed in a comment.

# Incidents per million transactions  
![](/api/attachments/N6MG2TY7/fulltext/images/00b3601b00f270b436fccfd748d5a30e696815dc1e52873e197b5392e0592eb2.jpg)  
# Changes per million transactions

![](/api/attachments/N6MG2TY7/fulltext/images/523abba30aff7294e57b18605edc37c87acd2f617cff12cd8c4820ae7a94453d.jpg)

<table><tr><td></td><td>May-15</td><td>Jun-15</td><td>Jul-15</td><td>May-16</td><td>Jun-16</td><td>Jul-16</td></tr><tr><td># Incidents</td><td>1,899</td><td>2,495</td><td>1,831</td><td>1,351</td><td>968</td><td>1,185</td></tr><tr><td># Changes</td><td>595</td><td>745</td><td>743</td><td>534</td><td>358</td><td>486</td></tr><tr><td># Trades</td><td>6,500,226</td><td>7,862,355</td><td>7,170,050</td><td>6,399,613</td><td>9,005,845</td><td>8,262,355</td></tr></table>

Fig. 4. Incidents and changes per million transactions for a 3-month period in 2015 and 2016 at Company X.

## 8.2.5. Assessment evaluation

After each round of assessment, a focus group workshop was held to evaluate the SMPA method and consider the process capability assessment report results for process improvement. The focus groups included process managers and a cross-section of senior managers. An evaluation of the SMPA method was conducted using the same five criteria applied during the trials (as explained in Table 5). The assessment results were reviewed and the comments provided by participants in the surveys

were discussed.

Table 7 shows the combined results from both focus groups of evaluation of the SMPA method at Company X.

In the first evaluation, there were a few comments that strongly opposed the usability characteristic of the SMPA method; however, after changes were made to the SMPA method (for example, the addi tion of relevant examples to better describe the questions), the overall sentiment of the SMPA method was that it was accurate, useful and easy to use during the second evaluation.

## 8.2.6. Impact of SMPA method at company X

An annual comparison of survey results did not show an improvement in capability levels for any of the three processes, however, deeper analysis revealed a reduction in the number of recommendations generated by the DSS tool, indicating progress in capability achievement at a more granular level.

A historical trend analysis of trading volumes at Company X showed that global events cause higher trading volumes that are directly associated with higher numbers of incidents, problems and changes. Between the two assessments, one important event, Brexit, occurred. ‘Brexit’ refers to the decision of the Government of the United Kingdom (UK) to leave the European Union (EU) as a result of a referendum held on 23 June 2016 [81]. This event caused unpredictable market volatility that translated into exceptionally high foreign exchange trading volumes. In fact, Company X’s highest daily trading volume to date coincided with Brexit. The British Pound (GBP) started to weaken as poll numbers were released from individual areas throughout the day. This marked the lowest the pound had traded at since 1985. Globally foreign exchange trading volumes jumped to record highs in June 2016. Although this event caused peak trading volumes, Company X sufered minimal service disruptions and the executive staf attributed this positive situation to the actions taken to address recommendations provided by the SMPA method. Fig. 4 charts the number of incidents and changes per million transactions for the 3-month periods, May through July of 2015 and 2016. These measures can be used for the comparison of the number of incidents and changes over the two time periods while taking into account the dependency of incidents and changes on the number of trading transactions.

Fig. 4 highlights the process performance improvements during the period of May – July 2016 in comparison with the same period in 2015 despite a peak in the number of transactions in 2016. As Fig. 4 shows, the proportion of incidents and changes to transactions has decreased in each of the three months in 2016 compared to the respective months in 2015. In addition, the upward overall trend of incidents and changes in 2015 has changed to a downward overall trend in 2016.

Fig. 4 demonstrates that the SMPA method could have potentially played a role in the improvement of performance metrics (reduced number of incidents and changes) that occurred in Company X. There was a sudden spike in the number of trading transactions due to the Brexit event in June 2016 but this did not appear to influence the number of ITSM incidents and changes. In fact, the lowest number of incidents and changes were recorded in June 2016. Moreover, the executives at Company X confirmed that the process improvements un dertaken, based on the SMPA report, were the only substantial changes made to their ITSM practices [82] and they supported the view that the SMPA method helped improve ITSM processes as reported in favourable process performance metrics. Nevertheless, in the absence of statistically valid and reliable evidence, causality cannot be asserted. Next, we discuss major issues that emerged from the reflections on our research.

## 9. Discussion

In this section, we discuss three major issues that emerged from our research during the development, evaluation and application of the SMPA method. These issues emerged from an analysis of the feedback from the evaluation and discussions with researchers and ITSM practitioners regarding the SMPA method.

## 9.1. Use of staged capability maturity models for improvement

Staged Capability Maturity Models have undoubtedly played a key role in the process improvement projects in a variety of fields including risk management, information technology, resource management, project management and software engineering [83]. In particular, the CMMI model is widely known in the IT industry and used by clients to select software vendors and by vendors to attract more clients.

Recognising that staged models are useful in audits to assure a level of process quality for vendor selection, the issue we raise is the usefulness of staged models for process improvement. To date, there is little theoretical support for process improvement based on staged models. Recently, concerns have been raised that staged maturity models fail to enable organisation-wide continuous process improvement [84]. In particular, in relation to small and medium enterprises, it has been suggested (by [85]) that the widely used CMMI and international standard for process assessment have shortcomings. Alternative process improvement approaches such as defined process target profiles, reference models and modelling may produce better results.

The feedback from the SMPA trials and evaluation indicated that all assessment facilitators were interested to find out the capability level of each assessed process. In many cases, the facilitator’s response to the resulting capability level was one of disappointment as the level was less than anticipated. In total, four ITSM processes during the trials and three ITSM processes at Company X were calculated as CL1 ‘defined’, whereas two ITSM processes during the trials were calculated as CL0 ‘ad hoc’. On the other hand, the facilitators concurred with the process attribute ratings but commented that the poor results could have been owing to surveyed staf being unaware of the details of the assessed processes.

It is recognised that maturity dimensions should be grounded in both scientific and practical relevance [43]. However, our research results challenge the underlying assumption that higher levels of process capability depend on the achievement of lower level process attributes. For example, the Trial B profile (Table A2 in Appendix A) rated configuration management process as CL1 despite six of the seven process attributes being largely achieved and the remaining process attribute (at Level 4) being fully achieved. The practitioners reported that it was not informative to represent the assessment result as a single CL integer on a scale of zero to five. In fact, they found the more granular representation of profiles meaningful when the achievement of each process attribute was reported on the four point scale NPLF. We argue for granular process attributes to be presented in detail to report process improvement rather than the maturity path in terms of capability levels. It is interesting to note that the revised version of the process assessment standard (ISO/IEC 33020 [86]) provides greater granularity with an option to report the achievement of attributes on a six point scale: N, P-, P+, L-, L + and F. In this light, although the new standard still reports capability levels, it promises to provide more granular feedback to practitioners. Our research supports this action and provides empirical evidence to support the use of process attributes as a suitable metric for assessments that aim for process improvement.

## 9.2. Challenges of automating process capability assessments

Although our SMPA method achieved its goal of automating ITSM process assessments in a more transparent and cost-efective manner as compared to manual assessments, there were several challenges of automating process capability assessments during our experience of the trials and application of the SMPA method. The key challenges discovered during the SMPA experience are highlighted in the next section.

A complete automation of process assessment is problematic in terms of understandability of the online survey-based questionnaires. For example, the meaning of words such as incident vs problem, together with qualitative measures of process quality and efectiveness, generated considerable debate that was observed during the evaluation of focus groups. This dialogue was useful, but more accurate definitions of terms would be helpful. During the evaluation, most participants mentioned that they were not familiar with some of the language and terminology used in the assessment questions. Because the assessment survey is online, the participants cannot easily ask an assessment facilitator for guidance. In terms of survey responses, although comments were sought for every question, the number of responses with comments was very low. Therefore, we acknowledge that people answering the questions using an automated process assessment method such as the SMPA method, may overlook context-related information cues in terms of organisational dynamics, culture and politics within the assessment environment. This is true for any quantitative assessment (survey method) vs. qualitative assessment (interview method) in general, and a complementary use of both types of assessments may portray a more valid result [87]. However, such combined assessment exercises are resource-intensive for companies. Hence, the value of SMPA method for transparent and cost-efective assessments can be established.

The way the rating scale (i.e., NPLF) from the process assessment standard was applied to determine the process scores may have resulted in an underestimation of the assessment results. The strictness of the SMPA scoring technique to rate the Fully (> 85%) and the Not (< 15%) meant most of the results fell towards the Partially or Largely range (15% to 85%), thereby resulting in a Yes-and-No type of response. Consequently, the process capability scores during all assessments failed to achieve CL2 because of the fact that it was practically impossible to achieve Fully in CL1. There is a lot of ‘noise’ in the automated assessment data with regards to the number of questions and the number of participants, the issue of lack of understanding of the question, lack of weighting on the questions and responses, and the fact that the Don’t Know and Don’t understand the Question metrics, although acknowledged as very critical metrics were ignored for process capability measurement. These challenges do not emerge from the use of the SMPA method, per se, but based on the design decisions made about how the scoring scale was applied (Table 4) by the DSS tool. The experienced assessors involved in the research team expressed their opinion that a manual assessment based on the same standards would have returned higher CL scores. A sensitivity analysis of existing assessment data about scoring could shed some light. This was beyond our research scope but an important area for future research.

Finally, the current SMPA method assumes that all responses in a survey are of equal value, that is, regardless of the role of a respondent (and their level of expertise) all views are treated the same. This is the so-called frequentist approach to data and statistical treatment of such data. The probability of an outcome is not assumed to be influenced by prior knowledge, such as, for example, who responded. An alternative approach to statistical analysis of data is a Bayesian approach (e.g. [88]) where a priori knowledge is valued and used in formulating the probability of an outcome. In the example of treatment of data collected and analysed in the SMPA method, Bayesian statistics could take account of the roles of the respondents and their level of expertise. This may not only produce results more in line with expectations of the organisations but might also better reflect the analyses of external consultants (who typically are highly skilled and knowledgeable about the processes in use).

## 9.3. Limited transparency in the assessment report

The application of a standards-based assessment model was the first design principle for the development of the SMPA method in response to the challenge of lack of transparency in manual process assessments. The use of the international standard for process assessment and relevant process models as discussed in section 4.1 provided a muchneeded rationale to demonstrate transparency. Consequently, the notion of transparency is apparent in the assessment structure and assessment instruments (assessment questions in online survey, measurement framework and knowledge base). During the SMPA trials and application, this level of transparency was endorsed by the relevant stakeholders.

The process assessment profiles that are presented in the assessment report (see Appendix A) could be tainted from individual over- or under-confidence and group think. In defence of the design of the SMPA method, we can argue that no assessments are immune from this challenge. However, the SMPA method could have used its DSS analytics capability with an ability to drill down and report assessment results by diferent stakeholder groups that would enable the audience of the report to better respond to such inconsistencies. Focus group participants highlighted a number of other shortcomings of the assessment report, in particular, the fact that the capability levels were not explicitly stated in the report. Even though in section 9.1, we argue the relative futility of capability levels in comparison to process attributes, the international standard for process assessment mandates reporting of the capability levels. In this light, there is opportunity to further improve the assessment report.

Another specific challenge was the readability and applicability of the assessment report. During the SMPA evaluation focus group sessions, we gathered evidence of lack of clarity of how the report was presented. Guidance by the assessment facilitator and the researchers was required for the intended audience of the assessment report (process managers) to understand the reports. The assessment reports, albeit compiling improvement recommendations from the ITIL framework, failed to provide a clear and transparent roadmap to demonstrate how to improve processes.

A number of suggestions to address these challenges were discussed with the research participants. Pertinent areas of improvement are the use of advanced data analytics and visualisation features in the DSS tool to provide interactive reporting features with graphical representation of ideal process flows and a capability to drill down into the results from the organisation level to group to individual responses. In comparing the benchmark and checkpoint assessment results, the assessment facilitator at Company X noted the decrease in the number of improvement recommendation items, suggesting lower process risks, even though the process capability level remained unchanged. The assessment results are currently based on the quantitative evaluation of survey responses. Another consideration is to include some rationalisation of the assessments using qualitative interpretation of process capability, together with tailored guidance for process improvements.

Therefore, the transparency design principle of the SMPA method could only be partly applied in the assessment report. The process attribute rating reported was based on the established assessment scales and guidelines provided by the international standards. Guidelines from the ITIL framework were used to provide recommendations for process improvement in the report. However, the proprietary tool that produced the assessment report did not follow any standard design or template. This issue of limited transparency of the SMPA assessment report has not been addressed in our current research and is a future research consideration. As a result, the strong level of transparency in the assessment instruments and structure did not fully transfer through to the end of the assessment journey – the assessment report for process improvement.

## 10. Conclusions

The research problem we focused on was the lack of transparency and high costs of conducting consistent and repeatable process assessments in IT organisations. Using a DSR approach to address the problem, the SMPA method was developed to assist organisations to selfassess their processes for improvement. The method consists of four phases: process identification, process assessment, process capability measurement and process improvement. The SMPA method incorporates a DSS tool that has four main functions: process selection method, online assessment survey, process attribute rating and assessment report. The SMPA method was designed for transparent assessment to support continual improvement of IT services. Evaluation trials were conducted at two IT service providers to determine the usability of the SMPA method. Participants reported that overall they found the online survey for assessment trustworthy and efective. The SMPA method was usable in the context of the trial organisations, although the trials revealed that some improvements were suggested to enhance the usability of the SMPA method. We addressed the usability concerns and the SMPA method was subsequently applied within a high‐volume foreign exchange trading business with two rounds of assessments in one year of an ITSM process improvement project.

The key benefit of the SMPA method is that it can be used to measure the process capabilities that contribute to ITSM in an organisation, allowing overall management and improvement of ITSM processes. With the current evolution of the process assessment standard to the new ISO/IEC 330xx family [77], modification of the survey questions and the knowledge base to reflect new process capability assessment models will be required – a future research consideration; how ever, the changes will not afect the SMPA phases as they are well grounded on the design principles based on the task-technology fit theory [58].

The SMPA method provides a new opportunity for automation and transparency in the way process assessments are conducted. Beyond the discipline of ITSM, the SMPA method can potentially be applicable to other domains where a process assessment model is available. Using the SMPA method, a compliant process assessment model can be used to develop survey questions. Likewise, process improvement recommendations can be generated based on industry best practice guidelines such as ITIL in our case. With the expanding value and reach of the process assessment standard and the new ISO/IEC 330xx series, the SMPA method is applicable to process assessments in any processbased management system. It is anticipated that the SMPA method can be generalisable, i.e., applicable to diferent organisations, owing to the generic nature of the four-phase SMPA method. The range of cases covered during the trials and application of the SMPA method supports this claim. However, the general applicability of the SMPA method would require comprehensive facilitator guidance, combined with the support of an internal champion. This is of particular importance when the goal-oriented nature of the SMPA structure is considered.

We also report the research limitations in terms of the challenges in automating process capability assessments and shortcomings of the assessment report that could be addressed in future research. The SMPA method requires respondents to answer assessment questions based on the process indicators from the process assessment model. A limitation of this method is that some respondents might have unrealistic perceptions about their process activities. A more rigorous ITSM process assessment method would involve the review of process input and output documents (work products) as instructed in the international standard. Another limitation of this research is that the evaluation of the SMPA method was limited to three sites.

As a theoretical contribution, after eight years of research in the area of ITSM process assessments, we found that assessment results based on the staged maturity model may not be representative of the capability of assessed processes. Our empirical evidence challenges the underlying assumption that higher levels of process capability depend on the full achievement of lower level process attributes. Rather than

## Appendix A. Process Assessment Profiles

representing the assessment results on a scale of zero to five, a more granular representation of assessment results was meaningful and useful for practitioners. We advocate for the use of process attributes as a suitable metric for process assessments, particularly to report process improvements.

As a contribution to research methodology, this research demon strated the use of the international standards as a design principle in a DSR project. Three international standards in the areas of process assessment, ITSM, and System and Software Quality were used to corroborate artefact development and evaluation in our DSR project. Our DSR project is an exemplar demonstrating that with the use of international standards, concerns about the quality of artefacts can be addressed and thereby the utility of the artefact can be verified.

As a contribution to practice, the SMPA method demonstrated positive impacts in terms of benefits to the participating organisations and ongoing improvements to the method. We conclude that the SMPA method can help ITSM practitioners to transparently self-assess their processes for improvement. The SMPA method is not intended to replace a formal conformity assessment. However, it is expected that organisations could use this method when the focus is to monitor process improvements using process attributes rather than to strictly audit for capability levels. We also argue for the relevance of the SMPA method to assessors in a formal appraisal environment as one of the evidence sources to determine process capability or investigate granular process attributes for improvement.

Note. ITIL® is a Registered Trade Mark of AXELOS Limited.

## Funding

This work was supported by an Australian Research Council in dustry linkage project [grant number LP100200227].

## Declaration of Competing Interest

None.

## Acknowledgements

We thank Mr. Paul Collins, Chief Executive Oficer of Assessment Portal Pty Ltd. for his involvement and support in providing the platform to implement the DSS tool for the SMPA method. We also ap preciate the staf at the three organisations who were involved during the evaluation of the SMPA method. Finally, we thank the anonymous reviewers and ITSM practitioners who provided us valuable input during the presentation of our preliminary research work in academic outlets and industry conferences.

Table A1  
Trial A Process Assessment Profile.

<table><tr><td></td><td>Level 1</td><td colspan="2">Level 2</td><td colspan="2">Level 3</td><td colspan="2">Level 4</td><td colspan="2">Level 5</td></tr><tr><td>Profile</td><td>PA1.1</td><td>PA2.1</td><td>PA2.2</td><td>PA3.1</td><td>PA3.2</td><td>PA4.1</td><td>PA4.2</td><td>PA5.1</td><td>PA5.2</td></tr><tr><td colspan="10">PROBLEM MANAGEMENT- 10 responses - Capability Level 1</td></tr><tr><td>Process attribute</td><td>L</td><td>P</td><td>P</td><td>P</td><td>P</td><td>P</td><td>N</td><td>P</td><td>P</td></tr><tr><td>Reliability</td><td>HIGH</td><td>MED</td><td>POOR</td><td>POOR</td><td>MED</td><td>MED</td><td>MED</td><td>MED</td><td>MED</td></tr><tr><td colspan="10">CHANGE MANAGEMENT - 9 responses - Capability Level 0</td></tr><tr><td>Process attribute</td><td>P</td><td>P</td><td>P</td><td>P</td><td>L</td><td>P</td><td>P</td><td>P</td><td>P</td></tr><tr><td>Reliability</td><td>MED</td><td>MED</td><td>MED</td><td>POOR</td><td>HIGH</td><td>MED</td><td>MED</td><td>MED</td><td>MED</td></tr><tr><td colspan="10">CONFIGURATION MANAGEMENT - 9 responses - Capability Level 0</td></tr><tr><td>Process attribute</td><td>P</td><td>P</td><td>P</td><td>P</td><td>P</td><td>P</td><td>P</td><td>P</td><td>P</td></tr><tr><td>Reliability</td><td>POOR</td><td>MED</td><td>POOR</td><td>POOR</td><td>HIGH</td><td>MED</td><td>MED</td><td>MED</td><td>MED</td></tr></table>

Table A2  
Trial B Process Assessment Profile.

<table><tr><td></td><td>Level 1</td><td colspan="2">Level 2</td><td colspan="2">Level 3</td><td colspan="2">Level 4</td><td colspan="2">Level 5</td></tr><tr><td>Profile</td><td>PA1.1</td><td>PA2.1</td><td>PA2.2</td><td>PA3.1</td><td>PA3.2</td><td>PA4.1</td><td>PA4.2</td><td>PA5.1</td><td>PA5.2</td></tr><tr><td colspan="10">PROBLEM MANAGEMENT – 4 responses - Capability Level 1</td></tr><tr><td>Process attribute</td><td>L</td><td>L</td><td>L</td><td>L</td><td>L</td><td>L</td><td>P</td><td></td><td></td></tr><tr><td>Reliability</td><td>HIGH</td><td>HIGH</td><td>HIGH</td><td>HIGH</td><td>HIGH</td><td>HIGH</td><td>POOR</td><td></td><td></td></tr><tr><td colspan="10">SERVICE LEVEL MANAGEMENT – 5 responses - Capability Level 1</td></tr><tr><td>Process attribute</td><td>L</td><td>L</td><td>L</td><td>L</td><td>L</td><td>P</td><td>L</td><td></td><td></td></tr><tr><td>Reliability</td><td>HIGH</td><td>HIGH</td><td>HIGH</td><td>HIGH</td><td>HIGH</td><td>MED</td><td>HIGH</td><td></td><td></td></tr><tr><td colspan="10">CONFIGURATION MANAGEMENT – 5 responses - Capability Level 1</td></tr><tr><td>Process attribute</td><td>L</td><td>L</td><td>L</td><td>L</td><td>L</td><td>L</td><td>F</td><td></td><td></td></tr><tr><td>Reliability</td><td>HIGH</td><td>HIGH</td><td>HIGH</td><td>HIGH</td><td>HIGH</td><td>HIGH</td><td>HIGH</td><td></td><td></td></tr></table>

Table A3  
Company X Baseline Process Assessment Profile.

<table><tr><td></td><td>Level 1</td><td colspan="2">Level 2</td><td colspan="2">Level 3</td><td colspan="2">Level 4</td><td colspan="2">Level 5</td></tr><tr><td>Profile</td><td>PA1.1</td><td>PA2.1</td><td>PA2.2</td><td>PA3.1</td><td>PA3.2</td><td>PA4.1</td><td>PA4.2</td><td>PA5.1</td><td>PA5.2</td></tr><tr><td colspan="10">PROBLEM MANAGEMENT - 21 responses - Capability Level 1</td></tr><tr><td>Process attribute</td><td>L</td><td>P</td><td>P</td><td>P</td><td>P</td><td></td><td></td><td></td><td></td></tr><tr><td>Reliability</td><td>HIGH</td><td>POOR</td><td>HIGH</td><td>HIGH</td><td>MED</td><td></td><td></td><td></td><td></td></tr><tr><td>Recommendations</td><td>1</td><td>9</td><td>8</td><td>9</td><td>5</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="10">CHANGE MANAGEMENT - 45 responses - Capability Level 1</td></tr><tr><td>Process attribute</td><td>L</td><td>L</td><td>L</td><td>L</td><td>L</td><td></td><td></td><td></td><td></td></tr><tr><td>Reliability</td><td>HIGH</td><td>HIGH</td><td>HIGH</td><td>HIGH</td><td>POOR</td><td></td><td></td><td></td><td></td></tr><tr><td>Recommendations</td><td>1</td><td>3</td><td>3</td><td>3</td><td>3</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="10">INCIDENT MANAGEMENT - 26 responses - Capability Level 1</td></tr><tr><td>Process attribute</td><td>L</td><td>L</td><td>L</td><td>L</td><td>L</td><td></td><td></td><td></td><td></td></tr><tr><td>Reliability</td><td>HIGH</td><td>HIGH</td><td>HIGH</td><td>HIGH</td><td>HIGH</td><td></td><td></td><td></td><td></td></tr><tr><td>Recommendations</td><td>1</td><td>3</td><td>0</td><td>2</td><td>2</td><td></td><td></td><td></td><td></td></tr></table>

Table A4  
Company X Checkpoint Process Assessment Profile.

<table><tr><td></td><td>Level 1</td><td colspan="2">Level 2</td><td colspan="2">Level 3</td><td colspan="2">Level 4</td><td colspan="2">Level 5</td></tr><tr><td>Profile</td><td>PA1.1</td><td>PA2.1</td><td>PA2.2</td><td>PA3.1</td><td>PA3.2</td><td>PA4.1</td><td>PA4.2</td><td>PA5.1</td><td>PA5.2</td></tr><tr><td colspan="10">PROBLEM MANAGEMENT - 27 responses - Capability Level 1</td></tr><tr><td>Process attribute</td><td>L</td><td>L</td><td>L</td><td>L</td><td>L</td><td></td><td></td><td></td><td></td></tr><tr><td>Reliability</td><td>HIGH</td><td>POOR</td><td>HIGH</td><td>HIGH</td><td>POOR</td><td></td><td></td><td></td><td></td></tr><tr><td>Recommendations</td><td>1</td><td>0</td><td>0</td><td>4</td><td>3</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="10">CHANGE MANAGEMENT - 46 responses - Capability Level 1</td></tr><tr><td>Process attribute</td><td>L</td><td>L</td><td>L</td><td>L</td><td>L</td><td></td><td></td><td></td><td></td></tr><tr><td>Reliability</td><td>HIGH</td><td>HIGH</td><td>HIGH</td><td>HIGH</td><td>HIGH</td><td></td><td></td><td></td><td></td></tr><tr><td>Recommendations</td><td>0</td><td>0</td><td>2</td><td>1</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="10">INCIDENT MANAGEMENT - 29 responses - Capability Level 1</td></tr><tr><td>Process attribute</td><td>L</td><td>L</td><td>L</td><td>L</td><td>L</td><td></td><td></td><td></td><td></td></tr><tr><td>Reliability</td><td>HIGH</td><td>HIGH</td><td>HIGH</td><td>HIGH</td><td>HIGH</td><td></td><td></td><td></td><td></td></tr><tr><td>Recommendations</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td><td></td><td></td><td></td></tr></table>

## References

[1] A. Drejer, The discipline of management of technology based on considerations related to technology. Technovation 17 (1997) 253–265

[2] A. Parasuraman, V.A. Zeithaml, L.L. Berry, A conceptual model of service quality and its implications for future research. J. Mark. 49 (1985) 41–50.

[3] M. Gregory, Technology management: a process approach, Arch. Proc. Inst. Mech. Eng, 1847-1982 209 (1995) 347–356.

[4] S.D. Galup, R. Dattero, J.J. Quan, S. Conger, An overview of IT service management, Commun. ACM 52 (2009) 124–127.

[5] B. McNaughton, P. Ray, L. Lewis, Designing an evaluation framework for IT service management, Inf, Manag, 47 (2010) 219–225.

[6] J. Iden, T.R. Eikebrokk. Implementing IT service management: a systematic literature review. Int. J. Inf, Manage, 33 (2013) 512–523.

[7] The Oficial Introduction to the ITIL Service Lifecycle, The Stationery Ofice, TSO, London, 2011.

[8] T.R. Eikebrokk, J. Iden, Enabling a culture for IT services: the role of the IT infrastructure library. Int. J. Inf, Technol, Manag. 15 (2016) 14–40.

[9] ISO/IEC. ISO/IEC 20000-1:2018 – Information Technology – Service Management - Part 1: Service Management System Requirements, International Organisation for

Standardisation, Geneva, Switzerland, 2018.

[10] B. Barafort, V. Betry, S. Cortina, M. Picard, M. St-Jean, A. Renault, O. Valdès, ITSM Process Assessment Supporting ITI. Van Haren Publishing. Zaltbommel Netherlands, 2009.

[11] P. Bernard, Foundations of ITIL, Van Haren Publishing, Zaltbommel, Netherlands, 2012.

[12] V. Lloyd, ITIL Continual Service Improvement, The Stationery Ofice, London, UK, 2011.

[13] CMMI, CMMI® for Services, Version 1.3, Software Engineering Institute, Carnegie Mellon University, MA. USA. 2010.

[14] B. Barafort. B. Di Renzo. O. Merlan. Benefits resulting from the combined use of ISO/IEC 15504 with the information technology infrastructure library (ITIL), in: M. Oivo, S. Komi-Sirviö (Eds.), 4th International Conference on Product Focussed Software Development and Process Improvement (PROFES). LNCS 2559, Springer Verlag, 2002, pp. 314–325.

[15] T.P. Rout, K. El Emam, M. Fusani, D. Goldenson, H.W. Jung, SPICE in retrospect: developing a standard for process assessment. J. Syst. Softw. 80 (2007) 1483–1493

[16] ISO/IEC, ISO/IEC 33002:2015 – Information Technology – Process Assessment – Requirements for Performing Process Assessment. International Organization fot Standardization, Geneva, Switzerland, 2015

[17] S. Mingay, K. Peattie, IT consultants — source of expertise or expense? Inf. Softw.

Technol. 34 (1992) 341–349.

[18] S. Yoon, H. Suh, Ensuring IT Consulting SERVQUAL and User Satisfaction: A Modified Measurement Tool, Inf, Syst, Front, 6 (2004) 341–351.

[19] M. Bruhn, D. Karlan, A. Schoar, The impact of consulting services on small and medium enterprises: evidence from a randomized trial in Mexico, J. Polit. Econ. 126 (2018) 635–687.

[20] M. Zarour, A. Abran, J.-M. Desharnais, A. Alarifi, An investigation into the best practices for the successful design and implementation of lightweight software process assessment methods: A systematic literature review, J. Syst. Softw. 101 (2015) 180–192.

[21] F.J.S. Vasconcellos, G.B. Landre, J.A.O.G. Cunha, J.L. Oliveira, R.A. Ferreira, A.M.R. Vincenzi, Approaches to strategic alignment of software process improvement: a systematic literature review. J. Syst, Softw. 123 (2017) 45–63

[22] H. Göbel, S. Cronholm, U. Seigerroth, Towards an agile method for ITSM self-assessment : a design science research approach, Proceedings of the International Conference on Management, Leadership and Governance (ICMLG 2013), Bangkok, Thailand, 2013, pp. 135–142.

[23] S. Peldzius, S. Ragaisis, Usage of multiple process assessment models, in: T. Woronowicz, T. Rout, R. O’Connor, A. Dorling (Eds.), Software Process Improvement and Capability Determination, Springer, Berlin Heidelberg, Germany, 2013, pp. 223–234.

[24] E. Deutskens, K. de Ruyter, M. Wetzels, An assessment of equivalence between online and mail surveys in service research, J. Serv. Res. 8 (2006) 346–355.

[25] L. Ritchie, B.G. Dale, Self-assessment using the business excellence model: a study of practice and process, Int. J. Prod. Econ. 66 (2000) 241–254.

[26] R. Williams, B. Bertsch, A. Van Der Wiele, J. Van Iwaarden, B. Dale, Self-assessment against business excellence models: a critique and perspective, Total. Qual. Manag. Bus, Excell, 17 (2006) 1287–1300.

[27] AXELOS, ITIL® Maturity Model, AXELOS, 2013.

[28] B. Barafort, A. Shrestha, S. Cortina, A. Renault, A.-L. Mesquida, A. Mas, A software artefact to support standard-based process assessment: evolution of the TIPA® fra mework in a design science research project, Comput. Stand. Interfaces (2018)

[29] M. Simonsson, P. Johnson, H. Wijkström, Model-based IT governance maturity assessments with COBIT, European Conference on Information Systems (ECIS) (2007) 1276–1287.

[30] M. Lepmets, A. Cater-Steel, F. Gacenga, E. Ras, Extending the IT service quality measurement framework through a systematic literature review, J. Serv. Sci. Res. 4 (2012) 7–47.

[311 S. Lee. H. Ahn. Assessment of process improvement from organizational change. Inf Manag, 45 (2008) 270–280.

[32] R. Jia, B.H. Reich, IT service climate—an essential managerial tool to improve client satisfaction with IT service quality, Inf. Syst. Manag. 28 (2011) 174–179.

[33] D. Spath, W. Bauer, C.-P. Praeg, IT service quality management: assumptions, frameworks and efects on business performance, Quality Management for IT Services-Perspectives on Business and Process Performance, IGI Global, PA, 2011, pp. 1–21.

[34] T.P. Rout, A. Tufley, Harmonizing ISO/IEC 15504 and CMMI, Softw. Process. Improv. Pract. 12 (2007) 361–371.

[35] E.B. Hyder, K.M. Heston, M.C. Paulk, The eSourcing capability model for service providers (eSCM-SP) v2, part 1: model overview, Information Technology Service Qualification Center (ITSQC), Carnegie Mellon University, Pittsburgh, USA, 2004.

[36] C. Tully. P. Kuvaia. R. Messnarz, Software process analysis and improvement: a catalogue and comparison of models. in: R. Messnarz. C. Tully (Eds.). Better Software Practice for Business Benefit: Principles and Experience. JEEE Computer Society. 1999, pp. 51–106.

[37] P. Crosby, Quality Is Free, McGraw-Hill, New York, 1979.

[38] W.E. Deming, Out of the Crisis, MIT Centre for Advanced Engineering Study, Mass, Cambridge, 1986.

[39] J.M. Juran, Juran on Planning for Quality, Macmillan, New York NY, 1988.

[40] R. Likert, The Human Organization: Its Management and Value, McGraw-Hill, New York, 1967.

[41] W.S. Humphrey, Managing the Software Process, Addison-Wesley, Reading, MA. USA, 1989.

[42] P. Fraser, J. Moultrie. M. Gregory, The use of maturity models/grids as a tool in assessing product development capability. Proceedings of JEEE International Engineering Management Conference (2002) 244–249.

[43] A.A. Nef, F. Hamel, T.P. Herz, F. Uebernickel, W. Brenner, J. vom Brocke, Developing a maturity model for service systems in heavy equipment manu facturing enterprises, Inf. Manag. 51 (2014) 895–911.

[44] ISO/IEC, ISO/IEC PDTS 33054 – Information Technology – Process Assessment – Process Reference Model (PRM) for Service Management, International Organization for Standardization, Geneva, Switzerland, 2019 In preparation.

[45] ISO/IEC, ISO/IEC PDTS 33074 - Information Technology - Process Assessment - Process Capability Assessment Model (PAM) for Service Management, Internationa Organization for Standardization, Geneva, Switzerland, 2019 In preparation.

[46] I. Benbasat, R.W. Zmud, The identity crisis within the is discipline: defining and communicating the discipline's core properties. Mis O. 27 (2003) 183–194.

[47] B. Furneaux, M. Wade, Theoretical constructs and relationships in information systems research. Handbook of Research on Contemporary Theoretical Models in Information Systems, IGI Global, 2009, pp. 1–17.

[48] S. Gregor, D. Jones, The anatomy of a design theory, J. Assoc. Inf. Syst. 8 (2007) 312-335.

[49] A.R. Heyner, S.T. March, J. Park, S. Ram, Design science in information systems research, Mis Q. 28 (2004) 75–105.

[50] S.A. Carlsson, S. Henningsson, S. Hrastinski, C. Keller, Socio-technical IS design science research: developing design theory for IS integration management, Inf. Syst. E-business Manag, 9 (2011) 109–131.

[51] K. Pefers, T. Tuunanen, B. Niehaves, Design science research genres: introduction to the special issue on exemplars and criteria for applicable design science research, Eur. J. Inf Syst, 27 (2018) 129–139.

[52] J. Venable, J. Pries-Heje, R. Baskerville, FEDS: a framework for evaluation in design science research, Eur. J. Inf. Syst. 25 (2016) 77–89.

[53] R.L. Baskerville, M. Kaul, V.C. Storey, Genres of inquiry in Design-Science research: justification and evaluation of knowledge production, Mis Q. 39 (2015) 541–564.

[54] S.T. March, G.F. Smith, Design and natural science research on information tech nology, Decis. Support Syst. 15 (1995) 251–266.

[55] B. Kuechler, V. Vaishnavi, On theory development in design science research: anatomy of a research project, Eur. J. Inf. Syst. 17 (2008) 489–504.

[56] K. Pefers, T. Tuunanen, M.A. Rothenberger, S. Chatterjee, A design science research methodology for information systems research, J. Manag. Inf. Syst. 24 (2007) 45–77.

[57] J.R. Venable, The role of theory and theorising in design science research, 1st International Conference on Design Science Research in Information Systems and Technology, CA, USA, 2006.

[58] I. Zigurs, B.K. Buckland, A theory of Task/Technology fit and group support systems effectiveness, Mis O. 22 (1998) 313–334.

[59] M.T. Dishaw, D.M. Strong, Extending the technology acceptance model with task–technology fit constructs, Inf. Manag. 36 (1999) 9–21.

[60] D.L. Goodhue, R.L. Thompson, Task-technology fit and individual performance, Mis Q. 19 (1995) 213–236.

[61] L.S. K, F. Howard, A supply chain study of technology trust and antecedents to technology internalization consequences, Int. J. Phys. Distrib. Logist. Manag. 36 (2006) 271–288.

[62] V.R. Basili, G. Caldiera, H.D. Rombach, Goal question metric paradigm, Encyclopedia of Software Engineering - 2 Volume Set, John Wiley & Sons, Inc., New York, USA, 1994, pp. 528–532.

[63] R.M. Fuller, A.R. Dennis, Does fit matter? The impact of task-technology fit and ap propriation on team performance in repeated tasks, Inf. Syst. Res. 20 (2009) 2–17.

[64] R. Moen, C. Norman, Evolution of the PDCA Cycle, Associates in Process Improvement, MI, USA, 2006.

[65] R.B. Austenfeld Jr, W. Edwards Deming, The Story of a Truly Remarkable Person 42 Research Society of Commerce and Economics–Hiroshima Shudo University, 2001, pp. 49–102.

[66] M. Hammer, J. Champy, Reengineering the Corporation: a Manifesto for Business Revolution, Harper Business, New York, NY, 1993.

[67] T.H. Davenport, Process Innovation: Reengineering Work Through Information Technology. Harvard Business School Press. Boston. MA. 1993

[68] M. Rosemann, J. vom Brocke, The six core elements of business process manage ment, Handbook on Business Process Management 1, Springer, 2015, pp. 105–122.

[69] ISO, ISO 9001:2015 – Quality Management Systems - Requirements, Internationa Organization for Standardization, Geneva, 2015.

[70] ISO/IEC, ISO/IEC 33004:2015 – Information Technology – Process Assessment – Requirements for Process Reference. Process Assessment and Maturity Models International Organization for Standardization. Geneva. 2015

[71] R.S. Kaplan, D.P. Norton, The Strategy Focused Organization: How Balanced Scorecard Companies Thrive in the New Business Environment, Harvard Business Press, USA, 2001.

[72] T.H. Davenport, J.E. Short, The new industrial engineering: information technology and business process redesign, Sloan Manage. Rey. 31 (1990) 11–27.

[73] K.B. Sheehan. E-mail survey response rates: a review, J. Comput. Commun, 6 (2001) 0.

[Z4]J. Ho-Won. H. Robin. G.D. R. E.E. Khaled. Findings from Phase 2 of the SPICE trials Softw. Process. Improv. Pract, 6 (2001) 205–242.

[75] T.P. Rout, K. El Emam, M. Fusani, D. Goldenson, H.-W. Jung, SPICE in retrospect: developing a standard for process assessment. J. Syst. Softw. 80 (2007) 1483–1493.

[76] ISO/IEC, ISO/IEC 33020:2015 – Information Technology – Process Assessment – Process Measurement Framework for Assessment of Process Capability, International Organization for Standardization, Geneva, 2015.

[77] ISO/IEC, ISO/IEC JTC1/SC7 WG10, Transition from ISO/IEC 15504 to ISO/IEC 330xx, Standing Document. 2017.

[78] J. Venable. J. Pries-Heie. R. Baskerville. A comprehensive framework for evaluation in design science research. 7th International Conference on Design Science Research in Information Systems and Technology, Las Vegas, USA, 2012.

[79] ISO/IEC, ISO/IEC 25010:2011 – Systems and Software Engineering – Systems and Software Quality Requirements and Evaluation (SQuaRE) - System and Software Ouality Models, International Organisation for Standardisation, Geneva. Switzerland, 2011.

[80] V.S. Lai, R.K. Mahapatra, Exploring the research in information technology im plementation, Inf. Manag. 32 (1997) 187–201.

[81] M.J. Goodwin, O. Heath, The 2016 Referendum, Brexit and the Left Behind: An Aggregate‐level Analysis of the Result, Polit. Q. 87 (2016) 323–332.

[82] S. Behari, IT Service Management: Process Capability, Process Performance, and Business Performance, University of Southern Queensland, 2018.

[83] V. Saavedra. A. Dávila. K. Melendez. M. Pessoa. Organizational maturity models architectures: a systematic literature review. in: M.M. Mejia J. Á. Rocha. T. San Feliu A. Peña (Eds.). Trends and Applications in Software Engineering. CIMPS 2016 Advances in Intelligent Systems and Computing, Springer, Cham, 2017. pp. 33–46

[84] A. Uskarci, O. Demirörs, Do staged maturity models result in organization-wide continuous process improvement? Insight from employees, Comput. Stand. Interfaces 52 (2017) 25–40

[85] F.Ç. Yeşildoruk, B. Bozlu, O. Demirörs, The Tool Coverage of Software Process Improvement Frameworks for Small and Medium Enterprises, PROFES, LNBIP, 2009, pp. 290–302.

[86] ISO/IEC, ISO/IEC FDIS 33020 – Information Technology - Process Assessment -

Process Measurement Framework for Assessment of Process Capability, International Organization for Standardization, Geneva, 2019 In preparation.

[87] C.A. Yauch, H.J. Steudel, Complementary use of qualitative and quantitative cultural assessment methods, Organ. Res. Methods 6 (2003) 465–481.

[88] P.M. Lee, Bayesian Statistics: an Introduction, 2nd ed., Wiley, London, 1997.

[89] AXELOS, ITIL Foundation: ITIL 4 Edition, The Stationery Ofice Ltd, 2019.

[90] A. Shrestha, A. Cater-Steel, M. Toleman, W.-G. Tan, A method to select IT service management processes for improvement, Journal of Information Technology Theory and Application 15 (3) (2015).

Dr Anup Shrestha is a lecturer and PhD in Information Systems from the University of Southern Queensland, Australia. His research interests include IT service management, process assessment, software engineering, IT standards, design science research, cloud computing and knowledge management. His pH.D. research, working on an Australian Research Council (ARC) industry linkage grant in the IT Service Management industry, was awarded the best Australian pH.D. in Information Systems ACPHIS (Australian Council of Professors and Heads of Information Systems) prize in 2016. His research collaboration with IT practitioners was recognized with the Queensland IT innovation award in 2015 and the Australian IT Service Management (itSMF) Service Management Innovation award in 2019. He is currently serving as the Standards Australia national representative for the develop ment and review of ISO/IEC JTC1/SC7 standards of software engineering. He has published peer-reviewed articles in IT conferences and academic journals including Behaviour and Information Technology, International Journal of Information Management and Computer Standards & Interfaces. Prior to his academic journey, Anup worked in the IT industry where his career progressed from programmer to project manager for 8 years.

Professor Aileen Cater-Steel is an Emeritus Professor of Information Systems and Higher Education consultant. Her research interests include IT Service Management (ITSM), IT Standards and Governance, e-Learning systems and IT outsourcing. In 2016, Aileen was honoured with a life-time achievement award from itSMF. She was Lead Chief Investigator on two ITSM projects funded by the Australian Research Council. She received a citation for outstanding contribution to student learning from the Australian Learning & Teaching Council and was awarded the ACPHIS (Australian Council of Professors and Heads of Information Systems) prize for her pH.D. thesis. She has published more than 160 peer reviewed articles and co-edited five research books. Prior to her academic appointment,

Aileen worked in the private sector and government organisations where her career progressed from programmer to IT manager. She is a Fellow of the Australian Computer Society and a Graduate member of the Australian Institute of Company Directors.

Professor Mark Toleman holds a joint appointment as University Secretary and Professor of Information Systems at the University of Southern Queensland (USQ). From 2006 to 2012 he was Professor and Head, School of Information Systems and Chair, Academic Board at USQ. He was Director of the e-Business Advisory and Research Centre at USQ from 2003 to 2005 and from 2000 to 2006 he was Associate Professor and Deputy Chair, Academic Board. Professor Toleman has a pH.D. in computer science from the University of Queensland and an MSc in mathematics from James Cook University. He was the President of the Australian Council of Professors and Heads of Information Systems from 2009 to 2012. Professor Toleman is a member of the Australian Institute of Company Directors, the Australian Computer Society, the Association for Information Systems and IFIP Working Groups 8.6 and 13.1. He has published over 170 peer reviewed articles in areas ranging from information systems to human–computer interaction to agricultural science.

Dr Suren Behari is the Director of Engineering at a financial services company in California, USA. He received his Bachelor of Science degree in Mathematics and Statistics from the University of Durban-Westville, South Africa. He moved to the United States and worked as a software engineer and later as a senior product manager. Behari has spoken at a variety of businesses, events and conferences around the world. He received his MBA in e-Business from the University of Southern Queensland in 2012 and pH.D. in Information Systems from the University of Southern Queensland in 2018. His research interest is the link between Information Technology Service Management (ITSM) Maturity and Financial Profitability.

Dr Mohammad Mehdi Rajaeian is a Lecturer in Information Technology at the Australian Catholic University, Peter Faber Business School. He holds a pH.D. in Information Systems from the University of Southern Queensland. He also received a Master of Business Administration and a BSc in Industrial Engineering both from Sharif University of Technology, Iran. His research interests include Decision Support System and Business Intelligence, Design Science Research, IT outsourcing, System Theory, Difusion of Innovation and the Research-Practice Gap.
