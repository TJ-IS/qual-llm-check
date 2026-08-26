---
otero_id: 26954
otero_key: "BR4PYQKA"
title: "System Development Methods—A Comparative Investigation"
authors: "Mo A. Mahmood"
year: "1987"
journal: "MIS Quarterly"
doi: "10.2307/248674"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
System Development Methods-A Comparative Investigation
Author(s): Mo A. Mahmood
Source: MIS Quarterly, Vol. 11, No. 3 (Sep., 1987), pp. 293-311
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/248674

Accessed: 15/11/2014 16:40

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# System Development Methods—A Comparative Investigation

By: Mo A. Mahmood
Associate Professor
College of Business Administration
University of Texas—El Paso
El Paso, Texas 79968

## Abstract

This article presents a retrospective comparative study of the use of the system development life cycle (SDLC) and prototyping methods to help select a development approach for a given information systems (IS) project. The respondents were asked (a) to decide independently whether one of their recent IS projects was developed using either the SDLC or prototyping approach and if so, (b) to evaluate the merit of that approach in terms of ease of project management, project requirements, project characteristics, impact on decision making, and user and designer satisfaction. The results indicate:

1. Design methods cannot be considered apart from project, environment and decision characteristics.

2. A clear cut preference of one method over the other could not be established. Each method performed better in some areas that in others.

3. A framework that can be used by a project director for selecting a design method to develop a system could be postulated.

Keywords: System design methods, project management, project requirement, user satisfaction.

ACM Categories: D.2.9, D.3.2, D.3.5, K.6.1, K.6.3

## Introduction

The productivity achieved in information systems (IS) development and responsiveness of system development methods to user needs are matters of growing concern for IS managers. With completion times for new applications running into years $[24]$ , system development costs increasing at a faster rate than productivity itself $[24]$ , and growing evidence linking user satisfaction to system success $[4, 21, 25, 36]$ , IS managers are working to improve the productivity of their system development methods. Two ways to increase this productivity have been proposed. The first is to improve the efficiency and responsiveness of the traditional system development life cycle (SDLC) approach, while the other is to employ a prototyping method in the development process.

Improvements to the SDLC approach have been proposed in the form of user involvement $[15]$ , critical review of system design with particular emphasis on marginally useful features $[13]$ , and the use of fourth generation languages to allow users to program the computer directly $[20, 23]$ . These suggested improvements, however, have not stopped researchers and practitioners from questioning the SDLC approach. The main complaints are that the SDLC method (a) delays the delivery of systems to users until the last stages of system development $[7]$ ; (b) requires specified systems outputs at the outset $[23]$ ; and (c) creates communication problems $[33]$ .

The prototype approach, on the other hand, receives wide support from researchers and practitioners alike because it (a) allows more concrete identification and validation of user information requirements [2, 5, 16, 21, 34]; (b) facilitates implementation and user acceptance [3, 20] by getting usable portions of the systems to users sooner [2, 34]; (c) elucidates the design best suited to the user's individual cognitive style [6]; (d) improves communication between users and designers [2, 10, 20]; and (e) encourages enthusiasm and commitment during the development process which results in more satisfied users [2, 10, 20].

Some disadvantages in the prototyping method, when compared to the SDLC technique, have also been cited. These include (a) the tendency to oversell the prototyping method to users, creating unrealistic expectations of development speed and usefulness of the method [2, 10, 20]; (b) the difficulty in managing and controlling the system development approach [2, 20]; (c) the difficulty in applying the method to large systems [2]; (d) the problem in interfacing with other systems since interfaces cannot be designed early in the development [9]; and (e) the fact that the development of such systems may require the acquisition and support of expensive, unfamiliar software [35].

The virtues and drawbacks of the traditional SDLC and prototyping methods are based on conceptual discussions, technical literature, and case studies, but little empirical research. It is obvious that a rigorous comparison of the two methods in a real-world setting is needed to verify or deny many of the claims being made. This article reports the results of such a comparison.

## A Discussion of the Methods

The basic concept behind the SDLC method is that “there is a well-defined process by which an application is conceived, developed, and implemented” [19]. The approach is characterized by the use of abstract representations of the proposed system (e.g., verbal explanations, diagrams, charts, etc.) to identify user requirements, data structures, processing logic, and user interfaces. Many writers have discussed virtues and drawbacks of the method, and have proposed a number of improvements. Several were described by Peters and Tripp [37], including structured design, the Jackson methodology, logical construction of programs, META Stepwise Refinement (MSR), and Higher Order Software (HOS).

This widespread understanding of the SDLC concept is not true of the prototyping method. The term has been used in so many ways—even in reference to system development—that generalizations drawn from the literature are difficult to make. Several different kinds of prototypes have been described, including:

1. “throw-away” prototypes (rapid, application-driven)—used primarily to clarify and satisfy information requirements and then discarded [3, 10, 15];

2. "build-upon" prototypes (system sculpture, heuristic development, proto-cycling)—integrated into the entire system development process, used to clarify user requirements, and continually refined to become the final system [13, 38, 40]; and

3. "data-driven" prototypes—used both to improve data structures and satisfy information requirements [3, 35].

Most authors discuss prototyping in terms of its differences from the traditional SDLC method. Basic differences have been described in Table 1.

## Previous research

An extensive search of the literature revealed that very little empirical research has been undertaken to compare the SDLC to prototyping methods. In fact, there are only two empirical studies [2, 9]. Even those were laboratory studies and “by the nature of laboratory experiments, they [the methods] were compared in a less than realistic setting" [2]. There are a few case studies narrating applications of one design approach or another, though there is a significant body of technical and conceptual literature on the methods. This section discusses briefly the empirical studies, case studies, and the technical and conceptual literature.

Table 1. SDLC vs. Prototyping

<table><tr><td>Design Method</td><td>Information Requirements [35]</td><td>System Representation [32]</td><td>Changes in Design [5]</td></tr><tr><td>SDLC</td><td>predetermined</td><td>user deals with explanations, diagrams and charts of proposed system</td><td>minimized</td></tr><tr><td>Prototyping</td><td>best developed in parallel with coding rather than serially</td><td>user deals with a realistic view of the system</td><td>encouraged</td></tr></table>

The empirical research performed by Alavi [2] described experiments conducted with university students as both developers and users. She measured three categories of success: (a) user evaluation of and satisfaction with the information system developed; (b) positive user and designer perceptions and attitudes toward the design process; and (c) the extent of developed system usage in decision making. Alavi found that the prototyping method improved user satisfaction, usage of the system, and user communication with designers. Designers, however, experienced an increased change in user requirements and more difficulty in controlling the process; they did not notice any communication improvement.

Boehm, et al., [9] also used university students in their study. Four teams utilized the SDLC method, and three teams used the prototyping approach to design different versions of the same software application. The prototyping method was found to produce a less bulky system, with roughly the same efficiency as the SDLC method, while requiring less development effort. The prototyped systems were rated somewhat lower on functionality and robustness, but higher on ease of learning and use. The prototyped versions also produced higher user satisfaction.

Other writers have contributed case studies describing successful applications of the prototyping method. For example, Blum [8] detailed a work station for prototyping at John Hopkins University. Brice, et al., [10] described the use of INGRES at the Los Alamos National Laboratory. Jenkins [28] employed the prototyping method to install a database management system at the Congressional Budget Office in Washington. Spiegel [39] described the application of a prototyped system for AVCO Financial Services.

Case studies describing the use of the SDLC approach are also present in the literature.

Couger [17] used the SDLC method to compare the costs associated with life cycle phases for first- and third-generation computer systems. Graver, et al., [22] cited an application of the SDLC approach to the development of large defense-related systems. McKeen [30] utilized the SDLC method to design and develop business application systems. Ahituv and Neumann [1] applied the SDLC method to a wholesale firm.

Conceptual discussions, for the most part, espouse the prototyping method, including who should use prototyping and in what environment. For example, while Jenkins [26] and Brice, et al., [10] recommend that only professional prototype builders from the MIS department be allowed to develop system prototypes, Connell and Brice [15] and Zajonc and McGowan [40] emphasize that natural languages, expert systems, and other advances allow users to prototype their own systems.

Alavi [2] points out the importance of the organizational environment in which prototyping is used. According to her, management understanding and support are essential, since the speed and deliverables of the method are different from the SDLC.

In addition to specifying who should use prototyping and in what environment, many writers have identified what project characteristics are best suited to prototyping. These include situations where:

1. user requirements for designing and developing a system are not clear [2];

2. there is a need to go through a trial and error method before committing resources [2];

3. conventional system development is expected to be too long [26];

4. the project is small [26];

5. a large project can be subdivided into portions that can be prototyped [26];

6. data resources are organized and easily accessible for system development purposes [26].

Finally, as a cautionary note the following suggestions have been offered:

1. define the scope of the prototype clearly and plan the development process in advance [2];

2. establish and enforce rules for modifying, testing, and documentation [2];

3. make the prototyping simple and quick

[20]; and

4. base the prototyping on information gathered from system users [14].

## Research Method

In order to investigate the impact of development methods on a system's success, two questionnaires, one for the designers and the other for the users, were constructed by reviewing relevant literature [2, 27, 29, 31]. Whenever possible, items with histories of reliability and validity were employed in the instruments, thus accomplishing the following: improved validity in the questionnaire and comparison of present research findings with previous research.

On each questionnaire the two design methods were defined without using their names. If the system development method most recently used by the respondent fell into one of the two categories, the respondent was asked to (a) circle the appropriate choice, and (b) complete the rest of the questionnaire. Each questionnaire consisted of 24 items related to user and designer issues. Twelve of these items were aimed at identical issues for both groups.

The common items were related to (a) user/designer communication and conflict; (b) user participation and influence in the system development process; (c) user understanding of and satisfaction with the system; (d) project schedule, budget and time; and (e) project requirements in terms of time, money and effort.

The designer items were based on (a) development approach flexibility, overall quality, ease of management and control, and satisfaction; (b) information systems conceptualizing, planning, implementing, testing and maintenance; and (c) user commitment, use and specifications.

The user items pertained to (a) decision attributes (complexity, confidence and cost, and efforts in making decisions); (b) information system characteristics (flexibility, adaptability, and capability to estimate decision-making variables, produce a variety of reports, and extend decision-making capabilities); and (c) output quality (accuracy, reliability and timeliness).

In addition, several items based on project characteristics (e.g., cost, duration, effort) were listed on the designer questionnaire. Previous researchers [27, 29] have used these characteristics to investigate system design methods. Similarly, the user questionnaire also contained several items on the parent organization's characteristics. The sole purpose of these items was to collect and report information on respondents and their organizations and projects.

On each questionnaire some of the items were phrased as positive statements and others as negative statements to avoid response bias (such as agreement with every statement). The respondents were asked to indicate the extent of their agreement or disagreement with each statement on a seven-interval, Likert-type scale.

To further minimize bias and provide external confirmation, the questionnaires were administered to 20 DP/MIS managers in a large midwestern city. This pretest led to minor changes in the questionnaires. The final questionnaires were mailed or personally delivered to 300 DP/MIS managers who were members of the Association for Systems Management (ASM). The questionnaires were hand delivered to some of the DP/MIS managers because of their proximity to the research institution and the assumption that this would lead to an increased response rate. It was still the responsibility of the DP/MIS manager to choose a project and its designer and user. It was never intended to influence the opinion expressed by the respondents. The responses from the two groups—mail vs. personally-delivered—should, therefore, provide similar results and were combined for further analysis.

The DP/MIS managers were asked to select a recently developed system only if it was designed by either the SDLC or prototyping method, and to send the questionnaires to the lead designer and user of the system. The designer and user were also asked to categorize the system into one of the two design methods. Each pair of the designer-user questionnaires had the same identification number. Only the matched pairs—where the designer and user agreed on the design method—were employed in the study. This validation process should reduce the potential selection bias. The respondents were asked to fill out the questionnaires, based on their experience with the system, and mail them directly to the research institution. The respondents were also assured of complete anonymity.

Sixty-one pairs of questionnaires were returned, giving a 20 percent rate of return. Seven pairs of questionnaires could not be used because of nonmatching design methods and incomplete items. While this response rate is somewhat low, it was not unexpected for the following reasons:

1. The questionnaires were fairly lengthy.

2. Several companies have policies against completing unsolicited questionnaires.

3. Some of the managers on the ASM list had changed jobs or companies and could not be located.

4. In some cases, only one of the pair of questionnaires had been returned and thus could not be used.

## Respondent characteristics

Half of the respondents were designers and the other half were users (see Table 2). The respondent organizations represented a broad cross-section of firms and industries. Project characteristics were similarly varied. Interestingly, no significant correlations were found between the development method used for a project and the project characteristics such as development cost and duration.

## Analyses

As a first step toward analyzing the data, the individual responses by designers and users were examined separately by using a t-test to assess the difference between the two development methods. The t-test was used since it allows one to test the hypothesis that the means of the two groups came from the same population. If the hypothesis is rejected, it can be concluded that the variance between the means is too large to be attributed to a sampling difference.

Table 2. Sample Demographics

<table><tr><td colspan="3">Respondents</td></tr><tr><td>Designers</td><td colspan="2">Users</td></tr><tr><td>System Analyst 29%</td><td>User</td><td>31%</td></tr><tr><td>Programmer 17%</td><td>Supervisor</td><td>25%</td></tr><tr><td>Programmer Analyst 16%</td><td>Manager</td><td>44%</td></tr><tr><td>System Development Manager 15%</td><td></td><td></td></tr><tr><td>Project Leader 9%</td><td></td><td></td></tr><tr><td>MIS Director 7%</td><td></td><td></td></tr><tr><td>Unspecified 7%</td><td></td><td></td></tr><tr><td colspan="3">Organizations</td></tr><tr><td>Type</td><td colspan="2">Size (in Sales)</td></tr><tr><td>Manufacturing 60%</td><td>over $2 billion</td><td>53%</td></tr><tr><td>Fiduciary 19%</td><td>$1 - $2 billion</td><td>9%</td></tr><tr><td>Wholesaling/Retailing 6%</td><td>$501 million - $1 billion</td><td>17%</td></tr><tr><td>Utilities 2%</td><td>$101 million - $500 million</td><td>9%</td></tr><tr><td>Unspecified 13%</td><td>$100 million and less</td><td>12%</td></tr><tr><td colspan="3">Project Characteristics</td></tr><tr><td>Development cost</td><td colspan="2">Size (in person-days)</td></tr><tr><td>Over $1 million 4%</td><td>Over 1000</td><td>15%</td></tr><tr><td>$501 - $1 million 9%</td><td>501 - 1000</td><td>17%</td></tr><tr><td>$101 - $500,000 19%</td><td>101 - 500</td><td>30%</td></tr><tr><td>$11 - $100,000 40%</td><td>51 - 100</td><td>15%</td></tr><tr><td>$10,000 and less 28%</td><td>11 - 50</td><td>15%</td></tr><tr><td></td><td>0 or less</td><td>8%</td></tr></table>

Table 3. T-Test Analysis of Designer Responses

<table><tr><td>No.</td><td>Item</td><td>Method Favored</td><td>Significant (p = .10)</td><td>Probability</td></tr><tr><td>1.</td><td>Ease of User/Designer Communication</td><td>SDLC</td><td>No</td><td>.9148</td></tr><tr><td>2.</td><td>Satisfaction with User Participation</td><td>Prototype</td><td>Yes</td><td>.0320</td></tr><tr><td>3.</td><td>Amount of Change in User Specifications</td><td>SDLC</td><td>No</td><td>.1166</td></tr><tr><td>4.</td><td>Perceived User/Designer Conflict</td><td>Prototype</td><td>Yes</td><td>.0174</td></tr><tr><td>5.</td><td>User Understanding of the System</td><td>Prototype</td><td>No</td><td>.5382</td></tr><tr><td>6.</td><td>User Influence on the Development Process</td><td>SDLC</td><td>No</td><td>.1884</td></tr><tr><td>7.</td><td>User Commitment to the Project</td><td>Prototype</td><td>No</td><td>.1526</td></tr><tr><td>8.</td><td>Extent of User Use of the System</td><td>Prototype</td><td>Yes</td><td>.0018</td></tr><tr><td>9.</td><td>Satisfaction with the Development Approach</td><td>Prototype</td><td>Yes</td><td>.0102</td></tr><tr><td>10.</td><td>Overall Quality of Development Effort</td><td>Prototype</td><td>No</td><td>.1167</td></tr><tr><td>11.</td><td>Ability to Conceptualize the System</td><td>Prototype</td><td>No</td><td>.1747</td></tr><tr><td>12.</td><td>Ease of Project Management and Control</td><td>SDLC</td><td>Yes</td><td>.0067</td></tr><tr><td>13.</td><td>Project Completed on Schedule</td><td>SDLC</td><td>Yes</td><td>.0793</td></tr><tr><td>14.</td><td>Project Completed in Projected Person-Days</td><td>SDLC</td><td>No</td><td>.7826</td></tr><tr><td>15.</td><td>Project Completed within Budget</td><td>No preference</td><td>No</td><td>.9872</td></tr><tr><td>16.</td><td>Ease of System Planning</td><td>SDLC</td><td>Yes</td><td>.0070</td></tr><tr><td>17.</td><td>Flexibility of the Approach</td><td>Prototype</td><td>Yes</td><td>.0001</td></tr><tr><td>18.</td><td>Requirements (Time, Money, Effort, etc.)</td><td>SDLC</td><td>No</td><td>.9533</td></tr><tr><td>19.</td><td>Validation of User Requirements</td><td>Prototype</td><td>Yes</td><td>.0003</td></tr><tr><td>20.</td><td>Implementation and User Acceptance</td><td>Prototype</td><td>Yes</td><td>.0553</td></tr><tr><td>21.</td><td>User Satisfaction with the System</td><td>Prototype</td><td>No</td><td>.1307</td></tr><tr><td>22.</td><td>System Maintenance Requirements</td><td>SDLC</td><td>No</td><td>.1728</td></tr><tr><td>23.</td><td>Acquisition of Expensive Software</td><td>Prototype</td><td>Yes</td><td>.0384</td></tr><tr><td>24.</td><td>System Testing</td><td>Prototype</td><td>No</td><td>.3744</td></tr></table>

The t-test is appropriate here since it can be used to investigate any significant difference between the responses from the two populations (i.e., SDLC and prototyping). Before the t-test was used, however, the multicollinearity problem was checked, since this could distort the results obtained from a t-test analysis. For example, a t-statistic may not show a statistically significant relationship between the design method and the designer or user item, even though a definite statistical relation exists. Accordingly, a collinearity diagnostic was performed on the user and designer data using the Statistical Analysis System (SAS). The collinearity diagnostic clearly indicated that there is little or no multicollinearity among the independent variables. Also, in analyzing individual designer and user responses the alpha level on the t-test was adjusted to account for multiple testing of the same data.

## Analysis of Individual Responses

At first glance, respondents did not clearly favor either the SLDC or the prototyping approach (Tables 3 and 4). Both designers and users felt each method had its advantages and disadvantages. In fact, user responses indicated almost no significant difference between the two methods (at the .10 level).

Table 3 presents the t-test results of the designer responses. The designers seemed to be more satisfied with the prototyping approach. More specifically, they felt the prototyping method was superior in terms of flexibility and resolving user-related problems (e.g., reducing user/designer conflict, introducing more user participation in the development process, increasing use of the system, validating user requirements, etc.). On the other hand, they also realized that the prototyping method required more expensive software.

The only significant items that favored the SDLC method were ease of systems planning and development, followed by ease of project management and control. While these results are not intuitively surprising, the relatively insignificant difference between the two methods runs contrary to previous laboratory studies.

Table 4. T-Test Analysis of User Responses

<table><tr><td>No.</td><td>Item</td><td>Method Favored</td><td>Significant (p = .10)</td><td>Probability</td></tr><tr><td>1.</td><td>Effect on Complexity of Decision Making</td><td>Prototype</td><td>Yes</td><td>.0026</td></tr><tr><td>2.</td><td>Quality of System Results</td><td>SDLC</td><td>No</td><td>.7213</td></tr><tr><td>3.</td><td>Confidence in Decisions</td><td>Prototype</td><td>No</td><td>.5291</td></tr><tr><td>4.</td><td>Range of Decision-Making Capabilities</td><td>SDLC</td><td>No</td><td>.4406</td></tr><tr><td>5.</td><td>Cost and Effort of Decision Making</td><td>SDLC</td><td>No</td><td>.5929</td></tr><tr><td>6.</td><td>System Flexibility</td><td>Prototype</td><td>No</td><td>.7210</td></tr><tr><td>7.</td><td>User Satisfaction with the System</td><td>Prototype</td><td>No</td><td>.9711</td></tr><tr><td>8.</td><td>Project Completed within Budget</td><td>Prototype</td><td>No</td><td>.5279</td></tr><tr><td>9.</td><td>Project Completed in Projected Person-Days</td><td>SDLC</td><td>No</td><td>.4709</td></tr><tr><td>10.</td><td>Project Completed on Schedule</td><td>Prototype</td><td>No</td><td>.7073</td></tr><tr><td>11.</td><td>Acquisition of Expensive Software</td><td>Prototype</td><td>No</td><td>.6434</td></tr><tr><td>12.</td><td>Time from Request to System Completion</td><td>Prototype</td><td>No</td><td>.1902</td></tr><tr><td>13.</td><td>Timeliness of System Output Information</td><td>SDLC</td><td>No</td><td>.5126</td></tr><tr><td>14.</td><td>Communication with the DP/MIS Staff</td><td>SDLC</td><td>No</td><td>.7432</td></tr><tr><td>15.</td><td>Ability to Produce Output</td><td>No preference</td><td>No</td><td>.9857</td></tr><tr><td>16.</td><td>Estimation of Decision-Making Variables</td><td>Prototype</td><td>No</td><td>.2426</td></tr><tr><td>17.</td><td>Accuracy of System Output</td><td>SDLC</td><td>No</td><td>.3330</td></tr><tr><td>18.</td><td>Reliability of Output Information</td><td>Prototype</td><td>No</td><td>.3932</td></tr><tr><td>19.</td><td>Convenience of Access to the System</td><td>Prototype</td><td>No</td><td>.8870</td></tr><tr><td>20.</td><td>User Feeling of Control of the Project</td><td>Prototype</td><td>No</td><td>.4073</td></tr><tr><td>21.</td><td>Relationship with the DP/MIS Staff</td><td>SDLC</td><td>No</td><td>.8645</td></tr><tr><td>22.</td><td>User Feelings of Participation in Project</td><td>Prototype</td><td>No</td><td>.4432</td></tr><tr><td>23.</td><td>User Understanding of the System</td><td>Prototype</td><td>No</td><td>.5860</td></tr><tr><td>24.</td><td>Relevance of Output to Intended Function</td><td>SDLC</td><td>No</td><td>.8908</td></tr></table>

Table 4 presents the results of similar analysis of user responses on individual items. Surprisingly, the findings indicated a significant difference between the two development methods only with respect to the system's effect on the complexity of decision making. The users felt that the prototyping method helped reduce complexity. Previous studies have generally shown users to be significantly more satisfied with the prototyping system development effort than the traditional SDLC method. The present research did not bear out these conclusions.

## Combined Effects of Responses

In addition to analyzing individual responses, the author used linear multiple regression analysis to determine the extent to which all of the items combined explain the variation in preference of a design method. A residual analysis was performed on the designer and user data to investigate their adherence to the multiple regression model's assumptions of normality, homogeneity, and randomness. The residual analysis confirmed the fact that the user and designer data reasonably satisfy these assumptions.

Using a linear combination of all items, the designer responses interpreted 65 percent of the variation in the selection process (i.e., $r^{2}$ was 64.71), while 75 percent of the variation in the same was explained by the user responses (i.e., $r^{2}$ was 74.50). The designer items that contributed significantly (at the .10 level) to this interpretation can be divided into user and system dimensions (see Appendix A). The user dimension referred to user requirements for and user acceptance of the system, while the system dimension pertained to system maintenance and expensive software acquisitions.

Similarly, the user items can be segregated into decision making, project, and output (see Appendix B). Using the decision-making dimension, the users emphasized system support for reducing decision complexity, estimating decision variables, system design cost and effort, increasing communication with the DP/MIS staff, and increasing the user's feeling of participation in the project. When it came to the project, the users stressed the importance of completing a project on time and within budget. In terms of the output, the users emphasized the ability to produce a variety of outputs (e.g. reports, charts, diagrams, and pictures).

This whole process of analysis for combined effects indicated that while individual item responses were not very successful in differentiating between the two methods, all of the items together were able to explain the difference more effectively. This was especially true for user responses and would seem to indicate that the difference between the two development approaches is a complex one, not necessarily assailable through individual items.

## Analysis of Group Effects

Looking at either individual or combined effects of items can be revealing, but it is also important to distill these into several central issues that can be used to weigh the relative advantages and disadvantages of each approach. Principal components factor analysis was employed on all user and designer items to extract those issues represented by factors (minimum eigenvalue of 0.95 with a varimax rotation was used). Using a cutoff level of 0.50, two six-factor structures—one for the designer items and one for the user items—resulted with all the items loading at that level. The designer factors explained 75% of the total variance in the original designer items, while 77% of the variance in the original user items was accounted for by the user factors.

Appendix C shows the designer items loading on different factors. The first factor carried with it the items related to project management. The second factor was drawn from the measures associated with user contribution and project implementation. The third factor referred to the criteria contained in user-designer interaction. The fourth factor dealt with user satisfaction and acceptance items. The fifth factor encompassed the project requirements criteria. The sixth factor entailed only one item—user change in specifications. All items from the designer questionnaire were loaded on at least one factor.

Appendix D shows the user items loading on different factors. The first factor pertained to user contribution to the project. The second factor evolved from the items related to user satisfaction with system outputs. The third factor was composed of project management items. The fourth factor was fabricated from the variables related to the system's impact on decision effectiveness. The fifth factor was carved out of the two items which related to quality of system results. The sixth factor was related to the system's effect on the decision-making process. All items from the user questionnaire were also loaded on at least one factor. While no a priori loadings were hypothesized, the results of the factor analysis indicate the validity of the instruments.

Table 5. T-Test Analysis of Designer and User Factors

<table><tr><td>No.</td><td>Designer Factors</td><td>Method Favored</td><td>Significant (p = .10)</td><td>Probability</td></tr><tr><td>1.</td><td>Project Management</td><td>SDLC</td><td>Yes</td><td>.0875</td></tr><tr><td>2.</td><td>Perceived User Contribution</td><td>Prototype</td><td>Yes</td><td>.0002</td></tr><tr><td>3.</td><td>Perceived User-Designer Interaction</td><td>Prototype</td><td>No</td><td>.5579</td></tr><tr><td>4.</td><td>Post-Implementation Consideration</td><td>Prototype</td><td>No</td><td>.9499</td></tr><tr><td>5.</td><td>Project Requirements</td><td>Prototype</td><td>No</td><td>.2338</td></tr><tr><td>6.</td><td>Change in Specifications</td><td>SDLC</td><td>No</td><td>.1166</td></tr><tr><td>No.</td><td>User Factors</td><td>Method Favored</td><td>Significant (p = .10)</td><td>Probability</td></tr><tr><td>1.</td><td>User Contribution</td><td>Prototype</td><td>No</td><td>.5630</td></tr><tr><td>2.</td><td>Satisfaction with Outputs</td><td>SDLC</td><td>No</td><td>.6977</td></tr><tr><td>3.</td><td>Project Management</td><td>Prototype</td><td>No</td><td>.9226</td></tr><tr><td>4.</td><td>Impact on Decision Effectiveness</td><td>Prototype</td><td>No</td><td>.9825</td></tr><tr><td>5.</td><td>Quality of System Results</td><td>Prototype</td><td>No</td><td>.5855</td></tr><tr><td>6.</td><td>Effect on Decision-Making</td><td>Prototype</td><td>No</td><td>.2214</td></tr></table>

As was true with the individual items, a t-test analysis of these factors revealed relatively little correlation between the factors and the development methods (Table 5). Only designer factors 1 (project management) and 2 (user contribution/implementation) were able to distinguish between the two methods at the .10 significance level. The other three designer factors and all user factors were not able to discriminate between the development methods. This analysis, once again, provides evidence as to the complexity involved in differentiating between the two design methods.

## Consistency of Responses

This part of the analysis focused on the consistency of the designer and user responses. Of the twenty-four items used for the designers and users, twelve of these items were aimed at the same issues for both groups. Kendall's Tau analysis of the responses for these items revealed agreement between the users and designers on six items and disagreement on six items, although only four of these agreements were statistically significant (Table 6). The most significant difference of opinions between the two groups seemed to be in the area of project cost and scheduling. The users felt the prousers felt the prototyping method resulted in better managed projects, while the designers thought the SDLC-designed systems were likely to take less time and money. The items on which both the designer and user groups agreed should be emphasized and carefully examined in selecting a development method. The items on which they disagreed need further research and investigation.

Table 6. Measuring Consistency of Responses (Kendall's Tau Analysis)

<table><tr><td colspan="5">USERS AND DESIGNERS AGREED ON:</td></tr><tr><td>No. Item</td><td>DesignersFavored</td><td>UsersFavored</td><td>Significant(p = .10)</td><td>Probability</td></tr><tr><td>1. Ease of User/Designer Communication</td><td>SDLC</td><td>SDLC</td><td>No</td><td>.1417</td></tr><tr><td>2. Satisfaction with User Participation</td><td>Prototype</td><td>Prototype</td><td>No</td><td>.1363</td></tr><tr><td>3. User Understanding of the System</td><td>Prototype</td><td>Prototype</td><td>Yes</td><td>.0165</td></tr><tr><td>4. Project Completed in Projected Person-Days</td><td>SDLC</td><td>SDLC</td><td>Yes</td><td>.0017</td></tr><tr><td>5. User Satisfaction with the System</td><td>Prototype</td><td>Prototype</td><td>Yes</td><td>.0910</td></tr><tr><td>6. Acquisition of Expensive Software</td><td>Prototype</td><td>Prototype</td><td>Yes</td><td>.0505</td></tr><tr><td colspan="5">USERS AND DESIGNERS DISAGREED ON:</td></tr><tr><td>No. Item</td><td>DesignersFavored</td><td>UsersFavored</td><td>Significant(p = .10)</td><td>Probability</td></tr><tr><td>1. Perceived User/Designer Conflict</td><td>Prototype</td><td>SDLC</td><td>Yes</td><td>.0134</td></tr><tr><td>2. User Influence on the Development Process</td><td>SDLC</td><td>Prototype</td><td>Yes</td><td>.0983</td></tr><tr><td>3. Project Completed on Schedule</td><td>SDLC</td><td>Prototype</td><td>Yes</td><td>.0281</td></tr><tr><td>4. Project Completed within Budget</td><td>No preference</td><td>Prototype</td><td>Yes</td><td>.0003</td></tr><tr><td>5. Requirements (Time, Money, Effort, etc.)</td><td>SDLC</td><td>Prototype</td><td>Yes</td><td>.0468</td></tr><tr><td>6. Validation of User Requirements</td><td>Prototype</td><td>SDLC</td><td>Yes</td><td>.0975</td></tr></table>

## Effect of Project Characteristics

In the final analysis, project characteristics (e.g., cost, duration, effort, type and mode) and IS organizational characteristics (e.g., maturity and budget) were used in an effort to differentiate between the preferences for the two development methods. Only the IS organization's maturity and project mode (i.e., online or batch) were statistically significant at the .10 level. Project size was significant at the .15 level. Other project and IS organizational characteristics did not play a significant role in selecting a development method.

## Discussion

The present research indicates that both the designer and the user items, individually and in groups, are not very effective in predicting preference for a development method. When combined, however, they became powerful tools for such forecasting.

The study also demonstrates that, although the designers preferred the prototyping method more often than the users, the inclination to use prototyping was not very strong. For example, of 24 designer items, only 14 showed the designers' preference toward the prototyping method. Of those 14, only 8 items were statistically significant (Table 3).

This was even more obvious for the user responses. While users favored the prototyping method for approximately half the items (14 out of 24 items), only one item—that prototyped systems helped reduce the complexity of decision making—was statistically significant at the .10 level.

Alavi [2] and Dearnley and Mayhew [20] found, through their research, that the prototyping method made it difficult to manage and control a project, and brought in more changes in user specifications [2]. The present study partially confirmed these findings. Contrary to Alavi's findings, the present research found the latter item, changes in user specifications, to be not significant. In addition, the present study also discovered that prototyping made it arduous to plan.

Alavi [2] stated that this difficulty in management and change in specifications could be due to increased user participation. The present study confirmed that fact. It should be noted, however, that user participation was perceived as statistically significant by the designers, not by the users' own responses. It is encouraging to note that this increased user participation did not bring in additional user-designer conflicts. This result may be due, in part, to the prior identification and validation of user requirements, as confirmed by this research [2, 13, 16, 20, 34].

In addition, the results of the study indicated increased use of systems by the users, as perceived by the designers. This increased use can be partially explained by the fact that the users had a better understanding of and higher satisfaction with the prototyped systems. The intensified use can also be explained by increased user involvement in the design process (as perceived by the designers), which gave users a sense of ownership [18]. The literature [8, 12, 35] suggested that the prototyping method required expensive and unfamiliar software and the results of this study support that conclusion (see Table 3).

Table 7. T-Test Analysis of Project Characteristics

<table><tr><td>No.</td><td>Project Characteristic</td><td>Method Favored By Designers</td><td>Significant at .10</td><td>Probability</td></tr><tr><td>1.</td><td>Project Cost</td><td>SDLC</td><td>No</td><td>.6378</td></tr><tr><td>2.</td><td>Project Duration</td><td>Prototype</td><td>No</td><td>.5553</td></tr><tr><td>3.</td><td>Project Effort</td><td>SDLC</td><td>No</td><td>.1594</td></tr><tr><td>4.</td><td>Project Type</td><td>SDLC</td><td>No</td><td>.3557</td></tr><tr><td>5.</td><td>Project Mode</td><td>SDLC</td><td>Yes</td><td>.0125</td></tr><tr><td>6.</td><td>IS Organization Maturity</td><td>Prototype</td><td>Yes</td><td>.0505</td></tr><tr><td>7.</td><td>IS Budget</td><td>Prototype</td><td>No</td><td>.4738</td></tr></table>

Previous studies $[2, 10, 20]$ found users more satisfied with the prototyping approach than the SDLC method. Of these studies, one $[2]$ revealed significantly higher user satisfaction with prototyped systems. The present research did not bear out this conclusion. The difference between the two methods, in terms of perceived user satisfaction (as rated by the designer) and actual user satisfaction, was not statistically significant, although both groups rated user satisfaction higher with the prototyped systems.

Several prototyping researchers [2, 10, 20] have commented that prototyping improves communication between system designers and users. The analysis of the users' and designers' responses did not support this remark.

Alavi [2] stated that the prototyped outputs were seen by the users as more accurate and helpful. Again, the results of the present study did not bear out those findings (see Table 4).

## A Framework for Reviewing System Design Methods

Based on the preceding analyses and discussions, a practical procedure for systematically evaluating the design methods is presented in this section. The author cautions the readers at the outset that there is no magic wand to assist in selecting a design method, nor is there any mathematical formula that does the job.

Previous studies [1, 9, 11] have commented on the selection of an appropriate development strategy for a given project. However to this author's knowledge, none has put forth a framework for systematic evaluation of the appropriateness of design methods.

When a project manager needs to decide on a design for a specific project, the present framework will help him/her select an appropriate development method by providing proper guidelines.

The framework was constructed using the average of the designer and user responses on a total of 13 significant items (at the .10 level of significance). Of those 13, seven came from the designer items dealing exclusively with the designers' issues. Four were selected aimed at the users' issues, and the rest were common items relevant to both the designers and users. Table 8 consists of a five-interval scale. This scale is the same as the original seven-interval Likert-type scale minus the first and last intervals. These intervals were deleted from the table since no item-average fell in those intervals. Appropriate qualifiers were also added to each interval for each item.

The t-test results were used to decide on the method favored and its significance level for each item. The following procedures were used on the common items to decide for the same.

1. For those items where designer and user groups agreed, the lowest significance level of the two (provided it is less than the .10 level) was reported in the table;

2. For those items where designer and user groups disagreed,

a. if one of the two items was significant, the significant one was reported irrespective of its significance level;

b. if none were significant, they were not included in the table.

The framework, by far, favors the prototyping approach. Of the thirteen statistically significant items, only four supported the SDLC approach. The designers perceived the SDLC-based projects as predominantly batch-oriented and easier to plan, manage and control. Both the designers and users thought that SDLC-based projects are more likely to be completed on time.

Both groups overwhelmingly favored the prototyping approach. The users perceived the prototyping approach as a panacea for improved user-DP relations, greater feelings of participation in the system development process, and more relevant output. At the same time, they felt that the use of the prototyping method increases decision-making complexities. The designers also expressed more satisfaction with the prototyping approach and felt that it increased the overall quality of the development effort. The designers perceived the prototyping approach as a more flexible approach that facilitates implementation and user acceptance, coupled with increased user commitment and use of the system. Both groups felt that the use of prototyping may require acquisition of expensive software.

Table 8. A Framework for the Final Selection Analysis

<table><tr><td rowspan="2">Item</td><td colspan="5">Scale</td><td rowspan="2">Method Favored</td><td rowspan="2">Favored By</td><td rowspan="2">Significant Level</td></tr><tr><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Flexibility of the Approach</td><td>Inflexible</td><td>Somewhat Inflexible</td><td>Neither</td><td>Somewhat Flexible</td><td> $Flexible^P$ </td><td>Prototype</td><td>Designers</td><td>.0001</td></tr><tr><td>Implementation and User Acceptance</td><td>Hindered</td><td>Somewhat Hindered</td><td>Neither</td><td>Somewhat Facilitated</td><td> $Facilitated^P$ </td><td>Prototype</td><td>Designers</td><td>.0005</td></tr><tr><td>Extent of User Use of the System</td><td>Decreased</td><td>Somewhat Decreased</td><td>No Change</td><td>Somewhat Increased</td><td> $Increased^P$ </td><td>Prototype</td><td>Designers</td><td>.0018</td></tr><tr><td>Relevance of Output to Intended Function</td><td>Irrelevant</td><td>Somewhat Irrelevant</td><td>Neither</td><td>Somewhat Relevant</td><td> $Relevant^P$ </td><td>Prototype</td><td>Users</td><td>.0030</td></tr><tr><td>Ease of Project Management and Control</td><td>Obstructed</td><td> $Somewhat^S$  Obstructed</td><td>Neither</td><td> $Somewhat^S$  Aided</td><td>Aided</td><td>SDLC</td><td>Designers</td><td>.0067</td></tr><tr><td>Ease of System Planning</td><td>Hindered</td><td>Somewhat Hindered</td><td>Neither</td><td>Somewhat Helped</td><td> $Helped^S$ </td><td>SDLC</td><td>Designers</td><td>.0070</td></tr><tr><td>Effect on Decision Making Complexities</td><td>Decreased</td><td>Somewhat Decreased</td><td>No Change</td><td>Somewhat Increased</td><td> $Increased^P$ </td><td>Prototype</td><td>Users</td><td>.0101</td></tr><tr><td>Development Approach</td><td>Dissatisfied</td><td>Somewhat Dissatisfied</td><td>Neither</td><td>Somewhat Satisfied</td><td> $Satisfied^P$ </td><td>Prototype</td><td>Designers</td><td>.0102</td></tr><tr><td>Relationship with DP/MIS Staff</td><td>Worsened</td><td>Somewhat Worsened</td><td>No Change</td><td>Somewhat Improved</td><td> $Improved^P$ </td><td>Prototype</td><td>Users</td><td>.0174</td></tr><tr><td>User Feeling of Participation in the Project</td><td>Dissatisfied</td><td>Somewhat Dissatisfied</td><td>Neither</td><td>Somewhat Satisfied</td><td> $Satisfied^P$ </td><td>Prototype</td><td>Users</td><td>.0320</td></tr><tr><td>Acquisition of Expensive Software</td><td>Not Required</td><td>Sometimes Not Required</td><td>No Change</td><td>Sometimes Required</td><td> $Required^P$ </td><td>Prototype</td><td>Both</td><td>.0384</td></tr><tr><td>Project Mode</td><td>Online</td><td> $Batch^S$ </td><td>-</td><td>-</td><td>-</td><td>SDLC</td><td>Designers</td><td>.0525</td></tr><tr><td>Project Completed on Schedule</td><td>Off Schedule</td><td>Sometimes Off Schedule</td><td>No Change</td><td> $Sometimes^S$  On Schedule</td><td>On Schedule</td><td>SDLC</td><td>Both</td><td>.0797</td></tr><tr><td></td><td></td><td>Somewhat</td><td>No</td><td>Somewhat</td><td></td><td></td><td></td><td></td></tr></table>

Superscript 'S' indicates SDLC
Superscript 'P' indicates Prototype

In summary, if a project manager is interested in a relatively easy-to-plan and easy-to-manage project, has a tight schedule, and lacks state-of-the-art technology, he or she should definitely look into the possibility of using the SDLC approach. On the other hand, if the project manager is interested in increased user satisfaction and commitment to the system, designer satisfaction with the design approach, and does not have constraints on acquiring additional design and development tools, he should choose the prototyping approach.

## Limitations

The research carries some limitations. First, it concerns only those systems that are developed using either an SDLC or prototyping method. Clearly, there are systems that may be developed using a hybrid method. This study may not help those project managers who use a hybrid approach to design and develop a system.

Second, some of the responses may not be based on users' and designers' actual experiences. Rather, they may be based on their perceptions of the design methods. It is possible that the respondents have biased their responses with their own perceptions of the system design methods, even though they were asked to fill out the questionnaires based on their most recent experience with designing or using a system.

Third, the study used the DP/MIS managers, designers, and users in classifying a system as prototype- or SDLC-based. Even though such dependency is not uncommon in the literature, it clearly leaves some room for bias.

## Conclusion and Implications

The fundamental conclusion of this research is that the effectiveness of a system design method is influenced by a project's requirements, characteristics, user and designer satisfaction, and impact on the decision-making process. This conclusion, arrived at empirically, is a confirmation of certain statements in the literature, while it contradicts some intuitive expectations and assertions by previous researchers. The conclusion is a departure from implicit assumptions by the supporters of the prototyping and SDLC methods that these approaches can be applied to any project regardless of its characteristics or decision situation for which it is being designed.

To improve the effectiveness of system development methods, the findings of the research suggest the following:

1. System development techniques cannot be considered apart from the project's characteristics or requirements.

2. Decision characteristics, such as decision complexity and decision needs, should be considered in selecting a development method.

3. Criteria relating to user and designer satisfaction with the development approaches should be carefully weighed before choosing a development method.

4. Criteria related to user satisfaction with output should be evaluated before using a development technique.

5. Based on the analyses of user and designer responses, a framework can be established to help project managers in selecting a development method for a specific project.

Some of the results of the study are both clear and confusing at the same time. They are clear in that they show a definitive relationship between the development methods and the project and decision characteristics. They are confusing in that they are contrary to some intuitive expectations and assertions by previous researchers.

Further research must be undertaken in real-world settings before definitive conclusions can be reached about the selection of a development method.

The following are suggested:

1. The motivation behind this research was that system development methods are different and we should unearth sufficient information about these differences to facilitate a more informed selection of a development method. Not all factors of these differences, however, have been considered. Other factors, such as IS organizational and functional area characteristics, should be considered.

2. This research relied on the DP/MIS managers, designers and users to characterize a system as SDLC- or prototype-based. Further research should be undertaken for the development of a reliable method to accurately classify the development method for any given system.

3. Research should be conducted to determine the effect on the development method of differences in user style and preference. It might be unwise to recommend prototyping for a project when the potential user(s) are not willing to get involved in the development process for lack of time or other reasons.

4. Research should also be conducted on the effect of skills and cognitive makeup of the designers on the selection of development methods.

## Acknowledgments

The author thanks Paul VanWert for his help in data analyses.

## References

1. Ahituv, N., Hadass, M. and Neumann, S. "A Flexible Approach to Information System Development," MIS Quarterly, Volume 8, Number 2, June 1984, pp. 69–78.

2. Alavi, M. "An Assessment of the Prototyping Approach to Information Systems Development," Communications of the ACM, Volume 27, Number 6, June 1984, pp. 556–563.

3. Appleton, D.S. "Data-Driven Prototyping," Datamation, November 1983, pp. 259–268.

4. Bailey, J.E. and Pearson, S.W. "Development of a Tool for Measuring and Analyzing Computer User Satisfaction," Management Science, Volume 29, Number 6, 1983, pp. 519–529.

5. Bell, T.E. "Structured Life-Cycle Assumptions," ACM Performance Evaluation Re-

view, Volume 10, Number 1, Spring 1981, pp. 1–3.

6. Benbasat, I. and Taylor, R.N. "The Impact of Cognitive Styles on Information System Design," MIS Quarterly, Volume 2, Number 2, June 1978, pp. 43–54.

7. Berrisford, T.R. and Wetherbe, J.C. "Heuristic Development: A Redesign of Systems Design," MIS Quarterly, Volume 3, Number 1, March 1979, pp. 11–19.

8. Blum, B.I. "A Work Station for Information System Development," IEEE Proceedings in Computer Science, Tucson, Arizona, November 7–9, 1983, pp. 116–120.

9. Boehm, B.W., Gray, T.E. and Seewaldt, T. "Prototyping vs. Specifying: A Multi-Project Experiment," IEEE Proceedings of the 7th International Conference on Software Engineering, Orlando, Florida, March 26–29, 1984, pp. 473–485.

10. Brice, L., Connell, J. and Shafer, D. "Using INGRES as a Rapid Prototyping Device During Development of Management Information Applications," IEEE Proceedings in Computer Science, Tucson, Arizona, November 7–9, 1983, pp. 34–43.

11. Budde, R., Kuhlenkamp, K., Mathiassen, L., and Zullighoven, H. "Working Conference on Prototyping," Information and Management, Volume 7, Number 3, June 1984, pp. 149–168.

12. Burford, M.A.J., and Belli, F. "CADAS: A Tool for Rapid Prototyping and Testing of Embedded Software," IEEE Proceedings on Database Conference, San Jose, California, May 23–26, 1983, pp. 27–33.

13. Canning, R.G. "Tools to Rejuvenate Your Old Systems," EDP Analyzer, Volume 22, Number 4, April 1984, pp. 1–14.

14. Chapin, N. "Prototyping—Quick, Not Dirty," Data Management, Volume 21, Number 10, October 1983, pp. 46–48.

15. Connell, J. and Brice, L. "Rapid Prototyping," Datamation, Volume 30, August 15, 1984, pp. 93–100.

16. Coughlin, D.T. "System Development Methodology or System Research Methodology?" ACM Performance Evaluation Review, Volume 10, Number 1, Spring 1981, pp. 5–6.

17. Couger, J.D. "Evolution of Business System Analysis Techniques," Computing Surveys, Volume 5, Number 3, September 1973, pp. 167–198.

18. Courbon, J.C., Grajew, J. and Tolovi, J.

"Design and Implementation of Decision Support Systems by an Evolutive Approach," Unpublished Working Paper, Grenoble, France 1978.

19. Davis, G.B. and Olson, M.H. Management Information Systems: Conceptual Foundations, Structure, and Development, McGraw-Hill, New York, New York, 1985.

20. Dearnley, P.A. and Mayhew, P.J. "In Favour of System Prototypes and Their Integration into the Systems Development Cycle," The Computer Journal, Volume 26, Number 1, February 1983, pp. 36–42.

21. Gallagher, C.A. "Perceptions of the Value of a Management Information System," Academy of Management Journal, Volume 17, Number 1, March 1974, pp. 46–55.

22. Graver, C.A., Balkovich, E.E., Carriere, W.M., and Thibodeau, R. "Tradeoffs for Defense System Software, General Research Corporation," California Final Report, Number CR-1-721, General Research Corporation, March 1977.

23. Gremillion, L.L. and Pyburn, P. "Breaking the Systems Development Bottleneck," Harvard Business Review, Volume 61, Number 2, March–April 1983, pp. 130–137.

24. Harel, E.C. and McLean, E.R. "The Effects of Using a Nonprocedural Language on Programmer Productivity," M/S Quarterly, Volume 9, Number 2, June 1985, pp. 109–120.

25. Ives, B., Olson, M.H., and Baroudi, J.J., "The Measurement of User Information Satisfaction," Communications of the ACM, Volume 26, Number 10, October 1983, pp. 785–793.

26. Jenkins, A.M. "Prototyping: A Methodology for the Design and Development of Application Systems," Research Paper #221, Indiana University, Division of Research, School of Business, April 1983.

27. Jenkins, A.M., Naumann, J.D., and Wetherbe, J.C. "Empirical Investigation of Systems Development Practices and Results," Information and Management, Volume 7, Number 2, April 1984, pp. 73–82.

28. Jenkins, C.W. "Application Prototyping:

A Case Study," ACM Performance Evaluation Review, Volume 10, Number 1, Spring 1981, pp. 21–27.

29. McFarlan, F.W. "Portfolio Approach to Information Systems," Harvard Business Review, Volume 59, Number 5, September–October 1981, pp. 142–150.

30. McKeen, J.D. "Successful Development Strategies for Business Application Systems," MIS Quarterly, Volume 7, Number 3, September 1983, pp. 47–65.

31. McKenney, J.L., McFarlan, F.W. and Pyburn, P. "The Information Archipelago—Plotting a Course," Harvard Business Review, Volume 61, Number 1, January–February 1983, pp. 145–156.

32. Miner, R.J., Grant, M.E., and Mayer, R.J. "Decision Support for Manufacturing," IEEE 1981 Winter Simulation Conference Proceedings, pp. 543–549.

33. Mittermeir, R.T., Hsia, P. and Yeh, R.T. Requirements Engineering Environments, North-Holland Publishing Company, Amsterdam, Holland 1982.

34. Naumann, J.D. and Davis, G.B. "A Contingency Theory to Select an Information Requirements Determination Methodology," Journal of Systems Software, Volume 1, Number 4, December 1980, pp. 29–44.

35. Naumann, J.D. and Jenkins, A.M. "Prototyping: The New Paradigm for Systems Development," M/S Quarterly, Volume 6, Number 3, September 1982, pp. 29–44.

36. Pearson, S.W. "Measurement of Computer User Satisfaction," Ph.D. Dissertation, Arizona State University, Tempe, Arizona, 1977.

37. Peters, L.J. and Tripp, L.L. "Comparing Software Design Methodologies," Data-mation, Volume 23, November 1977, pp. 89–94.

38. Podolsky, J.L. "Horace Builds a Cycle," Datamation, Volume 23, November 1977, pp. 162–168.

39. Spiegel, M.G. "Prototyping: An Approach to Information and Communication System Design," ACM Performance Evaluation Review, Volume 10, Number 1, Spring 1981, pp. 9–19.

40. Zajonc, P.C. and McGowan, K.J. "Proto-Cycling: A New Method for Application Development Using Fourth Generation Languages," unpublished paper.

## About the Author

A former NASA faculty fellow, Mo A. Mahmood is Associate Professor of Management Information Systems at the University of Texas-El Paso. Prior to joining UT-El Paso he taught at the University of Missouri-St. Louis and Eastern Kentucky University. Dr. Mahmood received his D.B.A. in management information systems from Texas Tech University and holds an M.B.A. from California State

University. He has published in the Journal of Systems Management, Data Base, Decision Sciences, the Journal of Management Information Systems, the International Journal of Policy and Information, Information and Management, INFOR—Canadian Journal of Operation Research and Information Processing (forthcoming).

## Appendix A Linear Regression Analysis of Designer Responses

## Dependent Variable: Design Method Preference

<table><tr><td>Source</td><td>DF</td><td>Sum of Squares</td><td>Mean Square</td><td>F Value</td><td>Probability &gt; F</td></tr><tr><td>Model</td><td>24</td><td>7.883565</td><td>0.328432</td><td>2.674</td><td>0.0040</td></tr><tr><td>Error</td><td>35</td><td>4.299768</td><td>0.122851</td><td></td><td></td></tr><tr><td>C Total</td><td>59</td><td>12.183333</td><td></td><td></td><td></td></tr><tr><td>Root MSE</td><td></td><td>0.350500</td><td>R-Square</td><td>0.6471</td><td></td></tr><tr><td>Dep Mean</td><td></td><td>1.283333</td><td></td><td></td><td></td></tr><tr><td>C.V.</td><td></td><td>27.31172</td><td></td><td></td><td></td></tr></table>

<table><tr><td>No.</td><td>Item</td><td>Probability &gt; |T|</td></tr><tr><td>0.</td><td>Intercept</td><td>0.1496</td></tr><tr><td>1.</td><td>Ease of User/Designer Communication</td><td>0.8150</td></tr><tr><td>2.</td><td>Satisfaction with User Participation</td><td>0.5189</td></tr><tr><td>3.</td><td>Amount of Change in User Specifications</td><td>0.1448</td></tr><tr><td>4.</td><td>Perceived User/Designer Conflict</td><td>0.8783</td></tr><tr><td>5.</td><td>User Understanding of the System</td><td>0.8877</td></tr><tr><td>6.</td><td>User Influence on the Development Process</td><td>0.5054</td></tr><tr><td>7.</td><td>User Commitment to the Project</td><td>0.3427</td></tr><tr><td>8.</td><td>Extent of User Use of the System</td><td>0.6180</td></tr><tr><td>9.</td><td>Satisfaction with the Development Approach</td><td>0.9698</td></tr><tr><td>10.</td><td>Overall Quality of Development Effort</td><td>0.7844</td></tr><tr><td>11.</td><td>Ability to Conceptualize the System</td><td>0.5535</td></tr><tr><td>12.</td><td>Ease of Project Management and Control</td><td>0.1413</td></tr><tr><td>13.</td><td>Project Completed on Schedule</td><td>0.2610</td></tr><tr><td>14.</td><td>Project Completed in Projected Person-Days</td><td>0.3420</td></tr><tr><td>15.</td><td>Project Completed within Budget</td><td>0.7216</td></tr><tr><td>16.</td><td>Ease of System Planning</td><td>0.9302</td></tr><tr><td>17.</td><td>Flexibility of the Approach</td><td>0.8686</td></tr><tr><td>18.</td><td>Requirements (Time, Money, Effort, etc.)</td><td>0.5471</td></tr><tr><td>19.</td><td>Validation of User Requirements</td><td>0.0624</td></tr><tr><td>20.</td><td>Implementation and User Acceptance</td><td>0.0856</td></tr><tr><td>21.</td><td>User Satisfaction with the System</td><td>0.8785</td></tr><tr><td>22.</td><td>System Maintenance Requirements</td><td>0.0532</td></tr><tr><td>23.</td><td>Acquisition of Expensive Software</td><td>0.0449</td></tr><tr><td>24.</td><td>System Testing</td><td>0.8970</td></tr></table>

# Appendix B Linear Regression Analysis of User Responses

Dependent Variable: Design Method Preference

<table><tr><td>Source</td><td>DF</td><td>Sum of Squares</td><td>Mean Square</td><td>F Value</td><td>Probability &gt; F</td></tr><tr><td>Model</td><td>24</td><td>7.566959</td><td>0.315290</td><td>3.165</td><td>0.0025</td></tr><tr><td>Error</td><td>26</td><td>2.589904</td><td>0.099612</td><td></td><td></td></tr><tr><td>C Total</td><td>50</td><td>10.156863</td><td></td><td></td><td></td></tr><tr><td>Root MSE</td><td></td><td>0.315613</td><td>R-Square</td><td>0.7450</td><td></td></tr><tr><td>Dep Mean</td><td></td><td>1.274510</td><td></td><td></td><td></td></tr><tr><td>C.V.</td><td></td><td>24.7635</td><td></td><td></td><td></td></tr></table>

<table><tr><td>No.</td><td>Item</td><td>Probability &gt; | T</td></tr><tr><td>0.</td><td>Intercept</td><td>0.1121</td></tr><tr><td>1.</td><td>Effect on Complexity of Decision-Making</td><td>0.0001</td></tr><tr><td>2.</td><td>Quality of System Results</td><td>0.6942</td></tr><tr><td>3.</td><td>Confidence in Decisions</td><td>0.6918</td></tr><tr><td>4.</td><td>Range of Decision-Making Capabilities</td><td>0.5479</td></tr><tr><td>5.</td><td>Cost and Effort of Decision-Making</td><td>0.0591</td></tr><tr><td>6.</td><td>System Flexibility</td><td>0.1496</td></tr><tr><td>7.</td><td>User Satisfaction with the System</td><td>0.7511</td></tr><tr><td>8.</td><td>Project Completed within Budget</td><td>0.0665</td></tr><tr><td>9.</td><td>Project Completed in Projected Person-Days</td><td>0.0128</td></tr><tr><td>10.</td><td>Project Completed on Schedule</td><td>0.6401</td></tr><tr><td>11.</td><td>Acquisition of Expensive Software</td><td>0.5507</td></tr><tr><td>12.</td><td>Time from Request to System Completion</td><td>0.9037</td></tr><tr><td>13.</td><td>Timeliness of System Output Information</td><td>0.4608</td></tr><tr><td>14.</td><td>Communication with the DP/MIS Staff</td><td>0.0508</td></tr><tr><td>15.</td><td>Ability to Produce Output</td><td>0.0386</td></tr><tr><td>16.</td><td>Estimation of Decision-Making Variables</td><td>0.0089</td></tr><tr><td>17.</td><td>Accuracy of System Output</td><td>0.3394</td></tr><tr><td>18.</td><td>Reliability of Output Information</td><td>0.1338</td></tr><tr><td>19.</td><td>Convenience of Access to the System</td><td>0.1941</td></tr><tr><td>20.</td><td>User Feeling of Control of the Project</td><td>0.3101</td></tr><tr><td>21.</td><td>Relationship with the DP/MIS Staff</td><td>0.6119</td></tr><tr><td>22.</td><td>User Feelings of Participation in Project</td><td>0.0148</td></tr><tr><td>23.</td><td>User Understanding of the System</td><td>0.4131</td></tr><tr><td>24.</td><td>Relevance of Output to Intended Function</td><td>0.5598</td></tr></table>

Appendix C
Factor Analysis of Designer Responses

<table><tr><td colspan="8">Factor Analysis of Designer Responses</td></tr><tr><td rowspan="2">No.</td><td rowspan="2">Item</td><td colspan="6">Factor Loadings</td></tr><tr><td>Project Management</td><td>User Contribution</td><td>User Designer Interaction</td><td>Post-Implementation Consideration</td><td>Project Requirements</td><td>Change In Specifications</td></tr><tr><td>1.</td><td>Ease of User/Designer Communication</td><td>0.52345</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2.</td><td>Satisfaction with User Participation</td><td>0.52356</td><td>0.54870</td><td></td><td></td><td></td><td></td></tr><tr><td>3.</td><td>Amount of Change in User Specifications</td><td></td><td></td><td></td><td></td><td></td><td>0.86221</td></tr><tr><td>4.</td><td>Perceived User/Designer Conflict</td><td></td><td></td><td>0.65482</td><td></td><td></td><td></td></tr><tr><td>5.</td><td>User Understanding of the System</td><td></td><td></td><td>0.80583</td><td></td><td></td><td></td></tr><tr><td>6.</td><td>User Influence on the Development Process</td><td></td><td></td><td>0.74946</td><td></td><td></td><td></td></tr><tr><td>7.</td><td>User Commitment to the Project</td><td></td><td>0.56848</td><td></td><td></td><td></td><td></td></tr><tr><td>8.</td><td>Extent of User Use of the System</td><td></td><td>0.63688</td><td></td><td></td><td></td><td></td></tr><tr><td>9.</td><td>Satisfaction with the Development Approach</td><td></td><td>0.71772</td><td></td><td></td><td></td><td></td></tr><tr><td>10.</td><td>Overall Quality of Development Effort</td><td>0.51591</td><td>0.63272</td><td></td><td></td><td></td><td></td></tr><tr><td>11.</td><td>Ability to Conceptualize the System</td><td>0.67137</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>12.</td><td>Ease of Project Management and Control</td><td>0.76415</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>13.</td><td>Project Completed on Schedule</td><td>0.90006</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>14.</td><td>Project Completed in Projected Person-Days</td><td>0.80430</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15.</td><td>Project Completed within Budget</td><td>0.75175</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>16.</td><td>Ease of System Planning</td><td>0.73662</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>17.</td><td>Flexibility of the Approach</td><td></td><td>0.87968</td><td></td><td></td><td></td><td></td></tr><tr><td>18.</td><td>Requirements (Time, Money, Effort, etc.)</td><td></td><td></td><td></td><td></td><td>0.71560</td><td></td></tr><tr><td>19.</td><td>Validation of User Requirements</td><td></td><td>0.73692</td><td></td><td></td><td></td><td></td></tr><tr><td>20.</td><td>Implementation and User Acceptance</td><td></td><td>0.62791</td><td></td><td></td><td></td><td></td></tr><tr><td>21.</td><td>User Satisfaction with the System</td><td></td><td></td><td></td><td>0.54828</td><td></td><td></td></tr><tr><td>22.</td><td>System Maintenance Requirements</td><td></td><td></td><td></td><td>0.79594</td><td></td><td></td></tr><tr><td>23.</td><td>Acquisition of Expensive Software</td><td></td><td></td><td></td><td></td><td>0.69238</td><td></td></tr><tr><td>24.</td><td>System Testing</td><td>0.52910</td><td>0.55084</td><td></td><td></td><td></td><td></td></tr></table>

Appendix D
Factor Analysis of User Responses

<table><tr><td rowspan="2">No.</td><td rowspan="2">Item</td><td colspan="6">Factor Loadings</td></tr><tr><td>User Contribution</td><td>Satisfaction With Outputs</td><td>Project Management</td><td>Impact On Decision Effectiveness</td><td>Quality Of System Results</td><td>Effect On Decision Making</td></tr><tr><td>1.</td><td>Effect on Complexity of Decision-Making</td><td></td><td></td><td></td><td></td><td></td><td>0.56183</td></tr><tr><td>2.</td><td>Quality of System Results</td><td></td><td></td><td></td><td></td><td>0.73461</td><td></td></tr><tr><td>3.</td><td>Confidence in Decisions</td><td>0.54419</td><td></td><td></td><td>0.57857</td><td></td><td></td></tr><tr><td>4.</td><td>Range of Decision-Making Capabilities</td><td></td><td></td><td></td><td>0.90172</td><td></td><td></td></tr><tr><td>5.</td><td>Cost and Effort of Decision-Making</td><td></td><td></td><td></td><td></td><td></td><td>0.81946</td></tr><tr><td>6.</td><td>System Flexibility</td><td>0.63216</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7.</td><td>User Satisfaction with the System</td><td></td><td>0.52420</td><td></td><td>0.51228</td><td></td><td></td></tr><tr><td>8.</td><td>Project Completed within Budget</td><td></td><td></td><td>0.85208</td><td></td><td></td><td></td></tr><tr><td>9.</td><td>Project Completed within Project Person-Days</td><td></td><td></td><td>0.86404</td><td></td><td></td><td></td></tr><tr><td>10.</td><td>Project Completed on Schedule</td><td></td><td></td><td>0.83621</td><td></td><td></td><td></td></tr><tr><td>11.</td><td>Acquisition of Expensive Software</td><td></td><td>0.50000</td><td></td><td></td><td></td><td></td></tr><tr><td>12.</td><td>Time from Request to System Completion</td><td>0.70679</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>13.</td><td>Timeliness of System Output Information</td><td></td><td>0.72633</td><td></td><td></td><td></td><td></td></tr><tr><td>14.</td><td>Communication with the DP/MIS Staff</td><td>0.83765</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15.</td><td>Ability to Produce Output</td><td></td><td>0.83306</td><td></td><td></td><td></td><td></td></tr><tr><td>16.</td><td>Estimation of Decision-Making Variables</td><td></td><td></td><td></td><td></td><td>-0.57693</td><td></td></tr><tr><td>17.</td><td>Accuracy of System Output</td><td></td><td>0.62846</td><td></td><td></td><td></td><td></td></tr><tr><td>18.</td><td>Reliability of Output Information</td><td></td><td>0.59501</td><td></td><td></td><td></td><td></td></tr><tr><td>19.</td><td>Convenience of Access to the System</td><td></td><td></td><td></td><td>0.50914</td><td></td><td></td></tr><tr><td>20.</td><td>User Feeling of Control of the Project</td><td>0.83921</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>21.</td><td>Relationship with the DP/MIS Staff</td><td>0.84367</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>22.</td><td>User Feelings of Participation in Project</td><td>0.73352</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>23.</td><td>User Understanding of the System</td><td>0.70464</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>24.</td><td>Relevance of Output to Intended Function</td><td>0.56652</td><td></td><td></td><td></td><td></td><td></td></tr></table>
