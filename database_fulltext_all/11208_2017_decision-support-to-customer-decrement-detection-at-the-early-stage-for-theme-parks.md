---
otero_id: 11208
otero_key: "VJDKGA3J"
title: "Decision support to customer decrement detection at the early stage for theme parks"
authors: "Chung-En Yen; Chun-Che Huang; Dan-Wei (Marian) Wen; You-Ping Wang"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.07.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Decision support to customer decrement detection at the early stage for theme parks

Yen Chung-en, Chun-Che Huang, Marian (Dan-Wei) Wen, Wang You-Ping

![](/api/attachments/VJDKGA3J/fulltext/images/b027503f8d3eeabc9918e072384710f89af6239dcb2573610ac8fcdfd58f71d4.jpg)

PII: S0167-9236(17)30143-4

DOI: doi: 10.1016/j.dss.2017.07.005

Reference: DECSUP 12866

To appear in: Decision Support Systems

Received date: 21 December 2016

Revised date: 28 July 2017

Accepted date: 29 July 2017

Please cite this article as: Yen Chung-en, Chun-Che Huang, Marian (Dan-Wei) Wen, Wang You-Ping , Decision support to customer decrement detection at the early stage for theme parks, Decision Support Systems (2017), doi: 10.1016/j.dss.2017.07.005

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

Article reference: DECSUP\_DECSUP-D-16-00943

# Decision Support to Customer Decrement Detection at the Early Stage for Theme Parks

Yen Chung-en<sup>a</sup>; Chun-Che Huang<sup>b\*</sup>; Marian (Dan-Wei) Wen<sup>c</sup>; Wang You-Ping<sup>d</sup>

<sup>a</sup> Management School, Program in Strategy and Development of Emerging Industries, National Chi Nan University, Taiwan,

<sup>b</sup> Department of Information Management, National Chi Nan University, Taiwan, cchuang@ncnu.edu.tw to whom correspond to

<sup>c</sup> Department of Business Administration, National Cheng Kung University, Taiwan, marian.wen@gmail.com

<sup>d</sup> Department of Information Management, National Chi Nan University, Taiwan, s101213504@mail1.ncnu.edu.tw

## Decision Support to Customer Decrement Detection at the Early Stage for Theme Parks

## Abstract

In recent years, a theme park drives significant attention in tourism industry due to the provision of quality and integrated service, and issuing annual pass cards help the theme park to differentiate long-term customers from short-term ones. Customer Value Analysis is demanded for theme parks to identify potential customers as well as to appraise customer value through the setting of the annual pass. Moreover, customer value often alters from time to time since theme park industry is relevantly competitive and innovation demanded than other industries, and customer preferences are frequently changed. This study provides an early warning system to support the theme park to detect, monitor and analyze the changes of customer value. By applying the aggregated approach based on Rough Set Theory and Recency, Frequency and Monetary architecture, the tourist satisfaction levels can be captured after the aforementioned approach is executed. In addition, the rule comparison approach is contributed to predicting customer behavior from technical viewpoint. This study aims at providing an early correction strategy for the theme park to avoid losing VIP customers and identify latent customers.

Key words: Customer Decrement Detection, Customer Value Analysis, Rough Set Theory.

## 1. Introduction

Theme parks offer more interactive experiences, instead of passive patterns in traditional amusement parks [1], to enhance the parent-child relationship through the interaction and discussion of facilities and themes [1, 2]. The flourishing of theme parks has induced many studies [3-5], which conclude that a well-developed theme park, with limited land, capitals, and resources, cannot continuously rely on expanding the land and building new facilities to attract visitors. Business should recognize which stage of Tourism Area Life Cycle (first proposed by Butler in 1980 [3, 4] , the theme park is posited: Exploration, Involvement, Development, Consolidation, Stagnation, Decline or Rejuvenation stage).

Although tourism life cycle and related work reveal that a theme park should pay attention to how to stay on the consolidation and stagnation stage and prevent from falling into decline stage, discussions on the conceptual stage and practical mechanisms for theme park managers are required in the competitive tourism industry. That is, providing an early warning is crucial. Traditional early warning literatures almost relied on three approaches, namely financial analysis approach, signaling approach, and logit regression. According to financial analysis approach, the bankruptcy prediction model [5] is created based on risk detection [6]. However, it is often too late to prevent from stepping in decline stage. The downside of signaling approach is that it considers early warning indicators separately [7] and the downside of the logit regression is unable to result that the regression can ultimately be estimated only on a relatively short sample [8]. Therefore, a novel approach is required to decoct customer decrement at the early stage of a theme park by permanently observing the potential value and behaviors of customers to prevent it from getting into Decline Stage and even to guide the theme park to positive Rejuvenation Stage.

To achieve this goal, Customer Value Analysis is therefore required for a well-developed theme park finding out valuable customers. Customer Value Analysis at a single time point could reveal the customer value at the time, but could not show the long-term trend, such as the disappearance, decline, and changes of loyal customers. It therefore could result in missing the opportunity to find out potential customers and even possibly to invest resources in declined customers. These are important warnings of a theme park getting into the decline stage. Nevertheless, when a theme park is not aware of the situation, but simply proposes strategies based on short-term collected Customer Value Analysis, it might no longer attract customers, lose customer confidence, reduce competitiveness, and cause loss of customers to gradually step into the decline stage.

Furthermore, current indicators for analyzing customer value, namely recency, frequency and monetary [9, 10] , only pay attention to the quantitative data. However, feedbacks from visitors, e.g., questionnaire, may use common languages, e.g. High, Low, Large, for qualitative indicators. Such neglect of qualitative indicators may pose potential risk of ignoring how customers feel about the designed climate or situation by the theme park, leaving the theme park unaware of intrinsic voice of the customers. In order to address the aforementioned limitations in the literature, this paper evaluates both quantitative and qualitative indicators for theme park managers to detect changes in customer value and decrement.

In this study, quantitatively, recency, frequency and monetary [9, 10] are considered in the system and, qualitatively, customer satisfaction [11, 12] and destination image [13, 14] are adopted. These five indicators together form a more comprehensive view in analyzing customer value. Thus, rough set (RS) theory [15], which can simultaneously evaluate quantitative and qualitative indicators, is used. Traditional RS approaches are ―one-shot solution‖ and merely focus on how rules are generated and validated. Further rule set comparison has not been precisely and thoroughly conducted and implemented. None of them discusses the implication of rule change. This study, from the technical viewpoint, contributes to enhancing the accuracy in capturing critical indicators by using weight [16]. Besides, rule comparison [17] is adopted to reflect the

# ACCEPTED MANUSCRIPT

change of customer values, making the warning system more practical.

This study provides some guidance for theme parks promoting yearly concession cards and effectively finding out the value of card customers. The trend of customer development at different time points is also emphasized to solve the problem of a theme park continuously investing high marketing resources in disappearing loyal customers. The research objectives are summarized (1) to identify problems of a theme park promoting yearly concession cards and risks caused by improper management, (2) to formulate solutions for a theme park which is not able to effectively find out important customers and the trend of customer development at a single time point, and (3) to verify the advantage of the approach through case study that the volume increase/decrease in the various membership categories can be recognized.

This study has following restrictions. (1) Data collection and access methods are not discussed, as this study focuses on the warning model. (2) It is assumed that customers would sincerely respond to the questionnaire without refusal or casual responses. The remaining of the paper is organized as following. Section 2 surveys the literature and the methodology is proposed in Section 3. A case is studied in Section 4 to demonstrate the value of this study. Section 5 concludes this study.

## 2. Literature review

Tourism Area Life Cycle was first proposed by Butler in 1980 [4], who considered that tourism industry would follow the stages of Exploration, Involvement, Development, Consolidation, Stagnation and eventually encounter Decline or Rejuvenation. Accordingly, research on Tourism Area Life Cycle has not been settled, but tourist spots could encounter Decline Stage, no matter how Tourism Area Life Cycle is developed. Manente and Pechlaner [18] applied IDES to design an Early Warning System for detecting

Decline Stage. However, little research focused on the prediction of Decline Stage, especially in the analysis of theme parks.

To provide an early warning, this study focuses on permanently observing the potential value and behaviors of customers to prevent it from getting into decline stage and even guiding the theme park to positive rejuvenation stage. For the theme park to understand the current stage in Tourism Area Life Cycle and to make optimum resource allocation effectively, Customer Value Analysis [19-22] is one of crucial perspectives and presents two important points for enterprises, including taking the cognition of changeable customers into account for decision makers making corporate strategies [23, 24] and striving for loyal customers to further acquire higher income, reduce loss of customers, and decrease expenses to benefit the company [25]. For example, Lee and his colleagues [26] found the significant relationship between customer perceived value and customer loyalty from a South Korean Water Park case, with service quality, image, and food quality to enhance the interaction. Zeithaml, et al. [27] proved that increasing 5％ customer retention rate could result in 25-95％ profit growth. Many companies discovered that it was not necessary to offer equivalent services to all customers, as some customers were more profitable than others. Recent studies further indicated the strong impact of life-long value of customers, instead of only making purchase for one time or a short period of time, on the profitability of a firm [28].

To discuss customer value through customer behaviors, RFM (Recency, Frequency and Monetary) first proposed by Hughes in 1994 has been broadly applied [9, 10]. Due to low complexity, RFM is often used with Customer Value Analysis. For instance, Khajvand et al. [29] applied Customer Lifetime Value matching with RFM to calculate customers’ purchase behaviors. However, traditional Customer Value Analysis

methods [30], e.g. Customer Profitability Analysis [31] and Customer Lifetime Value Analysis [32], require more complicated numerical equations for the calculation and focus more on quantization that customer behaviors could not be discussed from the qualitative aspect. Rough Set Theory, first proposed by Pawlak in 1982 [33] with qualitative and quantitative data analysis ability, is utilized in this study; and, by integrating customer behavior attributes and RFM customer value, reduction is applied to help theme parks understand customer classification knowledge with less time and costs.

In this study, customer satisfaction and customers’ tourism imagery are also considered to complete the evaluation model. Customer satisfaction refers to the anticipated psychology of customers in the product or service life cycle [34]. A lot of research indicated that satisfactory travel experiences could benefit the loyalty of targets [11, 12]. Tourism imagery, on the other hand, refers to the overall impression or attitudes towards a place. The overall impression is composed of visitors’ perceived tourism quality. The evaluation understand visitor behaviors [13, 35].

## 3. Research methodology

As discussed in the literature review that quantitative indicators (e.g., recency, frequency and monetary [9, 10]) and qualitative ones (e.g., customer satisfaction and destination image) need to be considered simultaneously to make rough set [15] adequate for this research. This approach was proposed by Pawlak in 1982 [33] to find rules from incomplete and inconsistent data or knowledge by looking into the relations within the dataset [33]. In a rough set, a decision table that comprises condition attributes and decision attributes is fundamental to extract relations, and every object in the decision table represents a set of data

# ACCEPTED MANUSCRIPT

described by condition attributes and decision attributes [36].

Since its outset, rough set has been widely applied to management, engineering, medical science, and finance [37, 38] as well as been significantly improved [15]. Among various attempts in improving rough set approach, two salients in managerial decision making incorporate weight in the attributes [16] and compare rules across different time periods [17]. Although they are distinctively important, joint consideration is even more realistic for managers because in most cases, decision making involves viewing some attributes more significantly than others while comparing them to see the changes and trend. Therefore, this research proposes a framework that integrates weight and rule comparison, which has been overlooked.

In this study, the rough set (RS) approach is used for extracting information and knowledge from inaccurate, incomplete, and inconsistent data [33]. The RFM evaluation model and tourism related evaluation attributes are included in the conditional attribute evaluation. Previous research on Rough Set approaches simply focused on solving one-time rules, but seldom discussed the changes with time. With the proposed Customer Value Analysis, rule comparison is applied to propose a decision support system, called Early Warning System (EWS) for assisting theme parks in understanding the trend of customer changes with time, evaluating the value decline of loyal customers, and preventing theme parks from getting into Decline Stage because of investing great marketing resources in wrong customers.

As rough set gains popularity due to its capacity in excavating valuable knowledge from inaccurate, incomplete, or inconsistent raw data, a variety of improvements have been proposed. However, they tend to solve one drawback of rough set at a time, making real-world implementation problematic. Therefore, to implement an early warning system for theme parks to detect risk of decline, this research carefully

integrates two major breakthroughs, rule comparison [17] and weight [16], to conform to the requirements of finding changes and giving different value to customer characteristics.

## 3.1 Rough Set Based Rule Generation for Customer Value Analysis

Traditional RS approaches often generated many unimportant and uncertain classification decision rules. Rough Set based Rule Extraction Algorithm (RSREA), is proposed in this study, and the idea of weight index is also included for searching more meaningful and obvious important rules, according to the weights. The idea of weight enhances the reliability of rules and solves the possible problem of rule repeatability.

Conditional attributes in this study are classified into attributes to evaluate customer behaviors and attributes to evaluate customer value. For calculating the weights in RSREA, each conditional attribute would be given a weight to calculate the strength index (SI), which recognizes significant rules. (1) Customer Behavior Attributes: Customers’ basic data are covered, such as gender, place of residence, and Section 4, several attributes are used. (2) Customers Value Attributes: Such attributes are evaluative, and the elements are ordered with 1\~5 as the evaluation standard. In the case study in Section 4, the RFM evaluation model matches with tourism imagery and tourist satisfaction as the customer value attributes are applied. (i) Recency (R) is primary for a theme park. With deeper analyses, customer preference could be understood. For example, some customers prefer visiting a theme park in certain seasons or on special holidays for the activities. (ii) Frequency could enhance customer consumption. Generally speaking, a customer often visiting a theme park could possibly be affected the consumption by the environment, climat interpersonal relationship, and psychology to show higher consumption probability than customers who

seldom visit the park. (iii) Monetary refers to additional consumption for other services beyond the ticket. Theme parks offer integrated services, and the consumption is diversified. However, past research on RFM merely evaluated customer consumption with Monetary. To better conform to the real situation in a theme park, Monetary is divided into "souvenir consumption", "extra activity consumption", and "Accommodation and food consumption" for making more accurate analyses. (iv) Customer satisfaction (CS). Several studies proved that customer satisfaction would enhance loyalty that it is included in the evaluation model of theme parks. However, total satisfaction contains various compositions, such as "facility satisfaction", "activity satisfaction", "price satisfaction", and "service satisfaction". Accordingly, satisfaction is divided into such four attributes for the evaluation. (v) Tourism imagery (TC). Including tourism imagery in the evaluation allows a theme park realizing customer opinions and feelings before visiting the park. It could help a theme park make adjustment and improvement on the future advertisement and marketing. Similarly, tourism imagery in this study is classified into four attributes of "Destination brand imagery", "Emotional imagery", "Entertainment imagery", and "Climate imagery".

(3) Decision attributes classify customers with Tourism Customer Pyramid, where the most valuable customers are on the top and descending in sequence. For instance, the class of yearly concession cards is used in this study for the classification that Platinum customers are placed on the top, while those without concession cards are at the bottom. Customers who might damage facilities and even commit crimes are excluded in this study, as such customers are special cases and theme parks normally have their exclusion mechanisms. This study aims to find out important customers that such special conditions are not discussed

According to rough set theory, the decision table is used and presented in Table 1.

Table 1 Customer value analysis

<table><tr><td></td><td colspan="4">Customer behavior attributes</td><td colspan="5">Customers value attributes</td><td colspan="2">Decision attributes</td></tr><tr><td>Object No.</td><td>Gender</td><td>Place of residence</td><td>Age group</td><td>Other attributes</td><td>R</td><td>F</td><td>M</td><td>CS</td><td>TI</td><td>Classes of Concession card</td><td>Cards</td></tr><tr><td>1</td><td>Male</td><td>Foreign country</td><td>Adult</td><td>...</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>Platinum customers</td><td>20</td></tr><tr><td>2</td><td>Female</td><td>Domestic (close)</td><td>Senior</td><td>...</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>Gold customers</td><td>30</td></tr><tr><td>3</td><td>Male</td><td>Domestic (close)</td><td>Adult</td><td>...</td><td>3</td><td>4</td><td>3</td><td>3</td><td>3</td><td>Silver customers</td><td>10</td></tr><tr><td>4</td><td>Male</td><td>Domestic (far)</td><td>Child</td><td>...</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>Common customers</td><td>20</td></tr><tr><td>Weight</td><td>0.1</td><td>0.1</td><td>0.1</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td></td><td></td></tr></table>

In traditional RS theory, a subset of attributes has more than one reduction, hence the simplification of decision rules does not yield unique results. Thus decision rules can be inducted according to the presumed criteria related to the user's problem domain. In general, a decision rule is a combination of the value of some attributes such that the set of all objects matching it is contained in the set of objects labeled with the same class. In order to simplify the decision table, value-reductions of the attributes illustrated in the previous section should be determined. Denote rule $r _ { i }$ as an expression:

$$
r _ {i} \colon (A _ {i 1} = u _ {i 1}) \wedge (A _ {i 2} = u _ {i 2}) \vee \dots \wedge (A _ {i n} = u _ {i n}) \rightarrow (O = u _ {d})
$$

where: $u _ { i I } , u _ { i 2 } , . . . , u _ { i n } ,$ and $u _ { d }$ are the value contents of the attributes; set $\{ \lor , \land , \to \}$ of connectives are disjunction, conjunction, implication, respectively.

Basically, a set of specific decision rules (reductions) forms a reduced information system. Each rule corresponds to exactly one equivalent class of the original system. Next, the RSREA is presented in Fig. 1. Specifically, steps 4-6 can avoid generating repetitive rules.

Notations. t: reduction index, X : object number, ${ \mathrm { R } } _ { { \mathrm { i f } } } \colon$ t-th reduction for object X <sub>,</sub> $\mathrm { R ^ { \prime } } _ { \mathrm { i t } } .$ t-th merged reduction for object $\mathrm { X } _ { \mathrm { i } } , \mathrm { R } _ { \mathrm { s } } \mathrm { : }$ set of merged reductions in case S, : set of valid merged reductions from $\mathsf { R } _ { \mathsf { S } } , \Omega \colon$ set of merged reductions selected from $\Theta , \mathbf { N } ^ { * }$ : minimum number of objects for the reduction required for a qualified rule, ${ \mathrm { L } } _ { 1 } ^ { \mathrm { ~ \normalfont ~ : ~ } }$ set of rules (reductions) selected from object $\mathrm { X } _ { \mathrm { i } } , \mathrm { L } _ { 2 } ^ { \mathrm { : } }$ set of qualified rules (reductions) selected from $\mathrm { L } _ { 1 } , \mathrm { A } _ { 1 } \mathrm { : }$ set of rules selected from object $\mathrm { X } _ { \mathrm { i } } , \mathrm { A } _ { 2 } \mathrm { : }$ set of qualified rules selected from $\mathbf { A } _ { 1 }$

The strength index of reduct f is defined as follows: $\begin{array} { r } { \mathrm { S I } ( f ) = \frac { 1 } { \sum _ { j = 1 } ^ { m } \frac { v _ { j } \times n _ { f } } { w _ { j } } } } \end{array}$

where: f is the reduction number, $f = 1 , . . . , n ; \nu _ { j } = 1$ if condition attribute j is selected, 0 otherwise $( A _ { j } = { } ^ { 6 6 } x ^ { 3 3 } )$ ; $n _ { f }$ is the number of identical reduction f (Object Cardinality); w<sub>f</sub> is weight.

The RSREA generates customer value rules, and the strategies are evaluated according to the results. For example, the rule, Gender=Female, Age group=Adult, Income=High, Frequency=5, Monetary =5, Platinum customers, refers to that ―Based on customer behavior attributes, Platinum customers are adult female, with high income, high visit frequency, and high consumption. They are regarded as valuable customers that theme parks would try to retain such customers.‖

<table><tr><td>Step 0. Initialization←(i) Sort reducts  $R_{it}$  by case number S.←(ii) Compute strength index SI for each reduct.←(iii) Set S = 1,  $R_S = \varnothing$ ,  $\Theta = \varnothing$ ,  $\Omega = \varnothing$ ,  $L_1 = \varnothing$ ,  $L_2 = \varnothing$ ,  $A_1 = \varnothing$ ,  $A_2 = \varnothing$ .←Step 1. If all the decision rules and alternative rules have been derived, STOP; otherwise go to Step 2.←Step 2. For each case select one reduct at a time and compare it with all reducts in remaining objects. Merge all identical reducts determined by this comparison and store them in  $R_S$ .←If  $R_S = \varnothing$ , then go to Step 6.←Step 3. Examine if each merged reduct in  $R_S$  is valid.←If SI of each merged reduct in  $R_S$  is greater than SI of each individual reduct from merged objects (except itself) in case S then the qualified merged reducts  $\in \Theta$ , go to Step 4; otherwise, select one out of the merged objects ( $X_i$ ) which contains the highest SI from its reducts and go to Step 6.←Step 4. In the set  $\Theta$ , select the reducts which contain the max value of SI to construct, select the first merged reduct  $R'_{it}$  from  $\Omega$ , update  $L_1 = L_1 \cup \{R'_{it}\}$ , and select the rest of merged reduct  $R'_{it}$  from  $\Omega$ , update  $A_1 = A_1 \cup \{R'_{it}\}$ , and eliminate the objects which construct the first merged reduct  $R'_{it}$ .←If all of the  $R_{it}$  (max value of SI) have been removed in case S, go to Step 5; otherwise, set  $R_S = \varnothing$ , and go to Step 2.←Step 5. If all of the  $R_{it}$  (max value of SI) have been removed in all of cases, go to Step 7; otherwise, set← $S = S + 1$ ,  $R_S = \varnothing$ ,  $\Theta = \varnothing$ ,  $\Omega = \varnothing$ , and go to Step 2.←Step 6. Select the  $R_{it}$  with highest SI for  $X_i$ , update  $L_1 = L_1 \cup \{R_{it}\}$ , if more than one reduct with highest SI for  $X_i$ , store the rest of reducts  $R_{it}$  in  $A_1$ , and eliminate the object  $X_i$ .←If all of the  $R_{it}$  (max value of SI) have been removed in case S, go to Step 5; otherwise, go to Step 6.←Step 7. Select the reducts which number of objects are greater than  $N^*$  from  $L_1$  and  $A_1$  to construct  $L_2$  and  $A_2$ .←Step 8. List all decision rules and alternative rules.←</td></tr></table>

Fig. 1. RSREA.

## 3.2 Early Warning System

## 3.2.1 Detection process

By inputting decision rules and the number of visitors to a theme park to Early Warning System, a well-developed theme park can be judged the decline risk through the following three steps. Step 1. Evaluation of total number of visitors: The total number of visitors in two periods is compared. Decline might appear when the total number of visitors drops too much. Step 2. Evaluation of customer proportion in different classes: Customer proportion is further compared. Decreasing proportion of common customers but increasing concession-card customers would benefit a theme park, as concession-card customers are comparatively valuable than common customers. On the contrary, decline might appear on increasing common customers, but decreasing concession-card customers. Step 3. Warning Method: The above two steps could preliminarily judge the decline of a theme park. However, such conditions merely reveal the fuzzy decline stage of a theme park, as decreasing visitors do not necessarily present decreasing profits. For this reason, Rule Comparison is applied to evaluate the actual decline of customer value and to further judge the decline risk of a theme park. Detailed explanations of Rule Comparison are presented next.

## 3.2.2 Rule Comparison

![](/api/attachments/VJDKGA3J/fulltext/images/4e219a832c34f49eee498e7a0b848827a39ed65e6de2c64cc41355684213a238.jpg)  
Fig. 2. Rule comparison structure.

Rule Comparison proposed by Chen [17] is applied in this study (Fig. 2). Rules generated at two different time points are compared with several functions in order to understand customer behaviors and the actual value, find out growing and declining loyal customers, and help theme parks invest in right customers at right time to enhance the profits and avoid decline. Five functions in Rule Comparison are used for discussing rule changes at different time points: Equ function: Comparing decision rules at two time points for both conditional attributes and decision attributes with identical decision rules. Add function: Comparing decision rules at two time points for decision rules increased at new time points. Sub function:

Comparing decision rules at two time points for decision rules decreased at new time points. Sdtra function： Comparing decision rules at two time points for decision rules with same conditional attributes but different decision attributes. Ddtra function：Comparing decision rules at two time points for decision rules with same decision attributes, where customer behavior attributes are the same while customer value attributes are changing.

Taking some examples for above 5 functions, decision rules generated at two different time points (i, i+1) are shown in Tables 2 and 3.

Table 2 Rules generated at time point i.

<table><tr><td>Rule No</td><td>Gender</td><td>Age group</td><td>Occupation</td><td>residence</td><td>Place of</td><td>Recency</td><td>Frequency</td><td>Monetary</td><td>Outcome</td></tr><tr><td>1</td><td>Male</td><td>Adult</td><td></td><td></td><td></td><td></td><td>5</td><td>5</td><td>Platinum customers</td></tr><tr><td>2</td><td>Female</td><td></td><td>Student</td><td></td><td></td><td>2</td><td>5</td><td></td><td>Common customers</td></tr><tr><td>3</td><td></td><td>Adult</td><td></td><td>Domesitc (close)</td><td></td><td></td><td>5</td><td>4</td><td>Gold customers</td></tr><tr><td>4</td><td>Male</td><td></td><td></td><td>Foreign country</td><td></td><td></td><td>4</td><td>4</td><td>Common customers</td></tr></table>

Table 3 Rules generated at time point i+1.

<table><tr><td>Rule No</td><td>Gender</td><td>Age group</td><td>Occupation</td><td>residence</td><td>Place of</td><td>Recency</td><td>Frequency</td><td>Monetary</td><td>Outcome</td></tr><tr><td>1</td><td>Male</td><td>Adult</td><td></td><td></td><td></td><td></td><td>5</td><td>5</td><td>Platinum customers</td></tr><tr><td>2</td><td>Female</td><td>Child</td><td>Early childhood</td><td></td><td></td><td></td><td></td><td></td><td>Common customers</td></tr><tr><td>3</td><td></td><td>Adult</td><td></td><td>Domestic (close)</td><td></td><td></td><td>4</td><td>3</td><td>Gold customers</td></tr><tr><td>4</td><td>Male</td><td></td><td></td><td>Foreign country</td><td></td><td></td><td>4</td><td>4</td><td>Platinum customers</td></tr></table>

According to the rules generated at different time points in above two tables, the comparison results of 5 functions in Rule Comparison are summarized as below. Equ function: From above tables, rule1 at time point i and rule1 at time point (i+1) are the same. In other words, adult male Platinum customers with Frequency=5 and Monetary=5 do not change with time. Such a result is beneficial for a theme park. Sub function: Rule2 at time point i disappears with time. A theme park might face the loss when continuously proposing marketing strategies with such a rule. Add function: Rule2 at time point (i+1) is added. Such rules require more observation as they are unstable. Sdtra function: Rule4 at time points i

# ACCEPTED MANUSCRIPT

and i+1 reveals the same conditional attributes but different decision attributes of customers. Such customers would become Platinum customers as time goes by. Apparently, the marketing strategies proposed by the theme park for such customers are successful. Ddtra function: According to rule3 at time points i and (i+1), the customer behavior attributes are the same, but the value of customer value attributes is different. Besides, the decreasing Frequency and Monetary might be a warning for a theme park.

The comparison of such 5 functions could assist a theme park in clearly realizing customer changes. Table 4 shows the comparison of 5 functions and the management implications. Based on above process, the Rule Comparison algorithms are proposed in Fig. 3

Notations: i: season index, Rule\_set(i): the seasonal decision rule set, $\mathbf { A } _ { \mathrm { c o n } }$ : the conditional attribute, $\mathbf { A } _ { \mathrm { o u t } }$ : the decision attribute, j: Rule\_set(i) rule index, k: Rule\_set(i+1) rule index, $[ \mathrm { A _ { c o n } } ] _ { \mathrm { R u ( j ) } } .$ the contribute attribute in Rule j, $[ \mathrm { A _ { o u t } } ] _ { \mathrm { R u ( j ) } } .$ the decision attribute in Rule j, $\mathrm { [ R u l e ( j ) ] _ { R u l e \_ s e t ( i ) } } \mathrm { : }$ index j rule in i season.

Table 4 Comparison of functions and the management implications.

<table><tr><td></td><td>Result</td><td>Management implication</td></tr><tr><td>Equ</td><td>Stable</td><td>Retaining high-value customers is beneficial for a theme park, showing that customer value does not decline with time. Nonetheless, the marketing results of low-class customers present the failure of the marketing strategies that improvement is necessary.</td></tr><tr><td>Add</td><td>Increase</td><td>Potential rules are added, but they are unstable and require observation.</td></tr><tr><td>Sub</td><td>Disappear</td><td>Rules are eliminated as time goes by that strategies should be changed.</td></tr><tr><td>Sdtra</td><td>Change of customers&#x27; card class</td><td>When customers change from low class to higher class, the marketing strategies for such customers are considered successful. However, the customer value might be losing when customers change from high class to lower class.</td></tr><tr><td>Ddtra</td><td>Change of customer value</td><td>Increasing customer value attributes reveals the importance of customer value to an enterprise; contrarily, the decrease shows declining customer confidence in the theme park.</td></tr></table>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Step 0 Initialization
    Set Equ, Add, Sub, Dstra, Sdtra, Ddtra = ∅
Step 1 Find the Equ, Dstra, Sdtra, Ddtra rule sets
    For m= 1 to j
    For n = 1 to k
    If [Rule(m)]$_{Rule\_set(i)}$ = [Rule(n)]$_{Rule\_set(i+1)}$
    Equ = Equ ∪ [Rule(m)]$_{Rule\_set(i)}$
    End if
    If [A$_{con}$]$_{Ru(i,j)}$ != [A$_{con}$]$_{Ru(i+1,k)}$ and [A$_{out}$]$_{Ru(i,j)}$ = [A$_{out}$]$_{Ru(i+1,k)}$
    dstra = dstra ∪ [Rule(j)]$_{Rule\_set(i)}$
    End if
    If [A$_{con}$]$_{Ru(i,j)}$ = [A$_{con}$]$_{Ru(i+1,k)}$ and [A$_{out}$]$_{Ru(i,j)}$ != [A$_{out}$]$_{Ru(i+1,k)}$
    Sdtra = Sdtra ∪ [Rule(j)]$_{Rule\_set(i)}$
    End if
    If [A$_{con}$]$_{Ru(i,j)}$ != [A$_{con}$]$_{Ru(i+1,k)}$ and [A$_{out}$]$_{Ru(i,j)}$ != [A$_{out}$]$_{Ru(i+1,k)}$
    Ddtra = Ddtra ∪ [Rule(j)]$_{Rule\_set(i)}$
    End if
    End for
    Add=Add ∪ [Rule(m)]$_{Rule\_set(i+1)}$
    Sub=Sub ∪ [Rule(m)]$_{Rule\_set(i)}$
    End for
Step 2 Find Add, Sub rule sets
    Add= Add-Equ
    Sub= Sub-Equ
Step 3 Output the Equ, Add, Sub, Dstra, Sdtra, Ddtra rule sets
</div>

Fig. 3. The Rule Comparison Algorithm.

## 4. Case Study

A globally famous Asian theme park, referred to hereafter as Park A, utilizes the cartoons and films published by the production company as the themes. Interviews with general managers of theme parks show that future customers would be mostly interested in parks with films, fantasy, and even science fiction as the themes [1, 2], making focal case advantageous over other parks featuring culture and folk. In addition to recreational facilities, regular feature activities (i.e., cartoon festival, cartoon cook, masquerade, and photo-taking with cartoon figures), specialty food and restaurants, and characteristic hotels are equipped in the theme park. Customers are also provided with options on exclusive tourism services or integrated service perceptions and a variety of souvenirs related to featured films or cartoons.

# ACCEPTED MANUSCRIPT

To permanently tie up important customers, annual concession cards are issued since early 2010 to allow card owners enjoy discounts for in-park consumption and preferential ticket in the theatre. Memberships are classified into Silver, Gold, and Platinum. Platinum cards allow free entrance in the year round, Gold cards are suitable for most days in a year, except particular holidays, and Silver cards are good for weekdays and some special weekends and holidays. Distinct discounts and concessions are offered for such three different-price cards. Fig. 4 shows the detailed information of the concession cards.

![](/api/attachments/VJDKGA3J/fulltext/images/c020276ff5f370415a285c2a85233859dd5391c450abe0165bb6b1f6e6d43b57.jpg)

99USD. 20% discount for tickets, food, shopping, hotels, and optional activities. Priority for shows in the theatre, free parking, birthday gifts and 50% discount on the day (including tickets, food, shopping, and hotels). Available for 365 days in the year.

66USD. 15% discount for tickets, food, shopping, hotels and optional activities. Free parking, birthday gifts and 35% discounts on the day (including tickets. food. shopping, and hotels). Available for Mon.-Sun, except some special holidays.

33USD. 10% discount for tickets, food, shopping, hotels, and optional activities. 50% discount for parking, birthday gifts. Available for most Mon.-Sun., except special holidays, and some specially selected weekends

Fig. 4. Yearly concession cards of the Asian theme park.

Sales of the annual concession cards are in good condition due to the large number of visitors. However, as a well-developed theme park, Park A noticed the proliferating importance of customer purchase alongside number of visits, raising below concerns:

(1) Customer classification: Because marketing resources are limited, Park A needs allocate resources according to customers’ potential of purchase since the number of visitors is increasing. In this regard, an approach to classify customers is necessary.

(2) Risk of losing customers: Card owners are important for Park A to pursuit higher customer value, but if they do not use the card often enough, they may not continue purchasing the cards, which will result to potential loss of the customer. In this case, understanding the use conditions of customers is primary for the park.

(3) Customer change detection: An approach for permanently observing customer changes is necessary for proposing long-term marketing strategies and instantaneously understanding the success of the strategies so as to avoid wrong investment in disappeared customers.

When not being able to invest large marketing resources in all visitors, Park A needs to find out valuable customers with Customer Value Analysis so that the resources could be applied to potential customers. To realize the actual behaviors of customers, Park A applies the data collection process and evaluation to acquire customer information. However, the expiration of each customer’s concession card is different. For success of strategies. Since the promotion of approach is emphasized, the data in this study are fabricated that the results could not represent the trend of real parks. The following attributes are utilized for analyzing customer value in Park A in year t:

(1) Customer behavior attributes: Gender {Male, Female}, Age {Child, Teenager, Adult, Senior}, Place of residence {Domestic (far), Domestic (close), Foreign country}, Occupation {Early childhood, Student, Military, Public and Teaching Personnel, Service Industry, Industrial, Commercial and Agricultural Industry, Entrepreneurship, Homemaker, Retirement, Unemployment}, Average personal monthly income {Low, Medium, High}.

(2) Customer Value Analysis attribute: Recency (R). The evaluation of "more than 5 months", "3\~4 months", "2\~3 months", "1\~2 months", and "less than 1 month" is rated 1\~5 sequentially. Frequency (F). The evaluation of "less than 5 times a year", "6\~10 times a year", "11\~15 times a year", "16\~20 times a year", and "more than 20 times a year" is rated 1\~5 sequentially. Monetary (M). Table 5 shows the evaluation model of the three attributes. The columns show the evaluation rating 1\~5 and the price range for each rating (Unit: US dollars).

(3) Customer satisfaction. It is divided into "facility satisfaction", "activity satisfaction", "price satisfaction", and "service satisfaction" for analyses, and is evaluated with "Extremely dissatisfactory", "Dissatisfactory", "Common", "Satisfactory", and "Extremely satisfactory", rated 1\~5. (4) Tourism imagery. Tourism imagery is divided into "Destination brand imagery", "Emotional imagery", "Entertainment imagery", and "Climate imagery", and is evaluated with "Extremely bad", "Bad", "Common", "Good", and "Extremely good", rated 1\~5.

Table 5 Evaluation of monetary.

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Souvenir consumption</td><td>No consumption</td><td>1~6.64</td><td>6.65~16.6</td><td>16.7~33.2</td><td>Above 33.3</td></tr><tr><td>Extra activity consumption</td><td>No consumption</td><td>1~36.52</td><td>36.53~73.04</td><td>73.05~109.56</td><td>Above 109.57</td></tr><tr><td>Accommodation and food</td><td>No consumption</td><td>1~33.20</td><td>33.21~166</td><td>166.01~ 311.04</td><td>Above 311.05</td></tr></table>

After collecting the aforementioned data and based on Table 1, the decision table is presented in Table 6. The weights are given by the decision makers to reflect managerial considerations. In section 4.1, the RSREA is applied to Table 6 to induct rules.

Table 6 Decision table.

<table><tr><td></td><td>Objects</td><td>Gender $^{*2}$ </td><td>Age group $^{*3}$ </td><td>Place of residence $^{*4}$ </td><td>Occupation $^{*5}$ </td><td>Marital status $^{*6}$ </td><td>monthly income $^{*7}$ </td><td>Average persona</td><td>Recency</td><td>Frequency</td><td>consumption</td><td>exu activity</td><td>food consumption</td><td>Accommodation and</td><td>Souvenir consumption</td><td>Price satisfaction</td><td>Facility satisfaction</td><td>Service satisfaction</td><td>imagery</td><td>lesunaton oratu</td><td>Climate imagery</td><td>Entertainment imagery</td><td>Results</td></tr><tr><td></td><td>Weight</td><td>.025</td><td>.025</td><td>0.25</td><td>.05</td><td>.025</td><td>0.5</td><td>0.1</td><td>0.1</td><td>0.05</td><td>0.05</td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.05</td><td>0.05</td><td>0.05</td><td></td><td></td><td></td></tr><tr><td>1</td><td></td><td colspan="4">A</td><td colspan="3">Hi</td><td colspan="2">5</td><td colspan="5">5</td><td colspan="6">5</td><td>P.C</td><td></td></tr><tr><td>2</td><td></td><td colspan="2"></td><td>E</td><td>Ma</td><td colspan="8"></td><td>5</td><td colspan="3">5</td><td colspan="4">5</td><td>P.C</td><td></td></tr><tr><td>Skip*</td><td></td><td colspan="20"></td><td>skip</td><td></td></tr></table>

<sup>\*</sup>Only the first two objects are presented since there are a huge of objects. The objects after the $3 ^ { \mathrm { r d } }$ row are will be provided upon contacting the corresponding author.

## 4.1. Analysis of situations from time point t to time point t+2

Park A senses the potential decline about time point t+1, and decides to work on stimulating total consumption. Besides strengthening collaboration with movie and cartoon producers and promoting related products, new attractions are developed for different themes and programs. More importantly, additional premium is introduced for concession cards and the customers who have purchased the cards before are offered some concessions for continuing cards so as to enhance the confidence of valuable customers as well as attract potential valuable customers to purchase concession cards. The added plans for concession cards are summarized as following:

(1) Half price for continuing the card.

(2) A friend, who does not have a concession card, of a card owner can enjoy the concession.

(3) Extended usage of the card to several appointed stores outside the park. Bonus points are offered for purchase in appointed stores, and the bonus points could be exchanged concessions in Park A.

After practicing above three strategies, Park A checks the improvement on the same day in the third year (time point t+2) and finds out the total number of visitors reaching 9 million. Following the methods introduced in section 3.2, Park A executes the steps below to understand more details of changes in customer value.

## Step 1 Comparison of total number of visitors, from time point t+1 to time point t+2

The total number of visitors increases from 6 million in the second year up to 9 million, which is 1 million more than 8 million in the first year. It is a great growth for the park. However, the comparison results of different-class proportion and customer rules are required for judging the park getting rid of decline.

Step 2 Comparison of different-class customer proportion

As shown in Table 7, the member proportion reaches 50% in the third year, the same as the proportion of Common members. It is worth mentioning that Gold members increase from 10% to 20%. Such a large rise reveals positive growth of Park A. The enhancement of customer value is further discussed.

Table 7 Proportion of visitors at time point t+1\~time point t+2.

<table><tr><td></td><td></td><td>The t year proportion</td><td>The t+1 year Proportion</td><td>The t+2 year Proportion</td></tr><tr><td>Platinum</td><td>members</td><td>10%</td><td>6%</td><td>10% (0.9 million)</td></tr></table>

## ACCEPTED MANUSCRIPT

<table><tr><td>Gold</td><td>members</td><td>12.5%</td><td>10%</td><td>20% (1.8 million)</td></tr><tr><td>Silver</td><td>members</td><td>18.75%</td><td>20%</td><td>20% (1.8 million)</td></tr><tr><td>Common</td><td>members</td><td>58.75%</td><td>61.7%</td><td>50% (4.5 million)</td></tr></table>

Step 3 Rule comparison.

Apply the RSREA to Table 6 and the total of 31 rules are generated. In this stage, these 31 rules at different time points are compared, using methods introduced in Section 3.2.2. The comparison of customer value attribute in Rule 15 at time points t, t+1, and t+2 is presented here below as an example: Rule 15 (Ddtra function of t and t+1; Sdtra function of t+1 and t+2): IF (Place of residence = D(f)) AND (Occupation = S.I) AND (Extra activity consumption = 2->3) AND (Facility satisfaction = 3->4) AND (Climate imagery = 3->4) THEN (Customer’s level = C.C-> S.C)

It is shown that customer value attributes in rule15 are changed from time point t to time point t+1 after the evolution at two time points of Ddtra (time point t\~time point t+1) and Sdtra (time point t+1\~time point t+2). Extra activity consumption was at level 2 at time point t but changes to 3 at time point t+1 (shown as ―Extra activity consumption = 2->3” in the rule). Similarly, customers’ card class changes from Common at time point t+1 to Silver at time point t+2, shown in the rule as ―Customer’s level = C.C -> S.C) to denote changes from common customer to silver customer.

Step 4 Judgment of decline trend

In comparison with time point t-time point t+1, it appears positive trend at time point t+1-time point t+2, showing that Park A makes several strategy changes when facing the decline risk at time point t+1. The outcomes reveal customers’ confidence that the number is increased and the overall effectiveness is higher

than it in the first year to get rid of the decline stage.

## 4.3 Management implication

Rule Comparison allows observing the customer rule trend in Park A from time point t to time point $t { + } 2$ . Understanding the changes of customer rules in the three years provides managers with reference to propose marketing strategies. The organized rules are classified into four categories for discussing the management implication.

## (1) Value unchanged rules (rule1\~rule7)

Customers belonging to this category are stable and exhibit no changes within the three year of observation. Rule 1 and 2 describe high-value customers, who present high loyalty and create high value for the park. Investing marketing resources on these customers may be more profitable. As shown in below Rule 1 that no attribute changes form time t to t+2, and all values in the attributes are favorable to Park A. Rule 1 (Equ function of t and t+2): IF (Age group = A) AND (Average personal monthly income\* = Hi) AND (Frequency = 5) AND (Accommodation and food consumption = 5) AND (Service satisfaction = 5)

However, customers in rule 3 and rule 4 tend not to purchase cards, rendering marketing efforts valueless. For example, as shown in below Rule 4 that no attribute changes form time t to t+2: teenager, student, and common customer throughout.

Rule 4 (Equ function of t and t+2): IF (Age group = B) AND (Occupation = S) THEN (Customer’s

$$
l e v e l = C. C)
$$

Rule5 to Rule7 describe customers who experience one change and are considered sub-stable. Take Rule 5 for example, if in either time t or t+1, the values of age group, place of residence, accommodation and food consumption, destination brand image, and climate imagery are denoted as in the rules, the customer is a Platinum customer (P.C). Similarly, customers in rule5 and rule6 show high value that they are regarded as major marketing subjects. Rule 5 (Add function of t and t+1; Equ function of t+1 and t+2): IF (Age group = A) AND (Place of residence = F.C) AND (Accommodation and food consumption = 5) AND (Destination brand imagery = 5) AND (Climate imagery = 5) THEN (Customer’s level = P.C)

## (2) Value changed rules (rule8\~rule17)

Customers in rule 8 degrade from Platinum down to Gold at time point t\~time point t+1 but upgrade to Platinum at time point t+1-time point t+2, revealing the successful strategies of the park to win customer confidence in returning value drops at time point t\~time point t+1 but enhances at time point t+1\~time point t+2, showing that the proposed card concessions attract such customers. Rule11\~13 present customers upgrading cards. Although such customers might remain the value, the customer value is enhanced due to the value of Platinum >Gold > Silver. Customer value in rule16 and rule17 also enhances after three years, but is restricted to Silver customers. The park could promote higher-class cards to such customers in order to increase the profits. Customers in rule15 upgrade both the class of cards and customer value, presenting higher value of such customers who are willing to purchase higher-class cards and become more loyal to the park. Nevertheless, customer value in rule9 and rule14 is reduced, with low interests in the park.

Particularly, customers in rule 9 are Platinum customers that it is important for managers considering to re-acquire the customer value.

## (3) Halfway disappear rules (rule18\~rule27)

Customers described by these rules are those who disappear within the three year time period. Take Rule 18 below as an example, it describes a single female customer, working in Industrial, Commercial and Agricultural Industry, consuming high level of extra activity and having high level of facility satisfaction, also having high level of climate imager. He is rated Platinum customer, but is very likely to stop visiting the park. In order to make the best use of limited marketing resources, the theme park should consider reduce promotions to such customers so as to avoid potential loss or even profit decline of the park.

Rule 18 (Sub function of t and t+1): IF (Gender = F) AND (Occupation = IACI) AND (Marital status = Si) AND (Extra activity consumption = 5) AND (Facility satisfaction = 5) AND (Climate imagery = 5) THEN (Customer’s level = P.C)

## (4) Potential value rules (rule28\~rule31)

Unlike previous three groups of rules that describe clear pattern of customers, this last group presents customers with vague behaviors. These rules were not found in time t, but appear later in time period t+1 and/or t+2. Managers have to make careful evaluation before making marketing strategies, as such rules, with merely one-year change, are comparatively unstable. It would be better to observe for few more years. Examples include Rule 31 as below that (Add function of t+1 and t+2) indicates the appearance of this rule in t+1 and t+2.

e 31 (Add function of t+1 and t+2): IF (Occupation = MPAT) AND (Marital status = Si) AND (Recency = 3) AND (Frequency = 4) AND (Accommodation and food consumption = 4) THEN (Customer’s level = S.C)

## 4.4. Discussion

Based on Customer Value Analysis in this study, Park A could understand the customer value every year and the value of customers with yearly membership cards for the decision making at the next stage. The designed Early Warning System helps the park realize the long-term trend of customer value. The possibility of customer value decline could be noticed by comparing different time points to show the early warning effect. Such an approach presents the advantages of searching current customer value without complicated numerical equation calculation and finding out the behaviors of valuable customers by matching the characteristic of Rough Set which is able to analyze qualitative data to solve the qualitative problem which could not be solved with past Customer Value Analysis.

The proposed Customer Value Analysis assists Park A in finding out target customers and applying limited marketing resources to right customers. After customers purchase yearly concession cards, the value could be evaluated to help Park A make adjustment and modification on the marketing. Finally, Early Warning System could detect the yearly number of visitors, the member proportion, and the customer value rule trend so as to avoid decline risks, instantaneously realize the success of strategies, and prevent resources from being wrongly applied to disappeared customers.

# ACCEPTED MANUSCRIPT

## 5. Conclusion

Theme parks are popular attractions for many people nowadays. Different from past amusement parks, theme parks provide services of entertainment facilities, food, accommodation, and activities, offer customers with overall perception, allow customers temporarily getting rid of pressure through the thematic climate, and integrate fantasy into the designed situations. Nonetheless, the development of theme parks has increased the number of customers. A lot of well-developed theme parks promote yearly concession cards to tie up long-term loyal customers and maintain longer consumption of customers who, with the card value, could enjoy the concessions the year round. Under limited marketing resources, a theme park could not propose equivalent marketing tactics to every customer. For this reason, a theme park would invest the marketing resources in high-value customers. Customer Value Analysis proposed in this study includes customer behavior attributes and applies several value evaluation attributes to assist theme parks in finding What is more, the proposed Early Warning System could also detect the customer value decline trend, where a theme park could understand the success of the marketing strategies through Rule Comparison so as to avoid continuously investing important marketing resources in wrong customers.

Despite our effort in adopting rough set theory to customer value analysis for theme parks, a fundamental limitation lies in how to connect customer value analysis with the fluctuation of revenue. As member card classification reflects the amount and activities of customers, further efforts are needed to see how these factors are associated with revenue increase or decline so that the warning system can be more complete for the decision making of theme parks. Besides, future research could discuss the rule change at

# ACCEPTED MANUSCRIPT

different time points in a year. For instance, tourism industry often faces the problem of high/low-peak seasons. In order to more accurately find out customer value, an information collection mechanism matched with the model to effectively collect and deal with such evaluation information for a theme park is required. Customer responses to questionnaire, including refusal and casual responses, could also be included so as to achieve the practical demand. Moreover, Sensitivity Analysis could be applied to prove the confidence of the approach.

## References

1. Milman, A. (2001).The future of the theme park and attraction industry: A management perspective. Journal of Travel Research. 40(2), p. 139-147. DOI: 10.1177/004728750104000204.

2. Tsai, C.-Y. & S.-H. Chung (2012).A personalized route recommendation service for theme parks using rfid information and tourist behavior. Decision Support Systems. 52(2), p. 514-527. DOI: http://doi.org/10.1016/j.dss.2011.10.013.

3. Butler, R. (2006). The tourism area life cycle. Vol. 1. Channel view publications.

4. Butler, R.W. (1980).The concept of a tourist area cycle of evolution: Implications for management of resources. Canadian Geographer / Le Géographe canadien. 24(1), p. 5-12. DOI: 10.1111/j.1541-0064.1980.tb00970.x.

5. Korol, T. (2013).Early warning models against bankruptcy risk for central european and latin american enterprises. Economic Modelling. 31, p. 22-30. DOI: https://doi.org/10.1016/j.econmod.2012.11.017.

6. Koyuncugil, A.S. & N. Ozgulbas (2012).Financial early warning system model and data mining

application for risk detection. Expert Systems with Applications. 39(6), p. 6238-6253. DOI: https://doi.org/10.1016/j.eswa.2011.12.021.

Asanovic, Z. (2013).Early warning models for system banking crises in montenegro. Economic and Business Review for Central and South - Eastern Europe. 15(2), p. 135-149.

8. Alessi, L. & C. Detken (2014).Identifying excessive credit growth and leverage.

9. Miglautsch, J. (2002).Application of rfm principles: What to do with 1–1–1 customers? Journal of Database Marketing & Customer Strategy Management. 9(4), p. 319-324. DOI:

10. Miglautsch, J.R. (2000).Thoughts on rfm scoring. Journal of Database Marketing & Customer Strategy Management. 8(1), p. 67-72. DOI: 10.1057/palgrave.jdm.3240019.

11. Alexandris, K., C. Kouthouris, & M. Andreas (2006).Increasing customers' loyalty in a skiing resort: The contribution of place attachment and service quality. International Journal of Contemporary Hospitality Management. 18(5), p. 414-425. DOI: 10.1108/09596110610673547.

12. Oppermann, M. (2000).Tourism destination loyalty. Journal of Travel Research. 39(1), p. 78-84. DOI: 10.1177/004728750003900110.

13. Beerli, A. & J.D. Martín (2004).Factors influencing destination image. Annals of Tourism Research. 31(3), p. 657-681. DOI: http://doi.org/10.1016/j.annals.2004.01.010.

14. Hunt, J.D. (1975).Image as a factor in tourism development. Journal of Travel Research. 13(3), p. 1-7. DOI: 10.1177/004728757501300301.

15. Huang, C.-C., et al. (2014).Rough set theory: A novel approach for extraction of robust decision rules based on incremental attributes. Annals of Operations Research. 216(1), p. 163-189. DOI: 10.1007/s10479-013-1352-1.

16. Huang, C.-C., et al. (2013).Alternative rule induction methods based on incremental object using rough set theory. Applied Soft Computing. 13(1), p. 372-389. DOI: https://doi.org/10.1016/j.asoc.2012.08.042.

17. Lin, S.-H., C.-C. Huang, & Z.-X. Che (2015).Rule induction for hierarchical attributes using a rough set for the selection of a green fleet. Applied Soft Computing. 37, p. 456-466. DOI: http://doi.org/10.1016/j.asoc.2015.08.016.

18. Manente, M. & H. Pechlaner (2006).How to define, identify and monitor the decline of tourist destinations: Towards an early warning system. The tourism area life cycle: Conceptual and theoretical issues. 2, p. 235-253.

19. Blocker, C.P. (2011).Modeling customer value perceptions in cross-cultural business markets. Journal of Business Research. 64(5), p. 533-540. DOI: 10.1016/j.jbusres.2010.05.001.

20. Kim, J., et al. (2015).The contributions of firm innovativeness to customer value in purchasing behavior. Journal of Product Innovation Management. 32(2), p. 201-213. DOI: 10.1111/jpim.12173.

21. Ulaga, W. (2011).Investigating customer value in global business markets: Commentary essay. Journal of Business Research. 64(8), p. 928-930. DOI: 10.1016/j.jbusres.2011.04.005.

22. Kim, G.-W., J. Lim, & M. Yun (2016).Analysis of consumer value using semantic network: The comparison of hierarchical and nonhierarchical value structures. Human Factors & Ergonomics in Manufacturing & Service Industries. 26(3), p. 393-407. DOI: 10.1002/hfm.20665.

23. Prahalad, C.K. & G. Hamel (1994).Strategy as a field of study: Why search for a new paradigm? Strategic Management Journal. 15(S2), p. 5-16. DOI: 10.1002/smj.4250151002.

24. Slater, S.F. & J.C. Narver (1998).Customer-led and market-oriented: Let's not confuse the two. Strategic Management Journal. 19(10), p. 1001-1006.

25. Reichheld, F.F. & T. Teal (2001). The loyalty effect: The hidden force behind growth, profits, and lasting value. Harvard Business Press.

26. Lee, S., N. Jin, & H. Lee (2014).The moderating role of water park service quality, environment, image, and food quality on perceived value and customer loyalty: A south korean case study. Journal of Quality Assurance in Hospitality & Tourism. 15(1), p. 19-43. DOI: 10.1080/1528008X.2014.855102.

27. Zeithaml, V.A., R.T. Rust, & K.N. Lemon (2001).The customer pyramid: Creating and serving profitable customers. California Management Review. 43(4), p. 118.

28. Abdolvand, N., A. Albadvi, & M. Aghdasi (2015).Performance management using a value-based customer-centered model. International Journal of Production Research. 53(18), p. 5472-5483. DOI: 10.1080/00207543.2015.1026613.

29. Khajvand, M., et al. (2011).Estimating customer lifetime value based on rfm analysis of customer purchase behavior: Case study. Procedia Computer Science. 3, p. 57-63. DOI: http://dx.doi.org/10.1016/j.procs.2010.12.011.

30. Teo, T.S.H., P. Devadoss, & S.L. Pan (2006).Towards a holistic perspective of customer relationship management (crm) implementation: A case study of the housing and development board, singapore.

Decision Support Systems. 42(3), p. 1613-1627. DOI: http://doi.org/10.1016/j.dss.2006.01.007.

31. Kim, E. & B. Lee (2007).An economic analysis of customer selection and leveraging strategies in a market where network externalities exist. Decision Support Systems. 44(1), p. 124-134. DOI: http://doi.org/10.1016/j.dss.2007.03.006.

32. Shaw, M.J., et al. (2001).Knowledge management and data mining for marketing. Decision Support Systems. 31(1), p. 127-137. DOI: http://doi.org/10.1016/S0167-9236(00)00123-8.

33. Pawlak, Z. (1982).Rough sets. International Journal of Computer & Information Sciences. 11(5), p. 341-356. DOI: 10.1007/BF01001956.

34. Flott, L.W. (2002).Customer satisfaction. Metal Finishing. 100(1), p. 58-63. DOI: http://dx.doi.org/10.1016/S0026-0576(02)80021-6.

35. Pike, S. (2002).Destination image analysis—a review of 142 papers from 1973 to 2000. Tourism Management. 23(5), p. 541-549. DOI: http://doi.org/10.1016/S0261-5177(02)00005-5.

36. Kusiak, A. (2001).Rough set theory: A data mining tool for semiconductor manufacturing. IEEE Transactions on Electronics Packaging Manufacturing. 24(1), p. 44-50. DOI: 10.1109/6104.924792.

37. Pai, P.-F. & T.-C. Chen (2009).Rough set theory with discriminant analysis in analyzing electricity loads. Expert Systems with Applications. 36(5), p. 8799-8806. DOI:

https://doi.org/10.1016/j.eswa.2008.11.012.

38. Tay, F.E.H. & L. Shen (2003).Fault diagnosis based on rough set theory. Engineering Applications of Artificial Intelligence. 16(1), p. 39-43. DOI: https://doi.org/10.1016/S0952-1976(03)00022-8.

Chun-Che Huang received his Ph.D. degree in Industrial Engineering from the University of Iowa, Iowa City, and his M.S. degree in Operations Research from Columbia University, New York, NY. He is a Professor in the Department of Information Engineering, National Chi Nan University, Taiwan and directs the Laboratory of Intelligent Systems and Knowledge Management (the ISKM Lab.). He is interested in intelligent systems, knowledge management, and data mining. He has published more than 60 research papers in journals sponsored by various societies.

# ACCEPTED MANUSCRIPT

## Highlights

 The Customer Value Analysis is demanded for the theme park to identify potential customers in tourism industry.

 This study provides an early warning system to analyze the changes of customer value.

 The aggregated approach based on Rough Set Theory and REM architectures applied.

 Providing an early correction strategy to avoid losing VIP customers.
