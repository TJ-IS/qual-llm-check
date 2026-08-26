---
otero_id: 9968
otero_key: "3SAZ655U"
title: "A practical multi-sensor activity recognition system for home-based care"
authors: "Saisakul Chernbumroong; Shuang Cang; Hongnian Yu"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.06.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A practical multi-sensor activity recognition system for home-based care

Saisakul Chernbumroong <sup>a</sup>, Shuang Cang <sup>b</sup>, Hongnian Yu <sup>a,</sup>⁎

![](/api/attachments/3SAZ655U/fulltext/images/3c24bade83441f17648071015c9dce36a5ce6c3ae167e921fda193b7a0c3237c.jpg)

<sup>a</sup> Faculty of Science and Technology, Bournemouth University, Fern Barrow, Poole, Dorset BH12 5BB, United Kingdom

<sup>b</sup> School of Tourism, Bournemouth University, Fern Barrow, Poole, Dorset BH12 5BB, United Kingdom

## a r t i c l e i n f o

Article history: Received 6 November 2013 Received in revised form 16 April 2014 Accepted 7 June 2014 Available online 26 June 2014

Keywords: Multi-sensor activity recognition Home-based care Feature selection Classi<sup>fi</sup>cation Mutual information

## a b s t r a c t

To cope with the increasing number of aging population, a type of care which can help prevent or postpone entry into institutional care is preferable. Activity recognition can be used for home-based care in order to help elderly people to remain at home as long as possible. This paper proposes a practical multi-sensor activity recognition system for home-based care utilizing on-body sensors. Seven types of sensors are investigated on their contributions toward activity classi<sup>fi</sup>cation. We collected a real data set through the experiments participated by a group of elderly people. Seven classi<sup>fi</sup>cation models are developed to explore contribution of each sensor. We conduct a comparison study of four feature selection techniques using the developed models and the collected data. The experimental results show our proposed system is superior to previous works achieving 97% accuracy. The study also demonstrates how the developed activity recognition model can be applied to promote a home-based care and enhance decision support system in health care.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

The number of aging population worldwide has increased rapidly. In 2010, there were 520 million people aged 65 years and over and is expected to increase to 1.9 billion people in 2050 [1]. Population aging affects people in various aspects from society, politics to health care. Health care in particularly is greatly affected as people's health deteriorate as they get older. These effects include high demand in long-term care, poor standard of care, and <sup>fi</sup>nancial constraints in care expenditure. Different studies have been carried out with the aim of overcoming these effects. For example, an autonomous intelligent system was proposed in [2] for planning nurses' working time in order to provide effective care to Alzheimer patients. The in<sup>fl</sup>uencing factors that lead to initiate adoption of healthcare information systems were studied in [3]. The investigation was conducted in [4] to identify the level of autonomy–disability of elderly people living in a nursing home for forecasting, planning and management of healthcare and social services.

Due to the effects of an increasing older population, it is important to encourage preventive care to help prevent acute illness or delay entry into institutional care e.g. nursing homes, hospitals, etc. Examples of preventive care are aging healthy and home-based care. Healthy aging are such as eating healthy, regular exercising, regular health check-up, etc. Aging healthily could extend longevity and reduce the possibility of acute serious illness. Another preventive care is to provide care at home such as health monitoring, activity monitoring, etc. Home-based care allows elderly people to be monitored seamlessly from their own homes allowing them to remain at home as long as possible. With current advance in sensors and technology, home-based care is possible and affordable for general population.

Activity recognition is a part of home-based care. By manipulating and mining sensor data, the current activity of a person can be determined. This information can be used to provide home monitoring, detect early sign of deterioration, provide a means of assurance for family members, etc. Prior works in activity recognition are usually performed through visual sensing. However, this is not practical for elderly care application due to privacy issues resulting from the use of cameras. Due to this reason, a non-visual based activity recognition approach is more suitable. Recently, non-visual based activity recognition [5,6] has been studied in an attempt of proposing a model that is practical and highly accurate.

Although these studies have demonstrated that activity recognition can bene<sup>fi</sup>t from combining information from multiple sensors, it is not yet clear how each of the sensors helps in the detection of human activities. In this paper, we investigate seven types of sensors including accelerometer, temperature, altimeter, heart rate monitor, gyroscope, barometer and light sensor to understand how the loss of a particular sensor affects the classi<sup>fi</sup>cation accuracy and to which type of activity. We have collected a real data set from a group of elderly people performing a range of daily activities. This paper also studies several feature selection techniques and classi<sup>fi</sup>cation techniques in order to propose a practical activity recognition model. We compared our approach with other studies to demonstrate the superior in our model.

## 2. Related works

Based on sensor location, there are two main approaches in activity recognition i.e. infer activity from detected objects or changes in environment and infer activity from movement data. Object-based activity recognition requires sensors to be attached to numerous objects such as cups, toothbrush, tooth paste, spoon, etc. within homes. Sometimes sensors are also placed in environment for example, door switch [7], RFID [8], and motion detectors [7] in rooms. This approach infers activity by observing the sequence of objects used or changes in environment. Although the approach can provide clear semantic toward activity recognition, it requires a large number of sensors installed in homes. Also, when there is a new object, a sensor must be tagged and the system needs to be updated. Problems related to uncertainty e.g. false start and fail to detect object can affect recognition performance. To address the problems, the approach which infers activity from movement data obtained from on-body sensors is adopted.

Human activity recognition based on on-body sensors has become popular due to the advance in sensor technology making sensors more accessible and affordable. A variety of on-body sensors have been explored such as accelerometer [5,7–11], gyroscope [6, 11], temperature [6,7,9], etc. Accelerometer is shown to be the most powerful sensor for activity recognition as it responds fast to movement change and can re<sup>fl</sup>ect the type of activity well [9]. A number of studies use several sensors attached to different parts of human body to increase recognition accuracy. Locations such as chest [10,11], wrist [5–7,11], thigh [10], waist [12], ankle [10,11], etc. have been studied. For example, accelerometers were used on subjects' wrists, ankles and chest [11]. Inertial sensors were attached to chest, right thigh and left ankle to detect postures and transition activities [10]. However, attaching several sensors on body may decrease mobility or even obstruct daily activity routine. Also, these sensors may sometimes be perceived as stigmatization. It is important, especially for elderly care applications, that the activity recognition system is practical with high performance.

Taking aforementioned issues into consideration, some of studies proposed an activity recognition model based on a single location on human body [5]. Wrist is an ideal location for on-body sensors as it will not obstruct daily activity mobility. In this paper we consider the use of multiple sensor worn on wrist as we hypothesize that they will help yield more information necessary for activity recognition. Some studies were carried out based on wrist-worn multisensors. Multi-sensor wrist-worn equipment was used to detect walking, walking upstairs, walking downstairs, sitting and running activities [5]. The study showed that using a combination of accelerometer and light worn on wrist can produce good classi<sup>fi</sup>cation accuracy. Accelerometer, temperature sensor and altimeter worn on wrist were used to detect nine activities [6]. It showed that by combining accelerometer with temperature sensor and altimeter, classi<sup>fi</sup>cation accuracy is improved. Although the literatures indicated good results on the use of multiple sensors, it is not yet clear how each of the sensor helps in activity classi<sup>fi</sup>cation. This prompted us to investigate how the loss of a particular sensor will affect the classi<sup>fi</sup>cation accuracy. Seven sensors have been selected including accelerometer, temperature, altimeter, gyroscope, barometer, light, and heart rate monitor. These sensors have been used in several prior works [5–9,12–15]. A study showed that by using gyroscope and magnetometer with accelerometer, the classi<sup>fi</sup>cation accuracy is increased by 17% [13]. Accelerometer and barometer were used to detect 11 children activities [12]. The results indicated improvement in accuracy after adding barometer. Accelerometer and light sensor were used in [14] to detect seven of<sup>fi</sup>ce worker activities. A study showed that combining acceleration and heart rate improves the accuracy of estimation of energy expenditure by 1.4% [15].

Based on these sensors, we propose an activity recognition model where we investigated several feature selection and classi<sup>fi</sup>cation techniques. As feature space becomes larger when several sensors are used, it is important that only important and relevant features for classi<sup>fi</sup>cation are selected. The feature selection technique usually measures the relationship between feature and the output such as by using information theory [16–18], or by measuring the variable salient using neural network [6,19], etc. For example, Minimal Redundancy Maximal Relevance (mRMR) [16] employs information theory to <sup>fi</sup>nd a subset of features that have high mutual information between feature and output (maximal relevance) and low information among the selected features (minimal redundancy). Normalized Mutual Information Feature Selection (NMIFS) [17] is another technique which uses information theory. It claimed to be an enhancement over mRMR where normalized MI is used as a measurement of redundancy to reduce the bias of MI toward multi-valued features and also constraint value to be in [0 1] range. Feature Combination (FC) technique uses neural network theory to perform feature selection. FC [6] takes into account a combination of feature to monitor network performance while features are added to the network. In this paper, we combine Clamping [19] with mRMR and NMIFS and compare it with other feature selection techniques including mRMR, NMIFS, and FC. Several classi<sup>fi</sup>cation algorithms such as Support Vector Machine (SVM) [6,7,12], neural network [6,9,11], Decision Tree [8,9,12,5], etc. have been studied in human activity recognition. In this study, SVM, MLP, and RBF are investigated.

## 3. Methodology

## 3.1. Multi-sensor activity recognition system

This section presents a practical multi-sensor activity recognition system shown in Fig. 1 and describes how it can be used for homebased care. The elderly person wears sensors including accelerometer, temperature sensor, altimeter, gyroscope, light sensor, and barometer which are embedded on watch on their wrists and a heart rate monitor on their chests. The data from the sensor is continuously transmitted wirelessly through radio frequency to the PC in the elderly's home. The PC contains the activity recognition model (AR) which can recognize and detect daily activities of a user. The detected activity is perceived wirelessly by a companion robot who provides assistances or services based on the current activity. For example, if the robot detects that the elderly person is exercising, it can play music or video related to that exercise. If the house is equipped with smart sensors, the detected activities can be used to provide information for adaptive services. For example, if it is detected that a user is sleeping, the light and the temperature can be adjusted to the suitable condition.

The detected activities can also be used by carer, health professionals, and families. To protect the privacy of the elderly person, the system will not send the raw sensor data over the network. The detected activities are encrypted when sent over the Internet. For carers, their systems will contain an activity abnormal detection model to detect abnormality of the elderly person. When the abnormal activity is detected, a carer can visit the elderly home and provide help. This will allow independence for both elderly person and carer, while maintaining safety and good care when necessary. The families of the elderly person will also bene<sup>fi</sup>t from the system where they can use it to monitor them online anywhere and anytime to provide a peace of mind that their love ones are doing well. Health professionals will have access to the activity records. Their systems will contain a model which interprets each activity into activity patterns. They can use this as a complement to normal independent assessment and to support illness diagnostic. Also, if they detect any changes in behavior, they could send a request to elderly person's system to retrieve a raw sensor data for further analysis or arrange a home or hospital visit for a check up on the elderly person.

Any sensor data sent from the elderly person must be encrypted and authorization system must be installed and used whenever someone requested to access the data. Also, there must be a signed agreement on who can have access to what information and the elderly must give their consent prior to the use of the system to ensure privacy and visibility.

![](/api/attachments/3SAZ655U/fulltext/images/7b68e429f6218ac45d5a3c1039b972fbadcac0376eee58dd665216f2f6e2a5eb.jpg)  
Fig. 1. A practical multi-sensor activity recognition system for home-based care.

## 3.2. Decision support system for health care

This section describes how the proposed multi-sensor activity recognition can be used to enhance the decision support system (DSS) for health care. Fig. 2 shows the design of the DSS. The proposed method is used for classifying the complex sensor data into activities to generate a database of activity records over times. The data management is used for manage databases from several sources. The operations that the data management carries out include organize, search, query, add, update, and delete databases. It also connects to the user interface management to provide interface for the users to perform operations with the databases. Besides the activity database, other databases related to health care information such as medical records, hospital resources, carer records, and independence assessments are connected with the data management so that the DSS can cooperate several sources to make reliable decisions.

![](/api/attachments/3SAZ655U/fulltext/images/121ba3884d12d14f633ab25c843a4162bdd4fb79639512e9df43ed4d3d8afeae.jpg)  
Fig. 2. Decision support system for health care.

The model management (MM) is used to manage models, select suitable models for different problems, execute the model, and combine results from models. MM is connected to data management and UI to retrieve input data and to present outputs. The models are used to predict, simulate, etc. information. An example is a model to predict decline in daily activities, schedule the carer timetable, classify independence level, simulate utilities in hospital, etc.

In health care, experiences or expertise may be needed to make critical decisions. Therefore, the DSS contains the knowledge management (KM) which is used to store the knowledge resulting from the decision made by experts. The knowledge includes the process and/or information required to make decision by experts. KM consists of subsystems such as representation, validation, inference, and explanation of the knowledge.

The DSS contains the user interface management (UI) to manage different terminals for users to interact with the DSS. UI includes several interfaces suitable for different tasks and user groups. For example, the interface for management staffs should present overall result with graphical formats, while information of a particular task in detail is presented to operational staffs. High usability is a crucial aspect of the acceptance of DSS.

The DSS can be used to generate a monthly activity graph which shows the amount of each activity carried out in different months. This can be used to see the trend and detect changes in activities and support the decision whether to contact the person to come to the hospital and to which department or a home visit or whether further activity data should be requested from the patient. For example, if the graph shows the decline in walking over several months, this could suggest that there is a problem with ambulating. This would help reduce the number of hospital visits, improve hospital resources utilization, and increase earlier detection rate.

The DSS can be used to support the decision on the type of carer that is required for different patients. For example, if an activity record shows no decline or changes in activity pattern, carer may not be needed. If the activity record suggests that the person may have problem with feeding, the carer who can provide assistance with feeding or cooking should be sent. Also, based on activity database, the DSS can build a model to predict when it is likely that the person will need a carer, so that the management of carer e.g. schedule and number of carer can be done effectively.

The activity record can be used for the assessment of independence. The DSS can use this to make a decision whether the carer is needed or predict when the carer will be needed in order to manage resources effectively. The activity database can be used as part of the other clinical decision support systems to give more information to support the illness diagnostic or disease symptom. For example, if the activity record shows that the patient has very little sleep per day, it could in<sup>fl</sup>uence the decision of the speci<sup>fi</sup>c sleeping disorder.

## 3.3. System design justification

The design of the system was based on the practicality factors for the assisted living system which was gathered from a questionnaire study. Questionnaires were distributed randomly at a major local hospital, nursing homes, general population in Stafford and the elderly club in Swansea to investigate senior adult perceptions on six assistive technologies and six factors regarding technology adoption. Descriptive statistics were used to analyze quantitative data. Qualitative data were analyzed by categorization techniques. The response rate of 74.7% was obtained of which 49 people were aged 60 years and over. The participant perceptions toward assistive technologies were positive except for video monitoring system. Privacy, cost, usability, reliability, functionality and misuse of technology were identi<sup>fi</sup>ed as concerns in assistive technology adoption. The <sup>fi</sup>ndings from this study indicate that privacy and cost are the most important issues which may affect tech nology adoption.

## 3.4. Sensor characteristic and implementation

We used the EZ-430 watch with integrated accelerometer, temperature sensor and altimeter on the CC430F6137 microcontroller with the MSP430 CPU from Texas Instrument (see Fig. 3). The accelerometer measures 3-axis acceleration between ±2G $( \mathrm { G } = 9 . 8 1 ~ \mathrm { m } / s ^ { 2 } )$ with sensitivity of 56 count/G. The pressure sensor can measure between 30– 120 kPa with 6 Pa resolution. The heart rate monitor chest strap is from BlueRobin. It has built-in 868 MHz radio frequency which can transmit a range of up to 800 m. Temperature, altitude, and heart rate are logged in an 8 kB <sup>fl</sup>ash on the watch. Acceleration is transmitted wirelessly to PC via application implemented on MatLab based on 868 MHz radio frequency. Gyroscope, barometer, and light sensor are implemented on Gadgeteer FEZ Cerberus board with 168 MHz 32bit Cortex M4 processor. The gyroscope can measure up t $\dot { \mathbf { \varepsilon } } \pm 2 0 0 0 ^ { \circ } / s$ with 14.375 LSBs per°/s sensitivity. The barometer measures between 300 and 1100 hPa absolute pressure range. The 2 GB SD card is used to log the data. The board was powered using an 800 mAh power bank for a light weight application. The board was placed on the power bank which was placed on top of the wrist watch. Accelerometer and gyroscope are sampling at 33 Hz, while the others are at 1 Hz.

## 3.5. Sensor location justification

As the aim of this study is to propose a practical multi-sensor activity recognition system for home-based care, it was decided that the sensors should be worn at a user's wrist. The justi<sup>fi</sup>cation of the system design on this work has been based on the literatures and innovative ideas. For example, the justi<sup>fi</sup>cation that using the accelerometer on the wrist is based on literatures and that wrist is the optimum location for wearable sensor as it does not interrupt daily activities. Also, literatures indicate that it is possible to predict activities based on wrist-worn accelerometer.

However, due to hardware limitation, it was not possible to implement all the sensors on a single watch. Therefore, it was decided to separate the sensors between two wrists. We separate the sensors in a way that it should not interfere with the activity recognition. The sensors which are related to the movement i.e. accelerometer and gyroscope are worn on the dominant wrist in order to capture the activity movement. Also, barometer and light sensors are also worn on the dominant wrist as they are parts of the Gadgeteer platform. The temperature sensor which captures the body temperature and altimeter are worn on the non-dominant wrist. In real application, we are expected to implement all the sensors into a single watch and will be worn on the dominant wrist of the elderly person. This location will not disrupt a user from performing an activity and/or cause discomfort in wearing sensors. The heart rate monitor needs to be worn on a user's chest using a chest strap. Fig. 3 shows the location of the sensors on a participant. Although the chest strap is made from elastic fabric, wearing the sensor for a continuous time might cause discomfort. The study will evaluate the trade-off between discomfort and the obtained accuracy.

## 3.6. Data collection procedure

The project was approved by the Faculty of Computing, Engineering and Technology Academic Ethics Team, Staffordshire University, UK. Before the data collection, all participants were asked about their age, gender, and health issues to evaluate their suitability for participation. We recruited 12 participants and their characteristics are shown in Table 1. The number of participants is slightly larger than the average number of participants in activity recognition studies.

![](/api/attachments/3SAZ655U/fulltext/images/329a11e1d1909aa30d809850bfbc5eebbc46d8e8f81eb6042f3059e154745f0b.jpg)  
Fig. 3. The location of the sensors. The gyroscope, barometer, and light sensor on Gadgeteer board are mounted over the Chronos watch. The participant wore two watches and a heart rate monitor on her chest.

We studied 13 activities of daily living including brushing teeth, exercising, feeding, ironing, reading, scrubbing, sleeping, using stairs, sweeping, walking, washing dishes, watching TV and wiping. For exercise activity, the participants were asked to perform exercise using elastic stretching band. For each activity, the participants were asked to carry out the activity for 10 min. They could perform the activity in any order. In total, 33.75 h of activity data was recorded. We recorded 12 raw data including 3 axis of acceleration, heart rate, temperature, altitude, light, barometer temperature, barometer pressure, and 3 axis of rotation. In total there are 64,084 patterns.

## 3.7. Feature extraction

It is dif<sup>fi</sup>cult to built classi<sup>fi</sup>cation boundary directly from raw input, therefore suitable features need to be extracted or calculated from them. We <sup>fi</sup>rst calculated the norm of both acceleration and rotation. There are 14 input data in total (12 raw data + acceleration norm + rotation norm). For each input, we calculated features from both time and frequency domains. These features include mean, standard deviation (STD), maximum, minimum, median, mode, kurtosis, skewness, intensity, difference, and root-mean-square (RMS), energy between 0.3 and 6 Hz, entropy, key coef<sup>fi</sup>cient between 0.5 and 3 Hz, correlations between each acceleration axis e.g. acc-X and acc-Y and correlations between each gyroscope axis e.g. gyro-X and gyro-Y. In total, 202 features were calculated.

As our feature space is large, it is important to carry out feature selection process. This process determines the smallest set of features while retaining the class discriminatory information. This will allow a classi<sup>fi</sup>cation model to be constructed effectively and reduce computational cost.

## 3.8. Feature selection algorithms

In this study, the following feature selection algorithms are investigated:

## 1. Minimal Redundancy Maximal Relevance (mRMR) [16]

It is based on the concept of the maximal statistical dependency criterion using MI which is used for de<sup>fi</sup>ning the dependency between variables. Given the two variables, i and j, the MI can be calculated as [20]:

Participant characteristics for the wearable-sensor activity data set.

<table><tr><td rowspan="2">Gender</td><td colspan="3">Age (year)</td><td colspan="2">Weight (kg)</td><td colspan="2">Height (m.)</td><td colspan="2">BMI  $(kg/m^2)$ </td></tr><tr><td>Mean</td><td>STD</td><td>Range</td><td>Mean</td><td>STD</td><td>Mean</td><td>STD</td><td>Mean</td><td>STD</td></tr><tr><td>Female</td><td>72.70</td><td>4.76</td><td>13.00</td><td>50.80</td><td>10.75</td><td>1.58</td><td>0.039</td><td>20.44</td><td>4.48</td></tr><tr><td>Male</td><td>74.50</td><td>2.12</td><td>3.00</td><td>47.00</td><td>14.14</td><td>1.58</td><td>0.035</td><td>18.83</td><td>4.85</td></tr><tr><td>All</td><td>73.00</td><td>4.41</td><td>13.00</td><td>50.17</td><td>10.72</td><td>1.58</td><td>0.037</td><td>20.17</td><td>4.36</td></tr></table>

$$
I (i; j) = \int \int p (i, j) \log \frac {p (i , j)}{p (i) p (j)} \mathrm{d} i \mathrm{d} j.
$$

The mRMR technique employs the minimal redundancy maximal relevance criterion to achieve a maximal dependency condition. By combining mRMR and some subset selection algorithms e.g. forward selection, a subset of features, S, can be found by the following steps:

(a) Given S = {} where S is a set of selected features and $F = \{ f _ { 1 } , f _ { 2 } , . . . ,$ f } where F is a set of N features. Select the feature f in F which has the maximum mutual information between itself and output C where $C = \{ c _ { 1 } , c _ { 3 } , . . . , c _ { K } \}$ and $f _ { s } = m a x _ { f _ { i } \in F } I ( f _ { i } ; C )$ . Update S and F.

$$
\begin{array}{l} S = S \cup \{f _ {s} \} \\ F = F \setminus \{f _ {s} \}. \end{array}\tag{1}
$$

2

(b) Select feature $f _ { s }$ in F which satis<sup>fi</sup>es the following condition:

$$
\max _ {f _ {i} \in F} \left\{I (f _ {i}; C) - \frac {1}{| s |} \sum_ {f _ {j} \in S} I \left(f _ {i}; f _ {j}\right) \right\}.
$$

Update S and F using Eqs. (1) and (2). Repeat step (b) until the desired number of features is obtained.

2. Normalized Mutual Information Feature Selection (NMIFS) [17] NMIFS is an enhancement of mRMR. Rather than using the average of MI as a measure of redundancy between feature and the subset of selected features as in mRMR, a normalized MI (NMI) is used:

$$
N M I (i; j) = \frac {I (i ; j)}{\min \{H (i) , H (j) \}}
$$

where H() is the entropy function. Similar steps as mRMR is carried out, however the condition in step (b) is changed to:

$$
\max _ {f _ {i} \in F} \left\{I (f _ {i}; C) - \frac {1}{| S |} \sum_ {f _ {j} \in S} N M I \left(f _ {i}; f _ {j}\right) \right\}.
$$

3. Combination of mRMR, NMIFS and Clamping (COM)

We propose to combine feature rankings from mRMR, NMIFS and Clamping. The importance of the feature can be calculated as [19]:

$$
I m (f _ {i}) = 1 - \frac {g (F | f _ {i} = f _ {i})}{g (F)}\tag{3}
$$

where $g ( \ u )$ is the generalized performance of the network. The following steps are used to perform feature selection using Clamping:

(a) Calculate the importance of each feature f using Eq. (3). A subset of features is selected according their importance.

$$
f _ {s} = \max _ {f _ {i} \in F} I m (f _ {i})\tag{4}
$$

(b) A subset of features is updated using Eqs. (1) and (2).

These steps are repeated until the desired number of features is reached. After rankings from mRMR, NMIFS, and Clamping are obtained, the rankings are combined using the Borda count. Given the N features, the highest score N is given to the most important features and 1 to the least important features. The score is then combined for all the rankings from each feature selection technique. The <sup>fi</sup>nal ranking is obtained by sorting out the features in descending order (highest score for the most important feature).

## 4. Feature combination (FC) [6]

FC monitors the performance of the selected features so that the subset contains a suitable combination of features. First, the features are ranked using the Clamping technique. Then, the features are selected based on its importance using Eq. (4). Before a feature is added to S, an MLP network is constructed using S and F as input and if and only if $g ( S \cup f _ { i } ) \geq g ( S )$ , then update S and F using Eqs. (1) and (2). This is repeated until all features have been evaluated. All feature sets are combined using Borda count to obtain the <sup>fi</sup>nal ranking.

## 3.9. Classification algorithm

After a suitable subset of features is identi<sup>fi</sup>ed, a classi<sup>fi</sup>cation model can be constructed. In this study, three classi<sup>fi</sup>cation algorithms are investigated. A brief description on these techniques is reviewed below with a given input $\mathfrak { r } _ { i } \in \Re$ and output $o _ { i } \in \{ 0 , 1 , . . . , K \}$

## 1. Multi-Layer Perceptron neural network (MLP) [21]

MLP is capable of learning any nonlinear functions by adjusting the connection weights to minimize the error of the output. It utilizes the concept of connectionist where several input nodes are connected with several output nodes. These connections are associated with weights and the network output, and can be calculated as

$$
o _ {i} = \phi \left(\sum_ {i} w _ {i} x _ {i}\right)
$$

where ϕ is the activation or transfer function which normally is a sigmoid function $\mathrm { e . g . }$ logistic function and hyperbolic tangent. MLP learns the classi<sup>fi</sup>cation error through the back propagation algorithm and minimizes that error by adjusting the weights $w _ { i } .$

## 2. Radial Basis Function neural network (RBF) [21] 2. Radial Basis Function neural network (RBF) [21]

RBF is a network which uses the Radial Basis Function as the activation function. For N hidden neurons, the activation function is de-<sup>fi</sup>ned as:

$$
f (x) = \sum_ {i = 1} ^ {N} w _ {i} \varphi (\| x - c _ {i} \|)
$$

where $c _ { i }$ is the center vector for neuron i and φ is a kernel function e.g. Gaussian and thin plate spline.

3. Support Vector Machine (SVM) [22]

SVM projects input into a higher dimensional space so that non-linear data can be separated. It searches for hyperplane with a maximal margin to separate the data by solving the following optimization problem:

$$
\min _ {w, b, \xi} \left[ \frac {1}{2} w ^ {T} w + C \sum_ {i = 1} ^ {m} \xi_ {i} \right]
$$

subject to:

$$
o _ {i} \left(w ^ {T} f (x _ {i}) + b\right) \geq 1 - \xi_ {i}; \xi_ {i} \geq 0.
$$

The slack term $\xi _ { i }$ is used to relax the constraints allowing misclassi<sup>fi</sup>ed examples. The associated cost parameter C is used for penalizing $\xi _ { i \cdot } f ( \cdot )$ is a kernel function which transforms the input $x _ { i }$ into a higher dimensional space. Common kernel functions are linear kernel, RBF kernel and polynomial kernel, etc. This study uses RBF kernel function $\begin{array} { r } { f ( x _ { i } ) = \exp \biggl ( - \frac { 1 } { \left( 2 \sigma ^ { 2 } \right) } \Bigl | \Bigl | x _ { i } - x _ { j } \Bigr | \Bigr | ^ { 2 } \biggr ) } \end{array}$ where σ is the width of the Gaussian kernel. For K-class classi<sup>fi</sup>cation, K binary classi<sup>fi</sup>ers are constructed and one-VS-all classi<sup>fi</sup>cation is applied.

## 3.10. Statistical tests

Statistical tests were employed to test if the difference in classi<sup>fi</sup>cation accuracy is signi<sup>fi</sup>cant. First, the data is tested against its normality using Shapiro–Wilk. If the data is a normal distribution, paired-sample T-test is used. Otherwise, related-sample Wilcoxon Signed Rank test is used. All statistics used were carried out at 95% con<sup>fi</sup>dence interval.

## 4. Experimental results

The collected data was pre-analyzed and missing data was removed as it did not statistically affect the data set. Sweeping activity data was removed as after removing missing data this class only constitutes to 3% of the data set. Balanced class sampling is used to help build a more accurate decision boundary and make the model more robust to detect unknown input. Also, imbalanced class can impose problems such as error in interpreting classi<sup>fi</sup>cation results, and data from minority class may be treated as noise.

The data was pre-processing using weighted moving average and segmented at 3.88 s with 50% overlapping, resulting in 39,328 patterns. 202 features were extracted as speci<sup>fi</sup>ed in Section 3.5. NaN and constant valued features were removed. Also to reduce the feature space, we calculated MI of each feature and decided a cut-off point at 3% of the maximum MI. Note that, MI is calculated on discretized data using 10 bins. As for the result, there were 141 features. All experiments carried out in this study use a 10-fold cross validation where 8 folds are used for training, 1 for validation and 1 for testing. The data was randomly selected using uniform distribution. All experiments were repeated for 10 runs.

## 4.1. Feature selection

Firstly, features were ranked using the speci<sup>fi</sup>ed techniques mentioned in Section 3.6. The results from different runs are combined using the Borda count. Feature selection was performed using neural network. A Multi-Layer Perceptron with one hidden layer was used where the hidden node was set to α × number of input. Experiments were carried out to determine the appropriate value of alpha and the number of epoch where trade-off between accuracy and training time was considered.

The result of averaged validation accuracy is shown in Fig. 4. From the graph, it can be seen that FC achieves the highest accuracy. We tested the hypothesis if the accuracy difference is signi<sup>fi</sup>cant. The data is not a normal distribution and statistical tests indicated that the accuracy of FC is signi<sup>fi</sup>cantly higher than other techniques $\left( p < 0 . 0 5 \right)$ . COM is signi<sup>fi</sup>cantly higher than mRMR and NMIFS $\left( p < 0 . 0 5 \right)$ . The difference in accuracies of mRMR and NMIFS is not statistically signi<sup>fi</sup>cant $( p =$ 0.315). To sum up, the performance of the feature selection techniques can be expressed as $F C > ^ { * } C O M > ^ { * } m R M R = N M I F S \mathrm { w h e r e } ^ { * } > ^ { * , }$ indicates signi<sup>fi</sup>cantly better and $" = "$ indicates no signi<sup>fi</sup>cant difference at 95% con<sup>fi</sup>dence interval.

![](/api/attachments/3SAZ655U/fulltext/images/4a620802a4fc8858573ea51ebb9396903087316aaf2483d17c91862c41eb2838.jpg)  
Fig. 4. Validation accuracy on different feature selection techniques.

mRMR and NMIFS produced similar accuracy and selected similar set of features. The reason is that they are based on mutual information. This is evident in which mRMR and NMIFS produced similar ranking. When we investigated why these techniques cannot achieve higher accuracy, it was found that majority of the features selected at the beginning were from accelerometer and gyroscope only. Although features extracted from these sensors contain valuable information, when using the forward selection strategy this would lead to a selection of redundant features. mRMR and NMIFS only select features from accelerometer, gyroscope and light sensor.

On the other hand, Clamping ranking selects features from a variety of sensors such as accelerometer, gyroscope, heart rate sensor, barometer, light, and altimeter (see Table 2). It can be seen that the result has considerably improved when COM is used. Besides accelerometer, gyroscope and light sensor, COM also selects features from barometer which means that this sensor provides valuable information for activity classi-<sup>fi</sup>cation. Features selected from Clamping and FC are similar as FC is modi<sup>fi</sup>ed from Clamping technique. However, FC searches for only the subset of features which are complementing each other and reduce redundant features. FC clearly achieved better accuracy as compared to the other three techniques. However, according to the graph, the accuracies at the beginning are lower. Thus, in the case of data set with small number of features (less than 5), using mRMR should produce a better result. The truncation at 24 features was selected where the accuracy starts to remain constant.

Table 3  
Test classi<sup>fi</sup>cation accuracy of each model.

<table><tr><td>Model</td><td> $SVM16_{7S}$ </td><td> $SVM24_{7S}$ </td><td> $MLP16_{7S}$ </td><td> $MLP24_{7S}$ </td><td> $RBF16_{7S}$ </td><td> $RBF24_{7S}$ </td><td> $SVM16_{3S}$ </td></tr><tr><td>Mean</td><td>96.9575</td><td>97.2040</td><td>94.8496</td><td>96.7349</td><td>95.3075</td><td>95.6734</td><td>85.4238</td></tr><tr><td>STD error</td><td>0.0349</td><td>0.0310</td><td>0.0421</td><td>0.0371</td><td>0.0413</td><td>0.0375</td><td>0.0672</td></tr></table>

## 4.2. Classification

The classi<sup>fi</sup>cation models were developed using classi<sup>fi</sup>cation algorithms as described in Section 3.7 with 24 selected features. Also, to demonstrate that the proposed method using more sensors can achieve better accuracy, we construct another model where 16 features from three sensors were used and classi<sup>fi</sup>cation is based on SVM [6]. From here, we shall refer this model as $S V M 1 6 _ { 3 S } .$ As the $S V M 1 6 _ { 3 S }$ uses only 16 features, we also constructed classi<sup>fi</sup>cation models using truncation point at 16 features. The classi<sup>fi</sup>cation is performed using test data and the results are shown in Table 3. The notation of the model name is given by the algorithm, number of feature, and number of sensor. For example, $R B F 1 6 _ { 7 S }$ represents the classi<sup>fi</sup>cation model using RBF with 16 features from 7 sensors.

The data is a normal distribution and statistical test indicated that the differences between each model are statistically signi<sup>fi</sup>cant where $S V M 2 4 _ { 7 S } > ^ { * } S V M 1 6 _ { 7 S } > ^ { * } M L P 2 4 _ { 7 S } > ^ { * } R B F 2 4 _ { 7 S } > ^ { * } R B F 1 6 _ { 7 S } > ^ { * } M L P 1 6 _ { 7 S } > ^ { * } R B .$ $^ { * } S V M 1 6 _ { 3 S }$ where $" > ^ { * , }$ indicates signi<sup>fi</sup>cantly better at 95% con<sup>fi</sup>dence interval. We also tested if there is a difference in accuracy when 16 and 24 features are used. The result indicated that using 24 features obtained statistically higher accuracy than using 16 features (p b 0.05).

The results revealed that SVM is the best classi<sup>fi</sup>cation model among others. In general, the models can classify walking very well. However, they have dif<sup>fi</sup>culty in classifying feeding activity. The result shows that in our dataset SVM is superior to MLP and RBF. $S V M 2 4 _ { 7 S }$ achieved the highest classi<sup>fi</sup>cation accuracy while $M L P 1 6 _ { 7 S }$ achieved the lowest accuracy. When observing the F-score for each class, it was found that in general $S V M 2 4 _ { 7 S }$ obtained the highest score, especially for exercise activity. $S V M 1 6 _ { 7 S }$ achieved slightly better result in classifying brushing teeth and feeding than $S V M 2 4 _ { 7 S } .$ When observing precision and recall, it can be seen that $S V M 1 6 _ { 7 S }$ achieved higher precision in washing dishes and watching TV as compared to $S V M 2 4 _ { 7 S } .$ . While $S V M 2 4 _ { 7 S }$ has higher sensitivity in obtaining these classes, $S V M 1 6 _ { 7 S }$ makes prediction more accurately.

Table 2  
Features selected using different techniques.

<table><tr><td>Sensor</td><td>Data</td><td>MRMR</td><td>NMIFS</td><td>Clamping</td><td>COM</td><td>FC</td></tr><tr><td rowspan="4">Accelerometer</td><td>X-axis</td><td>-</td><td>-</td><td>RMS, mean</td><td>RMS</td><td>RMS, mean</td></tr><tr><td>Y-axis</td><td>RMS, max, median, mode, key coefficient, mean, min</td><td>Max, median, mean, mode, min</td><td>RMS, max, median, key coefficient, mode, mean</td><td>RMS, median, mean, min, mode</td><td>Max, median, mean, min, mode, RMS</td></tr><tr><td>Z-axis</td><td>Min, median, mode, mean</td><td>max</td><td>RMS, mean</td><td>Mean, median, min, mode</td><td>RMS, mean</td></tr><tr><td> $\sqrt{x^2 + y^2 + z^2}$ </td><td>Intensity, max, median, mean, RMS</td><td>Intensity, RMS, max, mean</td><td>Correlation X, Z, max, RMS</td><td>Max, intensity, RMS, median, mean</td><td>Correlation X, Z, max, RMS</td></tr><tr><td>Temperature</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Altimeter</td><td>Altitude</td><td>-</td><td>-</td><td>Min</td><td>-</td><td>Min</td></tr><tr><td>Heart rate monitor</td><td>Heart rate</td><td>-</td><td>-</td><td>-</td><td>-</td><td>Min</td></tr><tr><td>Light</td><td>Light intensity</td><td>Max</td><td>Max</td><td>Max, min</td><td>Max, RMS, mean, median</td><td>Max, min</td></tr><tr><td rowspan="2">Barometer</td><td>Temperature</td><td>-</td><td>-</td><td>Max, median, RMS, mean</td><td>Median, Max</td><td>Max, median, RMS</td></tr><tr><td>Pressure</td><td>-</td><td>-</td><td>Max, median</td><td>Max</td><td>Max, median</td></tr><tr><td rowspan="4">Gyroscope</td><td>X-axis</td><td>STD, RMS</td><td>STD, mode</td><td>-</td><td>STD</td><td>STD</td></tr><tr><td>Y-axis</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Z-axis</td><td>STD, RMS, intensity</td><td>Min, median, mode, mean</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $\sqrt{x^2 + y^2 + z^2}$ </td><td>RMS, mean, median, STD</td><td>RMS, mean, median</td><td>Correlation X, Y</td><td>RMS</td><td>Correlation X, Y</td></tr></table>

Table 4  
Confusion matrix of the $S W M 2 4 _ { 7 S }$

<table><tr><td rowspan="2">Actual</td><td colspan="12">Predicted</td></tr><tr><td>Brush</td><td>Exercise</td><td>Feed</td><td>Iron</td><td>Read</td><td>Scrub</td><td>Sleep</td><td>Stairs</td><td>Walk</td><td>Wash</td><td>Watch</td><td>Wipe</td></tr><tr><td>Brush</td><td>20,246</td><td>29</td><td>280</td><td>65</td><td>53</td><td>20</td><td>30</td><td>85</td><td>0</td><td>101</td><td>47</td><td>44</td></tr><tr><td>Exercise</td><td>40</td><td>20,667</td><td>26</td><td>57</td><td>20</td><td>16</td><td>1</td><td>38</td><td>17</td><td>59</td><td>11</td><td>48</td></tr><tr><td>Feed</td><td>289</td><td>35</td><td>19,824</td><td>197</td><td>142</td><td>67</td><td>67</td><td>63</td><td>2</td><td>186</td><td>78</td><td>50</td></tr><tr><td>Iron</td><td>91</td><td>69</td><td>162</td><td>20,210</td><td>30</td><td>56</td><td>10</td><td>62</td><td>8</td><td>127</td><td>14</td><td>161</td></tr><tr><td>Read</td><td>61</td><td>32</td><td>154</td><td>101</td><td>20,463</td><td>14</td><td>25</td><td>20</td><td>5</td><td>40</td><td>68</td><td>17</td></tr><tr><td>Scrub</td><td>9</td><td>23</td><td>34</td><td>58</td><td>6</td><td>20,549</td><td>8</td><td>29</td><td>4</td><td>38</td><td>40</td><td>202</td></tr><tr><td>Sleep</td><td>65</td><td>9</td><td>70</td><td>24</td><td>21</td><td>37</td><td>20,526</td><td>124</td><td>2</td><td>28</td><td>26</td><td>68</td></tr><tr><td>Stairs</td><td>86</td><td>37</td><td>96</td><td>38</td><td>14</td><td>55</td><td>44</td><td>20,498</td><td>99</td><td>22</td><td>30</td><td>29</td></tr><tr><td>Walk</td><td>0</td><td>33</td><td>3</td><td>8</td><td>6</td><td>38</td><td>8</td><td>153</td><td>20,670</td><td>6</td><td>0</td><td>27</td></tr><tr><td>Wash</td><td>78</td><td>28</td><td>208</td><td>123</td><td>54</td><td>66</td><td>19</td><td>34</td><td>19</td><td>20,278</td><td>18</td><td>75</td></tr><tr><td>Watch</td><td>13</td><td>6</td><td>19</td><td>8</td><td>55</td><td>6</td><td>30</td><td>72</td><td>6</td><td>20</td><td>20,742</td><td>23</td></tr><tr><td>Wipe</td><td>43</td><td>52</td><td>17</td><td>112</td><td>25</td><td>164</td><td>21</td><td>48</td><td>20</td><td>195</td><td>29</td><td>20,274</td></tr></table>

When examining classi<sup>fi</sup>cation algorithms using 24 features, we found that SVM has the highest F-score in most classes except feeding and reading where MLP is better. RBF has the lowest F-score in every class especially in feeding which is substantially lower. However, we found that RBF has comparable or even higher precision with SVM in some classes such as exercising and reading. MLP has a comparable F-score with SVM in brushing teeth, washing dishes and watching TV. When examining at the models using 16 features (which is not the optimal number of features), SVM has the highest F-score in all classes. The F-score of RBF is higher than that of MLP in most classes except for brushing teeth and feeding.

The statistical results indicated that our models using 7 sensors obtained signi<sup>fi</sup>cant higher accuracy than the model based on 3 sensors regardless classi<sup>fi</sup>cation algorithms used. The improvement in accuracy is between 9.43% and 11.78%. We then compare the F-score of each class between previous work and our SVM models. The results indicated that the proposed system achieved a higher F-score than $S V M 1 6 _ { 3 S }$ model in all 12 activities (see Table 5). The F-score of all classes of the $S V M 2 4 _ { 7 S }$ is higher than $S V M 1 6 _ { 7 S }$ except for brushing teeth, feeding and wiping. When observing the confusion matrix of $S V M 2 4 _ { 7 S }$ (see Table 4), we found that the model often confuses between feeding and brushing teeth, wiping and scrubbing, and walking and using stairs. Ironing and washing sometimes are also confused with feeding. It is observed that these activities have similar motion on the wrist.

To evaluate the trade-off between accuracy and the use of heart rate monitor, we performed a classi<sup>fi</sup>cation without using the feature from the heart rate where we substitute the feature with the next best feature. The classi<sup>fi</sup>cation using MLP obtained $9 3 . 1 0 2 0 \% \pm 0 . 5 8 5 0 \%$ The data is a normal distribution and the statistical test indicated that by removing heart rate feature, the classi<sup>fi</sup>cation accuracy is signi<sup>fi</sup>cant ly lowered $( T = - 2 8 . 9 9 3 , p < 0 . 0 5 )$ .

## 4.3. Sensor contribution

In this section, we consider how each sensor helps with classi<sup>fi</sup>cation. We performed experiments to understand how the loss of a particular sensor affects the classi<sup>fi</sup>cation accuracy and to which activity. To control the experiment, top features (based on MI) of each sensor were selected to use in the classi<sup>fi</sup>cation. The selected features are maximum acceleration Y-axis, maximum heart rate, maximum barometric pressure, maximum light intensity, RMS gyro magnitude, minimum temperature, and minimum altitude.

Firstly, we generated a classi<sup>fi</sup>cation model (called base model) which uses all sensors. We constructed the next model by removing one sensor. For example, model 1 used all sensors except accelerometer. Model 2 used all sensors except heart rate sensor. In total, 8 models were built. The notation of the model is given by M followed by the name of the removed sensor e.g. $M _ { A c c }$ represents model which does not use accelerometer. The classi<sup>fi</sup>cation was performed using MLP and the number of hidden nodes is twice the number of input. Table 6 shows the mean accuracy of the model when a particular sensor is not used. The test of normality indicated that model $M _ { L i g h t }$ is not a normal distribution, thus we employed Wilcoxon Signed Ranks to test the effect of the loss of a sensor. The statistical results indicate that there is a statistical signi<sup>fi</sup>cant difference between the base model and all the other models $\left( p < 0 . 0 5 \right)$ . Based on the reduced accuracy, the contribution of the sensor can be ranked from the highest to the lowest as accelerometer, gyroscope, light sensor, barometer, heart rate sensor, temperature sensor, and altimeter, respectively. We examined the F-score of each class of each model (see Table 7). The model which does not include accelerometer has an effect on several activities including brushing teeth, feeding, ironing, reading, scrubbing, walking, and wiping. The effect on the absence of light sensor is on sleeping, stairs, and washing dish activities. The model without a gyroscope sensor has effects on exercise and watching TV activity.

## 5. Discussion

In this paper we developed several models to investigate the absence of a particular sensor. It was found that each sensor has a signi<sup>fi</sup>- cant contribution toward the classi<sup>fi</sup>cation accuracy in general. This means that each sensor has given speci<sup>fi</sup>c information which is useful for activity classi<sup>fi</sup>cation. The results also show that accelerometer is the most important sensor since the classi<sup>fi</sup>cation accuracy has signi<sup>fi</sup>- cantly dropped when the sensor is not used. However, missing this sensor does not strongly affect the detection of sleeping. This is due to the fact that this activity is not involved in much movement. On the other hand, missing the light sensor has signi<sup>fi</sup>cantly affected sleeping detection. This suggests that the model uses information from the light sensor to detect sleeping activity. Similarly, stair activity is also affected by missing light intensity information. When observing the plot of the maximum light intensity of these two classes, it is found that, unlike other classes, the data from these two activities are rather clustered. Therefore, missing this information affects the classi<sup>fi</sup>cation of these two classes. The absence of gyroscope has an effect on exercise and watching TV activities. This shows that although the $M _ { G y r o }$ model contains accelerometer feature, it is not enough to detect these activities. The RMS of gyro magnitude signi<sup>fi</sup>cantly helps classify these activities. Although the results demonstrate that each of the seven sensors are important, these models are constructed based on only one feature from each sensor. It is possible that when a model is developed with more number of features, information from a particular sensor could be substituted by the other features from other sensors as well. In fact, in the proposed model, temperature sensors are not selected.

Table 5  
F-score comparison between models based on 3 sensors and 7 sensors.

<table><tr><td>Model</td><td>Brush</td><td>Exercise</td><td>Feed</td><td>Iron</td><td>Read</td><td>Scrub</td><td>Sleep</td><td>Stairs</td><td>Walk</td><td>Wash</td><td>Watch</td><td>Wipe</td></tr><tr><td> $SVM16_{3S}$ </td><td>0.7684</td><td>0.8670</td><td>0.7575</td><td>0.8214</td><td>0.8496</td><td>0.8615</td><td>0.9478</td><td>0.8771</td><td>0.9530</td><td>0.8069</td><td>0.9398</td><td>0.8055</td></tr><tr><td> $SVM16_{7S}$ </td><td>0.9649</td><td>0.9725</td><td>0.9471</td><td>0.9580</td><td>0.9748</td><td>0.9685</td><td>0.9814</td><td>0.9661</td><td>0.9883</td><td>0.9631</td><td>0.9852</td><td>0.9653</td></tr><tr><td> $SVM24_{7S}$ </td><td>0.9636</td><td>0.9837</td><td>0.9464</td><td>0.9624</td><td>0.9770</td><td>0.9765</td><td>0.9824</td><td>0.9698</td><td>0.9889</td><td>0.9633</td><td>0.9853</td><td>0.9650</td></tr></table>

Table 6  
The effect of the loss of a particular sensor.

<table><tr><td>Model</td><td>Missing sensor</td><td>Accuracy (%)</td><td>STD</td></tr><tr><td>Base model</td><td>None</td><td>65.1913</td><td>1.4354</td></tr><tr><td> $M_{ACC}$ </td><td>Accelerometer</td><td>50.0933</td><td>1.4140</td></tr><tr><td> $M_{HR}$ </td><td>Heart rate sensor</td><td>62.0873</td><td>1.2548</td></tr><tr><td> $M_{Baro}$ </td><td>Barometer</td><td>60.7004</td><td>1.2010</td></tr><tr><td> $M_{Light}$ </td><td>Light sensor</td><td>57.6663</td><td>1.1589</td></tr><tr><td> $M_{Gyro}$ </td><td>Gyroscope</td><td>55.8540</td><td>1.4780</td></tr><tr><td> $M_{Temp}$ </td><td>Temperature sensor</td><td>62.2528</td><td>1.1885</td></tr><tr><td> $M_{Alt}$ </td><td>Altimeter</td><td>62.8056</td><td>1.1016</td></tr></table>

Comparing with $S V M 1 6 _ { 3 S } ,$ the results suggest that the addition of heart rate sensor, barometer, gyroscope and light sensor improves classi<sup>fi</sup>cation accuracy. This means that they provide valuable information for the classi<sup>fi</sup>cation of the activities studied. The results of the study provide suggestion on possible sensors for other activity classi<sup>fi</sup>cation systems. Also, these sensors except for heart rate monitor are used on a user's wrist will allow practical applications of activity recognition for home-based care. The results of the study show that our proposed system achieves a better performance statistically.

The results show that combining heart rate with other sensors signi<sup>fi</sup>cantly improves classi<sup>fi</sup>cation accuracy. Nevertheless, the classi<sup>fi</sup>- cation accuracy without using heart rate is still high as compared to $S V M 1 6 _ { 3 S } .$ This suggests that it is possible to use only wrist worn sensors to maintain its practicality and better accuracy can be achieved.

Table 5 indicates that our model is comparable to or in some activities higher than previous studies. Also, our approach only requires sensor worn on wrist and chest. We also show that even when we remove the heart rate sensor, high accuracy can be achieved. This is an important aspect for a practical application in elder care. The system which is not intrusive or perceived as stigmatization can be easily accepted by the elderly.

Another objective of this study is to compare the performance of 4 feature selection techniques (Table 8). Our results suggest that FC is the most appropriate technique for our application. FC can select a more diversity set of features as compared to other techniques. It monitors the performance of a subset of features along the selection to make sure that redundant features are not selected. However, according to the FC algorithm, redundant features may still be selected at earlier stage and we suggest that post checking should be added to remove any redundant feature after selection. mRMR and NMIFS only measure the redundancy between 2 variables which was shown not enough to reduce the overlapped features. The result of this study implies that the technique which can select a subset of features with the lowest feature redundancy is the most optimum technique.

## 6. Conclusion

We have proposed a practical multi-sensor activity recognition system for home-based care and evaluated it through the real data we collected. We investigated seven types of sensors including accelerometer, temperature, altimeter, heart rate monitor, barometer, light sensor, and gyroscope on how it helps classi<sup>fi</sup>cation accuracy and to which types of activity. In general we found accelerometer to be the most important sensor. We also found that maximum light intensity can be useful for detecting sleeping, stairs, and washing dish activities. The RMS of gyro magnitude can help in classifying exercise and watching TV activities. Although we found that all the sensors provide important information toward classi<sup>fi</sup>cation, when larger features of sensors are available, a particular sensor could be omitted.

We compared the results with previous method which only used three sensors and the results show that the additional four sensors help improve activity classi<sup>fi</sup>cation accuracy. We achieve 97.2040% accuracy using six sensors. The study also demonstrates how the developed activity recognition model can be applied for home-based care and DSS for health care. The study also investigated 4 feature selection techniques including mRMR, NMIFS, COM and FC. The results indicate that

Table 7  
F-score of each model.  
Table 8

<table><tr><td>Model</td><td>Brush</td><td>Exercise</td><td>Feed</td><td>Iron</td><td>Read</td><td>Scrub</td><td>Sleep</td><td>Stairs</td><td>Walk</td><td>Wash</td><td>Watch</td><td>Wipe</td></tr><tr><td>Base model</td><td>0.6771</td><td>0.5818</td><td>0.5506</td><td>0.5856</td><td>0.5549</td><td>0.7140</td><td>0.7382</td><td>0.7144</td><td>0.7809</td><td>0.5191</td><td>0.7088</td><td>0.6683</td></tr><tr><td> $M_{ACC}$ </td><td>0.5036</td><td>0.4438</td><td>0.4239</td><td>0.3715</td><td>0.4271</td><td>0.5025</td><td>0.6579</td><td>0.6437</td><td>0.3858</td><td>0.4307</td><td>0.6048</td><td>0.5325</td></tr><tr><td> $M_{HR}$ </td><td>0.6493</td><td>0.5382</td><td>0.5393</td><td>0.5797</td><td>0.5122</td><td>0.6826</td><td>0.6995</td><td>0.6995</td><td>0.7725</td><td>0.4459</td><td>0.6652</td><td>0.6229</td></tr><tr><td> $M_{Baro}$ </td><td>0.6406</td><td>0.5494</td><td>0.5397</td><td>0.5483</td><td>0.4824</td><td>0.6771</td><td>0.6456</td><td>0.6639</td><td>0.7596</td><td>0.4715</td><td>0.6500</td><td>0.6211</td></tr><tr><td> $M_{Light}$ </td><td>0.5688</td><td>0.5639</td><td>0.4673</td><td>0.5640</td><td>0.5062</td><td>0.6843</td><td>0.5994</td><td>0.5354</td><td>0.7428</td><td>0.3973</td><td>0.6193</td><td>0.6035</td></tr><tr><td> $M_{Gyro}$ </td><td>0.5995</td><td>0.3807</td><td>0.4841</td><td>0.5147</td><td>0.4879</td><td>0.5878</td><td>0.6676</td><td>0.6402</td><td>0.7286</td><td>0.4489</td><td>0.4838</td><td>0.6304</td></tr><tr><td> $M_{Temp}$ </td><td>0.6544</td><td>0.5410</td><td>0.5405</td><td>0.5644</td><td>0.5197</td><td>0.6968</td><td>0.7204</td><td>0.6885</td><td>0.7541</td><td>0.4542</td><td>0.6816</td><td>0.6155</td></tr><tr><td> $M_{Alt}$ </td><td>0.6583</td><td>0.5541</td><td>0.5417</td><td>0.5624</td><td>0.5157</td><td>0.7094</td><td>0.7033</td><td>0.6885</td><td>0.7645</td><td>0.4883</td><td>0.6814</td><td>0.6359</td></tr></table>

Accuracy comparison between previous works and the proposed system.

<table><tr><td></td><td># activity</td><td>Sensor location</td><td>Brush teeth</td><td>Feed</td><td>Iron</td><td>Sleep</td><td>Stairs</td><td>Walk</td><td>Average</td></tr><tr><td> $SVM24_{7S}$ </td><td>12</td><td>Wrist, chest</td><td>96.36</td><td>94.64</td><td>96.24</td><td>98.24</td><td>97.39</td><td>98.65</td><td>97.20</td></tr><tr><td>[11]</td><td>12</td><td>Wrists, ankles, chest</td><td>-</td><td>89.50</td><td>-</td><td>89.20</td><td>90.80</td><td>88.20</td><td>91.3</td></tr><tr><td>[7]</td><td>7</td><td>Body, environment</td><td>64.30</td><td>97.80</td><td>-</td><td>93.90</td><td>-</td><td>95.00</td><td>86.20</td></tr><tr><td>[8]</td><td>-</td><td>Wrist, objects</td><td>-</td><td>-</td><td>97.94</td><td>92.66</td><td>-</td><td>84.36</td><td>-</td></tr><tr><td>[9]</td><td>7</td><td>On-body</td><td>-</td><td>-</td><td>87.00</td><td>-</td><td>79.00</td><td>86.00</td><td>82–86</td></tr><tr><td>[5]</td><td>6</td><td>Wrist</td><td>-</td><td>-</td><td>-</td><td>-</td><td>&gt;90</td><td>-</td><td>87.10</td></tr><tr><td>[10]</td><td>12</td><td>Chest, thigh, left ankle</td><td>-</td><td>-</td><td>-</td><td>95.4</td><td>-</td><td>98.1</td><td>91.4</td></tr></table>

FC can select the optimum set of features as it can select features from diverse sensors which helps reduce feature redundancy. We suggest improvement on this technique by adding a post feature check to remove redundant feature which may be selected during earlier stage. Also, further investigation on the proposed model in a natural setting is recommended.

## Acknowledgment

We thank Mrs Pan Ayumak and Mrs Juntip Tubtimsri, the representatives of Watket elderly club, Chiang Mai, Thailand and Mr Somchit Chernbumroong for their support on data collection.

## References

[1] UN, World population prospects: the 2012 revision, URL: http://esa.un.org/unpd/ wpp/index.htm 2012.

[2] J.M. Corchado, J. Bajo, Y. de Paz, D.I. Tapia, Intelligent environment for monitoring Alzheimer patients, agent technology for health care, Decision Support Systems 44 (2) (2008) 382–396.

[3] Z. Yang, A. Kankanhalli, B.Y. Ng, J.T.Y. Lim, Analyzing the enabling factors for the organizational decision to adopt healthcare information systems, Decision Support Systems 55 (3) (2013) 764-776.

[4] C. Combes, J. Azema, Clustering using principal component analysis applied to autonomy–disability of elderly people, Decision Support Systems 55 (2) (2013) 578–586.

[5] U. Maurer, A. Rowe, A. Smailagic, D. Siewiorek, Location and activity recognition using eWatch: a wearable sensor platform, Ambient Intelligence in Everyday Life2006.86-102

[6] S. Chernbumroong, S. Cang, A. Atkins, H. Yu, Elderly activities recognition and classi<sup>fi</sup>cation for applications in assisted living, Expert Systems with Applications 40 (5) (2013) 1662–1674.

[7] A. Fleury, M. Vacher, N. Noury, SVM-based multimodal classi<sup>fi</sup>cation of activities of daily living in health smart homes: sensors, algorithms, and <sup>fi</sup>rst experimental results, IEEE Transactions on Information Technology in Biomedicine 14 (2) (2010) 274–283 (ID: 1).

[8] Y.J. Hong, I.J. Kim, S.C. Ahn, H.G. Kim, Mobile health monitoring system based on activity recognition using accelerometer, Simulation Modelling Practice and Theory 18 (4) (2010) 446–455.

[9] J. Parkka, M. Ermes, P. Korpipaa, J. Mantyjarvi, J. Peltola, I. Korhonen, Activity classification using realistic data from wearable sensors JEEE Transactions on Information Technology in Biomedicine 10 (1) (2006) 119–128.

[10] D. Trabelsi, S. Mohammed, F. Chamroukhi, L. Oukhellou, Y. Amirat, An unsupervised approach for automatic activity recognition based on hidden Markov model regression, IEEE Transactions on Automation Science and Engineering 10 (3) (2013) 829–835.

[11] Z. Wang, M. Jiang, Y. Hu, H. Li, An incremental learning method based on probabilistic neural networks and adjustable fuzzy clustering for human activity recognition by using wearable sensors, IEEE Transactions on Information Technology in Biomedicine 16 (4) (2012) 691–699.

[12] Y. Nam, J. Park, Child activity recognition based on cooperative fusion model of a triaxial accelerometer and a barometric pressure sensor, IEEE Journal of Biomedical and Health Informatics 17 (2) (2013) 420–426.

[13] H. Gjoreski, M. Gams, Activity/posture recognition using wearable sensors placed on different body locations, Proceeding of Signal and Image Processing and Applications, 2011, pp. 22–24.

[14] C. Lombriser, N.B. Bharatula, D. Roggen, G. Tröster, On-body activity recognition in a dynamic sensor network, Proceedings of the ICST 2nd international conference on Body area networks; BodyNets '07, 17, 2007, pp. 1–17, (6).

[15] E. Munguia Tapia, Using Machine Learning for Real-Time Activity Recognition and Estimation of Energy Expenditure, (Ph.D. thesis) Massachusetts Institute of Technology, 2008.

[16] H. Peng, F. Long, C. Ding, Feature selection based on mutual information: criteria of max-dependency, max-relevance, and min-redundancy, IEEE Transactions on Pattern Analysis and Machine Intelligence 27 (2005) 1226–1238.

[17] P. Estevez, M. Tesmer, C. Perez, J. Zurada, Normalized mutual information feature selection, IEEE Transactions on Neural Networks 20 (2) (2009) 189–201.

[18] S. Cang, H. Yu, Mutual information based input feature selection for classi<sup>fi</sup>cation problems, Decision Support Systems 54 (1) (2012) 691–698.

[19] W. Wang, P. Jones, D. Partridge, Assessing the impact of input features in a feedforward neural network, Neural Computing & Applications 9 (2) (2000) 101–112.

[20] C.E. Shannon, A mathematical theory of communication, SIGMOBILE: Mobile Computing and Communications Review 5 (1) (2001) 3–55.

[21] C.M. Bishop, Neural Networks for Pattern Recognition, Oxford University Press, Inc., New York NY USA 1995

[22] C.C. Chang, C.J. Lin, LIBSVM: a library for support vector machines, ACM Transactions on Intelligent Systems and Technology 2 (27) (2011) 1–27 (27).

Saisakul Chernbumroong received a B.Eng. in Industrial Engineering from Chiang Mai University, Thailand and a M.Sc. in Computer Science from University of Hertfordshire, UK. She is currently working toward the Ph.D. degree at the Faculty of Science and Technology, Bournemouth University, UK. Her research interest includes sensor-based activity recognition, RFID sensors, and intelligent system for smart health. Her current research is focused on multi-sensor based activity recognition and classi<sup>fi</sup>cation to support elderly care.

Shuang Cang is a Senior Lecturer in the School of Tourism, Bournemouth University, UK. She gained BSc (Hons) with <sup>fi</sup>rst class honors, MSc with distinction and a PhD degree in Mathematics/Applied Mathematics. She worked in a UK leading Software Company for about two and half years. Then she worked in the Department of Computer Sciences at Exeter University and University of Wales (Aberystwyth). She spent over two years as Senior Statistician/Senior Analyst in the UK Government Research Laboratory and UK Government Department, where she applied statistical and pattern recognition techniques to solve real and complex problems. Her research interests cover data mining, arti<sup>fi</sup>cial intelligence, pattern recognition, multivariance statistics, forecasting and segmentations.

Hongnian Yu has held academic positions at the Universities of Sussex, Liverpool John Moor, Exeter, Bradford, Staffordshire and Bournemouth in the UK. He is currently Professor in Computing at Faculty of Science and Technology, Bournemouth University. He has extensive research experience in mobile computing, modeling, scheduling, planning, and simulations of large discrete event dynamic systems with applications to manufacturing systems, supply chains, transportation networks, computer networks and RFID applications, modeling and control of robots and mechatronics, and neural networks. He has graduated over 20 PhD/MPhil and MRes research students, is supervising 8 PhD students, and has examined over 20 PhD/MPhil students' theses as both internal and external examiner. He has published over 200 journal and conference research papers. He has held several research grants worth about <sup>fi</sup>ve million pounds from the UK EPSRC, the Royal Society, and the European, AWM, as well as from industry. Prof Yu was awarded the F.C. William Premium for his paper on adaptive and robust control of robot manipulators by the IEF Council. He is a member of the EPSRC Peer Review College. Prof Yu has strong research collaboration with partners from many countries, such as China, France, Germany, Hungary, Italy, Japan, Romania, Thailand and USA. He was a General Chair of International conference on Software Knowledge Information Management and Applications (SKIMA) in 2012, and is serving on various other conferences and academic societies
