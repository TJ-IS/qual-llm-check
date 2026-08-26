---
otero_id: 10650
otero_key: "NSNGADKK"
title: "Human Identification for Activities of Daily Living: A Deep Transfer Learning Approach"
authors: "Hongyi Zhu; Sagar Samtani; Hsinchun Chen; Jay F. Nunamaker"
year: "2020"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2020.1759961"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Human Identification for Activities of Daily Living: A Deep Transfer Learning Approach

Hongyi Zhu , Sagar Samtani , Hsinchun Chen & Jay F. Nunamaker Jr.

To cite this article: Hongyi Zhu , Sagar Samtani , Hsinchun Chen & Jay F. Nunamaker Jr. (2020) Human Identification for Activities of Daily Living: A Deep Transfer Learning Approach, Journal of Management Information Systems, 37:2, 457-483, DOI: 10.1080/07421222.2020.1759961

To link to this article: https://doi.org/10.1080/07421222.2020.1759961

![](/api/attachments/NSNGADKK/fulltext/images/83bd4535e2c29ba620ab0081497ff6d79ffb1f2c2adcea3a29234138a562ad25.jpg)

Published online: 16 Jun 2020.

![](/api/attachments/NSNGADKK/fulltext/images/b7b8145215c9865013e9c664bcec5671247d873abaa32f1fb4f40eb3bb5192ef.jpg)

Submit your article to this journal

![](/api/attachments/NSNGADKK/fulltext/images/4879d212a1b56072bdfc60f18abe34cc22c97fec119d4864a72340c9dd3c0864.jpg)

Article views: 18

![](/api/attachments/NSNGADKK/fulltext/images/e309cb209c744fafcb2f3a629657a9ffeaac71017ba888e5741805607d61b862.jpg)

View related articles

![](/api/attachments/NSNGADKK/fulltext/images/a00845d7caf2b79361e6b5d15e02f06ae7548fc98a1717919ca53f64185934a2.jpg)

View Crossmark data

Check for updates

# Human Identi<sup>fi</sup>cation for Activities of Daily Living: A Deep Transfer Learning Approach

Hongyi Zhu<sup>a</sup>, Sagar Samtani<sup>b</sup>, Hsinchun Chen<sup>c</sup>, and Jay F. Nunamaker, Jr.<sup>c</sup>

<sup>a</sup>Department of Information Systems and Cyber Security, University of Texas at San Antonio, San Antonio, TX, USA; <sup>b</sup>Department of Operations and Decision Technologies, Indiana University, Bloomington, IN, USA; <sup>c</sup>Department of Management Information Systems, University of Arizona, Tucson, AZ, USA

## ABSTRACT

Sensor-based home Activities of Daily Living (ADLs) monitoring systems have emerged to monitor elderly people’s self-care ability remotely. However, the unobtrusive, privacy-friendly object motion sensor-based systems face challenges such as scarce labeled data and ADL performer confusion in a multi-resident setting. This study adopts the design science paradigm to develop an innovative deep transfer learning framework for human identi<sup>fi</sup>cation (DTL-HID) to address both challenges. A novel convolutional neural network (CNN) is proposed to automatically extract comprehensive temporal and cross-axial motion patterns for the DTL-HID framework. We rigorously evaluate the DTL-HID framework against state-of-the-art benchmarks (e.g., k Nearest Neighbors, Support Vector Machines, and alternative CNN designs). Results demonstrate our proposed DTL-HID framework can identify the ADL performer accurately even on a small amount of labeled data. We demonstrate a case study and discuss how stakeholders can further apply this approach to unobtrusive smart home monitoring for senior citizens. Beyond demonstrating the framework’s practical utility, we discuss two implications of our design principles to mobile analytics and design science research: (1) extracting temporal and axial local dependencies can capture richer information from multi-axial time-series data and (2) transferring knowledge learned on a relevant source domain with su<sup>fi</sup>cient data can improve the performance of the desired task on the target domain with scarce data.

## KEYWORDS

Deep transfer learning; human identi<sup>fi</sup>cation; activities of daily living; deep learning; mobile health; design science; health monitoring

## Introduction

Medical advancement and increased accessibility of healthcare have contributed to the growing life expectancy worldwide [60]. In 2016, the senior citizen population (aged over 65 years old) reached 49.2 million and 98.0 million in the United States (US) and European Union (EU), respectively, accounting for 15.2% and 19.2% of the population in the US and EU [8, 13]. The growing aging population has raised societal concerns on senior citizen’s well-being. In their late life, senior citizens’ health and independent-living ability can be a<sup>f</sup>ected by chronic diseases. Physical deteriorations such as frailty and mobility impairments limit senior citizen’s self-caring ability; mental deteriorations such as dementia and amnesia further increase their self-caring di<sup>fi</sup>culties. Thus, in order to ensure a healthy life to senior citizens, it is crucial to monitor and assess their Activities of Daily Living (ADLs) performance.

ADL is a set of self-caring activities needed for independent-living senior citizens [20]. It consists of two major types: basic and instrumental. Basic ADLs are short and simple tasks. These include functional mobility, bathing, dressing, self-feeding, hygiene, and grooming. Instrumental ADLs are long and complex tasks such as housework, preparing meals, taking medications, shopping, and others. ADLs can serve as a proxy to assess senior citizen’s physical or cognitive impairments and their chronic disease progression [20]. Inability to perform a certain activity can indicate physical conditions; irregular ADL patterns can suggest mental deterioration; and the longitudinal shifting of activity patterns can imply disease progression. Therefore, preventative care requires regular and frequent ADL monitoring and assessment, which infrequent (e.g., monthly) clinic visits cannot provide [12].

The senior care industry has started to explore sensor-based home ADL monitoring systems to provide a<sup>f</sup>ordable, predictive, preventive, and personalized care [16]. Predictive and preventive care requires granular data for analytics. Given that 57% of US senior citizens live with a spouse in a multi-resident environment [2], personalized care further requires that the identity of the ADL performer be correctly recognized. Current ADL monitoring systems incorporate two common types of sensors to collect granular ADL data: cameras and motion sensors [12]. Table 1 describes the sensor types, the information they capture, and their respective strengths and drawbacks.

The data can record critical information such as “who performed the ADL,” “when and where the ADL was performed,” and “how the ADL was performed.” Machine learning (ML) or health analytics algorithms can then process collected sensor data for valuable healthcare applications (e.g., “who” for personalized care, “when,” “where,” and “how” for predictive care such as behavior deterioration tracking). Although camera and wearable motion sensors can capture rich information for various health applications, senior citizens are often reluctant to adopt them due to privacy concerns and the amount of e<sup>f</sup>ort required to use the technology, respectively [12, 26]. In real life, object motion sensor-based systems may have higher acceptance and adoption.

One drawback of object motion sensor-based systems is the lack of activity performer information. For example, grandparents can both open the fridge for food. However, the object motion sensor on the fridge door cannot record the activity performer, preventing personalized dietary tracking. Therefore, object motion sensor-based systems necessitate computational models (e.g., ML algorithms) that accurately recognize or infer the identity of activity performers from available data (e.g., how the ADL was performed). However, several technical challenges and constraints exist for developing the required ML models. First, extant ML models rely heavily on ad-hoc and laborious feature engineering that can potentially leave out important sensor signal patterns and result in less accurate performance. Second, object motion sensors have various placements based on customized monitoring goals, and they move less compared with the human body. The high placement variation and low data availability prevent e<sup>f</sup>ective ML and health analytics and can hinder the results’ generalizability.

Two common types of sensors used in home ADL monitoring systems.

<table><tr><td>Sensor Type</td><td>Description</td><td>Information Captured</td><td>Strengths</td><td>Drawbacks</td></tr><tr><td>Camera</td><td>Records human, object, and environment information [52]</td><td>Who, when, where, and how</td><td>High data granularity</td><td>Many privacy concernsData storage cost</td></tr><tr><td rowspan="2">Motion (e.g., tri-axial accelerometer)</td><td>Wearable (attaches to body): records body movements [4]</td><td>Who, when, and how</td><td>High sensitivity and data granularity</td><td rowspan="2">ObtrusiveGreat effort required by frequent sensor attach/ detachUnaware of activity performerScarce data</td></tr><tr><td>Object (attaches to objects): records object movements [4]</td><td>When, where, and how</td><td></td></tr></table>

Addressing these challenges could enable accurate and generalizable HID for object motion sensor-based ADL monitoring systems in real life. To this end, this study adopts the design science research paradigm and proposes a novel deep transfer learning (DTL) framework for ADL performer identi<sup>fi</sup>cation with object motion sensors [21, 43]. The novelty of this research is three-fold. First, this framework can accurately distinguish activity performers in a multi-resident environment with scarce object motion sensor data. This enables unprecedented performance in downstream ADL recognition and monitoring applications for personalized care. Second, this framework consists of a novel Convolutional Neural Network (CNN) to automatically extract comprehensive temporal and cross-axial features for performer identi<sup>fi</sup>cation. This avoids ad-hoc and laborious feature engineering for sensor data. Third, this framework transfers patterns learned from the identi<sup>fi</sup>ed rich and relevant data (i.e., labeled wearable motion sensor data) to improve the activity performer identi<sup>fi</sup>cation performance on scarce object sensor data. In addition to these novelties, this research also o<sup>f</sup>ers design guidelines (i.e., principles) to the IS knowledge base and practical implications. For the former, our CNN and DTL design can potentially motivate IS researchers and guide the design of new analytical models for multichannel time-series data or scarce data, respectively. With regard to the latter, this research can potentially aid the senior care industry in their e<sup>f</sup>orts to e<sup>f</sup>ectively implement and use object sensor-based monitoring systems in multiresident environments.

The remainder of this paper is organized as follows. First, we review literature related to motion sensor-based ADL monitoring, human identi<sup>fi</sup>cation, and DTL. Second, we identify research gaps within existing literature and pose research questions for study. Third, we introduce each component of our research design and evaluation experiments. Subsequently, we present the experiment results and discuss their implications. We then demonstrate the usability of our method with a case study. Finally, we conclude this research and highlight promising directions for future research.

## Literature Review

We review three areas of literature to form the basis of this research: (1) motion sensorbased ADL monitoring to understand motion sensor applications and their data characteristics, (2) human identi<sup>fi</sup>cation to understand state-of-the-art sensor-based human identi<sup>fi</sup>cation techniques, and (3) deep transfer learning (DTL) to address scarce object motion sensor data issue.

## Motion Sensor-Based ADL Monitoring

Motion sensors are often preferred for home monitoring systems due to their low setup cost and ability to collect rich, detailed data. Motion sensors are easily attachable to objects or human bodies. Consequently, they are a viable option for widespread deployment in senior residences such as nursing homes, assisted living facilities, and houses/apartments. Moreover, motion sensors capture human and object movements within an environment with high resolution and frequency. For example, a 16-bit Micro-Electro-Mechanical Systems (MEMS) accelerometer can collect over eight million data samples per day with a resolution of $6 \times 1 0 ^ { - 5 } ~ g$ (g denotes gravity) under a sample rate of 100Hz (i.e., 100 data samples per second). Such rates are beyond a human’s manual processing capacity. These data samples usually contain multiple channels that can precisely record movements. For example, data collected by tri-axial accelerometers attached to a cup contains accelerations on x-, y-, and z-axes (Figure 1). When aligned by timestamps, the two data dimensions have heterogeneous temporal and axial local dependencies. The temporal local dependency denotes the temporal patterns of sensor values on one axis (rotated gray boxes in Figure 1). The axial dependency denotes axial correlation patterns and interactions (e.g., sensor rotation) between two axes (two pairs of gray boxes in Figure 1).

According to Newton’s second law of motion $F = m a ,$ acceleration (a) can measure the force (F) acting on an object, whose mass (m) is a constant. Therefore, Figure 1 also illustrates how di<sup>f</sup>erent people may demonstrate distinguishable patterns while conducting the same activity. For example, subject B has larger absolute acceleration than subject A while picking up the cup (rotated gray boxes), denoting more extreme (i.e., harder) movements than subject A’s smoother (i.e., lighter) movements (Figure 1). The volume, resolution, and granularity of sensor data o<sup>f</sup>er immense value for ADL monitoring, speci<sup>fi</sup>cally on how a subject performs an activity. Table 2 summarizes selected motion sensor-based ADL monitoring literature to illustrate how motion sensors are applied and how their data is processed.

Two categories of computational algorithms have been employed to extract patterns from vast amounts of sensor data: classical machine learning [45, 47] and deep learning [22, 40, 65]. Classical machine learning algorithms (e.g., SVM, HMM, etc.) generally use two categories of manually derived features: general signal-related (e.g., mean, standard deviation, curvature) and activity-speci<sup>fi</sup>c (e.g., cycle count, motion direction). However, feature engineering is often labor-intensive and ad-hoc; thus, features may not generalize to alternative sensor con<sup>fi</sup>gurations. These limitations have motivated researchers to shift to deep learning. Deep learning is a class of machine learning algorithms that use neural networks with multiple layers of non-linear operations to learn data features [17]. Deep learning’s ability to automatically learn the most salient data representation without manual feature engineering makes it a suitable selection for sensor data [6].

![](/api/attachments/NSNGADKK/fulltext/images/2035c1fe58468ffb8f32eb14a2bd0c6f828b57e595b53ce0a071f613b50866ab.jpg)

![](/api/attachments/NSNGADKK/fulltext/images/03aad9e7a113e00c91d2a00236dc32765ff93085780d746818ec4b03429988b5.jpg)  
Accelerometer data contains temporal and axial local dependencies.

Selected recent literature on motion sensor-based ADL monitoring.

<table><tr><td>Year</td><td>Authors</td><td>Model/ Algorithm*</td><td>Approach to Obtain Features</td><td>Recognition Tasks</td><td>Sensors**</td></tr><tr><td>2018</td><td>Ignatov [22]</td><td>CNN</td><td>Learned + manually extracted</td><td>Locomotion activities</td><td>Mobile Acc. &amp; Gyro</td></tr><tr><td>2018</td><td>Zhu et al. [65]</td><td>Seq2Seq</td><td>Learned</td><td>ADLs</td><td>Wearable Acc.</td></tr><tr><td>2016</td><td>Hammerla et al. [19]</td><td>DNN, CNN, LSTM</td><td>Learned</td><td>Gestures</td><td>Wearable Acc., Gyro., &amp; Mag.</td></tr><tr><td>2016</td><td>Reyes-Ortiz et al. [45]</td><td>Probabilistic SVM</td><td>Manually extracted</td><td>Locomotion transitions</td><td>Wearable Acc. &amp; Gyro.</td></tr><tr><td>2016</td><td>Safi et al. [47]</td><td>HMM Regression</td><td>Manually extracted</td><td>Locomotion activities</td><td>Wearable Acc.</td></tr><tr><td>2015</td><td>Ranjan and Whitehouse [44]</td><td>Nearest Neighbor</td><td>Manually extracted</td><td>User identity</td><td>Wearable Acc.</td></tr><tr><td>2015</td><td>Nabiei et al. [31]</td><td>HMM</td><td>Manually extracted</td><td>Gestures</td><td>Object Acc. &amp; Gyro.</td></tr><tr><td>2014</td><td>Zeng et al. [63]</td><td>CNN</td><td>Learned</td><td>Gestures</td><td>Wearable Acc., Gyro., &amp; Mag.</td></tr></table>

Notes: DNN = deep neural networks; LSTM = Long Short-Term Memory; SVM = support vector machines; HMM = Hidden Markov Models. Acc. = accelerometer; Gyro. = gyroscope; Mag. = magnetometer.

Past literature indicates that CNN is the preferred deep learning architecture for sensor signal analysis [22]. CNN stacks multiple convolutional and pooling layers hierarchically to extract features of various granularity [17, 27]. The convolutional layer applies a kernel K on the data V to extract local information c, where

$$
c = K \odot V,
$$

and denotes the elementwise multiplication [17]. The extracted information is further <sup>fi</sup>ltered by non-linear activation functions to constitute local dependencies. The pooling layer aggregates a condensed representation of local dependencies for higher-level processing. Past CNN-based ADL monitoring studies analyze each sensor axis separately. A 1D convolution operation extracts temporal local dependencies from each axis [19, 22].

Regardless of approach, wearable motion sensors, speci<sup>fi</sup>cally accelerometers, are primarily used for gesture [19, 63] and activity [22, 45, 47] recognition tasks. Most data were collected from a controlled, single-resident environment, where the activity performer’s identity is irrelevant to the task. A few studies explored wearable sensor applications in multi-resident environments on tasks such as human identi<sup>fi</sup>cation [44]. Due to di<sup>f</sup>erent motion patterns between human and objects, human identi<sup>fi</sup>cation (HID) literature is reviewed next to better understand the state-of-the-art HID techniques and the feasibility of HID in a multi-resident setting with unobtrusive object motion sensors.

## Human Identi<sup>fi</sup>cation (HID)

Capturing a person’s physical traits (e.g., height, gait) is essential for human identi<sup>fi</sup>cation tasks [56]. Physical traits are categorized with static-dynamic and intrinsic-extrinsic dimensions [56]. Static traits, such as weight and body shape, measure invariant properties regardless of the activities performed. Dynamic traits measure properties that vary across activities, such as eye movements, facial features, and gait [14, 39, 42]. Intrinsic traits are measured directly from the human. Extrinsic traits measure objects the human interacts with as a proxy of intrinsic traits. Table 3 summarizes the traits, sensors, and computational models used in selected HID research.

Selected recent literature on human identi<sup>fi</sup>cation (HID).

<table><tr><td>Year</td><td>Author</td><td>Traits</td><td>Types of Traits</td><td>Sensors</td><td>Models*</td><td>Evaluation Metrics</td></tr><tr><td>2017</td><td>Pentland et al. [39]</td><td>Facial features</td><td>Intrinsic, dynamic</td><td>Camera</td><td>Video processing</td><td>Face rigidity</td></tr><tr><td>2017</td><td>Mokhtari et al. [29]</td><td>Height</td><td>Intrinsic, static</td><td>Ultra-wideband sensors</td><td>Statistical methods and PCA</td><td>Identification rate (accuracy)</td></tr><tr><td>2017</td><td>Al-Naimi et al. [3]</td><td>Presence traces, gait features</td><td>Extrinsic, dynamic, intrinsic, dynamic</td><td>PIR, pressure sensors</td><td>Signal processing</td><td>Accuracy</td></tr><tr><td>2016</td><td>Corpus et al. [10]</td><td>Keystrokes and acceleration</td><td>Extrinsic, dynamic</td><td>Mobile accelerometer</td><td>DT, NB, kNN</td><td>Accuracy, false rejections rate, false acceptance rate</td></tr><tr><td>2016</td><td>Gadaleta et al. [14]</td><td>Ankle motion, gait</td><td>Intrinsic, dynamic</td><td>Wearable accelerometer</td><td>CNN, SVM</td><td>Accuracy</td></tr><tr><td>2016</td><td>Jain and Kanhangad [23]</td><td>Acceleration and rotation</td><td>Extrinsic, dynamic</td><td>Mobile accelerometer gyroscope</td><td>SVM, bagging</td><td>Accuracy</td></tr><tr><td>2016</td><td>Zhang et al. [64]</td><td>Signal variations caused by gait variations</td><td>Extrinsic, dynamic</td><td>Wi-Fi signal</td><td>Sparse approximation</td><td>Accuracy</td></tr><tr><td>2015</td><td>Wu et al. [61]</td><td>Human shape and posture</td><td>Intrinsic, static, and dynamic</td><td>Camera</td><td>Signal processing, customized classifier</td><td>Matching rate (accuracy)</td></tr></table>

Notes: \*PCA = Principle Component Analysis; DT = decision tree; NB = Naïve Bayes Classi<sup>fi</sup>er; kNN = k Nearest Neighbors.

Intrinsic traits, such as height and ankle motion measured by pyroelectric infrared (PIR), wearable motion sensors, or cameras, can easily reveal human identities [3, 14, 29, 61]. However, these direct measurements can be invasive and obtrusive. Extrinsic traits (e.g., acceleration, keystrokes on mobile devices, pressure traces) are mostly dynamic and more privacy-friendly for HID tasks [3, 10, 23, 64]. However, they are often measured with expensive and highly-specialized devices (e.g., pressure plates, Wi-Fi signal analyzer).

Extant HID research extracts physical traits with manual feature engineering for input into classical machine learning algorithms [3, 23, 39]. Deep learning-based methods have emerged recently to automatically extract dynamic traits from wearable/mobile motion sensors (e.g., accelerometers). HID with daily-using objects can enable more passive monitoring and customized care. However, a key obstacle for object-based HID is obtaining labeled data to train an algorithm e<sup>f</sup>ectively [55]. Transfer learning, an emerging branch of machine learning, can potentially address this issue by leveraging the similar motion dynamics between wearable and object sensors [9].

## Deep Transfer Learning (DTL)

Transfer Learning (TL) applies knowledge gained in a source domain S to improve problem-solving in a related target domain T. TL is often used when machine learning tasks conducted on T achieves low performance due to insu<sup>fi</sup>cient training data [59]. TL can transfer four types of knowledge for target tasks: instance (e.g., data point), parameter (e.g., prior distribution, parameter estimation), feature representation, and relational knowledge (e.g., rules) [36]. Since deep learning automatically learns and preserves the feature representation on network layers and weights, DTL commonly transfers representations by reusing models trained on S to transfer such knowledge [17, 59]. Figure 2 illustrates the general DTL process.

DTL generally follows three steps. First, a deep learning model $Y = f _ { A } ( X ; W _ { \mathrm { A } } | \Phi _ { \mathrm { A } } )$ for source domain Task A is trained with rich source domain data $X _ { S }$ until the optimized weights $W _ { A } ^ { * }$ converge and the cost function $J _ { A }$ is minimized. Second, this trained model $f _ { A } ^ { * }$ is used as the basis of the deep learning model $Y ^ { \prime } = f _ { B } ( X ; W _ { B } \vert \Phi _ { B } )$ for Task B. The <sup>fi</sup>rst n layers o $\vdots f _ { A } ^ { * }$ is reused in the new mode $Y ^ { \prime } = f _ { B } \ ( n = 2$ in Figure 2). This ensures $f _ { B }$ generates representations following the knowledge learned from the source domain. Finally, the transferred model $Y ^ { \prime } = f _ { B }$ is trained to minimize $J _ { B }$ given the low-resourced, labeled training data $X _ { T }$ This step is also known as adaptation, indicating the process adapts a representation from the source to the target domain. The layers and weights transferred from the trained model $f _ { A }$ are <sup>fi</sup>xed (i.e., weights on transferred layers are not updated by the backpropagation algorithm). The <sup>fi</sup>nal outcome is a deep learning model $f _ { B } ^ { * }$ for the target domain Task B that contains knowledge transferred from the source domain. This overall DTL process of automatically learning, transferring, and adapting feature representations has enabled scholars to achieve state-of-the-art performances in various applications [25, 30, 49, 57, 58]. Selected recent DTL studies are summarized in Table 4.

DTL has primarily been applied in natural language processing (NLP) and image recognition contexts. Both have unique data characteristics extracted by specialized deep learning models. Texts contain sequential word patterns; thus, recurrent neural networks (RNN) are reused by TL for their ability to capture temporal text patterns [11, 49]. In image recognition, input data (e.g., radiology image) contains homogeneous spatial patterns (i.e., insensitive to transpose operations) on both dimensions across di<sup>f</sup>erent color channels [7, 24, 50]. These patterns are usually extracted and transferred with a 2Dkernel-based CNN [25, 58].

![](/api/attachments/NSNGADKK/fulltext/images/bb1bb331118cffaa4f8e222c4c8fc55bb0d2f3b723e2e87de333037a15e580d0.jpg)  
A General architecture of deep transfer learning. $Y = f ( X ; W | \Phi )$ denotes a L-layer deep learning model with $\Phi = \{ \Phi ^ { 1 } ( \cdot ) , \Phi ^ { 2 } ( \cdot ) , \dots , \Phi ^ { \mathsf { L } } ( \cdot ) \}$ as the forward propagation functions on each layer $( \mathsf { i . e . }$ , the model structure) and W as the model weights. Each task is formalized with a cost function $J ( W | X , \Phi )$ ; and the objective is to learn the best $W ^ { * }$ that optimize the cost function.

Selected recent literature on deep transfer learning (DTL).

<table><tr><td>Year</td><td>Author</td><td>Context</td><td>Model*</td><td>Knowledge Transferred</td><td>Reused Model Component</td></tr><tr><td>2018</td><td>Kermany et al. [25]</td><td>Medical image diagnosing</td><td>CNN</td><td>Image patterns</td><td>Convolution layers</td></tr><tr><td>2017</td><td>Wang et al. [58]</td><td>Vehicle recognition</td><td>CNN</td><td>Image patterns</td><td>Convolution layers</td></tr><tr><td>2017</td><td>Burlina et al. [7]</td><td>Retina image diagnosing</td><td>CNN</td><td>Image patterns</td><td>Convolution models</td></tr><tr><td>2017</td><td>Völker et al. [57]</td><td>EEG decoding</td><td>CNN</td><td>Temporal signal patterns</td><td>Entire model on new data</td></tr><tr><td>2017</td><td>Coutinho and Schuller [11]</td><td>Emotional communication detection</td><td>LSTM</td><td>Temporal word patterns</td><td>Entire model</td></tr><tr><td>2017</td><td>Shickel et al. [49]</td><td>Opinion mining</td><td>GRU</td><td>Temporal word patterns</td><td>Entire model</td></tr><tr><td>2016</td><td>Kandaswamy et al. [24]</td><td>Breast cancer image recognition</td><td>DNN</td><td>Image patterns</td><td>Network layers</td></tr><tr><td>2016</td><td>Morales and Roggen [30]</td><td>Wearable sensors</td><td>CNN</td><td>Temporal signal patterns</td><td>Convolution layers</td></tr><tr><td>2016</td><td>Shin et al. [50]</td><td>Medical image recognition</td><td>CNN</td><td>Image patterns</td><td>Convolution layers</td></tr></table>

Notes: \*GRU = Gated Recurrent Unit.

Studies examining sensor data, such as motion sensors and EEG, only apply convolution on each sensor axis to extract single-axial temporal patterns [30, 57]. However, as illustrated earlier, motion sensor data is heterogeneous (as compared with text or images), containing temporal and axial dependencies. Extracting and transferring both dependency types require a carefully customized, novel deep learning model.

## Research Gaps and Questions

Several research gaps are identi<sup>fi</sup>ed from the existing literature. First, current motion sensor-based ADL monitoring primarily focuses on single-resident setting and gesture recognition. The HID task remains to be addressed to enable personalized ADL monitoring and care in multi-resident environments. Second, prior studies mainly used cameras or wearable/mobile motion sensors for HID. However, senior citizens may be reluctant to adopt these invasive and obtrusive technologies in real life. Moreover, deep learning-based HID models are needed for object sensors to automatically capture valuable temporal and cross-axial patterns and avoid ad-hoc, laborious, manual feature engineering. Third, object motion sensor-based systems su<sup>f</sup>er from data scarcity issues that prevent e<sup>f</sup>ective algorithm training and performance. Extant DTL models primarily address applications that have homogeneous data patterns (e.g., image processing and NLP). A novel DTL approach for motion sensor data is required to extract heterogeneous data dependencies and transfer the representations e<sup>f</sup>ectively. Based on these gaps, we pose the following research questions for our study:

● How can we design a DTL framework to leverage the scarce object motion sensor data for human identi<sup>fi</sup>cation in home ADL monitoring systems?

● How can we design deep learning-based models that automatically and comprehensively extract temporal and cross-axial patterns (i.e., features) from motion sensor data to better represent the motion dynamics?

● How transferable (i.e., potential to improve target domain task) are features extracted by the DTL framework?

## Research Design

To address these research gaps and answer the posed research questions, we developed a novel CNN-based DTL-HID framework (Figure 3) for object sensor-based HID. The HID framework consists of four major components: Data Collection, Data Pre-Processing, DTL-HID Framework, and Evaluation. This framework trains and transfers a novel CNN (CNN-HID) that extracts both dependency types from rich wearable motion sensor data (the large source dataset in Figure 3) to improve the HID performance on scarce object motion sensors data (the small target dataset in Figure 3). The research dataset and the framework components are detailed in the following subsections.

## Data Collection

Two real-world ADL datasets are gathered: “Opportunity” (OPPO) [46] and HANDY [1]. OPPO is a rich real-world morning activity dataset collected under an EU Commission funded project [46]. It contains 20 accelerometers attached to 20 objects (e.g., cup, bread). The sensors collect motion data during <sup>fi</sup>ve general activities: relaxing, early morning, co<sup>f</sup>ee time, sandwich time, and clean up. All accelerometers sampled at 30 Hz, generating on average over 200,000 data points per subject. Four subjects independently performed multiple, scripted ADLs in the same lab environment (i.e., same space and identical sensor con<sup>fi</sup>gurations). They interacted with di<sup>f</sup>erent objects with no restrictions. Therefore, the movements of the same object can be extracted from di<sup>f</sup>erent subjects’ collection and combined to synthesize a 4-resident setting, where each object sensor records distinct movement patterns from all four subjects. Among the 20 object sensors, four (glass, cup, spoon, and bread) are selected as target domains, as they can represent real-life objects shared by residents that can move without constraints (e.g., nutrition supplement bottles, remote control). The target domain data represents the scarce object sensor data we may obtain in real life. They are used to evaluate if HID algorithms can recognize common patterns in a person’s behavior and distinguish among the residents in a multi-resident environment.

![](/api/attachments/NSNGADKK/fulltext/images/4b9a6848b23590c3fbf046a701f12efa2186393e572c01a999086be8d72ec624.jpg)  
The HID framework.

HANDY is a wrist-worn motion sensor (accelerometer, gyroscope, and magnetometer) dataset that contains hand-related activities performed in a controlled lab environment [1]. In this research, seven activities are selected from HANDY, which fall into three general categories based on the plane in the space where wrists primarily moved: vertical (chopping, cleaning a window, and kneading dough), horizontal (cleaning a table and using a computer mouse), and hybrid (drinking water and eating soup). They generally represent data we may obtain during ADLs such as self-feeding, food preparation, housework, and object use [20]. Thirty participants performed the activities separately. Each activity took one to two minutes. All sensors sampled at 52 Hz, resulting in over 30,000 data points per subject. Accelerometer is used as a source domain. HID models extract motion dynamics to distinguish among subjects on source domain data. Since HANDY and OPPO are collected with di<sup>f</sup>erent activities, subject pools, and environment settings, selecting both datasets helps demonstrate the framework’s generalizability.

## Data Pre-Processing

Data pre-processing is critically important for handling mobile sensor data [46, 53, 65]. It contains resampling [30, 65], segmentation [30, 53, 65], standardization [17], and dataset split [30, 65]. Resampling is often conducted when sensors sample at di<sup>f</sup>erent rates. A sample rate mismatch between source and target domain data (i.e., 52 Hz in HANDY and 30 Hz in OPPO) can distort the transferability of the motion dynamics learned by an HID model. Resampling combats this issue in two steps: (1) data points sampled with original rates are interpolated to form continuous value functions, and (2) new data points are then resampled from the functions with a target rate. In our application, we <sup>fi</sup>rst interpolate the HANDY dataset (52 Hz tri-axial accelerometer recordings) with Piecewise Cubic Hermite Interpolation Polynomials (PCHIP). This produces continuous tri-axial acceleration values for all timestamps in the given time period [28]. We then resample at 30 Hz from the interpolated data to match OPPO’s rate [65]. These lower sample rates lead to reduced battery consumptions in real life [51]. Data segmentation ensures machine learning models e<sup>fi</sup>ciently process <sup>fi</sup>xed-sized data. The resampled data is segmented with an 8-second sliding window, which on average is long enough to capture a human-object interaction. Each segmented sample X contains 240 temporallyaligned tri-axial acceleration values $X = [ x _ { 1 } , x _ { 2 } , \dotsc , x _ { 2 4 0 } ]$ and $x _ { i } = \left( x _ { i x } , x _ { i y } , x _ { i z } \right)$ Standardization uni<sup>fi</sup>es feature scales to avoid attributing errors to a few features. The segmented samples are standardized with $\begin{array} { r } { X _ { s t d } = \frac { X - \mu _ { X } } { \sigma _ { X } } } \end{array}$ , where $\mu _ { \chi }$ is the mean and $\sigma _ { X }$ is the standard deviation of a sample [17]. Finally, 45,111 samples from HANDY are extracted as a source domain dataset. For each target domain dataset, we only include segments that contain movements of the corresponding object. Table 5 summarizes the number of segments in each dataset.

Summary of research testbeds.

<table><tr><td>Dataset</td><td colspan="2">Class Label</td><td colspan="2">Number of Segments</td></tr><tr><td>Source Domain</td><td>Types</td><td>Activity</td><td>Each Class</td><td>Total</td></tr><tr><td rowspan="7">HANDY</td><td rowspan="3">Vertical</td><td>Chopping</td><td>6,029</td><td>45,111</td></tr><tr><td>Cleaning a window</td><td>2,801</td><td></td></tr><tr><td>Kneading dough</td><td>8,004</td><td></td></tr><tr><td rowspan="2">Horizontal</td><td>Cleaning a table</td><td>3,194</td><td></td></tr><tr><td>Using a PC mouse</td><td>8,958</td><td></td></tr><tr><td rowspan="2">Hybrid</td><td>Drinking water</td><td>9,500</td><td></td></tr><tr><td>Eating soup</td><td>6,625</td><td></td></tr><tr><td>Target Domain (OPPO_OBJ)</td><td colspan="2">Subject</td><td>Each Class</td><td>Total</td></tr><tr><td rowspan="4">OPPO_GLASS</td><td>I</td><td></td><td>69</td><td>269</td></tr><tr><td>II</td><td></td><td>83</td><td></td></tr><tr><td>III</td><td></td><td>55</td><td></td></tr><tr><td>IV</td><td></td><td>62</td><td></td></tr><tr><td rowspan="4">OPPO_CUP</td><td>I</td><td></td><td>156</td><td>726</td></tr><tr><td>II</td><td></td><td>197</td><td></td></tr><tr><td>III</td><td></td><td>214</td><td></td></tr><tr><td>IV</td><td></td><td>159</td><td></td></tr><tr><td rowspan="4">OPPO_SPOON</td><td>I</td><td></td><td>24</td><td>129</td></tr><tr><td>II</td><td></td><td>44</td><td></td></tr><tr><td>III</td><td></td><td>42</td><td></td></tr><tr><td>IV</td><td></td><td>19</td><td></td></tr><tr><td rowspan="4">OPPO_BREAD</td><td>I</td><td></td><td>91</td><td>350</td></tr><tr><td>II</td><td></td><td>141</td><td></td></tr><tr><td>III</td><td></td><td>56</td><td></td></tr><tr><td>IV</td><td></td><td>62</td><td></td></tr></table>

## DTL-HID Framework

The DTL-HID framework comprises two components: CNN-based Human Identi<sup>fi</sup>cation (CNN-HID) Model and DTL-HID Algorithm. The former extracts motion dynamics while the latter transfers knowledge learned by CNN-HID. The following subsections further detail each.

## CNN-based Human Identi<sup>fi</sup>cation (CNN-HID) Model

As discussed in the literature review, CNN’s ability to automatically learn representations from raw sensor data makes it the prevailing approach for HID. However, past studies use 1D convolution (left of Figure 4) on each axis to extract the single-axial temporal patterns [14, 30]. This approach omits valuable axial dependency depicting axis correlations and interactions. To address this issue, we design a novel CNN-HID model (right of Figure 4) that comprehensively captures both single-axial temporal and cross-axial.

The proposed CNN-HID has two parts: feature extraction and classi<sup>fi</sup>cation. Preprocessed data segments form 2D input matrices for a novel 3-layer CNN to automatically extract motion dynamics. To ensure the extracted features are temporally aligned, we use convolutions with strides instead of pooling layers in the network design [54]. The <sup>fi</sup>rst convolution layer contains two convolutional kernels, $K ^ { 1 }$ and $K ^ { 2 } , K ^ { 1 }$ is a 1D kernel that extracts temporal patterns from a single axis. The convolution result is given by

$$
c ^ {1} = K _ {1} \odot V _ {i},
$$

where $K _ { i }$ and $V _ { i }$ denote the kernel and data value on the ith row. $K ^ { 2 }$ is a 2D interaction kernel. Conventional 2D kernels in image processing are denoted as

![](/api/attachments/NSNGADKK/fulltext/images/bf7871b527acc494410f93175121ec05bc665329bccdd0d5ed894012ace0cb83.jpg)  
Conventional CNN for sensor data processing [14] (left) versus proposed CNN-HID (right).

$$
c = \sum_ {j = 0} ^ {n - 1} K _ {j} \odot V _ {i + j},
$$

where convolution is applied to n spatially adjacent rows $( V _ { i }$ to $V _ { i + n - 1 } )$ . Contrast to the common 2D kernel, CNN-HID’s 2D interaction kernel applies its rows to two distinct axes. The 2D interaction kernel output is

$$
c ^ {2} = K _ {1} \odot V _ {i} + K _ {2} \odot V _ {j} (i \neq j, i <   j).
$$

This 2D convolution captures the interactions between axis pairs (i.e., extracts cross-axial patterns which are not necessarily spatially adjacent). $c ^ { 1 }$ and $c ^ { 2 }$ are then concatenated and used as input for CNN-HID’s second layer. The kernels in the second and third layers, $K ^ { 3 }$ and $K ^ { 4 }$ , are 1D convolution kernels. Each further distills temporal and cross-axial patterns. Activation functions introduce non-linear properties into the neural networks and create nonlinear mappings between the input and outputs. Common activation functions include Sigmoid $\textstyle \sigma ( x ) = { \frac { 1 } { 1 + e ^ { - x } } }$ , hyperbolic tangent tanh $\textstyle ( x ) = { \frac { e ^ { 2 x } - 1 } { e ^ { 2 x } + 1 } }$ , and Recti<sup>fi</sup>ed Linear Units (ReLU) $\mathrm { R e L U } ( x ) = \operatorname* { m a x } ( 0 , x )$ . Among these, ReLU is widely used in modern neural networks due to its faster convergence and better learning due to the resistance to vanishing gradient [17, 35]. Due to their widespread implementation in past literature, faster convergence rates, and robustness against gradient miscalculations, we implemented ReLU for all convolution layers [30, 35]. A fully-connected layer FC weights and maps extracted features to N output nodes (N is the number of subjects) with a Sigmoid activation function. Finally, a softmax layer S computes the distribution of each category i (i.e., subject i) with

$$
p _ {i} = \frac {e ^ {z _ {j}}}{\sum_ {k = 1} ^ {N} e ^ {z _ {k}}}, j = 1, \ldots , N.
$$

Each input segment is classi<sup>fi</sup>ed to category C that maximizes $\boldsymbol { p }$ where $C = \arg \operatorname* { m a x } _ { i } p _ { i }$

The learning process of CNN-HID follows a feed-forward and back-propagation design [30, 62, 63]. To ensure model generalizability, dropout operations are applied to each convolutional layer, and an L2 regularizer is used on the fully connected layer. Consistent with past literature, output error is measured with cross-entropy $H ( p , q )$ , which denotes the divergence between the predicted and true distribution:

$$
H (p, q) = - \sum_ {x} p (x) \log q (x),
$$

where $\boldsymbol { p }$ and $q$ are two probability distributions [17]. The more similar these distributions are, the lower their cross-entropy. The calculated entropy is used by backpropagation error-correction algorithm to update network weights. This process iterates until the entropy is minimized.

## DTL-HID Algorithm

Wearable and object motion sensors capture di<sup>f</sup>erent aspects of human-object interactions during ADLs. Training on the abundant wearable motion sensor dataset ensures CNN-HID learns to extract generalizable motion dynamics for HID. Such knowledge is bene<sup>fi</sup>cial for object motion sensor-based HID as well. Therefore, we propose the threestep DTL-HID algorithm for object motion sensor-based HID as follows:

Step 1: (Learning) A CNN-HID for the source domain $\left( \mathrm { C N N - H I D _ { S } } \right)$ is trained on wearable motion sensor data to learn an optimal motion dynamics representation for source domain HID tasks. The wearable sensor dataset is the source domain data labeled with anonymized identities. Step 2: (Transferring) Construct a CNN-HID for the target domain (i.e., $\mathrm { C N N - H I D _ { T } }$ for object motion sensor) by reusing the <sup>fi</sup>rst n layers from the trained CNN-HID . The weights on the reused layers are <sup>fi</sup>xed from being changed in the next step.

Step 3: (Adaptation) $\mathrm { C N N - H I D _ { T } }$ is trained on a small amount of labeled object motion sensor data (i.e., the training set on the target domain) to adapt the feature representation from the source (i.e., wearable motion) to the target domain.2

After adaptation, we obtain $\mathrm { C N N - H I D _ { T } }$ for object motion sensor-based HID. The algorithmic formulation is as follows.

## Algorithm 1: Deep Transfer Learning for Human Identification (DTL-HID)

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Inputs:
Wearable motion sensor segments and corresponding ID labels ($X_S, Y_S$), object motion sensor adaptation segments and ID labels ($X_T, Y_T$), object motion sensor domain test segments $X_T'$, transferred layer number $n$.

Outputs:
Predicted ID labels for the test segments $\widehat{Y_T'}$

procedure DTL-HID($X_S, Y_S, X_T, Y_T, X_T', n$):
construct CNN-HIDs $\widehat{Y_S} = f_A(X_S; W_A | \Phi_A)$ for wearable sensor HID task A
$W_A^* \leftarrow argmin_{W_A} CrossEntropy(Y_S, \widehat{Y_S})$
construct CNN-HID$_T$ $\widehat{Y_T} = f_B(X_T; W_B | \Phi_B)$ for object sensor HID task B, where $W_B = \{W_A^{1*}, \cdots, W_A^{n*}, W_B^{n+1}, \cdots, W_B^{l_B}\}$ and $\Phi_B = \{\phi_A^1, \cdots, \phi_A^n, \phi_B^{n+1}, \cdots, \phi_B^{l_B}\}$.

$W_B^* \leftarrow argmin_{W_B} CrossEntropy(Y_T, \widehat{Y_T'})$
return $\widehat{Y_T'} = f_B(X_T'; W_B^* | \Phi_B)$
</div>

## Evaluation Design

Design science research emphasizes the importance of rigorously evaluating the proposed artifact to con<sup>fi</sup>rm its technical superiority against well-established benchmarks [21]. As such, four experiments are designed to evaluate the DTL-HID framework (Table 6). Experiment 1 examines whether extracting cross-axial patterns improves general HID performance. Experiment 2 evaluates if transferring the knowledge learned from wearable sensors improves HID performance on object motion sensors. Experiment 3 compares the value of transferring di<sup>f</sup>erent dependencies. Experiment 4 examines how changing the source domain data a<sup>f</sup>ects the HID performance. All experiments were conducted in Python 3.6 on a Ubuntu 18.04 virtual machine with three 3-GHz CPU kernels and 16 GB memory.

Deep learning models are implemented with Keras,<sup>1</sup> with 10% of the training data as a validation set for model selection. Training is terminated when the validation set’s cross-entropy does not improve for ten epochs. Classical machine learning benchmarks are implemented with scikit-learn with default parameters [37]. Precision, recall, and F-1 are calculated to evaluate how well the models can recognize each target class (i.e., individual). Their arithmetic means across classes (i.e., macro-averaged scores) are used as overall evaluation metrics. These macro-averaged metrics focus on the general performance across classes and bias towards classes with low classi<sup>fi</sup>cation performance. Accuracy also evaluates HID performance [3, 10, 14, 29]. In order to evaluate the actual classi<sup>fi</sup>cation performance, the accuracy score is calculated on all data samples (i.e., micro-averaged accuracy), accounting for the unbalanced class sizes in each dataset (e.g., OPPO\_SPOON, OPPO\_CUP). One-tailed paired t-tests are conducted to identify statistically signi<sup>fi</sup>cant di<sup>f</sup>erences between the best model and others.

Summary of experiment designs.

<table><tr><td>#</td><td>Model/Framework</td><td>Goal</td><td>Benchmarks</td><td>Evaluate on</td><td>Metrics</td><td>References</td></tr><tr><td>1</td><td>CNN-HID trained on HANDY</td><td>Verify the effectiveness of the CNN-HID design for HID tasks</td><td>Classical ML: kNN, SVM, NB, DT w/signal featuresDeep Learning: CNN-HID/T, CNN-HID/CA*</td><td>HANDY(30 subjects)</td><td>Precision, Recall, F-1 Score, Accuracy</td><td>[10, 23, 44]</td></tr><tr><td>2</td><td>DTL-HID w/HANDY as the source</td><td>Examine the value of transferring source domain knowledge</td><td>Deep Learning: CNN-HID, CNN-HID/T, CNN-HID/CAClassical ML: kNN, SVM, NB, DT w/signal features</td><td>OPPO_GLASS, OPPO_CUP, OPPO_SPOON, OPPO_BREAD(4 subjects)</td><td></td><td>[14]</td></tr><tr><td>3</td><td></td><td>Examine the value of transferring both types of dependencies</td><td>DTL-HID/T and DTL-HID/CA w/HANDY as source</td><td></td><td></td><td>[14]</td></tr><tr><td>4</td><td>DTL-HID w/HANDY (all seven source activities)</td><td>Examine the value of transferring different types of activities</td><td>DTL-HID w/HANDY (combinations of source activities)</td><td></td><td></td><td>[1]</td></tr></table>

Notes: \* Alternative CNN-HIDs with only $K ^ { 1 }$ or $K ^ { 2 }$ on the <sup>fi</sup>rst layer are named CNN-HID/T (extracts temporal dependency) and CNN-HID/CA (extracts axial dependency), respectively.

## Experiment 1: HID with Wearable Motion Sensor Data

Experiment 1 aims to verify CNN-HID’s e<sup>f</sup>ectiveness for HID tasks against (1) state-ofthe-art manual feature engineering algorithms and (2) alternative CNN designs that extract a speci<sup>fi</sup>c dependency type. The <sup>fi</sup>rst benchmark set includes four classical machine learning classi<sup>fi</sup>ers: kNN (k = 5, by default), SVM (polynomial kernel to avoid over<sup>fi</sup>tting), Naïve Bayes (NB), and decision tree (DT). For these benchmarks, signal features including the mean, standard deviation, minimum, and maximum of each sensor axis are extracted from each input segment [10, 23]. The second benchmark set consists of two alternative CNN-HID designs that extract only temporal (CNN-HID/T) or axial (CNN-HID/CA) dependency. All models are trained and tested using 10-fold cross-validation on the HANDY dataset.

## Experiment 2: Transfer Learning for HID on Object Motion Sensor Data

Experiment 2 examines if motion dynamics transferred from wearable motion sensor data improve HID performance on object motion sensor domain. The transferred CNN-HID model for the target domain reuses the CNN-HID pre-trained on HANDY, but reinitialized classi<sup>fi</sup>cation portion and resized the output layer to match the subject number in OPPO\_OBJ. We use all benchmark models in Experiment 1 together with an untrained CNN-HID as the non-transfer-learning benchmark. Inspired by Morales and Roggen [30], a reversed 4-fold cross-validation simulates real-world data scarcity: models are trained on one of the four randomly partitioned subsets and evaluated on the remainder. This process repeats four times, with each subset being used once as the training set.

## Experiment 3: Alternative DTL-HIDs Transferring Di<sup>f</sup>erent Types of Dependencies

Experiment 3 evaluates whether transferring both temporal and axial dependencies improves HID performance on target data. The benchmark frameworks are DTL-HID /T and DTL-HID/CA, whose CNNs are CNN-HID/T and CNN-HID/CA, respectively. All frameworks are pre-trained on the HANDY dataset to extract the motion dynamics. The transfer learning and evaluation con<sup>fi</sup>gurations are identical to Experiment 2.

## Experiment 4: DTL-HID with Di<sup>f</sup>erent Source Activities

Experiment 4 evaluates the sensitivity of the DTL-HID framework by altering the source domain activities. The seven selected source activities can be categorized into three categories based on their primary movement plane: vertical (chopping, cleaning a window, and kneading dough), horizontal (cleaning a table and using a computer mouse), and hybrid (drinking water and eating soup). We pre-train six DTL-HID variations on one or two activity categories as benchmarks. The transfer learning and evaluation con<sup>fi</sup>gurations are identical to Experiment 2.

## Results and Discussion

## Experiment 1: HID with Wearable Motion Sensor Data

We evaluated our proposed CNN-HID against state-of-the-art classical machine learning benchmarks and CNN-HID variations on the HANDY dataset. The macro-averaged HID precision, recall, F-1 score, and the micro-averaged accuracy on 30 subjects are summarized in Table 7. Top scores are highlighted in bold.

Overall, CNN-HID outperformed classical machine learning and deep learning benchmarks on all metrics. The performance di<sup>f</sup>erences between CNN-HID and benchmark algorithms are statistically signi<sup>fi</sup>cant. Within the classical machine learning benchmarks, the accuracies of kNN (0.825) and DT (0.882) were signi<sup>fi</sup>cantly better than SVM (0.288) and NB (0.094). The result indicates that the 30 subjects have distinguishable signal features within each activity. However, none of these features is generalizable to HID regardless of the underlying activities. Deep learning’s superior performance over classical machine learning suggests that automatically learning feature representations rather than manually engineering features in an ad-hoc fashion enables more e<sup>f</sup>ective HID.

Within deep learning methods, CNN-HID/CA outperformed CNN-HID/T (0.964 vs. 0.938). This result suggests that extracting cross-axial patterns instead of temporal patterns improves HID. CNN-HID extracted both types of dependencies and outperformed both CNN-HID/T and CNN-HID/CA. This indicates that more precise HID is achievable by jointly representing motion dynamics with two types of dependencies.

## Experiment 2: Transfer Learning for HID on Object Motion Sensor Data

Experiment 2 evaluates whether the motion dynamics extracted from the source domain improves the HID accuracy on the target domain (i.e., object motion sensor). All benchmarks are non-transfer-learning models. All accuracy scores on each OPPO\_OBJ datasets (i.e., OPPPO\_GLASS, OPPO\_CUP, OPPO\_SPOON, and OPPO\_BREAD) and the microaveraged accuracy score are summarized in Table 8. Figure 5 depicts macro-averaged HID precision, recall, F-1 score results, the micro-averaged receiver operating characteristic (ROC) curve, and the areas under curve (AUCs). ROC is a common approach to examine the false positive and true positive rates of models within healthcare contexts.

The DTL-HID framework obtained accuracy scores over 0.6 (0.610 for Glass, 0.778 for Cup, 0.660 for Spoon, and 0.652 for Bread) for all four test datasets. It outperformed all non-transfer-learning benchmarks with statistically signi<sup>fi</sup>cant margins (Table 8, AUCs in Figure 5). Figure 5 also shows that DTL-HID outperformed all benchmarks in precision, recall, and F-1 score. The low performance of these benchmark methods demonstrates the di<sup>fi</sup>culty of using object motion sensor data for HID in real life. Among the benchmarks, deep learning models’ large number of trainable weights leads to over<sup>fi</sup>tting, resulting in worse performance than classical machine learning models. The ROC curve of DTL-HID demonstrates that while most recognitions are accurate (false positive rate (FPR)  0, $0 \leq \mathrm { t r u e }$ positive rate $\left( \mathrm { T P R } \right) \le 0 . 6 )$ , DTL-HID can still be improved by better distinguishing the <sup>fi</sup>rst and second most likely subjects $( 0 \leq \mathrm { F P R } ~ \leq 0 . 3 8 , ~ 0 . 6 ~ \leq \mathrm { T P R } ~ \leq 0 . 9 6 )$ (Figure 5).

HID performances for the CNN-HID against benchmark classi<sup>fi</sup>ers on HANDY dataset.

<table><tr><td>Benchmark Category</td><td>Model</td><td>Precision</td><td>Recall</td><td>F-1 Score</td><td>Accuracy</td></tr><tr><td rowspan="5">Classical ML Benchmarks</td><td>CNN-HID</td><td>0.984</td><td>0.983</td><td>0.984</td><td>0.984</td></tr><tr><td>kNN w/Signal Features</td><td>0.822***</td><td>0.823***</td><td>0.822***</td><td>0.825***</td></tr><tr><td>SVM w/Signal Features</td><td>0.356***</td><td>0.273***</td><td>0.281***</td><td>0.288***</td></tr><tr><td>NB w/Signal Features</td><td>0.120***</td><td>0.095***</td><td>0.080***</td><td>0.094***</td></tr><tr><td>DT w/Signal Features</td><td>0.881***</td><td>0.881***</td><td>0.881***</td><td>0.882***</td></tr><tr><td rowspan="2">Deep Learning Benchmarks</td><td>CNN-HID/T</td><td>0.940***</td><td>0.936***</td><td>0.937***</td><td>0.938***</td></tr><tr><td>CNN-HID/CA</td><td>0.964***</td><td>0.962***</td><td>0.963***</td><td>0.964***</td></tr></table>

Notes: \*p-value < 0.05. \*\*p-value < 0.01. \*\*\*p-value < 0.001.

HID accuracies for the DTL-HID framework against non-transfer-learning benchmarks.

<table><tr><td>Benchmark Category</td><td>Model</td><td>Glass</td><td>Cup</td><td>Spoon</td><td>Bread</td><td>Micro-Averaged</td></tr><tr><td>-</td><td>DTL-HID</td><td>0.610</td><td>0.778</td><td>0.660</td><td>0.652</td><td>0.707</td></tr><tr><td rowspan="3">Deep Learning</td><td>CNN-HID</td><td>0.362***</td><td>0.593***</td><td>0.326***</td><td>0.509***</td><td>0.508***</td></tr><tr><td>CNN-HID/T</td><td>0.322***</td><td>0.429***</td><td>0.322***</td><td>0.459***</td><td>0.407***</td></tr><tr><td>CNN-HID/CA</td><td>0.392***</td><td>0.589***</td><td>0.381***</td><td>0.500***</td><td>0.514***</td></tr><tr><td rowspan="4">Classical ML</td><td>kNN w/Signal Features</td><td>0.465***</td><td>0.572***</td><td>0.433***</td><td>0.437***</td><td>0.509***</td></tr><tr><td>SVM w/Signal Features</td><td>0.455***</td><td>0.532***</td><td>0.495***</td><td>0.540***</td><td>0.517***</td></tr><tr><td>NB w/Signal Features</td><td>0.426***</td><td>0.400***</td><td>0.423***</td><td>0.411***</td><td>0.409***</td></tr><tr><td>DT w/Signal Features</td><td>0.495***</td><td>0.618***</td><td>0.402***</td><td>0.589***</td><td>0.570***</td></tr></table>

Notes: \*p-value < 0.05. \*\*p-value < 0.01. \*\*\*p-value < 0.001.

Although the motion dynamics that DTL-HID framework extracted were from a source dataset that is not related to our test set (i.e., collected with di<sup>f</sup>erent sensors during relevant but least-overlapped activities), transferring such knowledge (i.e., network structure and weights) still improved the HID performance on target data. The <sup>fi</sup>nding indicates that transferring motion dynamics from wearable motion sensors is a viable approach to resolve the issue of lacking labeled training data for object motion sensorbased HID tasks.

## Experiment 3: Alternative DTL-HIDs Transferring Di<sup>f</sup>erent Types of Dependencies

Experiments 1 and 2 examined the value of CNN-HID for general and transfer learningbased HID tasks. Experiment 3 further explores the transferability of di<sup>f</sup>erent dependencies from the source domain. The HID accuracy scores of three deep transfer learning frameworks on di<sup>f</sup>erent objects are reported in Table 9. Table 10 summarizes HID precision, recall, and F-1 score.

![](/api/attachments/NSNGADKK/fulltext/images/9392b06fa916faf082fd47d6817189e451c92ec801039d2c1a1beed35cdabf6b.jpg)

![](/api/attachments/NSNGADKK/fulltext/images/829b62390a606ab2534e560875543a79e516c56aac950f80e8e1b8642f65f827.jpg)  
(Left) HID performance comparison and (right) ROC curves for the DTL-HID framework and <sup>Figure 5.</sup>non-transfer-learning benchmarks.

HID accuracies for the DTL-HID framework against other DTL frameworks.

<table><tr><td>Model</td><td>Glass</td><td>Cup</td><td>Spoon</td><td>Bread</td><td>Micro-Averaged</td></tr><tr><td>DTL-HID</td><td>0.610</td><td>0.778</td><td>0.660</td><td>0.652</td><td>0.707</td></tr><tr><td>DTL-HID/T</td><td>0.536***</td><td>0.710***</td><td>0.553**</td><td>0.670</td><td>0.655***</td></tr><tr><td>DTL-HID/CA</td><td>0.577</td><td>0.700***</td><td>0.637</td><td>0.677</td><td>0.667*</td></tr></table>

Notes: \*p-value < 0.05. \*\*p-value < 0.01. \*\*\*p-value < 0.001.

HID performances for the DTL-HID framework against <sup>Table 10.</sup>other DTL frameworks.

<table><tr><td>Model</td><td>Precision</td><td>Recall</td><td>F-1 Score</td></tr><tr><td>DTL-HID</td><td>0.711</td><td>0.700</td><td>0.703</td></tr><tr><td>DTL-HID/T</td><td>0.668**</td><td>0.652***</td><td>0.657**</td></tr><tr><td>DTL-HID/CA</td><td>0.672*</td><td>0.663*</td><td>0.667*</td></tr></table>

Notes: \*p-value < 0.05. \*\*p-value < 0.01. \*\*\*p-value < 0.001.

Overall, the DTL-HID framework, which transfers both dependency types, achieves the highest identi<sup>fi</sup>cation performance (Tables 9 and 10). Its micro-averaged accuracy (0.707) is statistically signi<sup>fi</sup>cantly higher compared with those of the benchmarks (0.655 for DTL-HID/T and 0.667 DTL-HID/CA). The result indicates extracting and transferring both dependency types can lead to more robust motion dynamics representations for HID tasks.

DTL-HID/CA showed higher accuracy than DTL-HID/T within each test set. On OPPO\_GLASS, DTL-HID/CA outperformed DTL-HID/T (0.577 vs. 0.536) with a p-value of 0.03. DTL-HID/CA (0.637) also outperformed DTL-HID/T (0.553) with a p-value of 0.007 on OPPO\_SPOON. The performance di<sup>f</sup>erences were not signi<sup>fi</sup>cant on the Cup and Bread datasets. Therefore, cross-axial patterns can more comprehensively capture generalizable motion dynamics for HID than single-axial temporal patterns.

## Experiment 4: DTL-HID with Di<sup>f</sup>erent Source Activities

Experiments 2 and 3 demonstrated that using deep transfer learning framework and transferring both temporal and cross-axial dependencies improved HID performance with scarce object sensor data. Experiment 4 further examined the impact of altering source activity types. The HID accuracies of DTL-HIDs pre-trained on di<sup>f</sup>erent source activity combinations are reported in Table 11.

HID accuracies for the DTL-HID framework with di<sup>f</sup>erent source activity combinations.

<table><tr><td>Source Activities</td><td># Types</td><td>Glass</td><td>Cup</td><td>Spoon</td><td>Bread</td><td>Micro-Averaged</td></tr><tr><td>All</td><td>3</td><td>0.610</td><td>0.778</td><td>0.660</td><td>0.652</td><td>0.707</td></tr><tr><td>No-hybrid</td><td>2</td><td>0.525***</td><td>0.687***</td><td>0.580**</td><td>0.567***</td><td>0.593***</td></tr><tr><td>No-vertical</td><td></td><td>0.486***</td><td>0.673***</td><td>0.553***</td><td>0.578***</td><td>0.579***</td></tr><tr><td>No-horizontal</td><td></td><td>0.548**</td><td>0.694***</td><td>0.551***</td><td>0.621</td><td>0.610***</td></tr><tr><td>Hybrid-only</td><td>1</td><td>0.501***</td><td>0.629***</td><td>0.516***</td><td>0.570***</td><td>0.561***</td></tr><tr><td>Vertical-only</td><td></td><td>0.522***</td><td>0.682***</td><td>0.542***</td><td>0.547***</td><td>0.578***</td></tr><tr><td>Horizontal-only</td><td></td><td>0.511***</td><td>0.668***</td><td>0.491***</td><td>0.533***</td><td>0.555***</td></tr></table>

Notes: \*p-value < 0.05. \*\*p-value < 0.01. \*\*\*p-value < 0.001.

Overall, DTL-HID pre-trained on all three activity types yielded the best HID accuracies in our synthesized four-resident setting. This indicates that the diversity of collected source domain activities can signi<sup>fi</sup>cantly a<sup>f</sup>ect HID outcome. Among the three benchmarks pre-trained on two activity types, the one pre-trained on Nohorizontal (i.e., vertical and hybrid activities) had the best HID accuracy (0.610 vs. 0.593 and 0.579). This <sup>fi</sup>nding suggests that practitioners can exclude horizontal activities in source domain data collection if there exist cost or time constraints. Similarly, we found vertical activities (e.g., cleaning a window, chopping, and kneading dough) o<sup>f</sup>ered the most informative motion dynamics for HID, leading to the most accurate HID among the three benchmarks pre-trained on one activity type (0.578 vs. 0.561 and 0.555). These results can help practitioners prioritize their source data collection accordingly.

## Case Study: Human Identi<sup>fi</sup>cation for a Water Drinking Activity

In addition to rigorously evaluating a novel IT artifact with a series of technical experiments, numerous IS scholars emphasized the importance of demonstrating the proof-ofconcept and proof-of-value with an in-depth case study [32, 33, 38]. Such a demonstration serves two purposes. First, it helps illustrate examples wherein the proposed approach correctly detects instances within the application environment missed by best competing approaches (as identi<sup>fi</sup>ed through the technical experiments). Second, they illustrate the potential practical utility of the proposed approach. To this end, we illustrate DTL-HID’s utility and value against non-transfer-learning methods with a water drinking activity case study. Drinking water is a common but critical component of various ADLs. These include self-feeding (basic) and taking medication as prescribed (instrumental). Human identi<sup>fi</sup>cation for such an activity helps ADL monitoring systems accurately track the activities of di<sup>f</sup>erent residents. Figure 6 decomposes the stage of a water drinking activity from OPPO\_CUP.

Screenshots in Figure 6 are extracted at 1.5-second intervals from the sample video<sup>2</sup>. This decomposition allows us to better locate, analyze, and interpret drinking activities from case study samples. All these samples were correctly classi<sup>fi</sup>ed by DTL-HID but not CNN-HID nor DT, the two best-performing non-transfer-learning benchmarks for deep learning and feature engineering approaches, respectively (Table 8).

Figure 7 illustrates two cup motion segments from Subject 4. Both contain similar Stage 3 patterns (gray box) recorded at di<sup>f</sup>erent periods within the segment (top: 5.2\~7.3 s; bottom: 1.6\~4 s). The proposed DTL-HID correctly recognized these temporally invariant salient patterns. Since these features are not commonly included for sensor signal analysis, DT missed these patterns and misclassi<sup>fi</sup>ed both segments. While CNN-HID automatically extracts temporally invariant features, not transferring motion dynamics from the source domain prevented it from learning these patterns.

Figure 8 shows two cup motion segments from Subjects 1 and 2. The proposed DTL-HID successfully recognized acceleration amplitude di<sup>f</sup>erences in Stage 5 (left boxes; top: −5\~2; bottom: −5.8\~3) and the following Stage 3 (right boxes; top: −1.5\~1.5; bottom: −2.3\~2). This result indicates DTL-HID can better distinguish between extreme (i.e., fast) and mild (i.e., slow) motions than non-transfer-learning methods.

![](/api/attachments/NSNGADKK/fulltext/images/3f38291a4bcc9e8a6cf05cbd6bd5f4e2178d81e755602becdbf8bc59cc698a20.jpg)  
1. Reach → 2. Pick up → 3. Drink — 4. Put down →5. Release

Coffee Cup Motion  
![](/api/attachments/NSNGADKK/fulltext/images/1076201b45736719f605cc641e19f7c9ea6b21bc1f795644e6b2842a2e973d7e.jpg)

A drinking activity demonstration. A general drinking activity can be decomposed to 5 stages: <sup>Figure 6.</sup>(1) reach, (2) pick up, (3) drink, (4) put down, and (5) release. During Stages 1 and 5, the cup maintains stable positions (i.e., without volatile movements). During Stages 2 and 4, the cup moves rapidly, both accelerates and decelerates, along the desired direction (i.e., up and down). The cup rotates during Stage 3, resulting in the transformed acceleration readings. All <sup>fi</sup>ve stages contain distinct motion patterns. Di<sup>f</sup>erent subjects could demonstrate personal signatures within or across stages.  
![](/api/attachments/NSNGADKK/fulltext/images/e17f50baefd96f2c7d242d4e14ca1f47b828dc4520be7c8ee356a4ca365339a1.jpg)

![](/api/attachments/NSNGADKK/fulltext/images/2fe2ee5ff6e4d11ad7fca2c5cce3eaf840f83888214964ec0786a0ac77851304.jpg)  
Two cup motion samples from subject 4.

![](/api/attachments/NSNGADKK/fulltext/images/74a8a65394a59750fd309376e9f9d6a7f6ed4442dc3b531ceee203abc9295be7.jpg)

![](/api/attachments/NSNGADKK/fulltext/images/b7b1edee54e0f79935a9b4b03edffb35568fcd120a2f80cd7605cdb96ebb3219.jpg)  
Cup motion segments from subjects 1 and 2.

In all cases, DTL-HID leverages transferred knowledge from the source domain to automatically extract salient, temporally-invariant features. It also recognizes distinct motion amplitudes across activity stages and subjects. These results illustrate how DTL-HID better captures key individual di<sup>f</sup>erences for object sensor-based human identi<sup>fi</sup>cation as compared with non-transfer-learning benchmarks.

## Conclusion and Future Directions

The growing societal concerns on the aging population’s well-being necessitate a more a<sup>f</sup>ordable, predictive, preventive, and personalized care solution for elderly citizens. With the advancement in mobile sensing technology, object motion sensor-based ADL monitoring systems have emerged to meet such requirements for their abilities to capture granular, high-resolution activity data passively. However, these systems su<sup>f</sup>er from scarce labeled training data and can be confused by di<sup>f</sup>erent residents interacting with the same object. Moreover, extant approaches to analyze sensor signal data employ traditional machine learning approaches that rely on ad-hoc and laborious feature engineering e<sup>f</sup>orts.

In this study, we adopt the design science paradigm to design, develop, and evaluate an innovative deep transfer learning framework for object motion sensor-based human identi<sup>fi</sup>cation. Within this framework, a novel CNN-HID is designed to extract both crossaxial and temporal patterns from sensor data. The framework transfers the patterns learned from the rich wearable motion sensor data to improve HID accuracy on object motion sensor data. The framework allows us to accurately identify the activity performer even only a small number of labeled data is given. Our approach is generalizable to mobile sensors with di<sup>fi</sup>culties to obtain labeled data.

Following the design science paradigm, we search a solution space for e<sup>f</sup>ective computational models of practical utility (e.g., CNN-HID model, DTL-HID framework) [5, 32, 34, 43, 48]. The novel CNN-HID model and DTL-HID framework are IT artifact instantiations that comprehensively address the practical problem within the domain [33, 38]. Two design principles are contributed in the form of nascent design theory (i.e., knowledge as operation principles or architectures). First, extracting temporal and axial local dependencies can capture richer information from multiaxial sensor data for di<sup>f</sup>erent applications. This principle contributes to the higher HID accuracy of our DTL-HID framework on di<sup>f</sup>erent datasets. Future mobile health researchers can extract more information from multichannel sensors (e.g., EEG) to improve the performance of healthcare applications (e.g., seizure detection). Second, transfer learning from a source domain that is similar to the target domain and easier to train with su<sup>fi</sup>cient data can potentially boost the performance of the desired task on the target domain with scarce data. Future IS researchers facing scarce data issues can adopt this guideline and potentially develop a transfer learning framework for their application. The IT artifact development, the rigorously designed evaluations, and the demonstrated case study validate these design principles and their applicability [18, 21, 41, 48].

Beyond the research contributions to the IS knowledge base, this study also contributes practical implications for stakeholders such as clinicians, caregivers, and senior citizens. With the proposed approach, clinicians will be able to obtain more accurate activity monitoring report for prescriptions when the patient lives in a multi-resident environment. Caregivers within an assisted living community can better distinguish di<sup>f</sup>erent residents’ activities within the shared area, such as a dining hall. Senior citizens can be monitored on activities of interest (e.g., dining activity) without attaching/detaching wearable sensors regularly.

Future studies can expand this work in several promising directions. First, misclassifying an activity performer (i.e., false positive/false negative) can a<sup>f</sup>ect downstream task performances (e.g., inaccurate ADL recognition/ADL pattern monitoring), also hindering the ability to provide and the reliability of personalized care. To mitigate these risks, future DTL-HID models can couple with temporal activity modeling in an active learning framework for high-level multi-resident ADL monitoring. DTL-HID can group activities by performers for temporal activity modeling; in return, temporal modeling establishes activity contexts (e.g., food preparation, housework) to detect and reject misclassi<sup>fi</sup>ed object activities. These misclassi<sup>fi</sup>ed activities can be reported to practitioners as detected anomalies for examination and be used to improve DTL-HID’s performance iteratively. Second, a deep multi-source learning framework can potentially extract and integrate various types of transferable knowledge from di<sup>f</sup>erent source domains (e.g., sensor modalities) for better transfer learning performance. Third, Bayesian learning frameworks such as Bayesian Deep Learning [15] can also leverage the high-level activity in which the subject and the object interact as a prior to distinguish motion patterns of the same object in di<sup>f</sup>erent activities. Finally, this framework may also apply to other healthcare devices equipped with multiple sensors (e.g., EEG) or the emerging IoT-enable smart home settings for improved healthcare and home intelligence. Each of these research directions can help signi<sup>fi</sup>cantly improve the usability and reliability of sensor- and smart device-based home care systems, ultimately contributing to a more supportive and intelligent home environment for senior citizens.

## Notes

1. https://github.com/keras-team/keras

2. https://vimeo.com/8704668

## Acknowledgements

This project is funded by NSF awards IIP-1622788 and IIP-1417181.

## References

1. Açıcı, K.; Erdaş, Ç.B.; Aşuroğlu, T.; and Oğul, H. HANDY: A Benchmark dataset for context-awareness via wrist-worn motion sensors. Data, 3, 3 (June 2018), 24.

2. Administration on Aging. A pro<sup>fi</sup>le of older American: 2013. 2013. www.aoa.acl.gov/Aging\_ Statistics/Pro<sup>fi</sup>le/2013/docs/2013\_Pro<sup>fi</sup>le.pdf.

3. Al-Naimi, I.; Wong, C.B.; Moore, P.; and Chen, X. Multimodal approach for non-tagged indoor identi<sup>fi</sup>cation and tracking using smart <sup>fl</sup>oor and pyroelectric infrared sensors. International Journal of Computational Science and Engineering, 14, 1 (2017), 1.

4. Alsheikh, M.A.; Selim, A.; Niyato, D.; Doyle, L.; Lin, S.; and Tan, H.-P. Deep activity recognition models with triaxial accelerometers. In AAAI Workshop: Artificial Intelligence Applied to Assistive Technologies and Smart Environments, 2016.

5. Baskerville, R.; Baiyere, A.; Gergor, S.; Hevner, A.; and Rossi, M. Design science research contributions: <sup>fi</sup>nding a balance between artifact and theory. Journal of the Association for Information Systems, 19, 5 (May 2018), 358–376.

6. Bengio, Y.; Courville, A.; and Vincent, P. Representation learning: A review and new perspectives. IEEE Transactions on Pattern Analysis and Machine Intelligence, 35, 8 (2013), 1798–1828.

7. Burlina, P.; Pacheco, K.D.; Joshi, N.; Freund, D.E.; and Bressler, N.M. Comparing humans and deep learning performance for grading AMD: a study in using universal deep features and transfer learning for automated AMD analysis. Computers in Biology and Medicine, 82, (March 2017), 80–86.

8. Census Bureau. The nation’s older population is still growing. Census Bureau Reports, 2017. https://www.census.gov/newsroom/press-releases/2017/cb17-100.htm.

9. Cook, D.; Feuz, K.D.; and Krishnan, N.C. Transfer learning for activity recognition: a survey. Knowledge and Information Systems, 36, 3 (2013), 537–556.

10. Corpus, K.R.; Gonzales, R.J.D.; Morada, A.S.; and Vea, L.A. Mobile user identi<sup>fi</sup>cation through authentication using keystroke dynamics and accelerometer biometrics. In Proceedings of the International Workshop on Mobile Software Engineering and Systems - MOBILESoft ’16. 2016, pp. 11–12.

11. Coutinho, E.; and Schuller, B. Shared acoustic codes underlie emotional communication in music and speech—evidence from deep transfer learning. PLoS ONE, 12, 6 (2017).

12. Debes, C.; Merentitis, A.; Sukhanov, S.; Niessen, M.; Frangiadakis, N.; and Bauer, A. Monitoring activities of daily living in smart homes: understanding human behavior. IEEE Signal Processing Magazine, 33, 2 (March 2016), 81–94.

13. Eurostat. Population structure and ageing. 2017. http://ec.europa.eu/eurostat/statisticsexplained/index.php/Population\_structure\_and\_ageing.

14. Gadaleta, M.; Merelli, L.; and Rossi, M. Human authentication from ankle motion data using convolutional neural networks. In IEEE Workshop on Statistical Signal Processing Proceedings. 2016.

15. Gal, Y. Uncertainty in Deep Learning. PhD Thesis, University of Cambridge, (2016).

16. Golubnitschaja, O.; Kinkorova, J.; and Costigliola, V. Predictive, preventive and personalised medicine as the hardcore of “horizon 2020”: EPMA position paper. EPMA Journal, 5, 1 (2014).

17. Goodfellow, I.; Bengio, Y.; Courville, A.; and Bengio, Y. Deep learning. MIT press Cambridge, 2016.

18. Gregor, S.; and Hevner, A.R. Positioning and Presenting Design Science Research for Maximum Impact. MIS Quarterly, 37, 2 (2013), 337–355.

19. Hammerla, N.Y.; Halloran, S.; and Ploetz, T. Deep, convolutional, and recurrent models for human activity recognition using wearables. In Proceedings of the Twenty-Fifth International Joint Conference on Artificial Intelligence. 2016, pp. 1533–1540.

20. Hardy, S.E. Consideration of function & functional decline. In B.A. Williams, A. Chang, C. Ahalt, H. Chen, R. Conant, C.S. Landefeld, C. Ritchie, and M. Yukawa (eds.), Current Diagnosis & Treatment: Geriatrics. McGraw-Hill, New York, NY, 2014, pp. 3–4.

21. Hevner, A.R.; March, S.T.; Park, J.; and Ram, S. Design science in information systems research. MIS Quarterly, 28, 1 (2004), 75–105.

22. Ignatov, A. Real-time human activity recognition from accelerometer data using Convolutional Neural Networks. Applied Soft Computing, 62, (2018), 915–922.

23. Jain, A.; and Kanhangad, V. Investigating gender recognition in smartphones using accelerometer and gyroscope sensor readings. In 2016 International Conference on Computational Techniques in Information and Communication Technologies, ICCTICT 2016 - Proceedings. 2016, pp. 597–602.

24. Kandaswamy, C.; Silva, L.M.; Alexandre, L.A.; and Santos, J.M. High-Content Analysis of Breast Cancer Using Single-Cell Deep Transfer Learning. Journal of Biomolecular Screening, 21, 3 (2016), 252–259.

25. Kermany, D.S.; Goldbaum, M.; Cai, W.; Valentim, C.C.; Liang, H.; Baxter, S.L.; McKeown, A.; Yang, G.; Wu, X.; Yan, F.; and Dong, J. Identifying medical diagnoses and treatable diseases by image-based deep learning. Cell, 172, 5 (February 2018), 1122-1131.e9.

26. Knowles, B.; and Hanson, V.L. The wisdom of older technology (non)users. Communications of the ACM, 61, 3 (February 2018), 72–77.

27. LeCun, Y.; Bengio, Y.; and Hinton, G. Deep learning. Nature, 521, 7553 (May 2015), 436–444.

28. Mishra, A.; and Agrawal, D.P. Continuous health condition monitoring by 24x7 sensing and transmission of physiological data over 5-G cellular channels. In 2015 International Conference on Computing, Networking and Communications (ICNC). IEEE, 2015, pp. 584–590.

29. Mokhtari, G.; Zhang, Q.; Hargrave, C.; and Ralston, J.C. Non-wearable UWB sensor for Human identi<sup>fi</sup>cation in smart home. IEEE Sensors Journal, 17, 11 (2017), 3332–3340.

30. Morales, F.J.O.; and Roggen, D. Deep convolutional feature transfer across mobile activity recognition domains, sensor modalities and locations. In Proceedings of the 2016 ACM International Symposium on Wearable Computers - ISWC ’16. ACM Press, New York, New York, USA, 2016, pp. 92–99.

31. Nabiei, R.; Parekh, M.; Jean-Baptiste, E.; Jancovic, P.; and Russell, M. Object-centred recognition of human activity. In 2015 International Conference on Healthcare Informatics. IEEE, 2015, pp. 63–68.

32. Nunamaker, J.F.; Briggs, R.O.; Derrick, D.C.; and Schwabe, G. The last research mile: achieving both rigor and relevance in information systems research. Journal of Management Information Systems, 32, 3 (2015), 10–47.

33. Nunamaker, J.F.; Chen, M.; and Purdin, T.D.M. Systems development in information systems research. Journal of Management Information Systems, 7, 3 (1990), 89–106.

34. Nunamaker, J.F.; Twyman, N.W.; Giboney, J.S.; and Briggs, R.O. Creating high-value real-world impact through systematic programs of research. MIS Quarterly, 41, 2 (2017), 335–351.

35. Ordóñez, F.; and Roggen, D. Deep convolutional and LSTM recurrent neural networks for multimodal wearable activity recognition. Sensors, 16, 12 (January 2016), 115.

36. Pan, S.J.; and Yang, Q. A Survey on Transfer Learning. IEEE Transactions on Knowledge and Data Engineering, 22, 10 (October 2010), 1345–1359.

37. Pedregosa, F.; Varoquaux, G.; Gramfort, A.; Michel, V.; Thirion, B.; Grisel, O.; Blondel, M.; Prettenhofer, P.; Weiss, R.; Dubourg, V.; and Vanderplas, J. Scikit-learn: machine learning in Python. Journal of Machine Learning Research, 12, Oct (2011), 2825–2830.

38. Pe<sup>f</sup>ers, K.; Tuunanen, T.; Rothenberger, M.A.; and Chatterjee, S. A design science research methodology for information systems research. Journal of management information systems, 24, 3 (2007), 45–77.

39. Pentland, S.J.; Twyman, N.W.; Burgoon, J.K.; Nunamaker, J.F.; and Diller, C.B.R. A Video-based screening system for automated risk assessment using nuanced facial features. Journal of Management Information Systems, 34, 4 (2017), 970–993.

40. Plötz, T.; Hammerla, N.Y.; and Olivier, P. Feature learning for activity recognition in ubiquitous computing. In Proceedings of the 22nd International Joint Conference on Artificial Intelligence (IJCAI). AAAI Press, 2011, pp. 1729–1734.

41. Prat, N.; Comyn-Wattiau, I.; and Akoka, J. A Taxonomy of evaluation methods for information systems artifacts. Journal of Management Information Systems, 32, 3 (2015), 229–267.

42. Proudfoot, J.G.; Jenkins, J.L.; Burgoon, J.K.; and Nunamaker, J.F. More than meets the eye: how oculometric behaviors evolve over the course of automated deception detection interactions. Journal of Management Information Systems, 33, 2 (2016), 332–360.

43. Rai, A. Editor’s comments: diversity of design science research. MIS Quarterly, 41, 1 (2017), iii–xviii.

44. Ranjan, J.; and Whitehouse, K. Object hallmarks: identifying object users using wearable wrist sensors. In Proceedings of the 2015 ACM International Joint Conference on Pervasive and Ubiquitous Computing (UbiComp ’15). 2015, pp. 51–61.

45. Reyes-Ortiz, J.-L.; Oneto, L.; Samà, A.; Parra, X.; and Anguita, D. Transition-aware human activity recognition using smartphones. Neurocomputing, 171, (January 2016), 754–767.

46. Roggen, D.; Calatroni, A.; Rossi, M.; Holleczek, T.; Förster, K.; Tröster, G.; Lukowicz, P.; Bannach, D.; Pirkl, G.; Ferscha, A.; and Doppler, J. Collecting complex activity datasets in highly rich networked sensor environments. In Proceedings of the 7th International Conference on Networked Sensing Systems (INSS). IEEE, 2010, pp. 233–240.

47. Sa<sup>fi</sup>, K.; Mohammed, S.; Attal, F.; Khalil, M.; and Amirat, Y. Recognition of di<sup>f</sup>erent daily living activities using Hidden Markov Model regression. In 2016 3rd Middle East Conference on Biomedical Engineering (MECBME). IEEE, 2016, pp. 16–19.

48. Samtani, S.; Chinn, R.; Chen, H.; and Nunamaker, J.F. Exploring emerging hacker assets and key hackers for proactive cyber threat intelligence. Journal of Management Information Systems, 34, 4 (2017), 1023–1053.

49. Shickel, B.; Heesacker, M.; Benton, S.; and Rashidi, P. Hashtag healthcare: from tweets to mental health journals using deep transfer learning. (August 2017). arXiv preprint arXiv:1708.01372.

50. Shin, H.C.; Roth, H.R.; Gao, M.; Lu, L.; Xu, Z.; Nogues, I.; Yao, J.; Mollura, D.; and Summers, R.M. Deep convolutional neural networks for computer-aided detection: CNN architectures, dataset characteristics and transfer learning. IEEE Transactions on Medical Imaging, 35, 5 (2016), 1285–1298.

51. Shoaib, M.; Bosch, S.; Incel, O.; Scholten, H.; and Havinga, P. A Survey of Online Activity Recognition Using Mobile Phones. Sensors, 15, 1 (January 2015), 2059–2085.

52. Simonyan, K.; and Zisserman, A. Two-stream convolutional networks for action recognition in videos. In Advances in Neural Information Processing Systems (NIPS). 2014, pp. 568–576.

53. Sprager, S.; and Juric, M. Inertial sensor-based gait recognition: a review. Sensors, 15, 9 (September 2015), 22089–22127.

54. Springenberg, J.T.; Dosovitskiy, A.; Brox, T.; and Riedmiller, M. Striving for simplicity: The All Convolutional Net. In arXiv:1412.6806, also appeared at ICLR 2015 Workshop Track.

55. Srinivasan, V.; Stankovic, J.; and Whitehouse, K. Using height sensors for biometric identi-<sup>fi</sup>cation in multi-resident homes. In Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics). 2010, pp. 337–354.

56. Teixeira, T.; Dublon, G.; and Savvides, A. A Survey of human-sensing: methods for detecting presence, count, location, track, and identity. ACM Computing Surveys, 5, (2010), 1–35.

57. Völker, M.; Schirrmeister, R.T.; Fiederer, L.D.J.; Burgard, W.; and Ball, T. Deep transfer learning for error decoding from non-invasive EEG. (October 2017).

58. Wang, J.; Zheng, H.; Huang, Y.; and Ding, X. Vehicle type recognition in surveillance images from labeled web-nature data using deep transfer learning. IEEE Transactions on Intelligent Transportation Systems, 2017.

59. Weiss, K.; Khoshgoftaar, T.M.; and Wang, D.D. A survey of transfer learning. Journal of Big Data, 3, 1 (2016).

60. World Health Organization. Life expectancy increased by 5 years since 2000, but health inequalities persist. 2016. http://www.who.int/en/news-room/detail/19-05-2016-lifeexpectancy-increased-by-5-years-since-2000-but-health-inequalities-persist.

61. Wu, Z.; Li, Y.; and Radke, R.J. Viewpoint invariant human re-identi<sup>fi</sup>cation in camera networks using pose priors and subject-discriminative features. IEEE Transactions on Pattern Analysis and Machine Intelligence, 37, 5 (2015), 1095–1108.

62. Yang, J.B.; Nguyen, M.N.; San, P.P.; Li, X.L.; and Shonali, K. Deep convolutional neural networks on multichannel time series for human activity recognition. In Proceedings of the 24th International Conference on Artificial Intelligence (IJCAI). 2015, pp. 3995–4001.

63. Zeng, M.; Nguyen, L.T.; Yu, B.; Mengshoel, O.J.; Zhu, J.; Wu, P.; and Zhang, J. Convolutional neural networks for human activity recognition using mobile sensors. In Proceedings of the 6th International Conference on Mobile Computing, Applications and Services. ICST, 2014, pp. 197–205.

64. Zhang, J.; Wei, B.; Hu, W.; and Kanhere, S.S. WiFi-ID: human identi<sup>fi</sup>cation using WiFi signal. In 2016 International Conference on Distributed Computing in Sensor Systems (DCOSS). 2016, pp. 75–82.

65. Zhu, H.; Chen, H.; and Brown, R. A sequence-to-sequence model-based deep learning approach for recognizing activity of daily living for senior care. Journal of Biomedical Informatics, 84, (August 2018), 148–158.

## About the Authors

(hongyi.zhu@utsa.edu; corresponding author) is an Assistant Professor at the College <sup>Hongyi Zhu</sup>of Business at the University of Texas at San Antonio. He received his Ph.D. in Management Information Systems from University of Arizona. Dr. Zhu’s research focuses on designing advanced mobile analytics for smart home care, such as recognition, extraction, and analysis of in-house behaviors from raw mobile sensors data. His work has been published or accepted in such journals as Journal of Biomedical Informatics, IEEE Intelligent Systems, MIS Quarterly, and others. He has contributed to several projects supported by the National Science Foundation.

(ssamtani@iu.edu) is an Assistant Professor and a Grant Thornton Scholar at the <sup>Sagar Samtani</sup>Kelley School of Business at Indiana University. He received his Ph.D. in Management Information Systems from the University of Arizona. Dr. Samtani’s research initiatives have garnered nearly \$1.5M in funding, including by the National Science Foundation programs. His research has been published or accepted in such journals as Journal of Management Information Systems, IEEE Intelligent Systems, MIS Quarterly, and others. His research has also received signi<sup>fi</sup>cant media coverage.

(hchen@eller.arizona.edu) is Regents Professor and Thomas R. Brown Chair in <sup>Hsinchun Chen</sup>Management and Technology at the Eller College of Management, University of Arizona. He received his Ph.D. in Information Systems from New York University. He is author or editor of 20 books, 300 journal papers, and 200 refereed conference articles covering digital library, data/ text/web mining, business analytics, security informatics, and health informatics. He served as the lead Program Director of the Smart and Connected (SCH) Program at the National Science Foundation (NSF). Dr. Chen founded the Arti<sup>fi</sup>cial Intelligence Lab at University of Arizona, which has received \$50M+ research funding from the NSF, National Institutes of Health, National Library of Medicine, Department of Defense, Department of Justice, Central Intelligence Agency, Department of Homeland Security, and other agencies. He is a Fellow of ACM, IEEE, and AAAS.

. (jnunamaker@cmi.arizona.edu) is Regents and Soldwedel Professor of <sup>Jay F. Nunamaker Jr</sup>MIS, Computer Science and Communication, and director of the Center for the Management of Information and the National Center for Border Security and Immigration at the University of Arizona. He received his Ph.D. in Operations Research and Systems Engineering from Case Institute of Technology. Dr. Nunamaker has held a professional engineer’s license since 1965. He was inducted into the Design Science Hall of Fame and received the LEO Award for Lifetime Achievement from the Association for Information Systems. He was featured in the July 1997 issue of Forbes Magazine on technology as one of eight key innovators in information technology. His specialization is in the <sup>fi</sup>elds of system analysis and design, collaboration technology, and deception detection. The commercial product GroupSystems ThinkTank, based on his research, is often referred to as the gold standard for structured collaboration systems. He founded the MIS Department at the University of Arizona and served as department head for 18 years.
