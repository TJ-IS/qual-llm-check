---
otero_id: 24828
otero_key: "ZZ7BA3EV"
title: "User-Developed Applications: An Empirical Study of Application Quality and Developer Productivity"
authors: "Dana T. Edberg; Brent J. Bowman"
year: "1996"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1996.11518117"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# User-Developed Applications: An Empirical Study of Application Quality and Developer Productivity

Dana T. Edberg & Brent J. Bowman

To cite this article: Dana T. Edberg & Brent J. Bowman (1996) User-Developed Applications: An Empirical Study of Application Quality and Developer Productivity, Journal of Management Information Systems, 13:1, 167-185, DOI: 10.1080/07421222.1996.11518117

To link to this article: http://dx.doi.org/10.1080/07421222.1996.11518117

![](/api/attachments/ZZ7BA3EV/fulltext/images/66cbfbf1416c96f5b3aa70bd28bcc86feaf19334060704d81b8b69a5780d2854.jpg)

Published online: 11 Dec 2015.

![](/api/attachments/ZZ7BA3EV/fulltext/images/e083f87fb2112c8286798828cd56a090f12f61b74d506e657cd18eeb20290bee.jpg)

Submit your article to this journal ↗

![](/api/attachments/ZZ7BA3EV/fulltext/images/1d2610ccd04f93ac07b58e6842ab91cf0fec815883f3b38d17caa84873a5c7e5.jpg)

Article views: 1

![](/api/attachments/ZZ7BA3EV/fulltext/images/6526e6e338d32f47ae93b48f726e73d9bcdbae37b1952e2e88f5d429745ea5ea.jpg)

View related articles ↗

![](/api/attachments/ZZ7BA3EV/fulltext/images/1685454293f848132ffe6e9601116d18578fbb36a1c309a3fbe28cf40903164c.jpg)

Citing articles: 14 View citing articles ↗

# User-Developed Applications: An Empirical Study of Application Quality and Developer Productivity

DANA T. EDBERG AND BRENT J. BOWMAN

DANA T. EDBERG is a lecturer in computer information systems at the University of Nevada, Reno. She holds a B.S. and M.B.A. from the University of Nevada, Reno, and is currently completing her Ph.D. in IS from Claremont Graduate School. Her prior work experience includes software engineering project management in government and industry as well as consulting and training in IS management and software design processes. Her current research interests include measurement of the software development organization, end-user computing, and software engineering.

BRENT J. BOWMAN is an Associate Professor of Computer Information Systems and Associate Dean of the College of Business Administration at the University of Nevada, Reno. He has held both technical and managerial positions in the information technology field in government and industry. He has published a variety of articles on information systems, and his current research interests include end-user computing, software engineering, and systems analysis and design methodologies.

ABSTRACT: As inexpensive microcomputers and easy-to-use software have proliferated throughout organizations, increasing numbers of employees are developing applications. The end-user computing (EUC) literature contains many prescriptions for managing this activity, but there has been little direct empirical examination of the effectiveness of end users as application developers. This paper describes a study in which five different applications were developed independently by paired teams of end users and IS students acting as surrogate IS professionals. This permitted comparison of end users and surrogate IS professionals on the quality of the finished applications and on productivity. The quality analysis focused on technical design and implementation factors as measured by defect counting and a subjective quality attribute rating. Productivity was measured by function point analysis and lines-of-code metrics.

The results of the study indicate that the surrogate IS professionals were much more productive and produced higher-quality applications than did the end users. The fact that student surrogates significantly outperformed the end users is particularly interesting since experienced IS professionals might be expected to show even greater differences in productivity and quality. The study should be replicated using IS professionals to confirm the preliminary findings. The results suggest that additional research on the efficacy of end users as application developers is needed.

KEY WORDS AND PHRASES: end-user computing, programmer productivity, quality of programming, user-developed applications.

THE WIDESPREAD AVAILABILITY OF INEXPENSIVE MICROCOMPUTERS and the emergence of easy-to-use software packages have resulted in the rapid growth of end-user computing (EUC). These technologies have developed to the point where a large, and increasing, number of end users are engaged in creating substantial application systems to support important organizational processes and decision-making activities $[7, 27, 31]$ . In this paper, these applications are referred to as user-developed applications (UDAs) and are defined as any computer-based application for which non-IS professionals (end users) assume primary development responsibility.

Perhaps the most significant benefit attributed to effective EUC is improvement in employee productivity and performance. Since end users best know what they need, it has been suggested that they should be able to develop “better” applications $[2, 23, 25]$ . The EUC literature suggests that users may be more productive at developing applications than IS professionals since the user is both the developer and the expert who possesses knowledge of the application’s requirements, thereby removing the need to communicate requirements to an IS professional $[2, 19, 22, 23, 25]$ . However, there appears to be little empirical evidence to support the contention that application development by end users reduces development time $[2, 24]$ . This is particularly alarming when one considers the amount of time that some employees are devoting to this activity. In one study, managers and technical staff spent an average of 9.5 hours per week using microcomputers $[20]$ .

A second important issue associated with UDAs is quality, although the literature is somewhat contradictory on this topic. Some authors have suggested that user-developed applications should closely match user needs since the end user is both the developer and the individual who best understands the information requirements $[2, 19, 22, 23, 25]$ . However, many of these same authors acknowledge that UDAs represent a considerable risk to organizations since users who create applications frequently have little or no training in development methods. The risks are due to problems with information produced by UDAs that may be incorrect in design, inadequately tested, and poorly maintained $[2, 23, 24, 31]$ . Previous research indicates that concern with the technical quality of UDAs is well founded. In one study, UDAs were generally found to lack proper documentation, controls, backup, and security provisions $[31]$ .

Although the importance of EUC productivity and quality issues seems evident, there is little research directly addressing these topics. In particular, seemingly contradictory propositions concerning the quality of UDAs need to be researched. This study examines two important organizational issues related to UDAs. An experiment was performed in which five different applications were each developed by a team of end users and a team of surrogate entry-level IS professional programmer/analysts. The objectives of the study were:

1. To compare the technical quality of applications developed by end users and surrogate IS professionals; and

2. To compare the productivity of end users and surrogate IS professionals as developers of computer applications.

## Perspectives on Application Quality

THE MOST GENERAL AND ALL-ENCOMPASSING DEFINITION of quality is “fitness for use” [17], which for computer applications may be interpreted as “meets user requirements” [3, 4, 9]. In the IS literature, terms such as system success, application effectiveness, and application quality have been used as indicators of how well an application accomplishes this objective. Measurement approaches proposed for this construct focus on improved organizational profitability, effect on decision performance, cost–benefit analysis, user information satisfaction (UIS), and system utilization [3, 30]. In particular, there has been considerable effort devoted to developing measures of UIS [5, 12, 15].

The software engineering discipline, on the other hand, has examined application quality from a different perspective, that of direct assessment of the application itself. Measurement approaches may be characterized as defect counting or quality attribute modeling. In the first approach, software quality is defined as the absence of defects $[10]$ , where a defect is any failure of an application to perform its intended purpose. Quality is measured as the number of defects divided by some measure of application size (e.g., defects/K lines of code or defects/function point).

The quality attribute modeling approach is also based on how well an application satisfies user requirements. Application requirements are classified according to dimensions such as product use, transition, and revision $[4, 6, 8]$ . The first, product use, includes such quality factors as correctness, reliability, efficiency, integrity, and usability. Product transition refers to using the software in other hardware environments and reusing portions of a system for other related applications. It includes quality factors such as portability, reusability, and interoperability. The third dimension, product revision, refers to ease of modification of the software product and includes quality factors such as maintainability, flexibility, and testability. The aggregate quality of a software product is determined by the extent to which it meets the requirements for the quality attributes associated with each of these dimensions, weighted according to each attribute's importance for the application $[10, 14, 26]$ .

A comparison of the IS and software engineering approaches to measuring application quality reveals several important differences. In practice, measures such as UIS and system utilization are typically obtained by interrogating application users. This approach to measuring application quality focuses on how the information produced by computer-based applications is perceived by users (e.g., accuracy, reliability, relevance, etc.) and how well it supports their operational and decision-making activities. A potential weakness of this approach is that a user may perceive the information from an application to be accurate and reliable when, in fact, technical design and implementation flaws have introduced serious errors.

In the software engineering perspective of quality, the “product use and operation” dimension of software is similar to the user information satisfaction construct. Measurement strategies may include perceptual measures of user satisfaction, but also involve direct examination of the source code, databases, outputs, and documentation to evaluate such factors as accuracy of file update processes, appropriateness of database design, accuracy of formulas and algorithms, and inclusion of proper controls. Furthermore, direct examination is also necessary to assess design characteristics such as modularity and understandability, which in turn affect maintainability.

As noted earlier, many authors have speculated that applications created by users who are not trained in application development methods may include a variety of errors due to design and implementation flaws. The user-developer may be pleased with his or her “creation” and may use it to support decision-making activities when, in fact, the application includes incorrect formulas and inadequate control of database updates. Furthermore, if user-developed databases are not normalized, there is considerably less flexibility in how the information may be used. An application with fundamental weaknesses in accuracy and reliability may be considered to have severe quality problems regardless of the developer’s level of satisfaction.

In the study described in this paper, the software engineering approach was used for measuring application quality. Specifically, the quality of the design and implementation was measured by direct examination of source code, outputs, and documentation. Each completed application was evaluated to determine the number of defects and was rated on several quality attributes. It was felt that this type of measurement strategy was important for IS researchers to consider and has not been adequately evaluated in previous IS studies. User information satisfaction was informally assessed via postexperimental interviews.

## Perspectives on Application Development Productivity

PRODUCTIVITY HAS TRADITIONALLY BEEN DEFINED IN TERMS OF THE QUANTITY of work outputs divided by the quantity of the inputs required to produce the outputs. In the IS industry, it has proved easier to specify and measure work inputs than outputs $[29]$ . Since many of the tasks associated with developing information applications are intellectual in nature, developer time is usually considered the primary input unit. Characterizing and measuring work outputs has been much more problematic. Such partial measures as lines of code (LOC), documentation pages, test cases developed, and function points have been proposed and utilized as output metrics in previous discussions of developer productivity $[1, 16, 29, 33]$ . Examples of productivity indicators that have been used in both industry and research settings include LOC/hour and function points/hour $[11, 16, 21]$ .

## Lines of Code

Although lines of code (LOC) has been the most commonly used measure of work output, the shortcomings of this metric are well documented $[13, 16]$ . Precisely defining an LOC is less straightforward than it initially appears and variations may include different combinations of executable statements, data definition statements, comments, and job control language [16]. Another problem in using LOC as a measure of work output is its language dependence. Third-generation languages require more LOC to perform most processing functions than do fourth-generation languages (4GLs). Consequently, it is very difficult to directly compare productivity on projects developed with different languages [29].

## Function Points

Albrecht [1] has proposed a metric based on the functionality delivered by an application that is independent of the language and technology utilized for its implementation. Function points are currently being used by a number of organizations as a posteriori measures of work performed for purposes of determining developer productivity and as a priori measures of expected effort for estimation purposes [21]. In this study, both LOC and function points are used to measure the work output of the development teams. The problems of comparability across languages associated with using LOC are avoided since all applications were developed using dBASE.

## Research Methodology

FEW ORGANIZATIONS ARE WILLING TO CREATE TWO VIRTUALLY identical information systems in order to compare the productivity of the developers and the resulting quality of the systems. Because of this practical consideration, the research method employed for this study was a laboratory experiment. Paired teams of end users and surrogate IS professionals each developed an application required in a real organization. Senior-level college students majoring in computer information systems (CIS) served as surrogates for entry-level IS professionals.

The purpose of this study was to empirically test the capabilities of users as application system developers. Specifically, this study examined the productivity of users and the technical quality of the systems they produced in comparison to the same applications developed by the surrogate IS professionals. Two hypotheses were developed for this study:

H1: There is no significant difference in technical program quality between applications developed by end users and those developed by surrogate IS professionals.

H2: There is no significant difference in developer productivity between end users and surrogate IS professionals.

## Experimental Task and Procedures

An experiment was designed and conducted to test the hypotheses using two university classes. M.B.A. students enrolled in a course on CIS fundamentals represented the end users, while CIS majors enrolled in a senior-level undergraduate database course acted as surrogate entry-level IS professionals. The class representing end users was divided into five groups based upon their area of actual business expertise. These areas were engineering management, banking operations, general accounting, accounts receivable, and library operations. Each individual included in this study had at least two years of professional experience in one of these areas. Each group from the M.B.A. class consisted of three members. The class representing entry-level IS professionals was then randomly divided into five groups, also containing three members each.

Each end-user group was asked to identify an application system that was needed in any one of the team member's employing organizations. They were required to select an application that would actually be used by one of their organizations. In order to be considered, the application had to consist of at least two data files, four display screens, and two hard-copy reports. All of the applications produced for the project were substantially larger. Each end-user group was required to write a brief system request describing the objectives of their application. These requests were randomly distributed to the surrogate IS professional groups. Consequently, each application was developed by an end user and a surrogate IS professional group. Both classes had to complete the following phases of systems development: analysis, design, coding, testing, and documentation.

The surrogate IS professional groups did not have to analyze and design systems that would meet the approval of the end-user groups. They were, however, expected to produce systems that would satisfy the requests developed by the end users. They were encouraged to seek additional information about their application by performing outside reading and consulting people in organizations with similar applications. They were also permitted to discuss the project with their corresponding group in the end-user class, but there was no formal time set aside by the researcher for these discussions. The instructor of the M.B.A. class performed the role of an information center consultant. Subjects in the end-user groups frequently consulted with the instructor on technical development questions. Both classes had access to lab consultants for assistance with general hardware and software “help-desk” types of questions.

The project accounted for 15 percent of the course grade in both classes. Subjects were required to submit a final project containing the following components: a business memo, a floppy disk containing the completed application, documentation, program listings, and data to be used for testing. Each team had six weeks to complete the project after the initial application request was finished.

## Subjects

Students enrolled in the senior-level undergraduate class representing the IS professionals had previously completed an average of five CIS courses. Their self-reported GPAs ranged from 2.00 to 3.97 on a 4.00 scale, with approximately 60 percent of the students reporting a cumulative GPA between 3.00 and 3.50.

Eighty percent of the students enrolled in the graduate class representing end users were employed full time and were seeking a master's degree on a part-time basis. As stated earlier, each student had at least two years of professional business experience; the average was five years. Students' self-reported graduate GPAs ranged from 3.00 to 4.00 on a 4.00 scale, with approximately 70 percent of the students reporting a cumulative GPA between 3.00 and 3.50. A comparison of the subjects' ages and their prior experience with computers and information systems is shown in Table 1. Both end users and surrogate IS professionals used the dBASE package to complete their application systems.

Table 1. Description of Subjects

<table><tr><td rowspan="2">Months</td><td colspan="2">Using a computer</td><td colspan="2">Programming in a procedural language</td><td colspan="2">Using dBase II, III, IV</td></tr><tr><td>Surrogate MIS professionals</td><td>End users</td><td>Surrogate MIS professionals</td><td>End users</td><td>Surrogate MIS professionals</td><td>End users</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>3</td><td>0</td><td>7</td></tr><tr><td>1–6</td><td>0</td><td>2</td><td>1</td><td>5</td><td>9</td><td>8</td></tr><tr><td>7–12</td><td>0</td><td>1</td><td>3</td><td>1</td><td>5</td><td>0</td></tr><tr><td>13–24</td><td>3</td><td>3</td><td>3</td><td>3</td><td>1</td><td>0</td></tr><tr><td>25–36</td><td>3</td><td>3</td><td>2</td><td>3</td><td>0</td><td>0</td></tr><tr><td>Over 36</td><td>9</td><td>6</td><td>6</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Mean</td><td>53.5</td><td>19.1</td><td>31.8</td><td>8.6</td><td>7.3</td><td>1.0</td></tr><tr><td>Std. dev.</td><td>37.7</td><td>52.9</td><td>20.9</td><td>11.6</td><td>4.6</td><td>1.0</td></tr><tr><td>Age (years)</td><td>Surrogate MIS professionals</td><td>End users</td><td colspan="2">Business experience (years)</td><td>Surrogate MIS professionals</td><td>End users</td></tr><tr><td>20–29</td><td>12</td><td>6</td><td colspan="2">0–1</td><td>8</td><td>0</td></tr><tr><td>30–39</td><td>3</td><td>6</td><td colspan="2">1–2</td><td>5</td><td>2</td></tr><tr><td>40–49</td><td>0</td><td>3</td><td colspan="2">3–5</td><td>2</td><td>9</td></tr><tr><td></td><td></td><td></td><td colspan="2">6–20</td><td>0</td><td>4</td></tr><tr><td>Mean</td><td>26</td><td>30</td><td></td><td></td><td></td><td></td></tr><tr><td>Std. dev.</td><td>4.0</td><td>7.6</td><td></td><td></td><td>2.1</td><td>12.4</td></tr></table>

The M.B.A. students who participated in this study are highly representative of end-user developers. Previous research on the characteristics of end users indicates that, as a group, end users have limited computer knowledge, have college degrees, have gained what computer knowledge they have in a computer programming class, are normally in their early thirties, and are usually employed in a professional/technical position $[20]$ . This profile is consistent with the subjects representing end users in this study. As shown in Table 1, the end-user developers reported relatively low levels of experience developing programs using the dBASE language. However, the subjects also reported a substantial degree of variation in their level of programming experience (using other languages). This made it possible to group more experienced end-user developers with novices. The end users were developing real applications to be used in their organizations, so they not only represented end-user developers, they truly were end-user developers.

Using CIS majors as surrogates for IS professionals is more problematic. The application development skills of student CIS majors should not be considered equivalent to those of experienced IS professionals. For example, it is common practice for entry-level programmers to work under the guidance of experienced programmer/analysts prior to assuming responsibility for a development project. The productivity and quality of work produced would be expected to increase with additional experience. Furthermore, IS professionals frequently have greater access to powerful hardware and software development tools. It is interesting to note, however, that even with this limitation, the student surrogate teams were considerably more productive and produced higher-quality applications than did the end-user teams. Even greater differences in productivity and quality might be expected when applications are developed by experienced IS professionals.

## Training

The end-user groups received training on the dBASE package. The training was similar to that often provided in organizations and consisted of five hours of formal instruction on the features of the package, including hands-on time using the package. They were provided with a large set of sample programs that demonstrated such traditional application functions as data edit, update, inquiry, reporting, and menu processing. The end-user groups were also given separate and additional training concerning the systems development life cycle. This training discussed the system development process and focused on topics such as software design, database design, programming, documentation standards, and backup and security procedures.

## Limitations

There are several limitations that should be considered when interpreting the results of this study. As has already been noted, university students majoring in CIS are not equivalent to experienced IS professionals. The results of this study should therefore be considered preliminary until additional work comparing application development performance of professional programmer/analysts with end users is completed.

The small sample size used in this study is also a limitation. It is inappropriate to draw strong conclusions on the basis of only five applications. Perhaps the major contribution of this study is that it demonstrates the importance of additional research in this area involving larger sample sizes and different populations.

## Measuring Productivity and Application Quality

FOUR MEASURES OF PRODUCTIVITY AND APPLICATION QUALITY WERE USED to compare the performance of the end users and surrogate IS professionals. Productivity was measured by the number of function points/hour and lines of code (LOC)/hour. The quality metrics adopted for this study are the number of defects/function point and a quality rating based on the quality attribute models described in the literature [8]. The measurement strategies for each of these metrics are described in the following sections.

## Developer Productivity Metrics

Each subject in each group kept a weekly time sheet of the time spent on the project. Time spent was broken down into six categories, including hours spent learning the software package, analyzing the application, designing the project, programming the project, testing the project, and documenting the project. There was no incentive for students to overstate their time since it was explained that these time sheets would not be reviewed until after course grades had been assigned. The time reported on these sheets was used to calculate the denominator for the two measures of productivity: LOC/hour and function points/hour. The LOC values were obtained by direct examination of the source code turned in as part of each application system project. All non-commentary lines of code were counted in this study; thus, LOC included data definition statements as well as executable code lines.

Following previous research, we also used function point analysis as a measure of developer productivity $[1, 21]$ . Function points were calculated from the source code of each application system project by one of the researchers with considerable experience performing this task. Function points were calculated according to the methodology proposed by Albrecht $[1]$ and enhanced by the International Function Point User Group (IFPUG).

## Program Quality Metrics

Defects were counted by tabulating errors detected while inspecting the source code and executing each application system project. Only significant defects were counted. Examples of defects included: displaying an incorrect total on the output; infinitely looping a program module; abnormally terminating an individual program within a project; calling a nonexistent subprogram; adding a record to a file when the user canceled the operation; and deleting the wrong record from a file. Trivial defects such as misspellings on the output were not counted.

Since application size and functionality were expected to vary for different applications, merely counting defects does not provide a direct comparison. Larger applications that provide significantly greater functionality might be expected to have a greater number of defects. A better indicator of application quality is obtained by normalizing the number of defects by some measure of application size. The number of function points rather than LOC was selected as the measure of application size since this metric is a more direct measure of application functionality.

The proponents of the quality attribute models assert that using defect count as the only quality metric does not take into account the many other factors that differentiate good and bad applications $[16, 19]$ . Following prior research $[8, 14, 26]$ , each application was subjectively rated on eleven quality attributes. Each attribute was scored from 0 (low) to 5 (high) using a Likert-type scale. This scheme resulted in a possible maximum application quality rating of 55 points. The program quality worksheet that lists the quality attributes evaluated in this study is provided in the appendix.

## Results and Analysis

## Overall Productivity and Quality Results

Table 2 summarizes the data gathered in this study. Means and standard deviations are presented for hours spent, lines of code produced, number of function points generated, number of detected defects, and number of quality points. When interpreting this data, recall that five different applications were developed. Large standard deviations were not unexpected, however, the variation in the total hours spent and total function points among the surrogate IS groups was much greater than the end-user groups. Thus, the variation in the productivity scores for the surrogate IS groups was substantially higher. This is consistent with prior studies $[28, 32]$ , however, the high degree of observed productivity variation introduces problems in comparing the performance of the surrogate IS professional groups to the end users and must be considered when interpreting the results of this study.

## Development Time

The average number of hours devoted to each project was slightly higher for end users (162 hrs) than the IS surrogates (154 hrs), but the difference was not substantial. As described above, the IS group demonstrated considerably greater variance with the greatest deviation observed in the hours spent programming. This finding is consistent with those of earlier studies $[28, 32]$ .

Table 2 also presents the percentage of time spent on the six system development tasks for end users and IS professionals. The surrogate IS professionals spent the largest percentage (67 percent) of their time on programming and testing activities. Each of the other tasks averaged less than 10 percent of total project time. The end users also spent the largest percentage (40 percent) of their time on programming and testing, but this percentage was substantially smaller than that for the surrogate IS professionals.

It is interesting to note the percentage of time spent analyzing the business problem. The literature suggests the intuitive notion that end users should have a greater understanding of the business problem and the necessary information processing requirements. Consequently, users should not have to devote as much effort to analyzing the problem and defining a solution. As shown in Table 2, this proposition is not supported in this study. Surprisingly, end users spent 13.7 percent of their time doing analysis, while the surrogate IS professionals devoted only 8.4 percent of total project time to this task. However, one reason for this difference may be that the surrogate IS professionals did not have to communicate with the end users or create systems to the exact satisfaction of the end users. This limitation of the study may have led to an understated amount of analysis time for the surrogate IS professionals. A second reason for this difference may have been the relative importance the end users placed on completing this task. Still, the difference in emphasis on this task by the two groups is worthy of further study. The results on productivity and quality discussed in subsequent sections provide additional evidence that end users are not particularly proficient at performing analysis of system requirements.

Table 2. Productivity and Quality Scores

<table><tr><td rowspan="2"></td><td colspan="2">Surrogate MIS professionals</td><td colspan="2">End users</td></tr><tr><td>Mean</td><td>Std. dev.</td><td>Mean</td><td>Std. dev.</td></tr><tr><td colspan="5">Hours spent on the project:</td></tr><tr><td>Learning the package</td><td>15.3</td><td>8.5</td><td>45.5</td><td>17.4</td></tr><tr><td>Analyzing the application</td><td>12.9</td><td>10.5</td><td>22.1</td><td>4.1</td></tr><tr><td>Designing the solution</td><td>12.3</td><td>12.1</td><td>17.1</td><td>3.1</td></tr><tr><td>Creating the solution</td><td>77.0</td><td>57.8</td><td>48.8</td><td>28.1</td></tr><tr><td>Testing the solution</td><td>25.4</td><td>39.5</td><td>16.7</td><td>6.5</td></tr><tr><td>Documenting the solution</td><td>11.1</td><td>7.9</td><td>11.7</td><td>5.7</td></tr><tr><td>Total hours</td><td>153.9</td><td>118.6</td><td>161.8</td><td>33.9</td></tr><tr><td>Total lines of code</td><td>991.0</td><td>664.0</td><td>359.0</td><td>294.0</td></tr><tr><td>Total function points</td><td>130.0</td><td>77.2</td><td>53.9</td><td>34.1</td></tr><tr><td>Total defects</td><td>2.8</td><td>1.7</td><td>6.0</td><td>1.4</td></tr><tr><td>Total quality points</td><td>40.0</td><td>6.2</td><td>22.0</td><td>7.6</td></tr></table>

## LOC and Function Points Produced

Overall, the surrogate IS professionals wrote considerably more lines of code: on average, 991 LOC per application as compared to 359 LOC for end users. A possible explanation for this difference could be that end users relied more heavily on the fourth-generation capabilities of the programming language and were thus able to produce their applications with considerably less code. However, a detailed examination of each application's source code revealed that neither the end users nor the surrogate IS professionals used the existing dBASE control center. Both groups elected to create menu-based systems implemented with procedural code. As indicated in Table 2, the surrogate IS professionals also produced substantially more function points on average (130) than did end users (54).

An example of the increased functionality in the applications produced by surrogate IS professionals is illustrated by one of the applications: a project time reporting system developed for the engineering group in a manufacturing organization. The objective of the system was to keep track of the number of hours spent on different engineering tasks involved in the design of new products. Both groups created applications that reported time spent by project number and task. However, the application created by the surrogate IS professionals also reported time spent by individual engineer and permitted various online queries. The end users, when viewing this system during the postexperiment review, were impressed that it was possible to have online access to the information and were excited about the possibility of individual productivity information. The end users had not realized how helpful those features might be until they watched the execution of the system developed by the surrogate IS professionals.

The pattern of greater functionality in the applications developed by the surrogate IS professionals was consistent across each of the five different applications. Conversations with the end users during the postexperiment interviews suggested that the applications produced by the surrogate IS professionals were larger (in terms of both LOC and function points) because they contained additional functions that were desired by the end users—functions that the end users were unable to effectively create for themselves.

## Number of Defects and Quality Points

As may be seen in Table 2, the end users averaged substantially more defects per project than did the surrogate IS professionals. The end-user applications also received lower average quality ratings (22) than the applications developed by surrogate IS professionals (40).

## Productivity and Application Quality Metric Results

Table 3 presents the metric scores used to measure productivity and quality in this study. Each score for the surrogate IS professionals and the end users was compared statistically using the nonparametric Wilcoxon matched-pairs signed-ranks test. The probability of observing a T value less than or equal to 1 with five related pairs and no difference between the two populations is $\leq 0.05$ . As shown in Table 3, the differences are significant for all measures. The conclusion is that there is a difference in both productivity and quality between the two groups of system developers.

## Productivity Metrics

The difference in programmer productivity as measured by LOC/hour and function points/hour is shown graphically in figures 1 and 2. According to these metrics, the surrogate IS professionals were more productive in four out of five projects. With the exception of project 3, the differences in productivity were very large. As indicated in Table 3, the average time devoted to the projects was not materially different for the end users and the surrogate IS professionals. However, the function point and LOC data indicate that the end users did not accomplish as much with their time as did the surrogate IS professionals. On average, the end users required three hours to create one function point, while the surrogate IS professionals were able to create each function point in 1.13 hours. This is consistent with the LOC metric results. On average, the surrogate IS professionals produced 8.1 lines of code per hour, while the end users produced 2.1 lines of code per hour.

Table 3. Normalized Productivity and Quality Metrics

<table><tr><td rowspan="2"></td><td colspan="2">Surrogate MIS professionals</td><td colspan="2">End users</td><td rowspan="2">Wilcoxon T value</td></tr><tr><td>Mean</td><td>Std. dev.</td><td>Mean</td><td>Std. dev.</td></tr><tr><td colspan="6">Productivity metrics:</td></tr><tr><td>LOC/hour</td><td>8.1</td><td>3.1</td><td>2.1</td><td>1.4</td><td>1*</td></tr><tr><td>Function points/hour</td><td>1.1</td><td>0.5</td><td>0.3</td><td>0.2</td><td>1*</td></tr><tr><td colspan="6">Quality metrics:</td></tr><tr><td>Function points/ defect</td><td>80.3</td><td>97.6</td><td>9.2</td><td>5.4</td><td>0*</td></tr><tr><td>Total quality points</td><td>40.0</td><td>6.2</td><td>22.0</td><td>7.6</td><td>0*</td></tr></table>

\* Significant for one-tailed test at alpha = 0.05.

As described earlier, one commonly cited benefit of end-user application development is the elimination of the need for communication between the user and the application developer. It has been proposed that systems might be developed in a more timely fashion if the user were completely responsible for the development $[2, 25, 27]$ . This study does not support that proposition. In this experiment, the surrogate IS professionals produced greater functionality in less time than did the end users.

## Quality Metrics Results

The applications developed by surrogate IS professionals had fewer average defects than those developed by end users. However, a more accurate view of the defect rate is obtained by normalizing this metric with some indication of application size, such as function points. As shown in Table 3, this adjustment results in an even greater disparity in quality. Surrogate IS professionals produced an average of 80.3 function points per defect while the end users averaged 9.2 function points per defect. Figure 3 contrasts the number of function points per defect for each application. The surrogate IS professionals outperformed their end user counterparts on all five projects.

The applications developed by the IS group also received higher average quality attribute rating scores. Out of a maximum of 55 points, the surrogate IS professional projects received an average of 40 points while the end-user projects received an average of 22 points. Figure 4 provides a project-by-project comparison of the quality point ratings.

It is useful to examine the factors that resulted in less favorable quality point and defect scores for the end-user applications. For example, very few of the end-user programs performed any data validity checking. Incorrect data input frequently caused infinite loops or abnormal terminations in the programs. Furthermore, the programs created by the end users did not adhere to any principles of structured design or modularity. Code that could have been reused by a variety of programs in a given project was simply repeated in each individual program. Another shortcoming of the end-user applications was the lack of documentation. Only one group produced any form of user documentation.

![](/api/attachments/ZZ7BA3EV/fulltext/images/80e340e55e557e29aed473d9960122f8a7ddcb956e9b752f12ed83662ab1cdfb.jpg)

Figure 1. Lines of Code per Hour  
![](/api/attachments/ZZ7BA3EV/fulltext/images/1fe1e1b41cce8e1d5c739656001f09653867e519af1be22088ac7fe2a3df47c8.jpg)  
Figure 2. Function Points per Hour

![](/api/attachments/ZZ7BA3EV/fulltext/images/af938385facb4f4e478769734ac710776b610d90961efeb94b62f5b6e3a7b04c.jpg)

Figure 3. Function Points per Defect  
![](/api/attachments/ZZ7BA3EV/fulltext/images/6cab0d1306107542f7afd27349b2c13c118edd921bae09f74ba5f3563fc9f51c.jpg)  
Figure 4. Quality Rating Score

Perhaps the most disturbing finding was the frequency and severity of data integrity problems observed in the end-user applications. Test runs exercising the update functions resulted in database files that contained incorrect data. Examples of data integrity problems included adding blank records, incorrectly deleting records, and leaving records in the file even when the program indicated that they had been deleted. No comparable data integrity problems were observed in any of the systems developed by the surrogate IS professionals. A common theme in the EUC literature warns that organizations may face risks due to poorly designed UDAs. The results of this experiment support this proposition.

## Postexperiment Interviews

QUANTITATIVE MEASURES OF USER INFORMATION SATISFACTION were not collected as part of this experiment. However, after the experiment was completed, each end-user team was given the opportunity to observe and use the matched application developed by the team of surrogate IS professionals. The end users were then interviewed about their reactions to the applications. This provided an informal indication of user information satisfaction with the applications developed by the surrogate IS groups. Furthermore, it provided an indication of whether the increased functionality included in the surrogate IS group applications was valued by the end users or merely superfluous.

Each end user expressed very favorable impressions of the system developed by the counterpart surrogate IS group. Actual comments received from end users during the interviews included:

This system is much easier to use than mine.

I couldn't figure out how to put constant data on the screen and just let the user skip over input that doesn't change very often.

You mean it's possible to bypass submenus?

These screens have more analytical data.

The reports are more complete.

I didn't think of including this kind of information in my report, I didn't know you could store the data that would be necessary to produce this [character data in a memo field].

I want to use this application back at work. Do you think the other group will mind if I take this?

## Conclusion

THE RESULTS OF THIS STUDY CAST DOUBT ON THE EFFECTIVENESS of end users as developers of business applications. While the findings should be considered preliminary, the results support several interesting observations. A purported benefit of EUC is that users can develop applications that the professional IS staff will never get to because of the backlog in demand for new applications. Implicit in this proposition is the assumption that users can create applications of reasonable quality. The results of this study suggest that users may have significant problems developing even moderately complex applications. Particularly troublesome was the frequency and severity of the defects (e.g., the serious data integrity problems) that were observed in the UDAs. One must question whether organizations truly benefit if errors in UDAs affect the accuracy of the information provided. While this study did not directly compare the UIS of applications developed by users with those developed by the surrogate IS professionals, it is interesting that in postexperiment interviews, the end users themselves uniformly agreed that the applications created by the surrogate IS professionals were “better.”

It is not surprising that CIS majors acting as surrogates for entry-level IS professionals are more productive application developers than are end users. However, the magnitude of the productivity differences was not expected. As noted above, more research on the efficacy of end users as application developers is needed, but the results of this study suggest several preliminary recommendations:

1. It is critically important for organizations to provide end users with training on application development methods and procedures, especially in the area of quality assurance. It is apparent that significant numbers of end users will continue to create computer-based applications. Unless end-user proficiency at developing applications is significantly increased, organizations may incur considerable costs due to unproductive use of time and reduced effectiveness due to low-quality applications.

2. There is a trend toward downsizing the centralized IS development group and reassigning programmer/analysts to business units. The evidence provided by this experiment suggests that this trend is healthy. If personnel with strong IS skills are available to assist in the development of departmental and work group applications, some of the problems that occur when less qualified end users create applications may be avoided. Managers should hire employees with formal IS training as computing begins to proliferate within their units.

3. When investigating issues associated with EUC, researchers should consider direct examination of the applications. Less direct measures such as user information satisfaction and system utilization are very useful in evaluating the effectiveness of EUC activities, but additional insights can be gained from detailed inspection of the work product.

## REFERENCES

1. Albrecht, A.J., and Gaffney, Jr., J. Software function, source lines of code, and development effort prediction: a software science. IEEE Transactions on Software Engineering, 9, 11 (November 1983), 639–648.

2. Amoroso, D.L. Organizational issues of end-user computing. Data Base, 19, 3–4 (Fall-Winter 1988), 49–58.

3. Amoroso, D.L., and Cheney, P.H. Testing a causal model of end-user application

effectiveness. Journal of Management Information Systems, 8, 1 (Summer 1991), 63–89.

4. Arthur, J. Measuring Programmer Productivity and Software Quality. New York: John Wiley, 1985.

5. Bailey, J.E., and Pearson, S.W. Development of a tool for measuring and analyzing computer user satisfaction. Management Science, 29, 6 (May 1983), 519–529.

6. Boehm, B.W.; Brown, J.R.; Kaspar, H.; Lipow, M.; MacLeod, E.J.; and Merritt, M.J. Characteristics of Software Quality. Amsterdam: North-Holland, 1978.

7. Bowman, B.J.; Alavi, M.; and Scamell, R. The development of applications by end-users: some relationships between development controls and application quality. Proceedings of the First International Meeting of the Decision Sciences Institute, Brussels, June 24–26, 1991.

8. Cavano, J.P., and McCall, J.A. A framework for the measurement of software quality. Proceedings of the ACM Software Quality Assurance Workshop, November 1978, pp. 133–139.

9. Cho, C.K. An Introduction to Software Quality Control. New York: John Wiley, 1980.

10. Chow, T.S. Software quality: definitions, measurements and applications. Tutorial on Software Quality Assurance: A Practical Approach. Silver Spring, MD: IEEE Computer Society Press, 1985, pp. 13–20.

11. Chrysler, E. Some basic determinants of computer programming productivity. Communications of the ACM, 21, 6 (June 1978), 472–483.

12. Doll, W.J., and Torkzadeh, G. The measurement of end-user computing satisfaction. MIS Quarterly, 12, 2 (June 1988), 259–274.

13. Duncan, A.S. Software development productivity tools and metrics. Proceedings of the 10th International Conference on Software Engineering, April 1988, pp. 41–48.

14. Inglis, J. Standard software quality metrics. AT&T Technical Journal, 65, 2 (March–April 1986), 113–118.

15. Ives, B.; Olson, M.H.; and Baroudi, J.J. The measurement of user information satisfaction. Communications of the ACM, 26, 10 (October 1983), 785–793.

16. Jones, C. Applied Software Measurement: Assuring Productivity and Quality. New York: McGraw-Hill, 1991.

17. Juran, J.M. Quality Control Handbook. New York: McGraw-Hill, 1974.

18. Kalmbach, H. Software quality assurance in a changing development environment.

AFIPS Conference Proceedings, National Computer Conference, 55 (June 1986), 51–59.

19. Kozar, K.A., and Mahlum, J.M. A user generated information system: an innovative development approach. MIS Quarterly, 11, 2 (June 1987), 163–176.

20. Lee, D.M.S. Usage pattern and sources of assistance for personal computer use. MIS Quarterly, 10, 4 (December 1986), 313–325.

21. Low, G.C., and Jeffery, D.R. Function points in the estimation and evaluation of the software process. IEEE Transactions on Software Engineering, 16, 1 (January 1990), 64–71.

22. Martin, J. Application Development without Programmers. Englewood Cliffs, NJ: Prentice-Hall, 1982.

23. O'Donnell, D.J., and March, S.T. End-user computing environments—finding a balance between productivity and control. Information and Management, 13, 2 (September 1987), 77–84.

24. Palvia, P. On end-user computing productivity: results of controlled experiments. Information and Management, 21, 4 (November 1991), 217–224.

25. Porter, L.R., and Gogan, J.L. Coming to terms with end-user systems integration. Journal of Management Information Systems, 5, 1 (Winter 1988), 8–16.

26. Redish, K.A., and Smyth, W.F. Evaluating measures of program quality. Computer Journal, 30, 3 (June 1987), 228–232.

27. Rivard, S., and Huff, S.L. An empirical study of users as application developers. Information and Management, 8, 5 (May 1985), 89–102.

28. Sackman, J.; Erikson, W.; and Grant, E. Exploratory experimental studies comparing online and offline program performance. Communications of the ACM, 11, 1 (January 1968), 3–11.

29. Scudder, R.A., and Kucic, R.A. Productivity measures for information systems. Information and Management, 20, 5 (May 1991), 343–354.

30. Srinivasan, A. Alternative measures of system effectiveness: associations and implications. MIS Quarterly, 9, 3 (September 1985), 243–253.

31. Sumner, M., and Klepper, R. Information systems strategy and end-user application development. Data Base, 18, 4 (Summer 1987), 18–30.

32. Valett, J.D., and McGarry, G.E. A summary of software measurement experienced in the software engineering laboratory. Journal of Systems and Software, 9, 2 (February 1989), 137–148.

33. Vessey, I. On program development effort and productivity. Information and Management, 10, 5 (May 1986), 255–266.

## APPENDIX A: Program Quality Worksheet

Rate each factor on a scale of 0 to 5:

<table><tr><td>0 None</td><td>1 Fair</td><td>2 Moderate</td><td>3 Average</td><td>4 Good</td><td>5 Excellent</td></tr><tr><td colspan="6">Rating Factor</td></tr><tr><td>______</td><td colspan="5">1. Online data validity checking</td></tr><tr><td>______</td><td colspan="5">2. Backup and recovery procedures</td></tr><tr><td>______</td><td colspan="5">3. File cross checking for data validity</td></tr><tr><td>______</td><td colspan="5">4. Screen design</td></tr><tr><td>______</td><td colspan="5">5. Report design</td></tr><tr><td>______</td><td colspan="5">6. Ease of use</td></tr><tr><td>______</td><td colspan="5">7. Online help</td></tr><tr><td>______</td><td colspan="5">8. Programmer documentation</td></tr><tr><td>______</td><td colspan="5">9. User documentation</td></tr><tr><td>______</td><td colspan="5">10. Program modularity</td></tr><tr><td>______</td><td colspan="5">11. Program complexity</td></tr></table>
