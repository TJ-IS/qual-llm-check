---
otero_id: 16336
otero_key: "Q2Y8XVHW"
title: "Towards an integrated model of IT acceptance in healthcare"
authors: "Trevor T. Moores"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.04.014"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Towards an integrated model of IT acceptance in healthcare

Trevor T. Moores ⁎

Department of Information Systems and Decision Sciences, ESSEC Business School, Av. Bernard Hirsch, BP 50105, 95021 Cergy-Pontoise Cedex, France

a r t i c l e i n f o

Article history: Received 22 September 2011 Received in revised form 7 March 2012 Accepted 29 April 2012 Available online 5 May 2012

Keywords: Compatibility Information quality PLS System use TAM User experience

## a b s t r a c t

We develop and test an integrated model of IT acceptance that revisits the technology acceptance model (TAM) and compares the role of attitude, use, and compatibility as measures of IT acceptance. A pair of second-order constructs de<sup>fi</sup>ne perceived usefulness in terms of information quality (accuracy, content, format, and timeliness), while perceived ease of use is de<sup>fi</sup>ned in terms of factors that enable the user to make use of the system (speci<sup>fi</sup>cally, computing support and user ef<sup>fi</sup>cacy). Using PLS, we apply the model to the adoption of a clinical management system for hospital workers and <sup>fi</sup>nd strong support. By assessing levels of user experience we <sup>fi</sup>nd enabling factors drive a users' initial understanding of the system, while more experienced users focus on usefulness and compatibility. Theoretical and practical contributions are discussed. © 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

The promise of health IT, such as electronic health records and clinical data exchanges, is the potential to improve the quality of patient care by increasing care coordination, eliminating errors, and reducing costs [6]. Electronic health records (EHR) store the medical history of patients and can be multi-functional systems that allow physicians to enter care (i.e., treatment) orders, manage lab results, and provide diagnostic decision support. Clinical data exchanges (CDE, or telemedicine) are network systems that facilitate the exchange of information between patients and health care providers. Estimates suggest that the development of a national telemedicine infrastructure would save \$5.2 billion a year from reduced patient visits, transfers between emergency departments, and duplicate testing [15]. The 2009 Health Information Technology for Economic and Clinical Health (HITECH) Act provides over \$22 billion in incentives and support costs to encourage the adoption and use of IT in healthcare. The largest amount, \$18 billion, is aimed at reimbursing hospitals and physicians for the “meaningful use” of electronic health record systems, while \$2 billion is set aside for infrastructure and training.

Despite these positive aspects the challenges are formidable. It is estimated that up to 98,000 people die each year in US hospitals because of medical errors, more than double the number that die in motor vehicle accidents [35]. Recent studies suggest while the use of health IT does indeed increase the quality of care and reduce errors, evidence to suggest an improvement in ef<sup>fi</sup>ciency or reduction in cost has been mixed [9]. Adoption rates are also low. Less than 10% of US hospitals and only 17% of physicians have adopted a basic electronic medical record system, with the cost of implementing and maintaining the technology often cited as a main concern [20,29]. Furthermore, the introduction of health IT can often generate resistance from healthcare workers, especially if the system is seen as a threat or incompatible with the way they like to work [16,28,37,45,64]. Clearly, there is a problem with the adoption of IT in healthcare.

We propose a research model based on the technology acceptance model (TAM) [17,19]. We retain the TAM constructs perceived usefulness (PU) and perceived ease of use (PEOU) as the fundamental determinants of IT acceptance, but also seek to address some of the criticisms recently directed towards TAM. In particular, that system use is a poor surrogate for acceptance because it is a poorly de<sup>fi</sup>ned measure, while little work has been done to delineate the antecedents of PU and PEOU [1,2]. If system use is a weak construct then attitude towards using (ATT) is the only dependent variable left, but this is an unsatisfying measure of IT acceptance. We propose that a better measure might be compatibility with the way end-users like to work (COM). With respect to the antecedents of PU and PEOU, we de<sup>fi</sup>ne a pair of second-order constructs that de<sup>fi</sup>ne PU in terms of the information quality, while PEOU is de<sup>fi</sup>ned in terms of factors that enable the user to make use of the system. We believe this model is in line with the original intentions of TAM and provides a parsimonious set of constructs that tap into the most important issues related to IT acceptance.

## 2. Background

The technology acceptance model (TAM) is one of the most in<sup>fl</sup>uential theories in IT adoption and acceptance research [38,39]. Derived from the theory of reasoned action (TRA) [23], TAM suggests that the most salient beliefs that determine one's attitude towards using a system, and consequently one's intention and actual level of use, are perceived usefulness (PU) and perceived ease of use (PEOU). Perceived usefulness is de<sup>fi</sup>ned as the subjective probability that using the system will increase his or her job performance, while perceived ease of use is de<sup>fi</sup>ned as the degree to which the prospective user expects the target system to be free of effort [17,19].

The most common version of TAM (see Fig. 1) suggests that PU and PEOU jointly determine attitude towards using a system (ATT), ATT and PU determine the behavioral intention to use (INT), while INT determines actual system use (USE). Given usefulness is easier to perceive if the system is easy to use, it is also hypothesized that there is a relationship between PEOU and PU. A more parsimonious version of TAM eliminates ATT, with PEOU directly impacting on INT [19]. The PU and PEOU scales have since been found to have strong psychometric properties, with TAM explaining 30–40% of the variance in intention or use in a wide variety of settings, although PU is clearly the dominant construct [33,41]. New versions of TAM primarily focus on providing additional antecedent constructs for PU and PEOU [53–55,57].

A number of studies have applied TAM to the adoption and acceptance of IT in healthcare, <sup>fi</sup>rst in terms of proving the veracity of TAM [25,65], and later with additional constructs that take into account the particular context of health IT. For instance, willingness to try new technology (personal innovativeness) positively in<sup>fl</sup>uences the intention to use a patient–physician web portal [34], while resistance to change negatively impacts the intention to use a computerized physician order entry system [4]. Service level is also an important determinant of PU and PEOU, either in terms of the general reliability, stability, and responsiveness of the system [40,62], or more speci<sup>fi</sup>c issues, such as physical access to computers and access rights to the system [27].

There are three main criticisms of TAM [1,2]: 1. system use is too narrow as a de<sup>fi</sup>nition of adoption or acceptance and needs to be broadened; 2. the lack of research on the design and implementation-based antecedents of PU and PEOU has resulted in a confusing plethora of versions of TAM; and, 3. TAM fails to explain the behavioral and performancebased consequences of adoption and acceptance. The problem of system use, both in terms of its de<sup>fi</sup>nition and its applicability as a measure of adoption, acceptance, or success, has been known for some time [8,46]. The failure to de<sup>fi</sup>ne the antecedents of PU and PEOU or the consequences of adoption is derived from the habit of researchers to add to, rather than explain, PU or PEOU. Furthermore, given that PU and PEOU are hypothesized to impact on either system use [17,18], attitude, or intention to use [19], it is sometimes dif<sup>fi</sup>cult to know exactly which dependent variable should be used. But if PU is the key to understanding system use [2], this construct must be the focal point of any model of IT acceptance.

## 3. Research model

To develop a version of TAM that applies to healthcare IT, while laudable, would simply fall into the trap of adding just another variant to the already extensive literature. Rather, we are guided by one principle: The model must be as parsimonious as possible, and include only the essential components most likely to in<sup>fl</sup>uence IT acceptance. From a theoretical point of view, such a model would provide a benchmark against which further extensions of TAM could be compared. From a practical point of view, the dif<sup>fi</sup>culty of collecting data from medical staff during their normal working day would be alleviated to some extent by only asking questions that are essential to understanding the key constructs that drive IT acceptance.

The solution, we suggest, is to retain PU and PEOU as the fundamental determinants of IT acceptance, explain the antecedents of these two constructs, and explore alternative dependent variables. Therefore, our research model (see Fig. 2) proposes three measures of acceptance: depth and breadth of use (USE) as a standard measure, attitude towards using (ATT) as the only remaining endogenous variable from TAM, and compatibility (COM), as an alternative attitudinal construct that taps into the extent to which the system <sup>fi</sup>ts the way the user likes to work. The basic mechanisms underlying PU are system and design characteristics, while the basic mechanisms underlying PEOU are self-ef<sup>fi</sup>cacy and reduction in effort [17]. Therefore, we de<sup>fi</sup>ne information quality (INFQ) as the key design-based antecedent to PU, while enabling factors (ENBF) are the key effortrelated antecedent to PEOU. Support for this model is outlined below.

## 3.1. Measures of acceptance

While a common representation of IT adoption or acceptance, the interpretation of system use is open to debate [8,46]. For instance, if a system is supposed to increase ef<sup>fi</sup>ciency then low levels of use would indicate success, while high levels of use for systems that are a required part of an individual's work routine would be effort, not acceptance. When system use is mandatory, PEOU can replace PU as the most important determinant of intention to use [7], although PU is still a signi<sup>fi</sup>cant predictor of the level of system use [55,61]. On the other hand, system use has strong face validity: If the system is not used it cannot provide any intended bene<sup>fi</sup>ts and must be deemed a failure. The possibility that a system might reduce overall effort must be deemed a special case, given that if the system increases productivity it's more likely the user will produce more work rather than see a reduction of time spent using the system. As such, we retain system use (USE) as a measure of behavior but anticipate there may be insigni<sup>fi</sup>cant relationships with antecedent constructs if system use is mandated. Therefore, we suggest:

H1. System use will be signi<sup>fi</sup>cantly and positively determined by (a) perceived usefulness; or, (b) perceived ease of use, unless system use is mandatory.

If system use is no longer the key dependent variable, then intention to use (INT) has no nomological validity, given that no relationship now exists to its required consequent, system use. The remaining dependent variable is attitude towards using (ATT), although in the parsimonious version of TAM this construct was dismissed because it was not signi<sup>fi</sup>- cantly related to INT [19]. Studies that include this construct <sup>fi</sup>nd strong support for the PU–ATT relationship [63]. When included in the acceptance of IT in healthcare, PU–ATT is found to be strongly signi<sup>fi</sup>- cant, while PEOU–ATT is either weak [62] or not signi<sup>fi</sup>cant [25,27]. On the other hand, the value of PEOU is that early in the development process PU and PEOU can be used to gauge an early, and hopefully predictive, assessment of the likely level of acceptance of the new system. We will therefore take a positive view of PEOU, and suggest:

![](/api/attachments/Q2Y8XVHW/fulltext/images/a3c05f1c7c2ae3891d6472b8cc9bfb38fa17580c82c34d32b917d8532012271b.jpg)  
Fig. 1. The technology acceptance model (TAM).

![](/api/attachments/Q2Y8XVHW/fulltext/images/b8bf85fc0e52fa63b6fe1d7a1671a37b8b98adf06a1844cf44ca8d97d9dc5e84.jpg)  
Fig. 2. The research model.

H2. Attitude towards using will be signi<sup>fi</sup>cantly and positively determined by (a) perceived usefulness; and, (b) perceived ease of use.

While a number of other net bene<sup>fi</sup>ts are expected to accrue from the implementation of an information system, we also suggest that ensuring the compatibility of the system with current work practices is a necessary component of IT acceptance. Compatibility (COM) is de<sup>fi</sup>ned as one of the key beliefs that in<sup>fl</sup>uence adoption [42], and de-<sup>fi</sup>ned as the extent to which the system <sup>fi</sup>ts or is compatible with the way the user likes to work [32,47,50]. If the technology is perceived to interfere with the power or status of physicians, slow down procedures or increase workloads, then patterns of resistance can emerge that undermines the potential bene<sup>fi</sup>ts of the system and lead to project failure [37]. Only by allowing key stakeholders to maintain a central role in the decision-making process can resistance be overcome [16]. We suggest that COM can rival ATT as a consequent of PU and PEOU. Most importantly, compatibility is framed in attitudinal/belief statements about work practices that are consistent with the notion that a system must “<sup>fi</sup>t” with the needs of the user, exactly the issue that may help overcome resistance to the adoption of IT often found in healthcare. Compatibility can therefore be used as a more workspecific measure of the impact of IT than USE or ATT. Thus, we have:

H3. Compatibility will be signi<sup>fi</sup>cantly and positively determined by (a) perceived usefulness; and, (b) perceived ease of use.

## 3.2. Antecedents of PU and PEOU

If system and design characteristics are the basic mechanisms underlying PU, while self-ef<sup>fi</sup>cacy and reduction in effort are the basic mechanisms underlying PEOU [19], we suggest that two secondorder constructs, information quality (INFQ) and enabling factors (ENBF) can summarize exactly these properties.

Information quality is de<sup>fi</sup>ned in terms of the accuracy (ACC), content (CNT), format (FMT), and timeliness (TIM). In other words, is the system free of errors (ACC), does the system provide the information needed for the user to complete their work (CNT) at the time they need it (TIM), and is the information output in an easy-to-read format (FMT)? These factors are the main components of the second-order end-user computing satisfaction (EUCS) instrument [21], and have previously been incorporated into antecedents of information quality within TAM [60]. Ease of use is also part of the EUCS construct, but PEOU has already been accounted for in our model. The EUCS constructs are well-established, and have been validated in terms of their psychometric properties [22]. Other studies have also found that high-quality data should be intrinsically good, contextually appropriate, clearly represented, and accessible [58]. These four factors also neatly summarize the functionality a user needs to perform their computer-based task. Therefore, we have:

H4. Information quality will be signi<sup>fi</sup>cantly and positively determined by (a) accuracy; (b) content; (c) format; and, (d) timeliness.

Enabling factors (ENBF) is de<sup>fi</sup>ned in terms of organizational and personal factors that allow the user to make full use of the technology. Speci<sup>fi</sup>cally, we suggest the extent to which the organization provides technical support to end-users, and the individual's belief in their ability to use the system, will have a signi<sup>fi</sup>cant impact on how the technology is perceived. Computing support (CSP) refers to the extent to which the user believes adequate computing support is being provided, such as the availability of specialized training and assistance in the event of hardware or system dif<sup>fi</sup>culties [26]. Ability, here de<sup>fi</sup>ned in terms of self-ef<sup>fi</sup>cacy (EFF), refers to the extent to which the system user believes they have the capability to use the system [13]. Capability is measured in terms of comfort, ease, or con-<sup>fi</sup>dence in using the system without help from someone else. Computing support and self-ef<sup>fi</sup>cacy have a rich history in terms of denoting key antecedents to levels of use and/or performance [14,48]. Therefore, we have:

H5. Enabling factors will be signi<sup>fi</sup>cantly and positively determined by (a) computing support; and, (b) self-ef<sup>fi</sup>cacy.

As a measure of the quality of the information the system provides, INFQ will be most strongly related to PU. After all, the raison d'être of an information system is to support the information needs of the user. It is also possible that presenting this information in a coherent and meaningful form will also promote a belief that the system is easy to use, in which case INFQ may in<sup>fl</sup>uence PEOU. Furthermore, it seems reasonable to suggest that ENBF will be most strongly related to PEOU. If computing support (CSP) is effective, problems with the system should be resolved quickly, while an individual's belief in their own ef<sup>fi</sup>cacy in using the system (EFF) will promote an overall perception that the system is easy to use (PEOU). Given that TAM also hypothesizes a link between PEOU and PU, we may also <sup>fi</sup>nd that if the enabling factors reduce effort, the perception of the usefulness of the system will increase. Therefore, we have:

H6. Perceived usefulness will be signi<sup>fi</sup>cantly and positively determined by (a) perceived ease of use; (b) information quality; and, (c) enabling factors.

H7. Perceived ease of use will be signi<sup>fi</sup>cantly and positively determined by (a) information quality; and, (b) enabling factors.

Finally, a number of studies have suggested that certain demographic variables, such as gender and experience, are likely to moderate the relationship between the TAM constructs [56,57]. While sensitivity to gender (or age) might help in training and development programs, experience is perhaps the most important variable, given this demographic may help explain the changing beliefs and levels of satisfaction found over time that can result in a decline in system use [3,5]. In short, dividing the sample into low- and high-experience groups would allow us to see how perceptions of the system change over time. Our <sup>fi</sup>nal hypothesis, therefore, is:

H8. Experience in using the system has a signi<sup>fi</sup>cant moderating effect on each component of IT acceptance.

## 4. Method

The target system was a proprietary clinical management system (CMS) used in a public, regional hospital with approximately 900 clinical staff, which includes physicians, nurses, and allied health workers (counselors, speech therapists, dieticians, etc.). The CMS involved an integrated suite of applications related to all aspects of a patient's visit and treatment, including admission/discharge or transfer, diagnosis and procedure coding, laboratory results and reporting, medication order entry, out-patient appointment management, and clinical records. Any staff member admitting, treating, or releasing a patient would make use of one or more of these systems. As such, the CMS is an example of a system where utilization is not voluntary and so we would expect our null hypothesis to be valid, with no relationship between PU, PEOU, and system use.

Given the target sample, it was assumed at the outset that the response rate would be low and a pilot study would further reduce the sample size. As such, items for each construct were adapted from existing literature where the items were well-established, short, and showed signi<sup>fi</sup>cant psychometric properties. The second-order information quality (INFQ) and enabling factors (ENBF) constructs are measured using repeated indicators, where each of the items from the <sup>fi</sup>rst-order constructs is included in the second-order construct. For each of the INFQ and ENBF constructs, an item that began “Overall, …” and summarized the construct was added to round out the construct and ensure each construct had at last three items. Constructs with at least three items tend to have better psychometric properties [12]. The order of each set of items was randomized, with USE placed at the end. Readability of the instrument was tested with the help of two physicians that completed the survey and were then asked for feedback. Both <sup>fi</sup>nished within 15 min and reported no problems in answering the questions. The items, source, and amendments made are shown in Appendix A.

With the permission of the hospital manager, sets of surveys were produced for each of the departments. Each set included an introductory letter explaining the aim of the survey, the survey instrument, and a pre-paid envelope for the return. There were 383 returns, giving an approximate return rate of 43%, although several were incomplete. Given that most of the constructs in our model have three or more items it seemed reasonable to retain all returns that had no more than three missing items, which resulted in 346 usable returns. The majority of respondents classi<sup>fi</sup>ed themselves as nursing staff (78%), with the remainder as physicians (18%), and allied health (4%). Experience in using the CMS ranged from 1 month to over 6 years, with an average of 2.4 years. About 18% are responsible for data input, 50% use the CMS for data retrieval, while 32% do both.

We test for non-response bias by comparing early to late respondents on the assumption that late respondents are more representative of non-respondents. Given that returns tended to come in large batches it is not certain the order in which the returns were received indicated the order in which they were completed. As such, we take a broad approach and compare the <sup>fi</sup>rst 150 recorded returns to the last 150. We use a 1-way MANOVA with early versus late as the grouping variable and the set of items for each construct as the dependent variable. No signi<sup>fi</sup>cant differences were found (p>0.1). We test for common method bias using Harman's One-Factor test, which suggests that if the majority of the variance explained loads on a single factor there is evidence of a common method bias. A principal component factor analysis produced 10 factors with eigenvalues greater than 1.0, accounting for 70.4% of the variance. The <sup>fi</sup>rst factor accounted for 31.2% of the variance, which suggests common method bias is not likely to be a concern.

## 5. Data analysis

We test the research model using partial least squares (PLS) and SmartPLS [44]. PLS is a component-based approach to structural equation modeling. The main advantage of PLS is that relatively complex, exploratory models can be developed where the main objective is predictive rather than con<sup>fi</sup>rmatory analysis [11]. The technique is fairly robust with respect to sample size and does not require normal distribution of the manifest variables. When applying PLS we <sup>fi</sup>rst examine the measurement model by assessing the convergent and discriminant validity of items and constructs, and then examine the structural model by assessing the path coef<sup>fi</sup>cients between constructs.

## 5.1. Measurement model

To ensure convergent validity, items should load on their respective (a priori) constructs with loadings greater than 0.6, and to ensure discriminant validity there should be no signi<sup>fi</sup>cant cross-loadings [10]. As can be seen (Table 1), all items have loadings greater than 0.6, with no cross-loadings greater than 0.6, while t-statistics derived from bootstrapping (1000 resamples) suggest all loadings are signi<sup>fi</sup>- cant at pb0.001. The one exception is the EFF2 item that cross-loads with the PEOU construct with a loading of 0.62, although the loading is less than the loading on the EFF construct (0.86), and lower than the PEOU items (0.67–0.80). As such, this cross-loading is not deemed to be a threat to the validity of the EFF or PEOU constructs.

Constructs should have an average variance extracted (AVE) of more than 0.5 and a composite reliability of more than 0.7 (convergent validity), and inter-construct correlations should be less than the square-root of the AVE (discriminant validity) [10]. As can be seen (Table 2), all constructs exceed these criteria, with AVE and CR generally greater than 0.6 and 0.8, respectively, and the square-root of the AVE being at least 0.3 greater than the inter-construct correlations (Table 3). The one exception is the correlation between EFF and PEOU, almost certainly due to the cross-loading of the EFF2 item.

However, the square-root of the AVE still exceeds the inter-construct correlation by 0.22 and is deemed satisfactory.

## 5.2. Structural model

The results of the PLS analysis is shown in Fig. 3. Standardized path coef<sup>fi</sup>cients are expected to be at least 0.2, and preferably greater than 0.3 [10]. The reliability of each coef<sup>fi</sup>cient is assessed from bootstrapping (1000 resamples). Support is provided for all hypotheses except H1a, H1b, H6a, H6c, and H7a. Although the path coef<sup>fi</sup>cients for ENBF–PU (H6c) and INFQ–PEOU (H7a) are signi<sup>fi</sup>cant (pb0.01), the magnitude of the coef<sup>fi</sup>cient is borderline. The path coef<sup>fi</sup>cient for PEOU–PU (H6a) is not signi<sup>fi</sup>cant (0.07), and appears to interfere with the in<sup>fl</sup>uence of ENBF on PU. When PEOU–PU is removed, the path coef<sup>fi</sup>cient for ENBF–PU increases to 0.22 (pb0.001). All other path coef<sup>fi</sup>cients are above 0.2 and signi<sup>fi</sup>cant (pb0.001), with the majority above 0.3.

As a test of parsimony, we add further plausible relationships to determine whether any signi<sup>fi</sup>cant relationships are missing. The path coef<sup>fi</sup>cient of ATT–USE (0.02), and COM–USE (0.14) is not significant, while COM–ATT (0.19) is borderline. Adjusting the model to represent COM as an antecedent to PU and PEOU shows that COM–

Table 1  
PLS con<sup>fi</sup>rmatory factor analysis.  
Note. Loadings shown in bold represent items loading on their a priori constructs. Cross-loadings less than 0.6 suppressed.

<table><tr><td></td><td>ACC</td><td>ATT</td><td>CNT</td><td>COM</td><td>CSP</td><td>EFF</td><td>FMT</td><td>PEOU</td><td>PU</td><td>TIM</td><td>USE</td></tr><tr><td>ACC1</td><td>0.77</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ACC2</td><td>0.86</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ACC3</td><td>0.78</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ATT1</td><td></td><td>0.82</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ATT2</td><td></td><td>0.89</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ATT3</td><td></td><td>0.71</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ATT4</td><td></td><td>0.75</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CNT1</td><td></td><td></td><td>0.80</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CNT2</td><td></td><td></td><td>0.80</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CNT3</td><td></td><td></td><td>0.65</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CNT4</td><td></td><td></td><td>0.76</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CNT5</td><td></td><td></td><td>0.84</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>COM1</td><td></td><td></td><td></td><td>0.89</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>COM2</td><td></td><td></td><td></td><td>0.87</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>COM3</td><td></td><td></td><td></td><td>0.86</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CSP1</td><td></td><td></td><td></td><td></td><td>0.85</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CSP2</td><td></td><td></td><td></td><td></td><td>0.87</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CSP3</td><td></td><td></td><td></td><td></td><td>0.81</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CSP4</td><td></td><td></td><td></td><td></td><td>0.86</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EFF1</td><td></td><td></td><td></td><td></td><td></td><td>0.81</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EFF2</td><td></td><td></td><td></td><td></td><td></td><td>0.86</td><td></td><td>0.62</td><td></td><td></td><td></td></tr><tr><td>EFF3</td><td></td><td></td><td></td><td></td><td></td><td>0.79</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EFF4</td><td></td><td></td><td></td><td></td><td></td><td>0.88</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>FMT1</td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.85</td><td></td><td></td><td></td><td></td></tr><tr><td>FMT2</td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.86</td><td></td><td></td><td></td><td></td></tr><tr><td>FMT3</td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.87</td><td></td><td></td><td></td><td></td></tr><tr><td>PEOU1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.69</td><td></td><td></td><td></td></tr><tr><td>PEOU2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.77</td><td></td><td></td><td></td></tr><tr><td>PEOU3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.80</td><td></td><td></td><td></td></tr><tr><td>PEOU4</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.67</td><td></td><td></td><td></td></tr><tr><td>PEOU5</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.76</td><td></td><td></td><td></td></tr><tr><td>PEOU6</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.79</td><td></td><td></td><td></td></tr><tr><td>PU1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.81</td><td></td><td></td></tr><tr><td>PU2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.80</td><td></td><td></td></tr><tr><td>PU3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.86</td><td></td><td></td></tr><tr><td>PU4</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.86</td><td></td><td></td></tr><tr><td>PU5</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.77</td><td></td><td></td></tr><tr><td>PU6</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.86</td><td></td><td></td></tr><tr><td>TIM1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.78</td><td></td></tr><tr><td>TIM2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.83</td><td></td></tr><tr><td>TIM3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.81</td><td></td></tr><tr><td>USE1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.67</td></tr><tr><td>USE2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.83</td></tr><tr><td>USE3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.61</td></tr></table>

Table 2  
Convergent reliability of constructs.

<table><tr><td>Construct</td><td>Average variance extracted (AVE)</td><td>Composite reliability (CR)</td></tr><tr><td>ACC</td><td>0.64</td><td>0.84</td></tr><tr><td>ATT</td><td>0.63</td><td>0.87</td></tr><tr><td>CNT</td><td>0.60</td><td>0.88</td></tr><tr><td>COM</td><td>0.76</td><td>0.90</td></tr><tr><td>CSP</td><td>0.72</td><td>0.91</td></tr><tr><td>EFF</td><td>0.70</td><td>0.90</td></tr><tr><td>FMT</td><td>0.74</td><td>0.89</td></tr><tr><td>PEOU</td><td>0.56</td><td>0.88</td></tr><tr><td>PU</td><td>0.68</td><td>0.93</td></tr><tr><td>TIM</td><td>0.65</td><td>0.85</td></tr><tr><td>USE</td><td>0.50</td><td>0.75</td></tr></table>

PEOU (0.16) is not signi<sup>fi</sup>cant, but COM–PU (0.34) is, although the path coef<sup>fi</sup>cients in both cases are lower than PEOU–COM (0.26), and PU–COM (0.46). These results suggest that the model is parsimonious, with no signi<sup>fi</sup>cant relationships omitted, and COM is more meaningfully represented as a consequent of PU and PEOU, rather than as an antecedent to either PU, PEOU, or ATT.

Overall, the model explains more than 30% of the variance in the endogenous variables (PU, PEOU, ATT, and COM). Following others [49], we calculate the global goodness-of-<sup>fi</sup>t (GoF) statistic for our model using the equation:

$$
\mathrm{GoF} = \sqrt {\overline {{\mathrm{AVE}}} * \overline {{\mathrm{R} ^ {2}}}}.
$$

Including USE gives GoF=0.42, while omitting USE gives GoF=0.46. Both exceed the threshold of GoF>0.36 suggested for large effect sizes of R<sup>2</sup> [59]. Thus, we conclude our model has a good overall <sup>fi</sup>t and incorporates a large effect size.

Finally, we determine the moderating effect of experience in using the system by dividing the sample above and below the mean (2.4 years), and calculating a pooled error term t-test. The results (see Table 4) show signi<sup>fi</sup>cant differences in the path coef<sup>fi</sup>cients for ENBF–PU and PEOU–PU. There are also marginal differences in CSP– ENBF and EFF–ENBF. Overall, the PLS analysis shows distinct differences. In particular, for inexperienced users (Fig. 4a) the enabling factors CSP and EFF drive an understanding of PU and PEOU, with ATT and COM being determined, albeit weakly, by both PU and PEOU. For experienced users (Fig. 4b) ENBF–PU is no longer signi<sup>fi</sup>cant, while PEOU no longer determines USE, ATT, or COM, but now acts through PU.

Discriminant reliability of constructs.  
Note: Square-root of the AVE on the diagonals (in bold), inter-construct correlations within the columns.

<table><tr><td></td><td>ACC</td><td>ATT</td><td>CNT</td><td>COM</td><td>CSP</td><td>EFF</td><td>FMT</td><td>PEOU</td><td>PU</td><td>TIM</td><td>USE</td></tr><tr><td>ACC</td><td>0.80</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ATT</td><td>0.23</td><td>0.80</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CNT</td><td>0.40</td><td>0.33</td><td>0.77</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>COM</td><td>0.23</td><td>0.41</td><td>0.34</td><td>0.87</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CSP</td><td>0.14</td><td>0.41</td><td>0.29</td><td>0.35</td><td>0.85</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EFF</td><td>0.12</td><td>0.33</td><td>0.17</td><td>0.29</td><td>0.20</td><td>0.84</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>FMT</td><td>0.34</td><td>0.38</td><td>0.41</td><td>0.37</td><td>0.37</td><td>0.28</td><td>0.86</td><td></td><td></td><td></td><td></td></tr><tr><td>PEOU</td><td>0.19</td><td>0.36</td><td>0.29</td><td>0.43</td><td>0.32</td><td>0.62</td><td>0.40</td><td>0.75</td><td></td><td></td><td></td></tr><tr><td>PU</td><td>0.30</td><td>0.43</td><td>0.42</td><td>0.56</td><td>0.29</td><td>0.35</td><td>0.48</td><td>0.37</td><td>0.82</td><td></td><td></td></tr><tr><td>TIM</td><td>0.33</td><td>0.46</td><td>0.43</td><td>0.45</td><td>0.32</td><td>0.25</td><td>0.45</td><td>0.34</td><td>0.42</td><td>0.81</td><td></td></tr><tr><td>USE</td><td>0.04</td><td>-0.02</td><td>0.06</td><td>0.03</td><td>0.06</td><td>-0.12</td><td>0.13</td><td>-0.13</td><td>-0.01</td><td>0.14</td><td>0.71</td></tr></table>

![](/api/attachments/Q2Y8XVHW/fulltext/images/311ed9cbb09cbc0e40de7271b4a604d308350f8279d640eef0fb8bb922f72ff8.jpg)  
Fig. 3. Results of PLS analysis. Note: \*p b0.05, \*\*p b 0.01, \*\*\*p b0.001.

## 6. Discussion

For a system that is mandatory the level of system use (USE) was not signi<sup>fi</sup>cantly determined by attitude towards using (ATT), compatibility (COM), perceived usefulness (PU), or ease of use (PEOU). This suggests that measuring USE will tell us nothing about what drives a user's perception of system success. While ATT could be used as a surrogate for IT acceptance, compatibility, de<sup>fi</sup>ned in terms of the <sup>fi</sup>t the system has with how the user likes to work, is more strongly determined by PU and PEOU. The PEOU–COM path suggests the user-interface will impact a user's perception of the compatibility of the system. However, PU is clearly the dominant factor, as it should be, given that the <sup>fi</sup>rst priority of any information system is to provide the functionality required to support the user in their job. If a system is not perceived as useful it cannot be deemed a success.

The quality of the information provided by the system (INFQ) and the extent to which the user feels they have the technical support or skills to make use of the system (ENBF) are both signi<sup>fi</sup>cant, and strongly in<sup>fl</sup>uence PU and PEOU. The moderating effect of experience shows how the role of PEOU changes. For relatively inexperienced users almost every pathway of the model is signi<sup>fi</sup>cant (see again

## Table 4

Results of pooled error term t-test.  
Note: p-Level +pb0.10, \*pb0.05, \*\*pb0.01, and \*\*\*pb0.001.

<table><tr><td rowspan="2" colspan="2">Path</td><td colspan="4">Experience</td><td rowspan="3">t-Statistic</td><td rowspan="3">p-Level</td></tr><tr><td colspan="2">Low (&lt;2.4 years)</td><td colspan="2">High (&gt;2.4 years)</td></tr><tr><td>From</td><td>To</td><td>Coefficient</td><td>SE</td><td>Coefficient</td><td>SE</td></tr><tr><td>ACC</td><td>INFQ</td><td>0.24</td><td>0.04</td><td>0.19</td><td>0.04</td><td>0.80</td><td></td></tr><tr><td>CNT</td><td>INFQ</td><td>0.50</td><td>0.05</td><td>0.44</td><td>0.04</td><td>0.92</td><td></td></tr><tr><td>CSP</td><td>ENBF</td><td>0.45</td><td>0.09</td><td>0.65</td><td>0.07</td><td>-1.78</td><td>+</td></tr><tr><td>EFF</td><td>ENBF</td><td>0.80</td><td>0.06</td><td>0.63</td><td>0.08</td><td>1.68</td><td>+</td></tr><tr><td>ENBF</td><td>PU</td><td>0.47</td><td>0.08</td><td>-0.11</td><td>0.08</td><td>5.00</td><td>***</td></tr><tr><td>ENBF</td><td>PEOU</td><td>0.62</td><td>0.07</td><td>0.48</td><td>0.09</td><td>1.21</td><td></td></tr><tr><td>FMT</td><td>INFQ</td><td>0.35</td><td>0.03</td><td>0.35</td><td>0.04</td><td>-0.04</td><td></td></tr><tr><td>INFQ</td><td>PU</td><td>0.43</td><td>0.08</td><td>0.48</td><td>0.12</td><td>-0.34</td><td></td></tr><tr><td>INFQ</td><td>PEOU</td><td>0.14</td><td>0.07</td><td>0.21</td><td>0.10</td><td>-0.64</td><td></td></tr><tr><td>PEOU</td><td>PU</td><td>-0.16</td><td>0.09</td><td>0.32</td><td>0.12</td><td>-3.03</td><td>**</td></tr><tr><td>PEOU</td><td>USE</td><td>-0.22</td><td>0.10</td><td>-0.07</td><td>0.14</td><td>-0.94</td><td></td></tr><tr><td>PEOU</td><td>ATT</td><td>0.23</td><td>0.09</td><td>0.18</td><td>0.08</td><td>0.45</td><td></td></tr><tr><td>PEOU</td><td>COM</td><td>0.31</td><td>0.11</td><td>0.18</td><td>0.08</td><td>0.91</td><td></td></tr><tr><td>PU</td><td>USE</td><td>0.05</td><td>0.12</td><td>0.12</td><td>0.20</td><td>-0.29</td><td></td></tr><tr><td>PU</td><td>ATT</td><td>0.32</td><td>0.08</td><td>0.40</td><td>0.11</td><td>-0.61</td><td></td></tr><tr><td>PU</td><td>COM</td><td>0.38</td><td>0.10</td><td>0.55</td><td>0.08</td><td>-1.34</td><td></td></tr><tr><td>TIM</td><td>INFQ</td><td>0.25</td><td>0.04</td><td>0.31</td><td>0.03</td><td>-1.10</td><td></td></tr></table>

Fig. 4a). For more experienced users, INFQ, PU, and COM become the dominant issues (see again Fig. 4b). It would appear that as users begin the process of IT acceptance, the initial training and support they receive enables them to think about what the system can do and how it affects all aspects of their work. After a period of time (in this case, 2.4 years), the value of the system has been established and differences in attitude or perceived compatibility are explained in terms of the actual usefulness of the system.

## 6.1. Theoretical contributions

From a theoretical point of view, the model presented here makes a number of important theoretical contributions. First, and foremost, we incorporate elements from a number of well-established models of IT acceptance, diffusion of innovation, and user satisfaction. We build upon the intuitively compelling argument put forward by TAM that the key to understanding IT acceptance is usefulness and ease of use. Satisfying the information needs of the user in terms of accuracy, content, format, and timeliness, drives primarily the perceived usefulness of the system, while providing computing support and boosting self-ef<sup>fi</sup>cacy enable higher levels of pro<sup>fi</sup>ciency in the user. While attitude towards using and levels of system use have some role to play, especially for less experienced users, compatibility is the key dependent variable.

The strength of the usefulness and ease of use constructs again demonstrates the intuitive power of these two constructs. In line with previous research, we posit PU and PEOU to be antecedent to the endogenous variables. In this case, we have a behavioral measure (USE) and two attitudinal measures of IT acceptance (ATT and COM). A meta-analysis of TAM studies suggests that PU and PEOU have path coef<sup>fi</sup>cients on the endogenous variable of around 0.49 and 0.18, respectively [33]. The coef<sup>fi</sup>cients derived for COM in this study (0.46 and 0.26) are within this range and provide further support for the assertion that usefulness is the most important factor, with ease of use providing an additional, although weaker, driving force.

One of the criticisms of TAM is that researchers tend to focus on moderating and mediating variables of PU and PEOU, without exploring the characteristics of the IT artifact itself [2]. Within our model, the second-order constructs are a critical part of understanding how antecedent factors drive perceptions of usefulness and ease of use. If the second-order construct is deleted from our model and <sup>fi</sup>rstorder constructs are related directly to usefulness and ease of use, all path coef<sup>fi</sup>cients drop below 0.2, except for format (0.28) and ef<sup>fi</sup>- cacy (0.59). This suggests that models investigating the impact of <sup>fi</sup>rst-order constructs on TAM might be underestimating their contribution. By incorporating a second-order construct that group factors under their expected rubric of information quality and enabling factors, a more signi<sup>fi</sup>cant relationship is detected.

(b) High experience (more than 2.4 years)  
(a) Low experience (less than 2.4 years)  
![](/api/attachments/Q2Y8XVHW/fulltext/images/5d7a43dc4e00c3b642af08b6b39059121de95ecedad372c20bc7bde16d20d4db.jpg)  
Fig. 4. Moderating effect of system experience. Note: Signi<sup>fi</sup>cant paths (coef<sup>fi</sup>cients above .2) shown in bold. Actual path coef<sup>fi</sup>cients shown in Table 4.

## 6.2. Practical contributions

The clinical management system (CMS) assessed as part of this study underpins all the decision-making throughout the hospital. Physicians use the results of clinical tests to make evidence-based diagnoses, while nurses use the system to determine care procedures for each patient. By de<sup>fi</sup>ning compatibility as the measure of IT acceptance we are attempting to resolve the problem of how to overcome resistance towards the adoption of IT, an effect often found among healthcare workers. Measures of system use provide little insight into how the system is perceived. Rather, the system must be designed to take into account how the system will <sup>fi</sup>t with current work practices, with low compatibility likely to result in low levels of use, feelings of frustration, and potentially lead to aggressive resistance. For instance, the decision of nurses to use mobile workstations depended on a <sup>fi</sup>t with preferred work processes [30]. Compatibility provides the social context in which the technology is being applied, which can have a strong in<sup>fl</sup>uence on the success of technological innovations [43].

The model suggests that in order to promote a high level of perceived compatibility, managers need to focus on the quality of the information provided by the system and provide adequate computer support and training in order to help users apply the technology as ef-<sup>fi</sup>ciently as possible. Ensuring the system contains the right information to support the user in their work is a perennial issue. In this case, our de<sup>fi</sup>nition of INFQ, derived from the EUCS model, provides a check-list of factors that can be used to assess whether the system is providing information that is complete (CNT) and presented in a way that is easy to understand (FMT), timely (TIM), and accurate (ACC). This checklist seems to neatly de<sup>fi</sup>ne the minimum requirements of any successful system.

Even if the system contains the right information, optimizing the bene<sup>fi</sup>t of the system will depend on blending the right level of computing support (CSP) for the skill level of the user (EFF). In other words, the amount of computing support needed is likely to vary with the skill of the user. For general support systems, such as the CMS studied here, a wide range of skill levels can be assumed, and so, the IT department must provide basic to expert training to match the needs of the user. For instance, 62% of physicians reported using the CMS for both data input and retrieval, compared to 24% for nurses, although nurses were signi<sup>fi</sup>cantly more experienced in using the system than physicians (2.5 versus 1.7 years, pb.001). Perhaps critical to the adoption of IT in healthcare, the integration of IT in the network of healthcare providers is signi<sup>fi</sup>cantly related to performance, in terms of reducing mortality rates and admissions [51], while skillful “super users” have been found to have a signi<sup>fi</sup>cant effect on the overall performance of healthcare teams [31].

Sub-sets of the model can also be applied at various stages of system development to ensure the right system is being developed. This would allow a longitudinal assessment of IT acceptance to be conducted that expands as the system develops. For instance, when the system is in the requirements stage issues of information quality and perceived usefulness can be assessed. When a prototype is developed or during the user acceptance/<sup>fi</sup>eld testing phase, the ease of use and compatibility constructs can be added, while an operational system would allow the remaining enabling factors to be assessed. Changes in perception of the system can also be measured over time, allowing evolving needs and perceptions to be taken into account. More importantly, the INFQ and ENBF constructs would provide clues to what is going wrong, and what system or organizational changes are needed to ensure the success of the system.

## 6.3. Further work

A number of areas of further research present themselves. First, we would recommend exploring the four INFQ factors to ensure they do indeed provide a concise de<sup>fi</sup>nition of system characteristics related to the successful adoption of an information system. Given that 82% of respondents use the CMS for data retrieval we can surmise that a clear presentation of the information (i.e., CNT and FMT) is of the utmost importance. That is not to say ACC and TIM are not important, rather, respondents may not be able to give a de<sup>fi</sup>nitive answer on the accuracy or timeliness of the information entered by others. A data-strong system, such as the CMS system studied here, might favor CNT and FMT, while a processing-strong system, such as a medical diagnostic system, might raise the importance of ACC and TIM. By applying the model across other systems we can determine whether the relatively weak in<sup>fl</sup>uence of ACC and TIM is a function of the type of user, or possibly an indication of the type of system being assessed.

Second, although we de<sup>fi</sup>ne two factors as part of our ENBF construct, we do recognize that additional factors could be added. More importantly, we feel the ENBF construct lays a foundation for an increased assessment of the socio-technical problems inherent in introducing technology into an organization. Socio-technical issues include the demands of the technology and the social forces that promote or hinder its acceptance and use [36]. For instance, a project to integrate medical data across sites encountered resistance from users when an early design decision attempted to develop a “one size <sup>fi</sup>ts all” data model, an approach that failed to account for the local context in which data is collected, interpreted, and used [52].

## 6.4. Limitations

As with many other studies there were problems with the measurement of USE. For the sample as a whole the loadings were relatively low (0.61 and above), although all three items were signi<sup>fi</sup>cant (pb0.05), and removing any of the items did not affect the overall results. Others have suggested that a better threshold for item loadings is 0.7, but items should be considered for removal only if loadings fall below 0.4 and their removal improves the composite reliability above the required threshold (0.7) [24]. The loading for USE1 fell to −0.17 for the experienced group while the composite reliability for the USE construct was 0.47. Removing the USE1 item raised the composite reliability to 0.77, but these changes did not affect the overall results.

Furthermore, while the response rate was good, our sample was overwhelmingly nursing staff, which may limit the generalizability of our results. A sample targeting physicians and allied health workers, who may have different information needs and different levels of computing support and abilities, may produce different results. We also concede that a better de<sup>fi</sup>nition of use may have produced a signi<sup>fi</sup>cant relationship between usefulness, ease of use, and compatibility. Finally, we did not collect demographic data, such as age, gender, job title, department, etc., principally to reinforce the promise of anonymity. By not collecting such data we rule out testing further moderating relationships. Again, the decision was motivated by a desire to ensure the highest possible response rate.

## 7. Conclusion

We developed a concise model of IT acceptance that took into account many of the important factors from the technology acceptance (TAM), end-user computing satisfaction (EUCS), and diffusion of innovation literature (COM). The most important factors in IT acceptance, we suggest, derive from a perception of the information quality provided by the system and individual enabling factors, such as computing support and ef<sup>fi</sup>cacy. These constructs motivate a perception of the usefulness and ease of use, which in turn, drives an understanding of how the system <sup>fi</sup>ts with one's preferred work practices. As expected, levels of use are not signi<sup>fi</sup>cantly related to these factors. Rather, we de<sup>fi</sup>ne IT acceptance in terms of compatibility with the way the user likes to work. Further elaboration of the INFQ and ENBF factors will provide a richer picture of what underpins the success of any information system, while the model also has the potential to be applied at different stages of the development process, allowing a longitudinal assessment of <sup>fi</sup>t. These are important features, we suggest, of any model of IT acceptance.

## Appendix A. Survey items

Note. For all constructs except USE, the scale for items was 1- Strongly Agree to 5-Strongly Disagree, along with a Don't Know/ Can't Answer option which was coded as a missing response.

ACC (Accuracy). The extent to which the user believes the system is free of errors [23]. Added ACC3.

ACC1: The CMS is accurate.

ACC2: I am satis<sup>fi</sup>ed with the accuracy of the CMS.

ACC3: Overall, I believe the information provided by the CMS is free of errors.

ATT (Attitude). The overall feeling the user has towards using the CMS [46]. Semantic differential transformed to Likert scale.

All things considered, in using the system I am:

ATT1: Pleased.

ATT2: Happy.

ATT3: Frustrated. (Reversed)

ATT4: Satis<sup>fi</sup>ed.

CNT (Content). The extent to which the user believes the system provides all the information needed to carry out their work [23]. Added CNT5.

CNT1: The CMS provides the precise information I need.

CNT2: The information content meets my needs.

CNT3: The CMS provides reports that are just about what I need.

CNT4: The CMS provides suf<sup>fi</sup>cient information.

CNT5: Overall, the information content meets my needs.

COM (Compatibility). The extent to which the user believes the system is consistent with their existing values, needs and past experiences [43].

COM1: I think that using the CMS <sup>fi</sup>ts well with the way I like to work.

COM2: Using the CMS <sup>fi</sup>ts into my work style.

COM3: Overall, using the CMS is compatible with all aspects of my work.

CSP (Computing Support). The extent to which the user believes adequate computing support been given in the use of the system [28]. Added CSP4.

CSP1: A speci<sup>fi</sup>c person (or group) is available for assistance with hardware dif<sup>fi</sup>culties.

CSP2: A speci<sup>fi</sup>c person (or group) is available for assistance with system dif<sup>fi</sup>culties.

CSP3: Specialized instruction and education concerning the CMS is available to me.

CSP4: Overall, I have been given adequate support in the use of the CMS.

EFF (Ef<sup>fi</sup>cacy). The extent to which the user believes they have the capability to use the system [46]. Added EFF4.

EFF1: I feel comfortable using the CMS on my own.

EFF2: I can easily operate the CMS on my own.

EFF3: I am able to use the CMS, even if there was no one around to show me how to use it.

EFF4: Overall, I am con<sup>fi</sup>dent in my ability to use the CMS.

FMT (Format). The extent to which the user believes the output of the system is easy to read and understand [23].

FMT1: The layout of the screen makes it easy for me to read the in formation presented.

FMT2: The information is clear.

FMT3: Overall, I think the output is presented in a useful format.

PEOU (Perceived Ease of Use). The extent to which the user believes that using the system is free of effort [17].

PEOU1: Learning to operate the CMS is easy for me.

PEOU2: I <sup>fi</sup>nd it easy to get the CMS to do what I want it to do.

PEOU3: My interaction with the CMS is clear and understandable.

PEOU4: I <sup>fi</sup>nd the CMS to be <sup>fl</sup>exible to interact with.

PEOU5: It is easy for me to become skillful at using the CMS.

PEOU6: Overall, I <sup>fi</sup>nd the CMS easy to use.

PU (Perceived Usefulness). The extent to which the user believes that using the system will enhance their job performance [17].

PU1: Using the CMS in my job enables me to accomplish tasks more quickly.

PU2: Using the CMS improves my job performance.

PU3: Using the CMS enables me to increase my productivity.

PU4: Using the CMS enhances my effectiveness on the job.

PU5: Using the CMS makes it easier to do my job.

PU6: Overall, I <sup>fi</sup>nd the CMS useful in my job.

TIM (Timeliness). The extent to which the user believes the system provides the information they need when they need it [23]. Added TIM3.

TIM1: I get the information I need in time.

TIM2: The CMS provides up-to-date information.

TIM3: Overall, the information I need is always available in the CMS when I need it.

USE (System Use). The extent to which the user believes they make use of the system as part of their work [28]. USE1 added.

USE1: Which functions of the CMS do you use? Scale: (a) ADT (admission/discharge/transfer); (b) OP (out-patient appointment management); (c) diagnosis and procedure coding; (d) medication order entry; (e) laboratory results and reporting; and (f) clinical records.

USE2: On average, how often do you use the CMS? Scale: (a) less than once a month; (b) once a month; (c) a few times a month; (d) a few times a week; (e) about once a day; and (f) several times a day.

USE3: On average, how much time do you spend per day using the CMS? Scale: (a) almost never; (b) less than 1/2 h; (c) From 1/2 h to 1 h; (d) 1–2 h; (e) 2–3 h; and (f) more than 3 h.

## References

[1] R.P. Bagozzi, The legacy of the technology acceptance model and a proposal for a paradigm shift, Journal of the Association for Information Systems 8 (4) (2007) 244–254.

[2] I. Benbasat, H. Barki, Quo Vadis, TAM? Journal of the Association for Information Systems 8 (4) (2007) 211–218.

[3] A. Bhattacherjee, Understanding information systems continuance: an expectation– con<sup>fi</sup>rmation model, MIS Quarterly 25 (3) (2001) 351–370.

[4] A. Bhattacherjee, N. Hikmet, Physicians' resistance toward healthcare information technology: a theoretical model and empirical test, European Journal of Informa tion Systems 16 (6) (2007) 725–737.

[5] A. Bhattacherjee, G. Premkumar, Understanding changes in belief and attitude toward information technology usage: a theoretical model and longitudinal test, MIS Quarterly 28 (2) (2004) 229–254.

[6] D. Blumenthal, J.P. Glaser, Information technology comes to medicine, The New England Journal of Medicine 356 (24) (2007) 2527–2534.

[7] S.A. Brown, A.P. Massey, M.M. Montoya-Weiss, J.R. Burkman, Do I really have to? User acceptance of mandated technology, European Journal of Information Systems 11 (4) (2002) 283–295.

[8] A. Burton-Jones, D.W. Straub, Reconceptualizing system usage: an approach and empirical test, Information Systems Research 17 (3) (2006) 228–246.

[9] B. Chaudhry, J. Wang, S. Wu, M. Maglione, W. Mojica, E. Roth, S.C. Morton, P.G. Shekelle, Systematic review: impact of health information technology on quality, ef<sup>fi</sup>ciency, and costs of medical care, Annals of Internal Medicine 144 (10) (2006) 742–752.

[10] W.W. Chin, Issues and opinion on structural equation modeling, MIS Quarterly 22 (1) (1998) vii–xvi.

[11] W.W. Chin, P.R. Newsted, Structural equation modeling analysis with small samples using partial least squares, in: R.H. Hoyle (Ed.), Statistical Strategies for Small Sample Research, Sage Publications, Thousand Oaks, CA, 1999, pp. 307–341

[12] W.W. Chin, R.A. Peterson, S.P. Brown, Structural equation modeling in marketing: some practical reminders, Journal of Marketing Theory and Practice 16 (4) (2008) 287–298.

[13] D.R. Compeau, C.A. Higgins, Computer self-ef<sup>fi</sup>cacy: development of a measure and initial test, MIS Quarterly 19 (2) (1995) 189–211.

[14] D. Compeau, C.A. Higgins, S. Huff, Social cognitive theory and individual reactions to computing technology: a longitudinal study, MIS Quarterly 23 (2) (1999) 145–158

[15] C.M. Cusack, E. Pan, J.M. Hook, A. Vincent, D.C. Kaelber, D.W. Bates, B. Middleton, The Value of Provider-to-Provider Telehealth Technologies Center for Information Technology Leadership Charleston NC 2007.

[16] E.J. Davidson, W.G. Chismar, The interaction of institutionally triggered and technology-triggered social structure change: an investigation of computerized physician order entry, MIS Quarterly 31 (4) (2007) 739–758.

[17] F.D. Davis, Perceived usefulness, perceived ease of use and user acceptance of information technology, MIS Quarterly 13 (3) (1989) 318–339.

[18] F.D. Davis, User acceptance of information technology: system characteristics, user perceptions, and behavioral impacts, International Journal of Man Machine Studies 38 (3) (1993) 475–487.

[19] F.D. Davis, R.P. Bagozzi, P.R. Warshaw, User acceptance of computer technology: a comparison of two theoretical models, Management Science 35 (8) (1989) 982–1003.

[20] C.M. DesRoches, E.G. Campbell, S.R. Rao, K. Donelan, T.G. Ferris, A. Jha, R. Kaushal, D.E. Leyy S. Rosenbaum A.E. Shields D. Blumenthal Electronic health records in ambulatory care — a national survey of physicians, The New England Journal of Medicine 359 (1) (2008) 50–60.

[21] W.J. Doll, G. Torkzadeh, The measurement of end-user computing satisfaction, MIS Quarterly 12 (2) (1988) 259–274.

[22] W.J. Doll, X. Deng, T.S. Raghunathan, G. Torkzadeh, W. Xia, The meaning and measurement of user satisfaction: a multigroup invariance analysis of the enduser computing satisfaction instrument, Journal of Management Information Systems 21 (1) (2004) 227–262

[23] M. Fishbein, I. Ajzen, Belief, Attitude, Intention and Behavior: An Introduction to Theory and Research, Addison-Wesley, Reading, MA, 1975.

[24] J.F. Hair, C.M. Ringle, M. Sarstedt, PLS-SEM: indeed a silver bullet, Journal of Marketing Theory and Practice 19 (2) (2011) 139–151.

[25] P.J. Hu, P.Y.K. Chau, O.R. Liu Sheng, K.Y. Tam, Examining the technology acceptance model using physician acceptance of telemedicine technology, Journal of Management Information Systems 16 (2) (1999) 91–112.

[26] M. Igbaria, N. Zinatelli, P. Cragg, A.L.M. Cavaye, Personal computing acceptance factors in small <sup>fi</sup>rms: a structural equation model, MIS Quarterly 21 (3) (1997) 279–305.

[27] V. Ilie, C. Van Slyke, M.A. Parikh, J.F. Courtney, Paper versus electronic medical records: the effects of access on physicians' decisions to use complex information technologies, Decision Sciences 40 (2) (2009) 213–241.

[28] T.B. Jensen, M. Aanestad, Hospitality and hostility in hospitals: a case study of an EPR adoption among surgeons, European Journal of Information Systems 16 (6) (2007) 672–680.

[29] A.K. Jha, C.M. DesRoches, E.G. Campbell, K. Donelan, S.R. Rao, T.G. Ferris, A. Shields, S. Rosenbaum, D. Blumenthal, Use of electronic health records in U.S. hospitals, The New England Journal of Medicine 360 (16) (2009) 1628–1638.

[30] I. Junglas, C. Abraham, B. Ives, Mobile technology at the frontlines of patient care: understanding <sup>fi</sup>t and human drives in utilization decisions and performance, Decision Support Systems 46 (3) (2009) 634–647.

[31] G.C. Kane, S.P. Borgatti, Centrality-IS pro<sup>fi</sup>ciency alignment and workgroup performance, MIS Quarterly 35 (4) (2011) 1063–1078.

[32] E. Karahanna, R. Agarwal, C. Angst, Reconceptualizing compatibility beliefs in technology acceptance, MIS Quarterly 30 (4) (2006) 781–804.

[33] W.R. King, J. He, A meta-analysis of the technology acceptance model, Information Management 43 (6) (2006) 740–755.

[34] R. Klein, An empirical examination of patient–physician portal acceptance, European Journal of Information Systems 16 (6) (2007) 751–760.

[35] L.T. Kohn, J.M. Corrigan, M.S. Donaldson, To Err is Human: Building a Safer Health System, National Academy Press, Washington, DC, 2000.

[36] R. Lamb, R. Kling, Reconceptualizing users as social actors in information systems research, MIS Quarterly 27 (2) (2003) 197–235.

[37] L. Lapointe, S. Rivard, A multilevel model of resistance to information technology implementation, MIS Quarterly 29 (3) (2005) 461–491

[38] Y. Lee, K.A. Kozar, R.T. Larsen, The technology acceptance model: past, present, and the future Communications of the AIS 12 (3) (2003) 752-780

[39] P. Legris, J. Ingham, P. Collerette, Why do people use information technology? A critical review of the technology acceptance model, Information Management 40 (3) (2003) 191–204.

[40] L. Liu, Q. Ma, The impact of service level on the acceptance of application service oriented medical records, Information Management 42 (8) (2005) 1121–1135.

[41] Q. Ma, L. Liu, The technology acceptance model: a meta-analysis of empirical <sup>fi</sup>ndings, Journal of End User Computing 16 (1) (2004) 59–72.

[42] G. Moore, I. Benbasat, Development of an instrument to measure the perceptions of adopting an information technology innovation, Information Systems Research 2 (3) (1991) 192–222.

[43] F.C. Payton, G. Pare, C.M. Le Rouge, M. Reddy, Health care IT: process, people, patients and interdisciplinary considerations, Journal of the Association for Information Systems 12 (2) (2011) i–xiii (Article 4).

[44] C.M. Ringle, S. Wende, A. Will, Smart PLS 2.0 (Beta), University of Hamburg, Germany, 2005 (available at: http://www.smartpls.de).

[45] S. Rivard, L. Lapointe, A. Kappos, An organizational culture-based theory of clinical information systems implementation in hospitals, Journal of the Association for Information Systems 12 (2) (2011) 123–162 (Article 3).

[46] R. Sabherwal, A. Jeyaraj, C. Chowa, Information system success: individual and organizational determinants, Management Science 52 (12) (2006) 1849–1864.

[47] Y. Sun, A. Bhattacherjee, Q. Ma, Extending technology usage to work settings: the role of perceived work compatibility in ERP implementation, Information Management 46 (6) (2009) 351–356.

[48] S. Taylor, P. Todd, Understanding information technology usage: a test of competing models, Information Systems Research 6 (2) (1995) 144–176.

[49] M. Tenenhaus, V. Esposito Vinzi, Y.-M. Chatelin, C. Lauro, PLS path modeling, Computational Statistics and Data Analysis 48 (1) (2005) 159–205.

[50] T.S.H. Teo, B. Men, Knowledge portals in Chinese consulting <sup>fi</sup>rms: a tasktechnology <sup>fi</sup>t perspective, European Journal of Information Systems 17 (6) (2008) 557–574.

[51] E.H. Thrasher, C.W. Craighead, T.A. Byrd, An empirical investigation of integration in healthcare alliance networks, Decision Support Systems 50 (1) (2010) 116–127.

[52] J. Ure, R. Procter, Y.-W. Lin, M. Hartswood, S. Anderson, S. Lloyd, J. Wardlaw, H. Gonzalez-Velez K. Ho The development of data infrastructures for e-health: a

socio-technical perspective, Journal of the Association for Information Systems 10 (5) (2009) 415–429.

[53] V. Venkatesh, H. Bala, Technology acceptance model 3 and a research agenda on interventions, Decision Sciences 39 (2) (2008) 273–315.

[54] V. Venkatesh, F.D. Davis, A model of the antecedents of perceived ease of use: development and test, Decision Sciences 27 (3) (1996) 451–481.

[55] V. Venkatesh, F.D. Davis, A theoretical extension of the technology acceptance model: four longitudinal <sup>fi</sup>eld studies, Management Science 46 (2) (2000) 186–204.

[56] V. Venkatesh, M.G. Morris, Why don't men ever stop and ask for directions? Gender, social in<sup>fl</sup>uence, and their role in technology acceptance and usage behavior, MIS Quarterly 24 (1) (2000) 115–139.

[57] V. Venkatesh, M.G. Morris, G.B. Davis, F.D. Davis, User acceptance of information technology: toward a uni<sup>fi</sup>ed view, MIS Quarterly 27 (3) (2003) 425–478.

[58] R.W. Wang, D.M. Strong, Beyond accuracy: what data quality means to data consumers, Journal of Management Information Systems 12 (4) (1996) 5–33.

[59] M. Wetzels, G. Odekerken-Schröder, C. van Oppen, Using PLS path modeling for assessing hierarchical construct models: guidelines and empirical illustration, MIS Quarterly 33 (1) (2009) 177–195.

[60] B.H. Wixom, P.A. Todd, A theoretical integration of user satisfaction and technology acceptance, Information Systems Research 16 (1) (2005) 85–102.

[61] J. Wu, A. Lederer, A meta-analysis of the role of environment-based voluntariness in information technology acceptance, MIS Quarterly 33 (2) (2009) 419–432.

[62] I.-L. Wu, J.-Y. Li, C.-Y. Fu, The adoption of mobile healthcare by hospital's professionals: an integrative perspective, Decision Support Systems 51 (3) (2011) 587–596.

[63] H.-D. Yang, Y. Yoo, It's all about attitude: revisiting the technology acceptance model, Decision Support Systems 38 (1) (2004) 19–31.

[64] A.K. Yarbrough, T.B. Smith, Technology acceptance among physicians: a new take on TAM, Medical Care Research and Review 64 (6) (2007) 650–672.

[65] M.Y. Yi, J.D. Jackson, J.S. Park, J.C. Probst, Understanding information technology acceptance by individual professionals: towards an integrative view, Information Management 43 (3) (2006) 350–363.

Trevor T. Moores is a Professor of Information Systems at ESSEC Business School Cergy-Pontoise, France. He received his B.A. (Hons) in Combined Studies (Arts) majoring in Philosophy and Psychology from Sunderland Polytechnic, an M.Sc. in Intelligent Knowledge Based Systems from the University of Essex, and a Ph.D. in Information Systems from the University of Aston. His research interests include software piracy, IS ethics, software measurement, IT management, and issues of online trust. His work has appeared in MIS Quarterly, Communications of the ACM, Journal of Business Ethics, DATA BASE, the European Journal of Information Systems, IEEE Transactions on Knowledge Engineering, Information & Management, and others
