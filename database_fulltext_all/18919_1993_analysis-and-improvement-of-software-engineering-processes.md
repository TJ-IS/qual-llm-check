---
otero_id: 18919
otero_key: "ZWBCXAWN"
title: "Analysis and improvement of software engineering processes"
authors: "Michiel van Genuchten"
year: "1993"
journal: "Information & Management"
doi: "10.1016/0378-7206(93)90024-n"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Applications

# Analysis and improvement of software engineering processes

Michiel van Genuchten

S and P Consulting, Valkenswaard, Netherlands

Data collection and analysis of software engineering processes are a prerequisite for improved software construction. This paper shows some examples of data collection and analysis in practice. We would like to stimulate software engineering organizations to improve their data collection and analysis and, as a result, advance to an improved level of process control. To achieve this, we discuss basic principles and give practical examples; these include analysis of delays, maintenance data, and inspection data.

Keywords: Analysis of software engineering; Delay; Defects; Fagan inspection; S curve; Metrics; Software process.

![](/api/attachments/ZWBCXAWN/fulltext/images/71882529cb5e96c4cfbd7f0430624f14c406a0dccf7a870dcb9269054022a54f.jpg)

Michiel J.I.M. van Genuchten is partner of S&P Consulting. He holds a M.Sc. (1987) and a Ph.D. (1991) from the Eindhoven University of Technology. He was employed by Philips Electronics from 1987 to 1993 and by the Eindhoven University of Technology from 1987 to 1991. His consulting practice and research interests include the topics control and improvement of software engineering, reuse of software, groupware as well as the impact of software on business. Re sults of his work have been published in a book (Towards a software factory, 1992, [7]) and journals such as IEEE Transactions on Software Engineering, Information & Management and Information and Software Technology.

Correspondence to: M. van Genuchten, S and P Consulting, Waalreseweg 17, 5554 HA Valkenswaard, The Netherlands.

## Introduction

The need for data collection is widely acknowledged as an important part software engineering control. This, however, has still not led to substantive data collection in software engineering organizations. A recent survey in the Netherlands showed that 50 percent of the software engineering organizations do not collect any data on their engineering process [14]. Data collection is a necessity for the analysis of the software engineering processes and analysis will be needed to show how to improve those processes. Basili distinguishes between analytic and constructive aspects of software engineering [1]. The distinction leads to activities with associated analytic and constructive methods and tools. Whereas constructive methods and tools are concerned with building products, analytic methods and tools are concerned with analyzing the constructive process and the resulting products. Basili states: “We need to clearly distinguish between the role of constructive and analytic activities. Only improved construction processes will result in higher quality software. Quality cannot be tested or inspected into software. Analytic processes (e.g. quality assurance) cannot serve as a substitute for constructive processes but will provide control of the constructive processes” [1, page 759].

This paper shows some practical examples of data collection and analysis. We hope to stimulate software engineering organizations to improve their data collection and analysis and, as a result, advance to an improved level of process control.

## 1. Annoying questions

The following questions are all too often faced by a lot of software engineering managers.

\- The project has faced a one month delay so far, what is the expected delay in the remainder of the project?

\- Why is the software late?

\- What is the cost of a defect?

\- How many defects are delivered when a product is released to a customer?

These questions are annoying because software engineering managers should be able to answer them, but generally they are not able to do so. An answer is required in quantitative terms, because, as Lord Kelvin already indicated: “when you measure what you are speaking about, and express it in numbers, you know something about it; but when you cannot measure it, when you cannot express it in numbers, your knowledge is of a meagre and unsatisfactory kind”. Software engineering departments should be able to answer those kind of questions for several reasons. Answering the first question is necessary to be able to track a project and ensure that it will be on time. Answering the second question is needed to improve the software process and to be able to finish the next project in time. The cost of a defect and the number of defects should be known in order to be able to determine when to release a software product and how to estimate the maintenance effort.

## 2. Basic principles

The principles we have applied in data collection and analysis are based on publications by Basili [1] and Bemelmans [2], as well as practical experience [6,7]. The principles are:

\- “Local for local” data collection

\- The “closed loop” principle in information systems

\- A focus on continuous improvement

## "Local for local" data collection

The approach to software engineering varies from one organization to another. The differences relate to products, development processes, resources, tools, goals and organizational structures. One consequence is that data collection and analysis methods must be tailored for the environment in which they will be used [1]. Another consequence is that it makes little sense to collect data in one environment and use it in another: a software engineering department can gain most insight from data collected in its own environment.

## The “closed loop” principle in information systems

The second principle is what Bemelmans $[2,7]$ has called “closed loop information supply”. Information systems should be designed in such a way that those who provide input are the main users of its output. Application of this principle results in feedback to the data supplier, providing a number of advantages. Firstly, it forces the data supplier to provide accurate and complete input. The supplier must be involved and care for quality data. Secondly, this principle prevents users of information systems from asking for more information than they need. If not, they again harm themselves, because they will be the ones who have to provide the excess input. The closed loop principle forces the members of the organization to restrict themselves to the data they really need for control.

The closed loop principle can be applied to software engineering. One consequence is that the data collected by engineers should primarily support the engineers in controlling their own work. Time sheets that are filled in every week without feedback are an example of an information system that has not utilized the closed loop principle. These kinds of systems often provide an organization with highly inaccurate and useless data. Another consequence of the closed loop principle is that data suppliers should know for what purpose the data will (and will not) be used. It should be obvious that the data should not be used against the supplier.

## A focus on continuous improvement

The data collection effort will be aimed at events that have been perceived as deficiencies in the software process. The analysis focuses on events, such as delays and defects; such events often take place as a result of software engineering activities. The data collection and analysis can take place during engineering activities, at a time when everybody is interested in the software product and project at hand. Data collection and analysis should provide insight into the causes of the deficiencies, resulting in actions to provide improvement. Most people would agree that delays and defects are examples of deficiencies. It is, however, sometimes unclear whether a one week delay should be regarded as a deficiency or an achievement by a project team that has taken just a little more time than was budgeted for in the unrealistic schedule. We may consider every deficiency as an opportunity for improvement. As a result, it is not a matter of “who is right or wrong” but a matter of “how can we prevent this from happening again.”

The techniques do not require massive data collection. Their forms usually consist of only one page. We believe that a number of small incremental steps towards improvement are better than one big leap. The improvement actions resulting from our studies were incremental rather than revolutionary. The results of one study can lead to some actions for improvement that will probably pinpoint the next analytical study.

## 3. A sequence of analysis and improvement activities

The focus must not only not be on the results, but also on the application of the basic principles and the arrangement of the analysis studies.

## Reasons for delay

The first sequence of activities starts with an analysis of reasons for delay in software development. Such a study has been discussed in $[6,7]$ . The goal of the study was to gain insight into the reasons for delays in software development. Such a simple analysis technique is usually a good way to start analysis and improvement of the software engineering processes. Reasons for delay were determined in cooperation with the project leaders, using the following data collection scheme.

The study can be perceived as an application of the closed loop principle. The data were collected by project leaders. The same data were analyzed by them and their managers in a joint meeting. The analysis increased insight into reasons for delay among project leaders and their managers. It also resulted in actions for improve-

## Table 1

Data determined for each activity.

<table><tr><td></td><td>planned</td><td>actual</td><td>difference</td><td>reason</td></tr><tr><td>effort</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>starting date</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>ending date</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>duration</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

ment that enabled future projects to follow their plans more closely, an outcome of interest to the project leaders.

The “local for local” principle was also of importance in the study. The reasons for delay varied substantially, depending on the department, as experimentation in over ten departments showed. The delays also varied with the phase of the project, as shown in Table 2, which gives the delays in the various phases of the projects for three departments.

Two of the three projects showed a delay, the third one was finished on time and under budget. The data of two of the three departments suggests that the delay in a projects increases towards its end. This insight can be used in the department concerned while tracking a project.

## Tracking a project

The reasons for delay can be used to estimate the delay in the remainder of an ongoing project. The fact that this collected data can be used in estimating the time to complete the project allows the people involved to benefit from the data collection and the analysis. The closed loop principle is applied and the participants of the project benefit from the data collection throughout the project.

Insight in the delay in the first phases can be used to estimate the delay in the remainder of it. It is important to be able to make a convincing estimation early in the project, because control

## Table 2

Percentage of delay for subsequent phases of development. Percentage of delay is defined as: 100 \* ((real lead time-planned lead time)/real lead time).

<table><tr><td></td><td>department 1</td><td>department 2</td><td>department 3</td></tr><tr><td>requirements</td><td>43</td><td>11</td><td>-25</td></tr><tr><td>design</td><td>23</td><td>20</td><td>-8</td></tr><tr><td>implementation</td><td>32</td><td>46</td><td>-1</td></tr></table>

![](/api/attachments/ZWBCXAWN/fulltext/images/0e7233610425d11be773f7f2b55c6647ca936a3af9c7e6ee9f6b46aaabd745be.jpg)  
Fig. 1. The S-curve.

actions can still have a positive effect at that time; e.g. one control action could be a simplification or modification of the functional requirements. If this is accomplished at an early phase, it will result in less development effort.

One way to look at delays and overruns in projects is the S-curve. This technique has been in use in non software development for decades and is discussed in $[10]$ . The application of the S-curve shows that techniques and methods that have been developed in non-software environments, can be applied to software development. The S-curve compares the planned and actual cost of an ongoing project. The curve usually takes the S-shape because the project often starts with a limited number of people; this is followed by a period of many participants, and it is concluded with less people involved. An example is given in Figure 1.

The S-curve has three lines:

\- The Planned line represents the cumulative effort planned to occur until the assumed end date of the activities. The line can be computed from the data available in the project plan.

\- The Actual line represents the cumulative actual effort up to the actual end date of the activities.

\- The Earned value line is needed because the Planned and Actual lines cannot be directly compared: they often differ on both axes; they may show a delay in lead-time and a cost overrun. The earned value line shows the planned effort plotted against the actual end date of the activity.

The Planned, Actual and Earned value line can be compared in pairs. The vertical difference between the Actual line (actual effort versus actual end date) and the Earned value line (planned effort against actual end date) gives the difference in effort. The horizontal difference between the Planned line (planned effort versus planned end date) and the Earned value line (planned effort versus actual end date) gives the difference in lead time.

Extrapolation of the S-curve should be based on the insight of the project leaders which they have gained in managing the project so far. For example, suppose that a 20 percent lead time delay is found in the first phase of the project and that ten of the 40 reasons that were mentioned are related to lack of experience of the team with a new development method. Suppose that five percent (one fourth of 20 percent) of the lead time delay can be ascribed to this lack of experience. The project leaders can be asked to give their view of the impact of such reasons for delay on the remainder of the project. Suppose they expect the problem of lack of experience to double in the remainder of the project. The delay can therefore be expected to be 10 percent. Applying this type of reasoning to all the (groups of) reasons for delay and cost overrun results in an extrapolation of the expected delay for the remainder of the project.

It is not important whether the expected delay is specified in one or two digits. Key to the value of the extrapolation is the fact that the project leaders are involved in the extrapolation and that the method of reasoning is clear and can be verified by anyone who is involved. The insight into both the delays in different phases and the reasons for delay should be used in extrapolating the delay for the rest of the project. It is also recommended that several extrapolations be made, based on different assumptions. We have found that different extrapolations stimulate discussion on the actions that can be taken to avoid the delay that is estimated $[7,13]$ . The goal of the extrapolation is not to predict the delay in the project, but to encourage an early understanding of actions that can avoid further delay.

## Analysis of problem reports

The analysis of reasons for delays has led us to further analysis of maintenance reports. The study of reasons for delays has showed that maintenance is a major reason for delay in development. This has led the department to study causes and consequences of defects. The Goal-Question-Metric paradigm of Basili [1] was used to arrive at a one page data collection sheet. The major goal of the study was to gain insight into the causes and consequences of defects. The major questions were:

\- Where do defects originate?

\- What is the cost of a defect?

\- Are defects that are incurred early in the life cycle more expensive to solve than errors that are incurred later?

Maintenance reports represent the information that is gathered on faults that are detected and solved. The department concerned calls them “problem reports”. If a problem occurs, a problem report is written describing the problem perceived and its correction. Analysis of these reports required additional data collection. Some multiple choice questions were therefore added to the existing reports. Three of these are shown in Table 3.

Over 400 problem reports were analyzed. Table 4 shows the solution time of the fault versus the kind of fault.

Table 4 shows that more than half of the problems were solved within an hour. Requirements errors were as easy to solve as design or implementation errors [7,8]. The results of the study were analyzed by the software engineers, project leaders, the manager and members of the quality assurance department. The analysis yielded some unexpected results. It showed, for example, no relation between the phase in which an error was incurred and the effort required to fix it. In this case the results focused attention on what is perhaps the real problem – that the methods and procedures that were prescribed are not, in fact, being followed – and thus opened an opportunity for improvement.

Table 3  
Three questions related to problem reports.

<table><tr><td>1) How many hours did it take to solve the problem?</td></tr><tr><td>○ Less than one hour</td></tr><tr><td>○ 1 to 2 hours</td></tr><tr><td>○ 2 to 4 hours</td></tr><tr><td>○ 4 to 8 hours</td></tr><tr><td>○ over 8 hours</td></tr><tr><td>2) In what phase did the error occur?</td></tr><tr><td>○ exploration</td></tr><tr><td>○ requirements</td></tr><tr><td>○ design</td></tr><tr><td>○ implementation</td></tr><tr><td>○ other,......</td></tr><tr><td>3) In what test was the fault detected?</td></tr><tr><td>○ integration test</td></tr><tr><td>○ verification test</td></tr><tr><td>○ validation test</td></tr></table>

Table 4  
Solution time versus the kind of error.

<table><tr><td colspan="8">Solution time</td></tr><tr><td>Kind of error</td><td>&lt;1</td><td>1-2</td><td>2-4</td><td>4-8</td><td>&gt;8</td><td>Total</td><td>%</td></tr><tr><td>Requirements</td><td>22</td><td>10</td><td>7</td><td>0</td><td>1</td><td>40</td><td>10</td></tr><tr><td>Design</td><td>12</td><td>8</td><td>6</td><td>1</td><td>4</td><td>31</td><td>7</td></tr><tr><td>Implementation</td><td>93</td><td>37</td><td>15</td><td>6</td><td>12</td><td>163</td><td>40</td></tr><tr><td>Other</td><td>103</td><td>25</td><td>16</td><td>7</td><td>26</td><td>177</td><td>43</td></tr><tr><td>Total</td><td>230</td><td>80</td><td>44</td><td>14</td><td>43</td><td>411</td><td>100</td></tr><tr><td>Percentage</td><td>56</td><td>20</td><td>11</td><td>3</td><td>10</td><td>100</td><td></td></tr></table>

In another department an initial study into reasons for delay also led to an analysis of the causes and consequences of defects. Two insights were gained from the study: firstly, it became clear to all involved that the average effort to correct a defect was 6 hours. Secondly, the department became aware of the excessive elapsed time between error occurrence and detection. For example, a lot of the specification and design defects were not detected until the “alpha and beta” tests. These two insights have led the department concerned to the introduction of Fagan inspections.

## The analysis of inspection or walk through data

The analysis of problem reports looks into the errors that remain undisclosed during development. It is obviously better to detect faults earlier. Fagan inspection is a well engineered and documented technique to do this $[4,5,9,12]$ . Here we view it as a technique to analyze and improve software engineering processes. Data collection is an important aspect of inspection; it is used, in the first place, to give the author feed-back. Inspection data can also be used to analyze software development. We argue that the analysis of inspection data, test reports and maintenance reports allows us answer the last of the “annoying questions”: How many defects are delivered to a customer when a product is released?

This question is really interesting. If we are not able to answer it, one can question the basis for a release decision. Apparently, it is not based on quality criteria, such as the number of remaining defects. Presumably other control aspects such as time and cost prevail. Defects are found during development, test, and use. Suppose that the software engineering operation is a repeatable level of process control, as described by Humphrey $[11,12]$ . This means that the process has achieved a degree of statistical control; i.e. its performance is predictable within established statistical limits $[3]$ . The analysis of inspection, test, and maintenance data should thus indicate the percentage of the defects that are found during development, testing, and in use.

Suppose the percentage distribution of errors found in previous projects have been assessed as about 70 for development, 25 for testing and 5 for use. Let us assume that, in the product under development right now, 400 defects have been found during development (via inspections) and 100 in test. This provides at least a clue to the number of defects that remain in the product.

The decision whether or not to release should be based on the number of expected undisclosed defects and the expected cost of a defect. Additional engineering effort may be spent if the costs of defects are considered too high.

## Conclusions and recommendations

This paper has discussed what we termed a set of “annoying questions” for software engineering managers. We discussed how those questions have been addressed in several engineering departments over the years. The focus has been on the basic principles applied and the sequence of analysis activities. The sequence can be crucial in the success of analysis efforts. For example: we once have tried to convince an engineering department of the virtues of early defect detection via Fagan inspection. We did not succeed. One of the reasons was that the department concerned was not aware of the cost of a defect. In this case it would have been appropriate to start with the analysis of problem reports in order to gain insight into the costs of defects, before continuing to early defect detection.

So far four questions have been named. One result of studies like this is that they often raise new annoying and interesting questions such as:

\- What is the cost of a change of the requirements in the design phase?

\- What is the impact of object oriented techniques on the reusability of software?

We intend to continue to raise and answer questions like this in order to understand and control software engineering processes.

Let us take another look at construction of software and analysis of software engineering. The goal of software engineering improvement is to upgrade software construction, since only its improvement can result in better quality software. Analysis is required to control and improve the software construction processes. Data on the engineering process are necessary to analyze software engineering. Data collection techniques are intended to provide information that will allow the analysis of the software engineering process, which can result in actions for improvement that lead to better software construction processes. The relation between construction and analysis is illustrated in another way in Figure 2, which represents construction and analysis as the two wheels of a bicycle. The left picture shows the way most organizations approach software engineering nowadays. This could be called construction driven engineering.

The right-hand picture shows another, more modern approach to software engineering that might be called balanced engineering. A similarity is that the construction wheel is the driving wheel in both pictures. That is justified since only improved construction can result in improved

![](/api/attachments/ZWBCXAWN/fulltext/images/3afc46b97c8f8601b9244cf85bde57b9514fb7b2701f4e255cc95d7bde0928ba.jpg)  
construction of software  
analysis of engineering process

![](/api/attachments/ZWBCXAWN/fulltext/images/4931c68609ab95f232a9c15be45ebc275cd5142dd64df76f1578779a1823ccdc.jpg)  
construction of software  
analysis of engineering process

Fig. 2. Construction versus analysis.

software quality. The left-hand picture shows that the construction wheel is also the steering wheel. This should be considered a design defect because it results in an unstable engineering process. The future direction of the engineering process should be determined by the analysis of the current engineering process and new technological possibilities, as is the case in the right hand picture.

## References

[1] V.R. Basili, H.D. Rombach, “The TAME project: towards improvement oriented software environments”, IEEE Trans. Software Eng., Vol. SE-14, no. 6, pp. 758–773, 1988.

[2] T.M.A. Bemelmans, “Informatiekunde; vragen, geen antwoorden”, Special Issue Informatie, June 1989, volume 31, pp. 447–456 (in Dutch).

[3] W.E. Deming, “Quality, productivity and competitive performance”, Massachusetts Institute of Technology, Centre for Avanced Engineering Studies, 1982.

[4] M. Fagan, “Design and code inspections to reduce errors in program development”, IBM Systems Journal, no.3, 1976.

[5] M. Fagan, “Advances in software inspections”, IEEE

Transactions on Software Engineering, Volume SE-12, no. 7, pp. 416–423, July 1986.

[6] M.J.I.M. van Genuchten, “Why is software late? An empirical study of reasons for delay in software development”, IEEE Transactions on Software Engineering, SE-17, no. 6, pp. 582–590, June 1991.

[7] M.J.I.M. van Genuchten, Towards a Software Factory, Kluwer Academic Publishers, Boston Massachusetts, Dordrecht The Netherlands, ISBN 0-7923-1751-3, 1992.

[8] M.J.I.M. van Genuchten, T. van den Boomen, G. Brethouwers, F.J. Heemstra, “An empirical study of software maintenance”, Information and Software Technology, Volume 34, no. 8, pp. 507–512, 1992.

[9] T. Gilb, Principles of software engineering management, Addison Wesley, 1988.

[10] F.L. Harrison, Advanced Project Management, Gower Publishing Company Limited, Aldershot, England, 1977.

[11] W.S. Humphrey, “Characterizing the software process: a maturity framework”, IEEE Software, pp. 73–79, March 1988.

[12] W.S. Humphrey, Managing the Software Process, Addison Wesley, 1989.

[13] F.L.G. van Lierop, R.S.A. Volkers, M.I.J.M. van Genuchten, and F.J. Heemstra, “Heeft iemand de software al gezien? Inzicht in het uitlopen van softwareprojecten”, Informatie, Vol. 33, pp. 193–200, March 1991 (in Dutch).

[14] W.J.A.M. Siskens, F.J. Heemstra, H. van der Stelt, “Cost control in automation projects, an empirical study”, Informatie, volume 31, pp. 34–43, January 1989 (in Dutch).
