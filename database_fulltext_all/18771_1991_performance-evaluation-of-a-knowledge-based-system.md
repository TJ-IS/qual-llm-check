---
otero_id: 18771
otero_key: "6UYTEHXX"
title: "Performance evaluation of a knowledge-based system"
authors: "Ajay S. Vinze; Douglas R. Vogel; Jay F. Nunamaker"
year: "1991"
journal: "Information & Management"
doi: "10.1016/0378-7206(91)90068-d"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Performance evaluation of a knowledge-based system A validation study

Ajay S. Vinze

Department of Business Analysis and Research, College of Business Administration, Texas A&M University, College Station, TX 77843-4217, USA

Douglas R. Vogel
and Jay F. Nunamaker, Jr.

Department of Management Information Systems, College of Business and Public Administration, University of Arizona, Tucson, AZ 85721, USA

To demonstrate the usefulness of a system, it is important to test it within the boundaries of its limitations. In the case of expert systems, the premise is that the goal of the technology is to enable a non-expert to complete the steps of solving a problem in a way similar to that of an expert. If computer-based systems are to take the lead in problem solving, they must inevitably be subjected to appropriate and adequate validation. In this paper, we present results from a validation study conducted on a knowledge-based system called ICE (Information Center Expert). The ICE system was developed to determine the software requirements of end-users and make appropriate recommendations. It incorporates the expertise of consultants from IBM/Endicott, IBM Tucson and the Center for the Management of Information (CMI) at the University of Arizona. The results reported here are based on the validation exercise conducted for the ICE implementation at the University of Arizona.

Keywords: Knowledge-based systems, Information centers, Expert system validation.

![](/api/attachments/6UYTEHXX/fulltext/images/34e3dd848379ac5baf49a871be8db1c6d71b39306980feaba4fa73d743d06e54.jpg)

![](/api/attachments/6UYTEHXX/fulltext/images/371b432616fd4ffef40c759fae785d64f47c1b649f7ed70d36b22c2e1cff6ada.jpg)

Ajay S. Vinze is an Assistant Professor of Management Information Systems at Texas A&M University. He received an M.B.A. from the University of Connecticut, and a Ph.D. from the University of Arizona. His research interests include business applications for expert systems, intelligent decision support systems, planning systems, and blackboard systems. He has published in journals like the Journal of Management Information Systems, IEEE-Transactions on Systems, and Database.

Douglas R. Vogel is an Assistant Professor of MIS at the University of Arizona. He has been involved with computers and computer systems in various capacities for over 20 years. He received his M.S. in Computer Science from U.C.L.A in 1972 and his Ph.D. in Business Administration from the University of Minnesota in 1986 where he was also research coordinator for the MIS Research Center. His current research interests bridge the business and academic communities in

addressing questions of the impact of management information systems on aspects of interpersonal communication, group decision making, and organizational productivity. Dr. Vogel is also responsible for coordinating University of Arizona electronic meeting system research activities.

![](/api/attachments/6UYTEHXX/fulltext/images/cef73a548c2a4a1f396aa59917985ddade0095252d2f8a39e4ae4998582c031a.jpg)

Jay F. Nunamaker, Jr. is Head of the Department of Management Information Systems and is a Professor of Management Information Systems and Computer Science at the University of Arizona. He received a Ph.D. from Case Institute of Technology in systems engineering and operations research. He was an Associate Professor of Computer Science and Industrial Administration at Purdue University. Dr. Nunamaker joined the faculty at the University of Arizona in 1974 to develop the MIS program. He has authored numerous papers on group decision support systems, the automation of systems, decision support systems for systems analysis and design, and has lectured throughout Europe, Russia, Asia and South America.

![](/api/attachments/6UYTEHXX/fulltext/images/259a049b05347ae7abc6717b50956d2a0333719045416149b77281cb5b350069.jpg)  
Fig. 1. ICE Architecture.

## 1. Introduction

For many organizations, the growth of end user computing is one of the significant developments of the 1980s. An Information Center (IC) is described as an organization specifically designed to produce “guided service to help users help themselves” [16]. In fulfilling this role, the IC commits information system resources and personnel – both end users and management – to an information support theme for technical as well as non-technical users. In a study by Brancheau et al. [3], it was reported that end users expect to be even more dependent on the IC in the future than they are now, and that it will be more important than ever to remain “current” on new applications of technology. Thus, ICs are experiencing increased user expectations, higher demand for integrated applications, and growing pressure to accomplish more with fewer resources.

A major problem that ICs must face is the high rate of turnover in personnel. The proper combination of skills is difficult to find, and contact between qualified individuals and, persons at the high levels of the end user community presents unique visibility and opportunities that result in many job shifts. For ICs, this higher-than-normal turnover rate is a major disruption in the continuity of their consulting services and their relationships with end users. Harmon and King [10] suggest that knowledge systems are particularly helpful in places where “a few key individuals are in short supply...(where) they spend substantial amount of time helping others.”

The Information Center Project at the University of Arizona's Department of Management Information Systems has resulted in the design and implementation of a knowledge-based system to support one of the major activities of information centers, namely, consulting with users to assist them with software selection. The system known as ICE (Information Center Expert) is a rule-based knowledge system intended to be used in consultation with users who wish to make use of software and training resources [24,12].

## 2. ICE Overview

The ICE system models the expertise of consultants at five information center (IC) locations: three at IBM/Endicott, one at IBM/Tucson, and one at the Center for the Management of Information (CMI) in the College of Business and Public Administration at the University of Arizona [24]. The purpose of each of these ICs is “to provide tools and techniques that will allow you to retrieve, analyze, manipulate and present data more effectively…” [25]. Clients of the ICs have ranged from application programmers with extensive skills in use of computers, to engineers and financial analysts who use computer packages as tools to do their jobs more efficiently and effectively, to students and staff who may never have used a computer before. To respond to such diverse users, ICE had to be designed with a flexible architecture that would allow the knowledge base to represent many different and sometimes changing sets of software tools. The architecture of ICE, depicted in Figure 1, was built using ESE/VM, an expert system shell developed by IBM. In addition to the' rule-based implementation, a database defining the software resources of the IC and a procedure for tool selection were also used.

![](/api/attachments/6UYTEHXX/fulltext/images/2c19082a02fa95109705b14b8a9de65138722ae19299e6cbd7ef20f92349aaeb.jpg)  
Fig. 2. Recommendation Format.

There are five major components of the ICE architecture: (1) reasoning control, (2) intelligent dialogue, (3) selection algorithm, (4) maintenance tool for ICE, and (5) tracking facility. Purposes and implementation of these five components are now discussed.

Reasoning Control: This subsystem controls the process of user consultation. In a standard ICE consultation, the flow of control is: collection of the user's background knowledge or profile, analysis of the user's current requirements, and initiation of the selection algorithm. The consultation concludes with software tools being recommended to the user.

Intelligent Dialogue: The inferencing mechanism uses rules to classify the user's tasks and requirements for software tools. The user's response to the system's queries determines the flow of the dialogue, i.e., ICE will ask relevant questions for collecting detailed functionalities of a high-level requirement. Users' background knowledge and requirements for performing their tasks are acquired by this intelligent dialogue subsystem.

Selection Algorithm: Once the user profile has been collected, the reasoning control subsystem initiates the selection algorithm, which tries to match the user's needs and preferences with the functionalities of tools. Tool recommendations are listed, ordered by their confidence level in satisfying the user's needs. Users can check the tool descriptions and learn what consultants are responsible for the suggested tools.

Maintenance Tool for ICE (MTICE): MTICE is used to maintain information about tool resources. Consultants or IC managers use MTICE to add, update, or delete software tools supported by the IC.

Tracking Facility: A tracking system captures consultation results to support the following functions: print out the consultation result for a user, "target marketing" (e.g., use statistical consultation data to identify the audiences for new products and announcing training sessions), and assist software purchasing and supporting decisions.

A consultation session with ICE is concluded with the system's recommending software tools to users. The recommendations include name of the software and a confidence level ascribed to the recommendation (see Figure 2). Confidence levels are used to rank the recommended software, but it is recognized that users may be unfamiliar with the proposed software product. A user option that allows him or her to choose a software product of interest and browse through a short description of it has therefore been incorporated. The system has also been given the capability of providing the name and phone number of an IC consultant who is responsible for each of the different software products recommended.

## 3. Expert System Validation

In comparison with the extensive literature on design and development issues concerning knowledge-based systems, the literature on expert systems addresses the validation concerns only infrequently. The need for validation is, however, pointed out as explaining the relatively small number of documented successful knowledge-based system implementations $[20,8,23,26]$ .

## 3.1 A Brief Literature Review

The validation of knowledge-based systems is defined as “substantiating that a system performs with an acceptable level of accuracy” [19]. This is also referred to as summative evaluation [9,22] because it focuses on the outcomes or the end results. Several approaches to validation have been reported. Decision analysis [13] used the concept of expected utility to judge the alternatives. The theory of measurable multi-attribute value functions was proposed by Dyer and Sarin [6], who extended the work of Keeney and Raiffa [13]. Turing tests [7,4] have been used extensively in the evaluation of MYCIN.

The literature concerning validation of knowledge-based systems is spread along the dimensions of: what to validate, instruments for validation, and techniques for controlling bias [19]. The question of what is to be validated is determined by the stage of development of the system. Validation can be performed for the final outcome of a session with the system, for the reasoning that accompanies the process, or for both the conclusions and the reasoning as the situation warrants. There is consensus in the literature, however, that validation that takes the form of designating an outcome as correct or incorrect is an oversimplification [14]. A more acceptable form of validation provides experts with several categories into which they can classify an outcome, for example: “ideal, acceptable, suboptimal, and unacceptable” [12].

The use of case scenarios to facilitate validation of an expert system is producing encouraging results $[21]$ . There are, however, some concerns about the use of test case scenarios. One of these is that the case coverage may not ensure either the exhaustive testing of all the conditions or the testing of combinations of the conditions $[18,2]$ . It should be recognized that a knowledge-based system cannot recognize scenarios “beyond those for which knowledge is explicitly available” $[15]$ . It is further suggested that knowledge-based systems are still very fragile, and that they do not handle boundary conditions well $[5]$ .

Another concern related to using scenarios for evaluation is the need for defining standards for the correct answer to a problem (in some objective sense), or what a human expert (or a group of them), presented with the same information as is available to the system, says is the correct answer.

A standard for the evaluation of system validity is not clearly definable for all knowledge-based systems. It is the domain that determines the standards to be used for validating a system. As a result, certain domains allow for more definitive evaluation than others. In the testing of MYCIN, several eminent physicians were used as evaluators. Even this distinguished set of experts could not always agree on an acceptable solution and in some cases their evaluations showed prejudice and inconsistency.

## 3.2 Focus for Validation

For ICE to gain acceptance in an organization, it is important to show the validity of its recommendations to both users and IC consultants. The users will not use the system unless they have confidence in the recommendations. Without user cooperation, the system is useless. IC consultants, the alternative source of expertise, must be satisfied with the system if they are to recommend its use to clients. Validation is therefore crucial to the success of the system.

Three criteria are important for validating ICE. The first is the validation of the recommendation given by the system. The advice given by an advising expert system should be similar to the advice that would be received if an expert were consulted.

The second, which is related to the first, is the completeness and consistency of the knowledge base. Recommendations made by the system must be correct, and based on a complete set of facts and correct reasoning using those facts. The experts involved with the construction of the system described here were concerned with this validation standard.

The third emphasizes the point of comparison for validation. In the results, this point of comparison is the average consultant, i.e., the consultant available at the time a user arrives at the IC need not necessarily be the “expert” consultant in a particular area of user need. The consultant should, however, be aware of all the software products available and the general policies of the IC.

Our research conducted included testing ICE for recommendation validity. Although it is difficult to determine what constitutes expert behavior and it is difficult to validate expert systems without first having validated the expertise of the evaluators of the system, the development of an expert system must be followed by its validation.

The validation effort addressed these concerns by dealing with the question:

Is the recommendation given by ICE consistent with that given by an average consultant in the information center?

## 4. Validation of the ICE System

Validation may be defined as a process undertaken to ensure that the problem being addressed is solved correctly and that the solution is useful [17]. ICE introduces a new process for problem solving for IC clientele in an organization, that is, the users now have a choice of experts (human or the system) that may be consulted to obtain a recommendation for their computing requirements. As with any problem solving activity, the determination of the validity of the process is the key to its success [1]. The validation of ICE will help instill confidence in its recommendations for both end users and the IC consultants, allowing it to become a more useful instrument in the IC setting.

The validation of ICE used the case approach, with blind validation that employed a modified form of the Turing tests. A set of 21 cases was used. The set contained three cases for each of the seven categories of software that ICE supports. The cases were constructed to ensure coverage of the conditions addressed by ICE. They were evaluated by IC consultants who were involved in the development of the ICE system but were not members of the group of consultants assisting in the validation process. The problems presented in the cases were solved by both the CMI consultants and volunteers using the ICE system. The experts were asked to review the cases and the two sets of solutions, with the source of each recommendation being masked. The effectiveness of blind evaluation for controlling the bias of the experts judging the performance of knowledge-based system has been shown in studies with MYCIN and Oncocin. The setting, process, results, and concerns with the ICE validation study are now discussed.

## 4.1. The Setting

The validation of ICE was conducted at the Center for the Management of Information (CMI). This established in 1985, operates as an information center for the College of Business. It provides several services to the user community – students and faculty. Helping users select software to meet their needs is one such service. At the time that this study was undertaken, the CMI was staffed with seven consultants and two full-time staff. These full-time employees, CMI managers, were responsible for setting policy related to software recommendations and were well versed with the software package supported by CMI; they therefore were the designated experts for this study. As might be expected, each of the seven consultants had an area of expertise and knew about the software supported by the center. Furthermore, they were aware of the features of all the software packages officially supported by the CMI and were “expert” for some of them.

## 4.2. The Test Cases

The ICE system provides recommendations for seven categories of software: (a) Data Management, (b) Data Analysis, (c) Graphics, (d) Document Preparation, (e) Project Management, (f) Utilities, and (g) Integrated Packages. Case scenarios have been constructed to address each of these. In total, twenty-one were prepared, three per category of software recommended (see appendix A for some examples of them). The cases were based on consultation sessions that had been observed at the five different IC. They represent an attempt to test most of the features that ICE incorporates. The cases were prepared to test the various consultation paths, but in some instances they were restricted to make them reflect more accurately the length and details of a real consultation session.

## 4.3. The Process

Each CMI consultant was given the complete set of 21 cases and a listing of the software packages officially supported by the CMI (see appendix B). The cases were arranged in a different order for each consultant: a random number table was used to order them. After being instructed that recommendations were to be restricted to software officially supported by the CMI, the consultants were asked to make their recommendations for each case. Consultants could recommend more than one software package for any case; moreover, a consultant who felt that any case was not meaningful had the option of not making a recommendation (see appendix C). The experimenters further requested that the cases not be discussed among the consultants before the exercise was completed. A one week period was allotted to complete the cases.

The evaluation used seven graduate students of the M.I.S. Department as their test subjects. Participation was voluntary. Each participant was assigned three cases that were randomly selected from the set of 21. Participants were given a brief demonstration of the ICE system before they attempted their consultations. The tracking subsystem in ICE recorded the resulting recommendations for the various cases. In addition to the recommendation the sequence and contents of the questions and answers in the consultation session were stored by the tracking subsystem. The recorded recommendations were used in the empirical evaluation. The consultation session details, i.e., the questions and answers, helped with the subjective evaluation of consistency and completeness of the ICE knowledge base by the designated experts, the CMI managers.

The recommendations of the consultants were then compiled by bringing together all the solutions and eliminating duplication. The solutions offered by ICE were compiled from the tracking subsystem. The recommendations from the consultants and ICE constituted two solution sets to each of the cases.

The next step was to prepare the cases for evaluation by experts (the two managers of the CMI). The two options, recommendations made by ICE and those made by the consultants, were labeled option A and B respectively and appended at the end of each case. To make this a blind validation, the recommendations generated by ICE and the human consultants were arranged randomly in the A and B categories to mask the identity of the recommender. In this way, any effect of the evaluating expert's bias toward the role of the computer in the IC consultation process were minimized. In a previous study, conducted to evaluate MYCIN, it was observed that the bias of the expert with regard to the use of computers for the given task had a negative effect on the results.

The experts each received copies of the complete set of 21 cases, with two solutions for each. The instructions to the experts asked them to judge the solutions in the context of the case and to categorize their reaction to each solution set as: (1) Option A is better, (2) Option B is better, (3) Both are equally good, and (4) Neither is correct. The experts were aware that the comparison was between solutions given by ICE and those provided by the CMI consultants, but they were not told which option represented which.

## 5. Results

The results of the study were evaluated using the Binomial Goodness-of-Fit test. The first hypothesis to be tested was:

HIO: The ICE system recommendations are as good as the recommendations of the IC consultants.

Table 1  
Raw Scores of the Expert Evaluations.

<table><tr><td></td><td>ICE better</td><td>Consultant better</td><td>Both equal</td><td>Neither acceptable</td></tr><tr><td>Expert 1</td><td>8</td><td>11</td><td>1</td><td>1</td></tr><tr><td>Expert 2</td><td>9</td><td>9</td><td>3</td><td>0</td></tr><tr><td>Total</td><td>17</td><td>20</td><td>4</td><td>1</td></tr></table>

Table 1 presents the raw scores of the expert evaluations of the recommendations made by ICE and the CMI consultants.

The hypothesis being tested was intended to determine whether ICE performs as well as the CMI consultants. With that emphasis, the combined score from the categories “ICE better,” “Both equal,” and “Neither acceptable” can be taken to indicate that ICE performed “as well as” the CMI consultant.

The results of the binomial goodness-of-fit test shown in Table 2 indicated that in 22 cases the experts judged the ICE system to perform “as well as” or “better” than the consultants. Using the binomial test proportion of 0.5000 the null hypothesis could not be rejected because the ‘z’ approximation of a 2-tailed ‘p’ was 0.8774. It could therefore be concluded that the solutions given by ICE were comparable to those given by the consultants.

A second hypothesis was tested to check whether either of the two, ICE or CMI consultants, produced superior results. The hypothesis was:

HO: The frequency of better solutions is the same for both the ICE system and the CMI consultants.

To test this hypothesis, the cases in which ICE and the CMI consultants were judged equally good and scores for instances in which neither was

Binomial Goodness-of-fit Test Results for Hypothesis 1.

Table 3
Binomial Goodness-of-fit Test Results for Hypothesis 2.  
```txt
“as well as”: 17 cases
“not as well as”: 20 cases
Test proportion = 0.5000
Observed proportion = 0.4595
Z approximation (2-tailed p) = 0.7423
```

judged satisfactory were dropped from consideration. Table 3 presents the results.

The results indicate that using a pretest proportion of 0.5000, the null hypothesis could not be rejected because the 'z' approximation of a 2-tailed 'p' is 0.7423. It therefore was concluded that neither of the two processes was clearly superior based on the recommendation. Stated differently, on an average, the two processes provided equally good solutions.

## 6. Discussion

The effectiveness of the validation effort depends primarily on the test cases and the choice of experts. Myers [18] discusses the preparation of test cases for conventional software. Of these, the criteria applied in generating the test cases for ICE can be summarized as: (1) attempt to test every requirement by focusing on both the average and boundary conditions, and (2) push the system to the limits for both scope and error recovery. Previous studies have suggested that the use of test cases for evaluating the performance of an expert system is biased toward the system, as cases are preselected and presented using the correct descriptors from the system's perspective. In an attempt to minimize this, a number of the test cases used for evaluating ICE were borrowed verbatim from consultation sessions observed during the development of ICE. The remaining cases were developed with user participation in order to bring realism to them.

In evaluating ICE, validation was conducted to ascertain if the recommendations made by the system were “correct” for a given scenario: the judgment was made by the designated experts. There was, however, no attempt to validate the judgement of the “experts.” In the case of ICE, the experts were the CMI managers, i.e., the policy makers for the IC. This reduced concern over possible prejudice and inconsistency among experts. By validating the outcome from ICE (based on the perception of the CMI managers), we ensured that the recommendations were consistent with the policies of the information center.

## 7. Conclusion

In conclusion, we can say that the performance of ICE is comparable to that of the consultants at CMI. As a result, it would be fair to say that the real use for ICE is as a front end to the consulting process that will enable CMI consultants to restrict their efforts to exceptional cases, i.e., cases that are not adequately covered by the ICE system. This alteration to the consulting process would enhance the effectiveness of the software selection process for users and also prove helpful to the consultants by reducing the number of consultations requiring their attention. Furthermore, consultants would only need to be consulted for problems within their area of expertise, since ICE can service the average request. The validation effort for ICE has shown that the system can support the IC in such a role. The preliminary feedback from users of ICE at the CMI implementation has confirmed the utility of the ICE system.

## Acknowledgement

The authors would like to thank IBM Corporation for its support of this project. We especially acknowledge the excellent contributions of Fred Wallace and Al Smith, IBM/Tucson; Yiu Leung IBM/Endicott; and Kendall Cliff and Irene Chen, CMI University of Arizona.

## References

[1] Adrion, W.R., M.A. Branstad and J.C. Cherniavsky, "Validation, Verification, and Testing Computer Software," Computing Surveys, Volume 14, Number 2, June, 1982, pp. 159–192.

[2] Boehm, B., J.R. Brown, H. Kasper, M. Lipow, G.J. McLeod and M.J. Merrit, Characteristics of Software Quality, North Holland, 1978.

[3] Brancheau, J.C., D.R. Vogel and J.C. Wetherbe, “An Investigation of the Information Center from the User's Perspective,” DATABASE, Fall, 1985, pp. 4–17.

[4] Buchanan, B.G. and E.H. Shortliffe, Rule-Based Expert Systems: The MYCIN Experiments of the Stanford Heuristic Programming Project, Addison-Wesley, 1984.

[5] Davis, R., “Knowledge-Based Systems,” Science, 231, 1986, pp. 957–963.

[6] Dyer, J.S. and R.K. Sarin, "Measurable Multiattribute Value Functions," Operations Research, Volume 27, Number 4, July-August, 1979.

[7] Gaschnig, J., P. Klahr, H. Pople, E. Shortliffe, and A. Terry, “Evaluation of Expert Systems: Issues and Case Studies,” in Building Expert Systems, Hayes-Roth, F., D.A. Waterman and D.B. Lenat (eds.), Addison-Wesley, Reading, MA, 1983, pp. 241–280.

[8] Green, C.J.R. and M.M. Keyes, “Verification and Validation of Expert Systems,” in IEEE Western Conference on Expert Systems, June 2-4, Anaheim, CA, 1987, pp. 38–43.

[9] Hamilton, S. and N.L. Chervany, “Evaluating Information System Effectiveness-Part I,” MIS Quarterly, September, 1981.

[10] Harmon P. and D. King, Expert Systems: Artificial Intelligence in Business, Wiley, 1985.

[11] Heltne, Mari, M., Ajay S. Vinze, Benn R. Konsynski and Jay F. Nunamaker, Jr., "ICE: Information Center Expert - A Consultation System for Information Center Resource Allocation," DATABASE, Volume 19, Number 2, Summer 1988, pp. 1–15.

[12] Hickam, D.H. et al., “The Treatment Advice of Computer Based Cancer Chemotherapy Protocol Advisor,” Annals of Internal Medicine, Volume 103, Number 6, Part 1, 1985, pp. 928–936.

[13] Keeney, R.L. and H. Raiffa, Decisions with Multiple Objectives: Preferences and Value Tradeoffs, John Wiley and Sons, 1976.

[14] Kulikowski, C.A. and S.H. Weiss, “Representation of Expert Knowledge for Consultation: The Casnet and Expert Projects,” in Artificial Intelligence in Medicine, P. Splovits (ed.), Westview Press, Boulder, CO, 1982, pp. 21–56.

[15] Lane, N.E., “Global Issues in Evaluation of Expert Systems,” in Proceedings of the 1986 IEEE International Conference on Systems; Man, and Cybernetics, pp. 121–125, NJ, 1986.

[16] Leitheiser, R.L., and J. Wetherbe, “Avoiding the Pitfalls of End-User Computing,” MISRC-WP-85-09, MIS Research Center, School of Management, University of Minnesota, 1985.

[17] Liebowitz, Jay, "Useful Approach for Evaluating Expert Systems," Expert Systems, Volume 3, Number 2, April 1986, pp. 86–96.

[18] Myers, G.J., The Art of Software Testing, John Wiley and Sons, New York, NY, 1979.

[19] O'Keefe, R.M., O. Balci and E.P. Smith, "Validating Expert System Performance," IEEE Expert, Winter 1987, pp. 81–90.

[20] O'Leary, D.E., "Validation of Expert Systems-with Applications to Auditing and Accounting Expert Systems," Decision Sciences, Volume 18, 1987, pp. 468-486.

[21] Scambos, E.T., "A Scenario-Based Test Tool for Examining Expert Systems," in Proceedings of the 1986 IEEE International Conference on Systems, Man, and Cybernetics, NJ, 1986, pp. 131-135.

[22] Schriven, M., “The Methodology of Evaluation: Formative and Summative Evaluation,” Evaluating Action Programs, C.H. Weiss (ed.), Allyn and Bacon, Boston, 1972.

[23] Sviokla, J.J., “Business Implications of Knowledge-Based Systems,” Part II, DATABASE, Fall 1986, pp. 5–16.

[24] Vinze Ajay S., “Knowledge-Based Support for Software Selection in Information Centers: Design Criteria, Development Issues, and Empirical Evaluation,” Ph.D. Dissertation, MIS Department, University of Arizona, 1988.

[25] Wallace, Fred., Information Center, IBM Corporation, Tucson, AZ. Interview with ICE developers, June, 1986.

[26] Yu, V.L., B.G. Buchanan, E.H. Shortliffe, S.M. Wraith, R. Davis, A.C. Scott and S.N. Cohen, “Evaluating the Performance of a Computer-Based Consultant,” Computer Programs in Biomedicine, Volume 9, 1979, pp. 95–102.

## Appendix A

## Selected Set of Case Scenarios

## Case 1

Joe has a PC, using it both as a stand-alone PC and as a connection to the host. Joe is proficient in using the computer for text preparation, simple programming, and already uses several software packages in his work.

Current need: Joe has less than 1000 inventory records for which he wants to do the following:

● perform general queries and data retrieval

\- be able to save the queries for re-use

• perform calculations on the data

\- view and edit the stored data

\- prepare simple reports

Joe realizes that his data is subject to frequent changes. He is willing to spend anywhere from 5–20 hours learning a software package to accomplish this task, and wants to work in the PC environment.

## Case 2

Lewis uses a PC exclusively in his work. He rates himself as a “proficient” user and finds himself using the computer with increasing frequency to accomplish his tasks. He has used data base programs, word processing packages and simple graphics programs; he knows Basic and Cobol programming languages.

Now Lewis wants to find a package to assist in a Business Planning activity, and thinks a spreadsheet would help. He needs some quick answers to hypothetical questions about financial issues: to perform “what if” analyses. The analyses are complicated enough that he wants to be able to write his own subroutines.

When the analyses are finished, he needs to prepare a customized report for his manager. The report must include charts of the data.

Lewis is willing to spend up to 20 hours learning the new package, and must work in the PC environment.

## Case 3

Cynthia has been using her PC since she received it as a “dumb” terminal. Over the last few months, with an increase in the data analysis aspect of her work, she is starting to feel irritated by the occasional downtime of the mainframe. In the past, Cynthia has used the mainframe on a very regular basis, and she is very proficient with the programming environment and the software available. Her current need is to be able to:

\- Perform statistical analysis coupled with business financial planning and forecasting.

\- Accomplish statistical analysis of a fairly complex nature, including MANOVA, multiple regression and the like.

\- Incorporate the analysis into business charts and user defined reports.

\- Remain online.

Cynthia wants to find out about software which is available to her in either the VM or the PC environment.

Case 4

Barbara began using the computer last year to prepare memos and letters with a simple word processing package. She has a PC on her desk, with a connection to the host, but she mainly uses the host to receive mail messages. She is eager to expand her skills in taking advantage of what the host has to offer.

Now she has been asked to prepare presentation materials in the form of overhead transparencies. The material includes alphanumeric text as well as graphics, so she requires a package with the following capabilities:

\- different fonts

● varying character sizes

\- library of pre-stored symbols

\- color

Barbara will be entering the data via the keyboard. She is willing to spend up to a week learning the package, as she has been told that she will in the future be preparing many of these presentations for her department. She would like to work in the VM environment.

## Case 5

Jack began using the computer two years ago to prepare documents with PROFS. He has a PC on his desk, with a connection to the host. He knows no programming languages, but has used many of the facilities of the PROFS environment and is eager to expand his knowledge of the VM environment.

Now he has been asked to prepare presentation materials in the form of overhead transparencies as well as paper copies. The material is alphanumeric text, and so he requires the following capabilities.

\- different fonts

● varying character size

\- color

Jack will be entering the data via the keyboard. He is willing to spend around 20 hours learning the package and wishes to work in the VM environment.

Case 6

Olivia is a manager in charge of a project in which 5 other people are working under her. The project has about 30 tasks and involves managing 10 other resources.

Olivia needs the following capabilities from a PC program:

\- resource leveling

\- slack time analysis

● critical path analysis

\- project tracking

Olivia want the facility for defining the work-days on a user-specific calendar. She must provide simple progress reports to her third-level manager. These reports must include PERT and Gantt charts.

Case 7

Wayne has a been using a PC for the past two years. His PC use has been restricted to preparing documents using Word Perfect. His job, however, requires him to do extensive data gathering, and data analysis. Wayne would like to use his PC to help him with data analysis and data retrieval. He does not however want to spend too much time learning several different packages.

Current need:

\- word processing with a spell checker

● ability to perform simple statistical procedures

\- view and edit the data

\- include data into reports being prepared

Wayne enjoys working on the PC and is ready to spend a reasonable amount of time learning any new package.

## Appendix B

Software Packages Supported by the CMI

<table><tr><td>Personal Editor</td><td>VM/AS</td></tr><tr><td>Professional Editor</td><td>SAS</td></tr><tr><td>DisplayWrite 4</td><td>Lotus 123</td></tr><tr><td>Writing Assistant</td><td>Planning Assistant</td></tr><tr><td>DW Assistant</td><td></td></tr><tr><td>PROFS</td><td>Kermit</td></tr><tr><td>Wordstar</td><td>ProComm</td></tr><tr><td>Word Perfect</td><td></td></tr><tr><td></td><td>Smart</td></tr><tr><td>Filing Assistant</td><td>Framework-II</td></tr><tr><td>SQL/QMF/DBEdit</td><td>Sidekick</td></tr><tr><td>S1032</td><td>Superkey</td></tr><tr><td></td><td>Assistant Series</td></tr><tr><td>Graphing Assistant</td><td>Fixed Disk</td></tr><tr><td></td><td>Organizer</td></tr><tr><td>Drawing Assistant</td><td>Lighting</td></tr><tr><td>SlideWrite</td><td>Open Access</td></tr><tr><td>PC Storyboard</td><td>PC Tools</td></tr><tr><td>PC Storyboard Plus</td><td>Norton Utilities</td></tr><tr><td></td><td>PC-Magazine</td></tr><tr><td></td><td>DOS</td></tr></table>

Not all these software packages can be clearly classified into one of the seven categories, as the functionalities overlap.

## Appendix C

Questions accompanying each case to be completed by the CMI Consultant

1. What software package(s) do you recommend for this user? Base your recommendation on the list of software packages supported by the CMI (see the attached list).

2. Explain briefly why you recommend the software above.

3. List any further information that you would like to have had before making a software recommendation to this user.
