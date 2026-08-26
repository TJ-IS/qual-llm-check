---
otero_id: 24794
otero_key: "2PUD5PZ3"
title: "Software Processes and Project Performance"
authors: "Christopher Deephouse; Tridas Mukhopadhyay; Dennis R. Goldenson; Marc I. Kellner"
year: "1995"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1995.11518097"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Software Processes and Project Performance

Christopher Deephouse, Tridas Mukhopadhyay, Dennis R. Goldenson & Marc I. Kellner

To cite this article: Christopher Deephouse, Tridas Mukhopadhyay, Dennis R. Goldenson & Marc I. Kellner (1995) Software Processes and Project Performance, Journal of Management Information Systems, 12:3, 187-205, DOI: 10.1080/07421222.1995.11518097

To link to this article: http://dx.doi.org/10.1080/07421222.1995.11518097

![](/api/attachments/2PUD5PZ3/fulltext/images/99e8f134541c1f3e20aacccaded79f21157bb8f94f6419054879d98a070e1628.jpg)

Published online: 11 Dec 2015.

![](/api/attachments/2PUD5PZ3/fulltext/images/182875e0a8d9d4e1b1e9fd0e1a087007c66296d299f093e75672f73333629034.jpg)

Submit your article to this journal ↗

![](/api/attachments/2PUD5PZ3/fulltext/images/bbcc7ac00b506f858c570df776569518a1ab961a3988d4ba1f6a3665f6eb56da.jpg)

View related articles ↗

![](/api/attachments/2PUD5PZ3/fulltext/images/89c7e3f85cdfdf6f78f1f1db1ef8ab70b8efd277cce2a7c7412c6a9981e83dec.jpg)

Citing articles: 4 View citing articles ↗

# Software Processes and Project Performance

CHRISTOPHER DEEPHOUSE, TRIDAS MUKHOPADHYAY, DENNIS R. GOLDENSON, AND MARC I. KELLNER

CHRISTOPHER DEEPHOUSE is currently National Accounts Manager for NetBill $^{™}$ , an electronic commerce project at Carnegie Mellon University. He received his M.S.I.A. degree in information systems from Carnegie Mellon, his M.S. degree in transportation systems from M.I.T., and his B.S.E. degree in operations research and economics from Princeton University. His current research focuses on design, planning, and coordination processes in software engineering. Prior to coming to Carnegie Mellon, he was a founding partner for eight years at Sundance Software, Inc., a New York software consulting company. Previously, he worked at General Foods Corporation improving transportation and distribution processes.

TRIDAS MUKHOPADHYAY is an Associate Professor of Industrial Administration at Carnegie Mellon University. He received his Ph.D. in computer and information systems from the University of Michigan. His research interests include business value of information technology, economic impacts of electronic data interchange, software development productivity, and cost analysis. His primary area of interest is the economics of information technology. His research appears in Information Systems Research, Journal of Manufacturing and Operations Management, Journal of Experimental and Theoretical Artificial Intelligence, MIS Quarterly, Omega, IEEE Transactions on Software Engineering, Journal of Operations Management, Accounting Review, Management Science, Journal of Management Information Systems, Decision Support Systems, Journal of Organizational Computing, and other publications. He serves as an editor for Information Systems Research, Journal of Management Information Systems, and Journal of Organizational Computing.

DENNIS R. GOLDENSON is a member of the technical staff at the Software Engineering Institute (SEI). His interests focus on empirical analysis of software engineering process, the results of software process improvement, and the interaction between software tools and software engineering practice. Dr. Goldenson came to SEI over five years ago, after teaching at Carnegie Mellon University since 1982. Currently he is a member of the core trials team of the ISO-SPICE Project and serves as secretary-treasurer of the Foundation for the Empirical Studies of Programmers. He is the author

Acknowledgments: The authors thank Mark Fichman, the reviewers, and the editors of this special issue for their helpful comments. We acknowledge support for this research from the Mellon Foundation and the Software Engineering Institute. Work by Dennis Goldenson and Marc Kellner at the Software Engineering Institute is sponsored by the U.S. Department of Defense. This paper presents views of the authors alone; these views have not been endorsed by Carnegie Mellon University, the United States government, or any agencies thereof. A preliminary version of this paper was presented at the Twenty-Eighth Hawaii International Conference on System Sciences.

of many published papers and professional presentations. He holds a B.A. from Northwestern University and an M.A. and Ph.D. from the University of Minnesota.

MARC I. KELLNER is employed as a senior scientist at the Software Engineering Institute (SEI) at Carnegie Mellon University. He has pioneered and led much of the research on software process modeling conducted at SEI, and has published more than twenty papers on a variety of software process issues. Prior to joining SEI, Dr. Kellner was a professor at Carnegie Mellon, where he established and directed a degree program in information systems. He received his Ph.D. in systems sciences (specializing in MIS) from the Graduate School of Industrial Administration at Carnegie Mellon. His research interests include management and improvement of software processes, software process modeling and definition, software maintenance, and quality management for software. He is a member of the Association for Computing Machinery, the IEEE Computer Society, and the Institute for Operations Research and the Management Sciences.

ABSTRACT: Firms developing software face increasing pressures to improve project outcomes in terms of product quality, productivity, time to market, and customer satisfaction. As projects expand in size and complexity, and competition grows, firms are reengineering their software processes. They are adopting more intensive procedures for requirements management, project planning, defect tracking, configuration management, design and code inspections, and so forth. To assess the effectiveness of these efforts, we conducted a survey of senior practitioners at the 1993 Software Engineering Process Group National Meeting. The survey asked participants about the processes followed on, and the outcome of, a specific software project. Certain practices—notably project planning and cross-functional teams—were consistently associated with favorable outcomes. Based on the survey results, other practices may have little impact on project outcomes.

KEY WORDS AND PHRASES: cross-functional teams, software development processes, software project management, software project planning.

MANAGING SOFTWARE PROJECTS FROM REQUIREMENTS DETERMINATION through implementation is a complex task. Thus, it is not surprising that the performance of software projects has been erratic. Of 500 projects surveyed by DeMarco [11], 15 percent were canceled. Major rework is often required before a software product is accepted. While the system originally developed is unsuitable, frequently much has been learned during the project about the requirements and technical design to warrant further investment. "Several highly productive projects have emerged from the ashes of failed architectures" [8]. Despite the uneven performance of software projects, demand for software continues to grow. Annual expenditures for software development and maintenance are estimated at \$200 billion [4]. Research attention to improving the performance of large-scale systems projects is therefore clearly warranted.

Improvements in software process have been proposed as a way to improve the performance of software organizations [17]. The Software Engineering Institute at Carnegie Mellon University has developed the Capability Maturity Model (CMM) for software [25]. This model classifies the capability of software organizations into five levels. At the lowest level, the chaotic level, no planning or quality control processes are in place. At the highest level, metric data from across the organization are used iteratively to optimize the process used on each project.

Software process assessments using the CMM have been conducted at over 260 sites. Of these sites, 75 percent were classified at the initial, or chaotic, level [32]. Managers in many organizations are pursuing software process improvements. Their top goals are meeting tight schedules and budgets, and improving customer satisfaction [10]. In many cases, software process improvement is regarded as a specialized form of business process reengineering [21].

A software process is a set of semiordered activities performed during the development or evolution of a software product or system $[9]$ . This paper describes an exploratory study that assesses the effectiveness of some processes in common use. The processes studied are project planning, design reviews, cross-functional teams, process training, prototyping, and communication with users. We also consider whether following a consistent process across projects within an organization has an influence on project performance.

If the processes followed influence performance, it is reasonable to ask how this occurred. A plausible explanation is that consistent processes are effective because they reduce the amount of rework that occurs during the project life-cycle. This study also considers the role of rework in mediating the effects of processes.

To explore these research questions, a survey was conducted of experienced software engineers attending the Software Engineering Process Group National Meeting in April 1993. The survey asked participants about the processes followed on, and the outcome of, a specific software project. Certain practices—notably, project planning and cross-functional teams—were consistently associated with favorable outcomes. Based on the survey results, other practices may have little impact on project outcomes.

This paper presents the results of this survey and their implications for software process management. The next section contains a review of recent empirical studies of software processes. We then describe the software processes and other factors covered in the survey, followed by a section describing the method used in creating the survey and administering it at the conference. Responses to the survey are then analyzed and we conclude with a summary of the results, implications for software managers, and directions for further research.

## Empirical Studies of Software Processes

RECENT STUDIES HAVE REPORTED ON THE EFFECTS OF PROCESS CHANGES introduced into a single organization. Three studies are representative of this genre. Best-case results from specific process changes at Schlumberger are cited in Wohlwend [30]. In one example, a site adopted standard project status reporting and reviews. Over a three-year period, the percentage of projects completed on schedule improved from 50 percent to 99 percent while the defect rate declined by over one-third. Humphrey [18] reports on process improvements at Hughes Aircraft. Over a three-year period, the facility studied achieved a \$2 million reduction in budget overruns, representing 6 percent of budgeted work. While it is reasonable to conclude from these articles that the process improvements were effective, there are other plausible explanations, such as easier projects, more experienced staff, and more realistic budgeting.

Dion [12] presents a two-stage model of process improvements at a division of Raytheon. In the first stage, the author measured costs that resulted from quality defects. These activities declined following the introduction of software process improvements. In particular, rework declined from 41 percent to 11 percent of project costs. In the second stage, the author compared the cost of process improvement with productivity increases over the same time period, and concluded that the benefits far exceeded the costs. While this study documents a clearer link between process improvements and overall performance, it does not rule out alternative explanations.

A controlled field study of the effectiveness of software process improvements is very difficult to execute. For example, few organizations will assign two groups to execute the same project using different methods or processes. Most studies to date have compared either before and after conditions, or conditions on pilot projects to baseline projects that used established processes. Since random assignment to conditions is not present, it requires careful consideration and often some faith to conclude that the changes in software process caused the improvements observed.

In this paper, we describe a survey of eighty-seven projects from different organizations. The survey is an alternative method to case studies for exploring the impact of software processes. Surveys are subject to possible biased reporting by respondents. However, as we discuss later in the section on limitations, we chose our survey setting and designed our study to reduce or eliminate bias. Statistical analysis of the survey results is based on the assumption that other determinants of project outcomes are randomly distributed through the population of respondents.

## Conceptual Model

THE CONCEPTUAL MODEL USED IN THIS STUDY is shown in Figure 1. The main effect of software processes on performance is shown horizontally. We propose that the presence or absence of rework may be a mediator [3] of the effectiveness of software processes. We also test the robustness of the main effect by testing interactions with project characteristics. For example, certain processes may be more effective on larger projects or in certain application areas. This section covers the variables included in our study, with some discussion of related variables that have been left out.

## Software Processes

For this exploratory study, we chose to include seven software processes. Each process chosen has received wide attention in the software engineering field. We restricted the processes considered to ones that could be reliably assessed in a survey. Further, we chose processes that would be familiar to respondents and applicable to most projects.

![](/api/attachments/2PUD5PZ3/fulltext/images/3c07aebe25583985cc9a81a77ffc5cc4f7dc0b5e92d95919264ae0d6b951c11e.jpg)  
Figure 1. Conceptual Model  
Processes were also chosen for which some variation in responses could be anticipated. This last criterion eliminated most process areas at the higher maturity levels of the CMM, because these are practiced in relatively few organizations.

## Software Project Planning

The survey included questions regarding frequent failures in project planning: unrealistic plans including schedules and budgets, and failure to identify and manage project risks.

Unrealistic budgets and schedules are frequently adopted, often to close a sale or to gain political advantage. Such plans have negative effects on the conduct of a project, including “loss of managerial control; production of a low-quality, ineffective system; and demotivation of both managers and workers” [24]. Indeed, for a project team that is rewarded for meeting tight budgets and schedules, lowering product quality is a means to success [24]. A large proportion of systems developed to meet unrealistic commitments may be one cause of the high level of software maintenance expenses reported by many firms [14].

Significant risks to software projects take many forms [6]. Observers claim that proactive risk management would benefit most software projects. For example, the Department of Defense now requires explicit risk management on all software projects [6]. Some firms are adopting software processes based on the spiral model [5], which is a risk-driven approach to the software life-cycle.

## Software Process Stability

The CMM recommends that each project should follow a software process that is tailored from the organization's standard process. The management of the project's scope, schedule, staffing, and other resources is tied to this defined process [25]. One possible benefit of following this approach is the easy transfer of knowledge from one project to the next. Since the process followed on each project is based on the standard, successful techniques become routine and exceptions are more salient.

## Software Process Training

Training can be effective to bring newcomers up to speed quickly and to promote adherence to standard operating procedures. Training may include technical material, project management, communication skills, and other topics. This study focuses on software process training. Process training is generally tailored to an organization's defined processes. Hence, organizations providing process training show a commitment to consistently following a defined process.

## Coordination with Users or Customers

Frequent user contact enables the developers to verify details of the requirements, to discuss trade-offs in design alternatives, to get feedback on the work in progress, and to learn as early as possible of changes in requirements affecting the project. Some of the worst software project outcomes are the result of developers creating the wrong system as a result of inadequate communication with the users or customers. Weak communication can occur when a small number of business analysts or contracting agents serve as the sole conduit of information between developers and users. Weak communication can also occur from overreliance on written specifications and change orders. We test for frequent contact between developers and users. Note that if no association is found between frequent contact and performance, it is possible that critical communications did not take place despite frequent contact.

## Design Reviews

Design and code reviews are structured meetings in which a particular work product is examined in detail by a team of peers. A review contrasts with black box testing, in which a known set of outputs are verified for a given set of inputs. In a review, the internal logic and external interfaces of a module are examined manually to ensure that they are accurate, consistent, and robust. Reviews are based on the principle that a group working together will select the best alternative offered by any of the group members. The defects identified during the review are measured, tracked, and corrected before the work product is accepted into the overall system $[16]$ .

## Software Prototyping

Building prototypes of key modules is promoted as a means of verifying the user requirements and the technical feasibility of complex modules $[26]$ . It has been found empirically that “prototyping facilitates communication between users and designers” $[1]$ . The need for building prototypes is explicitly allowed for in the spiral model of software development $[5]$ .

## Cross-Functional Teams

Implementing complex software systems requires a combination of functional and technical expertise. Curtis [8] identifies a project guru as one person who combines both forms of expertise. Such gurus were found on about one-third of a sample of software projects [8]. With no guru, different people combining the required expertise must work in close concert. We used two tests for the presence of expertise during the project phases when it was most likely to be absent. First, we tested for the presence of technical expertise during requirements analysis. Technical experts at this stage should provide a useful schema for integrating details of the requirements, and should help ensure that requirements knowledge is transmitted to the development team. Second, we tested for the presence of functional expertise during development. Functional experts should help identify defects in the system early on when the defects are easiest to correct.

## Software Project Performance

Performance in software development has several dimensions. This paper concentrates on two dimensions: software quality and meeting targets, which include schedules and budgets.

Software quality covers the extent to which the software system meets the actual needs of the intended users. These needs can be diverse. For example, a major software developer conducted a customer satisfaction survey that included seven aspects of software quality: reliability, capability, usability, installability, maintainability, performance, and documentation [19]. We concentrate on capability and usability, because they are significant components of quality across most applications [19].

Meeting targets centers around the fact that, to be successful, a project should be “on time and on budget.” Projects that are late or over budget have a number of consequences. Anticipated benefits of the completed project may be lost or delayed [23]. People on the project generally must stay with the project, instead of moving on to a new one, which would likely delay the next project. A late project could lead to an embarrassing post hoc review of the original decision to start the project or to select a particular group of people to carry it out.

An important issue is the level of realism in the initial schedule and budget. These are often negotiated between the developer and user organizations. Since the users' goal is to minimize costs and completion time, and the developers' goal is to gain the users' agreement to the project, there is a tendency to set unrealistically low targets. Achieving control over commitments is the first step in managing the software process $[17]$ .

There are other criteria for judging the performance of software projects that are not covered in the survey. One criterion is productivity. Improving productivity reduces cost and improves a developer's competitiveness in the marketplace. Project duration—that is, elapsed time—is another dimension of performance. In competitive software markets, quick delivery of new features, and replicating competitors' features, makes a big difference in sales volume. Even in captive markets, rapid satisfaction of user requirements is desirable. These dimensions were not included in this survey because it did not appear feasible to measure them reliably across projects.

## Rework on Software Projects

Major rework has been observed on many software projects [8]. Rework may occur as a result of poor understanding of the requirements or poor technical design. "Our techniques of estimating [software projects] reflect an unvoiced assumption that is quite untrue (i.e., “that all will go well”) [7]. When not planned, as in a prototyping strategy, rework can play havoc with schedules and budgets. Substantial rework often introduces new bugs to a system, lowering overall quality. Our study investigates whether avoiding rework is a significant explanation for the effectiveness of software processes.

## Project Characteristics

We tested for interactions between the effectiveness of software processes and project characteristics. These characteristics included project size, stage (new development or maintenance), and application area (military or nonmilitary). In particular, we tested the assertion of some at the conference where the survey was conducted that software process improvement would not be effective for relatively small, nonmilitary projects.

Good software processes were clearly not the only factor influencing project outcomes. Other factors included the complexity of the application, the stability of the requirements, the capabilities of the team members, and the availability and quality of software tools. A good study of these factors is in Banker [2]. These factors were not included in our study since they would be difficult to assess in a short survey. Further, it was assumed that these factors varied independently from process factors and hence would not affect the impacts of software processes reported here.

## Survey Method

THIS SECTION DESCRIBES THE DESIGN OF THE SURVEY instrument and the methods used for developing and administering it.

## Subjects

The survey was distributed to participants at the Software Engineering Process Group (SEPG) National Meeting, held April 26–29, 1993, in Costa Mesa, California. This conference is sponsored by the Software Engineering Institute (SEI) and the Software Process Improvement Network, an industry group. The topics covered during the conference were similar to the topics in the survey. This similarity should increase the salience of the topics and make the responses more informed.

## Survey Instrument

This study was conducted as part of a broad survey covering software process improvement. In order to cover a variety of material, the survey was divided into two forms, A and B. Each respondent completed only one of the forms. The questions for this study appeared in one section on form B only. The first two questions in this section qualified the respondent to participate in the study (Table 1).

The next nine items covered general characteristics of the project and the

Table 1. Qualifying Questions

1. How many software development or maintenance projects have you worked on, or with, in your organization since January 1, 1990? Include all projects whether you consulted or were directly assigned to them. If ZERO, please skip to the next section.

2. How many of these projects have delivered completed products or modules? If ZERO, please skip to the next section.

Please choose the one project of these with which you are most familiar.

respondent's role on the project. The respondent who skipped these questions was dropped from the analysis. These items were also used as control variables in the ensuing analysis. Most important, these items focused the respondents' attention and recall on a single project, as required for the process and performance questions.

The next page of the survey contained fifteen statements about the project. For each statement, the respondent could check off AGREE, PARTLY AGREE, PARTLY DISAGREE, or DISAGREE. A box for DON'T KNOW was provided to avoid bias from answers where the respondent was unfamiliar with the situation or could not remember. The survey form was pretested by six resident affiliates of the SEI. These are experienced employees of commercial software developers who generally spend a year at SEI working on applied research, development, and technology transition projects. In particular, the pretesters encouraged us to permit responses for projects that occurred as many as forty months before the survey date.

Surveys were distributed at one session of the conference. Forms A and B were placed on alternating chairs so that people seated together from the same organization would respond to different forms. About 84 percent of the surveys were completed at the end of the session and turned in to staff posted at the door. Surveys could also be picked up from the conference registration area after the session. All remaining surveys were turned in to the conference registration area within twenty-four hours.

## Results and Analysis

THREE HUNDRED AND THIRTY-NINE (339) SURVEY RESPONSES were turned in. Given the conference setting, we are unsure of the exact number of surveys distributed. If every eligible conference attendee had received a survey, the response rate would be 69 percent. More likely, the response rate was near 80 percent. Given this high level of response, no further analysis was done on the difference between respondents and nonrespondents.

The survey's target audience was practitioners directly involved in software development organizations. Therefore, it was appropriate to exclude from analysis SEI employees, university professors and staff, and independent consultants. We determined by visual inspection of the conference registration list that 15 percent of the attendees were in these categories. By the same rationale, 25 of the 339 survey responses were excluded from further analysis based on responses to demographic questions on the survey.

Of 165 form B responses, 87 provided project experience data that was analyzed for this paper. Of the 78 excluded, 69 had not worked on a completed project (see the screening questions in the previous section), four skipped either all the project characteristics or all the performance questions, one is an SEI employee, and four reported on one- or two-person projects, which were inappropriate for the process focus of our study.

Of the 87 responses analyzed, 40 percent were from managers and 60 percent from technical staff. They reported a mean of seventeen years of software experience and nine years with their present organization.

## Process and Performance Questions

The fifteen questions on processes and project outcomes are shown in Table 2. The process and performance questions were coded 1 = disagree, 2 = partly disagree, 3 = partly agree, and 4 = agree. Some questions were reverse-scored so that a positive correlation would always support the hypothesis that strong processes improve performance. For the performance questions (dependent variables), missing and don't know responses were omitted from analysis. For the process questions (independent variables), missing and don't know responses were filled in with the average response for that question in order to avoid having to drop the useful data present in the balance of the response. Table 2 includes the mean response and the number of responses for each question.

When two questions were used to assess one variable, the responses to the two questions were averaged. To verify the discriminant validity of these combinations, we checked the correlations between question responses. Significant positive correlations were found among many of the software processes surveyed; projects strong on one process tended to be strong on others. Yet, the correlation of the question responses within a single construct (e.g., planning, process stability, and cross-functional teams) was consistently higher than the correlation between responses included in different constructs.

For the performance variables, the responses to the two questions for meeting targets were highly correlated and the responses for quality were highly correlated. The correlation between meeting targets and quality, while positive, was much lower. As expected, meeting targets and quality were independent dimensions of project performance.

## The Impacts of Process on Performance

The model in Figure 1 was analyzed using generalized least squares and ordered probit methods, with convergent results. Initially, the models were estimated using ordinary least squares. However, strong heteroscedasticity was observed in the results. The models were reestimated using generalized least squares (GLS) to address the heteroscedasticity problem. Tables 2, 3, and 4 show the GLS results. Each column presents a separate regression model. Coefficients that are significant at the p = 0.05 level are marked with a single asterisk (\*). Those significant at p = 0.01 are marked with double asterisks (\*\*).

Table 2. Performance and Process Variables

<table><tr><td>Outcome variables</td><td>Question text</td><td>N</td><td>Mean</td></tr><tr><td>Meeting targets</td><td>1. Project costs exceeded budget. [reverse scored]</td><td>80</td><td>2.138</td></tr><tr><td>Quality</td><td>1. Capabilities of the system fit well with customer or user needs.</td><td>86</td><td>3.547</td></tr><tr><td>Rework</td><td>1. Major rework was required. [reverse scored]</td><td>82</td><td>2.659</td></tr><tr><td colspan="4">Process variables</td></tr><tr><td>Planning</td><td>1. The project plan and estimates were realistic.</td><td>85</td><td>2.435</td></tr><tr><td>Process training</td><td>1. Project team members received training in following the software process.</td><td>85</td><td>2.082</td></tr><tr><td>Stable environment</td><td>1. The software process followed on this project was similar to that on other projects in your organization.</td><td>83</td><td>3.181</td></tr><tr><td>User contact</td><td>1. The technical staff was in frequent contact with eventual users of the software.</td><td>86</td><td>2.860</td></tr><tr><td>Design reviews</td><td>1. A senior team thoroughly reviewed the design.</td><td>82</td><td>2.659</td></tr><tr><td>Prototyping</td><td>1. Prototypes of key modules were built before requirements were frozen.</td><td>84</td><td>2.417</td></tr><tr><td>Cross-functional teams</td><td>1. People with relevant technical expertise contributed to requirements analysis.</td><td>81</td><td>3.383</td></tr></table>

Table 3 shows the results of the GLS analysis for the basic model. For meeting targets, only planning had a significant positive effect. For explaining quality, both planning and cross-functional expertise had a significant positive effect. Stable environment, user contact, and prototype had negative coefficients, though they were not significant.

Linear regression is commonly used for analysis of survey data. The dependent variables in this model, however, used a Likert scale. A Likert scale is an ordinal scale but not an interval scale—that is, the difference between 1 and 2 is not necessarily equivalent to the difference between 2 and 3, and so on. This characteristic violates an assumption of linear regression.

Table 3. Process Impacts on Performance (Generalized Least Squares Regression Estimates)

<table><tr><td rowspan="2">Independent variables</td><td colspan="2">Dependent variable</td></tr><tr><td>Meeting targets</td><td>Quality</td></tr><tr><td>Planning</td><td>**0.791</td><td>*0.228</td></tr><tr><td>Process training</td><td>0.051</td><td>0.060</td></tr><tr><td>Stable environment</td><td>-0.103</td><td>-0.070</td></tr><tr><td>User contact</td><td>-0.122</td><td>-0.018</td></tr><tr><td>Design reviews</td><td>0.003</td><td>0.065</td></tr><tr><td>Prototyping</td><td>-0.044</td><td>-0.028</td></tr><tr><td>Cross-functional teams</td><td>0.101</td><td>**0.406</td></tr><tr><td>Constant</td><td>0.411</td><td>**1.300</td></tr><tr><td>N</td><td>80</td><td>79</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.488</td><td>0.696</td></tr></table>

Ordered probit [31] provides an alternative means of modeling data that requires that only the dependent variable be ordinal. Additional parameters are estimated that account for the potential differences in the interval size in the dependent variable. A brief description of the ordered probit methods used is provided in the appendix.

We analyzed the same model using the ordered probit method. The results were consistent with the generalized least squares analysis. The same coefficients were significant and the signs of the coefficients were in the same direction. The results again showed that planning was a significant predictor of quality and meeting targets. Cross-functional teams were positively associated with quality.

## Reported Planning Effectiveness

There is a possible alternative explanation of the results relating to the effectiveness of planning. The survey questions were intended to measure whether effective planning efforts took place. However, respondents may have had difficulty reporting the effectiveness of planning after the project was complete. They may have allowed the outcome of the project to influence their response as to how well the project was planned. They could have reasoned, “The project was late, so clearly the plan was not realistic.” (The other process questions were much less susceptible to influence from the project outcome. As intended, these questions asked if a particular activity took place. They did not include tests of effectiveness, as were included in the planning questions.)

If this occurred, the planning variable may be considered an outcome and interpreted as “reported planning effectiveness” (RPE). RPE can be modeled as a mediator of the relationship between the other process variables and performance, as shown in Figure 2.

![](/api/attachments/2PUD5PZ3/fulltext/images/029df1233d4c29dff9b018dbb67978d3bf4941f32a8da871c9cfdf5e3aec9c97.jpg)  
Figure 2. Reported Planning Effectiveness as a Mediator

To demonstrate the mediator relationship, three criteria must be met [3]:

• A process variable predicts RPE.

• A process variable predicts performance.

\- When the process variable and RPE are modeled as predictors of performance, the effect (i.e., the coefficient) of the process variable is smaller than when the process variable is modeled alone.

Generalized least squares regression was used to test this model. The results are shown in Table 4. Process training and cross-functional teams had a significant positive relationship with both planning effectiveness and meeting targets. When planning effectiveness was included as an independent variable, the coefficients of process training and cross-functional teams were much lower. F-tests were calculated on the differences in the coefficients. The mediator relationships were statistically significant (p < 0.05). However, stable environment and user contact had a positive effect on planning effectiveness, but this effect did not appear to influence meeting targets.

While process training, a stable environment, and user contact had a positive influence on planning effectiveness (column 4), these processes did not appear to influence quality. Cross-functional teams had a strong positive influence on quality, but planning effectiveness was only a minor mediator, as evidenced by the F-test (one-tailed p = 0.130). Even when planning effectiveness was included in the model, cross-functional teams had a strong positive effect on quality.

## The Mediator Role of Rework

The avoidance of rework can be viewed as an intermediate outcome that is a mediator or mechanism in the link between process and performance. The same procedure was employed to test the mediator role of rework as in the previous section. Table 5 shows the results. The test of a mediator relationship failed for meeting targets. For the projects surveyed, rework was not a significant predictor of meeting targets.

Rework is a significant mediator of the effectiveness of planning and cross-functional teams in improving quality. F-tests were calculated to compare the coefficients in the two quality models. These tests show that good planning and cross-functional teams improve product quality in part by reducing rework.

Table 4. Mediator Role of Reported Planning Effectiveness (Generalized Least Squares Regression Estimates)

<table><tr><td rowspan="2"></td><td colspan="3">Meeting targets model</td><td colspan="3">Quality model</td></tr><tr><td>RPE</td><td>Meeting targets (w/o RPE)</td><td>Meeting targets* (w/RPE)</td><td>RPE</td><td>Quality (w/o RPE)</td><td>Quality* (w/RPE)</td></tr><tr><td>Process training</td><td>**0.276</td><td>**0.315</td><td>0.075</td><td>**0.273</td><td>0.094</td><td>0.006</td></tr><tr><td>Stable environment</td><td>*0.207</td><td>0.008</td><td>-0.087</td><td>0.156</td><td>0.029</td><td>-0.012</td></tr><tr><td>User contact</td><td>*0.190</td><td>-0.001</td><td>-0.101</td><td>*0.197</td><td>0.011</td><td>-0.030</td></tr><tr><td>Design reviews</td><td>-0.041</td><td>-0.027</td><td>-0.019</td><td>-0.090</td><td>0.029</td><td>0.034</td></tr><tr><td>Prototype</td><td>-0.015</td><td>-0.003</td><td>0.020</td><td>-0.076</td><td>0.012</td><td>-0.004</td></tr><tr><td>Cross-functional teams</td><td>**0.540</td><td>**0.538</td><td>0.147</td><td>**0.561</td><td>**0.630</td><td>**0.459</td></tr><tr><td>RPE</td><td></td><td></td><td>**0.690</td><td></td><td></td><td>*0.262</td></tr><tr><td>Constant</td><td>-1.082</td><td>-0.466</td><td>0.233</td><td>-0.702</td><td>0.564</td><td>0.967</td></tr><tr><td>N</td><td>78</td><td>78</td><td>78</td><td>77</td><td>77</td><td>77</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.605</td><td>0.104</td><td>0.171</td><td>0.555</td><td>0.643</td><td>0.711</td></tr></table>

\* Models with the same variables may show different results because different responses were dropped due to missing data.

## Sensitivity to Project Characteristics

Control variables were introduced to the models to test the sensitivity of the results to project characteristics. The five control variables were peak staff level, project length, percentage of outside contracting, and binary variables for military/nonmilitary and new development/maintenance. The estimated coefficients of the process variables are not significantly altered by the introduction of the control variables. In no case did the new estimated coefficient of a process variable differ by more than one-half of the standard error of the original estimate ( $|\beta_{c}-\beta_{o}|<0.5*\sigma_{o}$ ). These results support the robustness of the original model results [21]. In particular, the results reported hold for small as well as large projects.

For meeting targets, none of the control variables was significant. The model with control variables added did not explain significant variance compared with the process only model. For quality, short military projects with big staffs report higher quality, while long, nonmilitary projects with relatively small staffs report lower quality. The difference compared with the process only model was significant $p = 0.039$ . The main effects, however, of the process variables are not mitigated.

Table 5. Mediator Role of Rework (Generalized Least Squares Regression Estimates)

<table><tr><td rowspan="2"></td><td colspan="3">Meeting targets model</td><td colspan="3">Quality model</td></tr><tr><td>Avoidance of rework</td><td>Meeting targets (w/o rework)</td><td>Meeting targets (w/rework)</td><td>Avoidance of rework</td><td>Quality (w/o rework)</td><td>Quality (w/rework)</td></tr><tr><td>Planning</td><td>*0.338</td><td>**0.718</td><td>**0.698</td><td>**0.446</td><td>*0.302</td><td>0.164</td></tr><tr><td>Process training</td><td>0.220</td><td>0.087</td><td>0.077</td><td>0.107</td><td>-0.015</td><td>-0.006</td></tr><tr><td>Stable environment</td><td>-0.188</td><td>-0.093</td><td>-0.080</td><td>0.035</td><td>-0.035</td><td>-0.052</td></tr><tr><td>User contact</td><td>-0.212</td><td>-0.146</td><td>-0.131</td><td>*-0.260</td><td>-0.038</td><td>0.062</td></tr><tr><td>Design reviews</td><td>-0.058</td><td>0.013</td><td>0.022</td><td>-0.059</td><td>0.049</td><td>0.089</td></tr><tr><td>Prototype</td><td>0.102</td><td>0.012</td><td>0.003</td><td>0.040</td><td>-0.018</td><td>-0.032</td></tr><tr><td>Cross-functional teams</td><td>**0.694</td><td>0.125</td><td>0.082</td><td>**0.645</td><td>*0.384</td><td>0.175</td></tr><tr><td>Avoidance of rework</td><td></td><td></td><td>0.060</td><td></td><td></td><td>**0.311</td></tr><tr><td>Constant</td><td>0.046</td><td>0.281</td><td>0.253</td><td>-0.152</td><td>*1.235</td><td>*1.144</td></tr><tr><td>N</td><td>78</td><td>78</td><td>78</td><td>75</td><td>75</td><td>75</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.412</td><td>0.160</td><td>0.204</td><td>0.244</td><td>0.666</td><td>0.749</td></tr></table>

## Limitations

A survey of conference participants is limited in the types of information that may be collected and in the accuracy of recall. A field study can explore the topics in more depth and may benefit from access to written records. However, the survey of conference participants provides access to a much larger number and wider diversity of projects than is normally possible in a field study.

In the survey conducted, each process and performance construct was measured by responses to one or two questions. A survey would be preferred that includes several questions per construct. Such a survey would permit a better test of the discriminant validity for each construct. We were limited in the time we could ask of conference participants and chose to include fewer questions to meet this time limit.

Biased recall is a concern in any study of this nature. Fischoff [13] warns against misinterpretation of surveys when participants' values are not fully articulated. People have been shown to adjust behavior towards researcher expectations, unless the behavior is socially undesirable [27]. Bias in recall can be split into three classifications: bias in observation, bias in memory, and bias in beliefs. Bias in observation occurs when a subject pays attention to certain events or characteristics and not to others. The subject matter of the conference helps train the participants to systematically observe events in a software organization. Bias in memory occurs when events or characteristics are forgotten in a nonrandom fashion. The high salience of the subject matter, and the project characteristic questions included in the survey, help to activate recall needed for the later questions. The screening questions and the available "don't know" response provided in the survey were intended to eliminate making up answers when the topic has been forgotten.

Bias in beliefs occurs when a subject's response is (consciously or unconsciously) modified to conform to his or her beliefs about the subject [28]. Such bias is a particular concern for this study, because many subjects have committed a portion of their career to promoting software process improvement. A question was included in the survey to measure the subject's level of involvement in process improvement. We tested statistically for an interaction between this measure and the results reported and found none. In summary, while concerns may remain about the reliability of subjects' recall, specific steps were taken to reduce or eliminate bias.

The survey responses were analyzed using generalized least squares and ordered probit. These techniques do per se indicate that improved processes caused improved performance, or vice versa. The processes were carried out, however, before the outcomes of the projects were known. We used the state-of-the-art statistical techniques in order to test for interactions between processes, and between processes and other factors. Hence, for the statistically significant results reported, we have some basis for claiming that improved processes will benefit performance.

## Discussion and Conclusion

THIS PAPER HAS DESCRIBED AN EXPLORATORY STUDY OF THE EFFECTIVENESS of software processes. We surveyed experienced software engineers attending the Software Engineering Process Group National Meeting. They identified the extent to which seven processes were used on a project they had worked on recently. They also rated project outcomes in terms of meeting budgets and schedules, and product quality, including capability fit and ease of use. Eighty-seven responses were analyzed. Within the limitations of the survey method, the results support the conclusions summarized in Table 6.

The effectiveness of software development is a major concern for managers as software projects continue to grow in size and complexity. In many markets, from military avionics to financial trading, effective software development is a competitive necessity. Continued research into the effectiveness of software processes is clearly warranted.

## Table 6. Key Findings for Software Managers

1. Effective planning appears to be an important determinant of meeting targets, such as schedules and budgets, and of product quality.

2. Process training improves planning effectiveness and has an indirect effect on meeting budgets and schedules. The observed impact of process training on quality is insignificant.

3. Cross-functional teams are an important determinant of product quality. Cross-functional teams also improve planning effectiveness, which, in turn, improves meeting budgets and schedules.

4. Effective planning and cross-functional teams improve product quality in part by reducing the amount of rework. No association was found between the extent of rework and meeting budgets and schedules.

5. This study is inconclusive on the effectiveness of design reviews, prototyping, frequent user contact, and maintaining a stable environment.

6. These results are consistent across a range of project characteristics, including large and small, military and civilian, and new development and maintenance.

Further research should follow two directions. The first is acquiring a richer set of field data. This can be done via some combination of interview, survey, and examination of project artifacts and records. The second direction is connecting this work to empirical and theoretical work on group processes outside of software engineering. Software development should be a fertile environment for testing theories of group processes, and work in other fields can contribute to the development of software engineering processes.

## REFERENCES

1. Alavi, M. An assessment of the prototyping approach to information systems development. Communications of the ACM, 27, 6 (June 1984), 556–563.

2. Banker, R.; Datar, S.; and Kemerer, C. A model to evaluate variables impacting the productivity of software maintenance projects. Management Science, 37, 1 (January 1991), 1–17.

3. Baron, R., and Kenny, D. The moderator-mediator variable distinction in social psychological research: conceptual, strategic, and statistical considerations. Journal of Personality and Social Psychology, 51, 6 (1986), 1173-1182.

4. Boehm, B. Improving software productivity. Computer, 20, 9 (September 1987), 43–57.

5. Boehm, B. A spiral model of software development and enhancement. Computer, 21, 5 (May 1988), 61–72.

6. Boehm, B. Software risk management. ESEC '89. 2nd European Software Engineering Conference Proceedings. Berlin: Springer-Verlag, 1989, pp. 1–19.

7. Brooks, F., Jr. The Mythical Man-Month. Reading, MA: Addison-Wesley, 1975.

8. Curtis, B.; Krasner, H.; and Iscoe, N. A field study of the software design process for large systems. Communications of the ACM (November 1988), 1268–1286.

9. Curtis, B.; Kellner, M.; and Over, J. Process modeling. Communications of the ACM, 35, 9 (September 1992), 75-90.

10. Deephouse, C.; Goldenson, D.; and Kellner, M. Survey of software process improvement,

1993. Pittsburgh: Software Engineering Institute, unpublished working paper, 1993.

11. DeMarco, T., and Lister, T. Peopleware. New York: Dorset House, 1987.

12. Dion, R. Process improvement and the corporate balance sheet. IEEE Software, 10, 4 (July 1993), 28–35.

13. Fischoff, B. Value elicitation. Is there anything in there? American Psychologist (August 1991), 835–847.

14. Gallant, J. Survey finds maintenance problems still escalating. Computerworld, 20, 4 (January 1986).

15. Greene, W. Econometric Analysis. New York: Macmillan, 1993.

16. Hollocker, C.P. Software Reviews and Audits Handbook. New York: Wiley, 1990.

17. Humphrey, W. Managing the Software Process. Reading, MA: Addison-Wesley, 1989.

18. Humphrey, W.; Snyder, T.; and Willis, R. Software process improvement at Hughes Aircraft. IEEE Software, 8, 4 (July 1991), 11–23.

19. Kekre, S.; Krishnan, M.S.; and Srinivasan, K. Drivers of customer satisfaction for software products: implications for design and service support. Management Science (forthcoming).

20. Kellner, M. Software process modeling: value and experience. SEI Technical Review, 1989. Pittsburgh: Software Engineering Institute, 1989.

21. Kellner, M. Reengineering business processes and software. Proceedings of the Software Engineering Techniques Workshop on Software Reengineering. Pittsburgh: SEI, May 1994.

22. Lieberson, S. Control variables. In Making It Count: The Improvement of Social Research and Theory. Berkeley: University of California Press, 1985, pp. 121–151.

23. Mukhopadhyay, T.; Vicinanza, S.; and Prietula, M. Examining the feasibility of a case-reasoning model for software effort estimation. MIS Quarterly, 16, 2 (1992), 155–171.

24. Page-Jones, M. Practical Project Management. New York: Dorset House, 1985.

25. Paulk, M.; Curtis, B.; Chrissis, M.B.; and Weber, C.V. Capability maturity model, version 1.1. IEEE Software, 10, 4 (April 1993), 18–27.

26. Senn, J. Application prototyping. Analysis and Design of Information Systems. New York: McGraw-Hill, 1989, pp. 212–244.

27. Sigall, H.; Aronson, E.; and Van Hoose T. The cooperative subject: myth or reality? Journal of Experimental Social Psychology, 6, 1 (1970), 1–10.

28. Staw, B. Attribution of the “causes” of performance: a general alternative interpretation of cross-sectional research in organizations. Organizational Behavior and Human Performance, 13 (1975), 414–432.

29. Sterman, J. Modeling managerial behavior: misperceptions of feedback in a dynamic decision making experiment. Management Science, 35, 3 (March 1989), 321–339.

30. Wohlwend, H., and Rosenbaum, S. Software improvements in an international company. Proceedings of the Fifteenth International Conference on Software Engineering. Los Alamitos, CA: IEEE Computer Society Press, 1993, pp. 212–220.

31. Zavoina, T., and McElvey, W. A statistical model for the analysis of ordinal level dependent variables. Journal of the Mathematical Society (Summer 1975), 103–120.

32. Zubrow, D., and Herbsleb, J. Software process improvement: an analysis of assessment data and outcomes. Proceedings of the Software Engineering Symposium. Pittsburgh: Software Engineering Institute, August 1994, pp. 21–27.

## APPENDIX: Ordered Probit

ORDERED PROBIT IS USED TO MODEL SITUATIONS where the dependent variable takes on three or more discrete, ordinal, but not interval, values. A common example is a Likert scale response to a survey question.

In ordered probit [31], a latent variable for the “true” response value is assumed to be a function of the independent variables. The difference between the observed response and the latent true response is assumed to have a standard normal distribution.

The models in this paper use an affine combination as follows:

$$
\text { Latent   true   response } = \beta_ {0} + \beta_ {1} * \mathrm{IV} _ {1} + \beta_ {2} * \mathrm{IV} _ {2} + \beta_ {3} * \mathrm{IV} _ {3} + \dots
$$

Maximum likelihood estimation is used to estimate the parameters, $\beta_{0}$ , $\beta_{1}$ , $\beta_{2}$ , $\ldots$ , $\delta_{1}$ , and $\delta_{2}$ , which best fit this mapping. In practice, the likelihood function is transformed by taking its logarithm and inverting the sign. Parameter values that minimize the negative logarithm of a function will maximize the original function. The transformed function is minimized in order to make use of an existing nonlinear estimation tool. For the estimations in this paper, the negative logarithm of the likelihood function for each observation is as follows:

$$
- \log L = - (\text { observed\_response } = 1) * \log (\text { zcf } (- \text { estimate }))
$$

$$
- (\text { observed\_response } = 2) * \log (\text { zcf } (- \text { estimate } + \delta 1) - \text { zcf } (- \text { estimate }))
$$

$$
- (\text { observed\_response } = 3) * \log (\text { zcf } (- \text { estimate } + \delta 2) - \text { zcf } (- \text { estimate } + \delta 1))
$$

$$
- (\text { observed\_response } = 4) * \log (1 - z c f (- \text { estimate } + \delta 2))
$$

where “(observed\_response=n)” is a Boolean variable; “zcf” is the cumulative standard normal distribution function; and “estimate” is the estimated value of the latent true response defined previously.

Ordered probit models are estimated using maximum likelihood. Maximum likelihood estimation is efficient and unbiased for large sample sizes $[15]$ . The models estimated in this paper have seventy-nine to eighty-seven cases, depending on the number of missing values. For samples of this size, ordered probit is marginally appropriate. Use of maximum likelihood estimation with smaller sample sizes has been reported $[2, 29]$ . Given the complementary strengths of GLS and ordered probit, both methods are used in this paper.
