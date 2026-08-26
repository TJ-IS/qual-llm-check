---
otero_id: 23580
otero_key: "NTQ9HUAP"
title: "Information systems software cost estimating: a current assessment"
authors: "Albert L Lederer; Jayesh Prasad"
year: "1993"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1993.4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information systems software cost estimating: a current assessment

ALBERT L. LEDERER

Oakland University, Rochester, MI 48309-4401, USA

JAYESH PRASAD

University of Dayton, Dayton, OH 45469-2130, USA

A study of information systems managers and other information systems professionals at 112 different organizations confirmed that information systems software cost estimating is an important concern. Subjects reported the completion of only one of every four systems development projects within their estimates. According to them, the major cause of inaccurate estimates was changes in user requirements. Organizations using sophisticated cost estimating software packages were less successful at preventing large cost overruns than organizations not using them. However, the use of the estimator as system developer, the careful monitoring of systems development projects, and the inclusion in performance evaluations of success in meeting estimates were associated with more accurate cost estimating.

## Introduction

Accurate software development cost estimating is crucial. Underestimated costs may persuade management to develop new systems that later overrun their budgets and fail to achieve their expected return on investment. Extreme overruns may be canceled before completion and thus waste the resources invested in them. Overruns can reduce information systems management's credibility and discourage future user cooperation.

Overestimated costs may persuade management not to develop potentially beneficial systems. When a new system with major benefits is proposed, but estimators predict unrealistically high costs beyond the maximum permitted to cost justify it, management generally declines to approve it and thus loses its potential benefits (Emery, 1971; King and Schrems, 1978). Hence, both underestimates and overestimates can have a significant, deleterious impact (Tate and Verner, 1990). They can thus both cause lost strategic opportunities (Benjamin et al., 1984).

The impact of inaccurate estimating on business practice has been so significant that Businessweek (1988) reported several US information systems development calamities. An Allstate Insurance system initially estimated at US \$8m was begun and then while still incomplete, was re-estimated at US \$100m. A State of Oklahoma project initially estimated at US \$500 000 was later completed at US \$4m. The Businessweek article also reported a Peat Marwick Mitchell & Co. survey that found that 35% of its largest clients admitted major cost overruns.

Despite the prevalence of cost overruns, no study before this one has investigated current cost estimating practice in business and industry. This paper describes a study of the cost estimating practices reported by 112 information systems managers and other information systems professionals. The study sought to better understand the current degree of success of estimating, the influences on it, its process, the causes of inaccurate estimating, and practices associated with greater accuracy.

A current assessment of a practice can be valuable. By understanding cost estimating practices, researchers may be able to identify methods of improving cost estimating accuracy and thus reducing the serious problems of inaccurate estimates. If unable to identify such methods, researchers might at least be better able to suggest avenues for further research to do so.

## Background

Prior research on information systems development cost estimating has largely concentrated on the study of algorithmic techniques. Some of this research has identified factors that are believed to affect information systems development and must therefore be considered while estimating development costs (Benbasat and Vessey, 1980; Boehm, 1984; Boehm and Papaccio, 1986; Mohanty, 1981). These diverse factors include system size and complexity, personnel capabilities and experience, hardware constraints, the use of modern software tools and practices, users' understanding of information systems technology, the volatility of their requirements, and many others.

Most algorithmic methods are based on one or more such factors (Conte et al., 1986). The estimator quantifies each factor based on historical data about past development projects or on intuition and experience (Aron, 1976; Mohanty, 1981). Different methods, however, may define the same factors in different ways. For example, many methods operationalize system size in terms of the projected number of lines of executable code in the proposed system (Boehm, 1984; Conte et al., 1986; Freiman and Park, 1979; Herd et al., 1977; Jensen, 1983; Nelson, 1966; Putnam, 1978; Walston and Felix, 1977; Wolverton, 1974) whereas relatively fewer methods use the number of functions, modules, or program features in the system (Albrecht, 1979; Demarco, 1984; Donelson, 1976; Halstead, 1977; Jones, 1986; McCabe, 1976).

The algorithmic methods utilize these quantified factors to produce an estimate of the proposed system's cost. These methods vary widely in mathematical sophistication. Some use simple arithmetic formulas based on such summary statistics as means and standard deviations (Donelson, 1976) while others employ regression models (Walston and Felix, 1977) and differential equations (Putnam, 1978). Some algorithmic methods are available for use in computer-based software packages. For example, ESTIMACS (Computer Associates, 1987) is based on Albrecht's (1979) Function Point method (Rubin, 1983). An expert system has even been proposed to calibrate the model used by the estimating process (Cuelenaere et al., 1987).

Objective studies of these methods have been few. Often the developers of a method have described their own technique and reported their own assessment of its accuracy (Donelson, 1976; Jensen, 1983; Putnam, 1978; Walston and Felix, 1977; Wolverton, 1974). Other researchers have tried to predict the cost of projects but only after their completion and hence with full knowledge of their final scope (Banker and Kemerer, 1989; Kemerer, 1987; Kitchenham and Taylor, 1985; Miyazaki and Mori, 1985).

For example, one study evaluated the accuracy of four algorithmic methods by predicting the durations of projects which had already been completed (Kemerer, 1987). However, it found considerable inaccuracy with error rates averaging from 85% to 772%. In a related study, experts estimated these same projects without using formal algorithmic techniques generally and performed better than the models in the original study although mean error rates ranged from 32% to 1107% (Vicinanza et al., 1991). A third study (using different projects) found error rates averaging 166% (Miyazaki and Mori, 1985) and a fourth study (again with different projects) found similarly high error rates (Martin, 1988). These studies are admirable as preliminary efforts;

however, the researchers' knowledge of the scope at the time of estimating (knowledge generally available only in laboratory settings) has caused speculation that the techniques would be even more inaccurate when the scope is initially unknown (Kemerer, 1987).

Nevertheless, the elegance of the algorithmic methods is so impressive that it has inspired the view that ‘the methods available today are more than adequate to establish an estimation approach. All that is needed is management’s willingness to employ the planning and control philosophy used in other functional areas in the information systems department (Benbasat and Vessey, 1980, p. 42).’ However, the extent to which organizations use these estimating methods is known. Besides a few prescriptive articles (Boehm, 1981; Demarco, 1982), research on the actual practice of cost estimating and its problems is also scanty.

Still, a recent case study did describe the actual practice of cost estimating at the largest division of a Fortune 200 organization (Lederer et al., 1990). The research revealed that cost estimates were used for a variety of purposes that included selecting projects for implementation, staffing and scheduling projects, controlling and monitoring their progress, evaluating employee performance, and also marketing proposed systems to users. It also demonstrated how cost estimates were initially prepared and later revised at different stages of the systems development life cycle. It identified the participants in the preparation and approval of the estimates, described the management of the estimating process, and highlighted reasons why cost estimating is often inaccurate.

The case study also stressed the tight link between the preparation of an estimate and the actual development of the estimated system. That is, the touchstone of an estimating method is the comparison of the final cost of the completed system to its original estimate. However, the proximity of the final cost to the original estimate is governed not only by the quality of the estimate but also by the quality of the management of the development effort. Hence, researchers must consider the entire development process when studying the estimating process. Understanding a process as a whole – or gestalt – can explain its parts (Kohler, 1929).

While the case study revealed the actual practice and problems of cost estimating in a single organization, no empirical study of a large sample has described the current state of cost estimating practice in industry until the current one. It extends the case by examining questions it raised but did not answer.

## Objectives

The current study sought answers to eight questions about information systems cost estimating. Their purpose was to enable researchers to understand current cost estimating practice since the literature described above has not yet done so. They might thus help researchers identify methods of improving cost estimating accuracy or suggest avenues for research to do so in order to reduce the potential management problems of inaccurate estimates. The rationale for asking each question and the question follows.

First, confirmation of the importance of the issue would lend credence to reporting the results. Conversely, if the issue were unimportant (a possible but not expected findings), then the need to report the results might be much less. Thus the research asked 'How important is cost estimating to information systems managers and professionals?'

Second, if the respondents reported being highly successful (again a possible but unexpected finding), the need for further study might be less critical. Thus we asked ‘How successful are information systems managers and professionals at cost estimating?’

Third, the uses of cost estimates might help researchers understand the rationale for the cost estimating procedure. This understanding, combined with an understanding of actual cost estimating procedure, might identify problems with the procedure and suggest means to improve it. Hence, the research asked ‘For what purposes do information systems managers and professionals use cost estimates?’

The broad backgrounds for cost estimating and the specific factors influencing it might be flawed. If so, the grounds and factors might suggest efforts for improving cost estimating or for further research to do so. Hence the research asked the following two questions:

(1) 'What broad grounds influence cost estimating?'

(2) 'What specific factors influence cost estimating?'

Because the causes themselves of inaccurate cost estimates might likewise suggest further research about their nature or about practices to eliminate them, the research asked ‘What are the causes of inaccurate cost estimates?’

Finally, by understanding contemporary cost estimating practices and identifying those associated with greater accuracy, researchers may find inconsistencies and flaws that might cause inaccuracy. With an understanding of the reasons for the association, researchers might also suggest practices to improve accuracy. Thus, we asked these last questions:

(1) 'What practices do information systems managers and professionals use in cost estimating?'

(2) 'Which practices are associated with more accurate cost estimating?'

## Methodology

To study these issues, the authors developed a questionnaire based on the case study and other software development cost estimation literature just described (with additions noted below). Major sections were:

(1) A list of potential uses (e.g., to staff projects) of cost estimating. Subjects identified the importance of each on a five-point Likert-type scale.

(2) A list of cost estimating activities (e.g., user management sign-off on the cost estimate). Subjects identified the percentage of their organization's large projects that follow each.

(3) A list of factors (e.g., the size of the system in number of programs) typically influencing cost estimating. Subjects identified the influence of each on a five-point Likert-type scale.

(4) A list of general bases (e.g., intuition) of cost estimating. On a five-point Likert-type scale, subjects identified the extensiveness of their use of each.

(5) A list of recognized software packages (e.g., ESTIMACS) for helping estimate development costs (Coursey, 1987; Datapro, 1988a, b; Kemerer, 1987). Subjects stated if they used each.

(6) A list of potential causes (e.g., overlooked tasks) of inaccurate estimates. Subjects identified on a five-point Likert-type scale the extent to which each was responsible for inaccurate estimates.

(7) One question asking the percentage of large project overruns at their organization and another asking the percentage of underruns.

(8) Demographic questions.

Subjects were asked to answer the questions in terms of what their organization defined as ‘large projects’ (e.g., some companies such as the one in the case study consider large projects to be those estimated to exceed an arbitrary figure such as US \$50 000) to prevent them from considering trivial tasks routinely handled without formal estimating. Subjects were permitted to augment the lists. For example, they could add a software estimating tool if it was not identified in the instrument.

After a pilot test with four information systems managers and analysts followed by a revision to improve the questionnaire's clarity, the authors mailed it to 400 randomly selected members of a large, nationwide association of information systems managers and analysts. A second mailing to non-respondents yielded a total of 116 responses.

Using the respondents' job titles and functions from the demographic items, the researchers eliminated a manager of telecommunications, director of office automation, records manager and EDP auditor since they may have lacked knowledge of estimating in their firms. Because all of the remaining 112 participate in the development of estimates, their approval, or system development based on them, they were knowledgeable about the questions in this study and are appropriate participants in it. $^{1}$ However, it should be noted that their responses represent the perceptions of information systems managers and analysts and these could differ considerably from those of users.

Table 1 Respondents' industries

<table><tr><td>Industry</td><td>Percent of respondents (%)</td></tr><tr><td>Manufacturing</td><td>33</td></tr><tr><td>Insurance</td><td>17</td></tr><tr><td>Banking and finance</td><td>9</td></tr><tr><td>Government</td><td>5</td></tr><tr><td>Utilities</td><td>5</td></tr><tr><td>Retail</td><td>5</td></tr><tr><td>Education</td><td>4</td></tr><tr><td>Systems consulting</td><td>8</td></tr><tr><td>Other</td><td>14</td></tr></table>

All subjects were North Americans. A well-educated group, 87% possessed at least a four-year college degree and at least 33% a masters degree. Respondents supervised an average of 12 employees and had 14 years of experience in information systems with eight at their current firm. Thus respondents were responsible, educated, and experienced professionals familiar with their current firm.

The firms varied in size and industry. Their annual sales averaged almost US 2b. Each averaged 10797 employees while the mean number of employees in their information systems departments was 478. Annual information systems department budgets averaged US 28m. No two subjects came from the same firm. Table 1 shows the firms' industries. The sample represents a wide variety of industries and sizes. Thus the results of the study are probably fairly generalizable. $^{2}$

## Findings

The findings with respect to each objective are described below.

## How important is cost estimating to information systems managers and professionals?

The study confirmed that system development cost estimating is an important issue for information systems managers and professionals. Forty-three percent of the respondents gave it the highest possible rating, indicating it was ‘very important’, while an additional 41% gave it the second highest, ‘moderately important’. Only 10% indicated it was ‘moderately unimportant’ or ‘very unimportant’. The overall rating on the one to five point scale of importance was 4.17 and was higher than the expected mean of 3.00 at the 0.01 level of statistical significance. $^{3}$ Hence, the value of reporting the results is greater than if the subjects said the matter was unimportant.

## How successful are information systems managers and professionals at cost estimating?

Although information systems cost estimating is important, information systems professionals are not successful at it. Respondents reported that approximately 63% of all large projects significantly overrun their estimates while approximately 14% of all large projects significantly underrun their estimates (probably a less serious problem). This suggests that only about one of every four projects is completed at a cost either reasonably above or below its estimate. Hence, the importance of cost estimating along with its inaccuracy confirms that the study of methods of improving accuracy is worthwhile.

## For what purposes do information systems managers and professionals use cost estimates?

Since cost estimating is important, its uses are likewise probably important. As seen in Table 2, the study revealed that cost estimating is used more for project planning and control than for evaluation. The cost estimate is used to staff projects, control project implementation, select projects, schedule them, and quote charges to users. In contrast, it is used, but significantly less important, for auditing project success, evaluating project developers, and evaluating project estimators. The ‘Importance of Use’ rating of each of those three latter uses in Table 2 was lower than the former five at the 0.05 level of significance or better. (More specifically, the rating of 3.22 for auditing project success was lower than the 3.51 rating for quoting charges to users at the 0.05 level of significance.) The division of the table into the two parts may suggest that the estimate is used insufficiently for evaluation and, since evaluation may be tied to improved performance (Lawler et al., 1984), if it were so used more extensively, estimates might be met more frequently.

Table 2 The uses of the cost estimate

<table><tr><td>Use of estimate</td><td>Importance of use mean rating (1-5 scale)</td></tr><tr><td>To staff projects</td><td>3.78</td></tr><tr><td>To control or monitor project implementation</td><td>3.72</td></tr><tr><td>To select proposed projects for implementation</td><td>3.69</td></tr><tr><td>To schedule projects</td><td>3.66</td></tr><tr><td>To quote the charges to users for projects</td><td>3.51</td></tr><tr><td>To audit project success</td><td>3.22</td></tr><tr><td>To evaluate project developers</td><td>3.06</td></tr><tr><td>To evaluate project estimators</td><td>2.90</td></tr></table>

## What broad grounds influence cost estimating?

A variety of general grounds for estimating are possible. As seen in Table 3, this study found that estimators claim to rely more heavily on their personal memory of past projects than on documented facts, established standards, estimating packages and formulas. The participants' rating of the 'Extensiveness of Use' in Table 3 for the comparison to similar, past projects based on personal memory at 3.77 was higher than the other grounds in the table at least at the 0.01 level of significance. However, the participants also rely more heavily on using intuition (i.e., quick and ready insight) than on guessing (i.e., forming an opinion with little or no evidence), two slightly similar means. The rating of 3.38 for intuition was significantly higher than the rating of 2.76 for guessing at the 0.01 level of significance.

The reliance on personal memory rather than documented facts may suggest a flaw in the estimating process: Its basis is not very scientific. However, the unimportance of guessing implies it is also not completely conjecture.

In addition, only 17% reported using a software package to help estimate the development costs of large projects. Table 4 identifies the packages they reported using and the number of respondents using each. $^{4}$

Table 3 Basis of the estimating process

<table><tr><td>Use basis</td><td>Extensiveness of mean rating (1-5 scale)</td></tr><tr><td>Comparison to similar, past projects based on personal memory</td><td>3.77</td></tr><tr><td>Comparison to similar, past projects based on documented facts</td><td>3.41</td></tr><tr><td>Intuition</td><td>3.38</td></tr><tr><td>A simple arithmetic formula (such as summing task durations)</td><td>3.09</td></tr><tr><td>Guessing</td><td>2.76</td></tr><tr><td>Established standards (such as averages, standard deviations, etc.)</td><td>2.33</td></tr><tr><td>A software package for estimating</td><td>1.80</td></tr><tr><td>A complex statistical formula (such as multiple regression, differential equations, etc.)</td><td>1.49</td></tr></table>

Table 4 Software packages in use

<table><tr><td>Software package</td><td>Users</td></tr><tr><td>*ESTIMACS</td><td>6</td></tr><tr><td>*SPECTRUM/ESTIMATOR</td><td>4</td></tr><tr><td>INHOUSE PACKAGE</td><td>2</td></tr><tr><td>PROJECT WORKBENCH</td><td>2</td></tr><tr><td>*Nolan/PROMPT</td><td>1</td></tr><tr><td>PROJECT MANAGER</td><td>1</td></tr><tr><td>AGS PAC III</td><td>1</td></tr><tr><td>DEC/VAX SOFTWARE PROJECT MANAGER</td><td>1</td></tr><tr><td>MICROSOFT PROJECT</td><td>1</td></tr><tr><td>*SLIM</td><td>0</td></tr><tr><td>*SOFTCOST</td><td>0</td></tr><tr><td>*SPQR/ESTIMATOR</td><td>0</td></tr><tr><td>*BEFORE YOU LEAP</td><td>0</td></tr></table>

\* Packages with an asterisk appeared by name in the questionnaire. Respondents wrote in those without asterisks. Those with no users appear in the table to show the comprehensiveness of the study.

## What specific factors influence cost estimating?

Of the numerous potential factors in Table 5, the complexity of the proposed application (with a 4.26 rating) and its required integration with existing systems (with a 4.19 rating) influenced cost estimating most heavily. Both were higher than all of the remaining influences at the 0.05 level of significance or better.

Because many estimating methods are based on the number of lines of code in the application, it is striking that this factor (with a 2.23 rating) was the least influential. In fact, it was lower than the second lowest (and thus all other factors) at the 0.01 level of significance. This suggests that information systems professionals may see research on lines of code as unwarranted. The result is consistent with previous research showing that the use of lines of code is less effective than other measures of size (Kemerer, 1987; Low and Jeffrey, 1990). Combined with the previous finding, it might suggest that researchers focus more on application complexity and integration.

## What are the causes of inaccurate estimates?

Table 6 shows several potential causes of inaccurate estimates. The most responsible cause, frequent requests for changes by users, had a 3.89 rating for ‘Extent of Responsibility’, higher than the remaining causes at least at the 0.05 level of significance. That cause, along with the second highest one, users’ lack of understanding of their own requirements, suggests that information systems managers and professionals attach considerable user responsibility for their inaccurate estimates. Although user inadequacy may be the main cause of inaccuracy, perhaps by assigning the fault to users, estimators can rationalize their own shortcomings and might even be less diligent in their estimating. $^{5}$

Table 5 Influences on the estimate

<table><tr><td>Influence</td><td>Extent of influence mean rating (1–5 scale)</td></tr><tr><td>The complexity of the proposed application system</td><td>4.26</td></tr><tr><td>The required integration with existing systems</td><td>4.19</td></tr><tr><td>The complexity of the programs in the system</td><td>3.92</td></tr><tr><td>The size of the system in number of functions</td><td>3.77</td></tr><tr><td>The capabilities of the project team members</td><td>3.63</td></tr><tr><td>The size of the system in number of programs</td><td>3.60</td></tr><tr><td>The project team&#x27;s experience with the application</td><td>3.49</td></tr><tr><td>The anticipated frequency or extent of potential changes in requirements</td><td>3.44</td></tr><tr><td>The project team&#x27;s experience with the programming language</td><td>3.43</td></tr><tr><td>The data management system (flat files, database, etc.)</td><td>3.39</td></tr><tr><td>The number of project team members</td><td>3.30</td></tr><tr><td>The availability of software productivity tools (such as screen generators or code generators)</td><td>3.14</td></tr><tr><td>The extent of programming or documentation standards</td><td>3.13</td></tr><tr><td>The development mode (batch or on-line)</td><td>3.10</td></tr><tr><td>The particular programming language used</td><td>3.06</td></tr><tr><td>The project team&#x27;s experience with the hardware</td><td>3.05</td></tr><tr><td>The availability of testing aids</td><td>2.84</td></tr><tr><td>The availability of test time on the hardware</td><td>2.68</td></tr><tr><td>Computer memory and secondary storage constraints</td><td>2.65</td></tr><tr><td>The size of the system in number of lines of code</td><td>2.23</td></tr></table>

## What practices do information systems managers and professionals use in cost estimating?

Cost estimating is almost routinely done. Respondents indicated that a cost estimate is prepared for 87% of their organizations' large projects. To better understand the process, this study inquired more about specifically how these organizations prepare their estimates.

## Who prepares the estimate?

Frequently, the estimator later develops the estimated system. For 61% of all projects, the same systems analysts and programmers, who eventually developed the system, had also participated in the preparation of the initial cost estimate. Thus, conversely, for nearly two of every five projects, after the initial estimate, projects are handed-off to different analysts and programmers for final development.

Table 6 Causes of inaccurate estimates

<table><tr><td>Causes</td><td>Extent of responsibility mean rating (1–5 scale)</td></tr><tr><td>Frequent requests for changes by users</td><td>3.89</td></tr><tr><td>Users&#x27; lack of understanding of their own requirements</td><td>3.60</td></tr><tr><td>Overlooked tasks</td><td>3.59</td></tr><tr><td>Insufficient user-analyst communication and understanding</td><td>3.34</td></tr><tr><td>Poor or imprecise problem definition</td><td>3.29</td></tr><tr><td>Insufficient analysis when developing estimate</td><td>3.21</td></tr><tr><td>Lack of an adequate methodology or guidelines for estimating</td><td>3.09</td></tr><tr><td>Lack of coordination of systems development, technical services, operations, data administration, etc. functions during development</td><td>3.06</td></tr><tr><td>Changes in Information Systems Department personnel</td><td>2.95</td></tr><tr><td>Insufficient time for testing</td><td>2.86</td></tr><tr><td>Lack of historical data regarding past estimates and actuals</td><td>2.83</td></tr><tr><td>Lack of setting and review of standard durations for use in estimating</td><td>2.83</td></tr><tr><td>Pressures from managers, users or others to increase or reduce the estimate</td><td>2.83</td></tr><tr><td>Inability to anticipate skills of project team members</td><td>2.81</td></tr><tr><td>Red tape</td><td>2.80</td></tr><tr><td>Users&#x27; lack of Data Processing understanding</td><td>2.77</td></tr><tr><td>Lack of project control comparing estimates and actuals</td><td>2.76</td></tr><tr><td>Reduction of project scope or quality to stay within estimate resulting in extra work later</td><td>2.73</td></tr><tr><td>Inability to tell where past estimates failed</td><td>2.71</td></tr><tr><td>Lack of careful examination of the estimate by Information Systems Department management</td><td>2.61</td></tr><tr><td>Lack of participation in estimating by the systems analysts and programmers who ultimately develop the system</td><td>2.60</td></tr><tr><td>Performance reviews don&#x27;t consider whether estimates were met</td><td>2.49</td></tr><tr><td>Lack of diligence by systems analysts and programmers</td><td>2.34</td></tr><tr><td>Removal of padding from the estimate by management</td><td>2.30</td></tr></table>

## Who approves the estimate?

For $58\%$ of an organization's large projects, a cost-benefit analysis is used to justify system development. Information systems department management carefully studies and approves the cost estimate in $61\%$ of all large projects while user management signs-off on the estimate in $59\%$ . Thus conversely, about two out of five projects can be carried out without a formal cost-benefit analysis, information systems department management's approval of the estimate, or user management's approval of it.

## Is the estimate monitored?

The estimate can be used as a control standard in system development. For 70% of all large projects, a formal monitoring of the progress of a project compares it to its estimate in its project plan. Hence, about three of ten projects are not monitored in this fashion.

When the estimate is used to monitor a project, it is done so primarily by those involved with the project. That is, for only 8% of an organization's large projects, an evaluation of the development process (meaning comparison of the cost estimate to the actual cost) is done by independent auditors.

## Are variances from the estimate used to evaluate personnel?

As expected, the cost estimate is used much less extensively in the performance reviews of users than of information systems personnel. The evaluation of the completion within the estimate is included in user management's performance review for 26% of an organization's large projects and is included in the performance review of user representatives (i.e., liaisons from the application area of the business organization to the information systems department) for 19% of the projects.

In contrast, the evaluation of the completion within the estimate is included in information systems department management's performance review in $54\%$ of all large projects, in the performance review of systems analysts and programmers responsible for final project development in $48\%$ , and in the performance review of the information systems department's initial estimators in $42\%$ . Responses in all three categories for information systems managers and other professionals were higher than those for users at the 0.05 level of significance or better.

## When is the estimate prepared?

The cost estimate is prepared at the beginning of a project and is revised during the project as suggested by the case study but with decreasing frequency. That is, for $77\%$ of an organization's large projects, a cost estimate is prepared during an initial project proposal stage. For $63\%$ of its large projects, a cost estimate is prepared (or revised)

during a feasibility study. For 51%, a cost estimate is prepared (or revised) during systems analysis. And finally, for 47%, a cost estimate is prepared (or revised) during systems design. Hence, while most organizations prepare at least one estimate, they frequently but not universally, reconsider and revise the estimate over the course of the project.

In addition, for $63\%$ of an organization's large projects, the cost estimate is revised to accompany changes in user requirements. This implies that for $37\%$ of its large projects, changes in user requirements are not accompanied by changes in the estimate. This may suggest some reluctance to adjust the estimate when warranted.

## Which practices are associated with more accurate estimating?

Due to the extensive research and publication about estimating algorithms, it has been suggested that organizations using an established, sophisticated one would have more accurate estimating than other organizations (Benbasat and Vessey, 1980). The use of algorithm-based packages would cause this, suggesting the following hypothesis. $^{6}$

H1: Organizations that use software packages for estimating large projects have fewer overruns than organizations that do not use such packages.

However in this study, users of established, sophisticated estimating software packages (namely ESTIMACS, SPECTRUM/ESTIMATOR, and Nolan/PROMPT – those 11 respondents in Table 4 that the researchers had a priori recognized as accepted $^{7}$ ) reported that approximately 71% of all large projects significantly overrun their estimates while non-users reported that only about 62% overrun their estimates. The difference was statistically significant at the 0.10 level and is at first glance surprising. At a minimum, this failure to support H1 suggests that these packages, when used, have not solved the problems of inaccurate estimating. However, it is consistent with Kemerer (1987) and Vicinanza et al. (1991).

It also suggests the need for a closer look at the association of the practices described above with more accurate cost estimating.

## Identity of the estimator

Job enrichment (combining several related activities into one job) provides the worker with more autonomy and responsibility and thus stimulates improved performance (Ford, 1973). In the estimating procedure, this implies the following hypothesis.

H2: Organizations, that more extensively use the same analysts and programmers to initially prepare large project estimates and later develop the same projects, have fewer overruns than organizations that do so less extensively.

The correlation between the percent of an organization's large projects that overrun their estimates and the percent of its large projects for which the same systems analysts and programmers, who eventually develop the system, also had participated in the preparation of the initial estimate was negative and significant at the 0.05 level. This support for H2 is consistent with the view that developers show stronger commitment to timely project completion when they personally perform the estimate.

## Approval of the estimate

Management control principles state that when management approves standards and performance measures, it gives subordinates realistic targets and thus inspires performance (Newman, 1975).

H3: Organizations, whose management more extensively studies and approves large project estimates, have fewer overruns than organizations whose management does so less extensively.

The correlation of the percent of an organization's large projects that overrun their estimates with the percent of projects for which information systems department management carefully studies and approves the estimate was significant at the 0.01 level (and negative as expected). However, the correlation of the percent of projects that overrun their estimates with the percent of projects for which user management also signs-off on an estimate was not. This partial support for H3 is consistent with a belief that information systems department management approval may reduce overruns but user management approval may not.

## Monitoring of the estimate

Management control principles state when management compares actual performance to standards, it increases supervisor and subordinate awareness and inspires performance (Newman, 1975).

H4: Organizations, that more extensively monitor large projects against their estimates, have fewer overruns than organizations that do so less extensively.

As seen in Table 7, the percent of large projects that overrun their estimates correlated significantly and negatively at the 0.01 level with two items about monitoring. The items were

Table 7 Management practices and overruns

<table><tr><td></td><td>Significance level</td><td>Sign of correlation</td></tr><tr><td colspan="3">Identity of the estimator</td></tr><tr><td>Same systems analysts and programmers who eventually develop system also prepared initial cost estimate</td><td>0.05</td><td>negative</td></tr><tr><td colspan="3">Approval of the estimate</td></tr><tr><td>Information systems management carefully study and approval of cost estimate</td><td>0.01</td><td>negative</td></tr><tr><td>User management sign-off on a cost estimate</td><td>ns</td><td></td></tr><tr><td colspan="3">Monitoring of the estimate</td></tr><tr><td>Evaluation of the development process by independent auditors</td><td>0.01</td><td>negative</td></tr><tr><td>Formal monitoring of the project progress by comparing it to its project plan</td><td>0.01</td><td>negative</td></tr><tr><td colspan="3">Use of the estimate to evaluate personnel</td></tr><tr><td>Evaluation of completion within estimate in information systems management&#x27;s performance review</td><td>0.01</td><td>negative</td></tr><tr><td>Evaluation of the accuracy of the estimate in the performance review of information system department estimators</td><td>0.05</td><td>negative</td></tr><tr><td>Evaluation of the completion within the estimate included in the performance review of systems developers</td><td>0.05</td><td>negative</td></tr><tr><td>Evaluation of completion within estimate in user management&#x27;s performance review</td><td>ns</td><td></td></tr><tr><td>Evaluation of completion within the estimate in user liaison&#x27;s performance review</td><td>ns</td><td></td></tr><tr><td colspan="3">Timing of the estimate</td></tr><tr><td>Preparation of a cost estimate during an initial project proposal stage</td><td>0.05</td><td>negative</td></tr><tr><td>Preparation or revision of a cost estimate during feasibility study</td><td>ns</td><td></td></tr><tr><td>Preparation or revision of a cost estimate during systems analysis stage</td><td>ns</td><td></td></tr><tr><td>Preparation or revision of a cost estimate during systems design stage</td><td>ns</td><td></td></tr><tr><td>Cost estimate revised to accompany changes in user requirements</td><td>ns</td><td></td></tr></table>

(1) the percent of its large projects where a formal monitoring of the progress of a project compares it to its project plan and

(2) the percent of those where the evaluation of the development process is done by independent auditors.

This support for H4 confirms both the importance of monitoring the project and of using independent auditors to do so to complete it within its estimate.

Use of estimate variances of evaluate personnel

Performance evaluation is often used to improve performance because employees anticipate rewards or sanctions and thus modify their performance (Lawler et al., 1984).

H5: Organizations, that more extensively have large project estimates to evaluate project personnel, have fewer overruns than organizations that do so less extensively.

The correlations in Table 7 of the percent of large projects that overrun their estimates with the percent of its large projects for which project personnel are evaluated were statistically significant at the 0.01 and 0.05 levels for information systems management, estimators, and developers but not for user management and user liaisons. This partial support for H5 confirms the importance of evaluating information systems project personnel in order to complete a project within its estimate.

## Timing of the estimate

Management control principles state that when management compares actual performance to predetermined standards and takes action when it finds deviation, it can improve performance (Mockler, 1972). In cost estimating, one would expect that the preparation of the initial estimates and its revision (one form of action) during system development would be associated with fewer overruns.

H6: Organizations, that more extensively prepare and revise large project estimates, have fewer overruns than organizations who do so less extensively.

As seen in Table 7, the correlation between the percent of an organization's large projects that overrun their estimates and the percent of those for which a cost estimate is prepared during an initial project proposal stage was negative and statistically significant at the 0.05 level. This was not surprising because it merely attests to the importance of preparing an estimate during an initial project proposal.

However, the correlations between the percent of an organization's large projects that overrun their estimates and the percent of those for which a cost estimate is prepared (or revised) during a feasibility study stage, during a systems analysis stage, or during a systems design stage were not significant. This was very surprising because it fails to support the belief that the revision of the estimate reduces overruns. Before attempting to explain it, one more analysis would be worthwhile.

Namely, as seen in Table 7, the correlation of the percent of an organization's large projects that overrun their estimates with the percent of those for which the cost estimate is revised to accompany changes in user requirements was not significant. This again is an unusual result because one would strongly expect accuracy to improve when assessed in terms of late revisions to the estimate.

The authors suggest that the lack of support for H6 stems from the survey's not explicitly asking respondents to identify the percentage of overruns as measured against a specific estimate in a systems development stage. Had this been done (requiring a slightly more complex instrument), the authors suspect the hypothesis would have been supported. However, the current finding is more interesting.

This is because the current finding implies respondents were probably answering questions about overruns in terms of earlier estimates rather than later ones. Thus the finding supports the notion that revising to respond to user changes, though it may prevent overruns against late estimates, does not prevent the perception of them. In other words, whilst estimators may prefer to be held unaccountable for their early inaccuracies, they may still recognize that later estimates do not exculpate them. In fact, revising to respond to changes may simply call attention to initial estimation errors!

## Implications

The contribution of this study to the literature is a portrayal of how organizations carry out cost estimating. The study is unique in its treatment of cost estimating as coupled with, rather than separate from, other systems development activities. Because it studied cost estimating with a survey of current practice (rather than by reporting the developer of an algorithm's assessment of its accuracy or by predicting completed projects' costs with full knowledge of their scope – the two previously used approaches), it demonstrated an alternative and useful approach to learning about the subject.

In doing so, it has revealed an unsettled state of practice. Estimators appear to select an estimate with limited factual basis. What separates the more accurate estimators from the less accurate ones appears to be that the organizations of the former use the estimate more extensively to evaluate their information systems managers, estimators, and developers and that they monitor these individuals more closely during estimation and development.

This study revealed little evidence of the ability to accurately estimate costs. It simply suggested that effective project management rather than accurate estimating may be the key to project completion within an estimate. The major impediment to accurate estimating, namely frequent requests for changes by users, might be very difficult for systems developers to anticipate and control.

Thus the study also reaffirmed the paradox of cost estimating. That is, systems developers might not know the estimated cost of the proposed system until they know its complete user requirements and scope. They might not know its complete user requirements and scope until they have finished developing it, adjusting and readjusting the specifications along the way. However, after they have finished developing it, they may have spent (and perhaps overrun) its estimated cost.

## Implications for researchers

This study has affirmed the importance of cost estimating and the deficient state of its current practice. It thus offers several suggestions to researchers to build on its contributions.

First, the investigation of cost estimating represents a major opportunity. Researchers should study it to contribute significantly to practice.

Second, this research has suggested that cost-estimating software is used infrequently. This may be because when it is used, it is not very accurate. Therefore, researchers should continue to try to improve cost estimating algorithms. The research spearheaded by Kemerer (1987), Miyazaki and Mori (1985), Martin (1988), and Banker and Kemerer (1989) using the final, working specifications of completed projects should continue. It may be the best empirical research to date to have assessed the algorithms' accuracy and shown it can be improved through better calibration. However, it has done so in a research setting where user requirements remained stable although the current research suggests that unstable requirements are the most serious cause of inaccurate estimates. Therefore, it might be improved by using earlier, more uncertain user requirements rather than the final, certain ones.

Thus third, and in a similar vein, researchers should study the estimating and development processes simultaneously in ongoing organizational activities. A major contribution of the current research is its recognition of the link between estimation and development. Researchers should thus track individual projects by investigating their cost estimating techniques, initial estimates, user requirement changes (the major cause of inaccuracy in this research), re-estimates (an ongoing process recognized in this research), and final costs simultaneously to assess the accuracy of the estimating techniques. Such longitudinal studies may reveal strengths and weaknesses in estimating and development techniques. They may have the greatest likelihood of contributing enduring improvements in estimating accuracy.

Fourth, researchers should independently study information requirements analysis due to its important tie to inaccurate estimation.

Fifth, because the current research used broad questions to obtain a general view of current practice, future research should examine many of its individual questions in more detail by asking exactly who does what when. As examples, research should further investigate the combined estimator/developer role, the estimate approval process, the monitoring of the estimate, personnel evaluation using it, and its timing. This could provide a much more precise picture and suggest more definitive methods of improving estimating.

Sixth, although the current research confirmed some relationships between those practices and project completion within an estimate for large projects, other related variables might have great influence. Examples include estimators' and developers' education and experience, the organization's reward systems, management styles, and others. These variables offer opportunities for research.

Seventh, given the apparent contribution of user changes to cost overruns, researchers should investigate the question of securing systems and supporting them against the instabilities that may result from these changes.

Eighth, replication of this study with a different sample might be valuable. For example, perhaps the estimation and development of engineering systems differs from those of business information systems. Perhaps estimating practices vary in different geographical areas. A different sample might teach useful lessons.

## Implications for Managers

This study offers no immediate key to better cost estimating. However, because current practice in cost estimating is so problematic, the authors do offer several possible suggested actions to information systems managers seeking to increase the accuracy of their estimating. The authors offer them with the assumption of causal relationships between the practices and cost estimating accuracy but also with the caveat that intervening variables may play a role. The suggested

actions are as follows.

(1) Prepare an estimate. Top management will reasonably demand it.

(2) Assign the task of estimating to the individuals who will be the final developers of the system and thus build their commitment to their estimate.

(3) Determine user requirements as accurately as possible before promulgating the estimate in order to minimize frequent user requests for changes and revisions of the estimate later on.

(4) Monitor the progress of a development project closely by comparing it to its project plan. If possible, use independent auditors.

(5) Inform personnel in advance of the intended use of the monitoring to evaluate them. Recognize those who meet their estimates.

## Notes

$^{1}$ Of the final 112 respondents, 94% were responsible for systems department management, project management, and/or systems estimating. Six percent were responsible solely for systems analysis and programming. However, very similar statistical findings resulted both when excluding this 6% and when including the other four dropped subjects.

$^{2}$ The establishment of an instrument's psychometric properties conventionally requires demonstrating validity and reliability. The literature basis and pilot testing reflect the instrument's content validity. Because the analysis described later exclusively used single item rather than multi-item measurement scales, the popularly used Cronbach's alpha was not applicable to assess reliability. Single-item scales were used to reduce the length of the instrument and encourage responses while enabling the study to cover the wide variety of issues. The psychometric properties of this instrument are consistent with exploratory as opposed to confirmatory research testing established theory (Straub, 1989). Because this is a first survey of current practice and only the section on the practices associated with accurate estimates had a solid theoretical background, it alone tested hypotheses.

$^{3}$ This paper used t-tests to compare means (as in this case) and Pearson r correlations to describe relationships.

$^{4}$ Readers familiar with the literature on estimating software may be surprised to see so few actual users. Still, the authors see no reason to doubt the number of users. However, we may question that all the packages actually produce estimates and we discuss this later.

$^{5}$ Prototyping, computer-aided software engineering (CASE) methods, object-oriented programming (OOP), and other techniques are emerging as possible aides in cost estimating. However, this research did not assess their impact on it.

$^{6}$ Because expectations about practices are reasonably founded in the literature, hypotheses about them were tested. The remaining hypotheses are generally modelled around the principles of management control (Mockler, 1972; Newman, 1975) but are augmented by the performance evaluation (Lawler et al., 1984) and job enrichment (Ford, 1975) literature. Details accompany each hypothesis.

$^{7}$ The authors report findings in the text for only the three recognized packages because of their knowledge that at least some of the others were project management rather than estimating tools. However, a test using all 19 packages showed the use of the packages to be slightly more inaccurate than no use of them although not statistically significantly so.

This interesting finding may attest to the value of project management software rather than estimating software!

## References

Albrecht, A.J. (1979) Measuring application development productivity. GUIDE/SHARE Application Development Symposium Proceedings, October, pp. 83–92.

Aron, J.D. (1976) Estimating resources for large programming systems, in Software Engineering: Concepts and Techniques, Proceedings of the NATO Conferences, Naur, P., Randell, B. and Buxton, J.N. (Petrocelli/Charter 1976, New York, NY) (Litton Educational Publishing, Inc.)

Banker, R. and Kemerer, K. (1989) Scale economies in new software development. IEEE Transactions on Software Engineering, 15(10), 1199–1205.

Benbasat, I. and Vessey, I. (1980) Programmer and analyst time cost estimation. MIS Quarterly, 4(2), 30–43.

Benjamin, R.I., Rockart, J.F., Scott Morton, M.S. and Wyman, J. (1984) Information technology: A strategic opportunity. Sloan Management Review, 25(3), 3–10.

Boehm, B.W. (1981) Software Engineering Economics (Prentice-Hall, Englewood Cliffs, NJ).

Boehm, B.W. (1984) Software engineering economics. IEEE Transactions on Software Engineering, January, 4–21.

Boehm, B.W. and Papaccio, P.N. (1986) Understanding and controlling software costs. IEEE Transactions on Software Engineering, 14(10), 1462–1477.

Businessweek (1988) It's late costly, incompetent – But try firing a computer system. November 7, Issue 3078, 164–165.

Computer Associates (1987) CA-ESTIMACS: An Application Development Project Estimation Systems (Computer Associates, Mt Laurel, NJ).

Conte, S.D., Dunsmore, H.E. and Shen, V.Y. (1986) Software Engineering Metrics and Models (Benjamin/Cummings Publishing Company Inc., Menlo Park, CA).

Coursey, D. (1987) Level five's new tool figures software cost. MIS Week, 8, April 20.

Cuelenaere, A.M.E., van Genuchten, M.J.I.M. and Heemstra, F.J. (1987) Calibrating a software cost estimation model: why and how. Information and Software Technology, 29(10), 358–367.

Datapro Research Corp. (1988a) Datapro Directory of Microcomputer Software (Datapro Research Corp., Delran NJ).

Datapro Research Corp. (1988b) Datapro Directory of Software (Datapro Research Corp., Delran NJ).

Demarco, T. (1982) The estimating dilemma. Controlling Software Projects: Management, Measurement and Estimation (Yourdon Press, Englewood Cliffs, NJ).

Demarco, T. (1984) An algorithm for sizing software products. Performance Evaluation Review, 12(2), 13–22.

Donelson, W.S. (1976) Project planning and control. Datamation, 22, June, pp. 73–80.

Emery, J.C. (1971) Cost/Benefit Analysis of Information Systems (The Society for Information Management, Chicago, IL).

Ford, R.N. (1973) Job enrichment lessons from AT&T. Harvard Business Review, 51(1), 96–106.

Freiman, F.R. and Park, R.D. (1979) PRICE software model - version 3; an overview, in Proceedings of IEEE-PINY

workshop on Quantitative Software Models, IEEE Cat. TH0067–9, October, pp. 32–41.

Halstead, M.H. (1977) Elements of Software Science (Elsevier North Holland, New York).

Herd, J.R., Postak, J.N., Russell, W.E. and Stuart, K.R. (1977) Software Cost Estimation Study – Study Results. Doty Associates, Inc., Rockville, MD, Final Technical Report RADC-TR-77-220, Vol. 1 (of two), June.

Jensen, R.W. (1983) An improved macrolevel software development resource estimation model, in Preceedings of the 5th ISPA Conference, April, pp. 384–389.

Jones, T.C. (1986) Programming Productivity (McGraw Hill, NY).

Kemerer, C. (1987) An empirical validation of software cost estimation models. Communications of the ACM, 30(5), 416–429.

King, J.L. and Schrems, E.L. (1978) Cost-benefit analysis in information system development and operation. Computing Surveys, 10, 19–34.

Kohler, W. (1929) Gestalt psychology (H. Liveright, New York).

Kitchenham, B. and Taylor, N.R. (1985) Software project development cost estimation. Journal of Systems and Software, 5(4), 267–278.

Lawler, E.E., Mohrman, A.M. and Resnick, S.M. (1984) Performance appraisal revisited. Organizational Dynamics, 13(1), 20–35.

Lederer, A.L., Mirani, R., Neo, B.S., Pollard, C., Prasad, J. and Ramamurthy, K. (1990) Information system cost estimating: A management perspective. MIS Quarterly, 14(2), 159–178.

Low, G.C. and Jeffrey, D.R. (1990) Functions points in the estimation and evaluation of the software process. IEEE Transactions of Software Engineering, 16(1), 64–71.

Martin, R. (1988) Evaluation of current software costing tools. Software Engineering Notes, 13(3), 49–51.

McCabe, T.J. (1976) A complexity measure. IEEE Transactions on Software Engineering. SE-2(4), 308–320.

Miyazaki, Y. and Mori, K. (1965) COCOMO evaluation and tailoring, in Proceedings of the 8th International Conference on Software Engineering of the IEEE, pp. 292–299.

Mockler, R.J. (1972) The Management Process (Prentice Hall, Englewood Cliffs, NJ).

Mohanty, S.N. (1981) Software cost estimation: Present and future. Software – Practice and Exterience, 11, 103–121.

Nelson, E.A. (1966) Management Handbook for the Estimation of

Computer Programming Costs. System Development Corporation, AD-A648750, October 31.

Newman, W.H. (1975) Constructive Control (Prentice Hall, Englewood Cliffs, NJ).

Putnam, L.H. (1978) A general empirical solution to the macro software sizing and estimating problem. IEEE Transactions on Software Engineering, SE-4(4) July, pp. 3456–361.

Rubin, H.A. (1983) Macro-estimation of software development parameters: The ESTIMACS system document CH1919-0/83/0000/0109 (The Computer Society of the IEEE, Washington DC).

Straub, D.W. (1989) Validating instruments in MIS research. MIS Quarterly, 13(2), 147–169.

Tate, G. and Verner, J.M. (1990) Software sizing and costing models: a survey of empirical validation and comparison studies. Journal of Information Technology, 5, 12–26.

Vicinanza, S.S., Mukhopadhyay, T. and Prietula, M.J. (1991) Software Effort Estimation: An Exploratory Study of Expert Performance. Information Systems Research, 2(4), 243–262.

Walston, C.E. and Felix, C.P. (1977) A method of programming measurement and estimation. IBM Systems Journal, 16(1), 54–73.

Wolverton, R.W. (1974) The cost of developing large-scale software. IEEE Transactions on Computers, C-23(6), June, 615–636.

## Biographical notes

Albert L. Lederer is Professor of MIS and Chair of the Department of Decision and Information Sciences at Oakland University. His current research interests are the management of information with special interests in strategic information planning and cost estimating.

Jayesh Prasad is Assistant Professor of MIS in the Department of MIS and Decision Sciences at the University of Dayton. His current research interests are the organizational impact of information systems and the management of information resources.

Address for correspondence: Albert L. Lederer, Decision and Information Sciences Department, School of Business Administration, Oakland University, Rochester, MI, USA 48309-4401.
