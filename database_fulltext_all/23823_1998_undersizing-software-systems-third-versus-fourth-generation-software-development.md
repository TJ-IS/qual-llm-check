---
otero_id: 23823
otero_key: "ZXFWKJ8N"
title: "Undersizing software systems: third versus fourth generation software development"
authors: "M R Lind; J M Sulek"
year: "1998"
journal: "European Journal of Information Systems"
doi: "10.1057/palgrave.ejis.3000308"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Undersizing software systems: third versus fourth generation software development

MR Lind and JM Sulek

School of Business and Economics, NCA&T State University, Merrick Hall, Greensboro, NC 27411, USA

A critical component of information systems (IS) project management is completing projects on time; however, most software development efforts have completion time overruns. This study examines the prior research in IS project management for assessing the completion time for new software development projects and discusses a project management phenomenon where the expected time for project completion is undersized. At one firm two groups of software development projects are examined: (1) Cobol projects (third generation) and (2) Natural (fourth generation). It was found that both the Cobol and Natural projects experienced similar overruns. Undersizing is posited as the explanation.

## Introduction

While firms have experienced significant improvement in the price/performance ratio for computing hardware in recent years, there has not been a corresponding improvement in the price/performance ratio for software development (Itakura & Takayanagi, 1982; Abdel-Hamid & Madnick, 1989; Cusamano & Kemerer, 1990; Munson & Khoshgoftaar, 1990). To increase software development productivity, many firms are seeking ways to better manage their software development projects. Although most information systems (IS) departments track hours expended by IS workers on system development projects, many managers still have problems accurately predicting labour requirements and completion dates for software development projects and many IS projects are completed overschedule and overbudget. In this study, the problem of software project overruns will be examined for software developed using a fourth generation development tool (Natural) as compared to a third generation development tool (Cobol).

## Software project estimation

In the past, assessment of software development projects has centred around two approaches: (1) software engineering and (2) the group behavioural aspects of software development. Neither approach has been completely accurate nor reliable for estimating software project completion time. Pfleeger (1991) found that current software estimation tools using complexity metrics were only successful 75% of the time at estimating project duration within 25% of actual project time. Behaviouralbased methods for estimating software completion, which rely primarily on the judgement of the lead analysts, lack the rigour of algorithmic techniques; empirical studies involving these methods are rarely found in the literature.

As shown in Table 1, much software engineering work has been devoted to the development of software metrics—real time software metrics, data structure complexity metrics, systems design metrics, CASE metrics, entity metrics, function point analysis, etc. Despite extensive research on software development measures, these metrics have not been widely applied in practice. Table 2 shows that there have been relatively few studies which focus on the use of these metrics in the workplace. MacDonell (1994, p 141) states, “The lack of widespread industry acceptance of much of the research into the measurement of software complexity must be due at least in part to the lack of experimental rigour associated with many of the studies.” MacDonell elaborates on this problem by discussing: (1) the post hoc nature of much of this research (which lacks a planned research design for hypothesis testing); (2) the use of surrogates for attributes that need to be measured directly; (3) the absence of experimental techniques which reflect actual software development environments in which programmers work with code over long periods of time; (4) the subjective evaluation required by some of the metrics used; (5) the difficulty in obtaining accurate software development project management data from programmers; (6) the use of unrealistically small software programs or small sample size; (7) reliance on student programmers; (8) the lack of statistical validation of the metrics used; and (9) the lack of precision in the presentation of results which may lead to incorrect result interpretation.

Table 3 summarises the comparative and critical literature on software metric development. Kemerer (1991) showed that existing algorithmic methods in most cases do not provide accurate forecasts of development effort. In a later study, Kremerer (1993) found that function point analysis, which incorporates expert judgement of software managers, possesses high inter-rater reliability. However, Vincinza et al (1991) demonstrated that software managers produce better project completion estimates using intuition and judgement than by using function point analysis.

Table 1 Development of software metrics

<table><tr><td>Authors</td><td>Title</td><td>Focus</td></tr><tr><td>Cook &amp; Roesch (1994)</td><td>Real-time software metrics</td><td>Describes the software metrics analysis of real-time telephone switching systems using standard software complexity metrics and information flow metrics</td></tr><tr><td>Khoshgoftaar et al (1994)</td><td>Alternative approaches for the user of metrics to order programs by complexity</td><td>Compares the Halstead and McCabe cyclomatic complexity metrics and derives a relative complexity metric</td></tr><tr><td>MacDonell (1994)</td><td>Comparative review of functional complexity assessment methods for effort estimation</td><td>A review of the complexity metrics—bang metrics, bang metric analysis (BMA), CASE size metrics, entity metrics, function point analysis, information engineering, Mark II FPA, metric guided methodology, and usability measures</td></tr><tr><td>Olsen (1993)</td><td>The software rush hour</td><td>Estimates of time to make changes in software projects using fluid-approximation model</td></tr><tr><td>Zage &amp; Zage (1993)</td><td>Evaluating design metrics on large-scale software</td><td>Developed and tested design metrics to be used to predict potential system quality and complexity</td></tr><tr><td>Weller (1993)</td><td>Lesson from three years of inspection data</td><td>Used defect inspection data to control process quality in software development projects</td></tr><tr><td>Munson &amp; Kohshgoftaar (1993)</td><td>Measurement of data structure complexity</td><td>Introduce a new software complexity metric based on the data structure complexity</td></tr><tr><td>Damerla &amp; Shatz (1992)</td><td>Software complexity and Ada rendezvous: metrics based on nondeterminism</td><td>Proposes metrics for concurrent and distributed software systems, specifically of Ada tasking programs</td></tr><tr><td>McColl &amp; McKin (1992)</td><td>Evaluating and extending NPath as a software complexity measure</td><td>Compared the complexity metric Npath to existing complexity metrics</td></tr><tr><td>Khoshgoftaar et al (1992)</td><td>Predictive modeling techniques of software quality from software measures</td><td>A study of four estimation techniques in the development of regression models for software complexity metrics: linear regression modelling, relative least squares, and minimum relative error procedures</td></tr><tr><td>Kemerer (1991)</td><td>Software cost estimation models</td><td>Discusses models for estimating software development effort</td></tr><tr><td>Redmond &amp; Ah-Chuen (1990)</td><td>Software metrics—a user&#x27;s perspective</td><td>Discusses the SCMT prototype metric tool and the concept of justifiable complexity</td></tr><tr><td>Munson &amp; Khoshgoftaar (1990)</td><td>Applications of a relative complexity metric for software project management</td><td>Develops the relative complexity metric and shows that for a set of software programs it may show which programs will need more resources in development</td></tr><tr><td>Ince &amp; Shepperd (1988)</td><td>System design metrics: a review and perspective</td><td>Review of research for systems design metrics</td></tr></table>

The behavioural stream of software development literature emphasises the importance of group processes (Table 4) in software project management. The behavioural approach to software development was initiated by Brooks (1975) in the Mythical Man Month in which he described software development as a collaborative process involving complex human interrelationships which are not easily modelled through quantitative techniques. Brooks (1975) found that just adding software development people to a project did not lead to associated reductions in time needed to finish the project. Later research on group processes in software development supported Brooks’ finding by showing that software team productivity was affected by a number of behavioural issues including: governance techniques (Beath, 1983), conflict resolution (Hirschheim et al, 1987), effective time management (Olsen, 1993; Ward, 1994), and the designer/user interaction (Robey et al, 1989). The critical role of designer/user communication in software project management is stressed in Lederer and Prasad’s (1992) study which showed that IS managers listed ‘frequent requests for changes by users’ as the top reason for systems development overrun. While the behavioural IS literature provides little guidance for predicting finish times for software development projects, it does suggest that accurate forecasts of project completion times require careful interpretation of qualitative variables which reflect the project context.

Table 2 Using complexity metrics in the workplace

<table><tr><td>Authors</td><td>Title</td><td>Focus</td></tr><tr><td>Cusumano &amp; Kemerer (1990)</td><td>A quantitative analysis of US and Japanese practice and performance in software development</td><td>Comparison of complexity metrics for software development between the US and Japan</td></tr><tr><td>Bowman &amp; Newman (1990)</td><td>Software metrics as a programming training tool</td><td>Complexity metrics were used as a programmer training tool and resulted in programs with less coding and testing time and higher reliability</td></tr><tr><td>Henry &amp; Lewis (1990)</td><td>Integrating metrics into a large-scale software development environment</td><td>Presents an experiment that introduces a non-disruptive method for integrating metrics into a large-scale commercial software development environment</td></tr></table>

Table 3 Comparative and critical research on complexity metrics

<table><tr><td>Authors</td><td>Title</td><td>Focus</td></tr><tr><td>Jeffrey et al (1993)</td><td>A comparison of function point counting techniques</td><td>To estimate project size, the SPQR/20 function point method was compared to traditional function point analysis and little difference was found</td></tr><tr><td>Kemerer (1993)</td><td>Reliability of function point measurement: a field experiment</td><td>Found in a large-scale field experiment sufficiently high inter-rater and inter-method reliability of the function point approach</td></tr><tr><td>Mata-Toledo &amp; Gustafson (1992)</td><td>A factor analysis of software complexity measures</td><td>Used factor analysis to analyse software measures and determine the factors that influence variability in measures</td></tr><tr><td>Kemerer &amp; Porter (1992)</td><td>Improving the reliability of function point measurement: an empirical study</td><td>Showed factors that affect function point reliability and made recommendations</td></tr><tr><td>MacDonnell (1991)</td><td>Rigor in software complexity measurement experimentation</td><td>Discusses the lack of rigour in many software complexity studies</td></tr><tr><td>Vicinanza et al (1991)</td><td>Software-effort estimation: an exploratory study of expert performance</td><td>Compared the expert judgement of five software managers to function points and COCOMO and found that the managers made better estimates</td></tr><tr><td>Kemerer (1987)</td><td>An empirical validation of software cost estimation models</td><td>Showed that existing algorithmic models in most cases do not produce accurate estimates of development effort</td></tr><tr><td>Jones (1978)</td><td>Measuring programming quality and productivity</td><td>Discusses the problems with the unit of analysis used to assess program quality and programmer productivity</td></tr></table>

Further exacerbating the problem of estimating project completion time is the pressure to develop software within compressed time frames (Abdel-Hamid & Madnick, 1989). Schedule compression is the percentage to which the schedule for the project is cut given the time originally forecast for the project (Boehm, 1981). One method of schedule compression is undersizing the projected completion time for the software project (Abdel-Hamid & Madnick, 1989). Undersizing may be the result of a conscious effort to speed up the project or it may result from the inability of the systems analyst to estimate project completion time correctly due to a lack of understanding of the software’s needed complexity or the behavioural dynamics of the software development team that will develop the software. In the following section, the basis of project undersizing is discussed.

Table 4 Group processes in software development groups

<table><tr><td>Article</td><td>Title</td><td>Focus</td></tr><tr><td>Ward (1994)</td><td>Productivity through project management</td><td>Non-empirical discussion of achieving systems development productivity through better project management of work, resources, and time</td></tr><tr><td>Perry et al (1994)</td><td>People, organizations, and process improvement</td><td>Reported on two experiments of how developers spend their time describing wasted time on non-coding activities and the use of email primarily for non-technical activities</td></tr><tr><td>Robey et al (1989)</td><td>Group process and conflict in system development</td><td>Examined the influence relationship between developers and users</td></tr><tr><td>Weitzel &amp; Graen (1989)</td><td>System development project effectiveness: problem-solving competence as a moderator variable</td><td>Researched the IS manager/user relationship for 75 projects and found the relationship complex</td></tr><tr><td>Hirschheim et al (1987)</td><td>A social action perspective of information systems development</td><td>Examined conflict resolution strategies between developers and users</td></tr><tr><td>Beath (1983)</td><td>Strategies for managing MIS projects: a transaction cost approach</td><td>Showed that I/S project managers need to use governance techniques that depend on the project&#x27;s characteristics (complex projects—more involvement; simple projects—emphasise outcomes).</td></tr><tr><td>Brooks (1975)</td><td>The mythical man-month</td><td>Showed that merely adding people to a programming team did not result in the software project finishing on time—mythical man month</td></tr><tr><td>Mills (1971)</td><td>Chief programmer teams: principles and procedure</td><td>Proposed the use of the chief programmer in a programming team</td></tr><tr><td>Weinberg (1971)</td><td>The psychology of computer programming</td><td>Introduced the concept of egoless programming</td></tr></table>

## Project undersizing

The review of the software project estimation literature shows that much effort has been expended in this area with little success. Kahneman et al (1985, p 48) explain this lack of success by stating: “In making predictions and judgements under uncertainty, people do not appear to follow the calculus of chance or the statistical theory of prediction. Instead, they rely on a limited number of heuristics which sometimes yield reasonable judgements and sometimes lead to severe and systematic errors (Kahneman & Tversky, 1972; Tversky & Kahneman, 1971, 1973).” Kahneman and Tversky (1973, p 4) showed that prior probabilities on outcomes are properly used when no other evidence is given to those making predictions, but when worthless evidence is given, the prior probabilities are ignored. Thus people are generally insensitive to prior probability of outcomes. Further Kahneman and Tversky (1972, p 3) showed that respondents failed to consider sample size in making predictions of the average height of men for samples of 1000, 100, and 10 men. Also respondents had misconceptions of chance and would make predictions on samples that were too small (Tversky & Kahneman, 1971, 1973).

Given the pervasiveness of project overruns for software development, this study seeks to determine if project overruns will be affected by the type of software development tool used. Since fourth generation languages are expected to make software developers more productive as compared to third generation development in languages such as Cobol, fourth generation languagebased projects should in most cases be completed on time. However, another factor affecting completion on time is the accuracy of the initial projection for project completion time. Thus if a project is undersized in the original projection even with fourth generation development tools there will be a project overrun.

The phenomena of undersizing is difficult to measure directly, and in many cases IS managers may be reluctant to admit that their systems analysts are undersizing software development projects. The rationale for undersizing may be to spur the IS staff to work faster or it may lie with project approval. An undersized project that estimates using fewer resources in a shorter time frame may receive quicker management approval than a ‘rightsized’ one. While many studies (Table 4) have examined the effect of software project overrun in terms of problems with the various stages of the systems life cycle and with changing users requirements, this study will examine the influence of undersizing.

It is proposed that, because of undersizing, software projects developed with fourth generation tools will experience project overruns as do software projects developed with third generation tools. The assumption is that an important issue in project overrun is project undersizing. Undersizing will result in project overruns for software developed using fourth generation tools even with the increased software development productivity afforded by them. It is thus hypothesised that:

Software project overruns using fourth generation tools will not significantly differ from software project overruns using third generation tools.

## Research context

The software development projects at one firm will be used to examine the undersizing issue. Since these software projects were developed within the same IS department, the analysts and programmers experienced similar organizational pressures and expectations in their project development and estimation efforts. This IS department used the fourth generation tool Natural and the third generation tool Cobol for software development. The staff (analysts, programmers, and management) worked very closely together, with their offices in close proximity. While this controlled context does limit generalisability of these results, it provides an opportunity to determine if there will be a significant difference in overrun for software projects developed with the different tools. These projects were of comparable size for new systems development (comparison of the mean projected project completion time for the Cobol projects was not significantly different from the mean of the projects using fourth generation level tools.) Two sets of projects will be examined: (1) those completed, and (2) those in process.

## Analysis of the projects

As part of this firm’s project management effort, an assessment of efficiency was made. The efficiency of each project was determined by dividing earned hours by the actual hours expended on the project. Every two weeks the project management team determined the number of hours earned on the project. Hours earned were based on the project objectives that were accomplished in that two-week period. Thus if the actual hours were more than hours earned then the software development effort was not completely efficient and conversely if actual hours were less than hours earned. Variance in this efficiency metric could be due to the type of software development tool used, or it could be attributable to the skill level of the employees or other organizational factors. Table 5 shows that the mean level efficiency rating indicated that Cobol was less efficient than Natural but there was not a significant difference across the two types of projects for both projects completed and for projects in process. The finding that the fourth generation tool Natural did not have a significantly higher efficiency rating than Cobol is counterintuitive, but Misra and Jalics (1988) have produced similar findings which may in this case be attributable to these employees’ greater familiarity with Cobol. Natural had been in place a little over a year at this firm when this data was collected.

For the completed projects, the percentage of project overruns was determined by dividing the difference between the actual number of person hours worked on each project, less the original projection for that project, by the original projection. While the means in Table 5 show that on average both the Cobol and the natural projects experienced overruns, there was not a significant difference between these percentage project overruns for the third generation software projects as compared to the fourth generation software projects.

For the software projects in process, every two weeks the project manager would update the estimated time to completion for the project. For these in process projects this estimated time to completion was added to the actual time booked on the project so that the percentage project overrun could be calculated. Table 5 shows that there is still not a significant difference between the percentage project overrun for the third generation software projects as compared to the fourth generation software projects for the projects in process. The project managers are still predicting that these projects will be completed ahead of schedule. This is the case even though the efficiency ratings are comparable to those for the completed projects.

Finally logistic regression was used to determine how well the overrun and efficiency metric predicts placement in either of the two groups of software projects (third generation, Cobol; and fourth generation, Natural). Table 6 shows the two analyses: (1) for the completed projects, and (2) for the in process projects. The logistic regression model for the completed projects showed an acceptable goodness of fit while this was not the case for the projects in process.

Table 5 T-tests of third generation versus fourth generation software project management metrics

<table><tr><td></td><td>Completed Projects</td><td>Inprocess Projects</td></tr><tr><td>Variable</td><td>Mean(Std)</td><td></td></tr><tr><td colspan="3">Efficiency</td></tr><tr><td>third generation</td><td>0.92 (0.27)</td><td>0.98 (0.18)</td></tr><tr><td>fourth generation</td><td>1.12 (0.19) NS</td><td>1.09 (0.27) NS</td></tr><tr><td colspan="3">Percentage overrun</td></tr><tr><td>third generation</td><td>1.21 (0.34)</td><td>0.88 (0.23)</td></tr><tr><td>fourth generation</td><td>1.17 (0.32) NS</td><td>0.96 (0.31) NS</td></tr><tr><td>n</td><td>43</td><td>22</td></tr></table>

\*P,0.05; \*\*P,0.01; \*\*\*P,0.001; NS = not significant.

To explain these results, the software project manager at this firm was interviewed. So as not to bias the qualitative feedback, no mention was made of the undersizing hypothesis. The manager was asked to identify the factors that resulted in project overrun for the third and fourth generation software projects. Invariably the two reasons given were programmer turnover and project definition changes. When this manager was asked if these factors were accounted for in the original estimates, the manager responded that they were but that they were always under pressure from management to improve the productivity of the IS unit. This manager acknowledged that the project estimates succumbed to this pressure but he never said that the undersizing was done to ensure the approval of new projects.

## Discussion

The logistic results indicate that estimates of project completion time and of estimated time to completion for in process projects do not predict project group membership (Cobol or Natural) until projects are completed. This is true even though the effect of the difference in efficiency rating of Cobol versus Natural is controlled in the model.

The software project managers for this research context, by using their first hand knowledge of the software development context in making their projections, “provided subjective evaluations of [contextual] variables that are difficult to measure objectively” (Blattenburg & Hoch, 1990, p 890). Judgemental forecasts such as these are in practice the most widely used method of estimating software completion times (Lederer & Prasad, 1992) despite the availability of software tools for project management.

Table 6 Logit regression dependent variable: 1 if third generation, 2 if fourth generation

<table><tr><td>Logit regression</td><td>Model: completed projects</td><td>Model: projects in process</td></tr><tr><td>Intercept</td><td>-0.12</td><td>0.41</td></tr><tr><td>Percentage overrun</td><td>0.39</td><td>-0.98</td></tr><tr><td>Efficiency</td><td>-0.19</td><td>-0.04</td></tr><tr><td> $\chi^2$ </td><td>15.11***</td><td>0.38 NS</td></tr><tr><td>df</td><td>2</td><td>2</td></tr><tr><td>n</td><td>43</td><td>22</td></tr></table>

\*P,0.05; \*\*P,0.01; \*\*\*P,0.001; NS = not significant.

While the project manager’s intuitive approach to software completion prediction (Vicinanza et al, 1991) provides context knowledge, there are shortcomings to relying on this approach. These shortcomings are generally interrelated and in many cases include: (1) decreased forecaster reliability as prediction task complexity increases, (2) possible exclusion of critical subjective information, and (3) forecaster bias (Kahneman et al, 1985).

The information processing reliability of the individual forecaster can influence the accuracy of a judgemental forecast with forecaster reliability declining as environmental predictability decreases (Camerer, 1981; Brehmer & Brehmer, 1988). As a result, in a rapidly changing software development context, a project manager’s ability to identify and interpret critical forecast cues for estimating completion times may decline. Software projects which are complex, may also overload the project manager with volumes of project management data, further decreasing the manager’s ability to fine tune project completion estimates (Lee & Yates, 1992; Stewart et al, 1992; Stewart & Lusk, 1994). Also software project managers may rely on ingrained heuristics (Klein, 1993) to manage project information; however, these heuristics may not suit the context of the current project. The relative permanence of these heuristics may lead to pervasive bias in the project manager’s forecasts (Bunn & Wright, 1991; Klein, 1993).

In estimation of project completion times, a common type of bias is optimistic bias (Simon, 1957) in which managers’ forecasts “reflect not only what they think will happen but what they hope will happen” (Armstrong, 1985, p 86). Since overconfidence becomes more pronounced as the difficulty of the prediction task increases (Stewart & Lusk, 1994) and software project managers are under time and budget pressure from their management, it is not surprising that completion times are underestimated (Lederer & Prasad, 1992; Gray, 1994).

The effect of prediction bias may intensify as the software project manager becomes more personally involved in the forecast situation and is held accountable for project outcomes (Armstrong, 1985). Thus, for the information processing reasons discussed, the use of judgemental forecasting in predicting software project duration may explain the chronic underestimation of completion time that has characterised software development for large and complex projects. A new approach is needed for forecasting software project finish times that incorporates the best of judgemental and quantitative forecasting. Predictive techniques are needed that produce realistic stretch targets for software completion.

In this research context, project management appears to be undersizing projects whether they are traditional Cobol projects or fourth generation level projects in Natural. While external factors such as personal productivity of the programmer analysts and other organizational distractions cannot be discounted, these results appear to support the paper’s hypothesis that project overruns will occur for both fourth generation and third generation software development. Project management may undersize projects for a number of reasons: (1) to encourage employees to be more productive, (2) to make it easier to get initial project approval, or (3) there just may be an optimistic bias that only the reality of project completion will erase.

## Conclusion

While the context for this study is of limited generalisability, it does provide support for Abdel-Hamid and Madnick’s (1989) findings on project compression and undersizing. This undersizing phenomena poses a dilemma for IS management. Would ‘rightsizing’ projects lead to completing projects on time/on schedule but could the projects have been pushed to be completed more quickly if they had been undersized?

Increasingly IS have become a competitive weapon for firms. Thus developing software in a ‘crunch mode’ is a matter of survival (Boddie, 1987). To meet the time pressures, IS management may try to compress the project’s schedule through increasing staff, by the staff working longer hours, or obtaining software automation tools (Abdel-Hamid & Madnick, 1989). These factors then can lead to IS that fail to meet the needs of the users or can lead to high turnover in IS employees.

Undersizing IS projects is a problem that is hard to assess. It is difficult to identify when it occurs. Undersizing by the project manager may not be a conscious effort but may be the result of a lack of understanding of the complexity of the information system being sized. Thus the greater availability and accessibility of this information for highly analysable tasks will reinforce individuals’ tendency to collect more information than is needed. As Feldman and March (1981) proposed this information gathering is done as a symbol or signal to demonstrate one’s competence masking the underlying estimation biases such as undersizing. While the reaction to undersizing may be to compensate by building more slack into the estimate this may result in a lax work ethic and bloated project estimates that are unlikely to be approved by management. While complexity metrics have been used to estimate the complexity of software, they have not helped predict project completion times. Quantitative, predictive techniques that incorporate both the systems complexity and the behavioural dynamics of team development should help to remove the subjectivity and politics from IS project estimation.

## References

Abdel-Hamid TK and Madnick SE (1989) Lessons learned from modeling the dynamics of software development. Communications of the ACM 32(12), 1426–1438.

Armstrong JS (1985) Long-Range Forecasting from Crystal Ball to Computer. Wiley-Interscience, New York.

Beath CM (1983) Strategies for managing MIS projects: a transaction cost approach. In Proceedings of the Fourth International Conference on Information Systems, Houston, Texas, December 15–17 (DeGross J, Eds), pp 133–147, ACM Publications, Baltimore, Maryland.

Blattenburg R and Hoch S (1990) Database models and managerial intuition: 50% model + 50% manager. Management Science 36(8), 887–899.

Boddie JC (1987) Crunch Model: Building Effective Systems on a Tight Schedule. Prentice-Hall, Englewood Cliffs, NJ.

Boehm BW (1981) Software Engineering Economics. Prentice-Hall, Englewood Cliffs, NJ.

Bowman BJ and Newman WA (1990) Software metrics as a program ming tool. Journal of Systems Software 13, 139–147.

Brehmer A and Brehmer B (1988) What we have learned from thirty years of policy capturing? In Human Judgement: The Social Judgement Theory View (Brehmer B and Joyce C, Eds), pp 213–218, North-Holland, Amsterdam.

Brooks F, Jr (1975) The Mythical Man-Month. Addison-Wesley, Reading, Mass.

Bunn D and Wright G (1991) Interaction of judgmental and statistical forecasting methods: issues and analysis. Management Science 37(5), 501–518.

Camerer C (1981) General conditions for the success of bootstrapping models. Organizational Behavior and Human Decision Processes 27, 411–422.

Cook CR and Roesch A (1994) Real-time software metrics. Journal of Systems Software 24, 223–237.

Cusumano MA and Kemerer CF (1990) A quantitative analysis of

US and Japanese practice and performance in software development. Management Science 36(11), 1384–1406.

Damerla S and Shatz SM (1992) Software complexity and Ada rendezvous: metrics based on nondeterminism. Journal of Systems Software 17, 119–127.

Feldman MS and March JG (1981) Information in organizations as signal and symbol. Administrative Science Quarterly 26, 171–186.

Gray P (1994) How to get gains from technology. Information Systems Management Winter, 88–91.

Henry S and Lewis J (1990) Integrating metrics into a large-scale software development environment. Journal of Systems Software 13, 89–95.

Hirschheim R, Klein H and Newman M (1987) A social action perspective of information systems development. In Proceedings of the Eighth International Conference on Information Systems, Pittsburgh, PA, (DeGross J and Kriebel C, Eds), pp 45–56, ACM Publications, Baltimore, Maryland.

Ince D and Shepperd MJ (1988) System design metrics: A review and perspective. In Proceedings of IEE/BCS Conference on Software Engineering. IEEE CD-Rom Literature Database, pp 23–37.

Itakura M and Takayanagi A (1982) A model for estimating program size and its evaluation. In Proceedings of the 6th International Conference on Software Engineering, IEEE CD-Rom Literature Database, pp 140–149.

Jeffery DR, Low GC and Barnes M (1993) A comparison of function point counting techniques. IEEE Transactions on Software Engineering 19(5), 529–532.

Jones TC (1978) Measuring programming quality and productivity. IBM Systems Journal 17, 39–63.

Kahneman D and Tversky A (1972) Subjective probability: a judgment of representativeness, Cognitive Psychology 3, 430– 454.

Kahneman D and Tversky A (1973) On the psychology of prediction. Psychological Review 80, 237–251.

Kahneman D, Slovic P and Tversky A (1985) Judgment Under

Uncertainty: Heuristics and Biases. Cambridge University Press, Cambridge.

Kemerer CF (1993) Reliability of function point measurement: a field experiment. Communications of the ACM 36(2), 85–97.

Kemerer CF (1991) Software cost estimation models. In Software Engineers Reference Handbook, Chapter 25, Butterworth, Surrey, U.K.

Kemerer CF (1987) An empirical validation of software cost estimation models. Communication of the ACM 30, 416–429.

Kemerer CF and Porter BS (1992) Improving the reliability of function point measurement: an empirical study. MIT Working Paper, July.

Khoshgoftaar TM et al (1992) Predictive modeling techniques of software quality from software measures. IEEE Transactions on Software Engineering 18(11), 979–987.

Khoshgoftaar TM, Munson JC and Lanning DL (1994) Alternative approaches for the use of metrics to order programs by com plexity. Journal of Systems Software 24, 211–221.

Klein JH (1993) Cognitive processes and operational research: a human information processing perspective. Journal of the Oper ational Research Society 45(8), 855–866.

Lederer AL and Prasad J (1992) Nine management guidelines for better cost estimating. Communications of the ACM 25(2), 51–59.

Lee JW and Yates JF (1992) How quantity judgment changes as the number of cues increases: an analytical framework and review. Psychological Bulletin 112, 363–367.

MacDonell SG (1991) Rigor in software complexity measurement experimentation. Journal of Systems Software 16, 141–149.

MacDonell SG 91994) Comparative review of functional complexity assessment methods for effort estimation. Software Engineering Journal May, 107–116.

Mata-Toledo RA and Gustafson DA (1992) A factor analysis of software complexity measures. Journal of Systems Software 17, 267–273.

McColl RB and McKim JC (1992) Evaluating and extending NPath as a software complexity measure. Journal of Systems Software 17, 275–279.

Mills HD (1971) Chief programmer teams: principles and procedures. IBM Rep. FSC 71-5108, IBM Federal Systems Division, Gaithersburg, MD.

Misra SK and Jalics PJ (1988) Third-generation versus fourth-generation software development. IEEE Software July, 9–14.

## About the authors

Mary R Lind received the PhD degree in business administration from the University of North Carolina at Chapel Hill in 1988. Prior to graduate school, she worked for ten years as a systems analyst in the management information systems field. She is currently Asssociate Professor of Management Information Systems in the School of Business and Economics at North Carolina A&T State University. Her current research interests are in the areas of innovation, computer mediated communication channels, and the impact of technology on firm’s performance and service quality. She has published in Organization Science, Management Science, Information Systems Research, Information and Management, IEEE Transactions in Engineering Management, International Journal of Quality and Work Study. Dr Lind is a member of DSI, INFORMS, Academy of Management, and the ACM.

Munson JC and Khoshgoftaar TM (1990) Applications of a relative complexity metric for software project management. Journal of Systems Software 12, 283–291.

Munson JC and Khoshgoftaar TM (1993) Measurement of data structure complexity. Journal of Systems Software 20, 217–225.

Olsen NC (1993) The software rush hours. IEEE Software September, 29–45.

Perry DE, Staudenmayer NA and Votta LG (1994) People, organizations, and process improvement. IEEE Software July, 36– 45.

Pfleeger SL (1991) Software Estimates: The Production of Quality, 2nd edn. Macmillian, NY.

Redmond JA and Ah-Chuen R (1990) Software metrics—a user’s perspective. Journal of Systems Software 13, 97–110.

Robey D, Farrow L and Franz CR (1989) Group process and conflict in system development. Management Science 35, 1172–1191.

Simon H (1957) Models of Man: Social and Rational. Wiley, New York.

Stewart TR and Lusk CM (1994) Seven components of judgmental forecasting skill implications for research and the improvement of forecasts. Journal of Forecasting 13, 579–599.

Stewart TR et al (1992) Effects of improved information on the components of skill in weather forecasting. Organizational behavior and Human Decision Processing 53, 104–107.

Tversky A and Kahneman D (1971) The belief in the law of small numbers. Psychological Bulletin 76, 105–110.

Tversky A and Kahneman D (1973) Availability: a heuristic for judging frequency and probability. Cognitive Psychology 5, 207– 232.

Vicinanza SS, Mukhopadhyay T and Prietual MJ (1991) Software effort estimation: an exploratory study of expert performance. Information Systems Research 2(4), 243–262.

Ward JA (1994) Productivity through project management. Information Systems Management Winter, 16–21.

Weinberg G (1971) The Psychology of Computer Programming. Van Nostrand, Reinhold, NY.

Weitzel JR and Graen GB (1989) System development project effectiveness: problem-solving competence as a moderator variable. Decision Sciences 20, 507–531.

Weller EF (1993) Lessons from three years of inspection data. IEEE Software September, 38–45.

Zage WM and Zage DM (1993) Evaluating design metrics on largescale software. IEEE Software July, 75–81.

Joanne M Sulek received the BS and MA degrees in mathematics from Wake Forest University. She received the PhD degree in operations management from the University of North Carolina at Chapel Hill in 1989. She is currently Associate Professor of Operations Management at the School of Business and Economics at North Carolina A&T State University. Her research interests include technology management, service quality, quality control, and white collar productivity. Her research has appeared in such publications as Management Science, Decision Sciences, Operation Management Review, Work Study, IEEE Transactions in Engineering Management, and the International Journal of Quality & Reliability Management. Dr Sulek is a member of DSI, INFORMS, APICS and OMA.
