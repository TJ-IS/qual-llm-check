---
otero_id: 18720
otero_key: "BQ39CQYQ"
title: "Linear regression and information systems"
authors: "Marius A. Janson"
year: "1991"
journal: "Information & Management"
doi: "10.1016/0378-7206(91)90038-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Linear regression and information systems An exploratory study

Marius A. Janson

University of Missouri-St Louis, Management Science and Information Systems Department, St Louis, MO 63121 USA

Linear regression serves information systems researchers and practitioners in different ways experimentally verifying a priori models and theories, constructing data-based models and theories, and enabling data-based and model-based decision making. Drawing on these differences regression applications occurring over the last decade are examined. Evidence gathered by this study suggests that these differences are often not acknowledged, leading to results that are frequently suboptimal and at times erroneous

Keywords Information systems, Confirmatory analysis Hypothesis testing, Theory building Exploratory analysis, Decision making, Linear regression

![](/api/attachments/BQ39CQYQ/fulltext/images/fffc7045ace1acc43142a4b4555113a7cd8164b7a3ffd2c0f2b3364cf79ac874.jpg)

Marius A Janson is Associate Professor in the Department of Management Science and Information Systems at the University of Missouri-St Louis During the 1989–1990 academic year he was a Visiting Associate Professor in the Faculty of Commerce and Business at the University of British Columbia, Vancouver, Canada. He received his Ph D from the University of Minnesota His research interests include methodologies for systems analysis and design managerial issues of end-user computing, and the application of exploratory statistical techniques to problems in information systems research His articles have appeared in Behaviour and Information Technology, Information and Management, Journal of Management Information Systems, and Management Information Systems Quarterly

## Introduction

A survey by Ledbetter and Cox [13] shows that linear regression is employed by more people and for a greater variety of applications than any other management science method. In view of its broad acceptance in management sciences, it is important to examine its use for studying information systems (IS). An investigation should identify areas of theoretical and practical concern that can be analyzed by linear regression and result in a set of descriptives for applying the method

Linear regression can be applied for many objectives that differ in purpose (1) to summarize a large mass of data by constructing interpolative equations [7], (2) to corroborate or to refute an a priori theory by a process of hypothesis testing, and (3) to aid in decision making There are several ways of applying linear regression to questions in IS First, because it is a relatively young discipline much IS research aims at theory building, which often requires extensive data summarization Second, research in IS involves testing the models from theory building Third, in addition to the research issues, many ISs are analyzed, developed, and implemented in working environments These activities often require model-based managerial decision making In the ways illustrated in Figures 1, 2, and 3, linear regression can contribute effectively in all three areas

This article has a twofold purpose to investigate the contribution of linear regression to IS research and IS implementation, and to suggest ways for enhancing the contribution of this statistical technique. First, I present a framework for applying regression to theory testing, theory building, and decision making, these are all illustrated. Next, I analyze the nature of the application of regression techniques, basing my findings on an extensive analysis of articles published in the leading IS journals [8,10] The literature analysis employs recently developed exploratory statistical techniques. The implications of these findings for the proper use of exploratory linear regression are generalized to other areas in IS research and IS implementation

## Linear regression and theory testing

Popper [15] observed that it is quite easy to find confirmation for nearly every theory. To avoid this drawback he suggested that theories should be constructed based on falsification principle. This process starts with a theory that may arise from vague notions or informed guesses (Figure 1). The theory provides the basis for constructing a hypothesis and a model whose predictions are verifiable by experimentation. If experimental results disagree with predictions, then the model, and hence the theory, is proven to be false. Agreement between experimental results and the predictions are regarded as corroborative of the theory, but never as its proof. The theory maintains its tentative or provisional status, being ready to be tested, or is proven to be false and ready to be replaced by a different theory, which in turn is subjected to the same procedure

The function of linear regression in the theory testing process is to provide a theory-based model

![](/api/attachments/BQ39CQYQ/fulltext/images/19e651af9e46aed1ed9c704aa8cdec9108d47ae917fb2ec0df0742644c6fe3fe.jpg)  
Fig 1 Hypothesis testing

The model's predictions are compared against actual experimental data, resulting in the rejection or corroboration of the theory Cale et al [3] provide an interesting example of this process by testing a theory known as Grosch's law. This theory holds that the power of a computer increases by the square of its cost. The authors point out the elusive nature of "computing power" and finally express it as a function of main memory size, direct access storage device size, and year of system introduction. Data on computer cost and operational characteristics of 167 computers collected over the 1970–1978 period were used to estimate model parameters and to test the theory. The regression results led the authors to conclude that the simple straightforward relationship between computer price and computing power does not accurately reflect the actual data and that more complicated relationships between computer cost and computer characteristics are needed. The initial interpretations of Grosch's Law are rejected and they then present a refined version of Grosch's Law

## Linear regression and theory building

The role of linear regression with respect to theory building is to find structures that can explain data $[4,5,16]$ . Often the data have been collected under conditions outside the control of the analyst, for example, when the data originate from economic studies conducted by government agencies. These empirical conditions in combination with the knowledge of the analyst are the basis for defining the data structure, which need not be unique and may not be valid beyond the data set under investigation. Because data analysis focuses on reducing data complexity it does not have to lead to a model, although the results may suggest one. Exploratory analysis is an inductive process, that is, it ultimately functions as theory building through the act of making a closer reading of the data (Figure 2), which acquire meaning as the analyst seeks to define a satisfactory structure through a selection process that attempts to fit the data into a variety of alternative models (thus the model follows the data). In this spirit, data analysis is defined by Benzecri $[1]$ as a “rigorous method that extracts structure from data”.

![](/api/attachments/BQ39CQYQ/fulltext/images/1970246ca85bf0b4b801e66102d96a09140e4c4c2e27f39ea98e30d831e2ae76.jpg)  
Fig 2 Theory building

These concepts are applied by Jeffery [12] in the context of a software programming environment. The focus of the research is on understanding the relation between programmer productivity and program development effort and staffing levels. Based on data collected on nine software projects and using stepwise linear regression, he fits a model of the form

$$
\log (\text { production }) = 0. 9 5 + 0. 8 6 \log (\text { project   size })
$$

$$
- 1 6 6 \log (\text { staffing   level }),
$$

where production, project size, and staffing level are expressed in lines of code per staff-month, lines of program code, and number of people assigned to the project, respectively. The model led to the theory that project effort relates positively to productivity and, conversely, staffing levels relate negatively to it. Thus, linear regression provides a vehicle for data analysis and summarization, in addition to presenting a useful data model. The theory's validity with respect to other software development projects is quite tentative, because it is based on a very small data set comprised of just nine projects and, more importantly, an extension is an inductive process. However, despite its tentative nature, the theory and its model provide a basis for additional studies that may corroborate or reject the model

## Linear regression and decision making

The application of regression analysis to decision making uses the functional relationships that arise from theory building and testing activities (Figure 3) for evaluating alternative problem solutions. The decision maker then selects a reasonable course of action based on the outcome of the analysis. Decision making differs materially from theory building and theory testing [17], where the outcome of the analysis can be merely a conclusion that additional research is necessary. In cases of decision making, however, the analyst or manager rarely has this option and usually has to select a course of action bases on data in hand

Colton et al [6] show the use of linear regression in decision making. They suggest financial resource allocation procedures that aid police department staff members in the selection and acquisition of an IS for automobile dispatching. The procedure consists of four equations, three relate hardware, software, and system service cost to the size of the population served by the information system, and the fourth reflects total system cost. For example, total system cost is given by

Total Cost (\$1,000)

## $= -24 + 1989$ Population Size (1,000)

Equation parameters were estimated on a small data set comprised of system cost and population size collected on 13 systems that were developed and implemented during the 1974–1977 period. The functional form of the regression models is not based on any specific theory, but motivated by an indirect line of reasoning. They argue that system cost is directly related to processing load and file sizes, which in turn are linked to city population size In short, the decision making procedures are based on theory building concepts

![](/api/attachments/BQ39CQYQ/fulltext/images/df02f469faf15ef2078da7aa4ed331810fba59a54877df6a4f1f343a2027908f.jpg)  
Fig 3 Decision making

Identifying the underlying purpose of regression analysis with respect to a specific research project is important for optimal execution of the method. Thus, using regression analysis for hypothesis testing will be much more likely to be effective for research questions that pertain to a well-established discipline. Conversely, research in less well-established disciplines tends to be more exploratory and therefore better served by regression analysis providing theory building. These considerations are the motivation for a literature-based exploration of regression use in IS research and implementation

## The use of linear regression for IS research and implementations

My study of linear regression involves and exploratory examination of key IS journals Those identified by Davis [8] and Hamilton and Ives [10] were taken as a convenient point of departure This set was enlarged by journals that publish articles of interests to IS research, even though their editorial policy may not be specifically directed toward IS issues Next, the set of over 20 journals was reduced by omitting those that featured very few or no articles employing linear regression Thus, the journals relevant to this study are (1) Communications of the ACM, (2) Information and Management, (3) Information Processing and Management, (4) Journal of Management Information Systems, (5) Journal of Systems and Software, (6) Management Information Systems Quarterly, and (7) IEEE Transactions on Software Engineering

A cursory analysis of Table 1 reveals that only a handful of articles employ linear regression. Of the approximately 4,000 articles published since 1978, only 93 (2%) reported the use of linear regression. Of greater interest, however, is the breakdown by usage category of articles that do use regression. Table 2 shows by journal and year the number of articles that used linear regression for the purpose of hypothesis testing (HT), theory building (TB), and managerial decision making (MD). The table's right-hand column shows, by journal, the total number of articles published between 1978 and 1988. For example, in 1987 Communications of the ACM (CACM) featured one article on hypothesis testing, two articles on theory building, and none on decision making. From 1978 until 1988, Communications of the ACM published 21 articles that used linear regression, of these 6 employed regression for hypothesis testing, 9 for theory building, and 6 for managerial decision making. The table's three bottom rows report by year and usage category the number of articles published in all journals combined. The three rows at the table's bottom show that for all three usage categories the number of articles using regression increased between 1978 and 1989. In

Table 1  
Number of articles by journal and year

<table><tr><td>Journal title</td><td>Journal code</td><td>Period</td><td>Number MIS articles</td><td>Number linear regression articles</td><td>Percent linear regressiona</td></tr><tr><td>Communications of the ACM</td><td>CACM</td><td>1978–88</td><td>1008</td><td>21</td><td>2</td></tr><tr><td>Information and Management</td><td>IM</td><td>1978–88</td><td>297</td><td>10</td><td>4</td></tr><tr><td>Information Processing and Management</td><td>IPM</td><td>1978–88</td><td>732</td><td>11</td><td>2</td></tr><tr><td>Journal of Management Information Systems</td><td>JMIS</td><td>1984b–88</td><td>114</td><td>4</td><td>4</td></tr><tr><td>Journal of Systems and Software</td><td>JSS</td><td>1982b–88</td><td>231</td><td>21</td><td>9</td></tr><tr><td>Management Information Systems Quarterly</td><td>MISQ</td><td>1978–88</td><td>302</td><td>12</td><td>4</td></tr><tr><td>IEEE Transactions on Software Engineering</td><td>TSE</td><td>1978–88</td><td>1862</td><td>14</td><td>1</td></tr></table>

the earlier years (i.e., 1978 to 1980) few articles used regression and thus a very uneven distribution arises over the three categories. However, with the increasing number of articles using linear regression during the later part of the period, its use becomes more evenly divided over the three categories. The increasing use of linear regression is also evident from Figure 4, which is based on the data from the three bottom rows of Table 2. The figure shows by year the combined use of linear regression for hypothesis testing, theory building, and decision making as a percent of the number of articles reported. The increasing trend can arise from multiple causes One possibility is a greater appreciation of IS researchers and practitioners of the value of this statistical technique, a second could be a greater number of IS research and implementation projects suitable for analysis by linear regression

The increasing use of linear regression is important, because this can result in the identification of areas of application that are particularly suited to being analyzed by this statistical method Table 3 classifies the use of linear regression into planning, managing the IS resources, and development. Each category in turn is divided into subcat-

Table 2  
Articles by journal and category

<table><tr><td rowspan="2">Journal Code</td><td rowspan="2">Category</td><td colspan="11">Year</td><td rowspan="2">Total by Journal</td></tr><tr><td>78</td><td>79</td><td>80</td><td>81</td><td>82</td><td>83</td><td>84</td><td>85</td><td>86</td><td>87</td><td>88</td></tr><tr><td rowspan="3">CACM</td><td>HT</td><td></td><td>1</td><td></td><td></td><td></td><td></td><td>2</td><td>1</td><td></td><td>1</td><td>1</td><td>6</td></tr><tr><td>TB</td><td></td><td></td><td></td><td>1</td><td></td><td></td><td>1</td><td></td><td>2</td><td>2</td><td>3</td><td>9</td></tr><tr><td>MD</td><td>1</td><td></td><td>1</td><td>1</td><td></td><td></td><td></td><td>2</td><td>1</td><td></td><td></td><td>6</td></tr><tr><td rowspan="3">IM</td><td>HT</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>TB</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>3</td><td>3</td><td></td><td></td><td>8</td></tr><tr><td>MD</td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td>1</td><td></td><td></td><td></td><td>2</td></tr><tr><td rowspan="3">IPM</td><td>HT</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td>1</td><td>2</td></tr><tr><td>TB</td><td></td><td></td><td>1</td><td></td><td>1</td><td></td><td>3</td><td>2</td><td>1</td><td></td><td></td><td>8</td></tr><tr><td>MD</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td>1</td></tr><tr><td rowspan="3">JMIS</td><td>HT</td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td>1</td><td>2</td></tr><tr><td>TB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td>1</td></tr><tr><td>MD</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td>1</td></tr><tr><td rowspan="3">JSS</td><td>HT</td><td></td><td></td><td>1</td><td>2</td><td>1</td><td></td><td></td><td>1</td><td></td><td>1</td><td>1</td><td>7</td></tr><tr><td>TB</td><td></td><td></td><td></td><td>1</td><td></td><td></td><td>1</td><td>4</td><td></td><td>1</td><td>3</td><td>10</td></tr><tr><td>MD</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>2</td><td></td><td></td><td>1</td><td></td><td>4</td></tr><tr><td rowspan="3">MISQ</td><td>HT</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td>1</td><td></td><td>3</td><td>5</td></tr><tr><td>TB</td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td></td><td>1</td><td>3</td></tr><tr><td>MD</td><td></td><td></td><td>1</td><td></td><td></td><td></td><td>1</td><td></td><td></td><td>2</td><td></td><td>4</td></tr><tr><td rowspan="3">TSE</td><td>HT</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td>1</td><td>1</td><td>3</td></tr><tr><td>TB</td><td></td><td>1</td><td></td><td></td><td></td><td>3</td><td></td><td>4</td><td>1</td><td></td><td></td><td>9</td></tr><tr><td>MD</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td></tr><tr><td rowspan="3">TOTAL by Year</td><td>HT</td><td></td><td>1</td><td>1</td><td>2</td><td>1</td><td>3</td><td>3</td><td>2</td><td>1</td><td>3</td><td>8</td><td>25</td></tr><tr><td>TB</td><td></td><td>1</td><td>1</td><td>2</td><td>1</td><td>4</td><td>7</td><td>14</td><td>8</td><td>3</td><td>7</td><td>48</td></tr><tr><td>MD</td><td>2</td><td></td><td>2</td><td>1</td><td>2</td><td>1</td><td>3</td><td>3</td><td>2</td><td>4</td><td></td><td>20</td></tr></table>

Legend HT = Hypothesis Testing, TB = Theory Building, MD = Managerial Decision Making  
CACM = Communications of the ACM  
IM = Information and Management  
IPM = Information Processing and Management  
JMIS = Journal of Management Information Systems  
JSS = Journal of Systems and Software  
MISQ = Management Information Systems Quarterly  
TSE = IEEE Transactions on Software Engineering

![](/api/attachments/BQ39CQYQ/fulltext/images/3893fa1afa8f489d4adec79da39dab09a484842f75df4e0217ecb5d92b317431.jpg)  
Fig 4 Number of articles using regression/Total number of published journal articles

egories Category 11 typically includes articles that discuss selecting information systems that enhance the organization's strategic position and help it achieve its objectives Category 12 represents articles on cost accounting methods for computing services and assessing the value of information system proposals before committing financial resources Category 21 includes articles dealing with managing personnel resources Typical examples are in improving programmer productivity, motivation, interpersonal skills, and job satisfaction Category 2 2 pertains to the management of software quality in a day-to-day production environment Software quality is assessed along several dimensions reliability, robustness, being free from program errors, and ease of maintenance Category 2 3 concerns articles that ensure the efficient and effective use of computing resources, and data integrity System development (category 31) is composed of system analysis, system design (excluding programming), and system implementation Finally, software development (category 32) refers to assessing program development effort and cost as functions of program size and complexity, developing programming methods, and devising ways of forecasting software debugging time

Table 3
Articles by subject and purpose

<table><tr><td rowspan="2">Subject</td><td rowspan="2"></td><td colspan="3">Purpose</td></tr><tr><td>Hypothesis testing</td><td>Theory building</td><td>Decision making</td></tr><tr><td rowspan="2">1 Planning</td><td>1 1 Identifying information systems that support organizational objectives</td><td>2</td><td>4</td><td>1</td></tr><tr><td>1 2 Allocating financial, personnel, and managerial resources to IS</td><td>4</td><td>4</td><td>2</td></tr><tr><td rowspan="3">2 Managing</td><td>2 1 Personnel resources</td><td>3</td><td>7</td><td>1</td></tr><tr><td>2 2 Ensuring software quality</td><td>1</td><td>12</td><td>0</td></tr><tr><td>2 3 Ensuring efficient and effective operations</td><td>2</td><td>1</td><td>4</td></tr><tr><td rowspan="2">3 Development</td><td>3 1 System development</td><td>4</td><td>7</td><td>8</td></tr><tr><td>3 2 Software development</td><td>9</td><td>13</td><td>4</td></tr></table>

The columns of Table 3 indicate whether an article employs linear regression for the purpose of hypothesis testing, theory building, or managerial decision making. For example, power relationships between the IS department and users determine in part how IS services are organized and funded. A study that employs linear regression for testing the hypothesis that organizational power depends on the ability of the organization to cope in a complex environment would be classified into cell [1 2, HT] A different questionnaire-based study may seek to provide a basic framework to account for the effects of computerization on job satisfaction. This study would fall into cell [2 1, TB] if linear regression were used to analyze the questionnaire results. A third study may use linear regression for modeling the quality of a batch computer run as a function of operating characteristics, such as CPU time, number of DASD accesses, and other variables. Such use of linear regression would be classified as belonging in category [2 3, DM] if, in fact, this model were employed for control in the day-to-day operating environment

A visual inspection reveals that compared to other table entries, linear regression is most often used for managing personnel resources (category 2 1) and ensuring software quality (category 2 3), and for system (category 3 1) and software development (category 3 2). In fact, when categories 2 3 and 3 2 are combined into one category, linear regression is most often used in the context of software development and software quality assurance. The importance of linear regression is analyzed more effectively by carrying out a median polish on Table 3 [18]

Table 4
Two sweeps of a median polish

<table><tr><td colspan="6">a Initial table entries</td></tr><tr><td rowspan="2">Planning</td><td>Identifying Information Systems that Support Organizationa Objectives</td><td>2</td><td>4</td><td>1</td><td></td></tr><tr><td>Allocating Financial, Personnel, and Managerial Resources to IS</td><td>4</td><td>4</td><td>2</td><td></td></tr><tr><td rowspan="3">Managing</td><td>Personnel Resources</td><td>3</td><td>7</td><td>1</td><td></td></tr><tr><td>Ensuring Software Quality</td><td>1</td><td>12</td><td>0</td><td></td></tr><tr><td>Ensuring Efficient and Effective Operations</td><td>2</td><td>1</td><td>4</td><td></td></tr><tr><td rowspan="2">Development</td><td>System Development</td><td>4</td><td>7</td><td>8</td><td></td></tr><tr><td>Software Development</td><td>9</td><td>13</td><td>4</td><td></td></tr><tr><td colspan="6">b First sweep-Row medians subtracted from row entries</td></tr><tr><td rowspan="2">Planning</td><td>Identifying Information Systems that Support Organizationa Objectives</td><td>0</td><td>2</td><td>-1</td><td>2</td></tr><tr><td>Allocating Financial, Personnel, and Managerial Resources to IS</td><td>0</td><td>0</td><td>-2</td><td>4</td></tr><tr><td rowspan="3">Managing</td><td>Personnel Resources</td><td>0</td><td>4</td><td>-2</td><td>3</td></tr><tr><td>Ensuring Software Quality</td><td>0</td><td>11</td><td>-1</td><td>1</td></tr><tr><td>Ensuring Efficient and Effective Operations</td><td>0</td><td>-1</td><td>2</td><td>2</td></tr><tr><td rowspan="2">Development</td><td>System Development</td><td>-3</td><td>0</td><td>1</td><td>7</td></tr><tr><td>Software Development</td><td>0</td><td>4</td><td>-5</td><td>9</td></tr><tr><td colspan="6">c Second sweep-Column medians subtracted from column entries</td></tr><tr><td rowspan="2">Planning</td><td>Identifying Information Systems that Support Organizationa Objectives</td><td>0</td><td>0</td><td>0</td><td>-1</td></tr><tr><td>Allocating Financial, Personnel, and Managerial Resources to IS</td><td>0</td><td>-2</td><td>-1</td><td>1</td></tr><tr><td rowspan="3">Managing</td><td>Personnel Resources</td><td>0</td><td>2</td><td>-1</td><td>0</td></tr><tr><td>Ensuring Software Quality</td><td>0</td><td>9</td><td>0</td><td>-2</td></tr><tr><td>Ensuring Efficient and Effective Operations</td><td>0</td><td>-3</td><td>3</td><td>-1</td></tr><tr><td rowspan="3">Development</td><td>System Development</td><td>-3</td><td>-2</td><td>2</td><td>4</td></tr><tr><td>Software Development</td><td>0</td><td>2</td><td>-4</td><td>6</td></tr><tr><td></td><td>0</td><td>2</td><td>-1</td><td>3</td></tr></table>

The application of a median polish expresses each cell entry as a common value, a row effect, a column effect, and a residual. The common value describes the table entries as a whole. Row effects account for differences among table values that arise from use categories. Column effects reflect the use of linear regression for hypothesis testing, theory building, and managerial decision making. Finally, the residual terms are the part of table entries unaccounted for by the common values and row and column effects. Each table entry is thus given by the model

$$
\begin{array}{r l} \mathrm{Y} _ {\mathrm{ij}} & = \text { common } + \text { row   effects } _ {\mathrm{i}} + \text { column   effects } _ {\mathrm{j}} \\ & + \text { residual } _ {\mathrm{ij}}, \end{array}
$$

where 1 refers to use category, and j to use purpose

Table 4 shows how to effect the median polish First, each row median is subtracted from the row's entries (Table 4a) and placed in a column to the right (Table 4b). Next, each column median is subtracted from the column's entries (Table 4b)

and placed in a row at the foot of the table (Table 4c) The second iteration applies the aforementioned procedure to the entries of Table 4c. The process stops when additional iterations fail to produce further table entry changes. The median polish on Table 3 which is shown in Table 5, requires only four iterations

For example, Table 3 reports eight articles that use linear regression for decision making in the context of systems development. This figure can now be expressed as

$$
8 = 3 (\text { common }) + 2 (\text { subject   effect })
$$

$$
- 1 (\text { purpose   effect }) + 4 (\text { residual })
$$

The purpose effect values (Table 5, bottom row) suggest that linear regression is used predominantly for theory building (effect value 2) and to a much lesser degree for decision making (effect value -1). The subject effect values (Table 5, right-hand column) identify software development (effect value 6) as an area where linear regression is heavily used. The residuals of Table 5 lack a particular pattern. However, the residual associated with applying regression analysis in the context of theory building and ensuring software quality (value 9) is extraordinarily large when compared to the other residuals. The large positive residual implies that regression is far more heavily used in the aforementioned context than reflected by the common factor, the purpose effect, and the subject effect. In the same way, the negative residual associated with software development and decision making (value -4) implies that linear regression is used less than is indicated by the common factor, the purpose effect, and the subject effect The significance of extreme residuals can be conveniently assessed in coded table form [14]

Table 5  
Median polish-articles by subject and purpose

<table><tr><td rowspan="2">Subject</td><td rowspan="2"></td><td colspan="4">Purpose</td></tr><tr><td>Hypothesis testing</td><td>Theory building</td><td>Decision making</td><td>Subject effect</td></tr><tr><td rowspan="2">1 Planning</td><td>1 1 Identifying information systems that support organizational objectives</td><td>0</td><td>0</td><td>0</td><td>-1</td></tr><tr><td>1 2 Allocating financial personnel, and managerial resources to IS</td><td>1</td><td>-1</td><td>0</td><td>0</td></tr><tr><td rowspan="3">2 Managing</td><td>2 1 Personnel resources</td><td>0</td><td>2</td><td>-1</td><td>0</td></tr><tr><td>2 2 Ensuring software quality</td><td>0</td><td>9</td><td>0</td><td>-2</td></tr><tr><td>2 3 Ensuring efficient and effective operations</td><td>0</td><td>-3</td><td>3</td><td>-1</td></tr><tr><td rowspan="2">3 Development</td><td>3 1 System development</td><td>-1</td><td>0</td><td>4</td><td>2</td></tr><tr><td>3 2 Software development</td><td>0</td><td>2</td><td>-4</td><td>6</td></tr><tr><td>Purpose effect</td><td></td><td>0</td><td>2</td><td>-1</td><td>3</td></tr></table>

Table 6 is the result of reexpressing the residuals of Table 5 using the following coding convention, residuals between the two hinges are coded as “\*” residuals beyond the hinges but within the inner fences are coded as “−” and “+”, residuals beyond the inner fences but inside the outer fences are coded as “=” and “#”, and residuals beyond the outer fences are coded as “M” and “P”. Although they are not equivalent, the lower and upper hinges are similar to the upper and the lower quartiles. The distance between the hinges is referred to as the H-spread. The lower and upper inner fences are calculated as

lower hinge - (1 5 × H-spread)

upper hinge + (1 5 × H-spread)

The lower and upper outer fences are calculated as lower hinge - (3 × H-spread)

upper hinge + (3 × H-spread)

Residuals beyond the inner fences are unusual in comparison to the majority of the residual values

Table 6 shows one residual beyond the upper outer fence (code = P) and one residual below the lower outer fence (code = M) Thus, the application of linear regression in the context of theory building for ensuring software quality (code = P) is significantly larger than implied by the common factor, the purpose effect, and the subject effect. Similarly, the application of regression for decision making and software development (code = M) is significantly lower than expected. To put it differently in comparison to all areas of application, the application of linear regression is unusually prominent with respect to software development and software quality

Figure 5 shows the split of the use of linear regression. The scarcity of articles employing regression for hypothesis testing (27%) may be attributed to the newness of the field of IS, which, by definition, would preclude the existence of many hypotheses. The scarcity of hypotheses to test would also necessitate alternative approaches to research. For example, Galliers and Land [9] propose a long chain of research paradigms that has the construction of testable theories as its end goal. This chain includes formulating research questions, conducting survey research, theory building, case studies, theory testing, and extension. The many preparatory steps toward testable theories explain the frequent use of regression techniques, since these research activities involve

Median polish coded - articles by subject and purpose

<table><tr><td rowspan="2">Subject</td><td rowspan="2"></td><td colspan="3">Purpose</td></tr><tr><td>Hypothesis testing</td><td>Theory building</td><td>Decision making</td></tr><tr><td rowspan="2">Planning</td><td>Identifying information systems that support organizational objectives</td><td>*</td><td>*</td><td>*</td></tr><tr><td>Allocating financial, personnel, and managerial resources to IS</td><td>*</td><td>-</td><td>*</td></tr><tr><td rowspan="3">Managing</td><td>Personnel resources</td><td>*</td><td>+</td><td>-</td></tr><tr><td>Ensuring software quality</td><td>*</td><td>P</td><td>*</td></tr><tr><td>Ensuring efficient and effective operations</td><td>*</td><td>=</td><td>#</td></tr><tr><td rowspan="2">Development</td><td>System development</td><td>-</td><td>*</td><td>#</td></tr><tr><td>software development</td><td>*</td><td>+</td><td>M</td></tr></table>

P Above upper outer fence  
# Between upper inner and upper outer fence  
+ Between upper hinge and upper inner fence  
\* Between lower and upper hinges  
- Between lower hinge and lower inner fence

= Between lower inner and lower outer fences

M Below lower outer fence

![](/api/attachments/BQ39CQYQ/fulltext/images/c1bf86faaf013e63842d0d6af3dd7b6e4fb2985524afb7dc1f96628540e07ccc.jpg)  
Fig 5 Articles reporting hypothesis testing theory building, and decision making/Number of articles using regression

summarization and exploration of large quantities of data, for which regression analysis is uniquely suited

When linear regression is used for theory building (52%), it is most often to support software quality management and software development. Factors associated with software cost can often be expressed as a regression model with a surprisingly simple functional form. The model's parameters in turn can be estimated using historical cost figures. This simple example also applies to other issues arising from software quality and software development. Many of these can be solved, in part, by an engineering approach and thus are prime candidates for linear regression

The small proportion of regression used for decision making (21%) was unexpected and is disappointing in view of the application orientation of the IS discipline

Because regression for theory building constitutes such an important use, the application that was most often reported warrants closer evaluation. When used in this context, most, if indeed not all, direction for the model's functional form has to be gleaned from the data. It is therefore discouraging to find that the choice of the model's functional form is frequently the result of mechanistic procedures, such as stepwise regression. Furthermore, none of the articles surveyed report a fit of the data to more than one model or mention investigating possible erroneous observations by conducting a residual analysis. Multiple models lead to a richer appreciation of the phenomena underlying the data and, possibly, to different conclusions. A better understanding of the data structure can be instrumental in explaining observations that seem to be anomalous in relation to other cases in one model, but not in another. The discovery and study of these so-called outliers frequently result in better models in the sense of providing a more complete summary of the data. Such an approach supports what theory building aims to do to generate hypotheses that need to be tested by additional data. The combined application of exploratory techniques and residual analysis is a crucial component of theory building However, what emerges from the literature is a lack of appreciation for these procedures, or else that they are used, but not reported

## Conclusion

Linear regression can make important contributions to IS by providing support for theory building, by testing research hypotheses, and as a tool for managerial decision making. The literature shows that, when used, linear regression is employed most frequently for the first purpose but infrequently for testing research hypotheses and managerial decision making. Contrary to its status as a method of choice in management sciences, linear regression is a severely underused and often misapplied tool in IS

More importantly, the evidence from published journal articles suggests a lack of appreciation of the difference between using linear regression for hypothesis testing or for theory building. It seems that linear regression is narrowly applied, as though the method were a minor extension of larger research or practical concerns and in a rather mechanistic fashion through such procedures as stepwise regression. The in-depth literature examination demonstrates the need for testing the assumptions underlying linear regression by carefully analyzing the residuals with the aid of exploratory techniques, in a way similar to that used for analyzing Tables 3, 5, and 6. This approach calls for a willingness to fit several alternative models to the same data with the expectation that it will lead to additional insight and, ultimately, to a better model. Thus, the first priority of the modeling process is not to predict but rather to stimulate thinking. With respect to the question of the model, it is perhaps useful to quote Box [2] “All models are wrong but some are useful.” Thinking this way about models encourages the analyst to regard statistical modeling as an iterative process, involving multiple and often conflicting models that require careful consideration of the underlying assumptions

If it is assumed that much statistical analysis is carried out by nonstatisticians who apply the methods learned in graduate school, then conducting statistical analysis in the manner proposed has implications for teaching. It seems that emphasis should not be on teaching additional statistical techniques, but rather on studying epistemological issues with a focus on the different paradigms of advancing scientific knowledge, specifically the role and the limitations of the scientific research model Harrison and Andrangi [11] observe that "In the absence of any a priori theoretical foundation one should allow the empirical results to determine the explicit form of the functional relationship" If this indeed is our aim, then we should allow the data to do so through the combination of linear regression and exploratory techniques

## References

[1] Benzecri, F (1980) “Data Analysis,” Paris, France Dunod

[2] Box, G E P (1979) "Robustness in the Strategy of Scientific Model Building," in Robustness in Statistics, R L Launer and G N Wilkinson, (eds), New York, NY Academic Press 201–236

[3] Cale, E G, Gremillion, L L, and McKenney, J L (April 1979) "Price/Performance Patterns of U S Computer Systems," Communications of the ACM, Vol 22, No 4, 225–233

[4] Chatfield, C (1985) “The Initial Examination of Data,” Journal of the Royal Statistical Society, series A, Vol 148, Part 3 214–253

[5] Chatfield, C (1986) “Exploratory Data Analysis,” European Journal of Operations Research, Vol 23, 5–13

[6] Colton, K W, Brandeau, M L, and Tien, J M (January 1983) A National Assessment of Police Command, Control, and Communications Systems, National Institute of Justice U S Department of Justice, Washington D C

[7] Daniel, C., and Wood, F S (1980) “Fitting Equations to Data,” 2d ed New York, NY Wiley

[8] Davis, G B “A Systematic Evaluation of Publications for Promotion of MIS Academics,” Proceedings of the First International Conference on Information Systems, Philadelphia PA, December 8–10, 1980, 202–216, revised June 1986

[9] Galliers, R D, and Land, F F (December 1988) Rebuttal to “The Importance of Laboratory Experimentation in IS Research,” by S Jarvenpaa, Communications of the ACM, Vol 31, No 12, 1502–1505

[10] Hamilton, S., and Ives, B (Winter 1983) “The Journal Communication System for MIS Research” Data Base, Vol 14, No 2, 3–14

[11] Harrison, W., and Adrang, B (Winter 1986–87) "Programming Language and Software Development Cost," Journal of Management Information Systems, Vol 3, No 3, 101–10

[12] Jeffery, D R (June 1987) "A Software Development Productivity Model for MIS" Journal of Systems and Software, Vol 7, No 2, 115–125

[13] Ledbetter, W N, and Cox, J F (February 1982) "Are OR

techniques being used?" Industrial Engineering, Vol 9, No 2, 19–21

[14] McNeil, R (1977) "Interactive Data Analysis," New York, NY John Wiley

[15] Popper, K R (1965) “Conjectures and Refutations The Growth of Scientific Knowledge,” New York, NY Harper and Row

[16] Rizzi, A (1984) “On the Logical Aspects of Data Analysis,” Metron Rivista Internazionale di Statistica, Vol 42 No 2, 35–49

[17] Tukey, J W (November 1960) "Conclusions vs Decisions," Technometrics, Vol 2, No 4, 423–433

[18] Tukey, J W (1977) “Exploratory Data Analysis,” Reading, MA Addison-Wesley
