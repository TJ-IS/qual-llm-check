---
otero_id: 18391
otero_key: "JR7P985T"
title: "A study of the effects of three commonly used software engineering strategies on software enhancement productivity"
authors: "Robert P. Cerveny; Daniel A. Joseph"
year: "1988"
journal: "Information & Management"
doi: "10.1016/0378-7206(88)90012-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Study of the Effects of Three Commonly Used Software Engineering Strategies on Software Enhancement Productivity \*

Robert P. Cerveny

State University of New York at Buffalo, School of Management, Jacobs Management Center, Buffalo, NY 14260, USA

Daniel A. Joseph

Rochester Institute of Technology, College of Business, 1 Lomb Memorial Drive, Rochester, NY 14623-0887, USA

The results of a study of software enhancement projects involving identical information requirements are reported. A sample drawn from the 200 largest commercial banks in the United States was examined to determine the levels of programming, systems analysis, and project management effort necessary to implement interest reporting requirements of the U.S. Tax Equity and Fiscal Responsibility Act (TEFRA) of 1982. Results of the study indicate that firms using structured systems design and programming techniques expended twice as much effort to implement the TEFRA requirements as those using non-structured approaches. It was also found that firms purchasing software expended nearly the same amount of effort as those using traditional systems analysis and programming techniques.

Keywords: Bank regulation, Banking software, Productivity, Software engineering, Software enhancement, Software maintenance, Structured analysis, Structured programming, Taxation, TEFRA.

## 1. Introduction

Human resources account for a substantial portion of the expenses associated with computer-based information systems. Software development, enhancement and maintenance are especially labor intensive portions of these expenses. A variety of software engineering strategies have been deployed to help minimize these expenditures in projects involving internally developed software. The degrees of formalization involved in these

![](/api/attachments/JR7P985T/fulltext/images/81161be402088476204afe076f3c0b3d601183a510a6a0519aba699ed1987d77.jpg)

Robert P. Cerveny is an Associate Professor of Management Science and Systems in the School of Management, State University of New York at Buffalo, where he is the director of MIS programs and the Chair of the Institute for Computing and Computer Applications. He holds a Ph.D. degree from the University of Texas at Austin. He is the author of over 25 papers in the information systems area. His current research interests include information systems implementation issues and requirements analysis, especially as applied in the health care sector. He is a member of the Decision Sciences Institute, The Institute for Management Science, and the Society for Information Management.

![](/api/attachments/JR7P985T/fulltext/images/d6ac13df3f8aa6e915507938d5abb967f8edfddcb3cfec60ccfe0b095a78b7d1.jpg)

Daniel A. Joseph is an Assistant Professor of Information Systems in the College of Business at Rochester Institute of Technology. He holds a Ph.D. degree in MIS from the State University of New York (SUNY) at Buffalo as well as Master's degrees in Business Administration and Economics from SUNY at Buffalo and SUNY at Albany, respectively. He has worked as a system analyst and systems development team leader in the insurance and banking industries and as a fiscal analyst for the Wisconsin State Legislature. His current research interests include productivity issues relating to systems analysis, decision support, and knowledge-based applications. He is a member of the Decision Science Institute and the Association for Computing Machinery.

strategies range from relatively informal (unstructured) to highly structured. In contrast, some organizations purchase software from outside vendors rather than rely on internal development. The implications of these strategies on the software development/modification process do not appear to be well understood. As a result, organizations base their decisions to adopt alternative strategies on their faith in claims made by advocates rather than on clear understandings of the costs and benefits.

A fortuitous opportunity to investigate the software development process arose with passage of the Tax Equity and Fiscal Responsibility Act (TEFRA), of 1982, in the U.S.A. The act required banks to report interest and dividend income to the Internal Revenue Service of the U.S. Treasury Department. Compliance with the TEFRA required considerable modification of existing bank software. The forty-seven banks involved in the study described here reported they spent in excess of 160,000 hours of work effort implementing these changes.

The purpose of the study was to evaluate the implications of utilizing one of three commonly used approaches to systems development and design. The conclusions of the study suggests that the two most efficient strategies for implementing major enhancements to existing software systems are reliance on vendor developed software or in-house development using nonstructured techniques.

## 2. Issues and Claims

## 2.1. Non-Structured Techniques

Non-structured techniques were the first to be applied to the systems development process. They focus on the particulars of subsystems with subsequent attempts to address interface and integration issues [3]. These techniques require no special forms of documentation and do not require organized program code in any special or standard way. Some advantages of these techniques are: a minimal amount of planning is required; they apparently work well in situations where initial solutions to problems are small enough for one individual to solve them, and a minimal amount of project control is needed. Purported disadvantages include difficulty in coordinating the efforts of more than a small number of developers; prosaic system specifications and documentation [13]; convoluted solutions which get worse as systems evolve, and the generation of hard-to-maintain “spaghetti” code.

## 2.2. Structured Techniques

Structured techniques focus on a planned, well-documented, and systematic approach to systems development. When applied to systems analysis and design they involve the use of such tools as data flow diagrams, data dictionaries, program specifications written in “structured English”, decision tables, and decision trees. When applied to programming activities they include an avoidance of “Go To” statements, modular program development, and observance of program and design walkthroughs. They are used to varying degrees in Information System (IS) departments because they purportedly result in better requirements analysis and a better understanding of a system by users [16]; the development of more efficient, easier-to-maintain software when compared with non-structured techniques [22]; a reduced likelihood of programming and design errors [18]; improvements in programming productivity of up to 25%; and the development of better documentation [10,15,20].

There is, however, controversy over the effectiveness of structured tools. Edward Yourdon, a proponent of structured methods, recently reported that while many organizations have attempted to use structured software engineering techniques, they eventually abandoned them altogether. He notes that only about ten percent of the data processing departments in North America currently use structured techniques in a disciplined fashion. He cites three reasons for this state of affairs:

(1) people became frustrated with the amount of manual labor that was required to develop structured analysis models;

(2) people became frustrated with their inability to apply classical structured analysis to complex, real-time problems; and

(3) people were lured away from structured analysis by the promises of prototyping tools and fourth generation languages.

These reasons all involve productivity issues. It appears that most practitioners feel that structured techniques are counterproductive. One major disadvantage associated with using these techniques is that they appear to require more planning and design effort than do nonstructured approaches. The results of a recent survey of systems analysts and project managers at 36 firms highlights the significance of this disadvantage. Participants in the survey acknowledged the benefits of structured tools in requirements analysis and system design, but reported they were not using them. The reason; they were too time-consuming [16]. It has been argued that structured software development strategies require higher levels of initial effort, but that savings in subsequent modifications make their use worthwhile. Research places that claim in doubt.

## 2.3. Purchased Software

Purchased software represents an alternative to systems developed in-house. This variant is frequently followed because it is thought: the user can be certain software will operate correctly before it is purchased; vendor-developed software costs less than if it were developed in-house, because costs associated with its development and maintenance can be shared among the users of software; the purchase of software allows an organization to benefit from software development expertise that usually exceeds that of most organizations, and time is saved by the organization because there is no development work necessary [7].

The purported major disadvantages to using purchased software packages are that: purchase hampers the development of an in-house program design and implementation capability; serious problems can arise for the user of an application package if the vendor stops supporting the product; purchased software may need extensive custom modification to fit the needs of individual users, and the vendor is in control of the priority with which changes will be made to a particular package.

## 2.4. Empirical Research on Software Development Techniques

Research on the efficiency of strategies involving the use of vendor-developed software could not be found in the MIS literature. This was not surprising since it has been generally assumed that purchasing an application package from a vendor is less uncertain, less expensive, and less time consuming for a user than the in-house development alternative.

The results of a few studies on the efficiency of structured techniques have been reported but they have not been very conclusive. Much more has been written about the technique itself than about the accuracy of the claims of productivity improvement made about it [2]. Vessey and Weber have made the following points about this.

"Whereas conceptual developments in structured programming have been forthcoming, corresponding empirical developments have been slower... The acid test of a normative theory of programming must be whether or not the principles derived from the theory produce cost-effective changes in software practice..." [17].

Most of the research on structured techniques has involved experimental studies conducted under controlled conditions. The results of these studies have been equivocal. Almost all of the research on structured techniques reported to-date has used the ratio between lines of code written and hours of work effort to measure the productivity of the technique. For example, Walston and Felix [19] used this measure when they studied the results of 60 completed software development projects. Their findings suggested that both structured programming and top-down design improved productivity. Vessey and Weber [18] also used this measure in their study of 447 operational commercial and clerical COBOL programs used in three business organizations. Their focus was on the effect of structured techniques on maintenance activity. Over 90% of the software in the organizations they studied required two or fewer repairs, once it had been installed regardless of the development strategy used. This suggests the claim about structured techniques reducing the number of coding and logic errors in the software they are used to develop will not provide sufficient justification for their use.

Survey research methods have also been applied in the area. Some of this research has indicated that managers in IS departments which use structured techniques think they contribute to better quality software and more productive effort in their organizations [8,9,12]. Nevertheless, the results of a survey of five hundred companies in twenty two industrial categories conducted by Lientz and Swanson in 1977 revealed little evidence to support these claims [11].

In summary, the results of most of the research on the efficiency of structured techniques have been either positive or equivocal. Most of the research reported above, however, focused on the development of new software. With the exception of the Lientz and Swanson study, little work appears to have been directed toward determining the effects of structured techniques on software maintenance/enhancement activities [1].

## 3. The Study

Our study evaluated the efficiency of three general strategies for implementing major enhancements to software. It focused on the work effort involved in implementing the TEFRA interest reporting requirements. These requirements were applied uniformly to all commercial banks and all banks were to implement the system on the same date. While the TEFRA required modifications to other systems as well, only projects involving changes to checking and savings account transaction processing systems were included in the study. Due to the significant levels of enhancement effort required in modifying the systems, the projects were usually implemented as stand-alones. This unusual implementation event provided a homogeneous study setting for measuring the effects of the three software development strategies.

## 3.1. Sample Population

Commercial banks constitute an excellent sample population for this study. Virtually all employ transaction processing systems which are implemented with unique software, but which perform similar functions and produce similar output: i.e., they employ equifinal systems [14]. This condition implies that similar levels of complexity exist across all the systems. In addition, since all the banks were required to meet identical changes in information requirements, it was possible to focus more clearly on the methods used to implement the changes.

There are about 14,000 commercial banks in the United States. The sample population for this study consisted of the 200 largest, measured according to their assets at the end of 1983. Since most smaller banks either contract their processing out to other banks or service bureaus or purchase transaction processing software and thus have little or no in-house development capabilities, larger banks were thought more appropriate for the study. All of the banks in the study were located in large population centers across the United States. There were no unusual concentrations in the geographic distribution of these centers. The value of assets at the banks included in this study ranged from 1.7 billion dollars to over 80 billion dollars; the sizes of their MIS staffs ranged from 3 to 400 employees.

Questionnaires were mailed to the banks in early 1984. They solicited information about TEFRA-related enhancement projects involving changes to checking and savings account transaction processing systems. Seventy-five of the two hundred banks contacted responded to one of two mailings, yielding forty-seven usable responses (23.5%). Unusable questionnaires included those which (1) reported effort for projects involving more than just the TEFRA enhancements; (2) contained too little information; (3) were returned by bank officials who did not wish to report their banks' work efforts but who wished to receive copies of the study results; or (4) reported their work effort in ways that made their data unusable for the study. There was no obvious systematic difference between responding and non-responding firms.

## 3.2. Overview of the Study

The independent variable evaluated in the study was the strategy used to integrate the substantial and identical TEFRA information requirements into the transaction processing software of the banks. The software strategy used to implement the TEFRA changes was determined by an evaluation of responses to questions about the techniques used.

The dependent measure used in the study was the effort expended to implement the TEFRA changes. This was measured in terms of the actual hours expended to implement the changes. Data for this was relatively easy to collect: Banks routinely keep track of project activity in terms of work effort, making it an unobtrusive measure [21]. Furthermore, since data about work effort was readily available to respondents, its use reduced the effort required to complete the questionnaire, thereby improving response rates.

An alternative measure, lines-of-code generated to implement the changes, could have been used instead of level-of-effort. This measure was used in much of the prior research reported here. Lines-of-code measures, however, focus on programmer productivity and ignore management and systems analysis effort. For this reason these measures are inappropriate for evaluating total software enhancement activity.

## 3.3. Results

The results of the study are based on the 47 usable returns. These indicated that the total support effort required to implement the TEFRA changes amounted to 164,969 hours of work effort. This included 25,137 hours of managerial time, 51,505 hours of analytic time, and 88,327 hours of programmer time. The total effort spent by all banks in the United States to implement the requirements must have been massive! The distribution of banks by software engineering strategies employed was: non-structured approaches 21% (10 banks), structured approaches 40% (19 banks), and reliance on vendor-developed software 39% (18 banks). The average levels of work effort for programming, system analysis and project management activities under the three strategies evaluated in the study are reported in Table 1.

This indicates that implementation of the changes took approximately twice as much effort when utilizing structured design strategies as either of the other techniques. This is significant at an alpha level of 0.02, using a t-test for unequal sample sizes. It also indicates that projects involving purchased software required similar amounts of total effort compared to those utilizing non-structured techniques. However, a breakdown of effort by category shows: (1) banks which purchased their software reported a significantly larger proportion of time spent on project management than banks using other methods; (2) projects involving purchased software strategies required a significant $^{14}$ smaller proportion of systems analysis time than those involving software developed in-house; (3) programming activity accounted for the largest proportion of project time, regardless of which strategy was followed. These results show that while the proportion of effort required for management, analysis, and programming is approximately the same for structured and non-structured strategies, the absolute level of effort in all categories was significantly higher using structured strategies. There was a slight, but not statistically significant, increase in the proportion of time spent in the programming phase for projects involving non-structured techniques. This last point is consistent with the literature, and, with the differences in magnitude of effort between the two approaches, would not appear to justify the use of structured techniques.

Categories of Average Work Effort Required for Modification of Each Type of Application Category (measured in hours of work effort)

<table><tr><td rowspan="2">TEFRA Project Activity</td><td colspan="3">Strategy Used to Implement the Change</td></tr><tr><td>Non-structured Techniques</td><td>Structured Design</td><td>Purchased Software</td></tr><tr><td>Programming</td><td>1,545 (57%)</td><td>2,830 (54%)</td><td>1,155 (51%)</td></tr><tr><td>Systems Analysis</td><td>874 (32%)</td><td>1,790 (34%)</td><td>544 (24%)</td></tr><tr><td>Project Management</td><td>300 (11%)</td><td>635 (12%)</td><td>563 (25%)</td></tr><tr><td>Total Effort</td><td>2,719 (100%)</td><td>5,255 (100%)</td><td>2,272 (100%)</td></tr></table>

Tables 2 through 5 examine additional parameters which aid in understanding the banks' selection of enhancement techniques. Table 2 presents the strategy used to develop and modify software by rank of bank. Table 3 presents this by asset size. Table 4 describes the methodologies used by IS department size. Table 5 shows the average number of employees required for each type of project activity under each of the three strategies evaluated in the study. The data in these tables indicate: (1) except for very large banks (assets greater than \$10 billion) there is not an absolute determinant of methodology employed; and (2)

Table 2  
Techniques Employed by Banks of Various Sizes (measured by total assets)

<table><tr><td rowspan="2">Ranking of Banks</td><td colspan="3">Technique Used to Make TEFR; Changes</td><td rowspan="2">Total Banks</td></tr><tr><td>Non-structured</td><td>Structured</td><td>Purchased</td></tr><tr><td>1–50</td><td>3</td><td>14</td><td>1</td><td>18</td></tr><tr><td>51–100</td><td>5</td><td>5</td><td>5</td><td>15</td></tr><tr><td>101–200</td><td>2</td><td>0</td><td>12</td><td>14</td></tr><tr><td>Totals</td><td>10</td><td>19</td><td>18</td><td>47</td></tr></table>

Table 5  
Techniques Employed by Banks of Various Sizes (measured by total assets)

<table><tr><td rowspan="2">Assets of Bank</td><td colspan="3">Technique Used to Make TEFRA Changes</td><td rowspan="2">Total Banks</td></tr><tr><td>Non-structured</td><td>Structured</td><td>Purchased</td></tr><tr><td>&gt; $10 bil</td><td>0</td><td>8</td><td>0</td><td>8</td></tr><tr><td>&lt; $10 bil</td><td>10</td><td>11</td><td>18</td><td>39</td></tr><tr><td>Totals</td><td>10</td><td>19</td><td>18</td><td>47</td></tr></table>

Techniques Employed by IS Departments of Various Sizes (measured by number IS employees)

<table><tr><td rowspan="2">Nun.ber of IS Employees</td><td colspan="3">Technique Used to Make TEFRA Changes</td><td rowspan="2">Total Banks</td></tr><tr><td>Non-structured</td><td>Structured</td><td>Purchased</td></tr><tr><td>&gt;100</td><td>1</td><td>8</td><td>1</td><td>10</td></tr><tr><td>51–100</td><td>5</td><td>9</td><td>4</td><td>18</td></tr><tr><td>1–50</td><td>4</td><td>2</td><td>13</td><td>19</td></tr><tr><td>Totals</td><td>10</td><td>19</td><td>18</td><td>47</td></tr></table>

Average Sizes of IS Departments Using Various Software Engineering Strategies (Portion of total staff accounted for by each category is indicated in parentheses)

<table><tr><td rowspan="2">Employee Category</td><td colspan="3">Strategy Used to Make TEFRA Changes</td></tr><tr><td>Non-structured</td><td>Structured</td><td>Purchased</td></tr><tr><td>Programmer or Trainee</td><td>4.6 (31%)</td><td>15.0 (20%)</td><td>4.6 (30%)</td></tr><tr><td>Systems Analyst or Programmer/ Analyst</td><td>8.2 (56%)</td><td>41.0 (54%)</td><td>9.1 (59%)</td></tr><tr><td>Project Manager</td><td>1.9 (13%)</td><td>20.0 (26%)</td><td>1.7 (11%)</td></tr><tr><td>Average Size of Staff</td><td>14.7 (100%)</td><td>76.0 (100%)</td><td>15.4 (100%)</td></tr></table>

the larger banks tended to use structured techniques, while the smaller ones purchased from external vendors.

One-half of the banks with systems supporting fewer than 500,000 accounts used purchased software for their checking and savings account processing. Larger banks (measured by number of accounts) used less vendor-developed software. Indeed, the data indicate that banks in the study sample with larger account bases tended to develop their software in-house and used more sophisticated (structured) approaches to software development than the smaller banks.

## 4. Disersion

The data indicate that structured techniques are certainly used by banks. But there is no support for the notion that structured techniques reduce software enhancement effort. In addition, even if there was a reduction in error rate or severity, there is little evidence that it resulted in sufficient reductions in test time to offset the large increase in total time required by the use of structured techniques. Why then do banks, and presumably others, use structured techniques? Reflections upon the patterns in our data lead us to the following observation: banks which use structured techniques tend to be large ones with many accounts, large contingents of data processing personnel, and large assets. They appear to use structured techniques for control reasons (see [5] for a discussion of this). Proponents of structured techniques have indicated that projects that use structured methods require more effort compared with projects where non-structured methods are used. They insist, however, that the additional effort is profitable, because it results in software that is easier to maintain. This was not the case for the TEFRA enhancements.

Table 1 indicates that, in absolute terms, banks using structured techniques required about twice as much overall effort to implement the TEFRA enhancements as banks relying on either of the other two strategies. This was the case for every category of work effort. It was most dramatic in programming and systems analysis activities, where structured techniques required twice as much effort as projects in which non-structured and purchased strategies were followed. An interesting finding was that projects using structured techniques required twice as much management effort as projects using non-structured methods. Management effort was nearly the same for projects using structured methods as for projects using "purchased software". Two surprising conclusions might be drawn. First, structured techniques are more labor intensive for software enhancement work compared to non-structured techniques. Second, projects involving purchased software required a total effort similar to that when using non-structured methods. Neither of these findings conform to popular conceptions of these strategies.

Why did projects involving structured techniques take so much more time than those where non-structured techniques were used? The answer is not evident from the data. However, a few comments can be made. Projects in an applications programming department involve three types of work: systems development, maintenance, and enhancement. Development effort consists of the design, construction and implementation of new software or the total revision of existing software. Maintenance work consists of routine modifications, such as updates to data tables, the correction of latent bugs, and modifications due to the installation of new hardware or new data access techniques. Enhancement projects involve the modification of existing software so that it will better perform new tasks or old ones. Structured techniques are known to require more time when used in systems development projects. The payoff in using such techniques is presumed to be that lower levels of effort are necessary in the maintenance or enhancement work. Enhancement projects are often considered to be similar to maintenance projects, because both involve existing software. But enhancement is different from maintenance because it involves the design of new procedures and features. In this respect, enhancement is more like systems development than maintenance. Since similar activity is required in both development and enhancement projects, it should not be surprising that more effort is required to implement enhancements to software using structured techniques.

Despite these findings, there may still be some benefits from using structured techniques. Structured documentation provides a standard, consistent basis for communicating systems design. It also appears to be more organized than the documentation produced when non-structured techniques are used. The labor-intensive aspects of current structured practice are certainly partially due to the maintenance of documentation. Computer Aided Software Engineering (CASE) tools that automatically update and maintain structured documentation are currently being introduced into the software development environment; these should help reduce the effort required to generate and maintain structured documentation. Reductions in maintenance costs of 20% and increases in productivity of 30% have been reported by the Hartford Insurance Group as a result of their use of CASE tools [4].

In addition, automatic code generators are being used by some firms to help eliminate or reduce programming effort in software development. A standard Structured Design Specification Language, based on current structured documentation conventions and independent of any particular programming language, could be used as the user interface in some code generation products. This might allow vendors to focus their attention on developing code generators with varying performance objectives without spending substantial time on the invention of a user interface language.

Table 1 also shows that projects involving purchased software required as much effort as ones involving non-structured in-house-developed software. This finding runs counter to popular thinking on the use of purchased software. There is little doubt that it is less expensive to purchase software from a vendor than to develop it using in-house staff. This has been suggested as a reason for the proliferation of personal computing technology [6]. A word of caution is in order, since this assumes the purchaser of the software will need to make few, if any changes. Such is not the case when large mainframe-based transaction processing applications are purchased. Users frequently purchase it and then build “hooks” so it will be simple to integrate it with other software. Then it is difficult to install upgrades of the purchased software. We did not consider such complex interfaces in our study, but we are confident that, to the extent these conditions were present in the surveyed banks, this explains the findings about the work effort. It is assumed that software in at least some of the banks studied has “hooks”. Further study is warranted.

The reader may be tempted to conclude from the data reported in Table 1 that “make-or-buy” decisions are now equivalent, because the enhancement projects in the study required as much effort when software was developed in-house as when it was purchased. Other factors, however, must be considered when the make-or-buy decision is made. These include:

(1) The cost of in-house systems development may exceed the cost of purchasing software by so much that it is still reasonable to purchase software in many cases.

(2) There is less risk associated with the purchase of new software than with the in-house development of it.

Table 1 also shows the distribution of effort required to implement the TEFRA changes under each of the three strategies. It shows that programming effort was proportionally twice the systems analysis effort for projects involving the modification of purchased software. It suggests that a larger portion of project management personnel will be required in banks that purchase software than in those that do not. In addition, fewer systems analysts will be required in these cases. This suggests that banks which rely on purchased software cannot expect to maintain the same staff-to-management ratios as banks using in-house developed software.

## 5. Conclusion

Our results suggest that projects where structured systems analysis and programming are used are much more labor intensive than those where non-structured techniques or purchased software strategies are followed. Proponents of structured analysis and programming techniques have claimed that those techniques result in the development of software that is easier to maintain than software developed under non-structured techniques. But the findings do not support that contention. Instead, they suggest that structured techniques, as practiced today, are more labor intensive than those non-structured techniques that are assumed to be inferior. Additionally, it appears from the data that banks that purchased their software expended just as much effort on the

TEFRA enhancements as those that used non-structured techniques to enhance in-house software. Despite these findings, it is thought that structured techniques still hold a promise for more productive systems analysis and programming. The development of CASE technology may dramatically change the productivity of these methods, by automating the tedious, time consuming documentation activities associated with structured analysis, as well as by eliminating the need for programming support. In addition, a standard Structured Systems Design Language could be based on current structured documentation conventions. It could contribute to the standardization of systems design and result in improvements in systems performance.

## References

[1] Jack J. Baroudi and Michael J. Ginzberg. "Impact of the Technological Environment on Programmer/Analyst Job Outcomes", Communications of the ACM, Vol. 26, No. 9 (June 1986), pp. 546–555, see especially p. 547.

[2] Victor R. Basili and Robert W. Reiter, Jr. "A Controlled Experiment Quantitatively Comparing Software Development Approaches". IEEE Transactions on Software Engineering, Vol. SE-7, No. 3 (May 1981), pp. 299–329, see especially p. 299.

[3] Barry W. Boehm, "Software Engineering", in J. Daniel Couger, Mel A. Colter, and Robert W. Knapp Advanced System Development/Feasibility Techniques. New York: John Wiley & Sons, 1982.

[4] Ralph Emmett Carlyle. "High Cost, Lack of Standards Is Slowing Pace of CASE", Datamation, Vol. 33, No. 16 (August 15, 1987), pp. 23–24.

[5] Robert P. Cerveny, Edward J. Gerrity, and G. Lawrence Sanders. "The Application of Prototyping to Systems Development: A Rationale and Model", Journal of Management Information Systems, Vol. III, No. 2 (Fall 1986), pp. 52–62.

[6] Robert P. Cerveny and Daniel A. Joseph. "Large Business Organizations' Use of PC Technology", Journal of Systems Management. Vol. 37, No. 6 (June 1986), pp. 14–17.

[7] Tor Guimaraes. "Managing Application Program Maintenance Expenditures", Communications of the ACM. Vol. 26, No. 10 (October, 1983), pp. 739–746.

[8] J.B. Holton. "Are The New Programming Techniques Being Used?" Datamation, Vol. 23 (July, 1977), pp. 97–103.

[9] I.S.J. Hugo. "A Survey of Structured Programming Practice". AFIPS Conference Proceedings, New York, 1977, pp. 741–752.

[10] Michael A. Jackson. Principles of Program design. New York: Academic Press, 1975.

[11] B.P. Lientz and E.B. Swanson. Software Maintenance Management. Reading, Massachusetts: Addison-Wesley Publishing Company, 1980.

[12] B.P. Lientz and E.B. Swanson. "Problems in Applications Software Maintenance". Communications of the ACM, November 1981, pp. 763–769.

[13] James Martin. Application Development Without Programmers. Englewood Cliffs, N.J.: Prentice-Hall, Inc., 1982.

[14] James G. Miller. Living Systems. New York: McGraw-Hill Book Company, 1978.

[15] I. Nassi and B. Schneiderman. "Flowchart Techniques for Structured Programming". ACM SIGPLAN Notices. Vol. 8, No. 8 (August 1973), pp. 12–26.

[16] Mary Sumner and Jerry Sitek. "Are Structured Methods for Systems Analysis and Design Being Used?", Journal of Systems Management, Vol. 37, No. 6 (June 1986), pp. 18–24.

[17] Iris Vessey and Ronald Weber. "Research on Structured Programming: An Empirical Evaluation. IEEE Transac-

tions on Software Engineering, Vol. SE-10, No. 4 (July, 1984), pp. 397–407.

[18] Iris Vessey and Ronald Weber. "Some Factors Affecting Program Repair Maintenance: An Empirical Study", Communications of the ACM, February 1983, pp. 128–134.

[19] C.E. Walston and C.P. Felix. "A Method of Program Measurement and Estimation", IBM Systems Journal, Vol. 16 (1977), pp. 54–73.

[20] J.D. Warnier. Logical Construction of Programs. New York: Van Nostrand Reinhold, 1976.

[21] E.J. Webb, D.T. Campbell, R.D. Schwartz, L. Sechrest, and J.B. Grove. Nonreactive Measures in the Social Sciences, Boston, Massachusetts: Houghton Mifflin Company, 1981.

[22] Edward Yourdon. "What Ever Happened To Structured Analysis?", Datamation, vol. 32, no. 11 (June 1, 1986), p. 133+.
