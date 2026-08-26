---
otero_id: 2266
otero_key: "HAWDCF4H"
title: "Design of an information volatility measure for health care decision making"
authors: "Monica Chiarini Tremblay; Alan R. Hevner; Donald J. Berndt"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.08.009"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Design of an information volatility measure for health care decision making

Monica Chiarini Tremblay <sup>a,</sup>⁎, Alan R. Hevner <sup>b</sup>, Donald J. Berndt <sup>b</sup>

<sup>a</sup> Decision Sciences and Information Systems, College of Business Administration, Florida International University, 11200 SW 8th Street, RB 250, Miami, FL 33199, United States <sup>b</sup> Information Systems and Decision Sciences, College of Business, 4202 Fowler Ave., CIS1040, University of South Florida,, Tampa, FL 33620, United States

## a r t i c l e i n f o

Article history: Received 13 April 2011 Accepted 25 August 2011 Available online 3 September 201

Keywords: OLAP Health care informatics Data quality Decision support systems Data instability Information volatility

## a b s t r a c t

Health care decision makers and researchers often use reporting tools (e.g. Online Analytical Processing (OLAP)) that present data aggregated from multiple medical registries and electronic medical records to gain insights into health care practices and to understand and improve patient outcomes and quality of care. An important limitation is that the data are usually displayed as point estimates without full description of the instability of the underlying data, thus decision makers are often unaware of the presence of outliers or data errors. To manage this problem, we propose an Information Volatility Measure (IVM) to complement business intelligence (BI) tools when considering aggregated data (intra-cell) or when observing trends in data (inter-cell). The IVM de<sup>fi</sup>nitions and calculations are drawn from volatility measures found in the <sup>fi</sup>eld of <sup>fi</sup>nance, since the underlying data in both arenas display similar behaviors. The presentation of the IVM is supplemented with three types of benchmarking to support improved user understanding of the measure: numerical benchmarking, graphical benchmarking, and categorical benchmarking. The IVM is designed and evaluated using exploratory and con<sup>fi</sup>rmatory focus groups.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Health care decision makers and researchers often use aggregated data from centralized repositories and/or data warehouses to gain insights into health care practices and to understand and improve patient outcomes and quality of care. For example, policy makers may analyze aggregated data to point out signi<sup>fi</sup>cant variations in hospitalization rates for expensive medical interventions [13], or researchers may compare cancer mortality rates in similar communities by investigating average tumor size at detection.

These aggregated data are often created by combining administrative data collected across several sources as a patient traverses the health care system. Data are collected from the moment a patient enrolls in a health plan and along each step as he or she seeks care as health care providers and payers approve expenditures and track service utilization and monitor cost and performance. Administrative data are submitted when billing for care. These data are not explicitly collected to examine the health or healthcare of populations, but offer important advantages for this purpose [24].

Unfortunately, in the United States the health care delivery system is fragmented which impedes the creation of longitudinal, population based databases. Efforts have been made to centralize this information in medical registries. Thanks to increased availability of data and new health information exchange initiatives with centralized repositories, data from multiple medical registries and from electronic medical records can be stored in data warehouses and, thus are available to create meaningful insights [6,18]. Data from data warehouses are presented to decision makers using reporting tools (often referred to as business intelligence (BI) tools) such as Online Analytical Processing (OLAP) which display aggregated data to help decision makers make comparisons and observe trends [42]. One challenge to decision makers is that the data are usually displayed as point estimates (typically mean values) and do not contain information about instability (such as variation around the mean), so decision makers often are unaware of the presence of outliers or data errors. When aggregating data from several medical registries, the possibility of type mismatches and other integration problems, and well documented problems with data quality from the original data sources have the potential to create the illusion of data trends or data shifts where none exist. In these cases, a descriptive analysis of the data can often provide an understanding of any unusual patterns. Yet, the impact and importance of the variability of a point estimate or trend on a decision is dif<sup>fi</sup>cult to quantify, since it is highly subjective and dependent on the context of the decision being made.

To address this problem, we propose a measure of data variability termed an information volatility measure (IVM) and we introduce the notion of benchmarking the variability of data vis-à-vis a standard baseline to support better user understanding. Volatility is de<sup>fi</sup>ned as a measure of instability of underlying data: data that are relatively stable exhibit low volatility and vice-versa. We implement the IVM design in the health care context, in particular in the area of public health decision making and evaluate the effectiveness and utility of the design with expert users, through the use of focus groups. We calculate IVM based on the underlying distribution of the point estimate. We examine the two most common distributions we have found in aggregated health care data: a normal distribution and log normal distribution. For data that are normally distributed we argue that the coef<sup>fi</sup>cient of variation (i.e. the standard deviation divided by the mean) is best. For log normal data (as is often the case for time series data) we borrow from <sup>fi</sup>nance where the term ‘volatility’ connotes the variability of stock returns over time, namely the standard deviation of log-relative stock returns.

Because the best way to present the IVM to decision makers is not self-evident, we employ the design science research paradigm [17,21,36] to develop a presentation method and then re<sup>fi</sup>ne and evaluate the IVM measure. We implement the IVM using simple OLAP interfaces. The re<sup>fi</sup>nement and evaluation of the IVM is done by conducting four focus groups consisting of domain experts. Though the focus group technique is a qualitative approach, our epistemology is positivist. We introduce several manipulations within the focus groups to compare decisions made without the IVM measure and with several versions of the IVM. Additionally, we conduct two types of focus groups: exploratory and con<sup>fi</sup>rmatory [43]. The <sup>fi</sup>rst two (exploratory) focus groups are mainly used to provide feedback to be utilized for design changes and improvement of the IVM. The second two (con<sup>fi</sup>rmatory) focus groups to provide evidence of utility and ef<sup>fi</sup>cacy of the IVM metric in <sup>fi</sup>eld settings.

The remainder of this paper is organized as follows. We begin with a discussion of related work. We follow with a detailed de<sup>fi</sup>nition of information volatility and a description of how the information volatility measure is calculated and implemented. We describe how four focus groups were conducted and present the results of the evaluations. We conclude with a discussion of our <sup>fi</sup>ndings and suggest future research directions.

## 2. Related work

Information data products are manufactured much like any other product [3,30,31,34,38,46,48]. Information producers generate and provide the “raw material” which is stored and maintained by information systems (or custodians) and accessed and utilized by information consumers for their tasks [38,48], creating a data product. As in manufacturing, the data products are in turn the raw material for a different data manufacturing process [48]. Thus, just like the inputs and outputs of several manufacturing processes create a product supply chain, the input and output of a series of data manufacturing processes create an information supply chain [40].

The literatures on data quality [46] and on information manufacturing systems [3–5,30,33–35,47] have considered the quality of data derived from information supply chains. These supply chains may rely on human or automated agents to gather and transform data for analytic use directly on the desktop or indirectly through a more integrated data warehouse infrastructure. Regardless of the path through the information supply chain, the end-user is presented with (or helps create) an information product. Similarly to the way a consumer purchasing an off-the-shelf product wishes to know information about the product (such as the ingredients, instructions for use, or date of expiration), data consumers should be informed about information on the quality of data products [46].

In health care there has been a strong push to become an information-driven discipline. As a result, the amount of data stored in electronic medical registries is increasing rapidly [2]. Medical registries is a term used to describe databases that store clinical information collected as a byproduct of a patient's care [2]. A medical registry can be de<sup>fi</sup>ned as a systematic collection of a set of health and demographic data for patients with speci<sup>fi</sup>c health characteristics held in a de<sup>fi</sup>ned database for a prede<sup>fi</sup>ned purpose [26]. Medical registries are often used as tools to monitor and improve quality of care, as resources for epidemiological research [2], to describe patterns in medical care or effectiveness of therapies [26], for etiological research, for intervention program evaluation, for quality improvement, for health policy decision-making at local, state and national level [50], and for risk management [22]. Different medical registries serve as data repositories with speci<sup>fi</sup>c purposes. For example, some registries hold administrative data used primarily for billing purposes, others store encounter data, which are primarily used by payers for reimbursement, and <sup>fi</sup>nally enrollment data allows identi<sup>fi</sup>cation of demographic information [26].

Data sets that collect information from several medical registries are increasingly being used to address community health and health care process questions and are growing in popularity due to enhanced availability of data and new health information exchange initiatives [6,18]. These data repositories are aggregated at the population level and cut across traditional socioeconomic categories and geographic divisions. Recently, the societal bene<sup>fi</sup>ts of such data have been articulated clearly in a call for the creation of a national framework for the appropriate “secondary use of health data to expand knowledge about disease and appropriate treatments, strengthen understanding about effectiveness and ef<sup>fi</sup>ciency of health care systems, support public health and security goals, and aid businesses in meeting customers' needs.” [32, pg. 1]. Thus, these registries can be classi<sup>fi</sup>ed as source data for information supply chains that are used to make important decisions in health care.

In health care data, there are unique challenges with information supply chains. This is due to competing or con<sup>fl</sup>icting standards, data silos (due to fragmented health care delivery and concerns about data privacy), questionable accuracy of diagnosis codes [24], data entry errors [12,45,49], and changes in medical processes that lead to confusion. These errors are dif<sup>fi</sup>cult to track, since they are introduced at multiple points of the information supply chain [22]. As a result, data repositories created from information supply chains, such as medical registries, display the following characteristics: data sparseness, a very large number of dimensions, non-additive facts, and a constantly changing set of attributes [15]. It is no wonder that that both electronic and paper based registries show evidence of poor data quality. In fact, it is well documented that medical registries are often neither accurate nor complete [2,7,8,14,19,22,26,50]. Unfortunately, very little research focuses on data accuracy, reliability of medical registries [22,26,50], and the effects on accuracy of decisions made using decision support systems that use data from these registries [50].

In our research, we aggregated several registries in a data warehouse [6,39,42] and realized an important problem. Point estimates presented to users in OLAP tools in essence hid the data quality problems outlined above and lead to poor decision making. We describe this problem as an issue of data instability and the related concept of data volatility. Our thesis is that such unstable data exhibit high volatility and lead to poor decision making.

We use the term ‘volatility’ somewhat differently from the de<sup>fi</sup>nition traditionally used in the literature. Most data quality frameworks consider volatility as a part of timeliness of the data [3,47,48]. Ballou et al. [3] de<sup>fi</sup>ne the volatility of data by how long an information product remains valid. From this information product perspective, volatility is analogous to shelf life. Shelf life is less important when products do not spoil; while critical when they need to be sold within a certain window. Similarly, raw data or information products have a length of time during which they are valid and useful. Highly volatile data will have a short shelf life (for example stock quotes) and data with low volatility, such as the name of the <sup>fi</sup>rst president of the United States has an in<sup>fi</sup>nite shelf life [3]. Similarly Wang et al. [48], characterize volatility as an aspect of timeliness documenting how long the item remains valid.

In our research, we depart from this de<sup>fi</sup>nition and de<sup>fi</sup>ne volatility as a measure of rate of change in aggregated data values rather than relating to timeliness or shelf life. We propose a measure of volatility of aggregated data termed the information volatility measure (IVM).

Table 1  
Types of information volatility measures.

<table><tr><td>Information volatility</td><td>Definition</td></tr><tr><td>Intra-cell</td><td>In aggregated data, for example an average, the information volatility within the series of numbers that form that calculation</td></tr><tr><td>Inter-cell</td><td>When comparing values across groupings, the information volatility across those values</td></tr></table>

Information volatility is de<sup>fi</sup>ned as the rate of change or variability in the values of stored data. It follows that data that exhibit rapid and/or unpredictable changes are considered highly volatile, thus riskier to use.

The problem of volatility is well researched in the <sup>fi</sup>eld of <sup>fi</sup>nance. In <sup>fi</sup>nancial analysis, volatility is de<sup>fi</sup>ned as a standard measure of <sup>fi</sup>nancial vulnerability and is used to assess the risk/return tradeoffs in option pricing [23]. In fact much research in <sup>fi</sup>nance has focused on estimating volatility in data which is a measure of risk of a <sup>fi</sup>nancial instrument over a certain period of time. Similar to our context the source of volatility that lead prices to part from fundamental values are 1) the quality of the information used by market participants and 2) the complexity of the markets in which trades are affected [11].

## 3. Information volatility measure

There is a rich literature that documents decision making biases under uncertainty [44]. Information products inform decisions in the context of unknowns arising from complexity and inherent biases in our decision making abilities. It requires cognitive effort to reframe problems and mitigate our natural biases. Information volatility and this research agenda in general aim to develop quantitative measures that can be incorporated into information products to highlight potentially misleading uses of data.

Speci<sup>fi</sup>cally, our research is motivated by a recent <sup>fi</sup>eld study [42] where we noted several examples of unusual or unpredictable trends and averages in aggregated data from several information supply chains. In one example, health planners noticed an odd trend in heart disease that, after investigation, was due to changes in the data de<sup>fi</sup>nitions. Different data sources reported data with diverse de<sup>fi</sup>nitions for their calculations. Furthermore, even within a single data source, a change in IT staff can result in de<sup>fi</sup>nitional changes.

Another example was caused by seasonal changes, as is the case in Florida with both migrant workers and “snowbirds”. Yet another example was caused by sparsely populated groupings, where even a small change seemed very signi<sup>fi</sup>cant. All three of these scenarios indicate the presence of large variability or instability in the underlying data. In this section we de<sup>fi</sup>ne a potentially useful measure to capture and understand these issues: the information volatility measure.

<table><tr><td colspan="8">Page Items: Cancer:Lung &amp; Bronchus</td></tr><tr><td rowspan="2"></td><td>Hillsboro</td><td>Manatee</td><td>Orange</td><td>Osceola</td><td>Pasco</td><td>Pinellas</td><td>Seminole</td></tr><tr><td>Average Tumor Size</td><td>Average Tumor Size</td><td>Average Tumor Size</td><td>Average Tumor Size</td><td>Average Tumor Size</td><td>Average Tumor Size</td><td>Average Tumor Size</td></tr><tr><td>1994</td><td>3.96</td><td>3.53</td><td>4.67</td><td>6.41</td><td>3.68</td><td>6.93</td><td>4.71</td></tr><tr><td>1995</td><td>4.10</td><td>4.57</td><td>4.32</td><td>3.84</td><td>4.31</td><td>4.81</td><td>4.82</td></tr><tr><td>1996</td><td>8.85</td><td>5.50</td><td>4.02</td><td>4.11</td><td>5.65</td><td>5.94</td><td>4.71</td></tr><tr><td>1997</td><td>5.30</td><td>4.42</td><td>4.74</td><td>3.67</td><td>3.74</td><td>4.27</td><td>4.71</td></tr><tr><td>1998</td><td>4.26</td><td>4.63</td><td>4.72</td><td>4.69</td><td>3.71</td><td>4.19</td><td>4.17</td></tr><tr><td>1999</td><td>4.76</td><td>4.45</td><td>4.60</td><td>4.16</td><td>3.85</td><td>4.09</td><td>4.04</td></tr><tr><td>2000</td><td>4.25</td><td>4.44</td><td>4.13</td><td>5.29</td><td>4.09</td><td>4.18</td><td>3.67</td></tr><tr><td>2001</td><td>3.99</td><td>4.62</td><td>4.12</td><td>4.58</td><td>4.22</td><td>4.22</td><td>4.24</td></tr><tr><td>2002</td><td>4.27</td><td>4.48</td><td>4.25</td><td>4.55</td><td>3.44</td><td>4.18</td><td>4.24</td></tr></table>

Fig. 1. Example of intra-cell volatility.

<table><tr><td>SELECT avg(eod_tum_size)FROM fcds_cancersWHERE fcds_site_grp=&#x27;012&#x27; (code for stomach cancer)AND cat_year=&#x27;1997&#x27;AND cat_county=&#x27;12097&#x27; (code for Hillsborough County)</td></tr></table>

Fig. 2. Query for average tumor size at <sup>fi</sup>rst visit for patients in Hillsborough County.

## 3.1. Information volatility measure: definition

Information Volatility Measure (IVM) is de<sup>fi</sup>ned as a measure of instability in the values of aggregated data. According to our de<sup>fi</sup>nition, highly volatile data are riskier to use than those that are less volatile. Two forms of information volatility are identi<sup>fi</sup>ed in Table 1: inter-cell IVM and intra-cell IVM.

## 3.2. Intra-cell volatility

Using OLAP tools, aggregated data are calculated from a series of numbers and represent a summarized value for a particular set of grouping variables. The values of these aggregated <sup>fi</sup>elds can be deceiving. Take, for example, summarized data being shown as an average. This average is comprised of a series of numbers arriving from various sources with various levels of accuracy. In cases where the data are not tightly distributed around the mean, a central tendency may not be descriptive. The values that make up this average could have several outliers or <sup>fl</sup>uctuate signi<sup>fi</sup>cantly. Thus an average would not be a truly accurate representation of the data.

For example, the OLAP screen shown in Fig. 1 shows the average tumor size for lung cancer (based on real data), by county and year. In the year 1996 for Hillsborough County we <sup>fi</sup>nd an unusually large value. Based on our expert sense of these data, it is highly unlikely that this average is an accurate representation of central tendency. More than likely there are some outliers or some issues with data quality that compromise this particular unusual average.

## 3.3. Inter-cell volatility

Summarized values are frequently utilized to observe trends across a dimension such as the time dimension. For example, a decision maker may want to observe trends over time in rates of certain diseases for a certain county and decide if these rates are increasing, decreasing, or staying constant. The decision maker should be warned about interpreting or drawing any conclusion about trends that are sporadic or unstable.

## 4. Design of the information volatility measure

The stability of data from a certain source in the information supply chain can be examined by considering the rate of change and impact of change in the values it provides over a grouping variable or by its dispersion about a central tendency. Assuming a normal distribution, a con<sup>fi</sup>dence interval can give a decision maker a feel for the stability of the data. For example, a large con<sup>fi</sup>dence interval is indicative of data that are not tightly distributed along the mean, thus displaying volatility in its values. In this case, a point estimate is not a particularly reliable measure due to the instability of the underlying data.

![](/api/attachments/HAWDCF4H/fulltext/images/cbfc416b31940c3c0cfdadb9e8b2c9263af592d981359db91749da6de8fb9ea9.jpg)  
Fig. 3. Distribution of tumor size data

To investigate what distributions are present in our data streams, we used the ARENA software to identify distributions. We found the two most common to be log-normal and normal. When the data is log-normal we need to transform the data in order to achieve a more “well-behaved” distribution. This problem is well researched in the <sup>fi</sup>eld of <sup>fi</sup>nance. In <sup>fi</sup>nancial analysis, volatility is de<sup>fi</sup>ned as a standard measure of <sup>fi</sup>nancial vulnerability and is used to assess the risk/return tradeoffs in option pricing [23]. We borrow several calculations used in the <sup>fi</sup>nance <sup>fi</sup>eld, in particular those used to observe the behavior of <sup>fi</sup>nancial assets.

We begin with a description of these calculations, in particular, how logarithmic returns are calculated. We then extend these calculations to health care data. We use the coef<sup>fi</sup>cient of variation to decide if the underlying data are normally distributed or log-normally distributed. Once we determine the distribution of the data, we select which calculation to use for our IVM.

We follow with three examples utilizing real data from various healthcare information supply chains. Finally, in one of the most challenging steps, we illustrate various ways that IVM can be presented to a decision-maker. The data presentation methods are re<sup>fi</sup>nements which we designed thorough the help of exploratory focus groups.

## 4.1. Volatility in finance

In the <sup>fi</sup>eld of <sup>fi</sup>nance, volatility is de<sup>fi</sup>ned as a measure of uncertainty or risk based on the size of changes in a security's value [27]. A fund's volatility indicates the tendency of the returns to rise or fall in a short period of time. A volatile security is considered high risk because its performance may change quickly in either direction at any moment [10]. Frequently, the average price of a security will be different for each sub-period of history. In order to meaningfully measure volatility the mean around which the variability is measured has to be stable [23]. For this reason, a continuously compounded return is utilized. A continuously compounded return can be scaled over a longer time frame. For stock price volatility, for example, it is preferable to compute the continuously compounded return (also referred to as the log relative return) by using Eq. 1 below, with the assumption that the returns will be normally distributed. Here r is the return at time t and $p _ { t }$ is the price at time t and $p _ { t }$ is the price one period earlier:

$$
r _ {t} = \ln \left(\frac {p _ {t}}{p _ {t - 1}}\right).\tag{1}
$$

Volatility is calculated by using standard deviation where n is the number of periods, r is the mean return of the sample, and $r _ { t }$ is the return at time t (calculated as log relatives):

$$
\sqrt {\frac {1}{n - 1}} \cdot \sum_ {t = 1} ^ {n} (r _ {t} - \bar {r}) ^ {2}.\tag{2}
$$

A major assumption is that <sup>fi</sup>nancial asset prices are random variables that are log-normally distributed. The log-normal distribution is widely used in situations where values are positively skewed, for example in <sup>fi</sup>nancial analysis for security valuation or in real estate for property valuation [29]. The log-normal distribution allows prices to rise in<sup>fi</sup>nitely (though this would be a rare case), but they cannot fall below zero. There is some disagreement on the assumption of log-normality of stock price movements; however, empirical data have supported the log-normal distribution and it is generally accepted as a reasonable approximation [28].

Intuitively, this makes sense. Stock prices are usually positively skewed rather than normally (symmetrically) distributed. Stock prices exhibit this trend because they cannot fall below the lower limit of zero but might increase to any price without limit (thus they show a skewness). Other data have shown the same patterns, including property values, IQs, and latent periods (time from infection to <sup>fi</sup>rst symptoms) of infectious diseases. The three conditions that underlie the log-normal distribution are [29]:

1. The uncertain variable can increase without limits but cannot fall below zero.

2. The uncertain variable is positively skewed, with most of the values near the lower limit.

3. The natural logarithm of the uncertain variable yields a normal distribution.

## 4.2. Calculating IVM in the information supply chain

In order to calculate IVM in an information supply chain (ISC), we need to understand the distribution of the underlying data. The Coef<sup>fi</sup>- cient of Variation (CV) is useful to compare the standard deviations of variables with different units of measure. In probability theory and statistics, CV, also known as unitized risk, is a normalized measure of dispersion of a probability distribution and is expressed as percentage. The use of CV is practical for our purpose because the standard deviation of data must always be understood in the context of the mean of the data. CV is a dimensionless number so it is useful when comparing between data sets with different units or widely different means. This statistic measures the ratio of the standard deviation, σ, of a variable relative to its mean ${ } , \mu { }$ Thus:

$$
C V = \left[ \frac {(1 0 0) \cdot \sigma}{\mu} \right].\tag{3}
$$

As we extend the volatility calculation to an approximation of dispersion of the data, we need to consider whether the log-normal distribution is an accurate assumption. We adopt the following rule of thumb [29], since large coef<sup>fi</sup>cients of variation (N30%) are often associated with increased experimental variability [41]. If CV:

• Is greater than 30%, we assume a log-normal distribution and utilize Eq. (2) as the standard deviation of the log-returns to calculate the IVM of the series.

• Is less than 30%, we assume a normal distribution, and we use the CV as our IVM.

In summary we present either CV or the log-return as a measure of dispersion in the data. Though these are different measures, they are presented in the same unit (a percentage) and convey the same information (they are both measures of risk).

In the next sections we describe this technique with the two possible distribution assumptions, show examples of the calculations, and provide an interpretation of the measure. Rather than simulating the data, we utilize real data from various health care ISCs, including Florida's statewide cancer registry (Florida Cancer Data System at http://fcds.med.miami.edu). In addition, county data from the U.S. Census Bureau, demographic data from commercial sources, and an internally generated time dimension are used to construct the data cubes used in our examples.

## 4.2.1. Intra-cell IVM with a non-normal distribution

For an intra-cell example, we consider the information volatility within the calculation of an aggregated data average. In this example we <sup>fi</sup>nd the average tumor size for a certain cancer for each county in the data cube. Tumor size clinically serves as a simple predictor of tumor progression and survival of patients in gastric carcinoma [1]. Tumor size thus can be used as a predictor of survival (we can argue that counties with smaller average tumor sizes are more successful at identifying cancers at an early stage and starting treatment). As an illustration we consider the occurrences of stomach cancers in Hillsborough County in 1997, by utilizing the query shown in Fig. 2.

![](/api/attachments/HAWDCF4H/fulltext/images/07a0d850156ac03da1c31d27d0e037bd8b02ac45ff3784315085ea0f28e936ca.jpg)  
Fig. 4. Return values for stomach cancer data.

The average tumor size for this query is approximately 40.5 mm but we wish to have a measure of how indicative or reliable this number really is. The <sup>fi</sup>rst step is to decide which distribution to utilize. The CV for this series, which had $\mu { = } 4 0 . 5 , \sigma { = } 7 3$ is 180%, which is greater than the 30% for a normal distribution assignment, thus the log-normal transformation is used.

In order to check our assumption, we utilize ARENA software to <sup>fi</sup>t a log-normal distribution to these data (prior to transformation). As seen in Fig. 3, the assumption that the data are log-normal is appropriate.

The data are transformed by calculating the log-relative returns of each of the values. When the returns are plotted, we see a much tighter normal distribution (Fig. 4). We then calculate the standard deviation of the returns, which provides the information volatility for an average stomach cancer tumor size (118% volatility).

Assume that a decision maker is evaluating if Hillsborough County is effective at early detection of stomach cancer and thus is good at increasing chances of survival. This average would be compared to a benchmark or to a benchmark county. The large volatility of this average would indicate to a decision maker that using the reported average might be risky. In an OLAP tool, the decision maker may decide to “look under the hood”, perhaps investigating the data at a different granularity (looking at the monthly averages, for example, to see if this average is similar in every month).

## 4.2.2. Intra-cell IVM with a normal distribution

Some of the data encountered in health care are well described with a normal distribution. A good example of this is birth weight. Low birth weight in a region could be indicative of poor prenatal care [16]. The following example shows data from Florida's Vital Statistics records stored in a data warehouse. We query (Fig. 5) to obtain the average weight of boys born in Hillsborough County in the year 2000.

The data show an average of 3316 g and a standard deviation of 570 g. The $\mathrm { C V } = ( 5 7 0 / 3 3 1 6 ) * 1 0 0 = 1 7 \%$ which is below 30%, so we can assume the data are normally distributed. A histogram of the data shows that a normal distribution (Fig. 6) is appropriate. Thus we utilize the coef<sup>fi</sup>cient of variation as a measure for volatility (17%). A decision maker may be deciding whether Hillsborough County needs a program to improve prenatal care, and since the IV of this average is low should feel con<sup>fi</sup>dent using this number.

<table><tr><td colspan="2">SELECT weight_grams</td></tr><tr><td colspan="2">FROM vs_births</td></tr><tr><td colspan="2">WHERE cat_county=12097 (Hillsborough County)</td></tr><tr><td colspan="2">AND cat_gender=1 (boys)</td></tr><tr><td colspan="2">AND cat_year=2000;</td></tr></table>

Fig. 5. Query for Hillsborough County birth weight.

![](/api/attachments/HAWDCF4H/fulltext/images/4e98d45e49b6f98e197e05bb4c9b6dd517811ad5e90ae708aee36163451d1d98.jpg)  
Fig. 6. Histogram of birth weight of males in Hillsborough County.

## 4.2.3. Inter-cell IVM Measure

Summarized values are frequently utilized to observe trends and the inter-cell volatility measure is utilized to help a decision maker judge the stability of an observed trend. A decision maker may be utilizing trends to get a feel for the future behavior of data. The IVM can help a decision maker get a feel for the variability in the trend and the trend's stability for use for future prediction. In this case we illustrate data where we assume log-normal distribution since in the great majority of the cases trends are observed across time periods.

As an example we examine breast cancer volumes by county<sup>1</sup>. A downward trend in breast cancer incidence in a region can indicate improvements in the management of breast cancer [9]. By observing monthly volumes of breast cancer diagnosis for each county we build a cube with the query shown in Fig. 7.

In Fig. 8 we examine the volumes for breast cancer in Clay County to understand if the downward trend is true for this particular county. We build the OLAP cube in EXCEL (linked to an ORACLE database) and include a chart with a linear trend line. There appears to be a downward trend but from the chart the data seem volatile. In this example information on volatility may give the decision maker a feel for the “jumpiness” in this trend.

Fig. 9 illustrates how IVM may be presented to a decision maker. This particular trend has about 70% volatility which indicates that the trend has quite a bit of variation.

## 4.3. Interpreting the IVM measure

IVM is interpreted as a percentage. For example, if a volatility of 10% has the mean of 0 (a return of zero means no change in the values of the data) due to the properties of a normal distribution, we can say:

• with a probability of 68.3% (1 standard deviation from the mean) the returns will exhibit a change within [−10%, +10%],

• with a probability of 95.4% (2 standard deviations) the returns will exhibit a change within [−20%, +20%]

• with a probability of 99.7% (2 standard deviations) the returns will exhibit a change within [−30%, +30%].

All three interpretations (for one, two, or three standard deviations) can be provided to a decision maker, but for ease of understanding, the <sup>fi</sup>rst (a single standard deviation) is suf<sup>fi</sup>cient to communicate the volatility of the data. Fig. 10 illustrates the calculated volatility. In this particular example, the decision maker is examining the trend in monthly volumes of breast cancer diagnosis by county. The IVM of 19.79% explains the level of volatility in the data. It is probably suf<sup>fi</sup>cient for a decision maker to consider the one standard deviation interpretation particularly if the focus is to compare the volatility of this trend to that of another trend.

<table><tr><td>SELECT</td><td>sum(fcds_cancers.cat_count),fcds_cancers.cat_county,fcds_cancers. month,fcds_cancers.year,fcds_sites.site_label,counties.county_name</td></tr><tr><td>FROM</td><td>counties, fcds_sites, fcds_cancers</td></tr><tr><td>WHERE</td><td>counties.county_id = fcds_cancers.cat_county ANDfcds_cancers.fcds_site_grp = fcds_sites.code</td></tr></table>

Fig. 7. Query on counts of cancer occurrences by month and county.

## 4.3.1. Benchmarking

To improve the interpretation of our numerical IVM, we apply the local volatility model as part of a benchmarking approach. This approach is also common in stock indices [20]. While we propose future studies to investigate the potential set of benchmarks for different types of health care data, the initial approach is to roll up to the largest granularity. For example, if considering a trend in monthly volumes of breast cancer occurrences for a certain county in Florida, we would calculate the volatility in the monthly volumes for the entire state of Florida as a benchmark. We prototyped three presentation designs:

1. Number Benchmark. Reporting numerical values for volatility by calculating IVM for the benchmark. Fig. 11 shows an example in which the IVM for a county is benchmarked against the state's IVM for the data under study.

2. Graphic Benchmark. By graphing the return both for the trend of interest and its benchmark (on the same scale). Fig. 12 shows an example for the same data as shown in Fig. 11. The red line represents the benchmark volatility; the blue line represents the actual volatility of the trend.

3. Category Benchmarking. Assigning a category to the level of IVM in comparison to the benchmark of Low, Medium, or High. For our example we arbitrarily set 50% or higher as HIGH, 30% to 50% as MEDIUM, and lower than 30% as LOW. Ideally these sensitivities would be set by the decision-maker. Fig. 13 demonstrates showing IVM as a category.

## 5. Re<sup>fi</sup>nement and evaluation of IVM using focus groups

The design of artifacts can be described as having two phases: the development of the artifact and its evaluation. This is a process which involves frequent iteration between development and evaluation rather than a strictly procedural approach [25]. A design researcher not only designs an artifact but must provide evidence that this artifact solves a real problem. After careful consideration of several possible evaluation techniques we decided to evaluate the IVM using expert focus groups. We contend that there are several key reasons focus groups are an appropriate evaluation technique for design research projects. We <sup>fi</sup>nd focus groups give us <sup>fl</sup>exibility, the ability to directly interact with domain experts and probe them on key design ideas, the ability to collect both qualitative and quantitative data, and <sup>fi</sup>nally we <sup>fi</sup>nd that the interaction between respondents gives us key insights that normally do not surface in face to face interviews [43].

We utilize two types of focus groups. Exploratory focus groups (EFG) are used for the design and improvement of the IVM and con-<sup>fi</sup>rmatory focus groups (CFG) are used for gathering evidence of the IVM's ef<sup>fi</sup>cacy and utility in the application <sup>fi</sup>eld. In the <sup>fi</sup>rst phase, EFGs are used to provide feedback for improvement both to the design of the proposed measure and the focus group questioning route/coding procedures. In the second phase, no more changes are made to the IVM nor to the questioning and the CFGs are used to evaluate the measure's functionality, completeness, usability, and the impact of the measure on the data analysis strategies of the decision-makers [43].

## 5.1. Approach

Though the focus group technique is primarily a qualitative approach, our epistemology is positivist. We introduce several manipulations within the focus groups to compare decisions made without the IVM measure and also with several presentation versions of the IVM. The strategy is to present the dashboards <sup>fi</sup>rst without and then with the IVM in order to detect differences in the collective decision making processes. Making the decision without the IVM is akin to the decisions being currently made by decision makers using BI tools that only report point estimates. This experimental design allows us to measure changes in decision making, speci<sup>fi</sup>cally to discover if better decisions are made.

In order to correctly design the focus group scripts and identify quali<sup>fi</sup>ed participants, the research goals are clearly identi<sup>fi</sup>ed for each type of focus group. Both EFG and CFG share the <sup>fi</sup>rst goal: To solicit participant feedback about the utility and efficacy of the IVM. Utility was de<sup>fi</sup>ned as “usefulness of the measure” and ef<sup>fi</sup>cacy as “having the ability to change data analytic strategies”. The additional research goals for the EFGs are:

<table><tr><td>COUNTY</td><td>Clay</td><td></td></tr><tr><td>SITE</td><td>Breast</td><td></td></tr></table>

![](/api/attachments/HAWDCF4H/fulltext/images/6163873d5d28b41b9a1aa3a94920a2f9130e417390e8405f59bf11d1ba3366ef.jpg)

![](/api/attachments/HAWDCF4H/fulltext/images/372aa9f88747f17a775e1c5f903c16c54977951ceb792d9422b9d90d398887ca.jpg)  
Fig. 8. Volatility in breast cancer monthly volumes.

![](/api/attachments/HAWDCF4H/fulltext/images/b2b1afd0250e2801d52be97fcecf1472010b793ec8ba0b58511e7c299bf94a78.jpg)  
Fig. 9. Volatility metric.

• To solicit participant feedback on how to improve the usability and presentation of IVM.

• To analyze transcribed data in order to improve the focus group script and coding schema.

For the CFGs an additional research goal is to collect evidence of the utility and ef<sup>fi</sup>cacy of the IVM.

The planning process included creating a carefully planned script in which the IVM was presented to the participants in the context of a health care decision. “Vignettes” or story lines are used to create decision scenarios based on health care situations with realistic health care data. These decision scenarios are based on the decisions we observed in the <sup>fi</sup>eld study [6,42]. The focus group participants are asked to make a decision both before receiving information about the volatility of the data and after. A sample vignette is shown in Table 2.

Participants are asked to compare several series of numbers and a graph (with a linear trend line) that describes a trend. A claim is made that counties neighboring Miami-Dade were better at early detection/ prevention of breast cancer based on their decreasing trend lines on volumes of cases while the trend line was <sup>fl</sup>at for Miami-Dade. Yet, several of the counties selected for comparison exhibited large jumps in values and thus were probably less reliable leading to an unrealistic comparison from which to draw any conclusions. The participants are asked to make a judgment by observing a trend line on a graph, as well as the actual numbers, and then again, after introducing and presenting the IVM for each series of numbers.

Fig. 14 provides details about the focus group evaluation procedure and results. All the focus groups took place in a conference room and with a duration of 1 hour. The vignettes were presented on an overhead screen with the moderator navigating the OLAP interfaces. The moderator explained the vignettes, the OLAP tool, and the decision problem. After the explanations, the participants formulated their group decision based on the data in the OLAP tool. The participants could navigate the cube by asking the moderator to show greater/lower granularity or different <sup>fi</sup>ltering and grouping variables.

Each focus group was recorded (sound only) and professionally transcribed. The initial template was created by two of the researchers after a reading of the transcript. Using a “rolling interview” [37] approach, incremental changes were made after each of the exploratory focus groups based on feedback from an observer and the focus group participants.

Additionally, based on feedback from the <sup>fi</sup>rst focus group, a change was made to how the IVM was presented. The participants had a dif<sup>fi</sup>cult time understanding the IVM and the importance of the value for decision making. For the next exploratory focus group, rather than just presenting a numeric value for IVM, the graph and benchmark IVM information was added to the OLAP screen to provide a richer pictorial feel of the variability in the data (see Figs. 11 and 12).

After the completion of both of the exploratory focus groups two types of changes were made based on participant comments: 1) changes to the focus group methodology and 2) an additional change to the IVM benchmark presentation (by adding the categorical

![](/api/attachments/HAWDCF4H/fulltext/images/66ddd573057a2ea9a79a5c6d24be7e4cb368d0e911a72c80a1b9f61a8b14cf33.jpg)  
Fig. 10. IVM presentation with standard deviation interpretations.

Volatility for Breast Cancer Volumes,Collier County

<table><tr><td></td><td>Actual</td><td>Benchmark</td></tr><tr><td>Monthly Volatility</td><td>32.76%</td><td>14.06%</td></tr></table>

Fig. 11. Numerical presentation of IVM benchmark.

benchmark, see Fig. 13). Participants in the second exploratory focus group still had dif<sup>fi</sup>culty interpreting the IVM so further benchmarking information was added. Benchmarking included a graphical presentation, a numerical presentation, and a categorical presentation (medium, high, low) of benchmarking data as described in the previous section.

## 5.2. Focus group results

IVM design evaluation is accomplished by interpreting and analyzing the data collected in the four focus groups [37]. Utility and ef<sup>fi</sup>cacy are investigated using the coded qualitative data shown in Table 3.

## 5.2.1. Utility of the information volatility measure

Utility is de<sup>fi</sup>ned as “usefulness of the IVM” and ef<sup>fi</sup>cacy as “having the ability to change data analytic strategies”. To analyze utility of the IVM all passages that were coded as “design features” were analyzed. Table 4 summarizes the utility evaluation by focus group. In general all the groups found IVM to be a useful measure.

For the exploratory focus groups, benchmarking was not used and the participants stated that just a numeric representation was dif<sup>fi</sup>- cult to understand. They had a hard time interpreting what the IVM number meant as demonstrated by the following comments:

“I think it would depend on the user. I mean, I think we would be able to <sup>fi</sup>gure it out, and I think a lot of people would, but I think a lot wouldn't.”

“Yeah, the volatility one is a little – I think a little more – dif<sup>fi</sup>cult. Well, because people don't have a lot of background in what that means.”

The benchmarking idea was a design feature that was added after the exploratory focus groups. For example, one participant stated:

“You (need to) draw a line in the sand and say, this is a problem, this is not. And maybe if it goes over that line, it pops up and says, ‘Hey, check this out.’”

This was corroborated by the con<sup>fi</sup>rmatory focus groups. For example a participant stated:

“…benchmarking is a necessary component of it.”

Benchmarking Volatility- Breast Cancer Collier County  
![](/api/attachments/HAWDCF4H/fulltext/images/e5fb2d931f3f0048fac5969f01fc1f539f065189c0d2ed673e9a14dde968d637.jpg)  
Fig. 12. Graphical volatility benchmarking.

Volatility for Breast Cancer,Collier County

<table><tr><td colspan="2">Volatility Level is</td><td>MEDIUM</td></tr><tr><td></td><td>Actual</td><td>Benchmark</td></tr><tr><td>Monthly Volatility</td><td>34.02%</td><td>14.06%</td></tr></table>

Fig. 13. Category volatility benchmarking

Two of the focus groups were extremely enthusiastic about the utility of the IVM. For example a participant in a con<sup>fi</sup>rmatory focus group stated:

“I like that calculation and the idea of having a measure or measuring and giving you this kind of information.”

In fact, most of the focus group participants made very similar comments and discussed several ways that this measure would be useful in their current jobs. For example a participant related:

“So this – this applied to an example of the VA where you have some nursing homes that have less than 30 beds, small n's can make it 5 percent – 10 percent change as opposed to a 300 bed plus facility where it takes 25 people to get the same kind of, you know, impact. So we can use this.”

Another participant found the benchmarking information useful relating it to issues in their workplace:

“It's keeping the institutional memory to what those numbers really mean because you know we — we've sat over at this end and don't see much. Okay, let's compare that example of like Tampa to Miami and/or you're looking at costs or you're looking at clinical wait times or something and then you have some sort of huge variation between the two and you can make a conclusion like they don't know what they're doing… and then you get down to the numbers and the nitty gritty and you talk to someone over there and say oh, we're in a transition period and we've got some issues with our data.”

## 5.2.2. Efficacy of the IVM measure

We describe ef<sup>fi</sup>cacy as the changes in decision making strategies when the participants are asked to make a series of decision with and without the use of the IVM. Ef<sup>fi</sup>cacy results are summarized in Table 5.

The counties included in our sample decision making vignette (see Table 2) were highly volatile but, in general, most focus groups prior to receiving IVM thought Miami-Dade was not declining as rapidly as other counties. For example, prior to seeing the IVM a participant in one of the con<sup>fi</sup>rmatory groups noted:

“No, they're not doing as well, because they have a straight across line, and there's no decrease; whereas the other two counties that you showed had a decrease.”

Most focus groups changed their decisions once they were informed about the volatility in the data. When information on volatility was available, the participants were less likely to compare trends if one of the trends were labeled as highly volatile. In the case of this vignette,

## Table 2

Summary of a sample focus group vignette

<table><tr><td>Claim</td><td>IVM concern</td></tr><tr><td>Counties neighboring Miami-Dade are better at early detection/prevention of breast cancer based on volumes of cases</td><td>Examine this trend and investigate if this is a plausible claim based on potential data volatility</td></tr></table>

Evaluation coding template.  
![](/api/attachments/HAWDCF4H/fulltext/images/b988ac1ba6f22eaaabaed2efccd37da66d33aaa6e2bae51390b8c9e94cdde76f.jpg)  
Fig. 14. Summary of focus group evaluations of IVM.

both con<sup>fi</sup>rmatory focus groups reversed their prior decision since the counties that were being compared to Miami-Dade had high IVM values.

One of the focus groups, however, had dif<sup>fi</sup>culty “buying into” the reality of such a scenario, though they found this measure useful and saw the potential for its use in their daily tasks. They did show some changes in data analytic strategies when they decided they would “think like a manager”:

Table 3

<table><tr><td>Construct</td><td>Template code</td><td>Definition</td></tr><tr><td>Utility</td><td>Design features</td><td>Mention of the information volatility feature, design improvement suggestion</td></tr><tr><td>Efficacy</td><td>Volatility before</td><td rowspan="2">Strategies to deal with volatility prior to receiving measure.Interpretation before.Strategies to deal with volatility after receiving measure.Interpretation after.</td></tr><tr><td>Efficacy</td><td>Volatility after</td></tr></table>

“… if I were a manager and I'm looking at these trend lines and one looks <sup>fl</sup>at and one looks down and the variability looks about the same, you know it's not huge on one or huge on another, I think I'd be asking what's going on. I think I'd say you know what are they doing right and what are we doing wrong here or whatever.”

<table><tr><td>Focus group</td><td>Evidence of utility</td><td>Counter-evidence of utility</td></tr><tr><td>EFG1</td><td>Yes</td><td>Difficulty interpreting</td></tr><tr><td>EFG2</td><td>Yes</td><td>Difficulty interpreting</td></tr><tr><td>CFG1</td><td>Yes – saw several instances where this would be useful in their daily data analysis</td><td>None</td></tr><tr><td>CFG2</td><td>Yes</td><td>None</td></tr></table>

Table 5  
Changes in data analytic strategies.

<table><tr><td>Focus group</td><td>Change in data analytic strategies?</td><td>Comments/observed changes</td></tr><tr><td>EFG1</td><td>Yes</td><td></td></tr><tr><td>EFG2</td><td>Yes</td><td></td></tr><tr><td>CFG1</td><td>Slight</td><td>Rejected task, group disliked low realism of the vignettes.</td></tr><tr><td>CFG2</td><td>Yes</td><td></td></tr></table>

Based on our experiences, we are encouraged by the reception of the IVM by the expert focus group participants. We are excited by the emergence of rich ideas and concepts from the focus group technique. Unlike traditional interviews and one-on-one prototyping, focus groups generate interactive conversations among the participants. The comments and the language used by the target audience regarding the IVM and the discussions that led to a <sup>fi</sup>nal consensus helped point to design <sup>fl</sup>aws and areas for improvement such as the idea of benchmarking for better interpretability. Additionally, we are able to capture data that may not have been evident with a structured technique. For example, though CFG2 did not buy the realism of the vignette, they still saw applicability of the IVM to their daily data analysis tasks.

## 6. Discussion and future work

In our research, we investigate an important issue: the instability of the underlying data for point estimates and trends used in tools that present aggregated data, such as OLAP, spreadsheet or reporting tools. Statisticians are well aware that aggregated values should always be presented with a measure of con<sup>fi</sup>dence, yet this is rarely done in practice. Decision makers rarely consider the reliability of the underlying data when they formulate their decisions. As a result, they may be making decisions based on data that are not representative of the population. This is particularly important in health care since we are moving into an era where health information is readily accessible and transferable. Health care has increasingly become an information-centric activity. A well-known problem in both electronic and paper based health registries is poor data quality, yet such questionable data are increasingly being used for evidence-based decision making.

Using design science research methods we design an information volatility measure (IVM) to inform and aid decision makers with incomplete and inconsistent data by describing the rate of change in the values of stored data. The calculation is based on the underlying distribution and is grounded on prior research in <sup>fi</sup>nance, an area that examines risk and future behavior using data that shares similarities with data that are found in health care information supply chains.

Through the use of focus groups, we found that comparative techniques, such as benchmarking, are promising approaches in communicating information volatility to decision makers. We found clear evidence to indicate that focus group participants <sup>fi</sup>nd the IVM useful in the three presentation modes (number, graphic, and category) studied. The majority of the focus groups changed vignette decisions when faced with the IVM knowledge.

We observed some limitations in the use of focus groups in the evaluation of the IVM. Generalization to a larger population can be dif<sup>fi</sup>cult for several reasons. The <sup>fi</sup>rst is due to the convenience nature of focus group recruiting practices. It is particularly dif<sup>fi</sup>cult to <sup>fi</sup>nd quali<sup>fi</sup>ed participants when evaluating artifacts due to the technical nature of the subject which limits the pool of possible participants. Additionally, individual responses cannot be considered because of the interaction between respondents and between respondents and the moderator. Also, a strongly opinionated member may bias the results and discourage other participants from speaking, as we saw in one of the focus groups.

For future research we plan to further re<sup>fi</sup>ne the design and use of IVM. For this research, the measure was implemented on a simple cube. A more complex and fully implemented cube solution will certainly provide some further research challenges, including issues with decreased execution time in OLAP navigation and space overhead. Other interesting areas for future research are:

1. When and how should the IVM be shown to decision-makers? For example, should IVM be presented as part of the ISC or as metadata describing the ISC?

2. Should the IVM be shown only if there is signi<sup>fi</sup>cant volatility in the data?

3. Which benchmarking presentation mode (number, graphic, or category) is most effective and will the effectiveness vary by decision making scenario?

4. In what other contexts besides health care will information volatility be pertinent and will other contexts require changes in the IVM calculations?

We currently have initiated a study using controlled experiments to clearly understand the impacts of the IVM on decision making. In this study, we will investigate how the decision biases outlined by Tversky and Kahneman [44], such as insensitivity to sample size and anchoring and adjustment, play a role in the calculation and presentation of the IVM.

Finally, we also plan to investigate, through the use of simulations, how to communicate volatility in different data distributions not considered in this study (for example, hospital arrivals that may exhibit a Poisson distribution).

## References

[1] Y. Adachi, T. Oshiro, M. Mori, Y. Maehara, K. Sugimachi, Tumor size as a simple prognostic indicator for gastric carcinoma, Annals of Surgical Oncology 4 (2) (1997) 137–140.

[2] D.G.T. Arts, N.F. de Keizer, G.-J. Scheffer, De<sup>fi</sup>ning and improving data quality in medical registries: a literature review, case study, and generic framework, Journal of the American Medical Informatics Association 9 (6) (2002) 600–611.

[3] D. Ballou, R. Wang, H. Pazer, G.K. Tayi, Modeling information manufacturing systems to determine information product quality, Management Science 44 (4) (1998) 462–484.

[4] D.P. Ballou, H.L. Pazer, Modeling data and process quality in multi-input, Multi-Output Information Systems Management Science 31 (2) (1985) 150–162.

[5] D.P. Ballou, H.L. Pazer, Modeling completeness versus consistency tradeoffs in information decision contexts, Knowledge and Data Engineering, IEEE Transaction on 15 (1) (2003) 240–243.

[6] D.J. Berndt, A.R. Hevner, J. Studnicki, The CATCH data warehouse: support for community health care decision-making, Decision Support Systems 35 (3) (2003) 367.

[7] E.S. Berner, D.E. Detmer, D. Simborg, Will the wave <sup>fi</sup>nally break? A brief view of the adoption of electronic medical records in the United States, Journal of the American Medical Informatics Association 12 (1) (2005) 3–7.

[8] E.S. Berner, J. Moss, Informatics challenges for the impending patient information explosion, Journal of the American Medical Informatics Association 12 (6) (2005) 614–617.

[9] M.P. Coleman, Trends in breast cancer incidence, survival, and mortality, The Lancet 356 (9229) (2000) 590–591.

[10] S. Croome, Understanding volatility measurements, http://www.investopedia com/articles/mutualfund/03/072303.asp2003.

[11] L.A. Cunningham, How to think like Benjamin Graham and invest like Warren Buffett, McGraw-Hill, New York, 2001.

[12] M.R. Dambro, B.D. Weiss, Assessing the quality of data entry in a computerized medical records system, Journal of Medical Systems 12 (3) (1988) 181–187

[13] R.A. Deyo, D. Cherkin, D. Conrad, E. Volinn, Cost, controversy, crisis: low back pain and the health of the public, Annual Review of Public Health 12 (1) (1991) 141–156.

[14] B.C. Drolet, K.B. Johnson, Categorizing the world of registries, Journal of Biomedical Informatics 41 (6) (2008) 1009–1020

[15] T.I. Eggebraaten IW. Tenner LC. Dubbels A health-care data model based on the HL7 reference information model IBM Systems Journal 46 (1) (2007) 5–18.

[16] R.D. Gorsky, J.P. Colby Jr., The cost effectiveness of prenatal care in reducing low birth weight in New Hampshire, Health Services Research 24 (5) (1989) 583–598.

[17] S. Gregor, D. Jones, The anatomy of a design theory, Journal of the Association for Information Systems 8 (5) (2007) 312.

[18] J. Harrison Jr., R. Aller, Regional and national health care repositories, Clinics in Laboratory Medicine 28 (1) (2008) 101–117.

[19] S. Hasan, R. Padman, Analyzing the effect of data quality on the accuracy of clinical decision support systems: a computer simulation approach, AMIA Annual Symposium, 2006, pp. 324–328.

[20] D. Heath, E. Platen, Local volatility function models under a benchmark approach, Quantitative Finance 6 (3) (2006) 197–206.

[21] A. Hevner, S. March, J. Park, S. Ram, Design science research in information systems, Management Information Systems Quarterly 28 (1) (2004) 75–105.

[22] W.R. Hogan, M.M. Wagner, Accuracy of data in computer-based patient records, Journal of the American Medical Informatics Association 4 (5) (1997) 342–355.

[23] S. Hotopp, Practical issues concerning volatility and its measurement past and predicted, in: I. Nelken (Ed.), Volatility in the Capital Markets : State-of-the-art Techniques for Modeling, Managing, and Trading Volatility, Glenlake/Fitzroy Dearborn, Chicago; London; New Delhi, 1997, pp. xii, 224.

[24] L.I. Iezzoni, Risk Adjustment for Measuring Health Care Outcomes, 3rd ed. Health Administration Press, Chicago, 2003.

[25] B. Kuechler, V. Vaishnavi, On theory development in design science research: anatomy of a research project, European Journal of Information Systems 17 (5) (2008) 489.

[26] M.N. Levine, J.A. Julian, Registries that show ef<sup>fi</sup>cacy: good, but not good enough, Journal of Clinical Oncology 26 (33) (2008) 5316–5319.

[27] J. McClave, P.G. Benson, T. Sincich, Statistics for Business and Economics, Ninth ed. Pearson Prentice Hall, Upper Saddle River, NJ, 2005.

[28] L.G. McMillan, McMillan on Options, J. Wiley, New York, 1996

[29] J. Mun, Real Options Analysis : Tools and Techniques for Valuing Strategic Investments and Decisions, 2nd ed. John Wiley & Sons, Hoboken, N.J., 2006

[30] A. Parssian, S. Sarkar, V.S. Jacob, Assessing data quality for information products: impact for selection, projection, and Cartesian product, Management Science 50 (7) (2004) 967–982.

[31] L.L. Pipino, Y.W. Lee, R.Y. Wang, Data quality assessment, Communications of the ACM 45 (4ve) (2002) 211–218.

[32] C. Safran, M. Bloomrosen, W.E. Hammond, S. Labkoff, S. Markel-Fox, P.C. Tang, D.E. Detmer, Toward a national framework for the secondary use of health data: an American medical informatics association white paper, Journal of the American Medical Informatics Association 14 (1) (2007) 1–9.

[33] G. Shankaranarayan, Y. Cai, Supporting data quality management in decisionmaking, Decision Support Systems 42 (1) (2006) 302–317.

[34] G. Shankaranarayan, M. Ziad, R.Y. Wang, Managing data quality in dynamic decision environments: an information product approach, Journal of Database Management 14 (4) (2003).

[35] G. Shankaranarayanan, Y. Cai, Supporting data quality management in decisionmaking, Decision Support Systems 42 (1) (2006) 302–317.

[36] H.A. Simon, The Sciences of the Arti<sup>fi</sup>cial, 3rd ed. MIT Press, Cambridge, MA, 1996.

[37] D.W. Stewart, P.N. Shamdasani, D.W. Rook, Focus Groups: Theory and Practice, 2nd ed. Sage Publications, Newbury Park Calif., 2007.

[38] D.M. Strong, Y.W. Lee, R.Y. Wang, 10 potholes in the road to information quality JEEE Computer 30 (8) (1997) 38–46.

[39] J. Studnicki, A.R. Hevner, D.J. Berndt, S.L. Luther, Comparing alternative methods for composing community peer groups: a data warehouse application, Journal of Public Health Management and Practice 7 (6) (2001) 87–95.

[40] S. Sun, J. Yen, Information supply chain: a uni<sup>fi</sup>ed framework for informationsharing, in: SpringerLink (Ed.), Intelligence and Security Informatics, Springer, Berlin/ Heidelberg, 2005, pp. 422–428.

[41] S.L. Taylor, M.E. Payton, W.R. Raun, Relationship between mean yield, coef<sup>fi</sup>cient of variation, mean square error, and plot size in wheat <sup>fi</sup>eld experiments, Communications in Soil Science and Plant Analysis 30 (9) (1999) 1439–1447.

[42] M.C. Tremblay, R. Fuller, D. Berndt, J. Studnicki, Doing more with more information: changing healthcare planning with OLAP tools, Decision Support Systems 43 (4) (2007) 1305–1320.

[43] M.C. Tremblay, A.R. Hevner, D.J. Berndt, Focus groups for artifact re<sup>fi</sup>nement and evaluation in design research, Communications of the Association for Information Systems 26 (1) (2010).

[44] A. Tversky, D. Kahneman, Judgment under uncertainty: heuristics and biases, in: D. Kahneman, P. Slovic, A. Tversky (Eds.), Judgment Under Uncertainty:Heuristics and Biases, Cambridge University Press, Cambridge, 1982.

[45] M.M. Wagner, W.R. Hogan, The accuracy of medication data in an outpatient electronic medical record, Journal of the American Medical Informatics Association 3 (3) (1996) 234–244.

[46] R. Wang, M.P. Reddy, A. Gupta, An object-oriented implementation of quality data products, WITS-93, 1993, Orlando, Florida.

[47] R.Y. Wang, M.P. Reddy, H.B. Kon, Toward quality data: an attribute-based approach, Decision Support Systems 13 (3–4) (1995) 349–372.

[48] R.Y. Wang, V.C. Storey, C.P. Firth, A framework for analysis of data quality research, IEEE Transactions on Knowledge and Data Engineering 7 (4) (1995) 623–640.

[49] R. Wilton, A.J. Pennisi, Evaluating the accuracy of transcribed computer-stored immunization data, Pediatrics 94 (6) (1994) 902–906.

[50] S.S. Yoon, M.G. George, S. Myers, L.J. Lux, D. Wilson, J. Heinrich, Z.-J. Zheng, Analysis of data-collection methods for an acute stroke care registry, American Journal of Preventive Medicine 31 (6, Supplement 2) (2006) S196–S201.

![](/api/attachments/HAWDCF4H/fulltext/images/c5afadc9ecba0aef81e39c83e46b71bbd9a03bce3e9efc847bdf3971e81c1743.jpg)

Monica Chiarini Tremblay is an Assistant Professor in the Decision Sciences and Information Systems Department in the College of Business Administration at Florida International University in Miami. Her research interests focus on data analytics and business intelligence, data and text mining, data quality, data warehousing, decision support systems and knowledge management, particularly in the context of healthcare. Speci<sup>fi</sup>cally, she concentrates on electronic health records, health information exchanges and medical passports. Dr. Tremblay is the principal and co-investigator on several large federally and state funded grants. Her work has been published in European Journal of Information Systems, Communications of the AIS, ACM

Journal of Data and Information Quality, Information Technology and Management, Decision Support Systems, Journal of Computer Information Systems, and Health Progress

![](/api/attachments/HAWDCF4H/fulltext/images/1796266eb184e6498f1827d07514290e50f8a2d35c15bc687d57978623aef11d.jpg)

Alan R. Hevner is an Eminent Scholar and Professor in the Information Systems and Decision Sciences Department in the College of Business at the University of South Florida. He holds the Citigroup/Hidden River Chair of Distributed Technology. Dr. Hevner's areas of research interest include information systems development, software engineering, distributed database systems, healthcare information systems, and service-oriented computing. Dr. Hevner has co-authored a 2010 book on design science research, presented seminars internationally on the topic, and co-founded an international annual conference (Design Science Research in Information Systems and Technology – DESRIST) that is in its sixth vear. He has published over 150

research papers on these topics and has consulted for a number of Fortune 500 companies. Dr. Hevner received a Ph.D. in Computer Science from Purdue University. He has held faculty positions at the University of Maryland and the University of Minnesota. Dr. Hevner is a member of ACM, IEEE, AIS, and INFORMS. Recently, he served as a program manager at the U.S. National Science Foundation in the Computer and Information Science and Engineering (CISE) Directorate.

![](/api/attachments/HAWDCF4H/fulltext/images/a2196459324405c997143b66a77a6779585ba8ff9067d7dcffabbf4764bdafbd.jpg)

Donald J. Berndt is an associate professor in the Information Systems Decision Sciences Department at the University of South Florida in Tampa. His areas of expertise include data mining, business intelligence. bioterrorism surveillance, and healthcare data warehousing and management. His work on business intelligence and the role of data in effective bioterrorism surveillance systems was published in Decision Support Systems: Special Issue on Cybersecurity for Homeland Security. Other papers have been published journals such as the American Journal of Preventive Medicine and Journal of Computer Information Systems. A frequent presenter at academic conferences, Berndt also coauthors for computer science textbooks and serves as chief technology of<sup>fi</sup>cer for a healthcare information management company.
