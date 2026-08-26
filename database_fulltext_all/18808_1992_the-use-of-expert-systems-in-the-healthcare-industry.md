---
otero_id: 18808
otero_key: "Z8Q43CPT"
title: "The use of expert systems in the healthcare industry"
authors: "Nancy McCauley; Mohammad Ala"
year: "1992"
journal: "Information & Management"
doi: "10.1016/0378-7206(92)90025-b"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Briefing

# The use of expert systems in the healthcare industry

Nancy McCauley \*

McCauley and Associates, Los Angeles, CA, USA

Mohammad Ala

California State University-LA, Los Angeles, CA, USA

The large, enormously complex expert systems (ES) such as MYCIN, ONCOCIN, and INTERNIST raised the expectations of many that artificial intelligence (AI) technology would have a significant impact on the everyday practice of medicine. A rather eclectic literature search reveals that while hundreds of applied expert systems have been prototyped, these have not led to a groundswell of interest among either practicing physicians or healthcare administrators. To account for this apparent failure of expert systems to deliver on their promised capabilities, three key factors are explored: physician disinterest; the low priority assigned to AI among healthcare information systems executives; and the relatively new competitive market pressures affecting health services delivery. A domain of the healthcare industry where ES and knowledge-based technology has taken hold, i.e. the managed care/utilization review arena, is described. This new application of ES technology has the potential to influence standards of medical practice through “medical necessity criteria” embedded in the knowledge base, and to disseminate key findings from research on medical treatment outcomes. Ethical and legal issues surrounding the appropriate use of this technology remain as yet untested and unresolved, however.

Keywords: Artificial intelligence, Expert systems, Knowledge-based systems, Healthcare information systems, Managed care, Medical necessity criteria, Outcomes research, Utilization review.

## 1. Introduction

Since the efforts of the Medical Computer Science Group at Stanford University, which resulted in the development of MYCIN, an infectious disease treatment advisor, and the subsequent creation of ONCOCIN, a medical consultation system for the management of cancer therapy, much has been expected of artificial intelligence (AI) and especially rule-based expert systems (ES) as clinical decision support tools. As a market for ES applications, the healthcare industry would seem to offer great potential, given the explosive rate-of-change in the areas of diagnosis and treatment, and the concern on the part of consumers, employers, providers, and both government and private payors for efficient, yet consistently high quality care. The emergence of over 200 on-line databases for literature searches and continuing medical education (MEDLINE, Grateful Med, etc.) can be viewed as a logical and necessary precursor to the development of systems to assist in clinical decision-making.

ES technology, however conceptually exciting, has not been embraced by most medical practitioners. We begin our inquiry with an operational definition of an expert system. Then an eclectic literature review provides the background for a presentation of three factors which help explain why expert systems have failed to become tools in the daily practice of medicine. A segment of the healthcare industry which has recently begun to utilize ES-related technology will then be introduced. It will be asserted that these new applications of ES and knowledge-based systems reflect profound and controversial changes underway in both the discipline of medicine and the business of providing health care services.

## 2. Definitions

Previous articles in I&M have researched the process of designing “intelligent” decision support systems (DSS) [1], discussed the distinctions between DSS and ES [2], surveyed the extent of ES usage in business organizations [3], suggested techniques for evaluating DSS and ES applications [4], and addressed such critical issues as unreliable data and cost-effectiveness [5]. We begin with a simple definition:

Plainly stated, an expert system is a computer program capable of automating decisions by asking questions and providing answers or conclusions. For the purposes of this discussion and in accordance with general usage, the terms expert system and knowledge-based system will be used here interchangeably. The essential ingredients of these systems are by now well-known, i.e.:

(1) a knowledge base, consisting of commonly agreed upon facts general to the knowledge domain (a medical school textbook is in fact a hard copy example), and “heuristics”, or rules of good judgment or best guessing;

(2) a strategy for knowledge representation, or encoding the knowledge. Two basic types of knowledge representation are (a) IF\_THEN\_rules, also called production rules, based upon logical reasoning, and (b) the more general semantic network, which represents small pieces of knowledge and how they relate to one another. Most knowledge-based systems to date use a combination of rules and nets to represent the knowledge they contain; and

(3) an inference engine, which is the problem-solving method or line of reasoning used by the system. The two classic methods used during an expert systems consultation are (a) backward chaining, which starts with a suspected diagnosis, and searches through rules and facts to prove or disprove the proposed conclusion, and (b) forward chaining, which starts with an array of facts about a present situation (a database), and comes up with one or more conclusions.

Two other features, or facilities, of the inference engine should also be noted:

(1) a way of dealing with uncertainty, since knowledge is often incomplete or of dubious reliability. Rules may be assigned different “weights” or certainty factors – based on empirical evidence rather than actual mathematical probability. Sophisticated expert systems have ways of dealing with observer variation (e.g., what is considered a normal range of laboratory measurements at different sites), using calculations based on fuzzy set logic (see Zadeh, e.g. [6,7,8]); and

(2) a facility called explanation, in which the line of reasoning or rule tree the system constructed for the problem it tried to solve can be displayed on the screen, or provided as text to the user.

## 3. Promise vs. reality: Observations

It is reasonable to assume that, as in the manufacturing sector [9], the use of expert/knowledge-based systems in the healthcare industry will grow. The potential benefits offered by ES are compelling: (1) the capture of the knowledge and experience of experts; (2) increased speed in the completion of complex but repetitive tasks (e.g., analysis of diagnostic test results); (3) increased consistency in decision making; and (4) the ability to capture the underlying assumptions of a decision-making process.

A review of the literature reveals that expert systems have remained on the periphery of the broader domain of healthcare information systems (HIS). Of an eclectic array of publications, Computers in Healthcare has published the most articles on expert systems in healthcare (four in 1988; by comparison, this periodical devoted seventeen articles in the same period to tools for “business/financial management”, nineteen to computerizing departmental operations, and fourteen to networking within or between departments). Of the ES articles, only one profiled an up-and-running, hospital-based application [10]; the others were basically promoting the concept. [11,12,13]

Several examples of ES software targeted at physician users were listed in M.D. Computing's Fifth Annual Buyers' Guide (November/December 1988). This Guide contains brief descriptions of 1,075 products from 460 vendors. Within the category of "Diagnosis/Therapy Support", fourteen products were listed, of which three are expert systems (including versions of the venerable INTERNIST, and INTERNIST PLUS). Under "Expert Systems", two development tools are listed. A handful of ES applications are listed by diagnostic category, e.g., cancer and hypertension. In contrast, over 200 software packages for billing and/or practice management were listed.

Expert systems as add-ons to high tech testing equipment (e.g., signal processing and imaging) remain in an exploratory phase. For example, of a group of several hundred abstracts from a recent international congress, just 15 abstracts were included under the heading “Expert Systems and Medicine … Pacing, Cardiology, Diabetes”. [14] None of the systems cited were in operational use.

Feigenbaum et al.'s recent book designed to inspire executives with stories of innovative uses of expert systems contains an appendix with brief descriptions of 139 ES applications across ten different industries. Under “Medical and Scientific Applications”, only six medical applications are described, of which just three are “off the shelf” and for sale; three others are systems built for internal use only.

A review of several library databases revealed evidence of a scattering (a few hundred, generously estimated) of ES and/or knowledge-based system applications under development in a variety of healthcare-related settings. For example:

(1) an ES was developed in-house for the Johns Hopkins Hospital psychiatric emergency room to assist resident MD's with triage (referral/disposition) decisions; “a study of its impact is underway” [15];

(2) the University of South Florida's Department of Health Policy and Management has developed an ES for determining Medicaid eligibility [16];

(3) an 8,000 rule ES was developed by the U.K. branch of Coopers and Lybrand to analyze the performance of England's regional health authorities [17].

Is some sort of breakthrough in applied clinical ES use just around the corner? One opinion survey found physicians less than half as likely as healthcare executives or trustees to think that computer-assisted diagnosis and medical decision support would have significant impact on healthcare delivery by the year 1995 (33% vs. 74% and 89% respectively). [18] What can be inferred from this is that practitioners do not intend to become end users, while both professional managers and their board members have at least bought into the underlying concepts – although our research found no evidence that these latter groups are willing to invest money in ES development.

Those interested in assessing for themselves the state of the art of healthcare applications of computer technology would be well advised to consult the Proceedings of the Annual Symposia on Computer Applications in Medical Care (SCAMC), as this is where university and medical school-based physicians and healthcare information systems developers present their latest accomplishments. With over 100 sessions, a broad range of technical, legal, educational and management issues are addressed. Several sessions of the 1990 SCAMC were devoted exclusively to applied expert systems; all of the systems described therein were developed at universities and teaching hospitals. Actual demonstrations of a variety of applications included just a few which were not university-based, among them a knowledge-based system designed at a major insurance company which will be further discussed below. While SCAMC represents the cutting edge of medical informatics in the United States, it would be interesting and challenging to assess the extent to which these Symposia have stimulated “real world” ES development and implementation, i.e. outside the academic research community.

## 4. Healthcare experts on expert systems

Medical and information systems authorities have expressed varying opinions about the current state of expert system development. A radiology specialist's perspective, drawn from a somewhat larger discussion, acknowledges the (as yet untested and unresolved) issue of potential liability:

…“the contribution of computers in medical diagnosis has been disappointing, in part because of the approaches taken in modeling human decision processes, the complexity of medical diagnosis, and the limitations of previous computer software… It seems certain that imaging equipment manufacturers eventually will provide AI with their instruments, but when this will occur depends on the resolution of a unique class of legal and social issues.” [19]

Two authorities on information systems echo this concern about risk:

…“acceptance of expert systems has not progressed as easily or rapidly as many have desired... Expert systems opponents have a grave concern for risks associated with systems which have a potential for poor decisions.” [20]

A recent article in a healthcare industry periodical poses the question of risk in no uncertain terms: in situations where an ES is used as a diagnostic tool, “[i]f treatment is administered improperly, who does the patient sue? The doctor? The software maker?” And if the technology does become widely available: “Do doctors who fail to consult their expert systems leave themselves open to malpractice suits?” [21]

Governmental evaluation and oversight is probably not forthcoming. The U.S. Food and Drug Administration (FDA) is in the process of addressing a number of software issues, but it is unlikely to get involved anytime soon in the regulation of expert systems. The FDA's reasoning is that since ES software only provides probable diagnoses and likely outcomes, physicians will continue to make the actual decisions and thus will remain professionally responsible for diagnostic and treatment decisions. [21,22]

A well-known industry analyst takes high technology companies to task for their approach to information systems in general; with regard to ES in particular, it is physicians (presumably in university computer labs) who are held responsible for the failed promise of expert systems:

…“The brilliant MDs designing these systems have trouble empathizing with the mass of physicians who are uncomfortable with computers or unwilling to abdicate their decision making to a machine. User-friendly expert systems that support doctors’ decision-making, instead of supplanting it, have yet to be designed.” [23]

## 5. Three limiting factors

The primary reason for the failure of expert systems to gain widespread acceptance by the medical community can be summed up as physician disinterest. To describe this phenomenon in marketing terms: ES technology is a solution (perhaps) lacking an agreed upon problem. Physicians, like many professionals, do not perceive that they have a deficiency of expertise or decision making ability within their own areas of specialty. In actual practice, when presented with an unusual or difficult case, they may call in a consultant physician for assistance with diagnosis and treatment planning. For a diagnosis which proves to be outside the original physician's area of expertise, it is highly unlikely that he or she would seek out a computer program for advice on how to manage the patient's care. Common practice dictates that such a patient be referred out to an appropriate specialist. In general, ES tool developers who view clinical problems as merely the absence of their particular solution(s) have not convinced physicians that such “advisors” (despite the more palatable term) can replicate, much less improve upon the quality of their decisions, given their eight or more years of medical education and training and countless hours of real world experience.

Moreover, any widespread clinical use of ES and other medical decision support systems, whether for advice prospectively or evaluation retrospectively awaits breakthroughs in medical informatics, i.e. standardization of medical nomenclature and electronic medical records $[24]$ , and storage and retrieval technology, e.g. optical disk imaging $[25,26]$ , as well as voice recognition technology (for narrative text portions of the medical record).

A second factor limiting the use of ES technology by healthcare providers has to do with current priorities in the allocation of limited resources. The top priority for hospital information systems today is database integration; 18 of 50 sessions were devoted to this and related HIS issues at the American Hospital Association's 1989 convention. When billing systems are fully integrated with care delivery recordkeeping and monitoring systems (via Medical Records and Quality Assurance departments), healthcare providers and managers may have the resources, the time, and the will to explore the promise of knowledge-based systems. At such time, the experience of some models will be of interest; for example, an integrated database at one large metropolitan hospital is being used in support of an “empirically-based decision-aiding system” which claims to be an improvement over the traditional rule-based expert system. [27]

The third factor that helps explain the virtual invisibility of ES technology in the clinical setting derives from the relatively new competitive market pressures affecting health services delivery: prompted by changes in federal reimbursement practices in the early 1980s, the healthcare industry has only recently become market-driven, and is really looking for business, and not clinical (or diagnostic) solutions. Hospital administrators are still trying to implement information systems to maximize reimbursement and become yet more cost efficient. Payors, led by the federal government, have been experimenting with attempts to control spiralling costs; these efforts have ushered in an era of “managed care”. Managed care as it developed in the 1980’s refers to alternative distribution systems, such as health maintenance organizations (HMOs) and preferred provider organizations (PPOs), which attempt to “contain” costs through combinations of capitated (fixed) payments, or discounted fee-for-service contracts, to networks of providers. (The federally funded Medicare system can thus be viewed as the nation’s largest PPO.)

Managed care has broadened to include various forms of utilization management or review, e.g., auditing for appropriate lengths of stay in hospitals, and for measures of quality such as the “medical necessity” of certain procedures prescribed by physicians. (Medical necessity is defined as clinical appropriateness, with appropriateness taken to mean when benefits to the patient outweigh the risks). In sum, employers, as the largest private bloc of purchasers of healthcare services, and insurance companies, as the major claims payors and risk underwriters, are attempting to manage costs by (1) requiring providers to share the financial risk of healthcare delivery, and (2) incentivizing employees through lower out of pocket copayments to seek care through networks of providers who contract to perform within certain cost and quality criteria.

Given these factors, we asked the following question: which players in the healthcare industry will be most likely to conceptualize clinical applications of ES technology as a business solution – and have the resources and information systems experience to explore this possibility?

In this context, one large insurance company has applied knowledge-based systems technology to address the costly problem of unnecessary healthcare services. Recognizing that health services research had shown that between 15–30% of selected procedures are performed inappropriately, Aetna Life and Casualty, based in Hartford, CT, applied some of its in-house expertise (derived from development of life insurance underwriting and other business solutions) to creating two utilization management programs to prospectively determine whether some ten inpatient and 19 outpatient procedures are in fact medically necessary as prescribed. The knowledge base and clinical decision logic are derived from practice guidelines developed by outside contractors who specialize in health services research and guideline development. Both programs are used by Aetna's utilization review nurses to certify medical necessity, or to refer the cases for further medical review, as patients and their physicians call to pre-certify the targeted procedures. (This certification is a requisite for payment, in accordance with the patient's health plan.)

The inpatient program in particular requires sophisticated technology to guarantee that procedures (for which there may be over 1,000 “clinical indications”) can be effectively logged in and discussed within a 5–7 minute telephone call. Aetna’s programmers customized the interface and added a version of induction technology to optimize the questioning process. Optimization determines the questioning strategy, producing the shortest possible path from initiation of call to certification or to review. [28]

## 6. Discussion

The use of knowledge-based technology in preventing unnecessary medical treatment, as described in the Aetna example, would seem to be an appropriate application conferring as it does most of the benefits of ES listed in section 3. This example also fits the criterion mentioned above, i.e. it is a business solution offering measurable fiscal benefits (dollars saved, revenue generated as utilization management becomes an add-on component of private health plans).

The trend toward utilization review (UR) by third parties, mediated by database and other innovative technology, seems sure to continue despite the protests of physicians. Other mechanisms have not worked, e.g. surgical second opinions (physicians tend to ratify the decisions of their peers, particularly within their own specialty) or hospital-based peer review (which helps to establish practice standards, but generally contends with errors retrospectively and is not designed as a cost containment strategy).

Our examination of this trend centered on three areas: (1) implications for the practice of medicine; (2) the reliability of the knowledge bases supporting UR services; and (3) alternative methodologies which could enhance effectiveness and make better use of the technologies involved.

(1) Implications for the practice of medicine. External monitoring by third party payors, while perceived by physicians as an unwelcome intrusion and at times capricious form of technological surveillance, reflects a growing demand for justification and documentation of diagnostic and treatment procedures. The UR phenomenon raises an interesting set of questions: Who all now control the practice of medicine? To what extent is it becoming employers and insurers, who now provide financial incentives to employees for selecting “preferred providers” and to physicians for adhering to appropriateness guidelines? To what degree is it insurers and managed care vendors who install computer-based protocols to assist UR nurses in the diplomatic, but rigorous oversight of the prescribing physician’s recommendations? And what of the risk issue? How will liability be partitioned among ES application developers, insurers, managed care companies, and providers? [29] Who will be responsible for updating these costly systems as new information becomes available? These and related questions will enter debates on healthcare delivery over the next several years.

(2) Knowledge base reliability. UR vendors and their medical staff defend their oversight criteria as clinically sound and scientifically valid, based upon public knowledge (the medical literature) and fine-tuned by in-house experts and/or outside contractors. The resulting knowledge bases are therefore proprietary and idiosyncratic, and are not subject to external scrutiny or regulation. Confidence in their reliability thus must assume that the proper conclusions have been drawn from a literature review, and that in-house experts have applied good judgment. Where ES/knowledge-based technology is used, the technical skills of the knowledge engineers must also be factored in. From a technologist's standpoint, confidence in such a system seems to depend upon many subjective factors, and often upon scant data. From a clinical standpoint, it is well known that the literature is sparse or silent in many areas, and contradictory in others.

Medical database developers and clinicians alike have reason to be encouraged by new initiatives which appear certain to enhance the reliability of these knowledge bases. We refer to the growing interest in and support for medical technology assessment and research on outcomes of medical treatment. For example, the U.S. government has funded outcomes studies for procedures performed on Medicare (primarily elder) patients, and its Agency for Health Care Policy and Research was authorized in 1989 to begin outcomes research in five key treatment areas (acute myocardial infarction, cataracts, prostate gland enlargement, low back pain, and total knee replacement), through the newly established Center for Medical Effectiveness Research. Optimally, knowledge gained through these inquiries will be made available to all providers and consumers of health care services. When medical appropriateness criteria are derived from outcomes studies of large and diverse populations, the credibility of proprietary UR systems will be enhanced. Because of the sheer numbers of patients involved, the opportunity exists for ES/knowledge-based technology to have a tremendous impact on the implementation of well-validated medical necessity criteria and practice guidelines.

(3) Alternative methodologies. If confidence in the knowledge base can be established, ES/KB systems can in theory mediate powerfully between a physician treating an individual and a body of medical wisdom based on many similar cases. In practice, physicians claim their judgment is being second-guessed by people on the other end of the telephone who often have less clinical expertise than they themselves do.

The need for UR oversight seems justified by both cost and quality considerations. The logic of keeping UR criteria and supporting technology at arms length from providers, however, is not obvious from an operational or management point of view. We wondered why payors could not instead download their knowledge base and/or assessment criteria to physicians' offices or to hospitals. Physicians could then prospectively gather supporting documentation, and proactively log in their treatment authorization requests. This could reduce the processing time for payors, and make the administrative burden more tolerable for physicians.

This approach has appeal for at least two reasons: (1) it is in keeping with current performance evaluation practices in the business community to provide clear and specific criteria by which performance will be measured; and (2) distinctions between insurers' and practitioners' roles could be better maintained. It should be recalled that insurers are not providers of healthcare services by training or intent; what they do best is calculate risk, set and collect premiums, process and pay claims. In other words, insurers handle the cash flow for the employee health cost line item in employers' operating budgets.

Moreover, physicians have asserted that they should have input into the criteria by which they are being “profiled”; this is another sound management principle. If, as in this scenario, physicians were able to access the explanation facility of an ES developed by a payor/UR vendor, points of dispute could be objectively identified. End users could have immediate and ad hoc input regarding these criteria, providing additional data for knowledge base developers to consider when updating their UR protocols. Changes in practice standards and updates of medical appropriateness criteria could be disseminated efficiently.

## 7. Summary and recommendations

This inquiry was inspired by curiosity about the extent to which ES and AI technology had impacted the clinical practice of medicine. We considered the points of view of three possible end users: physician, hospital, and third party payor. Three factors were advanced to explain the current state of ES/knowledge-based system utilization in the healthcare industry. In summary:

(1) For the vast majority of physicians, computer consultation is an alien, unwanted, and unnecessary addition to the conventional practice of medicine, offering neither clinical benefits, increased revenue potential, nor time savings. The earlier, pioneering institutional experiments have led, however, to the establishment of a small but active niche of physicians interested in medical informatics. The resulting “boutique” applications, primarily housed in teaching hospitals, are customized to local problems and tasks, with no commercial intent or exportability;

(2) Most hospitals are probably years away from the integrated information systems configurations that will truly meet their needs. Clinical decision support systems may be inserted into some functional areas (e.g. labs, bedside monitoring equipment, etc.) where operational efficiencies may result. In general, technology that is not demanded by physicians for optimal patient care, or by managers for better documentation or cost efficiency, will not be a priority for this group;

(3) Third party payors were identified as the most likely group to support ES/KB system development, for business rather than clinical reasons. Much is now expected of utilization review as a managed care strategy: the marriage of innovative information systems technology and health services research on outcomes of medical treatment is supporting this fast-growing segment of the healthcare industry. Since the changing of reimbursement policies does affect practice patterns and patients' decisions, overly stringent utilization management and review protocols are vulnerable to litigation. ES and knowledge-based systems applied in the delivery of UR services have the potential to make great contributions, through the widespread dissemination and efficient updating of practice standards embedded in the knowledge base. At the same time, the issue of shared liability in the event of adverse outcomes has yet to be resolved.

The use of ES/KB technology to optimize and rationalize the implementation of utilization review protocols or practice standards may or may not be welcomed as a promising development, depending on one's point of view. We conclude with these recommendations for where to look for other future applications:

(1) Document searching. The trend toward greater accountability has led to exponential increases in the volume of documentation required to secure reimbursement and/or meet quality standards. New technologies offer better ways to manage this administrative burden. [26] Once medical records are computerized and storage/retrieval technology is installed, AI/ES may be useful in the form of document searching applications;

(2) Online database searching. Work is well underway in this area, which includes applications for database selection and “intelligent” information retrieval, as performed either by end users themselves, or mediated by “search analysts” (medical librarians, etc.). [30] We surmise that this sort of application may gain more ready acceptance by physicians than would clinical decision support systems, particularly if the search could be delegated to competent information scientists; and

(3) Operational problem-solving, e.g. triage, case management, and otherwise optimizing the sequence of events during an episode of care.

In other words, we would expect to see more applications with both appropriate problem selection, and non-physician end users. With the objective of greater coordination of care, system developers will need to focus on the standardization and integration of patient databases as well as on the conceptual marvels of ES.

## References

[1] Elam, Joyce J. and Henderson, John C. Knowledge Engineering Concepts for Decision Support System Design

and Implementation. Information and Management, 6 (1983) 109–114.

[2] Ford, F. Nelson. Decision Support Systems and Expert Systems: A Comparison. Information and Management, 8 (1985) 21–26.

[3] Beheshtian-Ardekani, Mehdi and Salchenberger, Linda M. An Empirical Study of the Use of Business Expert Systems. Information and Management, 15 (1988) 183-190.

[4] O'Keefe, Robert M. The Evaluation of Decision-Aiding Systems: Guidelines and Methods. Information and Management, 17 (1989) 217–226.

[5] Berztiss, Alfs T. Software Methodologies for Decision Support. Information and Management, 18 (1990) 221-229.

[6] Zadeh, Lofti A. Fuzzy Sets. Information and Control, 8 (1965), 338–353.

[7] Zadeh, L.A. The Birth and Evolution of Fuzzy Logic. International Journal of General Systems, 17 (1990), N2–3: 95–105.

[8] Zadeh, L.A. Fuzzy Sets and Systems. International Journal of General Systems, 17 (1990), N2–3: 129–138.

[9] Feigenbaum, Edward, Nii, H. Penny, and McCorduck, Pamela. THE RISE OF THE EXPERT COMPANY. New York: Times Books/Random House, 1988. With Introduction by Tom (In Search of Excellence) Peters, and Appendix by Paul Harmon.

[10] Evans, Stevens. A Clinical Tool for Nursing. Computers in Healthcare, August 1988.

[11] Morgan, John, Ph.D. and Slivka, Scott. Benefitting from Expert Systems. Computers in Healthcare, January 1988.

[12] Warner, Homer R. What You Don't Know Can Hurt You. Computers in Healthcare, March 1988.

[13] Durham, James D. Market Forces Drive Growth. Computers in Healthcare, June 1988.

[14] Expert Systems and Medicine: Expert Systems and Computers (Pacing, Cardiology, Diabetes). Abstracts from presentations at the 6th International Congress "CARDIOSTIM 88", Monaco. PACE (Pacing and Clinical Electrophysiology), Vol. 11, No.6 Part II, June 1988.

[15] Computer Aids Psychiatric ER Triage. Computers and Medicine, April 1989, p. 7.

[16] Sear, A.M. An Expert System for Determining Medicaid Eligibility. Journal of Medical Systems, Vol. 12, No. 5, October 1988.

[17] Brooks, Martin. Accounting ES Aids Health Care. Applied Artificial Intelligence Reporter, Vol. 4, No. 4, April 1987. (Published by the Univ. of Miami's Intelligent Computer Systems Research Institute)

[18] The Future of Healthcare: Changes and Choices. Arthur Andersen and Co. and the American College of Healthcare Executives, 1987, p. 24.

[19] Lewellen, T.K. and Bice, A.N. Computers in Medicine. Investigative Radiology, Vol.23:857–865, November 1988.

[20] Davis, Jerome A. and Ladd, Ronald D. Computer Aided Medicine. U.S. Healthcare, July 1989.

[21] Fliegel, Tova F. Knowledge-Based Systems: Trying to Define a Role That's Wise. Healthweek, June 11, 1990.

[22] Young, F.E. Validation of medical software: Present Policy of the Food and Drug Administration. Annals of Internal Medicine 106 (1987) 628–629.

[23] Herzlinger, Regina E. The Failed Revolution in Health Care – The Role of Management. Harvard Business Review, March–April 1989.

[24] Gabrieli MD, E.R. and Murphy, Gretchen. Computerized Medical Records. Journal of American Medical Records Assoc. Vol.61, No.1 January 1990.

[25] McLendon, Kelly. Optical Disk Imaging – Tomorrow's Technology for Today's Medical Records. Journal of American Medical Records Assoc. Vol.61, No.2 February 1990.

[26] Randall, Arthur M. The Optical Disk: a Medical Record Breakthrough. Topics in Health Record Management Vol. 9, No. 2 December 1988.

[27] Walker, H. Kenneth, M.D. Grady Memorial's Integrated Database Improves Speed, Accuracy and Cost Containment. Computers in Healthcare, March 1989.

[28] Scheibner, Irene and Winslow, Constance M. Does Mr. Jones Need Bypass Surgery? Best's Review, March 1990 (and conversations with the authors).

[29] Koco, Linda. 'Programs' Can Turn Into 'Industries'. National Underwriter, June 25, 1990.

[30] Hawkins, Donald T. Applications of Artificial Intelligence (AI) and Expert Systems for Online Searching. Online, January 1988.
