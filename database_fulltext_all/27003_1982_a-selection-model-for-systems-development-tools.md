---
otero_id: 27003
otero_key: "X4BYUVXW"
title: "A Selection Model for Systems Development Tools"
authors: "Justus D. Naumann; Shailendra Palvia"
year: "1982"
journal: "MIS Quarterly"
doi: "10.2307/248753"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
A Selection Model for Systems Development Tools
Author(s): Justus D. Naumann and Shailendra Palvia
Source: MIS Quarterly, Vol. 6, No. 1 (Mar., 1982), pp. 39-48
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/248753
Accessed: 13-01-2016 12:23 UTC

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# A Selection Model for Systems Development Tools

By: Justus D. Naumann
Shailendra Palvia

## Abstract

Selecting from the many currently available systems development methodologies (SDMs) and development techniques is a difficult problem with economic, technical, and behavioral implications. A quantitative approach to the selection problem is presented.

The selection model begins with a definition of a superset of functions expected of a systems development tool. Functions are then weighted, using a Delphi approach to achieve acceptable valuations among system managers. Next, each approach under consideration is evaluated with respect to each function desired. After scores are computed for each methodology, economic and qualitative aspects such as training availability and cost can be used to differentiate the highest ranked alternatives.

A four-person MBA project team from the Graduate School of Management at the University of Minnesota, with the guidance from the authors, applied the model to a methodology selection problem. In addition to producing a quantitative ranking of competing methodologies, the approach described furthered understanding of the functions to be performed by the methodologies being considered. It also gained acceptance, admittedly reluctant, of the recommended methodology from managers who strongly advocated their own favorites.

Keywords: Management, systems development, standards, methodology, SDM

ACM Categories: 2.43, 8.3

## Introduction

To develop and implement Information Decision Support Systems efficiently, several structured and disciplined methodologies and techniques of system development have been developed and promoted. These system development tools generally attempt to deal with complexity through a procedural approach, with clear definitions of deliverable products and formal controls over personnel, time, budget, and other resources. Not surprisingly, most of these work. Vendors and users can cite cases where use of a methodology (SPECTRUM, PRIDE, SDM-70, CARA) or a technique (HIPO, Warnier/Orr, Jackson) has resulted in the production of reliable and efficient systems on schedule and budget.

The IS Manager is typically faced with the challenge of selecting and implementing a package of methodologies and techniques to suit the organization. Selection and implementation of a package impacts standards, training, documentation, communication with users, and communication among DP professionals. Most importantly, the implementation of new methodologies and techniques impacts the work procedures and work styles of people.

Selection from among competing methodologies and techniques is not easy since:

\- people involved in the decision making process have different perceptions of needs,

\- people are naturally biased toward the approach they are used to, and

• each alternative under consideration meets certain perceived needs.

Under such circumstances, the subjective views, based on personal experiences and biases, of influential people in the organization become the most important selection criteria. Ideally, when a new package of system development methodologies and techniques is to be selected, a committed consensus will assure effective implementation and use. To meet this goal, participation of key persons in a well-defined and objective decision making process is a lot better than the “like it or leave it” method or the “thou shalt” method. Such an objective method is described in the next section, and an application of the model is presented in the third section.

## The Model

The problem statement, for which an objective model is developed, can be stated as follows:

Feasible alternatives (system development techniques) exist to meet a given set of system development objectives. Each feasible alternative has at least one sponsor and several advocates. Only one of the feasible alternatives can be selected for ongoing use as a standard. There is considerable disagreement over the pros and cons of each feasible alternative.

In many organizations, interminable, heated arguments often ensue between the advocates of each alternative. Either no decision is taken or alternatives are tried in a hit-and-miss mode to the benefit of none.

The model consists of two parts — quantitative evaluation and qualitative evaluation. Most criteria can be objectively evaluated and are included in the quantitative model. The highest rated alternatives resulting from quantitative evaluation may be compared further in the qualitative model.

## Quantitative evaluation

Figure 1 shows the process of evaluation that makes up the quantitative model discussed here in detail.

1. Identifying Functions (Objectives) of the Applicable Life Cycle Phase: A list of functions can be generated by a literature survey, by inspecting actual system development documents and by interviewing both writers and recipients of system development documentation. The product of this step is simply a list of the functions needed. No evaluation should be attempted — the objective of this stage is to produce an exhaustive list.

2. Weighing Functions: The Delphi technique [7, 9] is used to arrive at weights of functions. In this method,

a. The list of functions is circulated to a group of evaluators.

b. Each evaluator assigns a weight to each function on the basis of importance using an arbitrary numeric scale (say 1-10).

c. A coordinator tabulates the results to show the mean weights, the range of weights, and the standard deviation of weights for each function.

d. The list of functions is recirculated to the evaluators along with the tabulated results of the previous weights. Evaluators are asked to work toward consensus while maintaining their personal values.

e. Each evaluator reviews the results and reassigns weights to functions. Any change away from the mean, as compared to the previous weight, has to be justified in terms of brief comments.

f. Steps 3 through 5 are repeated until the weights stabilize (little or no change in mean, range, and standard deviation). A high standard deviation may reflect disagreements due to differing interpretation (brief comments from step 5 will provide a clue to this).

The major advantage of the Delphi technique is that it is impersonal and objective. It prevents confrontation between group members and thus eliminates the negative aspects of individual dominance.

The final set of weights represents a group opinion of the relative importance of the functions to be performed by the alternatives under consideration.

3. Developing Criteria to Evaluate Functions: A list of evaluation criteria can be generated for each function by doing a literature survey and by interviewing writers and recipients of documentation. Criteria can be different for different functions. For example, “specifying logic” is a function of program design specs and the evaluation criteria for this function may be:

![](/api/attachments/X4BYUVXW/fulltext/images/8e25603f2543ba96ca2f75d38be97be6e0ed88867a871639fbb71e126986a0e9.jpg)

Weighted functions developed using the “Delphi Technique” are used to evaluate alternatives based on scores for each function. Qualitative factors are applied after the Quantitative evaluation.

Figure 1. Selection Model

\- ease of understandability,

\- ease of transforming into computer code, and

\- ease of checking for completeness.

4. Assigning Values to Each Criterion: One could choose binary (0-1) or multiple values for a criterion, e.g., yes, definitely; yes, to a large extent; yes, to some extent; yes, to a negligible extent; or no, not at all; with corresponding numerical values of 4, 3, 2, 1, or 0.

5. Relating Each Technique: Each technique must then be evaluated on the basis of the specified evaluation criteria for each function. To obtain the rating for each criterion within each function for each competing technique, individuals participating in the study complete the rating questionnaire. These individuals should have knowledge in the use of the technique but can be biased for or against any of the alternatives under consideration.

6. Calculating Total Score: A total score can now be calculated from the criterion ratings and the function weights:

\- Let the functions be denoted by “i” where $i = 1,2,\ldots n$ .

\- Let the function-weights be denoted by $W_{i}$ .

\- Let there be “m” criteria within each function, i.e., j = 1, 2, ...m for each i.

\- Let $S_{ij}$ represent the rating of “j”th criterion within the “i”th function.

Now $S_{i}$ = Score for Function “i” = $\sum_{j=1}^{m} S_{ij}$

The Total Score (TS) for a technique is given by:

$$
T S = \sum_ {i = 1} ^ {n} W _ {i} S _ {i} = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {m} W _ {i} S _ {i j}
$$

## Qualitative evaluation

It would be nice to say that the alternative with the highest quantitative score wins. But certain subjective criteria also need to be considered, for example:

• strength of the package vendor,

• quality of available training, and

\- likelihood of the alternative becoming a dead end.

When two alternatives are close on the basis of the quantitative evaluation, a limited qualitative evaluation may aid in making the final choice. Qualitative evaluation typically emphasizes aspects related to overall system development rather than to a particular phase.

Finally, acquisition costs must be considered. The authors consider acquisition, and training and operation, cost considerations to be separable from the quantitative model. After alternatives have been quantitatively and qualitatively evaluated, relative costs of the high scoring alternatives will certainly influence selection.

## An Example

The model was developed and implemented for a real problem situation at Hennepin County Data Processing (HCDP) by a team of four graduate students from the MBA program of the University of Minnesota. $^{1}$ The focus of the problem was on the program-design phase, i.e., communication from the analyst to the programmer. The objective was to compare four techniques: HIPO (Hierarchy Input Processing Output), “13-point Technique” (an inhouse approach involving the use of decision tables and edit-move matrices), the Warnier/Orr technique, and the Chapin-Chart technique. Each technique had sponsors and advocates in a DP organization of 200 people with an annual budget of 6 million.

## Quantitative evaluation

1. Identifying Functions: The team defined functions to be the information to be communicated by the analyst, in Program Specifications, to enable the programmer to do the job of designing, coding, and testing effectively. On the basis of a literature survey and interviews with data processing professionals (writers and recipients of documentation), the following 15 functions (i=1,2...15) were identified:

a. Program objectives — a general description or abstract of what the program should do, including a problem statement.

b. System overview — presentation of an overall view of the system, usually by means of a hierarchical chart or system flowchart that shows the relationship of a program to all other programs in the system.

c. Inputs/Outputs — sets of data entered as input to a program, or sets of data produced by a program, such as a report. The data should be described as to content, organization, and format.

d. Data structure — for database files, a description of the organization of the data, usually in a hierarchical format.

e. File descriptions — descriptions of record layouts used by the program, including content, organization and sequence, access method, and file security, if applicable.

f. Edit criteria — information to insure input is edited properly. This includes standard criteria for the entire system as well as any specific criteria for the particular program.

g. Error procedures — description of error messages and the action to be taken when error conditions occur.

h. Control breaks — used in report programs to indicate a change in processing; for example, batch totals and new page headings.

i. Defined modules — separate modules within a program indicating specific functions; usually arrived at through a functional decomposition.

j. Interface between modules — the relationship between program modules. For example, one may be a subset of another, or two modules may be mutually exclusive.

k. External interface — description of the job control language used by a program.

I. Program logic — tables, graphs, or narrative, which communicate enough detail for the programmer to create and construct the proper logic to build the program.

m. Controls — concerned with monitoring accuracy of processing and ensuring that no data is lost or mishandled during processing; e.g., batch totals and audit trails.

n. History of change — chronological description of revisions made to a program.

o. Program test criteria — description of test objectives for unit testing a program.

2. Ranking Functions: The team initially believed that all functions were equally important. However, based on discussions with analysts and programmers, the team decided to assign weights to the functions using the Delphi technique. A group of seven data processing personnel with extensive backgrounds in system development was selected to participate in the weighting process. Weighting was done on a scale of 1 (unimportant) to 10 (very important). Composite results of two iterations of weight-assignment are shown as follows in Table 1. Weights are based upon results of the second Delphi iteration and are shown as percentages. (Only two Delphi iterations were carried out because of the limited time available for the student project.)

The individual weights of functions varied widely. The least agreement was on External Interface Definition, which ranged from 1 to 10 with a standard deviation of 2.9. Overall, weights ranged from 4 to 9. The Input/Output and the Program Logic functions received the highest weight of 9. At the other extreme, Defined Interface Between Modules received the lowest weight of 4, closely followed by History of Changes with a weight of 5.

Table 1 shows how the Delphi-technique helps in arriving at a consensus (standard deviation has decreased for almost all functions from the first iteration to the second iteration). It forces the par-

Table 1. Delphi Process Results

<table><tr><td rowspan="2">(i)</td><td rowspan="2">Functions Description</td><td colspan="3">Weights First Iteration</td><td colspan="3">Weights Second Iteration</td><td rowspan="2">Rounded Percentage Weights (Wi)</td></tr><tr><td>Mean</td><td>Range</td><td>Standard Deviation.</td><td>Mean</td><td>Range</td><td>Standard Deviation</td></tr><tr><td>1.</td><td>Program Objectives</td><td>7.7</td><td>3-10</td><td>2.7</td><td>7.3</td><td>6-10</td><td>2.2</td><td>7</td></tr><tr><td>2.</td><td>System Overview</td><td>5.3</td><td>1-7</td><td>2.5</td><td>5.1</td><td>1-7</td><td>2.1</td><td>5</td></tr><tr><td>3.</td><td>Input/Output</td><td>8.7</td><td>7-10</td><td>1.1</td><td>9.0</td><td>8-10</td><td>0.8</td><td>9</td></tr><tr><td>4.</td><td>Data Structure</td><td>6.1</td><td>3-8</td><td>1.9</td><td>6.7</td><td>6-8</td><td>0.9</td><td>6</td></tr><tr><td>5.</td><td>File Descriptions</td><td>8.0</td><td>6-10</td><td>1.6</td><td>8.0</td><td>7-9</td><td>0.8</td><td>7</td></tr><tr><td>6.</td><td>Edit Criteria</td><td>8.9</td><td>6-10</td><td>1.4</td><td>8.7</td><td>6-10</td><td>1.3</td><td>8</td></tr><tr><td>7.</td><td>Error Procedures</td><td>7.7</td><td>4-10</td><td>2.1</td><td>8.1</td><td>7-10</td><td>1.2</td><td>8</td></tr><tr><td>8.</td><td>Control Breaks</td><td>7.7</td><td>4-10</td><td>1.9</td><td>7.7</td><td>1-10</td><td>1.4</td><td>7</td></tr><tr><td>9.</td><td>Defined Modules</td><td>5.7</td><td>2-10</td><td>2.6</td><td>5.4</td><td>1-10</td><td>2.3</td><td>5</td></tr><tr><td>10.</td><td>Defined Interface Between Modules</td><td>6.0</td><td>2-10</td><td>2.3</td><td>4.7</td><td>1-9</td><td>1.7</td><td>4</td></tr><tr><td>11.</td><td>External Interface</td><td>6.3</td><td>3-10</td><td>2.6</td><td>6.1</td><td>1-10</td><td>2.9</td><td>6</td></tr><tr><td>12.</td><td>Program Logic</td><td>9.3</td><td>7-10</td><td>1.1</td><td>9.4</td><td>7-10</td><td>1.0</td><td>9</td></tr><tr><td>13.</td><td>Control Procedures</td><td>7.4</td><td>2-10</td><td>2.6</td><td>7.3</td><td>4-10</td><td>1.8</td><td>7</td></tr><tr><td>14.</td><td>Historic Record of Changes</td><td>5.6</td><td>1-9</td><td>2.7</td><td>5.1</td><td>2-9</td><td>2.4</td><td>5</td></tr><tr><td>15.</td><td>Program Test Criteria</td><td>7.3</td><td>3-10</td><td>2.3</td><td>7.4</td><td>4-10</td><td>1.8</td><td>7</td></tr></table>

Each function was weighted on a scale of 1-10 by the managers and analysts involved. In the second Delphi iteration, the summary was distributed. The results of the second iteration were converted to percentage weights to objectively evaluate functions.

participants to objectively reevaluate their previous weights, so that they can move toward the mean. In a subtle way, peer pressure motivates the participants toward agreement.

3. Developing Criteria to Evaluate Functions: In order to determine if each function was provided by the alternatives under consideration, objective and measureable criteria were established. The questions listed below are the criteria (j = 1, 2, 3) for each function i.

1) Does the technique include or allow the function? (j = 1)

2) Is the function required by the technique? $(j = 2)$

3) Does the technique tell how to perform the function? (j = 3)

## 4. Assigning Values to Each Criterion:

a. If the technique provides a means for communicating the required information, the answer would be yes for criterion 1, otherwise no.

b. If the system analyst is required to include the specific function, the answer would be yes, otherwise no for criterion 2. The significance of this question is to avoid giving the analyst the option of deciding what information should be passed along to the programmer.

c. If there are steps or instructions available to aid the analyst in conveying the needed information, the answer would be yes, otherwise no for criterion 3.

5. Rating each Technique: For each of the four competing approaches/techniques, rating was done for each criterion within each function. A rating of a yes meant a score of "1" and a no meant a score of "0." The student team interviewed the advocates of the technique concerned to rate the four alternatives being considered. Ratings were based on the documentation provided for each technique and the accumulated experience of interviewed subjects.

6. Calculating Total Score for each Technique: To score, for Technique "k" (where k = 1, 2, 3, or 4)

$S_{ki} = \text{Score for function "i" for technique "k" }$

$$
= \sum_ {j = 1} ^ {3} S _ {k i j}, \quad S _ {k i j} = \begin{array}{l} \text { Score   for   criterion } \\ \text {"j" within function} \\ \text {"i" for technique "k"} \end{array}
$$

and $S_{k} =$ Overall score for approach "k"

$$
= \sum_ {i = 1} ^ {1 5} W _ {i} S _ {k i} = \sum_ {i = 1} ^ {1 5} \sum_ {j = 1} ^ {3} S _ {k i j} W _ {i}
$$

The results were as follows:

$$
\begin{array}{r l} S _ {1} & = \text { Overall   score   for   Augmented } ^ {2} \text { technique } \\ & \quad \text { “A” } = 2 8 8 \text { points } \end{array}
$$

$S_{2}$ = Overall score for Unaugmented $^{2}$ technique “B” = 225 points

$S_{3}$ = Overall score for technique “C” = 208 points

$S_{4}$ = Overall score for technique “D” = 149 points

## 7. Analysis of the Results:

\- The weights developed for the fifteen documentation functions were as expected. Input/output requirements and program logic, which are fundamental in program design, received the highest weights. The functions of defining interfaces between modules and of providing a history of changes are clearly supplemental, and received lower weights.

\- The large “standard deviation” in some of the individual weights was unexpected. Since the standard deviation failed to decrease substantially from the first to the second iteration, it is obvious that group members had strong and varied convictions about “which functions a program design technique should perform.” A positive correlation between the weights and the technique used by the weighter was observed in several instances, i.e., low weights appeared to correspond to functions that were not performed by the technique used. This bias did not significantly affect the final scores.

\- It is misleading to compare the competing techniques directly. Two of the four techniques were in active use in the organization and were, therefore, augmented with special shop practices and standards. This gave techniques "A" and "C" a distinct advantage over techniques "B" and "D." This advantage might be partly reflected in the extra time, effort, and cost that would be necessary to augment the new techniques with shop practices and approaches and implement later. Technique "B" could be modified by adding shop standards for program objectives, external interface definitions, and test criteria, similar to those developed for and in use with technique "A." The resulting augmented technique "B" would have the highest score of 295.

\- Function ratings for a particular technique were obtained by interviewing advocates of that technique. This naturally introduced an upward bias for each technique. The extent of this upward bias might have been different for different techniques.

## Qualitative evaluation

The qualitative evaluation focused on the two most promising techniques — “A” and “B.” In this study, qualitative factors represented the particular needs and goals of HCDP. Four factors seemed important but difficult to evaluate quantitatively: maintainability, teachability, efficiency, and suitability to automation.

1. Maintainability: The question was, "Can the documentation produced from the technique be easily and adequately maintained?" If it cannot be updated, it will always be out of date. The factors considered in evaluating maintainability included the extent to which the documentation has to be revised when a change occurs, and how easy it is to spot where the change needs to be made.

Both techniques have the capability of being adequately maintained; however, differing amounts of effort are required. For simple changes each technique would require only one chart or one page to be modified. Since "A" and "B" included diagrams that related closely to the program structure, changes are generally easier to spot. Technique "A" tends to need extensive modification in the documentation to incorporate a change in specifications. This could prove to be both a time consuming and costly operation. Overall, technique "B" documentation was considered generally more succinct, so reviews and revisions were expected to be less time consuming.

2. Teachability: This issue prompted the question, "What is required to train the staff in the technique if it were implemented as standard?" Important points to consider are the resources (instruction material, personnel, and costs) available to train staff, and the intrinsic aspects of a technique which make it easy or difficult to learn.

There are various aids available for training analysts and programmers in each of the techniques. Technique "A" is supported by its vendor, who has prepared a manual describing its use. Besides this manual, the County also has a video course on technique "A" and its own instructional reference manual. Technique "B" is supported by its vendor, with a 4-day on-site seminar available. Also, 4-day public courses are offered periodically by the vendor at various locations in the country. There is a book available describing the technique and HCDP has a video course on the technique. The number of HCDP employees already familiar with technique "A" was 19 versus only two with technique "B." In that sense, learning and accepting technique "B" would cause more organizational upheaval than technique "A."

3. Efficiency: The question was, "Is the technique an efficient tool in terms of accuracy, completeness, and consistency for both the analyst and programmer to use?"

The aspects of accuracy and completeness for each of these techniques depend on the checking procedures, i.e., walkthrough reviews. Since completeness is independent of the technique, the distinction was made on the readability of the diagrams. Technique "A" communicates the logic of program segments fairly well but its charts do poorly at defining intermodular relationships. Diagrams of technique "B" appeared to be the most easily read and understood; they include chronological sequencing and hierarchy, and therefore appear to be quite useful for communication.

Consistency can be thought of as achieving a single graphic documentation mode. Technique "A" provides consistency through the entire project cycle, but uses several types of diagrams to express different things. Technique "B" uses only one type of diagram throughout to convey the overall views, detail specifications, and data structure. Because of the emphasis on the sequence of events, technique "B" has the most consistent documentation.

4 Suitability for automation: "What automation software is available and/or what efforts are currently being made in this direction for each technique?" A software package should facilitate development and maintenance of documentation. Suitability to automation is an important consideration for future use of the technique. Packages are available for automating technique "A" but have not been widely used. Some automation techniques are being used by some of technique "B" users.

## Project results

The project team's recommendation was to select either technique "A" or "B" as a standard, subject to a similar evaluation of the needs of other phases in system development.

A follow-up study by the County's Standards Group showed that for other phases, technique "B" seemed superior in the important qualitative aspects of efficiency and ease of automation. An informal survey of those who had sponsored the techniques "C" and "D" favored "B" over "A." Others, initially unbiased, also seemed to tilt in favor of technique "B." At the time of this writing, however, a final decision has not yet been made to have either technique "A" or "B" as a standard.

However, technique “B” was adopted for the largest current project (requiring 200 person-years of effort). Two of the five project groups have adopted technique “B” for most of their program design documentation. One person has attended a workshop on the technique “B” and two persons have attended a “Technique ‘B’ Users’ Conference,” both organized by the vendor. The decision to standardize on technique “B” is imminent.

## Conclusions

The model we have presented helps structure a difficult and often emotion-laden decision. The example used is just one of many such decisions faced by information systems organizations and managers. The required definition of the functions to be performed at a given point in systems development is a useful exercise in and of itself. The use of precise evaluation criteria that separate the objective test for the presence or absence of a function from the judgment stage permits agreement on the claims for each alternative. The Delphi approach to weighting each function adds objectivity and promotes mutual understanding of the functions of systems development methodologies and techniques. While the model includes a more subjective, or qualitative phase, many of the issues have been resolved and some alternatives eliminated before that stage is reached. The choice of qualitative factors is of course subjective. If a particular factor seems both important and controversial it may be possible to convert it into a function and add it to the quantitative evaluation.

A final feature of this decision model is worth consideration: its behavioral implications. There is no limit on the number of people who contribute to the definition of functions and their weights. Programmers and analysts as well as supervisors and managers can participate in the decision process through the Delphi weighting approach. Not only do they add their judgments, they compare their own opinions with their peers, subordinates, and supervisors. As our case study shows, such participation is a powerful force toward consensus even when a decision is not immediately forthcoming.

## Bibliography

[1] Bryant J., Kacker, R., Schultheis, M., and Weisbecker, J. "Evaluation of Program Design Techniques," unpublished MBA Field Project Report 8-159, School of Management, University of Minnesota, Minneapolis, Minnesota, June 1979.

[2] Canning Publications. "How to Use Decision Tables," EDP Analyzer, May 1966.

[3] Canning Publications. "The Production of Better Software," EDP Analyzer, February 1979.

[4] Canning Publications. "Program Design Techniques," EDP Analyzer, March 1979.

[5] Etter. “Prudential Algebra,” Decision Sciences, January 1974, pp. 145-147.

[6] Fergus, R. "Decision Tables — What, Why, How," Systems Analysis Techniques, Couger, D. and Knapp, R., eds., John Wiley & Sons, New York, New York, 1974, pp. 162-179.

[7] Helmer, O. "Systematic Use of Expert Opinions," Clearing House for Federal, Scientific and Technical Information, AD-662320, November 1967.

[8] Jones, M.N. "HIPO for Developing Specifications," Datamation, March 1976, pp. 112-125.

[9] Linstone, H.A. and Turoff, M. The Delphi Approach: Techniques and Applications, Addison-Wesley, Reading, Massachusetts, 1975.

[10] Stevens, B.M. "Structured Techniques: Comparative Analysis," unpublished, available from Langston & Kitch Associates,

715 East 8th Street, Topeka, Kansas 66607.

[11] Yourdon, E. "Chapin Charts," EDP In-Depth Reports, December 1977, pp. 4-11.

## About the Authors

Justus D. Naumann, Ph.D., is Assistant Professor of MIS at the University of Minnesota. He has been in the computer industry for 25 years, holding technical and managerial positions in hardware and software design, marketing, and systems analysis, and design. He is currently conducting research in information systems development, software engineering, and management of systems development. Professor Naumann holds a BA degree, plus MS and Ph.D. degrees in MIS from the University of Minnesota. He is a member of ACM, AIDS, IEEE, SMIS, and TIMS.

Shailendra Palvia is Management Support Analyst with the Federal Reserve Bank of Minneapolis. He is also a Ph.D. Candidate in Quantitative Analysis and MIS at the University of Minnesota, where his research interests include use of quantitative methods and understanding implementation problems with special emphasis on resistance to change. Mr. Palvia has eleven years of experience as a programmer, analyst, and administrator with IBM, Control Data, Hen-nepin County, and now with Federal Reserve Bank. He holds a B.S. (Chem. Engrg.) from ITT, New Delhi (India), and an MBA (MIS Specialist) from the University of Minnesota.
