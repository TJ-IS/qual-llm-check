---
otero_id: 15538
otero_key: "GXNKNFBM"
title: "A decision support system for lower back pain diagnosis: Uncertainty management and clinical evaluations"
authors: "Lin Lin; Paul Jen-Hwa Hu; Olivia R. Liu Sheng"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.10.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 42 (2006) 1152–1169

www.elsevier.com/locate/dsw

# A decision support system for lower back pain diagnosis: Uncertainty management and clinical evaluations

Lin Lin <sup>a</sup>, Paul Jen-Hwa Hu <sup>b</sup>, Olivia R. Liu Sheng <sup>b,\*</sup>

Department of Management, College of Business and Economics, Lehigh University Bethlehem, PA 18015, USA <sup>b</sup> Accounting and Information Systems, David Eccles School of Business, University of Utah, Salt Lake City, Utah 84112, USA

Received 2 July 2003; received in revised form 6 October 2005; accepted 13 October 2005 Available online 3 February 2006

## Abstract

Lower back pain (LBP) is a common medical problem that deprives many individuals of their normal lifestyles and keeps them from routine activities. Diagnosing LBP is challenging because it requires highly specialized knowledge involving a complex anatomical and physiological structure as well as diverse clinical considerations. Although a handful of studies have proposed or developed systems to support LBP diagnosis and improve knowledge sharing, these systems have limited scope, lack systematic evaluations, and/or ignore diagnoses that consist of multiple parts (i.e., decision outcomes), each of which corresponds to a particular medical condition, disease, or abnormality. In this study, we design, implement, and evaluate a Web-based decision support system that employs an intuitive and easy-to-use framework to assess the patient’s information and recommend a diagnosis consisting of one or multiple parts. Our system design addresses the challenging characteristics of a LBP diagnosis and uses verbal probability estimation to represent and reason about the associated uncertainty. Our evaluations are systematic, including knowledge base verification, system validation using a modified Turing test, and clinical efficacy assessment involving 5 clinicians and 180 real-world cases collected from geographically dispersed clinics. Our evaluation design is more thorough than those used by most previous studies, and the proposed system is relatively ready for clinical deployment. Therefore, this study both contributes to decision support systems research and has advanced clinical support for LBP diagnosis. In light of some of the limitations of this study, we also identify and discuss several areas that need continued investigation.

Keywords: Low back pain diagnosis; Decision support system; Rule-based system; Consensus model; System evaluation; System verification and validation; Turing test; Diagnosis

## 1. Introduction

The use of decision support systems in clinical medicine has received considerable attention from information systems researchers and practitioners [2,6,17,23,38– 40]. Of particular importance is diagnosis decision-making, a critical aspect of patient care and management by healthcare professionals. Broadly, diagnosis refers to a classification process through which the attending clinician, on the basis of information and symptoms collected, assigns a new patient to one or more pre-specified medical conditions (e.g., illness/disease, injury, abnormality) [36]. An inadequate or incorrect diagnosis can adversely affect subsequent patient treatment or management plan. When diagnosing a patient, a clinician often needs complex and highly specialized knowledge that may not be accessible in a convenient and timely manner. In this vein, the use of a decision support system that embraces pertinent diagnosis knowledge is desirable, particularly because it may improve service quality and diagnosis knowledge accessibility and dissemination.

Although clinical diagnosis decision-making support has been examined by previous research, several challenges remain, including the representation of the associated uncertainty, reasoning under uncertainty, the support of a non-exclusive multi-part diagnosis<sup>1</sup> (in which each part refers to a specific medical condition, illness, injury, or abnormality), and systematic clinical evaluation. Many clinical diagnosis tasks involve reasoning under uncertainty. Although different methods have been proposed to model such uncertainty, including certainty factor [6,7], Bayesian theory [1,30], belief functions [11,31], and fuzzy logic [42], these methods require significant probability estimation efforts by domain experts and thus often create bottlenecks in the already tedious and time-consuming knowledge acquisition process. The support of diagnosis that contains multiple non-exclusive medical conditions represents another challenge to the development of clinical decision support systems [36]. Conceivably, a patient may be diagnosed with multiple medical conditions simultaneously. Unfortunately, only few systems are able to support multiple-part diagnosis. In addition, a clinically viable system requires systematic and thorough evaluation. To be accepted and routinely used by targeted clinicians, a diagnosis support system must embrace verifiable domain knowledge, exhibit appropriate validity, and demonstrate sufficient clinical efficacy. A review of extant literature suggests that most previous research has addressed some but not all of these fundamental evaluation requirements.

In this research, we develop a system to support clinicians’ diagnosis of lower back pain (LBP), a prevailing medical problem that requires appropriate responses to several challenging characteristics. Although LBP has been identified as a common cause of missed work and altered lifestyles among adults [40], its diagnosis is challenging and requires highly specialized knowledge that involves a complex anatomical and physiological structure, diverse clinical considerations, and nonstandard terminology [10]. As Jackson et al. [19] note, only approximately 15% of LBP patients surveyed had received accurate diagnoses with some degree of certainty. Clinicians usually acquire their diagnosis knowledge experientially in an intensive, time-consuming process. Therefore, a system-based approach for supporting their diagnosis of LBP patients is appealing and can improve both diagnosis quality and timely knowledge access.

We report the design, implementation, and evaluation of a diagnosis support system whose design addresses the challenging characteristics of LBP diagnosis. We used multiple complementary methods to acquire the targeted knowledge from two highly experienced domain experts who practice in different clinics in distant geographic regions. We used verbal probability estimation to capture and represent uncertainty, and we developed a voting scheme for knowledge inference on the basis of consensus-based modeling. Our system is Web based and architecturally consists of a knowledge base, an inference engine, a case repository, and two interfaces for convenient system access and knowledge update. To ensure the system’s validity and clinical utility, we verified our knowledge base, examined the system<sup>T</sup>s validity, and evaluated its efficacy using 180 cases collected from various clinics.

This study makes several contributions to decision support systems research. First, we propose an intuitive and easy-to-use framework for representing and reasoning about diagnosis knowledge that both involves uncertainty and may consist of multiple decision outcomes simultaneously (i.e., a multi-part diagnosis). This framework can alleviate the relentless probability-estimation requirements of domain experts and thereby facilitate the conventional knowledge-engineering process. We also demonstrate a systematic and thorough approach to developing and evaluating a clinical diagnosis support system using LBP diagnoses for illustration. Our system development attends to issues pertinent to problem analysis, system design, knowledge base verification, system validation, and clinical efficacy assessment. Clinically, this study responds to the need for a system-based approach to support clinicians’ diagnoses of LBP. Our evaluations arguably are more systematic and thorough than those involved in most previous research [5,16]. In turn, our proposed system may be more ready for clinical deployment than were those reported by most previous studies.

The organization of the article is as follows. In Section 2, we provide an overview of LBP, together with the challenging characteristics that must be addressed during the development of a diagnosis support system. In Section 3, we review relevant previous research and highlight our motivation. We then describe our system design and implementation (including system architecture, knowledge acquisition, representation, and inference) in Section 4. In Section 5, we detail our verification, validation, and clinical evaluation designs and discuss some important results. Finally, we conclude in Section 6 with a summary, a discussion of the contributions of this study, and some future research directions.

![](/api/attachments/GXNKNFBM/fulltext/images/499648bd28acf0d8051ecdf15d03ec6ff7ec7d9aa0a7a9c3d9f14c7f7470d932.jpg)  
Fig. 1. The common S.O.A.P. process for managing LBP patients by physical therapists.

## 2. Overview of lower back pain and its diagnosis

Anatomically, the <sup>b</sup>lower back<sup>Q</sup> refers to a complex structure of vertebrae, disks, and nerves and the spinal cord. A prevailing physiological and medical problem, LBP is often accompanied by or results from common colds and other illnesses. According to Waddell [40], four out of five adults will experience some significant LBP in their lives. The diagnosis of persistent and oppressive LBP is challenging partially because the underlying pathology may not be easily identifiable [25]. When diagnosing a LBP patient, the attending clinician usually must assess physical, social, behavioral, and/or environmental factors. In addition, LBP patients often exhibit symptoms commonly observable in individuals free of LBP, making the clinician’s diagnosis increasingly difficult [5].

Different groups of clinicians, including physical therapists, orthopedists, general practitioners, and pain specialists, have treated LBP patients. These different groups of care providers may vary subtly, or even considerably, with respect to their pain epidemiology, training, diagnosis decision-making, therapeutic protocol design/selection, and overall patient management plan. Among them, physical therapists probably are the most frequently sought-after care providers and therefore are the targets of our research.<sup>2</sup>

2.1. Common process for managing LBP patients by physical therapists

The S.O.A.P. (subjective testing, objective testing, assessment, and planning) process is common for LBP patient management by physical therapists. As shown in Fig. 1, this process consists of four distinct, sequentially connected phases. In the initial subjective testing phase, the physical therapist collects relevant patient history and clinical information. Central to this phase is a question-and-answer session, which is based on question items designed to identify probable cause(s), explanation(s), and the nature of the pain being evaluated. Using the patient’s responses, the therapist establishes a baseline understanding in terms of the pain description, location(s), activation, severity, and frequency, as well as important patient symptoms. The subjective testing phase also enables the therapist to acquire the patient’s own assessment of and concerns about the LBP problem in relation to his or her clinical history, such as previous medical problems and/or treatments. By documenting and analyzing such information, the therapist then generates a diagnosis<sup>3</sup> (consisting of one or multiple parts), which in turn provides a basis for his or her subsequent evaluation and therapeutic protocol design/ selection. The tasks included in this initial phase are knowledge intense, and their effectiveness largely depends on the attending therapist’s experience.

In the objective testing phase, the therapist performs physical examinations to confirm or refine his or her preliminary diagnosis. This testing usually proceeds in an iterative fashion and may require additional (subjective) question-and-answer sessions, particularly when the preliminary diagnosis is not supported by the examination results. After confirming a preliminary diagnosis, the therapist advances to the assessment phase, in which he or she evaluates the pain epidemiology, severity, and plausible therapeutic protocols. In the final patient management planning phase, the therapist designs (or selects) an appropriate therapeutic protocol and administers it to the patient. The attending therapist continually monitors and assesses the patient’s response and then revises the diagnosis and/or treatment plan accordingly. This process continues until it terminates with satisfactory patient recovery.

Central to the S.O.A.P. process is the accuracy of the preliminary diagnosis in the subjective testing phase, which has significant impacts on the subsequent patient assessment, therapeutic protocol design/selection, and overall patient treatment plan. An inadequate diagnosis demands unnecessary testing and can lead to the selection of an ineffective therapeutic protocol or patient management plan. As a consequence, service quality is diminished, and the patient’s well-being is adversely affected.

## 2.2. Challenging characteristics of LBP diagnosis

Anatomically, the diagnosis of LBP problems requires a systematic approach to identify the particular tissues embracing nerve supplies that cause the pain [27]. Clinicians often depend on the patient’s responses and examination results to diagnose LBP problems. However, effective diagnosis is challenging largely because of the inevitable uncertainty associated with analysis [19]. Such uncertainty can be attributed partly to the multiplicity of treatment methods and plans that have yielded inconclusive or even questionable diagnostic efficacy [14].

Several characteristics of an LBP diagnosis are important and need to be properly addressed. First, effective diagnosis requires highly specialized knowledge. Second, a physical therapist may reach a (preliminary) diagnosis that consists of multiple parts, each of which refers to a specific medical condition, disease, or abnormality, probably due to incomplete patient information. Third, therapists, even highly experienced ones, may have great difficulty articulating their diagnosis knowledge. Fourth, the availability or accessibility of important diagnosis knowledge appears to be confined largely by geographic proximity or personal networks, which makes timely knowledge access and sharing difficult. Coupled with the stringent time constraints commonly placed on clinicians, these challenging characteristics are likely to affect the quality of patient care and management.

Efforts to establish general guidelines for diagnosis and therapeutic protocols have been observed [14,18,28,35]. These guidelines, or protocols, often differ considerably in purpose; for example, some emphasize clinical history analysis [14,18], whereas others target clinical examinations or patient treatment [35]. Regardless, few (if any) have been systematically evaluated for their validity or clinical efficacy. The use of medical imaging technology, including discography and radiography, to support clinicians’ LBP diagnoses has also been investigated. Although radiographic evidence may suggest probable cause(s) of an LBP problem, the images can be difficult to read and often are plagued by wide variations in interpretation and frequent false-positive or false-negative findings [12]. Previous research also has suggested inconclusive associations between particular radiographic findings and patient symptoms [12]. Discography is an alternative to radiography but has not yet demonstrated convincing clinical efficacy in LBP diagnoses [26]. The probability of making an accurate diagnosis by using discography may be less than 15%, mainly because of the ambiguity in the relationships between radiological findings and patient symptoms [12,32].

These prevailing LBP problems and clinicians’ limited access to meager diagnosis knowledge make a system-based approach to support LBP diagnosis appealing, particularly when that approach satisfactorily addresses the issues surrounding system validity and clinical efficacy. A decision support system based on an adequate design and implementation can facilitate and enhance therapists’ acquisition, sharing, and use of specialized knowledge that is critical for effective LBP patient management. In this role, the system must encompass pertinent diagnosis knowledge and demonstrate sufficient validity and clinical efficacy through systematic evaluations.

## 3. Literature review and motivation

## 3.1. Diagnosis involving uncertainty

Uncertainty is common to many clinical diagnosis tasks and thus represents a fundamental challenge in the development of clinical decision support systems. Several methods have been proposed to represent or reason about uncertainty. Considerable prior research adopted a certainty factor scheme to model the certainty (confidence level) of a system-recommended decision, such as a diagnosis [6]. The certainty value associated with a particular rule usually is determined by the presence of specific evidence that has been identified or emphasized by domain experts or related literature. The overall <sup>b</sup>degree of belief<sup>Q</sup> of a decision outcome can be calculated by combining all relevant evidence and symptoms probabilistically [6]. Alternative methods based on formal modeling also have been examined, including Bayesian theory [30] and belief functions [11,31], which draw their theoretical premises from probabilistic and set theories, respectively. Regardless of the representation or modeling differences, these approaches require substantial numerical probability estimations from domain experts.

Eliciting numerical probability estimates from domain experts is difficult and susceptible to considerable bias, particularly when an adequate anchor is lacking or the experts are not properly calibrated [20]. The likelihood of inconsistent estimates increases with the sheer volume or complexity of the targeted knowledge. Previ ous research has examined different methods for eliciting numerical probability estimates, such as having experts mark their assessments on a visual probability scale or making choices between risky or uncertain alternatives (i.e., risk-laden gambling) [37]. However, such methods are not directly applicable to LBP diagnoses for several reasons. First, physical therapists in general are not experienced in numerical probability assessments, thus making the use of a probability scale to articulate, visualize, and interpret conditional probabilities difficult. Second, from a reasoning perspective, probabilistic combinations of individual rules for an LBP diagnosis differ from those proposed and used for the diagnosis tasks examined by previous studies. For example, the presence or absence of particular evidence can rule out a particular medical condition, disease or abnormality completely rather than merely affecting its degree of belief. To address this <sup>b</sup>exclusive negation<sup>Q</sup> (elimination) characteristic and mitigate the probability assessment requirements from domain experts, we propose a certainty factor scheme based on an uncertainty representation and reasoning framework that is intuitive and easy to use. Our approach employs verbal probability estimation [37] and is more effective for facilitating estimations by domain experts, as compared with methods based on Bayesian theory or belief functions. The performance of the proposed framework is robust and not highly sensitive to the precision of an expert’s certainty estimates for individual rules. Therefore, our approach for addressing the exclusive negation characteristic of an LBP diagnosis differs from the certainty factor and its variations, as used in previous research; e.g. [8].

## 3.2. Support of nonexclusive, multi-part clinical diagnosis

The support of a simultaneous, multi-part diagnosis has been an ongoing challenge for the development of clinical decision support systems [36]. Considerable prior research ignored this challenge by assuming that patients suffered from specified, mutually exclusive medical conditions one at a time (e.g., Pathfinder [17]). In this way, they were able to model the underlying medical condition using the single state of a discrete stochastic variable. Other studies have modeled a medical condition using a stochastic variable and thus were able to address multiple conditions simultaneously (e.g., MUNIN [36]).

When treating LBP patients, therapists often make their diagnoses under uncertainty; that is, they choose among multiple, nonexclusive medical conditions that may vary considerably in probability. The simultaneous existence of two or more medical conditions in a patent cannot be ignored and therefore requires that the clinician reach a nonexclusive, multi-part diagnosis. We address this requirement by examining the confidence level of each specified medical condition independently and thereby allow multiple medical conditions to compete on a likelihood basis. Whereas most rule-based systems use a certainty factor scheme to support such competitions among individual rules, a review of extant literature suggests that limited efforts have explicitly addressed simultaneous, multiple decision outcomes in which each outcome corresponds to a particular medical condition included as a part of the diagnosis. In addition, constructing a probabilistic, rule-based system capable of ranking or differentiating multiple decision outcomes on the basis of their respective likelihoods requires considerable probability elicitation or a complex and computationally demanding stochastic model [36]. More importantly, most prior studies focus on accuracy-oriented, dichotomous evaluation metrics that typically categorize a case as either correct or incorrect, which is not sufficient for assessing a system’s effectiveness in support of a nonexclusive, multi-part diagnosis that includes multiple decision outcomes simultaneously.

## 3.3. <sup>b</sup>Completeness<sup>Q</sup> of clinical decision support systems

Most systems reported by previous research have limited completeness in terms of scope and clinical readiness. In particular, these systems have not been examined systematically for their validity or clinical efficacy [33,34]. A review of related previous studies highlights their prominent focus on modeling, algorithm development, or computational efficiency. Although interesting, the resulting systems provide adhoc evaluations (if any) and therefore are far from being ready for clinical deployments. As Engelrecht et al. [13] comment, evaluations of a decision support system should include verification, validation, and impact assessments at individual and organizational levels. Shortliffe and Davis [33] advocate evaluating a system’s clinical efficacy using real-world cases and settings. Clinicians tend to exhibit a tool-oriented view of technology and therefore are likely to accept a decision support system only if it offers significant utility in their patient care and management [9]. Our evaluations of the proposed diagnosis support system included knowledge base verification, system validation, and clinical efficacy using targeted clinicians and real-world cases.

## 3.4. System-based decision support for LBP diagnosis

Investigations of a system-based approach to support clinicians’ LBP diagnoses have been limited. Although a handful of studies have examined LBP diagnosis through the lens of a single decision outcome [5,16,39], we target decision support for multiple decision outcomes, namely, a nonexclusive, multi-part diagnosis. From previous interviews with therapists and non-participative field observations, we found that therapists would include multiple medical conditions in a preliminary diagnosis (often ranging from 1 to 3). For instance, a patient may be diagnosed with degenerative disc disease and degenerative joint disease concurrently. The particular medical conditions included in a diagnosis may differ in their respective likelihoods, which would require adequate representations of uncertainty. Although prior research has addressed such uncertainty using automated learning techniques in artificial intelligence [e.g., [5,16,39]], efforts that employ a systematic <sup>b</sup>white-box<sup>Q</sup> approach are limited. In our case, explicit modeling and comprehensible (verifiable) reasoning about uncertainty both is desirable and can foster user acceptance and system use.

To support therapists’ LBP diagnoses, we designed, implemented, and clinically evaluated a Web-based decision support system. Compared with those used by previous research, our knowledge representation and reasoning scheme requires significantly fewer probability elicitation requirements from domain experts. In addition, our system development attends to important issues in problem analysis, uncertainty modeling and reasoning, system design, implementation, and evaluation. As a result, the reported system arguably is more complete and clinically ready than were most systems reported previously. Following the suggestions of Engelrecht et al. [13] and Shortliffe and Davis [33], we include in our overall evaluation design knowledge base verification, system validation based on a modified Turing test, and a clinical efficacy assessment using 180 real-world clinical cases collected from multiple, geographically dispersed clinics.

## 4. System design and implementation

The important guiding principles for our system design and implementation are verifiable knowledge, validated system utility and clinical efficacy, and userfriendly interfaces for convenient access and knowledge updates. Our Web-based system enables 24/7 access without temporal or geographic constraints [3]. In addition to assisting clinicians’ diagnosis tasks, the system supports self-service by patients, with or without a clinician’s assistance. We next provide details of our system architecture, knowledge acquisition and representation, and inference design.

## 4.1. System architecture design

As shown in Fig. 2, our system architecture consists of a knowledge base, an inference engine, a case repository, and two Web-based interfaces for system access and knowledge updates. The knowledge base comprises a total of 140 rules and uses a modified certainty factor scheme designed to alleviate the burdensome expert probability estimation requirements. The rules were solicited from two highly experienced physical therapists and are stored in a relational database implemented using MySQL. Our inference engine, implemented with ANSI standard Java 2, supports multi-part diagnoses with an algorithm built on a consensus model for combining the likelihood of individual rules. The algorithm is effective for addressing the exclusive negation characteristic of an LBP diagnosis. For each patient case, the system recommends a diagnosis that consists of one or more parts that have varying certainty values, based on patient information and clinical evidence provided by the user (clinician or patient) as well as intermediate results from the system’s rule activation. Ultimately, the system-recommended diagnosis includes the medical condition (disease or abnormality) with the highest likelihood or those that exceed a specified likelihood threshold.

The system has two graphic user interfaces. The diagnosis interface allows the user to describe important patient symptoms using non-medical terminology.

![](/api/attachments/GXNKNFBM/fulltext/images/2245c04e50942305d867f8b4c72b5c95660e6fbd0cb42905f56436c9174a9405.jpg)  
Fig. 2. A Web-based decision support system for LBP diagnosis—architecture design.

A patient, with or without a clinician’s assistance, can log on through the Web-based interface to start a selfdiagnosis session. All diagnosis sessions are structured by a sequence of questions presented through Web pages, each of which solicits the patient<sup>T</sup>s response to a specific pain symptom or assessment. Typically, a session includes 13–15 pages, depending on the number of follow-up questions triggered; sample diagnostic question pages appear in Fig. 3. After completing all the questions, the user submits his or her responses to the inference engine, which then generates a diagnosis that includes one or more parts that refer to specific medical conditions, diseases, or abnormalities. A clinician can override a system-recommended diagnosis or any of its part(s). In addition, a clinician can activate the explanatory panel to review how the system’s reasoning process led to a particular diagnosis. Each diagnostic session is stored in the case repository for future reference and analysis, such as clinical training or data mining.

The system also includes a knowledge-update interface that enables the clinician to update the knowledge base directly. Using this graphical interface, the clinician can add, remove, or modify an existing rule in reference to its observation (left-hand side), decision outcome (right-hand side), or certainty level. The support of clinicians’ knowledge updates is essential because they may acquire additional diagnosis knowledge over time. Our system supports such knowledge update by individual clinicians, without requiring their knowing the details of the underlying knowledge representation schema. We implemented both interfaces using Java Server Pages and Java Servlets technology.

The case repository was implemented using a data warehouse. Specifically, we used a star schema, in which the fact table is the session information, and dimensions represent key factors such as patient demographics and symptoms. By <sup>b</sup>slicing and dicing<sup>Q</sup> the data, clinicians may gain insights into potentially useful diagnosis knowledge, including indicators that suggest a particular diagnosis, specific diagnostic patterns by an individual or group of clinicians, or association relationships between demographic variables and particular medical conditions. Implemented in Oracle, our case repository supports data cleansing and preparation, both of which are critical to the use of data mining techniques to extract novel diagnosis knowledge from previous cases.

![](/api/attachments/GXNKNFBM/fulltext/images/6aca74a74a06603a29aaefdbab00a2133aaf9e160634527ec3726eca528da70e.jpg)  
Fig. 3. Sample diagnostic interface based on non-medical terminology and graphs.

## 4.2. Knowledge acquisition

We solicited diagnostic knowledge from two highly experienced physical therapists. One was a visiting therapist from Europe, and the other was a practitioner in the United States. Both experts had extensive clinical training and had practiced for more than 15 years in the LBP diagnosis and treatment area. Our experts also are active leaders in the LBP therapy community and have authored highly regarded books. Using multiple methods, including unstructured and structured interviews, non-participative field observations, and scenario-based case reasoning and analysis, three knowledge engineers worked closely with both experts for six months; i.e., a total of 18 man-months. Through these efforts, we identified a total of 14 common medical conditions (decision outcomes) that cause or are related to LBP<sup>4</sup>, summarize in Table 1.

Table 1  
Listing of decision outcomes included in LBP diagnosis support system

<table><tr><td>Diagnosis category</td><td>Description</td></tr><tr><td>1</td><td>Acute disc-related pain</td></tr><tr><td>2</td><td>Acute disc-related pain with radiculopathy/ myleopathy</td></tr><tr><td>3</td><td>Chronic disc-related pain; e.g., degenerative disc disease or instability</td></tr><tr><td>4</td><td>Chronic disc-related pain with radiculopathy/ myelopathy</td></tr><tr><td>5</td><td>Stenosis/osteoporosis/compression fracture</td></tr><tr><td>6</td><td>Acute facet joint-related pain</td></tr><tr><td>7</td><td>Chronic facet joint-related pain (degenerative joint disease)</td></tr><tr><td>8</td><td>Neuropathy of a peripheral nerve; e.g., sciatic, cluneal, and others</td></tr><tr><td>9</td><td>Sacroiliac joint-related pain and other pelvic ring related conditions</td></tr><tr><td>10</td><td>Hip joint-related pain</td></tr><tr><td>11</td><td>Miscellaneous musculoskeletal pathologies, including muscle/tendon/ligament strains/sprains, busitis, compartment syndromes, fractures and kissing spine</td></tr><tr><td>12</td><td>Non-musculoskeletal internal pathologies, including neoplasms</td></tr><tr><td>13</td><td>Gynecological</td></tr><tr><td>14</td><td>Inappropriate illness behavior</td></tr></table>

Also from the knowledge acquisition process, we identified 15 questions critical to therapists’ LBP diagnosis. As shows in Table 2, these questions can be broadly categorized into patient demographics, current symptoms, clinical history, and follow-up questions specific to gender or the pain description. The domain experts also identified 152 legitimate responses to these questions; that is, each question is associated with an average of 10 plausible responses.

## 4.3. Knowledge representation

Analysis of the therapists’ LBP diagnoses suggested several challenging characteristics. First, a therapist usually combined evidence from the question-and-answer session in some additive fashion. Therefore, a medical condition (i.e., decision outcome) supported by more evidence (i.e., positive responses to multiple questions) was considered more <sup>b</sup>likely<sup>Q</sup> than those supported by less evidence. This finding implies an independent contribution of particular evidence toward the inclusion of a medical condition (decision outcome) in the system’s recommended diagnosis.

Second, therapists often have difficulty estimating uncertainty in their diagnoses. Unlike those participating in the development of MYCIN, who had been calibrated for making estimates of great preciseness (e.g., certainty factor of 0.525) [7]), our domain experts had difficulty assessing or estimating the numerical probability of individual rules, regardless of the different methods the knowledge engineers attempted. Previous research of probability judgments suggests that a domain expert may be more comfortable rendering verbal probability expressions (such as <sup>b</sup>maybe<sup>Q</sup> or <sup>b</sup>possibly<sup>Q</sup>) than providing specific numerical probability estimations [37]. To physical therapists, the notion of certainty may become increasingly natural, meaningful, comprehensible, and consistent with their practices when they can express it using a verbal probability scale rather than a numeric one. Based on our knowledge elicitation results, we defined certainty at three distinct verbal levels: impossible, neutral, and likely. Thus, a sample rule may read as follows:

If observation shows patient age is between 30 and 40 Then recommend diagnosis <sup>b</sup>Chronic Disc Degenerative<sup>Q</sup> with a certainty level of <sup>b</sup>likely<sup>Q</sup>

Table 2  
Listing of question items included in LBP diagnosis support System

<table><tr><td>Category</td><td>Name</td><td>Description</td></tr><tr><td rowspan="2">Demographic</td><td>Gender</td><td>Patient&#x27;s gender</td></tr><tr><td>Age</td><td>Patient&#x27;s age</td></tr><tr><td rowspan="6">Current symptoms</td><td>Pain location</td><td>Anatomic parts where the pain occurs</td></tr><tr><td>Pain pattern</td><td>How the pain changes throughout the day</td></tr><tr><td>Pain feeling</td><td>How the pain is felt</td></tr><tr><td>Pain duration</td><td>How long the patient has had the pain</td></tr><tr><td>Alleviating position</td><td>Positions that relieves or alleviates the pain</td></tr><tr><td>Worsening position</td><td>Positions that aggravates or intensifies the pain</td></tr><tr><td rowspan="5">Clinical history</td><td>Pain start</td><td>Activation of the pain; e.g., sudden on-set or gradually</td></tr><tr><td>Cause of pain</td><td>Whether a trauma has caused the pain and type of trauma</td></tr><tr><td>Pain history</td><td>Number of pain episodes the patient has experienced before</td></tr><tr><td>Facture history</td><td>Type(s) of fracture the patient has had before</td></tr><tr><td>Surgery history</td><td>Type(s) of surgery the patient has had before</td></tr><tr><td rowspan="2">Follow-up questions</td><td>Female related pain (if gender is female)</td><td>Pain patterns that might appear with pregnancy</td></tr><tr><td>Numbness/tingling (if patient feels numbness or tingling)</td><td>Regions where the patient has numbness or tingling</td></tr></table>

P xð Þ is true j m likely rules

Third, therapists often exclude a particular medical condition when they observe evidence that suggests its impossibility, regardless of its support by other evidence. From a modeling perspective, this characteristic is unique and has not been examined by previous research. We therefore designed an intuitive scheme based on the verbal probability estimation method. Structurally, we implemented knowledge using a production-rule format; that is, if response, then decision outcome (i.e., medical condition), with a certainty level expressed in the verbal probability estimation. We stored and maintained the resulting knowledge, a total of 140 diagnosis rules, in a relational database implemented using an Oracle platform.

## 4.4. Knowledge inference

Our knowledge inference is based on a voting scheme in which a rule with a verbal probability of <sup>b</sup>likely<sup>Q</sup> generates one vote in favor of the decision outcome(s) it recommends. A rule with a verbal probability of <sup>b</sup>neutral<sup>Q</sup> has no effect on the voting, whereas a rule with an <sup>b</sup>impossible<sup>Q</sup> verbal probability nullifies all votes the associated decision outcome(s) has received from the other rules. According to this scheme, the votes received by each decision outcome are combined, and those that receive the most vote(s) or exceed a specified threshold are included in the system-generated diagnosis.

Our scheme draws its theoretical premises from consensus-based modeling [29] and therefore differs from the probabilistic summation approach used in previous research [7]. Central to a consensus-based model is the theoretical adequacy of the consensus position jointly established by the voting experts. We represented the LBP diagnosis using a consensus model primarily because each response can partially affect the likelihood of a decision outcome independently. We provide a simple illustration by considering a consensus model that involves only one decision outcome (x) and then derives a decision about whether to accept (i.e., recommend) $x .$ Assume n independent observations $O _ { 1 } , . . . , O _ { n } .$ . For each observation $o _ { i } ,$ there exists a rule $r _ { i }$ in the form of $\therefore  \operatorname { i f } O _ { i } ,$ , then $x ^ { \prime \prime }$ with a verbal probability $p ( r _ { i } )$ , where $p ( r _ { i } ) \in \mathfrak { i }$ {impossible, neutral, likely}. Let $p _ { i }$ be the probability that rule $r _ { i }$ is correct $( 1 \leq i \leq n )$ and $P _ { x }$ be the prior probability that decision outcome x is correct. We further assume the following:

1. If p(r<sub>i</sub>) = impossible, P(x is true $| R ) = 0$ , where R is any set of observations that contains $o _ { i }$ . That is, the presence or absence of particular evidence can rule out a decision outcome completely; and

2. $p _ { i } = ~ p _ { j } = p , ~ \forall ~ 1 \leq i , j \leq n$ , so that the prior probability of each rule being correct is identical. This assumption is reasonable in light of the comprehensive and nondiscriminant nature of therapists’ practices; that is, therapists often diagnose and treat patients suffering from various LBP problems. As a result, the decision rules extracted from their diagnosis knowledge should be comparable in correctness.

Assumption 1 implies that x cannot be true if there exists any observation on the left-hand side of a rule with a certainty level of <sup>b</sup>impossible<sup>Q</sup>. Therefore, we only consider cases associated with rules with <sup>b</sup>neutral<sup>Q</sup> or <sup>b</sup>likely<sup>Q</sup> certainty levels. Assume there are m rules with a certainty level of likely $( m < = n )$ and all other rules are neutral. According to the Bayes theorem, we can derive the following proposition:

Proposition 1. When $p { > } 0 . 5 ,$ , P(x is true | m likely rules ) monotonically increases in m; that is, the more likely rules, the higher the likelihood that x is true.

Proof.

$$
\begin{array}{l} = \frac {P (m \text { likely   rules } \mid x \text { is   true}) ^ {*} P _ {x}}{P (m \text { likely   rules } \mid x \text { is   true}) ^ {*} P _ {x} + P (m \text { likely   rules } \mid x \text { is   false}) ^ {*} (1 - P _ {x})} \\ = \frac {p ^ {m} (1 - p) ^ {n - m} P _ {x}}{p ^ {m} (1 - p) ^ {n - m} P _ {x} + p ^ {n - m} (1 - p) ^ {m} (1 - P _ {x})} \\ = \frac {1}{1 + \left[ \left(\frac {p}{1 - p}\right) ^ {n - 2 m} \cdot \left(\frac {1 - P _ {x}}{P _ {x}}\right) \right]}. \end{array} \tag {1}
$$

The Bayesian probability monotonically increases in m when $p { > } 0 . 5 .$ . Given our domain experts’ extensive clinical experiences, we consider the assumption that $p { > } 0 . 5$ reasonable. For single decision-outcome problems, our voting scheme suggests an increasing likelihood of accepting a diagnosis when it receives more likely votes.

To expand our illustration to multi-decision-outcome diagnosis scenarios, assume that there are l decision outcomes $d _ { I } , \ldots , d _ { l }$ . For each observation $o _ { i } ,$ there are l rules $r _ { i j } ( 1 \leq i \leq n \leq j \leq l )$ in the format <sup>b</sup>if $o _ { i } ,$ , then $d _ { j } ^ { \mathfrak { N } }$ with a verbal probability $p ( r _ { i j } )$ , where $p ( r _ { i j } ) \in \{ \mathrm { i m p o s - }$ {impossible, neutral, likely}. Let $p _ { i j }$ be the probability that $r _ { i j }$ is correct and $P _ { d _ { i } }$ be the prior probability that decision outcome $d _ { j }$ is correct. We continue making the two assumptions from the previous illustration. Likewise, we focus on scenarios that do not contain any impossible rules.

Proposition $2 . \forall j , k , 1 \leq j , k \leq 1$ , for an observation set R, if the following are true:

1. $p { > } 0 . 5 ;$

2. $P _ { d _ { i } } { = } P _ { d _ { k } } ;$ and

3. Based on $R , d _ { j }$ receives $n _ { j }$ votes and $d _ { k }$ receives $n _ { k }$ votes, where $n _ { j } > n _ { k } ;$ then $P ( d _ { j }$ is true| $R ) { > } P ( d _ { k }$ is true| R). That is, from the same set of observations, the diagnoses that receive more votes are more likely to be true.

Proof. Based on Eq. (1),

$$
P \left(d _ {j} \text {   is   true   } \mid R\right) = \frac {1}{1 + \left[ \left(\frac {p}{1 - p}\right) ^ {n - 2 n _ {j}} \cdot \left(\frac {1 - P _ {d _ {j}}}{P _ {d _ {j}}}\right) \right]};
$$

$$
P (d _ {k} \text {   is   true   } | R) = \frac {1}{1 + \left[ \left(\frac {p}{1 - p}\right) ^ {n - 2 n _ {k}} \cdot \left(\frac {1 - P _ {d _ {k}}}{P _ {d _ {k}}}\right) \right]}.\tag{2}
$$

5

Because 8j, $1 \leq j , k \leq l , P _ { d _ { i } } = P _ { d _ { k } }$ and in light of the monotonic characteristic of the function, Proposition 2 is proved. Central to our proposition is the assumption that $P _ { d _ { i } }$ is identical for all $j .$ This assumption holds when each decision outcome has a similar occurrence frequency in all clinical cases (i.e., prior probability of occurrence). Although an exhaustive examination of diagnoses’ respective occurrence rates is prohibitively costly, an analysis of a fairly large set of real-world clinical LBP cases supports the assumption reasonably across the 14 decision outcome categories under investigation. To extend our framework to other clinical diagnosis tasks or non-healthcare applications in which the prior probability of each decision outcome may vary, we must obtain the respective prior probabilities using extant literature or domain experts’ estimations and incorporate them into Eq. (2) to derive the actual posterior probability value for each decision outcome. We describe the extended algorithm as follows:

## 4.4.1. Extended diagnosis algorithm

For an observation set R, if the following are true:

1. $p { > } 0 . 5 ;$

2. $\forall j , 1 \le j , P _ { d _ { i } }$ , the known prior probability for decision outcome $d _ { j }$ is correct; and

3. Based on R, $d _ { j }$ receives $n _ { j }$ votes, then the probability that $d _ { j }$ is actually true $P \big ( \mathrm { \mathrm { } } _ { d _ { j } } \mathrm { i s } \mathrm { \ t r u e } | R \big ) =$ $\begin{array} { r l } {  { \overline { { 1 + [ ( \frac { p } { 1 - p } ) ^ { n - 2 n _ { j } } \cdot ( \frac { 1 - P _ { d _ { j } } } { P _ { d _ { j } } } ) ] } } } \quad } & { { } } \end{array}$

To use the extended algorithm, we must know the values of two parameters: the prior probability of each decision outcome $( P _ { d _ { i } } )$ and the probability that a rule is correct $( p )$ . As we described, we can obtain $P _ { d _ { i } }$ using relevant clinical literature and/or domain experts’ estimations. To obtain $p ,$ , we can examine the experts’ diagnostic performance in previously completed cases and calculate such simple statistics as the number of correctly diagnosed cases divided by total number of cases. Alternatively, we can derive a reasonable estimation for $p$ from a panel of domain experts.

Our approach uses a simplified verbal probability representation scheme and thus requires significantly less estimation efforts from domain experts, even if we take prior probability estimations into account. Nevertheless, the non-exhaustive analysis represents a limitation of our approach and, to some degree, may affect our system’s performance for several decision-outcome categories in the evaluations we discuss in the next section.

In essence, our algorithm shares the same underlying logic as a Bayesian classifier, which uses a multiplicative approach by taking products from all conditional probabilities to derive the probability of a particular decision outcome. The effectiveness of a Bayesian classifier is largely dependent on the accurate estimation of probabilities by domain experts, which is difficult to achieve if the targeted knowledge is complex or highly specialized. By reducing the probability estimation requirements and the subsequent inference using a verbal probability-based voting scheme, our model may be considered an efficient <sup>b</sup>mini-Bayesian<sup>Q</sup> approach, advantageous for rapid developments of prototype systems of satisfactory performance.

## 5. Evaluation design and results

Our evaluations include knowledge base verification, system validation, and clinical efficacy using real-world testing cases. Central to our evaluations are five senior therapists, all clinically active with at least 10 years of experience in LBP diagnosis and treatment. Among them, three practice in a nationwide pain clinic in the United States, and the others practice in Europe. By including therapists who practice in different clinics and regions, we increased the validity and generalizability of our evaluation results. In Table 3, we summarize our evaluation design in terms of focus, method, and metrics.

Table 3  
Evaluation framework — focus, method and metrics

<table><tr><td>Evaluation focus</td><td>Evaluation methods</td><td>Evaluation metrics</td></tr><tr><td>Knowledge base verification</td><td>-Preliminary completeness verification-Face value verification-Completeness verification-Check for developer-induced errors</td><td>•Usefulness•Completeness</td></tr><tr><td>System validation</td><td>Modified Turing test</td><td>•Interpreted system performance benchmarked by experts&#x27; performance</td></tr><tr><td>Clinical efficacy</td><td>Test using 180 real-world clinical cases</td><td>•Recall rate•Precision rate•Accuracy</td></tr></table>

## 5.1. Knowledge base verification and results

Verification refers to <sup>b</sup>building the system right<sup>Q</sup> with a particular focus on its compliance with the defined specifications [21]. Using pertinent medical knowledge, we verified each rule in the knowledge base in terms of its left- and right-hand sides and their pairing (causal or correlational mapping). The important verification criteria included consistency and completeness. Specifically, we examined syntactic or semantic errors that could adversely affect the knowledge base’s consistency and completeness and then corrected them accordingly.

Using a questionnaire, each therapist verified the usefulness and completeness of the rules by examining each rule’s left-hand (i.e., patient responses) and righthand (i.e., decision outcome) sides. According to the overall assessment results, our knowledge base exhibited satisfactory completeness and contained decision variables and decision outcomes essential to therapists LBP diagnoses. Although several individual therapists suggested including a new diagnosis, removing an existing diagnosis, or allowing additional responses to a decision variable, as a group, the therapists discussed these suggestions and collectively recommended keeping the rules intact.

The therapists were then asked to verify each rule at its face value, with particular emphasis on mapping its left- and right-hand sides. When examining a rule, a therapist needed to assess the pairing of its left-and right-hand sides and specify his or her confidence level for that assessment. Although the assessments were individually completed, all the therapists collaboratively reviewed them during panel meetings. Of the 140 rules stored in the knowledge base, a revised certainty level, determined from the confidence value reached by the group, was applied to 8 rules. The results from the face-value verification were satisfactory overall and suggest that the system embraces verified knowledge for therapists’ LBP diagnoses.

Also included in our verification was an assessment of the completeness of the knowledge base with respect to the system’s ability to reach a decision outcome for each case. For each of the 180 real-world clinical cases examined, the system suggested at least one decision outcome. Although not exhaustive, our evaluation used a reasonably large number of clinical cases with considerable diversity. In addition, we assessed potential developer-induced errors that might have occurred when we implemented individual rules in the backend database. Judging by the knowledge representation scheme and the integrity constraints enforced by the relational data model, the knowledge base has no serious syntactic or semantic problems resulting from system development errors.

## 5.2. System validation and results

Validation is about <sup>b</sup>building the right system<sup>Q</sup> by ensuring its performing at a level acceptable to domain experts or targeted users [4,21]. We validated the system using a modified Turing test that involved all five therapists and 20 clinical cases. Turing tests are commonly used to validate knowledge-based systems, demonstrating whether a system exhibits a performance level comparable to that achieved by human experts [41]. In spite of the concerns raised by some researchers, Turing tests are generally considered a valid and effective method for evaluating a system’s performance [15]. Specifically, we designed and conducted a modified Turing test that focused on the system’s utility in LBP diagnoses using 20 previously completed clinical cases randomly selected from a national clinic. Several considerations were crucial in our case selection. First, we included at least one case for each decision outcome that the system could reach. Second, our selection set preserved a similar case distribution, including diagnoses and medical conditions, to that of the underlying case population. Using our sample of 180 clinical cases, we analyzed the distribution of their diagnoses and selected 20 test cases accordingly. Our decision about the number of test cases to include was based on the trade-off between the sample size required for the intended analysis and the likelihood of overwhelming our therapist subjects.

The details of our Turing test are as follows. Let there be n experts $e _ { i } ( 1 < = i < = n )$ and m testing cases $t _ { j } ( 1 < = j < = m )$ in the panel. Let $\mathrm { S o l } _ { i j }$ represent the diagnosis by expert i for case j. We denote our system as $\mathrm { ~ \ " e x p e r t { } ~ } n + 1$ . Our Turing test consists of four phases. In the case-solving phase, each expert (including our system) performed diagnoses on each of the m cases assigned and thus generated a total of $m ^ { * } \left( n + 1 \right)$ diagnoses. In the second phase, we made all diagnoses anonymous by removing the identity of the expert who had rendered the diagnosis, which allowed the other experts to evaluate all the diagnoses recorded for each case blindly. In the third phase, an expert rated each diagnosis. Using a rating r and a certainty factor $c ( r )$ the expert made an explicit assessment of a diagnosis, together with his or her self-reported confidence in the assessment. As a result, expert i produced an $m ^ { * } \left( n + 1 \right)$ rank matrix $r _ { i j k }$ in evaluating the diagnosis by expert $e _ { k }$ for case $t _ { j } ( \mathrm { S o l } _ { k j } ) ; \mathrm { i . e . }$ , for $r _ { i } ( \mathrm { S o l } _ { k j } )$ . We measured r and $c ( r )$ using a seven-point Likert scale, with 1 as <sup>b</sup>not certain/confident at $\mathrm { a l l } ^ { \mathsf { P } }$ and 7 as <sup>b</sup>very confident/ certain.<sup>Q</sup> In the final phase of the Turing test, our system was evaluated and thereby produced a validity measure $\nu ( t _ { j } )$ for each test case. We calculated this validity measure using the average rating of the system-recommended diagnosis (comprising of one or more parts) for a test case by individual review experts, taking into account each expert’s competence and self-reported confidence/certainty. We then rated the global validity of the system v(sys) by averaging its validity score across all the test cases examined.

Using these procedures, we first estimated each expert’s competence. Understandably, experts may not be equally competent for a particular case, and a specific expert may not be equally competent across all cases. Our unit of analysis therefore was the expert’s diagnosis of a particular case. Sources of individual competence estimations included the confidence/certainty level specified by an expert when evaluating a diagnosis by another expert, the consistency of an expert in diagnosing different cases and in rating the diagnoses of other experts, the stability of an expert, and the rating of an expert’s diagnoses by other experts.

Certainty refers to an expert’s certainty in rating other experts’ diagnoses, which demonstrates his or her intentional reflection about a diagnosis. In particular, we denote the certainty of an expert i for case j using Certainty $( e _ { i } , ~ t _ { j } )$ , which is calculated as his or her average certainty ratings $( c ( r ) )$ for all other experts’ diagnoses of case $j ,$ including that made by the system:

$$
\text { Certainty } \left(e _ {i}, t _ {j}\right) = \sum_ {k = 1, k \neq i} ^ {n + 1} c _ {i j k} / n.\tag{3}
$$

Consistency refers to an expert’s consistency in making diagnoses for different cases, as well as in the rating of a diagnosis he or she rendered. In our evaluation, consistency is calculated by the rating an expert, specified for his or her own diagnoses.

$$
\text { Consistency } \left(e _ {i}, t _ {j} = r _ {i j i}\right)\tag{4}
$$

Stability measures the certainty of an expert’s rating of his or her own diagnoses. Whereas consistency shows an expert’s self-assessed performance, stability reveals his or her confidence in his or her judgment. Together, these metrics measure the unintentional reflection of an expert on his or her own diagnoses. Stability is calculated as follows.

$$
\text { Stability } (e _ {i}, t _ {j}) = c _ {i j i}.\tag{5}
$$

The Performance of an expert is measured by the average rating received from other experts (including the system), weighted by their respective certainty.

$$
\text { Performance } \left(e _ {i}, t _ {j}\right) = \frac {\sum_ {k = 1 , k \neq i} ^ {n} \left(c _ {k j i} ^ {*} r _ {k j i}\right)}{\sum_ {k = 1 , k \neq i} ^ {n} c _ {k j i}}.\tag{6}
$$

Central to our competence estimation is intentional reflection measured by certainty, unintentional reflection measured by consistency and stability, and external competence measured by performance. Intentional reflection reveals an expert’s capability to evaluate others’ performance, whereas unintentional reflection demonstrates the ability to evaluate his or her own work. In contrast, external competence conveys an expert’s performance as judged by others. We assume these three measurements are highly comparable in significance and thus assign an equal weight to each source for our estimation of competence.

$$
\begin{array}{l} \text { Competence } (e _ {i}, t _ {j}) = 1 / 3 \big [ \text { Certainty } (e _ {i}, t _ {j}) \\ \qquad + 1 / 2 \big (\text { Consistency } (e _ {i}, t _ {j}) \\ \qquad + \text { Stability } (e _ {i}, t _ {j}) \big) \\ \qquad + \text { Performance } (e _ {i}, t _ {j}) \big ]. \end{array}\tag{7}
$$

Using these metrics described, we calculate the average rating of the system’s diagnoses by the human experts, weighted by their estimated competence and certainty levels.

$$
V _ {\text { sys }} (t j) = \frac {\sum_ {i = 1} ^ {n} \left(\text { Competence } (e _ {i} , t _ {j}) ^ {*} c _ {i j (n + 1)} ^ {*} r _ {i j (n + 1)}\right)}{\sum_ {i = 1} ^ {n} \text { Competence } (e _ {i} , t _ {j}) ^ {*} c _ {i j i (n + 1)}}.\tag{8}
$$

Thus, we estimate the overall system validity by averaging the validity score across cases.

$$
V _ {\text { sys }} = \sum_ {j = 1} ^ {m} V _ {\text { sys }} (t _ {j}) / m.\tag{9}
$$

To facilitate interpretation, we examined the rating and confidence/certainty scores using normalized scores rather than their original values. We divided the rating or confidence/certainty score by seven because both were based on seven-point Likert scales. Hence, $V _ { \mathrm { s y s } }$ is bound between 0 and 1, inclusively.

Consistent with the discussion of Knauf et al. [22], we consider the use of a single $V _ { \mathrm { s y s } }$ insufficient to reflect the system’s performance accurately. To draw conclusive evaluation results, we compare the system’s performance with the performance of the domain experts. Thus, we modified the approach of Knauf et al. [22] and introduced $V _ { \mathrm { e x p } } ,$ defined as follows.

$$
V _ {\exp} \left(t _ {j}\right) _ {i} = \frac {\sum_ {k = 1 , k \neq i} ^ {n} \left(\text { Competence } \left(e _ {k} , t _ {j}\right) ^ {*} c _ {k j i} * r _ {k j i}\right)}{\sum_ {k = 1 , k \neq i} ^ {n} \text { Competence } \left(e _ {k} , t _ {j}\right) ^ {*} c _ {k j i}}.\tag{10}
$$

$V _ { \mathrm { e x p } } \left( t _ { j } \right) _ { i }$ reflects expert $i \ ' \mathrm { s }$ performance for case j as evaluated by his or her peers. Expert i’s overall performance can be then calculated as follows.

$$
V _ {\mathrm{exp} i} = \sum_ {j = 1} ^ {m} v _ {\exp (t _ {j}) i} / m.\tag{11}
$$

Using the performances of the system and the individual experts, we performed a one-way analysis of variance (ANOVA) to test for significant differences. We summarize our results in Table 4 which include the average performances of the system and each of the five experts in each test case. At the 95% significance level, our system performs at a level comparable to that achieved by the domain experts, thus validating the system’s performance with respect to human experts’.

## 5.3. Clinical efficacy evaluation and results

After validating the system’s clinical utility with respect to domain experts’ expectations, we proceeded to assess the system’s clinical efficacy using 180 realworld cases randomly collected from a nationwide clinic in the United States. Two highly experienced therapists examined each case before we included it in our clinical efficacy evaluation; one had not been involved in our system development, whereas the other was an active participant. Each therapist reviewed the diagnosis provided for a test case and supplemented it with his or her diagnosis if necessary. Together, the experts reviewed, discussed, and consolidated their individual assessments to produce a <sup>b</sup>gold standard<sup>Q</sup> diagnosis for each test case. We used the resulting diagnoses to approximate <sup>b</sup>adequate diagnoses,<sup>Q</sup> against which our system’s clinical efficacy was evaluated.

Table 4  
Comparative analysis of performance — proposed system versus human experts

<table><tr><td>Testing case</td><td>System</td><td>Expert 1</td><td>Expert 2</td><td>Expert 3</td><td>Expert 4</td><td>Expert 5</td></tr><tr><td>1</td><td>0.77</td><td>0.72</td><td>0.93</td><td>0.97</td><td>0.93</td><td>0.97</td></tr><tr><td>2</td><td>0.87</td><td>0.74</td><td>0.63</td><td>0.72</td><td>0.32</td><td>0.22</td></tr><tr><td>3</td><td>0.81</td><td>0.74</td><td>0.79</td><td>0.74</td><td>0.56</td><td>0.43</td></tr><tr><td>4</td><td>0.63</td><td>0.64</td><td>0.83</td><td>0.88</td><td>0.82</td><td>0.79</td></tr><tr><td>5</td><td>0.62</td><td>0.72</td><td>0.70</td><td>0.71</td><td>0.74</td><td>0.71</td></tr><tr><td>6</td><td>0.39</td><td>0.76</td><td>0.71</td><td>0.79</td><td>0.69</td><td>0.55</td></tr><tr><td>7</td><td>0.72</td><td>0.55</td><td>0.44</td><td>0.44</td><td>0.62</td><td>0.61</td></tr><tr><td>8</td><td>0.40</td><td>0.68</td><td>0.53</td><td>0.73</td><td>0.53</td><td>0.69</td></tr><tr><td>9</td><td>0.84</td><td>0.93</td><td>0.93</td><td>0.93</td><td>0.89</td><td>0.90</td></tr><tr><td>10</td><td>0.82</td><td>0.81</td><td>0.81</td><td>0.86</td><td>0.53</td><td>0.76</td></tr><tr><td>11</td><td>0.83</td><td>0.81</td><td>0.85</td><td>0.28</td><td>0.74</td><td>0.41</td></tr><tr><td>12</td><td>0.48</td><td>0.63</td><td>0.67</td><td>0.77</td><td>0.78</td><td>0.39</td></tr><tr><td>13</td><td>0.50</td><td>0.62</td><td>0.48</td><td>0.67</td><td>0.61</td><td>0.62</td></tr><tr><td>14</td><td>0.86</td><td>0.80</td><td>0.83</td><td>0.83</td><td>0.79</td><td>0.86</td></tr><tr><td>15</td><td>0.70</td><td>0.90</td><td>0.90</td><td>0.72</td><td>0.86</td><td>0.84</td></tr><tr><td>16</td><td>0.49</td><td>0.41</td><td>0.66</td><td>0.52</td><td>0.63</td><td>0.62</td></tr><tr><td>17</td><td>0.92</td><td>0.80</td><td>0.80</td><td>0.94</td><td>0.90</td><td>0.90</td></tr><tr><td>18</td><td>0.86</td><td>0.62</td><td>0.64</td><td>0.49</td><td>0.86</td><td>0.86</td></tr><tr><td>19</td><td>0.75</td><td>0.60</td><td>0.70</td><td>0.49</td><td>0.50</td><td>0.55</td></tr><tr><td>20</td><td>0.63</td><td>0.63</td><td>0.43</td><td>0.56</td><td>0.65</td><td>0.58</td></tr><tr><td>Overall Performance</td><td>0.69</td><td>0.71</td><td>0.71</td><td>0.70</td><td>0.70</td><td>0.66</td></tr></table>

We used three measurements in our efficacy evaluation: recall, precision, and accuracy. Recall rate refers to the portion of a gold standard diagnosis (which may consist of multiple parts) that has been correctly recommended by the system. As defined here, recall rate measures the system’s power and particularly emphasizes false negatives. Precision rate measures the system’s efficiency and highlights false positives. Specifically, precision rate is defined as the portion of a diagnosis reached by the system that is actually included in the corresponding gold standard diagnosis. Clinical definitions of the recall and precision rates are as follows.

For a LBP patient, assume that a therapist reaches a diagnosis that consists of $D _ { T } ,$ whereas the decision support system recommends a diagnosis that consists of $D _ { M }$

$$
\text { Precision } = \left| D _ {T} \cap D _ {M} \right| / \left| D _ {M} \right|\tag{12}
$$

$$
\text { Recall } = | D _ {T} \cap D _ {M} | / | D _ {T} |.\tag{13}
$$

For example, assume a therapist reaches a threepart (preliminary) diagnosis for a patient, and two parts exactly match the two-part diagnosis by the system. In this case, the recall rate is 66.6%, and the precision rate is 100%. In addition, we examine the system’s accuracy using the principal diagnosis, which provides system performance assessments for those scenarios in which the system-recommended diagnosis has only one medical condition, disease or abnormality (i.e., principal diagnosis). The results from our previous field observations and interviews with therapists suggest that some therapists prefer pursuing the principal diagnosis first by identifying the particular medical condition in which they feel most confident. To these clinicians, principal diagnosis is more important or relevant than are others. We took a dichotomous approach in which we assign 100% accuracy if the therapist’s principal diagnosis is captured by the system’s recommendation and 0% accuracy otherwise.

As summarized in Table 5, our system averaged 75.82% for recall, 64.56% for precision, and 73.08% for accuracy. These results suggest that our system exhibits reasonably satisfactory efficacy, particularly in light of the low likelihood that LBP patients will receive adequate diagnoses clinically [19]. Analysis shows that our test cases include an instance of acute facet joint-related pain (i.e., decision outcome category 6) and one case for gynecological (i.e., decision outcome category 13). Infrequent occurrences in clinical settings, these cases might have been challenging diagnostically, which in turn indicates the need for further assessments of the diagnosis knowledge for such LBP problems. The system’s performance in the acute disease categories (e.g., decision outcome categories 1 and 2) also suggests a need for further examination of the assumption that different LBP categories have comparable clinical occurrence rates. When we remove those cases pertinent to decision outcome categories 1 and 2, our system averages 82.67% for recall, 69.33% for precision, and 77.33% for accuracy. According to Eq. (2), our algorithm has a tendency to favor diagnoses with high prior probabilities. That is, a diagnosis with a high prior probability has a higher posterior probability for being true, even though it may receive the same number of votes as other diagnoses. Our comparative analysis of the system’s performance for chronic (e.g., decision outcome categories 3, 4, and 7) and acute (i.e., decision outcome categories 1 and 2) LBP problems suggests that chronic problems might have a higher prior probability than acute ones and thus are likely to yield favorable system performance. Results from an interview with a senior therapist support this speculation. The differential performance also may be attributed partially to potential selection bias; participating therapists may be more experienced in diagnosing chronic LBP problems than acute LBP problems. Therefore, $p _ { i j }$ may not be constant across different diagnosis categories. Refined knowledge representation and reasoning approaches are needed to examine these plausible speculations further.

Table 5  
Summary of clinical efficacy evaluation results

<table><tr><td>Diagnosis category</td><td>Testing cases</td><td>Distribution of testing cases (cumulative)</td><td>Precision (%)</td><td>Recall (%)</td><td>Accuracy (%)</td></tr><tr><td>1</td><td>16</td><td>8.79</td><td>46.88</td><td>46.88</td><td>56.25</td></tr><tr><td>2</td><td>16</td><td>8.79</td><td>37.50</td><td>40.62</td><td>50.00</td></tr><tr><td>3</td><td>46</td><td>25.27</td><td>74.47</td><td>86.17</td><td>89.36</td></tr><tr><td>4</td><td>45</td><td>24.73</td><td>64.44</td><td>81.11</td><td>62.22</td></tr><tr><td>5</td><td>10</td><td>5.49</td><td>60.00</td><td>80.00</td><td>60.00</td></tr><tr><td>6</td><td>1</td><td>0.55</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>7</td><td>3</td><td>1.65</td><td>66.67</td><td>100.00</td><td>100.00</td></tr><tr><td>8</td><td>3</td><td>1.65</td><td>33.33</td><td>66.67</td><td>33.33</td></tr><tr><td>9</td><td>11</td><td>6.04</td><td>72.72</td><td>90.91</td><td>90.91</td></tr><tr><td>10</td><td>13</td><td>7.14</td><td>76.92</td><td>73.08</td><td>92.31</td></tr><tr><td>11</td><td>14</td><td>7.69</td><td>82.14</td><td>92.86</td><td>92.86</td></tr><tr><td>12</td><td>3</td><td>1.65</td><td>50.00</td><td>50.00</td><td>33.33</td></tr><tr><td>13</td><td>1</td><td>0.55</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>14</td><td>0</td><td>0.00</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Overall</td><td>182</td><td>100.00</td><td>64.56</td><td>75.82</td><td>73.08</td></tr><tr><td>Total Excluded Category 6 and 13</td><td>180</td><td>98.90</td><td>65.28</td><td>76.67</td><td>73.89</td></tr></table>

## 6. Conclusion

Motivated by the need for an effective, systembased approach to support clinicians’ diagnoses of LBP, we designed, implemented, and evaluated a web-based decision support system. Our system design addresses the challenging characteristics of LBP diagnosis using an intuitive, easy-to-use framework for representing and reasoning the uncertainty associated with nonexclusive, multi-part diagnosis. Our system evaluation attends to knowledge base verification, system validation, and clinical efficacy and is more systematic and thorough than those reported by most prior research. According to the evaluation results based on multiple performance metrics, our system embraces important and verifiable diagnosis knowledge, is capable of performing at a level comparable to domain experts, and exhibits encouraging clinical efficacy.

The current research has made several contributions to decision support systems research. We proposed an intuitive framework to represent and reason under uncertainty in diagnosis tasks that simultaneously involve multiple decision outcomes. Our framework is based on verbal probability estimation and draws its theoretical premises from a consensus-based model for combining simultaneous multiple decisions. In addition, we illustrated a systematic approach for evaluating a clinical diagnosis support system and use multiple performance metrics to respond to evaluation requirements for knowledge base verification, system validity, and clinical efficacy. We also make contributions toward improving current LBP diagnosis practices by developing a clinically viable system that supports therapists’ LBP patient management.

Several areas deserve our continued research attention. First, we need to examine and reconcile the system’s differential effectiveness observed across different LBP diagnosis categories. By scrutinizing the source of inconsistent performance, we can further enhance the system’s validity and efficacy and, at the same time, re-examine our assumption about the comparable prior probabilities of different diagnosis categories, which will provide insight into the plausible boundaries of the proposed framework for uncertainty representation and reasoning. In either case, further refinements to the proposed framework should be analyzed and developed.

Second, although our system is capable of recommending multiple, non-exclusive decision outcomes simultaneously, it does not explicitly examine the issue of possible recommendation of conflicting decision outcomes. When all rules are captured and correctly weighted, in theory we should not encounter such conflicts. However, it is difficult to prove that we have captured all the targeted knowledge; thus, we must develop an effective measure to prevent the system from recommending conflicting diagnoses. The reported system prevents conflicting input information by creating a separate decision outcome category, namely <sup>b</sup>inappropriate illness behavior<sup>Q</sup>. When conflicting symptoms are provided by the user, a rule for generating the <sup>b</sup>inappropriate illness behavior<sup>Q</sup> decision outcome is then activated. However, compare to conflicting input information, the prevention of conflicting outcomes is more difficult and warrants further investigation.

Third, we need to expand our system evaluations to include additional clinicians and clinical cases. While encouraging, our evaluation results were obtained from selected therapists and cases. For increased clinical validity and generalizability, we should examine the system’s validity and efficacy further in different clinical settings. Particularly desirable would be an evaluation of the system with different groups of clinicians (including physicians and pain specialists) who practice in other institutions or clinics.

In addition, the current research investigates only a rule-based approach to supporting clinicians’ LBP diagnoses. This approach has been challenged for its shallow reasoning and can be hindered by ineffective extractions of the targeted knowledge from domain experts. Although it allows for knowledge updates by individual clinicians, our system needs to expand its knowledge replenishment support. A clinician’s diagnosis knowledge is likely to accumulate over time, making the system’s knowledge replenishment support important. In this aspect, approaches based on modelbased reasoning, machine learning, or data mining are promising. Because of their capability for addressing requirements pertinent to uncertainty and multiple decision outcomes, machine learning and data mining may be preferable to model-based reasoning. From a knowledge-quality perspective, such automated approaches enable the desirable integration or fusion of knowledge from multiple sources extracted by different methods. For example, the knowledge solicited from human experts might complement or anchor the use of data mining techniques for knowledge discovery. In addition, the use of a Bayesian network to support knowledge integration is also appealing. An investigation of a Bayesian network that combines targeted diagnosis knowledge from different sources is currently underway, using the existing knowledge base, inference engine, case repository, and knowledge update module as a basis for a hybrid-decision support system [24].

## References

[1] S.K. Andersen, K.G. Olesen, F.V. Jensen, F. Jensen, HUGIN: a shell for building Bayesian belief universes for expert systems, Proceedings of the Eleventh International Joint Conference on Artificial Intelligence (1989) 1080 – 1085.

[2] E.S. Berner, M.J. Ball, Clinical Decision Support Systems: Theory and Practice, Springer, NY, 1998.

[3] P. Bharati, A. Chaudhury, An empirical investigation of decision-making satisfaction in web-based decision support systems, Decision Support Systems 37 (2) (2004).

[4] G. Biswas, R. Abramczyk, M. Oliff, OASES: an expert system for operations analysis—the system for cause analysis, IEEE

Transactions on Systems, Man, and Cybernetics 17 (2) (1987) 133 – 1125.

[5] D.G. Bounds, P.J. Lloyd, B. Mathew, G. Waddell, A multilayer perception network for the diagnosis of low back pain, Proceedings of IEEE International Conference on Neural Networks 2 (1988) 481–489.

[6] B.G. Buchanan, E.H. Shortliffe, A model of inexact reasoning in medicine, Mathematical Biosciences 23 (1975) 351 – 379.

[7] B.G. Buchanan, E.H. Shortliffe, Rule-Based Expert Systems: The MYCIN Experiments of the Stanford Heuristic Programming Project, Addison-Wesley Publishing, Reading, MA, 1985.

[8] M. Cabrero-Canosa, M. Castro-Pereiro, M. Gran˜ a-Ramos, E. Hernandez-Pereira, V. Moret-Bonillo, M. Martin-Egan˜a, H. Verea-Hernando, An intelligent system for the detection and interpretation of sleep apneas, Expert Systems with Applications 24 (4) (2003) 335– 477.

[9] P. Chau, P.J. Hu, Examining a model for information technology acceptance by individual professionals: an exploratory study, Journal of Management Information Systems 18 (4) (2002) 191 – 229.

[10] Causes of Low Back Pain, available at http://www.back.com/ causes.html.

[11] A.P. Dempster, Upper and lower probabilities induced by a multi-valued mapping, Annals of Mathematical Statistics 38 (1967) 325 – 339.

[12] R.A. Deyo, Reproducibility and accuracy of lumbar spine imaging studies, The Lumbar Spine, Manchester University Press, Manchester, 1986.

[13] R. Engelrecht, A. Rector, W. Moser, Assessment and Evaluation of Information Technologies, IOS Press, Amsterdam, 1995.

[14] J.C.T. Fairbank, J.B. Davies, J. Couper, J. O’Brien, The Owestry low back pain disability questionnaire, Physiotherapy 66 (1980) 271 – 273.

[15] J. Gordon, E. Shortliffe, A method for managing evidential reasoning in a hierarchical hypothesis space, Artificial Intelligence 26 (1985) 323– 357.

[16] J.H. Graham, A. Espinosa, Computer assisted analysis of electromyographic data in diagnosis of low back pain, IEEE International Conference on Systems, Man and Cybernetics 3 (1989) 1118– 1123.

[17] D.E. Heckerman, E.J. Horvitz, B.N. Nathwani, Systems: Part I. The pathfinder project toward normative expert, Methods of Information in Medicine 31 (1992) 90 – 105.

[18] D.W.L. Hukins, R.C. Mulholland, Back Pain, Methods for Clinical Investigation and Assessment, Manchester University Press, Manchester, 1986.

[19] D. Jackson, H. Llewelyn-Phillips, J. Klaber-Moffett, Categorization of low back pain patients using an evidence-based approach, Musculoskeletal Management 2 (1996) 39 – 46.

[20] D. Kahneman, P. Slovic, A. Tversky, Judgment Under Uncertainty: Heuristics and Biases, Cambridge University Press, Cambridge, 1982.

[21] A.C. Kak, K.M. Andress, et al., Hierarchical evidence accumulation in the PSEIKI system and experiments in model-driven mobile robot navigation, Uncertainty in Artificial Intelligence, Elsevier, Amsterdam, 1990.

[22] R. Knauf, A.J. Gonzalez, T. Abel, A framework for validation of rule-based systems, IEEE Transactions on Systems, Man and Cybernetics Part B 32 (3) (2002) 281 – 295.

[23] D.J. Leaper, J.C. Horrocks, J.R. Staniland, F.T. deDombal, Computer assisted diagnosis of abdominal pain using estimates provided by clinicians, British Medical Journal 4 (1972) 350 – 354.

[24] L. Lin, O.R.L. Sheng, P.J. Hu, M. Pirtle, Adaptive medical knowledge management: an integrated rule-based and Bayesian Network approach, Proceeding of the 10th Annual Workshop on Information Technologies and Systems (WITS), 2002.

[25] A.L. Nachemson, Advances in low-back pain, Clinical Orthopedics and Related Research 200 (1985) 266 – 278.

[26] A.L. Nachemson, Editorial comment: lumbar discography— where are we today? Spine 14 (1989) 555– 557.

[27] A.L. Nachemson, The Lumbar Spine, W.B. Saunders Company, 1996.

[28] R.M. Nelson, D.E. Nestor, Atlas of standardized low back tests and measures of the national institute for occupational safety and health, Scandinavian Journal of Work, Environment & Health 14 (1988) 82–84.

[29] D.E. O’Leary, Models of consensus for knowledge acquisition, Proceedings of the 32nd Hawaii International Conference on System Sciences, 1999.

[30] K.W. Przytula, D. Thompson, Construction of Bayesian Networks for diagnostics, IEEE Aerospace Conference Proceedings 5 (2000) 193 – 200.

[31] G. Shafer, A Mathematical Theory of Evidence, Princeton University Press, Princeton, NJ, 1976.

[32] K. Shinomiya, K. Nakao, S. Shindoh, Evaluation of cervical discography in pain origin and provocation, Journal of Spinal Disorders 6 (1993) 422 – 426.

[33] E.H. Shortliffe, R. Davis, Some considerations for the implementation of knowledge-based expert systems, SIGART Newsletter 55 (1975) 9 – 12.

[34] A.E. Smith, C.D. Nugent, S.I. McClean, Evaluation of inherent performance of intelligent medical decision support systems: utilizing neural networks as an example, AI in Medicine 27 (1) (2003) 1 – 27.

[35] W.O. Spitzer, F.E. LeBlanc, M. Dupuis, Scientific approach to the assessment and management of activity-related spinal disorders, Spine 12 (1987) 9 – 59.

[36] M. Suojanen, S. Andreassen, K.G. Olesen, A method for diagnosing multiple diseases in MUNIN, IEEE Transactions on Biomedical Engineering 48 (5) (2001) 522– 532.

[37] L.C. van der Gaag, S. Renooij, C.L.M. Witteman, B.M.P. Aleman, B.G. Taal, Probabilities for a probabilistic network: a case study in oesophageal cancer, A.I. in Medicine 25 (2) (2002) 123– 148.

[38] M.L. Vaughn, S.J. Cavill, S.J. Taylor, M.A. Foy, A.J.B. Fogg, Interpretation and knowledge discovery from a MLP Network that performs low back pain classification, IEEE Colloquium on Knowledge Discovery and Data Mining (1998) 2/1 – 2/4.

[39] M.L. Vaughn, S.J. Cavill, S.J. Taylor, M.A. Foy, A.J.B. Fogg, Using direct explanations to validate a multi-layer perception network that classifies low back pain patients, Proceedings of 6th International Conference on Neural Information Processing 2 (1999) 692–699.

[40] G. Waddell, A new clinical model for the treatment of low back pain, Spine 12 (7) (1987) 632 – 644.

[41] S. Walczak, W.E. Pofahl, R.J. Scorpio, A decision support tool for allocating hospital bed resources and determining required acuity of care, Decision Support Systems 34 (4) (2003) 445–456.

[42] L.A. Zadeh, The role of fuzzy logic in the management of uncertainty in expert systems, Fuzzy Sets and Systems 11 (1983) 199–227.

Lin Lin is an Assistant Professor at the School of Business and Economics, Lehigh University. He has a Ph.D. in Management Information Systems from the University of Arizona. His current research interests include health-care information systems and management, electronic commerce, knowledge management and data mining algorithm development.

Paul J. Hu is an Associate Professor and David Eccles Faculty Fellow at the David Eccles School of Business, the University of Utah. He has a Ph.D. in Management Information Systems from the University of Arizona. His current research interests include health-care information systems and management, technology implementation management, electronic commerce, digital government, human–computer interaction, and knowledge management. Hu has published papers in Decision Support Systems; Journal of Management Information Systems; Decision Sciences; Communications of the ACM; IEEE Transactions on Systems, Man and Cybernetics; IEEE Transactions on Information Technology in Biomedicine; IEEE Transactions on Engineering Management; IEEE Intelligent Systems; IEEE Software; Journal of the American Society for Information Science and Technology; Social Science Computer Review; European Journal of Information Systems; Information and Management, Journal of Electronic Commerce Research; Journal of Organizational Computing and Electronic Commerce; and Journal of Telemedicine and Telecare.

Olivia R. Liu Sheng is Presidential Professor and Emma Eccles Jones Presidential Chair of Information Systems at the David Eccles School of Business, University of Utah. She also directs a Utah Center of Excellence — the Global Knowledge Management Center (http://gkmc.utah.edu) to seek commercialization of knowledge management technologies. Her research focuses on data mining and optimization techniques for portal management, emetrics and customer analysis, customer profiling, personalization, recommendation, fraud/intrusion detection, bio-medical, digital government, risk management, telemedicine, telework and distributed learning applications. Her research has received funding from various Utah State agencies, Wasatch Advisors, U.S. Army, NSF, IBM, Tivoli, Toshiba Corp., Sun Microsystems, Hong Kong Research Grants Council, Asia Productivity Organization, SAP University Alliance, and Bureau of Land Management.

Dr. Sheng received a B.S. degree from the National Chiao Tung University in Taiwan, ROC and a Master’s degree and Ph.D. degree in Computers and Information Systems from the University of Rochester. She joined the faculty of Management Information Systems at the University of Arizona in 1985 and was the Department Head from 1997 to 2002. Dr. Sheng was visiting faculty at the Hong Kong University of Science and Technology, Tokyo Institute of Technology, and Shanghai JaioTung University. She has published widely in such journals as Management Science, ACM Transactions On Information Systems, ACM Transactions on Internet Technology, INFORMS Journal on Computing, Communications of ACM, IEEE Transactions on Man, Machine and Cybernetics, IEEE Transactions on Biomedical Computing, and IEEE Transactions on Engineering Management.
