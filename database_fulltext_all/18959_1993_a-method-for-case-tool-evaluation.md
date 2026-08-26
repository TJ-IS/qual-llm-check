---
otero_id: 18959
otero_key: "DXRMWPNQ"
title: "A method for CASE tool evaluation"
authors: "Annette L. du Plessis"
year: "1993"
journal: "Information & Management"
doi: "10.1016/0378-7206(93)90051-t"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Techniques

# A method for CASE tool evaluation

Annette L. du Plessis

University of South Africa, Pretoria, South Africa

An epistemology for CASE that defines the current CASE technologies is presented. Its influence on traditional software process models is considered, and its support throughout a typical software development life cycle is identified. A four stage software process model is used as a basis for classifying CASE technology. A method for evaluating CASE products that follows a procedural framework is presented. Five evaluation criteria sets are used when applying the method to determine the CASE requirements for an organization.

Keywords: Software development life cycle; Software process model; CASE; Evaluation criteria sets; CASE evaluation method.

![](/api/attachments/DXRMWPNQ/fulltext/images/cda1d6f55f5917d50c2f046d9429352a5795c36f7dcc7029544c6be580ae9c1c.jpg)

Lerine du Plessis is professor in the Department of Computer Science and information Systems at the University of South Africa (UNISA). She started her computing career in 1964 after obtaining a MSc in Physics at the University of Stellenbosch, South Africa. She has worked in second, third and fourth generation environments while researching various aspects of software engineering over the past eighteen years. During the past nine years she has specialized in soft-

ware engineering environments, formal software specification and methodologies for information system development. She obtained a PhD in Computer Science under the supervision of Prof Daniel Teichroew of the University of Michigan in 1986 with a thesis entitled: A software engineering environment for real-time systems. She consults to various organizations, and is a member of a number of professional bodies such as the Computer Society of South Africa and the South African institute of Computer Scientists, of which she is Vice-President.

Correspondence to: A.L. du Plessis, Department of Computer Science and Information Systems, University of South Africa, P.O. Box 392, Pretoria, South Africa.

## 1. Introduction

Computer-assisted Software Engineering, or CASE, has acquired different meanings to developers and end-users in recent years. Since the nineteen sixties research projects have been undertaken to automate the system building process giving rise to the original notion of CASE. These projects focussed on providing aids for individual tasks of the development process and tended to be limited to a particular phase of the system development life cycle [1]. Although significant advances have been made since then to computer-assist the engineering of software, no computer can be used to develop and maintain software without human intervention. This is partly because the software development process is not understood fully, and the innovative ability of human developers cannot be conveyed to a computer.

Despite this Software Engineering (SE) as a discipline has matured from 1967 when it was given the name by a NATO Study Group [2]. Advances have since been made to improve both the task of the software engineer and the project manager by means of technical and managerial techniques, methods and methodologies [3]. Various life cycle frameworks and enhancements to software development models have gained acceptance. Project management techniques, well-established in other engineering disciplines, have been adopted in software projects. A comprehensive epistemology for SE has emerged, and along with it new ways of supporting the process by means of the computer.

Recent years have seen an explosion in microcomputer technology, with powerful desktop micros gradually becoming available at reasonable prices. Closely following this hardware trend is a proliferation of sophisticated presentation software, development tools and micro-based operating systems. At the same time multi-user environments and distributed development have become common. Users now have a range of hardware and software platforms, local area/wide area technologies and CASE products to choose from. As a result it has become difficult for management of large corporations and small businesses to choose among available products that will be useful for both the short and long term.

## 2. What is CASE today?

The overriding goal of CASE is to support software developers by means of automated tools; i.e. to use the capabilities of the computer in support of SE to improve the productivity of software development and the quality of the product [4]. There are of course direct analogies in the engineering disciplines, e.g. the productivity of design engineers is greatly enhanced by the use of computer-aided design (CAD) systems which help the drawing, analysis, and documentation tasks, and checks some aspects of the validity of a design. Despite the fact that a software product is abstract (not concrete), software development is a manufacturing process [5]. Over the past three decades various automated tools have been devised in support of the tasks of the software development life cycle (SDLC). Software tools to support the implementation phase of the SDLC became available as soon as symbolic programming languages were developed; there has been a gradually increasing level of support for the programmer ever since. Whereas earlier attempts at developing CASE products during the late sixties and early seventies were targeted mainly for mainframe platforms, the availability of cheap personal computers (PCs) in the 80s offered new possibilities. PCs and large workstations now have sufficient power and storage capacity to host a set of automated tools, making

CASE environments available to software developers [6].

The capabilities of CASE products vary from tools supporting a single phase method on a single workstation to integrated CASE environments supporting a life cycle methodology on a large mainframe or network of PCs $[7,8]$ . Many CASE products have expert system components to support the human software developer with the SE tasks $[9,10]$ . A taxonomy for CASE based on $[11]$ and $[12]$ is presented in Appendix 1.

The trends in CASE technology may be summarised as in Figure 1.

## 3. A software process model for CASE

The notion of a software development life cycle framework that represents a software process model has its origins in the Stagewise Model $[13]$ and the monolithic Waterfall Model $[14]$ . Monolithic models regard development as one large process which should be viewed in its entirety. Such models prescribe the development tasks according to a phased framework, where work in a successive phase only commence after satisfactory completion of the preceding phase. Only at the end of the implementation phase is the completed system delivered. In this context SDLCs that prescribe the full specification of requirements are also regarded as monolithic. Enhancements to such models, that permitted expansion of software products in the light of operational experience, influenced the direction of development which lead to the evolutionary development model $[15]$ . The availability of efficient prototyping tools required that the process model be augmented to allow incremental development $[16]$ .

Computer assistance was first attempted for the implementation phase of the SDLC by means of improvements in programming languages, and the design of powerful compilers and interpreters. More recently automation has advanced back in the life cycle as code generators, query language and fourth generation language systems provide code directly from the design documents. The tools that automate the tasks of the Construction Stage have been called lower-CASE tools. The phenomenon of automation progressing back up the Waterfall model has been called the salmon effect: a salmon advancing up a series of water steps [17]. Advances in automation however also occurred from the front-end of the life cycle as formal methods of requirements specification have been adopted. These formal methods use mathematics based and/or graphics based notations instead of natural language specification. Tools to support such methods are called upper-CASE tools.

<table><tr><td>Mainframe based development</td><td>→</td><td>PC Based development</td></tr><tr><td>CASE tool support for individual phases</td><td>→</td><td>CASE environment for complete SDLC</td></tr><tr><td>CASE support for Implementation</td><td>→</td><td>CASE support for Requirements Engineering</td></tr><tr><td>Human development skills</td><td>→</td><td>Expert system support for development</td></tr></table>

Fig. 1. Trends in CASE technology.

The software process model is influenced by the scope of CASE support and the degree of integration of the tools used. Tool intensive software development modifies the software process model and hence the life cycle framework by eliminating or curtailing one or more of the phases. For example, where appropriate prototyping tools are available a non-monolithic incremental development strategy may be adopted. The tools emphasise formal requirements specification that are machine processable. Such a strategy enables the software system to be built in a number of increments, where each is a functional unit of the software system $[17]$ . For commercial data processing applications, fourth generation technology is frequently applied to generate code from requirements specified in a suitable language.

For purposes of this paper the framework for comparing the various classes of technology is based on a four stage software process model. This model is representative of software process models used as a basis for information systems methodologies $[18]$ . The CASE tool support for the technical tasks of each of the stages has been identified from personal observation and $[19]$ and $[20]$ , and is summarized in Table 1.

## Strategy / tactical study stage

This stage involves an analysis of the organization to determine its information requirements.

The flow of strategic, tactical and operational information within the business areas of the organization is modelled, and the critical success factors are established. For each business area the information systems required to meet the objectives are identified. The stage deliverables are the repository and a Strategic and Tactical Information Systems Plan. Upper-CASE tool support, although not as well established as for later stages, does exist but usually it does not integrate well with the later CASE products.

## Requirements engineering stage

Requirements Engineering (RE) is concerned with a particular information system and involves Requirements Acquisition, Specification and Analysis. The stage deliverables are the repository and the Requirements Specification Document.

Requirements Acquisition (RA) is the capture of information from the users to determine their needs. RA requires an analysis of the existing system and of the problems, constraints and needs involved. Upper-CASE tool support exists for some of the tasks.

Requirements Specifications (RS) is the expression of the user's statement of the requirements in a notation that assists the analyst in considering their implications with the user. The specification should facilitate detailed analysis of requirements. Upper-CASE tool support is available for the textual/graphical/formal representation schemes of many RE methods for specifying requirements of the system with regard to system structure, function, control flow, and temporal behaviour perspectives and constraints. Other tasks that are supported are summarized in Table 1.

Requirements Analysis (RA) is the analysis of the specifications for completeness, consistency and feasibility, and checking for correct syntax and semantics. Upper-CASE tool support is available.

## Design stage

This stage comprises Design Specification, Detailed Design and Design Analysis. The stage deliverables are the repository, and the Design Document.

Table 1
CASE support for the life cycle stages.

<table><tr><td>Life cycle stage</td><td>Case support</td></tr><tr><td>Strategic/Tactical</td><td>Upper-CASEIdentifying objectives/organization units/business activitiesDevelopment of business modelIdentifying information systems and business areasAnalysis of priorities and cost/benefitPreparing Strategic/tactical IS Plan</td></tr><tr><td>Requirements Engineering</td><td>Upper-CASE</td></tr><tr><td>Requirements Acquisition</td><td>Acquisition of requirementsAnalysis of existing systemIdentifying requirements specifiersMultiple choice questionnaires and statistical processingPreparation of interview plans/recording results</td></tr><tr><td>Requirements Specification</td><td>Logical system modelingData definitionConcurrency definitionInterface/environmental requirementsPerformance/acceptance testing requirements prototypingVerification/validation/testing requirementsRequirements Specification Document</td></tr><tr><td>Requirements Analysis</td><td>Performance analysisRisk analysisCost/benefit analysisReviews/inspections of requirements specification</td></tr><tr><td>Design</td><td>Middle-CASE</td></tr><tr><td>Design Specification</td><td>PrototypingRecording of reusable designsUpdating verification/validation/testing requirementsDesign Document</td></tr><tr><td>Detailed Design</td><td>System architecture designDesign decomposition by function/dataDocumentation/evaluation of design algorithmsDocumentation of design element interrelationshipsUpdating Design Document</td></tr><tr><td>Design Analysis</td><td>Verification of design vs requirements specificationsStatic analysisProduction of executable modelsSimulation of designAnalysis of performance/access requirementsComplexity analysis of functions/data/events/interfacesAnalysis of access/operational/integration requirementsAnalysis of data volumesReviews of design</td></tr><tr><td>Construction</td><td>Lower-CASE</td></tr><tr><td>Program Coding</td><td>Syntax directed edition of source codeSource code compilation/interpreting/debuggingLinking/executing of object codeCode/stub generation from program specificationsOnline document production/help information</td></tr><tr><td>Testing</td><td>Test data generationExecution flow summaryFile comparisonSimulation of environmental conditionsSymbolic dumps and execution tracingInteractive debuggingAssembly of implementation Document</td></tr></table>

Table 2 Summary of evaluation framework.

<table><tr><td>Stage</td><td>Input</td><td>Task</td><td>Output</td></tr><tr><td>1. Project Planning</td><td>Initial request</td><td>Prepare evaluation project plan</td><td>Project proposalProject plan</td></tr><tr><td>2. Requirements Definition</td><td>Evaluation Criteria Sets</td><td>Prepare checklist for organizationPrepare invitation to tenderIdentify CASE product suppliers and literature</td><td>Organization Requirements ListInvitation-to-tender Document</td></tr><tr><td>3. Critical Requirements Definition</td><td>Organization Requirements List</td><td>Prepare critical Requirements ListFinalise CASE Product Monitor History</td><td>Product Monitor HistoryCritical Requirements ListProduct Monitor History</td></tr><tr><td>4. Preliminary Evaluation</td><td>Invitation-to-tender DocumentProduct Monitor HistoryCritical Requirements List</td><td>Prepare coarse filterConduct coarse filter evaluationDerive preliminary evaluation results</td><td></td></tr><tr><td>5. Detailed Non-Functional Evaluation</td><td>Invitation-to-tender DocumentOrganization Requirements ListProduct Monitor HistoryCritical Requirements ListRequirements Judgement Scale</td><td>Complete actual valuesReview Detailed Non-functional evaluation results</td><td>Product Monitor HistoryProduct Monitor History</td></tr><tr><td>6. Detailed Functional Evaluation</td><td>Product Monitor HistoryTechniques ChecklistProcedural FrameworkRequirements Judgement ScaleTechniques Judgement ScaleCost and impact Analysis Checklist</td><td>Evaluate functionalityDo cost/impact analysis</td><td>Product Monitor HistoryCost and impact Analysis</td></tr><tr><td>7. Results Evaluation</td><td>Organization Requirements ListProduct Monitor HistoryCritical Requirements ListCost and impact Analysis</td><td>Review evaluation results</td><td>Most suitable CASE product</td></tr></table>

Design Specification is the phase during which design alternatives are recorded in machine processable notation that is intended to enhance communication between project participants. Middle-CASE support is available for textual/graphical/formal representation schemes of many design methods used for specifying the design alternatives, and for the tasks shown in Table 1.

Detailed Design, during which a design is derived that meets the functional, operational, and implementation requirements. Middle-CASE support is available.

Design Analysis is performed to validate the chosen design by verifying it against the requirements specifications to ensure that it meets them. The process also includes checking the completeness and consistency by static analysis of the models, rules, structures and algorithms of the design. Dynamic analysis of the behaviour of the design is done by checking control and data flows for possible deadlock situations. Middle-CASE support is available for this and other tasks.

## Construction stage

This stage consists of two phases: Program Coding and Testing/Debugging. The stage deliverables are the software system, the repository and the implementation Document.

Program Coding involves the development of algorithms and accompanying data declarations in the programming language of choice. LowerCASE support is available for a number of technical tasks and the production of training material (refer Table 1).

Testing is the process of inferring certain behavioural properties of a product based, in part, on the results of executing the product in a known environment with elected inputs [21]. Testing is done in a number of steps: unit testing, module testing, subsystem testing, integration testing, hardware/software integration and acceptance testing.

Debugging is the process of locating errors in a program and correcting the code. Lower-CASE tool support is available.

Besides tool support for the technical software engineering tasks, project management tools are also available to support the management tasks of a software project. These tasks are, however, outside the scope of this article.

With considerable support available in the form of a large number of tools for the stages of the Software Process Model, it is necessary to follow a well-defined evaluation method when selecting tools $[22,23]$ .

## 4. The evaluation method

The method of evaluation proposed here provides some structure to the evaluation of CASE tools. It consists of a procedural framework that describes the following aspects:

(i) The breakdown of the evaluation task into a number of stages, each in turn broken down further into detailed activities.

(ii) Each stage should have clearly defined objectives, with required inputs, outputs to be delivered, and predetermined review points stated.

(iii) The required documentation for each stage.

(iv) The accumulation of stage deliverables into a final baseline representing the outcome of an evaluation procedure.

The framework of Heap [19] was used as a basis for the evaluation method. It was compiled to evaluate CASE tools for the analysis and design stages of the SDLC. The purpose of the CASE tool and the life cycle stage that it supports, should first be established.

The evaluation procedure for CASE evaluation may be structured into seven stages. Table 2 summarizes the evaluation procedure, listing the input, the tasks to be performed, and output for each of the stages of the evaluation project. It is important to note that the task of project management does not form part of this evaluation method. The evaluation project should be managed using the Project Proposal and Project Plan documents as input to a project management and control system. The stages are reviewed below:

Stage 1 – Project planning. During this stage, the Project Proposal and the Project Plan are prepared. Estimates of costs, time, and resources for each stage and also means of controlling the project reviews are included.

Stage 2 - Requirements definition. Here a requirements analysis is performed to define what is required of the CASE tool. A list of requirements of the organization is prepared by referencing the Evaluation Criteria Sets detailed in

Table 3
Techniques for CASE evaluation.

<table><tr><td>Stages</td><td>Techniques</td></tr><tr><td>1</td><td>Cost and time estimationProject planning and staff allocationDocument preparation: Project Proposal and Project Plan</td></tr><tr><td>2</td><td>Analysis and documentation of organization requirements vs Evaluation Criteria SetsDocument preparation: Invitation to tender, Organization Requirements List</td></tr><tr><td>3</td><td>Document preparation: Product Monitor List, Critical Requirements History</td></tr><tr><td>4</td><td>EvaluationDocument preparation: Product Monitor History</td></tr><tr><td>5</td><td>QuantificationScore allocationWeight allocationDocument preparation: Product Monitor History</td></tr><tr><td>6</td><td>Hands-on evaluationEvaluationScore allocationCost/impact analysisDocument preparation: Cost and impact Analysis, Product Monitor List</td></tr><tr><td>7</td><td>Result evaluationDocument preparation: Final selection of most suitable CASE product</td></tr></table>

<table><tr><td>Price per unit, Multiple units</td></tr><tr><td>Product availability</td></tr><tr><td>Training requirements, costs</td></tr><tr><td>Product maturity</td></tr><tr><td>Adaptability within Technologies of organization</td></tr><tr><td>Vendor/supplier characteristics</td></tr><tr><td>- Market/Business credibility</td></tr><tr><td>- Product portfolio</td></tr><tr><td>- Company viability</td></tr><tr><td>Vendor technical support and maintenance</td></tr><tr><td>Audit features</td></tr><tr><td>Product portability</td></tr><tr><td>- Hardware environments</td></tr><tr><td>- Range of OS</td></tr><tr><td>- Hardware independent OS</td></tr><tr><td>- Hardware architecture supported by various suppliers</td></tr></table>

Tables 4 to 8. Invitations to organizations to tender are drawn up and product sources and references are established. The deliverables are invitations-to-tender and the Organization Requirements List, both to be used in later stages of the framework.

Stage 3 - Critical requirements definition, where a short list of critical and/or essential requirements are compiled from the requirements analysis. This stage involves drawing up a list of suppliers of CASE products, called the Product Monitor History, which follows the progress of a product throughout the evaluation.

Stage 4 – Preliminary evaluation during which the original CASE tools that are to be evaluated are reduced by performing a coarse evaluation against the Critical Requirements List. The deliverable is an update of the Product Monitor History.

Stage 5 - Non-functional evaluation, when a reduced number of CASE tools are evaluated in detail, resulting in a shortlist of possible CASE tools. Evaluation is performed against a number of quantified requirements (values which are assigned). The deliverable is another update of the Product Monitor History.

Stage 6 - Detailed functional evaluation in which a detailed evaluation of the CASE tools on the short list is conducted in order to establish the practical functionality of the tools. The deliverables are the updated Product Monitor History, and a Cost and impact Analysis Document.

Stage 7 - Results evaluation during which the CASE tool that rates highest in meeting the requirements is identified.

The techniques that are used during the stages are summarized in Table 3. The final selection documentation contains details of costs, benefits, requirements and functionality.

## 5. Evaluation criteria sets

The CASE requirements for an organization, the Organization Requirements List, are determined from a comprehensive framework of criteria, the Evaluation Criteria Sets, during Stage 2 of the evaluation project. The Organization Requirements List forms the basis for Stages 4, 5 and 6. The Evaluation Criteria Sets define the large number of evaluation criteria that an orga-

Table 5
Project management criteria.

clude the criteria relevant to project planning, monitoring, and control, and project standards. Configuration Criteria (refer Table 6) are concerned with hardware related and physical issues of the environment. Technical Criteria (refer Table 7) concern the support provided by the CASE tool for the analyst, designer, software and system engineers. The Usage Criteria (refer Table

Table 7
Technical criteria.

nization may deem relevant. The following sets have been identified: General Management Criteria, Project Management Criteria, Configuration Criteria, Technical Criteria, and Usage Criteria.

General Management Criteria (refer Table 4) include those criteria that can guide management in the cost \benefit analysis of the CASE tool. Project Management Criteria (refer Table 5) in-

Table 6
Configuration criteria.

Hardware platform (main, mini, micro)
Memory and processing capability
Graphics interface (mouse)
Hardcopy (printers, plotters)
Network configurations (LAN, WAN)
RAM/ROM/EPROM
Disk space system residing requirements
Porting techniques
Power supply
Physical Environment
Logistical constraints
Robustness

Life cycle range of application
Domain of application
Integration features
- compatibility of I/O between life cycle phases
- with other software tools
- sharing of HW and SW platform with other software
- customizability of interface
Adaptability
Extensibility
Customizability
Predefined deliverables
communication of deliverables
Traceability among product components
Documentation quality
Volume features
- data volumes
- maximum number of users
- maximum number of concurrent projects
Man-machine interface
- graphics for representation schemes
- method of data entry/retrieval,
    manipulation/update by
    menu selection
    mouse
    windows/icons/scroll/pan/zoom techniques
Performance features
Quality assurance

8) provide guidance to developers and end-users regarding the suitability of the tool for the development of particular applications. The evaluation criteria sets are to be described in detail in a follow-up article.

## 6. Summary

This article reviews the emergence of CASE as a technology to improve the productivity of the development process, and the quality of the software product. The influence of CASE technology on the traditional software process model is explored and CASE support classified into upper-, middle-, and lower-CASE. Tool support for the tasks of a typical process model is indicated. Since the evaluation and selection of a suitable CASE product has become difficult an evaluation method is outlined which provides some structure to a CASE evaluation project. The method is being applied in a number of student projects, and the results are to be evaluated when sufficient data is available.

## References

[1] D. Teichroew and H. Sayani, Automation of system building, Datamation, Vol. 17, No. 8, 1971.

[2] P. Naur, B. Randall and J. Buxton (eds), Software Engineering: Concepts and Techniques, Petrocelli/Charter, New York, 1976.

[3] Computer Science and Technology Board, Scaling up: a Research Agenda for Software Engineering, National Academy Press, Washington DC, 1989.

[4] E.J. Chikofsky and B.L. Rubenstein, CASE: Reliability engineering for information Systems, IEEE Software, March 1988.

[5] A. Spector and D. Gifford, A computer Science perspective of bridge design, Comm ACM, 29(4), 1986.

[6] K. Spurr and P. Layzell (eds), CASE on trial, John Wiley & Sons, 1990.

[7] W. Suydam, CASE makes strides toward automated software development, Computer Design, January 1987.

[8] T. Parker, A baker's dozen CASE tools for PCs and workstations, Computer Language, January 1989.

[9] M.A. Cherubini, L. Fanti, P. Torrigiabi and M. Zallocco, An integrated expert-system builder, IEEE Software, November 1989.

[10] P. Devanbu, R.J. Brachman, P.G. Selfridge and B.W. Ballard, Lassie: a knowledge-based software information system, Comm ACM, Vol. 34, No. 5, 1991.

[11] A.L. du Plessis, A Software Engineering Environment for Real-time Systems, PhD thesis, University of South Africa, 1986.

[12] C. McClure, CASE: State of the practice, 1990 CASE Conference, Mike Bergen and Associates, Johannesburg, Republic of South Africa, 1990.

[13] H.D. Bennington, Production of large computer programs, Proc ONR Symp Advanced Programming Methods for Digital Computers, 1956.

[14] W.W. Royce, Managing the development of large software systems: Concepts and techniques, Proc Wescon, 1970.

[15] D.D. McCracken and M.A. Jackson, Life-cycle concept considered harmful, ACM SE Notes, April 1982.

[16] S. Hekmatpour, and D. Ince, Rapid software prototyping, Technical Report 86/4, Open University, Milton Keynes, UK, 1986.

[17] D.R. Graham, Incremental Development: Review of non-monolithic models, Information and Software Technology, Vol. 31, No. 1, 1989.

[18] T.W. Olle, J. Hagelstein, I.G. Macdonald, C. Rolland, H.G. Sol, F.J.M. van Assche and A.A. Verrijn-Stuart, Information Systems Methodologies: A framework for understanding, 2nd ed, Addison Wesley, 1991.

[19] G. Heap, Evaluating software tools for systems analysis and design, NCC Publications, 1988.

[20] R. Rock-Evans, CASE Analyst Workbenches: a detailed product evaluation, Vol. 1 and Vol. 2, Ovum Ltd, 1989.

[21] J.B. Goodenough, A survey of program testing issues, Research Directions in Software Technology, P. Wegner (ed), The MIT Press, Cambridge, 1979.

[22] G.F. Evans and J.R. Riha, Assessing DSS effectiveness using evaluation research methods, Information and Management, 16, 1989.

[23] L.A. Black and M.T. Jelassi, DSS Software selection: a multiple criteria decision methodology, Information and Management, 17, 1989.

## Appendix 1. A CASE taxonomy

CASE Hardware Platform - a one-, two-, or three-tiered hardware system architecture that provides an operating platform for CASE tools.

CASE Methodology - a structured methodology defining a disciplined engineering approach, supported by automated tools, for the development and maintenance of software.

CASE System - a set of integrated CASE tools that share a common user-interface and run in a common computer environment.

CASE Technology - a software technology providing an automated engineering discipline for software development, maintenance and project management.

CASE Tool - any software tool that provides automated assistance for the creation, maintenance and project management of software systems.

CASE Toolkit - a set of integrated CASE tools automating a phase of the SDLC, or a software job class.

CASE Workbench - a set of integrated CASE tools for automating various phases of the SDLC and running on a personal workstation.

CASE Workshop - a set of integrated CASE tools for automating the entire SDLC within a distributed environment, with the generic capability to accommodate new system development models.

CASE Workstation - a technical workstation or PC equipped with CASE tools that can automate various SDLC phases.

Encyclopedia - (in the context of SE) a storage mechanism for defining and managing all the information and objects needed to develop, maintain and execute a software system.

ICASE - a set of integrated CASE tools sharing a common user interface, data interface, life cycle framework, and repository.

Lower-CASE - CASE tools that support the tasks of the later life cycle stage, namely Construction. Method - (in the context of SE) an orderly, defined way of carrying out one or more of the software development and post-deployment support activities.

Methodology - a system of methods that provides the overall approach to developing and monitoring software by unifying technical and project management tasks during the SDLC.

Methodology Companion - a set of CASE tools that automates tasks of a particular CASE methodology, as well as the production of phase deliverables.

Middle-CASE - CASE tools that support the design tasks of the life cycle.

Repository – the encyclopedia of an organisation's software systems.

Software Development Life Cycle (SDLC) - a framework structured as a succession of stages, or phases, according to which a software product is developed. The life cycle framework is also referred to as the software process model.

Upper-CASE - CASE tools that support the tasks of the earlier life cycle stages, i.e. Strategy/Tactical Study and Requirements Engineering.
