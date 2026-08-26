---
otero_id: 20039
otero_key: "64DEHFQK"
title: "Measuring service quality based on customer emotion: An explainable AI approach"
authors: "Yiting Guo; Yilin Li; De Liu; Sean Xin Xu"
year: "2024"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2023.114051"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Measuring service quality based on customer emotion: An explainable AI approach

![](/api/attachments/64DEHFQK/fulltext/images/639ac0292b5266830db19d9d5b390a923c88af390424afb239d5fc40c991653c.jpg)

Yiting Guo <sup>a,1</sup>, Yilin Li <sup>b,\*,2</sup>, De Liu <sup>c,3</sup>, Sean Xin Xu <sup>d,4</sup>

<sup>a</sup> School of Economics and Management, Southeast University, Nanjing, China

<sup>b</sup> Guanghua School of Management, Peking University, Beijing, China

<sup>c</sup> Carlson School of Management, University of Minnesota Twin Cities, Minneapolis, MN, USA

<sup>d</sup> Center for AI and Management (AIM), School of Economics and Management, Tsinghua University, Beijing, China

## A R T I C L E I N F O

Keywords: Service quality Emotional intelligence Explainable AI Referral Time series classification

## A B S T R A C T

This paper develops an explainable artificial intelligence (AI) approach to measuring service quality in voicebased service encounters. Drawing from the psychology and computer science literature, we construct features of a customer’s emotion dynamics during a service encounter. Using real-world call center data from a large insurance company, we train an ensemble model with these emotion dynamics features to predict service quality. The model has higher prediction performance than the two benchmark approaches using quality-assurance evaluation and operational indices. Our method for emotion dynamics classification outperforms a host of state-of-the-art time series classification algorithms. We further apply explainable AI methods to identify the most important features of emotion dynamics and show how they are related to service quality. For example, the location where the last emotion episode appears in a service call has a U-shaped relationship to low quality. Finally, to demonstrate utility, we design an IT artifact to automatically measure service quality after service encounters in the call center and use the measure to predict a customer's referral intention.

If you can’t measure, your knowledge is meager and unsatisfactory. —Lord Kelvin

## 1. Introduction

Firms must constantly track how customers perceive the service they receive—namely service quality—because service quality influences critical outcomes such as customer loyalty, word-of-mouth, firm reve nue, and long-term survivability [1]. As of 2018, U.S. businesses lose more than \$75 billion a year because of poor customer service.<sup>5</sup> A key challenge for businesses in managing service quality is measuring it accurately and effectively. This paper seeks to improve the measurement of call center service quality based on customer emotion dynamics and explainable artificial intelligence (AI) techniques.

Although service quality measures have long been an important topic in management fields including service science [2] and information systems [3], the existing approaches have notable drawbacks. Until recently, call centers primarily used three approaches to measure service quality: customer surveys, manual quality inspections, and operational indices. The first two rely on manual work and are time-consuming and unscalable. Customer surveys usually have low response rates, some customers find them intrusive [4], and there may be a gap between quality-inspection results and customers’ perception of service [5]. The third approach, using operational indices (such as call time and delay), can work automatically, but most of these indices focus on call-handling efficiency instead of the underlying service quality [6]. In practice, there is a lack of real-time, efficient systems for managing the quality of call center service. At the same time, scholars have yet to fully study the prediction model that specializes in service quality.

The rapid development of digital technologies, big data, and AI techniques provides new opportunities to improve the measurement of service quality. Given their transformative potential, AI techniques can be applied to the design of intelligent artifacts to solve business prob lems [7]. In particular, AI has advantages in mining unstructured multimedia data (images, text, speech, etc.) recorded during the service encounter, offering much richer information and possibly obtaining more profound insights. Call centers have especially accumulated massive recorded call data that contain customer speech in time series. Moreover, AI provides an unprecedented opportunity for theory devel opment [8]. Even though most AI techniques are seen as black boxes because of their lack of transparency, explainable AI could help extract knowledge and discover complex relationships between predictors and targets [9].

The present research proposes a theory-driven approach with the capacity for prediction and interpretation based on explainable AI. Specifically, this approach uses customer emotion during service en counters to measure service quality. The approach is grounded in the service science literature, which documents that customers’ emotions during service encounters correlate with how they perceive service quality [10]. We extract features (of customer emotion) using this theoretical guidance, which helps avoid overfitting [11]. On the tech nical side, applications for tracking people’s emotions are increasingly available. These two pillars—theoretical and technical—motivate us to leverage customer emotions to develop a measure of service quality.

Furthermore, we explore emotion dynamics—the dynamics of customer emotions throughout a service encounter—which refers to “changes and fluctuations in people’s emotional and affective states over multiple points in time” [12]. Connecting those changes and fluctua tions in customer emotions with the outcome of customer service offers a rich context for identifying new relationships between customer emotion and service quality, which, to the best of our knowledge, are under-researched. From the technological perspective, there remain some challenges in analyzing customer emotion series. The existing time series classification (TSC) methods have not been applied to emotion sequences and are limited because they are not interpretable and usually focus on merely identifying shapes or measuring global distances be tween time series. Therefore, this paper proposes a framework for analyzing customer emotion dynamics including feature extraction, prediction, and explanation.

We work with a large insurance company, which provides us with data from three sources:

• a sample of recorded service calls (i.e., service encounters)

• ground truth: results of customer surveys for assessing service quality • benchmarks: results of other approaches to service evaluation, including (a) quality-inspection-team assessments and (b) opera tional indices

This paper trains an ensemble model that uses six sub-categories of customer-emotion dynamic features to predict service quality. We further use explainable AI methods (i.e., permutation feature impor tance and accumulated local effects) to obtain the contribution of each emotion dynamics feature and to uncover its relationship to service quality. Finally, we design a real-time system based on automatic speech emotion recognition and assess the value of service-quality prediction in inferring customers’ referring intentions.

Our study makes four contributions:

(1) Measurement. This study develops a new method to measure service quality in call centers. Based on customer emotion, this method is superior to two benchmarks (based on quality inspection evaluation and operational indices) for assessing ser vice quality. It offers many benefits, including reduced costs, reduced latency in handling service problems, and scalability.

(2) Insights. Our explainable AI approach unveils what dynamic characteristics of consumer emotions influence service quality, and how.

(3) Technical. When executing (1) and (2), we propose a TSC framework that uses customer emotion dynamics to predict ser vice quality. It outperforms the state-of-the-art TSC methods in our research setting.

(4) Practice. This study substantiates the utility of the new measure by (a) designing an IT artifact that can automatically track customer emotion and then measure service quality, which har nesses the potential of customer speech data for generating valuable business insights, and (b) leveraging such emotional intelligence to predict customers’ referral intention, which showcases how to integrate emotional intelligence into decision support systems.

## 2. Background

## 2.1. Approaches to assessing service quality

Call centers typically use three approaches to assess service en counters: operational indices, manual quality inspection, and customer feedback.

Common operational indices include the average speed to answer, abandonment rate, average talk time, calls per agent, and longest delay. These operational indices are easily quantifiable and are automatically recorded [13], but they tend toward efficiency instead of the quality of services [6]. Studies have repeatedly shown that superior operational indices do not necessarily translate to superior customer experiences [14].

Call centers also routinely employ specialists who assess service quality by listening to recorded service calls, and evaluating service employees’ call-handling processes, protocol compliance, call-handling skills, and etiquette against the center’s service quality standards [6]. Earlier studies identified service employees’ performance as a signifi cant factor affecting service quality [15,16]. However, quality in spections tend to emphasize standardized service processes, which may not correspond to a customer’s specific needs. Moreover, quality in spections are costly and labor-intensive. Consequently, call centers typically inspect only a small fraction (e.g., 2%) of all recorded service calls.

Call centers also often follow up with customers and obtain their feedback on service quality through phone or mail surveys. The most widely used questionnaire is the service quality (SERVQUAL) scale developed by [17]. Customer feedback is seen as the ultimate way to capture service quality [17]. However, gathering customer feedback is time-consuming and resource-intensive [13]. Such surveys also suffer from low response rates and may disturb customers. The approach described in this paper differs from the conventional approaches by automatically predicting service quality using widely available call audio data.

## 2.2. Emotion dynamics and service quality

Our design of artifacts is guided by theories about the relationship between customer emotion and service quality, which conforms to the design science paradigm [18]. Both theoretical and empirical studies suggest that during service-encounter contexts, especially for highcontact services, emotion is a crucial determinant of the perception and evaluation of the service experience [19–21]. If customers have a positive emotional reaction to focal service performance, their subse quent assessment of service and satisfaction is likely to be positive [20]. Therefore, their emotions provide clues about how they assess service quality.

Research has mostly studied emotions as a single-state consequence of a service encounter, paying too little attention to their dynamics [22].

Yet studies show that customers’ experiences and perceptions evolve during service encounters and may affect the final perceived service quality [15]. Therefore, the present research treats customer emotion as a process instead of a single state.

Prior psychological studies have examined the relationship between people’s emotion patterns and several psychological outcomes, such as depression [23], well-being [12], emotion regulation [24], and the re sults of psychotherapy [25]. This paper adds to this literature by relating emotion dynamics to perceived service quality.

Emotion dynamics can be categorized into two general groups: trajectory-based and episode-based [26]. Emotion trajectories are the recorded sequences of emotions over a given period, presenting the continuous, ongoing levels of emotions [26], which reflect the global change patterns of emotion trajectories over that period. An emotion episode presents a sub-sequence range from the beginning to the end of an emotion, usually equal to one or more utterances expressing emotion, revealing the characteristics of specific emotion episodes, such as an emotion’s duration. The most commonly applied emotion features, such as variability, instability, and inertia, are all trajectory-based; for example, [12,23]. One notable omission in prior literature is time-specific fea tures. For example, emotions at the end of an encounter may have different implications from emotions at the beginning of the encounter. The present research builds on existing emotional dynamic features and enriches the set to include time-specific features, such as the locations of negative emotions.

## 2.3. Time series classification (TSC) methods

The problem of predicting low-service-quality calls from a cus tomer’s emotion sequence is a special case of TSC. TSC models can be classified into three main categories: distance-based, feature-based, and model-based. Distance-based methods first measure the similarity be tween a whole series using elastic distances (such as dynamic time warping, DTW) and then apply k-nearest-neighbor (KNN) models to perform the classification. DTW-KNN is the model most frequently used in this category [27]. Feature-based methods map the original series to a feature space. Frequently used features in TSC tasks include statistics of time series intervals (e.g., means, standard deviations, and slopes) and series decomposition in the frequency or time domain. Representative feature-based methods include a time series forest (TSF) [28], Shapelets [29], and a bag of SFA symbols (BOSS) [30]. Model-based methods typically use generative models (e.g., hidden Markov models and autoregressive models). In addition, deep learning models have gained interest in recent years. However, perhaps because deep learning models are highly complex, studies have not found them to be superior to other methods [31]. Finally, some studies combine two or more of these ap proaches to achieve better classification performance, such as the elastic ensemble (EE) model [27] and HIVE-COTE [32].

We developed our own TSC framework for three main reasons. First, many TSC methods (e.g., most distance- and model-based methods) do not meet our goal of explainable AI. Second, the most widely used TSC dataset, the UCR Time Series Classification Archive [33], does not cover an emotion time series that is comparable with our emotion dataset, making the existing algorithms’ performance not directly analogous to our emotion TSC task. Third, many methods focus on identifying shapes, or measuring global distances between time series, and they disregard the timing and frequency of patterns, which make them unlikely to apply to our setting.

## 3. Methodology

## 3.1. Research context and data

Our data come from a top 10 insurance company in China. Each day, the company’s call centers receive over 10,000 service calls. The com pany routinely samples 2% of all service calls in order to follow up with a customer survey. The company’s representatives call the chosen cus tomers several days after the service and ask them to rate the service. Because of the company’s requirements for customer privacy protection and data security, we randomly selected 1200 historical calls related to property insurance (between July and August 2016) with follow-up surveys as our dataset. After inspection, 57 calls were removed from the dataset either because they reflected dialogue between two em ployees or because they were marred by severe background noise.

## 3.2. Labeling

This paper labeled service quality, the target variable, using the customer survey data. The company uses a modified instrument with a rating scale of 1 to 5 (very poor to very good). SERVQUAL includes five service-quality dimensions: tangibles, reliability, responsiveness, assurance, and empathy. We mapped the company’s survey questions into four di mensions of SERVQUAL but not tangibles (Table 1)—because the latter does not apply to call centers [34].

According to the company, its service objective is a 5 in each dimension. Therefore, we dichotomized customer ratings by labeling a rating of 5 as high and others as low. We labeled a call as high-quality (1) if all four dimensions were rated high, and low-quality (0), otherwise. We obtained 704 high-quality calls and 439 low-quality ones.

To obtain customers’ emotion dynamics, this paper first manually coded customer emotions in each call. Specifically, the labelers were

## Table 1

Service quality: dimensions and survey questions.

<table><tr><td>Dimension</td><td>Definition</td><td>Survey question</td><td>Comparable items in the literature</td></tr><tr><td>Reliability</td><td>Ability to perform the promised service dependably and accurately.</td><td>Has the question you consulted / the problem you encountered been addressed? *Please rate the solution offered by the service employee.</td><td>When you have a problem, XYZ shows a sincere interest in solving it [35].XYZ is dependable [36].</td></tr><tr><td>Responsiveness</td><td>Willingness to help customers and provide prompt service.</td><td>Please rate the promptness of the service provided by the service employee.Please rate the willingness of the service employee to help you.</td><td>Employees of XYZ give you prompt service [35].Employees of XYZ are always willing to help you [35].</td></tr><tr><td>Assurance</td><td>Knowledge and courtesy of employees and their ability to convey trust and confidence.</td><td>Please rate the attitude of the service employee.Please rate the tone expressed by the service employee.</td><td>Generally, the employees are courteous, polite, and respectful [37].</td></tr><tr><td>Empathy</td><td>Caring, individualized attention the company provides its customers.</td><td>Please rate the degree of the service employee&#x27;s patience in listening and talking to you.Please rate the ability of the service employee to understand your needs.</td><td>Attention and patience of the staff [38].Employees of XYZ do not know what your needs are [35].</td></tr></table>

Notes:\* For this question, an answer of “Yes” is assigned the label high; otherwise, low.

trained and experienced service employees. Every call was segmented into natural utterances (i.e., a continuous piece of speech beginning and ending with a clear pause) by machine. Then, the labelers listened to each utterance in the calls and assigned it an emotion tag. According to the annotation scheme, the labelers identify the speakers’ role, under stand the context, and recognize the customers’ emotions based on both dialogue and utterance information. The given tag is negative or nonnegative,<sup>6</sup> with the negative class encompassing several basic negative emotions (anger, anxiety, fear, and sadness) and the non-negative class encompassing positive emotions (rare in this dataset) and neutral emotions. Each speech was tagged by three labelers, and the final emotion tags were decided by a majority vote.

Tagging all utterances yields a sequence $\{ e _ { 1 } , e _ { 2 } , . . . , e _ { \mathrm { n } } \}$ for each call, where $e _ { \mathrm { i } }$ equals 1 for a negative emotion and 0 for a non-negative emotion. This paper followed a common practice of transforming the utterance-based time series into an equally spaced time series using a sliding window. Specifically, we applied a 20-s sliding window with a 10-s sliding interval and defined the new time series as $\{ x _ { 1 } , x _ { 2 } , . . . , x _ { \mathrm { N } } \}$ where $x _ { \mathrm { i } }$ is the duration (in seconds) of negative emotion within the i-th window $[ t _ { i } , t _ { i + 1 } ]$ , and N is the number of periods (windows) in the call. The overlap of adjacent windows was chosen to ensure the smoothness of the time series. Both representations of the customer emotion sequence were used in the analyses to extract features.

## 3.3. Extracting emotion dynamics features

This paper extracted interpretable emotion sequence characteristics as input features that are easy to understand by humans and achieve high descriptive and predictive accuracy with a simple model [39]. Based on the literature, this paper included 33 emotion dynamic features and categorized the features into two groups: trajectory-based (23 fea tures) and episode-based (10 features). After collinearity checks and removing redundant features, 29 features remain (See Table 2).<sup>7</sup>

## 3.3.1. Trajectory-based features

Variability represents the range of fluctuations in emotions [23]. In our context, emotional variability reflects the amount of variation in a customer’s emotions during a service encounter. Higher variability in dicates a higher likelihood of genuine emotional fluctuations. Following the literature [12], the emotional variability, denoted as Var, can be calculated as

$$
V a r = \frac {\sum_ {i = 1} ^ {N} (x _ {i} - \bar {x}) ^ {2}}{N - 1}\tag{1}
$$

where x ¯ denotes the average value of $\{ x _ { 1 } , x _ { 2 } , . . . , x _ { \mathrm { N } } \}$

Instability refers to the amplitude of emotional changes across adja cent periods [12] and includes both variability and temporal de pendency [39]. Higher emotional instability reflects a more drastic change in emotional valence from one moment to the next. This paper adopted the most common instability measure, the mean square of successive differences (MSSD) [23], defined as

$$
M S S D = \sqrt {\frac {\sum_ {i = 1} ^ {N - 1} \left(x _ {i} - x _ {i + 1}\right) ^ {2}}{N - 1}}\tag{2}
$$

Inertia is the degree to which an emotion carries over from one moment to another, indicating resistance to change [24]. Following psychological studies (e.g., [12]) and TSC research (e.g., [32]), this paper used the autocorrelation function (ACF) and the partial autocor relation function (PACF) to measure emotional inertia. Given a time series $\{ x _ { 1 } , x _ { 2 } , . . . , x _ { \mathrm { N } } \}$ , the ACF of lag k is the correlation between $x _ { \mathrm { t } }$ and $x _ { \mathrm { t + k } } .$ . The PACF of lag k is the conditional correlation between x and $x _ { { \mathrm { t + k } } }$ with the linear dependence of $x _ { \mathrm { t } }$ on $x _ { { \mathrm { t } } + 1 }$ through $x _ { \mathrm { t + k - 1 } }$ removed. A positive value of ACF (PACF) indicates a positive correlation (partial correlation), or a stronger tendency for emotions to linger. [40] sug gested that the lag should not exceed a quarter of a sequence’s length. Applying this guideline, we calculated ACFs and PACFs with lags from 1 to 10 periods. Formally, the definition of ACF and PACF are

$$
A C F _ {k} = \operatorname{corr} \left(x _ {t}, x _ {t + k}\right) = \sum_ {i = 1} ^ {N - k} \left(x _ {t} - \bar {x}\right) \left(x _ {t + k} - \bar {x}\right) / \sum_ {t = 1} ^ {N} \left(x _ {t} - x\right) ^ {2}\tag{3}
$$

$$
P A C F _ {k} = \operatorname{corr} \left(x _ {t} - P _ {t, k} \left(x _ {t}\right), x _ {t + k} - P _ {t, k} \left(x _ {t + k}\right)\right)\tag{4}
$$

where $P _ { \mathrm { t , k } }$ (x) is a surjective operator of an orthogonal projection of x onto the linear subspace of the Hilbert space spanned by $x _ { \mathrm { t + 1 } } , x _ { \mathrm { t + 2 } } , . . . ,$ $x _ { \mathrm { t + k - 1 } } .$

This paper follows the literature to measure trends using slope $( \boldsymbol { \mathrm { e . } } \boldsymbol { \mathrm { g . } } ,$ [25,28]), defined as $s l o p e = \left( x _ { \mathrm { N } }  – x _ { 1 } \right) / \left( N - 1 \right)$ , to capture the overall di rection of the emotion trajectory without regard to local fluctuations. In our context, a rising trend indicates that a customer’s emotion is increasingly negative.

## 3.3.2. Episode-based features

Duration refers to the length of an emotion episode [22]. A longer duration of negative emotion may indicate a longer exposure to unde sirable services. We computed the total, average, longest, and shortest duration of all episodes in a service call (Dur , Dur , Dur , and $D u r _ { \mathrm { { M i n } } } ) .$

Location of an emotion episode has never been used as a predictive feature but matters in the present context. For example, a negative emotion episode at the beginning of a call may be the result of a previous service problem, whereas one at the end may indicate poor service and unresolved problems during the focal call. We computed the absolute location as the time elapsed since the beginning of the call and the relative location as the quantile of the emotion episode. We calculated the absolute and relative locations of the first and last emotion episodes $( L o c _ { \mathrm { F i r s t } } , L o c _ { \mathrm { R e l F i r s t } } , L o c _ { \mathrm { L a s t } } ,$ and $L o c _ { \mathrm { R e l L a s t } } )$ and the average absolute and relative locations of all episodes (Loc and Loc ).

## 3.4. Prediction method

After obtaining emotion dynamics features as the predictors, we chose the approach to predicting service quality. To effectively combine the heterogeneous features, we built an ensemble of component models, one for each feature set [41]. In addition, some of the features (e.g., $D u r _ { \mathrm { T o t a l } } , D u r _ { \mathrm { A v g } } )$ have severely skewed distributions due to the sparsity of negative emotions (as shown in Table 2), and there are inevitable outliers in the dataset. The objective nature of the dataset implies that the outliers cannot be simply treated as data errors and discarded, because these extreme values may be strongly related to service quality. Ideally, this paper wanted to adopt a predictive modeling approach that is robust to skewness and noise. Meanwhile, we hoped to obtain both good predictive performance and interpretable findings; thus, this paper chose a post hoc interpretation approach to explain complex underlying relationships while obtaining higher predictive accuracy [42].

This paper first constructed separate component models for trajectory- and episode-based features and then created an ensemble of the two using the stacking method for ensemble learning [43], which takes all the predictions of component models as the input of a combiner/classifier to make a final prediction. A decision tree served as a combiner to automatically determine the contribution weight of each input. For each component model, we chose XGBoost, which is widely used and is known to handle skewness and noise well and permits the computation of feature importance, and set the number of trees to 50 after experimentation. 70% of the sample is used for training, while the remaining 30% is used for testing.

Table 2 Features of emotion dynamics.

<table><tr><td>Category</td><td>Variable</td><td>Mean</td><td>Std</td><td>Min</td><td>25%</td><td>50%</td><td>75%</td><td>Max</td></tr><tr><td colspan="9">Trajectory-based features</td></tr><tr><td>Variability: amplitude of emotion fluctuations</td><td>Var</td><td>3.62</td><td>8.23</td><td>0</td><td>0</td><td>0.66</td><td>3.65</td><td>86.66</td></tr><tr><td>Instability: magnitude of consecutive emotional changes</td><td>MSSD</td><td>2.74</td><td>4.75</td><td>0</td><td>0</td><td>0.62</td><td>3.46</td><td>37.58</td></tr><tr><td rowspan="19">Inertia: degree of emotion carried over from one moment to another</td><td> $ACF_2$ </td><td>-0.03</td><td>0.16</td><td>-0.76</td><td>-0.10</td><td>0</td><td>0</td><td>0.71</td></tr><tr><td> $ACF_3$ </td><td>-0.06</td><td>0.14</td><td>-0.56</td><td>-0.14</td><td>-0.02</td><td>0</td><td>0.55</td></tr><tr><td> $ACF_4$ </td><td>-0.06</td><td>0.13</td><td>-0.57</td><td>-0.14</td><td>-0.02</td><td>0</td><td>0.49</td></tr><tr><td> $ACF_5$ </td><td>-0.06</td><td>0.12</td><td>-0.55</td><td>-0.13</td><td>-0.02</td><td>0</td><td>0.43</td></tr><tr><td> $ACF_6$ </td><td>-0.05</td><td>0.11</td><td>-0.56</td><td>-0.11</td><td>-0.02</td><td>0</td><td>0.43</td></tr><tr><td> $ACF_7$ </td><td>-0.04</td><td>0.11</td><td>-0.55</td><td>-0.10</td><td>-0.01</td><td>0</td><td>0.54</td></tr><tr><td> $ACF_8$ </td><td>-0.04</td><td>0.11</td><td>-0.45</td><td>-0.08</td><td>0</td><td>0</td><td>0.45</td></tr><tr><td> $ACF_9$ </td><td>-0.03</td><td>0.10</td><td>-0.47</td><td>-0.08</td><td>0</td><td>0</td><td>0.52</td></tr><tr><td> $ACF_{10}$ </td><td>-0.03</td><td>0.10</td><td>-0.40</td><td>-0.08</td><td>0</td><td>0</td><td>0.50</td></tr><tr><td> $PACF_1$ </td><td>0.33</td><td>0.27</td><td>-0.05</td><td>0.00</td><td>0.43</td><td>0.54</td><td>0.94</td></tr><tr><td> $PACF_2$ </td><td>-0.31</td><td>0.27</td><td>-1.18</td><td>-0.51</td><td>-0.40</td><td>0</td><td>0.23</td></tr><tr><td> $PACF_3$ </td><td>0.19</td><td>0.38</td><td>-1.52</td><td>0.00</td><td>0.14</td><td>0.29</td><td>5.53</td></tr><tr><td> $PACF_4$ </td><td>-0.26</td><td>0.76</td><td>-10.92</td><td>-0.44</td><td>-0.26</td><td>0</td><td>11.22</td></tr><tr><td> $PACF_5$ </td><td>0.24</td><td>14.50</td><td>-281.62</td><td>0.00</td><td>0.01</td><td>0.27</td><td>375.21</td></tr><tr><td> $PACF_6$ </td><td>0.02</td><td>4.51</td><td>-19.30</td><td>-0.46</td><td>-0.07</td><td>0</td><td>130.18</td></tr><tr><td> $PACF_7$ </td><td>0.18</td><td>5.47</td><td>-75.81</td><td>0.00</td><td>0</td><td>0.27</td><td>140.91</td></tr><tr><td> $PACF_8$ </td><td>-0.53</td><td>15.86</td><td>-515.73</td><td>-0.48</td><td>0</td><td>0</td><td>102.08</td></tr><tr><td> $PACF_9$ </td><td>0.45</td><td>23.87</td><td>-182.95</td><td>-0.49</td><td>0</td><td>0</td><td>724.53</td></tr><tr><td> $PACF_{10}$ </td><td>-0.76</td><td>13.74</td><td>-246.59</td><td>-0.10</td><td>0</td><td>0.30</td><td>25.31</td></tr><tr><td>Trend: overall tendency of emotional changes</td><td>Slope</td><td>9.99</td><td>35.20</td><td>-1.99</td><td>-0.03</td><td>0</td><td>0.01</td><td>1.38</td></tr><tr><td colspan="9">Episode-based features</td></tr><tr><td rowspan="4">Duration: elapsed time between the start and end of (an) emotion episode(s)</td><td> $Dur_{Total}$ </td><td>2.76</td><td>4.71</td><td>0</td><td>0</td><td>3.19</td><td>10.01</td><td>931.95</td></tr><tr><td> $Dur_{Avg}$ </td><td>4.12</td><td>8.08</td><td>0</td><td>0</td><td>1.95</td><td>3.86</td><td>66.58</td></tr><tr><td> $Dur_{Max}$ </td><td>1.84</td><td>3.72</td><td>0</td><td>0</td><td>2.36</td><td>5.51</td><td>146.62</td></tr><tr><td> $Dur_{Min}$ </td><td>49.71</td><td>67.69</td><td>0</td><td>0</td><td>1.07</td><td>2.33</td><td>66.58</td></tr><tr><td rowspan="3">Location: absolute and relative location of emotion episodes</td><td> $Loc_{First}$ </td><td>0.33</td><td>0.30</td><td>0</td><td>0</td><td>16.60</td><td>78.35</td><td>408.29</td></tr><tr><td> $Loc_{Last}$ </td><td>106.08</td><td>117.87</td><td>0</td><td>0</td><td>83.43</td><td>179.36</td><td>1529.44</td></tr><tr><td> $Loc_{RelAvg}$ </td><td>-0.02</td><td>0.16</td><td>0</td><td>0</td><td>0.35</td><td>0.56</td><td>0.97</td></tr></table>

Our explainability design has two parts: (1) obtaining the predictive ability of each emotion dynamics feature, and (2) extracting the rela tionship between each feature and service quality. For the first part, we adopted permutation feature importance [44]. When we permute that feature while keeping others unchanged, the more important a feature is, the more likely the prediction error will change. For the second part, we used the accumulated local effects (ALE) method [45] to describe and visualize the effect of features on prediction targets. We first divided a feature into several windows and then measured how the model pre dictions change when replacing the feature value with boundary values for data instances in that window, and then accumulated the average effects across all windows. Compared with similar methods, such as the partial dependence plot, ALE is more trustworthy, effective, and unbi ased when predictors are correlated [46] and ALE plots can capture different types of linear and nonlinear relationships.

## 4. Prediction performance

## 3.5. Explanation method

This section reports the predictive performance of our approach (using customer emotion to predict service quality) against the bench marks. Because the company’s priority is to find low-quality service calls, the ideal performance metric should focus on the low-quality class. Following literature predicting customer satisfaction [47,48], we use the F1-score – the harmonic mean of precision and recall – of the low-quality class as our performance metric.

Based on common practices for gauging service quality, this study constructed two models as benchmarks: a quality-inspection-based model and an operational-indices-based model. In our context, the quality inspection covers multiple dimensions, including attitude, behavior, and expertise, with a total of 22 items.<sup>8</sup> The operationalindices-based benchmark model includes basic information on cus tomers (e.g., gender, city, and inbound call history) and call details $( \boldsymbol { \mathrm { e . } } \boldsymbol { \mathrm { g . } } ,$ call duration, silence duration, and number of turns). There are 12 items in this feature set (see Appendix A for details). We tried several commonly used classifiers (XGBoost, logistic regression, decision tree, neural network, and Adaboost). As seen in Table 3, we obtained the best result using XGBoost and our approach obtained a higher F1-score (of 0.529) than the two benchmark models using the quality-inspection features and operational indices (their best F1-scores are 0.261 and 0.458, respectively). While our model’s F1-score is not particularly $\mathrm { \ h i g h } , ^ { \mathrm { \ 9 } }$ it is a significant improvement over the two benchmark ap proaches. In other words, if the company uses our approach instead of using quality inspection results or calls’ operational indices to predict service quality, they would obtain a notably better performance. This confirms the benefit of using customer emotion to predict service quality, answering our first research question.

Table 3  
Prediction performance: comparison with benchmarks (F1-score for negative class). The best test result is presented in bold.

<table><tr><td></td><td>Using</td><td>XGBoost</td><td>Logistic regression</td><td>Decision tree</td><td>Neural network</td><td>Adaboost</td></tr><tr><td>Our method</td><td>Customer emotion dynamics</td><td>0.529</td><td>0.499</td><td>0.497</td><td>0.410</td><td>0.468</td></tr><tr><td>Benchmark 1</td><td>Quality inspection</td><td>0.201</td><td>0.261</td><td>0.212</td><td>0.205</td><td>0.215</td></tr><tr><td>Benchmark 2</td><td>Operational indices</td><td>0.458</td><td>0.417</td><td>0.426</td><td>0.259</td><td>0.423</td></tr></table>

We further evaluated the performance of our method for emotionsequence classification by comparing it with a host of widely used, high-performance TSC methods, including DTW-KNN, EE, TSF, BOSS, random interval spectral ensemble (RISE) [32], Shapelets, and HIVE-COTE. This paper excluded deep learning models because our sample size is too small to meet the requirements of these models, and, in any case, studies have shown that they do not outperform the aforemen tioned models (e.g., [31]). We implemented the aforementioned models using sktime, a Python framework with a comprehensive collection of advanced TSC algorithms proposed by recent research.<sup>10</sup>

Table 4 describes the features and classifiers of each model. Table 4 shows that our approach obtained a higher F1-score than the other TSC methods (Rows (2) through (8) in Table 4). We thus conclude that the

Prediction performance: Comparison with other TSC methods (F1-score for negative class). The result of our method and the best benchmark method is presented in bold for comparison purposes.

<table><tr><td></td><td>Method</td><td>Features</td><td>Classifier</td><td>F1-score</td></tr><tr><td>(1)</td><td>Our method</td><td>Emotion dynamics features listed in Table 2</td><td>XGBoost</td><td>0.529</td></tr><tr><td>(2)</td><td>DTW-KNN</td><td>DTW distance</td><td>KNN</td><td>0.336</td></tr><tr><td>(3)</td><td>EE</td><td>Eight distance metrics</td><td>KNN</td><td>0.314</td></tr><tr><td>(4)</td><td>TSF</td><td>Standard deviation, average, and slope of random intervals</td><td>Ensemble of decision trees</td><td>0.442</td></tr><tr><td>(5)</td><td>BOSS</td><td>Word and Fourier transformation</td><td>KNN</td><td>0.446</td></tr><tr><td>(6)</td><td>RISE</td><td>ACF, PACF, and powerspectrum of random intervals</td><td>Ensemble of decision trees</td><td>0.448</td></tr><tr><td>(7)</td><td>Shapelets</td><td>Discriminative subseries</td><td>Ensemble of decision trees</td><td>0.176</td></tr><tr><td>(8)</td><td>HIVE-COTE</td><td></td><td>Weighted ensemble of (2), (3), (4), (5), (6), and (7)</td><td>0.346</td></tr></table>

TSC method we develop for customer emotion classification is superior to the state-of-the-art methods as documented in the literature. It is also worth noting that most benchmark methods are not explainable and only focus on a subset of features (See Section 2.3 for details).

Finally, this paper drilled down on emotion’s effect on specific di mensions of service quality. In practice, companies require such knowledge to better diagnose which dimension of service needs improvement and to provide recovery strategies. We constructed models to predict each of the four dimensions of service quality (reliability, responsiveness, assurance, and empathy) based on emotion dynamics features. Table 5 shows that our method outperforms the benchmarks based on quality inspection and operational indices in three service quality dimensions, i.e., responsiveness, assurance, and empathy. The quality-inspection-based model (benchmark 1) obtain a higher F1-score than our model on the reliability dimension. One explanation is that most quality assurance metrics are closely related to service reliability, giving the quality-inspection-based model an advantage in predicting consumers’ reliability ratings.

## 5. Explanation

From the prediction model, we proceed to the explanation element of our method by investigating the relationships between specific features of emotion dynamics and service quality.

We first examined feature importance. Table 6 shows the permutation feature importance score and rank of each feature. We observe that the trajectory-based features, which capture global sequence patterns, have greater predictive power than the local episode-based features.

Of the trajectory-based features (including the categories of vari ability, instability, inertia, and trend), $P A C F _ { 1 0 }$ and $A C F _ { 1 0 }$ have the highest predictive ability. Long-lag (6–10) inertia is more predictive than short-lag (1–5) inertia, with average feature importance of 0.046 and 0.022, respectively. The result indicates that whether a consumer’s negative emotion is likely to persist for a long time is an important signal of service quality. Among the remaining features, instability (MSSD) is more important than variability (Var) and trend (Slope).

Of the episode-based features (including duration and location), the top feature is the location of the last emotion episode $( L o c _ { \mathrm { L a s t } } )$ . The average importance of location-related features (0.0187) is larger than that of the duration-based features (0.0173).

To understand how the change of emotion impacts service quality, we visualized the marginal effect of features using ALE plots (Table 7).

Because of space limitations, this paper presents ALE plots for the most important feature in each category. We observe the following from the ALE plots.

First, when the customer’s negative emotions in the service encounter have a high fluctuation (more variable and unstable), positive trend, or long duration, the perceived quality is likely to be low. The ALE plots of variability and instability (Table 7 (a) (b)) show that a large fluctuation in negative emotions during service calls indicates low ser vice quality. For the trend feature, the ALE curve (Table 7 (d)) is almost linear, indicating the covariant relationship between customers’ nega tive emotions and low service quality. Moreover, the longer the duration of emotion episodes $( D u r _ { \mathrm { T o t a l } } , D u r _ { \mathrm { M a x } } , D u r _ { \mathrm { M i n } } ,$ and $D u r _ { \mathrm { { A v g } } } ) _ { \mathrm { { ; } } }$ , the more likely the encounter is of low quality. Table 7 (e) shows that when the total duration of negative emotions is larger than a threshold (16 s), it is positively correlated with the likelihood of low quality.

Second, when a customer’s emotion status has a lower intention to linger, the service quality is more likely to be low. The ALE plot of the most important inertia feature $( P A C F _ { 1 0 } ,$ Table 7 (c)) shows that a small (large) absolute value indicates low (high) quality. In other words, when the partial correlation between emotion at t and $t + 1 0$ is small, the service quality is likely to be low.

Table 5  
Prediction results of four dimensions of service quality (F1-score for negative class). We present the best test result in four dimensions of service quality in bold.

<table><tr><td></td><td>Using</td><td>Reliability</td><td>Responsiveness</td><td>Assurance</td><td>Empathy</td></tr><tr><td>Our method</td><td>Customer emotion dynamics</td><td>0.187</td><td>0.466</td><td>0.308</td><td>0.352</td></tr><tr><td>Benchmark 1</td><td>Quality inspection</td><td>0.269</td><td>0.227</td><td>0.178</td><td>0.159</td></tr><tr><td>Benchmark 2</td><td>Operational indices</td><td>0.143</td><td>0.332</td><td>0.130</td><td>0.319</td></tr></table>

Table 6  
Feature importance.

<table><tr><td>Category</td><td>Measure</td><td>Importance</td><td>Rank</td><td>Category</td><td>Measure</td><td>Importance</td><td>Rank</td></tr><tr><td>Variability</td><td>Var</td><td>0.037</td><td>8</td><td>Inertia (cont&#x27;d)</td><td> $PACF_5$ </td><td>0.015</td><td>23</td></tr><tr><td>Instability</td><td>MSSD</td><td>0.097</td><td>3</td><td></td><td> $PACF_6$ </td><td>0.023</td><td>15</td></tr><tr><td rowspan="13">Inertia</td><td> $ACF_2$ </td><td>0.024</td><td>13</td><td></td><td> $PACF_7$ </td><td>0.036</td><td>9</td></tr><tr><td> $ACF_3$ </td><td>0.01</td><td>27</td><td></td><td> $PACF_8$ </td><td>0.016</td><td>21</td></tr><tr><td> $ACF_4$ </td><td>0.014</td><td>24</td><td></td><td> $PACF_9$ </td><td>0.04</td><td>7</td></tr><tr><td> $ACF_5$ </td><td>0.072</td><td>5</td><td></td><td> $PACF_{10}$ </td><td>0.134</td><td>1</td></tr><tr><td> $ACF_6$ </td><td>0.006</td><td>28</td><td>Trend</td><td>Slope</td><td>0.026</td><td>10</td></tr><tr><td> $ACF_7$ </td><td>0.023</td><td>14</td><td>Duration</td><td> $Dur_{Total}$ </td><td>0.019</td><td>17</td></tr><tr><td> $ACF_8$ </td><td>0.054</td><td>6</td><td></td><td> $Dur_{Avg}$ </td><td>0.019</td><td>18</td></tr><tr><td> $ACF_9$ </td><td>0.016</td><td>19</td><td></td><td> $Dur_{Max}$ </td><td>0.015</td><td>22</td></tr><tr><td> $ACF_{10}$ </td><td>0.111</td><td>2</td><td></td><td> $Dur_{Min}$ </td><td>0.016</td><td>20</td></tr><tr><td> $PACF_1$ </td><td>0.081</td><td>4</td><td>Location</td><td> $Loc_{First}$ </td><td>0.013</td><td>25</td></tr><tr><td> $PACF_2$ </td><td>0.011</td><td>26</td><td></td><td> $Loc_{Last}$ </td><td>0.024</td><td>12</td></tr><tr><td> $PACF_3$ </td><td>0.004</td><td>29</td><td></td><td> $Loc_{RelAvg}$ </td><td>0.019</td><td>16</td></tr><tr><td> $PACF_4$ </td><td>0.026</td><td>11</td><td></td><td></td><td></td><td></td></tr></table>

Table 7  
Accumulated Local Effects (ALE) of important features.  
![](/api/attachments/64DEHFQK/fulltext/images/72a104147dbc60cca771aa57d08a88969f585abc5517a013689417a3372e30b8.jpg)  
Notes: The x-axis of the ALE plots is the scaled value of the features. For better visualization, we transform skewed distributions with a square-root function or quantile transformation to make them closer to normal distribution. Then we keep the value between the 5% to 95% quantiles and use polynomial functions to fit the curve. The y-axis is the ALE value, representing the centered probability of low service quality. The larger the ALE value, the more likely the service encounter is of low quality. A zero ALE value represents the mean effect of the feature on service quality.

Third, the location where the last emotion episode appears in a call has a U-shaped relationship with low service quality. The plot in Table 7 (f) indicates that if the last negative emotion episode appears more than

170 s after the service begins, the service is more likely to be low-quality. After a long service procedure, it is certainly the employee’s re sponsibility that he or she failed to soothe the customers’ feelings or even aroused anger. If the last emotion episode occurs shortly after the call begins, the service encounter might also be of low quality.

<sup>11</sup> Examining the data, we find two primary explanations for this situation: (a) the encounter is short and the expected service is not performed (e.g., the service employee announces that he/she cannot offer any help), leading to low service quality, or (b) the customer had high expectations before the service but soon received only perfunctory service, which does not lead to the expression of additional negative emotions but is not satisfying.

## 6. Application

This section instantiates the application of our method by developing an IT artifact that automatically measures service quality based on automatic emotion-recognition techniques. We also apply the measure for a specific business purpose, which, as suggested by our research site (the insurance company), is to identify customers who have referral intentions.

Customers’ referral intentions are the best predictor of revenue growth because consumers tend to trust recommendations from friends [49]. It is crucial for companies to carefully manage referral programs [50]. In the present context, the insurance company conducts post service surveys, directly asking sampled customers whether they would recommend the company. Again, the surveys are time-consuming and labor-intensive and may disturb the customer. In theory, customers referral intention covaries with the quality of the service they have received [37], so we developed an IT artifact using the service quality measure to predict referral intention by the following three steps.

In Step 1, the artifact automatically detects customer emotions from service calls. As described in Section 3, in developing our method, we manually labeled customers’ emotions. To be fully automated, the IT artifact must be able to automatically tag a customer’s emotion during a service call. Based on a review of state-of-the-art automatic emotion recognition techniques, we designed a system for real-time emotion recognition. The system leveraged three AI techniques (CNN, RNN, and SVM) and two types of features (linguistic and acoustic features) to build six independent models. The acoustic features include Mel frequency cepstrum coefficient (MFCC) and spectrogram, and the linguistic fea tures include n-gram and word2vec. We then integrated the six models using the ensemble method. The ensemble model achieved an accuracy of 87%, an average recall of 65.05%, and an average F-score of 0.684, which outperforms most models based on natural speech (see model details and evaluation results in Appendix B). It provided an emotion tag for each speech utterance. And all the identified emotion tags of the speech utterances in one service call made up the customer’s emotion sequence.

In Step 2, we used the emotion sequence generated from the above process to predict the service quality of a phone call. We retrained the method developed in Section 3 using automatically tagged emotions and applied it. The company provided a set of 2140 service calls that include complete records of quality inspections and post-service customer sur veys. We divided the set into two parts, with 1500 calls for training and the rest for prediction. Our method of using customer emotion (auto matically tagged this time) to predict service quality outperformed the benchmark model based on operational indices. These operational indices can be obtained automatically, whereas the quality inspection is executed manually and therefore does not serve as a reasonable benchmark for an automatic IT artifact.

In Step 3, we used the automatic measure of service quality to predict referral intention. The company provided another set of 1500 service calls, in which 40% of customers indicated, in the post-service survey, willingness to recommend the company to friends. For each of the phone calls, we automatically generated service-quality measures based on the above two steps. Then, we used 70% of the data to train a referral pre diction model and reserved the rest for testing. To be specific, we used the probabilities of four dimensions of service quality as features and XGBoost as the classifier. We have two benchmarks in this analysis. The first uses a set of operational indices of a service call to predict referral intention. For the second, we trained a model to predict referral inten tion by using actual service quality (in the four dimensions) collected via customer surveys. This provides the best possible prediction result based on service quality, in that customer surveys provide the “ground truth” of service quality. Table 8 presents the prediction model’s performance (recall and precision) on the recommendation probability. The auto matic IT artifact significantly outperforms the benchmark of using operational indices. The performance of the automatic IT artifact is slightly inferior to the benchmark of using actual service quality. It is deemed acceptable by the insurance company because the automatic IT artifact can scan all service encounters, far more than the original level of 2%, potentially enlarging the pool of sales prospects.

Table 8  
Referral intention prediction.

<table><tr><td></td><td>Predict referral intention using</td><td>Recall</td><td>Precision</td></tr><tr><td>(1)</td><td>Operational indices of the service call</td><td>52.74%</td><td>51.73%</td></tr><tr><td>(2)</td><td>Actual service quality (ground truth, collected via customer survey)</td><td>91.56%</td><td>58.33%</td></tr><tr><td>(3)</td><td>Service-quality measure based on customer emotion (our method)</td><td>86.50%</td><td>54.25%</td></tr></table>

## 7. Discussion

## 7.1. Contributions

This study makes several contributions. First. we develop an effective method for measuring service quality, a core variable in service science, based on customer emotion. Our method leverages AI techniques (e.g., TSC, automatic emotion recognition, and explainable AI methods) and is automatic and scalable. Using real-world data, we verify that it is su perior to manual quality inspection and operational indices for identi fying low service quality. Compared with widely used approaches such as customer surveys and quality inspection, our method is automatic, cost-effective, real-time, and better positioned to generate a large-scale or longitudinal sample of service quality. This enables better theory testing with greater statistical power and the development of theory interested in temporal changes for domains such as e-service, e-gov ernment, and e-commerce. Using real-world data, we show that the measure is useful for predicting customers’ referral intentions, which is a further testament to the measure’s nomological validity.

Second, our findings based on explainable AI contribute to the ser vice literature. The interpretation of our model highlights the impor tance of features of customer emotion dynamics and shows which dynamic characteristics of consumer emotions may correlate with low service quality and these characteristics’ particular effects. Prior research has mainly examined the customer’s emotion at a single-point state, usually at the end of the service encounter [20]. Our approach sheds light on the relationships between characteristics of customer emotional dynamics during the service encounter and perceived service quality. The results show that when negative emotions are highly fluc tuating, showing a positive trend, or long-lasting, perceived service quality is likely to be low. The results also show that the location where the last emotion episode appears in a service call has a U-shaped rela tionship to low quality. These findings deepen our understanding of the relationship between customer emotion and service quality.

Third, on the technical side, we propose a classification framework for using customer emotion dynamics. Although the literature provides a rich pool of TSC methods, it lacks research on which methods are suit able for emotion sequence analysis. Unlike existing methods, we propose a TSC framework that is explainable, sensitive to the time location of emotional events, and combines trajectory- and episode-based features. We use unstructured multi-media data containing extremely rich in formation that aids in decision-making. Our approach outperforms the state-of-the-art TSC methods in our research context. This approach for emotion-sequence analysis is also promising for other contexts, such as recommendations, online reviews, and online education.

Fourth, we demonstrate how to integrate emotion recognition technologies and emotion sequence analysis into decision support sys tems. Our prototype system enables real-time prediction of service quality using information contained in customer emotions. While pre vious studies have extensively studied emotion recognition techniques, they seldom study how they can be used in real-world applications. We provide one of the first evidence of their value in predicting service quality and referral intention.

Finally, we showcase how to harness the potential of customer speech data for generating valuable business insights, thereby making a significant contribution to the decision support systems literature. Customer speech, particularly in call centers, represents a valuable yet underutilized data source. The existing literature does not provide suf ficient information regarding the implementation of speech emotion recognition using real-world speech data, as it primarily focuses on using acted data. Our system offers a comprehensive integration of realtime voice input analysis, encompassing noise reduction, voice activity detection, voice feature extraction and classification. By leveraging this system, we can gain valuable insights that can inform the design and implementation of future speech-based decision support systems.

## 7.2. Managerial implications

Our study offers significant practical value to managers and customer service professionals. First, we designed an effective approach that is highly scalable, automated, and of low cost, addressing a crucial bottleneck in service-quality management. The entire service-quality prediction process using real-time speech data can be completed in seconds, which opens up opportunities for in-time interventions. Com panies can also integrate the service-quality prediction model into other applications, such as referral reward programs, to enhance business performance.

Our explainable AI approach has the key advantage of allowing practitioners to gain insights into why a particular call receives a particular service-quality score. For example, managers can use our ALE plots in coaching service employees and pinpoint whether a low-quality call suffers from large instability of negative emotion. Similarly, our analysis of feature importance can help managers prioritize their monitoring and intervention efforts. Overall, our system enables a better understanding of customer emotions and more prompt managerial support.

## 7.3. Limitations and future research

This work is subject to several limitations that should be addressed in future research. First, our analysis is based on a limited-size dataset. We expect that with increased data size, one can obtain higher predictive performance [51]. Second, our findings on how emotional dynamics are related to service quality are data-driven and exploratory. Future research should complement these findings by further validating such relationships, perhaps using experiments and surveys. Third, because we lack information about a customer’s service history, we cannot personalize the prediction by leveraging past information. With repeat customers, this could be a useful direction for future work. With more customer information, prediction performance can be improved. Finally, this study focuses on voice data only. Future research could combine our method with other data sources (e.g., video and texts) to further improve predictive performance.

## CRediT authorship contribution statement

Yiting Guo: Conceptualization, Methodology, Software, Data cura tion, Visualization, Writing – original draft. Yilin Li: Conceptualization, Methodology, Software, Data curation, Writing – original draft. De Liu: Conceptualization, Writing – review & editing, Supervision. Sean Xin Xu: Conceptualization, Resources, Writing – review & editing, Supervision.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

The authors do not have permission to share data.

## Appendix A. Operational indices

Table A.1  
Operational indices.

<table><tr><td></td><td>Item</td><td>Reference</td></tr><tr><td>Customer information</td><td>Customer genderCustomer city classification (1–5 classes)Number of historical inbound calls before this encounter</td><td>[52]</td></tr><tr><td>Call information</td><td>Call time (morning, afternoon, evening)Silence durationNumber of turns taken by an agentNumber of turns taken by a customerTotal utterance duration of customersAverage utterance duration of customersAverage utterance duration of agentDuration of dialogs</td><td>[53][54][55][55]</td></tr></table>

## Appendix B. Automatic customer emotion recognition system

The system for real-time automatic customer emotion recognition consists of three modules: preprocessing, feature extraction, and emotion recognition.

Preprocessing

Noise reduction

The input audio stream may be mixed with background noises such as wind, TV, vehicles, and other people. We apply a classic method, the adaptive Weiner filter, to reduce the noise and increase the signal-to-noise ratio [56].

## Voice activity detection and speaker recognition

After de-noising, we divide speech into segments, each of which is an utterance or complete sentence spoken by one person, using a popular algorithm proposed by [57]. Segments that are not suitable for customer emotion recognition (e.g., overlapping utterances, without human speech) are excluded from further analyses. We then classify the speech segments by speakers using the Gaussian Mixture Model with Bavesian Information Criterion [58]. Only customers’ speech segments are used in the following analyses.

## Speech-to-text conversion

We convert the speech into text using the automatic speech recognition service of Iflytek, a leading vendor for Mandarin speech recognition.

## Text preprocessing

First, we perform tokenization and expand abbreviations to their full forms. We remove words that provide little information about emotion (e.g., special entities’ names) and retain stop words because they may contain important emotional information (e.g., “not” in “A delay of two weeks does not please me”).

## Feature extraction

After preprocessing, the raw data has been converted into audio segments and the corresponding texts. We extract two kinds of acoustic features from the audio: Mel frequency cepstrum coefficient (MFCC) and spectrogram. MFCC is one of the most well-known acoustic features, widely used in speech analysis [59]. Spectrogram is a visual representation of audio signals in the time-frequency domain and is usually used as input into deep learning models [60]. Each speech segment is transformed into a spectrogram using the Short-Time Fourier Transform algorithm. The size of the spectrogram is 129 × n, where 129 is the dimension of the frequency domain and n is the number of frames in the segment.

The linguistic features are extracted from speech texts, including n-gram and word2vec. N-gram refers to a contiguous sequence of n words in the given sentence [61]. N-gram has the merit of simplicity and has been applied in text categorization, machine translation, and emotion recognition. We keep unigrams (n = 1) and bigrams (n = 2) because spoken dialogs are usually short, incomplete, and disjointed. We select 70% of the most infor mative n-gram features using Chi-square tests.

Word2vec is a widely used word embedding that maps all the words and phrases to vectors of real numbers [62]. In this study, the word vector’s dimension is 50, and the context window size is 8. Words with a frequency less than 5 are removed. Finally, we obtain 50 × n word vectors, where n is the number of words in the segment.

## Emotion recognition

The emotion-recognition module classifies customers’ speech segments into negative and non-negative emotions using extracted acoustic and linguistic features as inputs. After exploring a host of classifier-feature combinations,<sup>12</sup> the current study applies three classifiers with better performance—CNN, RNN, and SVM—on different acoustic/linguistic inputs and obtains six classification models. We then integrate the six models using the ensemble method (as shown in Fig. B.1).

![](/api/attachments/64DEHFQK/fulltext/images/66c7d4c9091ce9081d3b85d87b92d13d6f391c2fcfc88bb3aa3e9b8cfc0eb862.jpg)  
Fig. B.1. Speech emotion recognition models.

We construct two CNN models, one using MFCC features (called CNN-MFCC hereafter) and the other using spectrograms (CNN-Spectrogram). CNN has advantages in extracting high-level abstract features and reducing dimensionality, which is also important in classifving high-dimension audio data, To model the temporal dynamic linguistic feature, we run an RNN model. Specifically, we choose Gated Recurrent Unit (GRU) for its low computational costs.

Support Vector Machine (SVM) is a supervised machine learning algorithm, especially suitable for nonlinear classification problems. Compared with neural networks, SVM shows superiority in small datasets. We create three SVM models—SVM-MFCC, SVM-Ngram, and SVM-Word2vec—for MFCC (acoustic), n-gram (linguistic), and word2vec (linguistic) features, respectively.

We then create an ensemble of these different models. Specifically, we assign each classifier a weight, W , to represent its importance and use the weighted average ensemble method. The ensemble output y is given by $\begin{array} { r } { y _ { i j } = \sum _ { k = 1 } ^ { K } W _ { k } \bullet P _ { i j k } ^ { N e g a t i \nu e } } \end{array}$ , where $W _ { \mathrm { k } }$ ranges from 0 to 1, with a constraint $\begin{array} { r } { \sum _ { k = 1 } ^ { K } W _ { k } = 1 \mathrm { a n d } P _ { i j k } \mathrm { P } _ { \mathrm { i j k } } ^ { \mathrm { N e g a t i v e } } } \end{array}$ is the predicted probability of the negative emotion class by classifier k for the j-th segment of the i-th call. We train three ensemble models: the linguistic ensemble model (including RNN-Word2vec, SVM-Ngram, and SVM-Word2vec), the acoustic ensemble mode (including CNN-MFCC, CNN-Spectrogram, and SVM-MFCC), and the acoustic-linguistic ensemble model (which integrates all six models). Evaluation

In management practice, we need to identify customers' negative emotions as precisely as possible. We use three evaluation metrics (precision recall, and F-score) in the negative class and set β in the F-score at 0.5 to assign more weight to precision. Table B.1 reports the performance of the six independent models and three ensemble models. The results show that ensemble models perform better overall. And integrating both acoustic and linguistic information of speech is more beneficial than using uni-channel information.

The results show that all models perform well beyond the chance level. All three ensemble models achieve higher precision than the independent models, and the acoustic-linguistic-ensemble model achieves the best precision of the nine models. The acoustic-linguistic-ensemble model has an average recall of 65.05% and an average F-score of 0.684, higher than the literature using real-world speech data. And this model achieves an accuracy of 87%, which is among the best models based on natural speech in the literature.

Table B.1  
Performance of individual and ensemble models.

<table><tr><td>Feature type</td><td>Models</td><td>Recall</td><td>Precision</td><td>F-score</td></tr><tr><td rowspan="4">Acoustic</td><td>(1) CNN-MFCC</td><td>21.12%</td><td>40.96%</td><td>0.345</td></tr><tr><td>(2) CNN-Spectrogram</td><td>63.98%</td><td>44.02%</td><td>0.470</td></tr><tr><td>(3) SVM-MFCC</td><td>38.82%</td><td>38.82%</td><td>0.388</td></tr><tr><td>(4) Acoustic Ensemble: 1 + 2 + 3</td><td>36.96%</td><td>57.77%</td><td>0.519</td></tr><tr><td rowspan="4">Linguistic</td><td>(5) SVM-Ngram</td><td>11.49%</td><td>55.22%</td><td>0.314</td></tr><tr><td>(6) SVM-Word2vec</td><td>35.40%</td><td>40.43%</td><td>0.393</td></tr><tr><td>(7) RNN-Word2vec</td><td>34.16%</td><td>48.46%</td><td>0.447</td></tr><tr><td>(8) Linguistic Ensemble: 5 + 6 + 7</td><td>24.53%</td><td>56.43%</td><td>0.448</td></tr><tr><td>Acoustic + Linguistic</td><td>(9) Acoustic-linguistic Ensemble: 1 + 2 + 3 + 5 + 6 + 7</td><td>33.23%</td><td>66.05%</td><td>0.552</td></tr></table>

Notes: In order to maintain stable predictive performance under realistic conditions, we construct the test data set with the ratio of positive: negative =5.5:1, so the chance level of precision is 15.38%.

## References

[1] R. Ladhari, A review of twenty years of SERVQUAL research, Int. J. Qual. Serv. Sci. 1 (2009) 172–198, https://doi.org/10.1108/17566690910971445.

[2] M. Blut, N. Chowdhry, V. Mittal, C. Brock, E-service quality: a meta-analytic review, J. Retail. 91 (2015) 679–700.

[3] R. Nishant, S.C. Srivastava, T.S. Teo, Using polynomial modeling to understand service quality in e-government websites, MIS O. 43 (2019) 807–826.

[4] M. Saberi, O. Khadeer Hussain, E. Chang, Past, present and future of contact centers: a literature review. Bus, Process, Manag, J. 23 (2017) 574–597. https:/ doi.org/10.1108/BPMJ-02-2015-0018.

[5] Berry Zeithaml, Parasuraman, communication and control processes in the delivery of service quality, J. Mark. 52 (1988) 35–48.

[6] N. Gans, G. Koole, A. Mandelbaum, Telephone call centers: tutorial, review, and research prospects, Manuf. Sery, Oper, Manag. 5 (2003) 79–141, https://doi,org/ 10.1287/msom 5.2.79.16071

[7] N. Berente, B. Gu, J. Recker, R. Santhanam, Managing AI. Call for papers, MIS Q. (2019) 1–5.

[8] E. Brynjolfsson, C. Wang, X. Zhang, The economics of IT and digitization: eight questions for research, MIS Q. 45 (2021) 473.

[9] A. Adadi, M. Berrada, Peeking inside the black-box: a survey on explainable artificial intelligence (XAI), IEEE Access. 6 (2018) 52138–52160, https://doi.org/ 10.1109/ACCESS.2018.2870052

[10] C.J. White, The impact of emotions on service quality, satisfaction, and positive word-of-mouth intentions over time, J. Mark. Manag. 26 (2010) 381–394, https:/ doi.org/10.1080/02672571003633610.

[11] I. Guyon, A. Elisseeff, An introduction to feature extraction, in: Featur. Extr., Springer, Berlin, Heidelberg, 2006, pp. 1–25.

[12] M. Houben, W. Van Den Noortgate, P. Kuppens, The relation between short-term emotion dynamics and psychological well-being: a meta-analysis, Psychol. Bull. 141 (2015) 901–930.

[13] A.K. Jaiswal, Customer satisfaction and service quality measurement in Indian call centres, Manag. Serv. Qual. 18 (2008) 405–416, https://doi.org/10.1108 09604520810885635.

[14] A. Miciak, M. Desmarais. Benchmarking service quality performance at business 340–353.

[15] W. Boulding, A. Kalra, R. Staelin, V.A. Zeithaml, A dynamic process model of service quality: from expectations to behavioral intentions, J. Mark. Res. 30 (1993) 7, https://doi.org/10.2307/3172510.

[16] H. Liao, A. Chuang, A multilevel investigation of factors influencing employee service performance and customer outcomes, Acad. Manag. J. 47 (2004) 41–58, https://doi.org/10.2307/20159559.

[17] A. Parasuraman, V.A. Zeithaml, L.L. Berry, A conceptual model of service quality and its implications for future research, J. Mark. 49 (1985) 41, https://doi.org 10.2307/1251430

[18] J. Walls, G. Widmeyer, O. El-Sawy, Building an information system design theory for vigilant EIS, Inf. Syst. Res. 3 (1992) 36–59, https://doi,org/10.1287 isre.3.1.36.

[19] M.K. Brady, J.J. Cronin Jr., Some new thoughts on conceptualizing perceived service quality: a hierarchical approach, J. Mark. 65 (2001) 34–49, https://doi. org/10.1509/jmkg.65.3.34.18334.

[20] A.S. Mattila, C.A. Enz, The role of emotions in service encounters, J. Sery, Res, 4 (2002) 268–277, https://doi.org/10.1177/1094670502004004004.

[21] S. Gregor, A.C.H. Lin, T. Gedeon, A. Riaz, D. Zhu, Neuroscience and a nomological network for the understanding and assessment of emotions in information systems research, J. Manag. Inf. Syst. 30 (2014) 13–48.

[22] P. Verduyn, P. Delaveau, J.Y. Rotg´e, P. Fossati, I. Van Mechelen, Determinants of emotion duration and underlying psychological and neural mechanisms, Emot. Rev. 7 (2015) 330–335, https://doi.org/10.1177/1754073915590618.

[23] E.M. Seabrook, M.L. Kern, B.D. Fulcher, N.S. Rickard, Predicting depression from language-based emotion dynamics: longitudinal analysis of facebook and twitter status updates, J. Med. Internet Res. 20 (2018), https://doi.org/10.2196 imir.9267.

[24] P. Kuppens, N.B. Allen, L.B. Sheeber, Emotional inertia and psychological maladjustment, Psychol. Sci. 21 (2010) 984–991, https://doi.org/10.1177 0956797610372634

[25] A. Pascual-Leone, How clients “change emotion with emotion”: a programme of research on emotional processing, Psychother. Res. 28 (2018) 165–182, https:// doi.org/10.1080/10503307.2017.1349350.

[26] P. Kuppens, P. Verduyn, Looking at emotion regulation through the window of emotion dynamics, Psychol. Inq. 26 (2015) 72–79, https://doi.org/10.1080/ 1047840X.2015.960505

[27] J. Lines, A. Bagnall, Time series classification with ensembles of elastic distance measures, Data Min. Knowl. Disc. 29 (2015) 565–592, https://doi.org/10.1007/ s10618-014-0361-2.

[28] H. Deng, G. Runger, E. Tuv, M. Vladimir, A time series forest for classification and feature extraction. Inf. Sci. (Ny). 239 (2013) 142–153. https://doi,org/10.1016/i ins,2013.02,030.

[29] L. Ye. E. Keogh, Time series shapelets: a new primitive for data mining, in: Proc 15th ACM SIGKDD Int. Conf. Knowl. Discov. Data Min., 2009, pp. 947–956.

[30] P. Schafer, ¨ The BOSS is concerned with time series classification in the presence of noise, Data Min. Knowl. Disc. 29 (2015) 1505–1530, https://doi.org/10.1007/ s10618-014-0377-7

[31] H.I. Fawaz, G. Forestier, J. Weber, L. Idoumghar, P.A. Muller, Deep learning for time series classification: a review, Data Min. Knowl. Disc. 33 (2019) 917–963, https://doi.org/10.1007/s10618-019-00619-1.

[32] J. Lines, S. Tavlor. A. Bagnall. Time series classification with HIVE-COTE: the hierarchical vote collective of transformation-based ensembles, ACM Trans. Knowl Discov, Data 12 (2018) https://doi org/10.1145/3182382

[33] H.A. Dau, A. Bagnall, K. Kamgar, C.C.M. Yeh, Y. Zhu, S. Gharghabi, C. A. Ratanamahatana. E. Keogh. The UCR time series archive, JEEE/CAA J. Autom Sin. 6 (2019) 1293–1305.

[34] J.J.P.A. Hsieh, A. Rai, S.X. Xu. Extracting business value from IT: a sensemaking perspective of post-adoptive use, Manag, Sci. 57 (2011) 2018–2039, https://doi. org/10.1287/mnsc.1110.1398.

[35] A. Parasuraman, L.L. Berry, V.A. Zeithaml, Refinement and reassessment of the SERVQUAL scale, J. Retail. 67 (1991) 420, https://doi.org/10.1111/j.1438. 8677.2010.00335.x

[36] J.J. Cronin, S.A. Taylor, Measuring service quality: a reexamination and extension, J. Mark. 56 (1992) 55, https://doi.org/10.2307/1252296.

[37] M.K. Brady, J.J. Cronin, R.R. Brand, Performance-only measurement of service quality: a replication and extension, J. Bus. Res. 55 (2002) 17–31, https://doi.org/ 10.1016/S0148-2963(00)00171-5.

[38] C.N. Krishna Naik, S.B. Gantasala, G.V. Prabhakar, Service quality (Servqual) and its effect on customer satisfaction in retailing, Eur. J. Soc. Sci. 16 (2010) 239–251.

[39] T.J. Trull, S.P. Lane, P. Koval, U.W. Ebner-Priemer, Affective dynamics in psychopathology, Emot. Rev. 7 (2015) 355–361, https://doi.org/10.1177/ 1754073915590617

[40] A. Bagnall, J. Lines, J. Hills, A. Bostrom, Time-series classification with COTE: the collective of transformation-based ensembles, IEEE Trans. Knowl. Data Eng. 27 (2015) 2522–2535. https://doi.org/10.1109/TKDE.2015.2416723

[41] R. Xia, C. Zong, S. Li, Ensemble of feature sets and classification algorithms for sentiment classification, Inf. Sci. (Ny). 181 (2011) 1138–1152, https://doi.org/ 10.1016/j.ins.2010.11.023.

[42] W.J. Murdoch, C. Singh, K. Kumbier, R. Abbasi-Asl, B. Yu, Interpretable machine learning: definitions, methods, and applications, Proc. Natl. Acad. Sci. U. S. A. 116 (2019) 22071–22080, https://doi.org/10.1073/pnas.1900654116.

[43] S. Dˇzeroski, B. Zenko, <sup>ˇ</sup> Is combining classifiers with stacking better than selecting the best one? Mach. Learn. 54 (2004) 255–273, https://doi.org/10.1023/B: MACH.0000015881.36452.6e.

[44] A. Fisher, C. Rudin, F. Dominici, All models are wrong, but many are useful: learning a variable’s importance by studying an entire class of prediction models simultaneously, J. Mach. Learn. Res. 20 (2019) 1–81.

[45] D.W. Apley, J. Zhu, Visualizing the effects of predictor variables in black box supervised learning models, J. R. Stat. Soc. Ser. B Stat Methodol. 82 (2020) 1059–1086.

[46] C. Molnar, Interpretable Machine Learning. A Guide for Making Black Box Models Explainable. https://christophm.github.io/interpretable-ml-book, 2020 (accessed July 17, 2023).

[47] A. Ando, R. Masumura, H. Kamivama, S. Kobashikawa, Y. Aono. T. Toda, Customer satisfaction estimation in contact center calls based on a hierarchical multi-task model, IEEE/ACM Trans. Audio Speech Lang. Process. 28 (2020) 715–728, https:// doi.org/10.1109/TASLP.2020.2966857

[48] J. Luque, C. Segura, A. Sanchez, M. Umbert, L.A. Galindo, The role of linguistic and prosodic cues on the prediction of self-reported satisfaction in contact centre phone calls, in: Proc. Annu. Conf. Int. Speech Commun. Assoc. INTERSPEECH, 2017, pp. 2346–2350, https://doi.org/10.21437/Interspeech.2017-424.

[49] F.F. Reichheld, The one number you need to grow, Harv. Bus. Rev. 81 (2003) 46–55.

[50] J. Jung, R. Bapna, A. Gupta, S. Sen, Impact of incentive mechanism in online referral programs: evidence from randomized field experiments. J. Manag, Inf Syst, 38 (2021) 59–81.

[51] G. Phillips-Wren, M. Daly, F. Burstein, Reconciling business intelligence, analytics and decision support systems: more data, deeper insight, Decis. Support. Syst. 146 (2021). 113560.

[52] C.P. Wei, I.T. Chiu, Turning telecommunications call details to churn prediction: a data mining approach, Expert Syst. Appl. 23 (2002) 103–112

[53] J. Zhou, C. Wang, F. Ren, G. Chen, Inferring multi-stage risk for online consumer credit services: an integrated scheme using data augmentation and model enhancement, Decis. Support. Syst. 149 (2021), 113611.

[54] G. Zweig, O. Siohan, G. Saon, B. Ramabhadran, D. Povey, L. Mangu, B. Kingsbury, Automated quality monitoring for call centers using speech and NLP technologies, in: Proc. Hum. Lang. Technol. Conf. NAACL, Companion Vol. Demonstr., 2006, pp. 292–295, https://doi.org/10.3115/1225785.1225796.

[55] S. Stoyanchev, S. Maiti, S. Bangalore, Predicting interaction quality in customer service dialogs, in: Adv. Soc. Interact. with Agents, 2019, pp. 149–159, https://doi. org/10.1007/978-3-319-92108-2\_16.

[56] M.A. Abd El-Fattah, M.I. Dessouky, A.M. Abbas, S.M. Diab, E.S.M. El-Rabaie, W. Al-Wiener filter Int, J. Speech Technol 17 (2014) 53–64

[57] J.A. Haigh, J.S. Mason, Robust voice activity detection using cepstral features, in: Proc. TENCon’93. IEEE Reg. 10 Int. Conf. Comput. Commun. Autom., 1993, pp. 321–324.

[58] A. Mehrjou, R. Hosseini, B.N. Araabi, Improved Bayesian information criterion for mixture model selection, Pattern Recogn. Lett. 69 (2016) 22–27.

[59] M. Deng, T. Meng, J. Cao, S. Wang, J. Zhang, H. Fan, Heart sound classification based on improved MFCC features and convolutional recurrent neural networks, Neural Netw. 130 (2020) 22–32.

[60] O. Abdel-hamid, L. Deng, D. Yu, Exploring convolutional neural network structures and optimization techniques for speech recognition, in: 14th Annu. Conf. Int. Speech Commun. Assoc. (INTERSPEECH 2013). 2013, pp. 3366–3370, doi: 10.1.1.703.648.

[61] S. Banerjee, T. Pedersen, The design, implementation, and use of the ngram statistics package, in: Int. Conf. Intell. Text Process. Comput. Linguist., 2003, pp. 370–381.

[62] M. Phan, A. De Caigny, K. Coussement, A decision support framework to incorporate textual data for early student dropout prediction in higher education Decis, Support. Syst. 168 (2023), 113940.

[63] P. Cong, C. Wang, Z. Ren, H. Wang, Y. Wang, J. Feng, Unsatisfied customer call detection with deep learning, in: 2016 10th Int. Symp. Chinese Spok. Lang. Process., 2016, pp. 1–5.

Yiting Guo is an assistant professor at the School of Economics and Management, Southeast University. She received her doctorate from the School of Economics and Management at Tsinghua University. Her research interest is about the application and social impact of advanced technology in the areas of service, e-commerce, and finance. Sh employs AI-based technologies, such as speech emotion recognition, natural language processing, time-series classification, to solve managerial problems in IS field. Her research also investigates the outcomes of AR and intelligent chatbot applications and generates managerial implications. Her work has been published in IS conferences including International Conference on Information Systems. Conference on Informatior Systems and Technology, INFORMS Annual Meeting, and Annual Meeting of the Academy of Management.

Yilin Li is a post-doctoral fellow at the Guanghua School of Management, Peking Uni versity. She received her doctorate from the School of Economics and Management, Tsinghua University. Her research interests are social network evolution and online con tent innovation, intelligence recommendation in human-machine integration environ ments, and emotional computing in service contexts. Her work has been published in MIS Quarterly and International Conference on Information Systems

De Liu is a Xian Dong Eric Jing Professor of Information and Decision Sciences at the Carlson School of Management, University of Minnesota. He received his Ph.D. from the University of Texas at Austin, and his Master’s and Bachelor’s degrees from Tsinghua University. His recent research interests include gamification. Internet-based auctions and market mechanisms, crowdfunding, and AI /Augmented Reality applications. His research has appeared in leading journals such as MIS Quarterly, Management Science, Information Systems Research, Journal of Marketing, Journal of Market Research, and Production and Operations Management. He is an associator for Journal of Organizational Computing and Electronic Commerce and a former associate editor for Information Systems Research

Sean Xin Xu is a Professor at the School of Economics and Management (SEM), Tsinghu University. His current research interest focuses on digital enablement (particularly business transformation enabled by analytics in education and financial industries) and IT governance. His research has been published in Manggement Science, MIS Ouarterly. Information Systems Research, Journal of MIS, Strategic Management Journal, Contemporary Accounting Research, and Journal of Management Studies, among others. He won the MIS Ouarterly Best Paper Award for 2013. His editorial services include Senior Editor for MIS Ouarterly (2016-present) and Associate Editor for Information Systems Resegrch (2012–2015). Information Systems Research named him “Best Associate Editor” in 2013.
