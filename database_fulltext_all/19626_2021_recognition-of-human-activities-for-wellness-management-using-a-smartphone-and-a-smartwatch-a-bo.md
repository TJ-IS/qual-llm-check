---
otero_id: 19626
otero_key: "48A63D8C"
title: "Recognition of human activities for wellness management using a smartphone and a smartwatch: A boosting approach"
authors: "Pratik Tarafdar; Indranil Bose"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113426"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

Recognition of human activities for wellness management using a smartphone and a smartwatch: A boosting approach

Decision Support Systems

Pratik Tarafdar, Indranil Bose

![](/api/attachments/48A63D8C/fulltext/images/63fd24f0b2bcdf411662dac74197a7b7c77b36ba1fb1c99208626e44eed2f888.jpg)

PII: S0167-9236(20)30181-0

DOI: https://doi.org/10.1016/j.dss.2020.113426

Reference: DECSUP 113426

To appear in: Decision Support Systems

Received date: 20 April 2020

Revised date: 13 September 2020

Accepted date: 17 October 2020

Please cite this article as: P. Tarafdar and I. Bose, Recognition of human activities for wellness management using a smartphone and a smartwatch: A boosting approach, Decision Support Systems (2020), https://doi.org/10.1016/j.dss.2020.113426

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2020 Published by Elsevier.

# Recognition of Human Activities for Wellness Management Using a Smartphone and a Smartwatch: A Boosting Approach

Pratik Tarafdar<sup>1</sup> pratik\_tarafdar@yahoo.com, Indranil Bose<sup>2,\*</sup> bose@iimcal.ac.in

<sup>1</sup>Information Systems & Analytics, Jindal Global Business School, O.P. Jindal Global

University, Haryana 131001, India

<sup>2</sup>Indian Institute of Management Calcutta, Diamond Harbour Road, Kolkata 700104, India

Corresponding author.

## Abstract

Mobile health applications are considered to be powerful tools for activity-based wellness management. With the availability of multimodal sensors in smart devices used in our daily lives, it is possible to track human activity and deliver context-aware wellness services. The embedded sensors in naturally used devices such as smartphones, smartwatches, and wearables contain rich information that can be integrated for human activity recognition. Our research demonstrates how powerful boosting algorithms can extract knowledge for human activity classification in a real-life setting. Our results show that boosting classifiers outperform traditional machine learning classifiers in the detection of basic human activities such as walking, standing, sitting, exercise, and sleeping. Further, we perform feature engineering to compare the potential of a smartphone and a smartwatch in activity detection. Our feature engineering strategy provides directions about the selection of sensor features for improvement in classification of basic human activities. The theoretical and practical implications of this research for activity-based wellness management are also discussed.

Keywords

Activity-based wellness management, Boosting algorithms, Human activity recognition, Machine learning, Mobile health, Multimodal sensors.

## 1. Introduction

Wellness management is defined as the systematic management of an individual’s daily activities or habits to help him/ her pursue health goals and well-being. In this age of increasing costs of medical care, wellness systems are gaining popularity because they bring about the transformation of healthcare from treatment to prevention. To achieve this $\therefore \lambda \lambda$ , machine learning is instrumental in developing wellness monitoring tools for persuading users to lead a healthy lifestyle through timely intervention. The wellness monitoring tools are usually integrated with sophisticated sensors that continuously sense the user’s contextual environment, and machine learning helps in analysing the user’s context to determine the right strategy for wellness intervention. According to the Global Wellness Institute [1], wellness expenditures (\$4.2 trillion) constitute more than half of the total global healthcare expenditures (\$7.3 trillion). The growth of the wellness industry can be enhanced through the use of machine learning capabilities in the form of deeper personalization (i.e., specific recommendations under $\mathrm { { v } . . . \mathrm { { y i n g } } }$ contexts). Gartner envisaged that daily wellness activities in future would be prompted by a virtual assistant, powered by an algorithmic engine [2].

Smart devices such as smartphones and smartwatches are increasingly integrated with sensors that are helpful for inferring a person‟s activity and context at any particular time. The problem of activity recognition is important for wellness management applications such as assisted living [3], fitness tracking [4], user-adaptive services [5], and automatic monitoring or supervision of patients with chronic illness [6]. The challenge in human activity recognition (HAR) lies in providing a pervasive and unobtrusive mechanism for the collection of data related to the daily routine activities or human behaviour. The non-interfering systems in real-life settings such as smartphones and smart wearables are instrumental for HAR since the unobtrusive sensors can capture natural human behaviour.

The context of human behaviour is complex and nuanced. The data collected through unobtrusive systems need to be rich enough to give rise to actionable insights about the context of human behaviour. The natural behaviour consists of several overlapping contexts occurring at the same time. For example, people may be walking indoors, outdoors, or on a treadmill. In this case, the geographical context overlaps with the behavioural context. The efficacy of the HAR systems is assessed by its ability to eliminate such variability in the natural environment accurately. Most of the studies related to HAR have gathered sensor data through controlled laboratory experiments and developed models and algorithms using it [7–9]. However, these models have determined the context for scripted tasks in designated locations and are generally impractical for real-time applications due to the presence of inconvenient sensing apparatus or the failure to eliminate noise in natural behaviour [10]. This paper addresses the above research gap by analysing real-time data of human activities involved in daily living obtained from unobtrusive multimodal sensors present in smartphones and smartwatches. The research question we address in this paper can be stated as:

RQ: How accurate are machine learning methods in identifying human activities for

Our research proposes an advanced machine learning (ML) approach to HAR systems that includes data collection, data cleaning, feature extraction, feature engineering, and modelling with classification algorithms for predicting human activities. We compare the performance of tree-based boosting algorithms with other traditional ML techniques for identifying human activities using motion sensors from smart devices. Feature engineering techniques are used to highlight the importance of features in improving the performance of the system. We also show that our proposed model for HAR surpasses the predictive accuracy reported in extant research. Figure 1 provides a schematic representation of the research model.

![](/api/attachments/48A63D8C/fulltext/images/742b96e446c141212bbee5f2685a297c875bc345ee714925c3c2903c098f1606.jpg)  
Figure 1 The research model

## 2. Related Works

The HAR systems for wellness management have been extensively studied in the literature. Prior research has included different types of sensors and sensor locations, diverse populations, various research settings, and several human activities. For example, some researchers have focused on inertial sensors such as accelerometer, gyroscope, and magnetometer to generate insights about human activities, whereas others have focused on physical health sensors such as force/ pressure Some have used highly obtrusive sensing apparatus under controlled environmental conditions in contrast with others that have used less obtrusive or unobtrusive sensors in a natural environment [6]. Given our research objective, we focus our review of related literature on HAR using embedded sensors of smartphones, smartwatches, or wearables.

Controlled Laboratory Experiment: Several studies have collected data by instructing participants to perform scripted tasks in laboratory settings. For example, Guo et al. [12] have generated the training data for their smartphone-based patient activity recognition by instructing two volunteers to perform six basic movement activities each time by placing the phone in four different orientations (vertically inward, vertically outward, horizontally inward, and horizontally outward) for two different positions (coat pocket, and trouser pocket). They have used the data to develop a selflearning scheme for unpredictable activity recognition and have reported an accuracy of more than 80%. In another example, Chernbumroong et al. [13] have used a Chronos watch, a wearable gadget, and a heart rate monitor chest strap to record the scripted activities of 12 elderly participants in their study for home-based care. The participants are asked to perform 13 activities (including brushing teeth, exercising, feeding, ironing, reading, scrubbing, sleeping, using stairs, sweeping, walking, washing dishes, watching television, and wiping) in any order, each for 10 minutes. The researchers have recorded 12 raw data points, including three axes of acceleration, three axes of rotation, heart extracted 202 features (such as mean, standard deviation, skewness, kurtosis, etc.) from the raw data, used feature engineering, and trained several classifiers with the selected features. A support vector machine (SVM) classifier with 24 features has shown the highest average accuracy of 97.2% in HAR. In both the studies described above, the laboratory settings in their experiment have restricted the external validity of the predictive models.

San-Segundo et al. [14] have studied HAR using both smartphones and smartwatches. They have implemented several prediction models on a public dataset obtained from sensor recordings of eight smartphones and four smartwatches carried by nine users while performing a scripted set of activities. Apart from the limitation in terms of external validity of the experimental setup, another difficulty in their research was the necessity to carry multiple smart devices that defied the notion of user acceptance.

Natural Experiment: To promote real-life working applications, three conditions have been found to be important for HAR. These include the introduction of naturally used devices, unconstrained device placement, and recording of human behaviour in subjects‟ natural environment [15]. For this purpose, Ganti et al. [16] have performed a natural experiment by allowing eight subjects to follow their daily routine for eight weeks. However, the phone has been placed in a pouch or in the pocket of the subject. The researchers have developed a mobile application that has allowed users to select an activity from a set of eight activities and mark the start time as well as the end time of the activity.

A Bayesian learning approach has been used to train the naturally obtained sensor recordings to infer labelled activities. Similarly, Vaizman et al. [15] have developed a mobile application called ExtraSensory to record self-reporting of one or more of the 100 context labels. They have used sensor recordings (from the accelerometer, gyroscope, magnetometer, location sensors, microphone, and various other sensors) of both a smartphone and a smartwatch to recognize natural human behaviour. The participants have been allowed to select a combination of labels while performing a number of activities simultaneously. For example, if the participant has been eating while watching Moreover, the participants have not been constrained to wear the watch all the time or to keep the phone in a particular location. They have used smart devices as much as possible and as per their Ther fore, the dataset that is collected through the Extrasensory app, comprising labelled data for ensor recordings of over 300,000 minutes from 60 subjects, represents human collection is the largest among all extant studies related to HAR.

ance of single-sensor classifiers and sensor-fusion classifiers on 25 (out of 100) context labels extracted from the ExtraSensory dataset. The 25 labels can belong to diverse context domains such as bathing, driving, shopping, cycling, sleeping, running, walking, at home, at a restaurant, in a meeting, etc. They have observed that multi-sensor classifiers have performed better than single-sensor classifiers with the highest average accuracy of 80%. Natarajan [17] has used active learning methods to develop one-versus-all classifiers for each of the following activities – sleeping, working on a computer, driving, and surfing the internet. He has used the Extrasensory dataset to train and test his models and has achieved accuracies of 89%, 71%, 87%, and 63% respectively. Similarly, Adams [18] has used the same dataset to develop a sleep detection system using semi-Markov conditional random fields. We observe that multiple studies have exploited the ExtraSensory dataset to develop classification models for HAR.

## Journal Pre-proof

Table 1 summarizes the key literature related to activity monitoring using a smartphone and a smartwatch. The extant literature lacks in (a) HAR research under natural experimental conditions (i.e., using everyday devices, unconstrained device placement, and recording of natural human behaviour in a natural environment), (b) exploiting the potential of advanced ML algorithms to improve predictive performance on noisy sensor data of natural human behaviour, and (c) understanding the strengths of each of the smart devices in developing such predictive models. Therefore, our study is focused on the recognition of basic movement related activities such as walking, standing, sitting, exercise, and sleeping, that are essential for ambient assisted living or wellness management. We investigate advanced classification techniques and perform feature engineering for a natural, unobtrusive, and multimodal HAR system proposed in this paper for activity-based wellness management. One of the goals of this rese is t improve the accuracy reported in previous studies for classification of basic movement activities obtained from the ExtraSensory data. Various classification algorithms such as logistic regression (LR) [15], multilayer perceptron (MLP) [10], neural network [13,20,21], SVM [7,13,20,22], Naïve Bayes [19,23], for HAR. In this study, we choose three boosting algorithms, namely XgBoost, AdaBoost, and Boosted C5.0, for the same purpose. XgBoost is a relatively new technique and has gained popularity in recent times because of its scalability and accuracy for solving a wide range of prediction problems [24]. AdaBoost is one of the oldest and most popular boosting algorithms, which has shown excellent performance on real-world data [25]. Boosted C5.0 is largely known for its commercial use with scant attention from the academic community, but has been regarded as one of the best decision tree classifiers [26,27].

## Table 1

A summary of related literature

<table><tr><td>Topics studied</td><td>Research approach</td><td>Algorithms used</td><td>Research limitations</td></tr></table>

Journal Pre-proof

<table><tr><td>Activity</td><td>Data collection from</td><td>Self-learning</td><td>Controlled placement of</td></tr><tr><td>recognition for</td><td>two patients</td><td>activity</td><td>devices in different locations</td></tr><tr><td>lifestyle</td><td>performing activities</td><td>recognition</td><td>[12,16]</td></tr><tr><td>monitoring</td><td>(for 5 minutes) in a</td><td>scheme using</td><td>Arbitrary orientation of the</td></tr><tr><td>using</td><td>laboratory setup [12]</td><td>random forest and</td><td>phone in pockets [12]</td></tr><tr><td>smartphone</td><td>Naturally obtained</td><td>SVM classifiers</td><td>Participants&#x27; behaviour is</td></tr><tr><td>sensors</td><td>dataset from eight</td><td>[12]</td><td>scripted and instructed [12]</td></tr><tr><td></td><td>subjects following</td><td>Bayesian learning</td><td>A small number of</td></tr><tr><td></td><td>daily routine for eight</td><td>based approach</td><td>participants taking part in the</td></tr><tr><td></td><td>weeks [16]</td><td>[16]</td><td>experiment [12,16]</td></tr><tr><td rowspan="2">Monitoring of human activity</td><td>Recording scripted</td><td>Multi-layer</td><td>Unusual and inconvenient</td></tr><tr><td>activities (each for 10</td><td>reception, neural</td><td>number and location of</td></tr><tr><td>using Chronos</td><td>minutes) of twelve</td><td>network, and SVM</td><td>sensing apparatus [13,19]</td></tr><tr><td>watch sensors</td><td>elderly participants</td><td>with feature</td><td>Controlled laboratory setup</td></tr><tr><td></td><td>[13]</td><td>selection [13]</td><td>for data collection [13,19]</td></tr><tr><td></td><td>Recordings of activities</td><td>Naïve Bayes</td><td></td></tr><tr><td></td><td>(each repeated 125 times</td><td>classifier and</td><td></td></tr><tr><td></td><td>by a person) using</td><td>hidden markov</td><td></td></tr><tr><td></td><td>watches worn on ankle,</td><td>model [19]</td><td></td></tr><tr><td></td><td>thigh, or wrist [19]</td><td></td><td></td></tr><tr><td>Activity</td><td>Sensor data for scripted</td><td>Random forest,</td><td>Unnatural placement of</td></tr><tr><td>recognition</td><td>activities of nine users</td><td>hidden markov</td><td>devices and controlled</td></tr><tr><td>using</td><td>each carrying eight</td><td>model, and deep</td><td>conditions during data</td></tr><tr><td>smartphones</td><td>smartphones and four</td><td>learning [14]</td><td>collection [14]</td></tr></table>

and smartwatches [14] Logistic regression Scope of improvement in smartwatches and multi-layer activity prediction Sensor data from the perceptron [15] performance using advanced smartphone and the algorithms [15] smartwatch of 60 subjects during their A comparison of natural behaviour for a performance between week in their natural smartphone and smartwatch environment [15] in activity recognition is not

## 3. HAR System Using Motion Sensors of Smart Devices

## 3.1. Prediction Models for HAR

## 3.1.1. Data Description

We use the publicly available Extrasensory dataset [15] to build predictive models. The dataset is 20-second recording ses n ever and the smartwatch. The measurements from a single recording session are aggregated using different statistical measures. These aggregate measurements form the values of attributes corresponding to a single data point in the Extrasensory dataset. The interface of the mobile application provides a flexible and convenient mechanism for users to report labels describing their activity and context. The self-reported labels for every minute represent the context labels for a single data point that reflect the ground truth.

The Extrasensory dataset has 308,320 labelled examples from 60 users. Each example represents a time period of one minute and has aggregate measurements from different sensors on the smartphone and the smartwatch. For our analysis, we focus on the recordings obtained from five core sensors as follows:

Smartphone Measurements – The smartphone sensors considered in the dataset are accelerometer, gyroscope, and magnetometer. In the Extrasensory application, each of these sensors is sampled at 40 Hz during the 20-second recording session to produce raw sensor measurements of 800 time points.

Smartwatch Measurements – The smartwatch sensors considered in our study are accelerometer and compass. The accelerometer is sampled at 25 Hz during the 20-second recording session to produce raw sensor measurements of 500 time points. The compass does not have a constant more than one degree. All sensors are not available at all times. For example, the smartwatch is not worn by the participants all the time. In fact, four users refused to wear the smartwatch.

Table 2 shows the details of various sensors and the distribution of a number of labelled examples across those sensors that are used in the analysis. In Table 2, the number of users denote those users with the particular sensor information available on their device and the number of examples corresponding to the sensor represent the number of minutes of activities recorded by the sensor. We consider the ground truth walking, standing, sittin for each of the context labels is shown in Table 3. In Table 3, the number of users and the number of examples corresponding to the activity denote the number of users who have reported the activity at least once and the total number of minutes the users have engaged in the activity.

## Table 2

Different sensors, the format of their measurements, and the total number of labelled examples and users that have reported measurements from each sensor.

<table><tr><td>Sensor</td><td>Details</td><td>Dimension</td><td>Number of users</td><td>Number of examples</td></tr><tr><td>Accelerometer</td><td>Tri-axial direction and magnitude of</td><td>(~800) x 3</td><td>60</td><td>308,306</td></tr></table>

Gyroscope Rate of rotation around phone's 3 axes. (\~800) x 3 57 291,883 Sampled at 40 Hz for 20 seconds.

Magnetometer Tri-axial direction and magnitude of (\~800) x 3 58 282,527 magnetic field. Sampled at 40 Hz for 20 seconds.

Smartwatch Tri-axial acceleration from the watch. (\~500) x 3 56 210,716

Smartwatch Watch heading (degrees). N x 1 53 126,781

## Table 3

The number of users and examples corresponding to each label.

<table><tr><td>Label</td><td>Number of users</td><td>Number of examples</td><td>Number of examples after eliminating data points with missing information</td></tr><tr><td>Walking</td><td>60</td><td>22136</td><td>8933</td></tr><tr><td>Standing</td><td>60</td><td>37782</td><td>15701</td></tr><tr><td>Sitting</td><td>60</td><td>136356</td><td>55357</td></tr><tr><td>Exercise</td><td>44</td><td>8081</td><td>3798</td></tr><tr><td>Sleeping</td><td>53</td><td>83055</td><td>21922</td></tr></table>

## 3.1.2. Feature Extraction

The public dataset has provided specific features (i.e., aggregate measurements) for each sensor obtained from its raw measurements. Table 4 provides the pre-computed features available in the dataset. We use these features for the model building activity. There are 138 features in total. Since our feature space is large, we conduct feature engineering by identifying the important features that can contribute to improving the performance of the algorithm. The method of feature engineering is discussed later.

## Table 4

Description of data attributes that are reported in the Extrasensory dataset.

<table><tr><td>Sensor name</td><td>Number of features extracted</td><td>Feature type</td><td>Feature details</td></tr><tr><td>Accelerometer, gyroscope, magnetometer present in the smartphone and accelerometer present in the smartwatch</td><td>26 each</td><td>Magnitude signal*</td><td>Mean, standard deviation,  $3^{rd}$  moment,  $4^{th}$  moment,  $25^{th}$  percentile,  $50^{th}$  percentile,  $75^{th}$  percentileValue entropy – The entropy calculated from a histogram of quantization of the magnitude values to 20 binsTime entropy – The entropy obtained by normalizing the magnitude signal and treating it as a probability distribution designed to detect the sudden bursts of magnitude.Six spectral features – Log energies in 5 sub-bands (0-0.5 Hz, 0.5-1 Hz, 1-3 Hz, 3-5 Hz, &gt;5 Hz) and spectral entropy</td></tr></table>

<table><tr><td></td><td></td><td>• Two autocorrelation features</td></tr><tr><td></td><td>Direction vector</td><td>• Mean and standard deviation of each axis3 inter-axis correlation coefficients</td></tr><tr><td>Magnetometer in the smartphone</td><td>Direction vector</td><td>• 5 relative direction features using cosine-similarity</td></tr><tr><td>Smartwatch accelerometer</td><td>20 Direction vector</td><td>• Log energies in 5 sub-bands (0-0.5 Hz, 0.5-1 Hz, 1-3 Hz, 3-5 Hz, &gt;5 Hz) for each axis5 relative direction features using cosine-similarity</td></tr><tr><td>Smartwatch compass</td><td>9 Degree of an angle</td><td>• Mean, standard deviation,  $3^{rd}$  moment, and  $4^{th}$  moment of sine and cosine values of the angles• Entropy using 8 bins</td></tr></table>

\* The Euclidean norm of the 3-axis measurements (i.e., $a [ \mathrm { t } ] { = } \sqrt { \mathsf { a } _ { \mathrm { x } } [ \mathrm { t } ] ^ { 2 } + \mathsf { a } _ { \mathrm { y } } [ \mathrm { t } ] ^ { 2 } + \mathsf { a } _ { \mathrm { z } } [ \mathrm { t } ] ^ { 2 } } ) $ at each point in time is used to calculate the magnitude of the sensor readings.

## 3.1.3. Data Preparation

We use one-versus-all classification algorithms for prediction. Therefore, we add a column in the existing dataset corresponding to each of the activities, including walking, standing, sitting, exercise, and sleeping. Each of these columns has a binary outcome, which is 1 if the activity has been reported and 0 otherwise. Different classifiers are trained and tested for each of these outcome variables. After this, we remove the data points with missing sensor information. We use 130,670 data points for subsequent analysis.

As a data pre-processing step, we perform feature scaling by normalizing every feature of the dataset. Subsequently, we create a data partition with 60% belonging to t he training set and the rest belonging to the testing set. The data partition is random and is performed in such a way that the ratio of the outcome classes is nearly identical in both the sets. The data is partitioned each time before a new classifier is modelled. To avoid the problem of class imbalance, we use the method of undersampling before training any classifiers. Undersampling removes random examples of the majority class in the dataset until it has the same frequency as the minority class. It has an advantage over any other sampling method since it can save computation time while training a large set without compromising the performance of the algorithm [29]. For the large sample of data points, undersampling is a suitable choice to avoid highly skewed class distributions.

## 3.1.4. Classification Algorithms for Model Building

Our study focuses on boosting, which is considered to be a popular ensemble learning technique [30]. Ensemble learning involves a systematic solution based on the combined predictive power of multiple learners. Boosting is a widely used ensemble learner, where decision trees are sequentially built so that each subsequent tree reduces the classification errors of the previous tree. The multiple decision trees are considered to be weak learners<sup>1</sup>, whose results are combined to produce a strong learner for classification [30]. Boosting algorithms have emerged as one of the most promising approaches for supervised learning in the last two decades [31]. It has been extensively used in the areas of credit risk modelling, customer churn prediction, and stock index forecasting [32–34]. To develop predictive models for HAR, we investigate three classification algorithms based on boosting. A brief description of these three algorithms follows:

Extreme Gradient Boosting (XgBoost) – It is a popular boosting method developed in 2016 [24]. It is an approach where the weak learner tries to fit a new predictor to the residual error of the previous learner and sequentially reduces the classification errors of previous learners. Then, all learners are aggregated for the final prediction. XgBoost is based on gradient boosting. When the boosting uses gradient descent techniques to minimize the loss function while adding new models, it is called gradient boosting. In addition to the gradient boosting framework, XgBoost implements system optimization and algorithmic enhancements such as scalability, out-of-core computing, regularization, etc. It also implements two techniques to prevent overfitting – shrinkage (similar to the learning rate in stochastic optimization) and column (feature) subsampling [24]. In this study, we include maximum depth of the tree (to control the plexity of each tree), subsample ratio of training instances, and number of boosting iterations.

training simple decision trees using different weightings for the same training set [35,36]. The weights for each data point in the training set are adjusted in an iteration based on the actual performance of the algorithm in the previous iteration. The final classifier is a strong and composite classifier built from the linear combination of several weak learners. The weight of each weak learner in the linear combination is adjusted according to their misclassification rate. The number of tree classifiers to be considered for boosting is an input parameter. Therefore, it has been used as a tuning parameter for our study. Moreover, there are two simple versions of AdaBoost – AdaBoost.M1, and SAMME [35]. During model validation, the AdaBoost algorithm has been tuned to pick the optimum version in terms of the performance measure.

Boosted C5.0 – It is an extension of the C4.5 algorithm [37]. It is one of the most practical methods for inductive inference, where the learned function is represented by decision trees. The branches in the decision trees are split based on the discrete classification of input nodes, which gives the maximum information gain. An important feature of Boosted C5.0 is that the learned trees can also be reduced to rule sets (an unordered collection of simple if-then rules) for simplicity. Moreover, Boosted C5.0 provides the feature of adaptive boosting, where several classifiers are generated in a number of iterations. If the first classifier in the first iteration wrongly classifies n cases, then the second classifier in the second iteration is constructed to improve the classification rate for these n cases. This process continues until the pre-determined number of iterations is reached. For identification of new cases, the votes from each classifier are added to decide the final class. In this study, a logical parameter to decide the transformation of decision trees into rule sets, and an integer parameter to decide the number of iterations for boosting have been used as tuning parameters for model validation.

## 3.1.5. Experimental Results of Classification

The classification models are developed using the classification algorithms as described in the sleeping. In this section, we describe the results of the performance of all classifiers using 138 features.

Model Validation – We use bootstrapping [38] on the training set for model validation for tuning the model parameters [39]. It is the process where the model is trained on the dataset obtained using random sampling with replacement from the original dataset. The data points that are not used for training the model are used for estimating the performance of the model. This process is repeated several times, and the average performance score is computed for each combination of tuning parameters for a classification model. To get a performance score during model validation, we obtain the receiver operating characteristic (ROC) curve. The ROC curve is a graphical plot of true positive rate against the false positive rate at various discrimination thresholds for the classifier. The area under ROC (AUC) is a popular performance measure for classification algorithms [40]. Therefore, the set of parameters leading to the highest AUC is chosen for the model before using it on the testing dataset.

Model Testing – For a comparative analysis of performance for different classifiers on the testing dataset, we consider two performance metrics as shown below:

F1 Score: It is the harmonic mean of recall and precision. It resembles a score emphasizing false negatives and false positives. With reference to the confusion mat $\mathbf { \{ } \mathbf { X } , $ as shown below:

$$
\text { Recall } = \frac {\text { True   Positive }}{\text { True   Positive } + \text { False   Negative }}
$$

$$
P r e c i s i o n = \frac {T r u e P o s i t i v e}{T r u e P o s i t i v e + F a l s e P o s i t i v e}
$$

Accuracy: It is the average of recall and specificity. It resembles a score emphasizing true positives and true negatives. With reference to the confusion matrix, specificity is denoted as:

$$
\Delta_ {P} \text {   specificity } = \frac {\text { True   Negative }}{\text { True   Negative } + \text { False   Positive }}
$$

The above two competing metrics are commonly used as robust performance measures for classification algorithms [15]. These metrics are also suitable for tackling the problem of class imbalance [41]. Table 5 provides the performance scores of each algorithm for a variety of classification tasks.

## Table 5

Performance scores of boosting-based algorithms (using 138 features) for classification of five different human activities.

<table><tr><td>Activity</td><td>Classification</td><td>Model validation</td><td>Model testing</td></tr></table>

<table><tr><td></td><td>algorithm</td><td>AUC for optimal model</td><td>Accuracy</td><td>F1 Score</td></tr><tr><td rowspan="3">Walking</td><td>XgBoost</td><td>0.92</td><td>0.85</td><td>0.43</td></tr><tr><td>AdaBoost</td><td>0.93</td><td>0.87</td><td>0.45</td></tr><tr><td>Boosted C5.0</td><td>0.92</td><td>0.86</td><td>0.42</td></tr><tr><td rowspan="3">Standing</td><td>XgBoost</td><td>0.87</td><td>0.79</td><td>0.47</td></tr><tr><td>AdaBoost</td><td>0.90</td><td>0.82</td><td>0.50</td></tr><tr><td>Boosted C5.0</td><td>0.89</td><td>0.81</td><td>0.50</td></tr><tr><td rowspan="3">Sitting</td><td>XgBoost</td><td>0.90</td><td>0.82</td><td>0.80</td></tr><tr><td>AdaBoost</td><td>0.94</td><td>0.87</td><td>0.85</td></tr><tr><td>Boosted C5.0</td><td>0.92</td><td>0.86</td><td>0.84</td></tr><tr><td rowspan="3">Exercise</td><td>XgBoost</td><td>0.98</td><td>0.92</td><td>0.41</td></tr><tr><td>AdaBoost</td><td>0.97</td><td>0.92</td><td>0.42</td></tr><tr><td>Boosted C5.0</td><td>0.97</td><td>0.92</td><td>0.40</td></tr><tr><td rowspan="3">Sleeping</td><td>XgBoost</td><td>0.99</td><td>0.96</td><td>0.89</td></tr><tr><td>AdaBoost</td><td>0.99</td><td>0.96</td><td>0.91</td></tr><tr><td>Boosted C5.0</td><td>0.99</td><td>0.96</td><td>0.93</td></tr></table>

Note: Numbers in bold represent the best performance scores for a particular activity.

## 3.1.6. Feature Engineering

We attempt to improve the performance of the classification models using feature engineering. We use feature engineering only on the AdaBoost model (as shown in the previous section) since it outperformed all other techniques in predictive performance for most of the endeavours related to activity detection. The feature engineering has been performed in two steps as described below:

Comparing the Ability of the Smartphone and the Smartwatch in HAR (Step 1) – In the first step, the features are selected based on the choice of smart devices for HAR. The classification model for each activity is retrained twice, first based on the sensor features extracted from the smartphone and second based on the sensor features extracted from the smartwatch. Then, we compare the predictive performance using the smartphone sensor features versus the smartwatch sensor features on the test dataset.

Feature Engineering based on the Importance of Features (Step 2) – In the second step, the importance of features is calculated for each of the activities. For AdaBoost, the importance of a predictor is a function of the gain of the Gini index achieved by the predictor in a tree, and the weight of the tree [35]. Gini index is a widely used impurity measure for decision trees [42]. Therefore, the aggregated value of the weight of the boosted trees along with the Gini gain for a e scores are scaled to a maximum value of 100. Then, for each activity, the models are retrained (one each corresponding to the two devices) recursively after selecting features each time, based on the threshold value of importance scores. At each iteration, the threshold value is decreased by a step size of 5 and the ROC is calculated. Finally, for each device, we select the best set of features and test the performance of the model on the test dataset.

Figure 2 shows the performance scores of the classification models corresponding to each of the devices before and after feature engineering. In this figure, we also show the performance scores for the models when the features from both the devices are combined together. Table 6 shows the distribution of features across sensors after feature engineering for both devices.

WALKING  
![](/api/attachments/48A63D8C/fulltext/images/2404c731dd40390b68964e86fcf66ff6213e150601df9deed1984615f0c5aafb.jpg)

![](/api/attachments/48A63D8C/fulltext/images/d853a5b38423c024a7da0798e22520fd30897a8d99844327c80156e3dd6f975e.jpg)

![](/api/attachments/48A63D8C/fulltext/images/1da9e7b0ab214b4b0793e531762c7cd77d2e5dae8ef5015087887fd277498e63.jpg)  
Figure 2 A comparison of performance scores of the AdaBoost model  
for different types of feature engineering

Table 6  
Distribution of features across sensors after feature engineering

<table><tr><td colspan="3">Activity</td><td colspan="3">Smartphone</td><td colspan="2">Smartwatch</td></tr><tr><td></td><td>A</td><td>G</td><td>M</td><td>Total</td><td>A</td><td>C</td><td>Total</td></tr><tr><td>Walking</td><td>9</td><td>1</td><td>4</td><td>14</td><td>13</td><td>0</td><td>13</td></tr><tr><td>Standing</td><td>4</td><td>0</td><td>2</td><td>6</td><td>18</td><td>3</td><td>21</td></tr><tr><td>Sitting</td><td>4</td><td>5</td><td>3</td><td>7</td><td>15</td><td>2</td><td>17</td></tr><tr><td>Exercise</td><td>4</td><td>0</td><td>3</td><td>7</td><td>15</td><td>2</td><td>17</td></tr><tr><td>Sleeping</td><td>4</td><td>0</td><td>3</td><td>7</td><td>14</td><td>2</td><td>16</td></tr></table>

Note: A – Accelerometer, G – Gyroscope, M – Magnetometer, C – Compass

## 4. Discussion

This study proposes a HAR system using smart devices or wearables. The task of human activity classification is an integral part of our research model. As shown in Figure 1, this study focuses on predictive modelling of human activity using real-time data from the wireless sensor networks of smart devices. We use a publicly available dataset representing real-time sensor data on human activities collected under natural conditions to analyse the performance of various boosting algorithms in classification of human activities.

## 4.1. Performance of Boosting Models for HAR

For the classification of basic movement activities, we observe that the boosted tree-based classifiers show an excellent performance in terms of accuracy. In terms of the F1 score, the results are not compelling, but it surpasses those obtained in previous studies. We discuss this in detail in a later section. With the exception of the activity „sleeping‟, AdaBoost is the best performing algorithm for all classification tasks when the model is trained using the complete set of 138 features (see Table 5). Boosted C5.0 marginally outperforms AdaBoost in the prediction of „sleeping‟.

For the sake of understanding the contribution of features from various devices in HAR and improving the classification performance, we use feature engineering. We observe that the AdaBoost the prediction of all types of activities. With the help of feature engineering for smartphone sensor and shows the best outcome for all but two activities (namely, walking and exercise) (see Figure 2). In this smartphone-based model with feature engineering, the accelerometer and magnetometer related sensors contribute significantly to the superior performance (see Table 6). In case of the smartwatch-based model, feature engineering does not demonstrate any significant improvement in the performance of the model. However, for the activities „walking‟ and „exercise‟, the model with a combination of the best features from both devices outperform the rest. In this particular model, watch accelerometer plays an integral role apart from the phone accelerometer and phone magnetometer in determining predictive accuracy.

The real-time classification of human activity entails repeated training and validation of predictive models with the addition of new data to the existing data. This involves a high computational load. To ease the computation, AdaBoost with feature engineering can be a model of choice for HAR. The successive training and validation of the predictive model on a small number of features can significantly reduce the run time and the computation load for model building. Moreover, in terms of devices, it is observed that the smartphone outperforms the smartwatch in HAR. In fact, for most of the activities, the smartphone as a standalone sensing device can do a better job than the combination of smart devices. In case the sensor data of the smartphone is not available for some users, or it is inconvenient and uneconomical to extract, the smartwatch can be a viable tool for HAR in a wellness management system with a compromise on predictive performance for most activities.

## 4.2. Comparison with Standard Machine Learning Algorithms: Robustness Checks

We test the performance of standard ML algorithms such as Neural Network and SVM on the same dataset to compare their efficacy with that of the boosting algorithms. These ML algorithms serve as [12,13,21]. These techniques are frequently used in several areas of pattern recognition [43,44]. A brief description of the standard ML algorithms is provided in the Appendix.

## Table 7

Performance scores of standard ML algorithms for classification of five different activities.

<table><tr><td rowspan="2">Activity</td><td rowspan="2">Classification algorithm</td><td colspan="2">Model validation</td><td>Model testing</td></tr><tr><td>AUC for optimal model</td><td>Accuracy</td><td>F1 Score</td></tr><tr><td rowspan="4">Walking</td><td>Neural Network</td><td>0.87</td><td>0.80</td><td>0.36</td></tr><tr><td>SVM</td><td>0.90</td><td>0.83</td><td>0.40</td></tr><tr><td>LR [15]*</td><td>-</td><td>0.80</td><td>0.39</td></tr><tr><td>MLP [10]*</td><td>-</td><td>0.81</td><td>-</td></tr><tr><td rowspan="4">Standing</td><td>Neural Network</td><td>0.77</td><td>0.72</td><td>0.38</td></tr><tr><td>SVM</td><td>0.83</td><td>0.75</td><td>0.43</td></tr><tr><td>LR [15]*</td><td>-</td><td>0.68</td><td>0.36</td></tr><tr><td>MLP [10]*</td><td>-</td><td>0.68</td><td>-</td></tr><tr><td>Sitting</td><td>Neural Network</td><td>0.81</td><td>0.76</td><td>0.73</td></tr><tr><td colspan="5">Journal Pre-proof</td></tr><tr><td></td><td>SVM</td><td>0.86</td><td>0.79</td><td>0.76</td></tr><tr><td></td><td>LR [15]*</td><td>-</td><td>0.76</td><td>0.75</td></tr><tr><td></td><td>MLP [10]*</td><td>-</td><td>0.77</td><td>-</td></tr><tr><td>Exercise</td><td>Neural Network</td><td>0.89</td><td>0.83</td><td>0.21</td></tr><tr><td></td><td>SVM</td><td>0.94</td><td>0.88</td><td>0.31</td></tr><tr><td></td><td>LR [15]*</td><td>-</td><td>0.81</td><td>0.27</td></tr><tr><td></td><td>MLP [10]*</td><td>-</td><td>0.83</td><td>-</td></tr><tr><td>Sleeping</td><td>Neural Network</td><td>0.94</td><td>0.89</td><td>0.72</td></tr><tr><td></td><td>SVM</td><td>0.96</td><td>0.91</td><td>0.78</td></tr><tr><td></td><td>LR [15]*</td><td>-</td><td>0.82</td><td>0.81</td></tr><tr><td></td><td>MLP [10]*</td><td>-</td><td>0.90</td><td>-</td></tr></table>

according to the best performing algorithm reported in the paper.  
Note: The numbers in bold denote the best performance scores for a particular activity.

Table 7 presents the classification scores of the ML algorithms like Neural Networks and SVM for the complete set of 138 features. In addition, we provide the results of classification that are obtained using other standard ML algorithms in extant research [10,15]. Comparing Table 7 with Table 5, we observe that all boosting algorithms such as Boosted C5.0, XgBoost, and AdaBoost have a higher accuracy and F1 score for HAR as compared to the standard ML approaches (such as Neural Networks, SVM, MLP, and LR). We also observe that SVM performs relatively better among the standard ML algorithms. To summarize, we can say that the boosted classification trees provide the best predictive modelling of HAR using sensor data.

## 4.3. Decision Support System Based on HAR

HAR using advanced ML methods on motion sensors of smart devices can facilitate context-specific persuasion mechanisms for wellness management through their user interfaces. For example, the system can use the persuasion strategy of activity self-monitoring, where the users are notified of their progress on prescribed health-related activities to persuade them in completing their goals. The system designers can use digital assets of gamification such as badges, certificates, or reward points for persuasion. Moreover, the system can urge the user to complete his goal and share the success story in the online social platform comprising peer networks. The social platform can track the progress of each user, create leader boards for comparison, and allow participants to compete with each other. Such intervention can encourage and reinforce the active participation of users in wellness management.

Another example can be expert suggestions, where the underlying assumption is that information is most effective in changing user‟s behaviour if presented at the right time. During a particular activity, if relevant suggestions from medical or fitness experts are presented to the user, they are more likely to be effective for the users. For activity-based wellness management, the behavioural context and the persuasion strategies need to be aligned for countering non-adherence and achieving the HAR system for wellness management and clarify the link between predictive analytics and context-aware wellness services through persuasive user interfaces.

## 5. Implications

## 5.1. Implications for research

Most of the studies related to HAR have analysed the data collected in a laboratory setting. Such data are oversimplified representation of the real-life situation. The classification models tested using these data often underperform in practical situations. Therefore, it is essential to obtain data generated under natural settings. Our study fulfils this purpose by conducting research on available natural data on human activities.

This study has implications for researchers analysing real-world data. Sensor data recording natural behaviour is susceptible to noise. The noisy data complicates the problem of classification. Our study establishes the superior performance of powerful boosting methods over traditional ML techniques in the presence of noisy data. The performance is substantially improved with the help of feature engineering, and the role of sensor features in the performance improvement of different HAR is highlighted. This is significant as “a small improvement in analytical performance can result in substantial profit gains or cost savings” [45]. Moreover, advanced boosting algorithms can also be investigated for achieving better predictive performance.

Our study contributes towards the conceptualization of a HAR system using sensor readings from commonly used devices such as smartwatches or smartphones. The novelty of the research model lies in the unobtrusive mechanism to extract the knowledge, identify the behavioural context, and leveraged for large scale implementation of HAR system and its associated wellness measures for physical well-being.

## 5.2. Implications for practitioners

There are several implications of our research for wellness providers. Firstly, our proposed research model closely resembles a smart home solution for assisted living or activity-based wellness management. The wellness providers $\mathbf { a } , \mathbf { \mu } ^ { \mathbf { q } } \mathbf { V }$ benefit from learning about the possible real-world implementation of a HAR system u $\sin _ { \ z }$ smart devices. Moreover, our research informs them about how HAR can be useful context-aware persuasive strategies. These persuasive strategies can nudge users towards self-management of health conditions.

Secondly, this study illustrates how advanced ML techniques facilitate the creation of an intelligent environment that monitors user activities. The intelligent environment encompassing the users can help them take wellness related decisions based on their progress in a variety of activities. We believe the operationalization of the intelligent environment created by smart devices is a steppingstone towards the digital transformation of wellness management.

Thirdly, this study shows that the smartphone alone can be an efficient device for recognition of basic movement activities in the natural environment. In the detection of activities such as standing, sitting, and sleeping, the smartphone sensors (particularly the accelerometer and magnetometer)

shows maximum efficacy for accurate HAR. For the other basic movement activities, smartphone sensors show satisfactory performance. To ensure cost-effectiveness and to avoid the complexity in data integration from various sensor-based devices, the smartphone can be an effective choice for HAR under natural conditions. On the other hand, the smartwatch alone may be an appropriate choice for HAR when the use of the smartphone is either not possible or it is not conveniently available as a part of wellness management program for some users. For example, a user may not carry the smartphone everywhere or may not allow the phone sensors to transfer data to a HAR useful for wellness management. Moreover, the combination of the smartwatch and the smartphone can make up a robust HAR system for all users.

Fourthly, apart from the wellness providers, our research informs the practitioners in the wearables industry about the potential of sensor-based devices in forming an interconnected digital ecosystem. Things (IoT) enabled devices, and offer personalised and innovative services to users connected to the ecosystem.

## 6. Conclusion

collected under natural settings for predictive modelling of five basic movement activities – walking, standing, sitting, exercise, and sleeping. We find that the boosted trees perform better on such realworld data compared to other popular ML techniques. With the help of feature engineering, the performance of a boosting algorithm can be further improved. The smartphone sensor features play a major role in the improvement. Overall, the boosting model with feature engineering applied to sensor features from both the devices provides insights about the most suitable algorithmic implementation of HAR in the natural environment. Moreover, we propose a HAR system for realtime implementation of an unobtrusive and intelligent system for managing human activity through persuasive approaches to wellness recommendations.

Future research needs to establish the efficacy of such a HAR system in promoting wellness management. As conceptualized in this paper, we aim to develop the HAR system and empirically test its ability for self-care motivation through context-aware services. Also, researchers can build on our work to expand the boundaries of our research model to other IoT devices and test its feasibility. Multimedia data such as audio and video from wireless sensors networks of IoT devices can be powerful ML techniques. Other popular ML methods such as bagging and deep learning can be investigated in this context [46]. Through the use $\mathrm { { _ { o ^ { f } \bullet \bullet \bullet \mathbf { u } } } }$ intelligent system for HAR, future researchers can consider creating wellness communities based on similar profiles of activities. They Finally, they can study the effectivenes the activity-based wellness interventions on the improvements in health conditions of communit members

## Acknowledgement

The authors gratefully acknowledge the support received in the form of a Category II research grant with work order number xx from xx.

## Appendix

## Feed-Forward Neural Network with a Single Hidden Layer

It is the simplest form of artificial neural network where the input nodes are connected to the output nodes through one layer (called hidden layer) of connection objects (called neurons) [44]. The number of neurons determines the size of the hidden layer. This algorithm implements the function of the input nodes and the connection weights, and then, it adjusts the weight vector to optimize the error function of the output nodes. Further, to improve the generalization and to suppress the unnecessary connections, a weight decay approach is used [47]. In our study, the parameters for the size of the hidden layer and the weight decay are tuned during the model validation phase to obtain the best performance of the classifier.

## Support Vector Machine (SVM) with Radial Basis Function Kernel

SVM is capable of learning non-linear functions by projecting the input nodes into a higher dimensional space. Then, it separates the data based on their class labels by locating a hyperplane with maximal margin through optimization of the following objective function [43]:

$$
\min _ {w, b, \xi} \quad \frac {1}{2} \boldsymbol {w} ^ {\boldsymbol {T}} \boldsymbol {w} + C \sum_ {i = 1} ^ {l}.
$$

$$
\text { subject   to } \quad y _ {i} (\boldsymbol {w} ^ {T} \phi (\boldsymbol {x} _ {i}) \neg \xi) \geq 1 - \xi_ {i}; \xi_ {i} \geq 0
$$

The training vectors $\mathbf { X _ { i } } \in \mathbf { R ^ { n } }$ and the indicator $\mathrm { v e } \ \mathrm { \cdot } \mathrm { t o } \mathrm { \ } _ { \mathrm { \mathcal { J } } } \ \in \mathrm { \mathbb { R } } ^ { 1 }$ are such that $\mathrm { y _ { i } } \in \{ - 1 , 1 \} . \mathrm { C } > 0$ is the regularization parameter, and $\phi$ is the kernel function that maps $\mathbf { x _ { i } }$ into a higher-dimensional space. This study uses the radial basis function (RBF) as the kernel function. The RBF kernel is represented as follows:

$$
\phi \left(\boldsymbol {x} _ {i}\right) = e x p \left(- \frac {1}{2 \sigma^ {2}} \left. \begin{array}{l l} \prime & \\ \prime & - \lambda_ {j} \end{array} \right\| ^ {2}\right), \text {   where   } \sigma \text {   is   the   width   of   the   Gaussian   kernel }
$$

The parameters C and $\sigma , r e$ used to tune the SVM model for better predictive performance.

## References

[1] Global Wellness Institute, Wellness industry statistics and facts, (2018). https://globalwellnessinstitute.org/press-room/statistics-and-facts/ (accessed July 19, 2020).

[2] Gartner, Understand the value of AI for healthcare delivery organizations, (2018). https://www.gartner.com/document/3869974 (accessed July 19, 2020).

[3] P. Rashidi, A. Mihailidis, A survey on ambient-assisted living tools for older adults, IEEE Journal of Biomedical and Health Informatics. 17 (2013) 579–590.

[4] M. Rabbi, M.H. Aung, M. Zhang, T. Choudhury, MyBehavior: Automatic personalized health feedback from user behaviors and preferences using smartphones, in: ACM International Joint Conference on Pervasive and Ubiquitous Computing, 2015: pp. 707– 718.

[5] F. Buttussi, L. Chittaro, MOPET: A context-aware and user-adaptive wearable system for fitness training, Artificial Intelligence in Medicine. 42 (2008) 153–163.

[6] Ó.D. Lara, M.A. Labrador, A survey on human activity recognition using wearable sensors, IEEE Communications Surveys and Tutorials. 15 (2013) 1192–1209.

[7] A. Fleury, M. Vacher, N. Noury, SVM-based multimodal classification of activities of daily living in health smart homes: Sensors, algorithms, and first experimental results, IEEE Transactions on Information Technology in Biomedicine. 14 (2010) 274–283.

[8] J. Pärkkä, M. Ermes, P. Korpipää, J. Mäntyjärvi, J. Peltola, I. Korhonen, Activity Information Technology in Biomedicine. 10 (2006) 119–128.

[9] M.H. Khan, N. Roy, A. Misra, Scaling human activity recognition via deep learningbased domain adaptation, in: IEEE International Conference on Pervasive Computing and Communications, 2018: pp. 1–9.

[10] Y. Vaizman, N. Weibel, G. Lanckriet, Context recognition in-the-wild, Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies. 1 (2018) 1–22.

[11] Y. Wang, S. Cang, H. Yu, A survey on wearable sensor modality centred human activity recognition in health care, Expert Systems with Applications. 137 (2019) 167–190.

[12] J. Guo, X. Zhou, Y. Sun, G. Ping, G. Zhao, Z. Li, Smartphone-based patients‟ activity recognition by using a self-learning scheme for medical monitoring, Journal of Medical Systems. 40 (2016) 1–14.

[13] S. Chernbumroong, S. Cang, H. Yu, A practical multi-sensor activity recognition system for home-based care, Decision Support Systems. 66 (2014) 61–70.

[14] R. San-Segundo, H. Blunck, J. Moreno-Pimentel, A. Stisen, M. Gil-Martín, Robust human activity recognition using smartwatches and smartphones, Engineering Applications of Artificial Intelligence. 72 (2018) 190–202.

[15] Y. Vaizman, K. Ellis, G. Lanckriet, Recognizing detailed human context in the wild from smartphones and smartwatches, IEEE Pervasive Computing. 16 (2017) 62–74.

[16] R.K. Ganti, S. Srinivasan, A. Gacic, Multisensor fusion in smartphones for lifestyle monitoring, in: International Conference on Body Sensor Networks, 2010: pp. 36–43.

[17] A. Natarajan, Machine learning methods for personalized health monitoring using wearable sensors, PhD. Diss., University of Massachusetts Amherst. (2019) 1–141.

[18] R. Adams, Machine learning methods for activity detection in wearable sensor data streams, PhD. Diss., University of Massachusetts Amherst. (2018) 1–119.

[19] G. Uslu, H.I. Dursunoglu, O. Altun, S. Baydere, Human activity monitoring with wearable sensors and hybrid classifiers, International Journal of Computer Information Systems and Industrial Management Applications. 5 (2013) 345–353.

[20] S. Chernbumroong, S. Cang, A. Atkins, H. Yu, Elderly activities recognition and classification for applications in assisted living, Expert Systems with Applications. 40 (2013) 1662–1674.

[21] Z. Wang, M. Jiang, Y. Hu, H. Li, An incremental learning method based on probabilistic

neural networks and adjustable fuzzy clustering for human activity recognition by using wearable sensors, IEEE Transactions on Information Technology in Biomedicine. 16 (2012) 691–699.

[22] D. Fuentes, L. Gonzalez-Abril, C. Angulo, J.A. Ortega, Online motion recognition using an accelerometer in a mobile device, Expert Systems with Applications. 39 (2012) 2461– 2465.

[23] H. Martín, A.M. Bernardos, J. Iglesias, J.R. Casar, Activity logging using lightweight classification techniques in mobile devices, Personal and Ubiquitous Computing. 17 (2013) 675–695.

[24] T. Chen, C. Guestrin, XGBoost: A scalable tree boosting system, in: 22<sup>nd</sup> ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, San Francisco, California, USA, 2016: pp. 785–794.

[25] C. Zhang, Q. Cai, Y. Song, Boosting with pairwise constraints, Neurocomputing. 73 (2010) 908–919.

[26] D. Delen, H. Zaim, C. Kuzey, S. Zaim, A comparative analysis of machine learning systems for measuring the impact of knowledge management practices, Decision Support Systems. 54 (2013) 1150–1160.

[27] E. Pashaei, M. Ozen, N. Aydin, A novel gene selection algorithm for cancer identification based on random forest and particle swarm optimization, in: IEEE Conference on Computational Intelligence in Bioinformatics and Computational Biology, 2015: pp. 1–6.

[28] Y. Vaizman, K. Ellis, G. Lanckriet, N. Weibel, Extrasensory app: Data collection in-thewild with rich user interface to self-report behavior, in: CHI Conference on Human Factors in Computing Systems, New York, USA, 2018: pp. 1–12.

[29] Y. Liu, E. Shriberg, A. Stolcke, M. Harper, Using machine learning to cope with imbalanced classes in natural speech: Evidence from sentence boundary and disfluency detection, in: 8th International Conference on Spoken Language Processing, 2004: pp. 1525–1528.

[30] G. Wang, J. Sun, J. Ma, K. Xu, J. Gu, Sentiment classification: The contribution of ensemble learning, Decision Support Systems. 57 (2014) 77–93.

[31] A. Mayr, H. Binder, O. Gefeller, M. Schmid, The evolution of boosting algorithms: From machine learning to statistical modelling, Methods of Information in Medicine. 53 (2014) 419–427.

[32] S. Feuerriegel, J. Gordon, Long-term stock index forecasting based on text mining of regulatory disclosures, Decision Support Systems. 112 (2018) 88–97.

[33] M. Papouskova, P. Hajek, Two-stage consumer credit risk modelling using heterogeneous ensemble learning, Decision Support Systems. 118 (2019) 33–45.

[34] K. Coussement, S. Lessmann, G. Verstraeten, A comparative analysis of data preparation industry, Decision Support Systems. 95 (2017) 27–36.

[35] E. Alfaro, M. Gáamez, N. García, Adabag: An R package for classification with boosting and bagging, Journal of Statistical Software. 54 (2013) 1–35.

[36] Y. Freund, R.E. Schapire, Experiments with a new boosting algorithm, in: Thirteenth International Conference on Machine Learning, San Francisco, CA, USA, 1996: pp. 148– 156.

[37] J.R. Quinlan, C4.5: Programs for machine learning, Morgan Kaufmann Publishers Inc., San Francisco, CA, USA, 1993.

[38] B. Efron, R.J. Tibshirani, An introduction to the bootstrap, Chapman & Hall, New York, 1993.

[39] T. Van Gestel, J.A.K. Suykens, B. Baesens, S. Viaene, J. Vanthienen, G. Dedene, B. De Moor, J. Vandewalle, Benchmarking least squares support vector machine classifiers, Machine Learning. 54 (2004) 5–32.

[40] A.P. Bradley, The use of the area under the ROC curve in the evaluation of machine learning algorithms, Pattern Recognition. 30 (1997) 1145–1159.

[41] A. Tharwat, Classification assessment methods, Applied Computing and Informatics. (2018) 1–13.

[42] C. Strobl, A.L. Boulesteix, T. Augustin, Unbiased split selection for classification trees based on the Gini index, Computational Statistics and Data Analysis. 52 (2007) 483–501.

[43] C.C. Chang, C.J. Lin, LIBSVM: A library for support vector machines, ACM Transactions on Intelligent Systems and Technology. 2 (2011) 1–39.

[44] B.D. Ripley, Pattern recognition and neural networks, Cambridge University Press, New York, USA, 1996.

[45] B. Baesens, R. Bapna, J.R. Marsden, J. Vanthienen, J.L. Zhao, Transformational issues of big data and analytics in networked business, MIS Quarterly. 40 (2016) 807–818.

[46] M. Kraus, S. Feuerriegel, Decision support from financial disclosures with deep neural networks and transfer learning, Decision Support Systems. 104 (2017) 38–48.

[47] A. Krogh, J.A. Hertz, A simple weight decay can improve generalization, in: 4th International Conference on Neural Information Processing Systems, Denver, Colorado, 1991: pp. 950–957.

![](/api/attachments/48A63D8C/fulltext/images/667fd5c36183fedaf7e619a765f4ded05c0fcb10669d4d7a8fa4178e1437392e.jpg)

Pratik Tarafdar is a doctoral student of Management Information Systems at the Indian Institute of Management Calcutta. He holds an M. Sc. degree in Applied Mathematics from University of Calcutta. His research interests include cybersecurity, immersive technology, business analytics, machine learning, and human-computer interaction. His research articles have appeared in Journal of Organizational Computing and Electronic Commerce and conference proceedings of International Conference on Information Systems and ACM SIGMIS.

![](/api/attachments/48A63D8C/fulltext/images/dbba663271a21130b0ea67640500b9f97bfcce6297f335af53f2e06aa17b0f3f.jpg)

Indranil Bose is Professor of Management Information Systems at the Indian Institute of Management, Calcutta. He acts as Coordinator of IIMC Case Research Centre. He holds a BTech from the Indian Institute of Technology, MS from the University of Iowa, and MS and PhD from Purdue University. His research interests are in business analytics, digital transformation, information security, and management of innovation. His publications have appeared in MIS Quarterly, Journal of the MIS, Communications of the ACM, Communications of the AIS, Computers and Operations Research, Decision Support Systems, Electronic Markets, Ergonomics, European Journal of Operational Research, Information & Management, International Journal of Production Economics, Journal of Organizational Computing and Electronic Commerce, Journal of the American Society for Information Science and Technology, Operations Research Letters, Technological Forecasting and Social Change, etc. He serves as Senior Editor of Decision Support Systems and Pacific Asia Journal of the AIS, and as Associate Editor of Communications of the AIS, Information & Management, and Journal of the AIS.

The authors do not wish to include any author contribution statement for the paper.

## Highlights

 Human activity recognition is an important constituent for wellness management.

 Machine learning can be used for predicting human activities based on sensor data.

 Boosting methods show high predictive accuracy for human activity recognition.

 Feature engineering determines the importance of specific sensor data for different activities.

![](/api/attachments/48A63D8C/fulltext/images/e6a6d820113f4acd106a4714cd4b68ca3ad9e58255d3834ab27d179188cd76ec.jpg)  
Figure 1

WALKING  
![](/api/attachments/48A63D8C/fulltext/images/a39dc4345196864b1edac5d55e654b199f69d9aa1af73a3ba2a9bb29ed1a2607.jpg)  
SITTING

![](/api/attachments/48A63D8C/fulltext/images/493fa833795b9e576855c9a4cf3437295c482f282149f04cea9e1ccee0615f24.jpg)

STANDING  
![](/api/attachments/48A63D8C/fulltext/images/418063cb29d078605b807ebcbfc5174910f8781d4de1dcd9673ce0a424924f7e.jpg)  
EXERCISE

![](/api/attachments/48A63D8C/fulltext/images/a68fbe60083a0d5da9b38afc8062a39f6548afeaebe783881c93132f2611ece2.jpg)

SLEEPING  
![](/api/attachments/48A63D8C/fulltext/images/4050b09d46f3205a7d906f122536124b314c4505a8e494e5fa3bdb7a1e4978d7.jpg)
