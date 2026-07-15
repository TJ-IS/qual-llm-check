---
otero_id: 14794
otero_key: "D53XDAQM"
title: "Modeling the longitudinality of user acceptance of technology with an evidence-adaptive clinical decision support system"
authors: "Michael P. Johnson; Kai Zheng; Rema Padman"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.10.049"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Modeling the longitudinality of user acceptance of technology with an evidence-adaptive clinical decision support system<sup>☆</sup>

Michael P. Johnson <sup>a,</sup>⁎, Kai Zheng <sup>b</sup>, Rema Padman

<sup>a</sup> University of Massachusetts Boston, Boston, MA 02125-3393, USA

<sup>b</sup> University of Michigan, Ann Arbor, MI 48109-2029, USA

<sup>c</sup> Carnegie Mellon University, Pittsburgh, PA 15213-3390, USA

## a r t i c l e i n f o

Available online 5 November 2012

Keywords: Innovation adoption Electronic health record Clinical decision support system Social network analysis Usability assessments Clinical work<sup>fl</sup>ow User interface design

## a b s t r a c t

This paper presents multiple innovations associated with an electronic health record system developed to support evidence-based medicine practice, and highlights a new construct, based on the technology acceptance model, to explain end users' acceptance of this technology through a lens of continuous behavioral adaptation and change. We show that this new conceptualization of technology acceptance reveals a richer level of detail of the developmental course whereby individuals adjust their behavior gradually to assimilate technology use. We also show that traditional models such as technology acceptance model (TAM) are not capable of delineating this longitudinal behavioral development process. Our TAM-derived analysis provides a lens through which we summarize the signi<sup>fi</sup>cance of this project to research and practice. We show that our application is an excellent exemplar of the “end-to-end” IS design realization process; it has drawn upon multiple disciplines to formulate and solve challenges in medical knowledge engineering, just-in-time provisioning of computerized decision-support advice, diffusion of innovation and individual users' technology acceptance, usability of human-machine interfaces in healthcare, and sociotechnical issues associated with integrating IT applications into a patient care delivery environment.

© 2012 Elsevier B.V. All rights reserved

## 1. Introduction

Evidence-based medicine is the “conscientious, explicit, and judicious use of current best evidence in making medical decisions about the care of individual patients” [25]. There has been a general consensus that continuous, comprehensive practice of evidence-based medicine has tremendous potential to improve quality of care and reduce practice variation. However, there is also a widely acknowledged gap between clinicians' awareness of these care standards and their consistent application of the standards in practice. Clinical decision support systems (CDSS)—in particular, evidence-adaptive decision support systems— provide decision aids with a knowledge base constructed from and continually adapting to new research and practice based evidence of medicine [29]. Such decision aids address a current need in healthcare decision support for tools that use reliable patient data, decision models and problem solving methods to address challenges in performance requirements, data and knowledge forms and generalizability to other application areas [27]. However, while there is evidence that CDSS can improve clinician guideline compliance, and thus patient health [16,26], widespread use of such systems has not become available due to numerous technological, behavioral, and organizational barriers. These facts motivate the present research.

Clinical Reminder System (CRS) is a research-oriented clinical information system iteratively designed and developed through a 7-year joint effort by researchers from the H. John Heinz III College at Carnegie Mellon University (CMU) and medical practitioners at the Western Pennsylvania Hospital (WPH). CRS is an evidence-adaptive CDSS that aims to improve the quality of patient care by providing clinicians with just-in-time alerts and advisories based on best known evidence-based medicine guidelines and individual patients' health descriptors and treatment conditions. Of the four functions that a computerized CDSS may provide [21]—administrative support, managing clinical complexity and details, cost control, and decision support—CRS is designed to supply all except cost control.

CRS has been developed in the context of increased pressure to use electronic health records (EHR) to improve quality of care and patient safety, in the form of recommendations from professional organizations such as the Institute of Medicine and Federal mandates contained in the American Reinvestment and Recovery Act of 2009. However, adoption rates for EHRs in the U.S. are low compared to other industrialized countries [13]. Additionally, while CDSS technologies demonstrate great potential to improve quality of care and patient safety in laboratory and clinical trial settings (e.g., [4]), once deployed for routine use in the <sup>fi</sup>eld, they often fail to obtain adequate usage by medical practitioners and consequently fail to achieve those anticipated bene<sup>fi</sup>ts on clinical performance and patient outcomes [24]. For example, through a systematic review, Shojania et al. [34] found that computerized medication safety alerts are overridden by clinician users in 49% to 96% of cases including those for preventing severe drug–drug interaction events. In a more recent review, Shojania et al. [28] reported that point-of-care CDSS reminders have produced much smaller clinically signi<sup>fi</sup>cant improvements than those generally expected. Factors contributing to this missing link between the deployment of CDSS and the achievement of long-term end user adherence remain underexplored.

To enlarge the research base of knowledge regarding adoption and clinically relevant use of CDSS and EHR generally, CRS has operationalized research-based methods and models via a carefully designed application that has been evaluated in clinicians' day-to-day patient care routines. This process has generated research insights into reengineering the system's technological designs to improve its usability as well as informing tailored behavioral interventions for addressing the user resistance encountered. As an exemplar of the “end-to-end” IS design realization process, the CRS project draws upon multiple disciplines including decision science, computer science, information systems, and behavioral and social sciences to formulate and solve challenges in (1) medical knowledge engineering; (2) just-in-time provisioning of computerized decision-support advice; (3) diffusion of innovation and individual users' technology acceptance; (4) usability of human-machine interfaces in healthcare; and (5) sociotechnical issues when integrating technological systems into the reality of a patient care delivery environment. The CRS project hence embodies a “methodological pluralism” approach called by researchers [14] which demands extreme additional attention be paid to medical practitioners' work contexts, their preferences and constraints, and the social and organizational environments in which technologies and users are situated.

The purpose of this paper is twofold: to summarize a new understanding of the importance of rigorous and adaptive clinical IT design to bridge academic research and practice generated through our previously published work based on developing, evaluating, and iteratively improving CRS, and to use this understanding to frame novel insights provided by CRS regarding the behavioral underpinnings of technology acceptance that may inform more useful and usable technology designs as well as more effective diffusion strategies and use policies. We achieve the <sup>fi</sup>rst goal by reviewing the research contributions of the CRS project: analysis of longitudinal usage rates and causes of dissatisfaction with an early version of the application, and, with a reengineered version of CRS, user interface analysis to identify navigational patterns and opportunities for usability improvements, and social network analysis to reveal the nature of users' social interactions the relationship to individual clinicians' system utilization. We achieve the second goal by introducing a new model of technology adoption that addresses the limitations of the well-known technology acceptance model (TAM) through accommodation of the longitudinal course of acceptance behavior formation, development, and institutionalization relying on “actual system use” as computer-recorded objective usage instead of self-reported surrogates.

## 2. Materials and methods

## 2.1. CRS functionality

The Clinical Reminder System (CRS) is capable of managing work<sup>fl</sup>ow and clinical documentation as well as generating decision-support reminders at the point of care. To provide administrative support, CRS allows clerical staff to register new patients and manage patient appointments. When patients arrive in the clinic, clerical staff use CRS to track work<sup>fl</sup>ow activities such as patient check-in, encounter in progress, and patient check-out. To enable clinicians to manage all necessary patient information using a single system, CRS has evolved into a “lite” EHR system. The EHR features of CRS provide comprehensive patient data management support such as documenting clinical observations, tracking progress notes, prescribing medications and ordering laboratory tests. To minimize data entry and to collect electronically collect up-to-date patient health conditions, CRS is interfaced with other hospital information systems to retrieve laboratory test results (in real time) and patient demographic information and historical disease diagnoses (in batch mode, performed periodically).

In addition to storage, management, and retrieval of patient data, CRS implements evidence-based medicine guidelines to generate “just-in-time” alerts and advisories to improve medical practice of four chronic diseases: asthma, diabetes, hypertension, and hyperlipidemia; and <sup>fi</sup>ve preventive care categories: breast cancer, cervical cancer, in<sup>fl</sup>uenza, pneumonia, and steroid-induced osteoporosis. Such alerts and advisories, or reminders, provide clinicians with decision support aid in (1) managing clinical complexity and details, and (2) clinical diagnosis and treatment plans. The reminders that CRS generates take the form of recommendations to have certain tests performed, to receive vaccinations, or to discuss the pros and cons of alternative treatments. Fig. 1 contains an extended view of CRS' main workspace.

The most recent, web-enabled version of CRS is implemented using C# and ASP.Net technology and an Oracle 10 g database. All guideline-based, reminder generating algorithms are implemented as web services using a homegrown ontology. CRS is available at http://crs.sph.umich.edu:8088/.

## 2.2. CRS research directions

As a prelude to our discussion of new research results related to system usage, we summarize the primary research contributions of CRS. To enable effective and ef<sup>fi</sup>cient medical knowledge engineering, we designed and implemented a novel guideline ontology model that enables structured acquisition and automated execution of evidencebased medicine guidelines. The Guideline Representation and Execution Model (GREM), built upon several existing guideline ontologies such as Guideline Interchange Format, is discussed in detail in [40].

We conducted a longitudinal, quantitative usage analysis to assess the dynamics in the utilization rates of CRS. The main variable constructed from computer-recorded usage data is “the percentage of patient encounters in which CRS was used to generate clinician directed reminders.” The longitudinal usage data were analyzed using a novel developmental trajectory analysis model (DTA). This model embodies a semi-parametric, group-based statistical approach for identifying distinct trajectory groups within a population and relating the group membership probabilities to a set of covariates of interest [19]. Based on the quantitative analysis results, we further collected and analyzed qualitative data from multiple sources in order to explain the low utilization rates observed (approximately 35% on average), and the developmental usage trajectories identi<sup>fi</sup>ed. These empirical, <sup>fi</sup>eld-based user experiences of CRS within the context of clinical practice enabled us to identify a number of positive and negative themes that varied across usage trajectory groups. A summary of the quantitative and qualitative usage analysis is described in ref. [39].

The technology acceptance model, which provides a framework for understanding usage results such as those described above, is based on theory of reasoned action (TRA). TRA posits that an individual's consciously intended behavior is determined by behavioral intention: a function of the person's attitudes towards the behavior; and subjective norm: in<sup>fl</sup>uence the person receives from his or her signi<sup>fi</sup>cant others [2]. In extensions to TAM, the subjective norm construct has traditionally been measured using self-reported, general perceptions of other's in-<sup>fl</sup>uence to use software in question. As such, self-reports are incapable of delineating the structure of interpersonal networks over which a great deal of social hints and pressure is transmitted, we employed social network analysis to examine the impact of social in<sup>fl</sup>uence on individual usage. Using a survey instrument to assess the structure of three cohesion networks among the clinician users of CRS, we demonstrated [41] that: neither the professional nor the perceived in<sup>fl</sup>uence network is correlated with EHR usage; the structure of the friendship network signi<sup>fi</sup>cantly in<sup>fl</sup>uenced individual physicians' adaption of the EHR system; and residents who occupied similar social positions in the friendship network shared similar EHR utilization rates. As a result, social in<sup>fl</sup>uence affecting physician adoption of EHR seems to be predominantly conveyed through interactions with personal friends rather than interactions in professional settings.

![](/api/attachments/D53XDAQM/fulltext/images/b00c698ef991dbcf54c36b9fd36be63e9b219098c728cbbc1f3abb0b33dd42e5.jpg)  
Fig. 1. Screenshot of CRS main workspace.

Motivated by the negative theme “lack of guidance in the application work<sup>fl</sup>ow” found in the previous qualitative analysis, we employed sequential pattern analysis and a <sup>fi</sup>rst-order Markov chain model to analyze the temporal event sequences recorded in CRS. Such event sequences, or clickstreams, re<sup>fl</sup>ect clinicians' actual navigation behavior in their everyday interactions with the system. Using 10 months of interaction data between October 1, 2005 and August 1, 2006, generated by 30 users in 973 unique patient encounters, we found [38] that of 17 main EHR features provided in the system, there exist three bundled features: “Assessment and Plan” and “Diagnosis,” “Order” and “Medication,” and “Order” and “Laboratory Test,” and that clinicians often accessed these paired features in a bundle together in a continuous sequence. The Markov chain analysis further revealed a global navigational pathway, suggesting an overall sequential order of EHR feature accesses. Users showed consistent user interface navigational patterns, some of which were not anticipated by system designers or the clinic management.

Our interactions with CRS users, both direct through design meetings and direct user observation, and via clickstream data, reinforced the importance of methods to help clinicians address limitations imposed by structured data entry that may prevent them from documenting, for example, certain patient care data that could not be easily classi<sup>fi</sup>ed or codi<sup>fi</sup>ed using a given taxonomy or nomenclature. These EHR “exit strategies” may be useful aids to reduce disruptions and delays and prevent misinterpretation of the data in future patient care episodes or in research [20,22,32] but may also be misused as a speedy way of entering all types of patient care data—some of which perhaps could have been properly classi<sup>fi</sup>ed or codi<sup>fi</sup>ed with additional effort. Using data collected between September 2005 and August 2006, we found [37] that exit strategy utilization rates were not affected by post-implementation system maturity or patient visit volume, suggesting clinicians' needs to “exit” unwanted situations are persistent; and that clinician type and gender are strong predictors of exit strategy usage. Drilldown analyses further revealed that the exit strategies were judiciously used and enabled actions that would be otherwise dif<sup>fi</sup>cult or impossible. However, many data entries recorded via these strategies could have been ‘properly’ documented, yet were not, and a signi<sup>fi</sup>cant proportion containing temporary or incomplete information were never subsequently amended.

The previous research endeavors summarized in this section employed a wide range of tactics from technology improvements to the utilization of social in<sup>fl</sup>uence as a leverage to promote technology adoption among medical professionals. Collectively, they embody "methodological pluralism" that is crucial to addressing those multi-faceted user resistance issues commonly encountered in a healthcare context originating from a concatenation of system, individual, and organizational factors.

## 2.3. CRS usage analysis: trajectory analysis and new TAM constructs

To better understand previously published results on adoption and usage, we return to the technology acceptance model. Below and in subsequent sections, we propose an extension to TAM and test a number of hypotheses related to the TAM extension, using previously-published results on longitudinal usage analysis with the developmental trajectory model as a motivation.

Since its inception in 1989, TAM has been enthusiastically embraced by information systems (IS) researchers and is generally regarded as the most successful and most often applied theory developed in the IS <sup>fi</sup>eld. While TAM, its numerous model variants, and their empirical applications have provided valuable insights into what drives end users' decision to accept or reject a technology, their limitations have also been well recognized. A salient shortcoming of this family of models, for example, is its lack of consideration of the evolving nature of technology acceptance behavior [5]. In particular, TAM-based research has overly focused on predicting potential users' adoption intention, rather than the nature of ‘meaningful acceptance’ of a technology, and hence encountered dif<sup>fi</sup>culties in predicting future acceptance of technology given that users' perceptual beliefs may be subject to change over time. This issue remains unresolved in the latest developments of TAM, such as the uni<sup>fi</sup>ed theory of acceptance and use of technology [36].

Below, we address these TAM limitations by introducing a new model that accommodates the longitudinal course of acceptance behavior formation, development, and institutionalization. As for our developmental trajectory analysis, we use “actual system use” as computer-recorded objective usage instead of self-reported surrogates to test hypotheses regarding the relationship between TAM's fundamental constructs and our novel constructs, self-reported and actual usage, antecedents of TAM's fundamental constructs, and user satisfaction.

## 3. Theory and applications

## 3.1. Statement of TAM

The technology acceptance model is an adaptation of the theory of reasoned action [2] that is speci<sup>fi</sup>cally designed to study user acceptance of computer systems. The goal of TAM is to “provide an explanation of the determinants of computer acceptance that is general, capable of explaining user behavior across a broad range of end user computing technologies and user populations, while at the same time being both parsimonious and theoretically justi<sup>fi</sup>ed” [10]. As ref. [31] indicated, “TAM is intended to resolve the previous mixed and inconclusive research <sup>fi</sup>ndings associating various beliefs and attitudes with IS acceptance. It has the potential to integrate various development, implementation, and usage research streams in IS.”

The theoretical foundation of TRA is the assumption that behavioral intention in<sup>fl</sup>uences actual behavior. Davis [8] used this insight to propose that information technology acceptance behavior, actual system use (U), is determined by a person's behavioral intention to use (BI); this intention, in turn, is determined by the person's attitudes towards using (A) and his or her perceived usefulness (PU) of the IT. In TAM, attitudes towards use are formed from two beliefs: perceived usefulness (PU) of the IT and its perceived ease of use (PEoU). All external variables, such as system design characteristics, user characteristics, task characteristics, nature of the development or implementation process, political in<sup>fl</sup>uences, organization structure and so on, are expected to in<sup>fl</sup>uence acceptance behavior indirectly by affecting beliefs, attitudes, and intentions.

$$
\mathrm{BI} = \mathrm{A} + \mathrm{PU}\tag{3.1}
$$

$$
\mathrm{A} = \mathrm{PU} + \mathrm{PEoU}\tag{3.2}
$$

$$
\mathrm{PU} = \mathrm{PEoU} + \text { External   Variables }\tag{3.3}
$$

PU and PEoU are two fundamental determinants of TAM. Perceived usefulness is de<sup>fi</sup>ned as “the degree to which a person believes that using a particular system would enhance his or her job performance”, whereas perceived ease of use refers to “the degree to which a person believes that using a particular system would be free of effort”. Davis et al.'s [10] revision of the original model contains only three theoretical constructs: BI, PU, and PEoU. In addition, PEoU is postulated in post-implementation as a causal antecedent to PU, as opposed to a parallel, direct determination of BI. Fig. 2 depicts the constructs and their relations in the revised TAM model.

In con<sup>fi</sup>rmatory, empirical studies of TAM [1,10,18,33], two themes recur. First, TAM explains a substantial proportion of the variance in usage intentions and behavior, typically around 40%. Second, PU is a strong determinant of behavioral intentions—coef<sup>fi</sup>cients are typically around 6.

## 3.2. Contemporary critiques of TAM

Current research on technology acceptance addresses two categories of concerns. First, there has been a paucity of research on what constitutes meaningful acceptance of a technology. Obtaining accurate measurements of “actual system use,” TAM's outcome variable, has been particularly problematic because actual usage of a technology can be dif<sup>fi</sup>cult to de<sup>fi</sup>ne (e.g., whether frequency of use is a meaningful measure of email usage); and is oftentimes unavailable to researchers (e.g., due to prohibitive costs to collect or privacy concerns in actual usage monitoring). Consequently, the empirical applications of TAM chose to (1) only elicit a person's behavioral intention, which however may not necessarily lead to actual behavior; (2) use proxy measures that are not theoretically or empirically justi<sup>fi</sup>ed; for example, usage of an email system measured as the number of messages sent and received [12]; or (3) use self-reported usage measures in place of actual use by asking questions such as “on average, how much time do you spend on the system every day” [35] or “how many times do you believe you use this system during a week?” [17], which on one hand invites a wide range of measurement errors (e.g., the telescoping effect and the Hawthorne effect) and on the other hand may not accurately capture meaningful technology acceptance.

Second, TAM-based models are positioned to predict ‘future’ acceptance of a technology to be introduced based on ‘current’ beliefs of its potential end users, overlooking the fact that users' perceptual beliefs may be subject to change with increased use experience and continuously updated situational cues such as performance feedback and social appraisals. As observed by Rogers [23], a person's decision process of technology acceptance can be decomposed into a temporal sequence of steps from formation of attitude and adoption decision to actual use and reinforcement feedback of the adoption decision made. In addition, the mood of users, as moderated by uncertainty associated with complex tasks, may affect perceptions of ease and usefulness [11]. However, the prevalent design of TAM-based research usually assesses usage measures at the onset of technology introduction and then relates them to ‘usage’ collected at arbitrarily selected time intervals, for example 1 month post-introduction. This design, largely in<sup>fl</sup>uenced by how the original TAM validation studies were conducted, fails to accommodate the evolving aspect of technology acceptance. In addition, the time intervals are often arbitrarily selected in an atheoretical manner which may not allow for sustainable acceptance behavior to develop.

## 3.3. TAM extension variables

The true value of a technology cannot be realized until its use is institutionalized as an integral part of end users' day-to-day work. Regarded in this light, we propose to measure ‘acceptance’ as the stable usage state after the acceptance behavior of a technology has fully matured, referred to as institutionalized use (IU). In order to determine whether/when this state is reached, we introduce a new analytic method to model the development of acceptance behavior—from initial ‘trial’ adoption to long-term institutionalization—referred to as ‘developmental pattern.’ The latter construct also allows for a close perusal of the temporal dynamics in end users' acceptance behavior, so that they can be strati<sup>fi</sup>ed based on their patterns of behavioral evolution, those demonstrating problematic progression can be identi<sup>fi</sup>ed, and just-in-time behavior interventions can be introduced. These two constructs, institutionalized use and developmental pattern, together form our new conceptualization of actual, longitudinal acceptance behavior.

As previously discussed, developmental patterns are quanti<sup>fi</sup>ed using developmental trajectory analysis, a semi-parametric, group-based approach for identifying distinct groups of individual trajectories within a population and for pro<sup>fi</sup>ling the characteristics of group members [19]. In this study, we operationalize the developmental pattern construct as an end user's membership of trajectory groups (usage trajectory group— UTG) as estimated using the DTA method.

Besides TAM's PU and PEoU constructs, we also incorporate several additional variables including: (1) a person's general optimism (GO) held toward a technology, which is similar to the attitude psychological construct contained in TRA—from which TAM was derived—but differs in a way that GO assesses a person's holistic perception about the genre of the technology being introduced rather than the evaluation of a particular system or product; and (2) two computer literacy assessments: computer knowledge (CK) and computer experience (CE), which are necessary when a technology is complex requiring substantial user skills.

To examine how actual usage compares to self-reported measures, we also include in the test model self-reported usage (SRU). In addition, we include two static usage measures, initial usage (IniU) and average usage (AU), to validate TAM in the context of this study. In the empirical study the IniU measure was obtained 1 month after technology implementation following the common practice found in many TAM-based studies. Finally, we include user satisfaction (SAT) as an additional outcome variable, which has been suggested by researchers critiquing TAM for its lack of non-usage related outcome measures (e.g., [5]).

## 3.4. TAM extension hypotheses

Our <sup>fi</sup>rst two sets of hypotheses are related to TAM's constructs and traditional outcome measures:

![](/api/attachments/D53XDAQM/fulltext/images/7be1fa83505284022c62aa63781e7ac567c725a75ccdf73b20a122f248a85c4b.jpg)  
Fig. 2. Revised technology acceptance model (recreated based on [10])

• PU will predict self-reported measures including general optimism, user satisfaction and self-reported usage;

• PEoU will predict self-reported measures including general optimism, user satisfaction and self-reported usage.

The next two sets of hypotheses are related to TAM's constructs and the new outcome measures of this study based on longitudinal acceptance behavior:

• PU will not predict the actual usage measures objectively recorded (IU, UTG, IniU, and AU);

• PEoU will not predict the actual usage measures objectively recorded (IU, UTG, IniU, and AU).

We then tested the relationship between postulated antecedents of PU and PEoU and the new outcome measures, as well as the traditional TAM measures themselves:

• General optimism will predict actual acceptance behavior comprised of institutionalized use and usage group membership;

• Computer literacy scores will moderate the effect of the other predicting constructs;

• Computer literacy scores will have a direct in<sup>fl</sup>uence on the outcome variables.

Finally, to replicate previous critiques of TAM, we tested the relationship between self-reported usage and the new outcome measures:

• Self-reported usage will not be correlated with actual usage measures.

## 4. Results

## 4.1. Data collection

CRS was offered for use by 44 internal medicine residents at the Western Pennsylvania Hospital's ambulatory primary care practice between February–December 2002. The results to follow thus re<sup>fl</sup>ect the original (client–server, non-reengineered version) of CRS. The residents used the system to document and retrieve patient care data and generate patient-speci<sup>fi</sup>c reminders to improve the management of major chronic conditions and preventive care measures. During the study period, use of the system was highly recommended, however, it was not mandatory. The actual usage reported in this paper hence re<sup>fl</sup>ects the residents' true acceptance of the technology.

We selected to measure system usage as “percentage of patient visits in which the system was used to generate physician-directed reminders,” instead of “frequency of use” or “time spent using the system” as commonly used in TAM-based studies. The principal objective of the reminder system was to provide the “reminding” functionality to physicians to facilitate informed decision-making. Using the system to generate reminders is therefore the sentinel event signifying ‘meaningful’ acceptance of the technology. We monitored this usage measure continuously after the system was deployed until all users' acceptance behavior had stabilized, which occurred by the end of the 10th month after the system's “go-live” date.

We administered several questionnaire surveys to assess the perceptual constructs of the proposed model. Computer literacy and general optimism toward use of information technology in healthcare were assessed with Cork's instrument measuring physicians' use of, knowledge about, and attitudes toward computers [7]. TAM's constructs were assessed using its original survey instrument with slight rewording to <sup>fi</sup>t the context of this study. Finally, we used the IBM Satisfaction Questionnaire to elicit the resident users' satisfaction of CRS. This instrument constitutes items assessing general system usability, user interface design, and overall satisfaction [15]. Except for the Cork's survey which was administrated 1 month post-implementation, the other two surveys were conducted after the stable usage state was reached (i.e., 10 months after the system was implemented).

## 4.2. DTA developmental trajectories

Among the 44 potential users of CRS, 41 recorded valid system usage during the study period. We <sup>fi</sup>rst performed a developmental trajectory analysis of these 41 CRS users. The results show that they can be clustered into three groups each demonstrating distinct trajectory of usage development (Fig. 3).

Bold and light lines denote observed and predicted trends, respectively. Observed data values are computed as the mean use rate of users assigned to each of these groups identi<sup>fi</sup>ed by estimation, and expected values are computed using DTA model coef<sup>fi</sup>cient estimates. The three identi<sup>fi</sup>ed groups are labeled as “Heavy” (9 users including 5 users who completed all surveys), “Moderate” (15 including 12 who completed all surveys), and “Light” (17 including 11 who completed all surveys), respectively. We examine the developmental trends in Fig. 3 as follows: Users classi<sup>fi</sup>ed as “Light” initially utilized the system in about 35% of their patient encounters, and this rate remained steady over the 10-month study period. “Moderate” users had the highest initial usage, about 70%, but this rate consistently decreased over the study period to a level comparable with that of the “Light” users. “Heavy” users had an initial usage of approximately 50%, and this rate increased consistently to about 100% at the end of the study period. Changing acceptance behavior for members of the moderate group is of particular interest because it indicates that “Moderate” users demonstrated strong “enthusiasm” in use of the system initially, followed by a gradual decline in later stages. These usage measures are summarized in Table 1.

## 4.3. TAM analyses

Table 2 shows the correlation matrices of major research constructs. PU is strongly correlated with average usage (AvgU), and PEoU is strongly correlated with self-reported usage (SRU); both correlations are signi<sup>fi</sup>cant at .001 level. PU is also correlated with institutionalized use (IU, Pb.05) as well as usage group membership (UTG, Pb.01); and PEoU is correlated with self-reported user satisfaction (SAT, Pb.05).

![](/api/attachments/D53XDAQM/fulltext/images/1e2e61656953494063369e374775986ac088ef81c6fdc93fcb38bbd0e031682b.jpg)  
Fig. 3. Developmental trajectories identi<sup>fi</sup>ed.

Table 1  
Summary of actual usage measures.

<table><tr><td>Group</td><td>Initial usage</td><td>Institutionalized</td><td>Average usage</td></tr><tr><td>“Light” users</td><td>31.24</td><td>23.77</td><td>32.42</td></tr><tr><td>“Moderate” users</td><td>70.23</td><td>34.66</td><td>61.73</td></tr><tr><td>“Heavy” users</td><td>38.46</td><td>94.44</td><td>67.15</td></tr></table>

As de<sup>fi</sup>ned earlier, actual usage reported in this chapter to “percentage of patient encounters in which the system was used to generate physician reminders.”

Neither PU nor PEoU is correlated with initial usage (IniU). As TAM posits, PU is correlated with PEoU (Pb.001).

Self-reported usage is not correlated with any of the actual usage measures, nor is user satisfaction. Other interesting correlations worth noting in the table: general optimism (GO) is strongly correlated with PU, institutionalized use (IU), and AvgU (Pb.01), and computer experience (CE) is strongly correlated with both PU (Pb.05) and PEoU (Pb.01). This indicates GO and CE may be antecedents of PU or PEoU, and GO may directly in<sup>fl</sup>uence actual use behavior. Usage group membership is also strongly correlated with average usage and institutionalized use, Pb.001 for both, which indirectly con<sup>fi</sup>rms the validity of user clustering obtained by the developmental trajectory analysis. Note that usage group membership is an ordinal variable; its value roughly represents distinct usage levels, from the lowest to the highest.

Table 2 also reveals relationships among three computer literacy scales. Computer experience is signi<sup>fi</sup>cantly correlated with computer optimism. Other associations are also positive, but not statistically signi<sup>fi</sup>cant.

Hypothesis testing was performed using a series of stepwise regressions, consistent with the methods used in the original validation studies of TAM and its major extensions (e.g., [9,35]). We chose ordinal logistic regression because UGM is coded as an ordinal variable (1: “Light”; 2: “Moderate”; and 3: “Heavy”). Initial results are shown in Table 3.

Contradictory to TAM, PU has no signi<sup>fi</sup>cant in<sup>fl</sup>uence on any of the usage measures. PEoU, on the other hand, has a signi<sup>fi</sup>cantly positive impact on self-reported usage (Pb.001) and user satisfaction (Pb.01). Noticeably, both outcome variables are self-reported measures. For self-reported usage, PEoU alone explains 38% of its variance. For user satisfaction, PEoU and computer knowledge (CK) accounts for 33% of its variance. Note that CK has a negative impact on user satisfaction (Pb.01), which indicates that users who know more about computers are less satis<sup>fi</sup>ed with this application.

Institutionalized use is the main outcome variable of interest, representing the materialization of sustainable use. As shown in Table 3, this usage is signi<sup>fi</sup>cantly affected by a single factor: a person's general optimism (Pb.001). This factor alone accounts for 36% of the variance. PU or PEoU seem to have little in<sup>fl</sup>uence on this usage measure. Usage group membership, another main outcome variable, is not affected by PU or PEoU either. Instead the probability of a person's following a speci<sup>fi</sup>c developmental trajectory is jointly determined by his or her computer knowledge (Pb.05) and computer optimism (Pb.001). The estimated Logit coef<sup>fi</sup>cient of CK is negative, indicating that a higher computer knowledge score is associated with an increased probability of placing a user into a “less desirable” usage group. Initial usage was not found to be affected by any of the model's new constructs. This can be explained by the fact that all constructs were measured after sustainable use was achieved, i.e., these post-acceptance measures have little to do with a person's initial adoption decision. Average usage is in<sup>fl</sup>uenced by other computer knowledge (Pb.01) and general optimism (Pb.001); these two factors jointly explain 56% of the variance. CK, again, was found to negatively impact the average usage.

Correlation matrices of main model constructs.

<table><tr><td></td><td>PU</td><td>PEoU</td><td>SRU</td><td>IniU</td><td>IU</td><td>AvgU</td><td>SAT</td><td>CE</td><td>CK</td><td>GO</td></tr><tr><td>PU</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PEoU</td><td>.65***</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SRU</td><td>.38*</td><td>.63***</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>IniU</td><td>.19</td><td>-.0099</td><td>.12</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>IU</td><td>.39*</td><td>.17</td><td>.32</td><td>.21</td><td>-</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>AvgU</td><td>.65***</td><td>.35</td><td>.3</td><td>.49**</td><td>.74***</td><td>-</td><td></td><td></td><td></td><td></td></tr><tr><td>SAT</td><td>.34</td><td>.42*</td><td>.35</td><td>.36</td><td>.092</td><td>.32</td><td>-</td><td></td><td></td><td></td></tr><tr><td>CE</td><td>.41*</td><td>.56**</td><td>.31</td><td>.047</td><td>.32</td><td>.33</td><td>.20</td><td>-</td><td></td><td></td></tr><tr><td>CK</td><td>-.089</td><td>.25</td><td>.28</td><td>-.28</td><td>.0017</td><td>-.19</td><td>-.34</td><td>.35</td><td>-</td><td></td></tr><tr><td>GO</td><td>.59***</td><td>.28</td><td>.21</td><td>.12</td><td>.62***</td><td>-.05</td><td>.45*</td><td>.2</td><td>-</td><td></td></tr><tr><td>UTG</td><td>.55**</td><td>.28</td><td>.3</td><td>.31</td><td>.83***</td><td>.87***</td><td>.22</td><td>.21</td><td>-.22</td><td>.62***</td></tr></table>

<sup>⁎</sup>Pb.05; <sup>⁎⁎</sup>Pb.01; \*\*\*Pb.001.

The lower portion of Table 6.13 examines antecedents of PU and PEoU. As TAM posits, PEoU have a signi<sup>fi</sup>cant positive in<sup>fl</sup>uence over PU (Pb.001). CK negatively affects PU (Pb.01), consistent with <sup>fi</sup>ndings of its negative in<sup>fl</sup>uence on all other dependent variables. General optimism is another signi<sup>fi</sup>cant determinant of PU (Pb.001). These three factors together contribute to 67% of variance in perceived usefulness. PEoU has only one signi<sup>fi</sup>cant antecedent identi<sup>fi</sup>ed: computer experience. CE positively in<sup>fl</sup>uences PEoU (Pb.01), explaining 29% of its variance. This is also the only signi<sup>fi</sup>cant in<sup>fl</sup>uence of CE on other study constructs.

## 5. Discussion

## 5.1. Longitudinal analysis

Developmental trajectory results in Fig. 3 suggest that among the resident users, there existed a considerable amount of behavioral heterogeneity which should be differentially treated; for example, by introducing tailored training or incentivizing strategies to help “Moderate” avert the declining trend of usage. Further, the trajectories illustrate that end users' technology acceptance behavior could take an extended period of time to develop before arriving at the stable, saturated state (10 months in our case). Usage snapshots, such as that measured 1 month after the initial introduction of a technology, may not accurately capture the institutionalized use that is critical to achieving a sustainable performance impact.

To better illustrate the <sup>fi</sup>ndings, we present regression results reported in Table 3 as a diagram (Fig. 4). Note that only statistically signi<sup>fi</sup>cant coef<sup>fi</sup>cients are depicted in the diagram.

As shown in Fig. 4, PEoU is a strong predictor of SRU (self-reported usage). However, neither PU nor PEoU has a signi<sup>fi</sup>cant in<sup>fl</sup>uence over the actual usage measures objectively recorded. Although these <sup>fi</sup>ndings challenge the fundamental proposition of TAM, they are in agreement with previous studies that criticized use of self-reported usage measures. As discussed in earlier sections, these studies collectively reported that PU and PEoU are congruent to behavioral intention and self-reported usage, but are poor predictors of actual system usage objectively measured (e.g., [6,30,31]). Consistent with these critical studies, selfreported usage is shown to be correlated with none of the actual usages objectively measured

Table 3 Regression results.

<table><tr><td rowspan="2">Dependent variables</td><td colspan="5">Independent variables</td><td rowspan="2"> $R^{2}$ </td></tr><tr><td>PU</td><td>PEoU</td><td>CE</td><td>CK</td><td>GO</td></tr><tr><td colspan="7">Results explaining usage measures</td></tr><tr><td>Self-reported (SRU)</td><td>ns</td><td>.86***</td><td>ns</td><td>ns</td><td>ns</td><td>.38</td></tr><tr><td>Initial usage (IniU)</td><td>ns</td><td>ns</td><td>ns</td><td>ns</td><td>ns</td><td>-</td></tr><tr><td>Institutionalized use (IU)</td><td>ns</td><td>ns</td><td>ns</td><td>ns</td><td>.27***</td><td>.36</td></tr><tr><td>Average usage (AvgU)</td><td>ns</td><td>.047</td><td>ns</td><td>-.089**</td><td>.17***</td><td>.56</td></tr><tr><td>Satisfaction (SAT)</td><td>ns</td><td>.69**</td><td>ns</td><td>-.76**</td><td>ns</td><td>.33</td></tr><tr><td>Usage trajectory group (UTG) $^{a}$ </td><td>ns</td><td>ns</td><td>ns</td><td>-1.64*</td><td>2.99***</td><td>-</td></tr><tr><td colspan="7">Results explaining PU and PEoU</td></tr><tr><td>Perceived usefulness (PU)</td><td>-</td><td>.63***</td><td>ns</td><td>-.45**</td><td>.74***</td><td>.67</td></tr><tr><td>Perceived ease of use (PEoU)</td><td>-</td><td>-</td><td>.86**</td><td>ns</td><td>ns</td><td>.29</td></tr></table>

<sup>⁎</sup>Pb.05; <sup>⁎⁎</sup>Pb.01; <sup>⁎⁎⁎</sup>Pb.001. Adjusted R<sup>2</sup>s and standardized coef<sup>fi</sup>cients are shown. <sup>a</sup> Estimated using ordinal logistic regression with MLE.

![](/api/attachments/D53XDAQM/fulltext/images/ba4b081035b89298bf5a235fc37f7718ef0b0ceb616df0e09d7ecbc17287beca.jpg)  
Fig. 4. Results of model testing (<sup>⁎</sup>Pb.05; <sup>⁎⁎</sup>Pb.01; <sup>⁎⁎⁎</sup>Pb.001).

General optimism, on the other hand, is the most in<sup>fl</sup>uential factor that has a signi<sup>fi</sup>cant, positive impact on several outcome variables (IU, UTG, and AU). This result suggests that an end user's perception of the genre of the technology being introduced can be a stronger behavioral determinant as compared to the perceived usefulness and ease of use evaluation of a particular system or a particular product. Seeking ways to foster potential users' positive, holistic attitude toward a technological innovation may hence greatly increase the likelihood of success of its implementation instances. Although no signi<sup>fi</sup>cant impact is found by PU on either self-reported or actual behavior, perceived usefulness is positively associated with general optimism, i.e., GO positively and strongly in<sup>fl</sup>uences PU. The determinant role of general optimism shown in this study con<sup>fi</sup>rms previously published results [39], which state that “Heavy” users have a signi<sup>fi</sup>cant higher computer optimism score comparative to other users, and GO signi<sup>fi</sup>cantly in<sup>fl</sup>uences the membership probability of usage groups. Although CRS needed further improvement and objective barriers such as time constraints existed, “Heavy” users were willing to adapt their practice style to accommodate use of the system: they documented the clinical observation and generated and responded to reminders after patient encounter. In contrast, other types of users simply refused to adopt the system (light user group), or abandoned its use after initial trials (moderate user group).

Counter to intuition, computer knowledge has a consistent negative impact on several outcome variables (UTG, AU, SAT). Zheng et al. [39] report a similar <sup>fi</sup>nding using developmental trajectory analysis: an increase in computer knowledge score decreases the probability of a user's being categorized into heavy user group.<sup>1</sup> We interpret this result to mean that a computer savvy user will hold higher performance expectations of software applications. In addition, a system's de<sup>fi</sup>ciencies may be more transparent to knowledgeable users as compared to novice users. These effects may have an adverse impact on a person's willingness to adapt to accommodate the use of a system. Nonetheless, this <sup>fi</sup>nding indicates that inadequate computer literacy is no longer a barrier to physicians' adoption of IT, especially with a younger generation of physicians (mean age of the medical residents participated in this study is 29.6), because improved computer knowledge does not necessarily lead to an increased likelihood of acceptance.

## 5.2. System evolution, usage and impact in practice

We now discuss the importance of the longitudinal analysis results in the context of CRS' development and the series of <sup>fi</sup>ndings from this stream of work. CRS, designed as an evidence-based medical reminder system for small primary care physician practices, evolved over time into a ‘lightweight’ EHR system in response to user feedback and observed trends in usage ([39] and the current study). Our focus on usability and user acceptance is highly relevant given recent results that cast doubt on the ef<sup>fi</sup>cacy of EHRs and CDSS in practice, as opposed to laboratory settings or small-scale implementations [24]. Multidimensional analyses of a re-engineered version of CRS, e.g. interface design [38,40], social context for usage [41] and exit strategies [37], rooted in actual usage, is a model for future application development in research and practice. In particular, implementation of professional-quality applications in the practice context, routine and detailed collection of actual usage data, and analysis of the usage context are essential to developing health IT applications that are likely to be used and to improve medical practice.

## 6. Conclusions

This paper proposes a new conceptualization of technology acceptance—constituting institutionalized use and developmental pattern—to study the longitudinal behavioral adaptation and change. This new view of technology acceptance is presented in the context of a highly-engineered application that has been extensively revised to account for observed trends in usage and user feedback and which we feel embodies best research practices for IT development and evaluation.

To operationalize the developmental pattern construct, we used a semi-parametric, group-based modeling approach that identi<sup>fi</sup>es distinct patterns of trajectories within a population. We validated this model in an empirical setting where a clinical decision-support system was introduced to a group of internal medicine residents. We show that the new model, an extension to the original TAM incorporating four objective measures of actual usage from an implemented EHR, is able to reveal richer details of end users' acceptance of technology, while the original TAM performs poorly in explaining observed developmental behavior when relying on traditional self-reported usage measures derived from the Cork et al. [7] survey instrument.

The stream of research on electronic health records represented by our work on CRS, including the TAM extension, as discussed in this paper, embodies a number of features identi<sup>fi</sup>ed by [3] as essential for the health of the DSS discipline: it is directly relevant to medical practice; it is based on directly-measured usage of a professional-quality IT artifact, and it has bene<sup>fi</sup>tted from external funding. As such, our work makes a contribution to resolving the “tension between academic rigor and professional relevance” (p. 667).

This new notion of technology acceptance supports our multidimensional analysis of application usage: sophisticated users of IT applications have high expectations of application quality, and traditional notions of comfort with IT are not associated with levels of usage. Thus, future analyses of health IT applications must rigorously address ‘simple usage’—instances of interaction with system to understand adoption; ‘complex usage’—details of interaction with user interface (including exception management), and ‘usage context’—how users interact with each other and reinforce system usage, or lack thereof.

## References

[1] D.A. Adams, R.R. Nelson, P.A. Todd, Perceived usefulness, ease of use, and usage of information technology: a replication, MIS Quarterly 16 (2) (1992) 227–247.

[2] I. Ajzen, M. Fishbein, Understanding Attitudes and Predicting Social Behavior, Prentice-Hall, Englewood Cliffs, NJ, 1980.

[3] D. Arnott, G. Pervan, Eight key issues for the decision support systems discipline, Decision Support Systems 44 (2008) 657–672.

[4] D.W. Bates, L.L. Leape, D.J. Cullen, N. Laird, L.A. Petersen, J.M. Teich, E. Burdick, M. Hickey, S. Klee<sup>fi</sup>eld, B. Shea, M. Vander Vliet, D.L. Seger, Effect of computerized physician order entry and a team intervention on prevention of serious medication errors, Journal of the American Medical Association 280 (15) (1998) 1311–1316.

[5] I. Benbasat, H. Barki, Quo vadis, TAM? Journal of AIS 8 (4) (2007) 211–218.

[6] W.W. Chin, The measurement and meaning of IT usage: reconciling recent discrepancies between self reported and computer recorded usage, in: Proceedings of the Administrative Sciences Association of Canada, Information Systems Division. Montreal, Quebec, Canada, 1996, pp. 65–74.

[7] R.D. Cork, W.M. Detmer, C.P. Friedman, Development and initial validation of an instrument to measure physicians' use of, knowledge about, and attitudes toward computers, Journal of the American Medical Informatics Association 5 (2) (1998) 164–176

[8] F.D. Davis. A Technology Acceptance Model for Empirically Testing New End-User Information Systems: Theory and Results. PhD thesis, Sloan School of Management, Massachusetts Institute of Technology, 1986.

[9] F.D. Davis, Perceived usefulness, perceived ease of use, and user acceptance of information technology, MIS Quarterly 13 (3) (1989) 319–340.

[10] F.D. Davis, R.P. Bagozzi, P.R. Warshaw, User acceptance of computer technology: a comparison of two theoretical models, Management Science 35 (8) (1989) 982–1003.

[11] S. Djambasi, D.M. Strong, M. Dishaw, Affect and acceptance: examining the effects of positive mood on the technology acceptance model, Decision Support Systems 48 (2010) 383–394.

[12] D. Gefen, D.W. Straub, Gender differences in the perception and use of E-mail: an extension to the technology acceptance model, MIS Quarterly 21 (4) (1997) 389–400.

[13] A.K. Jha, C.M. DesRoches, E.G. Campbell, K. Donelan, S.R. Rao, T.G. Ferris, A. Shields, S. Rosenbaum, D. Blumenthal, Use of electronic health records in U.S. hospitals, The New England Journal of Medicine 360 (16) (2009) 1628–1638.

[14] B. Kaplan, Evaluating informatics applications—some alternative approaches: theory, social interactionism, and call for methodological pluralism, Internationa Journal of Medical Informatics 64 (1) (2001) 39–56.

[15] J.R. Lewis, IBM computer usability satisfaction questionnaires: psychometric evaluation and instructions for use, International Journal of Human Computer Interaction 7 (1) (1995) 57–78.

[16] J.A. Linder, J.L. Schnipper, R. Tsurikova, et al., Documentation-based clinical decision support to improve antibiotic prescribing for acute respiratory infections in primary care: a cluster randomised controlled trial, Informatics in Primary Care 17 (4) (2009) 231–240.

[17] Y. Malhotra, D.F. Galletta, Extending the Technology Acceptance Model to account for Social In<sup>fl</sup>uence: Theoretical Bases and Empirical Validation, in: Proceedings of the 32nd Annual HICSS IEEE Computer Society Washington DC 1999 pp, 1006–1020

[18] K. Mathieson, Predicting user intentions: comparing the technology acceptance model with the theory of planned behavior, Information Systems Research 2 (3) (1991) 173–191.

[19] D.S. Nagin, Analyzing developmental trajectories: a semi-parametric, group-based approach, Psychological Methods 4 (2) (1999) 139–157.

[20] M.B. Palchuk, E.A. Fang, J.M. Cygielnik, M. Labreche, M. Shubina, H.Z. Ramelson, et al., An unintended consequence of electronic prescriptions: prevalence and impact of internal discrepancies, Journal of the American Medical Informatics Association 17 (4) (2010) 472–476.

[21] L. Perreault, J. Metzger, A pragmatic framework for understanding clinical decision support, Journal of Healthcare Information Management 13 (2) (1999) 5–21.

[22] E.T. Rhodes, L.M. Laffel, T.V. Gonzalez, D.S. Ludwig, Accuracy of administrative coding for type 2 diabetes in children, adolescents, and young adults, Diabetes Care 30 (1) (2007) 141–143.

[23] E.M. Rogers, Diffusion of Innovations, The Free Press, New York, 1983.

[24] M.J. Romano, R.S. Stafford, Electronic health records and clinical decision support systems: impact on national ambulatory care quality, Archives of Internal Medicine 171 (10) (2011) 897–903.

[25] D.L. Sackett, M.C. Rosenberg, J.A. Gray, R.B. Haynes, W.S. Richardson, Evidence based medicine: what it is and what it isn't, British Medical Journal 312 (7023) (1996) 71–72.

[26] H.M. Seidling, S.P. Schmitt, T. Bruckner, et al., Patient-speci<sup>fi</sup>c electronic decision support reduces prescription of excessive doses, Quality & Safety in Health Care 19 (5) (2010) e15.

[27] O.R.L. Sheng, Decision support for healthcare in a new information age, Decision Support Systems 30 (2000) 101–103.

[28] K.G. Shojania, A. Jennings, A. Mayhew, C. Ramsay, M. Eccles, J. Grimshaw, Effect of point-of-care computer reminders on physician behaviour: a systematic review, Canadian Medical Association Journal 182 (5) (2010) E216–E225.

[29] I. Sim, P. Gorman, R.A. Greenes, R.B. Haynes, B. Kaplan, H. Lehmann, P.C. Tang, Clinical decision support systems for the practice of evidence-based medicine Journal of the American Medical Informatics Association 8 (6) (2001) 527–534.

[30] D. Straub, M. Limayem, E. Karahanna-Evaristo, Measuring system usage: implications for IS theory testing, Management Science 41 (8) (1995) 1328–1342.

[31] B. Szajna, Empirical evaluation of the revised technology acceptance model, Management Science 42 (1) (1996) 85–92

[32] P.C. Tang, M. Ralston, M.F. Arrigotti, L. Qureshi, J. Graham, Comparison of methodologies for calculating quality measures based on administrative data versus clinical data from an electronic health record system: implications for performance measures, Journal of the American Medical Informatics Association 14 (1) (2007) 10–15

[33] S. Taylor, P. Todd, Understanding information technology usage: a test of compet ing models Information Systems Research 6 (2) (1995) 145–176

[34] H. van der Sijs, J. Aarts, A. Vulto, M. Berg, Overriding of drug safety alerts in computerized physician order entry, Journal of the American Medical Informatics Association 13 (2) (2006) 138–147.

[35] V. Venkatesh, F.D. Davis, A theoretical extension of the technology acceptance model: four longitudinal <sup>fi</sup>eld studies, Management Science 46 (2) (2000) 186–204.

[36] V. Venkatesh, M.G. Morris, G.B. Davis, F.D. Davis, User acceptance of information technology: toward a uni<sup>fi</sup>ed view, MIS Quarterly 27 (3) (2003) 425–478.

[37] K. Zheng, D.A. Hanauer, R. Padman, M.P. Johnson, A.A. Hussasin, W. Ye, X. Zhou, H.S. Diamond, Handling anticipated exceptions in clinical care: investigating the bene<sup>fi</sup>ts and consequences of providing ‘exit strategies’ in an electronic health records system, Journal of the American Medical Informatics Association 18 (6) (2011) 883–889.

[38] K. Zheng, R. Padman, M.P. Johnson, H.S. Diamond, An interface-driven analysis of user behavior of an electronic health records system, Journal of the American Medical Informatics Association 16 (2) (2009) 228–237.

[39] K. Zheng, R. Padman, M.P. Johnson, H.S. Diamond, Understanding technology adop tion in clinical care: clinician adoption behavior of a point-of-care reminder system, International Journal of Medical Informatics 74 (7–8) (2005) 535–543.

[40] K. Zheng, R. Padman, M.P. Johnson, S. Hasan, Guideline representation ontologies for evidence-based medicine practice, in: K. Khoumbati, A. Srivastava, Y.K. Dwivedi, B. Lal (Eds.), Handbook of Research on Advances in Health Informatics and Electronic Healthcare Applications, Medical Information Science Reference, Hershey, PA, 2009.

[41] K. Zheng, R. Padman, D. Krackhardt, M.P. Johnson, H.S. Diamond, Social networks and physician adoption of electronic health records: insights from a pilot study, Journal of the American Medical Informatics Association 17 (3) (2010) 328–336.

![](/api/attachments/D53XDAQM/fulltext/images/64d968cf10723f0d819e733230d3d776039955126a804b88b01f1bf85de4269a.jpg)

Dr. Michael P. Johnson is Associate Professor in the Department of Public Policy and Public Affairs at University of Massachusetts Boston. Dr. Johnson received his Ph.D in operations research from Northwestern University in 1997 and B.S. from Morehouse College in 1987.

Dr. Johnson’s research interests lie in community-based opera tions research, with applications primarily to housing and community development. His methods enable organizations serving disadvantaged and vulnerable populations to develop programs that optimize economic ef<sup>fi</sup>ciency, population outcomes and social equity. Current research projects include: planning models for foreclosed housing acquisition and redevelopment; decision modeling for municipal shrinkage, and collaboration among non-pro<sup>fi</sup>t organizations.

and proceedings. He is editor of Community-Based Operations Research: Decision Modeling for Local Impact and Diverse Populations (Springer, 2011) and has co-edited Tutorials in Operations Research 2006 (Institute of Operations Research and the Management Sciences, 2006).

![](/api/attachments/D53XDAQM/fulltext/images/141f77feaadbbd34ab0decca207a42c974c25b03aaf3730ff3025ba84dd3589f.jpg)

Kai Zheng, Ph.D., is jointly appointed as Associate Professor of Health Management and Policy in the School of Public Health and Associate Professor of Information in the School of Information at the University of Michigan. He is also affiliated with the University of Michigan's School of Nursing, Medical School Department of Computational Medicine and Bioinformatics and Center for Entrepreneurship. He co-directs the Bio-Repository and Biomedical Informatics Core of the University of Michigan Health System and Peking University Health Science Center Joint Institute for Translational and Clinical Re search.

Zheng received his Ph.D. degree from Carnegie Mellon University, where his dissertation entitled won the University’s 2007 William W. Cooper Doctoral Dissertation Award in

Management or Management Science. He is the recipient of the 2011 American Medical Informatics Association New Investigator Award that recognizes early informatics contributions and significant scholarly contributions on the basis of scientific merit and research excellence.

![](/api/attachments/D53XDAQM/fulltext/images/7ab2b38a998ada1c64c821da1d7181b9feebcd434444f61d02aca67fc1d326e9.jpg)

Rema Padman is Professor of Management Science and Healthcare Informatics and Thrust Leader of Healthcare Informatics Research at iLab in H. John Heinz III College at Carnegie Mellon University, and Adjunct Professor in the Department of Biomedical Informatics at the University of Pittsburgh School of Medicine. Dr. Padman received B.Tech. in Chemical Engineering, Indian Institute of Tech nology; PhD in Operations Research, University of Texas at Austin; and National Library of Medicine Senior Fellowship in Applied Informatics, University of Pittsburgh School of Medicine.

Dr. Padman’s research examines healthcare operations and decision support, privacy and con<sup>fi</sup>dentiality, and process modeling and risk analysis in the context of IT interventions in healthcare delivery and management, such as e-health and chronic disease management. She has served on review panels for NSF and NIH, and Medical Research Council in UK. She is Associate Editor with INFORMS Journal on Computing and Information Technology and Management and past Associate Editor for Operations Research.
