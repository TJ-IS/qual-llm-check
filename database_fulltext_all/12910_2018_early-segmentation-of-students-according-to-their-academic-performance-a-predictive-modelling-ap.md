---
otero_id: 12910
otero_key: "F8DSE335"
title: "Early segmentation of students according to their academic performance: A predictive modelling approach"
authors: "V.L. Miguéis; Ana Freitas; Paulo J.V. Garcia; André Silva"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.09.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Early segmentation of students according to their academic performance: a predictive modeling approach

Decision Support Systems

V.L. Miguéis, Ana Freitas, Paulo J.V. Garcia, André Silva

![](/api/attachments/F8DSE335/fulltext/images/16356affd3732f74204698229c676780a5c9f7676155dcdfc37c468cbf548545.jpg)

PII: S0167-9236(18)30142-8

DOI: doi:10.1016/j.dss.2018.09.001

Reference: DECSUP 12987

To appear in: Decision Support Systems

Received date: 29 July 2017

Revised date: 1 August 2018

Accepted date: 3 September 2018

Please cite this article as: V.L. Miguéis, Ana Freitas, Paulo J.V. Garcia, André Silva , Early segmentation of students according to their academic performance: a predictive modeling approach. Decsup (2018), doi:10.1016/j.dss.2018.09.001

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

Early segmentation of students according to their academic performance: a data mining approach

## By

Vera L. Miguéis (corresponding author)

Faculdade de Engenharia da Universidade do Porto, INESC TEC

Address: Rua Dr. Roberto Frias 4200-465 Porto Portugal

Email: vera.migueis@fe.up.pt

## Ana Freitas

Faculdade de Engenharia da Universidade do Porto

Address: Rua Dr. Roberto Frias 4200-465 Porto Portugal

Email: anafreitas@fe.up.pt

## Paulo J. V. Garcia

Faculdade de Engenharia da Universidade do Porto

Address: Rua Dr. Roberto Frias 4200-465 Porto Portugal

Email: pgarcia@fe.up.pt

## André Silva

Faculdade de Engenharia da Universidade do Porto

Address: Rua Dr. Roberto Frias 4200-465 Porto Portugal

Email: ei10085@fe.up.pt

# Early segmentation of students according to their academic performance: a predictive modeling approach

## Abstract

The early classification of university students according to their potential academic performance can be a useful strategy to mitigate failure, to promote the achievement of better results and to better manage resources in higher education institutions. This paper proposes a two-stage model, supported by data mining techniques, that uses the information available at the end of the first year of students’ academic career (path) to predict their overall academic performance. Unlike most literature on educational data mining, academic success is inferred from both the average grade achieved and the time taken to conclude the degree. Furthermore, this study proposes to segment students based on the dichotomy between the evidence of failure or high performance at the beginning of the degree program, and the students’ performance levels predicted by the model. A data set of 2459 students, spanning the years from 2003 to 2015, from an European Engineering School of a public research University, is used to validate the proposed methodology. The empirical results demonstrate the ability of the proposed model to predict the students’ performance level with an accuracy above 95%, in an early stage of the students’ academic path. It is found that random forests are superior to the other classification techniques that were considered (decision trees, support vector machines, naive bayes, bagged trees and boosted trees). Together with the prediction model, the suggested segmentation framework represents a useful tool to delineate the optimum strategies to apply, in order to promote higher performance levels and mitigate academic failure, overall increasing the quality of the academic experience provided by a higher education institution.

Key words: Educational data mining, Predictive modelling, Data mining, Academic performance, Engineering education

## 1 Introduction

Considering that one of the Europe 2020’s targets states that at least 40% of the population aged 30-34 should have completed a tertiary education by 2020 (European Commission, 2010), and that one of the USA’s goals for 2020 is to lead the world in college graduates (American Council on Education, 2011), higher education institutions are faced with the challenge of, alongside attracting more students, dealing efectively with their very diferent academic performances. Within this challenging scenario, institutions have to timely devise strategies to promote academic success and enhance the academic experience of students with diferent academic performance levels.

To achieve this, higher education institutions are now becoming aware of the potential of studying educational data to improve the quality of their managerial decisions (Hofait and Schyns, 2017; Delen, 2010; Kiang et al., 2009). They are making eforts and investing in creating information systems to collect education-related data, and studying it using data mining techniques. The purpose is to extract meaningful and operational information from those large educational databases (Guruler et al., 2010), which have the potential to provide a better understanding of students behavioural patterns.

Despite the promising potential of data analysis supported by data mining, most higher education institutions have not been able to analyse this data and transform it into valuable information. In fact, in most cases, only conventional methods supported by statistics have been applied to the data. Therefore, the use of these new generation techniques is clearly in the agenda of higher education institutions, in order to support the development of educational strategies (Gibson, 2017).

Among the tasks where educational data plays an important role and where the literature has already made some progress, we can find the prediction of academic performance. A few institutions are now aware that the early inference of students potential academic performance may enable them to foster higher levels of academic achievement. This may result in the design of diferentiated actions targeting diferent groups of students according to their potential and may also result in a more eficient allocation of the institutions’ resources.

In this context, this study aims at supporting an European Engineering School in promoting the academic potential of each student and experience through data mining models. For this purpose, this study main goal is to early classify students into segments, which are not only based on the students average grade but also on the time taken to conclude the degree. It can be argued on higher education system eficiency and on the academic experience quality grounds that the average grade is incomplete and therefore the identification of those more likely to take a long time to graduate allows target intervention programs to act where they are needed most. Particularly, this study addresses the following questions:

(1) Is it possible to identify, in an early stage of the students’ academic path, their future academic success groups?

(2) In the specific context of study, which data mining technique, among random forests, decision trees, support vector machines, naive bayes, bagged trees and boosted trees, performs best?

(3) What are the dimensions that mainly determine the propensity of students to achieve a certain academic performance level?

This study adds value to the literature in several dimensions. First, and in what regards the methodology, we propose a two-stage approach, combining discretization and classification meth-

# ACCEPTED MANUSCRIPT

ods. Initially, using a discretization algorithm, the students’ performance is categorized into five classes, corresponding to diferent levels of academic performance. Then, we propose a model to early predict the performance of engineering students at the end of the academic degree or at an advanced stage of their academic career. The students’ performance is based on a new performance metric which combines the mean of the grades obtained and the number of enrollments in the courses to achieve that mean.

Several classification techniques are applied, namely random forests, bagged trees and boosted trees, to predict the overall level of academic performance of the students. The application of ensemble methods, such as these previously mentioned, to the educational data mining field is still incipient, although their predictive performance is generally high.

Third, we assess the importance of student-related variables to the prediction model in order to provide decision makers some information regarding the factors that impact students performance, both in terms of GPA and time to degree completion.

Finally, this study contributes to the literature, by proposing an approach to segment students based on both the predicted performance at the end of the academic degree, and the performance observed at the end of the first year. This segmentation approach may be a basis for the diferentiation of the actions developed by the institutions to: not only promote higher levels of academic success, but to enhance the quality of the students educational experience. For example, when designing a program to promote higher success, the institution may be interested in targeting a student belonging to the lowest performance group according to the prediction model, and that, simultaneously, already demonstrates signs of poor performance at the beginning of the degree program. At the other extreme, when designing a reward program, an institution may be interested in targeting students who are top performers according to the prediction model, and that are already top performers at the end of the first academic year.

The present study difers from other works on academic performance, as it is based on a high number of students, i.e., 2459 students, corresponding to five cohorts of students who enrolled in an European engineering and technology school during five academic years (2003 to 2007, followed up to 2015); most of the studies in the literature consider small sets of students to validate the proposed models.

The paper is structured as follows. The following section presents the related studies, in order to emphasize the contributions of the current study. Section 3 introduces the methods and data, the variables included in the proposed model, and the performance evaluation criteria. Section 4 addresses the results and the discussion. Section 5 highlights the conclusions and section 6 the limitations and ideas for future research.

# ACCEPTED MANUSCRIPT

## 2 Related Studies

As huge amounts of data are being made available by the institutional information systems, data mining techniques emerge as natural tools to tackle the above questions. The use of data mining in this context is not new (see Table 1). The progress in the educational data mining research field can be followed in several reviews (e.g. Pena-Ayala, 2014b,a; Romero and Ventura, 2010, 2007). These reviews provide many examples of the application of the diferent data mining techniques to support a variety of aspects related to education. These aspects include, for example, students dropout prediction (e.g. Delen, 2010; M´arquez-Vera et al., 2016; Thammasiri et al., 2014), the development of recommendation systems (e.g. Aher and Lobo, 2013; Elfaki et al., 2015), and students’ performance prediction (e.g. Huang and Fang, 2013; Marbouti et al., 2016). Regarding dropout prediction, for example M´arquez-Vera et al. (2016) conduct several experiments using a dataset of 419 students to predict dropout at diferent steps in a course, and select the best predictors of dropout. Bydzovska (2016) develops a recommendation model based on the students’ skills, knowledge, interests and free timetable time-slots to support students in their choice of selective and optional courses; this model is validated using data from 1444 students.

The prediction of students’ performance is one of the most popular and useful applications of educational data mining. This consists in estimating the unknown value of students’ performance, score or mark (Romero and Ventura, 2013). This is a challenging problem to solve, due to the large number of circumstances that can impact students’ performance, such as socio-economic status, previous scholar experience, interactions between colleagues, demographic characteristics, psychological profile and cultural background (Araque et al., 2009; Richardson et al., 2012). Tinto (1982) introduces a predominant theoretical framework regarding academic success. This popular framework considers academic success as a socio-psychological connection between the characteristics of the student enrolling in the university and the experience at that institution. According to this model, the commitment to the institution and the commitment to the goal of study completion are highly connected to the degree of integration.

Considering the aforementioned factors, the educational data mining studies that focus on students’ performance have been using a high number of attributes to characterize students and their environments. Bordea et al. (2015) reviews the attributes in predicting students’ performance in a course. Internal assessment attributes, such as assignment marks, quizzes, lab work, class tests and attendance, are frequently used among the researchers to predict students’ performance (Papamitsiou et al., 2014; Parack et al., 2012). Bordea et al. (2015) also stress students’ demographic attributes and external assessment attributes as relevant features. Demographic attributes include gender, age, family background, and disability (Natek and Zwilling, 2014; Christian and Ayub, 2014; Jeeva et al., 2014). External assessments correspond to marks obtained in the final exam for a particular subject. Furthermore, attributes related to high school background (Harlow et al., 2014; Saad, 2008), social interaction networks (Putnik et al., 2016; Romero et al., 2013b) and extracurricular activities (Natek and Zwilling, 2014; Jeeva et al., 2014; Mayilvaganan and Kalpanadevi,

2014) are frequently considered. There are also several studies that utilized psychometric factors to predict students’ performance (Gray et al., 2014; Mishra et al., 2014). A psychometric factor is identified as a student interest, study behaviour, engagement time, and family support.

Regarding the concept of students’ performance, a branch of the literature is dedicated to exploring the success in a specific course (Huang and Fang, 2013; Marbouti et al., 2016; Costa et al., 2017). In this case, several studies define academic success according to the collected average point grade (e.g. Huang and Fang, 2013), while other studies only consider whether a student failed or passed in that specific course (e.g. Marbouti et al., 2016; Costa et al., 2017; Macfadyen and Dawson, 2010). There is another, smaller branch of the literature, that explores academic performance at the degree level. In this case, some studies aim to predict whether a student will get a degree (Aluko et al., 2016), while others aim to predict a student’s final grade (e.g. Guruler et al., 2010; Laugerman et al., 2015). Several other studies focus on determining the students’ academic performance at the end of the first academic year (Hofait and Schyns, 2017; Gray et al., 2014; Vandamme et al., 2007).

In order to analyse the gathered educational data, several data mining techniques can be applied. Classification and regression are those mostly applied when handling a problem of performance prediction. Classification is used when the predicted variable is a categorical value, while regression is used when the predicted variable is a continuous variable. Among the classification and regression techniques used for classification and regression purposes, decision trees, artificial neural networks, naive bayes, k-nearest neighbour and support vector machines are the most frequently used (Bordea et al., 2015). Decision trees are used, for example, by Mishra et al. (2014) to predict the third semester performance of a group of 250 master program students, and by Natek and Zwilling (2014) to explore the use of small student data sets (i.e., two samples of 32 students and one of 42 students) to predict students’ performance in informatics courses. Regarding Neura Networks, Arsad et al. (2013) propose a model to predict the achievement of 505 students in the eighth semester, using data collected in the first semester. Naive Bayes is used by Marbouti et al. (2016) to identify at-risk students in a particular course, using a sample of approximately 1600 students. Support Vector Machines is also applied by Gray et al. (2014) to identify college students at risk of failing in the first year of their studies; this study uses a dataset of 1074 students. Strecht et al. (2015) also apply Support Vector Machines to predict students’ success in a set of 391 courses.

Table 1 summarizes the educational mining studies that address students’ academic performance, and are mentioned above. This table mainly focuses on the type of performance evaluated as well as the techniques employed. An extended version of Table 1 is available in the Appendix A.1. This table also highlights the number of observations (in most cases, the number of students) used in the study and provides further details on the dependent variable used in the study.

Table 1: Studies addressing students’ academic performance.

<table><tr><td>Study</td><td>Main Objective</td><td>Techniques*</td><td>Performance focus</td></tr><tr><td>Huang and Fang (2013)</td><td>To predict students scores on three dynamics mid-term exams</td><td>LinR, NN, SVM</td><td>Performance in exams</td></tr><tr><td>Marbouti et al. (2016)</td><td>To identify at-risk students in a course that used standards-based grading</td><td>LogR, NN, SVM, DT, NB, KNN</td><td>Success in course</td></tr><tr><td>Costa et al. (2017)</td><td>To predict students likely to fail two courses (one performed on campus and another in a distance education format) at an early enough stage</td><td>NN, SVM, DT, NB</td><td>Success in course</td></tr><tr><td>Gray et al. (2014)</td><td>To identify college students at risk of failing in the first year of study</td><td>LogR, NN, SVM, DT, NB, KNN</td><td>First year performance</td></tr><tr><td>Macfadyen and Dawson (2010)</td><td>To identify which student online activities accurately predict academic achievement</td><td>LogR</td><td>Success in course</td></tr><tr><td>Guruler et al. (2010)</td><td>To categorize students as either successful or unsuccessful and determine profiles of students whose GPA is equal to 2.0 (which is the minimum GPA required for graduation) or greater and of those students whose GPA is equal to 3.0 or greater (honor degree)</td><td>DT</td><td>Degree level performance</td></tr><tr><td>Laugerman et al. (2015)</td><td>To determine what academic integration characteristics contribute to their success in engineering using post-hoc graduation data</td><td>BR</td><td>Degree level performance</td></tr><tr><td>Hoffait and Schyns (2017)</td><td>To identify freshmens&#x27; profiles likely to face major difficulties to complete their first academic year</td><td>LogR, NN, RF</td><td>First year performance</td></tr><tr><td>Romero and Ventura (2013)</td><td>To predict the marks that university students will obtain in the final exam of a course</td><td>DT, NN, RI</td><td>Success in course</td></tr><tr><td>Palmer (2013)</td><td>To predict academic performance of engineering students enrolled in a second-year class</td><td>LogR</td><td>Degree level performance</td></tr><tr><td>Romero et al. (2013a)</td><td>To predict students&#x27; final marks based on their participation in forums</td><td>LogR, NN, RF, NB, bayesNet, SMO</td><td>Success in course</td></tr><tr><td>Mishra et al. (2014)</td><td>To predict the third semester performance of MCA students</td><td>DT, RT</td><td>3rd semestre performance</td></tr><tr><td>Natek and Zwilling (2014)</td><td>To predict the success rate of students enrolled in their courses</td><td>DT</td><td>Success in courses</td></tr><tr><td>Arsad et al. (2013)</td><td>To predict the academic performance of Electrical Degree students</td><td>NN</td><td>8th semestre performance</td></tr><tr><td colspan="3"></td><td>Continued on next page</td></tr></table>

Table 1 – continued from previous page

<table><tr><td>Study</td><td>Main Objective</td><td>Techniques*</td><td>Performance focus</td></tr><tr><td>Strecht et al. (2015)</td><td>To predict approval/failure in a course and to predict its grade</td><td>LinR, NN, SVM, DT, NB, KNN, adaBoost</td><td>Success in course</td></tr><tr><td>Vandamme et al. (2007)</td><td>To predict the first year performance of students</td><td>DA, NN, RF, DT</td><td>First year performance</td></tr><tr><td>Aluko et al. (2016)</td><td>To predict academic success of architecture students based on information provided in prior academic performance</td><td>DA, KNN</td><td>Degree level performance</td></tr><tr><td>Current study</td><td>To predict performance levels in the end of the degree (or at an advanced stage of the academic career), in the end of the first academic year</td><td>RF, DT, SVM, NB, BagT, BoosT</td><td>Degree level performance</td></tr></table>

\*LinR: Linear Regression, NN: Neural Networks, SVM: Support Vector Machines, LogR: Logistic Regression, DT: Decision Trees, NB: Naive Bayes, KNN: k-nearest neighbor, RI: Rule Induction, BR: Boosted regression, SMO: Sequential Minimal Optimization, RT: Random Trees, BagT: Bagging Tress, BoosT: Boosting Trees

The analysis of the literature reveals that there are opportunities for development in several domains. First, a considerable number of the studies address prediction performance in a specific course, while those addressing overall performance are mainly based on the GPA obtained. Thus, there is room for exploration of diferent performance measures, as the average grade does not reveal much about the academic career of students, namely their failures in courses and the time taken to obtain the degree. Second, most of the studies available in the literature do not explore the use of state of the art classification techniques such as the ensemble techniques, which have revealed a huge potential in other contexts. In addition, most of the studies in the literature consider small sets of data to validate the proposed models. Finally, in general, the literature does not discuss the process that follows the classification of the students in terms of academic performance. For example, if a student is predicted to have poor performance in the future but, until the moment of the application of the prediction model is performing well, the level of actionability of the student is conditioned. Consequently this student should be managed in a diferent way when comparing to another student that in the moment of the prediction is already having poor performance.

## 3 Methods and data

## 3.1 Proposed method

This study aims to perform an early segmentation of students according to their academic performance. For this purpose, we propose to use a two-stage approach, illustrated in Figure 1.

![](/api/attachments/F8DSE335/fulltext/images/470c67aebe5d8189edca91f3a7c99bd2ff067e273349b1971b4f6481df04878d.jpg)  
Fig. 1. Proposed model.

Firstly, students are grouped into sets, considering their overall academic performance indicator (defined in Section 3.4). We use a binning algorithm (equal-width binning) to establish five levels of academic performance, i.e., A, B, C, D and E <sup>1</sup> The identification of five academic performance levels is mainly related to managerial questions. This is the maximum number of groups considered manageable by the institution and that, at the same time, enables to discriminate the students with reasonable detail.

Considering the numeric overall academic performance indicator, the equal-width binning algorithm creates a predefined number of groups (in this case five), by dividing the range of AP score into intervals of equal size. Note that there are alternative methods to discretize the numeric academic performance indicator (Dougherty et al., 1995).

It is important to note that our goal is not to determine the exact performance value of a student, but rather to be able to segment them, as determined by grouping the performances of the students’ peers. The performance level, obtained through the binning procedure, corresponds to the dependent variable of the prediction model developed in the second stage. This means that this is the variable we intend to predict in the end of the first year of the students’ academic career.

Secondly, we construct a data mining prediction model that uses the data available at the end of the first year as independent variables, and uses, as a dependent variable, the categorical variable reflecting the level of academic performance at the end of the degree assigned to each student, as described above. Thus, this model constitutes a multi-class classification problem.

Following the literature, we propose to include, in the prediction model, independent variables related to the high school background, psychometric factors, social factors and demographics. We also propose to incorporate the results of internal and external assessments of the courses that are part of the first semester of the academic program.

Besides the proposed two-stage approach, this paper aims to segment students according to their first year observed performance, and their expected performance. Thus, we propose to use a matrix that confronts the students’ predicted performance levels with the diferent level of academic success already observed in the first year of their studies. The indicator used to group students according to their academic achievement in the first year was the same used to group students at the end of the degree (defined in Section 3.4). We believe that each student segment leads to diferent potential actions that can be used to promote higher academic success, or to reward students with proven results.

## 3.2 Data

This study uses secondary data from an engineering and technology school, belonging to an European public research University <sup>2</sup> . The school has approximately 7000 students, 500 academic staf and 300 researchers, and ofers undergraduate and graduate (masters, doctorate) programs in several fields, such as Civil Engineering and Mechanical Engineering.

The data refers to the student information for those enrolled between 2003 and 2007, i.e., 2459 students. It encompasses all academic information obtained until either the conclusion of their degree, or until the academic year 2014/2015. If a student concludes the studies before the academic year 2014/2015, we only collect data until the conclusion, while if a student concludes the studies in the academic year 2014/2015 or after, the last data available refers to 2014/2015. In this study we are not considering the students who have dropped out.

Despite the relevance of all attribute categories highlighted in Section 2, the data provided by the institution used as case study only include socio-demographic information about the student and student socio-economic status, information regarding the high school background, information about the enrolment process and information regarding external assessments. A detailed description of the attributes used in this empirical study is presented in Table A2 in the Appendix A.2.

Regarding socio-demographic information, students are characterized by their gender and marital status. In terms of socio-economic status, we try to infer it by considering their parents’ jobs and educational levels. High school background is qualified by the type of school attended (public or private), enrolment average grade, enrolment exams grade and high school final grade. Regarding the enrolment process, students are characterized according to the year of entry into university, the program they enrol in, the enrolment stage and the enrolment option. In the enrolment process, students are required to rank five degree programs according to their preference, in order to allow students with better performance in high school to have priority in selecting a degree program. Furthermore, this process is composed by multiple stages, and the students who are not able to enter in the first stage are conditioned to the number of vacancies that are left in the subsequent stage.

Regarding external assessments, it was only possible to access information in an aggregated level. Thus, students are characterized by their grade at the end of the first and second semesters of the first academic year, as well as by the number of European Credit Transfer System (ECTS) credits referring to the courses concluded in each of these two semesters. Moreover, we could also collect the grade of the student at the end of the academic path, or by end of the period of analysis, i.e., 2015, and the total number of ECTS credits the student enrolled in during this period. These two latter metrics are used to infer the dependent variable of the model.

Figure 2 illustrates the independent and dependent periods considered in this study, and the period of time in which each variable is collected.

![](/api/attachments/F8DSE335/fulltext/images/30a230fea472e09fc0da1594b05b0f0d7ca6066a218b084b34f5fd682c7f3619.jpg)  
Fig. 2. Prediction model representation.

## 3.3 Classification techniques

Six data mining classification techniques are used to predict the performance level each student will achieve: random forests (Breiman, 2001), decision trees (Quinlan, 1986), support vector machines (Hearst et al., 1998), naive Bayes (Lewis, 1998), bagged trees (Breiman, 1996) and adaptive boosting trees (Freund and Schapire, 1996). We use random forests because, despite its general ability to provide very good results (typical of ensemble methods), this technique is underutilized

# ACCEPTED MANUSCRIPT

in the educational mining context (see Table 1). Decision trees, support vector machines and Naive Bayes are also used, due to their popularity in the literature, and due to the fact that the nowadays the trade-of between their performance and training efort is reasonable (Baeza-Yates and Liaghat, 2017). In fact, these techniques do not have any hyperparameter, or have only a few. Bagged trees and adaptive boosting trees are used due to their ensemble nature, usually resulting in higher performances than individual techniques.

Ensemble methods (Dietterich, 2000), such as random forests, bagged trees and adaptive boosting trees are techniques that combine several models into one final predictive model, generally in order to improve the predictive performance. The motivation for the adoption of ensemble techniques relies in the fact that a set of models with similar training performances may have diferent generalization abilities. Furthermore, the combination of outputs of several models reduces the risk of selecting a poorly performing model.

In the next sections we briefly describe each of the techniques considered in this study. Please note that the models were run in RapidMiner software and that we have usually used the parameter values defined by default by this software (Rapidminer, 2018).

## 3.3.1 Naive Bayes

Naive Bayes (Lewis, 1998) is part of a family of simple probabilistic classifiers based on applying Bayes’ theorem with strong (naive) independence assumptions between the explanatory variables. Bayes’ theorem describes the probability of an event, based on conditions that might be relevant to the event. Therefore, given an object to be classified, characterized by several explanatory variables, Naive Bayes assigns to this object probabilities for each of the possible classes.

## 3.3.2 Support Vector Machines

A Support Vector Machine (SVM) (Hearst et al., 1998) is a technique that, given a set of objects belonging to one of two categories, constructs a hyperplane in a high dimensional space that separates those categories. A good separation is achieved by the hyperplane that has the largest distance to the nearest training-data object of any class (so-called functional margin), since in general the larger the margin the lower the generalization error of the classifier. SVM were originally introduced to handle binary classification problems. Therefore, several methods were proposed to extend binary SVM to solve multi-classification problems. One popular approach for doing so is to reduce the single multi-classification problem into multiple binary problems.

Support vector machines usually imply the definition of meta-parameters such as the kernel and the complexity constant. In this particular case we used a linear kernel function with a complexity constant equal to one.

# ACCEPTED MANUSCRIPT

## 3.3.3 Decision trees

Decision trees (Quinlan, 1986) are classification techniques based on the concept of divide and conquer. This means that the initial set of data is divided progressively in smaller subsets. These subdivisions are based on on the values of an explanatory variable chosen according to a attributeselection criterion, i.e. criterion which identifies the attribute that “best” separates a given data set of objects into individual classes. For each subset a child node is created and the subset data is included in it. The process is then subsequently repeated on the data of the child nodes, until a termination criterion is satisfied. A decision tree has a tree structure, where each node is either a leaf, which indicates the value of the class, or a decision node, which species some test to be carried out on a single explanatory variable. Each outgoing branch represents an outcome of the test.

## 3.3.4 Random Forests

Random forests (Breiman, 2001) are part of the ensemble techniques group, since they combine multiple decision trees in order to outperform the performance of each individual decision tree. Usually this technique enables to overcome problems related to overfitting and noise in data, that are dificult to overcome by a single tree. Each decision tree used by the random forests algorithm is generated based on diferent training sets which are drawn independently with replacement from the original training set. Moreover, each decision tree is generated by considering a random sample of attributes. Each decision tree gives a classification for each object, called “vote” for that class. The random forest assigns to each object the class having a higher number of votes (over all trees in the forest).

In this case we have adopted a number of trees equal to 100 and the the number of random features to pick at each node split was defined as five.

## 3.3.5 Bagged trees

Bagged trees (Breiman, 1996) are also part of ensemble techniques group. Several decision trees are constructed based on diferent datasets resulting from a resampling procedure with replacement from the original datasets. This bootstraping procedure results in the exclusion of around 1/3 of the records in each sample. Usually, the classification of an object is also based on the majority vote.

In this case we have also adopted a number of trees equal to 100.

## 3.3.6 Adaptive boosting trees

Adaptive boosting (Freund and Schapire, 1996) is another ensemble technique, that mainly difers from bagging trees due to the fact of not using randomly subsamples of the data to construct the trees, but using weighted versions of the original datasets. A set of trees are iteratively trained. When a tree is tested, the weights of each training records are updated in order to enable the subsequent tree to focus in the records that were misclassified by the previous tree. The predictions from all the trees are usually combined through a weighted majority vote. These weights are based on the accuracy of each tree.

In this case we have also constructed 100 trees.

## 3.4 Overall academic performance

As mentioned before, several studies have already explored the use of data mining tools to predict academic performance. However, the way academic performance is defined is not always the same.

GPA has been widely used as an indicator of academic performance because it is an objective measure with good internal reliability and temporal stability (e.g. Bacon and Bean, 2006; Richardson et al., 2012). However, it is not without limitations and several authors have explored other metrics to assess academic performance.

For example, Wati et al. (2017); Yue and Fu (2017); Miao and Haney (2004) have explored time to degree completion. In fact, time to degree completion is a very important indicator for the institutions as it is linked to student and institutional success and accountability, education expenditure, and time investment (Shapiro, D. et al., 2016).

Other studies have explored academic performance as the amount of study-points (credits) that students obtained in a certain point of their academic career (Berg and Hofman, 2005; Busato et al., 1998, 2000). Knowing that not all students enroll in the full program, and that frequent students fail specific courses and retake those courses the next academic year, Vanthournout et al. (2012) proposes not to use the absolute value of credits obtained but a ratio between the number of study credits a student obtained after a certain period of time and the total amount of credits the student was enrolled in during that period. In tune with this metric and with the purpose of also accommodating the primary indicator of academic performance, i.e. the grade point average (Pike and Saupe, 2002) we propose a new metric of the overall academic performance of a student, i.e. the AP indicator.

The AP of a student at the end of the degree program (or in an advanced stage of the academic career) is defined by the ratio between the weighted mean of the grades obtained along the academic career (taking into account the number of ECTS credits the courses concluded are worth), and the total number of ECTS credits the student enrolled in to obtain approval. This performance indicator penalizes students with long academic careers and low average program grades.

$$
A P = \frac {\sum_ {i} G _ {i} * C _ {i}}{\sum_ {j} C _ {j}}\tag{1}
$$

# ACCEPTED MANUSCRIPT

Equation 1 presents the mathematical formulation of the proposed academic performance indicator. $G _ { i }$ represents the score obtained in each course i concluded with success, and $C _ { i }$ the corresponding number of ECTS credits. $C _ { j }$ refers to the number of ECTS credits of each course $j$ a student enrolled in, to get approval. When a student fails a course, he or she has to enrol in that course as many times as needed to complete the course. Consequently, $\Sigma _ { j } C _ { j }$ is a proxy for the time required to conclude a degree or to achieve a certain stage of the academic career, as a student can enrol up to a limit number of ECTS credits in each academic year.

The reason for the introduction of the AP metric relies on the fact that academic performance is not only reflected by students’ average grade but also by the efectiveness of the student during the academic path, and consequently the time taken to obtain approval in the curricular plan. This new approach captures, for example, in a situation in which two students have the same average grade, the one that did not have to repeat any course should have a higher performance score than the other that failed some courses and had to repeat them.

## 3.5 Evaluation criteria

In order to evaluate the performance of the techniques used to handle this problem, we use a validation procedure that aims to avoid overfitting. It is very important to address this issue, in order to quantify the ability of the model to generalize, i.e., its performance towards unseen data. We use a 10-fold cross validation, meaning that the data is divided into 10 blocks. The model is trained with 9 of the blocks, and the remaining one is used for testing purposes. The process is repeated 10 times, once for each of the diferent blocks. This validation procedure enables the maximization of the total number of observations used for testing.

In order to measure the performance of the proposed prediction model, we use the overall accuracy, the sensitivity (also called recall) and precision per class (Witten et al., 2011; Labatut and Cherifi, 2011).

Consider the following multi-class confusion matrix, referring to a three-class task {X, Y, Z}. We can define:

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">Observed</td></tr><tr><td>X</td><td>Y</td><td>Z</td></tr><tr><td rowspan="3">Predicted</td><td>X</td><td>a</td><td>b</td><td>c</td></tr><tr><td>Y</td><td>d</td><td>e</td><td>f</td></tr><tr><td>Z</td><td>g</td><td>h</td><td>i</td></tr></table>

Fig. 3: Confusion matrix

$$
\mathrm{Accuracy} = \frac {\mathrm{a+e+i}}{\mathrm{a+b+c+d+e+f+g+h+i}}\tag{2}
$$

$$
\mathrm{Sensitivity} _ {X} = \frac {\mathrm{a}}{\mathrm{a+d+g}}\tag{3}
$$

$$
\mathrm{Precision} _ {X} = \frac {\mathrm{a}}{\mathrm{a+b+c}}\tag{4}
$$

(5)

For example a refers to the number of observations where X was predicted and X was observed, while b refers to the number of observations that belong to $Y$ and were predicted to belong to X.

# ACCEPTED MANUSCRIPT

The overall accuracy corresponds to the number of correct predictions divided by the total number of observations. Sensitivity refers to the fraction of observations of a class that were correctly predicted. Precision is defined as the fraction of correct predictions for a certain class.

## 4 Results and discussion

## 4.1 Performance level discretization

Based on the academic performance indicator introduced in Sec. 3.4, we use a discretization algorithm (equal-width binning) to establish five levels of academic performance. We decided to adopt the maximum number of clusters that is considered manageable by the institution.

The resulting performance levels are shown in Table 2. This table highlights the mean and standard deviation of the students’ AP indicator included in each performance group.

Performance Levels for Overall Success.

<table><tr><td>Performance Level</td><td>AP Mean (sd)</td><td>Percentage of students</td></tr><tr><td>A</td><td>16.8 (1.0)</td><td>10.33%</td></tr><tr><td>B</td><td>13.5 (1.1)</td><td>38.96%</td></tr><tr><td>C</td><td>9.8 (1.1)</td><td>28.14%</td></tr><tr><td>D</td><td>6.1 (1.1)</td><td>14.80%</td></tr><tr><td>E</td><td>2.5 (0.8)</td><td>7.77%</td></tr></table>

For example, a student who is able to successfully conclude all the courses in which he enrolled for the first time, will have enrolled in a total of 300 ECTS by the end of the degree. Suppose that in half of the courses he received a final grade of 18 (out of 20), and in the other half of the courses he received a final grade of 16 (out of 20). In this scenario, he will have a weighted sum grade equal to 5100 (25 courses × 6 ECTS × 18 grade + 25 courses × 6 ECTS × 16 grade). This corresponds to an AP of 17 (=5100/300), and this student will be classified as a student A.

If another student also concludes all the courses, when enrolled for the first time, and gets a final grade of 14 (out of 20) in all the courses, he will be considered a student B (AP = 50 courses × 6 ECTS × 14 values / 300 ECTS = 14).

Consider another student who enrolled in courses corresponding to 384 ECTS during the student’s academic path, meaning that the student had to repeat 14 courses, and received a final grade of 14 (out of 20) in all the courses. He is classified as a student C (AP = 50 courses × 6 ECTS × 14 values / 384 ECTS = 10.9).

We can observe in Table 2 that this classification results in a quite balanced share of students in

## Table 3

Classification techniques performance.

<table><tr><td></td><td>Decision trees</td><td>SVM</td><td>Naive bayes</td><td>Random forests</td><td>Bagging - decision trees</td><td>Adaptive Boosting - decision trees</td></tr><tr><td>Accuracy</td><td>91.5%</td><td>93.9%</td><td>75.9%</td><td>96.1%</td><td>88.7%</td><td>95.7%</td></tr><tr><td>Recall A</td><td>91.0%</td><td>97.6%</td><td>80.9%</td><td>92.1%</td><td>75.2%</td><td>95.3%</td></tr><tr><td>Recall B</td><td>96.8%</td><td>95.2%</td><td>80.2%</td><td>98.5%</td><td>95.8%</td><td>96.5%</td></tr><tr><td>Recall C</td><td>91.5%</td><td>93.4%</td><td>71.5%</td><td>96.1%</td><td>86.6%</td><td>95.7%</td></tr><tr><td>Recall D</td><td>83.6%</td><td>89.3%</td><td>70.6%</td><td>93.4%</td><td>85.2%</td><td>95.1%</td></tr><tr><td>Recall E</td><td>81.0%</td><td>93.7%</td><td>73.5%</td><td>93.7%</td><td>85.9%</td><td>93.7%</td></tr><tr><td>Precision A</td><td>99.6%</td><td>88.9%</td><td>72.9%</td><td>99.2%</td><td>93.2%</td><td>95.3%</td></tr><tr><td>Precision B</td><td>91.1%</td><td>95.8%</td><td>81.0%</td><td>95.4%</td><td>84.2%</td><td>96.5%</td></tr><tr><td>Precision C</td><td>88.9%</td><td>93.8%</td><td>78.0%</td><td>94.1%</td><td>89.9%</td><td>95.9%</td></tr><tr><td>Precision D</td><td>90.7%</td><td>92.6%</td><td>68.1%</td><td>97.7%</td><td>93.7%</td><td>93.0%</td></tr><tr><td>Precision E</td><td>96.2%</td><td>95.2%</td><td>64.7%</td><td>100.0%</td><td>98.2%</td><td>96.8%</td></tr></table>

each cluster.

## 4.2 Classification techniques performance

The performance of the proposed model was estimated when using each of the mentioned six classification techniques. Table 3 synthesizes the results obtained. The detailed results, including the confusion matrices obtained for each classification technique are introduced in the Appendix A.3.

From the analysis of Table 3, we can conclude that the academic performance prediction in the beginning of the students’ academic career is promising. Accuracy, precision and recall values are high when using each classification technique. This means that the institution in charge may adopt these techniques to predict the performance of new students. Random forests guarantees good prediction results, outperforming the other techniques in practically all explored performance metrics explored. This result corroborates the result in Zaklouta et al. (2011), which refers that random forests achieve state-of-the-art performance in many multi-class classification applications. In opposition, and similarly to what happens in other settings (e.g. Bogaert et al., 2016; Groth and Muntermann, 2011), Naive Bayes is the worst performer, demonstrating the lowest values of all the considered metrics.

The other considered ensemble methods, i.e., bagging and adaptive boosting trees, also lead to accurate predictions. The results seem to reveal that, in this particular setting boosting decision trees generally outperform SVM, naive bayes and decision trees. The superiority of the ensemble

# ACCEPTED MANUSCRIPT

methods has been widely discussed in the literature (Piri et al., 2017).

In order to validate the results described, Table 4 presents the values obtained by performing a marginal homogeneity test for pairs of techniques. It tests the equality of two multinomial response vectors. The null hypothesis is that the probability of being classified into one category is the same for the pair of techniques considered. The cells contain the p-value of the tests.

The results reveal that that there is statistically significant diference between the models (significance level of 95%), with the exception of adaptive Boosting - decision trees and both decision tress and naive bayes; random forests and decision trees; and SVM and naive bayes. Table 4

t-test results (p-value).

<table><tr><td></td><td>SVM</td><td>Naive bayes</td><td>Random forests</td><td>Bagging - decision trees</td><td>Adaptive Boosting - decision trees</td></tr><tr><td>Decision trees</td><td>8.11E-03</td><td>3.43E-13</td><td>4.63E-01</td><td>2.41E-02</td><td>1.15E-01</td></tr><tr><td>SVM</td><td></td><td>1.78E-01</td><td>4.76E-10</td><td>&lt;2.20E-16</td><td>7.64E-05</td></tr><tr><td>Naive bayes</td><td></td><td></td><td>1.94E-3</td><td>4.60E-08</td><td>9.28E-2</td></tr><tr><td>Random forests</td><td></td><td></td><td></td><td>5.30E-12</td><td>3.70E-08</td></tr><tr><td>Bagging - decision trees</td><td></td><td></td><td></td><td></td><td>&lt;2.20E-16</td></tr></table>

## 4.3 Explanatory variables importance

We used random forests to derive the importance of each of the explanatory variables considered in the model (see Table 5), in order to get some insight into the importance of each feature in determining the academic success of a student. For this purpose, we followed the approach introduced by Menze et al. (2009). For each explanatory variable we considered all the nodes of the trees that used the variable under consideration and summed the increase in the accuracy promoted by the corresponding splits. Then we normalized the obtained sums, in order to bring all the values into the [0,1] range. Menze et al. (2009) used Gini Index to evaluate the benefit promoted by each variable, while in this study we used accuracy for this purpose.

From the analysis of Table 5, it is interesting to note that the features that characterize the students in the enrolment process, particularly the enrolment average grade and the enrolment exams average grade, are the two most discriminating variables. This seems to suggest that the high school average grade is informative (8<sup>th</sup> position in the ranking), but that the combination with the enrolment exams average grade (resulting in the enrolment average grade) is more relevant. This is in line with the idea that there are diferences between class-based and state-wide examination results (Maag Merki, 2011). High school final exams promote standardization in the grading system. Moreover, the relevance of enrolment average grade and the enrolment exams average grade attributes is aligned with a significant body of literature, that shows that both high

## ACCEPTED MANUSCRIPT

Table 5

<table><tr><td>Explanatory variables</td><td>Type of variable</td><td>Normalized weight</td></tr><tr><td>Enrolment average grade</td><td>Enrolment process</td><td>1.00</td></tr><tr><td>Enrolment exams average grade</td><td>Enrolment process</td><td>0.79</td></tr><tr><td>Average grade in the first semester</td><td>First year assessment</td><td>0.76</td></tr><tr><td>Average grade in the second semester</td><td>First year performance</td><td>0.73</td></tr><tr><td>Number of ECTS completed in the second semester</td><td>First year performance</td><td>0.62</td></tr><tr><td>Number of ECTS completed in the first semester</td><td>First year performance</td><td>0.43</td></tr><tr><td>Average # of exams attended to conclude the courses in the first academic year</td><td>First year performance</td><td>0.40</td></tr><tr><td>High school average grade</td><td>High school background</td><td>0.39</td></tr><tr><td>Degree</td><td>Enrolment process</td><td>0.29</td></tr><tr><td>Mother&#x27;s education level</td><td>Socio-economic status</td><td>0.26</td></tr><tr><td>Father&#x27;s education level</td><td>Socio-economic status</td><td>0.26</td></tr><tr><td>Mother&#x27;s job</td><td>Socio-economic status</td><td>0.23</td></tr><tr><td>Father&#x27;s job</td><td>Socio-economic status</td><td>0.21</td></tr><tr><td>Academic year of enrolment</td><td>Enrolment process</td><td>0.17</td></tr><tr><td>Enrolment option</td><td>Enrolment process</td><td>0.17</td></tr><tr><td>Marital status</td><td>Socio-demographic</td><td>0.09</td></tr><tr><td>School type</td><td>High school background</td><td>0.06</td></tr><tr><td>Gender</td><td>Socio-demographic</td><td>0.05</td></tr><tr><td>Enrolment stage</td><td>Enrolment process</td><td>0.00</td></tr></table>

school grade and standardized exams grades are generally strong predictors of student success in higher education institutions (Cohn et al., 2004; Kuncel et al., 2005). The second group of most informative variables is composed of those referring to the results obtained in the first academic year. However, it is worth noting that these features are considered less important than those previously highlighted, which may indicate that the results obtained in the first year itself are not suficient to achieve high levels of accuracy in inferring students’ performance. This fact may be linked to evidence that the first year in the university is a period of adjustment (Nightingale et al., 2013), influencing the results that students achieve. Focusing on the least informative attributes, the enrolment stage seems not to be very informative. This may be related to the fact that a very high majority of Engineering School students enrol in the first stage. The school type is also a weak predictor, in addition to socio-demographic aspects, such as gender and marital status. Regarding the middle positioned attributes, there are the socio-economic related attributes, i.e. parents education and jobs. Despite not opposing the well-established positive relation between socio-economic status and academic achievement, the comparatively low position of the parents’ education and job variables in the ranking, appears to suggest that, in this particular setting, the relationship is weaker than others that the model is able to capture.

## 4.4 Student segmentation and educational implications

We propose a students’ segmentation framework, in order to easily and timely identify the target students for the diferent actions to be developed by the institutions for those specific segments. Therefore, we recommend the segmentation of students according to a cross-tabulation matrix that confronts the students’ predicted performance levels with the diferent levels of academic success already observed in the first year of their studies (see Figure 4). The indicator used to group students according to their academic achievement in the first year was the same used to group students by their final performance, i.e., the AP score.

![](/api/attachments/F8DSE335/fulltext/images/a960be2fdb439b473ec2df962e775d13463652a937fd887031df480748a28043.jpg)  
Fig. 4. Student segmentation matrix.

Figure 4 reveals that most of the students predicted to belong to one particular performance class by the end of the degree program, already give evidence of belonging to that performance class by the first year. In fact, the diagonal of the matrix refers to the majority of the students. However, and as can be anticipated, the cells adjacent to the diagonal are very populated, meaning that there is a significant number of students whose performance levels achieved in the first year do not correspond to the final levels.

We believe that each segment of students, represented in each of these cells, should be targeted in a diferent way. Indeed, by using this approach, the institution may robustly sustain their diferentiated actions, specifically targeted to mitigate or enhance performance efects. For example, if, in a certain moment, the institution is interested in involving those students who potentially are high achievers in a mid-term tutoring system as tutors (e.g. Nomura et al., 2017), the institution should focus on the 114 students who are predicted to belong to the top performers, and already demonstrate potential in their first year. If the institution did not consider their recent performance pattern, selecting, for example, the 14 students who in the first year were part of segment C, the peers would not recognize the students’ value, and even the students in charge would not feel comfortable in that position. In opposition, if the institution would focus on the students who demonstrated high performance, regardless of the predicted performance, these students could potentially disappoint (e.g., the 4 students who ended up belonging to cluster C).

In another scenario, if, for example, the institution is interested in promoting the shift of those potentially lower performing students to higher levels of performance, by setting up a counselling program managed by the internal services (e.g. Russell et al., 2008; Lee et al., 2009), the institution should target those students whom the model predicts will have poor performance, and that already demonstrate signs of poor performance, i.e., the segment with 92 students. In fact, it may be dificult to persuade students who have not yet demonstrated dificulties to take part in the program. In opposition, to involve students who may naturally overcome their dificulties (for example, the 14 students who may end up belonging to cluster B) may constitute a waste of resources.

In another scenario, the institution may intend to address the 6 students that are grouped in class B in the first year, and whose predicting model classifies them as class D. This may reveal that if there is an appropriate follow-up, the student may overcome the potential tendency of lowering their performance.

## 5 Conclusions

This study proposes a model, supported by data mining classification techniques, that predicts students’ overall academic performance based on the information available at the end of the first year of the students’ academic path at the University.

This study confirms that prediction modelling is efective in the academic domain, and that decision makers can use such models to efectively plan the institution strategy and policy (Natek and Zwilling, 2014), as well as to optimize its limited resource allocation (Delen, 2010).

The results show that, in the context of the analysis, the information available at the end of the first year is suficient to develop a solid model for a student’s performance prediction. For example, the model supported by random forests was able to reach performance levels of about 96.1%, in terms of accuracy.

Moreover, the results reveal that, in this particular case study, random forests classification technique is the one presenting the best results, and naive bayes is the one presenting the worst results. The results obtained also enable to conclude that the enrolment average grade and the enrolment exams average grade are the most relevant attributes for predicting the students’ overall academic performance.

This study also proposes a students’ segmentation framework, with the aim to distinguish students based on their observed achievements in the first year of the degree, and their propensity for academic success revealed by the prediction model. The proposed segmentation framework allows the identification of 25 segments of students and, thus, it may allow decision makers to specify diferent targets for the diferent actions to be developed.

From an educational standpoint, the authors believe that the proposed model is relevant, as it aids in inferring students’ behaviour, and allows, for example, timely decision making for interventions that may either promote an increase in academic performance rates for the poor achievers or an increase in the quality of the students’ academic experience for the high achievers.

On the one hand, using this tool, managers will be able to anticipate academic failure and act accordingly, in a proactive and timely manner, in order to change that tendency and mitigate its efects. For example, in order to stimulate those students whose propensity to not succeed is high and who have exhibited dificulties already in the first year of their academic path, decision makers could deploy measures that, for example, would involve psychological counselling services, the creation of tutoring systems and/or peer support groups, formal training in study skills, remedial lessons, etc. (Huang and Fang, 2013).

On the other hand, this tool can also be used to manage intellectual talent, and to enhance the impact of undergraduate education for particularly talented and motivated students, as it helps to identify potential academically-gifted students. Such students could either act as tutors for their peers (e.g. Nomura et al., 2017), or become monitors/assistants in practical classes, motivating them for a future academic career, or set up honours programmes to attract talented students, providing them with the possibility to enhance their skills and pursue individual interests. Such programs may help schools compete for gifted students who, otherwise, may be attracted to other schools (Hartshorn et al., 1997). The accomplishments of these gifted students enhance universities’ prestige and reputation, and leads to an atmosphere of academic vigour within the university community (Rinn and Plucker, 2004; Hbert and McBee, 2007). These programmes might also give students a slight advantage, in terms of grades earned and time to graduation (Harper et al., 2014).

## 6 Limitations and future work

This study sufers from some limitations. One of them is related to the sample bias. Despite considering a significant number of students, the conclusions drawn are only valid for the sample considered. In line with this, we only have data from a European institution. A good follow-up study would include other samples of data and would include other European as well as American faculties.

# ACCEPTED MANUSCRIPT

The model proposed was also tested with students attending only one learning area. Therefore, another possibility for future work is the extension of this project to other schools in diferent areas of learning, in which the students’ performance patterns may be diferent. In fact, the adaptation and the application of the proposed method to other institutions may lead to diferent conclusions due to the heterogeneity observed among students of diferent scientific areas and of schools with diferent educational strategies.

Another limitation of the study is linked with the nature of the data considered. The prediction proposed model is based on data available in the enrollment period and is also based on the aggregated results achieved in the end of the first academic year. The possibility of predicting the academic performance of the students at the end of the first year using other data, such as questionnaires (Richardson et al., 2012) and involvement data from - for example - moodle, constitutes an interesting topic for future research. Moreover, the use of results data for each course, instead of the aggregated results may be extremely relevant.

Regarding future work, the authors also believe that it is crucial to integrate the proposed method on the platforms already used by the institutions’ educational decision makers, such as programme directors and committees, to support the development of early and appropriate educational measures, targeting the specific segmented groups of students.

## 7 Acknowledgements

We thank Mercedes Filho for the critical reading of the manuscript. We also thank the reviewers for the constructive reviews and comments on the manuscript.

## References

Aher, S. B. and Lobo, L. M. R. J. (2013). Combination of machine learning algorithms for recommendation of courses in E-Learning System based on historical data. Knowledge-Based Systems, 51:1–14.

Aluko, R. O., Adenuga, O. A., Kukoyi, P. O., Soyingbe, A. A., and Oyedeji, J. O. (2016). Predicting the academic success of architecture students by pre-enrolment requirement: using machinelearning techniques. Construction Economics and Building, 16(4):86–98.

American Council on Education (2011). First in the World by 2020: What Will It Take? http://www.acenet.edu/the-presidency/columns-and-features/Pages/ First-in-the-World-by-2020-What-Will-It-Take.aspx. [Online; accessed 14-July-2017].

Araque, F., Roldn, C., and Salguero, A. (2009). Factors influencing university drop out rates. Computers & Education, 53(3):563–574.

Arsad, P. M., Buniyamin, N., and Manan, J. l. A. (2013). A neural network students’ performance prediction model (NNSPPM). In 2013 IEEE International Conference on Smart Instrumentation, Measurement and Applications (ICSIMA), pages 1–5.

Bacon, D. R. and Bean, B. (2006). GPA in Research Studies: An Invaluable but Neglected Opportunity. Journal of Marketing Education, 28(1):35–42.

Baeza-Yates, R. and Liaghat, Z. (2017). Quality-eficiency trade-ofs in machine learning for text processing. In 2017 IEEE International Conference on Big Data (Big Data), pages 897–904.

Berg, M. N. V. D. and Hofman, W. H. A. (2005). Student Success in University Education: A Multi-measurement Study of the Impact of Student and Faculty Factors on Study Progress. Higher Education, 50(3):413–446.

Bogaert, M., Ballings, M., and Van den Poel, D. (2016). The added value of Facebook friends data in event attendance prediction. Decision Support Systems, 82:26–34.

Bordea, G., Shahiri, A. M., Husain, W., and Rashid, N. A. (2015). A review on predicting students performance using data mining techniques. Procedia Computer Science, 72:414–422.

Breiman, L. (1996). Bagging Predictors. Machine Learning, 24(2):123–140.

Breiman, L. (2001). Random forests. Machine Learning, 45(1):5–32.

Busato, V. V., Prins, F. J., Elshout, J. J., and Hamaker, C. (1998). Learning styles: a crosssectional and longitudinal study in higher education. British Journal of Educational Psychology, 68(3):427–441.

Busato, V. V., Prins, F. J., Elshout, J. J., and Hamaker, C. (2000). Intellectual ability, learning style, personality, achievement motivation and academic success of psychology students in higher education. Personality and Individual Diferences, 29(6):1057–1068.

Bydzovska, H. (2016). Course enrollment recommender system. In Tifany Barnes, Min Chi, M. F., editor, Proceedings of the 9th International Conference on Educational Data Mining, pages 312–317, Raleigh, NC, USA. International Educational Data Mining Society.

Christian, T. M. and Ayub, M. (2014). Exploration of classification using NBTree for predicting students’ performance. In 2014 International Conference on Data and Software Engineering (ICODSE), pages 1–6.

Cohn, E., Cohn, S., Balch, D. C., and Bradley, J. (2004). Determinants of undergraduate GPAs: SAT scores, high-school GPA and high-school rank. Economics of Education Review, 23(6):577– 586.

Costa, E. B., Fonseca, B., Santana, M. A., de Arajo, F. F., and Rego, J. (2017). Evaluating the efectiveness of educational data mining techniques for early prediction of students’ academic failure in introductory programming courses. Computers in Human Behavior, 73:247–256.

Delen, D. (2010). A comparative analysis of machine learning techniques for student retention management. Decision Support Systems, 49(4):498–506.

Dietterich, T. G. (2000). Ensemble Methods in Machine Learning. In Multiple Classifier Systems, Lecture Notes in Computer Science, pages 1–15. Springer, Berlin, Heidelberg.

Dougherty, J., Kohavi, R., and Sahami, M. (1995). Supervised and Unsupervised Discretization of Continuous Features. In Prieditis, A. and Russell, S., editors, Machine Learning Proceedings 1995, pages 194–202. Morgan Kaufmann, San Francisco (CA).

Elfaki, A. O., Alhawiti, K. M., AlMurtadha, Y. M., Abdalla, O. A., and Elshiekh, A. A. (2015). Supporting students’ learning-pathway choices by providing rule-based recommendation system. International Journal of Education and Information Technologies, 9:81–94.

European Commission (2010). Europe 2020 targets. http://ec.europa.eu/eurostat/web/ europe-2020-indicators/europe-2020-strategy/targets. [Online; accessed 9-October-2017].

Freund, Y. and Schapire, R. E. (1996). Experiments with a New Boosting Algorithm. In In Proceedings of the Thirteenth International Conference on Machine Learning, pages 148–156. Morgan Kaufmann.

Gibson, D. (2017). Big data in higher education: Research methods and analytics supporting the learning journey. Technology, Knowledge and Learning, 22(3):237–241.

Gray, G., McGuinness, C., and Owende, P. (2014). An application of classification models to predict learner progression in tertiary education. In Advance Computing Conference (IACC), 2014 IEEE International, pages 549–554.

Groth, S. S. and Muntermann, J. (2011). An intraday market risk management approach based on textual analysis. Decision Support Systems, 50(4):680–691.

Guruler, H., Istanbullu, A., and Karahasan, M. (2010). A new student performance analysing system using knowledge discovery in higher educational databases. Computers & Education, 55(1):247–254.

Harlow, J. J. B., Harrison, D. M., and Meyertholen, A. (2014). Correlating student interest and high school preparation with learning and performance in an introductory university physics course. Physical Review Special Topics-Physics Education Research, 10(1):010112.

Harper, K. A., Abrams, L., and Rufley, J. P. (2014). A Longitudinal Study of the Impact of a First-Year Honors Engineering Program. pages 1–8.

Hartshorn, J. C., Berbiglia, V. A., and Heye, M. (1997). An honors program: directing our future leaders. The Journal of Nursing Education, 36(4):187–189.

Hearst, M. A., Dumais, S. T., Osman, E., Platt, J., and Scholkopf, B. (1998). Support vector machines. IEEE Intelligent Systems and their Applications, 13(4):18–28.

Hofait, A.-S. and Schyns, M. (2017). Early detection of university students with potential dificulties. Decision Support Systems.

Huang, S. and Fang, N. (2013). Predicting student academic performance in an engineering dynamics course: A comparison of four types of predictive mathematical models. Computers & Education, 61:133–145.

Hbert, T. P. and McBee, M. T. (2007). The Impact of an Undergraduate Honors Program on Gifted University Students. Gifted Child Quarterly, 51(2):136–151.

Jeeva, N., Elakia, Gayathri, and Aarthi (2014). Application of Data Mining in Educational Database for Predicting Behavioural Patterns of the Students. International Journal of Computer Science and Information Technologies, 5(3):4469–4472.

Kiang, M. Y., Fisher, D. M., Chen, J.-C. V., Fisher, S. A., and Chi, R. T. (2009). The application of SOM as a decision support tool to identify AACSB peer schools. Decision Support Systems, 47(1):51–59.

Kuncel, N. R., Crede, M., Thomas, L. L., Klieger, D. M., Seiler, S. N., and Woo, S. E. (2005). A meta-analysis of the validity of the Pharmacy College Admission Test (PCAT) and grade predictors of pharmacy student performance. American Journal of Pharmaceutical Education,

69(3):51.

Labatut, V. and Cherifi, H. (2011). Accuracy Measures for the Comparison of Classifiers. In Ali, A.-D., editor, The 5th International Conference on Information Technology, pages 1,5, amman, Jordan. Al-Zaytoonah University of Jordan.

Laugerman, M., Rover, D., Shelley, M., and Mickelson, S. (2015). Determining Graduation Rates in Engineering for Community College Transfer Students Using Data Mining. International Journal of Engineering Education, pages 1448–1457.

Lee, D., Olson, E. A., Locke, B., Michelson, S. T., and Odes, E. (2009). The Efects of College Counseling Services on Academic Performance and Retention. Journal of College Student Development, 50(3):305–319.

Lewis, D. D. (1998). Naive (Bayes) at forty: The independence assumption in information retrieval. In Ndellec, C. and Rouveirol, C., editors, Machine Learning: ECML-98, number 1398 in Lecture Notes in Computer Science, pages 4–15. Springer Berlin Heidelberg.

Maag Merki, K. (2011). Efects of the implementation of state-wide exit exams on students selfregulated learning. Studies in Educational Evaluation, 37(4):196–205.

Macfadyen, L. P. and Dawson, S. (2010). Mining LMS data to develop an early warning system for educators: A proof of concept. Computers & Education, 54(2):588–599.

Marbouti, F., Diefes-Dux, H. A., and Madhavan, K. (2016). Models for early prediction of at-risk students in a course using standards-based grading. Computers & Education, 103:1–15.

M´arquez-Vera, C., Cano, A., Romero, C., Noaman, A. Y. M., Mousa Fardoun, H., and Ventura, S. (2016). Early dropout prediction using data mining: a case study with high school students. Expert Systems, 33(1):107–124.

Mayilvaganan, M. and Kalpanadevi, D. (2014). Comparison of classification techniques for predicting the performance of students academic environment. In 2014 International Conference on Communication and Network Technologies (ICCNT), pages 113–118.

Menze, B. H., Kelm, B. M., Masuch, R., Himmelreich, U., Bachert, P., Petrich, W., and Hamprecht, F. A. (2009). A comparison of random forest and its Gini importance with standard chemometric methods for the feature selection and classification of spectral data. BMC Bioinformatics, 10:213.

Miao, J. and Haney, W. (2004). High School Graduation Rates:Alternative Methods and Implications. education policy analysis archives, 12(0):55.

Mishra, T., Kumar, D., and Gupta, S. (2014). Mining students’ data for prediction performance. In 2014 Fourth International Conference on Advanced Computing Communication Technologies, pages 255–262.

Natek, S. and Zwilling, M. (2014). Student data mining solutionknowledge management system related to higher education institutions. Expert Systems with Applications, 41(14):6400–6407.

Nightingale, S. M., Roberts, S., Tariq, V., Appleby, Y., Barnes, L., Harris, R. A., Dacre-Pool, L., and Qualter, P. (2013). Trajectories of university adjustment in the United Kingdom: Emotion management and emotional self-eficacy protect against initial poor adjustment. Learning and Individual Diferences, 27:174–181.

Nomura, O., Onishi, H., and Kato, H. (2017). Medical students can teach communication skills -

a mixed methods study of cross-year peer tutoring. BMC Medical Education, 17:103.

Palmer, S. (2013). Modelling engineering student academic performance using academic analytics. International journal of engineering education, 29(1):132–138.

Papamitsiou, Z. K., Terzis, V., and Economides, A. A. (2014). Temporal Learning Analytics for Computer Based Testing. In Proceedings of the Fourth International Conference on Learning Analytics And Knowledge, LAK ’14, pages 31–35, New York, NY, USA. ACM.

Parack, S., Zahid, Z., and Merchant, F. (2012). Application of data mining in educational databases for predicting academic trends and patterns. In 2012 IEEE International Conference on Technology Enhanced Education (ICTEE), pages 1–4.

Pena-Ayala, A., editor (2014a). Educational Data Mining, volume 524 of Studies in Computational Intelligence. Springer International Publishing, Cham.

Pena-Ayala, A. (2014b). Educational data mining: A survey and a data mining-based analysis of recent works. Expert Systems with Applications, 41(4):1432–1462.

Pike, G. R. and Saupe, J. L. (2002). Does High School Matter? An Analysis of Three Methods of Predicting First-Year Grades. Research in Higher Education, 43(2):187–207.

Piri, S., Delen, D., Liu, T., and Zolbanin, H. M. (2017). A data analytics approach to building a clinical decision support system for diabetic retinopathy: Developing and deploying a model ensemble. Decision Support Systems, 101(Supplement C):12–27.

Putnik, G., Costa, E., Alves, C., Castro, H., Varela, L., and Shah, V. (2016). Analysing the correlation between social network analysis measures and performance of students in social network-based engineering education. International Journal of Technology and Design Education, 26(3):413–437.

Quinlan, J. R. (1986). Induction of Decision Trees. Machine Learning, 1(1):81–106.

Rapidminer (2018). Rapidminer. https://rapidminer.com/. [Online; accessed 14-Mar-2017].

Richardson, M., Abraham, C., and Bond, R. (2012). Psychological correlates of university students’ academic performance: a systematic review and meta-analysis. Psychological Bulletin, 138(2):353–387.

Rinn, A. N. and Plucker, J. A. (2004). We Recruit Them, But Then What? The Educational and Psychological Experiences of Academically Talented Undergraduates. Gifted Child Quarterly, 48(1):54–67.

Romero, C., Espejo, P. G., Zafra, A., Romero, J. R., and Ventura, S. (2013a). Web usage mining for predicting final marks of students that use Moodle courses. Computer Applications in Engineering Education, 21(1):135–146.

Romero, C., Lpez, M.-I., Luna, J.-M., and Ventura, S. (2013b). Predicting students’ final performance from participation in on-line discussion forums. Computers & Education, 68:458–472.

Romero, C. and Ventura, S. (2007). Educational data mining: A survey from 1995 to 2005. Expert Syst. Appl., 33(1):135–146

Romero, C. and Ventura, S. (2010). Educational Data Mining: A Review of the State of the Art. IEEE Transactions on Systems, Man, and Cybernetics, Part C (Applications and Reviews), 40(6):601–618.

Romero, C. and Ventura, S. (2013). Data mining in education. Wiley Interdisciplinary Reviews:

Data Mining and Knowledge Discovery, 3(1):12–27.

Russell, J., Thomson, G., and Rosenthal, D. (2008). International student use of university health and counselling services. Higher Education, 56(1):59–75.

Saad, I. A. (2008). Predictive validity of high school performance with respect to academic achievement at the university level. International Journal of Psychology, 43(3-4):772–772.

Shapiro, D., Dundar, A., Wakhungu, P.K., Yuan, X., Nathan, A, and Hwang, Y (2016). Time to Degree: A National View of the Time Enrolled and Elapsed for Associate and Bachelors Degree Earners. Technical report, Herndon, VA: National Student Clearinghouse Research Center.

Strecht, P., Cruz, L., Soares, C., Mendes-Moreira, J., and Abreu, R. (2015). A Comparative Study of Classification and Regression Algorithms for Modelling Students’ Academic Performance. Madrid. International Educational Data Mining Society.

Thammasiri, D., Delen, D., Meesad, P., and Kasap, N. (2014). A critical assessment of imbalanced class distribution problem: The case of predicting freshmen student attrition. Expert Systems with Applications, 41(2):321–330.

Tinto, V. (1982). Limits of Theory and Practice in Student Attrition. The Journal of Higher Education, 53(6):687–700.

Vandamme, J.-P., Meskens, N., and Superby, J.-F. (2007). Predicting Academic Performance by Data Mining Methods. Education Economics, 15(4):405–419.

Vanthournout, G., Gijbels, D., Coertjens, L., Donche, V., and Van Petegem, P. (2012). Students’ Persistence and Academic Success in a First-Year Professional Bachelor Program: The Influence of Students’ Learning Strategies and Academic Motivation. Education Research International, 2012:1–10.

Wati, M., Haeruddin, and Indrawan, W. (2017). Predicting degree-completion time with data mining. In 2017 3rd International Conference on Science in Information Technology (ICSITech), pages 732–736.

Witten, I. H., Frank, E., and Hall, M. A. (2011). Data Mining: Practical Machine Learning Tools and Techniques. Morgan Kaufmann, USA, 3 edition.

Yue, H. and Fu, X. (2017). Rethinking Graduation and Time to Degree: A Fresh Perspective. Research in Higher Education, 58(2):184–213.

Zaklouta, F., Stanciulescu, B., and Hamdoun, O. (2011). Trafic sign classification using K-d trees and Random Forests. In The 2011 International Joint Conference on Neural Networks (IJCNN), pages 2151–2155.

## A APPENDICES

## A.1 Related literature

Table A1: Studies addressing students’ academic performance.

<table><tr><td>Study</td><td>Main Objective</td><td># In- stances</td><td>Techniques</td><td>Dependent variable</td></tr><tr><td>Huang and Fang (2013)</td><td>To predict students scores on three dynamics mid-term exams</td><td>2907 exams/ students</td><td>Linear Regression, neural networks, support vector machines</td><td>Students&#x27; scores on the dynamics final comprehensive exam</td></tr><tr><td>Marbouti et al. (2016)</td><td>To identify at-risk students in a course that used standards-based grading</td><td>2973 stu- dents</td><td>Logistic regression, neural networks, support vector machines, decision trees, naive bayes, k-nearest neighbour</td><td>Fail or do not fail a course</td></tr><tr><td>Costa et al. (2017)</td><td>To predict students likely to fail two courses (one performed on campus and another in a distance education format) at an early enough stage</td><td>262+161 stu- dents</td><td>Neural networks, support vec- tor machines, decision trees, naive bayes</td><td>Fail or do not fail a course</td></tr><tr><td>Gray et al. (2014)</td><td>To identify college students at risk of failing in the first year of study</td><td>1193 stu- dents</td><td>Logistic regression, neural net- works, support vector ma- chines, decision trees, naive bayes, k-nearest neighbor</td><td>First year poor academic achievers ( $GPA < 2$ ) and strong academic achievers ( $GPA > 2.5$ )</td></tr><tr><td>Macfadyen and Dawson (2010)</td><td>To identify which student on- line activities accurately pre- dict academic achievement</td><td>118 students</td><td>Logistic regression</td><td>Fail or do not fail a course</td></tr><tr><td>Guruler et al. (2010)</td><td>To categorize students as ei- ther successful or unsuccessful and determine profiles of students whose GPA is equal to 2.0 (which is the minimum GPA required for graduation) or greater and of those stu- dents whose GPA is equal to 3.0 or greater (honor degree)</td><td>&gt; 2699 stu- dents</td><td>Decision trees</td><td>Final GPA is equal to 2.0 or greater+ Final GPA is equal to 3.0 or greater</td></tr><tr><td>Laugerman et al. (2015)</td><td>To determine what academic integration characteristics con- tribute to their success in engi- neering using post-hoc gradua- tion data</td><td>472 students</td><td>Boosted regression</td><td>Earn or not an engineering degree</td></tr><tr><td>Hoffait and Schyns (2017)</td><td>To identify freshmens&#x27; profiles likely to face major difficul- ties to complete their first aca- demic year</td><td>6845 stu- dents</td><td>Logit regression, neural net- works, random forests</td><td>Complete first year or not</td></tr></table>

Continued on next page

Table A1 – continued from previous page

<table><tr><td>Study</td><td>Main Objective</td><td># In- stances</td><td>Techniques</td><td>Dependent variable</td></tr><tr><td>Romero and Ventura (2013)</td><td>To predict the marks that uni- versity students will obtain in the final exam of a course</td><td>438+135+438 students</td><td>Decision trees, neural net- works, rule induction</td><td>Student fail in the exam of a course (value is &lt; 5), pass (value is ≥ 5 and &lt; 7), has a good mark (value is ≥ 7 and &lt; 9) or has an excellent mark (value is ≥ 9)</td></tr><tr><td>Palmer (2013)</td><td>To predict academic perfor- mance of engineering students enrolled in a second-year class</td><td>132 students</td><td>Logistic regression</td><td>Fail or do not fail a course</td></tr><tr><td>Romero et al. (2013a)</td><td>To predict students&#x27; final marks based on their partici- pation in forums</td><td>114 students</td><td>Logit regression, neural net- works, random forests, naive bayes, bayesNet, Sequential Minimal Optimization</td><td>Fail or do not fail a course</td></tr><tr><td>Mishra et al. (2014)</td><td>To predict the third semester performance of MCA students</td><td>250 students</td><td>Decision trees, random trees</td><td>Third semester performance as BAVG (&lt; 60%), AVG (60% to less than 70%), ABVG (70% to less than 79%) and EXCL (≥ 80%)</td></tr><tr><td>Natek and Zwilling (2014)</td><td>To predict the success rate of students enrolled in their courses</td><td>106 students</td><td>Decision trees</td><td>High (values between 8 and 10), medium (values between 6 and 7), low final grade (values lower than 6) in informatics courses</td></tr><tr><td>Arsad et al. (2013)</td><td>To predict the academic per- formance of Electrical Degree students</td><td>391+505 stu- dents</td><td>Neural Networks</td><td>Cumulative Grade Point Average (CGPA) in semester 8</td></tr><tr><td>Strecht et al. (2015)</td><td>To predict approval/failure in a course and to predict its grade</td><td>5779 courses/students</td><td>Linear regression, neural net- works, support vector ma- chines, decision trees, naive bayes, k-nearest neigbour, ad- aBoost</td><td>Fail or do not fail a course; Final Grade</td></tr><tr><td>Vandamme et al. (2007)</td><td>To predict the first year perfor- mance of students</td><td>227 students</td><td>Discriminant analysis, neural networks, random forests and decision trees</td><td>High risk (average mark of less than 45% in a session), Low risk (average of more than 70% a ses- sion), Medium risk (average grade between 45% and 70%)</td></tr><tr><td>Aluko et al. (2016)</td><td>To predict academic success of architecture students based on information provided in prior academic performance</td><td>101 students</td><td>Discriminant analysis, k- nearest neighbour</td><td>Pass (CGPA at graduation be- tween 5-2.4) and Fail (CGPA at graduation between 2.39-0)</td></tr></table>

Continued on next page

Table A1 – continued from previous page

<table><tr><td>Study</td><td>Main Objective</td><td>#Instances</td><td>Instances</td><td>Techniques</td><td>Dependent variable</td></tr><tr><td>Current study</td><td>To predict performance levels in the end of the degree (or at an advanced stage of the academic career), in the end of the first academic year</td><td>2459 students</td><td></td><td>Random forests, decision trees, support vector machines, naive bayes, bagged trees and boosted trees</td><td>A, B, C, D, E levels determined based on the ratio between the weighted mean of the grades obtained along the academic career and the total number of ECTS credits the student enrolled in</td></tr></table>

## A.2 Dataset variables

Table A2: Dataset variables.

<table><tr><td>Attribute</td><td>Type</td><td>Description</td><td>Values(frequency)/Mean(std. deviation)</td></tr><tr><td>1</td><td>Categorical</td><td>Weighted mean of the grade</td><td>A:10.3%B:39.0%C:28.1%D:14.8%E:7.8%</td></tr><tr><td>2</td><td>Categorical</td><td>Gender</td><td>Male:77.5%Female:22.5%</td></tr><tr><td>3</td><td>Categorical</td><td>Marital status</td><td>Single:98.0%Married:2.0%</td></tr><tr><td>4</td><td>Categorical</td><td>Father's education level</td><td>Undergraduate level: 20.2%Unknown:19.4%1st cycle of elementary school:13.9%Secondary education:13.4%3rd Cycle of Elementary School:12.7%2nd Cycle of Elementary School:6.8%Bachelors:4.1%Postgraduate level (masters):3.3%</td></tr><tr><td colspan="4">Table A2 – continued from previous page</td></tr><tr><td>Attr.</td><td>Type</td><td>Description</td><td>Values(frequency)/Mean(std. deviation)</td></tr><tr><td></td><td></td><td></td><td>Postgraduate level (PhD):2.4%</td></tr><tr><td></td><td></td><td></td><td>Postsecondary non-higher education:1.8%</td></tr><tr><td></td><td></td><td></td><td>Able to read and write but has not completed 1st cycle of elementary</td></tr><tr><td></td><td></td><td></td><td>Technological specialization (higher education):0.8%</td></tr><tr><td></td><td></td><td></td><td>Not able to read and write :0.1%</td></tr><tr><td></td><td></td><td></td><td>Unknown: 27.8%</td></tr><tr><td></td><td></td><td></td><td>Other activity: 17.6%</td></tr><tr><td></td><td></td><td></td><td>Qualified civil servants, directors and qualified company employees: 1</td></tr><tr><td></td><td></td><td></td><td>Intermediate-level technicians and professionals: 9.1%</td></tr><tr><td></td><td></td><td></td><td>Specialists in intellectual and scientific professions:7.6%</td></tr><tr><td></td><td></td><td></td><td>Services and sales staff: 6.9%</td></tr><tr><td>5</td><td>Categorical</td><td>Father's job</td><td>Workers, craftsmen and similar:6.5%</td></tr><tr><td></td><td></td><td></td><td>Administrative staff and similar workers:4.5%</td></tr><tr><td></td><td></td><td></td><td>Unskilled workers:2.6%</td></tr><tr><td></td><td></td><td></td><td>Machine operators and assembly workers:1.6%</td></tr><tr><td></td><td></td><td></td><td>Farmers and workers qualified in agriculture and fishing:1.4%</td></tr><tr><td></td><td></td><td></td><td>Members of the armed forces:1.1%</td></tr><tr><td></td><td></td><td></td><td>Undergraduate level: 26.6%</td></tr><tr><td></td><td></td><td></td><td>Unknown:18.8%</td></tr><tr><td></td><td></td><td></td><td>3rd cycle of elementary school:12.2%</td></tr><tr><td></td><td></td><td></td><td>Secondary education:11.2%</td></tr><tr><td></td><td></td><td></td><td>1st Cycle of Elementary School:10.0%</td></tr><tr><td></td><td></td><td></td><td>2nd Cycle of Elementary School:7.6%</td></tr><tr><td></td><td></td><td></td><td>Postgraduate level (masters):3.6%</td></tr><tr><td>6</td><td>Categorical</td><td>Mother's education level</td><td>Able to read and write but has not completed 1st cycle of elementary</td></tr><tr><td></td><td></td><td></td><td>Bachelors:3.2%</td></tr><tr><td></td><td></td><td></td><td>Postgraduate level (PhD):1.5%</td></tr><tr><td></td><td></td><td></td><td>Postsecondary non-higher education:1.5%</td></tr></table>

## ACCEPTED MANUSCRIPT

Table A2 – continued from previous page

<table><tr><td rowspan="3">Attr.</td><td rowspan="3">Type</td><td rowspan="3">Description</td><td>Values(frequency)/Mean(std. deviation)</td></tr><tr><td>Technological specialization (higher education):0.4%</td></tr><tr><td>Not able to read and write :0.1%</td></tr><tr><td></td><td></td><td></td><td>Unknown: 34.9%</td></tr><tr><td></td><td></td><td></td><td>Other activity: 19.2%</td></tr><tr><td></td><td></td><td></td><td>Qualified civil servants, directors and qualified company employees: 1.8%</td></tr><tr><td></td><td></td><td></td><td>Specialists in intellectual and scientific professions:9.6%</td></tr><tr><td></td><td></td><td></td><td>Administrative staff and similar workers:8.3%</td></tr><tr><td>7</td><td>Categorical</td><td>Mother&#x27;s job</td><td>Intermediate-level technicians and professionals: 5.9%</td></tr><tr><td></td><td></td><td></td><td>Services and sales staff: 4.8%</td></tr><tr><td></td><td></td><td></td><td>Unskilled workers:3.2%</td></tr><tr><td></td><td></td><td></td><td>Workers, craftsmen and similar:3.0%</td></tr><tr><td></td><td></td><td></td><td>Farmers and workers qualified in agriculture and fishing:0.6%</td></tr><tr><td></td><td></td><td></td><td>Machine operators and assembly workers:0.3%</td></tr><tr><td>8</td><td>Categorical</td><td>School type</td><td>Public: 83.7%</td></tr><tr><td></td><td></td><td></td><td>Private: 16.3%</td></tr><tr><td></td><td></td><td></td><td>1: 81.5%</td></tr><tr><td></td><td></td><td></td><td>2: 12.3%</td></tr><tr><td>9</td><td>Categorical</td><td>Enrolment option</td><td>3: 3.7%</td></tr><tr><td></td><td></td><td></td><td>4: 1.6%</td></tr><tr><td></td><td></td><td></td><td>5: 0.6%</td></tr><tr><td></td><td></td><td></td><td>6: 0.3%</td></tr><tr><td>10</td><td>Categorical</td><td>Enrolment stage</td><td>1: 87.3%</td></tr><tr><td></td><td></td><td></td><td>2: 12.7%</td></tr><tr><td></td><td></td><td></td><td>2003:23.8%</td></tr><tr><td></td><td></td><td></td><td>2004:21.7%</td></tr><tr><td>11</td><td>Categorical</td><td>Academic year of enrolment</td><td>2005:16.0%</td></tr><tr><td></td><td></td><td></td><td>2006:18.2%</td></tr><tr><td></td><td></td><td></td><td>2007:20.3%</td></tr></table>

Table A2 – continued from previous page

<table><tr><td>Attr.</td><td>Type</td><td>Description</td><td>Values(frequency)/Mean(std. deviation)</td></tr><tr><td>12</td><td>Numerical</td><td>High school average grade</td><td>16.0 (1.5)</td></tr><tr><td>13</td><td>Numerical</td><td>Enrolment exams average grade</td><td>148.4 (22.3)</td></tr><tr><td>14</td><td>Numerical</td><td>Enrolment average grade</td><td>154.3 (16.3)</td></tr><tr><td></td><td></td><td></td><td>Civil engineering (LEC):17.5%</td></tr><tr><td></td><td></td><td></td><td>Electrical and Computers Engineering (LEEC):14.5%</td></tr><tr><td></td><td></td><td></td><td>Informatics and Computing Engineering (LIEC):9.6%</td></tr><tr><td></td><td></td><td></td><td>Master in Civil Engineering (MIEC):9.6%</td></tr><tr><td></td><td></td><td></td><td>Mechanical Engineering (LEM):9.2%</td></tr><tr><td></td><td></td><td></td><td>Master in Electrical and Computers Engineering (MIEEC):7.7%</td></tr><tr><td></td><td></td><td></td><td>Master in Informatics and Computing Engineering (MIEIC):6.4%</td></tr><tr><td></td><td></td><td></td><td>Master in Mechanical Engineering (MIEM):5.9%</td></tr><tr><td>15</td><td>Categorical</td><td>Degree</td><td>Industrial Engineering and Management (LGEI):4.1%</td></tr><tr><td></td><td></td><td></td><td>Chemical Engineering (LEQ):3.4%</td></tr><tr><td></td><td></td><td></td><td>Master in Environmental Engineering (MIEA):3.1%</td></tr><tr><td></td><td></td><td></td><td>Master in Industrial Engineering and Management (MIEIG):1.9%</td></tr><tr><td></td><td></td><td></td><td>Master in Chemical Engineering (MIEQ):1.9%</td></tr><tr><td></td><td></td><td></td><td>Engineering and Environment Management (LEGA):1.5%</td></tr><tr><td></td><td></td><td></td><td>Master in Bioengineering (MIB):1.5%</td></tr><tr><td></td><td></td><td></td><td>Metallurgical and Materials Engineering (LEMM):1.5%</td></tr><tr><td></td><td></td><td></td><td>Master in Metallurgical and Materials Engineering (MIEMM):0.7%</td></tr><tr><td>15</td><td>Numerical</td><td>Average number of exams attended to conclude the courses of the first year</td><td>6.8 (1.5)</td></tr><tr><td>16</td><td>Numerical</td><td>Number of ECTS completed in the first semester</td><td>24.6 (6.9)</td></tr><tr><td>17</td><td>Numerical</td><td>Average grade in the first semester</td><td>13.14 (1.6)</td></tr><tr><td>18</td><td>Numerical</td><td>Number of ECTS completed in the second semester</td><td>22.5 (8.3)</td></tr><tr><td>19</td><td>Numerical</td><td>Average grade in the second semester</td><td>12.6 (1.7)</td></tr></table>

## A.3 Confusion matrices

## Table A3

Confusion matrix - Decision trees

<table><tr><td colspan="8">Observed</td></tr><tr><td colspan="2"></td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>Prec.</td></tr><tr><td rowspan="5">Predicted</td><td>A</td><td>233</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1.00</td></tr><tr><td>B</td><td>22</td><td>929</td><td>46</td><td>21</td><td>2</td><td>0.91</td></tr><tr><td>C</td><td>1</td><td>21</td><td>635</td><td>34</td><td>23</td><td>0.89</td></tr><tr><td>D</td><td>0</td><td>9</td><td>11</td><td>301</td><td>11</td><td>0.91</td></tr><tr><td>E</td><td>0</td><td>0</td><td>2</td><td>4</td><td>153</td><td>0.96</td></tr><tr><td></td><td>Recall</td><td>0.91</td><td>0.97</td><td>0.91</td><td>0.84</td><td>0.81</td><td></td></tr></table>

## Table A4

Confusion matrix - SVM

<table><tr><td colspan="8">Observed</td></tr><tr><td colspan="2"></td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>Prec.</td></tr><tr><td rowspan="5">Predicted</td><td>A</td><td>248</td><td>24</td><td>3</td><td>4</td><td>0</td><td>0.89</td></tr><tr><td>B</td><td>6</td><td>912</td><td>26</td><td>8</td><td>0</td><td>0.96</td></tr><tr><td>C</td><td>0</td><td>18</td><td>646</td><td>20</td><td>5</td><td>0.94</td></tr><tr><td>D</td><td>0</td><td>4</td><td>15</td><td>325</td><td>7</td><td>0.93</td></tr><tr><td>E</td><td>0</td><td>0</td><td>2</td><td>7</td><td>179</td><td>0.95</td></tr><tr><td></td><td>Recall</td><td>0.98</td><td>0.95</td><td>0.93</td><td>0.89</td><td>0.94</td><td></td></tr></table>

## Table A5

Confusion matrix - NB

<table><tr><td colspan="2"></td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>Prec.</td></tr><tr><td rowspan="5">Predicted</td><td>A</td><td>207</td><td>68</td><td>9</td><td>0</td><td>0</td><td>0.73</td></tr><tr><td>B</td><td>44</td><td>770</td><td>102</td><td>31</td><td>4</td><td>0.81</td></tr><tr><td>C</td><td>5</td><td>73</td><td>496</td><td>44</td><td>18</td><td>0.78</td></tr><tr><td>D</td><td>0</td><td>38</td><td>53</td><td>254</td><td>28</td><td>0.68</td></tr><tr><td>E</td><td>0</td><td>11</td><td>34</td><td>31</td><td>139</td><td>0.65</td></tr><tr><td></td><td>Recall</td><td>0.81</td><td>0.80</td><td>0.71</td><td>0.71</td><td>0.74</td><td></td></tr></table>

Table A6

Confusion matrix - RF

<table><tr><td colspan="8">Observed</td></tr><tr><td colspan="2"></td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>Prec.</td></tr><tr><td rowspan="5">Predicted</td><td>A</td><td>234</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0.99</td></tr><tr><td>B</td><td>20</td><td>944</td><td>19</td><td>2</td><td>4</td><td>0.95</td></tr><tr><td>C</td><td>0</td><td>12</td><td>665</td><td>22</td><td>8</td><td>0.94</td></tr><tr><td>D</td><td>0</td><td>0</td><td>8</td><td>340</td><td>0</td><td>0.98</td></tr><tr><td>E</td><td>0</td><td>0</td><td>0</td><td>0</td><td>179</td><td>1.00</td></tr><tr><td></td><td>Recall</td><td>0.92</td><td>0.99</td><td>0.96</td><td>0.93</td><td>0.94</td><td></td></tr></table>

## Table A7

Confusion matrix - Bagging DT

<table><tr><td colspan="8">Observed</td></tr><tr><td colspan="2"></td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>Prec.</td></tr><tr><td rowspan="5">Predicted</td><td>A</td><td>191</td><td>12</td><td>2</td><td>0</td><td>0</td><td>0.93</td></tr><tr><td>B</td><td>60</td><td>918</td><td>85</td><td>23</td><td>4</td><td>0.84</td></tr><tr><td>C</td><td>3</td><td>21</td><td>599</td><td>30</td><td>13</td><td>0.90</td></tr><tr><td>D</td><td>0</td><td>7</td><td>4</td><td>310</td><td>10</td><td>0.94</td></tr><tr><td>E</td><td>0</td><td>0</td><td>2</td><td>1</td><td>164</td><td>0.98</td></tr><tr><td></td><td>Recall</td><td>0.75</td><td>0.96</td><td>0.87</td><td>0.85</td><td>0.86</td><td></td></tr></table>

## Table A8

Confusion matrix - Boosting DT

<table><tr><td colspan="8">Observed</td></tr><tr><td colspan="2"></td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>Prec.</td></tr><tr><td rowspan="5">Predicted</td><td>A</td><td>242</td><td>12</td><td>0</td><td>0</td><td>0</td><td>0.95</td></tr><tr><td>B</td><td>10</td><td>924</td><td>14</td><td>6</td><td>4</td><td>0.96</td></tr><tr><td>C</td><td>0</td><td>18</td><td>662</td><td>10</td><td>0</td><td>0.96</td></tr><tr><td>D</td><td>2</td><td>2</td><td>14</td><td>346</td><td>8</td><td>0.93</td></tr><tr><td>E</td><td>0</td><td>2</td><td>2</td><td>2</td><td>179</td><td>0.97</td></tr><tr><td></td><td>Recall</td><td>0.95</td><td>0.96</td><td>0.96</td><td>0.95</td><td>0.94</td><td></td></tr></table>

## BIOGRAPHICAL NOTES

V. L. Miguéis is an Assistant Professor in the department of Industrial Engineering and Management at the School of Engineering of the University of Porto, Portugal. She received her PhD in Industrial Engineering and Management from the School of Engineering of the University of Porto. Her research interests include educational mining, customer relationship management, data mining, customer intelligence and forecasting. Her research specifically focuses on the use of data mining techniques to support the decision process. She has published papers in several international journals indexed in the Web of Knowledge. She has taught courses in operations research, data mining, statistics and operations management. She is the external relations manager of the Industrial Engineering and Management Master of the School of Engineering of the University of Porto.

Ana Freitas has a degree in Education and a Master in Educational Sciences, both from the University of Minho, Portugal. She’s also a PhD candidate in Educational Sciences at the University of Porto, Portugal. She’s been working, for 15 years, in Higher Education Institutions, in the area of educational consultancy & support, academic management and research in education. She is currently working as a Senior Officer at the Laboratory of Teaching and Learning, in the School of Engineering, University of Porto. Her specific interest areas and field of activities are in professors’ continuing professional development, doctoral education/innovative doctoral training and academic success. She collaborated in 6 financed projects. She’s accredited as a trainer of trainers and as a trainer of teachers/professors.

Paulo J. V. Garcia holds a PhD in Physics from Université de Lyon (France). He is an Associate Professor at the Department of Engineering Physics at the School of Engineering of the University of Porto, Portugal and is also the Coordinator of the Teaching Learning Laboratory of the same School. He conducts research mostly in the fields of astrophysics, optical instrumentation, signal processing and physics education.

André Silva received his Master’s degree in Informatics and Computing Engineering from the School of Engineering of the University of Porto, Portugal. He became interested in educational mining and business analytics after being developing his masters’ project.

## Highlights

• We propose a two-stage model for early predicting students overall academic success

• We introduce a new academic performance metric and use single and ensemble data mining techniques

• We introduce a students’ segmentation approach based on evidences and predictions

• A dataset of about 2500 students is used to validate the proposed methodology

• The proposed model reveals to have high predictive power (above 95%)

![](/api/attachments/F8DSE335/fulltext/images/213ddbac5cdc5b827a395382b8ba0bab198baf3629a3a24ad186e21e35237cac.jpg)

![](/api/attachments/F8DSE335/fulltext/images/09fe025990534354ca4c0c2bcc9025f2ee113a4c1aade3b98a1429d850d96e94.jpg)

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">Observed</td></tr><tr><td>X</td><td>Y</td><td>Z</td></tr><tr><td rowspan="3">Predicted</td><td>X</td><td>a</td><td>b</td><td>c</td></tr><tr><td>Y</td><td>d</td><td>e</td><td>f</td></tr><tr><td>Z</td><td>g</td><td>h</td><td>i</td></tr></table>

Figure 3

Students segmentation matrix  
![](/api/attachments/F8DSE335/fulltext/images/2afe8fdde812a9139f7ce9288e6861a70f2849b97025479ead302864a9fed607.jpg)  
Figure 4
