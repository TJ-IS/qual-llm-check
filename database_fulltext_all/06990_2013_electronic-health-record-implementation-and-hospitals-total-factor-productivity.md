---
otero_id: 6990
otero_key: "P9UAPNBG"
title: "Electronic health record implementation and hospitals' total factor productivity"
authors: "Timothy R. Huerta; Mark A. Thompson; Eric W. Ford; William F. Ford"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.10.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Electronic health record implementation and hospitals' total factor productivity

Timothy R. Huerta <sup>a</sup>, Mark A. Thompson <sup>a,</sup>⁎, Eric W. Ford <sup>b</sup>, William F. Ford <sup>c</sup>

<sup>a</sup> Texas Tech University, United States

<sup>b</sup> University of North Carolina Greensboro, United States

<sup>c</sup> Middle Tennessee State University, United States

## a r t i c l e i n f o

Available online 6 October 2012

Keywords: EHR HIT implementation Data envelopment analysis Hospitals Meaningful use

## a b s t r a c t

The adoption and implementation of electronic health record (EHR) systems have been widely promoted as a means for improving health care delivery and controlling costs in U.S. hospitals. To date, the results of efforts to adopt such systems have been mixed and often unsuccessful. This paper uses frontier analysis to measure hospitals' Total Factor Productivity (TFP) during 2006–2008 and compare it to nine different stages of EHR implementation. Overall, we <sup>fi</sup>nd that hospitals implementing EHR systems have lower TFP gains relative to those facilities that have as yet to adopt. In particular, hospitals that attempt to fully implement an EHR in one year, the ‘Big Bang’ strategy, have relatively low TFP levels. Therefore, the anticipated savings from increased EHR use may not be realized in the near-term for EHR system adopters. Moreover, an evidence-based approach to developing the ‘Meaningful Use’ incentive and reward program for EHR implementation is warranted.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

The U.S. healthcare system is far more costly to operate on a per capita basis than that of any other industrialized nation, many of which achieve comparable or superior clinical outcomes. One of the primary explanations offered for this excessive cost difference is the poor care coordination within U.S. hospitals. For example, both the duplication of diagnostic tests [32] and ordering unnecessary tests [37] could be avoided with better health information management. Further, as much as 20%, and perhaps more, of hospitals' lab orders are either unnecessary duplications or inappropriate requests that could be avoided [22,32]. In 2008, Peter Orszag, the Director of the Congressional Budget Of<sup>fi</sup>ce, estimated that <sup>fi</sup>ve percent of the nation's GDP, about \$700 billion dollars per year, goes towards tests and procedures that do not improve health outcomes [30]. When one considers that the total cost of health care in the U.S. is estimated at 17%, this assessment implies that 30% of all healthcare expenses do not improve health outcomes. The difference in these numbers suggests an assessment on the costs associated with potential savings related to the ‘Meaningful Use’ of health information, such as avoiding medical errors, and the magnitude of the avoidable costs becomes much larger.

With the potential to create healthcare cost savings in the billions, electronic health records (EHRs) are considered a critical component of reform efforts [14]. Yet, despite the potential savings, EHR adoption is not widespread in U.S. hospitals [29]. Moreover, in most facilities where EHR systems have been adopted, the implementation is often incomplete. The slow uptake of EHRs has been attributed to the systems' high costs, the signi<sup>fi</sup>cant change to a hospital's work processes that are required for the implementation and the major culture shift it represents for health professionals. Such factors can disrupt an EHR implementing facility's productivity in the short term. However, in the long run it is still assumed that EHRs will produce productivity gains for both individual hospitals and the health sector as a whole. To address these short-term costs, the Of<sup>fi</sup>ce of the National Coordinator for Health Information Technology introduced an EHR ‘Meaningful Use’ program in 2009 to reward and incentivize the systems' adoption and implementation in hospitals by 2014 [13]. As a result, EHR adoption strategies have been the subject of much discussion in the literature. One such taxonomy used by Jha, et al. [29] has sought to explore the state of the moment in terms of EHR adoption.

The purpose of this study is to measure EHR implementation's impacts on hospitals' ef<sup>fi</sup>ciency change, technological process change and total factor productivity in the short term. The study uses a three-step process to assess hospitals' EHR implementation strategies in the early part of the Meaningful Use era. First, the taxonomy described by Jha et al. [29] is extended into a longitudinal form to classify hospitals' progress towards full EHR implementation over time. Next, frontier analysis is used to measure U.S. hospitals' productivity gains from 2006 through 2008 (3 years). In particular, the Malmquist Total Factor Productivity (TFP) index and its underlying indices, Technical Ef-<sup>fi</sup>ciency Change (EFFCH) and Technological Change (TC) are calculated. Finally, the longitudinal EHR implementation stages taxonomy is analyzed in relationship to the productivity change measures. The results and a discussion of their implications are presented last.

This research makes important contributions to the health policy, administration, and research literatures. With the large-scale investments made by the Federal Government to promote the Meaningful

Use of health information technologies (HITs), there is a need to understand the implications of accelerating hospitals' EHR implementation on productivity [3,5], especially since meaningful use is a longitudinal reward system. While bene<sup>fi</sup>ts may be gained from more extensive EHR use in the long term, the short-term EHR implementation impacts on facilities' EFFCH and TC can be signi<sup>fi</sup>cant relative to non-adopting facilities. For managers, healthcare executives and their boards of directors, empirically demonstrating the link between a sustained and incremental commitment to EHR use and its long-term positive relationship with productivity is an important aspect of promoting behavioral change in professional workforces who are often resistant to external pressures.

For researchers, the extension of the hospital EHR implementation taxonomy to a longitudinal measure increases its utility. In particular, the Meaningful Use reward and incentive program has multiple stages that are linked to varying levels of EHR use. Therefore, having an EHR implementation taxonomy that aligns with the Meaningful Use program's staged approach brings the outcomes experienced by hospitals into alignment with the rewards potentially garnered. A second important contribution is the use of frontier analysis to explicitly link a public policy initiative to the performance of the targeted organizations [26]. Assessing the impact of major programs, such as the Meaningful Use initiative, is dif<sup>fi</sup>cult because there are varied outcomes — both intended and unintended. While this is not the <sup>fi</sup>rst study employing productivity analysis in health care, it adds to the body of knowledge about how to assess various EHR implementation protocols, over time, in different organizational settings.

## 2. Literature and policy reviews

EHR systems were <sup>fi</sup>rst introduced in 1969 and have been evolving ever since [21]. In 2007 and 2008, The American Hospital Association (AHA) measured four major classes of EHR sub-systems that were anticipated to be part of the Meaningful Use program. The most frequently discussed of these classes is Computerized Provider Order Entry (CPOE), which includes electronic prescribing (ePrescribing or eRx) because of the signi<sup>fi</sup>cant role medication errors play in compromising care quality [49]. The second major EHR application is ‘Decision Support’, which is designed to facilitate adherence to clinical guidelines and the avoidance of errors, such as drug–drug interactions, by providing real-time feedback to EHR users. The use of those systems has been slow to take hold because it is dif<sup>fi</sup>cult to get large groups of physicians to agree on standardized regimens of care [45].

The third major class of EHR application is ‘Results Management’. Such systems are the most widely adopted EHR application because physicians and nurses value the timeliness of electronic results management compared to paper-based systems [7]. Further, results management systems require very little organizational change to implement because most of the work is con<sup>fi</sup>ned to a few specialized units that already rely on other HITs to conduct their work. Front-line employees are, by-and-large, passive information consumers as it relates to results management.

The last major class of EHR applications is related to ‘Patient Health Information’. Electronic patient health information involves collecting demographic measures, important health history events (e.g., prior surgeries), immunizations records, drug allergies and other data in a structured format. Having patient health information in a structured database is critical to the function of an effective decision support application. For example, knowing a patient's allergies provides critical information about potential adverse reactions to many classes of drugs. In order for patient health information to be effectively managed, HIT systems from physicians' of<sup>fi</sup>ces, health insurance companies, hospitals and other healthcare organizations must all share data. A complete, patient-centered record therefore requires robust interoperability in an EHR system, beyond individual clinical applications.

Ensuring effective EHR interoperability with other HIT applications is a signi<sup>fi</sup>cant challenge [34]. With a growing number of reports of costly EHR implementation failures [23], there is a reticence to adopt and implement EHR systems that may engender yet another failure or negatively impact productivity in either the short or long term. The ability to integrate EHR data into existing HITs, such as legacy billing systems that were not originally built to handle laboratory data, can slow adoption. The inherently networked nature of HIT systems makes their coordinated adoption more complicated than stand alone technologies and thus slowed their widespread adoption [15]. As a result, the full implementation of a high performing EHR system therefore requires extensive work<sup>fl</sup>ow redesigns across the entire organization. The high start-up costs for HIT adoption and resistance to change that accompanies their implementation lead many administrators to take a wait-and-see approach rather than joining the ‘bleeding edge’ of the earlier adopters. The potential negative impacts that implementing EHR solutions can have on their organizations' productivity was seen as such a signi<sup>fi</sup>cant issue that the AHA successfully petitioned the Of-<sup>fi</sup>ce of the National Coordinator for Health Information Technology to delay pressing for early ‘Meaningful Use’ of some EHR applications requirements being promulgated as part of the Patient Protection and Affordable Care Act [44].

This is not to say that the challenge of change is insurmountable. There are several factors helping to accelerate EHR adoption and implementation. First, as younger physicians are brought into the clinical community, they bring with them an increased familiarity with EHRs. Many medical residents have never used a paper-based health record system. As a result, the medical <sup>fi</sup>eld is experiencing an evolutionary shift in their expectations for clinical systems in the hospital environment, creating new internal in<sup>fl</sup>uences on technology innovation [19]. As this new generation of end-users systematically replaces the retiring cohort of physicians, it is likely that their generation of physician-users will accelerate EHR adoption through their expectations and experiences.

A second factor supporting increased adoption is the labor savings that hospitals may realize by eliminating unnecessary duplication of services such as laboratory orders. Consider the labor costs associated with a laboratory order. Sometimes the nursing staff must prepare the patient for an initial procedure (e.g., X-rays, blood draws, and other screening). Laboratory procedures may then require the patient be moved to another part of the facility (e.g., radiology) to be examined. Such movements require the coordination of resources, and constitute a patient hand-off, which is a source of potential medical errors that can prove costly [8]. Even when laboratory orders do not require the patient to be moved, the nursing staff is often redirected from care of other patients as they become involved in completing the order. In either case, unnecessary laboratory orders represent both direct and indirect costs to the nursing staff and a reduction of duplicative orders is a potential source of signi<sup>fi</sup>cant savings. The more readily measured cost of unnecessary or duplicate laboratory orders is within the lab itself. While the materials needed to conduct laboratory tests can be expensive, it is typically the technician's compensation that constitutes the major cost. Unnecessary testing creates avoidable expenses. In an environment where hospitals are remunerated through the use of capitated payments, such additional costs cannot be passed through to the purchaser. These costs must therefore be absorbed by the hospital and result in a concomitant reduction of the operating pro<sup>fi</sup>t of the facility.

Coordinated EHR implementation also increases the availability of information that can be used to demonstrate service delivery and support billing claims. As greater documentation of clinical activities is required for reimbursement, it becomes increasingly impractical to have manual, post hoc entry of orders and other diagnostic information. Medicare has begun the process of requiring providers to track patient outcomes as part of its reimbursement program [4,47]. Patients that are re-admitted to a hospital within thirty days of discharge for the same ailment will trigger a ‘claw-back’ where Medicare seeks to recover its earlier payment. Such changes to payment schemes are important new external in<sup>fl</sup>uences that may also affect HIT innovation and adoption rates [41].

There are three main rationales for studying EHR adoption. First, adoption of EHRs is a resource-intensive effort that represents a perceived risk and non-value adding cost for organizations in the short term. The result is an increase in expense without a concomitant increase in revenue or throughput of the facility, in the short term. Second, there are external pressures to accelerate the adoption process that are linked to <sup>fi</sup>nancial remuneration. These programs and dynamics make such efforts more attractive in the near term as facilities are <sup>fi</sup>- nancially incentivized towards adoption to offset productivity losses. Finally, the opportunities for reducing both patient errors and unnecessary diagnostics, again in the long term, create a willingness to accept costs in the near term manifested as a negative impact on productivity.

The common cause for concern is the role of EHR adoption on productivity. Without understanding HITs, the adoption or implementation process, and productivity, it is impossible to determine whether such gains translate into cost ef<sup>fi</sup>ciencies that pass through to payers, as envisioned. Therefore, examining the role of EHR implementation strategies on hospitals' EFFCH, TC and TFP should be an activity of interest to facility managers, policymakers and payers.

## 3. Measuring hospital productivity

While there are competing de<sup>fi</sup>nitions of ef<sup>fi</sup>ciency and productivity in the literature, they are all built on the same basic principle: the “transformation” of inputs to outputs. The Agency for Healthcare Quality and Research uses a de<sup>fi</sup>nition of ef<sup>fi</sup>ciency that re<sup>fl</sup>ects this perspective “ef<sup>fi</sup>ciency [is] as an attribute of performance that is measured by examining the relationship between a speci<sup>fi</sup>c product of the health care system (also called an output) and the resources used to create that product (also called inputs)” [35]. Ef<sup>fi</sup>ciency measures can be classi<sup>fi</sup>ed in one of three basic forms: ratios, regression estimates, and frontier analytic indices, and these forms can be either simple or complex. Simple measures generally focus on outputs alone, as in the case of patient discharges, or as a ratio of inputs to outputs such as full-time equivalent personnel costs per discharge. The use of ‘simple’ is not intended to imply that they are somehow easy to determine or not robust. Efforts to create simple measures, as de<sup>fi</sup>ned here, include such complex models of measurement as cost per health improvement, which focuses on health functional status rather than cost alone.

Simple measures are advantageous because they are easy to calculate and interpret, and as such, <sup>fi</sup>nd their way into performance dashboards and other metrics popular in healthcare management [35]. However, simple measures often fail to provide actionable information because they fail to explain why hospitals differ in their performance, and are therefore unable to point the way to performance improvements that might be implemented. In contrast, frontier approaches allow complex measures of multiple inputs and outputs to be considered simultaneously. Moreover, the optimal relationship of inputs to outputs can be determined using linear programming as is done in data envelopment analysis (DEA). Therefore, frontier analyses allow managers and researchers to assess how both economies and diseconomies of scale impact ef<sup>fi</sup>ciency and productivity levels [38].

DEA is non-parametric approach that seeks to identify the frontier through the use of linear programming models. There are a number of treatises on the calculation of the DEA frontier. For a more in-depth discussion of DEA, the interested reader is referred to the seminal work by Charnes, Cooper, and Rhodes [11], which provides a number of examples and a step-by-step discussion of both the method and the linear programming associated with the calculations. A more technical discussion can be also found in the article by Banker and Morey [2].

The most commonly used productivity measurement algorithms in the economics literature are the Fisher and Törnquist indices [39]. However, both of these indices require price data to assess productivity. A third approach was developed by Malmquist in 1953 and was subsequently linked to frontier analysis by Caves, Christensen and Diewert [9] as an alternative to the Törnqvist [48] index. The Malmquist TFP index was further explored by Färe et al. [16] who proposed the use of linear programming to identity the frontier, further facilitating analysis [17].

As such, we use DEA to calculate the distance functions, $D _ { t } ^ { o } ( x _ { t } , y _ { t } )$ where $x _ { t }$ is the input vector at period t and $y _ { t }$ is the output vector at period t. The Malmquist TFP index, as de<sup>fi</sup>ned by Caves et al. can be expressed as:

$$
M ^ {o} (x _ {t}, y _ {t}, x _ {t + 1}, y _ {t + 1}) = \left[ \frac {D _ {t} ^ {o} (x _ {t + 1} , y _ {t + 1})}{D _ {t} ^ {o} (x _ {t} , y _ {t})} * \frac {D _ {t + 1} ^ {o} (x _ {t + 1} , y _ {t + 1})}{D _ {t + 1} ^ {o} (x _ {t} , y _ {t})} \right] ^ {1 / 2}.\tag{1}
$$

Eq. (1) can be decomposed to the following:

$$
\begin{array}{l} M ^ {o} (x _ {t}, y _ {t}, x _ {t + 1}, y _ {t + 1}) = \left[ \frac {D _ {t + 1} ^ {o} (x _ {t + 1} , y _ {t + 1})}{D _ {t + 1} ^ {o} (x _ {t} , y _ {t})} \right] \\ * \left[ \frac {D _ {t} ^ {o} (x _ {t + 1} , y _ {t + 1})}{D _ {t + 1} ^ {o} (x _ {t + 1} , y _ {t + 1})} * \frac {D _ {t} ^ {o} (x _ {t} , y _ {t})}{D _ {t + 1} ^ {o} (x _ {t} , y _ {t})} \right] ^ {1 / 2} \end{array}\tag{2}
$$

where the ratio of $\left[ \frac { D _ { t + 1 } ^ { o } \left( x _ { t + 1 } , y _ { t + 1 } \right) } { D _ { t + 1 } ^ { o } \left( x _ { t } , y _ { t } \right) } \right]$ denotes the EFFCH and $\left[ \frac { D _ { t } ^ { o } \big ( x _ { t + 1 } , y _ { t + 1 } \big ) } { D _ { t + 1 } ^ { o } \big ( x _ { t + 1 } , y _ { t + 1 } \big ) } * \frac { D _ { t } ^ { o } ( x _ { t } , y _ { t } ) } { D _ { t + 1 } ^ { o } ( x _ { t } , y _ { t } ) } \right] ^ { 1 / 2 }$ denotes the TC component and the value of these components denote an improvement (greater than 1) or deterioration (less than 1).

The decomposition of TFP has been explored widely in the literature and, more speci<sup>fi</sup>cally, has been used to explore various issues in healthcare [31]. EFFCH measures the technical transformation of input into outputs [27]. When an organization is not on the ef<sup>fi</sup>ciency frontier, the measure of how far it is away from the frontier is called its ‘X-inef<sup>fi</sup>ciency’. Economists refer to this as the ‘management effect’ on organizational performance because well functioning markets will eventually drive inef<sup>fi</sup>cient <sup>fi</sup>rms out of business. Alternatively, insuf-<sup>fi</sup>cient competitive pressures may allow management to engage in suboptimal productivity for extended periods. Under competitive pressure, managers are incentivized to improve their underlying organizational processes in order to keep pace with other <sup>fi</sup>rms in the market through innovation [33].

On the other hand, the TC index measures shifts in the TFP frontier that arise from organizational innovations across organizations. It is interpreted as the change of the “best practice” frontier over time; typically due to improvements in the “technology” of organizational processes [43]. The term “technology” has a general meaning here and refers to information management as well as clinical process innovations. The most signi<sup>fi</sup>cant technological changes in an organization often rely on behavior modi<sup>fi</sup>cations. Collectively evaluating changes in hospitals' ef<sup>fi</sup>ciency and technological acumen is thus critical to evaluating the sector's overall productivity and the impact of major public policies on that productivity.

The use of TFP, EFFCH and TC to explore issues in healthcare is diverse. One study, conducted by Kontodimopolous and Niakas [31] used those three variables to explore productivity among dialysis treatment facilities in Greece. In that article, Malmquist indices were calculated for dialysis facilities in Greece over a 12-year period, using nationally representative panel data. Similar to the study presented here, the authors decomposed the Malmquist TFP into EFFCH and TC.

## 4. Taxonomy of EHR implementation levels and rates

## 4.1. Cross-sectional design

In 2007 and 2008, the AHA gathered data on the use of EHR components encapsulated as a conditional question — “Does your hospital have an electronic health record?” Facilities either scored the question “Yes, fully implemented”, “Yes, partially implemented” or “No” [28]. Those that answered “No” were asked to skip to a later question. Those that selected either of the ‘Yes’ prefaced questions were asked to rank their implementation of ‘Order entry management’ (such as orders for laboratory tests, radiology studies, and other tests)’ [parenthetic notation used in survey]. The overarching EHR item is the focus of this paper to ensure that the level of the variable studied is commensurate with the organizational level of analysis. In this case, the unit of the analysis is the hospitals and the overarching EHR item measures applications that touch most every part of a facility. This taxonomy has been used in the literature in cross-sectional studies discussing EHR adoption trends [29].

## 4.2. Longitudinal design

A second taxonomy was developed to explore how adoptions rates of EHR changed from 2007 to 2008. The comparison of the two years possible responses results in 9 categories. Table 1 illustrates the full model. The <sup>fi</sup>rst three groups are on the diagonal and represent ‘No change’ from 2007 to 2008 at the varying levels of EHR implementation. Fig. 1 illustrates how the respondents to the national survey fared in their adoption pattern.

1. Group 1, the ‘Never Adopter’ (n=614) hospitals are those facilities that reported that they had no EHR system in place in either 2007 or 2008.

2. Group 2 is facilities that reported ‘No Change 1’ (n=1257) in EHR implementation level and had the EHR application ‘partially implemented’.

3. Group 3 is populated with hospitals that experienced ‘No Change 2’ (n=393) in utilization from 2007 to 2008 because they reported ‘full implementation’ in both years.

Groups four through six contain hospitals that reported positive changes in EHR implementation level across years.

4. Group 4, labeled ‘Simple Introduction’ (n=213), are hospitals that reported no EHR usage in 2007, and ‘partially implemented’ usage in 2008. The move from no use to simple introduction belies a signi<sup>fi</sup>cant transition from no use to having an EHR system. This transition entails a signi<sup>fi</sup>cant organizational change and work process redesign is required.

5. Group 5 contains the hospitals that moved from the ‘Yes, partially implemented’ to ‘Yes, fully implemented status and is labeled

Longitudinal taxonomy of EHR functional adoption rates.

<table><tr><td rowspan="2" colspan="2">Question</td><td colspan="3">2008</td></tr><tr><td>No (0)</td><td>Yes, partially implemented (1)</td><td>Yes, fully implemented (2)</td></tr><tr><td rowspan="6">2007</td><td rowspan="2">No (0)</td><td>0-0</td><td>0-1</td><td>0-2</td></tr><tr><td>Group 1-NA</td><td>Group 4-SI</td><td>Group 6-BB</td></tr><tr><td rowspan="2">Yes, partially implemented (1)</td><td>1-0</td><td>1-1</td><td>1-2</td></tr><tr><td>Group 7-FS</td><td>Group 2-NC1</td><td>Group 5-IP</td></tr><tr><td rowspan="2">Yes, fully implemented (2)</td><td>2-0</td><td>2-1</td><td>2-2</td></tr><tr><td>Group 9-TC</td><td>Group 8-PC</td><td>Group 3-NC2</td></tr></table>

Notes: Group 1 — NA is the ‘Never Adopter’, Group 2 — NC1 is the ‘No Change 1’, Group 3 — NC2 is the ‘No Change 2’, Group 4 — SI is the ‘Simple Introduction’, Group 5 — IP is the ‘Incremental Progress’, Group 6 — BB is the ‘Big Bang’, Group 7 — FS is the ‘False Start' Group 8 – PC is the 'Partial Collapse' and Group 9 – TC is the 'Total Collapse'

‘Incremental Progress’ (n=101).

6. Group 6 is called the ‘Big Bang’ (n=26) because it represents the transition from ‘No’ EHR usage to usage to ‘Yes, fully implemented’ in one reporting period. We call this a ‘Big Bang’ because the transitional impacts on the organization are expected to be signi<sup>fi</sup>cant [24,40]

The last three groups reported a declining EHR implementations level from 2007 to 2008.

7. Group 7 is labeled the ‘False Start’ (n=31) and it contains facilities reporting an abandonment of the EHR technology in 2008 after having said, ‘Yes, partially implemented’ in 2007.

8. Group 8 is labeled the ‘Partial Collapse’ (n=81). Members of this group went from reporting, ‘Yes, fully implemented’ in 2007 to reporting at the lower, ‘Yes, partially implemented’ level in 2008.

9. Group is labeled the ‘Total Collapse’ (n=3). This group of hospitals moved from reporting, ‘Yes, fully implemented’ in 2007 to reporting “No” use in 2008. This category represents the most signi<sup>fi</sup>cant form of EHR system abandonment.

The groups formed in the longitudinal taxonomy are used to assess EHR implementation on hospitals' productivity, which is calculated using the Malmquist Algorithm. This leads us to examine the following hypotheses. First, to test for possible response bias, we compare productivity metrics of facilities that responded in both years with those that did not respond in both years. There is a real cause for concern about response bias in the population, as smaller hospitals tend to be less responsive to the AHA survey, historically, than larger ones. We examine this hypothesis across all three productivity measures.

H1. The productivity of facilities reporting EHR status in both years will differ signi<sup>fi</sup>cantly from non-reporting facilities.

H1a. The EFFCH of facilities reporting EHR status in both years will differ signi<sup>fi</sup>cantly from non-reporting facilities.

H1b. The TC of facilities reporting EHR status in both years will differ signi<sup>fi</sup>cantly from non-reporting facilities.

H1c. The TFP of facilities reporting EHR status in both years will differ signi<sup>fi</sup>cantly from non-reporting facilities.

Using the taxonomy in Table 1, we explore productivity differences between the implementation strategies. As noted earlier, we expect differences in the implementation approach to manifest as productivity differences between the strategy categories. We propose the use of ANCOVA as an approach to control for differential effects potentially emerging from membership in the Council of Teaching Hospitals (COTH) and the impact of the controlling authority (CONTROL).

H2. The productivity of facilities reporting EHR status in both years will differ signi<sup>fi</sup>cantly (controlling for COTH and CONTROL).

H2a. The EFFCH of facilities reporting EHR status in both years will differ signi<sup>fi</sup>cantly (controlling for COTH and CONTROL).

H2b. The TC of facilities reporting EHR status in both years will differ signi<sup>fi</sup>cantly (controlling for COTH and CONTROL).

H2c. The TFP of facilities reporting EHR status in both years will differ signi<sup>fi</sup>cantly (controlling for COTH and CONTROL).

The materials and methods used to examine the effects of EHR implementation on TFP, and its components, EFFCH and TC are presented next.

![](/api/attachments/P9UAPNBG/fulltext/images/ab63e1352f9da9b0f6a028ddae2e745f8b1664b076f59855a5ecfc2d0c887d5d.jpg)  
Fig. 1. Analytic plan.

## 5. Material and methods

## 5.1. Data source

This study draws on three iterations of the AHA's Annual Survey of Hospitals from <sup>fi</sup>scal years 2006 to 2008-inclusive. In addition to the variables used to calculate the TFP statistics, a supplemental series of questions asked in 2007 and 2008 related to HIT were used for the secondary analysis. The 2006 AHA data was used as a baseline and 4165 hospitals had the complete data needed to conduct the TFP analysis across all years (sample size availability: 2006: n= 6346; 2007: n=6312; 2008: n=6407). Data were merged, cleaned, and cross-validated in STATA 11 using the AHA ID numbers as universal identi<sup>fi</sup>ers.

## 5.2. Malmquist model specification

Our analysis began by drawing on similar input/output model speci<sup>fi</sup>cations used throughout the literature [35] and the stepwise analytic plan is illustrated in Fig. 1. The analysis used six (6) inputs and <sup>fi</sup>ve (5) outputs drawn from the AHA's Annual Survey of

Hospitals. The input variables include ‘total of licensed beds’ (input 1) as a proxy for the size of the facility. Labor was measured using ‘full-time equivalent employees’ (input 2), excluding the registered nursing staff. This allows us to segregate the ‘nursing staff’ (input 3) from the non-nursing staff in a manner that maximized the available data for the analysis. To better understand patient mix, we included ‘Medicare’ (input 4) and Medicaid inpatient days' (input 5). Finally, we included a calculated measure of high-technology dependent service lines commonly used in frontier analyses [42]. The ‘high-tech 6’ measure is a binary variable based on the number of service lines designated as high-technology. The measure is scored a one (1) if the count is six or more and a zero (0) if it is <sup>fi</sup>ve or less.

Outputs focused on facility usage by patients. To identify those with heavy outpatient surgical loads, we included the number of ‘outpatient surgical procedures’ (output 1). We also used the ‘number of emergency room visits’ (output 2) and the number of ‘total outpatient visits’ (output 3). These three variables offer a good volume measure of outpatient services provided. Inpatient output was measured as the ‘number of patient days’ (output 4) provided beyond the initial admission day. Together with the ‘total admission variable’ (output 5), it is used to capture the average daily census.

The foregoing analysis generated the Malmquist TFP indices using DEAP, a software program authored by Tim Coelli [12]. DEAP provides not only the Malmquist TFP index, but also the measures of EFFCH and TC described above. SPSS is used for the secondary analysis.

## 5.3. Secondary analyses

In order to test for potential response biases between hospitals that provided EHR implementation data and those that did not, t-tests were used to compare the two groups. The data from respondents to the AHA EHR items was used to parse and evaluate the Malmquist TFP index using a one-way Analysis of Co-Variance (ANCOVA) across the groups de<sup>fi</sup>ne by the longitudinal EHR implementation groups. In addition, to the TFP and EHR measures, two control variables were entered: Council of Teaching Hospitals (COTH) membership and for-pro<sup>fi</sup>t versus nonpro<sup>fi</sup>t ownership form (CONTROL). These variables are not true inputs, but they do in<sup>fl</sup>uence productivity and are included for that reason.

Given the hierarchical nature of the groupings, we would expect consistent increases in signi<sup>fi</sup>cance with increases in EHR usage. While we submit that an a priori hierarchy of short-term productivity impacts should be seen based on the disruptive in<sup>fl</sup>uence of the transition, there exists little to no literature on how productivity should be relatively impacted. For instance, one might argue that a linearity exists between “False Start”, “Partial Collapse” and “Total Collapse” such that we would expect productivity to be impacted incrementally along that dynamic. Unfortunately, the size of these groups is often too small to make such judgments possible. As a result, we submit that multiple post hoc comparison of means is an appropriate strategy to enter into the literature the state of the data. The comparisons were used to determine whether the signi<sup>fi</sup>cance tests for each group follow a consistent pattern. The results are presented next.

## 6. Results

U.S. hospitals' performance was evaluated using the Malmquist productivity and ef<sup>fi</sup>ciency indices described earlier. Table 2 summarizes the three indices' geometric means for the period from 2006 to 2008-inclusive. Hospitals experienced an average annual decrease of 4.54% in EFFCH during the three-year period, which translates into a cumulative 8.87% decrease in ef<sup>fi</sup>ciency over the same three-year period. However, declining ef<sup>fi</sup>ciency attributed to EFFCH component of the productivity measure largely offset the gains in the TC factor. Overall, the Malmquist analysis indicates that TFP increased approximately 3.06% over the period studied in the 4165 hospitals that provided a full response to the AHA variables in the frontier analysis' model speci<sup>fi</sup>cation.

To determine whether there was a response bias between those hospitals that submitted responses to the EHR implementation item and those that did not, t-tests were used (see Table 3). The results found no statistical difference between facilities that reported their EHR implementation status and those that did not across the three productivity variables. Hospitals that reported data in both years on EHR implementation were slightly less ef<sup>fi</sup>cient that their counterparts and they were slightly more technologically advanced as indicated by the TC factor — albeit not at a signi<sup>fi</sup>cant level. With respect to TFP, the difference between those that responded to the EHR implementation item and non-respondents indicated that responders enjoyed slightly greater productivity gains; but, not at a statistically signi<sup>fi</sup>cant level. As a result, H1 and all its sub-hypotheses were not supported by the <sup>fi</sup>ndings, which indicate that (possible) response bias is not a concern.

Table 2  
The Malmquist indices summary of U.S. hospitals' means (2006–2008).

<table><tr><td></td><td>Technical efficiency Change (EFFCH)</td><td>Technological Change (TC)</td><td>Total factor Productivity (TFP)</td></tr><tr><td>Mean</td><td>0.9546</td><td>1.0701</td><td>1.0152</td></tr><tr><td>Std. deviation</td><td>0.0777</td><td>0.1536</td><td>0.1199</td></tr><tr><td>Minimum</td><td>0.5330</td><td>0.5380</td><td>0.3410</td></tr><tr><td>Maximum</td><td>1.5220</td><td>3.0740</td><td>2.9800</td></tr></table>

Note: all indices are geometric averages.

An ANCOVA was used to determine if differences existed between the groups on the three Malmquist indices (see Table 4). On the EFFCH measure, marginally signi<sup>fi</sup>cant differences between the groups' implementing EHR were found $( p = 0 . 0 7 3 )$ ). However, the two control variables, being a teaching hospital or for-pro<sup>fi</sup>t were not signi<sup>fi</sup>cantly related to EFFCH. Similar to EFFCH, there were signi<sup>fi</sup>cant differences in the TC index across groups using the longitudinal EHR implementation taxonomy $( p = 0 . 0 2 9 )$ . The TFP index was also signi<sup>fi</sup>cantly related to the longitudinal EHR implementation taxonomy (p=0.021). Unlike the TC component, the ownership variable was signi<sup>fi</sup>cantly related to the taxonomy and TFP $( p = 0 . 0 0 7 )$ . Being a teaching hospital was signi<sup>fi</sup>cantly related to TFP/TC and the longitudinal EHR taxonomy $( p = 0 . 0 3 3 / p = 0 . 0 2 8 )$ . These <sup>fi</sup>ndings of signi<sup>fi</sup>cant differences in TFP and TC and marginally signi<sup>fi</sup>cant differences in EFFCH across the longitudinal EHR taxonomy provide support for H2.

To provide a basis for discussion, we report the means for EFFCH, TC, and TFP at the subgroup level. Next, the EHR implementation groups are compared in relationship to each other and strati<sup>fi</sup>ed across the Malmquist indices (see Table 5). There are signi<sup>fi</sup>cant differences between the groups' EFFCH depending on what stage they of EHR implementation they are in described by the longitudinal taxonomy. Facilities that had ‘Never Adopted’ (Group 1) an EHR had the highest level of EFFCH. Those hospitals that used the ‘Big Bang’ (Group 6) EHR implementation strategy had the lowest level of EFFCH among all the groups.

The pattern of EHR implementation group membership relative to TC was qualitatively different and nearly opposite from the results of the EFFCH groupings. In particular, the relationship between TC and facilities that had ‘Never Adopted’ (Group 1) an EHR showed that they had the second lowest gain in this dimension. Hospitals that used the ‘Big Bang’ (Group 6) EHR implementation strategy had the highest level of TC among all the groups. Those facilities that reported having fully implemented an EHR had the second highest level of TC, indicating that impact of adoption was still being felt.

Similar to the EFFCH measure, TFP gains over the three years studied were greatest in the ‘Never Adopted’ EHR group (Group 1). The group with the lowest TFP was the ‘Total Collapse’ group, but it only had three members. The next lowest group in terms of TFP was the ‘Big Bang’ cohort, which went from reporting ‘No’ to the EHR use item in 2007 to reporting, ‘Yes, fully implemented’ in 2008.

## 7. Discussion

Efforts to increase U.S. hospitals' productivity through the use of EHR systems are meeting with mixed results. On the one hand, over the three years studied, hospitals were able to increase technical ef<sup>fi</sup>- ciency levels (EFFCH) under every possible EHR implementation scenario. On the other hand, efforts to improve the underlying care processes (i.e., TC) were not yet able to make a positive contribution to TFP as is evidenced by the fact no group's mean TC exceeded one. Therefore, there has been a trade-off between the EFFCH and TC factors resulting in minor gains in overall TFP.

Productivity gains attributable to process improvements, measured as the mean TC, did not exceed unity (TCb1.0) over the period studied. Put another way, the impact of TC as a contributor to hospital productivity is not positive in the near-term. Given the use of full-time equivalent employees and nurses as inputs, this analysis could indicate that hospital employees are working harder (i.e., increasing ef<sup>fi</sup>ciency gains), but not necessarily smarter (i.e., effectively employing new technologies) in order to generate incremental, but marginal gains. Alternatively, hospitals could be expanding their numbers of licensed beds to gain economies of scale that would increase ef<sup>fi</sup>ciency, but not in<sup>fl</sup>uence TC. Given the relatively short time frame of the study, the former seems to be the more plausible explanation as major changes to physical structures are unlikely to have occurred in a widespread, systematic fashion that could be detected. As noted above, the EFFCH measure does account for the majority of gains in overall productivity rather than TC, and those results are con<sup>fi</sup>rmed by the data.

Table 3  
t-Test for difference between respondents and non-respondents for EHR status and Malmquist indices.

<table><tr><td></td><td>EHR reported in both 2007 and 2008 (Yes = 1)</td><td>n</td><td>Mean</td><td>Std. deviation</td><td>Std. error mean</td><td>t-Test</td><td>Significance (p-value)</td></tr><tr><td rowspan="2">EFFCH</td><td>1</td><td>2719</td><td>1.06934</td><td>0.13931</td><td>0.00267</td><td>0.4256</td><td>0.6704</td></tr><tr><td>0</td><td>1446</td><td>1.07147</td><td>0.17752</td><td>0.00467</td><td></td><td></td></tr><tr><td rowspan="2">TC</td><td>1</td><td>2719</td><td>0.95599</td><td>0.07288</td><td>0.00140</td><td>1.5914</td><td>0.1116</td></tr><tr><td>0</td><td>1446</td><td>0.95197</td><td>0.08588</td><td>0.00226</td><td></td><td></td></tr><tr><td rowspan="2">TFP</td><td>1</td><td>2719</td><td>1.01693</td><td>0.10927</td><td>0.00210</td><td>1.2534</td><td>0.2101</td></tr><tr><td>0</td><td>1446</td><td>1.01203</td><td>0.13767</td><td>0.00362</td><td></td><td></td></tr></table>

With respect to EHR implementation strategies, as presented in Table 5, the most underperforming approach is the Big Bang roll-out. Fully implementing an EHR over the course of one year has a negative impact on both EFFCH and TFP — at least in the short-run. This <sup>fi</sup>nding is further reinforced by the fact that the TC for the Big Bang hospitals is the highest among the groups.

The best performing EHR implementation strategy with respect to relative EFFCH and TFP, is NOT to adopt at all. For hospital administrators, this may con<sup>fi</sup>rm their fear that to be an early EHR adopter is to be on the ‘bleeding edge’. Therefore, the bene<sup>fi</sup>ts of waiting to implement an EHR, while others suffer through the trial and error process, may outweigh the penalties of forgoing Meaningful Use rewards and incentives. Supporting this <sup>fi</sup>nding is the fact that the eighty-one hospitals that reduced their EHR implementation level (Partial Collapse) had the second highest overall TFP relative to the other groups.

The ‘Simple Introduction’ approach to EHR implementation also presented an interesting pattern of results relative to the other groups. The ‘Simple-Introduction’ group had the second highest level of EFFCH, the lowest level of TC and the third lowest relative gain in TFP. That pattern may re<sup>fl</sup>ect the signi<sup>fi</sup>cant disruption to work<sup>fl</sup>ows which accompany an initial EHR implementation (i.e., lower TC), while the hospital continues to admit and treat patients at its usual operating levels (i.e., higher EFFCH). The net effect is that workers are making-up for the EHR driven change in process through additional effort, but it still leads to relatively lower TFP compared to other groups. Such a pattern is consistent with the normal stresses of introducing new technologies and processes while attempting to maintain previous levels of throughput. Given the economic conditions that U.S. hospitals are operating under, it is likely that this pro<sup>fi</sup>le will be the norm for many facilities in the short-term as they begin to implement EHRs.

ANCOVA for Malmquist indices and longitudinal taxonomy of EHR implementation levels (including covariates).

<table><tr><td>Variable</td><td></td><td>Sum of squares</td><td>df</td><td>Mean square</td><td>F</td><td>Sig.</td></tr><tr><td rowspan="5">EFFCH</td><td>Between groups</td><td>0.07266</td><td>8</td><td>3.81</td><td>0.000</td><td>0.07266</td></tr><tr><td>COTH</td><td>0.20224</td><td>1</td><td>10.61</td><td>0.001</td><td>0.20224</td></tr><tr><td>CONTROL</td><td>0.31364</td><td>1</td><td>16.45</td><td>0.000</td><td>0.31364</td></tr><tr><td>Within groups</td><td>0.01907</td><td>2708</td><td></td><td></td><td>0.01907</td></tr><tr><td>Total</td><td>0.01941</td><td>2718</td><td></td><td></td><td>0.01941</td></tr><tr><td rowspan="5">TC</td><td>Between groups</td><td>0.02852</td><td>8</td><td>5.54</td><td>0.000</td><td>0.02852</td></tr><tr><td>COTH</td><td>0.02838</td><td>1</td><td>5.51</td><td>0.019</td><td>0.02838</td></tr><tr><td>CONTROL</td><td>0.25246</td><td>1</td><td>49.04</td><td>0.000</td><td>0.25246</td></tr><tr><td>Within groups</td><td>0.00515</td><td>2708</td><td></td><td></td><td>0.00515</td></tr><tr><td>Total</td><td>0.00531</td><td>2718</td><td></td><td></td><td>0.00531</td></tr><tr><td rowspan="5">TFP</td><td>Between groups</td><td>0.02117</td><td>8</td><td>1.78</td><td>0.077</td><td>0.02117</td></tr><tr><td>COTH</td><td>0.03266</td><td>1</td><td>2.74</td><td>0.098</td><td>0.03266</td></tr><tr><td>CONTROL</td><td>0.00749</td><td>1</td><td>0.63</td><td>0.428</td><td>0.00749</td></tr><tr><td>Within groups</td><td>0.01190</td><td>2708</td><td></td><td></td><td>0.01190</td></tr><tr><td>Total</td><td>0.01194</td><td>2718</td><td></td><td></td><td>0.01194</td></tr></table>

NOTE: the ANCOVA includes two control variables: Council of Teaching Hospitals (COTH) membership and for-pro<sup>fi</sup>t versus nonpro<sup>fi</sup>t ownership form (CONTROL).

## 8. Conclusion

Computerization of clinical information is an essential component of a broader system of hospital changes. To gain productivity advantages from computers in healthcare settings, rather than simply computerizing their traditional practices, managers have to re-engineer the hospital to match their work<sup>fl</sup>ows with the capabilities of new EHR systems. Therefore, it is necessary to implement work process changes throughout the hospital, which represents a major technological change. Further, it is reasonable to assume that changes in EHR would impact hospital productivity negatively in the short-run.

There is more to implementing an EHR system than just the installation of new computers. The transition to an EHR environment from a paper system must occur concomitantly with a rethinking of job processes, employees' new roles and responsibilities (i.e., scope of practice) and the needed organizational hierarchy changes [10]. Among other things, the move to a fully functional EHR implies upgrading the skills of the workforce, which would impact EFFCH favorably. Further, for increasing productivity and fostering innovation, a multi-disciplinary educated workforce is critical to being able to use evidence-based guidelines.

Descriptive statistics for Malmquist indices by longitudinal taxonomy of EHR implementation levels.

<table><tr><td>Variable</td><td>Category</td><td>n</td><td>Mean</td><td>Std. deviation</td><td>Std. error</td></tr><tr><td rowspan="9">EFFCH</td><td>Group 1: ‘Never Adopter’</td><td>614</td><td>1.08874</td><td>0.17804</td><td>0.00719</td></tr><tr><td>Group 2: ‘No Change 1’</td><td>1257</td><td>1.06875</td><td>0.13181</td><td>0.00372</td></tr><tr><td>Group 3: ‘No Change 2’</td><td>393</td><td>1.04976</td><td>0.08762</td><td>0.00442</td></tr><tr><td>Group 4: ‘Simple Intro.’</td><td>213</td><td>1.08230</td><td>0.15162</td><td>0.01039</td></tr><tr><td>Group 5: ‘Incremental Prog.’</td><td>101</td><td>1.03528</td><td>0.09908</td><td>0.00986</td></tr><tr><td>Group 6: ‘Big Bang’</td><td>26</td><td>1.01431</td><td>0.12496</td><td>0.02451</td></tr><tr><td>Group 7: ‘False Start’</td><td>31</td><td>1.05358</td><td>0.10805</td><td>0.01941</td></tr><tr><td>Group 8: ‘Partial Collapse’</td><td>81</td><td>1.06035</td><td>0.12492</td><td>0.01388</td></tr><tr><td>Group 9: ‘Total Collapse’</td><td>3</td><td>1.01567</td><td>0.06123</td><td>0.03535</td></tr><tr><td rowspan="9">TC</td><td>Group 1: ‘Never Adopter’</td><td>614</td><td>0.94929</td><td>0.08344</td><td>0.00337</td></tr><tr><td>Group 2: ‘No Change 1’</td><td>1257</td><td>0.95435</td><td>0.07123</td><td>0.00201</td></tr><tr><td>Group 3: ‘No Change 2’</td><td>393</td><td>0.97252</td><td>0.04468</td><td>0.00225</td></tr><tr><td>Group 4: ‘Simple Intro.’</td><td>213</td><td>0.94125</td><td>0.09513</td><td>0.00652</td></tr><tr><td>Group 5: ‘Incremental Prog.’</td><td>101</td><td>0.96731</td><td>0.05912</td><td>0.00588</td></tr><tr><td>Group 6: ‘Big Bang’</td><td>26</td><td>0.97396</td><td>0.04186</td><td>0.00821</td></tr><tr><td>Group 7: ‘False Start’</td><td>31</td><td>0.95519</td><td>0.06546</td><td>0.01176</td></tr><tr><td>Group 8: ‘Partial Collapse’</td><td>81</td><td>0.97128</td><td>0.06604</td><td>0.00734</td></tr><tr><td>Group 9: ‘Total Collapse’</td><td>3</td><td>0.95233</td><td>0.01358</td><td>0.00784</td></tr><tr><td rowspan="9">TFP</td><td>Group 1: ‘Never Adopter’</td><td>614</td><td>1.02781</td><td>0.15469</td><td>0.00624</td></tr><tr><td>Group 2: ‘No Change 1’</td><td>1257</td><td>1.01416</td><td>0.09271</td><td>0.00261</td></tr><tr><td>Group 3: ‘No Change 2’</td><td>393</td><td>1.01946</td><td>0.08022</td><td>0.00405</td></tr><tr><td>Group 4: ‘Simple Intro.’</td><td>213</td><td>1.00861</td><td>0.09838</td><td>0.00674</td></tr><tr><td>Group 5: ‘Incremental Prog.’</td><td>101</td><td>0.99847</td><td>0.08155</td><td>0.00812</td></tr><tr><td>Group 6: ‘Big Bang’</td><td>26</td><td>0.98477</td><td>0.09762</td><td>0.01914</td></tr><tr><td>Group 7: ‘False Start’</td><td>31</td><td>1.00336</td><td>0.09544</td><td>0.01714</td></tr><tr><td>Group 8: ‘Partial Collapse’</td><td>81</td><td>1.02731</td><td>0.11467</td><td>0.01274</td></tr><tr><td>Group 9: ‘Total Collapse’</td><td>3</td><td>0.96633</td><td>0.04895</td><td>0.02826</td></tr></table>

Nonetheless many organizations retain their old structures because the required EHR changes are time consuming to learn, risky, and initially costly. In large part this problem emerges because such changes are perceived as impinging on the professional domains of the many clinically trained stakeholders–physicians in particular [6]. Therefore, rather than changing their behavior or increasing the skills of current staffers, it is a more common strategy to add a costly specialist (i.e., outsourcing) to handle speci<sup>fi</sup>c types of EHR issues in professional domains. The increase use of scribes is one indication that this phenomenon may be occurring [1]. For the sample of U.S. hospitals studied, TFP levels increased from 2006 to 2008, but only to a small degree. Further, the TFP gains witnessed are largely the result of increases in EFFCH rather than changes in the underlying technological processes (TC) used by facilities.

EHR systems are networked technologies, and networked technologies' ef<sup>fi</sup>ciency increases as more users join the systems. Therefore, the bene<sup>fi</sup>ts of information technologies, such as EHR, are not fully realized until their adoption reaches critical mass [20]. The time delays in the development of such symbiotic relationships are among the reasons economists give for the rise of a “productivity paradox” [46], which arises when a new technology does not increase ef<sup>fi</sup>ciency in the near term. Without demonstrable savings in direct care costs, such as labor expenses, the cost-bene<sup>fi</sup>t analysis becomes more dif<sup>fi</sup>cult to measure. This has a secondary effect of pushing returns on investment beyond the typical payback horizons demanded by most managers, further delaying the adoption of other critical elements of the HIT network. Therefore, a negative feedback loop is created that dampens the diffusion of technology. To the extent that DEA can demonstrate long-term increases in productivity related to the use of EHR, it has the potential to re<sup>fi</sup>ne and more accurately inform managers' calculations.

Of greater concern is the push to Meaningful Use and the implication of these <sup>fi</sup>ndings to such efforts. The data suggests that when EHR implementation is advanced too quickly in hospitals (e.g., the Big Bang), ef<sup>fi</sup>ciency and productivity are impacted negatively relative to other facilities. The loss is made larger by the fact that facilities using some of the other incremental strategies experience productivity gains in the same year.

## 9. Limitations and future research

The AHA datasets used here suffer from the following limitations. First, they do not provide complete information on EHR implementation status for all U.S. hospitals for the entire period studied. Second, the AHA survey is conducted on an annual basis, which limits within year analysis of EHR adoption. Third, because hospitals may also be conducting other process improvements along with EHR implementation, the causal effect of EHR implementation cannot be isolated accurately. Further, the study does not include reimbursement information that would allow other forms of productivity analyses to be performed [25]. In particular, it would be useful to generate information on allocative ef<sup>fi</sup>ciency using the Fisher [18] and Törnqvist [48] productivity indices. However, such models require better service pricing information that is not widely available. Indices that include such pricing data would be more helpful to the study of policy changes designed to increase productivity by using global payment schemes that are central to many healthcare reform plans now being promoted [36]. Finally, another limitation of this study is its focus on near-term productivity gains <sup>fl</sup>owing from various EHR implementation strategies. Therefore, as more hospitals implement EHR systems and gain experience with them, over longer time frames, TFP studies like this one can be expected to yield more conclusive results about the cost effectiveness and return-on-investment from EHR use.

## References

[1] Anonymous, Do your docs need scribes to use an EMR? MGMA Connexion 8 (5) (2008) 13.

[2] R. Banker, R. Morey, Ef<sup>fi</sup>ciency analysis for exogenously <sup>fi</sup>xed inputs and outputs, Operations Research 34 (4) (1986) 513–521.

[3] C.P. Barros, A. Gomes de Menzes, N. Peypoch, B. Solonandrasana, J.C. Vieira, An analysis of hospital ef<sup>fi</sup>ciency and productivity growth using the Luenberger indi cator, Health Care Management Science 11 (4) (2008) 373–381.

[4] C. Becker, Time to pay for quality. CMS will partner with premier in trial project to give <sup>fi</sup>nancial bonuses to hospitals that deliver the best care, Modern Healthcare 33 (26) (2003) 6–7 (16, 11)

[5] E. Biørn, T. Hagen, T. Iversen, J. Magnussen, How different are hospitals' responses to a <sup>fi</sup>nancial reform? The impact on ef<sup>fi</sup>ciency of activity-based <sup>fi</sup>nancing, Health Care Management Science 13 (1) (2010) 1–16.

[6] S.C. Blake, S. Kohler, K. Rask, A. Davis, D.V. Naylor, Facilitators and barriers to 10 National Quality Forum safe practices, American Journal of Medical Quality 21 (5) (2006) 323–334.

[7] V.H. Castillo, A.I. Martinez-Garcia, J.R. Pulido, A knowledge-based taxonomy of critical factors for adopting electronic health record systems by physicians: a systematic literature review, BMC Medical Informatics and Decision Making 10 (2010) 60.

[8] K. Catalano, Hand-off communication does affect patient safety, Plastic Surgical Nursing 29 (4) (2009) 266–270.

[9] D. Caves, L. Christensen, W. Diewert, The economic theory of index numbers and the measurement of input, output, and productivity, Econometrica 50 (1982) 1393–1414 (pre-1986).

[10] G. Chapman, Innovation: the “productivity paradox” requires a human solution, 1997.

[11] A. Charnes, W. Cooper, E. Rhodes, Measuring the ef<sup>fi</sup>ciency of decision making units, European Journal of Operational Research 2 (1978) 429–444.

[12] T. Coelli, D. Rao, C. O'Donnell, G. Battese, An Introduction to Ef<sup>fi</sup>ciency and Productivity Analysis, 2nd ed. Springer, New York 2005.

[13] R. Cunningham, Stimulus bill implementation: expanding meaningful use of health IT, NHPF Issue Brief (834) (2009) 1–16.

[14] D. Cutler, K. Davis, K. Stremikis, Why health reform will bend the cost curve, in: Issue Brief, Commonwealth Fund, 2009, pp. 1–16.

[15] S. DeVore, K. Figlioli, Lessons premier hospitals learned about implementing electronic health records, Health Affairs 29 (4) (2010) 664.

[16] R. Fare, S. Grosskopf, P. Roos, The Malmquist Total Factor Productivity Index: Some remarks, SSRN eLibrary1995

[17] R. Färe, S. Grosskopf, R.R. Russel, Index Numbers: Essays in Honor of Sten Malmquist, Springer-Verlag, New York 1997.

[18] I. Fisher, The Making of Index Numbers, Houghton-Mif<sup>fl</sup>in, Boston 1922.

[19] E.W. Ford, N. Menachemi, M.T. Phillips, Predicting the adoption of electronic health records by physicians: when will health care be paperless? Journal of the American Medical Informatics Association 13 (1) (2006) 106–112.

[20] E.W. Ford, A. McAlearney, M.T. Phillips, N. Menachemi, B. Rudolph, Predicting Computerized Physician Order Entry (CPOE) adoption in U.S. hospitals: can the federal mandate be met? International Journal of Medical Informatics 77 (2) (2008).

[21] K. Goolsby, The story of evolving the world's <sup>fi</sup>rst Computerized Physician Order Entry system and implications for today's CPOE decision makers, in: BPO Outsourcing Journal, 2002.

[22] N. Grunden, Lean at the front line: all hands on deck, Frontiers of Health Services Management 26 (1) (2009) 33–37.

[23] R. Heeks, Health information systems: failure, success and improvisation, International Journal of Medical Informatics 75 (2) (2006) 125–137.

[24] S. Heichert, Taking the big bang approach, Health Data Management 16 (6) (2008) 72.

[25] I. Herrero, S. Pascoe, Analysing the effect of technical change on individual outputs using modi<sup>fi</sup>ed quasi-Malmquist indexes, The Journal of the Operational Research Society 55 (10) (2004) 1081.

[26] P.S. Hussey, H.d. Vries, J. Romley, M.C. Wang, S.S. Chen, P.G. Shekelle, E.A. McGlynn, A systematic review of health care ef<sup>fi</sup>ciency measures, Health Services Research 44 (3) (2009) 784–805.

[27] I. Isik, Bank ownership and productivity developments: evidence from Turkey, Studies in Economics and Finance 24 (2) (2007) 115.

[28] A.K. Jha, C.M. DesRoches, E.G. Campbell, K. Donelan, S.R. Rao, T.G. Ferris, A. Shields, S. Rosenbaum, D. Blumenthal, Use of electronic health records in U.S. hospitals, The New England Journal of Medicine 360 (16) (2009) 1628–1638.

[29] A. Jha, C. DesRoches, P.D. Kralovec, M.S. Joshi, A progress report on electronic health records in U.S. hospitals, Health Affairs 29 (10) (2010) (web-<sup>fi</sup>rst).

[30] D.B. Kendall, in: Improving Health Care — by ‘Spreading the Mayo’ (the Mayo Clinic Model, That Is), PPI, 2009.

[31] N. Kontodimopoulos, D. Niakas, A 12-year analysis of Malmquist total factor productivity in dialysis facilities Journal of Medical Systems 30 (5) (2006) 333–342

[32] J. Kwok, B. Jones, Unnecessary repeat requesting of tests: an audit in a government hospital immunology laboratory Journal of Clinical Pathology 58 (2005) 457–462 g g

[33] J.R. Langabeer II, Y.A. Ozcan, The economics of cancer care: longitudinal changes in provider ef<sup>fi</sup>ciency, Health Care Management Science 12 (2) (2009) 192–200.

[34] C. Lovis, S. Spahni, N. Cassoni, A. Geissbuhler, Comprehensive management of the access to the electronic patient record: towards trans-institutional networks, International Journal of Medical Informatics 76 (5–6) (2007) 466–470.

[35] E.A. McGlynn, Identifying, categorizing, and evaluating health care ef<sup>fi</sup>ciency measures, in: Final Report (prepared by the Southern California Evidence-based Practice Center—RAND Corporation, under Contract No. 282-00-0005-21). AHRQ Publication No. 08-0030, Agency for Healthcare Research and Ouality, Rockyille, MD, 2008.

[36] R.E. Mechanic, S.H. Altman, Payment Reform Options: Episode Payment is a Good Place to Start. Health Aff, Millwood2009

[37] H. Mekhjian, J. Saltz, P. Rogers, J. Kamal, Impact of CPOE order sets on lab orders, in: AMIA Annu Symp Proc, 2003, p. 931.

[38] Y.A. Ozcan, Physician benchmarking: measuring variation in practice behavior in treatment of otitis media, Health Care Management Science 1 (1) (1998) 5–17.

[39] M.B. Reinsdorf, W.E. Diewert, C. Ehemann, Additive decompositions for Fisher, Törnqvist and geometric mean indexes, Journal of Economic and Social Measurement 28 (1) (2002) 51–61.

[40] B. Roberts, Big Bang or Phased Rollout?, HR Magazine, 49(1) (2004) 89.

[41] J.C. Robinson, L.P. Casalino, R.R. Gillies, D.R. Rittenhouse, S.S. Shortell, S. Fernandes-Taylor, Financial incentives, quality improvement programs, and the adoption of clinical information technology, Medical Care 47 (4) (2009) 411–417.

[42] M.D. Rosko, J. Proenca, J.S. Zinn, G.J. Bazzoli, Hospital inef<sup>fi</sup>ciency: what is the impact of membership in different types of systems? Inquiry 44 (3) (2007) 335–349.

[43] N. Salehirad, T. Sowlati, Productivity and ef<sup>fi</sup>ciency assessment of the wood industry: a review with a focus on Canada, Forest Products Journal 56 (11/12) (2006) 25.

[44] M. Segal, Quality/cost initiative of PPACA: an evolution in healthcare delivery? The Journal of Medical Practice Management 26 (2) (2010) 106–108.

[45] C. Stolle, Evidence-based order sets and CPOE. Interview by Mark Hagland, Healthcare Informatics 27 (9) (2010) 46, 48.

[46] M. Thouin, J.J. Hoffman, E.W. Ford, The effect of Information Technology (IT) investments on <sup>fi</sup>rm-level performance in the healthcare industry, Health Care Management Review 33 (1) (2008) 60–69.

[47] J. Tieman, Experimenting with quality. CMS-premier initiative to reward best, punish worst, Modern Healthcare 33 (28) (2003) 6.

[48] L. Törnqvist, The Bank of Finland's consumption price index, Bank Finland Monthl Bulletin 10 (1936) 1–8.

[49] F.B. Yu, N. Menachemi, E.S. Berner, J.J. Allison, N.W. Weissman, T.K. Houston, Full implementation of computerized physician order entry and medication-related quality outcomes: a study of 3364 hospitals, American Journal of Medical Quality 24 (4) (2009) 278–286.

Dr. Timothy R. Huerta (MPA, California State University, Los Angeles; Ph.D., University of Southern California) is currently an Assistant Professor in Health Organization Management (HOM) in the Rawls College of Business at Texas Tech University and the Director of the Center for Healthcare Innovation, Education and Research (CHIER). Tim is currently working directly with Covenant Health System on both its Electronic Health Record (EHR) implementation and its quality improvement program. This collaboration enables him to work with healthcare organizations in addressing the “value proposition” — the development of outcome measures that link quality of care with organizational ef<sup>fi</sup>ciency.

Mark A. Thompson is an Associate Professor of Operations Management and Associate Director of the Health Organization Management program at Texas Tech University. He joined the faculty in 2009 and has worked in the <sup>fi</sup>elds of operations management, risk analysis, energy, and health care. Currently, he serves as the co-editor of International Journal of Information and Operations Management Education and on the editorial board of another journal. Professor Thompson has previously held positions as the Cree-Walker Chair of Business Administration at Augusta State University, as State Economic Forecaster at the University of Arkansas-Little Rock, and as Assistant Professor at Stephen F. Austin State University.

Eric W. Ford is the Forsyth Medical Center Distinguished Professor of Healthcare at the University of North Carolina Greensboro. Prior to his current position, Dr. Ford was the Director of Texas Tech's Health Organization Management Program and the Center for Health Innovation, Education & Research. Eric's research interests include healthcare information systems and how they are used to improve patient safety and control costs. He is currently working on multiple grants and contracts to study health information technology, patient-safety initiatives, and processes for quality improvement. Ford is a graduate of Cornell University and earned his Ph.D. in Administration from the University of Alabama at Birmingham.

William F. Ford holds the Weatherford Chair of Finance in the Jennings A. Jones College of Business at Middle Tennessee State University. He formerly served as Dean of the Business School at the University of Denver; President and CEO of the Federal Reserve Bank of Atlanta; President and COO of First Nationwide Bank; Senior Vice President of Wells Fargo Bank; and as Executive Director and Chief Economist of the American Bankers Association. Dr. Ford often appears on nationwide and regional TV and radio business news shows as an economic policy expert and served as TeleCheck's Senior Economic Advisor from 1990 to 2001. He has authored or coauthored about 100 articles in business and academic journals and has served on the boards of six corporations, the U.S. Chamber of Commerce and NABE, the National Association for Business Economics. He is also an elected Fellow of NABE and the Phi Beta Kappa Society.
