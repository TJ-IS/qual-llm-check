---
otero_id: 15444
otero_key: "EJR9P5A3"
title: "Investigating Physicians' Compliance with Drug Prescription Notifications"
authors: "Tsipi Heart; Allon Zucker; Yisrael Parmet; Joseph Pliskin; Nava Pliskin"
year: "2011"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00262"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
3-30-2011

# Investigating Physicians' Compliance with Drug Prescription Notifications

Tsipi Heart , heart@bgu.ac.il

Allon Zucker , allon@roshtov.com

Yisrael Parmet , iparmet@bgu.ac.il

Joseph S. Pliskin , jpliskin@bgu.ac.il

Nava Pliskin , pliskinn@bgu.ac.il

Follow this and additional works at: https://aisel.aisnet.org/jais

Recommended Citation Heart, Tsipi; Zucker, Allon; Parmet, Yisrael; Pliskin, Joseph S.; and Pliskin, Nava (2011) "Investigating Physicians' Compliance with Drug Prescription Notifications," , 12(3), . DOI: 10.17705/1jais.00262 Available at: https://aisel.aisnet.org/jais/vol12/iss3/3

# Journal of the Asşociation for Information Systems JAIS

Special Issue

# Investigating Physicians' Compliance with Drug Prescription Notifications

Tsipi Heart Ben-Gurion University of the Negev heart@bgu.ac.il

Yisrael Parmet Ben-Gurion University of the Negev iparmet@bgu.ac.il

Nava Pliskin Ben-Gurion University of the Negev pliskinn@bgu.ac.il

Allon Zuker Roshtov Software Inc. allon@roshtov.com

Joseph S Pliskin Ben-Gurion University of the Negev jpliskin@bgu.ac.il

## Abstract

The objective of this study was to investigate physicians' compliance with recommendations for drug substitutes embedded within an electronic medical record, to assess factors affecting compliance, and to evaluate associated cost savings. An exploratory study of all physicians in all clinics operated by a large health maintenance organization (HMO) was conducted using a transparent computerized agent that collected 1.21 million prescriptions prescribed by 647 physicians. Compliance with HMO recommendations for substitute drugs reached a 70 percent rate. Substitute type, whether generic or therapeutic, was found to be the most significant factor affecting compliance, with physician workload and age second and third in effect magnitude, respectively. Compliance was found to be non-automatic and selective, following a thoughtful cognitive process. The HMO realized at least a 4 percent reduction in costs for prescribed drugs as a result of compliance with substitute recommendations. The results can be interpreted via the lens of Organizational Justice Theory, assuming that the broad compliance with generic substitutes was driven by perception of just procedures, whereas there was no such perception in the case of therapeutic substitutes. While more research is warranted for investigating the motivations driving physicians' compliance, we strongly feel that the results can be generalized to other HMOs and healthcare settings.

Keywords: Health Care IT (Special Issue), Electronic Medical Record, Physician Compliance, Drug Cost Containment, Organizational Justice Theory.

\* Fay Cobb Payton, Guy Paré, Cynthia LeRouge, and Madhu Reddy were the accepting guest editors. This article was submitted on 6th June 2010 and went through two revisions.

# Investigating Physicians' Compliance with Drug Prescription Notifications

## 1. Introduction

Healthcare costs are escalating world-wide. According to a 2006 report of the Organization for Economic and Co-operation Development (OECD) (figures for later years are yet to be published), national healthcare expenditures ranged from 15.3 percent (U.S.) to 6 percent (Mexico, Korea, Poland) of countries’ Gross Domestic Product (GDP). Annual growth rates between the years 2000 and 2006 were above 10 percent in several countries, surpassing the growth of the respective economies (OECD, 2007; Schur, Berk, & Yegian, 2004). Spending on prescription drugs in the US, for example, increased by 14 percent between 2004 and 2007 (Daly, 2007), and drug expenditures exceeded 12 percent of the total healthcare expenditure in 2006 (KFF, 2007).

Interventions used by insurers to contain drug costs frequently require physicians' compliance. When compliance is not forthcoming, cost containment is not achieved. In other cases, achievement of cost containment has resulted in a decrease in quality of care (Shamliyan, Duval, Du, & Kane, 2008). While electronic medical records systems (EMR) have been advocated as a means for meeting these cost and quality challenges, recent studies have marginally substantiated this assertion (Delpierre et al., 2004; DesRoches et al., 2008; Shamliyan et al., 2008; Wolfstadt et al., 2008). Two obstacles to achieving these goals are physicians' resistance (Piderit, 2000) and their preference to maintain existing behaviors (Coch & French, 1948). In this sense, a compliant behavior has been used as evidence of reduced resistance (Sagie, Elizur, & Greenbaum, 1985), which health maintenance organizations (HMOs) strive to secure in order to achieve enhanced quality of healthcare while containing costs.

Voluntary EMR adoption by independent care providers can be regarded to some degree as compliance with governmental requests (Goldman, 2009) and is believed to enhance healthcare efficiency (Ginsburg, Doherty, Ralston, & Senkeeto, 2008; Matheny et al., 2008; Mongan, Ferris, & Lee, 2008; Reynolds, Harper, Jenner, & Dunne, 2008; Shamliyan et al., 2008; Weber, 2008; Wolfstadt et al., 2008). However, in spite of two decades of efforts, EMR adoption rates are still only around 14 percent of primary care physicians in the US (DesRoches et al., 2008). Among reasons for nonadoption of EMR technology are: questionable return on investment, risks of privacy breach or records unavailability, user interface difficulties, and questionable effectiveness (Blumenthal, 2009; Jha et al., 2009a, 2009b; Kush, Helton, Rockhold, & Hardison, 2008; Martens et al., 2008; Shachak, Hadas-Dayagi, Ziv & Reis, 2009; Vardy, Kayam, & Kitai, 2008). HMOs that have adopted EMRs encounter similar difficulties, confronting internal resistance to use the systems and comply with new organizational processes (Connell & Young, 2007; Jensen & Aanestad, 2007; Reardon & Davidson, 2007; Subramanian et al., 2007).

While the rates of EMR adoption or non-adoption is by now fairly clear, this is not the case for care provider compliance with computerized notifications embedded within implemented EMRs to improve quality of care or reduce costs. Recent studies focusing on the effectiveness of computerized reminders yielded mixed results (Matheny et al., 2008; Sequist et al., 2005), with effectiveness declining over time (Demakis et al., 2000). Most of this research was conducted in institutions where the investigated behavior involved recently implemented systems or experimental environments, hindering the generalizability of the results.

Against this background, the objective of this study was to examine physicians' compliance with a wellestablished intervention to contain costs of prescription drugs without decreasing the quality of care administered by a large HMO. We conducted the study in the normal organizational environment, where we transparently monitored the natural behavior of the physician population employed by the studied HMO in all its clinics. The intervention involved a notification about HMO-recommended substitutes issued to the physician by the drug prescription module of the EMR. We examined the patterns of physicians’ compliance with notifications, both in general and in relation to their demographic traits, as well as the contribution of compliance to containment of drug costs. We employed an exploratory epistemology, hence, we did not attempt to test any hypotheses. Rather, we wanted to examine the actual physicians' behavior and suggest a plausible theoretical explanation for future research.

The strength and importance of this work is in the comprehensiveness of the data, which is rooted in a normal organizational setting, in the rigorous statistical analyses, and in the theoretical and practical implications derived. Furthermore, although the results represent one organization, we are confident in their generalizability and external validity under similar circumstances.

The paper is organized as follows: the next two sections present the background, including review of the literature, description of the study environment, and explanation of the theoretical lens for this paper, followed by the research method. We then present the results, leading to the discussion and conclusions.

## 2. Background

Drug prescription is a primary component of medical care, yet it suffers from quality and cost problems and ineffective response to administrative measures that address both these concerns (Kuperman & Gibson, 2003; Shamliyan et al., 2008). To overcome cost problems, several cost containment measures have been attempted, of which the most common are: (1) administering drug formularies (Huskamp et al., 2005); (2) shifting to generic-drug-only coverage (Patterson et al., 2005); and (3) instituting co-payments (Gibson, Ozminkowski, & Goetzel, 2005). All three measures, however, although successful in achieving cost containment (Huskamp et al., 2003a), are contingent on care providers' compliance with organizational procedures, and can also bear undesirable health consequences (Gibson et al., 2005) when patients, particularly sensitive populations such as elderly patients, deviate from disciplined drug consumption due to financial difficulties (Goldman et al., 2004; Huskamp et al., 2003b; Reed, Brand, Newhouse, Selby, & Hsu, 2008; Steinman, Sands, & Covinsky, 2001).

Prior research about physicians' compliance with various manual or computerized clinical procedures, introduced to increase quality of care, reduce costs, or minimize errors, generally revealed either marginal success or none (Matheny et al., 2008; Sanders & Satyvavolu, 2002; Sequist et al., 2005; Tamblyn et al., 2006).

Physicians' response to clinical reminders can be divided into four behavioral categories: compliance, reliance, spillover, and reactance. Compliance is defined as the tendency to perform an action when a clinical monitor issues an alert; reliance is defined as a tendency to refrain from performing an action when the warning system does not indicate that it is necessary (Meyer, 2004); spillover is defined as "the spread or expansion of responses, activities, or roles from one instance, system, or domain, to another" (Vashitz et al., 2009, p. 318); and reactance (or non-compliance) is defined as "an unpleasant motivational state, in which people react to situations [where] they feel their autonomy is threatened, in ways that reaffirm their freedom or autonomy" (Vashitz et al., 2009, p. 318). Barriers to compliance with clinical reminders identified by prior research include lack of time, poor patient compliance, and physicians' lack of knowledge of, awareness to, or disagreement with specific guidelines (Sequist et al., 2005). User interface and other usability issues were likewise identified as hindering adherence to clinical reminders (Patterson et al., 2005), as well as workload and patient characteristics (Mayo-Smith & Agrawal, 2007; Sittig, Krall, Dykstra, Russell, & Chin, 2006).

As elaborated upon next, the HMO under study here employed a combined policy of drug formulary, co-payment, and differentiated cost coverage based on the type of drug prescribed. The policy was administered via a computerized drug prescription module embedded in an EMR whose use is mandatory yet open to various levels of compliance.

## 2.1. Description of the Study Environment

Israeli citizens are fully insured through the Israeli National Insurance Law, and can enroll with one of four HMOs that provide full health coverage to their members. EMR systems have been widely implemented in Israel since the early 1990s. All primary care physicians, as well as practitioners in most secondary care clinics of the studied HMO have been using the studied EMR system for nearly 20 years (Pliskin, 1994; Pliskin, Glezerman, Modai, & Weiler, 1996). The other three HMOs either use this same or a similar EMR system. Thus, all primary care and the vast majority of secondary healthcare records in Israel are fully computerized. The EMR system facilitates electronic real-time documentation of all physician-patient encounters during a visit and selective context-based data retrieval during treatment monitoring, including various clinical alerts and decision aids. In addition to order entry for drugs (via a built-in drug-prescription module), the EMR system supports such processes as laboratory referrals, expert consultation and imaging, and a bi-directional interface with administrative computerized systems, used to validate patient coverage and transmit various administrative data, for example, for cost calculation purposes. Based on DeRoches et al.'s (2008) classification, this is a comprehensive EMR.

The built-in drug prescription module, which is the only method practiced at the HMO for generating drug prescriptions, displays clinical details relevant to the prescription process, including patient clinical information, current and previous drugs prescribed to the patient, alerts of drug contradictions upon prescribing new drugs, and known allergies or sensitivities. The system also presents a list of drugs from which the physician may select. The list (see Figure 1) reflects the HMO's drug formulary, where drugs are ordered from the most to least preferred according to the HMO policy for drug coverage. The list contains ample information about each drug, some visible and some available upon clicking (e.g., administrative and pharmacological information). The first time a prescription is called for, the physicians may select any drug from the list as an initial choice. Upon prescribing a non-preferred drug, the drug-prescription module notifies the physician about available HMOpreferred generic substitutes (where the substitute is identical in chemical formulation to the patent drug) or therapeutic substitutes (where the substitute is not identical but is known to yield similar therapeutic results). More specifically, when a physician prescribes a non-preferred drug as an initial choice, the notification screen pops up and notifies the physician in real time: "Have you considered prescribing XXXX?" (See Appendix 1) The physician can then either choose the proposed preferred substitute instead of his/her initial choice. However, if the notification is ignored and the final choice is the same as the initial choice, s/he is asked to fill out an online form and explain the reasons for noncompliance (See Appendix 2). Physicians know that HMO administration can access these forms and examine their explanations. This feature is activated only for drugs with HMO-preferred substitutes that are prescribed to a patient for the first time. Clearly, the HMO's objective is to maximize physicians' compliance.

![](/api/attachments/EJR9P5A3/fulltext/images/720e3c05a50ea0ead4bee3d88fa7cd3ea637a46e6de1d85000794fc9e398d13a.jpg)  
Figure 1. The Drug Prescription Module

## 2.2. Compliance as an Organizational Behavior–the Organizational Justice Lens

The present exploratory study aimed to examine a behavior rather than to substantiate theoretical hypotheses. Yet, there is merit in a post-hoc theoretical interpretation of the factors found to affect compliance, believed to be a desirable organizational behavior, linked to other positive organizational outcomes such as job satisfaction, organizational commitment, withdrawal, and organizational citizenship (Colquitt, Conlon, Wesson, Porter, & Ng, 2001).

Of the four types of adherence behavior defined by Vashitz et al. (2009)--compliance, reliance, spillover, and reactance--physicians in the present study could only demonstrate compliance or reactance behaviors. Thus, we define compliance as adherence to drug substitute notification, either initially (self-compliance) or in response to a notification (assisted compliance). Non-compliance or reactance is refusal to adhere to a drug substitute recommendation even after being notified.

Two quite different theories that attempt to explain compliance behavior are the deterrence model and the accommodative model (Kagan & Scholz, 1984). The deterrence theory argues that people are motivated entirely by profit-seeking, assessing opportunities and risks and disobeying when the anticipated risks are small compared with the profits to be made through non-compliance (Kagan & Scholz, 1984). Advocates of the deterrence view believe that individuals will only comply with an authority’s rules and decisions when confronted with harsh sanctions and penalties. Clearly, this was not the case in the studied HMO, where physicians neither directly benefited from complying, nor were penalized for not complying. The accommodative theory maintains that attitudes and moral obligations, in addition to economic calculations or fear of punishment, are important in explaining compliance behavior and, therefore, need to be considered when managing non-compliance (Braithwaite, 2002).

Related to the accommodative model of compliance behavior is Tyler’s (1990) theory on compliance, according to which, people’s compliance behavior is strongly linked to views about justice and injustice. In particular, he suggests that procedural justice plays an important role in peoples decisions to comply with rules and regulations. Procedural justice is a refinement of the organizational justice or fairness theory, which initially dealt with the fairness of outcome distribution or allocation and the fairness of the procedures used to determine this distribution or allocation (Adams, 1965). This type of organizational justice was termed distributive justice (Leventhal, 1976). Later work introduced the concept of the fair process effect into the organizational justice literature, termed procedural justice (Folger, 1977; Leventhal, 1976; Lind & Tyler, 1988).

Procedural justice concerns the perceived fairness of the procedures involved in decision making and the perceived treatment one receives from a decision maker. The procedural justice literature demonstrates that people’s reactions to their personal experiences with authorities are rooted in their evaluations of the fairness of the procedures those agencies use to exercise their authority (Lind & Tyler, 1988; Tyler & Blader, 2000). A procedure should meet six criteria to be perceived as fair: a) be applied consistently across people and across time; b) be free from bias (e.g., ensuring that a third party has no vested interest in the particular settlement); c) ensure that accurate information is collected and used in making decisions; d) have some mechanism to correct flawed or inaccurate decisions; e) conform to personal or prevailing standards of ethics or morality; and f) ensure that the opinions of various groups affected by the decision have been taken into account (Colquitt et al., 2001; Leventhal, 1976).

Focusing on the importance of interpersonal treatment people receive when procedures are implemented, Bies and Moag (1986) suggested differentiating interactional justice from procedural justice. Further work (Greenberg, 1990; Greenberg, 1993) hypothesized interpersonal justice to consist of two dimensions: interactional justice, which refers to the degree to which people are treated with politeness, dignity, and respect by the authorities involved in executing procedures, and informational justice, which focuses on the explanations provided to people that convey information about why procedures were used in a certain way (Colquitt et al., 2001). There are, however, conflicting results concerning the discriminant validity of procedural justice, interactional, and informational justice, therefore, many researchers (see Colquitt et al., 2001 for details) have operationalized procedural justice by measuring process control as suggested by Leventhal (1976) along with interactional and informational justice in one combined scale.

There is empirical evidence to show that people who feel they have been treated in a procedurally fair manner by an organization will be more inclined to accept its decisions and follow its directions (Lind & Tyler, 1988; Tyler, Degoey, & Smith, 1996). It has also been found that people are more likely to challenge a situation collectively when they believe that the procedures are unfair (Greenberg, 1987; Murphy, 2003; Tyler, 1990).

Organizational justice theory is relevant to the context of this study because the drug substitute intervention studied here affects physicians' professional autonomy and self esteem, and because the issuing HMO clearly has vested interests in the outcomes, as have the patients. Therefore, we chose to explain the results via this lens, as further elaborated in the concluding section.

## 3. Research Methods

## 3.1. Research Approach

As previously stated, the present study adopts the interpretive, exploratory epistemology, aiming to examine routine behaviors of physicians who are proficient users of a drug prescription module within an EMR that includes drug substitution notifications.

## 3.2. Studied Intervention

At the time of the study, the HMO's catalog included about 2,600 drugs, to which substitutes (either generic or therapeutic) were offered for 1,443 drugs in 47 pharmacological groups. In describing the studied intervention, italics highlight the terminology used:

The intervention is activated upon a physician prescribing a first-time prescription for a drug with substitutes (a satisfying prescription), as opposed to a repeat prescription, where the same drug is represcribed for the patient. If at start time the physician's initial choice is a preferred drug (e.g., from the top of the list), s/he is exhibiting self-compliance behavior. If not, s/he is notified about recommended substitutes (Appendix 1) and can choose a preferred drug as a final choice, thus exhibiting assisted-compliance behavior. Otherwise, an online form appears and the physician is asked to specify the reasons for the non-compliance behavior (Appendix 2). The response time is the time elapsed between the initial and final choices (which equals zero for self-compliance), including the time required to fill out the form following non-compliance.

## 3.3. Study Design and Administration

Data collection for the study lasted 40 consecutive weeks from June 1, 2005 to February 28, 2006. To collect data for this study, a transparent computerized agent was embedded into the drug prescription module, recording for the entire physician population in all 176 primary care clinics of the HMO, and for each prescription: the physician's ID, patient age, visit date and time, initial drug choice, final drug choice, and the time elapsed between the two. Physician demographics were provided by the HMO whose management approved the data collection. Physicians were unaware of the data collection; hence, regular work practices were not disrupted and no bias was suspected. Data recorded by the computerized agent were stored in real time in an MS-Access 2003 database and analyzed using SPSS version 17.0.

## 3.4. Sample

We collected about 5 million prescriptions written by 2,120 physicians. However, only about 1.2 million prescriptions, prescribed by 647 physicians, were for satisfying prescriptions, invoking the studied intervention because they were first-time prescriptions for drugs with substitutes.

## 3.5. Statistical Analyses

We used the following methods: cross-tab analysis for the descriptive statistics; independent-samples t-test for comparing means between self-employed and HMO-employed physicians; and multinomial logistic regression for compliance analyses, with the dependent variable being the three compliance types (1=self, 2=assisted, and 3=non) and the independent variables being substitution type (1=generic, 2=therapeutic), employment type (1=self-employed, 2=HMO-employed), domain (1=GP, 2=specialist), gender (1=male, 2=female), country of medical education (1=Eastern Europe, 2=Western Europe, 3=North America, 4=South America, 5=Israel), average number of patient visits per day, physician age, tenure with the HMO, and patient age. We standardized quantitative variables indicating years or visits to cater to unit differences. Variance Inflation Factor (VIF) values for the independent variables were around 1, indicating lack of multicollinearity. We employed a forward stepwise entry method with score as the entry criterion and Wald as the removal criterion. Additionally, we checked two-way interactions for all variables except country of education (because of numerous combinations, the reporting of which is beyond the scope of this study). None of the interaction effects was practically significant as the odds ratios were close to 1 (although all were statistically significant due to the large sample). We examined correlations using univariate two-tailed Pearson correlations. We assessed the lower bound on cost savings by calculating the difference between the costs of the initial and final choices in the assisted-compliance group.

## 4. Results

## 4.1. Sample Description

We present descriptive statistics of the sample in Table 1. Two hundred ninety-seven (46 percent) of the participating physicians were self-employed, whereas 350 (54 percent) were HMO-employed. The percentage of specialists in the self-employed group (53 percent) was significantly higher than in the HMO-employed group (22 percent), the rest being GPs. These two groups significantly differed on several traits, such as average number of work days (self-employed worked more) and average number of patients treated per day (self-employed treated more). The two groups, however, were not significantly different in terms of age, average tenure on the job, and number of patient visits yielding prescriptions.

<table><tr><td colspan="5">Table 1. Descriptive Statistics</td></tr><tr><td></td><td>Self-employed</td><td>HMO-employed</td><td>Total</td><td>Significance</td></tr><tr><td>Number of physicians</td><td>297</td><td>350</td><td>647</td><td>P&lt;0.001</td></tr><tr><td>Number of General Practitioners/ Specialists</td><td>140 / 157</td><td>274 / 76</td><td>414 / 233</td><td>P&lt;0.001</td></tr><tr><td>Average physician age (S.D.) $^{1}$ </td><td>48.8 (7.7)</td><td>48.06 (9.17)</td><td>48.4 (8.53)</td><td>n.s.</td></tr><tr><td>Average (S.D.) tenure on the job</td><td>9.17 (5.3)</td><td>9.12 (5.2)</td><td>9.14 (5.26)</td><td>n.s.</td></tr><tr><td>Percent of females</td><td>41%</td><td>62%</td><td>52 %</td><td>P&lt;0.001</td></tr><tr><td>Average (S.D.) number of work days per physician during the study period</td><td>140.98 (55.53)</td><td>125.34 (48.72)</td><td>132.52 (52.5)</td><td>P&lt;0.001</td></tr><tr><td>Average (S.D.) number of patient visits per day</td><td>28.9 (17.18)</td><td>21.92 (10.96)</td><td>25.12 (14.57)</td><td>P&lt;0.001</td></tr><tr><td>Percent of visits yielding prescriptions</td><td>59.15%</td><td>60.97%</td><td>59.94%</td><td>n.s.</td></tr><tr><td>Number of satisfying prescriptions</td><td>667,362</td><td>547,885</td><td>1,212,247</td><td>P&lt;0.001</td></tr><tr><td>Number of satisfying prescriptions per physician</td><td>2,236.91(2380.45)</td><td>1,565.39(1440.45)</td><td>1,873.64(1956.93)</td><td>P&lt;0.001</td></tr></table>

## 4.2. Compliance Patterns

Overall, the self-compliance rate (i.e., the ratio of self-compliance to the total number of satisfying prescriptions) was 57.2 percent (Table 2). Of the remaining prescriptions (the difference between the total number of satisfying prescriptions and the number of self-compliance prescriptions), the assisted-compliance rate was 29.8 percent (13 percent of the total number of satisfying prescriptions), leading to a 30 percent non-compliance rate and a 70 percent accumulated-compliance rate (the difference between 100 percent and the non-compliance rate).

Table 2. Compliance Rate for Generic, Therapeutic and All Substitutes

<table><tr><td></td><td colspan="3">Generic substitutes</td><td colspan="3">Therapeutic substitutes</td><td colspan="3">All Substitutes</td></tr><tr><td></td><td>Prescribed</td><td>Rate</td><td>% from total</td><td>Prescribed</td><td>Rate</td><td>% from total</td><td>Prescribed</td><td>Rate</td><td>% from total</td></tr><tr><td>Self-compliance</td><td>576,907</td><td>74%</td><td>74%</td><td>115,971</td><td>27%</td><td>27%</td><td>692,878</td><td>57%</td><td>57%</td></tr><tr><td>Assisted-compliance</td><td>127,585</td><td>63%</td><td>16%</td><td>27,096</td><td>9%</td><td>6%</td><td>154,681</td><td>30%</td><td>13%</td></tr><tr><td>Non-compliance</td><td>74,864</td><td>10%</td><td>10%</td><td>289,824</td><td>67%</td><td>67%</td><td>364,688</td><td>30%</td><td>30%</td></tr><tr><td>Total</td><td>779,356</td><td></td><td>100%</td><td>432,891</td><td></td><td>100%</td><td>1,212,247</td><td></td><td>100%</td></tr></table>

The results in Table 2 show a significantly higher tendency to comply with HMO recommendations for generic substitutes than for therapeutic ones (p<0.001): for generic substitution, 74 percent selfcomplied and 63 percent of the others assisted-complied, bringing the accumulated-compliance rate to 90 percent. For therapeutic substitution, however, only 27 percent self-complied, 8.5 percent of the rest assisted-complied, bringing the accumulated-compliance rate to only 33 percent. Thus, the noncompliance rate was as high as 67 percent for therapeutic substitution but as low as 10 percent for generic substitution.

## 4.3. Compliance Patterns and the Number of Recommended Substitutes

We observed a positive and statistically significant correlation (r=0.201, p<0.01) between log time and the number of recommended substitute drugs on the list presented to the physician for therapeutic substitutions and non-compliance. Thus, physicians tended not to comply and to adhere to their initial choice when lists of recommended substitutes were longer, possibly avoiding the time required to examine a long list of drugs, particularly therapeutic ones. Hence, the optimal number of listed substitutes merits further investigation.

## 4.4. Learning Curves

Introduction of new drugs, one before data collection commenced, and one at Week 20 of data collection, or changes in recommended substitutes, allowed for the elicitation of learning curves over the 40 weeks of data collection. For introduction of new drugs, the learning period in Figures 2 and 3 is characterized by a continuous increase in assisted compliance, as well as in self-compliance, toward stabilization. In Figure 3, the learning curve is steeper and accompanied by a sharp climb in assisted compliance.

Also noteworthy is that a change in the drug policy of the HMO in the generic drug substitutes group resulted in a steep decrease in self-compliance, compensated for by a high and stable assisted compliance rate occurring within a week after policy change, while self-compliance remained low (Figure 4). This, however, is not the case in the therapeutic substitutes group, where the assisted compliance rate was low (Figure 5). Although self-compliance behaves similarly for the two groups, the assisted-compliance rate for the therapeutic substitute was not affected and remained low. Learning curves for drugs in drug groups where no such change occurred, show that self-compliance increased slightly with time, whereas assisted compliance tended to remain rather stable, implying that the contribution of the system's notification capacity to compliance does not diminish over time, and there is merit in continued notifications for existing as well as for new drugs.

BONE DISEASE (ALENDRONATE Group 165)  
![](/api/attachments/EJR9P5A3/fulltext/images/d2e047ecdcea68399b6da543391e33f26950d98fb4a96f8e39fe88f6700bd6ad.jpg)

Figure 2. Learning Curve of a New Drug (Introduced Before Start of Data Collection)

VITAMINS/MINERALS (TRIPLE B. Group 706)  
![](/api/attachments/EJR9P5A3/fulltext/images/976ace958aa3ae44d4fa4d32fcbcd4c84f66fa98f51386601366c60c8f6c6c92.jpg)

Figure 3. Learning Curve of a New Drug Introduced at Week 20

VITAMINS/MINERALS ( BABY A+D Group 256)  
![](/api/attachments/EJR9P5A3/fulltext/images/a47ca5101bd6378750ce51151454dca504fafe02c8799315eac5e2d24a7432e0.jpg)  
Figure 4. Reaction to Change in Recommendations (Generic Drug Substitute)

ANTIVIRALS (ZOVIRAX Group623)  
![](/api/attachments/EJR9P5A3/fulltext/images/eb14102fda1e27cfcc272584e0c8385b67d72a00b8737e733784601675b23e3f.jpg)  
Figure 5. Reaction to Change in Recommendations (Therapeutic Substitute)

## 4.5. Resistance to Notifications

In certain pharmaceutical groups, efforts to impact physicians' drug prescription habits failed, as depicted, for example, in Figure 6 for the antibiotics group. In one case, the HMO's effort to shift physicians’ prescription habits via notifications from one drug to another drug, which was not identical in its chemical formulation, resulted in a 5 percent self-compliance and a 2 percent assisted compliance rate. Evidently, physicians did not perceive the HMO-recommended drug as an adequate substitute. Analysis of response time, next, allows an insight into their way of thinking.

ANTIBIOTICS (MOXYVIT FORTE Group 702)  
![](/api/attachments/EJR9P5A3/fulltext/images/532b414981773492f1ecfa0fa37e728ce889eb30425d200248ad2e705f508b15.jpg)  
Figure 6. Resistance to Notifications (Non-Compliance)

## 4.6. Physician Response Time to Substitute Notifications

We calculated average response time (elapsed between initial and final choices) using two methods: 1) elimination of 10 percent of outliers (exhibiting an unrealistically long response time possibly due to pausing during the prescription process in order to accomplish another task), and 2) using log(time), an arithmetic procedure that shortens the upper tail relative to the lower tail. As displayed in Table 3, the results were quite similar for both methods: non-compliance took longer than assisted compliance in the generic substitution group (p<0.001), but in the therapeutic substitution group assisted compliance took significantly longer than non-compliance (p<0.001), in spite of the extra time required to fill the non-compliance form.

<table><tr><td colspan="8">Table 3. Time to Prescription Completion</td></tr><tr><td colspan="2"></td><td>Prescriptions</td><td>Min</td><td>Max</td><td>Mean</td><td>St. Dev.</td><td rowspan="7"></td></tr><tr><td rowspan="3">Generic</td><td>Compliance</td><td colspan="5">Method 1: Eliminating 10% of outliers</td></tr><tr><td>Assisted-</td><td>126,532</td><td>0.08</td><td>29.99</td><td>2.61</td><td>3.05</td></tr><tr><td>Non-</td><td>74,449</td><td>0.12</td><td>29.97</td><td>2.84</td><td>2.74</td></tr><tr><td rowspan="2">Therapeutic</td><td>Assisted-</td><td>26,390</td><td>0.11</td><td>29.99</td><td>4.48</td><td>4.62</td></tr><tr><td>Non-</td><td>286,849</td><td>0.14</td><td>29.98</td><td>3.53</td><td>3.32</td></tr><tr><td colspan="2">Total</td><td>514,220</td><td>0.08</td><td>29.99</td><td>3.25</td><td>3.30</td></tr><tr><td colspan="7">Method 2: log(time)</td><td>Mean Time (sec)</td></tr><tr><td rowspan="2">Generic</td><td>Assisted-</td><td>127,585</td><td>-2.53</td><td>7.38</td><td>0.66</td><td>0.79</td><td>2.64</td></tr><tr><td>Non-</td><td>74,864</td><td>-2.12</td><td>6.60</td><td>0.84</td><td>0.63</td><td>2.83</td></tr><tr><td rowspan="2">Therapeutic</td><td>Assisted-</td><td>27,096</td><td>-2.21</td><td>8.49</td><td>1.21</td><td>0.94</td><td>5.19</td></tr><tr><td>Non-</td><td>289,824</td><td>-1.97</td><td>7.15</td><td>1.06</td><td>0.68</td><td>3.62</td></tr><tr><td colspan="2">Total</td><td>519,369</td><td>-2.53</td><td>8.49</td><td>0.94</td><td>0.74</td><td>3.35</td></tr></table>

## 4.7. Compliance Patterns and Physician Demographic Traits

In a multinomial logistic regression, all independent factorial variables express odds of showing assisted compliance or non-compliance, respectively, compared to demonstrating self-compliance relative to the last category of the variable, with all other variables being equal. Continuous factors represent odds compared to an increase of one standard deviation. The model explained between 31 percent (Cox and Snell) and 36.8 percent (Negelkerke pseudo R-square) of the variance in compliance type. Although all variables were statistically significant, substitution type, either generic or therapeutic, had a dominant effect on the model likelihood (χ2=392,116, df=2, p<0.001), with average visits per day with the physician $( \times 2 = 2 , 1 9 8 , { \mathsf { d f } } { = } 2 , { \mathsf { p } } { < } 0 . 0 0 1 )$ , and physician's age $( \mathsf { X } 2 = 1 , 3 0 1$ df=2, p<0.001) as second and third in effect size, albeit significantly smaller than substitution type. Patient age (χ2=469, df=2, p<0.001) and physician's HMO employment type (χ2=222, df=2, p<0.001) had a much lesser effect. All other variables had a negligible effect on the model likelihood. The odds (in the form of Exp(B)) entailed by the independent variables on assisted compliance and noncompliance compared to self-compliance are summarized in Table 4.

Table 4. Results of the Multinomial Logistic Regression

<table><tr><td rowspan="2">Assisted-compliance</td><td rowspan="2">B</td><td rowspan="2">Std. Error</td><td rowspan="2">Wald</td><td rowspan="2">df</td><td rowspan="2">Sig.</td><td rowspan="2">Exp(B)</td><td colspan="2">95% Confidence Interval for Exp(B)</td></tr><tr><td>Lower Bound</td><td>Upper Bound</td></tr><tr><td>Intercept</td><td>-1.47</td><td>0.011</td><td>17404.36</td><td>1</td><td>0.000</td><td></td><td></td><td></td></tr><tr><td>Generic (vs. Therapeutic)</td><td>-0.03</td><td>0.008</td><td>17.95</td><td>1</td><td>0.000</td><td>0.97</td><td>0.952</td><td>0.982</td></tr><tr><td>Male (vs. Female)</td><td>0.04</td><td>0.007</td><td>27.79</td><td>1</td><td>0.000</td><td>1.04</td><td>1.022</td><td>1.050</td></tr><tr><td>HMO-employed (vs. Self-employed)</td><td>0.10</td><td>0.007</td><td>194.22</td><td>1</td><td>0.000</td><td>1.10</td><td>1.085</td><td>1.115</td></tr><tr><td>GP (Vs. Specialist)</td><td>-0.03</td><td>0.008</td><td>17.67</td><td>1</td><td>0.000</td><td>0.97</td><td>0.954</td><td>0.983</td></tr><tr><td>Z-Patient age</td><td>-0.02</td><td>0.003</td><td>32.26</td><td>1</td><td>0.000</td><td>0.98</td><td>0.975</td><td>0.988</td></tr><tr><td>Z- Physician age</td><td>-0.13</td><td>0.004</td><td>972.75</td><td>1</td><td>0.000</td><td>0.88</td><td>0.870</td><td>0.885</td></tr><tr><td>Z - Physician tenure on the job</td><td>0.02</td><td>0.004</td><td>19.08</td><td>1</td><td>0.000</td><td>1.02</td><td>1.010</td><td>1.027</td></tr><tr><td>Z- Average Visits per day</td><td>-0.11</td><td>0.004</td><td>1070.25</td><td>1</td><td>0.000</td><td>0.89</td><td>0.886</td><td>0.898</td></tr><tr><td>Eastern Europe education</td><td>-0.14</td><td>0.008</td><td>326.83</td><td>1</td><td>0.000</td><td>0.87</td><td>0.858</td><td>0.884</td></tr><tr><td>Western Europe education</td><td>0.08</td><td>0.010</td><td>72.00</td><td>1</td><td>0.000</td><td>1.09</td><td>1.067</td><td>1.109</td></tr><tr><td>North America education</td><td>0.30</td><td>0.025</td><td>141.14</td><td>1</td><td>0.000</td><td>1.35</td><td>1.282</td><td>1.414</td></tr><tr><td>South America education</td><td>-0.14</td><td>0.019</td><td>54.95</td><td>1</td><td>0.000</td><td>0.87</td><td>0.839</td><td>0.903</td></tr><tr><td colspan="9">Non-compliance</td></tr><tr><td>Intercept</td><td>0.91</td><td>0.009</td><td>10023.63</td><td>1</td><td>0.000</td><td></td><td></td><td></td></tr><tr><td>Generic (vs. Therapeutic)</td><td>-2.97</td><td>0.006</td><td>287228.91</td><td>1</td><td>0.000</td><td>0.05</td><td>0.051</td><td>0.052</td></tr><tr><td>Male (vs. Female)</td><td>0.05</td><td>0.006</td><td>70.57</td><td>1</td><td>0.000</td><td>1.05</td><td>1.039</td><td>1.063</td></tr><tr><td>HMO-employed (vs. Self-employed)</td><td>-0.01</td><td>0.006</td><td>0.67</td><td>1</td><td>0.413</td><td>0.99</td><td>0.983</td><td>1.007</td></tr><tr><td>GP (Vs. Specialist)</td><td>-0.01</td><td>0.008</td><td>1.84</td><td>1</td><td>0.175</td><td>0.99</td><td>0.974</td><td>1.005</td></tr><tr><td>Z-Patient age</td><td>0.10</td><td>0.005</td><td>415.65</td><td>1</td><td>0.000</td><td>1.11</td><td>1.095</td><td>1.117</td></tr><tr><td>Z- Physician age</td><td>-0.01</td><td>0.004</td><td>10.77</td><td>1</td><td>0.001</td><td>0.99</td><td>0.981</td><td>0.995</td></tr><tr><td>Z - Physician tenure on the job</td><td>-0.02</td><td>0.004</td><td>41.52</td><td>1</td><td>0.000</td><td>0.98</td><td>0.969</td><td>0.983</td></tr><tr><td>Z- Average Visits per day</td><td>0.02</td><td>0.003</td><td>37.30</td><td>1</td><td>0.000</td><td>1.02</td><td>1.012</td><td>1.024</td></tr><tr><td>Eastern Europe education</td><td>0.01</td><td>0.007</td><td>3.67</td><td>1</td><td>0.055</td><td>1.01</td><td>1.000</td><td>1.027</td></tr><tr><td>Western Europe education</td><td>-0.07</td><td>0.009</td><td>61.99</td><td>1</td><td>0.000</td><td>0.93</td><td>0.914</td><td>0.947</td></tr><tr><td>North America education</td><td>0.24</td><td>0.024</td><td>102.79</td><td>1</td><td>0.000</td><td>1.27</td><td>1.214</td><td>1.333</td></tr><tr><td>South America education</td><td>-0.05</td><td>0.016</td><td>8.08</td><td>1</td><td>0.004</td><td>0.95</td><td>0.924</td><td>0.986</td></tr></table>

## 4.8. Estimated Cost Savings

We calculated a lower bound on drug cost savings in millions of New Israeli Shekel (NIS), with the exchange rate during the data collection period between 4.4 and 4.7 NIS to one US dollar. Cost calculations were based on the difference between the cost of the initial and final drug choices (private pharmacy prices, since the studied HMO refused to disclose paid prices), reflecting cost savings associated with assisted compliance. The total estimated cost of drugs in the 1.21 million satisfying prescriptions was 246.67 million NIS, of which 67 percent (165.78 Million NIS) was for chronic drugs and 33 percent (80.89 million NIS) for acute ones. Table 5 displays the estimated savings in monetary and percentage terms for acute (one time) and chronic (long term) drugs, keeping in mind savings achieved for the latter have a long-term cumulative impact due to dominance (67 percent) and life-long (chronic) consumption. As evident from Table 5, savings for chronic drugs (4.7 percent) were higher than for acute ones (2.39 percent). The lower savings on acute drugs may have stemmed from the fact that physicians generally did not comply with substitutes for antibiotics, the most commonly prescribed acute drugs, but the associated savings have a short-term effect anyway. Altogether, the estimated lower bound on cost savings amounted to 1.6 million NIS (an average of 3.6 percent savings). It is plausible that higher savings are achieved assuming that physicians become accustomed to prescribing generic drugs as a result of using the system, as evident by the large proportion of self-compliance behavior.

<table><tr><td colspan="7">Table 5. Savings (in Million NIS)</td></tr><tr><td></td><td colspan="3">Acute Drugs Cost</td><td colspan="3">Chronic Drugs Cost</td></tr><tr><td></td><td>Initial choice</td><td>Final choice</td><td>Difference (%)</td><td>Initial choice</td><td>Final choice</td><td>Difference (%)</td></tr><tr><td>Generic substitutes</td><td>15.2</td><td>14.8</td><td>0.4 (2.39)</td><td>14.1</td><td>13.6</td><td>0.5 (4.72)</td></tr><tr><td>Therapeutic substitutes</td><td>22.2</td><td>22.0</td><td>0.2 (1.46)</td><td>11.7</td><td>11.2</td><td>0.5 (4.63)</td></tr><tr><td>Total</td><td>37.4</td><td>36.8</td><td>0.6 (1.46)</td><td>25.8</td><td>24.8</td><td>1.0 (4.68)</td></tr></table>

## 5. Discussion and Conclusions

The spiraling spending on healthcare, in general, and the growing relative proportion of drug costs, in particular, merit special attention to measures to contain drug costs taken by healthcare providers and insurers. Several questions guided this study, the fundamental one being whether it is possible to gain physicians' compliance with drug prescription procedures preferred by the HMO to contain costs. In other words, when so notified by the system, do physicians comply with an HMO's notification, rethink their initial drug choice, and prescribe instead an HMO-preferred substitute? Other questions stemming from the primary one are: Is compliance context-dependent? Does compliance depend on personal or environmental traits? Is such notification capacity associated with a financial contribution? In addition to addressing these issues, we reflect on the theoretical implications of the results, showing how a theory stemming from the behavioral and organizational sciences can contribute to explaining the clinical behavior of physicians. Added to the information systems aspect, it emphasizes the multi-disciplinary approach adopted in this study.

## 5.1. Limitations

A major limitation of this study is that the studied environment was dynamic during the data collection period, as is the case with any real business environment during a long period of 40 weeks. In this dynamic environment, changes were introduced both to drugs and to the organizational drug formulary, causing some interference. These changes were documented and eventually accounted for in the results, actually contributing to a broader understanding of physicians' behavior by allowing for example illustration and observation of learning curves. Another limitation lies in the fact that only about half of the drugs included in the HMO’s formulary had recommended substitutes, yet these were the most frequently prescribed drugs. An additional limitation is related to the use of private pharmacy prices for calculating drug costs, since the HMO was reluctant to disclose prices it pays for drugs. Therefore, drug cost savings should be regarded as demonstration rather than actual monetary cost savings. Finally, we studied only one HMO, therefore, external validity may be questionable. Although more research is called for, we believe that the results can be generalized to other HMOs and healthcare providers, and that HMOs employing a similar intervention under comparable conditions can experience parallel results, particularly because no organizational or personal characteristics were found to affect compliance as strongly as the type of substitute.

## 5.2. Summary of the Results

The results show that physicians tended to comply more with notifications about generic substitute drugs than with notifications about therapeutic substitutes. The fact that new drugs and new drug recommendations have been introduced during the study period allowed drawing learning curves, showing that users of the notification capacity of the system learned to comply when convinced that a recommended substitute was an identical drug, demonstrating in these cases a steep learning curve and a high rate of compliance (self-compliance and assisted compliance combined). In contrast, the level of compliance when physicians doubted the adequacy of the recommended substitutes remained low throughout. Moreover, users spent a longer time examining therapeutic substitutes, evidently contemplating the adequacy of the recommendations. This result attests to the fact that compliance is not automatic but a cognitive and calculated process. Several demographic traits were found to marginally affect the various compliance types, the most notable of which are the effects of employment type, expertise, age, and work load. Finally, a cautious estimate of drug cost savings showed that such a system holds promise for significant cost containment.

## 5.3. Theoretical Interpretation

The fact that physicians tended to more readily comply with notifications about generic substitute drugs, and demonstrated a rather reactant behavior when asked to substitute a prescribed drug with a non-identical therapeutic substitute, shows that issues pertaining to procedural justice may have been involved. The difference in response time between the two types of substitutes likewise lends support to this interpretation.

Substitution with generic drugs adheres more to the six criteria proposed by Leventhal (1976) for a procedure to be perceived fair, than does substitution with therapeutic drugs, because the generic drug is supposed to be identical to the patent drug. Therefore, this procedure can be perceived as free of bias (in spite of the fact that the HMO benefits from the substitute, yet seemingly at no professional or ethical harm), and it clearly conforms to prevailing standards of ethics and morality. The additional information provided for each drug on the HMO's formulary contributed to the perceptions of informational justice, and no interactional unfair conduct could have been associated with this substitution procedure.

In contrast, there is strong evidence that therapeutic substitutes invoked perceptions of unjust procedures. Physicians might not have been convinced of the adequacy of the substitution, which could be an explanation for the extra time taken for this decision. For example, they could have perceived this recommendation as merely representing the vested interest of the HMO to save money at the expense of patients. Physicians could clearly regard such a notion as hindering their professional efficacy and autonomy, rendering a rather reactant response (Vashitz et al., 2009). It may very well be that these recommendations were additionally interpreted as unfair interactional conduct between HMO's management and physicians whose voice might not have been heard, or at least not adequately regarded (Lind & Tyler, 1988). Assuming that physicians perceive themselves as representing the well-being of their patients, they may also regard therapeutic substitute recommendations as interactional injustice toward their patients, as well as an informational unjust procedure, because patients might not possess the full information concerning the nature of the drug substitute.

## 5.4. Implications for Research

Future research should investigate reasons for the elicited compliance behavior possibly by using scales measuring the organizational justice constructs (Colquitt, 2001) focusing on procedural, interactional, and informational justice, which are more relevant to this context. In-depth interviews with physicians who demonstrate various compliance behaviors can also greatly contribute to understanding their motivations.

Although the three types of organizational justice seem more relevant to the investigated context, the negative effect of workload on compliance possibly suggests some form of distributive justice issue. It is plausible that overloaded physicians feel that resources and outcomes are not justly distributed, hence they develop a form of resentment expressed by not complying with a recommendation that, if adhered to, would save costs for the presumably unjust employer. We suggest this topic for future research.

Further work along this trajectory will shed light on the important topic of adherence to administrative procedures. Results of such work should be of interest to researchers in healthcare administration, to management scientists who study organizational conduct in the current prevailing environments of knowledge and knowledgeable workers, and to designers of information systems who could use the results to develop organizational systems that would be more readily accepted by users if perceived as adhering to procedural, interactional, and informational justice.

## 5.5. Implications for Practice

HMOs and other healthcare providers, as well as providers of EMR, particularly drug prescription systems, can benefit from the results of this study in several ways. First, the results support the assertion that similar clinical information systems might be effective in reducing drug costs without impeding quality of healthcare. Nonetheless, compliance with drug notifications is neither automatic nor immediate, and physicians need to be convinced that the substitute notifications are based on good clinical practices and are not intended to promote cost savings at the expense of the quality of care. Furthermore, time is an important determinant for users when deciding whether or not to comply with a drug substitute notification in an EMR system. Hence, when designing such a system, every feature, key, and functionality needs to be carefully scrutinized for necessity, and its impact on response time must be evaluated.

Our findings relating compliance to employment type and specialty suggest that HMOs might choose to act proactively and differentially toward increasing compliance via educational programs as well as incentives aimed at driving compliance up. In addition, HMOs can revisit and change substitute recommendations that are difficult for physicians to comply with. Workload has also been found to negatively affect compliance in certain instances. Employers should evaluate the benefits of a heavier workload against lost cost savings.

In conclusion, this study illustrates the contribution of an EMR system with a substitute notification capacity built into a drug prescription module in a generally complex and difficult field, where benefits, in general, and economic impacts, in particular, are not easily obtained and demonstrated. However, more research is called for to further substantiate these results.

## References

Adams, J. S. (1965). Inequity in social exchange. Advances in Experimental Social Psychology, 2, 267-299.

Bies, R. J., & Moag, J. S. (1986). Interactional justice: Communication criteria of fairness. In R. J. Lewicki, B. H. Sheppard & M. H. Bazerman (Eds.), Research on negotiation in organizations (Vol. 1, pp. 43-55). Greenwich, CT: JAI Press.

Blumenthal, D. (2009). Stimulating the adoption of health information technology. New England Journal of Medicine, 360, 1477-1479.

Braithwaite, J. (2002). Restorative justice & responsive regulation. USA: Oxford University Press.

Coch, L., & French, J. R. P., Jr. (1948). Overcoming resistance to change. Human Relations, 1(4), 512-532.

Colquitt, J. A. (2001). On the dimensionality of organizational justice: A construct validation of a measure. Journal of applied Psychology, 86(3), 386-400.

Colquitt, J. A., Conlon, D. E., Wesson, M. J., Porter, C. O. L. H., & Ng, K. Y. (2001). Justice at the millennium: A meta-analytic review of 25 years of organizational justice research. Journal of Applied Psychology, 86(3), 425-445.

Connell, N. A. D., & Young, T. P. (2007). Evaluating healthcare information systems through an "enterprise" perspective. Information & Management, 44(4), 433-440.

Daly, R. (2007). Prescription drug cost increases far outpace U.S. inflation rate. Psychiatric News, 42(23), 12.

Delpierre, C., Cuzin, L., Fillaux, J., Alvarez, M., Massip, P., & Lang, T. (2004). A systematic review of computer-based patient record systems and quality of care: More randomized clinical trials or a broader approach? International Journal of Quality in Health Care, 16(5), 407-416.

Demakis, J. G., Beauchamp, C., Cull, W. L., Denwood, R., Eisen, S. A., Lofgren, R., ... Henderson, W. G. (2000). Improving residents' compliance with standards of ambulatory care: Results from the VA cooperative study on computerized reminders. Journal of the American Medical Association (JAMA), 284(11), 1411-1416.

DesRoches, C. M., Campbell, E. G., Rao, S. R., Donelan, K., Ferris, T. G., Jha, A., ... Blumenthal, M. D. (2008). Electronic health records in ambulatory care -- A national survey of physicians. New England Journal of Medicine, 359(1), 50-60.

Folger, R. (1977). Distributive and procedural justice: Combined impact of “voice” and improvement on experienced inequity. Journal of Personality and Social Psychology, 35(2), 108-119.

Gibson, T. B., Ozminkowski, R. J., & Goetzel, R. Z. (2005). The effects of prescription drug cost sharing: A review of the evidence. American Journal of Managed Care, 11(11), 730-740.

Ginsburg, J. A., Doherty, R. B., Ralston, J. F. J., MD , & Senkeeto, N. (2008). Achieving a highperformance health care system with universal access: What the United States can learn from other countries. Annals of Internal Medicine, 148(1), 55-75.

Goldman, D. (2009, January 12, 2009). Obama's big idea: Digital health records, Retrieved May 14, 2009, from http://money.cnn.com/2009/01/12/technology/stimulus\_health\_care/

Goldman, D. P., Joyce, G. F., Escarce, J. J., Pace, J. E., Solomon, M. D., Laouri, M., ... Teutsch, S. M. (2004). Pharmacy benefits and the use of drugs by the chronically ill. The Journal of the American Medical Association, 291(19), 2344-2350.

Greenberg, J. (1987). Reactions to procedural injustice in payment distributions: Do the means justify the ends? Journal of Applied Psychology, 72(1), 55-61.

Greenberg, J. (1990). Employee theft as a reaction to underpayment inequity: The hidden cost of pay cuts. Journal of Applied Psychology, 75(5), 561-568.

Greenberg, J. (1993). The social side of fairness: Interpersonal and informational classes of organizational justice. In R. Cropanzano (Ed.), Justice in the workplace: Approaching fairness in human resource management (Vol. 1, pp. 79-103). Hillside, NJ: Erlbaum.

Huskamp, H. A., Deverka, P. A., Epstein, A. M., Epstein, R. S., McGuigan, K. A., & Frank, R. G. (2003a). The effect of incentive-based formularies on prescription-drug utilization and spending. The New England Journal of Medicine, 349(23), 2224-2232.

Huskamp, H. A., Epstein, A. M., & Blumenthal, D. (2003b). The impact of a national prescription drug formulary on prices, market share, and spending: Lessons for Medicare? Health Affairs, 22(3), 149-158.

Huskamp, H.A., Frank , R.G., McGuigan, K.A., & Yuting, Z (2005). The Impact of a Three-Tier Formulary on Demand Response for Prescription Drugs, Journal of Economics & Management Strategy 14(3), 729-753.

Jensen, T. B., & Aanestad, M. (2007). Hospitality and hostility in hospitals: A case study of an EPR adoption among surgeons. European Journal of Information Systems, 16(6), 672-680.

Jha, A. K., Bates, D. W., Jenter, C., Orav, E. J., Zheng, J., Cleary, P., & Simon, S. R. (2009). Electronic health records: Use, barriers and satisfaction among physicians who care for black and Hispanic patients. Journal of Evaluation in Clinical Practice, 15(1), 158-163.

Jha, A. K., DesRoches, C. M., Campbell, E. G., Donelan, K., Rao, S. R., Ferris, T. G., ... Blumenthal, D. (2009). Use of electronic health records in U.S. hospitals. New England Journal of Medicine, 360(16), 1628-1638.

Kagan, R. A., & Scholz, J. T. (1984). The criminology of the corporation and regulatory enforcement strategies. In K. Hawkins & J. M. Thomas (Eds.), Enforcing regulation (pp. 67-97). Boston: Kluwer-Nijhoff Publishing.

KFF. (2007). Trends in healthcare costs and spending, Retrieved June 3, 2009, from http://ww.health08.org/insurance/upload/7692.pdf

Kuperman, G. J., & Gibson, R. F. (2003). Computer physician order entry: Benefits, costs, and issues. Annals of Internal Medicine, 139(1), 31-39.

Kush, R. D., Helton, E., Rockhold, F. W., & Hardison, C. D. (2008). Electronic health records, medica research, and the tower of Babel. The New England Journal of Medicine, 358(16), 1738- 1740.

Leventhal, G. S. (1976). The distribution of rewards and resources in groups and organizations. In l. Berkowitz & W. Walster (Eds.), Advances in experimental social psychology (Vol. 9, pp. 91- 131). New-York: Academic Press.

Lind, E. A., & Tyler, T. R. (1988). The social psychology of procedural justice. In M. J. Lerner (Ed.), Critical issues in social justice. New York: Plenum Press.

Martens, J. D., van der Weijden, T., Winkens, R. A. G., Kester, A. D. M., Geerts, P. J. H., Evers, S. M. A. A., & Severens, J. L. (2008). Feasibility and acceptability of a computerised system with automated reminders for prescribing behaviour in primary care. International Journal of Medical Informatics, 77(3), 199-207.

Matheny, M. E., Sequist, T. D., Seger, A. C., Fiskio, J. M., Sperling, M., Bugbee, D., ... Gandhi, T. K. (2008). A randomized trial of electronic clinical reminders to improve medication laboratory monitoring. Journal of the American Medical Informatics Association, 15(4), 424-429.

Mayo-Smith, M. F., & Agrawal, A. (2007). Factors associated with improved completion of computerized clinical reminders across a large healthcare system. International Journal of Medical Informatics, 76(10), 710-716.

Meyer, J. (2004). Conceptual issues in the study of dynamic hazard warnings. Human Factors, 46(2), 196-204.

Mongan, J. J., Ferris, T. G., & Lee, T. H. (2008). Options for slowing the growth of health care costs. The New England Journal of Medicine, 358(14), 1509-1514.

Murphy, K. (2003). Procedural justice and tax compliance. Australian Journal of Social Issues, 38(3), 379-408.

OECD. (2007, July 2007). OECD in Figures: OECD Health Data 2007, Retrieved November 24, 2008, from http://titania.sourceoecd.org/vl=1327807/cl=44/nw=1/rpsv/figures\_2007/en/page2.htm

Patterson, E. S., Doebbeling, B. N., Fung, C. H., Militello, L., Anders, S., & Asch, S. M. (2005). Identifying barriers to the effective use of clinical reminders: Bootstrapping multiple methods. Journal of Biomedical Informatics, 38(3), 189-199.

Piderit, S. K. (2000). Rethinking resistance and recognizing ambivalence: A multidimensional view of attitudes toward an organizational change. Academy of Management. The Academy of Management Review, 25(4), 783-794.

Pliskin, N. (1994). The role of clinical information systems in the linkage between health care providers and insurers. Journal of Information Technology Management, 5(2), 11-18.

Pliskin, N., Glezerman, M., Modai, I., & Weiler, D. (1996). Spreadsheet evaluation of computerized medical records: The impact on quality, time, and money. Journal of Medical Systems, 20(2), 85-100.

Reardon, J., L., & Davidson, E. (2007). An organizational learning perspective on the assimilation of electronic medical records among small physician practices. European Journal of Information Systems, 16(6), 681-694.

Reed, M., Brand , R., Newhouse, J. P., Selby , J. V., & Hsu, J. (2008). Coping with prescription drug cost sharing: Knowledge, adherence, and financial burden. Health Services Research, 43(2), 785-797.

Reynolds, P. A., Harper, J., Jenner, A. M., & Dunne, S. (2008). Better informed: An overview of health informatics. British Dental Journal, 204(5), 259-264.

Sagie, A., Elizur, D., & Greenbaum, C., W. (1985). Job experience, persuasion strategy and resistance to change: An experimental study. Journal of Occupational Behavior (pre-1986), 6(2), 157-162.

Sanders, K. M., & Satyvavolu, A. (2002). Improving blood pressure control in diabetes: limitations of a clinical reminder in influencing physician behavior. Journal of Continuing Education in the Health Profession, 22(1), 23-32.

Schur, C., L., Berk, M., L., & Yegian, J., M. (2004). Public perceptions of cost containment strategies: Mixed signals for managed care (11/10/2004). Health Affairs, 23(6), 284.

Sequist, T. D., Gandhi, T. K., Karson, A. S., Fiskio, J. M., Bugbee, D., Sperling, M., ... Bates, D. W. (2005). A randomized trial of electronic clinical reminders to improve quality of care for diabetes and coronary artery disease. Journal of the American Medical Informatics Association, 12(4), 431-437.

Shachak, A., Hadas-Dayagi, M., Ziv, A., & Reis, S. (2009). Primary care physicians’ use of an electronic medical record system: A cognitive task analysis. Journal of General Internal Medicine, 24(3), 341-348.

Shamliyan, T. A., Duval, S., Du, J., & Kane, R. L. (2008). Just what the doctor ordered. Review of the evidence of the impact of computerized physician order entry system on medication errors. Health Services Research, 43(1p1), 32-53.

Sittig, D. F., Krall, M. A., Dykstra, R. H., Russell, A., & Chin, H. L. (2006). A survey of factors affecting clinician acceptance of clinical decision support. BMC Medical Informatics and Decision Making, 6(1), 6-12.

Steinman, M., Sands, L., & Covinsky, K. (2001). Self-restriction of medications due to cost in seniors without prescription coverage. Journal of General Internal Medicine, 16(12), 793-799.

Subramanian, S., Hoover, S., Gilman, B., Field, T. S., Mutter, R., & Gurwitz, J. H. (2007). Computerized physician order entry with clinical decision support in long-term care facilities: Costs and benefits to stakeholders. Journal of the American Geriatrics Society, 55(9), 1451- 1457.

Tamblyn, R., Huang, A., Kawasumi, Y., Bartlett, G., Grad, R., Jacques, A., ... Pinsonneault, A. (2006). The development and evaluation of an integrated electronic prescribing and drug management system for primary care. Journal of the American Medical Informatics Association, 13(2), 148-159.

Tyler, T., Degoey, P., & Smith, H. (1996). Understanding why the justice of group procedures matters: A test of the psychological dynamics of the group-value model. Journal of Personality and Social Psychology, 70(5), 913-930.

Tyler, T. R. (1990). Why people obey the law: Yale University Press, New Haven.

Tyler, T. R., & Blader, S. L. (2000). Cooperation in groups: Procedural justice, social identity, and behavioral engagement. Philadelphia, PA: Psychology Press.

Vardy, D. A., Kayam, R., & Kitai, E. (2008). Community health: How to incentivize physcians. Harefuah, 147(12), 999-1003.

Vashitz, G., Meyer, J., Parmet, Y., Peleg, R., Goldfarb, D., Porath, A., & Gilutz, H. (2009). Defining and measuring physicians' responses to clinical reminders. Journal of Biomedical Informatics, 42(2), 317-326.

Weber, V., White, A., & McIlvried, R. (2008). An electronic medical record (EMR)-based intervention to reduce polypharmacy and falls in an ambulatory rural elderly population. Journal of General Internal Medicine, 23(4), 399-404.

Wolfstadt, J., Gurwitz, J., Field, T., Lee, M., Kalkar, S., Wu, W., & Rochon, P. A. (2008). The effect of computerized physician order entry with clinical decision support on the rates of adverse drug events: A systematic review. Journal of General Internal Medicine, 23(4), 451-458.

## Appendices

Appendix A.

![](/api/attachments/EJR9P5A3/fulltext/images/d679e8abdcb18d318448b9a4464cb704b1d07ad1bb22e16995b194aec753085e.jpg)

Appendix B.

Exhibit B-1. A Digital Form to Justify Drug Prescription When not Complying with Drug Substitute Recommendation  
![](/api/attachments/EJR9P5A3/fulltext/images/d046761ccb34bb7c730437ae3f060a5df325b3d340034daad2e3241bd12782b5.jpg)

## About the Authors

Tsipi HEART is a lecturer at the Department of Industrial Engineering and Management, Ben-Gurion University of the Negev in Israel. She has acquired her Ph.D. at Ben-Gurion University of the Negev (thesis winning the Highly Commended Award of the 2006 Emerald/EFMD Outstanding Doctoral Research Award in the category of Management and Governance), and her MBA from Tel-Aviv University, and B. Sc. in Computer Science from the Technion – Israeli Institute of Technology. Dr. Heart has joined Academia in 2005 after twenty years experience as an IS executive and consultant, and her research interests are within information systems innovation such as cloud computing and SaaS, and strategic impact of information systems particularly in healthcare. She has taught at the Business Information Systems Department, University College Cork in 2005-2007. Her work has been presented at conferences as ICIS and ECIS, and published in journals as INFOR, JITTA, IJEB, JGITM, IJMI, and MDM, among others.

Allon ZUKER is the Co-Founder, Chairman, and R&D Manager of Roshtov Software Inc. the developer of Clicks®, the most prevalent EMR software in Israel. Clicks® was adopted by the two largest Health Maintenance Organizations insuring 85% of Israel’s population, and is fully implemented since the early 1990s in primary and secondary care. Dr. Zuker has acquired his M.D. in 1980 and his Ph.D. in 2008 from Ben-Gurion University of the Negev, Israel. He served as a GP for several years and as the Vice-President for Technology and Services at the Soroka Academic Medical Center before turning to EMR systems development full time. He has published in several journals and is a popular speaker at professional conferences.

Yisrael PARMET is a Senior Lecturer of Statistics in the Department of Industrial, Engineering and Management (IEM) at Ben Gurion University of the Negev, Israel. He has a Master and Ph.D. degrees in Applied Statistic and a Bachelor degree in Statistics and Economics. During his postgraduate studies he served as a research assistant at the Statistical Laboratory at the Department of Statistics and Operations Research, Tel Aviv University. His research involves evaluation projects and statistical data analysis, which he presented at conferences and seminar. Dr. Parmet has been revising curricula in various courses in Statistics, and is teaching undergraduate and graduate courses.

Joseph S PLISKIN is the Sidney Liswood Professor of Health Care Management at Ben-Gurion University of the Negev. He is a member of the Department of Industrial Engineering and Management and of the Department of Health Systems Management, and is an Adjunct Professor at the Department of Health Policy and Management at the Harvard School of Public Health. He received his BSc degree in Mathematics and Statistics from the Hebrew University in Jerusalem (1969) and SM (1970) and PhD (1974) degrees in Applied Mathematics (Operations Research) from Harvard University. Dr. Pliskin's research interests focus on clinical decision making, operations management in health care organizations, cost-benefit and cost-effectiveness analysis in health and medicine, technology assessment, utility theory and decision analysis. He was the recipient of the "Career Achievement Award" from the Society for Medical Decision Making in 2005. He has published extensively on issues relating to end stage renal disease, heart disease, Down syndrome, technology assessment and methodological issues in decision analysis. He is co-author of the book Decision Making in Health and Medicine: Integrating Evidence and Values (Cambridge University Press, Cambridge, UK, 2001), and the book Focused Operations Management for Health Services Organizations (Jossey-Bass, San-Francisco, 2006).

Nava PLISKIN is a tenured full Professor at the Department of Industrial Engineering and Management, Ben-Gurion University of the Negev in Israel, where she has been a senior faculty member since 1985 and is in charge of the Information Systems programs. The Harvard Business School invited her during 1996- 1997 to serve as a Visiting Associate Professor and hold the Thomas Henry Carroll Ford Foundation Chair. Professor Pliskin is conducting research in topics related to IS management and strategy, focusing on longitudinal analysis of IS impacts at the global, national, organizational, and individual levels, and her research papers have been published in conference proceedings (most recently ICIS2008) and in such leading journals as: ACM Transactions on Information Systems, Information Society, Communications of the ACM, IEEE Transactions on Engineering Management, and Decision Support Systems. The Ph.D. and S.M. degrees she acquired are from Harvard University and the B.Sc. degree is from Tel-Aviv University.
