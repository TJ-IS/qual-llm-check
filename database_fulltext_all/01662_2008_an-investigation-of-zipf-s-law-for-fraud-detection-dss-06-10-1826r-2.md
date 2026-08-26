---
otero_id: 1662
otero_key: "8KXYBQ7E"
title: "An investigation of Zipf's Law for fraud detection (DSS#06-10-1826R(2))"
authors: "Shi-Ming Huang; David C. Yen; Luen-Wei Yang; Jing-Shiuan Hua"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.05.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An investigation of Zipf's Law for fraud detection (DSS#06-10-1826R(2))

Shi-Ming Huang <sup>a</sup>, David C. Yen <sup>b,</sup>⁎, Luen-Wei Yang <sup>a</sup>, Jing-Shiuan Hua <sup>c</sup>

<sup>a</sup> Department of Accounting & Information Technology, National Chung-Cheng University, Chia-Yi, Taiwan, ROC

<sup>b</sup> Department of DSC & MIS, Miami University, Oxford, OH 45056, United States

<sup>c</sup> Department of Information Management, National Chung-Cheng University, Chia-Yi, Taiwan, ROC

## a r t i c l e i n f o

Article history: Received 5 October 2006 Received in revised form 4 May 2008 Accepted 25 May 2008 Available online 16 July 2008

Keywords: Fraud detection Zipf's Law Benford's Law Quasi-experiment research Misclassi<sup>fi</sup>cation cost matrix

## a b s t r a c t

Fraud risk is higher than ever before. Unfortunately, many auditors lack the expertise to deal with the related risks. The objectives of this research are to develop an innovative fraud detection mechanism on the basis of Zipf's Law. The purpose of this technique is to assist auditors in reviewing the overwhelming volumes of datasets and identifying any potential fraud records. The authors conducted Quasi-experiment research on the KDDCUP'99 benchmark intrusion detection dataset to verify the performance of the proposed mechanism. The simulation experimental results demonstrate that Zipf Analysis can assist auditors to locate the source of suspicion and further enhance the resulting audit processes.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Fraud risk is higher than ever before. According to the results of KPMG's Fraud Survey of 2003, organizations are reporting more experiences of fraud than in prior years [16]. In 2003, 75% of surveyed companies reported that they experienced an instance of fraud, an increase of 13% as compared with 1998. Furthermore, Ernst & Young's Global Survey pointed out that the main contributing factors to the prevalence of fraud are the growing complexity of organizations and systems, changes in business processes and activities, enormous and ever-expanding volumes of transaction data, outdated and ineffective internal controls and so on [11]. Complex organizations and transactions lead to increased opportunity for subjective interpretation, borderline disclosure and even misrepresentation.

Auditors must take fraud prevention and awareness seriously. The main reason is that the occupational fraud issue against organizations is a costly business problem. The economic impact can be signi<sup>fi</sup>cant: up to 6% of organizations' revenues may be lost annually as a result of fraud and abuse [3].<sup>1</sup> Within the United States, this translates into losses of approximately \$660 billion. Furthermore, the true cost of fraud goes beyond the <sup>fi</sup>nancial loss to the impact on reputation, diversion of management focus, and loss of morale and trust within teams [11]. However, recent corporate scandals clearly indicate the potential for fraud abuse and many auditors lack the skills and expertise to deal with the related risks.

It is clear that there is a critical need to implement some technology solutions to auditing areas, especially the data analysis technique [17]. Proper data analysis is critical as a means of allowing auditors to streamline audit processes, bring fraudulent activities to light before they result in critical losses, minimize <sup>fi</sup>nancial losses, and ensure compliance with business rules and external regulatory requirements, such as SAS 410 and SOX.

In this research, the authors propose an innovative mechanism of analytical review procedure, named “Zipf Analysis” that utilizes the conception of Zipf's Law to facilitate the systematic construction of a fraud detection model. For the purpose of building such fraud detection systems, we examine the properties of Zipf's Law and evaluate its capability of discriminating abnormal records from a simulation experiment on the KDDCUP'99 intrusion detection dataset, and revising the fraud detection system to provide a higher level of accuracy and ef<sup>fi</sup>ciency.

This paper is organized as follows: Section 2 reviews related literatures about analytical procedures: Benford's Law and Zipf's Law. Section 3 describes the systematic mechanism of the fraud detection model on the basis of Zipf's Law. Sections 4 and 5, present a simulation experiment for the system implementation and evaluation of the proposed mechanism by comparing other fraud detection methods. Finally, the conclusions of this study are provided in Section 6.

## 2. The problem and related work

Fraud by nature is composed of the following three categories: intentional illegal act, the concealment of that act, and deriving a bene<sup>fi</sup>t from that act [5,8]. In recent years, deceptive behaviors have been transformed and have emerged into new paradigms, such as money laundering, etc. Fortunately, it is indeed the case that some enterprise-wide fraud can be systematically detected with the assistance of emerging information technologies. Conventionally, data analysis approaches using power laws have been adopted as a feasible artifact to offer valuable assistance to fraud detection in computer auditing operations.

Benford's Law is actually one of the most commonly utilized power laws for fraud detection. The underlying concept Benford's Law states that in the lists of numbers obtained from real-life data resources, the distribution of leading digit is a long-tail distribution [4]. To this end, many prior researchers have proved that auditors could improve their performance by conducting analytical procedures before utilizing substantive tests [10,12,25,32]. For example, the study of Reed and Pence [25] examines the appropriateness of Digital Analysis as an analytical review procedure to determine the possibility of <sup>fi</sup>nancial statement fraud. They indicate that using Digital Analysis in analytical procedures can be more effective or ef<sup>fi</sup>cient than tests of details in reducing detection risk for speci<sup>fi</sup>c <sup>fi</sup>nancial statement assertions. In addition, the Statement of Auditing Standards No. 410 also suggested that auditors should apply analytical procedures at the planning stage to assist in understanding the business and in identifying areas of potential risk. On the other hand, some studies in the accounting area have also suggested that Digital Analysis could be used as an analytical review procedure to assist auditors in identifying any possible fraud issues. However, there are some limitations while using Benford's Law for fraud detections [30]. The restrictions noted by the author include the following:

1) Some populations of accounting-related data do not conform to a Benford distribution [10] [18,19]. For instance, we found that in some businesses, numbers (especially monetary amounts) in transactions are not a natural set. For example, when evaluating a data <sup>fi</sup>le of travel claims you might <sup>fi</sup>nd that the <sup>fi</sup>rst-two-digit combination of 24 appears more often than expected with Benford's Law. This might happen if the company has a policy that stipulates that reimbursement claims for \$25 and above must be supported with receipts — so travelers claim a lesser amount, such as \$24.95. Therefore, it is hard to use Benford's Law when the amounts are mostly identical.

2) Using Digital Analysis may generate too many cases to review [30]. As an example, in a database containing 250,000 records, one expects that approximately 12,250 records will start with 10. Should one <sup>fi</sup>nd 15,000 numbers starting with 10, there is a doubt, and we still have to check 15,000 transactions. Therefore, we understand that some other <sup>fi</sup>lters are necessary to narrow down these sets of data to a manageable size and to reduce some noisy data.

3) When execute analytical procedures with Benford's Law, auditors only can use the data of digital shape for analysis. However, Statements on Auditing Standards, SAS 410, suggests that analytical procedures should be designed to consider each kind of different data shape simultaneously and identify the interrelation of <sup>fi</sup>nancial and non-<sup>fi</sup>nancial data.

Although Digital Analysis using Benford's Law had been proven to facilitate auditor review on overwhelming volumes of data and transactions, there are many drawbacks from using this particular method. After completing related literature review we found another power law by the name of Zipf's Law. The basic concept of Zipf's Law is that the frequency of the word occurrence in an article in fact furnishes a useful measurement and hence, management of word signi<sup>fi</sup>cance: The product of frequency of the use of words, f, and the rank order, r, is approximately constant [39]. Many scholars believe that Benford's Law is a special case of Zipf's Law [21]. According to Zipf's Law, we believe we can use Zipf's Law to verify the frequency of string or date <sup>fi</sup>elds in records. Therefore, this research aims to construct an analytical procedure mechanism on the basis of Zipf's Law and further test its performance of detecting anomalies by comparing with other fraud detection algorithm. The following Table 1 summarized the comparison between Digital Analysis using Benford's Law and Zipf's Law, accordingly.

The concept of Zipf's Law has also been adopted in the area of Information Retrieval. Information Retrieval (IR) typically involves problems inherent to the collection process for a corpus of documents, and then provides functionalities for users to <sup>fi</sup>nd a particular subset of it by constructing queries [13]. Basically, the idea of IR implementation revolves around an attempt to systematically extract information from available document corpora, and then utilize it to determine whether or not each document is relevant to a particular request [28]. Among the various IR models, the Vector Space Model (VSM) is one of the most popular and successful approaches for modeling in the IR associated environment [1,9,26]. In addition, the basic idea of VSM is relying on the belief that the frequency of terms in a document usually follows a Zipf distribution, meaning that a small number of keywords can categorize a document's content [35]. In other words, it involves the similarity determination between documents and resulting queries, and the corresponding, weights evaluation for keywords appeared in the documents or queries.

Comparison between Benford's Law and Zipf's Law

<table><tr><td>Benford&#x27;s Law</td><td>Zipf&#x27;s Law</td></tr><tr><td colspan="2">They are both derived from Nature Laws.They can be used to handle disaggregated account level data.They both follow the principle of Power Law.</td></tr><tr><td>Shows relationship between digit and frequency.Numeric attributes are required</td><td>Shows relationship between rank and frequency.No pre-requirements defined for type of attributes.</td></tr><tr><td>Applied for fraud detection already</td><td>Under review as a potential tool for fraud detection</td></tr></table>

A variety of prior studies have been focused on the application of Zipf's Law in IR systems. In addition to the TF-IDF weighting mechanism employed in the Information Retrieval environment, another category of studies is focused on the modeling of communication using Zipf's Law. For example, some prior studies such as Adamic's [2] and Ramanathan's [23] recommended applying power laws to model the multicast strategy in the distributed IR network. Since the “good peers” in the entire network are determined by analyzing users' experience from Zipf's Law, the strategy of selective <sup>fl</sup>ooding in a distributed IR network can be systematically con<sup>fi</sup>gured.

It is indeed a fact that both laws match with a power law distribution and the advantages had been con<sup>fi</sup>rmed in many <sup>fi</sup>nancial and accounting dataset [7,15,19,22]. One obvious difference between them is that Zipf's Law can verify diverse attributes other than numeric attribute [31,37]. Therefore, this study would like to explore an innovative analytical procedure based on Zipf's Law to verify the frequency of string or date attributes, and to further con<sup>fi</sup>rm its ability to detect fraud records.

So far, there is no literature that explores the possibilities of Zipf's Law being applied to auditing and accounting-related problems. According to prior literature, most accountingrelated data can be expected to conform to a Benford distribution [10,14]. Therefore, this research believes that most accounting-related dataset might also follow Zipf's Law. Since Benford's Law had been con<sup>fi</sup>rmed as a special case of Zipf's Law [21]. Our research intends to design an innovative fraud-detecting model, which can conduct some other examinations based on Zipf's Law to verify the frequencies of any speci<sup>fi</sup>c patterns of a given dataset. In addition, we expect that it might be able to improve the performance of analytical procedures for auditors.

## 3. System architecture

The aim of this research is to investigate the properties of Zipf's Law for detecting anomalies in a complicated dataset. According to Zipf's Law, the pattern's frequency under a study is inversely proportional to the rank [24]. Therefore, we use Zipf Analysis to verify the frequencies of patterns, which are the combination of any speci<sup>fi</sup>c attributes of records in a given dataset.

## 3.1. Overview

In Fig. 1, we conceptually demonstrate the architecture of Zipf Analysis for fraud detection. According to Zipf's Law, the frequency of occurrence of various complex patterns or natural languages would follow a power law. Therefore, we make an assumption that, in a given dataset, if any patterns frequency does not follow Zipf's Law; then it might imply that there are some anomalies existing.

First of all, auditors should generate some patterns in accordance with a speci<sup>fi</sup>c audit objective. Consequently, by comparing the theoretical frequency distribution, predicted by Zipf's Law, with actual frequency distribution, then one could discriminate abnormal patterns in the analyzed datasets and further identify possible fraud issues.

## 3.2. Mechanism of Zipf Analysis

Zipf's Analysis is an approach used to distinguish abnormal data from normal and help facilitate discovery of potential fraud issues from an extensive dataset. The Zipf

![](/api/attachments/8KXYBQ7E/fulltext/images/dd3a617e8bc559288dffee4d19cb756092443a289bada4051114549dbd4d4c5f.jpg)  
Fig. 1. Fraud detection model of Zipf Analysis.

analytical procedure has several distinct steps that begin with the determination of audit objectives and data acquisition. The following step focuses on preliminary works, in which relevant and valid data is sought for consequent analysis. The third step is patterns generation, which is an invaluable process of Zipf Analysis, because it is the most distinctive features from Digital Analysis. At this point, the data is ready to be utilized for Zipf Analysis. Finally, the analyzed outcomes can be summarized and visualized for sifting anomalies from normality. According to these results, auditors can determine whether to conduct a further fraud detection process. The complete mechanism of Zipf analysis is demonstrated in Fig. 2.

## 3.3. Draft an audit program

An analytical procedure assignment must begin with clear objectives in mind. These objectives must state clearly the scope of the study and the potential goals that are dependent on a comprehensive risk assessment and auditors' professional judgments. One can, thus, successfully matriculate through the following described tasks.

![](/api/attachments/8KXYBQ7E/fulltext/images/090e54154a3cbc963075ae901b19c6646b25562e2bd81ab35e4176706824135d.jpg)  
Fig. 2. The mechanism of Zipf Analysis

![](/api/attachments/8KXYBQ7E/fulltext/images/05fa9e1d45d0bf17e0b7b985ecda769113973a89befbfd601081545ed3ed6bc2.jpg)  
Fig. 3. Pattern generation.

Next, the preliminary tasks include: customer discussions, data extraction and data validation and cleaning [33]. In this stage, data elements of interest are located and extracted. In other words, one should transform existing data into more relative and clearer views. Preliminary works also include data validation and cleaning, which ensures that accurate elements are being incorporated into the examination.

## 3.4. Zipf Analysis

There are six sub-processes in the second phase. First of all, auditors should generate desired patterns in accordance with a speci<sup>fi</sup>c audit objective. Next, auditors can calculate the actual and theoretical frequency distributions. Then we use statistical testing to identify any possible anomalies which may have signi<sup>fi</sup>cantly deviated from theoretical value as predicted by Zipf's Law. Each step is described below.

## 3.4.1. Phase 1. Patterns generation

This stage, distinguished from Digital Analysis, is a key and distinctive process in the initial implementation of Zipf Analysis. This stage can be subdivided into four sub-processes (See Fig. 3). First, auditors have to select some signi<sup>fi</sup>cant attributes in accordance with a speci<sup>fi</sup>c audit objective. Secondly, one can generate any pattern desired combining speci<sup>fi</sup>c attributes. Third, the auditor should use distinct content for the purpose of understanding all characteristics of analyzed patterns. Finally, in order to carry on further analysis, auditors should count the frequency of each pattern and sort them accordingly based on their frequency.

3.4.1.1. Step 1. Attributes selection. This process is the most distinctive feature between Zipf Analysis and Digital Analysis. The main reason is that Digital Analysis can only focus on the numeric attributes. However, Zipf Analysis can analyze not only the numeric attributes but also the string or date attributes. For example, if we think about a healthcare insurance claim, we will have patient identi<sup>fi</sup>cation, doctor identi<sup>fi</sup>cation, date of service, billing date, diagnosis code, and treatment code, etc. In Zipf Analysis, auditors can use more complete and meaningful attributes to examine their legitimacy of frequency of occurrences. The algorithm of attributes selection is shown in Table 2.

3.4.1.2. Step 2. Patterns generation. Note that, a speci<sup>fi</sup>c pattern is composed of any given attributes in accordance with the audit objective (see Table 3).

3.4.1.3. Step 3. Distinct content. According to the result of selected attributes, auditors can then calculate all possible patterns by using the algorithm (Table 4):

3.4.1.4. Step 4. Count and rank. Auditors can use below (see Table 5) algorithm to sort analyzed patterns based on their frequency.

## 3.4.2. Phase 2. Actual frequency distribution of patterns

First of all, auditors should calculate the actual frequency of occurrence (f ) of each pattern, and sorting out these patterns according to their frequency, i.e. a rank (R ) is assigned to each pattern, with R<sub>i</sub>= 1 for the most frequent one. A power law

$$
f _ {i}: R ^ {- \zeta}\tag{1}
$$

with an exponent ζ is next obtained on a log–log plot. The appearance of this power law is due to the presence of a socalled hierarchical structure in writing a text.

## 3.4.3. Phase 3. Theoretical frequency distribution of patterns

In this step, we calculate the expected frequency of occurrence of analyzed attributions, which is predicted by Zipf's Law. The theoretical value is mainly for the purposes of distinguishing abnormal data from the observed value.

Algorithm of distinct content

SELECT DISTINCT Patterns FROM table\_name

Carlos [6] has suggested that a Zipf's Law test is sometimes constructed by estimating, through ordinary least squares and to check whether the estimate of $\beta _ { 1 }$ is close to −1. Thus, we calculate the theoretical value by the utilizing the regression below:

$$
\ln (f _ {i}) = \beta_ {1} \times \ln (R _ {i}) + \beta_ {2} + \varepsilon_ {i}\tag{2}
$$

where the slope $( \beta _ { 1 } )$ equals to minus one, and the constant $( \beta _ { 2 } )$ is derived from the average values of $\bar { f } _ { i }$ and $\bar { R } _ { i }$ and the estimate $\hat { \beta } _ { 1 }$

$$
\beta_ {2} = \overline {{f}} _ {i} - \hat {\beta} _ {1} \times \overline {{R}} _ {i}\tag{3}
$$

where ${ \hat { \beta } } _ { 1 } = 1 .$ In our case $\bar { \mathbf { \xi } } _ { i } = \frac { \sum _ { i = 1 } ^ { N } l n ( f _ { i } ) } { N } \mathop { \mathrm { a n d } } \overline { { R } } _ { i } = \frac { \sum _ { i = 1 } ^ { N } \ln ( R _ { i } ) } { N } .$

Once the estimates of the slope and the constant had been obtained, auditors can then calculate each pattern's theoretical value and graph its frequency distribution in accordance with this regression.

## 3.4.4. Phase 4. Interval estimating and testing

The con<sup>fi</sup>dence interval can assist auditors in pinpointing anomalies which deviate from the theoretical value as predicted by Zipf's Law [10,19,32]. The con<sup>fi</sup>dence interval testing can assists auditors in narrowing down the sample size and avoiding any arbitrary conclusion.

First, auditors should estimate the con<sup>fi</sup>dence interval of $\beta _ { 1 }$ and $\beta _ { 2 } .$ . Once the upper and lower bounds of $\lvert \beta _ { 1 }$ and $\beta _ { 2 }$ had been obtained, auditors then could estimate the con<sup>fi</sup>dence interval of theoretical value by bring them back to the original regression. Then, how to estimate the con<sup>fi</sup>dence interval of $\beta _ { 1 }$ and $\beta _ { 2 }$ is introduced, respectively.

3.4.4.1. Step 1. The confidence interval $o f \beta _ { l } .$ First of all, we use formula (4) to calculate the interval estimation of slope (β ) with 1−α con<sup>fi</sup>dence level, in which α is the critical value.

$$
\left(\hat {\beta} _ {1} - t _ {n - 2, \frac {\alpha}{2}} \times S (\hat {\beta} _ {1}), \hat {\beta} _ {1} + t _ {n - 2, \frac {\alpha}{2}} \times S (\hat {\beta} _ {1})\right)\tag{4}
$$

where $\beta _ { 1 } = - 1$ and $t _ { N - 2 , \frac { \alpha } { 2 } }$ can be obtained from a statistical table of the t distribution. In addition, $S ( { \hat { \beta } } _ { 1 } )$ means the estimated standard deviation of slope (See formula (5)).

$$
S \left(\hat {\beta} _ {1}\right) = \hat {\sigma} / \sqrt {\sum_ {i = 1} ^ {n} \left(f _ {i} - \bar {f}\right) ^ {2}}\tag{5}
$$

where

$$
\hat {\sigma} = \sqrt {\frac {\sum_ {i = 1} ^ {N} (f _ {i} - f _ {\mathrm{tv}}) ^ {2}}{N - 2}}
$$

3.4.4.2. Step 2. The confidence interval of $\beta _ { 2 } .$ Second, we calculate interval estimation of the constant (β ) with 1−α con<sup>fi</sup>dence level, in which α is the critical value.

$$
\left(\hat {\beta} _ {2} - t _ {n - 2, \frac {\alpha}{2}} \times S (\hat {\beta} _ {2}), \hat {\beta} _ {2} + t _ {n - 2, \frac {\alpha}{2}} \times S (\hat {\beta} _ {2})\right)\tag{6}
$$

where $t _ { N - 2 , \frac { \alpha } { 2 } }$ can be obtained from a statistical table of the t distribution. In addition, $S ( \hat { \beta } _ { 2 } )$ means the estimated standard deviation of the constant (See formula (7)).

$$
S \left(\hat {\beta} _ {2}\right) = \hat {\sigma} \times \sqrt {\frac {1}{N} + \frac {\bar {f} ^ {2}}{\sum_ {i - 1} ^ {N} \left(f _ {i} - \bar {f}\right) ^ {2}}}\tag{7}
$$

where

$$
\hat {\sigma} = \sqrt {\frac {\sum_ {i = 1} ^ {N} (f _ {i} - f _ {\mathrm{tv}}) ^ {2}}{N - 2}}.
$$

3.4.4.3. Step 3. Confidence interval of theoretical value. According to the interval estimation of $\beta _ { 1 }$ and $\beta _ { 2 } ,$ , we then can calculate the upper and lower bounds of theoretical frequency, by bring them back to the original regression.

$$
\left(\hat {\beta} _ {1 - \text { Lower }} \times R _ {i} \times \hat {\beta} _ {2 - \text { Lower }}, \hat {\beta} _ {1 - \text { Upper }} \times R _ {i} + \hat {\beta} _ {2 - \text { Upper }}\right)\tag{8}
$$

Auditors could use below algorithm (See Table 6) to determine which observation value deviate from theoretical value.

## 3.4.5. Phase 5. Z-statistic testing

The Z-score is a statistical signi<sup>fi</sup>cance test used in inference, which determines whether the difference between the observed value and the theoretical value are statistically signi<sup>fi</sup>cant [19,32] [36]. In other words, auditors can use the Z-statistic test to examine the null hypothesis of no manipulative effort in the chosen datasets by comparing the observed frequency for each pattern to the expected frequency of occurrences as predicted by Zipf's Law.

To perform a signi<sup>fi</sup>cance test of the observed deviations from the expected values, we used a normally distributed Zstatistic, suggested by Skousen [32]:

$$
Z = \frac {\left| f _ {i} - f _ {\mathrm{tv}} \right|}{\sigma}\tag{9}
$$

In above formula, $f _ { i }$ is the actual frequency, $f _ { \mathrm { t v } }$ is the theoretical value and $\mathbf { \sigma } \mathbf { \mathbf { { \sigma } } } \mathbf { \mathbf { { \sigma } } } \mathbf { \mathbf { { \sigma } } } \mathbf { \mathbf { { \sigma } } } \mathbf { \mathbf { { ( } } } \mathbf { \frac { 1 } { \mathbf { { ( } } N \mathrm { { - } } 1 ) } } \times \sum _ { i = 1 } ^ { N } \left( f _ { \mathrm { { t v } } } \mathbf { \bar { { \mathbf { \sigma } } } } \mathbf { \mathbf { { \bar { f } } } } _ { \mathrm { { t v } } } \right)$ is the standard deviation of the theoretical value.

Table 6 Algorithm of con<sup>fi</sup>dence interval

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Let
 $\alpha=$ critical value
 $x_{i}=$ actual frequency, where i=1, 2, 3...N.
 $(x_{\text{low}}, x_{\text{up}})=\text{confidence interval}$ $\alpha=1\%$ 
Do While  $\alpha\leq100\%$ 
Calculate Confidence Interval
If  $x_{i}\leq x_{low}$  or  $x_{i}\geq x_{up}$ 
Then go Step 5: Z-statistic testing
Else
 $\alpha=\alpha-1\%$ 
Loop
</div>

These Z-statistics would reject the null hypothesis at the 10%, 5%, and 1% level if their values exceed 1.64, 1.96, and 2.57, respectively. For example: when Z-score≥1.96, it means there is a 95% con<sup>fi</sup>dence level to make a conclusion about the observation values which one signi<sup>fi</sup>cantly deviate from the theoretical values. The algorithm of Z-statistic testing is demonstrated in Table 7.

## 3.4.6. Phase 6. Results display

After all above analyses, auditors should summarize all analyzed outcomes and demonstrate them in the form of a graph and table in order to facilitate the speed of recognition of the unusual situations.

## 3.5. Substantive testing

Zipf Analysis is an analytical review procedure. The purpose of Zipf Analysis is to permit auditors to <sup>fi</sup>lter any potential fraud records, which have abnormal frequency pattern. However, we cannot promise that Zipf Analysis has 100% accuracy in fraud detection. Any analytical review procedures just can assist the auditors in planning the nature, timing and extent of other audit procedures [34]. Therefore, further substantive testing must be conducted.

Substantive testing means a more detailed examination, designed to obtain more accurate audit evidences to support or deny previous analytical procedure outcomes. Substantive testing usually includes a great deal of human resource and auditors' subjective judgments. Following, we will detail how to perform the substantive testing.

In previous phases, the raw data was clustered into two clusters, normal cluster and suspicion cluster, by Zipf Analysis. Zipf Analysis can <sup>fi</sup>lter some patterns that have abnormal frequency of occurrences. Then, auditors should check all of the records in the signi<sup>fi</sup>cant deviations. In addition, auditors should review the source documents or conduct an interview for those records and transactions, in order to obtain the evidence to explain these anomalies.

Consequently, auditors should understand and rationalize the reasons for these deviations before dismissing any of them. If anything comes up that heightens suspicion, a detailed background search will begin.

## 4. Quasi-experiment research

In this section, we conduct an experiment to examine the performance of Zipf Analysis. The rest of this chapter is organized in the following manner: we start with an illustration of our research strategy; quasi-experiment research. Next, an overview of the attempts for intrusion detection systems using the KDDCUP'99 dataset will be described. In the third section, we present the design of our simulation experiment and followed by system implementation. Finally, we end this chapter with a brief discussion of our experiment results.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm of Z-statistic testing
Let
 $\alpha=$ critical value
 $Z_{i}=Z-score$ , where  $i=1,2,3,\ldots$ $\alpha=1\%$ 
Do While  $\alpha\leq100\%$ 
Calculate Z-score
If  $Z_{i}\geq Z-score$  under standard normal distribution
Then go Phase 3: Substantive testing
Else
 $\alpha=\alpha-1\%$ 
Loop
</div>

## 4.1. Research strategy

The experiment research methodology is one of the best approaches to verify the effectiveness and ef<sup>fi</sup>ciency of a theoretical model [27]. In our study, we proposed an innovational fraud detection system by using Zipf's law, which is a new thought for audit. However, there are some similar techniques that exist, such as Digital Analysis. For this experiment, we conduct a quasi-experiment study to make a comparison with related fraud detection systems, and we use the KDDCUP'99 intrusion detection dataset as benchmark. Furthermore, we set some key performance indicators to examine the effectiveness and ef<sup>fi</sup>ciency of Zipf Analysis.

Our quasi-experimentation is designed to examine the performance of fraud detection with different treatments. There are two different fraud detection systems; one considers Zipf Analysis as the pre-process stage, another without any pre-process. Therefore, our quasi-experimentation study can be formulated as:

$$
\begin{array}{c} A: X _ {1} \to Y _ {1} \\ B: X _ {2} \to Y _ {2} \end{array}\tag{10}
$$

where $X _ { 1 }$ is the <sup>fi</sup>rst treatment, with Zipf Analysis as the preprocess, and result in the output of $Y _ { 1 } ; ~ X _ { 2 }$ is the second treatment, without Zipf Analysis as the pre-process, and generate the output of $Y _ { 2 }$

## 4.2. KDDCUP'99 contest problem

This is the dataset used for The Third International Knowledge Discovery and Data Mining Tools Competition, which was held in conjunction with KDD-99 The Fifth International Conference on Knowledge Discovery and Data Mining. The competition task was to build a network intrusion detector, a predictive model capable of distinguishing between “bad” connections, called intrusions or attacks, and “good” normal connections. This database contains a standard set of data to be audited, which includes a wide variety of intrusions simulated in a military network environment. The attributes of this dataset can refer to KDDCUP'99 benchmark dataset<sup>2</sup>. In this study, the fraud detection system is evaluated on the KDDCUP'99 intrusion detection dataset2. Two reasons that we choose this dataset are described below.

1) Organizations were more concerned about computer crimes. Ernst & Young's Global Survey pointed out that more than half of surveyed companies were concerned about computer crimes (See Fig. 4). Beyond 70% of respondents felt that intrusion attacks were awful computer crimes.

![](/api/attachments/8KXYBQ7E/fulltext/images/ff6700d23b9cee9e0e7e34833b87af0980770c065b2f026a498ceb272e39023a.jpg)  
Fig. 4. Organization concerned fraud.

2) Zipf Analysis is very suitable for detecting attacks that have frequent sequential patterns, for example: Denial-of-Service, Surveillance and other Probing attacks. Because the DOS and Probing attacks involve many connections to some host(s) in a period of time, this implies that some patterns that have abnormal occurrence frequency may appear.

## 4.3. Processes of experimentation

We separated two groups by assigning two different treatments based on Fig. 5, the <sup>fi</sup>rst group without any preprocess and the second group with Zipf Analysis as preprocess before intrusion detection classi<sup>fi</sup>cation. In the second group, we run three experiments to examine the effectiveness of our fraud detection mechanism. Each experiment is divided into two phases. The <sup>fi</sup>rst phase is based on Zipf Analysis as pre-process. The purposes of using Zipf Analysis are to improve the quality of row data for later classifying, promote the ef<sup>fi</sup>ciency of auditing, and raise the reliability of outcome. Thus, the Zipf Analysis includes the following <sup>fi</sup>ve kinds of roles: (1) simplifying the raw data for later classifying, (2) verifying the pattern of raw data whether corresponding nature law, (3) <sup>fi</sup>ltering anomalies infringing the patterns of nature laws, (4) discriminating normal and abnormal clusters, and (5) providing the potential dataset with evidences of intrusion.

After we <sup>fi</sup>ltered any anomalies which transgress the patterns of nature laws, we started the second phase: data mining for intrusion detection classifying. In this phase, we used a data mining algorism, proposed by the winning entry of KDDCUP'99, for classifying the patterns of intrusion attacks towards the anomalies <sup>fi</sup>ltered in the <sup>fi</sup>rst phase. In order to compare with the winner of KDDCUP'99, we performed the same data mining algorism, C5.0 Decision Tree with a mixture of bagging and boosting, which was proposed by Bernhard et al. [20]. According to Bernhard [20], the initial setting was a kind of inverted cross-validation, where the data was split into ten folds. Only one fold was always used for learning (the training set) and all the other nine folds for testing (the testing sets). Furthermore, for the purpose of comparison, the <sup>fi</sup>rst group performs the same data mining algorism directly without any pre-process. The process of quasi-experiment process can be illustrated in Fig. 5.

![](/api/attachments/8KXYBQ7E/fulltext/images/c831386f06f0db063d88a703ea26d4cb682633feae55603e5c80574829166a7c.jpg)  
Fig. 5. Quasi-experiment process.

Note that the difference between three experiments in the <sup>fi</sup>rst group is the setting of critical value in the <sup>fi</sup>rst phase. With regard to existing experimental literature, we take 1%, 2% and 5% as the critical value for Zipf Analysis. Therefore, the amount of <sup>fi</sup>ltered data for each experiment in the <sup>fi</sup>rst phase will be different. In second phase, data mining is considered for these different <sup>fi</sup>ltered datasets, generated in the <sup>fi</sup>rst phase, based on the C5.0 Decision Tree algorism. Finally, our experiment results were compared with the winner of KDDCUP'99. The signi<sup>fi</sup>cant reasons for using Zipf Analysis as pre-process before classifying of intrusion detecting process are described below:

1) Easy to apply the nature law. Zipf Analysis is derived from nature laws and no pre-requirements de<sup>fi</sup>ned for type of attributes. Therefore, Zipf Analysis can facilitate intrusion detection based on nature law in this study.

2) Easy to <sup>fi</sup>lter the anomalies. By con<sup>fi</sup>rming the pattern of raw data whether corresponding nature law, the abnormal data transgressing nature law can be easily extracted from the complicated raw data.

3) Easy to detect the fraud. By means of classifying the patterns of intrusion attacks towards the anomalies <sup>fi</sup>ltered by Zipf Analysis, the range of the dataset for classi<sup>fi</sup>cation can be narrowed and the accuracy of intrusion detection can be improved.

Our simulation experiments were performed on an Asus desktop with a 2.6 GHz Celeron(R) processor and 1 GB RAM running Microsoft Windows XP. We mainly used auditing software: Audit Command Language (ACL) and Microsoft Excel to perform Zipf Analysis, and used SPSS Clementine 7.2 to perform the data mining process.

## 4.4. Results of experimentation

After completion of all above analysis processes, Zipf Analysis separates the raw data into two clusters: Attacks and Normal. The distribution of raw data can be referred from Yang's research [38]. Zipf Analysis has discriminated the most attack records into the Attack Cluster. We <sup>fi</sup>nd that the performance of Zipf Analysis for <sup>fi</sup>ltering anomalies is indeed better than 100% sampling under each level of critical value. In addition, we obtained the best performance when set the critical value under the level of 2%. Therefore, we expected that it could enhance the performance of using data mining for detecting and classifying intrusion records.

## 5. System evaluation

In this research, the system evaluation can be separated into two phases in accordance with the design of simulation experimentation. First we use Audit Hit Rate and the Bayes Theorem to measure the accuracy of Zipf Analysis in the <sup>fi</sup>rst phase of our experiment. Next, we use the confusion matrix, the total misclassi<sup>fi</sup>cation cost and the average misclassi<sup>fi</sup>cation cost to examine the performance of our simulations.

## 5.1. Audit Hit Rate

Audit Hit Rate (AHR) is an easy-to-use approach to determine the accuracy of a fraud detection system [15]. Furthermore, AHR is presented in percentage formats. This characteristic is very suitable for the performance measurement among several different groups. Therefore, in our system evaluation, we calculate the Audit Hit Rate to measure the effectiveness of Zipf Analysis for distinguishing fraud data under different levels of the critical value. The formula of AHR is demonstrated below:

$$
\mathrm{AHR} = \left(\left(\sum Z _ {i}\right) / N\right) \times 100 \%\tag{11}
$$

where $\textstyle \sum Z _ { i }$ is the number of detected fraud records and N is the number of total records. Note that the higher value of Audit Hit Rate, the better performance of clustering.

According to the result of Zipf Analysis, the raw data have been clustered into two clusters: Normal cluster and Attack cluster. When the critical value was set under the level of 2%, we obtain the best Audit Hit Rate, 80.50% and 87.08%, in the normal and attack clusters respectively [38]. In both clusters, we can see that Zipf Analysis under three different levels of the critical value have better performance than 100% sampling, especially when the critical value under the level of 2%.

## 5.2. Bayes' Theorem and conditional probabilities

The performance of a fraud detection system could be determined by Bayes' Theorem, also named conditional probabilities [10]. The Bayes' Theorem, (we name it as Bayes Audit Hit Rate (BAHR) here), which is the probability that an event will occur, given that another event has already occurred. The probability that Event A will occur on the condition that Event B has already occurred, denoted P(A|B), can be determined using the following formula:

$$
P (F | S) = \frac {P (S | F) \times P (F)}{P (F) \times P (S | F) + P (\mathrm{NF}) \times P (S | \mathrm{NF})} = \frac {P (S | F) \times P (F)}{P (S)}\tag{12}
$$

$$
\begin{array}{l l} \text {Where:} & F \text {is fraud present;} \\ & \text {NF is no fraud present;} \\ & S \text {is the signal of fraud; and} \\ & P \text {is the probability.} \end{array}
$$

Thus, the usefulness of Zipf Analysis for fraud detection can be summarized as accurate fraud signals divided by total fraud signals Note that the higher value of Baves Audit Hit Rate, the better accuracy of BAHR. When the critical value was set under the level of 2%, we can obtain the best Bayes Audit Hit Rate, 50.56% and 96.45%, in the normal and attack clusters respectively [38]. Still, in both clusters, we can see that Zipf Analysis under three different levels of the critical value have better performance than 100% sampling, especially when the critical value under the level of 2%.

## 5.3. Confusion matrix

A confusion matrix contains information about actual and predicted classi<sup>fi</sup>cations done by a classi<sup>fi</sup>cation system. Performance of such systems is commonly evaluated using the data in the matrix. One bene<sup>fi</sup>t of a confusion matrix is that it is easy to see if the system is confusing two classes (i.e. commonly mislabeling one as an other). Therefore, we report our results using a confusion matrix, which is also used in the KDDCUP'99 contest. Each entry CM(x,y) is the number of predictions whose predicted class is y, but the actual class is x. In order to compare the performance on different classes, we attach a column of $\textstyle \cdot { \mathrm { A c c u r a c y } } = { \frac { \mathrm { C M } ( x _ { i } , y _ { i } ) } { \sum _ { i = 1 } ^ { 5 } { C M } \left( x _ { i } , y _ { j } \right) } } ,$ the accuracy (AC) is the proportion of the total number of predictions that were correct, and one row of false positive rate, $\begin{array} { r } { \mathrm { { { F P } \_ r a t e } } = \frac { \sum _ { i = 1 } ^ { 5 } C M \left( x _ { i } , y _ { j } \right) - C M \left( x _ { i } , y _ { j } \right) } { \sum _ { i = 1 } ^ { 5 } C M \left( x _ { i } , y _ { j } \right) } , } \end{array}$ the false positive rate (FP) is the proportion of negatives cases that were incorrectly classi<sup>fi</sup>ed as positive. Note that the higher accuracy, the better performance of prediction. However, the lower FP-rate implies lower misclassi<sup>fi</sup>cations.

Our simulations experimental results demonstrate that better performance by using Zipf Analysis as pre-process can be obtained. Because when the critical value was set under the level of 5%, we got a better average accuracy, 79.81546%. The rate of accuracy of class “Normal”, “Probe” and “R2L” is better than the benchmark rate. Moreover, the FP-rate of class “Normal”, “DOS” and “U2R” is better than the benchmark rate. On the other hand, we obtain better average accuracy, 99.3039%, when the critical value was set under the level of 2%. The better accuracy was obtained than benchmark in the class of “Normal”, “Probe”, “DOS” and “R2L”. The FP-rate of class “Normal”, “DOS” and “R2L” is better than the benchmark [38]. Note that the accuracy and FP-rate of U2R in the confusion matrix of CV=2% can not be calculated. The reason is that when we set the critical value equal to 2%, the preprocess, Zipf Analysis, <sup>fi</sup>lters all of the U2R connection records into the normal cluster.

## 5.4. Misclassification cost matrix

Most of the machine learning literature concentrates on model accuracy [29]. The KDDCUP'99 provides a considerably different matrix to evaluate the performance of learned models and they are evaluated and rated by a “cost matrix”. Cost-based matrices are more relevant in certain domains, and de<sup>fi</sup>ning such matrices poses signi<sup>fi</sup>cant and interesting research questions both in evaluating systems and alternative models, and in formalizing the problems to which one may wish to apply data mining technologies [29].

A misclassi<sup>fi</sup>cation cost matrix (See Table 8) is given to evaluate results of the KDDCUP'99 contest. Here, as in the misclassi<sup>fi</sup>cation cost matrix below, columns correspond to predicted categories, while rows correspond to actual categories. An entry at row x and column y, C(x,y) is the cost when an example of class x is classi<sup>fi</sup>ed to class y. For test example t, let $t _ { p }$ be the predicted class and $t _ { a }$ be the actual class, then the total misclassi<sup>fi</sup>cation cost, TMC on test dataset $T , T M C _ { T } \mathrm { i s } \ \Sigma _ { a = 1 , p = 1 } ^ { 5 , 5 } C ( t _ { a } , t _ { p } )$ and the average cost per test can be calculated by $\frac { \dot { \Sigma } _ { a = 1 , p = 1 } ^ { 5 , 5 } C \left( t _ { a } , t _ { p } \right) } { N }$ where N is the total test sample size.

Table 8 Cost matrix

<table><tr><td></td><td>Normal</td><td>Probe</td><td>DOS</td><td>U2R</td><td>R2L</td></tr><tr><td>Normal</td><td>0</td><td>1</td><td>2</td><td>2</td><td>2</td></tr><tr><td>Probe</td><td>1</td><td>0</td><td>2</td><td>2</td><td>2</td></tr><tr><td>DOS</td><td>2</td><td>1</td><td>0</td><td>2</td><td>2</td></tr><tr><td>U2R</td><td>3</td><td>2</td><td>2</td><td>0</td><td>2</td></tr><tr><td>R2L</td><td>4</td><td>2</td><td>2</td><td>2</td><td>0</td></tr></table>

Table 9 TMC and AMC

<table><tr><td></td><td>Sample size</td><td>TMC</td><td>AMC</td></tr><tr><td>Baseline</td><td>311,029</td><td>72,500</td><td>0.2331</td></tr><tr><td>Zipf CV=5%</td><td>4,898,430</td><td>281,653</td><td>0.0575</td></tr><tr><td>Analysis CV=2%</td><td>4,898,430</td><td>274,441</td><td>0.0560</td></tr></table>

Finally, we calculated the total and average misclassi<sup>fi</sup>cation cost using the new confusion matrix with the formula described above. The results are demonstrated in Table 9.

## 5.5. Discussion

In order to recognize the performance of Zipf Analysis in each cluster, we put AHR and BAHR together and graph these results into Figs. 6 and 7.

The <sup>fi</sup>ndings from our evaluations of AHR and BAHR are described below:

We <sup>fi</sup>nd that the performance of Zipf Analysis for anomalies <sup>fi</sup>ltering is indeed better than 100% sampling, especially when the critical value is under the level of 2%.

When the critical value is under the level of 2%, the interval testing and Z-statistic testing has the best performance for <sup>fi</sup>ltering connection records that have abnormal frequency patterns. In this case, we obtain the AHR of 87.08% and BAHR of 96.45%.

When the critical value is under the level of 5%, the interval testing and Z-statistic testing has the worst performance for <sup>fi</sup>ltering connection records that have abnormal frequency patterns. However, we still obtain better performance of AHR and BAHR than 100% sampling.

Following the above discussion, we can thus graph experiment results: the average cost of misclassi<sup>fi</sup>cation baseline and each simulation in Fig. 8. When we set CV=5% and CV=2%, we obtained the average cost per test equal to 0.057 and 0.056, respectively. One can see that both of our mechanisms obtained better performance than baseline.

Normal Cluster  
![](/api/attachments/8KXYBQ7E/fulltext/images/4b7be40839d5a429e5123e0d12595fe116310e6047c837e42446eeb63bc2e4d6.jpg)  
Fig. 6. AHR and BAHR of normal cluster.

![](/api/attachments/8KXYBQ7E/fulltext/images/30e5c9ec18549b3412eeedb0d274fa53a5ab9d5740d43f9ab37bef5023b14c44.jpg)  
Fig. 7. AHR and BAHR of attack cluster.

Our experiment results are conformed to Chu's declaration [7]: applying multiple algorithms for fraud detection can provide better performance than a single algorithm. In our case, we <sup>fi</sup>rst clustered the raw data into normal and attack clusters by Zipf Analysis. After this pre-process we obtained a new dataset, which contained more homogenous connection records. In second phase, we applied a classi<sup>fi</sup>cation algorithm, C5.0 Decision Tree, on the homogeneity dataset. Finally, we obtained a better predictive model for intrusion detection.

## 5.6. Case study

In order to verify the feasibility and effectiveness for a practical utilization, this study applied the proposed analysis mechanism in a real world case study. The case company X is one of high-tech enterprises in Taiwan. It currently has more than 200 employees. The company network service unexpectedly jammed and crashed about AM 8:30 in January 2nd, 2007, which is the morning of the <sup>fi</sup>rst working day after New Year holiday. The accident was initially determined to be due to outside attacks, since the network device still functioned in a good order. The company's MIS manager, who has a master degree in computer science and 5 years experience in audit and control, attempted to systematically identify and pinpoint the causes and consequently resolve problems caused by the attacks by analyzing system log <sup>fi</sup>les provided by networking devices. Fig. 9 shows the enterprise computer network architecture.

![](/api/attachments/8KXYBQ7E/fulltext/images/627e75f7c0b307105a6bd60f7fb657d519b8bc2046cec53783d1e8b81bffbe72.jpg)  
Fig. 8. Average misclassi<sup>fi</sup>cation cost.

![](/api/attachments/8KXYBQ7E/fulltext/images/8745d39e49248aeb7ecf0aed7dec8a7fc4de98e2ba81c1a81ffba92b411b6c5d.jpg)  
Fig. 9. Computer network architecture.

The MIS manager collected 7194 records from the <sup>fi</sup>rewall log <sup>fi</sup>le and 3895 records from the core switch log <sup>fi</sup>le, respectively. The records from the <sup>fi</sup>rewall log <sup>fi</sup>le were collected in the time period between 8:41 AM and 8:42 AM. There are three reasons why selecting the records from the <sup>fi</sup>rewall log <sup>fi</sup>le in that time period made sense. First, it was at the precise moment when the network jammed and the crash occurred. Secondly, the time of the attack fell within regular of<sup>fi</sup>ce hours, thus MIS manager was required to complete the duties of his job in dealing with the network problem. Finally, all systems and computers in the company had already freshened in that time at the <sup>fi</sup>rst working day after New Year holiday. The <sup>fi</sup>rewall log <sup>fi</sup>le was used to examine abnormal network access. After analyzing the abnormal network access, the 3895 records from the records from core switch log <sup>fi</sup>le were collected about 9:14 AM for detecting computers which were infected with virus in the abnormal network access. Table 10 is provided for comparing the <sup>fi</sup>rewall log <sup>fi</sup>le with the core switch log <sup>fi</sup>le.

## Table 10

The comparison between <sup>fi</sup>rewall and core switch log <sup>fi</sup>le

<table><tr><td></td><td>Firewall log file</td><td>Core switch log file</td></tr><tr><td>Purpose</td><td>To recognize the causes of unexpectedly jammed networks</td><td>To identify the attack sources</td></tr><tr><td>Order of usage</td><td>Preceding usage</td><td>Following usage</td></tr><tr><td>Time period</td><td>From 8:41 AM to 8:42 AM</td><td>From 9:14 AM to 10:25 AM</td></tr><tr><td>Number of records</td><td>7194</td><td>3895</td></tr></table>

<table><tr><td colspan="4">TCP port number 2967 is not a well known port number.</td></tr><tr><td>2007-01-02 08:41:55</td><td>Local4.Info</td><td>172.31.254.1</td><td>Jan 02 2007 08:41:55 172.31.254.1 : %PIX-6-302013: Built outbound TCP connection</td></tr><tr><td colspan="4">4506013 for outside:172.31.60.167/2967 (172.31.60.167/2967) to inside:172.31.5.58/4744 (139.223.23.125/3072)</td></tr><tr><td>2007-01-02 08:41:55</td><td>Local4.Info</td><td>172.31.254.1</td><td>Jan 02 2007 08:41:55 172.31.254.1 : %PIX-6-305011: Built dynamic TCP translation</td></tr><tr><td colspan="4">from inside:172.31.8.175/1547 to outside:139.223.23.125/3073</td></tr><tr><td>2007-01-02 08:41:55</td><td>Local4.Info</td><td>172.31.254.1</td><td>Jan 02 2007 08:41:55 172.31.254.1 : %PIX-6-302013: Built outbound TCP connection</td></tr><tr><td colspan="4">450604 for outside:172.31.242.66/2967 (172.31.242.66/2967) to inside:172.31.8.175/1547 (139.223.23.125/3073)</td></tr><tr><td>2007-01-02 08:41:55</td><td>Local4.Info</td><td>172.31.254.1</td><td>Jan 02 2007 08:41:55 172.31.254.1 : %PIX-6-305011: Built dynamic TCP translation</td></tr><tr><td colspan="4">from inside:122.31.5.58/4745 to outside:139.223.23.125/3074</td></tr></table>

TCP port number 2967 is not a well known port number.  
Fig. 10. The part of <sup>fi</sup>rewall log <sup>fi</sup>le.

<table><tr><td>2007-01-02 09:14:39</td><td>Local7.Info</td><td>172.31.2.1</td><td>543261: 11w3d: %SEC-6-IPACCESSLOGP: list 190 denied tcp 172.31.4.74(1386) -&gt;</td></tr><tr><td colspan="4">172.31.153.76(2967), 1 packet</td></tr><tr><td>2007-01-02 09:14:40</td><td>Local7.Info</td><td>172.31.2.1</td><td>543262: 11w3d: %SEC-6-IPACCESSLOGP: list 190 permitted tcp 172.31.2.111(4298) -&gt;</td></tr><tr><td colspan="4">210.161.32.232(80), 1 packet</td></tr><tr><td>2007-01-02 09:14:40</td><td>Local7.info</td><td>172.31.2.1</td><td>543263: 11w3d: %SEC-6-IPACCESSLOGP: list 190 denied tcp 172.31.9.104(4268) -&gt;</td></tr><tr><td colspan="4">172.31.35.117(2967), 1 packet</td></tr><tr><td>2007-01-02 09:14:42</td><td>Local7.info</td><td>172.31.2.1</td><td>543264: 11w3d: %SEC-6-IPACCESSLOGP: list 190 permitted tcp 172.31.5.47(2401) -&gt;</td></tr><tr><td colspan="4">207.46.111.10(1063), 1 packet</td></tr></table>

Fig. 11. The suspect segment of core switch log <sup>fi</sup>le.

In this case study, the case company's existing network fraud detection method and the proposed method were compared and contrasted. Further, these aforementioned two experiments used the same dataset.

5.6.1. Experiment 1: The existing network fraud detection method. Since no tools and methods were available to be utilized to help the manager identify the problem, he can only analyze the problem manually by performing the following steps in sequence.

5.6.1.1. Step 1: Analysis of TCP communications in log files provided by network devices. The TCP log <sup>fi</sup>les available after network abnormally crashed are utilized as an input for a detailed analysis. After spending 3 hours analyzing the data, the MIS manager <sup>fi</sup>nally found that the log <sup>fi</sup>le contains a number of records associated with “TCP connection port number 80”, “TCP connection port number 2967”, and “TCP connection port number 3921”. Fig.10 illustrates the part of <sup>fi</sup>rewall log <sup>fi</sup>le, which displays some inside IP connected outside by using TCP connection port number 2967. As per the experience of the manager, there is apparently no applications use TCP port number 2967 as an outside port in the company based on past experience. This manager, therefore, suspected that TCP port numbers 2967 and 3921 actually caused the problem.

5.6.1.2. Step 2: Action performed on network device to resolve the potential attacks. After determining abnormal communication by collecting and analyzing log data, the manager decided to block 2967 and 3921 TCP port communications to conduct the testing.

5.6.1.3. Step 3: Verification of the effectiveness of the problem resolution strategy. Applying an alternative to block port 3921 on the <sup>fi</sup>rewall devices, the network loading remained the same. Further, by applying a second alternative to block port 2967 on the firewall devices, the average load of network devices was relieved from 80% to 15%. After several rounds of testing, the network jam was properly resolved by the newlyadded networking policy.

5.6.1.4. Step 4: Further identification of attack sources in the company. With the network jam resolved, the managers attempted to identify the sources of network attacks in the company. Core switch Log <sup>fi</sup>les related to each computer are further classi<sup>fi</sup>ed and individually analyzed. Analyzing communications of individual computers, 18 computers in total are identi<sup>fi</sup>ed as possible sources of the network attacks. The suspected part of core switch log <sup>fi</sup>le is shown as Fig. 11. There two computers with 172.31.4.74 and 172.31.9.104 were included in sources of the network attacks. These computers were deemed to be virus infected ones using the new version of computer virus scanning software. The entire intranet was recovered after the virus was cleaned.

5.6.2. Experiment 2: The proposed mechanism. The MIS manager and 3 IT staff members with college degree in computer science spent a whole working day using the above method. The case company has more than 200 employees as the foregoing. The full salaries of all employees for each working day are around NTD

![](/api/attachments/8KXYBQ7E/fulltext/images/3704b6c309cc66b8b591e797bcf58097046abeb35eb504eda42a28c8ec630ff2.jpg)  
Fig. 12. Fraud detection for Top 50 patterns.

Table 11  
Experiment results

<table><tr><td></td><td>Estimate fraud</td><td>Real fraud</td><td>Audit Hit Rate</td></tr><tr><td>TOP 30</td><td>13</td><td>7</td><td>7/13</td></tr><tr><td>TOP 50</td><td>16</td><td>7</td><td>7/16</td></tr><tr><td>TOP 100</td><td>20</td><td>8</td><td>8/20</td></tr></table>

1,000,000. If the company network service is disabled, the productionwill be reduced about 40% per day. Thus, the jammed networks resulted in almost NTD 400,000 in direct loss. Furthermore, it also caused more serious indirect loss, such as disabled the ability of order acceptance, impacted customer satisfaction, and damaged the company's brand name and goodwill. In addition, due to the fact that repairing jammed networks takes too much time, the MIS manager had to answer at least 100 calls regarding customer complaints.

The same <sup>fi</sup>rewall log <sup>fi</sup>le was employed by utilizing our proposed mechanism. The port\_number and IP\_address attributes were selected to generate the patterns for this case study. The reason to select these two attributes is that they are basic attributes available for all network transactions. Consequently, the <sup>fi</sup>rewall log contains 2417 different IP and 1811 different inside ports. There are 4599 patterns in total.

Since the majority of the patterns only appear once in our log <sup>fi</sup>le, we had to randomly select the top 30, 50, and 100 patterns to process the Zipf analysis. Fig. 12 was provided to show the analysis result for top 50 patterns.

Furthermore, Table 11 was summarized to show the result of the Experiment 2. Using our proposed approach, the potential abnormal patterns, such as potential fraud or attacks can be easily identi<sup>fi</sup>ed since this proposed mechanism can be utilized effectively to determine data distribution patterns in both normal and abnormal cases.

Relative to the manual analysis for fraud detection in the Experiment 1, several noteworthy occurrences which justify grounds for using our proposed approach in the Experiment 2 are interpreted as the following. First, the ef<sup>fi</sup>ciency for detecting fraud of our proposed approach is substantially more ef<sup>fi</sup>cient than the manual analysis. Secondly, the cost of fraud detection by using the proposed approach is also lower than the manual analysis. Furthermore, any fraud which has not been detected can result in a great deal of damage. Finally, the proposed approach is the right technique to assist auditors in inspecting the tremendous and complicated datasets and detecting any potential fraud ef<sup>fi</sup>caciously. The eventual decision and policy are still made by auditors based on their knowledge and experience. Via our proposed approach, the auditors therefore can promptly make more correct decision and policy in a short time.

## 6. Conclusions

The principal objectives of this research are to introduce an innovative fraud detection mechanism on the basis of Zipf's Law. The main purpose of this technique is to assist auditors for reviewing the overwhelming volumes of datasets and transactions and identifying any potential fraud records. We conducted a simulation experiment and a real case study to verify the performance of our mechanism. In order to evaluate our simulations, we used four key performance indicators: the Audit Hit Rate, Bayes Audit Hit Rate, the confusion matrix and misclassi<sup>fi</sup>cation cost matrix. Finally, our simulation experimental results demonstrate that Zipf Analysis can assist auditors in distinguishing normal versus abnormal data occurrences, helping to decrease suspicion. The achieved objectives are described as follows:

1) Zipf Analysis is very suitable for identifying the potential fraud records that have frequent sequential patterns. The <sup>fi</sup>rst-two evaluations demonstrate that Zipf's Law could <sup>fi</sup>lter the most of fraud records, especially for frauds that have frequent sequential patterns. The results show that when the critical value under the level of 2% Zipf Analysis has the best performance, AHR=87.06% and BAHR=96.45%.

2) Zipf Analysis is more effective and ef<sup>fi</sup>cient than 100% sampling. Our experiment shows that Zipf's Law could generate higher AHR and BAHR. Therefore, it implies that our mechanism for fraud detection can facilitate the performance of auditor's reviewing of vastly increased volumes of data and transactions.

As to the possibility of future research on this subject matter, there are several directions that the reader can take.

1) This research conducted a simulation experiment only for the purpose of testing the ability of Zipf's Law to detect fraud. In the future, one can further evaluate the fraud detection performance of Zipf's Law by comparing Zipf Analysis with other clustering algorithms, some examples being K-means, Kohonen, Digital Analysis and so on.

2) One can apply our mechanism into real case studies to examine the feasibility and effectiveness of Zipf Analysis, even in different domain's datasets, such as time-varying data, multi-dimensional data and data from multiple sources.

3) Similarly, one could apply our mechanism on these datasets that consider time-serial attributions to verify the capacity of Zipf Analysis for detecting time-serial fraud patterns.

## Acknowledgments

The work presented in this paper has been supported by The National Science Council, Taiwan, R.O.C, under Grant No. 96-2416-H-194-007-MY3. The authors of this research appreciate deeply their <sup>fi</sup>nancial support and encouragement. In addition, the authors also wish to thank Dr. Shing-Han Li for giving advice and supporting the case study.

## References

[1] C. Aasheim, G.J. Koehler, Scanning world wide web documents with the vector space model, Decision Support Systems 42 (2) (2006).

[2] L.A. Adamic, B.A. Huberman, Zipf's law and the Internet, Journal of Glottometrics 3 (2002).

[3] Association of Certi<sup>fi</sup>ed Fraud Examiners, Report to the Nation 2004, 2004 http://www.acfe.com/fraud/report.asp

[4] F. Benford, The law of anomalous numbers, Proceedings of the American Philosophical Society 78 (4) (1938)

[5] R.J. Bolton, D.J. Hand, Statistical fraud detection: a review, Journal of Statistic 17 (3) (2002).

[6] M. Carlos, A simple and ef<sup>fi</sup>cient test for Zipf's law, Journal of Economics Letters 66 (3) (2000)

[7] M. Chu, A research of using digital rules and data mining to build an investigation model of the audit selecting case, Master student Dissertation (National Chung Cheng University Taiwan. 2005).

[8] D. Coderre, Fraud Detection: Using Data Analysis Techniques to Detect Fraud GAP Publication, 1999

[9] V. Dobrynin, D. Patterson, M. Galushka, N. Rooney, SOPHIA: an interactive cluster-based retrieval system for the OHSUMED collection IEEE Transactions on Information Technology in Biomedicine 9 (2) (2005).

[10] C. Durtschi, W. Hillison, C. Pacini, The effective use of Benford's law to assist in detecting fraud in accounting data, Journal of Forensic Accounting 5 (1) (2004).

[11] Ernst Young, Fraud: The Unmanaged Risk — 8th Global Survey, 2003 http://www.ey.com/global/content.nsf/International/Home.

[12] H.M. Gao, How analytical procedures, internal control and regression analysis affect the auditors' judgments, Master student Dissertation (National Chengchi University, Taiwan, 1989).

[13] V. Gudivada, V. Raghavan, W. Grosky, R. Kasanagottu, Information retrieval on the World Wide Web, IEEE Internet Computing 1 (5) (1997).

[14] T.P. Hill, A statistical derivation of the signi<sup>fi</sup>cant digit law, Journal of Statistical Science 10 (4) (1996).

[15] Y.R. Ju, A research by using digital analysis and data mining as an auditing analytical procedure, Master student Dissertation (National Chung Cheng University, Taiwan, 2004).

[16] KPMG, Fraud Survey of 2003, 2003 http://www.kpmg.com/.

[17] S.H. Li, S.M. Huang, Y.C. Lin, Developing a continuous auditing assistance system based on information process models, Journal of Computer Information Systems 48 (1) (2007)

[18] M.J. Nigrini, Digital analysis and the reduction of auditor litigation risk, Proceedings of the 1996 Deloitte & Touche/University of Kansas Symposium on Auditing Problems, 1996.

[19] M.J. Nigrini, L.J. Mittermaier, The use of Benford's Law as an aid in analytical procedures, Auditing: A Journal of Practice and Theory 16 (2) (1997).

[20] B. Pfahringer, Winning the KDD99 classi<sup>fi</sup>cation cup: bagged boosting Journal of SIGKDD Explorations 1 (2) (2000).

[21] L. Pietronero, E. Tosatti, V. Tosatti, A. Vespignani, Explaining the uneven distribution of numbers in nature: the laws of Benford and Zipf, Journal of Physica A 293 (1–2) (2004).

[22] D.M.W. Powers, Applications and explanations of Zipf's law, Proceedings of New Methods in Language Processing and Computational Natural Language Learning, 1998.

[23] M. Ramanathan, V. Kalogeraki, J. Pruyne, Finding good peers in peer-topeer networks, Proceeding of the 16th IEEE International Parallel and Distributed Processing Symposium. 2002.

[24] F.C. Ramon, R.V. Sole, Zipf's law and random texts, Journal of Advances in Complex Systems 5 (1) (2002).

[25] R. Reed, D. Pence, Detecting fraud in <sup>fi</sup>nancial statements: the use of digital analysis as an analytical review procedure, Journal of Forensic Accounting 6 (1) (2005).

[26] R.Y. Ricardo, R.N. Berthier, Modern Information Retrieval, Addison-Wesley Press, 1999.

[27] C.J. Robert, M.H. Olson, R. Hauser, Field Experimentation of MIS research, Harvard Business School Research Colloquium, 1989 Part III, Ch. 8.

[28] C.J. van Rijsbergen, Information Retrieval, Butterworth's Publication,1979.

[29] S.J. Salvatore, W. Fan, W. Lee, A. Prodromidis, P. Chan, Cost-based modeling for fraud and intrusion detection: results from the JAM Project, Proceedings of DARPA Information Survivability Conference and Exposition 2 (2000).

[30] C. Silvio, Using digital analysis to detect fraud, Proceedings of 10th Annual ACFE Canadian Fraud Conference, 2004.

[31] H. Situngkir, Y. Surya, What can we see from investment simulation based on generalized (m, 2)-Zipf law? Bandung Fe Institute Working Paper No.WPE2005, Social Science Research Network, 2005.

[32] C. Skousen, L. Guan, S. Wetzel, Anomalies and unusual patterns in reported earnings: Japanese managers round earnings, Journal of International Financial Management and Accounting 15 (3) (2004).

[33] L. Sokol, B. Garcia, M. West, J. Rodriguez, K. Johnson, Precursory steps to mining HCFA health care claims, Proceedings of the 34th Hawaii International Conference on System Sciences, 2001.

[34] Statements on Auditing Standards: SAS 410 Analytical procedures, 2005 http://www.hkicpa.org.hk/ebook/HKSA\_Members\_Handbook\_Master/ volumeIII/sas410.pdf.

[35] C. Tang, Z. Xu and M. Mahalingam, PeerSearch: ef<sup>fi</sup>cient information retrieval in peer-to-peer networks, Technical Report HPL-2002-198, Internet Systems and Storage Laboratory, HP Laboratories (2002).

[36] J.K. Thomas, Unusual patterns in reported earning, Journal of The Accounting Review 64 (4) (1989).

[37] D. Wang, M. Li, Z. Di, True reasons for Zipf's law in language, Journal of Physics A 358 (2–4) (2005).

[38] L.W. Yang, An investigation of Zipf's Law for fraud detection, Master student Dissertation (National Chung Cheng University Taiwan 2006)

[39] G.K. Zipf, Human Behavior and the Principle of Least Effort: An Introduction to Human ecology, Hafner Publication, 1949.

![](/api/attachments/8KXYBQ7E/fulltext/images/e3347d51804f57731485311ea04141d06939c5e64986b911dc1e086dee6baaa3.jpg)

Dr. Shi-Ming Huang received his PhD degree at the School of Computing and Information Systems, University of Sunderland, UK. He is currently a Head of Accounting and Information Technology Department and a Director for the Research Center of e-Manufacturing and e-Commerce at National Chung Cheng University, Taiwan. He is 2006 President for International Chinese Information Systems Association (ICISA). He has published five books. three business software and over 50 articles in refereed information system journals, such as Information and Management, Decision

Support Systems, Journal of Computer Information Systems, European Journal of Operational Research, Journal of Database Management, ACM SIGMOD, etc. He has received over 10 achievement awards in information system area.

![](/api/attachments/8KXYBQ7E/fulltext/images/f507b31b6761c65fd01c0a0ecf04c8234508944cfeabc8ad180366f716b91fd6.jpg)

David C. Yen is currently Jennifer J. Petters Chair in Asian Business and Professor of MIS of the Department of Decision Sciences and Management Information Systems at Miami University He assumed Raymond E. Glos Professor in Business from 2005–2007 and was a department chair from 1995–2005. He has published books and articles which have appeared in Communications of the ACM, Decision Support Systems, Information & Management, Information Sciences, Computer Standards and Interfaces, Information Society, Omega, International Journal of Organiza-

tional Computing and Electronic Commerce, and Communications of AIS among others.

Luen-Wei Yang received his master's degree from the National Chung Cheng University, Taiwan, 2006. Currently, he has served as a consultant of Jacksoft Commerce Automated LTD since 2007 His research interests are in computer auditing, data mining, and information security.

![](/api/attachments/8KXYBQ7E/fulltext/images/9ebb1ad37b99438bc4a2bd94fd386675d0d5c5a408e46cc9f300b05dd237029a.jpg)

![](/api/attachments/8KXYBQ7E/fulltext/images/bb6cdb6e936cac2d852bd4c7eee0e9eaefbd2f65a76c5355cf89f2a60b22f2cb.jpg)

Jing-Shiuan Hua is currently a PhD student in the Department of Information Management, National Chung Cheng University, Taiwan. Her current research interests include software engineering, project management and information security management.
