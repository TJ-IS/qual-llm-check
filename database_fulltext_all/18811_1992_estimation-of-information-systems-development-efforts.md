---
otero_id: 18811
otero_key: "BTK6J8A2"
title: "Estimation of information systems development efforts"
authors: "François Bergeron; Jean-Yves St-Arnaud"
year: "1992"
journal: "Information & Management"
doi: "10.1016/0378-7206(92)90026-c"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
SOS

# Estimation of information systems development efforts

François Bergeron

Université Laval, Québec, Canada

Jean-Yves St-Arnaud

Donohue Inc., Québec, Canada

This study attempts to identify estimation methods, underlying variables and factors that can be used to improve estimates of information system development efforts. To accomplish this, 89 development projects from 63 organizations were analyzed. The results indicate that (1) qualitative methods are related to accurate estimates, (2) the relationships between the factors, the underlying variables, and the accuracy of the estimate vary among development phases and generally tend to improve based upon the phase at which the estimate is made, and (3) the proportion of variance in the accuracy of the estimates explained by the factors increases dependent upon the phase at which the estimate is made.

Keywords: Cost estimates, Development efforts, Estimation factors, Estimation techniques, Estimation methods

![](/api/attachments/BTK6J8A2/fulltext/images/abed64584cd0b7eda1836558342c19d4570a8ccd0322e67831f494482a5b9970.jpg)

François Bergeron is an associate professor and director of the Département systèmes d'information organisationnels Université Laval, Québec City, Canada. He received a Ph.D. from the Anderson Graduate School of Management, University of California, Los Angeles, and an M.Sc. in Economics and an MBA from Laval University. His current research interests focus on the planning and management of information systems. Dr. Bergeron has consulted for public and private organizations and has published in various journals such as MIS Quarterly, Information and Management, Journal of Management Information Systems and Journal of Systems Management. He is a member of SIM, TIMS and ACM. Correspondence to: François Bergeron, Département Systèmes d'Information Organisationnels, Faculté des Sciences de l'Administration, Université Laval, Québec, Québec G1K 7P4, Canada. Bitnet: bergerof@lavalvm1.

## Introduction

Empirical research has indicated that it is often quite difficult to estimate the effort required to develop an information system (IS). Boehm [1981] and Augustine [1979], for example, reported that for 100 systems in the U.S. Defense Department, the average variance of the actual IS effort from the estimated IS effort was approximately 33 percent. McKeen [1983] found that for a sample of 32 IS projects which were developed in the private sector, only 25 percent were completed within their estimated budgets and for those that were off the mark they were about 25 percent over or under budget. Topping [1985] found that for 22 government IS projects the average deviation from the estimate was 40 percent. The median deviation was 26 percent and 90 percent of the development efforts turned out to be above their estimates.

The accuracy of IS development efforts is important for a variety of reasons. First, accurate IS development efforts could help classify and prior-

![](/api/attachments/BTK6J8A2/fulltext/images/baa7c79e120b97ddacaebbde6db8c0966647619933d156dfeaa14ef9e75bb745.jpg)

Jean-Yves St-Arnaud, MBA, is information systems development manager at Donohue Inc, a pulp and paper company. Prior to this appointment, he was an information systems consultant for Groupe DMR Inc, an international consulting firm. Mr. St-Arnaud has worked as an analyst and project manager on numerous information systems development projects for the last twelve years, mainly in the manufacturing sector. As project manager, Mr. St-Arnaud has been ininvolved in many information systems development costs appraisals, thus he has developed a strong interest in methods and techniques allowing precise estimates. Mr. St-Arnaud is a member of the Fédération de l'informatique du Québec and the Canadian Association for Production and Inventory.

itize development projects with respect to an overall IS plan [Buss, 1982]. Second, projects could be easier to manage and control when resources are matched better to real needs [De Marco, 1982]. Third, management practices such as IS cost chargeout systems [Bergeron, 1986] might be better accepted by users who expect actual IS development costs to be in line with estimated costs. Fourth, the structuring of IS departments as profit centers [Allen, 1987] could be more easily implemented if managers were provided with better planning tools for IS development expenses. The purpose of this research was to learn which estimation methods, underlying variables and factors used to make estimates are indeed related to more accurate estimates.

## Review of the research

Studies concerned with IS development cost estimation deal with the identification of significant software parameters that can be assessed at the start of a project to get an estimate of the total software development effort. Studies in this area include Nelson [1966], Aron [1976], Putnam [1980], Boehm [1981] and Wolverton [1984]. The software cost estimation literature can be partitioned into four categories: (1) estimation theory, (2) estimation methods, (3) underlying variables, and (4) accuracy of estimation methods.

## Estimation theory

Theory on software cost estimation is sparse. Indeed, there are only a few concepts unto which software appraisers agree. These basic concepts help to understand the limits inherent to software cost estimation. They are as follows: (1) the use of lines of codes as a software metric, (2) the quantification of effort, (3) the schedule of work, and (4) the size of development projects.

Lines of codes has been used in several software costing models (e.g. Boehm [1981], Putnam [1980], Aron [1976]). It is, however, a poor measure of effort if no attempt is made to control for the language used. As reported by Jones [1986], the number of lines of codes may vary by a factor of 50 between different languages and there is a range of as much as 5 to 1 between various definitions of what a line of code really is. A specific problem related to actual software cost estimation models is the use of lines of codes as a predictor of software size. At the earlier phases of systems development, lines of codes are more an output characteristic than an input attribute which may be very difficult to estimate beforehand. Estimation methods based on an initial estimate of lines of codes are therefore difficult to apply at the preliminary and feasibility phases. The quantification of effort in person-month is another problematic metric. Brooks [1982] pointed out that persons and months are not interchangeable commodities and that adding people on a system job does not reduce the total length of development by the same proportion. The optimal schedule of work is related to this latter point. Some schedules, such as the one proposed by McKeen [1983], with an emphasis on earlier phases of the system development life cycle could be better than the bell-shape Rayleigh curve used by Boehm [1981]. Few cost estimation models take this point into account. Finally, it has been observed by Brooks [1982], and Boehm [1981] that large projects show a lower productivity than small projects, i.e., bigger projects take a relatively longer development time.

## Estimation methods

A software cost estimation method is an approach used by an appraiser to estimate the scope of a development project usually in terms of person-days. In spite of the variety of terminology, nine estimation methods can be identified in the literature (Figure 1). Boehm [1981] and Wolverton [1984] strongly recommended the simultaneous use of more than one method and the combination of results to arrive at an estimate. Mostly because they are not exclusive from one another. These estimation methods are briefly presented here along with references to the authors who mentioned them (most of the definitions are adapted from Boehm [1981]).

1. Personal Experience: This method is based on the estimator's judgment, knowledge and experience with former development projects [Benbasat and Vessey, 1980].

2. Expert judgment: One or more experts are consulted to obtain an estimate of the proposed project, perhaps with the aid of an expert-consensus mechanism such as the Delphi technique [Boehm, 1981].

<table><tr><td>Methods</td><td>Benbasat &amp; Vessey (1980)</td><td>Wolverton (1974,84)</td><td>Aron (1976)</td><td>Boehm (1981,84)</td></tr><tr><td>Experience</td><td>x</td><td></td><td></td><td></td></tr><tr><td>Expert</td><td></td><td></td><td></td><td>x</td></tr><tr><td>Analogy</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Algorithmic</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Top-down</td><td></td><td>x</td><td></td><td>x</td></tr><tr><td>Bottom-up</td><td></td><td>x</td><td>x</td><td>x</td></tr><tr><td>Restriction</td><td></td><td></td><td>x</td><td>x</td></tr><tr><td>Price to win</td><td></td><td></td><td></td><td>x</td></tr><tr><td>Standards</td><td>x</td><td>x</td><td></td><td></td></tr></table>

Fig. 1. Estimation methods mentioned in literature.

3. Analogy: This method is based on a comparison of similar past projects with the proposed one. It involves reasoning by analogy with one or more completed projects to relate their actual costs to an estimate of the cost of a similar new project [Benbasat and Vessey, 1980; Wolverton, 1974, 1984; Aron, 1976; Boehm, 1981, 1984].

4. Algorithmic: This technique refers to the use of one or more algorithms which produce a software cost estimate as a function of a number of variables which are considered to be the major costs drivers. The COCOMO scale [Boehm, 1981] is an example of an algorithmic model (Benbasat and Vessey, 1980; Wolverton, 1974, 1984; Aron, 1976; Boehm, 1981, 1984).

5. Top-down: An overall estimate for a project is derived from global properties of the system to be developed. The global estimate is then split up among the principal system components [Wolverton, 1974; Boehm, 1981, 1984].

6. Bottom-up: Each system component is separately estimated and the results are aggregated to produce an estimate for the overall job [Wolverton, 1974; Aron, 1976; Boehm, 1981, 1984].

7. Restriction: The estimate corresponds to the budget or to the number of person-days available to develop the system [Aron, 1976; Boehm, 1981, 1984].

8. Price to win: The cost estimate developed by this method is equated to the price, or number of person-days, believed necessary to win the job, i.e., to obtain the contract or the authorization to develop the system [Boehm, 1981, 1984].

9. Standards: The estimate relies on standards of performance that have been systematically developed as stable reference points from which new tasks can be calibrated [Benbasat and Vessey, 1980; Wolverton, 1974, 1984].

## Underlying variables

A software cost estimation method is usually independent of the variables that are used to make the estimate. Whatever method an appraiser uses, such as expert, analogy or standards, there is a multiplicity of variables (also called “parameters”, “software attributes” and “cost drivers”) that can be taken in consideration to make the estimate and which will vary dependent upon the appraiser.

Since there are numerous variables that can influence the amount of effort needed to complete a system development project, they have been grouped into eight main factors for the purpose of presentation: users, data base, personnel, size, language, time constraints, project management environment, complexity. The groupings result from a factor analysis made on data collected in this survey and for which the details are presented later in this paper. Figure 2 presents the variables used in the most frequently cited software cost estimation methods. Two factors (data base and size) represent systems characteristics that cannot easily be modified or manipulated by the project team once they are specified. The other factors are more of a managerial nature and therefore are more easily manipulable. In this latter case, different project structure and management may have an impact on the size of the software development estimate without any immediate consequence on the product delivered.

<table><tr><td rowspan="9"></td><td>N</td><td>W</td><td>A</td><td>W</td><td>P</td><td>B</td><td>A</td></tr><tr><td>E</td><td>O</td><td>R</td><td>A</td><td>U</td><td>O</td><td>L</td></tr><tr><td>L</td><td>L</td><td>O</td><td>L</td><td>T</td><td>E</td><td>B</td></tr><tr><td>S</td><td>V</td><td>N</td><td>S</td><td>N</td><td>H</td><td>R</td></tr><tr><td>O</td><td>E</td><td></td><td>T</td><td>A</td><td>M</td><td>E</td></tr><tr><td>N</td><td>R</td><td></td><td>O</td><td>M</td><td></td><td>C</td></tr><tr><td></td><td>T</td><td></td><td>N</td><td></td><td></td><td>H</td></tr><tr><td></td><td>O</td><td></td><td>&amp; al</td><td></td><td></td><td>T</td></tr><tr><td></td><td>N</td><td></td><td></td><td></td><td></td><td>&amp; al</td></tr><tr><td colspan="8">Variables</td></tr><tr><td colspan="8">USERS</td></tr><tr><td>Content of documentation to be produced</td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>User familiarity with information systems</td><td></td><td>X</td><td>X</td><td>X</td><td></td><td></td><td></td></tr><tr><td>Number of users or groups of users</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Geographical dispersion of users</td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>Availability of users</td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>Quality of user needs identification</td><td>X</td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td></tr><tr><td colspan="8">DATA BASE</td></tr><tr><td>Level of security to be incorporated</td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Number of data bases or files</td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td>X</td></tr><tr><td>Number of information elements handled</td><td></td><td></td><td>X</td><td>X</td><td></td><td>X</td><td>X</td></tr><tr><td>Number of routines</td><td>X</td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Number of reusable program applications</td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td></tr><tr><td colspan="8">PERSONNEL</td></tr><tr><td>Qualifications of personnel</td><td></td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td></tr><tr><td>Exp.pers w. type proc.(interactive, differed)</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Exp.pers w. system complexity</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td>X</td><td></td></tr><tr><td>Personnel turn-over</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Stability of technological environment</td><td>X</td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td></tr><tr><td colspan="8">SIZE</td></tr><tr><td>Type of processing (online, offline)</td><td>X</td><td>X</td><td></td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>Number of functions (additions or modifications)</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Number of reports or displays</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td></tr><tr><td>Number of queries to develop</td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td></tr><tr><td>Number of interfaces with other systems</td><td>X</td><td></td><td>X</td><td>X</td><td></td><td></td><td>X</td></tr><tr><td colspan="8">LANGUAGE</td></tr><tr><td>Technological risk (use of new tool/technique)</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Use of productivity tools</td><td></td><td>X</td><td></td><td></td><td>X</td><td>X</td><td></td></tr><tr><td>Programming language</td><td>X</td><td>X</td><td></td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>Exp.pers.w. programming language</td><td></td><td>X</td><td>X</td><td>X</td><td></td><td>X</td><td></td></tr><tr><td>Exp.pers.w. computer</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td>X</td><td></td></tr><tr><td colspan="8">TIME CONSTRAINTS</td></tr><tr><td>Number of persons involved in development</td><td></td><td>X</td><td></td><td>X</td><td>X</td><td>X</td><td></td></tr><tr><td>Time allotted (overtime requirements)</td><td></td><td>X</td><td></td><td>X</td><td>X</td><td>X</td><td></td></tr><tr><td>Computer time available</td><td></td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td></tr><tr><td colspan="8">PROJECT MANAGEMENT ENVIRONMENT</td></tr><tr><td>Project management structure</td><td>X</td><td></td><td>X</td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>Development methodology used</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Development policy (within the organization)</td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td></tr><tr><td colspan="8">COMPLEXITY</td></tr><tr><td>Complexity of the system/product</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>Complexity of the system/product-number instructions</td><td></td><td>X</td><td></td><td>X</td><td>X</td><td>X</td><td></td></tr><tr><td>Approval cycle (cumbersomeness)-reliability required</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td></tr><tr><td>Approval cycle (cumbersomeness)-quality required</td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Processing capacity-processing time</td><td></td><td>X</td><td></td><td>X</td><td>X</td><td>X</td><td></td></tr><tr><td>Processing capacity-frequency of runs</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Processing capacity-memory congestion</td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td></tr><tr><td>Processing capacity-computer capacity</td><td></td><td>X</td><td></td><td>X</td><td>X</td><td></td><td></td></tr></table>

Fig. 2. Underlying variables suggested in literature.  
(Note: The total number of items in the Figure may differ slightly from what is reported in the literature review because some parameters had to be grouped or split in the process of building one common list of variables.)

Generally, the authors have suggested variables of both manipulable and non-manipulable nature for the purpose of estimating development efforts. Nelson [1966], Aron [1976], Walston and Felix [1977], Putnam [1980], Boehm [1981], and Wolverton [1984] have suggested the use of variables pertaining to six or more factors. Following Farr and Zagorski's [1965] pioneer work at System Development Corporation, Nelson [1966], also from SDC, published a formula to predict the development time of a software development project. Based on 169 projects and an initial estimate of 104 attributes, he identified 14 variables helpful to predict the number of person-months. Ten years later, Aron [1976] drawing on the Nelson's study and his own personal experience, mentioned 12 variables that should be considered in making an estimate. In 1977, Walston and Felix [1977], used correlation analysis on 60 projects to select 29 variables having an impact on productivity. Putnam [1980] proposed that 12 variables should be considered in an estimate. One of the most important contributor to software cost engineering is Boehm [1981] who isolated 16 variables judged pertinent in estimating software development efforts on the basis of 63 projects. Wolverton [1984], who had suggested a software cost estimation model in 1974, mentioned 26 variables in 1984 that should be taken into account in making an estimate.

Albrecht and Gaffney [1983] are the only authors who developed an estimation methodology mostly based on non-manipulable variables. Their method, entitled Function Points, was based on the weighting of five variables (number of inputs, number of outputs, number of internal files, number of interface files, and number of inquiries) and an overall measure of complexity. This hybrid method, i.e., combining both quantitative and qualitative cost drivers [Desharnais, 1989], is rapidly gaining popularity and is reported as being useful even in the early phases of the development cycle [Richards, 1989; Dreger, 1989].

## Accuracy of estimation methods

Among the estimation methods, the algorithmic technique (or estimation model), is by far the most widely documented. This method uses empirically derived formulae to predict data that are a required part of the software project planning step such as effort (in person-months), project duration (in chronological months), or other pertinent project data [Pressman, 1987]. The results obtained from these algorithms are however somewhat deceptive.

While Nelson [1966] admitted that his model led to inaccurate estimates, Aron [1976] indicated that his method was not as good as an estimate based on sound experience. Boehm [1981], who was more optimistic, reported the accuracy of software development effort estimates calculated with the COCOMO Intermediate scale to be within 20% of projects 68% of the time. These results do not, however, match those obtained by Kemerer [1987] who tested the SLIM (Putnam), COCOMO (Boehm) and Function Points (Albrecht and Gaffney) models. He observed average percentage error in person-month estimates of 772 percent for the SLIM model, 610 percent for COCOMO and 103 percent for Function Points. Once calibrated for the organization where he made his tests, the SLIM model explained 88% of the variation in the number of person-months, COCOMO 60%, and Function Points, 55%. Kemerer gave some valuable insight into the accuracy of algorithmic techniques and his work supports the conclusion that algorithmic techniques are not accurate. Unfortunately, little is known about the accuracy of the other estimation methods. Furthermore, there is no information available on the relationship between the underlying variables used in any of these methods and the accuracy of the estimates. A better knowledge of these relationships would help design appropriate approaches to the estimation of information systems development efforts. It is to fill this gap that the actual research was undertaken.

## Theoretical stance

The accuracy of an estimate of an information system development effort is dependent on both estimation method, underlying variables used, and project management. While ineffective methods or unrelated variables will inevitably lead to inaccurate estimates, the appropriate choice of estimation methods and underlying variables is not the unique condition to make an accurate estimate.

Indeed, an estimate can be realized only if there is proper project management. The quality of the project management has a definite impact on the accuracy of the estimate. Whatever the intrinsic quality of an estimate, if the project is mismanaged, the estimate will turn out to be an inaccurate one.

This research focused on the estimation methods and the underlying variables associated with accurate estimates. It did not include the project management dimension in spite of its importance in explaining the accuracy of the estimates. The quality of project management practices was therefore assumed to be constant among projects. Unexplained variations in the accuracy of the estimates might therefore be due to varying project management practices.

The purpose of this research was to learn which estimation methods and underlying variables used to make estimates are indeed related to more accurate estimates. No specific estimation model (e.g. COCOMO, SLIM, Function Points) was tested since these are really just algorithms for incorporating various variables. More precisely, this study sought to answer two basic questions:

1. Which estimation methods are related to more accurate estimates?

Each estimation method has strengths and weaknesses [Boehm, 1981]. A better understanding of the importance of each method in the accuracy of the estimates should ease the work of the estimator in choosing the method to be used. Since methods are not exclusive from one another, the estimator could possibly combine the most successful ones in his/her estimation work. More has to be known on estimation methods to end up with economical solutions to evaluate development efforts.

2. Which underlying variables are related to more accurate estimates?

As far as variables are concerned, it has been suggested [Aron, 1976; Wolverton, 1984] and even established [Boehm, 1981; Walston and Felix, 1977] that certain variables have an influence on information systems development costs. Some or many of these variables differ, however, from one study to another and there is no way to find out which variable should or should not be used. The importance of some variables are emphasized by their inclusion in algorithmic models while some other variables are only suggested for consideration in any state of the art estimation. Evidently, authors usually argue that their own set of variables is the good one. It is worth testing the relative importance of these variables in one single study in order to compare the usefulness of these variables in making accurate estimates. The groupings of these underlying variables into factors will also be studied.

In this research, the accuracy of the estimate is related to the importance attributed to an underlying variable or an estimation method at the time of the estimate. The importance of a method or a variable in an estimate corresponds to the absolute weight attributed to each method or variable. The existence of a relationship between importance and accuracy is based on the logic that if a variable was important in the assessment of software costs, the accuracy of the estimate should be higher. The importance variable is not given a direction indicating if it tends to increase or decrease the estimated cost since the direction is dependent upon many variables, such as the estimation method used, that could not be controlled within the context of this study. Once it is established that a higher importance attributed to a variable is related to higher accuracy, the next step, not accomplished in this research, is to study the nature of the relationship.

## Methodology

This research was accomplished through a cross sectional study of a survey type conducted with software development managers. A questionnaire was used to retrospectively measure original estimates, actual efforts, the use of nine different estimation methods and the presence of thirty-five underlying variables on a recall of the managers' behavior at the time the estimates were made. This part is divided in two sections. The measures are presented in the first section, while the second section deals with survey characteristics.

## Measures

## Dependent variable

The accuracy of estimates was measured by the difference, in absolute value, between the global effort estimated and the global effort actually required (in person-days), as recommended by Conte et al., [1986]. It is the percentage difference calculated using the following formula:

$$
\text { Accuracy } = \left| \left[ (\text { actual   effort } - \text { estimated   effort }) \right. \right.
$$

/estimated effort]

The estimated effort is placed in the denominator since it is a logical point of reference for studies dealing with software cost estimation. For project managers, a profit or a loss is usually calculated on the basis of the expected cost.

## Independent variables

The two independent variables in the model predicting the accuracy of the estimate are the estimation methods and the underlying variables.

The nine estimation methods tested were those most frequently cited in the literature (Figure 1): personal experience, expert judgment, analogy, algorithmic, top-down, bottom-up, restriction, price to win, and standards. The thirty-five underlying variables tested were drawn from the initial list of forty variables presented in Figure 2. Of the initial list, the following were grouped. Number of instructions was grouped with system complexity since most of the authors presented it as a measure of system complexity and the number of instructions, per se, is an output measure rather than an input measure. Reliability and quality required were grouped under approval cycle since the pretest revealed that respondents did not differentiate the two concepts. Processing time, memory congestion, frequency of runs and computer capacity were grouped under processing capacity since pretest respondents indicated that these concepts were very much related together and were better represented by processing complexity. The final list of variables is presented in

Table 4 in the Empirical Findings section, along with some descriptive statistics that will be explained later in this paper.

The questionnaire used in this survey allowed for gathering information on the first estimate of the total development costs. Respondents were asked to provide different data with respect to the stage at which the first global estimate was made: firstly, the number of person-days estimated as opposed to the number actually required for the whole project; secondly, the level of importance of the different methods they used (if many methods were used) for the estimation of the project at the time of the first detailed estimate and thirdly, the level of importance of the different variables considered in this estimate also at the time of the first estimate. Concerning variables, for instance, the question was the following: “Variables used in the Estimate of the project: Please identify the variables used in the first detailed estimate of the project and indicate the level of importance associated to each variable in your estimate”.

The scale measuring the importance of each method and variable used in making the estimate was an ordinal four-points scale anchored at each point as follows: 1 – not used, 2 – low importance, 3 – medium importance, and 4 – high importance. The importance metric has been used in various researches on user attitudes and behavior [Ajzen et Fishbein, 1980, Assael, 1987; Seashore et al., 1983; Swieringa and Moncur, 1975] and was recently suggested as a predictor of accuracy in forecasting models [Beach et al., 1986]. It is based on these references that the importance concept has been selected to weight each factor. It was assumed that a method or a variable rated as more important was given more attention by the estimator than one rated as less important. While a variable classified as unimportant by an estimator is not likely to influence the accuracy of a prediction, it seems that a variable rated as important by an estimator would normally influence his/her calculation of the expected costs. It might lead either to an accurate or to an inaccurate estimate but it should have an effect. This research aims at finding which variables and methods are associated with accurate estimates, which ones are associated with inaccurate estimates and which ones show no clear relationship.

In whatever phase the estimate was made, it always concerned the total number of person-days for all the remaining phases of the project, not only the phase at which the estimate was made. The ratings were therefore made on a recall of what they felt was important when they made the estimate, not on what turned out to be the important methods and variables once the project was completed. The use of a recall judgment (or retrospective pretest) can be considered as a valid measure when complementary data is available [Campbell and Stanley, 1966; Isaac and Michael 1980]. A retrospective pretest consists in asking subjects to reflect their attitudes or behavior prior to some given event on which they are being compared.

As suggested by Mumford [1985], the researchers met with eleven managers, once the research was completed. The purpose of these meetings was to complete and validate their interpretation of results. To ease the discussion, each manager was provided with a copy of his own completed questionnaire. In addition to obtaining many valuable remarks and insight from them, it was observed that respondents kept detailed files of estimated and actual costs of each project, increasing our confidence that the figures reported on the questionnaires could be considered valid. Furthermore, although we made no detail review of the respondents' ratings of the methods and variables, respondents generally agreed, by looking back at the questionnaire, that the ratings they had made would be the same, or mostly the same, if they had to complete the questionnaire again. This is not a scientific test but it gives some insight into the validity of the recall judgment and the test-retest validity of the questionnaire.

This research dealt with estimates made during the first three phases of the development cycle since estimates are generally made during these phases. Based on the writings of Boehm [1981, 1984], Wolverton [1974], McKeen [1983], Gane and Sarson [1980] and Davis and Olson [1985], the information systems development effort may be divided into five stages, each having a number of activities to accomplish and goods to deliver. These phases are as follows. Phase 1 – the feasibility study (initiation): to decide whether it is advisable to undertake development of the project. Phase 2 – the preliminary analysis (administrative design): to define the system in terms of objectives, requirements, and operating principles. Phase 3 – the functional analysis: to describe the functional model of operations and data. Phase 4 – technical development: concerns the preparation of organic specifications and programming. Phase 5 – the testing phase.

Table 1 Respondents' characteristics.

<table><tr><td>Position</td><td colspan="2">Respondents (N = 89)</td></tr><tr><td></td><td>N</td><td>%</td></tr><tr><td>Vice-president Information Systems</td><td>1</td><td>1</td></tr><tr><td>Director Information Systems</td><td>9</td><td>10</td></tr><tr><td>Chief Information Systems Development</td><td>22</td><td>25</td></tr><tr><td>Project Manager</td><td>17</td><td>19</td></tr><tr><td>Systems Analyst</td><td>24</td><td>27</td></tr><tr><td>Consultant</td><td>16</td><td>18</td></tr><tr><td>Industry</td><td colspan="2">Organization (N = 63)</td></tr><tr><td></td><td>N</td><td>%</td></tr><tr><td>Government</td><td>21</td><td>33</td></tr><tr><td>Public Services</td><td>3</td><td>5</td></tr><tr><td>Manufacturing</td><td>11</td><td>17</td></tr><tr><td>Banking</td><td>6</td><td>10</td></tr><tr><td>Insurance</td><td>7</td><td>11</td></tr><tr><td>Education</td><td>3</td><td>5</td></tr><tr><td>Retail</td><td>1</td><td>2</td></tr><tr><td>Engineering</td><td>2</td><td>3</td></tr><tr><td>Consulting</td><td>9</td><td>14</td></tr></table>

## Survey Characteristics

## Sample

The survey results reported here concerned a population composed of a wide range of private and public sector organizations having places of business in the eastern part of Canada (Table 1). The respondents held a variety of positions in the information systems area. Their experience in cost estimation varied from 1 year to 19 years with an average of 6 years and a median of 5 years.

## Data analysis

Separate tests were made based upon the phase at which the first detailed estimate of the project was made. The relationship between the level of use of each method and the accuracy of the estimate was tested using Spearman correlation coefficients, suitable for ordinal scales.

The relationship between the level of use of variables and the accuracy of the estimate required a more extensive handling of statistical analysis. First, a factor analysis was conducted on all underlying variables of the total sample in order to group the variables that correlated together. This factor analysis allowed to group the variables measuring the same aspect of the system while allowing the identification of factors measuring different aspects. The orthogonal (varimax) solution explained 56% of the variance of the construct and produced an eight factor solution. The resulting classification of the underlying variables is first presented in Table 4 and is used in various tables throughout this report. For each estimation development phase, unique values were then computed for each factor. Only those variables showing significant correlations with accuracy were included in the computation of each factor value. The value attributed to each factor was then correlated with accuracy using Spearman correlation coefficients.

Finally, a stepwise multiple regression was run to determine the proportion of variance explained by factors at each development phase. Only those factors showing a significant correlation with accuracy were included in the regression. The scales were assumed to be nearly ratio scales.

## Questionnaire administration procedure

With the help of various government publications, professional associations and personal contacts, 152 organizations were identified. Preliminary phone calls were made to the systems directors in order to explain the project, solicit their participation and determine the number of estimators who could participate in the study. Based on this discussion, copies of the questionnaire (1 to 4, as agreed upon with the systems director) were sent to him/her, with return envelopes and a cover letter explaining the purpose of the research. As explained in the cover letter, the questionnaire was to be completed by a person whose function consisted of estimating the efforts required for the development of information systems. The respondents, chosen by the systems director, were to answer the questionnaire with regard to the last completed project that had required more than 150 person-days of development efforts. Each respondent completed only one questionnaire. The respondents returned the questionnaire directly to the researchers. A first follow-up (by mail) was undertaken one week after the questionnaire was mailed and a second follow-up (by telephone) was conducted two weeks after on the organizations that had not yet responded. The lower limit of 150 person-days was set in accordance with Boehm's [1981] remark that programmer's personal differences tend to dominate any other effects on very small projects. Furthermore, all the variables identified in the literature concerned projects above a minimal size. The last completed project was selected in order to eliminate the respondent's possible preference for projects with accurate estimates and to increase the chances that he/she still had a good memory of the estimation methods and variables used at the time of the estimate. The questionnaire was pre-tested by eleven respondents.

## Response rate

In all, 374 copies of the questionnaire were distributed. Of the 152 organizations solicited, 67 organizations returned 110 questionnaires, out of which 89 could be used in the study. The response rate was 23.8%. Twenty-one questionnaires were eliminated for the following reasons: no information as to when the estimate was made (17), no data on actual costs (2), and no data on both estimated and actual costs (2).

## Empirical findings

## Descriptive results

The project characteristics are presented in Table 2. The estimated effort varied from 120 to 5800 person-days with a mean of 948 person-days and a median of 500 person-days. The actual effort of development projects varied from 150 to 6900 person-days with a mean of 1251 person-days and a median of 657 person-days. The estimate variances varied from 20% (overestimate) to 100% (underestimate), with a mean of 33% (underestimate). Approximately one third (33/89) of the estimates were made at the beginning of the feasibility study, one third (28/89) at the beginning of the preliminary study and one third (28/89) at the beginning of the functional study.

Each of these estimates included the actual and all the remaining phases.

The level of importance of estimation methods as well as the number of methods used for each estimate are presented in Table 3. The experience, analogy and bottom-up methods were rated by the respondents as the most important to estimate project development effort whereas the price to win, algorithmic, top-down, standards, restrictions and experts methods were rated as the less important. Results further indicate an average of 3.6 methods used for each estimate.

The level of importance of variables is presented in Table 4. The variables rated as more important (median rates larger than 3) by the respondents were: number of functions or reports, complexity of system or product, qualifications of personnel, number of reports or displays and type of processing (on line, batch). On the other hand, 18 variables out of the initial list of 35 variables were rated as less important (median rates smaller than 2). On average, the respondents used 19 variables to make their estimate.

Table 2  
Characteristics of the estimates.  
PROJECT CHARACTERISTICS (N = 89)

<table><tr><td></td><td>Estimated effort</td><td>Actual effort</td></tr><tr><td>Number of person-days (range)</td><td>120–5800</td><td>150–6900</td></tr><tr><td>Mean</td><td>948</td><td>1251</td></tr><tr><td>Median</td><td>500</td><td>657</td></tr></table>

DISTRIBUTION OF ESTIMATE VARIANCES
Stage at which global estimate conducted

<table><tr><td>Estimate variancea%</td><td>Feasibility study (n = 33) (n)</td><td>Preliminary study (n = 28) (n)</td><td>Functional study (n = 28) (n)</td></tr><tr><td>-1 to -20b</td><td>2</td><td>2</td><td>4</td></tr><tr><td>0 to 19c</td><td>7</td><td>13</td><td>9</td></tr><tr><td>20 to 39</td><td>10</td><td>5</td><td>7</td></tr><tr><td>40 to 59</td><td>6</td><td>3</td><td>3</td></tr><tr><td>60 to 79</td><td>6</td><td>2</td><td>4</td></tr><tr><td>80 to 99</td><td>1</td><td>0</td><td>1</td></tr><tr><td>100 and more</td><td>1</td><td>3</td><td>0</td></tr><tr><td>Mean (%)</td><td>0.36</td><td>0.32</td><td>0.26</td></tr><tr><td>Std. Dev.</td><td>0.31</td><td>0.35</td><td>0.26</td></tr></table>

$^{a}$ The estimate variance is calculated with this formula: [(actual - estimate)/estimate].  
$^{h}$ Overestimate.  
$^{c}$ Underestimate.

Table 3  
Importance of use of estimation methods (N = 89). $^{a}$

<table><tr><td>Methods</td><td>Mean</td><td>Median</td><td>Std.dev.</td></tr><tr><td>Experience</td><td>3.3</td><td>3.6</td><td>0.9</td></tr><tr><td>Expert</td><td>1.8</td><td>1.3</td><td>1.1</td></tr><tr><td>Analogy</td><td>2.5</td><td>2.7</td><td>1.1</td></tr><tr><td>Algorithmic</td><td>1.3</td><td>1.1</td><td>0.8</td></tr><tr><td>Top-down</td><td>1.4</td><td>1.1</td><td>0.9</td></tr><tr><td>Bottom-up</td><td>2.4</td><td>2.7</td><td>1.3</td></tr><tr><td>Restriction</td><td>1.6</td><td>1.2</td><td>1.0</td></tr><tr><td>Price to win</td><td>1.2</td><td>1.0</td><td>0.5</td></tr><tr><td>Standards</td><td>1.5</td><td>1.2</td><td>1.0</td></tr><tr><td colspan="2">Number of methods used</td><td colspan="2">Respondents (N = 89)</td></tr><tr><td colspan="2">1</td><td colspan="2">3%</td></tr><tr><td colspan="2">2</td><td colspan="2">18%</td></tr><tr><td colspan="2">3</td><td colspan="2">30%</td></tr><tr><td colspan="2">4</td><td colspan="2">27%</td></tr><tr><td colspan="2">5</td><td colspan="2">11%</td></tr><tr><td colspan="2">6</td><td colspan="2">9%</td></tr><tr><td colspan="2">9</td><td colspan="2">1%</td></tr></table>

$^{a}$ Min = 1, max = 4.

## Findings about methods

Table 5 shows significant correlations between the use of methods and the absolute percentage error. To ease the presentation of results, the term accuracy of the estimate will be used instead of absolute percentage error; a higher accuracy corresponds to a smaller percentage error. No method was related to the accuracy of the estimate when the estimate was made at the feasibility stage. However, four methods were related to the accuracy of the estimate when the estimate was made at the preliminary stage. The use of the analogy and restriction methods produced more accurate estimates whereas the use of the price to win and standards methods were associated with less accurate estimates. At the functional stage, the experts and restrictions methods were related to more accurate estimates whereas the algorithmic methods was associated with less accurate estimates. The significant relationships observed between the price to win method, the algorithmic method and the accuracy of the estimates must however be accepted with caution, due to the low number of respondents in the sample who used these two methods.

## Findings about variables

Overall, 19 out of the initial list of 35 variables were related to the accuracy of the estimate (table 6). The Spearman correlations between the factors and the accuracy of the estimate is presented in table 7. Depending on the stage at which the estimation was made, different factors were related to the accuracy of the estimates. At the feasibility stage, two factors were associated with more accurate estimates: users and project management whereas one factor, size, was associated with less accurate estimates.

Table 4  
Importance of use of underlying variables (N = 89). $^{a}$

<table><tr><td>Variables used</td><td>Mean</td><td>Median</td><td>Std.dev</td></tr><tr><td colspan="4">Users</td></tr><tr><td>Content of documentation to be compiled</td><td>2.3</td><td>2.4</td><td>1.1</td></tr><tr><td>User familiarity with information systems</td><td>2.2</td><td>2.0</td><td>1.2</td></tr><tr><td>Number of users or groups of users</td><td>1.9</td><td>1.4</td><td>1.2</td></tr><tr><td>Geographical dispersion of users</td><td>1.6</td><td>1.2</td><td>1.0</td></tr><tr><td>Availability of users</td><td>2.2</td><td>1.6</td><td>1.3</td></tr><tr><td>Quality of user needs identification</td><td>2.5</td><td>2.7</td><td>1.3</td></tr><tr><td colspan="4">Data base</td></tr><tr><td>Level of security to be incorporated</td><td>1.8</td><td>1.4</td><td>1.0</td></tr><tr><td>Number of databases or files</td><td>2.5</td><td>2.6</td><td>1.2</td></tr><tr><td>Number of information elements handled</td><td>2.2</td><td>1.9</td><td>1.2</td></tr><tr><td>Number of routines</td><td>1.5</td><td>1.2</td><td>1.0</td></tr><tr><td>Number of reusable program applications</td><td>2.0</td><td>1.3</td><td>1.3</td></tr><tr><td colspan="4">Personnel</td></tr><tr><td>Qualifications of personnel</td><td>2.9</td><td>3.4</td><td>1.2</td></tr><tr><td>Exp. pers w.type of processing (on line, batch)</td><td>2.4</td><td>2.7</td><td>1.2</td></tr><tr><td>Exp. pers w. system complexity</td><td>2.4</td><td>2.7</td><td>1.3</td></tr><tr><td>Personnel turnover</td><td>1.9</td><td>1.4</td><td>1.2</td></tr><tr><td>Stability of technological environment</td><td>1.7</td><td>1.3</td><td>1.0</td></tr><tr><td colspan="4">Size</td></tr><tr><td>Type of processing (on line, batch)</td><td>2.9</td><td>3.1</td><td>1.1</td></tr><tr><td>Number of functions (additions or modifications)</td><td>3.5</td><td>3.8</td><td>1.0</td></tr><tr><td>Number of reports or displays</td><td>2.9</td><td>3.2</td><td>1.2</td></tr><tr><td>Number of queries to develop</td><td>2.5</td><td>2.8</td><td>1.3</td></tr><tr><td>Number of interfaces with other systems</td><td>2.5</td><td>2.6</td><td>1.3</td></tr><tr><td colspan="4">Language</td></tr><tr><td>Technological risk (use of new tool or technique)</td><td>2.3</td><td>2.1</td><td>1.3</td></tr><tr><td>Use of productivity tool</td><td>1.6</td><td>1.2</td><td>1.0</td></tr><tr><td>Programming language</td><td>2.3</td><td>2.2</td><td>1.3</td></tr><tr><td>Exp. pers w. programming language</td><td>2.1</td><td>1.5</td><td>1.2</td></tr><tr><td>Exp. pers w. computer</td><td>1.6</td><td>1.2</td><td>1.0</td></tr><tr><td colspan="4">Time constraints</td></tr><tr><td>Number of persons involved in development</td><td>2.6</td><td>2.9</td><td>1.2</td></tr><tr><td>Time allotted (overtime requirements)</td><td>2.1</td><td>1.5</td><td>1.3</td></tr><tr><td>Computer time available</td><td>1.8</td><td>1.4</td><td>1.1</td></tr><tr><td colspan="4">Project management environment</td></tr><tr><td>Project management structure</td><td>1.7</td><td>1.3</td><td>1.1</td></tr><tr><td>Development methodology used</td><td>2.2</td><td>2.1</td><td>1.2</td></tr><tr><td>Development policy (within the organization)</td><td>1.7</td><td>1.3</td><td>1.1</td></tr><tr><td colspan="4">Complexity</td></tr><tr><td>Complexity of the system/product</td><td>3.4</td><td>3.7</td><td>0.9</td></tr><tr><td>Approval cycle (cumbersomeness)</td><td>1.7</td><td>1.3</td><td>1.1</td></tr><tr><td>Processing capacity</td><td>1.8</td><td>1.3</td><td>1.1</td></tr><tr><td>Number of variables used</td><td colspan="3">Respondents (N = 89)</td></tr><tr><td>3 to 8</td><td colspan="3">10%</td></tr><tr><td>9 to 14</td><td colspan="3">23%</td></tr><tr><td>15 to 20</td><td colspan="3">29%</td></tr><tr><td>21 to 26</td><td colspan="3">19%</td></tr><tr><td>27 to 35</td><td colspan="3">19%</td></tr></table>

$^{a}$ Min = 1, max = 4.

Table 5  
Correlations between estimation methods and absolute percentage error (N = 89). $^{a}$

<table><tr><td rowspan="2">Methods employed</td><td colspan="3">Stage at which global estimate conducted</td></tr><tr><td>Feasibility study (n = 33)</td><td>Preliminary study (n = 28)</td><td>Functional study (n = 28)</td></tr><tr><td>Expert</td><td></td><td></td><td>-0.46 (0.01)</td></tr><tr><td>Analogy</td><td></td><td>-0.37 (0.03)</td><td></td></tr><tr><td>Algorithmic</td><td></td><td></td><td>0.27 (0.08)</td></tr><tr><td>Restriction</td><td></td><td>-0.25 (0.10)</td><td>-0.39 (0.02)</td></tr><tr><td>Price to Win</td><td></td><td>0.29 (0.07)</td><td></td></tr><tr><td>Standards</td><td></td><td>0.29 (0.07)</td><td></td></tr></table>

$^{a}$ The first number indicates Spearman's correlation coefficient and the second, in brackets, the significance levels of the correlation. The methods not mentioned in the table (experience, top-down, and bottom-up) did not show significant correlation. Negative signs indicate methods associated with better estimates. A negative correlation means that a higher importance attributed to a method is associated with a smaller absolute percentage error or an higher accuracy.

Table 6  
Correlations between underlying variables and absolute percentage error (N = 89). $^{a}$

<table><tr><td rowspan="2">Variables</td><td colspan="3">Stage at which global estimate conducted</td></tr><tr><td>Feasibility study (n = 33)</td><td>Preliminary study (n = 28)</td><td>Functional study (n = 28)</td></tr><tr><td>Users</td><td></td><td></td><td></td></tr><tr><td>Content of documentation to be compiled</td><td>-0.23 (0.10)</td><td>-0.30 (0.06)</td><td>-0.42 (0.01)</td></tr><tr><td>User familiarity with information systems</td><td></td><td>-0.32 (0.05)</td><td></td></tr><tr><td>Geographical dispersion of users</td><td></td><td>-0.25 (0.10)</td><td>-0.31 (0.05)</td></tr><tr><td>Availability of users</td><td>-0.37 (0.02)</td><td></td><td></td></tr><tr><td>Quality of user needs identification</td><td></td><td>-0.31 (0.06)</td><td></td></tr><tr><td>Data Base</td><td></td><td></td><td></td></tr><tr><td>Level of security to be incorporated</td><td></td><td></td><td>0.32 (0.05)</td></tr><tr><td>Number of databases or files</td><td></td><td>0.30 (0.06)</td><td></td></tr><tr><td>Personnel</td><td></td><td></td><td></td></tr><tr><td>Experience with system complexity</td><td></td><td>-0.35 (0.04)</td><td></td></tr><tr><td>Personnel turnover</td><td></td><td>-0.31 (0.06)</td><td></td></tr><tr><td>Stability of technological environment</td><td></td><td>-0.29 (0.07)</td><td>-0.40 (0.02)</td></tr><tr><td>Size</td><td></td><td></td><td></td></tr><tr><td>Type of processing</td><td></td><td></td><td>-0.27 (0.09)</td></tr><tr><td>Number of functions</td><td>0.37 (0.02)</td><td></td><td>-0.38 (0.02)</td></tr><tr><td>Number of reports or displays</td><td></td><td>0.36 (0.03)</td><td></td></tr><tr><td>Number of queries to develop</td><td></td><td>0.35 (0.03)</td><td></td></tr><tr><td>Language</td><td></td><td></td><td></td></tr><tr><td>Use of productivity tools</td><td></td><td></td><td>-0.42 (0.01)</td></tr><tr><td>Programming language</td><td></td><td>0.37 (0.03)</td><td></td></tr><tr><td>Time constraints</td><td></td><td></td><td></td></tr><tr><td>Number of persons involved</td><td></td><td></td><td>-0.29 (0.07)</td></tr><tr><td>Project Management Environment</td><td></td><td></td><td></td></tr><tr><td>Project management structure</td><td>-0.24 (0.09)</td><td></td><td></td></tr><tr><td>Complexity</td><td></td><td></td><td></td></tr><tr><td>Complexity of the system or product</td><td></td><td>-0.29 (0.07)</td><td></td></tr></table>

$^{a}$ The first number indicates Spearman's correlation coefficient and the second, in brackets, the significance levels of the correlation. The variables not mentioned did not show significant correlation. Negative signs indicate variables associated with better estimates. A negative correlation means that a higher importance attributed to a variable is associated with a smaller absolute percentage error or an higher accuracy.

Table 7  
Correlations between factors and absolute percentage error.

<table><tr><td>Factors</td><td>Feasibility study (n = 33)</td><td>Preliminary study (n = 28)</td><td>Functional study (n = 28)</td></tr><tr><td>Users</td><td>-0.38 (0.01)</td><td>-0.44 (0.01)</td><td>-0.44 (0.01)</td></tr><tr><td>Database</td><td></td><td>0.30 (0.06)</td><td>0.32 (0.05)</td></tr><tr><td>Personnel</td><td></td><td>-0.47 (0.01)</td><td>-0.40 (0.02)</td></tr><tr><td>Size</td><td>0.37 (0.02)</td><td>0.36 (0.03)</td><td>-0.41 (0.02)</td></tr><tr><td>Language</td><td></td><td>0.37 (0.03)</td><td>-0.42 (0.01)</td></tr><tr><td>Time constraints</td><td></td><td></td><td>-0.29 (0.07)</td></tr><tr><td>Project management</td><td>-0.24 (0.09)</td><td></td><td></td></tr><tr><td>Complexity</td><td></td><td>-0.29 (0.07)</td><td></td></tr></table>

$^{a}$ The first number indicates Spearman's correlation coefficient and the second, in brackets, the significance levels of the correlation. The categories not mentioned did not show significant correlation. Negative signs indicate factors associated with better estimates. A negative correlation means that a higher importance attributed to a category is associated with a smaller absolute percentage error or an higher accuracy.

At the preliminary stage, six out of the initial list of eight factors showed a significant relationship with the accuracy of the estimate. Three factors, users, personnel, and complexity were related to more accurate estimates. The estimators who gave much importance to these factors in making their estimates made more accurate estimates than those who did not. On the other hand, three other factors, data base, size and language, were associated to less accurate estimates.

Finally, six factors were found to be related to accuracy when the estimate was made at the functional phase. Five factors (users, personnel, size, language and time constraints) were related to more accurate estimates. Whereas only one factor (data base) was related to less accurate estimates. Again, some of these results, such as those pertaining to the project management factor at the feasibility study, and to the personnel, language and data base factors at the functional stage, need to be accepted with caution given the low number of respondents who used these underlying variables in making their estimates.

The cumulative effect of factors on the accuracy of the estimate differed among phases (Table 8). After deletion of outliers, the following results were obtained from the multiple regressions. At the feasibility phase, the proportion of the variance explained by the factors represented only

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Table 8
Regression equations predicting estimate accuracy. $^{a}$ 

Stage at which first global estimate is conducted:

Feasibility study
Accuracy = 0.05 + 0.11 (size)
t    2.67
sig    0.03
R$^{2}$   0.15
R$^{2}$ adj.    0.12
F = 5.34; sig = 0.03; n = 32

Preliminary Study
Accuracy = 0.18 - 0.12 (users) + 0.11 (size)
t    4.51    7.44
sig    0.01    0.001
R$^{2}$   0.56
R$^{2}$ adj.    0.52
F = 13.22; sig = 0.000; n = 24

Functional study
Accuracy
= 52 + 0.08 (data base) - 0.13 (size) - 0.04 (time constraints)
t    4.58    9.34    1.80
sig    0.01    0.000    0.07
R$^{2}$   0.60
R$^{2}$ adj.    0.54
F = 10.91; sig. = 0.000; n = 26
</div>

$^{a}$ After deletion of outliers.

15% of the variations in the accuracy of the estimate. Only the size factor entered the equation. Better results were obtained at the preliminary phase where 56% of the variations in the estimate could be explained by two factors (users and size). Finally, 60% of the variations in the estimate were explained by three factors (data base, size and time constraints) at the functional phase.

## Discussion

The key findings of this study are: 1 – the qualitative methods are related to accurate estimates, 2 – the relationship between some factors and the accuracy of the estimate varies among phases and generally tends to improve based upon the phase at which the estimate is made, and 3 – the proportion of variance in the accuracy of the estimates explained by the factors increases with the phase at which the estimate is made.

## Qualitative versus quantitative methods

Overall, the use of only three methods was associated with accurate estimates: experts, analogy, and restriction. The algorithmic, price to win and standards methods seemed to be related to less accurate estimates but the low number of estimators who used the algorithmic and price to win methods do not allow to generalize these results. The accurate methods, i.e. experts, analogy, and restriction, could be classified as qualitative as opposed to algorithmic, price to win and standards methods which could be classified as quantitative methods. Indeed, a common trait between the expert and analogy methods is the experience of the estimator(s) with similar development projects. To some extent, the restriction method belong to the same group in that the total amount of money or person-days available is known in advance and the estimator has to define by himself/herself the characteristics of the system to be developed. The different elements on which experience based estimates are made are mostly qualitative.

On the other hand, the algorithmic, price to win and standards methods which tend to be associated with less accurate estimates are based on a quantitative evaluation of the total development effort. Projects are appraised on the basis of a representation of the systems characteristics which are weighted and added up to a final estimate. The standards method is not based on a procedure as detailed as the algorithmic method but it refers to the same principle. As far as the price to win method is concerned, this is neither a qualitative nor a true quantitative method. This method is often used for the sole purpose of getting the authorization to begin a development project. Estimators may be aware that underestimates have no immediate consequence and that additional budget will be made available later or, in the case of external consultants, they might want to develop the system in order to get expertise on the topic and to obtain more development projects of this type in the future.

## Factors

A smaller number of factors were related to more accurate estimate at the feasibility phase as opposed to the preliminary and functional phases. This might be due to the fact that not much of a project is known at its inception. At the feasibility stage, two factors were related to the accurate estimate whereas at the preliminary stage, three factors enhance prediction of the total cost of the project. At the functional stage, most of the factors (five out of six) were associated with accurate estimates. This progression in the number of factors related to more accurate estimates in later stages is logic since the evaluator has then a more precise understanding of the work to be done.

In addition to the number of factors significantly related to more accurate estimates, it is interesting to look at the evolution in the direction of the relationships between the factors and the accuracy of the estimate. Some factors that were related with less accurate estimates at the feasibility and preliminary phases turned out to be accurate predictors at a later phase. This is the case for the size and language factors, for example. The lack of information about the system to develop is the reason why at an early stage some factors tend to mislead the evaluator in his/her work. Hence, care should be given to the factors that are related to inaccurate estimates. The best advice to the evaluators is to postpone the use of these factors until they reach a point of the development cycle where their use is related to more accurate estimate.

The proportion of the variance explained by the factors increases between the feasibility study and functional phase to start at a low 15% and to end up at a level of 60% at the functional phase. The large increase in the proportion of variance explained between the feasibility and the preliminary and the functional phases means that the factors are not as good predictors of accuracy at the feasibility phase than they are at the preliminary and functional phases. The high proportion of the variance explained by the model in later phases signifies that the information carried by the different factors is cumulative to some extent. Thus, in later phases, it is worthy to use several factors to make an estimate.

Although a sizeable part of the variations in the estimate can be explained by the factors under study, there remains a part of the variations that is not explained. The unexplained part may come from four sources: 1 – other variables not included in the study, 2 – the estimation methods used, 3 – the management of the project, and 4 – the political considerations. It is not very likely that other variables should have been considered since the initial list was drawn from a thorough literature review and included all variables suggested in earlier studies. However, it is possible that estimation methods explain an additional part of the variations in the accuracy since several estimation methods showed a significant relationships with accuracy. As far as project management is concerned, no data were gathered on this aspect but it was assumed in the research model that it could have an impact on accuracy. Political considerations associated with the project approval procedures in place might also have influenced the outcome of the estimate.

## Limitations

Before we conclude with these findings, it is important to indicate that this study carries some limitations. The first one concerns the internal validity of the data reported by the respondents. The questionnaires gathered data on completed projects, some of which were begun many months earlier. Despite some evidence on the validity of data, the respondents might not remember exactly which methods and variables they used at the time of the estimate nor the level of importance attributed to each.

The second limitation deals with the subjective character of data produced by self-report questionnaires. Objective data would be preferable but they could hardly be gathered in this study except for the algorithmic techniques. To the extent that the importance attributed to each variable can be interpreted as an attitude toward variable relevancy, Nunnally's [1978, p. 591] assessment of self-report questionnaire is useful. Nunnally indicated that most measures of attitudes are based on self-report, and from what evidence there is concerning the validity of different approaches to the measurement of attitude, self-report offers the most valid approach currently available.

As a third limitation, a larger sample size would produce more stable results. Some methods and variables showed a very low level of use in the sample, hence corresponding results might not be representative of a larger population of respondents. Although the relatively large number of respondents (89) and companies (63) that participated in the study makes of it the largest empirical study on software cost estimation that appeared in the literature, a still larger sample size would be needed.

## Conclusion

The results indicate that different levels of accuracy in development effort estimation depend on the choice of the methods and underlying variables used to make the estimate. While qualitative methods were observed to be related to accurate estimates, no clear conclusion could be drawn concerning the quantitative methods. As far as factors are concerned, the later the estimate, the more of factors are related to more accurate estimates. Different factors could also be used depending upon the development phase at which the first global estimate of the development effort is made. Given these results, estimators are encouraged to use specific methods and factors at specific phases. Further research should aim at determining the organizational, managerial and financial structures that could allow project managers to develop the systems within budget limits. For the Nineties specifically, the problem space would also gain in including additional dimensions such as the advent of end-user computing, the concept of information utilities, the availability of off-the-shelf technologies and CASE tools, and the different characteristics of knowledge-based systems and interorganizational applications. For these coming years, the estimation theory and the job of the estimator are becoming even more complex.

## References

Ajzen, Icek; Fishbein, M., Understanding Attitudes and Predicting Social Behavior, Prentice-Hall, New Jersey, 1980.

Albrecht, Allan J., Gaffney, John E., “Software Function, Source Lines of Code, and Development Effort Prediction: A Software Science Validation,” IEEE Transactions of Software Engineering, Vol. SE-9, No. 6, November 1983, pp. 639–648.

Allen, Brandt; “Make Information Services Pay Its Way,” Harvard Business Review, January-February 1987, pp. 57–63.

Aron, J.D.; “Estimating Resources for Large Programming Systems”, IEEE Catalogue No. EHO 165-1, Compsac 80, 1980, pp. 226–237.

Assael, Henry; Consumer Behavior and Marketing Action, 3rd Edition, Kent Publishing Company, Boston, Massachusetts, 1987, 700 p.

Augustine, N.R.; “Augustine’s Law and Major System Development Program,” Defense Systems Management Review. 1979, pp. 50–76.

Beach, Lee Roy; Barnes, Valerie E.; Christensen-Szalanski, Jay J.J., “Beyond Heuristics and Biases: A Contingency Model of Judgmental Forecasting,” Journal of Forecasting, Vol. 5, pp. 143–157, 1986.

Benbasat, Izak; Vessey, Iris; “Programmer and Analyst Time/Cost Estimation,” MIS Quarterly, Vol. 4, Number 2, June 1980, pp. 31–43.

Bergeron, François; “Factors Influencing the Use of DP Chargeback Information,” MIS Quarterly, Vol. 10, No. 3, September 1986, pp. 225–238.

Boehm, Barry; Software Engineering Economics, Prentice-Hall, Engelwood Cliffs, N.J., 1981.

Boehm, Barry; “Software Engineering Economics,” IEEE Transactions on Software Engineering, Vol. SE-10, No. 1, January 1984, pp. 4–21.

Brooks, F.P.; The Mythical Man-Month, Addison-Wesley; Reading, MA 1982.

Buss, Martin D.J.: “How to Rank Computer Projects” Harvard Business Review, Jan-Feb. 1983, pp. 118–125.

Campbell, D.T. and Stanley, J.C.: Experimental and Quasi-Experimental Designs for Research, Chicago: Rand McNally, 1966.

Conte, S.D.; Dunsmore, H.E.; Shen, V.Y.; Software Engineering Metrics and Models, The Benjamin/Cummings Publishing Company, Inc., Menlo Park, California, 1986.

De Marco, T.: Controlling Software Projects: Management,

Measurement, and Estimation. Yourdon Press, New-York, 1982.

Davis, Gordon B.; Olson, Margrethe H.; Management Information Systems: Conceptual Foundations, Structure and Development (2nd Edition), McGraw-Hill Book Company, New-York, 1985.

Desharnais, Jean-Marc, “Special Issue: PFA counting Rules with the “Entity” Concept”, The International Function Point Users Group, 1989 Spring Conference Proceedings, San Diego, California, April 3–6, 1989.

Dreger, J. Brian, Function Point Analysis, Prentice Hall, Englewood Cliffs, New Jersey, 1989.

Farr, L.; Zagorski, H.J., “Quantitative Analysis of Programming Costs Factors: A Progress Report”, ICC Symposium Proceedings on Economics of Automatic Data Processing, ed. by A.B. Friedlind, Amsterdam, North-Holland, 1965.

Gane, Chris; Sarson, Trish; Structured Systems Analysis: Tools and Techniques, Prentice-Hall Inc., Englewood Cliffs, New Jersey. 1979.

Issac, Stephen; Michael, William B.; Handbook in Research and Evaluation, EDITS Publishers, 1980.

Jones, Capers; Programming Productivity, McGraw-Hill, 1986.

Kemerer, Chris F.; “An Empirical Validation of Software Cost Estimation Models”, Communications of the ACM, Vol. 30, No. 5, May 1987, pp. 416–429.

McKeen, James D.; “Successful Development Strategies for Business Applications Systems,” MIS Quarterly, Vol. 7, No. 3, September 1983, pp. 47–65.

Mumford, Enid; “Keynote Speaker Address”, Sixth International Conference on Information Systems,” Indianapolis, Indiana, December 1985.

Nelson, E.A.: Management Handbook for the Estimation of Computer Programming Costs, AD-A648750, Systems Development Corporation, October 31, 1966.

Nunnally, Jum; Psychometric Theory, McGraw-Hill Book Company, 1978, 701 p.

Putnam, Lawrence H.; “Software Cost Estimating and Life-Cycle Control: Getting the Software Numbers,” IEEE Catalogue No EHO 165-1, Compsac 80, 1980.

Richards, Carl, “Estimating Function Points”, The International Function Point Users Group, 1989 Fall Conference Proceedings, St-Louis, Missouri, September 19–22, 1989.

Seashore, Stanley E.; Lawler, Edward E. III; Mirvis, Philip H.; Cammann, Cortlandt, Assessing Organizational Change; A Guide to Methods, Measures and Practices, John Wiley and Sons, USA, 1983, 563 p.

Swieringa, Robert J.; Moncur, Robert H., Some Effects of Participative Budgeting on Managerial Behavior, National Association of Accountants, New-York, New-York, 1975, 265 p.

Topping, Jacques; “Consultant Involvement in Information Systems Design”, Working Paper 85-01, Faculty of Management, Université Laval, Québec 1985.

Walston, C.E.; Felix, C.P.; “A Method of Programming Measurement and Estimation,” IBM Systems Journal, Vol. 16, No. 1, 1977, pp. 54–72.

Wolverton, Ray W.; “The Cost of Developing Large-Scale Software,” IEEE Transactions on Computer, Vol. C-23, No. 6, June 1974, pp. 282–303.

Wolverton, Ray W.; “Software Costing,” in Vicks, C.R. & Ramamoorthy, C.V., Handbook of Software Engineering, Van Nostrand Reinhold Company, New York, 1984, pp. 469–493.
