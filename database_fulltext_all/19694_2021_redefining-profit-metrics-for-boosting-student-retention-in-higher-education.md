---
otero_id: 19694
otero_key: "VK6H57ED"
title: "Redefining profit metrics for boosting student retention in higher education"
authors: "Sebastián Maldonado; Jaime Miranda; Diego Olaya; Jonathan Vásquez; Wouter Verbeke"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113493"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Redefining profit metrics for boosting student retention in higher education

![](/api/attachments/VK6H57ED/fulltext/images/8815c980d8087dd8ba7ce14319af99008cbee6df0531ed6447d913087516a784.jpg)

Sebastian ´ Maldonado <sup>a,b</sup>, Jaime Miranda <sup>a</sup>, Diego Olaya <sup>c,\*</sup>, Jonathan Vasquez´ <sup>d,e</sup>, Wouter Verbeke

<sup>a</sup> Department of Management Control and Information Systems, School of Economics and Business, University of Chile, Santiago, Chil <sup>b</sup> Instituto Sistemas Complejos de Ingeniería (ISCI), Chile

<sup>c</sup> Data Analytics Laboratory, Faculty of Social Sciences & Solvay Business School, Vrije Universiteit Brussel, Pleinlaan 2, 1050 Brussels, Belgium

<sup>e</sup> Centro de Investigaci´on en Negocios y Gestion ´ Empresarial, Universidad de Valparaíso, Chile

<sup>f</sup> Faculty of Economics and Business, Katholieke Universiteit Leuven, Naamsestraat 69, B-3000 Leuven, Belgium

## A R T I C L E I N F O

Keywords: Education Profit metrics Student dropout Student retention Analytics

## A B S T R A C T

Student dropout is a major concern in higher education, as it leads to direct economic losses and substantial social costs. Public and private institutions spend considerable resources to prevent student dropout. The effi. ciency and effectiveness of these investments, however, may be improved by adopting a profit-driven perspec tive. In this paper, we propose a novel approach for implementing student dropout prediction using data-driven methods. Extending upon profit metrics as used in business analytics, we design a novel performance measure for evaluating predictive models that is tailored to the student dropout problem and that quantifies the net savings of a retention campaign. This metric supports the identification and selection of students to optimally allocate the limited resources for preventing student dropout and to maximize the resulting savings. Experiments were performed using data from three bachelor’s programs of a higher education institution containing information on dropouts and participation in a retention program, i.e., tutorials. The proposed metric allows for a better choice of prediction model and classification threshold than conventional approaches and, as a result, yields tangible savings for the institution. Finally, the presented approach and experimental results highlight pathways to design tailored student retention programs.

## 1. Introduction

The early identification of dropouts is a major concern for higher education institutions (HEIs). Low dropout rates lead to important benefits for HEIs, such as reduced financial losses, improved ranking/ status and accreditation processes, and external perceptions among prospective students [1–4]. The majority of HEIs rely on specialized units that design tutorials, programs and other services to prevent dropouts [2]. In this regard, the use of analytics and machine learning techniques has proven to be successful in various tasks that are of prime interest: assessing student satisfaction [5], evaluating student perfor mance [6,7], and predicting student dropout [1,2,8].

An important limitation in existing studies on student dropout pre diction is that model performance is exclusively assessed by means of statistical measures. These measures, however, are not tailored to the problem at hand and do not align with the actual goal, e.g., maximizing the savings or profit from retention campaigns. Hence, we argue that the costs and benefits of implementing retention programs should be taken into account when selecting the best model for predicting student dropout, i.e., the model with the best performance as evaluated in terms of the goal of interest. Note here that the development of a customized performance measure is a nontrivial task and is the research objective in this article.

Recent studies in business analytics, particularly the research stream on profit metrics, which consider the costs and benefits that result from applying a predictive model [9,10], have revealed substantial advan tages of using goal-oriented metrics over purely statistical approaches. The predictive model with the highest accuracy, for instance, does not necessarily lead to the maximum profit that can be obtained.

Customer churn prediction is arguably the most studied application for profit metrics. This task is similar to student dropout prediction and seeks to identify customers that are likely to attrite, which allows us to target the customers that are most likely to churn in a retention campaign [11]. Retention campaigns lead to loyal, engaged customers that generate more revenue than others [10,11].

From a methodological perspective, this study contributes by pro posing a novel profit metric for assessing the performance of student dropout prediction models, with the eventual aim of aligning the development of these models and the design of retention strategies. Our hypothesis is that a goal-oriented performance measure improves the operational performance of dropout predictive models and that, as a result, an improved tool to support decision-making is obtained. The proposed metric identifies the optimal classification threshold for dropout predictive models and the variables that are relevant in the design of customized retention campaigns.

From an economic perspective, this study contributes by providing a novel definition of profit in the context of HEIs. Specifically, we relate the costs of retention efforts, e.g., tutorials, to the net present value of a retained student, e.g., the value of future tuition fees. The proposed approach is suitable for private and public HEIs. That is, the tuition fees in private institutions are directly transferred from students and are, supposedly, the main source of income. In contrast, in public in stitutions, the government sponsors students under the premise that a new professional is valuable to society. Therefore, there is a social benefit in retaining students that can be estimated based on the governmental contributions received by the public HEI.

Specifically, the main contributions of this study are as follows:

• We propose a novel metric for evaluating and maximizing the performance of predictive models of student dropout. The proposed approach is the first profit metric that is tailored to this task. It is important to note that our metric is designed for any particular student dropout prediction task, regardless of the retention program or the na ture of the HEI.

• The presented approach extends the existing profit-driven framework for assessing classification model performance. The main methodological challenge is the extension of the conventional profit metric to a case in which the incentive is accepted, but subjects still attrite. The literature on profit-driven evaluation and subsequent ex tensions assumes that all individuals who accept a retention offer do not attrite. This, however, does not necessarily apply to all cases. This is an important contribution, as it incorporates additional flexibility into the meta-framework.

• We present a case study based on data from three undergraduate programs of an HEI. Cost and benefit parameters are calculated to es timate the net benefit of applying a retention program using the newly proposed metric.

• The effectiveness of the current retention program is assessed. The program consists of tutorials that are designed to improve academic performance and enhance motivation among freshmen students. Currently, the program is offered to the full student base; therefore, our hypothesis is that tailoring the program to the students who are selected by a predictive model could further increase the effectiveness of the program.

This work is structured as follows: A review of prior studies on stu dent dropout analytics is presented in Section 2. Section 3 introduces the profit-driven classification framework for churn prediction. The pro posed profit metric for assessing predictive models of student dropout is introduced in Section 4. Section 5 presents the experimental results using data from an HEI. Finally, we conclude and outline future de velopments in Section 6.

## 2. Preventing student dropout via analytics

Student dropout in HEIs can be understood as failure to graduate after enrolling in a program. This problem has attracted the interest of several researchers [12]. Early studies theorize on the phenomenon based on psychological models of human behavior that explain environment-human relationships [13–16]. Their findings have determined the main factors that are currently used in analytical models to describe and predict dropout. Such factors include but are not limited to family background, academic performance, and institutional envi ronment [12].

This article defines dropout as the student’s decision to abandon the program in which he/she was initially enrolled [4]. This decision can be associated with multidimensional factors related to academic perfor mance and social environment. For example, students who do not fit well disengage and later decide to leave the program [14]. The negative effect of dropouts involves different types of costs. The financial, emotional, and self-development dimensions of students are adversely affected, as are other agents in their environment, e.g., society as a whole. The latter refers to the lack of citizens with professional educa tion and to the weakening of HEIs [17]. Therefore, dropout prevention can result in favorable outcomes for individuals and societies [4,18].

The student dropout problem has been studied as a multidimensional phenomenon from several perspectives. Based on seniority, the analysis can be performed on freshmen [8,19–21] or on students from advanced years [3,4,22]. Conflicting results on the influence of gender and income levels on dropouts have been presented by [21,23–25] and [4,26], respectively. Different designs for analytical models have been pro posed. For example, the class imbalance problem has been addressed by implementing sample methods such as random under sampling (RUS), random over sampling (ROS), or the synthetic monitoring oversampling technique (SMOTE) [4,27–29]. The variety of research designs and conflicting findings may indicate that the study of the dropout problem is highly dependent on contextual elements and the choice of theoretical frameworks.

In addition, digitization and advances in information technology in HEIs have led to the collection of large volumes of data. This has stim ulated studies where data science methods have been proposed to improve the early prevention of student dropout. For example, predic tive models for anticipating academic performance [30], recommender systems to assist career advice [31,32] and a mix of descriptive and predictive approaches based on customer churn prevention [10,33,34].

Current studies on predictive modeling of student dropout evaluate model performance based on conventional statistical metrics. To the best of our knowledge, no methodological advances have been proposed to design novel evaluation approaches to improve decision-making in student dropout analytics. This leads to two important issues: (1) existing approaches do not quantify the benefits and costs of applying retention programs based on predictive models of student dropout, and (2) the use of statistical measures for model assessment may not be appropriate to validate the performance of classifiers in student dropout applications. Statistical metrics do not suggest a classification threshold, and student selection is performed based on the maximum likelihood threshold, i.e., target a student with probability of dropping out greater than 0.5.

This study evaluates student dropout learners based on the profit that could be generated if the targeting decision were based on model pre dictions with the objective of boosting the efficiency and effectiveness of retention programs. Our study goes beyond the use of classifiers to identify factors associated with student dropout and provides relevant insights to support the design of retention campaigns in HEIs. To the best of our knowledge, this has not been previously addressed in the learning analytics literature.

## 3. Profit metrics for churn prediction

The churn prediction task consists of identifying subjects whose likelihood of attrition is the highest. This enables the design of preven tion strategies that more efficiently allocate scarce resources, as the profitability of retention campaigns depends on the costs and future benefits associated with the targeting decision [33].

Churn prediction is a binary classification problem with the outcome variable Y ∈ {0,1}. We align with the notation used in previous profit evaluation approaches in which a churner is represented by $Y = 0$ Conventional machine learning classification methods can be employed to estimate the propensity of a subject to be a churner based on the observed features X.

The classifier outputs a continuous score $s = { \widehat { h } } ( \mathbf { X } ) .$ , which can be used to discriminate between churners and non-churners. A threshold t is predefined such that the campaign is deployed to the subjects who are most likely to attrite, $s \leq t ,$ i.e., churners.

Table 1 depicts the confusion matrix that results from the classifi cation task. N denotes the total size of the sample, $\pi _ { k }$ represents the prior probability of class $k ,$ and $F _ { k } ( t )$ is the associated cumulative distribution function.

The decision rule consists of assigning the retention campaign to the subjects predicted to be churners. However, this segment consists of instances that are correctly classified as churners, true would-be churners, i.e., π F (t)N, and those that are incorrectly classified, false would-be churners, i.e., $\pi _ { 1 } F _ { 1 } ( t ) N .$ . The latter group represents a loss of efficiency, as the campaign would be assigned to subjects who do not require it since they do not intend to attrite.

As mentioned above, the targeting decision involves benefits and costs. There are targeting-related and intervention-related costs. The targeting cost refers to the cost of contacting the predicted churners $C _ { c } ,$ whereas the cost of the intervention $C _ { i }$ concerns the unitary cost of the campaign. The false would-be churners and a proportion $\cdot \gamma$ of the wouldbe churners accept the incentive and do not churn. A benefit, e.g., the customer lifetime value (CLV), is gained from the latter group because they are prevented from churning. The remaining fraction of would-be churners $( 1 - \gamma )$ rejects the campaign and churns.

The profit of a churn classifier can be estimated based on the confusion matrix and the benefits and costs associated with the targeting decision. Eq. 1 defines the average profit of a churn classifier at threshold t as a function of the success rate of the incentive $\gamma$ and the associated benefits and costs as follows:

$$
P (t; \gamma , C L V, \delta , \phi) = C L V (\gamma (1 - \delta) - \phi) \pi_ {0} F _ {0} (t) - C L V (\delta + \phi) \pi_ {1} F _ {1} (t),\tag{1}
$$

where $\delta = C _ { i } / C L V$ and $\phi = C _ { c } / C L V$ are two dimensionless parameters introduced by [34].

The maximum profit (MP) generated by a classifier is obtained by optimizing the cutoff t as proposed by [10], $M P = P ( T ; \gamma , C L V , \delta , \phi )$ . The MP criterion is a business-driven performance metric that can be used to compare the performance of different classifiers. However, the MP as sumes predetermined benefit and cost parameters. [34] extends upon MP and proposes the expected maximum profit (EMP) criterion. EMP considers the uncertainty in the estimation of the parameters of the profit function by assuming a probability distribution for parameter $\gamma .$

## 4. Profit-driven evaluation of student dropout classifiers

The profit-driven evaluation of classifiers has been mainly applied to the problem of churn prediction. Specifically, in the design of marketing campaigns in the telecommunications industry [10], the evaluation of credit scoring models in the financial sector [35], and social network analysis for customer churn [36]. Since customer attrition is analogous to student dropout, we propose a profit-based evaluation of predictive models of student dropout, which to the best of our knowledge has not been implemented in the context of learning analytics.

The approach presented in this paper extends upon the profit framework that is presented in Section 3. Our objective is to shift the goal of developing a predictive model of student dropout from maxi mizing the predictive accuracy, as evaluated in terms of traditional performance measures, to maximizing the savings or profits that are generated. The proposed extension to the profit framework allows us to tailor a profit metric to consider the costs and benefits of the student dropout prevention campaign to maximize its return.

Table 1 Confusion matrix.

<table><tr><td></td><td colspan="2">Predicted</td></tr><tr><td rowspan="3">Real</td><td>Churner</td><td>Non-churner</td></tr><tr><td> $\pi_0F_0(t)N$ </td><td> $\pi_0(1 - F_0(t))N$ </td></tr><tr><td> $\pi_1F_1(t)N$ </td><td> $\pi_1(1 - F_1(t))N$ </td></tr></table>

The main methodological challenge in developing a tailored profit metric is to accommodate partial effectiveness of the retention campaign on student dropout in the event of the acceptance of the offer. The effectiveness in similar marketing applications, as accommodated by the existing profit framework, is generally assumed to be 100%. In the case of student dropout prediction, however, a retention program does not guarantee a successful outcome for a student who agrees to take part in a program.

## 4.1. Profit-driven student dropout framework

This study evaluates dropout classifiers from a profit-driven perspective. The classification task consists of accurately identifying students who will drop out, $Y = 0$ . Subsequently, the performance of the model is evaluated based on the profit generated after considering the future benefits and the targeting- and campaign-related costs, as dis cussed in Section 3.

Student dropout is of great interest, as the dropout rate is the highest in this segment, mainly due to academic performance reasons. Among the different strategies designed by HEIs to prevent early dropouts, this study particularly focuses on providing learning assistance in the form of tutorials. Tutorials are complementary face-to-face or online courses that support students’ learning process.

Fig. 1 depicts the process of the dropout and retention of first-year students. Due to resource constraints, HEIs are unable to provide aca demic assistance to the entire student population, N. Therefore, pre dictive models can be employed to identify a fraction α of the student base that is most likely to drop out. Later, these students are invited to participate in tutorials. Within the targeted fraction of students, a frac tion π F (t) are true would-be dropouts, whereas the remaining pro portion $\pi _ { 1 } F _ { 1 } ( t )$ are false would-be dropouts. Within both groups, however, a fraction γ participates in the tutorials, and a fraction $1 - \gamma$ declines the offer. Unlike in the conventional profit-driven framework wherein a contractual relationship implies the continuity of the customer-company relationship, only a fraction σ of true would-be dropouts who accept the program are retained in the context of stu dent dropout. Learning-support programs attempt to improve the aca demic performance of students, but participation does not necessarily imply that students will succeed. Hence, σ can be interpreted as the success rate of the program.

Eq. 2 defines the average profit of a student dropout classifier at threshold t as a function of the success rate of the program $\sigma ,$ the acceptance rate γ and the benefits and costs associated with the targeting decision.

$$
\begin{array}{c} P (t; \Lambda) = \gamma \sigma (b - C _ {i} - C _ {c}) \cdot \pi_ {0} F _ {0} (t) - \gamma (1 - \sigma) (C _ {i} + C _ {c}) \cdot \pi_ {0} F _ {0} (t) \\ - (1 - \gamma) (C _ {c}) \cdot \pi_ {0} F _ {0} (t) - \gamma (C _ {i} + C _ {c}) \cdot \pi_ {1} F _ {1} (t) - (1 - \gamma) C _ {c} \cdot \pi_ {1} F _ {1} (t), \end{array}\tag{2}
$$

with $\boldsymbol { \Lambda } = \left\{ \gamma , \sigma , b , C _ { i } , C _ { c } \right\}$ being the set of parameters. Subsequently, we can further simplify Eq. 2 by rearranging the terms as follows:

$$
P (t; \gamma , \sigma , b, \delta , \phi) = b (\gamma (\sigma - \delta) - \phi) \cdot \pi_ {0} F _ {0} (t) - b (\gamma \delta + \phi) \cdot \pi_ {1} F _ {1} (t),\tag{3}
$$

where $\delta = C _ { i } / b$ and $\phi = C _ { c } / b$ are the two dimensionless parameters introduced by [34]. Eq. 3 defines the profit of a student dropout clas sifier as the net benefit from targeting a fraction of the true would-be dropouts who participate and are retained by the program after dis counting the costs of targeting false would-be dropouts. Specifically, of the true would-be dropouts who are accepted, a fraction σ is retained, representing the gain b of the program, at the expense of the incentive ϕ and contact δ costs of targeting participants who are true and false would-be churners. Eqs. 1 and 3 are analogous. However, it is expected that the profit of a student dropout classifier depends on the acceptance rate of the program. Finally, the optimal cutoff T where the profit of the classifier is maximized can be estimated by calculating $M P = P ( T ; \gamma , \sigma ,$ $b , \delta , \phi )$ , as defined in Section 3. This cutoff also determines the optimal fraction α of the student base that should be invited to participate in the program.

![](/api/attachments/VK6H57ED/fulltext/images/00f23ad655adf153ad4880415b9a812684f6ebaa1dd074ac1b7d3f1250a862eb.jpg)  
Fig. 1. Retention process by selecting a fraction α of the N new students.

Note that the average acceptance rate of the prevention campaign and the effect of the incentive are captured in the profit metric in terms of the parameters γ and $\sigma ,$ respectively. Further research may explore the use of uplift modeling or causal classification methods for learning the individual effect of a campaign on student dropout risk, in terms of both acceptance and effectiveness, to rank students according to their like lihood of accepting the offer and of being retained because of the retention program. Uplift models estimate the incremental effect of an action, also known as a treatment, e.g., tutoring, on the behavior of subjects. The goal is to target persuadables, i.e., students who are most likely to be retained due to the treatment, and avoid applying the treatment to students who may be adversely affected, e.g., those who feel overwhelmed by the additional load of the tutorials and are driven to drop out by the retention campaign. This phenomenon has been observed in the churn prediction literature $[ 3 7 , 3 8 ]$

## 4.2. Student lifetime value

The profit-driven student dropout framework relies on the compu tation of the benefit b that results from the retained students. A general definition of benefits is difficult to obtain, as it depends on several di mensions. From a social perspective, retaining students leads to increasing graduation rates. This generates positive externalities, as living standards may improve due to the gain in human capital.

Our study defines the benefit of dropout prevention in terms of the student lifetime value (SLV). The SLV is analogous to the customer lifetime value (CLV) framework widely used in marketing applications. The CLV is computed as the net present value of future cash flows generated from the individual-organization relationship within a finite time horizon. Based on [39], the CLV can be formally defined as follows:

$$
C L V = \sum_ {t = 0} ^ {\infty} \frac {(p - c) r _ {t}}{(1 + i) ^ {t}} = m \frac {r}{(1 + i - r)},\tag{4}
$$

where at period $t , p$ and c denote the future cash inflows and outflows from subjects, respectively, $r _ { t }$ represents the likelihood of the endurance of the individual-organization relationship and i indicates the discount rate, usually assumed to be the weighted average cost of capital (WACC) [40].

The proposed SLV computes the economic value of a student in the context of HEIs as the net present value of future tuition fees. This approach is applicable to private HEIs, which largely rely on tuition fees as a source of income, as well as to tuition-free HEIs.

We redefine Eq. 4 to the context of student dropout. First, the time horizon is known, as it can be calculated on the basis of the academic periods predefined for a given program or can be measured based on the average duration for students in the program. Second, the likelihood of the endurance of the individual-organization relationship is commonly computed by HEIs, as it must be reported for certification purposes. We formally defined the SLV as follows:

$$
S L V = \sum_ {t = 1} ^ {T} \frac {\left(p _ {t} - c _ {t}\right) \left(r _ {t}\right) ^ {t - 1}}{\left(1 + r\right) ^ {t - 1}}.\tag{5}
$$

Let $p _ { t }$ and $c _ { t }$ be the tuition fee and the marginal cost of functioning at period t. Unlike in Eq. 4, the retention rate $r _ { t }$ is taken from the preceding period, $\mathrm { e . g . }$ , for $t = 1$ , the retention $r _ { t - 1 }$ is calculated as one less the portion of students enrolled at the beginning of period $t - 1$ and leaving the program at the beginning of period t. It is assumed that $r _ { t }$ increases as the student approaches the graduation period T.

## 5. Experimental design

This section describes the educational context of the case study, the retention program, the datasets, and the data preprocessing. Next, the findings of the experiments are discussed based on the proposed profit driven evaluation framework. The MP and SLV are used to assess model performance and to determine the optimal fraction of students to be targeted.

## 5.1. The academic support program and MP parameters

We apply the proposed framework to data from a Chilean HEI. The HEI participates in the National Admission Process (NAP), which con sists of fairly assigning students to each HEI according to (1) the Stan dard Admission Test (SAT) and (2) the Application Procedure (AP). The SAT evaluates students in the fields of mathematics, language, history, and science. In contrast, the AP is an application process where students can apply to more than one program offered by the HEI members of the NAP, indicating an ordinal preference. Then, the AP assigns students to each program based on SAT scores, high school performance, and preferences. For the particular case of the HEI in our study, the number of admissions is approximately 670 every year.

The student dropout prevention program designed by the HEI con sists of an academic support program (ASP) run since 2012. The ASP aims to prevent academic failures in the second and third semesters, i.e., it focuses on freshmen, by providing a set of tutorials that are given by students from advanced semesters. Although all new students are invited to participate in the ASP at the beginning of each semester, only a fraction accept the invitation. Nonetheless, generally, the number of applications exceeds the available slots, and acceptance is defined based on expert judgment. Therefore, the aim of our framework is to support ASP program designers and managers by providing a data-driven approach that prioritizes students who are most likely to drop out.

The SLV is calculated as shown in Eq. 5. We assume a time horizon of 5 years, which is the expected time until graduation. We compute for each year $t \in \{ 1 , 2 , 3 , 4 , 5 \}$ and bachelor’s program $b \in \{ b _ { 1 } , b _ { 2 } , b _ { 3 } \} _ { \mathrm { ; } }$ , the SLV input parameters, $p _ { t } ^ { b } , c _ { t } ^ { b } ,$ , and $r _ { t \cdot } ^ { b } . \mathrm { T h e } p _ { t } ^ { b } - c _ { t } ^ { b }$ values are considered to be similar for each period t. Table 2 presents the survival ratios $r _ { t } ^ { b }$ of each bachelor’s program and period.

Table 2 shows that the r values for all programs are 100% at $t =$ $^ { \{ 1 , 4 , 5 \} }$ . From our data, we observed no dropouts for the two last years, and we filtered out cases in which the students left the HEI before the first semester. The discount rate r was set based on the list of WACC values for the educational sector provided by [40], i.e., 9.42% for 2019. We assume that the social benefit of retained students, i.e., graduated students, is equal to the value of the tuition fee. Tuition fees are charged by all HEIs in Chile, but the government sponsors students within the bottom 60% of the income distribution.

The SLV that results from considering the tuition fee of the different programs and the above mentioned parameters is 11,744.69 EUR. Then, the parameters of our proposed evaluation metric (Eq. 3) are set as follows: benefit $\boldsymbol { b } = \boldsymbol { S } \boldsymbol { L } \boldsymbol { V } ,$ acceptance ratio $\gamma = 0 . 5 2 ,$ , contact cost $C _ { c } = 1$ EUR, and program participation cost $C _ { i } = 1 6 . 7 7 ~ \mathrm { E U R }$ . The value for γ is computed based on our data. Currently, 52% of the students accept the invitation to participate in the programs. The $C _ { c }$ and $C _ { i }$ costs were pro vided by the managers of the ASP and are in accordance with the literature on profit metrics. We compute the proposed MP measure on a set of different values for the success rate of the program $\sigma , \mathrm { i . e . , } \sigma =$ $\left\{ 0 . 0 1 , 0 . 0 2 , 0 . 0 3 , . . . , 0 . 1 5 \right\}$ , as this allows us to assess the change in terms of the net profit of the dropout model under different scenarios.

## 5.2. Experimental setup

The dataset spans the period from 2012 to 2016 and includes 3,362 observations explained by 51 features. The attributes are collected from various sources, such as the program enrollment process, prema triculation data, and academic performance after the first semester. Specifically, the prematriculation data consist of variables on family background $( \boldsymbol { \mathrm { e . } } \boldsymbol { \mathrm { g . } } ,$ , head of family, parents’ educational level, and num ber of parents who are alive), high school characteristics (e.g., funding type school, gender-type school, and governance-type school), socio demographic variables (e.g., region of residence, income level, and working-activity state), and the admission process $( \boldsymbol { \mathrm { e . } } \boldsymbol { \mathrm { g . } }$ , SAT scores and AP preferences). Academic performance features refer to the number of courses taken, the aggregated grade point average (GPA), and the GPA by topic (mathematics, economics, statistics, and English). Finally, the outcome variable $Y \in \{ 0 , 1 \}$ indicates whether the student drops out in the second or third semester.

Table 2  
Survival ratio for the three bachelor programs (b1, b2, and b3) at different time periods.

<table><tr><td>Program</td><td>t = 1</td><td>t = 2</td><td>t = 3</td><td>t = 4</td><td>t = 5</td></tr><tr><td>b1</td><td>100%</td><td>69.4%</td><td>85%</td><td>100%</td><td>100%</td></tr><tr><td>b2</td><td>100%</td><td>78.8%</td><td>83.7%</td><td>100%</td><td>100%</td></tr><tr><td>b3</td><td>100%</td><td>90.5%</td><td>94.9%</td><td>100%</td><td>100%</td></tr><tr><td>Total</td><td>100%</td><td>87.6%</td><td>94.6%</td><td>100%</td><td>100%</td></tr></table>

Note that we do not distinguish between voluntary and involuntary dropout, $\mathbf { e . g . , }$ academic suspension, as these are difficult to disentangle at the early stage at which we predict dropouts. For example, some voluntary dropouts occur when students expect that they may be sus pended due to poor performance. This suggests a dependency between voluntary and involuntary dropouts, and hence, we consider both types of dropouts in our study.

We implemented three preprocessing strategies on the original dataset. First, 72 records were removed, as these students were accepted into the AP but did not attend any course. Second, we removed variables related to the performance in statistics courses - 1st semester and the work schedule as more than 90% of observations had an unknown value. At tributes with relatively few missing values were imputed based on the data type, i.e., numerical or categorical, and the number of missing values. Numeric features were assigned the conditional average given the entry year. Observations in categorical variables were grouped by year-cohort, and missing values were imputed with the mode if the proportion of missing values was less than 10%; otherwise, the unknown level was assigned. Finally, all categorical variables were dummy coded, and the entire dataset was normalized. This resulted in a total of 88 features and 3,290 observations.

Seven machine learning algorithms were selected, all of which have been evaluated in the literature to predict student dropout [4,8,41]. These methods are available in the caret package in R. Table 3 lists the methods and their default settings used in this study. Note that the kernel parameter $\gamma$ is estimated by using the kernlab package, remaining constant in the tuning procedure for the svmRadial method.

We follow the traditional profit framework [10,34] and apply hyperparameter tuning based on 5-fold cross-validation with the area under the ROC curve (AUC) as the performance evaluation metric. The AUC is considered to be a good measure for hyperparameter tuning, including when the objective is to maximize profitability. In particular, it evaluates performance across all possible thresholds in a single aggregate measure. This yields a more robust approach for optimizing model performance than measures such as accuracy, top-decile lift, and maximum profit, which evaluates model performance at a single, spe cific threshold.

Note that the goal of adopting a profit measure is to post-process a classification model, i.e., to evaluate and compare the predictive per formance and eventually select a classification model and classification threshold. An interesting avenue for further research is to evaluate whether adopting more complex approaches leads to improvements in profitability, for example, by using profit as the evaluation criterion for hyperparameter tuning [42] or by employing profit-driven learning approaches, such as those presented by [43,44]. Incorporating the evaluation metric that is proposed in this study in the learning stage of a predictive model of student dropout is beyond the scope of this paper but marked as a prime topic for further research.

Table 3  
Models and tuning parameters used in this study (default caret configuration)

<table><tr><td>Model</td><td>Tuning parameters</td></tr><tr><td>Generalized Linear Model (glm)</td><td>No tuning parameters</td></tr><tr><td>k-Nearest Neighbors (knn)</td><td>k: numbers of neighbors $k = \{5,7,9,11,13,15,17,19,21,23\}$ </td></tr><tr><td>CART (rpart)</td><td>cp: complexity parameter $cp = \{0.00453,0.00996,0.11684\}$ </td></tr><tr><td>Random Forest (rf)</td><td>mtry: randomly selected predictors $mtry = \{2,8,14\}$ </td></tr><tr><td>Neural Network (nnet)</td><td>size: hidden units $size = \{1,3,5\}$ decay: weight decay $decay = \{0,0.001,0.1\}$ </td></tr><tr><td>SVM with Linear Kernel (svmLinear)</td><td>C: regularization parameter $C = \{0.25,0.5,1.00\}$ </td></tr><tr><td>SVM with Radial Basis Function</td><td> $\gamma$ : Inverse kernel width $\gamma = \{0.08132051\}$ </td></tr><tr><td>Kernel (svmRadial)</td><td> $C = \{0.25,0.50,1.00\}$ </td></tr></table>

In addition, we use the synthetic minority oversampling technique (SMOTE) [45] as the resampling method since the class imbalance ranges between 15 and 20%. SMOTE is considered the industry standard for class-imbalance classification thanks to its positive predictive per formance [29].

We use the feature selection approach as implemented in [46] to train the models with a reduced set of attributes. First, the dataset is split into training and testing sets in a 2/3 to 1/3 proportion, respectively. In a second step, the number of variables is iteratively reduced by using an input selection procedure based on a backward wrapper approach. Starting with k features, in the first iteration, k models are trained, where each model excludes one of the variables. The variable set yielding the model with the best performance is selected, and the pro cedure is repeated with the remaining k − 1 variables. This process continues until a single variable is left. Since the backward wrapper approach is computationally expensive, a filter is implemented before running the selection procedure. We used the Fisher score [47] to filter each variable (see Eq. (6)), where $\overline { { x } } _ { Y = j }$ and $s _ { Y = j } ^ { 2 }$ are the mean and stan dard deviation, respectively, for each class j ∈ {0,1}. Then, we select the 20 features with the highest Fisher scores. According to [46], this number of variables is sufficient for obtaining good predictive power.

$$
F i s h e r \quad s c o r e = \frac {\left| \overline {{x}} _ {Y = 0} - \overline {{x}} _ {Y = 1} \right|}{\sqrt {s _ {Y = 0} ^ {2} + s _ {Y = 1} ^ {2}}}\tag{6}
$$

The final feature selection step consists of a backward elimination process in which the least relevant attributes were removed using lo gistic regression as a base classifier. This procedure has been considered previously in the context of business analytics, resulting in a good complement to a filter method [48]. This step yields 13 variables to be used in the classification models.

Finally, we train a total of 28 predictive models and report their results with and without resampling (RS) and/or feature selection (FS)

![](/api/attachments/VK6H57ED/fulltext/images/da2fc00f35304ccdc6f977311936d74aa7097b5f5809c3902e54420d54554e43.jpg)  
(a) Max MP for each $\sigma .$ Linear Scale.

for completeness.

## 5.3. Results & discussion

We report the results of our experiments in terms of the targeted fraction of students, i.e., parameter α in $\operatorname { E q . 3 , }$ and the MP of the model based on the benefits and costs associated with the ASP program. Moreover, the value of the σ parameter is varied, i.e., $\sigma = \{ 0 . 0 1 , 0 . 0 2$ $\ldots , 0 . 1 5 \}$ , leading to a total of 28 different models.

The values of the parameter σ indicate the different scenarios that a decision-maker should consider, as variations in σ directly influence the MP of a model. Fig. 2 depicts the best MPs obtained for the 150 sce narios. We observed that MP is positively correlated with $\sigma ,$ as increases in σ lead to higher MP values. Nonetheless, at lower σ values, the vari ation in the MP is higher, i.e., in the range of $3 - 4 \%$

The targeting decision entails offering the ASP to the optimal fraction of students, as the potential benefit of retaining students should offset the targeting- and campaign-related costs. Fig. 3 depicts the minimal α for a defined MP value. The intuition is that targeting a smaller fraction of true would-be churners leads to cost reductions in the implementation of the ASP, hence, a larger profit. We observe that the MP does not in crease at α values larger than 85%. That is, the highest MP (15,050 EUR) is reached when targeting 85% of the student base. Therefore, targeting the total student base does not necessarily lead to profit maximization. Moreover, the smallest fraction of students is also optimal for larger values of σ and MP, i.e., 5% and 15,050, respectively. Based on these findings, we suggest refraining from targeting more than 85% of the student base. These results are consistent with the study by [49], where the authors conclude that the ASP can negatively affect students who are less likely to be retained by the program. It is important to note that our goal is not to prevent students from benefitting from tutorials but rather to design customized programs for those who are more likely to be retained. The programs will remain open for any student who would like to participate in them.

We analyzed the α values as a function of σ since the costs of the ASP are related to the fraction α. Fig. 3 depicts the α values that were obtained from the 28 models under all the different scenarios. The bold curve represents the α with the highest MP (the optimal α). By contrast, the gray area shows the α values for which a lower profit is obtained. Note that the optimal α in Fig. 3 is reached at a similar threshold, as shown in Fig. 4. The optimal α does not change for σ values larger than 4% and equals the minimum MP value for thresholds above 5%. Moreover, as the success rate of the program increases, it is profitable to target as many students as possible up to a certain point. This is because the α for which the highest MP is obtained never reaches a value of 1. Finally, the optimal α is very close to the dropout rate between periods 1 and 2 (see Table 2).

![](/api/attachments/VK6H57ED/fulltext/images/f0281c63e03cb68fad496ee74bfd5f6f2805fd93115f427788a01cb9f6eabf1f.jpg)  
(b) Max MP for each $\sigma .$ . Logarithmic Scale.  
Fig. 2. Maximum MP for each σ value. For better visual analysis, we also plot the MP by transforming axis y into a logarithmic scale.

![](/api/attachments/VK6H57ED/fulltext/images/ae5560148cd77592473b66acffc9ae9962740a0a9fa77b236a5c74f6396e6906.jpg)  
(a) Minimum α for increasing MP values.

![](/api/attachments/VK6H57ED/fulltext/images/4932bc4b7295921710094aced9d16559a5a9a137f0922907c06a2057364f2a66.jpg)  
(b) Optimal α for increasing σ values.  
Fig. 3. (a) α as a function of MP values and (b) α as a function of σ values. The y axis in (a) was transformed by using the log function to improve visualization.

We train different models at different σ values and compare their performance in terms of MP (Figs. 4 and 5). The MP values are scaled to lie within the range [0,1], where 1 is the maximum MP value among the 28 models for each given σ. This transformation allows us to assess the relative performance of each model in terms of MP. We observe that the svmRadial model outperforms the majority of machine learning tech niques for σ values greater than $3 \mathrm { ~ - ~ } 3 . 5 \%$ in three of the four groups depicted in Figs. 4 and 5. At smaller σ values, none of the models excels. Note that the knn classifier performs relatively poorly.

Table 4 illustrates the MP and the optimal α value of the 28 models when σ is set to 0.15. As expected, the svmRadial model without FS and SMOTE outperforms other models in terms of the MP. Note that svmRadial achieves the largest MP by targeting a smaller fraction α of the student base. The results suggest that offering the retention program on the basis of a predictive model, i.e., svmRadial, can increase the net benefit of the ASP program, as targeting a subsample of the student base is naturally less expensive. Particularly, assuming that the success rate of the ASP is σ = 15%, targeting all the student base would result in an MP of 66.25 thousand euros, which is lower than the MP that is achieved when targeting a subsample of students according to the svmRadial model, i.e., MP is equal to 67.33 thousand euros.

![](/api/attachments/VK6H57ED/fulltext/images/d9068681f8ec2b5fe0e4e28f50d94f07eaeacecf0e1ee2b282748cc94f7ae4de.jpg)  
(a) Models' MP, no SMOTE or FS.

In addition, we created two student profiles according to the best model (svmRadial) and the optimal threshold of σ. The two profiles correspond to students who should be targeted and those who should not be invited to the ASP. We averaged the features for each segment and compared the attributes with the largest differences. Fig. 6 shows a radar chart with the respective profiles. This representation is appropriate for decision-making, as it facilitates model interpretability.

We observe in Fig. 6 that students with poor performance in the first semester and who graduated from private schools should be prioritized when offering the ASP, according to the dropout predictive model. Furthermore, the figure shows that we should focus on students with higher household income and those from private schools. Based on this finding, we cannot conclude that there is a relationship between household income and dropouts. In contrast, we attempt to emphasize the utility of using visualization tools to make the results of classification models more interpretable for retention program designers. Depending on the context, one could assume that students from private schools may be less engaged with public institutions, as they may feel less attracted by their environment and social life. Nonetheless, our model considers the same SLV for all students, regardless of their household income.

![](/api/attachments/VK6H57ED/fulltext/images/ad24ac0cf18da89752c4c1b4ba0cfcd798fe339d5d19cf14cc96096f461d0fb9.jpg)  
(b) Models’MP with FS.  
Fig. 4. Models’ MP for each σ (Part 1)

![](/api/attachments/VK6H57ED/fulltext/images/c672543a655aaa2b55dab1372f80c6b2d6df672c36678feaea1f7ae8bb01b502.jpg)  
(a) Models'MP with SMOTE.

![](/api/attachments/VK6H57ED/fulltext/images/e52d18b0a561094bce28b1919c3d2a380a516d4b73968a94af0bc3ed5f7c9a5f.jpg)  
(b) Models' MP with FS and SMOTE.  
Fig. 5. Models’ MP for each σ (Part 2).

Performance in terms of MP and optimal α for the various classification methods with and without feature selection (FS) and resampling (RS). The MP values are expressed in thousands of euros.

<table><tr><td>Method</td><td>FS</td><td>RS</td><td>FS &amp; RS</td><td>NoFS &amp; NoRS</td></tr><tr><td rowspan="2">rpart</td><td>$66.25</td><td>$66.28</td><td>$66.29</td><td>$66.25</td></tr><tr><td>100%</td><td>99.6%</td><td>99.5%</td><td>100%</td></tr><tr><td rowspan="2">rf</td><td>$66.36</td><td>$66.48</td><td>$66.46</td><td>$66.50</td></tr><tr><td>98.5%</td><td>96.7%</td><td>97.0%</td><td>96.4%</td></tr><tr><td rowspan="2">knn</td><td>$66.35</td><td>$66.30</td><td>$66.29</td><td>$66.44</td></tr><tr><td>98.6%</td><td>99.3%</td><td>99.5%</td><td>97.2%</td></tr><tr><td rowspan="2">glm</td><td>$66.40</td><td>$66.26</td><td>$66.52</td><td>$66.26</td></tr><tr><td>97.8%</td><td>99.9%</td><td>96.1%</td><td>99.9%</td></tr><tr><td rowspan="2">nnet</td><td>$66.39</td><td>$66.65</td><td>$66.45</td><td>$66.27</td></tr><tr><td>98.1%</td><td>94.4%</td><td>97.1%</td><td>99.7%</td></tr><tr><td rowspan="2">svmLineal</td><td>$66.28</td><td>$66.33</td><td>$66.44</td><td>$66.33</td></tr><tr><td>99.6%</td><td>98.9%</td><td>97.2%</td><td>98.9%</td></tr><tr><td rowspan="2">svmRadial</td><td>$66.35</td><td>$66.86</td><td>$66.69</td><td>*$67.33</td></tr><tr><td>98.6%</td><td>91.3%</td><td>93.8%</td><td>*84.7%</td></tr></table>

Note that the incorrect interpretation of such a model may have regressive effects. Our main goal is to learn the differences among stu dents in terms of their likelihood of dropping out and provide guidance for an adequate implementation of tailored programs. One possible so lution is to deploy two different programs (one for the invite group and another for the do not invite group) with different contents and focus. This suggestion was made to the heads of the ASP to reduce the risk of regressive decisions.

Alternatively, fairness can be promoted via algorithmic modifica tions, such as thresholding or the inclusion of fairness constraints in model training [50]. This, however, requires further research.

## 6. Conclusions

The performance of classification methods has historically been assessed by statistical measures that ignore the benefits and costs of the decision-making process [9]. This may not be the best course of action when we are able to quantify the consequences of a classification approach when implemented. This is the case in business analytics, where the profit of a model can be computed to make the best choice of the classification technique.

In this study, we extend the reasoning behind profit metrics for churn prediction in telecommunications to the student dropout challenge. We establish a parallel between the two tasks, which have similarities but also important differences, for the definition of a goal-oriented evalua tion metric. The first key difference is that traditional churn prediction assumes that all targeted would-be churners that accept a monetary incentive are retained. This is not the case in student dropout because the retention efforts are only partially effective. In addition, the in centives in education contexts are mostly nonmonetary but rather sup port programs such as tutorials, psychological assistance, and mentoring. This makes our proposed measure more complex since it includes an additional parameter σ that represents the fraction of true would-be dropouts who accept participation in the program and are effectively retained. In this sense, our proposal can be seen as a multi purpose profit metric in which the retention campaign cannot be considered completely successful. Our proposal also contains the MP measure since both are equivalent when σ = 1. Similarly, our proposal does not assume that all targeted students will accept the incentive since it does not provide a direct benefit for them. Indeed, we calibrated the model on a case study in which all students were invited to be part of these tutorials, but only a fraction of them accepted the invitation.

![](/api/attachments/VK6H57ED/fulltext/images/da3af4a1ed267af11011ef25122d8ca810e30e7219422f6cc8ea62ba84004f1f.jpg)  
Fig. 6. Profile of students who should be invited vs. those who should not.

The second key difference is the use of CLV values for quantifying the benefit of retaining churners. Although tuition fees can be used to esti mate a ‘lifetime value’ for students, this approach may not be suitable in public and some private institutions. In this study, we justify this strat egy by the fact that the Chilean government sponsors the tuition fees for those students who belong to the bottom 60% of Chile’s income distri bution. This is equivalent to assuming that the government values a retained student who becomes a professional as a benefit to society in the same way as tuition fees. Under this assumption, we were able to estimate the net social benefit of a retention program when using a given classification function.

A case study on data from three bachelor’s programs from a Chilean university demonstrates the virtues of the proposed metric. Our findings suggest that offering a tailored retention program on the basis of the best predictive model can significantly improve on current practices. The current approach targets the entire student base $( \alpha = 1 )$ , which does not allow the design of customized programs based on the attributes of the targeted group. In this sense, we seize the resources that data science provides for interpreting our results and understanding those factors to gain insights into the application. As a recommendation, we suggested that the ASP design programs tailored to students with low academic performance in the first semester, specifically in mathematics and eco nomics, and who graduated from private schools. Finally, unlike pre vious studies, our results show that feature selection [see 10] and balancing techniques do not necessarily lead to larger gains [see $\mathrm { e . g . , 4 , }$ $2 9 , 4 1 ]$

One limitation of the present study and profit metrics in general is that they do not take into account the uplift of the model. As a possible future development, we believe that uplift modeling can be effectively combined with the use of profit metrics, extending a previous study we designed for uplift modeling for student dropout [49]. Additionally, as discussed in Section 2, the literature on student dropout has demon strated that the results obtained from the implementation of data mining techniques could differ across HEI contexts; therefore, future research could consider the development and implementation of the proposed performance metric approach to enrich disciplinary development in the study of student dropout.

## Acknowledgements

The first author gratefully acknowledges financial support from ANID, PIA/BASAL AFB180003, and FONDECYT-Chile, grant 1200221. The third author acknowledges the support of Innoviris, the Brussels Region Research funding agency.

## References

[1] K. Coussement, M. Phan, A. De Caigny, D.F. Benoit, A. Raes, Predicting student dropout in subscription-based online learning environments: the beneficial impact of the logit leaf model, Decis. Support. Syst. 135 (2020) 113325.

[2] D. Delen, K. Topuz, E. Eryarsoy, Development of a bayesian belief network-based dss for predicting and understanding freshmen student attrition, Eur. J. Oper. Res. 281 (3) (2020) 575–587

[3] N. Sutter, S. Paulson, Predicting college students’ intention to graduate: a test of the theory of planned behavior, Coll. Stud. J. 50 (3) (2017) 409–421.

[4] J. Vasquez, ´ J. Miranda, Student desertion: What is and how can it be detected on time?, in: Data Science and Digital Business Springer, 2019, pp. 263–283.

[5] K. Dejaeger, F. Goethals, A. Giangreco, L. Mola, B. Baesens, Gaining insight into student satisfaction using comprehensible data mining techniques, Eur. J. Oper.

[6] C. Masci, G. Johnes, T. Agasisti, Student and school performance across countries: a machine learning approach, Eur, J. Oper, Res, 269 (3) (2018) 1072–1085.

[7] V. Migu´eis, A. Freitas, P.J. Garcia, A. Silva, Early segmentation of students according to their academic performance: a predictive modelling approach, Decis.

[8] D. Delen, Predicting student attrition with data mining methods, Journal of College

[9] D. Hand. Measuring classifier performance: a coherent alternative to the area under

[10] W. Verbeke, K. Dejaeger, D. Martens, J. Hur, B. Baesens, New insights into churn prediction in the telecommunication sector: a profit driven data mining approach, Eur. J. Oper. Res. 218 (1) (2012) 211–229.

[11] W. Verbeke, B. Baesens, C. Bravo, Profit Driven Business Analytics, Wiley, 2017.

[12] J.M. Braxton, A.V. Shaw Sullivan, R.M. Johnson, Appraising tinto’s theory of college student departure, Higher Education-New York-Agathon Press Incorporated 12 (1997) 107–164.

[13] J.P. Bean, Dropouts and turnover: the synthesis and test of a causal model of student attrition, Res. High. Educ. 12 (2) (1980) 155–187.

[14] W.G. Spady, Dropouts from higher education: an interdisciplinary review and synthesis, Interchange 1 (1) (1970) 64–85.

[15] V. Tinto. Dropout from higher education: a theoretical synthesis of recent research Rev. Educ. Res, 45 (1) (1975) 89–125

[16] V. Tinto, Limits of theory and practice in student attrition, J. High. Educ. 53 (6) (1982) 687–700.

[17] B.M. Kehm, M.R. Larsen, H.B. Sommersel, Student dropout from universities in europe: a review of empirical literature, Hungarian Educational Research Journal 9 (2) (2019) 147–164.

[18] D.R. Lillard, P.P. DeCicca, Higher standards, more dropouts? Evidence within and across time, Econ. Educ. Rev. 20 (5) (2001) 459–473.

[19] L. Aulck, N. Velagapudi, J. Blumenstock, J. West, Predicting student dropout in higher education, Preprint arXiv 1606.06364 (2016).

[20] A.L. Caison, Analysis of institutionally specific retention research: a comparison between survey and institutional database methods, Res. High. Educ. 48 (4) (2007) 435–451.

[21] B.I. Mallette, A.F. Cabrera, Determinants of withdrawal behavior: an explorator study, Res. High. Educ. 32 (2) (1991) 179–194.

[22] C.H. Yu, S. DiGangi, A. Jannasch-Pennell, C. Kaprolet, A data mining approach for identifying predictors of student retention from sophomore to junior year, Journa of Data Science 8 (2) (2010) 307–325

[23] A. Fortin, L. Sauv´e, C. Viger, F. Landry, Nontraditional student withdrawal from undergraduate accounting programmes: a holistic perspective, Acc. Educ. 25 (5) (2016) 437–478.

[24] M. Ferreira, Gender issues related to graduate student attrition in two science

[25] M.L. Van Vonderen, R. Bekkers, R. Hermanussen, G. Sikora, A. Toth, ´ Gender and doubts about study in technology: a dutch-hungarian comparison, J. Gen. Psychol. 123 (1) (1996) 5–18

[26] S.V. Magdalena, An adaptation of tinto’s attrition model to the universidad catolica´ de la santísima concepcion, ´ chile, Argos 33 (65) (2016).

[27] D.S. Chaplot, E. Rhim, J. Kim, Predicting student attrition in moocs using sentiment analysis and neural networks, in: AIED workshops, Vol. 53 (2015) 54–57.

[28] A. Sangodiah, P. Beleya, M. Muniandy, L.E. Heng, Ramendran SPR, Minimizing student attrition in higher learning institutions in Malavsia using support vector machine. Journal of Theoretical & Applied Information Technology 71 (3) (2015)

[29] D. Thammasiri, D. Delen, P. Meesad, N. Kasap, A critical assessment of imbalanced class distribution problem: the case of predicting freshmen student attrition. Expert Syst, Appl. 41 (2) (2014) 321–330.

[30] M. Sweeney, J. Lester, H. Rangwala, Next-term student grade prediction, in: 2015 JEEE International Conference on Big Data (Big Data). JEEE. 2015. pp. 970–975.

[31] R.S. Baker, A.T. Corbett, V. Aleven, Improving contextual models of guessing and slipping with a truncated training set, Jun 2018.

[32] A. Elbadrawy, A. Polyzou, Z. Ren, M. Sweeney, G. Karypis, H. Rangwala, Predicting student performance using personalized analytics, Computer 49 (4) (2016) 61–69.

[33] S.A. Neslin, S. Gupta, W. Kamakura, J. Lu, C.H. Mason, Defection detection: measuring and understanding the predictive accuracy of customer churn models. J. Mark, Res, 43 (2) (2006) 204–211

[34] T. Verbraken, W. Verbeke, B. Baesens, A novel profit maximizing metric for measuring classification performance of customer churn prediction models. IEFE Trans Knowl Data Eng, 25 (5) (2012) 961–973

[35] T. Verbraken, C. Bravo, R. Weber, B. Baesens, Development and application of consumer credit scoring models using profit-based classification measures, Eur. J. Oper. Res. 238 (2) (2014) 505–513

[36] M. Oskarsd<sup>´</sup> otir, ´ C. Bravo, W. Verbeke, C. Sarraute, B. Baesens, J. Vanthienen, Social network analytics for churn prediction in telco: model building, evaluatior and network architecture, Expert Syst, Appl, 85 (2017) 204–220.

[37] E. Ascarza, R. Iyengar, M. Schleicher, The perils of proactive churn prevention using plan recommendations: evidence from a field experiment, J. Mark. Res. 5 (1) (2016) 46–60.

[38] F. Devriendt, J. Berrevoets, W. Verbeke, Why you should stop predicting customer churn and start using uplift models, Inf. Sci. 548 (2019) 497–515.

[39] S. Gupta. D. Hanssens. B. Hardie, W. Kahn. V. Kumar. N. Lin. N. Ravishanker S. Sriram, Modeling customer lifetime value, J. Sery. Res. 9 (2) (2006) 139–155

[40] A. Damodaran, Cost of Capital by Sector (US), http://people.stern.nyu.edu/ada modar/New\_Home\_Page/datafile/wacc.htm, accessed: 2020-06-13 (jan 2020).

[41] D. Delen. A comparative analysis of machine learning techniques for student retention management, Decis, Support, Syst, 49 (4) (2010) 498–506

[42] S. Maldonado, A. <sup>´</sup> Flores, T. Verbraken, B. Baesens, R. Weber, Profit-based feature selection using support vector machines–general framework and an application for customer retention, Appl. Soft Comput. 35 (2015) 740–748.

[43] S. Hoppner. E. Stripling, B. Baesens, S. vanden Broucke, T. Verdonck, profit driven decision trees for churn prediction, Eur, J. Oper, Res, 284 (3) (2020) 920–933

[44] S. Maldonado, J. López, C. Vairetti, Profit-based churn prediction based on

[45] N.V. Chawla, K.W. Bowyer, L.O. Hall, W.P. Kegelmeyer, Smote: synthetic minority over-sampling technique, J. Artif, Intell. Res, 16 (2002) 321–357

[46] W. Verbeke, K. Dejaeger, D. Martens, J. Hur, B. Baesens, New insights into churn prediction in the telecommunication sector: a profit driven data mining approach, Eur. J. Oper. Res. 218 (1) (2012) 211–229.

[47] R. Duda, P. Hard, D. Stork, Pattern Classification, Wiley-Interscience Publication, 2001.

[48] C. Bravo, S. Maldonado, R. Weber, Methodologies for granting and managing loans for micro-entrepreneurs: new developments and practical experiences, Eur. J. Oper. Res. 227 (2) (2013) 358–366.

[49] D. Olaya, J. V´asquez, S. Maldonado, J. Miranda, W. Verbeke, Uplift modeling for preventing student dropout in higher education, Decis. Support. Syst. 134 (2020) 113320.

[50] G. Pleiss, M. Raghavan, F. Wu, J. Kleinberg, K.Q. Weinberger, On fairness and calibration, in: Proceedings of the 31st International Conference on Neural Information Processing Systems, NIPS’17, Curran Associates Inc., 2017, pp. 5684–5693.

![](/api/attachments/VK6H57ED/fulltext/images/1c45765c0523c623bfd054adf4fd2c68fdf0757b562b1a0acb74666b8d143c8a.jpg)  
Sebastian ´ Maldonado received his B.S. and M.S. degree from the University of Chile in 2007 and his Ph D. degree from the University of Chile, in 2011. He is currently Full Professor at the Department of Management Control and Information Systems, School of Economics and Business. University of Chile, His research interests include statistical learning, data mining and business analytics. Sebasti´an Maldonado has published more than 70 scientific contributions including more than 50 Web of Science (WoS) papers in the last ten years.

![](/api/attachments/VK6H57ED/fulltext/images/522d1d2826299b871af3e73b0477ada0e2537cbe6dd80da945c7cbcac2f58f17.jpg)

![](/api/attachments/VK6H57ED/fulltext/images/1fa17847cdbafe11ca32125e46f3c6b0f0c94858b72ce4e4b38cb487a721a769.jpg)

![](/api/attachments/VK6H57ED/fulltext/images/f4677ee8a29a7836a051cf7d6bb6bffed5b6da4aab2d172b4ffef5323ae162b2.jpg)

Jaime Miranda is currently Associate Professor and Head at the Department of Management Control and Information Sys: tems, University of Chile. He has an Industrial Engineer B.S. degree, a M.S. degree in Operations Management and a PhD. degree in Engineering Systems from the University of Chile. In 2016 was president of the Association of Latin-Iberoamerican Operational Research Societies (ALIO). His research interests include Operation Research and Business Analytics. He ha published several articles and implemented OR systems in Chile.

![](/api/attachments/VK6H57ED/fulltext/images/04980b1625d615043f3222ffffb90eb168a8c5389fa1dd75da2876633af53146.jpg)

Diego Olava is a Ph.D. candidate at the Vrije Universiteit Brussel. He received his bachelor's degree in Economics from the Universidad Nacional de Colombia, and he holds a M.Sc. in Management Science from the Vrije Universiteit Brussel (VUB). His research interests include business analytics, data mining, and the intersection of machine learning and causal inference.

Jonathan Vasquez ´ received his B.S. and M.S. degree from the University of Chile in 2012 and 2016 respectively. He is currently academic at Ingenieria en Informacion ´ y Control de Gestion, ´ Escuela de Auditoría, Universidad de Valparaiso. His research focuses on the application of data mining and machine learning in student desertion, students’ performance, educa tional data science, and profiles classification

Wouter Verbeke, pH.D., is associate professor of data science at KU Leuven, Belgium. He obtained a Ph.D. in applied eco nomics at KU Leuven in 2012. His research is situated in the field of causal machine learning and profit-driven data ana lytics and is driven by real-life business applications in fraud. customer relationship, credit risk, supply chain, and human resources management. In 2014, he won the distinguished EURO award for best article published in the European Journal of Operational Research in the category ‘Innovative Applica tions of O.R. His work has been published in established in ternational scientific journals such as IEEE Transactions on Knowledge and Data Engineering, Information Sciences and European Journal of Operational Research. He has authored two books, entitled ‘Fraud Analytics Using Descriptive, Pre dictive & Social Network Techniques’ and ‘Profit-driven Busi ness Analytics', published by Wiley.
