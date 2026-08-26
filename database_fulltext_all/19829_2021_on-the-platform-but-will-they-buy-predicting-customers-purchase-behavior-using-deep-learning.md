---
otero_id: 19829
otero_key: "XWYU2MXG"
title: "On the platform but will they buy? Predicting customers' purchase behavior using deep learning"
authors: "Neha Chaudhuri; Gaurav Gupta; Vallurupalli Vamsi; Indranil Bose"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113622"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# On the platform but will they buy? Predicting customers’ purchase behavior using deep learning

Neha Chaudhuri <sup>a</sup>, Gaurav Gupta <sup>b</sup>, Vallurupalli Vamsi <sup>c</sup>, Indranil Bose <sup>d,\*</sup>

<sup>a</sup> Toulouse Business School, 20 Boulevard Lascrosses, 31068 Toulouse, France

<sup>b</sup> NEOMA Business School, 1 Rue du Mar´echal Juin, 76130 Mont-Saint-Aignan, France

<sup>c</sup> School of Management & Entrepreneurship, Shiv Nadar University, NH - 91, Tehsil Dadri, Gautam Buddha Nagar, Uttar Pradesh - 201314, India

<sup>d</sup> NEOMA Business School, 59 rue Pierre Taittinger, Reims, 51100, France

## A R T I C L E I N F O

Keywords: E-commerce Customer relationship Deep learning Machine learning Online purchase behavior

## A B S T R A C T

A thorough understanding of online customer’s purchase behavior will directly boost e-commerce business performance. Existing studies have overtly focused on purchase intention and used sales rank as a natural proxy, which however has limited business application. Additionally, intention to purchase does not necessarily convert to actual retail purchases. We aim to further our understanding of online customer’s purchase behavior for an ecommerce platform by predicting the same using deep learning techniques, on a large multidimensional data sample of more than 50,000 unique web sessions. This study used two distinct sets of variables, i.e., platform engagement and customer characteristics, as key predictors of online purchases by retail customers. We further compared the predictive capability of our deep learning method with other widely used machine learning techniques for prediction, including Decision Tree, Random Forest, Support Vector Machines, and Artificial Neural Networks. We found that the deep learning technique outperformed the machine learning techniques when applied to the same dataset. These analyses will help platform designers plan for more platform engage ments while simultaneously expanding the academic understanding of purchase prediction for online e-com merce platforms.

## 1. Introduction

Globally online purchasing has been growing consistently in the last few years. The US Department of Commerce Statistics has reported that retail e-commerce sales have witnessed an 11% rise from 2018 to 2019 while brick-and-mortar sales have seen a rise of only 2%. In 2020, the share of retail sales through the e-commerce mode amounted to 4.28 trillion USD which represented 18% of all such sales. It is projected to reach 21.8% of all sales globally. The recent COVID-19 pandemic has further improved those projections owing to the sudden movement of customers to digital sales channels. Easier delivery and return policies, fast and free shipping on most e-commerce websites, and the option to purchase anything round the clock from the comfort of one’s home, have further increased the desirability of online purchasing during this pandemic. This trend has necessitated the setup of online portals for businesses that were traditionally offline. While this has extended the working hours of these businesses to 24 × 7, it has changed the shopping behavior of both existing and new customers significantly. Unlike traditional businesses where customers visit a store with a strong intention to purchase, customers of online platforms spend a lot of time browsing, comparing products and their prices across websites, and voicing their opinions on brands and their products. These interactions on online platforms serve as a rich source of insights for businesses as well as platform designers to understand the customer mindset. Busi nesses consider it lucrative to understand the product purchase journey in general and purchase behavior in particular, by identifying and un derstanding the role of the actors involved in this process, especially the customers’ traits and the online platform and how their interactions affect actual purchases. Additionally, e-commerce platforms like Amazon and Target extensively use collaborative filtering to recom mend products and product categories based on insights from other customer’s purchase decision processes. The landing page is highly personalized for each customer to convert casual browsing to immediate purchase. Evidently, any advances in prediction of individual-level or group-level purchase decision has huge business implications.

Extant research on customer’s interaction leading to purchase in online platforms can be divided into two distinct streams. The first stream has examined customers’ browsing behavior through various forms of their engagement with the online platforms [1,2]. Clickstream data is considered an important source for understanding such in teractions. Moe [2] has examined a customer’s in-store navigational behavior based on the content of pages viewed. In this paper, click stream data is used to empirically categorize shopping strategies of customers into directed buying, search/ deliberation, hedonic buying, and knowledge building. Moe and Fader [1] have further developed a model to predict the conversion of store visits into purchases based on the observed history of online sessions of customers and their purchases. Schlosser, White, and Lloyd [3] have argued that varying platform de signs have led to different levels of customer trust on the e-commerce platforms, and have ultimately impacted purchase decisions. They have investigated the impact of various design elements such as background colour, fonts, zoom and product display, on users’ trust and purchase related decisions.

The other stream of research has examined customers’ characteris tics in their interactions with the online platform. Kumar et al. [4] have computed the customer lifetime value for each customer and have shown its importance in developing differential marketing initiatives targeted to each customer. Another study has investigated the role of customer demographics such as gender, age, profession, and other fac tors related to historical purchases to predict if a customer is likely to purchase a product in a consecutive visit to the online platform [5].

Although there have been studies in each stream, a concerted effort to link and examine platform engagement activities related to the online e-commerce platform and customer characteristics is scant. Addition ally, existing studies have primarily adopted customer purchase inten tion on e-commerce platforms as their dependent variable. Although measures of purchase intention do possess predictive usefulness [6], these do not always lead to actual purchases and are thus weaker proxies for understanding purchasing behavior of customers. In this study, we address the above gap by examining the actual purchase behavior of customers on an online platform as a consequence of their engagement with the online platform. We predict whether a customer purchases an order placed in a particular web session (a web session is a single visit to the online platform) and identify factors that affect the customer’s purchase. Unlike conventional predictive studies, we believe advances in computing techniques like deep learning (DL) will provide useful insights due to their capability to learn and improve prediction contin uously. Therefore, we answer the following research questions in thi study:

How does customer engagement with the online e-commerce platform affect their actual purchases? Can DL techniques be used to predict retail sales in an e-commerce platform? Does DL provide better prediction than con ventional machine learning (ML) techniques in this context?

We compare the predictive powers of different techniques to predict actual purchases on an online shopping platform. To this end, we analyze the actual purchases of online customers across more than 50,000 sessions on an online shopping platform and predict them accurately with the help of DL and ML techniques. The results of our study have significant implications for both theory and practice. In terms of academic contribution, we supplant the rich scholarship on user’s online purchase behavior by providing empirical evidence about the role of platform interactions on actual purchases. Although there have been attempts to explore this phenomenon [6], researchers have examined this primarily using sales rank, which does not reflect actual user behavior. Our consideration of actual purchase behavior makes this research unique.

## 2. Related work

## 2.1. Role of customer’s platform engagement in determining purchases

Customer’s platform engagement with the online platform marks the first step in the complex process of purchase decision-making [7,8] involving the creation of awareness, followed by engagement leading to consideration before an actual purchase decision is made. Customer’s platform engagement goes beyond satisfaction and loyalty and provides a real competitive advantage that drives success for businesses in the long term [9]. From a business perspective, a successful interaction with the platform is considered to be one which necessarily leads to a valid purchase. Customers’ engagement with online shopping platforms is considered to be an essential antecedent for the overall purchase pro cess, from the perspective of platform design, and is central to the cus tomers’ online purchase behavior [10]. To examine this complex process of purchase decision making, extant literature has approached cus tomers’ engagement with online platforms from two different perspec tives, platform engagement attributes and customer attributes.

## 2.1.1. Platform engagement attributes

Online e-commerce platforms have designed and developed a wide array of artefacts like user-friendly design, swift product search, easy checkout process, and convenient and ubiquitous access through different web and mobile platforms [11], to stimulate a positive pur chase decision at every instance of customer interaction. Various studies have determined that the interactivity of the web interface of the shopping platform plays a crucial role in affecting consumers’ online shopping performance [12,13]. Additionally, the purchase process dif fers online and so the platform plays a crucial role in decision making towards a purchase. In line with these findings, various scholars have examined platform engagement through persuasion in the online plat form design [14]. For instance, interactivity or the lack of it molds purchase intention through meaningful platform engagement and further affects the general attitude towards the platform. Website interactivity refers to the ease of reciprocal communication between the customer and the online shopping portal. It allows customers to browse the platform and have meaningful interactions with shopping portal across multiple sessions. Such interactive features are useful for enhancing the customer-platform relationship and reinforcing the cus tomers’ intention to return to the platform for future purchases [15]. Ye et al. [16] have found that website interactivity positively influences purchasing intentions even for a premium-priced product.

## 2.1.2. Customer attributes

Although platform attributes play a vital role in customer’s engagement with the platform, however, demographic characteristics like age and gender, along with other attributes like technology efficacy and individual value systems, are also significant influencers of the scale and scope of platform engagement [17]. As a result, even with the same set of platform engagement artefacts, different customers will engage differently. For example, significant generational differences exist in the use of the Internet [18]. Consequently, these different user categories engage with online platforms in their own distinct ways. Personality traits have thus been considered to be very important to examine online customer’s platform engagement [19].

## 2.2. Online purchase prediction

Predicting customers’ decision to purchase has been considered to be the holy grail of research in different management studies, including marketing, information systems, neuroscience, and so on. While mar keting scholars have developed various models to determine purchase decisions [20], neuroscience scholars have used techniques like analysis of real-time EEG to predict purchases [21]. While each of these different approaches has found some success, there still exists immense opportunity to further extend our knowledge in this area.

Existing studies have further examined website usability [22], modelled the convergence of transaction convergence as task comple tion [23] or have predicted this convergence [5]. Close & Kukar-Kinney [24] have examined the capabilities of the online platform as a function of the overall purchase process. They have linked user motivations on the platform with their actions with a focus on their usage of the online platform features. Various studies including those from Brown et al. [10], and Olbrich and Holsing [25] have analyzed customers’ online activity to draw insights about their purchasing behavior. However, a willingness to purchase does not necessarily translate to the same in an uncontrolled real-life setting [20]. Increasingly, studies have started adopting real world data (e.g., clickstreams or retail sales datasets) to examine online purchase behavior [35,36].

## 2.3. Analytical methods for prediction

In order to predict customers’ decision to purchase, analytical methods such as regression and ML have been used by researchers over the years. The most widely used methods include Stepwise Logistic Regression (SLR) [26], Decision Tree (DT) [27], Random Forest (RF) [28], Support Vector Machines (SVM) [29], and Artificial Neural Net works (ANN) [30]. DT and RF have widespread applications for pre diction related problems because of their ease of use and the high interpretability of their generated results. Moreover, unlike ANN, DT, and RF are both capable of directly handling categorical variables [27,28]. However, DT is less robust than RF and has been found to be highly sensitive to even small variations in data [31]. Additionally, RF is simpler to tune because it has a smaller number of hyperparameters as compared to neural network-based models [28]. However, ANN has been found to outperform DT and RF in terms of resource utilization and handling of multidimensional complex datasets [31,32]. SLR has been used in extant literature for predictions involving binary dependent variables. However, it suffers from a major limitation that makes it unfit for rigorous empirical analysis. SLR adds or removes variables during analysis in a specific order and studies have found that this order of addition or removal of variables can affect the final outcome [33]. This has prompted scholars to suggest the use of SLR for exploratory research only.

While all of these approaches have improved the ability to determine customers’ purchases, we believe that recent advances in computing, especially DL techniques, hold much promise, primarily due to their capability to improve predictions through learning. Recently various studies have started embracing this approach for analyzing large and complex datasets. For example, a recent study by Loureiro et al. [34] has adopted DL to forecast sales in fashion retailing. Also, Korpusik et al. [35] have applied a feedback-based DNN model (i.e., Recurrent Neural Network) to a large corpus of tweets of potential customers to predict their choice of products and final purchases.

In summary, a detailed review of literature in this area, as shown in Table A1, highlights important research gaps. First, there is a lack of empirical evidence connecting platform engagement with the actual purchase decision. The focus has primarily been on purchase intention which, as theory has shown, can be different from actual purchase behavior. While purchase intention represents the will to purchase a product, purchase behavior refers to the actual purchasing process on an online platform, which is the focus of our research. Second, existing studies have examined the impact of platform engagement attributes and customer attributes on purchase intentions, but separately. There is a lack of a concerted effort to link these two streams of research. It is necessary to examine these distinctions and their combined impact when attempting to examine online customer engagement. Additionally, behavioral data analysis from clickstream and retail sales has huge un tapped potential in understanding customers’ activities on online shopping platforms and the impact that these activities have on the customers’ purchase behavior. In this study, we attempt to bridge these gaps in literature by examining retail sales data to draw insights about purchase behavior of customers through meaningful engagement on an e-commerce platform. Table A1 provides a summary of the extant research in this area.

## 3. Data description

The challenges associated with the application of big data analytics to predict customer purchases stem from the lack of actual sales data. As a result, past literature has widely used ‘intention to purchase’ [36] as well as sales rank of products [37] as proxies for actual purchases of customers on e-commerce platforms. However, recent studies have shown that analyzing actual purchase data would yield more convincing results [38]. The dataset used in this study addresses this concern. We have collected anonymized web browsing data from an online e-com merce platform. This e-commerce platform is a multi-vendor general purpose online marketplace based in Germany and Belgium. The dataset comprised historical purchase data and other variables relevant for addressing the research questions of this study. The data consisted of 429,013 unique sessions. One or more products were purchased in 290,030 sessions (67.60%) while no product was purchased in 138,083 (32.40%) sessions. Each row of this dataset represented a single online session of a prospective customer. The corresponding variables included activities of prospective customers, such as browsing, clicking on products, adding products to shopping carts, purchasing products or abandoning the carts. Table 1 summarizes the platform engagement and purchasing behavior related variables for customers on the e-commerce platform as observed from the dataset.

Table A1  
Summary of related literature using ML and DL methods.

<table><tr><td>Topics studied</td><td>Research approach</td><td>Algorithm used</td><td>Research contributions</td><td>Research limitations</td></tr><tr><td rowspan="3">Role of customer characteristics and engagement with e-commerce platforms in purchase predictions</td><td>Dataset related to frequency, time lapse and values of earlier purchases [62]</td><td>Logistic lasso regression, extreme learning machine and gradient tree boosting methods [62]</td><td>Innovative pairwise comparison of time lapse and value difference between two consecutive purchases to predict future purchase [62]</td><td>No distinction between high versus low involvement product categories [62]</td></tr><tr><td>Online sale data of consumer goods [63]</td><td>LDA [63]</td><td>Inclusion of customer heterogeneity as a predictor [63]</td><td>Limited scalability of method [63]</td></tr><tr><td>Clickstream dataset related to browsing of online forum by potential customers [64]</td><td>Maximum likelihood estimation followed by binary regression [64]</td><td>Comparison between role of focused versus unfocused product search and browsing behavior on purchase decision [64]</td><td>Clickstream data did not allow in-depth analysis and classification of different browsing behaviors [64]</td></tr><tr><td rowspan="3">Role of platform characteristics in purchase predictions</td><td>Naturally obtained dataset from 4000 customers over 2 years related to multiple sources of advertisement exposure [65]</td><td>Tobit model followed by Variational Bayes ML method [65]</td><td>Data linked to advertisement exposure revealed negative effects of e-mail catalogues and positive effects of paid effects and competitor catalogues [65]</td><td>Examination of a single product category (i.e. clothing category) [65]</td></tr><tr><td>Data from 400 respondents about website quality in an experimental setup [66]</td><td>Ordinary Least Squares (OLS) regression [66]</td><td>Identification of website quality factors such as sophistication, genuineness, and unpleasantness [66]</td><td>Lack of external validity due to use of student samples [66]</td></tr><tr><td>Dataset of tourism e-commerce products [67]</td><td>Co-EM logistic regression [67]</td><td>Combined semi-supervised and multi-view learning procedures to exploit unlabeled data [67]</td><td>Lack of generalizability to other product domains [67]</td></tr></table>

Table 2 summarizes the demographics of customers who are repre sented in the dataset. Table 3 contains a brief description of variables present in the dataset used for this study. The dataset has 18 variables that can be broadly classified into two sets of attributes: the first set includes the platform engagement attributes, and the second set includes the customers’ attributes. The first set of attributes represents variables that are primarily related to a single online session on the portal, whereas the second set of attributes represents variables about the prospective customers. Variables about customers include de mographics, historical purchase patterns, and user profile data for the ecommerce platform. Table 3 also provides the descriptive statistics for this dataset.

The platform engagement related variables included data about the web sessions of customers (such as time and day of week of session, duration of a session, and number of times the customer logged in) as well as click-stream data related to exploratory search behavior of the customer (such as price and number of products clicked, cart size, and value).

## 4. Methodology

This study was aimed at identifying significant platform engagement related and customer related predictors of online purchases, while also focusing on examining the potential of DL approach in this context. This approach is relevant for this study as the DL technique uses its dense network structure to recognize complex patterns in datasets. This study has used different analytical methods, including some traditional ML techniques and the more advanced DL technique to examine the research question. The adopted methodology is shown in Fig. 1 below.

## 4.1. Pre-process

We adopted a four-stage approach (as shown in the data pre-process block of Fig. 1) to prepare the dataset in order to improve the predictive accuracy and computational efficiency. Apart from the platform engagement related variables as described in Table 2, the dataset also included records of availability status of products that customers were interested in purchasing and records related to the stage of completion of the multi-stage purchase process. However, we discarded these var iables from the dataset as they suffered from scant variability of data values and also more than 45% of the data values were missing. This is in line with extant research which suggest that the presence of missing values would reduce the predictive power of a technique [39]. We used the filtered dataset for subsequent analysis.

The second stage included the imputation of any remaining missing values in the variables. For this, we employed a DT. We chose this method over using the mean or median of the variable because a DT results in more accurate estimation by using the information of the remaining variables [40]. Moreover, the DT is also capable of handling categorical variables in the dataset [27]. We treated the variable with

## Table 1

Platform engagement and purchasing behavior of customers for the online portal.

<table><tr><td>Description</td><td>Frequency</td></tr><tr><td>Number of prospective unique customers</td><td>105,038</td></tr><tr><td>Number of sessions</td><td>429,013</td></tr><tr><td>Number of sessions with a purchase</td><td>290,030</td></tr><tr><td>Number of sessions without a purchase</td><td>138,983</td></tr></table>

## Table 2

Demographics of the data.

<table><tr><td colspan="2">Demographic traits</td><td>Statistic</td><td></td></tr><tr><td rowspan="2">Gender</td><td>Female</td><td>73.35%</td><td></td></tr><tr><td>Male</td><td>26.65%</td><td></td></tr><tr><td rowspan="6">Age</td><td></td><td>Mean</td><td>44.93</td></tr><tr><td></td><td>Std. dev.</td><td>11.93</td></tr><tr><td>Age (Female)</td><td>Mean</td><td>44.51</td></tr><tr><td></td><td>Std. dev.</td><td>11.68</td></tr><tr><td>Age (Male)</td><td>Mean</td><td>46.09</td></tr><tr><td></td><td>Std. dev.</td><td>12.52</td></tr></table>

Table 3  
Descriptive statistics of variables used in this research

<table><tr><td>Variables</td><td>Minimum</td><td>Maximum</td><td>Mean</td><td>Std. Dev.</td></tr><tr><td colspan="5">Platform engagement attributes</td></tr><tr><td>Time of session</td><td>1.23</td><td>23</td><td>14.48</td><td>4.37</td></tr><tr><td>Day of week of session</td><td>1</td><td>7</td><td>-</td><td>-</td></tr><tr><td>Duration of session (minutes)</td><td>0</td><td>8736.92</td><td>1415.71</td><td>1711.91</td></tr><tr><td>Number of log-ins of customer</td><td>1</td><td>6</td><td>2.37</td><td>0.81</td></tr><tr><td>Number of products clicked</td><td>1</td><td>114.97</td><td>21.52</td><td>24.73</td></tr><tr><td>Lowest price of product clicked</td><td>0</td><td>429.21</td><td>32.33</td><td>71.41</td></tr><tr><td>Highest price of product clicked</td><td>0</td><td>882.78</td><td>96.13</td><td>149.85</td></tr><tr><td>Sum of prices of all products clicked</td><td>0</td><td>8776.98</td><td>704.37</td><td>1122.17</td></tr><tr><td>Number of products in cart</td><td>0</td><td>15.67</td><td>3.65</td><td>3.25</td></tr><tr><td>Lowest price of product in cart</td><td>0</td><td>516.32</td><td>40.43</td><td>86.31</td></tr><tr><td>Highest price of product in cart</td><td>0</td><td>643.37</td><td>68.17</td><td>108.73</td></tr><tr><td>Sum of prices of all products in cart</td><td>0</td><td>1144.08</td><td>130.10</td><td>168.21</td></tr><tr><td colspan="5">Customers&#x27; attributes</td></tr><tr><td>Customer account score assigned by online retailer</td><td>89.53</td><td>638</td><td>486.38</td><td>126.18</td></tr><tr><td>Customer account lifetime (days)</td><td>0</td><td>602</td><td>135.56</td><td>108.32</td></tr><tr><td>Number of payments made by customer</td><td>0</td><td>93.12</td><td>11.36</td><td>14.44</td></tr><tr><td>Age of customer</td><td>17</td><td>81.17</td><td>45.07</td><td>11.98</td></tr><tr><td>Gender of customer</td><td>1</td><td>2</td><td>-</td><td>-</td></tr><tr><td>Days elapsed since last purchase</td><td>3</td><td>738</td><td>79.88</td><td>97.61</td></tr></table>

missing values as a dependent variable and the remaining independent variables as predictors. The steps followed in this model-based missing value imputation was similar to the one followed by Zolbanin et al. [41]. The remaining variables were first ranked by their ability to predict the dependent variable with missing values. The variables which only marginally contributed to the estimation were subsequently removed from consideration. Finally, the best predictor from the model was used to replace the missing values of the dependent variable. For the records in the dataset where the best predictor also had missing values, the next best predictor with no missing value was used. This whole process was repeated for all variables with some missing values in the dataset.

Following this, numerical values of the variables that were more than five standard deviations away from the mean were defined as extremes, while those values that were three standard deviations but within five standard deviations away from the mean were defined as outliers. Re cords containing more than one outlier were eliminated whereas for the remaining records, outlier variables were coerced to a value equivalent to mean ± three times its standard deviation.

The widely used DL and ML techniques are incapable of handling categorical inputs efficiently. This is true for specifically NN models as well as SVM. Hence, we applied one hot encoding to transform cate gorical variables into numerical variables while successfully averting wrongful interpretation of hierarchy in data values by the models [42].

Decision Support Systems xxx (xxxx) xxx

![](/api/attachments/XWYU2MXG/fulltext/images/07e23792e2770113cb97abcc3f0534fa0bf18970016bdf9790f18777881b088a.jpg)  
Fig. 1. The process diagram of the study.

For every n-level categorical variable, n variables were generated. After this preprocessing, the dataset had 25 numerical variables that acted as predictors of customers’ purchases.

## 4.2. Data analysis

The DL and ML techniques required initialization of hyper parameters during model building. These hyperparameters determined the training capability of the techniques [43] and needed to be tuned during the learning process. Moreover, the traditional approach of using a training dataset to train a ML technique and then using a testing dataset to evaluate the performance of the technique often suffers from overfitting and lack of robustness [44]. To overcome this problem, we employed k-fold cross validation with k = 5 for each run. This procedure involved partitioning of the training dataset into five folds. For every iteration of the procedure, one fold was treated as a validation set while the remaining four folds acted as training sets. In each iteration, we performed grid-search based hyperparameter tuning until the training and validation errors stabilized. This helped to overcome the more subtle ‘hyperparameter overfitting’ [45]. Further, following Zolbanin et al. [41], we calculated the accuracy-based importance score of variables fo each run. This importance score compared the predictive ability of the independent variable based on how much it contributed to the overall accuracy of a given model. To determine the importance of a variable, we started with the full combination of variables and kept dropping variables one by one, and trained the technique with the remaining variables, and calculated the accuracy of prediction. We observed that the absence of a relatively important variable resulted in a significant drop in the accuracy of the model. Finally, following Shen et al. [46], we used sensitivity analysis-based feature selection to extract the optimal subset of variables that most accurately predicted purchases. We also compared the training and validation errors for the predictive models and found that the validation error was within 0.048% of the training error. This confirmed insignificant overfitting.

## 4.3. Deep learning (DL)

The DNN is a DL technique that is an evolved variant of ANN. Unlike the network structure of a traditional ANN, a DNN has a fully connected layer as well as multiple sparsely connected intermediate layers. The greater depth of its structure, as compared to the ANN, allows it to learn multiple levels of representations in a dataset with increasing complexity. This enhanced representation learning leads to a better predictive performance of the DNN. DL has been used for various research applications, including image classification, emotion detection, sales prediction, and has been applied to a variety of data types. As a result, different types of DL architectures have been developed for different use cases. For example, convolutional neural network (CNN) has been used for image processing and is well-suited for multidimensional records. The recurrent neural network (RNN) works well with sequential data with a temporal dynamic behavior.

For this study, we used the feed-forward DNN. We chose this DL technique because the dataset used in this study consisted of onedimensional inputs only. Our choice to apply the DNN in this context was further affirmed due to the data-driven self-adaptive approach of the DNN that was in contrast to the traditional methods that required specific assumptions about the functional form of the data. The network structure of the DNN is defined in a way such that the initial layers learn the simpler data features, while the deeper layers handle the more complex features [47]; thus, enabling it to capture nonlinear relation ships in the dataset. Moreover, prior studies have shown that the DNN is less vulnerable to the curse of dimensionality, as compared to the ML regression-based models. This makes the DNN suitable for this study because it is expected to handle the multiple multi-class categorical as well as numerical variables of the dataset efficiently.

We used the stochastic gradient descent (SGD) method to train the DNN and initialized it with three layers and an equal number of neurons in each layer. SGD is the most preferred cost-effective optimization al gorithm to train neural networks as it ensures randomness by intro ducing a single training sample at each iteration [61]. We investigated different configurations of the network structure, including three, five, and seven layers with 64,128 and 256 neurons in each layer. The results are reported in the following section. Finally, since the DNN is vulner able to overfitting, we used an early stopping and a dropout layer to address this problem, as suggested by Srivastava et al. [48].

We used Keras 2.3.0, an open source Python library running on Py thon 3, to develop the DL and ML techniques. Keras is a programming interface which works on top of TensorFlow version 2.1.0. TensorFlow is an open source software library developed by Google for ML.

## 4.4. Performance metrics

We calculated nine evaluation metrics to compare the performance of the predictive models. These metrics are Accuracy, Recall, F1-score, Positive Predictive Value (PPV), Negative Predictive Value (NPV), False Positive Rate (FPR), ROC-AUC, and Matthews Correlation Coeffi cient (MCC) [49,50]. PPV and NPV are proportions of positive and negative results that are true positives and true negatives, respectively. The value of MCC range between [− 1,1] and the metric produces a good score only if a model has exhibited satisfactory performance for all four confusion matrix categories (i.e., true positives, true negatives, false positives, and false negatives) [50]. Unlike the scalar metrics like ac curacy, recall, and F1-score, MCC is symmetric and not sensitive to class imbalance [51]. It represents the correlation coefficients between the true and predicted values and works better than accuracy and F1-score for prediction of binary classes. The final reported values for the per formance metrics are the mean of the values that are obtained from the five folds of the cross-validation process.

## 5. Results

We initialized the DNN model with three layers and with an equal number of neurons in each layer. Following Loureiro et al. [34], we investigated different configurations of the network structure, including three, five, and seven layers with 64,128 and 256 neurons in each layer. The 5-layer network with 128 neurons in each layer exhibited the best performance. The performance of the nine configurations are shown in Table 4. The investigation revealed that an increase in network depth and width upto 5 layers and 128 neurons, steadily increased the pre dictive ability of the model. However, we observed a deterioration in the overall performance with a further increase in the network elements beyond these values. Existing literature asserts that additional network elements beyond the optimal number leads to overfitting of the model for the training dataset and results in poorer performance [41,52]. Hence, we discarded denser network architectures.

## 5.1. 5.3 Comparison of performances of the predictive techniques

We have summarized the performances of the DL (DNN configura tion with 5 layers and 128 neurons per layer) and ML techniques in Table 5. All models used in the study were tuned to optimize the hyperparameters. The value of the hyperparameters for the DNN is shown in Table A2. Due to limitations in space, the performance sta tistics of only the models with the best performing hyperparameters have been reported in Table 5. Similar values for performance metrics were obtained when the ML and DL techniques were used for the vali dation dataset. This is not reported due to paucity of space. The results indicate that all techniques have the capability to support the decisionmaking process of firms because their reported ROC-AUC values are above the standard benchmark value of 0.5. As shown in Table 5, all techniques are able to accurately predict whether a purchase has been

## Table 4

Performances of different configurations of the DNN.

<table><tr><td>Number of layers</td><td>Neurons per layer</td><td>Accuracy</td><td>F1-score</td><td>MCC</td></tr><tr><td rowspan="3">3</td><td>64</td><td>0.83</td><td>0.88</td><td>0.63</td></tr><tr><td>128</td><td>0.85</td><td>0.89</td><td>0.68</td></tr><tr><td>256</td><td>0.87</td><td>0.91</td><td>0.72</td></tr><tr><td rowspan="3">5</td><td>64</td><td>0.88</td><td>0.91</td><td>0.74</td></tr><tr><td>128</td><td>0.89</td><td>0.92</td><td>0.75</td></tr><tr><td>256</td><td>0.87</td><td>0.91</td><td>0.72</td></tr><tr><td rowspan="3">7</td><td>64</td><td>0.86</td><td>0.90</td><td>0.70</td></tr><tr><td>128</td><td>0.85</td><td>0.89</td><td>0.68</td></tr><tr><td>256</td><td>0.84</td><td>0.88</td><td>0.64</td></tr></table>

## Table 5

Performance metrics of the predictive techniques.

<table><tr><td rowspan="2">Metrics</td><td colspan="4">ML techniques</td><td>DL technique</td></tr><tr><td>DT</td><td>RF</td><td>SVM</td><td>ANN</td><td>DNN</td></tr><tr><td>Accuracy</td><td>0.83</td><td>0.81</td><td>0.83</td><td>0.84</td><td>0.89</td></tr><tr><td>PPV</td><td>0.81</td><td>0.82</td><td>0.84</td><td>0.83</td><td>0.87</td></tr><tr><td>Recall</td><td>0.95</td><td>0.90</td><td>0.91</td><td>0.94</td><td>0.96</td></tr><tr><td>NPV</td><td>0.87</td><td>0.79</td><td>0.82</td><td>0.87</td><td>0.92</td></tr><tr><td>FPR</td><td>0.38</td><td>0.34</td><td>0.31</td><td>0.34</td><td>0.26</td></tr><tr><td>F1-score</td><td>0.88</td><td>0.86</td><td>0.87</td><td>0.88</td><td>0.92</td></tr><tr><td>ROC-AUC</td><td>0.85</td><td>0.84</td><td>0.84</td><td>0.85</td><td>0.89</td></tr><tr><td>MCC</td><td>0.63</td><td>0.59</td><td>0.63</td><td>0.65</td><td>0.75</td></tr><tr><td>Std. dev. of accuracy</td><td>0.0241</td><td>0.1015</td><td>0.0277</td><td>0.0209</td><td>0.0053</td></tr></table>

Table A2  
Hyperparameter tuning for the DNN in this study.

<table><tr><td>Network hyperparameters</td><td>Search space</td><td>Selected values</td></tr><tr><td>Input units</td><td>Fixed</td><td>25</td></tr><tr><td>Learning rate</td><td> $[10^{-6},10^{-1}]$ </td><td> $10^{-3}$ </td></tr><tr><td>Batch size</td><td>[10,1000]</td><td>100</td></tr><tr><td>Number of hidden layers</td><td>3,5,7</td><td>5</td></tr><tr><td>Number of neurons per hidden layer</td><td>64,128,256</td><td>128</td></tr><tr><td>Dropout</td><td>[0,0.33]</td><td>0.1</td></tr><tr><td>Batch normalization</td><td>-</td><td>Yes</td></tr><tr><td>Activation function in hidden layer</td><td>ReLU, tanh</td><td> $ReLU^1$ </td></tr><tr><td>Loss function</td><td>-</td><td>Cross-entropy</td></tr><tr><td>Activation function in output layer</td><td>-</td><td>Softmax</td></tr></table>

1 ReLU activation function: With the addition of extra hidden layers to the DNN, the loss function starts approaching zero. This is particularly true for tanh and sigmoid functions. This is termed as the vanishing gradient problem. This problem becomes more prominent for the DNN with an increasing number of layers, making it hard to train. The use of the ReLU function and batch normalization can solve this problem for the DNN.

made for more than 80% of the web sessions.

The results indicate that the DNN was able to outperform the others on all explored metrics, followed closely by DT and ANN. To verify that the models indeed performed differently, we conducted the widely used Cochran’s Q test for statistical comparison of performances. We found that the Q value (approximating $\chi ^ { 2 } )$ was 12.794 which corresponded to a p-value 0.012327 $( \mathbf { i . e . , } p \ < \ 0 . 0 5 )$ and implied that the predictive models did not perform equally well. Additionally, the McNemar’s tests for pairwise comparison revealed that the DNN was indeed the best performing model as compared to the other ML models (p < 0.001). This significant improvement in the predictive performance of the DNN can be attributed to its distinct network elements (e.g., weight functions, number of layers in the network, and the number of neurons in each layer). The multiple network layers of the DNN enhanced the process of feature learning [53]. The initial layers are meant for learning simpler features, while the later layers are responsible for predicting the outcome based on more complex combinations of features produced by the previous layers. On the other hand, unlike the ML techniques, the network structure of the DNN makes it less vulnerable to the curse of dimensionality [54]. Therefore, the deep network structure of the DNN empowers it to handle the large dataset used in this study.

## 6. Discussion

## 6.1. Relative importance of predictor variables

To gain deeper insights about the individual predictive capabilities of variables, we calculated and ranked the accuracy-based relative variable importance [55]. Variable importance is measured by the decrease in the overall predictive accuracy when a predictor variable is dropped from the model. The impact on the overall accuracy for a predictor variable was calculated by dropping only one variable at a time from the complete DNN model and then re-analyzing the data. The impact (i.e., reduction in accuracy) was greater for a variable which had a higher contribution to accurately predict purchase in a web session and this translated into a higher importance score for the variable. We then normalized the scores in the form of ‘relative importance’ of a variable with respect to the whole set of variables available for analysis. The value of relative importance ranges from 0 to 1, where 1 represents the variable with the highest contribution to the accuracy of the model and 0 represents the variable with the lowest contribution. Table 6 shows the relative importance of the top twelve variables for the DNN model with 5 layers and 128 neurons per layer. However, each of the five runs of the DNN (corresponding to the five-fold cross-validation) accepted different combinations of predictor variables in order to ach ieve the best performance. This difference can be attributed to the varying specificities of each model [34]. Therefore, the results in Table 6 denote the average impact of each predictor variable on the accuracy of the model. Also, the relative importance indices across the other four ML techniques exhibited similar trends.

Of the top twelve predictors, nine belonged to the platform engagement category. This result suggests that platform engagement with the online e-commerce platform heavily impacts their purchase decisions. Specifically, the variables time when the session began and day of the week when the session began were highly predictive. These results suggested that time had a significant impact on customer purchases on an online platform. At specific times of the day and on specific days, the customers had a higher propensity to purchase. In other words, there existed peak shopping times similar to offline stores, even for online shopping platforms.

Customer account lifetime and days elapsed since last purchase were also found to be universally important for all techniques. These variables captured the sensitivity of the type of customer’s association with the ecommerce platform and established the conventionally accepted belief that loyal customers had a higher propensity to purchase than new customers. Interestingly, although customer account lifetime was found to be a good predictor of actual sales, the number of payments made by the customer did not significantly contribute to purchase decision. This suggested that even though the customer might not have multiple

## Table 6

Relative importance of variables.

<table><tr><td rowspan="2">Variable category</td><td rowspan="2">Variables</td><td colspan="2">DNN</td></tr><tr><td>Impact on accuracy (%)</td><td>Relative importance</td></tr><tr><td rowspan="9">Platform engagement attributes</td><td>Day of the week when session began</td><td>0.92</td><td>0.44</td></tr><tr><td>Time when session began</td><td>0.42</td><td>0.20</td></tr><tr><td>Sum of prices of all products added to cart</td><td>0.25</td><td>0.12</td></tr><tr><td>Sum of prices of all products clicked on</td><td>0.11</td><td>0.05</td></tr><tr><td>Lowest price of product added to cart</td><td>0.10</td><td>0.05</td></tr><tr><td>Number of products added to cart</td><td>0.09</td><td>0.04</td></tr><tr><td>Highest price of product added to cart</td><td>0.07</td><td>0.04</td></tr><tr><td>Number of products clicked on</td><td>0.07</td><td>0.03</td></tr><tr><td>Highest price of product clicked on</td><td>0.06</td><td>0.03</td></tr><tr><td rowspan="3">Customers&#x27; attributes</td><td>Customer account lifetime</td><td>2.10</td><td>1.00</td></tr><tr><td>Days elapsed since last purchase</td><td>1.48</td><td>0.71</td></tr><tr><td>Customer account score assigned by the online retailer</td><td>0.15</td><td>0.07</td></tr></table>

successful orders, the duration of their association with the platform impacted their propensity to purchase.

While we are not suggesting the lack of importance of repeat cus tomers for online purchases, we want to highlight the importance of loyal customers for all types of purchases. Such customers experienced greater familiarity and comfort with the online platform and returned to the platform repeatedly for additional purchases. The inclusion of these variables were a strong indicator of the need for ease of navigation a well as the customers’ familiarity and trust on the platform.

The variables sum of prices of all products clicked on, and lowest price of product added to cart, were also identified to be among the important predictors. They indicated the existence of a relationship between platform engagement and purchase behavior. The first variable indi cated a casual platform engagement session involving prospection while the second variable indicated consideration to add some products to the cart and preparation for successful checkout. The variable lowest price of product added to cart was found to be a better predictor as compared to the variable lowest price of product clicked on. This result suggested that spending time in browsing for products did not necessarily convert to actual purchases. Browsing was a phase where a potential customer often explored and compared products and their features and this did not necessarily indicate an intent to purchase.

Finally, customer score indicated the effectiveness of the retailer’s process for assigning this score to each customer. However, since this variable was proprietary and highly dependent on the product and other related characteristics, it was unlikely to exhibit importance for pre diction of purchases on other online retail platforms.

Another interesting observation from the results shown in Table 5 was that the duration of a session and the number of times the user logged in on an online e-commerce platform did not significantly impact pur chase. This indicated that engagement did not necessarily represent intention to purchase. This observation reinforced the need to design better recommendations and enhance platform engagement to help customers make quicker purchase decisions while limiting online re sources devoted to each customer. Online e-commerce platforms needed to address the balance between higher customer loyalty through better (often longer) engagement and streamlined design to support quicker purchases (also implying lower platform engagement).

## 6.2. Sensitivity analysis-based feature selection

Feature selection is a core component of any machine learning application. Discarding redundant variables improves the predictive accuracy of ML and DL models, speeds up the training process, and re duces the overall cost of computation [34,56]. The two frequently used feature selection methods include filter-based and wrapper-based methods. Filter-based methods (e.g., correlation coefficient) depend on properties of data and are often carried out as part of the data preprocessing stage. These methods suffer from instability due to inde pendence from underlying predictive models [57]. The wrapper-based methods have been found to perform better than filter-based methods because they use the knowledge of the underlying learning algorithms [58]. Therefore, we adopted a wrapper-based sensitivity analysis-based feature selection method that has been used in previous studies by Zhang [58] and Shen et al. [46], to generate an optimal subset of features which can most accurately predict purchases.

For this, we re-trained the DL and ML techniques with the features shown in Table 6, in a descending order. This meant that the first input variable was the one with the highest relative importance and so on. The changes in average accuracies for the ML and Dl models over five runs (corresponding to the five-fold cross-validation process) are shown in Fig. 2.

Fig. 2 indicates that the accuracy of all models peaked when trained with the top twelve features and decreased thereafter. This could be attributed to the curse of dimensionality which meant that adding new features during the training of a model, beyond an optimal number, could lead to degradation of its predictive performance [59]. However, unlike the ML techniques which exhibited sharper reduction in their accuracies after the optimal point, the relative degradation in accuracy for the DNN was lower. For all techniques, the sharp decline in accuracy could be attributed to overfitting and the noise introduced due to the addition of redundant variables. The DNN was able to handle the noise better which made it a better choice as a predictive technique.

![](/api/attachments/XWYU2MXG/fulltext/images/dbc476f9e0ce7a60bd818844d956388d284c555621817109782605c9f554f095.jpg)  
Fig. 2. The change in average accuracies of ML and DL techniques with feature selection.

## 6.3. DL based prediction of purchase behavior

Comparing the results of our analysis, we found strong evidence of better performance of DL techniques over conventional ML techniques. The analysis using the DNN improved the accuracy over the widely used RF model by over 6% and ROC-AUC by around 4%. While these im provements might not be significantly large, but its implication for businesses is enormous, given that it would directly translate into improved purchase prediction. Additionally, we found that the FPR decreased by close to 10% when comparing the DT technique with the DNN. The corresponding decrease between the best ML technique (SVM) with DT was 7%. Improvement in false positives is very important for online businesses in this context as it would help them to improve their understanding of the underlying factors affecting the purchase decision. Hence, DNN could be used as a potent tool for businesses to improve their bottom line through better prediction.

However, DNN is more resource-intensive than conventional ML techniques. A slew of methods have been proposed, for example, network pruning and deep compression [60], to reduce the resource overhead without comprising on their performance. These new tech niques involve encoding and removal of less important network weights to generate faster and smaller NN. The use of these techniques makes the DNN suitable for a wide range of practical applications.

## 7. Implications

## 7.1. Academic implications

There are three major academic implications of this study. First, this study bridges the acknowledged need to predict actual purchase instead of purchase intentions [38]. As mentioned earlier, proxies like sales rank [37] have limited business application, and hence it is prudent to focus on retail sales data to develop insights about purchase behavior. We use actual purchase data from a platform and show that it is possible to predict purchase with a high accuracy using DNN.

Secondly, this study compares the usage of multiple advanced analytical techniques for prediction of purchases on an online platform. Previous studies have asserted the importance of advanced analytical techniques for predictive purposes [38]. We adopted a comparative approach to examine the efficacy of DL and ML for the dataset. This examination further supports other studies that have demonstrated the higher predictive power of DL for large datasets [65]. As a result, it provides further empirical evidence to support the superior predictive capabilities of DL in such a context.

Finally, DL has been used in domains like healthcare [41], and sales prediction [34] but not in the area of online retailing. Our research has shown that the DNN was the best performing analytical technique that offered high predictive power for purchases on an online shopping platform. The popular DT technique was found to be close to it in terms of accuracy. Future research can use these insights when using multiple techniques for research in this and other similar domains.

Apart from these contributions, this study advances the extant debate on improving prediction for e-commerce sales. For example, some interesting results from this study like the significance of user account age, rather than the number of past transactions, on consumers’ pur chase opens up new debates on customer loyalty and platform engage ment. This needs to be responded through intensive studies in the future about the impact of customer loyalty (specifically relating to past pur chases) on future purchases.

## 7.2. Managerial implications

Based on the identification of significant predictors of online pur chases. we observe that platform designers should choose to design the online platform for quicker purchase when the competition from other channels and competitive options is high. In such cases, platform arte facts supporting higher engagement may not be a smart choice as it they not lead to a positive purchase decision. Our results also indicate that account age impacts the purchase decision. Hence, if the competition is not very high, awareness of the product is low, and the cost of engagement is not very high, it will be beneficial for businesses to develop long term relationship with all users on the platform.

Finally, our use of customers’ historical data to improve the pre diction of purchases on online e-commerce platforms, also accentuates the need to invest in appropriate infrastructure to control the quality and veracity of sales data. Currently, businesses capture data for a large number of variables and this often raises various privacy concerns. Also, such unorganized data collection strains the organisation’s computa tional resources. Businesses can use the results from this study to streamline their data collection practices and focus only on collecting those data items that can directly predict and influence the customers purchases.

## 8. Conclusion

This study examined predicted the actual purchase behavior of cus tomers on an online platform as a consequence of their interactions with the online platform. For this, it used a unique anonymized web browsing dataset comprised of historical purchase data along with data related to customer engagement with the online e-commerce platform. The study identified two distinct sets of variables, i.e., platform engagement and customer characteristics, as key predictors of purchases. Out of these two categories, we identified four variables, namely the time and day of the week when a session began, duration of a customer’s association with the platform, and days elapsed since last purchase, as the most significant contributors to accurate prediction of a purchase decision. Additionally, the results found that the DNN outperformed other ML techniques when applied on the same dataset. Retailers and e-commerce platform designers can use these findings and integrate them into their existing recommendation engines to improve their predictability. One way to use these findings in such retail IT systems would be to assign greater weightage to these variables in the existing recommendation engines. These, often ignored, platform engagement and customer characteristic variables should improve the accuracy of predictions without major disruption to their ongoing operations. These findings will help improve purchase prediction using DNN on similar platforms.

Despite these insights, this study has some limitations. First, this study is situated in the context of retail sales in a particular e-commerce platform. While the dataset is sufficiently large to allow usage of ML and DL techniques for predicting purchase behavior, a much larger dataset might require some tweaking of the model to further improve its pre dictive capabilities. Second, the data represents the customer behavior in a European online shopping context in a particular product space. Although representative of the context, the findings might not be generalizable across different customer demographics and product types. Further studies across different purchase contexts would be needed to improve the generalizability of the findings. Additionally, such future studies could allow us to analyze the findings and improve them by statistically comparing the performance of various predictive models. Third, this study was not able to compare the predictive accu racy of the model in real-time when the data was generated. This would have allowed us to provide just-in-time recommendations to improve retail sales and would have far superior practical implications. We hope that future studies can adopt such combined approaches that generate real-time recommendations that would have strong business implica tions. Finally, future research can also explore the development of a deep learning-based rule extraction method with applications in related situations and compare its performance with the existing benchmarks.

Author Statement.

The authors do not wish to include any author contribution state ment for the paper.

## References

[1] W.W. Moe, P.S. Fader, Dynamic conversion behavior at e-commerce sites, Manag. Sci, 50 (2004) 326–335, https://doi,org/10.1287/mnsc,1040.0153.

[2] W.W. Moe, Buying, searching, or browsing: differentiating between online shoppers using in-store navigational clickstream, J. Consum. Psychol. 13 (2003) 29–39, https://doi.org/10.1207/S15327663JCP13-1&2\_03.

[3] A.E. Schlosser, T.B. White, S.M. Lloyd, Converting web site visitors into buyers: how web site investment increases consumer trusting beliefs and online purchase intentions, J. Mark. 70 (2006) 133–148, https://doi.org/10.1509/jmkg.70.2.133.

[4] V. Kumar, G. Ramani, T. Bohling, Customer lifetime value approaches and best practice applications, J. Interact. Mark. 18 (2004) 60–72, https://doi.org/ 10.1002/dir.20014

[5] D. Van Den Poel, W. Buckinx, Predicting online-purchasing behaviour, Eur. J. Oper. Res. 166 (2005) 557–575, https://doi.org/10.1016/j.ejor.2004.04.022.

[6] L.F. Jamieson, F.M. Bass, Adjusting stated intention measures to predict trial purchase of new products: a comparison of models and methods, J. Mark. Res. 26 (1989) 336, https://doi.org/10.2307/3172905.

[7] T.R. Rao, Consumer’s purchase decision process: stochastic models, J. Mark. Res. 6 (1969) 321, https://doi.org/10.2307/3150138.

[8] S. Karimi, K.N. Papamichail, C.P. Holland, The effect of prior knowledge and decision-making style on the online purchase decision-making process: a typology of consumer shopping behaviour, Decis. Support. Syst. 77 (2015) 137–147, https:/ doi.org/10.1016/j.dss.2015.06.004

[9] C.K. Prahalad, V. Ramaswamy, Co-creation experiences: the next practice in value creation, J. Interact. Mark. 18 (2004) 5–14, https://doi.org/10.1002/dir.20015.

[10] M. Brown, N. Pope, K. Voges, Buying or browsing? An exploration of shopping orientations and online purchase intention, Eur. J. Mark. 37 (2003) 1666–1684, https://doi.org/10.1108/03090560310495401.

[11] L. Muzellec, E. O’Raghallaigh, Mobile technology and its impact on the consumer decision-making journey how brands can capture the mobile-driven “ubiquitous” moment of truth, J. Advert. Res. 58 (2018) 12–15, https://doi.org/10.2501/JAR-2017-058.

[12] J.W. Palmer, Web site usability, design, and performance metrics, Inf. Syst. Res. 13 (2002).151-167. https://doi.org/10.1287/isre.13.2.151.88.

[13] H.-H. Teo, L.-B. Oh, C. Liu, K.-K. Wei, An empirical study of the effects of interactivity on web user attitude, International Journal of Human-Computer Studies, 58 (2003) 281–305, https://doi,org/10.1016/S1071-5819(03)00008-9

[14] M.M. Alhammad, S.R. Gulliver, Persuasive technology and users acceptance of E commerce: users perceptions of website persuasiveness, J. Electron. Commer. Organ. 12 (2014) 1–13, https://doi.org/10.4018/jeco.2014040101.

[15] H.A.M. Voorveld, G. Van Noort, M. Duijn, Building brands with interactivity: the role of prior brand usage in the relation between perceived website interactivit and brand responses, J. Brand Manag. 20 (2013) 608–622, https://doi.org 10.1057/bm.2013.3

[16] B.H. Ye. A.A. Barreda. F. Okumus. K. Nusair. Website interactivity and brand development of online travel agencies in China: the moderating role of age. J. Bus Res. 99 (2019) 382–389. https://doi,org/10.1016/i,ibusres.2017.09.046.

[17] J. Marbach, C.R. Lages, D. Nunan, Who are you and what do you value? Investigating the role of personality traits and customer-perceived value in online customer engagement, J. Mark. Manag. 32 (2016) 502–525, https://doi.org 10.1080/0267257X.2015.1128472.

[18] J.S. Stewart, E.G. Oliver, K.S. Cravens, S. Oishi, Managing millennials: embracing generational differences, Business Horizons. 60 (2017) 45–54, https://doi.org/ 10.1016/i.bushor.2016.08.011

[19] L. Aksoy, A. van Riel, J. Kandampully, J. Wirtz, A. Den Ambtman, J. Bloemer, C. Horv´ath, B. Ramaseshan, J. Van de Klundert, Z. Gurhan Canli, Managing brands and customer engagement in online brand communities, J. Serv. Manag. 24 (2013) 223–244. https://doi.org/10.1108/09564231311326978.

[20] S. Kagan, R. Bekkerman, Predicting purchase behavior of website audiences, Int. J. Electron. Commer. 22 (2018) 510–539, https://doi,org/10.1080/ 10864415.2018.1485084

[21] N. Ravaja, O. Somervuori, M. Salminen, Predicting purchase decision: the role of hemispheric asymmetry over the frontal cortex, journal of neuroscience, psychology, and, Economics. 6 (2013) 1–13, https://doi.org/10.1037/a0029949.

[22] V. Venkatesh, R. Agarwal, Turning visitors into customers: a usability-centric perspective on purchase behavior in electronic channels, Manag. Sci. 52 (2006) 367–382, https://doi.org/10.1287/mnsc.1050.0442.

[23] C. Sismeiro, R.E. Bucklin, Modeling purchase behavior at an e-commerce web site: a task-completion approach, J. Mark. Res. 41 (2004) 306–323, https://doi.org 10.1509/imkr.41.3.306.35985

[24] A.G. Close, M. Kukar-Kinney, Beyond buying: motivations behind consumers online shopping cart use, J. Bus. Res. 63 (2010) 986–992, https://doi.org/ 10.1016/i,ibusres.2009.01.022.

[25] R. Olbrich, C. Holsing, Modeling consumer purchasing behavior in social shopping communities with clickstream data, Int. J. Electron. Commer. 16 (2011) 15–40, https://doi.org/10.2753/JEC1086-4415160202.

[26] S.L. Gortmaker, D.W. Hosmer, S. Lemeshow, Applied logistic regression, Contemp. Sociol. 23 (1994) 159. https://doi,org/10.2307/2074954.

[27] J.R. Quinlan, Induction of decision trees, Mach. Learn. 1 (1986) 81–106, https:// doi.org/10.1023/A:1022643204877.

[28] L. Breiman, Random forests, Mach. Learn. 45 (2001) 5–32, https://doi.org 10.1017/CB09781107415324.004.

[29] H. Drucker, C.J.C. Surges, L. Kaufman, A. Smola, V. Vapnik, Support vector regression machines, in: Advances in Neural Information Processing Systems, 1997: pp. 155–161.

[30] W.S. McCulloch, W. Pitts, A logical calculus of the ideas immanent in nervous activity, The Bulletin of Mathematical Biophysics. 5 (1943) 115–133. https://doi org/10.1007/BF02478259.

[31] S. Lessmann, B. Baesens, H.V. Seow, L.C. Thomas, Benchmarking state-of-the-art classification algorithms for credit scoring: an update of research, Eur. J. Oper. Res. 247 (2015) 124–136, https://doi.org/10.1016/j.ejor.2015.05.030.

[32] M. Chau, H. Chen, A machine learning approach to web page filtering using content and structure analysis, Decis. Support. Syst. 44 (2008) 482–494, https:// doi.org/10.1016/j.dss.2007.06.002.

[33] S. Dreiseitl, L. Ohno-Machado, Logistic regression and artificial neural network classification models: a methodology review, J. Biomed. Inform. 35 (2002) 352–359, https://doi.org/10.1016/S1532-0464(03)00034-0.

[34] A.L.D. Loureiro, V.L. Migu´eis, L.F.M. da Silva, Exploring the use of deep neural networks for sales forecasting in fashion retail, Decis. Support. Syst. 114 (2018) 81–93. https://doi.org/10.1016/i.dss.2018.08.010.

[35] M. Korpusik, S. Sakaki, F. Chen, Y.Y. Chen, Recurrent neural networks for customer purchase prediction on Twitter, in: CEUR Workshop Proceedings, 2016: pp. 47–50.

[36] M. Mousavizadeh, D.J. Kim, R. Chen, Effects of assurance mechanisms and consumer concerns on online purchase decisions: an empirical study, Decis. Support. Syst. 92 (2016) 79–90, https://doi.org/10.1016/j.dss.2016.09.011.

[37] C. Koças¸, C. Akkan, A system for pricing the sales distribution from blockbusters to the long tail, Decis. Support. Syst. 89 (2016) 56–65, https://doi.org/10.1016/j. dss.2016.06.008.

[38] X. Hu, Q. Huang, X. Zhong, R.M. Davison, D. Zhao, The influence of peer characteristics and technical features of a social shopping website on a consumer’s purchase intention, Int. J. Inf. Manag. 36 (2016) 1218–1230, https://doi.org/ 10.1016/j.ijinfomgt.2016.08.005.

[39] G.A. Morgan, K.C. Barrett, N.L. Leech, G.W. Gloeckner, SPSS for introductory statistics: Use and interpretation (2004), https://doi.org/10.4324/ 9780429287657.

[40] E. Zinovyeva, W.K. Hardle, ¨ S. Lessmann, Antisocial online behavior detection using deep learning, Decision Support Systems. 137 (2020). doi:https://doi.org/10.101 6/j.dss.2020.113362.

[41] H.M. Zolbanin, B. Davazdahemami, D. Delen, A.H. Zadeh, Data analytics for the sustainable use of resources in hospitals: predicting the length of stay for patients with chronic diseases, Information and Management. In Press (2020), https://doi. org/10.1016/j.im.2020.103282.

[42] H. Ahady Dolatsara, Y.J. Chen, C. Evans, A. Gupta, F.M. Megahed, A two-stage machine learning framework to predict heart transplantation survival probabilities over time with a monotonic probability constraint, Decision Support Systems. 137 (2020). doi:https://doi.org/10.1016/j.dss.2020.113363.

[43] Y. Guan, Q. Wei, G. Chen, Deep learning based personalized recommendation with multi-view information integration, Decis. Support. Syst. 118 (2019) 58–69, https://doi.org/10.1016/j.dss.2019.01.003.

[44] Y. Rao, H. Xie, J. Li, F. Jin, F.L. Wang, Q. Li, Social emotion classification of short text via topic-level maximum entropy model. Inf, Manag, 53 (2016) 978–986. https://doi.org/10.1016/i.im.2016.04.005.

[45] Y. Bengio, Gradient-based optimization of hyperparameters, Neural Comput. 12 (2000)1889–1900, https://doi.org/10.1162/089976600300015187.

[46] K.Q. Shen, C.J. Ong, X.P. Li, E.P.V. Wilder-Smith, Feature selection via sensitivity analysis of SVM probabilistic outputs, Mach. Learn. 70 (2008) 1–20, https://doi. org/10.1007/s10994-007-5025-7.

[47] S. Lee, J.Y. Choeh, Predicting the helpfulness of online reviews using multilayer perceptron neural networks, Expert Syst. Appl. 41 (2014) 3041–3046, https://doi. org/10.1016/j.eswa.2013.10.034.

[48] N. Srivastava, G. Hinton, A. Krizhevsky, I. Sutskever, R. Salakhutdinov, Dropout: a simple way to prevent neural networks from overfitting, J. Mach. Learn. Res. 15 (2014) 1929–1958.

[49] D.M.W.D. Powers, Evaluation: from precision, recall and f-factor to ROC, informedness, markedness & correlation, Journal of Machine Learning Technologies. 2 (2011) 37–63. doi:10.1.1.214.9232.

[50] S. Boughorbel, F. Jarray, M. El-Anbari, Optimal classifier for imbalanced data using Matthews Correlation Coefficient metric, PLoS ONE. 12 (2017). doi:https://doi.org /10.1371/journal.pone.0177678

[51] D. Chicco, G. Jurman, The advantages of the Matthews correlation coefficient (MCC) over F1 score and accuracy in binary classification evaluation. BMC Genomics 21 (2020) 6, https://doi.org/10.1186/s12864-019-6413-7.

[52] H. Larochelle, Y. Bengio, J. Louradour, P. Lamblin, Exploring strategies for training deep neural networks, J. Mach. Learn. Res. 10 (2009) 1–40, https://doi.org 10.1145/1577069.1577070

[53] Y. Lecun, Y. Bengio, G. Hinton, Deep learning, Nature. 521 (2015) 436–444, https://doi.org/10.1038/nature14539

[54] B. Kim, J. Park, J. Suh, Transparency and accountability in AI decision support: Explaining and visualizing convolutional neural networks for text information, Decision Support Systems. 134 (2020). doi:https://doi.org/10.1016/j.dss.2020.11 3302.

[55] C. Strobl, A.L. Boulesteix, T. Kneib, T. Augustin, A. Zeileis, Conditional variable importance for random forests, BMC Bioinformatics. 9 (2008) 307, https://doi,org 10.1186/1471-2105-9-307.

[56] I. Iguyon, A. Elisseeff, An introduction to variable and feature selection, J. Mach. Learn. Res. 3 (2003) 1157–1182, https://doi.org/10.1162/153244303322753616.

[57] J.B. Yang, K.Q. Shen, C.J. Ong, X.P. Li, Feature selection via sensitivity analysis of MLP probabilistic outputs, in: Proceedings of the 2008 IEEE Internationa Conference on Systems, Man and Cybernetics, 2008: pp. 774–779. doi:https://doi. org/10.1109/ICSMC.2008.4811372

[58] P. Zhang, A novel feature selection method based on global sensitivity analysi with application in machine learning-based prediction model, Applied Soft Computing Journal. 85 (2019) In Press. doi:https://doi.org/10.1016/j.asoc.20 19.105859.

[59] J. Nascimento, W. Powell, Dynamic programming models and algorithms for the mutual fund cash balance problem, Manag. Sci. 56 (2010) 801–815, https://doi. org/10.1287/mnsc.1100.1143.

[60] Y. He, X. Zhang, J. Sun, Channel pruning for accelerating very Deep Neural Networks, in: Proceedings of the IEEE International Conference on Computer Vision, 2017: pp. 1398–1406. doi:https://doi.org/10.1109/ICCV.2017.155.

[61] N. Chaudhuri, I. Bose, Exploring the role of deep neural networks for post-disaster decision support, Decision Support Systems. 130 (2020). doi:https://doi. org/10.1016/j.dss.2019.113234.

[62] A. Martínez, C. Schmuck, S. Pereverzyev, C. Pirker, M. Haltmeier, A machine learning framework for customer purchase prediction in the non-contractua setting, Eur. J. Oper. Res. 281 (2020) 588–596, https://doi.org/10.1016/j. ejor.2018.04.034.

[63] B.J.D. Jacobs, B. Donkers, D. Fok, Model-based purchase predictions for large assortments, Mark. Sci. 35 (2016) 389–404, https://doi.org/10.1287/ mksc.2016.0985

[64] X. Lu. S. He. S. Lian. S. Ba, J. Wu. Is user-generated content always helpful? The effects of online forum browsing on consumers’ travel purchase decisions, Decision Support Systems. 137 (2020). doi:https://doi.org/10.1016/j.dss.2020.113368.

[65] P.J. Danaher, T.S. Danaher, M.S. Smith, R. Loaiza-Maya, Advertising effectiveness for multiple retailer-brands in a multimedia and multichannel environment, J. Mark. Res. 57 (2020) 445–467, https://doi.org/10.1177/0022243720910104.

[66] A. Poddar, N. Donthu, Y. Wei, Web site customer orientations, web site quality, and purchase intentions: the role of web site personality, J. Bus. Res. 62 (2009) 441–450, https://doi.org/10.1016/j.jbusres.2008.01.036.

[67] G. Zhu, Z. Wu, Y. Wang, S. Cao, J. Cao, Online purchase decisions for tourism e commerce, Electronic Commerce Research and Applications. 38 (2019). doi:https ://doi.org/10.1016/j.elerap.2019.100887.
