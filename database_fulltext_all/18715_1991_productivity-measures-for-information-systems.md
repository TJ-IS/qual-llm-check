---
otero_id: 18715
otero_key: "3YKTS2ZC"
title: "Productivity measures for information systems"
authors: "Richard A. Scudder; A.Ronald Kucic"
year: "1991"
journal: "Information & Management"
doi: "10.1016/0378-7206(91)90033-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Techniques

# Productivity measures for information systems

Richard A. Scudder and A. Ronald Kucic
Management Information Systems Department, College of Business, University of Denver, Denver, CO 80208, USA

While much has been written concerning information systems productivity, defining and measuring it have proved to be difficult. There are few, if any, recognized standards, and those tools that are used with regularity tend to be technically oriented. Senior executives find the results provided them by these techniques difficult to interpret in ways meaningful to them and to the decisions they must make. It is clear that many top managers have become frustrated with this state of events and that they are determined to improve the situation. Methods for doing this, however, are not readily available. A variety of techniques which have been or which are used in practice are described, together with their strengths and weaknesses. Some of these are extremely technical in nature, others are not. Further, an attempt is made to describe a set of comprehensive measures. In addition, steps being taken by one organization to remedy senior executive frustration with information systems productivity measures are outlined in the context of a case study. Also, a method for presenting information productivity results in business terms also is demonstrated.

Keywords: Productivity, Information systems effectiveness, Software metrics, Function points, Software quality, Software performance measures.

![](/api/attachments/3YKTS2ZC/fulltext/images/05bd0b5c110e37b61209c24d2dfa39fd3ed8b7a20c05414c0ffc3af2ca3eb370.jpg)

A. Ronald Kucic is the 1989–90 US West Willemssen Professor, and he teaches and conducts research in management accounting and information systems at the University of Denver. His current consulting and research interests include systems productivity issues, IS resource allocation issues, activity based costing systems, and MIS curriculum design. Ongoing projects include an examination of the IS resource allocation process and top management's information needs con-

cerning IS at a large multinational service organization and a study to differentiate among organizations which are effective users of IS and those which are not. Professor Kucic also is involved in several joint projects with IS faculty at the University of Maribor (Yugoslavia). In addition, he has consulted and published in the areas of cost accounting and accounting information systems for human service organizations.

## Introduction

Productivity, encompassing the ability to both measure and improve it, has become a watchword of the '80s. According to information from the Bureau of Labor Statistics, the United States ranked next to last in output per hour among twelve leading industrial nations during the early eighties [26]. While the situation in the manufacturing sector seems clear, the performance picture for information systems development is less so. The number of books, monographs and seminars devoted to the issue of Information Systems (IS) productivity grows each year; yet many organizations experience difficulty in simply measuring the performance of existing information systems, particularly in terms understood by senior management. New productivity oriented tools have been introduced (Computer Assisted Software Engineering (CASE) technology, for example). Despite these, practical methods for measuring and improving IS productivity still are not readily available to middle and senior managers.

The aim of this paper is to explore a variety of measures, some technical, some not, which have been advocated for measuring IS productivity; i.e., their efficiency and effectiveness. In addition, an

![](/api/attachments/3YKTS2ZC/fulltext/images/f5bb45eeab67a9dbe2484baf6561d5f62451955f2dd9ed6f097f3037b24a47f2.jpg)  
ment, a determination of the education needs of systems analysts in the '90's, and an examination of the impact of outsourcing, among others.

IS measurement approach being adopted by one large US organization will be described.

Corporate managers have begun expressing serious concern over the role of IS in their organizations as indicated by the following questions and comments. “How, for instance, can you have a cost center that takes up 5% of total revenues without knowing what return on investment to expect? How much should you spend on new information systems technology?” [10] Senior management is tired of taking IS productivity on “faith-alone” [22]. While many believe that the use of information technology is the key to increasing productivity in organizations, they also feel that “in practice, the promise of technology hasn’t been fulfilled. In the broadly defined service sector, from banks to health care clinics, capital spending on computers and office equipment has boomed over the last decade – and productivity has languished” [8]. Senior management now asks tough questions, but the answers received from IS managers seem to be lacking in substance.

All IS shops have sets of parameters that are used to monitor operational factors – system downtime, numbers of reruns, and performance to budget, for example. While many IS managers are not completely comfortable with the measures used, senior non-IS management clearly is dissatisfied $[23]$ . Indeed, a research project sponsored by the Financial Executives Research Foundation, which focuses on the criteria used to justify IS investments, reveals that executives are concerned with the ability of their organizations to quantify both cost savings and the intangible benefits arising from IS projects. Executives also are troubled by the uncertainty and inconsistency of IS benefits throughout their organizations $[6]$ . While not expressly addressing the issue of IS productivity, the concerns appear related to it. Increasingly, senior executives are saying that ways must be found to measure and explain how well or how poorly the systems within their organizations are functioning, and these must be presented in business terms not in IS “technispeak.”

One method some managers use in an attempt to reduce the level of complexity is to focus on a single explanatory IS productivity variable, e.g., system throughput, system availability, number of reruns, etc. Single measures, however, simply are not sufficiently encompassing to adequately describe the performance of an entire IS organization, including both operations and development. Despite the intent to simplify, single measures usually are technically oriented. They also tend to provide data on inconsequential performance areas. Some have suggested that “we should give up counting the irrelevant, even if it is easy to do” [25]. Instead, IS managers should be seeking to describe the efficiency and effectiveness of the IS organization from multiple perspectives. A single explanatory variable is not likely to prove adequate to this task.

## Measurement of efficiency and effectiveness

To be useful to IS and senior management alike, the measurement focus must be on both sides of the productivity equation, i.e., it must deal with both efficiency and effectiveness. Efficiency is concerned with the resources consumed in producing a given application in a timely manner; and, as such, it ought not be ignored in measuring system performance. Effectiveness, on the other hand, is concerned with the quality of the finished product and its appropriateness to the problem/situation for which it was designed. It also would be difficult to judge system performance without taking this factor into account.

Automation of a manual procedure may increase the speed with which a business transaction is handled. If, however, the procedure were not critical to the organization's needs, automation would have achieved nothing of real value but would have generated actual costs. In fact, computerization of some manual processes may do more harm then good, as might be the case if the system design were inadequate or if the staff responsible for the manual process were unprepared for or unwilling to accept automation. IS performance then can be: (1) efficient but not effective, (2) effective but not efficient, (3) neither effective nor efficient, or (4) both efficient and effective – these representing but four possibilities on a continuum. For completeness, therefore, measures of performance need to provide data on both factors.

Many existing measures (throughput, downtime, and system responsiveness, e.g.) are efficiency oriented only. Effectiveness or quality is difficult to measure; hence, such factors are not readily available. There seems to be no doubt, however, that problems with quality in IS organizations are present. While the Quality Assurance Institute indicates that less than half of the 69 companies interested in quality measurement have a formal measurement program, the Institute feels that the quantification of “factors such as project costs and customer satisfaction is set to grow in importance in MIS groups in the next two years” [12]. Additional evidence comes from a recent study of Fortune 1000 companies [24], where the current percentage of organizational time spent in maintenance of existing systems is found to be greater than 45 percent. Arthur indicates that “80% of the typical DP budget” is spent on maintenance [5]. If these figures merely define the upper and lower limits of maintenance expenditures, significant savings can be expected through the development of higher quality (more effective) systems. Savings would come from the decrease in the maintenance effort that would be a direct result of improved quality.

Hamilton and Chervany describe effectiveness in a way that subsumes efficiency as a part of effectiveness $[17\ and\ 18]$ . They argue (along with Edelman $[16]$ ) that an effective system is also efficient. In order to be effective, the IS organization must have both a “goal-centered view” and a “systems-resource view.” Goal-centered effectiveness involves identifying the objectives of the IS organization, finding measures for those objectives, and then determining whether the objectives have been met. Hamilton and Chervany state the systems resource view as follows:

The MIS function is to develop and operate/maintain information systems that will enhance the organization's ability to accomplish its objectives. Accomplishment of this objective can be evaluated from two perspectives:

I. The efficiency with which the MIS development and operations process utilize assigned resources (staff, material, machines, money) to provide the information system to users.

II. The effectiveness of the users, or the users' organizational unit, using the information system in accomplishing their organizational mission.

According to this view, the efficiency of the IS organization is based on the decisions made by that organization with respect to resource utilization tion. Quality, on the other hand, is judged indirectly by focusing on the usefulness of delivered systems in performing the tasks for which it was designed. It is this which ultimately determines whether or not the IS group continues to receive the same level of resources.

## Systems performance measures

Pure systems performance can be measured in a variety of ways. Response time, workload volume capabilities, and network queuing algorithms all have been discussed extensively in the literature [e.g., 13]. Many methods and techniques for accomplishing this type of measurement are available, and the appropriate one in a given situation will be highly dependent on the hardware and software configuration. Anderson suggests that multiple measures of system functionality be used because they allow system designers to determine “performance feasibility prior to system development and the identification of performance trade-offs during design and development” [4]. Performance measures of this type are useful for determining overall technical system operability, predicting the impact of proposed applications, and identifying hardware performance bottlenecks.

## Development measures for software

One area which has been extensively analyzed is that of software development productivity. One traditional measure has been to count the number of source lines of written code (SLOC). This tool still is in common use. In fact, Drummond [15] notes that vendors and reviewers frequently refer to this metric when discussing the productivity of software tools. The nature of the information provided by the SLOC measure is unclear, however, as is its use in a decision making context.

<table><tr><td>Table 1Programmer productivity measures.</td></tr><tr><td>Productivity- Lines of code per staff hourCost- Staff hours per executable statementReliability- Errors per line of code- Logical faults per line of codeMaintainability- Modules or units affected per change- Staff hours to implement change</td></tr></table>

An example of the use of traditional measures comes from a continuing series of studies being conducted by the Software Engineering Laboratory [9]. For this project, a series of measures, including those shown in Table 1, has been analyzed.

The data have been made available, and the results emphasize the close relationship between good system performance and careful system design and development. A set of benchmarks for programmer productivity on modules of varying complexity and functionality also is provided by these data.

This set of metrics provides an excellent starting point for measuring software development productivity, but they are not without problems. There are inherent limitations with the lines of code metric. Some programmers use less code to produce programs of equal quality. Furthermore, applications developed using fourth generation languages or CASE tools cannot be easily compared with applications written using earlier generation languages. Even programs generated with different third generation tools cannot be compared on a lines of code basis. Individual organizations, therefore, will have to maintain an appropriate set of statistical measures for each of its different software development undertakings. These sets will be developed over a period of time and, of necessity, will be based on experience.

Yet another difficulty arises owing to the use of different counting rules $[20]$ . The rules used to count the number of lines of code in a program vary from shop to shop. Some methods count only lines which have actions in them; others count all lines, including those containing data. Further complicating matters is the fact that the counting rules have not been stable from development methodology to development methodology.

## Albrecht's function point analysis

One methodology designed to overcome some of the deficiencies listed above is that of Albrecht's function point analysis. [1,2,3]. Since this counts the external functions or project deliverables of an application, it is more independent of the technology used. The analysis focuses on identifying functions - an address change input, a printed bill output, queries, etc. For a given software application, five different elements are analyzed (see Table 2).

<table><tr><td>Table 2Function point elements.</td></tr><tr><td>A. The number of inputs to the application (forms, screens)</td></tr><tr><td>B. The number of outputs from the application (reports, screens)</td></tr><tr><td>C. The number of inquiries an end-user can make</td></tr><tr><td>D. The number of logical data files used by the system</td></tr><tr><td>E. The number of interfaces to other applications</td></tr></table>

To develop a function point index, each deliverable or element is assigned a numerical complexity level. Next, factors influencing the project are numerically assessed. According to Drummond, “system to system interfaces” are included among these influencing factors, along with others, such as innovation, telecommunications, and distributed databases. These influencing factors then are added together and expressed as a percentage. Percentages less than 100% imply a positive influence, while percentages greater than 100% indicate that the influencing factors will cause the software development project to take longer. The total influencing factor percentage is multiplied by the total of the deliverable complexity levels to arrive at the final function points index. For additional detail, see Drummond.

Albrecht's methodology has enjoyed a recent increase in attention and acceptance as a primary measure of IS development productivity. T. Capers Jones, among others, includes it as one of a primary set of metrics used to describe overall IS productivity [21]. He claims that the advantage brought to software project management by function point analysis is that of mathematical consistency. "They [function points] do not behave in strange ways, as the lines of code metrics do. The old metrics were perverse in that they often moved in the opposite direction of real economic productivity." In order to better understand the technique, Jones has been collecting data on function points from many different sources, including 250 corporations in the United States.

## Arthur's performance measures

Arthur argues for a supplemental set of methods for judging software quality. Most of his suggested analyses can be performed through use of static analyzers which mechanically analyze application code.

Two forms of measurement are used. One involves the executable lines of code (ELOC), and the other measures complexity. ELOC has been “widely correlated to development and maintenance costs,” as has complexity measurement, but it has the limitations previously discussed for SLOC. Programmed decisions (IF-THEN, CASE, DOWHILE and GOTO) and logical operators (AND, OR and NOT) provide the basis for complexity measurement using static analyzers, since their numbers and types are easily measured by mechanical analysis of the software.

Once logs of lines of code and programmed decisions are prepared, the IS organization can create a historical database of metrics – mean time between failures and mean time to repair, for example – for different types of coding structures. The database would be of use in determining the types of systems likely to give the most problems. Goals for software quality could be set based on the database, and future software development projects could avoid making similar errors.

Arthur's method is somewhat akin to Function Point Analysis. Both measures call for measuring complexity and building a database of historical software development data so that future measurement can be done more precisely. The difference is that Arthur's method focuses on the internal mechanics of the software; while Function Point Analysis is concerned with the utility of the software.

## Budgetary performance measures

Relating the costs of a project to its benefits and computing a return on investment is another commonly accepted method for judging IS performance. The approach requires that value be ascribed to the various tangible and intangible benefits expected to arise from the development of a successful system (improved operational productivity, improved cash flows, etc.). These then are compared to the costs of the project, and if the benefits exceed the costs the project is deemed successful.

The measurement of organizational performance usually is accomplished by computing the return on assets or other similar ratio (Return On Equity or Return On Investment, e.g.). There are limitations to this method, however. “These ratios measure the productivity of capital. But how efficiently you use the capital no longer determines the success of a knowledge based organization. Superior management is the magic element that separates excellence from mediocrity” [25].

Projects also can be measured in terms of time and budget. Software application projects usually have timelines and resource commitments established with specific target dates. Reports comparing project performance against budget can be useful tools in measuring progress toward completion. These reports often provide guidance in determining whether the application will provide the ROI anticipated. The techniques of SLOC, ROI, timelines and function point analysis provide a set of methods for quantitatively judging IS efficiency. They do not provide measures of the quality (effectiveness) of application development.

The use of either cost-based or market-based pricing of IS products and services is closely allied to the other budgetary measures. Cost-based prices are determined by dividing the projected IS costs to be recovered by the projected resource usage to arrive at a unit price per resource. It does not provide any significant measure of the productivity of the IS resource. The market-based pricing method, on the other hand, adopts the concept that prices for information systems services must be based on rates competitive with the market place. “Market-based pricing mandates that computer facilities not only be competitively priced but also full service – in other words, run as a business enterprise, responsive to the requirements of the users and to the business priorities of the greater corporation” [7].

In order to make market based pricing work, Bergstrom argues that the rules listed in Table 3 must be followed. The information systems group has to work in concert with the user group and treat them as valued customers. Since users are unlikely to purchase services that they view as uncompetitive or lacking in value, the availability of market-based data provides a powerful basis for measuring the performance of the IS organiza-

Table 3

<table><tr><td>Market based pricing rules.</td></tr><tr><td>A. Maintain detailed and accurate cost accounting</td></tr><tr><td>B. Continually measure and improve cost effectiveness</td></tr><tr><td>C. Realistically compare to peers and commercial vendors</td></tr><tr><td>D. Share ideas and concerns with peers</td></tr><tr><td>E. Stay on the leading edge of developments and trends</td></tr><tr><td>F. Satisfy your user community</td></tr></table>

tion. This assumes, of course, that users are free to acquire needed services in the open market, are aware of market prices, and/or can otherwise exert pressure on the IS group to be competitive in both price and service quality.

## The need for multiple measures

The complexity of IS performance measurement has been noted previously. Given the variety of measures available and the diverse uses to which they are put, the likelihood that any single explanatory variable can function as a surrogate for all other measures is small. For it to do this and also give senior management meaningful insight into the contributions of IS is asking for the impossible. Knowing the IS group performance against budget, for instance, gives no clue as to overall system response time and vice versa. Further, neither measure gives management any information on whether or not operational managers are satisfied with the systems being developed for them. An approach, therefore, is needed to enable the measurement of IS productivity from a variety of perspectives; while at the same time also providing information on both IS efficiency and effectiveness.  
T. Capers Jones has undertaken to define a set of multiple measures that are more broad ranging

<table><tr><td>Table 4IS organization performance measures</td></tr><tr><td>- Defect removal efficiency</td></tr><tr><td>- Maintenance productivity</td></tr><tr><td>- Successful product ratio</td></tr><tr><td>- User satisfaction</td></tr><tr><td>- Employee satisfaction</td></tr><tr><td>- Staff training</td></tr><tr><td>- Development Productivity</td></tr></table>

than any of the single ones. The suggested set (see Table 4) provides insight into many of the performance aspects of an information system, but it also includes information on additional areas. Jones suggests employee satisfaction, defect removal efficiency, staff training, and successful product ratio as new measures to consider. Employee satisfaction can be measured through surveys. Jones argues that it is important to track levels of employee morale within the organization. He also notes that “companies which provide 10 days of staff training per staff-year show higher annual rates for software productivity (measured by function points) than companies that provide no training.”

The successful product ratio is a the number of projects completed (and used) as a percentage of the number attempted. Defect removal ratio is computed by comparing the number of defects found by users to the number of defects found by developers prior to release. Based on his research using a sample of 250 companies, Jones suggests

Table 5
Performance measures.

that these latter two figures should have values of less than 5 percent in successful companies.

Dickson and Wetherbe are responsible for one of the most comprehensive set of measures developed so far (see Table 5). This set focuses on four major groups of IS performance measures: (1) financial, (2) organizational efficiency, (3) managerial, and (4) capacity [14].

The Dickson and Wetherbe set adds at least two elements not previously mentioned: (1) the need to set a performance goal for measuring planning for systems resources capacity, and (2) the focus on managerial performance.

Note that measurement of managerial performance involves the perceptions of those external to the IS organization: senior managers, users, and external assessors. There is an implicit assumption that the IS organization is performing well if those attitudes are positive. In the case of external assessors (auditors, for example), measurement of the IS organization based on budget and operational performance also is attained.

ComputerWorld has made a more recent attempt to define a multiple set of measures. Members of the publication's staff have developed a proprietary model to assess “the effectiveness of a company's total investment in information systems” [11]. The model involves 6 criteria and uses a weighting approach. Computations were made and organizations providing data were ranked in terms of the effectiveness of their information systems. The factors included in the scoring system and their weights are: current book value of all computer and computer related hardware (15%), estimated annual MIS/DP budget (30%), average percentage of profit growth over the past 5 years (15%), percentage of current MIS/DP budget spent on staff (10%), percentage of current MIS/DP budget spent on training and education (15%), and total number of personal computers and terminals in the organization (15%). In addition to separate weightings of each criterion, the model requires certain adjustments and other computations before the final weighted factor is generated. Each factor is separately computed, and the six are added together to arrive at a firm's final score. It is the final score which determines the rankings – the higher the score, the higher the ranking.

While some of the criteria in the Computer-World model are clearly related to those identified by Jones, some represent additions: for instance, overall corporate profits. In fact, a loss in any one of the past 5 years causes the profit criterion to be valued at zero. This and the “book value of existing hardware” factor may be providing a surrogate response to the “what am I getting for my investment in IS” question.

The “number of PCs and terminals” factor is designed to assess the level of integration of automation within an organization. As noted in a discussion of the model: “..., providing user access to technology is very important in both supporting information systems within the company and in how well companies are able to implement strategic systems.”

It is too soon to judge the usefulness of the ComputerWorld model. It does have the advantage that it has been used to rank the effectiveness of the information systems efforts of 100 companies. This yearly data collection effort likely will continue, thus providing researchers with an ever growing database for analysis. The fact that the model has been presented in a practitioner oriented publication read by technicians and users alike also is an advantage. It will be reviewed and responded to by IS, middle and senior managers; thus, increasing its potential usefulness. The resulting debate should serve to improve the design and the potential for acceptance of the model.

The foregoing has provided background on the available productivity measures. Subsequent discussion will focus on combining and refining these into a more comprehensive and coordinated set of measures designed to be adapted to the specific circumstances of a given organization. The purpose of any particular subset would be to provide managerial assistance in the assessment of the efficiency and effectiveness of an IS unit.

## A set of overall performance measures

The comprehensive series of measures shown in Table 6 is based on the discussion as well as the experience of several large organizations.

## Case study - One company's efforts

One organization planning to implement a set of coordinated measures is a Fortune 1000 company in the manufacturing and distribution business. It has plants and/or distribution sites in multiple states and operates nationally. Its product lines are diverse. The organization has multiple divisions with a loosely coordinated central information systems organization whose director reports to the head of the manufacturing division. The central IS organization provides transaction processing and some basic MIS reporting, but much of the design and programming of MIS reporting is done at the divisional level with advice from the IS group.

Table 6
Overall performance measures.

<table><tr><td>Personnel Performance- Technical capabilities- Business knowledge- Training- Replacement projections- Career Satisfaction- IS Job Satisfaction</td><td>Goal Setting- Senior management role in IS planning- IS representation in planning- Quality of planning- Balance of risk - portfolio management- Forecast for future technology- Forecast of future IS capabilities</td></tr><tr><td>Managerial Performance- Attitude of senior management- Attitudes of users- Performance audits- Perceptions of IS “problems”Perceptions of IS “capabilities”</td><td>Operational PerformanceQualitative- Backup performance- Security- Privacy- User interaction- Complete data- Accurate data</td></tr><tr><td>Developmental PerformanceQuantitative- Time and cost- Staff Turnover- Size of system request backlog- System maintenance costs- System cost standards- SLOC/ELOC- Feature point analysis- Function point analysis- Charge out performance</td><td>- Understandable output- Timely output- Relevant output- User friendly operations- Error resistant operations</td></tr><tr><td>Qualitative- Application portfolio- Formal methodology quality- SDLC- Structured design- Project control- Productivity aides- Documentation quality- Team size- User interaction</td><td>Quantitative- System availability- Late jobs- Job rerun percentages- Throughput- System utilization- Maintenance performance ratios</td></tr><tr><td></td><td>Financial Performance- Budget Performance- Cost Recovery- Distribution of costs- Market-based industry standard costs- Expense categorization- IS Investment Model</td></tr></table>

The IS group currently is confronting several problems. First, there is a need to establish a strategic vision for information systems in the organization. The company does not have a clear picture of how it will use IS in the future, nor has it determined which applications will be the most significant.

Second, the IS group is faced with a problem common to many organizations, viz., connectivity/compatibility. Several different computers, including IBM mainframes, Hewlett-Packard and DEC minis, and a large array of PCs, are operating within the company. Users complain of the inability readily to combine information from disparate sources. They are particularly unhappy with the large amount of manual reentry that is required when they must use and/or analyze data supplied from functional areas which use incompatible machines.

Third, the IS organization is in the midst of a turn-around. In the not too distant past, users viewed IS as bureaucratic and inflexible. That image has begun to change, but users still perceive a need for improved cooperation and communication. While many admit that the IS group seeks user input prior to making important decisions, there are still those who feel that the process has not gone far enough. An IS user advisory group now exists, but its role needs clearer definition.

Finally, users question the commitment of senior management to IS. They note that each major component of an IS related project must be separately justified in the same manner as other capital projects. Users, however, argue that top management either does not understand or simply ignores the fact that the project parts are related. The project is never viewed and evaluated as a whole. thus, many potentially worthwhile projects are never approved. The reason for the continuation of this process, in the view of the users, is that the senior managers do not understand IS and, hence, do not value it as a resource. It is unclear if this user perspective is a correct one.

## Main measures

An interview approach was used to determine which of the many available measures were appropriate to the organization. The principle IS managers and key users took part. Performance measures were reviewed, as were the strategic goals of both the IS group and the company.

Table 7
Corporate I.S. performance measures – Case study

<table><tr><td>A. System Availability</td></tr><tr><td>B. Error Removal</td></tr><tr><td>C. Developmental Effectiveness</td></tr><tr><td>D. Maintenance Effectiveness</td></tr><tr><td>E. Staff Satisfaction</td></tr><tr><td>F. User Satisfaction</td></tr><tr><td>G. Budget Performance</td></tr><tr><td>H. Information Availability</td></tr></table>

Based on the results of the interviews and other analyses, a set of factors was constructed from the group of coordinated measures. Those found in Table 7 are the ones on which the organization chose to focus for the coming year. These will be reported to senior management by the IS organization during that time. Since this process is still in its early stages, adjustments and refinements to the set are likely to occur as experience is gained with its use as an IS evaluation device. The primary measures, of course, must be supported by other lower level and, perhaps, more technically oriented measures.

## Secondary support measures

In reality, many of the primary performance measures will be aggregates of two or more sub-measures. A tentative set of contributing measures is identified below. The approach is to define a set of sub-measures which can be “normalized” to a “star” diagram using a scale ranging from 0 to 100 percent. This reporting method provides a means for translating the information provided by the selected measures into terms understandable by senior management (for additional information on “star diagrams,” see Figure 1 and its accompanying narrative). The sub-measures then can be averaged to provide an indication of the overall level of performance of each of the principle ones. Potential supporting measures for each of the main measures are identified in Table 8.

## Gathering performance data

Each of the different reporting levels in the IS organization will contribute to the reporting of performance measures. Obviously, not every group will report in all areas. An initial set of measures for the relevant groups might be:

Systems Operations (A, B, D, E, F, G, H)
Telecommunications (A, C, E, F, G, H)
End User Support (B, C, D, E, F, G, H)
Systems Development (B, C, E, F, G, H)

Table 8
Potential supporting measures.

A. System Availability
- Percentage of system availability
- Uptime/downtime ratio, throughput, jobs processed

B. Error Rate
- Ratio showing the percentage of errors found by users versus the percentage of errors found by IS prior to application release

C. Developmental Effectiveness
- Function points per staff member per month
- Comparison to national standards
- Documentation effectiveness

D. Maintenance Effectiveness
- Function points per staff member per month
- Comparison to national standards
- Repair of error prone modules
- Reduction in the number of job reruns required

E. Staff Satisfaction
- Job satisfaction survey
- Training level
- Turnover ratio

F. User Satisfaction
- System response time
- Response for equipment requests
- Communication with MIS Staff
- User satisfaction survey

G. Budget Performance
- Corporate wide performance to budget
- Comparison to industry standards
- Market-based charge-out

H. Data/Information Availability
- Connectivity levels
- Information response speed

In addition to identifying and reporting on performance measures for each part of the organization, performance goals must be determined. To accomplish this, the various operational, tactical and strategic levels of the organization will define a coordinated set of goals. The final results for the IS group, as a whole, will reflect the performance of its constituent parts.

A variety of techniques must be used to collect the data from the various organizational levels. Summaries of standard operating statistics will provide one level of data. Surveys of users designed to probe the degree to which IS or one of its components is meeting the critical success factors of that part of the organization and user satisfaction surveys also will be required. Some of the data collected will be objective in nature while some will be subjective. The key will be for the data to be collected in a consistent manner over time using care to insure that it is accurate and reliable.

Another necessary element will be to insure that the performance measures used on a continuous basis by the IS organization remain the ones of critical importance to key users. This means that users will have to be involved in ongoing evaluation of the reporting system. The use of a consensus based, interactive process to decide on effective measures and the goals for each of those measures is paramount. If the users and IS group agree on what the goals are and how they are going to be measured, then the levels of objectivity and subjectivity become less important.

Given the present stage of development of the model, it will be necessary to gather and report on the identified data elements for several months, perhaps even for as long as a year, to assess their appropriateness and usefulness to management. Only a thorough test will demonstrate whether or not the approach provides results that both IS and senior management feel are useful for evaluating and making resource allocation decisions concerning information systems.

## Informing top management

If this process is to succeed in the long run, IS managers must be able to present information to senior management in terms understood by them. Janulaitis states that a universal characteristic of successful IS managers is that they have developed ways to “objectively measure the performance of DP” [19]. This implies that information must be presented to top management in a manner that they can understand and interpret. Therefore, the test also will include presentation to management of the summary data on IS performance in a variety of formats. The emphasis, however, will be on the use of graphics.

IS managers should not strive to present all available measures of their unit to senior management. Instead, the most important measures, i.e., those which represent performance in each of the critical areas should be presented. One method for doing this is through the use of a star graph or diagram. A graph of this type can be used to illustrate from 8 to 10 performance measures simultaneously. An example, based on the primary measures chosen for the case study organization, is shown in Figure 1.

![](/api/attachments/3YKTS2ZC/fulltext/images/e5e8f4bd877fa4f423e019d0d46007c27748c3650db45e57dc79403b38a332ab.jpg)  
PERFORMANCE AGAINST GOALS, 1988  
Fig. 1. Sample star diagram for corporate IS.

In the diagram, the center point represents the maximum goal level for each of the different performance measures selected for use by the organization. The circle represents the agreed upon goal for each of the measures, arbitrarily set at 90% for each goal in this example. The irregular polygon and the associated percentage figures provide an indication of how well the IS organization is progressing in meeting those goals.

## Conclusion

Determining the productivity of information systems continues to be a major issue for many organizations. Instead of taking the simple, but potentially misleading, approach of assessing only one level of performance, it is recommended that companies look at assessing multiple levels of IS performance. If an organization carefully determines what it is that constitutes IS effectiveness and efficiency for itself, and then defines IS performance at all levels of the organization, it can choose an overall set of measures which will constructively represent performance in meaningful terms. The end result ought to be a set of productivity measures which will give a more accurate evaluation of the worth to the company of the IS group and its individual components than is possible with any single factor model. One adaption of this approach now is ready for implementation and testing.

## References

[1] A.J. Albrecht. "AD/M Productivity Measurement and Estimate Validation." CIS&A Guideline 313, IBM Corporate Information Systems and Administration, November, 1984.

[2] A.J. Albrecht. "Function Points Help Managers Assess Application, Maintenance Values." Computerworld Special Report on Software Productivity, CW Communications, 1985, pp. 20-21.

[3] A.J. Albrecht and J. Gaffney, Jr. "Software Function, Source Lines of Code, and Development Effort Prediction: A software Science Validation." IEEE Transactions on Software Engineering, SE-9, No. 6, November 1983, pp. 639–648.

[4] G. Anderson. "The Coordinated Use of Five Performance Evaluation Methodologies." Communications of the AC. Vol 27, No. 2, February, 1984, pp. 119–125.

[5] Jay Arthur. "Software Quality Measurement." Datamation, Vol 30, No 21, Dec 15, 1984, pp. 115-120.

[6] E. Band, S. Reed, and D. Robertson. "A Survey: How Do You Justify an Investment in Technology?" Financial Executive, September/October, 1988, pp. 44–48.

[7] L. Bergstrom. "MIS, INC." Business Software Review. November, 1987, pp. 36–42.

[8] Business Week, “The Productivity Paradox,” No. 3055, June 6, 1988, pp. 100–115.

[9] D. Card, F. McGarry, G. Page, et al. "Measures and Metrics For Software Development." Software Engineering Laboratory, March, 1984. Cited in "Software Development Metrics," DATAPRO Research, AS80-050-101, 1988.

[10] R. Carlyle. "ROI In Real Time." Datamation, Vol 33, No. 4, February 15, 1988, pp. 73–74.

[11] Computerworld Supplement. “How to Calculate Your Company’s Ranking.” September 12, 1988, p. 80. (Revised in subsequent issue, September 19, 1988).

[12] J. Connolly. "Job One: MIS Quality Measurement to Soar in Importance." ComputerWorld, April 11, 1988.

[13] P. Denning. "Performance Analysis: Experimental Computer Science at It's Best." Communications of the AC. Vol 24, No 11, Nov., 1981, pp. 725-727.

[14] G. Dickson and J. Wetherbe. The Management of Information Systems. New York: McGraw-Hill, 1985.

[15] S. Drummond. "Measuring Applications Development Performance." Datamation, Vol 31, No 4, Feb 15, 1985, pp. 102–108.

[16] F. Edelman. "The Management of Information Resources - A Challenge for American Business." MIS Quarterly March, 1981.

[17] S. Hamilton and N. Chervany. “Evaluating Information System Effectiveness – Part I: Comparing Evaluation Approaches.” MIS Quarterly September, 1981.

[18] S. Hamilton and N. Chervany. “Evaluating Information System Effectiveness – Part II: Comparing Evaluator Viewpoints.” MIS Quarterly December, 1981.

[19] V. Janulaitis. "Report the Good News to your CEO." ComputerWorld Extra, June 20, 1988, p. 28.

[20] C. Jones. Programming Productivity, McGraw-Hill, NY, 1986.

[21] C. Jones. "Building a Better Metric," Computerworld Extra June 20, 1988, pp. 38–39.

[22] R. Kaplan. "Must CIM Be Justified by Faith Alone?" Harvard Business Review, January–February, 1986.

[23] A. Lapland. “CEOs Question Value of Investments in Information Systems.” Info World, March 7, 1988, p. 6.

[24] R. Scudder and D. McCubbrey. “Study of Major MIS Issues in the United States and Japan.” Unpublished Working Paper, University of Denver, September, 1988.

[25] P. Strassman. “Productivity.” Computerworld Extra June 20, 1988, pp. 1, 11.

[26] U.S. Department of Labor, Bureau of Labor Statistics. Handbook of Labor Statistics, Bulletin 2217, 1985.
