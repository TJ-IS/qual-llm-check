---
otero_id: 4588
otero_key: "NGSNDZ6C"
title: "Stratifying no-show patients into multiple risk groups via a holistic data analytics-based framework"
authors: "Serhat Simsek; Thomas Tiahrt; Ali Dag"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113269"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Stratifying no-show patients into multiple risk groups via a holistic data analytics-based framework

![](/api/attachments/NGSNDZ6C/fulltext/images/09ff3add809951d9bf783f3efcf2f0a9029359b3d10230c08eb726f6cf429094.jpg)

Serhat Simsek<sup>a</sup>, Thomas Tiahrt<sup>b</sup>, Ali Dag<sup>c,⁎</sup>

<sup>a</sup> Feliciano School of Business, Montclair State University, Montclair, NJ 07043, USA

<sup>b</sup> Beacom School of Business, University of South Dakota, Vermillion, SD 57069, USA

<sup>c</sup> Heider College of Business, Creighton University, Omaha, NE 68178, USA

## A R T I C L E I N F O

Keywords: Data mining Healthcare informatics Medical decision making Patient no-shows

## A B S T R A C T

Accurate prediction of no-show patients plays a crucial role as it enables researchers to increase the eficiency of their scheduling systems. The purpose of the current study is to formulate a novel hybrid data mining-based methodology to a) accurately predict the no-show patients, b) build a parsimonious model by employing a comprehensive variable selection procedure, c) build a model that does not sufer due to data imbalance, and d) provide healthcare agencies with a patient-specific risk level. Our study suggests that an Artificial Neural Network (ANN) model should be employed as a classification algorithm in predicting patient no-shows by using the variable set that is commonly selected by a Genetic Algorithm (GA) and Simulated Annealing (SA). In addition, we used Random Under Sampling (RUS) to improve the performance of the model in predicting the minority group (no-show) patients. The patient-specific risk scores were justified by applying a threshold sensitivity analysis. Also, the web-based decision support tool that can be adopted by clinics is developed. The clinics can incorporate their own intuition/incentive to make the final decision on the cases where the model is not confident enough (i.e. when the estimated probabilities fall near the decision boundary). These insights enable health care professionals to improve clinic utilization and patient outcomes.

## 1. Introduction

When patients miss appointments, they impose a substantial burden on healthcare providers. Such patients are called “no-shows” and are an expensive problem as they reduce revenue and increase costs for healthcare providers [1,2]. No-show patients harm themselves, as they have poor healthcare outcomes [3]. Due to these problems, the literature has explored several strategies to mitigate both skipped appointments as well as their efects, including overbooking to reduce the number of open appointments [4,5], modifying patient behavior through incentives or deterrents [6], requiring patient prepayments [7], and imposing fines on patients who have skipped appointments [8].

Predicting patient no-shows plays a crucial role as it enables researchers to increase the eficiency of their scheduling prescription (through simulation and optimization). In other words, a high-quality predictive model is essential to constructing a high-quality prescriptive model. Researchers have a large number of complex datasets available to them, providing opportunities to increase useful knowledge through predictive analytics. Current machines can host eficient but computationally expensive data analytical models [9]. The combination of computing power and data-driven models leads to unprecedented op portunities in solving challenging problems.

We developed a data-driven method to classify no-show patients into five categories, (1) very low risk, (2) low risk, (3) moderate risk, (4) high risk, and (5) very high risk, by employing eficient machine learningbased predictive methods, heuristic-based optimization models, and data balancing algorithms. It should be clearly indicated that our study targets only the predictive modeling side of the problem, as it does not attempt to come up with a prescriptive solution (i.e. scheduling). Having said that, scheduling systems can be designed based on these insights to optimize the utilization of healthcare resources and develop more eficient no-show management systems as the present study pro vides the patient-specific (no-show) risk levels obtained through a highly parsimonious model. In addition, we examine the efects of the primary factors that lead to no-shows. Our aim is to identify and pinpoint the critical factors involved in the no-show problem, such as which patient types regularly miss appointments, and whether there are discernable patterns at diferent time scales, meaning whether certain times of the day, month or year have a higher probability of no-shows, etc. Such insights can help healthcare providers implement mitigation strategies based on root causes by deploying prediction models and intervention systems, and can ofer healthcare providers an accurate decision support system that can help them understand their patients' behaviors and manage their resource deployment accordingly.

The remainder of this paper is organized as follows. We provide a comprehensive literature review in Section 2 to identify/show the gap the present study fills and the potential benefits it contributes to the noshow problem. The dataset, data cleaning methodology, sampling methods, variable selection process, the prediction/classification models, the clustering methods, and the information fusion based sen sitivity analysis used in the current study are presented in Section 3. Section 4 is designated for the results and insights obtained via the hybrid data analytic methodology adopted in the current study. The decision support tool developed is explained in Section 5. Finally, the paper closes with the conclusions, research limitations and suggestions for potential future research directions, which are given in Section 6.

## 2. Literature review

Extensive research has been conducted with regards to no-shows or missed appointments since the 1960s. At that time, scientists studied the phenomenon using the term “broken appointments” instead of noshows [10–12]. In subsequent decades, “no-shows” became the foremost term used in academic studies of these problems. The existing studies focused on a) adverse efects of no-shows, b) strategies to reduce or prevent no-shows, and c) prediction of no-shows using data analytical techniques. In this section, we primarily focus on the third category as it is the category that our proposed study falls under. Having said that, for the sake of completeness, we refer the readers to [13–21], and [22–31] to have detailed information about the first and the second research streams, respectively.

To exemplify the studies in this research stream, Liu et al. [32] and Feldman et al. [33] proposed a scheduling methodology that employed Markov Decision Process (MDP) to model/predict the no-show probabilities. In their studies, the no-show probabilities were set as the function of lead time and previous no-show rates. These studies developed and introduced static and dynamic scheduling of patient appointments, in which they validated their scheduling strategies (as well as the noshow probabilities) through simulation by using Primary care datasets.

Samorani and LaGanga [34] employed a Bayesian classifier to predict the no-show patients, then used those outcomes as the inputs to a heuristic scheduling process to improve utilization. They used a mental health clinic dataset, and reported their sensitivity and specificity rates as (0.7, 0.7), (0.9, 0.5), (0.6, 0.8), respectively, for the three diferent probability thresholds determined by the authors.

Glowacka et al. [35] employed Association Rule Mining (ARM) to model the no-show probabilities by using a dataset from an outpatient clinic, and they used a set covering optimization method to derive three manageable sets of rules for patient sequencing. Later, a simulation method was used to evaluate/compare the models and to determine the

number of patients.

In a more recent study, Daggy et al. [36] used Veterans Afairs (VA) medical center data to estimate the probability of missing appointments; they regressed diagnosis, marital status, days from last visit, previous no-shows, insurance, prior appointments, season, patient age, travel distance, and lead time. They employed a logistic regression (LR) model with backward variable selection to obtain the no-show probabilities and deployed them into the simulation model. They reported only the AUC rate, which was reported as 0.82. Then, they employed an overbooking policy to optimize a schedule of patients and tested/validate through utilizing Monte Carlo simulation.

In a later study, Alaeddini et al. [37] developed a hybrid probabil istic model based on LR and empirical Bayesian inference to predict the probability of no-shows. Their dataset included general patient social and demographic information and individual clinical appointment attendance records obtained from a VA medical center. The central goal of their study was to obtain reliable no-show probabilities. The classi fication accuracy that they obtained was 0.799. In one of the most recent studies, Lenzi et al. [38] employed logistic regression with a backward stepwise variable selection method to obtain a simpler model. The AUC rate that they reported was 0.81, by using a dataset obtained from a primary care healthcare facility. Specifically dedicated to pediatric patients, Huang and Hanauver [39] employed an LR model to predict no-show patients. The main goal of their study was to determine the optimum probability threshold value to maximize the accuracy level via sensitivity analysis on the no-show probabilities. They employed the Likelihood ratio (Chi-square) to select the significant variables. Through simulation, they demonstrated that their method significantly reduced patient wait times by at least 6%, overtime by 27%, and total cost by 3% when compared to other flat-overbooking methods. Topuz et al. [40] proposed a probabilistic prediction framework based on the elastic net (EN) variable-selection methodology in tegrated with the Bayesian Belief Network (BBN). Their study predicted the “no-show probability of the pediatric patient(s)” using demographics, socioeconomic status, current appointment information, and appointment attendance history of patients and their families. Their study specifically focused on the interrelations of predictors of noshows via employing the BBN. The AUC and overall accuracy that they reported in their study were 0.691 and 0.743, respectively.

In this study, a hybrid data analytical methodology is proposed where; a) various statistical- and machine- learning algorithms were employed to predict the primary clinic no-shows, b) a comprehensive variable selection procedure was implemented via using heuristic op timization techniques, Genetic Algorithms (GA) and Simulated Annealing (SA) c) data balancing such as Synthetic Minority Oversampling Technique (SMOTE), and Random Under Sampling (RUS) were employed to increase the ability of the predictive models in detecting the minority class samples and d) patients' multinomial risk levels (from very low-risk, to very high-risk) of being a no-show were determined through k-means clustering algorithm and finally e) a webbased decision support tool is developed that can be used by the medical decision-maker.

Table 1  
Summary of the relevant literature.

<table><tr><td>Study</td><td>Data</td><td>Modeling</td><td>Variable selection</td><td>Imbalance handling</td><td>Decision support tool</td><td>Verification of probabilistic quality</td></tr><tr><td>Liu et al. [32] Feldman et al. [33]</td><td>Primary care</td><td>MDP</td><td>-</td><td>-</td><td>-</td><td>Simulation</td></tr><tr><td>Samorani and LaGanga [34]</td><td>Mental health clinic</td><td>Bayesian classifier</td><td>-</td><td>-</td><td>-</td><td>Simulation</td></tr><tr><td>Glowacka et al. [35]</td><td>Outpatient clinic</td><td>ARM</td><td>-</td><td>-</td><td>-</td><td>Simulation</td></tr><tr><td>Daggy et al. [36]</td><td>VA outpatient</td><td>LR</td><td>Stepwise backward</td><td>-</td><td>-</td><td>Simulation</td></tr><tr><td>Alaeddini et al. [37]</td><td>VA medical center</td><td>LR with Bayesian update</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Lenzi et al. [38]</td><td>Primary care</td><td>LR</td><td>Stepwise backward</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Huang and Hanauveret al. [39]</td><td>Pediatrics</td><td>LR</td><td>Likelihood ratio</td><td>-</td><td>-</td><td>Simulation</td></tr><tr><td>Topuz et al. [40]</td><td>Pediatrics</td><td>Bayesian belief network</td><td>Elastic net</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Proposed</td><td>Primary care</td><td>ANN, RF, LR, EL</td><td>GA, SA</td><td>SMOTE, RUS, ROS</td><td>Web-based</td><td>Sensitivity Analysis</td></tr></table>

Table 1, which summarizes the most relevant studies that fall into the third research stream (prediction of no-shows using data analytical techniques), shows that our contribution that has direct impact on the prediction quality comes from b and c, as no study we know of exists that; employs comprehensive variable selection methodology that is computationally eficient (when compared to exhaustive optimization algorithms) and minimizes the risk of sufering from collinearity, overfitting and being trapped in local minima. Although [36,38–40] used variable selection methods that are computationally eficient, these methods are prone to collinearity, overfitting or being trapped in the local minima. Moreover, in the no-show prediction literature, there is no study (we know $_ \mathrm { o f ) }$ that employs data balancing algorithms to strengthen the sensitivity of the model in detecting the minority samples. Such contributions are discussed in Section 3.2 and 3.3, and the results that come from these specific contributions are presented in Table 6. In addition to the contributions to the prediction quality, a web-based decision support tool is developed, which can be considered as the practical contribution of the proposed method. With that said, in the case of such tools being adopted by the medical centers, building a parsimonious model becomes more necessary since the reduction in the data entry and the computation time becomes crucially important, as it would enable medical clinics to react in the timeliest manner.

## 3. Methodology

To provide practitioners with better information for developing a scheduling system, we propose a framework that can be used by clinic to minimize their no-show patient cost. Fig. 1 shows the proposed fourstep methodology.

In the first step, we began with a healthcare provider dataset from the state of Espírito Santo, Brazil. The patient data were then downloaded from the Kaggle website and were preprocessed in preparation for the prediction/classification algorithms. The second step was to select the relevant predictors to be deployed into prediction/classification algorithms. The following two optimization techniques were employed to determine these potential predictors: simulated annealing (SA) and genetic algorithm (GA). In the third step, we balanced the da taset because the number of no-show patients in the dataset is sig nificantly less than patients who kept their appointments. To do this, we used random under-sampling (RUS), random over-sampling (ROS), and the synthetic minority over-sampling technique (SMOTE). Balancing applied solely to the training set. To split the dataset into training and test sets, a 10-fold cross-validation technique was implemented. Three classification models were trained: Logistic regression (LR), Random forests (RF), and Artificial neural networks (ANN), along with the variable sets obtained through the optimization algorithms (SA and GA), and the intersection of these variable sets. In addition, an ensemble learning model was developed by combining the aforementioned three models. In the fourth step, the individual performance of the classification/prediction models was analyzed. After finding the best performing variable set with the best classification algorithm and the best balancing technique, we explored the importance of these predictors using sensitivity analysis. An information fusion method was then used to combine essential variables. Lastly, patients were classified into five risk levels with regard to patient-specific no-show risk scores and a decision support tool incorporating the best performing model is developed. The details of each step of the methodology are provided in the following subsections.

## 3.1. Data acquisition and preparation

The dataset was acquired from the data science competition plat form Kaggle [41]. The dataset has 110,528 observations with 14 variables, and contains two categories: (1) appointment characteristics (appointment date, appointment scheduling time, appointment $I D ,$ patient ID); and (2) demographic information (age, gender, financial status, alcoholism, handicap, and patient health). In addition to these variables, new variables were derived from the originals. For example, a lead time variable was created using the number of days between when the ap pointment day was scheduled and the appointment day itself.

Similarly, we derived calling time, appointment day, appointment time, and appointment month variables from the appointment date. The patient appointment records were used to create prior no-show (proportion of prior missed appointments) and time between appointments (the time elapsed between two consecutive appointments) variables. Lastly, outliers and irrelevant variables like Patient ID and Appointment ID were pruned from the dataset. After variable extraction, we obtained a dataset with 72,602 observations and 17 variables. Brief definitions of these predictors are provided in Table 2.

## 3.2. Variable selection

Variable selection is the extraction of the most relevant subset of variables from the original set of variables. Performing a comprehensive variable selection enables researchers to find simple models that eficiently predict the target variable. Performing a comprehensive variable selection method enables researchers to find simple models that eficiently predict the target variable. However, finding an optimal subset of variables for big datasets is a challenging task due to the huge search space.

Univariate (filter) methods and wrapper methods are the two main types of variable selection methods. In the filter-based methods, the individual relationships between the variables are examined, during the data exploration process prior to the training phase. On the other hand, wrapper methods are “wrapped” around the prediction/classification algorithm, which adds/removes the potential predictors according to the pre-determined objective. Therefore, they are part of the model training process.

In the extant no-show literature, in order to find an optimal subset of variables, wrapper methods, such as backward- and forward stepwise, elastic net, and likelihood ratio (as can be seen from Table 1) are em ployed to perform variable selection. However, these methods perform poorly when collinearity among the predictors exists [42], although they are relatively time-eficient algorithms. Similarly, even though the elastic net is proposed to overcome the issue of collinearity, which comes with a computational cost, it sufers from overfitting due to the flexibility of the estimator [43]. Exhaustive searches, on the other hand, require computational efort that grows exponentially, thereby being prohibitively time-consuming and costly (i.e., evaluating all combina: tions of candidate subsets, which is $2 ^ { 1 6 }$ in our case, as we have 16 independent variables after the data preparation phase). Therefore, in the present study, we sought an accurate, parsimonious model, without the computationally intense demands of the exhaustive search. Therefore, two metaheuristic (wrapper-based) algorithms, SA and GA were em ployed due to their advantages of being able to avoid local minima, collinearity and overfitting, when the parameters are tuned/customized accordingly [44,45], as explained in greater detail, in Section 3.2.1 and 3.2.2. Moreover, possible combinations of the variable sets obtained through GA and SA are considered, as the empirical results showed that the combination of multiple variable selection algorithms can lead to better performing models [46].

## 3.2.1. Simulated annealing

Simulated annealing, inspired by the annealing process, seeks a global optimum for a given function [45]. The SA algorithm mimics the annealing process using a temperature variable that initially has a large (hot) value, then cools down (decreases) at each iteration step. SA always accepts better solutions, yet it also randomly accepts worse solutions as long as the system temperature is high. The system temperature cools down gradually, thereby restricting the search space. The central premise of simulated annealing algorithms is to “jump” out of local minima that the algorithm otherwise cannot escape, thereby gaining the ability to pursue the search in other regions. In the optimal case, the algorithm finds the global maximum [47].

![](/api/attachments/NGSNDZ6C/fulltext/images/243c149c88af33e974e6f2a3fa85d2f43b89f7e0f666220d208c5e23ef78d92c.jpg)  
Step 4: Extraction of variable importance, patient no-show risk score and development of a Decision Support Tool  
Fig. 1. An outline of the proposed data analytics methodology.

In this study, the proposed simulated annealing algorithm utilizes the Random Forest as it is invulnerable to both the issue of the multi collinearity and the overfitting, contrary to many other machine learning models [48]. Moreover, as the SA algorithm occasionally moves toward a worse solution to avoid falling into local minima, there is a chance that the algorithm goes the wrong direction. To mitigate this problem, the algorithm is dictated to reset the current solution (variable subset) to the best solution found if 50 consecutive iterations do not provide an improvement in fitness. Lastly, the algorithm is run 10 times with a diferent initial random variable subset, which enables the algorithm to allocate diferent trials to the region of the search space in an attempt to find the best solution possible.

## 3.2.2. Genetic algorithm

Genetic Algorithms (GA), inspired by biological evolution, seek an optimal solution both for continuous (diferentiable or not) and discrete functions [49]. Moreover, GAs do not require specific knowledge about the problem under study and usually perform better than traditional variable selection algorithms [50]. The GA algorithm generates an initial population of chromosomes represented by n number (n is the number of variables in the dataset) of binary strings, each of which consists of “0” and “1”, denoting the presence or absence of a variable, respectively. The GA algorithm mates the chromosomes having a relatively higher fitness function with each other to create new members of the next generation. This process is called crossover. In addition, the algorithm can mutate the chromosomes to create new members. Namely, the algorithm can exclude or include some of the variables in the chromosomes at random by changing a value of “0” in the binary string to “1” and vice versa; this process is pronounced as mutation.

The present study proposes a genetic algorithm that consists of the initial parameters summarized in Table 3.

The algorithm, as in SA, is designed to use the RF forest model as a custom fitness function, the parameters of which are tuned via the kfold cross-validation. The probability of crossover between pairs of chromosomes was kept high, at 0.8, to promote the algorithm to move the next generations toward the space defined by the fittest chromosomes. Moreover, even though it is a common practice to keep the mutation probability small, say < 0.05, this probability was set to 0.1, encouraging the algorithm to diversify chromosomes, and thereby providing the algorithm the ability to escape local optima, with the trade-of of having longer execution time. Lastly, the number of elite chromosomes is determined to be 3 (elitism), meaning that three chro mosomes with the highest fitness value are pushed to the next gen eration without being exposed to any of the reproduction processes such as crossover and mutation.

Table 2  
A description of predictor variables.

<table><tr><td>Variable name</td><td>Definition of variable</td></tr><tr><td>Age</td><td>Chronological patient age</td></tr><tr><td>Gender</td><td>Patient sex</td></tr><tr><td>Month</td><td>The month of the appointment</td></tr><tr><td>Appointment day</td><td>Day (1-31) of the appointment</td></tr><tr><td>Scheduling day</td><td>The day an appointment was scheduled to take place</td></tr><tr><td>Lead time</td><td>Waiting time for the up-coming appointment</td></tr><tr><td>Calling time</td><td>The time a patient called to schedule an appointment</td></tr><tr><td>Appointment reminder</td><td>Whether a reminder message or call is received</td></tr><tr><td>Alcoholism</td><td>Whether the patient is an alcoholic</td></tr><tr><td>Financial aid</td><td>Whether the patient has financial support</td></tr><tr><td>Handicap</td><td>Whether the patient has a permanent physical impediment</td></tr><tr><td>Hypertension</td><td>Whether the patient has high blood pressure</td></tr><tr><td>Diabetes</td><td>Whether the patient has diabetes</td></tr><tr><td>Neighborhood</td><td>Hospital location</td></tr><tr><td>Time between appointments</td><td>The elapsed time between two consecutive appointments</td></tr><tr><td>Prior no-shows</td><td>The proportion of no-shows</td></tr></table>

Table 3  
GA parameters.

<table><tr><td>GA Parameter</td><td>Value</td></tr><tr><td>Population size</td><td>100</td></tr><tr><td>Number of generations</td><td>250</td></tr><tr><td>Population type</td><td>Binary string</td></tr><tr><td>Crossover probability</td><td>0.8</td></tr><tr><td>Mutation probability</td><td>0.1</td></tr><tr><td>Elitism</td><td>3</td></tr></table>

## 3.3. Sampling techniques

The dataset used in the present study includes the records of 15,196 no-show patients and 57,406 show-up patients, thereby being an imbalanced dataset. Having such unequal class size in the target variable (i.e. \~20% no-shows, and \~80% show-ups) can lead to machine learning algorithms taking a naïve approach to minimize the loss function by classifying all the instances as the majority class (show-ups, in our case). In doing so, the machine learning algorithms maximize overall accuracy by generating high predictive accuracy for the majority class and low predictive accuracy for the minority class (e.g. see the first four rows of Table 6) [51].

In order to solve the learning problem from imbalanced data, sev eral balancing techniques such as sampling methods, cost-sensitive, kernel- and recognition-based learning methods are proposed [52]. In the present study, the sampling methods are used to deal with the existing imbalance problem in the dataset as they conform with any type of machine learning algorithms in contrary to the kernel- and re cognition-based learning methods. Similarly, in this study, cost-sensitive learning methods are not preferred as they require specification of the costs associated with misclassifying instances, which are not available to us.

Sampling methods are used to decrease or eliminate the imbalance. Approaches include minority class oversampling, majority class undersampling, or a blend of both methods [53,54]. However, there is no absolute winner among the techniques as diferent modeling techniques react diferently to sampling. Thus, we employed three wellknown resampling techniques during the model training process. It is noteworthy that none of the studies proposed in the literature has employed any of the balancing techniques (see Table 1).

The sampling techniques used included 1) random under-sampling (RUS), 2) random over-sampling (ROS), and 3) synthetic minority oversampling technique (SMOTE). Among these three, RUS randomly eliminates some majority-class observations until the majority class count is approximately equal to the minority-class observation count. Similarly, ROS increases the number of minority-class observations by randomly including existing samples as new samples until the number of observations in the minority class equals the majority class. SMOTE, on the other hand, increases the count of the minority class by inter polating pairs of close neighbors in the minority class randomly, generating synthetic instances. SMOTE incorporates two operational parameters that can be tuned by researchers to enhance the model's learning potential, thus producing better results. One of these parameters is the number of nearest neighbors that the SMOTE algorithm uses to determine the number of the closest instances used to the query instance to synthesize a new instance. The second parameter is the rate of under- and over-sampling that controls the amount of sampling of minority and majority classes. In the present study, the k-fold crossvalidation technique was used to optimize these parameters.

## 3.4. Predictive modeling

In this study, we employed ANN, RF, and LR models to predict whether a given patient will be a no-show or not. In addition, an Ensemble Learner (EL) was created by using combinations of ANN, RF, and LR. Specifically, the mean of the no-show probabilities estimated by the models for each patient is calculated, and the decisions on the likelihood of the patients being a no-show are made accordingly. Note that we also consider taking the majority vote into account to make an ultimate decision on the likelihood of the patients being a no-show, yet the results were inferior compared to the probabilistic average approach. The central premise of creating an EL model is that empirical studies have shown that EL-based algorithms may produce more accurate results compared to single algorithms [55,56]. However, coun terexamples exist [57]; therefore, both ensemble and single learning algorithms were included.

## 3.4.1. Artificial neural networks

Artificial Neural Networks (ANNs). inspired by the work theory of human brains, are sophisticated analytical techniques that can model complicated, nonlinear functions [58]. In this study, the most commonly used neural network, namely the single hidden layer back-propagation network (vanilla) was deployed. The vanilla model uses the back-propagation algorithm to find the solution to the optimal parameters. The propagation process is repeated until either the maximum number of iterations is reached or the estimates of the error rate start increasing.

The neural networks involve a great number of parameters to be estimated, thereby being prone to overfitting the data. To mitigate this problem, the model is regularized using the penalized loss function, in which the penalty term is added on the parameter estimations which was also known as weight decay.

Tuning the parameters of the ANN model is a challenging task since there is no explicit way to select optimal parameters. Consequently, we tuned all parameters of the ANN model, (weight decay, learning rate, and the number of units in the hidden layer), using cross-validation.

## 3.4.2. Random forests

Random Forests (RF), introduced by Breiman in 2001 [48], is a treebased machine learning algorithm that recursively partitions data using a plurality of decision trees. The RF algorithm uses the bootstrap sampling technique to grow unique trees, which overcomes overfitting and renders the algorithm robust against noise in the data set. Moreover, RF randomly samples a portion of the predictors at each tree split but uses only one predictor to divide the data into two partitions. Limiting the predictors at each node decorrelates the trees produced. Otherwise, a strong predictor, or a few strong predictors, will dominate and grow strongly correlated trees. The tree-growing process yields a forest of multiple trees. Then, RF tallies each tree's vote and chooses the class by majority vote. In the present study, the parameters of the RF were tuned using the cross-validation technique, and intentionally dictated the model to grow an odd number of trees to avoid possible ties in the decision-making process. For detailed information regarding RF, see [48,59].

![](/api/attachments/NGSNDZ6C/fulltext/images/52f6bda935706b3b4eff28018944b9b9cc888c16efc3a924858e445942d96917.jpg)  
Fig. 2. Sensitivity analysis for predictor variables.

## 3.4.3. Logistic regression

Logistic Regression (LR) is a member of the generalized linear models where the distribution of the response variable is assumed to belong to the exponential family of distribution [60]. Researchers mainly use LR for predicting dichotomous dependent variables. LR uses the logit function to relate the probability of the occurrence of events to the predictor variables. In a two-class problem (as is the case in the present study), when the odds of the occurrence exceed 1, the instance can be classified as one, and zero otherwise. The mathematical defini tion of the standard logistic function can be defined as follows:

$$
\operatorname{logit} (p) = \ln \left(\frac {p}{1 - p}\right) = \boldsymbol {\beta} \mathbf {X}\tag{1}
$$

where $\beta$ and X are the coeficient and the input vector, respectively, and p is the probability of the target variable equal to one. The ultimate classification, then, is made as follows.

$$
P r e d i c t i o n = \left\{ \begin{array}{l} " 1", i f \frac {p}{1 - p} > 1 \\ " 0", i f \frac {p}{1 - p} <   1 \end{array} \right.\tag{2}
$$

where $\frac { p } { 1 - p }$ is called the odds.

The researchers can manipulate the threshold value of the odds to obtain the desired level of sensitivity and specificity. For many programming languages, the default threshold for the odds is 1, or in other words, 0.5 for the p.

## 3.5. Sensitivity analysis

The relative importance of predictor variables can be obtained and interpreted in statistical models, such as generalized linear models, lasso, ridge regression, lars, and others. [42]. Conversely, black-box models (models with no closed mathematical form), such as ANNs, do not provide direct access to the mechanisms in the underlying process. Consequently, alternatives are required to provide insight into black box models. One path to insights is sensitivity analysis [61].

Sensitivity analysis determines the influence of independent variables in predictive models. The algorithm includes each of the predictors, calculates the model error, then excludes one of the predictors and recalculates the model error. The ratio of the model error with the variable to the model error without the variable is the sensitivity measure, indicating how sensitive the model is to the predictor [62]. This process is repeated recursively. Saltelli introduced a sensitivity measure used to rank the relative importance of the variables for each predictive model. Its form is [63]:

$$
S _ {i} = \frac {V _ {i}}{V (y)} = \frac {V (E (y \mid x _ {i}))}{V (y)}\tag{3}
$$

where the binary response variable is $y ,$ and $V ( y )$ is the unconditional output variance. E is the expectation operator, integrated over $x _ { i \cdot }$ The sensitivity analysis was applied to the best performing model, and the normalized sensitivity of the variable importance, as described by Saltelli et al. [64], was calculated (see Fig. 2).

## 3.6. Information fusion

Information Fusion (IF) gathers information obtained through different algorithms to reduce model uncertainty, improve robustness, and information completeness. Studies have shown that combining multiple predictive models produces more information with greater accuracy when compared to single models [65,66]. The IF aggregation can take numerous forms. In this study, we adopted the method demonstrated in the work of Dag et al. [53] to combine sensitivity information gained from each model. Formally, the IF technique used aggregates the sensitivity measures obtained from each model into an overall sensitivity measure as follows:

$$
S _ {j} (f u s e d) = \sum_ {k = 1} ^ {p} \alpha_ {k} S _ {k, j},\tag{4}
$$

where $S _ { k , j }$ is the normalized sensitivity measure of th ${ \bf \nabla } : j ^ { t h }$ variable in the $k ^ { t h }$ model and αis the AUC score of the $k ^ { t h }$ model.

The fused sensitivity scores enable us to discover the relative importance of each variable in identifying no-show patients despite the black-box nature of the models. The details of the fused variable importance results are discussed in Section 4.2.

## 4. Results & discussion

## 4.1. Variable selection results

As shown in Table 4, the optimization algorithms found diferent sub-optimal solutions due to their difering algorithmic nature. For example, the GA algorithm classified age and month as principal predictors in explaining the variation in the dataset, while the SA algo rithm ignored them. Similarly, SA considered handicap as a crucial predictor, but GA did not. However, both arrived at the same conclusion for appointment day, lead time, appointment reminder, alcoholism, financial aid, diabetes, prior no-show, and time between appointments. Lastly, neither GA nor SA considered gender, scheduling day, calling time, hypertension, and neighborhood as essential variables.

Table 4  
Variable selection results.

<table><tr><td>Variable Names</td><td>Simulated annealing</td><td>Genetic algorithm</td></tr><tr><td>Age</td><td></td><td>√</td></tr><tr><td>Gender</td><td></td><td></td></tr><tr><td>Scheduling day</td><td></td><td></td></tr><tr><td>Appointment day</td><td>√</td><td>√</td></tr><tr><td>Month</td><td></td><td>√</td></tr><tr><td>Lead time</td><td>√</td><td>√</td></tr><tr><td>Calling time</td><td></td><td></td></tr><tr><td>Appointment reminder</td><td>√</td><td>√</td></tr><tr><td>Alcoholism</td><td>√</td><td>√</td></tr><tr><td>Financial aid</td><td>√</td><td>√</td></tr><tr><td>Handicap</td><td>√</td><td></td></tr><tr><td>Hypertension</td><td></td><td></td></tr><tr><td>Diabetes</td><td>√</td><td>√</td></tr><tr><td>Neighborhood</td><td></td><td></td></tr><tr><td>Prior no-show</td><td>√</td><td>√</td></tr><tr><td>Time between appointments</td><td>√</td><td>√</td></tr></table>

The GA and SA optimization algorithms we used are considered metaheuristic techniques in that they do not explore the entire search space and thus, cannot guarantee a globally optimal solution. To compensate for this shortcoming, we considered using the possible combinations of these methods alongside the variable sets provided by GA and SA only. Specifically, the intersection set and union set of the variable sets given by the two algorithms were employed. In our preliminary analysis, the intersection of the predictor variables outperformed the union, presumably because of the issue of overfitting the data. Therefore, we include the intersection only (see Table 5). On the other hand, the intersection set not only provided promising results but also advanced the parsimony (simplicity) of the model, which is one of the essential products of the current study.

## 4.2. Classification results

The following four well-known performance evaluation metrics were used: accuracy, sensitivity, specificity, and area under the curve (AUC) to compare the results obtained through diferent alternatives/ combinations. See Powers [67] for a detailed explanation of the measures.

The models were trained with each of the variable subsets, which were defined in the previous sections (GA, SA, and the intersection of these two), along with the balancing techniques. The results were evaluated using 10-fold cross-validation, and the four measures of the performance of the predictive models were summarized numerically (i.e. accuracy, sensitivity, specificity, and AUC). Table 5 presents the classification/prediction results, with the standard deviation of each measure delimited by parentheses. The best results are set in boldface for each measure. The best AUC results (0.844) were found in the EL and ANN models, using RUS as the balancing algorithm and GA as the variable selection algorithm.

Similarly, the EL model, using the predictor variables suggested by GA and balanced via SMOTE, produced the best accuracy (0.786) and specificity (0.814). Finally, the ANN model, using the predictors ob tained from the intersection of the variable set of GA and SA and ba lanced by the RUS, obtained the best sensitivity results (0.792).

We used the sensitivity metric as a primary criterion as it is crucially important to detect no-show patients correctly so that necessary actions can be taken to mitigate any possible cost caused by no-show patients. The ANN model, when trained with data balanced by RUS, and intersection variables selected by GA and SA, outperformed all of the other options in Table 5.

On the other hand, Table 6 shows the performance of the predictive models developed with and without implementing the proposed data analytics technique. As expected, the models developed without im plementing the balancing methods produced low sensitivity scores (as low as 0.365 and as high as 0.426), while producing relatively high specificity scores. Such outcomes clearly indicate that these models have low power to classify no-show patients correctly, emphasizing the crucial necessity of performing data balancing. Similarly, the models developed using all variables fail to produce better sensitivity scores compared to the models using the intersection of the variable set of GA and SA, with the exception of the LR model that produces a sensitivity score of 0.728 – higher than the sensitivity score achieved by the parsimonious LR model. It should be noted that none of the models is able to produce as high a sensitivity score as the ANN model (0.792) developed by implementing the proposed methodology.

After selecting the ideal model (ANN with RUS and the intersection of SA and GA variables), the importance of the variables used in building the ideal (ANN) model was investigated via sensitivity analysis. Namely, ten diferent variable importance reports were produced by running 10 diferent models. Then, the reports obtained from the models were combined via the IF technique (which was discussed in detail in Section 3.6).

Fig. 2 shows the contribution (importance) of each variable in predicting the outcome. It is important to note that these numbers present the relative importance of each variable. For example, the contribution of prior no-show is 28.08% and diabetes is 12.03% in predicting the outcome variable. Thus, the two comprise 40.11% of the total prediction/classification power.

The findings of the present study confirm most of what has been published in the related literature. To exemplify, many studies have reported that patients with a high prior no–show history are more likely to miss their next appointments, confirming that the prior no-show is one of the most important predictors cited in the literature [36,39,68–73].

Similarly, the literature reported that patients with diabetes have no-show rates as high as 40% [74]. Bindmand et al. [75] have reported that chronic medical conditions such as diabetes, can require acute care service. Therefore, this might explain why patients with diabetes who fail to show up for appointments have a higher risk of being hospitalized, thereby missing their next appointments.

Moreover, the relative contributions of appointment reminder, alco holisim, lead time, and financial aid are 11.95%, 11.23%, 10.64%, and 9.48%, respectively. The importance of these variables is also well articulated in the literature. For example, researches argued that appointment reminders such as SMS, phone calls, and email reminders, are efective at reducing no-show rates of patients [27,76–78]. The reduction has been reported to be 75% [79]. Similarly, Dantas et al. [80] have shown that patients with addiction to alcohol are more likely to miss their appointments. Furthermore, researchers comparing four significant factors (age, payer, no-show history, and lead-time) found that lead-time was the strongest predictor of no-show patients [81]. Another study, using data from an ophthalmology clinic, confirmed that longer lead times increased no-show rates [82].

On the other hand, Norris et al. [28] have shown that financial aid is one of the main reasons associated with patient no-shows. This claim supported by Horsley et al. [83] asserts that Medicaid vs. non-Medicaid use was a significant predictor of missed appointments, with Medicaid patients having a much higher incidence of no-shows.

Lastly, we found that time between appointments and appointment day are two other important variables in the prediction of no-show patients having relatively lower contributions: 8.62%, and 7.65%, respectively.

Table 5 Classification results.

<table><tr><td>Variable set</td><td>Balancing method</td><td># of variable</td><td>Model</td><td>AUC</td><td>Accuracy</td><td>Sensitivity</td><td>Specificity</td></tr><tr><td rowspan="12">Simulated annealing</td><td rowspan="4">SMOTE</td><td rowspan="4">9</td><td>LR</td><td>0.805(0.004)</td><td>0.735(0.006)</td><td>0.706(0.011)</td><td>0.743(0.008)</td></tr><tr><td>RF</td><td>0.818(0.006)</td><td>0.766(0.006)</td><td>0.703(0.018)</td><td>0.782(0.010)</td></tr><tr><td>ANN</td><td>0.838(0.006)</td><td>0.757(0.009)</td><td>0.734(0.030)</td><td>0.763(0.018)</td></tr><tr><td>EL</td><td>0.837(0.004)</td><td>0.770(0.005)</td><td>0.702(0.017)</td><td>0.788(0.008)</td></tr><tr><td rowspan="4">ROS</td><td rowspan="4"></td><td>LR</td><td>0.805(0.004)</td><td>0.727(0.006)</td><td>0.723(0.012)</td><td>0.728(0.008)</td></tr><tr><td>RF</td><td>0.817(0.005)</td><td>0.756(0.004)</td><td>0.730(0.017)</td><td>0.763(0.008)</td></tr><tr><td>ANN</td><td>0.839(0.005)</td><td>0.749(0.008)</td><td>0.756(0.013)</td><td>0.747(0.009)</td></tr><tr><td>EL</td><td>0.837(0.004)</td><td>0.758(0.005)</td><td>0.733(0.012)</td><td>0.765(0.007)</td></tr><tr><td rowspan="4">RUS</td><td rowspan="4"></td><td>LR</td><td>0.805(0.004)</td><td>0.751(0.005)</td><td>0.664(0.013)</td><td>0.775(0.007)</td></tr><tr><td>RF</td><td>0.824(0.006)</td><td>0.771(0.004)</td><td>0.701(0.017)</td><td>0.789(0.006)</td></tr><tr><td>ANN</td><td>0.838(0.004)</td><td>0.768(0.006)</td><td>0.707(0.013)</td><td>0.784(0.009)</td></tr><tr><td>EL</td><td>0.837(0.004)</td><td>0.777(0.004)</td><td>0.688(0.013)</td><td>0.800(0.005)</td></tr><tr><td rowspan="12">Genetic algorithm</td><td rowspan="4">SMOTE</td><td rowspan="4">10</td><td>LR</td><td>0.806(0.004)</td><td>0.734(0.007)</td><td>0.714(0.012)</td><td>0.739(0.008)</td></tr><tr><td>RF</td><td>0.831(0.006)</td><td>0.782(0.005)</td><td>0.686(0.013)</td><td>0.807(0.005)</td></tr><tr><td>ANN</td><td>0.837(0.004)</td><td>0.758(0.010)</td><td>0.728(0.030)</td><td>0.766(0.020)</td></tr><tr><td>EL</td><td>0.843(0.005)</td><td>0.786(0.006)</td><td>0.680(0.009)</td><td>0.814(0.009)</td></tr><tr><td rowspan="4">ROS</td><td rowspan="4"></td><td>LR</td><td>0.806(0.004)</td><td>0.727(0.007)</td><td>0.732(0.012)</td><td>0.726(0.008)</td></tr><tr><td>RF</td><td>0.827(0.006)</td><td>0.771(0.007)</td><td>0.696(0.012)</td><td>0.791(0.009)</td></tr><tr><td>ANN</td><td>0.837(0.007)</td><td>0.761(0.011)</td><td>0.725(0.028)</td><td>0.770(0.019)</td></tr><tr><td>EL</td><td>0.842(0.005)</td><td>0.776(0.005)</td><td>0.701(0.010)</td><td>0.796(0.007)</td></tr><tr><td rowspan="4">RUS</td><td rowspan="4"></td><td>LR</td><td>0.806(0.004)</td><td>0.729(0.006)</td><td>0.727(0.011)</td><td>0.730(0.007)</td></tr><tr><td>RF</td><td>0.833(0.006)</td><td>0.745(0.006)</td><td>0.777(0.015)</td><td>0.737(0.008)</td></tr><tr><td>ANN</td><td>0.844(0.005)</td><td>0.742(0.007)</td><td>0.781(0.012)</td><td>0.732(0.010)</td></tr><tr><td>EL</td><td>0.844(0.005)</td><td>0.757(0.005)</td><td>0.750(0.012)</td><td>0.759(0.007)</td></tr><tr><td rowspan="12">Intersection</td><td rowspan="4">SMOTE</td><td rowspan="4">8</td><td>LR</td><td>0.805(0.004)</td><td>0.735(0.006)</td><td>0.706(0.011)</td><td>0.743(0.008)</td></tr><tr><td>RF</td><td>0.827(0.005)</td><td>0.765(0.006)</td><td>0.715(0.027)</td><td>0.778(0.014)</td></tr><tr><td>ANN</td><td>0.838(0.004)</td><td>0.757(0.005)</td><td>0.735(0.024)</td><td>0.763(0.011)</td></tr><tr><td>EL</td><td>0.837(0.004)</td><td>0.771(0.004)</td><td>0.703(0.021)</td><td>0.789(0.008)</td></tr><tr><td rowspan="4">ROS</td><td rowspan="4"></td><td>LR</td><td>0.805(0.004)</td><td>0.727(0.006)</td><td>0.723(0.012)</td><td>0.728(0.008)</td></tr><tr><td>RF</td><td>0.830(0.005)</td><td>0.752(0.005)</td><td>0.752(0.017)</td><td>0.752(0.008)</td></tr><tr><td>ANN</td><td>0.838(0.004)</td><td>0.746(0.010)</td><td>0.756(0.017)</td><td>0.744(0.015)</td></tr><tr><td>EL</td><td>0.837(0.004)</td><td>0.757(0.005)</td><td>0.736(0.015)</td><td>0.762(0.009)</td></tr><tr><td rowspan="4">RUS</td><td rowspan="4"></td><td>LR</td><td>0.805(0.004)</td><td>0.729(0.006)</td><td>0.718(0.010)</td><td>0.732(0.008)</td></tr><tr><td>RF</td><td>0.831(0.005)</td><td>0.740(0.005)</td><td>0.780(0.015)</td><td>0.729(0.008)</td></tr><tr><td>ANN</td><td>0.838(0.005)</td><td>0.730(0.005)</td><td>0.792(0.019)</td><td>0.714(0.008)</td></tr><tr><td>EL</td><td>0.838(0.004)</td><td>0.747(0.004)</td><td>0.765(0.014)</td><td>0.742(0.008)</td></tr></table>

Data in bold are the highest number in that specific category.

Table 6  
Classification results with and without employing the proposed data analytics technique.

<table><tr><td>Variable set</td><td>Balancing Method</td><td># of Variable</td><td>Model</td><td>AUC</td><td>Accuracy</td><td>Sensitivity</td><td>Specificity</td></tr><tr><td rowspan="4">None</td><td rowspan="4">None</td><td rowspan="4">16</td><td>LR</td><td>0.826(0.005)</td><td>0.822(0.004)</td><td>0.378(0.008)</td><td>0.940(0.003)</td></tr><tr><td>RF</td><td>0.847(0.005)</td><td>0.837(0.004)</td><td>0.426(0.009)</td><td>0.945(0.003)</td></tr><tr><td>ANN</td><td>0.825(0.010)</td><td>0.826(0.005)</td><td>0.416(0.059)</td><td>0.935(0.016)</td></tr><tr><td>EL</td><td>0.842(0.005)</td><td>0.835(0.004)</td><td>0.384(0.018)</td><td>0.954(0.005)</td></tr><tr><td rowspan="4">None</td><td rowspan="4">Proposed (RUS)</td><td rowspan="4">16</td><td>LR</td><td>0.806(0.005)</td><td>0.730(0.006)</td><td>0.728(0.010)</td><td>0.730(0.007)</td></tr><tr><td>RF</td><td>0.846(0.004)</td><td>0.757(0.004)</td><td>0.759(0.015)</td><td>0.756(0.006)</td></tr><tr><td>ANN</td><td>0.824(0.008)</td><td>0.739(0.017)</td><td>0.747(0.043)</td><td>0.737(0.031)</td></tr><tr><td>EL</td><td>0.842(0.005)</td><td>0.764(0.008)</td><td>0.721(0.021)</td><td>0.776(0.013)</td></tr><tr><td rowspan="4">Proposed (GA∩SA)</td><td rowspan="4">None</td><td rowspan="4">8</td><td>LR</td><td>0.804(0.004)</td><td>0.821(0.004)</td><td>0.365(0.005)</td><td>0.942(0.004)</td></tr><tr><td>RF</td><td>0.757(0.007)</td><td>0.835(0.004)</td><td>0.412(0.009)</td><td>0.947(0.004)</td></tr><tr><td>ANN</td><td>0.839(0.004)</td><td>0.834(0.002)</td><td>0.408(0.011)</td><td>0.947(0.005)</td></tr><tr><td>EL</td><td>0.834(0.004)</td><td>0.835(0.004)</td><td>0.385(0.006)</td><td>0.954(0.003)</td></tr><tr><td rowspan="4">Proposed (GA∩SA)</td><td rowspan="4">Proposed (RUS)</td><td rowspan="4">8</td><td>LR</td><td>0.805(0.004)</td><td>0.729(0.006)</td><td>0.718(0.010)</td><td>0.732(0.008)</td></tr><tr><td>RF</td><td>0.831(0.005)</td><td>0.740(0.005)</td><td>0.780(0.015)</td><td>0.729(0.008)</td></tr><tr><td>ANN</td><td>0.838(0.005)</td><td>0.730(0.005)</td><td>0.792(0.019)</td><td>0.714(0.008)</td></tr><tr><td>EL</td><td>0.838(0.004)</td><td>0.747(0.004)</td><td>0.765(0.014)</td><td>0.742(0.008)</td></tr></table>

Diferent from the published relevant literature, we have not found any studies focused on the time between two consecutive appointments created in the data processing step of the current study. Such a variable simply measures the elapsed time between the last appointment and the appointment scheduled before the last appointment, thereby providing insights into patients' appointment pattern. For example, if the length of time between appointments is relatively low, or in other words, if the appointments are scheduled frequently, it might indicate a chronic health condition that requires the patient to schedule appointments regularly and thus, the patient can be expected to show up for his/her appointments. On the other hand, a long period between two consecutive appointments might imply a regular check-up appointment that the patient might not choose to keep depending on the severity of the medical condition.

Finally, studies reported appointment day as an important predictor [29,68]. It was specifically mentioned that Monday and Friday are the two specific days on which the highest no-show rates occur [29,68,84,85].

The ANN model, which was selected to be the best model as it came up with the highest sensitivity score with a reasonable specificity, accuracy and AUC levels, assigns (estimates) probabilistic scores for each instance (patients), ranging between 0 and 1, as presented in Table 7. Note that these results are obtained from the 7th fold (among the 10 folds), as the best sensitivity score was obtained from this specific fold. The estimate of a probability score close to 1 indicates a high chance of being a no-show for the patient, while a probability score of 0 indicates otherwise. Any numbers in-between the two are classified as one way or the other, according to the specified threshold value. For example, if a patient is assigned a probability score of 0.9, then it can be considered that there is a 90% chance the patient will be a no-show. On the other hand, a probability score of 0.1 for a patient indicates there is a 10% chance of being a no-show (very low risk). With that in mind, Table 7 illustrates the changing performance of the proposed ANN model when the diferent probabilistic thresholds are considered. For example, dropping the instances with the assigned prediction probability scores on the interval [0.4, 0.6], improves the performance of the model in each metric.

Table 7  
Sensitivity analysis for diferent probability thresholds.

<table><tr><td rowspan="2">Probability score</td><td rowspan="2">Dropped cases</td><td rowspan="2"># Show-up</td><td rowspan="2"># No-show</td><td>TP</td><td>FN</td><td rowspan="2">AUC</td><td rowspan="2">Accuracy</td><td rowspan="2">Sensitivity</td><td rowspan="2">Specificity</td></tr><tr><td>FP</td><td>TN</td></tr><tr><td rowspan="2">0.5</td><td rowspan="2">0</td><td rowspan="2">5757</td><td rowspan="2">1470</td><td>1208</td><td>1660</td><td>0.846</td><td>0.734</td><td>0.822</td><td>0.712</td></tr><tr><td>262</td><td>4097</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2"> $\notin [0.4,0.6]$ </td><td rowspan="2">1945</td><td rowspan="2">4276</td><td rowspan="2">1006</td><td>828</td><td>599</td><td>0.892</td><td>0.853</td><td>0.823</td><td>0.860</td></tr><tr><td>178</td><td>3677</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2"> $\notin [0.3,0.7]$ </td><td rowspan="2">2602</td><td rowspan="2">3780</td><td rowspan="2">845</td><td>712</td><td>441</td><td>0.904</td><td>0.876</td><td>0.843</td><td>0.883</td></tr><tr><td>133</td><td>3339</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2"> $\notin [0.2,0.8]$ </td><td rowspan="2">3568</td><td rowspan="2">3003</td><td rowspan="2">656</td><td>584</td><td>302</td><td>0.919</td><td>0.898</td><td>0.890</td><td>0.899</td></tr><tr><td>72</td><td>2701</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2"> $\notin [0.1,0.9]$ </td><td rowspan="2">5722</td><td rowspan="2">1248</td><td rowspan="2">257</td><td>234</td><td>65</td><td>0.950</td><td>0.942</td><td>0.890</td><td>0.948</td></tr><tr><td>23</td><td>1183</td><td></td><td></td><td></td><td></td></tr></table>

Note that the interval between 0.4 and 0.6 is the range, wherein the model does not have high confidence in predicting the outcome (the closer the probability to 0.5, the less confident the model is in its predictions). In other words, the model performance increases when the instances that the model is not confident are dropped. As expected, the same pattern can be seen as the interval is widened and the cases in between the updated probability borders are dropped. As such, the performance of the model reaches an accuracy score of 0.942, an AUC score of 0.950, a sensitivity score of 0.890, and a specificity score of 0.948 in the classification of the patients with the estimated probability scores <0.10 and >0.90. This attests to the reliability of the probabilities estimated by the proposed model. Therefore, to increase the accuracy of the model aggressively, an expert can resolve the cases when the model probability is close to 0.5. This is another common practice in the modern machine learning world, wherein artificial intelligence and humans collaboration become inevitable [86].

In addition, we stratified patients into five categories (i.e., Very low risk(1), Low risk(2), Moderate risk(3), High risk(4) and Very high risk(5)) by employing a k-means clustering algorithm on the estimated probabilities (Fig. 3). As discussed earlier, the cases associated with these groups were incrementally dropped, starting with the middle group and moving outward in both directions on the probability spectrum, and the remaining cases were run through the ANN (ideal) model. Such risk level stratification can be used by medical decision-makers to augment their decision-making process when assessing specific patients' circumstances for no-shows. Such a decision support mechanism can be used to lighten the burden of a large portion of the cases associated with no-shows, depending on a specific threshold probability between available resources, risks, and costs. Healthcare agencies can, therefore, adjust their risk scoring metric to achieve an ideal balance between type I and type II errors based on the cost-benefit analysis.

## 5. Decision support tool

As a part of the present study, a decision support tool incorporating the best performing ANN model is created to identify patients who are likely to miss or show up for an appointment. The decision support tool can be used via a personal computer and a wide range of smartphones; the link to the decision support tool is https://rsearch.shinyapps.io/no\_ show\_tool/.

The tool requires an appointment setter to enter the necessary information pertaining to the appointment and the patient. Afterward, the tool provides a patient-specific risk score of being a no-show for the patient for whom an appointment will be scheduled while displaying a risk category that the patient falls into. The stratification of the patients into the risk categories, determined by the k-means algorithm, can lead to better/informed booking decisions that can potentially reduce the cost imposed by no-shows.

## 6. Conclusions, limitations and future research directions

In this study, a hybrid data mining based methodology was formulated to provide healthcare agencies and medical decision-makers with a patient-specific risk level of no-shows. The overarching goal was to provide better care by utilizing available resources more eficiently and to decrease the costs that originate from patient no-shows.

It should be clearly indicated that the contribution of the current study is not the application of well-known classification models. But it is rather; a) the comprehensive variable selection methodology that we employed, which minimizes the risk of sufering from collinearity, overfitting and being trapped in local minima, b) the data balancing algorithms that strengthen the sensitivity of the model in detecting the minority samples, c) determining the patients who have very low-, low-, moderate-, high- and very high-risk scores of being a no-show, and finally, 4) the web-based decision support tool that can be adopted by medical decision-makers in clinics as a decision support tool, which can be considered as the practical contribution of the proposed method. With that said, in the case of such tool being adopted by the medical centers, the importance of the proposed method increases, as the parsimonious model reduces the time spent in the data entry and the computation (training and test) stage, which would enable medical clinics to react in the timeliest manner.

![](/api/attachments/NGSNDZ6C/fulltext/images/ec8ab000d2749f695728537f83239706561f27200fc6f92af61448065e75b72d.jpg)  
Fig. 3. The risk level classification through the k-means clustering algorithm.

The patient-specific risk scores obtained were justified by applying a threshold sensitivity analysis and it has been shown that model performance consistently increases when the patients, whom the model does not have high confidence in, are dropped. Medical experts can confidently rely on the probabilistic score provided, while the data analytical models and medical experts' intuition/incentive should be combined to decide on the final decision of the cases where the model is not confident enough. Healthcare agencies can take advantage of the risk assessment to augment their decision-making procedures. These insights enable health care professionals to improve clinic utilization, and improve patient outcomes. Healthcare delivery systems can efectively adopt measures targeting patients who are no-show candidates by systematizing intervention tactics.

One of the major limitations in the present study is the use of the publicly available dataset, where we did not have the flexibility of collecting our own dataset. Collecting our own dataset could have provided a more feature-rich information in that we would have chance to know; a) the reason that the patients are making the appointment for, b) whether these reasons are urgent and/or associated with the patients' existing chronic conditions such as diabetes, etc. or not, c) severity of the issues that the patients are experiencing while making the appointment, etc., and finally d) what time of the day that the clinic set the appointments. All of these could enable the researcher to build better predictive models, as there is more valuable information in the dataset. Lastly, as a future direction, the web-based tool can be designed in a way that it not only predicts the risk group (of no show) of the patient but also provides the best appointment date on which the patients no show risk score is minimized.

## References

[1] C. DuMontier, K. Rindfleisch, J. Pruszynski, J.J. Frey, A multi-method intervention to reduce no-shows in an urban residency clinic, Fam. Med. 45 (2013) 634–641 http://www.ncbi.nlm.nih.gov/pubmed/24136694 . Accessed date: 6 August 2018

[2] C.G. Moore, P. Wilson-Witherspoon, J.C. Probst. Time and money: effects of noshows at a family practice residency clinic. Fam, Med. 33 (2001) 522–527 http:/ www.ncbi.nlm.nih.gov/pubmed/11456244 , Accessed date: 11 November 2018.

[3] K. Fortin, E. Pries, S. Kwon, Missed medical appointments and disease control in children with type 1 diabetes, J. Pediatr. Heal. Care. 30 (2016) 381–389, https:// doi.org/10.1016/j.pedhc.2015.09.012.

[4] M.W. Reid, F.P. May, B. Martinez, S. Cohen, H. Wang, D.L. Williams Jr., B.M.R. Spiegel, Preventing endoscopy clinic no-shows: prospective validation of a predictive overbooking model, Am. J. Gastroenterol. 111 (2016) 1267–1273, https://doi.org/10.1038/ajg.2016.269.

[5] B. Zeng, A. Turkcan, J. Lin, M. Lawley, Clinic scheduling models with overbooking for patients with heterogeneous no-show probabilities, Ann, Oper, Res, 178 (2010 121–144. https://doi,org/10.1007/s10479-009-0569-5.

[6] T. Vikander, K. Parnicky, R. Demers, K. Frisof, P. Demers, N. Chase, New-patient noshows in an urban family practice center: analysis and intervention, J. Fam. Pract. 22 (1986) 263–268 http://www.ncbi.nlm.nih.gov/pubmed/3950555 , Accessed date: 6 August 2018.

[7] S.R. Garuda, R.G. Javalgi, V.S. Talluri, Tackling no-show behavior, Health Mark. Q. 15 (1998) 25–44, https://doi.org/10.1300/J026v15n04\_02.

[8] M. Bech, The economics of non-attendance and the expected efect of charging a fine on non-attendees, Health Policy (New. York) 74 (2005) 181–191, https://doi. org/10.1016/j.healthpol.2005.01.001.

[9] D.L. Olson, D. Delen, Advanced data mining techniques, Springer Publishing Company, Incorporated, 2008, https://doi.org/10.1007/978-3-540-76917-0.

[10] J.J. Alpert, Broken appointments, Pediatrics 34 (1964), http://pediatrics aappublications.org/content/34/1/127.short , Accessed date: 6 August 2018.

[11] R.A. Deyo, T.S. Inui, Dropouts and broken appointments. A literature review and agenda for future research, Med. Care 18 (1980) 1146–1157 http://www ncbi,nlm nih.gov/pubmed/7432014 , Accessed date: 6 August 2018.

[12] D.S. Shepard, T.A.E. Moseley, Mailed versus telephoned appointment reminders to reduce broken appointments in a hospital outpatient department, Med. Care 14 (1976) 268–273, https://doi.org/10.1097/00005650-197603000-00008.

[13] P.R. Harper, H.M. Gamlin, Reduced outpatient waiting times with improved appointment scheduling: a simulation modelling approach, OR Spectr. 25 (2003) 207–222.

[14] R. Hassin. S. Mendel. Scheduling arrivals to queues: a single-server model with no: shows, Manag, Sci, 54 (2008) 565–572. https://doi,org/10.1287/mnsc.1070.0802

[15], T. Cavirli, K.K. Yang, S.A. Ouek. A universal appointment rule in the presence of no:

shows and walk-ins, Prod. Oper. Manag. 21 (2012) 682–697.

[16] J. Luo, V.G. Kulkarni, S. Ziya, Appointment scheduling under patient no-shows and service interruptions, Manuf. Serv. Oper. Manag. 14 (2012) 670–684.

[17] Y. Huang, P. Zuniga, Efective cancellation policy to reduce the negative impact of patient no-show, J. Oper. Res. Soc. 65 (2014) 605–615.

[18] Y. Huang, P. Zuniga, Dynamic overbooking scheduling system to improve patient access, J. Oper. Res. Soc. 63 (2012) 810–820.

[19] C. Zacharias, M. Pinedo, Appointment scheduling with no-shows and overbooking, Prod. Oper. Manag. 23 (2014) 788–801.

[20] N. Liu, Optimal choice for appointment scheduling window under patient no-show behavior, Prod. Oper. Manag. 25 (2016) 128–142.

[21] A. Ahmadi-Javid, Z. Jalali, K.J. Klassen, Outpatient appointment systems in healthcare: a review of optimization studies, Eur. J. Oper. Res. 258 (2017) 3–34, https://doi.org/10.1016/J.EJOR.2016.06.064.

[22] V. Pesata, G. Pallija, A.A. Webb, A descriptive study of missed appointments: fa milies’ perceptions of barriers to care, J. Pediatr. Heal. Care. 13 (1999) 178–182.

[23] R.D. Neal, D.A. Lawlor, V. Allgar, M. Colledge, S. Ali, A. Hassey, C. Portz, A. Wilson, Missed appointments in general practice: retrospective data analysis from four practices, Br. J. Gen. Pract. 51 (2001) 830–832 http://www.ncbi.nlm.nih.gov/ pubmed/11677708 , Accessed date: 6 August 2018.

[24] N.L. Lacy, A. Paulman, M.D. Reuter, B. Lovejoy, Why we don’t come: patient perceptions on no-shows, Ann. Fam. Med. 2 (2004) 541–545, https://doi.org/10.1370 afm.123.

[25] R.D. Neal, M. Hussain-Gambles, V.L. Allgar, D.A. Lawlor, O. Dempsey, Reasons for and consequences of missed appointments in general practice in the UK: questionnaire survey and prospective review of medical records, BMC Fam. Pract. 6 (2005) 47. https://doi.org/10.1186/1471-2296-6-47.

[26] V. Chariatte, A. Berchtold, C. Akré, P.-A. Michaud, J.-C. Suris, Missed appointments in an outpatient clinic for adolescents, an approach to predict the risk of missing, J. Adolesc. Health 43 (2008) 38–45, https://doi.org/10.1016/j.jadohealth.2007.12. 017.

[27] N. Junod Perron, M. Dominicé Dao, M.P. Kossovsky, V. Miserez, C. Chuard, A. Calmy, J.-M. Gaspoz, Reduction of missed appointments at an urban primary care clinic: a randomised controlled study, BMC Fam. Pract. 11 (2010) 79, https:/ doi.org/10.1186/1471-2296-11-79

[28] J.B. Norris, C. Kumar, S. Chand. H. Moskowitz, S.A. Shade, D.R. Willis, An empirical investigation into factors afecting patient cancellations and no-shows at outpatient clinics, Decis. Support. Syst. 57 (2014) 428–443, https://doi.org/10.1016/J.DSS. 2012.10.048

[29] P. Kheirkhah, Q. Feng, L.M. Travis, S. Tavakoli-Tabasi, A. Sharafkhaneh, Prevalence, predictors and economic consequences of no-shows, BMC Health Serv. Res. 16 (2015) 13.

[30] E.M. Boos, M.J. Bittner, M.R. Kramer, A profile of patients who fail to keep appointments in a veterans afairs primary care clinic, WMJ 115 (4) (2016) 185–190.

[31] M.L. Davies, R.M. Gofman, J.H. May, R.J. Monte, K.L. Rodriguez, Y.C. Tjader, D.L. Vargas, Large-Scale no-Show Patterns and Distributions for Clinic Operational Research, Healthcare, Multidisciplinary Digital Publishing Institute, 2016, p. 15.

[32] N. Liu, S. Ziya, V.G. Kulkarni, Dynamic scheduling of outpatient appointments under patient no-shows and cancellations, Manuf. Serv. Oper. Manag. 12 (2010) 347–364.

[33] J. Feldman, N. Liu, H. Topaloglu, S. Ziya, Appointment scheduling under patient preference and no-show behavior, Oper, Res, 62 (2014) 794–811.

[34] M. Samorani, L.R. LaGanga, Outpatient appointment scheduling given individua dav-dependent no-show predictions. Eur. J. Oper. Res. 240 (2015) 245–257. https://doi.org/10.1016/j.ejor.2014.06.034.

[35] K.J. Glowacka, R.M. Henry, J.H. May, A hybrid data mining/simulation approach for modelling outpatient no-shows in clinic scheduling, J. Oper. Res. Soc. 60 (2009) 1056–1068, https://doi.org/10.1057/jors.2008.177.

[36] J. Daggy, M. Lawley, D. Willis, D. Thayer, C. Suelzer, P.-C. DeLaurentis, A. Turkcan, S. Chakraborty, L. Sands, Using no-show modeling to improve clinic performance, Health Informatics J 16 (2010) 246–259, https://doi.org/10.1177 1460458210380521

[37] A. Alaeddini, K. Yang, C. Reddy, S. Yu, A probabilistic model for predicting the probability of no-show in hospital appointments, Health Care Manag. Sci. 14 (2011) 146–157, https://doi.org/10.1007/s10729-011-9148-9.

[38] H. Lenzi, Â.J. Ben, A.T. Stein, Development and validation of a patient no-show predictive model at a primary care setting in Southern Brazil, PLoS One 14 (2019) e0214869, , https://doi.org/10.1371/journal.pone.0214869.

[39] Y. Huang, D.A. Hanauer, Patient no-show predictive model development using multiple data sources for an efective overbooking approach, Appl. Clin. Inform. 5 (2014) 836–860. https://doi org/10.4338/ACI-2014-04-RA-0026

[40] K. Topuz, H. Uner, A. Oztekin, M.B. Yildirim, Predicting pediatric clinic no-shows: a decision analytic framework using elastic net and Bayesian belief network, Ann. Oper. Res. 263 (2018) 479–499, https://doi.org/10.1007/s10479-017-2489-0.

[41] Medical appointment no shows, Kaggle, https://www.kaggle.com/joniarroba/ noshowappointments. (2016)

[42] G. James, D. Witten, T. Hastie, R. Tibshirani, An Introduction to Statistical Learning, Springer New York, New York, NY, 2013, https://doi.org/10.1007/978- 1-4614-7138-7

[43] T. Hastie, Elements of Statistical Learning, (2009), https://doi.org/10.1007/ b94608.

[44] D. Whitley, A genetic algorithm tutorial, Stat. Comput. 4 (1994) 65–85, https://doi. org/10.1007/BF00175354.

[45] S. Kirkpatrick, C.D. Gelatt, M.P. Vecchi, Optimization by simulated annealing, Science 220 (1983) 671–680, https://doi.org/10.1126/science.220.4598.671.

[46] C.F. Tsai, Y.C. Hsiao, Combining multiple feature selection methods for stock

prediction: union, intersection, and multi-intersection approaches, Decis. Support. Syst. 50 (2010) 258–269, https://doi.org/10.1016/j.dss.2010.08.028.

[47] R.A. Rutenbar, Simulated annealing algorithms: an overview, IEEE Circuits Devices Mag 5 (1989) 19–26, https://doi.org/10.1109/101.17235.

[48] L. Breiman, Random forests, Mach. Learn. 45 (2001) 5–32, https://doi.org/10 1023/A:1010933404324

[49] D.E. Goldberg, Genetic Algorithms in Search, Optimization, and Machine Learning, (2011).

[50] H. Vafaie, K. De Jong, Genetic algorithms as a tool for feature selection in machine learning, Proc. - Int. Conf. Tools with Artif. Intell. ICTAI, IEEE Computer Society, 1992, pp. 200–203, , https://doi.org/10.1109/TAI.1992.246402.

[51] J.-S. Lee, D. Zhu, When costs are unequal and unknown: a subtree grafting approach for unbalanced data classification\*, Decis. Sci. 42 (4) (2011) 803–829, https://doi. org/10.1111/j.1540-5915.2011.00332.x.

[52] H. He, E.A. Garcia, Learning from imbalanced data, IEEE Trans. Knowl. Data Eng. 21 (2009) 1263–1284. https://doi,org/10.1109/TKDE,2008.239.

[53] A. Dag, A. Oztekin, A. Yucel, S. Bulur, F.M. Megahed, Predicting heart transplantation outcomes through data analytics, Decis. Support. Syst. 94 (2017) 42–52, https://doi.org/10.1016/j.dss.2016.10.005.

[54] E. Kibis, E. Buyuktahtakin, A. Dag, Data analytics approaches for breast cancer survivability: comparison of data mining methods, Proc. 2017 Ind. Syst. Eng. Conf, 2017.

[55] D. Opitz, R. Maclin, Popular ensemble methods: an empirical study, J. Artif. Intell. Res. 11 (1999) 169–198, https://doi.org/10.1613/jair.614.

[56] D. West, P. Mangiameli, R. Rampal, V. West, Ensemble strategies for a medica diagnostic decision support system: a breast cancer diagnosis application, Eur. J. Oper, Res, 162 (2005) 532–551, https://doi,org/10.1016/J.EJOR.2003.10.013.

[57] L. Orimoloye, Are Ensemble Classifiers Always Better than Single Classifiers?- SAS Users. https://blogs.sas.com/content/sgf/2017/03/10/are-ensemble-classifiersalways-better-than-single-classifiers/, (2017) , Accessed date: 28 December 2018.

[58] D.W. Patterson, Artificial Neural Networks : Theory and Applications, Prentice Hall 1996, https://dl.acm.org/citation.cfm?id=521611.

[59] L. Breiman, Manual on Setting up, Using, and Understanding Random Forests V3.1, https://www.stat.berkeley.edu/\~breiman/Using\_random\_forests\_V3.1.pdf, (2002).

[60] D.R. Hunter, M.S. Handcock, C.T. Butts, S.M. Goodreau, M. Morris, Ergm: a package to fit, simulate and diagnose exponential-family models for networks, J. Stat. Softw. 24 (2008) nihpa54860http://www.ncbi.nlm.nih.gov/pubmed/19756229.

[61] G.W. Davis, Sensitivity analysis in neural net solutions, IEEE Trans. Syst. Man. Cybern. 19 (1989) 1078–1082, https://doi,org/10.1109/21.44023

[62] J.C. Principe, N.R. Euliano, W.C. Lefebvre, Innovating adaptive and neural systems instruction with interactive electronic books, Proc. IEEE 88 (2000) 81–94, https:/ doi.org/10.1109/5.811604.

[63] A. Saltelli, Making best use of model evaluations to compute sensitivity indices, Comput. Phys. Commun. 145 (2002) 280–297, https://doi.org/10.1016/S0010- 4655(02)00280-1.

[64] A. Saltelli, S. Tarantola, F. Campolongo, M. Ratto, Sensitivity Analysis in Practice, John Wiley & Sons, Ltd, Chichester, UK, 2002, https://doi.org/10.1002/ 0470870958.

[65] J.F. Elder, The generalization paradox of ensembles, J. Comput. Graph. Stat. 12 (2003) 853–864. https://doi.org/10.1198/1061860032733.

[66] S. Cang, H. Yu, A combination selection algorithm on forecasting, Eur. J. Oper. Res. 234 (2014)127–139. https://doi,org/10.1016/i.eior,2013.08.045.

[67] D. Powers, Evaluation: from precision, recall and F-measure to ROC, informedness, markedness and correlation. J. Mach. Learn. Technol. 2 (2011) 37–63 https:// dspace2.flinders.eduau/xmlui/handle/2328/27165

[68] O. Torres, M.B. Rothberg, J. Garb, O. Ogunneye, J. Onyema, T. Higgins, Risk factor model to predict a missed clinic appointment in an urban, academic, and underserved setting, Popul. Health Manag. 18 (2015) 131–136, https://doi.org/10.1089 pop.2014.0047.

[69] A. Kempny, G.-P. Diller, K. Dimopoulos, R. Alonso-Gonzalez, A. Uebing, W. Li, S. Babu-Naravan, L. Swan, S.J. Wort, M.A. Gatzoulis, Determinants of outpatient clinic attendance amongst adults with congenital heart disease and outcome, Int. J Cardiol. 203 (2016) 245–250. https://doi,org/10.1016/J.JJCARD.2015.10.081.

[70] H.G. Dove. K.C. Schneider, The usefulness of patients' individual characteristics in predicting no-shows in outpatient clinics, Med. Care 19 (1981) 734–740 http:// www.ncbi.nlm.nih.goy/pubmed/7266121 , Accessed date: 6 August 2018.

[71] B.T. Farid, E. Alapont, Patients who fail to attend their first psychiatric outpatient appointment: non-attendance or inappropriate referral? J. Ment. Health 2 (1993) 81–83, https://doi.org/10.3109/09638239309016957.

[72] V.J. Lee, A. Earnest, M.I. Chen, B. Krishnan, Predictors of failed attendances in a multi-specialty outpatient centre using electronic databases, BMC Health Serv. Res. 5.(2005).51.https://doi org/10.1186/1472-6963-5-51

[73] P.R. Cronin, L. DeCoste, A.B. Kimball, A multivariate analysis of dermatology missed appointment predictors, JAMA Dermatology 149 (2013) 1435, https://doi. org/10.1001/jamadermatol.2013.5771.

[74] L.A. Nuti, M. Lawley, A. Turkcan, Z. Tian, L. Zhang, K. Chang, D.R. Willis, L.P. Sands, No-shows to primary care appointments: subsequent acute care utilization among diabetic patients, BMC Health Serv. Res. 12 (2012) 304, https://doi. org/10.1186/1472-6963-12-304

[75] A.B. Bindman, K. Grumbach, D. Osmond, M. Komaromy, K. Vranizan, N. Lurie, J. Billings, A. Stewart, Preventable hospitalizations and access to health care, JAMA J. Am. Med. Assoc. 274 (1995) 305, https://doi.org/10.1001/jama.1995.

03530040033037.

[76] P.E. Hasvold, R. Wootton, Use of telephone and SMS reminders to improve atten dance at hospital appointments: a systematic review, J. Telemed. Telecare 17 (2011) 358–364, https://doi.org/10.1258/jtt.2011.110707.

[77] V. Vodopivec-Jamsek, T. de Jongh, I. Gurol-Urganci, R. Atun, J. Car, Mobile phone messaging for preventive health care, Cochrane Database Syst. Rev. 12 (2012) CD007457, https://doi.org/10.1002/14651858.CD007457.pub2.

[78] R.G. Milne, M. Horne, B. Torsney, SMS reminders in the UK national health service: an evaluation of its impact on “no-shows” at hospital out-patient clinics, Health Care Manag. Rev. 31 (2006) 130–136.

[79] J.A. Tibble, I. Forgacs, I. Bjarnason, R. Przemioslo, The efects of a preassessment clinic on nonattendance rates for day-case colonoscopy, Endoscopy 32 (2000) 963–965, https://doi.org/10.1055/s-2000-9629.

[80] L.F. Dantas, J.L. Fleck, F.L. Cyrino Oliveira, S. Hamacher, No-shows in appointment scheduling – a systematic literature review, Health Policy (New. York) 122 (2018) 412–421. https://doi.org/10.1016/i.healthpol.2018.02.002

[81] J.B. Norris, C. Kumar, S. Chand, H. Moskowitz, S.A. Shade, D.R. Willis, An empirical investigation into factors afecting patient cancellations and no-shows at outpatient clinics, Decis. Support. Syst. 57 (2014) 428–443, https://doi.org/10.1016/J.DSS. 2012.10.048

[82] M.J. McMullen, P.A. Netland, Lead time for appointment and the no-show rate in an ophthalmology clinic, Clin. Ophthalmol. (Auckland, NZ). 9 (2015) 513.

[83] B.P. Horsley, S.J. Lindauer, B. Shrof, E. Tüfekçi, A.O. Abubaker, C.E. Fowler, B.J. Maxfield, Appointment keeping behavior of Medicaid vs non-Medicaid ortho dontic patients, Am. J. Orthod. Dentofac. Orthop. 132 (2007) 49–53

[84] Y.-L. Huang, D.A. Hanauer, Time dependent patient no-show predictive modelling development, Int. J. Health Care Qual. Assur. 29 (2016) 475–488, https://doi.org 10.1108/IJHCQA-06-2015-0077.

[85] Y. Huang, D.A. Hanauer, Patient no-show predictive model development using multiple data sources for an efective overbooking approach, Appl. Clin. Inform. 5 (2014) 836–860, https://doi.org/10.4338/ACI-2014-04-RA-0026.

[86] W.H. James, D. Paul R., Collaborative intelligence: humans and AI are joining forces, Harv. Bus. Rev. (2018) 114–123 https://hbr.org/2018/07/collaborativeintelligence-humans-and-ai-are-joining-forces.

![](/api/attachments/NGSNDZ6C/fulltext/images/bd08216c5237fa0562ecb559268e7f6a4c1a84051e6ff05d0797f2b2849b4abc.jpg)  
Dr. Serhat Simsek has a Ph.D. degree in Statistics and an MS degree in Mathematics & Probability from Auburn University. He is currently an Assistant Professor of Statistics & Business Analytics in the Department of Information Management & Business Analytics at Feliciano School of Business at Montclair State University. He is interested in statistical modeling, machine learning, business analytics, and healthcare analytics.

![](/api/attachments/NGSNDZ6C/fulltext/images/5a5fb4b85a2c4df0e5b337cd0ce82708d4da36f5166240e68b0e52de3e93175c.jpg)  
Dr. Thomas Tiahrt is an Assistant Professor of Decision Sciences at the Beacom School of Business at The University of South Dakota. He earned an M.A. in Computer Science and a Ph.D. in Computational Science and Statistics from The University of South Dakota. His research interests include business analytics, text mining, and natural language processing. He is a member of the ACM, INFORMS and the Decision Sciences Institute.

![](/api/attachments/NGSNDZ6C/fulltext/images/4653f09914b9505e416ecf8f7fb060b8975f3347e7448fc0ea2a5fad06f79b5b.jpg)

Dr. Ali Dag received his Ph.D. from Auburn University in Industrial and Systems Engineering, He is currently an Associate Professor of Analytics at the Business Intelligence & Analytics department at Heider College of Business at Creighton University. His research interests include business & data analytics, operations research, operations management and text mining. He is currently the vice chair of Informs Data Mining Section. He is one of the associate editors of Journal of Modelling in Management (JMM2), and Artificial Intelligence in Business (AIIB) journals. Dag's research have been published in many journals such us Decision Support Systems. Annals of Operations Research and Information Systems Frontiers etc
