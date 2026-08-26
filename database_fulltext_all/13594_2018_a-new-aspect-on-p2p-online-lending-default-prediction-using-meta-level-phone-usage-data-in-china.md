---
otero_id: 13594
otero_key: "CYKH5X3T"
title: "A new aspect on P2P online lending default prediction using meta-level phone usage data in China"
authors: "Lin Ma; Xi Zhao; Zhili Zhou; Yuanyuan Liu"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.05.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

A New Aspect on P2P Online Lending Default Prediction using Meta-level Phone Usage Data in China

Lin Ma, Xi Zhao, Zhili Zhou, Yuanyuan Liu

![](/api/attachments/CYKH5X3T/fulltext/images/7695ae63b44856e6d6d7008ec27d4f09ad54e8cd2ab026527fe42a0e532df957.jpg)

<table><tr><td>PII:</td><td>S0167-9236(18)30083-6</td></tr><tr><td>DOI:</td><td>doi:10.1016/j.dss.2018.05.001</td></tr><tr><td>Reference:</td><td>DECSUP 12952</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>6 November 2017</td></tr><tr><td>Revised date:</td><td>10 May 2018</td></tr><tr><td>Accepted date:</td><td>10 May 2018</td></tr></table>

Please cite this article as: Lin Ma, Xi Zhao, Zhili Zhou, Yuanyuan Liu , A New Aspect on P2P Online Lending Default Prediction using Meta-level Phone Usage Data in China. The address for the corresponding author was captured as affiliation for all authors. Please check if appropriate. Decsup(2018), doi:10.1016/j.dss.2018.05.001

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# A New Aspect on P2P Online Lending Default Prediction using Meta-level Phone Usage Data in China

Lin Ma<sup>a,b</sup>, Xi Zhao<sup>a,c,</sup>∗, Zhili Zhou<sup>a,b</sup>, Yuanyuan Liu<sup>a,b,</sup>∗

<sup>a</sup>School of Management, Xi’an Jiaotong University, Xi’an 710049, China <sup>b</sup>State key Laboratory for Manufacturing Systems Engineering, Xi’an 710049, China <sup>c</sup>Shaanxi Engineering Research Center of Medical and Health Big Data, Xi’an 710049, China

## Abstract

P2P online lending platforms provide services where individuals lend money to others without the involvement of traditional financial institutions. Due to its convenience, the platforms have gained in popularity. However, these platforms may sufer a significant loss if they cannot make good loan decisions based on default prediction results. In this paper, we aim to support the loan decision on P2P platforms based on meta-level phone usage data when the information asymmetry exists for mass borrowers. We extract variables from phone usage data, and use an empirical study to analyze the relationship between these variables and loan default. Then a default prediction method is conducted for P2P lending based on the AdaBoost algorithm. The data used in this study are from the generalized used mobile phones, which make the method applicable to a wide range of users. The empirical study shows that phone usage patterns, including telecommunication patterns, mobility patterns, and App usage patterns contain predictive capability of loan default. The experiments on prediction method demonstrate satisfying performance, which suggests the proposed method has favorable potential being implemented in realworld P2P lending platforms.

Keywords: P2P online lending, meta-level phone usage data, default prediction, AdaBo ost

# ACCEPTED MANUSCRIPT

## 1. Introduction

P2P (peer-to-peer) online lending platforms perform as a hub for connecting individual lenders and borrowers by providing micro-credit services (Boase and Ling, 2013). Benefiting from the elimination of the financial intermediary, P2P lending platforms could provide services with lower charges, more flexible conditions, and quicker loan approvals than traditional lending institutions (Guo et al., 2016; Zhao et al., 2017). These advantages attract individuals and platform investors, promoting a significant growth on P2P platforms especially in developing countries. In China, for example, the number of P2P platforms is 2,307 in 2016, with an annual growth rate of 2.81%. Transaction size has reached 28 trillion RMB, increasing 137% since 2015. (Wang and Xu, 2015).

Though P2P platforms can be prosperous, investments on P2P lending include risks. In P2P platforms, lenders make loan decisions and directly undertake the default losses rather than the platforms. In order to attract more lenders and maintain a steady operation, P2P platforms generally provide additional information about borrowers to support lenders’ loan decisions. Specifically, P2P platforms usually predict loan default probabilities of borrowers based on classification models (Emekter et al., 2015). However, because the commission of small loans is often low, P2P platforms need to reduce the cost of each loan, especially the cost of evaluating the default probability. Thus the trustworthiness of information cannot be guaranteed (Francis et al., 2017). Because some borrowers are unbanked or in countries with imperfect credit scoring systems (Aitken, 2017), their information is often insuficient, which makes it hard for the platforms to make loan decisions. It is therefore necessary for P2P platforms to seek a more reliable data-source and a loan default prediction method with low cost but high accuracy.

Several studies have been conducted in order to reduce default loss in P2P lending. From the method’s aspect, analytic models have been proposed to evaluate the loan default probability (Emekter et al., 2015; Polena and Regner, 2016). These models use various algorithms to predict the default probability, such as logistic regression (Serrano-Cinca et al., 2015), Bayesian network (Wang et al., 2013), random forest classification (Malekipirbazari and Aksakalli, 2015), decision tree (Zhang et al., 2016) and the SVM algorithm (Wang et al., 2016; Maldonado et al., 2017). Meanwhile, some studies focus on developing alternative methods of default prediction. Serrano-Cinca and Guti´errez-Nieto (2016) use profit scoring as an alternative evaluation method for credit scoring. Guo et al. (2016) propose a portfolio optimization strategy for lenders. These methods can reduce the default loss by improving investment performances of lenders.

From the perspective of credit-related data, besides the widely used data (e.g., FICO, credit history, and housing ownership), existing research also relies on soft information to predict default probability. Based on the social network data, Lin et al. (2013) find the relationship between online friendship and loan default risk. By analyzing the social network data, Chen et al. (2016) find that social capital could predict repayment performance. Specifically, borrowers’ structural social capital may have a negative efect on their repayment performances. Zhang et al. (2016) develop a credit scoring model based on social media information. Gonzalez and Loureiro (2014) use characteristics extracted from photos of both lenders and borrowers on the P2P lending decision to analysis the loan success. These studies demonstrate that behavioral-related soft information could be used to predict loan default.

Though the above methods show some predictability of loan default in P2P lending platforms, it is

# ACCEPTED MANUSCRIPT

problematic to directly use them in developing countries for the following reasons. First, these methods rely heavily on credit-related data and are, therefore, inapplicable in developing countries due to the immature credit system, and limited or even missing credit records (Aitken, 2017). Second, the availability and generalizability of using the soft information (e.g., social network data and social capital) cannot be guaranteed. For example, some people may not have network records. Therefore, we need to construct quantitative model to predict the default probability using more general data-sources.

Meta-level mobile phone usage data consist of phone calls, text messages, data trafic, and application programs (Apps) usage records. Notably, meta-level data refer to the log (e.g., locations and timestamps) instead of the content (e.g., detailed texts). These data are (1) authentic because they are automatically recorded, and (2) abundant because mobile phones are frequently used and therefore contain numerous data volume. In addition, phone usage data have already been used to analyze user behaviors, consumption patterns, and economic characteristics (Wu et al., 2007; Renso et al., 2013; Parent et al., 2013; Liu et al., 2015). Thus, meta-level phone usage data have great potential to predict loan default with all these advantages.

The current study conducts empirical analyses on the relationship between phone usage data and loan default behavior in P2P lending. We find three phone usage patterns (telecommunication patterns, mobility patterns, and App usage patterns) that significantly related to loan default. Variables measuring these three patterns were extracted from the raw phone usage data. Then, based on a real-data of 3,027 borrowers with their actual loan records, we further examine these hypotheses using the Mann & Whitney U tests. Based on the empirical results, we create a general and reliable default prediction method for P2P lending platforms using machine learning algorithms. In this method, a comprehensive recursive feature elimination (RFE) method is adapted to select the optimal variable combination from the primitive variables. The AdaBoost algorithm is applied to construct the default prediction model. The experimental results demonstrate that the method has a high precision on identifying the loan default, showing the advantages of using mobile usage data in default prediction. To the best of our knowledge, this is the first study to explain the relationships between phone usage patterns and loan default behavior from the theoretical approach. The main contributions of this study include the following:

1. We explore the relationships between individuals’ daily phone usage behavior and loan performance. The empirical study indicates that the variables derived from phone usage data are powerful in predicting loan default. Thus, the phone usage data could be used to support P2P platforms to make loan decisions.

2. We propose a quantitative method to predict the loan default behavior based on variables extracted from phone usage data. Specifically, we use the RFE method to select the variables to improve the prediction performance. Therefore, the prediction method proposed in the current study can be used to evaluate borrowers with insuficient information in P2P platforms.

3. Using the real-world dataset, we evaluate the predictability of the proposed method by analyzing the predictive power of variables and the performance of the proposed method. These results also indicate that the prediction result of the proposed method may help lenders and P2P platforms to make rational loan decision in reality.

The remainder of the paper is organized as follows. Section 2 presents the hypothesis development, data, variable extraction, and exploratory study. Section 3 introduces the default prediction model and the experiments. Section 4 presents the ethical consideration and practical implications. Finally, conclusions are presented in Section 5.

## 2. Empirical Study

## 2.1. Hypothesis Development

While mobile phones are ubiquitously adopted in the world and make modern life convenient, they also collect individuals’ phone usage data (Madden and Rainie, 2015; Lane et al., 2010). This data, generally used by mobile carriers for billing purpose, have now become a rich data source for logging individuals’ daily behaviors (Harari et al., 2017). Renso et al. (2013) propose methods to infer movement and human behavior from phone usage data. Parent et al. (2013) summarize the approaches on mining behavior from semantic trajectories. Combining situational context, these data enable researchers to further understand individual behavior patterns and to analyze implicit motivation and mental states (Harari et al., 2016). Some researchers find that phone usage data can reflect one’s purchase habits and natural attributes (Wu et al., 2007). Liu et al. (2015) propose a model to extract factors from trajectories and construct the connection between these factors and rationality decisions. And some studies leverage variables extracted from phone usage data to predict regional poverty (Blumenstock et al., 2015; Pokhriyal and Jacques, 2017). All these studies indicate that phone usage data have the potential to reflect individuals behaviors and economic status.

The traditional individual credit scoring relies on ‘4C’ variables, namely the character of the person, the capacity, the capital, and the collateral (Lessmann et al., 2015; Thomas, 2000; Stepanova and Thomas, 2002). Based on previous research, the phone usage data can mainly reflect the character of the person and the capacity. Thus, we mainly consider these two type of variables. In existing default prediction studies, the capacity, which refers to borrowers’ repaying ability (Thomas, 2000), can be described in term of individuals’ economic status (Lessmann et al., 2015; Bravo et al., 2015). The character of the person usually contains demographic information and individual personality traits (Thomas, 2000). Since findings indicate that the economic status and character of individuals relate to some variables in mobile phone usage data, we suggest that the phone usage data contains potential to predict the loan default behavior for P2P platforms.

## 2.1.1. Telecommunication Patterns

One’s telecommunication patterns, which refer to variables describing contacts and social interactions on telecommunications, can reflect his/her economic status (Pokhriyal and Jacques, 2017; S´cepanovi´c<sup>ˇ</sup> et al., 2015). Variables that indicate social connection behaviors, such as interactions per contact (call and text) and entropy of contacts, have a negative relationship with economic status (Blumenstock et al., 2015; Pokhriyal and Jacques, 2017; Soto et al., 2011). And the telecommunication consumption variables, including the number of days that have interaction records (Pokhriyal and Jacques, 2017) and the total number of calls (Frias-Martinez and Virseda, 2012), are positive indicators of economic status.

Economic status has been used as an indicator of individual default prediction in research on individual default behavior in P2P lending platforms (Lessmann et al., 2015; Stepanova and Thomas, 2002). Some studies have found that social capital has a direct connection with default outcome (Agarwal et al., 2011; Putnam, 2000). Based on these literatures, we propose the following hypothesis that:

H1. Telecommunication patterns contain predictability of loan default on P2P lending.

## 2.1.2. Mobility Patterns

Another sign of economic status is individuals’ mobility patterns, which represent the traits of the location accessing behaviors or individuals’ mobility behaviors (Pokhriyal and Jacques, 2017). In studies using phone usage data, individuals’ locations refer to the cell towers’ locations. As depicted in Fig. 1, the communication records are logged when subjects are within the range of the cell tower signal. Thus, the location of cell tower can be considered as the location of subject.

Figure 1: An example of location record in meta-level phone usage data. Points $P _ { 1 } , P _ { 2 } ,$ and $P _ { 3 }$ refer to mobile phones. Point A represents a cell tower, and the signal coverage area is inside the circle. When mobile phones $P _ { 1 }$ , $P _ { 2 }$ , and $P _ { 3 }$ request services, only P and $P _ { 2 }$ can be recorded by cell tower A.

Some studies suggest that activeness can be used as a proxy indicators to estimate economic status. Activeness can be measured from phone usage data in term of the diversity of locations, the physical distance between contacts, the average daily trajectory length, and the radius of gyration (S´cepanovi´c <sup>ˇ</sup> et al., 2015; Frias-Martinez and Virseda, 2012; Eagle et al., 2010). Studies also find that the cell towers density can reflect the economic conditions of an area, and variables reflecting traits of the cell towers that phone users pass by (namely location) can be used to reflect the economic status of individuals. Some of these variables have negative relationships with poverty, including entropy of locations, the number of frequently accessed locations, and a total number of locations in a certain period (Pokhriyal and Jacques, 2017). There are also other variables that may predict economic status, however, the specific impact has not yet been examined (Blumenstock et al., 2015). Based on these findings, we predict that:

H2. Mobility patterns contain predictability of loan default on P2P lending.

## 2.1.3. App Usage Patterns

A great number of Apps have been developed to provide various services to satisfy most daily-needs of users. Researchers suggest that the personality and individual diferences can be derived from the usage patterns of $\mathrm { A p p s }$ (Zhao et al., 2016; Pielot et al., 2015; LiKamWa et al., 2013; Shen et al., 2015). As one dimension of the Big Five Personality, conscientiousness can be inferred from fewer installations of Apps, less frequent usage of Apps, and less time spent on entertainment Apps (Stachl et al., 2017; Chittaranjan et al., 2013; Kim et al., 2015). Agreeableness, another important dimension of personality, can also be reflected by personalization of Apps usage because people high in agreeableness are more likely to use self-presentation functions of personalization Apps (Xu et al., 2016).

Studies on credit analysis find that diferent personality may influence default-related economic behaviors (Bernerth et al., 2012), including planning behaviors, control spending (Perry and Morris, 2005), and debt behaviors (Lea et al., 1995, 1993). Some studies find that conscientiousness positively relates to credit score (Bernerth et al., 2012). Individuals in high conscientiousness are less likely to make rash decisions and mire in financial troubles (Goldberg, 1999; Tokunaga, 1993). Some researchers indicate that agreeableness negatively relates to credit level (Bernerth et al., 2012). High-levels of agreeableness closely relate to the sacrifice of personal resources and promise keeping (Judge et al., 1999).

Based on these findings, it is reasonable to assume the connection between App usage patterns and default behaviors. Therefore, we hypothesize that:

H3. App usage patterns contain predictability of loan default on P2P lending.

## 2.2. Sample and Data

Table 1: The Descriptive Statistic of Individuals

<table><tr><td></td><td>Mean or (%)</td><td>Std.</td></tr><tr><td colspan="3">Borrowers</td></tr><tr><td>Gender</td><td>Female(28%)</td><td></td></tr><tr><td>Age</td><td>28.54</td><td></td></tr><tr><td colspan="3">Average daily mobile phone use</td></tr><tr><td>Phone call log, number</td><td>8.68</td><td>7.36</td></tr><tr><td>Text message log, number</td><td>0.69</td><td>3.1</td></tr><tr><td>Data traffic log, number</td><td>60.31</td><td>64.67</td></tr><tr><td colspan="3">Loan</td></tr><tr><td>P2P online lending Apps, number</td><td>2.24</td><td>1.6</td></tr><tr><td>Default</td><td>36.7%</td><td></td></tr><tr><td>N</td><td>3027</td><td></td></tr></table>

The phone usage data used in this study were provided from one of the largest mobile carries, and their corresponding P2P online records are from one P2P lending company in China. The panel data used in this study includes 3027 subjects. The raw data consist of default records, individuals demographic information and telecommunication service records, which contain phone calls, text messages, and data trafic. The name, ID, and phone numbers of subjects are encrypted to protect their privacy, making it impossible to identify the subject. The phone usage data contains subjects’ behavior records before the loan default occurs. The form of raw data is meta-level, which is analogous to the information on the envelope. The statistical analysis of these data for each individual is shown in Table 1. Among these subjects, 1111 (36.7%) have default records, and the average age is 28.54. The average number of daily phone calls is 8.68, the number of text messages is only 0.69, and the number of data trafic is 60.31. The gap between the two communication functions results from the fact that online social Apps can provide the alternative function of messages. Note that the average installed number of P2P online lending Apps is 2.24, which means one subject uses 2 to 3 P2P lending Apps on average. It is necessary to consider their performance on other platforms.

## 2.3. Variables

As introduced in section 2, diferent categories of variables extracted from phone usage data contain probability of default in P2P lending. Following these theory backgrounds, in addition to the existing variable pools on mobile data surveyed comprehensively (Harari et al., 2017, 2016), and characteristics

# ACCEPTED MANUSCRIPT

of our data, we extract the primitive variables from telecommunication patterns, mobility patterns, App usage patterns, demographics, and telecommunication records. Since the total number of these variables is large, we categorize the variables according to the data type and only present variable clusters based on the type of variables. Due to the large volume of data, we use MapReduce to carry out the extraction process.

Telecommunication Patterns: The telecommunication patterns represent the contacts and interactions on telecommunications networks. The extracted variables are separated into three variable sets.

Contacts variables include number of contacts and the contacts’ regularity of phone calls (T1, T2) and text messages (T3, T4). In order to have a quantitative measure of the regularity, we introduce the concept of information entropy(Mceliece, 2002). The higher the value is, the lower the regularity is. For each subject i and communication function j (phone calls or text messages), their contacts’ regularity is:

$$
v _ {i j} = - \sum_ {x \in X} p (x) \log (p (x))\tag{1}
$$

where X is the set of contacts, and p(x) is the probability that contact x occurs in phone calls or text messages.

Usage Time variables capture the usage time of telecommunications. The first set contains the statistics of usage time on phone calls, text messages, and the sum of phone calls and messages, including the average (T5, T12, T19), the variance (T6, T13, T20), the maximum (T7, T14, T21), and the minimum (T8, T15, T22) number of usage frequency in one day, and the number of days that have records (T11, T18, T23). Then the regularity of usage time of phone calls (T9, T10) and text messages (T16, T17) are extracted from day periodic and month periodic. For a given day, we separated 24 hours into five time slots, which consists of midnight (12am - 8am), forenoon (8am - 12 noon), noon (12 noon - 2pm), afternoon (2pm - 6pm), and night (6pm - 12am). For a given month, the variable is calculated by day interval. In each time slot, the ratio of communication is calculated and the regularity variables are extracted. Moreover, the number (T27) and the proportion (T28) of communications during the night are extracted.

Interval variables refers to the time interval between two interactions. The interval variable set consists of statistics of the interval on successive communications, including the average (T24), the variance (T25), and the maximum (T26) number of intervals.

Mobility Patterns: Based on the data structure of subjects, the locations (BTS) with time stamps can be obtained from phone calls and data trafic. From these data, the average number of locations where phone calls occurred in one day (M1), the average number (M2), the variance (M3), the maximum (M4), and the minimum (M5) of location are extracted. Next, by considering the sum of locations where phone calls and data trafic occurred, the sum of activity locations (M8), the range of locations (M11), and the number of locations that individuals frequently access are extracted (M12). Then, the regularity of locations from phone calls (M6), data trafic (M7), and the sum of phone calls and data trafic (M9) are extracted as Eq.(1), where X refers to the set of locations that communications ever occurred and $p ( x )$ represents the proportion of location x. Meanwhile, by analyzing the frequency and time stamps of communications’ occurrence at diferent locations, the distances between home and workplace can be

# ACCEPTED MANUSCRIPT

calculated (M10).

App Usage Patterns: App usage behaviors are describing the main operation behaviors in mobile phones, including the access behaviors and the data trafic spent on these Apps. As introduced in Section 2, these variables can reflect individuals’ personalities. Specifically, payment, financial, and P2P online lending Apps usage variables are extracted to reflect the diferent operation preference on economic behaviors services Apps. The variables are separated into four sets.

People may behave diferently in App usage on both the operation behaviors and App preference (Liu et al., 2017). For operation behaviors on Apps, the average (A1), the variance (A2), the maximum (A3), the minimum (A4) number of usage frequency in one day, the average usage time regularity per day (A5) and per month (A6), and the number of days that have records (A7) are considered. For App preference, the number of installed Apps (A8), the categories of installed Apps (A9), statistics of usage frequency of Apps, including the total (A10), the average (A11), the variance (A12), the maximum (A13), the minimum (A14) usage frequency, and the regularity of usage access (A15) are considered.

Data trafic spent on diferent time units is diverse in diferent individuals. Here, the sum (A16), the average (A17), the variance (A18), the maximum (A19), the minimum (A20) data trafic spent, and the regularity (A21) of data trafic spent are considered to describe these traits.

By analyzing operation records on financial & payment Apps, individuals’ consumption preference can be recognized. While the former consist of mobile bank Apps and third-party payment Apps, the latter include investment Apps and P2P online lending Apps. We extract variables from these two types of Apps as well as the overall consideration of these two types. For each set, the extracted variables include the number of installed Apps (A22, A27, A32), the proportion of Apps (A23, A28, A33), the number of Apps belonging to the top five installed financial (or payment) Apps (A24, A29, A34), the number of Apps belonging to the top five frequently used Apps of the user (A25, A30, A35), and the number of Apps belonging to the top five data trafic spent on Apps of the user (A26, A31, A36).

P2P online lending Apps, serving as mobile terminals of P2P lending platforms, can provide convenient services for consumers. In order to describe the traits of P2P lending, the number of installed Apps (A37), the proportion of P2P lending Apps (A38), the average number of access times per day (A39) and the average data trafic spent on lending Apps (A40) are extracted. Moreover, App choices are diferent in diferent types of people. We quantify this trait by the TF-IDF algorithm (Oren, 2002), which can express the minority preferences of each individual.

$$
w _ {t} = \sum_ {i} \frac {d _ {i}}{| D |} \left(\log \frac {| N |}{| j : t _ {i} \in d _ {j} |} + 1\right)\tag{2}
$$

Where $| N |$ refers to the total number of people, $| j : t _ { i } \in d _ { j } |$ refers to the number of individuals that use the Apps i. When t = 0, $w _ { t }$ represents the preference variable on frequency (A41), $d _ { i }$ refers to usage frequency of App i. When t = 1, $w _ { t }$ refers to the preference variable on data trafic (A42), $d _ { i }$ refers to data trafic spent on App i.

Demographic & Telecommunication Services: Demographic variables and telecommunication service variables can be directly obtained from raw phone usage data. The raw phone usage data contains age (D1), gender (D2), telecommunication services shutdown times in the last year (D3), total data trafic used in the last year (D4), total expenditure on the mobile phone in the last year (D5), and the number

Table 2: Exploratory study on variables from telecommunication patterns, mobility patterns, and demographic

<table><tr><td rowspan="2">Variables</td><td colspan="3">Non-default (N=1900)</td><td colspan="3">Default (N=1099)</td><td rowspan="2">Spearman</td><td rowspan="2">p-value</td></tr><tr><td>Mean</td><td>Median</td><td>Std.</td><td>Mean</td><td>Median</td><td>Std.</td></tr><tr><td colspan="9">Telecommunication Patterns</td></tr><tr><td>T1</td><td>15.11</td><td>11</td><td>18.09</td><td>15.27</td><td>9</td><td>27.46</td><td>0.037*</td><td>0.362(&gt;0.05)</td></tr><tr><td>T2</td><td>2.46</td><td>2.58</td><td>1.35</td><td>2.35</td><td>2.5</td><td>1.41</td><td>0.042*</td><td>0.049(&lt;0.05)</td></tr><tr><td>T3</td><td>0.1</td><td>0</td><td>0.53</td><td>0.07</td><td>0</td><td>0.29</td><td>0.017</td><td>0.069(&gt;0.05)</td></tr><tr><td>T4</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>T5</td><td>2.09</td><td>2.06</td><td>0.6</td><td>8.65</td><td>2.06</td><td>7.54</td><td>0.032</td><td>0.131(&gt;0.05)</td></tr><tr><td>T6</td><td>3.31</td><td>3.26</td><td>1.07</td><td>3.33</td><td>3.35</td><td>1.18</td><td>-0.015</td><td>0.019(&lt;0.05)</td></tr><tr><td>T7</td><td>25.71</td><td>21</td><td>17.12</td><td>26.55</td><td>22</td><td>20.31</td><td>-0.001</td><td>0.460(&gt;0.05)</td></tr><tr><td>T8</td><td>0.8</td><td>0</td><td>1.67</td><td>0.77</td><td>0</td><td>1.63</td><td>0.031</td><td>0.000(&lt;0.01)</td></tr><tr><td>T9</td><td>1.93</td><td>1.93</td><td>0.14</td><td>1.93</td><td>1.95</td><td>0.17</td><td>-0.021</td><td>0.121(&gt;0.05)</td></tr><tr><td>T10</td><td>4.49</td><td>4.57</td><td>0.34</td><td>4.33</td><td>4.52</td><td>0.61</td><td>0.11**</td><td>0.000(&lt;0.01)</td></tr><tr><td>T11</td><td>28.46</td><td>30</td><td>3.81</td><td>26.76</td><td>29</td><td>6.18</td><td>0.103**</td><td>0.000(&lt;0.01)</td></tr><tr><td>T12</td><td>0.37</td><td>0.23</td><td>0.41</td><td>0.43</td><td>0.28</td><td>0.47</td><td>-0.059**</td><td>0.000(&lt;0.01)</td></tr><tr><td>T13</td><td>0.81</td><td>0.38</td><td>1.06</td><td>0.99</td><td>0.53</td><td>1.21</td><td>-0.062**</td><td>0.000(&lt;0.01)</td></tr><tr><td>T14</td><td>6.25</td><td>3</td><td>11.69</td><td>7.77</td><td>4</td><td>15.03</td><td>-0.065**</td><td>0.000(&lt;0.01)</td></tr><tr><td>T15</td><td>0</td><td>0</td><td>0.05</td><td>0</td><td>0</td><td>0</td><td>0.027</td><td>0.001(&lt;0.01)</td></tr><tr><td>T16</td><td>1.15</td><td>1.35</td><td>0.68</td><td>1.18</td><td>1.4</td><td>0.7</td><td>-0.037*</td><td>0.000(&lt;0.01)</td></tr><tr><td>T17</td><td>1.85</td><td>1.92</td><td>1.18</td><td>1.92</td><td>2</td><td>1.21</td><td>-0.36*</td><td>0.000(&lt;0.01)</td></tr><tr><td>T18</td><td>6.1</td><td>4</td><td>5.52</td><td>6.66</td><td>5</td><td>5.7</td><td>-0.48*</td><td>0.000(&lt;0.01)</td></tr><tr><td>T19</td><td>9.33</td><td>7.52</td><td>6.89</td><td>9.47</td><td>7.52</td><td>8.28</td><td>0.022</td><td>0.667(&gt;0.05)</td></tr><tr><td>T20</td><td>3.47</td><td>3.42</td><td>1.1</td><td>3.54</td><td>3.49</td><td>1.22</td><td>-0.31</td><td>0.000(&lt;0.01)</td></tr><tr><td>T21</td><td>28.38</td><td>24</td><td>19.98</td><td>30.53</td><td>24</td><td>26.12</td><td>-0.2</td><td>0.001(&lt;0.01)</td></tr><tr><td>T22</td><td>0.9</td><td>0</td><td>1.77</td><td>0.81</td><td>0</td><td>1.67</td><td>0.045*</td><td>0.000(&lt;0.01)</td></tr><tr><td>T23</td><td>28.65</td><td>30</td><td>3.61</td><td>27.01</td><td>29</td><td>5.95</td><td>0.109**</td><td>0.000(&lt;0.01)</td></tr><tr><td>T24</td><td>4931.94</td><td>4615.81</td><td>2024.15</td><td>4862.58</td><td>4505.7</td><td>2203.28</td><td>0.026</td><td>0.014(&lt;0.05)</td></tr><tr><td>T25</td><td>5.80E+07</td><td>4.71E+07</td><td>4.26E+07</td><td>6.13E+07</td><td>4.73E+07</td><td>5.60E+07</td><td>-0.011</td><td>0.404(&gt;0.05)</td></tr><tr><td>T26</td><td>43285.3</td><td>40726</td><td>13080.65</td><td>43179.06</td><td>41025</td><td>13340.68</td><td>-0.026</td><td>0.031(&lt;0.05)</td></tr><tr><td>T27</td><td>63.33</td><td>49</td><td>53.17</td><td>66.69</td><td>51</td><td>61.04</td><td>-0.01</td><td>0.007(&lt;0.01)</td></tr><tr><td>T28</td><td>0.24</td><td>0.23</td><td>0.11</td><td>0.25</td><td>0.24</td><td>0.11</td><td>-0.07**</td><td>0.000(&lt;0.01)</td></tr><tr><td colspan="9">Mobility Patterns</td></tr><tr><td>M1</td><td>64.71</td><td>49</td><td>56.15</td><td>63.07</td><td>47</td><td>60.4</td><td>0.04*</td><td>0.304(&gt;0.05)</td></tr><tr><td>M2</td><td>5.39</td><td>4.02</td><td>4.28</td><td>5.64</td><td>4.04</td><td>7.25</td><td>0</td><td>0.273(&gt;0.05)</td></tr><tr><td>M3</td><td>4.49</td><td>4.44</td><td>1.56</td><td>4.39</td><td>4.36</td><td>1.65</td><td>0.027</td><td>0.001(&lt;0.01)</td></tr><tr><td>M4</td><td>4.14</td><td>4.13</td><td>0.79</td><td>4.14</td><td>4.11</td><td>0.81</td><td>0.005</td><td>0.066(&gt;0.05)</td></tr><tr><td>M5</td><td>0.84</td><td>0.69</td><td>1.09</td><td>0.81</td><td>0.69</td><td>1.08</td><td>0.026</td><td>0.000(&lt;0.01)</td></tr><tr><td>M6</td><td>4.1</td><td>4.16</td><td>1.29</td><td>4.01</td><td>4.11</td><td>1.35</td><td>0.032</td><td>0.300(&gt;0.05)</td></tr><tr><td>M7</td><td>4.02</td><td>4.16</td><td>1.57</td><td>3.84</td><td>4.03</td><td>1.68</td><td>0.048*</td><td>0.000(&lt;0.01)</td></tr><tr><td>M8</td><td>202.02</td><td>169</td><td>145.52</td><td>186.98</td><td>154</td><td>149.32</td><td>0.072**</td><td>0.000(&lt;0.01)</td></tr><tr><td>M9</td><td>4.75</td><td>4.76</td><td>1.27</td><td>4.61</td><td>4.66</td><td>1.36</td><td>0.046*</td><td>0.000(&lt;0.01)</td></tr><tr><td>M10</td><td>4.49</td><td>6.21</td><td>4.19</td><td>4.33</td><td>5.84</td><td>4.2</td><td>0.019</td><td>0.000(&lt;0.01)</td></tr><tr><td>M11</td><td>37741.35</td><td>33203.5</td><td>29485.68</td><td>37066.45</td><td>30814.09</td><td>31226.31</td><td>0.026</td><td>0.482(&gt;0.05)</td></tr><tr><td>M12</td><td>24.5</td><td>16</td><td>29.72</td><td>23.52</td><td>14</td><td>30.02</td><td>0.038*</td><td>0.127(&gt;0.05)</td></tr><tr><td colspan="9">Demographic</td></tr><tr><td>D1</td><td>28.68</td><td>28</td><td>5.92</td><td>28.3</td><td>27</td><td>5.94</td><td>0.03</td><td>0.000(&lt;0.01)</td></tr><tr><td>D2</td><td>1359 (male)</td><td></td><td></td><td>805 (male)</td><td></td><td></td><td>0.017</td><td>0.255(&gt;0.05)</td></tr></table>

The correlation is significance on 0.01. The correlation is significance on 0.05.  
p value is extracted by Mann & Whitney U test.  
The message contacts regularity (T4) is omitted caused by the data sparseness.

Table 3: Exploratory study on App usage patterns and telecommunication records (Continue to Table 2)

<table><tr><td rowspan="2">Variables</td><td colspan="3">Non-default (N=1900)</td><td colspan="3">Default (N=1099)</td><td rowspan="2">Spearman</td><td rowspan="2">p-value</td></tr><tr><td>Mean</td><td>Median</td><td>Std.</td><td>Mean</td><td>Median</td><td>Std.</td></tr><tr><td colspan="9">App Usage Patterns</td></tr><tr><td>A1</td><td>62.53</td><td>57.13</td><td>64.06</td><td>56.47</td><td>54.52</td><td>33.39</td><td>0.058**</td><td>0.000(&lt; 0.01)</td></tr><tr><td>A2</td><td>6.72</td><td>6.72</td><td>1.52</td><td>6.71</td><td>6.73</td><td>1.58</td><td>-0.009</td><td>0.347(&gt;0.05)</td></tr><tr><td>A3</td><td>191.11</td><td>146</td><td>208.91</td><td>183.3</td><td>142</td><td>183.98</td><td>0.025</td><td>0.019(&lt; 0.05)</td></tr><tr><td>A4</td><td>18.99</td><td>20</td><td>16.415</td><td>14.9</td><td>10</td><td>15.59</td><td>0.124**</td><td>0.000(&lt; 0.01)</td></tr><tr><td>A5</td><td>2.1</td><td>2.14</td><td>0.16</td><td>2.1</td><td>2.14</td><td>0.21</td><td>0.02</td><td>0.134(&gt;0.05)</td></tr><tr><td>A6</td><td>4.54</td><td>4.76</td><td>0.65</td><td>4.41</td><td>4.69</td><td>0.81</td><td>0.118**</td><td>0.000(&lt; 0.01)</td></tr><tr><td>A7</td><td>29.05</td><td>31</td><td>5.47</td><td>27.93</td><td>31</td><td>6.69</td><td>0.131**</td><td>0.000(&lt; 0.01)</td></tr><tr><td>A8</td><td>85.58</td><td>86</td><td>38.24</td><td>85.83</td><td>82</td><td>35.55</td><td>0.02</td><td>0.961(&gt;0.05)</td></tr><tr><td>A9</td><td>7.64</td><td>8</td><td>0.92</td><td>7.74</td><td>8</td><td>0.89</td><td>-0.067**</td><td>0.000(&lt; 0.01)</td></tr><tr><td>A10</td><td>55280.55</td><td>38592</td><td>62253.53</td><td>58183.08</td><td>41526</td><td>56415.46</td><td>-0.034</td><td>0.000(&lt; 0.01)</td></tr><tr><td>A11</td><td>549.37</td><td>443.24</td><td>530.66</td><td>579.34</td><td>478.14</td><td>446.51</td><td>-0.045*</td><td>0.000(&lt; 0.01)</td></tr><tr><td>A12</td><td>13.86</td><td>14.24</td><td>2.53</td><td>14.02</td><td>14.43</td><td>2.53</td><td>-0.044*</td><td>0.000(&lt; 0.01)</td></tr><tr><td>A13</td><td>8.79</td><td>8.98</td><td>0.04</td><td>8.88</td><td>9.08</td><td>1.45</td><td>-0.035*</td><td>0.000(&lt; 0.01)</td></tr><tr><td>A14</td><td>1.02</td><td>1</td><td>0.13</td><td>1.06</td><td>1</td><td>0.89</td><td>-0.016</td><td>0.026(&lt; 0.05)</td></tr><tr><td>A15</td><td>3.89</td><td>4.01</td><td>0.63</td><td>3.86</td><td>3.98</td><td>0.65</td><td>0.025</td><td>0.001(&lt; 0.01)</td></tr><tr><td>A16</td><td>20.15</td><td>20.43</td><td>1.96</td><td>20.21</td><td>20.47</td><td>1.99</td><td>-0.019</td><td>0.052(&gt;0.05)</td></tr><tr><td>A17</td><td>15.82</td><td>15.95</td><td>1.51</td><td>15.87</td><td>16.01</td><td>1.56</td><td>-0.023</td><td>0.038(&lt; 0.05)</td></tr><tr><td>A18</td><td>34.35</td><td>34.66</td><td>3.79</td><td>34.47</td><td>34.77</td><td>4.06</td><td>-0.024</td><td>0.014(&lt; 0.05)</td></tr><tr><td>A19</td><td>19.16</td><td>19.36</td><td>2.06</td><td>19.25</td><td>19.42</td><td>2.1</td><td>-0.025</td><td>0.011(&lt; 0.05)</td></tr><tr><td>A20</td><td>5.15</td><td>4.99</td><td>0.65</td><td>5.16</td><td>4.99</td><td>0.73</td><td>0.03</td><td>0.698(&gt;0.05)</td></tr><tr><td>A21</td><td>2.92</td><td>3.07</td><td>0.89</td><td>2.85</td><td>2.99</td><td>0.92</td><td>0.035*</td><td>0.000(&lt; 0.01)</td></tr><tr><td>A22</td><td>4.78</td><td>4</td><td>3.43</td><td>4.78</td><td>4</td><td>3.66</td><td>0.011</td><td>0.943(&gt;0.05)</td></tr><tr><td>A23</td><td>0.05</td><td>0.05</td><td>0.03</td><td>0.05</td><td>0.05</td><td>0.03</td><td>0.016</td><td>0.997(&gt;0.05)</td></tr><tr><td>A24</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>A25</td><td>0.06</td><td>0</td><td>0.24</td><td>0.06</td><td>0</td><td>0.26</td><td>0.09</td><td>0.982(&gt;0.05)</td></tr><tr><td>A26</td><td>0.06</td><td>0</td><td>0.26</td><td>0.05</td><td>0</td><td>0.24</td><td>0.06</td><td>0.157(&gt;0.05)</td></tr><tr><td>A27</td><td>5.25</td><td>5</td><td>2.83</td><td>4.85</td><td>4</td><td>2.66</td><td>0.068**</td><td>0.000(&lt; 0.01)</td></tr><tr><td>A28</td><td>0.06</td><td>0.06</td><td>0.04</td><td>0.06</td><td>0.05</td><td>0.04</td><td>0.091**</td><td>0.000(&lt; 0.01)</td></tr><tr><td>A29</td><td>1.29</td><td>1</td><td>0.95</td><td>0.79</td><td>1</td><td>0.76</td><td>0.257**</td><td>0.000(&lt; 0.01)</td></tr><tr><td>A30</td><td>0.32</td><td>0</td><td>0.49</td><td>0.29</td><td>0</td><td>0.48</td><td>0.035*</td><td>0.174(&gt;0.05)</td></tr><tr><td>A31</td><td>0.31</td><td>0</td><td>0.54</td><td>0.27</td><td>0</td><td>0.49</td><td>0.03</td><td>0.637(&gt;0.05)</td></tr><tr><td>A32</td><td>10.03</td><td>9</td><td>5.62</td><td>9.63</td><td>9</td><td>5.78</td><td>0.044*</td><td>0.000(&lt; 0.01)</td></tr><tr><td>A33</td><td>0.12</td><td>0.11</td><td>0.05</td><td>0.11</td><td>0.11</td><td>0.06</td><td>0.065**</td><td>0.000(&lt; 0.01)</td></tr><tr><td>A34</td><td>1.29</td><td>1</td><td>0.95</td><td>0.79</td><td>1</td><td>0.76</td><td>0.257**</td><td>0.000(&lt; 0.01)</td></tr><tr><td>A35</td><td>0.38</td><td>0</td><td>0.56</td><td>0.34</td><td>0</td><td>0.541</td><td>0.034*</td><td>0.363(&gt;0.05)</td></tr><tr><td>A36</td><td>0.37</td><td>0</td><td>0.61</td><td>0.32</td><td>0</td><td>0.57</td><td>0.034</td><td>0.567(&gt;0.05)</td></tr><tr><td>A37</td><td>2.24</td><td>2</td><td>1.55</td><td>2.25</td><td>2</td><td>1.7</td><td>0.013</td><td>0.618(&gt;0.05)</td></tr><tr><td>A38</td><td>0.03</td><td>0.02</td><td>0.02</td><td>0.02</td><td>0.02</td><td>0.02</td><td>0.014</td><td>0.380(&gt;0.05)</td></tr><tr><td>A39</td><td>2.64</td><td>0</td><td>2.98</td><td>2.19</td><td>0</td><td>2.85</td><td>0.073**</td><td>0.000(&lt; 0.01)</td></tr><tr><td>A40</td><td>6.47</td><td>0</td><td>7.02</td><td>5.5</td><td>0</td><td>6.88</td><td>0.065**</td><td>0.000(&lt; 0.01)</td></tr><tr><td>A41</td><td>0.64</td><td>0</td><td>0.74</td><td>0.59</td><td>0</td><td>0.81</td><td>0.05**</td><td>0.000(&lt; 0.01)</td></tr><tr><td>A42</td><td>0.78</td><td>0</td><td>0.92</td><td>0.72</td><td>0</td><td>0.99</td><td>0.05**</td><td>0.000(&lt; 0.01)</td></tr><tr><td colspan="9">Telecommunication Records</td></tr><tr><td>D3</td><td>0.19</td><td>0</td><td>0.72</td><td>0.22</td><td>0</td><td>0.71</td><td>-0.036*</td><td>0.036(&lt; 0.05)</td></tr><tr><td>D4</td><td>3.43E+10</td><td>2.55E+10</td><td>8.53E+08</td><td>3.50E+10</td><td>2.41E+10</td><td>4.06E+10</td><td>2.50E-02</td><td>0.000(&lt; 0.01)</td></tr><tr><td>D5</td><td>1992.37</td><td>1796.17</td><td>1124.8</td><td>1981.13</td><td>1773.54</td><td>1158.03</td><td>0.008</td><td>0.099(&gt;0.05)</td></tr><tr><td>D6</td><td>0.1</td><td>0</td><td>0.9</td><td>0.36</td><td>0</td><td>3.63</td><td>-0.036*</td><td>0.000(&lt; 0.01)</td></tr></table>

∗∗ <sup>The</sup> <sup>correlation</sup> <sup>is</sup> <sup>significance</sup> <sup>on</sup> <sup>0.01.</sup> ∗ <sup>The</sup> <sup>correlation</sup> <sup>is</sup> <sup>significance</sup> <sup>on</sup> <sup>0.05.</sup>10  
p value is extracted by Mann & Whitney U test.  
The number of installed Apps belonging to the Top 5 financial Apps (T4) is omitted caused by the data sparseness.

of international roaming days in the last year (D6).

## 2.4. Exploratory Analysis

Raw phone usage data contains data quality issues, such as missing data and atypical values. Thus, we perform data preprocessing before exploratory analysis. For handling missing data, 28 subjects have been excluded when more than two variables cannot be extracted from their raw data due to missing data. Then, we tested the existence of atypical values for variables, defined as values falling into the range beyond two standard deviation from the mean of variables (Maddala and Lahiri, 1992). Logarithm function has been adopted to transform the variables with atypical value. 2,999 subjects are included in the analysis. 1,099 are the default (36.6%) and 1,900 are the non-default (63.4%).

The exploratory study of the extracted variables is shown in Table 2 and Table 3. The first columns show the mean, the median and the standard deviation in both default and non-default people. The subsequent columns show the relationship between the variables and default behavior. Since the values of the variables are not satisfied with normal distributions, we use the Spearman test to analyze the correlation between variables and phone usage variables. As expected, there exist variables wherein the correlations are statistically significant in diferent categories. The most remarkable variable is the number of days that have telecommunication records (T23, 0.109) in telecommunication patterns, the sum of locations (M8, 0.072) in mobility patterns, and the number of payment Apps belonging to the top five payment Apps (A34, 0.257). The remaining variables of the correlation coeficients are significant but the magnitudes are not high.

The last columns display the significant results of asymptotic 2-tailed Mann & Whitney U test (Kasuya, 2001). This test is used to identify if there is a significant diference in two categories when values of variables are not satisfied with normal distributions. As expected, diferences are significant in some of the variables which belong to three patterns respectively $\left( p < 0 . 0 5 \right)$ . Note that the usage time (A39) and the data trafic spent (A40) on P2P lending Apps are statistically significant, which indicates that the usage behaviors in the P2P lending Apps may difer in default or non-default borrowers.

To sum up, within the exploratory analysis, the hypotheses can be partially accepted: there are variables belonging to telecommunication patterns, mobility patterns, and App usage patterns which contain predictability of loan default on P2P lending. Thus, we can use these variables to conduct default prediction on P2P lending.

## 3. Proposed Method

Since the variables extracted are used to predict the default on P2P lending platforms, it is necessary to assess the predictive power of the variables and propose a default model. As tested in Section 2, some of the variables may not contain the predictability of loan default behavior, we apply a synthetic recursive variable elimination algorithm to select efective variables from the primitive variable set. Then, we use the selected variables to conduct the default prediction model. At last, the experiments are conducted to evaluate the prediction eficiency of the proposed method.

# ACCEPTED MANUSCRIPT

## 3.1. Variable Selection

Finding efective variables is essential for improving the precision of recognizing default subjects. We apply the RFE to select variables (De Martino et al., 2008), which recursively tests the efect of smaller sets from the primitive variable set. However, a bias exists in the feature elimination process due to randomly selecting variables and samples. Thus, we apply a synthetic method to select variables from the multiple RFE results. The variable selection process is performed as Algorithm 1.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 Variable Selection Based on RFE
Input: F: The set of primitive variables extracted from raw meta-level phone usage data; R: Number of training rounds; β: The proportion of select times.
Output: List of selected variables.
1: repeat
2: Train one RFE to get the selected variable list  $L_{i}$  of F.
3: until i &lt; R
4: For each variable in F, calculate the total times existing on variable list  $L_{i}$ , and rank the variable list F by the selected frequency.
5: Select the variables with frequency on the variable list is larger than  $\beta \times R$ .
6: return Selected variable list  $F_{S}$ .
</div>

Figure 2: Variable selected result. The x-axis is the primitive variables, and the y-axis is the number of selected times in Algorithm 1. Variables above the red line are selected.

We define the training round as $R = 5 0 0$ , and the proportion as $\beta = 0 . 2$ , which means the variable is selected by at least 20 percent of training rounds. The selected result is depicted in Fig. 2. Due to the sited $\beta = 0 . 2$ , the selected variables need to satis $\mathrm { f y }$ the condition of the chosen times being equal to or larger than $\beta \times R = 0 . 2 \times 5 0 0 = 1 0 0$ , which is presented by the space above the red line in the figure. Overall, we obtained 41 variables from primitive variables.

In order to evaluate whether the selected variables are enough to represent diferent characteristics of subjects, we used AdaBoost (Freund and Schapire, 1997) to test the model performances based on the diferent amounts of variables. As the number of variables is decided by $\beta ,$ the problem is equal to the performance on diferent $\beta .$ When $\beta$ grows, the number of selected variables decreases, which is a result of the selection conditions becoming rigorous. When $\beta = 0$ , all primitive variables are selected. When $\beta = 0 . 8$ , only three variables satisfy the condition that they are selected by at least 400 rounds of RFE.

Figure 3: Model accuracy on diferent proportion of select times in Algorithm 1. The x-axis is the proportion of select times, and the y-axis is the model accuracy. The solid line depicts the accuracy of model on training samples. The dashed line depicts the accuracy of the model on testing samples.

The model performances are depicted in Fig. 3. The accuracy of models on training samples is decreased with the growth of $\beta ,$ but the performance of the model on testing samples grows until $\beta =$ 0.2. This means that the generality of the model increase when neglecting those variables with less distinguishing power. However, when $\beta$ grows over 0.2, the remaining variables are insuficient to identify

# ACCEPTED MANUSCRIPT

diferent persons. These results satisfy the Pareto principle (Pareto, 1964), where variable selected by at least 20% RFE training rounds may contain enough information to satisfy the distinguish requirements.

## 3.2. Default Prediction Model

## 3.2.1. Model

A default prediction model is adapted to detect the borrowers’ future performance in loan repayment. We apply an adaptive boosting (AdaBoost) algorithm (Freund and Schapire, 1997), which is used as a classification model, to solve the default prediction problem. The AdaBoost algorithm is an iterative algorithm, which uses multiple weak learners to train the same sample set, and combines the training results to obtain the final classifier. Each iterative in AdaBoost justifies the weight of samples according to the error rate of the former training learner. Due to the limit on the error rate of the samples, the final classifier can achieve a stable state. Thus, the precision and generality can be mutually exclusive in AdaBoost.

In the default prediction model, the sample is defined as $D = ( X _ { 1 } , y _ { 1 } ) , . . . , ( X _ { i } , y _ { i } ) , ( X _ { m } , y _ { m } )$ , where $X _ { i }$ represents variables extracted from phone usage data; y refers to the binary classification (0, 1). When $y = 1 ,$ , i represents a person with non-default record, and when $y = 0$ , i represents a person with default records on loan repayment.

Decision trees are used as weak learners, each learner is defined as $h _ { t } ( x )$ , where $t \in ( 1 , T )$ . T is the total number of weak learners, which is designated as forest size. The weight of each learner is defined as:

$$
\alpha_ {t} = \frac {1}{2} l o g \frac {1 - \epsilon_ {t}}{\epsilon_ {t}}\tag{3}
$$

where $\epsilon _ { t }$ represents the classification error rate in each learner. Then the trained weak learners are assembled to a strong classifier. The integrated model is defined as:

$$
H (x) = \sum_ {t = 1} ^ {T} v \alpha_ {t} h _ {t} (x)\tag{4}
$$

where the learning rate v ranges from 0 to 1. The smaller v means the model requires more interactions to train the model. The fitting efect of the model is decided by the trade-of between learning rate v and forest size T .

## 3.2.2. Parameter Fine-tuning

Figure 4: Parameter fine-tuning: forest size (learning rate = 0.1). The x-axis is the forest size, and the y-axis is the model accuracy. The solid line depicts the accuracy of the model on training samples. The dashed line depicts the accuracy of the model on testing samples.

This section evaluates the efects of learning rate v and forest size T on the performance of the AdaBoost model so that the optimal values of these parameters can be chosen. For convenience and creditability, we adopt a grid search method to conduct the parameter tuning process by two steps: (1) training and testing the proposed method on diferent parameters; (2) comparing and evaluating the results and selecting the optimal combination of parameters. This method has the advantage of considering the interaction of diferent parameters, and the trade-of between over-fitting and underfitting.

A parameter grid on $[ 1 , 1 0 0 0 ] \times [ 0 . 0 0 1 , 0 . 0 1 , 0 . 1 , 1 ]$ is applied to fine-tune the parameters. The result shows that when α is 0.1, and T is 500, the performance reaches its best. The trade-of results on forest size are depicted in Fig. 4, with learning rate settled at 0.1. It is observed that before 500, the accuracy of the model on both the training sample and the testing sample grows with forest size, where the model is under-fitting. However, when forest size is excessive, the fitting degree of testing samples is decreased. Thus, we select 500 as the trade-of between model performances on training and testing samples. Next, the model performance with a learning rate of $[ 0 . 0 0 1 , 0 . 0 1 , 0 . 1 , 1 ]$ and a constant forest size of 500 is demonstrated in Fig. 5. When the learning rate is 0.1, the model reaches the optimal trade-of on both training and testing samples. In our implementation, we settled on a forest size of 500 with a learning rate of 0.1 in the AdaBoost model.

Figure 5: Parameter fine-tuning: learning rate (forest size = 500).The x-axis is the learning rate, and the y-axis is the model accuracy. The solid line depicts the accuracy of the model on training samples. The dashed line depicts the accuracy of the model on testing samples.

## 3.3. Experimental Results

## 3.3.1. Evaluation Metrics

In order to evaluate the prediction performance of loan applicants, some evaluation metrics in other algorithms are considered, such as Accuracy, Ture Negative Rate (TNR), True Positive Rate (TPR), Receiver Operating Characteristic (ROC), as well as the area under curve ROC (AUC) (Sokolova and Lapalme, 2009). We use the ROC and AUC to measure the discriminatory ability. The Accuracy, TNR, and TPR are used to measure the correctness of the categorical predictions, which are defined as follows.

$$
\begin{array}{r} A c c u r a c y = \frac {T P + T N}{T P + N P + T N + F N} \\ T P R = \frac {T P}{T P + F N} \\ T N R = \frac {T N}{T N + F P} \end{array}
$$

where T P represents true positive, F P represents false positive, T N represents true negative, and F N represents false negative.

## 3.3.2. Variable Performance

Figure 6: Importance of each variables for the proposed model using selected variables. The bars are the variables, and the y-axis is the variable importance. The relevant result from the logistic regression is in parentheses after each variable: A + or refers to the significant coeficients. N represents that the variable was not significant. C represents when the variable was correlated with other variables.

In order to explore the relationship between the selected variables and loan default, we analyze the performance of the logistic regression. Considering the performance of logistic regression, some of these variables may not be significant, which suggests that there may exist a mixture of connections among these variables that cannot be learned by linear models. However, we can still learn the positive or negative sign of some variables. As depicted in Fig. 6, the telecommunication patterns tend to be good indicators of loan default, where the average time of internals (T24) and the regularity of phone calls per month (T10) have negative signs, the regularity of phone calls per day (T9), and the proportion of communications at the night (T28) have positive signs. Meanwhile, App usage patterns contain good indicators, where the sum of data trafic spent in one month (A16) is positive to loan default, the variance of data trafic (A18), the regularity of data trafic (A21), and the number of payment Apps (A27) have negative signs. Specifically, the total use frequency of P2P lending Apps (A39) is a negative sign and the usage preference of P2P lending Apps on data trafic (A42) is a positive sign, which suggests that less access to P2P lending Apps and more data trafic spent on unpopular lending Apps, may lead to a greater frequency of loan default.

In order to measure the importance of selected variables in the prediction model, we analyze the results derived from AdaBoost. We randomly split the dataset (2999 subjects) into two parts, where 80% are used for training (2399 subjects) and 20% (600 subjects) are used for testing. The variable importance is depicted in Fig. 6. It is interesting to find that the most relevant variable is the number of installed financial Apps and payment Apps (A32), as this variable can indicate the individuals’ digital economic-related operation behavior, providing an indication of the economic status of individuals. The next three variables describe the telecommunication patterns, which consist of the regularity of phone calls per day (T9), per month (T10), and the proportion of communications at night (T28). It followed the number of payment Apps (A22), which reflects the economic status of individuals. The following variables include the variance of phone calls and the number of text messages in one day (T20), the variance of intervals (T25), and the variance of messages in one day (T13), which also indicate the economic status of individuals. The average data trafic spent (A17) and the sum of locations (M8) also show a sign of default behavior. To sum up, it can be observed that the inclusion of App usage and telecommunication behaviors are most predictive of the loan default behavior.

Table 4: Performance on diferent categories of variables

<table><tr><td></td><td>Accuracy (%) (Training Sample)</td><td>Accuracy (%) (Testing Sample)</td><td>TNR (%)</td><td>TPR (%)</td></tr><tr><td>Model 1</td><td>66.0</td><td>66.0</td><td>18.0</td><td>66.0</td></tr><tr><td>Model 2</td><td>65.0</td><td>63.0</td><td>10.0</td><td>63.0</td></tr><tr><td>Model 3</td><td>72.0</td><td>66.0</td><td>38.0</td><td>66.0</td></tr><tr><td>Proposed Method</td><td>75.0</td><td>71.0</td><td>47.0</td><td>71.0</td></tr></table>

Model 1 includes variables in telecommunication patterns. Model 2 includes variables in mobility patterns. Model 3 includes variables in App usage patterns. The demographic variables and telecommunication records are included in all of the three models.

In order to further compare the predictability of diferent variable sets, we compare the performance of three models which use diferent categories of variables, respectively. The division of the training and testing set is same as the last experiment. Model 1 includes variables belonging to telecommunication patterns. Model 2 includes variables in mobility patterns. Model 3 includes variables in App usage patterns. The demographic variables and telecommunication records are included in all of the three models. The proposed method includes all variables. We compare the accuracy of the models on training and testing samples. As shown in Table 4, the performances of Model 1 and Model 3 are better when compared with Model 2, which suggests that the predictive ability of telecommunication and App usage patterns are better. Accuracies on both training and testing subjects achieve the highest level in the proposed method, which suggests the combination of all variables can improve the predictive capability of variables. Also, the proposed method increases TNR and TPR, which indicates the better distinguishing ability of the proposed method.

## 3.3.3. Comparison of the method

Table 5: Performance comparison on diferent models

<table><tr><td></td><td>Accuracy (%) (Training Sample)</td><td>Accuracy (%) (Testing Sample)</td><td>TNR (%)</td><td>TPR (%)</td></tr><tr><td>AdaBoost</td><td>75.0</td><td>71.0</td><td>47.0</td><td>71.0</td></tr><tr><td>Random Forest</td><td>80.0</td><td>68.0</td><td>44.0</td><td>68.0</td></tr><tr><td>Logistic Regression</td><td>68.0</td><td>67.0</td><td>36.0</td><td>67.0</td></tr></table>

Figure 7: AUC for AdaBoost, Random Forest, and Logistic Regression. The x-axis is the false positive rate, and the y-axis is the true positive rate. The solid line depicts the AUC of AdaBoost model. The dashed line depicts the AUC of random forest model. The dotted line depicts the AUC of the logistic regression model.

In order to analyze the prediction efect of AdaBoost, we compare the performance of AdaBoost with the other two models. One is random forest, the other is logistic regression. These two methods are widely used for prediction problems. Both applied grid search method to achieve the best parameters. The division of the training and testing set is same as the last experiment. The performance of AdaBoost, random forest and logistic regression are shown in Table 5. It can be observed that AdaBoost and random forest achieve better performances compared with logistic regression in evaluation metrics. TNR in AdaBoost is 47%, comparing with 44% in the random forest and 36% in logistic regression, which implies that AdaBoost-based model can identify more default subjects. This trait can be very useful in application to P2P platforms. Note that the accuracy of the training sample of random forest is 80%, which is higher than 75% in AdaBoost. But of the testing sample, 71% in AdaBoost is much higher than 68% in the random forest. This suggests that the applicability of AdaBoost is better. The AUC among these three models is depicted in Fig. 7. The AUC of AdaBoost is 0.723, which is higher than that of random forest (0.706) and logistic regression (0.684). The lower performance in the other two models is related to lower recognition rate of default and non-default subjects.

In order to test the predictive power of the proposed method, we analyze the performance of models using across time variables. The raw data are divided into two sets in chronological order and two sets of variables are extracted from these two data sets. $V _ { A }$ refers to the variables extracted from former periods; $V _ { B }$ refers to the variables extracted from the later periods. Three models are constructed based on the AdaBoost algorithm, respectively. Model 4 uses variables $V _ { A }$ , and Model 5 uses variables $V _ { B }$

## ACCEPTED MANUSCRIPT

Table 6: The performances compared among diferent sample sets

<table><tr><td></td><td>Accuracy (%) (Training Sample)</td><td>Accuracy (%) (Testing Sample)</td><td>TNR (%)</td><td>TPR (%)</td></tr><tr><td>Proposed Method</td><td>75.0</td><td>71.0</td><td>47.0</td><td>71.0</td></tr><tr><td>Model 4</td><td>76.0</td><td>68.0</td><td>39.0</td><td>68.0</td></tr><tr><td>Model 5</td><td>78.0</td><td>68.0</td><td>34.0</td><td>68.0</td></tr><tr><td>Model 6</td><td>77.0</td><td>70.0</td><td>58.0</td><td>70.0</td></tr></table>

The raw data are divided into two sets in chronological order. $V _ { A }$ refers to the variables extracted from former periods, $V _ { B }$ refers to the variables extracted from the later periods. Model 4, 5, 6 are constructed based on AdaBoost algorithm. Model 4 uses variables $V _ { A }$ . Model 5 uses variables V . Model 6 randomly selects 80% of subjects as training subjects, where the training variables were from $V _ { A }$ . The remaining 20% of subjects are used as testing samples and the variables are from $V _ { B }$

The division of the training and testing set is the same as the last experiment. Model 6 randomly selects 80% of the subjects as training subjects, where the training variables are from $V _ { A }$ . The remaining 20% of subjects are used as testing samples and the variables are from $V _ { B } .$ . The experiment results are shown in Table 6. Although the accuracy in the training sample are not advantageous in the proposed method, we are concerned with its generality. The accuracy in the testing sample, TPR, and TNR of Model 4 and Model 5, are not as good as the proposed model. This may be a result of the fact that the variables extracted from the whole period contain more information. However, the two models achieves stable performance, and we can use the samples from the two sets to further analyze the predictive power of the method. As shown in Table 6, Model 6 shows better performance in evaluation metrics, which can support the predictability of the proposed method. Notably, Model 6 has the biggest value on TNR (58.0%). This may because that the use of mobile phones has a certain regularity (Thomason et al., 2016). Therefore, the predictability of the model may increase by using the former data to predict the following behavior.

## 3.3.4. Comparison against existing methods

In order to explain how the proposed method can be used in practice, the performance has been compared with state-of-art studies. Malekipirbazari and Aksakalli (2015) train a random forest model on Lending Club dataset to assess the individual default risk. As depicted in Table 7, the proposed method has higher AUC (0.73) and Precision (0.7) than the compared model with AUC of 0.71 and precision of 0.56, which demonstrates that the proposed method has better prediction performance. Also, our recall is 0.71, which is lower than 0.87 in the comparison model. This result indicates that the proposed method is a more conservative model tending to reject more applicants in order to protect the platforms form possible financial loss.

Moreover, we compare the performance to another existing method (Serrano-Cinca et al., 2015) following the same protocol in the division of training samples and test samples. They develop a logistic regression model to predict default, also using data from Lending Club. As depicted in Table 8, our performance is better than the comparison model both on the training and testing samples. These results demonstrate that the proposed method has better performance when compared to the existing methods on the P2P lending problem, which implies the feasibility of adopting the proposed method on P2P lending platforms.

Table 7: The performance comparison between the proposed method and the comparison mo del

<table><tr><td></td><td>AUC</td><td>Precision</td><td>Recall</td></tr><tr><td>(Malekipirbazari and Aksakalli, 2015)</td><td>0.71</td><td>0.56</td><td>0.87</td></tr><tr><td>Proposed Method</td><td>0.72</td><td>0.7</td><td>0.71</td></tr></table>

Table 8: The performance comparison between the proposed method and the comparison model

<table><tr><td></td><td>(Serrano-Cinca et al., 2015)</td><td>Proposed Method</td></tr><tr><td>Training samples</td><td>0.651</td><td>0.75</td></tr><tr><td>Testing samples</td><td>0.646</td><td>0.71</td></tr></table>

## 4. Discussion

## 4.1. Practical Implications

The loan decision-making of lenders and P2P platforms is based on credit scoring results and other related information. However, in reality it is dificult to make loan decisions about some borrowers. On the one hand, the authenticity of the information source is dificult to evaluate through the Internet. On the other hand, some borrowers cannot provide suficient evidence to prove their trustworthiness, such as the unbanked and those in countries with limited credit scoring systems. The proposed method can solve this problem by using an alternative data source to predict default probability of loans. Since the phone usage data used in the method are more general and can provide ‘invisible’ credit-related information, the credibility and generality can be guaranteed.

Due to the large quantity of loan applications, P2P platforms are required to make numerous loan decisions at the same time. However, traditional financial institutions conduct loan prediction by manual vetting, which has high labor cost and time cost. This kind of low-eficiency and high-cost prediction can not meet loan decision requirements in P2P platforms(Francis et al., 2017). Default prediction method, such as one in this paper, can help P2P platforms solve this problem. The data used in the proposed method already exist before the loan prediction is conducted. The prediction method is based on machine learning algorithms, which can be automatically implemented. P2P platforms can obtain default prediction results immediately, which can help them to make quick decisions.

More and more financial projects attempt to score the ‘credit invisible’ by leveraging the alternative data and big data analysis method (Aitken, 2017). Our study sheds light on how to excavate the value of the mass digital footprint and facilitate the connection between the raw data and the credit.

## 4.2. Ethical Consideration

As the data involve individual privacy, the ethical problem of collecting and analyzing subjects’ behavior data requires careful consideration. The subjects used in this study are randomly selected from one of the P2P lending platforms in China. Before borrowers request a loan on the P2P platform, they are asked to sign an informed consent, where the P2P platform explains in detail that the information of individuals may be given to a third-party organization under the protection of privacy. Guaranteed by the encryption techniques, it is impossible for us to decrypt and identify the users.

Also, due to the application requirement, a support system of loan decisions for the P2P lending platform can be used. When a borrower applies for loans on a P2P platform, the default prediction system is triggered. First, the loan approval process encrypts the borrower’s ID and sends it to a mobile carrier via API. Second, the mobile carrier performs the default prediction based on the proposed method and sends the result back. Third, depending on the assessment result, the loan approval process decides whether or not to post the borrower’s loan application online. Finally, if the loan application is posted, lenders access the application and conclude the transaction. The loan applicant files are kept by the P2P platforms and the phone usage data are kept by the mobile carriers. Only the encrypted borrowers ID and the default prediction result could be transformed via API. By using this DSS, P2P platforms can make loan decisions while guaranteeing the privacy of potential borrowers.

## 5. Conclusion

The current paper proposes a default prediction method, which supports the loan decision in P2P lending platforms when information asymmetry exists for borrowers. Firstly, we find some theoretical evidence of the relationships between phone usage data and loan default behavior from three patterns of variables: telecommunication patterns, mobility patterns, and App usage patterns. The statistical analyses have been conducted to verify these relationships. Then, we propose a prediction method based on the extracted variables. In this method, a synthetical REF algorithm is adapted to select the most discriminative variables, and the AdaBoost algorithm is used to construct the default prediction model. Lastly, a real-world data have been adopted to evaluate the prediction eficiency of the proposed method.

The empirical analysis suggests that variables extracted from phone usage data contain predictability and the variables describing individuals’ telecommunication and App usage behaviors are the most predictive for individuals’ loan default. Compared with other classifiers, the AdaBoost model has achieved the best performance in terms of evaluation metrics. Moreover, the proposed method has demonstrated its advantages in comparison with state-of-the-art default prediction methods for P2P platforms.

In the future, long time span data may be collected and used to assess the stability of the variables extracted from mobile phone data for credit scoring. Reinforce learning based methods may also be anticipated to adapt as a dynamic update mechanism to handle streamed mobile phone usage data.

## Acknowledgements

This work is supported by the National Nature Science Foundation of China (Grant 71390333, Grant No. 91746111, Grant No.71702143, Grant No. 71731009, Grant No. 71732006, Grant No. 71742005), Ministry of Education & China Mobile Joint Research Fund Program (No. MCM20160302), Shaanxi provincial development and Reform Commission (No. SFG2016789), Xi’an Municipal Science & Technology Commission (No. 2017111SF/RK005-(7)) , Natural Science Foundation of Shaanxi (NO. 2017JQ7004), China Postdoctoral Science Fund (No. 2016M602840).

## References

Agarwal, S., Chomsisengphet, S., & Liu, C. (2011). Consumer bankruptcy and default: The role of individual social capital. Journal of Economic Psychology, 32(4),632–650. doi: 10.1016/j.joep.2010.11.007

Aitken, R. (2017). ‘All data is credit data’: Constituting the unbanked. Competition & Change, 21(4),274– 300. doi: 10.1177/1024529417712830

Bernerth, J. B., Taylor, S. G., Walker, H. J., & Whitman, D. S. (2012). An empirical investigation of dispositional antecedents and performance-related outcomes of credit scores. Journal of Applied Psychology, 97(2),469. doi: 10.1037/a0026055

Blumenstock, J., Cadamuro, G., & On, R. (2015). Predicting poverty and wealth from mobile phone metadata. Science, 350(6264), 1073–1076. doi: 10.1126/science.aac4420

Boase, J. & Ling, R. (2013). Measuring mobile phone use: Self-report versus log data. Journal of Computer-Mediated Communication, 18(4), 508–519. doi: 10.1111/jcc4.12021

Bravo, C., Thomas, L. C., & Weber, R. (2015). Improving credit scoring by diferentiating defaulter behaviour. Journal of the Operational Research Society, 66(5), 771–781. doi: 10.1057/jors.2014.50

Chen, X., Zhou, L., & Wan, D. (2016). Group social capital and lending outcomes in the financial credit market: An empirical study of online peer-to-peer lending. Electronic Commerce Research Applications, 15(C), 1–13. doi: 10.1016/j.elerap.2015.11.003

Chittaranjan, G., Blom, J., & Gatica-Perez, D. (2013). Mining large-scale smartphone data for personality studies. Personal and Ubiquitous Computing, 17(3), 433–450. doi: 10.1007/s00779-011-0490-1

De Martino, F., Valente, G., Staeren, N., Ashburner, J., Goebel, R., & Formisano, E. (2008). Combining multivariate voxel selection and support vector machines for mapping and classification of fMRI spatial patterns. NeuroImage, 43(1), 44–58. doi: 10.1016/j.neuroimage.2008.06.037

Eagle, N., Macy, M., & Claxton, R. (2010). Network diversity and economic development. Science, 328(5981), 1029–1031. doi: 10.1126/science.1186605

Emekter, R., Tu, Y., Jirasakuldech, B., & Lu, M. (2015). Evaluating credit risk and loan performance in online Peer-to-Peer (P2P) lending. Applied Economics, 47(1), 54–70. doi: 10.1080/00036846.2014.962222

Francis, E., Blumenstock, J., & Robinson, J. (2017). Digital credit: A snapshot of the current landscape and open research questions. UC Berkeley: Center for Efective Global Action. Retrieved from https://escholarship.org/uc/item/88r1j7sz

Freund, Y. & Schapire, R. E. (1997). A desicion-theoretic generalization of on-line learning and an application to boosting. Journal of Computer and System Sciences, 55(1), 119–139. doi: 10.1006/jcss.1997.1504

## ACCEPTED MANUSCRIPT

Frias-Martinez, V. & Virseda, J. (2012). On the relationship between socio-economic factors and cell phone usage. In Proceedings of the Fifth International Conference on Information and Communication Technologies and Development (pp. 76–84). ACM. doi: 10.1145/2160673.2160684

Goldberg, L. R. (1999). A broad-bandwidth, public domain, personality inventory measuring the lowerlevel facets of several Five-Factor models. Personality Psychology in Europe, 7(1), 7–28. doi: 10.1016/0167-4870(93)90004-5

Gonzalez, L. & Loureiro, Y. K. (2014). When can a photo increase credit? The impact of lender and borrower profiles on online peer-to-peer loans. Journal of Behavioral and Experimental Finance, 2, 44–58. doi: 10.1016/j.jbef.2014.04.002

Guo, Y., Zhou, W., Luo, C., Liu, C., & Xiong, H. (2016). Instance-based credit risk assessment for investment decisions in P2P lending. European Journal of Operational Research, 249(2), 417–426. doi: 10.1016/j.ejor.2015.05.050

Harari, G. M., Lane, N. D., Wang, R., Crosier, B. S., Campbell, A. T., & Gosling, S. D. (2016). Using smartphones to collect behavioral data in psychological science: Opportunities, practical considerations, and challenges. Perspectives on Psychological Science, 11(6), 838–854. doi: 10.1177/1745691616650285

Harari, G. M., M¨uller, S. R., Aung, M. S., & Rentfrow, P. J. (2017). Smartphone sensing methods for studying behavior in everyday life. Current Opinion in Behavioral Sciences, 18, 83–90. doi: 10.1016/j.cobeha.2017.07.018

Judge, T. A., Higgins, C. A., Thoresen, C. J., & Barrick, M. R. (1999). The big five personality traits, general mental ability, and career success across the life span. Personnel psychology, 52(3), 621–652. doi: 10.1111/j.1744-6570.1999.tb00174.x

Kasuya, E. (2001). Mann-Whitney U test when variances are unequal. Animal Behaviour, 61(6), 1247– 1249. doi: 10.1006/anbe.2001.1691

Kim, Y., Briley, D. A., & Ocepek, M. G. (2015). Diferential innovation of smartphone and application use by sociodemographics and personality. Computers in Human Behavior, 44, 141–147. doi: 10.1016/j.chb.2014.11.059

Lane, N. D., Miluzzo, E., Lu, H., Peebles, D., Choudhury, T., & Campbell, A. T. (2010). A survey of mobile phone sensing. IEEE Communications magazine, 48(9), 140–150. doi: 10.1109/MCOM.2010.5560598

Lea, S. E., Webley, P., & Levine, R. M. (1993). The economic psychology of consumer debt. Journal of Economic Psychology, 14(1), 85–119. doi: 10.1016/0167-4870(93)90041-I

Lea, S. E., Webley, P., & Walker, C. M. (1995). Psychological factors in consumer debt: Money management, economic socialization, and credit use. Journal of Economic Psychology, 16(4), 681–701. doi: 10.1016/0167-4870(95)00013-4

Lessmann, S., Baesens, B., Seow, H. V., & Thomas, L. C. (2015). Benchmarking state–of–the–art classification algorithms for credit scoring: An update of research. European Journal of Operational Research, 247(1), 124–136. doi: 10.1016/j.ejor.2015.05.030

LiKamWa, R., Liu, Y., Lane, N. D., & Zhong, L. (2013). Moodscope: Building a mood sensor from smartphone usage patterns. In Proceeding of the 11th Annual International Conference on Mobile Systems, Applications, and Services (pp. 389–402). ACM. doi: 10.1145/2462456.2464449

Lin, M., Prabhala, N. R., & Viswanathan, S. (2013). Judging borrowers by the company they keep: Friendship networks and information asymmetry in online Peer-to-Peer lending. Management Science, 59(1), 17–35. doi: 10.1287/mnsc.1120.1560

Liu, S., Qu, Q., & Wang, S. (2015). Rationality analytics from trajectories. ACM Transactions on Knowledge Discovery from Data, 10(1), 10:1–10:22. doi: 10.1145/2735634

Liu, X., Ai, W., Li, H., Tang, J., Huang, G., Feng, F., & Mei, Q. (2017). Deriving user preferences of mobile apps from their management activities. ACM Transactions on Information Systems, 35(4), 39:1–39:32. doi: 10.1145/3015462

Maddala, G. S. & Lahiri, K. (1992). Introduction to econometrics. Macmillan New York.

Madden, M. & Rainie, L. (2015). Americans’ attitudes about privacy, security and surveillance. Pew Research Center.

Maldonado, S., Bravo, C., Lpez, J., & Prez, J. (2017). Integrated framework for profit–based feature selection and SVM classification in credit scoring. Decision Support Systems, 104, 113–121. doi: 10.1016/j.dss.2017.10.007

Malekipirbazari, M. & Aksakalli, V. (2015). Risk assessment in social lending via random forests. Expert Systems with Applications, 42(10), 4621–4631. doi: 10.1016/j.eswa.2015.02.001

Mceliece, R. (2002). The theory of information and coding. Cambridge University Press.

Oren, N. (2002). Reexamining tf. idf based information retrieval with genetic programming. In Proceedings of the 2002 Annual Research Conference of the South African Institute of Computer Scientists and Information Technologists on Enablement Through Technology (pp. 224–234). South African Institute for Computer Scientists and Information Technologists. Retrieved from http://dl.acm.org/citation.cfm?id=581506.581538

Parent, C., Spaccapietra, S., Renso, C., Andrienko, G., Andrienko, N., Bogorny, V., Damiani, M. L., Gkoulalas-Divanis, A., Macedo, J., Pelekis, N., Theodoridis, Y., & Yan, Z. (2013). Semantic trajectories modeling and analysis. ACM Computing Surveys, 45(4), 42:1–42:32. doi: 10.1145/2501654.2501656

Pareto, V. (1964). Cours d’´economie politique. Librairie Droz.

Perry, V. G. & Morris, M. D. (2005). Who is in control? The role of self-perception, knowledge, and income in explaining consumer financial behavior. Journal of Consumer Afairs, 39(2), 299–313. doi: 10.1111/j.1745-6606.2005.00016.x

Pielot, M., Dingler, T., Pedro, J. S., & Oliver, N. (2015). When attention is not scarce-detecting boredom from mobile phone usage. In Proceedings of the 2015 ACM international joint conference on pervasive and ubiquitous computing (pp. 825–836). ACM. doi: 10.1145/2750858.2804252

Pokhriyal, N. & Jacques, D. C. (2017). Combining disparate data sources for improved poverty prediction and mapping. Proceedings of the National Academy of Sciences, 114(46), E9783–E9792. doi: 10.1073/pnas.1700319114

Polena, M. & Regner, T. (2016). Determinants of borrowers’ default in P2P lending under consideration of the loan risk class. Jena Economic Research Papers (No. 2016–023). Retrieved from http://hdl.handle.net/10419/148902

Putnam, R. D. (2000). Bowling alone: America’s declining social capital. In Culture and Politics: A Reader (pp. 223–234). Palgrave Macmillan, New York. doi: 10.1007/978-1-349-62397-6 12

Renso, C., Baglioni, M., de Macedo, J. A. F., Trasarti, R., & Wachowicz, M. (2013). How you move reveals who you are: Understanding human behavior by analyzing trajectory data. Knowledge and Information Systems, 37(2), 331–362. doi: 10.1007/s10115-012-0511-z

S´cepanovi´c, S., Mishkovski, I., Hui, P., Nurminen, J. K., & Yl¨a-J¨a¨aski, A. (2015). Mobile phone <sup>ˇ</sup> call data as a regional socio-economic proxy indicator. PloS one, 10(4), 1–15. doi: 10.1371/journal.pone.0124160

Serrano-Cinca, C. & Guti´errez-Nieto, B. (2016). The use of profit scoring as an alternative to credit scoring systems in peer-to-peer (P2P) lending. Decision Support Systems, 89, 113–122. doi: 10.1016/j.dss.2016.06.014

Serrano-Cinca, C., Gutierrez-Nieto, B., & L´opez-Palacios, L. (2015). Determinants of default in P2P lending. PloS one, 10(10), e0139427. doi: 10.1371/journal.pone.0139427

Shen, J., Brdiczka, O., & Liu, J. (2015). A study of Facebook behavior: What does it tell about your Neuroticism and Extraversion? Computers in Human Behavior, 45, 32–38. doi: 10.1016/j.chb.2014.11.067

Sokolova, M. & Lapalme, G. (2009). A systematic analysis of performance measures for classification tasks. Information Processing & Management, 45(4), 427–437. doi: 10.1016/j.ipm.2009.03.002

Soto, V., Frias-Martinez, V., Virseda, J., & Frias-Martinez, E. (2011). Prediction of socioeconomic levels using cell phone records. In International Conference on User Modeling, Adaption and Personalization (pp. 377–388). Springer, Berlin, Heidelberg. doi: 10.1007/978-3-642-22362-4 35

Stachl, C., Hilbert, S., Au, J.-Q., Buschek, D., De Luca, A., Bischl, B., Hussmann, H., & B¨uhner, M. (2017). Personality traits predict smartphone usage. European Journal of Personality, 31(6), 701–722. doi: 10.1002/per.2113

Stepanova, M. & Thomas, L. (2002). Survival analysis methods for personal loan data. Operations Research, 50(2), 277–289. doi: 10.1287/opre.50.2.277.426

Thomas, L. C. (2000). A survey of credit and behavioural scoring: Forecasting financial risk of lending to consumers. International Journal of Forecasting, 16(2), 149–172. doi: 10.1016/S0169-2070(00)00034- 0

Thomason, A., Grifiths, N., & Sanchez, V. (2016). Context trees: Augmenting geospatial trajectories with context. ACM Transactions on Information Systems, 35(2), 14:1–14:37. doi: 10.1145/2978578

Tokunaga, H. (1993). The use and abuse of consumer credit: Application of psychological theory and research. Journal of Economic Psychology, 14(2), 285–316. doi: 10.1016/0167-4870(93)90004-5

Wang, J. & Xu, H. (2015). China’s online lending industry in 2015. Tsinghua University Press.

Wang, M., Zheng, X., Zhu, M., & Hu, Z. (2016). P2P lending platforms bankruptcy prediction using fuzzy SVM with region information. In e-Business Engineering (ICEBE), 2016 IEEE 13th International Conference on (pp. 115–122). IEEE. doi: 10.1109/ICEBE.2016.028

Wang, X., Zhang, D., Zeng, X., & Wu, X. (2013). A Bayesian investment model for online P2P lending. In Frontiers in Internet Technologies (pp. 21–30). Springer Berlin, Heidelberg. doi: 10.1007/978-3- 642-53959-6 3

Wu, S., Kang, N., & Yang, L. (2007). Fraudulent behavior forecast in telecom industry based on data mining technology. Communications of the IIMA, 7(4), 1. Retrieved from http://scholarworks.lib.csusb.edu/ciima/vol7/iss4/1

Xu, R., Frey, R. M., Fleisch, E., & Ilic, A. (2016). Understanding the impact of personality traits on mobile app adoption–Insights from a large-scale field study. Computers in Human Behavior, 62, 244–256. doi: 10.1016/j.chb.2016.04.011

Zhang, Y., Jia, H., Diao, Y., Hai, M., & Li, H. (2016). Research on credit scoring by fusing social media information in online Peer–to–Peer lending. Procedia Computer Science, 91, 168–174. doi: 10.1016/j.procs.2016.07.055

Zhao, H., Ge, Y., Liu, Q., Wang, G., Chen, E., & Zhang, H. (2017). P2P lending survey: Platforms, recent advances and prospects. ACM Transactions on Intelligent Systems and Technology, 8(6), 72:1–72:28. doi: 10.1145/3078848

Zhao, S., Ramos, J., Tao, J., Jiang, Z., Li, S., Wu, Z., P, & Dey, A. K. (2016). Discovering diferent kinds of smartphone users through their application usage behaviors. In Proceedings of the 2016 ACM International Joint Conference on Pervasive and Ubiquitous Computing (pp. 498–509). ACM. doi: 10.1145/2971648.2971696

## Bibliograhy

Lin Ma received the bachelor degree in computer science and technology from Xi'an Jiaotong University, Xi'an, China, in 2015. She is currently working toward the Ph.D. degree in management science and engineering, Xi'an Jiaotong University. Her research mainly focuses on data mining and behavior analysis. Email: malin@stu.xjtu.edu.cn

Xi Zhao received the Ph.D. (Hons.) degree in computer science from the Ecole Centrale de Lyon, Lyon, France, in 2010. He conducted research in the fields of biometrics, data analytics, and pattern recognition as a Research Assistant Professor in the Department of Computer Science, University of Houston, Houston, TX, USA. He is currently an Associate Professor with Xi'an Jiaotong University, Xi'an, China. His current research interests include affective computing, behavior computing, mobile computing, and biometrics. Email: zhaoxi1@mail.xjtu.edu.cn

Zhili Zhou received the Ph.D. degree in management science from Xi'an Jiaotong University, Xi'an, China, in 2000. He is a Professor of Management School at Xi'an Jiaotong University. His current research interests include operations management and operational research, mathematical modeling and heuristic solution of practical operations problems. Email: zlzhou@mail.xjtu.edu.cn

Yuanyuan Liu received the Ph.D. degree from ESSEC Business School, France. She is currently an Assistant Professor in the Department of Marketing, Xi'an Jiaotong University, Xi'an, China. Her research interests include consumer behavior and behavioral decision theory. Email: yuanyuanliu@xjtu.edu.cn

## ACCEPTED MANUSCRIPT

![](/api/attachments/CYKH5X3T/fulltext/images/c1d8aef611e107541cca6d8e2aaa4fc4c64465b35a780eaaf57dff4f71717716.jpg)  
Fig. 1

![](/api/attachments/CYKH5X3T/fulltext/images/c56b8c32fa9788a667e6e7c5f6dc7ea3366a41d80a3bf4f8fece69d32e5b1674.jpg)  
Fig. 2

![](/api/attachments/CYKH5X3T/fulltext/images/6016fad3882a645258a50724a1dc42463f5e526eee043ca601fa368054456d71.jpg)  
Fig. 3

![](/api/attachments/CYKH5X3T/fulltext/images/dd27272a303e907f19df5b6ad4751ad76c02df6e64ae6e1c723e48746d39faa3.jpg)  
Fig. 4

![](/api/attachments/CYKH5X3T/fulltext/images/a93eb003b7ab2cb2fa90668572bab67f9f852b1847f07d7cca5bc1ef01056f4b.jpg)  
Fig.5

![](/api/attachments/CYKH5X3T/fulltext/images/274bf5924fcd08cb44827aee9cbf6cac04128e50037a4e068ff2b68ab2a794ce.jpg)  
Fig.6

![](/api/attachments/CYKH5X3T/fulltext/images/fccbbc97853d99dc79711f5b0f3ccb8e35685b2f510b63e56df6091fd04cce8d.jpg)  
Fig.7

## Highlights

Meta-level phone usage data is relevant to credit scoring

Variables extracted from phone usage data contain predictive ability to loan default.

A credit scoring method using mobile phone usage data obtained satisfying results.

![](/api/attachments/CYKH5X3T/fulltext/images/77eb328c5ac90bbcd955512a934258ff203ff1e05ef173743c7d19d76cfecb42.jpg)  
Figure 1

![](/api/attachments/CYKH5X3T/fulltext/images/3d98187ea0871606837546dd94ccfb2354d898fc8a867d0dfb3f0d2b226f1f06.jpg)  
Figure 2

![](/api/attachments/CYKH5X3T/fulltext/images/fbef6db26963662e6662ca37ed64ae045c481d8191600138b97d93db8a449694.jpg)  
Figure 3

![](/api/attachments/CYKH5X3T/fulltext/images/a282df05ea4a3e176247f436db0d40d420e979372ef39f1af29a9da225c68b51.jpg)  
Figure 4

![](/api/attachments/CYKH5X3T/fulltext/images/77d30eeca3720806cc093e5778880bb09b5fb0b75d66fee1ae5ffcad0af59997.jpg)  
Figure 5

![](/api/attachments/CYKH5X3T/fulltext/images/7a554881b13fc0ad5b28f33d78026db362729b7cc779ef5b313618f375d66565.jpg)  
Figure 6

![](/api/attachments/CYKH5X3T/fulltext/images/e631c800fe950cd47199425c505cc677f34d3ae0a2f644ef6c251ed37e02e2b5.jpg)  
Figure 7
