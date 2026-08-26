---
otero_id: 12804
otero_key: "B6JGVWCA"
title: "A data analytics approach to building a clinical decision support system for diabetic retinopathy: Developing and deploying a model ensemble"
authors: "Saeed Piri; Dursun Delen; Tieming Liu; Hamed M. Zolbanin"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.05.012"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A data analytics approach to building a clinical decision support system for diabetic retinopathy: Developing and deploying a model ensemble

Saeed Piri <sup>a</sup>, Dursun Delen <sup>b,</sup>⁎, Tieming Liu <sup>a</sup>, Hamed M. Zolbanin <sup>c</sup>

<sup>a</sup> Department of Industrial Engineering and Management, College of Engineering, Architecture and Technology, Oklahoma State University, Stillwater, OK 74078, United States

<sup>b</sup> Department of Management Science and Information Systems, Spears School of Business, Oklahoma State University, Tulsa, OK 74106, United States

<sup>c</sup> Department of Information Systems and Operations Management, Miller School of Business, Ball State University, Muncie, IN 47306, United States

## a r t i c l e i n f o

Article history: Received 8 September 2016 Received in revised form 22 April 2017 Accepted 7 May 2017 Available online xxxx

Keywords: Diabetic retinopathy Data analytics Predictive modeling Clinical decision support systems Model ensembles Variable importance

## a b s t r a c t

Diabetes is a common chronic disease that may lead to several complications. Diabetic retinopathy (DR), one of the most serious of these complications, is the most common cause of vision loss among diabetic patients. In this paper, we analyzed data from more than 1.4 million diabetics and developed a clinical decision support system (CDSS) for predicting DR. While the existing diagnostic approach requires access to ophthalmologists and expensive equipment, our CDSS only uses demographic and lab data to detect patients' susceptibility to retinopathy with a high accuracy. We illustrate how a combination of multiple data preparation and modeling steps helped us improve the performance of our CDSS. From the data preprocessing aspect, we aggregated the data at the patient level and incorporated comorbidity information into our models. From the modeling perspective, we built several predictive models and developed a novel “confidence margin” ensemble technique that outperformed the existing ensemble models. Our results suggest that diabetic neuropathy, creatinine serum, blood urea nitrogen, glucose serum plasma, and hematocrit are the most important variables in detecting DR. Our CDSS provides several important practical implications, including identifying the DR risk factors, facilitating the early diagnosis of DR, and solving the problem of low compliance with annual retinopathy screenings.

© 2017 Elsevier B.V. All rights reserved.

## 1. Introduction

An estimated 29 million Americans, aged 20 years or older, either have been diagnosed or remain undiagnosed with diabetes. In 2012, the United States incurred about \$245 billion in direct and indirect medical costs related to disability, work loss, and premature mortality associated with diabetes [1]. Over the course of this disease, the blood glucose level imbalance may lead to several complications, including neurological disorders, heart problems, kidney disease, and hyperosmolarity. A major complication of diabetes that has not received enough attention is diabetic retinopathy. This complication is caused by damage to the blood vessels of retina, the light-sensitive tissue at the back of the eye. At its early stages, diabetic retinopathy may be asymptomatic or only show mild vision problems, but if it is not diagnosed and treated in time, it can eventually cause blindness. This unnoticed progress of diabetic retinopathy has turned it into the most common cause of vision loss among diabetics and a leading cause of blindness for American adults. According to the 2014 National Diabetes Statistics Report, between the years 2005 and 2008, 4.2 million of American diabetics aged 40 or older suffered from diabetic retinopathy and this number is expected to grow to about 16 million by 2050. Among patients who have had diabetes for up to 20 years, almost all type І and N60% of type ІІ diabetics develop retinopathy [2].

Although retinopathy is preventable and existing treatments can slow down the disease progress, vision loss that happens in the late stages of retinopathy cannot be restored. Thus, it is critical to diagnose this complication as early as possible. The current method for diagnosing diabetic retinopathy is a comprehensive eye examination in which after a patient's eye is dilated, an ophthalmologist examines the retina with an indirect ophthalmoscope and a special lens. Unfortunately, and despite the intimidating statistics about the high prevalence of retinopathy, the annual diabetic retinopathy evaluation has one of the lowest rates of patient compliance for several reasons. First, many patients do not seek proper medical attention because this disease is asymptomatic at the early stages; second, availability of ophthalmologists is low or even nonexistent in many areas, especially in rural communities; and third, many patients find the necessary eye dilation unpleasant. Because of this low compliance rate, about 50% of patients with diabetic retinopathy are undiagnosed (National Eye Institute report, 2015). Therefore,

S. Piri et al. / Decision Support Systems xxx (2017) xxx–xxx

the rising prevalence of diabetes, coupled with barriers to ophthalmological screenings that lead to a high rate of undiagnosed diabetic retinopathy patients, create an urgent need for a tool to detect this complication. To be useful, this tool should be non-invasive, readily available to diabetic patients, validated on a large number of cases, and eliminate the need for specialized equipment that is not universally available. This study sets out to employ an analytics approach on data collected during routine primary care visits to fills this gap. Specifically, we build a clinical decision support system (CDSS) for prediction of diabetic retinopathy that satisfies the aforementioned requirements for diagnostic tools.

Our CDSS has several advantages over the existing diagnostic systems. First and foremost, it only uses the results of a simple blood test and demographic data to predict the risk of diabetic retinopathy. Therefore, unlike the dominant approach in the extant literature that uses image processing on images of retina, it does not require eye exams, thereby addressing the low rates of compliance with annual ophthalmologic tests for diabetic patients. Equally important, our CDSS eliminates the need to have access to specialists, which is particularly critical for patients living in remote areas. Second, our decision support system is based on a large database of clinical encounters that span over several years and across several states of America. The decisions of this system are far more generalizable and valid compared to those of other systems that employ a similar approach but only use data from a few hundred patients. Finally, our CDSS uses a greater number of risk factors to predict the outcome. This not only improves the prediction results, but also sheds more light on contribution and importance of different risk factors on diabetic patients' susceptibility to retinopathy.

We expect that the CDSS we develop in this effort will be able to detect diabetic retinopathy at its early stages with a high degree of accuracy. This CDSS, which relies exclusively on lab data, not only helps overcome one of the major barriers to the early diagnosis of diabetic retinopathy, but also provides a new standard of care that will improve quality and increase compliance in healthcare without raising costs. Therefore, this work contributes to the decision support and medical informatics literatures from three perspectives: methodology, data management, and application. In the methodological aspect, we develop and evaluate a novel approach in building ensemble models. This approach aggregates the predictions of individual models by calculating a weighted confidence margin across all models. However, in contrast to the existing weighted averaging ensembles that assign weights to individual models based on their overall prediction performance, our confidence margin ensemble assigns varying weights to the constituting models. These weights are calculated for each observation in the data and are based on the distance between the estimated probabilities of records and the decision cut off point. We show how this approach improves the accuracy of decisions made by our CDSS. From the data management perspective, we processed a very large transactional database of clinical encounters and aggregated the observations at the patient level. This enabled us to create a single data set containing comorbid conditions of patients to develop an accurate picture of their health status. Consequently, our CDSS is able to consider a larger number of risk factors and provides a more realistic depiction of the coexistence of chronic diseases. Finally, in the application aspect, we develop an accessible, easy-to-implement, and inexpensive solution to the currently high proportion of undiagnosed retinopahty among diabetics. This CDSS reduces direct and indirect medical costs of the healthcare system in the United States and more importantly, saves eyesight for a large number of citizens.

The rest of this paper is organized as follows. In Section 2, we provide a brief review of the related literature in the field of healthcare analytics. In Section 3, we explain the methodology we employed in the study. The results of the predictive models are provided in Section 4, and Section 5 includes discussion and conclusion of the research.

## 2. Literature review

The extensive availability of healthcare data in the past decade, as well as advances in the area of data mining and machine learning, has generated the interesting field of healthcare analytics. The development of CDSSs by data analysts with the aid of clinical experts' knowledge has eased the burden on physicians and clinicians and smoothed clinical procedures. Analyzing healthcare data and applying machine learning techniques in this area have several benefits: patients can be stratified based on the severity of a particular disease or condition and, consequently, suitable treatments can be provided for each group; risk factors of different diseases can be identified, leading potentially to better health management; and diseases can be detected at early stages, allowing for appropriate interventions and treatments. For a comprehensive discussion about healthcare analytics, its promises and its potentials we refer the readers to [3].

Even though CDSSs based on EMR data have been broadly used by practitioners in recent years, the field of ophthalmology has received limited attention [4]. This dearth exists while several researchers have studied the relationship between diabetic retinopathy and different potential risk factors. For instance, Karma, et al. [5] studied the existence of diabetic retinopathy in 328 diabetic patients using ophthalmoscopy and wide field fundus photography and tried to identify the association between diabetes duration and other risk factors, such as nephropathy and coronary disease. In another study, Klein, et al. [6] measured the relationship between retinopathy and hyperglycemia by studying 1878 diabetics.

Most of the existing CDSSs for diabetic retinopathy use image processing algorithms. While these algorithms facilitate early detection of diabetic retinopathy, they require an image of the retina. Therefore, although they ease the burden of assessing the images of retina, they fail to address the evident barrier of patients' access to specialists. Examples of studies that belong to this category are (Kahai, et al. [7], Paunksnis, et al. [8], Marsolo, et al. [9], Tsai, et al. [10], Noronha, et al. [11] Bursell, et al. [12], Kumar and Madheswaran [13], and Xiao, et al. [14]). We refer the readers to Mookiah, et al. [15] for a comprehensive review of research in this category.

The other category of CDSSs for diabetic retinopathy includes those matched with lenses or an ophthalmoscope that can be used on a smartphone. Prasanna, et al. [16] proposed a portable smartphonebased CDSS that requires attaching an ophthalmoscope to a smartphone to capture fundus images, and captured images will be processed by the algorithm installed on the smartphone. Bourouis, et al. [17] also proposed a smartphone-based algorithm integrated with microscopic lenses used to capture retinal images. Their CDSS uses a neural network model to analyze such images and provide the results. Despite all the benefits of these algorithms, additional equipment is still required for retinal imaging, which, for many diabetics and primary care providers, may be cost-prohibitive or unavailable.

Many research projects have studied the association of retinopathy and different lab tests. For instance, the association of retinopathy and hemoglobin A1c has been shown in several studies ([18,19,20]). Researchers have also studied the relationship between cholesterol and retinopathy and have found the two to be related ([21,22]). The Diabetes Control and Complications Trial (DCCT) and the U.K. Prospective Diabetes Study (UKPDS) have shown that controlling the glucose level could reduce the risk of retinopathy [23]. Other studies have shown that retinopathy and hypertension are associated [24]. Besides blood tests, some urine tests such as proteinuria are shown to be associated with retinopathy [25].

While these studies show the potential for developing tools that can detect or predict retinopathy using lab results, only a few studies have used lab and demographic data to detect diabetic retinopathy without requiring retinal imaging. Skevofilakas, et al. [26] developed a CDSS using data from 55 type І diabetic patients to predict the risk of diabetic retinopathy. They applied classi cation-based Rule Induction with C5.0,

Hybrid Wavelet Neural Network (HWNN), Classification and Regression Tree (CART), and neural network, and merged their results using a voting mechanism. In another work, Balakrishnan, et al. [27] used data from 140 diabetic patients in Malaysia to build a diabetic retinopathy predictive system, which employed a voting mechanism to select the final outcome from the results of decision tree and case-based reasoning (CBR). Although these two research projects did not use any retinal images to predict the risk of diabetic retinopathy, they are limited in a number of ways. First, they are based on small samples (55 in the first and 140 patients in the second study). Second, they consider a limited number of risk factors. These charactreistics not only contribute to lack of a comprehensive image of the patients' health status, but also make the final results less generalizable. Additionally, while according to the NIH statistics, 95% of the diabetics are type ІІ, the first study has only focused on type I diabetic patients. Research shows between 74.9% to 82.3% of type I diabetics have retinopathy [28]. Therefore, the baseline model for predicting retinopathy among type I diabetics will have an accuracy of about 80%. Moreover, almost all type І patients who have had the disease for 20 years develop this vision complication. Thus, despite the first study's high accuracy (98%) in predicting retinopathy among type I diabetic patients, it does not address the more important problem of detecting retinopathy in type II diabetics. This limitation is addressed in the second study, but with an overall accuracy of 85%, it leaves room for improvement. Therefore, another promise of the current effort is to develop a model that addresses the limitations of the extant literature, while improving upon their results.

Use of ensemble models in several studies in the literature, including the two studies that used lab and demographic data to predict diabetic retinopathy, points out to the complexity of this problem domain. Ensemble models have the benefit of being more robust than single models [29], and therefore, improve prediction accuracy. For this reason, we too employ an ensemble modeling approach in developing our CDSS. Specifically, we develop a heterogeneous confidence margin ensemble and illustrate how it outperforms the existing ensemble techniques. Due to our focus, therefore, it is important to have a brief review of the existing literature on ensemble models.

Ensemble models for supervised learning were first introduced by Tukey [30] and have since been studied by many researchers. At a high level, there are two categories of ensemble models: homogeneous and heterogeneous ensembles. Homogeneous ensembles combine multiple variations of a single classifier technique. Ensembles in this category use such algorithms as Bagging and AdaBoost to manipulate the training dataset and to develop multiple training datasets. These training datasets will be used by a data mining technique such as decision tree, and at the end, a voting or averaging mechanism will be used to make the final prediction using the outputs of single classifiers [31]. One of the most famous ensemble models in this category is random forest. Heterogeneous ensembles, on the other hand, combine various single classifiers (that are built using different data mining techniques) on the same training dataset. Simple average, weighted average, and voting based ensembles belong to this category [32].

A different type of ensemble models incorporates extra information into the predictive components to achieve higher accuracy. For instance, Li et al. [33] added web-based information from highly relevant search engine queries into their prediction framework and were able to predict the employment rate more accurately than such classical prediction methods as time series. Wang et al. [34] assessed three popular ensemble methods for sentiment classification and showed the benefits of ensemble techniques in sentiment classification. There are numerous other approaches to developing ensemble models. A comprehensive review of these techniques can be found in Rokach [35].

## 3. Methodology

It is often said that in any comprehensive data analytics study, N80% of the total project time is spent for data cleaning and preprocessing.

This is even more important in healthcare analytics, especially when real-world EMR data is involved—because the data are captured and stored in different clinical/hospital settings and for reasons other than data analytics [36]. Hence, in this study, data preparation was taken very seriously.

## 3.1. Data preprocessing

The data used for this research was obtained from the Cerner Corporation's Health Facts data warehouse; a comprehensive, relational repository of real-world, de-identified, and HIPAA-compliant patient data. Cerner Health Facts data warehouse includes pharmacy, laboratory, clinical, admission, and billing data, all linked through unique identifiers. This data warehouse is one of the largest commercial clinical data repositories in the United States. At the time of this study, Health Facts contained data from N58 million unique patients, about 84 million patient visits, over 320 million prescriptions, and about 2.4 billion clinical lab results that were collected since 2000 from 480 affiliated hospitals and hospital systems across the nation. A simplified conceptual data diagram of the Cerner Health Facts data warehouse is presented in Fig. 1.

Processing and analyzing large EMR datasets involves various challenges. Jagadish, et al. [37] classify these challenges into five categories: data acquisition; information extraction and cleaning; data integration, aggregation, and representation; modeling and analysis; and interpretation. Regarding the large number of variables in the data warehouse, we spent a significant amount of time to understand the purpose and relevance of each variable. An even more demanding step in preparing the dataset for final analysis was aggregrating the records at the patient level and integrating patients' comorbid conditions. Hence, information extraction and cleaning, together with data integration, aggregation, and representation constituted the majority of our data preprocessing efforts.

The nature of EMR data posed yet another difficulty to this study. Because EMR data is collected for purposes other than performing data analytics, it suffers from mutiple defficiencies. First, since EMR data is collected from several facilities around the country, it lacks integrity and consistency. For instance, different units or even naming might be used in different hospitals. Second, data missingness or incompleteness, which are endemic in EMR data, need to be addressed. And third, outliers and other data entry errors are prevalent in EMR data. We describe the approach we used in the data preparation step to address these challenges later in this section.

For the purpose of this research, we extracted data of N1.4 million unique diabetic patients from approximately 5.3 million visits. Since the number of variables collected from different data tables was rather

![](/api/attachments/B6JGVWCA/fulltext/images/a51ed86cea0ed3b7a1fb9803789761ad6d1551c8bb1750b63cb8d7521eae4267.jpg)  
Fig. 1. A simpli ed conceptual data model for Cerner Health Facts data warehouse.

Please cite this article as: S. Piri, et al., A data analytics approach to building a clinical decision support system for diabetic retinopathy: Developing and deploying a mode..., Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.05.012

S. Piri et al. / Decision Support Systems xxx (2017) xxx–xxx

large (300+), we needed to take many data selection, aggregation, and preparation steps.

First, data from all tables (e.g., encounter, patient, lab procedure, clinical event, etc.) for diabetes diagnosis and all associated complications, such as diabetic neuropathy, nephropathy, and retinopathy, were extracted. The table that included the lab procedure data was very important in this regard. The first dataset extracted from this table for diabetic patients included N800 different lab procedures. This primary dataset was very sparse, since not every patient had all of these lab results. We dropped those lab procedures that lacked sufficient results in the data. After taking several data cleaning steps, 88 lab procedures remained. Because EMR data are collected from hundreds of facilities across the United States, different names may be used for the same lab procedures. We consulted with clinical experts and merged identical lab procedures into one variable. As a result of this step, 58 lab procedures remained in our dataset.

The lab procedure table contained a column labeled “lab\_procedure\_name” that included all lab procedures for individual visits (encounters). We transposed this table so that each lab procedure had its own column. This increased the number of columns in the lab procedure table from 35 to about 100. Since every patient at each visit (hospital stay) could have multiple results for the same lab procedure, we retained the last result as consultations with physicians and clinical experts suggested these values could be considered the stable condition for a patient. Moreover, because our focus was on developing a CDSS for the early detection of retinopathy, we selected each patient's first chronological visit to increase the validity and generalizability of our findings.

In the next step, we used table keys (i.e., “Patient\_ID,” “Encounter\_ID,” and “Diagnosis\_ID”) to join data from multiple tables into a single table that included lab results, demographic data, and diagnosis data, with each record representing an individual diabetic patient. The resulting table included data from over 300,000 unique patients. Fig. 2 depicts different data preparation steps in our study.

![](/api/attachments/B6JGVWCA/fulltext/images/0db1d71c619191b5a6ee7cbed9e587f8bd680c0624cb427beda0bb32cbc71129.jpg)  
Fig. 2. Data preparation steps.

## 3.2. Modeling procedure

To develop the predictive models, we employed logistic regression, decision tree, random forest, and artificial neural networks. Building each of these models was preceded by various data manipulation steps, including transforming variables to approximate a normal distribution, replacing and filtering extreme data points, and applying different imputation methods, and at the end, we compared the results. The modeling procedure is shown in Fig. 3.

The target variable was a binary variable, where 0 denoted no diabetic retinopathy diagnosis and 1 denoted diabetic retinopathy diagnosis. Diabetic patients without a retinopathy diagnosis were included as the control group. The final dataset was largely imbalanced. In fact, we may face imbalanced data in several real world problems: fraud detection, oil-spill de tection, and medical applications (Kubat, et al. [38], Rao, et al. [39], Chan, et al. [40]). The majority class in the dataset was diabetic patients without retinopathy (95%), and our class of interest, diabetics with retinopathy (5%), was the minority class. The main challenge in analyzing imbalanced datasets is that the performance of most standard machine learning techniques will be poor in terms of identifying the target variable [41]. Therefore, a balanced dataset is necessary to develop predictive models with high accuracy. Since there were a reasonable number of retinopathy patients in the minority class (about 15,000 patients), we created a balanced dataset by randomly under-sampling the majority class. The next step was to partition the data into training and validation datasets to objectively assess the different model types. In the following section, we provide a brief description of each of the modeling techniques used in this study.

## 3.3. Modeling techniques

## 3.3.1. Logistic regression

Logistic regression is a classic statistical model. This method is capable of predicting and classifying categorical variables, but is mostly used

![](/api/attachments/B6JGVWCA/fulltext/images/6494dcebdafab58b17f0beb3309737f8043cac0de0a6c4c6c1f4e00166114a77.jpg)  
Fig. 3. Modeling procedure.

Please cite this article as: S. Piri, et al., A data analytics approach to building a clinical decision support system for diabetic retinopathy: Developing and deploying a mode..., Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.05.012

S. Piri et al. / Decision Support Systems xxx (2017) xxx–xxx

for binary variables [42]. It is an extended version of linear regression, but instead of modeling a continuous value, binary logistic regression models the log odds of the probability of an event, as opposed to its occurrence, as a linear function of the predictors.

Selection methods are often used to construct an optimal regression equation using a large number of predictors. Three statistical regression methods of variable selection are forward selection, backward elimination, and stepwise selection. The training in forward selection starts with an empty equation and adds predictors one at a time starting with the most significant predictor. Selection ends when all remaining predictors fail to meet the specified F-to-enter value. Backward elimination training starts with all predictors and removes, one at a time, the least significant predictors. Elimination ends when all remaining predictors fail to meet the specified F-to-remove value. The stepwise method is a variation of the above methods. It starts with an empty model, and after each step in which a predictor is added based on the F-toenter value, it evaluates predictors in the model against the specified significance level. Those that fall below this level are removed. In this study, we applied the stepwise method. The binary logistic regression equation is shown in Eq. (1) and Eq. (2).

$$
\operatorname{logit} [ P (x) ] = \ln \left[ \frac {P (x)}{1 - P (x)} \right] = \beta_ {0} + \beta_ {1} x _ {1} + \dots + \beta_ {n} x _ {n}\tag{1}
$$

$$
P (x) = \frac {e ^ {\beta_ {0} + \beta_ {1} x _ {1} + \dots + \beta_ {n} x _ {n}}}{1 + e ^ {\beta_ {0} + \beta_ {1} x _ {1} + \dots + \beta_ {n} x _ {n}}} = \frac {1}{1 + e ^ {- l o g i t [ p (x) ]}}\tag{2}
$$

P(x) is the probability that the target variable belongs to a specific category (in our study, a patient has retinopathy) and $\beta _ { i }$ is the coefficient of the ith predictor.

## 3.3.2. Artificial neural network

Artificial neural network (ANN) is a very popular model in healthcare analytics. ANN can be defined as “massively parallel processors, which tend to preserve experimental knowledge and enable their further use” [43]. One of the advantages of the neural network model is its ability in handling highly complex problem structures with nonlinear relationships among variables. A limitation of this method, however, is its high sensitivity to model parameters (i.e., structure/architecture of the model, learning rate, number of layers and neurons in each layer, etc.) [44]. Fig. 4 exhibits a simple two-layer perceptron network. In this example, there are three inputs and two neurons in the hidden layer. There is a transfer function for the output layer and for each neuron in the hidden layer. In this study, we used two-layer perceptron networks with hyperbolic tangent transfer functions in the hidden layer and a soft-max transfer function in the output layer (see Eq. (3), Eq. (4), and Eq. (5)). We also used the conjugate-gradient optimization technique to optimize the network. For more details about the neural networks design, we refer the readers to Hagan, et al. [45].

![](/api/attachments/B6JGVWCA/fulltext/images/52986f631a3011aabb0247d34d620faae01a304d43a78d2eb8b43baa51bd18c0.jpg)  
Fig. 4. Two-layer perceptron neural network.

$$
a _ {1} = f _ {1} (w _ {1 1} x _ {1} + w _ {2 1} x _ {2} + w _ {3 1} x _ {3} + b _ {1})\tag{3}
$$

$$
a _ {2} = f _ {2} (w _ {1 2} x _ {1} + w _ {2 2} x _ {2} + w _ {3 2} x _ {3} + b _ {2})\tag{4}
$$

$$
y = f (w _ {1} a _ {1} + w _ {2} a _ {2} + b)\tag{5}
$$

In these equations, $x _ { 1 } , x _ { 2 }$ and $x _ { 3 }$ are input variables; $w _ { i j }$ is the weight of the input i for neuron $j ; b _ { j }$ and a<sub>j</sub> are the bias and output of neuron j respectively; f and $f _ { 2 }$ are the transfer functions for the hidden layer; f is the transfer function of the output layer; and y is the output of the network. In this study, we developed neural network models in two settings. In the first setting, we fed all of the variables into the neural network models, but in the second setting, we only used the variables that were selected through the stepwise method in logistic regression.

## 3.3.3. Decision tree

Decision tree is a method that recursively partitions the data based on a predictor [46]. The training process in this method starts at the root node (i.e., all the records and predictors). The tree is built by splitting the records at each stage (i.e., each node) according to the best cutoff value of a predictor. There are several criteria to select the best split. In this study, we used Pearson's $\chi ^ { 2 }$ p-value and the Gini index. Pearson's $\chi ^ { 2 } p \cdot$ -value measures the level of separation achieved by the split. To calculate this measure, consider a 2×2 contingency table for the split. Columns represent the branch directions and rows specify the target variable (0 or 1). The $\chi ^ { 2 }$ value is calculated as in Eq. (6).

$$
\chi^ {2} = \sum_ {i = 1} ^ {2} \sum_ {j = 1} ^ {2} \frac {\left(O _ {i j} - E _ {i j}\right) ^ {2}}{E _ {i j}}\tag{6}
$$

In this equation $O _ { i j }$ is the observed frequency in row i and column j, and $E _ { i j }$ is the expected frequency in row i and column j. The p-value of the $\chi ^ { 2 }$ is then calculated. The smaller the p-value, the better the split or the higher the level of separation.

The Gini index shows the level of purity achieved by the split. Gini is the probability that two randomly selected members of a population are the same. For a pure population, this index would be 1. The calculation of the Gini index in each leaf of a split is as in Eq. (7), wher $: p _ { 1 }$ and $p _ { 2 }$ are the proportions of each level.

$$
G i n i = p _ {1} ^ {2} + p _ {2} ^ {2}\tag{7}
$$

Then, the Gini score of the split is calculated as in Eq. (8), where $w _ { l e f t }$ and $w _ { r i g h t }$ are the proportion of the records in each leaf.

$$
G i n i _ {s c o r e} = w _ {l e f t} G i n i _ {l e f t} + w _ {r i g h t} G i n i _ {r i g h}\tag{8}
$$

The higher the Gini score, the higher the level of purity achieved by the split. Although the decision tree method is easy to understand, especially for those without knowledge of theories underlying data mining methods, one of its major drawbacks is that data partitioning may result in one leaf comprised of few data points, precluding any useful information from that portion of the data [44].

## 3.3.4. Random Forest

Random forest could be considered an extension of decision tree. This method develops multiple smaller trees that classify each member of the sample data. The final predicted class for a particular sample member is determined using a voting mechanism based on the prediction of all trees [47]. Each tree in the random forest uses a subset of records and variables. Random sampling with replacement is used for building each tree. In this study, after examining several scenarios developed by altering model characteristics, we used 60% of the training

Please cite this article as: S. Piri, et al., A data analytics approach to building a clinical decision support system for diabetic retinopathy: Developing and deploying a mode..., Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.05.012

![](/api/attachments/B6JGVWCA/fulltext/images/5e0091b91c376d78c1d7a6d0d07fa0f297fe9ffe5aa5f3fd38500b962c6627b1.jpg)  
Fig. 5. Predictive model sets.

data and the square root of the number of variables to build each tree. Several advantages can be enumerated for random forest. Besides high accuracy, this method provides a variable importance metric that can be used for identifying important risk factors. Random forest can also handle datasets with a large number of variables [48].

## 3.4. Predictive model sets

In this research, four different sets of predictive models were developed (see Fig. 5). The first set, called the basic models, encompassed models that were developed using lab procedures and demographic data of diabetic patients. In the second set, models were built on lab procedures, demographics, and comorbidity data. These models are called comorbid models. The third set, dubbed over-sampled models, consisted of models built using the over-sampled data by applying the synthetic minority over-sampling technique (SMOTE). And, the fourth set included ensemble models that were developed based on the outputs of individual classifiers.

## 3.4.1. Basic models

In this set of models, we used the data compiled during the data preparation phase. We call this dataset “basic data” as it only included demographic and lab results of the diabetic patients.

## 3.4.2. Models based on comorbid data

The second set of predictive models was based on the comorbidity information. To develop these models, comorbidity data were added to the basic data through several data preparation steps. In recent years, the effects of co-existing conditions in the study of different diseases has received considerable attention. Researchers have shown the benefits of considering comorbidities in the diagnosis and treatment of diseases (Albertsen, et al. [49], Hanchate, et al. [50], Hill, et al. [51], and Teppo and Alho [52]).

In these models, we considered the existence of other diabetesrelated complications to predict diabetic retinopathy. The following complications were included in our analyses: neuropathy, nephropathy, peripheral circularity, hyperosmolarity, diabetes-related coma, and other specified diabetes-related conditions. To prepare the comorbid dataset, we performed several steps on the primary data table, which consisted of the list of patients, their complication (diagnosis code), and their demographic and lab data. Since each complication of a patient generated a different record in the database, we extracted all records in which the diagnosis was one of the aforementioned complications and saved them in separate tables. Next, we merged these tables by patient ID and added a binary variable for each complication. Therefore, for each patient, in addition to the demographic and lab data, we added information about their other co-existing complications. After taking these steps, the dataset became ready for the development of the predictive models.

3.4.3. Models based on over-sampled data

In the previous two sets of models, we carried out random undersampling for the majority class to create a balanced dataset. One obvious limitation of under-sampling is the possibility of losing important information about the majority class by removing some fractions of the data [53]. The other available approach to create a balanced dataset is to over-sample the minority class. Numerous over-sampling methods have been proposed in recent years, and among them synthetic data generation for the minority class has one of the best performances. By generating synthetic data, new examples of the minority class are generated using different techniques to reach some desired degree of balanced class distribution. SMOTE [54] is one of the most famous methods in this regard. In this method, synthetic data points are generated on the line joining each minority sample and any/all of its k minority class nearest neighbors (minority class with the smallest Euclidean distance from the original sample). Consider x a minority class, and x one of its k minority class nearest neighbors. The new data will be generated as in Eq. (9),

$$
x _ {n e w} = (1 - \delta) x + \delta x _ {i}\tag{9}
$$

where δ is a random number between [0,1]. Fig. 6 depicts the synthetic data generation process.

The number of k nearest neighbors to be used depends on the amount of over-sampling required. For instance, if we want to increase the minority class by 300%, k would be equal to 3. We can enumerate several advantages for this method. First, it requires no information other than the dataset itself [55]. Further, since it is a preprocessing method, over-sampled data can be used in any classification technique with good performance on balanced data [56]. Finally, by generating synthetic minority data, as opposed to simply replicating existing minority data, the minority region can be generalized and overfitting, a limitation of replication, can be avoided [57].

![](/api/attachments/B6JGVWCA/fulltext/images/ba392511d771cc6452cc7bfe872083f3962f41866205b5a2b541203d07be47d9.jpg)  
Fig. 6. Synthetic minority over-sampling technique (SMOTE).

Table 1 Demographic variables.

<table><tr><td>Name</td><td>No. of levels</td><td>Levels</td><td>Mode</td></tr><tr><td>Gender</td><td>3</td><td>Female/male/unknown</td><td>Female</td></tr><tr><td>Race</td><td>8</td><td>Caucasian/African American/Hispanic/Asian/Native American/Pacific Islander/unknown/null</td><td>Caucasian</td></tr><tr><td>Marital status</td><td>7</td><td>Married/single/widowed/legally separated/life partner/null</td><td>Married</td></tr><tr><td>Urban rural status</td><td>2</td><td>Urban (99%)/rural (1%)</td><td>Urban</td></tr></table>

In this study, we considered 5 neighbors to increase the size of the minority class by 10 times, which means we generated two synthetic data points on each line connecting the minority class and each of its five nearest neighbors. Rather than over-sampling the minority class up to the level of the majority class, we increased the size of the minority class to some extent and then under-sampled the majority class to reach a balanced dataset, which is consistent with Chawla, et al. [54] study that showed the combination of SMOTE and under-sampling of the majority class has a better result compared to plain undersampling. For simplicity, from this point to the end of the paper, we call models in Set 1 “basic models”, models in Set 2 “comorbid models”, and models in Set 3 “over-sampled models”.

## 3.4.4. Ensemble models

The ensemble models for this study were developed using five approaches: simple average, weighted average, voting-based, random forest, and confidence margin. The first four approaches already exist in the literature, but the last approach (i.e., the confidence margin), was developed in this study. We explained the random forest model in Section 3.3. A description of other approaches is presented next.

3.4.4.1. Simple average ensemble models. In this method, each model contributes an equally weighted output to compute an average. For instance, if there are 5 single models A,B,C,D and E with outputs of 0.66,0.45,0.76,0.92, and 0.48 for a record, the average output would be 0.654. The final classification decision would be YES, even though two of the single models would classify the record as NO (assuming that the decision cut-off is set at 0.50).

3.4.4.2. Weighted average ensemble models. Rather than assuming all classifiers contribute equally, this method assigns different weights to single classifier outputs for calculating the final result. The weight of each single classifier corresponds to its accuracy. Again, suppose there are 5 single models A,B,C,D and E. The weights will be determined as in Eq. (10).

$$
W ^ {A} = \frac {\text { Accuracy } ^ {A}}{\text { Accuracy } ^ {A} + \text { Accuracy } ^ {B} + \text { Accuracy } ^ {C} + \text { Accuracy } ^ {D} + \text { Accuracy } ^ {E}} (1 0)
$$

So, the more accurate a model, the greater weight the model will have in calculating the weighted average. The final prediction for a record can be calculated as in Eq. (11).

$$
P = W ^ {A} P ^ {A} + W ^ {B} P ^ {B} + W ^ {C} P ^ {C} + W ^ {D} P ^ {D} + W ^ {E} P ^ {E}\tag{11}
$$

3.4.4.3. Confidence margin ensemble models. To build these ensemble models, we define a metric, named confidence margin (c\_m). Confidence margin is calculated for each record predicted by each single model. The cut-off point to make the decision is considered to be 0.5, hence the confidence margin for record i, predicted by model A is

## Table 2

Lab procedure variables.

<table><tr><td>Name</td><td>Description</td><td>Mean</td><td>StDev</td><td>Skewness</td><td>Kurtosis</td><td>Missing (%)</td></tr><tr><td>Alanine Aminotransferase (ALT)</td><td>This test assesses the level of ALT enzyme in the blood.</td><td>31.14</td><td>31.66</td><td>5.814</td><td>46.38</td><td>0.49</td></tr><tr><td>Albumin serum</td><td>This test measures the level of albumin in the blood.</td><td>3.11</td><td>0.80</td><td>3.673</td><td>135.16</td><td>0.47</td></tr><tr><td>Anion gap (blood)</td><td>This test evaluates the electrically charged particles such as sodium, chloride, and bicarbonate in the blood.</td><td>9.61</td><td>3.68</td><td>0.868</td><td>3.49</td><td>0.39</td></tr><tr><td>Aspartate aminotransferase (AST)</td><td>This test measures the level of AST enzyme in the blood. AST test usually ordered with ALT.</td><td>28.49</td><td>26.03</td><td>5.174</td><td>34.73</td><td>0.44</td></tr><tr><td>Blood urea nitrogen (BUN)</td><td>BUN measures the amount of nitrogen in the blood that comes from urea. This test evaluates the functionality of kidneys and liver.</td><td>20.70</td><td>14.59</td><td>2.786</td><td>11.94</td><td>0.22</td></tr><tr><td>Calcium serum</td><td>This test evaluates the amount of the calcium in the blood.</td><td>8.48</td><td>1.11</td><td>-3.501</td><td>18.86</td><td>0.26</td></tr><tr><td>Chloride serum</td><td>This test helps detecting the abnormal amounts of chloride in the blood.</td><td>102.52</td><td>4.66</td><td>-1.47</td><td>30.47</td><td>0.21</td></tr><tr><td>Creatinine Serum</td><td>This test evaluates kidney function. Creatinine is a waste product of muscle metabolism and eating meat.</td><td>0.77</td><td>1.20</td><td>4.088</td><td>22.67</td><td>0.20</td></tr><tr><td>Glucose serum plasma</td><td>This test assesses the blood glucose level, a major test to screen for pre-diabetes and diabetes.</td><td>155.19</td><td>80.50</td><td>2.39</td><td>10.47</td><td>0.29</td></tr><tr><td>Hematocrit</td><td>This test measures the percentage of red blood cells in the blood.</td><td>35.27</td><td>9.09</td><td>-2.104</td><td>6.32</td><td>0.30</td></tr><tr><td>Hemoglobin</td><td>This test measures the amount of hemoglobin in the blood.</td><td>12.27</td><td>4.45</td><td>15.217</td><td>297.57</td><td>0.28</td></tr><tr><td>Mean corpuscular hemoglobin concentration (MCHC)</td><td>MCH measures the average concentration of hemoglobin per red blood cell.</td><td>33.23</td><td>1.39</td><td>-5.627</td><td>163.68</td><td>0.34</td></tr><tr><td>Mean platelet volume (MPV)</td><td>MPV is automated measurement of average size of platelets in the blood.</td><td>8.38</td><td>1.52</td><td>0.238</td><td>3.60</td><td>0.43</td></tr><tr><td>Potassium serum</td><td>This test measures the level of potassium in the blood.</td><td>3.76</td><td>0.61</td><td>-0.003</td><td>2.55</td><td>0.20</td></tr><tr><td>Protein total serum</td><td>This test evaluates the amounts of albumin and globulin proteins in the blood.</td><td>6.13</td><td>1.16</td><td>-2.199</td><td>9.96</td><td>0.50</td></tr><tr><td>Red blood cell (RBC) count</td><td>RBC measures the number of red blood cells in the blood and usually is ordered as a part of a complete blood cell (CBC) test.</td><td>3.72</td><td>1.31</td><td>21.354</td><td>725.58</td><td>0.36</td></tr><tr><td>Sodium serum</td><td>This test assesses the level of sodium and detects abnormal low/high sodium in the blood.</td><td>138.03</td><td>3.95</td><td>-6.576</td><td>226.32</td><td>0.22</td></tr><tr><td>White blood cell (WBC) count</td><td>This test determines the number of WBC in the blood and helps to diagnose infections and other medical conditions.</td><td>8.16</td><td>4.77</td><td>11.475</td><td>281.13</td><td>0.30</td></tr></table>

Please cite this article as: S. Piri, et al., A data analytics approach to building a clinical decision support system for diabetic retinopathy: Developing and deploying a mode..., Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.05.012

Table 3 Comorbidity variables.

<table><tr><td>Name</td><td>Description</td></tr><tr><td>Neuropathy</td><td>Type of nerve disorder; particularly prevalent in the feet and legs.</td></tr><tr><td>Nephropathy</td><td>Kidney disease</td></tr><tr><td>Peripheral Circulatory</td><td>Arterial blockage due to atherosclerosis; mostly affects lower extremities.</td></tr><tr><td>Ketoacidosis</td><td>High levels of ketone bodies, or blood acids, resulting from the breaking down of fat rather than glucose for energy; may lead to coma.</td></tr><tr><td>Hyperosmolarity</td><td>Extremely high blood sugar level in which excess blood sugar is passed into the urine; may lead to life-threatening dehydration.</td></tr><tr><td>Other Complications</td><td>Other specified complications of diabetes are in this category</td></tr></table>

defined as in Eq. (12).

$$
c \_ m _ {i} ^ {A} = \left\{ \begin{array}{l l} P _ {i} ^ {A} - 0. 5 & \text { if } P _ {i} ^ {A} > 0. 5 \\ 0. 5 - P _ {i} ^ {A} & \text { if } P _ {i} ^ {A} \leq 0. 5 \end{array} \right.\tag{12}
$$

where $P _ { i } ^ { 4 }$ is the prediction output of model A for record i.

Therefore, we say a model is more confident in predicting a record (or the confidence margin is greater) when its prediction is farther away from the cut-off. Final predictions are obtained after calculating confidence margins for all records in all models. Similar to the two previous ensemble models, the average of the single models' predictions is calculated, but different weights are used at both model and record levels. The weight of the prediction for record i by model A is calculated as in Eq. 13.

$$
W _ {i} ^ {A} = \frac {c _ {-} m _ {i} ^ {A}}{c _ {-} m _ {i} ^ {A} + c _ {-} m _ {i} ^ {B} + c _ {-} m _ {i} ^ {C} + c _ {-} m _ {i} ^ {D} + c _ {-} m _ {i} ^ {E}}\tag{13}
$$

Therefore, the final prediction for record i can be calculated as in Eq. (14).

$$
P _ {i} = W _ {i} ^ {A} P _ {i} ^ {A} + W _ {i} ^ {B} P _ {i} ^ {B} + W _ {i} ^ {C} P _ {i} ^ {C} + W _ {i} ^ {D} P _ {i} ^ {D} + W _ {i} ^ {E} P _ {i} ^ {E}\tag{14}
$$

3.4.4.4. Voting-based ensemble models. In these models, a voting procedure is utilized to make the final decision. When the number of single models is odd, the final decision is the majority vote. But when the number of single models is even, in case of equal votes between two classes, the final decision is made by comparing the sum of confidence margins for models that voted YES to the sum of confidence margins for models that voted NO (see Eq. (15)).

Set 1 - basic models' results.

<table><tr><td>Data manipulation</td><td>Imputation technique</td><td>Modeling technique</td><td>AUC</td><td>Accuracy</td><td>Sensitivity</td><td>Specificity</td></tr><tr><td rowspan="15">No manipulation</td><td rowspan="3">No imputation</td><td>DT-Gini</td><td>77.30%</td><td>70.76%</td><td>63.95%</td><td>77.56%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>77.30%</td><td>70.71%</td><td>65.04%</td><td>76.38%</td></tr><tr><td> $RF^a$ </td><td>81.80%</td><td>73.78%</td><td>72.37%</td><td>75.19%</td></tr><tr><td rowspan="6">Mean</td><td>DT-Gini</td><td>76.30%</td><td>70.98%</td><td>65.50%</td><td>76.47%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>75.60%</td><td>71.12%</td><td>59.76%</td><td>82.48%</td></tr><tr><td>RF</td><td>79.20%</td><td>71.87%</td><td>67.46%</td><td>76.29%</td></tr><tr><td>LR</td><td>78.00%</td><td>71.26%</td><td>63.27%</td><td>79.24%</td></tr><tr><td>ANN</td><td>79.40%</td><td>72.96%</td><td>69.69%</td><td>76.24%</td></tr><tr><td> $ANN-Reg^b$ </td><td>79.80%</td><td>72.28%</td><td>67.64%</td><td>76.92%</td></tr><tr><td rowspan="6">Tree</td><td>DT-Gini</td><td>75.20%</td><td>70.25%</td><td>56.62%</td><td>83.89%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>75.30%</td><td>70.41%</td><td>60.13%</td><td>80.70%</td></tr><tr><td> $RF^c$ </td><td>79.80%</td><td>72.33%</td><td>67.50%</td><td>77.15%</td></tr><tr><td>LR</td><td>78.00%</td><td>71.92%</td><td>65.50%</td><td>78.33%</td></tr><tr><td>ANN</td><td>79.60%</td><td>72.67%</td><td>70.82%</td><td>74.51%</td></tr><tr><td> $ANN-Reg^b$ </td><td>80.00%</td><td>72.99%</td><td>68.50%</td><td>77.47%</td></tr><tr><td rowspan="15">Extreme point replacement</td><td rowspan="3">No imputation</td><td>DT-Gini</td><td>77.30%</td><td>70.76%</td><td>63.95%</td><td>77.56%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>77.30%</td><td>70.71%</td><td>65.04%</td><td>76.38%</td></tr><tr><td> $RF^a$ </td><td>81.90%</td><td>73.78%</td><td>71.01%</td><td>76.56%</td></tr><tr><td rowspan="6">Mean</td><td>DT-Gini</td><td>76.40%</td><td>71.01%</td><td>65.91%</td><td>76.10%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>76.00%</td><td>71.10%</td><td>60.17%</td><td>82.02%</td></tr><tr><td>RF</td><td>79.20%</td><td>72.05%</td><td>67.14%</td><td>76.97%</td></tr><tr><td>LR</td><td>76.70%</td><td>69.71%</td><td>59.76%</td><td>79.65%</td></tr><tr><td>ANN</td><td>78.50%</td><td>72.01%</td><td>66.36%</td><td>77.65%</td></tr><tr><td>ANN-Reg</td><td>78.30%</td><td>72.14%</td><td>63.40%</td><td>80.88%</td></tr><tr><td rowspan="6">Tree</td><td>DT-Gini</td><td>75.10%</td><td>70.35%</td><td>56.26%</td><td>84.53%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>76.20%</td><td>70.89%</td><td>60.63%</td><td>81.16%</td></tr><tr><td>RF</td><td>79.30%</td><td>71.94%</td><td>66.32%</td><td>77.56%</td></tr><tr><td>LR</td><td>77.80%</td><td>71.48%</td><td>63.68%</td><td>79.29%</td></tr><tr><td> $ANN^b$ </td><td>80.00%</td><td>73.26%</td><td>67.96%</td><td>78.56%</td></tr><tr><td>ANN-Reg</td><td>79.40%</td><td>72.30%</td><td>67.73%</td><td>76.88%</td></tr><tr><td rowspan="15">Max normal variable transformation</td><td rowspan="3">No imputation</td><td>DT-Gini</td><td>77.20%</td><td>70.69%</td><td>64.00%</td><td>77.38%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>77.30%</td><td>70.71%</td><td>65.04%</td><td>76.38%</td></tr><tr><td> $RF^a$ </td><td>81.50%</td><td>73.33%</td><td>69.64%</td><td>77.01%</td></tr><tr><td rowspan="6">Mean</td><td>DT-Gini</td><td>76.60%</td><td>71.01%</td><td>62.72%</td><td>79.29%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>75.60%</td><td>71.17%</td><td>60.67%</td><td>81.66%</td></tr><tr><td> $RF^c$ </td><td>79.70%</td><td>72.05%</td><td>67.46%</td><td>76.65%</td></tr><tr><td>LR</td><td>78.10%</td><td>71.69%</td><td>66.77%</td><td>76.60%</td></tr><tr><td>ANN</td><td>79.60%</td><td>72.60%</td><td>68.37%</td><td>76.83%</td></tr><tr><td>ANN-Reg</td><td>79.30%</td><td>72.23%</td><td>66.95%</td><td>77.51%</td></tr><tr><td rowspan="6">Tree</td><td>DT-Gini</td><td>75.30%</td><td>70.69%</td><td>61.00%</td><td>80.38%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>76.60%</td><td>70.91%</td><td>61.77%</td><td>80.06%</td></tr><tr><td>RF</td><td>79.50%</td><td>71.71%</td><td>66.50%</td><td>76.92%</td></tr><tr><td>LR</td><td>78.20%</td><td>71.55%</td><td>67.60%</td><td>75.51%</td></tr><tr><td> $ANN^c$ </td><td>79.70%</td><td>72.78%</td><td>68.32%</td><td>77.24%</td></tr><tr><td>ANN-Reg</td><td>79.40%</td><td>72.46%</td><td>68.55%</td><td>76.38%</td></tr></table>

$$
\left\{\begin{array}{l l}i f \sum_ {j ^ {+} \in \text { Modles   which   voted   YES }} c _ {-} m _ {i} ^ {j ^ {+}} > \sum_ {j ^ {-} \in \text { Modles   which   voted   NO }} c _ {-} m _ {i} ^ {j ^ {-}}&- \rightarrow Y E S\\i f \sum_ {j ^ {+} \in \text { Modles   which   voted   YES }} c _ {-} m _ {i} ^ {j ^ {+}} \leq \sum_ {j ^ {-} \in \text { Modles   which   voted   NO }} c _ {-} m _ {i} ^ {j ^ {-}}&- \rightarrow N O\end{array}\right.\tag{15}
$$

## 3.5. Variable importance evaluation

One of the major benefits of analytics and data mining in healthcare is the identification of factors that have strong predictive power in detecting a disease. In this section, we elucidate the procedure used to evaluate the predictive power of different independent variables (predictors). To assess the predictive power (variable importance) of a variable, we used the Gini impurity reduction metric in the random forest models. As was mentioned earlier in Section 3.3.4, random forest is a collection of multiple decision trees. Thus, to calculate the Gini impurity reduction for different variables in a random forest model, the average Gini impurity reduction for each variable in all decision trees needs to be computed. The calculation of the Gini purity index for a node in a decision tree was shown in Eq. (7); therefore, the Gini impurity index, which is showed by $G i n i _ { i m p } ,$ is calculated as in Eq. (16),

$$
G i n i _ {i m p} = 1 - G i n i = 1 - \left(p _ {1} ^ {2} + p _ {2} ^ {2}\right) = p _ {1} (1 - p _ {1}) + p _ {2} (1 - p _ {2})\tag{16}
$$

where $p _ { 1 }$ and $p _ { 2 }$ are the proportions of each level of the target variable at the node. If a variable is used for a split in a decision tree, the Gini impurity reduction (GIR) for that variable is calculated as in Eq. (17),

$$
G I R = G i n i _ {i m p _ {p a r e n t}} - w _ {l e f t} G i n i _ {i m p _ {l e f t}} - w _ {r i g h t} G i n i _ {i m p _ {r i g h t}}\tag{17}
$$

where w<sub>left</sub> and w<sub>right</sub> are the proportion of the records in each leaf. Now suppose T trees are generated in a random forest model; the GIR for a variable in that random forest will be given as in Eq. (18),

$$
G I R _ {R F} = \frac {\sum_ {t = 1} ^ {T} G I R _ {t}}{T}\tag{18}
$$

Table 5  
Set 2 - comorbid models' results.

<table><tr><td>Data manipulation</td><td>Imputation technique</td><td>Modeling technique</td><td>AUC</td><td>Accuracy</td><td>Sensitivity</td><td>Specificity</td></tr><tr><td rowspan="15">No manipulation</td><td rowspan="3">No imputation</td><td>DT-Gini</td><td>83.40%</td><td>78.65%</td><td>76.83%</td><td>80.47%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>83.60%</td><td>79.06%</td><td>78.88%</td><td>79.24%</td></tr><tr><td> $RF^a$ </td><td>88.40%</td><td>80.61%</td><td>75.97%</td><td>85.25%</td></tr><tr><td rowspan="6">Mean</td><td>DT-Gini</td><td>84.20%</td><td>79.38%</td><td>79.88%</td><td>78.88%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>83.80%</td><td>79.18%</td><td>78.88%</td><td>79.47%</td></tr><tr><td> $RF^b$ </td><td>87.50%</td><td>79.81%</td><td>74.37%</td><td>85.25%</td></tr><tr><td>LR</td><td>86.20%</td><td>79.09%</td><td>70.41%</td><td>87.76%</td></tr><tr><td>ANN</td><td>87.00%</td><td>80.29%</td><td>74.42%</td><td>86.16%</td></tr><tr><td>ANN-Reg</td><td>86.90%</td><td>79.97%</td><td>73.83%</td><td>86.12%</td></tr><tr><td rowspan="6">Tree</td><td>DT-Gini</td><td>83.30%</td><td>78.81%</td><td>72.14%</td><td>85.48%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>84.70%</td><td>78.77%</td><td>68.78%</td><td>88.76%</td></tr><tr><td> $RF^b$ </td><td>87.70%</td><td>80.18%</td><td>75.92%</td><td>84.43%</td></tr><tr><td>LR</td><td>86.50%</td><td>79.40%</td><td>71.19%</td><td>87.62%</td></tr><tr><td> $ANN^c$ </td><td>87.40%</td><td>80.13%</td><td>75.47%</td><td>84.80%</td></tr><tr><td> $ANN-Reg^b$ </td><td>87.40%</td><td>80.18%</td><td>75.24%</td><td>85.12%</td></tr><tr><td rowspan="15">Extreme point replacement</td><td rowspan="3">No imputation</td><td>DT-Gini</td><td>83.40%</td><td>78.65%</td><td>76.83%</td><td>80.47%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>83.60%</td><td>79.06%</td><td>78.88%</td><td>79.24%</td></tr><tr><td> $RF^a$ </td><td>88.60%</td><td>80.38%</td><td>74.60%</td><td>86.16%</td></tr><tr><td rowspan="6">Mean</td><td>DT-Gini</td><td>84.20%</td><td>79.38%</td><td>79.88%</td><td>78.88%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>83.80%</td><td>79.18%</td><td>78.88%</td><td>79.47%</td></tr><tr><td> $RF^c$ </td><td>87.40%</td><td>79.84%</td><td>74.28%</td><td>85.39%</td></tr><tr><td>LR</td><td>85.90%</td><td>78.88%</td><td>69.78%</td><td>87.98%</td></tr><tr><td>ANN</td><td>86.40%</td><td>80.13%</td><td>74.15%</td><td>86.12%</td></tr><tr><td>ANN-Reg</td><td>86.30%</td><td>79.72%</td><td>73.51%</td><td>85.94%</td></tr><tr><td rowspan="6">Tree</td><td>DT-Gini</td><td>84.20%</td><td>79.20%</td><td>74.51%</td><td>83.89%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>84.40%</td><td>79.22%</td><td>74.51%</td><td>83.93%</td></tr><tr><td>RF</td><td>87.40%</td><td>79.95%</td><td>74.37%</td><td>85.53%</td></tr><tr><td>LR</td><td>85.90%</td><td>79.13%</td><td>70.28%</td><td>87.98%</td></tr><tr><td>ANN</td><td>87.30%</td><td>79.97%</td><td>75.56%</td><td>84.39%</td></tr><tr><td>ANN-Reg</td><td>86.10%</td><td>79.77%</td><td>72.05%</td><td>87.48%</td></tr><tr><td rowspan="15">Max normal variable transformation</td><td rowspan="3">No imputation</td><td>DT-Gini</td><td>83.40%</td><td>78.70%</td><td>76.74%</td><td>80.66%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>83.60%</td><td>79.06%</td><td>78.88%</td><td>79.24%</td></tr><tr><td> $RF^a$ </td><td>88.50%</td><td>80.41%</td><td>74.74%</td><td>86.07%</td></tr><tr><td rowspan="6">Mean</td><td>DT-Gini</td><td>84.10%</td><td>79.27%</td><td>79.79%</td><td>78.74%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>83.80%</td><td>79.18%</td><td>78.88%</td><td>79.47%</td></tr><tr><td> $RF^c$ </td><td>87.40%</td><td>79.90%</td><td>73.78%</td><td>86.03%</td></tr><tr><td>LR</td><td>86.30%</td><td>79.49%</td><td>72.64%</td><td>86.35%</td></tr><tr><td>ANN</td><td>86.60%</td><td>79.72%</td><td>73.96%</td><td>85.48%</td></tr><tr><td>ANN-Reg</td><td>86.50%</td><td>79.63%</td><td>73.69%</td><td>85.57%</td></tr><tr><td rowspan="6">Tree</td><td>DT-Gini</td><td>84.30%</td><td>78.95%</td><td>71.83%</td><td>86.07%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>85.00%</td><td>79.20%</td><td>73.60%</td><td>84.80%</td></tr><tr><td>RF</td><td>87.40%</td><td>79.79%</td><td>73.46%</td><td>86.12%</td></tr><tr><td>LR</td><td>85.70%</td><td>79.34%</td><td>71.46%</td><td>87.21%</td></tr><tr><td>ANN</td><td>86.30%</td><td>79.40%</td><td>74.65%</td><td>84.16%</td></tr><tr><td>ANN-Reg</td><td>86.10%</td><td>79.70%</td><td>71.73%</td><td>87.67%</td></tr></table>

The higher the GIR of a variable in the random forest, the more important that variable is for detecting the target variable. Since we have developed several random forest models in different data preparation settings, we develop the final ranking of important variables by following this procedure: first GIR for all variables is calculated in all random forest models in Sets 2 and 3; then, GIRs are normalized in each random forest model; and finally, the average of normalized GIRs for each variable in different random forest models is computed to obtain the variable importance metric for that variable. Since any manipulation in the data could change the models' output and, hence, the variable importance ranking, we believe our procedure for creating the list of important variables is more robust and more reliable.

## 4. Results

## 4.1. Variable description

The independent variables (predictors) in our dataset can be divided into three categories: demographic, lab, and comorbidity variables. Tables 1, 2 and 3 provide a brief description of the variables (out of 68 variables in the data) that made it to the final models. Table 1 describes the four demographic variables: gender, race, marital status, and urban/ rural status. There were slightly more females than males. Most of the patients were Caucasian, followed by African Americans and Hispanics. N37% of the patients were married and others were single, widowed, or legally separated.

Table 2 provides some descriptive statistics for lab procedures. In this table, mean, standard deviation (SD), skewness, kurtosis, and the missing value percentage for each variable are presented. A brief description of the comorbidity variables (other diabetes-related complications) is provided in Table 3.

## 4.2. Models' outputs

The results of the different sets of models are presented in Tables 4, $5 ,$ and $6 ,$ which include area under the curve (AUC) of the receiver operating characteristic (ROC), accuracy, sensitivity, and specificity. As the results show, the accuracy, sensitivity, specificity, and AUC of the models improved from the basic to the comorbid, and from the comorbid to the over-sampled models. Finally, for each set of models, ensemble models outperformed single models.

Set 3 - over-sampled models' results.

<table><tr><td>Data manipulation</td><td>Imputation technique</td><td>Modeling technique</td><td>AUC</td><td>Accuracy</td><td>Sensitivity</td><td>Specificity</td></tr><tr><td rowspan="15">No manipulation</td><td rowspan="3">No imputation</td><td>DT-Gini</td><td>93.00%</td><td>89.13%</td><td>89.05%</td><td>89.20%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>93.00%</td><td>89.14%</td><td>88.85%</td><td>89.42%</td></tr><tr><td> $RF^a$ </td><td>97.90%</td><td>92.71%</td><td>90.00%</td><td>95.43%</td></tr><tr><td rowspan="6">Mean</td><td>DT-Gini</td><td>89.90%</td><td>84.16%</td><td>89.03%</td><td>79.07%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>90.10%</td><td>84.16%</td><td>89.18%</td><td>79.13%</td></tr><tr><td> $RF^c$ </td><td>95.20%</td><td>88.03%</td><td>90.77%</td><td>85.28%</td></tr><tr><td>LR</td><td>87.40%</td><td>78.33%</td><td>68.25%</td><td>88.42%</td></tr><tr><td>ANN</td><td>92.20%</td><td>84.97%</td><td>86.95%</td><td>83.00%</td></tr><tr><td>ANN-Reg</td><td>93.20%</td><td>85.96%</td><td>87.47%</td><td>84.46%</td></tr><tr><td rowspan="6">Tree</td><td>DT-Gini</td><td>91.90%</td><td>87.17%</td><td>86.53%</td><td>87.81%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>92.10%</td><td>87.18%</td><td>86.51%</td><td>87.84%</td></tr><tr><td> $RF^b$ </td><td>96.00%</td><td>89.83%</td><td>90.04%</td><td>89.63%</td></tr><tr><td>LR</td><td>87.50%</td><td>79.79%</td><td>72.72%</td><td>86.85%</td></tr><tr><td>ANN</td><td>93.30%</td><td>86.91%</td><td>87.44%</td><td>86.37%</td></tr><tr><td>ANN-Reg</td><td>91.40%</td><td>84.06%</td><td>87.57%</td><td>80.56%</td></tr><tr><td rowspan="15">Extreme point replacement</td><td rowspan="3">No imputation</td><td>DT-Gini</td><td>93.00%</td><td>89.13%</td><td>89.05%</td><td>89.21%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>93.00%</td><td>89.14%</td><td>89.08%</td><td>89.21%</td></tr><tr><td> $RF^a$ </td><td>97.90%</td><td>92.76%</td><td>90.22%</td><td>95.30%</td></tr><tr><td rowspan="6">Mean</td><td>DT-Gini</td><td>89.90%</td><td>84.14%</td><td>88.72%</td><td>79.57%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>90.10%</td><td>84.14%</td><td>88.87%</td><td>79.42%</td></tr><tr><td> $RF^c$ </td><td>95.20%</td><td>88.02%</td><td>90.75%</td><td>85.28%</td></tr><tr><td>LR</td><td>83.40%</td><td>77.50%</td><td>67.38%</td><td>87.62%</td></tr><tr><td>ANN</td><td>92.20%</td><td>85.06%</td><td>86.66%</td><td>83.46%</td></tr><tr><td>ANN-Reg</td><td>91.70%</td><td>84.21%</td><td>88.08%</td><td>80.36%</td></tr><tr><td rowspan="6">Tree</td><td>DT-Gini</td><td>92.20%</td><td>87.27%</td><td>86.74%</td><td>87.80%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>92.20%</td><td>87.28%</td><td>86.76%</td><td>87.79%</td></tr><tr><td>RF</td><td>91.00%</td><td>89.66%</td><td>60.11%</td><td>94.20%</td></tr><tr><td>LR</td><td>87.80%</td><td>79.54%</td><td>72.13%</td><td>86.96%</td></tr><tr><td>ANN</td><td>93.50%</td><td>87.03%</td><td>87.74%</td><td>86.33%</td></tr><tr><td>ANN-Reg</td><td>91.50%</td><td>83.72%</td><td>86.72%</td><td>80.73%</td></tr><tr><td rowspan="15">Max normal variable transformation</td><td rowspan="3">No imputation</td><td>DT-Gini</td><td>93.00%</td><td>89.13%</td><td>89.05%</td><td>89.21%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>93.00%</td><td>89.14%</td><td>89.08%</td><td>89.21%</td></tr><tr><td> $RF^a$ </td><td>97.90%</td><td>90.21%</td><td>89.98%</td><td>95.43%</td></tr><tr><td rowspan="6">Mean</td><td>DT-Gini</td><td>90.30%</td><td>84.36%</td><td>89.12%</td><td>79.61%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>89.30%</td><td>84.31%</td><td>89.25%</td><td>79.37%</td></tr><tr><td> $RF^b$ </td><td>95.20%</td><td>88.04%</td><td>90.69%</td><td>85.51%</td></tr><tr><td>LR</td><td>87.20%</td><td>77.86%</td><td>68.21%</td><td>87.51%</td></tr><tr><td>ANN</td><td>92.40%</td><td>85.17%</td><td>86.72%</td><td>83.63%</td></tr><tr><td>ANN-Reg</td><td>93.40%</td><td>86.27%</td><td>87.64%</td><td>84.91%</td></tr><tr><td rowspan="6">Tree</td><td>DT-Gini</td><td>92.20%</td><td>88.01%</td><td>88.45%</td><td>87.57%</td></tr><tr><td>DT-Prob  $\chi^2$ </td><td>92.20%</td><td>88.04%</td><td>88.65%</td><td>87.43%</td></tr><tr><td> $RF^b$ </td><td>96.10%</td><td>89.94%</td><td>90.18%</td><td>89.69%</td></tr><tr><td>LR</td><td>88.80%</td><td>80.66%</td><td>83.90%</td><td>77.43%</td></tr><tr><td> $ANN^c$ </td><td>93.90%</td><td>87.57%</td><td>87.22%</td><td>87.92%</td></tr><tr><td>ANN-Reg</td><td>92.00%</td><td>84.30%</td><td>86.60%</td><td>82.00%</td></tr></table>

In set 1 (basic models), the best performance was obtained from random forests without imputation of missing values, with AUCs standing at 81.90%, 81.80% and 81.50%. This was followed by neural networks, with AUCs of 80.00% and 79.80%. In this set, following the random forest and neural networks, logistic regression models ranked third, and decision trees had the poorest performance.

In set 2 (comorbid models), random forests once again had the best performance with AUCs of 88.60%, 88.50% and 88.40% for the top three models. Similar to the basic models, neural networks, logistic regressions, and decision trees ranked second, third, and fourth, respectively.

In set 3 (over-sampled models), random forest models had the highest accuracy in detecting retinopathy among diabetic patients. The best models in set 3 had an AUC of 97.80%, which is remarkable. AUCs for other models in this set were significantly high, mostly over 92%. Neural networks were the second-best models in this set, but unlike sets 1 and 2, decision trees had the third rank in over-sampled models, and logistic regressions had the worst performance.

Graphs in Fig. 7 compare the modeling techniques within and between the three sets: basic, comorbid, and over-sampled. As expected, there clearly is a significant improvement (about 10%) from the basic to the comorbid models. Except for the logistic regression, the accuracy of the models built on the over-sampled sets are considerably higher than that of the comorbid sets for all the modeling techniques. Specifically, the AUCs of the over-sampled models (for random forest, neural networks, and decision tree techniques) were about 8% higher than the AUCs of their counterparts in the comorbid models. This improvement is expected, since in over-sampled models there are more data points available to train the models. The only modeling technique that did not improve by using over-sampled data was logistic regression, which was the only linear model used in this study. All other models (i.e., random forest, neural networks, and decision tree) are nonlinear; so, unlike logistic regression, they can take advantage of richer and more complicated data, leading to higher accuracy with oversampled data.

![](/api/attachments/B6JGVWCA/fulltext/images/63a16e10cfdd461860470d1dd4a46b9971d3ae3907f562c98db4ab66523d1911.jpg)  
No data manipulation- Tree imputation

![](/api/attachments/B6JGVWCA/fulltext/images/4d9e8e32a3573c53b862a06ffdfffc7a3a18834b3a9e616a55c81d85d9c12f9d.jpg)

![](/api/attachments/B6JGVWCA/fulltext/images/6c96b679fb49a918bf2a2d505ea8df85a1062ce71ff6796a2b572fab5b7044bb.jpg)  
No data manipulation- Mean imputation

The ROC charts of each one of the modeling techniques used in the three modeling sets is provided in Fig. 8, which demonstrates the superiority of the over-sampled models over the comorbid and basic models, and the dominance of the comorbid models over the basic models. In addition to the AUC, we compared the basic, comorbid, and oversampled models using the difference between sensitivity (true positive rate) and specificity (true negative rate) for each model in each set. Even though the overall accuracy is an important metric to compare models, a desired model is one that can classify both positive targets (in our case, patients with diabetic retinopathy) and negative targets (patients without diabetic retinopathy) at a high rate. Therefore, the lower the difference between sensitivity and specificity of a model, the better and more reliable that model. The average differences between sensitivity and specificity for models in set 1 (basic models), set 2 (comorbid models), and set 3 (over-sampled models) were 12.93%, 9.63%, and 6.06%, respectively. Thus, not only did the over-sampled

Max normal transformation- Tree imputation  
![](/api/attachments/B6JGVWCA/fulltext/images/f738fef33a012108ae4ddec1a4b5811ccc5fdc4a2ca8757626e71d237af64408.jpg)  
Extreme points replacement- Mean imputation  
Fig. 7. AUC comparison among modeling techniques and modeling sets.

Please cite this article as: S. Piri, et al., A data analytics approach to building a clinical decision support system for diabetic retinopathy: Developing and deploying a mode..., Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.05.012

models had the highest accuracy, but they were also more robust and reliable than the comorbid and basic models, with the comorbid models being more robust than the basic models.

Table 7 presents the accuracies of the best single model, existing ensemble approaches, and our proposed ensemble approach for the various datasets used in this study. As it can be seen, almost all ensemble models (except for 5 out of 90) have improved the prediction accuracy compared to the best single model. Those 5 simple average ensembles did not outperform their best constituting single models for a simple reason: not all models composing the ensemble had a good performance, however, they all were given an equal weight in determining the ensemble's final decision. Consequently, the overall accuracy of the ensembles created by simple averaging suffered in comparison to the accuracy of the best constituting single models. In fact, one of the most important requirements for building a good ensemble is to have comparably accurate and diverse single classifiers [58]. The results also show that the prediction accuracies improve from the simple average to the weighted average and culminate in the confidence margin ensemble models. Reaching to a performance peak in the confidence margin ensembles reflects their more accurate and more reliable assignment of weights compared to the weighted-average ensemble models. Voting-based ensembles outperformed the best single models in all cases. In two cases, voting-based models had the best predictive performance among all ensemble models. Similarly, random forest models outperformed all other types of ensembles in two cases. Overall, our proposed ensemble approach, the confidence margin ensemble, had the best performance in this study. More specifically, it excelled in 14 out of 18 total different data settings. It deserves to mention that we used logistic regression, decision tree, and neural network models for developing the simple average, weighted average, voting based, and confidence margin ensemble models.

![](/api/attachments/B6JGVWCA/fulltext/images/cb94fc8ba1d7cb3d4c449eacd51eb9959b806abb337d6008d074b9410172bf91.jpg)  
Random forest models (No data manipulation- no imputation)

## 4.3. Variable importance

As we mentioned in previous sections, 68 independent variables were included in our analyses. Understanding the predictive power of each of these variables could be helpful for physicians in better

![](/api/attachments/B6JGVWCA/fulltext/images/df67758811cf7b15db473a226ee25c819a87207145e40fe41fdfd3c09e530fd0.jpg)

![](/api/attachments/B6JGVWCA/fulltext/images/958258a614ee3c1670edd0bc66acc70f1745b4f0c068c4d47605bfce201a60a1.jpg)  
Artificial neural networks models (Extreme point replacementtree imputation)

Decision tree-Gini models (Extreme point replacement- mean imputation)  
![](/api/attachments/B6JGVWCA/fulltext/images/43f24d1a49f7b18751c246b6358c3137afb5867d9b25bde3b2ff4e3189a2ed0f.jpg)  
Logistic regression models (Max normal transformation- tree imputation)  
Fig. 8. ROC charts of modeling techniques in different sets

Table 7 Set 4 - ensemble models results.

<table><tr><td rowspan="3">Accuracy of ensemble models</td><td rowspan="3">Best single model</td><td colspan="5">Ensemble model type</td></tr><tr><td colspan="4">Existing approaches</td><td>Our approach</td></tr><tr><td>Simple average</td><td>Weighted average</td><td>Voting based</td><td>Random forest</td><td>Confidence margin</td></tr><tr><td colspan="7">Ensemble of models in set 1 (basic models)</td></tr><tr><td>No manipulation/tree imputation</td><td>72.99%</td><td>73.31%</td><td>73.37%</td><td>73.36%</td><td>72.33%</td><td>73.56%</td></tr><tr><td>No manipulation/mean imputation</td><td>72.96%</td><td>72.93%</td><td>72.99%</td><td>73.03%</td><td>71.87%</td><td>73.45%</td></tr><tr><td>Extreme point replacement/tree imputation</td><td>73.26%</td><td>73.28%</td><td>73.35%</td><td>73.46%</td><td>71.94%</td><td>73.42%</td></tr><tr><td>Extreme point replacement/mean imputation</td><td>72.14%</td><td>72.20%</td><td>72.34%</td><td>72.30%</td><td>72.05%</td><td>73.56%</td></tr><tr><td>Max normal variable transformation/tree imputation</td><td>72.78%</td><td>72.60%</td><td>72.89%</td><td>72.83%</td><td>71.71%</td><td>73.25%</td></tr><tr><td>Max normal variable transformation/mean imputation</td><td>72.60%</td><td>72.62%</td><td>72.75%</td><td>72.80%</td><td>72.05%</td><td>73.85%</td></tr><tr><td colspan="7">Ensemble of models in set 2 (comorbid models)</td></tr><tr><td>No manipulation/tree imputation</td><td>80.18%</td><td>80.16%</td><td>80.60%</td><td>80.78%</td><td>80.18%</td><td>80.64%</td></tr><tr><td>No manipulation/mean imputation</td><td>80.29%</td><td>80.57%</td><td>80.65%</td><td>80.62%</td><td>79.81%</td><td>80.97%</td></tr><tr><td>Extreme point replacement/tree imputation</td><td>79.97%</td><td>80.15%</td><td>80.29%</td><td>80.35%</td><td>79.95%</td><td>80.80%</td></tr><tr><td>Extreme point replacement/mean imputation</td><td>80.13%</td><td>80.25%</td><td>80.40%</td><td>81.05%</td><td>79.84%</td><td>80.93%</td></tr><tr><td>Max normal variable transformation/tree imputation</td><td>79.70%</td><td>80.11%</td><td>80.37%</td><td>80.40%</td><td>79.79%</td><td>80.75%</td></tr><tr><td>Max normal variable transformation/mean imputation</td><td>79.72%</td><td>80.20%</td><td>80.38%</td><td>80.40%</td><td>79.90%</td><td>80.81%</td></tr><tr><td colspan="7">Ensemble of models in set 3 (oversample models)</td></tr><tr><td>No manipulation/tree imputation</td><td>87.18%</td><td>88.23%</td><td>88.27%</td><td>88.03%</td><td>89.83%</td><td>88.38%</td></tr><tr><td>No manipulation/mean imputation</td><td>85.96%</td><td>86.15%</td><td>86.92%</td><td>87.11%</td><td>89.83%</td><td>89.21%</td></tr><tr><td>Extreme point replacement/tree imputation</td><td>87.28%</td><td>87.01%</td><td>88.68%</td><td>88.60%</td><td>89.66%</td><td>89.84%</td></tr><tr><td>Extreme point replacement/mean imputation</td><td>85.06%</td><td>86.08%</td><td>86.98%</td><td>87.15%</td><td>88.02%</td><td>88.42%</td></tr><tr><td>Max normal variable transformation/tree imputation</td><td>88.04%</td><td>87.91%</td><td>88.58%</td><td>88.52%</td><td>89.94%</td><td>90.12%</td></tr><tr><td>Max normal variable transformation/mean imputation</td><td>86.27%</td><td>86.52%</td><td>87.05%</td><td>87.62%</td><td>88.04%</td><td>88.25%</td></tr></table>

Bold values shows the best/highest accuracy percentage in each row

managing the course of the disease by controlling factors that are highly associated with retinopathy.

As the results show, random forest models have the best performance among other modeling techniques; therefore, to specify the importance of variables according to their predictive powers, we applied the Gini reduction metric on the validation datasets using the output from random forest models. Fig. 9 shows the variable importance in detecting retinopathy based on the Gini reduction score in multiple random forest models. Based on our findings, neuropathy; creatinine serum and blood urea nitrogen (both measures of kidney function); glucose serum plasma (used to screen for prediabetes and diabetes); and hematocrit (a measure of red blood cell concentration) were the most important variables for detecting diabetic retinopathy.

![](/api/attachments/B6JGVWCA/fulltext/images/b327d832f00c66efb0a6ebc77fdd2d364bd49ae6b0a9c49d9042236121c27347.jpg)  
Fig. 9. Variable importance ranking in detecting diabetic retinopathy [Y-axis represents the average of normalized Gini reduction].

Please cite this article as: S. Piri, et al., A data analytics approach to building a clinical decision support system for diabetic retinopathy: Developing and deploying a mode..., Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.05.012

S. Piri et al. / Decision Support Systems xxx (2017) xxx–xxx

## 5. Discussion and conclusion

In this study, we analyzed data from N1.4 million diabetic patients. Our objective was to develop a CDSS to detect diabetic retinopathy using demographic, lab procedure, and comorbidity data only. Several aspects distinguish this research study from other existing studies in this area. First, this study included a far greater number of patients and risk factors in the analysis, which contribute to the rigor and robustness of the findings. While other similar studies used data from several hundred patients, we employed data from N300,000 patients to develop the predictive models. Second, through a series of database operations and data preparation steps conducted in SAS, we incorporated patients' comorbidity data into our models, which significantly improved the accuracy of our predictive analytics-based CDSS. The results we obtained from the comorbid models were in line with other research that emphasizes the importance, and advantage, of analyzing concurrent conditions instead of studying each condition in isolation. Third, we over-sampled the rare event, which made it possible to preserve important features in the data that could have been lost through pure under-sampling. Models we built by utilizing over-sampled data were much more accurate and robust compared to comorbid and basic models, especially in non-linear modeling techniques (such as random forest, neural network, and decision tree) that can handle more complex data. Finally, we developed and evaluated a novel ensemble approach, which we call the confidence margin ensemble. Our evaluations showed that confidence margin ensembles had better overall performance compared to the existing ensemble models. We also addressed the issue of tie in voting-based ensemble models by comparing the confidence margins of the base predictors.

To make sure that the quality and veracity of our datasets were acceptable, we devoted a considerable amount of time and effort to data cleaning and preparation. We analyzed the distribution, missing value percentage, and potential outliers of each of the predictors, and included only those variables that were rich enough and had significant predictive powers. As a result, there should be little doubt about the quality, robustness, and accuracy of our models.

Based on our analyses, diabetic neuropathy had the strongest predictive power in detecting diabetic retinopathy, followed by creatinine serum, blood urea nitrogen, glucose serum plasma, and hematocrit. The results showed it is possible to predict diabetic retinopathy with 92.76% accuracy using only the results of a routine blood test. The accuracy of our CDSS may not be as high as the fundus image-based solutions (for example, Kumar and Madheswaran [13] reached an accuracy of 97%), but considering the ease-of-use and the cost-effectiveness of our approach, the resulting CDSS is not only competitive to the existing fundus image-based solutions, but also it can reduce the currently high rate of noncompliance with annual routine ophthalmologic exams. A conspicuous benefit of our CDSS, therefore, is a lower number of patients who would eventually develop retinopathy, which in turn will result in a more efficient healthcare delivery and management system.

Medical researchers and clinicians (e.g., Sabanayagam, et al. [59]) have noted the necessity of developing an accurate predictive model for diabetic retinopathy. We believe our CDSS, which has several practical and clinical applications, fills this gap. First, as mentioned earlier, it makes up for the low compliance rate of annual comprehensive eye examination for retinopathy. This annual eye examination is necessary for every diabetic patient, but because of inconvenience of the procedure and unavailability of equipment and specialists, it has one of the lowest compliance rates in the U.S. healthcare. Second, the input to this CDSS is nothing but the results of a routine blood test that makes it easy for clinicians, and even for patients, to use. Unlike the current procedure of diagnosing retinopathy, there is no need for an ophthalmologist and special cameras to employ this CDSS; clinician can refer high risk patients (based on the result of our CDSS) to ophthalmologists for more accurate examination and potential treatments. Third, our models identify factors that are most strongly related to diabetic retinopathy. By controlling these factors, doctors and patients will be able to manage the course of the disease in a more effective way. Finally, applying our CDSS can help detect this complication at early stages, and since there exists an effective laser therapy to prevent the progress of retinopathy, vision can be saved for many diabetic patients.

In conclusion, considering the prevalence of retinopathy among diabetic patients (about one third of diabetics have retinopathy [60]) and the significant proportion of individuals whose susceptibility to retinopathy remains undiagnosed (about 50% of all diabetic retinopathy patients), our CDSS provides a great value to people who suffer from diabetes all over the world. Based on the current statistics (about 30 million in the US and 415 million worldwide [61]), diabetic retinopathy remains undiagnosed in 5.5 million US citizens (30M×30% ×50% =5.5M) and in N62 million individuals around the globe $( 4 1 5 M \times 3 0 \% \times 5 0 \% = 6 2 . 2 5 M )$ Therefore, if our CDSS helps diagnose even a small percentage of these cases at early stages of the disease, vision, and quality of life, can be saved for a large number of diabetics. Although we cannot appraise the value of sight to an individual, we can enumerate some of the costs associated with losing it, such as medical care, assistance programs, and loss of productivity costs. Therefore, the application of our CDSS helps save a large amount of expenses in both healthcare and welfare systems.

As a final note, we admit that our study has a number of limitations. First, in the EMR data we used, we did not have information about the time a patient's disease was first diagnosed. As a results, we could not incorporate the duration of time the patients lived with diabetes into our models. Since longer duration of diabetes has been shown to be a strong predictor of retinopathy [18], our CDSS could even perform better had we had access to the patients' date of diagnosis. Fortunately, having access to several other predictors made up for the lack of this variable. Additionally, we should note that every machine learning tech nique has several parameters that can be adjusted. Even though we tried to systematically adjust these parameters to achieve better results, those values cannot be considered optimal.

## Acknowledgements

This study was conducted with the data provided by, and the support from, the Center for Health Systems Innovation (CHSI) at Oklahoma State University (OSU) and the Cerner Corporation. The mentorship and guidance of Dr. William Paiva, executive director of CHSI, Dr. Lloyd Hildebrand, professor of ophthalmology at University of Oklahoma, and Dr. Scott Shepherd, medical director of CHSI, during the conduct of this study is highly appreciated. Their medical insights provided us the much needed understanding of the medical domain for proper execution of this study. We would also like to acknowledge Ms. Elvena Fong, health data analytics program manager at CHSI, and Dr. Krista Schumacher, technical writer of CHSI for their support. The contents of this work are solely the responsibility of the authors and do not necessarily represent the official views of CHSI, OSU or the Cerner Corporation.

## References

[1] Department of Health and Human Services (Ed.), National Diabetes Statistics Report: Estimates of Diabetes and Its Burden in the United States. Centers for Disease Control and Prevention, Atlanta, GA: U.S, 2014.

[2] D.S. Fong, L. Aiello, T.W. Gardner, G.L. King, G. Blankenship, J.D. Cavallerano, F.L. Ferris, R. Klein, Diabetic retinopathy, Diabetes Care 26 (January 1, 2003) s99–s102.

[3] W. Raghupathi, V. Raghupathi, Big data analytics in healthcare: promise and potential, Health Information Science and Systems 2 (2014) 1.

[4] I. Torre-Díez, B. Martínez-Pérez, M. López-Coronado, J.R. Díaz, M.M. López, Decision support systems and applications in ophthalmology: literature and commercial review focused on mobile apps I. Med, Syst, 39 (2014) 1–10

[5] A. Karma, S. Gummerus, E. Kujansuu, T. Pitkäjärvi, Predicting diabetic retinopathy, Acta Ophthalmol. 65 (1987) 136–139.

[6] R. Klein, B.K. Klein, S.E. Moss, M.D. Davis, D.L. DeMets, GLycosylated hemoglobin predicts the incidence and progression of diabetic retinopathy, JAMA 260 (1988) 2864–2871.

[7] P. Kahai, K.R. Namuduri, H. Thompson, A decision support framework for automated screening of diabetic retinopathy, Int. J. Biomed. Imaging 2006 (2006) 8.

[8] A. Paunksnis, V. Barzdziukas, D. Jegelevicius, S. Kurapkiene, G. Dzemyda, The use of information technologies for diagnosis in ophthalmology, J. Telemed. Telecare 12 (Julv 1.2006) 37–40

Please cite this article as: S. Piri, et al., A data analytics approach to building a clinical decision support system for diabetic retinopathy: Developing and deploying a mode..., Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.05.012

ty (EMBC). 2010 Annual International Conference of the IEEE 2010, pp, 6713–6716.

[9] K. Marsolo, M. Twa, M.A. Bullimore, S. Parthasarathy, Spatial modeling and classification of corneal shape, IEEE Trans. Inf. Technol. Biomed. 11 (2007) 203–212.

[10] C.L. Tsai, B. Madore, M.J. Leotta, M. Sofka, G. Yang, A. Majerovics, H.L. Tanenbaum, C.V. Stewart, B. Roysam, Automated retinal image analysis over the internet, IEEE Trans. Inf. Technol. Biomed. 12 (2008) 480–487.

[11] K. Noronha, U. Acharya, K. Nayak, S. Kamath, S. Bhandary, Decision support system for diabetes retinopathy using discrete wavelet transform, Proc. Inst. Mech. Eng. H J. Eng. Med. (2012) p. 0954411912470240.

[12] S.-E. Bursell, L. Brazionis, A. Jenkins, Telemedicine and ocular health in diabetes mellitus, Clin. Exp. Optom. 95 (2012) 311–327.

[13] S.J.J. Kumar, M. Madheswaran, An improved medical decision support system to identify the diabetic retinopathy using fundus images, J. Med. Syst. 36 (2012) 3573–3581.

[14] D. Xiao, J. Vignarajan, J. Lock, S. Frost, M.-L. Tay-Kearney, Y. Kanagasingam, Retinal image registration and comparison for clinical decision support, The Australasian Medical Journal 5 (2012) 507.

[15] M.R.K. Mookiah, U.R. Acharya, C.K. Chua, C.M. Lim, E. Ng, A. Laude, Computer-aided diagnosis of diabetic retinopathy: a review, Comput. Biol. Med. 43 (2013) 2136–2155.

[16] P. Prasanna, S. Jain, N. Bhagat, A. Madabhushi, Decision support system for detection of diabetic retinopathy using smartphonesPervasive Computing Technologies for Healthcare (PervasiveHealth), 2013 7th International Conference on 2013, pp. 176–179.

[17] A. Bourouis, M. Feham, M.A. Hossain, L. Zhang, An intelligent mobile based decision support system for retinal disease diagnosis, Decis. Support. Syst. 59 (2014) 341–350.

[18] R. Klein, B.E. Klein, S.E. Moss, M.D. Davis, D.L. DeMets, The Wisconsin epidemiologic study of diabetic retinopathy: III. Prevalence and risk of diabetic retinopathy when age at diagnosis is 30 or more years, Arch. Ophthalmol. 102 (1984) 527–532.

[19] R. Klein, B.E. Klein, S.E. Moss, M.D. Davis, D.L. DeMets, The Wisconsin epidemiologic study of diabetic retinopathy: II. Prevalence and risk of diabetic retinopathy when age at diagnosis is less than 30 years, Arch. Ophthalmol. 102 (1984) 520–526.

[20] R.J. Tapp, J.E. Shaw, C.A. Harper, M.P. De Courten, B. Balkau, D.J. McCarty, H.R. Taylor, T.A. Welborn, P.Z. Zimmet, The prevalence of and factors associated with diabetic retinopathy in the Australian population, Diabetes Care 26 (2003) 1731–1737.

[21] B.E. Klein, S.E. Moss, R. Klein, T.S. Surawicz, The Wisconsin epidemiologic study of diabetic retinopathy: XIII. Relationship of serum cholesterol to retinopathy and hard exudate, Ophthalmology 98 (1991) 1261–1265.

[22] E.Y. Chew, M.L. Klein, F.L. Ferris, N.A. Remaley, R.P. Murphy, K. Chantry, B.J. Hoogwerf, D. Miller, Association of elevated serum lipid levels with retinal hard ex udate in diabetic retinopathy: early treatment diabetic retinopathy study (ETDRS) report 22, Arch. Ophthalmol. 114 (1996) 1079–1084.

[23] D.S. Fong, L. Aiello, T.W. Gardner, G.L. King, G. Blankenship, J.D. Cavallerano, F.L. Ferris, R. Klein, Retinopathy in diabetes, Diabetes Care 27 (2004) s84–s87.

[24] R. Klein, B.E. Klein, S.E. Moss, K.J. Cruickshanks, The Wisconsin epidemiologic study of diabetic retinopathy: XVII: the 14-year incidence and progression of diabetic retinopathy and associated risk factors in type І diabetes11Proprietary interest: none, Ophthalmology 105 (1998) 1801–1815.

[25] R. Klein, M.D. Knudtson, K.E. Lee, R. Gangnon, B.E. Klein, The Wisconsin epidemiologic study of diabetic retinopathy XXIII: the twenty-five-year incidence of macular edema in persons with type І diabetes, Ophthalmology 116 (2009) 497–503.

[26] M. Skevofilakas, K. Zarkogianni, B.G. Karamanos, K.S. Nikita, A hybrid Decision Support System for the risk assessment of retinopathy development as a long term complication of Type І Diabetes MellitusEngineering in Medicine and Biology Socie-

[27] V. Balakrishnan, M.R. Shakouri, H. Hoodeh, Developing a hybrid predictive system for retinopathy. I. Intell, Fuzzy Syst, 25 (2013) 191–199.

[28] M.S. Roy, R. Klein, B.J. O'Colmain, B.E. Klein, S.E. Moss, J.H. Kempen, The prevalence of diabetic retinopathy among adult Type 1 diabetic persons in the United States, Arch. Ophthalmol. 122 (2004) 546 551.

[29] E. Dimitriadou, A. Weingessel, K. Hornik, A Cluster Ensembles Framework, Design and Application of Hybrid Intelligent Systems, IOS Press, Amsterdam, The Netherlands. 2003

[30] J.W. Tukey, Exploratory Data Analysis, 1977.

[31] T.G. Dietterich, Ensemble methods in machine learning, International Workshop on Multiple Classifier Systems 2000, pp. 1–15.

[32] G. Seni, J.F. Elder, Ensemble methods in data mining: improving accuracy through combining predictions, Synthesis Lectures on Data Mining and Knowledge Discovery, vol. 2, 2010, pp. 1–126.

[33] Z. Li, W. Xu, L. Zhang, R.Y. Lau, An ontology-based web mining method for unemployment rate prediction, Decis. Support. Syst. 66 (2014) 114–122.

[34] G. Wang, J. Sun, J. Ma, K. Xu, J. Gu, Sentiment classification: The contribution of ensemble learning, Decis. Support. Syst. 57 (1) (2014) 77–93.

[35] L. Rokach, Ensemble-based classifiers, Artif. Intell. Rev. 33 (2009) 1–39.

[36] D. Delen, A. Oztekin, L. Tomak, An analytic approach to better understanding and management of coronary surgeries, Decis. Support. Syst. 52 (2) (2012) 698–705.

[37] H.V. Jagadish, J. Gehrke, A. Labrinidis, Y. Papakonstantinou, J.M. Patel, R. Ramakrishnan, C. Shahabi, Big data and its technical challenges, Commun. ACM 57 (2014) 86–94.

[38] M. Kubat, R.C. Holte, S. Matwin, Machine learning for the detection of oil spills in satellite radar images Mach. Learn. 30 (1998) 195–215

[39] R.B. Rao, S. Krishnan, R.S. Niculescu, Data mining for improved cardiac care, ACM SIGKDD Explorations Newsletter, vol. 8, 2006, pp. 3–10.

[40] P.K. Chan, W. Fan, A.L. Prodromidis, S.J. Stolfo, Distributed data mining in credit card fraud detection, Intelligent Systems and their Applications. IEEE, vol. 14. 1999. pp. 67–74.

[41] H. Haibo, E.A. Garcia, Learning from imbalanced data, Knowledge and Data Engineering, IEEE Transactions on, vol. 21, 2009, pp. 1263–1284.

[42] D.W. Hosmer Jr., S. Lemeshow, Applied Logistic Regression, John Wiley & Sons, 2004.

[43] P. Hájek, Municipal credit rating modelling by neural networks, Decis. Support. Syst. 51 (4) (2011) 108–118.

[44] R. Bellazzi, B. Zupan, Predictive data mining in clinical medicine: current issues and guidelines, Int. J. Med. Inform. 77 (2) (2008) 81–97.

[45] M.T. Hagan, H.B. Demuth, M.H. Beale, O. De Jesús, Neural Network Design, vol. 20, PWS Publishing Company, Boston, 1996.

[46] S. Lee, Using data envelopment analysis and decision trees for efficiency analysis and recommendation of B2C controls Decis Support, Syst, 49 (11) (2010) 486–497.

[47] L. Breiman, Random forests, Mach. Learn. 45 (2001/10/01) 5–32.

[48] H.M. Zolbanin, D. Delen, A. Hassan Zadeh, Predicting overall survivability in comorbidity of cancers: A data mining approach, Decis. Support. Syst. 74 (6) (2015) 150–161.

[49] P.C. Albertsen, D.F. Moore, W. Shih, Y. Lin, H. Li, G.L. Lu-Yao, Impact of comorbidity on survival among men with localized prostate cancer, J. Clin. Oncol. 29 (2011) 1335–1341.

[50] A.D. Hanchate, K.M. Clough-Gorr, A.S. Ash, S.S. Thwin, R.A. Silliman, Longitudinal patterns in survival, comorbidity. healthcare utilization and quality of care among older women following breast cancer diagnosis, J. Gen. Intern. Med. 25 (2010) 1045–1050.

[51] S. Hill, D. Sarfati, T. Blakely, B. Robson, G. Purdie, J. Chen, E. Dennett, D. Cormack, R. Cunningham, K. Dew, Survival disparities in indigenous and non-indigenous New Zealanders with colon cancer: the role of patient comorbidity, treatment and health service factors, J. Epidemiol. Community Health 64 (2010) 117–123

[52] H. Teppo, O.-P. Alho, Comorbidity and diagnostic delay in cancer of the larynx, tongue and pharynx, Oral Oncol. 45 (2009) 692–695.

[53] H. He, E.A. Garcia, Learning from imbalanced data, Knowledge and Data Engineering, IEEE Transactions on, vol. 21, 2009, pp. 1263–1284.

[54] N.V. Chawla, K.W. Bowyer, L.O. Hall, W.P. Kegelmeyer, SMOTE: synthetic minority over-sampling technique, J. Artif. Intell. Res. (2002) 321–357.

[55] P. Liu, Y. Wang, L. Cai, L. Zhang, Classifying skewed data streams based on reusing dataComputer Application and System Modeling (ICCASM), 2010 International Conference on, 2010 pp. V4-90-V4-93.

[56] V. Ganganwar, An overview of classification algorithms for imbalanced datasets, International Journal of Emerging Technology and Advanced Engineering 2 (2012) 42–47.

[57] B. Wang, N. Japkowicz, Imbalanced data set learning with synthetic samples, Proc. IRIS Machine Learning Workshop 2004, p. 19.

[58] L.K. Hansen, P. Salamon, Neural network ensembles, IEEE Trans. Pattern Anal. Mach. Intell. 12 (1990) 993–1001.

[59] C. Sabanayagam, W. Yip, D.S. Ting, G. Tan, T.Y. Wong, Ten emerging trends in the epidemiology of diabetic retinopathy, Ophthalmic Epidemiol. (2016) 1–14.

[60] R. Lee, T.Y. Wong, C. Sabanayagam, Epidemiology of diabetic retinopathy, diabetic macular edema and related vision loss, Eye and Vision 2 (2015) 17.

[61] Belgium International Diabetes Federation, IDF Diabetes Atlas, seventh ed. International Diabetes Federation. Brussels. 2015.

![](/api/attachments/B6JGVWCA/fulltext/images/60d891595c4509035a6ead95d870044784db745ff0624407052f2fff2000c788.jpg)  
Saeed Piri is a PhD student in the Industrial Engineering and Management and a Research Associate in the Center for Health Systems Innovation at Oklahoma State University. He earned his Master's degree in Industrial Engineering from Sharif University of Technology in 2008. He has presented his research in several national and international conferences. His research interests include developing decision support systems, machine learning, imbalanced data learning, and application of business analytics in healthcare domain.

![](/api/attachments/B6JGVWCA/fulltext/images/b836e76051d0ae016517e956b08967b46a17665e4e60a6d8869b74998a4076b1.jpg)

Dr. Dursun Delen is the holder of William S. Spears and Neal Patterson Endowed Chairs in Business Analytics, Director of Research for the Center for Health Systems Innovation, and Professor of Management Science and Information Systems in the Spears School of Business at Oklahoma State University (OSU). He received his Ph.D. in Industrial Engineering and Management from OSU in 1997. Prior to his appointment as an Assistant Professor at OSU in 2001, he worked for a privately-owned research and consultancy company, Knowledge Based Systems Inc., in College Station, Texas, as a research scientist for five years, during which he led a number of decision support, information systems and advanced analytics related research projects funded by federal agencies, including DoD, NASA, NIST and DOE. His research has appeared in major

journals including Decision Support Systems, Communications of the ACM, Computers and Operations Research Computers in Industry Journal of Production Operations Management Artificial Intelligence in Medicine, Expert Systems with Applications, among others. He recently published seven books/textbooks in the broader are of Business Analytics. He is often invited to national and international conferences for keynote addresses on topics related to Healthcare Analytics Data/Text Mining Business Intelligence, Decision Support Systems Business Analytics and Knowledge Management, He regularly serves and chairs tracks and mini-tracks at various information systems and analytics conferences, and serves on several academic journals as editor-in-chief, senior editor, associate editor and editorial board member. His research and teaching interests are in data and text mining, decision support systems, knowledge management, business intelligence and enterprise modeling.

![](/api/attachments/B6JGVWCA/fulltext/images/1b27e1b3f99255f60132487a264cf9911b1a08ca067a1d8f653a29c74daee3fe.jpg)

S. Piri et al. / Decision Support Systems xxx (2017) xxx–xxx

Dr. Tieming Liu is an associate professor at the School of Industrial Engineering and Management, Oklahoma State University. He received his doctoral degree in Transportation and Logistics from the Massachusetts Institute of Technology in 2005, his master's degree in Industrial Engineering and Management Science from Northwestern University in 2001, and his master's and bachelor's degrees in Control Theory and Control Engineering from Tsinghua University in 2000 and 1997, respectively. His research interests include supply chain management, logistics planning, and healthcare analytics. His research has been published in major journals, including IIE Transactions, Interfaces, Production and Operations Management, Naval Research Logistics, Operations Research Letters, European Journal of Operational Research, among others.

![](/api/attachments/B6JGVWCA/fulltext/images/3d1b2c2ef119e204acc40e6f6d57daf95b2f81257ab8e0c7399e9232461f31e1.jpg)

Dr. Hamed M. Zolbanin is an Assistant Professor and the Director of the Business Analytics program at Ball State University. He earned his doctorate in Management Science and Information Systems from Oklahoma State University. He has presented his research in several national and interna tional conferences. He has published a healthcare analytics research article in decision support systems journal, and has several articles under review at reputable journals in the area of analytics and information systems. His research interests include healthcare analytics, medical informatics, business intelligence, decision support systems, machine learning, predictive modeling and business analytics.
