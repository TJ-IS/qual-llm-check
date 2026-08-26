---
otero_id: 23110
otero_key: "EGJUASKR"
title: "Reliability factors in business software: volatility, requirements and end‐users"
authors: "Paul L Bowen; Jon Heales; Monthira T Vongphakdi"
year: "2002"
journal: "Information Systems Journal"
doi: "10.1046/j.1365-2575.2002.00128.x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Reliability factors in business software: volatility, requirements and end-users

Paul L Bowen, Jon Heales & Monthira T Vongphakdi

School of Commerce, University of Queensland, Brisbane, Queensland 4072, Australia, e-mail: bowen@lorien.commerce.uq.edu.au, heales@commerce.uq.edu.au

Abstract. Many business-oriented software applications are subject to frequent changes in requirements. This paper shows that, ceteris paribus, increases in the volatility of system requirements decrease the reliability of software. Further, systems that exhibit high volatility during the development phase are likely to have lower reliability during their operational phase. In addition to the typically higher volatility of requirements, end-users who specify the requirements of businessoriented systems are usually less technically oriented than people who specify the requirements of compilers, radar tracking systems or medical equipment. Hence, the characteristics of software reliability problems for business-oriented systems are likely to differ significantly from those of more technically oriented systems.

Keywords: Software reliability, information system volatility, systems requirements, end-user involvement

## INTRODUCTION

Software is playing an increasingly crucial role in critical business processes as computer applications become more diverse and permeate more areas of organizations (Lyu, 1996; Musa et al., 1990). The rapid evolution and the spread of information system technology increases the demand for reliability, because imperfect or faulty software can have dramatic consequences on organizations (Shooman, 1989; Bennett et al., 1996; Leung & Wong, 1997; Tian, 1999). For instance, unreliable software can result in inaccurate or inconsistent updates of data. These data errors can cause erroneous management decisions and result in financial losses.

Examples of software reliability errors abound. Software reliability errors include errors in functional specifications, errors in the implementation of specifications and lack of sufficient validity and other system integrity checks and protection routines. In one instance, the Inland Revenue Service (IRS) billed a taxpayer for more than one billion dollars when she owed less than 70 thousand dollars (Anonymous, 1991). In another example, a computer program at a major bank doubled the amount of alternate transactions (Anonymous, 1988). As a third illustration, a state trooper stopped a motorist when the police computer system erroneously indicated that the motorist was driving the car of someone who had killed another state trooper (Anonymous, 1988).

## NATURE OF SOFTWARE RELIABILITY

Traditionally, software reliability measurements are taken for two types of software. The first is software that has well-defined, stable specifications, in which continuous operation over an extended period of time is important. This software must be highly reliable because it is used widely by a large number of people and provides the basis of information systems infrastructure (Yamamoto et al., 1994). It includes compilers and other system software (Wordsworth, 1991; Khoshgoftaar et al., 1994). The second is safety-critical software. This software causes major concerns for the software engineering community because its failure could be life-threatening or result in extensive damage (Parnas et al., 1990; Leveson, 1991). It includes software used in military and civilian aircraft, nuclear plants and medical devices (Rushby & Von Henke, 1993; Gerhart et al., 1994a,b; May et al., 1995). For both systems infrastructure and safety-critical software, the requirements usually are well defined when the project is initiated and remain stable throughout the development and operational phases.

Although software reliability is an important issue (Daniels & Hughes, 1985; Lyu, 1996; Rook, 1990; Myers, 1994; Kettinger et al., 1997; Tian, 1999), few studies have examined the reliability of business applications. One reason is the cost and time involved in the reliability measurement process (Musa et al., 1990; Rook, 1990). Another is that the evolving nature of business environments changes the information needed (Oei et al., 1994). Software developers often have difficulty responding to all change requests rapidly and accurately, because changes to the software specifications affect all subsequent software development processes in the systems development life cycle (SDLC) (Dekleva, 1992; Banker et al., 1994; Banker & Slaughter, 1997). Processing change requests to existing systems are error prone because:

1 The people making the changes may be mentally focused on other (newer) projects.

2 Different and often less qualified people perform maintenance activities.

3 Time pressures may result in less comprehensive testing than that performed during an initial development cycle.

Consequently, as change requests are implemented, software maintenance personnel have difficulty ensuring that the software retains high levels of reliability. Reliability of any software depends on how well the software functions meet user requirements, that is on its operational reliability (Littlewood, 1980). Software reliability depends on:

1 the correlation between user requirements and software specifications;

2 the correlation between these specifications and the source code.

If software is developed from specifications that correctly reflect user requirements, then software developers can use techniques such as structured programming (Linger et al., 1979), formal specifications and correctness proofs (Reade & Fromme, 1990) and rigorous software testing (Shooman, 1989) to ensure that their source code is reliable (Bendell & Samson, 1985; Daniels & Hughes, 1985; Sommerville, 1989).

Adler et al. (1999) advocate the use of preventative techniques early in software development to reduce the risk of developmental errors. They state that ‘Organisations . . . typically ignore the processes available to reduce the risks early in development’, and go on to advocate the use of risk-avoidance techniques, such as the cleanroom approach, in an effort to improve software reliability.

Information systems become obsolete as the mapping between user requirements and software deteriorates (Heales, 1995, 1998, 2000). Monitoring the reliability of business software can provide an indication of how well user requirements are currently mapped to the corresponding information system. Indications of decreases in the accuracy of this mapping should lead to investigations into the causes of the deterioration, and identify the actions required to correct the current problems and prevent similar problems occurring in the future (Heales, 1998). The process of obtaining user requirements can vary from highly rational and cooperative to acutely political and acrimonious (Newman & Sabherwal, 1991). Problems associated with obtaining requirements in highly political and acrimonious environments are likely to be exacerbated by increases in volatility (the extent to which software changes are needed). Thus, the more volatile the development environment, the less accurate the mapping between user requirements and software specifications. This lack of accuracy results in a decrease in software reliability.

This negative relationship between the volatility of user requirements and software reliability is examined in two ways. First, the relationship is formally demonstrated and, second, statistical testing is used to confirm the relationship. As a result of the data collection methods used, the relationship is shown to extend beyond systems implementation and well into the operational life of the system. The study also investigates the relationship between software reliability, volatility and end-users’ understanding of system requirements.

## SOFTWARE RELIABILITY MODEL

Software reliability measures quantify how well software meets the requirements of the users (Siefert, 1989; Musa et al., 1990; Kokol et al., 1991). Currently, software reliability is addressed in two ways: from a technical perspective and from an end-user perspective (Kokol et al., 1991).

## Technical perspective

The technical perspective considers reliability from the developer’s viewpoint (Musa et al., 1990; Banker et al., 1994). From the technical perspective, software reliability means ensuring that coding errors do not occur, i.e. that specifications are implemented correctly (Weber, 1999). It assumes that specifications are complete and correct (Kokol et al., 1991), and focuses on the mapping from specifications to implemented software. Developers measure technical software reliability by comparing the operation of the software against the specifications, and counting the faults or defects detected during testing. Tools and techniques such as structured programming (Linger et al., 1979), formal specifications (Spivey, 1987), box structures (Mills et al., 1986) and the cleanroom approach (Dyer, 1992; Lokan, 1993; Linger, 1994) can help ensure that specifications are correctly coded.

## End-user perspective

The end-user perspective of software reliability considers how well the implemented software corresponds to current user requirements or expectations (Musa et al., 1990). It focuses on the operational experience and the impact of software failures on that experience. If software fails to meet user expectations, dissatisfaction often develops, irrespective of whether these failures result from specification deficiencies, coding errors or changing requirements.

To integrate the technical and end-user perspectives, Kokol et al. (1991) presented three propositions. First, during the requirement specifications phase, analysts must understand the user requirements and the environment in which the software will operate. The software specifications must correspond to user requirements. Methods and tools used to prepare specifications can include computer-aided software engineering (CASE), prototyping, data flow diagrams, entity relationship diagrams, structured English, decision trees and formal specifications. Second, during the implementation phase, all parts of the specifications should be implemented correctly. Third, the implemented system must be validated, i.e. software developers must ensure that the implemented system represents a correct mapping of the specifications.

The proposed reliability model is based on Lehman’s ‘two-leg’ software process model presented by Kokol et al. (1991). Lehman’s ‘two-leg’ software process model divides the software development process into two phases: the specification phase and the implementation phase. Requirements are transformed into specifications in the former phase and specifications are transformed into the implemented system in the latter phase.

Using Kokol et al.’s perspective, let $\Psi$ represent the mapping from user requirements to specifications and F represent the mapping from specifications to implemented software. Also, let W represent the overall mapping from user requirements to the implemented software (see Figure 1). The total reliability of software, R(W), depends on the reliability of the mapping from user requirements to specifications (analysis and design reliability), R(Y), and the reliability of the mapping from specifications to implemented system (construction and implementation reliability), R(F). That is, with reliability ranging from 0 to 1:

$$
R (\Omega) = R (\Psi) ^ {*} R (\Phi)\tag{1}
$$

The reliability of the mapping from requirements to specifications, R(Y), has been difficult to measure because the quality of this mapping depends on a number of factors including endusers’ inability or unwillingness to articulate their requirements and developers’ preoccupation with technical aspects of the system. For example, when users perceive the system to be a threat, they may resist system development, e.g. by withholding information during requirements elicitation (Keen, 1989; Newman & Sabherwal, 1991). Developers, on the other hand, may concentrate unduly on a new technique or environment to the detriment of delivering a system that meets user requirements in the most effective manner. That is, developers tend to focus on construction and implementation reliability, R(F), rather than total reliability, R(W).

![](/api/attachments/EGJUASKR/fulltext/images/32876e79f867d5c559c9eedb69b136b3ebb0e7ac1a715c23788334ac5e710460.jpg)  
Figure 1. Software reliability model. Adapted from Lehman’s two leg software process model (Kokol et al., 1991).

## PROPOSITIONS

As information becomes more integrated into business processes, producing reliable information systems becomes more crucial (Oei et al., 1994). In business environments, users often have difficulty defining their software requirements because they have insufficient understanding of an entire system and its interfaces with other systems (Doll & Torkzadeh, 1989). In this regard, software project managers in Hong Kong, Finland and the USA considered misunderstanding requirements, improper management of end-user expectations and changing requirements as some of the most important risk factors identified during software development (Keil et al., 1998).

## Volatility and reliability

The dynamic nature of most business environments means that many organizations are confronting rapidly changing information needs. For organizations that are evolving rapidly, defining software requirements becomes even more difficult, because software requirements need to be adjusted continually to support changing circumstances. When user requirements change, analysis and design reliability, R(Y), suffers and the specifications no longer accurately reflect user requirements.

If user requirements change frequently, maintaining construction and implementation reliability, R(F), also becomes more difficult. Systems that undergo frequent modifications often have higher error rates, because each modification represents an opportunity for new errors to be introduced (Banker et al., 1994). Developers have less opportunity and less motivation to test those changes thoroughly.

These arguments lead to:

Proposition 1: Ceteris paribus, increases in the volatility of user requirements are associated with decreases in total software reliability, R(W).

Appendix A contains a proof of proposition 1.

## Source of reliability degradation

Identifying which component, R( ) or R( ), causes greater reductions in total reliability, R( ), can help management to focus their efforts on the more serious exposure. As noted in the previous subsection, increases in requirements volatility negatively affect both construction and implementation reliability, R(F), and analysis and design reliability, R(Y). Recall, however, that many techniques and procedures such as structured programming (Linger et al., 1979), formal specifications and correctness proofs (Reade & Fromme, 1990), and rigorous software testing (Shooman, 1989) can minimize problems with construction and implementation reliability, R(F). CASE, well-designed (e.g. modular) code, configuration management and retention and use of test cases from previous versions of the software can also help to sustain high construction and implementation reliability, R(F), during maintenance activities (Conger, 1994; Dunn & Ullmann, 1994).

Analysis and design activities for business systems are typically social and political processes and often present problems that technically oriented analysts find difficult to resolve (Markus, 1983; Hirschheim & Newman, 1991). Individual end-users must transform their, possibly vague and incomplete mental representations of system requirements into clearly articulated specifications. These specifications are usually represented by data flow diagrams, entity relationship diagrams and other models with which end-users are typically not proficient. This transformation process is affected by the abilities and motivations of the individual endusers and by the experience and communication skills of both the individual end-users and the analysts. Furthermore, analysts must integrate specifications from the individual endusers. The integration requires the identification and resolution of issues of incompleteness, inconsistency and conflict. Activities to ensure construction and implementation reliability benefit from concrete audit trails between specification documents, source code and physically observable program behaviour. In contrast, activities to ensure analysis and design reliability often lack physical audit trails entirely, i.e. no one can directly access or assess endusers’ mental representations.

Although advances are being made in analysis and design activities (Baskerville & Stage, 1996; Kettinger et al., 1997; Jarke, 1998), the new techniques and methodologies are not as rigorous, controllable or measurable as the aforementioned construction and implementation techniques. Indeed, recent studies reveal that defining software requirements, insufficient understanding of systems and their interfaces and improper management of end-user expectations remain difficult problems (Keil et al., 1998; Doll & Torkzadeh, 1989). These problems are likely to be exacerbated by the increased volatility associated with business oriented systems. Hence:

Proposition 2: Decreases in total software reliability, R(W), are more likely to be associated with analysis and design reliability, R(Y), than with construction and implementation relia bility, R(F).

## RESEARCH METHOD

To empirically test the propositions, a single case design with multiple embedded units of analysis was used. (The types of case research designs are: single case design with a single unit of analysis; multiple case design with a single unit of analysis; single case design with multiple embedded units of analysis; and multiple case design with multiple embedded units of analysis.) This approach followed Yin’s (1993) suggestion that ‘a case study research is appropriate when the researcher desires to (a) define the topic broadly, (b) cover contextual conditions and not just the phenomenon of the study and (c) rely on multiple sources of evidence.’ The case study approach provided unique opportunities to gather both quantitative and qualitative evidence about the propositions. Furthermore, triangulation of qualitative and quantitative data improves the validity of the study. Fielding & Fielding (1986) observe that ‘in combining methods, researchers can reveal aspects of the problem that their strongest method would overlook’. Unique quantitative evidence obtained by this study includes statistical tests of the reliability of business information systems. Interesting qualitative evidence includes the identification and exploratory analysis of organization-specific and applicationspecific factors that affect business software reliability. The research design is a multiple embedded design because three application systems were examined.

A metropolitan government law enforcement agency employing 8500 people, of which over 6800 were law enforcement officers, agreed to participate in this research. This site was chosen because of the agency’s desire to improve its information systems environment. Three application systems that differ in terms of the volatility of user requirements were examined. These applications were selected based on the recommendation of the electronic data processing (EDP) application manager. The applications selected may have been subject to selection bias because applications selected by the EDP application manager may not be representative of business software applications at this organization or at other organizations. An examination of the interview transcripts, however, revealed no indication of bias. Test cases used in software testing were based on the researchers’ understanding of the applications and may have biased the software reliability measures. Responses from users used to calculate the estimate of R(W) may be biased because some of the users interviewed were recommended by the analysts.

Application A was developed in a HP/Sybase environment. (Hewlett-Packard 9000 series equipment was specially installed in 1988/89 for application A. Application programs are written in C and embedded SQL under the Sybase relational database management system.)

Applications B and C were developed in a ICL/IDMS environment. (An ICL Super Dual 2958 mainframe was installed in 1984 and later upgraded to a 3980 model in 1986. An integrated database management system (IDMS) based on the network data model is used under the Virtual Machine Engine (VME) operating system. Application programs are mainly written in Cobol.)

Training databases were used to examine all three applications so that the software testing did not impact on daily activities and did not access confidential data stored in the production databases. The ‘Application profiles’ subsection in Research Results provides detailed descriptions of each of the three applications.

Data collection methods included reviewing specification documents and user manuals, performing statistical tests on selected applications, the use of a questionnaire to gather data from project managers and IT staff, and interviewing end-users. The questionnaire is attached as Appendix B. End-user interviews addressed their perceptions of the reliability and volatility of each application that they use on a regular basis. A copy of the interview guide with pro-forma questions is attached as Appendix C. Reliability and volatility of the three applications were also discussed with the analysts and the application manager.

Data collection took 7.5 weeks. Reviewing specification documents and user manuals, and performing statistical tests took the 4.5 weeks. Interviewing end-users took the remaining 3 weeks.

## CONSTRUCTS MEASUREMENT

Statistical software testing (also referred to as statistical usage testing, software functional testing or random testing) was used to calculate the reliability measures. Given the organizational constraints associated with the case study, the data sampling and collection procedures followed those recommended for cleanroom software engineering as much as possible (Dyer, 1992 Linger, 1994; Walton et al., 1995). The reliability measurements correspond to the measure proposed by Cheung (1980).

## Volatility

The volatility of user requirements was derived from questionnaires. The questionnaire is attached as Appendix B. Two questions were used to determine the volatility. Respondents were asked to answer questions relating to changes during system development. First ‘how often did the system specification requirements change during the development of the software?’ A seven-point Likert scale ranging from ‘No changes’ to ‘Frequent changes’ was used to collect responses (Q\_FREQ). Second, respondents were asked, ‘how significant were changes in system specification requirements?’ A seven-point Likert scale ranging from ‘Extremely minor’ to ‘Extremely major’ was used to collect these responses (Q\_SIG). The responses to both questions were highly correlated (R = 0.756, P < 0.01).

Responses to the second question were used to measure volatility. To use the frequency of changes as a proxy for volatility is less appropriate because each change requires some common unit of measure to determine the extent of the change. For example, frequency of changes could lead to a minor field size change being equated to a major database expansion and reorganization. The measure of volatility requires a common way of sizing a given change. The organization did not quantitatively measure the size of changes [such as function points or Lines of Code (LOC)], but personnel did have some idea of how extensive changes were. No record of change requests or changes has been maintained, so change size measures that couple program size with the number of changed modules (or other measures of the extent of change) were impossible to obtain. It was decided to use a measure relating to the significance of changes to proxy for volatility and compare this with a measure relating to the frequency of changes (as a cross-check, because, ceteris paribus, the greater the number of changes, the greater the extent of change). Both the sum of Q\_FREQ and Q\_SIG, i.e. Q\_SUM, and the product Q\_FREQ\*Q\_SIG, i.e. Q\_PROD, were also tested for their association with reliability.

## Construction and implementation reliability, R(F)

Statistical software testing was used to measure the construction and implementation reliability, R(F), of each software application, i.e. the extent to which the system had been constructed and implemented as per the specifications. First, the specifications documents and user manuals were examined to gain an understanding of the applications. Next, the implemented systems were examined to determine whether the implemented system matched the specifications. Because the three applications, especially application B, were too large and too complex to test completely, representative sections of the systems were selected for statistical testing. Moreover, because statistical testing should reflect the expected usage pattern of the software, monthly transaction reports of the production systems were examined and used to determine the distribution of transactions to test.

To measure construction and implementation reliability, R(F), each field on each screen was tested according to the specification documents, i.e. a sample of possible values was tested to see whether the software behaviour matched the specifications. (The specification document for application C was not available because the application was developed in conjunction with other governmental bodies. To understand the functionality of this application, one of the researchers was briefed by the responsible programmer and a training officer. Each briefing took approximately 1.5 hours. Consequently, statistical testing was based on this understanding and the user manual.) For example, data values of a particular field may require master file checks. Testing each field included entering both valid and invalid codes according to typical usage patterns (e.g. where account validation was specified, the screens were tested using valid and invalid account numbers). Correct and incorrect software responses were recorded and tabulated. The estimated reliability of the mapping from specifications to implemented software was calculated as:

$$
\hat {R} (\Phi) = S / N
$$

where S is the total number of correct responses (successes) and N is the total number of test values.

## Total reliability, R(W)

Interviews with end-users were used to measure the total (overall) reliability of the software. Each end-user interview started with an open-ended question about the functionality of the application under study. Users were asked to demonstrate how they usually operate the application, what they liked or disliked about the system, and what was working or not working. For each screen that they displayed, users were asked to assess each data field on the screen. Three end-users were interviewed for application A and three others for application B. Five additional users were interviewed for application ${ \mathsf { C } } ;$ however, two of these interviews were discarded because these users were reluctant to divulge their opinions about the system. (One user seemed unreasonably paranoid that management would obtain and misuse the responses. The other user refused to cooperate meaningfully, apparently because of a ‘why bother?’ attitude.)

Each interview lasted between 0.5 and 2.5 hours. Table 1 shows demographic information about the users.

Because users’ perceptions are the focus of the end-user reliability, if a particular field does not satisfy the users’ expectations in some way then that field is a failure. For example, a particular field may be positioned incorrectly on the screen, or it may display inaccurate information. The estimated value of R(W) was calculated as:

$$
\hat {R} (\Omega) = S ^ {\prime} / N ^ {\prime}
$$

where $S ^ { \prime }$ is the total number of successful data fields and N¢ is the total number of data fields evaluated by the user. Where a field was missing, N¢ was incremented by 1.

The reliability of business software includes the ability of software to detect and prevent erroneous data from being entered and stored in the system. When erroneous data are entered, the reliability of the entire system suffers because of the inaccurate and inconsistent reports the system will produce. Therefore, the quality of input controls that govern the data entering the system play an important role in determining the reliability of an information system. In this research, the measurement of the construction and implementation reliability of the application systems is based on the reliability of input controls.

Table 1. Demographic information for users

<table><tr><td>User no</td><td>Appendix</td><td>Age group (years)</td><td>Position</td><td>No. computer courses</td><td>Involved in development</td><td>Hours using computers (per week)</td><td>Hours using application (per week)</td></tr><tr><td>1</td><td>A</td><td>41–50</td><td>Communications centre operator</td><td>1</td><td>Y</td><td>Over 20</td><td>35</td></tr><tr><td>2</td><td>A</td><td>21–30</td><td>Communications centre operator</td><td>1</td><td>N</td><td>Over 20</td><td>40</td></tr><tr><td>3</td><td>A</td><td>41–50</td><td>Communications centre trainer/operator</td><td>5</td><td>N</td><td>Over 20</td><td>30</td></tr><tr><td>4</td><td>B</td><td>21–30</td><td>Business analyst/testing coordinator/data entry</td><td>3</td><td>Y</td><td>Over 20</td><td>20</td></tr><tr><td>5</td><td>B</td><td>31–40</td><td>Clerical/data entry</td><td>1</td><td>N</td><td>Over 20</td><td>35</td></tr><tr><td>6</td><td>B</td><td>51–60</td><td>Clerical/data entry</td><td>1</td><td>N</td><td>Over 20</td><td>40</td></tr><tr><td>7</td><td>C</td><td>41–50</td><td>Business analyst/Accident investigator</td><td>3</td><td>Y</td><td>Over 20</td><td>1</td></tr><tr><td>8</td><td>C</td><td>31–40</td><td>Accident investigator</td><td>2</td><td>N</td><td>2–5</td><td>3</td></tr><tr><td>9</td><td>C</td><td>31–40</td><td>Accident investigator</td><td>3</td><td>Y</td><td>Over 20</td><td>3</td></tr></table>

Analysis and design reliability, R(Y)

${ \hat { R } } ( \Psi )$ can be derived from $\hat { R } ( \Omega )$ and ${ \hat { R } } ( \Phi )$ . That is:

$$
\hat {R} (\Psi) = \hat {R} (\Omega) / \hat {R} (\Phi)
$$

## RESEARCH RESULTS

This section describes each of the three applications examined, presents the empirical evi dence gathered via the case study and examines how this evidence enhances our understanding of the factors that influence software reliability.

## Application profiles

Application A is a computer-aided despatching system that supports police emergency phone calls. The system has two major functions: first, it records information about reported incidents and, second, it allocates resources, including patrol vehicles, patrol officers and other uni formed officers, to these incidents. The application was developed by the organization’s information systems (IS) department in conjunction with two governmental bodies and a telecommunications company. The application went live in September 1990.

Among the three applications, application A is the most critical and the most sophisticated system. All data entry and resource allocations are performed centrally. Because of the complexity of this application, end-users must attend a 6-week specialized training course before they can use the system. Only trained users are authorized to access application A.

Application B is the largest of the three applications. The system integrates information from four disjoint databases and records information about offences. At the time during which the study was undertaken, the participating organization did not have a corporate data model, i.e. all databases were separate and disjoint. The application was developed by a team of IS staff and user representatives. Application B was completed and went live in November 1994.

All data entry for application B is performed centrally by data entry clerks who were required to complete a 4-week training course. Other end-users with access to this application can only perform queries.

Application C is used to record traffic incidents. The system serves as an electronic copy of the original paper-based forms. During development, a systems analyst, in conjunction with a business analyst, performed the requirements analysis and wrote the specifications. Many of the requirements were dictated by another government office that maintains traffic accident statistics. Application C went live in 1991. After the initial implementation, the formats of source documents were reviewed and some major changes were made to improve the quality of information recorded.

Most of the organization’s staff use application C. All users with access to the application can enter, modify, and query data.

## Quantitative analysis

The construction and implementation reliability, R(F), of each system was measured by using numerous test cases. Because of the size of the applications (especially applications B and C) and the amount of time available, screens were randomly selected for testing. The results of these tests were used to calculate the population proportions (Freund, 1979) for each system, i.e. the estimated construction and implementation reliability, R<sup>ˆ</sup> (F), for each system (see Table 2).

Total software reliability, R(W), was measured using end-user evaluations. The users were asked to assess the reliability of fields on the screens they access with each application. Differences exist in the total number of fields evaluated among users because all users (of the same application) do not access the same screens. These sessions took from 0.5–2 hours for each end-user. Table 3 summarizes these results.

Table 2. Empirical estimates of construction and implementation reliability, R<sup>ˆ</sup> (F)

<table><tr><td>Application</td><td>Number of fields tested</td><td>Unsuccessful fields</td><td>Ratio</td><td> $\hat{R}(\Phi)$ </td></tr><tr><td>A</td><td>268</td><td>6</td><td>262/268</td><td>0.9776</td></tr><tr><td>B</td><td>220</td><td>7</td><td>213/220</td><td>0.9682</td></tr><tr><td>C</td><td>242</td><td>6</td><td>236/242</td><td>0.9752</td></tr></table>

Table 3. Empirical estimates of total reliability, $\hat { R } ( \Omega )$

<table><tr><td rowspan="2">Application</td><td colspan="3">Correct/total</td><td rowspan="2"> $\hat{R}(\Omega)$ </td><td rowspan="2"> $\hat{R}(\Omega)$ </td></tr><tr><td>User 1*</td><td>User 2*</td><td>User 3*</td></tr><tr><td>A</td><td>70/77</td><td>51/55</td><td>53/56</td><td>174/188</td><td>0.9255</td></tr><tr><td>B</td><td>1127/139</td><td>85/87</td><td>121/124</td><td>333/350</td><td>0.9514</td></tr><tr><td>C</td><td>105/116</td><td>121/134</td><td>121/134</td><td>347/384</td><td>0.9036</td></tr></table>

\*The evaluations were by nine different individuals, i.e. no individual evaluated more than one application.

Table 4. Means and confidence intervals for ${ \hat { R } } ( \Psi ) ,$ ${ \hat { R } } ( \Phi )$ and ${ \hat { R } } ( \Omega ) ,$

<table><tr><td>Application</td><td>EDP manager&#x27;s volatility ranking</td><td> $\hat{R}(\Psi)$ </td><td>80% confidence interval of  $\hat{R}(\Psi)$ </td><td> $\hat{R}(\Phi)$ </td><td>80% confidence interval of  $\hat{R}(\Phi)$ </td><td> $\hat{R}(\Omega)$ </td><td>80% confidence interval of  $\hat{R}(\Omega)$ </td></tr><tr><td>A</td><td>Highest</td><td>0.947</td><td>[0.928, 0.966]</td><td>0.978</td><td>[0.966, 0.989]</td><td>0.926</td><td>[0.901, 0.950]</td></tr><tr><td>B</td><td>Middle</td><td>0.983</td><td>[0.973, 0.993]</td><td>0.968</td><td>[0.953, 0.983]</td><td>0.951</td><td>[0.937, 0.966]</td></tr><tr><td>C</td><td>Lowest</td><td>0.927</td><td>[0.908, 0.946]</td><td>0.975</td><td>[0.962, 0.988]</td><td>0.904</td><td>[0.884, 0.923]</td></tr></table>

The estimated analysis and design reliability, ${ \hat { R } } ( \Psi )$ , for each system was derived from ${ \hat { R } } ( \Phi )$ and $\hat { R } ( \Omega )$ . Eighty percent confidence intervals (Zikmund, 1994) were calculated for each system. Table 4 summarizes the results.

Prior to statistical analysis, the variables were examined for accuracy of data entry, and for the fit between their distributions and the assumptions of multivariate analysis. R(W) was found to have a bimodal distribution, and was recoded accordingly. Questionnaire number 7 was found to be a multivariate outlier (Cook’s distance 1.289). To ensure that assumptions relating to normality were not violated, data relating to this questionnaire were removed from the analysis. Tabachnick & Fidell (1996: 134) recommend the removal of variables identified as multivariate outliers using Cook’s distance $> 1 . 0$ as the criterion.

Table 5 shows the correlation coefficients for all dependent and independent variables. Figure 2 shows the graphical relationship between each system and the variables analysed.

Table 6 shows the results of the regressions against the models tested for statistical association. The relationship between total reliability, R(W), and volatility (Q\_SIG) was tested using regression and was found to be significant $( P { < } 0 . 0 5 )$ . The relationships between total reliability, R(W), and Q\_SUM and between total reliability, $R ( \Omega )$ , and Q\_PROD were also significant, indicating that reliability was associated with volatility when measured as a combination of the significance of changes and the number of changes. The relationship between total reliability, R(W), and Q\_FREQ was not significant, indicating that reliability was not significantly associated with the number of changes made to a system. These findings support proposition 1, that increases in the volatility of user requirements are associated with decreases in total software reliability, R(W).

Table 5. Pearson correlation coefficients (P-value)

<table><tr><td></td><td> $R(\Omega)$ </td><td> $R(\Psi)$ </td><td> $R(\Phi)$ </td><td>Q_FREQ</td><td>Q_SIG</td><td>Q_SUM</td><td>Q_PROD</td></tr><tr><td> $R(\Omega)$ </td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $R(\Psi)$ </td><td>0.923**(0.001)</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $R(\Phi)$ </td><td>-0.396(0.332)</td><td>-0.574(0.137)</td><td>1.000</td><td></td><td></td><td></td><td></td></tr><tr><td>Q_FREQ</td><td>-0.667(0.219)</td><td>-0.689(0.198)</td><td>0.112(0.759)</td><td>1.000</td><td></td><td></td><td></td></tr><tr><td>Q_SIG</td><td>-0.913*(0.030)</td><td>-0.864(0.059)</td><td>0.268(0.454)</td><td>0.735*(0.015)</td><td>1.000</td><td></td><td></td></tr><tr><td>Q_SUM</td><td>-0.919*(0.028)</td><td>-0.905*(0.035)</td><td>0.196(0.588)</td><td>0.944**(0.000)</td><td>0.917**(0.000)</td><td>1.000</td><td></td></tr><tr><td>Q_PROD</td><td>-0.955*(0.011)</td><td>-0.935*(0.020)</td><td>0.184(0.610)</td><td>0.879**(0.001)</td><td>0.948**(0.000)</td><td>0.977**(0.000)</td><td>1.000</td></tr></table>

\*Correlation is significant at the 0.05 level (two-tailed).  
\*\*Correlation is significant at the 0.01 level (two-tailed).

Reliability and Volatility Measures  
![](/api/attachments/EGJUASKR/fulltext/images/1c1ac61262443ebf55f24d1ed5c30f040f1d1f52d284a62ecd1b01cc900e976a.jpg)  
Figure 2. Reliability and volatility by system.

The question which relates to total reliability measures reliability at the time the questionnaires were completed, whereas the question which relates to volatility measures the volatility of the system at the time of system development. The significant association between reliability and volatility suggests that systems that experience high volatility during development continue to have lower reliability during their period of operation.

There are several possible explanations for this lower reliability during the operational phase. First, the most likely explanation is that the system continues to be inherently volatile. It is likely that factors causing high volatility are still present unless some specific action has been taken to neutralize them. For example, the systems environment may be subject to a high rate of change (e.g. because of the type of industry within which the organization operates). Implementation of a new system is unlikely to address industry characteristics. Second, the system may be perceived as being less important than other systems. This may lead to a reduced allocation of resources available for making changes, which means that requested changes are not being made, resulting in lower reliability. Third, other factors such as training may act as moderators to the perception that users have of reliability (e.g. with appropriate training on ways to overcome deficiencies with the system, users may happily accept the system as being reliable). Figure 2 shows the relationship between the measures of volatility and total reliability.

Table 6. Regression results for reliability associations

<table><tr><td></td><td>Mean square</td><td>F-value</td><td>t</td><td>Significance</td><td>Unstandardized coefficients</td><td> $R^2$ </td></tr><tr><td colspan="7">Model 1</td></tr><tr><td>Dependent variable, ln(Ω)</td><td>0.004</td><td>210.650</td><td></td><td>0.000</td><td></td><td>0.981</td></tr><tr><td>(Intercept)</td><td></td><td></td><td>-1.041</td><td>0.338</td><td>-0.014</td><td></td></tr><tr><td>ln(Ψ)</td><td></td><td></td><td>17.094</td><td>0.000</td><td>1.084</td><td></td></tr><tr><td>ln(Φ)</td><td></td><td></td><td>0.705</td><td>0.507</td><td>0.331</td><td></td></tr><tr><td colspan="7">Model 2</td></tr><tr><td>Dependent variable, R(Ω)</td><td>0.067</td><td>15.000</td><td></td><td>0.030</td><td></td><td>0.778</td></tr><tr><td>(Intercept)</td><td></td><td></td><td>6.425</td><td>0.008</td><td>3.400</td><td></td></tr><tr><td>Q_SIG</td><td></td><td></td><td>-3.873</td><td>0.030</td><td>-0.500</td><td></td></tr><tr><td colspan="7">Model 3</td></tr><tr><td>Dependent variable, R(Ω)</td><td>0.222</td><td>2.400</td><td></td><td>0.219</td><td></td><td>0.259</td></tr><tr><td>(Intercept)</td><td></td><td></td><td>2.846</td><td>0.065</td><td>3.000</td><td></td></tr><tr><td>Q_FREQ</td><td></td><td></td><td>-1.549</td><td>0.219</td><td>-0.333</td><td></td></tr><tr><td colspan="7">Model 4</td></tr><tr><td>Dependent variable, R(Ω)</td><td>0.062</td><td>16.200</td><td></td><td>0.028</td><td></td><td>0.792</td></tr><tr><td>(Intercept)</td><td></td><td></td><td>6.200</td><td>0.008</td><td>3.875</td><td></td></tr><tr><td>Q_SUM</td><td></td><td></td><td>-4.025</td><td>0.028</td><td>-0.281</td><td></td></tr><tr><td colspan="7">Model 5</td></tr><tr><td>Dependent variable, R(Ω)</td><td>0.035</td><td>30.940</td><td></td><td>0.011</td><td></td><td>0.882</td></tr><tr><td>(Intercept)</td><td></td><td></td><td>10.520</td><td>0.002</td><td>2.811</td><td></td></tr><tr><td>Q_PROD</td><td></td><td></td><td>-5.563</td><td>0.011</td><td>-0.072</td><td></td></tr></table>

To test the source of variability in the dependent variable, total reliability R(W), Equation 1 needs to be restated as a linear relationship between total reliability, R(W), and independent variables analysis and design reliability, R(Y), and construction and implementation reliability, R(F). Restating the relationship as a logarithmic function allows for regression to be used to test the relationship because of the linear nature of the transformed equation (Box et al., 1978), i.e.

Normalised Values of Reliability  
![](/api/attachments/EGJUASKR/fulltext/images/91ca09bae9fb387d15d4a6e68bb763e17fe809cc95131de90fa17b63aeb3d4d0.jpg)  
Figure 3. Total software reliability, R(W), analysis and design reliability, R(Y), and construction and implementation reliability, R(F), by system

$$
\ln (R (\Omega)) = \alpha + \beta_ {1} \ln (R (\Psi)) + \beta_ {2} \ln (R (\Phi)) + \varepsilon
$$

Log analysis and design reliability, ln(R(Y)), and log construction and implementation reliability, ln(R(F)), were regressed against log total reliability, ln(R(W)). The model fit (Montgomery, 1984; Tabachnick & Fidell, 1996) was tested and found to be significant $( P { < } 0 . 0 1 )$ and the normal probability plot of the standardized residuals revealed no significant deviations from the diagonal (although, because independent measures of only two variables are available there is the possibility of a competing theory to explain the variance in total reliability). This result is consistent with the correlations shown in Table 5 and the confidence intervals shown in Table 4. Table 6 shows the results of the analysis. This finding supports proposition 2, that decreases in total software reliability, R(W), are more likely to be associated with analysis and design reliability, $R ( \Psi )$ , than with construction and implementation reliability, R(F). Figure 3 shows total software reliability, R(W), analysis and design reliability, $R ( \Psi )$ , and construction and implementation reliability, R(F), by system.

At an 80% confidence level, which was considered an appropriate level because of the low number of participants and low number of systems examined, the values of ${ \hat { R } } ( \Psi )$ and ${ \hat { R } } ( \Phi )$ for applications A and C support proposition 2: that the mapping from user requirements to specifications, Y, produces more negative effects on total reliability $R ( \Omega )$ , than the mapping from specifications to implemented software, F. Two unexpected results were observed. First, application C did not have the highest estimated total reliability. Second, although not statistically significant, application $\mathsf { B } ^ { \prime } \mathsf { s }$ estimated analysis and design reliability, ${ \hat { R } } ( \Psi )$ , was higher than its estimated construction and implementation reliability, ${ \ddot { R } } ( \Phi )$ . These unexpected results are explored in the following section.

## Qualitative analysis

This subsection explores the organizational and system specific factors that confirm and help to explain the results noted above. It also identifies other factors that affect business software reliability.

## Volatility

Why does application C violate proposition 1, i.e. that information systems subject to less volatile user requirements should exhibit higher reliability? Interview data revealed deficiencies in three areas that contributed to application C’s low reliability: poor end-user understanding of system requirements, volatility of reporting requirements and data quality.

First, prior to designing and implementing application C, end-users did not have a clear understanding of their requirements. One of the end-users involved in the development and implementation of application C said:

When we were doing this system . . . no one had [previous] knowledge of the computerized traffic accident reports. When we asked them what they wanted in terms of reports and we received so little feedback because nobody seemed to know what they wanted. So when we brought the system in, they started saying ‘can we have this? can we have that?’ We went out giving them examples and asked ‘would you like this? would you like that?’ Some users say ‘yes’, some say ‘no.’. . . It was very difficult to get information out from them because they never had the [system] before so they didn’t know what they wanted. I think that applies to a lot of computerized systems when they never had the systems before. They don’t know what they want until they’ve got the system.

In contrast, the requirements for application B, which exhibited the highest overall reliability, were well known to end-users because (a) application B was similar to an international system that the end-users had been using for many years and (b) prototyping efforts during the design and implementation of application B were much more extensive than for application C. Similarly, application A was well known to its users.

Second, application C exhibited highly volatile reporting requirements. End-users agreed with the EDP application manager that the basic requirements of application C were stable. They noted, however, that the requirements for the customized user interfaces initially were poorly understood and underwent frequent changes. One especially troublesome problem was that queries required entering complete and exact search criteria. In contrast, application B allowed wild-card search criteria. An application C user complained that searches required exact specifications of the criteria and that the system was not designed to find ‘near’ matches. This user also noted that the format of reports by clerical personnel who were not present at the scene of the accident were easier to review than the format of the reports by officers on the scene. This difference in ease-of-use often resulted in senior officials basing their decisions on easier-to-use, but second-hand reports, rather than the first-hand and more-expert reports of the officers at the scene of the accident.

Third, application C experienced problems related to data quality. Sources of these problems included (a) inputting codes without on-line selection or verification of the meaning of the codes; (b) inadequate input controls; (c) little intraorganizational communication between people inputting the data and those retrieving the data; and (d) incomplete training of input personnel relative to the expected content and format of long text fields. In relation to entering codes, an application C user recognized that pull down menus and other input aids were needed but had not been implemented. For some attributes, this user stated that input personnel were not inputting the information that query users were looking for, and were entering other data in formats that were not compatible with the search routines. Some required data were not being entered and this user would have to go physically to the originating department to obtain the required data. Applications A and B did not suffer from this problem. Application A required 6 weeks’ training before users could enter data into the system, and application B required 4 weeks’ training for personnel entering data. Perceptions of software reliability are likely to be affected by the quality of the data, i.e. inaccurate data are typically viewed as a problem with the system’s reliability. These problems, especially data quality, partially explain why users evaluated application C’s overall reliability so low.

## Components of software reliability

Why does application B violate proposition 2, that reliability problems are more likely to be associated with analysis and design reliability, R(Y), than construction and implementation reliability, R(F)? First, based on user interviews, application B exhibited a better-than-expected mapping from user requirements to specifications, primarily because the end-users had a better understanding of their own requirements. Application B was modelled after an international system that many of the users had accessed frequently over a number of years, thus there was some familiarity with a similar system in the user community.

Second, application B benefited from extensive interaction and communication between users and analysts. To illustrate, one of the users involved in the design and implementation of application B said:

. . . we piloted the . . . system in one region . . . we then took on board the [feedback] . . . and did some further analysis by talking to other users. . . . We are constantly getting ideas and suggestions of ways to improve [the system] further. We take those [ideas] onboard and each one gets evaluated. Those that are feasible, we put in the system. For example, we find where people make common mistakes and try to improve the wording of an option or the help system.

Although the end-user interviews clearly indicated that better user–analyst communication was desirable for all three systems, user-analyst communication for application B appeared to be the best of the three applications.

Third, as a result of the users’ understanding and the user-analyst communication, application B contained a number of desirable features. These features included easy navigation of screens, synonyms (e.g. toilet and bathroom), drill-down capabilities, more extensive data integrity checks, etc.

Fourth, although users thought additional improvements were needed, end-users of application B seemed more satisfied with data quality than end-users of applications A or C. One user did note, however, that application B’s data quality was highly dependent on the individual officers filling out the reports.

In summary, a better understanding of end-user requirements, extensive interaction and communication between users and analysts, the inclusion of additional user-friendly features, and users’ perceptions of better quality data contributed to the significantly higher overall reliability of application B.

## IMPLICATIONS FOR PRACTICE

## Specifications and software reliability

Based on the empirical results of this study, an organization’s total software reliability can be more easily improved by focusing efforts on performance in the analysis and design phase. In particular, Table 7 presents a number of suggestions that focus on improving communications between end-users, analysts and systems developers. These suggestions facilitate the implementation of a continuing user-requirements validation process as recommended by Flynn & Warhurst (1994) and Nosek & Schwartz (1988).

Table 7. Suggestions for continuously improving analysis and design reliability, ${ \hat { R } } ( \Psi )$

<table><tr><td colspan="2">Suggestion</td></tr><tr><td>1</td><td>Add a function key to allow in-context feedback to analysts and programmers for problems and suggestions</td></tr><tr><td>2</td><td>Make more extensive use of prototyping especially when initial end-user understanding is low</td></tr><tr><td>3</td><td>Select a prototypical end-user with good knowledge of the business application and ensure that this person has adequate time to work closely with analysts and programmers</td></tr><tr><td>4</td><td>Maintain a prioritized wish list</td></tr><tr><td>5</td><td>Create a user group for each major group of applications</td></tr><tr><td>6</td><td>Where possible, change the organizational structure to place the people inputting the data in the same organizational subunit as the people retrieving the data for decisions</td></tr><tr><td>7</td><td>Align performance goals and rewards of input personnel with needs of the people retrieving the data and making decisions based on that data</td></tr><tr><td>8</td><td>Encourage frequent and constructive communication between user groups, especially input and retrieval personnel</td></tr><tr><td>9</td><td>Provide multiple channels for communication between users and analysts and between various groups of users (Keil &amp; Carmel, 1995)</td></tr><tr><td>10</td><td>Use advanced CASE tools to facilitate communications between end-users, analysts, and developers (Gulla, 1996)</td></tr></table>

## Data accuracy

A notable observation from the interviews is that end-users take a very holistic view of information systems, i.e. they evaluate systems reliability relative to both software reliability and data accuracy. The body of literature about data quality is extensive (see Wang et al., 1995, for a summary). A number of techniques and procedures can be used to manage and improve data accuracy (Bowen et al., 1995; Klein, 1998) including statistical sampling (Bowen et al., 1998).

## SUMMARY

This research indicates, first, that the operational reliability of a system, vis-à-vis other systems in the organizational portfolio, is affected by its volatility during the development phase. Second, the analysis and design phase of development contributes more to reliability degradation than the construction and implementation phase. The reasons for these results lie eithe in the system itself being inherently volatile or in the system being perceived to be less important than others. Given knowledge of a system’s volatility during development, management can better plan the allocation of resources to make ongoing changes, or improve reliability with other moderating factors such as training.

Although the analysis and design phase of systems development is widely accepted as the source of information systems development failure, we found no extant empirical research that supports this assertion. This paper provides that evidence by measuring the source of reliability degradation using the software engineering techniques for measuring technical and end-user reliability. These techniques identify the source of software reliability degradation as being the analysis and design phase of systems development. This result lays the groundwork for a more in-depth investigation of sources of reliability degradation that are more closely aligned with a finer breakdown of systems development phases.

## CONCLUSION

## Contributions

This research investigated factors and relationships that affect the reliability of business software. First, the research developed a software reliability model that focuses on the effect on overall business software reliability of the analysis and design phase and the construction and implementation phase. Second, the paper formally proved the intuitive relationship between greater volatility and lower software reliability. Third, the study used statistical software testing to measure the reliability of three business applications. Fourth, the research reported the results of a qualitative analysis of end-user interviews. Fifth, the paper offers suggestions for improving business software reliability, especially for the analysis and design phase. Sixth, the study notes the inexorable link between business end-users’ perception of software reliability and data accuracy.

## Limitations

This research is subject to a number of limitations. First, the three systems examined are a convenience sample selected by officials at the participating organization. Second, even if the reliability characteristics of these three systems are representative of the systems at this organization, they may not be representative of the reliability characteristics of business software at other organizations. Third, both the quantitative and qualitative data represent a snapshot of the reliability of these systems. Fourth, the statistical sample used for the quantitative analysis is smaller than desired. This last limitation is mitigated, at least to some degree, by triangulation of evidence of multiple types, e.g. a proof, quantitative evidence and qualitative evidence.

## Future research

This research provides the impetus for several future research projects that can help to improve the reliability of business software. First, the EDP manager and the end-users expressed substantially different subjective assessments of volatility for application C. These differences indicate a need to develop and validate objective measures of the volatility of business software. Second, the interviews indicated that end-users evaluate the reliability of the entire system, i.e. they focus on data accuracy at least as much as on software reliability. Because data accuracy depends on end-user training, organizational practices and structure, and integrity constraints built into the software, research into how these factors interrelate is likely to provide valuable insights. Third, although rigorous tools, procedures and methodologies exist to ensure construction and implementation reliability, similar mechanisms do not exist to ensure analysis and design reliability. The design and empirical validation of analogous tools, procedures, and methodologies to improve analysis and design reliability for all organizations that purchase, customize, or build business software, need to be undertaken.

This research has identified the analysis and design phase of systems development as being the source of software reliability degradation. Future research should be directed to analysing more accurately which subphases of analysis and design are responsible for the source of software reliability degradation, and why.

The reasons for the association between high volatility during development and low reliability during the period of operation are not clear and should be a subject of further investigation.

## ACKNOWLEDGEMENTS

The authors would like to thank Jim Hann, Fiona Rhode, Rosie Roberts, Ralph Saunders, John Seymour and Ron Weber for their assistance in making collection of the research data possible and for their comments on previous drafts of this paper. Comments from PACIS\_97 reviewers and delegates helped to improve early drafts of this paper. More recent iterations have benefited from the suggestions of the reviewers and editors.

## REFERENCES

Adler, T.R., Leonard, J.G. & Nordgren, R.K. (1999) Improving risk management: moving from risk elimination to risk avoidance. Information and Software Technology, 41, 29–34.

Anonymous. (1988) Software Engineering Notes, 13, 5–12.

Anonymous. (1991) Software Engineering Notes, 16, 10–11.

Banker, R., Datar, S., Kemerer, C. & Zweig, D. (1994) Software Reliability in a Maintenance Environment. Working Paper. Carnegie Mellon University, Pittsburgh, Pennsylvania, USA.

Banker, R.D. & Slaughter, S.A. (1997) A field study of scale economies in software maintenance. Management Science, 43, 1709–1725.

Baskerville, R.L. & Stage, J. (1996) Controlling prototype development through risk analysis. MIS Quarterly, 20, 481–504.

Bendell, A. & Samson, W. (1985) The State of the Art Report. Software Quality and Reliability, 13, 17–26.

Bennett, J.C., Bohoris, G.A., Aspinwall, E.M. & Hall, R.C. (1996) Risk analysis techniques and their application to software development. European Journal of Operational Research, 95, 467–475.

Bowen, P.L., Fuhrer, D.A. & Guess, F.M. (1998) Continuously improving data quality in persistent databases, Data Quality, 4. http://www.dataquality.com/998bowen.htm.

Bowen, P.L., Schneider, G.P. & Fields, K.T. (1995) Managing data quality in client/server environments. IS Audit and Contrology, IV, 28–35.

Box, G.P.P., Hunter, W.G. & Hunter, J.S. (1978) Statistics for Experimenters. John Wiley, New York.

Cheung, R.C. (1980) A user-oriented software reliability model. IEEE Transactions on Software Engineering, SE-6, 118–125.

Cinlar, E. (1975) Introduction to Stochastic Processes, Prentice Hall, Englewood Cliffs, NJ.

Conger, S. (1994) The New Software Engineering, Wadsworth Publishing Co, Belmont, CA.

Daniels, B. & Hughes, M. (1985) A literature survey of computer software reliability. In: The State of the Art Report, Software Quality and Reliability. Bendell, A. & Samson, W. (eds), 13, 17–26.

Dekleva, S.M. (1992) The influence of the information systems development approach on maintenance. MIS Quarterly, 16, 355–372.

Doll, W. & Torkzadeh, G. (1989) A discrepancy model of end-user computing involvement. Management Science, 35, 1151–1171.

Dunn, R.H. & Ullmann, R.S. (1994) TQM for Computer Software, McGraw-Hill, New York.

Dyer, M. (1992) The Cleanroom Approach to Quality Software Development, John Wiley, New York

Fielding, N.G. & Fielding, J.L. (1986) Linking Data. Sage Publications, Beverley Hills, CA.

Flynn, D. & Warhurst, R. (1994) An empirical study of the validation process within requirements determination, Information Systems Journal, 4, 185–212.

Freund, J. (1979) Modern Elementary Statistics, Prentice/Hall International, London.

Gerhart, S., Craigen, D. & Ralston, T. (1994a) Experience with formal methods in critical systems. IEEE Software, 11, 21–29.

Gerhart, S., Craigen, D. & Ralston, T. (1994b) Regulatory case studies. IEEE Software, 11, 30–40.

Gulla, J. (1996) A general explanation component for conceptual modeling in CASE environments. ACM Transactions on Information Systems, 14, 297–329.

Heales, J. (1995) Proceedings of 16th International Conference on Information Systems, DeGross, J.I., Ariav, G., Beath, C., Hoyer, R. & Kemerer, C. (eds), pp. 352–353. ICIS, Pittsburgh, PA.

Heales, J. (1998) Evolutionary and Revolutionary Maintenance of Information System: A Theoretical and Empirical Analysis. PhD dissertation, The University of Queensland, St Lucia, Brisbane, Queensland, Australia.

Heales, J. (2000) In: 21st Annual International Conference on Information Systems, pp. 70–83. ICIS, Brisbane.

Hirschheim, R. & Newman, M. (1991) Symbolism and information systems development: myth, metaphor, and magic. Information Systems Research, 2, 29–62.

Jarke, M. (1998) Requirements tracing. Communications of the ACM, 41, 32–36.

Keen, P. (1989) Information systems and organizational change. Communications sof the ACM, 24, 24–33.

Keil, M. & Carmel, E. (1995) Customer–developer links in

software development. Communications of the ACM, 38, 33–44.

Keil, M., Cule, P.E., Lyytinen, K. & Schmidt, R.C. (1998) A framework for identifying software project risks. Communications of the ACM, 41, 76–83.

Kettinger, W.J., Teng, J.T.C. & Juha, S. (1997) Business process change: a study of methodologies, techniques, and tools. MIS Quarterly, 21, 55–80.

Khoshgoftaar, T.M., Szabo, R.M. & Woodcock, T.G. (1994) An empirical study of program quality during testing and maintenance. Software Quality Journal, 3, 137–151.

Klein, B.D. (1998) Data quality in the practice of consumer product management: evidence from the field, Data Quality, 4. http://www.dataquality.com/998klein.htm.

Kokol, P., Zumer, V. & Stiglic, B. (1991) New Evaluation Framework for Assessing the Reliability of Engineering Software Systems Design Paradigms. In: Reliability and Robustness of Engineering Software II, Brebbia, C. & Ferrante, A. (eds), pp. 173–184. Computational Mechanics Publications, Southampton, UK

Leung, H.K.N. & Wong, P.W.L. (1997) A study of user acceptance tests. Software Quality Journal, 6, 137–149.

Leveson, N. (1991) Software safety in embedded computer systems. Communications of the ACM, 34, 34–46.

Linger, R.C. (1994) Cleanroom process model. IEEE Software, 11, 50–58.

Linger, R., Mills, H. & Witt, B. (1979) Structured Programming: Theory and Practice, Addison-Wesley, Reading, Massachusetts, USA.

Littlewood, B. (1980) Theories of software reliability: how good are they and how can they be improved?, IEEE Transactions on Software Engineering, SE-6, 489–500.

Lokan, C. (1993) The cleanroom process for software de velopment. Australian Computer Journal, 25, 129–134.

Lyu, M.R. (1996) Introduction. In: Handbook of Software Reliability Engineering, Lyu, M.R. (ed), pp. 1–25. IEEE Computer Society Press, Los Alamitos, CA.

Markus, M.L. (1983) Power, politics, and MIS implementation. Communications of the ACM, 26, 430–444.

May, J., Hughes, G. & Lunn, A.D. (1995) Reliability estimation from appropriate testing of plant protection software. Software Engineering Journal, 10, 206–218.

Mills, H.D., Linger, R.C. & Hevner, A.R. (1986) Principles of Information Systems Analysis and Design, Academic Press, Orlando, USA.

Montgomery, D.C. (1984) Design and Analysis of Experi ments, John Wiley, New York.

Musa, J., Iaanino, A. & Okumoto, K. (1987) Software Reliability: Measurement Prediction Application, McGraw-Hill, New York.

Musa, J., Iaanino, A. & Okumoto, K. (1990) Software Reliability: Professional Edition, McGraw-Hill, New York.

Myers, W. (1994) Hard data will lead managers to quality. IEEE Software, 11, 100–101.

Newman, M. & Sabherwal, R. (1991) Information system development: four process scenarios with case studies, Journal of Information Systems, 5, 84–101.

Nosek, J. & Schwartz, R. (1988) User validation of information system requirements: some empirical results. IEEE Transactions on Software Engineering, 14, 1372–1375.

Oei, J., Proper, H. & Falkenberg, E. (1994) Evolving infor mation systems: meeting the ever-changing environment. Information Systems Journal, 4, 213–233.

Parnas, D., Van Schouwen, J. & Kwan, S. (1990) Evaluation of safety-critical software. Communications of the ACM, 33, 636–648.

Reade, C. & Fromme, P. (1990) Formal Methods for Reliability. In: Software Reliability Handbook, Rook, P (ed.), pp. 51–82. Elsevier Applied Science, London; New York.

Rook, P. (1990) Software Reliability Handbook, Elsevie Applied Science, London, England.

Rushby, J.M. & Von Henke, F. (1993) Formal verification of algorithms for critical systems. IEEE Transactions on Software Engineering, 19, 13–23.

Shooman, M. (1989) Software Engineering – Design/ Reliability/Management, McGraw-Hill, New York.

Siefert, D. (1989) International Symposium on Software Reliability Engineering. Computer Society Press, Los Alimitos, CA.

Sommerville, I. (1989) Software Engineering, Addison-Wesley, Workingham, England.

Spivey, M. (1987) The Z Notation: a Reference Manual, Oxford University Research Group, Oxford.

Tabachnick, B.G. & Fidell, L.S. (1996) Using Multivariate Statistics, HarperCollins, New York.

Tian, J. (1999) Measurement and continuous improvement of software reliability throughout software life-cycle. Journal of Systems and Software, 47, 189–195.

Walton, G.H., Poore, J.H. & Trammell, C.J. (1995) Statistical testing of software based on a usage model. Software Practice and Experience, 25, 97–108.

Wang, R.Y., Storey, V. & Firth, C. (1995) A framework for analysis of data quality research. IEEE Transactions on Knowledge and Data Engineering, 7, 623–640.

Weber, R. (1999) Information Systems Control and Audit. Prentice Hall, Upper Saddle Hill, NJ.

Wordsworth, J.B. (1991) Proceedings of the Fifth Annual Z User Meeting, Springer-Verlag, 285–294.

Yamamoto, M., Aizawa, M. & Yamagishi, H. (1994) High-

reliability operating system ACOS-4/XVP. NEC Research and Development, 35, 89–95.

Yin, R. (1993) Applications of Case Study Research, Sage Publications, CA.

Zikmund, W. (1994) Business Research Methods: International Edition, The Dryden Press, Fort Worth, TX.

## Biographies

Jon Heales PhD undertakes research and teaching in the information systems area. His primary research activities revolve around the longevity of information systems and ways to leverage the return on an information systems investment by extending the operational period of stability or by reducing the ongoing costs of maintenance and enhancement. Jon also conducts research into other aspects of information systems development and strategy, including the social aspects of information systems, departmental reorganization in government and its effects on information systems, IS strategic planning and the use of soft systems methodology as a tool to assist in the research of social aspects relating to information systems with particular interest in organizational culture. He worked in industry for 15 years prior to joining academia. His commercial appointments were in the areas of information systems management and computer auditing in the information systems, banking and mining industries.

Paul L. Bowen PhD is Senior Lecturer in Information Systems in the school of Commerce, University of Queensland, Brisbane, Australia. His research activities involve the measurement, control and improvement of information quality. This research includes developing analytical models of data quality, measuring the impact of data errors on decision quality and applying artificial intelligence techniques to the identification and classification of data errors. He also has related research interests in database design, internal controls, end-user queries and software reliability. He has been a systems analyst and project manager at the Oak Ridge National Laboratory and has taught at the University of Tennessee and Auburn University.

Monthira T. Vongphakdi, MInfSys, obtained her degree from The University of Queensland. She is a project manager with Thai Airways, specializing in airline information systems. She has also worked in the information systems area for law enforcement agencies.

## APPENDIX A: VOLATILITY–RELIABILITY PROOF

## Initial definitions

Let $N _ { 1 }$ and $N _ { 2 }$ be two Poisson processes (Cinlar, 1975) associated with two different environments with mean arrival rates $\lambda _ { 1 }$ and $\lambda _ { 2 }$ of changes that affect a common set of software such that $0 < \lambda _ { 1 } < \lambda _ { 2 } < \infty$ , i.e. software requirements in the first environment are less volatile than in the second environment. Let $\lambda _ { 0 }$ be the initial number of discrepancies between the requirements and the software. For a fixed level of usage, a, the expected mean failure rate in envi ronment i at time t is $E I M _ { i } ( t ) J { = } \alpha ( \lambda _ { 0 } + \lambda _ { i } t )$ and the reliability of set of software in environment i is (Musa et al., 1987)

$$
R _ {i} (t) = e ^ {- \alpha (\lambda_ {0} + \lambda_ {i} t) t}
$$

## Proof

By assumption, $\lambda _ { 1 } < \lambda _ { 2 }$ or, equivalently, $- \lambda _ { 1 } > - \lambda _ { 2 }$ . Multiplying both sides of the expression by t and adding the constant $- \lambda _ { 0 }$ yields $- \lambda _ { 0 } - \lambda _ { 1 } t > - \lambda _ { 0 } - \lambda _ { 2 } t .$ . Multiplying both sides of this expression by at gives $- \alpha ( \lambda _ { 0 } + \lambda _ { 1 } t ) t > - \alpha ( \lambda _ { 0 } + \lambda _ { 2 } t ) t$ . Applying the exponential produces

$$
e ^ {- \alpha (\lambda_ {0} + \lambda_ {1} t) t} > e ^ {- \alpha (\lambda_ {0} + \lambda_ {2} t) t}
$$

which, by the definition of reliability above, is equivalent to $R _ { 1 } ( t ) > R _ { 2 } ( t )$ , i.e. ceteris paribus, the reliability of the set of software in the less volatile first environment is greater than the reliability of the same set of software in the more volatile second environment.

## APPENDIX B: QUESTIONNAIRE USED FOR SYSTEM RESEARCH

Name:. Department: Gender: ..

Section One The following group of items pertains to the characteristics of the system. Please circle the most appropriate response.

1. The system has great impact to the organisation's core business. 1 2 3 4 5 6 7 Never Almost never Not usually Uncertain Usually Almost always Always true true true true true trué

2. The system plays a strategic role in the organisation's core competency. 1 2 3 4 5 6 7 Never Almost never Not usually Uncertain Usually Almost always Always true true true true true true

3. The users have the technical knowledge to develop the system. 1 2 3 4 5 6 7 Never Almost never Not usually Uncertain Usually Almost always Always true true true true true true

4. The users have the technical knowledge to operate the system. 1 2 3 4 5 6 7 Never Almost never Not usually Uncertain Usually Almost always Always true true true true true true

5. The users have the technical knowledge to maintain the system 1 2 3 4 5 6 7 Never Almost never Not usually Uncertain Usually Almost always Always true true true true true true

6. The system is decentralised where the hardware, software or data are located at the various sites. 1 2 3 4 5 6 7 Never Almost never Not usually Uncertain Usually Almost always Always true true true true true true

Section Two The following group of items pertains to the relationship between you as a user and your role in system development. Please circle the most appropriate response

1. I am not invited to participate in the systems development. I have no involvement in the development process. I have no control over system development.

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Never true</td><td>Almost never true</td><td>Not usually true</td><td>Uncertain</td><td>Usually true</td><td>Almost always true</td><td>Always true</td></tr><tr><td>1Never true</td><td>2Almost never true</td><td>3Not usually true</td><td>4Uncertain</td><td>5Usually true</td><td>6Almost always true</td><td>7Always true</td></tr></table>

2. My advice is formally solicited through interviews or questionnaires. I have some responsibility to system development. I have an advisory role with some degree of control over the development.

3. I am a design team member of the information systems development group. The system developers and I have equal control in the development process. 1 2 3 4 5 6 7 Never Almost never Not usually Uncertain Usually Almost always Always true true true true true true

4. My department initiates the development of the new system. We develop the system ourselves. I have control over the development process. 1 2 3 4 5 6 7 Never Almost never Not usually Uncertain Usually Almost always Always true true true true true true

5. When I participate in system development, my participation is strictly voluntary. 1 2 3 4 5 6 7 Never Almost never Not usually Uncertain Usually Almost always Always true true true true true trué

Section Three This section contains items pertains to your views as a user regarding the system that you are using.. Please circle the most appropriate response.

1. Does the system provide the information you need?

1 2 3 4 5 6 7 Never Almost never Some of About half Most of Almost always Always the time the time the time

2. Does the system provide sufficient information? 1 2 3 4 5 6 7 Never Almost never Some of About half Most of Almost always Always the time the time the time

3. Are the data accurate? 1 2 3 4 5 6 7 Never Almost never Some of About half Most of Almost always Always the time the time the time

4. Are you satisfied with the accuracy of the system? 1 2 3 4 5 6 7 Never Almost never Some of About half Most of Almost always Always the time the time the time

5. Is the output presented in an understandable format? 1 2 3 4 5 6 7 Never Almost never Some of About half Most of Almost always Always the time the time the time

6. Is the information understandable?

<table><tr><td>1Never</td><td>2Almost never</td><td>3Some of the time</td><td>4About half the time</td><td>5Most of the time</td><td>6Almost always</td><td>7Always</td></tr></table>

1 2 3 4 5 6 7 Never Almost never Some of About half Most of Almost always Always the time the time the time

<table><tr><td>1Never</td><td>2Almost never</td><td>3Some ofthe time</td><td>4About halfthe time</td><td>5Most ofthe time</td><td>6Almost always</td><td>7Always</td></tr></table>

9. Do you get the information in time to use it for the relevant decisions?

<table><tr><td>1 Never</td><td>2 Almost never</td><td>3 Some of the time</td><td>4 About half the time</td><td>5 Most of the time</td><td>6 Almost always</td><td>7 Always</td></tr></table>

10. Does the system provide up-to-date information?

<table><tr><td>1Never</td><td>2Almost never</td><td>3Some ofthe time</td><td>4About halfthe time</td><td>5Most ofthe time</td><td>6Almost always</td><td>7Always</td></tr></table>

11. How adequately do you feel the Information Systems group meets the information processing needs of your area of responsibility? 1 2 3 4 5 6 7 Very poorly Poorly Marginally Adequately More than Well Very well adeguately

12. How adequately do you feel the Information Systems group meets the information processing needs of the broader class of users they serve? 1 2 3 4 5 6 7 Very poorly Poorly Marginally Adequately More than Well Very well adequately

13. How many different types of computer systems, including mainframes and personal computers have you worked with (eg., Macintosh, DEC VAX)? none 3-4 1 5-6 2 more than 6

14. Of the following devices and software, check those that you have used and are familiar with:

keyboard

text editor

colour monitor

numeric key pad

word processor

time-share system

mouse

file manager

workstation

light pen

electronic spreadsheet

personal computer

touch screen

electronic mail

floppy drive

track ball

graphics software

hard drive

joy stick

computer games

compact disk drive

## APPENDIX C: INTERVIEW QUESTIONS

The interview questions consisted of three separate parts. Part 1 measured the completeness aspect of the software reliability. It examined the modules for compliance with the requirement specifications. Part 2 measured the consistency aspect of the software reliability. The users and developers ranked the system in terms of its match to the requirements. Part 3 measured the correctness aspect of the reliability. Each function and module was tested to determine the reliability of the system.

## Part 1

## Completeness

1. The system fulfils all functionality definition in the requirement specifications.

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Never true</td><td>Almost never true</td><td>Not usually true</td><td>Uncertain</td><td>Usually true</td><td>Almost always true</td><td>Always true</td></tr></table>

2. There are no references to non-existent or incomplete documents.

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Never true</td><td>Almost never true</td><td>Not usually true</td><td>Uncertain</td><td>Usually true</td><td>Almost always true</td><td>Always true</td></tr></table>

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Never true</td><td>Almost never true</td><td>Not usually true</td><td>Uncertain</td><td>Usually true</td><td>Almost always true</td><td>Always true</td></tr></table>

## Part 2

## Consistency

4. There is no conflicting usage of internal, external or operational items.

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Never true</td><td>Almost never true</td><td>Not usually true</td><td>Uncertain</td><td>Usually true</td><td>Almost always true</td><td>Always true</td></tr></table>

5. There are no unsatisfactory response times which affect performance.

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Never true</td><td>Almost never true</td><td>Not usually true</td><td>Uncertain</td><td>Usually true</td><td>Almost always true</td><td>Always true</td></tr></table>

6. Each module design is traced back to Requirement Specification.

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Never true</td><td>Almost never true</td><td>Not usually true</td><td>Uncertain</td><td>Usually true</td><td>Almost always true</td><td>Always true</td></tr></table>

## Part 3

## Correctness

7. The modules and controls perform the correct functionality as described in the Requirement Specification.

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Never true</td><td>Almost never true</td><td>Not usually true</td><td>Uncertain</td><td>Usually true</td><td>Almost always true</td><td>Always true</td></tr></table>

8. The modules and controls provide an accurate portrayal of the data.

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Never true</td><td>Almost never true</td><td>Not usually true</td><td>Uncertain</td><td>Usually true</td><td>Almost always true</td><td>Always true</td></tr></table>
