---
otero_id: 20899
otero_key: "HREMA7EY"
title: "Information systems architecture to support managed care business processes"
authors: "Amitava Dutta; Shyam Heda"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00098-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information systems architecture to support managed care business processes

Amitava Dutta <sup>a,)</sup>, Shyam Heda <sup>b</sup>

Department of Decision Sciences and MIS, School Management, George Mason UniÕersity, 4400 UniÕersity DriÕe Fairfax VA 22030, USA

InoÕa Health System, Springfield, VA 22151 USA

## Abstract

Escalating costs have forced dramatic changes in the healthcare industry, with a move towards managed care. Managed care seeks to integrate healthcare delivery processes and continuously improve them through feedback based on evaluation of care outcomes. The success of managed care depends critically on the collection, analysis and seamless exchange of information within and across organizational borders. This paper examines the business processes unique to managed care, and identifies its architecture requirements. We find that in addition to interorganizational networking, the architecture must provide sophisticated decision support capabilities. Historically, the emphasis of decision support in healthcare has been on clinical applications. Our examination shows that in the new managed care environment, it is equally important to also provide decision support for i specific nonclinical aspects of care delivery ii outcome analysis and iii continualŽ . Ž . Ž . refinement of care protocols to enhance cost-effectiveness. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Managed care; Data standards; Decision support architecture; Outcome analysis

## 1. Introduction

The US healthcare industry has been going through extensive reforms driven primarily by escalating costs 7 . One major reform has been the trend <sup>w</sup> <sup>x</sup> towards some version of Amanaged careB instead of Afee-for-service.B The delivery of healthcare has always been information intensive, and there are signs that the industry is recognizing the increasing importance of information processing in the new managed care environment 22 . A significant segment of<sup>w</sup> <sup>x</sup> healthcare IS executives view the move towards managed care as the biggest force driving healthcare automation 27 . Influential US technology com-<sup>w</sup> <sup>x</sup> panies, such as Ameritech, Bell Atlantic, and Westinghouse, are entering the healthcare information processing market and the European Community is attempting to coordinate healthcare informatics research and development across its members 18 .<sup>w</sup> <sup>x</sup>

In this paper, we identify major differences in business process between fee-for-service and managed care environments. This analysis will show the need for i networking for exchanging clinical and Ž . nonclinical information among disparate organizational entities in real time and ii decision supportŽ .

for real-time and off-line analysis of collected data for healthcare operations and management. Our discussions are based on the actual experience and actions of InoÕa Health System, a major healthcare provider in the Northern Virginia area.

## 2. Industry trends in healthcare delivery

The fee-for-service paradigm arose after World War II and took root with the establishment of Medicare in 1965. Care providers were reimbursed for costs, and there was little control. Healthcare costs rose steadily and represented over 11% of GNP by 1988. The industry began facing increasing pressure to cut costs and the Amanaged careB paradigm emerged. Currently, this trend towards managed care is the most influential driver of change in the industry.

Fig. 1 summarizes important differences in Abusiness processesB between the two environments. Three communities are central to both — i patients ii Ž . Ž . insurance companies and iii healthcare providers.Ž . However, the contractual relationships are drastically different in the two environments, resulting in very different business processes.

In the traditional fee-for-service model shown on top, patients contract with an insurance company for health coverage. When care is needed, patients choose a physician who starts the care process. If necessary, they see specialists and<sup>r</sup>or use hospital services. Physicians, hospitals and other care providers are subsequently paid by the insurance company for each instance of service they perform. Patients had minimal restrictions in selecting care providers, and physicians had minimal oversight of treatment plans. Insurance companies bore the full financial risk of covering patients.

The managed care environment is depicted in the bottom half of Fig. 1. As before, patients contract with an insurance company for health benefits. Now however, proÕiders are also required to participate in one or more insurance plans. Providers are reimbursed only when they participate in a plan in which the treated patient is enrolled. Furthermore, every patient is required to select a APrimary Care PhysicianB. All care is coordinated by the PCP whose practice is monitored by the insurance company.

Insurance authorization is needed before proceeding with specialized or costly treatment plans. With managed care, the financial risk of covering patients is shared with healthcare providers. In discounted-feefor-serÕice contracts, providers discount their fees for that plan’s enrolled patients. Under capitated contracts, which are becoming more prevalent 11 , insurers agree to pay providers a fixed amount for each life that is covered, regardless of actual costs incurred. This provides providers with very strong incentives to continually monitor care outcomes and streamline care delivery 2 .<sup>w</sup> <sup>x</sup>

From a process viewpoint, managed care requires integrated delivery of care across different providers. There is also a much greater degree of control and supervision exercised by the insurance company and the PCP. This is very different from the fee-forservice environment, where the relationship between insurance companies and providers was primarily a financial one, and the concept of PCPs authorizing and coordinating care was nonexistent.

## 3. Information processing needs

In this section, we determine the information processing requirements implied by the business processes of managed care. Fig. 1 shows that for managed care, there needs to be a seamless flow of clinical and nonclinical information within and across the boundaries of multiple organizations. Current practice does not lend itself to such exchange. For example, most physician offices automate only their patient billing and scheduling activities while clinical information is mostly paper-based. Hospitals and insurance companies have often built customized systems, which hamper information exchange. Additionally, there are inadequate standards for measuring and recording healthcare information, making it becomes difficult to interpret or compare measures across different organizations. Clearly, this is a recipe for incompatibility, inefficiency and error.

Managed care also requires eÕaluation of the care process for continuous improvement. Therefore, in addition to clinical and financial data, it is now necessary to maintain additional information on resource utilization and treatment outcomes. Process improvements require that outcomes of medical

![](/api/attachments/HREMA7EY/fulltext/images/6c63cc2594f1055a5044da7b7285a2ab6a18bb46e0112ea84a85f1dfee545a8e.jpg)  
Fig. 1. Comparison of managed care and fee-for-service.

treatment be recorded accurately and then analyzed, and we are seeing increased use of decision support technology in managed healthcare 23 . In fact, it is<sup>w</sup> <sup>x</sup> the analysis of care outcomes that closes the infor-

Integrate IT Plan and Business Strategy

![](/api/attachments/HREMA7EY/fulltext/images/694ff78e29a6af1111432b8e8e5785b4aa6043c8e48288235428303244471bb5.jpg)  
Fig. 2. Integrating healthcare IT plan with business plan.

mation feedback loop in managed care. Hospitals or Physician–Hospital–Organizations PHOs accepting Ž . capitation arrangements will need to capture and analyze additional data resembling that recorded by insurance companies. In short, the importance of decision support in the delivery of managed healthcare can hardly be overemphasized 13 Figs. 2–4 . <sup>w</sup> <sup>x</sup> Ž .

## 4. Information systems architecture

In this section, we describe an architecture to meet information processing needs identified in Section 3. In doing so, we will use the experience of Inova Health System as an example. Inova is located across the Potomac river from Washington, DC in Fairfax county. It budgeted about US\$60 million between 1993 and 1997 for information and communications systems, and has developed a strategic plan for IT deployment to transform the organization from a community hospital system to an integrated healthcare delivery system.

The IT architecture developed by INOVA resulted from strategic planning, during which senior executives ensured that the IT plan was aligned with business objectives and supportive of Inova’s com-

![](/api/attachments/HREMA7EY/fulltext/images/a5c208653247911067772bf6cccfb4479db6c0a3ec2c56715abcda283f00a454.jpg)  
EIS: Executive Information System RCN: Regional Communications Network CPR: Clinical Patient Record  
Fig. 3. Relating business requirements with architecture components.

# Overall IS Architecture

![](/api/attachments/HREMA7EY/fulltext/images/357b8a2b62f5d1973bd7434582a7703f5a67e7f5880e6665e48a0475a9f1bf1b.jpg)  
Fig. 4. Major components of healthcare IT architecture.

petitive strategy. Such alignment is essential to successfully leverage IT for competitive advantage 1 . For brevity, we do not report details of the strategic planning process, but the general steps appear in Fig. 2. Since implementation of the IT architecture would span multiple years and there were yearly budget constraints, it was necessary to prioritize different architectural elements. This was done by classifying the impact of different components on business objectives. Fig. 3 summarizes this exercise, and we do not describe it further.

Inova’s IT architecture appears in Fig. 4. Many of those components are generic to most managed care environments and we elaborate on them now. Notice the central role of networks. Fig. 4 shows three levels of networks — Data Center Network DCN ,Ž . Enterprise Network EN and Regional Communica-Ž . tion Network RCN . The DCN integrates differentŽ . transactional systems — such as clinical care, radiology, patient accounting and laboratory work. As a result of care delivery, a clinical data repository consisting of Computer-based Patient Records Ž . CPRs is created. The DCN, therefore, supports functional integration in the delivery of care. The EN extends this functional integration to different physical sites that are part of the same healthcare organization. Inova, for instance, consists of multiple hospitals, nursing homes and other care centers spread out across Northern Virginia. These two network components are under control of one organization. The third component, the RCN, is an interorganizational system. It connects Inova to Employers, Payers, suppliers, physician offices and other non-Inova hospitals. It is essential for delivery of managed care, and was much less significant in the older fee-forservice setting. Interorganizational networks, such as the RCN, are notoriously difficult to set up and manage, as has been evident in other industries 1,Ž<sup>w</sup> Chap. 4 , 28 . In short, the networking elements of<sup>x</sup> <sup>x</sup> the architecture help meet the first requirement identified in Section 3 — the seamless exchange of healthcare information within and across organizational boundaries.

## 5. The role of decision support systems DSS ( )

The architectural component needed to meet the second requirement identified in Section 3 is DSS. One indication of the pervasive role of decision support in managed care is the number of such products currently being offered or under development for all aspects ranging from accounts receivable analysis to clinical protocoling 14,15 . In this<sup>w</sup> <sup>x</sup> section, we elaborate on the role of decision support and give some specific examples. For ease of reference, the different steps in managed care have been labeled A through F in Fig. 1. Unlike the fee-forservice environment, each of these steps depends on complex analyses of healthcare data that is being continually accumulated through the network infrastructure shown earlier in Fig. 4. Broadly viewed, DSS are used to analyze the profit potential of current and new health insurance plans, review utilization of costly healthcare resources, develop benchmarks for quality of care and costs, and to improve cost effectiveness of the care delivery process through continuous monitoring and feedback of medical outcomes. These analyses have to be performed by insurance companies as well as healthcare providers. We now proceed to described some specific decision support scenarios with reference to Fig. 1.

## 5.1. Specific decision support scenarios

Activity AAB in Fig. 1 represents the act of a customer choosing to enroll in one or more insurance plans. Insurance companies often develop customized plans for large employee groups that are tailored to the group profile. Decision support for profitability analysis is crucial in designing and marketing these plans. Further, although employees are the primary users of the health plan, insurance companies generally market plans to the employer — not individual employees. Employers may want to see performance statistics on such things as current customer satisfaction, physician competence and experience, hospitals’ quality of care, etc. The insurance company needs to be able to analyze existing transactional data to provide such analysis to employers.

One of the decision support activities that affects several different steps in managed care is Aoutcome analysis.B The intent is to measure, and perhaps codify, the cost effectiveness of different levels of care. For example, statistical analysis of medical outcomes may indicate that the recovery rate of alcoholics from rehabilitation programs does not increase significantly after a stay of 1 month. Therefore, the insurance company may decide not to pay for stays longer than 1 month. Alternatively, outcome analysis may indicate that current treatments Ž . such as bone marrow transplants of certain serious illnesses have very low success rates, while also being very costly. They may decide to exclude those treatments from covered benefits, or require considerable scrutiny before authorizing treatment. Clearly, outcome analysis has a major impact on step AAB in terms of deciding premiums and levels of medical benefits in different plans. It also has far reaching effects on other steps as will be described below.

In activity AB,B customers choose their primary care physicians, specialists and hospitals from within an authorized set of care providers who participate in their plan. Currently, there is little publicly available hard data on which customers can base this decision, but there are moves underway in the healthcare industry to develop standards for performance comparison 16 . DSS will improve the ability of care<sup>w</sup> <sup>x</sup> providers to produce such performance measures, and of employers and patients to make judicious choices of providers based on comparative analysis of such measures.

Activity ACB consists of different healthcare providers such as hospitals, general practitioners Ž and specialists choosing to ‘participate’ in health . plans. The decision to participate is a mutual one between care providers and the insurance company, and requires financial analysis by both parties. This analysis becomes particularly complex under capitation and other risk sharing arrangements, and resembles that performed by financial institutions involving actuarial data and risk assessments. A DSS can also help executives continually monitor whether their managed care contracts are delivering the number and mix of patients that are consistent with the profitability of participating in different plans 4 .

Step ADB includes all activities associated with the actual delivery of care by providers to patients. Therefore, the decision support activities in this step are focused on providing the analysis, real-time as well as off-line, necessary to continually improve the cost-effectiveness of care delivery. One example of real-time decision support, is in assisting with the task of demand management 3 . This is basically a <sup>w</sup> <sup>x</sup> process of using nurses to triage patients who call in with symptoms, so as to match their symptoms with the most appropriate level of care. Clearly, this is a diagnostic activity, and DSS are already being deployed to help nurses offer advice and perform triage in certain specialty areas such as prenatal care and chronic illnesses 10 . The assumption is that this <sup>w</sup> <sup>x</sup> advising and triage will reduce medical costs without sacrificing quality of care, since medically trained personnel are determining the initial level of care as opposed to untrained patients. There have been other decision support technologies that have been developed to provide real time assistance with care delivery, but there is considerable reluctance among physicians to actually use them.

A major component of off-line decision support in step ADB consists of outcome analysis for a variety of purposes. One is to provide comparative analysis of internal performance measures vs. key competitors 26 . Software is available to analyze publicly <sup>w</sup> <sup>x</sup> available transactions data to establish these comparative norms 6 . While this performance comparison <sup>w</sup> <sup>x</sup> is also relevant to step $\mathbf { \ddot { c } } \mathbf { \vec { C } } ^ { 5 }$ as mentioned earlier, in step $ { ^ { 6 } \mathrm { \Delta T } } ,  { ^ { \circ } }$ it provides high level drivers for the feedback process — i.e., process changes resulting from feedback should ultimately drive internal performance measures closer to or beyond industry norms. Software that analyzes computerized patient records to monitor quality of care, detect outcome trends, etc., are already available from vendors 8 .<sup>w</sup> <sup>x</sup> The department of health and human services has recently released a computer tool allowing users to collect and assess clinical performance 6 .

A second major objective of off-line outcome analysis is to develop Aclinical pathways.B These are maps of the course of medical interventions and their expected outcomes, which balance standards of care against the resources necessary to provide them. Clinical pathways help to standardize practice protocols and reduce costs without sacrificing quality of care 9,17 . During one study in Cincinnati, for <sup>w</sup> <sup>x</sup> example, analysis showed that there was a 300% variation in the diagnostic tests ordered for cardiac arrest cases 20 .<sup>w</sup> <sup>x</sup>

Notice that managed care improvements in step ADB requires clinicians and administrators to sit down together to analyze the relationship among clinical practice, care outcomes and finances. This requires a new and different type of decision support, one which has not been explored extensively in the literature. A model of this collaborative effort needs to be developed and then group DSS can be built on that foundation 19 . It is this collaborative decision-mak-<sup>w</sup> <sup>x</sup> ing involving clinicians and administrators that will improve profitability while maintaining care quality <sup>w</sup> <sup>x</sup> 5,9 .

Steps AFB and $\mathbf { \ddot { G } } ^ { \ 5 }$ in Fig. 1 involve the submission of claims by providers and subsequent payment by insurance companies. As such, these two steps depend more on transaction processing capability rather than decision support. However, step AEB can benefit from decision support because it requires some analysis of the utilization of medical resources implied in the treatment plan that has been submitted for authorization 25 . This analysis is complicated<sup>w</sup> <sup>x</sup> by the fact that quality and cost norms must be applied to individual patients with specific medical histories. To manage authorization efficiently, the insurance company’s medical director can use DSS to perform the analysis needed to develop referral policies. The system can also be used to identify exception situations that need further scrutiny.

In order for DSS to achieve their full potential impact on the practice of managed care, certain industry-wide challenges must also be met. These challenges were considerably less urgent in the era of fee-for-service, when detailed medical information on patients usually stayed within organizational boundaries, and was not subject to such extensive analysis and comparison. In Section 6, we mention some of these issues and associated recent developments.

## 6. Some industry-wide it challenges

The major challenge is that relating to data standards, which, in turn, has a major impact on the quality of data being analyzed. One of the biggest problems is Apositive identificationB of patients, i.e., how can one be sure that two medical records are of the same person. This is critical when aggregating patient data across multiple organizations. Simple things, such as test results, are sometimes reported in different ways by different laboratories. Definitions are fuzzy and data is often incomplete. This lack of standards is a major hurdle for interorganizational information exchange. Furthermore, without industry wide standards for reporting medical information, performance comparisons of different plans or providers is meaningless. However, some standards are beginning to emerge. The Healthcare Financing Association HCFA is adopting national EDI stan-Ž . dards for electronic claims processing 21 . Ques-<sup>w</sup> <sup>x</sup> tions are being raised about popular healthcare quality report cards comparing managed care plans. These are based on internal measures of quality and efficiency. Customers are demanding some form of standardization. In this context, Health Plan Employer Data and Information Set HEDIS 2.0 may Ž . become the managed care industry’s standard for measuring future performance 12 . Other quality of <sup>w</sup> <sup>x</sup> care performance measures are being proposed 16 . Nevertheless, much remains to be done inn the area of data standardization.

Overarching all of these are the issues of security and confidentiality 29 . The public has a very real <sup>w</sup> <sup>x</sup> fear of various forms of discrimination that may occur if this automated information gets into the AwrongB hands. It is unlikely that these issues will be resolved through industry action and regulatory action will probably be necessary 24 .<sup>w</sup> <sup>x</sup>

## 7. Conclusion

DSS will play an increasingly widespread role as the healthcare industry moves towards the managed care paradigm. In this paper, we have identified two major architectural components that will be needed to meet the information processing needs of this changed environment. One is the need for intra- and interorganizational networks. They will provide the connectivity needed to offer integrated care across disparate care delivery facilities. Second, a variety of decision support capabilities will be necessary to increase the productivity of medical personnel, analyze care outcomes, and continually refine care delivery processes to remain profitable while holding the line on costs and maintaining quality of care. In the short-term, these decision support systems DSS Ž . will be targeted towards management functions, with clinical applications being targeted at a subsequent time. However, networks and DSS will not be adopted, and we will not derive their full benefits, until the industry addresses data standardization issues and there is further legislative progress on the privacy issues.

## References

<sup>w</sup> <sup>x</sup> 1 L. Applegate, W. McFarlan, J.L. McKenney, Corporate Information Systems Management: Text and Cases, Irwin, Boston, 1996.

<sup>w</sup> <sup>x</sup> 2 A.C. Bartling, Trends in managed care, Healthcare Executive 10 2 1995 6–11.Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 W.H. Bell, Telephone based demand management: what you need to know, Healthcare Strategic Management 14 2Ž . Ž .1996 6–8.

<sup>w</sup> <sup>x</sup> 4 J. Brice, Decision support, Healthcare Forum 32 2 1989 Ž . Ž . 19–26.

<sup>w</sup> <sup>x</sup> 5 S. Butters, S. Eom, Decision support systems in the healthcare industry, Journal of Systems Management 43 6 1992Ž . Ž . 28–31.

<sup>w</sup> <sup>x</sup> 6 G.R. Campbell, DHHS releases innovative performance measurement tool, announces managed medicare initiative to rate plan quality, Managed Healthcare 6 5 1996 15.Ž . Ž .

<sup>w</sup> <sup>x</sup> 7 M. Clare, D. Sargent, R. Moxley, T. Forthman, Reducing health care delivery costs using clinical paths: a case study on improving hospital profitability, Journal of Health Care Finance 21 3 1995 48–58.Ž . Ž .

<sup>w</sup> <sup>x</sup> 8 R. Coile Jr, Assessing healthcare market trends and capital needs: 1996–2000, Healthcare Financial Management 49 8Ž . Ž . 1995 60–65.

<sup>w</sup> <sup>x</sup> 9 Computer software for decisions and utilization review, Federation of American Health Systems Review 21 4 1998Ž . Ž . 50–52.

10 L. Drapin, Demand management links consumers, Information to Healthcare, Management Technology 16 9 1995Ž . Ž . 8–12.

<sup>w</sup> <sup>x</sup> 11 R. Fromberg, Capitation is Coming, Healthcare Executive 11 Ž . Ž . 1 1996 4–9.

<sup>w</sup> <sup>x</sup> 12 G. Halpern, Measuring pharmacists via HEDIS, Managed Healthcare, PharmaCare Economics Supplement 1996Ž . S39–S41, Mar .Ž .

<sup>w</sup> <sup>x</sup>13 D.A. Hampshire, B.J. Rosborough, The evolution of decision support in a managed care organization, Topics in Health Care Financing 20 2 1993 26–37.Ž . Ž .

<sup>w</sup> <sup>x</sup> 14 HCm Products; http:<sup>rr</sup>www.hcm-inc.com<sup>r</sup>HCMPROD. NSF.

<sup>w</sup> <sup>x</sup>15 JJO Enterprises, Innovative Solutions for Healthcare; http:<sup>rr</sup>www.jjo.com<sup>r</sup>prod02.htm.

<sup>w</sup> <sup>x</sup> 16 R. Kazel, Measuring quality of care, Business Insurance 30 Ž . Ž . 27 1996 pp. 3, 34.

<sup>w</sup> <sup>x</sup> 17 M.B. Kilmer, Clinical pathways can help manage managed care, Healthcare Financial Management 51 2 1997 40–43.Ž . Ž .

<sup>w</sup> <sup>x</sup> 18 J. Mantas, The application of advanced information technology in medicine and health care: a European approach, International Journal of Technology Management 7 6 1992 Ž . Ž . 560–571.

<sup>w</sup> <sup>x</sup> 19 L.F. McMahon Jr., A.M. Eward, A.M. Bernard, R.A. Hayward, The integrated inpatient management model’s clinical management information system, Hospital and Health Services Administration 39 1 1994 81–92.Ž . Ž .

<sup>w</sup> <sup>x</sup> 20 J. Miller, Outcomes and bottom lines, Managed Healthcare 4 Ž . Ž . 10 1994 30–32.

<sup>w</sup> <sup>x</sup> 21 J.J. Moynihan, A milestone for paperless claims processing, Healthcare Financial Management 50 1 1996 68–69.Ž . Ž .

<sup>w</sup> <sup>x</sup> 22 J. Morrissey, Managed care steers info systems, Modern Healthcare 25 8 1995 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 23 J. Nunnelly, Decision-support software clarifies cost, revenue division, Health Management Technology 17 7 1996 44.Ž . Ž .

<sup>w</sup> <sup>x</sup> 24 M. Pretzer, Why you should have been at the health lawyer’s convention, Medical Economics 73 16 1996 160–168.Ž . Ž .

<sup>w</sup> <sup>x</sup> 25 M.J. Schlesinger, B.H. Gray, K.M. Perreira, Medical professionalism under managed care: the pros a and cons of utilization review, Health Affairs 16 1 1997 106–124.Ž . Ž .

<sup>w</sup> <sup>x</sup> 26 R.B. Siegrist, Knowledge, power and comparative information, Health Management Technology 17 13 1996 66.Ž . Ž .

<sup>w</sup> <sup>x</sup> 27 R.L. Simpson, Trends in health-care computing according to CIOs, Nursing Management 26 8 1995 20–21.Ž . Ž .

<sup>w</sup> <sup>x</sup> 28 SWIFT reviews standards strategy, Cash Management News 112 1995 1–2.Ž .

<sup>w</sup> <sup>x</sup> 29 D.J. Weissburg, Managed care organizations and confidentia patient information: the need for a uniform standard, Journal of Health Care Finance 21 4 1995 42–46.Ž . Ž .

Amitava Dutta holds the LeRoy Eakin Chair in Electronic Commerce and is Professor of Management Information Systems in George Mason University’s School of Management. He received his PhD in Management Information Systems from Purdue University, and a B. Tech. in Electronics and Telecommunications Engineering from the Indian Institute of Technology. His papers have appeared in leading journals including Operations Research, Management Science, IEEE Transactions and IIE Transactions. Dr. Dutta serves on the editorial boards of several IS journals and is an international fellow in Electronic Commerce at the Korea Advanced Institute of Science and Technology. He has consulted with and conducted executive education courses for several technology organizations and the federal government.

Shyam Heda was the Vice President of Information Systems at Inova Health System in Springfield, VA at the time this paper was written. Prior to this position, he was Vice President of Information Systems at Bethesda Hospitals in Cincinnatti, OH. He earned his MS degree from the University of Michigan and his Bachelor of Engineering degree in India. Mr. Heda is the President of ACHIA and was the chairman of the Planning Committee. He has served as the President and on the Board of Directors for the Information Systems Society of the Ohio Hospital Association. Mr. Heda has published many articles related to the healthcare industry and has made presentations at many healthcare professional conferences and seminars.
