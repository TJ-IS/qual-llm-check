---
otero_id: 19236
otero_key: "MQB9863X"
title: "Managing software quality in a very large development project"
authors: "Dien D. Phan; Joey F. George; Douglas R. Vogel"
year: "1995"
journal: "Information & Management"
doi: "10.1016/0378-7206(95)00032-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Case study

# Managing software quality in a very large development project

Dien D. Phan ${}^{a,*}$ , Joey F. George ${}^{b}$ , Douglas R. Vogel ${}^{c}$

$^{a}$ Business Computer Information Systems Department, St. Cloud State University, St. Cloud, MN 56301, USA $^{b}$ Information & Management Sciences Department, Florida State University, Tallahassee, FL 32306, USA $^{c}$ Management Information Systems Department, University of Arizona, Tucson, AZ 85721, USA

## Abstract

Control of quality remains a major challenge in software project management. Although there has been some research in the management of software development projects, very few studies have investigated the management and control of the quality of the software created, especially in large-scale development projects. During the development of OS/400 R.1 at IBM Corporation, thousands of programmers were involved in writing and refining millions of lines of code. Such an effort would fail without good software quality management. Using measurement derived from the literature, this study was able to verify the high quality of the OS/400 software based on rigid quality assurance strategies used in the project.

Keywords: Software project management; Software quality; Fault; Failure; Defect; Defect removal efficiency

## 1. Introduction

Software investment has grown rapidly during the past decade. With fierce global competition causing financial setbacks for many computer hardware manufacturers, the U.S. computer industry is gradually reducing its investment in building computer hardware while increasing investment in building software $[18]$ . However, despite recent and ongoing efforts to enhance the processes and techniques used in the management of software projects at all stages in the systems development life cycle, controlling software quality remains one of the most neglected areas.

Although the costs of controlling and improving software quality rank among the top expense elements in software development projects [11], so far inadequate and insufficient empirical studies on software quality have made it difficult for project managers to find up-to-date benchmarks and appropriate strategies in management and control of software quality.

Some of the critical quality management and control issues in software development projects include: 1. How can defects and quality be controlled? What are the available strategies?

2. What are the benchmarks for measurement and evaluation of quality and service before and after delivery? What are the ratios of test code and data and of re-used code over the total amount of code delivered to end user?

3. What are the relative costs for late removal of defects?

This paper addresses key quality management and control issues in large development projects using, as a case, IBM's OS/400 R.1 project.

## 2. Software quality management concepts

Despite numerous efforts at defining and measuring software quality in the past decade, the management of software quality remains in its infancy and the quality concept is still not well-defined. As Weinberg [19] stated: “Quality is relative. What is quality to one person may even be lack of quality to another.”

The most widely accepted definition of quality, taken from the recent ISO 8402 standard, is “the totality of features and characteristics of a product or service that bear on its ability to satisfy stated or implied needs” [13]. Other ways of defining the domain include Musa et al. [14] who argue that reliability is the most important characteristic in software quality. The official definition of software reliability from the IEEE Standard Glossary of Software Engineering Terminology [9] is “the probability of failure-free operation of software components or systems in a specified environment for a specified time.” In general, the predominant measure of software quality is the counting of known faults at various points in the software development life cycle [13]. The widely accepted definition of software fault (the cause) and failure (the result) is:

1. A failure is the departure of the external results of program operation from requirements.

2. A fault is the defect in the program that, when executed under particular conditions, causes a failure. Since there are many sets of conditions that cause failure, a fault can be the source of multiple failures [14].

In order to improve competitiveness and to comply with new production quality requirements, such as those of Malcolm Baldrige National Award and ISO 9000 series (see appendix), many business firms collect quality data and introduce quality prediction techniques into management processes. They also build quality models to improve reliability predictions.

The major task in improving software quality is to minimize the number of faults or defects that exist during and after development. Based on the time of injection and detection, Jones [10] classifies defects into various categories: requirements, design, coding, documentation, administrative, and bad fixes. Requirements, design, coding, and documentation defects are injected during the analysis, design and implementation stages. Administrative defects are administrative and service problems that occur after delivery. Bad fixes are new defects injected into software when programmers try to fix other defects.

Defects in the requirements, design, coding, and fixes are normally detected during the development and testing stages. The two common metrics for the measurement of these defects are the rate of defects per thousand lines of code (KLOC) and the rate of defects per function point. Most of the defects in the documentation and software administration are detected after delivery through customer complaints, requests for help, suggestions for improvement, user feedback, surveys, and independent evaluations from consultants and user groups.

## 3. The OS/400 development project study

In this effort, quality assurance measures in use in a large-scale software development project were studied. Such a study could provide a baseline for illustrating current practices for assuring software quality and the success of following these practices. The focus of this study is the development efforts of the OS/400 R.1 project, a very large systems development project at IBM Corporation during 1986–1988. During the 26-month period, over 50 million lines of high-level code were developed in Rochester, Minnesota. The code was reviewed, tested, and refined into a final version consisting of over 3.6 million lines of programming code, in which 1.2 million lines were re-used from prior projects. For general information about our study on this project, please refer to [15].

## 3.1. OS/400 project quality goals and strategies

At the time the OS/400 was being developed, the continuous stream of innovations in the computer industry had resulted in tremendous improvement in achieving higher quality at lower cost for hardware and software products. However, in order to recover high R&D costs software products must arrive the market early. The major goals were to quickly seize the opportunity to satisfy the plethora of customer needs in the marketplace and to achieve high product quality. However, studies show that development schedule pressure may force management to reduce quality assurance efforts $[1,17]$ . This was also stated by DeMarco: “As time pressure increases, the only real option is to pay for speed by reducing quality…” $[6]$ . The quality goals were extended further by IBM corporate directive 105 which mandates that every new product must accomplish an improvement of at least five percent in quality and performance measurements over those of the previous products $[2]$ .

Fortunately, the management of the OS/400 project was willing to go extra miles for quality. By examining historical data, they found that a great portion of defects found after delivery were caused by insufficient testing of numerous types of system configurations. Such defects were very costly to fix. Traditional IBM culture of product secrecy and structural inertia had made it difficult for divisions to contract outside the company for reviewing and testing of software. Beta tests were limited to a few DP installations of trusted customers with non-disclosure agreements. As a result, many configuration defects escaped detection until after customer installation. Internally, experts agreed that direct customer participation in development and more beta tests would reduce the number of defects at delivery.

Deviating from the traditional culture of secrecy, IBM invited wide participation from customers and outside software vendors in the requirements definition, development, and testing of the software. Various resource control strategies (collaboration, coordination, merging and spreading of workload, reorganization, and contraction with outside software partners) were used. Outside partners helped in the review of requirements, designs, and beta test results. This was the first time IBM received outside help in quality assurance during development of a major computer system.

## 3.2. Quality control processes in development and testing

Written code went through three reviews and four tests. Some of these were performed jointly with customers and end-users.

Reviews: Reviews of the high level design, low level design, and code were conducted. The first examined functions, interfaces, control blocks, and data structures. The second focused on the logic flow, pseudocode, and error conditions in the design. The code reviews involved program walk-throughs. All problems and defects were logged by the moderators at the reviews and had to be resolved before proceeding to the next step.

Software Tests and Defect Removal: Experience, tools and process reused from prior systems development efforts helped developers reduce the time to build test plans and test cases before coding started. The software test stages were: unit, component (integration), system, and Beta. In all phases, defects were recorded for on-line query and monitoring.

Development and Quality Control Tools: Much attention was paid to CASE and development support tools: the Integrated Development Support System (IDSS) played a major role in the development activities and in maintaining the inventory of millions of lines of good quality reusable code. The following three tools were used to control and monitor software quality:

1. The Design Change Request (DCR) tool was used to record and track design changes and to control the implementation of new functions. Whenever there was a need to create or change capabilities, features, or design, a DCR feasibility review was conducted to seek to approval for implementation.

2. The Problem Tracking Report (PTR) system recorded and tracked suspected problems and their fixes. It provided a way to monitor progress in defect removal efforts, identify error-prone components, judge the work load, and certify quality of the software. It also provided an on-line documentation of problems. Whenever a defect was discovered, a PTR entry was logged into the system. The system then notified the developer responsible for providing answers and fixes. Guidelines were established for the allocation of time to solve a problem. Developers were allocated time to respond ranging from one to seven days, depending on the level of severity of the problem.

3. Error modeling tools included a defect injection and removal model and a weekly error arrival model [8,12]. Although these models were conventional, their accuracies were high. The first model predicted the rates of error injection and removal per KLOC at each development stage. These were then compared with actual defect rates. The second model predicted the numbers of error reported and must be fixed each week during the development. Thanks to these models management was able to plan in advance for necessary resources during the peak period of the testing stages. Furthermore, quality data predicted from these models were monitored regularly by top management. As a result, during the periods of schedule delay these projected quality data helped to fend off temptation to reduce quality assurance efforts.

## 3.3. Quality control in documentation, software services, and administration

User manuals written by developers were edited by professionals at independent editorial service companies to check for consistency, completeness, and ease of understanding plus the correction of spelling and syntax errors.

User satisfaction level, feedback, problems, and system performance evaluation were gathered frequently by user surveys. Follow-up telephone calls which made to every customer 90 days after installation provided abundance of feedback and identified new problems. Defects detected in the field after delivery were reported using the Problem Analysis Reports which were handled in a similar manner to the PTRs. Customers could also use the electronic customer support system to call for help and to receive software upgrades and fixes. In some instances, IBM permitted customers to contact the responsible developers in person to solve an urgent problem. These measures resulted in improved customer service and provided faster problem reporting and fixes.

## 4. Quality control results

## 4.1. Defect rate

As illustrated in Table 1, after all reviews and tests, the defect rate was reduced to below 1 per KLOC at delivery [8,12], a significant improvement over Systems 36's and 38's operating systems software. The estimated Net Defect Removal Efficiency at each stage was computed as 1 minus the ratio of defect rate at end of that stage, over the defect rate of its predecessor stage. The rate of errors injected during the design and coding stages were added before computing the Net Defect Removal Efficiency rates at the design and coding stages. The decline in the net defect removal efficiency rate after the Integration test stage, especially at the Beta test stage, occurs because the remaining errors become more difficult to detect and remove when the software is almost error-free.

Table 1  
Quality measurement at each development stage

<table><tr><td>Developments stage</td><td>Defects per KLOC at end of stage</td><td>Estimated net defect removal efficiency</td></tr><tr><td>Design &amp; review</td><td>12</td><td>.60</td></tr><tr><td>Coding &amp; review</td><td>17</td><td>.60</td></tr><tr><td>Unit test</td><td>6</td><td>.65</td></tr><tr><td>Integration test</td><td>2.4</td><td>.60</td></tr><tr><td>System test</td><td>1</td><td>.58</td></tr><tr><td>Beta test</td><td>.5 to .8</td><td>.40</td></tr></table>

## 4.2. Levels of user satisfaction and complaints regarding documentation and service

In order to detect quality improvement, quality statistics gathered before and after the system delivery were compared. The quality statistics gathered before delivery were mainly those on prior development projects. Based on the data gathered on customer service calls, the number of customer requests per user per month for software assistance on documentation, administrative, operation and software bugs decreased by an average of 50% between the period before (9/1988) and after the system delivery (9/1989). The cost of software service calls on average was 20% to 40% less than those for System 36 and System 38. Systems delivery and installation time were reduced from an average of six weeks before 1985 to two weeks in 1989. The number of errors in documentation found by users was reduced by 50% over that for the earlier projects and overall satisfaction level with user manuals, gathered from user surveys, was higher than was the case for manuals for Systems 36 and 38. With the use of the electronic customer support system to download software fixes to customer sites, the average waiting time after diagnosis was reduced from 24 hours in 1988 to 30 minutes in 1990. Complaints per thousand installed systems were reduced by 10% between 1988 and 1989. Best of all, after verifying other quality achievement records (better personnel turnover ratios, worker morale, working environments, employee training, and public image, etc.) for two years, the U.S. Department of Commerce awarded IBM Rochester the Malcolm Baldrige National Quality Award in 1990.

## 4.3. Costs of late defect removal

In order to predict costs of late removal of defects, the most commonly used benchmarks are those of Boehm's [3]. For large projects, relative to removing a defect discovered at the requirements definition stage, removing the same defect costs (on the average) 3.5 times more at the design stage, 10 times more at the coding stage, 50 times more at the testing stage, and 170 times more after delivery.

Analysis of the relative costs of defect removal in this project showed that the cost of detection and removal of a defect at the testing stage was about 13 times that at the earlier design stage. Furthermore, the cost after the delivery stage was about 7 times that at the testing stage and up to 92 times that at the design stage [8]. Since the IDSS system did not keep track of defects discovered prior to the design stage, Boehm's cost was used as the base for comparison. A comparison of the costs of late defect removal is illustrated in Fig. 1. Note that while the relative costs of removal defects at testing stage for the OS/400 was a bit lower than those of Boehm's study, the costs of removal defects after delivery were almost twice as high. Because IBM shipped hundreds of thousands copies of OS/400 software worldwide, it was very costly to fix a defect after installation.

## 4.4. Reusable and scaffolding code

Reusable code and re-used test cases have made a significant contribution to software quality levels. About one third of the OS/400 code shipped to customers was reused from previous efforts. There were a large volume of code and data created during the development but were not included in the final product at delivery. Some of this were “scaffolding code”, ie. program modules, test cases, and test data that were generated during development mainly for testing purpose, but not included in the final product [5]. The ratio of scaffolding code to actual code was at least 10 to 1. Other components were not included in the final product simply because they either failed rigorous quality tests or were mainly developed for future versions. Incorporation of a million lines of almost defect-free source code and re-use of existing test cases allowed this project to shift more time and resources toward quality improvement of the entire system.

![](/api/attachments/MQB9863X/fulltext/images/5a53e102d7de8ce259920a1bad0c6aed429e4e3a515546e3226a399b21a392f0.jpg)  
Fig. 1. Relative Costs of Late Defect Removal

## 4.5. Causes of bad fixes

Bad fixes are new defects injected into software when workers try to fix other defects. Common causes for bad-fixes were studied for defect prevention and improvements in future fixes. The causes ordered by their frequency of occurrence are:

1. Not thorough enough testing;

2. Incorrect instructions given to solve problems;

3. Not all steps of problems tested;

4. Incomplete test bucket for total testing;

5. Inadequate review process;

6. Inability to test the user hardware environment;

7. Insufficient testing of special installation instructions.

The above information suggested that there were room for improvement in the testing processes. In addition, it appeared that schedule compression may have taken a toll on the efforts devoted to quality assurance.

## 5. Lessons learned and success factors

Ky factors in improving software quality resulted from this study are:

1. Well-defined quality goals and objectives that are driven by market and end-user needs. In order to better meet user requirements, project managers must employ various environmental and resources control strategies including resource coordination, organization linkages, user participation in development and testing, and prioritizing requirements.

2. Good management of reusable and scaffolding code. Reuse and recycling of reliable code and good test cases saves time and reduces efforts in quality assurance. A repository is needed to manage large amount of code and data. Some of this code will be re-used, revised, and upgraded for future versions.

3. Good quality assurance planning and control. It is critical for large projects to have a systematic quality control plan and models and to allow adequate quality assurance resources. More emphasis should be made in early detection and prevention of defects, especially for a software product with many installations.

4. Effective feedback. Problems encountered should be reported and recorded as soon as possible. Management should be quick to respond to feedback to avoid costs of late action.

## 6. Conclusion

With the dramatic increases in worldwide software expenditures, software developers cannot afford to make software quality an afterthought. Our study showed that the inclusion of quality assurance strategies can result in high quality commercial software. We identified and described here the many quality assurance strategies used by IBM Rochester. Our study suggested that a tight project schedule compression may hurt quality.

To what extent can our findings be generalized to other software development projects? We do believe several aspects of our study and findings will be useful to software developers in general. We believe the quality assurance strategies documented here can serve as a menu of tools and techniques that can promote high levels of software quality.

## 7. For further reading

[4,7,16].

## Appendix A. Malcolm Baldrige National Quality Award and ISO 9000 Quality Standards

The Malcolm Baldrige National Quality Award and ISO 9000 series are the two major set of quality standards that are widely followed by many business firms in the U.S. These requirements apply to all business processes including manufacturing and services and they also apply to software development processes as well. The Malcolm Baldrige Quality Award requires that candidate organizations use quality metrics and sophisticated quality measurement systems. The measurements are subject to validation and verification. ISO 9000 series quality standards for software development go further and require the clear definition of management responsibility in quality control, production of document control procedures, implementation of process control by inspection, testing and veri \* fication of test results, performing corrective actions when appropriate, development of internal quality audits, thorough personnel training, and producing after-delivery servicing statistical analysis. The compliance with the above quality standards by major international corporations has created ripple effects for compliance on business firms world-wide because candidates for the Malcolm Baldrige awards and ISO 9000 certification also require their suppliers and subcontractors to comply with these standards.

## References

[1] Abdel-Hamid, T.K and Madnick, S.E., Software project dynamics: An integrated approach, Englewood Cliffs, NJ: Prentice Hall, 1991.

[2] Bauer, R., Collar, E., and Tang, V., The Silverlake project: transformation at IBM, NY: Oxford University Press, 1992.

[3] Boehm, B.W., Software Engineering Economics, Englewood Cliff, NJ: Prentice-Hall, 1981, p. 40.

[4] Boehm, B.W., "Improving Software Productivity," Computer, Sept. 1987, p. 43.

[5] Brooks, F., The Mythical Man-Month, Reading, MA: Addison-Wesley, 1978, p.148.

[6] DeMarco, T., “Why Does Software Cost So Much?,” IEEE Software, March 1993, p. 90.

[7] Humphrey, W.S., Managing the Software Process, Reading, MA: Addison-Wesley, 1989, p. 339.

[8] IBM Corp., The Quality Journal Continues..., Order Number G325-6015-01, 1990.

[9] IEEE, IEEE Standard Glossary of Software Engineering Terminology, 1983 & 1990.

[10] Jones, C., Programming Productivity, NY: McGraw-Hill, 1986, p. 171.

[11] Jones, C., “Software Quality: What Works and What Does Not”, Software Engineering Strategies, Jan.-Feb. 1994, pp. 6–13.

[12] Kan, S.H., “Modeling and Software Development Quality,” IBM Systems Journal, Vol. 30, No. 3, 1991, 351–362.

[13] Moller, K.H. and Paulish D.J., Software Metrics, IEEE Computer Society Press, London: Chapman & Hall, 1993, pp. 21–68.

[14] Musa, J.D., Iannino, A., Okumoto, K., Software Reliability, Professional Edition, NY: McGraw-Hill, 1990, pp. 5–9.

[15] Phan, D.D., Vogel D.R., and Nunamaker J.F. Jr., “Empirical studies in software development projects: Field survey and OS/400 study,” Information & Management, Vol 28, No. 4., April 1995, pp. 271–280.

[16] Phan, D.D., Vogel D.R., and Nunamaker J.F. Jr., “The Search for Perfect Project Management,” Computerworld, Sept. 26, 1988, pp. 95–100.

[17] Phan, D.D., “Information Systems Project Management: An Integrated Resource Planning Perspective Model,” Ph.D. dissertation, University of Arizona, 1990.

[18] Rappaport, A.S. and Halavi, S., “The Computerless Computer Company,” Harvard Business Review, Jul.-Aug. 1991, pp. 69–80.

[19] Weinberg, G.W., Quality Software Management, Vol. 1, NY: Dorset House, 1992, p. 13.

![](/api/attachments/MQB9863X/fulltext/images/bbe11ebfb3790b4a298d69456de6263ae00e36d6da50e6e4614bfd590bf2a893.jpg)

Dien D. Phan is Associate Professor in the Business Computer Information Systems, College of Business, St. Cloud State University, St. Cloud, Minnesota. He received the MBA degree from the University of Minnesota in 1980 and the Ph.D. in MIS from the University of Arizona in 1990. Prior to joining SCSU, he was employed at IBM Corporation, Rochester, MN during 1981–1991 in various software development positions. His research focuses on software devel-

opment productivity and group collaboration support.

![](/api/attachments/MQB9863X/fulltext/images/571f31022436283c2e70fc81bbe23d617d38d2df034eeec6e71a42c4ac4fb90f.jpg)

Joey F. George is Associate Professor in the Department of Information and Management Sciences, College of Business, Florida State University. He earned his bachelor's degree at Stanford University in 1979 and his Ph.D. in Management at the University of California at Irvine in 1986. Dr. George's research focuses on information systems and work, ranging from studies of computer-based monitoring in the workplace to studies of group support sys-

tems. He has published in several journals including Communications of the ACM, Information Systems Research, Communication Research, and MIS Quarterly.

![](/api/attachments/MQB9863X/fulltext/images/b96f117b6ca2e81e20b3a8d52c8d210ba199ff2108ad29183b9495546fe26656.jpg)

Douglas R. Vogel is Associate Professor in the Management Information Systems, College of Business and Public Administration, University of Arizona, Tucson, Arizona. He received the MS degree in computer science from UCLA in 1972 and the Ph.D. degree in MIS at the University of Minnesota in 1986. Prior to joining The University of Arizona, he was the research coordinator for the MIS Research Center at the University of Minnesota. His current re-

search interests bridge the business and academic communities in addressing questions of the impact of MIS on aspects of interpersonal communication, group decision making and organizational productivity.
