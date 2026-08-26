---
otero_id: 25440
otero_key: "NYV8D64F"
title: "Fall Detection with Wearable Sensors: A Hierarchical Attention-based Convolutional Neural Network Approach"
authors: "Shuo Yu; Yidong Chai; Hsinchun Chen; Randall A. Brown; Scott J. Sherman; Jay F. Nunamaker"
year: "2021"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2021.1990617"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Check for updates

# Fall Detection with Wearable Sensors: A Hierarchical Attention-based Convolutional Neural Network Approach

Shuo Yu<sup>a</sup>, Yidong Chai<sup>b</sup>, Hsinchun Chen<sup>c</sup>, Randall A. Brown<sup>d</sup>, Scott J. Sherman<sup>e</sup>, and Jay F. Nunamaker Jr.<sup>c</sup>

<sup>a</sup>Area of Information Systems and Quantitative Sciences, Rawls College of Business, Texas Tech University, Lubbock, TX 79409; <sup>b</sup>Department of Electronic Commerce, School of Management, Hefei University of Technology, Hefei, Anhui 230011, China; <sup>c</sup>Department of Management Information Systems, University of Arizona, Tucson, AZ 85721; <sup>d</sup>Hermes Medical Intelligence, LLC, Tucson, AZ 85721; <sup>e</sup>Department of Neurology, University of Arizona, Tucson, AZ 85721

## ABSTRACT

Falls are among the most life-threatening events that challenge senior citizens’ independent living. Wearable sensor technologies have emerged as a viable solution for fall detection. However, existing fall detection models either focus on manual feature engineering or lack explainability. To advance the state-of-the-art of wearable sensor-based health management, we follow the computational design science paradigm and develop a deep learning model to detect falls based on wearable sensor data. We propose a Hierarchical Attention-based Convolutional Neural Network (HACNN) to optimize the model efectiveness. We collected two large publicly available datasets to evaluate our fall detection model. We conduct extensive evaluations on our proposed HACNN and discuss a case study to illustrate its advantage and explainability, that could guide future set-ups for fall detection systems. We contribute to the information systems (IS) knowledge base by enabling explainable fall detection for chronic disease management. We also contribute to the design science theory by proposing generalizable design principles in model building.

## KEYWORDS

design science; chronic disease management; convolutional neural networks; hierarchical attention mechanism; fall detection; wearable sensors; learning systems explainability

## Introduction

People are enjoying longer life due to advances in medicine and public health services. The life expectancy of the United States is 77.8 years in 2020 [5]. However, population aging has also been an increasing societal concern. In 2019, 54.1 million United States (U.S.) citizens (16.5 percent of the total population) are at the age of 65 or older [68]. Senior citizens face many challenges to their independent living, including a decline in mobility or cognition and having chronic physical health conditions. Such conditions may include frailty, diabetes, Parkinson’s disease, dementia, stroke, falls, etc. Among these, falls can be one of the most severe threats afecting senior citizens’ lives as approximately 30 percent of adults aged 65 and over fall each year [13]. In addition to the direct injuries from falls, many fallers are unable to get up again without assistance, leading to a “long lie” situation. This subsequent situation can lead to hypothermia, dehydration, bronchopneumonia, and pressure sores, which increases the severity of falls [54] [66]. More than 20 percent of patients admitted to hospitals because of a fall were on the ground for an hour or more, and their morbidity rates within 6 months were very high. There were 24,190 fatal falls and 3.2 million non-fatal fall injuries in 2012; the average cost was \$26,340 for a fatal fall and \$9,780 for a non-fatal fall. In the U.S., fatal falls were estimated to cost \$637.2 million and non-fatal falls \$31.3 billion in 2015 alone [16].

Despite the severe consequences of falls, timely assistances after the occurrence of falls can reduce the risk of hospitalization by 26 percent and that of death by 80 percent [58]. Such assistances not only provide first aid for direct injuries but also alleviate long lie situations. However, those assistances often require human caregivers who live with the senior citizens to call emergency services and obtain help. This may be infeasible for many senior citizens who live alone. To address this need, wearable sensor-based information systems (IS) have emerged as a low-cost and non-intrusive means by practitioners and researchers to detect falls for the elderly. With high sampling frequency (up to 200 Hz, i.e., 200 data points per second), inexpensive wearable sensors (about \$15 each) are able to track seniors’ movements and capture falls with an analytical engine, after which care giving facility could be automatically notified and then dispatch personnel for assistance even if the seniors have become unconscious.

Although sensor-based fall detection has been an active research field for years, extant studies confront the following challenges. First, prevailing fall detection models apply a traditional manual feature extraction approach on wearable sensor data. This approach is ad hoc, labor-intensive, and could lead to inconclusive results [31]. Second, although several deep learning-based models have been proposed for fall detection, such models remain “black boxes” with limited explainability. Users are not able to identify how and why the model reaches a given decision, which could be a critical issue for chronic disease management tasks like fall detection. A model that could integrate explainability into its design could yield a more accurate and convincing detection of falls. We ask the following questions: (1)How to advance the state-of-the-art of wearable sensor-based fall detection? (2) How to improve the explainability of deep learning models for fall detection to guide future set-ups of fall detection systems? These questions motivate an innovative IT artifact for wearable sensor-based fall detection.

In recent top IS journals, chronic disease management has become a significant focus of the IS community [10] [43] [83]. Despite the efectiveness of wearable sensors in fall detection and IS scholars’ interest in mobile technologies [70] [65], to the best of our knowledge, no IT artifacts have been proposed for sensor-based fall detection. With the guidance of the computational design science paradigm [52] and prior IS research on chronic disease management [41] [43] [83], we propose and extensively evaluate a novel deep learning framework, Hierarchical Attention-based Convolutional Neural Networks (HACNN). Drawing upon Convolutional Neural Networks (CNN) as a significant deep learning branch and the emerging hierarchical attention mechanism, HACNN addresses the limitations in existing sensor-based fall detection studies by automatically extracting features from wearable sensor data and adopting the hierarchical attention mechanism to improve model explainability, both at a sensor axis level and at a sensor position (or sensor type) level. We conduct rigorous benchmark experiments to evaluate the proposed HACNN against state-of-the-art feature-based and deep learning models on two large fall detection datasets. We also demonstrate the utility of the HACNN through a case study.

The major contributions of our HACNN are as follows. First, we integrate the hierarchical attention mechanism into existing CNN models and propose a novel variation of deep learning model that specializes in explainable fall detection. By adding two attention layers beyond CNN, we are able to identify which part of sensor data contribute the most to the decision made by the model (fall or non-fall), which can help practitioners understand the occurring falls. Second, the proposed HACNN serves as a good template for future wearable sensor-related research. The extensive experiments and discussion in this work can guide future research in choosing model designs and hyperparameters on similar applications.

The remainder of the paper is organized as follows. In the next section, we review the literature on existing IS works on health and mobile analytics, sensor-based fall detection, and introduction to deep learning (CNN) and attention mechanism. We then present our research design of developing our HACNN for fall detection. Following that, we set up evaluations and case studies to compare the results and show the utility of our model. Finally, we discuss the contribution of this study to the IS knowledge base, consider its practical and managerial implications, and suggest future directions.

## Research Background

Our research background is informed by the following three streams of literature: (1) existing IS works on health information technology, mobile technology, and computational design science guidelines, (2) sensors and models applied in prior sensor-based fall detection studies, and (3) deep learning and its significant branches for wearable sensor-based fall detection. We then summarize research gaps and questions.

## IS Works on Health Information Technology (HIT) and Mobile Technology

Defined as “a broad concept that encompasses an array of technologies to store, share, and analyze health information” [8], HIT has long been an area of interest for IS researchers. Appendix A summarizes selected IS research on HIT based on their research topics and focuses. Recently, chronic disease management has been a topic that increasingly attracts IS researchers’ interest due to its societal relevance, as pointed out in a recent MIS Quarterly editorial [10]. Fall management is an important step in chronic disease management, because falls are closely related to numerous chronic diseases, including Parkinson’s disease, dementia, depression, etc. [61].

Meanwhile, the ever-growing usage of mobile sensors presents an unprecedented opportunity of high-velocity, always-on data collection for health analytics [21], which has also been a topic of interest in the IS community. With the technological advances on the Internet of Things (IoT), wearable sensors can play a pivotal role in chronic disease management [10]. Appendix B summarizes selected IS research on mobile technology. Although researchers have been exploring topics including mobile Web browsing and mobile apps, sensor-based mobile analytics for chronic disease management, especially for fall detection, still remains an underexplored perspective of IS literature.

The design science paradigm [28] can guide the systematic development of IT artifacts. Specifically, we focus on the computational design science perspective of IS [52] whose main objective is to address the design and development of computational models and novel algorithms to resolve practical and emerging business or socially impactful problems (in our case, wearable sensor-based fall detection). For example, Lin et al. [41] have successfully designed a novel Bayesian Multi-Task Learning (BMTL) algorithm to predict adverse events for diabetes patients. In addition, Zhu et al. [84] have designed a deep learning model to recognize activities of daily living (ADL) for senior citizens. Other examples in IS include Liu et al. [43] and Zhang and Ram [83]. However, designing efective computational IT artifacts for stakeholders requires a comprehensive knowledge of the problem domain. As such, we next review the area of sensor-based fall detection.

## Sensor-based Fall Detection: Sensors and Models

Fall detection has long been an active research field in related disciplines including computer science and bioengineering. Various types of sensors have been deployed to collect data, which is further processed by algorithms to detect falls. We summarize major fall detection studies in Table 1, based on the sensor type and analytical model.

As shown in Table 1, the sensors used to capture and detect falls can be grouped into the following two categories: ambient and wearable. Ambient sensors are placed in users’ living environment, such as cameras [23], thermal sensors, wireless access points, and Doppler radars. Wearable sensors, such as accelerometers and gyroscopes, are attached to the users waist, thigh, ankle, and other body parts, or embedded in almost all smartphones (e.g., iPhone 4 and above; Samsung Galaxy S series) and smart watches. They collect the users motion data. Between the two, wearable sensors are preferred due to their easy set-ups, less intrusion of user privacy, and low cost [53]. Numerous fitness and game apps in the Apple App Store and Google Play Store utilize accelerometers and gyroscopes, such as Nike Run Club and Asphalt series.

Wearable sensor data has two unique aspects compared to common data mining applications. First, data collected from these sensors are often high-velocity, e.g., 200 data points per second. Second, each data point is a tri-axial acceleration vector, which contains very little information in terms of the user’s motor status. These two aspects necessitate feature extraction on sensor data to distill information from series of data points. A good example of such features is the maximum acceleration magnitude, which is one of the most frequently used features to identify the impact phase of a fall [15]. With manual feature extraction, researchers design either threshold-based systems (e.g., if the maximum acceleration magnitude is greater than $4 0 ~ \mathrm { m } / \mathrm { s } ^ { 2 }$ , trigger a fall alert) or machine learning models (e.g., ANN, KNN, SVM) for the final task of fall detection.

Table 1. Selected Sensor-based Fall Detection Research

<table><tr><td>Year</td><td>Author</td><td>Sensor Type</td><td>Model</td></tr><tr><td>2021</td><td>Alarifi &amp; Alwadain [2]</td><td>Wearable</td><td>CNN</td></tr><tr><td>2021</td><td>Waheed et al. [72]</td><td>Wearable</td><td>LSTM</td></tr><tr><td>2019</td><td>Saadeh et al. [55]</td><td>Wearable</td><td>Threshold</td></tr><tr><td>2019</td><td>Santos et al. [57]</td><td>Wearable</td><td>CNN</td></tr><tr><td>2019</td><td>Chelli &amp; Patzold [20]</td><td>Wearable</td><td>ANN, KNN, SVM, EBT</td></tr><tr><td>2019</td><td>Lu et al. [44]</td><td>Ambient</td><td>CNN-LSTM</td></tr><tr><td>2018</td><td>Khojasteh et al. [36]</td><td>Wearable</td><td>ANN, SVM, Tree</td></tr><tr><td>2018</td><td>Montanini et al. [48]</td><td>Wearable</td><td>Threshold</td></tr><tr><td>2018</td><td>Putra et al. [51]</td><td>Wearable</td><td>Tree, KNN, LR, SVM</td></tr><tr><td>2018</td><td>Mauldin et al. [46]</td><td>Wearable</td><td>NB, SVM, GRU</td></tr><tr><td>2018</td><td>Zhang &amp; Zhu [82]</td><td>Wearable</td><td>CNN</td></tr><tr><td>2017</td><td>Tsinganos &amp; Skodras [67]</td><td>Wearable</td><td>ANN, SVM, KNN</td></tr><tr><td>2017</td><td>Wang et al. [73]</td><td>Ambient</td><td>SVM</td></tr><tr><td>2017</td><td>Jokanovic &amp; Amin [33]</td><td>Ambient</td><td>Sparse autoencoder</td></tr></table>

Notes: ANN = Artificial Neural Network; CNN = Convolutional Neural Network; EBT = Ensemble Bagged Tree; GRU = Gated Recurrent Unit; KNN = K-Nearest Neighbors; LDA = Linear discriminant analysis; LSTM = Long Short-Term Memory; LR = Logistic Regression; NB = Naïve Bayes; PPCA = Probabilistic Principal Component Analysis; RBF = Radial Basis Function; RF = Random Forest

However, fall detection systems based on manual feature extraction face the following two challenges. First, manual feature extraction is ad hoc, labor-intensive, and often inconclusive [31]. Researchers spend considerable time in proposing and selecting feature sets, while diferent researchers tend to propose diferent feature sets, limiting their generalizability. Second, many manually engineered features are insuficient in distinguishing falls from non-fall activities. For instance, a fall detection system with “if maximum acceleration magnitude is greater than $4 0 ~ \mathrm { m } / \mathrm { s } ^ { 2 }$ then trigger a fall alert” is likely to generate false alarms when intensive activities such as jumping occur. To resolve the above issues, deep learning-based fall detection systems have been emerging in recent literature [57] [46]. We will next review deep learning and one of its most significant branches, Convolutional Neural Networks (CNNs), as well as the recent emerging attention mechanism.

## Deep Learning: Convolutional Neural Networks and Attention Mechanism

With the rapid advancement of its methodology, deep learning has become one of the most prominent branch of machine learning with considerable successful applications [38]. In the machine learning community, the term “deep learning” is mostly used as a synonym of “deep neural networks,” where the adjective “deep” highlights that the neural networks are not “shallow.” In other words, any neural networks with multiple layers can be referred to as “deep learning.” Due to the stacked layers of non-linear transformation functions and errorcorrecting backpropagation operations, deep learning models can automatically learn salient features (representations) from complex data, especially raw sensory data [38]. This is known as representation learning. With this characteristic, deep learning avoids the need of manual feature extraction and provides a generalizable solution for representing sensory data. As the base form of deep learning, Multilayer Perceptron (MLP) has been studied for decades [26]. Recently, CNNs have been one of the most prevalent and successful implementations of deep learning.

CNNs are inspired by the mammalian visual cortex. The visual cortex contains a complex arrangement of cells, which are sensitive to small sub-regions of the visual field, called a receptive field. Such cells act as local filters over the input space and are well-suited to exploit the strong spatially local correlation present in images [26]. Similar to the mammalian visual cortex, a CNN is a neural network having a specialized connectivity structure with multiple layers stacked as feature extractors. There are three distinct types of stages in a CNN layer: convolution stage, non-linear stage (activation function), and pooling stage [26]. A convolution stage consists of a set of convolution filters. Each filter performs linear transformations on the input and is stimulated when observing some specific local pattern at some spatial position in the input (e.g., vertical edges in an image). A non-linear stage introduces nonlinearity into the convolution stage with an activation function. The rectified linear unit (ReLU) is one of the most popular activation functions [38]. A pooling layer progressively reduces the spatial size of the representation to reduce the number of parameters in the network, and hence also controls overfitting. With multiple sets of convolution, non-linear, and pooling stages, CNNs excel in representing data with a gridlike topology [26]. Such grid-like topology can be one-dimensional (e.g., time series data, audio data, etc.), two-dimensional (e.g., greyscale image data), or even three-dimensional (e.g., video data). Wearable sensor data possesses a grid-like topology, and thus is suitable for CNN-based representation learning. Scholars have successfully applied CNNs on wearable sensor-based fall detection tasks [57].

Nevertheless, there has been a critique that deep learning is a “black box” approach. For chronic disease management tasks like fall detection, people are increasingly asking for not only an accurate detection of falls, but also why the model makes such a decision. Recently, the attention mechanism was proposed as a significant step towards explainable deep learning. The attention mechanism was first introduced as an approach to machine translation [7]. Such a mechanism can be intuitively explained using human biological systems. For instance, people tend to focus selectively on parts of an image while ignoring irrelevant information, which can assist in perception [77]. The attention mechanism is implemented by allocating attention weights among input data parts. A larger attention weight is assigned if the corresponding part of data is more relevant to the model output. For example, in machine translation, attention weights reflect the alignment of words in source and target languages [7]. In image caption generation, attention weights reflect the relative importance of image areas for each image caption word [77]. In this way, the attention mechanism significantly improves the explainability and transparency of deep learning models, which is critical for applications that influence human lives [19]. To cope with more complex tasks such as document classification and translation, scholars also proposed the hierarchical attention mechanism [79] [47]. Essentially, the hierarchical attention mechanism is an extension of the attention mechanism that stacks multiple attention layers at diferent data granularities. For example, both word attention and sentence attention are used for document classification [79] and translation [47].

The attention mechanism has been applied on CNN [39] [40] [14], RNN [42] [77] [75, 76], CNN-RNN [12] [60] [30], among other deep learning architectures. In fall detection, attention-based deep learning models have been proposed for vision-based systems [24] [44]. Such models aim to identify people who are falling or have fallen in videos captured by cameras. However, to the best of our knowledge, no prior study has attempted integrating the attention mechanism into a wearable sensor-based deep learning model for explainable fall detection. The diferent natures in data (video data vs. wearable sensor data) require a new model to be proposed and examined. In addition, it is unknown how the hierarchical attention mechanism can improve our understanding in fall detection.

## Research Gaps and Questions

As discussed above, two key research gaps have been identified. First, most prior studies on wearable sensor-based fall detection extracted ad hoc features from signals and applied threshold-based or machine learning-based algorithms to detect falls. While valuable, manual feature engineering is ad hoc, labor-intensive, and could lead to inconclusive results. Second, although there have been attempts on deep learningbased fall detection that avoids manual feature engineering, no prior study has integrated the hierarchical attention mechanism into a deep learning model for an explainable fall detection model. We designed our study to ask the following research questions:

(1) How can we integrate the attention mechanism into a deep learning model to advance the state-of-the-art of sensor-based fall detection?

(2) How can the hierarchical attention mechanism improve the explainability of the proposed deep learning model and guide future set-ups of fall detection systems?

## Research Design

In this work, we propose a novel Hierarchical Attention-based Convolutional Neural Networks (HACNN) model for wearable sensor-based fall detection. Our research design consists of three major components: (1) data collection and preprocessing, (2) the proposed HACNN model, and (3) model evaluations with baseline models, ablation analysis, and case studies. Each is discussed below.

## Data Collection and Preprocessing

Two large publicly available datasets, MobiFall [69] and UMAFall [17]. Both are prevailingly used as ground-truth datasets for wearable sensor-based fall detection research [18] [45]. MobiFall utilizes three types of sensors in a smartphone: a tri-axial accelerometer, a triaxial gyroscope, and a tri-axial orientation sensor, all set at subjects’ thigh position. It contains 288 fall instances that cover forward, backward, and lateral falls, and 297 non-fall instances (standing, walking, jogging, etc.) collected in lab experiments. Each instance was sampled at 200 Hz and lasted for 10 seconds. UMAFall utilizes only one type of standalone sensors: tri-axial accelerometers. Four accelerometers are set at subjects’ ankle, chest, waist, and wrist positions, respectively. It contains 208 fall instances that cover forward, backward, and lateral falls, and 538 non-fall instances. Each instance was sampled at 200 Hz and lasted for 15 seconds. No additional preprocessing steps (filtering, denoising, etc.) were performed on either dataset.

## The Proposed Hierarchical Attention-based Convolutional Neural Networks (HACNN) Model

Figure 1 illustrates our proposed HACNN model. The model consists of three major components: CNN, Hierarchical Attention Mechanism, and Output. The model is adaptative to any number of sensors, and we assume there are n sensors. We detail each component as follows.

## CNN

In Component 1, a CNN is constructed as a sliding feature extractor on the input tri-axial sensor data at timestamp . The CNN has three sets of stages; each set comprises of three stages: convolution, non-linear, and pooling.

Convolution Stage

![](/api/attachments/NYV8D64F/fulltext/images/87c0986604856681de9998d29baa4b66c70a113fc4303c1b702ec6be7ee7f376.jpg)  
Figure 1. HACNN Model

A convolution stage convolves the data input or the previous stage’s output with a set of filters. The operation in convolution stages is represented by the following formula:

$$
c _ {p, t} ^ {i, j} = b ^ {i, j} + \sum_ {m} \sum_ {q = 0} ^ {Q _ {i} - 1} w _ {q} ^ {i, j, m} x _ {p + q, t} ^ {i - 1, m}
$$

where $c _ { p , t } ^ { i , j }$ is the output value at position p for feature map j in layer i at timestamp $t , b ^ { i , j }$ is the bias for feature map in layer i, m is the number of feature maps in the previous layer (layer i   1), $Q _ { i }$ is the width of the convolution filter in layer, is the output from the previous layer (layer) for feature map m at position ${ p + q }$ at timestamp t, and is the kernel weight for position q pointing from feature map m in layer i   1 to feature map j in layer, which is invariant to the value p and is to be learned through the training process.

## Non-linear Stage

The non-linear stage is to introduce non-linearity to the deep learning model for enhanced model capacity. A rectified linear unit (ReLU) maps the output of the convolution stage () to generate the non-linearity of the model by the following function:

The ReLU function is the most widely used non-linear function for CNNs due to its simplicity and efectiveness [38].

## Pooling Stage

In the pooling stage, the resolution of feature maps generated by the convolution and� � non-linear stages $\left( \mathrm { R e L U } \left( c _ { p , t } ^ { i , j } \right) \right)$ is reduced to keep salient features and increase local scale invariance. The pooling stage is represented by the following function:

$$
d _ {p, t} ^ {i, j} = \max _ {0 \leq s \leq S _ {i} - 1} \operatorname{ReLU} \left(c _ {p + s, t} ^ {i, j}\right)
$$

where $d _ { p } ^ { i , j }$ is the output value at position $\boldsymbol { p }$ for feature map j in stage $i , S _ { i }$ is the width of the pooling filter in stage .

After four sets of convolution, non-linear, and pooling stages, the output of the CNN is flattened as a vector, which is given by:

$$
z _ {t} = \text { Flatten } \left(\left[ d _ {p, t} ^ {\text { last }, j}, j, p \right]\right)
$$

## Hierarchical Attention Mechanism

We develop the Hierarchical Attention Mechanism to capture the relative importance of each axis within each sensor (axis-level attention weights) and that of each sensor position or sensor type (sensor-level attention weights).

We denote the hidden feature vector outputted by CNN for sensor s, axis as $h _ { s , t }$ . Its axislevel attention weight, $a _ { s , t } ^ { 1 } { : }$ , is computed as:

$$
u _ {s, t} ^ {1} = \tanh \left(W _ {a} ^ {1} h _ {s, t} + b _ {a} ^ {1}\right), a _ {s, t} ^ {1} = \frac {\exp \left(\left(u _ {s , t} ^ {1}\right) ^ {T} v ^ {1}\right)}{\sum_ {j} \exp \left(\left(u _ {s , j} ^ {1}\right) ^ {T} v ^ {1}\right)}
$$

where $W _ { a } ^ { 1 } , b _ { a } ^ { 1 } , \nu ^ { 1 }$ are parameter matrices (or vectors) to be trained. After $a _ { s , t } ^ { 1 }$ has been computed for all $h _ { s , t }$ , we summarize the hidden feature vector for sensor $s , R _ { s } ^ { 1 }$ , as follows:

$$
R _ {s} ^ {1} = \sum_ {t \in \{\mathrm{x}, \mathrm{y}, \mathrm{z} \}} a _ {s, t} ^ {1} h _ {s, t}.
$$

Next, we compute the sensor-level attention weight for sensor $s ,$ denoted as $a _ { s } ^ { 2 }$ , by:

$$
u _ {s} ^ {2} = \tanh \left(W _ {a} ^ {2} R _ {s} ^ {1} + b _ {a} ^ {2}\right), a _ {s} ^ {2} = \frac {\exp \left(\left(u _ {s} ^ {2}\right) ^ {T} v ^ {2}\right)}{\sum_ {s} \exp \left(\left(u _ {s} ^ {2}\right) ^ {T} v ^ {2}\right)}
$$

where $W _ { a } ^ { 2 } , b _ { a } ^ { 2 } , \nu ^ { 2 }$ are parameter matrices (or vectors) to be trained. After $a _ { s } ^ { 2 }$ has been computed for all $R _ { s } ^ { 1 }$ , we summarize the hidden feature vector across all sensors, $R ^ { a }$ , as follows:

$$
R ^ {a} = \sum_ {s} a _ {s} ^ {2} R _ {s} ^ {1}.
$$

## Output

Finally, $R ^ { a }$ is fed into two fully connected neural network layers and then a softmax layer to identify whether the input data is a fall instance $( y = 1 )$ or not $( \boldsymbol { y } = \boldsymbol { 0 } )$ :

$$
d _ {i} = \operatorname{ReLU} \left(W _ {d, 1} R ^ {a} + b _ {d, 1}\right), y = \operatorname{softmax} \left(W _ {d, 2} \operatorname{Drop} \left(d _ {i}\right) + b _ {d, 2}\right)
$$

where $W _ { d , 1 } , b _ { d , 1 } , W _ { d , 2 } , b _ { d , 2 }$ are parameter matrices (or vectors) to be trained. Note that a dropout layer (Drop) is inserted between the two fully connected layers as a common regularization technique to control overfitting. The detailed structure of the HACNN can be found in Appendix C.

## Evaluation

We compared the performance of our HACNN model with state-of-the-art baseline models for fall detection. We set up three sets of baselines.

Classic Machine Learning Algorithms. We compared our model with classic machine learning algorithms based on either raw sensor data or combined features extracted from sensor data that are most prevalent in the literature (e.g., [50]) (a full list of features can be found in Appendix D). The algorithms included support vector machines (SVM), logistic regression (LR), naïve Bayes (NB), k-nearest neighbors (KNN), decision tree (DT), random forest (RF), and AdaBoost (AB).

Alternative Deep Learning Models. We compared our model with existing state-of-theart deep learning baselines, including multilayer perceptron (MLP), convolutional neural networks (CNN), long short-term memory (LSTM), convolutional neural networks with long short-term memory (CNN-LSTM), and hierarchical attention-based long short-term memory (HALSTM). For the MLP baseline, either raw sensor data $o r$ combined features extracted from sensor data are used as the input. As CNN requires grid-like data while LSTM requires temporal data, only raw sensor data is used as the input for the remaining baselines (the extracted features are neither grid-like nor temporal).

Ablation Analysis. We provided ablation analysis on varying a series of hyperparameters and design choices of our HACNN, including the number of CNN layer sets, CNN slide window width, and model learning rate. In addition, we test how the dataset size could afect model performance by assuming we only had a random 25, 50, or 75 percent of our available datasets. Finally, we inject Gaussian noise into both datasets and test the robustness of our HACNN. The Gaussian noise follows a Gaussian distribution with mean 0 and variance equal to 1 percent of the data variance.

For each set of baselines, ten-fold cross-validation is applied as a common approach in evaluating machine learning models. By treating each run of the ten-fold cross-validation as a sample, we conduct two-sample statistical tests to identify whether our HACNN significantly outperformed the classic machine learning and alternative deep learning models. We list the mean, standard deviation (in parentheses), and significant levels (t-tests in asterisks and tests of proportions in plus signs) in the cells of the baseline models. For the ablation analysis, we do not list the significant levels as the point of ablation analysis is not to demonstrate one choice is “significantly better” than another. Nevertheless, we list the means and standard deviations for each model as a reference.

For simplicity, we compare the performance of HACNN and other baseline models based on $\mathrm { F } _ { 1 } \cdot$ measure (F-measure), which is the harmonic mean of precision and recall. The F-measure provides an overall evaluation of the system’s ability to identify falls while reducing false alarms. The formulas for the above metrics are as follows:

$$
\text { Precision } = \frac {T P}{T P + F P}, \text { Recall } = \frac {T P}{T P + F N}, F _ {1} - \text { measure } = \frac {2 \cdot \text { Precision } \cdot \text { Recall }}{\text { Precision } + \text { Recall }},
$$

where TP is the true positive (recognized as a fall and is a fall), FP is the false positive (recognized as a fall but is not), and FN is the false negative (not recognized as a fall but is actually a fall). For precision and recall, both t-tests and tests of proportions are conducted as robustness checks. For F-measure, only t-tests are conducted because F-measure is derived from precision and recall and is technically not a proportion, thus tests of proportions are not applicable.

In addition, we conduct a case study that reports the statistics of axis-level and sensorlevel attentions in the dataset as well as those attentions grouped by fall types. The aggregated attention statistics demonstrate populational patterns that could contribute to further understanding of falls, such as how placement and types of sensors can afect fall detection.

## Experimental Results

## Classic Machine Learning Algorithms

We compared our proposed HACNN with seven classic machine learning algorithms, SVM, LR, NB, KNN, DT, RF, and AB, with either manually extracted features or raw data as the input (Table 2). Our model significantly outperformed all benchmark models in F-measure in both datasets. On the one hand, the results indicated that classic machine learning algorithms were not designed to directly leverage raw wearable sensor data to detect falls. On the other hand, this suggested that manual feature engineering may overlook hidden features in sensor data, while our deep learning-based model is able to extract such hidden features. With a proper design, the neural network is able to learn the efective representation of the data and provide improved fall detection results.

In classic machine learning algorithms, RF and AB are among the best-performing models with manually extracted features due to them being ensemble (bagging or boosting) models. In circumstances where computing power is limited and deep learning models cannot be properly deployed, RF and AB can be considered as workable alternatives.

## Alternative Deep Learning Models

We compared our proposed HACNN with alternative deep learning models, including MLP, CNN, LSTM, CNN-LSTM, and HALSTM (Table 3). Due to the reasons elaborated in Section 3.3: Evaluation, only MLP used either manually extracted features or raw data as the input; the others solely used raw data. The results showed that HACNN significantly outperformed all benchmarks models in F-measure in both datasets. Overall, MLP is the worst-performing model as it is not designed to model grid-like data. CNN-based models (CNN, CNN-LSTM, HACNN) tend to perform better, which implies the importance of representation learning in dealing with sensor data.

We conducted a series of ablation analysis to investigate how the changes of hyperparameters and design choices of the deep learning architecture may influence model performance (Table 4). The results in boldface are the best ones in the same hyperparameter group. We compared our model with alternative hyperparameters in the number of CNN layer sets, CNN slide window width, and model learning rate. Overall, the number of CNN layers (2, 3, or 4) or its slide window length (8, 16, 32, or 48) do not seem to have a significant impact on model performance. For the learning rate, a choice of ${ { 1 0 } ^ { - 3 } }$ outperforms that of $1 0 ^ { - 2 } \mathrm { o r } 1 0 ^ { - 4 } ,$ In addition, we performed a dataset size evaluation where only 25, 50, or 75 percent of the original dataset instances are randomly selected. From the results, we can see that the dataset size does have an impact on deep learning model performance. In MobiFall, the F-measure increased from 0.6601 to 0.9808 with the dataset size increasing from 25 percent to the full. Finally, we observe that the Gaussian noise added to the datasets seems to have a minimal efect on model performance (MobiFall: F-measure from 0.9808 to 0.9750; UMAFall: F-measure from 0.9739 to 0.9688). This further supports the generalizability of HACNN.

Table 2. Experiment Results for Classic Machine Learning Algorithms

<table><tr><td rowspan="2">Input</td><td rowspan="2">Model</td><td colspan="3">MobiFall</td><td colspan="3">UMAFall</td></tr><tr><td>Precision</td><td>Recall</td><td>F-measure</td><td>Precision</td><td>Recall</td><td>F-measure</td></tr><tr><td rowspan="7">Manually extracted features</td><td>SVM</td><td>0.9608*(0.0259)</td><td>0.9577*(0.0191)</td><td>0.9591**(0.0199)</td><td>0.9078***(0.0282)+++</td><td>0.8604**(0.0487)+++</td><td>0.8826***(0.0296)</td></tr><tr><td>LR</td><td>0.9694*(0.0131)+</td><td>0.9473*(0.0311)</td><td>0.9578***(0.0146)</td><td>0.9175***(0.0247)+++</td><td>0.7849***(0.0321)+++</td><td>0.8456***(0.0228)</td></tr><tr><td>NB</td><td>0.9076***(0.0359)+++</td><td>0.9820(0.0245)</td><td>0.9426***(0.0169)</td><td>0.5652***(0.0609)+++</td><td>0.9057**(0.0225)+</td><td>0.6944***(0.0480)</td></tr><tr><td>KNN</td><td>0.9415***(0.0281)+</td><td>0.9519*(0.0240)+</td><td>0.9464***(0.0208)</td><td>0.8257***(0.0507)+++</td><td>0.7146***(0.0472)+</td><td>0.7648***(0.0371)</td></tr><tr><td>DT</td><td>0.9480**(0.0308)+</td><td>0.9727(0.0166)</td><td>0.9597**(0.0146)</td><td>0.7956***(0.0472)+++</td><td>0.9626(0.0202)</td><td>0.8704**(0.0313)</td></tr><tr><td>RF</td><td>0.9740(0.0195)</td><td>0.9638(0.0197)</td><td>0.9687*(0.0127)</td><td>0.9753(0.0203)</td><td>0.8679***(0.0428)+</td><td>0.9180**(0.0292)</td></tr><tr><td>AB</td><td>0.9631*(0.0273)</td><td>0.9691(0.0126)</td><td>0.9660*(0.0186)</td><td>0.9700(0.0239)+</td><td>0.8742***(0.0352)+</td><td>0.9192***(0.0234)</td></tr><tr><td rowspan="8">Raw data</td><td>SVM</td><td>0.9582**(0.0247)</td><td>0.3681***(0.0230)+</td><td>0.5311***(0.0216)</td><td>0.9491**(0.0249)+</td><td>0.7045***(0.0370)+</td><td>0.8082***(0.0285)</td></tr><tr><td>LR</td><td>0.3021***(0.0304)+</td><td>0.2077***(0.0241)+</td><td>0.2446***(0.0183)</td><td>0.6358***(0.0492)+</td><td>0.5631***(0.0393)+</td><td>0.5964***(0.0379)</td></tr><tr><td>NB</td><td>0.3327***(0.0290)+</td><td>0.8165***(0.0322)+</td><td>0.4721***(0.0315)</td><td>0.7592***(0.0227)+</td><td>0.9428(0.0201)</td><td>0.8408***(0.0174)</td></tr><tr><td>KNN</td><td>0.9349***(0.0243)+</td><td>0.7045***(0.0222)+</td><td>0.8034***(0.0212)</td><td>0.8889**(0.0615)+</td><td>0.9293*(0.0434)</td><td>0.9061***(0.0237)</td></tr><tr><td>DT</td><td>0.6995***(0.0277)+</td><td>0.6752***(0.0271)+</td><td>0.6868***(0.0233)</td><td>0.7659***(0.0386)+</td><td>0.9551*(0.0174)</td><td>0.8497***(0.0279)</td></tr><tr><td>RF</td><td>0.9392***(0.0314)+</td><td>0.6073***(0.0361)+</td><td>0.7368***(0.0288)</td><td>0.9788(0.0166)</td><td>0.8709***(0.0306)+</td><td>0.9214***(0.0194)</td></tr><tr><td>AB</td><td>0.6778***(0.0273)+</td><td>0.6550***(0.0172)+</td><td>0.6660***(0.0194)</td><td>0.9327***(0.0259)+</td><td>0.8423***(0.0497)+</td><td>0.8846***(0.0346)</td></tr><tr><td>HACNN</td><td>0.9859(0.0118)</td><td>0.9758(0.0084)</td><td>0.9808(0.0074)</td><td>0.9827(0.0088)</td><td>0.9654(0.0128)</td><td>0.9739(0.0075)</td></tr></table>

Notes: For t-test: \*: p-value < 0.05; \*\*: p-value < 0.01; \*\*\*: p-value < 0.001. For test of proportions: <sup>+</sup>: p-value $< 0 . 0 5 ; { ^ { + + } } ;$ p-value $< 0 . 0 1 ; { ^ { + + + } } ;$ p-value < 0.001. They indicate the significance level of HACNN outperforming the corresponding benchmark. Results with alternative hyperparameters can be found in Appendix E.

Table 3. Experiment Results for Alternative Deep Learning Models

<table><tr><td rowspan="2">Input</td><td rowspan="2">Model</td><td colspan="3">MobiFall</td><td colspan="3">UMAFall</td></tr><tr><td>Precision</td><td>Recall</td><td>F-measure</td><td>Precision</td><td>Recall</td><td>F-measure</td></tr><tr><td>Manually extracted features</td><td>MLP</td><td>0.9703 (0.0221)</td><td>0.9564(0.0319)</td><td>0.9629*(0.0177)</td><td>0.9360**(0.0369)+++</td><td>0.8861**(0.0342)++</td><td>0.9096***(0.0237)</td></tr><tr><td rowspan="6">Raw data</td><td>MLP</td><td>0.8642***(0.0245)+++</td><td>0.8472***(0.0251)+++</td><td>0.8551***(0.0125)</td><td>0.9635*(0.0161)+</td><td>0.8835***(0.0083)++</td><td>0.9216***(0.0098)</td></tr><tr><td>CNN</td><td>0.9753(0.0176)</td><td>0.9688(0.0207)</td><td>0.9709*(0.0153)</td><td>0.9715**(0.0107)</td><td>0.9078*(0.0427)+</td><td>0.9354*(0.0175)</td></tr><tr><td>LSTM</td><td>0.9708(0.0193)</td><td>0.9747(0.0231)</td><td>0.9724*(0.0115)</td><td>0.8938***(0.0342)+++</td><td>0.8396***(0.0215)+++</td><td>0.8653***(0.0182)</td></tr><tr><td>CNN-LSTM</td><td>0.9732(0.0166)</td><td>0.9671(0.0178)</td><td>0.9700*(0.0130)</td><td>0.9571*(0.0279)+++</td><td>0.9315(0.0270)++</td><td>0.9436*(0.0157)</td></tr><tr><td>HALSTM</td><td>0.9680(0.0173)</td><td>0.9744(0.0320)</td><td>0.9711*(0.0084)</td><td>0.9427*(0.0376)+++</td><td>0.9500(0.0258)</td><td>0.9451*(0.0135)</td></tr><tr><td>HACNN</td><td>0.9859(0.0118)</td><td>0.9758(0.0084)</td><td>0.9808(0.0074)</td><td>0.9827(0.0088)</td><td>0.9654(0.0128)</td><td>0.9739(0.0075)</td></tr></table>

Notes: For t-test: \*: p-value < 0.05; \*\*: p-value < 0.01; \*\*\*: p-value < 0.001. For test of proportions: <sup>+</sup>: p-value < 0.05; <sup>++</sup>: p-value < 0.01; <sup>+++</sup>: p-value < 0.001. They indicate the significance level of HACNN outperforming the corresponding benchmark. Results with alternative hyperparameters can be found in Appendix F.

## Case Study: Attention Weight Statistics

In this section, we report attention weights that reflect the relative importance of diferent sensors and their axes for both datasets. We report the overall results in Figure 2 as well as those further grouped by the type of falls (forward, backward, or lateral) in Figures 3 and 4. The I-shaped marks indicate 95% confidence intervals.

Figure 2 helps us examine how diferent sensor types (accelerometer, gyroscope, orientation sensor) and sensor positions (ankle, chest, waist, wrist), as well as their sensor axes contribute to fall detection. From MobiFall, we notice that accelerometers and gyroscopes contribute almost equally to fall detection, while orientation sensors do not contribute much. This makes sense as accelerometers and gyroscopes reflect subjects’ translational and rotational motions, respectively, which are more relevant for falls. Within each sensor, the three axes of accelerometers and gyroscopes contribute almost equally, while the x-axis of orientation sensors account for more than half of attention weights. From UMAFall, we notice that accelerometers set to the four positions basically contribute equally to fall detection. However, within each sensor, the x- and z-axes contribute more compared to the y-axis, especially for chest and waist positions.

Figures 3 and 4 show a detailed decomposition of attention weights based on diferent fall types. In MobiFall, fall types do not have a significant efect on sensor-level or axis-level attention weights with respect to sensor types. In UMAFall, x-axis seems to contribute more for forward and backward falls across all sensor positions, while y-axis seems to contribute more for lateral falls. One possible reason is that the y-axis points to the mediolateral axis of the human body, which is more closely related to lateral falls. Domain experts may find the results interesting, which could shed light on future sensor set-ups of fall detection systems.

Table 4. Experiment Results for Ablation Analysis

<table><tr><td rowspan="2">Hyper-parameter</td><td rowspan="2">Options</td><td colspan="3">MobiFall</td><td colspan="3">UMAFall</td></tr><tr><td>Precision</td><td>Recall</td><td>F-measure</td><td>Precision</td><td>Recall</td><td>F-measure</td></tr><tr><td rowspan="3">Number of CNN layers</td><td>2-layer</td><td>0.9761(0.0112)</td><td>0.9688(0.0130)</td><td>0.9723(0.0089)</td><td>0.9806(0.0115)</td><td>0.9533(0.0108)</td><td>0.9667(0.0086)</td></tr><tr><td>3-layer</td><td>0.9747(0.0104)</td><td>0.9836(0.0102)</td><td>0.9791(0.0080)</td><td>0.9827(0.0088)</td><td>0.9654(0.0128)</td><td>0.9739(0.0075)</td></tr><tr><td>4-layer</td><td>0.9859(0.0118)</td><td>0.9758(0.0084)</td><td>0.9808(0.0074)</td><td>0.9838(0.0129)</td><td>0.9623(0.0169)</td><td>0.9728(0.0111)</td></tr><tr><td rowspan="4">CNN slide window width</td><td>8</td><td>0.9747(0.0104)</td><td>0.9836(0.0102)</td><td>0.9791(0.0080)</td><td>0.9842(0.0112)</td><td>0.9556(0.0128)</td><td>0.9696(0.0096)</td></tr><tr><td>16</td><td>0.9859(0.0118)</td><td>0.9758(0.0084)</td><td>0.9808(0.0074)</td><td>0.9792(0.0112)</td><td>0.9640(0.0156)</td><td>0.9714(0.0068)</td></tr><tr><td>32</td><td>0.9726(0.0110)</td><td>0.9765(0.0111)</td><td>0.9745(0.0082)</td><td>0.9827(0.0088)</td><td>0.9654(0.0128)</td><td>0.9739(0.0075)</td></tr><tr><td>48</td><td>0.9752(0.0105)</td><td>0.9709(0.0197)</td><td>0.9729(0.0113)</td><td>0.9761(0.0148)</td><td>0.9589(0.0178)</td><td>0.9673(0.0105)</td></tr><tr><td rowspan="3">Learning rate</td><td> $10^{-2}$ </td><td>0.9764(0.0101)</td><td>0.9820(0.0077)</td><td>0.9792(0.0073)</td><td>0.9753(0.0117)</td><td>0.9562(0.0160)</td><td>0.9656(0.0109)</td></tr><tr><td> $10^{-3}$ </td><td>0.9859(0.0118)</td><td>0.9758(0.0084)</td><td>0.9808(0.0074)</td><td>0.9827(0.0088)</td><td>0.9654(0.0128)</td><td>0.9739(0.0075)</td></tr><tr><td> $10^{-4}$ </td><td>0.9797(0.0108)</td><td>0.9771(0.0154)</td><td>0.9783(0.0076)</td><td>0.9726(0.0133)</td><td>0.9519(0.0123)</td><td>0.9621(0.0091)</td></tr><tr><td rowspan="4">Dataset size</td><td>25%</td><td>0.6894(0.0180)</td><td>0.6337(0.0163)</td><td>0.6601(0.0117)</td><td>0.8654(0.0638)</td><td>0.8339(0.0420)</td><td>0.8458(0.0387)</td></tr><tr><td>50%</td><td>0.7922(0.0194)</td><td>0.8335(0.0102)</td><td>0.8122(0.0120)</td><td>0.9098(0.0505)</td><td>0.8954(0.0372)</td><td>0.9020(0.0229)</td></tr><tr><td>75%</td><td>0.9407(0.0108)</td><td>0.9669(0.0160)</td><td>0.9536(0.0120)</td><td>0.9405(0.0198)</td><td>0.9510(0.0265)</td><td>0.9447(0.0115)</td></tr><tr><td>100%</td><td>0.9859(0.0118)</td><td>0.9758(0.0084)</td><td>0.9808(0.0074)</td><td>0.9827(0.0088)</td><td>0.9654(0.0128)</td><td>0.9739(0.0075)</td></tr><tr><td>Gaussian noise</td><td>1%</td><td>0.9814(0.0104)</td><td>0.9702(0.0149)</td><td>0.9750(0.0093)</td><td>0.9770(0.0146)</td><td>0.9559(0.0168)</td><td>0.9688(0.0136)</td></tr></table>

## Contributions to the is Knowledge Base

Our study makes multiple unique contributions to the IS discipline. We summarize the contributions of our work as an IT artifact as well as diverse design guidelines for future research.

## IT Artifact for Health Management

Chronic disease management is a topic receiving increasing interest in the IS community (e.g., [43]; [83]). Our study advances chronic disease management research by proposing the HACNN, a deep learning model that enables explainable fall detection based on wearable sensor data. The intersection of chronic disease management and wearable sensor technology is an exciting but underexplored research area, both inside and outside the IS community. Methodologically, we contribute to deep learning by combining the hierarchical attention mechanism with CNN to form the HACNN for fall detection, which difers from and outperforms existing CNN architectures. Our model serves as an IT artifact for advanced clinical decision support, which can assist healthcare providers and senior citizens in detecting falls for more prompt and personalized care.

![](/api/attachments/NYV8D64F/fulltext/images/7a49e58beb9efe40e3166fe8d88dad0a776bde2e7a4ebb1f2211826c75ae0007.jpg)

![](/api/attachments/NYV8D64F/fulltext/images/302e87786b89dc5d910343ada57c432bd95763aaf2731e1d0b6b2de94ec7336d.jpg)

MobiFall Attention Weights. Left: Sensor-Level; Right: Axis-Level Notes: acc = accelerometer; gyro = gyroscope; ori = orientation sensor  
![](/api/attachments/NYV8D64F/fulltext/images/7a8270e34370ebf181f6db20c3f784d5eb67643aa7a8fcf5ae294bcc65d42744.jpg)  
UMAFall Attention Weights. Left: Sensor-Level; Right: Axis-Level Notes: ank = ankle  
Figure 2. Overall Attention Weight Statistics

## Generalizable Design Principles

Design science contributes to the IS knowledge base not only in the form of IT artifact, but also as a search process [28]. Based on our extensive experiments, comparisons, and ablation analysis, we discuss our generalizable design principles for future research from the following two perspectives: data and application characteristics, and model building suggestions.

Data and application characteristics. Sensor data is generated in an inherently highvelocity manner. For example, a sensor with a regular sampling rate of 50 Hz can lead to 4 million records per day. This characteristic prevents classic statistical machine learning methods from being directly applied on the raw sensor data due to the excessive variable dimensionality (a one-minute snippet of wearable sensor data can contain 3,000 ( ¼ 50 persecond � 60 seconds) independent variables). Deep learning serves as an efective tool of representation learning without human intervention [26]. Meanwhile, to improve model explainability, the attention mechanism is receiving increasing attention in the deep learning community. Consequently, our proposed HACNN is specifically designed to improve fall detection accuracy while providing another layer of explainability. Benefiting from its feature engineering-less design, no disease-specific domain knowledge has been explicitly encoded in the HACNN. This enables the model to generalize and transfer to other adverse event detection tasks, e.g., stroke, seizure, etc., which are promising directions for future research.

![](/api/attachments/NYV8D64F/fulltext/images/431824cd7c607c3ab16a26317c1158065f029d8df389ff3617d4976debc9b531.jpg)

![](/api/attachments/NYV8D64F/fulltext/images/83bd112a187f703c797593a79dace89686fb418ad82fae2d6b88b88b0e9fb190.jpg)  
MobiFall Attention Weights for Each Fall Type. Top: Sensor-Level; Bottom: Axis-Level Notes: acc = accelerometer; gyro = gyroscope; ori = orientation sensor  
Figure 3. MobiFall Attention Weight Statistics for Each Fall Type

Model building suggestions. Deep learning models including HACNN introduce flexibility in choosing the network architecture and hyperparameters. We conducted extensive ablation analysis to identify the optimal model designs and hyperparameters in our context. Results showed that the number of CNN layer sets and the CNN slide window width do not have significant impacts on model performance, while the model learning rate does play a role. In addition, deep learning models tend to obtain better performance with larger datasets. We hope our above exploration can guide more rapid and efective model building in future research.

![](/api/attachments/NYV8D64F/fulltext/images/51ef66567e01ae145c0cc0bd4192c7bc2cc9fd05fd30724f9f0957bff71fb2bc.jpg)

![](/api/attachments/NYV8D64F/fulltext/images/48d097bedefcbf0db4f93b6429a118a8125766a79df75239d495434cd83727e5.jpg)  
UMAFall Attention Weights for Each Fall Type. Top: Sensor-Level; Bottom: Axis-Level Notes: ank = ankle  
Figure 4. UMAFall Attention Weight Statistics for Each Fall Type

## Practical and Managerial Implications

Healthcare is inherently becoming mobile and ubiquitous. With the advancement of sensing technologies, people are able to collect and record their motion and physiological data on a daily basis. This creates a unique opportunity for people, especially senior citizens, to track themselves more precisely and promptly. Hospitals and retirement facilities can benefit from the model to track inpatients’ and senior citizens’ activities more accurately and timely. We discuss key practical and managerial implications for those stakeholders in the following subsections.

Senior citizens and families. The HACNN model enables the possibility of home monitoring systems that allow senior citizens and their families to detect falls without the need of human caregivers. This is especially important for those who are patients with certain chronic conditions, e.g., Parkinson’s disease, because the systems can provide fall monitoring. This can potentially guide senior citizens and their families to take steps to alleviate the consequences of falls.

Hospitals and retirement facilities. Hospital inpatient falls are common and may lead to injuries and prolonged hospitalization [59]. Senior citizens living in retirement facilities performed worse on tests of agility and balance compared to senior citizens living in the community [35], which leads to greater risks of falling. Fall management is a critical issue for hospital and retirement facility managers. By employing wearable sensors equipped with state-of-the-art fall detection algorithms such as HACNN, hospitals and retirement facilities can more accurately identify patients and senior citizens who fell, and provide assistance as soon as possible.

In addition, it is critical to promote senior citizens’ adoption and efective use of the proposed IT artifacts (wearable sensors and HACNN) to maximize the eficacy. Mobile apps with educational programs can be utilized to remind senior citizens to wear the sensors.

We next discuss how we can deploy the proposed HACNN model into a real-world setting. As HACNN is trained with 10-second or 15-second samples, it is suggested to run the model every 10 or 15 seconds to detect potential falls. The model execution time is not a critical factor, as it only takes less than a second (see Appendix G). Sensor position should not be a significant factor; the user can choose among ankle, chest, waist, wrist, or thigh positions, as those positions are used in MobiFall and UMAFall. Compared with other nondeep-learning state-of-the-art models, the advantages of HACNN are improved number of falls correctly detected and reduced false alarms. Although HACNN may require additional computational power as a deep learning model, this can be solved by deploying HACNN on cloud servers or smartphones that are equipped with neural engines (e.g., iPhones).

## Limitations and Future Research

As with any other scientific research in an emerging field, there are two important limitations in our work. First, only wearable sensor data have been used in training the deep learning model. It would be interesting to further explore how other types of data can be integrated into the framework (e.g., physiological data, medical imaging data, etc.), as the existing CNN architecture may not be directly applicable in such situations. Second, the approach has been verified on only two fall datasets. Although cross-validation has been conducted to demonstrate the efectiveness and utility of our model, it is still possible that the performance of HACNN is limited to the datasets. Researchers are encouraged to experiment with the HACNN on other real-world fall datasets. Third, this work trained HACNN on a static dataset without updating its parameters after training. However, in realworld scenarios, it may be preferable to continuously learn the user’s specific patterns and update model parameters. This area of online learning is a promising future direction. Despite the above limitations, this study pioneers the application of explainable deep learning on wearable sensor data for fall detection.

## Conclusions

Mobile technologies have been leading a new round of innovation and reformation in the IS community [21]. Mobile sensing technologies provide us an always-on option to obtain health data from individuals via smartphones and wearable sensors. With the vast amount of data that we are potentially able to collect, however, prior studies on wearable sensor-based fall detection focused on manual feature engineering, which is laborious, ad hoc, and inconclusive.

Although there have been attempts in leveraging deep learning models to process wearable sensor data, such approaches remain “black boxes” and lack explainability. To address the above concerns, we proposed a novel Hierarchical Attention-based Convolutional Neural Networks (HACNN) model for improved wearable sensor-based fall detection. With the design of CNN, Hierarchical Attention Mechanism, and Output components, the HACNN is able to recognize falls from wearable sensor data in an explainable manner and guide future set-ups of fall detection systems. To demonstrate the efectiveness of our proposed HACNN, we collected two large publicly available datasets, MobiFall and UMAFall, as our fall detection testbed. Our experimental results showed that the HACNN consistently outperformed the competitive benchmark models in terms of F-measure. The case studies illustrated the potential advantage of applying the hierarchical attention mechanism on deep learning models to explain the detection results and how diferent sensor placement and types contribute to fall detection. We contribute to the IS knowledge base by enabling explainable fall detection for chronic disease management and proposing generalizable design science principles in model building. We believe that this principled approach can further increase the accuracy of fall detection and create a better living environment and quality of life for senior citizens.

## Acknowledgements

This study was supported by USA NSF SES-1314631, DUE-1303362, IIP-1622788. Yidong Chai was supported by Excellent Fund of Hefei University of Technology (JZ2021HGPA0060) and Major Program of the National Natural Science Foundation of China (91846201).

## Disclosure statement

No potential conflict of interest was reported by the author(s).

## Notes on contributors

Shuo Yu (Shuo.Yu@ttu.edu) is an Assistant Professor at Rawls College of Business, Texas Tech University. He received his Ph.D. in Management Information Systems from the University of Arizona. Dr. Yu’s research focuses on data mining, text mining, deep learning, and health analytics. His work has been published or accepted in such journals as IEEE Journal of Biomedical and Health Informatics, IEEE Intelligent Systems, and ACM Transactions on Management Information Systems, among others.

Yidong Chai (chaiyd@hfut.edu.cn; corresponding author) is a Professor at School of Management, Hefei University of Technology, China. He received his Ph.D. in Management Science and Engineering from Tsinghua University. Dr. Chai’s research focuses on machine learning and its application in healthcare, cybersecurity, and e-business, among others. His work has been published or accepted in such journals as MIS Quarterly, Information Processing and Management, Knowledge Based Systems, and Applied Soft Computing, among others.

Hsinchun Chen (hchen@eller.arizona.edu) is Regents Professor and Thomas R. Brown Chair in Management and Technology at the Eller College of Management, University of Arizona. He received his Ph.D. in Information Systems from New York University. He is author or editor of 20 books, 300 journal papers, and 200 refereed conference articles covering digital library, data/text/web mining, business analytics, security informatics, and health informatics. He served as the lead Program Director of the Smart and Connected (SCH) Program at the National Science Foundation (NSF). Dr. Chen founded the Artificial Intelligence Lab at University of Arizona, which has received \$50M+ research funding from the NSF, National Institutes of Health, National Library of Medicine, Department of Defense, Department of Justice, Central Intelligence Agency, Department of Homeland Security, and other agencies. He is a Fellow of ACM, IEEE, and AAAS.

Randall A. Brown, MD, MBA (randall.brown247@gmail.com) is a physician board-certified in Internal Medicine who has over 30 years of clinical experience providing patient care in academic medical centers in the United States. He has retired from clinical practice and is as a medical advisor with Optum Insight as well as president of his independent consulting firm, Hermes Medical Intelligence. Dr. Brown collaborated with the University of Arizona Artificial Intelligence Lab from 2010 to 2019 as a medical domain expert advising on healthcare related projects that included data mining and predictive analytics utilizing electronic health records as well as the machine learning processing of healthcare related wireless mobile sensor data.

Scott J. Sherman, MD, PhD (ssherman@neurology.arizona.edu) is Director of the Movement Disorders Clinic at the University of Arizona with 30 years of experience treating patients with Parkinson Disease (PD). He splits his time 50/50 between patient care and research in the field of Movement Disorders including both pharma-sponsored studies and investigator-initiated research. Dr. Sherman is an expert in the clinical evaluation of patient with PD and also in the use of standardized rating scales to quantify clinical phenotypes and disease staging.

Jay F. Nunamaker Jr. (jnunamaker@cmi.arizona.edu) is Regents and Soldwedel Professor of MIS, Computer Science and Communication, Director of the Center for the Management of Information and Director (Emeritus) of the National Center for Border Security and Immigration at the University of Arizona. He received his Ph.D. in Operations Research and Systems Engineering from Case Institute of Technology. He founded the MIS Department at the University of Arizona and served as department head for 18 years. His specialization is in the fields of system analysis and design, collaboration technology, and deception detection. The commercial product GroupSystems ThinkTank, based on his research, is often referred to as the gold standard for structured collaboration systems. Dr. Nunamaker was inducted into the Design Science Hall of Fame and received the LEO Award for Lifetime Achievement from the Association for Information Systems. He was featured in the July 1997 issue of Forbes Magazine on technology as one of eight key innovators in information technology. Dr. Nunamaker has held a professional engineer’s license since 1965.

## References

1. Adipat, B., Zhang, D., and Zhou, L. The Efects of Tree-View Based Presentation Adaptation on Mobile Web Browsing. MIS Quarterly, 35, 1 (2011), 99–121.

2. Alarifi, A. and Alwadain, A. Killer heuristic optimized convolution neural network-based fall detection with wearable IoT sensor devices. Measurement, 167, 108258 (2021), 1–10.

3. Anderson, C.L. and Agarwal, R. The Digitization of Healthcare: Boundary Risks, Emotion, and Consumer Willingness to Disclose Personal Health Information. Information Systems Research, 22, 3 (2011), 469–490.

4. Angst, C.M., Block, E.S., D’Arcy, J., and Kelley, K. When Do IT Security Investments Matter? Accounting for the Influence of Institutional Factors in the Context of Healthcare Data Breaches. MIS Quarterly, 41, 3 (2017), 893–916.

5. Arias, E., Tejada-Vera, B., and Ahmad, F. Provisional life expectancy estimates for January through June, 2020. NVSS Vital Statistics Rapid Release, 10 (2021), 1–8.

6. Ayabakan, S., Bardhan, I., Zheng, Z., and Kirksey, K. The Impact of Health Information Sharing on Duplicate Testing. MIS Quarterly, 41, 4 (2017), 1083–1103.

7. Bahdanau, D., Cho, K., and Bengio, Y. Neural machine translation by jointly learning to align and translate. arXiv preprint arXiv:1409.0473, (2014).

8. Baird, A., Angst, C., and Oborn, E. MISQ Research Curation on Health Information Technology. MIS Quarterly, (2018), 1–14.

9. Baird, A., Davidson, E., and Mathiassen, L. Reflective technology assimilation: facilitating electronic health record assimilation in small physician practices. Journal of Management Information Systems, 34, 3 (2017), 664–694.

10. Bardhan, I., Chen, H., and Karahanna, E. Connecting systems, data, and people: A multidisciplinary research roadmap for chronic disease management. MIS Quarterly, 44, 1 (2020), 185–200.

11. Bardhan, I., Oh, J., Zheng, Z. (Eric), and Kirksey, K. Predictive Analytics for Readmission of Patients with Congestive Heart Failure. Information Systems Research, 26, 1 (2015), 19–39.

12. Basiri, M.E., Nemati, S., Abdar, M., Cambria, E., and Acharya, U.R. ABCDM: An attention-based bidirectional CNN-RNN deep model for sentiment analysis. Future Generation Computer Systems, 115, (2021), 279–294.

13. Bergen, G., Stevens, M.R., and Burns, E.R. Falls and Fall Injuries Among Adults Aged ≥65 Years — United States, 2014. Morbidity and Mortality Weekly Report (MMWR), 65, 37 (2016).

14. Bin, L., Quan, L., Jin, X., Qian, Z., and Peng, Z. Aspect-based sentiment analysis based on multi-attention CNN. Journal of Computer Research and Development, 54, 8 (2017), 1724.

15. Bourke, A.K., Klenk, J., Schwickert, L., et al. Fall detection algorithms for real - world falls harvested from lumbar sensors in the elderly population : A machine learning approach. In 2016 IEEE 38th Annual International Conference of the Engineering in Medicine and Biology Society (EMBC). 2016, pp. 3712–3715.

16. Burns, E.R., Stevens, J.A., and Lee, R. The Direct Costs of Fatal and Non-fatal Falls among Older Adults — United States. Journal of Safety Research, 58, (2016), 99–103.

17. Casilari, E., Santoyo-Ramón, J.A., and Cano-García, J.M. UMAFall: A Multisensor Dataset for the Research on Automatic Fall Detection. Procedia Computer Science, 110, (2017), 32–39.

18. Casilari, E., Santoyo-Ramón, J.A., and Cano-García, J.M. Analysis of public datasets for wearable fall detection systems. Sensors (Switzerland), 17, 7 (2017).

19. Chaudhari, S., Polatkan, G., Ramanath, R., and Mithal, V. An attentive survey of attention models. arXiv preprint arXiv:1904.02874, (2019).

20. Chelli, A. and Patzold, M. A Machine Learning Approach for Fall Detection and Daily Living Activity Recognition. IEEE Access, 7, (2019), 38670–38687.

21. Chen, H., Chiang, R.H., and Storey, V.C. Business Intelligence and Analytics: From Big Data to Big Impact. MIS Quarterly, 36, 4 (2012), 1165–1188.

22. Chen, L., Baird, A., and Straub, D. Fostering Participant Health Knowledge and Attitudes: An Econometric Study of a Chronic Disease-Focused Online Health Community. Journal of Management Information Systems, 36, 1 (2019), 194–229.

23. De Miguel, K., Brunete, A., Hernando, M., and Gambao, E. Home camera-based fall detection system for the elderly. Sensors (Switzerland), 17, 12 (2017).

24. Feng, Q., Gao, C., Wang, L., Zhao, Y., Song, T., and Li, Q. Spatio-temporal fall event detection in complex scenes using attention guided LSTM. Pattern Recognition Letters, 130, (2020), 242–249.

25. Ghose, A., Goldfarb, A., and Han, S.P. How Is the Mobile Internet Diferent? Search Costs and Local Activities. Information Systems Research, 24, 3 (2013), 613–631.

26. Goodfellow, I., Bengio, Y., and Courville, A. Deep Learning. MIT Press, 2016.

27. Guo, S., Guo, X., Fang, Y., and Vogel, D. How doctors gain social and economic returns in online health-care communities: a professional capital perspective. Journal of Management Information Systems, 34, 2 (2017), 487–519.

28. Hevner, A.R., March, S.T., Park, J., and Ram, S. Design Science in Information Systems Research. MIS Quarterly, 28, 1 (2004), 75–105.

29. Hoehle, H. and Venkatesh, V. Mobile Application Usability: Conceptualization and Instrument Development. MIS Quarterly, 39, 2 (2015), 435–472.

30. Hu, Y., Wong, Y., Wei, W., Du, Y., Kankanhalli, M., and Geng, W. A novel attention-based hybrid CNN-RNN architecture for sEMG-based gesture recognition. PloS one, 13, 10 (2018), e0206049.

31. Hubble, R.P., Naughton, G.A., Silburn, P.A., and Cole, M.H. Wearable Sensor Use for Assessing Standing Balance and Walking Stability in People with Parkinson’s Disease: A Systematic Review. PloS One, 10, 4 (2015), e0123705.

32. Ivanov, A. and Sharman, R. Impact of User-Generated Internet Content on Hospital Reputational Dynamics. Journal of Management Information Systems, 35, 4 (2018), 1277–1300.

33. Jokanovic, B. and Amin, M. Fall Detection Using Deep Learning in Range-Doppler Radars. IEEE Transactions on Aerospace and Electronic Systems, 54, 1 (2018), 180–189.

34. Jung, J., Bapna, R., Ramaprasad, J., and Umyarov, A. Love unshackled: Identifying the efect of mobile app adoption in online dating. MIS Quarterly, 43, (2019), 47–72.

35. Kang, K.-H., White, K.N., Hayes, W.C., and Snow, C.M. Agility and balance difer between older community and retirement facility residents. Journal of Applied Gerontology, 23, 4 (2004), 457–468.

36. Khojasteh, S.B., Villar, J.R., Chira, C., González, V.M., and de la Cal, E. Improving fall detection using an on-wrist wearable accelerometer. Sensors (Switzerland), 18, 5 (2018), 1–28.

37. Kwon, H.E., So, H., Han, S.P., and Oh, W. Excessive Dependence on Mobile Social Apps: A Rational Addiction Perspective. Information Systems Research, 27, 4 (2016), 919–939.

38. LeCun, Y., Bengio, Y., and Hinton, G. Deep Learning. Nature, 521, 7553 (2015), 436–444.

39. Li, L., Xu, M., Wang, X., Jiang, L., and Liu, H. Attention based glaucoma detection: A large-scale database and CNN model. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2019, pp. 10571–10580.

40. Li, Y., Zeng, J., Shan, S., and Chen, X. Occlusion aware facial expression recognition using CNN with attention mechanism. IEEE Transactions on Image Processing, 28, 5 (2018), 2439–2450.

41. Lin, Y.-K., Chen, H., and Brown, R.A. Healthcare Predictive Analytics for Risk Profiling in Chronic Care: A Bayesian Multitask Learning Approach. MIS Quarterly, 41, 2 (2017), 473–495.

42. Liu, J., Wang, G., Hu, P., Duan, L.-Y., and Kot, A.C. Global context-aware attention LSTM networks for 3D action recognition. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2017, pp. 1647–1656.

43. Liu, X., Zhang, B., Susarla, A., and Padman, R. Go to YouTube and Call Me in the Morning: Use of Social Media for Chronic Conditions. MIS Quarterly, 44, 1 (2020), 257–283.

44. Lu, N., Wu, Y., Feng, L., and Song, J. Deep learning for fall detection: Three-dimensional CNN combined with LSTM on video kinematic data. IEEE Journal of Biomedical and Health Informatics, 23, 1 (2018), 314–323.

45. Martínez-Villaseñor, L., Ponce, H., Brieva, J., Moya-Albor, E., Núñez-Martínez, J., and Peñafort-Asturiano, C. Up-fall detection dataset: A multimodal approach. Sensors (Switzerland), 19, 9 (2019).

46. Mauldin, T.R., Canby, M.E., Metsis, V., Ngu, A.H.H., and Rivera, C.C. Smartfall: A smartwatch-based fall detection system using deep learning. Sensors (Switzerland), 18, 10 (2018), 1–19.

47. Miculicich, L., Ram, D., Pappas, N., and Henderson, J. Document-Level Neural Machine Translation with Hierarchical Attention Networks. In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing. 2018, pp. 2947–2954.

48. Montanini, L., Del Campo, A., Perla, D., Spinsante, S., and Gambi, E. A Footwear-Based Methodology for Fall Detection. IEEE Sensors Journal, 18, 3 (2018), 1233–1242.

49. Mousavi, R., Raghu, T.S., and Frey, K. Harnessing Artificial Intelligence to Improve the Quality of Answers in Online Question-answering Health Forums. Journal of Management Information Systems, 37, 4 (2020), 1073–1098.

50. Pannurat, N., Thiemjarus, S., and Nantajeewarawat, E. Automatic fall monitoring: A review. Sensors (Switzerland), 14, 7 (2014), 12900–12936.

51. Putra, I.P.E.S., Brusey, J., Gaura, E., and Vesilo, R. An event-triggered machine learning approach for accelerometer-based fall detection. Sensors (Switzerland), 18, 1 (2018), 1–18.

52. Rai, A. Editor’s Comments: Diversity of Design Science Research. MIS Quarterly, 41, 1 (2017), iii–xviii.

53. Ren, L. and Peng, Y. Research of fall detection and fall prevention technologies: A systematic review. IEEE Access, 7, (2019), 77702–77722.

54. Rubenstein, L.Z. and Josephson, K.R. The epidemiology of falls and syncope. Clinics in geriatric medicine, 18, 2 (2002), 141–158.

55. Saadeh, W., Butt, S.A., and Altaf, M.A. Bin. A Patient-specific single sensor iot-based wearable fall prediction and detection system. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 27, 5 (2019), 995–1003.

56. Saifee, D.H., Bardhan, I.R., Lahiri, A., and Zheng, Z. Adherence to Clinical Guidelines, Electronic Health Record Use, and Online Reviews. Journal of Management Information Systems, 36, 4 (2019), 1071–1104.

57. Santos, G.L., Endo, P.T., Monteiro, K.H. de C., Rocha, E. da S., Silva, I., and Lynn, T. Accelerometer-based human fall detection using convolutional neural networks. Sensors, 19, 7 (2019), 1644.

58. Schefer, A.C., Schuurmans, M.J., Van Dijk, N., Van Der Hooft, T., and De Rooij, S.E. Fear of falling: measurement strategy, prevalence, risk factors and consequences among older persons. Age and ageing, 37, 1 (2008), 19–24.

59. Schwendimann, R., Bühler, H., De Geest, S., and Milisen, K. Characteristics of hospital inpatient falls across clinical departments. Gerontology, 54, 6 (2008), 342–348.

60. Si, C., Chen, W., Wang, W., Wang, L., and Tan, T. An attention enhanced graph convolutional lstm network for skeleton-based action recognition. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2019, pp. 1227–1236.

61. Sibley, K.M., Voth, J., Munce, S.E., Straus, S.E., and Jaglal, S.B. Chronic disease and falls in community-dwelling Canadians over 65 years old: a population-based study exploring associations with number and pattern of chronic conditions. BMC geriatrics, 14, 1 (2014), 1–11.

62. Soh, F. and Grover, V. Efect of Release Timing of App Innovations based on Mobile Platform Innovations. Journal of Management Information Systems, 37, 4 (2020), 957–987.

63. Steinbart, P.J., Keith, M.J., and Babb, J. Examining the continuance of secure behavior: A longitudinal field study of mobile device authentication. Information Systems Research, 27, 2 (2016), 219–239.

64. Steinhauser, S., Doblinger, C., and Hüsig, S. The Relative Role of Digital Complementary Assets and Regulation in Discontinuous Telemedicine Innovation in European Hospitals. Journal of Management Information Systems, 37, 4 (2020), 1155–1183.

65. Sun, Z., Dawande, M., Janakiraman, G., and Mookerjee, V. Not Just a Fad: Optimal Sequencing in Mobile In-App Advertising. Information Systems Research, 28, 3 (2017), 511–528.

66. Tinetti, M.E., Liu, W.-L., and Claus, E.B. Predictors and Prognosis of to Get Up After Falls Among Elderly Persons. Journal of the American Medical Association, 269, 1 (1993), 65–70.

67. Tsinganos, P. and Skodras, A. A smartphone-based fall detection system for the elderly. International Symposium on Image and Signal Processing and Analysis, ISPA, Ispa (2017), 53–58.

68. U.S. Census Bureau. American Community Survey: Age and Sex. 2020. https://data.census. gov/cedsci/table?q=PEPAGE&t=AgeandSex&tid=ACSST1Y2019.S0101&hidePreview=false .

69. Vavoulas, G., Pediaditis, M., Chatzaki, C., Spanakis, E.G., and Tsiknakis, M. The mobifall dataset: Fall detection and classification with a smartphone. International Journal of Monitoring and Surveillance Technologies Research (IJMSTR), 2, 1 (2014), 44–56.

70. Venkatesh, V., Aloysius, J.A., Hoehle, H., and Burton, S. Design and Evaluation of Auto-ID Enabled Shopping Assistance Artifacts in Customers’ Mobile Phones: Two Retail Store Laboratory Experiments. MIS Quarterly, 41, 1 (2017), 83–113.

71. Venkatesh, V., Zhang, X., and Sykes, T. a. “Doctors Do Too Little Technology”: A Longitudinal Field Study of an Electronic Healthcare System Implementation. Information Systems Research, 22, 3 (2011), 523–546.

72. Waheed, M., Afzal, H., and Mehmood, K. NT-FDS—A Noise Tolerant Fall Detection System Using Deep Learning on Wearable Devices. Sensors, 21, 6 (2021), 2006.

73. Wang, H., Zhang, D., Wang, Y., Ma, J., Wang, Y., and Li, S. RT-Fall: A Real-Time and Contactless Fall Detection System with Commodity WiFi Devices. IEEE Transactions on Mobile Computing, 16, 2 (2017), 511–526.

74. Xie, J., Zhang, Z., Liu, X., and Zeng, D.D. Unveiling the Hidden Truth of Drug Addiction: A Social Media Approach Using Similarity Network-Based Deep Learning. Journal of Management Information Systems, 38, 1 (2021), 166–195.

75. Xie, Y., Liang, R., Liang, Z., Huang, C., Zou, C., and Schuller, B. Speech emotion classification using attention-based LSTM. IEEE/ACM Transactions on Audio, Speech, and Language Processing, 27, 11 (2019), 1675–1685.

76. Xu, J., Yao, T., Zhang, Y., and Mei, T. Learning multimodal attention LSTM networks for video captioning. In Proceedings of the 25th ACM international conference on Multimedia. 2017, pp. 537–545.

77. Xu, K., Ba, J., Kiros, R., et al. Show, attend and tell: Neural image caption generation with visual attention. In International conference on machine learning. 2015, pp. 2048–2057.

78. Yan, L. and Tan, Y. The consensus efect in online health-care communities. Journal of Management Information Systems, 34, 1 (2017), 11–39.

79. Yang, Z., Yang, D., Dyer, C., He, X., Smola, A., and Hovy, E. Hierarchical attention networks for document classification. In Proceedings of the 2016 conference of the North American chapter of the association for computational linguistics: human language technologies. 2016, pp. 1480–1489.

80. Yaraghi, N., Du, A.Y., Sharman, R., Gopal, R.D., and Ramesh, R. Health Information Exchange as a Multisided Platform: Adoption, Usage, and Practice Involvement in Service Co-Production. Information Systems Research, 26, 1 (2014), 1–18.

81. Ye, H. (J.) and Kankanhalli, A. User Service Innovation on Mobile Phone Platforms: Investigating Impacts of Lead Userness, Toolkit Support, and Design Autonomy. MIS Quarterly, 42, 1 (2018), 165–187.

82. Zhang, Q. and Zhu, S. Real-time Activity and Fall Risk Detection for Aging Population Using Deep Learning. 2018 9th IEEE Annual Ubiquitous Computing, Electronics and Mobile Communication Conference, UEMCON 2018, (2018), 1055–1059.

83. Zhang, W. and Ram, S. A Comprehensive Analysis of Triggers and Risk Factors for Asthma Based on Machine Learning and Large Heterogeneous Data Sources. MIS Quarterly, 44, 1 (2020), 305–349.

84. Zhu, H., Samtani, S., Chen, H., and Nunamaker Jr, J.F. Human identification for activities of daily living: A deep transfer learning approach. Journal of Management Information Systems, 37, 2 (2020), 457–483.

## Appendices Appendix A: Selected IS Research on HIT

<table><tr><td>Year</td><td>Author</td><td>Topic</td><td>Focus</td></tr><tr><td>2021</td><td>Xie et al. [74]</td><td>Social Media</td><td>Using user-generated content in social media to study opioid use disorder</td></tr><tr><td>2020</td><td>Mousavi et al. [49]</td><td>Online Community</td><td>Understanding the quality of answers in health-related community-based question answering</td></tr><tr><td>2020</td><td>Steinhauser et al. [64]</td><td>Health IS</td><td>Relative role of digital complementary assets and regulation in discontinuous telemedicine innovation</td></tr><tr><td>2020</td><td>Liu et al. [43]</td><td>Social Media</td><td>Evidence-backed digital therapeutics with technology-enabled interventions</td></tr><tr><td>2020</td><td>Zhang and Ram [83]</td><td>Social Media</td><td>Identifying and understanding triggers and risk factors that cause asthma exacerbations</td></tr><tr><td>2019</td><td>Chen et al. [22]</td><td>Online Community</td><td>How the content exchanged between online community participants impacts health knowledge and attitudes</td></tr><tr><td>2019</td><td>Saifee et al. [56]</td><td>Online Review</td><td>Impact of Physician Quality Report System on physicians related to their online reputation</td></tr><tr><td>2018</td><td>Ivanov &amp; Sharman [32]</td><td>Online Review</td><td>Impact of user-generated content on hospital reputational dynamics</td></tr><tr><td>2017</td><td>Guo et al. [27]</td><td>Online Community</td><td>Examining the determinants of social and economic returns of doctors at online communities</td></tr><tr><td>2017</td><td>Baird et al. [9]</td><td>Health IS</td><td>Moving beyond initial plateaus of postadoption usage of electronic health records for small businesses</td></tr><tr><td>2017</td><td>Yan et al. [78]</td><td>Online Community</td><td>How other patients&#x27; treatment experiences affects patients&#x27; perceived treatment effectiveness</td></tr><tr><td>2017</td><td>Angst et al. [4]</td><td>IT Security</td><td>Factors impacting health security IT investments</td></tr><tr><td>2017</td><td>Ayabakan et al. [6]</td><td>Information Sharing</td><td>Impact of information sharing technologies on reducing duplicate testing</td></tr><tr><td>2017</td><td>Lin et al. [41]</td><td>Predictive Analytics</td><td>Predicting adverse event risks for diabetes patients</td></tr><tr><td>2015</td><td>Bardhan et al. [11]</td><td>Predictive Analytics</td><td>Predicting hospital readmission of patients with congestive heart failure</td></tr><tr><td>2014</td><td>Yaraghi et al. [80]</td><td>Health IS</td><td>How a health information exchange platform can be adopted and used by practitioners</td></tr><tr><td>2011</td><td>Anderson &amp; Agarwal [3]</td><td>Information Digitization</td><td>Circumstances under which individuals are willing to disclose and digitize identified personal health information</td></tr><tr><td>2011</td><td>Venkatesh et al. [71]</td><td>Health IS</td><td>Factors driving the use of e-healthcare systems</td></tr></table>

Appendix B: Selected IS Research on Mobile Technology

<table><tr><td>Year</td><td>Author</td><td>Topic</td><td>Focus</td></tr><tr><td>2020</td><td>Soh &amp; Grover [62]</td><td>Mobile App</td><td>How app developers can time the app innovations release to increase app financial performance</td></tr><tr><td>2020</td><td>Zhu et al. [84]</td><td>Wearable Sensor</td><td>Activity of daily living recognition for human identification</td></tr><tr><td>2019</td><td>Jung et al. [34]</td><td>Mobile App</td><td>Effect of mobile app adoption in online dating</td></tr><tr><td>2018</td><td>Ye &amp; Kankanhalli [81]</td><td>User Innovation</td><td>How mobile phone platforms and user innovators impact users&#x27; service innovation outcomes</td></tr><tr><td>2017</td><td>Venkatesh et al. [70]</td><td>Internet of Things</td><td>How the auto-ID technologies (barcode and RFID) affects technology adoption and shopping outcomes</td></tr><tr><td>2017</td><td>Sun et al. [65]</td><td>Mobile App</td><td>How to maximize revenue generated from mobile in-app fading ads</td></tr><tr><td>2016</td><td>Kwon et al. [37]</td><td>Mobile App</td><td>Addictive behaviors on mobile social apps at an individual level</td></tr><tr><td>2016</td><td>Steinbart et al. [63]</td><td>Security</td><td>How the user interface of authentication affects the continuance of user secure behavior</td></tr><tr><td>2015</td><td>Hoehle &amp; Venkatesh [29]</td><td>Mobile App</td><td>Developing a conceptualization of mobile application usability</td></tr><tr><td>2013</td><td>Ghose et al. [25]</td><td>Mobile Web Browsing</td><td>How Internet browsing behavior varies between mobile phones and personal computers</td></tr><tr><td>2011</td><td>Adipat et al. [1]</td><td>Mobile Web Browsing</td><td>Designing an effective approach to adapting Web page presentation on mobile devices</td></tr></table>

## Appendix C: HACNN Model Specifications

<table><tr><td>Component</td><td>Description</td><td>Details</td></tr><tr><td rowspan="12">CNN</td><td rowspan="3">Layer Set 1</td><td>Conv1d(1, 16, kernel_size=(16,), stride=(16,), padding=(16,), bias=False)</td></tr><tr><td>BatchNorm1d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)</td></tr><tr><td>MaxPool1d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)</td></tr><tr><td rowspan="3">Layer Set 2</td><td>Conv1d(16, 16, kernel_size=(3,), stride=(1,), padding=(1,), bias=False)</td></tr><tr><td>BatchNorm1d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)</td></tr><tr><td>MaxPool1d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)</td></tr><tr><td rowspan="3">Layer Set 3</td><td>Conv1d(16, 16, kernel_size=(3,), stride=(1,), padding=(1,), bias=False)</td></tr><tr><td>BatchNorm1d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)</td></tr><tr><td>MaxPool1d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)</td></tr><tr><td rowspan="3">Layer Set4</td><td>Conv1d(16, 16, kernel_size=(3,), stride=(1,), bias=False)</td></tr><tr><td>BatchNorm1d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)</td></tr><tr><td>MaxPool1d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)</td></tr><tr><td rowspan="4">Hierarchical Attention Mechanism</td><td rowspan="2">Axis-Level Attention</td><td>Linear(in_features=48, out_features=8, bias=True)</td></tr><tr><td>Linear(in_features=8, out_features=1, bias=True)</td></tr><tr><td rowspan="2">Sensor-Level Attention</td><td>Linear(in_features=48, out_features=8, bias=True)</td></tr><tr><td>Linear(in_features=8, out_features=1, bias=True)</td></tr><tr><td rowspan="2">Output</td><td>Fully Connected</td><td>Linear(in_features=48, out_features=32, bias=True)</td></tr><tr><td>Fully Connected</td><td>Linear(in_features=32, out_features=5, bias=True)</td></tr></table>

Appendix D: Feature List for Feature-based Algorithms

<table><tr><td>Feature Name</td><td>Formula</td></tr><tr><td>Max x-axis value</td><td> $\max_{i}(a_{x,i})$ </td></tr><tr><td>Max y-axis value</td><td> $\max_{i}(a_{y,i})$ </td></tr><tr><td>Max z-axis value</td><td> $\max_{i}(a_{z,i})$ </td></tr><tr><td>Max value magnitude</td><td> $\max_{i}\left(\sqrt{a_{x,i}^{2} + a_{y,i}^{2} + a_{z,i}^{2}}\right)$ </td></tr><tr><td>Min x-axis value</td><td> $\min_{i}(a_{x,i})$ </td></tr><tr><td>Min y-axis value</td><td> $\min_{i}(a_{y,i})$ </td></tr><tr><td>Min z-axis value</td><td> $\min_{i}(a_{z,i})$ </td></tr><tr><td>Min value magnitude</td><td> $\min_{i}\left(\sqrt{a_{x,i}^{2} + a_{y,i}^{2} + a_{z,i}^{2}}\right)$ </td></tr><tr><td>Standard deviation of x-axis value</td><td> $\sigma_x = \sqrt{\frac{1}{N-1}\sum_{i=1}^{N}\left(a_{x,i} - u_x\right)^2}, whereu_x = \frac{1}{N}\sum_{i=1}^{N}a_{x,i}$ </td></tr><tr><td>Standard deviation of y-axis value</td><td> $\sigma_y = \sqrt{\frac{1}{N-1}\sum_{i=1}^{N}\left(a_{y,i} - u_y\right)^2}, whereu_y = \frac{1}{N}\sum_{i=1}^{N}a_{y,i}$ </td></tr><tr><td>Standard deviation of z-axis value</td><td> $\sigma_z = \sqrt{\frac{1}{N-1}\sum_{i=1}^{N}\left(a_{z,i} - u_z\right)^2}, whereu_z = \frac{1}{N}\sum_{i=1}^{N}a_{z,i}$ </td></tr><tr><td>Mean value magnitude</td><td> $u_{|a|} = \frac{1}{N}\sum_{i=1}^{N}\left(|a|_i\right), where|a|_i = \sqrt{a_{x,i}^2 + a_{y,i}^2 + a_{z,i}^2}$ </td></tr><tr><td>Root mean square of value magnitude</td><td> $|a|_{rms} = \sqrt{\frac{1}{N}\sum_{i=1}^{N}|a|_i^2}$ </td></tr><tr><td>Standard deviation of value magnitude</td><td> $\sigma_{|a|} = \sqrt{\frac{1}{N-1}\sum_{i=1}^{N}\left(|a|_i - u_{|a|}\right)^2}$ </td></tr><tr><td>Difference of value magnitude max &amp; min</td><td> $\Delta |a|_{\text{max-min}} = \max_i(|a|_i^2) - \min_i(|a|_i^2)$ </td></tr></table>

Appendices E, F, and G are provided online.
