---
otero_id: 3978
otero_key: "HWQYBHN8"
title: "Disaggregating the Differential Impact of Healthcare IT in Complex Care Delivery: Insights from Field Research in Chronic Care"
authors: "Ravi Aron; Praveen Pathak"
year: "2021"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00675"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Volume 22 Issue 3

Article 8

2021

# Disaggr egating the Diff  erential Impact of Healthcar   e IT in Complex Car e Deliv  ery: Insights fr   om Field Resear  ch in Chr  onic Care

Ravi Aron , raron@bauer.uh.edu

Praveen Pathak , praveen@ufl.edu

Follow this and additional works at: https://aisel.aisnet.org/jais

# Disaggregating the Differential Impact of Healthcare IT in Complex Care Delivery: Insights from Field Research in Chronic Care

Ravi Aron<sup>1</sup>, Praveen Pathak<sup>2</sup>

<sup>1</sup>University of Houston, USA, raron@bauer.uh.edu <sup>2</sup>University of Florida, USA, praveen@ufl.edu

## Abstract

This study focuses on the impact of digitizing medical information on the efficiency and perceived quality of chronic care delivery at the individual physician level. This study extends the theory of task technology fit to activity systems consisting of highly interdependent tasks. We find that the outcomes of efficiency and quality gains are driven by the structure of interdependencies between tasks that physicians perform. While structured information plays a key role in enabling both decision-making and task execution, we find that physician-created semistructured information is also an important predictor of both efficiency and quality gains. We show that the structure of activity systems (task interdependencies) has a strong moderating influence on the factors that drive efficiency and quality gains. We find that digitization enables physicians to preprocess patients’ records prior to their visit which in turn drives gains in both the efficiency and the perceived quality of care delivered.

Keywords: Digitization, EMR, Complex Care Delivery, Field Research, Panel Data

Jason B. Thatcher was the accepting senior editor. This research article was submitted on May 3, 2019 and underwent two rounds of revisions.

## 1 Introduction

In recent years, the use of information technology (IT) in the healthcare field, particularly electronic health records (EHR), has created substantial controversy. Two surveys suggest (respectively) that the impact of EHRs on clinical workflow is negative and that the returns on EHRs are poor, while a research report from HIMSS argues that significant productivity gains resulted from implementing EHRs (HIMSS, 2006; Livernois, 2017; Tutty, 2019). Adler-Milstein et al. (2013) argue that the results of EHR implementation may bring gains to a few practices while resulting in losses for many practices. The average physician would lose money because of productivity losses and only 27% of the practices would realize gains from EHRs, with a large majority of practices encountering net losses (Adler-Milstein et al., 2013).

Proponents of EHRs claim that by digitizing and automating medical information, physicians will obtain accurate, complete, and timely information on which to base their clinical decisions (Bardhan & Thouin, 2013). However, several studies have failed to detect substantial benefits of health IT in terms of either quality or cost (Agha, 2014; McCullough et al., 2010; Reiss et al., 2017). There is even evidence that health IT leads to higher costs for payers (Abelson et al., 2012), which ignited a heated debate over whether the government should continue to push for the wider adoption of health IT. The debate about the costs and benefits of HIT is particularly relevant for chronic care, which accounts for 78% of total healthcare spending and is informationintensive, requiring frequent clinical testing of multiple types (Bhargava & Mishra, 2014; MEPS, 2006). This leads us to a key research question that this study seeks to answer about chronic care delivery: are there efficiency gains associated with the digitization of patients’ information into EHRs? There is little or no research in IS on how the delivery of chronic care— which is very different from acute care, emergency care, and family practice—is influenced by the use of EHRs and clinical decision support systems (CDSS) by chronic care specialists.

Studies on the use of HIT treat all healthcare delivery as one category (treating it as a single entity such as manufacturing or retailing). This approach is very problematic. Specialists that provide chronic care, such as cardiologists, oncologists, diabetologists, nephrologists, etc., work in contexts that are very different from the acute and primary care provided by primary care physicians and use HIT platforms very differently. Bates (2002) contrasts the information needs of chronic care with acute care delivery and observes that for chronic care to work, interdisciplinary teams of specialists need to be able to track multiple aspects of patients’ pathology and seamlessly exchange information (Bates, 2002). The direct inference from Bates’s study is that the clinical information in the EHRs that primary care providers (PCPs) create is of immense value to “downstream” specialists who use this both for their clinical diagnoses and to create collaborative boundary-spanning knowledge artifacts that enable the interdisciplinary work of specialists.

Wagner et al. (2001) argue that chronic care delivery requires the collaborative work of several specialists, which is very evidence intensive. Care delivery of this kind is therefore much more information intensive than primary or acute care. They argue that the information contained in EHRs, which is often created by other clinicians including PCPs, enable them to make clinical interventions and collaborate with other specialists, often with minimal time lag. Therefore, the benefits of digitization of clinical data and their maintenance (often done by PCPs) flow downstream to teams of specialists who depend on this information to enable collaboration. Young et al. (2007) noted the highly informationintensive nature of chronic care illnesses and found that for improved care delivery it was necessary to provide clinicians with real-time access to patient clinical status, treatment history, and decision support (Young et al., 2007). The discussion above on the differences between chronic care and acute and/or primary care leads us to observe that lumping all care delivery into one category ignores very important differences between chronic and primary care contexts.

This approach is very problematic. These studies systematically underestimate the benefits of HIT by ignoring the “downstream benefits” to specialists from the work of PCPs and clinicians that create and maintain EHRs and clinical information repositories. Thus, the claims made by these researchers that HIT platforms do not deliver the promised benefits, overlook significant benefits of EHRs that are captured by specialists— where the digitized information is of greatest value. This in turn results in several misleading claims being made about HIT not being of significant value (or even any value at all) in healthcare delivery (Agha, 2014; Reiss et al., 2017) and/or other studies that claim that digital processes actually make physicians less productive (Livernois, 2017; Tutty et al., 2019). This study therefore focuses on chronic care and the impact of digitization of patient data on efficiency and the perceived quality of care delivery. Our study develops theoretical frameworks to analyze the work of chronic care specialists by studying the tasks that they perform and the dependencies between those tasks as well as the extent to which technology supports the critical task characteristics of a system of interdependent tasks.

Extant empirical research in IS on the impact of digitizing information flows has looked at other industries such as retail, manufacturing, IT products, and financial services (Chiasson & Davidson, 2005). While there is a well-established body of research on IT productivity (Aral et al., 2012; Brynjolfsson & Hitt, 1996; Hitt et al., 2002; Lee at al., 2013; Menon et al., 2000; Tambe & Hitt, 2012), researchers have pointed out that studies have disproportionately focused on manufacturing industries (Aral et al., 2012). A smaller body of research investigates the impact of introducing digital technologies including EHR into the healthcare industry (Agha, 2012; Bhargava & Mishra, 2014; Furukawa et al., 2010; Lee at al., 2013). Several researchers have observed that there is a paucity of productivity studies at the individual knowledge worker level in IS literature (Aral et al., 2012; Bulkley & Van Alstyne, 2004). Bhargava and Mishra (2014) make a notable effort to study the impact of EHRs on the productivity of different kinds of physicians.

But while this study makes a key contribution, it does not incorporate two measures of the physician’s usage context: (1) there are no actual measures of the extent of task technology fit between specific tasks and the technology that supports those tasks, and (2) it does not consider interdependencies between tasks. Agarwal et al. (2010) observe that the current research in health IT looks at structural models with correlations between variables without paying sufficient attention to the contextual factors of actual HIT usage by specialists. Several researchers have argued that to gain a deeper understanding of IT’s impact on knowledge work, it is important to both include an explicit focus on the use context of various physicians and apply granular data about the individual IT worker (Agarwal et al., 2010; Athey & Stern, 2002). This study fills that gap in the literature by addressing both issues. First, we capture the IT use context of the knowledge worker (tasks performed by specialist physicians using IT and the interdependencies between those tasks); second, we capture data at the level of the individual IT worker (our unit of analysis is the individual specialist physician).

To our knowledge, this is the only study that accomplishes all four of the following objectives: (1)

captures actual measures of task technology fit for the tasks that specialist physicians perform; (2) captures the nature and extent of task interdependencies and shows how these result in two different types of task systems (activity systems); (3) uses times series data sets to show the impact of progressive digitization on the productivity of individual physicians and the perceived quality of care delivered by them; and (4) captures data about the digitization of the kinds of information used by specialists—structured, unstructured and semistructured—and links it to productivity and quality outcomes. This study draws upon theories from three streams of research—task-technology fit (TTF), theory of task interdependencies, and activity systems (organizational theory)—and applies these theories to explain physician productivity and the perceived quality of care delivered by physicians.

There are four principal findings of this research study. First, we find that the structure of task interdependencies, i.e., the nature of the activity system, has a strong moderating impact on determining which task characteristic is the critical task characteristic (CTC) and how the CTC impacts productivity and (perceived) quality gains at the level of the individual specialist physician. Second, we show that where there are task interdependencies, the TTF measures of individual tasks do not predict or explain the gains of technology implementation; however, the weighted average measures of TTF at the level of a system of interdependent tasks (activity system) do explain productivity and quality outcomes.<sup>1</sup> Third, specialistcreated, semistructured information (derived from unstructured information) plays a key role in driving productivity and quality outcomes at the level of the individual physician. Fourth, there are strong complementarities between the preprocessing of patient information by specialists and the creation of digitized semistructured information in delivering both efficiency and quality gains.

The rest of the paper is organized as follows. Section 2 reviews relevant theory. In Section 3, we derive testable hypotheses, and in Section 4, we outline the empirical research design including details of data collection and operationalization of variables. Empirical models and analyses are reported in Section 5. Section 6 concludes the paper with a discussion of the contributions of this study, including insights for practitioners, and identifies some limitations and possible extensions of this research.

## 2 Review of Theory

The work performed by specialist physicians that provide chronic care, such as cardiologists, diabetologists, and oncologists, consists of several tasks that are characterized by high degrees of task interdependence (Barr et al., 2003; Lekyum et al., 2014). We theorize how the use of technology by specialists, given the high degree of interdependencies in the tasks that they execute, results in efficiency and quality gains at the level of the individual specialist. To answer this question, we draw upon three streams of theory. Two of these streams are from IS—task technology fit theory and task interdependence theory—and the third is from activity systems in organizational theory. We build a model of effects drawing on theories from these three research domains in the sections that follow.

## 2.1 Task Technology Fit

The extent to which technology (that supports decisionmaking and task execution) can deliver beneficial outcomes such as productivity and quality gains can be explained in part by the theory of task technology fit (TTF). The central tenet of the theory is that business performance is driven by the extent of fit between critical task needs and the functional features of the system supporting the performance of those tasks (Dennis et al. 2001; Goodhue 1995, Goodhue and Thompson 1995). Extant research has also looked at the extent to which the characteristics of task and technology interact (Dishaw & Strong, 1999, 2003). All of these studies look at the impact of technology’s fit with task characteristics where the unit of analysis is one or more tasks in isolation. No study looks at the extent to which the characteristics of a technology fit with a system of interdependent tasks as opposed to an individual task.

This observation motivates a set of related questions that we address in this study: How does the TTF theory work when a technology is used to support the execution of multiple tasks that are highly interdependent, as opposed to a single task or a set of independent tasks? Will productivity and quality outcomes differ based on the nature of task interdependencies? The missing element in TTF theory is how TTF applies to a system of highly interdependent tasks and how the extent of fit is to be measured at the level of a system of tasks as opposed to an individual task level. To understand why a system of (highly) interdependent tasks might interact differently with a technology than a single task, we need to turn to the theory of task interdependency.

## 2.2 Task Interdependence Theories

Researchers have observed that task interdependence forms a key component of the task environment, which in turn shapes work outcomes and the institutional context of work (Majchrzak, 2000; Orlokowski, 1992). Sharma and Yetton (2003) showed that task interdependence shapes many other forms of institutional context including performance control systems. Chronic care specialists are faced with significant levels of performance control mechanisms that range from pricing controls (imposed by entities that pay for healthcare) to procedural controls (imposed by the Joint Commission on Accreditation of Healthcare Organization—JCAHO) and the policy regimes of their hospitals. Researchers studying task interdependencies have shown that task performance is influenced by the fit between the performance control mechanisms and the nature of task interdependence (Andres & Zmud, 2001).

These observations lead us to pose the question: How do technologies that support task execution fare when implemented in the presence of task interdependencies? Researchers have shown that the level of difficulty in achieving beneficial outcomes from information systems increases as the level of task interdependence increases (Hackthorn & Keen, 1981). In environments with high levels of task interdependence, IS innovations—i.e., systems that aid decision support and task execution—may require significant changes to the organizational context if they are to deliver beneficial outcomes (Sharma & Yetton, 2003). In contrast, it has been shown that, as opposed to technologies that aid in executing interdependent tasks, technologies that support individual or independent tasks require minimal to no information spillover between tasks, and end users can capture performance gains from technology usage relatively easily (Kang & Santhanam 2003; Sharma & Yetton, 2003). In a related finding, researchers show that when information systems are implemented to support workflow and task execution, coordination and information transfer between tasks are not critical to the performance of independent individual tasks (Sharma & Yetton, 2007). It is clear that factors that drive beneficial outcomes with technologies that support individual or independent tasks are significantly different from factors that drive outcomes with systems of interdependent tasks. We seek to extend the findings of the TTF theory to explain the impact of technology introduction in support of the highly interdependent system of tasks that chronic care specialists perform. To do this, we need to investigate the structure of interdependencies between tasks to theorize how the TTF model can be adapted to explain how technologies interact with interdependent task systems. To understand the defining characteristics of the structure of a system of interdependent tasks, we turn to the field of organizational theory—in particular, to activity systems and how they shape organizational outcomes.

## 2.3 Activity Systems

The complementarity framework developed by Milgrom and Roberts (1995) examined the nature of the interdependency between the many tasks performed within the organization and the resulting output and strategic outcomes at the firm level. The NK model developed by Kauffman (1993) enables the modeling of interactions between systems of interdependent tasks that constitute organizational activity systems. Recent research by Porter and Siggelkow (2008) has looked at interactions between interdependent tasks that constitute an activity system (as well as interactions between activity systems) to identify the factors that make these interactions complements or substitutes. Porter and Siggelkow illustrate the idea of an activity system consisting of interdependent tasks using the example of the auto insurance firm, Progressive Corp. Progressive Corp’s activity system configuration consists of several highly interdependent tasks, all of which support one central objective: settling claims as quickly as possible to avoid lawsuits.

The configuration of this activity system is also of interest. In their example, the activity system consists of highly interdependent tasks, ranging from a prompt accident site visit from an adjuster to electronic support for quick funds disbursement, and prompt information updates to claimants, which are configured so that every task depends on one or more other tasks. The structure of this activity system is such that each task depends on or contributes to the successful execution of several other tasks. There is no task within the activity system that is a “standalone” task that does not depend on or contribute to the execution of one or more tasks. For ease of exposition, we use the term fully connected activity systems (FCAS) to denote such activity systems. <sup>2</sup> To model such activity systems and their resulting impact on the performance of the firm, researchers have employed the technique of multidimensional performance landscapes of atomic tasks (Kauffman, 1993; Levinthal, 1997). Scholars studying organizational theory and strategy have posited that activity systems with tightly interconnected systems of tasks (FCAS) have a significant role to play in both creating and sustaining competitive advantage (Milgrom & Roberts, 1995; Porter 1996). As opposed to FCAS, there are activity systems in which tasks are not tightly interconnected and several tasks or clusters of tasks may be independent of each other. Again, for ease of exposition, we refer to these as partly connected activity systems (PCAS).

## 2.4 A Contextual Example of Activity Systems in Chronic Care Delivery:

Figure 1 provides an example of a fully connected activity system (FCAS) in which every task performed by a specialist during a patient’s visit is linked to multiple other tasks. Consider the visit of Patient # 1234 to the specialist Dr. John Doe. The specialist performs the task of diagnosis and diagnoses the patient’s current afflictions based on clinical reports and other data. This leads to two other tasks: checking and ascertaining the patent’s drug allergies and prescribing a set of drugs to treat the disease and provide symptom relief (the sixdigit billing reference code that specifies individual tasks such as diagnosis, pathology, prescribing, etc., at the level of each billable task<sup>3</sup> treats these as separate tasks).

Another task that is related to the tasks above has to do with substituting a brand name drug with a generic version. This task is related to two other tasks, as shown in Figure 1. The specialist also notes that the new drugs could have an adverse impact on the patient’s liver and recommends that the patient visit a liver specialist, thus performing the task of providing a referral to a liver specialist. This task in turn depends on two other tasks as shown in the figure: the task of diagnosis and the task of identifying possible adverse drug reactions. The numbers shown next to tasks indicate the extent to which the task depends on other tasks to which it is connected (measured on a 7-point Likert scale). The connector in Figure 1 that connects the task “Prescribe drugs” to the task “Diagnose current condition” is labeled with the number 7, indicating that the task of prescribing drugs is very highly dependent on the task of diagnosis. In this FCAS, every task is connected to multiple other tasks.

Figure 2, in contrast, provides an example of a partially connected activity system (PCAS), in which many tasks performed during a patient’s visit with a specialist are not connected to other tasks. Consider the visit of Patient #5678 to the specialist Dr. John Doe. The patient’s response to drugs is impacted by the patient’s dietary habits. The specialist’s first task is to tell the patient about the drugs he is taking for cardiovascular disease and their link to nutrition. He then recommends that the patient see a nutritionist and provides a referral. He also makes a note on the patient’s EMR and informs the patient’s PCP. These two tasks are connected to each other but are not connected to the next two tasks. The specialist’s next task is to inform the patient about surgical options to address possible blockages in the patient’s heart. The specialist then provides the patient with a referral to a surgeon. The last two tasks have to do with assessing the extent of oxygenation in the patient’s blood. The specialist explains the need to take regular SpO2 readings using a fingertip device to the patient. The specialist then prescribes a particular device that can be used for this purpose.

The above discussion on the two different kinds of activity systems leads us to the next question that we address in this study: When a new technology is introduced to support knowledge work that consists of both FCAS and PCAS, how will the structure of the activity system impact the work outcomes? Researchers have studied the structure of task interdependencies in business process outsourcing (BPO) and have examined how these interdependencies impact the efficiency and quality of work (Aron & Singh, 2005; Liu & Aron, 2015; Mani et al., 2011). Liu and Aron (2015) show that when systems of highly interdependent tasks are offshored, it is necessary to use interorganizational information systems to monitor the work of the agents (knowledge workers) who execute the tasks in real time so that the errors made in the execution of one task do not spill over to other tasks. Aron et al. (2007) use the term information architecture of a business process to refer to the nature and extent of interdependence between tasks in a business process. They show that when business processes are composed of tasks that are not highly interdependent, decision support technologies can be used to support the execution of these tasks very efficiently without compromising the quality of the output.

In contrast, in executing business processes with complex information architectures (with densely connected interdependent tasks), the gains from using technologies such as interorganizational information systems are limited in terms of output quality. Thus it becomes clear that to understand how the digitization of patient data and decision support systems (DSS) impact the efficiency and quality of work of chronic care specialists, it is necessary to bring together three different streams of research: TTF, task interdependency theories, and activity systems. TTF theories link the nature of task characteristics to the technology that supports the execution of these tasks, task interdependency theories explain how task interdependencies impact the performance of tasks, and research in activity systems explains how the configuration of these interdependent tasks—i.e., the structure of the activity system—impacts work outcomes. We theorize by drawing on the tenets of these three domains and develop a set of testable hypotheses.

![](/api/attachments/HWQYBHN8/fulltext/images/e76cef75c1c554d63431cbcaa94769dd0281046919e068a5ed02d6275e18ded8.jpg)  
Note: the task interdependency ratings on a 7 point Likert scale, are shown in the connections between tasks.  
Figure 1. Fully Connected Activity System (FCAS)

![](/api/attachments/HWQYBHN8/fulltext/images/869d55d9fc7c35981dd770c16f7f12ca87c913f671ad3193d6a0a4855c2ae38b.jpg)  
Note: the task interdependency ratings on a 7-point Likert scale, are shown in the connections between tasks.  
Figure 2. Partly Connected Activity System (PCAS)

## 3 Hypotheses

TTF theory offers a theoretical framework that explains how the nature and extent of fit between task characteristics and the system (technology) used to execute the tasks results in work outcomes (Dennis et al., 2001; Goodhue 1995; Goodhue 1995; Zigurs and Buckland 1998). Research into the process of chronic care delivery for outpatients that is nonsurgical and does not involve the performance of procedures<sup>4</sup> has identified the two principal task characteristics of chronic care specialists’ work: diagnostic decisionmaking and task execution (Riano et al., 2012; Walker et al., 2009; Wagner et al., 1996). In the chronic care model (CCM) developed by Wagner et al. (2001), the critical elements of clinical information systems can be divided into the categories of decision support and task execution support. The specialists in our panel also identified decision-making and execution as the two principal characteristics of tasks. <sup>5</sup> We extracted the TTF ratings of the extent of fit between the technology and each of these two task characteristics from users. As observed in the previous section, TTF measures can be applied at the level of individual tasks and not at the level of an activity system of interdependent tasks. Researchers have observed that task interdependencies in a system of tasks often result in decision-making errors that spill over from one task to another (Kadab et al., 2003; Liu & Aron, 2015).

Prior research has also shown that task interdependence is a key component of the task environment, which in turn shapes work outcomes (Majchrzak, 2000; Orlokowski, 1992). Further evidence of the interaction between task interdependencies and the technologies used to support them is provided by Hackthorn and Keen (1981), who show that the level of difficulty in driving beneficial outcomes from information systems increases as the level of task interdependence increases. Sharma and Yetton (2003) point out that, in the presence of task interdependencies, significant changes to the organizational context may need to be made if IS innovations are to deliver beneficial outcomes. In sharp contrast, researchers show that technologies that support individual tasks or independent tasks require no coordination or information transfer between tasks and end users can capture performance gains from technology usage relatively easily (Kang and Santhanam 2003; Sharma and Yetton 2003). We therefore posit that the nature of task interdependencies—as manifest in the structure of an activity system—has a moderating effect on how TTF impacts work outcomes.

## 3.1 Moderating Effect of Activity Systems

Researchers have noted that activity systems may consist of highly interdependent atomic tasks characterized by complementarities (Milgrom & Roberts, 1995; Porter, 1996; Porter & Siggelkow, 2008; Siggelkow & Rivkin, 2009). In such systems of highly interdependent tasks, where the output of one task often comprises the input of one or more tasks, the errors made in one task are often “carried over” into other tasks and, in such cases, incorrect decisions made in one task often have a cascading effect for other tasks (Kadab et al., 2003; Liu & Aron, 2015). Researchers have also observed that in highly connected networks of interdependent tasks, “task relatedness” (also called connectedness) results when the performance of one task has a significant impact on the completion of other tasks, thereby amplifying the hazard of bad decisions made in one task spilling over into other tasks (van der Vegt et al., 2003; Wybo & Goodhue, 1995).

These observations point to two important factors that may explain work outcomes in FCAS: (1) the critical task characteristic, i.e., the task characteristic that is most important in FCAS is decision-making, and (2) The weighted average TTF rating of this characteristic measured at the activity system level is likely to be more influential in determining work outcomes than the TTF ratings of individual tasks in the activity system.<sup>6</sup> Extant research points to the important role played by structured information (SI) in preventing clinical decision-making errors (Bates et al. 2001; Bates et al. 2003) and in formulating effective decision rules in chronic care when outcomes of decisionmaking in a task depend on decisions made in other tasks (Johnson et al., 2000). These observations lead us to our first hypothesis.

H1a: In FCAS, the interaction of the digitization of structured information and the TTF for the critical task characteristic of decision-making measured at the level of the activity system is associated with lower mean contact duration between patient and physician.

As opposed to FCAS, there are also partly connected clusters of independent and interdependent tasks, which together form a pooled dependency at the level of the activity system (Thomson, 1967). Aron et al. (2007) find that when tasks are not highly interdependent, technologies can be effectively used to support their execution, and the errors made in task execution can be relatively easily identified with minimal danger of error spillover between tasks. Other researchers observe that setting effective performance goals and objectives increases outcome efficiencies for tasks of low interdependency and result in increased performance variance for high interdependency tasks (Hirst & Yetton, 1999).

In a similar vein, researchers find that for systems of low interdependency tasks, successful implementation of information systems is less challenging and performance gains accrue to end users relatively easily (Kang & Santhanam, 2003; Sharma & Yetton, 2003). Researchers studying how CDSS support workflow in chronic care, especially in low task interdependency contexts, point out that the key to driving beneficial outcomes is for the technology to provide accurate task execution support such as ordering lab tests, providing referrals for other physicians, and scheduling followup visits. They note that for these kinds of task systems, specialists value accurate support for task execution far more than decision support (Unertl et al., 2009). As observed earlier, several researchers have shown that structured information (SI) plays a very important role in chronic care. What is interesting is the role played by semistructured information (SSI). SSI is created by specialists editing the patient’s EHR and creating keywords, hyperlinks, search terms, and notes from the unstructured information (UI).

Researchers working in the domain of medical informatics have noted that several important aspects of patient medical history and descriptions of prior afflictions are contained in “medical narratives” (unstructured, text data) that need to be processed either using natural language processing techniques or by physicians to create SSI (Afantenos et al., 2005; Van Vleck et al., 2007). Researchers studying CDSS in chronic care point out that in order to make CDSS more useful in supporting task execution, physicians need to edit free text to create SSI (Bates et al., 2001; Bates et al. 2003). Unertl et al. (2009) study systems that support workflows in chronic care, and they highlight the need for creating structure out of UI. They observe that clinicians are often required to search through disparate sources of information that are in an unstructured format and collate the results rapidly in order to execute tasks. We synthesize these research findings to posit that (1) for PCAS, the critical task characteristic is task execution (TE), (2) the weighted average TTF measure of this characteristic measured at the level of the activity system is likely to be more influential in determining work outcomes than the TTF ratings of individual tasks, and (3) SSI supports the critical characteristics of task execution. This leads us to our next hypothesis.

H1b: In PCAS, the interaction of digitization of both structured and semistructured information and the TTF measure for the critical task characteristic of task execution, measured at the level of the activity system, is associated with lower mean contact duration between patient and physician.

## 3.2 Digitization and Process Change

It is well established that if a new technology is introduced, business processes need to be redesigned to unleash the full potential of that technology (Melville et al., 2004). In the current study, we observe that physicians began to take advantage of information digitization by preprocessing patient information. Physicians and/or residents would review a patient’s clinical test results and key affliction indicators (SI), as well as keywords, edits, hyperlinks, and comments made by them and clinical annotations made by other specialists (SSI) before the patient’s scheduled visit. An important end objective enabled by the preprocessing of patient information is the formation of transactive memory (TM) (Jackson & Klobas, 2008; Lewis, 2004; Wegner et al., 1985) by specialist physicians.

Chronic care patients very often suffer from comorbidities; thus, chronic care specialists must integrate the information and insights—generated by other specialists that have treated the patient’s comorbidities—into a clinical decision-making framework. When specialists preprocess patient information, they often look at the notes that they have made in prior patient visits, as well as keywords and links to other specialists’ comments (including clinical annotations made by other clinicians). This further aids in the development of TM by specialist physicians. Extant research shows that when faced with interdependent tasks, the formation of TM is key to integrating the insights of multiple experts into a coherent decision-making framework (Argote & Ren, 2012; Lewis, 2004; Sharma and Yetton 2003; Sharma & Yetton, 2007). Researchers studying care delivery in outpatient settings in specialist clinics have also shown that the preprocessing of patients’ case histories by physicians resulted in more efficient utilization of specialists’ consulting hours (Williams et al., 2014).

We combine the findings from research in chronic care delivery and IS to formulate our next set of hypotheses.

H2a: In both kinds of activity systems, higher levels of preprocessing of patient information are associated with lower mean contact duration between patient and physician.

H2b: In both kinds of activity systems, the interaction of digitization of semistructured information and preprocessing of patient information are associated with lower mean contact duration between patient and physician.

## 3.3 Digitization and Quality of Care Delivered

Two dimensions characterize the delivery of chronic care; the outcomes are not easily measurable, and they take considerable time to manifest themselves. Given that, at the end of a visit to an oncologist or a cardiologist, patients cannot state whether the visit has had a beneficial impact on their health, we must rely on a measure of perceived quality of care in order to assess the quality of care experienced by patients. Researchers have observed that where the outcomes of service are not immediately evident or measurable, customers’ perceived quality of service is of great significance to organizations (Parasuraman et al., 1991; Zeithamal et al., 2002), a finding that has been replicated in the delivery of healthcare services as well (Hawkins et al. 2016). Further, extant research on service quality has shown that evaluations of service quality are not made solely on the outcome of the service; the process of service delivery is also important in shaping the perception of quality (Gronroos, 1982; Lehtinen & Lehtinen, 1982; Lewis & Booms, 1983). We combined these findings from extant research with our earlier theorizing on the moderating impact of activity systems, in order to arrive at our next set of hypotheses.

H3a: In FCAS, the interaction of digitization of structured information and the extent of TTF with the critical task characteristic of decisionmaking, measured at the level of the activity system, is associated with greater perceived quality of care delivered.

H3b: In PCAS, the interaction of digitization of semistructured information and the extent of TTF with the critical task characteristic of task execution, measured at the level of the activity system, is associated with greater perceived quality of care delivered.

A related question that arises has to do with the physician’s preparatory activities prior to seeing a patient and their impact on perceived quality of care delivered by the physician. More specifically, we ask: How does the preprocessing of chronic care patient information by physicians impact the perceived quality of service delivered by the physician? Preprocessing patient information gives physicians the context of the patient’s visit. Researchers have observed that personalizing the process of service delivery is key to strategic differentiation and drives perceptions of higher service quality (Gronroos, 1982; Lehtinen & Lehtinen, 1982; Lewis & Booms, 1983). Preprocessing patient information allows the physician to display familiarity with the patient’s case history and thus personalize the process of service delivery. The formation of transactive memory (TM) also plays a key role in helping experts integrate the information from multiple other experts into a coherent decision-making schema (Brandon & Hollingshead, 2004; Wegner et al., 1985). In the presence of task interdependencies, when faced with the imperative of integrating the opinions of multiple experts into a unified decision-making schema, the formation of TM is key to better and more accurate decision-making (Argote & Ren, 2012; Lewis, 2004; Sharma & Yetton, 2003; Sharma & Yetton, 2007). We combine the research findings above to theorize our next set of hypotheses:

H4a: In both kinds of activity systems, higher levels of preprocessing digital patient information are associated with higher levels of perceived quality of care delivered.

H4b: In both kinds of activity systems, the interaction of digitization of semistructured information and preprocessing of patient information is associated with higher levels of perceived quality of care delivered.

The hypotheses described above were tested on panel data collected from a hospital system over the course of a year. In the next section, we discuss the details of how the data were collected as well as the operationalization of variables.

## 4 Empirical Research Design

## 4.1 Data Collection:

Data for this research was obtained from a large multispecialty hospital system that offers a full range of tertiary healthcare services, including chronic care delivery services. <sup>7</sup> Our study focuses on outpatient services. The authors made seven visits to the hospitals over a two-year period, held numerous discussions with senior managers in the hospital, and conducted several interviews with IT managers, quality control managers, and the chief medical officer at the hospital. One of the authors also designed some sections of the survey instrument used by the hospital system to collect postimplementation feedback from physicians. This study is based on the visits made over the course of one year by 1527 patients with four predominant chronic care conditions: diabetes, cardiovascular disease, hypertension, and cancer. These conditions accounted for 79.8 % of the hospital’s chronic care patients at the start of the study. Twenty-five specialists in all, spread across the four chronic care categories (with seven, six, five, and seven specialist physicians in each chronic care unit, respectively), treated the patients involved in the study. Each specialist received several hundred visits each month from the total pool of patients. All chronic care specialists in our panel met with patients in their offices in outpatient settings. We constructed our measures based on aggregating 34,663 visits made by 1527 patients during the study period.

Over twelve months of observation, the hospital progressed incrementally toward complete digitization of clinical information flows for chronic care patients. Prior to the process of digitization, they designed and tested a CDSS that chronic care specialists could start using with the first batch of digitized patient records. In addition to decision support, the system had functionalities for clinical workflow support and computerized physician order entry (CPOE) that were very similar to the system described in Appari et al. (2013). The key difference between the systems described by Appari et al. (2013) and the one used by the hospital system was that the rollout of the CDSS preceded the batchwise digitization of patient electronic records and their release for use by specialists (in accordance with HL7,<sup>8</sup> and IHE,<sup>9</sup> IS standards adopted by the JCAHO). Starting from the first month, the CDSS could be used by chronic care specialists for patients whose records had been digitized. Each patient’s digitized information consisted of both SI and UI. As previously mentioned, extensive research in the domain of health informatics, data mining, and information retrieval categorizes information into three fundamental types: structured, unstructured, and semistructured (Buneman et al., 1997; Fernandez et al., 1997; Kanza et al., 2002; Rusu et al., 2012). SSI is created by human agents processing UI to create searchable query elements such as key words, hyperlinks, codes, and annotations (Barbulescu et. al., 2013; Kanza et al., 2002; Rusu et al., 2012; Sanchez et al., 2004).

The hospital digitized all SI (clinical lab reports, patient vital stats numbers, key clinical indicators, etc.) as well as UI (text and narrative data including patients comments, comments by multiple physicians, descriptions of affliction by patients and PCPs) at the level of each patient. Because of the vast amount of paper-based information that needed to be digitized, the hospital carried out the digitization incrementally and in such a way that batches of digitized patient records were made available to physicians at the start of each month.<sup>10</sup> The order of digitization was determined by each patient’s unique ID number, which consisted of a 12- digit alphanumeric code (a standard nine-digit SSN identifier followed by a three-digit alphanumeric code assigned by the hospital).<sup>11</sup>

To avoid any discrimination concerns, and to comply with JCAHO guidelines on digitizing patient records, the hospital intentionally avoided using any patient information other than the patient ID to sequence the digitization. Additionally, the rate of digitization progress varied according to medical information type. For instance, in the month of January, a patient may have had all clinical tests (SI) digitized, but some of the UI may not have been digitized until February. Therefore, from the physician’s perspective, there existed exogenous variation in the percentage of patients whose records were automated in each category. This variation serves a key purpose in our research: it allows us to identify the impact of digitization of specific types of information (SI, UI, and SSI) on the efficiency and quality of care delivered by individual physicians. We constructed our measures by aggregating this visit-level information for each physician for each measurement period (month).<sup>12</sup> In the next section, we discuss how each of the variables was operationalized.

Table 1a. Summary Statistics of Predictors and Dependent Variables

<table><tr><td>Variable</td><td>Mean</td><td>Std. dev.</td><td>Min</td><td>Max</td></tr><tr><td>Duration</td><td>29.4201</td><td>11.0989</td><td>0.6300</td><td>62.0400</td></tr><tr><td>Co_var</td><td>0.5959</td><td>0.0909</td><td>0.0239</td><td>0.8645</td></tr><tr><td>Comp</td><td>0.8033</td><td>0.1533</td><td>0.2197</td><td>1.0000</td></tr><tr><td>SI</td><td>0.6273</td><td>0.1800</td><td>0.2430</td><td>0.9930</td></tr><tr><td>SSI</td><td>0.3121</td><td>0.1825</td><td>0.0296</td><td>0.8673</td></tr><tr><td>Pre_proc</td><td>0.1664</td><td>0.1240</td><td>0.0004</td><td>0.6208</td></tr><tr><td>Cr_pal</td><td>5.1857</td><td>1.6806</td><td>0.8600</td><td>9.0000</td></tr></table>

Table 1b. Matrix of Correlation: Predictors and Dependent Variable

<table><tr><td></td><td></td><td>Duration</td><td>SI</td><td>UI</td><td>SSI</td><td>Pre_Proc</td><td>DM &amp; SI Fit</td><td>TE &amp; SI Fit</td><td>DM &amp; UI Fit</td><td>TE &amp; UI Fit</td><td>CR_Pal RAW</td></tr><tr><td>Duration</td><td>R</td><td>1.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SI</td><td>R</td><td>-0.226</td><td>1.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>p-value</td><td>8.24E-12</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>UI</td><td>R</td><td>-0.256</td><td>0.883</td><td>1.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>p-value</td><td>0.</td><td>0.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SSI</td><td>R</td><td>-0.23</td><td>0.801</td><td>0.878</td><td>1.</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>p-value</td><td>3.619E-12</td><td>0.</td><td>0.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Pre_Proc</td><td>R</td><td>-0.197</td><td>0.267</td><td>0.245</td><td>0.221</td><td>1.</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>p-value</td><td>2.951E-9</td><td>0.</td><td>0.</td><td>2.461E-11</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>DM &amp; SI Fit</td><td>R</td><td>-0.017</td><td>-0.021</td><td>0.002</td><td>-0.006</td><td>-0.014</td><td>1.</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>p-value</td><td>0.62</td><td>0.533</td><td>0.953</td><td>0.85</td><td>0.682</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>TE &amp; SI Fit</td><td>R</td><td>0.061</td><td>-0.018</td><td>-0.033</td><td>-0.037</td><td>-0.003</td><td>0.005</td><td>1.</td><td></td><td></td><td></td></tr><tr><td></td><td>p-value</td><td>0.068</td><td>0.59</td><td>0.324</td><td>0.263</td><td>0.935</td><td>0.876</td><td></td><td></td><td></td><td></td></tr><tr><td>DM &amp; UI Fit</td><td>R</td><td>0.026</td><td>0.016</td><td>0.017</td><td>0.012</td><td>-0.032</td><td>0.011</td><td>-0.165</td><td>1.</td><td></td><td></td></tr><tr><td></td><td>p-value</td><td>0.43</td><td>0.634</td><td>0.612</td><td>0.712</td><td>0.334</td><td>0.738</td><td>6.811E-7</td><td></td><td></td><td></td></tr><tr><td>TE &amp; UI Fit</td><td>R</td><td>-0.044</td><td>-0.017</td><td>-0.002</td><td>0.004</td><td>0.028</td><td>0.083</td><td>0.033</td><td>-0.09</td><td>1.</td><td></td></tr><tr><td></td><td>p-value</td><td>0.184</td><td>0.618</td><td>0.963</td><td>0.895</td><td>0.395</td><td>0.013</td><td>0.318</td><td>0.007</td><td></td><td></td></tr><tr><td>CR_Pal RAW</td><td>R</td><td>0.075</td><td>-0.06</td><td>-0.07</td><td>-0.077</td><td>0.056</td><td>-0.012</td><td>-0.03</td><td>-0.018</td><td>0.034</td><td>1.</td></tr><tr><td></td><td>p-value</td><td>0.025</td><td>0.072</td><td>0.038</td><td>0.021</td><td>0.096</td><td>0.712</td><td>0.366</td><td>0.589</td><td>0.314</td><td></td></tr></table>

## 4.2 Operationalization of Key Variables

The summary descriptive statistics of all variables are shown in Tables 1A and 1B.

## 4.2.1 Dependent Variables

In this section, we discuss the operationalization of the dependent variables.

1. Mean Physician-Patient Contact Duration (Duration) <sup>13</sup> : This is calculated based on the (electronic) log of the physician-patient visit time.<sup>14</sup> For the $i ^ { t h }$ physician, the time spent with a patient (including the preprocessing time where applicable) at the j<sup>th</sup> visit is given by $T _ { i j }$ . If the physician had N visits during a particular month, then the mean of the contact duration is defined as $\begin{array} { r } { D u r a t i o n _ { i } = \frac { \sum _ { j = 1 } ^ { N } ( T _ { i j } ) } { N } } \end{array}$ . This was indexed by the measurement period (t) to yield the mean contact duration for the $i ^ { t h }$ physician in the $t ^ { t h }$ month given by Duration<sub>it</sub> .

2. Visit Completion Rate (VCR): This is a binary variable that measures whether the patient’s purpose of the visit (to a particular physician) was fully addressed during the visit. Patients responded with $\mathrm { \cdots { Y e s ^ { , , } } } ( = 1 )$ if they felt that the purpose of their scheduled visit was fully achieved and $\bar { \bf \Phi } \bar { \bf N } \mathrm { o } ^ { 3 } \mathrm { ~ ( = 0 ) ~ }$ if it was not. If the $i ^ { t h }$ physician had N visits during month t, where k visits received a rating of 1, then for that physician his mean VCR score (for that month) is given by $\begin{array} { r } { V C R _ { i t } = \frac { k } { N } \leq } \end{array}$ 1. Each visit completion rating was provided by exactly one patient for one physician at the level of an individual visit.

## 4.2.2 Digitization-Related Variables

The clinical information flows being digitized comprise two different kinds <sup>15</sup> of information, structured and unstructured. A patient’s paper-based UI must first be digitized before the physician can edit it to create SSI.

1. Structured Information (SI): In every month, patients made visits to the physicians. For some of these patients the paper-based SI information was fully digitized, while for others it was not. This variable measures the fraction of visits made to a physician during the month for which all available SI for the visiting patients was digitized. <sup>16</sup> If a physician received 100 visits during a month, of which 40 visits were from patients with fully digitized structured information (and 60 visits were from patients who did not have fully digitized structured information), then this physician’s SI score for the month would be 0.40. Note that this variable is based on the average of all visits during the month and can therefore capture multiple visits by the same patient. In general, for the $i ^ { t h }$ physician in the $t ^ { t h }$ measurement period, if m<sub>it</sub> visits had completely digitized SI and the physician received a total of $M _ { i t }$ visits during the period, then $S I _ { i t } =$ $\frac { m _ { i t } } { M _ { i t } } \forall i , t .$

2. Unstructured Information (UI): This variable measures the fraction of visits made to a physician during the month for which all available UI at the patient level was digitized. If a physician received 100 visits during a month, of which 30 visits were from patients with fully digitized UI (and 70 were from patients whose UI sets were not yet digitized and still in paper form in case files), then this physician’s UI score for the month was 0.30. For the $\dot { \iota } ^ { t h }$ physician in the $t ^ { t h }$ measurement period, if $n _ { i t }$ visits were from patients that had complete digitized case histories out of a total of $N _ { i t }$ visits during the period, then $U I _ { i t } =$ $\begin{array} { r } { \frac { n _ { i t } } { N _ { i t } } \forall i , t . } \end{array}$

3. Semistructured Information (SSI): This variable measures the fraction of patient visits made to a physician during the month for which the patient’s record had been edited by the physician and one or more of the following elements of SSI had been created: searchable keywords, hyperlinks, annotations, or terminological inserts from drop-down menus. If a physician received 100 visits during a month, of which 25 visits were from patients that had SSI (and 75 were from patients without SSI), then this physician’s SSI score for the month was 0.25. For the $\bar { \mathbf { \chi } } _ { i ^ { t h } } ^ { * }$ physician in the $t ^ { t h }$ measurement period, if $n _ { i t }$ visits were from patients that had SSI in the EHR, out of a total of $N _ { i t }$ visits during the period, then $\begin{array} { r } { S S I _ { i t } = \frac { n _ { i t } } { N _ { i t } } \forall i , t } \end{array}$

4. Preprocessing (Pre\_proc): We captured the extent to which a physician preprocessed patient information prior to their visits. Typically, physicians preprocessed patient information for between 10% and 25% of visits. For the $i ^ { t h }$ physician in the $t ^ { t h }$ measurement period, if the physician received total of $P _ { i t }$ visits during the period, and the physician preprocessed information about $\alpha _ { i t }$ visits, then the preprocessing variable is given by: ?????? $\begin{array} { r } { p r o c _ { i t } = \frac { \alpha _ { i t } } { P _ { i t } } } \end{array}$ . Note that all four variables above are positive fractions.

Reasons for patient visits (including pathologies, billable tasks, test ordering and specialist task references) were obtained from ICD-10-CM and medical billing reference (MBR) codes. The reasons captured from the ICD-10-CM codes were matched with internal MBR codes for generating the list of tasks performed. In all, there were 47 different kinds of highlevel tasks that emerged. It is important to note that we distinguish between a category of tasks and an instance of a task category. For example, a category of tasks is “prescribing drugs,” while an instance of the category is prescribing Metformin HCL; similarly, a category of tasks is “ordering a lab test” while an instance of the task is ordering a test for A1C Hemoglobin. Our categorization of tasks is based on high-level categories of tasks and not individual instances of tasks. These 47 distinct, high-level tasks were extracted on the basis of the first seven digits of the

ICD-10-CM system code and the six-digit billing reference code (this combination generates the diagnosis, pathology, and billable task details<sup>17</sup>).

These tasks were then categorized into 12 different task systems based on the task interdependencies. <sup>18</sup> Each patient visit was modeled in terms of one or more of the 47 high-level tasks that were performed during the visit. This resulted in 12 different task combinations or systems of tasks.<sup>19</sup> We term each of these 12 different task combinations as an activity system because this system of tasks describes the activities performed by the specialist during the visit. Thus, there were 12 activity systems in all. Six of these twelve activity systems had “pairs” in that each activity system had another one that was very similar to it (differing only very slightly in task type) with an isomorphic graph structure.<sup>20</sup> These six activity systems were combined with their nearly identical pairs to yield six very distinct activity systems. Of these, three belonged to the FCAS type and three to the PCAS type.<sup>21</sup> We remind the reader that our interest is in the visit duration when the patient actually visits a specialist physician. Not all the administrative tasks would require a physician visit and some tasks would be performed by administers and would not require a patient visit. Tasks for which patients do not visit the specialist are not considered as a part of this study.

5. Task Technology Fit Rating: We identified two key task characteristics for each task: decision-making and task execution. For each of these two task characteristics, the extent to which technology supported the performance of the task was rated on a 7- point Likert scale based on Goodhue (1995). Therefore, for the $i ^ { t h }$ task, the extent of fit between the technology and the decision-making task characteristic is given by $D M T _ { i }$ where $1 \leq D M \bar { T } _ { i } \leq 7$ and the extent of fit between the technology and the task execution task characteristic is given by $T E _ { i }$ where $1 \leq T E T _ { i } \leq 7 .$

6. TTF Score at the Level of the Activity System: For an activity system consisting of ?? tasks, we compute the weighted average rating of each of the two task characteristics, where the dependency index of each task, given by $D _ { i }$ , serves as the weight.<sup>22</sup> Thus the weighted average rating of the decision-making characteristic at the level of the $j ^ { t h }$ activity system is given by: $\begin{array} { r } { D M _ { j } = \frac { 1 } { K } \left( \frac { \sum _ { i = 1 } ^ { K } \left( D M T _ { i } \times D _ { i } \right) } { \sum _ { i = 1 } ^ { k } D _ { i } } \right) } \end{array}$ . Similarly, the weighted rating of the task execution characteristic at the level of the $j ^ { t h }$ activity system is given by: $T E _ { j } =$ $\frac { 1 } { K } \left( \frac { \sum _ { i = 1 } ^ { K } ( T E T _ { i } \times D _ { i } ) } { \sum _ { i = 1 } ^ { k } D _ { i } } \right)$ . The task interdependency interrater reliability given by Fleiss kappa (free marginal kappa) was 0.89 for task interdependency values and 0.92 for Critical Task Characteristic values, indicating a very high level of reliability.

## 4.2.3 Control Variables

## 2. Dummy Variables:

1. Patient Affliction Level (Cr\_pal): This variable measures the severity of patient affliction levels, as rated by a physician,<sup>23</sup> based on the widely followed norms set by the JCAHO (and used by health quality survey systems such as IQIP and Press Ganey). This is a scale variable rated on a 0 to 10 scale where 0 is the lowest and 10 the highest level of affliction.<sup>24</sup>

a. Activity system type: The 3 FCAS activity systems were given the dummy variables AS1, AS2, and AS3, and the 3 PCAS activity systems were given AS4, AS5, and AS6.

b. Time dummies: Dummy variables were used, one each, for each period.

## 5 Results and Discussion

We ran multiple estimation models to estimate the impact of our theorized predictors. In this section we discuss the results of the analysis of each of these models.

## 5.1 Efficiency: Patient-Physician Contact Duration

We use two measures to analyze the efficiency of healthcare delivery: mean physician-patient contact duration and scheduled patient volume. The mean contact duration determines the number of patients that a specialist can see in any day. We adopt the following empirical model to estimate digitization’s impact on mean contact duration:

$$
\begin{array}{r l} & D u r a t i o n _ {i t} \\ & = \beta_ {0} + \beta_ {1} S I _ {i t} + \beta_ {2} S S I _ {i t} + \beta_ {3} P r e \_ p r o c _ {i t} \\ & + \beta_ {4} P r e \_ p r o c _ {i t} \times S S I _ {i t} + \beta_ {5} S I _ {i t} \times D M _ {i} \\ & + \beta_ {6} S S I _ {i t} \times D M _ {i} + \beta_ {7} S I _ {i t} \times T E _ {i} \\ & + \beta_ {8} S S I _ {i t} \times T E _ {i} + \beta_ {9} C r \_ p a l _ {i t} \\ & + A c t i v i t y S y s t e m D u m m i e s \\ & + P h y s i c i a n F i x e d E f f e c t s \\ & + T i m e P e r i o d D u m m i e s + \varepsilon_ {i t} \end{array}\tag{1}
$$

In the above specification, the subscripts denote that these measures are across physicians (i) and over time periods (t). To demonstrate the moderating impact of activity systems, we ran the estimation models on two separate panels, one each for FCAS and PCAS. In Equation (1), we are interested in estimating how digitizing structured information, as well as the creation of SSI and preprocessing, influence the mean contact duration of a patient visit. In particular, we are interested in the interaction between the TTF for the critical task characteristic of each activity system (decision-making and task execution, respectively) and the digitization of patient information types.

We include several control variables to account for other factors that might influence the contact duration, including controls for activity systems and patient affliction levels. All variables were mean centered to remove correlations. It is possible that the contact duration may change over time, which motivated us to add month dummies to allow for more flexibility to capture the time-related impacts. To guard against the possibility of conditional heteroskedasticity, which can influence the estimation of standard errors, we report the Huber-White clustered robust standard errors in our estimation.

In Table 2 we provide the full results of the estimation models on both panels. Columns (1) through (3) correspond to the results for FCAS while (4) through (6) correspond to the results for PCAS. The two panels present both similarities and contrasts. First, we find that in both cases, digitization alone is not a predictor of lower mean contact duration (efficiency gains). In the presence of task interdependencies, it is the interaction of digitization of SI and SSI with the weighted mean TTF of the CTC of the activity system that predicts gains in mean contact duration. The estimation model presented in the two panels also presents contrasting results that provide strong support for the moderating impact of activity systems.

We draw the reader’s attention to the four interaction terms between the two kinds of information and the two CTCs. For FCAS, the key factor that determines mean physician-patient contact duration is the extent to which progressive digitization supports the CTC of decision-making; for PCAS, it is the extent to which technology supports task execution. In both cases, the coefficients are negative and highly significant (FCAS beta = -408.5, p < 0.001; PCAS beta = -36.58, p < 0.001). In symmetric contrast, it is seen that for FCAS, the interaction terms with the task execution characteristic do not have any impact on mean contact duration; similarly, for PCAS, the interaction terms with the decision-making characteristic do not have any impact. This is precisely what we theorized in Section 2. We also tested the panel data to ascertain whether these results would hold if we pooled all the activity systems together at the level of the physician (specialist) and ran the estimation models. The estimation model based on pooled data did not find that any of TTF ratings were a significant predictor of outcomes. We also tested the model by retaining the activity system-level information but combining the two different kinds of activity systems, FCAS and PCAS, into a single panel. Again, none of the TTF factors turned out to be significant.

It is clear that in the presence of task interdependencies, the structure of the interdependencies, i.e., the structure of the activity system, has a strong moderating impact on the extent to which TTF factors drive efficiency gains. Furthermore, it is the TTF with the principal task characteristic measured at the level of the activity system and not at the individual task level that drives gains from digitization. In Section 2, we drew on extant research in health informatics to theorize that structured information would be the key enabler of clinical decision-making, while for task execution, both structured and semistructured information would be important. We find that this is indeed the case. These findings provide strong support for H1a and H1b. Next, we look at preprocessing of patient information by physicians and its impact on efficiency of care delivery.

Table 2: Effects of Digitization on Mean Contact Duration

<table><tr><td rowspan="2"></td><td colspan="4">FCAS</td><td colspan="4">PCAS</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td></td><td>(4)</td><td>(5)</td><td>(6)</td><td></td></tr><tr><td>Variables</td><td>Physician-fixed effects</td><td>Physician-fixed effects with activity system controls</td><td>Physician-fixed effects with activity system controls</td><td>VIF</td><td>Physician-fixed effects</td><td>Physician-fixed effects with activity system controls</td><td>Physician-fixed effects with activity system controls</td><td>VIF</td></tr><tr><td>SI</td><td>-2.244(3.322)</td><td>-1.223(3.392)</td><td>-1.223(4.244)</td><td>8.63</td><td>1.185(2.496)</td><td>1.099(2.500)</td><td>1.099(3.184)</td><td>2.69</td></tr><tr><td>SSI</td><td>-2.972(2.313)</td><td>-2.641(2.317)</td><td>-2.641(2.336)</td><td>4.15</td><td>2.999(2.483)</td><td>3.067(2.488)</td><td>3.067(2.534)</td><td>2.69</td></tr><tr><td>Pre_proc</td><td>-9.088***(2.062)</td><td>-9.160***(2.060)</td><td>-9.160***(2.470)</td><td>1.51</td><td>-21.65***(5.811)</td><td>-21.60***(5.815)</td><td>-21.60*(10.59)</td><td>1.04</td></tr><tr><td>SSI*Pre_proc</td><td>-49.30***(12.13)</td><td>-47.03***(12.17)</td><td>-47.03***(9.220)</td><td>1.25</td><td>-108.1***(32.85)</td><td>-108.0***(32.93)</td><td>-108.0**(49.01)</td><td>1.03</td></tr><tr><td>SI*DM</td><td>-408.2***(10.29)</td><td>-408.5***(10.27)</td><td>-408.5***(8.740)</td><td>1.05</td><td>3.280(11.60)</td><td>3.262(11.61)</td><td>3.262(18.44)</td><td>1.02</td></tr><tr><td>SSI*DM</td><td>15.16(11.98)</td><td>15.55(11.96)</td><td>15.55(11.31)</td><td>1.10</td><td>-2.966(11.01)</td><td>-2.741(11.02)</td><td>-2.741(12.97)</td><td>1.10</td></tr><tr><td>SI*TE</td><td>3.996(18.51)</td><td>3.383(18.50)</td><td>3.383(17.50)</td><td>4.22</td><td>-36.41***(11.42)</td><td>-36.58***(11.43)</td><td>-36.58**(16.50)</td><td>1.06</td></tr><tr><td>SSI*TE</td><td>4.368(20.36)</td><td>4.781(20.34)</td><td>4.781(22.20)</td><td>4.22</td><td>-221.6***(10.43)</td><td>-221.6***(10.44)</td><td>-221.6***(14.43)</td><td>1.06</td></tr><tr><td>AS2</td><td></td><td>-0.238(0.509)</td><td>-0.238(0.425)</td><td>1.36</td><td></td><td></td><td></td><td></td></tr><tr><td>AS3</td><td></td><td>0.771(0.521)</td><td>0.771(0.510)</td><td>1.42</td><td></td><td></td><td></td><td></td></tr><tr><td>AS5</td><td></td><td></td><td></td><td></td><td></td><td>-0.344(0.682)</td><td>-0.344(0.843)</td><td>1.34</td></tr><tr><td>AS6</td><td></td><td></td><td></td><td></td><td></td><td>-0.609(0.679)</td><td>-0.609(0.810)</td><td>1.34</td></tr><tr><td>Cr_pal</td><td>0.452***(0.136)</td><td>0.454***(0.136)</td><td>0.454***(0.136)</td><td>1.07</td><td>8.621***(0.402)</td><td>8.616***(0.403)</td><td>8.616***(0.406)</td><td>1.09</td></tr><tr><td>Constant</td><td>1.810(1.298)</td><td>1.940(1.306)</td><td>1.940(1.660)</td><td></td><td>-1.192(0.964)</td><td>-0.876(1.041)</td><td>-0.876(1.005)</td><td></td></tr><tr><td>other controls</td><td>Month dummies</td><td>Month dummies</td><td>Month dummies</td><td></td><td>Month dummies</td><td>Month dummies</td><td>Month dummies</td><td></td></tr><tr><td>Observations</td><td>891</td><td>891</td><td>891</td><td></td><td>895</td><td>895</td><td>895</td><td></td></tr><tr><td>R-squared</td><td>0.683</td><td>0.684</td><td>0.684</td><td></td><td>0.586</td><td>0.586</td><td>0.586</td><td></td></tr><tr><td colspan="9">Note:Huber White robust clustered standard errors in parentheses for Columns (3) and (6). *** p&lt;0.01, ** p&lt;0.05, * p&lt;0.1</td></tr></table>

## 5.2 Efficiency: Contact Duration and Preprocessing

From Table 2, it can be seen that in both kinds of activity systems, preprocessing has a significant impact on the mean physician-patient contact duration. In both cases, the coefficients are negative and highly significant $( \mathrm { F C A S b e t a } = - 9 . 1 6 0 , p < 0 . 0 0 I ; \mathrm { P C A S }$ beta $= - 2 1 . 6 0 , p < 0 . 0 0 I )$ . As we observed in Section 3.3, preprocessing has a twofold impact: it familiarizes the specialist with the patient’s condition, and it aids the formation of transactive memory. When the specialist sees the SSI that he and other specialists have created, TM formation is further enhanced. Therefore, we would expect both kinds of activity systems to have a complementarity between preprocessing and the creation of SSI. Table 2 shows that this is indeed the case. The interaction terms are negative and highly significant in both cases (FACS beta = -47.03, p < 0.001; PCAS beta $= - 1 0 8 . 0 , p < 0 . 0 0 1 )$ , providing evidence in support of H2a and H2b. Next, we investigate the perceived quality of care and how it is influenced by the digitization of patient information.

## 5.3 Perceived Quality of Care: Visit Completion Rates

As observed in the discussion of H3a and H3b, it has been shown in extant research on service quality that evaluations of service quality are not solely based on service outcomes; the process of service delivery is also important in shaping the perception of service quality (Gronroos 1982; Lehtinen and Lehtinen 1982; Lewis and Booms 1983). Our quality measure is the extent to which patients assess the objectives of their visit to the physician as being completely addressed. This quality measure is in consonance with the recommendations of Press Ganey (Press Ganey 2010) and JCAHO guidelines. We employ the following model to estimate the impact of factors that influence the VCRs.

$$
\begin{array}{r l} & V C R _ {i t} \\ & = \beta_ {0} + \beta_ {1} S I _ {i t} + \beta_ {2} S S I _ {i t} + \beta_ {3} P r e \_ p r o c _ {i t} \\ & + \beta_ {4} S I _ {i t} \times D M _ {i} + \beta_ {5} S S I _ {i t} \times D M _ {i} \\ & + \beta_ {6} S I _ {i t} \times T E _ {i} + \beta_ {7} S S I _ {i t} \times T E _ {i} \\ & + \beta_ {8} P r e \_ p r o c _ {i t} \times S S I _ {i t} + \beta_ {9} C r \_ p a l _ {i t} \\ & + A c t i v i t y S y s t e m D u m m i e s \\ & + P h y s i c i a n F i x e d E f f e c t s \\ & + T i m e P e r i o d D u m m i e s + \varepsilon_ {i t} \end{array}\tag{3}
$$

As stated previously, to demonstrate the moderating impact of the activity system we ran the estimation models on two separate panels, one each for the FCAS and PCAS. Within each activity system (panel) we distinguish between three categories of patient visits. The first is patients with high affliction levels with digitized information, the second is patients with low affliction levels and digitized information, and the third is patients whose information was not yet digitized (their information remained in paper-based repositories). To separate the patients into two categories of high and low affliction, we partitioned the patients into two groups based on their patient affliction level ratings (Cr\_Pal) and ran a subgroup separation test (test of mean and variance). The two distributions are clearly separate,<sup>25</sup> as the left tail of affliction values of the high affliction intensity patients was more than three standard deviations to the right of the mean of the low affliction intensity patients (µ<sub>L</sub> $= 2 . 6 3 , \ \sigma _ { L } = 1 . 0 9 ; \mu _ { H } = 8 . 0 6 , \ \sigma _ { H } = 1 . 0 3 )$ . This was confirmed by a t-test (test of means) with a p-value < 0.001. Therefore, within each panel (activity system type) we have three subgroups of patients. We ran the estimation model in each subgroup to contrast the findings. The results are shown in Table 3.

VIFs: There are six estimation models presented in Table 3. We would need to add six additional columns to provide the entire range of VIFs for each of the six models. Given page-width constraints, it is not possible to add these six columns to Table 3. Instead, we provide the range of VIFs for each model in Table 4. It can be seen from Table 4 that, in all cases, the VIF range is well under the permissible limit of 10. There is therefore no threat of multicollinearity (in part because we have mean centered all variables).

We now look at the results of the analysis provided in Table 3. By comparing Columns (1) and (2) and (4) and (5) in Table 3, it is the interaction of digitization of SI and SSI with the decision-making (DM) task characteristic that impacts visit completion rates for FCAS, (High Cr\_pal: SI\*DM, $\beta = 4 . 7 0 3$ , SSI\*DM, $\beta = 3 . 5 7 6 ; p \ < \ 0 . 0 0 1$ ; Low Cr\_Pal: SI\*DM, ?? = 1.986, SSI\*DM, $\beta = 4 . 7 9 0 ; p < 0 . 0 0 1 )$ . For PCAS it is the interaction of these two information types with the task execution (TE) task characteristic that drives visit completion rates (High Cr\_pal: SI\*TE, $\beta =$ 0.970, SSI\*TE, $\beta = 2 . 9 1 2 ; p < 0 . 0 0 1 ;$ Low Cr\_pal: SI\*TE, ?? = 3.01, p < 0.001). This is both consistent with our theorizing and with the prior hypotheses. We draw the reader’s attention to Columns (3) and (6) of Table 3. These are the results of running the same estimation model for the patient subgroup for which the information was not digitized. In marked contrast to Columns (1) and (2) and (4) and (5), Columns 3 and 6 show that none of the factors have any impact on the VCRs for patients with paper-based information.

Table 3: Effects of Digitization on Visit Completion Rate

<table><tr><td rowspan="2"></td><td colspan="3">FCAS</td><td colspan="3">PCAS</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td></tr><tr><td>Variables</td><td>Physician-fixed effectsCR_pal High</td><td>Physician-fixed effectsCR_pal Low</td><td>Physician- fixed effectsPaper-Based</td><td>Physician- fixed effectsCR_pal High</td><td>Physician- fixed effectsCR_pal Low</td><td>Physician- fixed effectsPaper-Based</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SI</td><td>0.0399(0.0464)</td><td>0.00410(0.0481)</td><td>-2.61e-06(0.0341)</td><td>0.0158(0.0338)</td><td>-0.00323(0.0285)</td><td>0.00249(0.0262)</td></tr><tr><td>SSI</td><td>0.0409(0.0309)</td><td>0.00554(0.0285)</td><td>4.50e-05(0.0297)</td><td>-0.0343(0.0361)</td><td>-0.0158(0.0351)</td><td>0.00600(0.0308)</td></tr><tr><td>Pre_proc</td><td>0.104***(0.0288)</td><td>0.161***(0.0295)</td><td>-0.0208(0.0174)</td><td>0.400***(0.0732)</td><td>0.785***(0.0724)</td><td>-0.00337(0.0237)</td></tr><tr><td>SSI*Pre_proc</td><td>1.864***(0.162)</td><td>1.986***(0.156)</td><td>0.0558(0.157)</td><td>1.812***(0.356)</td><td>2.462***(0.377)</td><td>-0.0882(0.148)</td></tr><tr><td>SI*DM</td><td>4.703***(0.129)</td><td>4.790***(0.132)</td><td>-0.0439(0.0815)</td><td>0.0900(0.126)</td><td>-0.134(0.177)</td><td>-0.0313(0.132)</td></tr><tr><td>SSI*DM</td><td>3.576***(0.125)</td><td>2.525***(0.103)</td><td>-0.110(0.0876)</td><td>0.0708(0.136)</td><td>-0.124(0.193)</td><td>-0.0130(0.0871)</td></tr><tr><td>SI*TE</td><td>0.140(0.213)</td><td>0.0417(0.218)</td><td>0.0555(0.0956)</td><td>0.970***(0.128)</td><td>3.010***(0.116)</td><td>0.00970(0.128)</td></tr><tr><td>SSI*TE</td><td>-0.00475(0.116)</td><td>0.00575(0.114)</td><td>0.0689(0.0813)</td><td>2.912***(0.172)</td><td>0.348(0.296)</td><td>0.0183(0.104)</td></tr><tr><td>AS2</td><td>0.00362(0.00846)</td><td>0.00269(0.00775)</td><td>-0.00173(0.00491)</td><td></td><td></td><td></td></tr><tr><td>AS3</td><td>0.00389(0.00709)</td><td>0.00304(0.00720)</td><td>-0.00253(0.00550)</td><td></td><td></td><td></td></tr><tr><td>AS5</td><td></td><td></td><td></td><td>-0.00844(0.00737)</td><td>-0.00389(0.00724)</td><td>0.00176(0.0107)</td></tr><tr><td>AS6</td><td></td><td></td><td></td><td>-0.00397(0.00767)</td><td>-0.0123*(0.00706)</td><td>-0.000642(0.00968)</td></tr><tr><td>Constant</td><td>-0.0209(0.0178)</td><td>-0.0150(0.0189)</td><td>0.0159(0.0119)</td><td>0.00295(0.00980)</td><td>0.0278(0.0174)</td><td>-0.0137(0.0144)</td></tr><tr><td>other controls</td><td>Month dummies</td><td>Month dummies</td><td>Month dummies</td><td>Month dummies</td><td>Month dummies</td><td>Month dummies</td></tr><tr><td>Observations</td><td>881</td><td>881</td><td>881</td><td>890</td><td>890</td><td>890</td></tr><tr><td>R-squared</td><td>0.713</td><td>0.694</td><td>0.060</td><td>0.453</td><td>0.430</td><td>0.014</td></tr><tr><td colspan="7">Note: Huber-White robust clustered standard errors in parentheses. *** p&lt;0.01, ** p&lt;0.05, * p&lt;0.1</td></tr></table>

Table 3: Effects of Digitization on Visit Completion Rate

<table><tr><td rowspan="3"></td><td colspan="3">FCAS</td><td colspan="3">PCAS</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(1)</td><td>(2)</td><td>(3)</td></tr><tr><td>Cr_pal High</td><td>Cr_pal Low</td><td>Paper</td><td>CR_pal High</td><td>CR_pal Low</td><td>Paper</td></tr><tr><td>Minimum VIF Value</td><td>1.062</td><td>1.049</td><td>1.211</td><td>1.071</td><td>1.127</td><td>1.102</td></tr><tr><td>Maximum VIF Value</td><td>6.441</td><td>6.560</td><td>7.310</td><td>5.032</td><td>6.314</td><td>7.740</td></tr></table>

Furthermore, none of the factors, not even the time dummies, have any impact on the VCRs for patients with paper-based information for whom the Adj $\mathbf { R } ^ { 2 }$ value is zero, showing that the model does not explain any of the observed variance. We offer this to establish convergent discriminant validity—i.e., the predictors that cohere theoretically only need to predict those effects that are theorized and need to vary from those that are in opposition to the theorized effects.

Finally, we turn our attention to the question of complementarities between preprocessing and specialist-created semistructured information. It is seen from Columns (2) and (3) and (6) and (7) that for both activity systems, the main effect and the interaction effect both hold (FCAS: Pre\_proc $\beta =$ 0.104, Pre\_proc\*SSI $\beta = 1 . 8 6 4$ $p < 0 . 0 0 1 ;$ PCAS Pre\_proc, $\beta = 0 . 7 8 5$ , Pre\_proc\*SSI $\beta = 2 . 4 6 2$ $p \ <$ 0.001). This evidence supports H4a and H4a. In the findings based on the analysis of all three estimation models, it is clear that outcomes of efficiency and perceived quality are explained by the interaction of the digitization of SI and SSI with the weighted average TTF between technology and CTC of the entire activity system. A question that arises in this context of our findings is: Are there other possible explanations for our findings? Or, more generally, how robust are our estimation models? We address these two questions in the next section.

## 5.4 Alternative Explanations and Tests of Model Robustness

Above, we analyze the impact of digitization on various performance measures separately. Since these measures reflect the behavior of the same group of physicians, one would naturally expect the unobserved errors to correlate with each other. Note that our findings remain unbiased even if the correlations are nonzero. However, we could improve the efficiency of estimation by exploiting the correlations in the error term. Therefore, we apply the seemingly unrelated regression (SUR) approach, originally proposed by Zellner (1962). This method conducts estimation on the system of equations, rather than assuming each equation to be independent of each other. For each subsample we conducted the Breusch-Pagan test, which rejects the independence assumption at $p \ <$ 0.001. Indeed, the standard errors from SUR estimation are typically smaller than what we had before, while the magnitudes are almost identical.<sup>26</sup> The improved accuracy in estimation gives us further confidence in our findings.

We next turn our attention to the robustness of the finding that it is the weighted average TTF score measured at the level of the activity system that matters. We tested alternative models to see if the TTF ratings at the level of the individual tasks and/or their interaction with the digitization of SI and SSI would matter. We tried substituting the weighted average TTF score at the level of the activity system with TTF scores of individual tasks, and none of these had any predictive power. <sup>27</sup> In the presence of task interdependencies, it is the weighted average TTF factor measured at the level of the activity system that predicts outcomes.

We also tested the robustness of the finding that the perceived quality of care—i.e., the visit completion rate—goes up with increasing digitization. This could well happen purely because of learning: as specialists learn more about their patients, it stands to reason that the perceived quality of care increases. To test whether there is indeed an impact of digitization and separate it from specialist learning, we compared the VCRs for the patients whose information had been digitized with the patients whose information was still in paperbased records. For both FCAS and PCAS activity systems, the weighted average mean visit completion rates were higher for the groups of patients whose information had been digitized.

While this evidence supports our position, it is not conclusive. We wanted to know whether the increase in visit completion rates from one period to another was caused by learning or by digitization. To show digitization’s impact, we first computed the mean VCRs in each period for both groups of patients. Then we took the first differences—i.e., the extent to which visit completion rate in the $( t + 1 ) ^ { t h }$ period was greater than the rate in the $t ^ { t h }$ period. This gave us two subsamples of weighted average VCRs for 11 periods (the method of first differences nullifies the first period). We tested to see if the means of these two subsamples were different. We rejected the null hypothesis that $\mu _ { D } = \mu _ { P B }$ at $p < 0 . 0 0 1$ for both activity systems (where the subscripts $" \mathrm { D } ^ { \prime \mathrm { 3 } }$ and “PB” denote “digital” and “paper based,” respectively).

Finally, we questioned whether there could be hospital-wide trends that could have driven outcomes of productivity and quality. The canonical method in a panel data to isolate the impact of the predictors on the outcome variable is the first difference (FD) model. The FD operator measures change in the DV because of change in the regressors. The results of the FD estimate were very consistent with those of the main estimation models offering further evidence of model robustness. <sup>28</sup> In the next section, we discuss the contributions of our research and its limitations and possible extensions.

## 6 Discussion

In Section 2, we synthesized three streams of research—theory of task technology fit, the theory of task dependencies, and activity systems (organizational theory)—to develop a theoretical framework to explain how the digitization of patient information impacted outcomes in chronic care delivery. We discuss the contributions of this study in light of these findings.

## 6.1 Contributions of This Study

This study makes several contributions to theory and also yields three recommendations to practitioners in the healthcare IT space. We begin with the theoretical implications and contributions. First, we formulate the idea of a critical task characteristic (CTC) for an entire activity system. We show that the CTC of an activity system is determined by the structure of the activity system. We draw on extant research from the theory of task dependencies and on activity systems in organizational theory to show that for FCAS the CTC is decision-making and for PCAS it is task execution. For an activity system consisting of a set of tasks densely connected with multiple interdependencies between them (FCAS), the danger that decisionmaking errors will spill over from one task to another is significant and the decision-making task characteristic that emerges is the critical one. For an activity system that is loosely connected with some independent task clusters in it (PCAS), the challenge lies in executing individual tasks accurately and task execution is the critical task characteristic of the activity system. Thus, unlike in the case of individual tasks, where the fit between a technology and a task characteristic can be measured in a straightforward manner, the CTC of an activity system emerges from the structure of the activity system.

Second, we formulate a new composite measure of Task Technology Fit (TTF), a weighted measure of fit that captures the level of interdependencies between tasks that constitute an activity system. We show that it is the extent of fit between the CTC and technology measured at the level of the activity system—i.e., the weighted average fit of all tasks in the activity system, weighted by the task dependency index of each task— that predicts gains in productivity and perceived quality. It can be seen from Tables 2 and 3 that the main effects of digitization of the two kinds of information alone are not significant. It is the interaction of this weighted average measure with the digitized SI and SSI that explains outcomes, and progressive digitization alone does not explain any of the outcomes.

Third, we demonstrate a very strong moderating influence of activity systems structure on how technology delivers gains in efficiency and quality. We show that in FCAS it is the interaction of digitized SI with the weighted average TTF measure for the decision-making characteristic that explains gains in productivity and perceived quality. In marked contrast, for PCAS we show that it is the interaction of both digitized SI and SSI, with the weighted average TTF measure for the task execution characteristic, that predicts gains in productivity and perceived quality. Thus, the structure of the activity system has a very strong moderating effect on how technology delivers gains in efficiency and quality (i.e., in all three models).

A fourth contribution of this study has to do with the nature of the digitized information (structured, unstructured, or semistructured) and its complementarity with preprocessing. In Sections 3 and 4 we observed that research in medical informatics has reached a relative consensus on the value of structured data in chronic care. Our research shows that the creation of semistructured data has strong complementarities with preprocessing. Greater levels of semistructured data amplify the benefits of preprocessing, and greater preprocessing amplifies the benefit of semistructured data.

## 6.2 Recommendations for Practitioners and Policy Makers

The findings of this study also enable us to make three recommendations for practitioners. First, there are great benefits to preprocessing by specialist physicians, resulting in both efficiency gains and gains in the perceived quality of care. While preprocessing information takes additional time and effort,<sup>29</sup> we show that even after accounting for that additional time, preprocessing drives very strong gains in efficiency and quality.

Second, specialists must be encouraged to edit the UI in patients’ digitized records and create SSI out of it. The benefits of creating SSI are twofold: First SSI is a key enabler of task execution in PCAS, and the ability of specialists to create SSI from unstructured information makes task execution more efficient and reliable. Since chronic care specialists work in interdisciplinary teams that require a lot of coordination between multiple specialists (Bates, 2002), task execution becomes even more important in this context. Therefore, the ability to create SSI plays a very important role in chronic care delivery. A second benefit of SSI is that it makes the preprocessing of patient information easier. Since there are strong complementarities between preprocessing and SSI, creating SSI offers another way to drive both efficiency and perceived quality. When specialists are able to create SSI—using annotations, hyperlinks, and searchable keywords, etc.—they make it easier to preprocess patients’ information, thereby making the time spent during the patient visit more productive, which also adds to the perceived quality of care received by the patient.

## 6.3 Limitations

We wish to highlight some limitations of our research. Our quality measures are based on patient VCRs. Our current data do not allow for quantification of the economic value of higher levels of quality, which we leave for future studies to explore. Second, all our data consist of patients in outpatient settings—i.e., patients making visits to chronic care specialists’ offices. Inpatients and surgery patients are not included in this data set. Our data set allowed us to cleanly partition patients into two subpopulations based on their affliction levels to test whether VCRs were similar among high- and low-affliction patients. In the absence of such clearly demarcated population subgroups it may be necessary to divide patients based on the complexity of their visit purpose (available in ICD-10- CM and billing reference codes); this may not result in the same clarity of findings or the same level of statistical significance.

## 6.4 Extensions

The use of activity systems to model the functioning of physicians and incorporating measures of task interdependencies to explain the impact of technology on the work of individual physicians holds great promise for future research. This study could be extended to inpatient care, especially geriatric care, which is both expensive and characterized by complicated workflows and information-intensive diagnostic processes. Alternatively, this study could also be extended to include surgeons and specialists who perform medical procedures. Their activity systems may have CTC’s other than the ones that we identified (decision-making and task execution). Performing similar analysis on other kinds of activity systems would lead to a richer understanding of how the structure of task interdependencies in healthcare delivery influences the effectiveness of IT.

## Acknowledgments

This research was supported in part by the Sasin School of Management at Chulalongkorn University, Thailand and the Johns Hopkins Carey Business School at Johns Hopkins University.

## References

Abelson, R., Creswell, J., & Palmer, G. (2012, Medicare billing rises at hospitals with electronic records. The New York Times, September 21, 2012.

Adler-Milstein, J., Green, C. E., & Bates, D. W. (2013). A Survey analysis suggests that electronic health records will yield revenue gains for some practices and losses for many. Health Affairs, 32(3), 562–570.

Afantenos, S., Karkaletsis, V., & Stamatopoulos, P. (2005). Summarization from medical documents: a survey. Artificial Intelligence in Medicine, 33(2) 157-177.

Agarwal, R., Gao, G. (Gordon), DesRoches, C., & Jha, A. K. (2010). Research Commentary—The digital transformation of healthcare: current status and the road ahead. Information Systems Research, 21(4) 796-809.

Agha, L. (2014). The effects of health information technology on the costs and quality of medical care. Journal of Health Economics, 34, 19-30.

Appari A., Johnson, E. M., & Anthony D. L. (2013). Meaningful use of electronic health record systems and process quality of care: Evidence from a panel data analysis of u.s. acute-care hospitals” Health Services Research, 48(2.1), 354-375.

Andres, H. P., & Zmud, R. W. (2001). A contingency approach to software project coordination. Journal of Management Information Systems, 18(3) 41-70.

Aral, S., Brynjolfsson, E., & Van Alstyne, M. (2012). Information, technology, and information worker productivity. Information Systems Research, 23(3.2), 849-867.

Argote, L., & Ren, Y. (2012). Transactive memory systems: a microfoundation of dynamic capabilities. Journal of Management Studies, 49(8) 1375-1382.

Aron, R., Jayanty, S., & Pathak, P. (2007). Impact of internet-based distributed monitoring systems on offshore sourcing of services. ACM Transactions on Internet Technology, 7(3), 16-es.

Aron, R., & Singh, J. V. (2005). Getting offshoring right. Harvard Business Review, 83(12) 135- 143.

Athey, S., & Stern, S. (2002). The impact of information technology on emergency health care outcomes. RAND Journal of Economics, 33(3) 399-432.

Barbulescu, M., Grigoriu, R., Halcu, I., Neculoiu, G., Sandulescu, V. C., Marinescu, M., & Marinescu,

V. (2013). Integrating of structured, semistructured and unstructured data in natural and build environmental engineering. Proceedings of the Roedunet International Conference.

Bardhan, I. R., & Thouin, M. F. (2013). Health information technology and its impact on the quality and cost of healthcare delivery. Decision Support Systems, 55(2), 438-449.

Barr, V. J., Robinson, S., Marin-Link, B., Underhill, L., Dotts, A., Ravensdale, D., & Salivaras, S. (2003). The expanded chronic care model: An integration of concepts and strategies from population health promotion and the chronic care model. Hospital Quarterly, 7(1) 73-82.

Bates, D. W., Cohen, M., Leape, L. L., Overhage, J. M., Shabot, M. M., & Sheridan, T. (2001). Reducing the frequency of errors in medicine using information technology. Journal of the American Medical Informatics Association, 8(4) 299-308.

Bates, D. W. (2002). The quality case for information technology in healthcare. BMC Medical Informatics and Decision Making, 2(1), Article 7.

Bates, D. W., Kuperman, G. J., Wang, S., Gandhi, T., Kittler, A., Volk, L., Spurr, C., Khorasani, R., Tanasijevic, M., & Middleton, B. (2003). Ten commandments for effective clinical decision support: Making the practice of evidence-based medicine a reality. Journal of the American Medical Informatics Association, 10(6) 523-530.

Bhargava, H. K., & Mishra, A. N. (2014). Electronic medical records and physician productivity: Evidence from panel data analysis. Management Science, 60(10) 2543-2562.

Bhargava, H., & Mishra, A. (2011). Electronic medical records and physicians’ productivity: Insights from panel data analysis and design implications. Proceeding of the Conference on Information Systems and Technology.

Brandon, D. P., & Hollingshead, A. B. (2004). Transactive memory systems in organizations: matching tasks, expertise, and people. Organization Science, 15(6) 633-644.

Brynjolfsson, E., & Hitt, L. (1996). Paradox lost? Firmlevel evidence on the returns to information systems spending. Management Science, 42(4) 541-558.

Bulkley, N., & Van Alstyne, M. (2004). Why information should influence productivity. Center for eBusiness @ MIT. http://ebusiness.mit.edu/research/papers/202\_va nAlstyne\_Productivity.pdf.

Buneman, P., Davidson, S. B., Fernandez, M. F., & Suciu, D. (1997. Adding structure to unstructured data. Proceedings of the 6th International Conference on Database Theory.

Chiasson, M., & Davidson, E. (2005). Taking industry seriously in information systems research. MIS Quarterly, 29(4), 591-605.

Cohen, J., & Cohen, P. (2002). Applied multiple regression/correlation analysis for the behavioral sciences (3rd ed.). Routledge.

Dennis, A. R., Wixom, B. H., & Vandenberg, R. J. (2001). Understanding fit and appropriation effects in group support systems via metaanalysis. MIS Quarterly, 25(2) 167-193.

Dishaw, M. T., & Strong, D. M. (1999). Extending the technology acceptance model with tasktechnology fit constructs. Information & Management, 36(1) 9-21.

Dishaw, M. T., & Strong, D. M. (2003). The effect of task and tool experience on maintenance CASE tool usage. Information Resources Management Journal, 16(3) 1-16.

Fernandez, M. F., Popa, L., & Suciu, D. (1997. A Structure-based approach to querying semistructured data. Proceedings of the 6th International Workshop on Database Programming Languages.

Furukawa, M. F., Raghu, T. S., & Shao, B. M. (2010). Electronic medical records, nurse staffing, and nurse-sensitive patient outcomes: evidence from California hospitals, 1998-2007. Health Services Research, 45(4), 941-962.

Gardino, S. L., Jeruss, J. S., & Woodruff, T. K. (2010). Using decision trees to enhance interdisciplinary team work: The case of oncofertility. Journal of Assisted Reproduction and Genetics, 27(5), 227- 231.

Goodhue, D. L. (1995). Understanding user evaluations of information systems. Management Science, 41(12) 1827-1844.

Goodhue, D. L., & Thompson, R. L. (1995). Tasktechnology fit and individual performance. MIS Quarterly, 19(2) 213-236.

Grönroos, C. (1982). An Applied Service Marketing Theory. European Journal of Marketing, 16(7), 30-41.

Hackathorn, R. D., & Keen, P. G. W. (1981. Organizational strategies for personal computing in decision support systems. MIS Quarterly, 5(3) 21-27.

HIMSS. (2006). The ROI of EMREHR: Productivity soars, hospitals save time and, yes, money.

http://beenajoy.weebly.com/uploads/6/7/0/0/67 00334/davies\_wp\_roi.pdf

Hirst, M. K., & Yetton, P. W. (1999). The effects of budget goals and task interdependence on the level of and variance in performance: A research note. Accounting, Organizations and Society, 24(3) 205-216.

Hitt, L. M., Wu, D. J., & Zhou, X. (2002. Investment in enterprise resource planning: Business impact and productivity measures. Journal of Management Information Systems, 19(1), 71-98.

Institute of Medicine. (2000). To err is human: Building a safer health system. National Academies Press.

Jackson, P., & Klobas, J. (2008). Transactive memory systems in organizations: Implications for knowledge directories. Decision Support Systems, 44(2), 409-424.

Johnson, P. D., Tu, S., Booth, N., Sugden, B., & Purves, I. N. (2000). Using scenarios in chronic disease management guidelines for primary care. Proceedings of the Annual American Medical Informatics Association Symposium.

Kadab, L., Ramkrishnan, G., Aron, R., & Singh, J. V. (2003). Two major errors that companies make in outsourcing services. Knowledge@Wharton. https://knowledge.wharton.upenn.edu/article/tw o-major-errors-that-companies-make-inoutsourcing-services/

Kang, D., & Santhanam, R. (2003). A longitudinal field study of training practices in a collaborative application environment. Journal of Management Information Systems, 20(3) 257- 281.

Kanza, Y., Nutt, W., & Sagiv, Y. (2002). Querying incomplete information in semistructured data. Journal of Computer and System Sciences, 64(3) 655-693.

Kauffman, S. (1993). The origins of order: Selforganization and selection in evolution, Oxford University Press.

Keating, P., Cambrosio, A., & Nelson, N. C. (2016). “Triple negative breast cancer”: Translational research and the (re)assembling of diseases in post-genomic medicine. Studies in History and Philosophy of Science—Part C: Studies in History and Philosophy of Biological and Biomedical Sciences, 59, 20-34.

Lee, J., McCullough, J. S., & Town, R. J. (2013. The impact of health information technology on hospital productivity. RAND Journal of Economics, 44(3) 545-568.

Lehtinen, U., & Lehtinen, J. R. (1982). Service quality: A study of quality dimensions (Working paper). Service Management Institute, Helsinki, Finland.

Levinthal, D. A. (1997). Adaptation on rugged landscapes. Management Science 43(7) 934- 950.

Lewis, K. (2004). Knowledge and performance in knowledge-worker teams: A longitudinal study of transactive memory systems. Management Science, 50(11) 1519-1533.

Lewis, R. C., & Booms, B. H. (1983). The marketing aspects of service quality. Emerging Perspectives on Services Marketing, 65(4) 99- 107.

Leykum, L. K., Lanham, H. J., Pugh, J. A. (2014). Manifestations and implications of uncertainty for improving healthcare systems: An analysis of observational and interventional studies grounded in complexity science. Implementation Science: IS, 9, Article 165.

Liu, Y., & Aron, R. (2015). Organizational control, incentive contracts, and knowledge transfer in offshore business process outsourcing. Information Systems Research, 26(1), 81-99.

Livernois, C. (2017). 61% of healthcare professionals rate ROI of EHRs as “poor,” “terrible.” AI in Healthcare. https://www.aiin.healthcare/topics/ ehr-emr/61-healthcare-professionals-rate-roiehrs-poor-terrible.

Majchrzak, A., Rice, R. E., Malhotra, A., King, N., & Ba, S. (2000). Technology adaptation: The case of a computer-supported inter-organizational virtual team. MIS Quarterly, 24(4) 569-600.

Mani, D., Barua, A., & Whinston, A. B. (2011). An empirical analysis of the contractual and information structures of business process outsourcing relationships. Information Systems Research, 23(3.1), 618-634.

McCullough, J. S., Casey, M., Moscovice, I., & Prasad, S. (2010). The effect of health information technology on quality in U.S. hospitals. Health Affairs, 29(4) 647-654.

Melville, N., Kraemer, K., & Gurbaxani, V. (2004). Information technology and organizational performance: An integrative model of IT business value. MIS Quarterly, 28(2) 283-322.

Menon, N. M., Lee, B., & Eldenburg, L. (2000). Productivity of information systems in the healthcare industry. Information Systems Research, 11(1), 83-92.

MEPS Medical Expenditure Panel Survey. (2006). Agency for Healthcare Research and Quality. https://meps.ahrq.gov/mepsweb/

Milgrom, P., & Roberts, J. (1995). Complementarities and fit strategy, structure, and organizational change in manufacturing. Journal of Accounting and Economics, 19(2-3), 179-208.

Nurok, M., & Gewertz, B. (2019). Relative Value Units and the Measurement of Physician Performance. JAMA, 322(12), 1139-1140.

Orlikowski, W. J. (1992). The duality of technology: Rethinking the concept of technology in organizations. Organization Science, 3(3) 398- 427.

Parasuraman, A., Berry, L. L., & Zeithaml, V. A. (1991. Perceived service quality as a customer-based performance measure: An empirical examination of organizational barriers using an extended service quality model. Human Resource Management (1986-1998), 30(3) 335- 364.

Porter, M. E. (1996). What Is Strategy? Harvard Business Review, 74(6), 61-78.

Porter, M., & Siggelkow, N. (2008). Contextuality within activity systems and sustainability of competitive advantage. Academy of Management Perspectives, 22(2) 34-56.

PressGaney. (2010). Patient satisfaction surveys. https://helpandtraining.pressganey.com/research Resources/hospitals/caseStudies.aspx

Reis, Z. S. N., Maia, T. A., Marcolino, M. S., Becerra-Posada, F., Novillo-Ortiz, D., & Ribeiro, A. L. P. (2017). Is there evidence of cost benefits of electronic medical records, standards, or interoperability in hospital information systems? Overview of systematic reviews. JMIR Medical Informatics, 5(3), e26.

Riaño, D., Real, F., López-Vallverdú, J. A., Campana, F., Ercolani, S., Mecocci, P., Annicchiarico, R., & Caltagirone, C. (2012). An ontology-based personalization of health-care knowledge to support clinical decisions for chronically ill patients. Journal of Biomedical Informatics, 45(3) 429-46.

Rosner, M. H., & Falk, R. J. (2020). Understanding work. Clinical Journal of the American Society of Nephrology, 15(7), 1053-1055.

Rusu, F., & Dobra, A. (2012). GLADE: A scalable framework for efficient analytics. SIGOPS Operating. Systems Review, 46(1) 12-18.

Sanchez, J. A., Proal, C., & Maldonado-Naude, F. (2004). Supporting structured, semi-structured

and unstructured data in digital libraries. Computer Science, 2004. ENC 2004. Proceedings of the Fifth Mexican International Conference in 368-375.

Sharma, R., & Yetton, P. (2003). The contingent effects of management support and task interdependence on successful information systems implementation. MIS Quarterly, 27(4) 533-555.

Sharma, R., & Yetton, P. (2007). The contingent effects of training, technical complexity, and task interdependence on successful information systems implementation. MIS Quarterly, 31(2) 219-238.

Siggelkow, N., & Rivkin, J. W. (2009). Hiding the evidence of valid theories: How coupled search processes obscure performance differences among organizations. Administrative Science Quarterly, 54(4) 602-634.

Storfa, A. H., & Wilson, M. L. (2015). Physician productivity. American Journal of Clinical Pathology, 143(1), 6-9.

Tambe, P., & Hitt, L. M. (2012). The productivity of information technology investments: New evidence from IT labor data. Information Systems Research, 23(3.1), 599-617.

Thompson, J. D. (1967. Organizations in action, McGraw Hill.

Tutty, M. A., Carlasare, L. E., Lloyd, S., & Sinsky, C. A. (2019). The complex case of EHRs: Examining the factors impacting the EHR user experience. Journal of the American Medical Informatics Association, 26(7), 673-677.

Ueno, N. T., Ito, T. D., Grigsby, R. K., Black, M. V., & Apted, J. (2010, September). ABC conceptual model of effective multidisciplinary cancer care. Nature Reviews Clinical Oncology, 7, 544-547.

Unertl, K. M., Weinger, M. B. 2009). Describing and modeling workflow and information flow in chronic disease care. Journal of the American Medical Informatics Association, 16(6) 826-836.

Urwin, J. W., & Emanuel, E. J. (2019, September 24). The relative value scale update committee: time for an update. JAMA, 322(12), 1137-1138.

van der Vegt, G. S., van de Vliert, E., & Oosterhof, A. (2003). Informational dissimilarity and organizational citizenship behavior: The role of intrateam interdependence and team identification. Academy of Management Journal, 46(6) 715-727.

Van Vleck, T. T., Stein, D. M. (2007). Assessing data relevance for automated generation of a clinical summary. Proceedings of the Annual American Medical Informatics Association Symposium.

Wagner, E. H., Austin, B. T., Davis, C., Hindmarsh, M., Schaefer, J., & Bonomi, A. (2001). Improving chronic illness care: Translating evidence into action. Health Affairs, 20(6) 64-78.

Wagner, E. H., Austin, B. T., & Korff, M. Von. (1996). Organizing care for patients with chronic illness. The Milbank Quarterly, 74(4) 511.

Walker, J. M., & Carayon, P. (2009). From tasks to processes: the case for changing health information technology to improve health care. Health Affairs, 28(2) 467-77.

Wegner, D. M., Giuliano, T., & Hertel, P. (1985). Cognitive interdependence in close relationships. In W. J. Ickes (Ed.), Compatible and incompatible relationships (pp. 253-276). Springer.

Williams, K. A., Chambers, C. G., Dada, M., Christo, P. J., Hough, D., Aron, R., & Ulatowski, J. A. (2014). Applying JIT principles to resident education to reduce patient delays: A pilot study in an academic medical center pain clinic. Pain Medicine, 16(2), 312-318.

Wybo, M. D., & Goodhue, D. L. (1995. Using interdependence as a predictor of data standards. Theoretical and measurement issues. Information & Management, 29(6) 317-329.

Young, A. S., Chaney, E., Shoai, R., Bonner, L., Cohen, A. N., Doebbeling, B., Perrin, R. (2007). Information technology to support improved care for chronic illness. Journal of General Internal Medicine, 22, 425-430.

Zeithaml, V. A. (1985). Problems and strategies in services marketing. Journal of Marketing, 49(2), 33-46.

Zeithaml, V. A., Parasuraman, A., & Malhotra, A. (2002). Service quality delivery through web sites: A critical review of extant knowledge. Journal of the Academy of Marketing Science, 30, 362-375.

Zellner, A. (1962). An efficient method of estimating seemingly unrelated regressions and tests for aggregation bias. Journal of the American Statistical Association, 57(298), 348-368.

Zigurs, I., & Buckland, B. K. (1998). A theory of task/technology fit and group support systems effectiveness, MIS Quarterly, 22(3), 313-334.

## Appendix A: Coding Task Interdependencies

Each patient visit was modeled in terms of one or more of the 47 high-level tasks that were performed during the visit. This resulted in 12 distinct task combinations or systems of tasks<sup>30</sup>. We term each of these 12 distinct task combinations as an activity system—for this system of tasks describes the activities performed by the specialist during the visit. Multiple clinical specialists drawn from each of the four chronic care categories in our data set, rated the task interdependencies within each Activity System. To determine pairwise interdependence between two activities within an activity system we used a Likert measure based on the construct used by Sharma and Yetton (2003). Coders were asked to rate the extent to which the successful performance of task $\mathrm { T _ { j } }$ was dependent on the performance of task $\mathrm { T _ { i } }$ on a Likert scale of 1 to 7. A rating of 1 corresponded to ‘not at all dependent’ and $^ 7$ to ‘very highly dependent’, with 4 as the neutral point. Thus for any pair of tasks $\mathrm { T _ { i } }$ and $\mathrm { T _ { j } } ,$ the task dependency score is given by $T D _ { i j }$ and where $1 \leq$ $T D _ { i j } \le 7$ . In an activity system consisting of ?? tasks, a task can have at most $K - 1$ dependencies. Thus the dependency index of the $\mathrm { i } ^ { \mathrm { t h } }$ task $\mathrm { D } _ { \mathrm { i } }$ is given by: $\begin{array} { r } { D _ { i } = \frac { 1 } { K - 1 } \big ( \sum _ { j = 1 } ^ { K } T D _ { i j } \big ) } \end{array}$ . The task interdependency interrater reliability given by Fleiss Kappa (free marginal Kappa) was 0.89 indicating a very high level of reliability.

Task Technology Fit Rating: We identified two key task characteristics for each task—Decision-Making and Task Execution. For each of these two task characteristics, the extent to which technology supported the performance of the task was rated on 1 to 7 Likert scale based on Goodhue (1993; 1995). Therefore for the $\mathrm { i ^ { \mathrm { { i } } } } ^ { \mathrm { { i } } }$ task, the extent of fit between the technology and the Decision Making task characteristic is given by $D M T _ { i }$ where $1 \leq D M T _ { i } \leq 7$ and the extent of fit between the Technology and the Task Execution task characteristic is given by ?????? where $1 \leq T E T _ { i } \leq 7$ . Clinical specialists from each of the four chronic care categories rated the tasks in each Activity System to determine the critical task characteristic. The interrater reliability for the critical task characteristic measure is given by Fleiss kappa (free marginal Kappa) was 0.92 indicating a very high level of reliability.

TTF Score At The Level of The Activity System: For an activity system consisting of ?? tasks, we compute the weighted average rating of the two task characteristics, where the dependency index of each task serves as the weight. Thus the weighted average rating of the Decision-Making characteristic at the level of the $j ^ { t h }$ activity system is given by: $\begin{array} { r } { D M _ { j } = \frac { 1 } { K } \left( \frac { \sum _ { i = 1 } ^ { K } \left( D M T _ { i } \times D _ { i } \right) } { \sum _ { i = 1 } ^ { k } D _ { i } } \right) } \end{array}$ . Similarly the weighted rating of the Task Execution characteristic at the level of the $j ^ { t h }$ Activity System is given by: $\begin{array} { r } { T E _ { j } = \frac { 1 } { K } \left( \frac { \sum _ { i = 1 } ^ { K } \left( T E T _ { i } \times D _ { i } \right) } { \sum _ { i = 1 } ^ { k } D _ { i } } \right) } \end{array}$

## Appendix B: Categorizing Activity Systems: A Graph Theoretic Approach

We mentioned earlier (Sections 3 and 4 in the main paper) that the activity systems were of two kinds—fully connected (FCAS) and partially connected (PCAS). If every task in an activity system was connected to at least one other task (at least one other task depended on it or the task depended on at least one other task) then the activity system was defined as being fully connected. If not, it is said to be partially connected.

More formally, we draw on the concept of a Connected Graph from Graph Theory to define a fully connected activity system (FCAS). If each task in an activity system is thought of as a node in a graph, then for two nodes (tasks) $T _ { i }$ and $T _ { j }$ to be connected the minimal path existence criterion is given by $T D _ { i j } > 1$ ???? $T D _ { j i } > 1$ , i.e., if there exists at least one dependency between the pair of tasks with a magnitude greater than 1. We specify the minimal path existence criterion is $T D _ { i j } > 1 o r T D _ { j i } > 1$ a dependency rating strictly greater than 1, because, task interdependencies are rated on a Likert Scale rating of 1 to 7 where a rating of 1 indicates there exists no dependency at all.

An activity system is an FCAS if the underlying graph is connected or if there is a dependency path from any task within the activity system to any other task within the same Activity system. Consistent with graph theoretic definitions, we use nondirectional paths as a part of the minimality condition. When there are one or more tasks that are NOT connected by a path to all other tasks within the Activity System, it is said to be partially connected (PCAS). Such tasks form disjointed subgraphs (or even degenerate subgraphs consisting of standalone, independent tasks).

## Appendix C: Correlation Tables

There are three estimation models that we use in this study. We run each model for FCAS and PCAS respectively. The tables of correlations are provided in Tables C1 and C2.

Table C1. Table of Correlations for FCAS

<table><tr><td></td><td>Duration (DV)</td><td>Co_var (DV)</td><td>VCR (DV)</td><td>CR_pal</td><td>SI</td><td>SSI</td><td>Pre_proc</td><td>DM</td><td>TE</td></tr><tr><td>Duration (DV)</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Co_var (DV)</td><td>0.007</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>VCR (DV)</td><td>.088**</td><td>.530**</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CR_pal</td><td>.077*</td><td>-0.039</td><td>-0.021</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SI</td><td>-.223**</td><td>0.02</td><td>-0.006</td><td>-.068*</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>SSI</td><td>-.228**</td><td>0</td><td>-0.009</td><td>-.085*</td><td>.800**</td><td>1</td><td></td><td></td><td></td></tr><tr><td>Pre_proc</td><td>-.199**</td><td>0.03</td><td>-0.02</td><td>0.057</td><td>.271**</td><td>.220**</td><td>1</td><td></td><td></td></tr><tr><td>DM</td><td>-0.012</td><td>-0.003</td><td>0.002</td><td>-0.013</td><td>-0.029</td><td>-0.014</td><td>-0.012</td><td>1</td><td></td></tr><tr><td>TE</td><td>0.059</td><td>-0.012</td><td>0.002</td><td>-0.031</td><td>-0.004</td><td>-0.024</td><td>-0.005</td><td>0.01</td><td>1</td></tr><tr><td colspan="10">*** p &lt;0.01, ** p &lt; 0.05, * p &lt; 0.1</td></tr></table>

Table C2. Correlations of Variables in the Three Estimation Models for PCAS

<table><tr><td></td><td>Duration (DV)</td><td>Co_Var (DV)</td><td>VCR (DV)</td><td>CR</td><td>SI</td><td>SSI</td><td>Pre_proc</td><td>DM</td><td>TE</td></tr><tr><td>Duration (DV)</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Co_Var (DV)</td><td>-.117**</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>VCR (DV)</td><td>-.097**</td><td>.408**</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CR_pal</td><td>.460**</td><td>-0.058</td><td>-0.043</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SI</td><td>0.016</td><td>0.01</td><td>0.033</td><td>-0.022</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>SSI</td><td>0.012</td><td>0.003</td><td>0.033</td><td>-0.031</td><td>.786**</td><td>1</td><td></td><td></td><td></td></tr><tr><td>Pre_proc</td><td>-.245**</td><td>0.043</td><td>0.056</td><td>-.133**</td><td>-0.056</td><td>-0.064</td><td>1</td><td></td><td></td></tr><tr><td>DM</td><td>0.012</td><td>0.011</td><td>-0.017</td><td>-.130**</td><td>-0.019</td><td>0.006</td><td>0.028</td><td>1</td><td></td></tr><tr><td>TE</td><td>0.023</td><td>0.016</td><td>0.009</td><td>-0.001</td><td>0</td><td>-0.031</td><td>-0.018</td><td>-0.029</td><td>1</td></tr><tr><td colspan="10">*** p&lt;0.01, ** p&lt;0.05, * p&lt;0.1</td></tr></table>

Note: in Tables C1 and C2 there are three dependent variables corresponding to each of the three estimation models respectively.

## Patient Affliction Levels:

Patients with clinician-rated affliction levels of 0 to 5 fall into the low affliction intensity group, while patients with ratings in the 6 to 10 category fall into the high affliction intensity group. Figure 1 depicts the frequency of patient affliction levels at the beginning of our study period, which clearly shows a bimodal distribution.

The two distributions are clearly separate, as the left tail of affliction values of the high affliction intensity patients was more than 3 standard deviations to the right of the mean of the low affliction intensity patients $( \mu _ { L } = 2 . 6 3 , \sigma _ { L } = 1 . 0 9 ;$ $\mu _ { H } = 8 . 0 6 , \sigma _ { H } = 1 . 0 3 )$

Furthermore, the visit contact duration is quite distinctive between high and low affliction patients, which is confirmed by a t-test (test of means) with p-value <0.001.

## Appendix D: Gains from Preprocessing

Here we outline how we can separate the gains of more efficient digital access from those of transactive memory (TM) formation. The findings here provide additional information about the benefits of preprocessing outlines in hypotheses 2A and 2B in the paper.

We illustrate the technique that we will use first with an example and then show via analytical methods, how we separate out the two different efficiency gains. For ease of exposition as well as notational clarity, we will explain the dynamics in the example during one period; it is easy to see that the same logic holds for all periods.

Let us consider two sets of patients, one set whose records have been digitized and the other set of patients whose records are still in paper format, in a particular measurement period (recall that we have time series data—of gradual digitization of patient records over 12 measurement periods).

## Patients with Digitized Medical Information (EHRs):

Let us begin with the patients whose records have been digitized. A small fraction, say, 15% of patients in each period have their records preprocessed by the physician.

Case 1: We first compute the mean preprocessing time for those patient visits where patient records have been preprocessed (prior to the visit).

For a particular patient, the total interaction time with the specialist is calculated as follows, the actual time of physician-patient interaction plus any time spent by the specialist in preprocessing the patient’s record prior to the patient’s visit.

For a given physician and a given patient, the following notation is adopted:

$t _ { i j } $ the time spent by the $i ^ { t h }$ physician with the $j ^ { t h }$ patient during a particular visit.

$p _ { i j } $ the time spent by the $i ^ { t h }$ physician, preprocessing the $j ^ { t h }$ patient’s record before a visit.

$T _ { i j } = t _ { i j } + p _ { i j }$ where $T _ { i j } $ is the total time spent by the physician on the patient visit (including the preprocessing time). If there are a total of n patient visits for this physician during the period, then the mean patient-specialist visit duration for this $i ^ { t h }$ physician is given by:

$$
\mu_ {i} = \frac {\sum_ {j} ^ {n} (T _ {i j})}{n}
$$

Note that in the above formulation the basic unit of measurement is the individual visit made by the patient to the specialist, i.e., we measure the duration of each patient-specialist visit. So, if the same patient makes multiple visits in the same period, the formulation will hold as all visits will be a part of the aggregate sum for the period.

Case 2: Next we compute the mean visit durations for patients whose patient records have not been preprocessed. We use the following notation.

$\alpha _ { i j } $ the time spent by the $i ^ { t h }$ physician with the $j ^ { t h }$ patient during a particular visit.

Note for these patient visits there is no preprocessing component to be added to the patient-physician interaction time. If there are a total of m patient visits for this physician during the period, then the mean patient-specialist visit duration for this physician is given by:

$$
\lambda_ {i} = \frac {\sum_ {j} ^ {m} (\alpha_ {i j})}{m}
$$

## Patients with Paper-Based Medical Information:

For patients whose data are in paper-based files, we do not know if specialists spent time preprocessing patient files, or how much time they spent preprocessing files or on how many occasions they spent preprocessing the patient files. We only know the visit duration during of each visit. Therefore, the actual visit duration mean is likely to be greater than the mean that we work with.

In other words, we use a conservative estimate of gains in formulating our hypotheses.

$\beta _ { i j } $ the time spent by the $i ^ { t h }$ physician with the $j ^ { t h }$ patient during a particular visit.

If there are a total of k patient visits for this physician during the period, then the mean patient-specialist visit duration for this physician is given by:

$$
\theta_ {i} = \frac {\sum_ {j} ^ {k} (\beta_ {i j})}{k}
$$

We now compare these three quantities: $\mu _ { i } , \lambda _ { i } ,$ and $\theta _ { i }$ .

To show that there are gains from ease of access and search enabled by digitization (and possible gains from TM formation) we need to show that:

$$
\mu_ {i} <   \theta_ {i}
$$

That is, the mean visit duration is less when there is digital preprocessing—in spite of the fact that in the case of digital records, the visit duration captures preprocessing time whereas in the case of paper-based records, it does not (so $\theta _ { i }$ is a conservative estimate, a lower bound for the actual mean). However, this represents some combination of the gain from digitization and benefits of TM formation because of preprocessing.

We wish to separate the gains of digitization from the gains of transactive memory and related issues. To do this we demonstrate an even stronger result is the following. We argue that when we restrict the comparison only to patients with digital records, we compare the mean duration of visits when records have been preprocessed against the mean duration of visits where there was no preprocessing. We will show that:

$$
\mu_ {i} <   \lambda_ {i}
$$

The only difference between $\mu _ { i }$ and $\lambda _ { i }$ is the difference that arises from digital preprocessing. In other words, we argue that where the gains from digitization are equally applicable to two patient subgroups (under comparison), the mean visit duration for patients whose records have been preprocessed (after adding the preprocessing time to the actual visit time), is less than the mean visit duration for patients whose records have not been preprocessed. This separates out the benefits of preprocessing from those of digital access.

## Separating the Gains: An Analytical Approach

Next, we will show via analytical methods that there are gains from TM formation. We now add the dimension of time and aggregate the three quantities across all 12 periods. We use exactly the same formulation in the example above, except that instead of calculating the weighted mean in a single period we will calculate the weighted mean across all 12 measurement periods. The three quantities: $\mu _ { i } , \lambda _ { i }$ , and $\theta _ { i }$ are aggregate values calculate across all 12 time periods.

We now furnish the results of our analysis.

First, we demonstrate the gains from digital preprocessing—the combined gains of both digital ease of access and TM formation. We will show that $\mu _ { i } < \theta _ { i }$

$$
\mathrm{HA:} \mu_ {i} <   \theta_ {i}
$$

$$
\mathrm{H0:} \mu_ {i} \prec \theta_ {i}
$$

In calculating the two sets of means for each specialist for each period, with controls for other covariates. The canonical test for testing the difference in means for large samples is the z-test for difference in means (Cohen & Cohen, 2002). We test this by running a one-tailed z-test for difference in means. The results are shown in Table D1. It can be seen from the table that the z-test statistic of -11.078 is less than z critical value (left tail) at $\alpha = 0 . 0 5$ and at $p < 0 . 0 0 1$ Therefore, the alternative hypothesis of $\mu _ { i } < \theta _ { i }$ holds.

Table D1: Two-Sample Z-Test for Means: One-Tailed Test

<table><tr><td rowspan="2">Two-sample z-test</td><td colspan="2">Mean visit duration</td></tr><tr><td>Digital</td><td>Paper</td></tr><tr><td>Mean</td><td>26.45428</td><td>32.16408</td></tr><tr><td>Variance</td><td>101.75745</td><td>155.40221</td></tr><tr><td>Population variance</td><td>95.88827</td><td>141.34627</td></tr><tr><td>Sample size</td><td>890</td><td>890</td></tr><tr><td>Alpha (significance level)</td><td colspan="2">0.050</td></tr><tr><td>Mean difference</td><td colspan="2">-5.710</td></tr><tr><td>Mean difference - 95% LCL</td><td colspan="2">-6.720</td></tr><tr><td>Mean difference - 95% UCL</td><td colspan="2">-4.700</td></tr><tr><td>Standard error</td><td colspan="2">0.515</td></tr><tr><td>Z-test statistic</td><td colspan="2">-11.078</td></tr><tr><td>P(Z &lt;= z): One-tailed distribution</td><td colspan="2">0.000</td></tr><tr><td>Z critical value: One-tailed distribution</td><td colspan="2">1.645</td></tr></table>

To make the case for benefits from TM formation from digital preprocessing, we formulate and test the following hypotheses:  
HA: $\mu _ { i } < \lambda _ { i }$  
H0: $\mu _ { i } \nless \lambda _ { i }$

As before, we test the hypothesis above by running a one-tailed z-test for difference in means. The results are shown in Table D2. It can be seen from the table that the z-test statistic of -11.408 is less than z critical value (left tail) at ?? = 0.05 and at $p < 0 . 0 0 1$ . Therefore, the alternative hypothesis of $\mu _ { i } < \lambda _ { i }$ holds.

Table D2. Two-Sample Z-test for Means: One-Tailed Test

<table><tr><td rowspan="2">Two-Sample Z-test</td><td colspan="2">Mean Visit Duration</td></tr><tr><td>Preprocessing</td><td>No Preprocessing</td></tr><tr><td>Mean</td><td>22.30735</td><td>27.25815</td></tr><tr><td>Variance</td><td>70.94887</td><td>106.34259</td></tr><tr><td>Population Variance</td><td>68.25323</td><td>99.92352</td></tr><tr><td>Sample size</td><td>893</td><td>893</td></tr><tr><td>Alpha (significance level)</td><td colspan="2">0.05</td></tr><tr><td>Mean Difference</td><td colspan="2">-4.951</td></tr><tr><td>Mean Difference - 95% LCL</td><td colspan="2">-5.801</td></tr><tr><td>Mean Difference - 95% UCL</td><td colspan="2">-4.1</td></tr><tr><td>Standard Error</td><td colspan="2">0.434</td></tr><tr><td>Z-test statistic</td><td colspan="2">-11.408</td></tr><tr><td>P(Z &lt;= z): One-tailed distribution</td><td colspan="2">0.000</td></tr><tr><td>Z Critical Value:One-tailed distribution</td><td colspan="2">1.645</td></tr></table>

## About the Authors

Ravi Aron is a professor in the Department of Decision and Information Sciences at the Bauer College of Business, at the University of Houston with expertise in the areas of information technology strategy, healthcare strategy and healthcare information systems. He received his PhD from the Leonard N. Stern School of Business at New York University. His research interests include machine learning and its applications, medical supply chains, and technology use in emerging economies. His research has been published in various journals including Management Science, Information Systems Research, Journal of Operations Management, Journal of Management Information Systems, and Harvard Business Review.

Praveen Pathak is the Robert B. Carter Professor in the Information Systems and Operations Management Department in the Warrington College of Business at the University of Florida. He received his PhD, from the Ross School of Business at the University of Michigan. His research interests include machine learning and its applications, blockchain technology, Healthcare IT, and web mining. His research has been published in various journals including Management Science, Information Systems Research, Journal of Operations Management, Journal of Management Information Systems, Decision Support Systems, and Journal of the Association for Information Systems.

Copyright © 2021 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
