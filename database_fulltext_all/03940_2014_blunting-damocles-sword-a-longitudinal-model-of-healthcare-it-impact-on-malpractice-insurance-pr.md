---
otero_id: 3940
otero_key: "7CJ3NTN7"
title: "Blunting Damocles' Sword: A Longitudinal Model of Healthcare IT Impact on Malpractice Insurance Premium and Quality of Patient Care"
authors: "Nirup M. Menon; Rajiv Kohli"
year: "2014"
journal: "Information Systems Research"
doi: "10.1287/isre.2013.0484"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## 6SR

![](/api/attachments/7CJ3NTN7/fulltext/images/e5ed98b704c80ac9d13b4fc11ae37c4b39bc16ce9f578e88b7c3153483d20b13.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Blunting Damocles' Sword: A Longitudinal Model of Healthcare IT Impact on Malpractice Insurance Premium and Quality of Patient Care

Nirup M. Menon, Rajiv Kohli

To cite this article:

Nirup M. Menon, Rajiv Kohli (2013) Blunting Damocles' Sword: A Longitudinal Model of Healthcare IT Impact on Malpractice Insurance Premium and Quality of Patient Care. Information Systems Research 24(4):918-932. http://dx.doi.org/10.1287/ isre.2013.0484

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2013, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/7CJ3NTN7/fulltext/images/2ab376cef876dbbcb442f1eb6fce7c946d2fc789451f49e21dfa13705f16772c.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

http://dx.doi.org/10.1287/isre.2013.0484 © 2013 INFORMS

# Blunting Damocles’ Sword: A Longitudinal Model of Healthcare IT Impact on Malpractice Insurance Premium and Quality of Patient Care

Nirup M. Menon

School of Management, George Mason University, Fairfax, Virginia 22030, nmenon@gmu.edu

Rajiv Kohli

Mason School of Business, College of William and Mary, Williamsburg, Virginia 23187, rajiv.kohli@mason.wm.edu

rior studies on the business value of information technology (IT) mainly focus on the impact of IT investments on productivity and firm profitability. Few have considered its implication on expected and actual product or service quality. This paper fills this gap by investigating the impact of past healthcare IT (HIT) expenditure on the malpractice insurance premium (MIP) and the moderating effect of past HIT expenditure on the relationship between past MIP and current quality of patient care in a longitudinal model. Based on archival panel data on costs, operations, and patient care outcomes of 66 hospitals in the U.S. state of Washington from 1998 to 2007, we find that past HIT expenditure is negatively associated with MIP, supporting our argument that HIT provides value that is anticipated by insurers and is captured by a change in MIP. We find that past HIT is positively associated with quality of patient care. We also find that past MIP is positively associated with quality of patient care, supporting the premise that hospitals respond to MIP by making risk mitigation efforts. However, we find that past HIT moderates this relationship negatively, suggesting a reliance on HIT at the expense of risk mitigation.

Key words: business value of IT; organizational risk; hospital; dynamic panel model

History: Vallabh Sambamurthy, Senior Editor. This paper was received May 26, 2010, and was with the authors 17 months for 3 revisions. Published online in Articles in Advance May 28, 2013.

## 1. Introduction

Like Damocles’ sword,<sup>1</sup> the threat of financial liability hangs over hospital managers in the form of malpractice lawsuits by patients for a perceived lack of quality patient care. Reasons for malpractice lawsuits include failure to accurately diagnose a disease condition or to administer the correct drug or errors during the conduct of a medical, surgical, therapeutic or diagnostic procedure, whether by intention or by oversight of a healthcare provider (Danzon 1985, Dubay et al. 1999, Weissman et al. 2005). The Kaiser Family Foundation<sup>2</sup> reports that 9,497 malpractice claims were paid in the United States in 2011 for the total amount of \$3.1 billion. Healthcare providers purchase malpractice insurance to protect themselves from financial liabilities resulting from malpractice claims judgments issued against them by the courts (Danzon 1985). The malpractice insurance premium (MIP) is the price that the hospital pays to the insurance company for protection from financial liability related to malpractice claim judgments (Danzon 1985, Dubay et al. 1999).

According to the National Association of Insurance Commissioners,<sup>3</sup> the total MIP in the United States grew from \$5 billion in 1991 to \$10 billion in 2011. An increase in MIP is likely to increase costs for hospitals, third-party payers, patients, and healthcare in general because healthcare providers raise prices for services in response to higher MIP and overuse healthcare services by practicing “defensive medicine” to reduce risk of malpractice claim lawsuits (Mello et al. 2010, Kessler 2011). Baicker et al. (2007) attribute an increase of more than \$15 billion in Medicare spending between 2000 and 2003 to a 60% increase in malpractice premiums during the same period. Likewise, Mello et al. (2010) estimate that the total annual cost of the medical liability system is about \$55.6 billion.

MIP is an important topic for information systems (IS) researchers because discussions in academia and public policy have centered around exploiting the potential of healthcare information technology (HIT), such as electronic health records, computer-assisted physician order entry, decision support, and pharmacy information systems, to lower overall malpractice costs (Hill et al. 2007, Mangalmurti et al. 2010, Orszag 2008). Although a few studies have examined the impact of HIT on malpractice claims activity and payout (e.g., Ransbotham et al. 2011), no study thus far has investigated how HIT impacts MIP. By studying the impact of HIT on MIP, we contribute to the HIT and healthcare literatures as well as inform the IT business value literature by establishing that IT provides value for organizations through the assurance of reduced ex ante risk. Such assurance is likely to translate into observable financial benefits. The presence of HIT in a hospital persuades an insurer to lower MIP and reduces spending of a hospital to protect itself from malpractice claims liabilities.<sup>4</sup>

Prior research on the business value of information technology (IT) has found that external entities, such as suppliers, financial markets, customers, and regulators who engage with other organizations, pay attention to IT investments of such organizations when evaluating the engagement. For instance, financial markets take into account expected cash flows from current IT investments when valuing a firm (Subramani and Walden 2001). The Joint Commission, an independent, not-for-profit organization that evaluates and accredits more than 20,000 healthcare organizations and programs in the United States, considers how HIT will be used to manage information in ensuring patient care quality when approving accreditation of hospitals.<sup>5</sup> In our context, malpractice insurers are external parties that evaluate a hospital’s HIT before settling on the amount of MIP.

In order to drive down premiums, a hospital can demonstrate to malpractice insurers that it has instituted appropriate technologies and processes and that its activities pose low risk of malpractice claims. For its part, a malpractice insurer assumes the financial risk with the expectation that a hospital’s investment in technologies and processes will enable (1) the hospital to avoid mistakes and intercept errors (e.g., a pharmacy IT to intercept dispensing an incorrect dose or wrong drug) before they harm patients and (2) the insurer to obtain electronic records and seek the cause when errors occur. That is, a hospital’s actions and an insurer’s premiums are influenced by the expected benefits from HIT when determining ex ante risk of malpractice claims. Both parties expect that HIT will monitor, control, and reduce information asymmetry between clinicians and the hospital and between the hospital and the insurer. Insurers believe that malpractice claims will be rare and the process of defending malpractice claims will be manageable and transparent. Thus, the hospital can blunt the proverbial Damocles’ sword by using HIT in two ways: (1) incurring lower MIP by investing in HIT and (2) improving the quality of patient care through use of HIT to (a) reduce the number and size of malpractice claims and payouts, if they occur, and (b) receive further discounts in MIP in the future by providing demonstrable high quality patient care.

Just as MIP has important financial implications for hospital operations, the quality of patient care is an important outcome for hospitals (McCullough et al. 2010). Conceptually, quality is an ex post measure of performance of a process, whereas risk is an ex ante measure of its performance. Indeed, a manager uses past quality as a starting point to estimate risk. Similarly, insurers observe past quality of patient care of a hospital and make adjustments to future MIP accordingly (Sloan 1990), just as an automobile insurer uses a driver’s past driving record as a starting point to establish an insurance premium. Current risk levels, in turn, can predict future quality because an organization typically undertakes risk mitigation efforts after risk has been perceived (Sitkin and Pablo 1992), thus reducing errors and enhancing quality. Despite the evidence that current risk affects organizational actions that, in turn, affect future organizational outcomes, few researchers have examined the impact of HIT on future quality of patient care by including MIP or other risk-related variables. Further, empirical evidence of the impact of HIT on hospital-level quality remains equivocal; past studies have found positive and negative relationships and, in some cases, an insignificant relationship (Ammenwert et al. 2008, Jones et al. 2010, McCullough et al. 2010).

The above discussion of the relationships between MIP, HIT, and quality of patient care suggests that these relationships are temporal in nature, i.e., subject to time lags. To account for such temporal effects, we formulate a longitudinal model and test a hypothesis that past HIT expenditure is negatively associated with MIP. We control for past quality of patient care and other variables. We further hypothesize that past MIP and past HIT expenditure together influence current quality of patient care. Finally, we propose that past HIT moderates the relationship between past MIP and current quality of patient care.

To validate our model, we conducted a panel data analysis of an archival data set comprising costs, operations, MIP, and the quality of patient care outcomes from 66 hospitals in the state of Washington from 1998 to 2007. We used readmission rate (a patient admission to the hospital within 30 days of a discharge for the same diagnostic condition) and mortality rate (number of deaths per 1,000 cases) as measures of the quality of patient care. Our findings indicate that past HIT expenditure is associated with lower MIP and readmission and mortality rates. We also find that past MIP is negatively associated with readmission rate, thus supporting our premise that hospitals respond to higher MIP by undertaking risk mitigation efforts that result in lower readmissions. We find that past HIT expenditure positively moderates the relationship between past MIP and current readmission rate. This indicates that the relationship between past MIP and current readmission rate becomes less negative when one takes into account a hospital’s past HIT expenditure.

## 2. Prior Literature

## 2.1. Measurement of IT Value

A rich body of literature has discussed the relationship between IT and organizational performance such as financial outcomes, intermediate process improvements, and system user satisfaction (see Kohli and Devaraj 2003, Melville et al. 2004). Although it is generally accepted that IT creates business value, researchers have argued that the creation of this value is a result of interaction of IT with organizational processes (Barua et al. 1995, Ray et al. 2005). This intermediate-level perspective of business value of IT suggests that IT impact is best assessed at the location in a firm where its first-order effects are expected to be realized (Barua et al. 1995, Ray et al. 2005). This perspective posits that because IT is deployed in support of specific activities, the first-order effect manifests at a process level in an organization. Through conceptual, theoretical, analytical, and empirical studies (Melville et al. 2004), researchers have also identified that IT impacts manifest across a range of granularities, from very detailed process granularities to aggregated firm- or industry-level granularities. Our study is an investigation at an intermediate level of hospitals involving MIP, the quality of patient care, and HIT over a period of time. Prior research has also established that the benefits of IT often accrue over time (Das et al. 2011).

Prior research has also examined expected benefits and costs in anticipation of an IT implementation. For example, financial markets react to announcements of IT implementation in expectation of benefits that could accrue in the future (Subramani and Walden 2001). Although research has found that HIT investments lead to improved quality of services in hospitals (Devaraj and Kohli 2000, Li and Collier 2000) and improved regulatory rankings (Bhattacherjee et al.

2007), previous research has not examined how risk assessment influences hospital quality, nor has it examined the moderating role of HIT on risk-related variables. Prior research has shown that IT has both direct and moderating effects in a firm’s performance outcomes (Mittal and Nault 2009, Ray et al. 2005). Direct effects of IT establish that IT causes changes in firm-level outcomes whereas moderating effects suggest that IT influences firm-level outcomes through its impact on other firm inputs and resources. Such effects are also called augmentation effects because IT augments the efficiency or effectiveness of other organizational inputs (Mittal and Nault 2009). In the next section, we briefly describe the risk construct as used in the management literature and in IS research.

## 2.2. Risk in Management and Information Systems Literatures

The concept of risk in the management literature traces its roots to the seminal work of Knight (1921, p. 233). Risk is a condition in which the consequences of a decision and the probabilities associated with the consequences are known beforehand (Knight 1921, Arrow 1971, Sitkin and Pablo 1992). Management researchers have operationalized risk in terms of the potential occurrence of negative consequences (March and Shapira 1987, Reufli et al. 1999). A negative consequence is a below-target performance, where a target or the acceptable level serves as a reference level (Knight et al. 2001, Reuer and Leiblein 2000). The conceptualization of risk in terms of probability of negative consequences has been useful in the context of operational failures (e.g., Kaplan and Garrick 1981). In hospitals, an operational failure is a negative consequence, such as a need to readmit a patient because of complications. A complication is a deviation from a normal course of postoperative and medical care and refers to the diagnosis of an illness or injury following treatment of a patient for another symptom, illness, or injury (Dindo et al. 2004, Romano et al. 2002).

The relationship between IT and risk in an organization has been expressed from two perspectives in the literature. The first perspective argues that IT implementation carries risk for an organization because of cost overruns and schedule overruns, along with the possibility that the implementation may never be completed. Even when successful, IT implementation can result in varying degrees of benefits. Thus, IT can expose an organization to financial risk. Drawn from financial theory, the risk-return relationship delves into the relationship between investing in high-risk and low-risk projects on the basis that higher returns on investment accrue from riskier projects. Dewan et al. (2007) applied the theory of risk and return to analyze how riskiness of IT investments is rewarded by the stock market. Similarly, Tanriverdi and Ruefli (2004) analyzed the impact of the riskiness of IT on the financial risk and reward of organizations.

The second perspective of the IT-risk relationship is that IT investment reduces various types of organizational risks such as operational risks, market (customer and product) risks, technology risks, and security risks (Clemons et al. 1993, Dewett and Jones 2001). This perspective is similar to the view held by organizational control theorists who view IT as an instrument for facilitating managerial control (Sitkin and Pablo 1992). Researchers have suggested that IT enables better control over processes through its ability to monitor employee behavior (Eisenhardt 1989). An organization’s ability to control business processes reduces risk relating to the performance of those processes. We add to the risk and IT research stream by theorizing that, all else remaining constant, managers will account for the control-enhancing and errorreducing capabilities provided by new IT in order to lower organizational risk. We quantify this impact of IT in the healthcare context with a uniquely constructed data set.

## 2.3. Risk and Insurance

When an organization faces risk from acts of nature, accident, or malice, it takes actions—collectively called self-protection—to reduce risk by protecting itself from or avoiding the sources of risk and losses (Ehrlich and Becker 1972). Because all risks cannot be completely eliminated, firms transfer risks associated with financial liabilities to an insurance company through a contractual mechanism (Dionne and Eeckhoudt 1985). Business disruption insurance, cyber-insurance, and malpractice medical insurance are examples of insurance contracts taken by organizations (Ö ˘güt et al. 2011). When entering into such contracts, insurers take into account protections put in place by the insured organization (e.g., a hospital) and assess the residual risk assumed as a result of the contract (Shavell 1979). For its part, the insured agrees to institute policies and the technological infrastructure to lower the probability and potential impact of a negative outcome.

An insurance contract specifies the insurance premium that is determined by the amount of loss, the probability of loss, and the price of insurance for unit probability and loss (Shavell 1979). In determining an insurance premium, the insurer factors in the degree to which an insured’s behavior can be monitored and the degree to which the circumstances surrounding a loss can be investigated when a negative outcome occurs (Holmström 1979). The insurer also factors in savings in potential monitoring costs to observe the insured during the contractual period to ensure that the insured does not deviate from agreed-upon behavior (Shavell 1979, Boyer and Dionne 1989).

Figure 1 Model Overview  
![](/api/attachments/7CJ3NTN7/fulltext/images/94a8047ec84e09e511720b3929c552a87ecbab37b9ce114f35f1a8d97ad0aca0.jpg)

## 3. Hypotheses Development

Hospitals organize risk management teams, consisting of clinical directors, physicians, nurses, and risk managers, whose role is to estimate probabilities of adverse events, severity of losses, level of monitoring, ease of proving malpractice, and other factors<sup>6</sup> so that team members can agree on an appropriate level of malpractice insurance to cover financial liabilities (Brennan et al. 1996; Carroll 2009; Gawande 2010; Kavaler and Spiegel 2003, p. 3; Morlock and Malitz 1991).<sup>7</sup> The quality of patient care is an important outcome in a hospital (Institute of Medicine 1999) that managers attempt to achieve through automation and control of activities before and during patient care processes. For example, through the use of HIT managers maintain a record of all treatment-related actions and coordinate patient care tasks by better integrating information (Ammenwerth et al. 2008).

The coordination of patient care tasks ensures that activities in interdependent processes, such as handoffs between nursing shifts, are executed smoothly so that errors in medication, diet, and clinical tests are reduced. Similarly, making a patient’s medical history available to clinical teams at the time of diagnosis improves the likelihood of a correct diagnosis (Garcia-Aymerich et al. 2007, Zarling et al. 1999). Thus, the coordination of interdependent processes, enabled by reporting and dissemination capabilities of IT, produces higher quality outcomes (Rockart and Short 1989).

Furthermore, HIT is known to improve quality by alerting clinicians to possible complications following treatments and by tracking a patient’s progress with up-to-date medical records (Bates et al. 2003, Piontek et al. 2010). As a treatment is prescribed or delivered and the data are input to the HIT, potential medication errors can be detected in a timely manner (Chaudhry et al. 2006). A study of a sample of hospitals and clinics found that following the implementation of a HIT, clinicians intercepted nearly 88% of potential errors as compared to only 18.6% when a paper-based system was used (Brown et al. 2004). Finally, because employees are aware that their actions and decisions are electronically recorded and can be scrutinized, they exercise caution during patient care, resulting in improved quality of patient care. Based on the above arguments, our first hypothesis is the following:

<sup>Hypothesis</sup> <sup>1</sup> <sup>(H1).</sup> Past HIT expenditure is positively associated with current quality of patient care.

Our second hypothesis addresses the impact of HIT on MIP (see Figure 1). The MIP that a hospital periodically pays to an insurer depends on the probability of an expected loss amount, the probability of disproving culpability, and the expected size of financial liability from malpractice claim lawsuits (Danzon 1985, Dubay et al. 1999). These probabilities and expected liabilities are imputed from expected levels of errors and failures likely to occur in future operations. If Hypothesis H1 and the surrounding premise are true, then hospitals and insurers can expect that the errorreducing, recordkeeping, and control-enhancing capabilities of the hospital will be enhanced through the new HIT expenditure and that MIP will be lower (Dubay et al. 1999).

Consider the following three explanations of why we propose that past HIT expenditure is associated with lower MIP. First, HIT expenditure signals to insurers a hospital’s due diligence in maintaining reliable patient care records. The availability of HIT provides confidence to an insurer that assessments of malpractice claims risk derived from hospital data records are verifiable. Thus, HIT is associated with lower expected moral hazard costs from an insurer’s perspective because insurers know that actions of hospital personnel are recorded in HIT and can be audited. Second, if and when employee actions introduce risk in the delivery of patient care, both the hospital and the insurer expect that, by using HIT, the hospital will be able to monitor employee behavior and exercise greater control over employees (Mangalmurti et al. 2010). When insurers assess a hospital’s monitoring capabilities as superior, they will assess the probability of loss to be low and will thus lower insurance price, resulting in a lower insurance premium (Ellis and McGuire 1996, Kessler 2011, Sloan 1990). Insurers and hospitals are confident that financial liability from malpractice claims will decline because HIT can detect and provide alerts about clinical errors before they occur.

Finally, hospitals and insurers recognize that HIT will enable quick and accurate diagnosis of patients, even when the disease type and severity of a patient is beyond the hospital’s capability (Gilman 2000).<sup>8</sup> For example, when a seriously ill patient arrives at a hospital’s emergency room, after an initial treatment to stabilize the patient, the hospital can assess the patient based on diagnosis and past medical records available in HIT. It can determine whether the hospital is properly equipped to continue to treat the patient or whether to transfer the patient to an appropriate facility (Metcalfe et al. 1997). Based on the above arguments, we propose that hospitals and insurers will expect that HIT lowers the probability of malpractice claim lawsuits, the probability of losing a lawsuit, and the size of financial liability, thus resulting in lower MIP for hospitals that make an HIT investment. Therefore we hypothesize the following:

<sup>Hypothesis</sup> <sup>2</sup> <sup>(H2).</sup> Past HIT expenditure is negatively associated with MIP.

Our third hypothesis addresses the relationship between past MIP and current quality of patient care (see Figure 2). As part of the insurance contract, hospital administrators commit to taking actions to maintain a high quality of healthcare delivery, for example, by adhering to best practices and by achieving targets for patient care outcomes (Goldschmidt 2005). Hospital administrators also commit to monitoring and maintaining records of healthcare activities. A hospital, like other risk-averse organizations, ensures that the assessed premium remains reasonably priced by taking risk mitigation actions comprising deterrence, prevention, detection, and response (Markus 2000, Straub and Welke 1998). Deterrence actions, which include employee training, environmental scanning, and business process redesign, are proactive and seek to control sources of risk. Prevention and detection efforts are actions undertaken during execution of processes and comprise employee supervision and process monitoring. In healthcare, deterrence and prevention actions are generally expressed as clinical vigilance. Specifically, clinical vigilance implies systematic and organized information search and thorough consideration of available alternatives for ensuring patient safety and health (Studdert et al. 2004, Towse and Danzon 1999).

Previous studies in clinical practice have also found that clinicians practice defensive medicine in order to reduce the risk of malpractice lawsuits (Studdert et al. 2004). Defensive medicine is defined as conducting additional tests and procedures in order to avoid malpractice claims that may result from a missed diagnosis (Kessler 2011). When clinicians practice defensive medicine, a patient is discharged only when clinicians are certain that the tests and treatments were thorough. As a result, readmissions and mortality rates are likely to decrease. Thus, in addition to clinical vigilance, defensive medicine may contribute to lower readmission and lower mortality rates resulting in higher quality of patient care. Based on the above arguments, we posit the following:<sup>9</sup>

<sup>Hypothesis</sup> <sup>3</sup> <sup>(H3).</sup> Past MIP is positively associated with quality of patient care.

To understand the moderating role of past HIT expenditure on the relationship between past MIP and the quality of patient care, consider a counterargument that can be made against Hypothesis H3: (i) the literature on economics of insurance argues that, regardless of the ex ante commitments made by the insured, the ex post behavior of the insured will not completely reflect those ex ante commitments (Shavell 1979, Dionne and Eeckhoudt 1985), and (ii) the insured party is the hospital, and physicians, who are often external “contractors” who practice at more than one hospital, are unlikely to adhere to, or be bound by, the commitments made by the hospital to control malpractice and improve quality. This counterargument is less likely to hold in the HIT context because HIT can force a hospital to follow agreed-upon service-delivery commitments corresponding to risk levels dictated in the contract with the insurer. HIT’s recordkeeping and monitoring capabilities also induce employees and physicians to align their behavior with service delivery prescribed by the hospital’s risk mitigation efforts. This inducement of sincerity in risk mitigation and clinical vigilance actions to maintain MIP will collectively result in higher quality.<sup>10</sup> Mittal and Nault (2009) explain that when IT enhances the efficiency or effectiveness of organizational actions or resources, it plays a moderating role. Here HIT is playing a moderating role in actions that follow MIP. In other words, the relationship between past MIP and quality of patient care is enhanced by the past HIT expenditure. Thus, we propose:

<sup>Hypothesis</sup> <sup>4</sup> <sup>(H4).</sup> The relationship between past MIP and quality of patient care is enhanced (positively moderated) by past HIT expenditure.

Figure 2 Hypothesized Relationships  
![](/api/attachments/7CJ3NTN7/fulltext/images/d65aab2317b75c12e0e4b379fc9a1b5ac6fb2281308a0fef3e46bf3ebc806961.jpg)  
Note. Remaining relationships, e.g., quality of patient care at time t − 1 to MIP in time t and other control variables, are not shown here but are depicted in the empirical model after data description.

## 4. Empirical Execution

Data for hospital spending were gathered from the Washington State Department of Health and span the period 1998 to 2007 for 66 general medical and surgical hospitals. We chose medical and surgical hospitals because they operate a broad range of specialties rather than one specialty or patient type, such as psychiatric hospitals or children’s hospitals. A single state, Washington in our case, as the source of data enables us to study hospitals that are subject to the same regulatory environment. Thus, we mitigate heterogeneity among hospitals that may result from narrow focus on patient care or differences in regulations, accounting practices, and other regional and environmental dissimilarities.

A second source for our data is a proprietary commercial database marketed to hospitals by Comparion Medical Analytics (formerly known as The Delta Group), a data services and consulting company,<sup>11</sup> that consists of estimates of the quality of patient care outcomes for each hospital for each year (DesHarnais et al. 2000). The outcomes data include estimated readmission rates and mortality rates. Estimates of readmissions for a hospital are typically calculated within a diagnostically related group (DRG), and estimates of the number of patients that are expected in each DRG are based upon national hospital records (Vincent 1997, Zhan and Miller 2003). Comparion Medical Analytics analyzes more than 25 million records each year pertaining to patient discharges from hospitals across the United States to arrive at estimates of readmissions and mortality rates for each disease category for various severity levels (Forthman et al. 2010). The records also contain patient demographics (e.g., age and gender) and clinical characteristics (e.g., chronic conditions and comorbidities). Comparion Medical Analytics data also provided us with actual readmissions and mortality rates for each hospital for previous years.<sup>12</sup> After matching hospitals in the state of Washington with those in Comparion Medical Analytics’ data set using the hospital’s unique Medicare identification number, name, address, and year, we constructed a comprehensive data set to test our hypotheses.

## 4.1. HIT Data Description

The Washington state hospital data are organized by accounts: revenue accounts, ancillary accounts, and cost accounts. Each account in a hospital consists of salaries, benefits, professional fees, and depreciation expenses. We extract HIT spending from depreciation expenses of cost accounts with a high concentration of information processing activities following a methodology deployed by prior works in HIT (Ko and Osei-Bryson 2004, Menon et al. 2009). HIT-relevant accounts are data processing, personnel, purchasing, communication, accounting, utilization management, hospital administration, in-patient admitting, patient medical records, and pharmacy.<sup>13</sup> These accounts subsume information processing activities, so the depreciation expense in these cost accounts is primarily related to IT (Menon et al. 2009). The inclusion of expenses from these accounts in HIT is a superior alternative to exclusive use of data processing expense account for HIT because this single account does not provide a full representation of HIT spending. For example, information processing expenses for billing and cost accounting, such as computing equipment, cost accounting software, and data storage assets, are likely to appear as accounting department expenses in the ledger rather than as data processing expenses of the IT department. This is especially the case in organizations in which expenses for hardware, software, and networks are charged to the department that requests information-related services, even though the IT department manages the implementation and maintenance of assets after they have been acquired.

The inclusion of accounts other than the data processing account in our proxy for HIT is in line with accounting literature that has argued in favor of tracing expenses based on the types of activities rather than simply tracking expense by one traditional department (Cleverley 1989, p. 101). Indeed, the widespread use of Activity Based Costing is attributed to overcoming such anomalies that otherwise understate expenses by focusing on individual functional areas.<sup>14</sup> Similarly, McKay et al. (1998) argued that the aim of creating cost centers, such as central supply administration, data processing, accounting, and pharmacy administration, is to exercise managerial control and has pooled costs from these costs centers as administrative costs. In our data, we are able to separate capital costs from labor costs for these cost centers and use the former as a proxy for HIT.

In order to account for differences due to hospital size, we divided the aggregate HIT expense by adjusted patient days (Cuellar and Gertler 2006). “Adjusted patient days” consists of both inpatient and outpatient volumes and is obtained by converting outpatient visits to patient days based on the ratio of outpatient charges to inpatient charges and by adding to inpatient days.

## 4.2. Actual (and Estimated) Readmission and Mortality Rates, and Insurance Premium

We measure quality of patient care with two variables: actual readmissions (Readm\_Actual) and actual mortality (Mort\_Actual). We obtained data for actual readmission (READM\_Actual) and mortality (MORT\_Actual) rates for each year for each hospital from Comparion Medical Analytics data. These rates are based on per-1,000 cases. The Washington state hospital data contain the annual malpractice insurance premium (MIP) paid by each hospital. We divided this variable by adjusted patient days to control for hospital size. Our data set contained case-mix index (Case\_Mix) for each hospital-year observation for use as a control variable. Case-mix index is a standard weighted measure of the diversity in the medical severity of cases of a hospital and is defined as a hospital-level metric to address the question “How sick (resource intensive) are my patients?” (Wang et al. 2001, Horn et al. 1991, Shukla and Pestian 1997). Because use of hospital resources is correlated with the severity of patients’ illnesses, case-mix is commonly used as a control variable for hospital performance. Similarly, as argued earlier regarding the use of estimates of probabilities of readmissions in determining insurance prices, we obtained data for estimated readmission (READM\_Estimate) and mortality (MORT\_Estimate) for each year for each hospital from Comparion Medical Analytics data. These rates are also per-1,000 cases.

We aggregated salaries, benefits, and professional fees in medical-related cost accounts to arrive at a proxy for medical salary (MED\_Salary). These data were divided by the employment cost index for healthcare services provided at the Bureau of Labor Statistics and were then divided by patient days to adjust for hospital size.<sup>15</sup> Further, we aggregated the depreciation expenses in revenue and ancillary accounts that are primarily clinical to arrive at a proxy for medical capital spending (MED\_Capital). These data were first divided by the producer price index for medical equipment and supplies manufacturing from the Bureau of Labor Statistics to reflect changing prices for medical equipment over time and were then divided by patient days of the hospital to control for size. In Table 1, we list our variables, their definitions, and references to previous work. In Table $^ { 2 , }$ we provide the mean and standard deviation of each variable as well as the correlation between the variables. In all, the final data contains 660 hospital-year observations resulting from 66 hospitals over 10 years.

## 4.3. Empirical Model and Analysis

To test the above hypotheses, we set up three regression models. We first set up the regression model for the dependent variable, Readm\_Actual, in Equation (1). A negative coefficient for $H I T _ { i t }$ in the estimated model will validate Hypothesis H1.

$$
\begin{array}{r l} \text {Readm\_Actual} _ {i t} & = c _ {0} + c _ {1} H I T _ {i, t - 1} + c _ {2} M I P _ {i, t - 1} + c _ {3} (H I T _ {i, t - 1} \times M I P _ {i, t - 1}) \\ & + c _ {4} \text {Med\_Salary} _ {i, t - 1} + c _ {5} \text {Med\_Capital} _ {i, t - 1} \\ & + c _ {6} \text {Case\_Mix} _ {i, t - 1} + c _ {7} \text {Readm\_Actual} _ {i, t - 1} + \varepsilon_ {i t}. \end{array} \tag {1}
$$

The parameters $c _ { 0 }$ to $c _ { 7 }$ are to be estimated. The subscripts i and t index the hospital and the year, respectively. In the above model, note the following: (1) the HIT and other explanatory variables are lagged by one year, denoted by subscript t −1, to ensure that causality can be inferred;<sup>16</sup> (2) the interaction between MIP and HIT is included to test for moderating effects in Hypothesis H4; (3) we added MED\_Salary and Med\_Capital in the model to control for hospitalspecific medical and clinical capabilities; and (4) we added the lag of dependent variable readmission actual $( R e a d m \_ A c t u a l _ { i , t - 1 } )$ to control for the likely persistence in organizational decisions and actions from year to year. The correlation of a dependent variable with its past value can lead to serial correlation among error terms, which violates an assumption of ordinary least squares. $c _ { 0 }$ is the intercept term in the equation. The unobserved parameter $\varepsilon _ { i t }$ captures three types of errors: first, it contains hospitalspecific factors that vary across hospitals, but do not vary over time. Examples of such factors are teaching status, location (rural or urban), and profit status. Second, it contains time-specific factors that are relatively constant across hospitals in a year. This includes macroeconomic conditions and technology changes in medical practice. Third, it contains other unobserved shocks that are randomly distributed over hospitals and years. This type of error is typically modeled as a random variable with a normal distribution and is assumed to be uncorrelated with the independent variables.

To address the first type of error, the hospitalspecific factors, we generate a first-differenced model by subtracting Equation (1) at time t −1 from Equation (1) at time $t ,$ yielding

$$
\begin{array}{l} \Delta \text {Readm\_Actual} _ {i t} \\ = c _ {0} ^ {\prime} + c _ {1} \Delta H I T _ {i, t - 1} + c _ {2} \Delta M I P _ {i, t - 1} \\ \quad + c _ {3} \Delta (H I T _ {i, t - 1} \times M I P _ {i, t - 1}) + c _ {4} \Delta \text {Med\_Salary} _ {i, t -} \\ \quad + c _ {5} \Delta \text {Med\_Capital} _ {i, t - 1} + c _ {6} \Delta \text {Case\_Mix} _ {i, t - 1} \\ \quad + c _ {7} \Delta \text {Readm\_Actual} _ {i, t - 1} + \varepsilon_ {i t} ^ {\prime}. \end{array} \tag {2}\tag{2}
$$

Where $\Delta H I T _ { i , t - 1 } { = } H I T _ { i , t - 1 } { - } H I T _ { i , t - 2 } ,$ etc. All hospitalspecific effects in the variables and in the error term that are time-invariant cancel out. Though the original intercept term $c _ { 0 }$ also drops out because of first-differencing, we added an intercept term, $c _ { 0 } ^ { \prime } ,$ to capture any constant effect over time in the firstdifferenced model.

In addition to reducing hospital-specific and timespecific errors, the first differenced model has an advantage of overcoming the confounding issue in panel models, such as ours, in that organizational factors unobserved by researchers can influence the independent and dependent variables (Greene 2003). In our case, capital and labor, as well as the risk of a hospital, are influenced by organizational and environmental factors. Although first-differencing can account for hospital-specific and time-specific confounding factors, factors external to the hospital, such as epidemiological status of the population, also impact the independent and dependent variables and have not been completely addressed by firstdifferencing. The impacts of these factors are likely to vary by hospital and year, and because the same underlying factors affect both dependent and independent variables and are omitted from the model, correlation between the error term and the independent variables must be modeled to be nonzero.

Table 1 Definitions and Sources of Variables

<table><tr><td>Measure (variable name)</td><td>Definition</td><td>Data source</td><td>References in literature</td></tr><tr><td>Healthcare information technology expenditure (HIT)</td><td>Depreciation expenses pooled from data processing, personnel, purchasing, communication, accounting, utilization management, hospital administration, patient admitting, patient medical records, and pharmacy, deflated by producer price index and adjusted for hospital size</td><td>Washington State Department of Health</td><td>Bhattacherjee et al. (2007), Menon et al. (2009)</td></tr><tr><td>Case mix (Case_Mix)</td><td>Diagnosis-based relative weighted measure of the severity of illnesses of patients</td><td>Washington State Department of Health</td><td>Wang et al. (2001), Horn et al. (1991), Shukla and Pestian (1997)</td></tr><tr><td>MIP (MIP)</td><td>Annual premium amount divided by patient days</td><td>Washington State Department of Health</td><td>Reynolds et al. (1987)</td></tr><tr><td>Medical salaries (MED_Salary)</td><td>Salaries pooled from medical accounts deflated by the employment cost index and adjusted for hospital size</td><td>Washington State Department of Health</td><td>Ko and Osei-Bryson (2004), Menon et al. (2000)</td></tr><tr><td>Medical capital (MED_Capital)</td><td>Depreciation expenses pooled from medical accounts deflated by producer price index and adjusted for hospital size</td><td>Washington State Department of Health</td><td></td></tr><tr><td>Actual readmission rate (Readm_Actual)</td><td>Actual number of readmissions for 1,000 cases</td><td>Comparison Medical Analytics</td><td></td></tr><tr><td>Estimated readmission rate (Readm_Estimate)</td><td>Expected number of readmissions for 1,000 cases</td><td>Comparison Medical Analytics</td><td>Shur and Simons (2008)</td></tr><tr><td>Actual mortality rate (Mort_Actual)</td><td>Actual number of mortalities for 1,000 cases</td><td>Comparison Medical Analytics</td><td></td></tr><tr><td>Estimated mortality rate (Mort_Estimate)</td><td>Expected number of mortalities for 1,000 cases</td><td>Comparison Medical Analytics</td><td></td></tr></table>

Table 2 Descriptive Statistics for Model Variables

<table><tr><td rowspan="2">Variable</td><td rowspan="2">N</td><td rowspan="2">Mean</td><td rowspan="2">Std. dev.</td><td colspan="8">Correlation matrix (correlations significant at p&lt;0.05 in boldface)</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td><td>(8)</td></tr><tr><td>(1) HIT</td><td>660</td><td>0.29</td><td>0.30</td><td>1.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(2) MIP</td><td>660</td><td>23.07</td><td>19.39</td><td>0.09</td><td>1.0</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(3) Readm_Estimate</td><td>660</td><td>21.20</td><td>10.56</td><td>0.06</td><td>-0.39</td><td>1.0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(4) Mort_Estimate</td><td>660</td><td>4.99</td><td>1.04</td><td>0.11</td><td>-0.27</td><td>0.44</td><td>1.0</td><td></td><td></td><td></td><td></td></tr><tr><td>(5) Readm_Actual</td><td>660</td><td>22.86</td><td>13.90</td><td>-0.03</td><td>-0.37</td><td>0.70</td><td>0.34</td><td>1.0</td><td></td><td></td><td></td></tr><tr><td>(6) Mort_Actual</td><td>660</td><td>4.67</td><td>1.49</td><td>0.05</td><td>-0.19</td><td>0.26</td><td>0.49</td><td>0.22</td><td>1.0</td><td></td><td></td></tr><tr><td>(7) MED_Salary</td><td>660</td><td>4.33</td><td>2.40</td><td>0.35</td><td>-0.22</td><td>0.38</td><td>0.30</td><td>0.16</td><td>0.17</td><td>1.0</td><td></td></tr><tr><td>(8) MED_Capital</td><td>660</td><td>0.75</td><td>0.48</td><td>0.32</td><td>-0.21</td><td>0.35</td><td>0.27</td><td>0.13</td><td>0.16</td><td>0.87</td><td>1.0</td></tr><tr><td>(9) Case_Mix</td><td>660</td><td>0.89</td><td>0.24</td><td>0.17</td><td>-0.06</td><td>0.04</td><td>-0.04</td><td>-0.01</td><td>0.08</td><td>0.33</td><td>0.31</td></tr></table>

A suitable approach to overcoming the presence of nonzero correlation between independent variables and the error term is to perform least squares regression of the dependent variable on predicted values of the independent variables with the assumption that the correlation between the predicted values of the independent variables and the error term is zero (therefore, the correlation between the actual values of the independent variable and the error term is nonzero). The predicted values are computed by the regression of the independent variables on “instrumental” variables that are correlated with the independent variables but are not correlated with the error terms. In panel data, such instrumental variables are difficult to find because time-related shocks pervade during the data generation of independent and exogenous variables. But in the case of first-differenced models, the lags of the first-differences of the variables in the model have been shown to be good instruments (Arellano and Bond 1991, Ahn and Schmidt 1995, Blundell and Bond 1998). Particularly, deep (e.g., fourth, fifth) lags of the first-differenced dependent variable are suitable (Roodman 2009). The first-differenced model is estimated using the generalized method of moments (GMM) so that moment restrictions can be imposed during estimation based on the nature of the instrumental variables.<sup>17</sup>

We obtained county-level annual average monthly earnings, annual birthrate, and annual injury-rate from the Washington state census and population estimates and deployed them as exogenous instruments. These exogenous variables vary by time and location of the hospital and thus capture environmental conditions surrounding the hospital. We further used an analysis option in the estimation procedure to correct for heteroscedastic error terms.

The remaining models were set up after firstdifferencing in a similar fashion: Equation (3) is the first-differenced model for actual mortality, Mort\_Actual, the second dependent variable for quality of patient care.

$$
\begin{array}{l} \Delta M o r t \_ A c t u a l _ {i t} \\ = d _ {0} ^ {\prime} + d _ {1} \Delta H I T _ {i, t - 1} + d _ {2} \Delta M I P _ {i, t - 1} \\ \quad + d _ {3} \Delta (H I T _ {i, t - 1} \times M I P _ {i, t - 1}) + d _ {4} \Delta M e d \_ S a l a r y _ {i, t - 1} \\ \quad + d _ {5} \Delta M e d \_ C a p i t a l _ {i, t - 1} + d _ {6} \Delta C a s e \_ M i x _ {i, t - 1} \\ \quad + d _ {7} \Delta M o r t \_ A c t u a l _ {i, t - 1} + \varepsilon_ {i t} ^ {\prime \prime}. \end{array}\tag{3}
$$

To test Hypothesis H2, we set up a model with MIP as the dependent variable and HIT as an independent variable. As before, our measures for the independent variables are lagged by one year to ensure that timing of the variables is clearly separable. We added the estimates of readmission rate and mortality rate in the model to capture the impact of these estimates on MIP. In addition to these variables, we also added the actual readmissions and mortality of the hospital. Because we included the Readm\_Estimate and Mort\_Estimate using their one year lag, we included the Readm\_Actual and Mort\_Actual using their twoyear lag, to ensure that the variables are separable over time. The full model, in its first-differenced form, is as follows:

$$
\begin{array}{r l} & {\Delta P r e m i u m _ {i t}} \\ & {\quad = b _ {0} ^ {\prime} + b _ {1} \Delta H I T _ {i, t - 1} + b _ {2} \Delta R e a d m \_ E s t i m a t e _ {i, t - 1}} \end{array}
$$

<sup>17</sup> It is generally difficult to find suitable instruments in panel data because of time and cross-section effects. Suitable instruments are those that are not correlated with the error term and so are exogenous but are correlated with the endogenous variables. The norm in literature is to find instruments and then specify whether they are correlated or not, so appropriate moment restrictions can be applied during estimation (Blundell and Bond 1998). We used four variables that are correlated with the hospital-specific effects and are exogenous: case-mix, county-specific average monthly earnings, birth rates, and injury rates. We specified that these instrumental variables are correlated with the hospital-specific effects so the statistical package applies the appropriate moment restrictions.

$$
\begin{array}{l} + b _ {3} \Delta \text {Mort\_Estimate} _ {t, t - 1} + b _ {4} \Delta \text {Readm\_Actual} _ {i, t - 2} \\ + b _ {5} \Delta \text {Mort\_Actual} _ {i, t - 2} + b _ {6} \Delta \text {Med\_Salary} _ {i, t - 1} \\ + b _ {7} \Delta \text {Med\_Capital} _ {i, t - 1} + b _ {8} \Delta \text {Case\_Mix} _ {i, t - 1} \\ + b _ {9} \Delta \text {Premium} _ {i, t - 1} + \varepsilon_ {i t} ^ {\prime \prime \prime}. \end{array} \tag {4}
$$

## 4.4. Results

The results for the GMM analysis using a dynamic panel approach are reported in Tables 3 and 4. The results for the models for actual readmission rate and actual mortality rate are in Table 3. Given that the coefficient estimate of past HIT is negative for both dependent variables, we conclude that past HIT is associated with lower current readmission rate as well as lower current mortality rate. Thus, Hypothesis H1 is supported for both outcome variables. Similarly, the estimate of the coefficient of MIP is negative in both models, thus supporting Hypothesis H3.

The moderating impact of HIT on the relationship between MIP and quality of patient care differs for the two measures of quality. In the case of readmission rate, the estimate of the coefficient of $M I P _ { i , t - 1 } \times$ ${ H I T } _ { i , t - 1 }$ is positive and significant. This is contrary to the effect hypothesized in H4. In the case of mortality rate, the estimate of this coefficient is not significant. We discuss possible explanations for these findings in the next section.

Among the control variables, all estimates are in the directions that we expected. The coefficient estimate for Case $\_ M i x _ { i t }$ is positive, indicating that higher severity of illnesses is associated with higher readmissions and mortality rates. Medical salary is positively associated with readmission rate and mortality rate. This does not mean that the medical staff causes readmission and mortality. This simply suggests that, because higher salaries are indicative of high-risk specialties in hospitals, such hospitals experience higher levels of readmissions and mortality. The estimate of the coefficient of medical capital is negative, indicating the therapeutic and diagnostic impact of medical equipment on readmissions and mortality rates. The two statistics used for model specification are root mean square error (RMSE), and the Sargan’s test (Blundell and Bond 1998). RMSE for the model for actual readmission rate is 18.1, which is the lowest for different specifications that we tested.<sup>18</sup> The Sargan test yielded a test-statistic of 106.7 (degrees of freedom = 118), a p-value of 0.77, providing confirmation that the model is not overidentified. Similarly, the model for the actual mortality rate is not overidentified.

Table 3 Dynamic Panel Analysis of Actual Readmission and Mortality Rate

<table><tr><td rowspan="2">Variable</td><td colspan="2">Actual readmission rate (Readm_Actualit)</td><td colspan="2">Actual mortality rate (Mort_Actualit)</td></tr><tr><td>Coeff. estimate</td><td>(Std. err.)</td><td>Coeff. estimate</td><td>(Std. err.)</td></tr><tr><td>Intercept</td><td>0.160</td><td>(0.14)</td><td>0.103</td><td>(0.02)***</td></tr><tr><td>HITi,t-1</td><td>-33.649</td><td>(4.2)***</td><td>-4.166</td><td>(0.49)***</td></tr><tr><td>MIPi,t-1</td><td>-0.927</td><td>(0.06)***</td><td>-0.027</td><td>(0.006)***</td></tr><tr><td>MIPi,t-1×HITi,t-1</td><td>1.279</td><td>(0.16)***</td><td>0.020</td><td>(0.013)</td></tr><tr><td>MED_Salaryi,t-1</td><td>10.742</td><td>(0.57)***</td><td>0.625</td><td>(0.05)***</td></tr><tr><td>MED_Capitali,t-1</td><td>-48.111</td><td>(2.1)***</td><td>-1.268</td><td>(0.22)***</td></tr><tr><td>Case_Mixi,t-1</td><td>31.896</td><td>(2.4)***</td><td>3.277</td><td>(0.25)***</td></tr><tr><td>Readm_Actuali,t-1</td><td>0.220</td><td>(0.01)***</td><td>—</td><td>—</td></tr><tr><td>Mort_Actuali,t-1</td><td>—</td><td>—</td><td>0.256</td><td>(0.02)***</td></tr><tr><td>Root mean square error</td><td></td><td>18.1</td><td></td><td>1.64</td></tr><tr><td rowspan="2">Sargan&#x27;s test statistic(degrees of freedom)†</td><td></td><td>106.7</td><td></td><td>116.0</td></tr><tr><td></td><td>(118)</td><td></td><td>(138)</td></tr><tr><td>p-value for Sargan&#x27;s test††</td><td></td><td>0.77</td><td></td><td>0.91</td></tr></table>

<sup>†</sup>Degrees of freedom differ across models because different numbers of lags of instrument variables were used to obtain insignificant p-value on Sargan’s test.  
<sup>††</sup>An insignificant p-value for Sargan’s test indicates that the instruments are appropriate, so the model has a good fit. $^ { * * * } p < 0 . 0 0 1 .$

Table 4 provides the estimates of coefficients and model fit results for the model with MIP as the dependent variable. The result for $M I P _ { i t }$ indicates that the estimate of coefficient of ${ H I T } _ { i , t - 1 }$ is negative and significant at 5% p-value (Table 4). Thus, Hypothesis H2 is supported. The coefficient of Readm\_ $\mathrm { E s t i m a t e } _ { i , t - 1 }$ is negative and significant, indicating that as a hospital’s estimate of readmission rate increases, its MIP decreases. This is likely because insurers may raise the price of malpractice insurance. But if the hospital is paying lower MIP, it means that the loss amount that is insured was lowered. The positive sign for the coefficient of Mort\_Estima $\ t e _ { i , t - 1 }$ indicates that MIP increases with estimated mortality. Unlike the estimate of readmissions, even as the price of malpractice insurance is raised with estimates of higher mortality rates, the net effect is a higher premium, which means the loss amount is not lowered. A similar effect is seen with Readm\_ $. A c t u a l _ { i , t - 2 } .$ . However, the coefficient of $M o r t \_ A c t u a l _ { i , t - 2 }$ is not significant, implying that past mortality rate does not affect MIP.

Among the remaining control variables, the coefficient of $\Breve { } { M } E D \_ C a p i t a l _ { i t }$ is negative, whereas those of $M I P _ { i , t - 1 }$ and $M E D \_ S a l a r y _ { i t }$ are positive. RMSE for the model is 15.7, which is the lowest for the different specifications that we tested. The Sargan test yielded a test-statistic of 111.9 (degrees of freedom = 118), a p-value 0.64, confirming that the model is not overidentified.

Using the results in Table 3, we can determine the net impact from direct and moderating impacts of

Table 4 Malpractice Insurance Premium $( M I P _ { i t } )$

<table><tr><td>Parameter</td><td>Estimate</td><td>(Std. err.)</td></tr><tr><td>Intercept</td><td>3.642</td><td>(0.79)***</td></tr><tr><td> $HIT_{i,t-1}$ </td><td>-44.178</td><td>(22.7)*</td></tr><tr><td> $Readm\_Estimate_{i,t-1}$ </td><td>-0.257</td><td>(0.12)*</td></tr><tr><td> $Mort\_Estimate_{i,t-1}$ </td><td>11.083</td><td>(4.45)*</td></tr><tr><td> $Readm\_Actual_{i,t-2}$ </td><td>0.216</td><td>(0.09)*</td></tr><tr><td> $Mort\_Actual_{i,t-2}$ </td><td>-0.074</td><td>(0.53)</td></tr><tr><td> $MED\_Salary_{i,t-1}$ </td><td>9.376</td><td>(4.1)*</td></tr><tr><td> $MED\_Capital_{i,t-1}$ </td><td>-40.504</td><td>(17.2)*</td></tr><tr><td> $Case\_Mix_{i,t-1}$ </td><td>-13.172</td><td>(67.9)*</td></tr><tr><td> $MIP_{i,t-1}$ </td><td>0.163</td><td>(0.07)*</td></tr><tr><td>Root mean square error</td><td></td><td>15.7</td></tr><tr><td>Sargan&#x27;s test statistic(degrees of freedom) $^{\dagger}$ </td><td></td><td>111.9</td></tr><tr><td>p-value for Sargan&#x27;s test $^{\dagger\dagger}$ </td><td></td><td>(118)</td></tr><tr><td></td><td></td><td>0.64</td></tr></table>

<sup>†</sup>Degrees of freedom differ across models because we used different number of lags of instrument variables to obtain insignificant p-value on Sargan’s test.  
<sup>††</sup>An insignificant p-value for Sargan’s test indicates that the instruments are appropriate, so the model has a good fit.  
<sup>∗</sup>p <0005; <sup>∗∗∗</sup>p <00001.

HIT on readmissions by differentiating Equation (2) with respect to $H I T _ { t - 1 } \ ( \bar { M } I P _ { t - 1 }$ is a function of $H I T _ { t - 2 }$ but is independent of $H I T _ { t - 1 } ,$ so we do not differentiate it with respect to $H I T _ { t - 1 } )$ , obtaining

$$
\frac {\partial (R e a d m \_ A c t u a l _ {t})}{\partial (H I T _ {t - 1})} = d _ {1} + d _ {3} M I P _ {t - 1}.
$$

Computing the average of the right side of the above equation provides the impact of a unit spending of HIT on readmissions. We find that HIT has a total unit impact of −90606 on readmissions when evaluated at the mean value of MIP in the above equation. Similarly, the net impact of HIT on mortality is −3.77 at the mean value of MIP. We plotted a graph of readmissions versus HIT for three levels of MIP to illustrate that the slope of readmissions gets less steep as MIP increases (Figure 3).

Figure 3 Graph of Readmissions Rate vs. Past HIT per Adjusted Patient Days  
![](/api/attachments/7CJ3NTN7/fulltext/images/ddd3f1380c0255f4ee529c0659e00df9a6932459c2900b07c1073f343fdde87c.jpg)

## 5. Discussion

By examining hospitals’ IT spending and performance, we found evidence of a direct impact of HIT on MIP as well as on the quality of patient care (Figure 4). The evidence of lower readmissions and mortalities in association with past HIT expenditure validates Hypothesis H1 regarding the direction of impact of HIT on quality of patient care. The hypothesis was supported by the argument that IT is able to provide appropriate alerts during patient care. Readily available patient information facilitates good quality medical care, and coordination between staff members administering medical care is facilitated by HIT, leading to fewer errors in patient care. Although this result is consistent with conclusions in prior studies (e.g., Ammenwert et al. 2008), the significance of the coefficients of past MIP in both models of patient care quality indicates that prior research had not satisfactorily accounted for ex ante risk. Thus, Hypothesis H3 contributes to healthcare literature by providing an explanation for the inconsistency among the findings of prior research.

We had hypothesized that past HIT expenditure is negatively associated with MIP (Hypothesis H2) and argued that hospitals and insurers would anticipate fewer errors after spending for HIT. This hypothesis is validated; insurers account for expected benefits from HIT in patient care when assessing risk of a hospital. These expected benefits may include management of risk by admitting patients with severity levels commensurate with the capabilities of the hospital; lower the probability of errors by effective coordination and tracking; raise the probability of proving due diligence by a hospital in malpractice litigation;

Figure 4 Results for the Hypothesized Relationships (See Tables 3 and 4 for the Results for the Control Variables)  
![](/api/attachments/7CJ3NTN7/fulltext/images/858ebe1fac379543e5dbb5b4fedaab630964bfe7069303f0b9517e474ae16e41.jpg)  
<sup>∗</sup>p <0005; <sup>∗∗∗</sup>p <00001.

and lower financial liability, even in lawsuits where a court awards penalties against the hospital.

In addition to the impact of past HIT expenditure on quality of patient care, we found a moderating impact of this HIT on quality of patient care through its impact on the link from past MIP to quality of patient care. However, the direction of this relationship (the sign of the coefficient of the interaction) is negative, contrary to Hypothesis H4. The premise for Hypothesis H4 was that after MIP is determined, the hospital will undertake risk mitigating actions and HIT will support these actions to make them effective. In view of the negative interaction result, we surmise that actions that follow MIP are less effective in improving the quality of patient care when HIT is increased. We surmise that HIT spending “crowded” traditional and nonautomated risk mitigation actions, thus indirectly decreasing the quality of patient care. Further, staff members may be relying on HIT for “automated vigilance” to such an extent that traditional non-HIT-based risk-mitigation actions have received less attention. Indeed, there is evidence that despite hospital investments in risk mitigation, there was an increase in readmissions (Friedman et al. 2009). These findings offer opportunities for further research.

## 5.1. Contributions

This study contributes to the business value of IT and HIT literature in a number of ways. First, a theoretical contribution is the surfacing of and our understanding of the expectation of IT benefits and its effect on an organization. We contribute by conceptualizing the impact of HIT on ex ante malpractice claims risk as an expectation, on the part of hospitals and insurers, of the impact of HIT on future operations. Second, the moderating effect of IT of a risk-related organizational variable on an organizational outcome emerges as a theoretical contribution. Third, our longitudinal models that incorporate moderating effects of HIT and include MIP as an antecedent factor for quality of patient care contribute to expounding the complex, temporal relationship between HIT and quality of patient care. Previous studies on the relationship between HIT and quality of patient care have shown mixed results (Culler et al. 2007, Garcia-Aymerich et al. 2007).

For practitioners, our study informs decision makers in risk, quality management, and the IT function to engage in joint risk mitigation decisions to achieve desired organizational goals. Managers must be aware of the possibility that staff may excessively rely on IT to the detriment of patients. Our findings imply that hospital managers must also keep third parties, such as insurers, well informed about some of their IT investments because this is likely to lead to favorable MIP rates in the future. Finally, our study also has implications for healthcare policy makers. Policy makers must account for the financial benefits from lower MIP when evaluating the business case and for allocating HIT funding.

## 5.2. Limitations and Future Research

Despite the uniquely constructed longitudinal data set and the rigorous analysis, our research is subject to limitations. First, our measure for HIT is an approximation based on the aggregation of depreciation expenses across information processing units. Though this approach is based upon contemporary thinking in cost accounting, more precise measures would further refine the HIT measure. In the same vein, because of the absence of detailed HIT-related investments, we were unable to explore the influence of specific application software on MIP. Another limitation of our study is that use of HIT in hospitals is likely to vary from HIT expenditures, which in turn could affect the relationship between HIT, risk, and quality. Future studies must delve into applicationlevel and clinical process-level usage of HIT using our analytical models. A third limitation of our research, as is common with archival data-based research, is that we do not know if all hospitals in all years made decisions in the sequence we have postulated (i.e., estimate readmission rates, invest in HIT, purchase malpractice insurance, perform actions, and observe readmission rates). Future studies may capture the sequence of risk management activities among hospitals as well as IT applications (e.g., Angst et al. 2011) and supplement data with other process-level measures and mediating variables that reflect hospitals risk behavior and outcomes.

## 6. Conclusions

Our objective in this paper was to investigate (1) whether past HIT expenditure affects MIP and the quality of patient care and (2) whether this expenditure moderates the relationship between past MIP and the quality of patient care. We developed a longitudinal model for this purpose. Our data set contained both estimated readmission and mortality, actual readmission and mortality, MIP, and HIT spending for 66 hospitals for each year for a 10-year period from 1998 to 2007. We used a GMM-based dynamic panel method with lags of dependent variable as instruments to account for endogeneity of the independent variables. Our empirical findings validate that past HIT expenditure improves the quality of patient care and that it is negatively associated with current MIP. We found a negative moderating relationship of past HIT expenditure on the link between past MIP and current quality of patient care. Our findings may have implications for researchers in the business value of IT who study the impact of IT on risk, on the relationship between intermediate risk-related variables and intermediate outcomes, and the notion of IT impact expected by external agents. Similarly, healthcare IT researchers, who study HIT’s impact on malpractice claims risk and the quality of patient care, will benefit from our findings pertaining to HIT and MIP. Finally, we anticipate that these findings will provide managers and healthcare policy makers with insights into the interplay between HIT, malpractice claims risk, and the quality of patient care.

## Acknowledgments

The authors are grateful for the comments from Maryam Alavi, Jon Beard, Carol Brown, Siddharta Das, Gordon Gao, Anant Mishra, Sunil Mithas, Pankaj Setia, Ranjani Krishnan and Chen Zhang. Previous versions of this paper benefitted from comments by seminar participants at the George Mason University, University of Maryland, University of Arkansas, University of Memphis, Arizona State University, Aston Business School, Copenhagen Business School, Cambridge Judge Business School, London School of Economics, and the INFORMS Annual Meeting 2007. The authors gratefully acknowledge the support of Rick Henderson, Carol Bachtel and Shane Wolverton of Comparion Medical Analytics (formerly known as The Delta Group) for providing hospital quality data. Summer support from the School of Management at George Mason University and Mason School of Business at College of William and Mary is gratefully acknowledged.

## References

Ahn SC, Schmidt P (1995) Efficient estimation of models for panel data estimation. J. Econometrics 68(1):5–27.

Ammenwerth E, Schnell-Inderst P, Machan C, Siebert U (2008) The effect of electronic prescribing on medication errors and adverse drug events: A systematic review. J. Amer. Medical Informatics Association 15(5):585–600.

Angst CM, Devaraj S, Queenan C, Greenwood B (2011) Performance effects related to the sequence of integration of healthcare technologies. Production Oper. Management J. 20(3):319–333.

Arellano M, Bond S (1991) Some tests of specification for panel data: Monte Carlo evidence and an application to employment equations. Rev. Econom. Stud. 58(2):277–297.

Arrow KJ (1971) Essays in the Theory of Risk-Bearing (Markham, Chicago).

Barua A, Kriebel CH, Mukhopadhyay T (1995) Information technologies and business value: An analytic and empirical investigation. Inform. Systems Res. 6(1):3–23.

Bates DW, Evans RS, Murff H, Stetson PD, Pizziferri L, Hripcsak G (2003) Detecting adverse events using information technology. J. Amer. Medical Informatics Association 10(2):115–128.

Bhattacherjee A, Hikmet N, Menachemi N, Kayhan V, Brooks RG (2007) Performance effects of hospital information technology adoption. Inform. Systems Management 24(1):7–16.

Blundell R, Bond S (1998) Initial conditions and moment restrictions in dynamic panel data models. J. Econometrics 87(1):115–143.

Boyer M, Dionne G (1989) An empirical analysis of moral hazard and experience rating. Rev. Econom. Statist. 71(1):128–134.

Brennan TA, Sox CM, Burstin HR (1996) Relation between negligent adverse events and the outcomes of medical-malpractice litigation. New England J. Medicine 335(26):1963–1967.

Brown CA, Bailey JH, Davis MEM, Garrett P, Rudman WJ (2004) Improving patient safety through information technology, Perspectives Health Inform. Management 2(5). Accessed May 28, 2008, http://library.ahima.org/xpedio/ groups/public/documents/ahima/bok1\_028123.html.

Carroll R (2009) Risk Management Handbook for Health Care Organizations, Student ed. (Jossey-Bass, San Francisco).

Chaudhry B, Wang J, Wu S, Maglione M, Mojica W, Roth E, Morton SC, Shekelle PG (2006) Systematic review: Impact of health information technology on quality, efficiency, and costs of medical care. Ann. Internal Medicine 144(10):E-12–E-22.

Clemons EK, Reddi SP, Row MC (1993) The impact of information technology on the organization of economic activity: The “move to the middle” hypothesis. J. Management Inform. Systems 10(2):9–35.

Cleverley WO (1989) Handbook of Health Care Accounting and Finance, 2nd ed. (Aspen Publishers, Rockville, MD).

Cuellar AE, Gertler PJ (2006) Strategic integration of hospitals and physicians. J. Health Econom. 25(1):1–28.

Culler SD, Hawley JN, Naylor V, Rask KJ (2007) Is the availability of hospital IT applications associated with a hospital’s risk adjusted incidence rate for patient safety indicators? Results from 66 Georgia hospitals. J. Medical Systems 31(5):319–327.

Danzon PM (1985) Liability and liability insurance for medical malpractice. J. Health Econom. 4(4):309–331.

Das S, Yaylacicegi U, Menon NM (2011) The effect of information technology investments in healthcare: A longitudinal study of its lag, duration, and economic value. IEEE Trans. Engrg. Management 58(1):124–140.

DesHarnais SI, Forthman MT, Homa-Lowry JM, Wooster LD (2000) Risk-adjusted clinical quality indicators: Indices for measuring and monitoring rates of mortality, complications, and readmissions. Quality Management Health Care 9(1):14–22.

Devaraj S, Kohli R (2000) Information technology payoff in the healthcare industry: A longitudinal study. J. Management Inform. Systems 16(4):41–67.

Dewan S, Shi C, Gurbaxani V (2007) Investigating the risk-return relationship of information technology investment: Firm-level empirical analysis. Management Sci. 53(12):1829–1842.

Dewett T, Jones GR (2001) The role of information technology in the organization: A review, model, and assessment. J. Management 27(3):313–346.

Dindo D, Demartines N, Clavien P-A (2004) Classification of surgical complications: A new proposal with evaluation in a cohort of 6,336 patients and results of a survey. Ann. Surgery 240(2):205–213.

Dionne G, Eeckhoudt L (1985) Self-insurance, self-protection and increased risk aversion. Econom. Lett. 17(1–2):39–42.

Dubay L, Kaestner R, Waidmann T (1999) The impact of malpractice fears on Cesarean section rates. J. Health Econom. 18(4):491–522.

Ehrlich I, Becker GS (1972) Market insurance, self-insurance, and self-protection. J. Political Econom. 80(4):623–648.

Eisenhardt K (1989) Agency theory: An assessment and review. Acad. Management Rev. 14(1):57–75.

Ellis RP, McGuire TG (1996) Hospital response to prospective payment: Moral hazard, selection, and practice-style effects. J. Health Econom. 15(3):257–277.

Forthman MT, Gold RS, Dove HG, Henderson RD (2010) Riskadjusted indices for measuring the quality of inpatient care. Quality Management Health Care 19(3):265–277.

Friedman B, Encinosa W, Jiang HJ, Mutter R (2009) Do patient safety events increase readmissions? Medical Care 47(5):583–590.

Garcia-Aymerich J, Hernandez C, Alonso A, Casas A, Rodriguez-Roisin R, Anto JM, Roca J (2007) Effects of an integrated care intervention on risk factors of COPD readmission. Respiratory Medicine 101(7):1462–1469.

Gawande A (2010) The Checklist Manifesto: How to Get Things Right, 1st ed. (Metropolitan Books, New York).

Gilman BH (2000) Hospital response to DRG refinements: The impact of multiple reimbursement incentives on inpatient length of stay. Health Econom. 9(4):277–294.

Goldschmidt PG (2005) HIT and MIS: Implications of health information technology and medical information systems. Comm. ACM 48(10):68–74.

Greene W (2003) Econometric Analysis (Prentice Hall, Upper Saddle River, NJ).

Hill JW, Langvardt AW, Massey AP (2007) Law, information technology, and medical errors: Toward a national healthcare information network approach to improving patient care and reduce malpractice costs. J. Law. Tech. Policy (2):159–237.

Holmström B (1979) Moral hazard and observability. Bell J. Econom. 10(1):74–91.

Horn SD, Sharkey PD, Buckle JM, Backofen JE, Averill RF, Horn RA (1991) The relationship between severity of illness and hospital length of stay and mortality. Medical Care 29(4):305–317.

Institute of Medicine (1999) To Err is Human: Building a Safer Health System (National Academy Press, Washington, DC).

Jones SS, Adams JL, Schneider EC, Ringel JS, McGlynn EA (2010) Electronic health record adoption and quality improvement in US hospitals. Amer. J. Medical Care 16(12):64–71.

Judson RA, Owen AL (1999) Estimating dynamic panel data models: A guide for macroeconomists. Econom. Lett. 65(1):9–15.

Kaplan S, Garrick BJ (1981) On the quantitative definition of risk. Risk Analysis 1(1):11–27.

Kavaler F, Spiegel AD (2003) Risk Management in Health Care Institutions : A Strategic Approach (Jones and Bartlett, Sudbury, MA).

Kessler DP (2011) Evaluating the medical malpractice system and options for reform. J. Econom. Perspect. 25(2):93–110.

Knight D, Durham CC, Locke EA (2001) The relationship of team goals, incentives, and efficacy to strategic risk, tactical implementation, and performance. Acad. Management J. 44(2):326–338.

Knight FH (1921) Risk, Uncertainty and Profit (Harper & Row, New York).

Ko M, Osei-Bryson K-M (2004) Assess the impact of information technology investments using regression splines to assess the impact of information technology investments on productivity in the health care industry. Inform. Systems J. 14(1):43–63.

Kohli R, Devaraj S (2003) Measuring information technology payoff: A meta-analysis of structural variables in firm-level empirical research. Inform. Systems Res. 14(2):127–145.

Li LX, Collier DA (2000) The role of technology and quality on hospital financial performance. Internat. J. Service Indust. Management 11(3):202–224.

Mangalmurti SS, Murtagh L, Mello MM (2010) Medical malpractice liability in the age of electronic health records. New England J. Medicine 363(21):2060–2067.

March JG, Shapira Z (1987) Managerial perspectives on risk and risk taking. Management Sci. 33(11):1404–1418.

Markus ML (2000) Toward an integrative theory of risk control. Baskerville R, Stage J, DeGross JI, eds. Organizational and Social Perspectives on Information Technology (Kluywer Academic Publishers, Boston), 167–178.

McCullough JS, Casey M, Moscovice I, Prasad S (2010) The effect of health information technology on quality in U.S. hospitals. Health Affairs 29(4):647–654.

McKay NL, Lemak CH, Lovett A, Wright RR (2008) Variations in hospital administrative costs. J. Healthcare Management 53(3):153–167.

Mello MM, Chandra A, Gawande AA, Studdert DM (2010) National costs of the medical liability system. Health Affairs 29(9):1569–77.

Melville N, Kraemer K, Gurbaxani V (2004) Review: Information technology and organizational performance: An integrative model of IT business value. MIS Quart. 28(2):283–322.

Menon NM, Lee B, Eldenburg L (2000) Productivity of information systems in the healthcare industry. Inform. Systems Res. 11(1):83–92.

Menon NM, Yaylacicegi U, Cezar A (2009) Differential effects of the two types of information systems: A hospital-based study. J. Management Inform. Systems 26(1):297–316.

Metcalfe MA, Sloggett A, McPherson K (1997) Mortality among appropriately referred patients refused admission to intensivecare units. The Lancet 350(9070):7–11.

Mittal N, Nault BR (2009) Investments in information technology: Indirect effects and information technology intensity. Inform. Systems Res. 20(1):140–154.

Morlock LL, Malitz FE (1991) Do hospital risk management programs make a difference? Relationships between risk management program activities and hospital malpractice claims experience. Law Contemporary Problems 54(2):1–22.

Ö ˘güt H, Raghunathan S, Menon NM (2011) Cyber security risk management: Public policy implications of correlated risk, imperfect ability to prove loss, and observability of selfprotection. Risk Analysis 31(3):497–512.

Orszag PR (2008) Evidence on the costs and benefits of health information technology. Testimony before the House Ways and Means Subcommittee on Health, 24 July, Washington, DC. Accessed November 28, 2009, http://www.hhs.gov/healthit.

Piontek F, Kohli R, Conlon P, Ellis JJ, Jablonski J, Kini N (2010) Effects of an adverse-drug-event alert system on cost and quality outcomes in community hospitals. Amer. J. Health-System Pharmacy 67(8):613–620.

Ransbotham S, Overby EM, Jernigan MC (2011) Medical malpractice claims and electronic medical records. Accessed March 12, 2013, http://ssrn.com/abstract=1963949.

Ray G, Muhanna WA, Barney JB (2005) Information technology and the performance of the customer service process: A resourcebased analysis. MIS Quart. 29(4):625–652.

Reuer JJ, Leiblein MJ (2000) Downside risk implications of multinationality and international joint ventures. Acad. Management J. 43(2):203–214.

Reufli TW, Collins JM, Lacugna JR (1999) Risk measures in strategic management research: Auld lang syne? Strategic Management J. 20(2):167–194.

Reynolds RA, Rizzo JA, Gonzalez ML (1987) The cost of medical professional liability. J. Amer. Medical Assoc. 257(20):2776–2781.

Rockart JF, Short JE (1989) IT in the 1990s: Managing organizational interdependence. Sloan Management Rev. 30(2):7–17.

Romano PS, Chan BK, Schembri ME, Rainwater JA (2002) Can administrative data be used to compare postoperative complication rates across hospitals? Medical Care 40(10):856–867.

Roodman D (2009) A note on the theme of too many instruments. Oxford Bulletin Econom. Statist. 71(1):135–158.

Setia P, Setia M, Krishnan R, Sambamurthy V (2011) The effects of the assimilation and use of IT applications on financial performance in healthcare organizations. J. Assoc. Inform. Systems 12(3):275–298.

Shavell S (1979) On moral hazard and insurance. Quart. J. Econom. 93(4):541–562.

Shukla RK, Pestian J (1997) A comparative analysis of revenue and cost-management strategies of not-for-profit and for-profit hospitals. Hospital Health Services Admin. 42(1):117–134.

Shur R, Simons N (2008) Quality issues in health care research and practice. Nursing Econom. 26(4):258–262.

Sitkin SB, Pablo AL (1992) Reconceptualizing the determinants of risk behavior. Acad. Management Rev. 17(1):9–38.

Sloan FA (1990) Experience rating: Does it make sense for medical malpractice insurance? Amer. Econom. Rev. 80(2):128–133.

Straub DW, Welke RJ (1998) Coping with systems risk: Security planning models for management decision making. MIS Quart. 22(4):441–469.

Studdert DM, Mello MM, Sage WM, DesRoches CM, Peugh J, Zapert K, Brennan TA (2004) Defensive medicine among highrisk specialist physicians in a volatile malpractice environment. JAMA 293(21):2609–2617.

Subramani M, Walden E (2001) The impact of e-commerce announcements on the market value of firms. Inform. Systems Res. 12(2):135–154.

Tanriverdi H, Ruefli TM (2004) The role of information technology in risk/return relations of firms. J. Assoc. Inform. Systems 5(11– 12):421–447.

Towse A, Danzon P (1999) Medical negligence and the NHS: An economic analysis. Health Econom. 8(2):93–101.

Vincent C (1997) Risk, safety, and the dark side of quality. British Med. J. 314(7097):1775–1776.

Wang BBL, Wan TTH, Falk JA, Goodwin D (2001) Management strategies and financial performance in rural and urban hospitals. J. Medical Systems. 25(4):241–255.

Weissman JS, Annas CL, Epstein AM, Schneider EC, Clarridge B, Kirle L, Gatsonis C, Feibelmann S, Ridley N (2005) Error reporting and disclosure systems: Views from hospital leaders. J. Amer. Medical Assoc. 293(11):1359–1366.

Zarling EJ, Piontek FA, Kohli R (1999) The utility of hospital administrative data for generating a screening program to predict adverse outcomes. Amer. J. Med. Qual. 14(6):242–247.

Zhan C, Miller MR (2003) Excess length of stay, charges, and mortality attributable to medical injuries during hospitalization. J. Amer. Med. Assoc. 290(14):1868–1874.
