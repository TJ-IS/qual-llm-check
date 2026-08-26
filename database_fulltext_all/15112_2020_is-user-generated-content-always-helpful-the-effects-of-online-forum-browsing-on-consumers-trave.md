---
otero_id: 15112
otero_key: "ZJ4S2RAR"
title: "Is user-generated content always helpful? The effects of online forum browsing on consumers' travel purchase decisions"
authors: "Xianghua Lu; Shu He; Shaohua Lian; Sulin Ba; Junjie Wu"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113368"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Is user-generated content always helpful? The efects of online forum browsing on consumers' travel purchase decisions

![](/api/attachments/ZJ4S2RAR/fulltext/images/452c4a624e20cc6044a7ccaae5c3b592447503e58e150292ff13d4b413ffc4ea.jpg)

Xianghua Lu<sup>a</sup>, Shu He<sup>b,⁎</sup>, Shaohua Lian<sup>a</sup>, Sulin Ba<sup>b</sup>, Junjie Wu<sup>c</sup>

<sup>a</sup> Department of Information Management and Information Systems, Fudan University, 220 Handan Road, Shanghai 200433, China

<sup>b</sup> Department of Operations and Information Management, University of Connecticut, 2100 Hillside Rd, Storrs, CT 06269, United States of America

<sup>c</sup> Department of Information Systems, Beihang University, No. 37 Xueyuan Road, Haidian District, Beijing 100083, China

## A B S T R A C T

This study examines how the unique information environment of online forums afects consumers' information acquisitions, and further impacts their purchase behavior. Based on the information foraging theory, we hypothesize that the relevant information patches in online forums facilitate consumers' information acquisition processes and increase purchase intention. However, the mixed information scents within online forums could also lead to fewer or no purchases because of distraction from unrelated information. To test the proposed hypotheses, we empirically analyze a unique data set of consumers' webpage browsing histories and purchase behavior from a major online travel agency in China. The findings of this study provide insights into how online forum browsing behavior afects consumers purchase decisions. The findings also ofer important implications for online forum design

## 1. Introduction

Online forums have been widely introduced on e-commerce websites which serve as consumers' communication platforms during prepurchase or post-purchase periods, which is a phenomenon known as social commerce. Prior studies of social commerce suggest that participation in online forums may help develop consumers' sense of com munity [22,39,42] and increase their enjoyment [51], which can potentially afect consumers' trust, loyalty [22,28,50], and purchase intentions on e-commerce websites [14,51,53].

However, research on the informational value of online forums has been relatively scarce. Existing studies generally find consumers' online forum activities positively influence their purchase probabilities without distinguishing whether the activities are product related [55, 56, 57]. This may be partially due to the open and diverse features of online forums compared with other information sources such as online product reviews [49]. It is not an easy task to classify the online forum content. More importantly, without detailed webpage clicking data, it is dificult to identify the exact content each customer has browsed. In the current study, we try to fill this research gap by drawing upon information foraging theory (IFT) and utilizing a unique data set.

IFT suggests that the information environment of an online forum can both positively and negatively afect consumers' purchase intentions. The open information exchange on online forums ofers resources to help consumers build their knowledge of a product. Consumers frequently collect related information of a product from various open online forums. However, diverse forum pages, or information patches,<sup>1</sup> in online forums may send inconsistent signals to consumers and disturb their usual information acquisition processes. For example, a consumer's product search process may be interrupted by badly formed opinions and recommendations from other forum members [53]. Consumers may also be distracted by the social features of online forums from making a quick purchase decision [17]. Therefore, it is not straightforward to predict the efect of online forum browsing on consumers' purchase decisions.

In this study, we use clickstream data from a leading online travel agency (OTA) in China to explore how the unique information environment of online forums impacts the consumers' information acquisition activities and their subsequent purchase behavior. Specifically, we classify online forum pages into three categories: focal product forum pages, non-focal product forum pages, and product-unrelated forum pages. Focal product forum pages are mainly comprised of focal product information, which is directly related to consumers focal product decision-making. However, the other two types of forum pages mainly contain non-focal product information or information that is not directly related to any specific product (e.g., activity notification and forum administration), which we regard as “irrelevant” information in the context of this study. The three types of forum pages therefore correspond to focal product, non-focal product, and productunrelated information patches in light of the IFT. Based on this classi fication, our paper mainly focuses on two sets of browsing variables which would influence consumers' information search decisions. First, we examine consumers' browsing frequencies on three types of in formation patches defined based on their relationship with the focal product, which is known as information diet in the IFT [37]. Second, we study the information complexity of patches browsed within online forums, which captures the distributions of information patches. Then we apply a structural model to empirically test how these browsing variables afect consumers' information acquisition process and purchase decisions.

![](/api/attachments/ZJ4S2RAR/fulltext/images/f75323d092ce1c4e1989d62c35b6fb4eb048047251a5111d7d0ce0be8fac008e.jpg)  
Recursive scatter-gather information acquisition process  
Fig. 1. Integrated process of information foraging.

Our empirical analysis has the following findings: (1) Only focal product information patch browsing behavior can significantly increase consumers' purchase tendency, while browsing the other two types of online forum patches has a negative impact on purchase probability. (2) The information complexity of online forum patches browsed has an inverted U-shape efect on the purchase tendency. The results could be explained by the fact that browsing irrelevant forum information might interrupt consumers' original information acquisition processes.

This study contributes to the literature on online forums by explicitly examining how consumers' browsing behavior in online forums afects their purchase decisions based on the IFT. The findings on the value of online forum information based on individual level clickstream data can complement prior studies that mainly rely on self-reported survey data and provide a more complete picture of online forums impact on consumers' purchase decisions. Furthermore, our findings ofer important implications to e-commerce website designers on their online forum designs.

The remainder of the paper is organized as follows: In the second and third sections, we present an overview of the IFT model to our study and develop the hypotheses of this study. We describe the re search context and the data set applied in the study in the fourth sec tion. We demostrate our empirical model in the fifth section and discuss our results in the sixth section. We further conduct several robustness checks in the seventh section. In the last section, we summarize our theoretical contributions and practical implications as well as the lim itations of this research.

## 2. Theoretical background

According to existing studies [39], the reasons why consumers would like to be involved in online forums include information exchange, social support, entertainment, and socializing. Most studies on online forums have examined how the social or hedonic functions of online forums afect consumers' purchase intensions [51,53]. On the other hand, there is relatively few studies on the information value of online forums. This could be partially due to the diversity of the information in online forums which may result in information conflict. In this study, we examine the information value of online forums drawing upon the IFT to fill the research gap.

IFT is a model to describe “how strategies and technologies for in formation seeking, gathering, and consumption are adapted to the flux of information in the environment” [37]. This theory, based primarily on patch–prey relationships, examines how to find optimal patch exploitation with the restrictions of time duration and energy consumption [13,46]. Description of information foraging processes requires three key concepts: the information patch, the information scent, and the information diet [36]. An information patch is a physical and/or conceptual space in which information exists (e.g., webpages that contain the information). The information scent refers to the approximate information or cues that interact with the surroundings of provided information (e.g., textual information containing web links). The information diet denotes a set of information that has a certain per ceived value to an information seeker [36].

These three concepts have been widely used in recent research to explain the adaptive interaction between an information seeker and the information environment [24]. For example, Liu et al. [26] use the IFT to assess user interaction with content-based image retrieval. Li et al. [24] adopt the IFT to explore the relationship between product review patch provision and consumers' information diet. Berg et al. [4] investigate how consumers' cognitive and demographic factors are related to the depth and breadth of information forage.

According to the IFT, consumers' information acquisition process is structured through a series of scatter–gather processes, a recursive process, and an ecologically strategic process to acquire necessary information until the information seeker feels suficiently satisfied to make a decision, which can be displayed in the framework in Fig. 1

[21].

In this integrated process, if an information seeker has one parti cular item in mind, such as a repeat purchase item, they can skip the scatter–gather process and directly make a decision. Otherwise, the information seeker undergoes a recursive and selective information acquisition process that begins from the search page or navigation page and then scatters to several information patches to acquire essential information, depending on whether the perceived information scents match consumers' information diet. This information patch browsing may help the seeker form an interest in some specific products, which leads to a new iteration of the scatter–gather process based on these specific products. This scatter–gather process is terminated upon reaching the criteria for suficiency (e.g., if the product is good enough) or if time constraints are met, when the information seeker makes the final decision, such as making a choice, forming a consideration set, or deferring the decision.

During this recursive scatter–gather process, information seekers decisions are not only afected by their information diet, but also by the immediate environmental conditions such as information patches' ambiguity and diversity [21,24]. The information environment shapes the information scents that information seekers perceive at each stage and afects their final decision [37]. In the context of online forums, the information environment of such forums is noisier than that of other webpages. For example, unlike the well-organized information patches on product webpages, the contents of an online forum are self-developed and self-managed by consumers, which may result in conflicting opinions, open-ended topics, and jumbled product recommendations [6]. The information scents on online forums thus can be disordered and mixed and may afect consumers' subsequent information acquisition activities, which will be discussed in the next section.

## 3. Research hypotheses

Existing studies have explored the relationships between users' so cial commerce activities and their purchase probabilities from various aspects [57]. The efectiveness of information acquisition depends on whether consumers find the correct information patch during the scatter–gather foraging process. Studies show the informativeness of reviews plays an important role in reviews' impact on sales [47,48]. The nature of online forums makes it a more complicated information en vironment for consumers in this process. As a result, existing papers investigating the impact of online communities on sales generally find a positive impact without distinguishing if the content in online forums is product related [8, 54, 55, 56]. In other words, it is empirically unknown whether browsing different types of content on online forums may play diferent roles in consumers' purchase decisions. Browsing an online forum can be contributory or inefective depending on whether the information is related to consumers' information diet [1,41]. If the information matches, consumers may build up their product knowledge through browsing forums and eventually make a purchase decision. If consumers are distracted into another irrelevant information patch because of the mixed information scents from an online forum, though it won't directly afect consumers' knowledge or evaluation on the focal product, the distraction may still have a negative efect on their original search task [12]. Moreover, the information complexity of browsed patches may also influence consumers' final purchase decisions, given that information with lower complexity is easier to process and has a stronger effect on behavior [23,29].

## 3.1. Positive efects of information patch browsing in online forums

The information acquisition and processing model in Assael [2] describes multiple stages through which individuals proceed before deciding whether to purchase a product. These stages include need recognition, information searching, and alternative evaluations and comparisons. Information foraging behavior in online forums is more likely to occur after the need recognition stage, wherein consumers have an interest in specific products and are attracted by the information scent in online forums to search for additional product knowledge.

In this process, we propose that information patch browsing related to focal products has a positive efect on purchase probability. When consumers browse an information patch related to the focal product, the discussions in online forums may help consumers discover more details or other relevant content. In other words, such browsing increases the consumers' knowledge regarding product attributes, even though opinions could be conflicting. Furthermore, the increased pro duct knowledge may encourage consumers to continue their primary information acquisition process. Meanwhile, consumers are very likely to revisit the focal product's webpages to evaluate it or to compare it with competing products during this process [2], whereas revisiting the focal product's webpages could increase consumers' purchase intention.

We summarize the arguments above to form the following hy pothesis:

H1. : The browsing of focal product information patches in online forums increases the probability that a consumer will purchase a focal product

## 3.2. Negative efects of information patch browsing in online forums

Apart from information patches that are related to focal products, many information patches in online forums are irrelevant to the focal products. In particular, online forums have been described as “a mixture of fact and opinion, impression and sentiment, founded and unfounded tidbits, experiences, and even rumor' [6], and irrelevant in formation can potentially dominate relevant information. We argue that encountering irrelevant information during consumers' online forum browsing behavior may negatively afect their purchase decisions because of information distraction and information dilution.

Iselin [17] reports that the interactivity of online forums can distract consumers from their primary search processes and switch their focus to other seemingly interesting but irrelevant information patches. According to the IFT, the foraging process over a noisy information environment is less predictable because various information scents are mixed together [36]. In other words, consumers' original information search tasks can be interrupted or distracted by irrelevant information patches [16,18].

Even if an irrelevant information patch does not distract consumers from their original information acquisition process, it still has a negative dilution efect. Meyvis and Janiszewski [31] present evidence that irrelevant information systematically weakens consumers' beliefs about specific products, even though it is generally expected that irrelevant information has little efect on consumers' decision-making. Studies on social judgment define this as the information dilution efect, which indicates that adding irrelevant information to diagnostic information may lead to less extreme judgments [10,11,34]. In other words, diagnostic information is rendered less useful. Information dilution efects have several underlying mechanisms. One mechanism is the averaging hypothesis, which proposes that adding irrelevant product information reduces the weight consumers assign to the supporting information and thus weakens their intention to purchase a focal product. Another mechanism is the biased hypothesis testing perspective proposed by Meyvis and Janiszewski [311. which assumes that consumers selectively look for information that suggests the product will deliver the desired benefit, and they tend to categorize any other additional evidence as not confirmatory. Consequently, when the amount of irrelevant information increases, the proportion of disconfirmatory evidence also increases and weakens consumers' beliefs in a product's ability to de liver the desired benefit.

In the case of online forums, the browsing of non-focal product information may be hindered by both the information distraction and dilution efects. Moreover, consumers who browse non-focal product information may be exposed to alternative products. This could either increase the consideration set or reduce the attention weight that consumers assign to their focal products. Thus, from the perspective of focal product purchase, this type of browsing can have a negative efect. We propose the following hypothesis:

H2a. : Browsing non-focal product information patches in online forum reduces the probability that a consumer will purchase a focal product

During the decision period, consumers may also be distracted by an information patch that is completely irrelevant to any product. Typical examples of product-unrelated forum information are activity notification or forum administration. Although it does not redirect con sumers' attention from a focal product to alternative products, this type of browsing decreases consumers' probability of revisiting the focal product webpage, increases the proportion of disconfirmatory information, and dilutes the efects of diagnostic information (focal products related online forum pages), which also leads to fewer purchases of focal products. Thus, we make the following hypothesis:

H2b. : Browsing product-unrelated information patches in online forums reduces the probability that a consumer will purchase a focal product

## 3.3. Information complexity of online forum patches

The recursive process of information foraging may increase information complexity through not only the number of each information components but also the interrelationships among these components [9]. Kim [21] reports that an appropriate amount of information helps reduce decisional risk and uncertainty, thus leading to positive deci sion-related responses. However, when the amount of information or the information complexity (e.g., the number of information sources) exceeds a specific threshold, consumers are prone to express negative decision-related responses as a form of dissatisfaction. Thus, in the case of online forum browsing, the information complexity may also afect consumers' decision-making during the information foraging process.

Information complexity includes two things: the number of parts and the interrelationships between these parts [38]. Thus information complexity not only involves the amount but also the distribution, the correlation, and the interdependence of information, as described by Lurie [29]. One implication of the information complexity definition is that the dificulty of information processing increases with the number of attribute levels and is the highest when attribute levels occur with uniform probability [29].

Studies in psychology provide similar reasoning that high information complexity causes cognitive load through the amount of in formation processing involved [20]. Cognitive capacity is limited and higher levels of complexity degrade the quality of information processing, and afect reaction time, decision time, and decision results [3,45]. In some circumstances, information complexity even reduces motivation [3] and causes stress and anxiety among consumers [30,52], resulting in lower purchase intention or probability. Thus, we make the following hypothesis:

H3. : Once the information complexity of the patches browsed by a consumer in online forums exceeds a certain threshold, it negatively afects the purchase probability of the focal product.

## 4. Research framework and data

The research framework of this study, based on the recursive scatter–gather process of the IFT, is presented in Fig. 2. Consumers who are interested in focal products begin their information acquisition processes by browsing the web pages of these focal products through either keyword search or other types of navigation.<sup>2</sup> These processes involve the interaction between online forum browsing and focal product page browsing and result in either a purchase or no purchase.

Some consumers make purchase decisions directly after they finish browsing product pages, which is consistent with purchase processes that skip the scatter–gather process in Fig. 1. In these cases, online forums do not play a direct role in consumers' information acquisition processes. We exclude these consumers in our research. This study focuses on consumers who engaged in both product page browsing and online forum browsing, and we examine how the scatter–gather process between product information browsing and online forum browsing affects their purchase decisions.

The data were obtained from a leading OTA in China. Founded in 2006, the OTA provides both domestic and international travel packages, including group tours, self-service tours, cruises, and tickets to attractions. By the end of 2018, it had provided more than half a million tour packages and tour services to more than 11 million consumers. The data from the tourism industry are ideal for our research context because it is an information-intensive industry, and tourism products are experience goods whose quality is hard for consumers to observe in advance. Consumers rely heavily on online information acquisition and comparison to assist them in their travel-related decisionmaking [19,27]. Online forums provide a large volume of travel-related comments, opinions, and personal experiences [53] and are among the most crucial sources of information for consumers [7].

The forum of the OTA website has multiple sections which cover all kinds of travel related information. Specifically, the product-related forum pages are organized by diferent continents. In other words, consumers will post product-related contents on the corresponding continent area (e.g., experience sharing or Q&A of an American travel route in the North America area). The product-unrelated pages are organized by diferent functions (e.g., activity notification and forum administration). Similar as other online forums, consumers can freely reply to and join the discussion under the main posting.

In this study, we use international travel packages as our research focus because these travel packages are expensive and people may spend more time collecting information in online forums before they make final decisions. Other products, such as 1-day tours and tickets to attractions, are relatively easy to decide upon; thus, consumers rely less on online forums to obtain extra product information. This observation is supported by the findings of Hwang et al. [15] that international tourists widely use online travel forums to acquire product knowledge prior to making a purchase. To eliminate unnecessary noises such as price, destination, and culture, we further set our focal products as travel packages in North America.<sup>3</sup>

We obtained directly from the company all clickstream and transaction data for consumers who had visited North American product pages from June 2012 to July 2013. Overall, we have approximately 10,000 consumers' web browsing and transaction data. We organize our dataset in the following steps to meet our research objectives:

(1) Using the clickstream data, we classify all web pages into five types of information patches: focal product page browsing (P1, i.e. the North America trip pages), non-focal product page browsing (P2, i.e. other continent trip pages), focal product forum information patch browsing (B1), non-focal product forum information patch browsing (B2), and product-unrelated information patch browsing (B3). We rely on the Uniform Resource Locator (URL) to code each web page. Specifically, the URL of each product page contains the product number, by which we can easily distinguish between North American package pages and other product pages. The forum categorization information, such as continent and function names, is also embedded in the URLs of product-related forum pages so that we can diferentiate three types of forum information patches. We exclude the data from consumers who participated only in product browsing but not forum browsing.

![](/api/attachments/ZJ4S2RAR/fulltext/images/c4fdec897868ec2cbde06a5c79d6cfc97b647b2ff7a8fa5ea9fece82ee78a0b2.jpg)  
Fig. 2. Research framework based on the information scatter–gather process.

(2) Next, we define each browsing session. If the time interval between a customer's two browsing activities is longer than 30 mins, then they will be defined as two browsing sessions. We exclude consumers' browsing data after they have purchased a focal product because subsequent online forum browsing could have been mainly for providing rather than seeking information. If a consumer did not make any immediate purchase right after their browsing, we keep tracking his or her purchase behavior for two more months, assuming that the efect of consumers' browsing behavior will not be longer than this timeframe.

(3) One concern of our data is that the purchases in our time window may have been afected by browsing that occurred before our ob servation period. To address this concern, we exclude the ob servations of consumers who made purchases within the first 2 months in the data collection period.<sup>5</sup>

(4) We aggregate all clickstream data to weekly level and match the data with the consumer transaction dataset. We further expand the data into balanced weekly panel data to capture the temporal effects of each browsing session. Overall, we have 24,855 observations from 5388 unique consumers.

We use the approach proposed by Lurie [29] to compute the information entropy as a proxy of information complexity. In information theory, entropy is a general measure to evaluate the amount of information in a message, and the more complex the information is, the bigger the entropy value is. This entropy measure has been well adopted in the area of information systems [35,43]. Specifically, the entropy of a message is mathematically defined by

$$
\mathrm{BI} = - \sum_ {j = 1} ^ {3} p (B _ {j}) \log_ {2} p (B _ {j})
$$

where $B _ { j }$ is the level of information attributes (in our case, this is the browsing frequency $B _ { j } ,$ with j = 1, 2, 3) and $p ( B _ { j } )$ is the percentage of level j in a given set of alternatives. A larger information entropy value indicates more information complexity. In our case, if $\mathbf { B } \mathbf { 1 } = 1 , \mathbf { B } 2 = 0 ,$ and $\mathrm { B } 3 \ = \ 0 ,$ then $\mathrm { B I } \ = \ - ( 0 \ + \ 0 \ + \ 0 ) \ = \ 0 .$ . Similarly, if B1 = 1, $\mathbf { B } 2 = 1 ,$ , and $\mathrm { B } 3 = 0 ,$ then $~ \mathrm { B I } ~ = ~ - ( ( - 1 / 2 ) ~ + ~ ( - 1 / 2 ) ~ + ~ 0 ) = 1$

We also include several control variables in our model. In particular, $P a g e N u m _ { i t } ,$ $S e s s i o n N u m _ { i t } ,$ and $M i n u t e s _ { i t }$ (see definition in Table 1) are used to control for consumers' activeness in each week. Duration , $C o n v e r s i o n _ { i t } ,$ and PurchaseNum are used to control for consumers' historical purchase behavior until week t. Table 1 lists the descriptive statistics of all variables in this study. The correlation matrix among main variables are displayed in Table 2. We also test the VIF of each variable and none of them is larger than 10.

We first visually check the relationships between the three types of information patch browsing frequency and the purchase ratio (i.e., conversion) in Fig. 3. A higher browsing frequency in focal product forum information patch is generally accompanied by an increase in purchase ratio; however, the trend is not significant when the number of pages browsed is higher than 40. For the other two types of forum information patch browsing, we have observed a downward trend, which is consistent with hypotheses H2a and H2b.

## 5. Model development

One of the challenges in capturing the efects of online forum browsing is its temporal dynamic efect. The tourism packages considered in this study are expensive so that it may take a relatively long time and more information gathering to make a decision. Consumers may repeatedly visit product pages and online forums to search for information, and the browsing that takes place in a specific week may not induce a purchase in the same week. Therefore, we must incorporate the delayed and long-term efects of browsing on purchase decisions in our model.

## 5.1. Modelling the efect of online forum browsing

We define $E _ { i t }$ as the contemporaneous efect of online forum browsing for consumer i at time t. We define $B _ { i t }$ as the cumulative efect of online forum information for consumer i at time t. So we use the following formula to present how $B _ { i t }$ evolves over time:

$$
B _ {i t} = a B _ {i, t - 1} + E _ {i t}
$$

This formulation allows the cumulative efect of $B _ { i t }$ to carry over into future periods, subject to geometric decay at rate a. The efects of online forums accumulate over time as consumer i is exposed to additional information.

Let $x _ { i j \mathrm { t } } \mathrm { b e }$ the cumulative amount of browsing in the online forum type j by consumer i at time t. The overall contemporaneous efect based on all three types of online forum browsing is expressed by

Table 1  
Descriptive statistics of main variables.

<table><tr><td>Variables</td><td>Definition</td><td>N</td><td>Mean</td><td>S.D.</td><td>Min</td><td>Max</td></tr><tr><td>P1</td><td>The number of focal product page browsing for member i in week t</td><td>24,855</td><td>0.87</td><td>3.55</td><td>0</td><td>157</td></tr><tr><td>P2</td><td>The number of non-focal product page browsing for member i in week t</td><td>24,855</td><td>8.57</td><td>18.61</td><td>0</td><td>474</td></tr><tr><td>B1</td><td>The number of focal product forum browsing for member i in week t</td><td>24,855</td><td>0.86</td><td>6.75</td><td>0</td><td>601</td></tr><tr><td>B2</td><td>The number of non-focal product forum browsing for member i in week t</td><td>24,855</td><td>6.18</td><td>37.58</td><td>0</td><td>2,447</td></tr><tr><td>B3</td><td>The number of product unrelated forum browsing for member i in week t</td><td>24,855</td><td>6.20</td><td>25.45</td><td>0</td><td>928</td></tr><tr><td>BI</td><td>The information entropy of online forum browsing for member i in week t</td><td>24,855</td><td>0.29</td><td>0.47</td><td>0</td><td>1.585</td></tr><tr><td>Y1</td><td>Whether member i purchase focal products in week t</td><td>24,855</td><td>0.02</td><td>0.12</td><td>0</td><td>1</td></tr><tr><td>PageNum</td><td>The number of web pages browsed by member i in week t</td><td>24,855</td><td>48.93</td><td>89.03</td><td>0</td><td>2,453</td></tr><tr><td>SessionNum</td><td>The number of browsing sessions of member i in week t</td><td>24,855</td><td>14.53</td><td>61.88</td><td>0</td><td>2,678</td></tr><tr><td>Minutes</td><td>The time interval (in minutes) between the first browsing and the last browsing of member i in week t (if PageNum = 1, Minutes = 0)</td><td>24,855</td><td>2,366.200</td><td>3,146.616</td><td>0</td><td>10,079.4</td></tr><tr><td>Duration</td><td>The total number of days of member i has been on this website before week t</td><td>24,855</td><td>303.80</td><td>166.99</td><td>0</td><td>1,521</td></tr><tr><td>Conversion</td><td>the ratio between number of purchases and OTA logons of customer i before week t</td><td>24,855</td><td>0.02</td><td>0.07</td><td>0</td><td>8</td></tr><tr><td>PurchaseNum</td><td>The number of purchases of member i before week t on this website</td><td>24,855</td><td>1.77</td><td>5.66</td><td>0</td><td>388</td></tr></table>

Table 2  
The correlations of main variables.

<table><tr><td></td><td>P1</td><td>P2</td><td>B1</td><td>B2</td><td>B3</td><td>PageNum</td><td>SessionNum</td><td>Minutes</td><td>Duration</td><td>Conversion</td><td>PurchaseNum</td></tr><tr><td>P1</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>P2</td><td>0.11</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>B1</td><td>0.06</td><td>0.01</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>B2</td><td>0.01</td><td>0.03</td><td>0.22</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>B3</td><td>0.01</td><td>0.01</td><td>0.34</td><td>0.52</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PageNum</td><td>0.16</td><td>0.57</td><td>0.33</td><td>0.66</td><td>0.63</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SessionNum</td><td>0.03</td><td>0.12</td><td>0.09</td><td>0.18</td><td>0.29</td><td>0.31</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>Minutes</td><td>0.08</td><td>0.30</td><td>0.15</td><td>0.23</td><td>0.38</td><td>0.49</td><td>0.31</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>Duration</td><td>-0.03</td><td>-0.03</td><td>0.01</td><td>0.01</td><td>0.05</td><td>-0.01</td><td>0.08</td><td>0.08</td><td>1.00</td><td></td><td></td></tr><tr><td>Conversion</td><td>-0.01</td><td>-0.06</td><td>-0.02</td><td>-0.03</td><td>-0.05</td><td>-0.08</td><td>-0.04</td><td>-0.09</td><td>0.06</td><td>1.00</td><td></td></tr><tr><td>PurchaseNum</td><td>-0.03</td><td>0.04</td><td>0.00</td><td>0.00</td><td>0.01</td><td>0.12</td><td>0.05</td><td>0.05</td><td>0.04</td><td>0.08</td><td>1.00</td></tr></table>

![](/api/attachments/ZJ4S2RAR/fulltext/images/ae3eddccdff2d97d295014d03149e42d0c43dbb07143572bb5ff61d12ef11576.jpg)  
Fig. 3. Relationships between information patch browsing and purchase ratio.

$$
E _ {\mathrm{it}} = \sum_ {j = 1, 2, 3} \delta_ {j} x _ {i j t}
$$

$E _ { i t }$ varies across individuals and evolves in stages based on each individual's browsing history. A marginal efect $\delta _ { j }$ captures the separate efect of each type of online forum browsing $j ( j = 1 , 2 , 3$ to represent focal product forum browsing, non-focal product forum browsing, and product-unrelated forum browsing, respectively).

## 5.2. Modelling the efect of product page browsing

Similarly, we model the cumulative efect of product page browsing as follows:

$$
P _ {i t} = \mathrm{b} P _ {i, t - 1} + M _ {i t}
$$

$M _ { i t }$ is the contemporaneous efect of product page browsing with the

following specification:

$$
M _ {\mathrm{it}} = P V _ {1} z _ {i 1 t} + P V _ {2} z _ {i 2 t}
$$

where $\mathcal { Z } _ { i 1 t }$ is the number of focal product pages and ${ z } _ { i 2 t }$ is the number of non-focal product pages browsed by consumer i at time t. We use $P V _ { I }$ and $P V _ { 2 }$ to capture the efect of focal product page browsing and nonfocal product page browsing, respectively.

## 5.3. Purchase decision model

We model that consumers' focal product purchase decisions are influenced by product information patch browsing, online forum information patch browsing, and other control variables described above. We use a random-utility framework to model the binary response (i.e., buy or not) within each week. Specifically, for a consumer i who browsed the focal product at time t, we use Buy to denote the consumers' binary response and $u _ { i t }$ to denote the latent utility.

$$
\mathsf {b u y} _ {i t} = \left\{ \begin{array}{l l} 1, & \text { if } u _ {i t} > 0 \\ 0, & \text { if } u _ {i t} \leq 0 \end{array} \right.\tag{1}
$$

$$
u _ {\mathrm{it}} = \omega P _ {i t} + \theta \mathrm{B} _ {i t} + \alpha_ {1} B I _ {i t} + \alpha_ {2} B I _ {i t} ^ {2} + \beta_ {i} X _ {i t} + \varepsilon_ {i t}
$$

where $X _ { i t }$ (e.g., PageNum, SessionNum, Minutes, Duration, Conversion, and PurchaseNum) stands for the idiosyncratic covariates of consumer i at time t, B<sub>it</sub> is the cumulative efect of the three types of online forum browsing at time t, and $P _ { i t }$ is the cumulative efect of product page browsing at time t. The efect of the information complexity of browsing online forum patches is also included with the variable BI and its square term.

By using these equations, we obtain the log likelihood function of our model as

$$
L (a, b, \omega , \theta , \alpha , \beta , \kappa , \delta) = \sum_ {i = 1} ^ {n} (y _ {i t} * \ln b u y _ {i t} + (1 - y _ {i t}) * \ln (1 - b u y _ {i t}))\tag{2}
$$

## 6. Estimation results

## 6.1. Model comparison

In our empirical analysis, we use the quasi-Newton method to maximize the log likelihood function. The Berndt–Hall–Hall–Hausman algorithm [5] is applied to approximate the Hessian matrix.

We first compare our structural model with a basic binary regression model to see which one fits the data more accurately.<sup>6</sup> Specifically, we would like to see if it is necessary to include the sustained efects of previous browsing $( { \mathbf a } = { \mathbf b } = 0 )$ or there is no decay of the sustained efects $( \mathbf { a _ { \alpha } } = \textbf { b } = \mathbf { \beta } 1 )$ . We follow the idea of cross validation and randomly select 80% of the observations to run the estimation for all three models. Then we use the rest data to check the prediction power of each model. Table 3 lists the results of the mean absolute percentage error (MAPE) and hit rates in the training sample. The full model achieves the lowest MAPE and highest hit rates in the training sample and yields the highest prediction hit rate for our test sample, suggesting that our model outperformed the other two models in terms of data fitness and prediction.

## 6.2. Estimation results

To better interpret our estimators, we standardize all browsing variables, including online forum information patch browsing and product page browsing. Table 4 lists the estimation results with dif ferent specifications.

We first estimate the efects of product browsing without the forum browsing variables in Column (1) of Table 4, the results show that focal product browsing (P1) has a positive impact on purchase probability while non-focal product browsing does not have significant impact. Then we add online forum browsing variables to see whether the model has improved. The results are reported in Column (2) of Table 4. Based on the AIC values, it is clear that the model with online forum browsing variables fits the data much better.

In addition, the estimators show that browsing diferent types of forum information patches has various efects on consumers' purchase behavior. The estimated coeficient of focal forum information patch browsing is positive and significant, which indicates that consumers who browse focal forum information patches more frequently are more likely to make a focal product purchase. This finding supports H1. Furthermore, we conduct an elasticity analysis and find that if othe variables were held at the mean values, an increase of one standard deviation (approximately six pages) of focal product forum browsing would increase the purchase probability of the focal product by 33.74%. In addition, comparing the estimators of focal product page browsing (P1) and focal product forum browsing (B1), we can see the efect of focal product page browsing is larger, which is in line with the decision-making literature, as consumers mainly rely on product-related information to make purchase decisions, and online forums serve as an external information source with an incremental efect on the decision-making. The coeficients of non-focal forum information patch browsing and product-unrelated information patch browsing are negative and significant, which suggests that browsing these two types of forum information patches reduces the purchase probability (H2a and H2b are supported).

Table 3  
Model comparison results.

<table><tr><td></td><td>MAPE in sample</td><td>Hit Rate in sample</td><td>Hit Rate out sample</td></tr><tr><td>Full Model</td><td>0.71</td><td>22.68%</td><td>23.75%</td></tr><tr><td>a = b = 0</td><td>0.76</td><td>17.18%</td><td>16.80%</td></tr><tr><td>a = b = 1</td><td>0.94</td><td>2.06%</td><td>1.25%</td></tr></table>

More importantly, we include the quadratic term of information complexity (BI) to test the inverted U-shaped relationship between the information complexity measurement and the purchase decision. The result suggests that H3 is supported. When the information complexity level exceeds a certain threshold, its marginal efect becomes negative. This finding is consistent with the results of Schhoder et al. [40] and Sicilia and Ruiz [44]. Both studies have shown that human information processing performance increases with more information up to a threshold and then decreases sharply.

For the sustained efects of information browsing, the estimated value of a is 0.255 and b is 0.665 in Column (2), which means that keeping other variables on average, one additional online forum page browsed at t-1 will on average enhance the efects of browsing behavior on purchase at time t about 25.5%; however, the product page browsing at t-1 will lead to a 66.5% increase on the efects of product page browsing behavior on purchase at time t. This result demonstrates that the efects of online forum browsing decay much faster than those of product pages browsing.

One caveat to our results is the potential large sample p-value issue. Following the suggestions of Lin et al. [25], we have calculated the 95% confidence intervals for each estimator and present them in column (3) of Table 4. All of the main variables' confidence intervals are very close to the coeficients' values, which supports the robustness of the coeficient estimation.

## 7. Robustness checks

We conduct two robustness checks to determine whether our main results hold under diferent assumptions and settings.

## 7.1. Addressing the endogeneity of focal product forum browsing

Our observations involve two types of consumers: those who browsed both focal product pages and focal product forum pages, and those who browsed focal product pages but only non-focal product or product-unrelated forums. The first type of consumers has presented a stronger interest in focal products than that of the second type of consumers and may be more likely to purchase the focal products. It has been confirmed with our data as the first type of consumers have a higher purchase probability (2.275%) than the second type (1.853%).

To address this potential endogeneity problem, we reran our model to analyze only the consumers who browsed focal product forums (the first type of consumer). By doing this, all the consumers in our dataset were self-selected as having stronger interest in the focal product. In total, 13,328 observations are included in the robustness check. The results are presented in Table 5 and they are quite consistent with our main results, suggesting that our hypotheses still hold when we control for the self-selection problem.

Table 4 Estimation results.

<table><tr><td rowspan="3"></td><td colspan="3">Purchase</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td></tr><tr><td>Without forum browsing</td><td>Full model</td><td>Confidence interval</td></tr><tr><td>Focal product forum browsing (B1)</td><td></td><td>0.45322*** (0.05473)</td><td>(0.34595, 0.56049)</td></tr><tr><td>Non-focal product forum browsing (B2)</td><td></td><td>-0.96133*** (0.09061)</td><td>(-1.13893, -0.78374)</td></tr><tr><td>Product-unrelated forum browsing (B3)</td><td></td><td>-0.58892*** (0.07512)</td><td>(-0.73616, -0.44167)</td></tr><tr><td>Forum content decay (a)</td><td></td><td>0.25530*** (0.23539)</td><td>(0.17771, 0.35224)</td></tr><tr><td>Focal product browsing (P1)</td><td>0.21576*** (0.01298)</td><td>0.62245*** (0.05745)</td><td>(0.50985, 0.73506)</td></tr><tr><td>Non-focal product browsing (P2)</td><td>0.00169 (0.01039)</td><td>-0.37262*** (0.06218)</td><td>(-0.49448, -0.25075)</td></tr><tr><td>Product content decay (b)</td><td>0.70550*** (0.11433)</td><td>0.66453*** (0.20503)</td><td>(0.56996, 0.74751)</td></tr><tr><td>Information complexity (BI)</td><td></td><td>4.64864*** (0.11737)</td><td>(4.41861, 4.87868)</td></tr><tr><td>BI square</td><td></td><td>-5.44933*** (0.10141)</td><td>(-5.64809, -5.25057)</td></tr><tr><td>duration</td><td>0.02185 (0.01453)</td><td>-0.09666 (0.04297)</td><td>(-0.18088, -0.01244)</td></tr><tr><td>PageNum</td><td>-0.11464*** (0.03320)</td><td>0.35022** (0.11417)</td><td>(0.12644, 0.57400)</td></tr><tr><td>SessionNum</td><td>0.02592 (0.02512)</td><td>0.29231*** (0.08373)</td><td>(0.12820, 045641)</td></tr><tr><td>Minutes</td><td>0.03803 (0.03363)</td><td>-0.38166*** (0.10970)</td><td>(-0.59666, -0.16665)</td></tr><tr><td>Conversion</td><td>-0.00577 (0.01374)</td><td>0.02391 (0.01707)</td><td>(-0.00955, 0.05736)</td></tr><tr><td>PurchaseNum</td><td>-0.00357 (0.01359)</td><td>0.05221 (0.02464)</td><td>(0.00391, 0.10052)</td></tr><tr><td>Sample Size</td><td>19,930</td><td>19,930</td><td></td></tr><tr><td>LogLikelihood</td><td>-13,592.14</td><td>-1,944.55</td><td></td></tr><tr><td>AIC</td><td>27,204.45</td><td>3,906.28</td><td></td></tr></table>

Standard errors in parentheses: $^ { * * } p \ < \ . 0 1 , ^ { * * } p \ < \ . 0 5 .$

Table 5  
Estimation results for self-selected consumers.

<table><tr><td></td><td>Coefficient</td></tr><tr><td>Focal product forum browsing (B1)</td><td>0.15976*** (0.02472)</td></tr><tr><td>Non-focal product forum browsing (B2)</td><td>-0.17734*** (0.01484)</td></tr><tr><td>Product-unrelated forum browsing (B3)</td><td>-0.16939*** (0.02198)</td></tr><tr><td>Forum content decay (a)</td><td>0.86383*** (0.39741)</td></tr><tr><td>Focal product browsing (P1)</td><td>0.80634*** (0.04789)</td></tr><tr><td>Non-focal product browsing (P2)</td><td>-0.55022*** (0.07742)</td></tr><tr><td>Product content decay (b)</td><td>0.35869** (0.18761)</td></tr><tr><td>Information complexity (BI)</td><td>1.27570*** (0.10298)</td></tr><tr><td>BI square</td><td>-5.34109*** (0.12263)</td></tr><tr><td>Control Variables</td><td>included</td></tr><tr><td>Sample Size</td><td>13,328</td></tr><tr><td>Log Likelihood</td><td>-1,158.37</td></tr></table>

Standard errors in parentheses: $\ast * * _ { \mathrm { ~ p ~ } } < \mathrm { ~ . 0 1 , ~ } ^ { * * } \mathrm { ~ p ~ } < \mathrm { ~ . 0 5 . ~ }$

## 7.2. Replacement the 2-month censor period with a 1-month period

In our data cleaning process, if a consumer did not make a purchase within 2 months after the initial focal product page browsing, the customer's data are not included in our analysis (right censor). We also excluded consumers who made purchases within the first 2 months in our dataset to address the missing data problem (initial period cutting). In this robustness check, we first replace the 2-month censor period with 1 month for the right censor, then replace the first 2-month threshold with 1 month for the initial period cutting, and at last replace both thresholds. Table 6 displays the estimation results using these three new datasets. The results are qualitatively equivalent to our main results.

Standard errors in parentheses: $^ { * * } p \ < \ . 0 1 , ^ { * * } p \ < \ . 0 5 .$

## 8. Conclusion

This study empirically investigates how information foraging behavior in online forums afects consumers' purchase decisions. We examine the efects of two information foraging measurements, the browsing frequency of the three types of information patches and the information complexity of patches, on consumers' purchase decisions. Our results indicate that only focal product online forum information patch browsing significantly increases purchase probability, and the information complexity of online forum patch browsing has an inverted U-shape efect on purchase behavior. The findings of our study ofer several important implications for research and practice.

## 8.1. Theoretical implications

First, this study contributes to the literature on online forums by explicitly examining the information browsing value, which has been less thoroughly investigated than the influence of the social and hedonic value. We introduce the IFT to explore how the unique information environment of online forums impacts the consumers' consequent information acquisition activities and eventually their purchase behavior. Based on the IFT, we reveal that the information value of online forums is double-edged. The findings provide a new perspective to understand the impact of online forums on purchase decisions.

Second, we investigate the information value of online forums with individual level clickstream data. The findings complement prior studies which mainly rely on self-reported survey data. In particular, our empirical model captures the browsing accumulation and decay efects, which allows us to test the information value of online browsing with a more realistic setting.

Third, our research contributes to the clickstream-based literature by analyzing the interaction between consumers' product page browsing and online forum browsing in the same decision period. Traditional clickstream studies have focused on the shopping decision from product search to purchase [32.33]. Few studies have disentangled online forum browsing from the overall process and examined its specific efect on product purchase. This study separates the browsing of online forums from that of product pages, which enables us to compare these diferent types of browsing behavior. We reveal that product page browsing has a significantly stronger efect than online forum browsing in terms of encouraging consumers to make purchases, and the efects of product browsing weaken more slowly than those of online forum browsing.

Table 6  
Estimation results when the cutof point was shortened.

<table><tr><td></td><td>1-month right censored</td><td>1-month initial cutting</td><td>1-month threshold for both cases</td></tr><tr><td>Focal product forum browsing (B1)</td><td>0.22899*** (0.04468)</td><td>0.11518*** (0.01695)</td><td>0.19335*** (0.02862)</td></tr><tr><td>Non-focal product forum browsing (B2)</td><td>-0.22581*** (0.04522)</td><td>-0.07906*** (0.01640)</td><td>-0.25411*** (0.05962)</td></tr><tr><td>Product-unrelated forum browsing (B3)</td><td>-0.27608*** (0.02464)</td><td>-0.22673*** (0.01410)</td><td>-0.22121*** (0.02779)</td></tr><tr><td>Forum content decay (a)</td><td>0.80102*** (0.39480)</td><td>0.90327*** (0.34672)</td><td>0.79773** (0.42073)</td></tr><tr><td>Focal product browsing (P1)</td><td>0.94464*** (0.04391)</td><td>0.83275*** (0.03667)</td><td>0.90853*** (0.04058)</td></tr><tr><td>Non-focal product browsing (P2)</td><td>-0.59575*** (0.06908)</td><td>-0.6136*** (0.05976)</td><td>-0.67178*** (0.06764)</td></tr><tr><td>Product content decay (b)</td><td>0.29208*** (0.15812)</td><td>0.39844*** (0.12303)</td><td>0.25726*** (0.16225)</td></tr><tr><td>Information complexity (BI)</td><td>2.64117*** (0.08784)</td><td>3.77424*** (0.08568)</td><td>2.2326*** (0.07577)</td></tr><tr><td>BI square</td><td>-5.17013*** (0.10178)</td><td>-5.5275*** (0.09078)</td><td>-5.3107*** (0.10030)</td></tr><tr><td>Control Variables</td><td>Included</td><td>Included</td><td>Included</td></tr><tr><td>Sample Size</td><td>17,203</td><td>27,580</td><td>18,837</td></tr><tr><td>Log Likelihood</td><td>-1,613.11</td><td>-2,114.92</td><td>-1,692.78</td></tr></table>

## 8.2. Managerial implications

Our research also has substantial implications for e-commerce websites that are leveraging social commerce to boost sales.

First, online forums are double-edged swords in terms of encouraging purchases. The findings of this study provide insights into how online forum browsing afects consumers' purchase behavior and aid e commerce website managers in optimizing their websites' designs. For example, given that focal product forum browsing has a positive efect on the purchase probability, including links to focal product online forums on focal product pages can increase sales. However, links to other product forums or product-unrelated content should not be en couraged because they could reduce the purchase probability.

Second, we find that consumers who choose to browse focal product online forum content have significantly higher purchase ratios than those who do not. This may assist website managers in diferentiating between consumers who are genuinely interested in purchasing a product and those who are randomly visiting product pages. Companies can target the first type of consumers with more specific promotions to increase their purchase probability.

## 8.3. Limitations and future directions

Certain limitations of our work provide research opportunities for future studies. First, because of the clickstream data's limitation, we are not able to identify consumers' detailed behavior in online forums. For example, we are unable to recognize whether browsing behavior involved posting or reading a message. Future studies with more detailed information could do analysis at a more granular level. Second, it is highly likely that external information search that occurred on other tourism websites may affect consumers' purchase decisions on the focal website. However, our single-website dataset prevents us from obser ving whether consumers engaged in browsing other websites at the same time. Third, our empirical conclusions are based on users' North America travel package purchase activities, which may not hold for less expensive travel products or products in other industries where con sumers may not have the need for extensive information gathering. Future studies could potentially analyze data from other markets such as automobiles and electronics, where online forums also play an important role in users' purchase decision, to validate if the results can be generalized. Investigations into these topics could further elaborate the efects of online forums and enhance the understanding of this field.

## Acknowledgments

The authors would like to thank the Editor and the three anonymous reviewers for their thoughtful reviews and constructive suggestions during the review process. The authors also acknowledge the support of the National Natural Science Foundation of China (Project 71872050, 91746302, 71229101).

## References

[1] I. Arsal, The influence of electronic word of mouth in an online travel community on travel decisions: a case study, (2008).

[2] H. Assael, Consumer behavior and marketing action, Kent Pub, Co, 1984

[3] K. Baldacchino, C. Armistead, D. Parker, Information overload: It's time to face the problem, Manag, Sery, 46 (4) (2002) 18–19.

[4] B. Berg, A.C. Stylianou, R.A. Mezei, Information Foraging—A Model for Exploration Breadth and Depth, Inf. Syst. Manag. 35 (2) (2018) 161–180.

[5] E.R. Berndt, B.H. Hall, R.E. Hall, J.A. Hausman, Estimation and inference in nonlinear structural models, Annals of Economic and Social Measurement, 3 1974, pp. 653–665 number 4.

[6] P. Blackshaw. Consumer-generated media (CGM) 101: Word-of-mouth in the age of the web-fortified consumer, (2004) http://www.nielsen-online.com/downloads/us/ buzz/nbzm wp CGM101 pdf

[7] D. Buhalis, R. Law, Progress in information technology and tourism management: 20 years on and 10 years after the Internet—The state of eTourism research, Tour. Manag. 29 (4) (2008) 609–623.

[8] A.F. Colladon, B. Guardabascio, R. Innarella, Using social network and semantic analysis to analyze online travel forums and forecast tourism demand, Decis. Support, Syst, 123 (2019) 113,075.

[9] R.L. Daft, N.B. Macintosh, A tentative exploration into the amount and equivocality of information processing in organizational work units, Adm. Sci. Q. (1981) 207-224.

[10] C.K. De Dreu, V.Y. Yzerbyt, J.P. Leyens, Dilution of stereotype-based cooperation in mixed-motive interdependence,J. Exp. Soc, Psychol. 31 (6) (1995) 575–593

[11] S. Fein, J.L. Hilton, Attitudes toward groups and behavioral intentions toward individual group members: The impact of nondiagnostic information, J. Exp. Soc. Psychol. 28 (2) (1992) 101–124.

[12] D. Fodness, B. Murray, A typology of tourist information search strategies, J. Travel Res. 37 (2) (1998) 108–119.

[13] L.A. Giraldeau, T. Caraco, Social foraging theory, Princeton University Press, 2018.

[14] N. Hajli, Social commerce constructs and consumer's intention to buy, Int. J. Inf Manag. 35 (2) (2015) 183–191.

[15] Y.H. Hwang, D. Jani, H.K. Jeong, Analyzing international tourists’ functional information needs: A comparative analysis of inquiries in an on-line travel forum, J. Bus, Res, 66 (6) (2013) 700–705.

[16] S.T. Iqbal, B.P. Bailey, Oasis: A framework for linking notification delivery to the perceptual structure of goal-directed tasks, ACM Trans. Comput. Human Interaction (TOCHI) 17 (4) (2010) 15.

[17] E. Iselin. The impact of information diversity on information overload effects ir unstructured managerial decision making, J. Inf, Sci, 15 (3) (1989) 163–173.

[18] J.L, Jenkins. B.B. Anderson, A. Vance. C.B. Kirwan, D. Eargle. More harm than good? How messages that interrupt can make us vulnerable. Inf, Syst. Res. 27 (4) (2016) 880–896.

[19] S.H. Jun, C.A. Vogt, K.J. MacKay, Relationships between travel information search and travel product purchase in pretrip contexts, J. Travel Res. 45 (3) (2007) 266-274.

[20] D. Kahneman, Attention and effort, 1063 Prentice-Hall, Englewood Cliffs, NJ, 1973

[21] W. Kim, Consumers as inforagers: Ecological information foraging under information overload paradigm-an integrative perspective between Darwinismand non-Darwinism. Temple University. 2014

[22] W.G. Kim, C. Lee, S.J. Hiemstra, Effects of an online virtual community on custome lovalty and travel product purchases, Tour. Manag, 25 (3) (2004) 343–355.

[23] B.K. Lee, W.N. Lee, The efect of information overload on consumer choice quality in an on-line environment, Psychol. Mark. 21 (3) (2004) 159–183.

[24] M.X. Li, C.H. Tan, K.K. Wei, K.L. Wang, Sequentiality of Product Review Information Provision: An Information Foraging Perspective, MIS Q. 41 (3) (2017) 867-892.

[25] M. Lin, H.C. Lucas Jr., G. Shmueli, Research commentary—too big to fail: large samples and the p-value problem, Inf. Syst. Res. 24 (4) (2013) 906–917

[26] H. Liu, P. Mulholland, D. Song, V. Uren, S. Rüger, Applying information foraging theory to understand user interaction with content-based image retrieval. Proceedings of the third Symposium on Information Interaction in Context. ACM 2010, August, pp. 135–144.

[27] A.C.C. Lu, B.T. Chen, Information search behavior of independent travelers: A cross cultural comparison between Chinese, Japanese, and American travelers, J. Hosp. Mark, Manag, 23 (8) (2014) 865–884

[28] X. Lu, C.W. Phang, J. Yu, Encouraging participation in virtual communities through usability and sociability development: An empirical investigation, ACM SIGMIS Database 42 (3) (2011) 96–114.

[29] N.H. Lurie, Decision making in information-rich environments: The role of information structure, J. Consum. Res. 30 (4) (2004) 473–486.

[30] N.K. Malhotra, Reflections on the information overload paradigm in consumer decision making, J. Consum. Res. 10 (4) (1984) 436–440.

[31] T. Meyvis, C. Janiszewski, Consumers' beliefs about product benefits: The efect of obviously irrelevant product information, J. Consum. Res. 28 (4) (2002) 618–635.

[33] A.L. Montgomery, S. Li, K. Srinivasan, J.C. Liechty, Modelling online browsing and path analysis using clickstream data, Mark. Sci. 23 (4) (2004) 579–595.

[34] R.E. Nisbett, H. Zukier, R.E. Lemley, The dilution efect: Nondiagnostic information weakens the implications of diagnostic information, Cogn. Psychol. 13 (2) (1981) 248–277.

[35] D.E. O’Leary, Empirical analysis of the evolution of a taxonomy for best practices, Decis. Support. Syst. 43 (4) (2007) 1650–1663.

[36] P. Pirolli, Information foraging theory: Adaptive interaction with information, Oxford University Press, 2007.

[37] P. Pirolli, S. Card, Information foraging, Psychol. Rev. 106 (4) (1999) 643.

[38] Yuri Ravdugin, Handbook of Research on Leveraging Risk and Uncertainties for Effective Project Management, IGI Global (2017) 1–504.

[39] C.M. Ridings, D. Gefen, Virtual community attraction: Why people hang out online, J. Comput.-Mediat. Commun. 10 (1) (2004) JCMC10110.

[40] H.M. Schhoder, M.J. Driver, S. Streukert, Human information processing: in dividuals and groups functioning in complex social situations, (1967).

[41] R. Sen, R.C. King, M.J. Shaw, Buvers' choice of online search strategy and its managerial implications, J. Manag. Inf. Syst. 23 (1) (2006) 211–238.

[42] H.P. Shih, K.H. Lai, T.C.E. Cheng, Informational and relational influences on elec tronic word of mouth: An empirical study of an online consumer discussion forum, Int. J. Electron. Commer. 17 (4) (2013) 137–166.

[43] Shin, Donghyuk, Shu He, Gene Moo Lee, Andrew B. Whinston, Suleyman Cetintas, and Kuang-Chih Lee. Enhancing social media analysis with visual data analytics: a deep learning approach. Forthcoming at MIS Quarterly (2019).

[44] M. Sicilia, S. Ruiz, The effects of the amount of information on cognitive responses in online purchasing tasks, Electron, Commer, Res, Appl, 9 (2) (2010) 183–191.

[45] S. Spiekermann, J. Korunovska, The importance of interface complexity and entropy for online information sharing, Behav. Inform. Technol. 33 (6) (2014) 636–645.

[46] D.W. Stephens, J.R. Krebs, Foraging theory, Princeton University Press, 1986

[47] X. Sun, M. Han, J. Feng, Helpfulness of online reviews: Examining review informativeness and classification thresholds by search products and experience products, Decis. Support. Syst. 124 (2019) 113,099.

[48] S.P. Eslami, M. Ghasemaghaei, K. Hassanein, Which online reviews do consumers find most helpful? A multi-method investigation, Decis. Support. Syst. 113 (2018) 32–42.

[49] Y. Wang, D.R. Fesenmaier. Towards understanding members' general participation in and active contribution to an online travel community, Tour, Manag, 25 (6) (2004) 709–722.

[50] C.W. Phang, C.H. Tan, J. Sutanto, F. Magagna, X. Lu, Leveraging O2O commerce for product promotion: an empirical investigation in Mainland China. JEEE Trans. Eng Manag, 61 (4) (2014) 623–632

[51] J.J. Wu, Y.S. Chang, Towards understanding members’ interactivity, trust, and flow in online travel community, Ind. Manag. Data Syst. 105 (7) (2005) 937–954.

[52] R.S. Wurman, Information anxiety (No. 302.234 WUR. CIMMYT.), (2001)

[53] Z. Xiang, U. Gretzel, Role of social media in online travel information search, Tour. Manag, 31 (2) (2010) 179–188

[54] W. Zhou, W. Duan, An empirical study of how third-party websites influence the feedback mechanism between online word-of-mouth and retail sales, Decis. Support. Syst. 76 (2015) 14–23.

[55] K.Y. Goh, C.S. Heng, Z. Lin, Social media brand community and consumer behavior: Quantifying the relative impact of user-and marketer-generated content, Inf. Syst. Res. 24 (1) (2013) 88–107.

[56] R. Rishika, A. Kumar, R. Janakiraman, R. Bezawada, The efect of customers' social media participation on customer visit frequency and profitability: an empirica investigation, Inf, Syst, Res, 24 (1) (2013) 108–127.

[57] K.Z. Zhang, M. Benyoucef, Consumer behavior in social commerce: A literature review, Decis. Support. Syst. 86 (2016) 95–108

Xianghua Lu is a professor in the Department of Information Management and Information Systems, School of management, Fudan University, Shanghai. She received her Ph.D degree from Fudan University, China. Her research interests include Internet Marketing, E-commerce and IT management. Her research work has been published in academic journals such as Management Science, Journal of Marketing, Marketing Science, Information Systems Research, Journal of Management Information System and other academic journals.

Shu He is an assistant professor at the Department of Operations and Information Management, School of Business, University of Connecticut. She earned her Ph.D. in Economics from the University of Texas at Austin. Dr. He’s research interests include social media, platform, online advertising, cyber security. Her work has appeared in Information Systems Research, MIS Quarterly, and Journal of Management Information Systems. She has received a National Science Foundation grant to support her research

Shaohua Lian is a Ph.D candidate in the Department of Information Management and Information Systems, School of management, Fudan University, Shanghai. His research interests include Internet Marketing, E-commerce and IT management. His research work has been published in academic journals such as Decision Support Systems.

Sulin Ba is a professor of Information Systems at the School of Business at the University of Connecticut and holds the Treibick Family Endowed Chair. She received her Ph.D. from the University of Texas at Austin. She has published in Management Science, Information Systems Research, MIS Quarterly, Journal of Management Information Systems, Production and Operations Management, Decision Support Systems, and other academic journals. She is a recipient of the prestigious Best Information Systems Publications Award (2010) (given by the Association for Information Systems and its Senior Scholars Consortium) and Year 20o0 MIS Ouarterly Best Paper Award, She is a senior editor for Production and Operations Management. She also serves on the editorial board of Decision Support Systems.

Junjie Wu is a professor in the Department of Information Systems. School of Economics and Management, Beihang University, China. He received his Ph.D degree from Tsinghua University, China. His area of research is data mining and complex networks, with a special interest in solving the problems raised from the emerging data-intensive appli cations. His research work has been published in academic journals and conferences such as Information Systems Research. KDD. ICDM. DMKD. TKDE. TFS, and TSMCB
