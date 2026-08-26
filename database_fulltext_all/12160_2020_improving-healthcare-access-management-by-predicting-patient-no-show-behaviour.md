---
otero_id: 12160
otero_key: "ZWMJ7CBY"
title: "Improving healthcare access management by predicting patient no-show behaviour"
authors: "David Barrera Ferro; Sally Brailsford; Cristián Bravo; Honora Smith"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113398"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Improving healthcare access management by predicting patient no-show behaviour

![](/api/attachments/ZWMJ7CBY/fulltext/images/69981a49ad3b288e61a87b62e9723f95dca3bd9d12a611d9e208caf6ae0f4887.jpg)

David Barrera Ferro<sup>a,b,⁎</sup>, Sally Brailsford<sup>a</sup>, Cristián Bravo<sup>c</sup>, Honora Smith<sup>d</sup>

<sup>a</sup> Southampton Business School, University of Southampton, Southampton, United Kingdom

<sup>b</sup> Industrial Engineering Department, Pontificia Universidad Javeriana, Bogotá, Colombia

<sup>c</sup> Department of Statistical and Actuarial Sciences, The University of Western Ontario, London, ON, Canada

<sup>d</sup> Mathematical Sciences, University of Southampton, Southampton, United Kingdom

## A R T I C L E I N F O

Keywords: Analytics No-show prediction Healthcare access Design science research

## A B S T R A C T

Low attendance levels in medical appointments have been associated with poor health outcomes and eficiency problems for service providers. To address this problem, healthcare managers could aim at improving attendance levels or minimizing the operational impact of no-shows by adapting resource allocation policies. However, given the uncertainty of patient behaviour, generating relevant information regarding no-show probabilities could support the decision-making process for both approaches. In this context many researchers have used multiple regression models to identify patient and appointment characteristics than can be used as good predictors for no-show probabilities. This work develops a Decision Support System (DSS) to support the implementation of strategies to encourage attendance, for a preventive care program targeted at underserved communities in Bogotá, Colombia. Our contribution to literature is threefold. Firstly, we assess the efectiveness of different machine learning approaches to improve the accuracy of regression models. In particular. Random Forest and Neural Networks are used to model the problem accounting for non-linearity and variable interactions. Secondly, we propose a novel use of Layer-wise Relevance Propagation in order to improve the explainability of neural network predictions and obtain insights from the modelling step. Thirdly, we identify variables explaining no-show, probabilities in a developing context and study its policy implications and potential fot improving healthcare access. In addition to quantifying relationships reported in previous studies, we find that income and neighbourhood crime statistics afect no-show probabilities. Our results will support patient prioritization in a pilot behavioural intervention and will inform appointment planning decisions

## 1. Introduction

High no-show rates are a major issue for health systems. On the one hand, there is a link between low attendance levels and poor health outcomes: consequences include delays in diagnosis and initiation of treatment [1], increased premature mortality rates [2] and increased use of emergency services [3], among others. On the other hand, high no-show rates reduce eficiency for service providers. When a patient fails to keep an appointment, it usually results in a vacant slot that might have been used by another patient [4], increases cost of care [5] and generates idle time for both physicians and consultancy rooms [6]. Consequently, there is a growing interest from the healthcare community in understanding the determinants of no-show behaviour [7] and minimizing its impact [8].

Two main approaches can be used to deal with no-shows in healthcare settings: to improve attendance levels or to minimize impact. The first approach is premised on the idea that it is possible to change patient behaviour. Strategies such as phone reminders [9] and education programs [5] have been successfully implemented in different contexts. According to Zebina et al. [1] a key element in this approach is to be able to correctly identify the patients that should be targeted with each strategy. In contrast, the underlying assumption of the second approach is that such changes in behaviour are unlikely to be achieved, and thus the objective is to minimize the impact of noshows, e.g. by improving the decision-making process regarding resource allocation and scheduling [8]. Given the uncertainty of patient behaviour, generating relevant information concerning no-show probabilities could improve the results of both approaches [10,11].

Good estimates of attendance levels have the potential to improve policy evaluation [12], to minimize undesired efects of resource allocation practices (such as overbooking) [13] and to inform identification of influential stakeholders. This is particularly important considering that one of the main objectives is to generate information that can be used to improve management practices [14]. However, there has been very little discussion in the literature on the trade-ofs between using ‘black box’ approaches (sophisticated analytical methods that would be incomprehensible to most healthcare managers) and more easily interpretable but less accurate approaches such as regression models [15].

Table 1  
No-show studies in primary care settings published since 2017.

<table><tr><td rowspan="2">Reference</td><td rowspan="2">Country</td><td rowspan="2">Sample size</td><td rowspan="2">Method</td><td colspan="5">Appointment variables</td><td colspan="5">Patient variables</td></tr><tr><td>Lead time</td><td>Day</td><td>Distance</td><td>Weather</td><td>Season</td><td>Gender</td><td>No-show history</td><td>Age</td><td>Race</td><td>Marital Status</td></tr><tr><td>[19]</td><td>United Kingdom</td><td>9,177,054</td><td>LR</td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>[23]</td><td>United Kingdom</td><td>2488</td><td>LR</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>[24]</td><td>United States</td><td>18,000,000</td><td>LR</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td>X</td></tr><tr><td>[20]</td><td>United States</td><td>46,710</td><td>Chi-squared</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>[25]</td><td>United States</td><td>2,231,000</td><td>LR</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>[21]</td><td>United Kingdom</td><td>7,351,597</td><td>Chi-squared</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>[28]</td><td>United States</td><td>73,811</td><td>LR/BC/NN</td><td>X</td><td>X</td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td>X</td><td>X</td></tr><tr><td>[15]</td><td>United States</td><td>105,344</td><td>BBN</td><td>X</td><td>X</td><td>X</td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>[3]</td><td>United States</td><td>51,580</td><td>LR</td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td>X</td><td>X</td><td></td></tr><tr><td>[22]</td><td>United States</td><td>509</td><td>LR</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td>X</td></tr><tr><td>[26]</td><td>Taiwan</td><td>2,132,577</td><td>LR</td><td>X</td><td>X</td><td></td><td>X</td><td></td><td>X</td><td>X</td><td>X</td><td></td><td></td></tr></table>

LR: Logistic regression, BC: Bayes Classifier, NN: Neural Networks, BBN: Bayes Behaviour Network.

The context of the study described in this paper is a primary healthcare program targeted at underserved communities in Bogotá, Colombia. Under this program, community workers make home visits to assess health-risk levels and then, if required, schedule medical appointments. Over the two years 2017–2018 the program coverage grew considerably but unfortunately no-show rates for the scheduled medical appointments also grew, reaching levels of 35% and above. Consequently, there was pressure to improve planning processes and use resources more eficiently. In this work, we develop a Decision Support System (DSS) to support the implementation of strategies to reduce no-show rates in this program. It has been argued that in complex problems with multiple variables and fragmented data, informa tion systems have potential to improve resource allocation practices [16] and increase system performance [17]. Hence, the DSS will use routinely collected data and Machine Learning (ML) methods to classify patients in three risk categories (low, medium and high) in terms of their individual no-show probability. Any intervention to encourage attendance will incur a cost, and hence it is more cost-efective to target such interventions at medium and high risk patients.

We adopt the Design Science Research (DSR) approach of Pefers et al. [35] to describe the development of the DSS and address three research questions:

• How reliably can routinely collected data on patient and appoint ment characteristics be used to predict no-show probabilities?

What is the added value, in terms of AUROC (Area Under the Receiver Operating Characteristic curve), of using diferent ML ap proaches to predict no-show probabilities?

How might insights obtained from these classification models be used in practice to reduce no-shows?

The paper is structured as follows. Section 2 presents recent work in no-show prediction, both in terms of the variables used and the modelling approach. Section 3 presents our DSR approach, describing the problem definition, the proposed solution, the design, and the demonstration and evaluation phases. Section 4 presents a descriptive analysis of the available data. Section 5 discusses the results and how these noshow risk classifications could be used in practice. Finally, Section 6 presents some general reflections.

## 2. Related work

Dantas et al. [7] reviewed studies about no-show prediction in health care, published between 1980 and 2016, and classified each reference considering the prediction variables, the modelling approach and the context of the application. The authors found that, over the last ten years, most studies use Multiple Logistic Regression models to quantify relationship between patient characteristics and no-show behaviour. Additionally, despite the highest no-show rates in the world being in Africa (43%), South America (28%) and Asia (25%), this problem was found to have been mainly studied in developed countries.

No-show behaviour in primary care appointments has been widely studied [7]. At least two features can been argued to explain the sci entific interest: firstly, since primary care services are designed to serve large populations, the economic impact of ineficiencies may be greater than in specialized low-coverage services [18]. Secondly, primary care patients are highly heterogeneous; thus, there is evidence that supports contradictory results regarding the impact that patient characteristics might have on no-show rates [19]. In this section, we discuss no-show studies that are related to primary care settings and were published after the review conducted by Dantas et al. [7]. Table 1 presents the modelling approach, sample size and main variables in each of the relevant studies.

To understand the impact of a particular feature on no-show rates, several studies have been conducted using large datasets. McComb et al. [20] find that the impact of lead time on no-show rates is greater among patients who cancel and were rescheduled. Ellis, Luther & Jenkins [21] conclude that reduced sleep consequence of the spring daylight savings change, increased no-show rates, suggesting seasonality on the patterns. Both studies present ways in which the results could be used to improve scheduling practices. More recently, Wallace et al. [3] conclude that patients with lower income and longer travel times to the medical facility are more likely to miss their appointments and Parker, Gaugler, Samus and Gliting [22] find lower no-show rates among care givers using adult day services.

A second approach is to identify patient- and practice-related factors that predict no-show probabilities, using regression models. Ellis et al. [19] find that age, socioeconomic status and lead times are good predictors for repeated non-attendance in Scotland. Analysing data from hospitals in south-west England, French et al. [23] conclude that children from higher deprivation areas are more likely to miss their appointments. Gofman et al. [24] report that no-show history, age and having multiple appointments scheduled on the same day are good predictors for no-show rates among veterans in the United States. Ding et al. [25] discuss the need for designing diferent risk models for each medical service and facility in order to improve accuracy. Lastly, Tsai, Lee, Chiang, Chen, and Chen [26] find that patient gender, age and no show history are good predictors in Taiwan.

In Design Science Research (DSR), knowledge can be descriptive (about the phenomena) or prescriptive (about the human-built artefacts) [27]. This paper adds to the existing body of research on no-show behaviour not only by its use of ML methods on routine health data (the artefact) but also through its focus on developing countries (the phenomena). According to Dantas et al. [7], between 2005 and 2016, most of the research uses regression models in order to predict no-show probabilities. However, recent studies explore the use of other machine learning techniques. Mohammadi, Wu, Turkan, Toscos and Doebbeling [28] analyse data from electronic health records, over a 3-year period, from Community Health Centres in Indianapolis. The authors imple ment logistic regression, neural networks and a Bayes classifier to predict no-show probabilities on a dataset containing 73,811 appointments. Unusually, the regression models and Bayes classifier perform better than neural networks, with AUROC values of 0.81, 0.86 and 0.66, respectively. Similarly, Topuz et al. [15] assess the efectiveness of Bayesian Belief Networks and propose an elastic net variable selection methodology. The authors conclude that there is a potential for machine learning methods to support improvements in management practices by providing accurate prediction of no-show probabilities. These studies make no mention of interpretability of these black-box models, a topic we tackle in this paper.

Lastly, while the same modelling methodology can be generalized to diferent countries, and the same independent variables have been used across diferent contexts and service settings, there is considerable variation between service delivery processes and the demographic and epidemiological population profiles in diferent countries. Each setting must be independently modelled to generate relevant information. Furthermore, previous studies in developing countries report specific features unique to that setting. Challenges such as low use of technology to centralize patient information [29,30], income inequality and job instability [31,32], long travel distances and poverty [33], access barriers to specialized care [34] and even low quality expectations [31] lead to diferent interactions between patients and service providers. Consequently, a systematic efort to develop prediction models and customize strategies for developing countries is required, and we do so in this work.

## 3. A design science research approach

In this section, we present a DSR approach to allow program managers to select patients who will participate in diferent behavioural interventions, by designing an ML-based DSS. Table 2 presents an overview as five of the six steps in the DSR methodology proposed by Pefers et al. [35].

## 3.1. Problem definition, scope and context

Broadly speaking, the national healthcare system in Colombia (Sistema General de Seguridad en Salud, SGSS) can be understood as a managed competition model with two insurance schemes: one contributory, covering people who are in formal employment, and one subsidized, covering people unable to pay [36]. Despite guaranteeing universal coverage, the SGSS faces constant challenges to improve service quality, increase eficiency and eliminate access barriers [12]. Recent studies have shown that these challenges primarily afect patients of lower socioeconomic status [37–39]. Therefore, the District Secretary of Health (Secretaría Distrital de Salud, SDS) in Bogotá instituted a program to eliminate access barriers afecting low-income patients in the city. The program consists of a group of community workers visiting patients, who are sparsely geographically distributed, to assess risks, quantify needs and define care routes within the health system.

The service process of the program can be summarized in three phases. First, patients are identified using existing databases from other social programs. Second, community workers make home visits and classify patients as high, medium or low risk. Finally, in the third phase, a primary care pathway is defined for each patient, according to their level of health risk of needing a service. For each high or medium risk patient, a first medical appointment is scheduled in one or more services. Table 3 presents the objective of the first appointment, in each service, as defined by the National Health Authority [40]. At the end of this phase, the barrier is considered to be overcome, and the patient is expected to start treatment using the services of the relevant insurance scheme. The city is divided into four clusters providing health services and, for each cluster, a team is in charge of the operational decisions of the program.

The SDS has defined three performance indicators to assess the operation of the program.

(i) The percentage of efective visits, i.e. where the patient was physically present at the registered address at the time of the visit, and the community worker was able to assess them and make a risk classification.

(ii) The percentage of appointments given within a target lead time. The designated health centre may not have the capacity to treat the patient within the required time limit, and in such cases the earliest appointment is given.

(iii) The percentage of attendance at appointments (i.e., the percentage of no-shows). These patients might enter the health system later via emergency departments due to complications of the identified risks.

By the end of 2018, program managers faced challenges with indicators (ii) and (iii). Only 30% of appointments met lead time targets and no-show rates reached levels of 35% in some services

## 3.2. The proposed solution

In this context, diferent interventions could be used to modify patient behaviour and improve program performance. Phone reminders [41,42], education [5] and engagement programs [43], among others, have shown positive impact in decreasing no-show rates in diferent service contexts. However, such interventions are most cost-efective when patients are classified according to their no-show risk [5,9]. Therefore, SDS has identified the need to divide patients into three groups. Group A will contain 30% of the patients, due to economic and operational constraints, no additional action will be implemented for them. For Group B, 40% of patients, lower-cost technology-based in terventions such as SMS reminders will be evaluated. Group C will contain the remaining 30% of patients. For these, personalized interventions such as engagement or education programs will be designed to improve attendance levels.

Table 2  
Methodology for Design Science Research (Pefers et al. [25]).

<table><tr><td>Phase</td><td>Our Study</td></tr><tr><td>Problem definition and motivationObjectives for a solutionDesign and development</td><td>To reduce no-show rates, associated with poor patient outcomes and inefficient use of resourcesTo allow program managers to select patients who will participate in different behavioural interventions aimed at increasing attendance levels.We compare four ML modelling approaches and address three questions:1. How reliably can routinely collected data on patient and appointment characteristics be used to predict no-show probabilities?2. Which ML approach performs best, using the AUROC metric?3. How might insights obtained from these classification models be used in practice to reduce no-shows?</td></tr><tr><td>DemonstrationEvaluation</td><td>Performance assessment using the average AUROC score of a 10-by-10 Cross validation.Impact on the coverage and risk of an intervention when a classification algorithm is used</td></tr></table>

Table 3  
Services and objectives of the program.

<table><tr><td>Service</td><td>Objective</td></tr><tr><td>Oral health (OH)</td><td>To assess oral health status and promote self-care.</td></tr><tr><td>Grow and Development (G&amp;D)</td><td>To assess and follow up growth and development status among children.</td></tr><tr><td>Young Adult Program (YAP)</td><td>To assess health status and development risks.</td></tr><tr><td>Senior Program (SP)</td><td>To assess health status and identity major changes.</td></tr><tr><td>CCU Program</td><td>To increase early diagnosis of cervical cancer.</td></tr><tr><td>Breast Cancer Screening</td><td>To increase early diagnosis of breast cancer.</td></tr><tr><td>Family Planning</td><td>To provide relevant information and counselling.</td></tr><tr><td>Antenatal Care</td><td>To ensure timely access and improve health outcomes.</td></tr><tr><td>Emergencies</td><td>To control health risks that might endanger quality of life.</td></tr><tr><td>Visual Care</td><td>To assess health status.</td></tr></table>

It has been argued that by introducing decision support tools, organizations can encourage reasoned thinking, reduce bias and improve decision quality [44]. Therefore, in this paper, we design a DSS to allow program managers to select patients who will participate in diferent behavioural interventions. Additionally, when adopting a DSR ap proach, there is a need to explicitly formulate a set of statements describing the goal, and the means to achieve it. These prescriptive statements are called design principles and are a distinctive char acteristic of design knowledge [45]. After conducting a series of meetings with program managers at SDS and reviewing research papers dealing with no-show behaviour for healthcare appointments, Table 4 presents the resulting components of our design principle using the schema proposed by Gregor et al. [45]. Within this strategy, the success of a set of interventions relies on the quality of the classification. Then, we define two performance indicators that describe the accuracy. The first is the coverage, defined as the percentage of no-show patients that end up classified in Group C, and the second is the risk, defined as the percentage of such patients that end up classified in Group A. A good classification will have high coverage and low risk. In contrast, a random classification would have both coverage and risk equal to 30%.

## 3.3. Design and development: The tested modelling approaches

The first step in the process is the quantification of linear relation ships between variables and no-show probabilities. Ordinary least squares (OLS) estimation is widely used to that end. However, Tibshirani [46] analyses two major drawbacks of OLS: accuracy and interpretation. Since OLS estimates have large variance, setting some coeficients to zero contributes to overcoming both limitations. Therefore, Tibshirani proposes the LASSO regression model, which minimizes the residual sum of squares and ensures that the sum of the absolute value of the coeficients is less than some chosen value. Recent applications of this model include forecasting [47] and classification problems [48]. We have used Scikit-Learn's logistic regression CV implementation, setting the alpha value to 0 so as not to not use ridge regression, and all other parameters have been left at their default values [49]. Additionally, we perform a parametric analysis on the penalty constant of the model. For each service, thirty values are tested (10 values for each of the following three intervals: (0–0.1], (0.1–1], (1−10]) selecting the constant under which the AUROC is stable (i.e. its improvement is marginal) and the prediction depends on the minimum number of variables. Then, for each input variable, we interpret the average coeficients of a 10-by-10 CV. These results are used to inform feature selection for both the RF and the NN.

Although logistic regression (LR) models are highly interpretable (i.e. understandable by non-experts), they may not be useful in contexts where the relationships between variables are nonlinear [50]. For those cases, tree-based ensemble algorithms have shown good performance and modelling flexibility [51]. Tree classifiers split the data set according to a criterion maximizing separation; the result is a tree-like structure [52]. An ensemble of tree predictors, where each tree depends on the values of a random sample of both cases and variables, is called a Random Forest [53]. For classification problems, RFs help to overcome the risk of overfitting, are less sensitive to outliers, and eliminate the need of pruning [54]. It is been argued that the use of oversampling techniques could lead to overly optimistic prediction results [55]. Therefore, in order to deal with an unbalanced data set, we decided to use weight class balancing. Table 5 provides detailed information of the parameters optimization process for the RF using Scikit Learn's Grid-SearchCV function [49].

Lastly, NNs are widely recognized for their capability to model complex statistical interactions between variables [56,57]. An NN is a system of interconnected neurons, organized by independent layers, inspired by biological nervous functioning [58]. Each neuron accepts a number of weighted inputs and processes them to produce an output [59]. The weights of the network connections measure the potential amount of the knowledge of the network [60]. Therefore, a training phase is needed in which the NN adapts the weights through mini mization of the error between actual and estimated outputs [58].

NNs have been shown to be highly accurate for classification problems. However, the major drawback is that they are considered blackbox models [52]. Their nested non-linear structure makes it dificult to understand what information in the input data makes them arrive at their decisions [61]. Recently, Layer-wise Relevance Propagation (LRP) has been proposed as a general solution to the problem of under standing classification decisions [62]. The algorithm relies on a conservation principle to propagate the prediction back throughout the network, ensuring the network output is fully redistributed through the layers of the NN back to the input variables [63]. The main idea is to understand which input variables contribute to a positive or negative classification result [62]. Recent applications of LRP include sentiment analysis [64] and image classification [65]. However, to the best of our knowledge, this explainable approach has not been used in the pre diction of no-show probabilities. This is particularly relevant in our case, since lack of explainability in decision support systems can lead to both practical and ethical issues [66].

Components of the design principle.

<table><tr><td>Design principle</td><td>Our DSS</td></tr><tr><td>Aim, Implementer and User Context</td><td>To allow program managers to select patients who will participate in different behavioural interventions aimed at increasing attendance levels.A primary care program, in a developing country, with high no-show rates.</td></tr><tr><td>Mechanism</td><td>Predict individual no-show probabilities using ML techniques.</td></tr><tr><td>Rationale</td><td>Behavioural interventions are most cost-effective when patients are classified according to their no-show risk.</td></tr></table>

Table 5  
Parameter optimization for RF.

<table><tr><td>Parameter</td><td>Tested values</td></tr><tr><td>Number of trees</td><td>From 50 to 1000 (step length = 50)</td></tr><tr><td>Number of variables for each split</td><td>2,6,8,10</td></tr><tr><td>Minimum number of samples required to be at a leaf node</td><td> $1 \times {10}^{-2},1 \times {10}^{-3},1 \times {10}^{-4},$  $1 \times {10}^{-5},1 \times {10}^{-6}$ </td></tr><tr><td>Minimum impurity required to split a node</td><td> $1 \times {10}^{-2},1 \times {10}^{-3},1 \times {10}^{-4},$  $1 \times {10}^{-5},1 \times {10}^{-6}$ </td></tr></table>

According to Guo and Berkhahm [67], the continuous nature of NNs limits their applicability to categorical variables. Although one-hot encoding is a popular approach to overcome such limitations, it can require an unrealistic amount of computational resource, increase variance and ignore informative relationships between variables. To deal with this problem, Guo and Berkhahm [67] apply the logic used in natural language processing and design an entity embedding method for categorical variables. The idea is to map discrete values to a multidimensional space where values with a similar function output are close to each other. Since the new representation increases the continuity of the data, it speeds up the training process and exploits intrinsic properties of categorical variables. For this work, both one-hot encoding and categorical embeddings are tested. Therefore, we implement an NN with one hidden layer and use heat maps produced by LRP to identify features supporting the classifier's decision for or against a specific class [64]. Table 6 provides basic information regarding parameters optimization using Scikit Learn's GridSearchCV function [49]. All other parameters have been left at their default values.

## 3.4. Demonstration and evaluation

Models performance was assessed using the AUROC score. From the available database, we randomly generated training (70%) and test (30%) sets. In the demonstration phase, a 10-fold Cross Validation process repeated 10 times (10-by-10 CV) was carried out using the training set. In the evaluation phase, we used the test set to assess the quality of the results and discuss the practical implications of increased accuracy when implementing interventions to reduce no-shows. A public version of the experimentation code and a randomly generated database are available [68]. Diferent patients may be selected for targeting according to which classification algorithm is used. As discussed in Section 3.2, we use two measures to assess the quality of a given classification, coverage and risk. Therefore, with this evaluation approach, we aim at quantifying the potential impact of using our DSS.

Table 6  
Parameter optimization for NN.

<table><tr><td>Parameter</td><td>Tested values</td></tr><tr><td>Number of iterations</td><td>From 100 to 1600 (step length = 100)</td></tr><tr><td>Number of neurones</td><td>10 values from N/2 to 2 N, where N is the number of variables</td></tr></table>

## 4. Data collection and initial analyses

We analyse data from the South West cluster of the city. Forty-nine medical facilities ofering primary care are located within this cluster. Four services: Oral Health (OH), Growth and Development (G&D), Young Adult Program (YAP) and Senior Program (SP), are studied as these cover 75% of scheduled appointments during 2017 and 2018. In many scoring models, segmentation of discrete variables results in more stable and parsimonious models [69], so we have used decision trees to classify these categorical variables coarsely (for age and lead time) and one-hot encoding to represent them in the models. Table 7 presents a list of patient and appointment-level variables, their descriptions and the Cramer's V correlation coeficient with the outcome (show or no show).

Our analysis also uses publicly available information relating to two of the above variables. First, using data from the National Administrative Department of Statistics (Departamento Administrativo Nacional de Estadística, DANE), we classify the zone in which each patient lives as low-income if 50% or more of its population belongs to the lowest two income strata: otherwise, it is classified as medium-income. We also use data provided by the National Police Ofice [70] on reported criminal events afecting individual citizens since 2015 to determine the sociodemographic context of each healthcare facility.

Table 8 summarizes basic information on 53,311 scheduled appointments during these two years, including the outcome (show or noshow). Oral Health has the greatest number of appointments (22,613, 42%) and Growth and Development the least, at 14%. No-show rates range from 21% to 39% for each service. At an aggregate level, there is no diference in gender between the no-show rates, but in Oral Health and Young Adult Program more females than males keep their appointments. With respect to age, the highest no-show rates are between 20 and 40 years and the lowest are among children under 10 years and adults over 50. It is also possible to see that smaller lead times yield lower no-show rates. The only exception to this behaviour is in Senior Program where no-show rates are slightly lower for appointments assigned more than 60 days in advance. Finally, Fig. 1 shows the attendance levels, for each service, presented by day of the week and month of the year. While, on average, 92% of the patients keep their appointments on Sunday, this indicator decreases to 69% on Fridays. Attendance levels range from 58% to 82%, for each month, and it behaviour changes across the four services.

## 5. Results and discussion

We present the results organized in three sections. Firstly, we quantify the impact of each variable in the LASSO regression model on the no-show probability, and analyse the average coeficients obtained by a 10-by-10 cross validation process. Next, we quantify the added value of using RF and NN and compare the four modelling alternatives using the AUROC score. Finally, we analyse the impact of using these results as a decision support system and quantify changes in coverage and risk of an intervention when accuracy of prediction models in creases.

## 5.1. LASSO regression model: variables afecting no-show probabilities

Females are more likely to keep their appointments except for SP (odds ratio OH: 1.03, G&D: 1.01, YAP: 1.08 and SP: 0.95). On the one hand, this result is highly context-dependent. Whereas some studies have reached the same conclusion [71,72], others have reported that males have lower no-show rates [19,73,74], or concluded that gender does not have impact in no-show probabilities [75,76]. On the other hand, in developing countries it has been argued that, among socioeconomically disadvantaged females, high no-show rates might be related to a lack of support from social networks and their responsibilities as caregivers [77–79]. This might explain the result for SP. In Bogotá it is common to find that women older than 60 years take care of their grandchildren while the parents work.

Table 7

<table><tr><td rowspan="2">Category</td><td rowspan="2">Variable</td><td rowspan="2">Description</td><td colspan="4">Correlation Coefficient</td></tr><tr><td>OH</td><td>G&amp;D</td><td>YAP</td><td>SP</td></tr><tr><td rowspan="3">Patient</td><td>Gender</td><td>Gender of the patient (Male, Female)</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>Age</td><td>Age of the patient at the moment of the appointment (years)</td><td>0.002</td><td>0.001</td><td>0.002</td><td>0.000</td></tr><tr><td>Zone</td><td>Area of the city where the patient lives</td><td>0.008</td><td>0.017</td><td>0.008</td><td>0.008</td></tr><tr><td rowspan="4">Appointment</td><td>Lead time</td><td>Elapsed time between the date of the home visit and the appointment date (days)</td><td>0.015</td><td>0.018</td><td>0.008</td><td>0.005</td></tr><tr><td>Month</td><td>Month in which the appointment was scheduled</td><td>0.009</td><td>0.015</td><td>0.012</td><td>0.009</td></tr><tr><td>Day</td><td>Day of the week in which the appointment was scheduled</td><td>0.006</td><td>0.005</td><td>0.006</td><td>0.001</td></tr><tr><td>Facility</td><td>Assigned healthcare facility</td><td>0.009</td><td>0.037</td><td>0.005</td><td>0.008</td></tr></table>

No-show probabilities change with the age of the patient. Fig. 2 shows odds ratios (OR) for each age range in the four services. Since four models were run, one for each service, the reference values (OR = 1) must be independently interpreted. Firstly, in OH, patients between 22 and 33 years have the highest no-show probability (OR = 0.72) and it is not possible to identify any age range in which patients have particularly low no-show rates. Secondly, in G&D (between 0 and 13 years) and YAP (between 14 and 44 years), older patients are more likely to miss their appointments. This result is consistent with previously reported findings in primary care and paediatrics settings [20,73,76]. Finally, age seems to have less impact among SP patients.

There is a relationship between the estimated income of the zone in which the patient lives and the no-show probability. In OH, 67% of zones with OR lower than one (i.e. higher no-show probabilities), are low-income zones. Additionally, 63% of zones with lower no-show probabilities have middle-income levels. This result might be associated with the patient's perception of oral health needs. Wallace et al. [80] found that, among low-income populations, dental care is perceived as desirable but more as a luxury than a necessity. The opposite scenario was found in SP: 75% of the zones in which OR is less than one and 25% of the zones with OR greater than one, have medium-income levels. Finally. for G&D and YAP. low-income zones represent the majority of both low and high no-show probability groups.

As expected, longer lead times increase no-show probabilities. Similar results have been reported in primary care settings [19,20], and paediatric clinics [15]. As can be seen in Fig. 3 for G&D and YAP, patients who are scheduled for appointments with lead times between 8 and 10 days are more likely to attend. Given the age of patients in these services, a companion (parent or carer) is often required to attend the appointment. Consequently, non-attendance may be due to challenges in coordinating these logistical aspects. On the other hand, the best attendance rates in OH occur when the lead-time ranges from 0 and 10 days, and the probability of no-shows reaches its maximum value after 15 days. Finally, in older patients, the probability of attendance changes less with respect to lead time. These results demonstrate the non-linear nature of no-shows and support the use of analytical techniques for scheduling appointments.

We also find the date of the appointment afects the no-show probability. Previous studies have reported seasonal behaviours through the year [71,73] or variations depending on the day of the week [28,81,82]. Table 9 shows the OR variations, for the four services, in each month of the year and each day of the week. As can be seen, in YAP the probability of no-show changes slightly in January, March and October. However, for the other months of the year and for all the days of the week, it remains constant. On the other hand, the service with the most changes throughout the year is SP with odds ratio varying between 0.61 and 1.22. This result is interesting because no-show probabilities show low sensitivity to factors such as age, area and lead-time in this service. The months of March, November and December seem to have higher levels of risk of no show. January, February and October have better behaviour. Regarding the days of the week, the best attendance levels are seen during the weekend.

Finally, we observe that there is a relationship between neighbourhood crime statistics and no-show probabilities. The four healthcare facilities with OR lower than one, across the four services, are in neighbourhoods with the highest number of incidents. Similarly, out of 49 facilities used in the program only two have OR greater than one, across all four services. These facilities are in neighbourhoods with the lowest incidence of crime in their respective districts.

Table 8  
Descriptive statistics.

<table><tr><td rowspan="2" colspan="2">Category</td><td colspan="3">OH</td><td colspan="3">G&amp;D</td><td colspan="3">YAP</td><td colspan="3">SP</td><td colspan="3">Total</td></tr><tr><td>Show</td><td colspan="2">No-show</td><td>Show</td><td colspan="2">No-show</td><td>Show</td><td colspan="2">No-show</td><td>Show</td><td colspan="2">No-show</td><td>Show</td><td colspan="2">No-show</td></tr><tr><td rowspan="2">Gender</td><td>Women</td><td>8457</td><td>3475</td><td>29%</td><td>2629</td><td>965</td><td>27%</td><td>4078</td><td>1946</td><td>32%</td><td>3294</td><td>1067</td><td>24%</td><td>18,458</td><td>7453</td><td>29%</td></tr><tr><td>Men</td><td>7482</td><td>3199</td><td>30%</td><td>2650</td><td>999</td><td>27%</td><td>4035</td><td>2065</td><td>34%</td><td>5365</td><td>1605</td><td>23%</td><td>19,532</td><td>7868</td><td>29%</td></tr><tr><td rowspan="7">Age (years)</td><td>0–10</td><td>1659</td><td>638</td><td>28%</td><td>5197</td><td>1918</td><td>27%</td><td>0</td><td>0</td><td>-</td><td>0</td><td>0</td><td>-</td><td>6856</td><td>2556</td><td>27%</td></tr><tr><td>10–20</td><td>2860</td><td>1186</td><td>29%</td><td>82</td><td>46</td><td>36%</td><td>5856</td><td>2530</td><td>30%</td><td>0</td><td>0</td><td>-</td><td>8798</td><td>3762</td><td>30%</td></tr><tr><td>20–30</td><td>1467</td><td>789</td><td>35%</td><td>0</td><td>0</td><td>-</td><td>2092</td><td>1178</td><td>36%</td><td>0</td><td>0</td><td>-</td><td>3559</td><td>1967</td><td>36%</td></tr><tr><td>30–40</td><td>2316</td><td>1058</td><td>31%</td><td>0</td><td>0</td><td>-</td><td>165</td><td>91</td><td>36%</td><td>0</td><td>0</td><td>-</td><td>2481</td><td>1149</td><td>32%</td></tr><tr><td>40–50</td><td>2964</td><td>1209</td><td>29%</td><td>0</td><td>0</td><td>-</td><td>0</td><td>0</td><td>-</td><td>1294</td><td>425</td><td>25%</td><td>4258</td><td>1634</td><td>28%</td></tr><tr><td>50–60</td><td>2093</td><td>791</td><td>27%</td><td>0</td><td>0</td><td>-</td><td>0</td><td>0</td><td>-</td><td>3232</td><td>1014</td><td>24%</td><td>5325</td><td>1805</td><td>25%</td></tr><tr><td>Over 60</td><td>2580</td><td>1003</td><td>28%</td><td>0</td><td>0</td><td>-</td><td>0</td><td>0</td><td>-</td><td>4133</td><td>1233</td><td>23%</td><td>6713</td><td>2236</td><td>25%</td></tr><tr><td rowspan="4">Lead time (days)</td><td>0–15</td><td>7689</td><td>2259</td><td>23%</td><td>3329</td><td>929</td><td>22%</td><td>4969</td><td>2029</td><td>29%</td><td>4070</td><td>1068</td><td>21%</td><td>20,057</td><td>6285</td><td>24%</td></tr><tr><td>15–30</td><td>2079</td><td>1061</td><td>34%</td><td>754</td><td>453</td><td>38%</td><td>902</td><td>562</td><td>38%</td><td>1013</td><td>434</td><td>30%</td><td>4748</td><td>2510</td><td>35%</td></tr><tr><td>30–60</td><td>1503</td><td>785</td><td>34%</td><td>373</td><td>166</td><td>31%</td><td>488</td><td>299</td><td>38%</td><td>901</td><td>309</td><td>26%</td><td>3265</td><td>1559</td><td>32%</td></tr><tr><td>Over 60</td><td>4668</td><td>2569</td><td>35%</td><td>823</td><td>416</td><td>34%</td><td>1754</td><td>1121</td><td>39%</td><td>2675</td><td>861</td><td>24%</td><td>9920</td><td>4967</td><td>33%</td></tr></table>

OH: Oral Health, G&D: Growth and Development, YAP: Young Adult Program, SP: Senior Program.

![](/api/attachments/ZWMJ7CBY/fulltext/images/10b2e8f1ddb37dcf329a5667ac5698c01c8ee44128acb8c48e02abe066962fdf.jpg)

![](/api/attachments/ZWMJ7CBY/fulltext/images/f015d599918aaae30ca584497b812c830325ccb298f148e46c632807f374a0d4.jpg)

![](/api/attachments/ZWMJ7CBY/fulltext/images/0777f3692ac7eb8e9d8f0ebfdf43ce8acaef0cea5824b4b15008d8bfd5543192.jpg)

![](/api/attachments/ZWMJ7CBY/fulltext/images/5a0cbcf6a8b47927651b705d9c96e0524504c3a4e606d12fd85d929f7eef787f.jpg)

![](/api/attachments/ZWMJ7CBY/fulltext/images/7da982bba9c5109016215912e70ad8dffbc7819e82c2775c906ce5288bc962bb.jpg)

![](/api/attachments/ZWMJ7CBY/fulltext/images/b9f96c8b6764317c55a090b3b4922762f4cb7c235884ab15604aa718c703e83c.jpg)

![](/api/attachments/ZWMJ7CBY/fulltext/images/9a9f43a4edf3954c193665fdae8296041a2a5852df42553f36b501ae47516586.jpg)  
Fig. 1. Attendance levels for each service.

![](/api/attachments/ZWMJ7CBY/fulltext/images/c38f3a61dc30901e58a0d709c6ce2154583e1321180f7f1632a858d7bdcc9e48.jpg)

![](/api/attachments/ZWMJ7CBY/fulltext/images/9d1c4eb5312911014fd488c02d9fa3dc8eef21c24b515710e2a676b77babad09.jpg)  
Fig. 2. Odds ratio for each range of age.

Fig. 4 presents the 15 variables with the greatest impact on no-show probabilities in each service. Firstly, attendance levels are higher on Saturdays (G&D) and Sundays (OH, YAP and SP). This result can be used to inform tactical decisions regarding the number of appointments that should be made available throughout the planning horizon. Secondly, ensuring reasonable lead times can afect utilization levels. For the four services, it is possible to identify a maximum lead time that can be set as an objective in the scheduling process. Lastly, some months and facilities have relatively high no-show rates. This information can be used in the design of overbooking policies, since better estimates of no-show probabilities would help to reduce the undesirable side efects of this practice.

## 5.2. The added value of using other modelling approaches

Fig. 5 presents the AUROC performance of the four models. Each point in the graph represents the average and standard deviation of the AUROC in a repetition of 10-by-10 cross-validation. For all four services, the NN model has better average performance. The diference between RF and LR may suggest that the non-linear component of the relationship between the variables is not very strong, but still significant. Additionally, the average AUROC of both NN models indicates that variable interaction can be successfully modelled without using categorical embedding. Despite having low standard deviations, the amount of available data might not be suficient to generate robust embeddings, and the disadvantage of increased variance is outweighed by better bias estimation with the increased number of dummy variables. Therefore, in our further analysis we consider only the NN with one-hot encoding.

![](/api/attachments/ZWMJ7CBY/fulltext/images/34868c972c4a8be51c48ab4f4e6d44bbe52a1bd4af108b3b3205ec4d447cec8c.jpg)

![](/api/attachments/ZWMJ7CBY/fulltext/images/0a4b92e8b90be8c220704a1da954d77817d9a09e345cfca954390e37e89d0177.jpg)

![](/api/attachments/ZWMJ7CBY/fulltext/images/1a3dc2369cf8bec6b6ca4f765794188b3874e21738151e519f0daa0be6b7cbaf.jpg)

![](/api/attachments/ZWMJ7CBY/fulltext/images/309f88ed834938ae6c86aa9ff731cbb9d0f40009507149f143dfe57e88ab1149.jpg)

![](/api/attachments/ZWMJ7CBY/fulltext/images/154ae1cbfc503f40821e0c420d3b1e9179bb8fd0be2444169f3dcfe21a80a1be.jpg)  
Fig. 3. Odds ratio for each service when lead time is varied.

Average odds ratio for the appointment date.

<table><tr><td></td><td></td><td>G&amp;D</td><td>YAP</td><td>SP</td><td>OH</td></tr><tr><td rowspan="12">Month of the year</td><td>January</td><td>1.02</td><td>0.96</td><td>1.01</td><td>1.11</td></tr><tr><td>February</td><td>1.10</td><td>1.00</td><td>1.22</td><td>1.30</td></tr><tr><td>March</td><td>0.72</td><td>0.85</td><td>0.87</td><td>1.00</td></tr><tr><td>April</td><td>1.00</td><td>1.00</td><td>1.13</td><td>1.00</td></tr><tr><td>May</td><td>1.00</td><td>1.00</td><td>0.99</td><td>0.80</td></tr><tr><td>June</td><td>0.9</td><td>1.00</td><td>0.61</td><td>0.75</td></tr><tr><td>July</td><td>1.02</td><td>1.00</td><td>0.99</td><td>1.04</td></tr><tr><td>August</td><td>0.74</td><td>1.00</td><td>1.00</td><td>0.90</td></tr><tr><td>September</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td></tr><tr><td>October</td><td>1.04</td><td>1.01</td><td>1.21</td><td>1.00</td></tr><tr><td>November</td><td>0.71</td><td>1.00</td><td>0.94</td><td>0.95</td></tr><tr><td>December</td><td>0.51</td><td>1.00</td><td>0.73</td><td>0.69</td></tr><tr><td rowspan="7">Day of the week</td><td>Sunday</td><td>1.06</td><td>1.00</td><td>1.37</td><td>3.50</td></tr><tr><td>Monday</td><td>0.96</td><td>1.00</td><td>1.00</td><td>0.93</td></tr><tr><td>Tuesday</td><td>1.00</td><td>1.00</td><td>1.00</td><td>0.96</td></tr><tr><td>Wednesday</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td></tr><tr><td>Thursday</td><td>1.00</td><td>1.00</td><td>0.96</td><td>1.00</td></tr><tr><td>Friday</td><td>0.96</td><td>1.00</td><td>0.98</td><td>0.84</td></tr><tr><td>Saturday</td><td>1.35</td><td>1.00</td><td>1.00</td><td>1.03</td></tr></table>

## 5.3. The decision support system

In this section we analyse the implications of using our DSS to select patients and implement targeted interventions. As discussed in Section 3, SDS have specified that the developed DSS should allow program managers to divide patients into three groups. Group A will contain the 30% of patients estimated to have lowest no-show risk. Group B, the 40% of patients with intermediate risk and Group C will contain the remaining 30% of patients with the highest no-show probabilities. From the machine learning perspective, this means that two cut-of points are required. This process is called cut-of point tuning and is based on ROC performance measures [83].

Table 10 presents the coverage and risk for each service and for three models. As can be seen, in G&D, an intervention for 30% of patients could cover 80% of the no-shows, if the prediction of the NN is used. This percentage would decrease to 64% or 41% using RF or LR. This result is consistent across the four services. The average improvement in coverage using NN is 14% with respect to RF and 62% with respect to LR. Lastly, the risk of not implementing any action among patients with low no-show risk can be quantified. Using the NN classification, these patients represent between 2% and 3% of no shows. On the other hand, using the RF prediction the highest risk is in OH and YAP where 9% of the no-shows are classified in group A. Finally, using logistic regression, the risk varies between 17% and 21%.

![](/api/attachments/ZWMJ7CBY/fulltext/images/c1df49d5aab12edd79a50f65746ceeba754723496a99982af40d8d08501cf346.jpg)  
Fig. 4. LASSO results: most relevant variables for each service.

![](/api/attachments/ZWMJ7CBY/fulltext/images/e0d8e6762835361e07d85d903a3f66bc1a374d1f29c8987c76215f33d35bc50a.jpg)

![](/api/attachments/ZWMJ7CBY/fulltext/images/401b8882a9675602519768948f697b0890deb54407d816ba98f5797815d25917.jpg)

![](/api/attachments/ZWMJ7CBY/fulltext/images/6c8e32948403724b65f785c76d3e89c2bd045374bab860e6e49098b38daa9d99.jpg)

Fig. 5. Model performance.  
![](/api/attachments/ZWMJ7CBY/fulltext/images/2c4ebdbaae897331d491965e7e9b821f2843e121616e0df2d4e49afcf9331d43.jpg)

Table 10  
Risk and Coverage for a potential intervention.

<table><tr><td rowspan="2">Service</td><td colspan="2">NN</td><td colspan="2">RF</td><td colspan="2">LR</td></tr><tr><td>Risk</td><td>Coverage</td><td>Risk</td><td>Coverage</td><td>Risk</td><td>Coverage</td></tr><tr><td>OH</td><td>2%</td><td>70%</td><td>9%</td><td>55%</td><td>17%</td><td>39%</td></tr><tr><td>G&amp;D</td><td>2%</td><td>80%</td><td>3%</td><td>64%</td><td>17%</td><td>41%</td></tr><tr><td>YAP</td><td>3%</td><td>67%</td><td>9%</td><td>55%</td><td>20%</td><td>41%</td></tr><tr><td>SP</td><td>2%</td><td>75%</td><td>6%</td><td>61%</td><td>21%</td><td>40%</td></tr></table>

Despite the high accuracy of the NN prediction (i.e. risk of 2.25% and average coverage around 72%), using NN results might be challenging. It has been argued that decision makers need to understand the reasons underpinning a prediction in order to trust the results [84,85]. Consequently, in an attempt to explain the results of the NN, we implement LRP [62]. As a result, the importance of each of the variables in the classification of a patient in each category is obtained. According to Yang, Tresp, Wuderle and Fasching [65], one of the advantages of this technique, compared with sensitivity analysis, is the interpretability of the signs (and absolute values) of the weights. For example, when the weight is large and positive, the variable strongly supports the classification chosen by the NN, whereas if the weight is small and negative, the variable weakly suggests the opposite classification.

Fig. 6 illustrates the results obtained for ten G&D patients. A column represents a patient, and the column heading the no-show probability. The blue cells represent positive coefficients and the red cells negative ones, shaded by the magnitude of the weight. Only those variables with at least one non-zero coeficient are shown for this group of patients. Our NN predicts that the first patient will not show up for his appointment (95% of no-show probability). The main reason for this conclusion is the month of the appointment, but lead time and age also support this classification. On the other hand, the day of the appointment, and the zone in which the patient lives support the opposite classification, i.e. that the patient would in fact attend. Moreover, the fact that the same variables have both positive and negative coeficients (regardless of the no-show probabilities) implies that the network is learning about the context. It means that the NN learns that it is not enough to know the gender of a patient to decide in which category they should be classified. For example, when running a regression model including the interaction of gender with age and day of the week, it is possible to observe slightly diferent results from those reported by the model without interaction. For G&D we found that females are more likely to miss appointments on Saturdays and Wednesdays (O.R. = 0.75 and 0.94).

This interpretation procedure can be used for any data-driven ma chine learning model, giving interesting insights which have real ap plications for decision support systems. The focus of the implementation of these processes must be on actionable combinations of parameters: if a relation between several variables is found (such as gender and day of the week), then an action can be performed for those specific groups. The use of such interpretability tools allows efects like these to be observed and revealed, which would otherwise be neglected.

## 6. Concluding remarks

This work has been developed with the active involvement of SDS. We conducted several workshops with program managers, operational analysts at the healthcare clusters, and community workers. This approach enabled us to develop a more comprehensive view of the program, identify a champion for the project within SDS, generate a shared vision of the main challenges and maintain stakeholders' engagement. Therefore, the discussion shifted from a resource allocation perspective to a better understanding of the underlying problem and the identification of restrictions that could prevent the implementation of changes in the operation. By the end of the workshops, they concluded that as the program covers a highly heterogenic population, more personalized strategies were required to reduce no-show behaviour. In this context, patient classification was identified as a key element to ensure the economic feasibility of any intervention strategy. Following this process we were able to reach an agreement on an appropriate design principle which captures the knowledge of our stakeholders. Consequently, our DSS aims at leveraging routinely collected data to inform such classification. During the feedback sessions, program managers stressed that they value that the results were easy to understand and have the potential to improve service quality.

![](/api/attachments/ZWMJ7CBY/fulltext/images/33300b2fa7e1e1d7d91b8285ef04d22841bdaae22686fe46e9a6619a9fab2b56.jpg)  
Fig. 6. Heatmap for G&D.

In light of the promising results, at the time of writing SDS is starting a pilot intervention to modify patient behaviour. Using the DSS to predict no-show probabilities will improve the effectiveness of the intervention since the NN classifies around 80% of potential no-show cases to Group C, the 30% of patients designated to receive the most intensive, personalized, intervention. Therefore, as stated in our design principle, the design of this DSS can be seen as a necessary first step to reduce no-show behaviour in primary care and the future development of design knowledge [86]. After an evaluation of the pilot is carried out, a web-based tool will be developed to enable models to be used in program operation.

Our objective is to use routinely collected data to predict no-show probabilities. However, in order to inform the discussion, we also use other sources of public information. Two findings are particularly relevant in developing country contexts. First, in Oral Health, 67% of zones with OR less than one (i.e. higher no-show probabilities), are lowincome zones, and 63% of zones with lower no-show probabilities have middle-income levels. Second, the four healthcare facilities (out of 49) with OR less than one across all four services are in neighbourhoods with the highest number of reported crime incidents, whereas the two facilities with OR greater than one across all four services are in neighbourhoods with the lowest crime incidence in their respective districts. These exploratory results indicate that including socioeconomic data could potentially increase understanding of no-show behaviour. Further research is required to evaluate the cost/benefit of collecting such data and including these variables in the SDS information system.

Since this paper presents retrospective analysis of historical data, it is not possible to draw conclusions regarding the reasons for no-show behaviour. Therefore, the next step in this research is a mixed-method study to understand and model patients' decision-making processes. Semi-structured interviews are being conducted among no-show patients in order to learn from their experiences and identify access barriers. Moreover, we are analysing survey data to quantify the relationship between the no-show probability and the constructs of a health psychology model.

Modelling no-show behaviour in primary care settings is an active research area. The most common approach in the literature is multiple regression, but due to its limitations in accuracy, using the results to improve management practice can be problematic. Machine learning methods are gaining in popularity but have the drawback of being a ‘black box’ that managers may not trust. Our research shows the benefits of a two-pronged approach to overcome this. Firstly, using LRP to produce a heat map visualisation that makes the model results immediately understandable, and secondly, involving stakeholders in every stage of the design process. Additionally, despite the highest noshow rates worldwide being in developing countries, the problem has been mainly studied in North America and the United Kingdom [7]. The research presented here contributes to the literature by assessing the efectiveness of machine learning approaches using routine data to predict no-show behaviour among low-income patients in a developing country context.

Throughout this research, we have designed a process to construct a DSS for improving healthcare access powered with machine learning models. In general, the first stages of the process are replicable across all healthcare systems that wish to develop such a DSS. Steps such as the facilitated formulation of a design principle, data collection strategies, data processing steps, and the selection of models to use are relevant issues for every designer facing a similar challenge. Additionally, by using the schema proposed by Gregor et al. [45], our design principle also meets the five criteria for reusability: accessibility, importance, novelty, and efectiveness [87]. Therefore, we expect that other DSS designers can build from this experience when defining intervention groups. We believe that our results could help not only other designers in healthcare settings but also those dealing with limited resources in other contexts such as educational or social programs, where prioritization plays a key role in ensuring feasibility.

## Funding

The first author's research is partially funded by a PhD scholarship from the healthcare research stream of the program Colombia Científica – Pasaporte a la Ciencia, granted by the Colombian Institute for Educational Technical Studies Abroad (Instituto Colombiano de Crédito Educativo y Estudios Técnicos en el Exterior, ICETEX). The third author acknowledges this research was undertaken, in part, thanks to funding from the Canada Research Chairs program.

## References

[1] M. Zebina, B. Melot, B. Binachon, R. Ouissa, I. Lamaury, B. Hoen, Impact of an SMS reminder service on outpatient clinic attendance rates by patients with HIV fol lowed-up at pointe-à-Pitre university hospital, Patient Prefer. Adherence. Volume 13 (2019) 215–221, https://doi.org/10.2147/ppa.s182186.

[2] R. McQueenie, D.A. Ellis, A. McConnachie, P. Wilson, A.E. Williamson, Morbidity, mortality and missed appointments in healthcare: a national retrospective data linkage study, BMC Med. 17 (2019) 1–9, https://doi.org/10.1186/s12916-018- 1234-0.

[3] D.J. Wallace, K.N. Ray, A. Degan, K. Kurland, D.C. Angus, A. Malinow, Transportation characteristics associated with non-arrivals to paediatric clinic ap pointments: a retrospective analysis of 51 580 scheduled visits, BMJ Qual. Saf. 27 (2018) 437–444, https://doi.org/10.1136/bmjqs-2017-007168.

[4] J.S. Mikhaeil, E. Celo, J. Shanahan, B. Harvey, B. Sipos, M.P. Law, Attend: a two pronged trial to eliminate no shows in diagnostic imaging at a community-based hospital, J. Med. Imaging Radiat. Sci. 50 (2019) 36–42, https://doi.org/10.1016/j. jmir.2018.10.012.

[5] K.R. Weaver, M. Talley, M. Mullins, C. Selleck, Evaluating patient navigation to improve first appointment no-show rates in uninsured patients with diabetes, J. Community Health Nurs. 36 (2019) 11–18, https://doi.org/10.1080/07370016. 2018.1555315.

[6] R.T. Finn, B. Lloyd, Y.A. Patel, J.T. Allen, J. Cornejo, A. Davis, T. McIntosh, S. Ferguson, K. Sims, S. Sudaj, J. Taheri, D. Provenzale, Z.F. Gellad, Decreasing endoscopy no-shows using a lean improvement framework. Clin. Gastroenterol. Hepatol. (2019), https://doi.org/10.1016/j.cgh.2019.02.002.

[7] L.F. Dantas, J.L. Fleck, F.L. Cyrino, S. Hamacher, No-shows in appointment scheduling – a systematic literature review, Health Policy (New. York). 122 (2018) 412–421, https://doi.org/10.1016/j.healthpol.2018.02.002.

[8] W.P. Millhiser, E.A. Veral, A decision support system for real-time scheduling of multiple patient classes in outpatient services, Health Care Manag. Sci. 22 (2019) 180–195, https://doi.org/10.1007/s10729-018-9430-1

[9] Y. Wu, Y. Liang, Q. Zhou, H. Liu, G. Lin, W. Cai, Y. Li, J. Gu, Efectiveness of a short message service intervention to motivate people with positive results in preliminary colorectal cancer screening to undergo colonoscopy: a randomized controlled trial, Cancer. (2019) 1–10, https://doi.org/10.1002/cncr.32043.

[10] F.J. Schwebel, M.E. Larimer, Using text message reminders in health care services: narrative literature review, Internet Interv. 13 (2018) 82–104, https://doi.org/10. 1016/i.invent,2018.06.002

[11] A. Ahmadi-Javid, Z. Jalali, K.J. Klassen, Outpatient appointment systems in healthcare: a review of optimization studies, Eur. J. Oper. Res. 258 (2017) 3–34, https://doi.org/10.1016/j.ejor.2016.06.064.

[12] S. Brailsford, P. Harper, J. Sykes, Incorporating human behaviour in simulation models of screening for breast cancer, Eur. J. Oper. Res. 219 (2012) 491–507, https://doi.org/10.1016/j.ejor.2011.10.041.

[13] J. Daggy, D. Willis, A. Turkcan, S. Chakraborty, M. Lawley, P.-C. DeLaurentis, D. Thaver. C. Suelzer. L. Sands, Using no-show modeling to improve clinic perfor mance, Health Informatics J. 16 (2010) 246–259. https://doi,org/10.1177 1460458210380521.

[14] A. Shuja, C. Harris, P. Aldridge, M. Malespin, S.W. De Melo, Predictors of no-show rate in the GI endoscopy suite at a safety net Academic Medical Center. J. Clin Gastroenterol. 53 (2019) 29–33, https://doi,org/10.1097/MCG. 0000000000000928.

[15] K. Topuz, H. Uner, A. Oztekin, M.B. Yildirim, Predicting pediatric clinic no-shows: a decision analytic framework using elastic net and Bayesian belief network, Ann. Oper. Res. 263 (2018) 479–499, https://doi.org/10.1007/s10479-017-2489-0.

[16] N. Chaudhuri, I. Bose, Exploring the role of deep neural networks for post-disaster decision support, Decis, Support, Syst, 130 (2020) 113234. https://doi,org/10. 1016/i.dss.2019.113234.

[17] J. Fredrickson, M. Mannino, O. Algahtani, F. Banaei-Kashani, Using similarity measures for medical event sequences to predict mortality in trauma patients, Decis. Support. Syst. 116 (2019) 35–47, https://doi.org/10.1016/j.dss.2018.10. 008.

[18] J.B. Norris, C. Kumar, S. Chand, H. Moskowitz, S.A. Shade, D.R. Willis, An empirical investigation into factors affecting patient cancellations and no-shows at outpatient clinics, Decis. Support. Syst. 57 (2014) 428–443, https://doi.org/10.1016/j.dss. 2012.10.048.

[19] D.A. Ellis, R. McQueenie, A. McConnachie, P. Wilson, A.E. Williamson, Demographic and practice factors predicting repeated non-attendance in primary care: a national retrospective cohort analysis, Lancet Public Heal. 2 (2017) e551–e559, https://doi.org/10.1016/S2468-2667(17)30217-7.

[20] S. McComb, L. Sands, L. Zhang, Z. Tian, M. Lawley, S. Frazier, A. Turkcan, Cancelled primary care appointments: a prospective cohort study of diabetic patients, J. Med. Syst. 41 (2017), https://doi.org/10.1007/s10916-017-0700-0.

[21] D.A. Ellis, K. Luther, R. Jenkins, Missed medical appointments during shifts to and from daylight saving time, Chronobiol. Int. 35 (2018) 584–588, https://doi.org/10. 1080/07420528.2017.1417313

[22] L.J. Parker, J.E. Gaugler, Q. Samus, L.N. Gitlin, Adult Day service use decreases likelihood of a missed Physician’s appointment among dementia caregivers, J. Am. Geriatr. Soc. (2019) 1467–1471, https://doi.org/10.1111/jgs.15995.

[23] L.R. French, K.M. Turner, D.J. Sharp, H. Morley, L. Goldsworthy, J. Hamilton-Shield, Characteristics of children who do not attend their hospital appointments, and GPs’ response: a mixed methods study in primary and secondary care, Br. J. Gen, Pract, 67 (2017) e483–e489, https://doi,org/10.3399/bigp17x691373

[24] R.M. Gofman, A.S. Milicevic, K.L. Rodriguez, L. Myaskovsky, S.L. Harris,

Y.C. Tjader, J.H. May, D.L. Vargas, R.J. Monte, Modeling patient no-show history and predicting future outpatient appointment behavior in the veterans health administration, Mil. Med. 182 (2017) e1708–e1714, https://doi.org/10.7205 milmed-d-16-00345.

[25] X. Ding, P. Barth, M. Newman, C. Mather, B.A. Goldstein, E.G. Poon, Z.F. Gellad Designing risk prediction models for ambulatory no-shows across diferent specialties and clinics, J. Am. Med. Informatics Assoc. 25 (2018) 924–930, https://doi. org/10.1093/jamia/ocy002.

[26] W.C. Tsai, W.C. Lee, S.C. Chiang, Y.C. Chen, T.J. Chen, Factors of missed ap pointments at an academic medical center in Taiwan, J. Chinese Med. Assoc. 82 (2019) 436–442, https://doi.org/10.1097/JCMA.0000000000000068.

[27] S. Gregor, A.R. Hevner, Positioning and presenting design science research for maximum impact, MIS Q. 37 (2013) 337–356, https://doi.org/10.25300/MISQ 2013/37.2.01.

[28] I. Mohammadi, H. Wu, A. Turkcan, T. Toscos, B.N. Doebbeling, Data analytics and Modeling for appointment no-show in community health Centers, J. Prim. Care Community Heal. 9 (2018), https://doi.org/10.1177/2150132718811692.

[29] D. Giunta, A. Briavore, A. Baun, D. Luna, Factors associated with nonattendance at clinical medicine scheduled outpatient appointments in a university general hospital, Patient Prefer. Adherence. 7 (2013) 1163–1170, https://doi.org/10.2147/ PPA.S51841.

[30] S. Ade, A. Trébucq, A.D. Harries, G. Ade, G. Agodokpessi, P. Wachinou, Follow-up and tracing of tuberculosis patients who fail to attend their scheduled appointments in Cotonou, Benin : a retrospective cohort study, BMC Health Serv. Res. (2016) 1–7, https://doi.org/10.1186/s12913-015-1219-z

[31] A.T. Machado, M. Azeredo, F. Werneck, S.D. Lucas, Who did not appear ? First dental visit absences in secondary care in a major Brazilian city : a cross-sectional study Quem não compareceu ? Ausências às primeiras consultas odontológicas na atenção secundária em um município brasileiro de grande porte, (2011), pp. 289–298, https://doi.org/10.1590/1413-81232014201.01012014.

[32] J. Barjis, G. Kolfschoten, J. Maritz, A sustainable and afordable support system for rural healthcare delivery, Decis. Support. Syst. 56 (2013) 223–233, https://doi.org 10.1016/j.dss.2013.06.005.

[33] C.E. Mbada, J. Nonvignon, O. Ajayi, B.M.R. Pt, O.O. Dada, T.O. Awotidebe, O.E. Johnson, A. Olarinde, B.S. Aat, Impact of missed appointments for out- patient physiotherapy on cost, eficiency, and patients’ recovery, Hong Kong Physiother. J. 31 (2013) 30–35, https://doi.org/10.1016/j.hkpj.2012.12.001.

[34] F.Y. Tseng, Non-attendance in endocrinology and metabolism patients, J. Formos. Med. Assoc. 109 (2010) 895–900, https://doi.org/10.1016/S0929-6646(10) 60136-2.

[35] K. Pefers, T. Tuunanen, M.A. Rothenberger, S. Chatterjee, A design science re search methodology for information systems research, J. Manag. Inf. Syst. 24 (2007) 45–77, https://doi.org/10.2753/MIS0742-1222240302.

[36] I. Vargas, A.S. Mogollón-Pérez, P. De Paepe, M.R. Ferreira Da Silva, J.P. Unger, M.L. Vázquez, Barriers to healthcare coordination in market-based and decentralized public health systems: a qualitative study in healthcare networks of Colombia and Brazil, Health Policy Plan. 31 (2016) 736–748, https://doi.org/10. 1093/heapol/czv126.

[37] I. Vargas, M.L. Vzquez, A.S. Mogollán-Pérez, J.P. Unger, Barriers of access to care in a managed competition model: lessons from Colombia. BMC Health Sery. Res. 10 (2010) 297, https://doi.org/10.1186/1472-6963-10-297

[38] J.C. Rivillas, F.D. Colonia, Reducing causes of inequity: policies focused on social determinants of health during generational transitions in Colombia. Glob. Health Action 10 (2017)1349238. https://doi.org/10.1080/16549716.2017.1349238

[39] I. Garcia-Subirats, I. Vargas, A.S. Mogollón-Pérez, P. De Paepe, M.R.F. da Silva, J.P. Unger, C. Borrell, M.L. Vázquez, Inequities in access to health care in diferent health systems: a study in municipalities of Central Colombia and North-Easterr Brazil, Int. J. Equity Health 13 (2014) 10, https://doi.org/10.1186/1475-9276- 13-10.

[40] Ministerio de Salud y Proteccion Social, Resolution 603280, https://www. minsalud.gov.co/Normatividad Nuevo/ResoluciónNo.3280de20183280.pdf. (2008).

[41] F. Tull, K. Borg, C. Knott, M. Beasley, J. Halliday, N. Faulkner, K. Sutton, P. Bragge, Short message service reminders to parents for increasing adolescent human papillomavirus vaccination rates in a secondary school vaccine program: a randomized control trial, J. Adolesc. Health (2019), https://doi.org/10.1016/j. jadohealth 2018.12.026

[42] J.F. Steiner, M.R. Shainline, J.Z. Dahlgren, A. Kroll, S. Xu, Optimizing number and timing of appointment reminders: a randomized trial, Am. J. Manag. Care 24 (2018) 377–384.

[43] D. Michelson, C. Day, Improving attendance at child and adolescent mental health services for families from socially disadvantaged communities: evaluation of a preintake engagement intervention in the UK, Adm. Policy Ment. Heal. Ment. Heal. Serv. Res. 41 (2014) 252–261, https://doi.org/10.1007/s10488-012-0462-4.

[44] M.A.A. Féris, O. Zwikael, S. Gregor, QPLAN: decision support for evaluating plan ning quality in software development proiects. Decis. Support. Syst. 96 (2017) 92–102. https://doi.org/10.1016/i.dss.2017.02.008

[45] S. Gregor, L. Chandra Kruse, S. Seidel, The anatomy of a design principle, J. Assoc. Inf. Syst. (2020) Forthcoming.

[46]. R. Tibshirani, Regression shrinkage and selection via the Lasso. J. R. Stat, Soc, Ser. B 58 (1996) 267–288, https://doi.org/10.1111/j.2517-6161.1996.tb02080.x.

[47] S. Wang, B. Ji, J. Zhao, W. Liu, T. Xu, Predicting ship fuel consumption based on LASSO regression, Transp. Res. Part D Transp. Environ. 65 (2018) 817–824, https://doi.org/10.1016/j.trd.2017.09.014.

[48] Z. Zhang, Y. Hong, Development of a novel score for the prediction of hospita mortality in patients with severe sepsis: the use of electronic healthcare records

with LASSO regression, Oncotarget. 8 (2017) 49637–49645, https://doi.org/10. 18632/oncotarget.17870.

[49] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Bllondel, P. Prettenhofer, R. Weiss, V. Dubourg, A. Vanderplas, D. Cournapeau, M. Brucher, E. Duchesnay, Scikit-learn: machine learning in Python, J. Mach. Learn. Res. 12 (2011) 2825–2830, https://doi.org/10.1145/2786984.2786995.

[50] L. Auret, C. Aldrich, Interpretation of nonlinear relationships between process variables by use of random forests, Miner. Eng. 35 (2012) 27–42, https://doi.org 10.1016/j.mineng.2012.05.008.

[51] L. Breiman, Manual on Setting up, Using and Understanding Random Forests V3, (2002).

[52] S. Dreiseitl, L. Ohno-Machado, Logistic regression and artificial neural network classification models: a methodology review. J. Biomed. Inform. 35 (2o02) 352-359.https://doi.org/10.1016/S1532-0464(03)00034-0

[53] L. Breiman, Random forests, Mach. Learn. (2001) 5–32, https://doi.org/10.1023 A:1010933404324

[54] J. Ali, N. Ahmad, I. Maqssod, Random forests and decision trees, Int. J. Comput. Sci. Issues, 9 (2012) 272–278.

[55] G. Vandewiele, I. Dehaene, G. Kovács, L. Sterckx, O. Janssens, F. Ongenae, F. De Backere. E. De Turck. K. Roelens., J. Decruvenaere, S. Van Hoecke. T. Demeester Overly Optimistic Prediction Results on Imbalanced Data: Flaws and Benefits of Applying Over-sampling, (2020) http://arxiv.org/abs/2001.06296.

[56] M. Tsang, D. Cheng, Y. Liu, Detecting Statistical Interactions from Neural Network Weights, (2017), pp. 1–21 http://arxiv.org/abs/1705.04977.

[57] D. Barrow, N. Kourentzes, The impact of special days in call arrivals forecasting: a neural network approach to modelling special days, Eur. J. Oper. Res. 264 (2018) 967–977. https://doi.org/10.1016/i.eior.2016.07.015

[58] W. Wong, P.J. Fos, F.E. Petry, Combining the performance strengths of the logistic regression and neural network models: a medical outcomes approach, ScientificWorldJournal. 3 (2003) 455–476, https://doi.org/10.1100/tsw.2003.35.

[59] D. Dancey, Z. Bandar, D. McLean, Logistic model tree extraction from artificial neural networks, IEEE Trans. Syst. Man Cybern. - Part B Cybern. 37 (2007) 73–91, https://doi.org/10.1007/978-3-7908-1771-3\_3.

[60] O.I. Abiodun, A. Jantan, A.E. Omolara, K.V. Dada, N.A.E. Mohamed, H. Arshad, State-of-the-art in artificial neural network applications: a survey, Heliyon. 4 (2018) e00938, , https://doi.org/10.1016/j.heliyon.2018.e00938.

[61] W. Samek, T. Wiegand, K.-R. Müller, Explainable Artificial Intelligence: Understanding, Visualizing and Interpreting Deep Learning Models, http://arxiv. org/abs/1708.08296, (2017).

[62] S. Bach, A. Binder, G. Montavon, F. Klauschen, K.R. Müller, W. Samek, On pixelwise explanations for non-linear classifier decisions by layer-wise relevance propagation, PLoS One 10 (2015) 1–46, https://doi.org/10.1371/journal.pone. 0130140.

[63] W. Samek, A. Binder, G. Montavon, S. Lapuschkin, K.R. Müller, Evaluating the vi sualization of what a deep neural network has learned, IEEE Trans. Neural Networks Learn. Syst. 28 (2017) 2660–2673, https://doi.org/10.1109/TNNLS. 2016.2599820.

[64] L. Arras, G. Montavon, K.-R. Müller, W. Samek, Explaining recurrent neural network predictions in sentiment analysis, Proc. 8th work. Comput. Approaches to subi, Sentim. Soc, Media Anal. (2017).159–168. https://doi,org/10.18653/v1 W17-5221.

[65] Y. Yang, V. Tresp, M. Wunderle, P.A. Fasching, Explaining therapy predictions with laver-wise relevance propagation in neural networks, Proc, - 2018 JEEE Int. Conf. Healthc. Informatics, ICHI 2018. 2018, pp. 152–162 . https://doi,org/10.1109/ JCHL2018.00025.

[66] R. Guidotti, A. Monreale, S. Ruggieri, A survey of methods for explaining black box models, Sury. 51 (2018). https://doi,org/10.1145/3236009.

[67] C. Guo, F. Berkhahn, Entity Embeddings of Categorical Variables, (2016), pp. 1–9 http://arxiv.org/abs/1604.06737.

[68] D. Barrera, S. Brailsford, C. Bravo, H.K. Smith, No-show, https://github.com/ DBarreraFerro/No-show, (2020)

[69] L. Thomas, J. Crook, D. Edelman, Credit Scoring and its Applications, 2nd ed, SIAM Society for Industrial and Applied Mathematics, Philadelphia, PA. USA. 2017.

[70] Policia Nacional de Colombia, Crime statistics, https://www.policia.gov.co/grupoinformación-criminalidad/estadistica-delictiva, (2019).

[71] C.A. Parente, D. Salvatore, G.M. Gallo, F. Cipollini, Using overbooking to manage no-shows in an Italian healthcare center, BMC Health Serv. Res. 18 (2018) 1–12, https://doi.org/10.1186/s12913-018-2979-z

[72] S.B. Cashman, J.A. Savageau, C.A. Lemay, W. Ferguson, Patient health status and appointment keeping in an Urban Community health Center, J. Health Care Poor Underserved.15 (2007) 474–488, https://doi org/10.1353/hpu 2004.0037

[73] C.A. Odonkor, S. Christiansen, Y. Chen, A. Sathiyakumar, H. Chaudhry, D. Cinquegrana, J. Lange, C. He, S.P. Cohen, Factors associated with missed appointments at an academic pain treatment Center: a prospective year-long longitudinal study, Anesth. Analg. 125 (2017) 562–570, https://doi.org/10.1213/ANE. 0000000000001794.

[74] G.T.W. Mander, L. Reynolds, A. Cook, M.M. Kwan, Factors associated with appointment non-attendance at a medical imaging department in regional Australia: a retrospective cohort analysis. J. Med. Radiat. Sci, 65 (2018) 192–199. https://doi

org/10.1002/jmrs.284.

[75] M.P. Shrestha, C. Hu, S. Taleban, Appointment wait time, primary care provider status, and patient demographics are associated with nonattendance at outpatient gastroenterology clinic, J. Clin. Gastroenterol. 51 (2017) 433–438, https://doi.org 10.1097/MCG.0000000000000706.

[76] D. Daye, E. Carrodeguas, M. Glover, C.E. Guerrier, H.B. Harvey, E.J. Flores, Impact of delayed time to advanced imaging on missed appointments across diferent demographic and socioeconomic factors, J. Am. Coll. Radiol. 15 (2018) 713–720, https://doi.org/10.1016/j.jacr.2018.01.023.

[77] A. Topuzoǧlu, P. Ay, S. Hidiroglu, Y. Gurbuz, The barriers against childhood im munizations: a qualitative research among socio-economically disadvantaged mothers, Eur. J. Pub. Health 17 (2007) 348–352, https://doi.org/10.1093/eurpub ckl250.

[78] L. Frost, L.S. Jenkins, B. Emmink, Improving access to health care in a rural regional hospital in South Africa: why do patients miss their appointments? African J. Prim. Heal. Care Fam. Med. 9 (2017) 1–-5. https://doi.org/10.4102/phcfm.y9i1.1255.

[79] B.P. Magadzire, T. Mathole, K. Ward, Reasons for missed appointments linked to a public-sector intervention targeting patients with stable chronic conditions in South Africa: results from in-depth interviews and a retrospective review of medical records, BMC Fam. Pract. 18 (2017).1–10. https://doi,org/10.1186/s12875-017 0655-8.

[80] B.B. Wallace, M.I. MacEntee, Access to dental care for low-income adults: perceptions of afordability, availability and acceptability, J. Community Health 37 (2012) 32–39. https://doi.org/10.1007/s10900-011-9412-4.

[81] H.B. Harvey, C. Liu, J. Ai, C. Jaworsky, C.E. Guerrier, E. Flores, O. Pianykh. Predicting no-shows in radiology using regression Modeling of data available in the electronic medical record, J. Am. Coll. Radiol. 14 (2017) 1303–1309, https://doi. org/10.1016/i jacr 2017.05 007

[82] D.H. Do, J.E. Siegler, Diagnoses and other predictors of patient absenteeism in an outpatient neurology clinic, Neurol. Clin. Pract. 8 (2018) 318–326, https://doi.org 10.1212/CPJ.0000000000000488

[83] W. Verbeke, B. Baesens, C. Bravo, Profit-driven model evaluation and implementation, Profit-Driven Bus. Anal. (2017) 296–354, https://doi.org/10.1002/ 9781119443179.ch6.

[84] R. Fong, A. Vedaldi, W. Samek, G. Montavon, A. Vedaldi, L.K. Hansen, K.-R. Müller (Eds.), Explanations for Attributing Deep Neural Network Predictions BT - Explainable AI: Interpreting, Explaining and Visualizing Deep Learning, Springer International Publishing, Cham, 2019, pp. 149–167 , https://doi.org/10.1007/978- 3-030-28954-6.8.

[85] R. El Shawi, Y. Sherif, M. Al-Mallah, S. Sakr, Interpretability in HealthCare A Comparative Study of Local Machine Learning Interpretability Techniques, 2019 IEEE 32nd Int. Symp. Comput. Med. Syst, 2019, pp. 275–280 , https://doi.org/10. 1109/CBMS.2019.00065.

[86] R. Baskerville, A. Baiyere, S. Gregor, A. Hevner, M. Rossi, Design science research contributions: finding a balance between artifact and theory, J. Assoc. Inf. Syst. 19 (2018) 358–376, https://doi.org/10.17705/1jais.00495.

[87] J. Iivari, M. Rotvit Perlt Hansen, A. Haj-Bolouri, A proposal for minimum reusability evaluation of design principles, Eur. J. Inf. Syst. (2020) 1–18, https://doi.org 10.1080/0960085X.2020.1793697.

David Barrera is PhD student in the Southampton Business School at the University of Southampton and Lecturer within the Industrial Engineering Department at Pontificia Universidad Javeriana. His main research interest is the use of data science and operational research modelling approaches to support the decision making process in healthcare systems.

Sally Brailsford is Professor of Management Science within Southampton Business School at the University of Southampton. Her research is in the area of healthcare si mulation modelling: to evaluate treatments and screening programmes, or to redesign and improve service delivery. Sally has worked for over 30 years in many diferent disease fields including diabetes, cancer, mental health and HIV/AIDS, in addition to emergency care and end-of-life care.

Cristián Bravo is Associate Professor and Canada Research Chair in Banking and Insurance Analytics at the University of Western Ontario. Canada. His research focuses on the development and application of data science methodologies in the context of credit risk analytics, in areas such as deep learning, text analytics, image processing, and social network analysis. He has over 30 publications in high-impact journals and conferences in operational research and computer science. He also serves as editorial board member in Applied Soft Computing and the Journal of Business Analytics. He is the co-author of the book “Profit Driven Business Analytics", published by Wiley in October 2017 in English and Chinese.

Honora Smith is Lecturer in Operational Research (OR) within Mathematical Sciences at the University of Southampton. Her primary research interest is in the applications of OR in health care. She uses a wide variety of approaches, such as location analysis, simulation and data mining, to suggest possible improvements to health practice and organisation.
