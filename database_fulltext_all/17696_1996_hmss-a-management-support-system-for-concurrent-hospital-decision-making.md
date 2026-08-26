---
otero_id: 17696
otero_key: "PK2G57E4"
title: "HMSS: a management support system for concurrent hospital decision making"
authors: "Guisseppi A. Forgionne; Rajiv Kohli"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(95)00011-9"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# HMSS: a management support system for concurrent hospital decision making

Guisseppi A. Forgionne $^{a,*}$ , Rajiv Kohli $^{b}$

$^{a}$ Information Systems Department, University of Maryland Baltimore County, Catonsville, MD 21228 USA $^{b}$ Hospital Information Systems Department, St. Joseph Medical Center, 7620 York Road, Towson, MD 21204 USA

## Abstract

Mounting health care costs have escalated the pressure on hospitals and other health care providers to control expenses. Conventional hospital information systems help meet the challenge by providing data necessary for policy formation and outcome measurement. Additional decision support systems deliver models that can be used to systematically evaluate the policies. When deployed successfully, each stand-alone system can effectively support a segment of the hospital decision making process. Integrating the stand-alone functions can enhance the quality and efficiency of the segmented support, create synergistic effects, and augment decision making performance and value. A high-level integration framework, known as the management support system (MSS), can be adapted to provide the desired synthesis. This paper demonstrates how management support systems can improve hospital decision making. It overviews the hospital decision making process, presents an MSS for supporting this process, and measures the impact of the MSS on the process and outcomes of decision making. The paper also examines the implications of the analyses for information systems research and health care practice.

Keywords: Concurrent engineering; Decision support systems; Decision technology systems; Expert systems; Executive information systems; Health care decision making; Health care games; Health care outcome measures; Health care process measures; Hospital information systems; Intelligent decision support systems; Management support system

## 1. Introduction

To be successful in the long term, health care organizations must provide competitive services that are valued by patients. Administrators are adopting the Total Quality Management (TQM) philosophy to help achieve the desired strategic results. For example, a recent study by the American Hospital Association (AHA) showed that 44% of surveyed hospitals use TQM to improve quality and cut costs [7]. The quality measure will be a composite of service, length of stay (LOS), and efficiency [16,45,58]. Recent reforms will spur health care institutions to follow this trend.

In TQM, there is an emphasis on the prevention of problems, customer satisfaction, and continuous improvement in the organization's processes [51]. A quality team is created to identify problems and improve relevant processes in a systematic and integrated manner. Systems are established to ensure that the organization maximizes quality and provides services as good, or better, than those of the competition. Rewards came in the form of continuous and concrete improvements that, over time, achieve strategic objectives, such as lowering costs, improving productivity, differentiating services from the competition, and innovating organizational processes $[24,33]$ .

For made-to-order enterprises, such as hospitals and other health care institutions, concurrent engineering (CE) can facilitate TQM and help the organization realize its strategic objectives $[9,30]$ . In CE, the service life cycle is treated as a harmonious process that focuses on the priorities and requirements of the patient. Participating staff are stimulated to continuously improve service tasks, events, and processes in an integrated and systematic manner $[20]$ . The goals of the effort are to improve quality, reduce costs, and decrease the lead time from admission to discharge for new or readmitted patients $[11]$ .

At each phase of concurrent engineering, clinicians and administrators must make complex decisions. Analytical techniques will be required to methodically evaluate the decision alternatives, and these techniques will employ and generate a large volume of clinical and administrative information $[34]$ . This information and the created knowledge must be shared among affected staff to enhance quality, to optimize the use of scarce resources, and to better plan and manage the concurrent engineering $[56]$ .

Various information systems can be used to provide the clinical and administrative support needed in concurrent engineering $[27,32]$ . While each system can bolster a separate segment of the health care process, none are designed to render entire CE support $[14]$ . Comprehensive support will require a consolidation of the separate information system functions and an effective delivery of the integrated capabilities $[25,71]$ .

This paper presents an information system, called the Hospital Management Support System (HMSS), that can deliver comprehensive CE support for hospitals. It first overviews the hospital decision making process, discusses the role of concurrent engineering in improving this process, and catalogs gaps in existing CE support. The paper then explains how information system functions can help close these support gaps, presents the HMSS architecture for integrating and delivering these functions, and measures the impact of the HMSS on hospital decision making process and outcomes. Also, there is an examination of HMSS's implications for information systems research and health care practice.

## 2. Hospital decision making

Fig. 1 outlines a hospital's made-to-order process. As Fig. 1 illustrates, administrative tasks are triggered by a patient admission. These tasks include recording the patient's demographics (such as name, age, address, and gender), insurance data, previous medical history, and reported complaints, establishing a billing account, and assigning the patient to a treatment or care room.

![](/api/attachments/PK2G57E4/fulltext/images/8cc39829b7fc68a7c42738c3b30b28ef48f74b51ace4ee00d9cdaa7d8404ec20.jpg)  
Fig. 1. Hospital made-to-order process.

Administrative tasks are used to develop work requirements, which prompt diagnostic and prescriptive events. These events involve vital signs taken by a nurse, physician examinations, and laboratory tests, X-rays, and other investigations ordered by physicians.

Diagnostic and prescriptive events result in specifications for medical services and its various components. Health care staff use the specifications to develop treatment and care processes, such as medication, surgery, and physical therapy. Treatment and care beget a recovered (or harmed) patient ready for discharge and billing. The clinical events and processes also generate facility and staff charges, tests, medical procedures, and length of stay (LOS) records, occupancy ratios, and other administrative data.

## 2.1. Sequential engineering

Traditionally, the hospital made-to-order process has been implemented through a successive set of steps from patient admission through discharge and billing $[21]$ . Outputs from each preceding step become inputs to the succeeding step in the process. For example, medical service specifications become guidelines for treatment and care processes. Information and knowledge from a preceding step flow unidirectionally to a succeeding step at the discretion of the participating personnel. For example, administrators decide the level of detail included in the work requirements sent forward for diagnostic and prescriptive events.

The sequential engineering can result in operational inefficiencies and knowledge transfer difficulties [22].

Operational inefficiencies. Training, experience, and other factors influence personnel to focus on domain-specific, rather than enterprise, performance. A domain-productive action at a preceding stage may inadvertently hinder operations at a succeeding stage of the sequential process. For example, an administrator may assign an admitted patient to a cost-effective but clinically-inefficient treatment facility, or a physician may specify medically-effective requirements that unknowingly create administrative difficulties.

Knowledge transfer difficulties. Throughout the made-to-order process, personnel will transform information into task, event, and process knowledge. Knowledge generated at a preceding step may be useful for a succeeding step of the sequential engineering. For example, problems encountered during medical treatment may be pertinent to hospital administration, and “lessons learned” during administration may help improve the hospital’s medical practices. Since participating personnel may be unaware of these relationships, generated knowledge may remain in the specific domains rather than being exchanged successively among the relevant parties.

If uncorrected, the operational inefficiencies and knowledge transfer difficulties can impair service quality $[30,54]$ . Rectifying the deficiencies in a sequential environment may involve extensive service reworking and other reactive actions that can strain scarce resources, lengthen hospital stays, increase costs, and degrade treatment and care $[23,70]$ . These outcomes will inhibit the hospital's ability to contend for patients in the dynamic and competitive marketplace $[73,74]$ .

## 2.2. Concurrent engineering

To alleviate the strategic problems experienced in sequential engineering, hospitals can utilize the concurrent engineering approach depicted in Fig. 2. In this approach, tasks, events, and processes are performed in a simultaneous, rather than sequential, fashion. During the synchronous processing, there is an interactive, multidirectional sharing of information and knowledge between the participating personnel. Physicians, nurses, and administrators are given concurrent access to pertinent information in real time, and the knowledge is focused on the specific decision making needs of each participant [31].

An experienced coordinator or a CE team (which typically would include clinicians and administrators) can be used to facilitate the information and knowledge transfer and to manage the concurrent engineering [48]. For example, an administrator can work through the coordinator or CE team to identify pertinent diagnostic/prescriptive and treatment/care issues at the time of patient admission. The coordinator or team representative can consult relevant clinical personnel to catalog the issues and, at the same time, communicate administrative work requirements to the clinicians. Itemized issues, such as specification and process alternatives, potential problems, and suggested actions, can be disclosed by the coordinator or CE team to the requesting administrator.

![](/api/attachments/PK2G57E4/fulltext/images/dbfa044efc87ae6fea5ab856aac9b0809a68984e8cba311a98c08e3cbc417ee2.jpg)  
Fig. 2. Hospital concurrent engineering.

Similar assistance on administrative matters can be obtained by nurses, physicians, and other pertinent clinicians. For example, a clinician can work through the coordinator or CE team to identify pertinent administrative issues at the time of patient diagnosis, treatment, and care. The coordinator or team representative can consult relevant administrative personnel to catalog the issues and, at the same time, communicate medical service specifications to the administrators.

Itemized issues, such as administrative task and billing plan alternatives, potential problems, and suggested actions, can be disclosed by the coordinator or CE team to the requesting clinician.

The concurrent engineering enables the hospital to be proactive rather than reactive. Service development is viewed as one coherent process with a focus on the continuous improvement in clinical and administrative practice. Participating personnel incorporate the concurrently shared information and knowledge within the development effort to avoid potential problems in administrative tasks, diagnostic and prescriptive events, and treatment and care processes. The proactive effort is expected to help hospitals achieve their strategic objectives by enhancing quality, reducing costs, decreasing diagnostic and prescriptive lead time, and improving treatment and care $[18]$ .

## 2.3. CE challenges

Realizing the strategic potential from concurrent engineering will present significant challenges to the traditional hospital. Some of the challenges are cultural in nature. Clinicians and administrators bring different backgrounds, experiences, perspectives, approaches, and expectations to hospital operations. These cultural differences can lead to conflicts that disrupt concurrent engineering efforts. To avert such disruptions, the CE coordinator or team must: (a) be skilled in both the clinical and administrative cultures and (b) establish programs and policies that accommodate (or even exploit) the cultural differences.

Other challenges are organizational in nature. Tasks, events, and processes must be redesigned and reengineered to accommodate CE [37]. A concurrent engineering team or coordinator must be formed and charged with the responsibility of managing the effort. Current personnel will require education and training in, or new personnel must be employed with, concurrent engineering skills and abilities. Clinicians and administrators must be convinced that the concurrent engineering will be personally as well as organizationally beneficial, and they must agree to participate in the effort.

The cultural and organizational changes will compel substantial informational technology support. Concurrent engineering depends on a complete, integrated, and systematic sharing in real time of administrative and clinical decision information and knowledge. Much of the necessary intelligence is complex and scattered within and outside the hospital. To integrate the information and knowledge in a purposeful and useful manner, staff must identify the relevant concurrent engineering issues, locate the formal and informal sources of intelligence, retrieve the intelligence, and perform essential analyses and evaluations $[40,50]$ .

## 2.4. Information technology support gaps

The hospital will have access to information technology that can support segments of clinical and administrative decision making. There are management information systems (MIS) that retrieve requested information from interfaced sources, organize the data, and generate reports that summarize department activities and performance $[6,8,43]$ . Decision support systems (DSS) and separate expert systems (ES) deliver methodologies that: (a) help clinicians diagnose illnesses and prescribe treatments and care, and (b) assist administrators model financial processes and forecast costs $[5,36,62]$ .

The available MISs, DSSs, and ESs, however, do not provide all the information technology needed to enable concurrent engineering in hospitals. Support gaps involve organization modeling, data access and reporting, and knowledge delivery.

Organization modeling. Alternative tasks, events, and processes will involve clinical and administrative trade-offs. To perform concurrent engineering successfully, participating personnel must consider these trade-offs, either explicitly or implicitly, when selecting alternatives. Moreover, the evaluation must focus on overall hospital, rather than individual department, performance. The required analyses and evaluations can be facilitated by utilizing models that: (a) formally or informally describe the clinical and administrative trade-offs, and (b) measure the impact of task, event, and process alternatives on hospital (rather than individual department) performance. These organization modeling functions can be delivered with a decision support system [44,59].

Data access and reporting. Much of the requisite numerical data for the organization models can be found in clinical and administrative databases within and outside the hospital. Typically, these databases reside at geographically-separated locations and are captured with, and stored on, incompatible hardware and software platforms. For the captured information to be useful in concurrent engineering:

1. the dispersed databases must be linked and shared in real time among relevant staff,

2. accessed data must be filtered, compressed, and focused on critical success factors, problems, and opportunities, and

3. there must be a quick and user-friendly "drill-down" to requested supporting detail.

These data access and reporting functions can be delivered with an executive information system [19,64].

Knowledge delivery. Expertise will be needed to recognize relevant CE issues, models, and data, locate and retrieve the knowledge, and identify and execute vital analyses and evaluations. Clinical and administrative staff, CE team representatives, or a CE coordinator must find the scarce expertise and acquire the relevant concurrent engineering knowledge from various experts dispersed throughout (and sometimes outside) the hospital. This interpersonal consultation process can be inefficient, and it does not provide a formal mechanism to preserve the acquired knowledge for future use. Expert systems can be used to capture the concurrent engineering knowledge and act as electronic counselors in delivering expertise to appropriate staff [42,49,53,63,61].

## 2.5. Hospital management support system (HMSS)

When implemented successfully, each autonomous new system can close a separate existing gap in the support for concurrent engineering. A new decision support system can provide the organization modeling, a new executive information system can provide the data access and reporting, and a new expert system can provide the knowledge delivery needed for effective concurrent engineering. Integrating the autonomous functions can enhance the quality and efficiency of the components, create synergistic effects, and augment system performance and value $[28,39,52,60]$ .

![](/api/attachments/PK2G57E4/fulltext/images/f9db34b70e0fcf150d7df996215b2d0bf3b428c40bd78af9bc07102f8f29a69e.jpg)  
Fig. 3. Hospital management support system (HMSS).

High-level integration can be achieved by embellishing a decision support system with executive information and expert systems to form a management support system (MSS) [17,67]. The hospital management support system (HMSS), shown conceptually in Fig. 3, is an application of this integration strategy.

As Fig. 3 illustrates, the HMSS is an integrated system of computer hardware and software. Hardware consists of a workstation, printer, and a modem (or other device) to link workstations with other hospital information systems.

Software includes a workstation-compatible, user-friendly operating environment and applications software. Applications software will include a decision support system (DSS) generator, an executive information system (EIS) product, and an expert system (ES) shell.

Inputs. The HMSS has a database that captures and stores joined patient, clinical, and administrative data. A modelbase captures and stores economic and accounting constructs to describe and simulate financial outcomes, management science models to evaluate hospital performance, and network methodologies to schedule clinical and administrative activities. In addition, there is a knowledgebase that captures and stores linked patient data, treatment/care issues, and historical management actions.

Processing. CE team representatives, a CE coordinator, and other interested clinicians and administrators use the HMSS interactively to perform analyses and evaluations that include:

1. organizing data into parameters needed for the clinical and administrative phases of concurrent engineering,

2. structuring organization models that represent administrative tasks, diagnostic and prescriptive events, and treatment and care processes in an integrated and complete manner,

3. simulating performance outcomes from proposed clinical and administrative policies under specified internal and external conditions, and

4. solving specified models for the most preferable clinical and administrative policies.

Internal patient, clinical, and administrative data will be available from separate hospital information systems. Industry associations and other reporting services can provide selected comparable data for competing hospitals. An embedded executive information system (EIS) is used to filter the internal and external data, form HMSS's database, focus the filtered information, and communicate CE problems, opportunities, and issues among affected personnel. Expert systems (ES) guide the CE team, CE coordinator, and other interested clinicians and administrators through the intelligent modeling and the model-base, database, and knowledgebase management needed for the EIS and DSS analyses and evaluations.

Outputs. By controlling processing tasks in the desired way, the user can generate:

1. visually attractive tabular and graphic CE status reports that describe the hospital's clinical and administrative environment, track meaningful trends, and display important patterns,

2. market condition forecasts,

3. CE policy simulation results, and

4. recommended clinical and administrative actions.

The system also depicts, in a graphic manner, the reasoning (explanations and supporting knowledge) that leads to the suggested actions.

Feedback loops. Feedback from the processing provides additional data, knowledge, and enhanced decision models that may be useful for future concurrent engineering activities and tasks. Output feedback (often in the form of sensitivity analyses) is used to extend or modify the original analyses and evaluations. All processing (including each feedback loop) is done in a very friendly manner, with artificial intelligence (mainly expert system) technology, that meets the decision styles and requirements of participating personnel.

Concurrent engineering support. The HMSS delivers the information and knowledge needed to support concurrent engineering decision making in a comprehensive, integrated, and continuous fashion. The embedded EIS (perhaps with the aid of an embedded ES) helps the user discern strategic problems or opportunities and gather pertinent information. CE team representatives, a CE coordinator, and other interested clinicians and administrators can utilize the information with the base DSS (perhaps with the aid of another embedded ES) to generate task, event, and process alternatives, establish criteria, and formulate relevant qualitative and quantitative models. These models can be used with the base DSS and another embedded ES to help the participating personnel evaluate the alternatives and select an action that achieves hospital, rather than individual department, objectives. Another ES can provide explanations to help clinicians and administrators gain confidence in, and execute, the decision. After the decision is implemented (on an actual or simulated basis), CE team representatives, a CE coordinator, and interested administrators and clinicians will want to observe the new reality and follow through with concurrent engineering. The interactive feedback loops of the HMSS make it relatively easy for participating personnel to support CE in this continuous manner.

Decision value. In theory, the comprehensive, integrated, and continuous CE support from the HMSS should yield more decision value than the nonsynthesized and partial support offered by any single autonomous system. Improvements should be observed in both the outcomes from, and the process of, strategic hospital decision making. Outcome improvements can include advancements in the level of the users' decision making maturity and gains in organization performance $[13,41]$ . A mature decision maker will expend considerable effort on, and be capable of, defining the problem, exploring the interpretation's relationship to alternative views, and generating alternative solution concepts $[55,60,72]$ . Process improvements can involve enhancements in the users' ability to perform the phases and steps of decision making $[57,66,69]$ .

## 3. Experiment

An experiment was developed to test the theory that an HMSS-like system can help nurses, physicians, and administrators improve the outcomes and process from strategic hospital decision making. In the experiment, a stand-alone decision support system was used to provide control group subjects with information and knowledge that partially supported concurrent engineering. Experimental group subjects used a HMSS-like system to generate additional information and knowledge that more fully supported concurrent hospital engineering. Decision outcome and process measures from the experimental group were compared with the analogous results from the control group.

The study adapted Simon's decision making framework into a process scheme with the following phases and steps:

1. Intelligence - observe objectives, recognize problems, gather qualitative data, and gather quantitative data;

2. Design - generate alternatives and establish criteria;

3. Choice - evaluate alternatives and choose the final alternative; and

4. Implementation - implement the final choice, express a degree of confidence in the decision, and rate the overall effectiveness of the support system.

## 3.1. Subjects

As in previous DSS, EIS, and ES studies, the health care experiment utilized students and professionals as subjects $[4,35,38,68]$ . The original design called for a single sample involving a representative mix of nurses, physicians, and administrators (the major hospital decision makers). Budgetary, logistical, and timing considerations necessitated an experiment that consisted of three independent samples. One sample involved physicians enrolled in a graduate public health policy course at a major private university; another included nurses taking a graduate health care administration course at a major public university; and the third engrossed executives at a regional hospital [29]. Table 1 briefly describes these samples and summarizes the modal characteristics of their volunteer subjects.

Student subjects were solicited by the participating course professors. A few students in each class did not appear for the experiment, one because of an emergency, and no demographic (or other) information was available for these no shows. All other class members participated in return for feedback on their competitive performance and for exposure to decision technologies. Experiments were conducted during hours usually allocated as lab sessions in the courses, and competitive feedback was provided one week after the completion of the experiments.

Practitioner subjects were chosen at random by a stratified sample of hospital decision makers. After selection, these subjects were approached by one of the researchers, who also works for the hospital, and asked to participate in exchange for feedback on their performance and for exposure to decision technologies. All solicited subjects

Table 1
MSS Experiments

<table><tr><td rowspan="2">Experiment</td><td rowspan="2">Subjects (number)</td><td colspan="6">Demographics</td></tr><tr><td>Age</td><td>Sex</td><td>Major</td><td>GPA (mean)</td><td>Experience</td><td>Field</td></tr><tr><td>A. Physicians enrolled in a graduate program in Public Health at Johns Hopkins University</td><td>20</td><td>above 40 years</td><td>F:13 M:7</td><td>Public Health</td><td>3.57</td><td>Above 10 years</td><td>Medicine</td></tr><tr><td rowspan="2">B. Graduate students enrolled in Nursing Administration program at the University of Maryland, Baltimore(UMAB)</td><td rowspan="2">19</td><td>30–35 years</td><td>F:18 M:1</td><td>Nursing Admn</td><td>3.78</td><td>Above 10 years</td><td>Nursing</td></tr><tr><td>Above 40 years (bimodal)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>C. Practitioners in healthcare at Saint Joseph Hospital, Towson, Maryland</td><td>20</td><td>above 40 years</td><td>F:9 M:11</td><td>Other *</td><td>3.32</td><td>Above 10 years</td><td>Health Admn /Policy</td></tr></table>

\* Not Applicable

agreed to participate. The experiment was conducted during normal business hours, and competitive feedback was provided immediately after the completion of the experiments.

## 3.2. Research plan

Each experiment followed a research plan adapted from schemes applied successfully in related studies [1-3,10,46]. Fig. 4 outlines this plan.

Group assignments. Subjects were introduced to the study through an oral presentation and a supplemental summary document. At a later date, a formal lecture was given about the hospital simulation, the variable to outcome relationships, the decision making process, and the role of information systems in the process. The lecture was augmented with written instructions. Next, a questionnaire was used to collect data on the subjects' demographic characteristics, and subjects were assigned, in a demographically balanced and random manner, to an experimental and a control group. Chi-square goodness of fit tests verified (at the $\alpha = 0.05$ level) that the two groups had the same demographic composition. Then, experiments were run on the experimental and control groups.

![](/api/attachments/PK2G57E4/fulltext/images/a88d4cab11d25d26a67a7446443f9d02b87d5810ac95339fa3207fab107ea30b.jpg)  
Fig. 4. Research plan.

Decision situation. As in previous DSS and EIS studies, subjects were challenged with a complex, semi-structured management problem. In both the experimental and control groups, every subject was required to set the levels of 9 decision variables and to forecast the levels of 4 environmental variables. Decision variables included emergency room fees, outpatient fees, the number of nurses, the salary of nurses, and the supplier pay period, while the environmental variables consisted of the projected inflation rate and occupancy projections in three clinical specialties. The 13 variables jointly influenced the financial performance of a simulated hospital. Twenty-six (26) additional variables were fixed from trial to trial and thereby became the scenario for decision making. The objective of the problem was to maximize financial performance, as measured by the return on revenue (ROR).

Information technology support. An information system was provided to support the decision making. By using this system, a subject could input decisions and environmental forecasts and get an instant report on the resulting revenue, profit (or loss), return on revenue (ROR), and other financial outcomes. Written instructions were given on the use of the information system, and assistants were available to help subjects operate the computer hardware and software. Subjects competed against each other, and they were aware of the competition. Participants were allowed to run as many trials as desired in a single 90-minute session, but only the end-of-simulation results were recorded for, and counted in, the competition and statistical testing. Subjects were conscious of these rules.

Data capture. Immediately after the 90-minute session, end-of-simulation results were captured electronically in a data file. While still at the computer terminals, and without delay, every subject in each group was given two questionnaires.

The first questionnaire requested: (a) demographic data, (b) a record of the time expended, number of problems and opportunities identified, and the number of alternatives generated during the simulations, and (c) open-ended responses about the subject's decision making process. To preserve anonymity, open-ended written responses were later transcribed into typed form and identified by a four-digit code by one of the researchers. The second questionnaire asked the subject to rate, on a five-point Likert scale with least helpful to most helpful anchors, the information system's usefulness in supporting the user's ability to perform the steps from the adapted Simon scheme of decision making. An item analysis on this second questionnaire's components verified (with a Cronbach's $\alpha = 0.85$ ) that the instrument reliably measured the subjects' self-ratings. Subjects had full access to the information system and their decisions as they completed the questionnaires.

Later, the code-identified, transcribed open-ended responses from the first questionnaire were given to three experts for independent grading. To prevent bias, no information was provided to the experts about the identity of, demographics of, or information system utilized by the subjects. The experts were executives for regional health care institutions with much experience in the type of decision making entailed in the hospital simulation. After receiving a briefing on the decision making process and a walkthrough of the experiment, the experts were asked to rate, on a 25-point scale, the subject's ability to perform each of the four general phases of decision making (intelligence, design, choice, and implementation). Rating was limited to phases, rather than steps, because of the difficulty involved in accurately assessing step prowess from the open-ended responses. An analysis of 8 responses from a pre-experiment pilot study verified (with a Kappa coefficient = 0.83) the experts' inter-grader reliability.

Statistical summaries. Collected outcome data were metric, but demographic data were categorical (nonmetric), in nature. The gathered process data (subjects' Likert-scaled self-ratings and experts' 25-point-scaled ratings) data were arguably interval-scaled and thereby metric in character [12,15]. Nonmetric data were summarized with frequency distributions and crosstabulations. Chi-square, Fisher's test, and Spearman correlation analyses of the crosstabulated data were used to test the hypotheses that the three (physician, nurse, and administrator) samples had the same demographic (age, experience, gender, and GPA) composition. The metric data were summarized with measures of central tendency and dispersions, and expert ratings were summed to form a cumulative (75-point-scaled) score for each subject on each phase of decision making. Multivariate analyses of the metric data were used to test the hypotheses that the outcome and process measures were each independent of the study group. The SPSS for Windows computer package was used to perform the descriptive and inferential statistical analyses [47].

## 3.3. Information systems

Each subject in the control group was given a decision support system (DSS), delivered through popular spreadsheet-based StratPlan software, to support the simulated hospital decision making. Although the software is tailored specifically for health care management, StratPlan is similar in architecture and usage to the decision support systems utilized in previous DSS studies. This health-care-management-specific DSS has: (a) a database that captures and stores clinical and administrative data, and (b) a modelbase of mathematical expressions that describes the relationships between the decision and environmental variables and the measures of financial performance. By making selections from display screen menus, subjects could input the decision variables, forecast the environmental variables, obtain financial status reports, and perform sensitivity analyses. Such analyses and evaluations assist users in arriving at a recommended policy (set of decision variables) for the simulated hospital.

Subjects in the experimental group were provided with a HMSS-like management support system (MSS). In this MSS, the StratPlan-based DSS was enhanced with Windows-based executive information (EIS) and expert (ES) systems. Since

StratPlan is a DOS program, the MSS could not take advantage of Windows' dynamic data exchange (DDE) feature to "hotlink" the components. Instead, subjects utilized Windows' task-switching and Clipboard capabilities to move among the components.

EIS component. The executive information system component was delivered through the popular EIS product Forest and Trees. Like the executive information systems in previous EIS studies, this Forest and Trees-delivered EIS allowed subjects to access and report data pertinent to the management problem's decisions. In the simulated hospital situation, these data included: (a) national figures on healthcare spending and return on revenue, and (b) local information on average nursing salaries, admissions, average length of stay (ALOS) for various specialties, occupancy rates, and other clinical and administrative statistics for five competing area hospitals. By selecting a topical folder, the subject could quickly search for the desired summary information. Each folder had further linked views that enabled the user to drill-down to supporting detail in tabular or graphic form. An explanation about the relevance of the selected variable and about the source of the provided data was available through a Clipboard icon in the EIS.

ES component. The expert system component was delivered through the popular ES development shell Level 5 Object. Like the expert systems in previous ES studies, this Level 5 Object-delivered ES acted as an electronic counselor to the user. A hybrid object-production rule knowledge base captured and stored clinical and administrative decision making expertise elicited from experienced, local hospital executives. These executives included a Director of Nursing, a Senior Director of Finance, a Director of Financial Planning, and a Vice President of Personnel. Upon entrance, the ES prompted the subject for information about the hospital and its environment. Completed responses triggered the ES' chaining-based inference engine to display professional advice on some (but not all) of the decision variables. The advice consisted of the recommended: (a) clinical specialties, (b) number of nurses, and (c) supplier pay period days. By selecting the ES' Expand menu item, the user could get an explanation for the prompts and ensuing recommendations.

## 3.4. Concurrent engineering support

The StratPlan-based DSS provides some information and knowledge needed to partially support concurrent engineering decision making. With the DSS, the user can specify decision and environmental variables and have the embedded model measure the impact of the actions on the financial performance of the simulated hospital (organization modeling for choice). However, the system does not provide data access and reporting for intelligence, organization modeling for design, and knowledge delivery for choice and implementation. As would be the case in practice, it was the subjects' responsibility to recognize the importance of, and informally locate, retrieve and interpret, the vital CE information and knowledge undelivered by the DSS.

The MSS delivers the information and knowledge needed to enable concurrent engineering decision making for the simulated hospital in a comprehensive, integrated, and continuous fashion. The embedded EIS helps users discern staffing, pricing, and financial problems or opportunities and gather pertinent clinical and administrative information (data access and reporting for intelligence). Users can utilize the information with the base DSS (with the aid of the embedded ES and EIS) to generate clinical specialty, nursing staff, and supplier pay period alternatives and to establish the environmental variable levels for the simulation model (organization modeling design). These operationalized models can be used with the base DSS and the embedded ES to help decision makers evaluate the alternatives and select the best alternative (organization modeling and knowledge delivery for choice). The EIS and ES can provide explanations to help users gain confidence in, and execute, the decision (knowledge delivery for implementation). After the decision is implemented on a trial basis, the user will want to observe the new reality and follow through with intelligence, design, choice, and implementation. The interactive feedback loops of the MSS make it relatively easy for the user to perform the consequent sensitivity analyses and other post-trial evaluations.

## 3.5. Decision value

As in previous DSS, EIS, and ES studies, decision value was assessed by the system's separate effects on the outcomes (level of maturity and organization performance) from, and the process (ability to perform the phases and steps) of, decision making.

Outcomes. Hospital performance was assessed with the return on revenue (ROR). However, since StratPlan allows unbounded decision and environmental variables, subjects could make unrealistic decisions and inadvertently get RORs impractically above (or below) the hospital industry standard of 5 to 7 %. For this reason, distance from the industry standard, as measured by the absolute difference between the observed return on revenue and the 6% midpoint of the standard (RORX), was judged to be the relevant gauge of hospital performance.

A mature hospital decision maker will expend considerable effort on, and be capable of, defining the management problem, exploring the interpretation's relationship to alternative views, and generating alternative clinical and administrative solution concepts. Effort was assessed by the time (in minutes) spent on the simulated decision making (TIME). Capability was measured by the numbers of opportunities (OPP) and problems (PROB) identified during the simulation, and the number of alternatives generated during the simulation (ALT).

Process. Cumulative expert ratings measured the subject's ability to perform the four general decision making phases of intelligence (PHASE1), design (PHASE2), choice (PHASE3), and implementation (PHASE4). Self-ratings assessed the usefulness of the system in supporting the subject's ability to perform the identifying objectives (IDENTIFY), recognizing problem or opportunity (RECGNIZE), gathering qualitative data (QUAL\_GAT), gathering quantitative data (QUAN\_GAT), generating alternatives (OBSERVE), establishing criteria (ESTABLSH), evaluating alternatives (EVALUATE), choosing the final alternative (CHOOSE), decision confidence (CONFIDNT), system effectiveness (EFFECT), and implementing the final choice (IMPLEMENT) steps of the decision making process.

## 4. Experimental results

Experimental results were used to assess the management support system's impact on the outcomes from, and process of, simulated hospital decision making. As in related studies, separate hypotheses were examined for outcome and process effects.

## 4.1. Research questions and hypotheses

The fundamental research question and corresponding hypotheses for outcome effects can be stated as follows:

Question: Can the MSS improve decision making outcomes?

Null: The MSS and DSS outcomes are the same.

Alternative: The MSS results in different outcomes than the DSS.

The fundamental research question and corresponding hypotheses for process effects can be stated as follows:

Question: Can the MSS improve the decision making process?

Null: Process ratings are the same for MSS and DSS users.

Alternative: Process ratings are different for MSS than DSS users.

## 4.2. Outcome and process functions

Neither information system generated a computer log that could be checked for feature usage during simulation trials. However, an examination of the end-of-simulation computer printouts showed that:

(a) all subjects in the control group utilized the DSS,

(b) all subjects in the experimental group used the DSS, EIS, and ES components of the MSS, and

(c) all of the subjects in the experimental group asked for, and virtually all accepted, the EIS and ES recommendations.

Hence, it was unnecessary to distinguish experimental group subjects by their feature usage.

Since the groups differed only by the information systems provided to the subjects, the control group served as a proxy for the DSS and the experimental group was a surrogate for the MSS. Outcome and process effects then were functions of the group (GROUP) and any other moderating factors, or

Outcomes = f(GROUP, Moderating Factors)

and

Process Ratings

= f(GROUP, Moderating Factors)

and the hypotheses could be tested through the statistically estimated parameters of the pertinent functions.

## 4.3. Moderating factors

In this study, demographics were the only surveyed factors that can moderate the influence of the information systems on outcomes and process ratings. The control and experimental groups had statistically equivalent age, sex, work experience, and GPA compositions. Moreover, Chi-square goodness of fit tests verified (at the $\alpha = 0.05$ level) that the three (nurse, physician, and administrator) samples had the same compositions with respect to these same demographic factors. Consequently, while the small sample sizes precluded definitive statistical testing, it seemed reasonable to assume that age, sex, work experience, and GPA would have no moderating effects on outcomes or process ratings.

The remaining demographic factor was the type of the health care professional (physician, nurse, or administrator). Each sample had a different, but the experimental and control groups had the same, professional type. This demographic factor, as proxied by the sample number (EXP\_NUM), then could have a moderating effect on the dependent variables, or

Outcomes

by GROUP)

and

Process Ratings

$= \mathrm{f}(\mathrm{GROUP},\mathrm{EXP\_NUM},\mathrm{EXP\_NUM}$

by GROUP)

Namely, outcomes and process ratings were functions of group (and thereby the information system provided to the subjects), the type of health care professional, and any interaction between the professional type and the provided information system.

## 4.4. Hypothesis testing

Since outcomes and process ratings were metric, MANOVA seemed to be an appropriate procedure to statistically test the hypotheses. Several diagnostics were conducted to ensure that this procedure was appropriate for the experiment.

Diagnostics. Bartlett-Box F and Cochrans C univariate tests indicated that the homogeneity-of-variance assumption was valid with respect to: (a) most (but not all) of the outcome variables, (b) most (but not all) of the process phase variables, and (c) most (but not all) of the process step variables. The Bartlett test for sphericity demonstrated that there was significant correlation: (a) among the outcome variables, (b) among the process phase measures, and (c) among the process step variables. Box's M multivariate tests suggested that the homogeneity-of-variance assumption was valid with respect to the process phase, but not the outcome and process step, variables.

According to the diagnostics, there were some variations from the equal variance assumption. Yet, MANOVA is reasonably robust with respect to minor assumption variations, and the procedure is more powerful (and generates more information) statistically than its nonparametric counterparts $[26,65]$ . For these reasons, the hypotheses were tested with MANOVA.

As a precaution, the outcome and process variables were recoded into nonmetric categories, and these recoded variables were crosstabulated against GROUP and EXP\_NUM for hypothesis testing purposes. Loglinear analyses and Chi-square goodness-of-fit tests of the crosstabulated data yielded results that were essentially the same as the MANOVA findings.

Table 2
Manova outcome statistics

<table><tr><td>Outcome variable</td><td>Factor Group</td><td>EXP_NUM</td><td>EXP_NUM by group</td></tr><tr><td>Multivariate</td><td>1.44311(0.000)</td><td>0.40344(0.106)</td><td>0.09333(0.951)</td></tr><tr><td>RORX</td><td>19.36516(0.000)</td><td>1.15727(0.324)</td><td>0.90869(0.411)</td></tr><tr><td>ALT</td><td>9.63289(0.003)</td><td>3.81121(0.029)</td><td>0.36855(0.694)</td></tr><tr><td>OPP</td><td>2.67940(0.109)</td><td>3.21088(0.050)</td><td>0.53631(0.589)</td></tr><tr><td>PROB</td><td>2.54224(0.118)</td><td>0.16923(0.845)</td><td>0.14290(0.867)</td></tr><tr><td>TIME</td><td>10.19530(0.003)</td><td>0.42590(0.656)</td><td>0.07292(0.930)</td></tr></table>

Notes: The multivariate row reports the Hotelling's T $^{2}$ for multivariate significance, while the other rows show the Roy-Bargman stepdown F tests for the individual outcome variable significance. In each case, the significance level is shown in parentheses below the reported statistic.

MANOVA tests. Pillais, Wilks, Roys, and Hotellings T $^{2}$ statistics were used to test for the multivariate equality of mean outcomes. The same statistics were used to perform analogous multivariate process phase and step tests. In every case, the Pillais, Wilks, Roys, and Hotellings tests yielded identical results. Bonferroni simultaneous confidence intervals and Roy–Bargman stepdown F statistics were used to isolate separate dependent variable differences. Each of these analyses generated the same results.

## 4.5. Findings

Hotellings and Roy-Bargman statistics, with significance levels in parentheses, are reported in Table 2 for the outcome variables, in Table 3 for the process phase measures, and in Table 4 for the process step variables.

Outcome differences. The statistics in Table 2 indicate that (at the $\alpha = 0.05$ level of significance):

Table 3  
Manova process phase statistics

<table><tr><td>Process phase variable</td><td>Factor Group</td><td>EXP_NUM</td><td>EXP_NUM by group</td></tr><tr><td>Multivariate</td><td>1.72743(0.000)</td><td>0.41192(0.034)</td><td>0.27073(0.186)</td></tr><tr><td>PHASE1</td><td>20.48834(0.000)</td><td>0.30364(0.740)</td><td>0.66885(0.517)</td></tr><tr><td>PHASE2</td><td>2.89049(0.096)</td><td>2.53937(0.090)</td><td>2.13806(0.129)</td></tr><tr><td>PHASE3</td><td>7.48778(0.009)</td><td>5.34617(0.008)</td><td>1.81473(0.175)</td></tr><tr><td>PHASE4</td><td>23.41613(0.000)</td><td>0.83956(0.439)</td><td>1.25035(0.296)</td></tr></table>

Notes: The multivariate row reports the Hotelling's T $^{2}$ for multivariate significance, while the other rows show the Roy-Bargman stepdown F tests for the individual outcome variable significance. In each case, the significance level is shown in parentheses below the reported statistic.

1. the information system provided to the subjects (GROUP) had a significant effect on outcomes;

2. the information system provided to the subjects (GROUP) had a significant effect on the proximity of ROR to the industry standard (RORX), on the number of alternatives generated (ALT), and on the effort expended (TIME) during simulated decision making;

3. the information system provided to the subjects (GROUP) had no significant effect on the number of opportunities (OPP) or on the number of problems (PROB) identified during the simulated decision making;

4. the subject's professional type (EXP\_NUM) had no significant effect on outcomes; and

5. the interaction between the professional type and the provided information system (EXP\_NUM by GROUP) had no significant effect on outcomes.

In summary, hospital performance and two measures of decision making maturity level were different for MSS than DSS users. These findings generally support the hypothesis that the MSS results in different outcomes than the DSS.

Process phase differences. The statistics in Table 3 indicate that (at the $\alpha = 0.05$ level of significance):

1. the information system provided to the subjects (GROUP) had a significant effect on process phase ratings;

2. the information system provided to the subjects (GROUP) had a significant effect on the intelligence (PHASE1), choice (PHASE3), and implementation (PHASE4) phases of simulated hospital decision making;

3. the information system provided to the subjects (GROUP) had no significant effect on the design (PHASE2) phase of simulated hospital decision making;

4. the subject's professional type (EXP\_NUM) had a significant independent effect on process phase ratings, but the effect was limited to the choice (PHASE3) phase of simulated hospital decision making; and

Table 4  
Manova process step statistics

<table><tr><td>Outcome variable</td><td>Factor Group</td><td>EXP_NUM</td><td>EXP_NUM by group</td></tr><tr><td>Multivariate</td><td>1.80638(0.000)</td><td>1.12423(0.028)</td><td>0.96282(0.077)</td></tr><tr><td>IDENTIFY</td><td>2.33777(0.134)</td><td>1.06461(0.354)</td><td>5.05604(0.011)</td></tr><tr><td>RECGNIZE</td><td>4.69616(0.037)</td><td>0.16189(0.851)</td><td>0.06711(0.935)</td></tr><tr><td>QUAL_GAT</td><td>3.81495(0.058)</td><td>2.20025(0.124)</td><td>2.07926(0.139)</td></tr><tr><td>QUAN_GAT</td><td>0.97642(0.329)</td><td>5.32739(0.009)</td><td>0.77461(0.468)</td></tr><tr><td>OBSERVE</td><td>5.83698(0.020)</td><td>0.75836(0.475)</td><td>1.80151(0.178)</td></tr><tr><td>ESTABLSH</td><td>0.01666(0.898)</td><td>2.54267(0.090)</td><td>0.22922(0.796)</td></tr><tr><td>EVALUATE</td><td>8.40786(0.006)</td><td>0.502(0.609)</td><td>1.48513(0.238)</td></tr><tr><td>CHOOSE</td><td>11.84281(0.001)</td><td>3.76532(0.030)</td><td>2.46309(0.096)</td></tr><tr><td>CONFIDNT</td><td>3.93119(0.053)</td><td>2.8574(0.068)</td><td>2.05326(0.140)</td></tr><tr><td>EFFECT</td><td>5.40586(0.025)</td><td>0.20065(0.819)</td><td>0.06114(0.941)</td></tr><tr><td>IMPLEMENT</td><td>0.17208(0.680)</td><td>0.17892(0.837)</td><td>1.35775(0.269)</td></tr></table>

Notes: The multivariate row reports the Hotelling's $T^{2}$ for multivariate significance, while the other rows show the Roy-Bargman stepdown F tests for the individual outcome variable significance. In each case, the significance level is shown in parentheses below the reported statistic.

5. the interaction between the professional type and the provided information system (EXP\_NUM by GROUP) had no significant effect on process phase ratings.

In summary, expert ratings on three phases of decision making were different for MSS than DSS users. These findings generally support the hypothesis that process phase ratings are different for MSS than DSS users.

Process step differences. The statistics in Table 4 indicate that (at the $\alpha = 0.05$ level of significance):

1. the information system provided to the subjects (GROUP) had a significant effect on process step ratings;

2. the information system provided to the subjects (GROUP) had a significant effect on the recognizing problem or opportunity (RECGNIZE), generating alternatives (OBSERVE), evaluating alternatives (EVALUATE), choosing the final alternative (CHOOSE), and system effectiveness (EF-FECT) steps of the hospital decision making process;

3. the information system provided to the subjects (GROUP) had no significant effect on the identifying objectives (IDENTIFY), gathering qualitative data (QUAL\_GAT), gathering quantitative data (QUAN\_GAT), establishing criteria (ESTABLSH), decision confidence (CONFIDNT), and implementing the final choice (IMPLEMET) steps of the hospital decision making process;

4. the subject's professional type (EXP\_NUM) had a significant independent effect on process step ratings, but the effect was limited to the gathering quantitative data (QUAN\_GAT) and choosing the final alternative (CHOOSE) steps of simulated hospital decision making; and

5. the interaction between the professional type and the provided information system (EXP\_NUM by GROUP) had no significant effect on process step ratings.

Table 5  
Group means for outcome and process variables

<table><tr><td rowspan="2">Variable</td><td colspan="2">System provided (group)</td></tr><tr><td>DSS</td><td>MSS</td></tr><tr><td colspan="3">Outcomes</td></tr><tr><td>ROR distance from industry standard (RORX)</td><td>17.306</td><td>3.186</td></tr><tr><td>Number of alternatives generated (ALT)</td><td>2.107</td><td>3.200</td></tr><tr><td>Number of opportunities identified (OPP)</td><td>1.607</td><td>2.375</td></tr><tr><td>Number of problems identified (PROB)</td><td>1.893</td><td>2.520</td></tr><tr><td>Time spent on decision making (TIME)</td><td>46.929</td><td>55.679</td></tr><tr><td colspan="3">Process phases</td></tr><tr><td>Intelligence (PHASE1)</td><td>45.411</td><td>58.920</td></tr><tr><td>Design (PHASE2)</td><td>46.268</td><td>61.640</td></tr><tr><td>Choice (PHASE3)</td><td>41.768</td><td>58.480</td></tr><tr><td>Implementation (PHASE4)</td><td>34.500</td><td>54.860</td></tr><tr><td colspan="3">Process steps</td></tr><tr><td>Identifying objectives (IDENTIFY)</td><td>2.714</td><td>3.962</td></tr><tr><td>Recognizing problems/opportunities (RECGNIZE)</td><td>2.571</td><td>3.885</td></tr><tr><td>Gathering qualitative data (QUAL_GAT)</td><td>3.179</td><td>4.360</td></tr><tr><td>Gathering quantitative data (QUAN_GAT)</td><td>2.036</td><td>3.720</td></tr><tr><td>Generating alternatives (OBSERVE)</td><td>3.071</td><td>3.615</td></tr><tr><td>Establishing criteria (ESTABLSH)</td><td>2.571</td><td>3.800</td></tr><tr><td>Evaluating alternatives (EVALUATE)</td><td>2.786</td><td>4.200</td></tr><tr><td>Choosing the final alternative (CHOOSE)</td><td>2.786</td><td>3.880</td></tr><tr><td>Decision confidence (CONFIDNT)</td><td>2.929</td><td>4.000</td></tr><tr><td>System effectiveness (EFFECT)</td><td>2.929</td><td>4.320</td></tr><tr><td>Implementing the final choice (IMPLEMET)</td><td>2.643</td><td>3.520</td></tr></table>

In summary, subject self-ratings on five steps of decision making were different for MSS than DSS users. These findings generally support the hypothesis that process step ratings are different for MSS than DSS users.

Decision value. Control (DSS) versus experimental (MSS) group means for the outcome, process phase, and process step variables are given in Table 5. The statistics in Table 5 indicate that:

1. MSS users had a smaller mean distance of ROR from the industry standard (RORX), a larger mean number of alternatives generated (ALT), and a larger mean effort expended (TIME) during simulated decision making than DSS users;

2. MSS users had larger mean expert ratings than DSS users on the intelligence (PHASE1), choice (PHASE3), and implementation (PHASE4) phases of simulated hospital decision making; and

3. MSS users had larger mean self ratings than DSS users on the recognizing problem or opportunity (RECGNIZE), generating alternatives (OBSERVE), evaluating alternatives (EVALUATE), choosing the final alternative (CHOOSE), and system effectiveness (EFFECT) steps of the hospital decision making process.

These results plus the MANOVA conclusions support the general finding that the MSS results in better decision value (superior outcomes from, and an improved process of, simulated hospital decision making) than the DSS.

Professional type. Table 6 reports the outcome, process phase, and process step means for the subject's professional type (EXP\_NUM). Although there was no significant interaction between the professional type and the provided information system (EXP\_NUM by GROUP), Table 7 shows the corresponding outcome and process means for reference. The statistics in Table 6 indicate that:

1. administrators had larger mean expert ratings than either nurses or physicians on the choice (PHASE3) phase of simulated hospital decision making;

Table 6  
Professional type outcome and process means

<table><tr><td rowspan="2">Variable</td><td colspan="3">Type of professional (EXP_NUM)</td></tr><tr><td>Physicians</td><td>Nurses</td><td>Administrators</td></tr><tr><td colspan="4">Outcomes</td></tr><tr><td>RORX</td><td>11.4665</td><td>8.2646</td><td>9.8496</td></tr><tr><td>ALT</td><td>2.2000</td><td>2.3158</td><td>3.2632</td></tr><tr><td>OPP</td><td>1.400</td><td>2.2632</td><td>2.1111</td></tr><tr><td>PROB</td><td>2.000</td><td>2.4211</td><td>2.1053</td></tr><tr><td>TIME</td><td>50.0000</td><td>52.0000</td><td>51.7500</td></tr><tr><td colspan="4">Process phases</td></tr><tr><td>PHASE1</td><td>49.5000</td><td>52.6053</td><td>52.6000</td></tr><tr><td>PHASE2</td><td>50.3571</td><td>51.2105</td><td>57.9250</td></tr><tr><td>PHASE3</td><td>39.8571</td><td>52.5263</td><td>53.7750</td></tr><tr><td>PHASE4</td><td>42.0000</td><td>44.7368</td><td>44.9750</td></tr><tr><td colspan="4">Process steps</td></tr><tr><td>IDENTIFY</td><td>2.9333</td><td>3.5263</td><td>3.4000</td></tr><tr><td>RECGNIZE</td><td>2.6667</td><td>3.4211</td><td>3.4000</td></tr><tr><td>QUAL_GAT</td><td>3.4286</td><td>4.1579</td><td>3.5500</td></tr><tr><td>QUAN_GAT</td><td>2.7857</td><td>2.7368</td><td>2.9500</td></tr><tr><td>OBSERVE</td><td>2.6000</td><td>3.6842</td><td>3.5500</td></tr><tr><td>ESTABLSH</td><td>2.2857</td><td>3.5789</td><td>3.3500</td></tr><tr><td>EVALUATE</td><td>2.8571</td><td>3.7895</td><td>3.5500</td></tr><tr><td>CHOOSE</td><td>2.7143</td><td>3.7368</td><td>3.3000</td></tr><tr><td>CONFIDNT</td><td>3.0000</td><td>4.0000</td><td>3.2000</td></tr><tr><td>EFFECT</td><td>3.0714</td><td>4.0526</td><td>3.5000</td></tr><tr><td>IMPLEMET</td><td>2.5714</td><td>3.4737</td><td>3.0000</td></tr></table>

2. administrators had larger mean self ratings than either nurses or physicians on the gathering quantitative data (QUAN\_GAT) step of simulated hospital decision making; and

3. nurses had larger mean self ratings than either administrators or physicians on the choosing the final alternative (CHOOSE) step of simulated hospital decision making.

These results plus the MANOVA conclusions support the general finding that administrators had little, if any, native decision making superiority over clinicians (nurses and physicians).

## 5. Conclusions

Concurrent engineering (CE) can facilitate Total Quality Management (TQM) and help a hospital realize its strategic objectives. To achieve these benefits, clinical and administrative information and knowledge must be shared in a systematic, complete, integrated, and timely manner among the affected decision makers. A hospital must meet significant organizational and information technology support challenges to promote the free flow of the necessary information and knowledge.

Table 7  
Interaction outcome and process means

<table><tr><td rowspan="3">Variable</td><td colspan="6">Interaction (EXP_NUM by group)</td></tr><tr><td colspan="2">Physicians</td><td colspan="2">Nurses</td><td colspan="2">Administrators</td></tr><tr><td>DSS</td><td>MSS</td><td>DSS</td><td>MSS</td><td>DSS</td><td>MSS</td></tr><tr><td colspan="7">Outcomes</td></tr><tr><td>RORX</td><td>18.281</td><td>6.923</td><td>13.468</td><td>1.109</td><td>21.130</td><td>0.619</td></tr><tr><td>ALT</td><td>1.875</td><td>2.571</td><td>1.727</td><td>3.125</td><td>2.777</td><td>3.700</td></tr><tr><td>OPP</td><td>1.250</td><td>1.571</td><td>1.909</td><td>2.750</td><td>1.555</td><td>2.666</td></tr><tr><td>PROB</td><td>1.750</td><td>2.285</td><td>2.181</td><td>2.750</td><td>1.667</td><td>2.500</td></tr><tr><td>TIME</td><td>44.375</td><td>55.000</td><td>48.090</td><td>57.375</td><td>47.777</td><td>55.000</td></tr><tr><td colspan="7">Process Phases</td></tr><tr><td>PHASE1</td><td>43.750</td><td>57.167</td><td>48.591</td><td>58.125</td><td>43.000</td><td>60.454</td></tr><tr><td>PHASE2</td><td>44.750</td><td>57.833</td><td>43.500</td><td>61.812</td><td>51.000</td><td>63.591</td></tr><tr><td>PHASE3</td><td>30.500</td><td>52.333</td><td>49.182</td><td>57.125</td><td>42.722</td><td>62.818</td></tr><tr><td>PHASE4</td><td>30.375</td><td>57.500</td><td>37.818</td><td>54.250</td><td>34.111</td><td>53.864</td></tr><tr><td colspan="7">Process Steps</td></tr><tr><td>IDENTIFY</td><td>2.250</td><td>3.714</td><td>3.454</td><td>3.625</td><td>2.222</td><td>4.364</td></tr><tr><td>RECGNIZE</td><td>2.000</td><td>3.429</td><td>3.273</td><td>3.625</td><td>2.222</td><td>4.364</td></tr><tr><td>QUAL_GAT</td><td>3.250</td><td>3.667</td><td>3.909</td><td>4.500</td><td>2.222</td><td>4.636</td></tr><tr><td>QUAN_GAT</td><td>2.250</td><td>3.500</td><td>2.091</td><td>3.625</td><td>1.778</td><td>3.909</td></tr><tr><td>OBSERVE</td><td>2.625</td><td>2.571</td><td>3.909</td><td>3.375</td><td>2.444</td><td>4.454</td></tr><tr><td>ESTABLSH</td><td>2.125</td><td>2.500</td><td>3.182</td><td>4.125</td><td>2.222</td><td>4.273</td></tr><tr><td>EVALUATE</td><td>2.500</td><td>3.333</td><td>3.454</td><td>4.250</td><td>2.222</td><td>4.636</td></tr><tr><td>CHOOSE</td><td>2.500</td><td>3.000</td><td>3.454</td><td>4.125</td><td>2.222</td><td>4.182</td></tr><tr><td>CONFIDNT</td><td>2.875</td><td>3.167</td><td>3.727</td><td>4.375</td><td>2.000</td><td>4.182</td></tr><tr><td>EFFECT</td><td>2.750</td><td>3.500</td><td>3.636</td><td>4.625</td><td>2.222</td><td>4.546</td></tr><tr><td>IMPLEMET</td><td>2.125</td><td>3.167</td><td>3.364</td><td>3.625</td><td>2.222</td><td>3.636</td></tr></table>

The hospital management support system (HMSS) delivers the information and knowledge needed to bolster concurrent engineering decision making in a comprehensive, integrated, and continuous fashion. In theory, such CE support should yield more decision value than the non-synthesized and partial support offered by any single autonomous system. The results of this study support the theory by indicating that a HMSS-like system can significantly improve both the outcomes from, and process of, hospital decision making.

Although the HMSS shows promise, the concept needs further research. The empirical findings of this study suggest that such research should focus on: (a) enhancements to the prototype

HMSS, (b) integration strategies, and (c) measurement and testing issues.

The prototype HMSS did no better than the DSS in supporting the design phase and selected process (the identifying objectives, gathering qualitative and quantitative data, establishing criteria, decision confidence, and implementing the final choice) steps of the hospital decision making process. In comparison to the DSS, the prototype HMSS also did not improve the user's proficiency in identifying the numbers of hospital problems or opportunities.

There are several questions about the prototype HMSS suggested by the support deficiencies. Should the EIS and ES components each be embellished to offer more support for the design phase and the selected process steps of hospital decision making? Could the EIS and ES enhancements be interfaced more effectively within the HMSS to provide the missing support? Are there other system functions (such as creative thinking support) that could be embedded within the HMSS to deliver the required additional decision support? Will any or all of the embellishments and enhancements in the HMSS architecture improve the user's proficiency in identifying the numbers of hospital problems or opportunities? Experiments can be designed that will test these questions.

Additional research can focus on alternative integration strategies. The HMSS is based on a specific integration of DSS, EIS, and ES functions. A higher-level integration strategy can be adopted to test the research questions. Experiments can be designed that will comparatively evaluate the decision value of management support system (MSS), executive support system (ESS), intelligent DSS, and other integration strategies in enabling concurrent engineering for hospital decision making.

Additional research can center on measurement and testing issues. A composite indicator can be developed that will measure the information system's joint, rather than separate, impacts of process and outcome on decision value. Large and broad-based samples with stringent moderating factor designs can be used to confirm the original, and test the additional, hypotheses.

## References

[1] L. Adleman, Experiments, Quasi-experiments, and Case Studies: A Review of Empirical Methods for Evaluating Decision Support Systems, IEEE Transactions of Systems, Man and Cybernetics 21, No. 2 (1991) 293–301.

[2] J.G. Amor, J.M. Martinez-Selva, F. Roman and S. Zamora, Electrodermal Activity in Menstrual Cycle Phases: A Comparison of Within- and Between-Subjects Designs, International Journal of Psychophysiology 9 (1990) 39–47.

[3] D.P. Ashmos, R.R. McDaniel and D. Duchon, Differences in Perception of Strategic Decision-Making Processes: The Case of Physicians and Administrators, The Journal of Applied Behavioral Science 26, No. 2 (1990) 201–218.

[4] I. Benbasat and B.R. Nault, An Evaluation of Empirical Research in Managerial Support Systems, Decision Support Systems 6, No. 3 (1990) 203–226.

[5] L. Berman, M. Cullen and P.L. Miller, Automated Integration of External Databases: A Knowledge-Based Ap

proach to Enhancing Rule-Based Expert Systems, Proceedings of the Sixteenth Annual Symposium on Computer Applications in Medical Care, November 1992, (Baltimore, 1993) 227–233.

[6] H. Bliech and W.V. Slack, Designing a Hospital Information System: A Comparison of Interfaced and Integrated systems, M.D. Computing: Computers in Medical Practice 5, No. 9 (1992) 293–296.

[7] D. Burda, Study Rates U.S. Hospitals vs. Other Nations, Industries, Modern Healthcare 21, No. 40 (1991) 36–38.

[8] S. Butters and S. Eom, Decision Support Systems in the Healthcare Industry, Journal of Systems Management 43, No. 6 (1992) 28–31.

[9] F. Classon, Surface Mount Technology for Concurrent Engineering and Manufacturing (McGraw-Hill, New York, 1993).

[10] J.P. Clements, An Investigation of the Effectiveness of Information Systems on the Creative Aspects of Managerial Decision Making, Unpublished Dissertation, University of Maryland, Baltimore (1993).

[11] R.C. Creese and L.T. Moore, Cost Modeling for Concurrent Engineering, Cost Engineering 32, No. 6 (1990) 23–27.

[12] J.W. Creswell, Research Design: Qualitative and Quantitative Approaches (Sage, Thousand Oaks, 1994).

[13] W.H. DeLone and E.R. McLean, Information Systems Success: The Quest for the Dependent Variable, Information Systems Research 3, No. 1 (1992) 61–95.

[14] C. Dyer, Implications for Health Care Information and Management Systems, Healthcare Information Management 6, No. 4 (1992) 3–5.

[15] C.W. Emory and D.R. Cooper, Business Research Methods, Fourth Edition (Irwin, Homewood, 1991).

[16] A. Epstein, The Outcomes Movement-Will It Get Us Where We Want to Go?, New England Journal of Medicine 32, No. 3 (1990) 266–270.

[17] G.A. Forgionne, Decision Technology Systems: A Vehicle to Consolidate Decision Making Support, Information Processing and Management 27, No. 6 (1991) 679–797.

[18] G. Forgionne and R. Kohli, Intelligent Healthcare Decision Support, Proceedings of the Twenty-Fifth Annual Meeting of Decision Sciences Institute, Vol. 2 (1993) 684–686.

[19] P. Gray, Ed., Decision Support and Executive Information Systems (Prentice-Hall, Englewood Cliffs, 1994).

[20] P.J. Guichelear, Ed., Design for Manufacturability (American Society of Mechanical Engineers, New York, 1993).

[21] J.P.H. Hamers, H.H. Abu-Saas and R.J.G. Halfens, Diagnostic Process and Decision Making in Nursing: A Literature Review, Journal of Professional Nursing 10, No. 3 (1994) 154–163.

[22] G. Hassan, Software Design Methods for Concurrent and Real-Time Systems (Addison-Wesley Publishing Company, Reading, 1993).

[23] K. Heidenberger, Strategic Decision Support in Preventive Health Care, Socio-Economic Planning Science 26, No. 2 (1992) 129–146.

[24] K. Hitomi, Manufacturing Systems Engineering: the Concept, its Context and the State of the Art, International Journal of Computer Integrated Manufacturing 3, No. 5 (1990) 275–288.

[25] P. Huang, T.A. Pryor and P.R. Frederick, Integrating Radiology and Hospital Information Systems: The Advantage of Shared Data, Proceedings of the Sixteenth Annual Symposium on Computer Applications in Medical Care, November 1992 (Baltimore, 1993) 187–191.

[26] G.K. Kanji, 100 Statistical Tests (Sage, Thousand Oaks, 1993).

[27] K. Kim and J. Michelman, An Examination of Factors for the Strategic Use of Information Systems in the Healthcare Industry, MIS Quarterly 14, No. 2 (1990) 200–215.

[28] D. King, Intelligent Decision Support: Strategies for Integrating Decision Support, Database Management, and Expert System Technologies, Expert Systems with Applications 1, No. 1 (1990) 23–38.

[29] R. Kohli, Providing Concurrent Decision Support in Healthcare Management through Decision Technology Systems, Unpublished Dissertation, University of Maryland, Baltimore (1993).

[30] R. Kohli and G. Forgionne, A Knowledge-Based System to Facilitate Concurrent Engineering, Fabricator 23, No. 5 (1993) 86–92.

[31] R. Kohli and G. Forgionne, Applying Concurrent Engineering Concepts to Clinical Information Systems, Healthcare Information Management 6, No. 4 (1992) 13–16.

[32] R. Kropf, Designing a Physician Computer Network for a Managed Care Environment, Healthcare Information Management 6, No. 4 (1992) 10–12.

[33] S. Kumar and Y.P. Gupta, Statistical Process Control at Motorola's Austin Assembly Plant, Interfaces 23, No. 2 (March-April 1993) 84–92.

[34] A. Kusiak, Ed., Concurrent Engineering: Automation, Tools, and Techniques (Wiley, New York, 1993).

[35] D.M. Lamberti and W.A. Wallace, Intelligent Interface Design: An Empirical Assessment of Knowledge Presentation in Expert Systems, MIS Quarterly 4, No. 3 (1990) 279–311.

[36] K.B. Langston, M.E. Johnston and A. Mathieu, A Critical Appraisal of the Literature on the Effects of Computer-Based Clinical Decision Support Systems on Clinical Performance and Patient Outcomes, Proceedings of the Sixteenth Annual Symposium on Computer Applications in Medical Care, November 1992 (Baltimore, 1993) 626–630.

[37] J.P. Lathrop, Restructuring Health Care (Jossey Bass, San Francisco, 1993).

[38] D. Leidner and J. Elam, Executive Information Systems: Their Impact on Executive Decision Making, Journal of

Management Information Systems 10, No. 3 (1993–94) 139–155.

[39] J. Liebowitz, The Dynamics of Decision Support and Expert Systems (The Dryden Press, Chicago, 1990).

[40] B. Lin, Organizational Issues in Health Care Information Systems, Proceedings of the Twenty-Third Annual Meeting of the Decision Sciences Institute, Miami Beach, Vol. 3 (1991) 912–914.

[41] J.M. Mackay and J.J. Elam, A Comparative Study of How Experts and Novices Use a Decision Aid to Solve Problems in Complex Domains, Information Systems Research 3, No. 2 (1992) 150–172.

[42] M. McNeilly and S. Gessner, Business Insights: An Expert System for Strategic Analysis, Planning Review 21, No. 2 (1993) p. 32.

[43] P. Meek, Healthy Business: Hospitals Operate More Effectively With Information Delivery Systems, SAS Communications 23, No. 3 (1992) 9–14.

[44] R.J. Mockler, Strategic Intelligence Systems: Competitive Intelligence Systems to Support Strategic Management Decision Making, S.A.M. Advanced Management Journal 57, No. 1 (Winter, 1992) p. 4.

[45] D. Nash and L. Markson, Managing Outcomes: The Perspective of the Players, Frontiers of Health Services Management 8, No. 2 (1992) 3–51.

[46] J. Newman, The Role of Idea Processing in Decision Support Systems, Unpublished Dissertation, University of Maryland, Baltimore (1993).

[47] M.J. Norusis, SPSS for Windows: Base System Users' Guide, Release 5.0 (SPSS Inc, Chicago, 1992).

[48] H.R. Parsaei and W.G. Sullivan, Concurrent Engineering: Contemporary Issues and Modern Design Tools (Chapman, London, 1993).

[49] K. Parsaye and M. Chignell, Data Quality Control with Smart Databases, AI Expert 8, No. 5 (1993) 22–27.

[50] A. Pasternack, Ed., The Fourth Annual HIMSS/Hewlett-Packard Leadership Survey: Trends in Health Care Computing (The Healthcare Information and Management Systems Society of the American Hospital Association, Chicago, 1993).

[51] M. Perigord, Achieving Total Quality Management: A Program for Action (Productivity Press, Cambridge, 1990).

[52] W. Potter, T. Byrd, J. Miller and K. Kochut, Extending Decision Support Systems: The Integration of Data, Knowledge, and Model Management, Annals of Operation Research 38 (1992) 501–527.

[53] W. Reitman, Generic Expert Systems for Management Applications: The Operations Advisor and the Management Advisor, Computer Science in Economics and Management 3, No. 2 (1990) 167–175.

[54] A. Sabbaghi, Computer-Integrated Manufacturing as an Integrated Decision Support System, International Journal of Modelling and Simulation 10, No. 2 (1990) 57–66.

[55] F. Sainfort, D.H. Gustafson, K. Bosworth and R.P. Hawkins, Decision Support Systems Effectiveness: Con-

ceptual Framework and Empirical Evaluation, Organizational Behavior and Human Decision Processes 45, No. 2 (1990) 232–252.

[56] S. Salzberg and M. Watkins, Managing Information for Concurrent Engineering: Challenges and Barriers, Research in Engineering Design 2 (1990) 35–52.

[57] V. Sethi and W.R. King, Construct Measurement in Information Systems Research: An Illustration in Strategic Systems, Decision Sciences 22, No. 3 (1991) 455–472.

[58] C. Shapleigh, Patient Data Critical to Hospital-Wide Quality, Healthcare Financial Management 45, No. 6 (1991) 80–83.

[59] M. Silver, Decisional Guidance for Computer-Based Decision Support, MIS Quarterly (March, 1991) 105–122.

[60] B.G. Silverman, Unifying Expert Systems and the Decision Sciences, Operations Research 42, No. 3 (1994) 393–413.

[61] W.E. Spangler, The Role of Intelligence in Understanding the Decision-making Process, IEEE Transactions on Knowledge and Data Engineering 3, No. 2 (1991) 149–159.

[62] W. Sujansky and M. Shwe, The SQLX System: Generating Explanations for Clinical Rules Encoded in SQL, Proceedings of the Sixteenth Annual Symposium on Computer Applications in Medical Care, November 1992 (Baltimore, 1993) 239–243.

[63] E.J. Szewczak, Using Information Technology to Implement Strategic Systems Planning as a Knowledge-Based Group Support Process, Information Resources Management Journal 5, No. 2 (Spring, 1992) p. 17.

[64] A. Targowski, The Architecture and Planning of Enterprise-Wide Information Management Systems (Idea Group Publishing, Harrisburg, 1990).

[65] M.M. Tatsuoka, Multivariate Analysis, Second Edition (Macmillan, New York, 1987).

[66] P. Todd and I. Benbasat, An Experimental Investigation of the Impact of Computer Based Decision Aids on Decision Making Strategies, Information Systems Research 2, No. 2 (1991) 87–115.

[67] E. Turban, Decision Support and Expert Systems: Management Support Systems, Third Edition (Macmillan Publishing Company, New York, 1993).

[68] C.K. Tyran and J.F. George, The Implementation of Expert Systems: A Survey of Successful Implementations, Database 24, No. 1 (1993) 5–15.

[69] G.J. Udo, Rethinking the Effectiveness Measures of Decision Support Systems, Information and Management 22, No. 2 (1992) 123–135.

[70] S.K. Vickery, C. Droge and R.E. Markland, Production Competence and Business Strategy: Do They Affect Business Performance? Decision Sciences 24, No. 2 (March-April, 1993) 435–455.

[71] R. Welch, Information Systems Eases Concurrent Engineering, Signal 44, No. 8 (1990) 67–68.

[72] L.A. West and J.F. Courtney, The Information Problems in Organizations: A Research Model for the Value of Information and Information Systems. Decision Sciences 24, No. 2 (1993) 229–251.

[73] D.B. Yoffie, Strategic Management in Information Technology (Prentice-Hall, Englewood Cliffs, 1994).

[74] R.A. Zink, Strategic Systems Classification, Journal of Information Systems Management 10, No. 2 (Spring, 1993) p. 59.

![](/api/attachments/PK2G57E4/fulltext/images/a000bad59ff5dd0808eedd83689bc9d0e8296c7498b7200dbd4612afcd406770.jpg)

Guisseppi A. Forgionne is Professor of Information Systems at the University of Maryland Baltimore County (UMBC). Professor Forgionne holds a B.S. in Commerce and Finance, an M.A. in Econometrics, an M.B.A., and a Ph.D. in Management Science and Econometrics. He has published 20 books and approximately 100 research articles and consulted for a variety of public and private organizations on decision support systems the

ory and applications. Dr. Forgionne also has served as department chair at UMBC, Mount Vernon College, and Cal Poly Pomona. He has received several national and international awards for his work.

![](/api/attachments/PK2G57E4/fulltext/images/c7731170c019df0770e9ab1a59748f988ed6c688088a4d28e50f368e1f1c59c1.jpg)

Rajiv Kohli is with the Hospital Information System Department at Saint Joseph Medical Center in Towson, Maryland. He received his Ph.D. in information systems from the University of Maryland Baltimore County (UMBC) in 1994. Dr. Kohli's research interests include enhancing DSS with expert systems and the application of decision technologies for competitive advantage. He also is assistant professor at Loyola College and the Univer-

sity of Maryland College Park (UMCP), teaching decision support systems and artificial intelligence.
