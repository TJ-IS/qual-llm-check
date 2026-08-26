---
otero_id: 15336
otero_key: "EFD22Q5P"
title: "Identifying RFID-embedded objects in pervasive healthcare applications"
authors: "Yu-Ju Tu; Wei Zhou; Selwyn Piramuthu"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.10.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Identifying RFID-embedded objects in pervasive healthcare applications

Yu-Ju Tu <sup>a</sup>, Wei Zhou <sup>b</sup>, Selwyn Piramuthu <sup>b,</sup>⁎

<sup>a</sup> Information Systems, University of Illinois at Urbana-Champaign, Champaign, IL 61820, USA

<sup>b</sup> Information Systems and Operations Management, University of Florida, 351 Stuzin Hall, Gainesville, FL 32611, USA

## a r t i c l e i n f o

Article history: Received 14 February 2008 Received in revised form 6 October 2008 Accepted 20 October 2008 Available online 31 October 2008

Keywords: RFID Pervasive healthcare Read rate False reads

## a b s t r a c t

The organization and delivery of pervasive healthcare have bene<sup>fi</sup>ted much from advances in wireless systems. While wireless systems and their components have certainly enhanced the quality of pervasive healthcare administered in remote locations, their potential in other areas of healthcare cannot be underestimated. We consider Radio Frequency Identi<sup>fi</sup>cation (RFID) tags, which are increasingly being used in pervasive healthcare applications. Speci<sup>fi</sup>cally, we study the dynamics of locating and identifying the presence of a tag in such systems. Although a tag may be present, it may not necessarily be visible to the tag reader due to various constraints or reasons. We propose and illustrate several algorithms for locating the presence of RFID tagged objects in the <sup>fi</sup>eld of the reader and study their dynamics as well as their strengths and bene<sup>fi</sup>ts. Our results indicate that the location accuracy of RFID tag readers can be improved through appropriate data collection as well as algorithms used for data inference.

© 2008 Elsevier B.V. All rights reserved

## 1. Introduction

The primary goal of pervasive healthcare is to be able to deliver necessary quality healthcare service anytime to anyone regardless of location and other constraints. Improvements in technology have enabled the feasibility of this vision, primarily based on physical constraints, even though the actual practice lags much behind what can and should be achieved. A key player in systems facilitating pervasive healthcare is wireless technology. The role played by wireless technology in pervasive healthcare spans a wide range from basic telecommunication to identi<sup>fi</sup>cation and tracking of mobile objects. Sensors and actuators are commonly used to measure ambient conditions and then react to such conditions through intelligent information systems by appropriately instantiating necessary components. Pervasive healthcare necessarily involves the use of multiple layers of intelligent information systems technology that work together synergistically to deliver results in a seamless fashion.

The idea of incorporating intelligent information systems in the healthcare domain is not new [17]. Although the terminology used is somewhat different, the underlying principle in most of these intelligent information systems are rather similar to the extent that they all utilize knowledge in some form to enable decision making in the healthcare environment. Commonly used terms for systems used for decision support in this environment include Clinical Decision Support Systems (CDSS), Intelligent Decision Support Systems (IDSS),

Healthcare Information Systems (HIS), among others. CDSS, IDSS, HIS, etc. all represent similar systems where the terminology are interchangeably used, and are therefore considered to be the same for purposes of this paper. CDSS are commonly used to aid in medical prescription, clinical laboratories, clinical surveillance, clinical education, and intensive care settings, among others. Frost & Sullivan (http://www.healthcare.frost.com) estimates that revenues for Clinical Decision Support Systems market in Europe would reach \$430.7 million in 2012. While intelligent decision support systems have successfully been utilized in healthcare settings, some common reasons cited for unsuccessful scenarios generally involve their use in solving problems that were not considered to be an issue or imposing poor human interface design, reluctance or computer illiteracy of some healthcare workers, restraining or signi<sup>fi</sup>cantly modifying the overall work<sup>fl</sup>ow in such a setting.

Intelligent Healthcare Information Systems (HIS) have been used to critique therapy; check for drug interactions, dosage errors, or allergy to improve the quality of clinical decisions; build and utilize electronic patient record system; and improve compliance with clinical pathways and guidelines. Therapy critiquing works by looking for inconsistencies, errors, or omissions in an existing treatment plan. During physician order entry, such a system can critique the combination of patient's condition and treatment plan. For example, when a clinician enters an order for blood transfusion to a patient with haemoglobin level above the transfusion threshold, the system can prompt the clinician to justify this order such as the presence of active bleeding [21]. Order entry and results reporting systems with embedded Decision Support Systems have been shown to increase compliance with recommended clinical pathways and guidelines and reduce rates of inappropriate diagnostic tests [11].

Potential bene<sup>fi</sup>ts that are associated with intelligent healthcare information systems include improved patient safety through reduced medication errors and adverse events, improved medication/test ordering, improved quality of care, and improved ef<sup>fi</sup>ciency in healthcare delivery by reducing costs related to theft and shrinkage. Moreover, electronic prescribing systems have been shown to be effective in reducing errors. Given the sheer complexity of the druguse process and the multitude of potential failure points, computerized order-entry and drug management systems are promising tools for decreasing medication errors, preventing ADEs (Adverse Drug Events), and improving drug use [6].

Clinical Decision Support System has been promoted as an enabling technology that transforms existing healthcare systems [7]. A growing body of evidence indicates that such systems may decrease error rates and improve therapy, thereby improving outcomes including survival, the length of time patients spend in dangerous conditions, hospital length of stay, and cost. After studying their dynamics in terms of health and bene<sup>fi</sup>ts, Bates et al. [5] conclude that appropriate use of information technology in healthcare could result in process simpli<sup>fi</sup>cation and substantial improvement in patient safety. Although injuries associated with errors in healthcare are important, costs of inef<sup>fi</sup>ciencies related to errors that do not directly or indirectly result in injury are also important. For example, “missed dose” medication errors occur when a required medication dose is not available for administering on time, and when this delay exceeds a few hours the dose is generally not given in order to prevent interference with a subsequent dose. To alleviate such problems nurses spend a great deal of time tracking down appropriate medications so that they are delivered to the patients on time. The costs associated with such events are generally not accounted for since they are harder to assess.

Considering support tools for clinical decision making, Garg et al. [10] reviewed several studies involving systems with human interaction and concluded that systems where users were automatically prompted to use the system had better performance compared with cases where users were required to actively initiate the system. They also found that compared to manual initiation, automatic prompting by these intelligent decision support systems may result in smooth integration with practitioner work<sup>fl</sup>ow as well as provide better opportunities to correct inadvertent de<sup>fi</sup>ciencies in care.

Bates [5] recommends incorporating barcodes on medications, blood, devices, and patients to reduce errors. In the U.S., it is estimated that over 770,000 people are injured or die each year in hospitals as a result of adverse drug effects [15], of which the greatest proportion (56%) occur at the drug ordering stage. Added to this is the fact that most laboratory systems do not communicate directly with pharmacy systems. These intermittent gaps in communication among healthcare systems result in simple misunderstandings to utter chaos when different parts of the systems are not in sync.

From the above discussion, it is clear that healthcare information systems where communication among its sub-components occurs seamlessly are essential for pervasive healthcare. It is also essential to automatically capture as much data as possible and let the computer do the checking, relating, and associated book-keeping work thus releasing healthcare personnel to do their primary work in delivering quality healthcare in a pervasive environment. Hospital employees make decisions utilizing available resources including patient records and necessary specialized equipment. Healthcare information systems that have discontinuities, where their sub-components are not seamlessly integrated with one another, are not completely reliable in providing error-free and timely necessary information for the decision makers. It is therefore critical for healthcare information systems to be current in being able to provide patient records and relevant reference material in a pervasive computing environment.

Pervasive healthcare is, by its very nature, multi-faceted and requires appropriate enabling technologies depending on location, time, treatment, personnel, and the general healthcare environment.

We consider RFID technology, which is increasingly becoming essential in pervasive healthcare environments [4]. RFID tags are used in scenarios where an object needs to be identi<sup>fi</sup>ed, tracked, or when ambient condition surrounding an object is captured and stored, among others [19]. Clearly, there are several modes of applications where RFID implementations are used, and each mode has its corresponding pros and cons. We consider the data generated as a result of incorporation of RFID tags. Speci<sup>fi</sup>cally, we consider some characteristics of RFID-generated data and how they relate to overall system performance. Although it is generally assumed that data read from RFID tags are highly accurate, variations in accuracy can and do occur due to several reasons. Jeffery et al. [14] claim that over 30% of RFID tag reads are routinely dropped. Although the extent of dropped reads varies across domains and is context-speci<sup>fi</sup>c, <sup>fi</sup>gures in the 60–99% range are not uncommon. We consider this problem, and propose algorithms that can be used to reduce false positive and false negative readings in such applications. It should be noted that we do not consider collisions that occur due to multiple tags simultaneously transmitting signals read by a single reader or when multiple readers are simultaneously trying to bounce off signals on a single tag. We illustrate the performance of the proposed algorithms using an example scenario. The proposed algorithms can generate more accurate tag reads, and can therefore be incorporated in an appropriate healthcare decision support system to improve its overall performance.

The remainder of this paper is organized as follows. We list general characteristics of RFID tags from a healthcare perspective in the next section. We then review and summarize some literature related to data generated by RFID tags in Section 3. We present a few algorithms that can be used to reduce false positives and false negatives, and illustrate their relative performance with examples in Section 4. We conclude with a brief discussion in Section 6.

## 2. RFID tags and healthcare

There are more than 3000 RFID case studies in a wide range of application areas. RFID in healthcare is growing rapidly and is forecast to become a \$2.1 billion global business by 2016. One of the largest volumes of RFID application has been in the healthcare industry, where about 4.5 million tags have been used every year on Diprivan drug syringes by AstraZeneca since 1999.

Asset tracking is a prime candidate for RFID applications. A typical hospital is unable to locate about 15–20% of its assets when needed [12]. One of the major market drivers of RFID applications in the healthcare industry include California's upcoming e-pedigree requirement that takes effect in January 2009. The core of e-pedigree consists of secure documents that record a drug's progression of ownership throughout the supply chain, from point of manufacture to the pharmacy. This helps in preventing counterfeiting, theft, etc. The World Health Organization has estimated that 5–8% of the \$500 billion trade in pharmaceuticals worldwide is counterfeit. Implementation of e-pedigree should help reduce these numbers.

Borriello et al. [8] demonstrate an application system with passive RFID tags that remind users if they mistakenly leave their personal belongings behind. Deterministic rules are used in the RFID application system to verify whether an object that is supposed to be with a person at a given time does indeed exist with that person. This system also has its own language to help users express reminders. For example, reminder (day = tuesday, destination = work, location = home, starttime = 12:00, endtime = 1:00, items = [keys, wallet]). They develop a prototype and implement it to show the feasibility of this system with existing RFID tag technology.

Michael and McCathie [18] study RFID-embedded supply chain applications and evaluate the pros and cons of such a setting vis-à-vis a system with barcodes and conclude that the pros outweigh the cons in the long run to improve supply chain ef<sup>fi</sup>ciency. As bene<sup>fi</sup>cial properties, they list automatic non line of sight scanning, labor reduction due to increased automation, enhanced visibility of supply chain, improved asset tracking and inventory management, item level tracking ability, traceable warranties and targeted product recalls, improved reliability, quality control and regulation, improved utilization of resources, security against product shrinkage, durability, and capacity to hold more information. As concerns, they list software and equipment costs, lack of standards, resistance to cooperation among different layers in the supply chain required to maintain information transparency, interferences that thwart signal transmission between tag and reader, and privacy concerns. Cost and privacy concerns have generally been recognized as major factors in the success of RFID applications [20]. After conducting a Delphi study with four experts, Viehland and Wong [25] conclude that although cost is a major factor, privacy concern is not a major issue at present since most applications do not have item-level RFID tags.

Information from sensors such as RFID tags provide basic context information including the presence of medical staff, devices, instruments and medication in the operating room [1], the coexistence of entities that are required to be simultaneously present together at a given location, among others. Clinical record keeping in high velocity healthcare delivery environments like surgery is a necessary and critical task. It is also a time consuming task that detracts from hands on patient care and contributes to extraordinary labor costs associated with collecting, transcribing, and re-keying records throughout. Fortunately, a majority of these can be automated in a pervasive healthcare environment through sensors, actuators, and intelligent information systems that coordinate and oversee events in these systems.

In any pervasive healthcare environment, there is a need to identify and track human and other assets. This is especially critical in the case of perishable assets that need to be used before they perish. Their inventory needs to be updated to re<sup>fl</sup>ect their status. They also need to be ordered with enough lead time in mind so that there is enough in stock at the right place where and when they are needed. Tracking of objects are especially critical in surgical environments where it is necessary to account for everything that was used during surgery. In such environments, it is paramount to ensure the presence of necessary and appropriate equipment, personnel, and of course patient. RFID tags can be used as an enabling technology in such environments.

Knowledge that a particular medicine was administered at a given time is important than the knowledge that this medicine was in a room. RFID-enabled systems can be used to ensure administration of proper medicine happens when due. In a pervasive healthcare environment, some common RFID data sources include tools, medicine, staff, and patient monitors.

Three main areas bene<sup>fi</sup>t from RFID technology in the healthcare industry: (1) asset management, (2) patient care, and (3) inventory management. Asset management is critical in pervasive healthcare where it is necessary to be able to identify and track mobile objects. Being able to correctly identify a patient is extremely important to be able to appropriately administer the necessary treatment. There have been numerous cases where patients have received wrong medical treatments that were scheduled to be given to other patients because of identi<sup>fi</sup>cation errors. Inventory management reduces out-of-stock situations, billing errors, misplaced articles, theft, and general shrinkage problems.

## 3. Related literature on improving RFID tag identi<sup>fi</sup>cation accuracy

While preserving the arrival sequence of tags, Bai et al. [2] propose means to <sup>fi</sup>lter and clean data streams from RFID applications that contain false (e.g., false positive, false negative) readings and duplicates. False positive readings or noise could be a result of the reader's detection <sup>fi</sup>eld being spread wider than necessary that signals from tags farther than its intended scope are captured. Duplicate readings occur when tags remain in the reader's detection <sup>fi</sup>eld for a longer duration, tags that are simultaneously present in the <sup>fi</sup>eld of multiple readers, or when multiple tags attached to an object are simultaneously scanned. They obtain multiple readings to reduce effects due to false negative and false positive readings. However, this process generates a signi<sup>fi</sup>cant number of duplicate readings, and elimination of duplicates is computationally expensive.

Using sliding time window, Bai et al. [3] propose means to reduce noise in RFID reads. They then eliminate cases with frequency count below a pre-determined threshold to remove duplicate data. They propose lazy de-noising and eager de-noising methods based on when a data point that is determined to be valid is saved in the database, with the former ignoring signal sequence constraints. Choosing the window size involves balancing between being able to identify the presence of a tag and at the same time being able to capture its dynamics (e.g., tag movement through the reader's detection <sup>fi</sup>eld), where the former requires a larger window size while the latter requires a smaller window size. A given window size is not ideal under all circumstances. Window size should be updated periodically depending on the dynamics of the system [14].

Hu et al. [13] propose a bitmap data type and illustrate its bene<sup>fi</sup>cial characteristics using a prototype implemented in Oracle DBMS. They claim that tracking related groups (e.g., based on physical proximity or shared property) of items is more ef<sup>fi</sup>cient than individual items. The bitmap representation thus is used to model a collection of RFID tags. They show that in addition to its loss-less transformation, their bitmap representation results in compact data storage. The bitmap data type translates to expensive incremental modi<sup>fi</sup>cations, and is therefore better suited for applications where updates occur infrequently. Hu et al. [13] propose keeping an item-level table in addition to those with bitmap representation to keep track of modi<sup>fi</sup>cations that occurs in-between updates at the aggregate level.

Most data cleansing approaches for RFID data are done before data are stored in databases. Rao et al. [22] propose deferred data cleansing of data in RFID systems since eager cleansing may not be feasible (e.g., rules and business context for cleansing data may change over time and across applications) nor appropriate (e.g., pharmaceutical e-pedigree tracking that precludes cleansing of data) in all applications. They use the functionalities present in SQL/OLAP for processing sequential data.

To improve RFID tag detection reliability, Agarwal et al. [1] let the reader sample every 2 s. Using experiments, they show that if a tag is detected at least ten times in a 30 second window (i.e., 66.67% of the time), the tag is present. However, if a tag goes undetected for 4 consecutive windows (i.e., 120 s), the tag is assumed to be absent in the <sup>fi</sup>eld of the reader.

Data reliability and ambiguity are two major issues in extraction of information from RFID data. Most existing methods either ignore issues related to data ambiguity and data input error or deterministically clean the data before processing. However, in certain situations, input data errors can lead deterministic approaches to sacri<sup>fi</sup>ce large signi<sup>fi</sup>cant events. Khoussainova et al. [16] use probabilistic method to provide the application with the <sup>fl</sup>exibility to build its own balance between detection and precision rate. Compared to traditional deterministic approaches, they experimentally show better event detection rates with their method.

## 4. Proposed methods

Identifying the presence of RFID tags is not always necessarily as straight-forward as it seems. False positives and false negatives can be a problem in RFID-embedded systems, especially when signal from a given tag is blocked by an impenetrable object (e.g., metal shielding) or when corrupted signal is read. We propose means to reduce false positives and false negatives through a variation of triangulation where we consider the presence/absence of a related tag. An example of this scenario would be where two objects are required to be simultaneously present such as a two medications that belong together in a prescription.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
- Initialize readers $\mathrm{R}_1, \mathrm{R}_2$.
- While there are more tags left to be read
    $r_1 = 1$ if $\mathrm{R}_1$ identifies tag T to be present in its field
    $r_1 = 0$ otherwise
    $r_2 = 1$ if $\mathrm{R}_2$ identifies tag T to be present in its field
    $r_2 = 0$ otherwise
- When $r_1 = 1 \&amp;\&amp; r_2 = 1$, Tag T is confirmed to be present
Otherwise, Tag T is confirmed to be absent
</div>

Fig. 1. Algorithm 1 — the base case.

We consider the case where two readers are simultaneously used to read information from each RFID tag that passes through the system. We assume that the tag of interest T is read twice by each of the two readers within short time duration at each location covered by the pervasive healthcare system. Therefore, we have two reads of each tag. For ease of representation, we consider the two reads of a tag by a reader as if they are two different tags and identify this (physically the same but read at different points in time) tag by T and T′. There are two readers $\left( \mathsf { R } _ { 1 } \right.$ and $\mathsf { R } _ { 2 } )$ in this scenario, and these two readers are assumed to be oriented at different angles with respect to the tagged object. The usage of several readers to reduce the error rate of tag reads is not new (e.g., [9]). This is particularly signi<sup>fi</sup>cant in RFID-tagged systems since the tag may be “visible” to the reader at one orientation but completely “invisible” to the reader in another orientation due to the (partial) presence of objects (e.g., metal shielding) in one orientation but not in the other. In order to compare the algorithms we present, we consider one of them as the base case since it involves minimal processing from the back-end server. We then compare the proposed algorithms against one another. We <sup>fi</sup>rst present the base-case and the proposed modi<sup>fi</sup>ed algorithms below.

## 4.1. Algorithm 1 (the base case)

We use only the <sup>fi</sup>rst of two readings of a tag in this base case algorithm [24] (Fig. 1). The tag (T) is assumed to be present only when both the readers $\left( \mathsf { R } _ { 1 } \right.$ and R ) identify its presence. I.e., when both $\mathsf { R } _ { 1 }$ and $\mathsf { R } _ { 2 }$ identify it as being present during their <sup>fi</sup>rst reading of this tag, tag T is con<sup>fi</sup>rmed to be present. When either R or R or both identify it as being absent, tag T is con<sup>fi</sup>rmed to be absent. Since both the readers identify the tag as being present, there is a very high possibility of it indeed being present since deleterious effects due to noise, etc. in this scenario is assumed to be minimal. We use this as the base case to compare the next three algorithms.

## 4.2. Algorithm 2

We modify Algorithm 1 to re<sup>fi</sup>ne the case where the tag is con-<sup>fi</sup>rmed to be present (Fig. 2). In this case, the tag T is assumed to be present when both the readers (R<sub>1</sub> and $\mathsf { R } _ { 2 } )$ identify its presence just like in the base case. When both the readers $( \mathsf { R } _ { 1 }$ and $\mathsf { R } _ { 2 } )$ identify it to be absent, the tag T is con<sup>fi</sup>rmed to be absent in the <sup>fi</sup>eld of the readers. Unlike the base case, we con<sup>fi</sup>rm the tag T to be present with probability 0.5 when either $\mathsf { R } _ { 1 }$ or $\mathsf { R } _ { 2 }$ identify it as being present. We include this probability since the fact that one of the readers has identi<sup>fi</sup>ed its presence signi<sup>fi</sup>es the possibility that the signal was probably blocked from one of the readers and not the other. We also assume that the probability of a reader identifying the tag's presence correctly when the other reader incorrectly identi<sup>fi</sup>es it as being absent to be 0.5.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
- Initialize readers $\mathrm{R}_1, \mathrm{R}_2$.
- While there are more tags left to be read
    $r_1 = 1$ if $\mathrm{R}_1$ identifies tag T to be present in its field
    $r_1 = 0$ otherwise
    $r_2 = 1$ if $\mathrm{R}_2$ identifies tag T to be present in its field
    $r_2 = 0$ otherwise
- When $r_1 = 1 \&amp;\&amp; r_2 = 1$, tag T is confirmed to be present
When $r_1 = 0 \&amp;\&amp; r_2 = 0$, tag T is confirmed to be absent
When $r_1 = 1$ XOR $r_2 = 1$, tag T is confirmed to be present with probability 0.5
</div>

Fig. 2. Algorithm 2.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
- Initialize readers $R_1$, $R_2$.
- While there are more tags left to be read
    $r_1 = 1$ if $R_1$ identifies tag T to be present in its field
    $r_1 = 0$ otherwise
    $r_2 = 1$ if $R_2$ identifies tag T to be present in its field
    $r_2 = 0$ otherwise
- When $r_1 = 1$ &amp;&amp; $r_2 = 1$, tag T is confirmed to be present
When $r_1 = 0$ &amp;&amp; $r_2 = 0$, tag T is confirmed to be absent
When $r_1 = 1$ XOR $r_2 = 1$,
    $r'_1 = 1$ if $R_1$ identifies tag T' to be present in its field
    $r'_1 = 0$ otherwise
    $r'_2 = 1$ if $R_2$ identifies tag T' to be present in its field
    $r'_2 = 0$ otherwise
When $r'_1 = 1$ &amp;&amp; $r'_2 = 1$, tag T is confirmed to be present
When $r'_1 = 0$ &amp;&amp; $r'_2 = 0$, tag T is confirmed to be absent
Else, tag T is confirmed to be present with probability 1%
</div>

Fig. 3. Algorithm 3.

## 4.3. Algorithm 3

We re<sup>fi</sup>ne the af<sup>fi</sup>rmative case in this algorithm (Fig. 3). We consider two separate reads of the tag within a brief duration of time to more accurately identify the tag's presence. Therefore, we have one tag that is read twice by each reader. In this case, the tag T is assumed to be present when, after the <sup>fi</sup>rst read, both the readers $\left( \mathsf { R } _ { 1 } \right.$ and $\mathsf { R } _ { 2 } )$ identify its presence just like in the base case. When both the readers $\left( \mathsf { R } _ { 1 } \right.$ and $\mathsf { R } _ { 2 } )$ identify it to be absent after the <sup>fi</sup>rst read, the tag T is con<sup>fi</sup>rmed to be absent in the <sup>fi</sup>eld of the readers just like in the base case.

However, when one of the readers identi<sup>fi</sup>es it to be present after the <sup>fi</sup>rst read while the other does not identify its presence, we utilize information from the second readings of this tag (T′) by the readers in determining the presence/absence of the tag T. When both the readers $\left( \mathsf { R } _ { 1 } \right.$ and $\mathsf { R } _ { 2 } )$ identify $\mathrm { T } ^ { \prime }$ to be present (i.e., the tag is identi<sup>fi</sup>ed to be present during the second reading of T by both the readers), we con<sup>fi</sup>rm the tag T to be present. When neither of the readers $\left( \mathsf { R } _ { 1 } \right.$ and $\mathsf { R } _ { 2 } )$ identi<sup>fi</sup>es T to be present during the second read, we con<sup>fi</sup>rm the tag T to be absent as well. When only one of the readers $\left( \mathsf { R } _ { 1 } \right.$ or $\mathsf { R } _ { 2 } )$ identi<sup>fi</sup>es T′ to be present, we con<sup>fi</sup>rm that tag T is present with probability $1 / 8 .$ . This is because during the <sup>fi</sup>rst read the probability of reader $\mathsf { R } _ { 1 }$ con<sup>fi</sup>rming tag $\mathrm { T } ^ { \prime } \boldsymbol { \varsigma }$ presence when reader $\mathsf { R } _ { 2 }$ con<sup>fi</sup>rms its absence and during the second read one of the readers $\left( \mathsf { R } _ { 1 } \right.$ or $\mathsf { R } _ { 2 } )$ con<sup>fi</sup>rms the tag's presence while the other reader con<sup>fi</sup>rms tag's absence is $( 1 / 4 ^ { * } 1 / 2 = ) 1 / 8$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
- Initialize readers $\mathrm{R}_1, \mathrm{R}_2$.
- While there are more tags left to be read
    $r_{11} = 1$ if $R_1$ identifies tag $T_1$ to be present in its field
    $r_{11} = 0$ otherwise
    $r_{21} = 1$ if $R_2$ identifies tag $T_1$ to be present in its field
    $r_{21} = 0$ otherwise
    $r'_{11} = 1$ if R1 identifies tag $T_1$ to be present in its field
    $r'_{11} = 0$ otherwise
    $r'_{21} = 1$ if R2 identifies tag $T_1$ to be present in its field
    $r'_{21} = 0$ otherwise
- When $r_{11} = 1$ &amp;&amp; $r'_{11} = 1$, tag $T_1$ is confirmed to be present
    When $r_{11} = 0$ &amp;&amp; $r'_{11} = 0$, tag $T_1$ is confirmed to be absent
    When $r_{11} = 1$ XOR $r'_{11} = 1$
    When $r_{21} = 1$ &amp;&amp; $r'_{21} = 1$, tag $T_1$ is confirmed to be present
    When $r_{21} = 0$ &amp;&amp; $r'_{21} = 0$, tag $T_1$ is confirmed to be absent
    Otherwise, we consider the second tag ($T_2$).
    $r_{12} = 1$ if $R_1$ identifies tag $T_2$ to be present in its field
    $r_{12} = 0$ otherwise
    $r_{22} = 1$ if $R_2$ identifies tag $T_2$ to be present in its field
    $r_{22} = 0$ otherwise
    $r'_{12} = 1$ if $R_1$ identifies tag $T_2$ to be present in its field
    $r'_{12} = 0$ otherwise
    $r'_{22} = 1$ if $R_2$ identifies tag $T_2$ to be present in its field
    $r'_{22} = 0$ otherwise
    When $r_{12} = 1$ &amp;&amp; $r'_{12} = 1$, tag $T_1$ is confirmed to be present
    When $r_{12} = 0$ &amp;&amp; $r'_{12} = 0$, tag $T_1$ is confirmed to be absent
    When $r_{12} = 1$ XOR $r'_{12} = 1$
    When $r_{22} = 1$ &amp;&amp; $r'_{22} = 1$, tag $T_1$ is confirmed to be present
    When $r_{22} = 0$ &amp;&amp; $r'_{22} = 0$, tag $T_1$ is confirmed to be absent
    Otherwise, tag $T_1$ is confirmed to be present with probability 0.5
</div>

Fig. 4. Algorithm 4.

<table><tr><td></td><td>Algorithm1</td><td>Algorithm2</td><td>Algorithm3</td><td>Algorithm4</td><td>AW</td></tr><tr><td>TP</td><td>382.750(36.966)</td><td>437.200(24.011)</td><td>467.600(22.251)</td><td>488.063(18.869)</td><td>99.862(23.078)</td></tr><tr><td>TN</td><td>493.269(17.577)</td><td>438.350(26.649)</td><td>488.269(19.174)</td><td>486.913(18.368)</td><td>446.631(25.774)</td></tr><tr><td>Total T</td><td>876.019(40.986)</td><td>875.550(40.180)</td><td>955.869(26.632)</td><td>974.975(18.615)</td><td>546.494(15.593)</td></tr><tr><td>FN</td><td>116.188(36.335)</td><td>61.738(20.704)</td><td>31.338(18.465)</td><td>12.700(9.807)</td><td>400.538(17.889)</td></tr><tr><td>FP</td><td>7.794(5.680)</td><td>62.713(20.975)</td><td>12.794(8.976)</td><td>12.325(9.475)</td><td>52.969(14.065)</td></tr><tr><td>Total F</td><td>123.981(40.986)</td><td>124.450(40.180)</td><td>44.131(26.632)</td><td>25.025(18.615)</td><td>453.506(15.593)</td></tr></table>

Fig. 5. Results for Algorithms 1–4 (A1–A4) and the sliding window (AW) Algorithm.

## 4.4. Algorithm 4

We further re<sup>fi</sup>ne Algorithm 3 in this case. In addition to the two separate reads of the tag within a brief duration of time to more accurately identify the tag's presence as in Algorithm 3, we introduce an additional tag that is assumed to be simultaneously present with the tag of interest. To avoid confusion, we identify the tag of interest by $\mathrm { T } _ { 1 }$ and the additional tag by $\mathrm { T } _ { 2 } .$ Therefore, we have two tags that are read twice by each reader (Fig. 4).

In a pervasive healthcare environment, for example, tag $\mathrm { T } _ { 1 }$ can physically be with a physician and tag $\mathrm { T } _ { 2 }$ can physically be on a PDA or any electronic information support providing device. The two readers can be located close to the patient. For example, reader $\mathsf { R } _ { 1 }$ can be located in front of the patient's bed and reader $\mathsf { R } _ { 2 }$ can be on the side of the bed. When a physician approaches this patient's bed, both the readers $( \mathsf { R } _ { 1 }$ and $\mathsf { R } _ { 2 } )$ can be used to detect the presence of tags $\mathrm { T _ { 1 } }$ and $\mathrm { T } _ { 2 } .$ . Once the physician is con<sup>fi</sup>rmed to be approaching the patient, the patient's medical records can be passed on to the physician's device. Information in the medical records can be a composite of keyed entries, entries generated from tests (e.g., X-rays) as well as sensorbased entries. This generation, gathering, and presentation of information can be achieved without error only when the different components of the system work in concert. This is especially critical in context-aware pervasive healthcare applications where essential relevant information and services are provided to appropriate caretakers based on patient's history and current state [23].

The tag $\mathrm { T } _ { 1 }$ is assumed to be present when, after the <sup>fi</sup>rst read, both the readers $( \mathsf { R } _ { 1 }$ and $\mathsf { R } _ { 2 } )$ identify its presence just like in the base case. When both the readers $\left( \mathsf { R } _ { 1 } \right.$ and $\mathsf { R } _ { 2 } )$ identify it to be absent after the <sup>fi</sup>rst read, the tag $\mathrm { T } _ { 1 }$ is con<sup>fi</sup>rmed to be absent in the <sup>fi</sup>eld of the readers just like in the base case.

However, when one of the readers identi<sup>fi</sup>es it to be present after the <sup>fi</sup>rst read while the other does not identify its presence, we utilize information from the second reads of this tag $\left( \mathrm { T } _ { 1 } ^ { \prime } \right)$ by the readers in determining the presence/absence of $\mathrm { T } _ { 1 } .$ This step is similar to those in Algorithm 3. When both the readers $\left( \mathsf { R } _ { 1 } \right.$ and $\mathsf { R } _ { 2 } )$ identify $\mathrm { T } _ { 1 } { } ^ { \prime }$ to be present (i.e., the tag is identi<sup>fi</sup>ed to be present during the second read of $\mathrm { T } _ { 1 }$ by both the readers), we con<sup>fi</sup>rm the tag $\mathrm { T } _ { 1 }$ to be present. When neither of the readers $( \mathsf { R } _ { 1 }$ and $\mathsf { R } _ { 2 } )$ identi<sup>fi</sup>es $\mathrm { T } _ { 1 } { } ^ { \prime }$ to be present during the second read, we con<sup>fi</sup>rm the tag $\mathrm { T } _ { 1 }$ is absent as well. When only one of the readers $( \mathsf { R } _ { 1 }$ or $\mathsf { R } _ { 2 } )$ identi<sup>fi</sup>es $\mathrm { T } _ { 1 } { } ^ { \prime }$ to be present, we utilize information about the presence or absence of the second tag (T ). When the <sup>fi</sup>rst reader $\left( \mathsf { R } _ { 1 } \right)$ identi<sup>fi</sup>es the second tag to be present at both the reads, the tag $\mathrm { T _ { 1 } }$ is con<sup>fi</sup>rmed to be present. And, when the <sup>fi</sup>rst reader identi<sup>fi</sup>es the second tag to be absent at both the reads, the tag $\mathrm { T } _ { 1 }$ is con<sup>fi</sup>rmed to be absent. When the <sup>fi</sup>rst reader $\left( \mathsf { R } _ { 1 } \right)$ identi<sup>fi</sup>es the second tag to be present either in the <sup>fi</sup>rst read or in the second read but not both, we consider results from the second reader (R ). When the second reader $\left( \mathsf { R } _ { 2 } \right)$ identi<sup>fi</sup>es the second tag to be present at both the reads, the tag $\mathrm { T } _ { 1 }$ is con<sup>fi</sup>rmed to be present. And, when the second reader identi<sup>fi</sup>es the second tag to be absent at both the reads, the tag $\mathrm { T } _ { 1 }$ is con<sup>fi</sup>rmed to be absent. Otherwise, the tag $\mathrm { T } _ { 1 }$ is con<sup>fi</sup>rmed to be present with probability 0.5.

## 4.5. Results

We simulated the four algorithms presented above 10 times with 1000 readings per run with the following assumptions: The tag T (or, T in Algorithm 4) is always present (or, absent) during both the reads in a reader's <sup>fi</sup>eld. We assume the probability that T is present during the <sup>fi</sup>rst read, P(T)=0.5. When T is present, P(reader $\mathsf { R } _ { 1 }$ con<sup>fi</sup>rming tag T is present)=0.8 and P(reader $\mathsf { R } _ { 2 }$ con<sup>fi</sup>rming tag T is present)=0.9. Similarly, when T′ (i.e., tag T during the second read by the two readers) is present, P(reader $\mathsf { R } _ { 1 }$ con<sup>fi</sup>rming tag T is present)=0.9 and P(reader $\mathsf { R } _ { 2 }$ con<sup>fi</sup>rming T is present)=0.8. A similar set of probability values was used for the second tag ${ \bigl ( } \mathrm { T } _ { 2 } { \bigr ) } .$ . We include these probabilities to account for signal noise and other incidental reasons resulting in false readings.

<table><tr><td></td><td>A1A2</td><td>A1A3</td><td>A1A4</td><td>A2A3</td><td>A2A4</td><td>A3A4</td></tr><tr><td>TP</td><td>9.91567E-85</td><td>6.9376E-104</td><td>1.35156E-83</td><td>2.14168E-93</td><td>3.88328E-59</td><td>1.47424E-21</td></tr><tr><td>TN</td><td>2.32925E-88</td><td>4.77993E-34</td><td>0.001096536</td><td>1.94474E-94</td><td>2.93604E-50</td><td>0.486000032</td></tr><tr><td>Total T</td><td>0.559305097</td><td>1.2895E-108</td><td>3.96194E-91</td><td>5.405E-109</td><td>4.59967E-93</td><td>1.27074E-33</td></tr><tr><td>FN</td><td>9.91567E-85</td><td>6.9376E-104</td><td>3.18443E-91</td><td>2.14168E-93</td><td>6.36438E-86</td><td>3.86939E-42</td></tr><tr><td>FP</td><td>2.32925E-88</td><td>4.77993E-34</td><td>5.34942E-15</td><td>1.94474E-94</td><td>7.38979E-89</td><td>0.34223378</td></tr><tr><td>Total F</td><td>0.559305097</td><td>1.2895E-108</td><td>3.96194E-91</td><td>5.405E-109</td><td>4.59967E-93</td><td>1.27074E-33</td></tr></table>

Fig. 6. The p-values for results in Fig. 5 (using pairwise t-test).

<table><tr><td></td><td>A1AW</td><td>A2AW</td><td>A3AW</td><td>A4AW</td></tr><tr><td>TP</td><td>8.1311E-136</td><td>2.4477E-165</td><td>3.2895E-174</td><td>2.5954E-180</td></tr><tr><td>TN</td><td>1.1124E-43</td><td>0.003292846</td><td>2.82934E-37</td><td>7.99095E-38</td></tr><tr><td>Total T</td><td>3.9341E-153</td><td>1.5979E-153</td><td>2.1538E-195</td><td>2.9152E-222</td></tr><tr><td>FN</td><td>4.2005E-144</td><td>8.8058E-184</td><td>5.7296E-195</td><td>1.9931E-213</td></tr><tr><td>FP</td><td>5.07904E-84</td><td>2.72165E-07</td><td>2.67223E-72</td><td>5.60289E-77</td></tr><tr><td>Total F</td><td>3.9341E-153</td><td>1.5979E-153</td><td>2.1538E-195</td><td>2.9152E-222</td></tr></table>

Fig. 7. The p-values for results in Fig. 5 for cases with AW (using pairwise t-test).

Results from these simulation runs, in the form of true positives and true negatives, are given in Fig. 5. In this <sup>fi</sup>gure, the numbers given are generated from the average of ten runs with 1000 reads per run. The standard deviation values are given in parentheses. Each of these values corresponds to [(4 different probability values for R ×4 different probability values for $\mathsf { R } _ { 2 } ) \times 1 0$ runs=160 runs, with 1000 RFID tag reads per run]. The standard deviation values for results from these runs are given in parentheses. Fig. 5 contains results in the form of true positives (TP), true negatives (TN), overall correctly classi<sup>fi</sup>ed cases (T), false negatives (FN), false positives (FP), and overall incorrectly classi<sup>fi</sup>ed cases (F) for Algorithms 1–4. The last column in Fig. 5 contains the sliding window algorithm (AW) where we model a scenario as proposed in [1]. The reader takes a read every 2 s. If a tag is detected 66.67% of the time in a sliding window of size 15, the tag is con<sup>fi</sup>rmed to be present. Otherwise, the tag is con<sup>fi</sup>rmed to not be present in the reader's <sup>fi</sup>eld of view.

As can be seen from Fig. 5, Algorithm 4 dominates among the <sup>fi</sup>ve algorithms when true positives are used as the performance criterion. When true negatives are used as the performance criterion, Algorithm 1 dominates the other algorithms. Similarly Algorithms 4 and 1 perform the best when false negatives and false positives are used as the performance criterion respectively. However, in the overall total true (correctly classi<sup>fi</sup>ed) cases and overall false (incorrectly classi<sup>fi</sup>ed) cases Algorithm 4 dominates among those algorithms that are introduced in this paper. The sliding window algorithm (AW) performs poorly under all performance criteria considered.

To check for statistical signi<sup>fi</sup>cance of differences in results generated using the four different algorithms proposed in this paper, we use pairwise t-tests, which provides con<sup>fi</sup>dence intervals about the difference between two means. Results from this exercise are given in Fig. 6. We considered all possible pairs of algorithms, and represent Algorithms 1–4 by A1, A2, A3, and A4 respectively.

As can be seen from Fig. 6, A1 and A3 are statistically signi<sup>fi</sup>cantly different from each other. And so are A1 and A4, A2 and A3, and A2 and A4. Although A1 and A2 are statistically signi<sup>fi</sup>cantly different when TP, TN, FP, FN are compared, these differences wash out when results for TP and TN are combined as well as when results for FP and

![](/api/attachments/EFD22Q5P/fulltext/images/fa042d62f5ba4884f27489b7c11d3ef3013d9122f58b9053ad97d79f29e2c78f.jpg)  
Fig. 8. Average false positive cases using different probability values for reader R

![](/api/attachments/EFD22Q5P/fulltext/images/4b748964834b66973e6759bba4f2b6d4abd13b161febb46d76196e899bd1c7cd.jpg)  
Fig. 9. Average false negative cases using different probability values for reader R .

FN are combined. As for A3 and A4, the differences in results between them are statistically signi<sup>fi</sup>cant under TP, T, FN, and F but are not statistically signi<sup>fi</sup>cant under TN or FP as the performance criterion. This suggests that A1 and A2 as well as A3 and A4 share enough similarities in performance respectively. Knowing that A2 was generated by slightly modifying A1 and A4 was generated by modifying A3, these signi<sup>fi</sup>cant values for differences in results are not surprising. The difference between A2 and A3 is major compared to those between A1 and A2, hence the reason for the results obtained.

The corresponding results pairing the sliding window method (AW) with one of the algorithms proposed in this paper are given in Fig. 7. As can be seen in Fig. 7, all the differences in average values between A1–A4 and AW are statistically signi<sup>fi</sup>cant.

Results presented in Figs. 5–7 include aggregated reads from both the readers (R and R ). It would be interesting to consider the results from the perspective of each of the readers. In order to study the differences among the algorithms and their dynamics as the probability values associated with the two readers (R and R ) are varied, we now separately consider the results from the two readers. We therefore disaggregate and present the results given in Fig. 5, but separately for $\mathtt { R } _ { 1 }$ and $\mathsf { R } _ { 2 } ,$ in graphical form in Figs. 8–13. We only present the “false” categories (i.e., false positives, false negatives, and overall false cases) in the following <sup>fi</sup>gures to provide a <sup>fl</sup>avor of the dynamics.

From Fig. 8, we see that performance as measured by average false positives using different probability values for reader $\mathsf { R } _ { 1 }$ is not favorable to Algorithm 2. Results for Algorithms 1–4 are comparable and not as different as those for Algorithm 2. The sliding window algorithm (AW) performs worse throughout than A1, A3, and A4 but better than A2 for lower values of R1. The performance of A2 is slightly better than the sliding window algorithm for probability values above 0.9 that are associated with R1. As for A3 and A4, both Figs. 5 and 6 show that their aggregated results are comparable and difference in their performance is not statistically signi<sup>fi</sup>cant. However, as can be seen in Fig. 8, A4 is slightly better than A3 overall for higher probability values.

![](/api/attachments/EFD22Q5P/fulltext/images/c6f4ef7cfebd2ea5d9dddcdf0c8533b45d2830a44ea15c4d9bb252de4353c407.jpg)  
Fig. 10. Average overall false cases using different probability values for reader R .

![](/api/attachments/EFD22Q5P/fulltext/images/066ee8ae03edfc31f74262b06f716ee3c670a1c0e1974c9ee638653b4486f673.jpg)  
Fig. 11. Average false positive cases using different probability values for reader $\mathrm { R } _ { 2 } .$

From Fig. 9, we can see that with average false negative as the performance criterion the algorithms A1, A2, A3, and A4 are increasingly favorable in that order, with the differences between consecutive pairs of algorithm diminishing as we go from A1 through A4. AW consistently performs signi<sup>fi</sup>cantly worst among the <sup>fi</sup>ve algorithms considered. Moreover, AW's performance improvement with increase in the probability values seems to be minimal vis-à-vis algorithms A1–A4.

From Fig. 10, with average of all false (incorrectly classi<sup>fi</sup>ed) cases as the performance criterion, we see that the performance of A1 and A2 overlaps across all probability values that were considered for reader $\mathrm { R } _ { 1 } .$ Although the performance of A3 and A4 is different from those of A1 and A2, the former are closer but still different in performance. Again, AW performs worst overall among all <sup>fi</sup>ve algorithms considered.

Since the second reader $\left( \mathsf { R } _ { 2 } \right)$ is not used in the sliding window algorithm, the sliding window algorithm (AW) is not included in Figs. 11–13.

In Fig. 11, with average false positives as the performance criterion, the performance of algorithms A1, A3, and A4 is comparable while that of A2 is quite different and much worse for different probability values associated with reader $\mathtt { R } _ { 2 } .$ Again, results in Figs. 3 and 4 do not distinguish performance of A3 and A4 to be statistically different. From Fig. 11 it is clear that the performance of A3 improves faster compared to A4 with higher probability values for $\mathrm { R } _ { 2 } .$

In Fig. 12, with average false negative cases as the performance criterion and for different probability values for reader $\mathsf { R } _ { 2 } ,$ we see that the performance of A4 dominates followed by A3, A2, and A1.

From Fig. 13, with overall average false (incorrectly classi<sup>fi</sup>ed) cases as the performance criterion and for various probability values associated with reader $\mathrm { R } _ { 1 } ,$ we see that performance corresponding to algorithms A1 and A2 is comparable.

## 5. Discussion

The complexities associated with seamlessly integrating different related components to deliver pervasive healthcare necessitate peak performance of the individual components of the system both by themselves and also in concert with others. Although RFID tags are increasingly being used in such pervasive healthcare environments, their performance and therefore the resulting overall system performance can be improved further. Speci<sup>fi</sup>cally, we considered the detection problem where a tagged object is accurately identi<sup>fi</sup>ed to be present or absent in the <sup>fi</sup>eld of a reader. Although it is generally assumed that RFID tagged objects are correctly identi<sup>fi</sup>ed to be present 100% of the time, the reality is that it can vary widely depending on several factors including the presence of metal objects in the reader's <sup>fi</sup>eld, certain liquids, the orientation of the tag with respect to the reader, etc. Despite these adverse environmental effects, it is desirable to have accurate identi<sup>fi</sup>cation to be able to both locate and exchange data with tagged objects.

![](/api/attachments/EFD22Q5P/fulltext/images/3534d13cf6776290126666dd538846a1ad82194544ff49621816450bfce8d421.jpg)  
Fig. 12. Average false negative cases using different probability values for reader $\mathrm { R } _ { 2 } .$

![](/api/attachments/EFD22Q5P/fulltext/images/dc34732055edc53cd62817b1d68a2ac040766791abdac110cf4a99b9c015801b.jpg)  
Fig. 13. Average overall false cases using different probability values for reader $\mathrm { R } _ { 2 } .$

We proposed algorithms to reduce false positives and false negatives while identifying the presence/absence of an RFID tag in the <sup>fi</sup>eld of a reader, and illustrated these algorithms by means of an example scenario. Although our results are based on simpli<sup>fi</sup>ed assumptions, they show that false positives and false negatives can indeed be reduced through minor modi<sup>fi</sup>cations to input data analysis. Among the algorithms we proposed and studied, Algorithm 4 was the best and Algorithm 1 the worst overall, excluding the sliding window algorithm. The latter performed the worst overall among the <sup>fi</sup>ve algorithms that we considered. The proposed methods have several advantages over the moving time window algorithms that have been previously proposed. This includes a precipitous reduction in the amount of data processed for identi<sup>fi</sup>cation purposes and the absence of need to wait for a given threshold number of readings of a tag to been taken before a data point can be validated. Moreover, in most applications, a given tag is only scanned a minimal number of times at any location due to resource constraints (e.g., tags are quickly in and out of the <sup>fi</sup>eld of the reader for any meaningful number of reads to occur, the sheer number of tags in a reader's <sup>fi</sup>eld precludes multiple number of reads, etc.) and the windowing algorithms are not applicable in these scenarios.

Preliminary results from this study are promising. We are in the process of extending this study to include more ambient information in determining the presence/absence of RFID tags in the <sup>fi</sup>eld of a reader. Since data gathering accuracy has been touted as a major bene<sup>fi</sup>cial property of RFID tag-enabled systems, false readings can drastically reduce the utility of RFID tags. Any successful attempt at improving true (positive and negative) readings would ultimately increase the performance and ef<sup>fi</sup>ciency of RFID tag-enabled systems. Unlike in a typical supply chain scenario where a false positive or false negative instance may not create even a ripple, such instances may result in a disastrous outcome for the patient involved in a pervasive healthcare setting. For example, falsely missing the presence of a foreign object in a patient could result in such object being left inside the patient with deleterious consequences. On the other hand, falsely identifying the presence of an object when it is not actually present could result in the precipitation of unnecessary measures that consume scarce resources and are truly not warranted. Given the criticality of accuracy in pervasive healthcare settings, any improvement in that direction translates to immediate tangible bene<sup>fi</sup>ts. This is even more salient given that the methods proposed in this paper can be implemented with minimal resources and effort.

## References

[1] S. Agarwal, A. Joshi, T. Finin, Y. Yesha, T. Ganous, A pervasive computing system for the operating room of the future, Mobile Networks and Applications 12 (2007) 215–228.

[2] Y. Bai, F. Wang, P. Liu, Ef<sup>fi</sup>ciently Filtering RFID Data Streams, CleanDB, 2006.

[3] Y. Bai, F. Wang, P. Liu, C. Zaniolo, S. Liu, RFID data processing with a data stream query language, Proceedings of the 23nd International Conference on Data Engineering, ICDE, vol. 2007, 2007, pp. 1184–1193.

[4] J.M. Corchado, J. Bajo, Y. de Paz, D.I. Tapia, Intelligent environment for monitoring Alzheimer patients, agent technology for healthcare, Decision Support Systems 44 (2) (2008) 382–396.

[5] D.W. Bates, M. Cohen, L.L. Leape, J.M. Overhage, M.M. Shabot, T. Sheridan, Reducing the frequency of errors in medicine using information technology, Journal of the American Medical Informatics Association 8 (4) (2001) 299–308.

[6] D.W. Bates, L.L. Leape, D.J. Cullen, Effects of computerized physician order entry and a team intervention on prevention of serious medication errors, Journal of the American Medical Association 280 (1998) 1311–1316.

[7] E.S. Berner, Diagnostic decision support systems: why aren't they used more and what can we do about it? Proceedings of AMIA 2006 Symposium, 2006, pp. 1167–1168.

[8] G. Borriello, W. Brunette, M. Hall, C. Hartung, C. Tangney, Reminding about tagged objects using passive RFIDs, Ubicomp (2004) 36–53.

[9] B. Carbunar, A. Grama, J. Vitek, O. Carbunar, Redundancy and coverage detection in sensor networks, ACM Transactions on Sensor Networks 2 (1) (2006) 94–128.

[10] A.X. Garg, N.K.J. Adhikari, H. McDonald, M.P. Rosas-Arellano, P.J. Devereaux, J. Beyene, J. Sam, R.B. Haynes, Effects of computerized clinical decision support systems on practitioner performance and patient outcomes, Journal of the American Medical Association 293 (10) (2005) 1223–1238.

[11] L. Harpole, R. Khorasani, J. Fiskio, G. Kuperman, D. Bates, Automated evidence based critiquing of orders for abdominal radiographics: impact on utilization and appropriateness, Journal of the American Medical Informatics Association 4 (1997) 511–521.

[12] P. Harrop, RFID in Healthcare and Pharmaceutical Applications, IDTechEx, , 2007.

[13] Y. Hu, S. Sundara, T. Chorma, J. Srinivasan, Supporting RFID-based item tracking applications in oracle DBMS using a bitmap datatype, Proceedings of the 31st VLDB Conference, 2005, pp. 1140–1151.

[14] S.R. Jeffery, N.M. Garofalakis, M.J. Franklin, Adaptive cleaning for RFID data streams, Proceedings of the 32nd VLDB Conference, 2006, pp. 163–174.

[15] R. Kaushal, D. Bates, Computerized Physician Order Entry (CPOE) with Clinical Decision Support Systems (CDSSs), Agency for Healthcare Research and Quality Evidence-based Practice Center Report on Patient Safety AHRQ, 2002.

[16] N. Khoussainova, M. Balazinska, D. Suciu, Probabilistic RFID Data Management, UW CSE Technical Report UW-CSE-07-03-01, 2007.

[17] R.S. Ledley, L.B. Lusted, Reasoning foundations of medical diagnosis, Science 130 (1959) 9–21.

[18] K. Michael, L. McCathie, The pros and cons of RFID in supply chain management Proceedings of the International Conference on Mobile Business, 2005, pp. 623–629.

[19] E.W.T. Ngai, T.C.E. Cheng, S. Au, K.H. Lai, Mobile commerce integrated with RFID technology in a container depot, Decision Support Systems 43 (1) (2007) 62–76.

[20] S. Piramuthu, Protocols for RFID tag/reader authentication, Decision Support Systems 43 (3) (2007) 897–914.

[21] A.G. Randolph, R.B. Haynes, J.C. Wyatt, D.J. Cook, G.H. Guyatt, Users' guides to the medical literature: XVIII. How to use an article evaluating the clinical impact of a computer-based clinical decision support system, Journal of the American Medical Association 282 (1) (1999) 67–74

[22] J. Rao, S. Doraiswamy, H. Thakkar, L.S. Colby, A deferred cleansing method for RFID data analytics Proceedings of the 32nd VLDB Conference (2006) 175–186

[23] M. Tentori, J. Favela, V.M. Gonzalez, Towards the Design of Activity-Aware Mobile Adaptive Applications for Hospitals, The 4th International Workshop on Ubiquitous Computing for Pervasive Healthcare Applications, 2006.

[24] Y.-J. Tu, S. Piramuthu, Reducing false reads in RFID-embedded supply chains, Journal of theoretical and Applied Electronic Commerce Research 3 (2) (2008) 60–70.

[25] D. Viehland, A. Wong, The future of radio frequency identi<sup>fi</sup>cation, Journal of Theoretical and Applied Electronic Commerce Research 2 (2) (2007) 74–81.

Yu-Ju Tu is a graduate student in Information Systems at the University of Illinois at Urbana-Champaign. His research interests include RFID systems.

Wei Zhou received his Ph.D. in Information Systems from the University of Florida in 2008. His research interests include RFID-enabled item-level information visibility, Internet advertising, and knowledge-based learning systems. His work has appeared in European Journal of Operational Research, IEEE Transactions on Geosciences and Remote Sensing, International Journal of Electronic Commerce, and Optical Engineering.

Selwyn Piramuthu is Associate Professor in the Information Systems and Operations Management Department at the University of Florida. His research interests include RFID systems, pattern recognition and its application in supply chain management, computer-aided manufacturing, and <sup>fi</sup>nancial credit-risk analysis.
