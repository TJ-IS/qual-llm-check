---
otero_id: 27343
otero_key: "5BHMQ938"
title: "Setting Priorities for DSS Development"
authors: "C. Lawrence Meado; Martin J. Guyote; Peter G.W. Keen"
year: "1984"
journal: "MIS Quarterly"
doi: "10.2307/249348"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Setting Priorities for DSS Development
Author(s): C. Lawrence Meador, Martin J. Guyote and Peter G. W. Keen
Source: MIS Quarterly, Vol. 8, No. 2 (Jun., 1984), pp. 117-129
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/249348

Accessed: 28/06/2014 17:27

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Setting Priorities for DSS Development

By: C. Lawrence Meador
Martin J. Guyote
Research & Planning, Inc.
215 First Street
Cambridge, Massachusetts 02142

By: Peter G.W. Keen
Informational Technology
Services, Inc.
One Forks Road
Lexington, Massachusetts 02123

## Introduction

Decision support systems (DSS) has become a popular buzzword in the last few years. The term DSS applies to information systems designed to help managers solve problems in relatively unstructured decision-making environments. The growing popularity of the DSS concept can be attributed, in part, to the increased competitiveness, uncertainty, and complexity of the economic environment. Successful DSS applications have included long-range and strategic planning, policy setting, new product planning, marketing planning, cash flow management, operational planning and budgeting, and portfolio management [3]. These systems usually integrate sophisticated data management, modeling, analytical, and display capabilities with powerful, user friendly command languages.

## Abstract

Traditional project management and design methods used for data processing and MIS applications are ill-suited to decision support systems (DSS). The authors argue that effective management of DSS development requires:

a) An explicit plan for the full development life cycle;

b) Careful assignment of responsibility for DSS development;

c) Appropriate user involvement and direction; and

d) On-going user needs assessment and problem diagnosis.

A 13-stage tactical plan for DSS development, called the DSS development life cycle, is described. Results are presented from an in-depth survey of users of 34 different DSS to show that the tasks performed most ineffectively in DSS development are planning, assessment of user needs, and system evaluation. Results from the survey are also presented that show the factors responsible for DSS project approval, and the factors responsible for DSS success.

Keywords: Decision support systems, development life cycle, architectural features, user need assessment, defining success

ACM Categories: H.1.2, H.4.2, J.O

Managers now have a more broadly perceived need for decision support and, in many cases, a belief that computer systems can be a valuable source of help [4]. In addition, the widespread and rapidly expanding diffusion of microcomputers has changed the way most managers think about computers in general. They are far more proactive in their interest and less resistant to the idea that they themselves can be “hands-on” users. They hear about software tools like VisiCalc (and the “Visi-clones”) that make it easy for computer novices to begin building models and incorporating more quantitative analysis approaches into their planning and decision making. Many managers are curious about computerized decision support, yet these managers are properly hesitant. They are uncertain about which criteria would help them to decide on whether to proceed with a DSS, and what impact they can expect a DSS to have on the organization and on themselves. DSS development often requires an unpredictable investment in time and money, and managers cannot easily estimate what return to expect on this investment beyond some vague promise of “better decisions.” They may also be unsure of how to initiate and develop a DSS or how to manage the development process as it evolves.

## Purpose and Approach

The authors have conducted an in-depth survey of DSS users in a wide variety of firms and industries. The results (based on 19 organizations and 34 DSS's) offer some insights into managers' needs, how DSS's are being developed and used to address these needs, and the impacts of DSS. This article summarizes these results, and defines strategies for managing DSS development and use.

The likelihood of a DSS succeeding and having the desired organizational impact strongly depends on understanding how to manage DSS development and use over time. Managerial decision environments, and managers' ways of thinking about them, change frequently. To be useful a DSS must be responsive to these changes. A distinctive feature of DSS development relative to other information systems is the use of an "adaptive" design and development strategy [9]. This calls for small-scale initial prototype systems, continued incremental development, and responsiveness to users' changing needs. Many articles on DSS design highlight aspects of this approach. Keen [9] calls it "adaptive design," Ness [10] terms it "middle-out" (versus top-down and bottom-up). Sprague and Carlson [11] provide general summaries and Bennett [12] describes specific examples of user integration and adaptive methods. The need for proactive DSS evolution follows naturally from the nature of the managerial tasks being supported. Ongoing management of DSS development and use, instead of just installation and exit, is necessary to address the need for responsiveness over time. The end user survey described here focuses on these issues.

## End User Survey

The end user survey on which this article is based has several purposes:

1. To provide a theoretical framework for systematic investigation and discussion of DSS end user design and development issues,

2. To develop an experimental methodology for gathering data relevant to these issues, and

3. To develop and test managerially useful diagnostic instruments and survey techniques for assessing critical DSS variables in a wide range of organizations.

The survey was conducted through administration of a written questionnaire. An hour-long version of the questionnaire was used for in-depth personal analysis of selected firms; questionnaires for the remaining firms were administered by mail and were shorter, with a completion time of approximately twenty minutes. The questions covered four areas:

1. Organizational context, and individual attitudes concerning computers, the organization's data processing department, and the effectiveness of the DSS development process,

2. Structural characteristics of important decisions/tasks facing end users,

3. Characteristics of the decision process for these tasks, and the impact of the DSS on the process, and

4. Characteristics of DSS implementation and use, plus end user assessments of DSS architecture, capabilities, and success.

The emphasis on brevity and ease of completion led to a reliance on direct questions and the use of rating scales for responses.

The questionnaire was accompanied by a cover-sheet that described what was meant by DSS. Each respondent was asked to answer the survey questions with reference to a single, computer-based system. Users were asked to choose an integrated system used to support decision making that offered end users the capability to model some important decisions, perform necessary analyses, manage the data involved, and generate reports and/or other visual displays. By an “integrated” system we meant one that offered these capabilities under a single interface (even though several software tools may have been used to create the system). The primary types of decisions made with the DSS in the survey are shown in Figure 1. Although we did not specifically distinguish between institutional and ad hoc DSS (see Donovan & Madnick [13]), all but a few of the DSS were institutional in nature and offered “organizational support” [14] (i.e., they were used to support recurring decisions such as budgeting and long-range planning and to coordinate decisions across the organization). Respondents were asked to rate the DSS with regard to the capabilities embodied in the system as presented to and used by them (which may or may not have reflected the capabilities of the underlying software tools).

The survey included widely different types of systems. Languages used to build the DSS included BASIC, FORTRAN, COBOL, PL/I and APL, although most used specialized languages such as EXPRESS, IFPS, FOCUS, EPS, EMPIRE, and XSIM. There was little variation in the nature of the hardware supporting the systems, with very few systems not run on internal mainframes through the data processing department.

<table><tr><td>Type of Decision</td><td>Percent of respondents whose primary use of the DSS is for this type of decision</td></tr><tr><td>General long-range planning</td><td>38</td></tr><tr><td>Strategic assessment</td><td>23</td></tr><tr><td>Product strategy</td><td>8</td></tr><tr><td>Negotiation of budgets</td><td>8</td></tr><tr><td>Reporting and analysis</td><td>8</td></tr><tr><td>Operational planning and control</td><td>6</td></tr><tr><td>Acquisition strategy</td><td>2</td></tr><tr><td>Capital investment strategy</td><td>2</td></tr><tr><td>Financing strategy</td><td>2</td></tr><tr><td>General budgeting</td><td>2</td></tr><tr><td>Cash flow management</td><td>2</td></tr></table>

Figure 1 Percent Distribution of Primary Type of Decision Made With DSS

While two of the systems had been in use for six years, half of the systems had been in use for nine months or less. Frequency of use of the systems varied from once a week or more (for about half of the systems), to every two to three weeks (about one out of four systems), to less than once every six months.

## Respondent Characteristics

Questionnaires were sent to attendees of the DSS Software Conference held in Cambridge, Massachusetts, and to selected members of national associations of strategic and financial planners during 1982 and 1983. In addition, 50 respondents at three test sites were chosen for in-depth analyses. These respondents were chosen in conjunction with high-level DSS users and providers at each site. The total number of questionnaires distributed was 340. The total number of questionnaires completed was 73 from

18 firms representing 34 different decision support systems. This represents a response rate of 22%.

Respondents in the end user survey came from firms with annual revenues ranging from a few million to several billion dollars. The majority of the respondents were senior and middle managers, the remainder were staff planners and analysts. All were either direct or indirect end users of the DSS they rated. The greatest number were in marketing departments, although financial and corporate planning functions were also well represented, as were MIS groups (Figure 2).

By and large, the respondents had extensive experience with computers or computer systems. It is not surprising, then, that they also held favorable attitudes toward computers. Respondents strongly disagreed with statements that computers were unlikeable or threatening, and strongly agreed that computers can increase the effectiveness of senior managers.

The direct user of the systems varied considerably. In twelve cases, corporate or division management used DSS directly. Nevertheless, in most cases the direct users of the systems were staff personnel, with top management using the system through intermediaries.

![](/api/attachments/5BHMQ938/fulltext/images/7727b4adec437a610ec0e11c73da8a58ed71294738de072038754400cdffa441.jpg)  
Figure 2 Frequency Distribution of Respondent Department

## Respondent Ratings of Data Processing

When asked to rate the importance of various skills for the data processing department, as well as how they felt their in-house DP group performed in these areas, the survey respondents rated as most important: sensitivity to users' needs, project management skills, and the motivation and education of users. These, and other "people" skills, were given priority over technical skills by the respondents (Figure 3). In this, DSS end users agreed with the information systems managers and systems analysts surveyed by Benbasat [15]. In terms of performance, DP departments were rated most highly in their willingness to work closely with users in designing new systems, and lowest in their knowledge of user department operations and their expertise in designing analysis-based systems like DSS.

## Respondent Ratings of DSS Features and Effectiveness

Respondents were asked to give their ratings of the importance of specific DSS design features,

<table><tr><td>Skill</td><td>Average Rated Importance</td><td>Average Rated Performance</td></tr><tr><td>Sensitivity to users&#x27; needs</td><td>6.23</td><td>4.43</td></tr><tr><td>Project management skills (planning and control)</td><td>5.64</td><td>4.42</td></tr><tr><td>Implementation planning: education, motivation and training of users</td><td>5.49</td><td>4.24</td></tr><tr><td>Expertise in design of analysis-based systems like DSS</td><td>5.47</td><td>3.57</td></tr><tr><td>Intimate knowledge of your department&#x27;s operations</td><td>5.21</td><td>3.82</td></tr><tr><td>Willingness to work closely with users in designing new systems</td><td>5.09</td><td>5.84</td></tr><tr><td>Leadership ability, administrative experience, sensitivity to political issues</td><td>4.78</td><td>4.03</td></tr></table>

Figure 3 Average Rated Importance and Performance of DP Department Skills (1 = Low, 7 = High)

## 120 MIS Quarterly/June 1984

as well as of the performance of their own systems with regard to these features. The results are shown in Figure 4; the rating scales used for this question and all others in the survey ranged from 1 (low) to 7 (high). Respondents agreed strongly about the importance of general features such as system adaptability, ease of learning and use, and integration of all components under a single command language. Common priorities concerning database characteristics stressed security and ability to support large and complex databases with many dimensions and variables. Among the remaining features, the highest priorities were sophisticated graphics and report formatting capabilities, and tools for performing “what-if” and sensitivity analyses.

Respondents were evidently satisfied with many of the database characteristics of their systems. The three features of security, database size, and complexity mentioned above were also among the highest rated features in terms of system performance. The DSS also received relatively high marks for database expandability and display formatting. The lowest marks were reserved for the available analytic and mathematical functions and, to a lesser extent, the modeling features of the systems.

Respondents were asked to rate their agreement with several statements indicating the “success” of their DSS. These statements included:

1. The DSS fits in well with our planning methods.

2. The DSS fits in well with our reporting methods.

3. The DSS fits in well with our way of thinking about problems.

4. The DSS has improved our way of thinking about problems.

5. The DSS fits in well with the “politics” of how decisions are made around here.

6. Decisions reached with the aid of the DSS are usually implemented.

7. The DSS has resulted in substantial time savings.

8. The DSS has been cost-effective.

9. The DSS has been valuable relative to its cost.

10. The DSS will continue to be useful to our organization for a number of years.

11. The DSS has so far been a success.

The first six statements were meant to indicate how effective the DSS had been in supporting organizational decision making; the average rated level of agreement with statements (1) to (6) was 4.65. Respondents were therefore equivocal in their assessment of the DSS' impact on decision making. Nevertheless, they were enthusiastic about the cost-effectiveness and overall worth of their DSS. The last five statements received an average rating of 5.43. The highest intercorrelations were also found among the last five statements (the average correlation between pairs of ratings for statements (7) to (11) was .70). Ratings for the first six statements were highly intercorrelated, but correlated less strongly with the statements regarding cost-effectiveness and success. These findings indicate that the perceived success of a DSS is dependent on more than its "fit" with organizational decision making; perceptions of overall cost-effectiveness predominate.

Ratings of the importance of various factors in the DSS project approval process showed the most important factor to be top management emphasis of the proposed system (Figure 5). The next most important factor was the anticipated return on investment in a cost/benefit sense; however, it seems that qualitative or “soft” benefits are not given a great deal of consideration.

Next in importance came a variety of practical issues such as development costs, impacts on data processing resources, and degree of user commitment. Surprisingly, despite the political implications of some of these factors, “company politics” rated last in importance. This may reflect the phrasing of the question; “company politics” is a more ambiguous and inclusive term than “degree of user commitment,” “top management emphasis,” etc.

## Respondent Ratings of DSS Development Life Cycle

To be effective, the DSS design and development process should follow a plan — “adaptive” does not mean ad hoc. A tactical plan is needed that lists specific tasks to be performed, plus their order and frequency of performance. Since DSS evolve, that plan must be cyclical, that is, all or most of the tasks will have to be redone at regular intervals to ensure responsiveness to changing users’ needs. The survey asked users to evaluate the importance and the performance in their organization of each of the various stages of DSS development. We call the tactical plan used in this research the DSS development life cycle (Figure 6). The tasks are described below:

Figure 4 Average Rated Importance and Performance of DSS Features

<table><tr><td></td><td>Average Rated Importance</td><td>Average Rated Performance</td></tr><tr><td>The data structure allows for multiple sets of rows and columns (or dimensions and subscripts, e.g., sales data arranged by month, geographic area, product, etc.)</td><td>6.32</td><td>5.28</td></tr><tr><td>The system supports a database large enough (in terms of the number and size of data entries) and complex enough (in terms of the number of rows, columns, or dimensions) to handle all users' needs</td><td>6.03</td><td>5.08</td></tr><tr><td>The system is easily learned by new users, even those with limited computer experience</td><td>6.00</td><td>4.57</td></tr><tr><td>The contents of the database can be easily changed and expanded.</td><td>5.97</td><td>4.91</td></tr><tr><td>The command language is natural to use and English-like</td><td>5.83</td><td>4.77</td></tr><tr><td>A security system exists that allows for restricted access to the database using prespecified criteria (e.g., ID's, passwords, etc.)</td><td>5.76</td><td>5.51</td></tr><tr><td>The user has extensive control over display format for reports and graphs (e.g., labels, titles, column size, decimal placement, report size, headers, scaling, plot symbols, etc.)</td><td>5.56</td><td>4.80</td></tr><tr><td>The system is integrated with all components running under a single command language</td><td>5.55</td><td>4.72</td></tr><tr><td>The system is adaptive, system components and language can grow as users' needs change</td><td>5.55</td><td>4.72</td></tr><tr><td>What if and sensitivity analysis functions, monte carlo capabilities.</td><td>5.41</td><td>4.42</td></tr><tr><td>There exists a database dictionary that catalogs all elements in the database (variable, dimension names, programs and functions, etc.)</td><td>5.39</td><td>4.58</td></tr><tr><td>The system can accept and manipulate data created by other system, especially commonly used packages</td><td>5.31</td><td>3.58</td></tr><tr><td>Multiple database entries, each with different structure or characteristics, can exist simultaneously within the database</td><td>5.27</td><td>3.87</td></tr><tr><td>There is an interactive command or program with which the user can alter the contents of the database or enter new data</td><td>5.24</td><td>4.77</td></tr><tr><td>An array of standard financial reports and exception reports can be generated automatically</td><td>5.21</td><td>4.45</td></tr><tr><td>Users can easily modify existing programs and functions, and write their own</td><td>5.16</td><td>4.20</td></tr><tr><td>Data for reports and tables can be drawn from many sources within the database simultaneously</td><td>5.15</td><td>4.52</td></tr><tr><td>A wide array of graph formats is supported (line, bar, histogram, pie, stock market, multiple plots)</td><td>5.14</td><td>3.75</td></tr><tr><td>The system is flexible; users from different functional areas with problems of different levels of complexity can all use it</td><td>5.07</td><td>4.35</td></tr><tr><td>Trend projection/curve fitting functions, and time-series analyses.</td><td>5.03</td><td>4.00</td></tr><tr><td>Two or more databases can be conceptually merged or hierarchically related</td><td>5.00</td><td>4.06</td></tr><tr><td>The system format displays tables automatically for multi-dimensional data structures</td><td>5.00</td><td>4.80</td></tr><tr><td>The format in which data is entered can be flexible and is not strictly regimented</td><td>4.97</td><td>3.52</td></tr><tr><td>A wide range of statistical procedures is available (descriptive statistics, regression, other multivariate techniques, scaling techniques, non-parametric, log-linear methods)</td><td>4.97</td><td>3.81</td></tr><tr><td>Multiple models can exist within a database</td><td>4.94</td><td>4.35</td></tr><tr><td>Goal seeking, or backward iteration, automatic reordering of systems of equations, and solution of systems of simultaneous equations</td><td>4.81</td><td>4.09</td></tr><tr><td>Time-series data can be mixed with non-temporal data</td><td>4.72</td><td>3.24</td></tr><tr><td>Standard financial functions (e.g., IRR, NPV, depreciation, discounted cash flow, capital asset pricing)</td><td>4.71</td><td>4.23</td></tr><tr><td>Risk analysis with wide range of distributions</td><td>4.46</td><td>3.65</td></tr><tr><td>The command language can be tailored to meet individual requirements and tastes</td><td>4.43</td><td>4.06</td></tr><tr><td>Ad-hoc calculator mode with all algebraic operators</td><td>4.40</td><td>3.96</td></tr><tr><td>Econometric modeling facilities with a wide range of parameter estimation techniques</td><td>4.35</td><td>2.76</td></tr><tr><td>Optimization functions (e.g., linear, integer, mixed integer, nonlinear, dynamic, and goal programming)</td><td>3.91</td><td>3.26</td></tr></table>

<table><tr><td>Factor</td><td>Average Rated Importance</td></tr><tr><td>Top management emphasis</td><td>5.91</td></tr><tr><td>Return on investment (cost/benefit)</td><td>5.04</td></tr><tr><td>Technically do-able</td><td>4.87</td></tr><tr><td>DSS development costs</td><td>4.76</td></tr><tr><td>Impact on data processing resources</td><td>4.70</td></tr><tr><td>Degree of user commitment</td><td>4.70</td></tr><tr><td>Increase in user effectiveness</td><td>4.67</td></tr><tr><td>DSS operating costs</td><td>4.64</td></tr><tr><td>Increase in user efficiency</td><td>4.61</td></tr><tr><td>Adaptability of organization to change</td><td>4.52</td></tr><tr><td>Urgency of user needs</td><td>4.49</td></tr><tr><td>Uncertainty of objectives for DSS design</td><td>4.27</td></tr><tr><td>Qualitative or “soft” benefits</td><td>4.11</td></tr><tr><td>Company politics</td><td>4.09</td></tr><tr><td colspan="2">(1=Low, 7=High)</td></tr></table>

Figure 5
Average Rated Importance of Factors in DSS Project Approval Process

1. Planning — User needs assessment and problem diagnosis.

2. Application research — Identification of relevant fundamental approaches for addressing user needs and available resources (vendors, systems, studies of related experiences in other organizations, and review of relevant research).

3. Analysis — Determination of best approach and specific resources required to implement it, including technical, staff, financial, and organizational resources.

4. Design — Detailed specifications of system components, structure, and features.

5. System construction — Technical implementation of the design.

6. System testing — Collection of data on system performance to determine whether the system performs in accordance with design specifications.

7. Evaluation — Determination of how well the implemented system satisfies users' needs and identification of technical and organizational loose-ends.

8. Demonstration — Demonstration of the fully-operational system capabilities to the user community.

9. Orientation — Instruction of top-level managerial users in the basic capabilities of the system.

10. Training — Training of direct users in system structure and operation.

11. Deployment — Operational deployment of the full system capability for all members of the user community.

12. Maintenance — Ongoing support of the system and its user community.

13. Adaptation — Planned periodic recycling through the above tasks to respond to changing user needs.

In assessing the importance of DSS development stages, users rated the planning stage (user needs assessment and problem diagnosis) as the highest priority: and the lowest priorities involved research, detailed specifications, and system construction (Figure 7). On the other hand, it was the more technical, typically DP-oriented activities that were given the highest marks for performance. The most poorly performed activities were evaluation and orientation of top-level managers in the basic capabilities of the system.

We measured the effectiveness with which each task was performed for each DSS in the survey. Given that the organization has limited resources to devote to developing a DSS, there should be a direct relationship between importance and performance — the more important a particular task, the better it should be performed. Obviously, it makes little sense to commit time and resources to a task if its performance has little bearing on success.

![](/api/attachments/5BHMQ938/fulltext/images/6141102fc4a91160af19e758019ec8c3ad2e97b483f7d677d065c945a8f7d6d8.jpg)  
Figure 6 Alternate Paths for DSS Development

Of course, the results varied somewhat for different systems, but the overall pattern is shown in Figure 8. This figure shows the average rated importance and performance of each task in the development life cycle. Planning, evaluation, and orientation of top-level users were all activities that were ineffectively performed. These tasks all fell more than one standard error of estimate below the regression line. (The standard error of estimate indicates the standard deviation of the points from the regression line.) Note that although planning did not receive the lowest absolute average performance rating, Figure 8 suggests that it was the least effectively performed task. The mediocre performance of planning should not be tolerated, given its distinctive importance. The more technical, DP-oriented tasks of design and construction were also ineffectively performed. These were the best performed tasks even though rated least important. This means that resources were committed to these tasks that might have been better spent on the more important tasks of planning and evaluation. This result may reflect an avoidance of the more ill-defined tasks in system development. The lesson here is that some assessment of the importance of these tasks should be a part of planning, and DSS development resources should be allocated accordingly. In addition, it seems that technical staff experienced in traditional software development methods may have trouble adjusting to the more unstructured environment of DSS. Data processing begins with functional specifications, DSS with contextual analysis.

<table><tr><td></td><td>Average Rated Importance</td><td>Average Rated Performance</td></tr><tr><td>DSS Planning:User needs assessment and problem diagnosis</td><td>6.09</td><td>4.49</td></tr><tr><td>Adaptation:Responsiveness to new user needs as well as to organization and environmental changes</td><td>5.74</td><td>4.54</td></tr><tr><td>Training:Training of direct system users in system structure and operation.</td><td>5.72</td><td>4.38</td></tr><tr><td>Maintenance:Ongoing support of the system and its user community</td><td>5.72</td><td>4.76</td></tr><tr><td>Evaluation:Determination of how well implemented system satisfies users&#x27; needs</td><td>5.64</td><td>4.18</td></tr><tr><td>System Testing:Collection of data on system performance to determine whether system performs in accordance with design specifications</td><td>5.60</td><td>4.54</td></tr><tr><td>Analysis:Determination of best approach and specific resources required to implement it</td><td>5.51</td><td>4.74</td></tr><tr><td>Orientation:Instruction of top-level managerial users in the basic capabilities of the system</td><td>5.47</td><td>4.00</td></tr><tr><td>Deployment:Operational deployment of the full system capability for all members of the user community</td><td>5.37</td><td>4.43</td></tr><tr><td>Construction:Technical implementation of the design</td><td>5.26</td><td>5.11</td></tr><tr><td>Demonstration:Demonstration of fully-operational system capabilities to members of the user community.</td><td>5.24</td><td>4.42</td></tr><tr><td>Application Research:Identification of relevant fundamental approaches for addressing user needs, and available resources (including systems, vendors, etc.)</td><td>5.21</td><td>4.46</td></tr><tr><td>Design:Detailed specification of system components, structure, and features</td><td>5.16</td><td>4.63</td></tr><tr><td></td><td colspan="2">(1=Low, 7=High)</td></tr></table>

Figure 7 Average Rated Importance and Performance of DSS Development Stages

## Conclusions

Despite the diversity of the sample, it is a small one, and the data presented here are based on respondents' impressions. It seems clear that in order to satisfactorily examine these ideas, in-depth longitudinal studies are needed in addition to cross-sectional ones of this type. Having said this however, we must add that some interesting patterns have emerged.

In interpreting the results, it is important to keep in mind the overwhelmingly favorable attitudes among the respondents toward computers and DSS. The accompanying success of the DSS in the survey could have been either a cause or a result of these attitudes. Given that most of the DSS were primarily used for organizational decisions involving more than a few people, it was not surprising to find high importance ratings for system adaptability, ease-of-use, database security, multidimensionality, and sophisticated display capabilities to support communication of results.

![](/api/attachments/5BHMQ938/fulltext/images/c9b8736ad80bc71fffea61bfd000d65f2b66b2bcf8b332ff2c342957689faf0d.jpg)  
Figure 8 Average Performance vs. Average Importance for DSS Development Process

Another important finding was the significance of cost-effectiveness as a factor in DSS project approval and perceived DSS success. Although managers may desire more effective decision making, the ability of a DSS to effect more efficient decision making is also important to creating and maintaining managerial support. This contrasts with case studies of early DSS [16] which showed an emphasis on value rather than cost, and a general disregard of traditional cost-benefit analysis. The importance of time-savings in formulating plans and budgets shows up often. This is particularly understandable for DSS designed to support regularly recurring institutional decisions like the ones in this survey.

In developing a DSS, the least effectively performed tasks were seen to be planning, evaluation, and orientation. The first two tasks are particularly important and difficult because they require the DSS developer to assess users' needs and how well they are being (or could be) met by a DSS, and what the DSS should look like to serve those needs. The crucial role played during the initial stages of application development have been borne out by research in MIS and EDP applications. For example, McKeen [17] surveyed 32 business applications systems and found that greater time and effort spent on front-end analysis resulted in less overall system development time, less overall cost, and greater user satisfaction with the delivered system.

Taken together, the survey results pose a dilemma familiar to developers of DSS; the problem of assessment. Before approving large scale DSS projects most managers need evidence of some concrete benefits to offset development costs. Evaluations of the success of existing systems also depends on assessing benefits. User needs assessment is critical in providing continuing direction to DSS development. But when DSS's support ill-defined problems their impact on organizational problem-solving is likely to be ill-defined. Successful introduction of DSS into an organization may then depend on targeting applications where substantial time cost benefits can be demonstrated (e.g. automating manual budgeting) until such time as users and developers can form more educated opinions about what DSS will do for them.

## References

[1] Keen, P.G.W., and Scott Morton, M.S. Decision Support Systems; An Organizational Perspective, Addison-Wesley, Reading, Massachusetts, 1978.

[2] Meador, C.L., and Ness, D.N. "Decision Support Systems: An Application to Corporate Planning," Sloan Management Review, Volume 14, Number 2, pp. 51-68.

[3] Alter, S.L. Decision Support Systems: Current Practice and Continuing Challenge, Addison-Wesley, Reading, Massachusetts, 1980.

[4] Scott Morton, M.S. “Organizing the Information Function for Effectiveness as Well as Efficiency,” Working Paper Number C15R-17, Massachusetts Institute of Technology, Cambridge, Massachusetts, 1975.

[5] Rockart, J.F., and Treacy, M.E. "Executive Information Support Systems," Working Paper Number C15R-65, Massachusetts Institute of Technology, Cambridge, Massachusetts, 1975.

[6] Alloway, R.M. “Defining Success for Data Processing,” Working Paper Number C15R-56, Massachusetts Institute of Technology, Cambridge, Massachusetts, 1980.

[7] Rockart, J.F., and Bullen, C. "A Primer on Critical Success Factors," Working Paper Number C15R-69, Massachusetts Institute

of Technology, Cambridge, Massachusetts, 1981.

[8] Alloway, R.M. “User Managers’ Systems Needs,” Working Paper Number C15R-56, Massachusetts Institute of Technology, Cambridge, Massachusetts, 1980.

[9] Keen, P.G.W. "DSS: A Research Perspective," Working Paper Number C15R-54, Massachusetts Institute of Technology, Cambridge, Massachusetts, 1980.

[10] Ness, D.N. "DSS: Theories of Design," Paper presented at the Wharton Office of Naval Research Conference on DSS, University of Pennsylvania, Philadelphia, Pennsylvania, November 4-7, 1975.

[11] Sprague, Jr., R.H., and Carlson, E.D. Building Effective Decision Support Systems. Prentice-Hall, Inc., Englewood Cliffs, New Jersey, 1982.

[12] Bennett, J.L. "Integrating Users and Decision Support Systems," in A Proceedings of the Sixth and Seventh Annual Conferences of the Society for Management Information Systems, J.D. White (ed.) University of Michigan Press, Ann Arbor, Michigan, 1976.

[13] Donovan, J.J., and Madnick, S.E. Institutional and Ad-Hoc Decision Support Systems and Their Effective Use, MIT Working Paper C15R-27, Cambridge, Massachusetts, 1977.

[14] Keen, P.G.W., and Hackathorn, R.D. "Decision Support Systems and Personal Computing," MIS Quarterly, Volume 5, Number 1, March 1981, pp. 21-27.

[15] Benbasat, I., Dexter, A.S., and Mantha, R.W. “Impact of Organizational Maturity on Information Systems Skill Needs,” MIS Quarterly, Volume 4, Number 1, March 1980, pp. 21-34.

[16] Keen, P.G.W. "Value Analysis: Justifying DSS," MIS Quarterly, Volume 5, Number 1, March 1981, pp. 1-16.

[17] McKeen, J.D. “Successful Development Strategies for Business Applications Systems,” MIS Quarterly, Volume 7, Number 3, September 1983, pp. 47-59.

## About the Authors

C. Lawrence Meador is a Lecturer in the School of Engineering, MIT, and is Executive Vice President of Research & Planning, Inc., a consulting firm in Cambridge, Massachusetts. He received his graduate degrees from the Sloan School of Management and the School of Engineering, MIT. He serves on the Board of Directors of Access Data Services, Inc. His current research is concerned with DSS end user needs assessment and software technology feature evaluation. He serves as an editor of Computer Communications and Communicacion e Informatica.

Martin J. Guyote received the M.S. and Ph.D degrees in cognitive psychology at Yale University, and the M.S. degree in management at MIT.

He has been on the faculty of Boston University. He is currently a Consultant with Research & Planning, Inc. in the areas of decision support systems, human problem solving and reasoning, and research methodology.

Peter G.W. Keen, Visiting Senior Lecturer of the London Business School, received his DBA from Harvard University and has been on the faculties of the Sloan School of Management, MIT, Harvard Business School, Stanford University, and the Wharton School at the University of Pennsylvania. His current research includes a study of support systems for policy analysts in educational finance and methodologies for evaluating computer systems which provide for qualitative benefits. He is the managing editor of Office: Technology and People.
