---
otero_id: 2872
otero_key: "5K28UJES"
title: "Using data mining techniques to predict hospitalization of hemodialysis patients"
authors: "Jinn-Yi Yeh; Tai-Hsi Wu; Chuan-Wei Tsao"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.11.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using data mining techniques to predict hospitalization of hemodialysis patients

Jinn-Yi Yeh <sup>a,</sup>⁎, Tai-Hsi Wu <sup>b</sup>, Chuan-Wei Tsao <sup>a</sup>

<sup>a</sup> Department of Management Information Systems, National Chiayi University, Taiwan

<sup>b</sup> Department of Business Administration, National Taipei University, Taiwan

## a r t i c l e i n f o

Article history: Received 20 February 2009 Received in revised form 22 October 2010 Accepted 1 November 2010 Available online 6 November 2010

Keywords: Hemodialysis Temporal abstract Data mining Healthcare quality

## a b s t r a c t

Hemodialysis patients might suffer from unhealthy care behaviors or long-term dialysis treatments and need to be hospitalized. If the hospitalization rate of a hemodialysis center is high, its service quality will be low. Therefore, decreasing hospitalization rate is a crucial problem for health care centers. This study combines temporal abstraction with data mining techniques for analyzing dialysis patients' biochemical data to develop a decision support system. The mined temporal patterns are helpful for clinicians to predict hospitalization of hemodialysis patients and to suggest immediate treatments to avoid hospitalization.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

End stage renal disease (ESRD), commonly known as uremia, is a severe chronic state corresponding to the <sup>fi</sup>nal stage of kidney failure. In ESRD, kidneys are not able to purify blood from metabolites or to exclude water from the body. Without medical intervention, ESRD patients may die or remain in intensive care unit (ICU) for a long time. These patients require either a kidney transplant or blood-<sup>fi</sup>ltering dialysis treatment. The former treatment is dif<sup>fi</sup>cult to obtain because of a long waiting list and certain patients, such as the elderly, cannot undergo a transplant. The latter includes two main categories, hemodialysis (HD) and peritoneal dialysis (PD). In HD, the blood passes through an extra-corporal circuit where metabolites (e.g. urea) are eliminated. The acid-based equilibrium is re-established and excess water is removed [3]. PD works on the same principles of solute diffusion and <sup>fl</sup>uid ultra <sup>fi</sup>ltration as HD, but the blood is cleaned inside the body rather than through a machine [16]. More than 80% of ESRD patients are currently treated with HD [3]. HD patients typically undergo a dialysis session for 4 h, three times a week. During the longterm dialysis treatment, patients will likely receive hospitalization due to caregiver carelessness or other infections. This has been the main reason for HD patient hospitalization in previous years.

High hospitalization rate for a hospital hemodialysis department (HHD) means low service quality in health care. Therefore, the HHD focuses on reducing hospitalization rate. Preventing hospitalization of HD patients from the perspective of preventive medicine is also very important. This paper develops a decision support system to predict hospitalization of HD patients based on a real dataset collected from a hemodialysis center in Taiwan. The HHD examines HD patients receiving long-term treatment to obtain biochemical data during hemodiaysis sessions, such as hematocrit (Hct), albumin, alkaline-p, cholesterol, triglyceride, blood urea nitrogen (BUN), creatinine, uric acid, Na, etc. [25]. The accumulated data over time contains a set of patient variables that are monitored during each dialysis session. The collected data are sequences of multidimensional time series [3].

For time series data, the temporal abstraction (TA) method proposed by Shahar [22] can be integrated with data mining techniques to support data analysis. For example, Bellazzi et al. [3] successfully applied temporal data mining techniques for assessing the clinical performance of HD services such as preprocessing, data reduction, multi-scale <sup>fi</sup>ltering, association rule discovery, etc. They found their approach to be suitable for knowledge discovery in clinical time series. Using an auditing system context for dialysis management helped clinicians improve their understanding of patients' behavior. Adlassnig et al. [1] proposed and discussed promising research directions in the <sup>fi</sup>eld of TA and temporal reasoning in medicine. They identi<sup>fi</sup>ed and focused on fuzzy logic, temporal reasoning and data mining, health information systems, and temporal clinical databases and recommended developing decision support systems to properly manage the multifaceted temporal aspects of information and knowledge encountered by physicians in their clinical work. Stacey and McGregor [23] surveyed previous research in developing intelligent clinical data analysis systems that incorporate TA mechanisms and present research trends. They suggested the necessity of fusing data mining and TA processes to fully exploit new knowledge from stored clinical data through data mining and apply it to data abstraction.

For TA rule mining, Sacchi et al. [21] proposed a new kind of TA rule and related algorithms for the extraction of temporal relationships between complex patterns de<sup>fi</sup>ned over time series. Their approaches could be used in a variety of application domains, and they were already tested on two different biomedical problems. Concaro et al. [5] developed a general methodology for the mining of TA rules on sequences of hybrid events for Diabetes Mellitus. The method was capable to characterize subgroups of subjects, highlighting interesting frequent temporal associations between diagnostic or therapeutic patterns and patterns related to the patients' clinical condition. They concluded that the approach could <sup>fi</sup>nd a practice for the evaluation of the pertinence of the care delivery <sup>fl</sup>ow for speci<sup>fi</sup>c pathologies.

Based on the literature review, this study integrates TA with data mining techniques for analyzing biochemical data of HD patients to discover temporal patterns resulting in hospitalization. This work develops a decision support system to provide clinicians with association rules and the probability of HD patients' hospitalization for implementing preventive medicine to decrease hospitalization incidence. This system will hopefully help to understand patients' changing biomedical data that leads to hospitalization and to improve service quality of the hemodialysis center. The remainder of this paper is arranged as follows: The Materials and methods Section describes hemodialysis and temporal abstraction, the Development of decision support system Section demonstrates the development of the decision support system used in this paper, the Computational results Section illustrates the experimental results using the combined approach for hemodialysis patients' data analysis, and the last section give the conclusions.

## 2. Materials and methods

## 2.1. Hemodialysis

HD for ESRD patients is typically performed in a clinic setting. The diffusion process exchanges solutes and metabolites across a semipermeable membrane, separating the blood and dialysate. Water is removed from the body using a negative pressure gradient in a process called ultra-<sup>fi</sup>ltration. After transit through the dialyzer, the clean, <sup>fi</sup>ltered blood is returned to the body. Typically, HD is performed three times a week for about four hours each session. The cost of providing care for HD patients is high. Finding ways to improve patient outcomes and reduce dialysis cost is important. Kusiak et al. [16] demonstrated that data mining, data transformation, data partitioning, and decision-making algorithms are useful for predicting dialysis patient survival. They applied a rough set theory and decision-tree algorithms to analyze biochemical data of HD patients. Sixteen classi<sup>fi</sup>ers were produced by these two methods to make predictions. A simple voting scheme was used, with each classi<sup>fi</sup>er having one vote. The decision outcome with the maximum number of votes resulted in the predicted outcome. These rules were used to predict the survival of new unseen patients. The results provide a base for analyzing HD patients' data in Taiwan.

The required HD service for ESRD patients has dramatically increased each year in Taiwan. Due to the special characteristics of these patients, both hospitalization times and hospitalization costs are higher than for other patients. Preventive medicine could decrease these costs by analyzing HD lab data to <sup>fi</sup>nd possible factors. The Bureau of National Health Insurance in Taiwan has also put forward a professional health care quality index according to various overall quality schemes for long-term monitoring. The main items for assessing hemodialysis center quality include: hospitalization rate, serum albumin, clearance rate of urea nitrogen (Kt/V), hematocrit, death rate, sinus reconstruction rate, and weaning rate. Hong [11] used multiple minimum support association rules to discover hospitalization cause and effect factors by analyzing HD lab data.

His approach increased the accuracy of health care results and shortened the analyzing period. However, he did not consider time series data recorded during HD sessions.

## 2.2. Temporal abstraction

Temporal abstraction (TA) is an arti<sup>fi</sup>cial intelligence technique, which integrates domain knowledge into the data analysis process. TA outlines the evolutionary process of temporal data through a qualitative presentation mode, such as level shifts, periods of stability and trends. Shahar [22] de<sup>fi</sup>ned TA as a program given a set of time series data including variables, external events, and abstract. The generated abstract description represents previous and current states and data trends. The TA program converts patients' data from a lowlevel quantitative format to a high-level qualitative description. This presentation format is close to the clinician's specialty vocabulary [23]. Clinicians and domain experts typically work together to discuss rules and knowledge based on TA. These rules and knowledge are very important for generating signi<sup>fi</sup>cant and data-dependent TA and to determine whether these abstractions can be explained correctly to work out correct diagnoses.

Generally, TA can be obtained from both basic TA and complex TA, described respectively as follows. Basic TA is typically indicated by combining state and trend from time series data of existing episodes. The state can be classi<sup>fi</sup>ed as low, normal, and high values. The trend can be classi<sup>fi</sup>ed as increased, decreased, and stable patterns [22]. An episode refers to the data in a time interval [3]. Complex TA describes the temporal relation between basic TAs and complex TAs. Typical complex TAs typically use the temporal operator proposed by [2] to concatenate basic TA (see Fig. 1). The most used operator is Meet, referring to the successively presented precedence order between basic TAs [23]. For example, if a rule states that two basic TAs, A-high and B-high, correspond to result C, and A occurs earlier than B, it can be indicated by A-high Meet B-high Then C.

Initially, TA is applied to data monitoring of patients in intensive care units (ICU) based on the intelligent data analysis (IDA) system which detects abnormal phenomena of patients' temporal data. This provides clinicians with relevant temporal information of patients for subsequent treatments [17]. Fig. 2 shows the IDA system schema, containing several different missions: data validation, data representation, data interpretation, and control tasks. TA is applicable to data representation and the interpretation phase. When TA is applied to the data analysis system during the reasoning process, interpretation or reasoning can be carried out by comparing prede<sup>fi</sup>ned patterns de<sup>fi</sup>ned by clinicians or derived from machine learning techniques. Finally, the control tasks present proper treatments according to abnormal phenomena of the data.

<table><tr><td>Relation</td><td>Examples</td></tr><tr><td rowspan="4">A operator(PRECEDE) B</td><td>Overlap :aaaaabbbbb</td></tr><tr><td>Meet:aaaaabbbbb</td></tr><tr><td>Before :aaaaabbbbb</td></tr><tr><td>Equal :aaaaabbbbb</td></tr></table>

Fig. 1. Temporal operator [3].

![](/api/attachments/5K28UJES/fulltext/images/90c5acc54d10914582b600ce304cbb8f83b92667d909e97680439928f0b82feb.jpg)  
Fig. 2. Typical intelligent data analysis system schema [23]

TA application is also related to medical data analysis, and often integrated with data mining techniques and arti<sup>fi</sup>cial intelligence approaches. In the study of [3], blood pressure and ferroheme of hemodialysis patients were derived from dialyzers in three weekly treatments. They were processed by discrete wavelet transformation and association rules mining to obtain insuf<sup>fi</sup>cient factors of hemodialysis service quality. The mined rules provided a reference for clinicians. The results show that an auditing system context for dialysis management helped clinicians improve their understanding of patients' behavior. Differing from [3], the hepatitis data used in [10] was collected at irregular intervals, therefore the TA time intervals were not the same. The study also used a “state change” temporal operator to describe temporal abstraction, and formula counting signi<sup>fi</sup>cance to prune the rules. The experimental results show that the generating hepatitis temporal pattern improved effectively.

## 2.3. Decision tree

A decision tree (DT) is a <sup>fl</sup>ow-chart-like tree structure, where each internal node denotes a test on an attribute, each branch represents an outcome of the test, and each leaf node represents hospitalization or non-hospitalization. The top-most node in a tree is the root node. The test on an attribute is associated with a splitting criterion chosen to split the data sets into subsets with better class separability, thus minimizing misclassi<sup>fi</sup>cation error. Once the tree is built from the training data, it is then heuristically pruned to avoid over-<sup>fi</sup>tting of data, which tends to introduce classi<sup>fi</sup>cation error on the test data [9,14].

![](/api/attachments/5K28UJES/fulltext/images/c83d9d13cd4523ca50b01cccfe6ff45ddb3e24514f4ac8dcecb2a92aa31d8349.jpg)  
Fig. 3. Flow of hemodialysis patients' data analysis

For DT pruning, C4.5 follows the postpruning approach which removes branches from a fully grown tree. For each nonleaf node in the tree, the pruning algorithm estimates the expected error rate that would occur if the subtree at that node were pruned. Then the expected error rate occurring if the node were not pruned is estimated using the error rates for each branch, combined by weighting according to the proportion of observations along each branch. If pruning the node leads to a greater expected error rate, then the subtree is kept. Otherwise, it is pruned [9].

## 2.4. Mining association rules with multiple minimum supports

Mining association rules with multiple minimum supports is an important generalization of the association-rule-mining problem, recently proposed by [19]. Instead of setting a single minimum support threshold for all items, users are allowed to specify multiple minimum supports to re<sup>fl</sup>ect the nature of items, and an Apriori-based algorithm is developed to mine all frequent item sets. Thus, different rules may need to satisfy different minimum supports depending on what items are in the rules. This new model enables users to produce rare item rules without causing frequent items to generate too many meaningless rules [12].

## 3. Development of decision support system

The schema system of this study was mainly developed from IDA, shown in Fig. 3. In the knowledge creation phase, patient's time series biochemical data is validated by knowledge engineers and relevant clinicians to remove outliers and to handle missing data. The preprocessed data is changed to a TA format based on TA rules speci<sup>fi</sup>ed by the domain expert. This process integrates the knowledge of specialized <sup>fi</sup>elds into the analysis program. The transformed TA data is afterwards fetched into the data mining program to <sup>fi</sup>nd out rules for predicting hemodialysis patients' hospitalization. The mined patterns are provided to clinicians for further processing, including rules evaluation and irrational rules deletion. The remaining rules are stored in a database, to provide a decision support system for clinicians to practically judge whether patients will need hospitalization or not.

## 3.1. Data collection

This study was conducted in a large nationwide hemodialysis center in Taiwan. A total of 8223 chronic hemodialysis patients (samples) who received regular hemodialysis for more than six consecutive months comprised the analysis subject. Data collection was based on known and unknown biochemical testing items (parameters) of effective dialysis treatment. The data mining view considers that every biochemical testing item represents a feature. Due to different biochemical testing items having their own clinical signi<sup>fi</sup>cance, we needed to discuss with a clinician to sort out the applications of various biochemical testing items. The clinical signi<sup>fi</sup>cance of some biochemical testing items in the data also appears frequently. After making enquiry, we selected the feature and avoided redundant features in<sup>fl</sup>uencing mining accuracy and effectiveness. For example, protein and albumin represent patients' nutritional status. Clinicians suggest selecting any of them as the feature.

Features used in this study were collected from 2005–2007 quarterly reports including gender, age, hospitalization, admission date, and monthly routine biochemical test items, such as White Blood Cell (WBC), Red Blood Cell (RBC), Hemoglobin (HBC), Hematocrit

![](/api/attachments/5K28UJES/fulltext/images/6e7126df69cf668145d386f6fdf23396437867ec4494c930463ad7988e3deedc.jpg)  
Fig. 4. Data preprocessing <sup>fl</sup>ow chart.

![](/api/attachments/5K28UJES/fulltext/images/4cb12377be64e10a8c6f4a24f8a469de45e340bb1c16390c5df1f194c15dfbd4.jpg)  
Fig. 5. Temporal abstraction <sup>fl</sup>ow.

(HCT), Mean Corpuscular Volume (MCV), Platelet, Albumin, Alanine aminotransferase (GPT), Alkaline Phosphatase (Alkaline-P), Cholesterol, Triglyceride, Glucose (AC), Creatinine, Uric Acid, Sodium (Na), Potassium (K), Calcium (Ca), Phosphorus (P), Urea Reduction Rate (URR), kt/v, Serum iron (Fe), Ferritin, and Ca×P where URR was calculated from the difference in blood urea concentration before and after dialysis divided by pre-dialysis blood urea concentration. The KT/V (Daugirdes) was calculated using the URR and adjusted for <sup>fl</sup>uid shifts that occur during dialysis. The product of calcium and phosphorous (Ca × P) has special meaning. If serum inorganic phosphorus is greater than 5.5 and Ca×P is greater than 55, death rate increases accordingly (calci<sup>fi</sup>cation of main coronary artery and cardiac muscle result in coronary heart disease and heart failure). Therefore the value of Ca×P needs additional calculations added to the system.

## 3.2. Data preprocessing

Due to heterogeneity and specialty problems of medical data, we analyzed the biochemical tests of original HD patients during the preprocessing phase. We also found it necessary to cooperate with clinicians in this step to <sup>fi</sup>nd out outliers and missing values. The process is shown in Fig. 4.

Table 1  
Threshold values of biochemical test items for TA transformation.

<table><tr><td>No.</td><td>Item</td><td>Normal value Unit</td><td>XH</td><td>H</td><td>N/H</td><td>N/L</td><td>L</td><td>XL</td></tr><tr><td>1</td><td>WBC</td><td>5-10×1000/ul</td><td>30</td><td>15</td><td>10</td><td>3</td><td>2</td><td>1</td></tr><tr><td>2</td><td>RBC</td><td>&gt;2.5×10^6/ul</td><td>6×.5</td><td>6</td><td>5.4</td><td>3.8</td><td>3</td><td>2.5</td></tr><tr><td>3</td><td>HBC</td><td>12.3-18.3 g/dl</td><td>20</td><td>18</td><td>15</td><td>9</td><td>8</td><td>6</td></tr><tr><td>4</td><td>HCT</td><td>39-53%</td><td>50</td><td>45</td><td>40</td><td>28</td><td>25</td><td>20</td></tr><tr><td>5</td><td>MCV</td><td>80-100 fl</td><td>110</td><td>100</td><td>95</td><td>80</td><td>70</td><td>60</td></tr><tr><td>6</td><td>Platelet</td><td>120-320×1000/ul</td><td>450</td><td>400</td><td>360</td><td>100</td><td>50</td><td>30</td></tr><tr><td>7</td><td>Albumin</td><td>3.7-5.1 gm/dl</td><td>5.5</td><td>5</td><td>4.8</td><td>3.4</td><td>3</td><td>2.5</td></tr><tr><td>8</td><td>GPT</td><td>0-36 mg/dl</td><td>500</td><td>100</td><td>45</td><td>5</td><td>4</td><td>1</td></tr><tr><td>9</td><td>Alkaline-P</td><td>37-95 IU/l</td><td>200</td><td>150</td><td>129</td><td>40</td><td>30</td><td>20</td></tr><tr><td>10</td><td>Cholesterol</td><td>&lt;200 mg/dl</td><td>260</td><td>240</td><td>200</td><td>130</td><td>120</td><td>100</td></tr><tr><td>11</td><td>Triglyceride</td><td>30-160 mg/dl</td><td>500</td><td>300</td><td>180</td><td>120</td><td>100</td><td>50</td></tr><tr><td>12</td><td>Glucose(AC)</td><td>80-120 mg/dl</td><td>500</td><td>300</td><td>110</td><td>70</td><td>60</td><td>50</td></tr><tr><td>13</td><td>Creatinine</td><td>0.7-2.0 mg/dl</td><td>20</td><td>15</td><td>10</td><td>8</td><td>6</td><td>5</td></tr><tr><td>14</td><td>Uric Acid(Male)</td><td>2.7-8.5 mg/dl</td><td>10</td><td>8</td><td>7.6</td><td>3.4</td><td>3</td><td>2</td></tr><tr><td>15</td><td>Uric Acid(Female)</td><td>3.2-8.2 mg/dl</td><td>9</td><td>7</td><td>6</td><td>2.8</td><td>2.5</td><td>2</td></tr><tr><td>16</td><td>Na</td><td>134-138.5 meq/l</td><td>160</td><td>155</td><td>150</td><td>130</td><td>120</td><td>110</td></tr><tr><td>17</td><td>K</td><td>3.4-4.8 m\l</td><td>7.5</td><td>6.5</td><td>6</td><td>3</td><td>2.5</td><td>2</td></tr><tr><td>18</td><td>Ca</td><td>8.4-10.2 mg/dl</td><td>12.5</td><td>10</td><td>9.5</td><td>8.4</td><td>8</td><td>7</td></tr><tr><td>19</td><td>P</td><td>2.8-112 mg/dl</td><td>7</td><td>6</td><td>5.5</td><td>3.5</td><td>2</td><td>1.5</td></tr><tr><td>20</td><td>URR</td><td>0.65</td><td>0.8</td><td>0.75</td><td>0.7</td><td>0.6</td><td>0.55</td><td>0.5</td></tr><tr><td>21</td><td>kt/v(Daugirdes)</td><td>1.3</td><td>1.6</td><td>1.45</td><td>1.35</td><td>1.2</td><td>1</td><td>0.8</td></tr><tr><td>22</td><td>Fe</td><td>50-190 mg/dl</td><td>200</td><td>160</td><td>135</td><td>80</td><td>50</td><td>30</td></tr><tr><td>23</td><td>Ferritin</td><td>100-300 ng/ml</td><td>1000</td><td>800</td><td>650</td><td>300</td><td>150</td><td>50</td></tr><tr><td>24</td><td>Tranferrin saturation</td><td>35%</td><td>60</td><td>50</td><td>40</td><td>30</td><td>20</td><td>10</td></tr><tr><td>25</td><td>intact_PTH</td><td>130-195 pg/ml</td><td>1000</td><td>600</td><td>300</td><td>60</td><td>50</td><td>40</td></tr><tr><td>26</td><td>Ca×P</td><td>50</td><td>70</td><td>65</td><td>55</td><td>45</td><td>35</td><td>30</td></tr></table>

Since HD patients' physiology is different from that of a normal person, a minority of patients' routine biochemical test values are ultra-abnormal. Medical data often support this fact. Furthermore, when clinicians input biochemical test values into computers, it is hard to avoid typos, resulting in serious data analysis errors. Therefore, it is also necessary to contact clinicians about the standard value scope of various testing items in this step. Then outliers can be found based on three times of standard deviation [14]. After deleting spurious data as well as outliers, 6776 samples remained, including 3146 males and 3630 females. The average age was 59.92 and the standard deviation was 13.6. Out of 6776 patients, 1710 (25.24%) were hospitalized during their HD treatment sessions.

Because the DT algorithm does not allow null values, we discarded more than 15 percent of those features with missing data, such as Chloride (Cl), Normalized Protein Catabolic Rate (nPCR), Unsaturated Iron Binding Capacity (UIBC), Total Iron Binding Capacity (TIBC), Tranferrin saturation, Aluminum (Al), Magnesium (Mg), intact-PTH, and Cardiac/thoracic rate. For those features with less than 15 percent missing data, we <sup>fi</sup>lled up the mean value of previous and latter values of the patient. After deleting those values containing nulls and missing data, 6284 samples remained.

## 3.3. Transforming to temporal abstraction

To change the monthly biochemical test data of HD patients into TA, we developed a system to extract professional persons' HD knowledge. The conversion rule threshold for temporal abstraction inputted by clinicians is visually presented. Clinicians can also indicate the clinical signi<sup>fi</sup>cance of the biochemical testing item in the remarks column. The TA primitives are de<sup>fi</sup>ned as follows [24]:

1. State primitive: N (normal), L (low), VL (very low), XL (extreme low), H (high), VH (very high), and XH (extreme high).

2. Relations: “N” (change state to), “&” (and), “-“ (and then), and “/” (X/Y means the majority of points are in state X and the minority of points are in state Y).

Fig. 5 shows the transformation <sup>fl</sup>ow. Each biochemical test item should obtain its corresponding normal value in advance to de<sup>fi</sup>ne the threshold values for transforming to TA. Table 1 lists these data. A time interval should also be determined to transform data to TA. Hong [11] set the time interval of basic TA at three months. However, to <sup>fi</sup>nd out the evolutionary patterns which may cause patients' hospitalization in six months of HD treatment, our study de<sup>fi</sup>ned the complex TA as six months for one interval. A long-term HD patient that does not receive hospitalization within six to twelve months after treatment would be regarded as a non-hospitalization data set. A patient that receives hospitalization within six months after treatment would be regarded as a hospitalization data set.

This study transformed patients' biochemical test value data into basic TA through the basic TA algorithm, and inputted the result into the complex TA algorithm to <sup>fi</sup>gure out the complex TA described as follows.

## 3.3.1. Transforming to basic TA

The time series data of HD patients should be transformed to qualitatively describe with time interval before data mining, to execute temporal mining. Firstly we need to de<sup>fi</sup>ne the basic TA format according to the abstraction rules given by clinicians (as Fig. 6).

For example, we assume that the time series data of biochemical test values of a patient is recorded from January to October, shown in Fig. 7. According to the abstraction intervals of basic TA and complex TA, we can select a set of basic TA and a set of complex TA from the data.

## 3.3.2. Transforming to complex TA

Composing the basic TA to complex TA can be concatenated by the temporal operator. The temporal operator, N (from one state to another), states transforming and trend evolution. This study used the temporal operator put forward by Ho et al. [10] to concatenate the basic TA. For example, the patient's long-term representation can be indicated by complex TA "normal (N) N higher than normal (N/H)". The patient's biochemical test value changes from normal to higher, than to normal state from the <sup>fi</sup>rst month to the sixth month. This also means the patient's biochemical test value tends to climb. Therefore, the complex TA formed by using the temporal operator contains the basic state and trend abstraction at the same time. After obtaining the basic TA, we can input all patients' basic TA data into the complex TA algorithm to transform to temporal abstraction. The complex TA algorithm is as follows:

```txt
Complex TA algorithm
Input: Seasonal (S) Biochemical test items' (Bio) Basic TA (State_TA), current month (Near_HD_date), and hospitalization date (Hospital_date) of each patient (P)
Output: P.Complex_TA
Parameters: Hospitalization (Yes/No)
```

```txt
1 for each P
2    for every two seasons
3    if all Hospitals of P=N then
4    Judge S belongs in which Season according to Near_HD_date
5    Temp_V=P.S-1.Bio.State_TA>P.S.Bio.
6    State_TA
7    P.Complex_TA=Temp_V
8    else
9    Judge S belongs in which Season according to Hospital_date
10    Temp_V=P.S-1.Bio.State_TA>P.S.Bio.
11    State_TA
12    P.Complex_TA=Temp_V
13    end if
14 next
15 next
```

After executing the complex TA algorithm, Table 2 lists the data format for further analyzing, which will be inputted into the

![](/api/attachments/5K28UJES/fulltext/images/598037315de66a983ec1158b0e5d094a314c60d34c21bf8ed986a0a4041c9750.jpg)  
Fig. 6. Basic TA.

![](/api/attachments/5K28UJES/fulltext/images/956f5c6658501f80e5dd7410d834267da6cce85afbbfc6657f8c05a58f44a791.jpg)  
Fig. 7. Schematic diagram of temporal abstraction.

MSApriori algorithm and the C4.5 decision tree for hospitalization pattern mining.

## 3.4. Hospitalization rule mining

This study applied association rule mining with multiple minimum supports and the DT to analyze TA data of HD patients, and <sup>fi</sup>nds out rules for predicting patients' hospitalization, to prevent hospitalization of HD patients, described as follows.

## 3.4.1. Mining association rules with multiple minimum supports

Using Apriori for association rules mining results in a shortage. For example, in the retailing business, if the minimum support is set too high, all the discovered rules are concerned with low-price products, which only contribute a small portion of the pro<sup>fi</sup>t to the business. On the other hand, if minimum support set too low, many meaningless frequent rules will be generated that will overload the decision maker, making it dif<sup>fi</sup>cult to understand the rules [7]. Therefore, Liu et al. [19] proposed the MSapriori algorithm using multiple minimum supports for different items based on the Apriori architecture. The result was actually more effective than Apriori because its association rules with some important and infrequent item set were found.

Similar to the retail business, the MSapriori algorithm is suitable for analyzing HD patients' data because some TA items are closely related to patients' hospitalization rate such as Kt/V, URR, albumin etc. These items are so important, that the item's minimum support must be particularly considered by the clinician. Therefore, this study used the MSapriori algorithm to <sup>fi</sup>nd out the most relevant TA of the testing item causing hospitalization. Minimum item support (MIS) represents the minimum support for each testing item de<sup>fi</sup>ned as follows:

$$
M I S (i) = \frac {T A (i) \cup H _ {y e s}}{N}\tag{4}
$$

where i represents the testing item, TA(i) is the TA of each testing item, i.e. $. \mathrm { N } { > } \mathrm { N } / \mathrm { H } , H _ { y e s }$ indicates that the hospitalization type is yes, N is the number of samples, and ∪ means the union of sets TA(i) and $H _ { y e s } ,$ or say both TA(i) and $H _ { y e s } .$ If a TA's MIS is less than the threshold 0.1, then the TA's MIS is set at 0.1. To evaluate correlativity between the testing item and hospitalization, Conf is de<sup>fi</sup>ned as follows [3].

$$
\operatorname{Conf} \left(\mathrm{TA} (i) \rightarrow H _ {\text { yes }}\right) = P \left(H _ {\text { yes }} \mid T A (i)\right) = \frac {\operatorname{support} \left(T A (i) \cup H _ {\text { yes }}\right)}{\operatorname{support} (T A (i))}\tag{5}
$$

where $T A ( i )  H _ { y e s }$ is a rule and support(TA(i)) is the percentage of samples that contain TA(i). This study used the cosine measure proposed by Han and Kamber [9] to delete rules. The cosine measure of TA(i) and $H _ { y e s }$ is de<sup>fi</sup>ned as

$$
\begin{array}{c} \text {cosine} \Big (T A (i), H _ {y e s} \Big) = \frac {P \Big (T A (i) \cup H _ {y e s} \Big)}{\sqrt {P (T A (i)) \times P \Big (H _ {y e s} \Big)}} \\ = \frac {\text {support} \Big (T A (i) \cup H _ {y e s} \Big)}{\sqrt {\text {support} (T A (i)) \times \text {support} \Big (H _ {y e s} \Big)}}. \end{array}\tag{6}
$$

Let $\mathrm { L } _ { \mathrm { k } }$ denote the set of large k-item sets. Each item set c is of the following form, bc[1], c[2], …, c[k]N, which consists of items, c[1], c[2], …, c[k], where MIS(c[1])≤ MIS(c[2]) ${ \le } . . . { \le } \mathrm { M I S } ( \mathsf { c } [ \mathrm { k } ] )$ . The MSapriori algorithm is listed as follows [11]:

```txt
MSapriori algorithm
1 M=sort(I, MS) /* according to MIS(i)'s stored in MS */
2 F=int-pass(M, T) /* make the first pass over T */
3 L1={<f>|f∈F, f.count≥MIS(f)
4 for (k=1; Lk-1≠∅; k++) do
5    if k=2 then C2=level2-candidate-gen(F)
6    else Ck=candidate-gen(Lk-1) end
7    for each transaction t∈T do
8    Ct subset(Ck, t)
9    for each candidate c∈Ct do c.count++
10 end
11    Lk={c∈Ck|c.count≥MIS(c[ l])}
12 end
13 Answer=UkLk end

Algorithm level2-candidate-gen
Input: F
Output: a superset of the set of all large 2-itemsets
1 for each item f in F in the same order do
2 if f.count≥MIS(f) then
3 for each item h in F that is after f do
4    if h.count≥MIS(f) then
5 insert <f, h> into C2
```

## 3.4.2. Decision tree

The DT result determines which items can be used as the feature for predicting hospitalization mainly by calculating the information gain of each biochemical testing item. We used InfoGainAttributeEval as the index for calculating the signi<sup>fi</sup>cance level of each biochemical item, and used the Ranker method to rank all biochemical items according to their signi<sup>fi</sup>cance levels [26]. The biochemical items totaled 25 in all (see Table 3). Most of the parameter settings are software pre-settings, and the con<sup>fi</sup>dence factor for trimming changed from 0.25 to 0.3.

This study used 10-fold cross validation to validate the C4.5 decision tree model. Podgorelec et al. [20] also indicated that in medical data analysis, using sensibility and speci<sup>fi</sup>city to evaluate the prediction model for predicting classi<sup>fi</sup>cation accuracy is appropriate.

Table 2  
Partial data after executing complex TA transformation for association rule mining.

<table><tr><td>ID</td><td colspan="8">Items</td></tr><tr><td>59</td><td>Gender .F</td><td>Age .72</td><td>Diabetes.No</td><td>WBC.H&gt;N</td><td>RBC.L&gt;L</td><td>...</td><td>CaxP.N/L&gt;XL</td><td>Hospitalization.Yes</td></tr><tr><td>77</td><td>Gender .F</td><td>Age .72</td><td>Diabetes.No</td><td>WBC.N&gt;N</td><td>RBC.N&gt;N</td><td>...</td><td>CaxP.N/H&gt;H</td><td>Hospitalization.Yes</td></tr><tr><td>84</td><td>Gender .F</td><td>Age .76</td><td>Diabetes.Yes</td><td>WBC.N&gt;N/H</td><td>RBC.L&gt;L</td><td>...</td><td>CaxP.N/L&gt;L</td><td>Hospitalization.Yes</td></tr><tr><td>101</td><td>Gender .F</td><td>Age .52</td><td>Diabetes.Yes</td><td>WBC.N&gt;N</td><td>RBC.N/L&gt;N</td><td>...</td><td>CaxP.N/H&gt;N/L</td><td>Hospitalization.Yes</td></tr><tr><td>106</td><td>Gender .M</td><td>Age .81</td><td>Diabetes.No</td><td>WBC.N&gt;N</td><td>RBC.N/L&gt;N/L</td><td>...</td><td>CaxP.N/L&gt;N/L</td><td>Hospitalization.Yes</td></tr><tr><td>114</td><td>Gender .M</td><td>Age .72</td><td>Diabetes.No</td><td>WBC.N&gt;N</td><td>RBC.N/L&gt;N/L</td><td>...</td><td>CaxP.XL&gt;L</td><td>Hospitalization.Yes</td></tr><tr><td>140</td><td>Gender .F</td><td>Age .41</td><td>Diabetes.No</td><td>WBC.N&gt;N</td><td>RBC.L&gt;XL</td><td>...</td><td>CaxP.N/L&gt;N/L</td><td>Hospitalization.Yes</td></tr><tr><td>143</td><td>Gender .F</td><td>Age .44</td><td>Diabetes.No</td><td>WBC.N&gt;N</td><td>RBC.N/L&gt;L</td><td>...</td><td>CaxP.L&gt;XL</td><td>Hospitalization.Yes</td></tr><tr><td>168</td><td>Gender .F</td><td>Age .82</td><td>Diabetes.No</td><td>WBC.N&gt;H</td><td>RBC.N/L&gt;N/L</td><td>...</td><td>CaxP.N/H&gt;N/L</td><td>Hospitalization.Yes</td></tr><tr><td>187</td><td>Gender .M</td><td>Age .85</td><td>Diabetes.No</td><td>WBC.N&gt;N</td><td>RBC.N/L&gt;L</td><td>...</td><td>CaxP.N/L&gt;XL</td><td>Hospitalization.Yes</td></tr><tr><td>203</td><td>Gender .M</td><td>Age .72</td><td>Diabetes.No</td><td>WBC.N/H&gt;N/H</td><td>RBC.L&gt;XL</td><td>...</td><td>CaxP.XL&gt;N/L</td><td>Hospitalization.Yes</td></tr><tr><td>213</td><td>Gender .F</td><td>Age .48</td><td>Diabetes.No</td><td>WBC.N&gt;N</td><td>RBC.N/L&gt;N/L</td><td>...</td><td>CaxP.XH&gt;N</td><td>Hospitalization.Yes</td></tr></table>

Table 3  
Partial data after executing complex TA transformation for decision tree.

<table><tr><td>Gender</td><td>Age</td><td>Diabetes</td><td>WBC</td><td>RBC</td><td>Hbc</td><td>Hct</td><td>...</td><td>CaxP</td><td>Hospitalization</td></tr><tr><td>2</td><td>72</td><td>No</td><td>H&gt;N</td><td>L&gt;L</td><td>N&gt;N</td><td>Hct.N&gt;N</td><td>...</td><td>N/L&gt;XL</td><td>Yes</td></tr><tr><td>2</td><td>72</td><td>No</td><td>N&gt;N</td><td>N&gt;N</td><td>N&gt;N</td><td>Hct.N&gt;N</td><td>...</td><td>N/H&gt;H</td><td>Yes</td></tr><tr><td>2</td><td>76</td><td>Yes</td><td>N&gt;N/H</td><td>L&gt;L</td><td>N&gt;N</td><td>Hct.N&gt;N</td><td>...</td><td>N/L&gt;L</td><td>Yes</td></tr><tr><td>2</td><td>52</td><td>Yes</td><td>N&gt;N</td><td>N/L&gt;N</td><td>N&gt;N</td><td>Hct.N&gt;N</td><td>...</td><td>N/H&gt;N/L</td><td>Yes</td></tr><tr><td>1</td><td>81</td><td>No</td><td>N&gt;N</td><td>N/L&gt;N/L</td><td>N&gt;N</td><td>Hct.N&gt;N</td><td>...</td><td>N/L&gt;N/L</td><td>Yes</td></tr><tr><td>1</td><td>72</td><td>No</td><td>N&gt;N</td><td>N/L&gt;N/L</td><td>N&gt;N</td><td>Hct.N&gt;N</td><td>...</td><td>XL&gt;L</td><td>Yes</td></tr><tr><td>2</td><td>41</td><td>No</td><td>N&gt;N</td><td>L&gt;XL</td><td>N&gt;L</td><td>Hct.N/L&gt;N/L</td><td>...</td><td>N/L&gt;N/L</td><td>Yes</td></tr><tr><td>2</td><td>44</td><td>No</td><td>N&gt;N</td><td>N/L&gt;L</td><td>N&gt;N/L</td><td>Hct.N&gt;N</td><td>...</td><td>L&gt;XL</td><td>Yes</td></tr><tr><td>2</td><td>82</td><td>No</td><td>N&gt;H</td><td>N/L&gt;N/L</td><td>N&gt;N</td><td>Hct.N&gt;N</td><td>...</td><td>N/H&gt;N/L</td><td>Yes</td></tr><tr><td>1</td><td>85</td><td>No</td><td>N&gt;N</td><td>N/L&gt;L</td><td>N&gt;N</td><td>Hct.N&gt;N</td><td>...</td><td>N/L&gt;XL</td><td>Yes</td></tr><tr><td>1</td><td>72</td><td>No</td><td>N/H&gt;N/H</td><td>L&gt;XL</td><td>N&gt;L</td><td>Hct.N&gt;L</td><td>...</td><td>XL&gt;N/L</td><td>Yes</td></tr><tr><td>2</td><td>48</td><td>No</td><td>N&gt;N</td><td>N/L&gt;N/L</td><td>N&gt;N/L</td><td>Hct.N&gt;N</td><td>...</td><td>XH&gt;N</td><td>Yes</td></tr><tr><td>1</td><td>65</td><td>No</td><td>N&gt;N</td><td>N/L&gt;N/L</td><td>N&gt;N</td><td>Hct.N&gt;N</td><td>...</td><td>N&gt;XL</td><td>Yes</td></tr></table>

Sensitivity is the proportion of correctly predicted hospitalization of all patients, also known as the true positive fraction (TPF). Speci<sup>fi</sup>city is the proportion of samples correctly recognized as non-hospitalization of all patients without admission to hospital, also known as true negative fraction (TNF). Table 4 shows the formulae. The main purpose of this study is to <sup>fi</sup>nd out the biochemical test value patterns causing patients' hospitalization. Therefore, this study emphasizes sensibility evaluation.

## 4. Computational results

## 4.1. Parameters of TA

This research conducted an experiment using DT to compare two time intervals of TA including 3-month and 6-month intervals. For the latter, if a patient has a hospitalization record in July, then the experiment considered the biochemical value record from January to June. Experimental results show that the sensibility of a 6-month interval (81.60%) is much higher than the sensibility of a 3-month interval (13%). Furthermore, the performance of two different numbers of TA state were compared by also using DT, such as a 3-state (high, normal, low) TA versus a 7-state (extra high, high, higher than normal, normal, lower than normal, low, extra low) TA. The experimental results indicate that 7-state TA (81.60%) is better than that of a 3-state TA (71.50%).

Table 4  
Performance evaluation index formulae.

<table><tr><td></td><td>(Classified as) hospitalization</td><td>(Classified as) non-hospitalization</td></tr><tr><td>(Actual) hospitalization</td><td>TP</td><td>FN</td></tr><tr><td>(Actual) non-hospitalization</td><td>FP</td><td>TN</td></tr><tr><td>Sensitivity</td><td> $\frac{TP}{TP + FN}$ </td><td></td></tr><tr><td>Specificity</td><td> $\frac{TN}{TN + FP}$ </td><td></td></tr></table>

## 4.2. Results of data mining

The number of inferred rules is 215 from the DT and 477 from the MSapriori algorithm. After discussing and evaluating with <sup>fi</sup>ve domain experts, twenty-six clinically meaningful rules listed in Tables 5 and 6 were <sup>fi</sup>ltered to better predict HD patients' hospitalization. Some important rules are explained as follows.

## 4.2.1. Rules from the decision tree

Paths to each leaf of DT can be transformed into IF–THEN rules which are mutually exclusive and exhaustive on the IF parts. However, the rules are more complex than necessary. C4.5 employs a set of test samples independent from the training set to estimate the accuracy of each rule. A rule may be pruned by removing any condition in its antecedent that does not improve the estimate accuracy of the rule. For the following rules, the end of each rule in brackets includes the accuracy rate (accuracy) for predicting patients' hospitalization and the absolute number (occurrence) of patients supporting the rule.

## (1) Relevant rules to albumin

IF (Albumin=“normal(N) to extra low(XL)”) THEN (Hospitalization=YES) (accuracy: 93%, occurrence: 12)

Albumin represents current nutrition status and in<sup>fl</sup>ammation degree and is one of the utmost factors in<sup>fl</sup>uencing long-term survival. If albumin is less than 3.4 gm/dl, the patient will likely to be infected due to malnutrition, and the death hazard will increase accordingly. If albumin is less than 2.5 gm/dl, the relative death risk will increase by sixteen times, and relative hospitalization rate will also high [24].

Table 5  
Clinically meaningful rules of HD patients' hospitalization from DT.

<table><tr><td>No</td><td>Rules</td><td>Accuracy</td><td>Occurrence</td></tr><tr><td>1</td><td>Albumin = “lower than normal(N/L) to lower than normal(N/L)” AND Hbc = “normal(N) to low(L)”</td><td>100%</td><td>6</td></tr><tr><td>2</td><td>Albumin = “lower than normal(N/L) to low(L)” AND Triglyceride = “lower than normal(N/L) to low(L)” AND age &gt;74</td><td>100%</td><td>2</td></tr><tr><td>3</td><td>Albumin = “normal(N) to extra low(XL)”</td><td>93%</td><td>12</td></tr><tr><td>4</td><td>Albumin = “low(L) to extra low(XL)”</td><td>92%</td><td>11</td></tr><tr><td>5</td><td>Albumin = “extra low(XL) to extra low(XL)”</td><td>83%</td><td>12</td></tr><tr><td>6</td><td>Albumin = “normal(N) to low(L)”</td><td>83%</td><td>43</td></tr><tr><td>7</td><td>Albumin = “lower than normal(N/L) to lower than normal(N/L)” AND Platelet = “lower than normal(N/L) to normal(N)”</td><td>82%</td><td>7</td></tr><tr><td>8</td><td>Albumin = “lower than normal(N/L) to lower than normal(N/L)” AND Hbc = “normal(N) to lower than normal(N/L)”</td><td>78%</td><td>8</td></tr><tr><td>9</td><td>Albumin = “lower than normal(N/L) to low(L)” AND Triglyceride = “low(L) to low(L)” AND K = “normal(N) to normal(N)”</td><td>75%</td><td>12</td></tr><tr><td>10</td><td>Albumin = “normal(N) to lower than normal(N/L)”</td><td>71%</td><td>188</td></tr><tr><td>11</td><td>Albumin = “low(L) to low(L)”</td><td>71%</td><td>30</td></tr></table>

(2) Relevant rule to albumin, hemachrome (Hbc), and platelet IF (Albumin=“lower than normal(N/L) to lower than normal (N/L)”) AND (Hbc=“normal(N) to low(L)”) THEN (Hospitalization=YES) (accuracy: 100%, occurrence: 6)

A patient with a low Hbc or insuf<sup>fi</sup>cient Hbc indicates that he has anemia. Worse still is the patient with malnutrition, who may have insuf<sup>fi</sup>cient antibodies and will likely contract other diseases. The major function of the platelet is to form thrombosis and concretionary shrinkage to arrest bleeding. Platelet value increases due to anemia, hepatocirrhosis, acute infection, chronic granular leukaemia, rheumatiod arthritis and so on.

(3) Relevant rule to albumin, triglyceride, and age

IF (Albumin=“lower than normal(N/L) to low(L)”) AND (Triglyceride=“lower than normal(N/L) to low(L)”) AND (age greater than 74) THEN (Hospitalization=YES) (accu racy: 100%, occurrence: 2)

Triglyceride is the fat in blood that mainly provides cellular capacity. A triglyceride decline may cause a lack of lipoprotein, chronic obstructive pulmonary disease, hyperthyroidism and malnutrition. Aged hemodialysis patients are likely to need hospitalization because of insuf<sup>fi</sup>cient nutrition and low triglycerides.

## 4.2.2. Rules from the MSapriori algorithm

Rules from the association rule mining are based on all frequent item sets which have been found using the MSapriori algorithm.

Strong association rules are those with a con<sup>fi</sup>dence value above a given threshold (0.7). The value of support in this study was initially set at 0.2 and adjusted by plus/minus 0.05 for the MIS setting. Unnecessary rules were deleted based on the rule reducing formula of Eq. (6).

(1) Rules related to blood examination

IF (Hct=“normal(N) to lower than normal(N/L)”) THEN (Hospitalization=YES) (support: 0.079, Conf: 0.77, occurrence: 213)

Decreased Hct is an index for judging whether the patient is anemic or not. A patient with lower Hct results in anoxia, dyspnea, and dilutedness, symptoms of serious anemia.

IF (RBC=“lower than normal(N/L) to low(L)”) AND (Albumin=“normal(N) to lower than normal(N/L)”) THEN (Hospitalization=YES) (support: 0.013; Conf: 0.87, occurrence: 48) A low erythrocyte (RBC) value means anemia. The patient should use erythropoietin just in time. Otherwise insuf<sup>fi</sup>cient nutrition will lead to contracting other diseases.

## (2) Other rules related to examination value

IF (Diabetes=YES) AND (Ca×P=“lower than normal(N/L) to lower than normal(N/L)”) AND (Phosphorous=“normal (N) to normal(N)”) THEN (Hospitalization=YES) (support: 0.02; Conf: 0.93, occurrence:70)

Generally speaking, the higher the Ca×P value is, the more likely the incidence of coronary heart disease and heart failure caused by calci<sup>fi</sup>cation of the main coronary artery and cardiac muscle. However, because diabetes patients have special characteristics, this study discusses the standard interval of Ca×P for diabetes patients.

Table 6  
Clinically meaningful rules of HD patients' hospitalization from MSApriori algorithm

<table><tr><td>No</td><td>Rules</td><td>support</td><td>Conf.</td><td>occurrence</td></tr><tr><td>1</td><td>Diabetes = YES AND RBC = lower than normal(N/L) to lower than normal(N/L)&quot; AND URR = &quot;high(H) to high(H)&quot; AND Kt/V = &quot;extra high(XH) to extra high(XH)&quot;</td><td>0.013</td><td>0.96</td><td>45</td></tr><tr><td>2</td><td>Hbc = &quot;normal(N) to lower than normal(N/L)&quot;) AND Albumin = &quot;normal(N) to lower than normal(N/L)&quot;</td><td>0.014</td><td>0.95</td><td>42</td></tr><tr><td>3</td><td>Diabetes = YES AND Ca × P = &quot;lower than normal(N/L) to lower than normal(N/L)&quot; AND P = &quot;normal(N) to normal(N)&quot;</td><td>0.02</td><td>0.93</td><td>70</td></tr><tr><td>4</td><td>Diabetes = YES AND Albumin = &quot;normal(N) to lower than normal(N/L)&quot; AND GlucoseAC = &quot;higher than normal(N/H) to higher than normal(N/H)&quot;</td><td>0.012</td><td>0.92</td><td>44</td></tr><tr><td>5</td><td>Diabetes = YES AND MCV = &quot;normal(N) to normal(N)&quot; AND Albumin = &quot;normal(N) to lower than normal(N/L)&quot;</td><td>0.011</td><td>0.89</td><td>39</td></tr><tr><td>6</td><td>Albumin = &quot;normal(N) to lower than normal(N/L)&quot; AND Creatinine = &quot;lower than normal(N/L) to lower than normal(N/L)&quot;</td><td>0.012</td><td>0.89</td><td>42</td></tr><tr><td>7</td><td>RBC = &quot;lower than normal(N/L) to low(L)&quot; AND Albumin = &quot;normal(N) to lower than normal(N/L)&quot;</td><td>0.013</td><td>0.87</td><td>48</td></tr><tr><td>8</td><td>Hct = &quot;normal(N) to lower than normal(N/L)&quot; AND Albumin = &quot;normal(N) to lower than normal(N/L)&quot;</td><td>0.013</td><td>0.87</td><td>41</td></tr><tr><td>9</td><td>Diabetes = YES AND Hbc = &quot;normal(N) to lower than normal(N/L)&quot; AND Hct = &quot;normal(N) to lower than normal(N/L)&quot;</td><td>0.012</td><td>0.87</td><td>45</td></tr><tr><td>10</td><td>Albumin = &quot;normal(N) to lower than normal(N/L)&quot;</td><td>0.065</td><td>0.83</td><td>188</td></tr><tr><td>11</td><td>Hbc = &quot;normal(N) to lower than normal(N/L)&quot; AND Hct = &quot;normal(N) to lower than normal(N/L)&quot;</td><td>0.035</td><td>0.81</td><td>100</td></tr><tr><td>12</td><td>RBC = &quot;lower than normal(N/L) to low(L)&quot; AND Hbc = &quot;normal(N) to lower than normal(N/L)&quot; AND Hct = &quot;normal(N) to lower than normal(N/L)&quot;</td><td>0.018</td><td>0.80</td><td>52</td></tr><tr><td>13</td><td>Hct = &quot;normal(N) to lower than normal(N/L)&quot;</td><td>0.079</td><td>0.77</td><td>213</td></tr><tr><td>14</td><td>Albumin = &quot;lower than normal(N/L) to lower than normal(N/L)&quot;</td><td>0.02</td><td>0.72</td><td>80</td></tr><tr><td>15</td><td>Diabetes = YES AND WBC = &quot;normal(N) to higher than normal(N/H)&quot;</td><td>0.018</td><td>0.70</td><td>66</td></tr></table>

If (Albumin=“normal(N) to lower than normal(N/L)”) THEN (Hospitalization=YES) (support:0.065; Conf:0.83, occurrence:188)

The same result obtained from the decision tree, too low albumin is still an important index for prognosis.

## 4.3. Summary

Although rules obtained from both DT and MSapriori algorithms are meaningful, we suggest using the MSapriori algorithm to <sup>fi</sup>nd HD patients' hospitalization rules because of the following reasons: (1) The MSapriori algorithm allows missing value, whereas the DT algorithm does not allow any null values. (2) The MSapriori algorithm concentrates on one class, disregarding what happens to the other classes, whereas the DT split takes all classes into account, trying to maximize the purity of the split. (3) The set of extracted rules from DT is not much simpler than the corresponding DT. Therefore, we need to do some more work by pruning the resulting rule set, whereas rules from the MSapriori algorithm are easier. (4) Rules selected by the DT within a class are according to their estimated accuracy. These will result in lower occurrences. Comparison between Tables 5 and 6, the number of occurrence from DT is less than the one from the MSApriori algorithm.

## 5. Conclusion

Medical data analysis includes data gathering, preprocessing, result evaluation, favorable interaction, and discussions with clinicians for correct analytic results [4,6,8,13]. This study used data mining techniques for extracting professional knowledge. This method is an improvement over traditional face-to-face discussions with professional persons, and enables us to obtain important knowledge effectively and quickly.

The experimental results show that different data mining methods can be combined effectively, and more abundant patterns can be found for practical applications. Furthermore, we can add domain knowledge prior to data analysis by combining the TA method, to make mining results more likely comprehended by the clinician. Therefore, TA is an indispensable method for future medical time series data analyses.

Among the hospitalization patterns found in this study, albumin is the most important index for predicting patients' hospitalization. This index is also currently used clinically for predicting patients' death rate. The results of this study therefore have clinical signi<sup>fi</sup>cance. Predicting patients' hospitalization by biochemical value evolution of blood examination has been an unde<sup>fi</sup>ned biochemical item in previous clinical applications. After validating by medical care personnel, the time evolution of this index value proves to have de<sup>fi</sup>nite relevance for hospitalization.

This study combined TA with data mining techniques to analyze dialysis patients' biochemical data. The mined temporal hospitalization patterns are helpful for doctors to diagnose patient hospitalization probability and to suggest some immediate treatments to avoid hospitalization. Finally, we hope this research will help hemodialysis centers to improve health care quality.

Many relevant methods and concepts could be added for analysis results. Directions for future research include the following three points. First, Adlassnig et al. [1] indicated that combining TA with Fuzzy Logic is more coincident for describing actual temporal data situations and is also a direction worthy of study. Second, HD patients' hospitalization rules can be obtained either by one-class classi<sup>fi</sup>cation method [15] or by subgroup discovery algorithm [18]. Third, for mined temporal patterns, implementing a system to assist medical care personnel to carry out medical intervention or treatment, namely to automate the overall <sup>fl</sup>ow from temporal mining preprocessing to rule generating, would assist medical personnel with daily business.

## Acknowledgement

We are grateful to the National Science Council for the grants program (NSC97-2221-E-415-008-MY3), and to the Hemodialysis Center of Chiayi Yang Ming Hospital for their professional consultations.

## References

[1] K.P. Adlassnig, C. Combi, A.K. Das, E.T. Keravnou, G. Pozzi, Temporal representation and reasoning in medicine: research directions and challenges Artificia Intelligence in Medicine 38 (2006) 101–113.

[2] J.F. Allen, Towards a general theory of action and time, Arti<sup>fi</sup>cial Intelligence 23 (1984) 123–154.

[3] R. Bellazzi, C. Larizza, P. Magni, R. Bellazzi, Temporal data mining for the quality assessment of hemodialysis services, Arti<sup>fi</sup>cial Intelligence in Medicine 34 (2005) 25–39.

[4] R. Bellazzi, B. Zupan, Predictive data mining in clinical medicine: current issues and guidelines, International Journal of Medical Informatics 77 (2) (2008) 81–97.

[5] S. Concaro, L. Sacchi, C. Cerra, P. Fratino, R. Bellazzi, Mining healthcare data with temporal association rules: improvements and assessment for a practice use Lecture Notes in Computer Science 5651 (2009) 16–25.

[6] J. Demsar, B. Zupan, N. Aoki, M.J. Wall, T.H. Granchi, J.R. Beck, Feature mining and predictive model construction from severe trauma patient's data, International Journal of Medical Informatics 63 (2001) 41–50.

[7] Y.H. Ding, M.Y. Chen, Data Mining, Canghai Books, Taiwan, 2003.

[8] U. Fayyad, G.P. Shapiro, P. Smyth, From data mining to knowledge discovery in databases, Arti<sup>fi</sup>cial Intelligence Magazine 17 (3) (1996) 37–54.

[9] J. Han, M. Kamber, Data Mining: Concepts and Techniques, Morgan Kaufmann Publishers, New York, 2006.

[10] T.B. Ho, T.D. Nguyen, S. Kawasaki, S.Q. Le, D.D. Nguyen, H. Yokoi, K. Takabayashi Mining hepatitis data with temporal abstraction, Proc. of ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, Washington, DC, USA, 2003.

[11] G. Q. Hong, Multiple-minimum-support association rule mining for hospitalization prediction of hemodialysis patients, M.S. thesis, Department of Information Engineering, National Tung Hua University, Taiwan, 2004.

[12] Y.H. Hu, Y.L. Chen, Mining association rules with multiple minimum supports: a new mining algorithm and a support tuning mechanism, Decision Support Systems 42 (1) (2006) 1–24.

[13] M.J. Huang, M.Y. Chen, S.C. Lee, Integrating data mining with case-based reasoning for chronic diseases prognosis and diagnosis, Expert Systems with Applications 32 (3) (2007) 856–867.

[14] M. Kantardzic, Data Mining: Concepts, Models, Methods, and Algorithms, John Wiley, New York, 2003.

[15] M. Koppel, J. Schler, Authorship veri<sup>fi</sup>cation as a one-class classi<sup>fi</sup>cation problem, Proc. of the Twenty-<sup>fi</sup>rst International Conference on Machine Learning (ICML 2004), Banff, Alberta, Canada, 2004.

[16] A. Kusiak, B. Dixon, S. Shah, Predicting survival time for kidney dialysis patients: a data mining approach, Computers in Biology and Medicine 35 (2005) 311–327.

[17] N. Lavrac, E. Keravnou, B. Zupan, Intelligent data analysis in medicine, in: A. Kent (Ed.), Encyclopedia of Computer Science and Technology 42, Marcel Dekker, New York, USA, Basel, 2000, pp. 113–157.

[18] N. Lavrac, B. Kavsek, P. Flach, L. Todorovski, Subgroup discovery with CN2-SD, Journal of Machine Learning Research 5 (2004) 153–188.

[19] B. Liu, W. Hsu, Y. Ma, Mining association rules with multiple minimum supports, Proc. of ACM SIGKDD International Conference on knowledge Discovery & Data Mining (KDD-99), San Diego, CA, USA, 1999.

[20] V. Podgorelec, P. Kokol, M.M. Stiglic, M. Hericko, I. Rozman, Knowledge discovery with classi<sup>fi</sup>cation rules in a cardiovascular dataset, Computer Methods and Programs in Biomedicine 80 (2005) S39–S49.

[21] L. Sacchi, C. Larizza, C. Combi, R. Bellazzi, Data mining with temporal abstractions: learning rules from time series, Data Mining and Knowledge Discovery 15 (2007) 217–247.

[22] Y. Shahar, A framework for knowledge-based temporal abstraction, Arti<sup>fi</sup>cial Intelligence 90 (1997) 79–133

[23] M. Stacey, C. McGregor, Temporal abstraction in intelligent clinical data analysis: a survey, Arti<sup>fi</sup>cial Intelligence in Medicine 39 (2007) 1–24.

[24] T. Takabayashi, T.B. Ho, H. Yokoi, T.D. Nguyen, S. Kawasaki, S.Q. Le, Temporal abstraction and data mining with visualization of laboratory data, Medinfo 2007 Congress, Brisbane, 2007, pp. 1304–13088, 2007.

[25] C.G. Tan, Interpretation of periodic examination results of dialysis patients, 20048 [Onlinel. Available http://www.kidney.org.tw/doc/49/01.doc

[26] I.H. Witten, E. Frank, Data Mining: Practical Machine Learning Tools and Techniques, 2nd Ed.Morgan Kaufmann, New York USA 2005
