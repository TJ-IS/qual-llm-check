---
otero_id: 8928
otero_key: "X5UZVYZ7"
title: "Employees recruitment: A prescriptive analytics approach via machine learning and mathematical programming"
authors: "Dana Pessach; Gonen Singer; Dan Avrahami; Hila Chalutz Ben-Gal; Erez Shmueli; Irad Ben-Gal"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113290"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Employees recruitment: A prescriptive analytics approach via machine learning and mathematical programming

![](/api/attachments/X5UZVYZ7/fulltext/images/275f4a8d94dc728e733ce138d48cba50033625906fa67bd17785f59d7379b596.jpg)

Dana Pessach<sup>a,⁎</sup>, Gonen Singer<sup>b</sup>, Dan Avrahami<sup>a</sup>, Hila Chalutz Ben-Gal<sup>c</sup>, Erez Shmueli<sup>a</sup>, Irad Ben-Gal<sup>a</sup>

<sup>a</sup> Department of Industrial Engineering, Tel-Aviv University, Israel

<sup>b</sup> Faculty of Engineering, Bar-Ilan University, Israel

<sup>c</sup> Department of Industrial Engineering and Management, Afeka College of Engineering, Israel

## A R T I C L E I N F O

Keywords: Recruitment Machine learning Human resource analytics Explainable artificial intelligence Interpretable AI Mathematical programming

## A B S T R A C T

In this paper, we propose a comprehensive analytics framework that can serve as a decision support tool for HR recruiters in real-world settings in order to improve hiring and placement decisions. The proposed framework follows two main phases: a local prediction scheme for recruitments' success at the level of a single job placement, and a mathematical model that provides a global recruitment optimization scheme for the organization, taking into account multilevel considerations. In the first phase, a key property of the proposed prediction approach is the interpretability of the machine learning (ML) model, which in this case is obtained by applying the Variable-Order Bayesian Network (VOBN) model to the recruitment data. Specifically, we used a uniquely large dataset that contains recruitment records of hundreds of thousands of employees over a decade and represents a wide range of heterogeneous populations. Our analysis shows that the VOBN model can provide both high accuracy and interpretability insights to HR professionals. Moreover, we show that using the interpretable VOBN can lead to unexpected and sometimes counter-intuitive insights that might otherwise be overlooked by recruiters who rely on conventional methods.

We demonstrate that it is feasible to predict the successful placement of a candidate in a specific position at a pre-hire stage and utilize predictions to devise a global optimization model. Our results show that in comparison to actual recruitment decisions, the devised framework is capable of providing a balanced recruitment plan while improving both diversity and recruitment success rates, despite the inherent trade-of between the two.

## 1. Introduction

One of the most challenging and strategic organizational processes is to eficiently hire suitable workforce. A comprehensive study by the Boston Consulting Group has shown that the recruitment function has the most significant impact on companies' revenue growth and profit margins compared to any other function in the field of human resources (HR) [1]. Indeed, poor recruitment decisions may lead not only to lowperforming employees but also to increased turnover. Turnover may have a direct impact stemming from employee replacement costs (e.g., interviews and rehiring costs, training and productivity loss, overtime of other employees), as well as indirect efects, such as poor service to clients or a decline in employee morale [2]. Thus, improving organizational recruitment processes by hiring the most suitable candidates has a significant impact on organizational performance [3,4].

In this study, we propose a data analytics approach, which can be used as a decision support tool for recruiters in real-world settings to improve hiring decisions of candidates to specific positions or jobs. The proposed approach comprises two components: a local prediction model for recruitment success per candidate and job type, and a global optimization model of the recruitment process.

The first part of this study is based on interpretability ML modeling, which provides meaningful insights into the potential recruitments related to the candidate's background features as well as the planned job placement. The output of these models is the probabilities of successful recruitment per employee and job. The second part in this research is based on a mathematical modeling formulation at an organizational level that takes into account multi-objective considerations and optimize the recruitment process over many candidates and jobs by using the success probability outputs of the ML models.

Previous eforts have been invested in trying to predict recruiters' decisions (e.g., [5,6]). Such prediction models, if accurate enough, may eventually replace the human recruiter and save a considerable amount of resources. Note, however, that recruiters' decisions are inherently subjective, and human intuition plays an important part in recruitments and placements. Hence, using interpretability modeling tools that can enrich and guide recruiters' decisions by insight seems to be a relevant approach, which recently gained popularity and is also known as explainable artificial intelligence (XAI) (see, for example, [7]). Another line of work has focused on the post-hire prediction of turnover or performance (e.g., [8]). While such measures are somewhat more objective, post-hire prediction eforts might be too late in certain cases to act upon. Therefore, in this paper, we focus on the pre-hire prediction of performance and turnover as a combined objective measure.

A key property of our approach is the interpretability of predictions, providing a useful explanation of how they are obtained. Apart from the accuracy of the prediction model, users' trust in the model is often directly impacted by how much they can understand and anticipate its behavior [9]. Understanding why the model behaves the way it does may increase users' trust and their potential to act upon its recommendations. This is especially true in decisions that involve human beings' intuition, such as in the case of employees' recruitment and job placement.

To address the prediction task described above, we propose applying the interpretable Variable-Order Bayesian Network (VOBN) model [10,11]. In contrast to other interpretable models such as decision trees, which often sufer from high variance and overfit to the training set, the VOBN model provides an inherent modeling flexibility that reduces such efects. Therefore, it often results in an improved generalization and predictive ability over various test sets. Finally, we show that the VOBN model is also flexible enough for mining significant patterns and insights in HR data.

Nevertheless, recruitment requires not only hiring the highest-potential workforce, but also meeting other organizational objectives. For example, there is a necessity to meet the demand for employees in diferent departments, the facilitation of diversity in teams and the al location of the workforce among diferent departments in a balanced manner. Each of these dimensions may also include numerous points of view: the local point of view of each separate candidate-position pair, the positional point of view and the organizational or regulatory point of view. Given that there are requirements of various stakeholders in the organization, there is a need to balance the trade-ofs in this multi objective scenario. Hence, in the second part of this research, we address the recruitment problem with a global perspective by accounting for the various dimensions and points of view.

We evaluate the proposed method using a unique dataset obtained from a large nonprofit service organization that is highly diversified over roles, accountabilities and job descriptions, with heterogeneous population of employees with diverse backgrounds, geographic locations and levels of socioeconomic status.

The dataset includes a rich feature set of hundreds of thousands of employment cases collected over a decade and represents a wide range of heterogeneous populations. These characteristics enable us to test potentially biased recruitment policies and placement decisions that traditionally may not be tested due to the absence of suficient data on such large groups in the population.

The results of our evaluation reveal that the proposed prediction approach can perform well in terms of both accuracy and interpretability, despite the inherent trade-of that often exists between the two [9,12]. In addition, we demonstrate how our interpretable approach can be used to extract meaningful insights that may support and benefit the recruiters' decision process. These extracted insights are sometimes counter-intuitive and shed light on the limitations of existing approaches and on the recruiters' intuition, which is limited and biased at times.

Moreover, we demonstrate that it is feasible to predict a successful placement of a candidate to a specific position at a pre-hire stage with a relatively high prediction performance (AUC = 0.73) and then utilize these predictions to devise a global optimization model. Our results show that using the proposed mathematical programming model, we are able to increase diversity (by 40%) while maintaining a high level of recruitment success (decreased by only 1%). Moreover, the results show an improvement of both diversity and recruitment success rates compared to recruiters' actual selections, although these objectives are generally found to be in conflict. The proposed approach can provide recruiters and organizations alike, with an applicable decision support tool for hiring successful candidates while improving organizational recruitment and placement processes and procedures.

This paper is structured as follows. Section 2 reviews the relevant literature. Section 3 describes the proposed analytics framework and the experimental settings. Section 4 describes the results, and finally, Section 5 summarizes and provides some concluding remarks.

## 2. Background and literature review

We organize the relevant literature review as follows. We first survey the related studies that address predictive analytics in HR and classify them along three core dimensions: functional, data and method. We then review the related topics from the HR literature.

## 2.1. Functional dimension

In recent years, several preliminary studies have focused on predicting recruiters' decisions [5,6,13–15]. However, imitating the recruiter's decision may not necessarily be the best approach, since they are often afected by highly subjective and potentially inaccurate judgments that preserve, rather than improve, hiring biases. Consequently, there is a need for an objective measure of the actual success of employee recruitment and performance, as well as providing meaningful insights to the recruiters themselves.

Other recent studies have focused on objective measures of successful recruitment based on employee past performance. Some of these studies examined the post-hire prediction of turnover or performance with predictors collected over the employment period [8,16–23]. Note that the prediction of turnover or performance using post-hire data (such as absenteeism, punctuality and performance reviews) may be useful as part of some retention activities but may lead to a late discovery of recruitment errors and may often be too late to act upon [8,24].

In contrast, the potential benefit of the early pre-hire foresight of longer-term employee success may be much higher, saving more financial and social costs. Few studies have addressed the pre-hire prediction of recruitment success using performance assessments [25–27] separately from turnover assessments [25,28].

Measuring performance may incorporate one aspect of the success of an employee; however, high-performers will not necessarily remain in the organization. Moreover, turnover alone may only partially indicate recruitment success — as often happens in practice, low-performers may not leave the organization due to organizational policies to minimize layofs and promote high internal mobility.

No previous study has referenced the combination of turnover and performance into one measure that represents an objective measure of recruitment success (see Fig. 1 for a taxonomy of the functional dimension). Thus, in this study, we focus on the case of pre-hire predictions of recruitment success using a combined measure. In the rest of this review, we focus mostly on the case of pre-hire predictions of recruitment success. Note that our methodology approaches hiring from the point of view of recruiters, as opposed to other methodologies that examine the perspective of candidates (for example, how they browse or select relevant job positions [29–31]).

![](/api/attachments/X5UZVYZ7/fulltext/images/3de74c4a7faa1090eb809f54e21ca5ff584f1092767e922f4344174498c0894b.jpg)  
Fig. 1. Literature review based on the functional dimension.

## 2.2. Data dimension

One of the challenges of using machine learning (ML) techniques in HR is the deficiency of empirical data. A noticeable number of studies have examined rather small datasets, in terms of both the number of candidates, as well as the number of features (e.g. [8,15,23,26,32]).

Within the line of studies that have addressed pre-hire prediction, studies traditionally included a rather narrow set of samples (such as [25–27]). However, in most cases, a small dataset fails to adequately portray the characteristics of the population, yielding the challenge to adequately train a reliable model based on such a small dataset. Narrow datasets often result in low support values of subpopulations, meaning that very few samples are associated with each predicted (or rulebased) subpopulation, resulting in low statistical significance. This challenge is even more noticeable with the growth in the number of features.

Some studies have also involved a limited set of features. For ex ample, Li et al. [26] and Bach et al. [27] use only psychological assessments of personality and cognitive abilities, whereas Mehta et al. [28] use resume data only. Chien and Chen [25] use only a few features, such as age, gender, marital status, educational background, work experience, and recruitment channels. Mehta et al. [28] conclude that features that capture candidate attributes, such as leadership, may contribute significantly to the analysis and that diferent models should be evaluated for diferent jobs. They indicate that a broader set of features and samples may enhance both prediction results and root cause analysis.

Lack of suficient empirical data is reflected not only in the absolute amount of data (features, candidates) but also in the available data on populations that are usually not recruited and often are not even interviewed. It is evident that to extract significant insights using the potential of machine learning techniques on HR data, data should include a range of difering applicants [33]. Hence, data collected from a large organization that promotes a wide social diversity policy and hires a wide range of heterogeneous populations would be beneficial in showing new understandings and counter-intuitive results.

In contrast to many of the abovementioned papers, in our study, we use a large dataset with hundreds of thousands of employees from a wide range of heterogeneous populations, containing > 100 features. This unique dataset allows us to extract relatively deeper rules and insights based on a wider feature set and with high significance predictions of successful or unsuccessful recruitments

## 2.3. Method dimension

Preliminary studies in HR analytics often used conventional statis tical tools such as descriptive statistics, hypothesis testing, analysis of variance, regression and correlation analysis [27,34–37]. Bollinger et al. [37] used a t-test to determine the factors that afect recruiters decisions and integrated them into their aggregated score. Then, this single-score measure was used as a correlated measure to recruiters' surveyed opinions. Samuel and Chipunza [35] used the Chi-square test to identify which post-hire employment factors impact organizational turnover. Bach et al. [27] used multiple regression analysis to test which personality traits and cognitive ability features have an impact on employee performance. However, their regression models obtain a low fit $( R ^ { 2 } = 0 . 0 5 4 , R ^ { 2 } = 0 . 0 8 8 )$

More recent studies have started to use machine learning techniques for HR analytics. Some of them have implemented models that provide interpretable insights (e.g., [19,21,25,38]) and others have implemented non-interpretable models that provide solely the predictions or their ranked scores (e.g., [8,16,28,39]; further literature is detailed in recent surveys, e.g., [18,33]). In the rest of this section, we mainly focus on papers that addressed the pre-hire prediction of recruitment success using ML tools.

Chien and Chen [25] used the CHAID decision tree to extract rules for three diferent problems with separate classification targets: employee performance levels, turnover in the first three months of employment, and turnover in the first year of employment. They extracted several rules based on the demographic data of a rather moderately sized dataset of 3825 applicants, using all data as the training set (without using validation or test set, which can lead to overfitting). They suggested implementing some strategies based on the one-time findings from the obtained decision trees, such as recruiting from firsttier universities. However, they indicate that the HR staf found the extracted rules to be dificult to implement. The researches suggest performing an in-depth analysis to further clarify the root causes of turnover and implementing processes to efectively improve orgranizational retention rate. The small dataset used in their research could be the reason for the limitations of the extracted rules.

Li et al. [26] used a support vector machine (SVM) model to predict the performance of seven test candidates using a training set of 32 employees and focused on their personality test features. Mehta et al. [28] showed the results of a random forest classifier on a dataset containing resumes of candidates. However, they did not use an interpretable model to provide recruitment insights for the organization.

It should be noted that the suggested modeling approach in this study is intended to be used by HR professionals in order to facilitate improved interaction with candidates. Thus, there is significant importance to the provision of an interpretable model that can be well comprehended by HR professionals. The model evaluation should consider the interpretability as well as the accuracy of the model [9,12].

Another challenge that the proposed approach must take into account is complexity. In the recruitment-success classification problem under consideration, the complexity arises from a large set of features in the HR dataset (with > 150 features). Each feature has several or more possible values, resulting in a large combinatorial space of potential feature interactions. Specifically, the dataset includes many categorical features, such as education certificates, test results, back ground details and potential assigned positions. In fact, extracting rules (i.e., patterns of feature values), even with a small number of features, may result in an extremely large space of potential combinations [10].

This study investigates several interpretable machine learning algorithms for predicting recruitment and placement success. The proposed method, which has not been used before for this objective, performs well in terms of both interpretability and accuracy, despite the inherent trade-of between the two [9,12]. The results of this research are expected to provide recruiters and organizations alike, with a useful modeling approach that generates insights for supporting recruitment and placement plans.

Moreover, the above reviewed studies provide local prediction scores, rankings or rules but do not provide a global prescriptive method that takes into account the position or the organizational point of view as a whole. To conclude, a prescriptive solution, rather than only a predictive methodology, is required for implementation in an actual organizational environment.

## 2.4. HR practices and HR analytics

Employees are considered one of the most important assets for modern organizations; hence, many eforts are invested in improving their success in the workplace. This has led to the rise of fields such a human resources (HR) analytics (which includes other related topics, such as “workforce analytics”, “people analytics”, and “human capital analytics” [40]). A recent review [40] maps the diferent tasks of HR practices to HR analytics tools and discusses how these tools can influence the organizational return on investment (ROI). The review shows that HR predictive analytics in workforce planning and recruitment have the highest efect on organizational ROI (similar conclusions are shown in a report by the Boston Consulting Group in [1]). Interestingly, as opposed to recruitment and workforce planning, other HR tasks, such as “industry analysis”, “job analysis” and “performance management”, have low expected ROI. Tasks such as “training”, “compensation” and “retention” have medium expected ROI [40].

These findings correspond with our approach of a pre-hire in-advance design of the recruitment plan, which is expected to have more impact than a post-hoc approach. Post-hire information includes information such as: employee engagement, organizational commitment, organizational support and HR practices applied for retention [41–44]. This information surely afects employees' success and could improve the prediction accuracy if included in the model, but it may be too late to act upon this information while inducing much higher expenses. Nevertheless, there is already much hinted evidence in pre-recruitment information that can help predict success, even before it is known how the recruited individual engages with the organization. Hence, it is highly beneficial to focus on early pre-hire predictions that have the highest efect on organizational ROI.

An additional important organizational aspect to examine is diversity. A report by McKinsey & Company shows that diversity leads to better profits and that diverse companies may outperform others [45,46]. Therefore, there are economic incentives for enhancing di versity, not solely social or legal incentives.

Literature reveals that there is some criticism with regards to the use of HR analytics for business and commercial use [47–49]. Gelbard et al. (2017) [41] state that one of the main reasons for the rather scarce adoption of HR analytics approaches among organizations is the use of “black-box" methods and a lack of actionable items. As shown in [40]. indeed, the focus of most human resources studies is mostly descriptive or predictive, and fewer are focused on prescriptive methodologies; however, a prescriptive solution can benefit organizations greatly [18]. For further information about the literature in the field of HR analytics, we refer the reader to recent reviews in [40–44].

In this paper, we aim to provide a prescriptive methodology that includes interpretable insights and an optimization tool for recruitment planning and execution. This tool can be used as a decision support tool for HR professionals, since it not only provides actionable items but also allows for the incorporation of their valuable knowledge and experience into the model.

## 3. Methods and data

The goal of this study is to develop an analytic framework that can be implemented as a decision support tool for HR recruiters in realworld settings to eficiently hire suitable candidates and place them in the organization. The proposed methodology comprises two main components: i) a local prediction scheme for the recruitments' success with a technique for extracting meaningful insights based on the trained ML model and ii) a robust mathematical model that provides a global optimization of the recruitment process, taking into account multilevel considerations.

## 3.1. Local recruitment perspective

The first phase of this study is essentially aimed at predicting the fit of an employee to a specific position he or she is hired for. In this part of the study, we focus on using machine learning models for the pre-hire prediction of recruitment success and for the extraction of interpretable insights. The recruitment success measure is based on a combination of turnover and an objective performance indicator. This approach has several advantages in comparison to traditional methods: i) the target measure is objective; ii) it takes into account both turnover and performance; and iii) it focuses on the pre-hire prediction of recruitment success.

The use of an objective target measure, as opposed to other evaluations, allows for the examination of existing recruitment policies as well as the extraction of actionable and sometimes intriguing and unexpected insights. Objective performance is afected by the circumstances leading to a position change within the organization.

For classification and prediction of successful and unsuccessful recruitments and placements, as well as for mining significant patterns, we use a Variable-Order Bayesian Network model (VOBN) proposed by Ben-Gal et al. [10] and Singer and Ben-Gal [11]. Further details on the model used and its implementation in the recruitment process can be found in Appendix A. We evaluate the model against other interpretable and non-interpretable machine learning algorithms applied to the real world recruitment dataset. We show that although the VOBN model has not been used before for the task of predicting recruitment success, it performs very well in terms of both interpretability and accuracy.

We use the trained VOBN model to identify context-based patterns that can support the organization in the recruitment process. As opposed to some black box models, the VOBN model can be used to extract rules and actions for the recruiters without any machine learning background, providing both scores and specific insights on factors and root causes that afect the success of recruitments.

In this phase, we focus on insights and interpretability (that are further discussed in Section 4 and Section 5), while in the second phase, we use the predicted probabilities for successful recruitments as inputs into a global recruitment optimization scheme that addresses more global parameters and objectives of the recruitment decisions at an organizational level.

## 3.2. Global recruitment optimization perspective

Recruitment success at an organizational level requires not only hiring the highest-potential workforce in a greedy manner but also optimizing the process to meet more general objectives. For example, a greedy allocation of candidates to jobs, such that the first candidates are allocated to the most promising job in terms of allocation success, can result in a sub-optimal situation in which certain jobs in the

Table 1

organization will be poorly allocated. Other high-level goals that could be considered are meeting the need for employees at a certain proportion, facilitating the diversity of teams, or properly balancing the workforce among diferent departments. Each of these dimensions may also include numerous viewpoints, e.g., successful recruitment from the candidate viewpoint, successful allocation from the job viewpoint, and an overall organizational regulatory viewpoint. In this section, we mainly focus on a global optimization perspective that takes into consideration multiple goals of various organizational stakeholders.

In the first phase, we pursued interpretability via extracted patterns, through which HR professionals can locally act. In this phase, however, we aim at higher prediction accuracy rather than interpretability for the purpose of designing a more global optimization strategy. To this end, the model with the best prediction results (even if non-interpretable) can be used to predict the probability of success of each candidate for each of the intended positions. These predictions can then be used to address a more global recruitment plan that controls more parameters of the recruitment decisions.

## 3.2.1. Global optimization implementation

The considered problem spans multiple dimensions, satisfying different requirements as follows: i) demand – minimizing the diference between the required workforce demand and the actual number of recruited employees; ii) accuracy – maximizing the sum of the prob abilities of the successful recruitment of employees in the organization; iii) diversity – balancing diverse groups of employees to maintain a heterogeneous work environment.

Note that when facing a recruitment challenge at an organizational level, it is important to ensure that each of the above dimensions is balanced across the various business units and positions in the organization. For example, when aiming to minimize the total number of non-filled open positions in the organization, the solution has to also account for fulfilling the demand over all the open positions in a balanced manner.

3.2.1.1. Mathematical programming formulation. We consider the global recruitment task as an optimization problem and propose a mathematical programming formulation to solve it. The proposed formulation incorporates the objectives that were described above. We use the following parameters as input for the problem: the set of candidates $E ;$ the set of positions $J ;$ the binary qualification of candidate i to position $^ { \dag , }$ represented by $q _ { i j }$ (it equals 1 if candidate i is qualified for position j and 0 otherwise); the predicted probability of candidate i to succeed in position $j ,$ denoted by $P _ { i j }$ which is the output of the learning model such as VOBN or GBM; and the number of open jobs in position j, denoted by $N _ { j } .$

Since diferent positions may have diferent values associated with successful recruitment, our formulation introduces $V _ { j }$ as an input parameter that represents the value of successful recruitment to position j, it equals 1 if all the jobs are considered evenly, or can be set propositionally to the compensation value of that position relatively to other positions. To support diversity, this formulation includes, in addition, the following input parameters: T denotes diferent types or classes of candidates (T may represent, for example, the association with diverse groups of the population); the association of candidate i to a class of type t, denoted by $b _ { i t }$ (it equals 1 if candidate i belongs to class t and 0 otherwise); and the minimal proportion of candidates of type t for position $j ,$ denoted by $P R _ { j t } .$ A summary of the notations, including the input parameters, the indices, and the model's decision variables, is presented in Table 1. Additionally, we use a more simplified and less constrained formulation for benchmark purposes.

The first formulation (Formulation 1) is used for benchmark purposes and is a rather simple adjustment to the assignment problem [50], in which the objective function (1.1) maximizes the sum of the predicted probabilities of assignments. Constraint set (1.2) ensures that no candidate is recruited to more than one position. Constraint set (1.3)

Formulation notations.

<table><tr><td colspan="2">Input parameters</td></tr><tr><td> $E$ </td><td>The set of candidates,  $i \in 1, \ldots |E|$ </td></tr><tr><td> $J$ </td><td>The set of open positions (jobs),  $j \in 1, \ldots |J|$ </td></tr><tr><td> $q_{ij}$ </td><td>Equals 1 if candidate  $i$  is qualified for position  $j$ , 0 otherwise</td></tr><tr><td> $P_{ij}$ </td><td>Probability for candidate  $i$  to succeed in position  $j$ </td></tr><tr><td> $N_j$ </td><td>Number of open jobs in position  $j$ </td></tr><tr><td> $V_j$ </td><td>Value of a successful recruitment to position  $j$ </td></tr><tr><td> $T$ </td><td>Set of candidate class types,  $t \in 1, \ldots |T|$ </td></tr><tr><td> $b_{it}$ </td><td>Equals 1 if candidate  $i$  belongs to class  $t$ , 0 otherwise</td></tr><tr><td> $PR_{jt}$ </td><td>Required proportion of workers of class  $t$  in position  $j$ </td></tr><tr><td> $B$ </td><td>A parameter that balances accuracy and demand objectives</td></tr><tr><td colspan="2">Indices</td></tr><tr><td> $i$ </td><td>Candidate</td></tr><tr><td> $j$ </td><td>Position</td></tr><tr><td> $t$ </td><td>Class types of candidates</td></tr><tr><td colspan="2">Decision variables</td></tr><tr><td> $X_{ij}$ </td><td>Recruitment of candidate  $i$  to position  $j$ </td></tr><tr><td> $Y_j$ </td><td>The difference between required and recruited employees for position  $j$ </td></tr><tr><td> $Y_{max}$ </td><td>Maximum allowed difference between required and recruited employees</td></tr><tr><td> $Z_{jt}$ </td><td>Number of candidates of type  $t$  recruited to position  $j$ </td></tr></table>

requires that the number of recruitments for position j will not exceed $N _ { j } .$ Constraint set (1.4) ensures that only qualified candidates are recruited for positions. The next set of constraints (1.5) limits the set of possible values for $X _ { i j }$ (whether to assign candidate i to position j) to 0 or 1.

Formulation 1. A simple linear programming based on the classic assignment problem solution.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
(1.1)  $\max(\Sigma_{i,j}[P_{ij}X_{ij}])$ 
Subject to the constraints
(1.2)  $\Sigma_{j}X_{ij} \leq 1$ ,  $\forall i \in E$ 
(1.3)  $\Sigma_{i}X_{ij} \leq N_{j}$ ,  $\forall j \in J$ 
(1.4)  $X_{ij} \leq q_{ij}$ ,  $\forall i \in E, j \in J$ 
(1.5)  $X_{ij} \in \{0,1\}$ ,  $\forall i \in E, j \in J$
</div>

Formulation 1 raises several challenges that we wish to address. For example, positions that have a very low probability of succeeding might not receive any recruitments (hence, not considering the positional point of view of our demand requirement). Another challenge is that employees might not be evenly distributed among positions. In Formulation 2 below, we propose one way to address these requirements by adding a cost to the deviation from the recruitment demand (can be proportional to the loss due to this position staying unfulfilled).

Formulation 2 introduces the decision variable $Y _ { j } ,$ which represents the diference between the required and recruited employees to the position while $Y _ { m a x } ,$ is set the maximal allowed position shortage (constraints sets (2.5) and (2.6)). Accordingly, we then modify the objective function (2.1) to penalize the maximum deviation from the number of open positions (B $Y _ { m a x } )$ , where B is a parameter that balances accuracy and demand objectives.

Hence, this penalty approach leads to a better distribution of the employee shortage among positions. Note that we choose to use the demand as a “soft” constraint and penalize shortages in the objective function, rather than forcing a specific level of demand satisfaction. This enables a larger feasible solution space and allows for achieving higher demand satisfaction by minimizing shortages in the objective function.

Formulation 2 also introduces diversity constraints into the model.

Table 2  
Dimensions addressed by Formulations 1 and 2.

<table><tr><td>Dimension view</td><td>Demand</td><td>Accuracy</td><td>Diversity</td></tr><tr><td>Position</td><td> $\sqrt{\text{(Formulations 2)}}$ </td><td></td><td> $\sqrt{\text{(Formulation 2)}}$ </td></tr><tr><td>Organization - total value</td><td> $\sqrt{\text{(Formulations 1, 2)}}$ </td><td> $\sqrt{\text{(Formulations 1, 2)}}$ </td><td> $\sqrt{\text{(Formulation 2)}}$ </td></tr><tr><td>Organization - balance across business units</td><td> $\sqrt{\text{(Formulation 2)}}$ </td><td></td><td> $\sqrt{\text{(Formulation 2)}}$ </td></tr></table>

Constraints (2.7) require that $Z _ { j t }$ will determine the number of candi dates of type t that are assigned to position j. Constraints (2.8) require that the proportion of candidates of type t assigned to position j will be at least $P R _ { j t } .$ Table 2 presents the requirements that both Formulations 1 and 2 address in terms of the dimensions and viewpoints presented above.

Formulation 2. Proposed linear programming with diversity and penalty on maximal position shortage.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
(2.1)  $\max(\Sigma_{i,j}[V_{j}P_{ij}X_{ij}] - B\cdot Y_{max})$ 

Subject to the constraints

(2.2)  $\Sigma_{j}X_{ij} \leq 1$ ,  $\forall i \in E$ 

(2.3)  $\Sigma_{i}X_{ij} \leq N_{j}$ ,  $\forall j \in J$ 

(2.4)  $X_{ij} \leq q_{ij}$ ,  $\forall i \in E, \forall j \in J$ 

(2.5)  $Y_{j} = N_{j} - \Sigma_{i}X_{ij}$ ,  $\forall j \in J$ 

(2.6)  $Y_{max} \geq Y_{j}$ ,  $\forall j \in J$ 

(2.7)  $Z_{jt} = \Sigma_{i}X_{ij}b_{it}$ ,  $\forall j \in J, t \in T$ 

(2.8)  $Z_{jt} \geq PR_{jt}\Sigma_{i}X_{ij}$ ,  $\forall j \in J, t \in T_{protected}$ 

(2.9)  $X_{ij} \in \{0,1\}, Z_{jt} \in \{0,1\}$ ,  $\forall i \in E, j \in J, t \in T$ 

(2.10)  $Y_{j} \in Integer$ ,  $\forall j \in J$
</div>

## 3.2.2. Motivating and illustrative example

We first solve the model over a sample of the real-world dataset as a motivating and illustrative example. We then continue to implement the solution using a larger real-world dataset and perform an analysis of the trade-of between the objectives, as shown in Section 4.4. As a first step, we use small sample data from the real-world dataset to illustrate the properties of the formulations. The data for the example are shown in Fig. 2. It includes four positions (columns), sixteen candidates (rows), two types of candidates that need to be balanced (e.g., based on their background), and the predicted success probability for each pair of candidate and position (shades of green represent high probability and shades of red represent low probabilities). In addition, we assume a demand of 6 employees for each position.

For example, it is clear from the table that if the only objective is to maximize the sum of success probabilities of candidates for each position separately, position 379 will be filled by candidates from the group of type 2 only.

Fig. 3 illustrates four diferent solutions to the problem: (1) solution to Formulation 1, (2) solution to Formulation 2 with PR = 0, (3) solution to Formulation 2 with $\mathrm { P R } = 0 . 1$ , and (4) solution to Formulation 2 with PR = 0.3. The rows represent the diferent candidates, and the columns represent the positions. Within each position, an assignment of a candidate to that position is marked with color. Table 3 shows several aggregated properties of the diferent solutions.

We observe the following: i) Accuracy: the predicted success prob ability decreases with more constrained models (i.e., models with more constraints) as a result of the shift from global to local objectives; ii) Demand: (1) formulations that penalize deviation from the required demand (Solutions 2–4) avoid cases of positions in shortage of assign ments, and (2) solutions that incorporate the penalty on the maximum shortage (Solutions 2–4) manage to better balance the demand satisfaction among positions; and iii) Diversity: (1) adding diversification constraints to the formulations (Solutions 3 and 4) results in higher diversity without significantly compromising accuracy, and (2) solutions that impose a high diversity requirement (Solution 4) may result in higher demand shortage. Similar results are expected over larger recruitment experiment.

## 3.3. Dataset description and target definition

The input dataset for this research includes hundreds of thousands of employment cases (approximately 700,000 cases) of employees who were recruited to the organization over the span of a decade (hired between the years 2000–2010). The pre-hire features in the dataset include age, gender, family and marital status, residence, nationality details, background record, education and grades, interviews and test scores (including leadership scores and language scores), professional preferences questionnaires, family details (when available), “lifestyle” data (when available), and details about the positions. Table 4 presents the main categories of the 164 features in the dataset.

In the preprocessing phase, 21 data tables were consolidated to mask sensitive private data and personal identification; on this dataset we also performed feature enrichment processes and addressed missing data and outliers. Specifically, in the feature enrichment process, we identified several interesting hierarchies of position groups and background data. In addition, we used residence-related data to deduce the socioeconomic levels of the candidates, using statistical data from the Central Bureau of Statistics. Missing values were tagged in the dataset by zeros, since these values mainly represented a lack of a specific test result or interview attribute. The reason to avoid a certain test or question for a specific candidate was not random nor uniform but rather based on the candidate's profile. For example, candidates who seemed to be less relevant to a specific job type were not asked to complete a related questionnaire or did not go through a specific interview segment. As such, these zeros indicate a specific categorical decision, which could be overlooked had we used the mean values (e.g., the mean of the results of certain tests, to impute them). The data records of candidates with many missing values were removed entirely; however, only < 1% of the records were removed in total. Additional dimensionality reduction procedures were performed in accordance with each of the applied machine learning algorithms (see details in Section 4).

The class feature definition for successful and unsuccessful recruitments was conducted by utilizing the following process: based on HR department records, the reasons for employee turnover were analyzed and accordingly divided into two groups: successful recruitments (e.g., the employee left for “natural” reasons, such as leaving the job after a suficient time period) and unsuccessful recruitments (e.g., job termination after a short amount of time or due to poor performance). Position and placement changes were classified as negative (e.g., “misfit”) or positive (e.g. “promotion” or “job enrichment processes”).

To conclude, the combination of turnover and position changes was used as a combined measure for labeling successful vs. unsuccessful recruitments, as seen in Table 5. To clarify, the fifth row in the table represents instances that were excluded from the analysis as their period of employment was not long enough to determine if they were successful or not. To maintain consistency, the a-priori distributions of the target class in both the training and testing datasets include 30% of the unsuccessful recruits and 70% of the successful recruitments.

Recall that the dataset was acquired from a large nonprofit service organization that is highly diversified over roles, accountabilities and job descriptions with a heterogeneous population. These characteristics allow for testing potentially biased recruitment policies and decisions that traditionally may not be tested due to the absence of suficient data on certain groups or lack of information on different personal proper ties. Specifically, it enables us to focus on various groups in the population and to show some counter-intuitive understandings based on data, which is not commonly available.

<table><tr><td>Candidate type</td><td>Candidate ID</td><td>Position 1409</td><td>Position 1509</td><td>Position 379</td><td>Position 40</td></tr><tr><td rowspan="7">type 1</td><td>Candidate 7317</td><td>0.67</td><td>0.68</td><td>0.68</td><td>0.48</td></tr><tr><td>Candidate 8320</td><td>0.47</td><td>0.68</td><td>0.48</td><td>0.56</td></tr><tr><td>Candidate 9346</td><td>0.53</td><td>0.68</td><td>0.39</td><td>0.56</td></tr><tr><td>Candidate 3145</td><td>0.61</td><td>0.68</td><td>0.51</td><td>0.55</td></tr><tr><td>Candidate 5438</td><td>0.63</td><td>0.68</td><td>0.48</td><td>0.57</td></tr><tr><td>Candidate 0142</td><td>0.67</td><td>0.68</td><td>0.51</td><td>0.51</td></tr><tr><td>Candidate 1617</td><td>0.55</td><td>0.68</td><td>0.45</td><td>0.55</td></tr><tr><td rowspan="9">type 2</td><td>Candidate 8610</td><td>0.66</td><td>0.68</td><td>0.85</td><td>0.58</td></tr><tr><td>Candidate 2939</td><td>0.48</td><td>0.68</td><td>0.85</td><td>0.60</td></tr><tr><td>Candidate 4349</td><td>0.56</td><td>0.73</td><td>0.85</td><td>0.60</td></tr><tr><td>Candidate 4842</td><td>0.69</td><td>0.68</td><td>0.85</td><td>0.55</td></tr><tr><td>Candidate 7983</td><td>0.69</td><td>0.58</td><td>0.86</td><td>0.59</td></tr><tr><td>Candidate 6405</td><td>0.64</td><td>0.68</td><td>0.86</td><td>0.59</td></tr><tr><td>Candidate 7882</td><td>0.59</td><td>0.62</td><td>0.86</td><td>0.48</td></tr><tr><td>Candidate 5481</td><td>0.84</td><td>0.68</td><td>0.85</td><td>0.54</td></tr><tr><td>Candidate 0226</td><td>0.62</td><td>0.69</td><td>0.83</td><td>0.54</td></tr></table>

Fig. 2. Predicted probabilities of success of assigning sixteen candidates of two types of populations to four positions. The entries are color-coded by the succes probability values, green - high probability, red - low probability. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

With respect to data selection, we aimed to focus on early pre-hire predictions; thus, the features that were integrated as predictors in the model included only the available pre-hire data, i.e., data from before the recruitment day. The motivation for such data selection was based on several reasons. First, the recruitment day is an important decision point in which it is easier for the organization to take action —for example, the early identification of a possible misfit may save a great deal of financial and social costs. Second, such data selection enables the identification of actionable recommendations for preventive actions. For example, there is little interest in the revelation of turnover among employees who were absent for a long period of time immediately before they resigned (these causes are obvious and self-evident and also occur too late to be acted upon).

Note that although post-hire data was available (i.e., data about each employee through his employment period), we utilize only the pre-recruitment data. This approach allows us to achieve the goal of improving the recruitment process and providing insights that may be integrated within recruitment decision processes.

![](/api/attachments/X5UZVYZ7/fulltext/images/493d41ed825238d5482cc7fe59d30128e35b5351e310b5c8b96b59f0e5815e54.jpg)  
Fig. 3. Assignment of candidates to positions by four diferent solutions. For example, solution 1 (marked in red) suggests the following: i) recruiting 4 candidates to position 1409; ii) recruiting 6 candidates to position 1509; iii) recruiting 6 candidates to position 379 (note that none of them are of type 1); and iy) not recruiting any of the candidates to position 40 (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.).

Table 3  
Illustrative example results. Entropy is used as a suitable measure for diversity in the case of more than two candidate type.

<table><tr><td rowspan="2">Solution #</td><td rowspan="2">Description</td><td colspan="2">Demand</td><td colspan="2">Diversity</td><td rowspan="2">Average success probability</td></tr><tr><td># of completely unassigned positions</td><td> $Y_{max}$ (maximal position shortage)</td><td>Minimum proportion of type 1 population</td><td>Average position entropy</td></tr><tr><td>1</td><td>Formulation 1</td><td>1</td><td>6</td><td>0</td><td>0.413</td><td>0.756</td></tr><tr><td>2</td><td>Formulation 2 with PR = 0</td><td>0</td><td>2</td><td>0</td><td>0.703</td><td>0.711</td></tr><tr><td>3</td><td>Formulation 2 with PR = 0.1</td><td>0</td><td>2</td><td>0.25</td><td>0.858</td><td>0.701</td></tr><tr><td>4</td><td>Formulation 2 with PR = 0.3</td><td>0</td><td>3</td><td>0.33</td><td>0.939</td><td>0.667</td></tr></table>

## 3.4. Prediction model and evaluation measure

The classification algorithms were trained on 70% of the candidates (first 8 years in the dataset). In the test stage, we used the trained classification models to predict the recruitment success of the remaining 30% of the candidates and validate our predictions with the ground truth. Note that we used time-dependent partitioning for training and testing to reassure the applicability of the model in the real world and show that the model can still be valid even when the organization changes.

In this process, we examined five interpretable machine learning algorithms and four non-interpretable algorithms. We evaluated the results of the prediction models by relying on the AUC (area under ROC curve) measure. According to the literature, e.g., Chawla [51], when the dataset is imbalanced (e.g., when the target variable includes large diferences between the frequencies of diferent class values), an appropriate performance measure is the ROC curve and the AUC measure.

## 4. Results

## 4.1. Model evaluation

The study results are presented in Table 6 below. Comparing various interpretable and non-interpretable models, the best AUC score obtained by an interpretable model was obtained using the VOBN algorithm [10,11], with an $\mathsf { A U C } = 0 . 7 0 5$ on the test set. The best results by a non-interpretable model, were obtained by the gradient boosting machine (GBM) algorithm with an $\mathsf { A U C } = 0 . 7 3$ . Thus, for interpretability purposes, we suggest selecting the VOBN model, whereas for solely aiming at prediction, we suggest using the GBM model.

A conventional approach to handle multiple (conflicting) objectives is to use a Pareto-optimality approach [52]. The model's AUC and its interpretability can be considered as two conflicting objectives that should be addressed by a Pareto-optimality approach. In this sense, the VOBN and the GBM algorithms are both “Pareto optimal”. Specifically, the GBM should be selected if the objective is mainly prediction (although non-interpretable), while the VOBN model should be prioritized if the model interpretability is important, despite a relatively small decrease in the AUC score. Such interpretability not only enhances the understanding of key features in the prediction model but also provides root cause analysis and insights into the recruitment process. Following the evaluation of the diferent models, the VOBN and GBM models were used for further experimentation and analysis — the former for iden tifying interpretable patterns and the latter for a global optimization approach.

## 4.2. Identified patterns

Patterns in this use case can be thought of as regularities in the dataset that characterize subpopulations of candidates with common characteristics. A pattern is often described by a set of rules that can be used to cluster subpopulations into diferent categories. The VOBN, as an interpretable descriptive model, enables the extraction of patterns that can be mapped into insights for the recruitment process, as seen in the next example. The VOBN model has generated more than a thousand patterns that went through a filtering process based on the following: their statistical validity (i.e., statistical significance and support set that indicates how many cases they refer to) and the change they imply on the recruitment's success probability with respect to other subpopulations. The final set of implemented patterns contained few dozens of patterns (a number that also depends on the ability of the recruiters to implement it in their routine procedures), including the ones used by the HR department and the ones presented in the next examples. These patterns were selected by a prioritization process that included the following steps: i) selecting patterns that contain at least one variable that can be controlled by the HR department, such as a threshold on a test result (otherwise the pattern is non-actionable); ii) selecting patterns in which the controlled variables separates well the population into subgroups resulting in diferent success probability outcomes; iii) prioritizing patterns that represent “counter-intuitive” phenomena that were not known to the recruiters; and iv) prioritizing patterns with larger number of instances in the leaves and with a larger turnover percentage.

The following are several examples of patterns, some of which are counter-intuitive and were extracted from the data by the VOBN algorithm.

Example 1. Correlation of a high analytical score in a pre-placement test with the dropout rate in a specific administrator position over diferent subpopulations.

As shown in Fig. 4, an interesting pattern is found related to the correlation of a high analytical score in a pre-placement test on the position dropout rate of certain administrator positions. As seen in the left figure, the position dropout rate falls only slightly (from 42.5% to 39.3%) when the candidate obtains a higher analytical score. However, as seen from the pattern in the right figure, for men with low leadership skills scores and low language scores, the dropout rate increases significantly (from 58.1% to 68.3%, with p-value < 0.001) if the candidate has a high analytical score. A possible explanation can be related to the fact that a high analytical ability has an over-qualifying efect on these specific candidates.

Skowronski [53] reviews the connections between over-qualification and turnover as well as performance. The paper proposes several practices for the pre-hire and post-hire management of overqualified emplovees and suggests considering perceived over-qualification rather than merely objective over-qualification. In the case of the considered pattern, it is likely for an employee to feel overqualified and less motivated if he or she is highly skilled but not able to demonstrate his or her competence due to language and communication gaps.

To overcome the above dificulties, recruiters should investigate which jobs' properties might decrease the probability of successful recruitment and adjust the specific job requirements to accommodate for wider populations of employees. They may also devise unique programs for diferent populations that includes for example language, communication and technical training.

Table 4  
Feature summary (after data preparation procedures).

<table><tr><td>Feature cluster</td><td>Lifestyle</td><td>Family</td><td>Interview and test scores</td><td>Special interview scores</td><td>Education</td><td>Position</td><td>Nationality</td><td>Language</td><td>Residence</td><td>Culture</td><td>Background record</td><td>Gender</td><td>Age</td></tr><tr><td># of Features</td><td>62</td><td>30</td><td>29</td><td>14</td><td>7</td><td>5</td><td>5</td><td>5</td><td>2</td><td>2</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Avg. rank by GBM importance</td><td>12</td><td>11</td><td>2</td><td>9</td><td>3</td><td>1</td><td>7</td><td>8</td><td>5</td><td>6</td><td>4</td><td>10</td><td>13</td></tr></table>

Example 2. The efect of competencies on the position dropout rate for a specific field-support position.

In general, the data show that candidates with high competencies are less likely to leave their position than are candidates with low competencies (15% vs. 30% position dropout rate, respectively, with pvalue < 0.001). However, for specific field-support positions, this efect is reversed. Fig. 5 illustrates how candidates for specific support positions who have high competencies follow a significantly higher position dropout rate than do candidates with low competencies (43% vs. 21% position dropout rate, respectively, with p-value < 0.001). Here, the recruiters should again be aware of the reversed relation in the case of

this field-support position.

This considered pattern also shows that the dropout rate for lowcompetency employees has decreased when they are assigned to a specific support position. This is somewhat unexpected since it implies that an organization should strive for the heterogeneity and diversity of its employees rather than recruiting only the most highly scored individuals. This notion is also supported in a report by McKinsey & Company that interestingly showed that diversity leads to better profits among organizations [45,46]. Let us note again that this output is due to the analysis of a unique dataset of a large nonprofit service organi zation that hires diverse populations with diferent backgrounds and skills.

Example 3. Correlation between low personal interview scores and low management skill levels with position dropout rates in specific business units for male candidates.

Table 5  
Target definitions by HR department.

<table><tr><td>Employment status</td><td>Completed expected time in position (Position dependent)</td><td>Reason for leaving</td><td>HR term</td><td>Target feature label</td></tr><tr><td>Left the organization</td><td>Yes</td><td>“Natural” reasons</td><td>Turnover</td><td>Successful recruitment</td></tr><tr><td>Left the organization</td><td>Yes</td><td>Negative reasons</td><td>Turnover</td><td>Unsuccessful recruitment</td></tr><tr><td>Left the organization</td><td>No</td><td>Negative reasons</td><td>Turnover</td><td>Unsuccessful recruitment</td></tr><tr><td>Employed in the organization</td><td>Yes</td><td>-</td><td>Retention</td><td>Successful recruitment</td></tr><tr><td>Employed in the organization</td><td>No</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Employed in the organization</td><td>No</td><td>Promotion or job enrichment</td><td>Position change - promotion</td><td>Successful recruitment</td></tr><tr><td>Employed in the organization</td><td>No</td><td>Negative reasons</td><td>Position change demotion</td><td>Unsuccessful recruitment</td></tr></table>

## Table 6

Evaluation of models.<sup>a</sup>

<table><tr><td rowspan="2"></td><td rowspan="2"> $Explainability/interpretability^b$ </td><td rowspan="2">AUC results over all test samples</td><td colspan="2">AUC results by each  $position^c$ </td></tr><tr><td>Number of positions with AUC &gt; 0.7d</td><td>Average rank over all positions (1 - highest)e</td></tr><tr><td>GBM (gradient boosting)</td><td>No</td><td>0.730</td><td>174</td><td>3.07</td></tr><tr><td>RF (random forest)</td><td>No</td><td>0.719</td><td>164</td><td>3.39</td></tr><tr><td>VOBN (variable-order Bayesian networks)</td><td>Yes</td><td>0.705</td><td>145</td><td>3.78</td></tr><tr><td>LR (logistic regression)</td><td>Partial</td><td>0.700</td><td>129</td><td>4.30</td></tr><tr><td>SVM (support vector machine)</td><td>No</td><td>0.697</td><td>100</td><td>5.16</td></tr><tr><td>C45 (J48)</td><td>Yes</td><td>0.682</td><td>103</td><td>5.37</td></tr><tr><td>CHAID</td><td>Yes</td><td>0.681</td><td>105</td><td>5.12</td></tr><tr><td>Naive Bayes</td><td>Yes</td><td>0.677</td><td>80</td><td>5.81</td></tr><tr><td>CART</td><td>Yes</td><td>0.644</td><td>7</td><td>7.92</td></tr></table>

<sup>a</sup> Note that both the RF and GBM models and their implementations are generally robust to noisy and high dimensionality datasets, since they base their decisions on multiple permutations of the dataset (see [56,66–69]). For the logistic regression and decision tree models, we implemented a feature selection preprocess by using information gain analysis (see [70]). For the SVM model, we used the built-in model as implemented in [71], that can deal with high dimensionality by testing diferent subsets of the data. In the VOBN model, there is a built-in preprocess procedure that uses mutual information to identify the high-impact features (see the Appendix A for further details)

![](/api/attachments/X5UZVYZ7/fulltext/images/334365d6063fedc039bf10049bbcda3aab0c75c6560f79f58ca08d3c2ce370b6.jpg)  
Fig. 4. High analytical score efect on administrator position dropout rate over various subpopulations.

![](/api/attachments/X5UZVYZ7/fulltext/images/9d756f9b702f75a16860875a5267407c4df99ab7cc20aa4c3f0e3346910e70c0.jpg)  
Fig. 5. The efect of competencies on the position dropout rate for all positions and for a specific field support position.

The pattern under consideration shows that the efect on the posi tion dropout rate for male candidates with low scores in a specific section in the personal interview, combined with low management skills score, is business-unit dependent, as shown in Fig. 6. For males, these low scores are associated with a position dropout rate of 37%, compared to an average dropout rate of 29% for all male candidates. However, this observation changes significantly among diferent busi ness units, as seen in the figure.

In business unit A, the position dropout rate for all males is 39% (1928 out of 4916), while candidates with low scores have a considerably higher position dropout rate of 60% (394 out of 662). In business unit B, the opposite efect is observed: the dropout rate for male candidates with low scores is 23% (4113 out of 17,600), which is slightly lower than the rate for males, with an average score of 26% (7648 out of 29,049). All these diferences have p-values lower than 0.001.

As mentioned above, these findings support previous observations in the literature that call for the diversification and heterogeneity of workers [45,46]. Moreover, these findings emphasize the advantage of using data-driven methods to allocate people with diversified backgrounds and skills to specific positions (involving complex hidden patterns, related in this example to gender, business units, managerial and personal skills as well as specific test scores), in which they have a higher potential for success and good performance. Using the proposed approach, organizations should detect the characteristics of specific positions that are found to be statistically related to the allocation success of candidates from various backgrounds. These recruitment and allocation insights should be implemented accordingly, as long as they follow the required regulations for transparency, fairness and explainability (e.g., see GDPR: The EU's General Data Protection Regulation).

Example 4. Cultural background efect on position dropout for a specific ofice administrative position.

The model identified a unique pattern that is related to a specific administrative ofice position. It turns out that for this ofice position, allocating a subpopulation of people with a specific common background results in a significantly lower dropout rate (23% instead of 44%, with p-value < 0.001).

![](/api/attachments/X5UZVYZ7/fulltext/images/1de4570965b3af968c4c6912f4d1389f68243b51913d87ddcd6c8d40927a43d2.jpg)  
Fig. 6. The relationship between poor-skill levels and position dropout rates for male candidates in diferent business units.

![](/api/attachments/X5UZVYZ7/fulltext/images/557e1126c121fbbc1857273439b489279b9b4cc913eaa2d68ce5f6c5ac04b533.jpg)  
Fig. 7. The potential efect of the candidates' cultural background (A or B) on the dropout rate for all positions and for a specific administrative ofice position

Note that without a granular pattern-detection model, such as the one proposed here, it would be extremely dificult to identify such significant correlations between this ofice position and the specific cultural background. As seen in Fig. 7, the average efect of the cultural background over all the positions is minor (indicating a 5% difference only). However, for this considered administrative ofice position, the efect on the dropout rate is marginal, i.e., more than four times greater (a 21% difference).

Organizations and researchers should investigate why some sub populations of candidates who share common characteristics outperform or underperform in specific jobs or scenarios. Accordingly, they should find more opportunities to include (rather than exclude) specific populations as well as to adjust other organizational practices to support successful recruitment, considering the data-driven patterns discovered. In this context, it worth noting that the literature already recognized, for example, that some subpopulations of immigrants who share common cultural assets and social norms are sometimes bette equipped than others to succeed in specific scenarios and vice versa (see [53,54]).

![](/api/attachments/X5UZVYZ7/fulltext/images/fa035569be758b44f1617582f5c8c98f7589c99c2438d26774957d645847a742.jpg)  
Fig. 8. The efect of the oral language score on turnover changes for specific subpopulations of candidates.

Example 5. The efect of oral language score on turnover difers by specific subpopulation.

The efect of an oral language score on turnover is heavily depen dent on the chosen subpopulation. Fig. 8 shows that when analyzing this factor over all the employees in the organization, the turnover rate associated with a low oral language score results in a significantly higher position dropout rate (31% vs. 9%, with p-value < 0.001) and thus a lift of 3.2. However, when considering a subpopulation of women in administrative positions from a specific cultural background and a certain educational path, the turnover lift grows approximately to 15.5 (77% vs. 5%, with p-value < 0.001). This pattern addresses a rather privileged group of women according to their cultural and educational background, and although expected to succeed in their placement (with a 6% turnover only), there is a noticeable language deficiency that af fects their ability to succeed in specific jobs.

It is interesting to compare the relative contribution of features when considering a large population to that of a specific subpopulation. Note that the feature importance of language according to Table 4 is relatively low; however, for a specific subpopulation, there is a greater impact of language skills. This notion is also closely related to Simpson's Paradox [55], which shows that an observed trend in subgroups may behave quite diferently (even reversely) when these subgroups are aggregated and analyzed together.

## 4.3. Results application

When recruiters are looking for candidates to be placed in certain positions, they can take advantage of many patterns, such as those shown above. First, they can check that all the relevant data being used by the algorithm are collected and analyzed for all candidates. In ad dition, they can decide to send some of the candidates to undergo additional testing shown to be informatively correlated with the dropout rates. Then, they can apply the obtained patterns that were discovered by the algorithm to improve the recruitment and placement processes.

Finally, the obtained patterns can be used to reveal insights about factors that contribute to the recruitment success of specific positions. This in turn can provide feedback to the organization and can be used to adjust the position definition, such that it increases employment satisfaction and the overall recruitment success probability.

It is important to note that these insights must be considered in the proper ethical and legal contexts following specific regulations (e.g., GDPR). Organizations should investigate the reasons as to why some candidates underperform under certain scenarios and find opportunities to include, rather than exclude, diverse populations while adjusting organizational practices when the discovered patterns are considered. In the next section, we discuss a proposed global optimization formulation that can be used to enhance diversity in the organization while maintaining high success placement rates.

## 4.4. Data-driven global optimization results

In this section, we show an analysis of the proposed global optimization model. The analysis incorporates the data of real candidates, positions and demand and includes the predicted success probabilities derived from the prediction for a yearly planning program of our organization. We then perform a sensitivity analysis of the results and compare them to the recruiters' actual decisions.

The best prediction was obtained using the GBM algorithm [56], with AUC = 0.73 (see Table 6). We analyzed the robustness of the model by using diferent time-based partitions for training and testing and noted that the AUC value remained stable. Let us note that the results may be improved using post-hire data; however, as mentioned above, in this study, we focus on recruitment, as performing a predic tion in a later post-hire phase may be too late to act upon, leading to much higher expenses.

Table 7  
Results for a yearly plan.

<table><tr><td rowspan="2">#</td><td colspan="2">Method</td><td colspan="2">Accuracy</td><td colspan="3">Diversity</td></tr><tr><td>Solution</td><td>Diversity requirement (PR)</td><td>Average of Predicted success probability</td><td>Standard deviation over the mean probabilities of all positions</td><td>Minimum proportion of type 1 population</td><td>Average position entropy</td><td>Mean difference in accuracy between candidate groups</td></tr><tr><td>1.1</td><td>Actual selection</td><td>-</td><td>0.7087</td><td>0.1602</td><td>0</td><td>0.718</td><td>9.67%</td></tr><tr><td>2.1</td><td>Formulation 2</td><td>0</td><td>0.7654</td><td>0.1434</td><td>0.0057</td><td>0.619</td><td>7.43%</td></tr><tr><td>2.2</td><td>Formulation 2</td><td>0.1</td><td>0.7653</td><td>0.1431</td><td>0.1003</td><td>0.653</td><td>7.33%</td></tr><tr><td>2.3</td><td>Formulation 2</td><td>0.2</td><td>0.7648</td><td>0.1427</td><td>0.2</td><td>0.700</td><td>6.07%</td></tr><tr><td>2.4</td><td>Formulation 2</td><td>0.3</td><td>0.7638</td><td>0.1422</td><td>0.3005</td><td>0.780</td><td>4.86%</td></tr><tr><td>2.5</td><td>Formulation 2</td><td>0.4</td><td>0.7623</td><td>0.1414</td><td>0.4</td><td>0.810</td><td>3.69%</td></tr><tr><td>2.6</td><td>Formulation 2</td><td>0.5</td><td>0.7607</td><td>0.1407</td><td>0.5</td><td>0.864</td><td>2.33%</td></tr></table>

![](/api/attachments/X5UZVYZ7/fulltext/images/ba3155a62b3d2aa3353042f26c476726c1e508bc13ac57649cb6d27860417f12.jpg)  
Fig. 9. Pareto eficiency for a yearly plan of the real-world scenario.

The problem includes 30 position-types and all the candidates recruited to these position-types during a period of one year (10,329 candidates). As in the previous section, we compared diferent for mulations of the problem to the actual assignment of the recruiters in the organization (see Table 7 and Fig. 9) and analyzed the trade-ofs between diferent objectives. We expect to have similar results and to be able to show an improvement (in terms of both accuracy and di versity) compared to the actual allocation that was performed by the recruiters.

The results above indicate the following<sup>1</sup>:

• We expect that more complicated diversity requirements will lead to a reduced predicted probability of success. However, it can be observed that in the suggested formulations (Solutions 2.4–2.6 in Table 7), there was a significant improvement in both objectives in comparison to the actual assignment.

• Interestingly, requiring diversity at the position level also con tributes to the organizational level:

o Average entropy - measuring individual positional diversity (the higher it is, the better).

o Mean diference - measuring balanced scoring between candidate groups (the lower it is, the better).

o Standard deviation of average probabilities for positions - measuring balanced average scoring between positions (the lower the standard deviation is, the higher the balance between positions).

To combine the local and global procedures, it is possible to integrate additional limitations or preferences in the model that were induced from interpretable insights or from other sources, such as legal or regulatory requirements. One approach for doing so is to incorporate additional constraints to the model. Another possible approach is to indicate entries in the probability matrix, such as in the Big M Method [57]. For a future study, we suggest devising a model that will explicitly require the reduction of the imbalance between positions.

## 4.4.1. Arc deletion heuristic

We note that a more demanding and complex diversity requirement entails longer runtime, which ranges from a few minutes for PR = 0 to 51 min with $\mathrm { P R } = 0 . 1$ up to several hours with a higher diversity requirement. However, the bottom line is that the size of a relevant assignment problem, even for a large organization with thousands of workers, is fully feasible with the proposed approach (specifically with the suggested heuristic described below).

In order to reduce the computational complexity of the model, we suggest a simple heuristic for the deletion of arcs. The heuristic deletes arcs that have a predicted success probability under a certain threshold (in our experimentation we use a threshold of $\mathrm { P _ { i j } } < 0 . 4 5 )$ . We found that such a deletion allows one to reduce computational complexity while having only a minor efect on the obtained accuracy. In particular, after introducing arc deletion, the observed gaps to the best solution (without an arc deletion) were at most 1% but resulted in runtimes shorter by half or less with respect to the original runtimes. Note that deleting arcs, although improving runtimes, may compromise demand satisfaction in cases in which there are many candidates with an allocation probability which is lower than the threshold, for a certain position.

## 5. Conclusions

The objective of this study is to develop a hybrid decision support tool for HR professionals in the operations of recruitment and placement. The proposed methodology consists of two main components. The first is the definition of the problem as a machine learning problem with objective recruitment success as the target variable for specific candidate-position recruitments. The second is the development of a method based on mathematical modeling, which provides a global prescriptive hiring policy at an organizational level rather than a local one.

In the first phase, the machine learning model predicts the probabilities of successful recruitments and placements by taking into account various turnover scenarios and pre-recruitment data. The proposed approach is objective, based on an integrated performance indicator as opposed to some other evaluation schemes from the HR literature. It allows for an examination of current recruitment policies and the extraction of interpretable and actionable pattern-based in sights.

In the second phase, the methodology considers the multi-stakeholder environment of the recruitment problem, including multisided balance and diversity in the process. We show that using the proposed mathematical programming model, even with the requirements of balanced demand and diversity, one is able to maintain a high level of accuracy and while improving the multiple objectives, compared to the actual selection of the recruiters. Implementing the presented approach as a decision support tool can increase the impact of recruiters and maximize organizational return on investment.

The utilized dataset in this study is unique and includes the data of hundreds of thousands of employees over a decade. The data represent a wide range of heterogeneous populations represented in a big-data repository. These characteristics allow us to analyze various recruitment policies and decisions that traditionally could not be tested due to the absence of proper data for such research studies.

The proposed methodology can be acted upon directly by HR professionals, without a need for deeper technical or machine learning knowledge, and can be implemented as a support software tool for recruiters and HR managers. A detailed study on the contribution of the proposed approach with respect to existing HR theories is beyond the scope of this paper and can be found in [40,58].

We recognize that a prediction model that stands alone may be inherently biased; hence, in this work, we approach this potential bias through several measures: i) an objective target measure; ii) a large dataset incorporating a large range of difering applicants; iii) a mathematical programming model that enhances diversity and balance; and iv) a proposition to use a combined decision of both the recruiter and the used algorithm.

For future research, we suggest examining various directions of post-hire feature analysis and studying how these factors afect re cruitment performance in comparison to the baseline literature as well as to a pre-hire analysis only. In light of the explainable patterns dis covered in relevant candidate profiles, organizations may also devise and adjust personalized practices, such as specific training programs, awareness workshops, compensation and benefit plans, definitions of job duties, work-life balance policies, management and communication campaigns, and the overall organizational culture [44].

## CRediT authorship contribution statement

All authors conceived of the presented ideas, developed the theory, performed the computations, discussed the results and took part in writing the paper. All authors read and approved the final manuscript.

Dana Pessach:Conceptualization, Methodology, Formal analysis, Validation, Writing - original draft, Writing - review & editing.Gonen Singer:Conceptualization, Methodology, Formal analysis, Validation, Writing - original draft, Writing - review & editing.Dan Avrahami:Conceptualization, Methodology, Formal analysis, Validation, Writing - original draft, Writing - review & editing.Hila Chalutz Ben-Gal:Conceptualization, Methodology, Formal analysis, Validation, Writing - original draft, Writing - review & editing.Erez Shmueli:Conceptualization, Methodology, Formal analysis, Validation, Writing - original draft, Writing - review & editing.Irad Ben-Gal:Conceptualization, Methodology, Formal analysis, Validation, Writing - original draft, Writing - review & editing.

## Declaration of competing interest

None.

## Acknowledgements

This paper was partially supported by the Koret Foundation Grant for Smart Cities and Digital Living 2030.

## Appendix A. Use of VOBN for recruitment success prediction

In this study, we propose to use flexible and generalized version of the Bayesian Network (BN) models [59], called Variable Order Bayesian Networks (VOBN) model as proposed by [10,11]. Similar to the BN it is an interpretable model that can be used to describe the relationship among various features, however, as opposed to BN possible connection between features does not imply necessarily that all the feature values of the conditioning features afect the conditioned feature. The possibility to construct such a flexible learning model that is not necessarily balanced over the entire feature space and at the same time can reveal those specific value-dependent patterns is found to be of outmost importance in the case of HR recruitment applications. For example, for a certain position, the probability of a successful recruitment might depend only on a specific language test score (e.g., a test score above 95) that is correlated with a specific managerial background, while all the other scores and background levels do not afect the recruitment success and should be therefore ignored or “lumped” together.

The following walk through example demonstrates the VOBN algorithm and implementation for predicting the turnover rate of female candidates who were hired to perform administrative roles. Detailed discussion on the VOBN algorithm can be found in [10].

## Stage 1: Bayesian Network construction

First, the algorithm builds a Bayesian Network for the available features and the target variable, which in this case is the turnover rate. It uses the mutual information between the features as a dependence measure, and constructs the maximum likelihood graph structure, by placing feature with high mutual information next to each other. Next, it locates the target variable in the Bayesian Network and the features leading to it. In Fig. 10 one can see a portion of the Bavesian Network generated for the candidates' dataset. It shows that the conditioned distribution of the turnover rate depends directly on the Oral Language Score feature, which depends on the feature Educational Background, which depends on the Birth Country etc.

For an alternative algorithm which uses a Bayesian network instead of the Bayesian tree see [10].

## Stage 2: variable order Markov (VOM) context tree construction

After the Bavesian network (or a Bavesian tree in this example) is constructed, the algorithm constructs a complete and balanced tree of depth L – a fixed-order Markov tree of depth $L ,$ using the features from the Bayesian Network. It sets R to be the minimal frequency of samples in a leaf, for statistically significance evaluation. It chooses an initial depth L for the context tree, such that there are on average at least R examples in each leaf, to enable suficient number of leaves with minimal frequency after the pruning stage (see stage 3). In the walk-through example the depth of the tree is set to L = 3 to obtain an average of R = 100 samples per leaf. We use the order found by the Bayesian network, as an input for the context tree construction.

![](/api/attachments/X5UZVYZ7/fulltext/images/c2fa4c34e5f7b3459d25d9bcac0cc248c8defed123f79133973be10c8590def6.jpg)  
Fig. 10. Portion of the Bayesian Network constructed for the dataset.

## Stage 3: context tree pruning

In order to obtain a minimal context tree, which capture most of the information in the features, and allows statistical significance, two pruning rules are applied as follows.

i) Pruning rule 1 – leaf (i.e. the end node in the context tree) which has less examples than our minimal frequency of $R = 1 0 0$ . Note that in Fig. 11 the pruned nodes/leaves are marked with a dashed border. Specifically, leaf {7} has only 48 examples and therefore it is pruned, since it has a smaller frequency than the minimal required (with 100 entities).

ii) Pruning rule 2 – The algorithm compares the information obtained from the descendant leaf, defined by series of features sb, to the information obtained from the parent node, defined by series of features s. It then prunes the descendant node if the diference is smaller than a predefined penalty value for making the tree bigger – this penalty is called the pruning threshold. Hence, a node that has a turnover distribution similar to the distribution of the parent's node is pruned, since it doesn't add enough information. In this example, the algorithm estimates the turnover probability for each of the nodes, according to the frequencies of turnover cases.

In Eq. (1) the algorithm computes ΔN(sb) - the (ideal) code length diference between each descendant leaf, denoted by the pattern sb and its parent node, marked by the pattern s. b is the last split feature and its value of the descendent leaf, and s is the pattern defined by all previous split features and their values till the parent node. For example, in Fig. 11, descendant leaf can be sb = {Low oral language score, Educational background A, Birth Country I}, while its parent node is denoted by s = {Low oral language score, Educational background A}.

$$
\Delta N (s b) = \sum_ {x \in X} n (x \mid s b) \log_ {2} \left(\frac {\widehat {P} (x \mid s b)}{\widehat {P} (x \mid s)}\right)\tag{1}
$$

## X turnoverTrue turnoverFalse= { , }

P x sb( | ) is the conditional probability for obtaining the value x in the descendant node $s b ,$ and $n ( \boldsymbol { x } | \boldsymbol { s b } )$ denotes the number of samples with the value x in the descendant node sb, X is the finite set of values of the variable target. In our case, these are the turnoverTrue and the turnoverFalse values. If the diference is smaller than a pre-selected pruning threshold, the leaf is pruned, as defined in Eq. (2).

In order to reduce over-fit and simplify the context tree, without losing much information, the algorithm prunes the context tree, which leaves nodes that contributes significantly to the turnover classification task and contains enough samples to allow statistical significance. In order to achieve this requirement, it requires that ΔN(sb) will satisfy Eq. (2).

$$
\varDelta N (s b) > C (d + 1) \cdot l o g _ {2} (t + 1)\tag{2}
$$

where C is a pruning constant tuned to the considered process requirements (with default of C = 2 as suggested in [60]). d is the number of values the target variable can obtain, in our case d = 2 (since the target variable includes only two values: turnoverTrue, turnoverFalse) and t is the number of features defined by the pattern sb of the examined node.

We will now show an example for the calculations of Eas. (1) and (2) using the tree shown on Fig. 11. When we calculate the (ideal) code lengtl diference for the bottom descendent left leaf {6}, defined by the patterns sb = {Low oral language score, Educational background B, Birth country II}, compared to its parent node defined by s = {Low oral language score, Educational background B} using Eq. (1) we obtain the following result

$$
\varDelta N (s b) = 1 2 \cdot l o g _ {2} \frac {\mathbf {0 . 1 2}}{\mathbf {0 . 2 5}} + 9 1 \cdot l o g _ {2} \frac {\mathbf {0 . 8 8}}{\mathbf {0 . 7 5}} = 8. 2 7
$$

In order for this descendent leaf not to be pruned, Eq. (2) must hold, i.e.,

$$
\Delta N (\mathrm{sb}) > 2 \cdot (2 + 1) \cdot l o g _ {2} (3 + 1) = 1 2.
$$

Since ΔN (8.27) is below the threshold in our case, 12, then leaf is pruned.

Similarly, the algorithm prunes leaf {2} in the tree shown on Fig. 11, with the pattern High Oral Language Score since its turnover rate (6%) is similar to the turnover rate of its parent node - in this case the root node {1} (7%).

The summary of the used notations in this section is presented in Table 8.

![](/api/attachments/X5UZVYZ7/fulltext/images/e8c3f27193cdc3dd2da17ab34902454051b098ab379d05032002b15abbb6deb2.jpg)  
Fig. 11. VOM Context Tree of the walk thorough example Pruned nodes are marked with a dashed line.

<table><tr><td colspan="2">Table 8Notations.</td></tr><tr><td>Notation</td><td></td></tr><tr><td>L</td><td>Depth of the complete and balanced tree</td></tr><tr><td>R</td><td>Minimal frequency of samples per leaf for statistically significance.</td></tr><tr><td>s</td><td>Pattern, define by series of variable of the parent node</td></tr><tr><td>sb</td><td>Pattern define the descendant leaf, by the series of the variables of the parent s, and addition split variable b.</td></tr><tr><td>x</td><td>The value of the target variable. In our case, x ∈ X {turnoverFalse, turnoverTrue}</td></tr><tr><td>X</td><td>Finite set for the target variable X {turnoverFalse, turnoverTrue}</td></tr><tr><td>n(x|sb)</td><td>Number of samples with the value x in the descendant node sb</td></tr><tr><td>ΔN(sb)</td><td>The (ideal) code length difference between the descendant node sb and the parent node</td></tr><tr><td> $\widehat{P}$  (x|sb)</td><td>The estimated conditional probability for getting the value x in the descendant node</td></tr><tr><td> $\widehat{P}$  (x|s)</td><td>The estimated conditional probability for getting the symbol x (in the parent)</td></tr><tr><td>d</td><td>The size of the finite set X.In our case d = 2 since X = {turnoverFalse, turnoverTrue}</td></tr><tr><td>C</td><td>The pruning constant tuned to process requirements (with default C = 2)</td></tr><tr><td>t</td><td>The pattern size of an examined node (depth of leaf).</td></tr></table>

## Stage 4: patterns identifications

The pruned context tree is left with a smaller number of leaves, each represents a pattern related to a specific sub-population, whose turnover rate is distinguishably diferent than the parent sub-population. In the context tree in Fig. 11, the following patterns are found for women in adminis trative roles with low oral language score:

1. Candidates from educational background B – 25% turnover rate.

2. Candidates from educational background A who were born in country II – 29% turnover rate.

3. Candidates from educational background A who were born in country I – 77% turnover rate.

Strength and Weaknesses of the VOBN Model in Recruitment Analysis

VOBN provides an important extension with respect to both Bayesian Network and Decision Tree models. In Decision Tree models, leaves represent class labels, nodes represent features and branches represent conjunctions of features that lead to those class labels. When the target variable takes a discrete set of values these trees are often called Classification Trees, while for a continuous target variable they are called Regression Trees. Decision Trees can generate a set of rules directing how to classify the target variable based on the associated features values, yet in a tree-like structure, thus where each node (feature) has only a single parent node. As opposed to decision trees, VOBN constructs a more general graph structure, where several nodes can be the parents of other nodes, thus representing a more general dependencies structure among diferent features in the model (these structures can then be mapped to a simpler tree-like rules, as done in this study). This generalization is important in the considered recruitment and placement application, since complex dependency patterns that involve several features and their interactions (e.g., background. performance, motivation etc.) can lead to different placements and recruitment recommendations that can result in a higher perfor: mance, as seen in Table 6.

The VOBN not only generalize Decision Trees but also generalizes the conventional Bavesian Network (BN) model. In BN modeling each variable (feature) depends on a fixed subset of random variables that are locally connected to it, however, in VOBN models these subsets may vary based on the specific realization of their observed variables. For example, a complex dependency between a Language Score and a Leadership Score features to the placement success in a specific position, might exists only for specific score values, while for other score values such a dependency is practically insignificant. This generalization lead to a reduction in the number of the model parameters, resulting in a better training and performance. The observed realizations in the VOBN are often called the contexts and, hence, VOBN models are also known as Context-Specific Bayesian networks.

In summary, compared to Decision Trees and conventional Bayesian Networks, often the classification performance of the VOBN is better, based on its higher flexibility in learning and expressing complex conditions and patterns among subsets of feature values. In the considered domain of HR analytics, this flexibility implies that the context dependency (based on the variable ordering) may be represented diferently for each of the considered positions. Additionally, the VOBN handles better the variance-bias tradeoff, compared to decision trees, which often suffers from over: fitting [10,61] and may cause high variance. The VOBN models have previously shown good performance in analyzing various datasets (some of which publicly available), including DNA sequence classification [10,62,63], transportation and production monitoring [11,64,65]. The VOBN has two main limitations. First, the dataset has to contain relatively large amount of data in order to construct the initial network structure. Second, the features introduced into the model should be discretized in a preprocess stage. In this study we used a large HR dataset, in which most of the features contain discrete values, hence yielding high performance of the VOBN.

It is worth noticing that this machine learning model has two main distinctions from traditional hypothesis-testing and regression models. First. the latter focuses on features that are highly correlated with trends across the entire aggregated sample, whereas the analysis by the VOBN mode allows for identifying patterns in specific sub-groups. This notion is also closely related to Simpson's Paradox [55], which shows that an observed trend in subgroups may behave quite diferently when these subgroups are aggregated and analyzed together. Second, hypothesis-testing requires in advance assumptions about the interactions among features, whereas machine learning models do not require such assumptions, and allow for discovering insights that were not assumed ahead. For further mathematical and experimental details on the construction of the VOBN model, please see [10,11].

## References

[1] J. Sullivan, News flash: recruiting has the highest business impact of any HR function, https://www.ere.net/news-flash-recruiting-has-the-highest-businessimpact-of-any-hr-function/, (2012) , Accessed date: 14 July 2019

[2] H. Boushey, S.J. Glynn, There are significant business costs to replacing employees, https://www.americanprogress.org/issues/economy/reports/2012/11/16/44464/ there-are-significant-business-costs-to-replacing-employees/, (2012) , Accessed date: 14 July 2019.

[3] P.R. Bernthal, R.S. Wellins, Retaining talent: a benchmarking study, HR Benchmark Gr 2 (2001) .1–28

[4] I. Lee, Modeling the benefit of e-recruiting process integration, Decis. Support. Syst. 51 (2011) 230–239.

[5] M.A. Shehu, F. Saeed, An adaptive personnel selection model for recruitment using domain-driven data mining, J. Theor. Appl. Inf. Technol. (2016) 91.

[6] A. Janusz, S. Stawicki, K. Drewniak Michałand Ciebiera, D. Ślkezak, K. Stencel, How to match jobs and candidates-a recruitment support system based on feature engineering and advanced analytics, Int. Conf. Inf. Process. Manag. Uncertain. Knowledge-Based Syst, 2018, pp. 503–514.

[7] P. Biecek, DALEX: explainers for complex predictive models in R, J. Mach. Learn. Res, 19 (2018) 3245–3249.

[8] E. Ribes, K. Touahri, B. Perthame, Employee turnover prediction and retention policies design: a case study. ArXiv Prepr. ArXiv1707 (2017) 01377

[9] M.T. Ribeiro. S. Singh. C. Guestrin. Model-agnostic interpretability of machine learning. ArXiv Prepr. ArXiv1606 (2016) 05386.

[10] I. Ben-Gal, A. Shani, A. Gohr, J. Grau, S. Arviv, A. Shmilovici, S. Posch, I. Grosse, Identification of transcription factor binding sites with variable-order Bavesian networks, Bioinformatics 21 (2005) 2657–2666, https://doi.org/10.1093/ bioinformatics/bti410.

[11] G. Singer, I. Ben-Gal, The funnel experiment: the Markov-based SPC approach, Oual. Reliab. Eng, Int. 23 (2007) 899–913.

[12] A.A. Freitas, Comprehensible classification models: a position paper, ACM SIGKDD Explor. Newsl. 15 (2014) 1–10

[13] N. Sivaram, K. Ramar, Applicability of clustering and classification algorithms for recruitment data mining Int J. Comput Appl 4 (2010) 23–28

[14] A. Barak, R. Gelbard, Classification by clustering decision tree-like classifier based on adjusted clusters, Expert Syst. Appl. 38 (2011) 8220–8228.

[15] E. Faliagka, L. Iliadis, I. Karydis, M. Rigou, S. Sioutas, A. Tsakalidis, G. Tzimas, Online consistent ranking on e-recruitment: seeking the truth behind a well-formed CV. Artif, Intell, Rev, 42 (2014) 515–528.

[16] K.-Y. Wang, H.-Y. Shun, Applying back propagation neural networks in the prediction of management associate work retention for small and medium enterprises, Univers. J. Manag. 4 (2016) 223–227.

[18] R. Punnoose, P. Ajit, Prediction of employee turnover in organizations using ma chine learning algorithms. Int. J. Ady. Res. Artif. Intell. 5 (2016).

[17] X.-L. Qu, A decision tree applied to the grass-roots stafs' turnover problem—take CR Group as an example, Grey Syst. Intell. Serv. (GSIS), 2015 IEEE Int. Conf, 2015, pp. 378–382.

[19] E. Sikaroudi, A. Mohammad. R. Ghousi, A. Sikaroudi, A data mining approach to emplovee turnover prediction (case study: Arak automotive parts manufacturing) J. Ind, Svst, Eng, 8 (2015) 106–121.

[20] X. Gui, Z. Hu, J. Zhang, Y. Bao, Assessing personal performance with M-SVMs, Comput, Sci, Optim, (CsO), 2014 Seventh Int, Jt. Conf, 2014, pp. 598–601.

[21] C.-Y. Fan, P.-S. Fan, T.-Y. Chan, S.-H. Chang, Using hybrid data mining and machin learning clustering analysis to predict the turnover rate for technology profes sionals, Expert Syst. Appl. 39 (2012) 8844–8851.

[22] V.V. Saradhi, G.K. Palshikar, Employee churn prediction, Expert Syst. Appl. 38 (2011)1999–2006.

[23] J.M. Kirimi, C.A. Moturi, Application of data mining classification in employee performance prediction, Int. J. Comput. Appl. 146 (2016).

[24] M.A. Valle, S. Varas, G.A. Ruz, Job performance prediction in a call center using a naive Baves classifier, Expert Syst Appl 39 (2012) 9939–9945

[25] C.-F. Chien, L.-F. Chen, Data mining to improve personnel selection and enhance human capital: a case study in high-technology industry. Expert Syst. Appl. 34 (2008) 280–290.

[26] Y.-M. Li, C.-Y. Lai, C.-P. Kao, Incorporate personality trait with support vector machine to acquire quality matching of personnel recruitment, 4th Int. Conf. Bus Inf, 2008, pp. 1–11.

[27] M.P. Bach, N. Simic, M. Merkac, Forecasting employees' success at work in banking: could psychological testing be used as the crystal ball? Manag. Glob. Transitions. 11 (2013) 283.

[28] S. Mehta, R. Pimplikar, A. Singh, L.R. Varshney, K. Visweswariah, Eficient multi faceted screening of job applicants, Proc. 16th Int. Conf. Extending Database Technol, 2013, pp. 661–671.

[29] S. Benabderrahmane, N. Mellouli, M. Lamolle, A. Janusz, S. Stawicki, K. Drewniak Michałand Ciebiera, D. Ślkezak, K. Stencel, On the predictive analysis of behavioral massive job data using embedded clustering and deep recurrent neural networks, Int. Conf. Inf. Process. Manag. Uncertain. Knowledge-based Syst, Elsevier, 2018, pp. 503–514

[30] S. Yang, M. Korayem, K. AlJadda, T. Grainger, S. Natarajan, Combining contentbased and collaborative filtering for job recommendation system: a cost-sensitive Statistical Relational Learning approach, Knowledge-Based Syst 136 (2017) 37–45.

[31] K.G. Bigsby, J.W. Ohlmann, K. Zhao, The turf is always greener: predicting decommitments in college football recruiting using twitter data. Decis. Support. Syst 116 (2019).1–12

[32] H. Jantan, A.R. Hamdan, Z.A. Othman, Towards applying data mining techniques for talent management, Int. Conf. Comput. Eng. Appl. IPCSIT, IACSIT Press, Singapore, 2011.

[33] S. Strohmeier, F. Piazza, Domain driven data mining in human resource management: a review of current research, Expert Syst. Appl. 40 (2013) 2410–2420.

[34] C.C. Hao, H.C. Jung, O. Yenhui, A study of the critical factors of the job involvement of financial service personnel after financial tsunami: take developing market (Taiwan) for example, African J. Bus. Manag. 3 (2009) 798.

[35] M.O. Samuel, C. Chipunza, Employee retention and turnover: using motivational variables as a panacea, African J. Bus. Manag. 3 (2009) 410.

[36] B. Coomber, K.L. Barriball, Impact of job satisfaction components on intent to leave and turnover for hospital-based nurses: a review of the research literature, Int. J Nurs, Stud, 44 (2007) 297–314.

[37] J. Bollinger, D. Hardtke, B. Martin, Using social data for resume job matching, Proc. 2012 Work. Data-Driven User Behav. Model. Min. From Soc. Media, 2012, pp. 27–30.

[38] C.-F. Chien, L.-F. Chen, Using rough set theory to recruit and retain high-potential talents for semiconductor manufacturing, IEEE Trans. Semicond. Manuf. 20 (2007) 528–541.

[39] V.M. Menon, H.A. Rahulnath, A novel approach to evaluate and rank candidates in a recruitment process by estimating emotional intelligence through social media data, Next Gener. Intell. Syst. (ICNGIS), Int. Conf, 2016, pp. 1–6.

[40] H. Chalutz Ben-Gal, An ROI-based review of HR analytics: practical implementation tools, Pers. Rev. 48 (2019) 1429–1448, https://doi.org/10.1108/PR-11-2017-0362.

[41] R. Gelbard, R. Ramon-Gonen, A. Carmeli, R.M. Bittmann, R. Talyansky, Sentiment analysis in organizational work: towards an ontology of people analytics, Expert. Syst. 35 (2018) e12289.

[42] D. McIver, M.L. Lengnick-Hall, C.A. Lengnick-Hall, A strategic approach to workforce analytics: integrating science and agility, Bus. Horiz. 61 (2018) 397–407.

[43] A. Tursunbayeva, S. Di Lauro, C. Pagliari, People analytics: a scoping review of conceptual boundaries and value propositions, Int. J. Inf. Manag. 43 (2018) 224–247.

[44] T.H. Davenport, J. Harris, J. Shapiro, Competing on talent analytics, Harv. Bus. Rev. 88 (2010) 52–58.

[45] More Evidence That Company Diversity Leads To Better Profits, (n.d.). https:// www.forbes.com/sites/karstenstrauss/2018/01/25/more-evidence-that-company diversity-leads-to-better-profits/#2d3f7ef1bc7 (accessed November 23, 2019).

[46] Racially Diverse Companies Outperform Industry Norms by 35%, (n.d.). https:// www.forbes.com/sites/ruchikatulshvan/2015/01/30/raciallv-diverse-companies: outperform-industry-norms-bv-30/#5d4de9cf1132 (accessed November 23. 2019)

[47] A. Levenson, A. Fink, Human capital analytics: too much data and analysis, not enough models and business insights, J. Organ. Ef. People Perform. 4 (2017) 145–156.

[48] J. Boudreau, W. Cascio, Human capital analytics: why are we not there? J. Organ. Ef. People Perform. 4 (2017) 119–126.

[49] D. Minbaeva, Human capital analytics: why aren't we there? Introduction to the special issue, J. Organ. Ef. People Perform. 4 (2017) 110–118.

[50] D.W. Pentico, Assignment problems: a golden anniversary survey, Eur. J. Oper. Res. 176 (2007) 774–793.

[51]. N.V. Chawla. Data mining for imbalanced datasets: an overview. Data Min. Knowl Discoy, Handb, Springer, 2009, pp. 875–886.

[52] A. Chinchuluun. P.M. Pardalos. A survey of recent developments in multiobiective optimization, Ann, Oper, Res, 154 (2007) 29–50.

[53] M. Skowronski, Overqualified emplovees: a review, a research agenda, and re commendations for practice, J. Appl. Bus. Econ, 21 (2019)

[54] D.C. Maynard, E.M. Brondolo, C.E. Connelly, C.E. Sauer, I'm too good for this job: Narcissism's role in the experience of overqualification, Appl. Psychol. 64 (2015) 208–232. https://doi.org/10.1111/apps.12031

[55] C.R. Blyth, On simpson's paradox and the sure-thing principle, J. Am. Stat. Assoc. 67 (1972) 364–366, https://doi.org/10.1080/01621459.1972.10482387.

[56] J. Elith, J.R. Leathwick, T. Hastie, A working guide to boosted regression trees, J. Anim, Ecol, 77 (2008) 802–813

[57] I. Griva, S.G. Nash, A. Sofer, Linear and Nonlinear Optimization, Siam, 2009

[58] H. Chalutz Ben-Gal, D. Avrahami, D. Pessach, Singer Gonen, I. Ben-Gal. A Human Resources Analytics and Machine-Learning Fxamination of Turnover: Implications for Theory and Practice, (2020)

[59] I. Ben-Gal, Bayesian networks, Encycl. Stat. Qual. Reliab, 2007.

[60] M.J. Weinberger, J.J. Rissanen, M. Feder, A universal finite memory source, IEEE Trans. Inf. Theory 41 (1995) 643–652.

[61] I. Ben-Gal, G. Morag, A. Shmilovici, Context-based statistical process control, Technometrics 45 (2003) 293–311, https://doi.org/10.1198 004017003000000122

[62] S. Posch, J. Grau, A. Gohr, I. Ben-Gal, A.E. Kel, I. Grosse, Recognition of cis-regulatory elements with vombat, J. Bioinforma. Comput. Biol. 5 (2007) 561–577.

[63] J. Grau, I. Ben-Gal, S. Posch, I. Grosse, VOMBAT: prediction of transcription facto binding sites using variable order Bavesian trees, Nucleic Acids Res. 34 (2006)

[64] I. Ben-Gal, G. Singer, Statistical process control via context modeling of finite-state processes: an application to production monitoring, IIE Trans. (Institute Ind. Eng.) 36 (2004) 401–415, https://doi.org/10.1080/07408170490426125.

[65] I. Ben-Gal, G. Morag, A. Shmilovici, Context-based statistical process control: a monitoring procedure for state-dependent processes, Technometrics 45 (2003) 293-311.

[66] M.N. Wright, A. Ziegler, {ranger}: a fast implementation of random forests for high dimensional data in {C++} and {R}, J. Stat. Softw. 77 (2017) 1–17, https://doi. org/10.18637/jss.v077.i01.

[67] R.J. Hijmans, S. Phillips, J. Leathwick, J. Elith, dismo: Species Distribution

Modeling, https://cran.r-project.org/package=dismo, (2017).

[68] S. Janitza, E. Celik, A.-L. Boulesteix, A computationally fast variable importance test for random forests for high-dimensional data, Adv. Data Anal. Classif. 12 (2018) 885–915.

[69] L. Breiman, Random forests, Mach. Learn. 45 (2001) 5–32.

[70] P. Romanski, L. Kotthof, FSelector: Selecting Attributes, (2016).

[71] I. Steinwart, P. Thomann, {liquidSVM}: A Fast and Versatile SVM Package, ArXiv E-Prints 1702.06899, http://www.isa.uni-stuttgart.de/software, (2017).

[72] S.B. Kotsiantis, I. Zaharakis, P. Pintelas, Supervised machine learning: a review of classification techniques, Emerg. Artif. Intell. Appl. Comput. Eng. 160 (2007) 3–24.

[73] S. Theussl, K. Hornik, Rglpk: R/GNU Linear Programming Kit Interface, https:// cran.r-project.org/package=Rglpk, (2017).

[74] J.M. Sallan, O. Lordan, V. Fernandez, Modeling and Solving Linear Programming With R, OmniaScience, 2015.

Dana Pessach is a PhD candidate at the Big Data Lab at Tel-Aviv University. Her research focuses on applying computational methods to social sciences and contributing to the development of new methods to deal with real-life problems. She is additionally a member of the steering committee at LAMBDA, the artificial intelligence lab at Tel-Aviv University, and a freelance consultant to start-ups and entrepreneurs in the fields of Machine Learning and Artificial Intelligence. As part of her role she leads research projects in domains such as: HR analytics using Machine Learning methods, financial data technologies, health data analysis and smart-cities. Her teaching experience includes several topics for undergraduate programs such as: operations research, robotics, mobile application development, modeling and 3D printing, social network analysis and com puter vision.

Gonen Singer, Ph.D., is a Senior Lecturer of Industrial Engineering and Information Systems at Bar-Ilan University. Before joining Bar Ilan, Gonen was a Senior Lecturer at AFEKA-Tel-Aviv Academic College of Engineering. He joined to the Department of Industrial Engineering and Management at AFEKA, shortly after its establishment at 2008 and was appointed as Head of the Department in the years 2009–2015. Gonen Singer has extensive expertise in machine learning techniques and stochastic optimal control and their application to real-world problems in diferent areas, such as retail, manufacturing and education and has around 50 Scientific and professional publications. Gonen Singer served as a principal investigator in 10 Research Grants since 2011 that were obtained from various sources.

Dan Avrahami holds an M.Sc. from LAMBDA, the artificial intelligence lab at Tel-Aviv University, where he also taught Information Systems Engineering. In his HR analytics research, he explored the application of machine learning in general, and a generalization of Bayesian Networks in particular, to improve employees' recruitment and placement.

Dan is a data scientist and machine learning researcher with experience implementing various machine learning methods on challenging data domains. He has a solid back ground as a software engineer and database administrator.

Hila Chalutz Ben-Gal is a Senior Lecturer at the Department of Industrial Engineering and Management, Tel Aviv Afeka College of Engineering, Israel. She received her BA degree (with honors) from the Hebrew University in Jerusalem, Master's Degree from Brandeis University, Boston, MA, USA, and her Ph.D from Haifa University, Israel. Her research interests include HR Analytics, and the changing nature of organizations in the digital era, with a focus on organizational design and the future of work. She conducts field research and consulting work in a variety of organizational settings. Some of her current projects include HR analytics and turnover forecasting, career moves detection in on-line labor markets and the changing nature of work due to COVID-19 pandemic During 2015–17 she was a Visiting Scholar at the ChartLAB at the University of San Francisco in California, USA

Erez Shmueli is a senior lecturer and the head of the Big Data Lab at the department of Industrial Engineering at Tel-Aviv University and a research afiliate at the MIT Media Lab. He received his BA degree (with honors) in Computer Science from the Open University of Israel and MSc and PhD degrees in Information Systems Engineering from Ben-Gurion University of the Negev and spent two years as a post-doctoral associate at the MIT Media Lab. His research interests include Big Data, Complex Networks, Computational Social Science, Machine Learning, Recommender Systems, Database Systems, Information Security and Privacy. His professional experience includes being a programmer and a team leader in the Israeli Air-Force and, a project manager in Deutsche Telekom Laboratories at Ben-Gurion University of the Negev, a co-founder of two startups (Babator and SafeMode), and a consultant (among the rest to Microsoft and the muni cipality of Ashdod).

Irad Ben-Gal is a full professor and the Head of the Laboratory for AI, Machine learning, Business & Data Analytics (LAMBDA) at the Engineering Faculty in Tel Aviv University. He received his M.Sc. (1996) and Ph.D. (1999) from the Boston University. His research interests include machine learning, applied probability and statistical control, involving R &D collaborations with companies such as Oracle, Intel, GM, AT&T, Applied Materials and Nokia. He wrote three books, published > 120 journal and peer-reviewed conference papers and patents, supervised dozens of graduate students and received numerous awards for his work. He co-heads the TAU/Stanford “Digital Living 2030” research program that focuses on data science challenges of modern digital life. The program involves scientists at TAU and Stanford, where he held a visiting professor position, teaching “analytics in action” to graduate students. Irad is the co-founder of CB4 (“See Before”), a startup backed by Sequoia Capital that provides predictive analytics solutions to retail organizations.
