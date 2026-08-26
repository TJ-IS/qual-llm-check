---
otero_id: 1390
otero_key: "TTUB4ZVA"
title: "Decision support for university enrollment management: Implementation and experience"
authors: "Elliot N. Maltz; Kenneth E. Murphy; Michael L. Hand"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.03.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Decision support for university enrollment management: Implementation and experience

Elliot N. Maltz <sup>a</sup>, Kenneth E. Murphy <sup>b,⁎</sup>, Michael L. Hand <sup>c</sup>

<sup>a</sup> Professor of Marketing, Atkinson Graduate School of Management, Willamette University, 900 State Street, Salem, Oregon 97301, United States <sup>b</sup> Associate Professor of Information Systems, Atkinson Graduate School of Management, Willamette University,

900 State Street, Salem, Oregon 97301, United States

<sup>c</sup> Professor of Applied Statistics and Information Systems, Atkinson Graduate School of Management, Willamette University, 900 State Street, Salem, Oregon 97301, United States

Received 2 April 2006; received in revised form 5 March 2007; accepted 18 March 2007 Available online 30 March 2007

## Abstract

Enrollment management is a process critical to many universities that rely on tuition for a significant portion of their operating budgets. This study describes how the development and implementation of a system to support decisions in the enrollment process allowed for increased responsiveness and real-time management as well as substantially increased institutional knowledge of the process itself. This, in turn, led to dramatic improvements in both operational performance and in the attainment of strategic admission objectives.

© 2007 Elsevier B.V. All rights reserved.

Keywords: Decision support system; Enrollment management; Data mining; Organizational learnin

## 1. Introduction

Most private colleges, unless they have developed a very large endowment, base their revenue primarily on tuition income. Consider, as an example, a moderatesized undergraduate liberal arts program with a budget of \$50 million. The college would require an endowment of \$500 million to cover half of their budget under standard 5% annual growth assumptions. Since few private liberal arts colleges have an endowment of that magnitude, a systematic approach to enrollment management is critical to ensuring stability in fiscal planning. Schools approach the technical challenges associated with enrollment management in a variety of ways, often relying on offices of institutional research to perform this function or by staffing the admission office with statistical specialists [5]. However, many smaller schools lack the resources or the technical expertise to address these problems internally. In these cases, outside consultants are often hired to assist in determining which students to admit and how much financial aid to offer in order to recruit a desirable incoming class. This approach can result in suboptimal performance, additional costs and may curtail the opportunity for institutional learning with respect to managing the admissions process.

This manuscript presents the design and implementation of a successful decision support system (DSS) for enrollment management at a small liberal arts college. The DSS, an integral component of the admissions process consists of two components—a predictive model and a user-friendly interface which allows the school to dispense with the services of outside consultants while at the same time making significant operational gains. The interaction between the DSS and the admissions process can be thought of as the enrollment work system [2]. The two-year, two-phase implementation project improved the enrollment work system by enhancing understanding of the admissions process overall through the conversion of tacit process knowledge to explicit and by its impact on financial measures of performance.

A variety of data mining techniques and associated methodologies were used to assist in developing the predictive model. As will be demonstrated, the methodologies employed to develop the DSS as well as the DSS itself contributed to both the operational success of the system and the organizational learning achieved during the design and implementation phases. The enrollment management tool was implemented in an environment that was based on principles that have been recognized as important by the decision support system literature [3,11,29,32]. As such the insights provided in this paper contribute to both the enrollment management and decision support system implementation literatures.

The balance of the manuscript is organized as follows. The following section provides a brief literature review of decision support and expert systems in the admissions setting as well as relevant observations on system implementation from the DSS literature. The legacy admission process and its associated challenges at the institution where the decision support system was implemented are then described, followed by a description of the data mining methodology used for constructing the system. The manuscript then reviews the operational and learning outcomes of the implementation. This section provides guidance for the development of DSS systems for enrollment management. The paper concludes with a broader discussion of the insights for successful implementation of DSS systems.

## 2. Decision support systems in the admissions process

Applications of management science techniques in academic administration go back forty or more years. In early implementations, the issues addressed were planning, budgeting or resource allocation problems including the forecasting of enrollment levels as well as facilities requirement planning, course scheduling and staffing to support estimated enrollments (e.g., see [28] and [30]). A survey of 146 articles identified 104 that employed management science (optimization) techniques while only 6 of 146 articles featured DSSs to tackle academic management problems. In this survey, there were no examples of DSS deployed directly for enrollment management [34].

In general, research on enrollment management has centered on two areas: developing forecasting models for predicting overall enrollment levels and on tools for identifying which individual applicants to admit. Many of the institutional level forecasting studies build models to identify the traits of students that choose the focal institution over others (see, e.g., [13] and [27]). Multiple linear, logistic and probit regression models were observed as the most commonly employed techniques for forecasting at this level [26]. Logistic regression has been compared to neural networks for classifying which students will and will not enroll in a university, based on a variety of applicant attributes, and neural networks were found to outperform logistic regression for the correct classification of admitted applicants who ultimately will and will not enroll [33]. With respect to the current problem, these results provide insight, but unfortunately, none of these studies incorporate the amount of financial aid awarded to applicants, a significant factor in the enrollment decision [6].

Beginning in the late 1980s several researchers discussed the use of expert systems for determining which students to admit into a variety of academic programs in Great Britain and elsewhere [10–12, 19,23,24]. While several of these papers implicitly consider the probability of enrollment in the analysis, this body of work does not explicitly consider the financial impact of enrollment decisions on the institution, a fundamental concern for many institutions. As such, from an operational perspective, our work builds on previous studies by considering both the probability of enrolling and the amount of financial aid awarded.

The quality of the predictive model incorporated into the DSS is an essential element in improving the performance of its associated work system [2]. However, DSS systems should also provide for the systematic acquisition and sharing of tacit and explicit knowledge to improve effectiveness and control [1] as well getting the right information to the right people at the right time [25]. In our context, the DSS system should incorporate knowledge acquired from experience and historical data on enrollment probability and provide a mechanism to share this information explicitly with the admissions decision makers. With this in mind, this paper describes how the DSS' interface was crucial to make this information available effectively and expediently.

Hartono et al., [17] provide a valuable review of factors that lead to DSS success, and in particular the research demonstrates that the relative importance of various implementation factors depends on how success is defined. In this setting success for the DSS is defined as “organizational impacts” [8], that is improving operational performance and increasing explicit knowledge and knowledge sharing. Antecedents of success on organizational impacts include management support, organizational support and attitude, user participation and system characteristics [3,15,17,29,32,35]. In particular Teo [32] suggests four categories of critical success factors in a knowledge management DSS implementation: people and culture, implementation method, content management and technology. Experience with respect to these factors over the two year cycle of the DSS design and implementation is described towards the end of the paper. However, as one might expect, the specific aspects of these factors that are important differ in each setting. As such, previous work is useful in providing a basis towards a better understanding of how particular critical success factors transferred to this setting. The next section proceeds with a discussion of the enrollment management process prior to the implementation of the DSS.

## 3. The traditional enrollment management process

The Willamette University College of Liberal Arts (CLA) in Salem, Oregon is typical of small schools that have traditionally relied upon outside consultants for technical guidance. Each year, from a pool of more than 3000 applications, admission is offered to approximately 1800 applicants, to achieve a target entering class of approximately 500. In fact, the actual percentage of admitted students who will enroll is not known in advance, and hence a critical task for any admissions office is to accurately predict this percentage. The percentage of admitted applicants who ultimately enroll is referred to as the enrollment yield. If the yield is overestimated, fewer students than expected will enroll and revenue to the university will be reduced. If the yield is underestimated, a higher than expected number of students will enroll, possibly exceeding the fixed capacity of the school and resulting in significant incremental costs for additional housing, faculty, and other resources. In the worst case, over-enrollment could compromise the quality of instruction, as classrooms become overcrowded and student to faculty ratios exceed levels conducive to optimal learning. Therefore an accurate estimate of the enrollment yield is essential to effective fiscal planning.

![](/api/attachments/TTUB4ZVA/fulltext/images/45bbdf12e9ac0a7f1bd74a04417dd8458605678f4181ff55795ed1fe01b89788.jpg)  
Fig. 1. Traditional enrollment management process.

A second critical decision for the CLA admission staff is the allocation of financial aid to admitted students. All universities offer financial aid to a large proportion of their incoming students, both as a means of meeting students' financial need and as a recruiting tool. Financial aid allocations provide a powerful lever for admissions, but these decisions have major fiscal implications as well. Once the admission office has identified a set of students to admit, the admissions staff conducts an assessment of financial need and merit to determine how much aid to offer each admitted student. Prior to sending out the final admission letters and financial aid packages the admission office must estimate the discount rate, defined as the percentage of the total tuition which is offered to the enrolled class in the form of financial aid. From a fiscal point of view, operational performance of the admission office is assessed based on the accuracy of both the predicted enrollment yield for the admitted class and the discount rate associated with the admitted applicants who actually enroll.

## 3.1. The traditional process for estimating yield and discount rate

The enrollment management process traditionally begins by establishing targets for enrollment and the discount rate for the incoming class (see Fig. 1). Consultations begin in the summer prior to the year when the admit decisions must be made to establish enrollment and discount rate targets. For instance targets are established in summer of 2005, for admission decisions to be made in the spring of 2006 that result in an entering class in the fall of 2006. These discussions between the Dean's office, the admission office, the President and the VP of Finance attempt to balance the long-term strategic goals of the college (e.g., academic quality, geographic and ethnic diversity of the student body) with the fiscal implications of attempting to achieve those goals.

Once enrollment and discount rate targets are set, the information is sent to an outside consultant who returns a suggested financial aid allocation strategy for achieving these goals. This strategy is embodied in a grid corresponding to seven levels of financial need and five levels of academic quality. The grid in Table 1 provides an example of a recommended financial aid figure for each level of need and academic quality, which is typically received from the consultant no later than the middle of October.

Table 1  
Example of financial need-academic quality grid <sup>a</sup>

<table><tr><td rowspan="2"></td><td colspan="6">Academic rank</td></tr><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td rowspan="7">Need rank</td><td>1</td><td>$0</td><td>$0</td><td>$0</td><td>$1000</td><td>$2000</td></tr><tr><td>2</td><td>$0</td><td>$0</td><td>$1000</td><td>$2000</td><td>$5000</td></tr><tr><td>3</td><td>$0</td><td>$1000</td><td>$2000</td><td>$5000</td><td>$8000</td></tr><tr><td>4</td><td>$1000</td><td>$2000</td><td>$5000</td><td>$8000</td><td>$10,000</td></tr><tr><td>5</td><td>$2000</td><td>$5000</td><td>$8000</td><td>$10,000</td><td>$12,000</td></tr><tr><td>6</td><td>$5000</td><td>$8000</td><td>$10,000</td><td>$12,000</td><td>$18,000</td></tr><tr><td>7</td><td>$10,000</td><td>$12,000</td><td>$15,000</td><td>$18,000</td><td>$22,000</td></tr></table>

<sup>a</sup> Data in this table are for illustrative purposes only. Actual allocations vary from year to year and are proprietary.

By February 1, all applications have been received. The more than 3000 applicants are reviewed to make decisions on the obvious candidates for admission or denial. Preliminary decisions are based primarily on academic credentials (e.g., GPA, classes taken, test scores). At this initial stage of selection, other factors, including student background, interests and activities play a lesser role. Approximately 20% of the applicants who have good but not outstanding credentials are then subject to a subsequent review. In this subsequent stage of selection, the admissions staff confers to make final decisions as to which students will be admitted, denied admittance or entered onto a wait-list.

Once the final admit list is determined, admitted applicants are classified by need and academic rank, into the squares of the Need-Academic Quality grid and counts are determined. The grid, along with the data on admitted students and the total financial aid budget is then sent to the consultant who uses their proprietary models to estimate the enrollment yield and discount rate for the admit pool. The results of the consultant's analysis are returned to the admissions office and, if the estimates of yield and discount rate do not meet preselected targets, the consultants offer advice on how the dollar values in the grid might be altered to improve the results. Based on this advice, the CLA admission office makes final financial aid allocations for each cell of the grid. Admitted applicants are then sent offers of admission, including financial aid awards determined by their position in the grid. Admission office personnel wait for students to either accept or decline admission which is indicated through personal contact or receipt of a deposit from the student.

As acceptances and declines arrive at the admission office, progress is evaluated based on historical trends to determine whether developing yields appear to be on target. If deposits arrive at a rate lower than anticipated, the admission staff may turn to the wait-list to admit additional students. If acceptances are higher than anticipated, the university faces the prospect of being substantially above targets for enrollment, discount rate, and total financial aid budget.

## 3.2. Drawbacks of the traditional admissions process

Several shortcomings are apparent in the traditional CLA enrollment management process. First because the consultant's work utilizes proprietary models, admissions staff gains limited explicit knowledge into what factors are most important in influencing enrollment.

![](/api/attachments/TTUB4ZVA/fulltext/images/0745414d762856776ed700d1569c442e04e88930d4bedf75d5e93abd846e4987.jpg)  
Fig. 2. The CRISP Methodology [5].

Second, the consultant's model is based upon assumptions that are used to build models for a variety of clients. Thus, forecasts may not adequately account for idiosyncratic differences of the CLA. The model used is built based simply on the previous year's model and modified to incorporate, to a limited degree, any shift in strategic goals. Finally and perhaps most significantly, because the analysis is performed by an outside agency, admission personnel are limited in their decision making by the timing and scope of the information provided by the consultant.

The admission process has become much more fluid and unpredictable due to the sophistication of applicants who are likely to research and apply to multiple institutions over varying time periods [14,18]. This behavior leads to significant shifts in the make-up of the applications pool even within a specific year. As new applications are received the admission office must make intermediate decisions with respect to the admitted pool, and changes in the admit pool requiring ondemand model adjustments. While the consultant would typically provide updates on request, the timeliness of these updates is dependent on the consultant's workload at the time of the request. Since the consultant has multiple clients all with similar admission decision calendars, the CLA admission office often did not get the information when it was needed to make timely decisions.

The combination of the limited incorporation of the CLA specific factors and lack of timely updates led to a loss of control of the enrollment management process at CLA resulting in poor operational performance. This, in turn, led to the need for and development of an in-house DSS. As will be described in the sections that follow, the resulting system resulted in dramatically improved operational performance and increased institutional knowledge.

## 4. Building the predictive enrollment model for CLA

Data mining is the process of discovering trends and usable patterns in data. The objective of this process is to sort through large quantities of data to extract new information [16]. Data mining models are built guided by key outcomes desired by the users of the model (e.g., accurate yield prediction,) and what the data suggest are the key factors relating to the outcome. A model deployed via data mining may often rely upon a mixture of traditional statistical techniques (e.g., logistic regression,) in combination with standard data mining techniques discussed below.

The system developers, in this case professor and graduate students, followed the CRISP paradigm for data mining projects [7]. The paradigm suggests six steps to developing successful data mining models. The developers involved closely followed the steps from Institutional understanding, Data Understanding, Data Preparation, Modeling to Evaluation and Deployment. Fig. 2 presents a broader description of these steps and Fig. 3 shows the two-year development process actually used at the CLA.

## 4.1. System development — 2002–2003

Work began on the system in 2002 as part of a graduate data mining course being developed at the university. The developers agreed to, over a three-year period, build a DSS consisting of: (1) a predictive model to project, for individual applicants, the likelihood of enrollment and, in aggregate, the enrollment yield and discount rate; and (2) a managerial tool with a userfriendly interface that could be used to provide timely and effective guidance for policies and decisions surrounding admissions and financial aid.

![](/api/attachments/TTUB4ZVA/fulltext/images/eed6917322c17843e86bfc9196c842d20dd13317a09b53f671fcb4814ee97a49.jpg)  
Fig. 3. The CRISP Process Applied to the Admissions Management DSS Project.

In the fall of 2002, the following business goals were identified: annually enroll approximately 500 students with the highest academic quality possible; achieve diversity goals; maintain a discount rate at or below the target level. Following the CRISP methodology model, development began with interviews with enrollment managers to gain a better understanding of the institutional setting (i.e., develop business and data understanding). This also provided opportunities for institutional knowledge creation as admissions personnel became more familiar with data that would be used to drive the models.

Once data preparation was complete and the initial analysis database was constructed, the model building stage commenced. The initial analysis data set consisted of applicant records for thousands of applicants from three preceding admissions cycles, 2000–2002, and comprised over 60 variables, 40 of which were suggested by enrollment managers. The remaining variables were chosen from among those available but not initially considered important by these same managers. The data set was split equally into training and validation sets. All model development was conducted using training data.

As is typical of data mining initiatives, meta-level modeling was employed using a multiplicity of approaches – neural networks, decision trees, and logistic regression models – to arrive at the ultimate predictive model and tool. Because neural networks have the ability to accurately predict outcomes in complex problems ([9] p. 64), and because neural network models were found in a previous study to outperform other techniques in correctly classifying admitted applicant who will ultimately enroll or not enroll [33] modeling began with neural networks. All available predictors were included in a neural network model to: lend insight as to the most influential variables and to set initial benchmarks for the predictive accuracy that might reasonably be attainable from the available data. In this way, the goal of correctly predicting the ultimate enroll/decline decision for admitted students 71% of the time was established for any predictive model. Using the relative importance of inputs data reported the original collection of more than 60 candidate predictor variables included in the neural network model was narrowed to 30 as input for the logistic regression model building process. Because it is difficult to determine the exact relationships being modeled in neural network approaches and because this limited model transparency for the managers, the decision tree and logistic regression approaches were employed to determine if similar predictive accuracy could be achieved.

In contrast to regression-based approaches, decision trees offer potentially attractive modeling alternatives as they do not rely upon assumptions about the linearity relationship between the response and selected predictor variables, nor does their interpretation suffer from correlation among the predictor variables. Thus, in theory, decision trees potentially promise greater predictive accuracy and simpler interpretation. In the course of the modeling process, decision tree models based on C5.0 and C and R Tree algorithms<sup>2</sup> were developed, both as additional benchmarks of predictive accuracy and to lend additional modeling insights to further modeling development. The best of the tree-based models exhibited an overall predictive accuracy of 70.3%, comparable to that attained via neural networks. However, from the standpoint of the enrollment management application, decision tree models have a significant drawback, producing only discrete breakpoints to describe the influence of financial aid on applicant propensity to enroll. CLA managers, instead, required a tool that would allow them to assess the impact of relatively small adjustments to financial aid policies and individual award packages. Moreover, the decision tree models could not be easily deployed in a software package available to the managers. With these factors in mind a logistic regression was considered to determine if a model with similar predictive accuracy could be developed. Logistic regression offered the potential to provide insights offered into the relative strength and effect of individual predictors and in particular the ability to smoothly assess the impact of financial aid allocations. It was also easily deployed in the form of a Microsoft Access or Excel-based decision support tool. These factors together maximized the ease of understanding and implementation by enrollment managers.

The modeling process began by exploring main effects that would ultimately provide a parsimonious description with a reasonable degree of fit. A model consisting of eight variables – including applicant characteristics and financial aid allocations – was ultimately selected to predict the likelihood of enrollment. It accurately predicted enroll/decline decisions for a little over 70% of the applicants in the training set. To test the predictive accuracy, the model was then scored using the validation data set, and accurately predicted enroll/decline decisions 68% of the time, only marginally lower than training set results. The model was further evaluated over the summer of 2003 based on the actual enrollee data from 2003, and again, the model performed well, accurately predicting 70% of the time. Consultation between managers and analysts revealed one principal concern. While the overall predictive accuracy of the model was acceptable the model did a much better job of predicting who would not enroll than those who would enroll (see Table 2). This finding is not surprising because the model is designed to maximize the probability of correctly classifying any individual and approximately 70% of those admitted decline to enroll. However, for CLA, it is more important to predict which applicants will enroll than those who won't. Thus, it was agreed that future models would place a greater emphasis on predicting those who would actually attend.

Table 2  
Enrollee classification matrix (Overall 70%)

<table><tr><td></td><td colspan="2">Predicted 2003</td></tr><tr><td>Actual 2003</td><td>Enroll</td><td>Decline</td></tr><tr><td>Enroll</td><td>25% (Goal is to maximize)</td><td>12% (Goal is to minimize)</td></tr><tr><td>Decline</td><td>75% (Goal is to minimize)</td><td>88% (Goal is to maximize)</td></tr></table>

One of the key pitfalls of data mining models is that they often may be too complex for managers to interpret and use. To address this issue, during summer of 2003, a user-friendly deployment tool was developed to allow the admission personnel to make use of the predictive model with minimal understanding of the underlying model. This interface was developed in the Microsoft Access database environment with the focus on maximizing ease of use for the managers. Functionally, the interface allowed managers to predict total yield and discount rate at the aggregate level. It also allowed managers to assess the likelihood that any individual admitted applicant would attend. This enhanced the transparency of the process for CLA managers and afforded them the opportunity to react in real time to shifts in strategy and/or the enrollment environment. However, because of only limited understanding of the Microsoft Access database environment among enrollment managers, this interface did not allow the managers to easily view components of the underlying models, limiting transparency to some degree.

In the fall of 2003, the CLA admission office began using the initial DSS to guide enrollment management. Because of the instant access to model results, the admission office was able to generate timely initial estimates of yield and discount rate based on the inputs to the earlier mentioned financial aid matrix. Combined with the ability to predict enrollment on an individual basis, this provided the opportunity to better manage the discount rate by allowing the admission office to fine tune financial aid allocations to the individual level and optimize yield while still maintaining desired academic and diversity profiles. Thus, as will be discussed in the next section, operational results improved significantly.

Further, the initial DSS development process yielded significant enhancements to institutional knowledge. The inclusion of certain variables in the yield model suggested others that should be considered for inclusion in subsequent analysis. In addition, improved data understanding suggested that a more comprehensive predictive model incorporating interactions between variables might be useful in increasing accuracy. In terms of the interface, while predicting at an individual level was thought to be useful for managing enrollment yield and discount rates, it was found to be prohibitively time consuming. To address this, managers suggested that the interface be modified to provide a vehicle to break out projected enrollments by geographic region to support strategic CLA geographic diversity initiatives. Finally, the manager of institutional research suggested that the interface be provided in a format that would allow easy modifications to the underlying model in order to support additional analyses as will be described below.

![](/api/attachments/TTUB4ZVA/fulltext/images/91d27b01f3ee68b60c7e23bf669bfbecf909a18589d14c944fa50d9302da3f51.jpg)  
Fig. 4. Decision trees for interaction detection. A: interaction between geography and aid award. B: interaction between geography and campus visit.

Table 3

## 4.2. System refinement 2003–2004

The second year of DSS development began by incorporating a number of new variables into the database and reformatting others to make the model development process more efficient. The total time devoted to understanding and setting up the data for the second stage of modeling was reduced from eight months to four. The modeling phase for the second year began with the investigation of interactions between predictors suggested by the 2002–03 model development process. Four years of data (2000–2003 admits) were used to identify highly correlated variables (via the use of plots and correlation matrices) and highly correlated cases (through the use of cluster analysis). In terms of the highly correlated cases, the team searched for large groups of applicants with similar characteristics that appeared to have an unusually high or unusually low propensity to attend. When these groups were identified, indicator variables were created to capture group membership information. Following data exploration, the full data set was again split randomly into two equal parts and the training set was used to develop a revised logistic regression model for deployment.

Potential extensions of the 2002–03 model were investigated including using variable interaction terms determined via additional meta-modeling. The refinement work began by executing several decision tree modeling routines on the training data set to identify potential interaction terms for inclusion.

The process of interaction detection was as follows:

▸ First, a decision tree model with the outcome variable enroll/decline was created. This model included:

○ All the variables included in the 2002–03 model.

○ Any variables suggested by managers in working with the model in 2002–03.

○ Flag variables to identify the effects of being a member of 2 groups suggested in the exploration phase described above.

▸ The output of the decision tree was examined to determine if any of the most important variables suggested by the tree differed at lower levels based on additional variable included in the model. For example:<sup>3</sup>

○ In Fig. 4A admitted students from Oregon were somewhat more likely to enroll (55% likelihood of enrollment). However, if they were promised high levels of financial aid (in this case more than \$10,000) they were much more likely to enroll (75% likelihood of enrollment). However, outof-state applicants did not show a similar increase in propensity to enroll at similar levels of financial aid. This might suggest an interaction between Oregon residence and aid provided.

○ In Fig. 4B, admitted students from outside Oregon were not very likely to enroll (22% chance of enrollment). However, out of state applicants who also visited campus were much more likely to enroll (55% chance of enrollment). For Oregon applicants, the likelihood of enrollment was relatively high whether they visited campus or not (55%). This suggests an interaction between non-residents and campus visits.

The main effects (variables from year 2002–03 model, new variables suggested by managers based on their learning from the first year, new flag variables suggested in the exploration stage) and interaction effects (suggested by the decision trees) were included in a preliminary logistic regression model. The new model initially consisted of 18 variables (see Table 3 for the set of predictors used in the model.) The predictors of enrollment probability included entrance scores, high school grade point average, geographic origin, the financial need of applicants as well as grant, scholarship and loan amounts in the financial aid package.<sup>4</sup> Prior to commencing the final model selection process, the training data set was balanced to reduce the model's tendency to over-predict the decliners. Many successive iterations of the logistic regression model were investigated before arriving at a final model with a prediction accuracy of 69.2% detailed in the Table 4 below. Examining the table reveals that by including selected interactions and balancing the data, the ability to successfully predict those admitted applicants who would actually enroll, as per management requirements, increased substantially from 25% to 65.7%.

Main effect predictors in the mode

<table><tr><td>Predictor</td><td>Description</td></tr><tr><td>Hsgpa</td><td>High School GPA</td></tr><tr><td>Othersch</td><td>Number of other schools to which the applicant applied based on FAFSA information applied</td></tr><tr><td>Need grant</td><td>Amount of aid award based on need</td></tr><tr><td>Merit grant</td><td>Additional award based on merit</td></tr><tr><td>Workstudy</td><td>Promised amount of work dollars</td></tr><tr><td>SATSOFT</td><td>A measure of SAT and/or imputed SAT based on ACT score</td></tr><tr><td>Sex</td><td>Gender of the applicant</td></tr><tr><td>Apptype</td><td>Early admit or Regular admit</td></tr><tr><td>Alum</td><td>Were the applicant’s parents alumni?</td></tr><tr><td>Appfacstaff</td><td>Were the applicant’s parents faculty or staff?</td></tr><tr><td>Visit</td><td>Had the applicant visited campus?</td></tr><tr><td>High school type</td><td>Public or private</td></tr><tr><td>Comp1</td><td>Had the applicant applied to an identified competitor based on FAFSA information?</td></tr><tr><td>Comp2</td><td>Had the applicant applied to an identified competitor based on FAFSA information?</td></tr><tr><td>Comp3</td><td>Had the applicant applied to an identified competitor based on FAFSA information?</td></tr><tr><td>Territory</td><td>What part of the country was the applicant from?</td></tr><tr><td>Need rank</td><td>Need rank on the grid</td></tr><tr><td>Merit rank</td><td>Merit rank on the grid</td></tr></table>

Table 5  
Table 4  
Enrollee classification matrix-training data set (Overall 69.2%)

<table><tr><td rowspan="2">Actual 2000–2003</td><td colspan="2">Predicted 2000–2003</td></tr><tr><td>Enroll</td><td>Decline</td></tr><tr><td>Enroll</td><td>65.7% (Goal is to maximize)</td><td>27.3% (Goal is to minimize)</td></tr><tr><td>Decline</td><td>34.3% (Goal is to minimize)</td><td>72.7% (Goal is to maximize)</td></tr></table>

The 2003–04 predictive model was submitted to test–retest validation, and while the results of this test were somewhat lower than those observed in the test set (see Table 5 below), they were deemed consistent with respect to the training data set. This conclusion is further supported by the observation that the same variables were statistically significant in both data sets and that the predictive validity was similar.

The DSS interface was also altered substantially from the first year to enhance functionality and ease of use. Specific changes included:

▸ The DSS was re-deployed in Microsoft Excel. This approach permitted the institutional research manager to easily develop auxiliary tools to better inform the enrollment management process.

▸ The revised DSS incorporated a new screen where the managers could modify financial aid allocations for each cell in the grid, to assess the effect on yield within particular cells and overall. For example, in Fig. 5A, the amount of financial aid given a student deemed a “3” on the academic quality scale and a “4” on the financial need scale is \$3000, yielding 25%. Fig. 5B shows changing the amount of financial aid in the cell to \$5000 increases the projected enrollment yield to 32.7%.

The revised DSS includes a screen which breaks out the expected yield by in-state and out-of-state admits. This feature was introduced to support CLA's strategic goal of geographic diversity.

▸ In addition to providing cell based results, the screen also provides aggregate level predictions of total financial aid outlays and the discount rate.

The DSS continued to include a screen that allowed managers to assess individual applicant level probabilities of enrollment. Users simply enter actual data values for the required variables and the interface displays the predicted enrollment probability for an individual applicant. If desired, the manager can then experiment with alternative financial aid awards to increase the probability of an applicant enrolling (See Fig. 6A and B).

## 5. Organizational impacts on the admissions work system realized with the DSS

The implementation of the DSS resulted in superior operational performance, and perhaps even more importantly, the modeling and system development activity provided a number of learning opportunities for CLA admissions office and the internal developers. The most significant indicator of the impact of the new DSS and its associated implementation activities was that it substantially and beneficially altered the process by which admissions activities are carried out. Using the knowledge acquired through the project and the resulting system, the admission staff altered the sequence, effectiveness and expediency of enrollment decision making (See Fig. 7.)

## 5.1. An improved enrollment management process

Through direct participation in the model development, the CLA admissions staff gained new insight into their own process, insight that would never have emerged under the traditional approaches employed by outside consultants. For example, admissions staff was now able to create an initial financial aid allocation grid, demonstrating the admissions decisions makers' explicit understanding of what may formerly have been only tacit knowledge. Managers now understand how financial aid choices affect discount rate and can capitalize on previous experience as well as an improved understanding of process goals, resulting in more precise estimates of enrollment yield and discount rate.

Enrollee classification matrix-validation set (Overall 66.8%)

<table><tr><td rowspan="2">Actual 2000–2003</td><td colspan="2">Predicted 2000–2003</td></tr><tr><td>Enroll</td><td>Decline</td></tr><tr><td rowspan="2">Enroll</td><td>61.0%</td><td>30.4%</td></tr><tr><td>(Goal is to maximize)</td><td>(Goal is to minimize)</td></tr><tr><td rowspan="2">Decline</td><td>39.0%</td><td>69.6%</td></tr><tr><td>(Goal is to minimize)</td><td>(Goal is to maximize)</td></tr></table>

The DSS reduces the time spent by admissions staff on the grid construction and assessment, increasing the time available to manage individual cases. Under the old process, almost all evaluation of financial aid allocations was conducted at the grid level and individual applicant level modifications were limited. Under the new process, up to 50% of the individuals admitted receive applicant-specific adjustments to their financial aid package, and the estimated impact of these adjustments is immediately assessed. The number of adjustments to the financial aid grid and the level of attention to directed towards individual financial aid packages would not have been possible without the analytical support of the DSS tools or the in-depth knowledge gained through the implementation process.

In addition more precise estimates of admission yield, enrollment predictions at the individual level support better estimates of incoming class characteristics – expected revenue and class profile with respect to academic quality, geographic and ethnic diversity. For individual applicants with given academic quality indicators, geographic origin and financial need, sensitivity curves can developed for varying levels of financial aid. As grants and scholarships increase while, correspondingly, loans decrease as a proportion of the total aid package, the probability of enrollment increases. Analyzing groups of admitted applicants that are homogeneous with respect to academic quality and financial need, financial aid sensitivity curves can also be obtained, allowing for the identification of aid thresholds above which the probability of enrollment moves a group into the “likely to enroll” range. This information is used to advise CLA admission policy and to inform the distribution of financial aid.

A  
![](/api/attachments/TTUB4ZVA/fulltext/images/e897d861046311625b60bb18a50b0d6251c3bc4e312b8483248f709244cbd6db.jpg)  
Fig. 5. A: financial need-academic quality grid. B: revised financial aid example in financial need-academic quality grid.

![](/api/attachments/TTUB4ZVA/fulltext/images/180912d9eafbcd85aa37bada553d216fe78a79eb239ff44e2bdb368eddaac683.jpg)  
continued

## 5.2. Real-time management of enrollment during the acceptance period

Once offers of admission are sent to applicants, these potential students have approximately one month to accept or decline. Admissions staff can use the system to rank students based on the model's estimate of their probability of enrolling. Once enrollment accept/declines begin coming in, the managers can use the system's interface to track how well the model predicted actual enrollment decisions. If a trend is detected where enrollment acceptance rates are coming in below projections, admissions managers can move quickly to start making offers from the wait-list. In addition, they can observe acceptance trends in financial aid, and gain insight into how much additional financial aid incentives might be available to influence admitted students who have not yet responded. In this way, the model and system interface support real-time enrollment management as the early results unfold.

## 5.3. Shifts in responsibilities of admissions managers

The introduction of the interface resulted in several new responsibilities for the managers that were formerly performed by the outside consultant. Shifts in responsibilities are summarized in Figs. 1 and 7, depicting the traditional and revised enrollment processes. These include:

➢ The initial financial aid grid, which serves as the foundation for the overall strategy, was previously developed by the outside consultant, largely on the basis of a single year of data. The revised process relies upon CLA top management using knowledge that they have accumulated through the in-house development process.

➢ The new interface allows managers to systematically analyze individual applicants, resulting in more individual adjustments to aid awards. Thus, the DSS and supporting interface is driving a migration from grid level analysis to individual level analysis.

A  
![](/api/attachments/TTUB4ZVA/fulltext/images/84c46cd7cf09303797e6b3d9ca32ef5861bbcfda777bc98e9910d07108f4fd64.jpg)  
Fig. 6. A: individual prediction <sup>7</sup>of probability of enrolling. B: individual prediction<sup>7</sup> of probability of enrolling with increase in aid.<sup>7</sup>

➢ The lead time required when working with the outside consultant was significantly reduced. Previously, it was difficult to determine in a timely fashion, if enrollment projections for enrollment developing according to plan. The in-house DSS interface allows for more rapid adjustment to unexpected market conditions, permitting enrollment decision makers to manage their wait list more strategically.

## 5.4. Operational results

The operational results attributable to the revised data-driven process for enrollment management (see Table 6) are quite impressive, especially relative to those realized in the two years preceding implementation. The first row of Table 6 illustrates the percentage variance between the targeted and actual enrollment. In the preceding years, the actual enrollment was 17–21% above or below desired enrollment.<sup>5</sup> In 2004–05, using the new system, the variance was less than 5%. Variance from the target discount rate was reduced from 2–3.5% under the consultant to less than 1%.<sup>6</sup> Moreover, a 1% reduction in the discount rate can yield hundreds of thousands of dollars in additional revenue to the university. From 2003 to 2005, using the new DSS, the CLA was able to reduce the discount rate by over 10%.

![](/api/attachments/TTUB4ZVA/fulltext/images/0ac61372fe22b0fde105975be91cdfe223d5531a5d1b5f8e60358a5c3ed1e793.jpg)  
continued

These results were achieved without any decline in academic quality (as indicated by SAT scores in Table 6.) There was a precipitous drop in ethnic diversity in 2004 and hence, ethnic diversity was identified as a point of emphasis in developing the underlying enrollment forecasting for the subsequent year. In year four, 2005, ethnic diversity rebounded along with significant gains in geographic diversity, with 4.6% more students from outside Oregon and 5.8% more students from outside the northwest region, while median SAT declined.

## 5.5. Costs of DSS implementation

The CLA paid the University's school of management a fixed yearly fee to support the purchase of specialized software, and a faculty member's time for project oversight. During the development period, total monetary outlays were less than \$50,000. As noted above, a 1% reduction in the discount rate yields hundreds of thousands of dollars in additional revenue to the university and the discount rate decreased 10% over the three-year implementation period. Thus, from a purely monetary cost-benefit perspective the implementation was hugely successful.

Other costs that are more difficult to quantify relate to the time that CLA management spent in: 1) educating project participants (graduate students) in enrollment business procedures; 2) providing input on interface development to achieve both maximum functionality and ease of use; 3) learning how to assimilate DSS tools into business processes. Initial time costs of education and development were substantial in the first year of the project but declined dramatically in years two and three.

However development costs also yielded intangible benefits equally difficult to quantify. The activities associated with DSS development and the use of the DSS itself resulted in immeasurable gains in process knowledge and significant process improvements. The DSS implementation project assists enrollment managers in making more precise financial projections and allows for significant gains in real-time response to shifts in the enrollment environment. All of these factors, led to improved enrollment management as well as major strides in class quality, diversity, and financial performance.

![](/api/attachments/TTUB4ZVA/fulltext/images/b3603361de46f108dbf7cf4df0bb71de20f0ad543a6277437579d6dab4b0beda.jpg)  
Fig. 7. The revised CLA admission process.

Enrollment outcomes for new freshmen

<table><tr><td>Outcome</td><td>2002</td><td>2003</td><td>2004</td><td>2005</td></tr><tr><td>Enrollment variance (actual-target)/target</td><td>-16.9%</td><td>+21.1%</td><td>+2.5%</td><td>-4.4%</td></tr><tr><td>Tuition discount variance (actual-target)/target</td><td>-3.5%</td><td>+2.0%</td><td>-0.5%</td><td>-0.4%</td></tr><tr><td>SAT median</td><td>1230</td><td>1250</td><td>1260</td><td>1230</td></tr><tr><td>Ethnic minority representation</td><td>20.8%</td><td>19.2%</td><td>15.4%</td><td>18.0%</td></tr><tr><td>Non-Oregon representation</td><td>59.8%</td><td>59.7%</td><td>61.4%</td><td>66.0%</td></tr><tr><td>Non-northwest representation (students from outside, Washington, Montana, Idaho, or Wyoming)</td><td>32.5%</td><td>34.2%</td><td>34.4%</td><td>40.2%</td></tr></table>

## 6. Insights on the implementation of DSS systems

Project outcomes detailed in the preceding section provide guidance for managers developing and implementing DSS systems in enrollment work systems. This section considers the general contributions of the project to the DSS implementation literature.

In terms of the frameworks provided in [17] and [32], implementation insights from the enrollment management DSS support the necessity of top management and organizational support, in particular a culture accepting of knowledge sharing. Both the Vice President for Enrollment and the University President, spurred by the lackluster performance of the traditional process, were strong advocates for process change. This permitted internal developers initial access to data and personnel that would not otherwise have been available. Over time, the internal developers were able to gain the deep enterprise and data understanding that are crucial to any successful DSS development project. It was also noted in [3,11,17,29] that top management support was a key to success in the development of an admissions DSS with respect to “opening doors”.

The internal developers spent a great deal of time educating the admissions staff to the potential of various solutions alternatives. The decision to use a logistic regression model as the fundamental predictive tool was one result of this interaction. Over the duration of the project, the internal developers and the admissions staff built up trust, resulting in the reciprocal knowledge sharing culture that has been suggested as a key success factor [3,15,17,32]. Further, the transparency of the DSS interface further supported the knowledge sharing culture, especially during the second year when it was redeployed in Microsoft Excel. By providing a mechanism whereby non-technical users and technical users could collaborate and share ideas, the interface promoted a free flow of knowledge that led to significant enhancements.

Project leadership and organization (during implementation) are other “people” factors generally believed to be critical to the success of a DSS implementation project [3,15,17,32]. Given that the number of project stakeholders was relatively small, fewer than ten, project leadership and team composition were perhaps less important than observed in larger project settings [11,32]. Moreover, given the environmental factors (poor historical performance) and the clearly articulated goals, individuals on both sides (admissions and internal developers) were highly motivated to succeed.

As is typical of many DSS and data mining projects, the admissions DSS was implemented in two phases and continues to be enhanced annually. Similar to the examples in [11] and [32] components were added over time, with more sophisticated functionality added in the later phases of the project. The key observation here is that learning by DSS implementers must continue to occur even after initial implementation. For example, user feedback from the 2002–03 year helped drive interface movement from MS Access to MS Excel, improving system functionality and transparency. Overall, the gradual implementation of new complex functionality is preferred to all at once rollout [11].

System characteristics, and in particular content management, was central to the successful implementation of a knowledge management DSS for Singapore's housing department [32]. In the enrollment management project, content is not as directly relevant to success as is the management of the predictive model's quality. The model is currently reevaluated and updated annually by the internal developers with ongoing performance evaluation. In this sense, the project requires continual attention from both the internal developers and admissions staff. As observed elsewhere, incentives are a requirement for ongoing participation [15,17,32]. In this case admissions managers provide their insight in order to improve performance gains with respect to their activities. The internal DSS developers continue to view the system as a learning opportunity and real-life experience, both for the professors and participating graduate students.

At the heart of many DSSs is the technological platform upon which the system is built. The enrollment management model was developed using Clementine, the SPSS data mining product, but the end-user sees only the final Microsoft Excel deployment. Deployment migration from Microsoft Access to Microsoft Excel was based on the admissions staff desire for instantaneous feedback on the impact of grid adjustments that was not so immediately achievable in the initial database application. This also supports the contention of many [11,29,32] that choosing technology with minimum training and/or providing effective training for the technology chosen can enhance information flows in the organization.

## 7. Conclusion and further research

DSS design and implementation is, at its core, an iterative activity. Data mining procedures lend themselves well to data intensive DSS implementations as additional data and new modeling approaches can be readily incorporated. In any case, properly built DSSs require regular user interaction and trust, both from enduser and designer perspectives. Effective implementation processes promote knowledge sharing through business and data understanding phases and favors deployment mechanisms that provide for the capture and free flow of tacit knowledge between managerial and technical project personnel.

Enrollment management essentially requires decisions on which students to admit and what price to charge for each available slot in the university; in order to maximize student quality; with constraints on capacity, discount rate, and target demographic composition of the admitted class. Optimization solutions for seemingly related yield or revenue management problems in the airline and hospitality industry have been broadly investigated [4,20–22,31]. However, rather than optimizing on a financial objective, enrollment managers seek to maximize quality, long-term customer value, subject to financial constraints, capacity and discount rate. Continuing research will seek to more systematically address optimization objectives and incorporate optimization tools into a further improved DSS.

This paper presents an example of successful DSS design and implementation to improve the enrollment work system at a small liberal arts college. Comprised of two interrelated components, a predictive model and a user friendly deployment tool, the DSS and the associated implementation have significantly improved financial performance in enrollment. More importantly, the two-year implementation yielded dramatically enhanced understanding of the enrollment work system and serves as a vehicle for the conversion of tacit process knowledge into readily deployable explicit understanding.

## References

[1] M. Alavi, D.E. Leidner, Review: knowledge management and knowledge management systems: conceptual foundations and research issues, MIS Quarterly 25 (1) (1999) 107–136.

[2] S. Alter, A work system view of DSS in its fourth decade, Decision Support Systems 38 (2004) 319–327.

[3] D.S. Bajwa, A. Rai, I. Brennen, Key antecedents of executive information systems success: a path analytic approach, Decision Support Systems 22 (1) (1998) 31–43.

[4] P.P. Belobaba, Airline yield management: an overview of inventory seat control, Transportation Science 21 (2) (1987) 63–73.

[5] B. Bontrager, Strategic enrollment management: core strategies and best practices, College and University Journal 79 (4) (2004) 9–16.

[6] A. Braunstein, M. McGrath, D. Pescatrice, Measuring the impact of income and financial aid offers on college enrollment decisions, Research in Higher Education 40 (3) (1999) 247–259.

[7] P. Chapman, J. Clinton, R. Kerber, T. Khabaza, T. Reinartz, C. Shearer, R. Wirth, CRISP\_ DM 1.0, CRISP-DM Consortium, 2000.

[8] W.H. Delone, E.R. MacLean, Information system success: the quest for the dependent variable, Information Systems Research 3 (1) (1992) 60–95.

[9] M. Dunham, Data Mining: Introductory and Advanced Topics, Pearson Education Inc, Upper Saddle River, New Jersey, 1993.

[10] J.S. Edwards, J.L. Bader, Expert systems for university admissions, Journal of the Operational Research Society 39 (1) (1988) 33–40.

[11] A.A. Elimam, A decision support system for university admission policies, European Journal of Operational Research 50 (2) (1991) 140–156.

[12] P.N. Finlay, M. King, Experiences in developing an expert system for MBA admissions, Journal of the Operational Research Society 40 (7) (1989) 625–635.

[13] G.H. Gaither, F.O. Dukes, J.R. Swanson, Enrollment forecasting: use of a multiple-method model for planning and budgeting, Decisions Sciences 12 (2) (1981) 217–230.

[14] K.M. Galoti, M.C. Mark, How do high school students structure an important life decision? A short-term longitudinal study of the college decision making process, Research in Higher Education 17 (1994) 589–607.

[15] M.J. Ginzberg, Early diagnosis of MIS implementation failure: promising results and unanswered questions, Management Science 27 (4) (1981) 459–478.

[16] R. Groth, Data Mining: Building Competitive Advantage, Prentice Hall, New Jersey, 1999.

[17] E. Hartono, R. Santhanam, C.W. Holsapple, Factors that contribute to management support systems success: an analysis of field studies, Decision Support Systems 43 (1) (2007) 256–268.

[18] D. Hossler, J. Schmit, N. Vesper, Going to college: how social, economic and educational factors influence the decisions students make, The Johns Hopkins University Press, Baltimore, 1999.

[19] J.V. Iyengar, An expert system for MBA admissions, Journal of Computer Information Systems 36 (1995).

[20] V. Liberman, U. Yechiali, On the hotel overbooking problem, Management Science 24 (11) (1978) 1117–1126.

[21] K. Littlewood, Forecasting and control of passenger bookings, AGIFORS Proceedings, vol. 12, Nathanya, Israel, 1972.

[22] J.I. McGill, G.J. Van Rizyn, Revenue management: research overview and prospects, Transportation Science 33 (2) (1999) 233–256.

[23] C.A. Molinero, M. Qing, Decision support systems for university undergraduate admissions, Journal of the Operational Research Society 41 (3) (1990) 219–228.

[24] J.S. Moore, An expert system approach to graduate school admissions decisions and academic performance prediction, Omega International Journal of Management Science 26 (5) (1998) 659–670.

[25] C. O'Dell, S. Elliot, C. Hubert, Achieving knowledge management outcomes, in: C. Holsapple (Ed.), Handbook on Knowledge Management: Knowledge Directions, Springer, Heidelberg, 2003.

[26] M.B. Paulsen, College choice: understanding student enrollment behavior, ASHE-ERIC Higher Education Report No. 6, George Washington University, School of Education and Human Development, Washington, DC, 1990.

[27] J.A. Pope, J.P Evans, A forecasting system for college admissions, College and University Journal 60 (1985) 113–131.

[28] G. Rath, Management science in university operation, Management Science 14 (6) (1968) B373–B384.

[29] R. Santhanam, T. Guimaraes, J. George, An empirical investigation of ODSS impact on individuals and organizations, Decision Support Systems 30 (1) (2000) 51–72.

[30] R. Schroeder, A survey of management science in university operations, Management Science 19 (3) (1973) 895–906.

[31] B.C. Smith, J.F. Leimkuhler, R.M. Darrow, Yield management at american airlines, Interfaces 22 (1) (1992) 8–31.

[32] T.S.H. Teo, Meeting the challenges of knowledge management at the housing and development board, Decision Support Systems 41 (1) (2005) 147–159.

[33] S. Walczak, T. Sincich, A comparative analysis of regression and neural networks for university admissions, Information Sciences 119 (1/2) (1999) 1–20.

[34] G.P. White, A survey of recent management science applications in higher education, Interfaces 17 (2) (1987) 97–108.

[35] Y. Yoon, T. Guimares, Q. O'Neal, Exploring the factors associated with expert system success, MIS Quarterly 19 (1) (1995) 83–106.

![](/api/attachments/TTUB4ZVA/fulltext/images/de2c5baefd800081717aba7263aebe9c2f6755a4500a0548750b5edb25cfbc16.jpg)  
Elliot Maltz received his Ph.D. in Marketing from the University of Texas at Austin. Dr. Maltz's current research focuses on effectively transmitting and combining market information to facilitate new product development and respond to changes in market conditions. He has published in the Harvard Business Review, Journal of Marketing, Journal of Marketing Research, The Journal of the Academy of Marketing Science, and Sloan Management Review.

![](/api/attachments/TTUB4ZVA/fulltext/images/e52cfd096b1628c65b7acd6a900a31a3861bae23e82b285a744c8d212955f8d4.jpg)

Kenneth Murphy holds a Ph.D. in Operations Research from Carnegie Mellon University. Dr. Murphy's work on integrated systems has followed several threads including the financial justification of large-scale systems using both tangible and intangible factors, and investigating the tools and methods for successful system implementation. He has published in Operations Research, Communications of the ACM, and the Information Systems Journal among others.

![](/api/attachments/TTUB4ZVA/fulltext/images/9269474ee60957c0bbc2f6fa2ba06c8ec5c0dbf03cd4c5f273447528b83b3047.jpg)

Michael L. Hand is a Professor of Applied Statistics and Information Systems. Dr. Hand has been widely recognized for his distinguished teaching and is a two-time recipient of Willamette University's highest teaching award. Professor Hand is the coauthor of a leading college statistics textbook and is the author or coauthor of a number of scholarly articles in statistics and statistical computing, both basic and applied. He is an experienced management consultant, with clients includ-

ing — Hewlett Packard, Safeco Corporation, the State of Arizona, and most major agencies of the State of Oregon.
