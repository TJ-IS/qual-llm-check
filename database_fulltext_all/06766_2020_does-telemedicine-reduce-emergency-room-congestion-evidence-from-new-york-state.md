---
otero_id: 6766
otero_key: "REEW3KC3"
title: "Does Telemedicine Reduce Emergency Room Congestion? Evidence from New York State"
authors: "Shujing Sun; Susan F. Lu; Huaxia Rui"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2020.0926"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/REEW3KC3/fulltext/images/88a0832df303dec2e9e1a91c8b010ce1296cd3644809ec666b9ee115ccbe2e0a.jpg)

# Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Does Telemedicine Reduce Emergency Room Congestion? Evidence from New York State

Shujing Sun, Susan F. Lu, Huaxia Rui

To cite this article:

Shujing Sun, Susan F. Lu, Huaxia Rui (2020) Does Telemedicine Reduce Emergency Room Congestion? Evidence from New York State. Information Systems Research

Published online in Articles in Advance 27 Aug 2020

https://doi.org/10.1287/isre.2020.0926

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Does Telemedicine Reduce Emergency Room Congestion? Evidence from New York State

Shujing Sun,<sup>a</sup> Susan F. Lu,<sup>b</sup> Huaxia Rui<sup>a</sup>

<sup>a</sup> Simon Business School, University of Rochester, Rochester, New York 14627; <sup>b</sup> Krannert School of Management, Purdue University, West Lafayette, Indiana 47907

Contact: shujing.sun@simon.rochester.edu, https://orcid.org/0000-0002-5181-1722 (SS); lu428@purdue.edu, https://orcid.org/0000-0001-5852-0816 (SFL); huaxia.rui@simon.rochester.edu, https://orcid.org/0000-0001-6727-1479 (HR)

Received: Revised: March 19, 2019; September 5, 2019; March 1 Accepted: Published Online in Articles in Advance: August 27, 2020

https://doi.org/10.1287/isre.2020.0926

Copyright:

Abstract. Overcrowding in emergency rooms (ERs) is a common yet nagging problem. It not only is costly for hospitals but also compromises care quality and patient experience Hence, finding effective ways to improve ER care delivery is of great importance. Using a large data set covering all emergency visits in New York State from 2010 to 2014, we investigate whether telemedicine enhances ER care delivery. We show that, on average, telemedicine availability in the ER significantly reduces average patients’ length of stay (LOS), which is partially driven by the flexible resource allocation. Specifically, the adoption of telemedicine leads to a larger reduction in ER LOS when there is a demand surge or supply shortage. Furthermore, such improvement is not a by-product of other widely adopted health IT applications and does not come at the expense of care quality or patient cost. We also replicate the analysis using annual U.S. hospital data and find that ER telemedicine adoption significantly reduces average patients’ waiting time, which suggests that the LOS reduction partially comes from the reduction of waiting time.

History: Eric Zheng, Senior Editor; Yili Hong, Associate Editor. Supplemental Material: The online appendices are available at https://doi.org/10.1287/isre.2020.0926.

Keywords: telemedicine • emergency department • overcrowding • health information technology • length of stay • waiting time • service tim

## 1. Introduction

Emergency rooms (also known as emergency departments; hereafter denoted as ERs) are often crowded, intimidating, and expensive places to be. In the United States, ER physicians constitute less than 5% of the physician workforce yet manage 28% of acute care encounters (Pitts et al. 2010). According to the National Hospital Ambulatory Medical Care Survey, from 2000 to 2015, the number of ER visits in the United States increased by 26.8%, from 108 million to 136.9 million. With the sharp rise in emergency visits and critical shortages of emergency physicians, ER overcrowding continues to intensify. Such congestion leads to various disturbing effects: worse patient outcomes due to delayed treatment, higher dissatisfaction rates due to prolonged pain and suffering, decreased physician productivity due to overwork, and increased financial costs for unnecessary diagnostic investigation (Hoot and Aronsky 2008, Boyle et al. 2012, Chang et al. 2018). Given the various adverse effects caused by ER overcrowding, finding effective ways to improve ER care delivery becomes an urgent task for every healthcare decision maker. Therefore, the central goal of this paper is to examine whether telemedicine can reduce ER congestion.

Telemedicine, a type of health information technology (hereafter denoted as HIT), is defined as the “remote delivery of healthcare services and clinical information using telecommunications technology.”<sup>1</sup> Although an ER seems to be the most unlikely place for telemedicine to play its role, it is happening. The Wall Street Journal recently reported an ER telemedicine initiative at New York-Presbyterian Hospital, which aims to reduce waiting times and get patients with nonurgent cases in and out of the emergency room efficiently without compromising care.<sup>2</sup> For patients who received treatment through this program, their total amount of time spent in the ER dropped from an average of 2–2.5 hours to only 35–40 minutes. The efficiency gain does not necessarily come at the expense of lower care quality because patients have the on-the-ground resources of a hospital, and on-site nurse practitioners or physician assistants are available to assist with care. Peter Greenwald, an emergency medicine physician in the program, says that the definition on the Avizia telemedicine cart they use “is better than the naked eye.” In another example,<sup>3</sup> at the ER telemedicine program at the University of California San Diego Medical Center, the average ER wait for those participating patients was about half of the minutes posted in the Hospital Compare da tabase.<sup>3</sup> Both programs reported positive patient experiences during treatment because they got more and undivided attention from doctors, even though they do not see the doctors in the flesh.

Although these pilot programs show the great promise of telemedicine application in ERs, only 10.7% of U.S. hospitals had such adoptions as of 2014. Given the anecdotal evidence of the effects of telemedicine in ERs, we believe it is time to provide healthcare decision makers with more analytics regarding these effects. Toward this goal, we need to carefully examine how care delivery efficiency, care quality, and medical expenditure in ERs change after adopting telemedicine. Like many other studies on the implications of technology adoption, the main challenge that we face is the causal inference with observational data, because the adoption decision is not random and it is impractical to conduct randomized experiments, especially in the ER setting. To meet the challenge, we use a combined approach of difference-in-differences (DID) analysis and various sampling strategies. We find that adopting telemedicine achieves a significant reduction in ER patients’ length of stay (LOS) and waiting time. Our main finding is consistently supported by multiple robustness checks and falsification tests. We also empirically test and find that the length-of-stay reduction is partially driven by the flexible resource allocation that was made available due to telemedicine, as we observe a larger efficiency gain when an ER encounters demand surges or physician supply shortages. Furthermore, we find no evidence that the efficiency improvement sacrifices patient care quality or increases medical expenditures.

The rest of the paper is organized as follows: Section 2 provides a literature review. Section 3 develops the hypotheses. Section 4 describes the data used for this study. Sections 5 and 6 discuss the empirical models and report estimation results. Section 7 presents robustness checks to further evaluate the validity of the main findings. Section 8 concludes the paper and acknowledges its limitations.

## 2. Research Background

Our paper closely relates to the literature on ER overcrowding and telemedicine. We review these two streams of research in this section.

## 2.1. ER Overcrowding: Causes, Consequences, and Solutions

ER overcrowding has become a widespread phenomenon in U.S. hospitals. Hoot and Aronsky (2008) classify the causes of ER overcrowding into three categories: input factor (e.g., nonurgent visits, influenza season), throughput factor (e.g., inadequate staffing), and output factor (e.g., inpatient boarding, hospital bed shortages). Enacted in 1986, the Emergency Medical Treatment and Active Labor Act (EMTALA) mandates that any emergency department provide care to all individuals seeking treatment for a medical condition, regardless of citizenship, legal status, or ability to pay.<sup>4</sup> As a result of this act, many patients go to the ER if they cannot get treatment otherwise, thus causing additional patient load. Despite EMTALA’s intention to make ERs a safety net of the healthcare system, the overcrowding problem has strained this safety net to the breaking point (Hoot and Aronsky 2008).

Considered as “the greatest threat to the viability of the U.S. emergency care system” (Trzeciak and Rivers 2003), ER overcrowding disturbs the normal operation of hospitals and reduces care quality for patients. For example, long waiting times and treatment delays lead to poor care quality (high mortality/readmission rate), increase financial costs, reduce patients’ satisfaction, and impair physician efficiency (Hoot and Aronsky 2008). Therefore, reducing ER overcrowding to improve operational efficiency and healthcare quality is on the top of every healthcare decision maker’s to-do list.

Given the various adverse effects caused by ER congestion, researchers have examined different interventions. There are several traditional approaches from the perspective of operations management, ranging from increasing capacity (Trzeciak and Rivers 2003) and establishing fast tracks for nonurgent patients (Considine et al. 2008) to improving scheduling (Sinreich et al. 2012) and flow management (Imperato et al. 2012, Song et al. 2015). These approaches are effective to some extent, but the implementation may not always be feasible, both financially and legally For example, hospitals often have budget constraints, and they cannot freely increase capacity due to the certificate-of-need restrictions on the provision of healthcare.<sup>5</sup> More importantly, the substantial volatility in arrival and service times makes it very difficult for proper capacity planning. Overcapacity leads to empty beds and idle staff in nonpeak hours and results in high operating costs, and low capacity delays treatment and leads to poor care quality.

In this paper, we investigate the potential of telemedicine as a generic solution to the ER overcrowding problem. There are several pioneering works linking HIT applications and ER efficiency. For example, Janakiraman et al. (2017) and Ayer et al. (2019) find that health information exchange (HIE) adoption reduces ER lengths of stay through better information coordination among healthcare providers. Our paper closely relates to these papers but also differs in important ways. Whereas HIT applications such as electronic medical record (EMR) and HIE focus on information recording and sharing, telemedicine focuses on remotely delivering clinical care. Besides the IT infrastructure, telemedicine functions very differently because it relies on two sources of labor input: on-site nurses/physicians and off-site physicians. Therefore, we cannot extrapolate the existing evidence of HIT to the application of ER telemedicine without a thorough empirical investigation.

## 2.2. Telemedicine

2.2.1. General Background of Telemedicine. Although the definition of telemedicine varies slightly from source to source, the essence of most definitions is “the delivery of health care services at a distance, using information and communication technology” (Ward et al. 2015, p. 602). According to the American Telemedicine Association, telemedicine includes a wide array of clinical services using different communication tools. For example, from the dimension of functionality, telemedicine service includes consultation between physicians or between providers and patients; remote diagnosis by specialists relying on transferred images, records, and laboratory results; home monitoring of discharged patients; and remote mentoring specialists, such as surgeons performing new or complicated procedures (Bashshur et al. 2011; Rajan et al. 2013, 2019). Telemedicine application relies on different types of communication structures, including real-time audio/visual communication, image transfer, telephone, email, and so on. In this paper, we focus on the context of telemedicine application (i.e., ER) and do not distinguish differences in formats.

Anecdotal evidence suggests that the equipment cost for telemedicine is not high.<sup>6</sup> Typically, physicians just need portable computer carts with videoconference capability and some diagnostic tools. With the rapid advancement of technology, care quality through telemedicine services has been consistently improving, resulting in high patient satisfaction and overall positive experiences. The major obstacle comes from collaboration among providers and payers, particularly concerning reimbursement policies, but there are encouraging signs of progress.<sup>7</sup>

2.2.2. Literature on ER Telemedicine. To the best of our knowledge, only a few papers investigate the effect of telemedicine usage related to ER. For example, two recent papers examined the effect of telemedicine consultation for geriatric patients in nursing homes (Yeow and Huat Goh 2015) and senior living communities (Gillespie et al. 2016). In these telemedicine applications, patients first consult remote physicians about an acute illness and then decide whether to visit the hospital for treatment. Both papers suggest that the telemedicine outreach program reduces the number of unnecessary ER visits for geriatric patients.

A few papers in the medical literature have discussed telemedicine applications in emergency rooms. However, limited evidence was available about the change in LOS and “the rigor of the studies was limited and needs additional support” (Ward et al. 2015, p. 615). Besides, these papers are mostly case studies focusing on small samples and specific disease types, which might have led to inconclusive findings.<sup>8</sup> For example, by comparing 24 patients treated before telemedicine adoption and 38 patients treated after telemedicine adoption, Southard et al. (2014) examine the effectiveness of emergency telemental service in a rural emergency room. They find that the average ER LOS reduced from 31.7 hours to 17.0 hours for mentally ill patients, which accounts for 46% reduction at the mean. Through a cohort study of adult trauma patients in North Dakota Critical Access Hospital Emergency Departments, Mohr et al. (2018) find that the effect of telemedicine is inconclusive. Specifically, telemedicine utilization associates with decreased initial ER LOS by 30 minutes for transferred trauma patients but has no effect on those not transferred.

Given the high costs of healthcare decision-making and the ethical concerns of conducting a large-scale randomized experiment among ERs, making causal inferences from observational data is an important research task that will benefit healthcare decision makers. Through a unique longitudinal data set that includes outpatient records and data on the availability of telemedicine in the ERs that they visited, this paper aims to obtain a more comprehensive understanding of the application of ER telemedicine and its potential impact on ER care delivery efficiency, care quality, and medical expenditures.

## 3. Development of Hypotheses

We develop the hypotheses in this section to conceptualize the mechanisms through which telemedicine can affect ER care delivery. Since telemedicine overcomes the distance barrier by enabling real-time interactions between patients and off-site physicians, it can potentially increase ER care delivery through the following channels.

First, ER telemedicine can increase on-call providers’ efficiency through transportation time elimination and smoother workflows. Although on-call physicians are often available when there is an influx of emergency patients, there is often a long lag before they arrive at the ER, thereby delaying the treatment. In contrast, contacting on-call physicians via telemedicine eliminates transportation time, thus significantly shortening patients’ wait for on-call physicians. Besides, having an on-call physician through telemedicine can speed up the ordering of laboratory work, so that those processes can start long before they otherwise would, thereby reducing physicians’ idle time.

Second, telemedicine can potentially address the problem of inadequate on-site physician staffing via flexible remote resource allocation. Due to the high cost of compensating on-call physicians, more and more hospitals lost the ability to provide coverage for on-call specialties on a 24-hour, seven-day-a-week basis, which is a key cause for ER overcrowding (McConnell et al. 2008, Rao et al. 2010). With telemedicine adoption, ERs can rely on a much larger pool of off-site physicians, since physicians can work for multiple hospitals from their office. For instance, during after-hours, emergency physicians can remotely consult off-site radiologists for correct interpretations of medical images and better treatment of patients with complex cases.<sup>9</sup>

Telemedicine also makes it easier for hospitals to collaborate and form a medical resource-sharing network, which helps patients access remote specialists who would not have been available otherwise. For example, whether a stroke patient should tissue plasminogen activator is a crucial and complicated medical decision. However, some hospitals lack such expertise. Through a telestroke program, a type of ER telemedicine application, stroke specialists can remotely perform real-time diagnoses and recommend treatment plans. As Dr. Lee Schwamm from Massachusetts General Hospital commented about the benefits of their telestroke program, “I can examine someone very interactively with the help of a physician or a nurse on the other end and I can make a determination of the stroke severity and the type of stroke by looking at the patient and at the brain image. It’s almost like being in the room.”<sup>10</sup>

Third, since the EMTALA has mandated that hospitals provide care to all individuals seeking treatment for a medical condition, ERs have become the safety net for those with access barriers. For example, patients who desire immediate care for convenience, who are uninsured, or who lack the usual source of care, might seek help from the ER (Boyle et al. 2012). Previous research shows that nurse practitioners (NPs) and physician assistants (PAs) are capable of filling the inadequate supply of providers when on-site physicians are unavailable. Yet, many states in the United States limit the scope of their practice and require attending physicians’ supervision (Naylor and Kurtzman 2010, Wiler and Ginde 2015). Telemedicine can potentially solve the problem because physicians can now remotely supervise NPs/PAs to treat patients with minor cases in a more convenient way.

While telemedicine seems to have great potential in improving ER care delivery, in practice, it can lead to unintended consequences due to possible frictions associated with coordination issues and technical limitations. First, information exchange highly relies on trust and relationship-building (Serrano and Karahanna 2016), and virtual communication through telemedicine may not be as effective as the on-site face-to-face service. Second, the effective use of telemedicine requires IT training and workflow restructuring. Noncompliance of IT staff or providers may hinder its usage or even delay the treatment. In addition, ER telemedicine needs two sources of labor input—onsite nurses/physicians and off-site physicians—and constraints from any sources or coordination difficulties among the two parties may lead to unchanged or even worse care delivery. Third, technological limitations may restrain physicians’ ability to fully diagnose patients because they cannot acquire sensory information (e.g., touch, smell) through telemedicine (Miller 2003), thereby slowing down the diagnosis and treatment process. Furthermore, technical glitches sometimes disrupt the treatment pro cess and negatively affect the continuity of care, thus introducing new inefficiency. Therefore, whether telemedicine can improve ER care delivery efficiency is ultimately an empirical question. To directly test this, we propose the following hypothesis.

## Hypothesis 1. ER telemedicine adoption leads to more efficient ER care delivery (measured by shorter LOS).

If telemedicine can improve efficiency through flexible resource allocation, we shall expect a larger effect when patient demand surges or when physician supply is in shortage, because these are situations in which hospitals are likely to use telemedicine more extensively. To capture the demand variation, we construct the variable EROccupancy following previous literature (Kuntz et al. 2015, Berry Jaeker and Tucker 2017, Freeman et al. 2017) and provide the construction details in Online Appendix B. The variable EROccupancy stands for the occupancy level in hospital j at patient i’s arrival time t, which captures the occupancy variation over time within an ER. The higher the value of EROccupancy, the more congested an ER is. If telemedicine enables hospitals to dispatch remote physicians flexibly, then we shall see a larger reduction in LOS when an ER becomes more congested. Accord ingly, we propose the following hypothesis.

## Hypothesis 2A. The effect of ER telemedicine adoption is larger, in terms of a larger reduction in LOS, when an ER encounters a demand surge.

We proxy supply variation using the staffing level difference between business-hours and after-hours. Previous literature suggests that there is limited availability of physician resources during after-hours (Rao et al. 2010, O’Malley 2012, Anderson et al. 2014). If telemedicine serves as a flexible way to connect oncall doctors, then we shall expect a larger efficiency improvement for patients who visited the ER during after-hours, when there is a higher chance to summon on-call specialists. Accordingly, we propose the following hypothesis.

Hypothesis 2B. The effect of ER telemedicine adoption is larger, in terms of a larger reduction in LOS, when an ER encounters a supply shortage.

## 4. Data

We obtain the data from two sources: the Healthcare Information and Management Systems Society (HIMSS) Dorenfest Survey and the New York State Emergency Department Database (SEDD) of the Healthcare Cost and Utilization Project (HCUP). The HIMSS database provides telemedicine adoption status for U.S. health facilities starting from 2010. The HCUP/SEDD captures discharge information for all ER visits that do not result in an inpatient admission.<sup>11</sup> We supplement the main data set with the waiting-time measure from the Hospital Compare database. We employ the hospital identifiers from the American Hospital Association database (AHA Annual Survey) to merge these data sets. The HIMSS data suggest that the ER telemedicine application is still in a very early stage. Until 2014, only 10.70% of hospitals have implemented such technology in their ERs. New York State has relatively higher adoption rates than the national average. Starting from 5.68% in 2010, ER telemedicine adoption rate in New York State increased to 12.5% in 2014 (see Table 1).

## 4.1. Variables

In this study, we choose LOS as the primary outcome measure, which is the door-out time minus door-in time for ER patients. HCUP/SEDD data provide the admission hour, the discharge hour, and the number of days staying in an ER at the patient level, which allows us to calculate the total hours a patient spent in the ER from being admitted until being discharged.

In addition to LOS, we also test the effect of ER telemedicine adoption on patient care quality and medical expenditure. Following the healthcare literature, we proxy care quality as the 30-day readmission and in-hospital mortality risk (Bardhan et al. 2014, Song et al. 2015, Lu and Rui 2018). We track patients using the visit linkage variable in HCUP and generate a 30-day readmission indicator that equals 1 (and 0 otherwise) if a patient revisited a hospital for any purpose (including ER and inpatient visits) within 30 days of ER discharge. By counting readmission across hospitals and visit types, we can better capture any potential risks following an ER visit and avoid underestimation of care quality shift (Bardhan et al. 2014). We define the in-hospital mortality indicator as 1 if a patient died during an ER visit. We proxy patients’ medical expenditure using the edited total charges (in U.S. dollars) from the HCUP/ SEDD database.

To adjust for any potential shifts of patient composition over time, we control for individual health conditions, demographic information, payer type, and diagnoses. We also control for hospital size, patient volume, and other health IT applications to account for hospital-level confounding factors that may correlate with ER telemedicine adoption and care delivery.<sup>12</sup>

## 4.2. ER Telemedicine Adoption Decision

In an ideal research design, telemedicine should be randomly assigned so that we can cleanly identify how its adoption affects ER care delivery. In reality, hospitals do not make random adoption decisions, thus making endogeneity a major concern for our analysis. Whereas we can include hospital fixed effects to control for time-invariant confounding factors, it is hard to control for all the time-varying confounding factors. For example, hospitals that anticipate a higher increase in ER LOS may have more incentives to adopt telemedicine if they believe such adoption can help reduce LOS. Such endogeneity wil underestimate the true effect of ER telemedicine. On the other hand, if ER telemedicine adoption is part of a hospital efficiency improvement initiative unobserved by researchers, such endogeneity will then overestimate the true effect of ER telemedicine.

Before alleviating these endogeneity concerns in the following sections, we first investigate what types of hospitals are likely to adopt telemedicine in ERs.

Table 1. Telemedicine Adoption Status in the United States and New York State

<table><tr><td rowspan="2">Year</td><td colspan="3">United States</td><td colspan="3">New York State</td></tr><tr><td>Frequency</td><td>tele (%)</td><td>tele_er (%)</td><td>Frequency</td><td>tele (%)</td><td>tele_er (%)</td></tr><tr><td>2010</td><td>5,283</td><td>21.11</td><td>4.32</td><td>176</td><td>22.73</td><td>5.68</td></tr><tr><td>2011</td><td>5,301</td><td>25.49</td><td>5.34</td><td>188</td><td>27.66</td><td>5.85</td></tr><tr><td>2012</td><td>5,372</td><td>28.85</td><td>6.66</td><td>179</td><td>30.73</td><td>5.59</td></tr><tr><td>2013</td><td>5,373</td><td>33.95</td><td>9.25</td><td>177</td><td>32.20</td><td>9.60</td></tr><tr><td>2014</td><td>5,344</td><td>38.96</td><td>10.70</td><td>184</td><td>37.50</td><td>12.5</td></tr><tr><td>Mean</td><td></td><td>29.70</td><td>7.27</td><td></td><td>30.20</td><td>7.85</td></tr></table>

Note. The tele (%) column shows the telemedicine adoption rate in any department (including ER and non-ER applications), and the tele\_er (%) column shows the adoption rate in ERs.

To do so, we conduct a probit analysis using a crosssectional data set that contains hospital-level characteristics prior to the adoption.<sup>13</sup> We define the dependent variable as 1 if a hospital adopted ER telemedicine by the end of 2014 and 0 otherwise. The independent variables include key hospital process measures and average patients’ characteristics. We find no correlation between previous patients’ LOS and the telemedicine adoption, which alleviates the endogeneity concern that past performance could have driven the adoption decision and thus bias the estimation. However, we do find that the likelihood of telemedicine adoption positively associates with ER patient volume and negatively associates with hospital size. In other words, a simple comparison between adopters and nonadopters without careful consideration of the endogeneity problem may bias the estimates of the adoption effect.

## 5. Empirical Strategies

Our empirical strategies consist of two parts: the DID model specification and the matching-based sample construction. We describe these two aspects separately.

## 5.1. Model Speci<sup>fi</sup>cation

To test whether the adoption of telemedicine can improve ER care delivery efficiency, we conduct the standard DID regression with multiple groups and time periods following previous literature (Angrist and Pischke 2008, Ayabakan et al. 2017, Ayer et al. 2019). The unit of analysis is a patient’s ER visit, and the primary specification of interests is the following:

$$
\begin{array}{r} Y _ {i j t} = \beta_ {0} + \beta_ {1} t e l e \_ e r _ {j t} + \gamma X _ {i j t} + \delta Z _ {j t} + H o s F E _ {j} \\ + T i m e F E _ {t} + \epsilon_ {i j t}. \end{array}\tag{1}
$$

The dependent variable $Y _ { i j t }$ corresponds to patient $i ^ { \prime } \mathrm { s }$ outcome measures, such as LOS in hospital j at time t. The main variable of interest, tele er , is the ER telemedicine adoption status in hospital j at time t, and $\beta _ { 1 }$ is the DID coefficient that captures the effect of telemedicine adoption.<sup>14</sup>

We include visit-specific characteristics, $X _ { i j t }$ , for patient i treated in hospital j at time t. We control timevarying hospital characteristics, $Z _ { j t . }$ , for hospital j at time t, which includes hospital size measure, patient volume, and the adoption status for several other health IT applications that may affect ER care delivery efficiency. We include both hospital fixed effects and time fixed effects such as the year effect, quarterly seasonality effect, and hour-of-day seasonality effect.

## 5.2. Sample Construction

During our sample period from 2010 to 2014, there are three types of hospitals: always adopters (hospitals that adopted ER telemedicine in 2010 or before), newly adopters (hospitals that adopted ER telemedicine in 2011, 2012, 2013, or 2014), and nonadopters (hospitals that had not yet adopted ER telemedicine by the end of 2014). The first sample includes newly adopters and nonadopters, which is the typical sampling method in DID analysis (please see Table 2 for summary statistics). As is discussed in Section 4.2, even though we control a large number of covariates in our analyses, there might still be unobserved timevarying confounding factors that could bias our estimates. To further alleviate the endogeneity concerns, we construct two alternative samples so that assignments of hospitals in the treatment and control groups more closely resemble the randomized assignment of ER telemedicine adoption.

The first alternative sample is based on propensity score matching (PSM) (Rosenbaum and Rubin 1983). We conduct the matching using a cross-sectional sample of newly adopters and nonadopters and in clude all the key variables that affect the probability of getting treated or potentially correlate with the out come variable.<sup>15</sup> Using propensity score matching with the number of nearest neighbor specified as 3 and a caliper of 0.25 standard deviation of the propensity score (Rosenbaum and Rubin 1983, Stuart 2010), we end up with 23 hospitals in the control group and 10 hospitals in the treatment group.<sup>16</sup> The matched sample is balanced (see panel A of Table A2 in Online Appendix A) and the total number of observations without missing variables is 2,848,135 over the sample period (see Table A3 in Online Appendix A).

While the traditional PSM method can address selection bias on observed characteristics, it cannot fully capture the unobserved differences among newly adopters and nonadopters. Inspired by previous literature (Brot-Goldberg et al. 2017, Bapna et al. 2018), we construct the second alternative sample using newly adopters and always adopters, with always adopters being the control group. The intuition behind this approach is as follows: since both the control (always adopters) and the treatment group (newly adopters) ultimately choose to adopt ER telemedicine, this approach accounts not just for the observed characteristics, but potentially also for some unobserved time-varying characteristics that are related to a hospital’s intrinsic propensity to adopt. We conduct a balance check and find that the resulting control ERs are highly comparable to the treated, as reflected by the statistically insignificant standardized difference in means for all the key covariates (see panel B of Table A2 in Online Appendix A).

## 6. Main Results

In this section, we execute the empirical strategies in the previous section and report the estimation results using different samples.

Table 2. Summary Statistics for Newly Adopters and Nonadopters

<table><tr><td colspan="5">New York State patient-level data (2010–2014)</td></tr><tr><td>Variable</td><td>Number of observations</td><td>Mean</td><td>Standard deviation</td><td>Definition</td></tr><tr><td colspan="5">Outcome measure (at the visit level)</td></tr><tr><td>LOS</td><td>17,573,681</td><td>4.11</td><td>6.16</td><td>Length of stay in hours</td></tr><tr><td>Medical expenditure</td><td>17,523,130</td><td>1,911</td><td>2,475</td><td>Total charges for the visit in U.S. dollars</td></tr><tr><td>30-day readmission</td><td>17,573,681</td><td>0.18</td><td>0.38</td><td>30-day all-cause hospital readmission indicator</td></tr><tr><td>In-hospital mortality</td><td>17,573,681</td><td>0.002</td><td>0.044</td><td>In-hospital death indicator</td></tr><tr><td colspan="5">Patient characteristics (at the visit level)</td></tr><tr><td colspan="5">Health conditions</td></tr><tr><td>Charlson Comorbidity Index (CCI)</td><td>17,573,681</td><td>0.20</td><td>0.58</td><td>Patient&#x27;s CCI at admission</td></tr><tr><td colspan="5">Demographic Information</td></tr><tr><td>Age</td><td>17,573,681</td><td>36.69</td><td>22.72</td><td>Patient&#x27;s age in years at admission</td></tr><tr><td>Gender</td><td>17,573,681</td><td>0.55</td><td>0.50</td><td>Patient&#x27;s gender indicator (1 if female)</td></tr><tr><td>Race</td><td></td><td></td><td></td><td>Patient&#x27;s race indicator.</td></tr><tr><td>White</td><td>17,573,681</td><td>0.52</td><td>0.50</td><td></td></tr><tr><td>Black</td><td>17,573,681</td><td>0.21</td><td>0.41</td><td></td></tr><tr><td>Other race</td><td>17,573,681</td><td>0.27</td><td>0.44</td><td></td></tr><tr><td>Core based statistical area (CBSA)</td><td></td><td></td><td></td><td>Patient&#x27;s location indicator</td></tr><tr><td>Non-CBSA</td><td>17,573,681</td><td>0.04</td><td>0.18</td><td></td></tr><tr><td>Micropolitan statistical area</td><td>17,573,681</td><td>0.11</td><td>0.31</td><td></td></tr><tr><td>Metropolitan statistical area</td><td>17,573,681</td><td>0.86</td><td>0.35</td><td></td></tr><tr><td>Payer type</td><td></td><td></td><td></td><td>Patient&#x27;s payer type indicator</td></tr><tr><td>Medicare</td><td>17,573,681</td><td>0.15</td><td>0.36</td><td></td></tr><tr><td>Medicaid</td><td>17,573,681</td><td>0.31</td><td>0.46</td><td></td></tr><tr><td>Private</td><td>17,573,681</td><td>0.36</td><td>0.48</td><td></td></tr><tr><td>Other</td><td>17,573,681</td><td>0.17</td><td>0.38</td><td></td></tr><tr><td colspan="5">Visit-specific information</td></tr><tr><td>EROccupancy</td><td>17,573,681</td><td>0.65</td><td>0.77</td><td>ER occupancy rate at admission</td></tr><tr><td>ER volume</td><td>17,573,681</td><td>117.37</td><td>68.58</td><td>ER volume at admission</td></tr><tr><td>ER telemedicine (tele_er)</td><td>17,573,681</td><td>0.03</td><td>0.17</td><td>ER telemedicine statistics at the visit level</td></tr><tr><td colspan="5">Hospital characteristics (at the hospital level, full New York State sample)</td></tr><tr><td>ER telemedicine (tele_er)</td><td>904</td><td>0.08</td><td>0.27</td><td>ER telemedicine adoption status</td></tr><tr><td>non-ER Telemedicine (tele_other)</td><td>904</td><td>0.19</td><td>0.39</td><td>non-ER telemedicine adoption status</td></tr><tr><td>Beds</td><td>904</td><td>287</td><td>204</td><td>Number of licensed beds in hospital</td></tr><tr><td colspan="5">Other HIT</td></tr><tr><td>EMR</td><td>904</td><td>0.92</td><td>0.27</td><td>Electronic medical record adoption status</td></tr><tr><td>EDIS</td><td>904</td><td>0.78</td><td>0.41</td><td>General ER information systems adoption status</td></tr><tr><td>HIE</td><td>591</td><td>0.78</td><td>0.42</td><td>Health information exchange adoption status</td></tr></table>

Notes. We also include the following covariates that are not reported here due to page limits: patient’s major diagnosis code based on HCUP multilevel diagnoses categorization; median household income quartile corresponding to patient’s ZIP code; and seasonality (admission hour, discharge quarter, year). The HIE variable is missing in the HIMSS 2011 data. For readability, we denote telemedicine adoption in ERs as tele er in the regression specifications and ER telemedicine in the result tables.

## 6.1. Effect on LOS

Table 3 reports the regression results using different specifications and samples. Columns 1–2 report the results on the sample of newly adopters and nonadopters without matching. Columns 3–4 report the results on the matched sample of newly adopters and nonadopters. Columns 5–6 report the results on the sample of newly adopters and always adopters. We show the results estimated by the baseline specification in those columns with odd numbers. To disentangle the effect of telemedicine from other health IT applications, we also run regressions controlling for other HIT adoptions. Those columns with even numbers report this set of results.

Taking column 3 as an example, we observe a significantly negative DID coefficient, suggesting that the adoption of telemedicine results in a significant reduction in ER LOS. The DID coefficient remains significant after accounting for other HIT applications, implying that the effect of telemedicine is not a mere reflection of other widely adopted HIT applications. As shown in column 4, telemedicine adoption shortens the LOS by 1.3 hours on average, which accounts for a 31% reduction in LOS at the mean. Overall, regardless of the differences in sampling and model specifications, the results in Table 3 consistently support Hypothesis 1.

## 6.2. Mechanism Discussion

To understand the sources of efficiency gain, we dedicate this section to mechanism tests.

6.2.1. Flexible Resource Allocation. As is discussed in Section 3, a potential mechanism is the flexible remote resource allocation. To empirically test this mechanism, we examine the heterogeneous effects of ER telemedi cine using the following specification:

$$
\begin{array}{r l} Y _ {i j t} = & \beta_ {0} + \beta_ {1} t e l e \_ e r _ {j t} + \beta_ {2} t e l e \_ e r _ {j t} \times M o d e r a t o r _ {i j t} \\ & + \beta_ {3} M o d e r a t o r _ {i j t} + \gamma X _ {i j t} + \delta Z _ {j t} + H o s F E _ {j} \\ & + T i m e F E _ {t} + \epsilon_ {i j t}, \end{array}\tag{2}
$$

where Moderator stands for the occupancy measure (EROccupancy) or after-hours indicator (After-hours), depending on different tests.

Columns 1, 3, and 5 of Table 4 report the heterogeneous effect of telemedicine adoption by ER occupancy level using different samples. Taking column 3 as an example, the DID coefficient is negatively significant, suggesting that ER telemedicine adoption leads to the reduction of LOS even when there is minimal congestion. The coefficient of the interaction term ER telemedicine  EROccupancy is 0.473 at a 5% significance level. Translating into the magnitude, one standard deviation increase in the ER occupancy level is associated with 0.5 hour, or a 12% reduction in average patients’ LOS at the mean after ER telemedicine adoption. Overall, the results suggest that efficiency improvement due to ER telemedicine adoption is more salient during the time of congestion, which supports the flexible resource-allocation channel in response to demand surge (Hypothesis 2A).

Columns 2, 4, and 6 of Table 4 report the heterogeneous results by patients’ arrival time. Taking column 4 as an example, after-hour visits experience 0.442 hour (or 10.4%) more reduction in LOS than business-hour visits controlling for the ER volume at the hour level. Our finding supports the proposed channel that telemedicine helps address the supply shortage of physicians (Hypothesis 2B). All the results

Table 3. Effect of ER Telemedicine on Patient LOS

<table><tr><td rowspan="2"></td><td colspan="2">AN</td><td colspan="2">PSM-AN</td><td colspan="2">AA</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td></tr><tr><td>ER telemedicine</td><td>-0.652***(0.205)</td><td>-0.661***(0.208)</td><td>-1.251**(0.569)</td><td>-1.316**(0.566)</td><td>-0.648***(0.225)</td><td>-0.708***(0.213)</td></tr><tr><td>Other HIT</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>Patient and hospital control</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time and hospital fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Number of observations</td><td>17,573,681</td><td>17,573,681</td><td>2,848,135</td><td>2,848,135</td><td>2,099,780</td><td>2,099,780</td></tr><tr><td> $R^2$ </td><td>0.129</td><td>0.129</td><td>0.239</td><td>0.244</td><td>0.234</td><td>0.234</td></tr></table>

Notes. This table reports DID regression results using New York State SEDD individual patient data from 2010 to 2014, where the dependent variable is the patient’s length of stay (LOS) in hours. AN stand for the sample of newly adopters and nonadopters. PSM-AN stands for the matched sample of newly adopters and nonadopters. AA stands for the sample of newly adopters and always adopters. Col umns 1, 3, and 5 show the baseline results. Columns 2, 4, and 6 further control for other HIT adoptions. Standard errors in parentheses are clustered by hospital

$$
^ {*} p <   0. 1; ^ {* *} p <   0. 0 5; ^ {* * *} p <   0. 0 1.
$$

Table 4. Mechanism Tests

<table><tr><td rowspan="2"></td><td colspan="2">AN</td><td colspan="2">PSM-AN</td><td colspan="2">AA</td><td colspan="2">U.S. sample (AN)</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td><td>(8)</td></tr><tr><td>ER telemedicine</td><td>-0.503***(0.193)</td><td>-0.448**(0.182)</td><td>-0.933*(0.549)</td><td>-1.057**(0.502)</td><td>-0.621***(0.188)</td><td>-0.514*(0.268)</td><td>-2.426**(1.171)</td><td>-1.980(1.314)</td></tr><tr><td>ER telemedicine × EROccupancy</td><td>-0.236***(0.078)</td><td></td><td>-0.473**(0.225)</td><td></td><td>-0.182*(0.106)</td><td></td><td></td><td></td></tr><tr><td>ER telemedicine × After-hours</td><td></td><td>-0.581***(0.154)</td><td></td><td>-0.442***(0.144)</td><td></td><td>-0.834**(0.297)</td><td></td><td></td></tr><tr><td>ER telemedicine × Utilization Rate</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-0.678*(0.361)</td></tr><tr><td>Effect at mean</td><td>-0.656***(0.194)</td><td></td><td>-1.185**(0.557)</td><td></td><td>-0.739***(0.210)</td><td></td><td></td><td>-2.341**(1.194)</td></tr><tr><td>Other HIT</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Patient and hospital control</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time and hospital fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Number of observations</td><td>17,573,681</td><td>17,573,681</td><td>2,848,135</td><td>2,848,135</td><td>2,099,780</td><td>2,099,780</td><td>8,181</td><td>8,181</td></tr><tr><td> $R^2$ </td><td>0.129</td><td>0.129</td><td>0.246</td><td>0.232</td><td>0.234</td><td>0.233</td><td>0.082</td><td>0.082</td></tr></table>

Notes. Columns 1–6 report the results on the flexible resource allocation mechanism using New York State SEDD individual patient data from 2010 to 2014, where the dependent variable is the patient’s length of stay (LOS) in hours. Columns 7–8 report the waiting time changes using the U.S. sample from 2012 to 2014, where the dependent variable is the average ER waiting time in minutes before patients were seen by a healthcare professional. EROccupancy captures the variation of occupancy level for a given ER across time, After-hours = 1 if an ER visit occurs between 8 p.m. and 8 a.m. Effect at mean is the average LOS (waiting time) reduction at the mean EROccupancy level (Utilization Rate) due to telemedicine adoption. AN, sample of newly adopters and nonadopters; PSM-AN, matched sample of newly adopters and nonadopters; AA, sample of newl adopters and always adopters. Standard errors in parentheses are clustered by hospital.

$$
^ {*} p <   0. 1; ^ {* *} p <   0. 0 5; ^ {* * *} p <   0. 0 1.
$$

remain robust when we use the lagged EROccupancy measure or different cutoffs in defining after-hour visits (see Table A5 in Online Appendix A).

6.2.2. Waiting-Time Reduction. To examine how patients’ waiting time changes due to telemedicine adoption, we refer to the waiting-time measure (OP-20) in the Hospital Compare database. Starting in 2012, the Centers for Medicare and Medicaid Services (CMS) reports, at hospital-year level, the average time (in minutes) that patients spent in the ER before they were seen by a healthcare professional. We conduct the following DID analysis using the hospitalyear panel including all the newly adopters and nonadopters in the United States from 2012 to 2014 (see the summary statistics of this panel in Table A4 of Online Appendix A):

$$
Y _ {j t} = \beta_ {0} + \beta_ {1} t e l e \_ e r _ {j t} + \delta Z _ {j t} + H o s F E _ {j} + T i m e F E _ {t} + \epsilon_ {j t}.\tag{3}
$$

The dependent variable $Y _ { j t }$ is the ER waiting-time measure OP-20, and the main variable of interest, $t e l e \_ e r _ { j t } ,$ , is the ER telemedicine adoption status for hospital j in year t. All control variables, denoted by $Z _ { j t } ,$ are time-varying hospital characteristics such as hospital size, annual ER patient volume, and the adoption status of other HIT applications.

Column 7 of Table 4 reports the regression result. We can see that ER telemedicine adoption significantly reduces waiting time by 2.426 minutes, corresponding to roughly an 8% reduction at the mean. We then test the heterogeneous effect by the average ER utilization level. Specifically, for hospital $j ,$ we construct its average utilization rate before telemedicine adoption as follows:

$$
\begin{array}{l} \text {UtilizationRate} _ {j} \\ = \frac {1}{N _ {j}} \sum_ {t = 1} ^ {N _ {j}} \frac {\text {Number of ER patients} _ {j , t}}{\text {Number of licensed beds} _ {j , t} \times 3 6 5} \end{array}
$$

where $N _ { j }$ stands for the number of observations for hospital j in AHA Annual survey between 2005 and 2011. A higher value of UtilizationRate implies a busier system before telemedicine adoption (McCarthy et al. 2008).<sup>17</sup> Column 8 in Table 4 reports the estimation result. We find a negative, albeit statistically insignificant, coefficient of telemedicine adoption but a significant and negative coefficient estimate for the interaction term. The results suggest that telemedicine is especially helpful to hospitals that were plagued by a congestion problem.<sup>18</sup>

## 7. Robustness Check

To further alleviate the endogeneity concern and to evaluate the validity of our main empirical findings, we perform a pretrend analysis, and conduct several falsification tests to address hospital-wide and ERspecific endogeneity concerns.

## 7.1. Pretrend Analysis

Following the literature (Adjerid et al. 2018), we test whether there is any differential pretrend in LOS between newly adopters and nonadopters. We extend our sample from 2007 to 2014 and generate a set of lead and lag indicators for each newly adopter.<sup>19</sup> Specifically, we create four indicators $( t e l e \_ e r _ { t - 1 } \sim$ $t e l e \_ e r _ { t - 4 \ b a c k w a r d } )$ that are equal to 1 only in the corresponding year(s), as well as an indicator for the first year of adoption and forward $( t e l e \_ e r _ { t = 0 } \_ f o r w a r d )$ We choose lags up to t  4 and one lead indicator because all adopters have these indicators available. We use four years before adoption as the baseline (i.e., omitted variable), which corresponds to the variable tele $e r _ { t - 4 } \ b a c k w a r d \cdot$ . We find no evidence of pretrend difference that might have driven our findings, as the coefficient estimates for all indicators before adopting telemedicine are small and insignificant, whereas newly adopters pick up the effect since the adoption year (see Figure 1).

## 7.2. Falsi<sup>fi</sup>cation Test: Hospital-Wide Endogeneity Concern

If the identified LOS reduction is primarily due to some unobserved hospital-wide efficiency-improvement initiative that was launched at the same time as ER telemedicine, then, by replacing the dependent variable with some non-ER efficiency measure, our econometric model should falsely detect efficiency improvement after ER telemedicine adoption.<sup>20</sup> To implement this idea, we obtain the HCUP/SID data for New York State, which include inpatient records from 2010 to 2014. We use the inpatient LOS as the dependent variable to estimate the baseline regression model (1) in Section 5.1, where the inpatient LOS is calculated from the time when a patient was admitted to the hospital as an inpatient to the time when he or she was discharged. Columns 1–3 of Table 5 report the estimation results. We find no evidence that the observed ER efficiency gain is driven by unobserved efficiency improvement at the hospital level, as can be seen from the insignificant coefficient estimate of tele er.

Similar to the previous falsification test, but implemented differently, we consider whether non-ER telemedicine adoption has a causal effect on ER care delivery. If there is a significant effect, we may then suspect that our main findings reflect a broader implication of telemedicine. To implement this idea, we first construct tele other <sub></sub> 1 if a hospital has adopted telemedicine in some department (not in ER) and 0 otherwise. We then subset the sample of hospitals without ER telemedicine adoption by 2014 and compare adopters (tele other <sub></sub> 1, tele er <sub></sub> 0) with nonadopters (tele other <sub></sub> 0, tele er <sub></sub> 0) (in terms of telemedicine in other departments). We find that the coefficient estimate (Table 5, column 4) for tele other is small and insignificant, which suggests that the identified ER efficiency improvement does not come from non-ER telemedicine adoption.

## 7.3. Falsi<sup>fi</sup>cation Test: ER-Speci<sup>fi</sup>c Endogeneity Concern

Although the above analyses can greatly alleviate the concerns on hospital-wide initiatives, one might worry about ER-specific confounding factors that could bias the estimation. If there were any endogenous factors, then we would expect a shorter LOS in a placebo sample of ER patients who are unlikely to be affected by telemedicine or changes in presumably unaffected ER process measures. To implement the idea, we conduct two falsification tests.

First, we choose ER patients with acute myocardial infarction (AMI) as the placebo sample due to several considerations. Firstly, AMI patients usually require immediate treatment and surgical operations such as coronary artery bypass graft. Due to technological limitations, they are unlikely to receive treatment via telemedicine. Secondly, AMI patients are typically placed with the highest priority (Lu and Lu 2018). Therefore, even if they receive the telemedicine service, their LOS is unlikely to be much affected, because they do not have to wait with or without telemedicine. However, immediate treatment for AMI patients reflects the overall ER care delivery efficiency, which makes it a feasible sample to detect any unobserved ER confounding factors that might have led to our observed efficiency gain. We find no evidence of ERspecific unobserved process changes that drive our findings, as we observe an insignificant effect for AMI patients in columns 5–6 of Table 5.

Figure 1. (Color online) Pretrend Analysis Using New York State Data from 2007 to 2014  
![](/api/attachments/REEW3KC3/fulltext/images/e219fb1dfd0cf27fab5887daacc519791591ca37f80b09d318336226e0d6d75a.jpg)  
Notes. This figure plots the coefficient estimates for the lead and lag indicators in the pretrend analysis. Error bars show 95% confidence intervals We use four years before adoption and backward (tele $e r _ { t - 4 ~ b a c k w a r d } )$ as the baseline.

Table 5. Falsification Tests on Hospital-Wide and ER-Specific Endogeneity

<table><tr><td rowspan="5"></td><td colspan="4">Hospital-level endogeneity</td><td colspan="4">ER-specific endogeneity</td></tr><tr><td colspan="4">New York State sample</td><td colspan="2">New York State sample</td><td colspan="2">U.S. sample</td></tr><tr><td colspan="3">Inpatient LOS</td><td>ER LOS</td><td colspan="2">ER LOS</td><td colspan="2">Time to ECG</td></tr><tr><td>AN</td><td>PSM AN</td><td>AA</td><td>AN+</td><td>AN</td><td>AA</td><td>AN</td><td>AA</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td><td>(8)</td></tr><tr><td>ER telemedicine (tele_er)</td><td>0.787(2.228)</td><td>0.950(2.737)</td><td>2.546(2.456)</td><td></td><td>-0.640***(0.201)</td><td>-0.695***(0.212)</td><td>0.269(0.312)</td><td>0.0295(0.316)</td></tr><tr><td>non-ER Telemedicine (tele_other)</td><td></td><td></td><td></td><td>0.146(0.233)</td><td></td><td></td><td></td><td></td></tr><tr><td>AMI</td><td></td><td></td><td></td><td></td><td>-2.313***(0.359)</td><td>-4.536***(0.773)</td><td></td><td></td></tr><tr><td>ER telemedicine × AMI</td><td></td><td></td><td></td><td></td><td>1.476(1.363)</td><td>0.974(1.001)</td><td></td><td></td></tr><tr><td>F-test: Effect for AMI patients</td><td></td><td></td><td></td><td></td><td>0.836(1.337)</td><td>0.278(1.045)</td><td></td><td></td></tr><tr><td>Other HIT</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Patient and hospital control</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time and hospital fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Number of observations</td><td>8,199,267</td><td>1,309,954</td><td>645,254</td><td>15,091,203</td><td>17,573,681</td><td>2,099,780</td><td>10,088</td><td>1,298</td></tr><tr><td> $R^2$ </td><td>0.176</td><td>0.186</td><td>0.178</td><td>0.118</td><td>0.129</td><td>0.234</td><td>0.005</td><td>0.037</td></tr></table>

Notes. Columns 1–3 test the effect of ER telemedicine adoption on inpatient LOS using HCUP SID patient data from 2010 to 2014. Column 4 test the effect of non-ER telemedicine adoption on ER patients’ LOS using New York State SEDD patient data from 2010 to 2014. Columns 5–6 report the effect of ER telemedicine on ER LOS for patients with/without AMI using the New York State SEDD patient data from 2010 to 2014 Columns 7–8 report the effect of ER telemedicine adoption on patients’ time to receive ECG (i.e., CMS OP-5 measure) using the U.S. sample from 2010 to 2014. AN, sample of newly adopters and nonadopters; PSM-AN, matched sample of newly adopters and nonadopters; AA sample of newly adopters and always adopters; AN+, sample of newly adopters and nonadopters in terms of non-ER telemedicine adoption (i.e., tele other). Standard errors in parentheses are clustered by hospital  
\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

Second, we choose the CMS key quality metric OP-5 as the placebo ER outcome measure, which records the average number of minutes before outpatients with chest pain or possible heart attack got an electrocardiogram (ECG). OP-5 serves as a valid placebo measure for two reasons: Firstly, ER registration and triage staff use pre-established screening criteria to identify patients that should receive an early ECG before physician evaluation (Yiadom et al. 2017). Therefore, no telemedicine service can be applied during this process. Secondly, a timely ECG test requires a fast screening and smooth workflow, which reflects the overall care efficiency and quality in the ER. Therefore, we should falsely detect the changes in OP-5 if our main finding is driven by some ER-specific initiative that we fail to capture in the regression. Again, we find no evidence of ER-specific unobserved process changes, as can be seen from the insignificant coefficient estimate for telemedicine adoption in columns 7–8 of Table 5.

## 7.4. Alternative Explanation: Potential Changes in Patient Flow

One may worry that telemedicine applications can redirect patient flow by affecting patients’ choices of ER and thus lead to LOS reduction. To examine this possibility, we check the changes in ER volume and the patients’ Charlson Comorbidity Index (CCI) (Charlson et al. 1987, Stagg 2017) due to telemedicine adoption. Table 6 reports the results using the DID specification on the aggregated individual patients’ data of New York State. We find no evidence of significant changes in both measures, as can be seen from the insignificant coefficient estimates for ER telemedicine throughout the samples. The results are in fact not surprising, because, at the operational level, the availability of ER telemedicine is unlikely to reduce the number of patients visiting the ER. In the ER telemedicine model, patients in emergencies have to first come to the ERs and then possibly receive the telemedicine service. The workflow is different from the telemedicine application, where patients remotely communicate with medical providers and then decide whether to visit the hospital (Yeow and Huat Goh 2015, Gillespie et al. 2016).

Table 6. Changes in ER Volume and Patient Severity Profile

<table><tr><td rowspan="3"></td><td colspan="4">AN</td><td colspan="4">PSM-AN</td><td colspan="4">AA</td></tr><tr><td rowspan="2">ER volume(1)</td><td colspan="3">CCI</td><td rowspan="2">ER volume(5)</td><td colspan="3">CCI</td><td rowspan="2">ER volume(9)</td><td colspan="3">CCI</td></tr><tr><td>Mean(2)</td><td>SD(3)</td><td>Range(4)</td><td>Mean(6)</td><td>SD(7)</td><td>Range(8)</td><td>Mean(10)</td><td>SD(11)</td><td>Range(12)</td></tr><tr><td>ER telemedicine</td><td>1,283.85(1,623.926)</td><td>0.015(0.022)</td><td>0.012(0.030)</td><td>-0.333(0.311)</td><td>2,076.356(2,221.398)</td><td>0.016(0.024)</td><td>0.013(0.033)</td><td>-0.259(0.403)</td><td>857.812(1,555.754)</td><td>0.026(0.020)</td><td>0.017(0.029)</td><td>-0.396(0.379)</td></tr><tr><td>Year and hospital fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Number of observations</td><td>847</td><td>847</td><td>847</td><td>847</td><td>160</td><td>160</td><td>160</td><td>160</td><td>114</td><td>114</td><td>114</td><td>114</td></tr><tr><td> $R^2$ </td><td>0.103</td><td>0.035</td><td>0.064</td><td>0.048</td><td>0.073</td><td>0.379</td><td>0.386</td><td>0.112</td><td>0.149</td><td>0.217</td><td>0.259</td><td>0.041</td></tr></table>

Notes. This table reports the DID estimates on the changes in ER volume and the distribution of patients’ CCI using aggregated New York State SEDD data from 2010 to 2014. In particular, we calculated the mean, standard deviation (SD), and range of patients’ severity level by hospital and year, so as to examine the changes in the central tendency and dispersion of patients’ CCI distribution. AN, sample of newly adopters and nonadopters; PSM-AN, matched sample of newly adopters and nonadopters; AA, sample of newly adopters and always adopters. Standard errors in parentheses are clustered by hospital.

## 8. Conclusion

Using a unique data set constructed from multiple sources, we evaluated the potential of telemedicine in improving ER care delivery. Robust empirical results suggest that the telemedicine application in ERs can significantly reduce the average patient length of stay. Such effect is larger when the ER occupancy level is higher or when patients visit ERs during afterhours. Furthermore, we find that the LOS reduction is partially driven by the reduction of waiting time. Additional evidence shows that the efficiency gained from telemedicine does not come at the expense of lower care quality or higher medical expenditure.<sup>21</sup>

This paper contributes to both the literature and practice on HIT. By bridging the literature on telemedicine and the literature on ER overcrowding, our study offers solid evidence on the promise of telemedicine application in ER, which is not readily available from the existing literature. Our findings also open a new channel on how HIT contributes to healthcare delivery. While previous studies suggest that HIE can increase ER efficiency through more efficient information coordination (Ayer et al. 2019), our paper shows that telemedicine achieves greater efficiencies through potentially several channels. In addition to more efficient information exchange, telemedicine can greatly improve care delivery through flexible resource allocation, especially in the presence of demand and supply fluctuations. We believe that such findings are critical for ERs, due to the special setting of unscheduled arrivals leading to high unpredictability of patient traffic.

For healthcare decision makers, our findings also have important implications. Due to the lack of evidence and the inflexibility of reimbursement policies, the adoption rate of ER telemedicine remains low and grows slowly. Our research provides ground for policy makers to incentivize hospitals to adopt telemedicine in ERs. In 2009, the Health Information Tech nology for Economic and Clinical Health Act (HITECH) was signed into law to promote the adoption and meaningful use of HIT. The policy provides financial incentives for digitizing records, which significantly facilitates the adoption of EMR and HIE (Agarwal et al. 2010, Yaraghi et al. 2014, Atasoy et al. 2017). We believe that it is time for policy makers to incentivize ER telemedicine adoption as well. The recent introduction of Healthcare Common Procedure Coding System (HCPCS) Code G2010 by the CMS to cover “remote evaluation of pre-recorded patient information” is a good example, but more coverages are needed.<sup>22</sup>

Previous literature (Miscione 2007, Singh et al. 2015, Srivastava and Shainesh 2015) points out the role of telemedicine in reducing the service divide between urban and rural areas through the “hub and spoke” architecture, where smaller “spoke” hospitals connect larger “hub” hospitals for consultation. Our paper highlights the general applicability of such a two-layer architecture for ER patients. Besides increasing patients’ access to more immediate care from specialists that were not available otherwise, telemedicine can help address demand shocks and supply shortages for any hospital. With the continued advancement of information technology, such as augmented reality and wearable devices, telemedicine can be the key to increase healthcare access and improve the healthcare delivery efficiency, no matter where hospitals are located.

Like any empirical study, this paper has limitations with respect to its internal validity and external validity. First, despite our best efforts, endogeneity due to unobserved time-varying confounders cannot be completely eliminated. Given the difficulty of running a randomized experiment among ERs, we believe that more observational studies using different data should be conducted to further reduce type-I errors. Second, although the adoption rate in New York State is above the national average, it is still low, which raises the question concerning the generalizability of our findings. The U.S. sample analysis alleviates the concern to some extent, but future research should address this issue, once the ER telemedicine adoption rate picks up in some regions. Third, the HCUP/SEDD data do not include ER patients who were later admitted as inpatients, which is a common issue for studies using HCUP/ SEDD data and could have implications on the external validity of our findings. Although the proportion of those patients is not high, it is worthwhile for future studies to quantify the impact of excluding such patients when such data become available. Finally, due to the lack of individual telemedicine usage information, we did not test the heterogeneous effects of telemedicine by patient type. We believe this is an important future research direction that can further shed light on the mechanisms for ER telemedicine to improve care delivery.

## Acknowledgments

The authors sincerely thank the senior editor, the associate editor, and the reviewers for their many helpful suggestions, which greatly contributed to this research. The authors also greatly appreciate Michael F. Rotondo, Justin A. Mazzillo, David Lee Waldman, Earl Ray Dorsey, Keith Evers Grams, Brenda Bartock, and Marita Michelin for sharing their practical insights on telemedicine applications.

## Endnotes

<sup>1</sup> See http://www.americantelemed.org/main/about/about-telemedicine/ telemedicine-faqs.

<sup>2</sup> See https://www.wsj.com/articles/can-tech-speed-up-emergency -room-care-1490629118.

<sup>3</sup> See https://www.healthleadersmedia.com/clinical-care/ed-tries -telemedicine-bid-cut-wait-times

<sup>4</sup> See https://www.cms.gov/Regulations-and-Guidance/Legislation/ EMTALA/index.html.

<sup>5</sup> See http://www.ncsl.org/research/health/con-certificate-of-need -state-laws.aspx.

<sup>6</sup> These are based on many interviews that we conducted with physicians from hospitals in New York State.

<sup>7</sup> For example, the Centers for Medicare and Medicaid Services recently introduced Healthcare Common Procedure Coding System (HCPCS) Code G2010 (https://www.federalregister.gov/documents/2018/11/ 23/2018-24170/medicare-program-revisions-to-payment-policies-under

-the-physician-fee-schedule-and-other-revisions), which, starting from 2019, covers “remote evaluation of pre-recorded patient information.”

<sup>8</sup> According to Ward et al. (2015), the median number of patients/ consultations from previous studies of tele-emergency applications is 60.

<sup>9</sup> See https://evisit.com/resources/what-is-teleradiology/.

<sup>10</sup> See https://telestroke.massgeneral.org/telestroke.aspx.

According to the HCUP data, 18% of ER patients were admitted to the hospital as inpatients from 2010 to 2014. In other words, the HCUP/SEDD data capture 82% of the ER visits. So, we believe that excluding those admitted ER patients would not severely hurt the generalizability of studies based on the HCUP/SEDD data.

<sup>12</sup> We control for EMR and EDIS throughout our analyses. All the results remain qualitatively the same when we control for HIE, and results are available upon request. We did not report this set of results in the paper because the HIE variable is missing in the HIMSS 2011 data, thus causing a reduction of 20% observations.

<sup>13</sup> Our main sample covers from 2010 to 2014. We use the average hospital-level characteristics from 2007 to 2009 in the probit analysis. Please see Table A1 in Online Appendix A for more details on the probit analysis.

<sup>14</sup> Note that tele er<sub>j,t </sub> tele er<sub>j ×</sub> post<sub>t</sub>, where tele $\mathcal { e } r _ { j }$ is a dummy variable that equals 1 if hospital j had adopted ER telemedicine during our sample period and 0 otherwise, and post<sub>t</sub> equals 1 for postadoption periods. tele $\mathcal { \boldsymbol { e r } } _ { j }$ is absorbed in the hospital fixed effects, and post is absorbed in the time fixed effects

<sup>15</sup> Since the time window ranges from 2010 to 2014 in our original sample, we choose the average hospital-level characteristics from 2007 to 2009 as the matching variables, which are unlikely to be affected by the adoption decision.

<sup>16</sup> The result of propensity score matching is not sensitive to the number of nearest neighbors. Results corresponding to differen parameter setups are available upon request.

<sup>17</sup> First, because the U.S. sample analysis includes hospital data from 2012 to 2014, UtilizationRate is not affected by telemedicine adoption. The results remain qualitatively the same when we vary the time window (e.g., 2005–2009, 2005–2010, 2005–2011) in calculating UtilizationRate . Second, UtilizationRate captures the mean utilization rate for an ER before telemedicine adoption, which differs from the occupancy measure EROccupancy that captures the occupancy variation across time within an ER.

<sup>18</sup> See Online Appendix C for the instrumental variable analysis on the U.S. sample.

<sup>19</sup> HIMSS does not report the telemedicine adoption status before 2010. Therefore, we exclude always adopters in the pretrend analysis because we do not know their exact year of adoption.

<sup>20</sup> We implicitly assume in the falsification test that ER telemedicine adoption does not impact inpatient stays, because hospital-wide care quality rather than ER telemedicine adoption shall be the first-order determinant in inpatient LOS. However, there could be downstream impacts such as more efficient inpatient boarding and, accordingly, shorter inpatient LOS. If such a channel exists, then it will be less likely for us to observe an insignificant effect in the falsification test, assuming that both ER telemedicine and unobserved hospital ini tiatives can improve inpatient care. We thank an anonymous reviewer for raising this point.

## References

Adjerid I, Adler-Milstein J, Angst C (2018) Reducing Medicare spending through electronic health information exchange: the role of incentives and exchange maturity. Inform. Systems Res. 29(2):341–361.

Agarwal R, Gao G, DesRoches C, Jha AK (2010) Research commentary—the digital transformation of healthcare: Current status and the road ahead. Inform. Systems Res. 21(4):796–809.

Anderson D, Gao G, Golden B (2014) Life is all about timing: An examination of differences in treatment quality for trauma patients based on hospital arrival time. Production Oper. Manage ment 23(12):2178–2190.

Angrist JD, Pischke JS (2008) Mostly Harmless Econometrics: An Em piricist’s Companion (Princeton University Press, Princeton, NJ)

Atasoy H, Chen P-Y, Ganju K (2017) The spillover effects of health IT investments on regional healthcare costs. Management Sci. 64(6): 2515–2534.

Ayabakan S, Bardhan IR, Zheng ZE, Kirksey K (2017) The impact of health information sharing on duplicate testing. MIS Quart. 41(4):1083–1103.

Ayer T, Ayvaci MU, Karaca Z, Vlachy J (2019) The impact of health information exchanges on emergency department length of stay. Production Oper. Management 28(3):740–758.

Bapna R, Ramaprasad J, Umyarov A (2018) Monetizing freemium communities: Does paying for premium increase social en gagement? MIS Quart. 42(3):719–735.

Bardhan I, Jh Oh, Zheng Z, Kirksey K (2014) Predictive analytics fo readmission of patients with congestive heart failure. Inform. Systems Res. 26(1):19–39.

Bashshur R, Shannon G, Krupinski E, Grigsby J (2011) The taxonomy of telemedicine. Telemedicine e-Health 17(6):484–494.

Berry Jaeker JA, Tucker AL (2017) Past the point of speeding up: The negative effects of workload saturation on efficiency and patient severity. Management Sci. 63(4):1042–1062.

Boyle A, Beniuk K, Higginson I, Atkinson P (2012) Emergency department crowding: Time for interventions and policy evaluations. Emergency Medicine Internat. 2012:838610.

Brot-Goldberg ZC, Chandra A, Handel BR, Kolstad JT (2017) What does a deductible do? The impact of cost-sharing on healthcare prices, quantities, and spending dynamics. Quart. J. Econom. 132(3):1261–1318.

Chang AM, Cohen DJ, Lin A, Augustine J, Handel DA, Howell E, Kim H, Pines JM, Schuur JD, McConnell KJ, et al. (2018) Hospital strategies for reducing emergency department crowding: A mixed-methods study. Ann. Emergency Medicine 71(4):497–505.

Charlson ME, Pompei P, Ales KL, MacKenzie CR (1987) A new method of classifying prognostic comorbidity in longitudinal studies: development and validation. J. Chronic Diseases 40(5):373–383.

Considine J, Kropman M, Kelly E, Winter C (2008) Effect of emergency department fast track on emergency department length of stay: A case-control study. Emergency Medicine J. 25(12):815–819.

Freeman M, Robinson S, Scholtes S (2020) Gatekeeping under congestion: An empirical study of referral errors in the emergency department. Working Paper No. 2020/09/TOM, INSEAD, Singapore.

Gillespie SM, Shah MN, Wasserman EB, Wood NE, Wang H, Noyes K, Nelson D, Dozier A, McConnochie KM (2016) Reducing emergency department utilization through engagement in telemedicine by senior living communities. Telemedicine e-Health 22(6):489–496.

Hoot NR, Aronsky D (2008) Systematic review of emergency department crowding: causes, effects, and solutions. Ann. Emergency Medicine 52(2):126–136.

Imperato J, Morris DS, Binder D, Fischer C, Patrick J, Sanchez LD, Setnik G (2012) Physician in triage improves emergency depart ment patient throughput. Internal Emergency Medcine 7(5):457–462.

Janakiraman R, Park E, Demirezen E, Kumar S (2017) The effects of health information exchange access on healthcare quality and efficiency: An empirical investigation. Research Paper No. 2915190, Mays Business School, Texas A&M University, College Station, TX.

Kuntz L, Mennicken R, Scholtes S (2015) Stress on the ward: Evidence of safety tipping points in hospitals. Management Sci. 61(4): 754–771.

Lu LX, Lu SF (2018) Distance, quality, or relationship? Interhospital transfer of heart attack patients. Production Oper. Management 27(12):2251–2269.

Lu SF, Rui H (2018) Can we trust online physician ratings? Evidence from cardiac surgeons in Florida. Management Sci. 64(6): 2557–2573.

McCarthy ML, Aronsky D, Jones ID, Miner JR, Band RA, Baren JM, Desmond JS, Baumlin KM, Ding R, Shesser R (2008) The emergency department occupancy rate: A simple measure of emergency department crowding? Ann. Emergency Medicin 51(1):15–24.

McConnell KJ, Newgard CD, Lee R (2008) Changes in the cost and management of emergency department on-call coverage: Evidence from a longitudinal statewide survey. Ann. Emergency Medicine 52(6):635–642.

Miller EA (2003) The technical and interpersonal aspects of telemed icine: effects on doctor–patient communication. J. Telemedicin Telecare 9(1):1–7.

Miscione G (2007) Telemedicine in the upper amazon: Interplay with local healthcare practices. MIS Quart. 31(2):403–425.

Mohr NM, Vakkalanka JP, Harland KK, Bell A, Skow B, Shane DM, Ward MM (2018) Telemedicine use decreases rural emergency department length of stay for transferred North Dakota trauma patients. Telemedicine e-Health 24(3):194–202

Naylor MD, Kurtzman ET (2010) The role of nurse practitioners in reinventing primary care. Health Affairs 29(5):893–899.

O’Malley AS (2012) After-hours access to primary care practices linked with lower emergency department use and less unmet medical need. Health Affairs 32(1):175–183.

Pitts SR, Carrier ER, Rich EC, Kellermann AL (2010) Where Americans get acute care: Increasingly, it’s not at their doctor’s office. Health Affairs 29(9):1620–1629.

Rajan B, Seidmann A, Dorsey ER (2013) The competitive business impact of using telemedicine for the treatment of patients with chronic conditions. J. Management Inform. Systems 30(2):127–158.

Rajan B, Tezcan T, Seidmann A (2019) Service systems with het erogeneous customers: Investigating the effect of telemedicine on chronic care. Management Sci. 65(3):1236–1267.

Rao MB, Lerro C, Gross CP (2010) The shortage of on-call surgical specialist coverage: A national survey of emergency department directors. Academic Emergency Medicine 17(12):1374–1382.

Rosenbaum PR, Rubin DB (1983) The central role of the propensity score in observational studies for causal effects. Biometrika 70(1):41–55.

Serrano CI, Karahanna E (2016) The compensatory interaction between user capabilities and technology capabilities in influencing task performance: An empirical assessment in telemedicine consultations. MIS Quart. 40(3):597–621.

Singh R, Mathiassen L, Mishra A (2015) Organizational path con stitution in technological innovation: Evidence from rural tele health. MIS Quart. 39(3):653–665.

Sinreich D, Jabali O, Dellaert NP (2012) Reducing emergency de partment waiting times by adjusting work shifts considering patient visits to multiple care providers. IIE Trans. 44(3):163–180.

Song H, Tucker AL, Murrell KL (2015) The diseconomies of queue pooling: An empirical investigation of emergency department length of stay. Management Sci. 61(12):3032–3053.

Southard EP, Neufeld JD, Laws S (2014) Telemental health evaluations enhance access and efficiency in a critical access hospital emergency department. Telemedicine e-Health 20(7):664–668.

Srivastava SC, Shainesh G (2015) Bridging the service divide through digitally enabled service innovations; evidence from Indian healthcare service providers. MIS Quart. 39(1):245–267.

Stagg V (2017) CHARLSON: Stata module to calculate Charlson index of comorbidity. Statistical Software Components S456719, Department of Economics, Boston College, Chestnut Hill, MA.

Stuart EA (2010) Matching methods for causal inference: A review and a look forward. Statistical Sci. 25(1):1–21.

Trzeciak S, Rivers E (2003) Emergency department overcrowding in the United States: An emerging threat to patient safety and public health. Emergency Medicine J. 20(5):402–405.

Ward MM, Jaana M, Natafgi N (2015) Systematic review of telemedicine applications in emergency rooms. Internat. J. Medical Inform. 84(9):601–616.

Wiler JL, Ginde AA (2015) State laws governing physician assistant practice in the United States and the impact on emergency medicine. J. Emergency Medicine 48(2):e49–e58.

Yaraghi N, Du AY, Sharman R, Gopal RD, Ramesh R (2014) Health information exchange as a multisided platform: Adoption, usage, and practice involvement in service co-production. Inform. Systems Res. 26(1):1–18.

Yeow A, Huat Goh K (2015) Work harder or work smarter? Information technology and resource allocation in healthcare pro cesses. MIS Quart. 39(4):763–785.

Yiadom MYAB, Baugh CW, McWade CM, Liu X, Song KJ, Patterson BW, Jenkins CA, Tanski M, Mills AM, Salazar G, et al. (2017) Performance of emergency department screening criteria for an early ECG to identify STt-segment elevation myocardial infarction. J. Amer. Heart Assoc. 6(3):e003528.
