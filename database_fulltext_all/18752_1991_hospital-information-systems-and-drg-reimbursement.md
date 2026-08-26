---
otero_id: 18752
otero_key: "G3N2956V"
title: "Hospital information systems and DRG reimbursement"
authors: "Michael A. Palley"
year: "1991"
journal: "Information & Management"
doi: "10.1016/0378-7206(91)90057-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
SOS

# Hospital information systems and DRG reimbursement

# The adaptation of large transactions processing systems to radical rule changes

Michael A. Palley

Baruch College, City University of New York, School of Business and Public Administration, New York, NY 10010, USA

Large transactions processing systems are often rigid, closed, and mechanistic. When faced with sudden and severe change, organizations may have difficulty adapting quickly and effectively. This paper investigates how three major New York hospitals adjusted to the imposition on their patient account systems of DRG based reimbursement. The field study identifies common strategies and problems, along with the need for further research into how to efficiently adapt such critical systems to drastic change.

Keywords: Hospital Information Systems, Management Information Systems, Computer Information Systems.

![](/api/attachments/G3N2956V/fulltext/images/27028832fed78b8c18f6734d32218835cc94aaf952dcbd83c824d13bfa12fb43.jpg)

Michael A. Palley is Associate Professor of computer information systems at Baruch College - City University of New York. His research interests include hospital information systems, management information systems, database management systems, and systems analysis and design. His research has appeared in several journals, including Communications of the ACM, ACM Transactions on Database Systems, and Journal of Management Information Systems. He holds a BS from the Wharton School, and a PhD in Information Systems from New York University.

## 1. When the Rules Change

What happens to an information system when confronted by drastic and all-encompassing process rule changes? Few information systems have encountered the degree of upheaval that the healthcare industry is experiencing with the advent of “Diagnosis Related Group (DRG)” based reimbursement. Hospitals that utilized rigid and time honored accounts receivable systems, have suddenly been faced with an impending need for system overhaul.

Budgets for healthcare data processing systems exceed \$4 billion annually, with expenditures for patient accounting systems approximately one-half of that amount (Kennedy and Collignon, 1987). The dramatic changeover to DRGs has had repercussions on all hospital information systems in states that have adopted the change. This study addresses the following question:

How can a large closed and mechanistic information system be adapted to sudden and radical changes to process rules and environment?

This question is investigated through a field study of patient accounts information systems. The study was conducted in August 1988 at three large New York City metropolitan area hospitals, several months after the statewide adoption of DRG based reimbursement.

First, some background material is presented on the nature of patient accounts systems and DRGs. In the next sections, observations of the three hospitals are described. Commonalities in the problems encountered are presented in section 4. In section 5, the basic strategies that these hospitals used to adapt are described. Finally, the need for generalized strategies to adapt rigid systems to radical change is discussed.

## 2. DRG Based Reimbursement

Patient account systems are concerned with the timely and accurate billing and collection of hospital charges. Prior to DRGs, patient account systems operated much like accounts receivable systems of other enterprises. Billing was based on charges for actual services that were provided by the hospital. Hospitals generally bill insurance companies as well as patients, the former referred to as “third party payers”.

Fedorowicz (1983) reported that hospital information systems in general lag “years behind their corporate counterparts”. Hospital environments historically had little concern for cost management (referred to as the “caste era” (May and Bowman, 1986)). This has ceased to be the case, with hospitals now in the “cost” and “value” era (ibid). The sudden shift to cost containment led to a reluctance to commit new funds to operations areas such as computing. Another reason that hospital systems may have lagged is that they were typically closed-mechanistic. Historically, it was very unusual for process logic to need more than routine maintenance and adjustment. Hence, these were never high profile systems where there would be commitment to innovation.

In New York State, DRG based reimbursement was adopted by the state legislature for Medicare in 1986, and for virtually all commercial insurers in 1988. This includes Medicaid, Blue Cross, health maintenance organizations (HMOs), Workers' Compensation, and most commercial and self-insured plans.

The DRG technique, developed at Yale University, attempts to “categorize patients into clinically coherent and homogeneous groups with respect to their consumption of hospital resources as measured by length of stay” (Hospital Assoc. of NY State, 1988). The DRG technique reimburses hospitals a flat fee based on a patient’s diagnosis, rather than on actual services provided. Adjustments to the fee are made for extreme cases such as patients defined as “high cost outliers” or “long stay outliers”. DRG information is culled from patients’ medical records. Therefore, one of the major impacts of the change is the sudden need for the integration of the patient account systems with other stand alone hospital systems (e.g., medical records).

The motivation for DRGs has presumably been to contain rising healthcare costs. The rules, definitions, and procedures involved in the DRG based technique are quite detailed and complex. On occasion, DRG rules have been mandated to hospitals and insurers before being fully clarified. Most of the management interviewed: patient account managers, MIS personnel, and vice-presidents of finance, were generally struggling just to stay abreast of the intricate procedures and changes to them. Needless to say, the change to DRGs has been controversial and emotional. The relative merits and criticisms of the approach remain outside the scope of this research.

In general, accounts receivable systems serve as the prototype for the closed-mechanistic information system. Rigidity and predictability are hailed as the desirable attributes for a financial system of this nature. Ironically, it is those close-mechanistic systems that have been thrown into disarray by the DRG environment.

## 3. A Case Study of Three Hospitals

The case study involved three major hospitals in the New York metropolitan area. Two are major facilities in Manhattan, the third is the major hospital in a nearby suburban county. Interviews were held with the director of patient accounts, vice president of finance, MIS director, and a few general staff members at each hospital. The turbulent nature of cost control and profitability in the hospital industry has made public discussion of these hospitals' general performance and their information systems delicate. A fourth major hospital could not be included in our study. Poor financial performance there for the previous few years led to the virtually complete turnover of financial management. An extremely defensive stance was adopted by management, leading to its exclusion from the study. Since the system overhauls involved are extremely expensive, the hospitals studied were not comfortable being publicly identified. Table 1 summarizes the observations at the three hospitals.

Table 1
Summary of Observations

<table><tr><td></td><td>Hospital One</td><td>Hospital Two</td><td>Hospital Three</td></tr><tr><td>Patient Days 1987</td><td>194,362</td><td>361,065</td><td>308,000</td></tr><tr><td>Software in Use</td><td>HCS</td><td>HOSPAC</td><td>MEDIPAC</td></tr><tr><td>Hardware</td><td>IBM 3080</td><td>IBM 4341</td><td>IBM 4083</td></tr><tr><td>Length of Service</td><td>since 1950s</td><td>since 1974</td><td>since 1985 formerly used SHAS since 1960s</td></tr><tr><td>Level of System Integration</td><td>Mostly Batch with a Manual Interface</td><td>Mostly Batch with Tape Interface</td><td>Mostly Batch with Tape Interface</td></tr><tr><td>Degree of Manual Intervention</td><td>High System Outputs Require Manual “Finishing”</td><td>High All DRG Calculations Performed Manually</td><td>Relatively Low</td></tr><tr><td>New System Plans</td><td>Complete System Overhaul imminent est. $ 1.5–2 million</td><td>Currently: Online Support of DRG tables Long term: no solid plans</td><td>Install Vendor Supplied Updates</td></tr><tr><td>Major Problems</td><td>System at Full Capacity; High Degree of Manual Intervention</td><td>Significant Reprocessing; Manual DRG Calculations</td><td>Significant Reprocessing; Inefficient Batch Processing</td></tr></table>

## 3.1. Hospital One - A Suburban County Hospital

The first hospital, one of the largest in the area, is a county run healthcare facility in a New York City suburban area. Total 1987 patient days was 194,362. Revenue for the hospital that year was \$ 129 million.

Since the 1950's, Patient accounts processing has run on the HCS (“Hospital Care System”) software package, developed by IBM. The source code is written mostly in COBOL, with some code written in assembler. The software runs on an IBM 3080 series mainframe, in batch mode; and is operated and maintained by a staff of three programmers.

## Transition to DRG's

In 1986, the software underwent extensive modification to accommodate introduction of DRG's to Medicare. Numerous new COBOL subroutines were installed to adapt processes to the new framework. The modification utilized as many as seven full-time programmers for a full year.

While modifying the system to accommodate Medicare DRGs, the systems staff also anticipated the impending more radical changeover for all commercial insurers. The system was built to DRG-process all patient accounts, although only the Medicare patient outputs were utilized at the time. An added advantage of this was that if a patient were not properly classified as a Medicare subscriber, later correction would not necessitate reprocessing the charges. The 1986 Medicare DRG changeover was eventually adaptable to the DRG procedures mandated for other insurers in 1988.

Currently, inpatient and emergency room charges have an online interface with the billing system. However, clinic registrations (approximately 100,000 transactions per year) continue to be processed in batch mode from manual input forms. Also, charges for ancillary services including physical and occupational therapy, urology, etc., continue to be entered in batch mode. All cash transactions are posted in batch mode as well. Laboratory and radiology services independently batch their transactions to tape. These tape transactions are merged with other patient account charges. Not only do inputs originate in batch mode, but output is not in final form. This requires a staff of personnel to manually “finish” the billing process. The batch environment at this hospital causes inefficiency, errors, and a several day lag in the processing of charges. All of these adversely affect the hospital's financial performance.

## Significant Problems

Discussion with system staff identified the following problems in descending order of severity:

a. Lack of Interface Among Subsystems. There is no online coordination between the patient accounts and other subsystems, e.g. labs, x-ray, medical records. This has led to numerous processing problems. For example, charges generated by the labs are not cross checked for validity with the patient accounts masterfile. The medical records system may contain invalid patient account numbers, causing delays in billing, or charges that can never be billed. These observed phenomenon are consistent with a study by Mendenhall (1988) that described the disjointed nature of hospital information systems, and the need for integration.

b. No Capacity for Expansion. The system no longer accommodates the growing number of patient services that are provided and billed by the hospital. A given account's maximum receivable balance is limited to \$100,000 by a restrictive field size declaration, a development assumption that is clearly obsolete. The hospital deals with exception cases of this sort by splitting a charge into multiple dummy accounts. Similarly, a charge for any test is limited to \$999. Each of these software limitations is considered to be infeasible to repair.

c. Need for Online Environment. The need to manually intervene and “finish” billing is both error prone, and slow. Additionally, the hospital is in dire need of electronic billing (e.g. magnetic tape) capabilities. The findings are consistent with Mager and Collignon (1988) who found a high percentage of hospitals naming “online account inquiry” and “electronic third party billing” capabilities as sorely needed.

## Future Plans

This hospital has undertaken the complete replacement of its HCS system. The system being developed by an outside concern will be fully integrated (admitting, patient accounts, etc.), and online. The system will facilitate tape to tape billing. The budget is currently roughly \$ 1.5 million, and may eventually run as high as \$2 million. This includes retention of a consulting firm to represent the hospital's needs to the software vendor. A chronic limitation is that certain cost centers have elected to remain independent of the new system, and will continue to provide taped batched charges. An elementary version of the system was delivered by the vendor subsequent to this study, in July 1989. The hospital continues to await additional enhancements to be delivered by the vendor.

## 3.2. Hospital Two - New York City

The second hospital had 361,065 patient days in 1987, making it the largest hospital in this study. Total revenue and profitability information for the hospital in 1987 were sensitive and not forthcoming.

Hospital Two has processed patient charges on a software package called HOSPAC (“Hospital Patient Accounts”), a package created by a private vendor. The software has been in place since 1974. HOSPAC is COBOL based, and currently runs on an IBM 4341. The software has been heavily modified during its tenure, and is maintained by the outside vendor, assisted by one in-house information systems staff member. The system is essentially batch in nature.

## Transition to DRG's

The transformation in 1986 for Medicare went relatively smoothly since there was only one uniform set of rules that had to be followed. However, the 1988 changeover, for all commercial carriers, led to (and continues to cause) difficulties due to the lack of standardization. At the present time, DRG calculations for the commercial carriers are being performed as a manual post-system process. At the time of our interview, the information systems department was actively involved in the computer support of such a calculation table.

## Significant Problems

Hospital Two's major problems stem from ambiguities in how to process claims under the 1988 DRG rules for commercial insurers. Furthermore, the changeover took effect before some key parts of the rules were completely developed by the State. At one point, the hospital was plagued by a six month delay, awaiting rules about how to process already pending claims. There is an expressed belief that the commercial insurers themselves do not fully understand the rule changes.

In the old environment, a bill was reimbursed on the basis of a known schedule. Therefore, the hospital would generate a list of patient charges. Upon comparison with each appropriate reimbursement schedule, books would be adjusted at the time the bill was produced. At present, since the commercial insurers' repayment rules are ambiguous, it is virtually impossible for the hospital to produce a bill that will not require further adjustment. On the contrary, once payment is received, and disagreements are resolved, each patient's account will typically require a new adjustment to zero out. As the information system was not created with this problem in mind, it has necessitated a second process cycle. Also, the existing system has several billing centers that are not directly linked to the system. This necessitates additional batch intervention. Time and resource consumption relating to these problems remain the major system related complaint at this hospital.

## Future Plans

In the future, the hospital plans to adopt a new vendor produced package. This will necessitate a rigorous planning process. Facilities must be planned to accommodate new hardware, anticipated to be an IBM 3090 series computer. At that point major budget planning, as well as system development stages will commence.

## 3.3 Hospital Three - New York City

The third hospital, had roughly 308,000 patient days in 1987, somewhat less that Hospital Two. Net income for the year was roughly zero.

Patient account processing at this hospital traditionally ran on an IBM software system called SHAS (“Shared Accounting System”), implemented in the 1960's. Medical records were maintained on a system called CHARMS since 1983. In December of 1985, patient account processing was converted over to a much more contemporary package called MEDIPAC (“Medical Patient Accounts”). MEDIPAC was interfaced with the hospital’s own existing admitting and medical records systems. The hospital utilized an IBM 370 series computer for many years, followed by a two year stint with an IBM 3081. That system rapidly ran out of capacity, leading to its ultimate replacement with and IBM 4083.

## Transition to DRG's

While New York State was mandating DRGs, the hospital's information systems staff was busily involved in an unrelated migration from the DOS to OS operating systems. This took a heavy toll on system development resources. At the same time, the hospital was plagued by the turnover of key systems personnel. As a result, installation of the MEDIPAC updates necessary for 1986 Medicare DRGs was first completed in mid 1988. The changeover took three to four full time programmers approximately two years, roughly $10\%$ of the information systems staff.

The updates necessary for changeover to commercial insurer DRG processing (effective Jan. 1, 1988) were first released in September 1988. Implementation of the new release was expected for October 1988.

Currently, laboratories are interfaced with the MEDIPAC system through tape. Other interfaces, including medical records are online.

## Significant Problems

Hospital Three suffers from various chronic problems. The first, as discussed, is its need to catch up on vendor distributed software updates. Batch process run time is also problematic. Account updates require a full nine hours to run at the end of every business day. This is due, in part, to inefficiencies among the subsystem interfaces. Many of these interfaces were COBOL patches into existing software. Another problem is that the system needlessly batch processes the file's numerous zero balance accounts.

The current system offers little in the way of ad hoc reporting capabilities. Case mix reports necessitate an off site tape merge by the hospital's audit firm. The medical record system is currently running out of medical identification numbers. Changing this variable from 6 to 8 bytes is requiring modification to roughly 6000 programs.

The hospital has found it prudent to provide insurers with a breakdown of how each DRG derived charge is created. This was implemented on a microcomputer system by the patient accounts manager himself. Thus, the lack of ad hoc capability is managed by circumventing the mainframe computer.

The most significant problems involve the dynamic DRG environment. Changes in rules and in the hospital's DRG schedules are revised by the State retroactively. This entails rebilling commercial carriers for balances, necessitating considerable reprocessing of accounts. This also creates an issue of what to do with self-payers. Are patients who previously “paid in full” now to be rebilled retroactively for recalculated higher charges? Certainly, some reduced charges will require refunds to both self-payers and insurers.

The net result to the hospital, is considerable need to reprocess. Additional requirements for trained and qualified staff are extremely costly. Nevertheless, Hospital Three appears to have coped with the changeover well, and has not lost money – a measure of success for a not for profit institution.

## Future Plans

Future plans for this system involve the installation of further updates of MEDIPAC. Delay in the delivery of software updates by the vendor causes the hospital difficulty. This is worsened by the untimely installation of these updates by a very busy information systems staff. At the moment, there are no plans for adding ad hoc reporting capabilities to the system.

## 4. Discussion

The three organizations suffer from three major problems in their adaptation to DRG processing: (a) the dynamic nature of the DRG environment, (b) small in-house development staffs suited to static information systems, and (c) decentralization of their information systems.

## a. Dynamic Nature of the DRG Environment

Part of the problem that these hospitals have encountered is related to the extremely turbulent nature of DRG rules. Although accounts receivable systems are typically of the static/mechanistic type, DRG based reimbursement has made the environment open/organic. Rate calculations and various processing rules (such as high cost outliers) change constantly, often retroactively. Besides undesirable uncertainty, the lack of a solidified rule structure causes these hospitals to routinely reprocess each transaction, often several times. Typically, financial transaction processing systems require clear, unambiguous rules. Within the framework of the classic Gorry–Scott Morton (1971) model, we are witnessing an “operational control” accounts receivable system that has moved from being extremely structured to semi-structured.

From lack of other viable options, the hospitals in this study rely on the acquisition of vendor developed software to cope with these changes. Lucas, Walton and Ginzburg (1988) suggest factors that might be related to the success of implementing such packaged software. However, research has yet to address how an industry might cope with radical changes short of scrapping long standing million dollar systems.

## b. Relatively Small In-House Development Staffs

Prior to imposition of DRGs, the hospital patient accounts systems were static. These hospitals, using packaged software, had little need for extensive information systems staffs. Most systems work was in maintenance. The hospitals clearly were not adequately staffed for the magnitude of the changeover to DRGs. Thus, the hospitals, for the most part, have relied on interim patching, and substantial manual intervention in order to cope with the new and semi-structured environment.

The hospitals relied on software which was geared towards a static environment. Kennedy and Collignon (1987) reported the results of a study sponsored by the Hospital Financial Management Association. This survey of 1330 hospitals found that “ease of modification” received the lowest satisfaction ranking of twelve factors related to their information systems. Likewise, “flexibility” was most frequently named as the factor considered critical in the selection of a new system.

## c. Decentralization of the Information Systems Process

The need to integrate hospital information systems has been documented in the literature (Lemon and Crudele, (1987); Vogel (1987)). Puhala and Barrett (1987) describe the need to integrate hospital information systems in order to validate data, e.g., matching the DRG value in the patient medical records file to the financial records file.

An ongoing problem for these hospitals is the relatively decentralized nature of information processing. Medical records, labs, admitting, and patient accounts areas have all developed their own information systems. Presumably this occurred in order to maintain departmental control over processing. The result is that considerable effort is devoted to create both online and manual interfaces to integrate non-standardized information. Resistance of these departments to relinquish control over processing continues to be a problem even after the introduction of expensive new software packages.

## 5. Conclusions

Returning to the original research questions, the question of interest is how a large closed-mechanistic information system adapts to sudden and drastic change. In the field study, three ways that the various hospitals have adjusted to the changes in the short run were identified.

## a. Reliance on Manual Intervention

Since the observed hospitals could not adapt their systems to the DRG changes in a timely manner, they have to a great extent coped through reliance on manual intervention. The intervention has taken the form of manual input of incompatible information. The DRG approach requires the integration of previously diverse sources of information – e.g. medical records with patient charges. These hospitals have resorted to a manual approach, with clear degradation to overall performance (speed, accuracy, etc.).

## b. Reprocessing

Erroneous DRG calculations, and the need to zero account balances that are still computed according to the old rules, cause hospitals to continually reprocess transactions. This is due in part to ambiguities in the DRG rule structure, and to poor performance of overpatched systems. Reprocessing in these systems is burdensome in terms of process time, and lack of reliability.

## c. Circumventing the Mainframe

Where time honored systems are inflexible, IS staffs have resorted to using timesharing or microcomputer solutions. As mentioned, one patient accounts manager developed an independent DRG calculation system on microcomputers. Besides the additional cost involved in this approach, there is the additional risk of reliability problems since the programs have been developed by non IS personnel. So called “case-mix” reports, which show the number of patients served by the hospital in each DRG category, are often farmed out to timesharing systems offered by vendors. Since much of the information processed by hospital billing systems is confidential, loss of control relating to timesharing introduces further risks.

## 5.1. Early Indicators of a System's Demise

The observations in this study suggest possible indicators of the oncoming death of a long standing information system. These are merely hypotheses, due to the small sample size of a case study. However these indicators should be of interest to systems managers. In future research, a larger study would be necessary to test the validity of these indicators (see Table 2).

Table 2

<table><tr><td>Indicator</td><td>Rationale</td></tr><tr><td>1. Age of Software</td><td>The longer the software&#x27;s length of service, the greater its likelihood of obsolescence.</td></tr><tr><td>2. Degree of Modification</td><td>The more the software has been modified, the more difficult future modifications become.</td></tr><tr><td>3. Potential for Environmental Change</td><td>Even a closed mechanistic environment needs periodic reassessment. In the case of DRGs, there were early warning signs that indicated a high likelihood of impending drastic change.</td></tr><tr><td>4. Degree of Internal Control over Current Software</td><td>An environment where software is provided and maintained by outside parties gives the user little control to manage impending change.</td></tr><tr><td>5. Criticality of Application</td><td>Clearly relevant in risk assessment. Will have implications on the amount of resources that a user will devote to maintenance of the software.</td></tr><tr><td>6. Size of Maintenance Staff</td><td>A small maintenance staff will have difficulty managing impending radical changes to a static system.</td></tr></table>

It would be useful for managers to have indicators of impending large system demise. The hospitals in this study have taken last minute, ad hoc, and emergency measures to cope with the demise of their very critical patient accounts systems. An earlier and more realistic recognition of the demise might have led to more cost and time efficient measures.

It is difficult to judge the extent that these hospitals are representative of the industry. As major players in a large urban center, one assumes that these hospitals have the resources to devote to major systems overhaul. One wonders what smaller hospitals, faced with the same changes are doing to cope.

It is unusual to see an industry have its procedures as quickly and radically overhauled as has happened with DRGs. Information systems research (Kim and Weston, 1988, for example) proposes several ways to design for system maintenance and modification. This includes the use of database management systems, CASE software approaches, fourth generation software tools, modular design, structured code, and so forth. However, the literature has not addressed the situation described here: how to effectively adapt existing large and static transactions processing systems to a suddenly dynamic and semi-structured environment. The hospitals observed have taken costly and inefficient patch solutions, followed by impending million dollar new system acquisitions. Further research might suggest more cost effective approaches.

## 6. References

Fedorowicz, J., "Hospital information systems: are we ready for case mix applications?", Health Care Management Review, Fall 1983, pp. 33–41.

Gorry, G.A., and Scott Morton, M.S., "A framework for management information systems", Sloan Management Review, 13, 1, pp. 55–70.

Hospital Association of New York State, "Excerpts from Hospital Reimbursed Case Based Rate of Payment for 1988, 1989, and 1990", April 30, 1988.

Kennedy, O.G. and Collignon, S.J., "Selecting patient accounting systems that stand out from the rest", Healthcare Financial Management, June 1987, pp. 29–44.

Kim, C. and Weston, S., "Software maintainability: perceptions of EDP professionals", MIS Quarterly, 12, 2, June 1988, pp. 167–186.

Lemon, R. and Crudele, J., “Systems integration: tying it all together”, Healthcare Financial Management, June 1987, pp. 46–53.

Lucas, H.C., Walton, E.J., and Ginzburg, M.J., “Implementing packaged software”, MIS Quarterly, 12, 4, Dec. 1988, pp. 537–549.

Mager, R.D. and Collignon, S.J., “Patient accounting systems: are satisfaction levels rising?”, Healthcare Financial Management, June 1988, pp. 40–46.

May, J.J and Bowman, E.H., “Information systems for the value management era”, Healthcare Financial Management, Dec. 1986, pp. 70–74.

Mendenhall, S., “Integrating clinical financial information: improving patient management”, Healthcare Financial Management, June 1988, pp. 54–60.

Puhala, J.J. and Barrett, M.J., “Patient accounting: vital for financial survival”, Healthcare Financial Management, Sept. 1987, pp. 25–36.

Vogel, L.H., “Patient accounts management: it’s what’s up front that counts”, Healthcare Financial Management, Sept. 1987, pp. 43–52.
