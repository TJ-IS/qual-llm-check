---
otero_id: 19047
otero_key: "ETRS65N8"
title: "Knowledge-based portfolio analysis for project evaluation"
authors: "Marko Bohanec; Vladislav Rajkovič; Brane Semolić; Aljana Pogačnik"
year: "1995"
journal: "Information & Management"
doi: "10.1016/0378-7206(94)00048-n"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Applications

# Knowledge-based portfolio analysis for project evaluation

Marko Bohanec $^{a,*}$ , Vladislav Rajkovič $^{a,b}$ , Brane Semolič $^{c}$ , Aljana Pogačnik $^{c}$

$^{a}$ Jožef Stefan Institute, Jamova 39, SI-61000 Ljubljana, Slovenia $^{b}$ University of Maribor, Faculty of Organizational Sciences, Prešernova 11, SI-64000 Kranj, Slovenia $^{c}$ Ministry of Science and Technology, Slovenska 50, SI-61000, Slovenia

## Abstract

A computer-based expert system for the evaluation of research and development projects is presented. The system was developed for The Ministry of Science and Technology of the Republic of Slovenia and in the process of evaluation and selection of projects submitted to the annual competition for funds. The system is based on an adapted portfolio matrix that determines the position of each project with respect to its contents and feasibility. The aggregation of these criteria is carried out by a qualitative multi-attribute decision model that was developed using an expert system shell: DEX. The model consists of a tree of criteria, supplemented by if-then rules. In addition to describing these components, the paper presents and discusses a practical application of the system.

Keywords: Project evaluation; Research and development projects; Multi-attribute decision making; Qualitative decision models; Expert systems; Portfolio analysis; Portfolio matrix

## 1. Introduction

The Ministry of Science and Technology of the Republic of Slovenia (MZT) finances or co-finances research and development (R and D) projects in the fields of technology, sociology, economy, and medicine on a regular basis. Several hundreds of projects submitted to the annual competition for funds must be evaluated for their suitability for funding from the state budget. Until recently, the evaluation was based on criteria that differed from one to another field. Expert groups that were involved in decision-making defined their objectives within these fields. The submitted projects were rated in accordance with these objectives. The overall value of projects that served for the final ranking of projects within individual fields were obtained by an aggregation procedure based on agreed weights of the partial objectives.

This method had a number of deficiencies and difficulties, primarily reflecting the non-comparability of the fields and the lack of general supervision over the large volume of projects. Specially notable was the problem of aggregating partial utilities corresponding to individual criteria into the final value, which involved the combining of different criteria by weighting and adding up the products of value and weight. The description criteria, themselves even also very difficult to rank numerically, played a major role in the project values. In addition, the procedure was not automated. It was practically impossible to conduct comparative analyses of projects on this basis; for example, with respect to content and feasibility. Moreover, no method of advising the submitters on ways to improve their projects was really available. All these problems were taken into account in developing the system described here.

The new system employs a specially adapted portfolio matrix that, in a simple graphic manner, determines the rank of an individual project with respect to its contents and feasibility. The value of a project is obtained by aggregating experts' evaluations based on multiple criteria. The aggregation is carried out by means of an system for multi-attribute decision-making named DEX-MZT. The basis of this system is a tree of criteria, supplemented by if-then rules which determine the aggregation of criteria. This facilitates transparent evaluation and analysis of projects. It is thus possible, in a simple and effective manner, to obtain an answer to the question: why has a certain project received a certain evaluation rather another?

In this paper, we present a modified portfolio method for the evaluation of projects. First, the portfolio matrix is presented and interpreted. This is followed by a more detailed description of the evaluation model that was developed using DEX. The paper concludes with the presentation of a practical application of the system.

## 2. The portfolio method for project evaluation

The portfolio method is one way that companies use for the formation of strategies $[18]$ . There are different methods of portfolio analysis. The well-known “BCG matrix” $[1]$ is a portfolio matrix method. Initially, it was used for evaluating a market situation by analysing the market share of a company and related flows. The portfolio concept has recently been extended to other areas, such as R and D. For example, since 1986 the Eastman Kodak company has been using its own portfolio method for analysing the risks of their R and D projects with the aim of increasing productivity in these activities $[14]$ .

<table><tr><td rowspan="2">ADDITIONAL REQUIREMENTS</td><td></td><td>“STARS”</td></tr><tr><td colspan="2">SATISFACTORY</td></tr><tr><td rowspan="2">UNSUITABLE</td><td colspan="2">TRANSITIONAL</td></tr><tr><td colspan="2">METHODOLOGICAL</td></tr></table>

Fig. 1. The portfolio matrix for project evaluation.

Using the portfolio concept to satisfy the need of the Ministry of Science and Technology [8,17,7], we developed our own portfolio matrix (Fig. 1). This is used for making decisions on project proposals after they have undergone the evaluation procedure. The data necessary for ranking a submitted project in one of the fields is obtained with the assistance of the DEX-MZT computer-based expert system. It produces three evaluation outputs: overall project, contents, and feasibility.

In the matrix, the evaluations of contents and feasibility are used. The first provides an assessment of the suitability of the project contents, and the second, feasibility, consists of an evaluation of the ability of the submitter of the proposal and an evaluation of the actual value of the project. In dealing with each, the two evaluations are used to determine the position of the project within the portfolio matrix. The project is then found to be in one of the following categories:

"STARS": which possess the highest evaluations in all respects and thus are most likely to have founds allocated to them;

SATISFACTORY: with an average evaluation (of second priority in the allocation of funds);

TRANSITIONAL: which are considered satisfactory only under certain conditions (projects in this category are only co-financed when there are sufficient funds available);

UNSUITABLE: which means that the project application is rejected;

ADDITIONAL REQUIREMENTS: whose subject is interesting, but which are poorly prepared (the submitter of the proposal is asked to supplement it with some required additions; when the proposal has been supplemented, it is re-assessed);

METHODOLOGICAL: which are well-prepared, yet do not have the proper contents (the project is rejected).

Depending on the availability of funds for a given budgetary year in the Programme of Technological and Other Development (PTOD), a strategy for co-financing projects within each field of the matrix is produced.

## 3. An expert system for project evaluation

There are two dimensions in the portfolio matrix: contents and feasibility. In evaluating these, it is necessary to consider a number of conditions and criteria set by the Ministry for each competition for funding. The project contents and feasibility are thus not evaluated directly, but by means of a model that consists of several dozen criteria, such as the project's contribution to mastering new technologies, its ecological effects and innovational contributions, the region and area of the project's influence, the submitter's references, etc. The assessment is carried out by requesting domestic and/or foreign reviewers to evaluate the project according to criteria given in questionnaires specially designed for the purpose. Each project is evaluated by two or three expert reviewers.

The evaluation models found in classical portfolio methods are mainly numerical [5], e.g., expressed with numbers between 0 and 100. A weight which expresses the significance with respect to the other criteria is formulated for each criterion. The weighted sum of partial evaluations according to individual criteria is then used to determine the final evaluation on the individual dimensions of the portfolio matrix. Users often ask where these numbers came from. This is a difficult question to answer, particularly because a number of descriptive criteria are also usually involved, and these are difficult to rate numerically. Furthermore, it is difficult to avoid at least some subjectivity and unreliability of the data. In general, models based on weights do not allow any complex interdependence of the criteria to be considered when modelling them in the overall evaluation.

Recently, an alternative approach was suggested for a similar problem of information system project selection $[13,16]$ . The approach is based on Saaty's Analytical Hierarchy Process $[15]$ and is particularly interesting for its capability of dealing with both tangible and intangible criteria. Unfortunately, it requires a pairwise comparison of projects, which is infeasible for our problem of evaluating several hundreds of projects.

In order to eliminate some of these problems, we employed an approach that combines multi-attribute decision-making $[5,12]$ with some elements of expert systems $[9,2,10]$ . The approach is supported by an expert system shell for multi-attribute decision-making called DEX $[3]$ . It helps in the creation of decision models that consist of non-numerical (qualitative) criteria. The criteria are hierarchically ordered into a tree structure. The aggregation of partial evaluations into the final evaluation is then carried out by decision rules of the if-then type. The weights are replaced by rules that define the interdependence of the criteria and their influence on the final evaluation. Thus the influence of a criterion can depend on its value, which corresponds in utility theory $[6]$ to the variability of the weights $[11]$ .

The development of the DEX-MZT expert system for the evaluation of projects took place in two stages. In the first, a model for the evaluation of the project contents and feasibility was developed using the shell. The model consists of two components: a tree of criteria and decision rules. In the second stage, a broader computer information system was developed. It includes subsystems for the acquisition of data on projects, the analysis of evaluation results and generating various reports; the portfolio matrix is one of these reports.

## 3.1. Criteria for project evaluation

The evaluation model is divided into two main parts: contents and feasibility (Fig. 2).

The suitability of the project contents is further divided into goals and objectives. The goals encompass a definition and declaration of the purposes to be achieved, where national and economic aspects are of particular importance. The objectives involve the definition of the results expected from the proposed project; e.g., a new product, new technology, or new solution. The two evaluations are the results of the assessment of further decompositions. Thus, the goals are assessed by means of direct and indirect advantages of the project, and the project's conformity with the development strategy of the Republic of Slovenia. The assessment of objectives is based on the project results, innovativeness of the project and appropriateness of the technology.

![](/api/attachments/ETRS65N8/fulltext/images/3cc3eee92fbe357616d87b080cf6e3cc52d1e80f288d783fceb0c3c10310272c.jpg)  
Fig. 2. Basic structure of evaluation criteria.

The project feasibility deals with both its external and internal feasibility. The assessment of the external feasibility involves a structure that evaluates the methodological and technical feasibility of the project, need for additional investment, appropriateness of the solution proposed, viability of the goals, the appropriateness of the methods, etc. Special emphasis is placed on the assessment of the professional qualifications and technical equipment of the project group and the professional qualifications and references of the group leaders. With internal feasibility, the project is assessed according to the goals of the Ministry, as well as the clarity of its goals, an assessment of the research strategy, organization of the project, and consideration of application conditions.

Since the PTOD programme includes the co-financing of projects in technological and other development areas (such as sociology and economy), two criteria models were developed for evaluating technological and socio-economic projects, respectively. Fig. 3 shows some of the structure of criteria for the evaluation of technological projects: this is intended for evaluating project goals. The remaining three sub-trees of criteria that appear in Fig. 2 (i.e., objectives, external and internal feasibility) are defined in a similar way.

The entire tree for the evaluation of technological projects consists of 78 criteria. There are 48 basic criteria on the leaves of the tree. The tree for the evaluation of socio-economic projects is a little smaller, containing 50 criteria, of which 30 are basic.

All criteria in the trees are qualitative. Thus instead of numbers, descriptive values are represented by words; the set of possible words is defined for each individual criterion. Thus a criterion such as Employment generation can be decreases, maintains, or increases. Similarly, the Area of influence can be community, region, or broader.

The criteria at the top of the tree (Project, Contents, and Feasibility) use a five-level Likert-type scale: unsuitable, less suitable, suitable, more suitable, and very suitable, so each project is classified into one of the five categories. Using these scales, the portfolio matrix is decomposed into 25 smaller fields that are illustrated in Figs. 5 and 6.

![](/api/attachments/ETRS65N8/fulltext/images/e04e204d70870f8dd27338369483e88e90d0ff95a522af3bde9a5345ec3c8c7a.jpg)  
Fig. 3. Structure of criteria for the evaluation of goals.

## 3.2. Decision rules

The tree of criteria defines the structure of the evaluation model by defining the criteria and their interdependence. In the final outcome, this means that the overall evaluation of the project depends on the 48 or 30 basic criteria. On the other hand, the criteria tree does not define the aggregation, i.e., the procedure that combines the values the final evaluation. In DEX, the aggregation procedure is defined by decision rules, an example of which is shown in Table 1.

The rules determine the evaluation of the criterion evaluation of project goals based on three criteria: Direct benefits, Indirect social benefits and Conformity of the goals with the development strategy of the Republic of Slovenia (RS). The first two rules determine the conditions by which the project goals are evaluated as unsuitable. This is whenever

(1) the project goals do not conform with the development strategy of the RS (regardless of the evaluation of the remaining two criteria, denoted by an asterisk), or when

(2) the project does not have any direct benefits. On the other hand the goals are suitable whenever the project offers great direct benefits and conforms to the development strategy of the RS (rule 11). The remaining rules can be interpreted similarly, with the signs $\leq$ and $\geq$ represent “worse or equal” and “better or equal”, respectively.

Table 1  
An example of decision rules for the evaluation of goals

<table><tr><td></td><td>Direct benefits</td><td>Indirect benefits</td><td>Strategy of the RS</td><td>GOALS</td></tr><tr><td>1.</td><td>*</td><td>*</td><td>no</td><td>unsuitable</td></tr><tr><td>2.</td><td>none</td><td>*</td><td>*</td><td>unsuitable</td></tr><tr><td>3.</td><td>few</td><td>≤ average</td><td>≥ partial</td><td>less suit.</td></tr><tr><td>4.</td><td>few, average</td><td>none</td><td>partial</td><td>less suit.</td></tr><tr><td>5.</td><td>great</td><td>none</td><td>partial</td><td>suitable</td></tr><tr><td>6.</td><td>average</td><td>few, average</td><td>≥ partial</td><td>suitable</td></tr><tr><td>7.</td><td>few</td><td>great</td><td>≥ partial</td><td>suitable</td></tr><tr><td>8.</td><td>average</td><td>≥ few</td><td>partial</td><td>suitable</td></tr><tr><td>9.</td><td>average</td><td>≤ average</td><td>yes</td><td>suitable</td></tr><tr><td>10.</td><td>great</td><td>≥ few</td><td>≥ partial</td><td>very suit.</td></tr><tr><td>11.</td><td>great</td><td>*</td><td>yes</td><td>very suit.</td></tr><tr><td>12.</td><td>≥ average</td><td>great</td><td>yes</td><td>very suit.</td></tr></table>

Obviously, there are many more such rules in the model. For each aggregate criterion (such as Goals), a similar table is defined. In the entire model for technological projects there are 30 defined in this way, and in the model for socioeconomic projects there are 20 tables of rules (some are equal in both models). The tables were defined by a group of experts at the Ministry of Science and Technology using the DEX computer system. Experts contributed the contents of the rules, and the system made sure that the tables were complete (covering all possible combinations of the evaluation criteria) and consistent (an improvement of a single lower-level criterion could never decrease the overall value of the project).

Decision rules therefore define the conditions under which a project is ranked, taking into account the conditions and long-term policy of the Ministry of Science and Technology to encourage high quality (innovative, technologically advanced, and socially significant) R and D projects.

## 3.3. Project evaluation

The initial data for the evaluation of projects is provided by the expert reviewers who answer questions on a special questionnaire. A project is evaluated by at least two reviewers. Apart from some general questions (such as the project's code, title, and name of the reviewer), the questions precisely correspond to the basic criteria of the evaluation model. Therefore, the questionnaire for technological projects has 48 such questions. The reviewers answer the questions by choosing one of the possible answers. For instance, the first two questions that correspond to the first two basic criteria for evaluating the goals in Fig. 3 are:

A1. Assess the extent to which the project contributes to the mastering of new technologies:

(1) no contribution

(2) contributes to a minor degree

(3) contributes to a greater degree

PROJECT: 9/X-999/92 Sample project
EVALUATION: 3.943 3.846-4.040

A2. Asses the project's ecological impact with respect to decreasing the load on the environment and solving other ecological problems:

(1) no impact

(2) minor impact

(3) great impact

The data collected in this way is then entered into the DEX-MZT system. A project is described by:

(1) General data: project code, title and team, research field, and project type (group): industrial-developmental, precompetition, sociological and discovery of raw materials.

(2) Reviewer's evaluations: The evaluations are represented by the 48 (30 for socio-economic projects) items from the questionnaire.

In the next stage, DEX-MZT evaluates the projects. The evaluation is carried out according to the tree of criteria from the basic criteria up. The method of aggregation is determined by the decision rules. The result is its classification into one of the five priority classes of content and feasibility. In the portfolio matrix, this means positioning into one of the 25 fields (Figs. 5 and 6). The exact project position within the field is determined by a calculation based on the ranking of projects within classes and the calculation of average criteria weights. The weights are derived from decision rules. The procedure is presented in [4].

At the end of the evaluation, each project is placed in the portfolio matrix; there are as many points as reviewers evaluating the project. The system calculates the average of these points, but merely for information purposes: it is important to know how much the evaluations differ from one another. If there are significant differences, it is necessary to coordinate the reviewers' answers, or obtain additional opinions from new reviewers, or formulate the evaluation more precisely during the final classification, which is carried out by an expert group.

In addition to the position of the project in the portfolio matrix, the evaluation yields partial results from each reviewer for all the aggregate criteria in the tree. Each is presented with a descriptive value (class) and a number that determines the project's ranking within the class. In the final, detailed report, the particularly advantages and disadvantages of the project are highlighted.

<table><tr><td></td><td colspan="2">Reviewer 1</td><td colspan="2">Reviewer 2</td></tr><tr><td>PROJECT</td><td>4.040</td><td>more suit.</td><td>3.846</td><td>more suit.</td></tr><tr><td>CONTENTS</td><td colspan="2">5.076 + very suit.</td><td colspan="2">4.379 + more,very</td></tr><tr><td>GOALS</td><td colspan="2">4.338 + very suit.</td><td colspan="2">3.611 + suit.,very</td></tr><tr><td>DIR_BENEF</td><td colspan="2">4.198 + great</td><td colspan="2">4.007 + great</td></tr><tr><td>DEV_BENEF</td><td colspan="2">3.866 + great</td><td colspan="2">3.566 + great</td></tr><tr><td>new tech</td><td colspan="2">3.000 + greater</td><td colspan="2">3.000 + greater</td></tr><tr><td>ecologic</td><td colspan="2">2.000 minor</td><td colspan="2">1.000 - none</td></tr><tr><td>EMPLOYMENT</td><td colspan="2">2.500 + greater</td><td colspan="2">2.500 + greater</td></tr><tr><td>emp-gen</td><td colspan="2">2.000 maintain.</td><td colspan="2">2.000 maintain.</td></tr><tr><td>emp_struc</td><td colspan="2">3.000 + greater</td><td colspan="2">3.000 + greater</td></tr><tr><td>ECON_BENEF</td><td colspan="2">3.689 + great</td><td colspan="2">2.860 average</td></tr><tr><td>MARKETING</td><td colspan="2">3.500 suit.</td><td colspan="2">3.388 suit.</td></tr><tr><td>new mark.</td><td colspan="2">2.000 + yes</td><td colspan="2">2.000 + yes</td></tr><tr><td>exports</td><td colspan="2">2.000 minor</td><td colspan="2">3.000 + greater</td></tr><tr><td>imports</td><td colspan="2">2.000 minor</td><td colspan="2">1.000 - none</td></tr><tr><td>profit</td><td colspan="2">3.000 + greater</td><td colspan="2">2.000 minor</td></tr><tr><td>energ-mat.</td><td colspan="2">1.000 - none</td><td colspan="2">1.000 - none</td></tr><tr><td>IND_BENEF</td><td colspan="2">3.666 + great</td><td colspan="2">2.677 * no,min,av,gr</td></tr><tr><td>LEVEL</td><td colspan="2">2.500 + high</td><td colspan="2">2.037 * none,av,high</td></tr><tr><td>area</td><td colspan="2">2.000 region</td><td colspan="2">2.000 * com,reg,bro</td></tr><tr><td>field</td><td colspan="2">2.000 + interbr.</td><td colspan="2">1.000 - branch</td></tr><tr><td>restruct.</td><td colspan="2">2.000 + yes</td><td colspan="2">1.500 * no,yes</td></tr><tr><td>defense</td><td colspan="2">1.000 - none</td><td colspan="2">2.000 * none,min,great</td></tr><tr><td>strat_rs</td><td colspan="2">3.000 + yes</td><td colspan="2">2.000 partial</td></tr><tr><td>OBJECTIV</td><td colspan="2">3.814 + very suit.</td><td colspan="2">3.814 + very suit.</td></tr><tr><td colspan="5">...... (here follow the evaluations of objectives)</td></tr><tr><td>FEASIB</td><td colspan="2">2.960 suit.</td><td colspan="2">2.960 suit.</td></tr><tr><td colspan="5">...... (here follow the evaluations of feasibility)</td></tr></table>

Fig. 4. A part of the detailed project report.

A part of a detailed report is shown in Fig. 4. The left hand side presents the structure of the criteria tree; the names of the basic and aggregate criteria are written in lower case and capital letters, respectively. Since the project was evaluated by two reviewers, the report contains two columns of results. The evaluation of the basic criteria was defined by the reviewers, and the remaining ones were derived according to the evaluation procedure. Each evaluation is presented as two values: descriptive and numeric. Particularly good and bad evaluations are highlighted by the signs “+” and “−”, respectively. In both cases, the project was classified as suitable, receiving the average value of 3.94.

It seems that the project data available to the second reviewer in Fig. 4 were insufficient: did not answer three questions: about the area of project influence and its impact on the defense and restructuring of the economy. The system is designed to evaluate projects in this case, too.

Table 2

When a data item is missing, it tests all the possible values (for example, community, region and broader with the Area criterion). In this case, the result is generally less precise and is expressed as a distribution of values. The project may be ranked into several classes simultaneously, the numerical values become intervals instead of single numbers, and the point in the matrix portfolio changes into a line or even a rectangle. In the project of Fig. 4, the missing input data from the second reviewer caused an imprecise evaluation of the indirect benefits. When combining these with the remaining criteria, the imprecision was reduced, so the project was finally ranked into one class, more suitable. The numerical evaluation of the contents yielded the interval of 3.96–4.80. Thus, the project is represented by a line in the portfolio matrix (Fig. 5).

In addition to detailed reports on individual projects, DEX-MZT also prepares a number of reports on groups of projects. Important groups of projects are: all, those from a certain research field, those of a certain type and all evaluated by a given reviewer. A group report typically presents various statistical data, such as the number of projects or individual evaluations in the group, the number of fields and number of reviewers in the group, the average of final contents and feasibility evaluations and their distribution. Another type of a group report is the portfolio matrix itself, with drawn positions of all projects in the group (an example is shown in Fig. 6).

![](/api/attachments/ETRS65N8/fulltext/images/9a302c0b956bda62ba3bcc75851641396bd3feef5115913734231743f67ce576.jpg)  
Fig. 5. Position of the project from Fig. 4 in the portfolio matrix.

![](/api/attachments/ETRS65N8/fulltext/images/735105ae0aef2644ab0b5fe4e4efe7654c29cd2aa606ba91adcf25ab1602e933.jpg)  
Fig. 6. Position of all the evaluated projects in the portfolio matrix.

In the final stage of decision-making, the reports resulting from the evaluation of projects are forwarded to expert groups constituted at the level of research fields. The reports provide the basis for decision-making, which then actually takes place in the groups and whose result is the final evaluation and priority ranking of the projects.

## 4. Application and results

The DEX-MZT system was first used in 1992, when 516 projects were evaluated from four larger groups: industrial-developmental, precompetition, sociological, and discovery of raw materials. The projects included 31 fields of research. The evaluation was performed on the basis of 1094 questionnaires contributed by 90 reviewers.

A global overview of the results is presented in Fig. 6, where the position of all the 1094 evaluations are shown in the portfolio matrix. For the results that were imprecisely evaluated due to unavailable data, only the average of the obtained intervals of values is given. Table 2 summarizes the average and borders of the overall evaluations of the project and the partial evaluations of the contents and feasibility.

Average and bounds of the obtained numerical evaluations

<table><tr><td>Evaluation</td><td>Average</td><td>Min.</td><td>Max.</td></tr><tr><td>Project as whole:</td><td>2.41</td><td>0.54</td><td>5.34</td></tr><tr><td>Contents:</td><td>3.58</td><td>0.60</td><td>5.45</td></tr><tr><td>Feasibility:</td><td>2.45</td><td>0.54</td><td>5.35</td></tr></table>

From both of these it is evident that the projects are spread throughout the space. We thus come across “stars”, as well as wholly unacceptable projects. As expected, there are more of the latter than the former. In certain fields of the matrix, a greater number of evaluations can be observed; this is probably caused by the similarity of projects, but also by the partitioning of the decision space based on decision rules.

There is an interesting relation between the evaluation of contents and feasibility. The contents evaluation is generally better than feasibility and, on average, exceeds it by one class. One of the reasons for this could be that the part of the model for evaluating feasibility is stronger than the other. A later survey of the results in expert groups showed that this was not the case, and that the results realistically expressed the actual state of the submitted projects.

The obtained results were later found in the expert groups responsible for the individual research fields. The groups' tasks primarily encompassed the following:

\- verification of project data and evaluation results together with their analysis, explanation, and interpretation,

\- coordination, in the case of large differences, between the reviewers' assessments and evaluations,

\- decisions related to the impreciseness and uncertainty of data and results (acquisition and evaluation of additional data or opinions),

\- final priority ranking of projects within the research field.

Some groups created their own proposals on the classification of projects, independent from our results. In general, the deviations were small, justifying the evaluation model. Greater deviations occurred only in the case of socio-economic projects that were, on average, rather poorly rated and, according to the opinion of experts, unjustly so. The corresponding evaluation model was therefore considered to be too strict; it will have to be modified in future.

The expert groups also reported that it was difficult to manage cases where great differences occurred between reviewers evaluating a given project, and when the evaluations were imprecise due to the missing data. This problem was solved with the help of a third reviewer, or by using additional assessments made by professionals from the Ministry of Science and Technology.

Finally, a problem should be mentioned that resulted from the relative newness of the methodology and the large number of people participating in the decision-making process. Due to a lack of time in training, the level of knowledge of the decision methodology differed greatly between the participants. This caused differences in the interpretation of certain criteria, the corresponding questions, and results. The advantages that the technology could provide (transparency of data and results, the possibility of analysing variants and explaining results) were not always utilized. This problem will be solved in future by means of a broader and timelier training of expert groups and reviewers.

## 5. Conclusion

Despite the minor deficiencies, we have found that the approach has fulfilled most of our expectations and revealed considerable advantages in comparison with other approaches. In particular, we emphasize the use of the qualitative decision-making model, which was suitable in a field where judgment prevails and it is thus difficult to give answers numerically. This kind of model is comprehensible to a wide range of users in the decision-making process. Its transparency facilitates a high level of verification and explanation of results. The model is based on the use of decision rules defined by experts from the Ministry of Science and Technology of the Republic of Slovenia, who found them very convenient.

The use of a well-defined decision model allowed a more systematic acquisition of data on projects, as well as the automation of the evaluation procedure. The result of the procedure was information that was important for making and justifying decisions in the expert groups. It allowed interactive comparisons of projects between and within groups, as well as detailed reports on individual projects.

The system in no way diminishes the authority of the expert groups, who are actually responsible for the proposed decisions. The system's role is primarily to aid in the systematic collection of large amounts of data, its processing, presentation of results and sensitivity analysis.

Further work related to the DEX-MZT system will continue. First, some modifications and extensions of the decision models will be necessary, particularly for socio-economic projects. Also, it will be necessary to reconsider and define in greater detail some of the criteria in the questionnaire.

## Acknowledgements

The authors wish to thank their colleagues at the Ministry of Science and Technology for their help in creating the model, particularly the Minister Professor Peter Tancig for his encouragement and direction of the project. Numerous project reviewers and members of expert groups also contributed a great deal to the results. We also thank Professor Edgar H. Sibley and anonymous reviewers whose comments and suggestions considerably contributed to the paper.

## References

[1] Armstrong, M., A handbook of management techniques, Kogan Page, London, 1987.

[2] Benders, J. and Manders, F., “Expert systems and organizational decision-making”, Information and Management 25, North-Holland, 1993, pp. 207–213.

[3] Bohanec, M. and Rajkovič, V., “DEX: An expert system shell for decision support”, Sistemica 1(1), 1990, pp. 145–157.

[4] Bohanec, M., Urh, B. and Rajkovič, V., “Evaluating options by combined qualitative and quantitative methods”, Acta Psychologica 80, North-Holland, 1992, pp. 67–89.

[5] Chankong, V. and Haimes, Y.Y., Multiattribute decision making: Theory and methodology, North-Holland, 1983.

[6] French, S., Decision theory: An Introduction to the mathematics of rationality, New York: Wiley, 1986.

[7] Gmeiner, P., “The evaluation of industrial, developmental, and precompetition research in Slovenia in 1990/91 from national and economic point of view” (in Slovene), IB-Journal for Planning 1-2, Ljubljana, 1991, pp. 34–39.

[8] Hauc, A. and Semolič, B., “Project oriented strategic management”, Proc. 11th INTERNET World Congress on Project Management, Florence, 1992.

[9] Klein, M. and Methlie, L.B., Expert systems: A decision support approach, Addison-Wesley, 1990.

[10] Krisper, M., Bukvič, V., Rajkovič, V. and Sagadin, T., "Strategic planning with expert system based portfolio analysis", EXPERSYS-91: Expert system applications (eds. J. Hasemi, J.G. Gouardères, J.P. Marciano), IITT-International, 1991.

[11] Mandić, J.N. and Mamdani, H.E., “A multi-attribute decision-making model with fuzzy rule-based modification od priorities”, TIMS/Studies in Management Sciences 20, 1984.

[12] O'Keefe, R.M., "The evaluation of decision-aiding systems: Guidelines and methods", Information and Management 17, North-Holland, 1989, pp. 217–226.

[13] Muralidhar, K., Santhanam, R. and Wilson, R.L., “Using the analytic hierarchy process for information system project selection”, Information and Management 18, North-Holland, 1990, pp. 87-95.

[14] Rzasa, P.V., Faulkner, W. and Sousa, N., “Analysing R and D portfolios at Eastman Kodak (A methodology based on decision and risk analysis can improve R and D productivity)”, Research and Technology Management, 1991.

[15] Saaty, T.L., The analytic hierarchy process, McGraw-Hill, 1980.

[16] Schneiderjans, M.J. and Wilson, R.L., “Using the analytic hierarchy process and goal programming for information system project selection”, Information and Management 20, North-Holland, 1991, pp. 333-342.

[17] Semolič, B., “The project of formulating the Slovenia’s national research program”, NORDNET ‘92, Helsinki, 1992.

[18] Sharplin, A., Strategic management, McGraw-Hill, 1985.

![](/api/attachments/ETRS65N8/fulltext/images/da5fc96efdc6324c06a71dae8f9adc0ee01eaf552b02c748fc595aa52ac3d1e0.jpg)

Marko Bohanec is a researcher in the Artificial Intelligence Laboratory at the Jožef Stefan Institute in Ljubljana, and assistant professor in information systems at the Faculty of Organizational Sciences, University of Maribor. He obtained his Ph.D. in Computer Science at the Faculty of Electrical Engineering and Computer Science, University of Ljubljana. His research interests are in decision support systems, expert systems and ma chine learning. He has published in journals such as Machine Learning, Acta Psychologica, and Sistemica.

![](/api/attachments/ETRS65N8/fulltext/images/3fdde2c0356232cdab36a1e424db25d8334d64c710611151fc24f05708e4ad37.jpg)

![](/api/attachments/ETRS65N8/fulltext/images/2bd22976d0dda62b98bbac3679ad1222877f563bc0f7b6ac89b6928aefadd565.jpg)

Vladislav Rajkovič is a professor of information systems at the Faculty of Organizational Sciences, University of Maribor. He also works with the Artificial Intelligence Laboratory at the Jožef Stefan Institute in Ljubljana. His research interests focus on artificial intelligence methods for supporting decision processes. He has published in journals such as IEEE Trans. on Systems, Man, and Cybernetics, Acta Psychologica, and Sistemica.

Brane Semolič is the president of the Jewellery Company in Celje and professor at the Faculty of Business Administration, University of Maribor. He holds the Ph.D. degree in MIS. His professional interests include strategic management, project management and strategic information systems.

![](/api/attachments/ETRS65N8/fulltext/images/3482660f38b35e6dd17897ba780c8f972e5c5b65d1ac7de1dc8edbbe9401221f.jpg)

Aljana Pogačnik is the adviser to the Minister of Science and Technology of the Republic of Slovenia. She graduated from Archeology Department at the University of Ljubljana. Currently she is a coordinator of the Research and Development Program and in charge for computer-supported systems for project evaluation.
