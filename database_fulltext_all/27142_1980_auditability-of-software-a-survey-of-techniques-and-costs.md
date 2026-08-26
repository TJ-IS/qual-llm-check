---
otero_id: 27142
otero_key: "47GXTNEZ"
title: "Auditability of Software: A Survey of Techniques and Costs*"
authors: "Ira R. Weiss"
year: "1980"
journal: "MIS Quarterly"
doi: "10.2307/248959"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Auditability of Software: A Survey of Techniques and Costs
Author(s): Ira R. Weiss

Source: MIS Quarterly, Vol. 4, No. 4 (Dec., 1980), pp. 39-50

Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/248959

Accessed: 08/05/2014 19:55

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

Auditability of Software: A Survey of Techniques and Costs\*

By: Ira R. Weiss

## Abstract

Numerous techniques have been identified to assist EDP auditors in accomplishing audit objectives. Within this realm a major issue of interest is identifying methodologies to monitor the reliability and integrity of production software. This article presents a number of available techniques to audit software, and evaluates each on the basis of development cost, operational cost, appropriate timing of usage, and effectiveness.

Keywords: EDP auditing, auditability of software, software integrity, software reliability  
ACM Categories: 1.3, 3.5, 4.6, 4.9

## Introduction

Issues relating to the auditability of software have evolved from two disciplines—computer science and auditing. Computer scientists and software engineers have been deeply involved in research addressing issues of certification of software and software reliability. This work has reviewed and investigated issues associated with user demands and corresponding software to respond to those demands; methodologies which can assist in the actual design and coding of software; validation techniques to substantiate statements of adherence to specifications; and methods for estimating and measuring reliability of software based on probabilistic models. $^{1}$ These computer scientists and engineers have been basically concerned with the development of formal models and methodologies which would enhance the software life cycle. To date, the literature identifies no definitive methodologies to certify the “correctness” of software. The current status of the application of software reliability research, although, can be seen by the growing utilization of concepts and methodologies associated with structured design, structured programming, and structured walkthroughs—all these attempt to improve the “correctness,” maintainability, and ultimately the reliability of software [4, 8].

The other group, extremely concerned with issues of auditability and reliability of software, is auditors. The subgrouping of auditors specifically concerned with the auditability of software is generally referred to as EDP auditors. The objectives of EDP auditors are substantially more pragmatic than those of the computer scientist or engineer. The EDP auditor has the responsibility of evaluating if software performance is in accordance with software specifications as one of the functions of the organizational position. Initially, this should be evaluated during the design phase of the software system as part of the audit of the systems development life cycle. Organizational benefits accrued here are assurances that software placed in production has been reviewed for conformity to logic and control specifications by independent sources. Additional conformity checks would occur within post implementation and routine recurring audits. Within the post implementation phases of specific issues the EDP auditor is concerned with are the ongoing reliability of organizational software and the potential impact of the human effect on software performance. Therefore, continuous reviews of organizational software are warranted because auditor statements associated with adherence to specifications in time period t give no assurance as to the status of performance in period t + n.

This article will primarily address issues relating to the auditability of software as it relates to the EDP auditor. Specifically, the following sections will address a review of audit approaches and techniques, the impact of techniques on systems performance, categorization of techniques, cost of implementation, effectiveness issues, and trade off analysis.

## General Discussion — EDP Auditing

Traditionally, methodologies associated with the software development process allowed for programs to be put into production without exhaustive testing procedures. Programmer testing and parallel processing systems tended to give enough assurance as to the correctness of the software. Outcomes of inadequate software testing procedures were program “bugs” discovered randomly during production processing. Initially, the consequences of such occurrences were not as severe as one might expect. This was because the system in question generally had one input file, one or two production programs, and one output file. With this structure in place, identification of errors and diagnosis of consequences and appropriate corrections was not a difficult task. Presently, as systems are being developed online, realtime, as well as in an automated chaining fashion (i.e., sales transaction generates credit check, billing, inventory, receivables), the effects of an error in processing could potentially lead to impossible reconstruction because of the pervasive effects of chained transactions and destructive updates. Therefore, state of the art technology, coupled with software design to maximize use of the technology, has created the need for new monitoring methods by management to oversee and control organization information processing.

Also, corporate awareness of computer abuses and the average dollar impact per abuse on the organization, \$500,000 - \$650,000 [2, 13], had led to management decisions to create and staff the EDP auditor function.

In order to fully understand the function of the EDP auditor a definition of EDP audit objectives is warranted.

Definition—The objective of an audit of compliance with controls is to predict the reliability and related exposures which should be expected from the system in operation in the future [11].

The EDP auditor is primarily involved with the evaluation of control structures surrounding EDP activities. The objectives of these controls are to enhance reliability of the system. These control structures are of both a general and specific nature. An audit of compliance with general controls might assess the concentration of potentially conflicting functions within operations, i.e., programmers operating the computer. Specific controls might address an application to insure that appropriate edit checks have been incorporated within a program. However, the essence of control evaluation is to insure or enhance the reliability of data being processed through the system.

The EDP auditor must continuously review systems to gain assurance that systems are performing in accordance with specifications in order to be responsive to the organizational mandate. The auditor has developed a number of techniques which gives the auditor assistance in the evaluation scheme in order to meet this objective. The spectrum of techniques must allow the auditor to review systems through the full software life cycle. A model of the software life cycle and associated audit impact may be viewed in Figure 1.

The auditor has responsibilities at two distinct phases with the System Development Life Cycle (SDLC), pre- and post implementation. Pre-implementation involvement may be described as:

1. liaison function,

2. control expert, and

3. software evaluator.

![](/api/attachments/47GXTNEZ/fulltext/images/3dfa80e05cebef43b2fec97e97d56d4cf7e66e6850a81cfe8a1dc1dc856df5fa.jpg)  
Figure 1. Auditor Impact on Software Life Cycle

During liaison activities, the auditor must insure that adequate communication has evolved between the user group and project team to assure that all parties involved understand the scope, nature, timing and other implications of the entire project. If the organization has developed a structured SDLC methodology then the auditor may select the critical points within the cycle to participate in, in order to review, evaluate, and report on such items as:

1. understanding project objectives by all parties involved,

2. user sign offs to critical design points within the SDLC,

3. the adequacy of feasibility and cost/benefit studies conducted,

4. adherence to budget and scheduling, and

5. the inclusion of project kill points and evaluations at each point.

This function is predominantly a compliance function. The auditor is not an analyst or designer, and therefore should concentrate on reviewing key documentation which could indicate problems or misunderstandings within the development function. The SDLC is a control structure of the organization, and the auditor's role is to assure the project's conformity to the control structure. Auditor tools to support this function may be categorized as of inquiry, questionnaires, and interviews.

During control activities the auditor is primarily concerned with:

1. the adequacy of control structures in the design phase, and

2. the effectiveness of the controls within the testing phase.

Many times the auditor may become an active participant within the systems design project team during the design specification phase. The auditor, as a control expert, should have the ability to affect the specifications by modifying the control structures if inadequate general and/or application controls have been designed for a software system. The auditor might be concerned with issues as diverse as data security, personnel authorization, backup, and retention within the general set of controls. Within the applications control set the auditor would be concerned with edit checks, logic checks, control reconciliations, suspense, and error reporting. One of the main reasons that it is very important for the auditor to get involved with controls at the specifications stage is demonstrated by experiences at the Kodak Corporation [7]. It was found that:

a control will cost—

\- four times as much to include if it is added after the system is specified,

\- eight times as much to include if it is added after the system has been programmed,

\- twelve times as much if it is included after the system has been tested, or

\- sixteen times as much if it is included after the system has been implemented.

The auditor must be assured during the testing phase that controls designed to be included within the system:

1. are actually included,

2. are working as specified, and

3. may not be overridden, unless specified.

This means that the auditor must carefully review the testing specifications to insure that they include global tests to insure that the controls are working as specified. The inclusion of the user in the total testing scheme is of concern to the auditor. The user's familiarity with the “normal” data processed by the system will add reality to the testing plan. Active participation is required if the auditor is dissatisfied with the testing plan. Instead of reviewing the results of the test the auditor must design global tests and assist in their implementation.

Audit tools that may be used within the control structure evaluation depend on the level of participation of the auditor. Generally, within the determination of the adequacy of controls, the auditor might utilize questionnaires to address general control structures' inclusions and omissions. System and flow charts might be utilized to determine the strengths and weaknesses of the intra- and inter-system control structures within the application control structures. Numerous automated techniques might be applied if the auditor actually gets involved in the design and implementation of the testing plan. These techniques are reviewed in the next section.

During software evaluation activities the auditor is primarily concerned with the adherence of design software to the software specifications. This addresses two issues.

1. Given a set of input transactions, does the software process them consistently with the software specifications?

2. Are there elements of the software that do not correspond to any types of input transactions?

The level of participation of the auditor within this phase again depends on the design of the global testing plan. The auditor could be satisfied by reviewing the testing documentation if the testing plan of the user and project team adequately includes tests to cover the above objectives. If these objectives are not adequately covered by the testing plan, then the auditor must become actively involved in designing a plan which covers the objectives. Very often the software specification adherence testing plan and the control testing plan may be combined to accomplish both sets of objectives with one set of activities. Therefore, many of the automated audit tools reviewed in the next section are applicable to all levels of software testing.

Active auditor involvement with software systems, prior to implementation, supplies a reliability base which the auditor may refer to after implementation. It also provides an independent evaluation of the probability that the system will meet the defined objectives, prior to implementation. Both of these functions are extremely important from an organizational standpoint.

The auditor's post implementation involvement within the SDLC may be described as:

1. a systems evaluator, and/or

2. a software/control evaluator—post implementation.

The auditor attempts to evaluate if the implemented system represents the original system specifications as designed by the user and project team within the Systems Evaluation function. Techniques associated with this phase are primarily inquiry and observance oriented. The auditor attempts to validate that the implemental system of logic and controls is a representation of the pre-implementation system within the Software/Control evaluation function. As production systems incur maintenance, that representation may change. The auditor must be aware of those changes and update the testing procedures to include the effect of the changes. Many of the tools and techniques available for this type of review should be the same as those used in the pre-implementation phases.

In summary, the auditor is responsible for making assertions about the reliability of the processing systems, and specifically, the reliability of the production programs both pre- and post implementation. The pre-implementation assertions are state-in-time assertions while the post implementation assertions must be dynamic and continuous. The auditor does this through the utilization of numerous techniques. Those techniques specifically used for software auditing are reviewed in the next section.

## Review of Auditing Techniques $^{2}$

There are a number of techniques currently being utilized by EDP auditors in performing their functions. Concentration in this section will be strictly geared to techniques associated with verification of controls and processing logic.

It might be useful to define some general categories that can be used to classify the techniques for review purposes. Two classifications that seem to be appropriate are Static/Discrete techniques and Continuous/Concurrent techniques. The Static/Discrete technique allows the auditor to address verification issues at a specific point. No inferences may be drawn regarding reliability until the static technique is again applied. The Continuous/Concurrent technique allows the auditor to monitor the software on a continuous basis, and concurrently with production processing. Static techniques never allow the auditor to verify the logic in a production environment. This is a major drawback to the static approach.

## Static Discrete techniques

Under the category of Static/Discrete techniques a review of the test data method and parallel simulation method is presented.

## Test Data

The Test Data Method supplies the software with a wide spectrum of test generated transactions to process. The transactions contain both valid and invalid data, with the objective being to make sure that valid data is processed correctly and that invalid data is not processed. The auditor must carefully study the software documentation with emphasis on the input record layout, valid and invalid transaction types, and processing logic in order to use this method effectively. The auditor then generates a set of fictitious transactions which will be used to substantiate whether or not the logic executes as the documentation indicates. The auditor must precalculate the result of each transaction, such that a comparison may be made with the result of the processing program. Errors in comparison of output indicate that either the auditor calculated the result incorrectly, or the software does not adhere to documentation specifications. This in and of itself, may indicate the documentation is outdated rather than errors in processing logic. Perfect comparability does not assure total validation. The auditor cannot be certain that all control points and logic paths in the program were tested. Also the program may be printing comparable results, but internally carrying out some surreptitious action, i.e., the payroll program may be adding fractions of pennies to the programmer's salary rather than truncating. Finally, the auditor cannot be certain that the software being tested is the actual production software which is of concern in a post implementation review environment.

## Parallel Simulation

The Parallel Simulation Method functions by the auditor creating an audit program that simulates the software. Transaction files are then processed through the simulated program and the output is compared with the output of the same transaction file processed through the software. However, the auditor must study the software documentation in great depth to effectively use this technique. The auditor may want to simulate total logic of the software or possibly only part of the logic. Audit objectives will dictate this decision. Generally the simulation will be written in a Generalized Audit Software (GAS) language, but the language has no direct bearing on the process. After the program has been created and tested, a transaction file will be processed. The output of this process will be compared to the output of the software processed with the same transaction file. Errors in comparability are again interpreted as either an auditor error or a non-adherence to documentation. Perfect comparability is interpreted in the same skeptical fashion as test data. The actual software might contain modules that are not documented, and therefore were not simulated and not tested. Also, when simulating production programs, there is the uncertainty that the program simulated is the one always used in production.

## Advantages/disadvantages of Static/Discrete Methods

The major advantage of the methods reviewed is, in a production environment, that they both have no impact or adverse effect on production processing. These techniques may be applied at slack time periods or even off-site. Both the parallel simulation and various test decks developed in a testing environment may be used again during post implementation reviews, unless the documentation indicates changes that would affect their use.

The major disadvantages of these methods are associated with the time periods between audits, and the inconclusive nature of the information generated during the audit.

## Continuous/Concurrent Techniques

Continuous/Concurrent Techniques are implemented by having principles of auditability built into the software at design stages, or at modification stages. Under this category a review of the Integrated Test Facility (ITF), Snapshot, and Tracing and Mapping techniques is presented.

## Integrated Test Facility

The Integrated Test Facility, or the Mini-Company Approach, creates an artificial entity and artificial transactions that are processed against this entity during software processing. The auditor must precalculate the result of processing in order to compare and generate inferences about the actual software as in the test data approach. Careful design of the system is imperative to operationalize this technique. If the software being audited updates a master file, the auditor must create a fictitious master file record to process against. If the software generates disbursements, then appropriate controls must be integrated into the system to assure that these fictitious transactions do not create valid disbursement vouchers or checks during production processing. The key component or strength of this technique though is that the fictitious transactions are being processed along with the “live” transactions. Issues relating to the uncertainty of testing the actual production programs are overcome by this technique. All other audit evidence issues are identical to the test data method.

The ITF is an implementation of the test data approach in a “live” environment. One additional benefit of the ITF is the ability to evaluate more than just software processing. Since auditor transactions must enter the system concurrently with “live” transactions, the auditor can evaluate total systems adherence to specifications, from transaction authorization, transcription, error reports, error reprocessing, etc. Assertions therefore can be made about total system processing rather than strictly about software processing.

## Snapshot Method

The Snapshot Technique generates status reports of key decision variables in a program at designated points. To insure that the output of a logical module is correct, specifically when one module is chained to other complicated modules, the auditor might want to view all variables and data values associated with the executing algorithm. The Snapshot Technique snaps picture images of memory at distinct intervals. Questions that this technique may address are issues relating to any variable(s) that have an impact on decision when they should not have an impact.

The Snapshot Audit Technique offers the capability of listing all the data that was involved in a specific decision making process. In and of itself, the Snapshot Method does not insure software validity; it does, however, simply verify those data items that have supplied an impact, or serve as input, to a decision. Careful analysis of key decision points in a program must be made to effectively operationalize the Snapshot Method. The key to this approach is printing only limited data with critical impacts on decision. It is an excellent tool to utilize when answering questions relating to why questionable results of processing occurred, and therefore is an excellent test environment tool.

## Tracing

The Tracing Technique is an option usually supplied within most standard programming languages. This method produces reports indicating the actual sequence of instructions executed in processing transactions. This might be considered control path auditing rather than program verification. In order to utilize this technique effectively, the auditor must desk trace a transaction through the software, and compare the desk trace to the computer trace. Perfect comparability indicates that transactions were processed by every instruction appropriate to that transaction, but gives no assurance to the correctness of any individual instruction. Errors in comparability again may indicate an auditor mistake, or that transactions are not being processed according to supplied documentation. Technical ability on the part of the auditor is necessary in order to utilize this technique. Generally this technique is operationalized by the auditor actually tracing transactions through the source code. Therefore, the ability to read and interpret source code is a prerequisite.

## Mapping

Mapping is a technique that generates summary reports of how software resources were utilized in processing a transaction file. These summary reports indicate such items as:

1. a list of program segments not executed,

2. a list of steps consuming the most CPU time, and

3. a list of the source code showing how many times each step was executed.

The auditor must be able to relate the report output to the transaction file processed in order to utilize this report. Also, the auditor should be able to detect exceptional occurrences from the report generated—why did some steps consume so much CPU time, or why was an instruction executed that many times? Mapping is generally implemented by utilizing commercially available software measurement tools $[1]$ .

## Advantages/disadvantages of Continuous/Concurrent processing

The major advantage of Continuous/Concurrent Methods is that they can be used during actual production processing. These techniques may be used each time a particular software system is executed if it is deemed necessary. More often than not, this requirement is not necessary. The ability to run these methods without disrupting normal operations and not informing operations people of the testing allows the auditor to use discretion as to timing of the usage. They are also excellent testing and debugging tools for pre-implementation purposes. Most of these techniques require that some modifications to the software be made prior to implementing these techniques. The optimum time to modify the software would be during the design stage. Therefore, these techniques could be built into the initial software design, used for software testing purposes, and then used to continuously monitor the production programs.

The major disadvantages of Continuous/Concurrent Methods are in the cost factors associated with their use, and the technical ability required on the part of the auditor in utilizing them. Cost factors are defined as both actual dollar outlay, as well as the cost of utilizing the machine. This may be defined as an opportunity cost or a cost associated with the effects of concurrent auditing processes or monitoring methods on production performance [10].

## Audit Techniques and Associated Cost Factors

Each of the techniques reviewed and described have identifiable cost factors associated with their implementation and use. A brief identification of the cost types and cost behavior with each technique will allow for both cost/benefit and trade off analysis considerations to be addressed.

## Test Data

Elements of cost associated with Test Data may be enumerated as follows:

Initial set up cost, or fixed cost:

a. total review of application documentation.

Recurring cost, or variable cost:

b. test planning,

c. create test data,

d. precalculate result of test data,

e. run test data, and

f. analysis of test data.

The above indicates that the Test Data Method is a labor intensive method. Cost may be modified by the utilization of test data generators which trades off time for creation of test data with the cost of the package and the computer time needed to create the data. In general, the cost of utilizing the Test Data Method would be proportional to the:

1. complexity of software tested, and

2. scope of the test.

To categorize cost behavior of the Test Data Method from the above description of development cost and recurring costs, it would appear that this method has a low fixed cost and a rather high variable cost.

## Parallel Simulation

Elements of cost associated with Parallel Simulation may be enumerated as:

Initial set up cost, or fixed cost:

a. total review of documentation,

b. design time,

c. coding time, and

d. testing procedures.

Recurring cost, or variable cost:

e. processing time, and

f. analysis of result.

The above indicates that Parallel Simulation is also a labor intensive method. Though this method probably consumes more computer time and resources than the Test Data Method, its cost elements are generally associated with labor. The cost of utilizing the Parallel Simulation Method would be proportional to the complexity of the system being simulated.

To categorize cost behavior implications of the Parallel Simulation Method, it could be stated that the fixed costs of developing the process are substantially greater than those of the Test Data Method. However, the variable cost of running the simulation is substantially lower than the effort associated with test data.

## Integrated Test Facility

Elements of cost associated with the Integrated Test Facility may be enumerated as follows:

Initial set up cost, or fixed cost:

a. total review of complete system—manual as well as automated procedures,

b. design time,

c. control issues,

d. testing procedures, and

e. creation of fictitious entities.

Recurring cost, or variable cost:

f. creation of fictitious transactions,

g. incremental processing time proportional to transaction volume,

h. precalculate results, and

i. analysis of results.

The above indicates that the Integrated Test Facility is also labor intensive, but more machine interfaces are occurring. Initial cost can vary from relatively high, if created at the design phase of the applications software, to extremely high, if imposed in a modification phase. Recurring costs are almost identical to those of the Test Data Method, except for processing at production time.

Cost behavior issues here can be categorized as high to very high fixed costs, depending on when it is imposed into the system, and relatively high variable costs. Reasons why fixed costs are high relate to the extreme care needed because of processing fictitious transactions during live production processing. Control point design and implementation must be carefully monitored and tested.

## Snapshot

Elements of cost associated with the Snapshot Technique may be enumerated as:

Initial set up cost, or fixed cost:

a. total review of documentation,

b. analyze critical decision point,

c. identify where snapshot is applicable,

d. design triggering method,

e. design snapshot files,

f. modify programs,

g. design snapshot report writer, and h. test.

Recurring cost, or variable cost:

i. incremental processing time, and

j. analysis of result.

The above indicates that the Snapshot Method is also labor intensive. Cost behavior may be categorized as a high fixed cost because of the analysis issues and design of all the automated triggering and recording mechanisms, but is a low variable cost. Incremental processing time should be minimal, unless the number of snapshots taken during processing is voluminous. The variable cost in implementing snapshots is probably very comparable to the variable cost associated with parallel simulation.

## Tracing

Elements of cost associated with the Tracing Technique may be enumerated as follows:

Initial set up cost, or fixed cost:

a. analysis of critical programs to trace, and

b. modifications to programs.

Recurring cost, or variable cost:

c. incremental processing time, and

d. analysis of results.

The above indicates that auditor involvement in implementation of the Tracing Method is generally minimal within the initial set up phase. Auditor involvement can be substantial in the analysis phase, but this depends on the complexity of the application. Cost behavior may therefore be categorized as low fixed costs, but potentially high variable costs. Actually it has been indicated in other studies $[9]$ that throughput time can actually increase twofold by utilizing the Tracing Method. Therefore, it may be interpreted that a substantial impact on systems performance is probable using Tracing Methods. Tracing most likely ranks lowest in fixed cost utilization, and highest on variable costs. $^{3}$

## Mapping

Elements of cost associated with the Mapping Technique may be enumerated as follows:

Initial set up cost, or fixed costs:

a. purchase or rental of software monitor,

b. analysis of critical programs, and

c. set up time for use on a program.

Recurring cost, or variable cost:

d. incremental processing time, and

e. analysis of results.

Auditor involvement within the Mapping Process is also generally minimal within the initial set up phase. Actual fixed costs are high because of purchase or rental of packages, estimated at about \$350/month or \$6500 purchase [9], but variable costs are moderate to high. Software mapping does imply some systems overhead, but this has been estimated at levels substantially below tracing [9]. Cost behavior classification

$^{3}$ See reference [10] for 10%-50% impacts of software overhead. This technique may have a 100% software overhead associated with it.

may therefore be rated as relatively high fixed costs and relatively high variable cost due to overhead on system.

Table 1 summarizes the techniques evaluated and ranks their cost factors based on interviews with users and an analysis of the techniques.

The cost information of Table 1 is presented in a rank comparative basis. Integrated Test Facility is shown as the most expensive to develop. Studies have indicated that between three and twelve man months development time is not uncommon [9], but relatively reasonable, to run on a continuing basis. Some interesting issues are the recurring costs associated with Tracing and Mapping. Both of these techniques, in and of themselves, do not explicitly meet the objective of auditing of software if the objective is defined as adherence to specifications. Both of these methods would have to be used in combination with other techniques, therefore using these techniques to accomplish total objectives would be exceedingly costly. Mapping would be an expensive proposition for sporadic use because of its high fixed cost, unless a software monitor is already in house, but tracing becomes very attractive for occasional use because of its exceedingly low fixed cost. The only techniques that explicitly audit to meet the definition of adherence to specifications are the Test Data, Parallel Simulation, and Integrated Test Facility. The Integrated Test Facility because of high fixed cost issues imposes two constraints—implementation at the design phase, and use in only critical systems. Once a system is already in production, modifying the system to incorporate ITF is very timely and costly. The best cost/performance ratio can be generated by incorporation at design phases. Also because of the high cost, even at design, this method should only be applied to critical systems that need continuous/concurrent monitoring. Parallel Simulation is a technique that addresses program verification explicitly, but in reality falls short of the objective. The weakness of only being able to simulate what is documented makes the fairly high fixed cost unwarranted. Also, with every modification to the production program the audit program must be modified. This also increases the fixed cost components. The remaining technique, Test Data, deserves attention. The highest cost associated with the Test Data Method is the creation of the test data. As previously mentioned, Test Data Generators have been developed to assist in this function. This trades off some variable for fixed cost, a good exchange for continuing use. The major weakness of this method then is its static nature. Using test data for periodic auditing with sporadic implementation of tracing might mitigate some of the inherent weakness.

Table 1. Techniques, Objectives, and Costs

<table><tr><td>Name</td><td>Type</td><td>Objective</td><td>Fixed Cost1 = Lowest</td><td>Variable Cost6 = Highest</td></tr><tr><td>Test Data</td><td>Static</td><td>Verification of Program Logic</td><td>2</td><td>4</td></tr><tr><td>Parallel Simulation</td><td>Static</td><td>Verification of Program Logic</td><td>3/4</td><td>1/2</td></tr><tr><td>Integrated Test Facilities</td><td>Continuous</td><td>Verification of System</td><td>6</td><td>3</td></tr><tr><td>Snapshot</td><td>Continuous</td><td>Analysis of Critical Modules</td><td>3/4</td><td>1/2</td></tr><tr><td>Tracing</td><td>Continuous</td><td>Critical Path Auditing</td><td>1</td><td>6</td></tr><tr><td>Mapping</td><td>Continuous</td><td>Auditing of Exception Through Summary Statistics</td><td>5</td><td>5</td></tr></table>

In evaluating all of the above methods, it might be concluded that because of the costs or weaknesses associated with any method, any one method is inadequate. Methods with high fixed cost could only be cost justified if used both at development and post implementation. Methods with a low fixed cost, but high variable costs, could be used intermittently at both development and post implementation to support conclusions based on other techniques used. In essence, the utilization of these methods in combination with specific audit objectives to address, would probably be the only way to achieve audit satisfaction. Therefore, the auditor must be knowledgeable of all the above techniques, their associated costs, and appropriate time of use to effectively accomplish the audit of software.

## Conclusion

An attempt has been made to evaluate six contemporary methods which give auditors some ability to validate software. These methods have been presented in a multi-dimensional fashion—type, cost, behavior, and objective. After detailed analysis it is concluded that no method, in and of itself, is totally superior to any other. This was concluded by comparative analysis utilizing all the dimensions enumerated above. The auditor's only recourse then is to be knowledgeable enough about the techniques to select the correct method for the appropriate situation. Utilization of methods in combination is recommended where appropriate. Purely on a cost/benefit basis Test Data methods appear to be more cost effective than the others, but inherent weaknesses associated with its static type still influence its effectiveness.

It is incumbent upon the EDP auditor to be able to evaluate, in items of cost, type behavior, etc., which method to use and when to use it in order to implement an effective audit program. Only with competent EDP auditors can auditability of software be accomplished.

## References

[1] Adams, D.L. "COMBI as an Audit Tool," EDPACS, Volume 2, Number 10, April 1975, pp. 7-8.

[2] Allen, B. “The Biggest Computer Frauds: Lessons for CPA’s,” Journal of Accountancy, Volume 143, Number 5, May 1977, pp. 52-62.

[3] Anderson, T. and Shrivasuva, S.K. "Reliable Software: A Selective Annotated Bibliography," Software Practice and Experience, Volume 8, Number 1, January-February 1978, pp. 59-76.

[4] Baker, F. T. “System Quality Through Structural Programming,” AFIPS Conference Proceedings, Volume 41, Part I, Fall 1972, pp. 339-343.

[5] Cash, J., Bailey, A., and Whinston, A. "A Survey of Techniques for Auditing EDP-Based Accounting Systems," Accounting Review, Volume 111, Number 4, October 1977, pp. 813-832.

[6] Gilb, T. “The Measurement of Software Reliability and Maintainability: Some Unconventional Approaches to Reliable Software,” Computers and People, Volume 26, Number 9, September 1977, pp. 16-21.

[7] Hannye, L. G. “Auditors and DP’ers Benefits from Association in the Systems Development Process,” The Internal Auditor, Volume 4, Number 6, December 1977, pp. 67-70.

[8] IBM, How to Write Correct Programs and Know It, FSC 73-5008, February 1973, Gaithersburg, Maryland.

[9] Institute of Internal Auditors, System Auditability and Control Audit Practices, Part 4, Institute of Internal Auditors, Inc., Altamonte Springs, Florida, 1977, pp. 109-164.

[10] Lientz, B. P. and Weiss, I. R. “Trade-Offs of Secure Processing in Centralized vs. Distributed Networks,” Computer Networks, Volume 2, Number 1, February 1978, pp. 35-43.

[11] Mair, W. C., Davis, K. W., and Wood, D. R. Computer Audit and Control, Q.E.D. Information Sciences, Institute of Internal Auditors, Inc., Altamonte Springs, Florida, 1977, p. 20.

[12] Myers, G. J. Software Reliability, Principles and Practices, Part 4, Wiley Publishing Co., New York, New York, 1976.

[13] Parker, D. Crime By Computer, Charles Scribner and Sons, Inc., New York, New York, 1976.

## About the Author

Ira R. Weiss, Ph.D., CPA, is an Assistant Professor of Accountancy and Taxation in the College of Business Administration at the University of Houston. He received his M.S. and Ph.D. at U.C.L.A. He is Assistant Director of Certification for the EDP Auditors Foundation. He has published professional articles in the Accounting Review, Computer Networks, Interface, and CPA Journal. His major research interests are in EDP Auditing and he is director of the Ph.D. EDP Auditing Program at the University of Houston.
