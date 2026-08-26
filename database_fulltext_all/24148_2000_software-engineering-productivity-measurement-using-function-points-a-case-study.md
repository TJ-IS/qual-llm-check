---
otero_id: 24148
otero_key: "C3QK4DT3"
title: "Software engineering productivity measurement using function points: a case study"
authors: "Hai Suan Bok; K.s. Raman"
year: "2000"
journal: "Journal of Information Technology"
doi: "10.1080/026839600344429"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Software engineering productivity measurement using function points: a case study

HAI SUAN BOK

5 Tanah Merah Kechil Road, 17–06, Singapore 466665

K. S. RAMAN

School of Computing, National University of Singapore, 10 Kent Ridge Crescent, Singapore 117543

This paper reports on the  ndings of an empirically based case study of the use of function points analysis (FPA) by the information systems division of a large  nancial services company. The software engineering productivity  gures measured by FPA in this company varied widely across the departments of the division and projects. Investigation of the reasons for the variations showed that, in addition to factors such as the technology platform and application characteristics, organizational and human factors affect the accuracy and reliability of productivity  gures. Elucidating the lessons from this case, this paper suggests that three factors – knowledge of the FPA, calibration of the function point productivity indicator and rigour of the measurement process – are critical to the successful implementation of an FPA programme. These  ndings and the issues identi ed in the paper will be of interest to academics in the area of software productivity measurement and companies considering FPA as a productivity metric.

## Introduction

Investment in information systems (IS) has become a competitive necessity and organizational imperative and organizations in the manufacturing, retail and service sectors continue to invest heavily in IS. Software development and maintenance is a major activity of the IS function and the capability of software teams has been identi ed to be the most signi cant software cost driver of this activity (Boehm, 1981). Consequently, the productivity and effectiveness of software development has become a key concern of IS and top management.

Productivity measurement is a complex organizational activity which focuses on management purpose. It has to address the diverse concerns of different management levels (Dale and Zee, 1992). Measuring software engineering productivity is even more complex because software engineering is a knowledgeintensive activity in which inputs and outputs are not always clearly de ned and stable. The results of two surveys have shown that few companies were successful in measuring the productivity of software development (Hetzel, 1993). The  rst survey was conducted in 1990 by the Software Quality Engineering Institute on 800 software companies. This survey found that the overall usage of software development productivity measurement in these companies was low and companies with measurement programmes were mostly dissatis ed with their programmes. The second survey was conducted in 1991 during the Application of Software Measurement Conference. A modest 15% of the delegates rated their software measurement programme as ‘established’ and none rated their programme as ‘highly developed’. Only 6% rated the effectiveness of their programme as ‘good’ or ‘excellent’. These results called for more research on the problems faced by organizations in software productivity measurement.

Four software metrics are popular in the measurement of productivity of software development activity. They are Halstead’s software science, McCabe’s syclomatic complexity, lines of codes and function point analysis (FPA). Amongst these, FPA has attracted much research attention and generated a large number of publications (Cote et al., 1988). Past studies of FPA have focused on the technical aspects of the metric. Such a focus, while necessary, does not address the implementation issues. Through an empirically based case study in a large  nancial services company that has used FPA for 6 years, this paper examines the problems and issues faced in using FPA to measure software engineering productivity. The  ndings of this study will be of interest to academics in the area of software productivity measurement using FPA and to companies considering implementing an FPA productivity measurement programme.

## The technique

FPA was proposed by IBM’s Allen J. Albrecht in 1979 and was later revised in 1983 (see the Appendix for a description of FPA). It sizes an application system from the end-user’s perspective by identifying data exchanges between users and the software application and those between the software application with other applications. The productivity of a software project is usually measured by the ratio of function points (FPs) delivered to programming hours and months (Bock and Klepper, 1992). An FP is designed to be dimensionless, independent of the programming language, tool and technology used. It is an empirically based (Wrigley and Dexter, 1991) and function-oriented metric (Pressman, 1987).

Much research has been done on the accuracy of FPA and how it can be applied to measuring the various aspects of IS. Davis (1992a) found that the accuracy of FPA estimates varied across different stages of a software development project, from approximately ±35% at the initial requirements stage to 10% in the design de nition stage. On the other hand, Dreger (1989) estimated that the accuracy and reliability of FPA estimates is within 10% for existing systems and 15–20% for planned systems. Although FPA is primarily used in productivity measurement (Verner and Tate, 1987), it has also been used to measure many aspects of software engineering activities (Dreger, 1989; Johnson, 1989; Martin, 1991). For example, it can be used to measure the speed and cost of development, quality and productivity of an information centre, the accuracy of projection of a project’s duration, the ef ciency of software maintenance, the usefulness of applications, the productivity gains from improvement programmes or used as a project control tool or a diagnostic tool. FPA is a useful management tool for an IS department if used effectively. FPA has two counting standards – one issued by the International Function Point User Group (IFPUG) and the other by the UK Function Point User Group covering the MKII method (Treble and Douglas, 1995).

FPA has gained much acceptance over the years as a software engineering metric. The 1992 IFPUG conference reported that there were approximately 300 user organizations, which includes large US and European organizations such as IBM, AT&T, GE, TRW, HP, Boeing, STC, the UK Inland Revenue, the Sema Group, Logica, GEC and EDS. FPA has been applied to more than 250 different programming languages (Dreger, 1989) and it was predicted that FPA would become the dominant metric by mid-1990s (Yourdon, 1992).

## Factors in uencing FPA

FPA de nes an FP as a unit of measurement of the complexity of an application or one end-user business function, although the two have different meanings. Some (Abran and Robillard, 1994; Kitchenham and P eeger, 1995) have questioned the de nitions of an FP – whether it is a unit of measurement for functionality, size, complexity or user deliverables. Having a clear de nition of an FP is important as productivity measurement should measure a result (such as value to users) over input rather than output (such as lines of codes) over input (Hetzel, 1993).

On FPA scales, Abran and Robillard (1994) questioned Albrecht’s model of summing ordinal scale measures, which violates basic scale-type constraints. They also found that the FP value that a system can obtain is not continuous. For example, an application that does not have an external input (IT) type has a weightage of 0, whilst those with low IT have a weightage of 3, medium IT of 4, and high IT of 6. They questioned whether FPA is a proper measurement scale. Moreover, the weightage used in FPA was derived from an empirical study of a speci c project database (Wrigley and Dexter, 1991) of 24 projects (Jones, 1991). The small sample size raises doubts about the general applicability of the FPA’s scales to other software projects.

FPA is in uenced by the technology used, project characteristics, application characteristics, organization and the people involved. Hence, any estimation of project resources using FPA should take into account new staff, increased project complexity and other development characteristics (Pressman, 1987).

## Technology factors

FPA is not independent of the technology used (Symons, 1988; Tate and Verner, 1991). Productivity tools such as a report generator are able to produce higher FP delivery rates than third-generation programming languages. FPA is suitable for a thirdgeneration environment (Banker et al., 1994) but not software languages and tools which have in nite number of uses (Symons, 1988).

## Project characteristics

FPA is not independent of a project’s size (Symons, 1988; Martin, 1991) and duration (Davis, 1992a). Many parameters can affect the duration of large and complex projects. These include the number of users who have the authority to sign off the project, the geographic distribution of software development staff and so on. Martin (1991) reported that productivity

## Software engineering productivity measurement

is inversely proportional to the size of a project because small projects are simpler and have less project overheads. However, Davis (1992b) suggested that very small projects show low productivity, but productivity increases with mid-size projects and then deteriorates for large projects. In a study of more than 100 projects in an organization in 1 year, Johnson (1989) found that the productivity  gures between projects varied as much as 15 times (0.16–2.43 FP/day). Hence, different productivity benchmarks need to be used to estimate the resource requirements for projects of different characteristics.

## Organisational factors

The FP delivery rate is in uenced by the software development environment and counting standards used (Davis, 1992a), training and organizational standards (Low and Jeffery, 1990). Therefore, it is essential that organizational factors are taken into consideration when comparing and interpreting FP delivery rates across organizations.

## Human factors

The rating of the raw count in FPA is subjective (Matson et al., 1994). Its accuracy depends on the skill and experience level of the analyst who performs the counting (Wrigley and Dexter, 1991). It takes 1 h to count between 25.8–35.3 (Bock and Klepper, 1992) and 100 FPs (Kemerer, 1993). Although good training is able to reduce the level of subjectivity between trained analysts (Low and Jeffrey, 1990; Douglass and Walsh, 1993; Kemerer, 1993), the differences in rating between trained analysts vary between plus and minus 10% (Kemerer, 1993). Recent research by Subramanian and Lacity (1997) found that users are able to count FPs consistently after some training. Another area which is in uenced by human factors is the rating of the general application characteristics (GACs) in FPA. It is highly subjective (Pressman, 1987; Johnson, 1989; Wrigley and Dexter, 1991; Bock and Klepper, 1992; Davis, 1992a; Matson et al., 1994), although one study (Jeffrey et al., 1993) found GACs have no signi cant effect on the  nal FP counts. The effect of human factors on FPA is too great to be ignored.

## Application characteristics

FPA has often been criticized for its failure to re ect the characteristics of real-time applications accurately (Carlyle, 1987; Dreger, 1989; Davis, 1992a; Yourdon, 1992). It awards more FPs to applications with many input and output (I/O) interfaces than applications with extensive and complex internal logic (Symons, 1988; Johnson, 1989) and its adjustment factors are greater for batch processing systems (Verner and Tate, 1987). Companies like McDonnell Douglas experienced signi cantly different productivity patterns between business, scienti c and engineering Computer Aided Design and Computer Aided Manufacturing (CAD/CAM) applications (Bock and Klepper, 1992). In another major study of 4000 software projects between 1950 and 1990 in the USA, Jones (1991) found management information systems (MIS) projects more productive than systems and military projects, as the MIS projects contain more I/Os and less logic. In this respect, Johnson (1989) found that a project generally has one or two overriding factors or ‘dominant’ characteristics which in uence the productivity measured by FPA (Table 1). These characteristics include screens, cloning, processing and integration. He asserted that these four characteristics plus his dominant theory are able to explain the productivity differences between applications.

In summary, several factors have an in uence on FPA. It is imperative to consider these factors when considering the implementation of FPA (Figure 1).

## Objectives of this study

This study suggests that few organizations consider the effect of the above  ve factors in their FPA implementations and, as a result, their productivity measurement programmes are ineffective. Hence, the main objective of this research is to elucidate lessons from an empirically based case study to draw the attention of research and practitioner communities to investigating and improving the success rates of FPA productivity measurement programmes.

Table 1 Dominant characteristics of applications and productivity

<table><tr><td>Major characteristics</td><td>FP/man-day</td><td>Productivity level</td></tr><tr><td>Few screens, limited cloning, complex process, extensive integration, etc.</td><td>0.20–0.53</td><td>Low</td></tr><tr><td>No dominant characteristics</td><td>0.63–0.89</td><td>Medium</td></tr><tr><td>Many screens, extensive cloning and limited integration.</td><td>1.00–3.89</td><td>High</td></tr></table>

![](/api/attachments/C3QK4DT3/fulltext/images/21f55de228cd899478c7305e5aeb2c207462ca3a93a139413fdee4c34623bebd.jpg)  
Figure 1 Factors affecting FPA

## Research site

Institutionalizing an FPA productivity measurement programme requires many years of effort. Therefore, the research site must have mature and established FPA practices. The research site in this study is the IS division of ECHO (a synonym), a large  nancial services company. ECHO has implemented FPA for over 6 years. Its IS division has 120 software engineers and it has more than 35 years of software development experience, beginning in 1963 with an IBM mainframe computer. More than 5000 programmes developed in-house are in use in ECHO today. ECHO operates a variety of computer platforms – a mainframe computer, a minicomputer and 700 PCs connected to several local area networks (LANs) and wide area networks (WANs). It uses network and relational databases and more than ten software languages which includes Cobol, CICS, ADS/O, SAS, Easytrieve Plus, Database IV, Rexx, C, Assembler, SQL Windows and Pascal.

The IS division of ECHO has three departments. Departments A and B develop and maintain the mission-critical mainframe applications which support the main business activities of ECHO. Department C develops and maintains the applications which support ECHO’s internal operations such as procurement, general ledger and payroll. Many of the mission-critical applications were developed using Assembler, Cobol, Easytrieve Plus, CICS, ADS/O, etc. These applications are large; they are more complex, critical, dynamic and integrated than those developed for internal operations. These applications make use of a combination of off-the-shelf packages, client server and mainframe. Departments A and B have more experienced staff than department C due to the missioncritical applications they support (Table 2). ECHO uses an FP productivity indicator (FPPI) to monitor the monthly productivity performance of the IS division and its three departments. The FPPI is a simple measure of year-to-date FPs delivered per man-day.

## Research methodology

Case study methodology is widely used in MIS (Lee, 1989). It can be used for exploratory, descriptive and explanatory research (Yin, 1994) and is particularly useful in studying behaviour in a natural environment and discovering new events (Graziano and Raulin, 1997). Therefore, the use of case study methodology is considered appropriate for studying the factors that in uence the effectiveness of FPA in a real-life situation.

This study investigated the entire process of productivity measurement of ECHO. Data were collected from multiple sources through interviews, inspection of past FPA records and direct observations. The inspections were carried out on the in-house FPA documentation to ascertain their level of knowledge of FPA. The observations were made on management’s interpretation of the FPPI in six IS division monthly management meetings in which the FPPI  gures were discussed. The computer records of 1649 FP computations between 1989 and 1993 were analysed to study the characteristics of the FP computations. Semi-structured interviews were conducted with the project leaders, their supervisors and managers involved in the FP computation in order to understand the problems and issues faced.

## ECHO’s productivity measurement process and problems

A software metric engineer (SME) who has 6 years experience in FPA heads ECHO’s software engineering productivity programme. ECHO’s IS staff are trained in FPA by the SME a few months after they join the company. They go through a 1-day intensive training course in FPA. In addition, ECHO has in-house standards to guide the counting of various commonly used data types.

ECHO’s FPA process starts with project leaders computing FPs upon completion of the respective projects. He/she makes use of project documentation which includes the documentation of database,  le, screen, report and programme logic in their computation. This computation is  rst reviewed by the supervisor and then by the SME who examines the data

Table 2 Department size, work experience and productivity

<table><tr><td>Department</td><td>Size (Number of staff)</td><td>Average work experience of staff (Number of years)</td><td>Productivity (FP/man-day)</td></tr><tr><td>A</td><td>35</td><td>4.1</td><td>1.79</td></tr><tr><td>B</td><td>50</td><td>5.8</td><td>1.34</td></tr><tr><td>C</td><td>35</td><td>3.6</td><td>2.50</td></tr><tr><td>Overall</td><td>120</td><td>4.6</td><td>1.71</td></tr></table>

## Software engineering productivity measurement

for exceptionally high or low FP counts. Clerical staff key the data into the FPA database. Every month an FPPI report is produced for managers of departments A–C so they can monitor their department’s productivity performance. These reports are discussed in the IS division’s monthly management meeting. Figure 2 depicts this process.

ECHO faces four main problems in using FPA to measure software development productivity. In ECHO, the FPPI  uctuates every month (Figure 3). ECHO could not explain these  uctuations or relate them to changes in the development process, tool, people or other factors. Such  uctuation affect the acceptance level and creditability of the metric (Kemerer and Porter, 1992). The second problem is ECHO’s inability to compare its productivity  gures with other companies. There are few FP  gures published and the  gures published are disparate – they vary between 0.2 and 40 FP/man-day (Table 3).

The third problem is that the productivity level measured by the FPPI contradicts management’s perception of the relative staff productivity levels of the three IS departments (Figure 4). In the period 1990–1992, department C measured the highest productivity with 2.5 FP/man-day whilst Department B measure 1.34 FP/man-day. This is despite the fact that department C has the least experienced staff with an average of 3.6 years of work experience whilst department B has the most experienced staff with an average of 5.8 years of experience (Table 2).

The fourth problem is that many software tasks requested by users do not yield FPs despite substantial effort spent on them. Of the 1649 tasks analysed between 1989 and 1993, only 31% yielded FPs, 47% of them yielded no FPs and the remaining 22% were user support activities where FPs are not computed. ECHO’s management questioned whether FPA measures all values delivered to users fairly.

Organizationally, FPA has been very much an IS activity in ECHO. User management are not concerned or involved and they do not relate FPs to the systems delivered to them. The cost of implementing FPA is around 2.9% of ECHO’s annual IS budget. It comprises mainly manpower costs incurred in FP computation, data capture and review. While cost was not an issue in implementing FPA initially, management now feels that FPA is not delivering the expected return. ECHO has not been able to set the cost of FPA against productivity improvement as ECHO cannot make much sense of what its productivity indicator means. However, ECHO persists with FPA as it cannot  nd a better and cheaper alternative and it believes that some measures are better than no measures.

![](/api/attachments/C3QK4DT3/fulltext/images/8330567da039e84973e97e902e3f9d818a351126df4d3b3c674481edd1d33d3f.jpg)  
Figure 2 ECHO’s productivity measurement process

![](/api/attachments/C3QK4DT3/fulltext/images/0d2349a5a0edd365bec529d389bfb5ef0ab6222339bd16a7f7c905f1772916f2.jpg)  
Figure 3 ECHO’s Fluctuating FPPI (1990–2)

## Analysis of ECHO’s problems

Analysis of the qualitative and quantitative data collected in this research showed that the problems faced by ECHO in its productivity measurement programme may be attributed to three main factors: insuf cient knowledge of FPA, poor calibration of the productivity indicator and lack of rigour in the measurement process. They are discussed in some detail here.

Table 3 Published productivity  gures

<table><tr><td>Software environment</td><td>Productivity reported</td><td>References</td></tr><tr><td>4GL, CASE tool</td><td>12–40 FP/man-day</td><td>Martin (1991)</td></tr><tr><td>Not reported</td><td>2.13–5.33 FP/man-day or 16–40 h/FP</td><td>Davis (1992a)</td></tr><tr><td>Cobol, database and conventional method</td><td>0.38–0.57 FP/man-day</td><td>Martin (1991)</td></tr><tr><td>Not reported</td><td>0.23 FP/man-day</td><td>Martin (1991)</td></tr><tr><td>LINC environment</td><td>0.20–3.55 FP/man-day or 1.5–26.6 h/FP</td><td>Davis (1992b)</td></tr></table>

![](/api/attachments/C3QK4DT3/fulltext/images/862793e81823ae9f60f24a67334c972fd182342b9bb11c8d8201429ce9d6557a.jpg)  
Figure 4 FPPI’s for the three IS departments (1990–2)

## ECHO’s knowledge of FPA

Good knowledge of a software metric is fundamental to an effective measurement programme. Part of ECHO’s problems can be attributed to its lack of in-depth knowledge of FPA such as its de nitions, purpose, assumptions and applications.

Albrecht (1984) de ned total work effort as the manpower expended to accomplish a software task without regard for organization lines. However, ECHO only includes the effort of the IS staff but not the effort of the users, database administrators and others. This deviation in ates ECHO’s FPPI because the FPPI measures the number of FPs produced for each manday spent on the project. This is consistent with prior studies which found that some organizations do not follow Albrecht’s (1984) de nition of work effort (Martin, 1991) and it affects the reliability of FP counts (Kemerer and Porter, 1992). On the other hand, FPA considers the value delivered to all categories of users which includes end-users, installation and conversion user functions, operations user functions, etc. (Albrecht, 1984). However, ECHO only considers the end-user’s perspective even though the application has to cater to the needs of many user groups. For example, an application needs to meet the needs for ease of operations, ease of data maintenance and security standards and others. The exclusion of these values results in lower FPs, as only some of the values delivered are recognized. Such deviations from the original theory contribute to the disparity of FP productivity  gures across organizations.

The main purpose of productivity measurement is to identify areas for improvement. However, ECHO’s FPA database only captures data elements which are necessary for productivity measurement but which are not suf cient to explain why one project has higher productivity than another project. Its database only contains data elements such as description of task, department, project leader, start date, completion date, FPs and man-days spent. These data elements are inadequate for explaining the productivity differences. For instance,  ve factors in uence software engineering productivity – people, problems, process, product and resources (Pressman, 1987). Without data on these factors, it is dif cult to identify areas for productivity improvement.

ECHO’s IS division performs three activities: software development, software maintenance and user support. However, ECHO only measures the productivity of its development and maintenance activities. The productivity measured by the FPPI is therefore biased towards these activities. ECHO is not aware that FPA may be used to measure the productivity of other IS activities such as user support, which is an important service in ECHO. It usually takes the forms of clari cation, discussion, a technical feasibility study, cost estimation and impact analysis. In the case of ECHO, mission-critical applications usually demand more user support services in order to meet the changing expectations of customers and its dynamic business environment. Hence, the productivity of the department mainly supporting mission-critical applications would be lower as it has to channel part of its productive resources to user support activities for which no FPs are given. This becomes a problem when the work activities of its three IS departments are not homogeneous – departments A and B spend 43.7 and 60% more resources on user support services, respectively, than department C. These departments often voice their concerns in management meetings that, while they spend a lot of resources supporting users, their effort are not recognized as value to customers in terms of FPs. These  ndings suggest that ECHO has inadequate knowledge on the assumptions and limitations of FPA and its applications. Such inadequacy has far reaching impacts on the measurement programme as we shall discuss in the next two sections.

## Calibration of an FPPI

A good productivity indicator should be valid and reliable. It should measure what it purports to measure while taking into consideration the factors which might

## Software engineering productivity measurement

affect its accuracy. It should also be interpreted according to its de nitions. This discussion shows that many of the problems faced by ECHO on  uctuating FPs stem from the way the indicator is calibrated and interpreted. The FPPI used by ECHO is a simple measure of year-to-date FPs delivered per man-day. This de nition does not consider technology, application and project factors. Like any large IS department, ECHO uses several technology platforms in developing its applications. Different technologies are capable of delivering different productivity (Martin, 1991). Disregarding the different dominant technologies used in the three departments makes productivity comparison between them dif cult. For instance, over 70% of the projects in departments A and B use conventional mainframe technologies, which is signi cantly higher than the 33.3% of department C (Table 4). On the other hand, 66.7% of Department C’s work uses mainframe of ce system, client server and PC technologies. Such disparities in the dominant technology platforms used in the different departments suggest that a productivity comparison across departments must consider the effect of the different technologies used.

Three application characteristics emerge clearly in ECHO – complexity, the need for integration and the number of output types. Complexity refers here to the number of business rules in the application. The need for integration refers to the number of interfaces an application has with other applications through shared data or programmes where a change in one application affects other applications. The number of output types of an application refers to the number of data elements on the screens or reports. The SME was asked to classify the applications into four categories, crossing high/low complexity and integration with high/low number of types of outputs. Complexity and integration are grouped together as most of the complexity arose from the integration between applications. Again, the characteristics of the applications supported by the three departments are signi cantly different (Table 5). More than 70% of the applications developed and supported by departments A and B are HL applications (see Table 5 for de nitions of HL, LH, LL and HH applications), whilst 89% of the applications supported by department C are LL and LH applications. HL applications are found to have lower productivity than LH applications. Hence, the productivity comparison between these departments is affected by the different characteristics of their applications.

To study the effect of the application characteristics and technology platform on project productivity, a sample of 202 computations was analysed. The project productivities between the three departments are statistically signi cantly different (F = 3.65 and p = 0.029). The application characteristics have an effect on the project productivities (F = 3.15 and $\pmb { \mathscr { p } } = 0 . 0 2 8 )$ ), but the technology platform has no effect (F = 1.03 and n.s.). This result supports Jones’ (1991) assertion that different types of applications have signi cantly different productivity levels, but it is not consistent with Martin’s (1991)  ndings that different technologies produce different productivity performances. This result does not reject the notion that some technologies are able to improve productivity. A possible explanation is that a high productivity technology platform was used to develop low productivity applications. The insigni - cant result could also be due to using a technology platform in developing applications of different characteristics. Study of the effect of technology on productivity will require developing the same application across different technology platforms. Such controlled experiments however are not possible in a  eld study such as this.

Table 4 Different technology platforms across departments

<table><tr><td rowspan="2">Department</td><td colspan="6">Technology platforms</td><td rowspan="2">Productivity (FP/man-day)</td></tr><tr><td>Mainframe non-database system (%)</td><td>Mainframe database system (%)</td><td>Mainframe office system (%)</td><td>Client server system (%)</td><td>Independent PC system (%)</td><td>Total (%)</td></tr><tr><td>A</td><td>70.0</td><td>10.8</td><td>0.0</td><td>3.0</td><td>16.2</td><td>100</td><td>1.79</td></tr><tr><td>B</td><td>0.0</td><td>72.0</td><td>8.0</td><td>0.0</td><td>20.0</td><td>100</td><td>1.34</td></tr><tr><td>C</td><td>25.5</td><td>7.8</td><td>31.4</td><td>11.8</td><td>23.5</td><td>100</td><td>2.50</td></tr></table>

Mainframe non-database systems: Cobol, Easytrieve Plus, CICS and VSAM.  
Mainframe database systems: IDMS, ADS/O, Cobol, and Easytrieve Plus.  
Mainframe Of ce System: Rexx.  
Client server Systems: Window/SQL and C.  
Independent PC Systems: Database IV and Pascal.

Project duration is yet another factor which is found to affect the calibration of a productivity indicator. In ECHO, software projects usually span many months or years. FPs are computed after the project completion and the productivity measured is treated as the productivity at the time of measurement. In fact, the productivity measured is the average productivity during the duration of the entire project. Of the 244 tasks used to compute the 1991 productivity indicator, 55 (22.5%) of them started in 1990. On the other hand, 72 (29.5%) of the 1992 projects did not complete in the same year and their productivity performances are included in subsequent years’ FPPI. A good productivity indicator has to consider this time factor. A  uctuating FPPI, to a large extent, is caused by its de nitions. Being a year-to-date indicator, it  uctuates more at the beginning of a year as its value is determined by only a few completed projects. As more projects are included in the computation of the FPPI in the year, the  uctuations decrease. This can be seen in the later parts of the 1991 and 1992  gures (Figure 4). The 1990 FPPI  uctuated throughout the year mainly due to fewer projects and probably inaccuracy in FP computation during the initial implementation. In summary, the productivity indicator has to be carefully calibrated and its implications studied before it can be interpreted correctly.

## Rigour of the measurement process

Having an in-depth knowledge of FPA and an appropriately calibrated productivity indicator is necessary but not suf cient for implementing a successful measurement programme. The measurement process has to be rigorous enough to ensure that the data collected are accurate.

Users in ECHO are not involved in FP computation. FPs are computed by the IS project leader based on technical documentation. Since FPA measures the value a user obtains from an application, its accuracy depends on the ability of the project leader to identify the various FPA components from users’ perspectives. We argue that such perspectives have to be obtained from user documentation or the users themselves. The use of technical documentation and lack of a user’s involvement in the FPA computation process results in the loss of some user perspectives and the inclusion of technical perspectives. Commonly found technical perspectives included in the computation are system control data and the most commonly missing user perspectives are relationships between data elements of different record types and multiple usage of screens and reports. Identifying and understanding a user’s perspectives have always been and will always be a challenge to IS people in application development and in this case measuring the values delivered to users.

An FPPI can only be as accurate as the data used to compute it. However, an analysis of the FPA database found irregular data. Sixty-one (4.8%) completed tasks had no man-days recorded, 33 (2.6%) completed tasks had no completion date which makes it impossible to identify the period of measurement and 17 (1.3%) tasks were non-application tasks which should not be in the database in the  rst place. These irregularities in the data suggest that there is insuf cient rigour in the measurement process.

The 14 GACs in FPA are meant to adjust for the different technology characteristics between applications. However, our analysis of the data found that the general characteristics adjustments (GCAs) for applications on similar technology platforms were sparse (Table 6). While some differences between applications on the same platform are expected, the differences should not be great. In this case, the range between the minimum and maximum GCAs on the same platform was between 27.9% for the mainframe database system and 74.7% for the client server system. At the individual GAC level, the greatest disparity comes from data communication, performance, on-line

Table 5 Dominant application characteristics of departments

<table><tr><td rowspan="2">Department</td><td colspan="5">Application characteristics</td><td rowspan="2">Productivity (FP/man-day)</td></tr><tr><td>HL (%)</td><td>HH (%)</td><td>LL (%)</td><td>LH (%)</td><td>Total (%)</td></tr><tr><td>A</td><td>72.3</td><td>4.1</td><td>14.1</td><td>9.5</td><td>100</td><td>1.79</td></tr><tr><td>B</td><td>73.6</td><td>2.6</td><td>16.0</td><td>7.8</td><td>100</td><td>1.34</td></tr><tr><td>C</td><td>3.4</td><td>7.2</td><td>33.7</td><td>55.7</td><td>100</td><td>2.50</td></tr></table>

HL: high complexity and integration and low output types.  
HH: high complexity and integration and high output types.  
LL: low complexity and integration and low output types.  
LH: low complexity and integration and high output types.

## Software engineering productivity measurement

data entry and design for end-user ef ciency with standard deviations above 2 on a scale of 0–5. These GACs should not vary much for the same technology platform. This is notwithstanding that two persons, a supervisor and the SME, review the GACs. Interviews with seven supervisors suggested that their reviews are not effective for three reasons: (1) they are not trained in review of the 14 GACs, (2) there are no common guidelines and (3) they may not be objective as their subordinates’ productivity performance contributes to their own performance. The last point is consistent with prior studies showing that FPA computation may be political (Low and Jeffrey, 1990; Subramanian and Lacity, 1997). These  ndings highlight the importance of managing the in uence of human factors on FPA.

As regards to training in FPA, ECHO’s IS staff attend a 1-day in-house FPA course conducted by the SME. Nine staff who had attended the latest FPA course were asked to rate their con dence level in using FPA on a scale of 1 (not con dent) to 5 (very con - dent). The eight responses received gave a mean score of 2.13 with 2.5 being the highest score and 1.0 being the lowest score. The below 3 rating suggests that the training has not prepared the staff for FP computation adequately. This is consistent with Low and Jeffery’s (1990) study that it is unlikely that an FP analyst can be pro cient in counting FP immediately after a training course.

Counting standards are found to improve consistency in FP counting. ECHO has 45 in-house counting rules for database applications (four for Internal Logic File (FT), three for External Interface File (EI),  ve for External Input (IT), 21 for External Output (OT) and 12 for External Inquiry (QT) and 12 rules for window applications. These standards have helped department B, which mainly develops database applications, to achieve more consistent productivity measurement patterns than the other two departments (Figure 4). In the treatment of zero-FP tasks, our analysis of the 1992 and 1993 tasks showed that, among the 180 (23.4%) zero-FP tasks, 54% arose from re nements to business policies and procedures in terms of logic changes, 8% were due to changes in technology such as software upgrades and 3% were corrective actions. Twenty-seven per cent of them were doubtful cases because whether they yield any FPs depends on an individual’s interpretation. For example, when there is extensive cloning of a task, treating it as a new entity will yield many FPs but treating it as a change to the existing task will yield zero FPs. The remaining 8% were mainly nonapplication tasks. ECHO has no written standards on how these tasks should be treated and it was left to an individual’s judgement which leads to inconsistencies in measurement. In summary, the organizational and human factors are as important as the technical know-how of FP computation in productivity measurement.

## Learning points

This case study suggests that a good knowledge of FPA is fundamental to a successful FPA productivity programme (Figure 5). Such knowledge should go beyond the basic de nitions of FPA. Participating in user groups such as the IFPUG and related conferences would help organizations to keep abreast of the latest developments. More importantly, a good knowledge of FPA would help calibrate an FPPI which meets the measurement objectives. As we saw from the case of ECHO, calibrating the productivity indicator needs to take into account the in uence of the application, technology and project characteristics. Last but not least, the measurement process has to be rigorous enough to achieve good quality of measurement. It is important to take into account organizational and human factors such as political interest, the competency of staff, counting standards and a user’s perspectives in the measurement process. Although the same level of methodological rigour of academic research cannot be expected in the industry, its total absence is likely to cause a measurement programme to fail. Productivity measurement is an expensive investment; it should be implemented correctly and effectively. It requires management attention to ensure that the measurement programme works effectively and meets its objectives.

Table 6 GCAs across technology platforms

<table><tr><td>Technology platforms</td><td>Minimum</td><td>Maximum</td><td>Mean</td><td>SD</td></tr><tr><td>Mainframe non-database systems(Cobol, Easytrieve Plus, CICS and VSAM)</td><td>0.65</td><td>1.02</td><td>0.80</td><td>0.11</td></tr><tr><td>Mainframe database systems(IDMS, ADS/O, Cobol and Easytrieve Plus)</td><td>0.86</td><td>1.10</td><td>0.99</td><td>0.08</td></tr><tr><td>Mainframe office system (Rexx)</td><td>0.65</td><td>1.08</td><td>0.87</td><td>0.13</td></tr><tr><td>Client server system (Window/SQL and C)</td><td>0.75</td><td>1.31</td><td>0.97</td><td>0.18</td></tr><tr><td>Independent PC system (Database IV and Pascal)</td><td>0.65</td><td>0.92</td><td>0.83</td><td>0.09</td></tr></table>

![](/api/attachments/C3QK4DT3/fulltext/images/5afa2a2a019dc1839a8fb69d4de3f47aeb840ced03e95e291fa564a3a0c65807.jpg)  
Figure 5 Factors in uencing an FPA productivity measurement programme

More research is required on the issues involved in using FPA for measuring ef ciency at the project level, its effectiveness as an IS function and bottom line measurement at the business level as proposed by Dale and Zee (1992). IS departments are looking beyond project level measurement to productivity measures at the departmental level for planning, organizing, training and rewarding purposes. With human capabilities being the most signi cant software driver attribute, a composite manpower productivity indicator is needed. It is not suf cient to explain that one project has higher productivity because of the technology, application or project characteristics. IS departments want to assess the productivity of their people and to reward them accordingly. This has to take into consideration the wide range of activities which includes IS planning, application development, systems maintenance, user support and diversities in technology platforms and projects. It will be useful for future research to investigate how a common metric can be calibrated to measure staff productivity across projects of different characteristics and to identify the data elements required to help identify the areas for productivity improvement.

## Conclusion

Organizations which implement FPA may be unaware of many of the ongoing developments in FPA. In the case of ECHO, its knowledge was limited to the original FPA theory. Many of its problems with FPA stemmed from its limited access to the latest developments of FPA.

Implementing a software engineering productivity measurement programme is more than a technical task. In addition to good knowledge of FPA, organizations must acquire the expertise for calibrating a productivity indicator which is valid for the measurement objectives. Otherwise the indicator will confuse rather than clarify the productivity performance of the organization, as in the case of ECHO. Last but not least, the measurement process must be rigorous enough to ensure that accurate data are collected and correctly analysed.

## Acknowledgements

The authors are grateful to the anonymous reviewers for their helpful comments on the  rst draft of this paper and to Professor John Sharp for his insightful comments on an earlier version of the research, a working paper submitted as part of the requirements of Henley Management College’s DBA programme.

## References

Abran, A. and Robillard, P.N. (1994) Function points: a study of their measurement processes and scale transformations. Journal of Systems and Software, 25(2), 171–84.

Albrecht, A.J. (1984) AD/M Productivity Measurement & Estimate Validation (IBN CIS and A Guidel).

Banker, R.D., Kauffman, R.J., Wright, C. and Zweig, D. (1994) Automating output size and reuse matrices in a repository-based computer-aided software engineering environment. IEEE Transactions on Software Engineering, 20(3), 169–87.

Bock, D.B. and Klepper, R. (1992) FP-S: a simpli ed function point counting method. Journal of Systems and Software, 18(3), 245–54.

Boehm, B.W. (1981) Software Engineering Economics (Prentice Hall: Englewood Cliffs, NJ).

Carlyle, R.E. (1987) High cost, lack of standards is slowing pace of CASE. Datamation, 33(16), 23–4.

Cote, V., Brurgue, P., Oligny, S. and Rivard, N. (1988) Software Metrics: an overview of recent results. Journal of Systems and Software, 8(2), 121–31.

Dale, C.J. and Zee, H.V.D. (1992) Software productivity metrics: Who needs them? Information and Software Technology, 34(11), 731–8.

Software engineering productivity measurement

Davis, D.B. (1992a) Does your IS shop measure up? Datamation, 27–33.

Davis, D.B. (1992b) Develop applications on time, every time. Datamation, 85–8.

Douglass, D.P. and Walsh, L. (1993) The cost and bene ts of CASE. I/S Analyzer, 31(6).

Dreger, J. B. (1989) Function Point Analysis (Prentice Hall: Englewood Cliffs, NJ).

Graziano, A.M. and Raulin, M.L. (1997) Research Methods: A Process of Inquiry (Addison-Wesley: New York).

Hetzel, B. (1993) Making Software Measurement Work: Building an Effective Program (QED: Boston).

Jeffery, D.R., Low, G.C. and Barnes, M. (1993) A comparison of function point counting techniques. IEEE Transactions on Software Engineering, 19(5), 529–32.

Johnson, J.R. (1989) The Software Factory (QED Information Sciences: Wellesley, Mass.).

Jones, C. (1991) Applied Software Measurement: Assuring Productivity and Quality (McGraw Hill: New York).

Kemerer, C.F. (1993) Reliability of Function Points Measurement: A Field Experiment. Communications of The ACM, 36 (2), 85–97.

Kemerer, C.F. and Porter, B.S. (1992) Improving the reliability of function point measurement: an empirical study. IEEE Transactions on Software Engineering, 18(11), 1011–24.

Kitchenham, B. and P eeger, S.R. (1995) Towards a framework for software measurement validation. IEEE Transactions on Software Engineering, 21(12), 929–43.

Lee, A. (1989) Scienti c methodology for MIS case studies, MIS Quarterly, 13(1), 33–52.

Low, G.C. and Jeffery, D.R. (1990) Function points in the estimation and evaluation of the software process. IEEE Transactions on Software Engineering, 16(1), 64–71.

Martin, J. (1991) Rapid Application Development (Maxwell Macmillian International: New York).

Matson, J.E., Barrett, B.E., and Mellichamp, J.M. (1994) Software development cost estimation using function points. IEEE Transactions on Software Engineering, 20(4), 275–87.

Pressman, R.S. (1987) Software Engineering (McGraw-Hill).

Subramanian, A. and Lacity, M.C. (1997) Determinants of variability in function point estimates. Journal of End User Computing, 9(4), 19–28.

Symons, C.R. (1988) Function point analysis: dif culties and improvements. IEEE Transactions on Software Engineering, 14(1), 2–11.

Tate, G. and Verner, J.M. (1991) Approaches to measuring size of application products with CASE tools. Information and Software Technology, 33(9), 622–8.

Treble, S. and Douglas, N. (1995) Sizing and Estimating Software in Practice: Making MKII Function Points Work (McGraw Hill: London).

Verner, J.M. and Tate, G. (1987) A model for software sizing. Journal of Systems and Software, 7(2), 173–7.

Wrigley, C.D. and Dexter, A.S. (1991) A model for measuring system size. MIS Quarterly, 15(2), 245–57.

Yin, R.K. (1984) Case Study Research: Design and Methods (Sage Publications, Beverly Hills, CA).

Yourdon, E. (1992) Decline & Fall of the American Programmer (Yourdon Press: Englewood Cliffs, NJ).

## Biographical notes

Hai Suan Bok, DBA, is an IS manager with a large information technology services company. He has worked in the information technology industry for 14 years in software development, software engineering methodology and productivity, project management, IS planning and architecture, consultancy and network management. His current research interests include IS management, software productivity, IS value and knowledge management.

K. S. Raman, PhD, CEng, is an adjunct associate professor in the Department of Information Systems, School of Computing, National University of Singapore. Prior to this, he was senior fellow and coordinator of the IS area of the school. He has published widely in the IS  eld and is included in the list of top researchers recently published in Decision Line. He has served on the editorial board of MIS Quarterly and is presently on the editorial board of Information Technology for Development. Raman has extensive experience in industry in planning, design, implementation and management of enterprise IS as IS manager and chief information of cer. He has consulted for large corporations and government agencies.

## Appendix: An FP metric

What is an FP? An FP is a measure of work product. Each FP can also be seen as a unit of measurement of the complexity of an application or an end-user business function. It is determined by the components relating to information processing (Figure 6) – input, output, inquiry,  le, interface  le and the 14 GACs. There are three types of FPs – development FPs, enhancement FPs and support FPs. The value of an FP is in uenced by the number of  le types (FTR), record types (RET) and data element types (DET) referenced by an application. Hence, the more  le types, record types and data types an application uses, the more FPs the application delivers.

Computation of FPs consists of  ve main steps. The  rst step consists of determining the external boundary for the application. This is followed by identifying the major data and transactional function types from the perspectives of the users. These include external input types (IT), external output types (OT), logical internal  le types (FT), external interface  le types (EI) and external inquiry types (QT). Next, for each of the function types, the complexity level of information processing is determined by the number of FTRs, RETs and DETs the application refers. An unadjusted function count (FC) is computed using Equation 1.

![](/api/attachments/C3QK4DT3/fulltext/images/665fb93f1789c4c0782589d99ea3a60b90f9b8df2d348ec68b4f55e9a6c09ea0.jpg)  
Figure 6 FP concept

$$
\mathrm{FC} = \sum_ {i = 1} ^ {5} \sum_ {i = 1} ^ {3} W _ {i j} Z _ {i j}\tag{1}
$$

In this equation, $\boldsymbol { W } _ { i j }$ is the  xed weightage assigned to each of the function types and $Z _ { i j }$ is the count for each function type i at complexity level j.

In the fourth step, the FC is adjusted by the 14 $\mathrm { G A C s }$ . Each characteristic $C _ { i }$ is to be rated between 0 and 5. The sum is called general characteristics (GC) in Equation 2.

$$
\mathbf {G C} = \sum_ {i = 1} ^ {1 4} C _ {i}\tag{2}
$$

The GCA is derived by

$$
\mathrm{GCA} = 0. 6 5 + (0. 0 1 \times \mathrm{GC})\tag{3}
$$

Lastly, the total FPs after adjustment are computed by

$$
\mathrm{TotalFP=FC} \times \mathrm{GCA}\tag{4}
$$

The GC has a minimum value of 0 and a maximum value of 70 (14 3 5); hence, the range of GCAs is 0.65–1.35. The 0.65 in Equation 3 sets the limits of the impact of GCAs on the total FPs. When ${ \mathrm { G C } } = 0 ,$ the GCA has a minimum value of 0.65. Hence, it is able to reduce the FC by a maximum of –35% in Equation 4. When the GC has the maximum value of $^ { 7 0 , }$ the GCA has a value of 1.35. Hence, it is able to increase the FC by a maximum of +35% in Equation 4. Hence, the total impact of the 14 GACs on the total FPs is +/–35% or 70% as a whole.

FPs can be used as a measure of output from an IS department. It measures productivity by computing output (in FPs) over input (in man-days or dollars). The quality of an information system can be measured by the number of defects per 1000 FPs.

Address for correspondence: Hai Suan Bok, 5 Tanah Merah Kechil Road, 17–06, Singapore 466665.
