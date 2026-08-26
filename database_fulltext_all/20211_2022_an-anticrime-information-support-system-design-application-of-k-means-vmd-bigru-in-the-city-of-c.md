---
otero_id: 20211
otero_key: "8X9WAPFX"
title: "An anticrime information support system design: Application of K-means-VMD-BiGRU in the city of Chicago"
authors: "Qing Zhu; Fan Zhang; Shan Liu; Yuze Li"
year: "2022"
journal: "Information & Management"
doi: "10.1016/j.im.2019.103247"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An anticrime information support system design: Application of K-means-VMD-BiGRU in the city of Chicago

Qing Zhu<sup>a,b</sup>, Fan Zhang<sup>a</sup>, Shan Liu<sup>b,</sup>\*, Yuze Li<sup>c</sup>

<sup>a</sup> International Business School, Shaanxi Normal University, Xi’an 710061, China

<sup>b</sup> School of Management, Xi’an Jiaotong University, Xi’an 710049, China

<sup>c</sup> Academy of Mathematics and Systems Science, Chinese Academy of Sciences, Beijing 100190, China

## A R T I C L E I N F O

Keywords: Crime inference Public security Spatial heterogeneity Time-lag efect Machine learning

## A B S T R A C T

The sharp rise in urban crime rates is becoming one of the most important issues of public security, afecting many aspects of social sustainability, such as employment, livelihood, health care, and education. Therefore, it is critical to develop a predictive model capable of identifying areas with high crime intensity and detecting trends of crime occurrence in such areas for the allocation of scarce resources and investment in the prevention and reduction of criminal strategies. This study develops a predictive model based on K-means clustering, signal decomposition technique, and neural networks to identify crime distribution in urban areas and accurately forecast the variation tendency of the number of crimes in each area. We find that the time series of the numbe of crimes in diferent areas show a correlation in the long term, but this long-term efect cannot be reflected in the short period. Therefore, we argue that short-term joint law enforcement has no theoretical basis because data show that spatial heterogeneity and time lag cannot be timely reflected in short-term prediction. By combining the temporal and spatial efects, a high-precision anticrime information support system is designed, which can help the police to implement more targeted crime prevention strategies at the micro level.

## 1. Introduction

With the acceleration of urbanization, urban crime in most cities of the world has become increasingly prominent. A statement released on June 1, 2019, said murders decreased by 7% and shootings reduced by 13% from January 1 to May 31, compared with those in 2018 in the city of Chicago. Unfortunately, in the same weekend, a report was released stating that 52 people were shot. 10 of which were fatal. because of a confluence of factors in Chicago during the weekend on June 1 and 2, 2019 [1]. The increasing urbanization movement is transforming every aspect of the human society and afecting its sustainable development [2–4], which can facilitate economic growth and bring other benefits such as creating additional employment opportunities and absorbing a good number of the surplus rural population [5]. However, it also brings many city management problems such as high force of em ployment, intensifying the public resources, and high crime rates [6]. Every day, people leave their homes to commute to work, shop at supermarkets, study at schools, and relax at restaurants and bars. In such commutes, people never expected to face the threat of death [7]. Therefore, crime identification is focused in this study, which is a major concern in the world: it is not only crucial for the wellbeing of citizens but also essential for the sustainable development of a society [8].

With the gradual increase in crime rates in urban areas, determining how to efectively manage and utilize limited public security resources has become a crucial issue for policymakers and urban management departments [9,10]. The capability of public organizations to collect and store data on crime is increasing, and this increase highlights the importance of developing methods that can efectively analyze the spatial and temporal patterns of such data [11]. By extracting useful pattern information and applying appropriate methods for data analysis, these methods enable public organizations to fully utilize their limited resources and formulate efective tactics to combat crime [12]. The purpose of this paper is to analyze and predict the number of crimes at spatial and temporal scales. To achieve this goal, the paper proposes a daily crime-forecasting model, that can capture high-crime-density areas and predict the number of daily crimes in these areas. Consistent with the crime pattern theory and the routine activity theory, our research results can help to improve the understanding of the connection between criminal occurrences at spatial and temporal scales. The results of the analysis put forward new areas of policy design.

The remainder of this paper is organized as follows: Section 2 discusses the related work and literature. Section 3 describes the architecture of our crime prediction system. Section 4 presents our findings and evaluation of the experiments performed on a real-world dataset. Section 5 provides conclusions and future research.

## 2. Related work

Previous studies related to crime analysis mostly focused on iden tifying crime distribution and capturing time patterns [13]. Extensive criminal justice research has shown that crime event occurrences are not equally distributed across a city [14–16]. The frequency of such occurrences varies from one geographic location to another [17]. The crime pattern theory [18] holds that criminals frequently commit occasional crimes and purposeful violent crimes by taking advantage of the opportunities they encounter, and the places they take as part of their activity space. The reason is that beyond the familiar scope of their activity, criminals will have to seek opportunities to commit crimes and are very likely to face uncertain or unpredictable risks. In addition, crime occurrences can vary across temporal periods, which is often called the seasonality of crime [19]. The routine activity theory [20] contends crime opportunities focus on place and time. The probability of convergence of three conditions are afected by spatial-temporal diferences, including (1) absence of a capable guardian, (2) suitable targets, and (3) motivated ofenders. The three components may be changed by seasonality in several ways.

Spatial-pattern-centric paradigm. Related to the crime pattern theory, many of the existing studies use a space-centric paradigm, and the focus of research is to predict where crime events occur. Given that crime event occurrences are not equally distributed across a city, most studies tend to identify high-crime-intensity areas and forecast crime hotspot areas where hotspot recognition is an application of spatial data clustering [21]. Corcoran et al. [22] presented an approach for crime incident forecasting, which focused on geographical areas of concern that exceed traditional policing boundaries. Instead of using clustering methods, Kianmehr and Alhajj [23] considered location recognition as a data classification task. They used a support vector machine to identify high-crime-intensity areas into crime “hotspots” and lowcrime-intensity areas into crime “coldspots.” Tayebi et al. [24] proposed a probability distribution model of the spatial behavior of criminals. Their experimental results show that criminals often commit crimes in familiar areas rather than venture into unknown areas. Mohler [25] combined short-term and long-term data to develop marked point process hotspot maps for predicting gun violence occurrence in the city of Chicago. Catlett et al. [19] proposed a hybrid forecasting model based on spatial clustering and the autoregressive integrated moving average (ARIMA) model. Such a model detects urban high-crime-intensity areas and then predicts the crime trends in each area. Generally, the identification and prediction of crime-intensity areas can provide valuable information for improving the prevention of public problems.

Temporal-pattern-centric paradigm. Basing on the routine activity theory, numerous researchers study crime datasets from the time dimension. By capturing time patterns from crime datasets, they attempt to analyze the variation tendency of the number of crimes in the future. Gorr et al. [26] used exponential smoothing as their forecasting tool to make monthly crime predictions for police stations. Chandra and Gupta [27] proposed a crime trend prediction model that can detect similar time patterns from diferent crime time series in diferent areas. Peng et al. [28] constructed an ARIMA model based on the property crime data for 50 weeks to make a seven-day-ahead prediction for the number of property crimes. Wang et al. [29] used large-scale point-of interest data in Chicago to estimate the crime rates in predefined neighborhood areas. Cesario at al. [30] used autoregressive models to predict crime in a selected area in Chicago. They analyzed the trends of crime occurrences and provided valuable insights into crime risk factors.

These studies provided detailed spatio-temporal analyses of crimes.

In the spatial analysis of crime, many studies focus on spatial heterogeneity to identify crime hotspots. The mutual influence of criminal activities between detected areas has also been studied in some studies. In the temporal analysis of crime, most studies focus on capturing the temporal patterns of the total number of crimes and fully analyzing the time-lag efect of the crime phenomenon. Basing on the results of these analyses, researchers have proposed various theories of crime, such as the crime pattern theory and the routine activity theory. However, although previous studies have fully analyzed the spatial heterogeneity and time-lag efect of the crime phenomenon, these theoretical results can only provide economical guidance to the government departments at the macro level but cannot provide practical and executable guidance to police departments at the micro level. While the results of these studies give us an idea of the spatial and seasonality distribution of the crime, police patrolling neighborhood still does not know whether the number of crimes will increase in their neighborhood tomorrow, and this situation leaves a huge gap between theoretical progress and police practice. How to implement the existing theory to guide the policing management practice is still a research blank, which focuses on the practical needs of policing activities. On the basis of this requirement, this paper focuses on developing an anticrime information support system that adopts big data analytics methodologies to obtain useful predictive information associated with crime events. Therefore, the contribution of this study is the construction of the bridge between theoretical analysis and policing management practice. This kind of system design allows theoretical achievements to be used in management practice to curb criminal activities at the micro level.

More specifically, in this study, the signal decomposition technique is used to decompose complex and nonstationary crime time series into simple and stationary subseries. The inner patterns captured by this technique are further inputted in the neural network for one-day-ahead prediction. The accuracy of the forecasting model may be increased by introducing the bidirectional neural network into the proposed method in the prediction step. Given that the current state is a basis of future state and reflects historical information, we suppose a bidirectional relationship of time series data. [31]. In addition, crime types are separated into index and nonindex crimes; hence, the patterns of index and nonindex crime occurrences can be analyzed individually.

In this research, the proposed model was applied into the crime data for Chicago, which remains one of the most violent cities in the United States [19]. Many studies such as those by Wang et al. [32], Dugato et al. [33], and Quick et al. [34] assume that hotspot areas are relatively independent when predicting the number of crimes in each region. Thus, we conducted experiments to study the interaction efect between hotspots and determine whether this assumption is realistic. To further analyze model performance, we introduced two traditional criminal prediction models in the literature to evaluate the validity of the proposed method. The analysis results indicate that the proposed model achieves higher accuracy than the algorithm in the literature. The model demonstrates good prediction accuracy and fitting performance in forecasting the number of occurrences of nonindex and index crimes. By accurately predicting the patterns of index and nonindex crime occurrences in crime-dense areas, this model provides guidance to law enforcement and enables them to efectively use limited resources and improve public security.

## 3. Methodology

The crime activities are closely related to the potential dangerous population, which does not necessarily correspond to the citizens in a geographic unit [35]. With a common modeling approach, this study adopts the counts of crime incidents as the dependent variable, which refers to number of crime incidents in a region (i.e., the detected crimedense areas) in diferent time intervals (i.e., one day, one week, one month, and one year). The crime rate inference problem is to estimate the crime counts in one area by using the number of crimes in other regions in the same time interval and taking the features of areas and correlations between areas into consideration. The geographical area used in this study is the crime-dense areas detected by a clustering algorithm, which can automatically trace the shapes of the detected regions without any predefined area divisions.

Before the model is introduced in detail, some notations are pre sented. In the urban area, the modeling for crime counts starts with a bounded and specific two-dimensional area $D \subset R ^ { 2 } :$ , where D represents the urban area. This two-dimensional area D can be separated into N non-overlapping and well-defined sub-regions $d _ { i }$ based on the coordinates proximity of crime occurrence, that ${ \mathrm { i } } s ,$ the detected crimedense areas in this study. The occurrence of crime can be considered as the realization process of a point on the detected crime-dense areas. Therefore the capture process of the crime-dense area is the clustering process of the points on the urban area D. As for the crime location, each crime instance can be denoted by a vector [( , , )]lat lon t , where the $( l a t _ { i } ,$ lon ) represents the points where a crime instance occurs, and the t denotes the time of crime occurrence. lat and lon are the latitude and longitude of the points, respectively, and i is the index of the de tected crime-dense area. Moreover, the crime counts of a certain area i is estimated according to the information of all the other areas. Without losing generality, this paper assumes that crime coun $. y _ { i }$ in one detected crime-dense area is the dependent variable, and the crime count $\{ \boldsymbol { y } _ { j } ,$ $j \in D \}$ in all the areas is used to infer the dependent variable $y _ { i } .$

## 3.1. K-means clustering

In this study, the coordinates of a crime can be divided into diferent sub-areas according to the spatial proximity among coordinates. Clustering algorithm is a typical unsupervised learning algorithm, which can be used to automatically classify the coordinates of a crime into the same sub-area [36,37]. As a prototype-based clustering method [38], K-means clustering algorithm classifies samples into K clusters. By calculating the spatial proximity between each coordinate of crime and the centroid of each cluster, the urban area is classified into several crime-dense sub-areas. Spatial proximity can be calculated by using the Manhattan distance (1-norm distance) or Euclidean distance (2-norm distance). To classify each crime instance into the nearest clustering sub-area, we need to find the specific location of these clustering sub area centers. However, to determine the location of the sub-area center, we must know which crime instances are included in the sub-area. which, in theory, is an NP-Hard problem [39]. Those crime instances are classified into six predetermined sub-areas. The number is determined by calculating the centroid for each clustering sub-area and then classifving each crime instance to the sub-area with the closest centroid. The sum of squares is used as the loss function in K-means clustering algorithm, which is defined as follows:

$$
c (S _ {i}) = \sum_ {r = 1} ^ {| S _ {i} |} \sum_ {s = 1} ^ {| S _ {i} |} [ d [ (l a t _ {r} ^ {i}, l o n _ {r} ^ {i}), (l a t _ {s} ^ {i}, l o n _ {s} ^ {i}) ] ] ^ {2}\tag{1}
$$

where $( l a t _ { r } ^ { i } , l o n _ { r } ^ { i } )$ denotes the coordinate of $r ^ { \mathrm { t h } }$ crime in the city, |S | is the number of crime instances in the city, and $\mathcal { I } [ ( l a t _ { r } ^ { i } , l o n _ { r } ^ { i } ) , ( l a t _ { s } ^ { i } .$ lon, )]<sup>i</sup> is the spatial proximity between ( , )lat lon<sup>i</sup> <sup>i</sup> and ( , )lat lon<sup>i</sup> <sup>i</sup> .

The pseudo-code of the K-means algorithm is as follows [40]:

Step 1. K objects are randomly selected from the original dataset as the centroids.

Step 2. Calculate the distance between each object in the dataset and each centroid, and find the nearest centroid to the object in the dataset. Then, take the nearest centroid as the new center of objects in the dataset.

Step 3. Update the center of each cluster

Step 4. Repeat the above two steps until each centroid remains the same, and exit the loop.

## 3.2. Variational mode decomposition

In general, the performance of a forecasting model depends heavily on the feature representation methods chosen [41]. Before the raw data (crime counts $\{ y _ { j } , j \in D \}$ in all areas) are inputted into the forecasting models, representing the raw data using some data representation methods can enhance the performance of the models to a large extent. As a signal decomposition and estimation method, variational mode decomposition (VMD) is an adaptive, quasi-orthogonal, and completely non-recursive signal processing technique [42]. In this paper, VMD was used to decompose the original 1-D crime count time series $f ( t )$ into Kindependent band-limited discrete sub-series $u _ { k } ,$ which have sparsity properties while reconstructing the original 1-D crime count time series $f ( t )$ [43]. Assuming that each criminal sub-series is band-limited and discrete, the variational framework can be viewed as a process of finding crime sub-series function u (t), by which it can minimize the sum of the estimated bandwidths of criminal sub-series [44]. By this variational framework, we can find a central frequency w tightly encompassed by crime sub-series $u _ { k }$ and then determine the main period of its fluctuation by transforming it from the frequency domain to the time domain.

The automatically iterational and variational framework can be calculated in the following process:

$$
\begin{array}{l} \min _ {\{u _ {k} \}, \{w _ {k} \}} \{\sum_ {k} \| \partial_ {t} [ (\delta (t) + \frac {j}{\pi t}) \otimes u _ {k} (t) ] e ^ {- j w _ {k} t} \| _ {2} ^ {2} \}, \\ s. t. \sum_ {k} u _ {k} = f (t) \end{array}\tag{2}
$$

where $\{ u _ { k } \} = \{ u _ { 1 } , . . . , u _ { k } \}$ and $\{ w _ { k } \} = \{ w _ { 1 } , . . . , w _ { k } \}$ are the criminal sub-series and their corresponding center frequencies, and $\begin{array} { r } { \sum _ { k } = \sum _ { k = 1 } ^ { K } , f ( t ) } \end{array}$ represents the original crime counts $\{ y _ { j } , \ j \in D , \ j \neq i \}$ , K denotes the number of subsequences to be decomposed, $u _ { k }$ denotes the $k ^ { \mathrm { t h } }$ crime sub-series, ⊗ denotes the convolution operator, and $\delta ( t )$ represents the Dirac distribution.

## 3.3. Bidirectional gated recurrent unit

Based on the assumption of the data-generating process, previous criminal studies considered the linear additive relationship between the number of crimes and predictors. In a data-driven manner. neural networks technology is flexible in explaining nonlinearity in the number of crimes and predictors. This paper utilizes the bidirectional recurrent neural network (BiRNN) proposed by Schuster and Paliwal [45]. Unlike traditional recurrent neural networks (RNN). BiRNN uses forward and backward information in the data. By replacing RNN cells with gated recurrent unit (GRU) cells, the network is adapted further to accurately model temporal sequences and long-range dependencies [46]. Bidirectional GRU (BiGRU) contains two hidden layers. One layer is used for the forward direction, and the other for the backward direction, which can use forward and backward information in the data. It connects the two separate and contrasting-direction hidden layers to the same output layer. In this study, we assume the time series of the number of crimes has a two-way relationsh ${ \mathrm { i p } } ,$ because the current state of crime in cities is the reflection of historical information and the basis of future state of crime [31]. Using this structure, BiGRU can process and obtain criminal information from the past and future states to make accurate predictions. The basic structure of BiGRU is illustrated in Fig. A.12.

As illustrated in Fig. A.12, a regular GRU cell consists of only two gates, namely, update gate $u _ { t }$ and reset gate $r _ { t ^ { * } }$ The update gate $u _ { t }$ determines the degree of input information transferred into the current state. The greater its value, the more input information is transferred into the current state. The reset gate $r _ { t }$ determines the degree of information reserved from the previous status information. The greater its value ${ \mathrm { i } } s ,$ the less information is reserved from previous status information. x represents the input data at timestamp $t ,$ and $h _ { t }$ indicates the hidden state at timestamp t. σ, shown in the picture, is the Sigmiod function and tanh denotes the tanh function. $u _ { t }$ and $r _ { t }$ are computed as shown in Eqs. (A.1)–(A.5).

![](/api/attachments/8X9WAPFX/fulltext/images/5b6d42d1faf9e13ba093db92e17cdb4227d2544eb971a1cb05c54ef07c18ebd7.jpg)  
Fig. 1. Architecture of the proposed model.

## 3.4. Prediction model architecture

Fig. 1 illustrates the architecture of the proposed prediction model, which consists of three steps. First, spatial clustering is conducted. Given that criminal acts are not evenly distributed in administrative areas, a large number of studies have utilized a clustering approach to efectively predict the high-crime-intensity areas [47]. This paper utilizes K-means clustering to conduct spatial analysis and identify crimedense areas. After the crime-dense areas are found, each crime instance is assigned to a specific area on the basis of their respective x- and ycoordinates. Thus, the daily overall occurrence, index crime occur rence, and nonindex crime occurrence for each region are obtained Second, we decompose the target variable into stationarity and timedependent sub-series. In the model, the time series of the number of index and nonindex crime occurrences of every area are selected as basic input variables and target variables. Then, we select to decompose forecasting target variables to capture the inner patterns. Third, the model uses the variables above as input in a seven-day window from timestamp t − 6 to t and predicts the number of occurrences for index and nonindex crimes in the particular area in timestamp t + 1. The efects of diferent scales of measurement are removed by normalizing the data in the range of 0–1.

The BiGRU network in the model is a five-layer model consisting of input and output layers, forward- and backward- direction hidden layers, and a fully connected layer. The numbers of neurons are all set to be the same as the dimension of the input data besides the fully connected layer. The number of neurons in the fully connected layer is set to 1. We use Adam optimizer to train the model, where the learning rate is set to 0.01.

## 4. Data and model

## 4.1. Data description

Data used in this paper were provided by Plenar.io (http://www. plenar.io). In this platform, data search and exploration is publicly available. The crime data were obtained from the City of Chicago Crimes 2001 to present dataset. It contains crime description from policeman records from January 1, 2011 to January 1, 2018. For our analysis, we collected all crime events from a total of 2557 days. The total number of crime instances used in the dataset is 1,048,516 during the 7 years, which is on average 149,788 crime incidents per year.

Out of the total 22 attributes contained in the raw dataset, 4 attributes were selected to form our dataset, namely, date, FBI code, x-coordinate, and y-coordinate. Table 1 illustrates the examples of raw data used in this study. By calculating the number of crimes in daily interval, the raw dataset was reorganized as a time series. According to the Uniform Crime Reporting (UCR) program (https://www.fbi.gov/ services/cjis/ucr) and the given FBI code in the raw dataset, each crime instance is classified further as either index crime or nonindex crime. According to UCR, index crimes include two categories, namely, property and violent crimes, and are labeled with an attribute value of 1 in this paper. Property crimes contain arson, burglary larceny-theft, and motor vehicle theft, whereas violent crimes include aggravated assault, forcible rape, murder, and robbery. Nonindex crimes are less serious crimes labeled with an attribute value of $^ { 2 , }$ where the following categories are tracked: simple assault, curfew offenses and loitering, embezzlement, forgery and counterfeiting, disorderly conduct, and driving under the influence. Compared with index crime, nonindex crimes are more occasional and random.

Figs. 2 and 3 present a general view of the collected crime data. All the observed crime data are drawn according to the observation time. Figs. 2 and 3 show several interesting features. First, the number of crimes in the collection period shows an obvious downward trend. Second, the data show a seasonal pattern that repeats every year; specifically, the number of crimes increases from the beginning to the middle of the year, peaks during summertime, and then decreases in the latter half of the year. Fig. 2 clearly presents the seasonality hidden in the data. Third, although crime occurrences appear to be less frequent in winter, a sudden peak-and-dip pattern is repeated around the late December and early January.

The crime occurrences are further divided by crime type. Fig. 4 shows the time plot of all nonindex and index crimes. On the one hand, index and nonindex crimes have decreased during the collected time period, as evidenced by the clear decreasing trend in the data. On the other hand, while the index crime occurrence displays the same repeating seasonal pattern as the overall crime occurrence, in which the number of crimes has a gradual increase from January to June but a gradual decrease from July to December, nonindex crime occurrence shows a more random pattern.

Table 1  
Examples of raw data used in this study.

<table><tr><td>Date</td><td>Primary type</td><td>FBI code</td><td>X-coordinate</td><td>Y-coordinate</td></tr><tr><td>2011/1/1 0:00</td><td>deceptive practice</td><td>12</td><td>1,168,742</td><td>1,850,871</td></tr><tr><td>2011/1/1 0:00</td><td>offense involving children</td><td>20</td><td>1,169,853</td><td>1,840,194</td></tr><tr><td>2011/1/1 0:00</td><td>burglary</td><td>5</td><td>1,182,559</td><td>1,867,055</td></tr><tr><td>2011/1/1 0:00</td><td>sex offense</td><td>17</td><td>1,148,213</td><td>1,898,018</td></tr></table>

![](/api/attachments/8X9WAPFX/fulltext/images/edf6240f8bdbefba2545e63c4e1fd92986fdf82e4f5f075efc5c4526d2c16235.jpg)  
Fig. 2. Number of crimes vs. time.

Number of crimes by month of the year  
![](/api/attachments/8X9WAPFX/fulltext/images/dc990ccc697399bf31c36b767b1d7ee3d721455f74168d951155c56d83d9c173.jpg)  
Fig. 3. Distribution by month.

Table 2 shows the common statistics for the time series of the overall number of crimes, nonindex and index crimes, as well as the augmented Dickey-Fuller (ADF) and Jarque-Bera test results. The results of the ADF test show that the overall number of crimes and index crimes is unstationary, with ADF test statistic of −2.55 and −2.76, respectively, both of which exceed the 5% critical value, that is, −2.86. However, the nonindex crime is stationary, with an ADF test statistic of −3.26. The Jarque-Bera test indicates rejections for the overall nor mality assumption, combining nonindex, and index crimes. Their distributions also reveal non-zero skewness and high kurtosis, which indicate that their distributions have leptokurtosis and are fat-tailed.

## 4.2. Rolling window and evaluation indicator

The prediction period for the model is from December 14, 2016, to January 1, 2018, which includes 383 samples. As shown in Fig. 5, a rolling period of 90 days is used to train the model. The model then uses the data from a seven-day window to generate a one-day forward prediction.

To evaluate the prediction performance of the BiGRU models, mean square error (MSE) is selected as the loss function. The MSE function is calculated using the following equation:

$$
\mathrm{MSE} = \frac {1}{N} \sum_ {t = 1} ^ {N} (\hat {X} (t) - X (t)) ^ {2}\tag{3}
$$

In addition, three indices are selected to assess the goodness of fit of the model, namely, coeficient of determination $( R ^ { 2 } ) _ { ; }$ , root MSE (RMSE), and mean absolute error (MAE). The equations for calculating these indices are as follows:

$$
\mathrm{R} ^ {2} = 1 - \frac {\sum_ {t = 1} ^ {N} (\hat {X} _ {t} - X _ {t}) ^ {2}}{\sum_ {t = 1} ^ {N} (\bar {X} _ {t} - X _ {t}) ^ {2}}\tag{4}
$$

$$
\mathrm{RMSE} = \sqrt {\frac {1}{N} \sum_ {t = 1} ^ {N} (\hat {X} _ {t} - X _ {t}) ^ {2}}\tag{5}
$$

$$
\mathrm{MAE} = \frac {1}{N} \sum_ {t = 1} ^ {N} | \hat {X} _ {t} - X _ {t} |\tag{6}
$$

Directional accuracy (DA) is also introduced to assess the proposed model's predictability for crime trends. If the model predicts that the number of crime occurrences in a region will increase (decrease) the next day and the actual number does increase (decrease), then the model correctly predicts the trend. On the contrary, if the model predicts that the number of crime occurrences in a region will increase (decrease) the next day but the actual number decreases (increases), then the model fails to predict the trend. Therefore, the greater the directional accuracy is, the better the crime trend predictability of the model is. Directional accuracy is calculated as follows:

![](/api/attachments/8X9WAPFX/fulltext/images/3aa298c6b3f4aabf53d5b97ca858d0e11883df2743760699cffc8f2d2c2db8bb.jpg)  
Fig. 4. Time plot of index and nonindex crimes.

Table 2  
Descriptive statistics for the number of crimes.

<table><tr><td></td><td>Mean</td><td>Max</td><td>Min</td><td>Std. Dev.</td><td>Skewness</td><td>Kurtosis</td><td>Jarque-Bera</td><td>ADF</td></tr><tr><td>All</td><td>410.0665</td><td>776</td><td>162</td><td>69.83152</td><td>0.380185</td><td>3.470618</td><td>85.1955</td><td>-2.55003</td></tr><tr><td>Index crime</td><td>235.5851</td><td>407</td><td>93</td><td>43.94623</td><td>0.332544</td><td>3.037128</td><td>47.27461</td><td>-2.76575</td></tr><tr><td>Nonindex crime</td><td>143.9628</td><td>311</td><td>44</td><td>28.19430</td><td>0.410509</td><td>4.201694</td><td>225.6702</td><td>-3.26372</td></tr></table>

![](/api/attachments/8X9WAPFX/fulltext/images/3b951d45c55c6037f7296e45c10ecd765450187166ca232cb7ff62655c82b50d.jpg)  
Fig. 5. Rolling window schematic for the continuous training and testing dataset during the entire sample period.

![](/api/attachments/8X9WAPFX/fulltext/images/5b35d870fa9a2c9aa433b91aeb1b93ae35406cf837f2d8644e77aca29e4557e3.jpg)  
Fig. 6. Comparison of clustered crime regions and map of Chicago.

$$
Z _ {t} = \left\{ \begin{array}{l l} 1, & (X _ {t} - X _ {t - 1}) \cdot (\hat {X} _ {t} - X _ {t - 1}) \geq 0 \\ 0, & (X _ {t} - X _ {t - 1}) \cdot (\hat {X} _ {t} - X _ {t - 1}) <   0 \end{array} \right.\tag{7}
$$

$$
\mathrm{DA} = \frac {\sum_ {i = 1} ^ {N} Z _ {t}}{N}\tag{8}
$$

In Eqs. $( 7 )$ and (8), $\hat { X } _ { t }$ and $X _ { t }$ are the forecasted and true values at time $t ,$ respectively; ${ \bar { X } } _ { t }$ denotes the mean of the actual value; and N denotes the total number of samples.

## 5. Results and discussion

To assess the prediction performance and validity of the proposed model, extensive analyses were carried out based on the real crime dataset collected from Chicago. The goal of the analysis was to identify automatically the most crime-dense areas and detect the patterns of crime occurrences in these areas, thus allowing the model to make daily predictions on the number of two types of crime occurrences in each area. For reading convenience and easy comprehension, the rest of this section is organized as follows: Section 5.1 shows the spatial clustering results and crime area detection results. Section 5.2 presents the VMD decomposition results, and the corresponding analysis and discussion.

Section 5.3 shows the correlation analysis between diferent identified areas. Section 5.4 shows the model's prediction results for diferent crime types. The structure of this section is consistent with the model architecture proposed in Section 3.4.

## 5.1. Spatial clustering

In this study, K-means clustering was used to conduct spatial clustering and identify the crime-dense areas. The Davies-Bouldin Index (DBI) [48] and the Silhouette Index (SI) [49] were taken as the measurement criteria. To assess spatial features, we evaluated the number of clusters from 1 to 24. The K-means spatial clustering algorithm with six groups performs best according to DBI and SI. As a result, six crime areas were selected for the dataset; these areas were labeled in Fig. 6 (Image copyright belongs to Google Maps, http://www.google.cn/ maps/.)

The numbers of crime occurrences for each clustered crime areas are shown in Table 3. Of the 6 clustered areas, areas 5, 3, and 2 had high crime intensities. These three areas contained almost 70% of the total crimes, accounting for 25%, 21%, and 21% of the total crimes, respectively. As a result, these regions were identified as crime hotspots. They will be analyzed in detail in the following sections.

Table 3  
Crime occurrences by area.

<table><tr><td>Area</td><td>Overall number</td><td>% of overall crimes</td><td>Type</td><td>Number of crimes</td><td>% of classified crimes</td></tr><tr><td rowspan="2">Area 1</td><td rowspan="2">160,900</td><td rowspan="2">15.31%</td><td>Index crime</td><td>112,857</td><td>10.74%</td></tr><tr><td>Nonindex crime</td><td>48,043</td><td>4.57%</td></tr><tr><td rowspan="2">Area 2</td><td rowspan="2">216,222</td><td rowspan="2">20.57%</td><td>Index crime</td><td>134,442</td><td>12.79%</td></tr><tr><td>Nonindex crime</td><td>81,780</td><td>7.78%</td></tr><tr><td rowspan="2">Area 3</td><td rowspan="2">216,923</td><td rowspan="2">20.64%</td><td>Index crime</td><td>119,503</td><td>11.37%</td></tr><tr><td>Nonindex crime</td><td>97,420</td><td>9.27%</td></tr><tr><td rowspan="2">Area 4</td><td rowspan="2">121,971</td><td rowspan="2">11.60%</td><td>Index crime</td><td>80,306</td><td>7.64%</td></tr><tr><td>Nonindex crime</td><td>41,665</td><td>3.96%</td></tr><tr><td rowspan="2">Area 5</td><td rowspan="2">257,022</td><td rowspan="2">24.45%</td><td>Index crime</td><td>157,828</td><td>15.02%</td></tr><tr><td>Nonindex crime</td><td>99,194</td><td>9.44%</td></tr><tr><td rowspan="2">Area 6</td><td rowspan="2">78,036</td><td rowspan="2">7.42%</td><td>Index crime</td><td>47,742</td><td>4.54%</td></tr><tr><td>Nonindex crime</td><td>30,294</td><td>2.88%</td></tr></table>

## 5.2. Analysis of VMD decomposition results

After clustering by K-means, we analyzed the time series for the discovered dense region. With the index crime in area 5 taken as an example, Fig. 8 shows that the number of index crimes in area 5 shows decreasing trend and seasonal pattern. To better capture these features and make more accurate predictions, VMD was introduced to decompose the number of index crimes in area 5. The time series in area 5 was clearly decomposed into 11 sub-series, ranging from low to high fre quency. Each sub-series denoted a type of volatility element hidden in the time series. In Fig. 7, the 11 sub-series are labeled as M1, M2, …, M11. M1 had the lowest-frequency signal from the subsequences, reflecting decreasing trend and seasonal pattern, and M11 was the highest-frequency sub-series, reflecting a random walk feature in the number of index crimes in area 5.

Moreover, the management implications of long-term trends and seasonal patterns of the number of crimes are further analyzed from the VMD decomposition results. The perception of public security is in fact divided often into two perspectives according to the social body differences. On the one hand, the city management departments assess the level of public security through the variation tendency of the overall number of crimes in the long-term period, which demonstrates a de creasing trend in the long term. Therefore, these departments tend to think that public security is improving with time. On the other hand, individuals in the society tend to assess the level of public security in a relatively short-term period through their own experiences. Furthermore, individuals are often very sensitive to the deterioration of public security and will not have a timely perception of its improvement. As a result, because of seasonal patterns manifesting with in creasing number of crimes from the beginning to the middle of the year, peaking during summertime, and then decreasing in the latter half of the year, individuals in the society will think that public security situation is deteriorating each year. This belief will lead to the contradiction between public service providers and recipients on the evaluation of public security quality and law enforcement efectiveness. Therefore, although law enforcement has been able to reduce the number of crime occurrences in each fiscal year from a long-term perspective, the repeating short-term crime patterns during the years show that its short-term crime prevention tactics constantly fluctuate between being efective and inefective during seasonal periods. This finding shows that their crime-fighting strategies have not been innovated. The contradiction requires the public security department to adopt innovative approaches to maintain a long-term downward trend in crime while smoothing seasonal fluctuations.

![](/api/attachments/8X9WAPFX/fulltext/images/4e8806c8c20a723f6c2c64595cf660bc409dcd3346c74dd6c87c612bfd65d144.jpg)  
Fig. 7. VMD decomposition result.

## 5.3. Correlation analysis between identified regions

To investigate the efects of spatial dependency between identified crime areas in the selected dataset, we performed tests for correlation and three diferent scenario simulations for the target area. To analyze the correlation between the time series of the number of crimes in diferent areas, we used Pearson correlation coeficient (Pearson's r) to measure the degree of correlation between sequences. This correlation coeficient is commonly used to reflect the degree of linear correlation between two random variables. Spearman's rank correlation coeficient (Spearman's r) was then introduced to determine whether the trends in diferent variables tend to be consistent with time. Table 4 illustrates the results for the Pearson's r and Spearman's r tests. The results in dicate an obvious linear dependence between each region and any other regions under 1% confidence interval. Furthermore, variation tendencies in the number of crimes in diferent areas tend to show consistency with time.

Fluctuation graph for the decomposition results  
![](/api/attachments/8X9WAPFX/fulltext/images/67eb54e22e2d5055eb3c9010d15ebf0235bff026011e2631706f386f2d99e7a1.jpg)  
Fig. 8. Fluctuation graph for the decomposition result.

After analyzing the correlation between the sequences, we further investigated whether the correlation has a positive efect on the oneday-ahead prediction for the crime counts committed in target area. Therefore, we selected a target area and predicted the crime counts committed in target area under three scenarios to analyze the impact of correlation on the forecasting results.

Scenario 1. Series from all areas are used to predict the crime occurrences committed in the target area. Therefore, the input variables contain the series of the number of crimes in all areas and the sub-series from VMD decomposition in the target area.

Scenario 2. The series from the target area and its adjacent areas are used to predict the crime occurrences in the target area. Similarly, the input variables contain the series of the number of crimes in its adjacent areas, in addition to the number of crime occurrences in the target area and its sub-series from VMD decom position.

Scenario 3. Only the time series from the target area is used to predict the crime occurrences. The input variables contain the crime counts in the target area and its sub-series from VMD decomposition.

The simulation was tested under the diferent scenarios mentioned above, and the results for area 5, which is the most crime-dense area, are shown in Table 5. Area 5 with all other regions represents scenario 1; Area 5 with adjacent regions represents scenario 2, where the adjacent areas are areas 1, 2, and 3; and Area 5 itself represents scenario 3.

Taking area 5 as the target region, we studied the influence of dif ferent scopes on the prediction for the target area by using the analysis method from the whole to the part and to the target. When taking the number of crime occurrences in all areas as the input for BiGRU, the R<sup>2</sup> value for Area 5 with all other regions is 0.94923, and the DA value i 93.47%. Furthermore, the values of MSE, RMSE, and MAE are 0.00015, 0.01237, and 0.00978, respectively. However, after the remote areas are removed, the results of Area 5 with adjacent regions show a slight improvement for the measurement criteria, with $R ^ { 2 }$ increasing from 0.94923 to 0.95134. In addition. the MSE, RMSE, and MAE decreased by 5.6%, 2.1%, and 3.1%, respectively. These results indicate that with the reduction of spatial scope, the accuracy of the prediction for the number of crime events in the target area increases.

Table 5  
Results comparison for area 5.

<table><tr><td>Area</td><td> $R^{2}$ </td><td>MSE</td><td>RMSE</td><td>MAE</td><td>DA</td></tr><tr><td>Area 5 with all other regions</td><td>0.94923</td><td>0.00036</td><td>0.01908</td><td>0.01576</td><td>0.93472</td></tr><tr><td>Area 5 with adjacent regions</td><td>0.95134</td><td>0.00034</td><td>0.01867</td><td>0.01528</td><td>0.93211</td></tr><tr><td>Area 5 itself</td><td>0.97865</td><td>0.00015</td><td>0.01237</td><td>0.00978</td><td>0.95039</td></tr></table>

A further comparison between the results of Area 5 with adjacent regions and Area 5 itself shows that Area 5 itself evidently shows improvement in performance. $R ^ { 2 }$ increased by 3.0%, while the MSE, RMSE, and MAE decreased by 55.9%, 33.7%, and 37.9%, respectively, indicating a significant improvement in the fitting performance. The DA value of the model also increased by 2%, indicating that using the data from Area 5 itself to predict the number of crime occurrences in the area is more accurate. Therefore, reducing the spatial scope down to the target area clearly improves forecasting results.

The analyzed results reveal that although the time series of the number of crimes in diferent areas show a correlation as a whole, this dependency cannot improve the accuracy of one-day-ahead prediction in each area. The primary cause is the correlation between sequences in diferent areas being mainly reflected in the long term. Furthermore, the experimental result show that a long-term efect cannot be reflected in the short-term prediction. That is, in the short term like a day, change in the number of crimes caused by the adjustment of public security policy in other areas will not have an obvious impact on the security status of the target region. This outcome shows that from a short-term perspective, the efectiveness of public security cooperation between areas is limited, and additional synergies that improve the overall public security state are almost impossible to observe. Furthermore, the short-term efect of public security policies in each area can be specifically improved by taking diferent measures in response to the characteristics of the diferent areas.

Why is there such a long-term correlation, but it cannot be reflected in the short term? Where do long-term correlations stem from? Wang et al. [29] estimated the annual crime rate in one community using the crime rate of other communities by considering the features of regions correlations. Although previous researchers (like Yong et al. [11], Loefer and Flaxman [13], and Chandra and Gupta [27]) have revealed the existence of long-term correlations, the sources of long-term correlations have not been considered. We have discussed several possible sources of long-term correlation in this work. We suppose that the longterm correlation of the identified areas represented by the time series may come from the following aspects. First, the financial support of the urban management department for various areas in a city is usually balanced. For example, every police station in a city often receives the same amount of financial support. Under the same resource constraints, the public security policies of diferent areas often produce similar effects. Second, public security organizations of various areas in a city often have long-term information exchanges, staf scheduling, and longterm coordination mechanism. Third, when public security organizations of one area take vigorous action to combat crimes, criminals will choose to move to other regions to avoid punishment. Owing to the increasing costs of crime, the negative spillover efect will form, and areas with high crime costs will export crimes to other areas.

Table 4  
Correlation test between identified areas.

<table><tr><td colspan="2"></td><td>Area 1</td><td>Area 2</td><td>Area 3</td><td>Area 4</td><td>Area 5</td><td>Area 6</td></tr><tr><td rowspan="2">Area 1</td><td>Pearson&#x27;s r</td><td>1.000</td><td>0.372**</td><td>0.339**</td><td>0.446**</td><td>0.372**</td><td>0.317**</td></tr><tr><td>Spearman&#x27;s r</td><td>1.000</td><td>0.339**</td><td>0.300**</td><td>0.435**</td><td>0.339**</td><td>0.290**</td></tr><tr><td rowspan="2">Area 2</td><td>Pearson&#x27;s r</td><td>0.372**</td><td>1.000</td><td>0.664**</td><td>0.583**</td><td>0.724**</td><td>0.515**</td></tr><tr><td>Spearman&#x27;s r</td><td>0.339**</td><td>1.000</td><td>0.654**</td><td>0.571**</td><td>0.707**</td><td>0.487**</td></tr><tr><td rowspan="2">Area 3</td><td>Pearson&#x27;s r</td><td>0.339**</td><td>0.664**</td><td>1.000</td><td>0.550**</td><td>0.696**</td><td>0.479**</td></tr><tr><td>Spearman&#x27;s r</td><td>0.300**</td><td>0.654**</td><td>1.000</td><td>0.527**</td><td>0.688**</td><td>0.455**</td></tr><tr><td rowspan="2">Area 4</td><td>Pearson&#x27;s r</td><td>0.446**</td><td>0.583**</td><td>0.550**</td><td>1.000</td><td>0.597**</td><td>0.461**</td></tr><tr><td>Spearman&#x27;s r</td><td>0.435**</td><td>0.571**</td><td>0.527**</td><td>1.000</td><td>0.581**</td><td>0.447**</td></tr><tr><td rowspan="2">Area 5</td><td>Pearson&#x27;s r</td><td>0.372**</td><td>0.724**</td><td>0.696**</td><td>0.597**</td><td>1.000</td><td>0.534**</td></tr><tr><td>Spearman&#x27;s r</td><td>0.339**</td><td>0.707**</td><td>0.688**</td><td>0.581**</td><td>1.000</td><td>0.505**</td></tr><tr><td rowspan="2">Area 6</td><td>Pearson&#x27;s r</td><td>0.317**</td><td>0.515**</td><td>0.479**</td><td>0.461**</td><td>0.534**</td><td>1.000</td></tr><tr><td>Spearman&#x27;s r</td><td>0.290**</td><td>0.487**</td><td>0.455**</td><td>0.447**</td><td>0.505**</td><td>1.000</td></tr></table>

\*\* Indicates that the correlation is significant under 1% confidence interval.

The long- and short- term relationship diferences between crime dense areas show that the synergistic efect produced by the interaction between diferent regions is a long-term mechanism that needs time to accumulate. In fact, to realize the balanced supply of basic public services guided by the principle of fairness is the core ideology formed in the process of social development of all countries in the world. However, this ideology is easy to be absolute in practice, and the equal public security services enjoyed by every citizen do not necessarily mean equal public security resources supplies among diferent areas in a city. The short-term relative independence between diferent areas indicates that it is ineficient to adopt the same public security resource supply strategy for each area in a city. Moreover, the long-term correlation among areas in a city indicates that if the public security of a certain area in a city is in a state of low eficiency, other areas in the city will be afected by the negative efects caused by this state of low efficiency in the long period. Therefore, the optimization of the resource supply of urban areas at the micro level can improve the public security status of all areas in the short period and produce regional synergies in the long term and can enhance the public security situation of a city as a whole.

## 5.4. Prediction of the number of crime events in hotspot areas

After the mutual influence among crime-dense areas is analyzed, the proposed model is further used to predict the daily number of crime events for index and nonindex crimes in hotspots and examine the temporal distribution of diferent crime types by inputting the time series from the target area only. The prediction results for the three most crime-dense areas (areas 5, 3, and 2) are shown in Table 6. The model displays satisfactory fitting performance for diferent areas and types of crimes, yielding good results in $R ^ { 2 }$ , MSE, RMSE, and MAE. The $R ^ { 2 }$ values for index and nonindex crime prediction in each crime-dense area are greater than 0.96. When the performances on both crime types in each crime-dense area are averaged, the $R ^ { 2 }$ values for areas 5, 3, and 2 are 0.981, 0.986, and 0.985, respectively. In addition, the values of MSE, RMSE, and MAE in all three areas are less than 0.0002, 0.039, and 0.012, respectively, and the DA values of the three areas are all greater than 90%. The fitting results for the number of crimes in each crimedense area are presented in Figs. 9–11, which indicate the fitting performance for index and nonindex crimes in hotspot area is almost the same.

To compare our prediction results, some similar studies are referenced. Catlett et al. [19] collected all 1,897,682 crime events in the city of Chicago for a 16-year period from January 2001 to December 2016. On the basis of the crime dataset of Chicago, they constructed a predictive model by integrating a density-based clustering algorithm and the Seasonal ARIMA. The average MAE of one-year-ahead prediction for the three crime-dense areas in Chicago are 30.20, 14.47, and 11.15, respectively. In comparison, our one-day-ahead forecasting model displayed a more precise prediction horizon and the observable fitting performance has significant increase in terms of MAE. The result is mainly attributed to the following two aspects. In the first aspect, they used the traditional linear prediction method, which has poor fit performance compared with the neural networks, and in the second aspect, in the absence of spatial correlation analysis on a more precise time scale, an underlying assumption in some researches like Peng et al. [28], Catlett et al. [19] and Cesario et al. [30] is that there is no spatial correlation between the crime-dense areas. Another interesting research was conducted by Wang et al. [29], which studied the problem of crime rate inference of communities. By considering the characteristics of the region and the correlation between regions, they use the crime data in relative communities to estimate the annual crime rate of the target community. Through the negative binomial regression method, the average relative error value of the annual crime rate forecast for each region is approximately 0.25. Their research reveals the long-term correlations of crime numbers in diferent regions. However, our experimental results show that a long-term correlation exists in the crime-dense areas while this long-term relationship cannot be reflected in the short-term prediction.

Table 6  
Results of the fitting performance.

<table><tr><td>Area</td><td>Type</td><td> $R^2$ </td><td>MSE</td><td>RMSE</td><td>MAE</td><td>DA</td></tr><tr><td rowspan="2">Area 5</td><td>Index crime</td><td>0.98148</td><td>0.00018</td><td>0.01338</td><td>0.01070</td><td>0.93211</td></tr><tr><td>Nonindex crime</td><td>0.97910</td><td>0.00020</td><td>0.01425</td><td>0.01121</td><td>0.95561</td></tr><tr><td rowspan="2">Area 3</td><td>Index crime</td><td>0.98676</td><td>0.00014</td><td>0.01186</td><td>0.00957</td><td>0.95561</td></tr><tr><td>Nonindex crime</td><td>0.98627</td><td>0.00011</td><td>0.01094</td><td>0.00849</td><td>0.96083</td></tr><tr><td rowspan="2">Area 2</td><td>Index crime</td><td>0.98542</td><td>0.00015</td><td>0.03836</td><td>0.00990</td><td>0.96083</td></tr><tr><td>Nonindex crime</td><td>0.97573</td><td>0.00020</td><td>0.01416</td><td>0.01135</td><td>0.90861</td></tr></table>

The proposed model's high fitting performance and directional accuracy in each crime region indicate its capability to accurately predict the short-period trend of the number of crime occurrences in diferent crime areas. Using the prediction results from the model, city management can plan and develop crime-prevention tactics in advance to counter the peak crime time periods. If the model predicts an increasing crime trend in an area, public resources can be redirected to this area in advance to prevent crimes from occurring. By contrast, if the model predicts a decreasing crime trend in the area, public resources can be redirected temporarily to other areas. By using the accurate prediction results from the model, instead of waiting for crimes to occur and responding to them, law enforcement can anticipate diferent crime occurrences in diferent regions and redistribute resources preemptively, thus efectively preventing crimes from occurring. The prediction results can also be used as guidance for city management during resource readjustment, thus achieving optimization on a micro-level without a great level of financial cost.

In addition, by shifting resource focuses based on the trends of index and nonindex crime occurrences in each area, law enforcement can efectively minimize the negative social impacts of all crimes. Index and nonindex crimes have diferent levels of social impact. Index crimes are more serious crimes, such as homicide, robbery, and aggravated assault, and have relatively larger negative impacts than do nonindex crimes. Therefore, index crimes require more law enforcement resources to combat. Conversely, nonindex crimes relatively mild, such as simple assault, vandalism, and drug abuse, and have relatively smaller nega tive impacts than do index crimes. Therefore, nonindex crimes require less law enforcement resources. The proposed model can accurately predict the number of occurrences for index and nonindex crimes in each crime area. The 24-hour-ahead forecasting proposed in this study allows law enforcement to redistribute resources and shift policing focus efectively. On the basis of the prediction results of the proposed model, individuals can likewise avoid sufering losses of life and property by knowing possible dangers in advance.

## 6. Conclusions

This paper presented an algorithm based on K-means clustering, signal decomposition technique, and neural network models for spatiotemporal crime inference. The algorithm can detect high-crime-intensity areas in urban regions and accurately predict the variation tendency of the number of crimes in each area. From the experimental results, several concrete conclusions were drawn. (i) The diference in

![](/api/attachments/8X9WAPFX/fulltext/images/edfc581f19495efd93156b384e83f2ee2efc8ced9397a73dbec44a07dc4f7c8f.jpg)  
Fig. 9. Prediction results of index and nonindex crimes in area 5.

![](/api/attachments/8X9WAPFX/fulltext/images/c62ac02fcb86c26209b4a6bac82b9bf68d40010b674bf3110b50768d45a8a2d3.jpg)  
Fig. 10. Prediction results of index and nonindex crimes in area 3.

![](/api/attachments/8X9WAPFX/fulltext/images/676e129aae88339095efbb0a60f2268a48179d37801f6e88b8e4bcff8b926f4a.jpg)  
Fig. 11. Prediction results of index and nonindex crimes in area 2.

the long-term trend and the seasonal pattern of the number of crimes will lead to inconsistency in policy objectives between the macro policy of public security and micro management policy of curbing crimes. This finding reveals that the public security department should adopt macrolevel management strategies to optimize resource distribution and maintain a long-term downward trend in the number of crimes and that community public security organizations should take measures to smoothen seasonal fluctuations in their districts. (ii) Although the time series of the number of crimes in diferent areas show a correlation in the long term, the long-term efect cannot be reflected in the short term. Therefore, while maintaining long-term links, law enforcement in each area of a city should take targeted measures to combat criminal activities according to the characteristics of the crime in the area itself. The short-term targeted anticrime actions should become the long-term behavior pattern of each region. In other words, if the aim is to clean up crime activities in the city in the long term, joint enforcement action among areas is not recommended.

The contribution of this paper is the construction of the bridge between the theoretical achievements and the policing management practice. By combining theoretical achievements of crime with big data analysis technology, a high-precision anticrime information support system is designed to help police departments implement more targeted crime prevention strategies at the micro level. Using this anticrime information system, city management can plan and develop crimeprevention tactics in advance to counter crime-peak time periods. Law enforcement can efectively minimize the negative social impacts of all crimes by utilizing the predicted trends of index and nonindex crime occurrences in each area.

In future studies, the crime types can be classified in more detail according to the consequences and social impacts of the crime, an approach that will involve complex feature engineering. This focus is an ongoing part of our latest research project. Furthermore, in this paper, the discussion on the management significance and management application of the crime prediction model is insuficient and thus should be considered in future research.

## Authors’ contributions

Qing Zhu: Conceptualization, Supervision, Resources. Fan Zhang:

Methodology, Writing – Original Draft, Writing – Review & Editing. Shan Liu: Project administration, Supervision, Funding acquisition. Yuze Li: Data Curation, Investigation, Writing – Original Draft.

## Acknowledgments

The project was funded by the National Natural Science Foundation (NSFC) Programs of China [91646113, 71722014, 71471141, and 71350007]. We also appreciate the support of the Youth Innovation Team of Shaanxi Universities “Big data and Business Intelligent Innovation Team.”.

## Appendix A. Architecture of BiGRU network

Fig. A.12 illustrates the regular BiGRU architecture, where the cell of BiGRU consists of only two gates, namely, update gate ${ { z } _ { t } }$ and reset gate $r _ { t } .$ The update gate ${ { z } _ { t } }$ and the reset gate $r _ { t }$ are calculated as shown in Eqs. (A.1)–(A.5):

$$
r _ {t} = \sigma (W _ {r} \cdot [ h _ {t - 1}, x _ {t} ])\tag{A.1}
$$

$$
z _ {t} = \sigma (W _ {z} \cdot [ h _ {t - 1}, x _ {t} ])\tag{A.2}
$$

$$
\tilde {h} _ {t} = \tanh (W _ {\tilde {h} _ {t}} \cdot [ r _ {t} ^ {*} h _ {t - 1}, x _ {t} ])\tag{A.3}
$$

![](/api/attachments/8X9WAPFX/fulltext/images/f9c38b3361058e96d1cb0bb5a3acff2050fa139d6ad000d42ebb97838083d2b7.jpg)  
Fig. A.12. Architecture of BiGRU network.

$$
h _ {t} = (1 - z _ {t}) ^ {*} h _ {t - 1} + z _ {t} ^ {*} \tilde {h} _ {t}\tag{A.4}
$$

$$
y _ {t} = \sigma (W _ {o} \cdot h _ {t})\tag{A.5}
$$

where $W _ { r } , W _ { z } , W _ { \tilde { h } _ { t } } ,$ and $W _ { \mathrm { o } }$ are weighted matrixes; and \* denotes element-wise multiplication and indicates that two vectors are connected.

## Appendix B. Heatmap of spatial clusters

Fig. A.13 shows whether any spatial clusters are formed or whether any areas are more prone to crime than others in the city of Chicago. As shown in Fig. A.13, North-East Chicago has more crimes recorded than other areas, and several clusters are obvious.

![](/api/attachments/8X9WAPFX/fulltext/images/bfb62ed9673409020cb90788de9f0e76099930ac9054b89d88ae3ebc2fe06b8f.jpg)  
Fig. A.13. The cluster of crime.

## Appendix C. Calculating time for area 2 prediction

Fig. A.14 illustrates the calculating time for each rolling step in area 2 prediction, where the average calculating time of the rolling step is 237.328 s. The number of computations for loss value in the four rolling windows is 6836, 7091, 6469, and 6441, respectively. The computing time of every computation for loss value is approximately 0.033 s.

![](/api/attachments/8X9WAPFX/fulltext/images/2a3f7a53adf5c7507b396a8c21ff3a9207f42594bd90d2d1b04a03b635bfefb3.jpg)  
Fig. A.14. The calculating time for area 2 prediction.

## References

[1] CNN. Chicago Violence That Saw 52 Shot, 10 Fatally, Over Weekend Requires ‘all hands on deck' Approach., Top Cop Says, (2019) (accessed 04,06.19). https:// edition.cnn.com/2019/06/03/us/chicago-weekend-shootings/index.html

[2] N. Grimm, S. Faeth, N. Golubiewski, C. Redman, J. Wu, X. Bai, J. Briggs, Global change and the ecology of cities, Science 319 (2008) 756–760.

[3] S. Angel, J. Parent, D.L. Civco, A. Blei, D. Potere, The dimensions of global urban expansion: estimates and projections for all countries 2000–2050, Prog. Plan. 75 (2011) 53–107.

[4] L. Jiang, B.C. O’Neill, Global urbanization projections for the shared socioeconomic pathways, Global Environ. Change 42 (2017) 193–199.

[5] F. Mariani, I. Zambon, L. Salvati, Population matters: identifying metropolitan sub centers from diachronic density-distance curves 19602010. Sustainability 10 (2018).

[6] R.J. Sampson, Urban sustainability in an age of enduring inequalities: advancing theory and ecometrics for the 21st-century city, Proc. Natl. Acad. Sci. USA 114 (2017) 8957-8962.

[7] Y. Tim, S.L. Pan, S. Bahri, A. Fauzi, Digitally enabled crime-fighting communities harnessing the boundary spanning competence of social media for civic engagement, Inf. Manag. 54 (2017) 177–188.

[8] D. Narayan, R. Chambers, M.K. Shah, P. Petesch, Voices of the Poor: Crying Out for

Change, World Bank Publications, 2003.

[9] S.A. Sumner, J.A. Mercy, L.L. Dahlberg, S.D. Hillis, J. Klevens, D. Houry, Violence in the united states: status, challenges, and opportunities, JAMA 314 (2015) 478–488

[10] S. Liu, F. Xia, B. Gao, G. Jiang, J. Zhang, Hybrid influences of social subsystem and technical subsystem risks in the crowdsourcing marketplace, IEEE Trans. Eng. Manag. (2019) 1–15.

[11] Z. Yong, M. Almeida, M. Morabito, D. Wei, Z. Yong, M. Almeida, M. Morabito, D. Wei, Crime hot spot forecasting: a recurrent model with spatial and temporal information, 2017 IEEE International Conference on Big Knowledge (ICBK) (2017) 143–150.

[12] S.J. Miah, H.Q. Vu, J. Gammack, M. McGrath, A big data analytics method for tourist behaviour analysis Inf, Manag, 54 (2017) 771–785

[13] C. Loefler, S. Flaxman, Is gun violence contagious? A spatiotemporal test, J. Quant. Criminol, 34 (2018) 999–1017

[14] D. Weisburd, C.W. Telep, Hot spots policing: what we know and what we need to know, J Contemp. Crim. Justice 30 (2014) 200–220

[15] S.D. Johnson, W. Bernasco, K.J. Bowers, H. Elfers, J. Ratclife, G. Rengert, M. Townsley. Space-time patterns of risk: a cross national assessment of residential burglary victimization, J. Ouant, Criminol. 23 (2007) 201–219.

[16] J. Law, M. Quick, P.W. Chan, Analyzing hotspots of crime using a bayesian spatiotemporal modeling approach: a case study of violent crime in the greater toronto area, Geogr. Anal. 47 (2015) 1–19.

[17] P.L. Brantingham, P.J. Brantingham, Nodes, paths and edges: considerations on the

complexity of crime and the physical environment, J. Environ. Psychol. 13 (1993) 3-28.

[18] M.A. Andresen, N. Malleson, Testing the stability of crime patterns: implications fo theory and policy, J. Res. Crime Delinq. 48 (2011) 58–82.

[19] C. Catlett, E. Cesario, D. Talia, A. Vinci, Spatio-temporal crime predictions in smart cities: a data-driven approach and experiments, Pervasive Mobile Comput. 53 (2019) 62–74.

[20] S.N. de Melo, D.V.S. Pereira, M.A. Andresen, L.F. Matias, Spatial/temporal variations of crime: a routine activity theory perspective, Int. J. Ofender Ther. Comp. Criminol. 62 (2018) 1967–1991.

[21] A. Borg, M. Boldt, N. Lavesson, U. Melander, V. Boeva, Detecting serial residential burglaries using clustering, Expert Syst. Appl. 41 (2014) 5252–5266.

[22] J.J. Corcoran, I.D. Wilson, J. Ware, Predicting the geo-temporal variations of crime and disorder, Int. J. Forecast. 19 (2003) 623–634.

[23] K. Kianmehr, R. Alhajj, Crime hot-spots prediction using support vector machine, IEEE International Conference on Computer Systems and Applications (2006) 952–959.

[24] M.A. Tayebi, M. Ester, U. Glässer, P.L. Brantingham, Crimetracer: activity space based crime location prediction. 2014 JEEE/ACM International Conference on Advances in Social Networks Analysis and Mining (ASONAM 2014) (2014) 472–480.

[25] G. Mohler, Marked point process hotspot maps for homicide and gun crime prediction in chicago, Int. J. Forecast. 30 (2014) 491–497.

[26] W. Gorr, A. Olligschlaeger, Y. Thompson, Short-term forecasting of crime, Int. J. Forecast, 19 (2003) 579–594.

[27] B. Chandra, M. Gupta, A multivariate time series clustering approach for crime trends prediction. 2008 IEEE International Conference on Systems. Man and Cybernetics (2008) 892–896.

[28] C. Peng, H. Yuan, X. Shu, Forecasting crime using the arima model, 2008 Fifth International Conference on Fuzzy Systems and Knowledge Discovery 5 (2008) 627-630.

[29] H. Wang, D. Kifer, C. Graif, Z. Li, Crime rate inference with big data, Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (2016) 635–644.

[30] E. Cesario, C. Catlett, D. Talia, Forecasting crimes using autoregressive models, 2016 IEEE 14th International Conference on Dependable, Autonomic and Secure Computing (2016) 795–802.

[31] R. Kadari, Y. Zhang, W. Zhang, T. Liu, Ccg supertagging via bidirectional lstm-crf neural architecture, Neurocomputing 283 (2018) 31–37

[32] L. Wang, G. Lee, I. Williams, The spatial and social patterning of property and violent crime in toronto neighbourhoods: a spatial-quantitative approach, ISPRS Int. J. Geo-Inf, 8 (2019)

[33] M. Dugato, S. Favarin, A. Bosisio, Isolating target and neighbourhood vulner abilities in crime forecasting, Eur. J. Crim. Policy Res. 24 (2018) 393–415.

[34] M. Quick, G. Li, I. Brunton-Smith, Crime-general and crime-specific spatial patterns: a multivariate spatial analysis of four crime types at the small-area scale, J. Crim. Justice 58 (2018) 22–32

[35] L. Vomfell, W.K. Härdle, S. Lessmann, Improving crime count forecasts using twitter and taxi data, Decis. Support Syst. 113 (2018) 73–85.

[36] T.T. Cai, J. Ma, L. Zhang, Chime: clustering of high-dimensional gaussian mixtures with em algorithm and its optimality. Ann, Stat. 47 (2019) 1234–1267.

[37] S. Ding, N. Zhang, J. Zhang, X. Xu, Z. Shi, Unsupervised extreme learning machine with representational features, Int. J. Mach. Learn. Cybern. 8 (2017) 587–595.

[38] D.G. Márquez, A. Otero, P. Félix, C.A. Garcıa, A novel and simple strategy for evolving prototype based clustering, Pattern Recognit. 82 (2018) 16–30

[39] C. Tîrnauca, D. Gómez-Pérez, J.L. Balcázar, J.L. Montaña, Global optimality in kmeans clustering, Inf. Sci. 439–440 (2018) 79–94.

[40] M. Capó, A. Pérez, J.A. Lozano, An eficient approximation to the k-means clus tering for massive data, Knowl. Based Syst. 117 (2017) 56–69 Volume, Variety and Velocity in Data Science.

[41] Y. Bengio, A. Courville, P. Vincent, Representation learning: a review and new perspectives, IEEE Trans. Pattern Anal. Mach. Intell. 35 (2013) 1798–1828.

[42] D. Zosso, K. Dragomiretskiy, Variational mode decomposition, IEEE Trans. Signal Process. 62 (2014) 531–544.

[43] W. Liu, S. Cao, Y. Chen, Applications of variational mode decomposition in seismic time-frequency analysis., Geophysics 81 (2016) V365–V378

[44] A.A. Abdoos, P. Khorshidian Mianaei, M. Rayatpanah Ghadikolaei, Combined VMD-SVM based feature selection method for classification of power quality events, Appl. Soft Comput, 38 (2016) 637–646

[45] M. Schuster, K.K. Paliwal, Bidirectional recurrent neural networks, IEEE Trans. Signal Process. 45 (1997) 2673–2681.

[46] J. Chung, Çaglar Gülçehre, K. Cho, Y. Bengio, Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling, (2014) arxiv:14123555.

[47] J. Ratclife, Intelligence-led policing and the problems of turning rhetoric into practice, Polic. Soc. 12 (2002) 53–66.

[48] D.L. Davies, D.W. Bouldin, A cluster separation measure, IEEE Trans. Pattern Anal Mach. Intell. PAMI-1 (1979) 224–227

[49] P.J. Rousseeuw, Silhouettes: a graphical aid to the interpretation and validation of cluster analysis, J. Comput. Appl. Math. 20 (1987) 53–65.

Qing Zhu is a professor of finance at International Business School, Shaanxi Normal University. and a postdoctoral researcher in data science at the School of Management of Xi’an Jiaotong University. His research interests are big data and soft computing, machine learning, and neural networks.

Fan Zhang is an M.S. candidate in statistics at International Business School, Shaanxi Normal University. He received his B.E. degree in mechanical design, manufacturing, and automation at the School of Manufacturing Science and Engineering of Sichuan University. His research interests are big data and soft computing, machine learning, and neural networks.

Shan Liu is a professor in information management and e-commerce at the School of Management of Xi’an Jiaotong University. His research interests include IT project management, IT-driven supply chain management, medical information systems, and online reviews.

Yuze Li is an M.S. candidate at the Academy of Mathematics and Systems Science at the Chinese Academy of Sciences. He received his BASc degree in Industrial Engineering from the University of Toronto in 2018. His research interests include machine learning, in formation systems, optimization, and platform competition.
